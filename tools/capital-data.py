# -*- coding: utf-8 -*-
"""资本流向数据 · 单一事实来源（V7-19 R10）

本模块是「资本流向可视化」的唯一数据源：
- 节点 = 资金来源（个人资本 / 风险与产业资本 / 公开市场 / 政府 / 收购方）
  与公司（Zip2 / PayPal / SpaceX / Tesla / SolarCity / X / xAI）；
- 流向 = 一笔真实发生的资金移动（个人投入 / 融资 / IPO / 政府合同 / 政府贷款 /
  收购对价 / 并购对价 / 退出套现），每笔必须带日期精度、金额与币种、
  统计口径说明和站内来源锚点。

纪律（每轮验收条件）：
- 零新增外部事实：全部金额与日期取自站内在册口径（言行账本 / 一手文档馆 /
  财务资本全景 / 公司档案 / 资本解剖），逐条带出处；
- 融资额、估值、收入、市值不得混写：估值 / 市值 / 减记不是资金流动，
  一律不入图（NON_FLOW_NOTE 显式声明），只在口径说明里作为背景引用并标「报道口径」；
- 站内确实未载金额的流向（2008 圣诞夜融资轮）保留入图但标「金额未入册」，
  线宽不适用——不编造数字凑图形；
- 收购方向用 from → to 表示（from 出资收购 to 的股东）；退出方向 公司 → 个人资本；
- 装饰性不伪装精确：线宽按金额对数标度（width_for()），图例明确声明是示意。

消费方：tools/build-capital.py（生成 capital-evolution.html #flow 资本流向区 +
capital-data.js 的 CAPITAL_V7 数据出口，供详情面板与 R15 检索复用）。
"""

# 流向类型 → 双语标签（决定徽标文字；线色按 GROUPS 分组）
KIND_LABELS = {
    "personal":    {"zh": "个人投入", "en": "Founder capital"},
    "funding":     {"zh": "融资", "en": "Funding round"},
    "ipo":         {"zh": "IPO 募资", "en": "IPO proceeds"},
    "contract":    {"zh": "政府合同", "en": "Gov. contract"},
    "loan":        {"zh": "政府贷款", "en": "Gov. loan"},
    "acquisition": {"zh": "收购对价", "en": "Acquisition price"},
    "merger":      {"zh": "并购对价", "en": "Merger price"},
    "exit":        {"zh": "退出套现", "en": "Exit proceeds"},
}

# 筛选分组 → 成员类型（线色与筛选芯片同组同色）
GROUPS = {
    "personal": {"label": {"zh": "个人投入", "en": "Founder capital"},
                 "color": "#C84032", "kinds": ["personal"]},
    "funding":  {"label": {"zh": "融资与 IPO", "en": "Funding & IPO"},
                 "color": "#1f3a5f", "kinds": ["funding", "ipo"]},
    "mna":      {"label": {"zh": "收购与并购", "en": "Acquisitions & mergers"},
                 "color": "#55524c", "kinds": ["acquisition", "merger"]},
    "gov":      {"label": {"zh": "政府资金", "en": "Government money"},
                 "color": "#8a6d1f", "kinds": ["contract", "loan"]},
    "exit":     {"label": {"zh": "退出套现", "en": "Exit proceeds"},
                 "color": "#2E7D4F", "kinds": ["exit"]},
}

# 日期精度 → 双语徽标（与事件档案同构）
PRECISION_LABELS = {
    "day":   {"zh": "精确到日", "en": "Day precision"},
    "month": {"zh": "精确到月", "en": "Month precision"},
    "year":  {"zh": "仅年份", "en": "Year only"},
}

