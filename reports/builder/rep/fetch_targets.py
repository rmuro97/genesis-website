# Nasdaq analyst consensus (mean/low/high target, buy/hold/sell counts) for every name -> rep/consensus_pt.json
import json, sys, time, urllib.request
sys.path.insert(0, "rep"); import content as C
H = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
out = {}
for _, _, names in C.LISTS:
    for t in names:
        for a in range(3):
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(f"https://api.nasdaq.com/api/analyst/{t}/targetprice", headers=H), timeout=20))["data"]
                out[t] = d["consensusOverview"]; break
            except Exception as e:
                err = e; time.sleep(2)
        else:
            out[t] = None; print("FAIL", t, err)
        print(t, out[t])
json.dump(out, open("rep/consensus_pt.json", "w"), indent=1)
