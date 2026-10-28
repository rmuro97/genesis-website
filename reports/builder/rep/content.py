# Per-stock research content for the report, in Ricky's list order.
# Every fact comes from the notes gathered Oct 25, 2026 (his outlets: CNBC, Bloomberg, Seeking Alpha, plus company SEC filings where coverage cited them).
SA = "https://seekingalpha.com/news/"
LISTS = [
 ("top5", "Top 5", ["SKHY", "AVGO", "TER", "GLW", "SPCX"]),
 ("portfolio", "2026 Portfolio", ["BE", "CRDO", "CIEN", "MRVL", "AMAT", "VRT", "COHR", "HOOD", "ARM", "INTC", "KLAC", "NVDA", "QCOM", "AMZN"]),
 ("dips", "15–50% Dip", ["IONQ", "CBRS", "CRWV", "VICR", "LRCX", "NBIS", "VST", "ORCL", "AKAM", "DOCN", "BAC", "COIN", "CRCL", "RDDT", "AAOI", "IREN", "BABA"]),
]

S = {}

S["AVGO"] = dict(
 name="Broadcom", what="Custom AI chips (ASICs) for Google, OpenAI and Anthropic, plus AI networking and VMware software.",
 results="Fiscal Q3 (reported Sep 2): revenue $29.6B, up 86%; adjusted EPS $3.32 vs $3.24 expected; AI chip revenue $16.7B, up 221%.",
 guide="Fiscal Q4 revenue $34.8B (+93%), slightly under the $35.03B consensus; AI chip revenue $21.7B. Fiscal 2026 AI revenue raised to $58B (from $56B). Outlines $115B of AI chip revenue in fiscal 2027 and $230B in 2028.",
 capex="Its own capex is small. Its growth depends on customers' AI budgets, and it is now helping fund one: talks on a $50B+ financing deal for OpenAI's custom chips.",
 partners=["OpenAI and Anthropic custom chips (concentration flagged by analysts)", "Google TPU designs", "NTT DOCOMO 10-year VMware cloud deal (Oct 20)"],
 catalysts=["Earnings Thu Dec 10", "Hyperscaler earnings: Microsoft and Alphabet Oct 28, Amazon Oct 29 (AI spending read-through)", "Progress on the OpenAI financing deal", "Nvidia earnings Nov 18 and GTC DC (Nov 30–Dec 3)"],
 macro="CEO Hock Tan says capital, not demand, is now the biggest limit on AI. Higher rates and AI-credit stress hit names tied to OpenAI and Anthropic financing. It names wafers, substrates, HBM memory and power as supply bottlenecks.",
 risks="Customer concentration in OpenAI and Anthropic; off-balance-sheet financing exposure; Q4 guide only in line.",
 src=[("CNBC · Broadcom Q3 report", "https://www.cnbc.com/2026/09/02/broadcom-avgo-q3-earnings-report-2026.html"), ("Seeking Alpha · $58B FY26 AI, $115B/$230B outlook", SA+"4639799"), ("Seeking Alpha · $50B+ OpenAI chip financing talks", SA+"4651203"), ("Seeking Alpha · CEO: capital is the biggest constraint", SA+"4652302"), ("Seeking Alpha · NTT DOCOMO VMware deal", SA+"4654578")])

S["AMZN"] = dict(
 name="Amazon", what="AWS cloud (the profit engine), e-commerce, ads; Anthropic's main cloud partner.",
 results="Q2 (Jul 30): sales $200.6B, up 20%; operating income $27.5B. AWS $42.2B, up 37% (fastest in 18 quarters), AWS operating income $16.6B, $169B run rate.",
 guide="Q3 sales $197–202B (+9–12%), below the $204.1B consensus because Prime Day moved to June; operating income $22.5–26.5B. AWS backlog $496B.",
 capex="2026 capex raised to about $220B (from $200B) because memory prices rose; CEO Andy Jassy says that still won't meet 2026 demand. Analysts flag negative free cash flow.",
 partners=["Anthropic (AWS)", "3M expanded data-center products relationship (Oct 19)"],
 catalysts=["⚠ Q3 earnings Thu Oct 29 after the close: AWS growth vs Q2's 37%, the capex number, free cash flow", "Morgan Stanley Top Pick (Oct 19)", "AWS re:Invent Nov 30–Dec 4", "Holiday season (hiring plans up 20%)"],
 macro="The Fed (Oct 28) and GDP/PCE (Oct 29, the same day it reports) move megacaps. Memory costs drive capex. The Meta capex scare that hit AI stocks Oct 22 shows how its own capex number will be judged.",
 risks="Capex outrunning cash flow; soft Q3 retail guide; AI agents shopping on rival platforms (Walmart allows them, Amazon blocks them).",
 src=[("CNBC · AWS Q2 growth", "https://www.cnbc.com/2026/07/30/aws-earnings-q2-2026.html"), ("CNBC · capex raised to $220B", "https://www.cnbc.com/2026/07/30/amazon-amzn-q2-earnings-report-2026.html"), ("Seeking Alpha · Q3 guide $197–202B", SA+"4622393"), ("Seeking Alpha · Morgan Stanley Top Pick", SA+"4654306"), ("Seeking Alpha · 3M data-center deal", SA+"4654445")])

