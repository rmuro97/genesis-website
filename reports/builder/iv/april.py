import json, math, sys, time, subprocess, datetime as dt
from concurrent.futures import ThreadPoolExecutor
# APRIL CALL SCREEN for Ricky. Usage: python3 aprilcheck.py TICKER ...   (one JSON line per ticker)
# Finds the April 2027 monthly call (third Friday, Apr 16, 2027; if a name lists no April expiry, the nearest listed one:
# May if listed (it still covers April), else March) that sits closest to the money while costing
# $100–$1,200 per contract at the ASK (ask $1.00–$12.00), with a liquidity check, then judges whether April
# options are cheap: at-the-money April IV vs the stock's actual movement over 60 trading days (HV60; a
# 5-month option is better compared with a longer window than 20 days) and over 20 days (HV20).
# Verdict: IV/HV60 < 1.0 Cheap, < 1.25 Normal, else Expensive. Nasdaq data via curl (its CDN blocks urllib).
TODAY = dt.date.today()
EXP = dt.date(2027, 4, 16)
LO, HI = 1.00, 12.00          # ask per share -> $100 to $1,200 per contract
R = 0.0385
ETF = {"LYTE", "DRAM", "NCLD", "IBIT", "EWY", "EWT"}


def get(u):
    for a in range(3):
        try:
            out = subprocess.run(["curl", "-sS", "--fail", "--max-time", "30", "-H", "User-Agent: Mozilla/5.0", "-H", "Accept: application/json", u],
                                 capture_output=True, check=True).stdout
            return json.loads(out)["data"]
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


def bs(S, K, T, s):
    d1 = (math.log(S / K) + (R + s * s / 2) * T) / (s * math.sqrt(T))
    return S * N(d1) - K * math.exp(-R * T) * N(d1 - s * math.sqrt(T)), N(d1)


def iv(p, S, K, T):
    lo, hi = 0.01, 5.0
    if not (bs(S, K, T, lo)[0] < p < bs(S, K, T, hi)[0]):
        return None
    for _ in range(100):
        m = (lo + hi) / 2
        lo, hi = (lo, m) if bs(S, K, T, m)[0] > p else (m, hi)
    return (lo + hi) / 2


