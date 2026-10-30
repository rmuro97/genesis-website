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
TODAY = dt.date(2026, 11, 2)
NEXT_SESSION = dt.date(2026, 11, 2)
LAST = max(dt.date.fromisoformat(r[-1][0]) for r in H.values())  # last official close in pdf/hist.json
# EDIT EACH MONTH: Rule 3 data days (FOMC, CPI, PCE, PPI, jobs, GDP) and market holidays for the next ~2 months
RULE3_DAYS = {dt.date(2026, 10, 28), dt.date(2026, 10, 29), dt.date(2026, 11, 6), dt.date(2026, 11, 10), dt.date(2026, 11, 13),
              dt.date(2026, 11, 25), dt.date(2026, 12, 4), dt.date(2026, 12, 9), dt.date(2026, 12, 10)}
HOLIDAYS = {dt.date(2026, 11, 26), dt.date(2026, 12, 25)}
# EDIT EACH MONTH: names that reported after the last close in hist.json: their option prices predate the report
PRE_REPORT = set()
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
TIME_OVERRIDE = {"SKHY": "evening, by ~5:00 PM PT (before 9:00 AM Seoul Oct 28)"}


def earn_info(t):
    p, k = PX[t], K.get(t, {})
    return dict(nxt=d(p.get("earn")), last=d(p.get("earnLast")),
                when=TIME_OVERRIDE.get(t) or TIME_PT.get(k.get("time") or "", "time not announced"),
                est=k.get("status") == "estimated", eps=num(k.get("eps")), prior=num(k.get("prior")), n=k.get("n"))


def rule_note(t, ei):
    nxt = ei["nxt"]
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
    base3 = max(i for i, x in enumerate(ds) if x <= LAST - dt.timedelta(days=92))
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
    c = PT.get(t)
    if not c:
        return "No Nasdaq consensus yet (recent U.S. listing)."
    up = (c["priceTarget"] / last - 1) * 100
    return (f'Consensus <b>${c["priceTarget"]:,.0f}</b> ({pc(up, False)} vs close) · range ${c["lowPriceTarget"]:,.0f}–${c["highPriceTarget"]:,.0f} · '
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
        if t in PRE_REPORT:
            txt += f' <font color="#8a5a00">These option prices are from before its {fmt_d(ei["last"], False)} after-close report; recheck live before buying.</font>'
        elif v["hv_has_earn"]:
            txt += f' <font color="#8a5a00">Actual movement includes the {fmt_d(ei["last"], False)} earnings move, so "cheap" may be overstated.</font>'
        if v["wide"]:
            txt += ' <font color="#8a5a00">Wide bid/ask at the last close; check live quotes.</font>'
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
M1 = TODAY.replace(day=1); M2 = (M1 + dt.timedelta(days=32)).replace(day=1)
EDITION = f"{M1:%B}–{M2:%B} Opportunities {M2.year if M1.month == 12 else M1.year}"
TITLE = f"Stock Analysis: {EDITION}"
OUT = os.path.join(HERE, f"Stock_Analysis_{M1:%B}-{M2:%B}_Opportunities_{M2.year if M1.month == 12 else M1.year}.pdf")
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
                      subject="Earnings, guidance, capex, partnerships, catalysts and market events for 39 stocks")
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
story += [Paragraph("MURO'S INVESTING ANALYSIS · MONTHLY STOCK ANALYSIS", S_LAB), Spacer(1, 4),
          Paragraph("Stock Analysis", S_T), Spacer(1, 2),
          Paragraph(X(EDITION), st("sub", fontName="DVB", fontSize=15, leading=19, textColor=ACC)), Spacer(1, 6),
          Paragraph("All 39 names on your lists, in your order: 3-month price charts, price moves, earnings, guidance, capex, partnerships, catalysts and the market events that can move each one. Updated for Monday Nov 2, 2026: your Oct 30 lists (INTC and AMZN now in the Top 5; GOOGL, HPE, FTNT and NOW added; LRCX removed), this week's results (SK hynix, Teradyne, Corning, Robinhood, Vertiv, KLA, Alphabet, Fortinet, ServiceNow, Amazon, Intel, Coinbase), the Fed's hold and Friday's tech selloff. Prices are official Nasdaq closes through Friday Oct 30. Times are Pacific.", S_BL),
          Spacer(1, 5),
          Paragraph("Charts show 3 months of daily closes, which shows each stock's trend and how far it has pulled back; the shaded band is the last month. Decision support, not advice. News facts come from CNBC, Bloomberg, Fox Business, WSJ, Seeking Alpha and Al Jazeera, plus company releases and filings. Consensus EPS is from Nasdaq. Earnings dates marked \"est.\" are not confirmed by the company.", S_M),
          ]