S["BE"] = dict(
 name="Bloom Energy", what="Solid-oxide fuel cells for on-site power at AI data centers.",
 results="Q3 (Oct 22): revenue $1.24B, $170M above estimates; non-GAAP EPS $0.94, $0.27 above. Stock still fell 11% on cash outflows and expansion costs.",
 guide="2026 revenue $4.4–4.6B; non-GAAP EPS outlook raised to $3.10–3.40.",
 capex="Factory capacity expansion (announced Sep 29). Spending on that expansion is why cash flow disappointed in Q3.",
 partners=["Oracle data-center power (a reported force-majeure notice on one Oracle site hit the stock Sep 24)", "Joined the S&P 500 in September"],
 catalysts=["The next earnings date isn't set (it just reported)", "Oracle AI World Oct 25–28 and Oracle investor day Oct 28", "New hyperscaler power contracts", "Trump's call (Oct 21) for data centers to supply their own electricity: a tailwind for on-site power"],
 macro="AI-power demand, utility grid limits and natural-gas prices (fuel). Rate-sensitive: a hike at the Oct 28 FOMC would weigh on it.",
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
 catalysts=["Earnings Tue Dec 1 (estimated)", "AWS re:Invent Nov 30 (custom chips)", "Peer reads: Credo, Broadcom, Arista"],
 macro="AI-capex sentiment; reads through to the whole optics group (AAOI, GLW, CIEN, COHR, CRDO).",
 risks="Program timing (TPU delays); one analyst downgraded to Hold after the investor-day rally.",
 src=[("Seeking Alpha · jumps on raised guidance at investor day", SA+"4650555"), ("Seeking Alpha · investor day $20B outlook", "https://seekingalpha.com/article/4952697"), ("Seeking Alpha · OCP security group", SA+"4652456")])

S["SKHY"] = dict(
 name="SK hynix", what="Memory chips: HBM for AI accelerators, DRAM and NAND (Solidigm).",
 results="Q2 (Jul 29): revenue about ₩79.3T (+257%), operating profit ₩60.5T (76% margin). Both were records but missed consensus; shares fell 9.6%.",
 guide="No formal guidance. HBM4 mass shipments began in Q2, with HBM4E samples out. Q3 results come before 9:00 AM Seoul on Oct 28, which is after the US close on Tue Oct 27.",
 capex="M15X fab started wafer processing; first phase of the Yongin fab targeted for Q1 2027. ASML is raising parts prices 10%.",
 partners=["HBM supplier to AI accelerator makers", "Solidigm (NAND): $10B US IPO pulled Oct 22; New York plant talks with Gov. Hochul", "SK Group chairman selling a 1.34% stake to the Dell family office (Oct 14)"],
 catalysts=["⚠ Q3 earnings Tue Oct 27 after the US close", "Samsung's full Q3 results ~Oct 29", "Nvidia AI Day Seoul Nov 9–10; Nvidia earnings Nov 18", "BofA expects bigger shareholder returns"],
 macro="Memory pricing, Korean won and the Kospi; China capacity (CXMT) and US approvals for its China fabs.",
 risks="Memory-cycle fears (Cathie Wood warned of 'vicious' cycles); China competition; high expectations (it missed in Q2).",
 src=[("CNBC · Q2 results", "https://www.cnbc.com/2026/07/29/sk-hynix-earnings-profit-revenue-hbm-memory.html"), ("Seeking Alpha · trims losses after Solidigm IPO pulled", SA+"4656416"), ("Seeking Alpha · BofA on shareholder returns", SA+"4656657"), ("Seeking Alpha · US NAND plant tied to China approvals", SA+"4653233"), ("SK hynix newsroom · Q3 date", "https://news.skhynix.com/en/?p=13734")])

