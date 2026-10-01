# -*- coding: utf-8 -*-
"""V10-15 N12：resources-data.py 追加 8 条 SpaceX 观测生态资源。"""
import io

p = 'tools/resources-data.py'
s = io.open(p, encoding='utf-8').read()
i = s.rfind('    },\n]')
assert i > 0

addition = '''    },
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
]'''
s = s[:i] + addition + s[i + len('    },\n]'):]
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('8 items appended')
