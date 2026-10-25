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
5. **IV**: `python3 iv/fetch_iv.py .` then `python3 iv/analyze.py .` (writes `iv/final.json`).
6. **Research**: rewrite each name's entry in `rep/content.py` (results, guidance, capex, partners,
   catalysts, macro, risks, sources) and every block in `pdf/mkpdf.py` marked `EDIT EACH MONTH`
   (dates, week table, tiles, game plan, themes, key dates). His 16 outlets only, never Yahoo,
   verified facts only.
7. **Build**: `python3 pdf/mkpdf.py`, check every stock fits on one page, copy the PDF to `reports/`.
