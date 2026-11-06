# Per-stock research content for the report, in Ricky's list order.
# Every fact comes from the notes gathered Oct 25–30, 2026 (his outlets: CNBC, Bloomberg, Seeking Alpha, plus company SEC filings where coverage cited them).
SA = "https://seekingalpha.com/news/"
LISTS = [
 ("top5", "Top 5", ["SKHY", "AMZN", "AVGO", "SPCX", "INTC"]),
 ("portfolio", "2026 Portfolio", ["ANET", "WDC", "HPE", "TER", "AMAT", "LRCX", "CIEN", "MRVL", "COHR", "CRDO", "QCOM", "VICR", "ARM", "NVDA", "CSCO", "ALAB"]),
 ("dips", "15–50% Dip", ["DDOG", "VRT", "HOOD", "IONQ", "KLAC", "ORCL", "GLW", "NBIS", "BE", "DOCN", "AKAM", "FTNT", "NOW", "CRWV", "VST", "COIN", "CRCL", "BABA", "CBRS"]),
]

S = {}

S["AVGO"] = dict(
 name="Broadcom", what="Custom AI chips (ASICs) for Google, OpenAI and Anthropic, plus AI networking and VMware software.",
 results="Fiscal Q3 (reported Sep 2): revenue $29.6B, up 86%; adjusted EPS $3.32 vs $3.24 expected; AI chip revenue $16.7B, up 221%.",
 guide="Fiscal Q4 revenue $34.8B (+93%), slightly under the $35.03B consensus; AI chip revenue $21.7B. Fiscal 2026 AI revenue raised to $58B (from $56B). Outlines $115B of AI chip revenue in fiscal 2027 and $230B in 2028.",
 capex="Its own capex is small. Its growth depends on customers' AI budgets, and it is now helping fund one: talks on a $50B+ financing deal for OpenAI's custom chips.",
 partners=["OpenAI and Anthropic custom chips (concentration flagged by analysts)", "Google TPU designs", "NTT DOCOMO 10-year VMware cloud deal (Oct 20)"],
 catalysts=["Earnings Thu Dec 10", "Hyperscaler capex held or trimmed (Amazon $220B, Alphabet $195–205B, Microsoft $170B), but Alphabet's and Amazon's cash burn sparked an AI-spending selloff Oct 29–30", "Progress on the OpenAI financing deal", "Nvidia earnings Nov 17 and GTC DC (Nov 30–Dec 3)"],
 macro="CEO Hock Tan says capital, not demand, is now the biggest limit on AI. Higher rates and AI-credit stress hit names tied to OpenAI and Anthropic financing. It names wafers, substrates, HBM memory and power as supply bottlenecks.",
 risks="Customer concentration in OpenAI and Anthropic; off-balance-sheet financing exposure; Q4 guide only in line.",
 src=[("CNBC · Broadcom Q3 report", "https://www.cnbc.com/2026/09/02/broadcom-avgo-q3-earnings-report-2026.html"), ("Seeking Alpha · $58B FY26 AI, $115B/$230B outlook", SA+"4639799"), ("Seeking Alpha · $50B+ OpenAI chip financing talks", SA+"4651203"), ("Seeking Alpha · CEO: capital is the biggest constraint", SA+"4652302"), ("Seeking Alpha · NTT DOCOMO VMware deal", SA+"4654578")])

S["AMZN"] = dict(
 name="Amazon", what="AWS cloud (the profit engine), e-commerce, ads; Anthropic's main cloud partner.",
 results="Q3 (Oct 29): sales $201.9B, up 12%, just under the $202.3B consensus; EPS $1.89 vs $1.96 expected. Record 13.9% operating margin ($28.1B). AWS revenue $46.0B, up 39% (faster than Q2's 37%); AWS operating income $17.8B, up 55%.",
 guide="2026 capex held at about $220B. Jassy says AWS can grow above 40% in both 2027 and 2028. Morgan Stanley's Nowak called it mostly an expectations miss (CNBC).",
 capex="Q3 capex $77.3B vs $58.7B expected (FactSet) and $35.1B a year ago; trailing 12-month free cash flow −$42.4B. That cash burn drove the selloff and the AI-spending worries.",
 partners=["Anthropic (AWS)", "3M expanded data-center products relationship (Oct 19)"],
 catalysts=["Reported Oct 29; next report late January (date not set)", "Analysts say buy the dip after the miss (CNBC, Oct 30)", "AWS re:Invent Nov 30–Dec 4", "Holiday season"],
 macro="The week's AI-spending scare: Alphabet's record one-day drop and Amazon's cash burn pushed investors toward companies that show returns on AI spending. Its capex is revenue for NVDA, AVGO, MRVL, CRDO, VRT and the optics names.",
 risks="Capex outrunning cash flow; retail growth only 12%; AI agents shopping on rival platforms.",
 src=[("CNBC · Q3: negative FCF of $42.4B, capex held", "https://www.cnbc.com/2026/10/29/amazon-amzn-q3-earnings-report-2026.html"), ("CNBC · AWS up 39%", "https://www.cnbc.com/2026/10/29/aws-q3-earnings-report-2026.html"), ("Seeking Alpha · slides on sales and capex guide", SA+"4660612"), ("CNBC · analysts say buy the dip", "https://www.cnbc.com/2026/10/30/amazon-earnings-analysts-stock.html")])

S["BE"] = dict(
 name="Bloom Energy", what="Solid-oxide fuel cells for on-site power at AI data centers.",
 results="Q3 (Oct 22): revenue $1.24B, $170M above estimates; non-GAAP EPS $0.94, $0.27 above. Stock still fell 11% on cash outflows and expansion costs.",
 guide="2026 revenue $4.4–4.6B; non-GAAP EPS outlook raised to $3.10–3.40.",
 capex="Factory capacity expansion (announced Sep 29). Spending on that expansion is why cash flow disappointed in Q3.",
 partners=["Oracle data-center power (a reported force-majeure notice on one Oracle site hit the stock Sep 24)", "Joined the S&P 500 in September"],
 catalysts=["The next earnings date isn't set (it just reported)", "New hyperscaler power contracts", "Trump's call (Oct 21) for data centers to supply their own electricity: a tailwind for on-site power"],
 macro="AI-power demand, utility grid limits and natural-gas prices (fuel). Rate-sensitive: the Fed held Oct 28 but December hike odds are ~83% (CNBC).",
 risks="Cash burn during expansion; execution on Oracle projects; valuation (the stock is 44% off its high after the report).",
 src=[("Seeking Alpha · 2026 guide $4.4–4.6B, EPS raised", SA+"4656392"), ("Seeking Alpha · slides on cash outflows", SA+"4656548"), ("Seeking Alpha · Oracle force-majeure report", SA+"4646631"), ("Seeking Alpha · joins S&P 500", SA+"4640512")])

S["CRDO"] = dict(
 name="Credo Technology", what="Active electrical cables, SerDes chips and optical DSPs that connect AI servers and switches.",
 results="Fiscal Q1 FY27 (Sep 1): revenue $479.0M, up 115%, above its own $465–475M guide; non-GAAP net income $236.3M. Shares fell on margin pressure.",
 guide="Fiscal Q2 revenue $525–535M, gross margin 67–69%. Targets more than $600M of optical revenue in fiscal 2027 and about 80%+ growth for the year.",
 capex="Light (it's a fabless chip company). Its demand follows hyperscaler AI-cluster builds.",
 partners=["Hyperscaler customers; the largest is 33% of revenue", "Moving from copper into optical connectivity"],
 catalysts=["Earnings Mon Dec 7 (estimated)", "Peer reads: Fabrinet Nov 2, Arista and Astera Labs Nov 3, Lumentum Nov 5, Marvell Dec 1", "Seeking Alpha upgrade 'The Reset Is Done' (Oct 23)"],
 macro="Trades with the optics/connectivity group and hyperscaler capex headlines. Tariffs and supply limits in optics were flagged by management.",
 risks="Customer concentration; gross-margin pressure; high volatility (fell 9.5% on Friday Oct 23; 51% off its high).",
 src=[("Seeking Alpha · Q2 guide, $600M+ optical target", SA+"4639254"), ("Seeking Alpha · shares fall on margin pressure", SA+"4639142"), ("Seeking Alpha · 80%+ FY27 growth signal", SA+"4599516")])

S["SPCX"] = dict(
 name="SpaceX", what="Starlink, launch, and a fast-growing AI business ('Super Intelligence', formerly xAI).",
 results="Q3 (Oct 20): revenue about $14.6B, up 161% vs $12.7B expected; operating income $2.8B; net income $4.4B. Super Intelligence revenue $7.56B (9x a year ago).",
 guide="Q1 2027 revenue $33–37B vs $22.2B consensus (LSEG).",
 capex="Q3 capex $19.6B, more than its revenue. It fell 9% on Oct 22 on capex worries. A ~$40B debt sale is nearing completion at higher borrowing costs.",
 partners=["AI partner network incl. Nvidia, Databricks, Bain (Oct 22)", "Proposed Tesla merger (needs Musk's approval; aimed to close before the end of Trump's term, per Bloomberg)", "Plans for 80K cell sites for a wireless network (report, Oct 23)"],
 catalysts=["The next earnings date isn't set (it just reported)", "Tesla merger terms", "Debt-sale pricing", "Starlink–Ukraine dispute headlines", "Phillip double upgrade, $250 target (Oct 23)"],
 macro="Rates and credit spreads (heavy borrowing); AI-capex sentiment; politics (Pentagon/Ukraine, White House).",
 risks="Capex burn; merger governance; key-person risk (Musk).",
 src=[("CNBC · Q3 beat, analysts", "https://www.cnbc.com/2026/10/21/spacex-stock-q3-earnings-analysts.html"), ("Seeking Alpha · falls 9% on capex", SA+"4656304"), ("Seeking Alpha · $40B debt sale", SA+"4656340"), ("Seeking Alpha · AI partner network", SA+"4655984"), ("Seeking Alpha · Tesla merger needs Musk approval", SA+"4656357"), ("Seeking Alpha · 80K cell sites", SA+"4656417")])

S["CIEN"] = dict(
 name="Ciena", what="Optical networking systems connecting AI data centers and telecom networks.",
 results="Fiscal Q3 (Sep 3): revenue $1.67B, $30M above estimates; non-GAAP EPS $2.11, $0.38 above. Raised full-year guidance; stock fell 10% that day on rotation.",
 guide="At least 30% revenue growth in fiscal 2027, a $10B+ backlog, 25–27% operating margin. Investor day (Sep 16): 30% revenue CAGR target through 2029.",
 capex="Its demand follows hyperscaler network spending; it also launched a $200M venture fund.",
 partners=["Hyperscaler and telecom customers"],
 catalysts=["Earnings Thu Dec 10", "Peer reads: Fabrinet Nov 2, Arista Nov 3, Lumentum Nov 5, Marvell Dec 1", "Optical-group momentum: Lumentum says AI parts are sold out into 2029"],
 macro="AI capex headlines move the optics group as a block (it rose 13.8% on Marvell's Oct 6 investor day).",
 risks="Already priced like a compounder (analysts); profit-taking swings of ±10%.",
 src=[("Seeking Alpha · ≥30% FY27 growth, $10B+ backlog", SA+"4640053"), ("Seeking Alpha · 30% CAGR through 2029", SA+"4643478")])

S["MRVL"] = dict(
 name="Marvell", what="Custom AI silicon and data-center connectivity (electro-optics, DSPs).",
 results="Its last quarterly report was in August. On Oct 6 investor day it raised targets instead (below).",
 guide="Fiscal 2028 revenue target raised to about $20B (from about $18B); fiscal 2031 target $70–90B. Expects custom chips to accelerate from the second half of fiscal 2027.",
 capex="Fabless. Its demand follows hyperscaler custom-chip programs.",
 partners=["Open Compute data-center security group with Microsoft and Oracle (Oct 13)", "Google TPU supply chain (TPU v9 slightly delayed, per GF)"],
 catalysts=["Bloomberg (Oct 28): in advanced talks to buy Lumentum in an all-stock deal (Lumentum ~$83–85B), possibly announced as soon as this week. MRVL fell 11%+ on the report", "Earnings Tue Dec 1 (estimated)", "AWS re:Invent Nov 30 (custom chips)"],
 macro="AI-capex sentiment; reads through to the whole optics group (AAOI, GLW, CIEN, COHR, CRDO, NOK). Lumentum says optical parts are sold out into early 2029.",
 risks="Dilution and integration risk from a Lumentum deal; program timing (TPU delays).",
 src=[("Bloomberg · nears deal for Lumentum", "https://www.bloomberg.com/news/articles/2026-10-28/marvell-is-said-to-near-deal-for-lumentum-in-ai-related-megadeal"), ("Seeking Alpha · jumps on raised guidance at investor day", SA+"4650555"), ("Seeking Alpha · investor day $20B outlook", "https://seekingalpha.com/article/4952697"), ("Seeking Alpha · OCP security group", SA+"4652456")])

S["SKHY"] = dict(
 name="SK hynix", what="Memory chips: HBM for AI accelerators, DRAM and NAND (Solidigm).",
 results="Q3 (Oct 28 Seoul, Tue evening US): record revenue ₩104.6T (+328% y/y, the first quarter above ₩100T); operating profit ₩83.3T (+632%, 80% margin), above the ~₩77T consensus; net profit ₩39.8T. Shares rose ~11% in Seoul and 13%+ in New York on Wed Oct 28 (CNBC), then gave back gains in Friday's chip selloff.",
 guide="No formal guidance. HBM4 shipments began in earnest in Q3 and should pass HBM3E in shipments and revenue in Q4. Long-term deals with 14 customers cover over half of 2027–28 capacity; it sees demand above supply through 2030.",
 capex="M15X ramps to full capacity by year-end; investment rises 'significantly' next year as Yongin phase 1 starts full operation.",
 partners=["~₩100T of 2026 shareholder returns: ₩30T+ dividends, ₩60T+ buybacks", "Q3 dividend ₩20,000/share (half special, from Kioxia gains) + ₩20T buyback", "DRAM supply talks with Alibaba and Tencent (report, Oct 27)", "Solidigm: $45B U.S. plant talks (report)"],
 catalysts=["Reported Oct 27 (US time); next date not set", "Nvidia AI Day Seoul Nov 9–10; Nvidia earnings Nov 17", "Your planned Mon Nov 2 entry with AVGO"],
 macro="Memory pricing, Korean won and the Kospi; China capacity (CXMT) and US approvals for its China fabs.",
 risks="Memory-cycle fears; net profit fell 58% q/q on non-operating losses; 27% off its high.",
 src=[("SK hynix newsroom · Q3 results", "https://news.skhynix.com/en/q3-2026-business-results/"), ("Seeking Alpha · shares jump on profit beat, payout plan", SA+"4658610"), ("Seeking Alpha · Q3 headline numbers", SA+"4658571"), ("CNBC · shares jump 11% on record profit", "https://www.cnbc.com/2026/10/28/sk-hynix-third-quarter-profit.html")])

