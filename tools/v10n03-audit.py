# -*- coding: utf-8 -*-
"""V10-15 N03：口径审计——snowflake 全量对表 + 日期口径注完备性走查。"""
import io
import json
import os
import re
from datetime import datetime, timezone

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

inv = json.load(io.open('qa/v10-15/round-02/inventory.json', encoding='utf-8'))
s = io.open('x-posts.html', encoding='utf-8').read()

rows = []
for t in inv['tweets']:
    if not t['mirror_id']:
        rows.append({'id': t['id'], 'verdict': 'no-id（卡内无 status id，无法机核对表——卡内日期口径以立条时多源核实为准）'})
        continue
    # snowflake 解码
    ts_ms = (int(t['mirror_id']) >> 22) + 1288834974657
    dt = datetime.fromtimestamp(ts_ms / 1000, tz=timezone.utc)
    utc_date = dt.strftime('%Y-%m-%d')
    # 卡内日期（tweet-date span）
    m = re.search(r'id="' + re.escape(t['id']) + r'"[\s\S]{0,600}?tweet-date[^>]*>(\d{4}\.\d{2}\.\d{2})<', s)
    card_date = m.group(1).replace('.', '-') if m else None
    # 卡内是否注明 UTC 口径
    note_m = re.search(r'id="' + re.escape(t['id']) + r'"[\s\S]{0,2500}?tweet-note[^>]*>(.*?)</p>', s, re.S)
    note = note_m.group(1) if note_m else ''
    has_utc_note = bool(re.search(r'UTC|utc', note))
    ok = (card_date == utc_date)
    rows.append({'id': t['id'], 'mirror_id': t['mirror_id'], 'snowflake_utc': utc_date,
                 'card_date': card_date, 'match': ok, 'utc_note': has_utc_note,
                 'verdict': 'match' if ok else ('match+note-missing' if ok else 'DATE-MISMATCH')})

mm = [r for r in rows if r['verdict'] == 'DATE-MISMATCH']
nm = [r for r in rows if r.get('verdict') == 'match+note-missing']
okc = [r for r in rows if r.get('verdict') == 'match']
noid = [r for r in rows if r['verdict'].startswith('no-id')]
print(f'X 帖 31：snowflake 对表 match {len(okc)} / 注记缺失 {len(nm)} / 日期不符 {len(mm)} / 无 id {len(noid)}')
for r in mm:
    print('  MISMATCH', r['id'], 'snowflake', r['snowflake_utc'], 'card', r['card_date'])
for r in nm:
    print('  note-missing', r['id'], r['snowflake_utc'])

with io.open('qa/v10-15/round-03/snowflake-audit.json', 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
print('snowflake-audit.json saved')
