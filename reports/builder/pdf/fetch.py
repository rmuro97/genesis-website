import json, sys, time, urllib.request, datetime as dt
# Run from the builder folder: python3 pdf/fetch.py  (about 100 days of official daily closes for all names)
TO = dt.date.today(); FROM = TO - dt.timedelta(days=100)
sys.path.insert(0, 'rep'); import content as C
H = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json'}
out = {}
for _, _, names in C.LISTS:
    for t in names:
        for attempt in range(3):
            try:
                u = f'https://api.nasdaq.com/api/quote/{t}/historical?assetclass=stocks&fromdate={FROM}&todate={TO}&limit=120'
                j = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=20))
                rows = j['data']['tradesTable']['rows']
                f = lambda s: float(s.replace('$', '').replace(',', ''))
                out[t] = sorted([(r['date'][6:] + '-' + r['date'][:2] + '-' + r['date'][3:5], f(r['close']), f(r['high']), f(r['low'])) for r in rows])
                # Nasdaq's history posts the day's row hours after the close; until then take the official close
                # ("Closed at <date> 4:00 PM ET") and the day's high/low from its quote pages
                q = json.load(urllib.request.urlopen(urllib.request.Request(f'https://api.nasdaq.com/api/quote/{t}/info?assetclass=stocks', headers=H), timeout=20))['data']
                sd = q.get('secondaryData') or {}
                ts = sd.get('lastTradeTimestamp') or ''
                if ts.startswith('Closed at '):
                    day = dt.datetime.strptime(ts[10:].split(',')[0] + ',' + ts.split(',')[1][:5], '%b %d, %Y').date().isoformat()
                    if day > out[t][-1][0]:
                        sm = json.load(urllib.request.urlopen(urllib.request.Request(f'https://api.nasdaq.com/api/quote/{t}/summary?assetclass=stocks', headers=H), timeout=20))['data']['summaryData']
                        hi, lo = sm['TodayHighLow']['value'].split('/')
                        out[t].append((day, f(sd['lastSalePrice']), f(hi), f(lo)))
                break
            except Exception as e:
                err = e; time.sleep(2)
        else:
            print('FAIL', t, err)
        print(t, len(out.get(t, [])), out[t][0][0] if t in out else '', out[t][-1] if t in out else '')
json.dump(out, open('pdf/hist.json', 'w'))
