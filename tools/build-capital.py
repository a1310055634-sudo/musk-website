# -*- coding: utf-8 -*-
"""资本流向可视化生成器（V7-19 R10）。

用法: python tools/build-capital.py
- 数据源: tools/capital-data.py（5 来源节点 + 7 公司节点 · 18 笔流向，先过结构自检）；
- 产出 1: capital-evolution.html 注入/替换 <!-- V7-R10-CAPITAL:BEGIN/END --> 区块
  （section#flow：SVG 流向图 + 图例 + 筛选芯片 + 交互详情面板 + 分组清单 + 非流向口径声明）；
  首次运行时会移除旧的静态 #ce-flow 装饰图（其内容已并入新区块）；
- 产出 2: capital-data.js（window.CAPITAL_V7，供详情面板交互与 R15 检索复用）；
- 幂等: 可重复运行，输出一致。

设计约定：
- SVG 全静态绘制（无 JS 也完整可读）：线宽按金额对数标度（示意，图例声明），
  金额未入册的流向画最细线并明确标注——装饰不伪装精确统计；
- 箭头方向 = 资金方向（from → to），退出流向个人资本（「退出即入场」闭环可见）；
- 估值 / 市值 / 减记不是资金流动，一律不入图（NON_FLOW_NOTE 显式声明）；
- 交互（点击/键盘查看详情、分组筛选）由 app.js 读取 capital-data.js 增强；
- ≤760px 隐 SVG，分组清单成为主形态（清单桌面同样可见，不是手机专属降级）。
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


CAP = load_module("capital-data.py", "capital_data")

problems = CAP.validate()
if problems:
    for p in problems:
        print("✗", p)
    sys.exit(1)


def esc(s):
    return H.escape(str(s), quote=True)


FLOWS = {f["id"]: f for f in CAP.FLOWS}
SRC = {n["id"]: n for n in CAP.SRC_NODES}
CO = {n["id"]: n for n in CAP.CO_NODES}

# ---- SVG 布局（viewBox 0 0 980 840）----
SRC_X, SRC_W = 24, 176          # 左列节点
CO_X, CO_W = 792, 170           # 右列节点
SRC_GEOM = {                    # id → (cy, h)
    "musk": (100, 64), "vc": (240, 56), "public": (340, 40),
    "gov": (452, 52), "acq": (648, 68),
}
CO_GEOM = {
    "zip2": (96, 48), "paypal": (204, 48), "spacex": (316, 56),
    "tesla": (448, 64), "solarcity": (566, 48), "x": (686, 56), "xai": (786, 60),
}
# 每个节点边缘的插槽顺序（上→下）：src 节点全在右缘；co 节点全在左缘
SLOTS = {
    "musk": ["zip2-exit", "pp-exit", "spacex-found", "tesla-found", "sc-found"],
    "vc": ["tesla-xmas", "spacex-gf", "xai-b", "xai-c", "xai-e"],
    "public": ["tesla-ipo"],
    "gov": ["spacex-nasa", "tesla-doe"],
    "acq": ["zip2-acq", "pp-acq", "sc-acq", "tw-acq", "xai-x"],
    "zip2": ["zip2-acq", "zip2-exit"],
    "paypal": ["pp-acq", "pp-exit"],
    "spacex": ["spacex-found", "spacex-gf", "spacex-nasa"],
    "tesla": ["tesla-found", "tesla-xmas", "tesla-ipo", "tesla-doe"],
    "solarcity": ["sc-found", "sc-acq"],
    "x": ["tw-acq", "xai-x"],
    "xai": ["xai-b", "xai-c", "xai-e"],
}
# 流向在其节点插槽序列中的序号（用于标签双列错位，避免逐行贴挤）
SLOT_INDEX = {}
for _nid, _order in SLOTS.items():
    for _i, _fid in enumerate(_order):
        SLOT_INDEX[_fid] = _i
PAD = 10

# 每条流向的端点坐标
ENDS = {}
for nid, order in SLOTS.items():
    if nid in SRC_GEOM:
        cy, h = SRC_GEOM[nid]
        x = SRC_X + SRC_W
    else:
        cy, h = CO_GEOM[nid]
        x = CO_X
    y0, y1 = cy - h / 2 + PAD, cy + h / 2 - PAD
    n = len(order)
    for i, fid in enumerate(order):
        ENDS.setdefault(fid, {})["x1" if nid in SRC_GEOM else "x2"] = x
        ENDS[fid]["y1" if nid in SRC_GEOM else "y2"] = y0 + (i + 0.5) * (y1 - y0) / n

# 来源节点类别色（节点左侧色条；与该节点主流出/流入组色一致）
SRC_BAR = {"musk": "var(--accent)", "vc": "var(--navy)", "public": "#4a7ba6",
           "gov": "#8a6d1f", "acq": "#55524c"}


def ribbon_path(x1, y1, x2, y2):
    c1 = x1 + (x2 - x1) * 0.42
    c2 = x2 - (x2 - x1) * 0.42
    return f"M{x1:.0f},{y1:.1f} C{c1:.0f},{y1:.1f} {c2:.0f},{y2:.1f} {x2:.0f},{y2:.1f}"


def render_svg():
    markers = "".join(
        f'<marker id="cap-arrow-{gid}" viewBox="0 0 10 8" refX="8.6" refY="4" '
        f'markerWidth="11" markerHeight="9" orient="auto" markerUnits="userSpaceOnUse">'
        f'<path d="M0,0 L10,4 L0,8 z" fill="{g["color"]}"></marker></marker>'
        for gid, g in CAP.GROUPS.items()
    )
    flows = []
    for f in CAP.FLOWS:
        fid = f["id"]
        g = CAP.GROUPS[f["group"]]
        x1, y1 = ENDS[fid]["x1"], ENDS[fid]["y1"]
        x2, y2 = ENDS[fid]["x2"], ENDS[fid]["y2"]
        d = ribbon_path(x1, y1, x2, y2)
        w = CAP.width_for(f["amount_usd"])
        no_amount = w is None
        vw = w if w else 1.4
        dash = ' stroke-dasharray="3 3"' if no_amount else ""
        # 详情摘要（aria 与 title 用）
        a = f["amount"]
        tip = f"{a['zh']} · {f['date']}（{CAP.PRECISION_LABELS[f['precision']]['zh']}）· 点击查看口径与出处"
        tip_en = f"{a['en']} · {f['date']} ({CAP.PRECISION_LABELS[f['precision']]['en']}) — select for caliber & sources"
        hit = (f'<path class="cap-hit" d="{d}" stroke-width="{max(vw + 12, 20):.0f}" fill="none"></path>')
        vis = (f'<path class="cap-ribbon" d="{d}" stroke="{g["color"]}" stroke-width="{vw}"'
               f'{dash} fill="none" opacity="0.42" marker-end="url(#cap-arrow-{f["group"]})"></path>')
        # 末端标签（金额 · 年份；收购笔另在线起点标注实际出资方）。
        # 标签按插槽序号奇偶双列错位（x2-8 / x2-150），避免密集插槽逐行贴挤。
        lab_col = 8 if SLOT_INDEX[fid] % 2 == 0 else 150
        lab_x, lab_y = x2 - lab_col, y2 - max(vw / 2, 2) - 6
        fl = CAP.flow_label(f)
        flows.append(
            f'<g class="cap-flow{" cap-flow--noamt" if no_amount else ""}" data-cap-flow="{fid}" '
            f'role="button" tabindex="0" aria-label="{esc(tip)}" data-en-aria="{esc(tip_en)}">'
            f'{hit}{vis}'
            f'<text class="cap-elabel" x="{lab_x:.0f}" y="{lab_y:.1f}" text-anchor="end" '
            f'data-en="{esc(fl["en"])}">{esc(fl["zh"])}</text>'
            + (f'<text class="cap-elabel" x="{x1 + (6 if SLOT_INDEX[fid] % 2 == 0 else 56):.0f}" '
               f'y="{y1 - max(vw / 2, 2) - 6:.1f}" text-anchor="start" '
               f'data-en="{esc(f["from_note"]["en"])}">{esc(f["from_note"]["zh"])}</text>' if f.get("from_note") else "")
            + f'<title>{esc(tip)}</title></g>'
        )
    nodes = []
    for nid, n in SRC.items():
        cy, h = SRC_GEOM[nid]
        label, sub = n["label"], n["sub"]
        nlab = f"{label['zh']}（{sub['zh']}）· 查看相关流向"
        nlab_en = f"{label['en']} ({sub['en']}) — view its flows"
        nodes.append(
            f'<g class="cap-node" data-cap-node="{nid}" role="button" tabindex="0" '
            f'aria-label="{esc(nlab)}" data-en-aria="{esc(nlab_en)}">'
            f'<rect x="{SRC_X}" y="{cy - h/2:.0f}" width="{SRC_W}" height="{h}" rx="6" class="cap-node-bg"></rect>'
            f'<rect x="{SRC_X}" y="{cy - h/2:.0f}" width="5" height="{h}" rx="2.5" fill="{SRC_BAR[nid]}"></rect>'
            f'<text class="cap-nlabel" x="{SRC_X + 16}" y="{cy - 3:.0f}" data-en="{esc(label["en"])}">{esc(label["zh"])}</text>'
            f'<text class="cap-nsub" x="{SRC_X + 16}" y="{cy + 14:.0f}" data-en="{esc(sub["en"])}">{esc(sub["zh"])}</text></g>'
        )
    for nid, n in CO.items():
        cy, h = CO_GEOM[nid]
        label = n["label"]
        nlab = f"{label['zh']} · 查看相关流向与档案"
        nlab_en = f"{label['en']} — view its flows and file"
        nodes.append(
            f'<g class="cap-node" data-cap-node="{nid}" role="button" tabindex="0" '
            f'aria-label="{esc(nlab)}" data-en-aria="{esc(nlab_en)}">'
            f'<rect x="{CO_X}" y="{cy - h/2:.0f}" width="{CO_W}" height="{h}" rx="6" class="cap-node-bg"></rect>'
            f'<rect x="{CO_X}" y="{cy - h/2:.0f}" width="{CO_W}" height="5" rx="2.5" fill="var({n["color_var"]})" class="cap-node-bar"></rect>'
            f'<text class="cap-nlabel" x="{CO_X + CO_W/2:.0f}" y="{cy + 6:.0f}" text-anchor="middle" data-en="{esc(label["en"])}">{esc(label["zh"])}</text></g>'
        )
    title = ('<title>资本流向图：个人资本、风险与产业资本、公开市场、政府与收购方，'
             '1999–2026 年间 18 笔资金流动；退出流向个人资本形成闭环</title>')
    return (
        '<div class="cap-graphwrap">'
        '<svg class="cap-graph" viewBox="0 0 980 840" role="group" '
        'aria-label="资本流向图：左列五个资金来源，右列七家公司，18 条带箭头与金额标注的流向线；'
        '文字清单见图下方，手机端以清单为主。">'
        + title + '<defs>' + markers + '</defs>' + "".join(flows) + "".join(nodes) +
        '</svg></div>'
    )


def render_legend():
    return (
        '<div class="cap-legend" data-en="Line width = log-scaled amount (indicative; exact figures are printed). '
        'Arrow = direction of money (exits flow back to personal capital). Thinnest dashed = amount not on file. '
        'Line color = nature of the money (below); company top bars = company colors (names are authoritative).">'
        '<span class="cap-lg"><span class="cap-lg-line cap-lg-line--w1"></span>细线 ≈ 数百万级</span>'
        '<span class="cap-lg"><span class="cap-lg-line cap-lg-line--w2"></span>粗线 ≈ 数百亿级</span>'
        '<span class="cap-lg">线宽按<b>金额对数</b>标度（示意）——精确数字一律以标注与详情为准</span>'
        '<span class="cap-lg"><span class="cap-lg-line cap-lg-line--dash"></span>最细虚线 = 金额未入册（不编造）</span>'
        '<span class="cap-lg"><svg width="30" height="10" aria-hidden="true"><line x1="0" y1="5" x2="20" y2="5" stroke="#55524c" stroke-width="2"/><path d="M20,1.5 L28,5 L20,8.5 z" fill="#55524c"/></svg>箭头 = 资金方向（退出回流个人资本）</span>'
        '<span class="cap-lg"><span class="cap-lg-dot" style="background:#C84032"></span>个人投入</span>'
        '<span class="cap-lg"><span class="cap-lg-dot" style="background:#1f3a5f"></span>融资与 IPO</span>'
        '<span class="cap-lg"><span class="cap-lg-dot" style="background:#55524c"></span>收购与并购</span>'
        '<span class="cap-lg"><span class="cap-lg-dot" style="background:#8a6d1f"></span>政府资金</span>'
        '<span class="cap-lg"><span class="cap-lg-dot" style="background:#2E7D4F"></span>退出套现</span>'
        '</div>'
    )


def render_chips():
    chips = [
        f'<button type="button" class="cap-chip" data-cap-filter="all" aria-pressed="true">'
        f'<span data-en="All ({len(CAP.FLOWS)})">全部（{len(CAP.FLOWS)}）</span></button>'
    ]
    counts = {g: sum(1 for f in CAP.FLOWS if f["group"] == g) for g in CAP.GROUPS}
    for gid, g in CAP.GROUPS.items():
        chips.append(
            f'<button type="button" class="cap-chip" data-cap-filter="{gid}" aria-pressed="false">'
            f'<i style="background:{g["color"]}" aria-hidden="true"></i>'
            f'<span data-en="{esc(g["label"]["en"])} ({counts[gid]})">{esc(g["label"]["zh"])}（{counts[gid]}）</span></button>'
        )
    clear = ('<button type="button" class="cap-clear" data-cap-clear '
             'data-en="Clear filter">清除筛选</button>')
    status = (f'<span class="cap-status" id="cap-status" role="status" aria-live="polite" '
              f'data-en="Showing all {len(CAP.FLOWS)} flows · 1999–2026 · currency USD unless noted. '
              f'Select a line or a node for caliber and sources.">'
              f'显示全部 {len(CAP.FLOWS)} 笔流向 · 1999–2026 · 币种 USD（除注明外）。点击线条或节点查看口径与出处。</span>')
    return ('<div class="cap-controls" role="group" aria-label="按资金性质筛选">'
            + "".join(chips) + clear + '</div><p class="cap-statusline">' + status + '</p>')


def render_detail():
    return (
        '<div class="cap-detail" id="cap-detail" aria-live="polite">'
        '<p class="cap-detail-empty" data-en="Select a flow line or a node in the chart — or read the list below. '
        'No JS: the full list below is complete on its own.">'
        '在图上点选一条流向线或一个节点（支持 Tab + Enter）——或直接阅读下方清单；无脚本环境下列表即完整信息。</p>'
        '</div>'
    )


GROUP_ORDER = ["personal", "funding", "mna", "gov", "exit"]


def render_list():
    groups = []
    for gid in GROUP_ORDER:
        g = CAP.GROUPS[gid]
        rows = []
        for f in CAP.FLOWS:
            if f["group"] != gid:
                continue
            kind = CAP.KIND_LABELS[f["kind"]]
            prec = CAP.PRECISION_LABELS[f["precision"]]
            fn = f.get("from_note")
            a = f["amount"]
            srcs = " · ".join(
                f'<a href="{esc(s["href"])}" data-en="{esc(s["label"]["en"])}">{esc(s["label"]["zh"])}</a>'
                for s in f["sources"])
            src_hrefs = {s["href"] for s in f["sources"]}
            # 固定的「事件档案 →」「公司档案 →」仅在来源里没给过同一目标时补（避免重复链接）
            ev = (f' <a class="cap-li-ev" href="events.html#{f["event"]}" '
                  f'data-en="Event file →">事件档案 →</a>' if f.get("event") and ("events.html#" + f["event"]) not in src_hrefs else "")
            fl = (f'<a class="cap-li-file" href="company-files.html#{f["file"]}" data-en="Company file →">公司档案 →</a>'
                  if f.get("file") and ("company-files.html#" + f["file"]) not in src_hrefs else "")
            from_zh = fn["zh"] if fn else (
                SRC[f["from"]]["label"]["zh"] if f["from"] in SRC else CO[f["from"]]["label"]["zh"])
            from_en = (fn["en"] if fn else (
                SRC[f["from"]]["label"]["en"] if f["from"] in SRC else CO[f["from"]]["label"]["en"]))
            to_zh = CO[f["to"]]["label"]["zh"] if f["to"] in CO else SRC[f["to"]]["label"]["zh"]
            to_en = CO[f["to"]]["label"]["en"] if f["to"] in CO else SRC[f["to"]]["label"]["en"]
            dot = f'<span class="cap-li-dot" style="background:{g["color"]}" aria-hidden="true"></span>'
            rows.append(
                f'<li class="cap-li" data-cap-group="{gid}" data-cap-flow="{f["id"]}">{dot}'
                f'<div class="cap-li-main"><b class="cap-li-dir" '
                f'data-en="{esc(from_en + " → " + to_en)}">{esc(from_zh + " → " + to_zh)}</b> '
                f'<b class="cap-li-amt" data-en="{esc(a["en"])}">{esc(a["zh"])}</b> '
                f'<span class="cap-li-date">{esc(f["date"])}</span>'
                f'<span class="cap-li-badge" data-en="{esc(kind["en"])}">{esc(kind["zh"])}</span>'
                f'<span class="cap-li-badge cap-li-badge--p" data-en="{esc(prec["en"])}">{esc(prec["zh"])}</span><br>'
                f'<span class="cap-li-caliber">口径 <span data-en="{esc(f["caliber"]["en"])}">{esc(f["caliber"]["zh"])}</span></span><br>'
                f'<span class="cap-li-src">来源 <span data-en="Sources">来源</span> {srcs}{ev}{fl}</span></div></li>'
            )
        if rows:
            groups.append(
                f'<div class="cap-group" id="cap-g-{gid}"><h3 class="cap-gtitle">'
                f'<span class="cap-gdot" style="background:{g["color"]}" aria-hidden="true"></span>'
                f'<span data-en="{esc(g["label"]["en"])}">{esc(g["label"]["zh"])}</span>'
                f'<span class="cap-gcount">（{len(rows)}）</span></h3>'
                f'<ul class="cap-ul">{"".join(rows)}</ul></div>'
            )
    return '<div class="cap-list">' + "".join(groups) + '</div>'


def render_nonflow():
    nf = CAP.NON_FLOW_NOTE
    return (
        '<p class="cap-nonflow" data-en="' + esc(nf["en"]) + '">'
        '<b>不入图声明（非资金流动）</b>'
        + esc(nf["zh"]) +
        '口径详见 <a href="company-files.html">公司档案</a> 与 <a href="finance.html">财务资本全景</a>。</p>'
    )


def render_block():
    standfirst = {
        "zh": "12 个节点、18 笔真实发生的资金移动（1999–2026）：个人投入、融资与 IPO、收购并购、政府合同与贷款、退出套现，"
              "逐笔带日期精度、金额口径与站内出处。估值、市值与减记不是资金流动，不入图。"
              "点击线条或节点看口径与出处；手机与无脚本环境直接读下方清单。",
        "en": "12 nodes, 18 real money movements (1999–2026): founder capital, funding & IPO, acquisitions, government "
              "money and exits — each with date precision, amount caliber and on-site sources. Valuations, market caps "
              "and writedowns are not money movements and are never drawn. Select a line or node for caliber and sources; "
              "on mobile or without JS, read the list below.",
    }
    head = (
        '<header class="section-head reveal">'
        '<p class="kicker">⓪a / <span data-en="CAPITAL FLOWS">资本流向</span></p>'
        '<h2 data-en="Where the money came from, where it went">钱从哪来、押到哪去</h2>'
        f'<p class="section-standfirst" data-en="{esc(standfirst["en"])}">{esc(standfirst["zh"])}</p>'
        '</header>'
    )
    meta = (f'<p class="cap-meta" data-en="{len(SRC) + len(CO)} nodes · {len(CAP.FLOWS)} flows · 1999–2026 · currency USD unless noted · '
            f'amounts use wording already on file (no valuation/revenue mixing).">'
            f'{len(SRC) + len(CO)} 节点 · {len(CAP.FLOWS)} 笔流向 · 1999–2026 · 币种 USD（除注明外）· 金额一律使用站内在册口径（估值、收入不混写）。</p>')
    return (
        '<!-- V7-R10-CAPITAL:BEGIN -->\n'
        '<section id="flow" class="ce-era cap-sec">\n'
        + head + '\n' + meta + '\n'
        + render_chips() + '\n'
        + render_svg() + '\n'
        + render_legend() + '\n'
        + render_detail() + '\n'
        + render_list() + '\n'
        + render_nonflow() + '\n'
        + '</section>\n'
        + '<!-- V7-R10-CAPITAL:END -->'
    )


def build_js_data():
    nodes_src = [{
        "id": n["id"], "side": "src", "label": n["label"], "sub": n["sub"],
        "desc": n["desc"],
    } for n in CAP.SRC_NODES]
    nodes_co = [{
        "id": n["id"], "side": "co", "label": n["label"], "colorVar": n["color_var"],
        "href": n["href"],
    } for n in CAP.CO_NODES]
    flows = []
    for f in CAP.FLOWS:
        flows.append({
            "id": f["id"], "kind": f["kind"], "kindLabel": CAP.KIND_LABELS[f["kind"]],
            "group": f["group"], "from": f["from"], "fromNote": f.get("from_note"),
            "to": f["to"], "date": f["date"], "precision": f["precision"],
            "precisionLabel": CAP.PRECISION_LABELS[f["precision"]],
            "amount": f["amount"], "currency": f["currency"], "amountUsd": f["amount_usd"],
            "caliber": f["caliber"], "sources": f["sources"],
            "event": f.get("event"), "file": f.get("file"),
        })
    groups = [{"id": gid, "label": g["label"], "color": g["color"],
               "kinds": g["kinds"], "count": sum(1 for f in flows if f["group"] == gid)}
              for gid, g in CAP.GROUPS.items()]
    return {"plan": "V7-19 R10", "meta": {
        "nodes": len(nodes_src) + len(nodes_co), "flows": len(flows),
        "amounted": sum(1 for f in CAP.FLOWS if f["amount_usd"]),
        "span": "1999–2026", "currency": "USD"},
        "srcNodes": nodes_src, "coNodes": nodes_co, "flows": flows, "groups": groups}


ANCHOR_COMMENT = "<!-- ⓪ 资本流向图 -->"
BEGIN, END = "<!-- V7-R10-CAPITAL:BEGIN -->", "<!-- V7-R10-CAPITAL:END -->"
OLD_BLOCK_RE = re.compile(
    re.escape(ANCHOR_COMMENT) + r"[^\n]*\n"                       # 注释行
    r'|<div class="ce-flow" id="ce-flow">.*?</div>\n',            # 旧装饰图块
    re.S)


def inject(path_html):
    s = io.open(path_html, encoding="utf-8").read()
    block = render_block()
    if BEGIN in s and END in s:
        pat = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
        s2 = pat.sub(lambda m: block, s, count=1)
        how = "替换既有区块"
    elif 'id="ce-flow"' in s:
        # 首次接入：移除旧静态装饰图（含其前导注释），原位换入新区块
        s2, n = OLD_BLOCK_RE.subn("", s)
        if n == 0 or 'id="ce-flow"' in s2:
            raise SystemExit(f"✗ {path_html}: 旧 #ce-flow 块移除失败，拒绝盲插")
        s2 = s2.replace('<div class="ce-era">\n', block + "\n\n  <div class=\"ce-era\">\n", 1)
        how = "移除旧 #ce-flow 装饰图并注入新区块"
    else:
        raise SystemExit(f"✗ {path_html}: 既无 {BEGIN} 也无旧 #ce-flow，拒绝盲插")
    tag = '<script src="capital-data.js"></script>'
    if tag not in s2:
        s2 = s2.replace('<script src="app.js"></script>',
                        tag + '\n  <script src="app.js"></script>', 1)
        how += " + 补挂 capital-data.js"
    if s2 == s:
        print(f"· {path_html}: 内容无变化")
        return False
    io.open(path_html, "w", encoding="utf-8", newline="\n").write(s2)
    print(f"✓ {path_html}: {how}")
    return True


def main():
    inject("capital-evolution.html")
    data = "window.CAPITAL_V7 = " + json.dumps(build_js_data(), ensure_ascii=False, indent=1) + ";\n"
    io.open("capital-data.js", "w", encoding="utf-8", newline="\n").write(data)
    print(f"✓ capital-data.js: CAPITAL_V7（{len(CAP.FLOWS)} 流向 · {len(SRC)+len(CO)} 节点）")


if __name__ == "__main__":
    main()