# ---------------------------------------------------------------- 来源节点（左列）
SRC_NODES = [
    {
        "id": "musk",
        "label": {"zh": "个人资本", "en": "Personal capital"},
        "sub": {"zh": "Elon Musk", "en": "Elon Musk"},
        "desc": {"zh": "两次退出的套现（Zip2 约 2,200 万、PayPal 税后约 1.8 亿）是他此后再投入的全部本金。",
                  "en": "Proceeds from two exits (≈$22M from Zip2, ≈$180M after tax from PayPal) funded everything that followed."},
    },
    {
        "id": "vc",
        "label": {"zh": "风险与产业资本", "en": "Venture & strategic capital"},
        "sub": {"zh": "投资方 · 各轮", "en": "Investors · by round"},
        "desc": {"zh": "2008 圣诞夜联合投资方、2015 Google + Fidelity、2024–2026 xAI 各轮投资方（Valor 领投，英伟达与思科参投）。",
                  "en": "The 2008 Christmas Eve syndicate, Google + Fidelity in 2015, and xAI's 2024–26 round investors (Valor-led, with Nvidia and Cisco)."},
    },
    {
        "id": "public",
        "label": {"zh": "公开市场", "en": "Public markets"},
        "sub": {"zh": "IPO", "en": "IPO"},
        "desc": {"zh": "2010.06 Tesla 纳斯达克 IPO——1956 年福特之后首家上市的美国车企。",
                  "en": "Tesla's June 2010 Nasdaq IPO — the first US carmaker listing since Ford in 1956."},
    },
    {
        "id": "gov",
        "label": {"zh": "政府", "en": "Government"},
        "sub": {"zh": "合同与贷款", "en": "Contracts & loans"},
        "desc": {"zh": "NASA 是客户（CRS 合同是收入），DOE 是债主（ATVM 贷款已还清）——两种关系都不让渡股权。",
                  "en": "NASA is a customer (CRS is revenue) and DOE was a lender (the ATVM loan was repaid) — neither is equity."},
    },
    {
        "id": "acq",
        "label": {"zh": "收购方", "en": "Acquirers"},
        "sub": {"zh": "逐笔标注", "en": "labeled per deal"},
        "desc": {"zh": "康柏、eBay、Tesla、他牵头的财团、xAI——每笔收购的实际出资方在线上逐笔标注。",
                  "en": "Compaq, eBay, Tesla, his consortium, xAI — each deal's actual payer is labeled on its line."},
    },
]

# ---------------------------------------------------------------- 公司节点（右列）
CO_NODES = [
    {"id": "zip2",      "label": {"zh": "Zip2", "en": "Zip2"},                    "color_var": "--co-history",
     "href": "company-files.html#brief-zip2"},
    {"id": "paypal",    "label": {"zh": "X.com / PayPal", "en": "X.com / PayPal"}, "color_var": "--co-paypal",
     "href": "company-files.html#brief-paypal"},
    {"id": "spacex",    "label": {"zh": "SpaceX", "en": "SpaceX"},                "color_var": "--co-spacex",
     "href": "company-files.html#file-spacex"},
    {"id": "tesla",     "label": {"zh": "Tesla", "en": "Tesla"},                  "color_var": "--co-tesla",
     "href": "company-files.html#file-tesla"},
    {"id": "solarcity", "label": {"zh": "SolarCity", "en": "SolarCity"},          "color_var": "--co-solarcity",
     "href": "company-files.html#brief-solarcity"},
    {"id": "x",         "label": {"zh": "X（原 Twitter）", "en": "X (ex-Twitter)"}, "color_var": "--co-x",
     "href": "company-files.html#file-x"},
    {"id": "xai",       "label": {"zh": "xAI", "en": "xAI"},                      "color_var": "--co-xai",
     "href": "company-files.html#file-xai"},
]

