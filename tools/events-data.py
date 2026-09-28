# -*- coding: utf-8 -*-
"""事件档案 · 单一事实来源（V7-19 R6）

本模块是「事件与来源结构」的唯一数据源：一个事件 = 一条事实本体记录，
描述它的多份材料（账本条目 / 一手文档 / X 帖 / 访谈 / 站内专题 / 外部来源）分开列示。

纪律：
- 所有事实与引语取自已核实的言行账本（primary.html）条目，不新增未核实事实；
- quotes 仅收录有对应原文的逐字引语；无逐字原话的事件用 no_quote_note 说明；
- date + precision 显式声明精度（day/month/year），不作超出材料的日期断言；
- 编者归纳（facts 中标注 editorial 的条目）不得伪装成当事人原话或外部事实。

消费方：tools/build-events.py（生成 events.html 静态页 + events-data.js 本地 JS 数据，
供 R7 公司关系 / R9 时间轴 / R15 检索复用）。

口径说明：本页迁移的是「代表性事件」，不等于账本全集（67 条）；
账本、材料、事件、页面数量分别统计，见页头元信息行。
"""

# 材料类型 → 双语标签（材料是描述事件的记录，事件是事实本体，二者分开）
KIND_LABELS = {
    "ledger":    {"zh": "账本条目", "en": "Ledger entry"},
    "document":  {"zh": "一手文档", "en": "Document"},
    "post":      {"zh": "X 帖", "en": "X post"},
    "interview": {"zh": "访谈", "en": "Interview"},
    "feature":   {"zh": "站内专题", "en": "Feature"},
    "image":     {"zh": "纪实图片", "en": "Photo"},
    "external":  {"zh": "外部来源", "en": "External source"},
}

# 日期精度 → 双语徽标
PRECISION_LABELS = {
    "day":   {"zh": "精确到日", "en": "Day precision"},
    "month": {"zh": "精确到月", "en": "Month precision"},
    "year":  {"zh": "仅年份", "en": "Year only"},
}

