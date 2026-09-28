# -*- coding: utf-8 -*-
"""R02 span 步进修复：12 页 site-version-val 6.6.0 → 6.7.0（上次正则笔误未执行）。"""
import io, re, glob

OLD, NEW = "6.6.0", "6.7.0"
pat = re.compile(r'(site-version-val">)' + re.escape(OLD) + r'<')
n_total = 0
for p in glob.glob("*.html"):
    with io.open(p, encoding="utf-8", newline="") as f:
        h = f.read()
    n = len(pat.findall(h))
    if n:
        h2 = pat.sub(r"\g<1>" + NEW + "<", h)
        with io.open(p, "w", encoding="utf-8", newline="") as f:
            f.write(h2)
        n_total += n
        print("OK span", p, n)
assert n_total == 12, n_total
print("ALL DONE, spans:", n_total)
