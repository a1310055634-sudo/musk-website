# V9-20 R19 验收记录 · 动效与微交互＋质量节点③（v9.9.0）

日期：2026-10-02（定时任务第二次触发，锁 run=V10PLAN-R19）

## 成果

- **transition 审计清单化**：全站 58 处声明全分类落盘 `transition-audit.tsv`（行号/分类/处置/声明四列）——token-fast 27 / slow 白名单保留 12 / none-reduce 9 / animation 5 / btn-press 1 / other 4。
- **归一**：0.18s/.18s/0.25s 硬编码 8 处 → var(--t-fast)；归一后硬编码清零（探针断言）。0.3s 浮起/0.4s 展开/0.6–1s 进场/stagger 为语义档保留白名单（12 行），避免视觉节奏回归。
- **三态闭环**：.btn 补 :active 按压（translateY(0)+80ms）；hover 浮起↔active 按压↔focus（R15 全局 :focus-visible 出口）齐备；aria-pressed 切换型组件不强加。
- **reduce 复核**：14 块覆盖（reveal/bars/gx/cap/net/汉堡/语录滚动/飞行彩蛋），CDP 模拟 reduce 实测 reveal 直出 opacity=1。
- **性能复测**：五页 load 中位 ≤5ms（127.0.0.1+urllib 口径注明）；体积 style.css 131.6 kB/app.js 31.9 kB/search-index.js 210.8 kB/HTML 38 页 2071.5 kB——perf.json。
- **质量节点③**：R15 32 张（双视口双语）+ R16 12 + R17 12 + R18 18 + R19 12 张 before/after 齐备（round-15/16 为 before|after 子目录结构）。

## 验证

| 项 | 结果 |
|---|---|
| verify.py | ✓ 9/9（38 页 / 索引 318） |
| CDP 探针 tools/v9r19-probe.js（端口 9375） | ✓ **23/23**：文件级 8（归一清零/令牌 27/白名单对齐 TSV/btn:active/全局 focus/ reduce 14/审计 58 行/perf）/btn 三态 2（computed 0.18s + 规则扫描）/reduce 模拟 1/三视口九宫格 12 |
| before/after | 桌面四页：timeline/capital 逐像素一致（零静态回归）；index/survival 微小字节差（13B/10B）＝运行中动画帧差（语录轮播），与 transition 归一无因果，如实注明；390 四页 in 档 |
| 版本三件套 | ✓ 9.8.0→9.9.0，15 页 span（resources 提前重建后 span 14+已建 1，复核全一致） |
| sync-changelog / EPUB | ✓ 208 条 / 223,159 B |

## 工程记录

- **bump 派生坑第三次出现（任务书红线生效）**：v9r18 文件的正则旧值仍是 `9\.7\.0`（上轮派生只改了 NEW 未升级正则），本轮派生 replace("9\.8\.0") 没匹配 → app.js count=0 即停（VERSION 已写）。按红线 grep subn 行发现后修正正则重跑。**教训固化：派生 bump 必须同时升级「OLD 常量+两处正则旧值」三处。**
- 探针两处自误修正：慢档断言基数按 TSV 对齐（12 vs decls 8——delay 行不匹配时长正则属预期）；reduce 总数实为 14（先前口头记 15 有误，以 grep 为准）。

## 产物

- qa/v9-20/round-19/：transition-audit.tsv（58 行）/ perf.json / before|after 桌面 8 张 + 390 4 张。
- 工具脚本：tools/v9r19-perf.py / v9r19-probe.js / v9r19-bump.py。

## 提交

- 成果提交：`[V9-20 R19]`（本地，不推送）。
- 第二提交：账本回填 + build-revisions + EPUB 重刷。
