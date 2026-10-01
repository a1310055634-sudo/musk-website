# -*- coding: utf-8 -*-
"""V10-15 N04：resources-data.py 36 条全量复测。

复用 N01 直连/api 结果（qa/v10-15/round-01/sources-report.json，2026-10-02 同日）
+ GitHub api 串行刷新 stars/pushed → 生成刷新补丁清单（人工核对后以脚本写回数据）。
输出 qa/v10-15/round-04/recheck.tsv。
"""
import glob
import io
import json
import os
import re
import time
import urllib.request

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0.0.0'

# 1) 载入资源清单（不 import 数据文件——直接读 URL 与 gh 字段）
src = io.open('tools/resources-data.py', encoding='utf-8').read()
ids = re.findall(r'"id": "([a-z0-9-]+)"', src)
urls = re.findall(r'"url": "(https?://[^"]+)"', src)
items = list(zip(ids, urls))
print(f'resources-data.py 共 {len(items)} 条')

# 2) N01 报告（同日直连/api 结果）
n01 = {}
try:
    rep = json.load(io.open('qa/v10-15/round-01/sources-report.json', encoding='utf-8'))
    for r in rep:
        if isinstance(r, dict) and 'url' in r:
            n01[r['url']] = (r.get('http'), r.get('verdict'), r.get('verdict2', ''))
except Exception as e:
    print('N01 report load fail:', e)

# 3) GitHub api 刷新（gh 条目）
gh_ids = re.findall(r'"id": "([a-z0-9-]+)",[\s\S]{0,600}?"url": "(https://github\.com/[^"]+)"', src)
print(f'GitHub 条目 {len(gh_ids)}')
gh_new = {}
for rid, u in gh_ids:
    repo = u.replace('https://github.com/', '').strip('/')
    if repo.count('/') != 1:
        continue
    try:
        req = urllib.request.Request(f'https://api.github.com/repos/{repo}', headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.load(r)
        gh_new[rid] = {'stars': d['stargazers_count'], 'pushed': str(d['pushed_at'])[:7],
                       'archived': d.get('archived')}
        print(f"  {rid}: ★{d['stargazers_count']} pushed {str(d['pushed_at'])[:7]} archived={d.get('archived')}")
    except Exception as e:
        print(f'  {rid} API FAIL {str(e)[:50]}')
    time.sleep(1.5)

# 4) 汇总
rows = []
for rid, u in items:
    h1, v1, v2 = n01.get(u, (None, 'no-n01', ''))
    rows.append({'id': rid, 'url': u, 'n01_http': h1, 'n01_verdict': v1 or v2,
                 'gh': gh_new.get(rid)})
with io.open('qa/v10-15/round-04/recheck.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
with io.open('qa/v10-15/round-04/recheck.tsv', 'w', encoding='utf-8', newline='\n') as f:
    f.write('id\tn01_verdict\tgh_stars\tgh_pushed\tgh_archived\n')
    for r in rows:
        g = r['gh'] or {}
        f.write(f"{r['id']}\t{r['n01_verdict']}\t{g.get('stars','')}\t{g.get('pushed','')}\t{g.get('archived','')}\n")
print('recheck saved')
