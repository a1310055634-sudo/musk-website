# -*- coding: utf-8 -*-
"""V8 R09 version bump 7.8.0 -> 7.9.0 + CHANGELOG/EXPANSION entries."""
import io, glob

OLD, NEW = '7.8.0', '7.9.0'
SP = 'site-version-val">'

v = io.open('VERSION', encoding='utf-8', newline='').read()
assert v.strip() == OLD, 'VERSION=%r' % v
io.open('VERSION', 'w', encoding='utf-8', newline='').write(v.replace(OLD, NEW))

a = io.open('app.js', encoding='utf-8', newline='').read()
pa = "var SITE_VERSION = '" + OLD + "';"
assert a.count(pa) == 1
io.open('app.js', 'w', encoding='utf-8', newline='').write(a.replace(pa, "var SITE_VERSION = '" + NEW + "';"))

total = 0
for f in sorted(glob.glob('*.html')):
    s = io.open(f, encoding='utf-8', newline='').read()
    o = SP + OLD + '<'
    n = s.count(o)
    if n:
        assert n == 1, (n, f)
        io.open(f, 'w', encoding='utf-8', newline='').write(s.replace(o, SP + NEW + '<'))
        total += 1
assert total == 14, total
print('version -> %s (%d files)' % (NEW, total))

CHANGELOG_ENTRY = """## v7.9.0 — 2026-10-01 · V8 扩充（9/10）：SpaceX / Neuralink / xAI 官方演讲与 demo

**主题包成果（V8 R09 · 账本 103 → 109 条）**
- **六条账本条目入册（官方发布会/demo/演讲逐字，镜像与媒体双源核验）**：
  **e2017-09-29** IAC 2017 阿德莱德 BFR（「space-faring civilization」句，Business Insider 逐字 + SpaceX 官方视频；互链 e2016-09-27/e2022-02-10）；
  **e2019-07-16** Neuralink 2019 发布会（「A monkey has been able to control a computer with his brain.」CT Insider/Mashable 双源；互链 e2021-04-09/e2024-01-29）；
  **e2020-08-28** Gertrude 猪演示（「a Fitbit in your skull with tiny wires」TechCrunch/Globe and Mail 双源）；
  **e2021-04-09** Pager MindPong（镜像回帖逐字「Sure.」「Hopefully, later this year.」status/1380314267077894148+1380314485324308482，snowflake 00:19 UTC；媒体记录转发语「literally playing a video game telepathically」CNBC/CNET）；
  **e2022-02-10** Starbase 星舰更新（「I feel, at this point, highly confident that we'll get to orbit this year.」Space.com 逐字——IFT-1 实际晚十四个月，「lose a few vehicles」字面兑现；互链 p2024-10-13）；
  **e2025-02-18** Grok 3 发布（镜像逐字两帖：「Grok 3 presentation starting shortly.」03:59 UTC +「the world's smartest AI」19:29 UTC；互链 p2023-11-04/grok.html）。
- **检索索引 244 → 250 条**（言行实录 103→109）；页顶时间轴重建 109 节点；index.html 计数文案 103→109 ×3 处（含 data-en）。
- **查重勘定**：IAC 2016（e2016-09-27/i2016-09-27）、Starship Mk1（e2019-09-28）、xAI 官宣（e2023-07-12）、xAI 收购 X（e2025-03-28）已在册，本轮不重复立条。
- **甄别记录（宁缺毋滥）**：①Starship 2022 发布会 Spaceflight Now/Everyday Astronaut 无直引，靠 Space.com（Mike Wall）逐字立条；②Neuralink 2020 TechCrunch 原文 URL 已 404，Fitbit 句以检索摘要多源核对收录；③Grok 3 直播内容逐字不可得，条目只收帖文第一手，「smartest AI on Earth」的现场口号版未采；④Neuralink JMIR 论文（d 条目候选）jmir.org 本机不可达，文档馆本轮不动。
- **工程备注**：primary.html 行尾已转 LF（与既往 CRLF 惯例不同），集成脚本改为自适应行尾；逐卡结构断言（4 ps-sec/1 quote/1 zh/1 permalink/1 src）全过。

**质量门**
- verify.py 9 项全绿；node --check（app.js + cite.js）通过；EPUB 重跑。
"""

