import json, os, sys, datetime as dt
from xml.sax.saxutils import escape as X

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
                                Image, PageBreak, KeepTogether, NextPageTemplate, KeepInFrame)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "rep"))
import content as C
import targets as TG

P = json.load(open(os.path.join(ROOT, "p2/final/prices/latest.json")))
K = json.load(open(os.path.join(ROOT, "rep/consensus.json")))
H = json.load(open(os.path.join(HERE, "hist.json")))
PX = {t["ticker"]: t for t in P["tickers"]}
MK = {m["key"]: m for m in P["market"]}
# EDIT EACH MONTH: TODAY = the edition date (the Monday after the build Sunday); NEXT_SESSION = first trading day.
TODAY = dt.date(2026, 11, 17)
NEXT_SESSION = dt.date(2026, 11, 17)
LAST = max(dt.date.fromisoformat(r[-1][0]) for r in H.values())  # last official close in pdf/hist.json
LIVE_AT = os.environ.get("LIVE_AT", "")  # intraday build: the last row in hist.json is a live, cross-checked price at this time, not a close
PXLAB = (f"LIVE {LIVE_AT.replace(' PT', '')}" if LIVE_AT else f"CLOSE {LAST:%b} {LAST.day}").upper()
# EDIT EACH MONTH: Rule 3 data days (FOMC, CPI, PCE, PPI, jobs, GDP) and market holidays for the next ~2 months
RULE3_DAYS = {dt.date(2026, 10, 28), dt.date(2026, 10, 29), dt.date(2026, 11, 6), dt.date(2026, 11, 10), dt.date(2026, 11, 13),
              dt.date(2026, 11, 25), dt.date(2026, 12, 4), dt.date(2026, 12, 9), dt.date(2026, 12, 10)}
HOLIDAYS = {dt.date(2026, 11, 26), dt.date(2026, 12, 25)}
# EDIT EACH MONTH: names that reported after the last close in hist.json: their option prices predate the report
PRE_REPORT = set()
POST_LIVE = {}
NEW_LIVE = ""
ETFS = getattr(C, "ETFS", set())  # option IV taken intraday after a same-day report
CH = os.path.join(HERE, "charts")
os.makedirs(CH, exist_ok=True)

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVBI", FD + "DejaVuSans-Bold.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DVB", italic="DVI", boldItalic="DVBI")

INK = colors.HexColor("#1c1d21"); MUT = colors.HexColor("#62656e"); LINE = colors.HexColor("#e1dfd8")
ACC = colors.HexColor("#1f5fbf"); ACCBG = colors.HexColor("#eaf1fc")
UP = colors.HexColor("#13804a"); DN = colors.HexColor("#c2362b")
BAD = colors.HexColor("#b42318"); BADBG = colors.HexColor("#fdecea")
WARN = colors.HexColor("#8a5a00"); WARNBG = colors.HexColor("#fdf4e1")
OK = colors.HexColor("#13804a"); OKBG = colors.HexColor("#e7f5ec")
CHIP = colors.HexColor("#f2f0ea")


def st(name, **kw):
    base = dict(fontName="DV", fontSize=9, leading=12.1, textColor=INK)
    base.update(kw)
    return ParagraphStyle(name, **base)


S_T = st("t", fontName="DVB", fontSize=24, leading=28)
S_H1 = st("h1", fontName="DVB", fontSize=15, leading=19, spaceBefore=4, spaceAfter=6)
S_H2 = st("h2", fontName="DVB", fontSize=11, leading=14, spaceBefore=8, spaceAfter=4)
S_B = st("b")
S_BL = st("bl", fontSize=10.5, leading=14.5)
S_M = st("m", fontSize=8, leading=10.5, textColor=MUT)
S_SM = st("sm", fontSize=8.4, leading=11)
S_LAB = st("lab", fontName="DVB", fontSize=7.4, leading=10, textColor=MUT)
S_TICK = st("tick", fontName="DVB", fontSize=22, leading=26)
S_R = st("r", alignment=TA_RIGHT)
S_C = st("c", alignment=TA_CENTER)


def num(s):
    return None if s in (None, "") else float(s.rstrip("."))


def eps_s(x):
    return f"-${-x:.2f}" if x < 0 else f"${x:.2f}"


def d(s):
    return dt.date.fromisoformat(s) if s else None


def fmt_d(x, dow=True):
    return x.strftime(("%a " if dow else "") + "%b ") + str(x.day)


def pct(x):
    x = round(x, 1) + 0.0
    return "0.0%" if x == 0 else f"{x:+.1f}%"


def pc(x, bold=True, size=None):
    x = round(x, 1)
    c = "#13804a" if x > 0 else "#c2362b" if x < 0 else "#1c1d21"
    f = "DVB" if bold else "DV"
    sz = f' size="{size}"' if size else ""
    return f'<font name="{f}" color="{c}"{sz}>{pct(x)}</font>'


LISTPOS = {}
for key, label, names in C.LISTS:
    for i, t in enumerate(names, 1):
        LISTPOS[t] = (label, i, len(names))

TIME_PT = {"AMC": "after the close (after 1:00 PM PT)", "BMO": "before the open (before 6:30 AM PT)"}
TIME_OVERRIDE = {"SKHY": "evening, by ~5:00 PM PT (Seoul morning)", "CRCL": "before the open", "NVDA": "after the close (1:20 PM PT)"}


def earn_info(t):
    p, k = PX[t], K.get(t, {})
    return dict(nxt=d(p.get("earn")), last=d(p.get("earnLast")),
                when=TIME_OVERRIDE.get(t) or TIME_PT.get(k.get("time") or "", "time not announced"),
                est=k.get("status") == "estimated", eps=num(k.get("eps")), prior=num(k.get("prior")), n=k.get("n"))


def rule_note(t, ei):
    nxt = ei["nxt"]
    if t in ETFS:
        return ("ok", "An ETF has no earnings, so a 7–60 DTE option never runs into a report. Only Rules 2 and 3 (Fridays and data days) apply.")
    if not nxt:
        return ("ok", f"Already reported {fmt_d(ei['last'])}; next date not set yet. A 7–60 DTE option bought now is not expected to run into a report.")
    days = (nxt - TODAY).days
    if days > 60:
        return ("ok", f"Earnings are {days} days out, so any 7–60 DTE option bought now expires before the report.")
    first_ok = NEXT_SESSION + dt.timedelta(days=7)
    if nxt <= first_ok:
        return ("bad", f"Reports {fmt_d(nxt)}, {days} days out. No expiry is both ≥7 DTE and before the report: no new options until it's out (Rules 3 and 4).")
    amc = K.get(t, {}).get("time") == "AMC"
    last_ok = nxt if amc else nxt - dt.timedelta(days=1)
    fris = [first_ok + dt.timedelta(days=i) for i in range((last_ok - first_ok).days + 1)]
    fris = [x for x in fris if x.weekday() == 4]
    if not fris:
        return ("bad", f"Reports {fmt_d(nxt)}, {days} days out. No Friday expiry is both ≥7 DTE and before the report, so a new option would run into earnings (Rules 3 and 4).")
    return ("warn", f"Reports {fmt_d(nxt)}, {days} days out. Friday expiries that are ≥7 DTE and still before the report: {', '.join(fmt_d(x, False) for x in fris)}. Anything later is held into earnings (Rules 3 and 4).")


def first_buy(t, ei):
    """First day a new option is allowed after the report: after-close/unknown-time reports -> next day; then skip
    Fridays (Rule 2), Rule 3 data days and holidays."""
    nd = ei["nxt"]
    if not nd:
        return None
    x = nd if (K.get(t, {}).get("time") == "BMO" and t not in TIME_OVERRIDE) else nd + dt.timedelta(days=1)
    while x.weekday() >= 4 or x in RULE3_DAYS or x in HOLIDAYS:
        x += dt.timedelta(days=1)
    return x


def vlabel(t):
    """IV verdict for every name: the rule-allowed check, or the earnings-adjusted estimate when blocked."""
    v = IVF[t]
    if v["verdict"] != "Blocked":
        return f'<font color="{VCOL[v["verdict"]]}"><b>{v["verdict"]}</b></font>'
    if v.get("ex"):
        return f'<font color="{VCOL[v["ex"]["verdict"]]}"><b>{v["ex"]["verdict"]}</b></font><font size="6.5" color="#62656e"> after earn.</font>'
    return '<font color="#62656e"><b>n/a</b></font>'