S["AMAT"] = dict(
 name="Applied Materials", what="The largest chip-equipment maker (deposition, etch, inspection).",
 results="Fiscal Q3 (Aug 13): record revenue $9.12B and record non-GAAP EPS $3.50; raised its Q4 outlook.",
 guide="CEO raised his 2026 chip-systems expectations and sees another strong growth year in 2027. Q4 consensus EPS $4.06 (Nasdaq). China sales are limited by US export rules.",
 capex="Its own investments: a $5B EPIC R&D center (Oct 12) and $5B in India over a decade. Its demand follows foundry and memory capex.",
 partners=["Deeper Intel collaboration (Oct 6)", "KIOXIA next-gen memory (Sep 29)", "Singapore ties with KLA and GlobalFoundries"],
 catalysts=["Earnings Thu Nov 12 after the close", "KLA beat and guided $4.5–4.9B (Oct 28); Intel guided below estimates (Oct 29)", "Lam's cautious Dec-quarter guide (Oct 21) is the overhang"],
 macro="Export controls and China; memory and foundry capex; Barron's says the group's trouble 'could be just getting started'.",
 risks="China revenue decline; supply-chain limits like those Lam flagged; 48% off its high.",
 src=[("Seeking Alpha · Q3 call transcript", "https://seekingalpha.com/article/4936471"), ("Seeking Alpha · $5B EPIC center", SA+"4652276"), ("Seeking Alpha · Intel collaboration", SA+"4650539"), ("Seeking Alpha · KIOXIA partnership", SA+"4648222")])

S["VRT"] = dict(
 name="Vertiv", what="Data-center power and liquid cooling.",
 results="Q3 (Oct 28): sales $4.31B, up 61%; adjusted EPS $2.21, up 78% ($0.39 above estimates); adjusted operating margin 25.2%; organic orders up more than 100%. Stock jumped 16% to $242.94 that day (Seeking Alpha).",
 guide="2026 raised to $14.65B sales and $7.15 adjusted EPS (from ~$14B / $6.70). Q4 sales ~$4.41B at the midpoint, 50% organic growth; signals above-market growth into 2027.",
 capex="Buying capacity through acquisitions: UtilityInnovation Group ($1.45B + earnouts) and King Environmental Services (liquid cooling). Last backlog figure found: $15.0B (Q4 2025).",
 partners=["Hyperscaler and colocation customers"],
 catalysts=["Reported Oct 28; next report February (date not set)", "Hyperscaler capex held: Amazon $220B, Alphabet $195–205B; Microsoft trimmed to $170B on chip delays", "Nvidia earnings Nov 17"],
 macro="AI-infrastructure trade; rising Treasury yields have hit this group before (Aug 18, Oct 15).",
 risks="Valuation; backlog conversion; hyperscaler spending discipline after the week's AI-spending scare.",
 src=[("Seeking Alpha · surges 16% on Q3, outlook raise", SA+"4659639"), ("Seeking Alpha · $14.65B / $7.15 2026 outlook", SA+"4659493"), ("CNBC · CEO on 17% drop", "https://www.cnbc.com/2026/07/29/vertiv-ceo-addresses-stock-plunge-disappointing-quarter.html"), ("Seeking Alpha · raised 2026 outlook", SA+"4621076"), ("Seeking Alpha · UtilityInnovation deal", SA+"4639364"), ("Seeking Alpha · King Environmental deal", SA+"4646516")])

S["COHR"] = dict(
 name="Coherent", what="Optical transceivers, lasers and materials for AI data centers.",
 results="Fiscal Q4 (Aug 12): revenue $2.05B (top of guidance); non-GAAP EPS $1.74 (above guidance); data-center and communications revenue for the year up 40% to $5.28B.",
 guide="Press reports point to quarterly revenue above $3B by the end of fiscal 2027; supply is ramping faster than expected. Q1 consensus EPS $1.78.",
 capex="Expanding production capacity (transceivers, 300mm silicon carbide).",
 partners=["PhotonLink integrated-optics platform for AI data centers (Sep 21)", "AI hyperscaler customers"],
 catalysts=["Earnings Wed Nov 4 after the close", "Lumentum Nov 5; Fabrinet Nov 2", "Optical shortage: Lumentum says AI parts are sold out into early 2029 (Oct 9)"],
 macro="Optics trades as a group on AI-capex news; it fell 12.5% on Oct 22 with Lumentum.",
 risks="Price swings; 51% off its high.",
 src=[("Seeking Alpha · Q4 revenue +34%", SA+"4631806"), ("Seeking Alpha · supply ramp, targets raised", SA+"4632305"), ("Seeking Alpha · Lumentum: sold out to 2029", SA+"4651678"), ("Seeking Alpha · PhotonLink", SA+"4645180")])

S["HOOD"] = dict(
 name="Robinhood", what="Retail brokerage: stocks, options, crypto, prediction markets.",
 results="Q3 (Oct 27): revenue $1.42B, $10M below estimates; non-GAAP EPS $0.60, $0.04 below, hit by venture-fund-related losses. The stock dipped after hours.",
 guide="2026 adjusted operating expenses $2.675–2.75B. Plans 24/7 stock trading later this year.",
 capex="Light. Bought its first $25M of bitcoin for its balance sheet (Oct 7).",
 partners=["Ripple infrastructure: stablecoins, institutional markets, treasury (Oct 27)", "Crypto.com and Susquehanna (prediction markets)", "Cboe KPI options approved by the SEC (Oct 14)", "Dubai expansion (Oct 23)"],
 catalysts=["Reported Oct 27; next date not set", "Circle reports Nov 4; Binance hack (Oct 29) hit crypto names", "24/7 equity trading launch"],
 macro="Bitcoin and trading volumes; rate path (interest income); crypto legislation (the Clarity Act stalled in the Senate).",
 risks="Earnings miss and higher spending; crypto weakness; regulatory pushback on tokenized stocks.",
 src=[("Seeking Alpha · Q3 miss", SA+"4658351"), ("Seeking Alpha · VC losses hit EPS", SA+"4658309"), ("Seeking Alpha · OpEx guide, 24/7 trading", SA+"4658555"), ("Seeking Alpha · Ripple deal", SA+"4657939")])

S["ARM"] = dict(
 name="Arm Holdings", what="Licenses chip designs (CPU IP) and is building its own data-center CPU.",
 results="Fiscal Q1 FY27 (late Jul): revenue about $1.29B, up 22%, above its $1.26B guide; EPS $0.45, $0.05 above. Data-center royalties more than doubled (analyst read).",
 guide="Q2 consensus EPS $0.22 (Nasdaq). An analyst read of management's long-term target: $25B revenue and $9+ EPS by 2031.",
 capex="Light (IP licensing).",
 partners=["Every major hyperscaler is ramping Arm server chips", "IBM dual-architecture mainframe", "Early talks on a possible Eliyan takeover (report)"],
 catalysts=["Earnings Wed Nov 4 after the close", "Apple Nov 2, AMD Nov 3", "Fallout from the Qualcomm lawsuit (jury found Arm breached the license agreement, Oct 13)"],
 macro="Semiconductor sentiment; AI-trade swings (it fell 9% and rose 17% within September).",
 risks="Legal loss to Qualcomm; investor pushback on the CEO's pay package; 52% off its high.",
 src=[("Seeking Alpha · Q1 FY27 presentation", "https://seekingalpha.com/article/4928459"), ("Seeking Alpha · Qualcomm–Arm verdict", SA+"4652607")])

S["GLW"] = dict(
 name="Corning", what="Optical fiber and cable for AI data centers, plus glass and solar materials.",
 results="Q3 (Oct 27): core sales $5.08B (+19%), $50M above estimates; core EPS $0.91, $0.03 above. Optical Communications $2.38B (+44%); Solar +37%, ramping slower than planned. The stock still closed −1.1%.",
 guide="Q4 core sales $5.2–5.3B and core EPS $0.96–1.00 (about +36%), above estimates. The 'Springboard' run rate has passed $20B; targets $30B by 2028 and $40B by 2030.",
 capex="Raised money through a $2B equity distribution agreement (stock fell 14%, Sep 14) to fund growth.",
 partners=["Verizon multi-billion fiber deal (Sep 8)", "AT&T multi-year fiber deal (Sep 29)", "Lumentum + Qualcomm AI optical tech (Sep 21)", "Meta fiber deal (Jan)"],
 catalysts=["Reported Oct 27; next date not set", "Hyperscaler capex held: Amazon $220B, Alphabet $195–205B; Microsoft $170B", "Apple earnings Nov 2"],
 macro="AI optics demand; telecom fiber builds; solar trade policy (polysilicon tariffs).",
 risks="Share dilution from the equity program; slower solar ramp; 51% off its high.",
 src=[("Seeking Alpha · Q3 beat", SA+"4657766"), ("Seeking Alpha · Q4 guide, Springboard past $20B", SA+"4658093"), ("Corning 8-K · Q3 release", "https://www.sec.gov/Archives/edgar/data/0000024741/000002474126000273/glw-20261027xex99xq32026.htm"), ("Seeking Alpha · AT&T deal", SA+"4648005")])

S["INTC"] = dict(
 name="Intel", what="CPUs (PC and data center) and a contract foundry (18A / 14A).",
 results="Q3 (Oct 29): revenue $16.51B, up 21%, in line with $16.50B expected; adjusted EPS $0.52 vs $0.40. Data-center and AI segment had its fastest growth in 15 years. The stock fell 28.6% Friday, its worst day since 1974 (CNBC).",
 guide="Q4 revenue $15–16B and adjusted EPS $0.25, below estimates. CFO Zinsner: 'We see the PC slowdown continuing at least through the first half of next year' (memory costs). 18A ramp continues; 14A customer decisions expected into 1H 2027.",
 capex="Arizona fab tools being installed (Wedbush says this supports revenue growth).",
 partners=["Applied Materials collaboration", "Musk's Terafab project", "Agentic AI is lifting CPU demand (Mizuho)"],
 catalysts=["Reported Oct 29; next report late January", "News of foundry customer wins", "Analyst target changes after the guide miss"],
 macro="Memory shortage limits PC builds; the US government's stake lost ~$12B in value Friday (CNBC).",
 risks="PC slowdown into 1H 2027; foundry customer timing; 55% off its high after Friday.",
 src=[("CNBC · plunges on PC-slowdown guide", "https://www.cnbc.com/2026/10/29/intel-intc-q3-earnings-report-2026-.html"), ("Seeking Alpha · Q3 results, guide miss", SA+"4660336"), ("CNBC · Q2 report", "https://www.cnbc.com/2026/07/23/intel-intc-earnings-report-q2-2026.html"), ("Seeking Alpha · Wedbush on Arizona fab", SA+"4656527"), ("Seeking Alpha · JPM upgrade", SA+"4654160")])

S["KLAC"] = dict(
 name="KLA", what="Chip process control and inspection equipment.",
 results="September quarter (Oct 28): revenue $4.14B, above the $4.0B guide midpoint ($98M above estimates); non-GAAP EPS $1.22, $0.04 above estimates (Seeking Alpha).",
 guide="December quarter revenue $4.5–4.9B and EPS $1.33–1.55 (Seeking Alpha). Raised its 2026 wafer-equipment view to the mid-$150B range and sees 2027 above $200B.",
 capex="Its demand follows foundry, memory and advanced-packaging spending. Margin pressure from memory prices, tariffs and supply lead times.",
 partners=["Singapore semiconductor ties with Applied Materials and GlobalFoundries"],
 catalysts=["Reported Oct 28; next report late January", "Applied Materials Nov 12 (group read-through)", "2027 WFE above $200B is the bull case"],
 macro="Export controls; China; wafer-equipment cycle; Friday's chip selloff.",
 risks="Chip-equipment selloffs when AI spending is questioned; 48% off its high.",
 src=[("Seeking Alpha · pops on Q1 results, guidance", SA+"4659498"), ("Seeking Alpha · what Wall Street's saying", SA+"4660227"), ("Seeking Alpha · ~$4B Sept-qtr, WFE low-$150B", SA+"4619965"), ("Seeking Alpha · falls 10%", SA+"4656277")])

S["NVDA"] = dict(
 name="Nvidia", what="AI accelerators (Blackwell, Vera Rubin), networking, software.",
 results="Fiscal Q2 FY27 (Aug 26): revenue $96.22B vs ~$92B expected; adjusted EPS $2.22; data center about $89B, up 117%; gross margin ~75%.",
 guide="Fiscal 2028 revenue growth about 70% (vs ~44–45% expected). Gross margin expected to bottom around 71–72% in fiscal Q4 because of memory costs. China data-center sales are excluded from the outlook. A secondary source puts fiscal Q3 at about $108B.",
 capex="Investing in partners: a ~$10B European push and backing German AI startups. TD Cowen says it may be backstopping Oracle data centers.",
 partners=["GTC Berlin deals: Amkor ($1.3B), Dell AI Factory, CrowdStrike, E.ON nuclear-site study", "~$35B of orders for a new export-compliant GPU from Chinese tech giants (report, Oct 20)", "Samsung using TSMC tech for its next memory chips"],
 catalysts=["Earnings Tue Nov 17 after the close (confirmed by Nvidia)", "Hyperscaler capex held (Amazon $220B, Alphabet $195–205B, Microsoft $170B on chip-supply delays)", "Nvidia AI Day Seoul Nov 9–10; GTC DC Nov 30–Dec 3 (Huang keynote Dec 1)"],
 macro="Huang says scarce capital is holding back the neoclouds (CoreWeave and Nebius are customers). China export policy; memory costs.",
 risks="Seaport repeated its Sell rating on mounting competition; customers' financing.",
 src=[("CNBC · Q2 FY27 takeaways", "https://www.cnbc.com/2026/08/26/nvidia-nvda-earnings-report-q2-2027-live-updates.html"), ("Seeking Alpha · $35B China orders (report)", SA+"4654626"), ("Seeking Alpha · Oracle backstop (TD Cowen)", SA+"4654748"), ("Seeking Alpha · Berlin deals", SA+"4655130"), ("Seeking Alpha · Huang on neocloud capital", SA+"4655787")])

