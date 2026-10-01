# -*- coding: utf-8 -*-
"""V10-15 N07：镜像 2018/2019 X 帖全量回捞（按月切片 24 月）+ 关键词候选过滤。"""
import io
import json
import os
import time
import urllib.request

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UA = 'Mozilla/5.0 Chrome/128.0.0.0'
KEYWORDS = ['falcon heavy', 'starman', 'starlink', 'model y', 'telsa', 'tesla',
            'funding', 'secured', 'ying ying', 'short shorts', 'sorry']

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode('utf-8', 'ignore'))

all_posts = {}
for y in (2018, 2019):
    for mo in range(1, 13):
        try:
            d = fetch(f'https://elonmuskarchive.org/agents/index?type=posts&year={y}&month={mo:02d}&list=1&fields=id,date,title,url&sort=date_asc')
            entries = d.get('entries') or d.get('results') or []
            all_posts[f'{y}-{mo:02d}'] = len(entries)
            for e in entries:
                all_posts.setdefault('_items', [])
                all_posts['_items'].append({'id': e.get('id'), 'date': e.get('date'), 'title': e.get('title')})
            print(f'{y}-{mo:02d}: {len(entries)}')
        except Exception as e:
            all_posts[f'{y}-{mo:02d}'] = f'ERR {str(e)[:40]}'
            print(f'{y}-{mo:02d}: ERR {str(e)[:40]}')
        time.sleep(0.5)

items = all_posts.pop('_items', [])
total = sum(v for k, v in all_posts.items() if isinstance(v, int))
print(f'\n2018-2019 总计 {total} 帖（清单 {len(items)} 条）')

# 关键词候选
cands = []
for it in items:
    tl = (it.get('title') or '').lower()
    if any(k in tl for k in KEYWORDS):
        cands.append(it)
print(f'\n关键词候选 {len(cands)} 条：')
for c in cands[:40]:
    print(' ', c['date'], c['id'], '|', (c.get('title') or '')[:90])

io.open('qa/v10-15/round-07/walk-2018-2019.json', 'w', encoding='utf-8').write(
    json.dumps({'months': all_posts, 'total': total, 'candidates': cands, 'all': items},
               ensure_ascii=False, indent=1))
print('\nwalk-2018-2019.json saved')