S["AMAT"] = dict(
 name="Applied Materials", what="The largest chip-equipment maker (deposition, etch, inspection).",
 results="Fiscal Q3 (Aug 13): record revenue $9.12B and record non-GAAP EPS $3.50; raised its Q4 outlook.",
 guide="CEO raised his 2026 chip-systems expectations and sees another strong growth year in 2027. Q4 consensus EPS $4.06 (Nasdaq). China sales are limited by US export rules.",
 capex="Its own investments: a $5B EPIC R&D center (Oct 12) and $5B in India over a decade. Its demand follows foundry and memory capex.",
 partners=["Deeper Intel collaboration (Oct 6)", "KIOXIA next-gen memory (Sep 29)", "Singapore ties with KLA and GlobalFoundries"],
 catalysts=["Earnings Thu Nov 12 after the close", "KLA (Oct 28) and Intel (Oct 29) reports", "Lam's cautious Dec-quarter guide (Oct 21) is the overhang"],
 macro="Export controls and China; memory and foundry capex; Barron's says the group's trouble 'could be just getting started'.",
 risks="China revenue decline; supply-chain limits like those Lam flagged; 48% off its high.",
 src=[("Seeking Alpha · Q3 call transcript", "https://seekingalpha.com/article/4936471"), ("Seeking Alpha · $5B EPIC center", SA+"4652276"), ("Seeking Alpha · Intel collaboration", SA+"4650539"), ("Seeking Alpha · KIOXIA partnership", SA+"4648222")])

S["VRT"] = dict(
 name="Vertiv", what="Data-center power and liquid cooling.",
 results="Q2 (Jul 29): sales $3.27B, up 24%; adjusted EPS $1.52, up 60%; reached net cash. Stock fell 17% because organic growth (17.8%) missed the 23.6% estimate on project timing.",
 guide="2026: about $14B sales, $6.70 adjusted EPS, $2.5B free cash flow; 31% organic growth at the midpoint. Q3 consensus EPS $1.82.",
 capex="Buying capacity through acquisitions: UtilityInnovation Group ($1.45B + earnouts) and King Environmental Services (liquid cooling). Last backlog figure found: $15.0B (Q4 2025).",
 partners=["Hyperscaler and colocation customers"],
 catalysts=["⚠ Q3 earnings Wed Oct 28 before the open (FOMC day)", "Microsoft and Alphabet capex Oct 28 after the close", "Oracle AI World / investor day"],
 macro="AI-infrastructure trade; rising Treasury yields have hit this group before (Aug 18, Oct 15).",
 risks="Project-timing misses; integration of acquisitions.",
 src=[("CNBC · CEO on 17% drop", "https://www.cnbc.com/2026/07/29/vertiv-ceo-addresses-stock-plunge-disappointing-quarter.html"), ("Seeking Alpha · raised 2026 outlook", SA+"4621076"), ("Seeking Alpha · UtilityInnovation deal", SA+"4639364"), ("Seeking Alpha · King Environmental deal", SA+"4646516")])

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
 results="Q2: revenue $1.308B, up 32%; EPS $0.62, up 48%; net deposits $21.7B; Gold subscribers 4.84M; prediction-market (event contract) revenue $156M; crypto transaction revenue down 38%.",
 guide="Expense guide trimmed (analyst report). Q3 consensus EPS $0.56 (Nasdaq).",
 capex="Light. Bought its first $25M of bitcoin for its balance sheet (Oct 7).",
 partners=["Crypto.com (prediction markets)", "Susquehanna (Rothera prediction-market platform)", "Cboe KPI options approved by the SEC (Oct 14)", "Dubai expansion (Oct 23)"],
 catalysts=["⚠ Q3 earnings Tue Oct 27 after the close", "Coinbase Oct 29 and Circle Nov 4 reports", "SEC tokenized-stock framework (it rose 9% on Sep 18)"],
 macro="Bitcoin and trading volumes; rate path (interest income); crypto legislation (the Clarity Act stalled in the Senate).",
 risks="Crypto weakness; regulatory pushback on tokenized stocks.",
 src=[("SEC 10-Q / CNBC · Q2", "https://www.cnbc.com/2026/09/08/stock-market-today-live-updates.html"), ("Seeking Alpha · Dubai expansion", SA+"4656534"), ("Seeking Alpha · Cboe KPI options", SA+"4653064"), ("Seeking Alpha · tokenized stock framework", SA+"4644519")])

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
 results="Q2 (Jul 28): core sales $4.74B, up 17%; core EPS $0.78, up 30%; Optical Communications $2.07B, up 32% (Enterprise up 65%).",
 guide="Q3 core sales $4.9–5.0B (+16%), core EPS $0.85–0.89 (+28%). 'Springboard' run-rate targets: $20B by end-2026, $30B by 2028, $40B by 2030.",
 capex="Raised money through a $2B equity distribution agreement (stock fell 14%, Sep 14) to fund growth.",
 partners=["Verizon multi-billion fiber deal (Sep 8)", "AT&T multi-year fiber deal (Sep 29)", "Lumentum + Qualcomm AI optical tech (Sep 21)", "Zayo fiber deal"],
 catalysts=["⚠ Q3 earnings Tue Oct 27 before the open", "JPM expects strong AI revenue (Oct 21)", "Apple earnings Nov 2"],
 macro="AI optics demand; telecom fiber builds; solar trade policy (polysilicon tariffs).",
 risks="Share dilution from the equity program; 52% off its high.",
 src=[("Seeking Alpha · Springboard and Q3 guide", SA+"4619971"), ("Seeking Alpha · Verizon deal", SA+"4640949"), ("Seeking Alpha · AT&T deal", SA+"4648005"), ("Seeking Alpha · $2B equity offering", SA+"4642663")])

