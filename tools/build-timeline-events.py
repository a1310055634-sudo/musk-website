# -*- coding: utf-8 -*-
"""事件泳道时间轴 · 聚合数据与静态清单生成（V7-19 R9）

用法：python tools/build-timeline-events.py
（站点根目录执行；幂等可重跑。事件或账本变动后重跑一次即可刷新。）

产出：
  timeline-events.js —— window.TIMELINE_V7 = {meta, records}：
      records 是「未被事件档案吸收」的一手材料记录（来自 search-index，与检索页同源）；
      已归入事件档案的记录不再单列（避免同一事件因多份材料伪装成多个事件），
      事件本体数据由 events-data.js 的 window.EVENTS_V7 提供（单一事实来源，不在本文件重复）。
  timeline.html —— TL-V7:BEGIN/END 标记之间的静态「清单模式」HTML（无 JS 可读、打印可见）。

聚合口径：
  search-index 条目 pg#id 与 events-data.py 材料 href 完全匹配 → 该条归入事件（吸收）；
  页面级材料（如深读/专页整页引用、纪实图片）本就不在检索索引中，不参与匹配。
"""
import html as H
import importlib.util
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
os.chdir(ROOT)


def load_module(fname, modname):
    spec = importlib.util.spec_from_file_location(modname, os.path.join(TOOLS, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ED = load_module("events-data.py", "events_data")
VERSION = io.open("VERSION", encoding="utf-8").read().strip()

problems = ED.validate()
if problems:
    for p in problems:
        print("✗", p)
    sys.exit(1)


def esc(s):
    return H.escape(str(s), quote=True)


def date_key(d):
    m = re.match(r"(\d{4})\.?(\d{1,2})?", str(d or ""))
    if not m:
        return None
    y = int(m.group(1))
    mo = int(m.group(2) or 1)
    return y + (mo - 0.5) / 12.0


# ---------------- 读检索索引（与检索页同源） ----------------
s = io.open("search-index.js", encoding="utf-8").read()
i = s.find("[")
j = s.rfind("]")
assert 0 < i < j, "search-index.js 结构异常"
items = json.loads(s[i:j + 1])
by_href = {it["pg"] + "#" + it["id"]: it for it in items}

# ---------------- 聚合：被事件档案吸收的记录 ----------------
absorbed = {}          # href -> event id
absorbed_by_event = {}  # event id -> count
for ev in ED.EVENTS:
    n = 0
    for m in ev["materials"]:
        href = m.get("href") or ""
        if href in by_href:
            absorbed[href] = ev["id"]
            n += 1
    if n:
        absorbed_by_event[ev["id"]] = n

# V7-19 R19 口径修正：events.html 的事件档案索引记录（R15 入检索）不是一手材料记录，
# 不入时间轴记录池——否则同一事件被「档案 + 材料」双重表达（151→160 的漂移即由此来）。
records = [it for it in items if it["pg"] != "events.html" and (it["pg"] + "#" + it["id"]) not in absorbed]

# ---------------- timeline-events.js ----------------
data = {
    "meta": {
        "built": "V7-19 R9",
        "version": VERSION,
        "nEvents": len(ED.EVENTS),
        "nRecords": len(records),
        "nAbsorbed": len(absorbed),
        "absorbedByEvent": absorbed_by_event,
        "source": "tools/events-data.py + search-index.js",
    },
    "records": records,
}
js = ("// 事件泳道时间轴数据（V7-19 R9）· 由 tools/build-timeline-events.py 自动生成，勿手改\n"
      "// records = 未被事件档案吸收的一手材料记录（search-index 同源）；事件本体见 events-data.js 的 EVENTS_V7\n"
      "// 已归入事件档案的记录不在本文件单列——泳道图与清单不再把同一事件画成多个点\n"
      "window.TIMELINE_V7 = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")
io.open("timeline-events.js", "w", encoding="utf-8", newline="\n").write(js)

# ---------------- 静态清单（注入 timeline.html，无 JS 可读、打印可见） ----------------
PREC = ED.PRECISION_LABELS
ETYPE = ED.ETYPE_LABELS

rows = []
for ev in ED.EVENTS:
    prec = PREC[ev["precision"]]
    et = ETYPE[ev["etype"]]
    n_mat = len(ev["materials"])
    n_abs = absorbed_by_event.get(ev["id"], 0)
    co = " · ".join(ev["companies"])
    title_en = esc(ev["title"]["en"])
    abs_note = f'（{n_abs} 条已归位）' if n_abs else ''
    rows.append((date_key(ev["date"]), 0, ev["id"], f'''          <li class="gxl-row gxl-ev" data-ev="{esc(ev["id"])}">
            <span class="gxl-date">{esc(ev["date"])}</span>
            <span class="ev-precision" data-en="{esc(prec["en"])}">{esc(prec["zh"])}</span>
            <span class="ev-etype ev-etype--{ev["etype"]}" data-en="{esc(et["en"])}">{esc(et["zh"])}</span>
            <span class="gxl-main"><a href="events.html#{esc(ev["id"])}" data-en="{title_en}">{esc(ev["title"]["zh"])}</a>
              <span class="gxl-co">{esc(co)}</span></span>
            <span class="gxl-n" data-en="{n_mat} records on file">{n_mat} 份材料在档{abs_note}</span>
          </li>'''))

for it in records:
    k = date_key(it.get("d"))
    if k is None:
        continue
    q = re.sub(r"\s+", " ", it.get("q") or "").strip()
    if len(q) > 90:
        q = q[:90] + "…"
    q_html = f'\n              <span class="gxl-q">{esc(q)}</span>' if q else ""
    rows.append((k, 1, it["pg"] + "#" + it["id"], f'''          <li class="gxl-row" data-key="{esc(it["pg"])}#{esc(it["id"])}">
            <span class="gxl-date">{esc(it["d"])}</span>
            <span class="gxl-kind">{esc(it.get("t") or "")}</span>
            <span class="gxl-main"><a href="{esc(it["pg"])}#{esc(it["id"])}">{esc(it.get("s") or "")}</a>{q_html}
            </span>
          </li>'''))

rows.sort(key=lambda r: (r[0], r[1]))

list_items = []
cur_year = None
for k, _, rid, html in rows:
    y = int(k)
    if y != cur_year:
        cur_year = y
        list_items.append(f'          <li class="gxl-year" data-year="{y}">{y}</li>')
    list_items.append(html)

N_EV, N_REC, N_ABS = len(ED.EVENTS), len(records), len(absorbed)
list_block = (
    '<!-- TL-V7:BEGIN (generated by tools/build-timeline-events.py) -->\n'
    f'        <p class="gx-listmeta" id="gx-listmeta" data-en="{N_EV} filed events · {N_REC} first-hand records · {N_ABS} records folded into event files">'
    f'{N_EV} 个已建档事件 · {N_REC} 条一手记录 · {N_ABS} 条已归入事件档案（不重复画出）</p>\n'
    '        <ol class="gx-list" id="gx-list" aria-label="事件与一手材料清单（按时间排序）">\n'
    + "\n".join(list_items) + "\n"
    + '        </ol>\n'
    + '<!-- TL-V7:END -->')

# ---------------- 注入 timeline.html（幂等） ----------------
p = "timeline.html"
s = io.open(p, encoding="utf-8").read()
BEGIN, END = "<!-- TL-V7:BEGIN", "<!-- TL-V7:END -->"
if BEGIN in s:
    s = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), list_block, s, flags=re.S)
else:
    anchor = '<div class="gx-detail" id="gx-detail" hidden></div>'
    assert s.count(anchor) == 1, "timeline.html 缺清单注入锚点"
    s = s.replace(anchor, anchor + "\n" + list_block, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)

n_ev_mat = sum(len(e["materials"]) for e in ED.EVENTS)
print(f"✓ timeline-events.js（{N_REC} 条独立记录 · 吸收 {N_ABS} 条）+ timeline.html 静态清单注入完毕（事件 {N_EV} · 材料 {n_ev_mat} · v{VERSION}）")