# EDIT EACH MONTH (editorial: verified facts only)
WEEK = [
    ("Mon Nov 2", "ok", "Clear for trading. Aehr and Apple report after the close, so no new AEHR options."),
    ("Tue Nov 3", "ok", "Clear for trading, but it's Election Day. DigitalOcean reports before the open (no new DOCN options); AMD, Arista, Astera Labs and Super Micro after the close."),
    ("Wed Nov 4", "ok", "Clear for trading. Circle reports before the open; Coherent, Arm and Qualcomm after the close (no new options on those four)."),
    ("Thu Nov 5", "ok", "Clear for trading. Akamai, IonQ, Applied Optoelectronics and IREN report (no new options on those four)."),
    ("Fri Nov 6", "bad", "October jobs report at 5:30 AM PT and a Friday, so no new trades (Rules 2 and 3). Vistra reports."),
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
    if t in PRE_REPORT:
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
bt = Table(brows, colWidths=[0.62 * inch, 1.02 * inch, 0.7 * inch, 1.34 * inch, 1.12 * inch, 1.16 * inch, CW - 5.96 * inch], repeatRows=1)
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
          Paragraph("Quotes are Nasdaq delayed option prices at the last close; recheck live before buying. A cheap reading is not a buy signal on its own.", S_M),
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
at = Table(arows, colWidths=[0.62 * inch, 1.02 * inch, 1.0 * inch, 1.05 * inch, 1.45 * inch, 0.72 * inch, CW - 5.86 * inch], repeatRows=1)
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
          box([Paragraph('<font color="#b42318"><b>Headwind.</b></font> The market turned on AI spending this week. Alphabet had its worst day ever (−12.6%) on a search miss and cash burn, Amazon's $77B quarterly capex drove free cash flow to −$42B, and Intel's guide sank it ~31% Friday. Add a Fed that held but leans toward a December hike, 3.6% PCE inflation, a 10-year near 4.9%, Brent near $115 and a record $6.3B crypto hack. The offset: capex budgets were held, not cut, and Vertiv, KLA and SK hynix posted blowout quarters.', S_B)], BADBG),
          Spacer(1, 6)]
BRENT = ("$114.88", "Thu Oct 29 settle (CNBC) · eased on U.S.–Iran talk reports")
spx, comp, y10, y30, btc = MK["SPX"], MK["COMP"], MK["US10Y"], MK["US30Y"], MK["BTC"]
# EDIT EACH MONTH (editorial: verified facts only; the Headwind box above too)
TILES = [("FED FUNDS", "3.75–4.00%", "Held Oct 28 (10–2, two wanted a hike) · Dec hike odds ~83% (CNBC)", BAD),
         ("PCE (SEP)", "3.6% y/y", "Core 3.1% · Q3 GDP +3.4% (CNBC)", BAD),
         ("CPI (SEP)", "3.7% y/y", "October CPI Tue Nov 10 (Rule 3 day)", BAD),
         ("10-YR YIELD", f"{y10['price']:.2f}%", f"30-yr {y30['price']:.2f}% · Fri close", WARN),
         ("BRENT CRUDE", BRENT[0], BRENT[1], BAD),
         ("S&P 500", f"{spx['price']:,.0f}", f"{spx['chg']:+.2f}% Fri · Nasdaq {comp['chg']:+.2f}%", INK),
         ("BITCOIN", f"${btc['price']:,.0f}", f"{btc['chg']:+.2f}% Fri · Binance $6.3B hack", INK),
         ("NEXT BIG EVENTS", "Nov 3–6", "Election Tue · jobs report Fri", INK)]
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
story += [Paragraph("Monday Nov 2 game plan", S_H1),
          Paragraph("What changed this week, what you can and can't trade, and when the system reports in. Facts from CNBC, Bloomberg, Fox Business and Seeking Alpha; prices are Friday's official closes.", S_M), Spacer(1, 6)]
