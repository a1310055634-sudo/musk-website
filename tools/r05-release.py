# -*- coding: utf-8 -*-
"""R05 发布流程：CHANGELOG 记账 → 版本步进（VERSION/app.js/全站 span）。
span 正则取自 r02-spans.py 修好版（含收尾 `<`，断言 14）。"""
import io, re, glob, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- 1) CHANGELOG 记账 ----------
ENTRY = """## v7.5.0 — 2026-09-30 · V8 扩充（5/10）：财报电话会 II（2019–2026）

**主题包成果（V8 R05 · primary.html 93 → 103 条）**
- **十条财报电话会条目入册（引语逐字取自逐字稿，关键句两源印证）**：
  **e2019-04-24** Q1 2019「斯巴达饮食」与「强制函数」——八天后 23→27 亿美元增发（Reuters「ends Spartan diet」印证）；
  **e2020-01-29** Q4 2019 Cybertruck 需求「难以置信」+ FSD「几个月 feature complete」（Fortune 当日印证）；
  **e2020-07-22** Q2 2020 FSD「年底前完成」+「一场『九』的长征」；
  **e2022-01-26** Q4 2021 Optimus 首获财报会排位：「有潜力比汽车业务更重要」（CNN Business 印证）；
  **e2022-10-19** Q3 2022「比 Apple 与沙特阿美加起来还值钱」（Business Insider 印证，合计约 4.4 万亿美元语境）；
  **e2023-10-18** Q3 2023 Cybertruck「我们给自己挖了坟」+「原型到量产难 10,000%」（TechRadar 印证）；
  **e2024-04-23** Q1 2024 Robotaxi 8/8 之约 + Optimus「年内工厂做有用任务」（Seeking Alpha 印证；8/8 后顺延至 10.10）；
  **e2024-10-23** Q3 2024「全球最有价值公司，遥遥领先」+ Cybercab 2026 量产（Investopedia/Fortune 印证，次日 +22%）；
  **e2025-04-22** Q1 2025「五月起 DOGE 时间大幅减少」（The Hill 印证）；
  **e2026-07-22** Q2 2026「Optimus 会是有史以来最大的产品」+ 里程周增 10%——账本 2026 年首条。
- **quotes.html +10 卡（80→90）**；index.html 计数文案 93→103 ×5；EXPANSION.md 补 R05 入包块（含十场逐字稿链接与甄别注）。
- **管线**：build-ledger-timeline（103 节点）/ build-search-index（断言 93→103，索引 209→219）/ build-epub 重跑。

**质量门**
- verify.py 9 项全绿；来源留档见 V8-PROGRESS.md「核实来源留档（R05）」节。

"""
with io.open("CHANGELOG.md", encoding="utf-8", newline="") as f:
    s = f.read()
marker = "## v7.4.0"
i = s.index(marker)
s = s[:i] + ENTRY + s[i:]
with io.open("CHANGELOG.md", "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("OK CHANGELOG entry inserted")

# ---------- 2) 版本步进 ----------
OLD, NEW = "7.4.0", "7.5.0"

with io.open("VERSION", encoding="utf-8", newline="") as f:
    v = f.read()
assert v.strip() == OLD, v
with io.open("VERSION", "w", encoding="utf-8", newline="") as f:
    f.write(NEW + "\n")
print("OK VERSION", NEW)

with io.open("app.js", encoding="utf-8", newline="") as f:
    a = f.read()
old = "var SITE_VERSION = '%s';" % OLD
assert a.count(old) == 1
a = a.replace(old, "var SITE_VERSION = '%s';" % NEW)
with io.open("app.js", "w", encoding="utf-8", newline="") as f:
    f.write(a)
print("OK app.js SITE_VERSION", NEW)

pat = re.compile(r'(site-version-val">)' + re.escape(OLD) + r'<')
n_total = 0
for p in glob.glob("*.html"):
    with io.open(p, encoding="utf-8", newline="") as f:
        h = f.read()
    n = len(pat.findall(h))
    if n:
        h2 = pat.sub(r"\g<1>" + NEW + "<", h)
        with io.open(p, "w", encoding="utf-8", newline="") as f:
            f.write(h2)
        n_total += n
        print("OK span", p, n)
assert n_total == 14, n_total
print("ALL DONE, spans:", n_total)