# ---------- stats from official daily closes ----------
def stats(t):
    rows = H[t]
    ds = [d(r[0]) for r in rows]; cl = [r[1] for r in rows]
    last = cl[-1]
    base3 = max([i for i, x in enumerate(ds) if x <= LAST - dt.timedelta(days=92)] or [0])  # funds launched < 3 months ago: since launch
    i1m = len(cl) - 22
    p = PX[t]
    return dict(
        dates=ds, close=cl, last=last, day=(last / cl[-2] - 1) * 100, wk=(last / cl[-6] - 1) * 100,
        m1=(last / cl[i1m] - 1) * 100, m1_from=ds[i1m], m3=(last / cl[base3] - 1) * 100, m3_from=ds[base3],
        hi3=max(r[2] for r in rows[base3:]), lo3=min(r[3] for r in rows[base3:]),
        hi1=max(r[2] for r in rows[i1m:]), lo1=min(r[3] for r in rows[i1m:]),
        hi=p["hi"], hiDate=p["hiDate"], offhi=(last / p["hi"] - 1) * 100, base3=base3, i1m=i1m)


ST = {t: stats(t) for t in H}
IVF = json.load(open(os.path.join(ROOT, "iv/final.json")))
PT = json.load(open(os.path.join(ROOT, "rep/consensus_pt.json")))  # Nasdaq analyst consensus


def pt_named(t, short=False):
    """Named firm targets, the six top firms first and in bold."""
    xs = sorted(TG.T.get(t, []), key=lambda x: (x[0] not in TG.TOP_FIRMS,))
    out = []
    for firm, rating, tgt, when, outlet, url in xs:
        name = f"<b>{X(firm)}</b>" if firm in TG.TOP_FIRMS else X(firm)
        if short:
            out.append(f"{name} {'$%s' % format(tgt, ',') if tgt else X(rating)}")
        else:
            bits = [b for b in (X(rating), f"${tgt:,}" if tgt else "") if b]
            out.append(f'{name} {" ".join(bits)} <font color="#62656e">({X(when)}, <a href="{X(url)}" color="#1f5fbf">{X(outlet)}</a>)</font>')
    return out


def pt_cons(t, last):
    if t == "IBIT":
        return "Not applicable: an ETF that holds bitcoin has no analyst price targets; it moves with the bitcoin price."
    if t in ETFS:
        return "Not applicable: an ETF has no analyst price targets. See its top holdings' pages and targets instead."
    c = PT.get(t)
    if not c:
        return "No Nasdaq consensus yet (recent U.S. listing)."
    up = (c["priceTarget"] / last - 1) * 100
    return (f'Consensus <b>${c["priceTarget"]:,.0f}</b> ({pc(up, False)} vs {'price' if LIVE_AT else 'close'}) · range ${c["lowPriceTarget"]:,.0f}–${c["highPriceTarget"]:,.0f} · '
            f'{c["buy"]} buy / {c["hold"]} hold / {c["sell"]} sell (Nasdaq)')
VCOL = {"Cheap": "#13804a", "Normal": "#1c1d21", "Expensive": "#b42318", "Blocked": "#62656e"}


def iv_rows(t, ei):
    v = IVF[t]
    if v["verdict"] == "Blocked":
        txt = f'<font color="#62656e">No new options yet: every 7–60 DTE expiry runs past earnings on {fmt_d(ei["nxt"], False)} (Rule 3).</font>'
        if v.get("ex"):
            x = v["ex"]; fb = first_buy(t, ei)
            txt += (f' <b>After the report:</b> <font color="{VCOL[x["verdict"]]}"><b>{x["verdict"]}</b></font> · IV without the earnings move about {x["iv"]:.0f}% vs {v["hv"]:.0f}% '
                    f'actual 20-day movement (ratio {x["ratio"]:.2f}). <b>First day you can buy: {fmt_d(fb)}.</b>')
    else:
        ed = dt.date.fromisoformat(v["exp"])
        txt = (f'<font color="{VCOL[v["verdict"]]}"><b>{v["verdict"]}</b></font> · IV {v["iv"]:.0f}% vs {v["hv"]:.0f}% actual 20-day movement '
               f'(ratio {v["ratio"]:.2f}) on the {fmt_d(ed, False)} expiry, {v["dte"]} DTE.')
        if t in POST_LIVE:
            txt += f' <font color="#8a5a00">IV from {POST_LIVE[t]} (stock near ${v["S"]:,.2f}); recheck live before buying.</font>'
        elif t in PRE_REPORT:
            txt += f' <font color="#8a5a00">These option prices are from before its {fmt_d(ei["last"], False)} after-close report; recheck live before buying.</font>'
        elif v["hv_has_earn"]:
            txt += f' <font color="#8a5a00">Actual movement includes the {fmt_d(ei["last"], False)} earnings move, so "cheap" may be overstated.</font>'
        if v["wide"]:
            txt += ' <font color="#8a5a00">Wide bid/ask ' + ("in the intraday quotes" if LIVE_AT else "at the last close") + '; check live quotes.</font>'
    rows = [("IV CHECK", txt)]
    if v["em"]:
        em = v["em"]
        rows.append(("EARNINGS MOVE PRICED IN", f'<b>±{em["move"]:.1f}%</b> (±${em["straddle"]:,.2f}) by the {fmt_d(dt.date.fromisoformat(em["exp"]), False)} expiry, from the ${em["k"]:,.2f} straddle.'))
    return rows


# ---------- charts ----------
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.edgecolor": "#c9c6bd",
                     "axes.labelcolor": "#62656e", "xtick.color": "#62656e", "ytick.color": "#62656e"})


def chart(t):
    s, ei = ST[t], earn_info(t)
    ds, cl = s["dates"][s["base3"]:], s["close"][s["base3"]:]
    up = cl[-1] >= cl[0]
    col = "#13804a" if up else "#c2362b"
    fig, ax = plt.subplots(figsize=(7.3, 1.9), dpi=200)
    ax.axvspan(s["dates"][s["i1m"]], ds[-1] + dt.timedelta(days=1), color="#1f5fbf", alpha=0.06, lw=0)
    lo = min(cl); hi = max(cl); pad = (hi - lo) * 0.12 or 1
    ax.fill_between(ds, cl, lo - pad, color=col, alpha=0.08, lw=0)
    ax.plot(ds, cl, color=col, lw=1.6)
    ax.axhline(cl[0], color="#9a9ca3", lw=0.7, ls=(0, (2, 2)))
    ax.text(ds[0], cl[0], f"3 mo ago ${cl[0]:,.2f}", va="bottom", ha="left", fontsize=7, color="#62656e",
            bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.85))
    ih, il = cl.index(hi), cl.index(lo)
    ax.plot([ds[ih]], [hi], "o", ms=3.2, color="#1c1d21")
    ax.annotate(f"High close ${hi:,.2f}", (ds[ih], hi), xytext=(0, 5), textcoords="offset points", ha="center", fontsize=7, color="#1c1d21")
    ax.plot([ds[il]], [lo], "o", ms=3.2, color="#1c1d21")
    ax.annotate(f"Low close ${lo:,.2f}", (ds[il], lo), xytext=(0, -11), textcoords="offset points", ha="center", fontsize=7, color="#1c1d21")
    ax.plot([ds[-1]], [cl[-1]], "o", ms=4.5, color=col)
    ax.annotate(f"${cl[-1]:,.2f}", (ds[-1], cl[-1]), xytext=(6, 0), textcoords="offset points", va="center", fontsize=8.5, fontweight="bold", color=col)
    if ei["last"] and ds[0] <= ei["last"] <= ds[-1]:
        ax.axvline(ei["last"], color="#8a5a00", lw=0.9, ls=(0, (4, 2)))
        ax.text(ei["last"], 1.015, f"Earnings {fmt_d(ei['last'], False)}", transform=ax.get_xaxis_transform(), fontsize=7, color="#8a5a00", ha="center", va="bottom")
    ax.set_ylim(lo - pad * 1.6, hi + pad * 1.7)
    ax.set_xlim(ds[0] - dt.timedelta(days=1), ds[-1] + dt.timedelta(days=7))
    ax.xaxis.set_major_locator(mdates.MonthLocator()); ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=0))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b 1"))
    ax.yaxis.tick_right(); ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"${v:,.0f}"))
    ax.grid(axis="y", color="#ebe9e3", lw=0.6); ax.set_axisbelow(True)
    for sp in ("top", "left"):
        ax.spines[sp].set_visible(False)
    fig.tight_layout(pad=0.4)
    f = os.path.join(CH, f"{t}.png"); fig.savefig(f); plt.close(fig)
    return f