S["INTC"] = dict(
 name="Intel", what="CPUs (PC and data center) and a contract foundry (18A / 14A).",
 results="Q2 (Jul 23): revenue $16.1B, up 25% vs $14.42B expected; non-GAAP EPS $0.42 vs $0.21; data-center revenue $6.3B, up 59%.",
 guide="Q3 revenue $15.8–16.8B and EPS $0.38 (vs $15.1B / $0.27 expected). PCs flat because of the memory shortage. 18A output ~25% above target; expects external 14A customer decisions from 2H 2026 into 1H 2027.",
 capex="Arizona fab tools being installed (Wedbush says this supports revenue growth).",
 partners=["Applied Materials collaboration", "Musk's Terafab project", "Agentic AI is lifting CPU demand (Mizuho)"],
 catalysts=["⚠ Q3 earnings Thu Oct 29 after the close (GDP/PCE day)", "News of foundry customer wins", "JPM upgrade (Oct 19); named a long idea at Robin Hood (Oct 21)"],
 macro="Memory shortage limits PC builds; US industrial policy.",
 risks="Foundry customer timing; PC weakness.",
 src=[("CNBC · Q2 report", "https://www.cnbc.com/2026/07/23/intel-intc-earnings-report-q2-2026.html"), ("Seeking Alpha · Wedbush on Arizona fab", SA+"4656527"), ("Seeking Alpha · JPM upgrade", SA+"4654160")])

S["KLAC"] = dict(
 name="KLA", what="Chip process control and inspection equipment.",
 results="June quarter (Jul 28): revenue $3.66B, $60M above estimates; non-GAAP EPS $1.05.",
 guide="September quarter about $4B; raised its 2026 wafer-equipment market view to the low-$150B range. Q1 consensus EPS $1.18 (Nasdaq).",
 capex="Its demand follows foundry, memory and advanced-packaging spending. Margin pressure from memory prices, tariffs and supply lead times.",
 partners=["Singapore semiconductor ties with Applied Materials and GlobalFoundries"],
 catalysts=["⚠ Earnings Wed Oct 28 after the close (Nasdaq; FOMC day). Our older calendar showed Nov 4, so treat Oct 28 as the date.", "Fell 10% on Oct 22 after Lam's guide"],
 macro="Export controls; China; wafer-equipment cycle.",
 risks="Lam's caution spreading to the group; 52% off its high.",
 src=[("Seeking Alpha · ~$4B Sept-qtr, WFE low-$150B", SA+"4619965"), ("Seeking Alpha · falls 10%", SA+"4656277")])

