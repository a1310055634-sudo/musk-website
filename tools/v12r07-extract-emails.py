# -*- coding: utf-8 -*-
"""R07 采料 II：两封镜像 email（dorsey-protocol / pif-alrumayyan）正文抽取。"""
import io, os, re

BASE = os.path.join('qa', 'v12', 'round-07', 'sources')
FILES = ['musk-texts-dorsey-protocol-2022', 'tesla-pif-alrumayyan-texts-2018']
KEYS = ('Elon', 'Dorsey', 'protocol', 'platform', 'company', 'Twitter',
        'PIF', 'Alrumayyan', 'bus', 'Tesla', 'private', 'deal', 'funding')

for f in FILES:
    raw = io.open(os.path.join(BASE, f + '.html'), encoding='utf-8').read()
    m = re.findall(r'"((?:[^"\\]|\\.){50,600})"', raw)
    seen = set()
    print('=' * 20, f)
    for s in m:
        t = s.encode('latin-1', errors='ignore').decode('unicode_escape', errors='ignore')
        if t in seen or 'className' in t or 'href' in t:
            continue
        seen.add(t)
        if any(k in t for k in KEYS):
            print('-', t[:500])
