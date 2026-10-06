# -*- coding: utf-8 -*-
"""R19 ①：transition 审计 TSV（style.css 全量）+ 归一到 --t-fast/--t-slow 两档（白名单注明）。"""
import io, re

src = io.open('style.css', encoding='utf-8').read()
lines = src.split('\n')

rows = []
for i, ln in enumerate(lines, 1):
    for m in re.finditer(r'(transition(?:-delay|-duration)?:\s*[^;]+)', ln):
        rows.append((i, m.group(1).strip(), ln.strip()[:80]))

with io.open('qa/v12/round-19/transition-audit.tsv', 'w', encoding='utf-8', newline='\n') as f:
    f.write('line\tdeclaration\tcontext\taudit\n')
    for i, dec, ctx in rows:
        if 'var(--t-fast)' in dec or 'var(--t-slow)' in dec:
            audit = 'OK 两档内'
        elif 'transition: none' in dec:
            audit = 'OK 显式关闭（reduced-motion/print）'
        elif 'delay' in dec:
            audit = 'WHITELIST reveal 级联节奏（进场编排，非 UI 反馈）'
        elif '1s' in dec:
            audit = 'WHITELIST 图表条形生长动画（数据可视化叙事，非 UI 反馈）'
        elif '0.6s' in dec:
            audit = 'WHITELIST reveal 进场渐显（可见性过渡需大于 fast 档）'
        elif re.search(r'\.25s|0\.25s', dec):
            audit = 'NORMALIZE -> var(--t-fast)（250ms 快档上界）'
        elif re.search(r'\.3s|0\.3s|0\.4s', dec):
            audit = 'NORMALIZE -> var(--t-slow)（300-420ms 慢档）'
        elif '80ms' in dec:
            audit = 'WHITELIST 微反馈快响应（active 态即时感）'
        else:
            audit = 'REVIEW'
        f.write(f'{i}\t{dec}\t{ctx}\t{audit}\n')

# ---- 归一 patch ----
s2 = src
norms = [
    ('transition: all .25s ease;', 'transition: all var(--t-fast);'),
    ('transition: grid-template-rows 0.4s ease;', 'transition: grid-template-rows var(--t-slow);'),
    ('transition: transform 0.3s ease, box-shadow 0.3s ease;', 'transition: transform var(--t-slow), box-shadow var(--t-slow);'),
    ('transition: transform 0.3s ease;', 'transition: transform var(--t-slow);'),
    ('transition: transform .3s ease, opacity .3s ease;', 'transition: transform var(--t-slow), opacity var(--t-slow);'),
]
applied = 0
for a, b in norms:
    n = s2.count(a)
    s2 = s2.replace(a, b)
    applied += n
io.open('style.css', 'w', encoding='utf-8', newline='\n').write(s2)
print('TSV rows:', len(rows), '| normalized rules:', applied)
