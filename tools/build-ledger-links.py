# -*- coding: utf-8 -*-
"""V7-19 R14 账本关联建档生成器：把事件档案/专题反向链接注入言行账本条目。

数据源：tools/events-data.py 各事件的 materials（kind=ledger 指向 primary.html#eXXX）。
注入：对应 ps-row 尾部插入 .ps-linkcard（<!-- PS-LINKCARD --> 标记，幂等可重跑）：
  「关联建档」事件档案链接 + 该事件材料组中的站内专题/文档深链。
无 JS 完整可见，打印保留。

用法：python tools/build-ledger-links.py
"""
import html as H
import importlib.util
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
os.chdir(ROOT)


def load_module(fname, modname):
    spec = importlib.util.spec_from_file_location(modname, os.path.join(TOOLS, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ED = load_module("events-data.py", "events_data")
P = "primary.html"

s = io.open(P, encoding="utf-8").read()

# ---------- 反向映射：账本条目 id -> [(event_id, event_title, extra_links)] ----------
links_by_entry = {}
for ev in ED.EVENTS:
    entry_ids = []
    extras = []
    for m in ev.get("materials", []):
        href = m.get("href") or ""
        if m.get("kind") == "ledger" and href.startswith("primary.html#"):
            entry_ids.append(href.split("#", 1)[1])
        elif m.get("kind") in ("feature", "document") and href and not href.startswith("#"):
            label = m["label"]["zh"]
            extras.append((href, label))
    for eid in entry_ids:
        links_by_entry.setdefault(eid, {"event": None, "extras": []})
        links_by_entry[eid]["event"] = ev["id"]
        for href, label in extras:
            if (href, label) not in links_by_entry[eid]["extras"]:
                links_by_entry[eid]["extras"].append((href, label))

# ---------- 注入 ----------
MARK = '<!-- PS-LINKCARD -->'
CARD_RE = re.compile(r'[ \t]*<!-- PS-LINKCARD -->\n[ \t]*<div class="ps-linkcard">.*?</div>\n', re.S)

injected = 0
for entry_id, info in sorted(links_by_entry.items()):
    card_html = MARK + '\n          <div class="ps-linkcard"><b data-en="Filed as">关联建档</b>' \
        '<a href="events.html#{eid}" data-en="Event file">事件档案 {eid}</a>{extras}</div>\n        '
    extras_html = ''.join(
        '<a href="%s" data-en="%s">%s</a>' % (href, H.escape(en, quote=True), H.escape(zh))
        for href, (zh, en) in []
    )
    # extras 存的是 (href, zh)；双语标签从 events-data 原文取，这里改存三元的写法见下
    # 重新构建 extras（带双语）：
    extras_html = ''
    for ev in ED.EVENTS:
        entry_hit = any(
            (m.get("href") or "") == "primary.html#" + entry_id and m.get("kind") == "ledger"
            for m in ev.get("materials", [])
        )
        if not entry_hit:
            continue
        for m in ev.get("materials", []):
            href = m.get("href") or ""
            if m.get("kind") in ("feature", "document") and href and not href.startswith("#") \
                    and href != "events.html#" + ev["id"]:
                zh = H.escape(m["label"]["zh"])
                en = H.escape(m["label"]["en"], quote=True)
                if 'href="%s"' % href not in extras_html:
                    extras_html += '<a href="%s" data-en="%s">%s</a>' % (href, en, zh)

    card = (MARK + '\n          <div class="ps-linkcard"><b data-en="Filed as">关联建档</b>'
            '<a href="events.html#' + info["event"] + '" data-en="Event file">事件档案 '
            + info["event"] + '</a>' + extras_html + '</div>\n        ')

    # 定位条目 </li>
    id_anchor = 'id="%s"' % entry_id
    i = s.find(id_anchor)
    if i < 0:
        print("!! 条目未找到:", entry_id)
        continue
    j = s.find("</li>", i)
    seg = s[i:j]
    # 幂等：先移除旧卡
    seg_new = CARD_RE.sub("", seg)
    if MARK not in seg_new:
        injected += 1
    seg_new = seg_new + card
    s = s[:i] + seg_new + s[j:]

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("✓ primary.html 关联建档卡注入 %d 处（覆盖 %d 条在册条目）" % (injected, len(links_by_entry)))
