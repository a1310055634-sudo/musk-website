# -*- coding: utf-8 -*-
"""V7-19 R4: 全站统一导航生成器（单一事实来源）。

用法: python tools/site-nav.py
- 以 NAV_GROUPS 注册表为唯一导航数据源，生成统一 masthead；
- 32 页逐页注入/替换（已有 <header class="masthead"> 则整块替换，否则插在 <body> 后）；
- 当前页链接自动标注 aria-current="page"；
- 缺 app.js 的页面自动补挂（语言切换/版本号依赖）；
- 幂等：可重复运行，输出一致。

设计约定：
- 桌面 ≥961px：分组标签 hover / focus-within / .open 展开下拉；
- 手机 ≤960px：汉堡开合面板，分组手风琴（.open），JS 自动展开当前组。
"""
import io
from datetime import datetime, timezone, timedelta
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- 导航注册表：五组 40 页，顺序即展示顺序 ----
NAV_GROUPS = [
    {
        "zh": "开始", "en": "Start",
        "items": [
            ("index.html", "首页", "Home"),
            ("reading.html", "长卷通读", "The Long Read"),
            ("profile.html", "速览", "Profile"),
            ("persona.html", "商业人格", "Persona"),
            ("playbook.html", "可复用的方法", "Playbook"),
        ],
    },
    {
        "zh": "公司", "en": "Companies",
        "items": [
            ("companies.html", "公司版图", "Companies"),
            ("company-files.html", "公司档案", "Company Files"),
            ("indepth.html", "公司深度", "In Depth"),
            ("grok.html", "xAI·Grok", "xAI &amp; Grok"),
            ("numbers.html", "数据一览", "In Numbers"),
            ("finance.html", "财务资本全景", "Finance"),
            ("supplychain.html", "供应链与工厂", "Supply Chain"),
            ("pricing.html", "定价与需求", "Pricing"),
        ],
    },
    {
        "zh": "事件", "en": "Events",
        "items": [
            ("timeline.html", "商业时间线", "Timeline"),
            ("chronicle.html", "公司编年史", "Chronicles"),
            ("stories.html", "经典商战", "War Stories"),
            ("controversy.html", "争议与批评", "Controversies"),
            ("events.html", "事件档案", "Event Files"),
        ],
    },
    {
        "zh": "专题", "en": "Features",
        "items": [
            ("survival-2008.html", "专题·2008 生死役", "Feature: Survival 2008"),
            ("platform-x.html", "专题·平台变局", "Feature: Platform X"),
            ("promises.html", "专题·承诺与结果", "Feature: Promises"),
            ("deep-dive-01.html", "深读·资本运作", "Deep Dive: Capital"),
            ("deep-dive-02.html", "深读·用人逻辑", "Deep Dive: Hiring"),
            ("deep-dive-03.html", "深读·失败模式", "Deep Dive: Failure"),
            ("deep-dive-04.html", "深读·监管博弈", "Deep Dive: Regulation"),
            ("deep-dive-05.html", "深读·AI 战略", "Deep Dive: AI Strategy"),
            ("deep-dive-06.html", "深读·xAI 三年志", "Deep Dive: xAI"),
            ("deep-dive-07.html", "深读·Robotaxi 落地考", "Deep Dive: Robotaxi"),
            ("ai-strategy.html", "AI 战略全景", "AI Landscape"),
        ],
    },
    {
        "zh": "资料", "en": "Archive",
        "items": [
            ("primary.html", "言行账本", "Ledger"),
            ("quotes.html", "语录", "Quotes"),
            ("documents.html", "一手文档馆", "Documents"),
            ("interviews.html", "访谈与表态", "Interviews"),
            ("x-posts.html", "X 帖史", "X Posts"),
            ("resources.html", "社区资源", "Resources"),
            ("money.html", "资本解剖", "Capital"),
            ("capital-evolution.html", "资本演化", "Capital Evolution"),
            ("search.html", "第一手检索", "Search"),
            ("revisions.html", "修订历史", "Revisions"),
            ("changelog.html", "修订记录", "Changelog"),
        ],
    },
]

