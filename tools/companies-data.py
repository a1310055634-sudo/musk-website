# -*- coding: utf-8 -*-
"""公司关系数据 · 单一事实来源（V7-19 R7）

本模块是「公司关系总览」的唯一数据源：
- 节点 = 一家公司（或运营者本人），含业务定位一句话与当前状态；
- 边 = 一条关系（创立 / 入主执掌 / 收购 / 创意发起 / 编者关联），
  每条边必须带 evidence 分级（verified=站内在册证实 / editorial=编者归纳）与站内来源锚点。

纪律：
- 全部关系取自站内已在册口径（言行账本 primary.html、公司版图 companies.html、
  长卷 profile.html、xAI·Grok grok.html、资本解剖 money.html、事件档案 events-data.py），
  本轮不新增外部事实；
- 收购方向用 from → to 表示（from 收购 to）；金额只写站内在册口径，不混用估值与收入；
- 「编者关联」必须显式标 evidence=editorial，不得与已证实关系混排；
- 2002 SpaceX 创立的戏剧细节未入册（见甄别记录），本数据只使用「2002 年创立」这一
  全站通识口径，不配逐字引语。

消费方：tools/build-network.py（生成 companies.html #network 关系区 + companies-data.js
本地 JS 数据，供 R8 公司档案 / R9 时间轴 / R10 资本流向复用）。
"""

# 关系类型 → 双语标签（决定边的线型与图例分组）
REL_LABELS = {
    "found":   {"zh": "创立", "en": "Founded"},
    "chair":   {"zh": "入主·执掌", "en": "Chair / CEO"},
    "acquire": {"zh": "收购", "en": "Acquired"},
    "originate": {"zh": "创意发起", "en": "Idea & chair"},
    "rival_editorial": {"zh": "对手（编者关联）", "en": "Rival (editorial)"},
}

# 证据分级 → 双语标签（图形、文字和公司色标一致；证据不只靠颜色区分，配前缀文字）
EVIDENCE_LABELS = {
    "verified":  {"zh": "已证实", "en": "Verified"},
    "editorial": {"zh": "编者关联", "en": "Editorial"},
}

# 公司状态 → 双语标签
STATUS_LABELS = {
    "operating":  {"zh": "在营", "en": "Operating"},
    "absorbed":   {"zh": "已并入", "en": "Absorbed"},
    "exited":     {"zh": "已退出", "en": "Exited"},
}

# 关系图上每个公司节点有专属色标（CSS 变量，色值集中在 style.css :root）。
# 色标只作辅助：节点内始终有公司名文字，边上有类型+年份文字，图例独立成文。

