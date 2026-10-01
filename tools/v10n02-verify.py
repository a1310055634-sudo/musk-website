# -*- coding: utf-8 -*-
"""V10-15 N02 Step2：引语机核。

语料 A（本地零网络）：qa/v9-20/round-*/sources/ 下 transcript 存档（txt/json）
  —— 访谈 42 块与账本 106 块逐块做归一 indexOf（跨语料全检索）。
语料 B（镜像 API）：X 帖 22 条有 status id 的卡逐条拉 transcript 做归一全等 diff。
输出 qa/v10-15/round-02/verify-results.json + 汇总打印（三类判定：verified /
unmatched / no-anchor，unmatched 不冒充失败——列明待人工口径）。
"""
import glob
import io
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import importlib.util as _iu
_spec = _iu.spec_from_file_location('v10n02_extract', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v10n02-extract.py'))
_mod = _iu.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
norm = _mod.norm

inv = json.load(io.open('qa/v10-15/round-02/inventory.json', encoding='utf-8'))

# ---------- 语料 A：本地 transcript 存档 ----------
corpus_parts = []
files = (glob.glob('qa/v9-20/round-*/sources/*.txt')
         + glob.glob('qa/v10-15/round-*/sources/*.txt')
         + glob.glob('qa/v9-20/round-*/sources/*.md')
         + glob.glob('qa/v9-20/round-*/sources/joined*.txt'))
for fp in files:
    try:
        corpus_parts.append(io.open(fp, encoding='utf-8', errors='ignore').read())
    except Exception:
        pass
# transcript JSON（round-02/03 的 {id: text} 形态）
for fp in glob.glob('qa/v9-20/round-*/sources/*.json'):
    try:
        d = json.load(io.open(fp, encoding='utf-8'))
        def _walk(o):
            if isinstance(o, str):
                corpus_parts.append(o)
            elif isinstance(o, dict):
                for v in o.values():
                    _walk(v)
            elif isinstance(o, list):
                for v in o:
                    _walk(v)
        _walk(d)
    except Exception:
        pass
CORPUS = norm('\n'.join(corpus_parts))
print(f'本地语料：{len(files)} 文件，归一后 {len(CORPUS):,} 字符')

results = {'interviews': [], 'ledger': [], 'tweets': []}

# ---------- 访谈 42：语料 A indexOf ----------
for it in inv['interviews']:
    segs = [seg.strip() for seg in re.split(r'\s+—\s+|\s+--\s+', it['text']) if len(seg.strip()) > 25]
    segs = segs or [it['text']]
    hits = [seg for seg in segs if norm(seg) and norm(seg) in CORPUS]
    verdict = 'verified' if hits else 'unmatched'
    results['interviews'].append({
        'id': it['id'], 'segs': len(segs), 'hits': len(hits),
        'verdict': verdict, 'miss': [seg[:60] for seg in segs if seg not in hits][:3],
    })

# ---------- 账本 106：语料 A indexOf ----------
for it in inv['ledger']:
    key = norm(it['text'])
    verdict = 'verified' if key and key in CORPUS else 'unmatched'
    results['ledger'].append({'id': it['id'], 'verdict': verdict})

# ---------- X 帖 22：镜像 API diff ----------
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0.0.0'
with_id = [t for t in inv['tweets'] if t['mirror_id']]
no_id = [t for t in inv['tweets'] if not t['mirror_id']]
for k, t in enumerate(with_id):
    mid = t['mirror_id']
    body = None
    cands = [f'https://elonmuskarchive.org/agents/transcript/x-{mid}',
             f'https://elonmuskarchive.org/agents/transcript/{mid}'] * 2  # 两轮重试
    for cand in cands:
        try:
            req = urllib.request.Request(cand, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=15) as r:
                body = r.read().decode('utf-8', 'ignore')
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                body = None
                break
            body = None
        except Exception:
            body = None
        time.sleep(0.8)
    if body is None:
        results['tweets'].append({'id': t['id'], 'mirror_id': mid, 'verdict': 'fetch-failed'})
    else:
        try:
            d = json.loads(body)
            text = d.get('text') or d.get('transcript') or str(d)
        except Exception:
            text = body
        mn = norm(text)
        # 合并卡口径：站内卡文本可含两连发（R08 建卡惯例），按句切段逐段 indexOf
        segs = [seg for seg in re.split(r'[.!?]+', t['text']) if len(norm(seg)) >= 8]
        hit = sum(1 for seg in segs if norm(seg) in mn)
        results['tweets'].append({
            'id': t['id'], 'mirror_id': mid,
            'verdict': ('verified' if (segs and hit == len(segs))
                        else ('merged-card' if hit else 'no-seg-hit')),
            'segs': len(segs), 'hits': hit,
            'mirror_len': len(mn),
        })
    time.sleep(0.6)
    if (k + 1) % 10 == 0:
        print(f'  X 帖 {k+1}/{len(with_id)}')

for t in no_id:
    results['tweets'].append({'id': t['id'], 'verdict': 'no-anchor（卡内无镜像 status id——早期卡 id 记录形态不同，人工口径）'})

# ---------- 汇总 ----------
def summ(lst, name):
    c = {}
    for x in lst:
        c[x['verdict']] = c.get(x['verdict'], 0) + 1
    print(f'{name}: {c}')
    return c

si = summ(results['interviews'], '访谈 42 块')
sl = summ(results['ledger'], '账本 106 块')
st = summ(results['tweets'], 'X 帖 31 卡')
with io.open('qa/v10-15/round-02/verify-results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=1)
print('verify-results.json saved')
