# -*- coding: utf-8 -*-
"""V8 R08: add two cross-links in platform-x.html sv-links (px-0414, px-0723)."""
import io

P = 'platform-x.html'
s = io.open(P, encoding='utf-8', newline='').read()

old1 = '<a href="documents.html#d2022-07-26" data-en="Proxy: the April 13 offer letter, full text">文档：4.13 要约信全文与全日程</a></p>'
new1 = '<a href="documents.html#d2022-07-26" data-en="Proxy: the April 13 offer letter, full text">文档：4.13 要约信全文与全日程</a><a href="x-posts.html#p2022-04-14" data-en="The three-word offer post">帖史：三个字的要约帖</a></p>'
assert s.count(old1) == 1, 'px-0414 anchor'
s = s.replace(old1, new1)

old2 = '<div class="sv-node-head"><span class="sv-node-date">2023.07.23</span><span class="sv-node-tag sv-tag-s2" data-en="Stage 2 · Rebrand">阶段二 · 更名</span></div>'
assert s.count(old2) == 1, 'px-0723 head'
# add link inside px-0723 sv-links (the one right after this head)
i = s.find(old2)
j = s.find('sv-links', i)
k = s.find('</p>', j)
seg = s[j:k+5]
old_link = '<a href="company-files.html#file-x" data-en="Company file: X">公司档案 X</a></p>'
assert seg.count(old_link) == 1, 'px-0723 sv-links shape'
seg_new = seg.replace(old_link, '<a href="company-files.html#file-x" data-en="Company file: X">公司档案 X</a><a href="x-posts.html#p2023-07-23" data-en="The bid-adieu post, verbatim">帖史：告别宣言原帖</a></p>')
s = s[:j] + seg_new + s[k:]

io.open(P, 'w', encoding='utf-8', newline='').write(s)
print('OK: 2 cross-links added')
