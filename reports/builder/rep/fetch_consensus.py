# Refresh rep/consensus.json from Nasdaq's earnings-date API (date, timing, EPS consensus, analyst count, prior-year EPS).
# Run from reports/builder: python3 rep/fetch_consensus.py
import json, re, sys, time, urllib.request
sys.path.insert(0, "rep"); import content as C

H = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
out = {}
for _, _, names in C.LISTS:
    for t in names:
        d = {}
        for _ in range(3):
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://api.nasdaq.com/api/analyst/{t}/earnings-date", headers=H), timeout=20))["data"] or {}
                break
            except Exception:
                time.sleep(2)
        rt = d.get("reportText") or ""
        ann = (d.get("announcement") or "").split(":")[-1].strip()
        g = lambda rx: (re.search(rx, rt) or [None, None])[1]
        out[t] = {"ann": ann, "eps": g(r"forecast for the quarter is \$(-?[\d.]+)"), "n": g(r"based on\s+(\d+) analyst"),
                  "time": "AMC" if "after market close" in rt else "BMO" if "before market open" in rt else "",
                  "status": "expected" if ann else "", "prior": g(r"same quarter last year was \$(-?[\d.]+)")}
        print(t, out[t])
        time.sleep(0.3)
json.dump(out, open("rep/consensus.json", "w"), indent=1)
