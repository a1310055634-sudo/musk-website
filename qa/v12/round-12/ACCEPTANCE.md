# V12-20 R12 验收 · 深读新篇 II：deep-dive-07《Robotaxi 落地考》（v11.13.0）

日期：2026-10-07 · 模式：纯本地（无 push/remote 写）

## 择题（任务书二选一）
- **开工：Robotaxi 落地考**（素材扎实：账本逐字×2+R02 四卡逐字+事件档 7 材料）。
- **落选：Musk 政治参与 2024–2026**——连同已探明素材写 EXPANSION 候选池（事件档 e2024-07+三镜像帖 200 实测+178+ 帖池检索锚，待专属轮次）。

## 成果（deep-dive-07.html，18.3KB，逐字克隆 dd05 骨架）
五章：①欠账的形状（2016–2024 承诺簇+**promises 五案为何不设 robotaxi 案的核查发现**）②We,Robot（Cybercab 逐字引语）③奥斯汀弧线（四帖逐字，含 p2026-01-22 "no safety monitor in the car"）④一周年口径（e2026-07-22，问题从「是否」变「多快」）⑤**指控·回应·本站核查三段体**（controversy 体例：「两半都真、分别可核」）。

## promises 互链（任务书条件句）
「若有 robotaxi 承诺条目则互链」——实测 promises.html 无 robotaxi 专属卡（五案=2008 融资/2014 专利/2017 生产地狱/2018 私有化/2025 薪酬包，FSD/robotaxi 关键词 0 命中），如实不造互链；以 s3 全览段互链+「制度性排除」作为核查发现写入正文。

## 七件接入
①site-nav 注册 41/41（五组 40 页）②索引深读长文 5→10（dd06+dd07 十章入册）③verify n_dd 正则扩展 ④新页含 span（**站点 span 16→17**）⑤sitemap 未动 ⑥build-longread 幂等 ⑦互链 6 处 fetch 验证（primary×2/x-posts×3/events/promises）。

## 验证
- verify.py 9/9（终态：索引 408=124+37+51+44+5+64+4+20+49）；**CDP 探针 18/18**（端口 9358：文件级 4/新页渲染 9（三段体/逐字×2/双语/aria-current/版本戳）/互链跨页 4/390）。
- QA 截图 2 张：desktop-dd07.png / desktop-dd07-s5.png（三段体节）。

## 工程记录（如实）
- 英文转义引号 `\\"` 会以字面反斜杠入 HTML——写入前改弯引号（R10 教训的变体）。
- 误执行 v12r11-bump 一次（同值无实害），正确 bump 为 v12r12-bump（17 span 断言）。
- promises.html 无 robotaxi 卡为核查发现而非遗漏——五案制只收「有明确日期下限的可判案」。

## 版本
- 11.12.0 → 11.13.0（17 span）。