S["NVDA"] = dict(
 name="Nvidia", what="AI accelerators (Blackwell, Vera Rubin), networking, software.",
 results="Fiscal Q2 FY27 (Aug 26): revenue $96.22B vs ~$92B expected; adjusted EPS $2.22; data center about $89B, up 117%; gross margin ~75%.",
 guide="Fiscal 2028 revenue growth about 70% (vs ~44–45% expected). Gross margin expected to bottom around 71–72% in fiscal Q4 because of memory costs. China data-center sales are excluded from the outlook. A secondary source puts fiscal Q3 at about $108B.",
 capex="Investing in partners: a ~$10B European push and backing German AI startups. TD Cowen says it may be backstopping Oracle data centers.",
 partners=["GTC Berlin deals: Amkor ($1.3B), Dell AI Factory, CrowdStrike, E.ON nuclear-site study", "~$35B of orders for a new export-compliant GPU from Chinese tech giants (report, Oct 20)", "Samsung using TSMC tech for its next memory chips"],
 catalysts=["Earnings Wed Nov 18", "Hyperscaler capex Oct 28–29", "Nvidia AI Day Seoul Nov 9–10; GTC DC Nov 30–Dec 3 (Huang keynote Dec 1)"],
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
 catalysts=["Earnings Thu Nov 12 (estimated)", "New OpenAI capacity tranches", "Nvidia Nov 18"],
 macro="AI-inference demand; OpenAI's funding health.",
 risks="Heavy reliance on OpenAI; losses; 64% off its high.",
 src=[("CNBC · Q2 report", "https://www.cnbc.com/2026/08/12/cerebras-cbrs-q2-earnings-report-2026.html"), ("Seeking Alpha · $880–890M core outlook", SA+"4632042"), ("Seeking Alpha · Altman 'close partner'", SA+"4650091")])

S["CRWV"] = dict(
 name="CoreWeave", what="AI 'neocloud' renting Nvidia GPU capacity.",
 results="Q2 (Aug 11): revenue $2.58B, up 112%; adjusted loss $1.03 per share (vs −$1.20 expected). Backlog $104B (about $129B including $25B signed early in Q3); 1.5 GW active power.",
 guide="Q3 revenue $3.4–3.6B; 2026 revenue $12.4–13.2B; adjusted operating income $960M–1.15B; more than 1.85 GW active by year-end. Q3 consensus EPS −$1.45.",
 capex="2026 capex $35–39B (raised from $31–35B). Debt about $35.6B; Q2 net interest $640M.",
 partners=["Anthropic and Meta contracts", "Nvidia (supplier)", "New robotics/EV workloads and a zero-trust AI framework (Oct 21)"],
 catalysts=["Earnings Mon Nov 9 (estimated)", "Financing news: credit spreads hit a record Oct 15", "Analyst split: Goldman upgrade and UBS Buy vs Bernstein 'not bottom yet'"],
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
 catalysts=["The next earnings date isn't set (late January)", "SK hynix Oct 27, KLA Oct 28, Samsung ~Oct 29 (memory capex read)"],
 macro="Export controls / China; memory capex; Barron's sees more downside for the group.",
 risks="China decline; supply constraints; 47% off its high.",
 src=[("Seeking Alpha · retreats 12% on cautious guide", SA+"4656207"), ("Seeking Alpha · >$200B 2027 WFE", SA+"4655710")])

S["TER"] = dict(
 name="Teradyne", what="Chip test equipment (AI accelerators, HBM/memory, networking) plus robotics.",
 results="Q2 (Jul 28): record revenue $1.33B (+104%), $110M above estimates; non-GAAP EPS $2.47, $0.42 above. About 70% of revenue is tied to AI.",
 guide="Q3 revenue $1.2–1.3B; GAAP EPS $1.79–2.09. Second half led by memory, auto/industrial, product test and robotics; mobile soft. Consensus EPS $2.04.",
 capex="Its demand follows AI-chip and HBM test needs.",
 partners=["FormFactor collaboration (Oct 12)"],
 catalysts=["⚠ Q3 earnings Tue Oct 27 after the close", "SK hynix the same night (HBM read)", "Fell 11% on Oct 22 in the chip selloff"],
 macro="Chip-equipment sentiment; memory test demand.",
 risks="Revenue swings from concentrated AI orders; ARK trimmed its stake.",
 src=[("Seeking Alpha · Q3 guide $1.2–1.3B", SA+"4620570"), ("Seeking Alpha · FormFactor collaboration", SA+"4652273")])

