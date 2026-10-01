# V9-20 R16 验收报告 · 首页视觉迭代（v9.6.0）

- **轮次**：R16/20（单轮单触发）
- **日期**：2026-10-01
- **成果提交**：`6a0a5ae`（26 文件）｜**账本回填**：本提交
- **版本**：9.5.0 → 9.6.0（VERSION + app.js SITE_VERSION + 15 页 span，替换计数在案）
- **模式**：纯本地（未 push、未发布、未做 Pages 验证）

## 一、本轮目标与达成

| 计划要求 | 达成情况 |
|---|---|
| 封面 hero 构图（标题/肖像/业务画面主次） | ✅ 封面标 `COVER · 2018` + 内衬双线框；`strip-tag` 移图上角标；hero-stats 边线 2px/55% + 数字提亮 `--paper-0` |
| 模块节奏（feature-lead/feature-rows/path-cards 层级差异化，打破等尺寸卡片感） | ✅ `firm-grid` 6 等大 → **2 特大（span 2）+ 4 标准**；`feature-row` 前三条朱红 3px 左标线；全行 hover 微底色；`path-row` hover 标题转朱红 |
| 三入口（阅读/版图/检索）视觉强化 | ✅ `.btn` 按钮行 → **`.act` 编号入口条**（01/02/03 + 分隔线 + 箭头；主入口朱红实底；hover 反白 + 箭头位移） |
| 消费 R15 令牌 | ✅ `--paper-*` 阶梯、`--paper-0`、`--fs-26/-14-5/-2xs/-label`、`--t-fast`、`--focus-*`、`--hairline-paper`、`--coal-200`、`--accent-bright`、`--on-hue` |
| 新旧首屏对比截图差异显著 | ✅ 像素差异 **11.03%–28.13%**（中位 22.3%），远超 10% 阈值 |
| 320/390/768 复扫 | ✅ 四页 × 三视口 × 中英，**零横向溢出** |
| EN 标题不破版 | ✅ `hero-title scrollWidth ≤ clientWidth`；EN 下三入口结构保持 3 枚 |

## 二、验收项明细

### 1. CDP 探针 43/43（`tools/v9r16-probe.js`，端口 9364）

| 组 | 项数 | 关键实测 |
|---|---|---|
| 文件级结构 | 6 | 2 特大瓦片 / 3×act-no+act-arr+act-txt / `data-en` 全落叶子上 / cover-tag / 4×strip-tag 为 img 后 figure 直接子元素 / figcaption 无 strip-tag |
| 文件级样式 | 8 | `.firm-tile--xl` span 2 / `.act-primary` 朱红实底 / `.act:focus-visible` 令牌 / `nth-child(-n+3)` 左标线 / cover-tag & strip-tag 绝对定位 / stats 2px/55% / reduced-motion 块 |
| 版本产物 | 3 | VERSION=9.6.0 / app.js=9.6.0 / 15 页 span |
| 特大瓦片几何 | 3 | **xl 宽 501px = 2× 标准 244px**；同行并排（right ≤ left2）；h3 26px vs 20px |
| 三入口与封面样式 | 6 | 3 枚；主入口 `rgb(200,64,50)` 白字；编号右细线 1px；cover-tag absolute+朱红；strip-tag absolute；stats 2px |
| FEATURE 行分层 | 4 | 7 条；前 3 条 `3px rgb(200,64,50)`；后 4 条 `0px`；hover 规则存在 |
| EN 切换 | 4 | 结构 3 枚不变；文案 Start Reading；标题不破版；零溢出 |
| 三视口溢出 | 6 | 320/390/768 × 四页（zh）+ index × 三视口（en） |
| 键盘可达 | 2 | 60 次 Tab 内命中 `.act`；焦点环 3px solid（`--focus-w`） |
| 产物 | 1 | 探针首屏截图 zh+en 落盘 |

### 2. 像素差异量化（`tools/v9r16-diff.py`，Pillow 逐像素）

