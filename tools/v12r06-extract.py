# -*- coding: utf-8 -*-
"""R06 采料：从四封镜像详情页 HTML（RSC payload）提取正文引语字符串。"""
import io, re, os

BASE = os.path.join('qa', 'v12', 'round-06', 'sources')
FILES = [
    'musk-texts-ellison-billion-2022',
    'openai-bait-and-switch-2023',
    'openai-altman-my-hero-2023',
    'twitter-first-email-remote-2022',
]
KEYS = ('Elon', 'billion', 'hero', 'hurts', 'civilization', 'bait',
        'remote', 'office', 'Twitter', 'OpenAI', 'Microsoft', 'deal',
        'Ellison', 'Altman', 'Thursday', '40 hours')

for f in FILES:
    raw = io.open(os.path.join(BASE, f + '.html'), encoding='utf-8').read()
    m = re.findall(r'"((?:[^"\\]|\\.){60,600})"', raw)
    seen = set()
    print('=' * 20, f)
    for s in m:
        t = s.encode('latin-1', errors='ignore').decode('unicode_escape', errors='ignore')
        if t in seen or 'className' in t or 'href' in t:
            continue
        seen.add(t)
        if any(k in t for k in KEYS):
            print('-', t[:500])
