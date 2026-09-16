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
    items.append({
        'id': m.group(1), 'pg': 'primary.html', 't': '言行实录',
        'd': date.group(1), 's': strip(src.group(1)),
        'q': strip(quote.group(1)) if quote else '', 'zh': strip(zh.group(1)) if zh else '',
    })

# ---------- documents.html 一手文档 ----------
s = io.open('documents.html', encoding='utf-8').read()
for m in re.finditer(r'<article class="doc-article" id="(d\d[\d-]*)">(.*?)</article>', s, re.S):
    b = m.group(2)
    h2 = re.search(r'<h2>([^<]+)</h2>', b)
    badges = re.findall(r'<(?:span|a) class="doc-badge"[^>]*>([^<]+)</(?:span|a)>', b)
    quote = re.search(r'<blockquote>(.*?)</blockquote>', b, re.S)
    assert h2 and badges and quote, m.group(1)
    date = next((x for x in badges if re.match(r'2\d{3}', x.strip())), badges[0])
    items.append({
        'id': m.group(1), 'pg': 'documents.html', 't': '一手文档',
        'd': strip(date), 's': strip(h2.group(1)), 'q': strip(quote.group(1)), 'zh': '',
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
    items.append({
        'id': m.group(1), 'pg': 'interviews.html', 't': '访谈与表态',
        'd': strip(badges[0] if re.match(r'2\d{3}', badges[0]) else badges[1] if len(badges) > 1 else badges[0]),
        's': strip(h2.group(1)), 'q': strip(quote.group(1)), 'zh': '',
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
    assert date and text, mid.group(1)
    items.append({
        'id': mid.group(1), 'pg': 'x-posts.html', 't': 'X 帖',
        'd': date.group(1), 's': '@elonmusk',
        'q': strip(text.group(1)), 'zh': strip(zh.group(1)) if zh else '',
    })

# ---------- 校验与排序 ----------
counts = {}
for it in items:
    counts[it['t']] = counts.get(it['t'], 0) + 1
assert counts == {'言行实录': 41, '一手文档': 6, '访谈与表态': 18, 'X 帖': 13}, counts
ids = [it['id'] for it in items]
assert len(ids) == len(set(ids)), 'id 重复'

def date_key(d):
    m = re.match(r'(\d{4})(?:\.(\d{1,2}))?(?:\.(\d{1,2}))?', d)
    return (int(m.group(1)), int(m.group(2) or 0), int(m.group(3) or 0)) if m else (0, 0, 0)

items.sort(key=lambda x: date_key(x['d']))

out = '// 由 tools/build-search-index.py 自动生成，请勿手改。\nwindow.SEARCH_INDEX = ' + json.dumps(items, ensure_ascii=False, indent=1) + ';\n'
io.open('search-index.js', 'w', encoding='utf-8', newline='\n').write(out)
print(f'search-index.js: {len(items)} 条 {counts}')