COMPANIES = [
    # ------------------------------------------------ 运营者（中心节点）
    {
        "id": "musk",
        "name": "Elon Musk",
        "abbr": "MUSK",
        "color_var": "--co-musk",
        "sector": {"zh": "运营者", "en": "Operator"},
        "era": {"zh": "1995 年至今", "en": "1995–present"},
        "era_short": "1995–",
        "status": "operating",
        "blurb": {
            "zh": "连续创业者与资本再投入者：四次退出（Zip2、PayPal 及早期股份），把个人套现变成新公司的启动资本。",
            "en": "Serial founder and recycler of capital: four exits, each converted into founding capital for the next company.",
        },
        "href": "profile.html",
    },
    # ------------------------------------------------ 在营六家
    {
        "id": "tesla",
        "name": "Tesla",
        "abbr": "TSLA",
        "color_var": "--co-tesla",
        "sector": {"zh": "电动车与能源", "en": "EV & Energy"},
        "era": {"zh": "2004 年入主 · 2008 年任 CEO", "en": "Joined 2004 · CEO since 2008"},
        "era_short": "2004",
        "status": "operating",
        "blurb": {
            "zh": "把电动车从「政策合规品」做成人人想要的科技产品；史上首家市值破万亿的车企。",
            "en": "Turned EVs from compliance cars into objects of desire; first carmaker to a $1T market cap.",
        },
        "href": "company-files.html#file-tesla",
    },
    {
        "id": "spacex",
        "name": "SpaceX",
        "abbr": "SPCX",
        "color_var": "--co-spacex",
        "sector": {"zh": "商业航天", "en": "Space"},
        "era": {"zh": "2002 年创立", "en": "Founded 2002"},
        "era_short": "2002",
        "status": "operating",
        "blurb": {
            "zh": "用可回收火箭把发射成本打下来；如今既运宇航员，也筹划火星。",
            "en": "Reusability collapsed launch costs; now carries astronauts and plans for Mars.",
        },
        "href": "company-files.html#file-spacex",
    },
    {
        "id": "x",
        "name": "X",
        "abbr": "X",
        "color_var": "--co-x",
        "sector": {"zh": "社交平台", "en": "Social platform"},
        "era": {"zh": "2022 年收购 · 2023 年更名", "en": "Acquired 2022 · renamed 2023"},
        "era_short": "2022",
        "status": "absorbed",
        "blurb": {
            "zh": "以 440 亿美元买入 Twitter 并更名 X——既是他的扩音器，2025 年并入 xAI 后成为 AI 公司的一部分。",
            "en": "Twitter, bought for $44B and renamed X — his loudspeaker, and since 2025 part of an AI company.",
        },
        "href": "company-files.html#file-x",
    },
    {
        "id": "xai",
        "name": "xAI",
        "abbr": "XAI",
        "color_var": "--co-xai",
        "sector": {"zh": "人工智能", "en": "AI"},
        "era": {"zh": "2023 年创立", "en": "Founded 2023"},
        "era_short": "2023",
        "status": "operating",
        "blurb": {
            "zh": "Grok 之父；2026 年 1 月完成 200 亿美元 Series E（估值约 2300 亿量级），2025 年已先行并入 X 平台。",
            "en": "Maker of Grok; raised $20B in Jan 2026 at a ~$230B scale valuation, after absorbing X in 2025.",
        },
        "href": "company-files.html#file-xai",
    },
    {
        "id": "neuralink",
        "name": "Neuralink",
        "abbr": "NRLK",
        "color_var": "--co-neuralink",
        "sector": {"zh": "脑机接口", "en": "Brain–computer"},
        "era": {"zh": "2016 年创立", "en": "Founded 2016"},
        "era_short": "2016",
        "status": "operating",
        "blurb": {
            "zh": "第一批客户是瘫痪患者——用意念移动光标；长期故事是在 AI 变强的年代给人类大脑留一个接口。",
            "en": "First customers are paralyzed patients moving cursors with thought; the long game is human–machine symbiosis.",
        },
        "href": "company-files.html#brief-neuralink",
    },
    {
        "id": "boring",
        "name": "The Boring Company",
        "abbr": "BORING",
        "color_var": "--co-boring",
        "sector": {"zh": "隧道交通", "en": "Tunneling"},
        "era": {"zh": "2016 年创立", "en": "Founded 2016"},
        "era_short": "2016",
        "node_label": "Boring Company",
        "status": "operating",
        "blurb": {
            "zh": "起因是一句堵车抱怨：地面解决不了，就从地下走；卖点是持续压低每英里造价。",
            "en": "Born from one traffic complaint: if the surface is stuck, go under it — competing on cost per mile.",
        },
        "href": "company-files.html#brief-boring",
    },
    # ------------------------------------------------ 历史 / 已并入
    {
        "id": "zip2",
        "name": "Zip2",
        "abbr": "ZIP2",
        "color_var": "--co-history",
        "sector": {"zh": "网上城市指南", "en": "Online city guide"},
        "era": {"zh": "1995 年创立 · 1999 年退出", "en": "1995 · exited 1999"},
        "era_short": "1995",
        "status": "exited",
        "blurb": {
            "zh": "给报纸做的网上城市指南；1999 年康柏以约 3.07 亿美元买下，个人套现约 2200 万——第一桶金。",
            "en": "A city guide for newspapers; Compaq paid ≈$307M in 1999, netting him ≈$22M — the first fortune.",
        },
        "href": "company-files.html#brief-zip2",
    },
    {
        "id": "paypal",
        "name": "X.com / PayPal",
        "abbr": "PYPL",
        "color_var": "--co-paypal",
        "sector": {"zh": "网上银行→支付", "en": "Online bank → payments"},
        "era": {"zh": "1999 年创立 · 2002 年退出", "en": "1999 · exited 2002"},
        "era_short": "1999",
        "node_label": "X.com / PayPal",
        "status": "exited",
        "blurb": {
            "zh": "他 1999 年创办的网上银行 X.com 长成了 PayPal；2002 年 eBay 以 15 亿美元收购，税后约 1.8 亿美元全部再投入。",
            "en": "His 1999 online bank X.com grew into PayPal; eBay paid $1.5B in 2002 — and the ≈$180M after tax was reinvested in full.",
        },
        "href": "company-files.html#brief-paypal",
    },
    {
        "id": "solarcity",
        "name": "SolarCity",
        "abbr": "SCTY",
        "color_var": "--co-solarcity",
        "sector": {"zh": "太阳能", "en": "Solar energy"},
        "era": {"zh": "2006 年创立 · 2016 年并入 Tesla", "en": "2006 · absorbed 2016"},
        "era_short": "2006",
        "status": "absorbed",
        "blurb": {
            "zh": "表兄弟按他的创意创立、他任董事长的太阳能公司；2016 年以约 26 亿美元并入 Tesla，2022 年法院认定交易公允。",
            "en": "A solar company his cousins founded on his idea, with him as chairman; absorbed by Tesla for ≈$2.6B in 2016, ruled fair in 2022.",
        },
        "href": "company-files.html#brief-solarcity",
    },
    {
        "id": "openai",
        "name": "OpenAI",
        "abbr": "OAI",
        "color_var": "--co-history",
        "sector": {"zh": "人工智能", "en": "AI"},
        "era": {"zh": "2015 年联合创立 · 2018 年退出董事会", "en": "Co-founded 2015 · left board 2018"},
        "era_short": "2015",
        "status": "exited",
        "blurb": {
            "zh": "2015 年的联合创始人，2018 年退出董事会——数年后成为 xAI 最受关注的对手。",
            "en": "A 2015 co-founder who left the board in 2018 — years later, xAI's most watched rival.",
        },
        "href": "company-files.html#brief-openai",
    },
]

