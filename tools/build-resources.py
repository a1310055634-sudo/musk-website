# -*- coding: utf-8 -*-
"""生成 resources.html（社区资源页，第 38 页）。V9-20 R10

用法：python tools/build-resources.py
（站点根目录执行；幂等可重跑，resources.html 整页由本生成器重建。）

产出：resources.html —— 开源社区马斯克相关网站与资源清单：
      lr-hero 页头 + 分类筛选芯片（仿 gx-fchip）+ 分类清单（无 JS 完整可读）
      + 每条资源的详情字段行（网址/语言/活跃度/许可/关联公司/核活口径/GitHub 实测）。
      只收「链接 + 一句话简介 + 元数据」，不复制外部正文；外链不构成运行时依赖，
      页面本体静态、file:// 离线可读。

数据源：tools/resources-data.py（单一事实来源，含 validate()，不过校验拒绝生成）。
版本：span 与 lr-meta 取自 VERSION（先改版本再重建本页）。
"""
import html as H
import importlib.util
import io
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


RD = load_module("resources-data.py", "resources_data")
NAV = load_module("site-nav.py", "site_nav")

VERSION = io.open("VERSION", encoding="utf-8").read().strip()

problems = RD.validate()
if problems:
    for p in problems:
        print("✗", p)
    sys.exit(1)


def esc(s):
    return H.escape(str(s), quote=True)


def t(obj, lang="zh"):
    return obj[lang] if obj else ""


def attr_en(obj):
    return esc(t(obj, "en")) if obj else ""


# 活跃度徽标（与事件档案 ev-etype 色板同源：绿=活跃 / 棕=停更 / 灰=存档）
ACT_CLASS = {"维护中": "rs-act--on", "停更": "rs-act--stale", "存档": "rs-act--arch"}
ACT_EN = {"维护中": "Active", "停更": "Stale", "存档": "Archived"}
LANG_ZH = {"en": "英文", "zh": "中文", "zh/en": "双语"}
LANG_EN = {"en": "English", "zh": "Chinese", "zh/en": "Bilingual"}


def render_item(r):
    """一条资源的详情字段行。锚 id=r-<id>，与检索索引、verify 计数共用。"""
    cat = RD.CATEGORIES[r["category"]]
    gh = r.get("gh")
    gh_row = ""
    if gh:
        stars = f"{gh['stars']:,}"
        gh_row = (f'          <div class="rs-mrow"><dt data-en="GitHub (measured)">GitHub 实测</dt>'
                  f'<dd><span class="rs-gh">★ {esc(stars)} · {esc(gh["pushed"])} <span data-en="last push">最近提交</span></span></dd></div>\n')
    note_html = ""
    if r.get("note"):
        note_html = (f'          <div class="rs-mrow"><dt data-en="Note">口径备注</dt>'
                     f'<dd class="rs-note" data-en="{attr_en(r["note"])}">{esc(t(r["note"]))}</dd></div>\n')
    co_chips = "".join(f'<span class="rs-co">{esc(c)}</span>' for c in r["companies"])
    return (
        f'      <article class="rs-item" id="r-{r["id"]}">\n'
        f'        <h3 class="rs-name"><a href="{esc(r["url"])}" data-en="{attr_en(r["name"])}">{esc(t(r["name"]))}</a><span class="rs-ext" aria-hidden="true">\N{NORTH EAST ARROW}</span></h3>\n'
        f'        <p class="rs-desc" data-en="{attr_en(r["desc"])}">{esc(t(r["desc"]))}</p>\n'
        f'        <dl class="rs-meta">\n'
        f'          <div class="rs-mrow"><dt data-en="URL">网址</dt><dd><a class="rs-url" href="{esc(r["url"])}">{esc(r["url"])}</a></dd></div>\n'
        f'          <div class="rs-mrow"><dt data-en="Category">分类</dt><dd><span class="rs-badge rs-badge--{r["category"]}" data-en="{attr_en(cat)}">{esc(t(cat))}</span></dd></div>\n'
        f'          <div class="rs-mrow"><dt data-en="Language">语言</dt><dd><span data-en="{esc(LANG_EN[r["lang"]])}">{esc(LANG_ZH[r["lang"]])}</span></dd></div>\n'
        f'          <div class="rs-mrow"><dt data-en="Status">活跃度</dt><dd><span class="rs-act {ACT_CLASS[r["activity"]]}" data-en="{esc(ACT_EN[r["activity"]])}">{esc(r["activity"])}</span></dd></div>\n'
        f'          <div class="rs-mrow"><dt data-en="License">许可</dt><dd data-en="{attr_en(r["license"])}">{esc(t(r["license"]))}</dd></div>\n'
        f'          <div class="rs-mrow"><dt data-en="Companies">关联公司</dt><dd>{co_chips}</dd></div>\n'
        f'{gh_row}'
        f'          <div class="rs-mrow"><dt data-en="Live check">核活</dt><dd><span class="rs-check">{esc(r["checked"])} · HTTP {r["http"]}</span></dd></div>\n'
        f'{note_html}'
        f'        </dl>\n'
        f'        <p class="rs-reason"><b data-en="WHY LISTED">收录理由</b><span data-en="{attr_en(r["reason"])}">{esc(t(r["reason"]))}</span></p>\n'
        f'      </article>')