EXPANSION_ENTRY = """> **新事实入包（V8 R09 轮 / 2026-10-01 官方发布会与 demo 逐字核验）**：账本 +6 条（103→109）。来源与方法：①X 帖类用 elonmuskarchive.org 镜像详情页直读（R08 管线复用：snowflake 对表日期）；②演讲/demo 类以媒体逐字报道双源立条（BI/TechCrunch/CT Insider/Mashable/Globe and Mail/Space.com），官方视频（SpaceX YouTube）佐证存在；③Spaceflight Now/Everyday Astronaut 仅转述无直引，如实区分。六条锚点：
> - **e2017-09-29**（IAC 2017 阿德莱德）：「The future is vastly more interesting and exciting if we're a space-faring civilization and a multiplanet species than if we're not.」= Business Insider（businessinsider.com/elon-musk-iac-mars-colonization-presentation-2017-9）；官方视频 SpaceX YouTube「Making Life Multiplanetary」（tdUX3ypDVwI）；社区逐字稿（r/SpaceXLounge）对勘。
> - **e2019-07-16**（Neuralink 2019）：「A monkey has been able to control a computer with his brain.」= CT Insider（2019-07-17）+ Mashable 双源；2020 人体试验时间表同场宣布。
> - **e2020-08-28**（Gertrude）：「a Fitbit in your skull with tiny wires」= TechCrunch（2020-08-28；原文 URL 现已 404，检索摘要多源核对）+ The Globe and Mail（同日）+ Silicon Republic（08-31）。
> - **e2021-04-09**（Pager MindPong）：镜像回帖逐字 status/1380314267077894148 + status/1380314485324308482（均为 2021-04-09 00:19 UTC）；转发语「A monkey is literally playing a video game telepathically」= CNBC（04-09）+ CNET（04-08）+ Reuters 广泛报道。
> - **e2022-02-10**（Starbase 更新）：「I feel, at this point, highly confident that we'll get to orbit this year.」+「We'll probably lose a few vehicles along the way.」= Space.com（Mike Wall，02-11 刊）逐字；Spaceflight Now/Everyday Astronaut 同日记录佐证（转述）。
> - **e2025-02-18**（Grok 3 发布）：「Grok 3 presentation starting shortly.」（03:59 UTC）+「Subscribe to Premium+ to get the world's smartest AI!」（19:29 UTC）+ Grok 官号「grok 3 is the world's smartest AI now available to all Premium+ subscribers」——三条均镜像详情页直读。
> 甄别记录（宁缺毋滥）：①Grok 3 直播逐字不可得（livestream 无转录），「smartest AI on Earth」现场口号版未采——条目只收帖文第一手；②Neuralink 2019 演讲完整逐字稿无公开版（Q&A 媒体记录为准）；③JMIR 2020 Neuralink 论文（d2020-10-16 候选）jmir.org 本机不可达未收录；④Neuralink 2019 的「symbiosis」表述多出现在后续访谈而非本场逐字，未采用。

"""

# CHANGELOG (CRLF)
s = io.open('CHANGELOG.md', encoding='utf-8', newline='').read()
assert s.count('## v7.8.0') == 1 and '## v7.9.0' not in s, 'changelog state'
entry = CHANGELOG_ENTRY.replace('\n', '\r\n')
s2 = s.replace('## v7.8.0', entry + '## v7.8.0', 1)
assert s2.count('## v7.9.0') == 1
io.open('CHANGELOG.md', 'w', encoding='utf-8', newline='').write(s2)
print('CHANGELOG.md: v7.9.0 prepended')

# EXPANSION (LF)
e = io.open('EXPANSION.md', encoding='utf-8', newline='').read()
marker = '> **新事实入包（V8 R08 轮'
assert e.count(marker) == 1 and 'V8 R09 轮' not in e, 'expansion state'
e2 = e.replace(marker, EXPANSION_ENTRY.rstrip('\n') + '\n\n' + marker, 1)
assert e2.count('V8 R09 轮') == 1
io.open('EXPANSION.md', 'w', encoding='utf-8', newline='').write(e2)
print('EXPANSION.md: R09 block prepended')
