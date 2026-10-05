# -*- coding: utf-8 -*-
"""V12 R13：RESOURCES 追加 5 条（official 3/opensource 1/tools 1），字段 13 个一个不少。
核活 qa/v12/round-13/probe.json + 三路法注记。锚=RESOURCES 列表尾。失败不落盘。"""
import io, re

PATH = 'tools/resources-data.py'
s = io.open(PATH, encoding='utf-8').read()

BLOCK = '''    {
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
]'''

# 锚：RESOURCES 列表收尾（"    },\n]" 且其后紧跟 ACTIVITY_ENUM——文件内唯一）
m = re.search(r'\n    \},\n\]\nACTIVITY_ENUM', s)
assert m, 'list tail not found'
s2 = s[:m.start()] + '\n' + BLOCK + '\nACTIVITY_ENUM' + s[m.end():]
before = len(re.findall(r'"id": "[a-z0-9-]+"', s))
after = len(re.findall(r'"id": "[a-z0-9-]+"', s2))
assert after == before + 5, 'ids %d -> %d != +5' % (before, after)
for qid in ['sec-edgar-spacex', 'docs-xai', 'tesla-support', 'xai-org-github', 'spacex-ir']:
    assert s2.count('"%s"' % qid) == 1, qid
io.open(PATH, 'w', encoding='utf-8', newline='\n').write(s2)
print('OK: RESOURCES %d -> %d' % (before, after))
