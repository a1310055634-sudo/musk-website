# -*- coding: utf-8 -*-
"""V8 R07: prepend CHANGELOG.md v7.7.0 entry (CRLF) and EXPANSION.md R07 block (LF)."""
import io

CHANGELOG_ENTRY = """## v7.7.0 — 2026-09-30 · V8 扩充（7/10）：长访谈 II · Rogan / TED / DealBook

**主题包成果（V8 R07 · interviews.html 26 → 33 条）**
- **七条长访谈条目入册（引语逐字取自逐字稿或官方转录，关键处两源印证）**：
  **i2017-04-28** TED 2017 温哥华「最摧残灵魂的东西，是堵车」+「It's maybe two or three percent」的爱好自陈（ted.com 官方逐字稿）；
  **i2018-09-07** JRE #1169 大麻卷烟时刻——次日 Guardian/CNBC 报道股价跌约 6%、两位高管辞职，六周后 SEC 起诉（互链 e2018-08-07 / e2018-09-27）；
  **i2018-09** JRE #1169「AI 一定会被用作武器」+「超出人类控制」（全文逐字稿在档，互链 AI 战略布局）；
  **i2020-05-07** JRE #1470「文明现在看起来很脆弱」+「What's that? I never heard of it.」疫情冷面段（Rev.com 官方逐字稿，互链 e2020-05-11）；
  **i2020-05** JRE #1470「Mars or a house? I'm like Mars.」——卖房宣言的时间经济学（Rev.com 官方逐字稿）；
  **i2022-04-06** TED Giga Texas 开幕前夜「人口崩溃是文明最大的威胁之一」+ curiosity/consciousness 动机自述（ted.com 官方逐字稿，互链 i2022-04-14）；
  **i2024-11-04** JRE #2223 大选前夜「If Trump doesn't win, this is the last election.」——多家转写出入如实注明（Musixmatch 逐字稿 + Mediaite/The Spectator 记录）。
- **检索索引 227 → 234 条**（访谈 26→33）；期数/日期勘定：JRE #1169=2018-09-07、#1470=2020-05-07、#2223=2024-11-04（jrelibrary 官方口径）；TED 2017 场次=2017-04-28（TED Blog）。
- **甄别记录（宁缺毋滥）**：All-In Summit 2024（2024-09-09 LA）无第二媒体直引源，弃收；JRE #2054（2023-10-31）逐字稿不可达且媒体仅转述，弃收；DealBook 2023「滚蛋」名句已在册 i2023-11-29；「I'm fucked / 监狱刑期」名句出自 Tucker Carlson 访谈（2024-10-07）而非 Rogan，已记录防止误引。

**自主优化**
- 工具脚本 tools/r07-snippet.html + tools/r07-integrate.py（唯一性断言 + CRLF 统一）+ tools/r07-spans.py（版本步进断言 14）。

**质量门**
- verify.py 9 项全绿（37 页，索引 234）；node --check（app.js + cite.js）通过；EPUB 重跑含最新条目。
"""

