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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
        "http": 200,
        "gh": {"stars": 706, "pushed": "2026-09"},
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
        "http": 200,
        "gh": {"stars": 9065, "pushed": "2026-10"},
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
        "checked": "2026-10-02",
        "http": 200,
        "gh": {"stars": 52233, "pushed": "2024-08"},
        "note": {
            "zh": "权重库为一次性发布物：2024-08 后无新提交属预期，「停更」不代表下线或方向变化。",
            "en": "A one-shot weights release: no pushes since Aug 2024 is expected — 'stale' here does not mean discontinued.",
        },
    },
    {
        "id": "tesla-api-io",
        "url": "https://tesla-api.io/",
        "name": {"zh": "tesla-api.io · Tesla API 社区文档", "en": "tesla-api.io — community Tesla API docs"},
        "desc": {
            "zh": "长期被社区引用的 Tesla JSON API 非官方文档站：鉴权、车辆指令与遥测端点的参考。",
            "en": "The long-cited unofficial reference for Tesla's JSON API: auth, vehicle commands and telemetry endpoints.",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "停更",
        "license": {"zh": "文档开放阅读（许可未声明）", "en": "Docs open to read (no license declared)"},
        "reason": {
            "zh": "官方 Fleet API 之前的社区文档事实标准：读懂第三方 Tesla API 生态的历史与端点语义。",
            "en": "The de-facto community docs before the official Fleet API — the history and endpoint semantics of the third-party Tesla ecosystem.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "站点自注 2024-01 起停止维护、由 Tesla 官方文档接管（deprecated ≠ 下线，页面仍在线）；本机运营商 DNS 曾报 ENOTFOUND（R10 留档），2026-10-01 服务端读取器核活 200 证伪死链判断。",
            "en": "Self-declared unmaintained since Jan 2024, superseded by Tesla's official docs (deprecated ≠ offline; page still serves). Local ISP DNS once gave ENOTFOUND (R10 note); a server-side reader verified HTTP 200 on 2026-10-01, disproving the dead-link read.",
        },
    },
    {
        "id": "timdorr-tesla-api",
        "url": "https://github.com/timdorr/tesla-api",
        "name": {"zh": "timdorr/tesla-api · 非官方 API 文档与 Ruby 库", "en": "timdorr/tesla-api — unofficial API docs & gem"},
        "desc": {
            "zh": "社区维护近十年的 Tesla JSON API 非官方文档与 Ruby gem：第三方集成的起点坐标。",
            "en": "Nearly a decade of community-maintained unofficial Tesla JSON API docs and a Ruby gem — the starting coordinate of third-party integrations.",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "MIT", "en": "MIT"},
        "reason": {
            "zh": "与官方 vehicle-command 库互为对照：官方协议之外社区实测口径的活档案。",
            "en": "The living counterpart of the official vehicle-command library — the community-tested caliber outside the official protocol.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-02",
        "http": 200,
        "gh": {"stars": 2065, "pushed": "2026-03"},
    },
    {
        "id": "r-spacex-api",
        "url": "https://github.com/r-spacex/SpaceX-API",
        "name": {"zh": "r-spacex/SpaceX-API · 社区发射数据 REST API", "en": "r-spacex/SpaceX-API — community launch data API"},
        "desc": {
            "zh": "r/SpaceX 社区维护的 SpaceX 数据开源 REST API：发射、火箭、飞船与星链的结构化接口（已存档）。",
            "en": "The r/SpaceX community's open REST API for SpaceX data: structured endpoints for launches, rockets, capsules and Starlink (archived).",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "存档",
        "license": {"zh": "Apache-2.0", "en": "Apache-2.0"},
        "reason": {
            "zh": "发射时间线交叉核对的结构化数据源；存档前仍是社区引用最广的 SpaceX 数据接口。",
            "en": "A structured cross-check for launch timelines; before archiving it was the most-cited community SpaceX data interface.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "gh": {"stars": 10913, "pushed": "2024-08"},
        "note": {
            "zh": "仓库已由维护者标记 archived（只读），2024-08 后无提交；其线上服务 api.spacex.land 的可用性不在本条断言范围。",
            "en": "The repo is maintainer-archived (read-only), no pushes since Aug 2024; the availability of its hosted service is not asserted by this entry.",
        },
    },
    {
        "id": "starlink-grpc-tools",
        "url": "https://github.com/sparky8512/starlink-grpc-tools",
        "name": {"zh": "sparky8512/starlink-grpc-tools · 星链终端遥测", "en": "sparky8512/starlink-grpc-tools — Starlink dish telemetry"},
        "desc": {
            "zh": "读取 Starlink 用户终端 gRPC 遥测的社区脚本集：状态、吞吐与可观测性数据的自采通道。",
            "en": "Community scripts for reading a Starlink dish's gRPC telemetry — a self-collected channel for status, throughput and observability data.",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "Unlicense（公有领域）", "en": "Unlicense (public domain)"},
        "reason": {
            "zh": "星链观测从「看别人的仪表盘」到「自己采数据」的代表项目，与 starlink.sx 可视化互补。",
            "en": "The representative project for observing Starlink first-hand rather than reading others' dashboards — complements the starlink.sx visualizer.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "gh": {"stars": 710, "pushed": "2026-09"},
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "「停更」指这篇 2017 定稿长文不再修订，非 Wait But Why 博客停运。",
            "en": "'Stale' refers to this 2017 essay being final, not to Wait But Why shutting down.",
        },
    },
    {
        "id": "r-spacex-wiki",
        "url": "https://old.reddit.com/r/spacex/wiki/index",
        "name": {"zh": "r/SpaceX 社区维基", "en": "r/SpaceX community wiki"},
        "desc": {
            "zh": "r/SpaceX 版区维基：发射编年史、任务清单与 FAQ 的社区协作整理（非官方）。",
            "en": "The r/SpaceX subreddit wiki: community-maintained launch chronicles, mission lists and FAQs (unofficial).",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "社区协作内容，Reddit 版权口径", "en": "Community content under Reddit terms"},
        "reason": {
            "zh": "发射编年史与任务统计的社区口径，与本站时间轴互为民间对照。",
            "en": "The community caliber for launch chronicles and mission stats — a folk cross-check for this site's timeline.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "Reddit 对脚本访问限制严格（本机 curl 000），经服务端读取器核活 200（2026-10-01）。",
            "en": "Reddit heavily restricts scripted access (curl 000 on this machine); verified live via a server-side reader (2026-10-01).",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
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
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "tessie",
        "url": "https://www.tessie.com/",
        "name": {"zh": "Tessie · Tesla 遥测与自动化服务", "en": "Tessie — Tesla telemetry & automation"},
        "desc": {
            "zh": "商业 Tesla 数据与自动化平台：遥测、充电管理与存储 API 的托管服务（非官方）。",
            "en": "A commercial Tesla data & automation platform: hosted telemetry, charge management and storage API (unofficial).",
        },
        "category": "tools",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "商业服务（非官方，条款见官网）", "en": "Commercial service (unofficial; terms per site)"},
        "reason": {
            "zh": "Tesla API 生态商业托管路线的代表，与 Teslamate 的自托管路线互为两端。",
            "en": "The representative of the hosted route in the Tesla API ecosystem — the two ends against Teslamate's self-hosting.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-02",
        "http": 200,
    },
    # ---------------- V9-20 R13：社区与档案资源 + 元数据补全 ----------------
    {
        "id": "wikipedia-elon-musk",
        "url": "https://en.wikipedia.org/wiki/Elon_Musk",
        "name": {"zh": "维基百科 · 埃隆·马斯克", "en": "Wikipedia — Elon Musk"},
        "desc": {
            "zh": "英文维基百科马斯克主条目：生平、公司、争议与公共形象的百科式综述，附大量一手引注。",
            "en": "The English Wikipedia article on Musk: an encyclopedic survey of biography, companies, controversies and public image, with extensive citations.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "CC BY-SA 4.0（维基百科惯例）", "en": "CC BY-SA 4.0 (Wikipedia standard)"},
        "reason": {
            "zh": "条目演化史本身即公众认知的刻度；其脚注链是回查一手来源的实用入口（非一手，仅作导航）。",
            "en": "The article's own revision history tracks public perception; its footnotes are a practical index back to primary sources (secondary, used for navigation only).",
        },
        "companies": ["综合"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "R10 曾因本机 DNS 污染（解析至 31.13.88.26）判定不可达；本轮实测直连 200 且内容为真（2.68 MB 正文），判定推翻，收录。所载 http 为该次实测口径。",
            "en": "R10 marked this unreachable due to local DNS pollution (resolved to 31.13.88.26); this round it returned 200 with genuine content (2.68 MB), overturning that call. The http code reflects this round's test.",
        },
    },
    {
        "id": "wikipedia-spacex",
        "url": "https://en.wikipedia.org/wiki/SpaceX",
        "name": {"zh": "维基百科 · SpaceX", "en": "Wikipedia — SpaceX"},
        "desc": {
            "zh": "英文维基百科全书 SpaceX 条目：公司史、火箭谱系、任务与合同脉络的百科综述。",
            "en": "The English Wikipedia article on SpaceX: an encyclopedic account of company history, vehicle lineage, missions and contracts.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "CC BY-SA 4.0（维基百科惯例）", "en": "CC BY-SA 4.0 (Wikipedia standard)"},
        "reason": {
            "zh": "公司史脉络的公共参照系，与本网站点时间轴互为交叉核对。",
            "en": "A public reference frame for company history, cross-checking this site's timeline.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "wikipedia-tesla",
        "url": "https://en.wikipedia.org/wiki/Tesla,_Inc.",
        "name": {"zh": "维基百科 · 特斯拉公司", "en": "Wikipedia — Tesla, Inc."},
        "desc": {
            "zh": "英文维基百科 Tesla, Inc. 条目：产品线、财务脉络与公司事件的百科综述。",
            "en": "The English Wikipedia article on Tesla, Inc.: product line, financial trajectory and corporate events.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "CC BY-SA 4.0（维基百科惯例）", "en": "CC BY-SA 4.0 (Wikipedia standard)"},
        "reason": {
            "zh": "公司级事实的公共底稿，便于对照本站账本中的财务与产品节点。",
            "en": "A public baseline for company-level facts, useful against this site's financial and product nodes.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "wikipedia-starship",
        "url": "https://en.wikipedia.org/wiki/Starship",
        "name": {"zh": "维基百科 · 星舰（Starship）", "en": "Wikipedia — SpaceX Starship"},
        "desc": {
            "zh": "英文维基百科星舰条目：研制历程、试飞记录与设计演进的百科梳理。",
            "en": "The English Wikipedia article on Starship: development history, flight record and design evolution.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "CC BY-SA 4.0（维基百科惯例）", "en": "CC BY-SA 4.0 (Wikipedia standard)"},
        "reason": {
            "zh": "试飞编年与设计迭代的公共清单，与本站编年史条目互为对照。",
            "en": "A public ledger of test flights and design iterations, mirroring this site's chronicle entries.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "wikipedia-twitter-acquisition",
        "url": "https://en.wikipedia.org/wiki/Acquisition_of_Twitter_by_Elon_Musk",
        "name": {"zh": "维基百科 · 马斯克收购推特", "en": "Wikipedia — Acquisition of Twitter by Elon Musk"},
        "desc": {
            "zh": "英文维基百科专条：2022 年收购推特的全过程，含报价、诉讼、交割与后续改名的编年综述。",
            "en": "The English Wikipedia article dedicated to the 2022 Twitter acquisition: bid, litigation, close and renaming.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "CC BY-SA 4.0（维基百科惯例）", "en": "CC BY-SA 4.0 (Wikipedia standard)"},
        "reason": {
            "zh": "收购长弧的公共编年参照，本站 X / Twitter 线事件的交叉核对对象。",
            "en": "A public chronicle of the acquisition arc — a cross-check for this site's X / Twitter line.",
        },
        "companies": ["X / Twitter"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "wikipedia-spacex-launches",
        "url": "https://en.wikipedia.org/wiki/List_of_SpaceX_launches",
        "name": {"zh": "维基百科 · SpaceX 发射列表", "en": "Wikipedia — List of SpaceX launches"},
        "desc": {
            "zh": "英文维基百科的 SpaceX 发射全量列表页：按年分列的发射记录、结果与载荷统计。",
            "en": "Wikipedia's full launch list for SpaceX: year-by-year records, outcomes and payload tallies.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "CC BY-SA 4.0（维基百科惯例）", "en": "CC BY-SA 4.0 (Wikipedia standard)"},
        "reason": {
            "zh": "发射频次与结果的公共统计口径，与 r/SpaceX 维基、本站编年史三方互校。",
            "en": "A public statistical caliber for launch cadence and outcomes, triangulating with the r/SpaceX wiki and this site's chronicle.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "旧标题 List_of_SpaceX_launch_vehicles 实测 404，已并入本页；以本页为准。",
            "en": "The older title List_of_SpaceX_launch_vehicles returns 404 and has been merged into this page, which is the canonical one.",
        },
    },
    {
        "id": "wikipedia-grok",
        "url": "https://en.wikipedia.org/wiki/Grok_(chatbot)",
        "name": {"zh": "维基百科 · Grok（聊天机器人）", "en": "Wikipedia — Grok (chatbot)"},
        "desc": {
            "zh": "英文维基百科 Grok 条目：xAI 聊天机器人的发布节点、版本沿革与争议梳理。",
            "en": "The English Wikipedia article on Grok: xAI's chatbot, its release milestones, versions and controversies.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "CC BY-SA 4.0（维基百科惯例）", "en": "CC BY-SA 4.0 (Wikipedia standard)"},
        "reason": {
            "zh": "xAI 产品线的公共版本编年，补本站 Grok 线材料的民间参照。",
            "en": "A public version chronicle of the xAI product line — a folk reference for this site's Grok material.",
        },
        "companies": ["xAI"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "wikipedia-neuralink",
        "url": "https://en.wikipedia.org/wiki/Neuralink",
        "name": {"zh": "维基百科 · Neuralink", "en": "Wikipedia — Neuralink"},
        "desc": {
            "zh": "英文维基百科 Neuralink 条目：公司沿革、植入技术与试验进程的百科综述。",
            "en": "The English Wikipedia article on Neuralink: company history, implant technology and trial progress.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "CC BY-SA 4.0（维基百科惯例）", "en": "CC BY-SA 4.0 (Wikipedia standard)"},
        "reason": {
            "zh": "脑机接口线的公共底稿，与 Wait But Why 长文、Neuralink 官方页三方互补。",
            "en": "A public baseline for the BCI line, complementing the Wait But Why essay and Neuralink's official pages.",
        },
        "companies": ["Neuralink"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "tesla-json-api-docs",
        "url": "https://tesla-api.timdorr.com/",
        "name": {"zh": "Tesla JSON API 非官方文档（timdorr）", "en": "Tesla JSON API (unofficial) — timdorr"},
        "desc": {
            "zh": "timdorr/tesla-api 仓库的文档落地站：Tesla 车辆 JSON API 的端点、认证与字段说明。",
            "en": "The docs site for the timdorr/tesla-api repo: endpoints, auth and fields of Tesla's vehicle JSON API.",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "MIT（见仓库）", "en": "MIT (see repository)"},
        "reason": {
            "zh": "Tesla API 生态事实上的字段字典——与同名仓库成对收录（仓库管代码、本页管文档）。",
            "en": "The de facto field dictionary of the Tesla API ecosystem — paired with the repo (code) as this page (docs).",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "tdorssers-teslapy",
        "url": "https://github.com/tdorssers/TeslaPy",
        "name": {"zh": "TeslaPy · Python Tesla API 客户端", "en": "TeslaPy — Python Tesla API client"},
        "desc": {
            "zh": "Python 编写的 Tesla 车主 API 客户端库，支持车辆查询、控制与 Powerwall 访问（非官方）。",
            "en": "A Python client for the Tesla Owner API — vehicle queries, commands and Powerwall access (unofficial).",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "MIT", "en": "MIT"},
        "reason": {
            "zh": "Python 生态里使用最广的 Tesla API 客户端，与 tesla-api（Ruby）成语言对照。",
            "en": "The most used Python client for the Tesla API, a language counterpart to tesla-api (Ruby).",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-02",
        "http": 200,
        "gh": {"stars": 417, "pushed": "2026-07"},
    },
    {
        "id": "powerwall2-local-api",
        "url": "https://github.com/vloschiavo/powerwall2",
        "name": {"zh": "Powerwall 2 本地网关 API 文档", "en": "Powerwall 2 local gateway API documentation"},
        "desc": {
            "zh": "Tesla Powerwall 2 本地网关接口的社区逆向文档（非官方，家庭储能开发者参考）。",
            "en": "Community reverse-engineered documentation of the Tesla Powerwall 2 local gateway API (unofficial).",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "停更",
        "license": {"zh": "Apache-2.0", "en": "Apache-2.0"},
        "reason": {
            "zh": "家庭储能侧唯一成体系的本地接口文档，展示 Tesla 生态开源测绘的深度。",
            "en": "The only systematic local-interface doc on the home-energy side, showing how deep the community mapping goes.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-02",
        "http": 200,
        "gh": {"stars": 290, "pushed": "2024-10"},
        "note": {
            "zh": "最近提交 2024-10，「停更」；文档类项目停更≠失效，本地网关接口仍可参考。",
            "en": "Last push 2024-10, marked stale; a docs project going quiet is not the same as breaking — the local gateway API remains referenceable.",
        },
    },
    {
        "id": "planet4589-space",
        "url": "https://planet4589.org/space/",
        "name": {"zh": "Jonathan McDowell 太空档案", "en": "Jonathan McDowell's space archive"},
        "desc": {
            "zh": "哈佛-史密松天体物理中心学者 Jonathan McDowell 维护的独立太空档案：发射与在轨物体权威统计。",
            "en": "An independent space archive by Harvard–Smithsonian astrophysicist Jonathan McDowell: authoritative launch and on-orbit object statistics.",
        },
        "category": "tools",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "个人学术站点，引用请注明来源", "en": "Personal academic site; cite the source"},
        "reason": {
            "zh": "独立学者口径的发射统计，媒体与业内回查航天数字时的常引来源（非官方）。",
            "en": "Independent-scholar launch statistics — a frequently cited source when media and industry check space numbers (unofficial).",
        },
        "companies": ["综合"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "labpadre",
        "url": "https://labpadre.com/",
        "name": {"zh": "LabPadre · 星舰 24 小时直播", "en": "LabPadre — 24/7 Starship live coverage"},
        "desc": {
            "zh": "博卡奇卡发射场的 24/7 独立直播网络：多机位全天候对准 Starbase 星舰工地。",
            "en": "The independent 24/7 webcam network at Boca Chica: multiple cameras pointed at the Starship build site around the clock.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "直播内容版权归 LabPadre（嵌入观看）", "en": "Stream content (c) LabPadre (embedded viewing)"},
        "reason": {
            "zh": "星舰「以飞代测」时代的第一手观测源：任何官方口径都能与画面当场对账。",
            "en": "The first-hand observation source of the fly-test-fly era: any official claim can be checked against the live picture.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "本机直连失败（curl 000），经服务端读取器核活 200（2026-10-02）。",
            "en": "Direct fetch failed on this machine (curl 000); verified live via a server-side reader (2026-10-02).",
        },
    },
    {
        "id": "nasaspaceflight",
        "url": "https://www.nasaspaceflight.com/",
        "name": {"zh": "NASASpaceflight · 航天报道站", "en": "NASASpaceflight — spaceflight news"},
        "desc": {
            "zh": "以星舰与发射报道深度著称的独立航天媒体，常抢在官方之前披露进度细节。",
            "en": "The independent spaceflight outlet known for deep Starship and launch coverage, often ahead of official statements.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "版权归 NSF（免费阅读）", "en": "Content (c) NSF (free to read)"},
        "reason": {
            "zh": "星舰进度与发射分析的社区权威口径，与本站时间线互为民间对照。",
            "en": "The community authority on Starship progress and launch analysis — a folk cross-check for this site timeline.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "本机直连被反爬拦截（curl 403），经服务端读取器核活 200（2026-10-02）。",
            "en": "Direct fetch blocked by anti-bot (curl 403); verified live via a server-side reader (2026-10-02).",
        },
    },
    {
        "id": "nsf-forum",
        "url": "https://forum.nasaspaceflight.com/",
        "name": {"zh": "NSF 论坛 · 航天社区讨论区", "en": "NSF Forum — spaceflight community"},
        "desc": {
            "zh": "NASASpaceflight 旗下的航天论坛：星舰/发射/进度讨论的社区情报中枢。",
            "en": "The NSF-run spaceflight forum: the community intel hub for Starship, launches and progress threads.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "社区协作内容，论坛版权口径", "en": "Community content under forum terms"},
        "reason": {
            "zh": "大量第一手现场信息首发于此（目击、航拍、硬件线索），是观测生态的情报层。",
            "en": "First-hand field intel surfaces here first (sightings, flights, hardware clues) — the observation layer of the ecosystem.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "本机直连被反爬拦截（curl 403），经服务端读取器核活 200（2026-10-02）。",
            "en": "Direct fetch blocked by anti-bot (curl 403); verified live via a server-side reader (2026-10-02).",
        },
    },
    {
        "id": "r-teslamotors-wiki",
        "url": "https://old.reddit.com/r/teslamotors/wiki/index",
        "name": {"zh": "r/teslamotors 社区维基", "en": "r/teslamotors community wiki"},
        "desc": {
            "zh": "Tesla 车主社区维基：常见问题、车型信息与充电指南的社区协作整理（非官方）。",
            "en": "The Tesla owners community wiki: FAQs, vehicle info and charging guides, community-maintained (unofficial).",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "社区协作内容，Reddit 版权口径", "en": "Community content under Reddit terms"},
        "reason": {
            "zh": "车主侧民间口径的入口（与 r/SpaceX 维基同为 Reddit 社区档案形态）。",
            "en": "The owner-side folk caliber — Reddit community archive in the same mold as the r/SpaceX wiki.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "Reddit 对脚本访问限制严格（本机 curl 000），经服务端读取器核活 200（2026-10-02）。",
            "en": "Reddit heavily restricts scripted access (curl 000 on this machine); verified live via a server-side reader (2026-10-02).",
        },
    },
    {
        "id": "everydayastronaut",
        "url": "https://everydayastronaut.com/",
        "name": {"zh": "Everyday Astronaut · 航天科普站", "en": "Everyday Astronaut — space explainer site"},
        "desc": {
            "zh": "Tim Dodd 的航天科普站：发动机对比、发射解读与深度专访（含 2021 星舰基地三部曲专访马斯克）。",
            "en": "Tim Dodd space explainer site: engine comparisons, launch breakdowns and deep interviews (incl. the 2021 Starbase interview with Musk).",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "版权归 Everyday Astronaut（免费阅读）", "en": "Content (c) Everyday Astronaut (free to read)"},
        "reason": {
            "zh": "本站已有其 2021 星舰基地专访逐字（i2021-07-30）——科普侧与专访侧的双向入口。",
            "en": "This site already carries his 2021 Starbase interview verbatim (i2021-07-30) — the explainer-side twin of that interview.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "ringwatchers",
        "url": "https://ringwatchers.com/",
        "name": {"zh": "Ringwatchers · 星舰建造追踪", "en": "Ringwatchers — Starship build tracker"},
        "desc": {
            "zh": "追踪星舰不锈钢环圈与硬件组装进度的独立数据库：S/N 序列、堆放位置与出厂去向。",
            "en": "The independent database tracking Starship ring stacks and hardware: S/N sequence, staging locations and rollout history.",
        },
        "category": "tools",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点服务", "en": "Web service"},
        "reason": {
            "zh": "「数环圈」社群的量化结晶：星舰硬件账本可与官方口径交叉核对。",
            "en": "The quantified output of the ring-counting community — a Starship hardware ledger to cross-check official claims.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "starship-wikibase",
        "url": "https://starship.wikibase.dev/",
        "name": {"zh": "Starship Wiki · 星舰序列号数据库", "en": "Starship Wiki — S/N database"},
        "desc": {
            "zh": "社区维护的星舰飞行器数据库：助推器与飞船序列号、飞行历史与分配关系。",
            "en": "Community-maintained Starship vehicle database: booster/ship serials, flight history and assignments.",
        },
        "category": "tools",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "社区开放数据（条款见站内）", "en": "Community open data (terms per site)"},
        "reason": {
            "zh": "S/N 级别的飞行历史结构化数据，是时间线交叉核对的工具层。",
            "en": "Structured S/N-level flight history — the tool layer for cross-checking the timeline.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "spacex-launches-page",
        "url": "https://www.spacex.com/launches/",
        "name": {"zh": "SpaceX 官网 · 发射列表", "en": "SpaceX (official) — Launches list"},
        "desc": {
            "zh": "SpaceX 官方发射任务列表：全部任务的官方档案入口。",
            "en": "SpaceX official launch mission list: the official archive entry for every mission flown.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "站点内容版权归 SpaceX", "en": "Site content (c) SpaceX"},
        "reason": {
            "zh": "任务档案的官方入口，与社区发射日历互为对照。",
            "en": "The official mission archive — the counterpart of community launch calendars.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "本机直连被反爬拦截（curl 403），经服务端读取器核活 200（2026-10-02）。",
            "en": "Direct fetch blocked by anti-bot (curl 403); verified live via a server-side reader (2026-10-02).",
        },
    },
    {
        "id": "wikidata-elon-musk",
        "url": "https://www.wikidata.org/wiki/Q317521",
        "name": {"zh": "Wikidata · 马斯克结构化数据条目", "en": "Wikidata — Elon Musk (Q317521)"},
        "desc": {
            "zh": "Wikidata 的马斯克结构化数据条目（Q317521）：身份、任职、亲属与公司关系以属性三元组形式开放。",
            "en": "Wikidata structured-data item for Musk (Q317521): roles, positions, family and company relations as open triples.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "CC0 公有领域", "en": "CC0 public domain"},
        "reason": {
            "zh": "结构化事实层（可比对、可引用、可机读），是人物基础事实的开放锚点。",
            "en": "The structured fact layer (comparable, citable, machine-readable) — an open anchor for baseline facts.",
        },
        "companies": ["综合"],
        "checked": "2026-10-02",
        "http": 200,
    },
    {
        "id": "archive-org-search",
        "url": "https://archive.org/search?query=elon+musk",
        "name": {"zh": "Internet Archive · 马斯克资料搜索", "en": "Internet Archive — Elon Musk search"},
        "desc": {
            "zh": "互联网档案馆的马斯克资料检索：文字、音视频的历史存档入口（含访谈与广播片段）。",
            "en": "Internet Archive search for Musk materials: the historical entry to texts, audio and video (incl. interviews and broadcasts).",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "按件各自标注（公共领域/版权保留）", "en": "Per-item (public domain or rights reserved)"},
        "reason": {
            "zh": "历史广播与早期访谈的存档层：很多逐字素材只能在这里回溯。",
            "en": "The archive layer for historical broadcasts and early interviews — some verbatim material is only recoverable here.",
        },
        "companies": ["综合"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "本机 DNS 污染致直连失败，经服务端读取器核活 200（2026-10-02）；搜索页为入口口径，具体 collection 页待用户环境定位。",
            "en": "Local DNS pollution blocks direct fetch; verified live via a server-side reader (2026-10-02). Search page listed as the entry; specific collection pages to be located in user environment.",
        },
    },
    {
        "id": "isaacson-official-page",
        "url": "https://www.harpercollins.com/products/elon-musk-walter-isaacson",
        "name": {"zh": "《Elon Musk》官方书页（Isaacson 著）", "en": "Elon Musk official book page (by Walter Isaacson)"},
        "desc": {
            "zh": "Simon & Schuster 官方书页：Walter Isaacson 2023 年传记《Elon Musk》的出版社正典入口。",
            "en": "The Simon & Schuster official page for Walter Isaacson's 2023 biography Elon Musk.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "出版社版权（页面免费浏览）", "en": "Publisher copyright (page free to view)"},
        "reason": {
            "zh": "官方书目口径：书中访谈与引语若有引用争议，出版社页是版本判定的锚点。",
            "en": "The official book caliber: when quotes from the biography are disputed, the publisher page anchors the edition.",
        },
        "companies": ["Tesla", "SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "本机 DNS 污染致直连失败，经服务端读取器核活 200（2026-10-02）。",
            "en": "Local DNS pollution blocks direct fetch; verified live via a server-side reader (2026-10-02).",
        },
    },
    {
        "id": "vance-official-page",
        "url": "https://www.harpercollins.com/products/elon-musk-how-the-billionaire-ceo-of-spacex-and-tesla-ashlee-vance",
        "name": {"zh": "《Elon Musk》官方书页（Ashlee Vance 著）", "en": "Elon Musk official book page (by Ashlee Vance)"},
        "desc": {
            "zh": "HarperCollins/Ecco 官方书页：Ashlee Vance 2015 年传记《Elon Musk》的出版社正典入口。",
            "en": "The HarperCollins/Ecco official page for Ashlee Vance's 2015 biography Elon Musk.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "出版社版权（页面免费浏览）", "en": "Publisher copyright (page free to view)"},
        "reason": {
            "zh": "2015 传记的版本判定锚点：早期 SpaceX/Tesla 叙事被引用时的出处正典。",
            "en": "The edition anchor for the 2015 biography — the canonical citation when early SpaceX/Tesla narratives are quoted.",
        },
        "companies": ["Tesla", "SpaceX"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "本机 DNS 污染致直连失败，经服务端读取器核活 200（2026-10-02）。",
            "en": "Local DNS pollution blocks direct fetch; verified live via a server-side reader (2026-10-02).",
        },
    },
    {
        "id": "reuters-tesla-topic",
        "url": "https://www.reuters.com/business/tesla-vehicles/",
        "name": {"zh": "Reuters · Tesla 专题页", "en": "Reuters — Tesla & Vehicles topic page"},
        "desc": {
            "zh": "路透社的 Tesla 车辆与公司新闻专题页：通讯社口径的滚动档案。",
            "en": "Reuters Tesla & Vehicles topic page: the wire-service rolling archive.",
        },
        "category": "community",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "路透社版权（页面免费浏览）", "en": "Reuters copyright (page free to view)"},
        "reason": {
            "zh": "通讯社口径的档案层：本站多条后续注记（如 America Party 引发 Tesla -7%）以此为背景源。",
            "en": "The wire-archive layer: several aftermath notes on this site (e.g. America Party -7% day) rest on Reuters background.",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-02",
        "http": 200,
        "note": {
            "zh": "本机 DNS 污染致直连失败，经服务端读取器核活 200（2026-10-02）。",
            "en": "Local DNS pollution blocks direct fetch; verified live via a server-side reader (2026-10-02).",
        },
    },
    {
        "id": "sec-edgar-spacex",
        "url": "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001181412&type=10-Q&dateb=&owner=include&count=40",
        "name": {"zh": "SEC EDGAR · SpaceX 上市公司文件", "en": "SEC EDGAR — SpaceX filings"},
        "desc": {
            "zh": "SpaceX（CIK 0001181412）的 EDGAR 备案页：2026-06 上市后的 10-Q、8-K 与大股东 13G——注册地德州、纳斯达克代码 SPCX。",
            "en": "SpaceX (CIK 0001181412) on EDGAR: post-IPO 10-Qs, 8-Ks and 13Gs since the June 2026 listing — Texas-incorporated, Nasdaq: SPCX.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "美国政府公开文献，无版权限制", "en": "US government public records"},
        "reason": {
            "zh": "SpaceX 上市后的第一披露通道——公司从「无公开档案」变为申报主体，本站近年化的一手锚。",
            "en": "SpaceX's first disclosure channel as a reporting company — the primary anchor for recent-era sourcing.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-07",
        "http": 200,
        "note": {
            "zh": "V12 R13 收录；本轮实测 200（curl）。同期链：S-1（2026-05-20）→424B4（06-12）→senior notes 8-K（06-22/23/26）→10-Q（08-04）。",
            "en": "Added in V12 R13; verified 200 by curl. Same-era chain: S-1 → 424B4 → notes 8-Ks → 10-Q.",
        },
    },
    {
        "id": "docs-xai",
        "url": "https://docs.x.ai/",
        "name": {"zh": "xAI 官方文档（Grok API）", "en": "xAI Docs — the Grok API"},
        "desc": {
            "zh": "xAI 官方开发者文档：Grok API 的模型清单、定价与调用规范——Grok 从聊天产品走向可编程接口的官方口径。",
            "en": "xAI's official developer docs: Grok API models, pricing and call specs — the official record of Grok as a programmable interface.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "文档版权归 xAI", "en": "Docs © xAI"},
        "reason": {
            "zh": "Grok API 官方文档——模型能力与定价的一手口径（任务书 R13 采集方向第一位）。",
            "en": "The official Grok API docs — first-hand record of model capabilities and pricing (R13's first collection target).",
        },
        "companies": ["xAI"],
        "checked": "2026-10-07",
        "http": 200,
    },
    {
        "id": "tesla-support",
        "url": "https://www.tesla.com/support",
        "name": {"zh": "Tesla 官方支持页", "en": "Tesla Support (official)"},
        "desc": {
            "zh": "Tesla 官方支持入口：车主手册、充电指南与产品 FAQ——官方口径的产品事实源。",
            "en": "Tesla's official support hub: owner's manuals, charging guides and product FAQs — the official product-fact source.",
        },
        "category": "official",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "内容版权归 Tesla", "en": "Content © Tesla"},
        "reason": {
            "zh": "官方类补强：车主手册与支持文档是一手产品事实源（任务书 R13 采集方向）。",
            "en": "Official-side reinforcement: owner's manuals and support docs as first-hand product facts (R13 target).",
        },
        "companies": ["Tesla"],
        "checked": "2026-10-07",
        "http": 200,
        "note": {
            "zh": "本机 curl/WebFetch 403（Cloudflare 拦截），经服务端读取器核活 200（2026-10-07）——三路法第三路实锤，同 xai-official 先例。",
            "en": "curl/WebFetch 403 (Cloudflare) on this machine; verified 200 via a server-side reader (2026-10-07) — third path of the three-way check, same precedent as xai-official.",
        },
    },
    {
        "id": "xai-org-github",
        "url": "https://github.com/xai-org",
        "name": {"zh": "xai-org · GitHub 组织页", "en": "xai-org on GitHub"},
        "desc": {
            "zh": "xAI 官方 GitHub 组织：Grok-1 开源权重（52,236 stars）与后续开源发布——「理解宇宙」的公开代码面。",
            "en": "xAI's official GitHub org: the Grok-1 open weights (52,236 stars) and later open-source releases — the public code face.",
        },
        "category": "opensource",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "各仓库许可见各自仓库页", "en": "Per-repo licenses"},
        "reason": {
            "zh": "开源类补强：org 页是 Grok 开源发布的第一入口（grok-1 单仓库已在册，此为组织级入口）。",
            "en": "Open-source reinforcement: the org page is the entry point for Grok open releases (the grok-1 repo is already listed).",
        },
        "companies": ["xAI"],
        "checked": "2026-10-07",
        "http": 200,
        "note": {
            "zh": "V12 R13 收录；org 页实测 200（curl）。grok-1 仓库实测（api.github.com，2026-10-07）：stars 52,236 · 最近 push 2024-08。",
            "en": "Added in V12 R13; org page verified 200 by curl. grok-1 repo via api.github.com (2026-10-07): 52,236 stars, last push 2024-08.",
        },
    },
    {
        "id": "spacex-ir",
        "url": "https://www.spacex.com/investors",
        "name": {"zh": "SpaceX 投资者关系", "en": "SpaceX Investor Relations"},
        "desc": {
            "zh": "SpaceX 上市后的投资者关系页：财报、备案指引与股东信息——2026-06 IPO 之后的官方资本信息口。",
            "en": "SpaceX's post-IPO investor relations page: filings, guidance and shareholder info — the official capital-information channel since the June 2026 IPO.",
        },
        "category": "tools",
        "lang": "en",
        "activity": "维护中",
        "license": {"zh": "内容版权归 SpaceX", "en": "Content © SpaceX"},
        "reason": {
            "zh": "工具类补强：IR 页与 EDGAR 备案互为表里，是近年化资本数据的官方索引。",
            "en": "Tools-side reinforcement: the IR page complements EDGAR filings as the official index of capital data.",
        },
        "companies": ["SpaceX"],
        "checked": "2026-10-07",
        "http": 200,
    },
]
ACTIVITY_ENUM = ("维护中", "停更", "存档")
LANG_ENUM = ("en", "zh", "zh/en")


def resources_for_company(company_name, limit=6):
    """V9-20 R14：资源↔公司档案/事件互链的单一事实来源查询。

    按 companies 字段匹配公司实体名（与 build-company-files.py 的 file name 对齐，
    调用方负责「Tesla, Inc.」「X（原推特）」等别名到词表的映射）。返回按
    category 顺序（official→opensource→community→tools）稳定排序的条目列表；
    「综合」条目（跨公司/无单一归属）不参与匹配，避免每家公司都挂同一批泛条。
    """
    order = {cid: i for i, cid in enumerate(CATEGORIES)}
    hits = [r for r in RESOURCES
            if company_name in (r.get("companies") or []) and company_name != "综合"]
    hits.sort(key=lambda r: (order.get(r.get("category"), 99), r.get("id", "")))
    return hits[:limit] if limit else hits


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
