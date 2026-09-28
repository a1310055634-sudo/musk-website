# -*- coding: utf-8 -*-
"""生成 company-files.html（公司档案页，第 34 页）与 companies-data.js。V7-19 R8

用法：python tools/build-company-files.py
（站点根目录执行；幂等可重跑，company-files.html 整页由本生成器重建。）

产出：
  company-files.html —— 4 份完整公司档案（Tesla / SpaceX / X / xAI：定位 · 里程碑 ·
                        财务口径 · 风险 · 相关事件与延伸阅读）+ 6 份公司简介，
                        中英双语 data-en，file:// 直接可用，无 JS 依赖（正文静态存在）；
  companies-data.js  —— window.COMPANIES_V7（R7 关系数据，本生成器自 R8 起接手写出）+
                        window.FILES_V7（档案数据出口，供 R9 时间轴 / R10 资本流向 /
                        R15 检索复用；file:// 下以 script 标签加载，不用 fetch）。

数据源：tools/company-files-data.py（档案单一事实来源，含结构自检）
       + tools/companies-data.py（节点表与事件交叉引用）。
版本：span 取自 VERSION（先改版本再重建本页）。
"""
import html as H
import importlib.util
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")
os.chdir(ROOT)


def load_module(fname, modname):
    spec = importlib.util.spec_from_file_location(modname, os.path.join(TOOLS, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


FD = load_module("company-files-data.py", "company_files_data")
CD = load_module("companies-data.py", "companies_data")
NW = load_module("build-network.py", "build_network")
NAV = load_module("site-nav.py", "site_nav")

VERSION = io.open("VERSION", encoding="utf-8").read().strip()

problems = FD.validate()
if problems:
    for p in problems:
        print("✗", p)
    sys.exit(1)
problems = CD.validate()
if problems:
    for p in problems:
        print("✗", p)
    sys.exit(1)


def esc(s):
    return H.escape(str(s), quote=True)


def t(obj, lang):
    return obj[lang] if obj else ""


def attr_en(obj):
    return esc(t(obj, "en")) if obj else ""


# href → 站内来源短标签（里程碑/财务/风险行的「核对 →」链接文字）
HREF_LABELS = {
    "primary.html":            {"zh": "言行账本", "en": "Ledger"},
    "documents.html":          {"zh": "一手文档", "en": "Document"},
    "x-posts.html":            {"zh": "X 帖史", "en": "X post"},
    "money.html":              {"zh": "资本解剖", "en": "Capital"},
    "finance.html":            {"zh": "财务全景", "en": "Finance"},
    "chronicle.html":          {"zh": "编年史", "en": "Chronicle"},
    "deep-dive-01.html":       {"zh": "资本运作深读", "en": "Capital deep dive"},
    "deep-dive-03.html":       {"zh": "失败模式深读", "en": "Failure deep dive"},
    "pricing.html":            {"zh": "定价页", "en": "Pricing"},
    "supplychain.html":        {"zh": "供应链页", "en": "Supply chain"},
    "stories.html":            {"zh": "商战时间轴", "en": "Takeover timeline"},
    "grok.html":               {"zh": "xAI·Grok 档案", "en": "xAI & Grok file"},
    "companies.html":          {"zh": "公司版图", "en": "Companies"},
    "companies.html#network":  {"zh": "关系总览", "en": "Network"},
    "profile.html":            {"zh": "速览", "en": "Profile"},
    "ai-strategy.html":        {"zh": "AI 战略全景", "en": "AI landscape"},
    "capital-evolution.html":  {"zh": "资本演化", "en": "Capital evolution"},
    "events.html":             {"zh": "事件档案", "en": "Event file"},
}


def src_label(href):
    """primary.html#e2008-12-24 → 账本；找不到映射时回退通用「在册来源」。"""
    base = href.split("#")[0] if not href.endswith(".html") else href
    lab = HREF_LABELS.get(base) or HREF_LABELS.get(href)
    if lab:
        return lab
    print(f"  · 提示：{href} 无来源短标签映射，回退「在册来源」")
    return {"zh": "在册来源", "en": "On file"}


def render_link(href, lang):
    lab = src_label(href)
    return f'<a class="cf-src" href="{esc(href)}" data-en="{esc("→ " + lab["en"])}">→ {esc(lab["zh"])}</a>'


def render_file(f):
    """一份完整档案 section。"""
    co_class = f["id"]
    head = (f'      <header class="cf-head cf-head--{co_class}">\n'
            f'        <div class="cf-idrow">\n'
            f'          <h2 class="cf-name" data-en="{attr_en({"zh": f["name"], "en": f["name"]})}">{esc(f["name"])}</h2>\n'
            + (f'          <span class="cf-ticker">{esc(f["ticker"])}</span>\n' if f.get("ticker") else "")
            + f'        </div>\n'
            f'        <p class="cf-asof" data-en="{attr_en(f["as_of"])}">{esc(t(f["as_of"], "zh"))}</p>\n'
            f'      </header>')

    fig = ""
    if f.get("image"):
        im = f["image"]
        fig = (f'      <figure class="cf-fig">\n'
               f'        <img src="{esc(im["src"])}" width="{im["w"]}" height="{im["h"]}" loading="lazy" decoding="async" alt="{attr_en(im["alt"])}" />\n'
               f'        <figcaption data-en="{attr_en(im["caption"])}">{esc(t(im["caption"], "zh"))}</figcaption>\n'
               f'      </figure>')

    pos = (f'      <div class="cf-sec"><h3 class="cf-label" data-en="Positioning · editorial">业务定位 · 编者归纳</h3>\n'
           f'        <p class="cf-pos" data-en="{attr_en(f["positioning"])}">{esc(t(f["positioning"], "zh"))}</p></div>')

    ms_rows = []
    for m in f["milestones"]:
        ms_rows.append(
            f'        <li class="cf-msrow">\n'
            f'          <span class="cf-date">{esc(m["date"])}</span>\n'
            f'          <div class="cf-msmain"><p data-en="{attr_en(m["text"])}">{esc(t(m["text"], "zh"))}</p>{render_link(m["href"], "zh")}</div>\n'
            f'        </li>')
    ms = (f'      <div class="cf-sec"><h3 class="cf-label" data-en="Milestones on file">关键里程碑（在册）</h3>\n'
          f'        <ul class="cf-ms">\n' + "\n".join(ms_rows) + '\n        </ul>\n'
          f'        <p class="cf-note" data-en="Only nodes already on file are listed; gaps mean no verified entry, not that nothing happened.">只列在册节点；空缺年份代表没有已核实条目，不代表无事发生。</p></div>')

    fin_rows = []
    for fn in f["finances"]:
        kind = FD.FIN_KINDS[fn["kind"]]
        fin_rows.append(
            f'        <li class="cf-finrow">\n'
            f'          <div class="cf-finline"><span class="cf-kind cf-kind--{fn["kind"]}" data-en="{esc(kind["en"])}">{esc(kind["zh"])}</span>'
            f'<span class="cf-date">{esc(fn["date"])}</span>'
            f'<b class="cf-amount" data-en="{esc(fn["amount"])}">{esc(fn["amount"])}</b></div>\n'
            f'          <p class="cf-finnote" data-en="{attr_en(fn["note"])}">{esc(t(fn["note"], "zh"))}{render_link(fn["href"], "zh")}</p>\n'
            f'        </li>')
    fin = (f'      <div class="cf-sec"><h3 class="cf-label" data-en="Financials by kind">财务口径（分列，不混用）</h3>\n'
           f'        <ul class="cf-fin">\n' + "\n".join(fin_rows) + '\n        </ul>\n'
           f'        <p class="cf-note" data-en="Funding, valuations, revenue and market cap are filed separately; private-company valuations are reported figures, not company disclosures.">融资、估值、收入与市值分列建档；私有公司估值均为公开报道口径，非公司披露。</p></div>')

    rk_rows = []
    for r in f["risks"]:
        rk_rows.append(
            f'        <li class="cf-rkrow"><a href="{esc(r["href"])}" data-en="{attr_en(r["title"])}">{esc(t(r["title"], "zh"))}</a>'
            f'<span class="cf-rknote" data-en="{attr_en(r["note"])}">{esc(t(r["note"], "zh"))}</span></li>')
    rk = (f'      <div class="cf-sec"><h3 class="cf-label" data-en="Risks &amp; controversies">风险与争议</h3>\n'
          f'        <ul class="cf-rk">\n' + "\n".join(rk_rows) + '\n        </ul></div>')

    # 相关事件：与 events-data.py 交叉引用（单一事实来源联动）
    evs = CD.events_for_company(f["id"])
    ev_html = ""
    if evs:
        links = "".join(
            f'\n          <a class="cf-ev" href="events.html#{esc(e["id"])}" data-en="{attr_en(e["title"])}"><b>{esc(e["date"])}</b> {esc(t(e["title"], "zh"))}</a>'
            for e in evs)
        ev_html = (f'      <div class="cf-sec"><h3 class="cf-label" data-en="Related event files">相关事件档案</h3>\n'
                   f'        <div class="cf-evs">{links}\n        </div></div>')

    rel_links = "".join(
        f'\n          <a href="{esc(r["href"])}" data-en="{attr_en(r["label"])}">{esc(t(r["label"], "zh"))}</a>'
        for r in f["related"])
    rel = (f'      <div class="cf-sec"><h3 class="cf-label" data-en="Further reading on this site">站内延伸阅读</h3>\n'
           f'        <div class="cf-rel">{rel_links}\n        </div></div>')

    return (f'    <section class="cf-file lr-sec" id="{f["slug"]}">\n' + head + "\n" + fig + "\n"
            + pos + "\n" + ms + "\n" + fin + "\n" + rk + "\n" + ev_html + "\n" + rel + "\n    </section>")


def render_brief(b):
    links = "".join(
        f'\n          <a href="{esc(l["href"])}" data-en="{attr_en(l["label"])}">{esc(t(l["label"], "zh"))}</a>'
        for l in b["links"])
    return (f'      <article class="cf-brief" id="{b["slug"]}">\n'
            f'        <div class="cf-brief-head"><span class="cf-brief-dot" style="background:var({b["color_var"]})" aria-hidden="true"></span>\n'
            f'          <h3 class="cf-brief-name" data-en="{attr_en({"zh": b["name"], "en": b["name"]})}">{esc(b["name"])}</h3>\n'
            f'          <span class="cf-brief-era" data-en="{attr_en(b["era"])}">{esc(t(b["era"], "zh"))}</span></div>\n'
            f'        <p class="cf-brief-text" data-en="{attr_en(b["text"])}">{esc(t(b["text"], "zh"))}</p>\n'
            f'        <div class="cf-brief-links"><span class="cf-brief-lh" data-en="On file:">在册入口：</span>{links}\n        </div>\n'
            f'      </article>')


# ---------------- 组装页面 ----------------
files_html = "\n".join(render_file(f) for f in FD.FILES)
briefs_html = "\n".join(render_brief(b) for b in FD.BRIEFS)

toc_links = "\n".join(
    [f'          <a href="#{f["slug"]}">{esc(f["name"])}</a>' for f in FD.FILES]
    + ['          <a href="#briefs" data-en="Six brief profiles">六份公司简介</a>']
    + [f'          <a href="#{b["slug"]}" class="cf-toc-sub">{esc(b["name"])}</a>' for b in FD.BRIEFS])

n_ev = sum(len(CD.events_for_company(f["id"])) for f in FD.FILES)

readme = (
    '<div class="lr-note" id="cf-readme">'
    '<b data-en="HOW TO READ">读法与口径</b>'
    '<span data-en="Each file answers five questions in order: what the business is (editorial positioning, labeled as such), which milestones are on file, the financials by kind — funding, valuations, revenue and market cap are never mixed — what the documented risks are, and where to verify everything. Every number and date links to its source on this site; each file carries an as-of line, and figures are not presented as current beyond it.">'
    '每份档案依次回答五个问题：这门业务是什么（业务定位，标注为编者归纳）、在册里程碑有哪些、财务口径如何分列（融资 / 估值 / 收入 / 市值绝不混写）、有据可查的风险与争议是什么、以及每一条去哪里核对。所有数字与日期都链向站内出处；每份档案带「截至」口径行，超出截止期的不冒充当前数字。'
    '</span></div>')

PAGE = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>公司档案 · 马斯克商业志 MUSK, INC.</title>
<meta name="description" content="四份完整公司档案（Tesla / SpaceX / X / xAI）与六份公司简介：业务定位、在册里程碑、分列财务口径、风险与争议、相关事件与延伸阅读——每一条都链向站内出处。" />
<meta property="og:title" content="公司档案 · 马斯克商业志 MUSK, INC." />
<meta property="og:description" content="四份完整公司档案与六份简介：定位、里程碑、财务口径、风险、事件与延伸阅读，逐条可核对。" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%237c2d2d'/%3E%3Ctext x='32' y='45' font-family='Georgia,serif' font-size='36' font-style='italic' fill='%23faf9f6' text-anchor='middle'%3EM%3C/text%3E%3C/svg%3E" />
<link rel="stylesheet" href="style.css" />
</head>
<body>
{NAV.build_masthead("company-files.html")}
  <main>
    <div class="lr-hero">
      <div class="container lr-hero-inner">
        <p class="ev-kicker">COMPANY FILES · V7-R8</p>
        <h1 data-en="Company Files">公司档案</h1>
        <p class="ev-lead" data-en="Four full company files — positioning, milestones on file, financials by kind, documented risks, related events and further reading — plus six brief profiles. Every line links back to its source on this site; every file carries an as-of line.">四份完整档案（业务定位 · 在册里程碑 · 财务口径分列 · 风险与争议 · 相关事件与延伸阅读）与六份公司简介。每一条都链向站内出处；每份档案带「截至」口径行。</p>
        <div class="lr-meta">
          <span data-en="4 full files">4 份完整档案</span>
          <span data-en="6 brief profiles">6 份公司简介</span>
          <span data-en="1995&ndash;2026">1995–2026</span>
          <span data-en="{n_ev} links into the event files">{n_ev} 条事件档案联动</span>
          <span data-en="Built at v{VERSION}">v{VERSION} 建档</span>
        </div>
      </div>
    </div>
    <div class="lr-layout">
      <div class="lr-main">
{readme}
{files_html}
        <section class="cf-file lr-sec" id="briefs">
          <header class="cf-head cf-head--briefs">
            <div class="cf-idrow"><h2 class="cf-name" data-en="Six brief profiles">六份公司简介</h2></div>
            <p class="cf-asof" data-en="One paragraph, one status line, and the on-file entry points — the full five-part treatment is reserved for the four files above.">一段话定位 + 状态行 + 在册入口；完整五段档案只保留给上面四家。</p>
          </header>
{briefs_html}
        </section>
        <p class="lr-foot" data-en="Filed by tools/build-company-files.py from tools/company-files-data.py — the same fact base behind the network view, the timeline and search.">本页由 tools/build-company-files.py 从单一事实来源 tools/company-files-data.py 生成；与关系总览、时间轴、检索共用同一份底层数据。事实核对全集见 <a href="primary.html">言行账本（67 条）</a>。</p>
      </div>
      <aside class="lr-toc" aria-label="本页档案目录">
        <p class="lr-toc-h">本页档案 · FILE INDEX</p>
{toc_links}
        <a href="#cf-readme" data-en="How to read">读法与口径</a>
        <a href="companies.html#network" data-en="Network · 13 links →">关系总览 · 13 条关系 →</a>
        <a href="primary.html" data-en="Full ledger · 67 entries →">账本全集 · 67 条 →</a>
      </aside>
    </div>
  </main>

  <!-- ============ 页脚 ============ -->
  <footer class="site-footer">
    <div class="container">
      <p class="footer-brand">马斯克商业志 <span class="brand-en">MUSK,&nbsp;INC.</span> <a class="footer-version" href="changelog.html" title="修订记录">v<span class="site-version-val">{VERSION}</span></a></p>
      <p class="footer-disclaimer" data-en="An unofficial, study-oriented business profile. Information compiled from public sources (Forbes, Reuters, CNBC, BBC, company announcements); photo via Wikimedia Commons. Not affiliated with or endorsed by Elon Musk or any of his companies.">
        本站为非官方、学习型的商业人物志。信息整理自公开资料（Forbes、Reuters、CNBC、BBC 及公司公告）；
        图片来自 Wikimedia Commons。与马斯克先生及其名下公司无任何隶属或背书关系。
      </p>
      <p class="footer-note" data-en="Built by scheduled autonomous iteration · full revision history in the changelog">由定时自主迭代持续构建 · 完整修订史见「修订记录」</p>
      <p class="footer-toplink"><a href="index.html" data-en="Back to top ↑">返回顶部 ↑</a></p>
    </div>
  </footer>

  <script src="companies-data.js"></script>
  <script src="app.js"></script>
</body>
</html>
"""

io.open("company-files.html", "w", encoding="utf-8", newline="\n").write(PAGE)

# ---------------- companies-data.js（自 R8 起由本生成器接手写出） ----------------
# COMPANIES_V7 与 R7 格式逐字节一致（复用 build-network.build_js_data()，app.js 交互依赖该结构）
js = ("// 公司关系与档案结构化数据（V7-19 R7/R8）· 由 tools/build-company-files.py 自动生成，勿手改\n"
      "// 数据源：tools/companies-data.py + tools/company-files-data.py · file:// 下以 <script src> 加载（fetch 会被 CORS 拦）\n"
      "window.COMPANIES_V7 = " + json.dumps(NW.build_js_data(), ensure_ascii=False, indent=1) + ";\n"
      "window.FILES_V7 = " + json.dumps(
          {"files": FD.FILES, "briefs": FD.BRIEFS, "finKinds": FD.FIN_KINDS},
          ensure_ascii=False, indent=1) + ";\n")
io.open("companies-data.js", "w", encoding="utf-8", newline="\n").write(js)

n_ms = sum(len(f["milestones"]) for f in FD.FILES)
n_fin = sum(len(f["finances"]) for f in FD.FILES)
n_rk = sum(len(f["risks"]) for f in FD.FILES)
print(f"✓ company-files.html（{len(FD.FILES)} 档案 · {n_ms} 里程碑 · {n_fin} 财务行 · {n_rk} 风险 · {len(FD.BRIEFS)} 简介 · {n_ev} 事件联动）+ companies-data.js 生成完毕（v{VERSION}）")