WKND = [
    ("Rules", "<b>Mon Nov 2 through Thu Nov 5 are clear</b> (Tuesday is Election Day). Fri Nov 6 is out: jobs report (Rule 3) and Friday (Rule 2). This week's reporters (AEHR, DOCN, CRCL, COHR, ARM, QCOM, AKAM, IONQ, AAOI, IREN, VST): no new options held into their reports. Your SKHY + AVGO entry check runs Monday at 7:40 AM PT."),
    ("AI spending", "Alphabet fell 12.6% Thu, its worst day ever (~$500B), on a search miss and negative free cash flow (CNBC, Fox Business). Amazon missed on sales and EPS; AWS grew 39% but capex hit $77.3B (CNBC). Microsoft beat with Azure +48% but trimmed capex to $170B on chip-supply delays. All held or trimmed budgets; none cut. Friday the Nasdaq was −3.6% at 11:30 AM PT."),
    ("Results", "<b>VRT</b> +16% Wed: sales +61%, orders +100%+, 2026 raised to $7.15 EPS. <b>KLAC</b> beat and guided $4.5–4.9B; sees 2027 WFE above $200B. <b>INTC</b> beat but guided Q4 to $0.25 EPS on a PC slowdown; ~−31% Fri, worst day since 1974. <b>COIN</b> revenue $1.20B missed. <b>SKHY</b> +11% in Seoul Wed after its record quarter."),
    ("Fed and data", "Fed held at 3.75–4.00% Wed, 10–2 (Cook and Hammack wanted a hike). Warsh gave no guidance; December hike odds rose to ~83% (CNBC). Q3 GDP +3.4% beat; September PCE 3.6% y/y, core 3.1% (CNBC)."),
    ("Your lists", "Updated Oct 30 in your broker's order. Top 5: <b>SKHY, INTC, AVGO, AMZN, SPCX</b> (TER and GLW moved to the Portfolio). 2026 Portfolio now starts with MRVL and adds <b>GOOGL</b> and IONQ. 15–50% Dip adds <b>HPE, FTNT and NOW</b>. LRCX is off. 39 names."),
    ("Software hit", "<b>NOW</b> fell 27% Thu (record) on weaker cRPO guidance despite a beat and AI contract value up 65% (CNBC). <b>FTNT</b> fell ~21–25% on a gross-margin miss despite raising billings guidance again (Seeking Alpha). AI-disruption fears are hitting software."),
    ("Deals and crypto", "<b>MRVL</b> is in advanced talks to buy Lumentum in an all-stock deal (Bloomberg); MRVL fell 11%+. Binance lost a record $6.3B to a hack (Bloomberg); bitcoin fell under $77K and Circle froze $800M of USDC tied to it (CNBC)."),
]
]
wk = Table([[Paragraph(f'<font name="DVB">{X(a)}</font>', S_SM), Paragraph(b, S_B)] for a, b in WKND], colWidths=[0.75 * inch, CW - 0.75 * inch])
wk.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -2), 0.4, LINE),
                        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                        ("BACKGROUND", (0, 0), (-1, 0), OKBG), ("LINEBEFORE", (0, 0), (0, 0), 3, OK)]))
story += [Paragraph("This week in review", S_H2), wk, Spacer(1, 8)]

# Friday's biggest movers on his lists, from official closes
mv = sorted(((t, ST[t]["day"]) for _, _, ns in C.LISTS for t in ns), key=lambda x: x[1])
dn, up = mv[:5], mv[::-1][:5]
def mvcell(xs):
    return Paragraph(" · ".join(f'<font name="DVB">{t}</font> {pc(v, False)}' for t, v in xs), S_B)