EXPANSION_ENTRY = """> **新事实入包（V8 R07 轮 / 2026-09-30 长访谈 II 逐字稿核实）**：访谈页 +7 条（26→33）——JRE 两期 + TED 两场 + JRE 大选期。逐字稿可得性：JRE #1169 全文英文逐字稿六分册（elonmuskinterviews.wordpress.com 2021/01/25-2021/02/24，含时间戳）、JRE #1470 Rev.com 官方逐字稿（rev.com/blog/transcripts/joe-rogan-elon-musk-podcast-transcript-may-7-2020）、TED 两场为 ted.com 官方页内嵌逐字稿（页面 JSON 字段）、JRE #2223 Musixmatch 逐字稿。日期锚：jrelibrary.com/1169-elon-musk/（2018-09-07）、/1470-elon-musk/（2020-05-07）、/2223-elon-musk/（2024-11-04）；TED 2017 场次 2017-04-28（TED Blog 口径，ted.com 结构化元数据 recordedOn=04-24 为大会开幕日占位，不采）。七条锚点与印证源：
> - **i2017-04-28**「soul-destroying traffic」+「two or three percent」爱好自陈 + 隧道深于楼高论证：ted.com 官方逐字稿（the future we're building — and boring）。
> - **i2018-09-07** 大麻卷烟时刻（joint/cigar 问答 +「Alcohol is a drug that's been grandfathered in」）： wordpress 六分册逐字稿 02:10:00 段；次日股价 -6% 与 Dave Morton/Gabrielle Toledano 辞职=Guardian/CNBC/WaPo/BBC 2018-09-07 同日报道（Guardian 站点本机不可达，四家报道事实经检索摘要两源核对）；#1169 为 JRE 观看量最高一期（jrelibrary 统计）。
> - **i2018-09**「tempting to use A.I. as a weapon. In fact, it will be used as a weapon.」+「outside of human control」+ 风险排序句：wordpress 逐字稿第一分册（AI 段）。
> - **i2020-05-07**「assuming civilization is still around, it's looking fragile right now.」+「What's that? I never heard of it.」+「practice」论 +「rapidly moving towards opening up」：Rev.com 官方逐字稿（55:30 / 57:21 / 01:04 段）+ CNBC 2020-05-07（cnbc.com/2020/05/07/elon-musk-says-coronavirus-pandemic-is-practice-run-for-future-viruses.html，已直验 200）+ Media Matters 记录。
> - **i2020-05**「Like what's more important? Mars or a house? I'm like Mars.」+ Boca Chica 小房子（01:46 段）：Rev.com 逐字稿；背景=2020-05-01「卖掉几乎所有有形财产」推文（媒体广泛报道）。
> - **i2022-04-06**「Population collapse is one of the biggest threats to the future of human civilization.」+「I've been motivated by curiosity more than anything.」+「We must expand the scope and scale of consciousness.」：ted.com 官方逐字稿（a future worth getting excited about；CA 开场句「the day before this thing opens」锚定 2022-04-06 Giga Texas 开幕前夜，energynow.ca 转载印证）。
> - **i2024-11-04**「I think this was the last election. If Trump doesn't win, this is the last election.」：Musixmatch 逐字稿（02:08:21 段）+ Mediaite 2024-11-05 + The Spectator 2024-11-04——三家措辞有出入（转写差异），条目取一致核心句并如实注明；罗根当晚背书帖「If it wasn't for him we'd be fucked」同源记录。
> 甄别记录（宁缺毋滥）：①All-In Summit 2024（2024-09-09，LA；podcastnotes.org 笔记在档：DMV at scale / paper vs rocket 等直引）——「DMV at scale」句 Yahoo Finance 系于 9 月 1 日（峰会前一周）场合存疑，单源不可立条，弃收；happyscribe 逐字稿存在但本机 403 不可核。②JRE #2054（2023-10-31）podscript/jrescribe/podscripts.co 均不可达，podcastnotes 直引单源，媒体（Daily Mail/Yahoo）仅转述「extinctionist」段——弃收；「slowest and least lucky」句为 2015/2017/2025 多场合惯用语，不宜绑定期次。③DealBook 2023「Go f*** themselves」名句已在册 i2023-11-29，不重复立条。④「If he loses, I'm fucked / How long do you think my prison sentence is going to be?」出自 Tucker Carlson 访谈（2024-10-07，Guardian/Gizmodo 报道）而非 JRE #2223——两处不可混淆，已核实记录。⑤JRE #1601（2021-01-26）为 Brian Redban 场，网传「马斯克 2021 年上过 Rogan」不实。

"""

# --- CHANGELOG (CRLF) ---
s = io.open('CHANGELOG.md', encoding='utf-8', newline='').read()
assert s.count('## v7.6.0') == 1 and '## v7.7.0' not in s, 'changelog state unexpected'
anchor = '## v7.6.0'
entry = CHANGELOG_ENTRY.replace('\n', '\r\n')
s2 = s.replace(anchor, entry + anchor, 1)
assert s2 != s and s2.count('## v7.7.0') == 1
io.open('CHANGELOG.md', 'w', encoding='utf-8', newline='').write(s2)
print('CHANGELOG.md: v7.7.0 entry prepended')

# --- EXPANSION (LF) ---
e = io.open('EXPANSION.md', encoding='utf-8', newline='').read()
marker = '> **新事实入包（V8 R06 轮'
assert e.count(marker) == 1 and 'V8 R07 轮' not in e, 'expansion state unexpected'
e2 = e.replace(marker, EXPANSION_ENTRY.rstrip('\n') + '\n\n' + marker, 1)
assert e2.count('V8 R07 轮') == 1
io.open('EXPANSION.md', 'w', encoding='utf-8', newline='').write(e2)
print('EXPANSION.md: R07 block prepended')
