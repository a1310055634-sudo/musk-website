# -*- coding: utf-8 -*-
"""R07 采料 VI：Dorsey 正文完整版（长串抽取）。"""
import io, re

raw = io.open('qa/v12/round-07/sources/musk-texts-dorsey-protocol-2022.html',
              encoding='utf-8').read()
pat = re.compile(r'"((?:[^"\\]|\\.){400,2000})"')
for t in pat.findall(raw):
    u = t.encode('latin-1', errors='ignore').decode('unicode_escape', errors='ignore')
    if 'protocol' in u or 'Dorsey' in u or 'Signal' in u:
        print(repr(u))
        print()
