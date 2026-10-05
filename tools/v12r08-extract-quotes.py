# -*- coding: utf-8 -*-
"""R08 采料：从 primary.html 提取 worklog 101 条的引语与查询短语（前 10 词）。"""
import io, json, re, html

TQ = 'qa/v12/round-01/quotes-worklog.tsv'
rows = [l.split('\t') for l in io.open(TQ, encoding='utf-8').read().split('\n') if l.strip()]
ids = [r[0] for r in rows[1:]]

prim = io.open('primary.html', encoding='utf-8').read()
# ps-row 块切分
blocks = re.split(r'(<li class="ps-row[^"]*" id=")', prim)
# 重建 id -> 块文本
found = {}
for i in range(1, len(blocks) - 1, 2):
    m = re.match(r'id="([^"]+)"', blocks[i + 1]) if False else re.search(r'id="([^"]+)"', blocks[i] + blocks[i + 1])
    seg = blocks[i] + blocks[i + 1]
    mm = re.search(r'id="(e[^"]+)"', seg[:200])
    if mm:
        found[mm.group(1)] = seg

out = []
missing = []
for qid in ids:
    seg = found.get(qid, '')
    if not seg:
        missing.append(qid)
        out.append({'id': qid, 'quote': '', 'q': '', 'first': ''})
        continue
    qm = re.search(r'<blockquote class="ps-quote">(.*?)</blockquote>', seg, re.S)
    if not qm:
        out.append({'id': qid, 'quote': '', 'q': '', 'first': ''})
        continue
    qt = html.unescape(re.sub(r'<[^>]+>', '', qm.group(1)))
    qt = re.sub(r'\s+', ' ', qt).strip()
    qt = qt.strip('\u201c\u201d "\u2018\u2019 ')
    # 取第一段引语的前 10 个英文词做镜像查询短语
    first = re.split(r'[—–/]|\.\s', qt)[0] if qt else ''
    words = re.findall(r"[A-Za-z0-9'$.,%-]+", first)
    phrase = ' '.join(words[:10]).strip(" .,;:!?'\"")
    out.append({'id': qid, 'quote': qt[:200], 'q': phrase, 'first': first[:120]})

io.open('qa/v12/round-08/quotes-payload.json', 'w', encoding='utf-8', newline='\n').write(
    json.dumps(out, ensure_ascii=False, indent=1))
print('total:', len(out), 'missing-in-primary:', len(missing))
empty_q = [o['id'] for o in out if not o['q']]
print('empty-phrase:', len(empty_q), empty_q[:10])
for o in out[:5]:
    print(o['id'], '|', o['q'][:70])
