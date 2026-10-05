# -*- coding: utf-8 -*-
"""R08 专路：TED transcript JSON 段落匹配 + EDGAR MISS 三条引语内容。"""
import io, os, re, json, html

raw = io.open(os.path.join(os.environ['TEMP'], 'ted-talk.html'), encoding='utf-8', errors='ignore').read()
# __NEXT_DATA__ JSON
m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', raw, re.S)
if m:
    data = json.loads(m.group(1))
    blob = json.dumps(data, ensure_ascii=False)
    # 找段落文本
    hits = []
    for kw in ['make money', 'inclusive arena', 'don&#x27;t care', "don't care", 'economics']:
        for mm in re.finditer(re.escape(kw), blob):
            hits.append(blob[max(0, mm.start() - 150):mm.end() + 150])
            break
    print('NEXT_DATA found, kw hits:', len(hits))
    for h in hits[:3]:
        print(' -', html.unescape(h)[:280])
else:
    # 退路：transcript 字段全文搜索
    tm = re.search(r'"transcripts?":\s*(\{.*?\})\s*,\s*"', raw[:400000], re.S)
    print('fallback transcript field:', bool(tm))

print()
payload = {o['id']: o for o in json.load(io.open('qa/v12/round-08/quotes-payload.json', encoding='utf-8'))}
for qid in ['e2018-09-27', 'e2019-02-19', 'e2022-03-08']:
    print(qid, '|', payload[qid]['quote'][:150])
