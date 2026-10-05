# V12-20 R11 验收 · 编年史补齐 + deep-dive-06 新页（v11.12.0）

日期：2026-10-07 · 模式：纯本地（无 push/remote 写）

## 成果
1. **chronicle.html +11 条（53→64）**：tesla 7（2023-03-01 Investor Day MP3/2023-05-15 SolarCity 终审/2023-10-18 Q3+Cybertruck 倒计时/2024-10-10 We,Robot/2025-06-22 Robotaxi 首发/2025-09-17 万亿薪酬包 proxy/2026-07 Optimus 产线）+spacex 2（2024-03-18 Starbase 员工会/**2026-06-12 SpaceX IPO 定价**）+x 2（2023-11-29 DealBook/2024-07 政治参与升级）。全部克隆 cy-year/cy-ev 结构、逐条带站内深链。
2. **deep-dive-06.html《xAI 三年志》**（17.7KB）：逐字克隆 deep-dive-05 全部结构（head/masthead/lr-hero/五 lr-sec/lr-foot/TOC/进度条/版本 span），公司志读法五章——一句话章程/四个月出 Grok/收购 X/第一份成绩单/资本线与披露缺位；引语全部一手锚。

## 七件接入（缺一不可）
①site-nav.py NAV_GROUPS 注册+全站重注入 40/40（头注释五组 39 页）；②build-search-index.py 新类型「深读长文」五章入索引+编年史断言 53→64；③verify.py 锚点计数加 n_dd（同事件档案先例，页数 38→39 由 glob 自动）；④新页含 site-version-val span——**站点 span 15→16，bump 断言同步**；⑤sitemap.xml 未动；⑥build-longread 幂等跳过（0/5 迁移）；⑦互链 7 处全 fetch 验证（primary×3/x-posts×2/documents/events）。

## 验证
- verify.py 9/9（终态：版本一致 11.12.0/索引 403=124+37+51+44+5+64+4+20+49/语录卡/时间轴/修订/CHANGELOG/EPUB）。
- **CDP 探针 20/20**（端口 9357）：文件级 5/新页渲染 7（含 aria-current 导航高亮/双语/TOC）/互链跨页 fetch 4/chronicle 2/390 双页零溢出。
- QA 截图 2 张：desktop-dd06.png / desktop-chronicle-spcx.png。

## 工程记录（如实）
- dd05 克隆源本身无 site-version-val span（不在 15 span 名单）——任务书④要求新页必须含，故在 lr-meta Updated 行补 span，站点 span 口径 15→16。
- dd06 索引条目 id 初版用页名无页面锚→verify 锚点差 1；改按五章 s1-s5 各录一条（id=页内真实锚，索引 +5），verify 加 n_dd 计数后两侧同步 403。
- Neuralink 无对应公司段弃收（EXPANSION 记档）。

## 版本
- 11.11.0 → 11.12.0（16 span）。
