# -*- coding: utf-8 -*-
"""V9-20 R16 像素差异量化 + 首屏并排对比图（Pillow）。
全页逐像素差异（before vs after 各 6 张）+ desktop/tablet/mobile zh 首屏 900px 并排对比拼图。"""
import io, os
from PIL import Image, ImageDraw

BASE = 'qa/v9-20/round-16'
VENVPY = None  # 用当前解释器（已带 Pillow 的环境跑）

NAMES = ['index-desktop-zh.png', 'index-desktop-en.png',
         'index-tablet-zh.png', 'index-tablet-en.png',
         'index-mobile-zh.png', 'index-mobile-en.png']

def diff_one(before_path, after_path):
    a = Image.open(before_path).convert('RGB')
    b = Image.open(after_path).convert('RGB')
    if a.size != b.size:
        # 高度不一致时按较短者裁剪再比（记录原始尺寸差）
        h = min(a.size[1], b.size[1])
        w = min(a.size[0], b.size[0])
        a = a.crop((0, 0, w, h)); b = b.crop((0, 0, w, h))
        sizediff = True
    else:
        sizediff = False
    pa, pb = a.load(), b.load()
    W, H = a.size
    diffpx = 0; maxd = 0; s = 0; band = [0]*10
    for y in range(H):
        for x in range(W):
            p1, p2 = pa[x, y], pb[x, y]
            d = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])
            if d > 0:
                diffpx += 1; s += d
                if d > maxd: maxd = d
                band[min(y*10//H, 9)] += 1
    total = W*H
    mean = (s/total) if total else 0
    peak = max(range(10), key=lambda i: band[i])
    return {
        'size': '%dx%d%s' % (W, H, '(裁齐)' if sizediff else ''),
        'pct': diffpx*100.0/total,
        'mean': mean/3.0,
        'maxd': maxd,
        'peakband': '段%d(%.0f%%)' % (peak, band[peak]*100.0/max(diffpx,1)),
    }

print('%-28s %-16s %9s %8s %6s %s' % ('file', 'size', 'diffPx%', 'mean', 'maxD', 'band'))
pcts = []
for n in NAMES:
    r = diff_one(os.path.join(BASE, 'before', n), os.path.join(BASE, 'after', n))
    pcts.append(r['pct'])
    print('%-28s %-16s %8.2f%% %8.3f %6d %s' % (n, r['size'], r['pct'], r['mean'], r['maxd'], r['peakband']))
pcts.sort()
print('\n变化像素占比：min %.2f%% / 中位 %.2f%% / max %.2f%%（6 张）' % (pcts[0], pcts[2]/2+pcts[3]/2, pcts[-1]))

# ---- 首屏并排对比拼图（zh 三视口，各取首屏 900px）----
GAP = 24; LABEL_H = 46
for tag, w in [('desktop', 1440), ('tablet', 768), ('mobile', 390)]:
    n = 'index-%s-zh.png' % tag
    a = Image.open(os.path.join(BASE, 'before', n)).convert('RGB').crop((0, 0, w, min(900, Image.open(os.path.join(BASE, 'before', n)).size[1])))
    b = Image.open(os.path.join(BASE, 'after', n)).convert('RGB').crop((0, 0, w, min(900, Image.open(os.path.join(BASE, 'after', n)).size[1])))
    H = max(a.size[1], b.size[1])
    canvas = Image.new('RGB', (w*2+GAP, H+LABEL_H), '#EBE7DC')
    canvas.paste(a, (0, LABEL_H)); canvas.paste(b, (w+GAP, LABEL_H))
    d = ImageDraw.Draw(canvas)
    d.text((18, 12), 'BEFORE  v9.5.0', fill='#A63628')
    d.text((w+GAP+18, 12), 'AFTER  v9.6.0 (R16)', fill='#A63628')
    out = os.path.join(BASE, 'compare', 'cmp-firstscreen-%s-zh.png' % tag)
    canvas.save(out)
    print('saved %s (%dx%d)' % (out, canvas.size[0], canvas.size[1]))
