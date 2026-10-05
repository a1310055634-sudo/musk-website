# -*- coding: utf-8 -*-
"""R07 采料 III：pif 正文全文抽取（under the bus 上下文）。"""
import io, re

raw = io.open('qa/v12/round-07/sources/tesla-pif-alrumayyan-texts-2018.html', encoding='utf-8').read()
pat = re.compile(r'"((?:[^"\\]|\\.){40,800})"')
positions = []
start = 0
while True:
    i = raw.find('under the bus', start)
    if i < 0:
        break
    positions.append(i)
    start = i + 1
print('hits:', len(positions))
seen = set()
for pos in positions:
    seg = raw[max(0, pos - 500):pos + 1200]
    for t in pat.findall(seg):
        u = t.encode('latin-1', errors='ignore').decode('unicode_escape', errors='ignore')
        if u in seen:
            continue
        seen.add(u)
        print('-', u[:800])
        print()