mt = Table([[Paragraph("FRIDAY'S BIGGEST GAINERS", S_LAB), Paragraph("FRIDAY'S BIGGEST DECLINERS", S_LAB)], [mvcell(up), mvcell(dn)]],
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
story += [Paragraph("Your options on Mon Nov 2", S_H2), Paragraph("Where options look cheap is on page 1.", S_M), Spacer(1, 3), ot, Spacer(1, 8)]

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
    ("AI spending under scrutiny", "The market now rewards companies that show a return on AI spending and punishes cash burn. Alphabet had its worst day ever, Amazon's free cash flow is −$42.4B over 12 months, and Intel's weak guide hit the whole chip group Friday. But budgets were held (Amazon $220B, Alphabet $195–205B) or trimmed only for supply (Microsoft $170B), so suppliers' orders are still intact: Vertiv's orders doubled and KLA raised its outlook.", "NVDA, AVGO, MRVL, CRDO, CIEN, COHR, GLW, NOK, AAOI, VRT, AMZN, ORCL, CRWV, NBIS"),
    ("Rates and the Fed", "The Fed held Oct 28 but two officials wanted a hike, and December hike odds rose to ~83% (CNBC). September PCE ran 3.6% with core at 3.1%, and Q3 GDP grew 3.4%. October CPI (Tue Nov 10) is the next big test. The 10-year near 4.9% keeps pressure on high-multiple names.", "All 36, most of all IONQ, CRWV, NBIS, IREN, AAOI, CBRS, AEHR, NOW"),
    ("Memory and chip equipment", "SK hynix's record quarter (80% operating margin) and KLA's outlook (2027 wafer-equipment spending above $200B) show the supply chain is still booming, even as memory costs squeeze PCs (Intel) and handsets. Applied Materials reports Nov 12; Aehr reports Nov 2.", "SKHY, TER, AEHR, AMAT, KLAC, INTC, QCOM"),
    ("Optics consolidation", "Marvell is in advanced talks to buy Lumentum, whose CEO says optical parts are sold out into early 2029 (Bloomberg). A deal would reshape the optics group; Coherent reports Wed Nov 4 and AAOI Thu Nov 5.", "MRVL, COHR, AAOI, CIEN, CRDO, GLW, NOK, AVGO"),
    ("Crypto shock", "Binance's $6.3B hack (Oct 29), attributed to North Korea's TraderTraitor, pushed bitcoin under $77K. Binance says it will cover losses; about $3B was frozen, including $800M of USDC by Circle (Bloomberg, CNBC). Coinbase also missed on revenue.", "COIN, HOOD, CRCL, IREN"),
    ("Oil", "Brent settled at $114.88 Thursday, easing on reports of renewed U.S.–Iran talks, with Houthi and post-election military risks still in play (CNBC). Higher oil feeds inflation and keeps the Fed hawkish.", "VST, BE, broad market"),
    ("Event risk ahead", "Midterm elections Tue Nov 3; jobs report Fri Nov 6; CPI Tue Nov 10; Nvidia earnings Nov 17 (the biggest single read-through for the AI names); Nvidia GTC DC and AWS re:Invent Nov 30–Dec 4.", "All 36"),
]
story.append(Paragraph("Market themes that can move your stocks", S_H1))
for a, b, c in THEMES:
    story.append(KeepTogether([Paragraph(X(a), S_H2), Paragraph(X(b), S_B), Paragraph("Most exposed: " + X(c), S_M)]))

# Key dates
# EDIT EACH MONTH (editorial: verified facts only)
MACRO = [
    ("2026-11-02", "after close", "Apple earnings", "r", ""),
    ("2026-11-03", "all day", "U.S. midterm elections; AMD, Arista, Astera Labs and Super Micro earnings", "r", ""),
    ("2026-11-06", "5:30 AM", "October jobs report", "m", "rule3"),
    ("2026-11-10", "5:30 AM", "October CPI: first CPI after the Oct 28 FOMC", "m", "rule3"),
    ("2026-11-13", "5:30 AM", "October PPI (date to confirm)", "m", "rule3"),
    ("2026-11-18", "11:00 AM", "FOMC minutes (estimated date)", "m2", ""),
    ("2026-11-20", "all day", "Monthly options expiration", "m2", ""),
    ("2026-11-25", "5:30 AM", "Q3 GDP (2nd estimate) + October PCE", "m", "rule3"),
    ("2026-11-26", "all day", "Thanksgiving: markets closed (Fri Nov 27 closes 10:00 AM PT)", "m2", ""),
    ("2026-11-30", "all week", "Nvidia GTC DC (Nov 30–Dec 3) and AWS re:Invent (Nov 30–Dec 4)", "r", ""),
    ("2026-12-04", "5:30 AM", "November jobs report", "m", "rule3"),
]
rows = [dict(date=d(a), time=b, what=c, kind=k, flag=f, t=None) for a, b, c, k, f in MACRO]
for key, label, names in C.LISTS:
    for t in names:
        ei = earn_info(t)
        if ei["nxt"] and ei["nxt"] <= dt.date(2026, 12, 10):
            short = "~5:00 PM" if t == "SKHY" else {"AMC": "after close", "BMO": "before open"}.get(K.get(t, {}).get("time") or "", "time TBA")
            eps = f" · est. EPS {eps_s(ei['eps'])}" if ei["eps"] is not None else ""
            rows.append(dict(date=ei["nxt"], time=short, what=f"{C.S[t]['name']} earnings{' (est. date)' if ei['est'] else ''}{eps}", kind="e", flag="earn", t=t))
