# -*- coding: utf-8 -*-
"""R6 一次性整合：interviews.html +8 条 Lex Fridman 访谈 + promises/ai-strategy 交叉引用。

教训继承（r04/r05）：replace 的 new 必须以新内容开头、以 anchor 拼回结尾；
工作区文件 CRLF，插入前把片段行尾统一成与目标一致；所有 replace 前先做唯一性断言。
"""
import io

def load(p):
    return io.open(p, encoding="utf-8", newline="").read()

def save(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)

def sub1(s, anchor, addition, tag):
    n = s.count(anchor)
    assert n == 1, f"{tag}: anchor 出现 {n} 次（应为 1）：{anchor[:60]!r}"
    i = s.find(anchor)
    # addition 插在 anchor 之前；若 addition 有行，需与上下文行尾一致（CRLF 由调用方处理）
    return s[:i] + addition + s[i:]

# ---------- 1) interviews.html ----------
P = "interviews.html"
s = load(P)
snippet = io.open("tools/r06-snippet.html", encoding="utf-8", newline="").read()
if "\r\n" in s:
    snippet = snippet.replace("\r\n", "\n").replace("\n", "\r\n")
anchor = '<p class="iv-foot"'
assert s.count(anchor) == 1, f"iv-foot 锚点出现 {s.count(anchor)} 次"
NEW_IDS = ["i2019-04-12", "i2019-04", "i2019-11-12", "i2019-11",
           "i2021-12-28", "i2021-12", "i2023-11-10", "i2023-11"]
for nid in NEW_IDS:
    assert f'id="{nid}"' not in s, f"{nid} 已存在于页面，拒绝重复插入"
assert snippet.count('<article class="iv-item"') == 8, "片段应为 8 条"
s = s.replace(anchor, snippet + anchor)
n_after = s.count('<article class="iv-item" id="i')
assert n_after == 26, f"插入后带 id 的 iv-item 应为 26，实际 {n_after}"
for nid in NEW_IDS:
    assert s.count(f'id="{nid}"') == 1, f"{nid} 插入异常"
save(P, s)
print(f"✓ interviews.html +8 条（18→26）")

# ---------- 2) promises.html 交叉引用 ----------
P = "promises.html"
s = load(P)
CRLF = "\r\n" if "\r\n" in s else "\n"

en_anchor = 'it claims nothing beyond what the five cases above show.">'
en_add = ' In the 2023 Lex Fridman interview he named the pattern himself: “pathologically optimistic on schedule” (interviews i2023-11-10).">'
zh_anchor = '这句话是本档案唯一的概括，且不主张任何超出上述五案的内容。</span>'
zh_add = '2023 年的 Lex Fridman 访谈里，他本人给这个模式起了名字：「病态乐观」——<a href="interviews.html#i2023-11-10">访谈 i2023-11-10</a>。</span>'
s = sub1(s, en_anchor, en_add, "promises-en")
s = sub1(s, zh_anchor, zh_add, "promises-zh")

li_anchor = '<li><a href="primary.html#e2025-11-06">账本 e2025-11-06</a><span data-en="Package approved; the Optimus speech">方案获批；Optimus 演讲</span></li>'
li_add = li_anchor + CRLF + '        <li><a href="interviews.html#i2023-11-10">访谈 i2023-11-10</a><span data-en="“Pathologically optimistic on schedule” — his own naming of the pattern">「病态乐观」——他对该模式的当众自认</span></li>'
s = sub1(s, li_anchor, li_add, "promises-li")
save(P, s)
print("✓ promises.html 交叉引用 ×3（s4 注 + s5 清单）")

# ---------- 3) ai-strategy.html 交叉引用 ----------
P = "ai-strategy.html"
s = load(P)
en_anchor = 'runs through every move on this page.">'
en_add = ' In the 2023 Lex Fridman interview he dated the origin earlier still: OpenAI, he said, grew out of his AI-safety arguments with Larry Page — “what team are you on, Larry?” (interviews i2023-11).">'
zh_anchor = '贯穿本页每一次动作。</p>'
zh_add = '2023 年的 Lex Fridman 访谈把这个起点推得更早：他说 OpenAI 正是与 Larry Page 那场「你站在哪一队」争吵的产物——<a href="interviews.html#i2023-11">访谈 i2023-11</a>。</p>'
s = sub1(s, en_anchor, en_add, "ai-en")
s = sub1(s, zh_anchor, zh_add, "ai-zh")
save(P, s)
print("✓ ai-strategy.html 交叉引用 ×2（捐资者岁月）")

print("R06 整合完成")
