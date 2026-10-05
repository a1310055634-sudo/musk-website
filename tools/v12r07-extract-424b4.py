# -*- coding: utf-8 -*-
"""R07 采料 IV：SpaceX 424B4 封面关键段（发行价/规模/募资用途/结构）。"""
import io, os, re, html

raw = io.open(os.path.join('qa', 'v12', 'round-07', 'sources', 'spcx-424b4.html'),
              encoding='utf-8', errors='ignore').read()
t = re.sub(r'<[^>]+>', ' ', raw)
t = html.unescape(t)
t = re.sub(r'\s+', ' ', t)
print('len:', len(t))

for kw in ['Initial public offering price', 'per share', 'We are offering',
           'use the net proceeds', 'proceeds of this offering to',
           'Class A common stock offered by us']:
    idx = t.find(kw)
    if idx >= 0:
        print('---', kw, '---')
        print(t[max(0, idx - 250):idx + 700])
        print()
