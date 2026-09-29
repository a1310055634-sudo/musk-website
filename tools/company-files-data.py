# -*- coding: utf-8 -*-
"""公司档案数据 · 单一事实来源（V7-19 R8）

本模块是「公司档案体系」的唯一数据源：
- FILES：四份完整公司档案（Tesla / SpaceX / X / xAI），五段结构 =
  业务定位 · 关键里程碑 · 财务口径 · 风险与争议 · 相关事件与延伸阅读；
- BRIEFS：六份公司简介（Neuralink / Boring / SolarCity / Zip2 / PayPal / OpenAI），
  一句话定位 + 状态 + 在册资料入口。

纪律（每轮验收条件）：
- 全部事实取自站内在册口径（言行账本 / 编年史 / 财务全景 / 争议深读 / 一手文档馆），
  本轮零新增外部事实；每条里程碑、财务行、风险项都带站内锚点；
- 财务行必须标 kind（个人投入 / 融资 / IPO / 收入 / 估值 / 市值 / 收购对价 / 减记 / 薪酬），
  融资额、估值、收入、市值不得混写——估值一律标注「报道口径」（私有公司非公司披露）；
- 不把站内旧陈述自动当作当前事实：每份档案带 as_of 截止口径，
  财务与估值行各自带年份，站内未再更新的不冒充「最新」；
- 每份档案的「业务定位」是编者归纳，页面上显式标注，不与当事人原话混排。

消费方：tools/build-company-files.py（生成 company-files.html 第 34 页 +
companies-data.js 的 FILES_V7 数据出口，供 R9 时间轴 / R10 资本流向 / R15 检索复用）。
"""

# 财务行 kind → 双语标签（口径分类：金额不混用；估值/减记必标「报道口径」）
FIN_KINDS = {
    "founder_invest": {"zh": "个人投入", "en": "Founder capital"},
    "funding":        {"zh": "融资", "en": "Funding round"},
    "ipo":            {"zh": "IPO 募资", "en": "IPO proceeds"},
    "contract":       {"zh": "合同", "en": "Contract"},
    "revenue":        {"zh": "收入", "en": "Revenue"},
    "valuation":      {"zh": "估值 · 报道口径", "en": "Valuation · reported"},
    "marketcap":      {"zh": "市值", "en": "Market cap"},
    "acquisition":    {"zh": "收购对价", "en": "Acquisition price"},
    "merger":         {"zh": "并购对价", "en": "Merger price"},
    "writedown":      {"zh": "机构减记 · 报道口径", "en": "Writedown · reported"},
    "compensation":   {"zh": "薪酬激励", "en": "Compensation"},
    "exit":           {"zh": "退出", "en": "Exit"},
}

