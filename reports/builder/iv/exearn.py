# Earnings-adjusted ("ex-earnings") IV from the option term structure, for every name.
# Two expiries after the report, T1 (first) and T2 (longest <= 60 DTE), share one earnings jump J:
#   s1^2*T1 = b^2*T1 + J   and   s2^2*T2 = b^2*T2 + J   ->   b^2 = (s2^2*T2 - s1^2*T1) / (T2 - T1)
# b = base IV without the earnings move (compared with 20-day HV); sqrt(J) = the 1-sd earnings-day move priced in.
import json, math, sys, datetime as dt
ROOT = sys.argv[1]
V = json.load(open(ROOT + "/iv/iv.json"))
F = json.load(open(ROOT + "/iv/final.json"))
PX = {t["ticker"]: t for t in json.load(open(ROOT + "/p2/final/prices/latest.json"))["tickers"]}
K = json.load(open(ROOT + "/rep/consensus.json"))
for t, v in V.items():
    nxt = PX[t].get("earn"); tm = K.get(t, {}).get("time") or ""
    ex = None
    if nxt:
        nd = dt.date.fromisoformat(nxt)
        post = sorted(e for e, x in v["exps"].items() if x["iv"] and (dt.date.fromisoformat(e) > nd or (dt.date.fromisoformat(e) == nd and tm == "BMO")))
        post = [e for e in post if v["exps"][e]["dte"] <= 63]
        if len(post) >= 2:
            e1, e2 = post[0], post[-1]
            T1, T2 = v["exps"][e1]["dte"] / 365, v["exps"][e2]["dte"] / 365
            s1, s2 = v["exps"][e1]["iv"] / 100, v["exps"][e2]["iv"] / 100
            b2 = (s2 * s2 * T2 - s1 * s1 * T1) / (T2 - T1)
            J = s1 * s1 * T1 - b2 * T1
            if b2 > 0 and J > 0:
                b = math.sqrt(b2) * 100
                r = round(b / v["hv"], 2)
                ex = dict(iv=round(b, 1), ratio=r, verdict="Cheap" if r < 1 else "Normal" if r < 1.5 else "Expensive",
                          jump=round(math.sqrt(J) * 100, 1), e1=e1, e2=e2)
    F[t]["ex"] = ex
    print(f"{t:5} {F[t]['verdict']:8} hv={v['hv']:5} ex={ex}")
json.dump(F, open(ROOT + "/iv/final.json", "w"), indent=1)
