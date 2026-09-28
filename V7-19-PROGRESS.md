# V7-19 计划进度记录

> 「马斯克商业志 MUSK, INC.」v7.0 升级计划（全新 19 轮，2026-09-29 启动）。
> 本文件是本计划的唯一轮次账本；与 git 提交记录相互核验，不以提交总数推算轮次。
> 历史计划（17 轮冲刺，v5.89→v6.5.0）已完结，不继承其计数。

## 基线快照（2026-09-29 核对）

- 分支 main @ `248fd70`（与规划参考一致），VERSION `6.5.0`
- 工作区干净；32 个 HTML 页面；assets 3 图（portrait/falcon-heavy/tesla-factory）
- 检索索引 169 条七类型；账本 67 条；verify.py 实为 9 项检查
- 起始分支：新建 `visual-v7-19rounds`

## 轮次状态

| 轮 | 主题 | 状态 | 版本 | 成果提交 | 推送 |
|---|---|---|---|---|---|
| 01 | 视觉基础与基线 | complete | v6.6.0 | 9c4867b | done |
| 02 | 图片与纪实素材体系 | complete | v6.7.0 | eb007ba | done |
| 03 | 首页首屏重构 | complete | v6.8.0 | 4bf942f | done |
| 04 | 首页编排与全局导航 | complete | v6.9.0 | 8686143 | done |
| 05 | 长文阅读模板 | complete | v6.10.0 | 1a6f3c5 | done |
| 06 | 事件与来源结构 | complete | v6.11.0 | 021faf4 | done |
| 07 | 公司关系总览 | complete | v6.12.0 | — | done |
| 08 | 公司档案体系 | pending | v6.13.0 | — | — |
| 09 | 事件时间轴升级 | pending | v6.14.0 | — | — |
| 10 | 资本流向可视化 | pending | v6.15.0 | — | — |
| 11 | 2008 旗舰专题 | pending | v6.16.0 | — | — |
| 12 | 平台与 AI 旗舰专题 | pending | v6.17.0 | — | — |
| 13 | 承诺与结果专题 | pending | v6.18.0 | — | — |
| 14 | 原始资料阅读体验 | pending | v6.19.0 | — | — |
| 15 | 搜索与发现 | pending | v6.20.0 | — | — |
| 16 | 手机全流程打磨 | pending | v6.21.0 | — | — |
| 17 | 双语与全站统一 | pending | v6.22.0 | — | — |
| 18 | 动效、无障碍与性能 | pending | v6.23.0 | — | — |
| 19 | 全站验收、交接与发布 | pending | v7.0.0 | — | — |

状态取值：pending / in_progress / complete / blocked。失败不推进轮次；推送失败时仅恢复推送。

## 恢复指引

- 每轮唯一成果提交信息带 `[V7-19 Rxx]` 前缀。
- 提交了但没推送 → 直接 `git push -u origin visual-v7-19rounds`，不重做工作。
- 代码完成但未验收 → 从该轮验收步骤继续。
- qa/v7-19/round-xx/ 存放每轮截图与验收记录。
- 运行锁：`.v7-lock.json`（gitignore，不入库）。发现遗留锁先确认无存活实例再删除。

## 第 1 轮工作记录（视觉基础与基线）— complete（2026-09-29）

- 交付：V7 令牌基础层（色彩/字号/间距/阅读宽/动效/焦点）；853 处全站色彩归一（32 页 + style.css + app.js + build-revisions.py 模板）；首页（朱红顶条/主按钮/kicker 短线/标题刻度）与长卷阅读版（正文 16.5px/行高 1.9/阅读宽度令牌）实际应用；重复 print 规则清理；qa-shots.py 截图协议。
- 验证：verify.py 9/9 绿（v6.6.0）；node --check 通过；双语切换/手机菜单/筛选实测正常；before/after 截图各 10 张 + QA 记录在 qa/v7-19/round-01/。
- 提交：[V7-19 R01] 一个成果提交；推送状态见表格。

## 第 2 轮工作记录（图片与纪实素材体系）— complete（2026-09-29）

