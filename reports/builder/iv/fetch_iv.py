# Pulls Nasdaq delayed option chains (as of the last close in pdf/hist.json) for all names. Run: python3 iv/fetch_iv.py <builder folder> and computes:
#  - ATM implied volatility for the expiry nearest 30 days (Black-Scholes, call/put average)
#  - 20-day historical volatility from official closes
#  - IV/HV verdict, and the straddle-implied move to the first expiry after next earnings
import json, math, sys, time, datetime as dt, urllib.request

ROOT = sys.argv[1]
sys.path.insert(0, ROOT + "/rep")
import content as C

H = json.load(open(ROOT + "/pdf/hist.json"))
PX = {t["ticker"]: t for t in json.load(open(ROOT + "/p2/final/prices/latest.json"))["tickers"]}
K = json.load(open(ROOT + "/rep/consensus.json"))
ASOF = dt.date.fromisoformat(max(r[-1][0] for r in H.values()))
R = 0.0385
HDR = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}


def ncdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def bs(S, K_, T, s, call):
    d1 = (math.log(S / K_) + (R + s * s / 2) * T) / (s * math.sqrt(T))
    d2 = d1 - s * math.sqrt(T)
    if call:
        return S * ncdf(d1) - K_ * math.exp(-R * T) * ncdf(d2)
    return K_ * math.exp(-R * T) * ncdf(-d2) - S * ncdf(-d1)


def iv(price, S, K_, T, call):
    lo, hi = 0.01, 5.0
    if price <= bs(S, K_, T, lo, call) or price >= bs(S, K_, T, hi, call):
        return None
    for _ in range(100):
        m = (lo + hi) / 2
        if bs(S, K_, T, m, call) > price:
            hi = m
        else:
            lo = m
    return (lo + hi) / 2


def f(x):
    try:
        return float(str(x).replace(",", ""))
    except Exception:
        return None


def chain(t):
    u = f"https://api.nasdaq.com/api/quote/{t}/option-chain?assetclass=stocks&limit=1000&fromdate={ASOF + dt.timedelta(days=1)}&todate={ASOF + dt.timedelta(days=62)}&money=at"
    for a in range(3):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=HDR), timeout=30))["data"]
        except Exception as e:
            err = e
            time.sleep(2)
    raise err


def hv20(t):
    c = [r[1] for r in H[t]][-21:]
    r = [math.log(c[i] / c[i - 1]) for i in range(1, len(c))]
    m = sum(r) / len(r)
    return math.sqrt(sum((x - m) ** 2 for x in r) / (len(r) - 1)) * math.sqrt(252)


out = {}
for _, _, names in C.LISTS:
    for t in names:
        S = H[t][-1][1]
        try:
            d = chain(t)
        except Exception as e:
            print("FAIL", t, e); continue
        exps = {}
        cur = None
        for r in d["table"]["rows"]:
            if r["expirygroup"]:
                cur = dt.datetime.strptime(r["expirygroup"], "%B %d, %Y").date(); continue
            k = f(r["strike"])
            cb, ca, pb, pa = f(r["c_Bid"]), f(r["c_Ask"]), f(r["p_Bid"]), f(r["p_Ask"])
            if None in (k, cb, ca, pb, pa) or ca <= 0 or pa <= 0:
                continue
            exps.setdefault(cur, []).append(dict(k=k, c=(cb + ca) / 2, p=(pb + pa) / 2, cs=(ca - cb), ps=(pa - pb)))
        res = {}
        for e, rows in sorted(exps.items()):
            a = min(rows, key=lambda x: abs(x["k"] - S))
            T = (e - ASOF).days / 365
            ic, ip = iv(a["c"], S, a["k"], T, True), iv(a["p"], S, a["k"], T, False)
            ivs = [x for x in (ic, ip) if x]
            res[e.isoformat()] = dict(k=a["k"], c=round(a["c"], 2), p=round(a["p"], 2), straddle=round(a["c"] + a["p"], 2),
                                      move=round((a["c"] + a["p"]) / S * 100, 1), iv=round(sum(ivs) / len(ivs) * 100, 1) if ivs else None,
                                      spread=round((a["cs"] + a["ps"]) / (a["c"] + a["p"]) * 100, 1), dte=(e - ASOF).days)
        if not res:
            print("NO EXPIRIES", t); continue
        # benchmark: expiry nearest 30 calendar days that has an IV
        good = {e: v for e, v in res.items() if v["iv"]}
        bench = min(good, key=lambda e: abs(good[e]["dte"] - 30)) if good else None
        hv = hv20(t)
        nxt = PX[t].get("earn")
        last = PX[t].get("earnLast")
        tm = K.get(t, {}).get("time") or ""
        post = None
        if nxt:
            nd = dt.date.fromisoformat(nxt)
            for e in sorted(res):
                ed = dt.date.fromisoformat(e)
                if ed > nd or (ed == nd and tm == "BMO"):
                    post = e; break
        hv_has_earn = bool(last) and dt.date.fromisoformat(last) >= dt.date.fromisoformat(H[t][-21][0])
        b = good.get(bench) if bench else None
        ratio = round(b["iv"] / (hv * 100), 2) if b else None
        verdict = None if ratio is None else ("Cheap" if ratio < 1.0 else "Normal" if ratio < 1.5 else "Expensive")
        bench_has_earn = bool(nxt and bench and dt.date.fromisoformat(bench) >= dt.date.fromisoformat(nxt))
        out[t] = dict(S=S, hv=round(hv * 100, 1), bench=bench, bench_iv=b["iv"] if b else None, bench_dte=b["dte"] if b else None,
                      ratio=ratio, verdict=verdict, bench_has_earn=bench_has_earn, hv_has_earn=hv_has_earn,
                      post=post, post_move=res[post]["move"] if post else None, post_straddle=res[post]["straddle"] if post else None,
                      post_k=res[post]["k"] if post else None, lastTrade=d.get("lastTrade"), exps=res)
        o = out[t]
        print(f"{t:5} S={S:<8} HV={o['hv']:5}  IV({bench},{o['bench_dte']}d)={o['bench_iv']}  ratio={ratio} {verdict}{' [earn in IV]' if bench_has_earn else ''}{' [earn in HV]' if hv_has_earn else ''}  post={post} move={o['post_move']}%  spread={b['spread'] if b else None}%")
        time.sleep(0.4)
json.dump(out, open(ROOT + "/iv/iv.json", "w"), indent=1)
print("done", len(out))
