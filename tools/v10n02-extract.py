# -*- coding: utf-8 -*-
"""V10-15 N02：引语逐字核验 I（机核）——Step1 提取站内引文库存清单。

三类对象：
  A. X 帖 31 卡（tweet-text 英文 + note 内镜像 status id）
  B. 访谈卡（iv-item 裸 blockquote 英文引语）
  C. 账本 115 条（ps-row 的 ps-quote 英文引语块，剥标签）
落盘 qa/v10-15/round-02/inventory.json，供 Step2 diff/indexOf。
"""
import html as H
import io
import json
import os
import re

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TAG_RX = re.compile(r'<[^>]+>')


def strip_tags(s):
    s = TAG_RX.sub('', s)
    s = H.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def norm(s):
    """机核归一：去引号形态/实体/空白/大小写差异，保留字母数字。"""
    s = H.unescape(s)
    s = (s.replace('\u201c', '"').replace('\u201d', '"')
          .replace('\u2018', "'").replace('\u2019', "'")
          .replace('&ldquo;', '"').replace('&rdquo;', '"')
          .replace('&mdash;', '-').replace('&amp;', '&'))
    s = re.sub(r'[^A-Za-z0-9]+', '', s)
    return s.lower()


out = {'tweets': [], 'interviews': [], 'ledger': []}

# ---- A. X 帖（卡起点切片，规避嵌套 div 截断） ----
s = io.open('x-posts.html', encoding='utf-8').read()
starts = [(m.start(), m.group(1)) for m in re.finditer(r'<div class="tweet-card" id="(p[\d-]+)">', s)]
for k, (pos, cid) in enumerate(starts):
    end = starts[k + 1][0] if k + 1 < len(starts) else len(s)
    body = s[pos:end]
    tm = re.search(r'<p class="tweet-text">(.*?)</p>', body, re.S)
    sm = re.search(r'status/(\d+)|x-(\d{8,})', body)
    if tm:
        out['tweets'].append({
            'id': cid,
            'text': strip_tags(tm.group(1)),
            'mirror_id': (sm.group(1) or sm.group(2)) if sm else None,
        })

# ---- B. 访谈 ----
s = io.open('interviews.html', encoding='utf-8').read()
for m in re.finditer(r'<article class="iv-item" id="(i[\d-]+)">(.*?)</article>', s, re.S):
    cid, body = m.group(1), m.group(2)
    for qm in re.finditer(r'<blockquote>(.*?)</blockquote>', body, re.S):
        txt = strip_tags(qm.group(1))
        if len(txt) > 30:
            out['interviews'].append({'id': cid, 'text': txt})

# ---- C. 账本 ----
s = io.open('primary.html', encoding='utf-8').read()
for m in re.finditer(r'<li class="ps-row[^"]*" id="(e[\d-]+)">(.*?)(?=<li class="ps-row|</ol>)', s, re.S):
    cid, body = m.group(1), m.group(2)
    for qm in re.finditer(r'<blockquote class="ps-quote">(.*?)</blockquote>', body, re.S):
        txt = strip_tags(qm.group(1))
        if len(txt) > 10:
            out['ledger'].append({'id': cid, 'text': txt})

with io.open('qa/v10-15/round-02/inventory.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

print(f"X 帖卡 {len(out['tweets'])}（有镜像 id {sum(1 for t in out['tweets'] if t['mirror_id'])}）")
print(f"访谈引语块 {len(out['interviews'])}")
print(f"账本引文块 {len(out['ledger'])}（覆盖 {len(set(x['id'] for x in out['ledger']))} 条目）")