# 分类节（每类一节，节内按数据文件原序）
cat_sections = []
for cid, cat in RD.CATEGORIES.items():
    entries = [r for r in RD.RESOURCES if r["category"] == cid]
    if not entries:
        continue
    items_html = "\n".join(render_item(r) for r in entries)
    cat_sections.append(
        f'    <section class="lr-sec rs-cat" id="cat-{cid}" data-cat="{cid}">\n'
        f'      <h2><span class="rs-catname" data-en="{attr_en(cat)}">{esc(t(cat))}</span><span class="rs-catcount">{len(entries)}</span></h2>\n'
        f'{items_html}\n'
        f'    </section>')

# 分类筛选芯片（无 JS 时为惰性按钮，页面默认全量可见）
chips = [f'        <button type="button" class="gx-fchip rs-fchip" data-cat="all" aria-pressed="true" data-zh-label="全部" data-en-label="All"><span data-en="All ({len(RD.RESOURCES)})">全部 · {len(RD.RESOURCES)}</span></button>']
for cid, cat in RD.CATEGORIES.items():
    n = sum(1 for r in RD.RESOURCES if r["category"] == cid)
    chips.append(
        f'        <button type="button" class="gx-fchip rs-fchip" data-cat="{cid}" aria-pressed="false" data-zh-label="{esc(t(cat))}" data-en-label="{attr_en(cat)}"><span data-en="{attr_en(cat)} ({n})">{esc(t(cat))} · {n}</span></button>')
chips_html = "\n".join(chips)

# 目录
toc_links = "\n".join(
    [f'          <a href="#cat-{cid}" data-en="{attr_en(cat)}">{esc(t(cat))}</a>'
     for cid, cat in RD.CATEGORIES.items()
     if any(r["category"] == cid for r in RD.RESOURCES)]
    + [f'          <a href="#r-{r["id"]}" class="rs-toc-sub" data-en="{attr_en(r["name"])}">{esc(t(r["name"]))}</a>'
       for r in RD.RESOURCES]
    + ['          <a href="#rs-readme" data-en="How to read">读法与口径</a>'])

n_gh = sum(1 for r in RD.RESOURCES if r.get("gh"))
last_check = max(r["checked"] for r in RD.RESOURCES)

readme = (
    '<div class="lr-note" id="rs-readme">'
    '<b data-en="HOW TO READ">读法与口径</b>'
    '<span data-en="This section lists community and open-source web resources related to Elon Musk and his companies — links plus a one-line description and metadata only; no external content is reproduced. External links are not a runtime dependency: the page itself is static and fully readable offline (file://). Every URL was live-checked on its &quot;live check&quot; date (curl status or fetch); dead links would be marked &quot;Archived&quot;, not removed. GitHub entries record stars and last-push month as measured on that date — they age. Nothing here is an official source for quotations; for verbatim sourcing use the ledger, documents, interviews and X posts sections.">'
    '本板块收录马斯克及其公司相关的开源社区网站与资源：只收「链接 + 一句话简介 + 元数据」，不复制外部内容正文。外链不构成运行时依赖——页面本体静态、file:// 离线可读。每条 URL 都在「核活」栏注明的日期实测过（curl 状态码或抓取核验）；死链会如实标「存档」，不会悄悄删除。GitHub 条目的星数与最近提交为核活当日实测值，会随时间过期。本板块资源一律不作为引语出处；查证原话请走言行账本、一手文档、访谈与 X 帖史。'
    '</span></div>')

