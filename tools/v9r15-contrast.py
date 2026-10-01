# -*- coding: utf-8 -*-
"""V9-20 R15 对比度核验：WCAG 2.1 相对亮度与对比度比。"""

def _lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def lum(css):
    s = css.lstrip('#')
    r, g, b = int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def over(fg, bg, alpha):
    """fg(带 alpha) 叠在 bg 上的实色。"""
    f = fg.lstrip('#')
    b = bg.lstrip('#')
    out = []
    for i in (0, 2, 4):
        fc = int(f[i:i + 2], 16)
        bc = int(b[i:i + 2], 16)
        out.append(round(fc * alpha + bc * (1 - alpha)))
    return '#%02X%02X%02X' % tuple(out)


def ratio(fg, bg):
    a, b = lum(fg), lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


PAPER = '#F3F0E8'
COAL = '#101316'
INK = '#17191d'
CARD = '#EBE7DC'

print('=== 浅底（--paper #F3F0E8）上的文字 ===')
light = [
    ('--ink #17191d', '#17191d'),
    ('--muted #5b5850', '#5b5850'),
    ('--accent-text #A63628', '#A63628'),
    ('accent #C84032', '#C84032'),
    ('n-45 #8a857c', '#8a857c'),
    ('n-40 #9a948b', '#9a948b'),
    ('ty-start #4a6b3a', '#4a6b3a'),
    ('ty-deal #1f3a5f', '#1f3a5f'),
    ('ty-milestone #55524c', '#55524c'),
    ('ty-risk #8a5a00', '#8a5a00'),
    ('ty-ok #1c7c40', '#1c7c40'),
]
for name, c in light:
    r = ratio(c, PAPER)
    print(f'  {name:26s} vs paper = {r:5.2f}  {"PASS" if r >= 4.5 else "FAIL"}')

print('=== 浅底卡片（--card #EBE7DC）===')
for name, c in [('--muted #5b5850', '#5b5850'), ('--accent-text #A63628', '#A63628')]:
    r = ratio(c, CARD)
    print(f'  {name:26s} vs card  = {r:5.2f}  {"PASS" if r >= 4.5 else "FAIL"}')

print('=== 深底（--coal #101316）上的文字 ===')
mist = over('#F3F0E8', COAL, 0.74)
dark = [
    ('--mist (paper@74%)', mist),
    ('--accent-bright #E4765F', '#E4765F'),
    ('accent-soft #d9a7a7', '#d9a7a7'),
    ('n-20 #d9d4cc', '#d9d4cc'),
    ('accent #C84032', '#C84032'),
]
for name, c in dark:
    r = ratio(c, COAL)
    print(f'  {name:26s} vs coal  = {r:5.2f}  {"PASS" if r >= 4.5 else "FAIL"}')

print('=== 深底页脚（--ink #17191d）===')
foot = [
    ('--mist #F3F0E8@74', over('#F3F0E8', INK, 0.74)),
    ('n-35 #b3aea3', '#b3aea3'),
    ('n-30 #a8a399', '#a8a399'),
    ('n-25 #d8d4cb', '#d8d4cb'),
    ('n-20 #d9d4cc', '#d9d4cc'),
]
for name, c in foot:
    r = ratio(c, INK)
    print(f'  {name:26s} vs ink   = {r:5.2f}  {"PASS" if r >= 4.5 else "FAIL"}')
