# V9-20 R15 验收记录 · 设计系统升级（v9.5.0）

日期：2026-10-01 · 轮次：R15/20 · 版本：9.4.0 → 9.5.0（本地提交，不推送）

## 一、本轮范围（计划 R15 原文对照）

| 计划要求 | 落实现状 |
|---|---|
| 色阶：`--coal` / `--paper` / `--accent` 各衍生 3–5 档 | ✅ `--paper-0/50/100/150/200`（5 档）、`--coal-soft/0/100/200`（4 档）、`--accent-deep/accent/accent-bright/accent-soft/accent-glow`（5 档）；另建 `--tx-1…4`（浅底文字 4 阶）、`--txd-1…6`+`--txd-cool`（深底文字 7 阶）、`--hue-*`（五色相刻度）、`--rule-*`（描边 6 阶） |
| 字号阶梯（clamp 体系） | ✅ 标题 `--fs-hero/hero-m/h1/h2/h3/h4/lead` 全 clamp；正文固定阶梯 `--fs-body-lg…--fs-3xs` 12 阶 + 大字号补充 14 阶（`--fs-9…--fs-48`）；**正文 px 字面值 0 残留**（本轮替换 335 处） |
| 间距标尺（4/8 基） | ✅ `--space-1…8` 主阶 + `--space-1h…6h/9` 半阶（共 18 阶）+ `--gap-inline/block/section` 语义别名 |
| 圆角/阴影/边框分层 | ✅ `--r-1…4 + --r-pill + --r-circle`（6 档，替换 46 处）、`--shadow-1/2/2b/accent/accent-lg/ring-paper`（6 档，替换 8 处）、`--wash/--rule-soft/--hairline/--rule-mid/--rule-strong/--hairline-paper`（6 阶，替换 7 处） |
| `:focus-visible` 统一 | ✅ 新增 `--focus-w(3px)/--focus-w-tight(2px)/--focus-offset(3px)/--focus-offset-tight(2px)/--focus-offset-wide(4px)/--focus-color/--focus-color-dark/--focus-color-invert`；正文区 outline 硬编码 **0 残留**（改 8 处） |
| 深浅双主题变量一致性核对（`--mist`/`--muted` 对比度 ≥4.5 复测） | ✅ `--mist` 9.27:1、`--muted` 6.24:1 均达标；**另查出并修复 3 类不达标小字色**（见第三节） |
| 落地 index + survival-2008 + timeline + capital-evolution 四页样板 | ✅ 四页全部消费新令牌，before/after 各 16 张全页截图 |
| 验收：before/after 八组截图；对比度抽测；三视口零溢出复扫 | ✅ 8 组（4 页 × 2 视口）× 中英 = 16 张 ×2；对比度双路核验（Python 静态 + 浏览器实算）；320/390/768 四页零溢出 |

## 二、令牌层结构（三层）

```
① 刻度令牌（唯一原值来源）   ② 语义令牌（组件唯一消费入口）   ③ 焦点令牌（统一出口）
  --hue-*      5 色相          --ty-*        6 事件类型          --focus-w / -tight
  --paper-*    5 档暖白        --paper/--coal/--ink/--card       --focus-offset / -tight / -wide
  --coal-*     4 档近黑        --muted/--mist/--navy             --focus-color / -dark / -invert
  --tx-*       4 阶浅底文字    --accent-text/--on-hue
  --txd-*      7 阶深底文字
  --accent-*   5 档朱红
  --rule-*     6 阶描边
  --r-*        6 档圆角
  --shadow-*   6 档块影
  --fs-*       26 阶字号
  --space-*    18 阶间距
```

**令牌总数 37 → 113**（`qa/v9-20/round-15/token-inventory.md` 为自动生成清单）。

**公司色标 `--co-*`（10 项）语义与值一字未动**——探针逐项断言通过。

## 三、对比度复核：查出并修复 3 类不达标小字色

WCAG 2.1 相对亮度公式，实测见 `contrast-baseline.txt`。

| 原值 | 用于 | 对比度 | 处理 |
|---|---|---|---|
| `#8a857c` | 时间轴年份轴标、`gx` 引语行（266 处）、`.pt-year`、`gxl-q` | **3.22:1 ❌** | → `--tx-3`（`#6A665D`，浅底 **5.02:1** / 卡片 4.63:1），5 处（style.css）+ 13 页内联页脚 |
| `#9a948b` | `gx-empty` 空态提示、`cap-detail-empty`、`reading` 目录待办 | **2.64:1 ❌** | → `--tx-3`（5.02:1），3 处 |
| `#6f6a62` | 页脚彩蛋行 `.footer-hint`（深底） | **3.47:1 ❌** | → `--txd-6`（`#8a857c`，深底 4.80:1） |
| `#fff` | chip/card/图节点底色（26 处） | 非文字 | → `--paper-0`（暖白，统一暖纸体系） |
| `#8a857c`（暗底） | 页脚英文注、图例装饰线 | 4.80–5.08 ✅ | 保留，归 `--tx-4`（标注「仅装饰/暗底小字」） |

