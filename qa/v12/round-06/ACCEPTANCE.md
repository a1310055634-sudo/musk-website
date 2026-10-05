# V12-20 R06 验收 · email 库双源核验 I（v11.7.0）

日期：2026-10-06 · 模式：纯本地（无 push/remote 写）

## 成果
- documents.html 新立 4 条 doc-article（27→31）：
  1. **d2022-04-20 埃里森十亿美元承诺**——镜像原文（"Any interest…/Yes … of course 👍/Roughly what dollar size…/A billion … or whatever you recommend"）；第二源=Twitter v. Musk 法庭披露件（TIME/WaPo 逐字转载）+SEC 2022-05-05 修订备案（71.4 亿新股权承诺含 Ellison 10 亿，Reuters/CNBC 报道）。与账本 e2022-04-20 互链。
  2. **d2022-11-09 Twitter 首封全员信**——镜像原文（"Remote work is no longer allowed, unless you have a specific exception. […] Starting tomorrow (Thursday)… 40 hours per week"）；第二源=CNBC 2022-11-10 全文页（镜像页脚自带链接）+Gizmodo/Campaign 等转载。
  3. **d2023-01 "This is a bait and switch"**——镜像原文；**口径如实标注：庭审宣誓作证当场追述（2026-04-29 Day 2），原始短信档未单独公开**；第二源=庭审证据+Business Insider/NYT/CNBC 逐字报道。月精度日期（镜像 2023-01-23=微软 $10B 公告时点）。
  4. **d2023-02 "You're my hero … it really fucking hurts"**——镜像原文（Altman+Musk 两条）；第二源=2026-01 解封展品+Business Insider「9 Revelations」等逐字引用；Musk 回复 BI 解封版更长（含道歉半句），注释如实区分。
- 归账：bret-taylor（"Please expect a take private offer"）=在册复用（e2022-04-09 现场段已覆盖对话），不新立。N09 留档 30 封消化 5 封（余 25 待 R07）。

## 双源核验链路
- 镜像底本：elonmuskarchive.org/email/{id} 详情页 SSR HTML（**带浏览器 UA curl 直取成功**，26KB 级；裸 curl=404 壳；web_reader 渲染亦可）——正文在 Next.js RSC payload，tools/v12r06-extract.py 抽取。
- 四封镜像存档：qa/v12/round-06/sources/*.html。
- 镜像页脚自带第二源链接：法庭展品（Ellison）/Musk v. OpenAI trial testimony（bait-and-switch）/unsealed exhibit+hardresetmedia（my-hero）/CNBC（first-email-remote）。

## 验证
- verify.py 9/9 全绿（终态：版本一致性 11.7.0/检索索引 377=124+31+51+44+5+53+4+16+49/时间轴/语录卡 107+豁免 2/修订历史/CHANGELOG 首条/EPUB 新鲜度）。
- **CDP 探针 24/24**（tools/v12r06-probe.js，端口 9352）：
  - 文件级 7：索引含四新 id/一手文档计数 31/总条数 377/版本戳 app.js 11.7.0
  - 桌面结构 5：doc-article=31/四条渲染/五件套/Permalink/doc-foot（见下「首跑修正」）
  - 逐字与口径 6：四条英文逐字+双语 CJK+口径戳 2026-10-06 核验
  - 时序与互链 5：2022-04 段（04-11→04-20→04-25）/2022-11 段（10-27→11-09→11-16）/2023 段（11-16→2023-01→2023-02→2023-04-05）三段邻居断言+互链 e2022-04-20 真实存在+d2023-01→d2023-02 站内互链
  - 390 溢出 1：scrollWidth≤clientWidth
- QA 截图 2 张：desktop-ellison.png（1440）/mobile-390-openai2023.png（390）。

## 首跑修正（如实记录）
- 探针首跑 23/1：挂「页面版本戳=11.7.0」——**documents.html 历史上无站点页脚**（无 site-version-val span，页尾结构=定制 doc-foot），15 span 口径从未含它，系探针断言写错非站点回归；断言改为验证 doc-foot 存在后 24/24。
- 集成断言两次拦截（写入前，页面未受损）：①permalink 计数裸 `href="#id"` 被站内互链虚增（d2023-02），改 `href="#id" title=` 特征；②口径戳措辞统一断言（③条为"镜像如实标注"句式），改统一日期戳 `2026-10-06 核验` 计数。
- build-search-index 守护断言 expected 一手文档 27→31 同步更新（生成器内硬编码期望值属每轮随增量更新项）。

## 版本
- 11.6.0 → 11.7.0（VERSION/app.js/15 span，bump 打印计数在案）。