# 关系边：from → to；acquire 方向 = from 收购 to。
# evidence: verified=站内在册证实 · editorial=编者归纳（线型用虚线，图例单独标明）
LINKS = [
    {
        "id": "l-musk-tesla",
        "from": "musk", "to": "tesla",
        "type": "chair",
        "date": "2004–2008",
        "precision": "year",
        "label": {"zh": "2004 年入主 · 2008 年起任 CEO", "en": "Joined 2004 · CEO since 2008"},
        "short": {"zh": "2004 入主 · 2008 CEO", "en": "2004 · CEO '08"},
        "evidence": "verified",
        "source": {"href": "primary.html#e2008-12-24",
                   "note": {"zh": "2008 圣诞夜融资——CEO 任期内的生死时刻（账本）",
                            "en": "Christmas Eve financing, 2008 — the CEO tenure's near-death moment (ledger)"}},
    },
    {
        "id": "l-musk-spacex",
        "from": "musk", "to": "spacex",
        "type": "found",
        "date": "2002",
        "precision": "year",
        "label": {"zh": "2002 年创立", "en": "Founded 2002"},
        "short": {"zh": "创立 2002", "en": "2002"},
        "evidence": "verified",
        "source": {"href": "companies.html",
                   "note": {"zh": "全站通识口径（创立年份）；创立故事细节未入册",
                            "en": "Site-wide common-knowledge year; founding-story details are not on file"}},
    },
    {
        "id": "l-musk-x",
        "from": "musk", "to": "x",
        "type": "acquire",
        "date": "2022",
        "precision": "day",
        "label": {"zh": "440 亿美元收购 · 2022.10.27 交割", "en": "$44B acquisition · closed 2022-10-27"},
        "short": {"zh": "收购 2022", "en": "2022"},
        "evidence": "verified",
        "source": {"href": "primary.html#e2022-10-28",
                   "note": {"zh": "交割与 let that sink in 现场（账本）",
                            "en": "Closing and the sink moment (ledger)"}},
    },
    {
        "id": "l-musk-xai",
        "from": "musk", "to": "xai",
        "type": "found",
        "date": "2023",
        "precision": "year",
        "label": {"zh": "2023 年创立", "en": "Founded 2023"},
        "short": {"zh": "创立 2023", "en": "2023"},
        "evidence": "verified",
        "source": {"href": "grok.html",
                   "note": {"zh": "xAI·Grok 档案：创立与 Grok 发布时间线",
                            "en": "xAI & Grok file: founding and Grok launch timeline"}},
    },
    {
        "id": "l-musk-neuralink",
        "from": "musk", "to": "neuralink",
        "type": "found",
        "date": "2016",
        "precision": "year",
        "label": {"zh": "2016 年创立", "en": "Founded 2016"},
        "short": {"zh": "创立 2016", "en": "2016"},
        "evidence": "verified",
        "source": {"href": "companies.html",
                   "note": {"zh": "公司档案卡：脑机接口 · 2016 年创立",
                            "en": "Company card: brain–computer interface · founded 2016"}},
    },
    {
        "id": "l-musk-boring",
        "from": "musk", "to": "boring",
        "type": "found",
        "date": "2016",
        "precision": "year",
        "label": {"zh": "2016 年创立", "en": "Founded 2016"},
        "short": {"zh": "创立 2016", "en": "2016"},
        "evidence": "verified",
        "source": {"href": "companies.html",
                   "note": {"zh": "公司档案卡：隧道交通 · 2016 年创立",
                            "en": "Company card: tunneling · founded 2016"}},
    },
    {
        "id": "l-musk-solarcity",
        "from": "musk", "to": "solarcity",
        "type": "originate",
        "date": "2006",
        "precision": "year",
        "label": {"zh": "创意发起 · 任董事长", "en": "His idea · he chaired"},
        "short": {"zh": "创意发起 2006", "en": "2006"},
        "evidence": "verified",
        "source": {"href": "primary.html#e2006",
                   "note": {"zh": "表兄弟按他的创意创立，他出任董事长（账本/事件档案 e2006）",
                            "en": "His cousins founded it on his idea; he chaired (ledger / event file e2006)"}},
    },
    {
        "id": "l-musk-paypal",
        "from": "musk", "to": "paypal",
        "type": "found",
        "date": "1999",
        "precision": "year",
        "label": {"zh": "1999 年创办 X.com", "en": "Founded X.com, 1999"},
        "short": {"zh": "X.com 1999", "en": "1999"},
        "evidence": "verified",
        "source": {"href": "profile.html",
                   "note": {"zh": "长卷：X.com——字母 X 的第一次出现——后来长成 PayPal",
                            "en": "Long read: X.com — the first appearance of the letter X — grew into PayPal"}},
    },
    {
        "id": "l-musk-zip2",
        "from": "musk", "to": "zip2",
        "type": "found",
        "date": "1995",
        "precision": "year",
        "label": {"zh": "1995 年创立", "en": "Founded 1995"},
        "short": {"zh": "创立 1995", "en": "1995"},
        "evidence": "verified",
        "source": {"href": "profile.html",
                   "note": {"zh": "长卷：1995 年从斯坦福退学两天，创办 Zip2",
                            "en": "Long read: dropped out of a Stanford PhD in 1995 and built Zip2"}},
    },
    {
        "id": "l-musk-openai",
        "from": "musk", "to": "openai",
        "type": "found",
        "date": "2015–2018",
        "precision": "year",
        "label": {"zh": "2015 年联合创立 · 2018 年退出董事会", "en": "Co-founded 2015 · left board 2018"},
        "short": {"zh": "联创 2015", "en": "2015"},
        "evidence": "verified",
        "source": {"href": "companies.html",
                   "note": {"zh": "早期交易记录表：OpenAI 行",
                            "en": "Early deal record: the OpenAI row"}},
    },
    {
        "id": "l-tesla-solarcity",
        "from": "tesla", "to": "solarcity",
        "type": "acquire",
        "date": "2016",
        "precision": "month",
        "label": {"zh": "约 26 亿美元 · 2016.11 股东通过", "en": "≈$2.6B · approved Nov 2016"},
        "short": {"zh": "26 亿收购 2016", "en": "$2.6B · 2016"},
        "evidence": "verified",
        "source": {"href": "primary.html#e2016-11",
                   "note": {"zh": "关联交易，当年受质疑；2022 年特拉华最高法院认定「entirely fair」（账本 e2016-11）",
                            "en": "A related-party deal criticized at the time; ruled “entirely fair” by Delaware's top court in 2022 (ledger e2016-11)"}},
    },
    {
        "id": "l-xai-x",
        "from": "xai", "to": "x",
        "type": "acquire",
        "date": "2025.03",
        "precision": "day",
        "label": {"zh": "全股票 · xAI 约 800 亿 / X 约 330 亿 · 2025.03.28", "en": "All-stock · xAI ≈$80B / X ≈$33B · 2025-03-28"},
        "short": {"zh": "全股票 2025", "en": "All-stock 2025"},
        "evidence": "verified",
        "source": {"href": "primary.html#e2025-03-28",
                   "note": {"zh": "本人推文逐字（x.com/elonmusk/status/1905731750275510312），CNBC/Forbes/AP 多源互证（账本 e2025-03-28）",
                            "en": "His own post (x.com/elonmusk/status/1905731750275510312), corroborated by CNBC/Forbes/AP (ledger e2025-03-28)"}},
    },
    {
        "id": "l-openai-xai",
        "from": "openai", "to": "xai",
        "type": "rival_editorial",
        "date": None,
        "precision": None,
        "label": {"zh": "数年后成为 xAI 最受关注的对手", "en": "Years later, xAI's most watched rival"},
        "short": {"zh": "对手", "en": "Rival"},
        "evidence": "editorial",
        "source": {"href": "companies.html",
                   "note": {"zh": "编者归纳（早期交易记录表编者按语），非任何一方的官方表述",
                            "en": "Editorial framing (early deal record note) — not an official characterization by either side"}},
    },
]