FILES = [
    # ================================================================ Tesla
    {
        "id": "tesla",
        "slug": "file-tesla",
        "name": "Tesla",
        "ticker": "NASDAQ: TSLA",
        "color_var": "--co-tesla",
        "as_of": {
            "zh": "截至 2025 年 11 月（站内在册最新口径）",
            "en": "As of Nov 2025 (latest account on file)",
        },
        "positioning": {
            "zh": "上市公司（NASDAQ: TSLA），电动车与能源业务。马斯克 2004 年以 A 轮领投入主、2008 年起任 CEO——把电动车从「政策合规品」做成人人想要的科技产品，2010 年 IPO，2021 年成为史上首家市值破万亿的车企。本档案截至口径：收入与交付数以站内在册的 2024 年报数据为最新，不冒充当前数字。",
            "en": "A listed EV & energy company (NASDAQ: TSLA). Musk led its Series A in 2004 and has been CEO since 2008 — turning EVs from compliance cars into objects of desire, taking it public in 2010, and making it the first carmaker to a $1T market cap in 2021. Latest financials on file: FY2024. Not presented as current.",
        },
        "milestones": [
            {"date": "2004", "text": {"zh": "A 轮融资 750 万美元，马斯克个人出资 650 万并出任董事长。", "en": "Series A of $7.5M — Musk personally put in $6.5M and became chairman."}, "href": "deep-dive-01.html"},
            {"date": "2008.12.24", "text": {"zh": "圣诞夜融资关闭——「可能的最后一天的最后一个小时」，公司免于破产。", "en": "Financing closed on Christmas Eve 2008 — “the last hour of the last day” — saving the company."}, "href": "primary.html#e2008-12-24"},
            {"date": "2010.06.29", "text": {"zh": "纳斯达克 IPO 募资约 2.26 亿美元——1956 年福特之后首家上市的美国车企。", "en": "IPO on Nasdaq raised ≈$226M — the first US carmaker listing since Ford in 1956."}, "href": "primary.html#e2010-06-29"},
            {"date": "2012.06.22", "text": {"zh": "Model S 首批交付——「打破魔咒：电动车可以比燃油车更好」。", "en": "First Model S deliveries — “breaking the spell: an EV can be better than a gas car.”"}, "href": "primary.html#e2012-06-22"},
            {"date": "2013.05.08", "text": {"zh": "Q1 2013 首次盈利——「十年历史中的第一次」；三周后 DOE 贷款 4.65 亿提前九年还清。", "en": "First-ever profitable quarter (Q1 2013); three weeks later the $465M DOE loan was repaid nine years early."}, "href": "primary.html#e2013-05-08"},
            {"date": "2016.11", "text": {"zh": "约 26 亿美元收购 SolarCity 获股东通过——关联交易当年受质疑，2022 年法院认定「entirely fair」。", "en": "Shareholders approved the ≈$2.6B SolarCity deal — a related-party buyout challenged then, ruled “entirely fair” in 2022."}, "href": "primary.html#e2016-11"},
            {"date": "2018.08.07", "text": {"zh": "「funding secured」推文 → SEC 起诉与和解（各罚 2000 万、卸任董事长）。", "en": "The “funding secured” tweet led to an SEC suit and settlement — $20M each and he gave up the chairman role."}, "href": "primary.html#e2018-08-07"},
            {"date": "2021", "text": {"zh": "市值突破 1 万亿美元——史上首家车企（Hertz 十万辆订单当日首破，一周后对冲推文一度蒸发约 400 亿）。", "en": "Market cap passed $1T — a first for a carmaker (on the Hertz order day; an hedging tweet erased ≈$40B within a week)."}, "href": "money.html"},
            {"date": "2023.01", "text": {"zh": "史上最大降价：全系 6%–20%，需求回路满量程运作。", "en": "The biggest price cuts ever: 6–20% across the line — the demand loop at full scale."}, "href": "pricing.html"},
            {"date": "2025.11.06", "text": {"zh": "股东大会约 75% 支持批准万亿美元级绩效薪酬——激励与市值目标互锁。", "en": "≈75% of shareholders approved the trillion-dollar performance package — pay locked to market-cap goals."}, "href": "primary.html#e2025-11-06"},
        ],
        "finances": [
            {"kind": "founder_invest", "date": "2004", "amount": "650 万美元", "amount_en": "$650K", "note": {"zh": "A 轮 750 万中的个人份额，并任董事长。", "en": "His personal share of the $7.5M Series A; he also chaired."}, "href": "deep-dive-01.html"},
            {"kind": "ipo", "date": "2010.06", "amount": "约 2.26 亿美元", "amount_en": "≈$226M", "note": {"zh": "IPO 募资额（财报/文件口径）。", "en": "IPO proceeds (filing-based figures)."}, "href": "primary.html#e2010-06-29"},
            {"kind": "marketcap", "date": "2021", "amount": "1 万亿美元", "amount_en": "$1T", "note": {"zh": "史上首家市值破万亿的车企。", "en": "First carmaker to a $1T market cap."}, "href": "money.html"},
            {"kind": "revenue", "date": "2023", "amount": "约 $96.8B", "amount_en": "≈$96.8B", "note": {"zh": "全年收入同比 +18.8%；交付约 181 万辆（Macrotrends/CNBC 口径）。", "en": "FY revenue +18.8%; ≈1.81M vehicles delivered (Macrotrends/CNBC)."}, "href": "finance.html#tesla"},
            {"kind": "revenue", "date": "2024", "amount": "约 $97.7B", "amount_en": "≈$97.7B", "note": {"zh": "全年收入同比 +0.95% 基本走平；交付约 179 万辆，经营现金流 $14.9B（10-K 口径）。站内在册最新年度数据。", "en": "FY revenue +0.95%, basically flat; ≈1.79M vehicles, $14.9B operating cash flow (10-K). Latest on file."}, "href": "finance.html#tesla"},
            {"kind": "compensation", "date": "2025.11", "amount": "万亿美元级", "amount_en": "trillion-dollar scale", "note": {"zh": "绩效薪酬包约 75% 股东通过——期权性质与市值目标互锁，非现金流支出。", "en": "Performance package approved by ≈75% — equity tied to market-cap goals, not a cash outlay."}, "href": "primary.html#e2025-11-06"},
        ],
        "risks": [
            {"title": {"zh": "SEC：funding secured 与后续", "en": "SEC: “funding secured” and its aftermath"}, "note": {"zh": "2018 年推文引发 SEC 起诉，和解各罚 2000 万、卸任董事长。", "en": "The 2018 tweet brought an SEC suit; the settlement fined $20M each and he left the chair."}, "href": "controversy.html#sec-sec"},
            {"title": {"zh": "Autopilot/FSD 安全争议", "en": "Autopilot/FSD safety controversy"}, "note": {"zh": "辅助驾驶的安全口径与监管审查是长期争议点。", "en": "Driver-assist safety claims and regulatory scrutiny remain a long-running controversy."}, "href": "controversy.html#autopilot"},
            {"title": {"zh": "工会与劳动争议", "en": "Labor and union disputes"}, "note": {"zh": "工会组织与劳动条件争议多次成为公开冲突。", "en": "Union drives and labor-condition disputes have repeatedly turned public."}, "href": "controversy.html#union"},
            {"title": {"zh": "降价换量的毛利承压（编者归纳）", "en": "Margin pressure from price cuts (editorial)"}, "note": {"zh": "编者分析：2024 年收入增长仅 0.95%，降价代价在年度报表显形——编者归纳，非公司表述。", "en": "Editorial: FY2024 revenue growth of just 0.95% showed the cost of cutting prices — an editorial reading, not company guidance."}, "href": "finance.html#tesla"},
        ],
        "related": [
            {"href": "deep-dive-01.html", "label": {"zh": "深读 · 资本运作", "en": "Deep dive: capital"}},
            {"href": "pricing.html", "label": {"zh": "定价与需求管理", "en": "Pricing & demand"}},
            {"href": "supplychain.html", "label": {"zh": "供应链与工厂哲学", "en": "Supply chain & factories"}},
            {"href": "chronicle.html#tesla", "label": {"zh": "编年史 · Tesla 全部 21 行", "en": "Chronicle: all 21 Tesla rows"}},
            {"href": "finance.html#tesla", "label": {"zh": "财务资本全景 · Tesla", "en": "Finance: Tesla"}},
        ],
        "image": {
            "src": "assets/tesla-factory.jpg", "w": 960, "h": 638,
            "alt": {"zh": "Tesla 弗里蒙特工厂总装线上的 Model S 车身", "en": "Model S bodies on the Fremont factory line"},
            "caption": {"zh": "图：Maurizio Pesce · CC BY 2.0 · Wikimedia Commons（2011，Fremont 总装线）", "en": "Photo: Maurizio Pesce · CC BY 2.0 · Wikimedia Commons (2011, Fremont line)"},
        },
    },
    # ================================================================ SpaceX
    {
        "id": "spacex",
        "slug": "file-spacex",
        "name": "SpaceX",
        "ticker": None,
        "color_var": "--co-spacex",
        "as_of": {
            "zh": "截至 2024 年 12 月（估值口径）；事件在册至 2024 年 10 月",
            "en": "Valuations as of Dec 2024; events on file through Oct 2024",
        },
        "positioning": {
            "zh": "未上市的私营航天公司，2002 年由马斯克以 PayPal 套现自投约 1 亿美元创立（创立故事细节未入册）。主线：可回收火箭把发射成本打下来——从三连败后第四发入轨，到整级复飞、塔式回收；如今既运宇航员，也筹划火星。本档案估值均标注「报道口径」（员工股转让/tender offer 报道，非公司披露）。",
            "en": "A private space company founded in 2002 with ≈$100M of Musk's own PayPal proceeds (founding-story details not on file). Reusability collapsed launch costs — from a fourth-launch orbit after three failures to full-stage reflying and tower catches; it now carries astronauts and plans for Mars. All valuations below are reported figures (tender offers), not company disclosures.",
        },
        "milestones": [
            {"date": "2002", "text": {"zh": "创立，自投约 1 亿美元——PayPal 套现的最大一笔再投入。", "en": "Founded with ≈$100M of his own money — the largest single reinvestment of his PayPal proceeds."}, "href": "primary.html#e2002-10-03"},
            {"date": "2008.09.28", "text": {"zh": "Falcon 1 第四次发射入轨——史上首枚入轨的私营液体燃料火箭；此前 Flight 3 失败后他说「I will never give up」。", "en": "Falcon 1 reached orbit on its fourth try — the first privately built liquid-fuel rocket to do so, after Flight 3's “I will never give up” moment."}, "href": "primary.html#e2008-09-28"},
            {"date": "2008.12.23", "text": {"zh": "NASA 16 亿美元 CRS 货运合同——与 Tesla 圣诞夜融资背靠背的两天。", "en": "NASA's $1.6B CRS cargo contract — back-to-back with Tesla's Christmas Eve financing."}, "href": "money.html"},
            {"date": "2012.05.25", "text": {"zh": "龙飞船首次对接国际空间站——首个与 ISS 对接的商业航天器。", "en": "Dragon became the first commercial spacecraft to dock with the ISS."}, "href": "primary.html#e2012-05-25"},
            {"date": "2015.12.21", "text": {"zh": "Falcon 9 一级首次陆上回收——「与史上任何火箭相比的根本性台阶变化」。", "en": "First land landing of a Falcon 9 first stage — “a fundamental step-change versus any rocket in history.”"}, "href": "primary.html#e2015-12-21"},
            {"date": "2017.03.30", "text": {"zh": "SES-10：首次整级复飞——复用从特技变成生意。", "en": "SES-10: first reflight of a full stage — reusability turned from stunt into business."}, "href": "primary.html#e2017-03-30"},
            {"date": "2018.02.06", "text": {"zh": "猎鹰重型首飞：双助推同步着陆 + 一辆 Roadster 入轨火星转移轨道。", "en": "Falcon Heavy's first flight: twin side-booster landings and a Roadster on a Mars-transfer orbit."}, "href": "primary.html#e2018-02-06"},
            {"date": "2020.05.30", "text": {"zh": "载人龙 Demo-2——商业公司首次送宇航员进入轨道。", "en": "Crew Dragon Demo-2 — a commercial company flew astronauts to orbit for the first time."}, "href": "primary.html#e2020-05-30"},
            {"date": "2024.10.13", "text": {"zh": "Starship 第五飞：「The tower has caught the rocket!!」——发射塔筷子回收。", "en": "Starship's fifth flight: “The tower has caught the rocket!!” — the chopstick catch."}, "href": "primary.html#e2024-10-13"},
        ],
        "finances": [
            {"kind": "founder_invest", "date": "2002", "amount": "约 1 亿美元", "amount_en": "≈$100M", "note": {"zh": "个人投入创立（PayPal 套现的最大一笔）。", "en": "Founder capital — the largest single chunk of his PayPal proceeds."}, "href": "primary.html#e2002-10-03"},
            {"kind": "contract", "date": "2008.12", "amount": "16 亿美元", "amount_en": "$1.6B", "note": {"zh": "NASA CRS 货运合同——至暗时刻的「救命现金流」。", "en": "NASA CRS contract — the life-saving cash line at the darkest hour."}, "href": "money.html"},
            {"kind": "funding", "date": "2015.01", "amount": "10 亿美元", "amount_en": "$1B", "note": {"zh": "Google + Fidelity 联合投资，持股 <10%（对应估值约 100 亿，账本在册）。", "en": "Google + Fidelity invested $1B for <10% (≈$10B implied, on file in the ledger)."}, "href": "primary.html#e2015-01-20"},
            {"kind": "valuation", "date": "2021.10", "amount": "约 $100.3B", "amount_en": "≈$100.3B", "note": {"zh": "股转 tender offer 后进入私人「千亿俱乐部」（CNBC 报道口径）。", "en": "Tender-offer valuation entering the private “$100B club” (CNBC-reported)."}, "href": "finance.html#spacex"},
            {"kind": "valuation", "date": "2024.12", "amount": "约 $350B", "amount_en": "≈$350B", "note": {"zh": "tender offer 协议估值（约合每股 185 美元，报道口径）。站内在册最新估值，非当前报价。", "en": "Tender-offer valuation (≈$185/share, reported). Latest on file — not a current quote."}, "href": "finance.html#spacex"},
        ],
        "risks": [
            {"title": {"zh": "早期三连败与第四发背水", "en": "Three early failures, one last chance"}, "note": {"zh": "2008 年 Flight 3 失败后资金与技术都到悬崖边，第四次发射前已预留 Flight 5 部件。", "en": "After Flight 3 (2008), money and hardware were both at the cliff edge; Flight 5 parts were already on hand."}, "href": "primary.html#e2008-08-02"},
            {"title": {"zh": "Amos-6 加注爆燃", "en": "Amos-6 pad explosion"}, "note": {"zh": "2016 年加注时爆燃，停飞逾四个月，2017 年 1 月复飞。", "en": "The 2016 pad explosion grounded the fleet for over four months; flights resumed in Jan 2017."}, "href": "primary.html#e2016-09-01"},
            {"title": {"zh": "Crew Dragon 静态点火爆燃", "en": "Crew Dragon static-fire explosion"}, "note": {"zh": "2019 年测试爆燃，SuperDraco 退出着陆用途——载人路线一度受挫。", "en": "The 2019 test explosion ended SuperDraco's landing role — a setback on the crewed path."}, "href": "primary.html#e2019-04-20"},
            {"title": {"zh": "估值依赖现金流叙事（编者归纳）", "en": "Valuation rests on the cash-flow story (editorial)"}, "note": {"zh": "编者分析：46B→350B 的七年十倍，「前提是现金流故事足够硬」——发射成本与星链订阅两个事实支撑。", "en": "Editorial: 46B→350B in seven years works only while the cash-flow story holds — launch costs and Starlink subscriptions."}, "href": "finance.html#spacex"},
        ],
        "related": [
            {"href": "deep-dive-03.html", "label": {"zh": "深读 · 失败模式（星舰塔捕）", "en": "Deep dive: failure (the tower catch)"}},
            {"href": "supplychain.html", "label": {"zh": "供应链与工厂哲学", "en": "Supply chain & factories"}},
            {"href": "chronicle.html#spacex", "label": {"zh": "编年史 · SpaceX 全部 15 行", "en": "Chronicle: all 15 SpaceX rows"}},
            {"href": "finance.html#spacex", "label": {"zh": "财务资本全景 · SpaceX", "en": "Finance: SpaceX"}},
            {"href": "capital-evolution.html", "label": {"zh": "资本演化与流向图", "en": "Capital evolution & flows"}},
        ],
        "image": {
            "src": "assets/starship-catch.jpg", "w": 1200, "h": 1345,
            "alt": {"zh": "Starship 超重型助推器被发射塔机械臂接住（2024 年 10 月第五飞）", "en": "The Super Heavy booster caught by the launch tower arms (fifth flight, Oct 2024)"},
            "caption": {"zh": "图：Steve Jurvetson · CC BY 2.0 · Wikimedia Commons（2024-10-13 塔捕）", "en": "Photo: Steve Jurvetson · CC BY 2.0 · Wikimedia Commons (the tower catch, 2024-10-13)"},
        },
    },
    # ================================================================ X
    {
        "id": "x",
        "slug": "file-x",
        "name": "X（原 Twitter）",
        "name_en": "X (formerly Twitter)",
        "ticker": None,
        "color_var": "--co-x",
        "as_of": {
            "zh": "截至 2025 年 3 月（并入 xAI）",
            "en": "As of Mar 2025 (absorbed into xAI)",
        },
        "positioning": {
            "zh": "2022 年以 440 亿美元（每股 54.20）收购的社交平台，2023 年 7 月更名 X，2025 年 3 月并入 xAI 后不再是独立公司。它既是他的扩音器，也是「言论广场实验」的现场；并入后平台的价值被重新定价为「模型公司的数据与分发底座」。",
            "en": "The social platform bought for $44B ($54.20/share) in 2022, renamed X in July 2023, and absorbed into xAI in March 2025 — no longer a standalone company. It was both his loudspeaker and his free-speech experiment; post-merger it is repriced as “the data and distribution layer of a model company.”",
        },
        "milestones": [
            {"date": "2022.04.14", "text": {"zh": "发出收购要约：「I will acquire Twitter for $54.20 a share」——420 大麻梗写进正式文书。", "en": "His offer: “I will acquire Twitter for $54.20 a share” — the 420 joke entered a formal filing."}, "href": "primary.html#e2022-04-14"},
            {"date": "2022.04.25", "text": {"zh": "与董事会签署 Merger Agreement：十亿美元终止费、第 9.9 条特定履约。", "en": "Merger agreement signed: a $1B termination fee and specific-performance clause 9.9."}, "href": "documents.html#d2022-04-25"},
            {"date": "2022.07–10", "text": {"zh": "反悔、被诉、反诉——Twitter 援引第 9.9 条在特拉华州法院要求强制履约；10 月初重启收购意向。", "en": "He tried to walk away, got sued, countersued; Twitter invoked 9.9 in Delaware — he revived the deal in early October."}, "href": "stories.html"},
            {"date": "2022.10.27", "text": {"zh": "在终止日前夜完成交割——440 亿美元，公司私有化；次日「the bird is freed」，解散董事会、自任 CEO。", "en": "The deal closed the night before the deadline — $44B, private again; next day “the bird is freed,” board dissolved, he became CEO."}, "href": "primary.html#e2022-10-28"},
            {"date": "2022.11.16", "text": {"zh": "「Extremely Hardcore」全员通牒：点 yes 留下，否则视为辞职；数百人离开。", "en": "The “Extremely Hardcore” ultimatum: click yes or be treated as resigned; hundreds left."}, "href": "primary.html#e2022-11-16"},
            {"date": "2023.07.23", "text": {"zh": "品牌更替——「bid adieu to the twitter brand」，鸟标退役、X.com 上线。", "en": "Rebrand: “bid adieu to the twitter brand” — the bird retired, X.com went live."}, "href": "primary.html#e2023-07-23"},
            {"date": "2023.11", "text": {"zh": "广告主因内容争议暂停投放；他在 DealBook 会上回应「别想勒索我用广告费」。", "en": "Advertisers paused over content disputes; at DealBook he answered “don't try to blackmail me with advertising.”"}, "href": "primary.html#e2023-11-29"},
            {"date": "2025.03.28", "text": {"zh": "xAI 全股票收购 X——平台并入模型公司，X 作为独立公司时代结束。", "en": "xAI bought X in an all-stock deal — the platform merged into the model company, ending standalone X."}, "href": "primary.html#e2025-03-28"},
        ],
        "finances": [
            {"kind": "acquisition", "date": "2022.10", "amount": "440 亿美元", "amount_en": "$44B", "note": {"zh": "每股 54.20 美元要约交割；同期背上约 130 亿美元银行债务（协议条款在册）。", "en": "Closed at $54.20/share; ≈$13B of bank debt came with it (clause excerpts on file)."}, "href": "documents.html#d2022-04-25"},
            {"kind": "revenue", "date": "2022–2024", "amount": "$5.2B → $3.4B → $2.5B", "note": {"zh": "收入曲线（Fortune/Axios/Entrepreneur 报道口径）：2023 年 -35%，广告主流失是主因。", "en": "Revenue path (Fortune/Axios/Entrepreneur-reported): -35% in 2023 as advertisers left."}, "href": "finance.html#x"},
            {"kind": "writedown", "date": "2023–2024", "amount": "-72% → -80%", "note": {"zh": "Fidelity 对持仓连续减记（2023-12 隐含约 $19B，2024-10 隐含约 $9.4B）；马斯克本人有异议（USA Today/Fortune 口径）。", "en": "Fidelity repeatedly marked down its stake (implied ≈$19B in Dec 2023, ≈$9.4B in Oct 2024); Musk disputed the marks (USA Today/Fortune)."}, "href": "finance.html#x"},
            {"kind": "merger", "date": "2025.03", "amount": "约 $33B", "amount_en": "≈$33B", "note": {"zh": "并入 xAI 的全股票对价（含债务约 $45B）——从机构减记价到并购对价，一年内反转。", "en": "The all-stock merger price (≈$45B with debt) — from writedown marks to deal price within a year."}, "href": "primary.html#e2025-03-28"},
        ],
        "risks": [
            {"title": {"zh": "内容审核与言论边界争议", "en": "Content moderation and speech controversies"}, "note": {"zh": "收购后的审核政策变化与广告主撤离是持续争议主线。", "en": "Post-acquisition moderation changes and advertiser walkouts form the main controversy line."}, "href": "controversy.html#twitter"},
            {"title": {"zh": "广告业务萎缩（编者归纳）", "en": "Shrinking advertising (editorial)"}, "note": {"zh": "编者归纳：收入曲线 2022→2024 三连降，广告主流失为主因——依据站内在册报道口径整理。", "en": "Editorial: three straight revenue declines 2022→2024, driven by advertiser exits — from on-file reporting."}, "href": "finance.html#x"},
            {"title": {"zh": "机构减记与本人异议", "en": "Institutional writedowns, disputed by Musk"}, "note": {"zh": "Fidelity 系列减记是市场口径的锚；本人公开不认可——两种口径并存呈示。", "en": "Fidelity's marks anchor the market view; he publicly disagreed — both accounts are shown."}, "href": "finance.html#x"},
        ],
        "related": [
            {"href": "stories.html", "label": {"zh": "经典商战 · 收购 Twitter 交互时间轴", "en": "War stories: the Twitter takeover timeline"}},
            {"href": "grok.html", "label": {"zh": "xAI·Grok 档案（并入后的归属页）", "en": "The xAI & Grok file (its post-merger home)"}},
            {"href": "ai-strategy.html", "label": {"zh": "AI 战略全景", "en": "AI strategy landscape"}},
            {"href": "chronicle.html#x", "label": {"zh": "编年史 · X 部", "en": "Chronicle: the X chapter"}},
            {"href": "controversy.html#twitter", "label": {"zh": "争议深读 · Twitter 内容审核", "en": "Controversy: content moderation"}},
        ],
        "image": {
            "src": "assets/x-hq.jpg", "w": 1200, "h": 800,
            "alt": {"zh": "旧金山市场街 Twitter 总部，2022 年 11 月收购完成时仍挂 @twitter 标牌", "en": "The Market St. HQ still wearing @twitter signage, Nov 2022"},
            "caption": {"zh": "图：osunpokeh · CC BY-SA 4.0 · Wikimedia Commons（2022-11）", "en": "Photo: osunpokeh · CC BY-SA 4.0 · Wikimedia Commons (Nov 2022)"},
        },
    },
    # ================================================================ xAI
    {
        "id": "xai",
        "slug": "file-xai",
        "name": "xAI",
        "ticker": None,
        "color_var": "--co-xai",
        "as_of": {
            "zh": "截至 2026 年 1 月（Series E 公告口径）",
            "en": "As of Jan 2026 (Series E announcement)",
        },
        "positioning": {
            "zh": "2023 年 7 月创立的 AI 公司（使命宣言：「To understand the true nature of the universe.」），Grok 模型之父。2025 年 3 月全股票收购 X，把「数据 → 模型 → 分发」回路闭合；2026 年 1 月完成 200 亿美元 Series E（投后估值约 2300 亿量级）。晚到者用资本速度追位置——B 轮到 E 轮只用 20 个月。",
            "en": "An AI company founded in July 2023 (mission: “To understand the true nature of the universe.”), maker of Grok. It bought X in an all-stock deal in March 2025, closing the data→model→distribution loop; in January 2026 it raised a $20B Series E (≈$230B post-money). A latecomer buying position with capital speed — Series B to E in 20 months.",
        },
        "milestones": [
            {"date": "2023.07.12", "text": {"zh": "成立宣言：「To understand the true nature of the universe.」", "en": "The founding statement: “To understand the true nature of the universe.”"}, "href": "primary.html#e2023-07-12"},
            {"date": "2023.11.04", "text": {"zh": "Grok 首发公告：早期测试后向 X Premium+ 订阅用户开放。", "en": "Grok announced: open to X Premium+ subscribers after early testing."}, "href": "x-posts.html#p2023-11-04"},
            {"date": "2024.03", "text": {"zh": "Grok-1 开源——模型权重公开（宣言兑现注脚在册）。", "en": "Grok-1 open-sourced — model weights released (the manifesto footnote on file)."}, "href": "documents.html#d2023-07-12"},
            {"date": "2025.03.28", "text": {"zh": "全股票收购 X：xAI 约 800 亿 / X 约 330 亿（含债约 450 亿）——本人推文逐字在册。", "en": "All-stock purchase of X: xAI ≈$80B / X ≈$33B (≈$45B with debt) — his own post on file, verbatim."}, "href": "primary.html#e2025-03-28"},
            {"date": "2025.07", "text": {"zh": "Grok 4 发布（xAI·Grok 档案在册节点）。", "en": "Grok 4 released (node on file in the xAI & Grok archive)."}, "href": "grok.html"},
            {"date": "2026.01", "text": {"zh": "Series E 完成：200 亿美元 @ 投后约 2300 亿——超 150 亿目标，Valor 领投、英伟达与思科参投。", "en": "Series E closed: $20B at ≈$230B post-money — above the $15B target, led by Valor with Nvidia and Cisco aboard."}, "href": "documents.html#d2026-01"},
        ],
        "finances": [
            {"kind": "funding", "date": "2024.05", "amount": "60 亿美元（B 轮）", "amount_en": "$6B (Series B)", "note": {"zh": "投后约 240 亿（pre-money 180 亿；Reuters/CNBC/Forbes 报道口径）。", "en": "≈$24B post-money ($18B pre; Reuters/CNBC/Forbes-reported)."}, "href": "finance.html#xai"},
            {"kind": "funding", "date": "2024.12", "amount": "60 亿美元（C 轮）", "amount_en": "$6B (Series C)", "note": {"zh": "估值约 400 亿（x.ai 官方公告口径）。", "en": "≈$40B valuation (x.ai's own announcement)."}, "href": "finance.html#xai"},
            {"kind": "funding", "date": "2025 秋", "amount": "股权 100 亿 + 债务 120 亿", "amount_en": "$10B equity + $12B debt", "note": {"zh": "Series E 公告原文自述口径。", "en": "As stated in the Series E announcement itself."}, "href": "documents.html#d2026-01"},
            {"kind": "funding", "date": "2026.01", "amount": "200 亿美元（E 轮）", "amount_en": "$20B (Series E)", "note": {"zh": "投后约 2300 亿量级，超募 33%；Valor 领投、英伟达与思科参投（公告全文在册）。", "en": "≈$230B post-money, 33% oversubscribed; led by Valor with Nvidia and Cisco (announcement on file)."}, "href": "documents.html#d2026-01"},
        ],
        "risks": [
            {"title": {"zh": "资本速度依赖（编者归纳）", "en": "Dependence on capital speed (editorial)"}, "note": {"zh": "编者分析：B→E 二十个月估值十倍——「AI 行业见过最陡的资本曲线」，速度本身是叙事的一部分（编者归纳，非公告文字）。", "en": "Editorial: 10× valuation in 20 months — the steepest curve AI has seen; the speed is itself part of the story (editorial, not from the announcement)."}, "href": "finance.html#xai"},
            {"title": {"zh": "与 OpenAI 的竞争（编者关联）", "en": "Rivalry with OpenAI (editorial)"}, "note": {"zh": "「数年后成为 xAI 最受关注的对手」为编者归纳——非任何一方官方表述（关系总览已标 editorial）。", "en": "“xAI's most watched rival” is an editorial framing — not an official characterization by either side (marked editorial in the network view)."}, "href": "companies.html#network"},
        ],
        "related": [
            {"href": "grok.html", "label": {"zh": "xAI·Grok 主档案页", "en": "The main xAI & Grok file"}},
            {"href": "ai-strategy.html", "label": {"zh": "AI 战略全景", "en": "AI strategy landscape"}},
            {"href": "deep-dive-05.html", "label": {"zh": "深读 · AI 战略", "en": "Deep dive: AI strategy"}},
            {"href": "documents.html#d2026-01", "label": {"zh": "一手文档 · Series E 公告全文", "en": "Primary source: the Series E announcement"}},
            {"href": "finance.html#xai", "label": {"zh": "财务资本全景 · xAI", "en": "Finance: xAI"}},
        ],
        "image": None,
    },
]