S["QCOM"] = dict(
 name="Qualcomm", what="Smartphone chips and licensing, expanding into autos, IoT and data-center AI.",
 results="Fiscal Q3 (Jul 29): revenue $9.9B (down 4%); non-GAAP EPS $2.21. Handsets down 20% (management called this the bottom); autos up 61%; IoT up 9%.",
 guide="Fiscal Q4 revenue $9.7–10.5B and EPS $2.05–2.25, below the $10.02B / $2.36 consensus because of the memory supply crunch. Chip price increases from Sep 1. Expects non-handset revenue above 60% in fiscal 2027.",
 capex="Light. Data-center custom silicon ships to a major hyperscaler starting in December.",
 partners=["Apple patent license renewed (Sep 24)", "Huawei patent license (Oct 5)", "Won its lawsuit against Arm (Oct 13)", "Buying PickNik (robotics)", "Lumentum + Corning AI optics"],
 catalysts=["Earnings Wed Nov 4 after the close", "Apple Nov 2", "Possible November layoffs (report)", "Ambarella takeover interest (report)"],
 macro="The memory shortage hits phone builds; smartphone demand; China.",
 risks="Handset weakness; data-center ramp timing. Q4 consensus EPS $1.46 (Nasdaq).",
 src=[("CNBC · Q3 report", "https://www.cnbc.com/2026/07/29/qualcomm-qcom-earnings-report-q3-2026-.html"), ("Seeking Alpha · handset bottom", "https://seekingalpha.com/news/4620785"), ("Seeking Alpha · Huawei license", SA+"4650073"), ("Seeking Alpha · layoffs report", SA+"4654534")])

S["IONQ"] = dict(
 name="IonQ", what="Trapped-ion quantum computers; now owns the SkyWater foundry.",
 results="Q2 (Aug 5): record revenue $80.1M (secondary source).",
 guide="2026 revenue raised to $280–290M (standalone, before SkyWater).",
 capex="Funded by equity: seeking about $2B in net proceeds from a stock and warrant offering (Oct 14).",
 partners=["Acquired SkyWater (~$1.8B, closed Jul 31)", "DARPA picked IBM and IonQ for the next phase of fault-tolerant quantum work (Oct 8)", "Nvidia (error-correction milestone, Sep 23)", "Buying Elisity (cybersecurity) for $1.3B in stock (Oct 12; the stock fell)", "SDT (South Korea), FIU Superion system"],
 catalysts=["Earnings Wed Nov 4 (estimated)", "Quantum-sector headlines", "Integration of SkyWater and Elisity"],
 macro="High-beta and rate-sensitive; risk appetite for speculative tech.",
 risks="Dilution from offerings and stock deals; losses (consensus EPS −$0.79); 57% off its high.",
 src=[("Seeking Alpha · $280–290M 2026 outlook", SA+"4627131"), ("Seeking Alpha · DARPA selection", SA+"4651377"), ("Seeking Alpha · Elisity deal", SA+"4652040"), ("Seeking Alpha · ~$2B offering", SA+"4652885")])

S["CBRS"] = dict(
 name="Cerebras", what="Wafer-scale AI chips and an inference cloud.",
 results="Q2 (Aug 12): GAAP revenue ~$180M (vs $194M expected); 'core' revenue $210M; net loss $450.5M. Stock fell 14% despite raising guidance.",
 guide="Q3 core revenue $214–216M; 2026 core revenue $880–890M (raised from $855–865M); plans to more than triple revenue in 2027. Order backlog (RPO) $25.4B.",
 capex="600 MW of data-center capacity under contract; Compute Nordic 165 MW site in Finland.",
 partners=["OpenAI: 750 MW of inference capacity through 2028, an option for 1.25 GW more, deal worth over $10B; Altman calls it a 'close partner'", "Compute Nordic, Callosum"],
 catalysts=["Earnings Thu Nov 12 (estimated)", "New OpenAI capacity tranches", "Nvidia Nov 17"],
 macro="AI-inference demand; OpenAI's funding health.",
 risks="Heavy reliance on OpenAI; losses; 64% off its high.",
 src=[("CNBC · Q2 report", "https://www.cnbc.com/2026/08/12/cerebras-cbrs-q2-earnings-report-2026.html"), ("Seeking Alpha · $880–890M core outlook", SA+"4632042"), ("Seeking Alpha · Altman 'close partner'", SA+"4650091")])

S["CRWV"] = dict(
 name="CoreWeave", what="AI 'neocloud' renting Nvidia GPU capacity.",
 results="Q2 (Aug 11): revenue $2.58B, up 112%; adjusted loss $1.03 per share (vs −$1.20 expected). Backlog $104B (about $129B including $25B signed early in Q3); 1.5 GW active power.",
 guide="Q3 revenue $3.4–3.6B; 2026 revenue $12.4–13.2B; adjusted operating income $960M–1.15B; more than 1.85 GW active by year-end. Q3 consensus EPS −$1.45.",
 capex="2026 capex $35–39B (raised from $31–35B). Debt about $35.6B; Q2 net interest $640M.",
 partners=["Anthropic and Meta contracts", "Nvidia (supplier)", "New robotics/EV workloads and a zero-trust AI framework (Oct 21)"],
 catalysts=["⚠ Earnings Tue Nov 10 after the close (confirmed)", "Financing news: credit spreads hit a record Oct 15", "Analyst split: Goldman upgrade and UBS Buy vs Bernstein 'not bottom yet'"],
 macro="The center of the AI-credit stress. Gartner predicts 80% of neoclouds will be gone by 2030; short sellers have $6B in paper profits. Rates and credit spreads drive it.",
 risks="Debt load and refinancing; customer concentration; new 52-week low on Oct 22 (61% off its high).",
 src=[("CNBC · Q2 report", "https://www.cnbc.com/2026/08/11/coreweave-crwv-q2-earnings-report-2026.html"), ("Seeking Alpha · Gartner neocloud warning", SA+"4653029"), ("Seeking Alpha · new 52-week low", SA+"4656253"), ("Seeking Alpha · Piper: financing fears overblown", SA+"4655159"), ("Seeking Alpha · shorts' $6B profits", SA+"4656446")])

S["VICR"] = dict(
 name="Vicor", what="Power modules that feed AI processors (Vertical Power Delivery), plus royalties from licensing that technology.",
 results="Q3 (Oct 20): revenue $197.1M (+78.5% y/y); gross margin 68.3%; net income $63.3M; EPS $1.33 ($0.04 below estimates).",
 guide="Q4: product revenue up about 10% and at least $43M of royalties. 2026 revenue above $600M; long-term target $2.5B at a 70% gross margin.",
 capex="Fab-2 equipment deployment targeted for Q2 2027.",
 partners=["New licensing agreement (it raised its Q3 outlook on the royalties, Sep 21–30)", "Royalties about 34% of revenue (analyst)"],
 catalysts=["The next earnings date isn't set (it just reported)", "New license signings", "ITC litigation outcomes"],
 macro="AI-power trade; small-cap volatility.",
 risks="Timing of license deals; litigation; 54% off its high.",
 src=[("Seeking Alpha · Q4 outlook, Fab-2", SA+"4654741"), ("Seeking Alpha · revenue surges, EPS miss", "https://seekingalpha.com/news/4654595")])

S["LRCX"] = dict(
 name="Lam Research", what="Etch and deposition equipment, heavily tied to memory capex.",
 results="September quarter (Oct 21): revenue $8.22B, $80M above; non-GAAP EPS $2.20, $0.02 above; record margins (operating margin above 40%).",
 guide="December-quarter guide trimmed on supply-chain issues; China revenue falling. Sees 2027 wafer-equipment spending above $200B; Aether revenue target raised to $2.5B by 2030. Stock fell 12% on Oct 22.",
 capex="$3B R&D lab network over 5 years; dividend raised 26.9%.",
 partners=["Memory makers (SK hynix, Samsung, Micron) are its key customers"],
 catalysts=["The next earnings date isn't set (late January)", "SK hynix record Q3 and plans to raise investment significantly in 2027; KLA sees 2027 WFE above $200B"],
 macro="Export controls / China; memory capex; Barron's sees more downside for the group.",
 risks="China decline; supply constraints; 47% off its high.",
 src=[("Seeking Alpha · retreats 12% on cautious guide", SA+"4656207"), ("Seeking Alpha · >$200B 2027 WFE", SA+"4655710")])

S["TER"] = dict(
 name="Teradyne", what="Chip test equipment (AI accelerators, HBM/memory, networking) plus robotics.",
 results="Q3 (Oct 27): revenue $1.306B (+70% y/y), $40M above estimates; non-GAAP EPS $2.29, $0.23 above. Semiconductor Test $1.072B, Product Test $138M, Robotics $96M.",
 guide="Q4 revenue $1.25–1.35B; non-GAAP EPS $1.95–2.25 (GAAP $1.88–2.18). CEO: demand 'extended across the AI value chain, from memory and hard disk drive test to high-speed interconnect and robotics.'",
 capex="Its demand follows AI-chip and HBM test needs.",
 partners=["FormFactor collaboration (Oct 12)", "HBM/memory test demand (SK hynix record quarter the same night)"],
 catalysts=["Reported Oct 27; next date not set", "KLA beat (Oct 28); Applied Materials Nov 12 (equipment read)", "Nvidia earnings Nov 17"],
 macro="Chip-equipment sentiment; memory test demand.",
 risks="Q4 guide midpoint roughly flat with Q3; revenue swings from concentrated AI orders; 33% off its high.",
 src=[("Seeking Alpha · Q3 beat", SA+"4658431"), ("Teradyne · Q3 release", "https://investors.teradyne.com/news-events/press-releases/detail/455/teradyne-reports-third-quarter-2026-results"), ("Seeking Alpha · FormFactor collaboration", SA+"4652273")])

S["NBIS"] = dict(
 name="Nebius", what="AI neocloud (GPU cloud), CoreWeave's closest peer.",
 results="Q2 (Aug 12): revenue $582.3M (+454%); AI cloud $574.9M (+514%); annual run-rate $3.0B at end of June. Shares rose 28–34%.",
 guide="Reaffirmed 2026 revenue of $3.0–3.4B and annual run-rate (ARR) guidance of $7–9B; capacity target raised to 5 GW. Q3 consensus EPS −$0.43.",
 capex="2026 capex $20–25B; customer prepayments cover 50–70% of project capex. New $3.5B Citi financing facility (Oct 22).",
 partners=["Meta: $12B over 5 years on Vera Rubin from early 2027, plus up to $15B more", "Microsoft (capacity tranches delivered)", ">$40B of additional contracted revenue", "Bought Inferize (inference)"],
 catalysts=["Earnings Tue Nov 10 (estimated)", "CoreWeave Nov 10", "Live spot GPU pricing launched (Oct 21)"],
 macro="Neocloud credit sentiment (Gartner, short sellers); rates.",
 risks="Funding gap and reliance on outside capital; it fell 12% on Oct 16.",
 src=[("Seeking Alpha · surges after Q2", SA+"4631437"), ("Seeking Alpha · $3.5B Citi facility", SA+"4655808"), ("Seeking Alpha · Gartner ratings", SA+"4653414")])

S["VST"] = dict(
 name="Vistra", what="Power producer (nuclear and gas) selling power to data centers.",
 results="Q2 (Aug 7): reaffirmed its 2026 adjusted EBITDA target of $6.8–7.6B; committed up to $1B to the Helix partnership.",
 guide="2026 adjusted EBITDA $6.8–7.6B. Q3 consensus EPS $2.87.",
 capex="DOE confirmed a loan of up to $4.2B to raise nuclear output (Oct 5); $1.5B of junior subordinated notes (Sep).",
 partners=["AWS: 20-year deal for 1,200 MW from the Comanche Peak nuclear plant (deliveries from Q4 2027)", "Meta: 20-year deals for 2,609 MW from its PJM nuclear plants", "New Era Energy: 207 MW gas deal, 20 years"],
 catalysts=["Earnings Fri Nov 6 before the open", "Microsoft/Alphabet/Amazon power demand comments", "FERC rejected most of PJM's data-center curtailment plan (Oct 12)"],
 macro="Power prices, gas prices, grid rules for data centers; rate-sensitive (pays a dividend).",
 risks="Regulatory changes on data-center grid access.",
 src=[("Seeking Alpha · 2026 EBITDA target", "https://seekingalpha.com/news/4517590"), ("Seeking Alpha · $4.2B DOE loan", SA+"4650394"), ("Seeking Alpha · FERC/PJM", SA+"4652290")])

S["ORCL"] = dict(
 name="Oracle", what="Oracle Cloud Infrastructure (AI data centers for OpenAI and others) plus database software.",
 results="Fiscal Q1 FY27 (Sep 10): revenue $19.35B (vs $19.14B); cloud infrastructure $7.4B (+121%); contract backlog (RPO) $664B (+$209B), more than $30B of new AI contracts.",
 guide="Fiscal 2027 revenue of at least $90B and $8.10 adjusted EPS. Q2 consensus EPS $1.57.",
 capex="Q1 capex $28.5B (vs $8.5B a year ago); free cash flow −$5.4B. The CFO put fiscal 2027 net capex at about $70B, excluding $20–25B of customer prepayments.",
 partners=["OpenAI (BofA: more than half of the backlog)", "Nvidia may be backstopping its data centers (TD Cowen)", "AstraZeneca AI collaboration", "OCP security group with Marvell and Microsoft", "$1B partner-ecosystem commitment (Oct 23)", "Bloom Energy on-site power"],
 catalysts=["Earnings Wed Dec 9", "OpenAI funding news"],
 macro="Center of the AI-credit stress: Oracle and CoreWeave credit spreads hit records Oct 15. Rates; power availability (it uses trucked natural gas to keep sites on track).",
 risks="OpenAI concentration; negative free cash flow; 56% off its high.",
 src=[("CNBC · Q1 FY27", "https://www.cnbc.com/2026/09/10/oracle-orcl-q1-earnings-report-2027.html"), ("Seeking Alpha · record CDS spreads", SA+"4653250"), ("Seeking Alpha · $1B partner commitment", SA+"4656530"), ("Seeking Alpha · Nvidia backstop", SA+"4654748")])

