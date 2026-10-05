# -*- coding: utf-8 -*-
"""R07 采料：EDGAR 2025 proxy（万亿薪酬包）与 10-K FY2025（风险因子）关键段抽取。"""
import io, os, re, html

BASE = os.path.join('qa', 'v12', 'round-07', 'sources')

def load(name):
    raw = io.open(os.path.join(BASE, name), encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<[^>]+>', ' ', raw)
    t = html.unescape(t)
    t = re.sub(r'\s+', ' ', t)
    return t

proxy = load('tesla-def14a-2025.html')
tenk = load('tesla-10k-fy2025.html')

print('=== proxy 2025: 2025 CEO Performance Award 关键句 ===')
for kw in ['2025 CEO Performance Award', 'Chief Executive Officer Performance Award',
           '12 trillion', '$2 trillion', 'market capitalization of']:
    for m in re.finditer(re.escape(kw), proxy):
        s = max(0, m.start() - 350)
        print('---', kw, '---')
        print(proxy[s:m.end() + 450])
        break

print()
print('=== 10-K FY2025: 风险因子关键句 ===')
for kw in ['highly dependent on the services of Elon Musk', 'kejrival', 'highly dependent on the services of Musk',
           'depends on the services of Elon Musk', 'artificial intelligence', 'Highly Qualified Personnel',
           'we may not be able to force']:
    idx = tenk.find(kw)
    if idx >= 0:
        s = max(0, idx - 300)
        print('---', kw, '---')
        print(tenk[s:idx + 600])