# ---------------------------------------------------------------- 简介六家
BRIEFS = [
    {
        "id": "neuralink",
        "slug": "brief-neuralink",
        "name": "Neuralink",
        "color_var": "--co-neuralink",
        "era": {"zh": "2016 年创立 · 在营", "en": "Founded 2016 · operating"},
        "text": {
            "zh": "脑机接口公司。2024 年 1 月完成首例人体植入——第一款产品 Telepathy，让瘫痪患者用意念控制手机与电脑；长期故事是「人机共生」。",
            "en": "Brain–computer interfaces. First human implant in Jan 2024 — Telepathy lets paralyzed patients control phones and computers by thought; the long game is human–machine symbiosis.",
        },
        "links": [
            {"href": "primary.html#e2024-01-29", "label": {"zh": "账本 · Telepathy 首例植入官宣", "en": "Ledger: the Telepathy implant announcement"}},
            {"href": "companies.html", "label": {"zh": "公司版图 · 档案卡", "en": "Companies: the profile card"}},
        ],
    },
    {
        "id": "boring",
        "slug": "brief-boring",
        "name": "The Boring Company",
        "color_var": "--co-boring",
        "era": {"zh": "2016 年创立 · 在营", "en": "Founded 2016 · operating"},
        "text": {
            "zh": "隧道交通公司，起因是一句堵车抱怨。首条测试隧道靠 500 美元一把的「Not-a-Flamethrower」周边融资；2018 年底首条隧道通车，此后经营拉斯维加斯 Loop。",
            "en": "Tunneling, born from one traffic complaint. The first test tunnel was funded by $500 “Not-a-Flamethrower” merch; the first tunnel opened in late 2018, and the Vegas Loop runs today.",
        },
        "links": [
            {"href": "primary.html#e2018-12-18", "label": {"zh": "账本 · 首条隧道通车", "en": "Ledger: the first tunnel opening"}},
            {"href": "primary.html#e2025", "label": {"zh": "账本 · Vegas Loop 项目页（2025）", "en": "Ledger: the Vegas Loop project page (2025)"}},
        ],
    },
    {
        "id": "solarcity",
        "slug": "brief-solarcity",
        "name": "SolarCity",
        "color_var": "--co-solarcity",
        "era": {"zh": "2006 年创立 · 2016 年并入 Tesla", "en": "Founded 2006 · absorbed into Tesla 2016"},
        "text": {
            "zh": "表兄弟按他的创意创立、他出任董事长的太阳能公司。2016 年 Tesla 以约 26 亿美元收购（关联交易当年受质疑），2022 年特拉华最高法院认定「entirely fair」。",
            "en": "A solar company his cousins founded on his idea, with him as chairman. Tesla bought it for ≈$2.6B in 2016 (a related-party deal challenged then); Delaware's top court ruled it “entirely fair” in 2022.",
        },
        "links": [
            {"href": "events.html#e2006", "label": {"zh": "事件档案 · SolarCity 创立", "en": "Event file: founding SolarCity"}},
            {"href": "primary.html#e2022-07-13", "label": {"zh": "账本 · 2022 判决胜诉", "en": "Ledger: the 2022 ruling"}},
        ],
    },
    {
        "id": "zip2",
        "slug": "brief-zip2",
        "name": "Zip2",
        "color_var": "--co-history",
        "era": {"zh": "1995 年创立 · 1999 年退出", "en": "1995 · exited 1999"},
        "text": {
            "zh": "给报纸做的网上城市指南——第一家公司。1999 年康柏以约 3.07 亿美元买下，个人套现约 2200 万美元：第一桶金。",
            "en": "An online city guide for newspapers — his first company. Compaq paid ≈$307M in 1999; his share was ≈$22M: the first fortune.",
        },
        "links": [
            {"href": "profile.html", "label": {"zh": "速览 · 早期两役", "en": "Profile: the early two campaigns"}},
            {"href": "money.html", "label": {"zh": "资本解剖 · 第一桶金", "en": "Capital: the first fortune"}},
        ],
    },
    {
        "id": "paypal",
        "slug": "brief-paypal",
        "name": "X.com / PayPal",
        "color_var": "--co-paypal",
        "era": {"zh": "1999 年创立 · 2002 年退出", "en": "1999 · exited 2002"},
        "text": {
            "zh": "他 1999 年创办的网上银行 X.com 长成了 PayPal；2002 年 eBay 以 15 亿美元收购，税后约 1.8 亿美元全部再投入 SpaceX、Tesla 与 SolarCity。",
            "en": "His 1999 online bank X.com grew into PayPal; eBay paid $1.5B in 2002 — and the ≈$180M after tax went straight into SpaceX, Tesla and SolarCity.",
        },
        "links": [
            {"href": "primary.html#e2002-10-03", "label": {"zh": "账本 · PayPal 交割与资金分配", "en": "Ledger: the PayPal closing and the splits"}},
            {"href": "events.html#e2002-10-03", "label": {"zh": "事件档案 · 交割日", "en": "Event file: closing day"}},
        ],
    },
    {
        "id": "openai",
        "slug": "brief-openai",
        "name": "OpenAI",
        "color_var": "--co-history",
        "era": {"zh": "2015 年联合创立 · 2018 年退出董事会", "en": "Co-founded 2015 · left board 2018"},
        "text": {
            "zh": "2015 年的联合创始人，2018 年退出董事会——数年后成为 xAI 最受关注的对手（编者归纳，非当事方表述）。",
            "en": "A 2015 co-founder who left the board in 2018 — years later, xAI's most watched rival (editorial framing, not either party's words).",
        },
        "links": [
            {"href": "companies.html#network", "label": {"zh": "关系总览 · OpenAI—xAI 编者关联", "en": "Network: the OpenAI—xAI editorial link"}},
            {"href": "ai-strategy.html", "label": {"zh": "AI 战略全景", "en": "AI strategy landscape"}},
        ],
    },
]


