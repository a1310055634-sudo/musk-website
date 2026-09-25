# -*- coding: utf-8 -*-
"""从四个第一手页面提取全部可引用条目，生成 search-index.js。

用法：python tools/build-search-index.py
（站点根目录执行；第一手内容更新后重跑一次即可刷新搜索索引。）

产物：search-index.js —— 内容为 `window.SEARCH_INDEX = [...]`。
用 JS 变量而非 JSON fetch：file:// 协议下 fetch 会被 CORS 拦截，script 标签不受限。
"""
import io
import html as H
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

def strip(t):
    t = re.sub(r'<[^>]+>', '', t)
    return re.sub(r'\s+', ' ', H.unescape(t)).strip()

items = []

# ---------- primary.html 言行实录 ----------
s = io.open('primary.html', encoding='utf-8').read()
for m in re.finditer(r'<li class="ps-row[^"]*" id="(e\d[\d-]*)".*?</li>', s, re.S):
    b = m.group(0)
    date = re.search(r'<a class="ps-date" href="#[^"]*"[^>]*>([^<]+)</a>', b)
    src = re.search(r'<span class="ps-src">([^<]+)</span>', b)
    quote = re.search(r'<blockquote class="ps-quote">(.*?)</blockquote>', b, re.S)
    zh = re.search(r'<p class="ps-zh">(.*?)</p>', b, re.S)
    assert date and src, m.group(1)
    if not quote:  # 部分条目以行为为主、无逐字引文段：降级取第一段背景文字
        quote = re.search(r'<div class="ps-sec">.*?data-en="[^"]*">([^<]+)</p>', b, re.S)
    bg = re.search(r'<div class="ps-sec"><h4[^>]*>[^<]*背景[^<]*</h4>\s*<p data-en="([^"]*)"', b)
    items.append({
        'id': m.group(1), 'pg': 'primary.html', 't': '言行实录',
        'd': date.group(1), 's': strip(src.group(1)),
        'q': strip(quote.group(1)) if quote else '', 'zh': strip(zh.group(1)) if zh else '',
        'bg': strip(bg.group(1)) if bg else '',
    })

# ---------- documents.html 一手文档 ----------
s = io.open('documents.html', encoding='utf-8').read()
for m in re.finditer(r'<article class="doc-article" id="(d\d[\d-]*)">(.*?)</article>', s, re.S):
    b = m.group(2)
    h2 = re.search(r'<h2>([^<]+)</h2>', b)
    badges = re.findall(r'<(?:span|a) class="doc-badge"[^>]*>([^<]+)</(?:span|a)>', b)
    quote = re.search(r'<blockquote>(.*?)</blockquote>', b, re.S)
    note = re.search(r'<p class="note">(.*?)</p>', b, re.S)
    assert h2 and badges and quote, m.group(1)
    date = next((x for x in badges if re.match(r'2\d{3}', x.strip())), badges[0])
    items.append({
        'id': m.group(1), 'pg': 'documents.html', 't': '一手文档',
        'd': strip(date), 's': strip(h2.group(1)), 'q': strip(quote.group(1)), 'zh': '',
        'bg': strip(note.group(1)) if note else '',
    })

# ---------- interviews.html 访谈与表态 ----------
s = io.open('interviews.html', encoding='utf-8').read()
for m in re.finditer(r'<article class="iv-item" id="(i\d[\d-]*)">(.*?)</article>', s, re.S):
    b = m.group(2)
    h2 = re.search(r'<h2>([^<]+)</h2>', b)
    badges = re.findall(r'<a class="iv-badge" href="#[^"]*"[^>]*>([^<]+)</a>', b)
    quote = re.search(r'<blockquote>(.*?)</blockquote>', b, re.S)
    assert h2 and badges, m.group(1)
    if not quote:
        quote = re.search(r'<p class="ctx">(.*?)</p>', b, re.S)
    ctx = re.search(r'<p class="ctx">(.*?)</p>', b, re.S)
    items.append({
        'id': m.group(1), 'pg': 'interviews.html', 't': '访谈与表态',
        'd': strip(badges[0] if re.match(r'2\d{3}', badges[0]) else badges[1] if len(badges) > 1 else badges[0]),
        's': strip(h2.group(1)), 'q': strip(quote.group(1)), 'zh': '',
        'bg': strip(ctx.group(1)) if ctx else '',
    })

# ---------- x-posts.html X 帖史 ----------
s = io.open('x-posts.html', encoding='utf-8').read()
parts = re.split(r'(?=<div class="tweet-card" id=")', s)
for part in parts[1:]:
    mid = re.match(r'<div class="tweet-card" id="(p\d[\d-]*)"', part)
    if not mid:
        continue
    b = part[:part.find('</div>\n    </div>') if '</div>\n    </div>' in part else len(part)]
    date = re.search(r'<a class="tweet-date" href="#[^"]*"[^>]*>([^<]+)</a>', b)
    text = re.search(r'<p class="tweet-text">(.*?)</p>', b, re.S)
    zh = re.search(r'<p class="tweet-zh">(.*?)</p>', b, re.S)
    note = re.search(r'<p class="tweet-note">(.*?)</p>', b, re.S)
    assert date and text, mid.group(1)
    items.append({
        'id': mid.group(1), 'pg': 'x-posts.html', 't': 'X 帖',
        'd': date.group(1), 's': '@elonmusk',
        'q': strip(text.group(1)), 'zh': strip(zh.group(1)) if zh else '',
        'bg': strip(note.group(1)) if note else '',
    })

