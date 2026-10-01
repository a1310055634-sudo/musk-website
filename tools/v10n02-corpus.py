# -*- coding: utf-8 -*-
"""V10-15 N02 Step2b：镜像 interview 语料扩展——按站内访谈卡日期匹配场次，
拉 /agents/transcript/{id} 建扩语料（扩后重跑 Step2 提升 indexOf 覆盖）。"""
import glob
import io
import json
import os
import re
import time
import urllib.request
import urllib.error

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0.0.0'

inv = json.load(io.open('qa/v10-15/round-02/inventory.json', encoding='utf-8'))
alliv = json.load(io.open('qa/v9-20/round-04/interviews-all.json', encoding='utf-8'))

# 站内卡日期（id iYYYY-MM-DD…）→ 候选场次（日期±3 天）
need = set()
for it in inv['interviews']:
    m = re.match(r'i(\d{4})-(\d{2})-(\d{2})', it['id'])
    if not m:
        continue
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    for rec in alliv:
        dm = re.match(r'(\d{4})-(\d{2})-(\d{2})', rec.get('date') or '')
        if not dm:
            continue
        dy, dmo, dd = int(dm.group(1)), int(dm.group(2)), int(dm.group(3))
        if (y, mo, d) == (dy, dmo, dd):
            need.add(rec['id'])
print(f'日期精确匹配场次 {len(need)}')

# 已在本地存档的场次 id（按文件名含 id 粗判）已存 = 跳过拉取
have = set()
for fp in glob.glob('qa/v9-20/round-*/sources/*'):
    for sid in need:
        if sid in fp:
            have.add(sid)
todo = sorted(need - have)
print(f'本地已有 {len(have)}，待拉 {len(todo)}')

ok = fail = 0
for sid in todo:
    try:
        req = urllib.request.Request(f'https://elonmuskarchive.org/agents/transcript/{sid}',
                                     headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            body = r.read().decode('utf-8', 'ignore')
        try:
            d = json.loads(body)
            text = d.get('text') or d.get('transcript') or ''
        except Exception:
            text = ''
        safe = re.sub(r'[^a-z0-9-]', '_', sid)
        io.open(f'qa/v10-15/round-02/sources/{safe}.txt', 'w', encoding='utf-8', newline='\n').write(
            f'[mirror transcript {sid}]\n{text}')
        ok += 1
    except Exception as e:
        fail += 1
        print('  FAIL', sid, str(e)[:60])
    time.sleep(0.6)
print(f'拉取完成 ok={ok} fail={fail}')