| 文件 | 尺寸 | 差异像素 | 平均通道差 | 最大差 | 峰值段 |
|---|---|---|---|---|---|
| index-desktop-zh | 1440×6231 | **11.77%** | 10.122 | 708 | 段5(21%) |
| index-desktop-en | 1440×6534 | **11.03%** | 9.742 | 708 | 段1(19%) |
| index-tablet-zh | 768×7496 | **25.67%** | 18.460 | 745 | 段1(17%) |
| index-tablet-en | 768×8257 | **28.13%** | 23.422 | 762 | 段1(21%) |
| index-mobile-zh | 390×8976 | **26.42%** | 23.880 | 765 | 段1(19%) |
| index-mobile-en | 390×11323 | **18.88%** | 14.851 | 741 | 段1(16%) |

解读：桌面差异 11% 因全页极长（6000+px）而改动集中在首屏与模块区；平板/手机全页在 MAXH 7000 截断范围内占比更高。峰值段集中在段 1（首屏 hero）符合预期。

### 3. 其他质量门

- `verify.py` **9/9**：断链 / 重复 id / 版本一致性 9.6.0 / 检索索引 318 / 时间轴 / 语录卡（103+2 豁免）/ 修订史 206 / CHANGELOG 首条 / EPUB 新鲜度
- `node --check` 全过（shot / probe / diff 脚本）
- 公司色标 `--co-*` 10 项语义与值未动（本轮零触碰）
- `prefers-reduced-motion: reduce` 下本轮新增微动效全覆盖
- EPUB 223,159 B / 24 章；修订史 206 锚点（幂等，本轮未动账本数据）

## 三、过程修正（探针首跑 38/43 → 43/43）

| # | 现象 | 定性 | 处理 |
|---|---|---|---|
| 1 | xl 瓦片标题实测 20px（期望 26px） | **页面真缺陷** | `.firm-tile--xl h3` 与 `.firm-tile h3` 同特异性（0-1-1），被源码顺序靠后者覆盖 → 改 `.firm-grid .firm-tile--xl h3`（0-2-1） |
| 2 | 主入口文字色实际 `rgb(255,255,255)` | 探针期望值写错 | `--on-hue` 本就是 `#fff`（非 `--paper-0`），修正断言期望 |
| 3 | `transitionProperty = none` | 探针环境矛盾 | reduce 模拟下所有 transition 被 `!important` 禁用（这正是设计目标）→ 改文件级断言 hover 规则存在 |
| 4 | 14 次 Tab 未命中三入口 | 探针上限不足 | `.nav-drop` 虽 `display:none`，但 `.nav-group:focus-within` 展开使其链接可聚焦（鼠标 hover ↔ 键盘 focus 对等的**刻意可达设计**，约 43 个导航项）→ 上限放宽至 60 |

教训沉淀：① 断言「动效已挂」不要在 reduce 模拟下做；② 断言「Tab 第 N 次命中」先清点导航可聚焦项数；③ CSS 同特异性规则冲突要靠提高特异性解决，不靠调整源码顺序（脆弱）。

## 四、产物清单

```
qa/v9-20/round-16/
├── ACCEPTANCE.md                  # 本文件
├── before/  (6 张)                 # index × 3 视口 × 中英（v9.5.0）
├── after/   (6 张)                 # 同上（v9.6.0）
├── compare/
│   ├── cmp-firstscreen-desktop-zh.png  # 首屏 900px 并排（2904×946）
│   ├── cmp-firstscreen-tablet-zh.png   # （1560×946）
│   └── cmp-firstscreen-mobile-zh.png   # （804×946）
├── pixel-diff.txt                 # 差异量化原始输出
└── probe/
    ├── probe-index-desktop-zh.png # 探针首屏证据
    └── probe-index-desktop-en.png
```

工具：`tools/v9r16-shot.js`、`tools/v9r16-probe.js`、`tools/v9r16-diff.py`、`tools/v9r16-bump.py`

## 五、遗留与下一轮

- 无遗留阻塞项。
- **R17 预告**：数据图形工业风——`gx-*`（timeline 年份轴）/ `cap-*`（capital-evolution 流向图）/ `net-*`（companies 关系图）三图精修：线宽与节点层级、网格与刻度统一、标签排版与碰撞避让、深底图形对比度复核。