TRANK = {"all day": 0, "all week": 0, "5:30 AM": 1, "before open": 2, "7:00 AM": 3, "11:00 AM": 4, "after close": 5, "~5:00 PM": 6, "time TBA": 7, "TBD": 7}
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
story += [PageBreak(), Paragraph("All 39 at a glance", S_H1),
          Paragraph(f"Official closes {fmt_d(LAST)}. 1M = since {fmt_d(ST['AVGO']['m1_from'], False)}; 3M = since {fmt_d(ST['AVGO']['m3_from'], False)}. Sparkline = 3 months, shaded = last month. IV check: see the next page. Red earnings dates are within 21 days.", S_M)]
for key, label, names in C.LISTS:
    data = [[Paragraph(x, S_LAB) for x in ("TICKER", "CLOSE", "DAY", "1M", "3M", "FROM HIGH", "3-MONTH TREND", "IV CHECK", "NEXT EARNINGS")]]
    for t in names:
        s, ei = ST[t], earn_info(t)
        if ei["nxt"]:
            soon = (ei["nxt"] - TODAY).days <= 21
            ne = f'<font color="{"#b42318" if soon else "#1c1d21"}">{"<b>" if soon else ""}{fmt_d(ei["nxt"])}{"</b>" if soon else ""}</font>' + (' <font color="#62656e">est.</font>' if ei["est"] else "")
        else:
            ne = f'<font color="#62656e">Reported {fmt_d(ei["last"], False)}</font>'
        data.append([Paragraph(f'<font name="DVB">{t}</font>', S_SM), Paragraph(f"${s['last']:,.2f}", st("rr", fontSize=8.4, alignment=TA_RIGHT)),
                     Paragraph(pc(s["day"], False), st("rr2", fontSize=8.4, alignment=TA_RIGHT)), Paragraph(pc(s["m1"]), st("rr3", fontSize=8.4, alignment=TA_RIGHT)),
                     Paragraph(pc(s["m3"]), st("rr4", fontSize=8.4, alignment=TA_RIGHT)), Paragraph(pc(s["offhi"], False), st("rr5", fontSize=8.4, alignment=TA_RIGHT)),
                     Image(spark(t), width=1.1 * inch, height=0.23 * inch), Paragraph(vlabel(t), S_SM), Paragraph(ne, S_SM)])
    gt = Table(data, colWidths=[0.58 * inch, 0.76 * inch, 0.62 * inch, 0.66 * inch, 0.74 * inch, 0.78 * inch, 1.14 * inch, 0.78 * inch, CW - 6.06 * inch], repeatRows=1)
    gt.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 1.6), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.6),
                            ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE), ("ALIGN", (1, 0), (5, 0), "RIGHT")]))
    story += [KeepTogether([Paragraph(f"{X(label)} <font size='8' color='#62656e'>· {len(names)} names in your order</font>", S_H2), gt])]