S["AKAM"] = dict(
 name="Akamai", what="CDN/edge network, cloud security, and a fast-growing cloud-computing business.",
 results="Q2 (Aug 6): revenue $1.1B, $10M above; non-GAAP EPS $1.59, $0.01 above.",
 guide="Expects low-teens revenue growth in 2027, backed by $2.8B of cloud-infrastructure commitments. 2026 guide reaffirmed after the Anthropic deal. Q3 consensus EPS $0.92.",
 capex="Analysts estimate about $5.5B of capex to serve the Anthropic contract; the financial impact starts in 2027.",
 partners=["Anthropic: $11.6B over 7 years for CPU cloud capacity, up to $9B more; Anthropic got warrants for ~2% of shares now, up to ~5% (Sep 24)", "Lenovo and Jabil deals (Sep 25)"],
 catalysts=["Earnings Thu Nov 5 after the close", "Cloudflare and Fastly reports Nov 4–5", "Raymond James upgrade (Oct 20)"],
 macro="Cyber incidents; AI inference demand; rates (capex funding).",
 risks="Execution and capex on the Anthropic build; dilution from the warrants.",
 src=[("Bloomberg · $12B Anthropic deal", "https://www.bloomberg.com/news/articles/2026-09-24/anthropic-strikes-12-billion-deal-with-akamai-for-ai-computing"), ("CNBC · Wall Street on the deal", "https://www.cnbc.com/2026/09/25/shares-of-akamai-surge-after-deal-with-anthropic-what-wall-street-is-saying.html"), ("Seeking Alpha · 2027 low-teens growth", SA+"4628707"), ("Seeking Alpha · Raymond James upgrade", SA+"4654566")])

S["DOCN"] = dict(
 name="DigitalOcean", what="Developer and small-business cloud, adding AI inference.",
 results="Q2 (Aug 4): revenue $281M (+29%); contract backlog (RPO) $894M (12x); AI customer annual revenue $234M (+212%), 85% from inference and core cloud.",
 guide="2026 revenue growth about 30.5%, exiting Q4 at 35%+. Q3 consensus EPS $0.11.",
 capex="Committed data-center capacity about 155 MW (+20 MW coming late 2027/early 2028); $725M equipment-finance facility (Sep 10).",
 partners=["GPU and inference customers"],
 catalysts=["Earnings Tue Nov 3 before the open (election day)", "CoreWeave Nov 10 and Nebius Nov 10"],
 macro="Neocloud sentiment (Gartner); rates.",
 risks="Capital needs; competition; 49% off its high.",
 src=[("Seeking Alpha · 30.5% 2026 growth", SA+"4624898"), ("Seeking Alpha · $725M facility", SA+"4641854")])

S["BAC"] = dict(
 name="Bank of America", what="Large US bank; profits move with interest rates and the yield curve.",
 results="Q3 (Oct 14): net interest income $16.6B (+7.9%, a beat); EPS $0.91 ($1.08 excluding a fine) vs $1.10 expected; revenue $30.12B (miss); fixed-income trading down 17%; $1.2B Treasury anti-money-laundering fine. Shares fell 8%.",
 guide="Expects 2027 net interest income up 8% or more. 2026 NII guide was +5–7% (given in January).",
 capex="Not a driver.",
 partners=["$0.32 dividend declared (Oct 21)"],
 catalysts=["The next earnings date isn't set (mid-January)", "FOMC Oct 28: a hike would help NII", "Bank capital rules"],
 macro="Yields and curve shape; credit quality (September card delinquencies contained); regulation (OCC 'debanking' finding).",
 risks="Regulatory and compliance costs; trading weakness.",
 src=[("CNBC · Q3 report", "https://www.cnbc.com/2026/10/14/bank-of-america-bac-q3-2026-earnings.html"), ("Seeking Alpha · 2027 NII +8%", SA+"4653213"), ("Seeking Alpha · $1.2B fine", SA+"4652672")])

S["COIN"] = dict(
 name="Coinbase", what="Crypto exchange, custody and stablecoin (USDC) partner.",
 results="Q3 (Oct 29): revenue $1.20B vs $1.233B expected (LSEG); adjusted net income $719M, up 66%, on the crypto recovery and expense discipline (CNBC).",
 guide="No formal revenue guide in the coverage found. Friday: Binance's record $6.3B hack (Oct 29) pushed bitcoin under $77K; Binance paused withdrawals and says it will cover losses (Bloomberg).",
 capex="Light.",
 partners=["Citi institutional stablecoin payments (Sep 28)", "CFTC approval for derivatives clearing (Sep 29)", "Samsung Wallet USDC custody (Oct 8)", "Marqeta stablecoin cards (Oct 16)", "Open USD with Visa/Mastercard/Stripe"],
 catalysts=["Reported Oct 29; next report February", "Fallout from the Binance hack (customers moving to US exchanges vs. a broad crypto scare)", "Clarity Act stalled in the Senate"],
 macro="Bitcoin price (about $77K Friday), crypto trading volumes, rates (USDC interest income).",
 risks="Revenue miss; crypto-security scare after Binance; 60% off its high.",
 src=[("CNBC · Q3 report", "https://www.cnbc.com/2026/10/29/coinbase-coin-earnings-q3-2026-.html"), ("Bloomberg · Binance $6.3B hack", "https://www.bloomberg.com/news/articles/2026-10-29/binance-founder-says-possible-hack-of-exchange-bitcoin-falls"), ("CNBC · Q2 report", "https://www.cnbc.com/2026/07/30/coinbase-coin-earnings-q2-2026.html"), ("Bloomberg · revenue falls third straight quarter", "https://www.bloomberg.com/news/articles/2026-07-30/coinbase-posts-loss-as-revenue-drops-for-third-straight-quarter"), ("Seeking Alpha · Citi partnership", SA+"4647563"), ("Seeking Alpha · CFTC clearing", SA+"4648080")])

S["CRCL"] = dict(
 name="Circle", what="Issuer of the USDC stablecoin; earns interest on reserves.",
 results="Q2 (Aug 5): EPS beat but revenue missed; USDC in circulation $73.3B (Jun 30); about 95% of revenue is reserve interest; reserve yield fell to 3.5%.",
 guide="2026 'other revenue' raised to $310–330M (about $180M is a one-time gain from the Arc token presale). Q3 consensus EPS $0.40.",
 capex="Acquisitions instead: Tazapay ($400M in stock).",
 partners=["Arc blockchain launched with Wall Street firms (Sep 16)", "Binance USDC promotion (Binance bought $100M of shares)", "Volante (banks)", "OKX investment", "Expansion into 40 markets"],
 catalysts=["⚠ Earnings Wed Nov 4 before the open", "Froze $800M of USDC tied to the Binance hack (CNBC)", "Fed stablecoin reserve rules"],
 macro="Interest rates (a Fed hike raises reserve income); crypto activity; stablecoin legislation.",
 risks="Falling rates; slowing USDC growth (one analysis says share is down); the CFO is leaving.",
 src=[("Seeking Alpha · Q2 beat on EPS", SA+"4625754"), ("Seeking Alpha · other-revenue guide", SA+"4626342"), ("Bloomberg · revenue misses", "https://www.bloomberg.com/news/articles/2026-08-05/circle-revenue-misses-estimates-as-crypto-markets-mired-in-rout"), ("CNBC · Binance hack: what we know", "https://www.cnbc.com/2026/10/30/billions-in-crypto-frozen-in-binance-hack-heres-what-happens-next-.html")])

S["RDDT"] = dict(
 name="Reddit", what="Social platform; ads plus AI data licensing (Google, OpenAI).",
 results="Q2 (Jul 30): revenue $805M, $74M above; EPS $1.25, $0.29 above; daily users 130.3M (+18%); data licensing ('other') $43M (+24%). Stock fell 11% on choppy Google search traffic.",
 guide="Q3 revenue $860–870M (vs $828M expected); adjusted EBITDA $385–395M. Q3 consensus EPS $1.30.",
 capex="Rising AI investment pressures cash flow (analysts).",
 partners=["Google and OpenAI data-licensing deals", "Joined the S&P 500 (Aug 14)"],
 catalysts=["⚠ Q3 earnings Thu Oct 29 after the close", "User-growth data (Piper says August accelerated)", "Alphabet Oct 28 (search traffic)"],
 macro="Ad market; Google search changes; EU rules for kids under 13.",
 risks="Reliance on Google for traffic; 44% off its high.",
 src=[("CNBC · Q2 report", "https://www.cnbc.com/2026/07/30/reddit-rddt-q2-2026-earnings-report.html"), ("Seeking Alpha · S&P 500 entry", SA+"4633045"), ("Seeking Alpha · August users accelerate", SA+"4641739")])

S["AAOI"] = dict(
 name="Applied Optoelectronics", what="800G and 1.6T optical transceivers for hyperscalers, built in Texas and Taiwan.",
 results="Q2 (Aug 6): revenue $191.9M (+86%); non-GAAP EPS $0.06; 800G volume more than doubled from Q1.",
 guide="Q3 revenue $255–290M. Demand expected to exceed capacity through mid-2027. Q3 consensus EPS $0.08.",
 capex="Capacity near 200K units/month, targeting about 650K 800G/1.6T units/month by year-end; expanding in the US and Taiwan; $600M at-the-market equity program (Aug 21).",
 partners=["Major hyperscaler orders: $53M (March), $71M (April); more than $324M across Mar–Apr (analyst tally)"],
 catalysts=["Earnings Thu Nov 5 after the close", "Lumentum Nov 5; Fabrinet Nov 2; 1.6T qualification timing"],
 macro="Optical shortage; AI capex; it moves with LITE and COHR.",
 risks="Share dilution; 1.6T timing could slip into 2027; 70% off its high.",
 src=[("Seeking Alpha · Q3 guide $255–290M", SA+"4628697"), ("Seeking Alpha · $53M hyperscaler order", SA+"4567596"), ("Seeking Alpha · optics sold out to 2029", SA+"4651678")])

S["IREN"] = dict(
 name="IREN", what="Former bitcoin miner turned AI cloud and data-center operator.",
 results="Its last quarterly report was in August (not reviewed in detail here).",
 guide="Targeted $3.4B of AI cloud ARR by end-2026 (set Nov 2025; we didn't find a newer figure).",
 capex="About $5.8B of GPU capex for the Microsoft contract; a $2.4B equipment financing led by Blue Owl (Aug 28); a 300 MW Spain data center coming online in 2028.",
 partners=["Microsoft: ~$9.7B over 5 years for GB300 GPU cloud (20% prepaid)", "Anthropic multiyear deal (reported by The Information, Oct 12; terms not disclosed)", "Nvidia cloud partner (Australia)"],
 catalysts=["Earnings Thu Nov 5 (estimated)", "Confirmation of Anthropic terms", "CoreWeave Nov 10 and Nebius Nov 10"],
 macro="Neocloud credit stress; bitcoin; one of the most-shorted stocks.",
 risks="Financing and execution; short-squeeze volatility; 67% off its high.",
 src=[("Seeking Alpha · Anthropic deal report", SA+"4653959"), ("Seeking Alpha · Spain data center", SA+"4655182"), ("Bloomberg · Microsoft $9.7B deal (2025)", "https://www.bloomberg.com/news/articles/2025-11-03/microsoft-signs-9-7-billion-ai-cloud-deal-with-australia-s-iren")])

S["BABA"] = dict(
 name="Alibaba", what="Chinese e-commerce plus Alibaba Cloud and Qwen AI models.",
 results="June quarter (Aug 20): revenue ¥268.95B (+9%); net income down 75%; cloud ¥48.4B (+45%); AI product revenue grew by triple digits for the 12th straight quarter.",
 guide="Will spend beyond its 3-year ¥380B AI plan. Consensus EPS $1.31 for the next report.",
 capex="Quarterly capex ¥67.7B (+75%). Target of 20 GW of data centers; new sites in Europe and the Middle East.",
 partners=["V900 AI chip and Qwen models (Sep 22)", "Possible approval to buy Nvidia RTX Pro 5500 chips", "Himax chip for its $450 AI glasses"],
 catalysts=["Earnings Tue Nov 24 (estimated)", "China e-commerce quality rules (stock fell Oct 22)", "US–China chip policy"],
 macro="China policy and stimulus; US export controls; Hong Kong market sentiment.",
 risks="Profit squeeze from AI spending; regulation.",
 src=[("CNBC · June-quarter results", "https://www.cnbc.com/2026/08/20/alibaba-cloud-revenue.html"), ("Seeking Alpha · V900 chip, 20 GW", SA+"4645223"), ("Seeking Alpha · quality-standards selloff", SA+"4655687")])

S["AEHR"] = dict(
 name="Aehr Test Systems", what="Wafer-level test and burn-in systems (FOX, Sonoma) for AI processors, silicon carbide and silicon photonics.",
 results="Fiscal Q4 2026 (Jul 14; quarter ended May 29): revenue $18.8M (vs $14.1M); GAAP EPS $0.04; record bookings $60.7M; effective backlog $100.6M. Fiscal 2026 revenue $50.0M.",
 guide="Fiscal 2027 revenue $130–150M (about 160–200% growth); non-GAAP net income 18–22% of revenue. Q1 consensus EPS $0.05 (Nasdaq).",
 capex="Light (an equipment maker; capacity follows orders).",
 partners=["Lead hyperscaler: follow-on Sonoma production orders for its next-gen AI processor (Oct; about $6M per Seeking Alpha)", "A top-tier AI processor supplier moving toward pilot production (Jul)", "Silicon-carbide WaferPak orders, incl. a major automaker", "Oppenheimer starts at Outperform (Sep 10); Jefferies at Buy (Aug)"],
 catalysts=["⚠ Fiscal Q1 results Mon Nov 2 after the close", "New AI-processor customer wins", "Nvidia earnings Nov 17"],
 macro="AI-accelerator build-outs; silicon-carbide demand from EVs; small-cap volatility.",
 risks="Lumpy orders from a few customers; valuation; 56% off its high even after +13% on Oct 27.",
 src=[("Aehr · fiscal Q4 results", "https://www.aehr.com/2026/07/aehr-test-systems-reports-fiscal-2026-fourth-quarter-and-full-year-financial-results-with-record-quarterly-bookings-and-100-million-effective-backlog/"), ("Seeking Alpha · $6M follow-on AI orders", SA+"4650915"), ("Seeking Alpha · Oppenheimer Outperform", SA+"4641618"), ("Seeking Alpha · Jefferies starts bullish", SA+"4633322"), ("Aehr · Nov 2 results date", "https://www.aehr.com/2026/10/aehr-test-systems-to-announce-first-quarter-fiscal-2027-financial-results-on-november-2-2026/")])

