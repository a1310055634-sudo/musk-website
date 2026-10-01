# -*- coding: utf-8 -*-
"""V9-20 R15 页面级内联样式令牌化（对比度修复 + 色值收敛）。

范围：手维护页面 <style> 块与 style="" 属性内的硬编码值。
  · #8a857c（对比 3.22:1）浅底页脚小字 -> var(--tx-3)（5.02:1）
  · #9a948b（对比 2.64:1）reading 目录待办 -> var(--tx-3)
  · #d9a7a7（深底引注，8.41:1）        -> var(--accent-soft)
  · #9aa3b2（深底冷灰元信息，6.92:1）  -> var(--txd-cool)
仅改内联样式；SVG 图形 fill（R17 范畴）与 @media print 块不动。
"""
import glob
import io
import re

PAIRS = [
    ('#8a857c', 'var(--tx-3)'),
    ('#9a948b', 'var(--tx-3)'),
    ('#d9a7a7', 'var(--accent-soft)'),
    ('#9aa3b2', 'var(--txd-cool)'),
]
PAT = re.compile('|'.join(re.escape(k) for k, _ in PAIRS), re.I)
MAP = {k.lower(): v for k, v in PAIRS}


def conv(text):
    return PAT.sub(lambda m: MAP[m.group(0).lower()], text)


total, files = 0, 0
for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8').read()
    before = PAT.findall(s)

    # 1) <style> 块
    def fix(m):
        return m.group(1) + conv(m.group(2)) + m.group(3)
    s = re.sub(r'(<style[^>]*>)(.*?)(</style>)', fix, s, flags=re.S)
    # 2) style="..." 属性
    s = re.sub(r'(style=")([^"]*)(")', lambda m: m.group(1) + conv(m.group(2)) + m.group(3), s)

    after = PAT.findall(s)
    if before:
        io.open(f, 'w', encoding='utf-8', newline='').write(s)
        print(f'  {f:28s} 内联样式替换 {len(before) - len(after)}（残留 {len(after)}）')
        total += len(before) - len(after)
        files += 1
print(f'合计 {files} 个文件、{total} 处替换')