def spark(t):
    s = ST[t]
    cl = s["close"][s["base3"]:]
    col = "#13804a" if cl[-1] >= cl[0] else "#c2362b"
    fig, ax = plt.subplots(figsize=(1.25, 0.26), dpi=220)
    ax.plot(range(len(cl)), cl, color=col, lw=1.0)
    ax.axvspan(len(cl) - 22, len(cl) - 1, color="#1f5fbf", alpha=0.08, lw=0)
    ax.plot([len(cl) - 1], [cl[-1]], "o", ms=1.8, color=col)
    ax.axis("off"); fig.subplots_adjust(0, 0, 1, 1)
    f = os.path.join(CH, f"{t}_sp.png"); fig.savefig(f, transparent=True); plt.close(fig)
    return f


# ---------- doc ----------
M1 = (TODAY + dt.timedelta(days=7)).replace(day=1); M2 = (M1 + dt.timedelta(days=32)).replace(day=1)  # named for the month the edition mainly covers (a Nov 30 edition is "December")
EDITION = f"{M1:%B} {M1.year} edition · {TODAY:%A} {fmt_d(TODAY, False)} · updated Nov 17"
TITLE = f"{M1:%B} Market Analysis"
OUT = os.path.join(HERE, f"{M1:%B}_Market_Analysis_{M1.year}.pdf")
W, Hh = letter
M = 0.55 * inch


def on_page(c, doc):
    c.saveState()
    c.setFont("DV", 7); c.setFillColor(MUT)
    c.drawString(M, 0.38 * inch, f"Muro's Investing Analysis · {TITLE} · {fmt_d(TODAY)}, {TODAY.year} · Decision support, not advice")
    c.drawRightString(W - M, 0.38 * inch, f"Page {doc.page}")
    c.restoreState()


doc = BaseDocTemplate(OUT, pagesize=letter, leftMargin=M, rightMargin=M, topMargin=0.5 * inch, bottomMargin=0.6 * inch,
                      title=TITLE, author="Muro's Investing Analysis",
                      subject="Price targets, 2026 capex, earnings, guidance, catalysts and market events for 50 stocks and ETFs")
FRAME_H = Hh - 1.1 * inch
frame = Frame(M, 0.6 * inch, W - 2 * M, FRAME_H, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=on_page)])
CW = W - 2 * M
story = []


def box(flows, bg, pad=8, border=None):
    t = Table([[flows]], colWidths=[CW])
    stl = [("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), pad), ("RIGHTPADDING", (0, 0), (-1, -1), pad),
           ("TOPPADDING", (0, 0), (-1, -1), pad - 2), ("BOTTOMPADDING", (0, 0), (-1, -1), pad - 1)]
    if border:
        stl.append(("LINEBEFORE", (0, 0), (0, -1), 3, border))
    t.setStyle(TableStyle(stl))
    return t


# EDIT EACH MONTH (editorial: verified facts only)
# Cover / overview
story += [Paragraph("MURO'S INVESTING ANALYSIS · MONTHLY REPORT", S_LAB), Spacer(1, 4),
          Paragraph(X(TITLE), S_T), Spacer(1, 2),
          Paragraph(X(EDITION), st("sub", fontName="DVB", fontSize=15, leading=19, textColor=ACC)), Spacer(1, 6),
          Paragraph("All 50 names on your lists, in your broker's order as of Nov 17, each with a company summary (what it does and specializes in; all 50 together on the \"Company summaries\" pages, and at the top of every stock page), Wall Street price targets, 2026 capex, latest results and guidance, catalysts, partnerships, risks and a 3-month chart. <b>Updated Nov 17 with your new lists and order:</b> Top 5 is now <b>AMZN, SKHY, AVGO, AMAT, BE</b> (Amazon back on top; Nvidia moved to #3 in the 2026 Portfolio, which Coherent now leads); and <b>IREN (IREN Limited)</b> is back on the 15–50% Dip list with a full page. It covers the news since Nov 12: Huang's resignation as Nvidia CEO, results from Cisco, Applied Materials, Cerebras and Nebius, PPI and the priced-in December hike, the AI selloff and bitcoin's slide. " + (f"Prices are live Nasdaq trades at {LIVE_AT} Tue Nov 17 (cross-checked on a second feed; history through Monday's official closes), and IV checks use Tuesday's intraday Nasdaq option quotes. " if LIVE_AT else f"Prices are official Nasdaq closes through {LAST:%A} {fmt_d(LAST, False)} (cross-checked on a second feed), and IV checks use Nasdaq option quotes at that close. ") + "All figures are in US dollars (SK hynix and Alibaba converted at ECB reference rates). Times are Pacific.", S_BL),
          Spacer(1, 5),
          Paragraph("Price targets: Nasdaq consensus (mean, low–high, buy/hold/sell count) for every name, plus named firm targets from your outlets. 2026 capex: spending to date from company SEC filings, with guidance from your outlets where companies give it. Charts show 3 months of daily closes, which shows each stock's trend and how far it has pulled back; the shaded band is the last month. Decision support, not advice. News facts come from CNBC, Bloomberg, Seeking Alpha and Fox Business, plus company releases and SEC filings. Consensus EPS is from Nasdaq. Earnings dates marked \"est.\" are not confirmed by the company.", S_M),
          ]
# EDIT EACH MONTH (editorial: verified facts only)
WEEK = [
    ("Tue Nov 17", "ok", "Clear for trading (October retail sales at 5:30 AM PT is not a Rule 3 print). Nvidia reports after the close (1:20 PM PT): no new NVDA options, and the whole AI group will move on it. Microsoft Ignite runs Tue–Fri."),
    ("Wed Nov 18", "ok", "Clear for trading. FOMC minutes at 11:00 AM PT. Palo Alto reports after the close (read-through to CRWD, ZS, FTNT, AKAM). Anthropic's IPO prices (range $70–78)."),
    ("Thu Nov 19", "ok", "Clear for trading. Anthropic starts trading (AMZN, AVGO, NVDA, SKHY hold stakes or bought into its placement). Alibaba reports before the open: no new BABA options."),
    ("Fri Nov 20", "bad", "A Friday, so no new trades (Rule 2). Monthly options expiration."),
    ("Mon Nov 23", "ok", "Clear for trading, but HPE reports: no new HPE options. Dell reports Tue Nov 24: no new DELL options. GDP and PCE Wed Nov 25 (Rule 3)."),
]
TONE = {"ok": (OK, OKBG), "bad": (BAD, BADBG), "warn": (WARN, WARNBG)}

# Where to buy options: the IV check, at the top of the report
BUYDAYS = [a for a, tone, _ in WEEK if tone == "ok"]
ALLT = [t for _, _, ns in C.LISTS for t in ns]
OPEN_T = [t for t in ALLT if IVF[t]["verdict"] not in ("Blocked", "Error") and rule_note(t, earn_info(t))[0] != "bad"]
SHUT_T = [t for t in ALLT if t not in OPEN_T]
ORDER = {"Cheap": 0, "Normal": 1, "Expensive": 2}
OPEN_T.sort(key=lambda t: (ORDER[IVF[t]["verdict"]], IVF[t]["ratio"]))
bh = [Paragraph(x, S_LAB) for x in ("TICKER", "LIST", "IV", "IV vs ACTUAL MOVE", "EXPIRY CHECKED", "NEXT EARNINGS", "NOTE")]
brows = [bh]
for t in OPEN_T:
    v, ei = IVF[t], earn_info(t)
    lab, pos, _ = LISTPOS[t]
    short = {"Top 5": "Top 5", "2026 Portfolio": "Portfolio"}.get(lab, "Dip")
    note = []
    if t in POST_LIVE:
        note.append(POST_LIVE[t])
    elif t in PRE_REPORT:
        note.append(f"priced before the {fmt_d(ei['last'], False)} report")
    elif v["hv_has_earn"]:
        note.append("incl. last earnings move")
    if v["wide"]:
        note.append("wide bid/ask")
    ne = fmt_d(ei["nxt"]) + (" est." if ei["est"] else "") if ei["nxt"] else "not set"
    brows.append([Paragraph(f'<font name="DVB">{t}</font>', S_SM), Paragraph(f"{short} #{pos}", S_SM),
                  Paragraph(f'<font color="{VCOL[v["verdict"]]}"><b>{v["verdict"]}</b></font>', S_SM),
                  Paragraph(f'{v["iv"]:.0f}% vs {v["hv"]:.0f}% <font color="#62656e">({v["ratio"]:.2f})</font>', S_SM),
                  Paragraph(f'{fmt_d(dt.date.fromisoformat(v["exp"]), False)} · {v["dte"]} DTE', S_SM),
                  Paragraph(ne, S_SM), Paragraph(X("; ".join(note)), st("nt", fontSize=7, leading=8.4, textColor=WARN))])
bt = Table(brows, colWidths=[0.62 * inch, 0.98 * inch, 0.66 * inch, 1.54 * inch, 1.12 * inch, 0.98 * inch, CW - 5.9 * inch], repeatRows=1)
bsty = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 1.8), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE)]
for i, t in enumerate(OPEN_T, 1):
    if IVF[t]["verdict"] == "Cheap":
        bsty.append(("BACKGROUND", (0, i), (-1, i), OKBG))