def validate():
    """结构自检：重复 ID / 边端点存在 / 双语字段完整 / 枚举合法 / 每边有来源。"""
    errs = []
    ids = set()
    for c in COMPANIES:
        cid = c["id"]
        if cid in ids:
            errs.append(f"重复公司 id: {cid}")
        ids.add(cid)
        for k in ("name", "abbr", "sector", "era", "blurb"):
            if k not in c:
                errs.append(f"{cid}: 缺字段 {k}")
        if not c["blurb"].get("zh") or not c["blurb"].get("en"):
            errs.append(f"{cid}: blurb 缺中/英文")
        if c["status"] not in STATUS_LABELS:
            errs.append(f"{cid}: 未知状态 {c['status']}")
        if not c.get("color_var", "").startswith("--co-"):
            errs.append(f"{cid}: color_var 必须是 --co-* 变量")
        if not c.get("href"):
            errs.append(f"{cid}: 缺档案入口 href")
    lids = set()
    for lnk in LINKS:
        lid = lnk["id"]
        if lid in lids:
            errs.append(f"重复关系 id: {lid}")
        lids.add(lid)
        for end in ("from", "to"):
            if lnk[end] not in ids:
                errs.append(f"{lid}: 端点 {end}={lnk[end]} 不在节点表")
        if lnk["type"] not in REL_LABELS:
            errs.append(f"{lid}: 未知关系类型 {lnk['type']}")
        if lnk["evidence"] not in EVIDENCE_LABELS:
            errs.append(f"{lid}: 未知证据分级 {lnk['evidence']}")
        if not lnk.get("short", {}).get("zh") or not lnk["short"].get("en"):
            errs.append(f"{lid}: short 缺中/英文")
        if not lnk["label"].get("zh") or not lnk["label"].get("en"):
            errs.append(f"{lid}: label 缺中/英文")
        src = lnk.get("source") or {}
        if not src.get("href"):
            errs.append(f"{lid}: 缺来源锚点（editorial 也必须有站内在册位置）")
        if not src.get("note", {}).get("zh") or not src.get("note", {}).get("en"):
            errs.append(f"{lid}: source.note 缺中/英文")
        if lnk["evidence"] == "verified" and not lnk.get("date"):
            errs.append(f"{lid}: 已证实关系必须带日期")
    # 中心节点必须存在且只作 from（运营者不被收购）
    if "musk" not in ids:
        errs.append("缺中心节点 musk")
    for lnk in LINKS:
        if lnk["to"] == "musk":
            errs.append(f"{lnk['id']}: musk 只能作关系起点")
    return errs


