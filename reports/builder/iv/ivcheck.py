import json, math, sys, time, datetime as dt, urllib.request
# IV check for Ricky's rules. Usage: python3 ivcheck.py AVGO AMZN ...  (prints one JSON object per ticker)
# Allowed expiries: 7-60 DTE from today and ending before the next report (after-close reports allow that day's expiry).
# IV = at-the-money Black-Scholes IV (call/put mid average) on the allowed expiry nearest 30 days; HV = 20-day from closes.
# Verdict: IV/HV < 1.0 Cheap, < 1.5 Normal, else Expensive; Blocked when every allowed expiry runs into earnings.
HDR = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
TODAY = dt.date.today()
R = 0.0385
OVERRIDE = {"SKHY": ("2026-10-27", "AMC")}


def get(u):
    for a in range(3):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=HDR), timeout=30))["data"]
        except Exception as e:
            err = e
            time.sleep(2)
    raise err


def num(x):
    try:
        return float(str(x).replace("$", "").replace(",", ""))
    except Exception:
        return None


def N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs(S, K, T, s, call):
    d1 = (math.log(S / K) + (R + s * s / 2) * T) / (s * math.sqrt(T)); d2 = d1 - s * math.sqrt(T)
    return S * N(d1) - K * math.exp(-R * T) * N(d2) if call else K * math.exp(-R * T) * N(-d2) - S * N(-d1)


def iv(p, S, K, T, call):
    lo, hi = 0.01, 5.0
    if not (bs(S, K, T, lo, call) < p < bs(S, K, T, hi, call)):
        return None
    for _ in range(100):
        m = (lo + hi) / 2
        lo, hi = (lo, m) if bs(S, K, T, m, call) > p else (m, hi)
    return (lo + hi) / 2


def earnings(t):
    if t in OVERRIDE:
        nd, tm = OVERRIDE[t]
        nd = dt.date.fromisoformat(nd)
    else:
        nd, tm = None, ""
        try:
            d = get(f"https://api.nasdaq.com/api/analyst/{t}/earnings-date")
            txt = (d or {}).get("announcement") or ""
            if ":" in txt:
                nd = dt.datetime.strptime(txt.split(":", 1)[1].strip(), "%b %d, %Y").date()
            rt = ((d or {}).get("reportText") or "").lower()
            tm = "AMC" if "after market close" in rt else "BMO" if "before market open" in rt else ""
        except Exception:
            pass
    if nd and nd < TODAY:
        nd = None
    last = None
    try:
        rows = get(f"https://api.nasdaq.com/api/company/{t}/earnings-surprise")["earningsSurpriseTable"]["rows"]
        last = max(dt.datetime.strptime(r["dateReported"], "%m/%d/%Y").date() for r in rows)
    except Exception:
        pass
    return nd, tm, last


for t in sys.argv[1:]:
    try:
        rows = get(f"https://api.nasdaq.com/api/quote/{t}/historical?assetclass=stocks&fromdate={TODAY - dt.timedelta(days=50)}&todate={TODAY}&limit=60")["tradesTable"]["rows"]
        h = sorted((dt.datetime.strptime(r["date"], "%m/%d/%Y").date(), num(r["close"])) for r in rows)[-21:]
        S = h[-1][1]
        lr = [math.log(h[i][1] / h[i - 1][1]) for i in range(1, len(h))]
        m = sum(lr) / len(lr)
        hv = math.sqrt(sum((x - m) ** 2 for x in lr) / (len(lr) - 1)) * math.sqrt(252) * 100
        nd, tm, last = earnings(t)
        ch = get(f"https://api.nasdaq.com/api/quote/{t}/option-chain?assetclass=stocks&limit=1000&fromdate={TODAY}&todate={TODAY + dt.timedelta(days=62)}&money=at")
        exps, cur = {}, None
        for r in ch["table"]["rows"]:
            if r["expirygroup"]:
                cur = dt.datetime.strptime(r["expirygroup"], "%B %d, %Y").date(); continue
            k, cb, ca, pb, pa = (num(r[x]) for x in ("strike", "c_Bid", "c_Ask", "p_Bid", "p_Ask"))
            if None in (k, cb, ca, pb, pa) or ca <= 0 or pa <= 0:
                continue
            exps.setdefault(cur, []).append((k, (cb + ca) / 2, (pb + pa) / 2, (ca - cb) + (pa - pb)))
        res = {}
        for e, xs in exps.items():
            k, c, p, sp = min(xs, key=lambda x: abs(x[0] - S))
            T = max((e - TODAY).days, 1) / 365
            v = [x for x in (iv(c, S, k, T, True), iv(p, S, k, T, False)) if x]
            res[e] = dict(k=k, straddle=c + p, move=(c + p) / S * 100, iv=sum(v) / len(v) * 100 if v else None, wide=sp / (c + p) > 0.15)
        ok = [e for e in res if 7 <= (e - TODAY).days <= 60 and res[e]["iv"] and (not nd or e < nd or (e == nd and tm == "AMC"))]
        b = min(ok, key=lambda e: abs((e - TODAY).days - 30)) if ok else None
        o = dict(t=t, close=S, hv=round(hv, 1), earn=nd.isoformat() if nd else None, earnTime=tm, earnLast=last.isoformat() if last else None)
        if b:
            ratio = res[b]["iv"] / hv
            o.update(verdict="Cheap" if ratio < 1 else "Normal" if ratio < 1.5 else "Expensive", iv=round(res[b]["iv"], 1),
                     ratio=round(ratio, 2), exp=b.isoformat(), dte=(b - TODAY).days, wide=res[b]["wide"])
        else:
            o.update(verdict="Blocked")
        o["hvHasEarnings"] = bool(last and last >= h[0][0])
        if nd and (nd - TODAY).days <= 28:
            post = [e for e in sorted(res) if e > nd or (e == nd and tm == "BMO")]
            if post:
                x = res[post[0]]
                o["earnMove"] = dict(exp=post[0].isoformat(), pct=round(x["move"], 1), dollars=round(x["straddle"], 2), strike=x["k"])
        print(json.dumps(o))
    except Exception as e:
        print(json.dumps(dict(t=t, verdict="Error", error=str(e)[:120])))
    sys.stdout.flush()
    time.sleep(0.3)