bt.setStyle(TableStyle(bsty))
story += [Spacer(1, 8), Paragraph("Where to buy options: IV check", S_H1),
          box([Paragraph(f'<b>Next buy days: {X(", ".join(BUYDAYS))}.</b> Only names your rules allow are listed, best value first. '
                         '<font color="#13804a"><b>Cheap</b></font> = options cost less than the stock has actually been moving (IV below 20-day movement): the better time to buy. '
                         'Normal = fair. Expensive = wait. The expiry shown is the allowed one nearest 30 days (7–60 DTE and ending before the next report); take profit at +25% to +100% (Rule 1).', S_B)], OKBG, border=OK),
          Spacer(1, 4), bt, Spacer(1, 3),
          Paragraph(("Quotes are Nasdaq delayed option prices taken intraday Tuesday; " if LIVE_AT else "Quotes are Nasdaq delayed option prices at the last close; ") + "recheck live before buying. A cheap reading is not a buy signal on its own.", S_M),
          Spacer(1, 8)]
# the names blocked by earnings: earnings-adjusted IV and the first day each can be bought
SHUT_T.sort(key=lambda t: (first_buy(t, earn_info(t)) or dt.date.max, t))
ah = [Paragraph(x, S_LAB) for x in ("TICKER", "LIST", "REPORTS", "FIRST BUY DAY", "IV AFTER EARNINGS (EST.)", "VERDICT", "EARNINGS MOVE PRICED")]
arows = [ah]
for t in SHUT_T:
    v, ei = IVF[t], earn_info(t); x = v.get("ex")
    lab, pos, _ = LISTPOS[t]
    short = {"Top 5": "Top 5", "2026 Portfolio": "Portfolio"}.get(lab, "Dip")
    mv = f'±{v["em"]["move"]:.1f}% (straddle)' if v.get("em") else (f'±{x["jump"]:.1f}% (1 sd)' if x else "–")
    arows.append([Paragraph(f'<font name="DVB">{t}</font>', S_SM), Paragraph(f"{short} #{pos}", S_SM),
                  Paragraph(fmt_d(ei["nxt"]) + (" est." if ei["est"] else ""), S_SM), Paragraph(f'<b>{fmt_d(first_buy(t, ei))}</b>', S_SM),
                  Paragraph(f'{x["iv"]:.0f}% vs {v["hv"]:.0f}% <font color="#62656e">({x["ratio"]:.2f})</font>' if x else "n/a", S_SM),
                  Paragraph(f'<font color="{VCOL[x["verdict"]]}"><b>{x["verdict"]}</b></font>' if x else "n/a", S_SM), Paragraph(mv, S_SM)])
at = Table(arows, colWidths=[0.72 * inch, 1.02 * inch, 1.0 * inch, 1.05 * inch, 1.45 * inch, 0.72 * inch, CW - 5.96 * inch], repeatRows=1)
asty = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 1.8), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.8),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE)]
for i, t in enumerate(SHUT_T, 1):
    if (IVF[t].get("ex") or {}).get("verdict") == "Cheap":
        asty.append(("BACKGROUND", (0, i), (-1, i), OKBG))
at.setStyle(TableStyle(asty))
story += [PageBreak(), Paragraph(f"After earnings: the other {len(SHUT_T)} names", S_H1),
          Paragraph("No new options on these until their report is out (Rules 3 and 4). IV here is estimated without the earnings move, from two expiries after the report, "
                    "so you know where each one stands and the first day you can buy (skipping Fridays and Rule 3 data days). Recheck live after the report: IV usually drops once earnings pass.", S_M),
          Spacer(1, 3), at,
          Spacer(1, 12), Paragraph("The next 5 sessions: when you can trade", S_H1)]
wt = Table([[Paragraph(f"<b>{a}</b>", S_B), Paragraph(X(b), S_B)] for a, _, b in WEEK], colWidths=[1.05 * inch, CW - 1.05 * inch])
ws = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
      ("LINEBELOW", (0, 0), (-1, -2), 0.5, colors.white)]
for i, (_, tone, _) in enumerate(WEEK):
    ws += [("BACKGROUND", (0, i), (-1, i), TONE[tone][1]), ("LINEBEFORE", (0, i), (0, i), 3, TONE[tone][0])]
wt.setStyle(TableStyle(ws)); story.append(wt)

story += [PageBreak(), Paragraph("Market backdrop", S_H1),
          box([Paragraph("<font color=\"#b42318\"><b>Headwind.</b></font> Nvidia lost its CEO: Jensen Huang resigned Nov 12 after reports of affairs, including one with a woman US officials suspect of spying for China; CFO Colette Kress is interim CEO (CNBC). NVDA fell as much as 14% that day and 12.75% on the week, its sixth straight weekly drop, and closed below a $4T value Friday. HSBC cut it to Hold ($170). The AI-hardware group followed: Nebius −16.8% Thursday on a $27B capex plan, then optics, memory and servers fell Friday (COHR, CRDO, LYTE −6% to −7%; Dell and CoreWeave down about 10% intraday). Rates: October PPI was +6.5% year on year, the most since 2022, a Dec 9 hike is fully priced (about 13% odds of 50 bp), the 10-year is above 5.1% and the dollar is at its highest since April 2025 (CNBC, FT). Bitcoin fell to about $62K over the weekend. Monday the S&amp;P 500 fell 1.92% to 7,417 and the Nasdaq 2.49% (its third straight loss); the VIX jumped as much as 25% to about 24, and staples were the only sector up (CNBC). SK hynix fell 5.6% in Seoul as the Kospi dropped 3.6% (Bloomberg), and Commerce closed the loophole that let Chinese firms rent US AI chips abroad. <font color=\"#13804a\"><b>Tailwind.</b></font> Money is rotating to Nvidia's rivals and suppliers of custom chips (Broadcom +5.5% Thursday, Cerebras +11% Friday on a beat and a Microsoft deal); Cisco and Applied Materials beat and raised; SpaceX caught Starship's upper stage from orbit; and Anthropic's IPO (trading Thursday) has Nvidia, Broadcom, Micron, TSMC and AMD in its $26B placement (CNBC).", S_B)], WARNBG),
          Spacer(1, 6)]
spx, comp, y10, y30, btc = MK["SPX"], MK["COMP"], MK["US10Y"], MK["US30Y"], MK["BTC"]
# EDIT EACH MONTH (editorial: verified facts only; the Headwind box above too)
TILES = [("FED FUNDS", "3.75–4.00%", "Dec 9 hike fully priced; ~13% odds of 50 bp (CME FedWatch via CNBC)", BAD),
         ("PPI (OCT)", "+0.3% m/m", "+6.5% y/y, the most since Nov 2022 (CNBC)", BAD),
         ("CPI (OCT)", "+0.4% m/m", "Core +0.3% vs +0.2% expected (CNBC)", BAD),
         ("10-YR YIELD", f"{y10['price']:.2f}%", f"30-yr {y30['price']:.2f}% · " + ("live" if LIVE_AT else f"{LAST:%a} close"), WARN),
         ("US DOLLAR", "Apr 2025 high", "Dollar index at its highest since April 2025 on Fed-hike bets (CNBC)", WARN),
         ("S&P 500", f"{spx['price']:,.0f}", f"{spx['chg']:+.2f}% {LAST:%a} · Nasdaq {comp['chg']:+.2f}%", INK),
         ("BITCOIN", f"${btc['price']:,.0f}", ("live" if LIVE_AT else f"{LAST:%a} close") + " · low ~$62K Sat Nov 14 (CNBC)", INK),
         ("NEXT BIG EVENTS", "Nov 17–25", "Nvidia Tue · Anthropic IPO Thu · Dell Nov 24 · GDP/PCE Nov 25", INK)]
cells = [[Paragraph(X(a), S_LAB), Paragraph(f'<font name="DVB" size="14" color="{c.hexval().replace("0x", "#")}">{X(b)}</font>', st("tv", leading=18)), Paragraph(X(s_), S_M)] for a, b, s_, c in TILES]
tw = (CW - 3 * 6) / 4
tt = Table([cells[0:4], cells[4:8]], colWidths=[tw] * 4, rowHeights=None)
tt = Table([[Table([[x] for x in c], colWidths=[tw - 14]) for c in cells[i:i + 4]] for i in (0, 4)], colWidths=[tw + 6] * 4)
tt.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0, colors.white), ("INNERGRID", (0, 0), (-1, -1), 4, colors.white),
                        ("BACKGROUND", (0, 0), (-1, -1), CHIP), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