PAGE = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>社区资源 · 马斯克商业志 MUSK, INC.</title>
<meta name="description" content="开源社区马斯克相关网站与资源清单：官方与标准、开源项目、社区与档案、工具与数据——只收链接、一句话简介与元数据，不复制外部正文；每条 URL 实测核活，外链不构成运行时依赖，file:// 离线可读。" />
<meta property="og:title" content="社区资源 · 马斯克商业志 MUSK, INC." />
<meta property="og:description" content="马斯克相关开源社区资源：官方与标准、开源项目、社区与档案、工具与数据，逐条核活、逐字段建档。" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%237c2d2d'/%3E%3Ctext x='32' y='45' font-family='Georgia,serif' font-size='36' font-style='italic' fill='%23faf9f6' text-anchor='middle'%3EM%3C/text%3E%3C/svg%3E" />
<link rel="stylesheet" href="style.css" />
</head>
<body>
{NAV.build_masthead("resources.html")}
  <main>
    <div class="lr-hero">
      <div class="container lr-hero-inner">
        <p class="ev-kicker">COMMUNITY RESOURCES · V9-R10</p>
        <h1 data-en="Community Resources">社区资源</h1>
        <p class="ev-lead" data-en="Open-source and community web resources on Elon Musk and his companies — official &amp; standards, open source, community &amp; archives, tools &amp; data. Links plus a one-line description and metadata only; every URL live-checked, no external content reproduced, fully readable offline.">马斯克及其公司相关的开源社区网站与资源：官方与标准 · 开源项目 · 社区与档案 · 工具与数据。只收链接、一句话简介与元数据；逐条 URL 实测核活，不复制外部正文，离线可读。</p>
        <div class="lr-meta">
          <span data-en="{len(RD.RESOURCES)} resources · {len(RD.CATEGORIES)} categories">{len(RD.RESOURCES)} 条资源 · {len(RD.CATEGORIES)} 类</span>
          <span data-en="All live-checked {last_check}">全部核活于 {last_check}</span>
          <span data-en="{n_gh} GitHub entries with measured stars">{n_gh} 条 GitHub 实测</span>
          <span data-en="Links only — no external content reproduced">只收链接，不复制正文</span>
          <span data-en="Built at v{VERSION}">v{VERSION} 建档</span>
        </div>
      </div>
    </div>
    <div class="lr-layout">
      <div class="lr-main">
{readme}
        <div class="rs-chipbar" role="group" aria-label="按分类筛选资源">
{chips_html}
        </div>
        <p class="rs-status" id="rs-status" data-en="Showing all {len(RD.RESOURCES)} resources · {len(RD.CATEGORIES)} categories · filtering needs JavaScript; without it the full list below is complete.">显示全部 {len(RD.RESOURCES)} 条资源 · {len(RD.CATEGORIES)} 类 · 筛选需脚本支持；无脚本环境下方清单即完整信息。</p>
{chr(10).join(cat_sections)}
        <p class="lr-foot" data-en="Filed by tools/build-resources.py from tools/resources-data.py — the single source of truth. Live checks were run from the build machine on the date each entry records; regional blocking may differ. External links are independent third-party resources, listed not endorsed.">本页由 tools/build-resources.py 从单一事实来源 tools/resources-data.py 生成。核活在生成机于各条注明日期实测，地区性屏蔽可能造成差异；外链均为独立第三方资源，收录不构成背书。第一手引语的核对入口见 <a href="primary.html">言行账本</a> 与 <a href="search.html">第一手检索</a>。</p>
      </div>
      <aside class="lr-toc" aria-label="本页资源目录">
        <p class="lr-toc-h">资源目录 · RESOURCE INDEX</p>
{toc_links}
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

  <script src="app.js"></script>
  <script>
  (function () {{
    var chips = Array.prototype.slice.call(document.querySelectorAll('.rs-fchip'));
    var cats = Array.prototype.slice.call(document.querySelectorAll('.rs-cat'));
    var status = document.getElementById('rs-status');
    function apply(cat) {{
      chips.forEach(function (c) {{
        c.setAttribute('aria-pressed', String(c.getAttribute('data-cat') === cat));
      }});
      var n = 0;
      cats.forEach(function (sec) {{
        var show = (cat === 'all') || (sec.getAttribute('data-cat') === cat);
        sec.classList.toggle('rs-cat-off', !show);
        if (show) n += sec.querySelectorAll('.rs-item').length;
      }});
      if (status) {{
        var en = document.documentElement.lang === 'en';
        var label = 'all';
        chips.forEach(function (c) {{
          if (c.getAttribute('data-cat') === cat) label = en ? c.getAttribute('data-en-label') : c.getAttribute('data-zh-label');
        }});
        status.textContent = en
          ? 'Showing ' + n + ' resources · ' + label + ' · without JavaScript the full list above is complete.'
          : '显示 ' + n + ' 条资源 · ' + label + ' · 无脚本环境上方清单即完整信息。';
      }}
    }}
    chips.forEach(function (c) {{
      c.addEventListener('click', function () {{ apply(c.getAttribute('data-cat')); }});
    }});
  }})();
  </script>
</body>
</html>
"""

io.open("resources.html", "w", encoding="utf-8", newline="\n").write(PAGE)

n_items = len(RD.RESOURCES)
print(f"✓ resources.html（{n_items} 条 · {len(RD.CATEGORIES)} 类 · {n_gh} 条 GitHub 实测 · 核活 {last_check}）生成完毕（v{VERSION}）")