- 交付：ASSETS.md 素材权威清单（来源/作者/许可/核实/加工/用途）；trace-assets.py 感知哈希溯源——portrait/tesla-factory 逐像素命中 Commons 原件（CC BY-SA 3.0 Debbie Rowe / CC BY 2.0 Maurizio Pesce），falcon-heavy 无匹配 → 替换为 SpaceX 官方 CC0 双助推着陆图（同名同尺寸零布局扰动）；新增 starship-catch（CC BY 2.0，2024-10-13 塔捕，与账本 e2024-10-13 互证）/x-hq（CC BY-SA 4.0，2022-11）/cybertruck（CC0）三张纪实图 + portrait-hero 两档封面备用裁切；companies.html 三卡配图带署名行；首页封面署名行（中英）+fetchpriority；indepth 图注补全与 alt 修正、Falcon 底部取景；全站 img height:auto；许可元数据 assets-meta/ 留档。
- 验证：verify.py 9/9 绿（v6.7.0）；node --check 通过；EN 署名切换/懒加载/3:2 比例/21:9 取景 CDP 实测；真 390px 视口零溢出（确认 qa-shots 手机档 500px 最小窗宽伪影，非站点缺陷）；改后证据 9 张 + QA.md 在 qa/v7-19/round-02/。
- 提交：[V7-19 R02] 主成果提交 eb007ba + 推送状态回填提交；已推送。
- 并发事件记录：02:49 一个并发触发（run-b）误判 run-a（本记录方）已停而接管；02:51-02:54 run-b 观察到 run-a 活跃后**主动全部退避**，将自写文件移至仓库外 `D:\vibe coding\v7r2-runb-evidence\`，并在此期间完成了 eb007ba 的推送（run-a 本地推送因网络超时未成）。run-b 的两份审计脚本（tools/verify-attrib.py、verify-tesla-factory.py）与两份元数据（assets-meta/portrait.json、tesla-factory.json）已被 run-a 的 `git add -A` 收入 eb007ba——其署名核验结论（hamming=0）与 run-a 独立溯源结果一致，互为佐证，**保留入库**。后续触发请勿重复删除或重做 R2；接管前先长观察≥10 分钟确认无写入，再核对本表与 git log。

## 第 3 轮工作记录（首页首屏重构）— complete（2026-09-29）

- 交付：首页 section#cover 重构为近黑 #101316 深色纪实封面（海报式构图：编者大标题「把未来做成生意」通栏 88–138px + 副标题定位句 + 开始阅读/探索版图/查找资料三入口 + hero-body 左文右图 + 关键数字行 + 四格业务横带带署名）；<picture> 手机档 4:5 肖像；html[lang=en] 英文标题独立刻度；删除 ≤960px 肖像 order:-1（手机照片抢占首屏根源）；print 转白底；令牌 +--accent-bright/--mist；index title/description/og/theme-color 换新定位；ASSETS.md 六处用途同步；12 页版本 span + VERSION → 6.8.0。
- 实测修复三缺陷：① 旧栅格列 144px×4 字放不下标题折三行 → 改标题通栏；② auto 轨道 min(480px,100%) 百分比循环致文字列 0 宽 → 轨道改 min(480px,44vw)；③ .deal-lines 亮色规则顺序压过暗底覆盖 → 特异性升 .deal-lines.hero-stats。
- 验证：verify.py 9/9 绿；node --check 过；CDP 真视口：桌面标题 138px 单行、EN 96px 两行、390 中英零页面溢出、CTA 底 546<844 在首屏、封面零 .reveal 无动画依赖；file:// 冒烟过；EN 切换/计数器/章节 reveal 正常；证据 9 张 + QA.md 在 qa/v7-19/round-03/。
- 提交：[V7-19 R03] 一个成果提交；推送状态见表格。
- 备注：本轮 scratch（手术脚本/探针）在仓库外 D:ibe coding7r3-work\；qa-shots 工具伪影（500px 最小窗宽/虚拟时间图片未绘）已 CDP 排除，见 QA.md。

## 第 4 轮工作记录（首页编排与全局导航）— complete（2026-09-29）

- 交付：新建 tools/site-nav.py 导航生成器（五组注册表 开始5/公司7/事件4/专题6/资料10=32 页唯一归属 + 单一模板 + aria-current + 缺 app.js 自动补挂，幂等）；32 页统一导航落地（12 masthead 页替换 + 20 页头页插入，17 页补挂 app.js，语言切换/版本号首次覆盖全站）；报头常驻「检索」胶囊；桌面下拉三态（hover/focus-within/点击）+ 外点/Esc 关闭焦点归位 + 互斥 + :has 当前组高亮；手机 ≤760px 五组手风琴 + 当前组自动展开；首页 16 卡平铺重组为五分区（#paths 三条路径 / #map 公司版图六瓦 / #features 旗舰专题主推+次级行 / #events 关键事件五条深链 primary#e* / #updates 最近更新四条）；消除 <a> 嵌套 <a>；删除 chapter-grid 死样式；.reveal 改 html.js 守卫（脚本失败正文不再隐形）。
- 实测修复两缺陷：① 汉堡点击冒泡触发外点关闭监听、清掉自动展开的当前组 → 外点处理排除 #nav-toggle；② data-en 放在按钮上会被 EN 切换的 innerHTML 替换吞掉下拉箭头 → 模板改内层 .nav-txt 承载文案。
- 验证：verify.py 9/9 绿（v6.9.0，含 32 页断链校验覆盖新导航与新锚点）；node --check 过；CDP 探针 29 项全过（下拉三态/互斥/外点/Esc 焦点/跳转落地/分区计数/EN/深读页注入/检索共存/锚点落视野/无 JS 正文可见/390 手风琴+零溢出）；reading/money/documents/timeline 注入回归零溢出；证据：before/after 各 10 张 + 整页长图 + 下拉与手机菜单交互截图 + QA.md 在 qa/v7-19/round-04/。
- 提交：[V7-19 R04] 一个成果提交；推送状态见表格。
- 备注：scratch（探针）在仓库外 D:/vibe coding/v7r4-work/；遗留两项到后续轮——20 个注入页页脚统一（R17）、公司色标体系（R7/R8，首页瓦片暂用中性编号）。

## 第 5 轮工作记录（长文阅读模板）— complete（2026-09-29）

- 交付：style.css 共享 `.lr-*` 长文组件层（深色纪实页头 .lr-hero：近黑底+大标题+斜体导语+元信息行+通栏大图署名；.lr-layout 正文列 --read-width+右侧目录栏；.lr-toc 桌面 sticky/≤960px 盒装；引语/数据框/编者注/来源脚注四类内容组件统一）；正文升 16.5px·1.92；新建 tools/build-longread.py 生成器（幂等，V7-R5-LONGREAD 标记跳过）——深读五篇全部迁移：删页内旧样式、h3→h2 建 {stem}-s{n} 锚点（站内原无深读页锚点深链，已核查）、dd-*→lr-* 类名映射、内容段落逐字保留；每篇配 R2 已溯源大图（弗里蒙特产线/肖像/星舰塔捕/猎鹰重型/Twitter 总部）+署名，og:image 指向本篇大图；阅读时长按实际内容计算静态写入（中文 300 字/分+英文 200 词/分，深读 4–5 分钟）；reading.html 加大图页头+元信息（11 分钟/约 2,900 字）并删重复旧 rd-head，十章目录与 #ch5 旧外链锚点原样保留；app.js 新增目录滚动定位（配对表+高亮带相交取最大+8px 擦边门槛）；深读页补挂进度条；ASSETS.md 五处用途同步；VERSION/12 页 span 步进 6.10.0；EPUB 重建。
- 实测修复四缺陷：① 生成器切分吃掉 `<script src="app.js">` 开标签致五页 app.js 失载（EN/进度条/定位全死）→ 开标签计入 tail 重生成；② 滚动高亮错节两段根因：观察无 id 的节但匹配 target.id（永不命中）→ 改链接↔章节配对表；IO 把相邻节 0.75px 擦边相交拆成独立回调批、批内取最大仍被覆盖 → 相交高度加 8px 参选门槛；③ 报头实为 sticky 121px（grep 截断误判），锚点 20px 余量不足钻到报头底下 → 实测后统一 132px（.lr-sec/.lr-sec h2/reading .rd-ch）；④ 探针自身断言 bug 两处（EN 图注截断 30 字符、手机截图拍在页面循环外）→ 修正并补拍真 390 证据。
- 验证：verify.py 9/9 绿（v6.10.0）；node --check 过；CDP 探针 35 项全过——页头/元信息/大图尺寸声明/正文 16.5px、目录=章节且锚点跳转落报头之下（132>121）、滚动定位高亮命中、进度条、EN 全量切换（标题/导语/图注/元信息/目录）、无 JS 正文与静态时长完整、print 页头转白底+目录隐藏、390 零溢出+盒装目录、search 索引 169 与账本深链回归；证据 before 4 张+after 17 张+QA.md 在 qa/v7-19/round-05/。
- 提交：[V7-19 R05] 一个成果提交；推送状态见表格。
- 备注：scratch（r05-probe.js 35 断言/dbg/mh/ev 可复跑）在仓库外 D:/vibe coding/v7r5-work/；qa-shots 手机档 500px 最小窗宽裁边为已知工具伪影（R2 已定性），真 390 以探针 Emulation 截图为准。

## 第 6 轮工作记录（事件与来源结构）— complete（2026-09-29）

- 交付：tools/events-data.py 事件数据单一事实来源（6 个代表性事件＝首页深链五节点 + e2006 仅年份精度示范；稳定 ID 沿用账本 e* 体系；显式日期精度 day/month/year；背景/关键事实/逐字引语/后续四段本体；七类材料 24 份关联；结构自检不过拒生成）；tools/build-events.py 生成 events.html（第 33 页，复用 R5 lr-* 模板层：深色页头+口径说明框+五段结构+精度徽标+公司 chip+材料清单+相关事件互链+塔捕图署名懒加载+sticky 目录）与 events-data.js（window.EVENTS_V7 全量数据，file:// script 标签加载，供 R7/R9/R15 复用）；site-nav.py 事件组注册（4→5）全站 33 页重注入；首页 #events 入口行 + 五条事件详情深链（r06-index-links.py）；style.css 增 .ev-* 组件层与 .section-more；VERSION/app.js/12 页 span → 6.11.0；ASSETS.md 补用途；EPUB 重建。
- 纪律：事实与引语全部取自已核实账本条目（零新增外部事实，5 条引语均在册）；e2006 无逐字原话以 no_quote_note 诚实建档；关键事实统一标注编者归纳；2018 SEC 起诉沿用「八天后」相对表述不虚构日期。
- 验证：verify.py 9/9 绿（33 页）；node --check 过；CDP 探针 33 断言全过——结构/外部深链落报头下 132px/EN 全量切换/材料链接可达（documents#d2018-08-07）/首页入口+5 深链落地/账本 67+时间轴 67+旧锚点回归/检索 169/无 JS 正文完整/390 真视口零溢出+目录盒装/file:// 六事件+数据+样式；before（v6.10.0 git worktree）/after 截图 11 张 + QA.md 在 qa/v7-19/round-06/；已人工复核干净整页图、EN 图、390 图、首页事件区改前改后。
- 探针伪影三项排除（非站点缺陷）：懒加载图视口外不取图、同文档 hash 导航不重载、captureBeyondViewport 的 sticky/reveal 冻结（截图前 static 化+强制 is-visible）。
- 提交：[V7-19 R06] 一个成果提交（amend 清除误入的 --help/ 截图杂物后为 021faf4）；推送状态见表格。
- 备注：scratch（r06-probe.js 33 断言/reshot 脚本）在仓库外 D:/vibe coding/v7r6-work/；公司色标留 R7/R8（本轮 chip 中性样式）；检索未覆盖 events.html 留 R15 事件聚合处理；并发交接——run-b 完成并推送 R5 后自录锁释放，本实例（run-a）核对 git log/账本/进程/写入四证后接管。

## 第 7 轮工作记录（公司关系总览）— complete（2026-09-29）

- 交付：tools/companies-data.py 关系数据单一事实来源（11 节点×13 边：类型/日期精度/双语标签/图上短标签/证据分级 12 verified+1 editorial/站内来源锚点；结构自检不过拒生成；与 events-data.py 交叉引用）；tools/build-network.py 生成器（幂等注入 companies.html#network：SVG 静态关系图+图例+交互详情面板+三组文字清单；自动补挂 companies-data.js）；companies-data.js（window.COMPANIES_V7，供 R8/R9/R10）；全站公司色标体系定稿（:root --co-* 十色，接入关系图/首页六瓦顶条/events chip 三处，色标只作辅助名称文字为准）；首页 #map 入口行；VERSION/app.js/13 页 span → 6.12.0；EPUB 重建。
- 纪律：13 条关系零新增外部事实；SolarCity 用 e2006「创意发起·任董事长」口径；SpaceX 只用通识年份并标注「创立故事细节未入册」；xAI 收购 X 引账本 e2025-03-28；OpenAI—xAI 标编者关联；金额不混估值与收入。
- 验证：verify.py 9/9 绿（33 页）；node --check 过；CDP 探针 43 断言全过（结构 14/交互 5/键盘 2/双语 6/首页 2/events 2/无 JS 3/390 真视口 4/file:// 4/版本 1）；探针抓出 2 真 bug（详情面板 evidenceLabel/statusLabel 双语对象字符串化）已修复；截图伪影 2 处排除（smooth-scroll 截图停顶→instant 重拍；懒加载视口外不取图）；桌面/390/EN/file:// 截图人工复核；证据 8 张 + QA.md 在 qa/v7-19/round-07/。
- 提交：[V7-19 R07] 一个成果提交；推送状态见表格。
- 备注：scratch（r07-probe.js 43 断言/r07-reshot*.js/d6-debug.js 可复跑）在仓库外 D:/vibe coding/v7r6-work/（应为 v7r7-work）；R6 事件档案未含 e2025-03-28，xai 详情无事件深链为已知口径（本轮不扩，账本锚点直链）；并发交接——本实例（run-a）接管依据：前锁(v7r6-20260929-a) complete、R06 三提交已推送 0/0、仓库 05:35:42 起 ≥12 分钟零写入、残留 http.server 为凌晨孤儿进程。
