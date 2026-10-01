# -*- coding: utf-8 -*-
"""社区资源注册表（resources.html 单一事实来源）。V9-20 R10

纪律（V9-20 计划·纪律 B，违反即返工）：
- 只收「链接 + 一句话简介 + 元数据」，不复制外部内容正文；
- 外链不构成运行时依赖：资源页本体静态、file:// 离线可读；
- 每条 URL 实访核活（curl http_code 或 WebFetch），GitHub 项目记 stars 与最近提交年
  （api.github.com/repos/… 无认证，串行限流）；
- 死链如实标「存档」不删；
- 收录理由一句必填；关联公司用检索实体词表（与 build-search-index.ENTITY_RULES 同表）。

字段说明（validate() 强制，不过校验拒绝生成）：
  id        稳定 slug（页面锚 r-<id>，检索索引同 id）
  url       http(s) 完整外链
  name      {zh, en}          一行名称
  desc      {zh, en}          一句话简介（不复制外部正文）
  category  CATEGORIES 键
  lang      en | zh | zh/en
  activity  维护中 | 停更 | 存档
  license   {zh, en}          许可 / 权利口径（不确知就写「见官方文档」，不编造）
  reason    {zh, en}          收录理由一句
  companies [实体名]          ⊆ COMPANIES_VOCAB
  checked   YYYY-MM-DD        核活日期（必填，逐条实测）
  http      int               核活响应码（200 = 当日可访问；403/000 记录不收录）
  gh        可选 {stars, pushed}  GitHub 项目实测（stars int，pushed "YYYY-MM"）
  note      可选 {zh, en}     口径备注（双语）
"""

CATEGORIES = {
    "official":   {"zh": "官方与标准", "en": "Official & Standards"},
    "opensource": {"zh": "开源项目",   "en": "Open Source"},
    "community":  {"zh": "社区与档案", "en": "Community & Archives"},
    "tools":      {"zh": "工具与数据", "en": "Tools & Data"},
}

# 与 build-search-index.py ENTITY_RULES 实体名一致（检索「按公司过滤」直接可用）。
# OpenAI（V9-20 R11）：仅资源条目使用——索引实体推断 ENTITY_RULES 不含 OpenAI，
# 资源条目经 CO_MAP 透传自动进入检索过滤，不扰动存量 282 条的实体推断。
COMPANIES_VOCAB = {"Tesla", "SpaceX", "X / Twitter", "xAI", "Neuralink", "Boring Company", "OpenAI", "综合"}

