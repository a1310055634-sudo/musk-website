# -*- coding: utf-8 -*-
"""公司关系总览生成器（V7-19 R7）。

用法: python tools/build-network.py
- 数据源: tools/companies-data.py（11 节点 · 13 关系，先过结构自检）；
- 产出 1: companies.html 注入/替换 <!-- V7-R7-NETWORK:BEGIN/END --> 区块
  （section#network：SVG 关系图 + 图例 + 交互详情面板 + 三组文字清单）；
- 产出 2: companies-data.js —— 【自 V7-19 R8 起移交 tools/build-company-files.py 写出】
  （含 window.COMPANIES_V7 + window.FILES_V7；本脚本只负责 companies.html 注入，
  以避免两个生成器写同一文件互相覆盖）；
- 幂等: 可重复运行，输出一致。

设计约定：
- SVG 全静态绘制（无 JS 也完整可读）；节点/边文字直接入图，色标只作辅助；
- 交互（点击/键盘查看详情）由 app.js 读取 companies-data.js 增强；
- ≤760px 隐藏 SVG，文字清单成为主形态（清单桌面同样可见，不是手机专属降级）；
- 边线均为在册证实关系（实线，收购带箭头）；虚线 = 编者关联，图例单独标明。
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


CD = load_module("companies-data.py", "companies_data")

problems = CD.validate()
if problems:
    for p in problems:
        print("✗", p)
    sys.exit(1)


def esc(s):
    return H.escape(str(s), quote=True)


# ---- SVG 布局（viewBox 0 0 1000 680；节点矩形 124×44，Musk 圆 r46）----
POS = {
    "musk": (500, 300),
    "tesla": (250, 110), "spacex": (450, 80), "x": (760, 250),
    "xai": (760, 430), "neuralink": (400, 560), "boring": (640, 580),
    "zip2": (90, 200), "paypal": (90, 400), "solarcity": (500, 610),
    "openai": (930, 340),
}
# 边短标签手工避让位（线的中点附近，已避开节点与其他标签）
LABEL_POS = {
    "l-musk-tesla": (365, 199), "l-musk-spacex": (485, 186),
    "l-musk-x": (630, 267), "l-musk-xai": (630, 377),
    "l-musk-neuralink": (442, 434), "l-musk-boring": (580, 444),
    "l-musk-solarcity": (516, 459), "l-musk-zip2": (295, 244),
    "l-musk-paypal": (295, 344), "l-musk-openai": (672, 316),
    "l-tesla-solarcity": (390, 380), "l-xai-x": (776, 340),
    "l-openai-xai": (860, 397),
}
NW, NH = 124.0, 44.0   # 节点矩形宽高
MR = 46.0              # Musk 圆半径

C = {c["id"]: c for c in CD.COMPANIES}


def node_half_exit(pid, dx, dy):
    """从节点中心沿 (dx,dy) 出发，回到节点边界的收缩距离。"""
    x, y = POS[pid]
    if pid == "musk":
        return MR
    hw, hh = NW / 2, NH / 2
    if abs(dx) < 1e-6 or abs(dy) < 1e-6:
        t = min(hw / max(abs(dx), 1e-6), hh / max(abs(dy), 1e-6))
    else:
        t = min(hw / abs(dx), hh / abs(dy))
    return t


def edge_path(lnk):
    """边线坐标：两端各收缩到节点边界外 2px；返回 (x1,y1,x2,y2)。"""
    a, b = POS[lnk["from"]], POS[lnk["to"]]
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = (dx * dx + dy * dy) ** 0.5
    ux, uy = dx / L, dy / L
    ta = node_half_exit(lnk["from"], ux, uy) + 3
    tb = node_half_exit(lnk["to"], -ux, -uy) + 3
    x1, y1 = a[0] + ux * ta, a[1] + uy * ta
    x2, y2 = b[0] - ux * tb, b[1] - uy * tb
    return x1, y1, x2, y2


def render_svg():
    defs = (
        '<defs>'
        '<marker id="net-arrow" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        '<path d="M0,0 L10,5 L0,10 z" fill="var(--ink-soft,#43464d)"></marker>'
        '</defs>'
    )
    edges, labels = [], []
    for lnk in CD.LINKS:
        x1, y1, x2, y2 = edge_path(lnk)
        to_id = lnk["to"]
        stroke = f"var({C[to_id]['color_var']})" if lnk["from"] == "musk" else f"var({C[lnk['from']]['color_var']})"
        dashed = ' stroke-dasharray="5 4"' if lnk["evidence"] == "editorial" else ""
        arrow = ' marker-end="url(#net-arrow)"' if lnk["type"] == "acquire" else ""
        width = "2.2" if lnk["type"] == "acquire" else "1.6"
        data_for = esc(",".join(sorted({lnk["from"], lnk["to"]})))
        edges.append(
            f'<line class="net-edge" x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" '
            f'stroke="{stroke}" stroke-width="{width}"{dashed}{arrow} data-net-link="{data_for}"></line>'
        )
        lx, ly = LABEL_POS[lnk["id"]]
        lang = ' lang="en"'  # 由 data-en 切换
        short = lnk["short"]
        labels.append(
            f'<text class="net-elabel" x="{lx}" y="{ly}" text-anchor="middle" '
            f'data-en="{esc(short["en"])}">{esc(short["zh"])}</text>'
        )
    nodes = []
    for c in CD.COMPANIES:
        x, y = POS[c["id"]]
        name = c.get("node_label", c["name"])
        era = c["era_short"]
        label = f"{name}（{c['sector']['zh']}·{era}）· 查看关系详情"
        label_en = f"{name} ({c['sector']['en']}, {era}) — view relationships"
        if c["id"] == "musk":
            body = (f'<circle cx="{x}" cy="{y}" r="{MR}" class="net-node-bg net-node-musk"></circle>'
                    f'<circle cx="{x}" cy="{y}" r="{MR}" class="net-node-ring"></circle>'
                    f'<text class="net-nname net-nname-musk" x="{x}" y="{y - 4}" text-anchor="middle">{esc(name)}</text>'
                    f'<text class="net-nera" x="{x}" y="{y + 14}" text-anchor="middle">{esc(era)}</text>')
        else:
            body = (f'<rect x="{x - NW/2:.0f}" y="{y - NH/2:.0f}" width="{NW:.0f}" height="{NH:.0f}" rx="7" '
                    f'class="net-node-bg"></rect>'
                    f'<rect x="{x - NW/2:.0f}" y="{y - NH/2:.0f}" width="{NW:.0f}" height="5" rx="2.5" '
                    f'fill="var({c["color_var"]})" class="net-node-bar"></rect>'
                    f'<text class="net-nname" x="{x}" y="{y - 1}" text-anchor="middle">{esc(name)}</text>'
                    f'<text class="net-nera" x="{x}" y="{y + 15}" text-anchor="middle">{esc(era)}</text>')
        nodes.append(
            f'<g class="net-node" data-net-node="{c["id"]}" role="button" tabindex="0" '
            f'aria-label="{esc(label)}" data-en-aria="{esc(label_en)}">{body}</g>'
        )
    title = '<title>公司关系总览：马斯克与 10 家公司的创立、入主与收购关系</title>'
    return (
        '<div class="net-graphwrap">'
        '<svg class="net-graph" viewBox="8 38 1004 612" role="group" '
        'aria-label="公司关系图：马斯克居中，向外辐射十条创立或入主关系；Tesla、xAI 分别收购 SolarCity 与 X。'
        '文字清单见图下方，手机端以清单为主。">'
        + title + defs + "".join(edges) + "".join(labels) + "".join(nodes) +
        '</svg></div>'
    )


def render_legend():
    items = [
        '<span class="net-lg"><span class="net-lg-line"></span>实线 = 在册证实关系</span>',
        '<span class="net-lg"><span class="net-lg-line net-lg-dash"></span>虚线 = 编者关联</span>',
        '<span class="net-lg"><svg width="26" height="10" aria-hidden="true"><line x1="0" y1="5" x2="18" y2="5" stroke="var(--ink-soft,#43464d)" stroke-width="1.6"/><path d="M18,1.5 L25,5 L18,8.5 z" fill="var(--ink-soft,#43464d)"/></svg>箭头 = 收购方向</span>',
        '<span class="net-lg"><span class="net-lg-bar"></span>节点顶条 = 公司色标（名称文字为准）</span>',
    ]
    return '<div class="net-legend" data-en="Solid = verified on file · Dashed = editorial · Arrow = acquisition direction · Top bar = company color (names are authoritative).">' + "".join(items) + '</div>'


def render_detail():
    return (
        '<div class="net-detail" id="net-detail" aria-live="polite">'
        '<p class="net-detail-empty" data-en="Select a company in the chart — or browse the list below. No JS: the full list below is complete on its own.">'
        '在图上点选一家公司（支持 Tab + Enter）——或直接阅读下方清单；无脚本环境下列表即完整信息。</p>'
        '</div>'
    )


LIST_GROUPS = [
    ("net-g-found", {"zh": "创立 · 入主 · 发起", "en": "Founded · Joined · Originated"},
     ["found", "chair", "originate"]),
    ("net-g-acquire", {"zh": "收购与合并", "en": "Acquisitions & mergers"}, ["acquire"]),
    ("net-g-editorial", {"zh": "编者关联（非当事方表述）", "en": "Editorial links (not a party's words)"}, ["rival_editorial"]),
]


def render_list():
    groups = []
    for gid, gt, types in LIST_GROUPS:
        rows = []
        for lnk in CD.LINKS:
            if lnk["type"] not in types:
                continue
            a, b = C[lnk["from"]], C[lnk["to"]]
            ev = CD.EVIDENCE_LABELS[lnk["evidence"]]
            src = lnk["source"]
            dot = f'<span class="net-li-dot" style="background:var({b["color_var"]})" aria-hidden="true"></span>'
            evc = f'<span class="net-ev net-ev--{lnk["evidence"]}" data-en="{esc(ev["en"])}">{esc(ev["zh"])}</span>'
            note = src["note"]
            rows.append(
                f'<li class="net-li" data-net-row="{esc(b["id"])}">{dot}<div class="net-li-main">'
                f'<b>{esc(a["name"])} → {esc(b["name"])}</b> '
                f'<span class="net-li-label" data-en="{esc(lnk["label"]["en"])}">{esc(lnk["label"]["zh"])}</span>'
                f'{evc}<br>'
                f'<span class="net-li-src">来源 <a href="{esc(src["href"])}" data-en="{esc(src["note"]["en"])}">{esc(note["zh"])}</a></span>'
                f'</div></li>'
            )
        if rows:
            groups.append(
                f'<div class="net-group" id="{gid}"><h3 class="net-gtitle" data-en="{esc(gt["en"])}">{esc(gt["zh"])}</h3>'
                f'<ul class="net-ul">{"".join(rows)}</ul></div>'
            )
    return '<div class="net-list">' + "".join(groups) + '</div>'


def render_block():
    standfirst = {
        "zh": "11 个节点、13 条关系：实线是在册证实的关系（来源逐条可查），虚线是编者归纳。"
              "点选节点看业务定位、相关事件与资料；手机与无脚本环境直接读下方清单。",
        "en": "11 nodes, 13 links: solid lines are verified relationships (each with a source), dashed lines are editorial. "
              "Select a node for positioning, related events and files; on mobile or without JS, read the list below.",
    }
    head = (
        '<header class="section-head reveal">'
        '<p class="kicker">03b / <span data-en="RELATIONS">关系总览</span></p>'
        '<h2 data-en="The company map, as a network">关系网：一家公司如何长成一片版图</h2>'
        f'<p class="section-standfirst" data-en="{esc(standfirst["en"])}">{esc(standfirst["zh"])}</p>'
        '</header>'
    )
    note = (
        '<p class="net-note" data-en="Amounts use the wording already on file on this site; valuations and revenue are not mixed. '
        'The 2025 xAI–X deal is filed in the ledger (primary.html#e2025-03-28) and the xAI &amp; Grok file.">'
        '金额一律使用站内在册口径，不混用估值与收入；2025 年 xAI–X 交易见账本 '
        '<a href="primary.html#e2025-03-28">e2025-03-28</a> 与 <a href="grok.html">xAI·Grok 档案</a>。</p>'
    )
    return (
        '<!-- V7-R7-NETWORK:BEGIN -->\n'
        '<section id="network" class="section container">\n'
        + head + '\n'
        + render_svg() + '\n'
        + render_legend() + '\n'
        + render_detail() + '\n'
        + render_list() + '\n'
        + note + '\n'
        + '</section>\n'
        + '<!-- V7-R7-NETWORK:END -->'
    )


def build_js_data():
    companies = []
    for c in CD.COMPANIES:
        evs = CD.events_for_company(c["id"])
        companies.append({
            "id": c["id"], "name": c.get("node_label", c["name"]),
            "sector": c["sector"], "era": c["era"], "eraShort": c["era_short"],
            "status": c["status"], "statusLabel": CD.STATUS_LABELS[c["status"]],
            "colorVar": c["color_var"], "blurb": c["blurb"], "href": c["href"],
            "events": [{"id": e["id"], "date": e["date"], "title": e["title"]} for e in evs],
        })
    links = []
    for lnk in CD.LINKS:
        links.append({
            "id": lnk["id"], "from": lnk["from"], "to": lnk["to"], "type": lnk["type"],
            "typeLabel": CD.REL_LABELS[lnk["type"]], "date": lnk["date"],
            "label": lnk["label"], "short": lnk["short"], "evidence": lnk["evidence"],
            "evidenceLabel": CD.EVIDENCE_LABELS[lnk["evidence"]], "source": lnk["source"],
        })
    return {"plan": "V7-19 R7", "companies": companies, "links": links}


ANCHOR = "<!-- V7-R7-NETWORK:INSERT -->"
BEGIN, END = "<!-- V7-R7-NETWORK:BEGIN -->", "<!-- V7-R7-NETWORK:END -->"


def inject(path_html):
    s = io.open(path_html, encoding="utf-8").read()
    block = render_block()
    if BEGIN in s and END in s:
        pat = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.S)
        s2 = pat.sub(lambda m: block, s, count=1)
        how = "替换既有区块"
    elif ANCHOR in s:
        s2 = s.replace(ANCHOR, block + "\n" + ANCHOR, 1)
        how = "锚点插入新区块"
    else:
        raise SystemExit(f"✗ {path_html}: 既无 {BEGIN} 也无 {ANCHOR}，拒绝盲插")
    # 自动补挂 companies-data.js（app.js 交互的数据源；file:// 下 script 标签加载）
    tag = '<script src="companies-data.js"></script>'
    if tag not in s2:
        s2 = s2.replace('<script src="app.js"></script>',
                        tag + '\n  <script src="app.js"></script>', 1)
        how += " + 补挂 companies-data.js"
    if s2 == s:
        print(f"· {path_html}: 内容无变化")
        return False
    io.open(path_html, "w", encoding="utf-8", newline="\n").write(s2)
    print(f"✓ {path_html}: {how}")
    return True


def main():
    changed = inject("companies.html")
    # companies-data.js 自 V7-19 R8 起由 tools/build-company-files.py 写出
    # （COMPANIES_V7 + FILES_V7 一并导出），本脚本不再写它，避免互相覆盖。
    print("· companies-data.js 由 tools/build-company-files.py 统一写出（R8 起）")
    if not changed:
        print("· companies.html 区块内容与上次一致（幂等）")


if __name__ == "__main__":
    main()
