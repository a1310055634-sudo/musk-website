# -*- coding: utf-8 -*-
"""V12 R10：events-data.py EVENTS 追加四档（2023–2026），带内建断言。
锚=EVENTS 列表收尾 `    },\n]`。失败即 exit 1 不落盘。"""
import io, re

PATH = 'tools/events-data.py'
s = io.open(PATH, encoding='utf-8').read()

BLOCK = '''    },
    # ------------------------------------------------ R10 2023.11 Grok 线
    {
        "id": "e2023-11",
        "date": "2023.11",
        "precision": "month",
        "etype": "milestone",
        "companies": ["xAI"],
        "title": {"zh": "Grok：从聊天玩具到操作系统层",
                  "en": "Grok: from chatbot toy to an OS layer"},
        "summary": {
            "zh": "2023 年 11 月 Grok 以「带幽默感」为卖点发布；两年多后，Grok 4.8 以 2.5T 参数与 C++ 推理栈上车入机，Grokkipedia 与预测模型把边界推到百科与预测——聊天玩具长成了横跨车机的 OS 层。",
            "en": "Grok launched in November 2023 sold on its sense of humor; two years on, Grok 4.8 runs 2.5T parameters with a C++ inference stack in cars and devices, while Grokipedia and forecasting models push past chat — a toy that grew into an OS layer.",
        },
        "background": {
            "zh": "xAI 于 2023 年 7 月 12 日官宣成立，同年 11 月 4 日向 X Premium 用户发布 Grok-1；2026 年 2 月首届 All-Hands 自评语音/图像/视频生成第一并发布 Grokipedia；9 月 Grok 4.8 参数规模与推理栈细节经 X 帖首曝。",
            "en": "xAI was announced on July 12, 2023 and shipped Grok-1 to X Premium users on November 4; the first All-Hands (Feb 2026) claimed #1 in voice/image/video and launched Grokipedia; Grok 4.8's scale and C++ stack surfaced via X posts that September.",
        },
        "facts": [
            {"zh": "2023-07-12 xAI 官宣成立；2023-11-04 Grok-1 向 X Premium 用户开放。",
             "en": "xAI announced July 12, 2023; Grok-1 opened to X Premium users on November 4, 2023."},
            {"zh": "2026-02 All-Hands：语音/图像/视频生成第一、Grokkipedia 对标维基百科、首个 10 万张 H100 集群。",
             "en": "Feb 2026 All-Hands: #1 in voice/image/video, Grokipedia vs Wikipedia, first 100k-H100 cluster."},
            {"zh": "2026-09 Grok 4.8 细节首曝：2.5T 参数规模与 C++ 推理栈（站内 X 帖卡转录口径）。",
             "en": "Sept 2026: Grok 4.8 details first surfaced — 2.5T parameters on a C++ inference stack (per the archived post on this site)."},
        ],
        "quotes": [
            {"en": "Grokkipedia is intended ultimately to be Encyclopedia Galactica, a distillation of all knowledge.",
             "zh": "Grokkipedia 的终极目标是成为「银河百科全书」——一切知识的蒸馏。",
             "src": "2026.02.10 xAI All-Hands（primary.html#e2026-02-10）"},
        ],
        "materials": [
            {"kind": "ledger", "href": "primary.html#e2023-07-12", "date": "2023.07.12",
             "label": {"zh": "言行账本 e2023-07-12 · xAI 成立", "en": "Ledger e2023-07-12 · xAI is announced"},
             "note": {"zh": "Grok 线的起点", "en": "Where the Grok thread starts"}},
            {"kind": "post", "href": "x-posts.html#p2023-11-04", "date": "2023.11.04",
             "label": {"zh": "X 帖卡 p2023-11-04 · Grok-1 发布", "en": "Post p2023-11-04 · Grok-1 ships"},
             "note": {"zh": "镜像逐字转录", "en": "Mirrored transcript"}},
            {"kind": "post", "href": "x-posts.html#p2026-09-14", "date": "2026.09.14",
             "label": {"zh": "X 帖卡 p2026-09-14 · Grok 4.8 2.5T/C++ 栈首曝", "en": "Post p2026-09-14 · Grok 4.8 details"},
             "note": {"zh": "参数与栈口径", "en": "Scale and stack claims"}},
            {"kind": "interview", "href": "interviews.html#i2026-01-06", "date": "2026.01.06",
             "label": {"zh": "访谈 i2026-01-06 · Moonshots 电路访谈", "en": "Interview i2026-01-06 · Moonshots on Grok"},
             "note": {"zh": "Grok 更新机制自述", "en": "On how Grok keeps updating"}},
            {"kind": "document", "href": "documents.html#d2026-01", "date": "2026.01",
             "label": {"zh": "文档 d2026-01 · xAI Series E（Grok 开发资金面）", "en": "Doc d2026-01 · Series E funds Grok"},
             "note": {"zh": "资本侧佐证", "en": "The capital-side record"}},
            {"kind": "feature", "href": "grok.html#grok", "date": "2026",
             "label": {"zh": "站内专题 grok.html · xAI/Grok 全梳理", "en": "Feature grok.html · the full Grok thread"},
             "note": {"zh": "站内汇总视角", "en": "On-site synthesis"}},
        ],
        "related": [],
        "no_quote_note": None,
        "outcome": {
            "zh": "「第一」与「超越」都是 xAI 自己给出的可核指标——预测基准、生成量与 Grokipedia 覆盖度可以逐项对账；OS 层的成色则交给装进了多少辆车与设备。（末句为编者分析，非其原话。）",
            "en": "The “firsts” are xAI's own checkable metrics — forecasting, generation volume, Grokipedia coverage can all be audited; whether the OS layer is real is decided by how many cars and devices actually run it. (Editorial analysis, not his words.)",
        },
    },
    # ------------------------------------------------ R10 2025.06.22 Robotaxi 落地
    {
        "id": "e2025-06-22",
        "date": "2025.06.22",
        "precision": "day",
        "etype": "milestone",
        "companies": ["Tesla"],
        "title": {"zh": "Robotaxi 落地：八年欠账之后的奥斯汀首发",
                  "en": "Robotaxi goes live: Austin, eight years after the promise"},
        "summary": {
            "zh": "从 2016 年「今年底无人横穿美国」到 2019 年「2020 年百万台」，欠账清单挂了八年；2025 年 6 月 22 日，奥斯汀的小规模付费服务终于开跑——安全员在驾驶座，但车轮真的自己转了。",
            "en": "Eight years after “crossing the country autonomously by year-end” (2016) and “a million robotaxis by 2020” (2019), a small paid service finally started in Austin on June 22, 2025 — a safety monitor still up front, but the wheels genuinely turned themselves.",
        },
        "background": {
            "zh": "2024-10-10「We, Robot」发布 Cybercab 把叙事重新拉回Robotaxi；2025-06 奥斯汀首批车辆上线；随后一年服务面积扩张、车内监督员撤除、深夜时段延长——站内以四张 X 帖卡记录了这条落地弧线。",
            "en": "The Oct 2024 “We, Robot” event (Cybercab) pulled the narrative back to robotaxi; Austin went live June 2025; over the following year the service area grew, in-car monitors were dropped and late-night hours extended — an arc this site tracks with four archived posts.",
        },
        "facts": [
            {"zh": "付费服务 2025.06 于奥斯汀启动（e2026-07-22 财报电话会口径：launched 2025.06）。",
             "en": "Paid service launched in Austin, June 2025 (per the Q2 2026 call, e2026-07-22)."},
            {"zh": "2026-01 起部分行程车内无安全监督员（p2026-01-22 卡）；服务面积与时段随后继续扩张。",
             "en": "By Jan 2026 some rides ran with no in-car safety monitor (p2026-01-22); area and hours kept expanding."},
            {"zh": "兑现记账：promises.html 五案将该承诺列为本站持续跟踪的口径之一。",
             "en": "Bookkeeping: promises.html tracks this among the site's standing promise cases."},
        ],
        "quotes": [],
        "materials": [
            {"kind": "ledger", "href": "primary.html#e2024-10-10", "date": "2024.10.10",
             "label": {"zh": "言行账本 e2024-10-10 · We,Robot 与 Cybercab", "en": "Ledger e2024-10-10 · We,Robot and Cybercab"},
             "note": {"zh": "落地前史", "en": "The runway before launch"}},
            {"kind": "ledger", "href": "primary.html#e2026-07-22", "date": "2026.07.22",
             "label": {"zh": "言行账本 e2026-07-22 · 一周年财报电话会", "en": "Ledger e2026-07-22 · one-year earnings call"},
             "note": {"zh": "「是否」变成「多快」", "en": "From “whether” to “how fast”"}},
            {"kind": "post", "href": "x-posts.html#p2025-08-16", "date": "2025.08.16",
             "label": {"zh": "X 帖卡 p2025-08-16 · 服务面积超对手", "en": "Post p2025-08-16 · area tops rivals"},
             "note": {"zh": "镜像逐字转录", "en": "Mirrored transcript"}},
            {"kind": "post", "href": "x-posts.html#p2025-10-29", "date": "2025.10.29",
             "label": {"zh": "X 帖卡 p2025-10-29 · 大奥斯汀全区", "en": "Post p2025-10-29 · greater Austin coverage"},
             "note": {"zh": "扩张节点", "en": "Expansion marker"}},
            {"kind": "post", "href": "x-posts.html#p2026-01-22", "date": "2026.01.22",
             "label": {"zh": "X 帖卡 p2026-01-22 · 车内无安全监督员", "en": "Post p2026-01-22 · no in-car monitor"},
             "note": {"zh": "监督员撤除", "en": "Monitors dropped"}},
            {"kind": "post", "href": "x-posts.html#p2026-10-03", "date": "2026.10.03",
             "label": {"zh": "X 帖卡 p2026-10-03 · 延时 23 点", "en": "Post p2026-10-03 · hours stretch to 11pm"},
             "note": {"zh": "时段扩张", "en": "Hours expansion"}},
            {"kind": "feature", "href": "promises.html#promises-s3", "date": "2026",
             "label": {"zh": "站内专题 promises.html · 五案全览（含 FSD/Robotaxi 欠账）", "en": "Feature promises.html · the five cases"},
             "note": {"zh": "欠账记账口径", "en": "The promise-ledger view"}},
        ],
        "related": [],
        "no_quote_note": "本档为服务落地事实记录，不设逐字引语节；弧线各节点的原话以 X 帖卡逐字转录为准（见 materials）。",
        "outcome": {
            "zh": "发车即记账：地理围栏、车内监督员、时段与收费都是可核参数——八年的承诺第一次以可验证的运营数据而不是演示视频推进。（末句为编者分析，非其原话。）",
            "en": "The ledger started the day the cars did: geofence, monitors, hours and fares are all checkable parameters — for the first time the promise advances as operating data, not demo videos. (Editorial analysis, not his words.)",
        },
    },
    # ------------------------------------------------ R10 2026.07 Optimus 产线
    {
        "id": "e2026-07",
        "date": "2026.07",
        "precision": "month",
        "etype": "milestone",
        "companies": ["Tesla"],
        "title": {"zh": "Optimus 量产线：Fremont 实拍与 AI5 上机",
                  "en": "Optimus line: Fremont footage and AI5 on-board"},
        "summary": {
            "zh": "2026 年 7 月，Fremont 产线实拍帖把 Optimus 从展会演示推进到「有产线的商品」；同一季度，AI5 芯片进 Optimus 的口径与一周年财报会相互印证——人形机器人的瓶颈从「能不能做」变成「能不能造」。",
            "en": "In July 2026 a Fremont production-line post moved Optimus from stage demo to product with a line; the same quarter, AI5-in-Optimus talk and the one-year earnings call corroborate — the bottleneck shifted from “can it be built” to “can it be manufactured”.",
        },
        "background": {
            "zh": "Optimus 自 2021 AI Day 立项、2024-04 财报会起进入量产叙事；2026-02-05 Dwarkesh 访谈中 AI5 芯片进 Optimus 的表述与 2026-07 Fremont 产线实拍帖构成「设计—芯片—产线」三节点。",
            "en": "From the 2021 AI Day reveal to the April 2024 call's production talk, the thread runs through the Feb 2026 Dwarkesh interview (AI5 going into Optimus) to the July 2026 Fremont line footage — design, chip, line.",
        },
        "facts": [
            {"zh": "2026-07 Fremont Optimus 产线实拍（t.co 图链不入正文，站内以 X 帖卡转录口径记录）。",
             "en": "July 2026: Fremont Optimus line footage (the t.co image link is kept out of body text; recorded via the archived post)."},
            {"zh": "AI5 芯片将进 Optimus（i2026-02-05 访谈逐字口径：AI5 chip is going into our Optimus robot）。",
             "en": "AI5 is going into the Optimus robot (verbatim from the Feb 2026 Dwarkesh interview)."},
            {"zh": "欠账记账口径：「消除贫困」级承诺仍列 promises.html 跟踪清单，尚无足够证据。",
             "en": "Promise bookkeeping: the “eliminate poverty” pledge remains on promises.html with no evidence yet."},
        ],
        "quotes": [],
        "materials": [
            {"kind": "post", "href": "x-posts.html#p2026-07-01", "date": "2026.07.01",
             "label": {"zh": "X 帖卡 p2026-07-01 · Fremont 产线实拍", "en": "Post p2026-07-01 · the Fremont line"},
             "note": {"zh": "镜像逐字转录", "en": "Mirrored transcript"}},
            {"kind": "interview", "href": "interviews.html#i2026-02-05", "date": "2026.02.05",
             "label": {"zh": "访谈 i2026-02-05 · Dwarkesh（AI5 进 Optimus）", "en": "Interview i2026-02-05 · Dwarkesh on AI5"},
             "note": {"zh": "芯片口径逐字", "en": "The chip claim verbatim"}},
            {"kind": "ledger", "href": "primary.html#e2024-04-23", "date": "2024.04.23",
             "label": {"zh": "言行账本 e2024-04-23 · Optimus 量产叙事前史", "en": "Ledger e2024-04-23 · the earlier production talk"},
             "note": {"zh": "前史节点", "en": "Prior marker"}},
            {"kind": "ledger", "href": "primary.html#e2026-07-22", "date": "2026.07.22",
             "label": {"zh": "言行账本 e2026-07-22 · 一周年财报电话会", "en": "Ledger e2026-07-22 · one-year earnings call"},
             "note": {"zh": "同期口径互证", "en": "Corroborating quarter"}},
            {"kind": "feature", "href": "promises.html#promises-s3", "date": "2026",
             "label": {"zh": "站内专题 promises.html · Optimus 欠账卡", "en": "Feature promises.html · the Optimus case"},
             "note": {"zh": "承诺记账", "en": "Promise bookkeeping"}},
        ],
        "related": [],
        "no_quote_note": "本档为产线与芯片口径的事实记录，不设逐字引语节；AI5 表述的逐字句见访谈条目本身。",
        "outcome": {
            "zh": "产线实拍是可核物证：站点、工位、节拍都经得起放大——但「量产」的会计口径（周产/交付/毛利）仍待财报逐季对账。（末句为编者分析，非其原话。）",
            "en": "A production line is checkable evidence — the stations and takt survive zooming in; whether “mass production” holds is settled quarterly, in the accounts. (Editorial analysis, not his words.)",
        },
    },
    # ------------------------------------------------ R10 2024.07 政治参与与 America Party
    {
        "id": "e2024-07",
        "date": "2024.07",
        "precision": "month",
        "etype": "risk",
        "companies": ["X", "Tesla", "SpaceX"],
        "title": {"zh": "政治参与与 America Party：关键人风险的第三战场",
                  "en": "Politics and the America Party: the third front of key-person risk"},
        "summary": {
            "zh": "2024 年 7 月大选背书入场，2025 年 7 月 America Party 宣布组党，2026 中期周期发帖强度升至峰值（镜像池 178+ 条）——政治参与成为横跨三家公司资产负债表的关键人风险；本站以镜像原文建档，立场与批评正反并陈。",
            "en": "From the July 2024 endorsement to the America Party launch in July 2025 and a midterms-cycle posting peak (178+ archived posts), politics became a key-person risk spanning three balance sheets. This site archives it in mirrored originals, giving his case and the critics' case side by side.",
        },
        "background": {
            "zh": "2024-07 背书后政治表达密度逐年上升；2025-07-05/06 经 X 民调宣布组建 America Party；2026-01 起围绕中期选举的帖组（single-party state 等表述）在镜像库中形成 178+ 条池。本档为事件档案视角，深读分析另立专题（任务书 R12）。",
            "en": "After the July 2024 endorsement, political posting escalated; the America Party was announced via an X poll on July 5–6, 2025; by January 2026 a midterms thread (“single-party state” and related) formed a 178+ post pool in the mirror. This entry is the event-archive view; the long-form analysis is a separate deep dive (R12).",
        },
        "facts": [
            {"zh": "他的立场（原文口径）：批评两党体制走向「single-party state」，主张以第三党制衡（2026-01-07 帖：\"That is their goal: a single-party state for all of America\"）。",
             "en": "His case (verbatim): he frames the two-party system as sliding toward a “single-party state” and argues a third party is the check (Jan 7, 2026 post)."},
            {"zh": "批评方立场：批评者认为其政治参与使 Tesla/SpaceX 的政府合同与监管关系复杂化，并把平台变成党争工具；该批判口径见主流报道与本站后续深读（R12 立）。",
             "en": "The critics' case: his involvement entangles Tesla/SpaceX government contracts and regulation, and turns the platform into a partisan tool — to be covered in the R12 deep dive."},
            {"zh": "记录口径：本站不预测政治后果，只逐条存档原文与日期；178+ 池以镜像检索链接为准。",
             "en": "Record-keeping stance: no political forecasting here — originals and dates archived item by item; the 178+ pool is indexed via the mirror search link."},
        ],
        "quotes": [
            {"en": "That is their goal: a single-party state for all of America",
             "zh": "这就是他们的目标：让全美国成为一个一党国家。",
             "src": "2026.01.07 X 帖（镜像 x-2008888326871535862）"},
        ],
        "materials": [
            {"kind": "external", "href": "https://elonmuskarchive.org/posts/2008888326871535862", "date": "2026.01.07",
             "label": {"zh": "镜像原文 x-2008888326871535862 · single-party state", "en": "Mirror x-2008888326871535862 · single-party state"},
             "note": {"zh": "2026-01-07 逐字帖", "en": "Verbatim post, Jan 7 2026"}},
            {"kind": "external", "href": "https://elonmuskarchive.org/posts/2103894760838897922", "date": "2026.09.26",
             "label": {"zh": "镜像原文 x-2103894760838897922 · 中期周期帖", "en": "Mirror x-2103894760838897922 · midterms-cycle post"},
             "note": {"zh": "2026-09-26 逐字帖", "en": "Verbatim post, Sep 26 2026"}},
            {"kind": "external", "href": "https://elonmuskarchive.org/posts/2008990970491072842", "date": "2026.01.07",
             "label": {"zh": "镜像原文 x-2008990970491072842 · 同日跟进帖", "en": "Mirror x-2008990970491072842 · same-day follow-up"},
             "note": {"zh": "2026-01-07 逐字帖", "en": "Verbatim post, Jan 7 2026"}},
            {"kind": "external", "href": "https://elonmuskarchive.org/agents/search?q=America%20Party", "date": "2026",
             "label": {"zh": "镜像检索：America Party 帖池（178+ 条）", "en": "Mirror search: the America Party pool (178+ posts)"},
             "note": {"zh": "全池检索入口", "en": "Index into the full pool"}},
        ],
        "related": [],
        "no_quote_note": None,
        "outcome": {
            "zh": "仍在进行时：组党登记、中期选举与三家公司监管关系都是未决变量——本档只固化已发生的原文与日期，判断留给读者与后续深读。（末句为编者分析，非其原话。）",
            "en": "Live issue: the party registration, the midterms and three companies' regulatory exposure all remain open variables — this entry fixes only what was said and when; judgment is left to the reader and the coming deep dive. (Editorial analysis, not his words.)",
        },
    },
]'''

anchor = '    },\n]'
assert s.count(anchor) == 1, 'tail anchor not unique: %d' % s.count(anchor)
before = len(re.findall(r'"id": "e[^"]+"', s))
for qid in ['"e2023-11"', '"e2025-06-22"', '"e2026-07"', '"e2024-07"']:
    assert s.count(qid) == 0, 'id exists: ' + qid
assert s.count('"id": "e2006"') == 1  # 年精度先例仍在

s2 = s.replace(anchor, BLOCK, 1)
after = len(re.findall(r'"id": "e[^"]+"', s2))
assert after == before + 4, 'events %d -> %d != +4' % (before, after)
assert s2.count('"etype": "milestone"') == 8 and s2.count('"etype": "risk"') == 3
for k in ['"start"', '"deal"', '"gamble"']:
    assert s2.count('"etype": ' + k) >= 1

io.open(PATH, 'w', encoding='utf-8', newline='\n').write(s2)
print('OK: EVENTS %d -> %d' % (before, after))
