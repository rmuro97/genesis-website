# Monthly Stock Analysis PDF

Builds **Stock Analysis: <Month>–<Next month> Opportunities <Year>**
(`Stock_Analysis_<Month>-<Next month>_Opportunities_<Year>.pdf`), one per month, made on the
**last Sunday of the month**. Page 1 is the "Where to buy options: IV check" list; then the week's
trading calendar, market backdrop, game plan, themes, key dates, all names at a glance, the IV page
and one page per stock.

Run everything from this folder with `/usr/bin/python3` (needs reportlab + matplotlib, DejaVu fonts).

## Monthly steps
1. **Lists**: update `LISTS` in `rep/content.py` from the app DB (`lists/conviction`), in the broker's order.
2. **Prices**: save the app DB doc `prices/latest` to `p2/final/prices/latest.json` (earnings dates, highs).
3. **Closes**: `python3 pdf/fetch.py` (100 days of official Nasdaq closes into `pdf/hist.json`).
4. **Consensus**: refresh `rep/consensus.json` (Nasdaq earnings-date + EPS forecast per name).
5. **IV**: `python3 iv/fetch_iv.py .`, `python3 iv/analyze.py .`, then `python3 iv/exearn.py .` (writes `iv/final.json`;
   exearn adds the earnings-adjusted IV so names blocked by earnings still get a verdict and a first buy day).
5b. **Price targets**: `python3 rep/fetch_targets.py` (Nasdaq consensus) and update `rep/targets.py` with the latest named
   targets (JPMorgan, BofA, Morgan Stanley, Goldman Sachs, Oppenheimer, Mizuho first; 3–5 per name; firm, rating, target, date,
   outlet, link) from his outlets. Also update `RULE3_DAYS` / `HOLIDAYS` in `pdf/mkpdf.py`.
6. **Research**: rewrite each name's entry in `rep/content.py` (results, guidance, capex, partners,
   catalysts, macro, risks, sources). A name new to the lists has no entry yet (AEHR and NOK, added Oct 28): add a full `S["<TICKER>"]` entry
   for it, plus its targets, before building and every block in `pdf/mkpdf.py` marked `EDIT EACH MONTH`
   (dates, week table, tiles, game plan, themes, key dates). His 16 outlets only, never Yahoo,
   verified facts only.
7. **Build**: `python3 pdf/mkpdf.py`, check every stock fits on one page, copy the PDF to `reports/`.