EVENTS = [
    # ------------------------------------------------ 2002.10.03 PayPal 交割
    {
        "id": "e2002-10-03",
        "date": "2002.10.03",
        "precision": "day",
        "companies": ["PayPal", "Tesla", "SpaceX", "SolarCity"],
        "title": {"zh": "PayPal 交割——1.8 亿美元的去向",
                  "en": "PayPal closes — where $180M went next"},
        "summary": {
            "zh": "eBay 以 15 亿美元完成收购；31 岁的马斯克税后到手约 1.8 亿美元——足够此生不再工作。钱的去向，是本站其余一切故事的起点。",
            "en": "eBay closes its $1.5B acquisition; at 31, Musk nets about $180M after tax — enough to never work again. Where the money went next is where the rest of this site begins.",
        },
        "background": {
            "zh": "2002 年 10 月 3 日，eBay 完成 15 亿美元收购 PayPal。31 岁的马斯克税后到手约 1.8 亿美元——足够此生不再工作。接下来的决定是钱去哪，而这个决定是本站其余一切故事的起点。",
            "en": "On October 3, 2002, eBay closed its $1.5 billion acquisition of PayPal. Musk, 31, walked away with roughly $180 million after tax — enough to never work again. The next decision was where the money would go, and it is the founding decision of everything else on this site.",
        },
        "facts": [
            {"zh": "eBay 于 2002.10.03 完成 15 亿美元收购 PayPal 的交割。",
             "en": "On 2002-10-03, eBay closed its $1.5B acquisition of PayPal."},
            {"zh": "税后所得约 1.8 亿美元——口径为其本人 2012–2013 年访谈自述。",
             "en": "About $180M after tax — per his own 2012–13 interview account."},
            {"zh": "分配去向：约 1 亿美元投 SpaceX、7,000 万投 Tesla、1,000 万投 SolarCity，全部是本人控制的公司。",
             "en": "The split: roughly $100M into SpaceX, $70M into Tesla, $10M into SolarCity — all companies he controlled."},
            {"zh": "此后数年，他在多个公开访谈中自述靠向朋友借钱付房租。",
             "en": "For years afterwards he said in interviews that he was borrowing rent money from friends."},
        ],
        "quotes": [
            {"en": "My proceeds from PayPal after tax were about $180M. $100M of that went into SpaceX, $70M into Tesla, and $10M into SolarCity. I had to borrow money for rent.",
             "zh": "我 PayPal 的税后所得大约 1.8 亿美元。其中 1 亿投进了 SpaceX，7000 万投进 Tesla，1000 万投进 SolarCity。然后我不得不借钱付房租。",
             "source": {"zh": "本人自述 · 2012–2013 访谈（USA Today《Innovators and Icons》等）",
                        "en": "In his own words · 2012–13 interviews (USA Today's Innovators and Icons etc.)"}},
        ],
        "no_quote_note": None,
        "outcome": {
            "zh": "三家公司全部成活：SpaceX 2008 年拿下 NASA 16 亿美元合同，Tesla 2010 年上市，SolarCity 2012 年上市。这笔分配就是本站「退出即入场」模式的源头——他把个人退出直接变成三家公司的启动资本，现金清零，换来三张牌桌上的三个座位。（末句为编者分析，非其原话。）",
            "en": "All three survived: SpaceX landed NASA's $1.6B contract in 2008, Tesla IPO'd in 2010, SolarCity went public in 2012. That allocation is the origin of this site's “exit as entry” pattern — he converted a personal exit into founding capital for three companies, zeroing his own cash to buy three seats at three tables. (The last sentence is editorial analysis, not his words.)",
        },
        "materials": [
            {"kind": "ledger", "href": "primary.html#e2002-10-03", "date": "2002.10.03",
             "label": {"zh": "言行账本 e2002-10-03 · PayPal 交割", "en": "Ledger e2002-10-03 · PayPal closes"},
             "note": {"zh": "一手言行记录：背景 / 原话 / 现场 / 后续四段全文", "en": "First-hand record: background / words / scene / aftermath"}},
            {"kind": "feature", "href": "deep-dive-01.html", "date": None,
             "label": {"zh": "深读·资本运作——「退出即入场」主线", "en": "Deep dive: Capital — the “exit as entry” thread"},
             "note": {"zh": "该模式在资本主线中的完整展开", "en": "The pattern traced through the capital thread"}},
            {"kind": "external", "href": None, "date": "2012–2013",
             "label": {"zh": "USA Today《Innovators and Icons》系列访谈 · 本人自述口径", "en": "USA Today, Innovators and Icons series · his own account"},
             "note": {"zh": "引语与分配数字的直接出处（口径）", "en": "Direct source of the quote and the split figures"}},
        ],
        "image": None,
        "related": [
            {"href": "#e2006", "label": {"zh": "2006 · SolarCity 创立", "en": "2006 · SolarCity founded"}},
            {"href": "#e2008-12-24", "label": {"zh": "2008.12.24 · 圣诞夜融资", "en": "2008-12-24 · Christmas Eve financing"}},
        ],
    },
    # ------------------------------------------------ 2006 SolarCity 创立
    {
        "id": "e2006",
        "date": "2006",
        "precision": "year",
        "companies": ["SolarCity", "Tesla"],
        "title": {"zh": "SolarCity 创立——PayPal 套现资助的第三家公司",
                  "en": "SolarCity founded — the third PayPal-funded bet"},
        "summary": {
            "zh": "表兄弟按他的创意创立 SolarCity，他出任董事长——第三笔押注落子能源。",
            "en": "His cousins founded SolarCity on his idea, with Musk as chairman — the third bet, this time on energy.",
        },
        "background": {
            "zh": "Tesla 在造电动车，但马斯克的能源命题需要第二条腿：太阳能发电。2006 年，他的表兄弟 Lyndon 与 Peter Rive 按他的创意创立 SolarCity，他出任董事长——这是 PayPal 套现资助的第三家公司。",
            "en": "Tesla was building an electric car, but Musk's energy thesis needed a second leg: solar generation. In 2006, his cousins Lyndon and Peter Rive founded SolarCity on his idea, with Musk as chairman — the third company funded by the PayPal proceeds.",
        },
        "facts": [
            {"zh": "仅年份口径（2006 年）：Lyndon 与 Peter Rive 创立 SolarCity，创意来自马斯克。",
             "en": "Year-only precision (2006): Lyndon and Peter Rive found SolarCity on Musk's idea."},
            {"zh": "马斯克出任董事长，不负责日常经营。",
             "en": "Musk serves as chairman; day-to-day operations stay with the founders."},
            {"zh": "模式是金融而非制造：太阳能系统零首付租赁给房主；公司后成为美国最大户用光伏安装商。",
             "en": "Financing, not manufacturing: zero-down solar leases; the company grows into the largest US residential solar installer."},
        ],
        "quotes": [],
        "no_quote_note": {
            "zh": "账本本条无逐字原话记录——以公司口径与公开资料建档，不作引语包装。",
            "en": "No verbatim quote on record for this entry — filed from company statements and public sources, without quote dressing.",
        },
        "outcome": {
            "zh": "2016 年，Tesla 以约 26 亿美元股票收购 SolarCity——2006 年蓝图里的能源板块并回，成为今天储能业务的起点；关联交易结构则引发多年股东诉讼。（末句为编者分析，非其原话。）",
            "en": "In 2016 Tesla acquired SolarCity for about $2.6 billion in stock — the energy half of the 2006 master plan folding back in, the starting point of today's storage business; the related-party structure drew shareholder litigation for years. (The last sentence is editorial analysis, not his words.)",
        },
        "materials": [
            {"kind": "ledger", "href": "primary.html#e2006", "date": "2006",
             "label": {"zh": "言行账本 e2006 · SolarCity 创立", "en": "Ledger e2006 · SolarCity founded"},
             "note": {"zh": "一手言行记录（无逐字引语段）", "en": "First-hand record (no verbatim quote section)"}},
            {"kind": "document", "href": "documents.html#d2006-08", "date": "2006.08",
             "label": {"zh": "《The Secret Tesla Motors Master Plan》· 同年 · 能源命题的原始出处", "en": "The Secret Tesla Motors Master Plan · same year · the origin of the energy thesis"},
             "note": {"zh": "「提供零排放发电选项」即出自这篇同年文档", "en": "“Zero-emission electric power generation options” comes from this document"}},
            {"kind": "external", "href": None, "date": "2006",
             "label": {"zh": "SolarCity 公司口径 · 公开资料", "en": "SolarCity company statements · public sources"},
             "note": {"zh": "创立时间与董事长职务的口径来源", "en": "Source for founding year and chairman role"}},
        ],
        "image": None,
        "related": [
            {"href": "#e2002-10-03", "label": {"zh": "2002.10.03 · PayPal 交割（钱从哪来）", "en": "2002-10-03 · PayPal closes (where the money came from)"}},
            {"href": "#e2008-12-24", "label": {"zh": "2008.12.24 · 圣诞夜融资", "en": "2008-12-24 · Christmas Eve financing"}},
        ],
    },
    # ------------------------------------------------ 2008.12.24 圣诞夜融资
    {
        "id": "e2008-12-24",
        "date": "2008.12.24",
        "precision": "day",
        "companies": ["Tesla", "SpaceX"],
        "title": {"zh": "圣诞夜融资——最后一天的最后一个小时",
                  "en": "Christmas Eve financing — the last hour of the last day"},
        "summary": {
            "zh": "金融危机最深处：SpaceX 前一天刚被 NASA 16 亿美元合同救起；Tesla 的融资在圣诞夜 18:00 关闭——距发不出工资只差几个小时。",
            "en": "At the bottom of the crisis: SpaceX saved by a $1.6B NASA contract the day before; Tesla's round closed at 6 p.m. on Christmas Eve — hours from missing payroll.",
        },
        "background": {
            "zh": "2008 年 12 月：金融危机最深处。SpaceX 刚在 12 月 23 日被 NASA 16 亿美元货运合同救下，下一个排队等死的是 Tesla——Model S 研发烧着钱，融资在信贷紧缩里摇摇欲坠。马斯克已经投进了自己最后一份钱，按他自己的说法，当时在借钱付房租。",
            "en": "December 2008: the financial crisis at full depth. SpaceX had just been saved by NASA's $1.6 billion cargo contract on December 23, and Tesla was next in line to die — burning cash on Model S development with the round collapsing under the credit crunch. Musk had already put in his own last money and, by his own account, was borrowing for rent.",
        },
        "facts": [
            {"zh": "2008.12.23，NASA 向 SpaceX 授出 16 亿美元商业货运合同——SpaceX 先获救。",
             "en": "On 2008-12-23, NASA awards SpaceX the $1.6B cargo contract — SpaceX is saved first."},
            {"zh": "Tesla 该轮融资于 2008.12.24 18:00 关闭（本人多次自述口径）——离发薪日只差几个小时。",
             "en": "Tesla's round closes at 6 p.m. on 2008-12-24 (his own repeated account) — hours from payday."},
            {"zh": "他已投入自己最后一份钱，并自述当时在借钱付房租。",
             "en": "He had put in his own last money and was, by his own account, borrowing for rent."},
            {"zh": "融资过程由本人多次公开讲述：2015 年巴黎演讲、其后在 X 发帖自述。",
             "en": "He told the story repeatedly: on stage in Paris (2015), later in a post on X."},
        ],
        "quotes": [
            {"en": "We actually closed the financing round on Christmas Eve 2008. It was the last hour of the last day that it was possible.",
             "zh": "我们其实是在 2008 年圣诞夜关闭那一轮融资的。那是可能的最后一天的最后一个小时。",
             "source": {"zh": "本人自述 · 2015 巴黎演讲 / Business Insider / X 帖",
                        "en": "In his own words · Paris speech 2015 / Business Insider / post on X"}},
        ],
        "no_quote_note": None,
        "outcome": {
            "zh": "Tesla 活了下来，17 个月后登陆纳斯达克募资约 2.26 亿美元——1956 年福特之后首家上市的美国车企。2018 年上《60 分钟》时他称 2008 是最艰难的一年，当场落泪。圣诞夜关闭不是奇迹，而是现金流管理的最后一格：把自己最后的钱投进去，这个行为本身成了为这一轮融资定价的抵押品。（末句为编者分析，非其原话。）",
            "en": "Tesla lived, and seventeen months later IPO'd on Nasdaq raising about $226 million — the first American carmaker to go public since Ford in 1956. On 60 Minutes in 2018 he called 2008 his hardest year, close to tears. The Christmas Eve close was not a miracle but the last square of cash-flow management: putting in his own last money was itself the collateral that priced the round. (The last sentence is editorial analysis, not his words.)",
        },
        "materials": [
            {"kind": "ledger", "href": "primary.html#e2008-12-24", "date": "2008.12.24",
             "label": {"zh": "言行账本 e2008-12-24 · 圣诞夜融资", "en": "Ledger e2008-12-24 · Christmas Eve financing"},
             "note": {"zh": "一手言行记录：背景 / 原话 / 现场 / 后续四段全文", "en": "First-hand record: background / words / scene / aftermath"}},
            {"kind": "feature", "href": "stories.html", "date": None,
             "label": {"zh": "经典商战 · 收录 2008 生死役", "en": "War stories — the 2008 survival rounds"},
             "note": {"zh": "本事件在商战叙事线中的展开", "en": "The event inside the war-story narrative"}},
            {"kind": "external", "href": None, "date": "2008–2015（多次讲述）",
             "label": {"zh": "Business Insider · 巴黎演讲（2015.12）· 本人 X 自述", "en": "Business Insider · Paris speech (Dec 2015) · his own posts on X"},
             "note": {"zh": "关闭时间与「最后一天最后一小时」表述的口径来源", "en": "Sources for the closing time and the “last hour of the last day” account"}},
        ],
        "image": None,
        "related": [
            {"href": "#e2002-10-03", "label": {"zh": "2002.10.03 · PayPal 交割（最后一份钱从哪来）", "en": "2002-10-03 · PayPal closes (where the last money came from)"}},
            {"href": "#e2018-08-07", "label": {"zh": "2018.08.07 · 「资金已落实」", "en": "2018-08-07 · “Funding secured”"}},
        ],
    },
    # ------------------------------------------------ 2018.08.07 funding secured
    {
        "id": "e2018-08-07",
        "date": "2018.08.07",
        "precision": "day",
        "companies": ["Tesla"],
        "title": {"zh": "「资金已落实」——一条推文变成一场官司",
                  "en": "“Funding secured” — one tweet becomes a lawsuit"},
        "summary": {
            "zh": "Model 3 刚爬出生产地狱；2018.08.07 上午，他敲下把一家公司的股票变成一场官司的那句话。",
            "en": "Model 3 had just clawed out of production hell; on the morning of August 7, 2018, he typed the sentence that turned a stock into a courtroom.",
        },
        "background": {
            "zh": "Model 3 刚爬出生产地狱，做空者围猎 Tesla 股票，马斯克对华尔街的短视公开不满。2018 年 8 月 7 日上午，他敲下把一家公司的股票变成一场官司的那句话。",
            "en": "Model 3 had just clawed out of production hell, short sellers were circling Tesla's stock, and Musk was openly frustrated with Wall Street's short-termism. On the morning of August 7, 2018, he typed out one sentence that turned a stock into a courtroom.",
        },
        "facts": [
            {"zh": "2018.08.07 推文：正考虑以每股 420 美元将 Tesla 私有化，「资金已落实」。",
             "en": "Tweet of 2018-08-07: considering taking Tesla private at $420 a share, funding secured."},
            {"zh": "420 这个数字他后来承认是玩笑；股价当日异动。",
             "en": "420 was, as he later acknowledged, a joke; the stock lurched that day."},
            {"zh": "八天后，SEC 以证券欺诈起诉，并寻求禁止他执掌上市公司。",
             "en": "Eight days later the SEC sued for securities fraud and moved to bar him from running a public company."},
            {"zh": "和解：他与公司各罚 2,000 万美元；卸任董事长、保留 CEO；重大推文自此需经律师预审。",
             "en": "Settlement: $20M fines each for him and Tesla; chairman title gone, CEO seat kept; material tweets under lawyer review since."},
        ],
        "quotes": [
            {"en": "Am considering taking Tesla private at $420. Funding secured.",
             "zh": "正考虑以每股 420 美元将 Tesla 私有化。资金已到位。",
             "source": {"zh": "X（原 Twitter）帖 · 2018.08.07", "en": "Post on X (then Twitter) · 2018-08-07"}},
        ],
        "no_quote_note": None,
        "outcome": {
            "zh": "「一条推文 4000 万美元」成了公司治理的教材案例——按他此后的说法，这也是他后来宁可买下一个平台、也不活在别人规则下的原因之一。四年后，他真的买了一个。",
            "en": "“One tweet, $40 million” became a corporate-governance textbook case — and, in his own telling afterwards, part of why he would rather own a platform than live under someone else's rules. Four years later, he bought one.",
        },
        "materials": [
            {"kind": "ledger", "href": "primary.html#e2018-08-07", "date": "2018.08.07",
             "label": {"zh": "言行账本 e2018-08-07 · funding secured", "en": "Ledger e2018-08-07 · funding secured"},
             "note": {"zh": "一手言行记录", "en": "First-hand record"}},
            {"kind": "document", "href": "documents.html#d2018-08-07", "date": "2018.08.07",
             "label": {"zh": "《Taking Tesla Private》致员工信 · 同日 · Tesla 官网博客（Wayback 存档全文）", "en": "“Taking Tesla Private” employee letter · same day · Tesla blog (Wayback archive)"},
             "note": {"zh": "同日的私有化方案原文——与推文互为对照", "en": "Same-day plan in his own words — read against the tweet"}},
            {"kind": "post", "href": "x-posts.html#p2018-08-07", "date": "2018.08.07",
             "label": {"zh": "X 帖史收录 · funding secured 原帖", "en": "X posts archive · the original post"},
             "note": {"zh": "可查原件", "en": "The checkable original"}},
            {"kind": "feature", "href": "controversy.html#sec-sec", "date": None,
             "label": {"zh": "争议与批评 · SEC 和解专节", "en": "Controversies · the SEC settlement section"},
             "note": {"zh": "诉讼、罚金与律师预审规则的完整梳理", "en": "The full arc: suit, fines and the lawyer-review rule"}},
            {"kind": "external", "href": None, "date": "2018",
             "label": {"zh": "SEC 诉讼与和解文件", "en": "SEC litigation and settlement filings"},
             "note": {"zh": "指控与和解条款的官方口径", "en": "Official record of the charge and settlement terms"}},
        ],
        "image": None,
        "related": [
            {"href": "#e2022-10-28", "label": {"zh": "2022.10.28 · 四年后，他买下了整个平台", "en": "2022-10-28 · four years later, he bought the platform"}},
        ],
    },
    # ------------------------------------------------ 2022.10.28 Twitter 交割
    {
        "id": "e2022-10-28",
        "date": "2022.10.28",
        "precision": "day",
        "companies": ["X（原 Twitter）"],
        "title": {"zh": "440 亿美元交割——「鸟儿自由了」",
                  "en": "The $44B close — “the bird is freed”"},
        "summary": {
            "zh": "试图退出、被起诉、被强制按 54.20 美元原价交割。2022.10.28，全球的「城市广场」归他所有。",
            "en": "He tried to walk away, was sued, and was forced to close at the original $54.20. On October 28, 2022, the world's town square became his.",
        },
        "background": {
            "zh": "他试图退出、被起诉、被强制按原价 54.20 美元交割。2022 年 10 月 28 日，440 亿美元的交易完成，全球的「城市广场」归他所有。",
            "en": "He had tried to walk away, been sued, and been forced to close at the original $54.20 a share. On October 28, 2022, the $44B deal was done and he owned the world's town square.",
        },
        "facts": [
            {"zh": "收购协议签署于 2022.04.25：每股 54.20 美元、总额约 440 亿美元。",
             "en": "Merger agreement signed 2022-04-25: $54.20 a share, about $44B in total."},
            {"zh": "他随后试图退出、被起诉，最终被强制按原价完成交割（2022.10.28）。",
             "en": "He then tried to walk away, was sued, and was forced to close at the original price (2022-10-28)."},
            {"zh": "交割前两天（2022.10.26），他抱着水槽走进总部，发帖「let that sink in」。",
             "en": "Two days before the close (2022-10-26), he carried a sink into HQ and posted “let that sink in”."},
            {"zh": "交割后数小时内：解雇 CEO Parag Agrawal、CFO Ned Segal 与法律负责人 Vijaya Gadde，解散董事会，自任 CEO。",
             "en": "Within hours of the close: CEO Parag Agrawal, CFO Ned Segal and legal chief Vijaya Gadde fired; board dissolved; he becomes CEO."},
        ],
        "quotes": [
            {"en": "The bird is freed. — Spoiler alert: Let the good times roll.",
             "zh": "鸟儿自由了。——剧透警告：让好日子滚滚而来。",
             "source": {"zh": "X 帖 · 2022.10.28", "en": "Posts on X · 2022-10-28"}},
        ],
        "no_quote_note": None,
        "outcome": {
            "zh": "两周后是「extremely hardcore」邮件；九个月后，平台更名 X。这场收购的开场白，全部发在他如今彻底掌控的平台上。",
            "en": "Two weeks later came the “extremely hardcore” email; nine months later, the rename to X. The takeover's opening act ran on a platform he now controlled end to end.",
        },
        "materials": [
            {"kind": "ledger", "href": "primary.html#e2022-10-28", "date": "2022.10.28",
             "label": {"zh": "言行账本 e2022-10-28 · 交割日", "en": "Ledger e2022-10-28 · closing day"},
             "note": {"zh": "一手言行记录", "en": "First-hand record"}},
            {"kind": "document", "href": "documents.html#d2022-04-25", "date": "2022.04.25",
             "label": {"zh": "《Agreement and Plan of Merger》关键条款摘录 · 协议签署日档案", "en": "Agreement and Plan of Merger — key clauses excerpt, filed on signing day"},
             "note": {"zh": "54.20 美元/股与交易结构的原始出处", "en": "Original record of the $54.20 price and deal structure"}},
            {"kind": "post", "href": "x-posts.html#p2022-10-28", "date": "2022.10.28",
             "label": {"zh": "「鸟儿自由了」原帖收录", "en": "“The bird is freed” — original post"},
             "note": {"zh": "交割日的第一手表态", "en": "First-hand words on closing day"}},
            {"kind": "post", "href": "x-posts.html#p2022-10-26", "date": "2022.10.26",
             "label": {"zh": "「let that sink in」水槽进总部 · 交割前两天", "en": "“Let that sink in” — two days before the close"},
             "note": {"zh": "同一事件的另一份材料：入场姿态", "en": "Another record of the event: the entrance act"}},
            {"kind": "external", "href": None, "date": "2022.10",
             "label": {"zh": "Reuters · Washington Post（交割报道）", "en": "Reuters · Washington Post (closing coverage)"},
             "note": {"zh": "交割完成与人事变动的外部报道口径", "en": "External record of the close and the firings"}},
        ],
        "image": None,
        "related": [
            {"href": "#e2018-08-07", "label": {"zh": "2018.08.07 · 四年前，一条推文埋下买平台的种子", "en": "2018-08-07 · four years earlier, one tweet planted the seed"}},
        ],
    },
    # ------------------------------------------------ 2024.10.13 星舰塔捕
    {
        "id": "e2024-10-13",
        "date": "2024.10.13",
        "precision": "day",
        "companies": ["SpaceX"],
        "title": {"zh": "星舰塔捕——助推器回到塔的臂弯",
                  "en": "The tower catch — a booster in the tower's arms"},
        "summary": {
            "zh": "第五次试飞拿到监管许可，去尝试从未有人做过的事：让二十层楼高的助推器直接回到发射塔的机械臂里。",
            "en": "Flight 5 had regulatory clearance to attempt what had never been tried: bringing a 20-story booster back into the launch tower's arms.",
        },
        "background": {
            "zh": "Starship 第五次试飞拿到了监管许可，去尝试一件从未有人做过的事：让二十层楼高的助推器不落回着陆场，而是直接回到发射塔的臂弯里。此前每一飞都在学习；这一飞，是为了接住。",
            "en": "Starship's fifth test flight had regulatory clearance to attempt something never tried: bringing a 20-story-tall booster back not to a landing pad, but into the arms of the launch tower itself. Every prior flight had been about learning; this one was about catching.",
        },
        "facts": [
            {"zh": "2024.10.13，Starship 第五次试飞：超重型助推器发射约 7 分钟后返回，被发射塔机械臂在半空接住。",
             "en": "On 2024-10-13, Starship Flight 5: the Super Heavy booster returns about seven minutes after launch and is caught mid-air by the tower's mechanical arms."},
            {"zh": "此为监管批准的首次「塔捕」尝试；此前每一飞都以验证学习为目标。",
             "en": "It was the first regulator-approved catch attempt; every prior flight had been about learning."},
            {"zh": "接住、加注、再飞是 Starship 经济学命题的支点——塔捕把最大成本项（硬件）变成可复用资产。（本条为编者归纳）",
             "en": "Catch, refuel, relaunch is the economic thesis of Starship — the catch turns the biggest cost line, hardware, into a reusable asset. (Editorial summary)"},
        ],
        "quotes": [
            {"en": "The tower has caught the rocket!! … Big step towards making life multiplanetary was made today. — Science fiction without the fiction part.",
             "zh": "塔接住了火箭！！……今天，向让生命多行星化迈出了一大步。——没有虚构部分的科幻。",
             "source": {"zh": "X 帖 · 2024.10.13（Reuters · AP 引述）", "en": "Posts on X · 2024-10-13 (as quoted by Reuters · AP)"}},
        ],
        "no_quote_note": None,
        "outcome": {
            "zh": "接住、加注、再飞，是 Starship 全部经济学命题的支点。塔捕把最大的一项成本——硬件——变成了可复用资产，此后的每一飞都建立在这天之上。",
            "en": "Catching, refueling and relaunching is the whole economic thesis of Starship. The catch converted the biggest cost line — hardware — into a reusable asset, and every subsequent flight built on it.",
        },
        "materials": [
            {"kind": "ledger", "href": "primary.html#e2024-10-13", "date": "2024.10.13",
             "label": {"zh": "言行账本 e2024-10-13 · 星舰塔捕", "en": "Ledger e2024-10-13 · the tower catch"},
             "note": {"zh": "一手言行记录", "en": "First-hand record"}},
            {"kind": "post", "href": "x-posts.html#p2024-10-13", "date": "2024.10.13",
             "label": {"zh": "X 帖史收录 · 塔捕当日原帖", "en": "X posts archive · posts from catch day"},
             "note": {"zh": "可查原件", "en": "The checkable originals"}},
            {"kind": "interview", "href": "interviews.html#i2024-10-13", "date": "2024.10.13",
             "label": {"zh": "访谈与表态 · 「塔接住了火箭」", "en": "Interviews · “the tower has caught the rocket”"},
             "note": {"zh": "当日表态的完整收录", "en": "The day's statements, in full"}},
            {"kind": "image", "href": "assets/starship-catch.jpg", "date": "2024.10.13",
             "label": {"zh": "站内纪实图 · 塔捕现场（Steve Jurvetson 摄 · CC BY 2.0）", "en": "Photo on file · the catch (Steve Jurvetson · CC BY 2.0)"},
             "note": {"zh": "与账本同日互证的现场影像", "en": "Same-day visual corroboration of the ledger entry"}},
            {"kind": "external", "href": None, "date": "2024.10",
             "label": {"zh": "Reuters · AP（发射报道与引述）", "en": "Reuters · AP (launch coverage and quotes)"},
             "note": {"zh": "外部报道与引语转述口径", "en": "External coverage and quote attribution"}},
        ],
        "image": {
            "src": "assets/starship-catch.jpg",
            "w": 1200, "h": 1345,
            "alt": {"zh": "2024.10.13，星舰第五飞的超重型助推器被发射塔「Mechzilla」机械臂在半空接住",
                    "en": "The Super Heavy booster caught mid-air by the launch tower's arms during Starship Flight 5, 2024-10-13"},
            "caption": {"zh": "2024.10.13 塔捕现场：助推器悬停在机械臂之间。摄影：Steve Jurvetson · CC BY 2.0",
                        "en": "The catch, 2024-10-13: the booster hovering between the tower's arms. Photo: Steve Jurvetson · CC BY 2.0"},
        },
        "related": [],
    },
]

