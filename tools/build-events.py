# -*- coding: utf-8 -*-
"""生成 events.html（静态事件档案页）与 events-data.js（本地 JS 数据）。V7-19 R6

用法：python tools/build-events.py
（站点根目录执行；幂等可重跑，events.html 整页由本生成器重建。）

产出：
  events.html     —— 6 个代表性事件的结构化静态详情（背景/关键事实/原话/后续/材料与证据），
                     中英双语 data-en，file:// 直接可用，无 JS 依赖（正文静态存在）；
  events-data.js  —— window.EVENTS_V7 = [...] 全量结构化数据（供 R7 公司关系视图、
                     R9 时间轴、R15 检索聚合消费；file:// 下以 script 标签加载，不用 fetch）。

数据源：tools/events-data.py（单一事实来源，含结构自检）。
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


ED = load_module("events-data.py", "events_data")
NAV = load_module("site-nav.py", "site_nav")

VERSION = io.open("VERSION", encoding="utf-8").read().strip()

problems = ED.validate()
if problems:
    for p in problems:
        print("✗", p)
    sys.exit(1)


def esc(s):
    return H.escape(s, quote=True)


def t(obj, lang):
    return obj[lang] if obj else ""


def attr_en(obj):
    return esc(t(obj, "en")) if obj else ""


# ---------------- 各事件 section ----------------
def render_material(m):
    kind = ED.KIND_LABELS[m["kind"]]
    date = f'<span class="ev-mat-date">{esc(m["date"])}</span>' if m.get("date") else ""
    label = t(m["label"], "zh")
    note = (f'<span class="ev-mat-note" data-en="{attr_en(m.get("note"))}">{esc(t(m["note"], "zh"))}</span>'
            if m.get("note") else "")
    if m.get("href"):
        inner = f'<a href="{esc(m["href"])}">{esc(label)}</a>'
    else:
        inner = f'<span class="ev-mat-plain">{esc(label)}</span>'
    return (f'        <li><span class="ev-kind ev-kind-{m["kind"]}" data-en="{esc(kind["en"])}">{esc(kind["zh"])}</span>'
            f'{inner}{date}{note}</li>')


def render_event(ev):
    prec = ED.PRECISION_LABELS[ev["precision"]]
    # V7-R7：chip 附公司色标类（名称文字为准，色条只作辅助；映射表与 companies-data.py 同源口径）
    _co = {"Tesla": "tesla", "SpaceX": "spacex", "X": "x", "X（原 Twitter）": "x",
           "xAI": "xai", "SolarCity": "solarcity", "PayPal": "paypal"}
    chips = "".join(
        f'<span class="ev-chip ev-chip--{_co.get(c, "default")}" data-en="{esc(c)}">{esc(c)}</span>'
        for c in ev["companies"])
    head = (f'      <div class="ev-head">\n'
            f'        <span class="ev-date">{esc(ev["date"])}</span>'
            f'<span class="ev-precision" data-en="{esc(prec["en"])}">{esc(prec["zh"])}</span>'
            f'<span class="ev-companies">{chips}</span>\n'
            f'      </div>')

    secs = []
    secs.append(f'      <div class="ev-sec"><h3 class="ev-label" data-en="Background">背景</h3>\n'
                f'        <p data-en="{attr_en(ev["background"])}">{esc(t(ev["background"], "zh"))}</p></div>')

    facts = "".join(f'\n        <li data-en="{attr_en(f)}">{esc(t(f, "zh"))}</li>' for f in ev["facts"])
    secs.append(f'      <div class="ev-sec"><h3 class="ev-label" data-en="Key facts">关键事实</h3>\n'
                f'        <ul class="ev-facts">{facts}\n        </ul>\n'
                f'        <p class="ev-facts-note" data-en="Editorial summaries structured from the records below — not his words.">关键事实为编者归纳，依据本节下方材料整理；非当事人原话。</p></div>')

    if ev["quotes"]:
        qs = []
        for q in ev["quotes"]:
            qs.append(f'        <blockquote class="lr-quote">“{esc(q["en"])}”'
                      f'<p class="lr-quote-zh">{esc(q["zh"])}</p>'
                      f'<cite class="ev-quote-src" data-en="{attr_en(q.get("source"))}">—— {esc(t(q.get("source"), "zh"))}</cite></blockquote>')
        words = "\n".join(qs)
    else:
        nq = ev["no_quote_note"]
        words = (f'        <p class="ev-noquote" data-en="{attr_en(nq)}">{esc(t(nq, "zh"))}</p>')
    secs.append(f'      <div class="ev-sec"><h3 class="ev-label" data-en="The words">原话</h3>\n{words}\n      </div>')

    secs.append(f'      <div class="ev-sec"><h3 class="ev-label" data-en="Aftermath">后续结果</h3>\n'
                f'        <p data-en="{attr_en(ev["outcome"])}">{esc(t(ev["outcome"], "zh"))}</p></div>')

    mats = "\n".join(render_material(m) for m in ev["materials"])
    secs.append(f'      <div class="ev-sec"><h3 class="ev-label" data-en="Materials &amp; evidence">材料与证据</h3>\n'
                f'        <ul class="ev-materials">\n{mats}\n        </ul>\n'
                f'        <p class="ev-materials-note" data-en="One event, several records — listed separately; the ledger entry is the baseline account.">同一事件的不同记录分开列示；事实表述以账本条目为基准口径。</p></div>')

    fig = ""
    if ev.get("image"):
        im = ev["image"]
        fig = (f'      <figure class="ev-fig">\n'
               f'        <img src="{esc(im["src"])}" width="{im["w"]}" height="{im["h"]}" loading="lazy" alt="{attr_en(im["alt"])}" />\n'
               f'        <figcaption data-en="{attr_en(im.get("caption"))}">{esc(t(im.get("caption"), "zh"))}</figcaption>\n'
               f'      </figure>')

    rel = ""
    if ev["related"]:
        links = "".join(f'\n          <a href="{esc(r["href"])}" data-en="{attr_en(r["label"])}">{esc(t(r["label"], "zh"))}</a>'
                        for r in ev["related"])
        rel = (f'      <p class="ev-related"><span class="ev-related-h" data-en="See also">相关事件</span>{links}\n'
               f'      </p>')

    return (f'    <section class="ev-item lr-sec" id="{ev["id"]}">\n'
            f'{head}\n'
            f'      <h2 class="ev-title" data-en="{attr_en(ev["title"])}">{esc(t(ev["title"], "zh"))}</h2>\n'
            f'      <p class="ev-summary" data-en="{attr_en(ev["summary"])}">{esc(t(ev["summary"], "zh"))}</p>\n'
            + "\n".join(secs) + "\n" + fig + "\n" + rel + "\n    </section>")


sections = "\n".join(render_event(ev) for ev in ED.EVENTS)

toc_links = "\n".join(
    f'          <a href="#{ev["id"]}">{esc(ev["date"])} · {esc(t(ev["title"], "zh"))}</a>'
    for ev in ED.EVENTS)

readme = (
    '<div class="lr-note" id="ev-readme">'
    '<b data-en="HOW TO READ">读法与口径</b>'
    '<span data-en="The event record answers what happened; the materials section lists the different records describing it — ledger entries are the first-hand baseline, documents and posts are checkable originals, editorial summaries are labeled as such. Date precision is badged (day / month / year) for honest filing, never fabricated.">'
    '「事件」记录回答发生了什么；「材料与证据」列出描述同一事件的不同记录——账本条目是一手基准口径，文档与帖子是可查原件，编者归纳均已标注。日期精度以徽标标明（精确到日 / 精确到月 / 仅年份），只作诚实的档案分层，不作超出材料的日期断言。'
    '</span></div>')

PAGE = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>事件档案 · 马斯克商业志 MUSK, INC.</title>
<meta name="description" content="六个代表性商业事件的结构化档案：背景、关键事实、逐字原话、后续结果与全部材料关联——事件与材料分开建档。" />
<meta property="og:title" content="事件档案 · 马斯克商业志 MUSK, INC." />
<meta property="og:description" content="事件与材料分开建档：每个节点汇齐背景、事实、原话、后续与全部证据。" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%237c2d2d'/%3E%3Ctext x='32' y='45' font-family='Georgia,serif' font-size='36' font-style='italic' fill='%23faf9f6' text-anchor='middle'%3EM%3C/text%3E%3C/svg%3E" />
<link rel="stylesheet" href="style.css" />
</head>
<body>
{NAV.build_masthead("events.html")}
  <main>
    <div class="lr-hero">
      <div class="container lr-hero-inner">
        <p class="ev-kicker">EVENT FILES · V7-R6</p>
        <h1 data-en="Event Files">事件档案</h1>
        <p class="ev-lead" data-en="Events and the records describing them, filed separately: background, facts, verbatim quotes, aftermath and every linked piece of evidence for each node. First batch: six representative events migrated from the 67-entry ledger.">把「事件」和「描述它的材料」分开建档：每个节点汇齐背景、关键事实、逐字原话、后续结果与全部材料关联。首批从 67 条言行账本迁移六个代表性事件。</p>
        <div class="lr-meta">
          <span data-en="6 representative events">6 个代表性事件</span>
          <span data-en="2002&ndash;2024">2002–2024</span>
          <span data-en="First batch from the 67-entry ledger">首批迁移自 67 条言行账本</span>
          <span data-en="Built at v{VERSION}">v{VERSION} 建档</span>
        </div>
      </div>
    </div>
    <div class="lr-layout">
      <div class="lr-main">
{readme}
{sections}
        <p class="lr-foot" data-en="Filed by tools/build-events.py from tools/events-data.py — one fact base for companies, events, timeline and search in later rounds.">本页由 tools/build-events.py 从单一事实来源 tools/events-data.py 生成；后续公司关系、时间轴与检索将复用同一份数据。账本全集见 <a href="primary.html">言行账本（67 条）</a>。</p>
      </div>
      <aside class="lr-toc" aria-label="本页事件目录">
        <p class="lr-toc-h">本页档案 · EVENT INDEX</p>
{toc_links}
        <a href="#ev-readme">读法与口径</a>
        <a href="primary.html">账本全集 · 67 条 →</a>
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

  <script src="events-data.js"></script>
  <script src="app.js"></script>
</body>
</html>
"""

io.open("events.html", "w", encoding="utf-8", newline="\n").write(PAGE)

js = ("// 事件档案结构化数据（V7-19 R6）· 由 tools/build-events.py 自动生成，勿手改\n"
      "// 数据源：tools/events-data.py · file:// 下以 <script src> 加载（fetch 会被 CORS 拦）\n"
      "window.EVENTS_V7 = " + json.dumps(ED.EVENTS, ensure_ascii=False, indent=1) + ";\n")
io.open("events-data.js", "w", encoding="utf-8", newline="\n").write(js)

n_q = sum(len(e["quotes"]) for e in ED.EVENTS)
n_m = sum(len(e["materials"]) for e in ED.EVENTS)
print(f"✓ events.html（{len(ED.EVENTS)} 事件 · {n_q} 引语 · {n_m} 材料）+ events-data.js 生成完毕（v{VERSION}）")
