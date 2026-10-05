# -*- coding: utf-8 -*-
"""R10 修复 III：还原 events-data.py 前 1018 行（历史档区）为 HEAD 原文——
fixquotes2 误把历史档合法转义引号也改了；R10 新块（1019 行起）的修复保留。"""
import io, subprocess

p = 'tools/events-data.py'
orig = subprocess.run(['git', 'show', 'HEAD:tools/events-data.py'],
                      capture_output=True, text=True, encoding='utf-8').stdout
cur = io.open(p, encoding='utf-8').read().split('\n')
orig_l = orig.split('\n')
print('orig lines:', len(orig_l), 'cur lines:', len(cur))
# 校验：当前 0..1016 行（1..1017）应与 orig 一致或仅引号差异——直接还原
# R10 块插入点：orig 1018 行为 '    },'（0-based 1017），1019 行 ']'（0-based 1018）
assert orig_l[1017].strip() == '},', repr(orig_l[1017])
assert orig_l[1018].strip() == ']', repr(orig_l[1018])
# 还原 0..1017（前 1018 行）为 orig
changed = 0
for i in range(1018):
    if cur[i] != orig_l[i]:
        changed += 1
    cur[i] = orig_l[i]
io.open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(cur))
print('restored historical lines changed by fixquotes2:', changed)
