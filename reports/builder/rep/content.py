# Per-stock research content for the report, in Ricky's list order.
# Every fact comes from the notes gathered Oct 25–30, 2026 (his outlets: CNBC, Bloomberg, Seeking Alpha, plus company SEC filings where coverage cited them).
SA = "https://seekingalpha.com/news/"
LISTS = [
 ("top5", "Top 5", ["SKHY", "INTC", "AVGO", "AMZN", "SPCX"]),
 ("portfolio", "2026 Portfolio", ["MRVL", "CIEN", "VICR", "TER", "CRDO", "NVDA", "COHR", "ARM", "AMAT", "HOOD", "GOOGL", "GLW", "ORCL", "KLAC", "VRT", "IONQ"]),
 ("dips", "15–50% Dip", ["HPE", "NBIS", "DOCN", "FTNT", "BE", "NOW", "CRWV", "CBRS", "QCOM", "NOK", "AKAM", "AEHR", "AAOI", "VST", "COIN", "CRCL", "IREN", "BABA"]),
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
