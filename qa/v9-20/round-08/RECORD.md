# V9-20 R08 工作记录（事件档案聚合扩容：V8/V9 新材料归档，9→14）

- 轮次：R08/20 ｜ 版本：8.7.0 → 8.8.0 ｜ 日期：2026-10-01
- 交付：tools/events-data.py 9 → **14 个事件档案**（材料关联 37 → 59 份，逐字引语 18 → 24 条）+
  events.html / events-data.js / timeline.html / timeline-events.js / search-index.js / primary.html 建档卡全链重生成
- 五个新档案（全部由已入册的账本/文档/X 帖/编年史聚合，零新增未核实事实）：
  - **e2010-06-29 Tesla IPO**（deal）：S-1 商业模式总纲+首份关键人风险因子（d2010-01-29）、
    Q1 2013 首盈利（e2013-05-08）、12 年后 10-K「Technoking」同名风险因子对照（d2022-02-07）。
    账本当日无本人逐字原话——档案如实引 SEC 文件原文并注明「公司文件口径」，未编造引语。
  - **e2021-10-25 万亿市值日**（deal）：账本 e2021-10-25 + p2021-11-02 same margin 帖
    （snowflake 解码 UTC 2021.11.02 01:48 = 美国时间 11.01 晚，与账本「11.01 对冲」同帖双注）+
    chronicle.html#c2021-10-25（**chronicle kind 首次使用**）。
  - **e2021-11-26 Raptor 危机与星舰翻身**（gamble）：d2021-11-26 破产警报信 +
    e2018-09-17 环月承诺 + e2019-09-28 不锈钢转向 + p2021-05-05 SN15 着陆 + e2024-03-18 Starbase 演讲，
    五材料时间线；outcome 如实对照「每两周一飞未兑现（IFT-1 迟至 2023-04-20）/破产未发生/dearMoon 2024 年中取消」。
  - **e2024-01-29 Neuralink 首例人体植入**（milestone）：e2020-08-28 三只小猪 + e2021-04-09 MindPong +
    e2022-11-30「大概六个月」预言 + e2024-01-29 官宣 + p2024-01-29，五材料「预言→兑现」线；
    口径如实：probably in about six months ≠ 承诺书，实际约十四个月。
  - **e2019-04-22 Autonomy Day → Optimus**（milestone）：e2019-04-22 LIDAR doomed +
    e2021-08 AI Day 2021 + e2022-01-26 电话会排位 + e2022-09-30 真机 + promises.html 对账（feature 材料）；
    related 链 controversy.html#autopilot（首个指向争议深读的 related）。
- 枚举扩充：KIND_LABELS 新增 chronicle（编年史条目）——validate() 通过；无 CSS 变更（非 ledger 类型共用默认样式）。
- **口径红线闭环（防 160 漂移重演）**：索引 277 → 282（事件档案断言 len(ED.EVENTS) 自动 9→14）；
  吸收 18 → 39；独立记录 250 → 229；**282 = 14 档案记录 + 39 吸收 + 229 独立**；
  absorbedByEvent：新档案 e2010-06-29=4 / e2021-10-25=3 / e2021-11-26=5 / e2024-01-29=5 / e2019-04-22=4（21 条新吸收）。
- 建档卡关联：primary.html 注入 18 → 23 处（新覆盖 5 个账本条目）。
- 选题边界（留档）：xAI/Grok 线仅 2 条索引材料（e2023-07-12 + p2023-11-04），未达聚合门槛不立档
  （e2025-03-28 已是档案不重复吸收）；Hertz 主题并入万亿市值日档案（单一叙事）；Gamestonk 单材料不立。
- 管线：build-events / build-timeline-events / build-network / build-company-files / build-capital /
  build-ledger-links（23 处）/ build-search-index（282）/ sync-changelog（197 条）/ 版本三件套 8.8.0
  （VERSION + app.js + 14 页 span，替换计数打印在案）/ build-epub（220,559 B，24 章）。
- 验证：verify.py 9/9（37 页/索引 282）；node --check 通过；**CDP 探针 35/35**（tools/v9r08-probe.js：
  文件级口径 11 / events.html 结构与逐字 10 / 互链与深链 4 / timeline 口径 4 / 建档卡 2 / 检索 3 / 390 零溢出 2，
  截图 3 张入本目录）。
- 探针插曲：首跑解析 TIMELINE_V7 meta 用非贪婪正则被 JSON 内部结构截断 → 改 indexOf/lastIndexOf 整体解析；
  records 引用笔误（meta.records → parsed.records）一处；events 卡选择器 .ev-sum → 实构 .ev-summary、
  引语块实构 blockquote.lr-quote（先目检 DOM 再写断言——R07 教训复验）。
  timeline-events.js meta.version 随版本 bump 后重跑刷新为 8.8.0。
- 证据：qa/v9-20/round-08/（probe.txt + 3 张截图：events 新五卡桌面 / timeline 口径桌面 / events 390 定位
  Neuralink 档案）。
- 提交：成果 = 本提交；账本回填+revisions+EPUB 重刷为第二提交。