S["NBIS"] = dict(
 name="Nebius", what="AI neocloud (GPU cloud), CoreWeave's closest peer.",
 results="Q2 (Aug 12): revenue $582.3M (+454%); AI cloud $574.9M (+514%); annual run-rate $3.0B at end of June. Shares rose 28–34%.",
 guide="Reaffirmed 2026 revenue of $3.0–3.4B and annual run-rate (ARR) guidance of $7–9B; capacity target raised to 5 GW. Q3 consensus EPS −$0.43.",
 capex="2026 capex $20–25B; customer prepayments cover 50–70% of project capex. New $3.5B Citi financing facility (Oct 22).",
 partners=["Meta: $12B over 5 years on Vera Rubin from early 2027, plus up to $15B more", "Microsoft (capacity tranches delivered)", ">$40B of additional contracted revenue", "Bought Inferize (inference)"],
 catalysts=["Earnings Tue Nov 10 (estimated)", "CoreWeave Nov 9", "Live spot GPU pricing launched (Oct 21)"],
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
 catalysts=["Oracle AI World Oct 25–28 and investor day Oct 28 (this week)", "Earnings Wed Dec 9", "OpenAI funding news"],
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
 catalysts=["Earnings Tue Nov 3 before the open (election day)", "CoreWeave Nov 9 and Nebius Nov 10"],
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
 results="Q2 (Jul 30): revenue $1.22B, down 19% (third straight miss); net loss $359.5M; adjusted EBITDA $207.8M; subscription and services $555.1M.",
 guide="Q3: transaction revenue lower; subscription and services roughly flat; adjusted expenses $980M–1.08B. Q3 consensus EPS −$0.18.",
 capex="Light.",
 partners=["Citi institutional stablecoin payments (Sep 28)", "CFTC approval for derivatives clearing (Sep 29)", "Samsung Wallet USDC custody (Oct 8)", "Marqeta stablecoin cards (Oct 16)", "Open USD with Visa/Mastercard/Stripe"],
 catalysts=["⚠ Q3 earnings Thu Oct 29 after the close", "SEC tokenized-stock relief (it rose 12% on Sep 18)", "Clarity Act stalled in the Senate"],
 macro="Bitcoin price (around $81K), crypto trading volumes, rates (USDC interest income).",
 risks="Weak crypto activity; regulation; 55% off its high.",
 src=[("CNBC · Q2 report", "https://www.cnbc.com/2026/07/30/coinbase-coin-earnings-q2-2026.html"), ("Bloomberg · revenue falls third straight quarter", "https://www.bloomberg.com/news/articles/2026-07-30/coinbase-posts-loss-as-revenue-drops-for-third-straight-quarter"), ("Seeking Alpha · Citi partnership", SA+"4647563"), ("Seeking Alpha · CFTC clearing", SA+"4648080")])

S["CRCL"] = dict(
 name="Circle", what="Issuer of the USDC stablecoin; earns interest on reserves.",
 results="Q2 (Aug 5): EPS beat but revenue missed; USDC in circulation $73.3B (Jun 30); about 95% of revenue is reserve interest; reserve yield fell to 3.5%.",
 guide="2026 'other revenue' raised to $310–330M (about $180M is a one-time gain from the Arc token presale). Q3 consensus EPS $0.40.",
 capex="Acquisitions instead: Tazapay ($400M in stock).",
 partners=["Arc blockchain launched with Wall Street firms (Sep 16)", "Binance USDC promotion (Binance bought $100M of shares)", "Volante (banks)", "OKX investment", "Expansion into 40 markets"],
 catalysts=["Earnings Wed Nov 4 before the open", "Fed stablecoin reserve rules", "Coinbase Oct 29"],
 macro="Interest rates (a Fed hike raises reserve income); crypto activity; stablecoin legislation.",
 risks="Falling rates; slowing USDC growth (one analysis says share is down); the CFO is leaving.",
 src=[("Seeking Alpha · Q2 beat on EPS", SA+"4625754"), ("Seeking Alpha · other-revenue guide", SA+"4626342"), ("Bloomberg · revenue misses", "https://www.bloomberg.com/news/articles/2026-08-05/circle-revenue-misses-estimates-as-crypto-markets-mired-in-rout"), ("Seeking Alpha · Arc launch", SA+"4643335")])

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
 catalysts=["Earnings Thu Nov 5 (estimated)", "Confirmation of Anthropic terms", "CoreWeave Nov 9 and Nebius Nov 10"],
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
