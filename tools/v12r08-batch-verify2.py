# -*- coding: utf-8 -*-
"""R08 批量核验 II：补漏——超时重试/EDGAR MISS 换短语/ted JSON/jre 转录。"""
import io, json, re, time, urllib.request, urllib.parse

payload = {o['id']: o for o in json.load(io.open('qa/v12/round-08/quotes-payload.json', encoding='utf-8'))}
res = json.load(io.open('qa/v12/round-08/mirror-edgar-results.json', encoding='utf-8'))

def http_json(url, ua):
    req = urllib.request.Request(url, headers={'User-Agent': ua})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def alt_phrases(quote):
    ws = re.findall(r"[A-Za-z0-9'$%-]+", quote)
    outs = []
    if len(ws) >= 12:
        outs.append(' '.join(ws[-10:]))
        outs.append(' '.join(ws[3:13]))
    if len(ws) >= 6:
        outs.append(' '.join(ws[:6]))
        outs.append(' '.join(ws[-6:]))
    return outs

# 1) e2022-10-28 超时重试（镜像）
for qid in ['e2022-10-28']:
    o = payload[qid]
    try:
        url = 'https://elonmuskarchive.org/agents/search?q=' + urllib.parse.quote(o['q'])
        d = http_json(url, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')
        items = d if isinstance(d, list) else d.get('results', d.get('items', []))
        needle = res[qid]['needle']
        hit = any(needle in json.dumps(it, ensure_ascii=False).lower() for it in (items or []))
        res[qid]['verdict'] = 'YES' if hit else 'MISS'
        if hit:
            res[qid]['anchor'] = (items[0].get('url') if items else '')
        print(qid, 'retry', res[qid]['verdict'])
    except Exception as e:
        print(qid, 'retry-err', str(e)[:50])
    time.sleep(0.8)

# 2) EDGAR MISS 3 条换短语重试
rows = [l.split('\t') for l in io.open('qa/v12/round-01/quotes-worklog.tsv', encoding='utf-8').read().split('\n') if l.strip()]
edgar_miss = [r[0] for r in rows[1:] if r[1].startswith('edgar') and res.get(r[0], {}).get('verdict') == 'MISS']
for qid in edgar_miss:
    o = payload[qid]
    got = False
    for ph in alt_phrases(o['quote']):
        try:
            url = 'https://efts.sec.gov/LATEST/search-index?q=' + urllib.parse.quote('"' + ph + '"')
            d = http_json(url, 'MuskArchiveResearch admin@example.com')
            hits = d.get('hits', {}).get('total', {}).get('value', 0)
            if hits:
                first = d['hits']['hits'][0]
                res[qid]['verdict'] = 'YES'
                res[qid]['anchor'] = 'https://efts.sec.gov/LATEST/search-index?q=' + urllib.parse.quote(ph) + ' | ' + first.get('_id', '')[:60]
                got = True
                print(qid, 'edgar-YES via', ph[:40])
                break
        except Exception as e:
            print(qid, 'edgar-err', str(e)[:40])
        time.sleep(0.6)
    if not got:
        print(qid, 'edgar-still-MISS')

# 3) ted 1 条：ted.com 页面找 transcript JSON
qid_ted = [r[0] for r in rows[1:] if r[1].startswith('ted.com')][0]
o = payload[qid_ted]
print('TED:', qid_ted, '| needle:', res[qid_ted]['needle'])
print('   quote:', o['quote'][:120])

# 4) jre 1 条
qid_jre = [r[0] for r in rows[1:] if r[1].startswith('jre')][0]
o = payload[qid_jre]
print('JRE:', qid_jre, '| needle:', res[qid_jre]['needle'])
print('   quote:', o['quote'][:120])

io.open('qa/v12/round-08/mirror-edgar-results.json', 'w', encoding='utf-8', newline='\n').write(
    json.dumps(res, ensure_ascii=False, indent=1))
from collections import Counter
print('NOW:', Counter(v['verdict'].split(':')[0] for v in res.values()))