# 结构自检：生成器运行前先验证数据完整性（锚点/字段/精度枚举）
def validate():
    errs = []
    ids = set()
    for ev in EVENTS:
        eid = ev["id"]
        if eid in ids:
            errs.append(f"重复事件 id: {eid}")
        ids.add(eid)
        if ev["precision"] not in PRECISION_LABELS:
            errs.append(f"{eid}: 未知精度 {ev['precision']}")
        for sec in ("title", "summary", "background", "outcome"):
            if not ev.get(sec, {}).get("zh") or not ev[sec].get("en"):
                errs.append(f"{eid}: {sec} 缺中/英文")
        if not ev.get("quotes") and not ev.get("no_quote_note"):
            errs.append(f"{eid}: 无引语且无 no_quote_note 说明")
        for m in ev["materials"]:
            if m["kind"] not in KIND_LABELS:
                errs.append(f"{eid}: 未知材料类型 {m['kind']}")
            if not m.get("label", {}).get("zh"):
                errs.append(f"{eid}: 材料缺中文标签")
        for r in ev["related"]:
            if not r.get("href"):
                errs.append(f"{eid}: 相关事件缺 href")
    return errs

if __name__ == "__main__":
    problems = validate()
    if problems:
        for p in problems:
            print("✗", p)
        raise SystemExit(1)
    n_quotes = sum(len(e["quotes"]) for e in EVENTS)
    n_materials = sum(len(e["materials"]) for e in EVENTS)
    print(f"✓ 事件数据校验通过：{len(EVENTS)} 个事件 · {n_quotes} 条逐字引语 · {n_materials} 份材料关联")
