# V9-20 R04 QA 记录 — 访谈扩充 I（v8.4.0，2026-10-01）

## 本轮范围
计划 R04：访谈扩充 I，目标 +4~6 条（33→37~39）。实际 +4 条，全部以 elonmuskarchive.org interview 类型库官方转写为逐字锚。

## 立条清单与来源锚
| 条目 | 镜像 transcript id | 字符数 | 引语核心 | 印证 |
|---|---|---|---|---|
| i2016-06-01 Code Conference | code-conference-2016-06-01 | 77,161 | one in billions chance…base reality / 两个选项句 | 本人推文 x-738470842695176192（snowflake 2016-06-02 20:42 UTC） |
| i2020-03-09 SATELLITE 2020 | satellite-2020-keynote-2020-03-09 | 34,957 | Zero impact whatsoever…Zero / fully and rapidly reusable rocket | Business Insider 当日报道（双源） |
| i2021-07-30 EA 星舰基地巡礼 | starbase-tour-…-part-1/2/202 + part-3 | 43,454+53,306+16,836 | a factory is underrated… / 五步算法完整版 | EA 官网文章（2021-08-11，编辑版引语，差异已注明） |
| i2024-09-08 All-In Summit | all-in-summit-2024-musk | 53,865 | The government is the DMV at scale | V8 R07 弃收件重验入册（原单源→现双源） |

- transcript 全文证据：sources/（6+1 个 .json+.txt，含 recode-decode 弃收证据）。
- 镜像 interview 库全量清单（161 场）：interviews-all.json（R05 候选池）。

## 甄别与弃收（宁缺毋滥）
- **Kara Swisher Recode Decode 2018-11-02 弃收**：镜像转写为主播事后复盘（全程间接转述无本人逐字）；Vox 官方全文稿 vox.com 超时 / recode.net 500 / web.archive.org 超时，三路不可得。重验条件已写入 EXPANSION.md。证据：sources/recode-decode-with-kara-swisher-2018-11-02.txt。
- Code 2016 转写为字幕平面化（口吃从略、标点编者所加），卡内注明。
- EA 措辞两版（镜像 a factory is underrated vs EA 官网 manufacturing is underrated），以镜像为准。
- All-In 日期口径：镜像锚 2024-09-08（EXPANSION 旧记 09-09），卡内注明。

## 验证结论
- 静态断言：iv-item 38（37 带 id）/ 新卡六件套 4×（blockquote/iv-zh/ctx/after/permalink 各 1）/ 全页 #i… 锚零缺失 / id 唯一。
- verify.py **9/9**（37 页 / 索引 262 = 109+14+37+31+5+53+4+9 / EPUB 新鲜度过）。
- node --check：app.js 与 tools/v9r04-probe.js 均过。
- **CDP 探针 29/29**（tools/v9r04-probe.js，端口 9335 全新 user-data-dir）：索引文件级 6 断言 / 桌面 1440×900 结构+逐字+双语+互链 15 断言 / 检索命中 4 断言（DMV→i2024-09-08、billions→i2016-06-01、存量 blackmail 回归）/ 390×844 零溢出+新卡无内部溢出。
- 版本三件套：VERSION / app.js SITE_VERSION / 14 页 span → 8.4.0（替换计数打印：14 处/14 页）。
- 生成器：build-search-index（断言 33→37）重跑；sync-changelog（193 条）；build-epub（207,570 B / 24 章）。
- 附带增强：索引器访谈 ctx 正则放宽兼容 data-en 版式，17 张卡 bg 字段补全（CHANGELOG 已注明理由，q/s/bg 口径不变）。

## 截图
- before-desktop-firstview.png（=上轮收官 33f5b2c 状态，git worktree 独立服务 8767 截取）
- after-desktop-firstview.png / after-i2016-06-01.png / after-i2020-03-09.png / after-i2021-07-30.png / after-i2024-09-08.png（1440×900，CDP scrollIntoView 定位）
- after-390-i2021-07-30.png（390×844）

## 提交
- 成果提交：见 git log `[V9-20 R04]`（纯本地，不推送）。
- 第二提交：build-revisions + EPUB 重刷 + 本账本回填。