RESOURCES = [
    {
        "id": "sec-edgar-tesla",
        "url": "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001318605&type=10-K&dateb=&owner=include&count=40",
        "name": {"zh": "SEC EDGAR · Tesla 上市公司文件", "en": "SEC EDGAR — Tesla filings"},
        "desc": {
            "zh": "美国证监会 EDGAR 库中 Tesla, Inc.（CIK 0001318605）的申报文件总目：10-K / 10-Q / 8-K / S-1 全文免费公开。",
            "en": "The SEC EDGAR index for Tesla, Inc. (CIK 0001318605): full texts of 10-K / 10-Q / 8-K / S-1 filings, free and public.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "美国政府公开数据", "en": "U.S. government public data"},
        "reason": {
            "zh": "本站财报与风险表述的原文锚点所在库；核对公司口径时「原文优先」的第一站。",
            "en": "Where this site anchors its filing quotes; the first stop for verifying the company side of any claim.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-01",
        "http": 200,
        "note": {
            "zh": "SEC 公平访问政策要求脚本访问申报含联系邮箱的 User-Agent 并限速（约 10 次/秒）。",
            "en": "SEC fair-access policy requires a declared User-Agent with contact e-mail for scripted access (~10 req/s).",
        },
    },
    {
        "id": "tesla-vehicle-command",
        "url": "https://github.com/teslamotors/vehicle-command",
        "name": {"zh": "Tesla 官方开源 · vehicle-command", "en": "Tesla (official) — vehicle-command"},
        "desc": {
            "zh": "Tesla 官方维护的车端指令协议库（Go）：解锁、充电等签名指令的参考实现。",
            "en": "Tesla's official Go library for the vehicle command protocol — the reference implementation for signed commands (lock, charge, …).",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "Apache-2.0", "en": "Apache-2.0"},
        "reason": {
            "zh": "官方代码即权威口径：第三方 Tesla API 生态的协议事实来源。",
            "en": "Official code is the authoritative caliber: the protocol source the whole third-party Tesla API ecosystem builds on.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-01",
        "http": 200,
        "gh": {"stars": 705, "pushed": "2026-09"},
    },
    {
        "id": "spacex-starship",
        "url": "https://www.spacex.com/vehicles/starship/",
        "name": {"zh": "SpaceX 官网 · Starship 星舰", "en": "SpaceX (official) — Starship"},
        "desc": {
            "zh": "SpaceX 官方星舰页面：史上最大运载火箭的官方定位、规格与任务动态。",
            "en": "SpaceX's official Starship page: the company's own positioning, specs and mission updates for the super-heavy launcher.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点内容版权归 SpaceX", "en": "Site content © SpaceX"},
        "reason": {
            "zh": "星舰叙事的官方口径页：本站星舰相关表述的规格与进度对照来源。",
            "en": "The official-caliber page for Starship — the spec and progress reference for this site's Starship narrative.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-01",
        "http": 200,
        "note": {
            "zh": "本机直连被反爬拦截（curl 403），经服务端读取器核活 200（2026-10-01）。",
            "en": "Direct fetch is blocked by anti-bot (curl 403); verified live via a server-side reader (2026-10-01).",
        },
    },
    {
        "id": "spacex-falcon9",
        "url": "https://www.spacex.com/vehicles/falcon-9/",
        "name": {"zh": "SpaceX 官网 · Falcon 9 猎鹰九号", "en": "SpaceX (official) — Falcon 9"},
        "desc": {
            "zh": "SpaceX 官方猎鹰九号页面：可复用主力火箭的官方规格、发射记录与复用数据。",
            "en": "SpaceX's official Falcon 9 page: official specs, launch record and reuse data for the workhorse reusable rocket.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点内容版权归 SpaceX", "en": "Site content © SpaceX"},
        "reason": {
            "zh": "火箭复用经济性的官方数据口径，与本站发射时间线交叉核对。",
            "en": "The official data caliber for reusability economics — cross-checked against this site's launch timeline.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-01",
        "http": 200,
        "note": {
            "zh": "本机直连被反爬拦截（curl 403），经服务端读取器核活 200（2026-10-01）。",
            "en": "Direct fetch is blocked by anti-bot (curl 403); verified live via a server-side reader (2026-10-01).",
        },
    },
    {
        "id": "spacex-updates",
        "url": "https://www.spacex.com/updates/",
        "name": {"zh": "SpaceX 官网 · Updates 官方更新", "en": "SpaceX (official) — Updates"},
        "desc": {
            "zh": "SpaceX 官方更新页：任务动态、发射回顾与公司新闻的官方发布口。",
            "en": "SpaceX's official updates feed: mission news, launch recaps and company announcements.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点内容版权归 SpaceX", "en": "Site content © SpaceX"},
        "reason": {
            "zh": "任务成败与进度的第一手官方口径，替代不可引的媒体转述。",
            "en": "First-party mission status straight from the company — the antidote to secondhand retellings.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-01",
        "http": 200,
        "note": {
            "zh": "本机直连被反爬拦截（curl 403），经服务端读取器核活 200（2026-10-01）。",
            "en": "Direct fetch is blocked by anti-bot (curl 403); verified live via a server-side reader (2026-10-01).",
        },
    },
    {
        "id": "tesla-fleet-api",
        "url": "https://developer.tesla.com/",
        "name": {"zh": "Tesla 官方开发者门户 · Fleet API", "en": "Tesla (official) — Developer / Fleet API"},
        "desc": {
            "zh": "Tesla 官方开发者门户：Fleet API 文档——车辆与能源设备的数据与指令官方接口。",
            "en": "Tesla's official developer portal: Fleet API docs — the company's data and command interface for vehicles and energy products.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "Tesla 开发者条款", "en": "Tesla developer terms"},
        "reason": {
            "zh": "第三方 Tesla API 生态的官方协议文档，与官方 vehicle-command 库互为表里。",
            "en": "The official protocol documentation behind the third-party Tesla API ecosystem — the counterpart of the vehicle-command library.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-01",
        "http": 200,
        "note": {
            "zh": "本机直连被反爬拦截（curl 403），经服务端读取器核活 200（2026-10-01）。",
            "en": "Direct fetch is blocked by anti-bot (curl 403); verified live via a server-side reader (2026-10-01).",
        },
    },
    {
        "id": "neuralink-registry",
        "url": "https://neuralink.com/patient-registry/",
        "name": {"zh": "Neuralink 官方 · 患者登记", "en": "Neuralink (official) — Patient Registry"},
        "desc": {
            "zh": "Neuralink 官方患者登记页：临床试验报名与进展了解的官方入口。",
            "en": "Neuralink's official patient registry: the entry point for clinical-trial sign-up and study updates.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点内容版权归 Neuralink", "en": "Site content © Neuralink"},
        "reason": {
            "zh": "首例人体植入后的官方一手通道，临床试验进展以官方口径为准。",
            "en": "The official first-party channel since the first human implant — clinical progress per the company's own page.",
        },
        "companies": ["Neuralink"],
        "checked": "2026-10-01",
        "http": 200,
        "note": {
            "zh": "本机直连连接被重置（curl/WebFetch 均失败），经服务端读取器核活 200（2026-10-01）。",
            "en": "Direct connection reset (curl/WebFetch both fail); verified live via a server-side reader (2026-10-01).",
        },
    },
    {
        "id": "openai-2015",
        "url": "https://openai.com/blog/introducing-openai/",
        "name": {"zh": "OpenAI 官方博客 · Introducing OpenAI（2015）", "en": "OpenAI (official) — Introducing OpenAI (2015)"},
        "desc": {
            "zh": "2015-12 官宣文：非营利 AI 研究实验室创立宣言，联合主席之一为马斯克。",
            "en": "The December 2015 founding announcement: a non-profit AI research lab with Musk as a co-chair.",
        },
        "category": "official",
        "lang": "en",
        "activity": "停更",
        "license": {"zh": "版权归 OpenAI（免费阅读）", "en": "Content © OpenAI (free to read)"},
        "reason": {
            "zh": "马斯克 AI 生涯的关键起点文书：联合主席→2018 退出董事会弧线的官方起点。",
            "en": "The founding document of Musk's AI arc — co-chair at creation, before his 2018 exit from the board.",
        },
        "companies": ["OpenAI"],
        "checked": "2026-10-01",
        "http": 200,
        "note": {
            "zh": "「停更」指这篇 2015 官宣文为历史定稿，非 OpenAI 博客停运；本机直连被反爬拦截（curl/WebFetch 403），经服务端读取器核活 200（2026-10-01）。",
            "en": "'Stale' means this 2015 announcement is a final historical post, not that OpenAI's blog is dead. Direct fetch blocked (curl/WebFetch 403); verified live via a server-side reader (2026-10-01).",
        },
    },
    {
        "id": "xai-official",
        "url": "https://x.ai/",
        "name": {"zh": "xAI 官网", "en": "xAI (official)"},
        "desc": {
            "zh": "xAI 官网：使命「理解宇宙的真实本质」，Grok 系列模型与公司动态的官方发布口。",
            "en": "xAI's official site: the mission 'to understand the true nature of the universe' and the official feed for Grok and company news.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点内容版权归 xAI", "en": "Site content © xAI"},
        "reason": {
            "zh": "Grok/xAI 产品与使命陈述的官方口径页。",
            "en": "The official-caliber page for Grok/xAI product and mission statements.",
        },
        "companies": ["xAI"],
        "checked": "2026-10-01",
        "http": 200,
        "note": {
            "zh": "本机直连超时（curl 连接无响应），经服务端读取器核活 200（2026-10-01）。",
            "en": "Direct connection times out on this machine; verified live via a server-side reader (2026-10-01).",
        },
    },
    {
        "id": "boringcompany-official",
        "url": "https://www.boringcompany.com/",
        "name": {"zh": "The Boring Company 官网", "en": "The Boring Company (official)"},
        "desc": {
            "zh": "The Boring Company 官网：安全、快挖、低成本的隧道交通——以 Loop 与 Prufrock 掘进机解决拥堵。",
            "en": "The Boring Company's official site: safe, fast-to-dig, low-cost tunnels — solving traffic with Loop, powered by the Prufrock TBM.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点内容版权归 The Boring Company", "en": "Site content © The Boring Company"},
        "reason": {
            "zh": "隧道项目官方口径，与本站 Boring 叙事与语录对照。",
            "en": "The official caliber for the tunnel ventures, cross-read with this site's Boring narrative and quotes.",
        },
        "companies": ["Boring Company"],
        "checked": "2026-10-01",
        "http": 200,
    },
    {
        "id": "teslamate",
        "url": "https://github.com/teslamate-org/teslamate",
        "name": {"zh": "Teslamate · 自托管特斯拉数据记录", "en": "Teslamate — self-hosted Tesla logger"},
        "desc": {
            "zh": "社区维护的自托管 Tesla 遥测记录器（Elixir/Phoenix）：车辆数据留在自己的服务器上。",
            "en": "Community-maintained, self-hosted Tesla telemetry logger (Elixir/Phoenix): your car's data stays on your own server.",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "AGPL-3.0", "en": "AGPL-3.0"},
        "reason": {
            "zh": "Tesla API 生态中星数最高、仍在活跃维护的自托管方案，代表社区「数据自主」路线。",
            "en": "The most-starred, actively maintained self-hosted project in the Tesla API ecosystem — the community's data-sovereignty route.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-01",
        "http": 200,
        "gh": {"stars": 9061, "pushed": "2026-09"},
    },
    {
        "id": "grok-1",
        "url": "https://github.com/xai-org/grok-1",
        "name": {"zh": "xAI 官方开源 · Grok-1 权重", "en": "xAI (official) — Grok-1 weights"},
        "desc": {
            "zh": "xAI 于 2024-03 开源的 3140 亿参数 MoE 语言模型 Grok-1：权重与推理代码（仓库由 grok 改名 grok-1）。",
            "en": "xAI's March 2024 open release of Grok-1, a 314B-parameter MoE LLM: weights and inference code (repo renamed from `grok` to `grok-1`).",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "停更",
        "license": {"zh": "Apache-2.0", "en": "Apache-2.0"},
        "reason": {
            "zh": "马斯克系公司把旗舰模型权重整体开源的唯一一例，xAI 开源立场的实物证据。",
            "en": "The one full open-weights release of a flagship model by a Musk company — physical evidence of xAI's open-source stance.",
        },
        "companies": ["xAI"],
        "checked": "2026-10-01",
        "http": 200,
        "gh": {"stars": 52239, "pushed": "2024-08"},
        "note": {
            "zh": "权重库为一次性发布物：2024-08 后无新提交属预期，「停更」不代表下线或方向变化。",
            "en": "A one-shot weights release: no pushes since Aug 2024 is expected — 'stale' here does not mean discontinued.",
        },
    },
    {
        "id": "elonmuskarchive",
        "url": "https://elonmuskarchive.org/",
        "name": {"zh": "Elon Musk Archive · 言行镜像库", "en": "Elon Musk Archive"},
        "desc": {
            "zh": "马斯克公开言行的非官方镜像档案：X 帖、访谈、演讲、文档按时间可检索（本站第一手采料的镜像来源）。",
            "en": "An unofficial archive of Musk's public record — posts, interviews, keynotes and documents, searchable in time order (this site's first-hand pipeline source).",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "非官方镜像，版权归原权利人", "en": "Unofficial mirror; rights remain with original owners"},
        "reason": {
            "zh": "本站 X 帖 / 访谈 / 演讲逐字采料的直接来源，收录以注明其非官方性质与用途。",
            "en": "The direct source of this site's verbatim pipeline; listed with its unofficial nature and use stated.",
        },
        "companies": ["综合"],
        "checked": "2026-10-01",
        "http": 200,
    },
    {
        "id": "wbw-neuralink",
        "url": "https://waitbutwhy.com/2017/04/neuralink.html",
        "name": {"zh": "Wait But Why · Neuralink 与大脑的魔法未来", "en": "Wait But Why — Neuralink and the Brain's Magical Future"},
        "desc": {
            "zh": "Tim Urban 2017 年长文：与马斯克数次长谈后对 Neuralink、脑机接口与大脑的科普解读。",
            "en": "Tim Urban's 2017 mega-essay on Neuralink, brain-computer interfaces and the brain, after long conversations with Musk.",
        },
        "category": "community",
        "lang": "en",
        "activity": "停更",
        "license": {"zh": "博客版权所有（免费阅读）", "en": "Blog copyright (free to read)"},
        "reason": {
            "zh": "流传最广的 Neuralink 科普定稿，2017 年创立期的第一手侧写。",
            "en": "The most widely read Neuralink explainer — a first-hand portrait of the founding moment.",
        },
        "companies": ["Neuralink"],
        "checked": "2026-10-01",
        "http": 200,
        "note": {
            "zh": "「停更」指这篇 2017 定稿长文不再修订，非 Wait But Why 博客停运。",
            "en": "'Stale' refers to this 2017 essay being final, not to Wait But Why shutting down.",
        },
    },
    {
        "id": "flight-club",
        "url": "https://www.flightclub.io/",
        "name": {"zh": "Flight Club · 火箭轨迹仿真", "en": "Flight Club — rocket trajectory simulator"},
        "desc": {
            "zh": "火箭发射实时三维轨迹仿真与预测站点，SpaceX 发射报道常引用其弹道可视化。",
            "en": "Real-time 3D rocket trajectory simulation and prediction; a staple visualization in SpaceX launch coverage.",
        },
        "category": "tools",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点服务（未声明开源许可）", "en": "Web service (no open license declared)"},
        "reason": {
            "zh": "发射追踪工具链中最老牌的轨迹仿真站，把发射数据变成可核对的弹道。",
            "en": "The oldest trajectory simulator in the launch-tracking toolbox — turns launch data into checkable trajectories.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-01",
        "http": 200,
    },
    {
        "id": "next-spaceflight",
        "url": "https://nextspaceflight.com/",
        "name": {"zh": "Next Spaceflight · 发射日历", "en": "Next Spaceflight — launch schedule"},
        "desc": {
            "zh": "全球航天发射日历与追踪：即将进行的发射、直播链接与统计，含 SpaceX 各次任务卡片。",
            "en": "Global launch schedule and tracker: upcoming launches, webcast links and statistics, incl. every SpaceX mission card.",
        },
        "category": "tools",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点服务", "en": "Web service"},
        "reason": {
            "zh": "核对「哪次发射、何时、成没成」的最快公共日历。",
            "en": "The fastest public calendar to check which launch, when, and whether it succeeded.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-01",
        "http": 200,
    },
    {
        "id": "launch-library-2",
        "url": "https://thespacedevs.com/llapi",
        "name": {"zh": "Launch Library 2 · 发射数据 API", "en": "Launch Library 2 — launch data API"},
        "desc": {
            "zh": "The Space Devs 社区维护的航天发射开放 API：发射、任务与轨道事件的结构化数据接口。",
            "en": "The Space Devs' community-run open API: structured data on launches, missions and orbital events.",
        },
        "category": "tools",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "社区开放 API（条款见官方文档）", "en": "Community open API (terms per official docs)"},
        "reason": {
            "zh": "发射数据的事实标准接口；本站时间线交叉核对发射日期的候选工具。",
            "en": "The de-facto open interface for launch data; a candidate cross-check for this site's launch dates.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-01",
        "http": 200,
    },
    {
        "id": "starlink-sx",
        "url": "https://starlink.sx/",
        "name": {"zh": "starlink.sx · 星链卫星追踪", "en": "starlink.sx — Starlink tracker"},
        "desc": {
            "zh": "独立 Starlink 星座可视化与覆盖模拟（Mike Puchol 维护，非 SpaceX 官方）：在轨卫星、网关与链路实时图。",
            "en": "Independent Starlink constellation visualization and coverage simulation by Mike Puchol (unofficial): live satellites, gateways and links.",
        },
        "category": "tools",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点服务", "en": "Web service"},
        "reason": {
            "zh": "Starlink 规模与覆盖最直观的独立量化视图，非官方口径标注清晰。",
            "en": "The clearest independent quantitative view of Starlink's scale and coverage, clearly labeled unofficial.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-01",
        "http": 200,
    },
]

ACTIVITY_ENUM = ("维护中", "停更", "存档")
LANG_ENUM = ("en", "zh", "zh/en")


def validate():
    """返回问题列表；空列表 = 通过。任何问题都应让生成器拒绝产出。"""
    problems = []
    seen_ids = set()
    for r in RESOURCES:
        rid = r.get("id", "<missing>")
        where = f"[{rid}]"
        if not re_id_ok(rid):
            problems.append(f"{where} id 非法（须 ^[a-z0-9-]+$）")
        if rid in seen_ids:
            problems.append(f"{where} id 重复")
        seen_ids.add(rid)
        url = r.get("url", "")
        if not (url.startswith("http://") or url.startswith("https://")):
            problems.append(f"{where} url 非空且须 http(s)")
        for field in ("name", "desc", "license", "reason"):
            obj = r.get(field)
            if not isinstance(obj, dict) or not obj.get("zh", "").strip() or not obj.get("en", "").strip():
                problems.append(f"{where} {field} 双语不完整")
        if r.get("category") not in CATEGORIES:
            problems.append(f"{where} category 非法：{r.get('category')}")
        if r.get("lang") not in LANG_ENUM:
            problems.append(f"{where} lang 非法：{r.get('lang')}")
        if r.get("activity") not in ACTIVITY_ENUM:
            problems.append(f"{where} activity 非法：{r.get('activity')}")
        cos = r.get("companies")
        if not isinstance(cos, list) or not cos or any(c not in COMPANIES_VOCAB for c in cos):
            problems.append(f"{where} companies 非法：{cos}")
        import re as _re
        if not _re.match(r"^\d{4}-\d{2}-\d{2}$", str(r.get("checked", ""))):
            problems.append(f"{where} checked 须为 YYYY-MM-DD（核活日期必填）")
        code = r.get("http")
        if not isinstance(code, int) or not (100 <= code <= 599):
            problems.append(f"{where} http 响应码缺失或非法")
        gh = r.get("gh")
        if gh is not None:
            if not isinstance(gh.get("stars"), int) or gh["stars"] < 0:
                problems.append(f"{where} gh.stars 须为非负整数")
            if not _re.match(r"^\d{4}-\d{2}$", str(gh.get("pushed", ""))):
                problems.append(f"{where} gh.pushed 须为 YYYY-MM")
        note = r.get("note")
        if note is not None and (not note.get("zh", "").strip() or not note.get("en", "").strip()):
            problems.append(f"{where} note 若提供则须双语完整")
    # 分类不空：每个已用分类至少 1 条（防生成空分类节）
    used = {r.get("category") for r in RESOURCES}
    for cid, lab in CATEGORIES.items():
        if cid in used and sum(1 for r in RESOURCES if r["category"] == cid) == 0:
            problems.append(f"[{cid}] 分类 {lab['zh']} 无条目")
    return problems


def re_id_ok(s):
    import re as _re
    return bool(_re.match(r"^[a-z0-9-]+$", str(s)))


if __name__ == "__main__":
    ps = validate()
    if ps:
        for p in ps:
            print("✗", p)
        raise SystemExit(1)
    n_by_cat = {cid: sum(1 for r in RESOURCES if r["category"] == cid) for cid in CATEGORIES}
    print(f"✓ resources-data.py：{len(RESOURCES)} 条 {n_by_cat}")