# ---------------------------------------------------------------- 流向（18 笔）
# amount_usd：口径数字（美元）；None = 站内未载金额（线宽不适用）
FLOWS = [
    # ---- 收购方 → 早期两公司；两笔退出闭环（1999–2002）
    {
        "id": "zip2-acq", "kind": "acquisition", "group": "mna",
        "from": "acq", "from_note": {"zh": "康柏", "en": "Compaq"},
        "to": "zip2", "date": "1999", "precision": "year",
        "amount_usd": 3.07e8, "currency": "USD",
        "amount": {"zh": "约 3.07 亿美元", "en": "≈$307M"},
        "caliber": {"zh": "康柏收购 Zip2 的全部交易对价（非个人套现额）。",
                     "en": "Compaq's full purchase price for Zip2 (not his personal take)."},
        "sources": [
            {"href": "money.html", "label": {"zh": "资本解剖 · 第一桶金", "en": "Capital: the first fortune"}},
            {"href": "profile.html", "label": {"zh": "速览 · 早期两役", "en": "Profile: the early campaigns"}},
        ],
        "event": None, "file": "brief-zip2",
    },
    {
        "id": "zip2-exit", "kind": "exit", "group": "exit",
        "from": "zip2", "from_note": None,
        "to": "musk", "date": "1999", "precision": "year",
        "amount_usd": 2.2e7, "currency": "USD",
        "amount": {"zh": "约 2,200 万美元", "en": "≈$22M"},
        "caliber": {"zh": "个人所得份额（口径：速览/资本解剖在册），非交易总额。",
                     "en": "His personal share (per on-file accounts), not the deal total."},
        "sources": [
            {"href": "profile.html", "label": {"zh": "速览 · 早期两役", "en": "Profile: the early campaigns"}},
        ],
        "event": None, "file": "brief-zip2",
    },
    {
        "id": "pp-acq", "kind": "acquisition", "group": "mna",
        "from": "acq", "from_note": {"zh": "eBay", "en": "eBay"},
        "to": "paypal", "date": "2002.10.03", "precision": "day",
        "amount_usd": 1.5e9, "currency": "USD",
        "amount": {"zh": "15 亿美元", "en": "$1.5B"},
        "caliber": {"zh": "eBay 收购 PayPal 全部交易对价，2002.10.03 交割。",
                     "en": "eBay's full acquisition price for PayPal, closed 2002-10-03."},
        "sources": [
            {"href": "primary.html#e2002-10-03", "label": {"zh": "言行账本 e2002-10-03", "en": "Ledger e2002-10-03"}},
        ],
        "event": "e2002-10-03", "file": "brief-paypal",
    },
    {
        "id": "pp-exit", "kind": "exit", "group": "exit",
        "from": "paypal", "from_note": None,
        "to": "musk", "date": "2002.10.03", "precision": "day",
        "amount_usd": 1.8e8, "currency": "USD",
        "amount": {"zh": "约 1.8 亿美元（税后）", "en": "≈$180M after tax"},
        "caliber": {"zh": "本人访谈自述口径（2012–2013，USA Today 等）——税后所得。",
                     "en": "His own interview account (2012–13, USA Today etc.) — after-tax proceeds."},
        "sources": [
            {"href": "primary.html#e2002-10-03", "label": {"zh": "言行账本 e2002-10-03 · 引语原文", "en": "Ledger e2002-10-03 · the quote"}},
        ],
        "event": "e2002-10-03", "file": "brief-paypal",
    },
    # ---- 个人资本 → 三条战线（2002–2006）
    {
        "id": "spacex-found", "kind": "personal", "group": "personal",
        "from": "musk", "from_note": None,
        "to": "spacex", "date": "2002", "precision": "year",
        "amount_usd": 1.0e8, "currency": "USD",
        "amount": {"zh": "约 1 亿美元", "en": "≈$100M"},
        "caliber": {"zh": "本人自述分配口径（与 PayPal 税后所得同一引语）；创立故事细节未入册。",
                     "en": "His own account of the split (same quote as the PayPal proceeds); founding-story details not on file."},
        "sources": [
            {"href": "primary.html#e2002-10-03", "label": {"zh": "言行账本 e2002-10-03", "en": "Ledger e2002-10-03"}},
        ],
        "event": "e2002-10-03", "file": "file-spacex",
    },
    {
        "id": "tesla-found", "kind": "personal", "group": "personal",
        "from": "musk", "from_note": None,
        "to": "tesla", "date": "2004", "precision": "year",
        "amount_usd": 6.5e6, "currency": "USD",
        "amount": {"zh": "650 万美元", "en": "$6.5M"},
        "caliber": {"zh": "A 轮 750 万中的个人份额，并出任董事长；轮次其余部分不在本图重复画线。",
                     "en": "His share of the $7.5M Series A, taking the chair; the rest of the round is not double-drawn here."},
        "sources": [
            {"href": "company-files.html#file-tesla", "label": {"zh": "公司档案 · Tesla 里程碑", "en": "Company file: Tesla"}},
            {"href": "deep-dive-01.html", "label": {"zh": "深读 · 资本运作", "en": "Deep dive: capital"}},
        ],
        "event": None, "file": "file-tesla",
    },
    {
        "id": "sc-found", "kind": "personal", "group": "personal",
        "from": "musk", "from_note": None,
        "to": "solarcity", "date": "2006", "precision": "year",
        "amount_usd": 1.0e7, "currency": "USD",
        "amount": {"zh": "约 1,000 万美元", "en": "≈$10M"},
        "caliber": {"zh": "本人自述分配口径；公司由表兄弟按其创意创立、他出任董事长。",
                     "en": "His own account of the split; founded by his cousins on his idea, with him as chairman."},
        "sources": [
            {"href": "primary.html#e2002-10-03", "label": {"zh": "言行账本 e2002-10-03 · 引语原文", "en": "Ledger e2002-10-03 · the quote"}},
            {"href": "events.html#e2006", "label": {"zh": "事件档案 · SolarCity 创立", "en": "Event file: SolarCity founded"}},
        ],
        "event": "e2006", "file": "brief-solarcity",
    },
    # ---- 政府两笔（2008–2010）
    {
        "id": "spacex-nasa", "kind": "contract", "group": "gov",
        "from": "gov", "from_note": {"zh": "NASA（客户）", "en": "NASA (customer)"},
        "to": "spacex", "date": "2008.12", "precision": "month",
        "amount_usd": 1.6e9, "currency": "USD",
        "amount": {"zh": "16 亿美元", "en": "$1.6B"},
        "caliber": {"zh": "CRS 货运服务合同（2008.12.23 授予）——收入性质，非股权融资；与 Tesla 圣诞夜融资背靠背。",
                     "en": "The CRS cargo-services contract (awarded 2008-12-23) — revenue, not equity; back-to-back with Tesla's Christmas Eve round."},
        "sources": [
            {"href": "money.html", "label": {"zh": "资本解剖 · 外部资本节点", "en": "Capital: external money"}},
            {"href": "company-files.html#file-spacex", "label": {"zh": "公司档案 · SpaceX 里程碑", "en": "Company file: SpaceX"}},
        ],
        "event": None, "file": "file-spacex",
    },
    {
        "id": "tesla-xmas", "kind": "funding", "group": "funding",
        "from": "vc", "from_note": None,
        "to": "tesla", "date": "2008.12.24", "precision": "day",
        "amount_usd": None, "currency": "USD",
        "amount": {"zh": "金额未入册", "en": "Amount not on file"},
        "caliber": {"zh": "圣诞夜关闭的救命轮次（「可能的最后一天的最后一个小时」）；轮次总额站内未载，线宽不适用——不编造数字。",
                     "en": "The Christmas Eve round (“the last hour of the last day”); its size is not on file, so no line width is claimed — no invented number."},
        "sources": [
            {"href": "primary.html#e2008-12-24", "label": {"zh": "言行账本 e2008-12-24", "en": "Ledger e2008-12-24"}},
        ],
        "event": "e2008-12-24", "file": "file-tesla",
    },
    {
        "id": "tesla-doe", "kind": "loan", "group": "gov",
        "from": "gov", "from_note": {"zh": "DOE（债主）", "en": "DOE (lender)"},
        "to": "tesla", "date": "2010.01", "precision": "month",
        "amount_usd": 4.65e8, "currency": "USD",
        "amount": {"zh": "4.65 亿美元", "en": "$465M"},
        "caliber": {"zh": "ATVM 贷款：2009.06 有条件批准、2010.01 放款、2013.05.22 提前九年全额还清——债务，非股权。",
                     "en": "The ATVM loan: conditionally approved Jun 2009, disbursed Jan 2010, repaid in full nine years early on 2013-05-22 — debt, not equity."},
        "sources": [
            {"href": "primary.html#e2013-05-22", "label": {"zh": "言行账本 e2013-05-22 · 还清", "en": "Ledger e2013-05-22 · repaid"}},
            {"href": "primary.html#e2009-03-26", "label": {"zh": "言行账本 e2009-03-26 · 批准", "en": "Ledger e2009-03-26 · approval"}},
        ],
        "event": None, "file": "file-tesla",
    },
    {
        "id": "tesla-ipo", "kind": "ipo", "group": "funding",
        "from": "public", "from_note": None,
        "to": "tesla", "date": "2010.06", "precision": "month",
        "amount_usd": 2.26e8, "currency": "USD",
        "amount": {"zh": "约 2.26 亿美元", "en": "≈$226M"},
        "caliber": {"zh": "IPO 募资额（文件口径）；2010.06.29 登陆纳斯达克。",
                     "en": "IPO proceeds (filing-based); listed on Nasdaq 2010-06-29."},
        "sources": [
            {"href": "primary.html#e2010-06-29", "label": {"zh": "言行账本 e2010-06-29", "en": "Ledger e2010-06-29"}},
        ],
        "event": None, "file": "file-tesla",
    },
    # ---- 外部资本放大（2015–2026）
    {
        "id": "spacex-gf", "kind": "funding", "group": "funding",
        "from": "vc", "from_note": {"zh": "Google + Fidelity", "en": "Google + Fidelity"},
        "to": "spacex", "date": "2015.01.20", "precision": "day",
        "amount_usd": 1.0e9, "currency": "USD",
        "amount": {"zh": "10 亿美元", "en": "$1B"},
        "caliber": {"zh": "联合投资换取不到 10% 股份；对应估值约 100 亿为报道口径——估值不画线。",
                     "en": "Joint investment for <10%; the ≈$10B implied valuation is reported — valuations are never drawn."},
        "sources": [
            {"href": "primary.html#e2015-01-20", "label": {"zh": "言行账本 e2015-01-20", "en": "Ledger e2015-01-20"}},
        ],
        "event": None, "file": "file-spacex",
    },
    {
        "id": "sc-acq", "kind": "acquisition", "group": "mna",
        "from": "acq", "from_note": {"zh": "Tesla", "en": "Tesla"},
        "to": "solarcity", "date": "2016.11", "precision": "month",
        "amount_usd": 2.6e9, "currency": "USD",
        "amount": {"zh": "约 26 亿美元", "en": "≈$2.6B"},
        "caliber": {"zh": "全股票收购对价；关联交易当年受质疑，2022 年特拉华法院认定「entirely fair」。",
                     "en": "All-stock consideration; challenged as related-party then, ruled “entirely fair” by Delaware in 2022."},
        "sources": [
            {"href": "primary.html#e2016-11", "label": {"zh": "言行账本 e2016-11", "en": "Ledger e2016-11"}},
        ],
        "event": None, "file": "brief-solarcity",
    },
    {
        "id": "tw-acq", "kind": "acquisition", "group": "mna",
        "from": "acq", "from_note": {"zh": "他牵头的财团", "en": "His consortium"},
        "to": "x", "date": "2022.10.27", "precision": "day",
        "amount_usd": 4.4e10, "currency": "USD",
        "amount": {"zh": "440 亿美元（54.20 美元/股）", "en": "$44B ($54.20/share)"},
        "caliber": {"zh": "要约收购交割对价（2022.10.27）；同期公司另背上约 130 亿美元银行债务（协议条款在册）。",
                     "en": "Tender-offer consideration (closed 2022-10-27); the company also took on ≈$13B of bank debt (clauses on file)."},
        "sources": [
            {"href": "primary.html#e2022-10-28", "label": {"zh": "言行账本 e2022-10-28 · 交割", "en": "Ledger e2022-10-28 · closing"}},
            {"href": "documents.html#d2022-04-25", "label": {"zh": "一手文档 · 合并协议条款", "en": "Document: merger agreement clauses"}},
        ],
        "event": "e2022-10-28", "file": "file-x",
    },
    {
        "id": "xai-b", "kind": "funding", "group": "funding",
        "from": "vc", "from_note": None,
        "to": "xai", "date": "2024.05", "precision": "month",
        "amount_usd": 6.0e9, "currency": "USD",
        "amount": {"zh": "60 亿美元（B 轮）", "en": "$6B (Series B)"},
        "caliber": {"zh": "投后约 240 亿为报道口径（Reuters/CNBC/Forbes）——估值不画线。",
                     "en": "≈$24B post-money is reported (Reuters/CNBC/Forbes) — valuations are never drawn."},
        "sources": [
            {"href": "finance.html#xai", "label": {"zh": "财务资本全景 · xAI", "en": "Finance: xAI"}},
        ],
        "event": None, "file": "file-xai",
    },
    {
        "id": "xai-c", "kind": "funding", "group": "funding",
        "from": "vc", "from_note": None,
        "to": "xai", "date": "2024.12", "precision": "month",
        "amount_usd": 6.0e9, "currency": "USD",
        "amount": {"zh": "60 亿美元（C 轮）", "en": "$6B (Series C)"},
        "caliber": {"zh": "估值约 400 亿为 x.ai 官方公告口径——估值不画线。",
                     "en": "≈$40B valuation per x.ai's own announcement — valuations are never drawn."},
        "sources": [
            {"href": "finance.html#xai", "label": {"zh": "财务资本全景 · xAI", "en": "Finance: xAI"}},
        ],
        "event": None, "file": "file-xai",
    },
    {
        "id": "xai-x", "kind": "merger", "group": "mna",
        "from": "acq", "from_note": {"zh": "xAI", "en": "xAI"},
        "to": "x", "date": "2025.03.28", "precision": "day",
        "amount_usd": 3.3e10, "currency": "USD",
        "amount": {"zh": "约 330 亿美元（全股票）", "en": "≈$33B (all-stock)"},
        "caliber": {"zh": "并购对价口径（本人宣布·多方报道转述）：xAI 约 800 亿 / X 约 330 亿（含债约 450 亿）；两家均未上市无市场报价，估值部分不画线。",
                     "en": "Deal accounting (his announcement, as reported): xAI ≈$80B / X ≈$33B (≈$45B with debt); neither is listed — valuations are never drawn."},
        "sources": [
            {"href": "primary.html#e2025-03-28", "label": {"zh": "言行账本 e2025-03-28 · 推文逐字", "en": "Ledger e2025-03-28 · the post verbatim"}},
        ],
        "event": "e2025-03-28", "file": "file-x",
    },
    {
        "id": "xai-e", "kind": "funding", "group": "funding",
        "from": "vc", "from_note": None,
        "to": "xai", "date": "2026.01", "precision": "month",
        "amount_usd": 2.0e10, "currency": "USD",
        "amount": {"zh": "200 亿美元（E 轮）", "en": "$20B (Series E)"},
        "caliber": {"zh": "超募 33%（目标 150 亿）；投后约 2300 亿量级为公告与报道口径——估值不画线。Valor 领投、英伟达与思科参投。",
                     "en": "33% oversubscribed ($15B target); ≈$230B post-money is announcement/reporting — valuations are never drawn. Valor-led, Nvidia and Cisco aboard."},
        "sources": [
            {"href": "documents.html#d2026-01", "label": {"zh": "一手文档 · Series E 公告全文", "en": "Document: the Series E announcement"}},
        ],
        "event": None, "file": "file-xai",
    },
]

