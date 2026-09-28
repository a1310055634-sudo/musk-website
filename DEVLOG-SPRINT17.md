# 马斯克商业志 · 17 轮冲刺开发日志（v5.89.0 → v6.5.0）

> **写给接手的 agent**：本日志记录 2026-09-26「每 20 分钟一轮 × 17 轮」自动化冲刺的全部技术变更、管线用法与坑位，目标是让你读完就能安全地开下一轮。项目全貌与内容纪律见 `DEVLOG.md`（**先读它**），本篇是它的技术增补，两者冲突时以实际代码为准。撰写日期 2026-09-28，基线 commit `adb2d93`。

---

## 一、冲刺总览

| 轮 | 版本 | 主题 | 净变更 |
|---|---|---|---|
| 1 | v5.89.0 | 检索扩容A | controversy 五篇入索引（107→112），新类型「争议深读」 |
| 2 | v5.90.0 | 检索扩容B | chronicle 53 行注入锚点 + finance 四节入索引（→169） |
| 3-5 | v5.91-5.93.0 | 争议三篇深化 | Autopilot/工会/Twitter 各 3 段→5 段，8 个多源新节点 |
| 6 | v5.94.0 | ai-strategy 重写 | 4.8→11.8KB，双语补齐 |
| 7-11 | v5.95-5.99.0 | deep-dive 01-05 重写 | 平均增幅 109%，全部 10KB+ |
| 12 | v6.0.0 | 账本候选裁定 | Fremont/NUMMI 放弃（无逐字源）→ 转排版精进 |
| 13 | v6.1.0 | Open Graph | 32 页 og 五件套 |
| 14 | v6.2.0 | 排版精进 | reading/controversy 480px + 时间轴横滑 |
| 15 | v6.3.0 | 技术债#1 核销 | bg 匹配缺口已被消化（6/6 实证） |
| 16 | v6.4.0 | 全面 QA | 打印 5/5、双语核查、补 1 处 480px 缺块 |
| 17 | v6.5.0 | 收官 | 全量对账 160 条、修订历史 100→107 锚点 |

触发机制：定时任务（每 20 分钟，maxRuns=17）已耗尽并验证完结——完成后 3 次触发均按 N≥18 分支静默退出。**不会再有自动轮次**，后续迭代由你手动/新任务驱动。

---

## 二、冲刺后的系统架构

### 2.1 检索子系统（变化最大，接手必懂）

`search-index.js` 由 `tools/build-search-index.py` 生成，现含 **七个解析段**（顺序固定）：

```
primary → documents → interviews → x-posts → controversy(CV_META) → chronicle(行锚点) → finance(节锚点)
```

- **controversy 段**：五篇深读的摘要/代表引语**硬编码**在脚本顶部 `CV_META` 字典（id: sec-sec / sec-pedo / autopilot / union / twitter）。深化争议内容后必须手工同步 CV_META 的 zh/bg 摘要。
- **chronicle 段**：53 行的锚点 id 是本轮**注入**的——精确日期 `c{Y-M-D}`、年月 `c{Y-M}`、纯年份 `c{Y-两位序号}`；区间日期（如 `2022.07–10`）按起始月定形；重月自动加 `-2` 后缀（现存 `c2025-03-2`）。entry 的 `d` 字段**必须用行内真实日期文本**，不得虚构精度。
- **finance 段**：四节沿用页内 id（tesla/spacex/x/xai），`d` 取节内最大年份。
- **实体推断**（ENTITY_RULES）对 s/q/zh/bg 文本跑正则生成 `c` 字段（公司过滤），无匹配落 `['综合']`——新增公司关键词要改这里的规则表。
- **断言字典**（脚本尾部）：`{'言行实录': 67, '一手文档': 9, '访谈与表态': 18, 'X 帖': 13, '争议深读': 5, '编年史': 53, '财务全景': 4}`。**任何页面增删条目，必须同步三处**：① 此断言；② `verify.py` 检查4 的 `total_expected` 公式（现为 n_ps+n_docs+n_iv+n_posts+n_cv+n_ch+n_fin）；③ `search.html` 类型按钮组（`.sr-types` 的 data-t）。
- **检索逻辑在 search.html 内嵌脚本**（不在 app.js！）：`match()` 约 179 行、已含 `(it.bg||'')`；`yearOf()` 解析 d 的前四位（纯年份条目如 '2022' 可正常过滤）；snippet 取 `q + ' ｜ ' + zh` 截 240 字符。

### 2.2 质量门禁 verify.py——实为 **9 项**

