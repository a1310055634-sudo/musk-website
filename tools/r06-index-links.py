# -*- coding: utf-8 -*-
"""R6 一次性：index.html #events 五个事件行的 event-links 追加「事件详情」深链。

锚点用 ASCII href（primary.html#e*），中文插入内容在脚本内声明（UTF-8，避开 bash GBK 坑）。
幂等：已含 events.html#e* 链接的行会跳过。
"""
import io

P = "index.html"
s = io.open(P, encoding="utf-8").read()

IDS = ["e2002-10-03", "e2008-12-24", "e2018-08-07", "e2022-10-28", "e2024-10-13"]
INS = '<span class="sep">·</span><a href="events.html#{eid}" data-en="Event file">事件详情</a>'

changed = 0
for eid in IDS:
    anchor = f'href="primary.html#{eid}"'
    i = s.find(anchor)
    if i < 0:
        print(f"✗ 未找到锚点 {anchor}")
        continue
    j = s.find("</a>", i)
    if j < 0:
        print(f"✗ {eid}: 找不到收尾 </a>")
        continue
    j += len("</a>")
    if f'events.html#{eid}' in s[i:j + 200]:
        print(f"· {eid}: 已有事件详情链接，跳过")
        continue
    s = s[:j] + INS.format(eid=eid) + s[j:]
    changed += 1

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print(f"✓ 追加 {changed}/5 个事件详情深链")
