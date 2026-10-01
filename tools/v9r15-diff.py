# -*- coding: utf-8 -*-
"""V9-20 R15 before/after 像素差异报告：量化美术升级的可辨度。

用法: <venv-python> tools/v9r15-diff.py
输出：每张对比图的尺寸一致性、变化像素占比、平均通道差、最大差、变化区域纵向分布。
"""
import os
import sys
from PIL import Image, ImageChops

BASE = 'qa/v9-20/round-15'
pairs = []
for f in sorted(os.listdir(os.path.join(BASE, 'before'))):
    if f.endswith('.png'):
        pairs.append((f, os.path.join(BASE, 'before', f), os.path.join(BASE, 'after', f)))

print('%-38s %-16s %8s %8s %7s %8s' % ('file', 'size', 'diffPx%', 'meanΔ', 'maxΔ', 'band10%'))
tot = []
for name, pb, pa in pairs:
    if not os.path.exists(pa):
        print('%-38s MISSING' % name)
        continue
    a, b = Image.open(pb).convert('RGB'), Image.open(pa).convert('RGB')
    same_size = a.size == b.size
    if not same_size:
        print('%-38s SIZE DIFF %s vs %s' % (name, a.size, b.size))
        continue
    diff = ImageChops.difference(a, b)
    px = list(diff.getdata())
    n = len(px)
    changed = sum(1 for p in px if p != (0, 0, 0))
    mean = sum(sum(p) for p in px) / (3.0 * n)
    mx = max(max(p) for p in px)
    # 变化像素的纵向分布（10 段）
    w, h = a.size
    bands = [0] * 10
    chg = diff.getdata()
    idx = 0
    for y in range(h):
        row_changed = 0
        for x in range(w):
            if chg[idx] != (0, 0, 0):
                row_changed += 1
            idx += 1
        bands[min(9, y * 10 // h)] += row_changed
    top = max(range(10), key=lambda i: bands[i])
    print('%-38s %-16s %7.2f%% %8.3f %7d   峰值段%d(%.0f%%)' % (
        name, '%dx%d' % a.size, 100.0 * changed / n, mean, mx, top, 100.0 * bands[top] / max(1, changed)))
    tot.append(100.0 * changed / n)
if tot:
    print('\n变化像素占比：min %.2f%% / 中位 %.2f%% / max %.2f%%（%d 张）' % (
        min(tot), sorted(tot)[len(tot) // 2], max(tot), len(tot)))
