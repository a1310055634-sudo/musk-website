# V9-20 R17 验收记录 · 数据图形工业风（v9.7.0）

日期：2026-10-02（单轮单触发，锁 run=V9-20-R17）

## 成果（纯 CSS，style.css +71 行，DOM/SVG 几何/生成器零改动）

- **etype 节点形状语言**（色标不变加形）：start=圆 / deal=方 / gamble=菱（45°）/ milestone=满圆 / risk=三角（clip-path）；类型筛选芯片补 ::before 形状图例（原纯文本），图例即形状表。
- **gx 年轴刻度细化**：年份等宽（新令牌 --font-num 入 R15 字体层）+ ::after 6px 刻度线；清单日期等宽。
- **标注层数字等宽**：cap-elabel 改 sans + tabular-nums（与 serif 节点名分层）；cap-meta/cap-status/net-elabel/图例 tabular-nums。
- **图例语法统一**：cap/net 同字号 --fs-small-2、同 22px 列距、虚线同构造（repeating-linear-gradient）。
- **图底点阵网格**：cap-graph/net-graph 示意纸面点阵（26px 网距，不模拟坐标）；print 显式关闭。
- **数据编码不动（红线自查入探针）**：ribbon 线宽=生成器属性值、gamble 色仍 rgb(200,64,50)、「示意非等比」口径注原文保留、R17 段零新增 transition/animation。

## 验证

| 项 | 结果 |
|---|---|
| verify.py | ✓ 9/9（38 页 / 索引 318） |
| CDP 探针 tools/v9r17-probe.js（端口 9365） | ✓ **34/34**：文件级 5（含数据编码保全/口径注保留/reduce 块仍在）/桌面三图 17（形状语言 4+芯片图例 1+年轴 2+cap 5+net 4）/三视口九宫格零溢出 9/390 清单形态 3 |
| node --check | ✓ app.js 与探针/截图脚本均过 |
| sync-changelog / build-epub | ✓ 206 条（v0.1.0→v9.7.0）/ 223,159 B · 24 章 |
| 版本三件套 | ✓ 9.6.0→9.7.0，15 页 span，复核全一致 |
| before/after | ✓ 6 组：gx 桌面（同取景 .gx-controls，stash 法取真 before，差异可辨）/ cap 桌面 / net 桌面（网格+标注+图例可见差异）；390 三组逐像素一致=**预期正确**（两 SVG 图移动端本就以清单形态呈现，本轮未动清单形态——这正是计划「390 清单形态」的回归证据） |

## 探针修正记录（三处均为探针自身缺陷，页面正确）

1. 「无新增 transition」断言被本段头注释里的 "transition" 字样误命中——改查 `transition:` 声明。
2. 「图例同字号」把 capital 页与 companies 页元素放在同页比较（.net-legend 不存在于 capital 页）——改跨页取值 Node 侧比较。
3. 芯片 ::before 断言把伪元素写进 querySelector（非法选择器抛异常）——改 querySelector(元素)+getComputedStyle(el, '::before') 分离调用。

## 截图取景教训（供 R18/R19 复用）

首拍 4 张 after 与 before 逐像素相同：①高图（cap/net）在 390 被既有移动端规则整体隐藏（清单形态）→一致=正确；②gx-board 高于视口，scrollIntoView block:'center' 框进中部泳道（本轮未动的区域）→改滚到 .gx-controls（芯片+年轴+事件道入画）并用 `git stash push -- style.css` 取同取景真 before 配对。

## 产物

- qa/v9-20/round-17/：before/after 各 6 张（桌面 1440×900 + 390×844）。
- 工具脚本：tools/v9r17-shot.js（选择器定位截图）/ v9r17-probe.js / v9r17-bump.py。

## 提交

- 成果提交：`[V9-20 R17]`（本地，不推送）。
- 第二提交：账本回填 + build-revisions + EPUB 重刷。