for row in tt._cellvalues:
    for inner in row:
        inner.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                   ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
story += [tt, PageBreak()]

# EDIT EACH MONTH (editorial: verified facts only)
# Monday game plan
story += [Paragraph("Tuesday Nov 17 game plan", S_H1),
          Paragraph("What changed this week, what you can and can't trade, and when the system reports in. Facts from CNBC, Bloomberg, Seeking Alpha, Barron's, MarketWatch and Fox Business, plus company releases; " + ("prices are live (" + LIVE_AT + " Tue)." if LIVE_AT else f"prices are {LAST:%A}'s official closes."), S_M), Spacer(1, 6)]
WKND = [
    ("Rules", "<b>Tue Nov 17, Wed Nov 18, Thu Nov 19 and Mon Nov 23 are clear.</b> Fri Nov 20 is out (a Friday). No new options held into reports: NVDA (Nov 17), BABA (Nov 19), HPE (Nov 23), DELL (Nov 24), CRWD and MRVL (Dec 1), ZS (Dec 2), AVGO and ORCL (Dec 9). Wed Nov 25 (GDP, PCE) is Rule 3."),
    ("Nvidia", "Jensen Huang resigned as CEO and from the board Nov 12; CFO Colette Kress is interim CEO and Harvey Jones is chair. NVDA fell as much as 14% that day, 12.75% on the week, and below a $4T value. HSBC cut it to Hold ($170 from $365); UBS trimmed to $240 but expects a $3–4B revenue beat. FT says the board approached Arm's Rene Haas. Earnings Tue after the close: LSEG consensus about $109.1B revenue and $2.47 EPS (CNBC)."),
    ("Results", "<b>CSCO</b>: revenue $18.5B (+24%), Q2 guide above consensus, hyperscaler AI revenue now seen at $9B; still −6.2% Friday. <b>AMAT</b>: revenue $10.4B (+53%), Q1 guide $11.1B, sees 2027 chip-equipment spending up 30%+. <b>CBRS</b>: core revenue $230.9M (+70%), Q4 guide $310–330M, Microsoft deal; +11.2%. <b>NBIS</b>: revenue $980.8M, but 2026 revenue at the low end and capex $27B; −16.8% and −9.9%."),
    ("Rates", "October PPI +0.3% m/m (est. +0.4%) but +6.5% y/y, the most since Nov 2022. Fed's Daly and Hammack said more hikes are needed; a Dec 9 hike is fully priced and Goldman added a March hike. Treasuries had their worst week since April 2025 and the dollar its highest level since then (CNBC, FT)."),
    ("Your lists", "Updated Nov 17 in your broker's order (50 names). Top 5: <b>AMZN, SKHY, AVGO, AMAT, BE</b> (Amazon back on top). 2026 Portfolio: COHR, SPCX, <b>NVDA</b> (moved down from the Top 5), TER, CRDO, NBIS, MRVL, CSCO, HPE, ANET, LRCX, WDC, CIEN, QCOM, CRWD, APH, VICR, LYTE, DRAM, NCLD. 15–50% Dip: DELL, VRT, VST, ARM, INTC, CRWV, CBRS, NOW, KLAC, ALAB, DDOG, HOOD, ZS, IONQ, ORCL, GLW, DOCN, AKAM, FTNT, MSTR, IBIT, COIN, CRCL, BABA, <b>IREN</b> (back on the list)."),
    ("Market", "Last week still ended as the best since early August despite Thursday–Friday losses (CNBC). Monday: S&amp;P 500 −1.92%, Nasdaq −2.49%; optics, neoclouds, memory and AI power led the drop."),
]
wk = Table([[Paragraph(f'<font name="DVB">{X(a)}</font>', S_SM), Paragraph(b, S_B)] for a, b in WKND], colWidths=[0.9 * inch, CW - 0.9 * inch])
wk.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), 0.4, LINE),
                        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                        ("BACKGROUND", (0, 0), (-1, 0), OKBG), ("LINEBEFORE", (0, 0), (0, 0), 3, OK)]))
story += [Paragraph("This week in review", S_H2), wk, Spacer(1, 8)]

# Tuesday's biggest movers on his lists, from official closes
mv = sorted(((t, ST[t]["day"]) for _, _, ns in C.LISTS for t in ns), key=lambda x: x[1])
dn, up = mv[:5], mv[::-1][:5]
def mvcell(xs):
    return Paragraph(" · ".join(f'<font name="DVB">{t}</font> {pc(v, False)}' for t, v in xs), S_B)
mt = Table([[Paragraph("MONDAY'S BIGGEST GAINERS" if up[0][1] > 0 else "HELD UP BEST MONDAY (ALL FELL)", S_LAB), Paragraph("MONDAY'S BIGGEST DECLINERS" if dn[0][1] < 0 else "SMALLEST GAINS MONDAY (ALL ROSE)", S_LAB)], [mvcell(up), mvcell(dn)]],
           colWidths=[CW / 2] * 2)
mt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), CHIP), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LINEAFTER", (0, 0), (0, -1), 4, colors.white), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
story += [mt, Spacer(1, 8)]

# Options status for the next clear days, by rule and IV
ALL = [t for _, _, ns in C.LISTS for t in ns]
blocked, windowed, cheap = [], [], []
for t in ALL:
    tone, _ = rule_note(t, earn_info(t))
    if tone == "bad" or IVF[t]["verdict"] == "Blocked":
        blocked.append(t)
    elif tone == "warn":
        windowed.append(t)
    if IVF[t]["verdict"] == "Cheap":
        cheap.append(t)
def tk(xs):
    return ", ".join(xs) if xs else "none"
OPT = [
    ("bad", "No new options right now", f"{len(blocked)} names: every 7–60 DTE expiry runs into their report (Rules 3 and 4): {tk(blocked)}."),
    ("warn", "Open, with an earnings cutoff", f"{tk(windowed)}: expiries must end before each report; each stock page lists the allowed Fridays."),
]
ot = Table([[Paragraph(f"<b>{X(a)}</b>", S_B), Paragraph(X(b), S_B)] for _, a, b in OPT], colWidths=[1.6 * inch, CW - 1.6 * inch])
os_ = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
       ("LINEBELOW", (0, 0), (-1, -2), 0.5, colors.white)]
for i, (tone, _, _) in enumerate(OPT):
    os_ += [("BACKGROUND", (0, i), (-1, i), TONE[tone][1]), ("LINEBEFORE", (0, i), (0, i), 3, TONE[tone][0])]
ot.setStyle(TableStyle(os_))
story += [Paragraph("Your options on Tue Nov 17", S_H2), Paragraph("Where options look cheap is on page 1.", S_M), Spacer(1, 3), ot, Spacer(1, 8)]

SCHED = [("5:50 AM", "Morning analysis in chat, with a live IV check"),
         ("6:30 AM", "Open; app prices refresh about every 15 min"),
         ("6:32 AM", "Morning briefing in chat and on your phone"),
         ("9:48 AM", "Midday analysis in chat"),
         ("1:00 PM", "Market closes"),
         ("1:50 PM", "After-close analysis with the next day's rule status")]
sc = Table([sum(([Paragraph(f'<font name="DVB">{a}</font>', S_SM), Paragraph(X(b), S_SM)] for a, b in SCHED[i::3]), []) for i in range(3)],
           colWidths=[0.74 * inch, CW / 2 - 0.74 * inch] * 2)