MASTHEAD_TMPL = """  <!-- ============ 报头（tools/site-nav.py 生成，勿手改分组） ============ -->
  <header class="masthead">
    <div class="container masthead-top">
      <a class="brand" href="index.html">
        <span class="brand-zh" data-en="Musk Business Review">马斯克商业志</span>
        <span class="brand-en">MUSK,&nbsp;INC.</span>
      </a>
      <div class="masthead-eyebrow">
        <span class="mh-dateline" data-en="{dateline_en}">{dateline_zh}</span>
        <span class="mh-sep" aria-hidden="true">—</span>
        <span class="masthead-issue" data-en="Business Profile · No. 001">商业人物志 · 创刊号</span>
        <span class="mh-sep" aria-hidden="true">—</span>
        <span class="mh-volno" title="版本三件套同源（VERSION / app.js / 页脚 span）">{volno}</span>
      </div>
      <div class="masthead-tools">
        <a class="masthead-search" href="search.html" data-en="Search">检索</a>
        <button class="lang-toggle" id="lang-toggle" type="button" aria-label="Switch language / 切换语言">EN</button>
        <button class="nav-toggle" id="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="打开菜单"><span></span><span></span><span></span></button>
      </div>
    </div>
    <nav class="container mainnav" id="site-nav" aria-label="主导航">
{groups}
    </nav>
  </header>"""

GROUP_TMPL = """      <div class="nav-group">
        <button class="nav-label" type="button" aria-expanded="false"><span class="nav-txt" data-en="{gen}">{gz}</span><span class="nav-caret" aria-hidden="true"></span></button>
        <div class="nav-drop">
{items}
        </div>
      </div>"""

ITEM_TMPL = '          <a href="{href}"{cur} data-en="{en}">{zh}</a>'


ROMAN = {10: "X", 11: "XI", 12: "XII"}


def build_masthead(current):
    """current: 文件名（如 'grok.html'），用于标注 aria-current。"""
    blocks = []
    for g in NAV_GROUPS:
        rows = []
        for href, zh, en in g["items"]:
            cur = ' aria-current="page"' if href == current else ""
            rows.append(ITEM_TMPL.format(href=href, cur=cur, en=en, zh=zh))
        blocks.append(GROUP_TMPL.format(gz=g["zh"], gen=g["en"], items="\n".join(rows)))
    # R15 刊头：期号（Vol.=主版本罗马数字/No.=VERSION，与页脚版本戳同源）+ 日期线（构建日北京时间）
    _root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ver = io.open(os.path.join(_root, "VERSION"), encoding="utf-8").read().strip()
    major = int(ver.split(".")[0])
    vol = ROMAN.get(major, "V" + "I" * major if major < 4 else str(major))
    now = datetime.now(timezone(timedelta(hours=8)))
    dateline_zh = "{y} 年 {m} 月 {d} 日".format(y=now.year, m=now.month, d=now.day)
    dateline_en = now.strftime("%B %d, %Y")
    return MASTHEAD_TMPL.format(
        groups="\n".join(blocks),
        volno="Vol. " + vol + " · No. <span class=\"site-version-val\">" + ver + "</span>",
        dateline_zh=dateline_zh, dateline_en=dateline_en)


MASTHEAD_RE = re.compile(r"[ \t]*<!-- ============[^\n]*报头[^\n]*============ -->\n[ \t]*<header class=\"masthead\">.*?</header>\n",
                         re.S)
PLAIN_MASTHEAD_RE = re.compile(r"[ \t]*<header class=\"masthead\">.*?</header>\n", re.S)


def process(path):
    fname = os.path.basename(path)
    s = io.open(path, encoding="utf-8").read()
    orig = s
    mast = build_masthead(fname)

    if MASTHEAD_RE.search(s) or PLAIN_MASTHEAD_RE.search(s):
        rx = MASTHEAD_RE if MASTHEAD_RE.search(s) else PLAIN_MASTHEAD_RE
        s = rx.sub(mast + "\n", s, count=1)
        action = "replaced"
    else:
        m = re.search(r"<body>\n", s)
        if not m:
            return fname, "NO-BODY", 0
        s = s[: m.end()] + mast + "\n" + s[m.end():]
        action = "inserted"

    if "app.js" not in s:
        s = s.replace("</body>", "  <script src=\"app.js\"></script>\n</body>")
        action += "+appjs"

    if s != orig:
        io.open(path, "w", encoding="utf-8", newline="\n").write(s)
    return fname, action, len(s)


def main():
    pages = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))
    changed = 0
    for p in pages:
        fname, action, size = process(os.path.join(ROOT, p))
        print(f"{fname:24s} {action:14s} {size}B")
        if action != "NO-BODY":
            changed += 1
    print(f"-- {changed}/{len(pages)} pages processed")


if __name__ == "__main__":
    sys.exit(main())