# 事件档案（events-data.py）中的公司名 → 本表公司 id 的别名映射。
# R9 起事件档案含 e2025-03-28（xAI 收购 X，记作「X（原 Twitter）」），
# xai—x 关系的证据锚点仍用账本 primary.html#e2025-03-28（在册口径不变）；
# 2022 交割同样记作「X（原 Twitter）」，故 x 节点别名保留两种写法。
EVENT_NAME_ALIASES = {
    "tesla": ["Tesla"],
    "spacex": ["SpaceX"],
    "solarcity": ["SolarCity"],
    "paypal": ["PayPal"],
    "x": ["X", "X（原 Twitter）"],
    "xai": ["xAI"],
}


def events_for_company(cid):
    """交叉引用：从 events-data.py 找出该公司出现在哪些事件里（单一事实来源联动）。"""
    names = EVENT_NAME_ALIASES.get(cid)
    if not names:
        return []
    ED = load_events()
    out = []
    for ev in ED.EVENTS:
        if ev["companies"] and any(n in ev["companies"] for n in names):
            out.append({"id": ev["id"], "date": ev["date"],
                        "title": ev["title"]})
    return out


def load_events():
    import importlib.util
    import os
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "events-data.py")
    spec = importlib.util.spec_from_file_location("events_data", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


if __name__ == "__main__":
    problems = validate()
    if problems:
        for p in problems:
            print("✗", p)
        raise SystemExit(1)
    print(f"✓ companies-data: {len(COMPANIES)} 节点 · {len(LINKS)} 关系 · 自检通过")
    for c in COMPANIES:
        evs = events_for_company(c["id"])
        print(f"  {c['id']:>10} ← {len(evs)} 个事件")
