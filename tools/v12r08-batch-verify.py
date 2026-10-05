# -*- coding: utf-8 -*-
"""R08 批量核验 I：镜像 /agents/search（75 条）+ EDGAR FTS（6 条）。
命中判定：结果条目 title/snippet 含引语中段 6 词子串（避开开头大写/引号噪声）。"""
import io, json, re, time, urllib.request, urllib.parse, os

payload = json.load(io.open('qa/v12/round-08/quotes-payload.json', encoding='utf-8'))
rows = [l.split('\t') for l in io.open('qa/v12/round-01/quotes-worklog.tsv', encoding='utf-8').read().split('\n') if l.strip()]
src_of = {r[0]: r[1] for r in rows[1:]}

def midwords(quote, n=6):
    ws = re.findall(r"[A-Za-z0-9'$%-]+", quote)
    if len(ws) <= n:
        return ' '.join(ws)
    start = max(0, (len(ws) - n) // 2)
    return ' '.join(ws[start:start + n]).lower()

def mirror_search(phrase):
    url = 'https://elonmuskarchive.org/agents/search?q=' + urllib.parse.quote(phrase)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)

def edgar_fts(phrase):
    url = 'https://efts.sec.gov/LATEST/search-index?q=' + urllib.parse.quote('"' + phrase + '"')
    req = urllib.request.Request(url, headers={'User-Agent': 'MuskArchiveResearch admin@example.com'})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)

results = {}
for o in payload:
    qid, quote, phrase = o['id'], o['quote'], o['q']
    src = src_of.get(qid, '')
    needle = midwords(quote)
    verdict = ''
    anchor = ''
    if src.startswith('edgar'):
        try:
            d = edgar_fts(needle)
            hits = d.get('hits', {}).get('total', {}).get('value', 0)
            if hits:
                first = d['hits']['hits'][0]
                verdict = 'YES'
                anchor = 'https://efts.sec.gov/LATEST/search-index?q=' + urllib.parse.quote(needle) + ' | ' + first.get('_id', '')[:60]
            else:
                verdict = 'MISS'
        except Exception as e:
            verdict = 'ERR:' + str(e)[:40]
        time.sleep(0.6)
    else:
        try:
            d = mirror_search(phrase)
            items = d if isinstance(d, list) else d.get('results', d.get('items', []))
            hit = False
            for it in items or []:
                blob = json.dumps(it, ensure_ascii=False).lower()
                if needle in blob:
                    hit = True
                    anchor = it.get('url') or it.get('id') or ''
                    break
            verdict = 'YES' if hit else 'MISS'
        except Exception as e:
            verdict = 'ERR:' + str(e)[:40]
        time.sleep(0.4)
    results[qid] = {'verdict': verdict, 'anchor': anchor, 'needle': needle}
    print(qid, verdict, anchor[:60])

io.open('qa/v12/round-08/mirror-edgar-results.json', 'w', encoding='utf-8', newline='\n').write(
    json.dumps(results, ensure_ascii=False, indent=1))
from collections import Counter
print('SUMMARY:', Counter(v['verdict'].split(':')[0] for v in results.values()))
