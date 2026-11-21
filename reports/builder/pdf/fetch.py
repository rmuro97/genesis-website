import json, sys, time, urllib.request, datetime as dt
# Run from the builder folder: python3 pdf/fetch.py  (about 100 days of official daily closes for all names)
TO = dt.date.today(); FROM = TO - dt.timedelta(days=100)
sys.path.insert(0, 'rep'); import content as C
H = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
out = {}
for _, _, names in C.LISTS:
    for t in names:
        ac = 'etf' if t in getattr(C, 'ETFS', set()) else 'stocks'
        for attempt in range(3):
            try:
                u = f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass={ac}&fromdate={FROM}&todate={TO}&limit=120'
                j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=20))
                rows = j['data']['tradesTable']['rows']
                f = lambda s: float(s.replace('$', '').replace(',', ''))
                out[t] = sorted([(r['date'][6:] + '-' + r['date'][:2] + '-' + r['date'][3:5], f(r['close']), f(r['high']), f(r['low'])) for r in rows])
                # Nasdaq's history posts the day's row hours after the close; until then take the official close
                # ("Closed at <date> 4:00 PM ET") and the day's high/low from its quote pages
                q = json.load(urllib.request.urlopen(urllib.request.Request(f'https://api.nasdaq.com/api/quote/{t}/info?assetclass={ac}', headers=H), timeout=20))['data']
                sd = q.get('secondaryData') or {}
                ts = sd.get('lastTradeTimestamp') or ''
                if ts.startswith('Closed at '):
                    day = dt.datetime.strptime(ts[10:].split(',')[0] + ',' + ts.split(',')[1][:5], '%b %d, %Y').date().isoformat()
                    if day > out[t][-1][0]:
                        sm = json.load(urllib.request.urlopen(urllib.request.Request(f'https://api.nasdaq.com/api/quote/{t}/summary?assetclass={ac}', headers=H), timeout=20))['data']['summaryData']
                        hi, lo = sm['TodayHighLow']['value'].split('/')
                        out[t].append((day, f(sd['lastSalePrice']), f(hi), f(lo)))
                # Nasdaq adjusts its daily history for a split only some time later (SanDisk's 8-for-1 on Nov 20, 2026 was still raw;
                # Amphenol's Sep 3 split was already adjusted): divide earlier rows by the ratio only when Nasdaq's last pre-split close
                # is about ratio x the second feed's split-adjusted close for that day
                try:
                    sp = json.load(urllib.request.urlopen(urllib.request.Request(f'https://query1.finance.yahoo.com/v8/finance/chart/{t}?interval=1d&range=1y&events=split', headers={'User-Agent': 'Mozilla/5.0'}), timeout=20))
                    r_ = sp['chart']['result'][0]
                    yc = {dt.datetime.utcfromtimestamp(ts).date().isoformat(): c for ts, c in zip(r_['timestamp'], r_['indicators']['quote'][0]['close']) if c}
                    for k, v in ((r_.get('events') or {}).get('splits') or {}).items():
                        sd_, ratio = dt.datetime.utcfromtimestamp(int(k)).date().isoformat(), v['numerator'] / v['denominator']
                        pre = [row for row in out[t] if row[0] < sd_ and row[0] in yc]
                        if ratio and ratio != 1 and pre and abs(pre[-1][1] / yc[pre[-1][0]] / ratio - 1) < 0.25:
                            out[t] = [(a, round(b / ratio, 4), round(c / ratio, 4), round(e / ratio, 4)) if a < sd_ else (a, b, c, e) for a, b, c, e in out[t]]
                            print('  split-adjusted', t, sd_, ratio)
                except Exception:
                    pass
                break
            except Exception as e:
                err = e; time.sleep(2)
        else:
            print('FAIL', t, err)
        print(t, len(out.get(t, [])), out[t][0][0] if t in out else '', out[t][-1] if t in out else '')
json.dump(out, open('pdf/hist.json', 'w'))