def closes(t, ac):
    rows = get(f"https://api.nasdaq.com/api/quote/{t}/historical?assetclass={ac}&fromdate={TODAY - dt.timedelta(days=120)}&todate={TODAY}&limit=120")["tradesTable"]["rows"]
    h = sorted((dt.datetime.strptime(r["date"], "%m/%d/%Y").date(), num(r["close"])) for r in rows)
    try:  # Nasdaq's history lags splits: adjust only if the pre-split close is still raw
        sp = json.loads(subprocess.run(["curl", "-s", "-m", "20", "-A", "Mozilla/5.0", f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=1d&range=6mo&events=split"],
                                       capture_output=True, text=True).stdout)["chart"]["result"][0]
        yc = {dt.datetime.utcfromtimestamp(x).date(): c for x, c in zip(sp["timestamp"], sp["indicators"]["quote"][0]["close"]) if c}
        for k, v in ((sp.get("events") or {}).get("splits") or {}).items():
            sd, ratio = dt.datetime.utcfromtimestamp(int(k)).date(), v["numerator"] / v["denominator"]
            pre = [(d_, c) for d_, c in h if d_ < sd and d_ in yc]
            if ratio != 1 and pre and abs(pre[-1][1] / yc[pre[-1][0]] / ratio - 1) < 0.25:
                h = [(d_, c / ratio if d_ < sd else c) for d_, c in h]
    except Exception:
        pass
    return h


def hv(h, n):
    xs = [c for _, c in h][-(n + 1):]
    lr = [math.log(xs[i] / xs[i - 1]) for i in range(1, len(xs))]
    m = sum(lr) / len(lr)
    return math.sqrt(sum((x - m) ** 2 for x in lr) / (len(lr) - 1)) * math.sqrt(252) * 100


def next_earn(t):
    if t in ETF:
        return None
    try:
        txt = (get(f"https://api.nasdaq.com/api/analyst/{t}/earnings-date") or {}).get("announcement") or ""
        if ":" in txt:
            d = dt.datetime.strptime(txt.split(":", 1)[1].strip(), "%b %d, %Y").date()
            return d if d >= TODAY else None
    except Exception:
        pass
    return None


def run(t):
    ac = "etf" if t in ETF else "stocks"
    try:
        h = closes(t, ac)
        S = h[-1][1]
        try:
            q = get(f"https://api.nasdaq.com/api/quote/{t}/info?assetclass={ac}")
            if q.get("marketStatus") == "Open":
                S = num(q["primaryData"]["lastSalePrice"]) or S
        except Exception:
            pass
        hv20, hv60 = hv(h, 20), hv(h, 60)
        ch = get(f"https://api.nasdaq.com/api/quote/{t}/option-chain?assetclass={ac}&limit=3000&fromdate=2027-03-01&todate=2027-05-31&money=all")
        by, cur = {}, None
        for r in ((ch or {}).get("table") or {}).get("rows") or []:
            if r["expirygroup"]:
                cur = dt.datetime.strptime(r["expirygroup"], "%B %d, %Y").date(); continue
            k, b, a = num(r["strike"]), num(r["c_Bid"]), num(r["c_Ask"])
            if None in (k, b, a) or a <= 0 or b <= 0:
                continue
            by.setdefault(cur, []).append(dict(k=k, bid=b, ask=a, mid=(a + b) / 2, oi=int(num(r.get("c_Openinterest")) or 0), vol=int(num(r.get("c_Volume")) or 0)))
        if not by:
            return dict(t=t, verdict="No chain", close=round(S, 2), note="no listed calls between March and May 2027")
        apr = [e for e in by if e.month == 4]
        later = sorted(e for e in by if e > EXP and (e - EXP).days <= 45)
        exp = apr[0] if apr else (later[0] if later else max(e for e in by if e < EXP))
        rows = by[exp]
        T = max((exp - TODAY).days, 1) / 365
        atm = min(rows, key=lambda x: abs(x["k"] - S))
        atm_iv = iv(atm["mid"], S, atm["k"], T)
        fit = [x for x in rows if LO <= x["ask"] <= HI]
        liquid = [x for x in fit if (x["ask"] - x["bid"]) / x["mid"] <= 0.15 and x["oi"] >= 100]
        # closest to the money: at-the-money or out-of-the-money strikes first (deep in-the-money calls behave like stock)
        pool = liquid or fit
        otm = [x for x in pool if x["k"] >= S * 0.97]
        pick = min(otm or pool, key=lambda x: abs(x["k"] - S)) if pool else None
        o = dict(t=t, close=round(S, 2), exp=exp.isoformat(), april=exp == EXP, dte=(exp - TODAY).days, hv20=round(hv20, 1), hv60=round(hv60, 1),
                 atmStrike=atm["k"], atmIv=round(atm_iv * 100, 1) if atm_iv else None, atmCost=round(atm["ask"] * 100))
        if atm_iv:
            ratio = atm_iv * 100 / hv60
            o.update(ratio60=round(ratio, 2), ratio20=round(atm_iv * 100 / hv20, 2),
                     verdict="Cheap" if ratio < 1 else "Normal" if ratio < 1.25 else "Expensive")
        else:
            o["verdict"] = "IV n/a"
        if pick:
            piv = iv(pick["mid"], S, pick["k"], T)
            delta = bs(S, pick["k"], T, piv)[1] if piv else None
            o["pick"] = dict(strike=pick["k"], ask=pick["ask"], bid=pick["bid"], cost=round(pick["ask"] * 100), breakeven=round(pick["k"] + pick["ask"], 2),
                             toBreakeven=round((pick["k"] + pick["ask"]) / S * 100 - 100, 1), otm=round(pick["k"] / S * 100 - 100, 1),
                             iv=round(piv * 100, 1) if piv else None, delta=round(delta, 2) if delta else None,
                             spread=round((pick["ask"] - pick["bid"]) / pick["mid"] * 100, 1), oi=pick["oi"], vol=pick["vol"], liquid=pick in liquid)
        else:
            o["pick"] = None
            o["note"] = "ATM call costs ${:,.0f}; no strike between $100 and $1,200".format(atm["ask"] * 100) if atm["ask"] > HI else "no strike in budget"
        ne = next_earn(t)
        o["earn"] = ne.isoformat() if ne else None
        o["spansEarnings"] = (t not in ETF)  # an April expiry spans every company's next quarterly report
        return o
    except Exception as e:
        return dict(t=t, verdict="Error", error=str(e)[:120])


with ThreadPoolExecutor(6) as ex:
    for o in ex.map(run, sys.argv[1:]):
        print(json.dumps(o)); sys.stdout.flush()
