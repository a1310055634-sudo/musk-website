# -*- coding: utf-8 -*-
"""v11.1.0 复古杂志方向正式落地：令牌替换 + 硬编码清扫（全部带计数守卫）。"""
import glob
import io
import re
import sys

changed = {}

def sub_count(label, s, old, new, expect=None, flags=0):
    s2, n = re.subn(old, new, s, flags=flags)
    changed[label] = n
    if expect is not None and n != expect:
        print(f'  ⚠ {label}: {n} 处（预期 {expect}）')
    return s2

# ============ style.css :root 令牌 ============
p = 'style.css'
s = io.open(p, encoding='utf-8').read()

pairs = [
    # 纸面五档（暖白 → 奶油）
    ('--paper-0:   #fffdf8;', '--paper-0:   #FFF9F0;'),
    ('--paper-50:  #F7F4EC;', '--paper-50:  #FBF3E4;'),
    ('--paper-100: #F3F0E8;', '--paper-100: #F6EBD7;'),
    ('--paper-150: #EBE7DC;', '--paper-150: #EEE0C9;'),
    ('--paper-200: #E2DDD1;', '--paper-200: #E4D3B8;'),
    # 文字刻度（冷黑 → 暖黑）
    ('--tx-1: #17191d;', '--tx-1: #2B2118;'),
    ('--tx-2: #5b5850;', '--tx-2: #5C4B3A;'),
    ('--tx-3: #6A665D;', '--tx-3: #6E5A45;'),
    ('--tx-4: #8a857c;', '--tx-4: #8A7460;'),
    # 朱红刻度 → 深棕刻度
    ('--accent-deep:   #A63628;', '--accent-deep:   #5C2D0D;'),
    ('--accent:        #C84032;', '--accent:        #8B4513;'),
    ('--accent-bright: #E4765F;', '--accent-bright: #C97B4A;'),
    ('--accent-soft:   #d9a7a7;', '--accent-soft:   #DDBEA0;'),
    ('--accent-glow:   rgba(200, 64, 50, 0.9);', '--accent-glow:   rgba(139, 69, 19, 0.9);'),
    # 色相刻度（豪赌与强调语义保留，值转棕）
    ('--hue-red:      #C84032;', '--hue-red:      #8B4513;'),
]
for old, new in pairs:
    if old not in s:
        sys.exit(f'令牌缺失: {old}')
    s = s.replace(old, new, 1)
    changed['token ' + old.split(':')[0]] = 1

# style.css 内散落 rgba(200, 64, 50 硬编码 → 新棕（--accent-glow 定义已换，其余为历史硬编码）
s, n = re.subn(r'rgba\(200, 64, 50', 'rgba(139, 69, 19', s)
changed['css rgba(200,64,50) 硬编码'] = n
# style.css 内残留 #C84032（若有）
s, n = re.subn(r'#C84032', '#8B4513', s, flags=re.I)
changed['css #C84032 残留'] = n

io.open(p, 'w', encoding='utf-8', newline='').write(s)
for k, v in changed.items():
    print(f'  {k}: {v}')

# ============ HTML 侧：favicon 与内联旧色 ============
fav_n = 0
theme_n = 0
inline_n = 0
for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8').read()
    orig = s
    s2, a = re.subn(r'%23C84032', '%238B4513', s, flags=re.I)
    fav_n += a
    s3, b = re.subn(r'%237c2d2d', '%238B4513', s2, flags=re.I)
    fav_n += b
    s4, c = re.subn(r'(<meta name="theme-color" content=")#C84032(")', r'\g<1>#8B4513\g<2>', s3, flags=re.I)
    theme_n += c
    s5, d = re.subn(r'#C84032', '#8B4513', s4, flags=re.I)
    inline_n += d
    if s5 != orig:
        io.open(f, 'w', encoding='utf-8', newline='').write(s5)
print(f'  favicon/内联: %23C84032+7c2d2d {fav_n} 处, theme-color {theme_n} 处, 其他内联 {inline_n} 处')

# ============ 复核：全站不应再有旧朱红（除风格试衣间预览工具） ============
left = 0
for f in sorted(glob.glob('*.html')) + ['style.css', 'app.js']:
    s = io.open(f, encoding='utf-8').read()
    n = len(re.findall(r'C84032|7c2d2d', s, re.I))
    if n:
        print(f'  ⚠ 残留 {f}: {n}')
        left += n
print('旧色残留总计:', left, '（preview-v12.html 试衣间不计）')