S["NOK"] = dict(
 name="Nokia", what="Network equipment: optical and IP networking for AI data centers (Infinera, bought 2025), mobile networks and patent licensing.",
 results="Q3 (Oct 22): net sales €5.15B (+9% at constant currency), €90M above estimates; comparable EPS €0.09, €0.03 above; comparable operating margin 11.7% (+220 bp). IP Networks +43%, Optical +18%; AI & cloud sales +123%, orders €1.5B.",
 guide="Full-year 2026 outlook unchanged. Expects combined Optical and IP Networks to grow 25–30% in 2027. Infinera integration finishes by end-2026, a year early, with €200M of net synergies.",
 capex="Investing in optical and IP for hyperscalers; restructuring and integration costs cut the reported operating margin to 3.8%.",
 partners=["Google's €13B Finland investment (optical and IP)", "T-Mobile + Nvidia: first AI-RAN call on a live network", "L&T Technology Services 5-year R&D deal (Oct 26)", "BofA upgraded to Buy (Apr)"],
 catalysts=["Reported Oct 22; next date not set", "Marvell–Lumentum deal talks (Bloomberg, Oct 28)", "Optical peers: Coherent Nov 4, Ciena Dec 10"],
 macro="AI data-center networking spend; telecom operator budgets; euro/dollar (it reports in euros).",
 risks="Free-cash-flow worries after Q3; slow mobile networks; 47% off its high.",
 src=[("Nokia · Q3 interim report", "https://www.nokia.com/system/files/2026-10/nokia_results_2026_q3.pdf"), ("Seeking Alpha · Q3 beat", SA+"4655689"), ("Seeking Alpha · 25–30% Optical/IP growth in 2027", SA+"4656040"), ("Seeking Alpha · L&T R&D deal", SA+"4657018"), ("Seeking Alpha · BofA upgrade", "https://seekingalpha.com/news/4574458")])

S["GOOGL"] = dict(
 name="Alphabet", what="Google Search and YouTube ads, Google Cloud (incl. its own TPU AI chips), Gemini AI models, Waymo.",
 results="Q3 (Oct 28): revenue $127.6B, up 25%; Google Cloud $30.7B, up 103% (GCP plus TPU system sales); Search $63.35B, up 12% but below the $64.96B estimate; EPS $2.12 vs $2.94 expected, hit by an $8.66B loss on equity holdings. First top- and bottom-line miss in nearly four years (CNBC).",
 guide="2026 capex held at $195–205B. Free cash flow about −$9B in the quarter, roughly three times the expected deficit (Fox Business).",
 capex="One of the four biggest AI spenders; its TPU program also buys from Broadcom (custom chips) and the optics chain.",
 partners=["TPU systems now sold to outside customers (a meaningful part of Cloud growth)", "Broadcom: TPU design partner", "Anthropic and other AI labs on Google Cloud"],
 catalysts=["Reported Oct 28; next report early February", "Worst day on record Oct 29 (−12.6%, ~$500B) on a search miss as ChatGPT, Claude and its own AI Mode take share (CNBC, Bloomberg)", "CNBC Investing Club cut its target to $350 from $400 (Oct 29)", "Nvidia earnings Nov 17 (AI read)"],
 macro="AI-spending scrutiny: investors now punish cash burn; antitrust remedies; ad market.",
 risks="AI eroding search revenue; negative free cash flow; capex discipline questions.",
 src=[("Alphabet · Q3 2026 results (SEC)", "https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm"), ("CNBC · Q3 earnings", "https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html"), ("CNBC · worst day ever, −$500B", "https://www.cnbc.com/2026/10/29/alphabet-google-microsoft-msft-shares-today-earnings.html"), ("Fox Business · $500B wipeout on AI spending fears", "https://www.foxbusiness.com/markets/google-parent-alphabet-suffers-nearly-500b-wall-street-wipeout-amid-ai-spending-fears")])

S["HPE"] = dict(
 name="Hewlett Packard Enterprise", what="AI and enterprise servers, networking (Juniper, bought 2025; Aruba) and hybrid cloud.",
 results="Fiscal Q3 (Sep 2; quarter ended Jul 31): record revenue $12.2B, up 34% (Juniper drove networking; Cloud & AI up on higher prices); non-GAAP EPS $1.02 vs $0.82 expected (Nasdaq).",
 guide="Raised: fiscal 2026 (Oct year-end) revenue growth 34–37%; about 15% growth at the midpoint for fiscal 2027, above estimates (Bloomberg). Plans to return at least 75% of Q4 free cash flow to shareholders.",
 capex="Builds AI racks to order; component costs (memory) are the margin swing factor.",
 partners=["Vultr: $1.2B AMD Helios AI rack order (Seeking Alpha)", "Nvidia and AMD AI systems", "Juniper networking synergies"],
 catalysts=["Fiscal Q4 earnings est. Wed Dec 3 (Nasdaq estimate)", "Super Micro and Dell results (AI-server read-through)", "Nvidia earnings Nov 17"],
 macro="Hyperscaler, neocloud and sovereign AI spending; memory and component prices; enterprise IT budgets.",
 risks="Juniper integration; rising component costs squeezing margins; a slowdown in AI-infrastructure orders.",
 src=[("Bloomberg · raises outlook on AI servers, networking", "https://www.bloomberg.com/news/articles/2026-09-02/hpe-lifts-sales-forecast-on-ai-demand-for-servers-networking"), ("HPE · fiscal Q3 results (SEC)", "https://www.sec.gov/Archives/edgar/data/0001645590/000164559026000078/ex-991x922026x8k.htm"), ("Seeking Alpha · rises 12% on AI infrastructure", SA+"4642222"), ("Seeking Alpha · 52-week high, Vultr order", SA+"4649989")])

S["FTNT"] = dict(
 name="Fortinet", what="Network security: FortiGate firewalls, secure networking/SASE and security operations.",
 results="Q3 (Oct 28): revenue $2.08B, up 20%; non-GAAP EPS $0.91 vs $0.86 expected; billings up 29% (product revenue up 37%). Gross margin 79.6% vs 80.1% expected on longer lead times and higher component costs.",
 guide="2026 billings raised again to $9.568–9.718B (from $9.35–9.55B). Stock still fell ~21–25% Oct 29 on the margin miss (CNBC, Seeking Alpha).",
 capex="Owns much of its real estate and builds its own ASICs; component (memory) costs are the margin swing.",
 partners=["Firewall refresh cycle", "SASE and AI-driven security operations"],
 catalysts=["Reported Oct 28; next report early February", "Analyst cuts Oct 29: RBC $165 (from $205), TD Cowen $190 (from $225), Deutsche $130, Scotiabank $140 (CNBC via TipRanks)", "Cyber incidents (e.g. the Binance hack) keep security spending in focus"],
 macro="Enterprise IT budgets; memory and component costs; software-sector selloff on AI-disruption fears.",
 risks="Gross-margin pressure; firewall refresh fading; valuation reset after the drop.",
 src=[("Seeking Alpha · falls despite strong Q3, higher guide", SA+"4659184"), ("Seeking Alpha · 2026 billings $9.568–9.718B", SA+"4659806"), ("Seeking Alpha · Q3 call transcript", "https://seekingalpha.com/article/4958933"), ("CNBC · biggest movers Oct 29", "https://www.cnbc.com/2026/10/29/stocks-making-the-biggest-moves-midday-adt-googl-cat-lly-cmg.html")])

S["NOW"] = dict(
 name="ServiceNow", what="Enterprise workflow software (IT, HR, customer service) and AI agents on its Now platform.",
 results="Q3 (Oct 28): revenue $4.11B (in line); subscription revenue $3.99B, up 21%; adjusted EPS $1.00 vs $1.02 expected; current RPO $13.65B, up 20.5%. Net new AI contract value up 65%.",
 guide="2026 subscription revenue raised to $15.78–15.79B; year-end AI contract-value target raised $200M to $1.7B. But cRPO and subscription growth guidance looked weaker; shares fell 27% Oct 29, a record drop, on fears AI disrupts traditional software (CNBC).",
 capex="Software; light capex.",
 partners=["Nvidia and hyperscaler AI partnerships", "AI agents (Now Assist) upsell"],
 catalysts=["Reported Oct 28; next report late January", "Analysts blame timing and accounting for the weak cRPO guide (Seeking Alpha)", "Salesforce and Workday results (software read)"],
 macro="Software multiples under pressure from AI-disruption fears; enterprise IT budgets; rates.",
 risks="AI agents cannibalizing seat-based software; growth slowing; sentiment on software.",
 src=[("CNBC · Q3 earnings, record drop", "https://www.cnbc.com/2026/10/29/servicenow-now-earnings-q3-2026.html"), ("Seeking Alpha · crashes on weak forecast", SA+"4660127"), ("ServiceNow · Q3 results (SEC)", "https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000092/erq3fy26.htm")])


# ===================== NOVEMBER 4, 2026 UPDATE =====================
# New names (ANET, WDC, CSCO, ALAB), a refreshed LRCX, a 2026 capex line for every name
# (company SEC filings for spending to date; outlet figures for guidance), and Nov 2–4 news.
CN_ = "https://www.cnbc.com/"
SEC_ = "https://www.sec.gov/Archives/edgar/data/"

S["ANET"] = dict(
 name="Arista Networks", what="High-speed Ethernet switches and software for AI clusters and cloud data centers (Microsoft and Meta are its largest customers).",
 results="Q3 (Nov 3, after the close): revenue about $3.66B, up 58.5% and above its $3.3B guide; adjusted EPS $1.20 vs $1.08 expected (Seeking Alpha).",
 guide="Q4 revenue $3.9–4.0B vs $3.60B expected; EPS $1.26–1.30 vs $1.15 (LSEG via CNBC). Initial fiscal 2027 outlook about $18.5B (38–40% growth) with a $7B AI-networking target. Shares rose about 12% after hours.",
 capex="2026: $84.2M spent in the first half vs $52.4M a year ago (SEC 10-Q). That's light because it outsources manufacturing; its demand follows cloud-titan capex.",
 partners=["Microsoft and Meta (largest customers)", "AI back-end and front-end networks for hyperscalers and neoclouds", "AMD Helios and Nvidia-based AI racks"],
 catalysts=["Reported Nov 3; next report mid-February", "Post-earnings price-target changes (prior: Citi $248, Evercore $250, JPMorgan $250)", "Cisco Nov 11 and Nvidia Nov 17 (AI-networking read)"],
 macro="Its customers' AI capex (Microsoft $170B, Amazon $220B, Alphabet $195–205B) is its revenue. The Nov 3 Democratic sweep raised worries about data-center restrictions (the incoming Texas governor pledged a moratorium).",
 risks="Customer concentration; supply costs (memory, optics); valuation after a 12% pop. Before the report it was about 22% off its high.",
 src=[("CNBC · after-hours movers: ANET +12% on guide", CN_ + "2026/11/03/stocks-making-the-biggest-moves-after-hours-anet-amd-smci-swks.html"), ("Seeking Alpha · Q3 results", SA + "4664027"), ("Seeking Alpha · FY27 outlook, AI target", SA + "4664443"), ("Seeking Alpha · 2026 outlook raised", SA + "4551641")])

S["WDC"] = dict(
 name="Western Digital", what="Hard-disk drives for cloud data centers (the flash business was spun off as Sandisk). AI data needs mass storage.",
 results="Fiscal Q1 FY27 (Oct 22): revenue $4.38B, up 55%; non-GAAP gross margin 58.1%; non-GAAP EPS $4.64 vs $4.10 expected (Seeking Alpha).",
 guide="Fiscal Q2 revenue $5.1B ±$100M at a 60–61% gross margin. 44TB HAMR drives in the first half of 2027; dividend raised 17% to $0.175.",
 capex="Fiscal 2027 (July year-start): $227M in Q1 vs $73M a year ago; fiscal 2026 total $418M (SEC 10-Q). The step-up funds the HAMR ramp.",
 partners=["Hyperscale cloud customers (most of revenue)", "HAMR technology roadmap"],
 catalysts=["Reported Oct 22; next report late January", "Seagate and Sandisk reads; Nvidia Nov 17", "Price-target cuts: Wells Fargo $450 from $730 (Oct 16)"],
 macro="Cloud storage pricing, DRAM/NAND input costs, AI capex sentiment.",
 risks="Industry capacity additions and pricing; input costs; 53.5% off its high, so the stock is volatile.",
 src=[("Seeking Alpha · FQ1 results", SA + "4656388"), ("Seeking Alpha · guide, HAMR timing", SA + "4655457"), ("Seeking Alpha · dividend raise", SA + "4627115")])

S["CSCO"] = dict(
 name="Cisco Systems", what="Networking (switches, routers, Silicon One AI chips), security (Splunk) and collaboration.",
 results="Fiscal Q4 (Aug 12): revenue $17.3B, up 18%; fiscal 2026 revenue $63.3B, up 12%. About $4B of AI-infrastructure revenue from hyperscalers in fiscal 2026, plus more than $1B of AI orders from neocloud, sovereign and enterprise customers. RPO $46.7B, up 7%.",
 guide="Fiscal 2027 revenue growth of about 15% guided (CNBC); Piper Sandler called the guide conservative. Shares fell 8.4% after the August report.",
 capex="Fiscal 2026 (to Jul 25): $1.41B vs $905M a year earlier (SEC 10-K). Product gross margin fell 0.5 point on memory costs.",
 partners=["Hyperscalers (AI networking)", "Neocloud and sovereign AI builds", "Nvidia Spectrum-X partnership"],
 catalysts=["⚠ Earnings Wed Nov 11 after the close: no new options into the report", "Arista's beat (Nov 3) raises the bar for AI networking", "Morgan Stanley target $135 (Aug)"],
 macro="Enterprise IT budgets, memory costs and AI networking share vs Arista and Nvidia.",
 risks="Slower growth expected after fiscal 2027; memory-driven margin pressure; 21% off its high.",
 src=[("CNBC · shares slide despite beat (Aug 13)", CN_ + "2026/08/13/cisco-shares-slide-9percent-despite-earnings-beat-and-strong-guidance.html"), ("Seeking Alpha · Q4 and analyst reactions", SA + "4632225"), ("Seeking Alpha · FY26 AI orders", SA + "4550809")])

