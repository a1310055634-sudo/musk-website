# -*- coding: utf-8 -*-
"""v11.1.0 复古杂志对比度复测：新令牌全部组合 WCAG 2.1。"""
import io
import sys

sys.path.insert(0, 'tools')
from importlib import util as _iu

spec = _iu.spec_from_file_location('c', 'tools/v9r15-contrast.py')
_c = _iu.module_from_spec(spec)
spec.loader.exec_module(_c)
ratio = _c.ratio

PAPER = '#F6EBD7'
PAPER0 = '#FFF9F0'
CARD = '#EEE0C9'
COAL = '#101316'

print('=== 浅底（--paper #F6EBD7） ===')
light = [
    ('--tx-1 #2B2118（正文）', '#2B2118'),
    ('--tx-2 #5C4B3A（次级）', '#5C4B3A'),
    ('--tx-3 #6E5A45（三级）', '#6E5A45'),
    ('--tx-4 #8A7460（装饰/大字）', '#8A7460'),
    ('--accent-deep #5C2D0D（浅底小字）', '#5C2D0D'),
    ('--accent #8B4513（大字/边框）', '#8B4513'),
    ('--hue-navy #1f3a5f', '#1f3a5f'),
    ('--hue-olive #4a6b3a', '#4a6b3a'),
    ('--hue-ochre #8a5a00', '#8a5a00'),
    ('--hue-graphite #55524c', '#55524c'),
]
fails = []
for name, fg in light:
    r = ratio(fg, PAPER)
    mark = '✓' if r >= 4.5 else ('~' if r >= 3.0 else '✗')
    print(f'  {mark} {name}: {r:.2f}')
    if r < 3.0:
        fails.append((name, r))

print('=== 卡片面（--paper-150 #EEE0C9） ===')
for name, fg in light[:6]:
    r = ratio(fg, CARD)
    mark = '✓' if r >= 4.5 else ('~' if r >= 3.0 else '✗')
    print(f'  {mark} {name}: {r:.2f}')
    if r < 3.0:
        fails.append((name + '@card', r))

print('=== 深底（--coal #101316） ===')
dark = [
    ('--txd-2 #F3F0E8', '#F3F0E8'),
    ('--accent-bright #C97B4A（暗底小字）', '#C97B4A'),
    ('--accent-soft #DDBEA0（暗底引注）', '#DDBEA0'),
    ('--txd-cool #9aa3b2', '#9aa3b2'),
]
for name, fg in dark:
    r = ratio(fg, COAL)
    mark = '✓' if r >= 4.5 else ('~' if r >= 3.0 else '✗')
    print(f'  {mark} {name}: {r:.2f}')
    if r < 4.5:
        fails.append((name, r))

print('=== 白字落在强调填充上（按钮） ===')
for name, bg in [
    ('白 on --accent #8B4513', '#8B4513'),
    ('白 on --accent-deep #5C2D0D', '#5C2D0D'),
    ('白 on --hue-red #8B4513', '#8B4513'),
]:
    r = ratio('#FFFFFF', bg)
    mark = '✓' if r >= 4.5 else '~'
    print(f'  {mark} {name}: {r:.2f}')
    if r < 4.5:
        fails.append((name, r))

print()
print('不达标（<3.0 浅底 / <4.5 深底白字）:', fails if fails else '无')