断链（含跨页锚点）/ 重复 id / 版本一致性 / 检索索引一致 / 时间轴节点一致 / 语录卡覆盖（白名单 3 豁免）/ 修订历史一致性 / **CHANGELOG 首条版本 = VERSION** / **EPUB 新鲜度**。

⚠️ **口径修正**：冲刺期间的提示词与 CHANGELOG 反复写「11 项全绿」，实际是 **9 项**（v5.88.1 加两道门禁时从 7 数成了 9，提示词又误写成 11 并沿用 17 轮）。接手后请以 `python tools/verify.py` 实际输出为准；若要改文案，全站 grep「11 项」一次清干净。

两道新门禁的含义：
- **CHANGELOG 首条版本**：每轮必须先记账再终检（顺序：改内容 → 记账 → sync-changelog → 版本步进 → verify → commit），漏记账直接红。
- **EPUB 新鲜度**：双重判据 = 最新账本条目日期文本（现 2025.11.06）在书内 + EPUB mtime 不旧于任何 html。**所以每轮改完内容必须跑 `python tools/build-epub.py`**（秒级），否则必红。

### 2.3 版本步进机制

三处一致（verify 检查3）：`VERSION` 文件 / `app.js` 的 `SITE_VERSION = '…'`（仅此一处）/ **12 个页面**的 `<span … site-version-val">X<`。步进用 python 精确替换 span 模式，**绝不碰 changelog.html 里渲染出的历史版本号文本**。模板脚本见本轮 CHANGELOG 各轮记录，要点：`io.open(…, encoding='utf-8', newline='\n')`、assert 替换数==1。

### 2.4 sync-changelog.py（v5.88.1 修复版）

标题正则已容忍「 轮」后缀（历史上有两条 `## v5.85.0 轮`）；遇到无法解析的 `## v` 标题会**打印警告并跳过**（不再静默丢弃）。changelog.html 页头的「N 条，v0.1.0 → vX」由脚本自动重写。

### 2.5 双语机制

app.js 对 `[data-en]` 元素做 **innerHTML 整体替换**（zh 原稿缓存在 dataset.zh）——因此 data-en 属性值里含 `<a href>` 标签是**合法且必要**的（链接在 EN 模式正常渲染），不是缺陷。引语块用「英文 blockquote + `.dd-zh`/`.ai-zh` 中译行」的并列结构，不走 data-en。

### 2.6 og / 窄屏 / 打印现状

- og 五件套 32 页全覆盖（og:image 绝对 URL 指 Pages 域名）；
- ≤480px 块：deep-dive×5、ai-strategy、reading、controversy；≤640px：style.css 时间轴横滑（.ps-timeline）；
- 打印防拆：各页 print 块 + style.css `.ps-timeline { break-inside: avoid; }`；
- **尚未覆盖**：interviews/x-posts/documents 等第一手页的窄屏细调（低优先级，内容密集但结构简单）。

---

## 三、每轮固定流程（17/17 全绿的作业模板）

```bash
cd "D:\vibe coding\musk-website"
git status                      # 0. 清场；非净先收尾上轮
# 1. 实现内容（HTML 大改用「python 读全文→替换→整文件写回」，勿用 Edit 工具跨轮改同文件）
python tools/build-search-index.py   # 2. 改过七个内容页之一必跑（断言同步过）
python tools/build-epub.py           # 3. 每轮必跑（EPUB 新鲜度门禁）
python tools/verify.py               # 4. 必须全绿；两修不过 → git checkout -- . && git clean -fd 回滚本轮，下轮重试
# 5. CHANGELOG.md 顶部记账：## v{X.Y.Z} — {日期} · 主题（自由精进第N轮）+ **主题包成果**/**质量门**
python tools/sync-changelog.py       # 6. 重生成 changelog.html
# 7. 版本步进（VERSION / app.js SITE_VERSION / 12 页 span，python 精确替换）
node --check app.js                  # 8. 改过 app.js 才需要
git add -A && git commit -m "v{X.Y.Z} 类型: 简述" && git push   # 9. 提交前 git log --oneline -3 核对版本号
```

失败协议：verify 两次修不过即回滚（不提交不记账），下一轮自动/手动重试同轮，版本号不空转。连续两败第三次降级为排版精进并在 CHANGELOG 注明。

---

## 四、本轮新增坑位（agent 必读）