# 非流向口径声明（估值 / 市值 / 减记不入图）
NON_FLOW_NOTE = {
    "zh": "估值、市值与机构减记不是资金流动，本图一律不画线：SpaceX 股转估值（2021 约 $100.3B · 2024.12 约 $350B，报道口径）、"
          "X 的 Fidelity 连续减记（2023–24）、Tesla 市值（2021 破万亿）、xAI 并购中的 xAI 约 800 亿口径与 E 轮投后约 2300 亿量级——"
          "均只在各笔口径说明里作背景引用。",
    "en": "Valuations, market caps and writedowns are not money movements and are never drawn here: SpaceX tender valuations "
          "(≈$100.3B in 2021, ≈$350B in Dec 2024, reported), Fidelity's marks on X (2023–24), Tesla's $1T market cap (2021), "
          "the ≈$80B xAI accounting in the merger and the ≈$230B Series E post-money — all appear only as background in each line's caliber note. Figures live in the company files and the finance overview.",
}


def width_for(amount_usd):
    """线宽：按金额对数标度（示意，图例声明）。
    500 万 → ≈1.6px；10 亿 → ≈4.5px；440 亿 → ≈6.9px；上限 8。
    金额未载返回 None（调用方用最细虚线宽 1.4 并以「金额未入册」标注）。"""
    if not amount_usd:
        return None
    import math
    w = 1.4 + 1.3 * math.log10(amount_usd / 5e6)
    return round(min(max(w, 1.4), 8.0), 2)