S["ALAB"] = dict(
 name="Astera Labs", what="Connectivity chips for AI racks: PCIe/CXL retimers (Aries), Scorpio fabric switches, Leo memory controllers, Taurus cables.",
 results="Q3 (Nov 3): record revenue $584.9M, up 154% and 49% sequentially; non-GAAP gross margin 72.4%; non-GAAP EPS $1.32. Scorpio fabric switches became its largest product family (company release).",
 guide="Q4 revenue $730–750M; non-GAAP EPS $1.62–1.66 vs $1.43 consensus (Seeking Alpha); gross margin about 72%. Aries 7 sampling in Q4. Shares erased losses and rose slightly after hours.",
 capex="2026: $73.4M in the first 9 months vs $18.9M a year ago (Q3 release). It's fabless, so capex stays light.",
 partners=["Hyperscaler custom-accelerator and GPU platforms (Nvidia, AMD and others)", "Orion rack-scale reference design (customers choose GPU/CPU)"],
 catalysts=["Reported Nov 3; next report early February", "Post-earnings price-target changes", "Nvidia Nov 17; AWS re:Invent Nov 30"],
 macro="AI-rack build pace and hyperscaler capex; trades with the AI-connectivity group (CRDO, MRVL, ANET).",
 risks="Customer concentration; a high valuation (about 35x 2026 sales per Seeking Alpha); 52% off its high, so it swings hard. Jefferies cut its target to $350 from $450.",
 src=[("Astera Labs · Q3 2026 results (SEC)", SEC_ + "0001736297/000173629726000044/q326exhibit991.htm"), ("Seeking Alpha · Q3 and guide top estimates", SA + "4663598"), ("Seeking Alpha · Q2 results", SA + "4625643")])

S["LRCX"] = dict(
 name="Lam Research", what="Etch and deposition equipment, heavily tied to memory (HBM, NAND) and advanced-logic capex.",
 results="Fiscal Q1 FY27 (Oct 21): revenue $8.22B, up 54%; non-GAAP EPS $2.20, $0.02 above; operating margin above 40%.",
 guide="December quarter $8.60B ±$0.4B, gross margin 52.5%, EPS $2.33 ±$0.15. That was below Morgan Stanley's >$9B hope, on supply constraints and a lower China share, and the stock fell 12% on Oct 22. Sees 2027 wafer-equipment spending above $200B.",
 capex="Fiscal 2027 (July year-start): $257.7M in Q1 vs $185.1M a year ago; fiscal 2026 total $966.4M (SEC 10-Q). Plus a $3B R&D lab network over 5 years.",
 partners=["Memory makers (SK hynix, Samsung, Micron) are its key customers", "TSMC and Intel (advanced logic and packaging)"],
 catalysts=["Reported Oct 21; next report late January", "Applied Materials Nov 12 (group read)", "SK hynix plans to raise investment significantly in 2027; KLA sees 2027 WFE above $200B", "Deutsche Bank Buy, $375 target (Oct 19)"],
 macro="Export controls and China; memory capex; the Nov 4 Asia chip-equipment selloff (Tokyo Electron −7%, Disco −10%) after the US midterms.",
 risks="China decline; supply constraints; 47% off its high.",
 src=[("Seeking Alpha · retreats 12% on cautious guide", SA + "4656207"), ("Seeking Alpha · Dec-quarter guide", SA + "4650254"), ("Seeking Alpha · Deutsche expects strong results", SA + "4654214"), ("CNBC · Nov 4 futures, Asia chip selloff", CN_ + "2026/11/03/stock-market-today-live-updates.html")])

# ---- 2026 capex for every name (spending to date from SEC filings; guidance from outlets) ----
CAPEX26 = {
 "SKHY": "2026: guided to the high-40 trillion won range, raised in July (CNBC; Bloomberg: at least ₩45T, about $31B). Q3 capex about $9.3B, up 265% (Seeking Alpha). ₩54T committed to two new fabs, Yongin Y2 and Cheongju M17 (Aug 7). M15X is at full capacity by year-end, and investment rises 'significantly' in 2027.",
 "AMZN": "2026: about $220B guided (held Oct 29). It spent $175.7B Jan–Sep vs $92.3B a year ago (SEC 10-Q); Q3 alone was $77.3B vs $58.7B expected. 2025 total: $131.8B. Trailing free cash flow of −$42.4B drove the selloff.",
 "AVGO": "Fiscal 2026 (Nov year-end): $1.01B in the first 9 months vs $386M; fiscal 2025 total $623M (SEC). That's small for its size. The real exposure is customers' AI budgets and the $50B+ OpenAI chip-financing talks.",
 "SPCX": "2026: $48.1B in the first 9 months vs $13.9B a year ago (SEC); Q3 alone $19.6B, more than its revenue. Funded by a ~$40B debt sale. KeyBanc (Nov 2) says heavy Starbase spending delays cash returns.",
 "INTC": "2026: $10.2B through Sep 26 vs $11.2B a year ago; 2025 total $14.65B (SEC). Spending is held below last year while Arizona fab tools are installed.",
 "HPE": "Fiscal 2026 (Oct year-end): $1.90B through Jul 31 vs $1.65B; fiscal 2025 total $2.29B (SEC). It builds AI racks to order; memory costs are the margin swing.",
 "TER": "2026: $241.8M in the first 9 months vs $161.1M, already above 2025's full-year $224M (SEC). The money adds capacity for AI-chip and HBM test.",
 "AMAT": "Fiscal 2026 (Oct year-end): $1.99B through Jul 26 vs $1.48B; fiscal 2025 total $2.26B (SEC). Plus a $5B EPIC R&D center and $5B for India. Customers' spending: KLA sees calendar-2026 WFE in the mid-$150B range and 2027 above $200B.",
 "CIEN": "Fiscal 2026 (Oct year-end): $194.9M through Aug 1 vs $95.4M, already above fiscal 2025's $140.8M (SEC). It also launched a $200M venture fund.",
 "MRVL": "Fiscal 2027 (Jan year-end): $282.4M in the first half vs $166.3M; fiscal 2026 total $354.1M (SEC). That's light because it's fabless. The big capital move is the $115B all-stock Lumentum deal (Nov 2).",
 "COHR": "Fiscal 2026 (to Jun 30): $1.10B vs $440.8M a year earlier, 2.5x (SEC). It's expanding transceiver and 300mm silicon-carbide capacity.",
 "CRDO": "Fiscal 2027 (May year-start): $7.3M in Q1 vs $2.8M; fiscal 2026 total $57.3M (SEC). Light because it's fabless; its demand follows hyperscaler AI-cluster builds.",
 "QCOM": "Fiscal 2026 (Sep year-end): $1.58B through Jun 28 vs $785M; fiscal 2025 total $1.19B (SEC). Spending doubled as it builds data-center silicon.",
 "VICR": "2026: $39.7M in the first 9 months vs $14.8M, nearly double 2025's $20.3M (SEC). Fab-2 equipment deployment targeted for Q2 2027.",
 "ARM": "Fiscal 2027 (Apr year-start): $197M in Q1 vs $154M; fiscal 2026 total $545M (SEC). Rising as it moves into its own chips.",
 "NVDA": "Fiscal 2027 (Jan year-end): $4.43B in the first half vs $3.12B; fiscal 2026 total $6.04B (SEC). It's putting larger sums into partners: a ~$10B European push and German AI startups. TD Cowen says it may be backstopping Oracle data centers.",
 "VRT": "2026: $425M in the first 9 months vs $126.7M, nearly double 2025's $220M (SEC). It's also buying capacity: UtilityInnovation Group ($1.45B + earnouts) and King Environmental (liquid cooling).",
 "HOOD": "2026: $32M (equipment and capitalized software) in the first 9 months vs $28M (SEC). That's light. It bought its first $25M of bitcoin for the balance sheet (Oct 7).",
 "IONQ": "2026: $18.6M in the first half vs $3.5M, already above 2025's $16.4M (SEC). Funded by equity: about $2B net from a stock and warrant offering (Oct 14).",
 "KLAC": "Fiscal 2027 (July year-start): $194.8M in Q1 vs $95.9M; fiscal 2026 total $375.9M (SEC). Customers' spending: it sees calendar-2026 WFE in the mid-$150B range and 2027 above $200B.",
 "ORCL": "Fiscal 2027 (June year-start): $28.5B in Q1 vs $8.5B; fiscal 2026 total $55.7B (SEC). The CFO puts fiscal 2027 net capex at about $70B. Funding: a $20B stock-and-bond raise (Nov 2; the $10B stock sale priced at $116).",
 "GLW": "2026: $1.30B in the first 9 months vs $850M, already above 2025's $1.28B (SEC), adding optical-fiber capacity for AI. It also has a $2B equity distribution agreement (Sep 14).",
 "NBIS": "2026: $20–25B guided; customer prepayments cover 50–70% of project capex. New $3.5B Citi financing facility (Oct 22).",
 "BE": "2026: $231.3M in the first 9 months vs $33.8M, 4x 2025's $56.8M (SEC), for the factory expansion (Sep 29). That spending is why Q3 cash flow disappointed.",
 "DOCN": "2026: $105.1M in the first 9 months vs $102.9M; 2025 total $129.1M (SEC). About 155 MW of committed data-center capacity; $725M equipment-finance facility (Sep 10).",
 "AKAM": "2026: $246.6M in the first half vs $263.3M; 2025 total $507.8M (SEC). Analysts estimate about $5.5B of capex to serve the Anthropic contract, starting in 2027.",
 "FTNT": "2026: $212.8M in the first 9 months vs $322M a year ago, down about a third (SEC). It's a light-capex software and appliance model.",
 "NOW": "2026: $346M in the first 9 months vs $630M, down 45%; 2025 total $868M (SEC). Light; it's software.",
 "CRWV": "2026: $35–39B guided (raised from $31–35B); $14.1B spent in the first half vs $3.9B (SEC). Debt about $35.6B; Q2 net interest $640M.",
 "VST": "2026: $1.57B in the first half vs $1.46B; 2025 total $2.75B (SEC). The DOE confirmed a loan of up to $4.2B to raise nuclear output (Oct 5).",
 "COIN": "No separate capex line. 'Other investing' (incl. software and equipment) was $85.0M in the first 9 months vs $86.3M, and it bought $217.9M of crypto for investment (SEC 10-Q). It cut its 2026 expense guidance after a May restructuring.",
 "CRCL": "2026: $35.8M (capitalized software) in the first half vs $24.9M; 2025 total $56.2M (SEC). Light. It's spending on acquisitions instead: Tazapay ($400M in stock).",
 "BABA": "Latest quarter's capex was ¥67.7B, up 75%. It targets 20 GW of data centers, with new sites in Europe and the Middle East. As a foreign filer it has no quarterly 10-Q figure.",
 "CBRS": "2026: $548.9M in the first half vs $185.1M, 3x (SEC), building OpenAI capacity. 600 MW of data-center capacity under contract; Compute Nordic 165 MW site in Finland.",
}
for _t, _c in CAPEX26.items():
    S[_t]["capex"] = _c