1. **Edit 工具跨轮失效**：多轮自动化后文件 mtime 变化，Edit 报 "File has been modified since read"。对策：内容修改统一走 python `io.open` 整文件读改写。
2. **bash heredoc 吃反斜杠**：`'\\'` 在 heredoc 中被转义吞掉导致语法错误。对策：路径拼接用 `os.sep`，复杂脚本先 Write 成 .py 再跑（老教训本轮重演一次）。
3. **写锚点前先查目标页**：编造/记错锚点会被断链门禁当场抓住（案例：写了不存在的 `e2008-12-23`，正确目标是编年史锚点 `c2008-12-23`）。查法：`grep -o 'id="…"' 目标页`。
4. **引语「已核实」必须账本可查**：冲刺修正了三处以讹传讹的引语标注——"I don't respect the SEC"（降级为 60 Minutes 广泛报道口径、逐字待考）、"I'm the reason OpenAI exists"（同上降级）、"Grok will actually answer…"（弃用，换成账本 e2023-07-12 章程句）。**引用前 `grep` primary/quotes/x-posts 三处对账**。
5. **PDF 打印文本默认中文模式**：headless Edge 出的 PDF 不含 data-en 内容，探针词必须用中文（案例：用 "unlimited money printer" 探针全 False，换中文全 True）。
6. **探针词与页面口径一致**：页面写「2300 亿」而非「2,300」——探针miss先怀疑自己拼写。
7. **修订历史数字会自己涨**：`build-revisions.py` 每次重跑会纳入新 commit（本轮 100→107），重跑后记得同步 DEVLOG 的数字。
8. **maxRuns 名额被空跑消耗**：定时任务曾有一次空触发白耗一个名额，导致整任务删除重建。再开定时任务时，提示词里要写「开始前先判定轮次，若无可做即输出一句退出」。

---

## 五、内容资产状态（v6.5.0 快照）

- **账本 67 条（2002→2026）**：候选序列已关闭（2010 Fremont/NUMMI 因三轮搜索无逐字引语放弃，Gruber 先例；记录在 v6.0.0 条目）。未来仅当出现**两源逐字**新事件才开新条目，全链流程见 DEVLOG 第六节。
- **争议五篇**：全部深化过（DMV 2025.12.16 认定 / 2026.02 起诉与停用 Autopilot 用语；NLRB 删帖令 2024.10.25 撤销（No. 21-60285）；欧盟 DSA 2025.12.05 €1.2 亿首罚）。新事实全部记入 EXPANSION.md 头部三条（v5.91/5.92/5.93 轮）。
- **分析页**：ai-strategy + deep-dive 01-05 全量重写（双语、锚点、引语、数据框齐备），与账本/财务/争议互链成网。
- **数字**：32 页 / 索引 169 七类型 / 语录卡 54（引文块 57、白名单豁免 3）/ CHANGELOG 160 / 修订历史 107 锚点 / git 172 commits / EPUB 121,762B 24 章 / 在线 https://a1310055634-sudo.github.io/musk-website/ 。

---

## 六、下一步建议（按优先级）

1. **「11 项」口径清理**（卫生，10 分钟）：全站 grep「11 项」改为 9 项或去掉数字（遵守无写死计数原则）。
2. **EN 模式全站走查**：本轮只系统核查过新写六页的 data-en，其余 26 页未复查——切 EN 模式逐页扫一遍漏翻与中英口径。
3. **sitemap.xml + robots.txt**：在线版已有 og，补站点地图即可提交搜索引擎（纯增量，不违反离线原则——本地 file:// 不加载任何联网资源）。
4. **第一手三页窄屏细调**：interviews/x-posts/documents 的 ≤480px（低优先级）。
5. **EPUB 目录锚点**：当前为纯文本章目录，可加页内跳转；build-epub.py 剥标签的架构下需在 strip 前保留标题 id。
6. **根目录清理**：`transform_sort.py`、`transform_v31.py` 为历史一次性脚本，可删。
7. **再开定时任务时**：沿用本日志第三节的作业模板 + 第四节坑位 8 的防空跑判据；提示词模板可参考被删任务 automation-5c9d67d2 的结构（轮次判定表 + 固定流程 + 失败协议 + 纪律）。

---

## 七、快速命令卡

```bash
python tools/verify.py              # 9 项体检（每轮必跑，全绿才提交）
python tools/build-search-index.py  # 重建检索索引（七个内容页变动后）
python tools/build-ledger-timeline.py  # 账本变动后重建页顶时间轴
python tools/build-revisions.py     # 从 git log 重建修订历史（数字会涨，同步 DEVLOG）
python tools/sync-changelog.py      # CHANGELOG.md → changelog.html
python tools/build-epub.py          # EPUB 打包（每轮必跑，满足新鲜度门禁）
python -m http.server 8765          # 本地预览 http://127.0.0.1:8765
```

（完。本文件由 17 轮冲刺收官后的主会话撰写，2026-09-28。）
