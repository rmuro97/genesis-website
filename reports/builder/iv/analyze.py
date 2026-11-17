# Rule-aware IV check: benchmark IV on the expiry nearest 30 days among expiries Ricky's rules allow
# (7-60 DTE from Mon Oct 26 and ending before the next report), compared with 20-day historical volatility.
import json, sys, datetime as dt
ROOT = sys.argv[1]
V = json.load(open(ROOT + "/iv/iv.json"))
PX = {t["ticker"]: t for t in json.load(open(ROOT + "/p2/final/prices/latest.json"))["tickers"]}
K = json.load(open(ROOT + "/rep/consensus.json"))
H = json.load(open(ROOT + "/pdf/hist.json"))
MON = dt.date.fromisoformat(max(r[-1][0] for r in H.values())) + dt.timedelta(days=1)
while MON.weekday() > 4:
    MON += dt.timedelta(days=1)  # next trading session (holidays not handled)
out = {}
for t, v in V.items():
    nxt = PX[t].get("earn"); tm = K.get(t, {}).get("time") or ""
    nd = dt.date.fromisoformat(nxt) if nxt else None
    allowed = []
    for e, x in v["exps"].items():
        ed = dt.date.fromisoformat(e); dte = (ed - MON).days
        if not (7 <= dte <= 60) or not x["iv"]:
            continue
        if nd and not (ed < nd or (ed == nd and tm == "AMC")):
            continue
        allowed.append((e, x, dte))
    b = min(allowed, key=lambda a: abs(a[2] - 30)) if allowed else None
    ratio = round(b[1]["iv"] / v["hv"], 2) if b else None
    verdict = ("Cheap" if ratio < 1.0 else "Normal" if ratio < 1.5 else "Expensive") if b else "Blocked"
    em = None
    if nd and (nd - MON).days <= 28 and v["post"]:
        x = v["exps"][v["post"]]
        em = dict(exp=v["post"], move=x["move"], straddle=x["straddle"], k=x["k"])
    out[t] = dict(S=v["S"], hv=v["hv"], exp=b[0] if b else None, dte=b[2] if b else None, iv=b[1]["iv"] if b else None,
                  spread=b[1]["spread"] if b else None, ratio=ratio, verdict=verdict, hv_has_earn=v["hv_has_earn"],
                  wide=bool(b and b[1]["spread"] > 15), em=em, n_allowed=len(allowed))
    o = out[t]
    print(f"{t:5} {verdict:9} IV={o['iv']} HV={o['hv']} r={ratio} exp={o['exp']} dte={o['dte']} wide={o['wide']} hvE={o['hv_has_earn']} EM={em and (em['exp'], em['move'])}")
json.dump(out, open(ROOT + "/iv/final.json", "w"), indent=1)
