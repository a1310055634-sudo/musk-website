# -*- coding: utf-8 -*-
"""V9-20 R19 性能复测：五页 load 计时 + 资源体积清单（本地条件如实记录）。"""
import io
import json
import os
import subprocess
import time
import urllib.request

PAGES = ['index.html', 'primary.html', 'timeline.html', 'capital-evolution.html', 'resources.html']
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0.0.0'}

print('== 资源体积（站点根） ==')
files = ['style.css', 'app.js', 'search-index.js', 'cite.js', 'musk-inc.epub']
sizes = {}
for f in files:
    if os.path.exists(f):
        b = os.path.getsize(f)
        sizes[f] = b
        print(f'  {f}: {b:,} B ({b/1024:.1f} kB)')
html_kb = sum(os.path.getsize(f) for f in os.listdir('.') if f.endswith('.html'))
print(f'  *.html 合计: {html_kb:,} B ({html_kb/1024:.1f} kB)，共 {sum(1 for f in os.listdir(".") if f.endswith(".html"))} 页')

print('\n== 五页 load 计时（urllib 全文取回，串行 3 轮取中位） ==')
loads = {}
for pg in PAGES:
    ts = []
    for _ in range(3):
        t0 = time.time()
        req = urllib.request.Request(f'http://127.0.0.1:8766/{pg}', headers=UA)
        with urllib.request.urlopen(req, timeout=15) as r:
            r.read()
        ts.append((time.time() - t0) * 1000)
    ts.sort()
    loads[pg] = round(ts[1], 1)
    print(f'  {pg}: 中位 {loads[pg]} ms（{ts}）')

out = {'sizes_bytes': sizes, 'html_total_bytes': html_kb, 'load_ms_median': loads,
       'note': '本机条件：127.0.0.1 http.server + Python urllib 全文取回（非浏览器首屏渲染时间），如实记录口径'}
with io.open('qa/v9-20/round-19/perf.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print('\nperf.json saved')
