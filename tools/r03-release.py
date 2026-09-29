# -*- coding: utf-8 -*-
"""R03 发布流程：CHANGELOG 记账 → 版本步进（VERSION/app.js/全站 span）。"""
import io, re, glob, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---------- 1) CHANGELOG 记账 ----------
ENTRY = """## v7.3.0 — 2026-09-30 · V8 扩充（3/10）：SEC EDGAR 公文扩容

**主题包成果（V8 R03 · documents.html 9 → 14 份）**
- **五份 SEC EDGAR 一手文书入册（引文全部逐字取自 EDGAR 原文，备案号在册）**：
  **d2018-08-14** Tesla 8-K 私有化特别委员会公告（Item 7.01 + Ex-99.1，0001564590-18-021585）——「尚未收到任何正式提案」，funding secured 一周后的监管口径急刹车；
  **d2022-04-11** Twitter 8-K/A 董事会提名五日始末（0001193125-22-101041）——4.04 邀请、4.09 辞谢、4.11 备案，收购案第一份正式法律文书；
  **d2022-07-26** Twitter DEFM14A（0001193125-22-202163）——4.13 要约信全文（含「My offer is my best and final offer」）+ Background of the Merger 逐日大事记（9.2% 曝光→毒丸→融资承诺→4.24-25 董事会放行）；
  **d2022-10-27** Twitter 最后一份 8-K（0001193125-22-272772）——交割完成、九董事列名离任、「马斯克成为唯一董事」、NYSE 摘牌（Form 25→15 档案定格）；
  **d2024-04-29** Tesla DEF 14A（0001104659-24-053333）——Tornetta 判决后 2018 奖励再批 + 迁州德州双议案（含 2.04/2.10 董事会程序内幕、proxy 引用的马斯克 X 帖与董事长署名信）。
- **交叉引用**：platform-x.html px-0414 补 d2022-04-11/d2022-07-26 两链、px-1028 补 d2022-10-27；promises.html 2018 私有化案 sv-links 与来源列表各补 d2018-08-14；documents.html d2022-04-25 词条补 d2022-07-26 站内链；reading.html「九份一手文档」升「十四份」；doc-path 导读链改写为十四份版（中英双语）。
- **管线**：build-search-index（断言 9→14，索引 194→199）/ build-epub 重跑；账本未动（时间轴/语录卡/EPUB 新鲜度不受影响）。

**质量门**
- verify.py 9 项全绿；来源留档见 V8-PROGRESS.md「核实来源留档（R03）」节（六份 EDGAR 索引页+正文直读，表决结果多源印证）。

"""
with io.open("CHANGELOG.md", encoding="utf-8", newline="") as f:
    s = f.read()
marker = "## v7.2.0"
i = s.index(marker)
s = s[:i] + ENTRY + s[i:]
with io.open("CHANGELOG.md", "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("OK CHANGELOG entry inserted")

# ---------- 2) 版本步进 ----------
OLD, NEW = "7.2.0", "7.3.0"

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

pat = re.compile(r'(site-version-val">)' + re.escape(OLD) + r'(')
n_total = 0
for p in glob.glob("*.html"):
    with io.open(p, encoding="utf-8", newline="") as f:
        h = f.read()
    n = len(pat.findall(h))
    if n:
        h2 = pat.sub(r"\g<1>%s\g<2>" % NEW, h)
        with io.open(p, "w", encoding="utf-8", newline="") as f:
            f.write(h2)
        n_total += n
        print("OK span", p, n)
assert n_total >= 10, n_total
print("ALL DONE, spans:", n_total)
