# -*- coding: utf-8 -*-
"""V10-15 N04：把复测结果写回 resources-data.py（checked 全刷 2026-10-02 + gh 刷新）。"""
import io
import re

p = 'tools/resources-data.py'
s = io.open(p, encoding='utf-8').read()
n_checked = s.count('"checked": "2026-10-01"')
s = s.replace('"checked": "2026-10-01"', '"checked": "2026-10-02"')
print(f'checked 刷新 {n_checked} 处（预期 36）')

# gh 字段刷新（逐条精确替换，带断言）
gh_updates = [
    ('tesla-vehicle-command', '"gh": {"stars": 705, "pushed": "2026-09"}', '"gh": {"stars": 706, "pushed": "2026-09"}'),
    ('teslamate', '"gh": {"stars": 9061, "pushed": "2026-09"}', '"gh": {"stars": 9065, "pushed": "2026-10"}'),
    ('grok-1', '"gh": {"stars": 52239, "pushed": "2024-08"}', '"gh": {"stars": 52233, "pushed": "2024-08"}'),
    ('r-spacex-api', '"gh": {"stars": 10912, "pushed": "2024-08"}', '"gh": {"stars": 10913, "pushed": "2024-08"}'),
]
for rid, old, new in gh_updates:
    i = s.find(f'"id": "{rid}"')
    assert i > 0, rid
    j = s.find('"gh":', i)
    k = s.find('}', j)
    cur = s[j:k + 1]
    assert cur == old, f'{rid}: {cur}'
    s = s[:j] + new + s[k + 1:]
    print(f'{rid}: {old} -> {new}')

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('saved')
