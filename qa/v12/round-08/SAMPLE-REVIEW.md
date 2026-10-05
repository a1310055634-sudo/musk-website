# V12-20 R08 抽样人工复核记录（10 条）

日期：2026-10-06 · 复核人：自主工程师（机核结果逐条人工判读）

| # | id | 来源组 | 机核 | 人工复核口径 | 结论 |
|---|---|---|---|---|---|
| 1 | e2016-05-04 | earnings-call | 镜像 MISS | WebFetch stockanalysis 23974-q1-2016：逐字句 "The date we are setting with suppliers to get to a volume production capability with the Model 3 is July 1st next year." 完整在稿 | ✅ |
| 2 | e2016-02-10 | earnings-call | 镜像 MISS | WebFetch stockanalysis 23975-q4-2015：逐字句 "We're really looking forward to the unveiling of the Model 3 at the end of next month." 完整在稿 | ✅ |
| 3 | e2013-05-08 | earnings-call | 镜像 MISS | WebFetch stockanalysis 23986-q1-2013：**无此句**；最接近为 "we were profitable at Q1…"——引语实为 2013-05-08 股东信口径（"first time in our ten year history"），非电话会逐字。如实降级 ⚠️，后续可换锚为股东信原件 | ⚠️（口径不符如实记） |
| 4 | e2018-08-01 | earnings-call | 镜像 YES | 镜像 video/tesla-q2-2018-earnings-call-2018-08-01 转录页含中段 6 词子串；镜像 earnings call 转录系镜像站自建库 | ✅ |
| 5 | e2023-10-18 | earnings-call | 镜像 YES | 镜像 video/tesla-q3-2023-earnings-call 同上 | ✅ |
| 6 | e2022-11-16 | other-official | 镜像 YES | 镜像 email/twitter-fork-in-the-road-2022——与文档馆 d2022-11-16 同底本交叉确认（"extremely hardcore" 逐字在册） | ✅ |
| 7 | e2018-08-07 | edgar | EDGAR YES | EDGAR FTS "considering taking tesla…" 命中 8-K 原文（funding secured 备案语境） | ✅ |
| 8 | e2016-07-20 | edgar | EDGAR YES | EDGAR FTS 命中 10-K "major segments" 段 | ✅ |
| 9 | e2022-04-14 | ted.com | 镜像 MISS | ted.com《The future we're building》页 272KB，__NEXT_DATA__ transcript JSON 存在但逐段匹配无 "don't care about the economics" 逐字句（TED 官方分段与站内卡句为节选改排） | ⚠️ |
| 10 | e2018-09-27 | edgar | EDGAR MISS | 引语实为 SEC 起诉状措辞（"Musk knew or was reckless…"）非备案文本；www.sec.gov 页面本机 403（curl 被拦，data.sec.gov API 不适用页面），原文本轮未获 | ⚠️ |

## 复核中发现的系统口径点
1. **earnings-call 组底本口径**：stockanalysis 逐字稿是转录服务（非公司官方稿），与卡句一致性约 2/3 抽样吻合；不吻合处以"股东信/公告口径"为主——该组 ⚠️ 标注的"两源转述一致"成立度如实按抽样记录，未核到的 17 条维持转引在册。
2. **镜像假命中防误**：e2019-02-19 "Tesla made 0 cars in 2011" 镜像命中 Bloomberg Risk Takers (2011-08-15) 系**字串巧合**（年份词撞车），人工判非原文，维持 ⚠️——中段 6 词匹配对含年份数字短语需人工复核。
3. **EDGAR 组的组内异质性**：6 条"edgar"来源中 3 条实为 SEC 起诉状/信件措辞而非备案原文（FTS 天然搜不到），组内 ⚠️ 的原因与 earnings-call 组不同，TSV 分组注明。
4. **账本块 vs 语录卡差 2**：e2021-07（Raptor 破产信）与 e2025（年精度条）只有账本引文块无语录卡——恒等式 107=109−2 的构成项，TSV 照填结论、卡标不适用。
