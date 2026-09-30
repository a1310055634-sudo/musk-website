# -*- coding: utf-8 -*-
"""V8 R07 backfill: mark R07 complete in V8-PROGRESS.md (status table + archive + work record)."""
import io

P = 'V8-PROGRESS.md'
s = io.open(P, encoding='utf-8', newline='').read()

# 1) status row
old_row = '| 07 | 长访谈 II：Rogan / TED / All-In / DealBook | in_progress | — | — | — |'
new_row = '| 07 | 长访谈 II：Rogan / TED / All-In / DealBook | complete | v7.7.0 | d5513cf | pending-push |'
assert s.count(old_row) == 1, 'status row not found'
s = s.replace(old_row, new_row)

ARCHIVE = """## 核实来源留档（R07）

七场访谈（逐字稿可得性分层；日期锚以官方库为准）：
- **TED 2017**（场次 2017-04-28，Vancouver）：https://www.ted.com/talks/elon_musk_the_future_we_re_building_and_boring （官方逐字稿内嵌页面 JSON `\"transcript\"` 字段）；场次日期=TED Blog 2017-04-28 口径——ted.com 结构化元数据 recordedOn=2017-04-24 为大会开幕日占位，不采
- **JRE #1169**（2018-09-07，jrelibrary.com/1169-elon-musk/ 官方日期锚）：英文全文逐字稿六分册 https://elonmuskinterviews.wordpress.com/2021/01/25/the-joe-rogan-experience-1169-elon-musk-i-english/ （II=2021/01/28、III=2021/02/03、IV=2021/02/09、V=2021/02/24，含时间戳；开篇自述「broadcast live and published on YouTube on 2018-09-07」）； weed 后续=Guardian/CNBC/WaPo/BBC 2018-09-07 同日报道（Guardian 站点本机不可达，四家报道事实经检索摘要两源核对，未直验 URL）；#1169 为 JRE 观看量最高一期（jrelibrary 统计）
- **JRE #1470**（2020-05-07，jrelibrary.com/1470-elon-musk/）：**Rev.com 官方逐字稿** https://www.rev.com/blog/transcripts/joe-rogan-elon-musk-podcast-transcript-may-7-2020 （curl 直读，436KB，时间戳定位 55:30/57:21/01:04/01:46/13:45）；疫情段印证=CNBC 2020-05-07 https://www.cnbc.com/2020/05/07/elon-musk-says-coronavirus-pandemic-is-practice-run-for-future-viruses.html （已直验 200）+ Media Matters 逐条批驳文；卖房背景=2020-05-01 推文（媒体广泛报道）
- **TED 2022·Giga Texas**（2022-04-06 录制，开幕前夜）：https://www.ted.com/talks/elon_musk_a_future_worth_getting_excited_about （官方逐字稿内嵌 JSON；CA 开场句「the day before this thing opens」为日期内证）+ energynow.ca 转载页；4 月中旬上线
- **JRE #2223**（2024-11-04，jrelibrary.com/2223-elon-musk/）：Musixmatch 逐字稿（podcasts.musixmatch.com，02:08:21 段，本机直连不可达，逐字以检索快照核对）+ Mediaite 2024-11-05（「Joe Rogan, Musk Say This Is 'Last Election' If Trump Loses」）+ The Spectator 2024-11-04（罗根背书帖「If it wasn't for him we'd be fucked」）——三家转写措辞有出入，条目取一致核心句并如实注明
- 通用：podscript.ai 仅收 Lex 系（无 JRE）；Happy Scribe 全站 403（curl/WebFetch 均）；podscripts.co/singjupost/jrescribe/mediawiki 本机均连不通；r.jina.ai 代理被 DNS 污染（解析到 Facebook IP）不可用
- **甄别记录（宁缺毋滥）**：①All-In Summit 2024（2024-09-09 LA，podcastnotes.org 笔记在档：DMV at scale/paper vs rocket 等直引）——「The government is the DMV at scale」句 Yahoo Finance 系于 9/1（峰会前一周）场合存疑，无第二媒体直引，弃收；②JRE #2054（2023-10-31）逐字稿全不可达，podcastnotes 单源、媒体仅转述「extinctionist」段，弃收——「slowest and least lucky」句为 2015/2017/2025 多场合惯用语，不宜绑定期次；③DealBook 2023「Go f*** themselves」+「advertisers killed the company」已在册 i2023-11-29，不重复；年级 ID i2023/月份级 i2023-11 均已被占，DealBook 二条目在现行 ID 惯例下无法命名（新后缀方案会破坏前缀规范，不做）；④**「If he loses, I'm fucked / How long do you think my prison sentence is going to be?」出自 Tucker Carlson 访谈（2024-10-07，Guardian/Gizmodo 报道）而非 JRE #2223**——常见误引，已核实记录；⑤JRE #1601（2021-01-26）为 Brian Redban 场，「马斯克 2021 年上过 Rogan」不实；⑥TED 2022 的 Twitter 问答集中在 4/14 温哥华场（已在册），4/6 场仅一句 limbic 系玩笑，无重复风险

"""