sc.setStyle(TableStyle([("LINEBELOW", (0, 0), (-1, -2), 0.4, LINE), ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))
story += [KeepTogether([Paragraph("Daily schedule (PT)", S_H2), sc]), PageBreak()]

# EDIT EACH MONTH (editorial: verified facts only)
THEMES = [
    ("Nvidia without Jensen Huang", "Huang resigned Nov 12 amid an affair and espionage scandal; CFO Colette Kress runs the company until a successor is named. The stock lost about $1.7T over six losing weeks. Treasury Secretary Bessent wants an outside CEO, while a petition and large holders back Huang's return; Congress is pushing tighter export rules (CNBC). Tuesday's report is the first under the interim CEO: the numbers, the Rubin ramp and any word on the search decide the AI group's next move.", "NVDA, AVGO, AMAT, SKHY, DELL, HPE, VRT, ARM, ALAB, CRDO, COHR, CBRS, CRWV, NBIS"),
    ("Rotation to custom chips and challengers", "Money left Nvidia for Broadcom (+5.5% Thursday) and AMD; Wedbush says 'custom ASICs are where we believe companies want to turn' and Evercore calls Arista the clearest beneficiary of a shift to open Ethernet (CNBC). Cerebras jumped 11% on a beat and a Microsoft deal. Rothschild & Co. cut Broadcom to Neutral on its reliance on OpenAI and Anthropic.", "AVGO, ANET, CBRS, MRVL, CRDO, ALAB, ARM"),
    ("Neoclouds lose their backer", "Nebius guided 2026 revenue to the low end and raised capex to $27B (2027: $40–45B), falling 16.8%; Barron's says CoreWeave and Nebius 'lost a friend in Huang', since Nvidia backs about $36B of their cloud deals. CoreWeave is seeking at least $4B of cheaper high-grade loans; Goldman trimmed its target to $101 (still Buy).", "CRWV, NBIS, NCLD, DOCN, DELL, HPE, BE, VST, VRT"),
    ("Rates: a December hike is priced", "Hot October CPI and PPI (+6.5% y/y) leave a Dec 9 hike fully priced; Goldman added a March hike. The 10-year is above 5.1% and the 30-year near 5.5%; Treasuries had their worst week since April 2025 and the dollar is at its highest since then. FOMC minutes Wednesday; GDP and PCE Nov 25.", "All 50, most of all IONQ, CRWV, NBIS, CBRS, ALAB, NOW, DDOG, ZS, CRWD, MSTR, IBIT"),
    ("Chip equipment and memory", "Applied Materials beat and sees 2027 chip-equipment spending up more than 30%, but the group fell with Nvidia (LRCX −3.4%, KLAC −3.2%, TER −5.4% Friday). Monday SK hynix fell 5.6% in Seoul as the Kospi dropped 3.6% (CNBC). Sen. Cotton wants China's CXMT, the No. 4 DRAM maker, blacklisted: protective for SK hynix.", "AMAT, LRCX, KLAC, TER, SKHY, DRAM, WDC"),
    ("The Anthropic IPO", "Prices Wednesday ($70–78), trades Thursday. Nvidia, Broadcom, Micron, TSMC, AMD, Microsoft and Google are strategic buyers in its $26B placement at the IPO price (CNBC); Amazon is one of its biggest holders. CNBC also flags it as one reason speculative money is leaving bitcoin.", "AMZN, AVGO, NVDA, SKHY, DRAM, AKAM, CBRS"),
    ("Crypto slide", "Bitcoin fell below $70K Friday and to about $62K late Saturday, its lowest since August, on liquidations, a strong dollar and Fed-hike bets; Nansen sees $60–62K as the next test (CNBC). Strategy bought only 485 bitcoin last week and spent $228M buying back preferred stock (SEC). Your new MSTR and IBIT trade directly with bitcoin.", "MSTR, IBIT, COIN, HOOD, CRCL"),
    ("Event risk ahead", "Nvidia Nov 17; FOMC minutes, Palo Alto and Anthropic pricing Nov 18; Anthropic trading and Alibaba Nov 19; HPE Nov 23; Dell Nov 24; GDP and PCE Nov 25; Thanksgiving Nov 26; Nvidia GTC DC and AWS re:Invent from Nov 30; CrowdStrike and Marvell Dec 1; Zscaler Dec 2; jobs Dec 4; FOMC, Broadcom and Oracle Dec 9.", "All 50"),
]
story.append(Paragraph("Market themes that can move your stocks", S_H1))
for a, b, c in THEMES:
    story.append(KeepTogether([Paragraph(X(a), S_H2), Paragraph(X(b), S_B), Paragraph("Most exposed: " + X(c), S_M)]))

# Key dates
# EDIT EACH MONTH (editorial: verified facts only)
MACRO = [
    ("2026-11-17", "5:30 AM", "October retail sales", "m2", ""),
    ("2026-11-17", "all week", "Microsoft Ignite (Nov 17–20) and SC26 supercomputing conference, Chicago (through Nov 20)", "r", ""),
    ("2026-11-18", "11:00 AM", "FOMC minutes (Oct 27–28 meeting)", "m2", ""),
    ("2026-11-18", "after close", "Palo Alto Networks earnings (read-through: CRWD, ZS, FTNT, AKAM)", "r", ""),
    ("2026-11-18", "all day", "Anthropic IPO prices ($70–78 range); trading starts Thu Nov 19", "r", ""),
    ("2026-11-20", "all day", "Monthly options expiration", "m2", ""),
    ("2026-11-25", "5:30 AM", "Q3 GDP (2nd estimate) + October PCE", "m", "rule3"),
    ("2026-11-26", "all day", "Thanksgiving: markets closed (Fri Nov 27 closes 10:00 AM PT)", "m2", ""),
    ("2026-11-30", "all week", "Nvidia GTC DC (Nov 30–Dec 3) and AWS re:Invent (Nov 30–Dec 4)", "r", ""),
    ("2026-12-04", "5:30 AM", "November jobs report", "m", "rule3"),
    ("2026-12-09", "11:00 AM", "FOMC decision", "m", "rule3"),
]
rows = [dict(date=d(a), time=b, what=c, kind=k, flag=f, t=None) for a, b, c, k, f in MACRO]
for key, label, names in C.LISTS:
    for t in names:
        ei = earn_info(t)
        if ei["nxt"] and ei["nxt"] <= dt.date(2026, 12, 10):
            short = "~5:00 PM" if t == "SKHY" else {"AMC": "after close", "BMO": "before open"}.get(K.get(t, {}).get("time") or "", "time TBA")
            eps = f" · est. EPS {eps_s(ei['eps'])}" if ei["eps"] is not None else ""
            rows.append(dict(date=ei["nxt"], time=short, what=f"{C.S[t]['name']} earnings{' (est. date)' if ei['est'] else ''}{eps}", kind="e", flag="earn", t=t))
TRANK = {"all day": 0, "all week": 0, "5:30 AM": 1, "before open": 2, "7:00 AM": 3, "10:00 AM": 3.5, "11:00 AM": 4, "after close": 5, "~5:00 PM": 6, "time TBA": 7, "TBD": 7}
rows.sort(key=lambda r: (r["date"], TRANK[r["time"]], {"m": 0, "m2": 1, "e": 2, "r": 3}[r["kind"]]))
story += [PageBreak(), Paragraph("Key dates through Dec 10 (Pacific Time)", S_H1),
          Paragraph('"No new X options" means none that would be held into that report (Rule 3). Your names\' earnings, the Rule 3 data days, and outside reports that move your names. "Before open" = before 6:30 AM PT; "after close" = after 1:00 PM PT.', S_M), Spacer(1, 6)]
data = [[Paragraph("DATE", S_LAB), Paragraph("TIME", S_LAB), Paragraph("EVENT", S_LAB), Paragraph("YOUR RULES", S_LAB)]]
sty = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
       ("LINEBELOW", (0, 0), (-1, 0), 0.6, LINE)]
last = None
for r in rows:
    i = len(data)
    if r["date"] != last and last is not None:
        sty.append(("LINEABOVE", (0, i), (-1, i), 0.5, LINE))
    dstr = fmt_d(r["date"]) if r["date"] != last else ""
    last = r["date"]
    wt_ = "<b>%s</b>" if r["kind"] == "m" else ("%s" if r["kind"] == "e" else '<font color="#62656e">%s</font>')
    ev = (f'<font name="DVB" color="#1f5fbf">{r["t"]}</font>  ' if r["t"] else "") + wt_ % X(r["what"])
    fl = ""
    if r["flag"] == "rule3":
        fl = '<font color="#b42318"><b>No trades · Rule 3</b></font>'
    elif r["flag"] == "earn":
        fl = f'<font color="#8a5a00">No new {r["t"]} options</font>'
    if r["date"].weekday() == 4:
        fl = (fl + "<br/>" if fl else "") + '<font color="#8a5a00">Friday · Rule 2</font>'
    data.append([Paragraph(f"<b>{dstr}</b>", S_SM), Paragraph(X(r["time"]), st("x", fontSize=8.4, leading=11, textColor=MUT)), Paragraph(ev, S_SM), Paragraph(fl, S_SM)])
ct = Table(data, colWidths=[0.95 * inch, 0.88 * inch, CW - 0.95 * inch - 0.88 * inch - 1.45 * inch, 1.45 * inch], repeatRows=1)
ct.setStyle(TableStyle(sty)); story.append(ct)

# At a glance
story += [PageBreak(), Paragraph(f"All {len(ALL)} at a glance", S_H1),
          Paragraph((f"Prices are live Nasdaq trades at {LIVE_AT} {fmt_d(LAST)}, cross-checked on a second feed; DAY = change from the previous session's official close. " if LIVE_AT else f"Official closes {fmt_d(LAST)}. ") + f"1M = since {fmt_d(ST['AVGO']['m1_from'], False)}; 3M = since {fmt_d(ST['AVGO']['m3_from'], False)}. Sparkline = 3 months, shaded = last month. IV check: see the next page. Red earnings dates are within 21 days.", S_M)]
