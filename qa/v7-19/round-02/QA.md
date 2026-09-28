# 第 2 轮验收记录 · 图片与纪实素材体系（v6.7.0）

日期：2026-09-29 · 分支 visual-v7-19rounds · 提交：[V7-19 R02]

## 本轮要解决的问题

全站图片无来源与许可记录（可追查性为零）；仅 3 张真实图片、题材单一；公司版图页纯文字无视觉锚点；falcon-heavy.jpg 来源不可查证；图片缺统一的尺寸声明与加载策略。

## 实际完成的改动

1. **溯源**：新建 tools/trace-assets.py（Commons API + 感知哈希比对）。portrait.jpg 与 tesla-factory.jpg 均**逐像素命中** Commons 原件（diff=0），拿到作者与许可；falcon-heavy.jpg 两轮检索（26 候选）无精确匹配 → 判定来源不可追查，整体替换为 SpaceX 官方 CC0 同题材图（双助推器同步着陆，2018），文件名不变（尺寸同为 960×1440，布局零扰动）。
2. **新增素材 4 张**：starship-catch.jpg（CC BY 2.0 Jurvetson，2024-10-13 第五飞塔捕，与账本 e2024-10-13 互证）、x-hq.jpg（CC BY-SA 4.0，2022-11 收购时点）、cybertruck.jpg（CC0，Denver 展厅）、falcon 替换图（CC0 SpaceX）。许可元数据存 assets-meta/*.json。
3. **加工**：tools/prep-assets.py 统一压缩（q80-85）、裁切（x-hq 上部 3:2 保标牌、cybertruck 偏移 3:2 对车头、portrait 派生 3:2 横版与 4:5 竖版封面备用图）。过程中发现并修复越界裁切黑边缺陷（评审缩略图 ≠ 原图尺寸）。
4. **接入**：companies.html 三家卡配图 + 署名行（xAI/Neuralink/Boring 无可查素材，诚实保持文字卡）；首页封面补署名行（中英双语，合并了原有 figcaption 避免重复）+ fetchpriority=high；indepth 图注补全署名、修正 alt 与实拍不符（「外景」→「总装线」）、Falcon 21:9 框 object-position 底部取景；全站 img 加 height:auto 防拉伸。
5. **清单**：ASSETS.md（每图来源页/作者/许可/核实日期/加工/用途/署名落点）；README 挂入口。

## 检查了哪些页面和交互

- 页面：index / companies / indepth（桌面 1440×900、手机 390×844）；indepth 另拍全页高窗图验证 Falcon 取景。
- 交互（tools/r02-interact.js，headless Chrome + CDP）：EN 切换后署名行正确切换；三张卡图 loading=lazy + figcaption 齐备 + 渲染比例 3:2；indepth Falcon 滚动触发加载 complete=true（960×1440）。
- 溢出诊断（tools/r02-probe.js，真 390px CDP 仿真）：scrollWidth=390、零越界元素。**此前 qa-shots 手机截图「文字裁边」为 headless Chrome 最小窗宽 500px 伪影**（截图按 500px 渲染再裁存），非站点缺陷——改前改后截图均受影响，对照可证。

## 测试结果及发现的问题

- verify.py 9 项全绿（v6.7.0）；node --check 通过；9 张改后证据图 PIL 非空白抽查全过。
- 发现并当场修复：① 封面署名行与原 figcaption 重复（合并为单行）；② 越界裁切黑边；③ 截图解码竞态致肖像白框（复拍即好，已有协议预案）。
- 已知伪影（非缺陷）：qa-shots 手机档 500px 最小窗宽；后续手机打磨（R16）应改用 CDP 仿真截图（r02-probe.js 模式已验证可用）。

## 是否完成本轮

完成。桌面/手机/双语/离线（无任何外链资源，全部素材本地化）验收通过，来源与许可全部可追查。

## 本轮新增事实的来源记录

全部图片许可信息见 ASSETS.md；事实性图注（Starship 第五飞塔捕 2024-10-13、Falcon Heavy 演示飞行 2018-02、X 收购 2022-10-27 交割）与本站账本既有锚点（e2024-10-13 等）互证，未新增未经核实的事实陈述。
