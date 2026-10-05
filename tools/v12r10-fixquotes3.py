# -*- coding: utf-8 -*-
"""R10 修复 IV：仅 R10 新块（1018 行 0-based 之后）扫描全部字符串行，
把值体内成对裸双引号换成单引号；不动历史区。修后 py_compile 校验。"""
import io, re, py_compile

p = 'tools/events-data.py'
lines = io.open(p, encoding='utf-8').read().split('\n')
fixed = 0
for i in range(1018, len(lines)):
    ln = lines[i]
    # 找 "en"/"zh"/label 文本值：匹配 "xxx": "值" 形式，值内若再有双引号则全换单引号
    m = re.match(r'^(\s*(?:"(?:zh|en|label|note)"|"label": \{"zh"): .*?)(.*)$', ln)
    # 更通用：按行处理——定位每对 "..." 字面量，若某对字面量内部还含双引号说明截断
    parts = ln.split('"')
    if len(parts) >= 5:  # 至少 2 个以上字符串段
        # 奇偶校验：正常行 parts 数为偶数（每串 2 个引号）；若奇数→有裸引号
        pass
    # 精确法：字符串值行形如  "key": "value",  —— 提取 value 段
    m2 = re.match(r'^(\s*(?:"[a-z]+": ?)+(?:\{"[a-z]+": ?)*)"(.+)"(\s*[},]*\s*)$', ln)
    if m2 and ('"' in m2.group(2)):
        newv = m2.group(2).replace('"', "'")
        lines[i] = m2.group(1) + newv + '"' + m2.group(3)
        print('fixed', i + 1, ':', m2.group(2)[:60])
        fixed += 1
io.open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
print('fixed:', fixed)
try:
    py_compile.compile(p, doraise=True)
    print('syntax OK')
except py_compile.PyCompileError as e:
    import re as _re
    ln = _re.findall(r'line (\d+)', str(e))
    print('STILL BROKEN at line', ln)
    n = int(ln[-1])
    print(repr(lines[n - 1][:160]))
    raise SystemExit(1)