# ---- Nov 2–4 news ----
S["MRVL"]["catalysts"] = ["Nov 2: agreed to buy Lumentum in an all-stock deal ($115B enterprise value, 4.5 MRVL shares per LITE share; MRVL holders keep ~67%). MRVL fell 13% that day. Expected to close in the first half of 2028", "BofA downgraded to Neutral and cut its target to $225 from $400 (Nov 3), citing the share overhang and a long China review", "Earnings Tue Dec 1 (estimated)"]
S["MRVL"]["risks"] = "About 50% share dilution and limited EPS accretion (BofA); a long regulatory review including China; deal-arbitrage pressure on the stock."
S["MRVL"]["src"] = S["MRVL"]["src"] + [("CNBC · Marvell to buy Lumentum for $115B", CN_ + "2026/11/02/marvell-to-buy-lumentum-in-115-billion-deal-in-ai-data-center-bet-.html"), ("CNBC · BofA downgrade", CN_ + "2026/11/03/acquisition-marvell-lumentum-acquisition-bofa-downgrade.html")]
S["ORCL"]["catalysts"] = ["Nov 2: filed a $20B raise ($10B stock, $10B notes) and fell 8.8%. The stock sale priced at $116 (an 11.2% discount); shares rebounded 5.9% Nov 3", "Stephens upgraded to Overweight (Nov 2): investor day resolved key questions", "Earnings Wed Dec 9"]
S["ORCL"]["src"] = S["ORCL"]["src"] + [("CNBC · files to sell $20B in stock, bonds", CN_ + "2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html"), ("Seeking Alpha · prices $20B offering at $116", SA + "4663122")]
S["COIN"]["catalysts"] = ["Morgan Stanley downgraded to Underweight and cut its target to $120 from $258 (Nov 2) on weak October trading. Q4 transaction revenue is tracking about 11% below consensus", "Rebounded 8% Nov 3 after a 15% three-day slide", "Next report February"]
S["COIN"]["src"] = S["COIN"]["src"] + [("CNBC · Morgan Stanley downgrade", CN_ + "2026/11/02/coinbase-stock-morgan-stanley-downgrade.html")]
S["BE"]["catalysts"] = ["Barclays upgraded to Overweight (Nov 3), citing faster demand, capacity and deposits; target $289 (from $319). The stock rose 9% that day", "Midterms: the Democratic sweep could slow data-center permits (Texas), but on-site power is the workaround", "New hyperscaler power contracts"]
S["BE"]["src"] = S["BE"]["src"] + [("CNBC · midday movers Nov 3 (Barclays upgrade)", CN_ + "2026/11/03/stocks-making-the-biggest-moves-midday-aapl-pltr-nvda-coin-be.html")]
S["DOCN"]["results"] = "Q3 (Nov 3): revenue $321M, up 40%; a record $160M of incremental ARR; AI-customer ARR up 288% to $376M; customers spending $100K+ are 41% of revenue (company release)."
S["DOCN"]["guide"] = "Raised its Q4 exit growth rate to 44–45% and expects 2027 revenue growth of 60% or more. The stock rose 0.8% on the day."
S["DOCN"]["catalysts"] = ["Reported Nov 3; next report February", "CoreWeave Nov 10 and Nebius Nov 12 (neocloud read)", "AI-capacity additions (155 MW committed)"]
S["DOCN"]["src"] = [("DigitalOcean · Q3 2026 results (SEC)", SEC_ + "0001582961/000162828026069125/a2026-q3dopressrelease.htm"), ("Seeking Alpha · Q3 call transcript", "https://seekingalpha.com/article/4961526-digitalocean-holdings-inc-docn-q3-2026-earnings-call-transcript")] + S["DOCN"]["src"]
S["NVDA"]["catalysts"] = ["⚠ Earnings Tue Nov 17 after the close: no new options into the report", "Melius kept Buy but cut its target to $315 from $420 (Nov 2); Bernstein reiterated Outperform (Nov 3)", "AMD beat Nov 3 (EPS $2.09 vs $1.95); Super Micro guided FY27 sales of $72–82B vs $69.2B", "Nvidia AI Day Seoul Nov 9–10; GTC DC Nov 30–Dec 3"]
S["SPCX"]["catalysts"] = ["Fell 5–6% overnight Nov 3–4 on the midterm results; Tesla −4%", "Morgan Stanley reiterated Overweight (EchoStar tie-up thesis, Nov 3); KeyBanc Sector Weight on Starbase capex (Nov 2)", "Tesla merger terms; debt-sale pricing"]
S["SKHY"]["catalysts"] = ["Fell 5.1% in Seoul Nov 4 as Asian chip stocks sold off after the US midterms (Nikkei −4.5%)", "Nvidia AI Day Seoul Nov 9–10; Nvidia earnings Nov 17", "Reported Oct 27 (record ₩83.3T operating profit); next date not set"]
S["CRWV"]["catalysts"] = ["⚠ Earnings Tue Nov 10 after the close: no new options into the report", "Down about 41% in a month; short interest above 21% of float (CNBC, Nov 3)", "Midterms: data-center restriction fears (Texas holds ~27% of US data-center GW, per Wells Fargo)"]
S["NBIS"]["catalysts"] = ["⚠ Earnings Thu Nov 12 before the open (Nasdaq): no new options into the report", "CoreWeave Nov 10", "Rose 7% Nov 3 as AI names rebounded"]
S["CBRS"]["catalysts"] = ["⚠ Earnings Thu Nov 12 after the close (Nasdaq)", "New OpenAI capacity tranches", "Nvidia Nov 17"]
S["IONQ"]["catalysts"] = ["⚠ Earnings Thu Nov 5 after the close (Nasdaq)", "Quantum-sector headlines", "Integration of SkyWater and Elisity"]
for _t in ("VST", "VRT", "BE", "CRWV", "NBIS", "IREN"):
    if _t in S and "Midterm" not in S[_t]["macro"]:
        S[_t]["macro"] = S[_t]["macro"] + " Midterms (Nov 3): Democrats are projected to win both chambers, and Texas's governor-elect pledged a data-center moratorium. Traders bet that slows the buildout."


# ===================== NOV 4 (2): DATADOG ADDED + COMPANY PROFILES =====================
S["DDOG"] = dict(
 name="Datadog", what="Cloud observability and security software: monitoring, logs, application performance and LLM observability.",
 results="Q3 (Nov 4, before the open): revenue $1.20B, up 35%; non-GAAP EPS $0.81; non-GAAP operating margin 28%; free cash flow $251M; about 4,860 customers with $100K+ ARR, up 20% (company release). Beat on both revenue and EPS (CNBC).",
 guide="Q4 revenue $1.19–1.20B vs a $1.20B consensus (CNBC), roughly flat with Q3; non-GAAP EPS $0.69–0.71. Full-year 2026 revenue $4.515–4.525B. Shares sank 17% on the soft outlook after running 62% higher this year (CNBC); −14.8% at 11:32 AM PT Nov 4 (Nasdaq).",
 capex="2026: $122.0M in the first 9 months ($32.1M of equipment + $89.9M of capitalized software) vs $99.4M a year ago (Q3 release). Light, because it runs on the public clouds rather than its own data centers.",
 partners=["AWS, Microsoft Azure and Google Cloud (it runs on them and sells through their marketplaces)", "AI-native customers (its fastest-growing usage group)", "Scout 1.0, its first specialized AI model, now powers Bits Investigation (Q3)"],
 catalysts=["Reported Nov 4 (before the open); next report mid-February", "Post-earnings price-target changes (before the report: Bernstein $350, BofA $335, Benchmark $330)", "Cloud-growth reads: AWS grew 39% in Q3; Snowflake and MongoDB report in coming weeks"],
 macro="Software sentiment (AI-disruption fears hit ServiceNow and Fortinet in late October), cloud-consumption trends and rates. Midterm data-center worries matter less here than for hardware names.",
 risks="Usage-based revenue slows quickly when customers optimize cloud spend; reliance on fast-growing AI-native customers; valuation after a 62% run this year.",
 src=[("Datadog · Q3 2026 results (SEC)", SEC_ + "0001561550/000162828026069792/ex-991x20260930x8k.htm"), ("CNBC · premarket movers Nov 4 (DDOG −17%)", CN_ + "2026/11/04/stocks-making-the-biggest-moves-premarket-djt-tsla-crwv-nvo.html"), ("Seeking Alpha · shares fall after in-line Q4 outlook", SA + "4664674"), ("Seeking Alpha · Bernstein upgrade to Outperform", SA + "4654186")])

# What each company does and what it specializes in (shown at the top of every stock page)
PROFILE = {
 "SKHY": "South Korean memory chipmaker (Icheon; founded 1983 as Hyundai Electronics) and one of the world's two largest DRAM makers. It leads in high-bandwidth memory (HBM), the stacked DRAM that sits next to Nvidia's AI GPUs, and also makes NAND flash and enterprise SSDs (through Solidigm).",
 "AMZN": "Seattle-based e-commerce and cloud giant. Amazon Web Services (AWS) is the world's largest cloud provider and earns most of Amazon's operating profit; the company also runs the largest US online store, a fast-growing ads business and Prime. It designs its own AI chips (Trainium, Inferentia) and is Anthropic's main cloud partner.",
 "AVGO": "Broadcom (Palo Alto) designs semiconductors and infrastructure software. Its growth engine is custom AI accelerators (XPUs/ASICs) built with hyperscalers such as Google, plus the Tomahawk and Jericho Ethernet switch chips that network AI clusters; it also sells broadband, wireless and storage chips and VMware cloud software.",
 "SPCX": "SpaceX (Starbase, Texas) is the world's dominant rocket launcher (Falcon 9, Starship) and runs Starlink, the largest satellite-internet network, including direct-to-cell service. It also has a fast-growing AI business ('Super Intelligence', formerly xAI) that builds large AI data centers.",
 "INTC": "Intel (Santa Clara) designs and manufactures x86 processors for PCs (Core) and servers (Xeon), and is building Intel Foundry to make chips for outside customers on its 18A/14A processes in Arizona and Ohio. It also owns stakes in Mobileye and Altera; the US government became a major shareholder in 2025.",
 "ANET": "Arista Networks (Santa Clara) sells high-speed Ethernet switches and its EOS network software to cloud titans and enterprises. It specializes in the data-center networks that connect AI GPU clusters, with Microsoft and Meta as its largest customers, and also sells campus switching, Wi-Fi and network observability.",
 "WDC": "Western Digital (San Jose) makes high-capacity hard-disk drives, mostly for cloud data centers, after spinning off its flash business as Sandisk in 2025. It specializes in nearline drives (30TB+, with HAMR and ePMR recording) that store the data AI models train on and generate; hyperscalers buy most of its output.",
 "HPE": "Hewlett Packard Enterprise (Houston) sells servers (including Nvidia- and AMD-based AI systems and Cray supercomputers), storage and networking, greatly expanded by its 2025 purchase of Juniper Networks, plus the GreenLake hybrid-cloud platform. It specializes in AI infrastructure for enterprises, governments and neoclouds.",
 "TER": "Teradyne (North Reading, Massachusetts) makes automated test equipment that checks chips before they ship, including AI accelerators, HBM memory and networking chips, plus electronics system test. It also owns Universal Robots and MiR (collaborative and mobile robots).",
 "AMAT": "Applied Materials (Santa Clara) is the world's largest chip-equipment maker by revenue. It supplies deposition, etch, ion-implant, inspection and advanced-packaging tools to foundries (TSMC, Samsung, Intel) and memory makers, plus a large service business for installed tools.",
 "LRCX": "Lam Research (Fremont) makes wafer-fabrication equipment, specializing in etch and deposition: the steps that carve and layer the 3D structures in NAND, DRAM/HBM and leading-edge logic chips. Memory makers are its largest customers, and services and spares are a big recurring business.",
 "CIEN": "Ciena (Hanover, Maryland) is a leading maker of optical networking systems and coherent optics (its WaveLogic modems) that move data over fiber between data centers, across cities and under oceans. Customers are telecom carriers, cable operators and, increasingly, cloud providers linking AI data centers.",
 "MRVL": "Marvell Technology (Santa Clara-based, fabless) designs data-infrastructure chips: custom AI accelerators for hyperscalers such as Amazon and Microsoft, electro-optical DSPs and interconnect chips that link AI servers, and switching, storage and automotive Ethernet chips. On Nov 2 it agreed to buy Lumentum (lasers and optics) for ~$115B in stock.",
 "COHR": "Coherent Corp. (Saxonburg, Pennsylvania; formerly II-VI) makes optical transceivers, lasers and engineered materials. It specializes in the 800G and 1.6T datacom transceivers that connect AI clusters, plus industrial lasers and silicon-carbide substrates for power chips.",
 "CRDO": "Credo Technology (San Jose, fabless) specializes in high-speed connectivity for AI data centers: active electrical cables (AECs) that link servers and switches, SerDes chiplets and IP, and optical DSPs. A few hyperscalers make up most of its revenue.",
 "QCOM": "Qualcomm (San Diego) designs Snapdragon processors and modems for smartphones and licenses its wireless patents (QTL). It is diversifying into PCs, automotive chips, IoT and data-center AI processors, and supplies Starlink Mobile base-station hardware to SpaceX.",
 "VICR": "Vicor (Andover, Massachusetts) designs and builds modular power components: high-density converters and power-delivery modules that feed hundreds of amps to AI processors at the board level. It also licenses its power patents; a few large AI and computing customers drive its revenue.",
 "ARM": "Arm Holdings (Cambridge, UK; majority-owned by SoftBank) designs CPU architectures and licenses them to chipmakers, earning royalties on nearly every smartphone and a growing share of data-center and PC chips (Nvidia Grace, AWS Graviton, Google Axion). It has started making its own chips.",
 "NVDA": "Nvidia (Santa Clara, fabless) is the dominant supplier of AI accelerators: data-center GPUs (Blackwell, Rubin), the CUDA software platform, and NVLink, InfiniBand and Spectrum-X networking sold as full rack-scale systems. Data center is the vast majority of revenue; gaming, visualization and automotive are smaller.",
 "CSCO": "Cisco Systems (San Jose) is the largest networking-equipment maker: routers, switches (including its Silicon One chips for AI data centers), Wi-Fi, plus a large security and observability software business (Splunk, bought 2024). Customers span enterprises, telecoms, governments and hyperscalers.",
 "ALAB": "Astera Labs (San Jose, fabless; IPO 2024) makes the connectivity chips inside AI racks: Aries PCIe/CXL retimers, Scorpio fabric switches, Leo memory controllers and Taurus smart cables that move data between GPUs, CPUs and memory. Hyperscalers and AI-platform builders are its customers.",
 "DDOG": "Datadog (New York) sells cloud-based observability and security software that monitors infrastructure, applications, logs and user experience, plus LLM/AI observability. Pricing is usage-based, so revenue tracks cloud consumption on AWS, Azure and Google Cloud; AI-native companies are its fastest-growing customers.",
 "VRT": "Vertiv (Westerville, Ohio) makes the power and cooling equipment inside data centers: UPS and power distribution, thermal management and liquid cooling for high-density AI racks, plus services. Hyperscalers, colocation providers and Nvidia rack designs drive its demand.",
 "HOOD": "Robinhood Markets (Menlo Park) runs a commission-free app for trading stocks, options and crypto, plus Gold subscriptions, retirement accounts, banking, prediction markets and an international crypto business (Bitstamp). Revenue tracks trading activity and interest on customer cash.",
 "IONQ": "IonQ (College Park, Maryland) builds trapped-ion quantum computers and sells access through the major clouds and as on-site systems. It has been buying companies to expand into quantum networking, sensing and secure communications.",
 "KLAC": "KLA Corp. (Milpitas) dominates process control: inspection and metrology tools that find defects and measure chips during manufacturing. Its tools are essential at leading-edge logic, memory and advanced packaging, so it gains as chips get more complex.",
 "ORCL": "Oracle (Austin) sells databases, enterprise applications (Fusion ERP, NetSuite, health records) and, increasingly, Oracle Cloud Infrastructure, which builds huge AI data centers for customers such as OpenAI. That buildout is funded with heavy debt and new stock.",
 "GLW": "Corning (Corning, New York) makes specialty glass and ceramics: optical fiber and connectivity for data centers and telecom, display glass, Gorilla Glass for phones, automotive emissions products and life-science labware. AI data-center fiber is its fastest-growing business.",
 "NBIS": "Nebius Group (Amsterdam; built from Yandex's former international assets) is an AI 'neocloud' that rents Nvidia GPU capacity and AI software to developers and large customers such as Microsoft and Meta. It also holds stakes in Avride (autonomous driving) and other tech businesses.",
 "BE": "Bloom Energy (San Jose) makes solid-oxide fuel cells that generate electricity on site from natural gas or hydrogen. Its fastest-growing market is power for AI data centers that can't wait for grid connections; Oracle and utilities such as AEP are customers.",
 "DOCN": "DigitalOcean (New York) runs a simple cloud platform for developers, startups and small businesses (virtual servers, storage, databases and managed Kubernetes) and is adding GPU capacity and AI-inference services.",
 "AKAM": "Akamai Technologies (Cambridge, Massachusetts) runs one of the world's largest content-delivery networks and sells cloud security (web-app firewall, DDoS protection, zero-trust access) and a growing distributed cloud-computing and AI-inference platform.",
 "FTNT": "Fortinet (Sunnyvale) is a leading network-security company: FortiGate firewalls built on its own security chips, secure networking (SD-WAN, SASE) and security-operations software, sold to enterprises, carriers and governments.",
 "NOW": "ServiceNow (Santa Clara) sells the Now Platform, cloud software that automates IT, HR, customer-service and other enterprise workflows. It is pushing AI agents and its Now Assist products across large enterprises and governments.",
 "CRWV": "CoreWeave (Livingston, New Jersey) is the largest AI 'neocloud', renting Nvidia GPU clusters to AI labs and hyperscalers such as Microsoft, OpenAI and Meta. It builds data centers with heavy debt financing, so its stock trades closely with its credit.",
 "VST": "Vistra (Irving, Texas) is one of the largest US power producers, with nuclear (including Comanche Peak), natural-gas and coal plants and a large retail-electricity business. It is signing long-term power deals with data centers.",
 "COIN": "Coinbase is the largest US crypto exchange: retail and institutional trading, custody (for most US bitcoin ETFs), USDC stablecoin revenue shared with Circle, staking, its Base blockchain, derivatives and prediction markets.",
 "CRCL": "Circle Internet Group (New York; IPO 2025) issues USDC, the second-largest dollar stablecoin, and earns most of its revenue from interest on USDC reserves, so falling rates hurt it. It also runs payment and cross-border settlement networks.",
 "BABA": "Alibaba Group (Hangzhou) runs China's largest e-commerce platforms (Taobao, Tmall), Alibaba Cloud (China's largest cloud provider), the Qwen AI models, international commerce (AliExpress, Lazada) and logistics (Cainiao).",
 "CBRS": "Cerebras Systems (Sunnyvale) builds wafer-scale AI processors (the WSE-3, a single chip the size of a silicon wafer) and sells AI computing both as systems and as a cloud inference service; OpenAI is a major customer.",
}
for _t, _p in PROFILE.items():
    S[_t]["profile"] = _p