# ---------- controversy.html 争议深读 ----------
# 五篇深读摘要与代表引语：q/zh/bg 均重组自页内已核实文字（不造新事实）；d 取篇内时间线首个关键年份
CV_META = {
    'sec-pedo': {'d': '2018', 'q': 'Sorry pedo guy, you really did ask for it. / Bet ya a signed dollar it\'s true.',
                 'zh': '2018.07.15 推文「pedo guy」→ Unsworth 1.9 亿美元诽谤诉讼 → 2019.12.06 陪审团约一小时裁决不构成诽谤。',
                 'bg': '从救援英雄的一句批评到 1.9 亿美元的诉讼——以及陪审团一小时的裁决。'},
    'sec-sec': {'d': '2018', 'q': 'Am considering taking Tesla private at $420. Funding secured.',
                'zh': 'SEC 认定「funding secured」构成证券欺诈：个人与公司各罚 2000 万美元、卸任董事长、重大推文律师预审。',
                'bg': '一条推文让他付出 2000 万美元、董事长职位，以及至今仍在约束他发推的律师预审规则。'},
    'autopilot': {'d': '2022', 'q': '「Autopilot」和「Full Self-Driving」这两个名字本身，就成了加州 DMV 虚假广告指控的核心。',
                  'zh': '2022 加州 DMV 虚假广告指控 → 2025.12 认定违法 → 2026.02 Tesla 起诉 DMV；2024.10 NHTSA 对 240 万辆 FSD 展开调查。',
                  'bg': '「Autopilot」「FSD」命名争议：监管线（加州 DMV）与 NHTSA 调查线的完整时间线。'},
    'union': {'d': '2018', 'q': 'Nothing stopping Tesla team at our car plant from voting union. Could do so tmrw if they wanted. But why pay union dues & give up stock options for nothing.',
              'zh': '一条推文引发六年 NLRB 法律战：2019 裁定非法威胁 → 2021 要求删帖他拒绝 → 2023.03 第五巡回法院部分支持。',
              'bg': '一条推文引发六年的 NLRB 法律战——「nothing stopping」到「为什么付会费」。'},
    'twitter': {'d': '2021', 'q': 'Much is made lately of unrealized gains being a means of tax avoidance, so I propose selling 10% of my Tesla stock. Do you support this?',
                'zh': '2021.11 卖股投票（350 万人、57.9% 赞成后售股）与 2022.12.15 记者封禁（48 小时后恢复）——平台规则与个人意志的边界。',
                'bg': '从「Tax the rich」投票到记者封禁——平台拥有者的推文边界与「言论自由绝对主义者」的自我矛盾。'},
}
s = io.open('controversy.html', encoding='utf-8').read()
found_cv = set()
for m in re.finditer(r'<section class="ct-ch" id="([a-z-]+)">(.*?)</section>', s, re.S):
    if m.group(1) not in CV_META:
        continue
    h2 = re.search(r'<h2[^>]*>([^<]+)</h2>', m.group(2))
    assert h2, m.group(1)
    meta = CV_META[m.group(1)]
    items.append({
        'id': m.group(1), 'pg': 'controversy.html', 't': '争议深读',
        'd': meta['d'], 's': strip(h2.group(1)), 'q': meta['q'], 'zh': meta['zh'], 'bg': meta['bg'],
    })
    found_cv.add(m.group(1))
assert found_cv == set(CV_META), found_cv

# ---------- 公司实体推断（多对多，用于检索过滤） ----------
import re as _re
ENTITY_RULES = [
    ('Zip2', _re.compile(r'Zip2', _re.I)),
    ('PayPal', _re.compile(r'PayPal|X\.com|Confinity', _re.I)),
    ('SolarCity', _re.compile(r'SolarCity', _re.I)),
    ('Tesla', _re.compile(r'Tesla|Model [S3XY]|Battery Day|4680|Roadster|Cybertruck|Fremont', _re.I)),
    ('SpaceX', _re.compile(r'SpaceX|Falcon|Crew Dragon|NASA|Starbase|Starship|Dragon|BFR', _re.I)),
    ('X / Twitter', _re.compile(r'Twitter|@elonmusk|bird is freed|DealBook|Parag|charter', _re.I)),
    ('xAI', _re.compile(r'xAI|Grok', _re.I)),
    ('Boring Company', _re.compile(r'Boring|flamethrower|tunnel|Loop', _re.I)),
    ('Neuralink', _re.compile(r'Neuralink', _re.I)),
]
for it in items:
    text = ' '.join([it.get('s',''), it.get('q',''), it.get('zh',''), it.get('bg','')])
    cs = [name for name, rx in ENTITY_RULES if rx.search(text)]
    it['c'] = cs if cs else ['综合']

# ---------- 校验与排序 ----------
counts = {}
for it in items:
    counts[it['t']] = counts.get(it['t'], 0) + 1
assert counts == {'言行实录': 67, '一手文档': 9, '访谈与表态': 18, 'X 帖': 13, '争议深读': 5}, counts
ids = [it['id'] for it in items]
assert len(ids) == len(set(ids)), 'id 重复'

def date_key(d):
    m = re.match(r'(\d{4})(?:\.(\d{1,2}))?(?:\.(\d{1,2}))?', d)
    return (int(m.group(1)), int(m.group(2) or 0), int(m.group(3) or 0)) if m else (0, 0, 0)

items.sort(key=lambda x: date_key(x['d']))

out = '// 由 tools/build-search-index.py 自动生成，请勿手改。\nwindow.SEARCH_INDEX = ' + json.dumps(items, ensure_ascii=False, indent=1) + ';\n'
io.open('search-index.js', 'w', encoding='utf-8', newline='\n').write(out)
print(f'search-index.js: {len(items)} 条 {counts}')
