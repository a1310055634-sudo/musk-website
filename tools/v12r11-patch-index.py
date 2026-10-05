# -*- coding: utf-8 -*-
"""R11 patch：build-search-index.py 编年史断言 53→64 + 新增 deep-dive-06 类型段 + counts 断言。"""
import io

p = 'tools/build-search-index.py'
s = io.open(p, encoding='utf-8').read()

# 1) 编年史断言
old = 'assert n_ch == 53, n_ch'
new = 'assert n_ch == 64, n_ch'
assert s.count(old) == 1
s = s.replace(old, new)

# 2) dd06 类型段（插在 chronicle 段断言之后）
anchor = '# ---------- finance.html 财务全景（四节，id 沿用页内 tesla/spacex/x/xai） ----------'
dd06_block = '''# ---------- deep-dive-06.html 深读长文（R11，xAI 三年志） ----------
s = io.open('deep-dive-06.html', encoding='utf-8').read()
_dd_h1 = re.search(r'<h1 data-en="[^"]*">([^<]+)</h1>', s)
_dd_lead = re.search(r'<p class="lr-lead"[^>]*>(.*?)</p>', s, re.S)
assert _dd_h1 and _dd_lead, 'dd06 h1/lead missing'
items.append({
    'id': 'deep-dive-06', 'pg': 'deep-dive-06.html', 't': '深读长文',
    'd': '2026', 's': strip(_dd_h1.group(1)),
    'q': strip(_dd_lead.group(1))[:120], 'zh': '', 'bg': strip(_dd_lead.group(1))[:160],
})

''' + anchor
assert s.count(anchor) == 1
s = s.replace(anchor, dd06_block)

# 3) counts 断言
old_c = "'争议深读': 5, '编年史': 53,"
new_c = "'争议深读': 5, '深读长文': 1, '编年史': 64,"
assert s.count(old_c) == 1
s = s.replace(old_c, new_c)

io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('build-search-index patched: chronicle 64 + dd06 type')