for key, label, names in C.LISTS:
    data = [[Paragraph(x, S_LAB) for x in ("TICKER", "PRICE" if LIVE_AT else "CLOSE", "DAY", "1M", "3M", "FROM HIGH", "3-MONTH TREND", "IV CHECK", "NEXT EARNINGS")]]
    for t in names:
        s, ei = ST[t], earn_info(t)
        if ei["nxt"]:
            soon = (ei["nxt"] - TODAY).days <= 21
            ne = f'<font color="{"#b42318" if soon else "#1c1d21"}">{"<b>" if soon else ""}{fmt_d(ei["nxt"])}{"</b>" if soon else ""}</font>' + (' <font color="#62656e">est.</font>' if ei["est"] else "")
        else:
            ne = '<font color="#62656e">ETF · no earnings</font>' if t in ETFS else f'<font color="#62656e">Reported {fmt_d(ei["last"], False)}</font>'
        data.append([Paragraph(f'<font name="DVB">{t}</font>', S_SM), Paragraph(f"${s['last']:,.2f}", st("rr", fontSize=8.4, alignment=TA_RIGHT)),
                     Paragraph(pc(s["day"], False), st("rr2", fontSize=8.4, alignment=TA_RIGHT)), Paragraph(pc(s["m1"]), st("rr3", fontSize=8.4, alignment=TA_RIGHT)),
                     Paragraph(pc(s["m3"]), st("rr4", fontSize=8.4, alignment=TA_RIGHT)), Paragraph(pc(s["offhi"], False), st("rr5", fontSize=8.4, alignment=TA_RIGHT)),
                     Image(spark(t), width=1.1 * inch, height=0.23 * inch), Paragraph(vlabel(t), S_SM), Paragraph(ne, S_SM)])
    gt = Table(data, colWidths=[0.68 * inch, 0.76 * inch, 0.62 * inch, 0.66 * inch, 0.74 * inch, 0.78 * inch, 1.14 * inch, 0.78 * inch, CW - 6.16 * inch], repeatRows=1)
    gt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 1.6), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.6),
                            ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE), ("ALIGN", (1, 0), (5, 0), "RIGHT")]))
    story += [KeepTogether([Paragraph(f"{X(label)} <font size='8' color='#62656e'>· {len(names)} names in your order</font>", S_H2), gt])]

# IV check page
# Wall Street price targets summary
# Company summaries: what each company does, all names in one place (also shown at the top of each stock page)
story += [PageBreak(), Paragraph("Company summaries: what each company does", S_H1),
          Paragraph("Every name on your lists in your broker's order, with what the company does and what it specializes in. The same summary opens each stock page.", S_M), Spacer(1, 4)]
S_PF = st("pfs", fontSize=8.2, leading=10.6)
for key, label, names in C.LISTS:
    prow = [[Paragraph(f"<b>{X(label)}</b> · {len(names)} names", S_B), ""]]
    for i, t in enumerate(names, 1):
        prow.append([Paragraph(f'<font name="DVB" color="#1f5fbf">{t}</font><br/><font size="7.4">{X(C.S[t]["name"])}<br/>#{i}</font>', S_SM),
                     Paragraph(X(C.S[t].get("profile") or C.S[t]["what"]), S_PF)])
    ptb = Table(prow, colWidths=[1.15 * inch, CW - 1.15 * inch], repeatRows=1)
    ptb.setStyle(TableStyle([("SPAN", (0, 0), (-1, 0)), ("BACKGROUND", (0, 0), (-1, 0), CHIP), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                             ("LINEBELOW", (0, 1), (-1, -1), 0.4, LINE), ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    story += [ptb, Spacer(1, 8)]

story += [PageBreak(), Paragraph("Wall Street price targets", S_H1),
          Paragraph("Consensus = Nasdaq analyst consensus (average, low–high, buy/hold/sell count). Named targets are the most recent ones reported by your outlets "
                    "(CNBC, Seeking Alpha; \"via TipRanks\" = headline on CNBC's quote page). <b>Bold</b> = JPMorgan, BofA, Morgan Stanley, Goldman Sachs, Oppenheimer, Mizuho. "
                    "Dates and sources are on each stock page. Many targets were set before October's selloff, so the upside looks large; watch for cuts after earnings.", S_M), Spacer(1, 4)]
S_T7 = st("t7", fontSize=7.4, leading=9.2)
S_T7R = st("t7r", fontSize=7.4, leading=9.2, alignment=TA_RIGHT)
pdata = [[Paragraph(x, S_LAB) for x in ("TICKER", "PRICE" if LIVE_AT else "CLOSE", "AVG", "UPSIDE", "LOW–HIGH", "B/H/S", "NAMED FIRM TARGETS")]]
psty = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 1.3), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.3), ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE)]
for key, label, names in C.LISTS:
    psty += [("BACKGROUND", (0, len(pdata)), (-1, len(pdata)), CHIP), ("SPAN", (0, len(pdata)), (-1, len(pdata)))]
    pdata.append([Paragraph(f"<b>{X(label)}</b>", S_T7)] + [""] * 6)
    for t in names:
        c, last = PT.get(t), ST[t]["last"]
        pdata.append([Paragraph(f"<b>{t}</b>", S_T7), Paragraph(f"${last:,.2f}", S_T7R),
                      Paragraph(f'${c["priceTarget"]:,.0f}' if c else "–", S_T7R),
                      Paragraph(pc((c["priceTarget"] / last - 1) * 100, False) if c else "–", S_T7R),
                      Paragraph(f'${c["lowPriceTarget"]:,.0f}–${c["highPriceTarget"]:,.0f}' if c else "–", S_T7R),
                      Paragraph(f'{c["buy"]}/{c["hold"]}/{c["sell"]}' if c else "–", S_T7R),
                      Paragraph(" · ".join(pt_named(t, short=True)) or ('<font color="#62656e">ETF: no analyst targets</font>' if t in ETFS else '<font color="#62656e">none reported recently</font>'), S_T7)])
ptab = Table(pdata, colWidths=[0.7 * inch, 0.66 * inch, 0.62 * inch, 0.7 * inch, 0.92 * inch, 0.55 * inch, CW - 4.15 * inch], repeatRows=1)
ptab.setStyle(TableStyle(psty))
story.append(KeepInFrame(CW, FRAME_H - 60, [ptab], mode="shrink"))

IVP_START = PageBreak()
story += [IVP_START, Paragraph("Options IV check: are the options you're allowed to buy cheap?", S_H1),
          Paragraph(f"For each name, I took the expiry your rules allow (7–60 DTE from {fmt_d(NEXT_SESSION)}, ending before the next report) closest to 30 days. Its at-the-money implied volatility (IV) is compared with how much the stock has actually moved over the last 20 trading days (HV).", S_B), Spacer(1, 3),
          Paragraph('<font color="#13804a"><b>Cheap</b></font>: IV below actual movement (ratio under 1.0); the better time to buy. <b>Normal</b>: ratio 1.0–1.5. <font color="#b42318"><b>Expensive</b></font>: ratio 1.5 or more; you pay up and need a bigger move. <b>after earn.</b> = every allowed expiry runs into earnings, so no new options yet (Rule 3); the verdict and IV marked * are estimated without the earnings move, from two expiries after the report (term structure), so you know where each name stands once it has reported.', S_B), Spacer(1, 3),
          Paragraph((f"Source: Nasdaq delayed option quotes taken intraday Tuesday ({LIVE_AT}), priced off the live stock price (mid of bid/ask)" if LIVE_AT else f"Source: Nasdaq delayed option quotes at {LAST:%A} {fmt_d(LAST, False)}'s close (mid of bid/ask)") + f", IV solved with Black-Scholes; HV from official closes. This compares IV with actual movement, not a true IV rank, because I don't have a verified year of IV history. Earnings move = straddle price on the first expiry after the report. Quotes change daily; check live before trading.", S_M), Spacer(1, 8)]
