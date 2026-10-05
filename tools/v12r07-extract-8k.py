# -*- coding: utf-8 -*-
"""R07 采料 V：SpaceX senior notes launch 8-K 正文段。"""
import io, re, html

raw = io.open('qa/v12/round-07/sources/spcx-launch-8k.html', encoding='utf-8', errors='ignore').read()
t = re.sub(r'<[^>]+>', ' ', raw)
t = html.unescape(t)
t = re.sub(r'\s+', ' ', t)
i = t.find('Date of Report')
print(t[i:i + 2600])