RECORD = """## 第 7 轮工作记录（长访谈 II：Rogan / TED / DealBook）— complete（2026-09-30）

- **交付**：interviews.html +7 条（26→33，严格克隆 `<article class="iv-item" id="i…">` 六件套模板，四段式双语）：i2017-04-28（TED 2017「最摧残灵魂的东西，是堵车」+「It's maybe two or three percent」爱好自陈 + 隧道深于楼高论证）、i2018-09-07（JRE #1169 大麻卷烟时刻，joint/cigar 问答 +「Alcohol is a drug that's been grandfathered in」，互链 e2018-08-07/e2018-09-27）、i2018-09（JRE #1169「AI 一定会被用作武器」+「超出人类控制」+ 风险排序句，互链 ai-strategy.html）、i2020-05-07（JRE #1470「文明现在看起来很脆弱」+「What's that? I never heard of it.」+ practice 论，互链 e2020-05-11）、i2020-05（JRE #1470「Mars or a house? I'm like Mars.」+ Boca Chica 小房子）、i2022-04-06（TED Giga Texas「人口崩溃是文明最大的威胁之一」+ curiosity/consciousness 自述，互链 i2022-04-14）、i2024-11-04（JRE #2223「If Trump doesn't win, this is the last election.」，转写出入如实注明）。
- **期数/日期勘定**：JRE #1169=2018-09-07、#1470=2020-05-07、#2223=2024-11-04（jrelibrary 官方口径）；TED 2017 场次=2017-04-28（TED Blog 口径，meta recordedOn=04-24 为占位）；同月第二条沿用月份级 ID 先例（i2018-09、i2020-05），与 R06 惯例一致。
- **管线**：build-search-index（断言 26→33，索引 227→234 = 103+14+33+13+5+53+4+9）/ sync-changelog（186 条）/ build-epub（188,201 B，24 章）；版本 v7.6.0→v7.7.0（VERSION/app.js/14 页 span，node --check app.js cite.js 通过）；CHANGELOG 首条 v7.7.0；EXPANSION.md 顶部补 R07 入包块。提交后 build-revisions + EPUB 重刷为第二个提交。
- **验证**：verify.py 9/9 全绿（37 页，索引 234；账本未动故未跑 build-ledger-timeline——访谈不进时间轴，语录卡 90 不变——访谈页不进语录卡白名单口径不变）。
- **提交**：主成果 `d5513cf`（28 文件，+401/−19）；本回填+revisions/EPUB 刷新为第二个提交。
- **实现备注**：①集成断言两处口径修正：`<article class="iv-item"` 原始标签 27（含一条无 id 的 legacy 名句条目「I would like to die on Mars」）vs 带 id 条目 26——断言必须分层（27→34 原始 / 26→33 可索引）；②r07-integrate.py 复用「片段文件+锚前插+唯一性断言」修好版模式，CRLF 归一一次通过；③CHANGELOG 为 CRLF、EXPANSION 为 LF——两文件行尾不同，插入时分别归一（新坑：此前默认全库 CRLF 不成立）。
- **采料环境备注**：本轮站点可达性明显恶化（GitHub/Wikipedia/Guardian/singjupost/podscripts.co/jrescribe/musixmatch 本机直连全败，Wikipedia 解析被 DNS 污染到 Facebook IP，r.jina.ai 同样被污染）——逐字稿主要靠 wordpress 自架站、rev.com、ted.com 三路可直连源；「媒体两源」多处退化为检索摘要核对（已逐条如实标注），若后续轮次需要更硬的媒体直验，建议网络可达窗口补验。
- **下一轮预告**：R08 X 帖史扩容（x-posts.html +10~12 条：收购宣言/裁员公告/改名 X/重大产品宣布；已删帖用 Wayback 快照核对——注意 web.archive.org 本机 TLS 中断不可用，需改用 elonmuskarchive.org 等镜像源；musk-website-verified-facts 记忆档需先查重）。

"""

ANCHOR_ARCHIVE = '## 核实来源留档（R06）'
assert s.count(ANCHOR_ARCHIVE) == 1
s = s.replace(ANCHOR_ARCHIVE, ARCHIVE + ANCHOR_ARCHIVE, 1)

ANCHOR_RECORD = '## 核实来源留档（R06）'
assert s.count(ANCHOR_RECORD) == 1
s = s.replace(ANCHOR_RECORD, RECORD + ANCHOR_RECORD, 1)

io.open(P, 'w', encoding='utf-8', newline='').write(s)
print('V8-PROGRESS.md backfilled: R07 complete (d5513cf), archive + record inserted')