**达标基线（未改，仅记录）**：`--muted` 6.24、`--mist` 9.27、`--accent-text` 5.80、`--accent-bright` 6.26、`--ty-start` 5.34、`--ty-deal` 10.08、`--ty-milestone` 6.84、`--ty-risk` 5.20、`--ty-ok` 4.60、白字于类型色块 5.24–11.48。
**已知并文档化的例外**：`--accent`（#C84032）浅底 4.35 / 深底 3.76 —— 该令牌按设计只用于大字/边框/填充，小字一律走 `--accent-text`（5.80）与 `--accent-bright`（6.26），此约定自 V7 沿用，本轮在 `:root` 注释中显式写明。

**正文区剩余色字面值仅 3 个**：`#101316`（底色）、`#F3F0E8`（底色）、`#C84032`（即 `--accent` 定义处）。

## 四、验证结果

| 项 | 结果 |
|---|---|
| `verify.py` | **9/9 全绿**（38 页 / 索引 318 / 版本 9.5.0 / 语录卡 103+2 豁免 / 修订史 206 / EPUB 新鲜） |
| `node --check` | app.js / search-index.js / companies-data.js / events-data.js / timeline-events.js / capital-data.js 全过 |
| CDP 探针 | **69/69 全绿**（`tools/v9r15-probe.js`，端口 9362）：文件级 33（令牌结构/8 组刻度/公司色标 10 项红线/硬编码清零/版本与产物）+ 语义别名等价性 14 + 元素级令牌消费 12 + 焦点环 4 + 对比度实算 5 + 三视口零溢出 3 |
| 三视口零溢出 | 320 / 390 / 768 × 四页 = 12 组合**零横向溢出** |
| 对比度 | 静态（Python）+ 动态（浏览器实算 WCAG 公式）双路核验，修复后全部 ≥4.5 |
| EPUB | 223,127 B / 24 章，新鲜度通过 |
| 版本三件套 | VERSION + app.js SITE_VERSION + 15 页 span（替换计数打印在案） |

**探针修正 2 项（均为探针缺陷，非页面缺陷）**
1. 断言「无 `font-size` px 字面值」首跑失败——实际残留为 `0.5em`/`3.2em`/`11.5pt`（相对单位与印刷块），断言收敛为仅禁 `px` 字面值。
2. 对比度抽测首跑 5 项失败——根因是 Node **模板字符串内 `\d` 被 JS 字符串转义吞成 `d`**，正则 `/[\d.]+/g` 实为 `/[d.]+/g` 匹配失败致 IIFE 抛错返回 `undefined`；改用 `slice+split` 解析颜色值后全过。**教训：CDP 探针里正则写进模板字符串必须 `\\d`，或干脆避开转义。**
3. `.gx-empty` 为条件渲染元素（筛选无结果时才出现），改用**合成元素**读取计算样式后再测对比度。

## 五、before/after 可视化证据

- 截图（全页）：`before/` 与 `after/` 各 **16 张**（index / survival-2008 / timeline / capital-evolution × 桌面 1440×900 / 手机 390×844 × 中/英）
- 像素差异量化（`pixel-diff.txt`，Pillow 逐像素）：

| 页面 | 变化像素占比（桌面中） | 主要变化 |
|---|---|---|
| timeline | **14.67%**（最大 14.83%） | 年份轴标 + 266 条引语行 3.22→5.02 加深（本轮最显著视觉 delta） |
| capital-evolution | 8.58% | 图节点底色纯白→暖白 `--paper-0`、图例线归 `--tx-4` |
| survival-2008 | 0.05–0.20% | `sv-*` 白盒→暖白、阶段徽标色相令牌化 |
| index | 0.03–0.07% | 页脚字色归 `--txd-*` 阶梯 + 版本串 |

- 拼图对照：`compare/cmp-timeline-zh.png`、`compare/cmp-capital-zh.png`、`compare/cmp-index-footer-zh.png`
- 探针态截图：`probe/probe-index-desktop.png`

**如实说明**：R15 是美术**地基轮**，视觉 delta 刻意克制（多为值等价的令牌化）；可辨变化集中在「对比度修复」与「暖白表面统一」两处。显著美术迭代在 R16（首页视觉）/R17（数据图形）/R18（排版）承接——四页样板的令牌通道已铺好。

## 六、源码改动清单

| 文件 | 改动 |
|---|---|
| `style.css` | `:root` 令牌层重建（37→113 项，含三层结构与对比度注释）；正文令牌化：类型色 12 处 / 徽标色 6 处 / 朱红派生 4 处 / 中性色 13 处 / 表面 26 处 / 描边 7 处 / 圆角 46 处 / 块影 8 处 / 字号 335 处 / 焦点环 8 处；`@media print` 18 块显式保护 |
| `tools/v9r15-tokens.py` | 上述令牌化脚本（逐项打印命中数，关键项计数不符即报错退出） |
| `tools/v9r15-pages.py` + 15 个 HTML | 页面级内联样式令牌化 21 处（对比度修复 + 色值收敛） |
| `tools/build-revisions.py` | 模板内 `#8a857c`/`#1f3a5f` 硬编码 → `var(--tx-3)`/`var(--navy)`（治本，防重跑回归） |
| `CHANGELOG.md` / `VERSION` / `app.js` / 15 页 span | v9.5.0 条目与版本三件套 |
| `tools/v9r15-{shot,diff,contrast,probe,bump}.py|js` | 本轮新增工具：截图器 / 像素差异 / 对比度算 / 探针 / 升版 |
| `capital-evolution.html` 等 | 页脚细字色令牌化（对比度修复） |