# ---------------- NOV 6 UPDATE: new list order from his broker (45 names); APH, CRWD, LYTE, DRAM, NCLD added ----------------
LISTS = [
 ("top5", "Top 5", ["SKHY", "INTC", "AMZN", "AVGO", "SPCX"]),
 ("portfolio", "2026 Portfolio", ["ANET", "APH", "CRWD", "CSCO", "WDC", "HPE", "TER", "AMAT", "LRCX", "CIEN", "MRVL", "COHR", "CRDO", "QCOM", "VICR", "ARM", "NVDA", "ALAB", "LYTE", "DRAM", "NCLD"]),
 ("dips", "15–50% Dip", ["BE", "VRT", "KLAC", "NBIS", "DDOG", "HOOD", "IONQ", "ORCL", "GLW", "DOCN", "AKAM", "FTNT", "NOW", "CRWV", "VST", "COIN", "CRCL", "BABA", "CBRS"]),
]
ETFS = {"LYTE", "DRAM", "NCLD"}
RH_ = "https://www.roundhillinvestments.com/etf/"

S["APH"] = dict(
 name="Amphenol", what="Connectors, cable assemblies, antennas and sensors; its IT datacom unit makes the high-speed interconnect inside AI servers and racks.",
 results="Q3 (Oct 28): record sales $10.2B, up 65% (37% organic); orders $12.2B, book-to-bill 1.19; adjusted EPS $0.80, up 74%; adjusted operating margin 29.7%; free cash flow $1.6B. Sales and EPS both beat the top of its own guidance, led by 'exceptional' IT datacom growth (company release). Revenue beat consensus by about $727M (Seeking Alpha).",
 guide="Q4 sales $10.3–10.5B (about +60%), adjusted EPS $0.81–0.83. Full-year 2026 sales $36.9–37.1B (about +60%), adjusted EPS $2.82–2.84; CommScope's acquired business adds about $5.1B of 2026 sales. Excludes three pending deals (company release). Guidance topped consensus (Seeking Alpha).",
 capex="2026: $1,104.3M in the first 9 months vs $742.9M a year ago (Q3 10-Q cash-flow statement), up about 49% as it adds capacity for AI datacom demand.",
 partners=["AI datacom: high-speed copper and fiber interconnect for AI servers and racks (its fastest-growing market)", "Acquisitions: closed Empire Electronics (Sept); signed AdvancedPCB, Dexgreen and Humanetics Sensors (~$1.6B combined with Empire)", "CommScope connectivity business (acquired; ~$5.1B of 2026 sales)"],
 catalysts=["Reported Oct 28; next report late January (date not set)", "Dividend up 20% to $0.15 (paid Jan 13) and a new $4B buyback from Jan 1, 2027", "Price targets raised after Q3: JPMorgan $115, UBS $111 (Oct 29)", "AI rack build-outs and hyperscaler capex updates read straight through"],
 macro="Trades with AI data-center spending and hyperscaler capex; the Nov 5 chip rout on midterm data-center fears hit the AI-hardware group. Also exposed to autos, defense and industrial cycles.",
 risks="A pause in AI rack orders after record bookings; integration of several acquisitions; premium valuation after a long run.",
 src=[("Amphenol · Q3 2026 results (SEC)", SEC_ + "820313/000110465926119421/aph-ex99d1.htm"), ("Amphenol · Q3 2026 10-Q (SEC)", SEC_ + "820313/000110465926120646/aph-20260930x10q.htm"),
      ("Seeking Alpha · Amphenol jumps on Q3 revenue surge; guidance tops consensus", SA + "4658881-amphenol-jumps-on-q3-revenue-surge-guidance-tops-consensus"),
      ("Seeking Alpha · BNP Paribas ups target after management meeting", SA + "4645447-bnp-paribas-ups-estimates-price-target-on-amphenol-after-management-meeting")])

S["CRWD"] = dict(
 name="CrowdStrike", what="Cloud-native cybersecurity: the Falcon platform for endpoint, cloud, identity, SIEM and AI security.",
 results="Q2 FY27 (Aug 26, quarter to Jul 31): revenue $1.47B, up 26%; ARR $5.84B, up 25%, with record net new ARR of $333M (up 51%); non-GAAP EPS $0.31; record Q2 free cash flow $377M; cash $5.01B. Falcon Flex ARR passed $2.29B, up 101% (company release).",
 guide="Q3 FY27 (to Oct 31): revenue $1.523–1.529B, non-GAAP EPS $0.31. Full FY27 (to Jan 31, 2027): revenue $5.99–6.01B, ending ARR $6.60–6.61B, non-GAAP EPS $1.25–1.26; net new ARR growth outlook raised to 34% at the midpoint (company release).",
 capex="FY2027 (Feb–Jul 2026, first half): $222.0M of property and equipment plus $49.1M of capitalized software, vs $116.2M and $34.7M a year ago (Q2 10-Q cash-flow statement). Mostly data-center capacity for its cloud platform.",
 partners=["Nvidia: real-time AI security agents for data centers and cloud (deepened in 2026, per CNBC)", "AWS: AI, cloud and Next-Gen SIEM work; Project QuiltWorks coalition", "Cerebras collaboration (also on your list); Schwarz Digits partnership in Europe and the XM Cyber technology purchase"],
 catalysts=["Next earnings Tue Dec 1 after the close (est.)", "Deutsche Bank upgraded to Buy, target $300 from $240 (Nov 2); Truist Buy $300 (Sept 1)", "AI-agent security demand; Falcon Flex adoption"],
 macro="Software and cybersecurity sentiment (AI-disruption fears hit software in late October), plus breach headlines that lift security demand. Less tied to data-center capex than the hardware names.",
 risks="Valuation after a 114% run this year (CNBC, Nov 2); GAAP profit still near breakeven; competition from Palo Alto, Microsoft and Zscaler.",
 src=[("CrowdStrike · Q2 FY27 results (SEC)", SEC_ + "1535527/000153552726000029/crwd-20260826xex991.htm"), ("CrowdStrike · Q2 FY27 10-Q (SEC)", SEC_ + "1535527/000153552726000031/crwd-20260731.htm"),
      ("CNBC · Deutsche Bank upgrade, Nov 2", CN_ + "2026/11/02/this-stock-is-a-double-in-2026-and-still-has-room-to-run-deutsche-bank-says.html"),
      ("Seeking Alpha · Truist on the 'Mythos moment'", SA + "4638911-crowdstrikes-mythos-moment-drives-platform-wide-adoption-truist")])

_ETF_RES = "An ETF: no earnings, guidance or analyst targets. Judge it by its holdings' news, its price trend and its options (it has listed options)."
S["LYTE"] = dict(
 name="Roundhill Photonics & Optics ETF", what="Actively managed ETF holding a concentrated basket of global photonics and optics makers.",
 results=_ETF_RES + " Launched Aug 6, 2026; expense ratio 0.65% (Roundhill). Down sharply from its Aug 17 high with the optics selloff.",
 guide="Not applicable (ETF). The driver is the optics group's guidance: Lumentum, Coherent and Ciena reports, plus Marvell's pending purchase of Lumentum.",
 capex="Not applicable (ETF has no capex). Its holdings ride AI data-center optics spending; see COHR and CIEN pages for their 2026 capex.",
 partners=["Top holdings (Roundhill): Lumentum, Eoptolink, Zhongji Innolight, Coherent, Ciena", "Overlaps your COHR, CIEN and, through Lumentum, MRVL"],
 catalysts=["Holdings' earnings: Lumentum and AAOI reported Nov 5; Coherent Nov 4", "Marvell–Lumentum deal news", "Hyperscaler capex and 800G/1.6T optics orders"],
 macro="AI networking spend, China supplier exposure (Eoptolink and Innolight are Chinese), and rates; it fell hard in the Nov 5 chip rout.",
 risks="Concentrated, actively managed and young (launched Aug 2026); China-listed holdings add tariff and export-control risk; wide option spreads.",
 src=[("Roundhill · LYTE fund page (holdings, launch, fee)", RH_ + "lyte/")])
S["DRAM"] = dict(
 name="Roundhill Memory ETF", what="Actively managed ETF holding a basket of global memory-chip makers (DRAM, HBM, NAND, storage).",
 results=_ETF_RES + " Launched Apr 2, 2026 (described by Roundhill as the first memory stock ETF); expense ratio 0.65%.",
 guide="Not applicable (ETF). The driver is memory pricing and its holdings' outlooks: SK hynix (record Q3), Micron and Samsung.",
 capex="Not applicable (ETF has no capex). Memory makers' capex drives LRCX, AMAT and TER; see SKHY's page for its 2026 capex.",
 partners=["Top holdings (Roundhill): Micron, Samsung, SK hynix, CXMT, Seagate", "Overlaps your SKHY and, through storage, WDC"],
 catalysts=["Memory price moves and HBM supply news", "Micron's next report (mid-December)", "Kospi and Korean export data"],
 macro="Memory is the tightest part of the AI supply chain; Qualcomm blamed a memory shortage for its Nov 4 guide. Moves with the Kospi and the chip index.",
 risks="Memory is the most cyclical corner of chips; a price rollover or capex cuts would hit it hard; foreign listings (Korea, China) add currency and policy risk.",
 src=[("Roundhill · DRAM fund page (holdings, launch, fee)", RH_ + "dram/")])
S["NCLD"] = dict(
 name="Roundhill Neocloud ETF", what="Actively managed ETF holding AI 'neocloud' companies that build and rent out GPU data centers.",
 results=_ETF_RES + " Launched Aug 6, 2026; expense ratio 0.65% (Roundhill). Down sharply since launch with the neocloud selloff.",
 guide="Not applicable (ETF). The driver is its holdings' guidance and financing: CoreWeave (reports Nov 10), Nebius and IREN.",
 capex="Not applicable (ETF has no capex). Its holdings are among the heaviest capex spenders; see CRWV and NBIS pages for their 2026 capex.",
 partners=["Top holdings (Roundhill): Nebius, CoreWeave, IREN, Hut 8, Galaxy", "Overlaps your NBIS and CRWV"],
 catalysts=["CoreWeave earnings Nov 10; Nebius Nov 12", "Neocloud financing deals and GPU-rental contracts", "Microsoft souring on neoclouds (Bloomberg, Nov 5) is the current headwind"],
 macro="Trades on credit and AI-capex sentiment: bond yields, financing spreads and hyperscaler contracts. Hit hardest in the post-midterm data-center selloff.",
 risks="Very volatile, concentrated holdings with heavy debt; young fund (Aug 2026); wide option spreads.",
 src=[("Roundhill · NCLD fund page (holdings, launch, fee)", RH_ + "ncld/")])

for _t, _p in {
 "APH": "Amphenol (Wallingford, Connecticut) is one of the world's largest makers of electrical and fiber-optic connectors, cable assemblies, antennas and sensors. Its IT datacom business, which supplies the high-speed copper and fiber interconnect inside AI servers and racks, is its fastest-growing market; it also serves autos, defense, aerospace, industrial and mobile devices, and has grown through a steady stream of acquisitions.",
 "CRWD": "CrowdStrike (Austin) sells cloud-delivered cybersecurity on its Falcon platform: endpoint protection, cloud and identity security, next-gen SIEM, threat intelligence and managed detection. It specializes in AI-driven threat detection and now in securing AI agents; customers buy modules through Falcon Flex subscriptions.",
 "LYTE": "Roundhill Photonics & Optics ETF: an actively managed fund (launched Aug 2026) holding a concentrated basket of global companies that make lasers, optical transceivers and other light-based components for AI data centers. Top holdings include Lumentum, Eoptolink, Zhongji Innolight, Coherent and Ciena.",
 "DRAM": "Roundhill Memory ETF: an actively managed fund (launched April 2026) holding a targeted basket of global memory-chip makers. Top holdings include Micron, Samsung, SK hynix, CXMT and Seagate, so it tracks DRAM, HBM and storage pricing.",
 "NCLD": "Roundhill Neocloud ETF: an actively managed fund (launched Aug 2026) holding AI 'neocloud' companies that build GPU data centers and rent the capacity on multi-year contracts. Top holdings include Nebius, CoreWeave, IREN, Hut 8 and Galaxy.",
}.items():
    S[_t]["profile"] = _p
