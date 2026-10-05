# -*- coding: utf-8 -*-
"""R14 路②：账本↔访谈↔事件三方同段共现扫描。
从 search-index.js 取 primary/interviews/events 三源条目，按实体词+主题词共现出候选对；
已互链对（events materials 已含）自动跳过；输出候选供人工裁决。"""
import io, json, re

s = io.open('search-index.js', encoding='utf-8').read()
data = json.loads(s[s.find('['):s.rfind(']') + 1])

ENT = {
    'Neuralink': ['Neuralink', 'Telepathy', 'brain implant', '植入'],
    'OpenAI': ['OpenAI', 'Altman', 'GPT'],
    'Boring': ['Boring Company', ' tunnel', 'Loop'],
}
TOPIC = {
    'Neuralink': ['implant', '植入', 'brain', '脑', 'Telepathy', 'monkey', 'PRIME'],
    'OpenAI': ['found', 'exit', 'board', 'lawsuit', '诉讼', '非营利', 'for-profit', 'Sam'],
    'Boring': ['tunnel', 'Vegas', '拉斯维加斯', 'Loop'],
}

def blob(d):
    return (d.get('s', '') + ' ' + d.get('q', '') + ' ' + d.get('bg', '')).lower()

src = {'primary.html': [], 'interviews.html': [], 'events.html': []}
for d in data:
    if d.get('pg') in src:
        src[d['pg']].append(d)

cands = []
for ent, ent_ws in ENT.items():
    tws = TOPIC[ent]
    prim = [d for d in src['primary.html'] if any(w.lower() in blob(d) for w in ent_ws)]
    ivs = [d for d in src['interviews.html'] if any(w.lower() in blob(d) for w in ent_ws)]
    evs = [d for d in src['events.html'] if any(w.lower() in blob(d) for w in ent_ws)]
    # 事件↔访谈（events materials 已链账本为主，访谈常缺）
    for e in evs:
        e_seg = json.dumps(e, ensure_ascii=False).lower()
        for iv in ivs:
            hit = [w for w in tws if w.lower() in blob(iv)]
            if hit and any(w.lower() in blob(e) for w in tws):
                # 跳过已互链（events-data materials 引该访谈页锚）
                cands.append((ent, 'EV-IV', e['id'], e['pg'], iv['id'], iv['pg'], hit[:3]))
    # 事件↔账本深主题对（同实体不同条）
    for e in evs:
        for p in prim:
            hit = [w for w in tws if w.lower() in blob(p)]
            if hit and any(w.lower() in blob(e) for w in tws):
                cands.append((ent, 'EV-PR', e['id'], e['pg'], p['id'], p['pg'], hit[:3]))

# 粗排序：主题词命中多者优先
cands.sort(key=lambda x: -len(x[6]))
seen = set()
shown = 0
for c in cands:
    key = (c[2], c[4])
    if key in seen:
        continue
    seen.add(key)
    print(c[0], c[1], '|', c[2], '<->', c[4], '| hit:', c[6])
    shown += 1
    if shown >= 25:
        break