data = [[Paragraph(x, S_LAB) for x in ("TICKER", "IV CHECK", "IV", "HV (20D)", "RATIO", "EXPIRY USED", "EARNINGS MOVE", "NOTE")]]
sty = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 1.1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.1), ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE)]
S_T8 = st("t8", fontSize=8, leading=10)
S_T8R = st("t8r", fontSize=8, leading=10, alignment=TA_RIGHT)
for key, label, names in C.LISTS:
    sty += [("BACKGROUND", (0, len(data)), (-1, len(data)), CHIP), ("SPAN", (0, len(data)), (-1, len(data)))]
    data.append([Paragraph(f"<b>{X(label)}</b>", S_T8)] + [""] * 7)
    for t in names:
        v, ei = IVF[t], earn_info(t)
        xv = v.get("ex") if v["verdict"] == "Blocked" else None
        em = f'±{v["em"]["move"]:.1f}% by {fmt_d(dt.date.fromisoformat(v["em"]["exp"]), False)}' if v["em"] else (f'±{xv["jump"]:.1f}% on report day (est.)' if xv else '<font color="#62656e">Report too far out</font>' if ei["nxt"] else '<font color="#62656e">' + ("ETF · no earnings" if t in ETFS else "Already reported") + '</font>')
        notes = []
        if v["verdict"] == "Blocked":
            notes.append(f'After earnings {fmt_d(ei["nxt"], False)} (est.); buy from {fmt_d(first_buy(t, ei), False)}')
        if t in POST_LIVE:
            notes.append("Live Nov 6 quotes (new name)" if POST_LIVE[t] == NEW_LIVE else "Live Nov 4 quotes, post-report")
        if v["hv_has_earn"]:
            notes.append("HV has earnings move")
        if v["wide"]:
            notes.append("Wide quotes")
        data.append([Paragraph(f"<b>{t}</b>", S_T8), Paragraph(vlabel(t), S_T8),
                     Paragraph(f'{v["iv"]:.0f}%' if v["iv"] else (f'{xv["iv"]:.0f}%*' if xv else "–"), S_T8R), Paragraph(f'{v["hv"]:.0f}%', S_T8R),
                     Paragraph(f'{v["ratio"]:.2f}' if v["ratio"] else (f'{xv["ratio"]:.2f}*' if xv else "–"), S_T8R),
                     Paragraph(f'{fmt_d(dt.date.fromisoformat(v["exp"]), False)} ({v["dte"]}d)' if v["exp"] else "–", S_T8),
                     Paragraph(em, S_T8), Paragraph("; ".join(notes), st("t8m", fontSize=7.4, leading=9.5, textColor=WARN))])
it = Table(data, colWidths=[0.72 * inch, 0.75 * inch, 0.52 * inch, 0.65 * inch, 0.55 * inch, 0.95 * inch, 1.45 * inch, CW - 5.59 * inch], repeatRows=1)
it.setStyle(TableStyle(sty))
ivp = story.index(IVP_START)
story[ivp + 1:] = [KeepInFrame(CW, FRAME_H - 2, story[ivp + 1:] + [it], mode="shrink")]

# Stock pages
for key, label, names in C.LISTS:
    for t in names:
        s, ei, info = ST[t], earn_info(t), C.S[t]
        lab, pos, tot = LISTPOS[t]
        tone, rn = rule_note(t, ei)
        f = [PageBreak()]
        head = Table([[Paragraph(f'{t} <font name="DV" size="14">{X(info["name"])}</font>', S_TICK),
                       Paragraph(f'<font color="#62656e">{X(lab)} · #{pos} of {tot}</font>', st("hr", alignment=TA_RIGHT, fontSize=9))]],
                     colWidths=[CW * 0.68, CW * 0.32])
        head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "BOTTOM"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                  ("LINEBELOW", (0, 0), (-1, -1), 1.2, INK), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
        f += [head, Spacer(1, 4), box([Paragraph('<font color="#1f5fbf"><b>WHAT IT DOES</b></font>  ' + X(info.get("profile") or info["what"]), st("pf", fontSize=8.8, leading=11.6))], ACCBG, pad=6), Spacer(1, 6)]
        hi_d = s["hiDate"].replace(", 2026", "").replace(", 2025", " 2025")
        vals = [(PXLAB, f'<font name="DVB" size="13">${s["last"]:,.2f}</font>'),
                ("DAY", pc(s["day"], size=12)), ("1 WEEK", pc(s["wk"], size=12)),
                ("1 MONTH", pc(s["m1"], size=12)), ("3 MONTHS", pc(s["m3"], size=12)),
                (f"FROM HIGH (${s['hi']:,.2f}, {hi_d})", pc(s["offhi"], size=12))]
        sw = [1.15, 0.92, 0.88, 0.92, 0.95]
        sw = [x * inch for x in sw] + [CW - sum(sw) * inch]
        stt = Table([[Paragraph(a, S_LAB) for a, _ in vals], [Paragraph(b, st("v", leading=16)) for _, b in vals]], colWidths=sw)
        stt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), CHIP), ("LEFTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, 0), 5),
                                 ("BOTTOMPADDING", (0, -1), (-1, -1), 5), ("TOPPADDING", (0, 1), (-1, 1), 0), ("LINEAFTER", (0, 0), (-2, -1), 0.6, colors.white)]))
        f += [stt, Spacer(1, 4), Image(chart(t), width=CW, height=CW * 1.9 / 7.3),
              Paragraph(f"3 months of daily closes ({fmt_d(s['m3_from'], False)} to {fmt_d(LAST, False)}{', last point live at ' + LIVE_AT if LIVE_AT else ''}); shaded = last month. Intraday ranges: 1 month ${s['lo1']:,.2f}–${s['hi1']:,.2f}; 3 months ${s['lo3']:,.2f}–${s['hi3']:,.2f}.", S_M),
              Spacer(1, 6)]
        if ei["nxt"]:
            days = (ei["nxt"] - TODAY).days
            red = days <= 21
            e1 = f'<font color="{"#b42318" if red else "#1c1d21"}"><b>{fmt_d(ei["nxt"])}</b></font>{" (est.)" if ei["est"] else ""} · {X(ei["when"])} · in {days} days'
        else:
            e1 = "<b>None</b> · an ETF does not report earnings" if t in ETFS else f"<b>Not set</b> · last reported {fmt_d(ei['last'])}"
        er = [[Paragraph("NEXT EARNINGS", S_LAB), Paragraph(e1, S_B)]]
        if ei["eps"] is not None:
            e2 = f"<b>{eps_s(ei['eps'])}</b>" + (f" vs {eps_s(ei['prior'])} a year ago" if ei["prior"] is not None else "") + (f" · {ei['n']} analyst{'s' if ei['n'] != '1' else ''}" if ei["n"] else "")
            er.append([Paragraph("CONSENSUS EPS", S_LAB), Paragraph(e2, S_B)])
        fg, bg = TONE[tone]
        er.append([Paragraph("OPTIONS WINDOW", S_LAB), Paragraph(f'<font color="{fg.hexval().replace("0x", "#")}">{X(rn)}</font>', S_B)])
        wi = len(er) - 1
        er += [[Paragraph(a, S_LAB), Paragraph(b, S_B)] for a, b in iv_rows(t, ei)]
        et = Table(er, colWidths=[1.25 * inch, CW - 1.25 * inch])
        et.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), ACCBG), ("BACKGROUND", (0, wi), (-1, wi), bg), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5), ("LEFTPADDING", (0, 0), (-1, -1), 7),
                                ("LINEBEFORE", (0, 0), (0, -1), 3, ACC)]))
        f += [et, Spacer(1, 6)]

        def bl(xs):
            return "<br/>".join("•  " + X(x) for x in xs)
        sec = [("LATEST RESULTS", X(info["results"])), ("GUIDANCE", X(info["guide"])), ("2026 CAPEX", X(info["capex"])),
               ("CURRENT PARTNERSHIPS", bl(info["partners"])), ("CATALYSTS", bl(info["catalysts"])),
               ("MARKET EVENTS", X(info["macro"])), ("RISKS", X(info["risks"])),
               ("WALL STREET TARGETS", pt_cons(t, s["last"]) + ("<br/>" + " · ".join(pt_named(t)) if TG.T.get(t) else "" if t in ETFS else "<br/><font color=\"#62656e\">No named firm target reported recently in your outlets.</font>"))]
        dt_ = Table([[Paragraph(a, S_LAB), Paragraph(b, S_B)] for a, b in sec], colWidths=[1.35 * inch, CW - 1.35 * inch])
        dt_.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEABOVE", (0, 1), (-1, -1), 0.5, LINE), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                 ("TOPPADDING", (0, 0), (-1, -1), 3.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2)]))
        src = " · ".join(f'<a href="{X(u)}" color="#1f5fbf">{X(l)}</a>' for l, u in info["src"])
        f += [dt_, Spacer(1, 5), Paragraph("<b>SOURCES</b>  " + src, st("src", fontSize=7.4, leading=10, textColor=MUT))]
        # one page per stock, always: shrink the page slightly if the content runs long
        story += [f[0], KeepInFrame(CW, FRAME_H - 2, f[1:], mode="shrink")]

doc.build(story)
print("wrote", OUT)