# IV check page
# Wall Street price targets summary
story += [PageBreak(), Paragraph("Wall Street price targets", S_H1),
          Paragraph("Consensus = Nasdaq analyst consensus (average, low–high, buy/hold/sell count). Named targets are the most recent ones reported by your outlets "
                    "(CNBC, Seeking Alpha; \"via TipRanks\" = headline on CNBC's quote page). <b>Bold</b> = JPMorgan, BofA, Morgan Stanley, Goldman Sachs, Oppenheimer, Mizuho. "
                    "Dates and sources are on each stock page. Many targets were set before October's selloff, so the upside looks large; watch for cuts after earnings.", S_M), Spacer(1, 4)]
S_T7 = st("t7", fontSize=7.4, leading=9.2)
S_T7R = st("t7r", fontSize=7.4, leading=9.2, alignment=TA_RIGHT)
pdata = [[Paragraph(x, S_LAB) for x in ("TICKER", "CLOSE", "AVG", "UPSIDE", "LOW–HIGH", "B/H/S", "NAMED FIRM TARGETS")]]
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
                      Paragraph(" · ".join(pt_named(t, short=True)) or '<font color="#62656e">none reported recently</font>', S_T7)])
ptab = Table(pdata, colWidths=[0.6 * inch, 0.66 * inch, 0.62 * inch, 0.7 * inch, 0.92 * inch, 0.55 * inch, CW - 4.05 * inch], repeatRows=1)
ptab.setStyle(TableStyle(psty))
story.append(KeepInFrame(CW, FRAME_H - 60, [ptab], mode="shrink"))

IVP_START = PageBreak()
story += [IVP_START, Paragraph("Options IV check: are the options you're allowed to buy cheap?", S_H1),
          Paragraph(f"For each name, I took the expiry your rules allow (7–60 DTE from {fmt_d(NEXT_SESSION)}, ending before the next report) closest to 30 days. Its at-the-money implied volatility (IV) is compared with how much the stock has actually moved over the last 20 trading days (HV).", S_B), Spacer(1, 3),
          Paragraph('<font color="#13804a"><b>Cheap</b></font>: IV below actual movement (ratio under 1.0); the better time to buy. <b>Normal</b>: ratio 1.0–1.5. <font color="#b42318"><b>Expensive</b></font>: ratio 1.5 or more; you pay up and need a bigger move. <b>after earn.</b> = every allowed expiry runs into earnings, so no new options yet (Rule 3); the verdict and IV marked * are estimated without the earnings move, from two expiries after the report (term structure), so you know where each name stands once it has reported.', S_B), Spacer(1, 3),
          Paragraph(f"Source: Nasdaq delayed option quotes at {LAST:%A} {fmt_d(LAST, False)}'s close (mid of bid/ask), IV solved with Black-Scholes; HV from official closes. This compares IV with actual movement, not a true IV rank, because I don't have a verified year of IV history. Earnings move = straddle price on the first expiry after the report. Quotes change daily; check live before trading.", S_M), Spacer(1, 8)]
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
        em = f'±{v["em"]["move"]:.1f}% by {fmt_d(dt.date.fromisoformat(v["em"]["exp"]), False)}' if v["em"] else (f'±{xv["jump"]:.1f}% on report day (est.)' if xv else '<font color="#62656e">Report too far out</font>' if ei["nxt"] else '<font color="#62656e">Already reported</font>')
        notes = []
        if v["verdict"] == "Blocked":
            notes.append(f'After earnings {fmt_d(ei["nxt"], False)} (est.); buy from {fmt_d(first_buy(t, ei), False)}')
        if v["hv_has_earn"]:
            notes.append("HV has earnings move")
        if v["wide"]:
            notes.append("Wide quotes")
        data.append([Paragraph(f"<b>{t}</b>", S_T8), Paragraph(vlabel(t), S_T8),
                     Paragraph(f'{v["iv"]:.0f}%' if v["iv"] else (f'{xv["iv"]:.0f}%*' if xv else "–"), S_T8R), Paragraph(f'{v["hv"]:.0f}%', S_T8R),
                     Paragraph(f'{v["ratio"]:.2f}' if v["ratio"] else (f'{xv["ratio"]:.2f}*' if xv else "–"), S_T8R),
                     Paragraph(f'{fmt_d(dt.date.fromisoformat(v["exp"]), False)} ({v["dte"]}d)' if v["exp"] else "–", S_T8),
                     Paragraph(em, S_T8), Paragraph("; ".join(notes), st("t8m", fontSize=7.4, leading=9.5, textColor=WARN))])
