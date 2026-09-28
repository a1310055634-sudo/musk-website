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
| 04 | 首页编排与全局导航 | complete | v6.9.0 | （提交后回填） | — |
| 05 | 长文阅读模板 | pending | v6.10.0 | — | — |
| 06 | 事件与来源结构 | pending | v6.11.0 | — | — |
| 07 | 公司关系总览 | pending | v6.12.0 | — | — |
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