def validate():
    """结构自检：档案 id 必须在公司节点表 / 字段双语完整 / 财务 kind 枚举 /
    每条里程碑与风险带站内锚点 / slug 唯一 / BRIEFS 必须带资料入口。"""
    import os
    import importlib.util
    errs = []
    cd_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "companies-data.py")
    spec = importlib.util.spec_from_file_location("companies_data_check", cd_path)
    cd = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cd)
    company_ids = {c["id"] for c in cd.COMPANIES}

    slugs = set()
    for f in FILES:
        fid = f["id"]
        if fid not in company_ids:
            errs.append(f"{fid}: 不在 companies-data.py 节点表")
        if f["slug"] in slugs:
            errs.append(f"重复 slug: {f['slug']}")
        slugs.add(f["slug"])
        if not f["as_of"].get("zh") or not f["as_of"].get("en"):
            errs.append(f"{fid}: as_of 缺中/英文（截止口径必填）")
        if not f["positioning"].get("zh") or not f["positioning"].get("en"):
            errs.append(f"{fid}: positioning 缺中/英文")
        if not f["milestones"]:
            errs.append(f"{fid}: 无里程碑")
        for m in f["milestones"]:
            if not m.get("date"):
                errs.append(f"{fid}: 里程碑缺日期")
            if not m.get("text", {}).get("zh") or not m["text"].get("en"):
                errs.append(f"{fid}: 里程碑文本缺中/英文")
            if not m.get("href"):
                errs.append(f"{fid}: 里程碑缺站内锚点（{m.get('date')}）")
        if not f["finances"]:
            errs.append(f"{fid}: 无财务行")
        for fn in f["finances"]:
            if fn["kind"] not in FIN_KINDS:
                errs.append(f"{fid}: 未知财务口径 {fn['kind']}")
            if not fn.get("date") or not fn.get("amount"):
                errs.append(f"{fid}: 财务行缺日期或金额（{fn.get('kind')}）")
            if not fn.get("note", {}).get("zh") or not fn["note"].get("en"):
                errs.append(f"{fid}: 财务行说明缺中/英文（{fn.get('kind')} {fn.get('date')}）")
            if not fn.get("href"):
                errs.append(f"{fid}: 财务行缺站内锚点（{fn.get('kind')} {fn.get('date')}）")
        if not f["risks"]:
            errs.append(f"{fid}: 无风险项")
        for r in f["risks"]:
            if not r.get("title", {}).get("zh") or not r["title"].get("en"):
                errs.append(f"{fid}: 风险标题缺中/英文")
            if not r.get("href"):
                errs.append(f"{fid}: 风险项缺站内锚点（{r.get('title', {}).get('zh')}）")
        if not f["related"]:
            errs.append(f"{fid}: 无延伸阅读")
        for r in f["related"]:
            if not r.get("href") or not r.get("label", {}).get("zh"):
                errs.append(f"{fid}: 延伸阅读缺链接或标签")
        im = f.get("image")
        if im:
            for k in ("src", "w", "h", "alt", "caption"):
                if not im.get(k):
                    errs.append(f"{fid}: image 缺 {k}")

    for b in BRIEFS:
        bid = b["id"]
        if bid not in company_ids:
            errs.append(f"brief {bid}: 不在 companies-data.py 节点表")
        if b["slug"] in slugs:
            errs.append(f"重复 slug: {b['slug']}")
        slugs.add(b["slug"])
        if not b.get("text", {}).get("zh") or not b["text"].get("en"):
            errs.append(f"brief {bid}: 文本缺中/英文")
        if not b.get("era", {}).get("zh"):
            errs.append(f"brief {bid}: 缺年代状态行")
        if not b.get("links"):
            errs.append(f"brief {bid}: 至少要有一个在册资料入口")
    return errs


if __name__ == "__main__":
    problems = validate()
    if problems:
        for p in problems:
            print("✗", p)
        raise SystemExit(1)
    n_ms = sum(len(f["milestones"]) for f in FILES)
    n_fin = sum(len(f["finances"]) for f in FILES)
    n_rk = sum(len(f["risks"]) for f in FILES)
    print(f"✓ company-files-data: {len(FILES)} 档案（{n_ms} 里程碑 · {n_fin} 财务行 · {n_rk} 风险项）+ {len(BRIEFS)} 简介 · 自检通过")