it = Table(data, colWidths=[0.62 * inch, 0.75 * inch, 0.52 * inch, 0.65 * inch, 0.55 * inch, 0.95 * inch, 1.45 * inch, CW - 5.49 * inch], repeatRows=1)
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
        f += [head, Spacer(1, 4), Paragraph(X(info["what"]), st("w", textColor=MUT, fontName="DVI", fontSize=9)), Spacer(1, 6)]
        hi_d = s["hiDate"].replace(", 2026", "").replace(", 2025", " 2025")
        vals = [(f"CLOSE {LAST:%b} {LAST.day}".upper(), f'<font name="DVB" size="13">${s["last"]:,.2f}</font>'),
                ("DAY", pc(s["day"], size=12)), ("1 WEEK", pc(s["wk"], size=12)),
                ("1 MONTH", pc(s["m1"], size=12)), ("3 MONTHS", pc(s["m3"], size=12)),
                (f"FROM HIGH (${s['hi']:,.2f}, {hi_d})", pc(s["offhi"], size=12))]
        sw = [1.15, 0.92, 0.88, 0.92, 0.95]
        sw = [x * inch for x in sw] + [CW - sum(sw) * inch]
        stt = Table([[Paragraph(a, S_LAB) for a, _ in vals], [Paragraph(b, st("v", leading=16)) for _, b in vals]], colWidths=sw)
        stt.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), CHIP), ("LEFTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, 0), 5),
                                 ("BOTTOMPADDING", (0, -1), (-1, -1), 5), ("TOPPADDING", (0, 1), (-1, 1), 0), ("LINEAFTER", (0, 0), (-2, -1), 0.6, colors.white)]))
        f += [stt, Spacer(1, 4), Image(chart(t), width=CW, height=CW * 1.9 / 7.3),
              Paragraph(f"3 months of daily closes ({fmt_d(s['m3_from'], False)} to {fmt_d(LAST, False)}); shaded = last month. Intraday ranges: 1 month ${s['lo1']:,.2f}–${s['hi1']:,.2f}; 3 months ${s['lo3']:,.2f}–${s['hi3']:,.2f}.", S_M),
              Spacer(1, 6)]
        if ei["nxt"]:
            days = (ei["nxt"] - TODAY).days
            red = days <= 21
            e1 = f'<font color="{"#b42318" if red else "#1c1d21"}"><b>{fmt_d(ei["nxt"])}</b></font>{" (est.)" if ei["est"] else ""} · {X(ei["when"])} · in {days} days'
        else:
            e1 = f"<b>Not set</b> · last reported {fmt_d(ei['last'])}"
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
        sec = [("LATEST RESULTS", X(info["results"])), ("GUIDANCE", X(info["guide"])), ("CAPEX & INVESTMENT", X(info["capex"])),
               ("CURRENT PARTNERSHIPS", bl(info["partners"])), ("CATALYSTS", bl(info["catalysts"])),
               ("MARKET EVENTS", X(info["macro"])), ("RISKS", X(info["risks"])),
               ("WALL STREET TARGETS", pt_cons(t, s["last"]) + ("<br/>" + " · ".join(pt_named(t)) if TG.T.get(t) else "<br/><font color=\"#62656e\">No named firm target reported recently in your outlets.</font>"))]
        dt_ = Table([[Paragraph(a, S_LAB), Paragraph(b, S_B)] for a, b in sec], colWidths=[1.35 * inch, CW - 1.35 * inch])
        dt_.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEABOVE", (0, 1), (-1, -1), 0.5, LINE), ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                 ("TOPPADDING", (0, 0), (-1, -1), 3.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2)]))
        src = " · ".join(f'<a href="{X(u)}" color="#1f5fbf">{X(l)}</a>' for l, u in info["src"])
        f += [dt_, Spacer(1, 5), Paragraph("<b>SOURCES</b>  " + src, st("src", fontSize=7.4, leading=10, textColor=MUT))]
        # one page per stock, always: shrink the page slightly if the content runs long
        story += [f[0], KeepInFrame(CW, FRAME_H - 2, f[1:], mode="shrink")]

doc.build(story)
print("wrote", OUT)