def flow_label(flow):
    """线上短标签（图上空间有限）：来源特注（若有，去括号）+ 金额（超长去括号）+ 年份。
    返回 {"zh": ..., "en": ...}，两个语言版本逐字对应。"""
    year = flow["date"].split(".")[0]
    az = flow["amount"]["zh"]
    if len(az) > 14 and "（" in az:
        az = az.split("（")[0]
    fn = flow.get("from_note")
    fzh = (fn["zh"].split("（")[0] + " ") if fn else ""
    fen = (fn["en"] + " ") if fn else ""
    return {"zh": f"{fzh}{az} · {year}", "en": f"{fen}{flow['amount']['en']} · {year}"}


def validate():
    """结构自检：端点存在 / 枚举合法 / 日期与精度 / 金额与币种 / 来源锚点 /
    事件与档案锚点在册 / id 唯一 / from_note 规则（acq 组必须标实际出资方）。"""
    errs = []
    node_ids = {n["id"] for n in SRC_NODES} | {n["id"] for n in CO_NODES}
    co_ids = {n["id"] for n in CO_NODES}
    src_ids = {n["id"] for n in SRC_NODES}
    fids = set()
    site_hrefs = set()
    import io
    import os
    import re
    # 收集站内现有 href（同 verify.py 的断链思路，本地静态核对）
    for fn in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/.."):
        if fn.endswith(".html"):
            try:
                s = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", fn), encoding="utf-8").read()
                site_hrefs.update(re.findall(r'id="([^"]+)"', s))
                site_hrefs.add(fn)
            except Exception:
                pass
    for f in FLOWS:
        fid = f["id"]
        if fid in fids:
            errs.append(f"重复流向 id: {fid}")
        fids.add(fid)
        if f["kind"] not in KIND_LABELS:
            errs.append(f"{fid}: 未知类型 {f['kind']}")
        if f["group"] not in GROUPS:
            errs.append(f"{fid}: 未知分组 {f['group']}")
        elif f["kind"] not in GROUPS[f["group"]]["kinds"]:
            errs.append(f"{fid}: kind {f['kind']} 不属于分组 {f['group']}")
        if f["from"] not in node_ids or f["to"] not in node_ids:
            errs.append(f"{fid}: 端点不存在 {f['from']}→{f['to']}")
        if f["from"] == f["to"]:
            errs.append(f"{fid}: 自环")
        # 方向语义：公司节点只能出现在 to（收购/投入/融资），或 from（退出/并购）
        if f["to"] in src_ids and f["from"] in co_ids and f["kind"] != "exit":
            errs.append(f"{fid}: 公司→来源 仅允许退出套现")
        if f["kind"] == "exit" and f["from"] not in co_ids:
            errs.append(f"{fid}: 退出的 from 必须是公司")
        if f["group"] == "mna" and not f.get("from_note"):
            errs.append(f"{fid}: 收购/并购必须标注实际出资方 from_note")
        if not f.get("date") or not f.get("precision"):
            errs.append(f"{fid}: 缺日期或精度")
        elif f["precision"] not in PRECISION_LABELS:
            errs.append(f"{fid}: 未知精度 {f['precision']}")
        if not f.get("amount", {}).get("zh") or not f["amount"].get("en"):
            errs.append(f"{fid}: 金额缺中/英文")
        if not f.get("currency"):
            errs.append(f"{fid}: 缺币种")
        if not f.get("caliber", {}).get("zh") or not f["caliber"].get("en"):
            errs.append(f"{fid}: 口径说明缺中/英文")
        if not f.get("sources"):
            errs.append(f"{fid}: 至少要有一个站内来源锚点")
        for s in f["sources"]:
            h = s["href"]
            if "#" in h:
                pg, anc = h.split("#", 1)
                if pg not in site_hrefs or anc not in site_hrefs:
                    errs.append(f"{fid}: 来源锚点不在册 {h}")
            elif h not in site_hrefs:
                errs.append(f"{fid}: 来源页不在册 {h}")
            if not s.get("label", {}).get("zh"):
                errs.append(f"{fid}: 来源标签缺失")
        if f.get("event"):
            if ("events.html#" + f["event"]) not in ("",) and f["event"] not in site_hrefs:
                errs.append(f"{fid}: 事件锚点不在册 events.html#{f['event']}")
        if f.get("file") and f["file"] not in site_hrefs:
            errs.append(f"{fid}: 档案锚点不在册 company-files.html#{f['file']}")
    # 节点检查
    for n in SRC_NODES + CO_NODES:
        if not n.get("label", {}).get("zh"):
            errs.append(f"节点 {n.get('id')}: 缺标签")
    for n in CO_NODES:
        h = n["href"]
        if "#" in h:
            pg, anc = h.split("#", 1)
            if pg not in site_hrefs or anc not in site_hrefs:
                errs.append(f"节点 {n['id']}: 档案锚点不在册 {h}")
    return errs


if __name__ == "__main__":
    problems = validate()
    if problems:
        for p in problems:
            print("✗", p)
        raise SystemExit(1)
    n_amounted = sum(1 for f in FLOWS if f["amount_usd"])
    groups = {g: sum(1 for f in FLOWS if f["group"] == g) for g in GROUPS}
    print(f"✓ capital-data: {len(SRC_NODES)} 来源节点 + {len(CO_NODES)} 公司节点 · "
          f"{len(FLOWS)} 笔流向（{n_amounted} 笔有金额口径 · {len(FLOWS)-n_amounted} 笔金额未入册）· "
          f"分组 {'/'.join(f'{k}:{v}' for k, v in groups.items())} · 自检通过")
