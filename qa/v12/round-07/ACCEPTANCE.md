# V12-20 R07 验收 · email 续 + 文档馆近年化（v11.8.0）

日期：2026-10-06 · 模式：纯本地（无 push/remote 写）

## 成果（+6 条，文档馆 31→37）
1. **d2018-08-12 PIF 鲁梅延短信**（"You are throwing me under the bus"）——镜像原文（五段对话体逐字）；第二源=funding secured 证券集团诉讼披露展品（镜像页脚自带 Fortune 2022-04-25 报道链接）。互链 e2018-08-07。
2. **d2022-03-26 Dorsey 协议短信**（"A new platform is needed. It can't be a company."）——镜像原文（对话体逐字，"Super interesting idea" 完整版经长串抽取修复）；第二源=Twitter v. Musk 法庭披露展品（danluu.com 披露件汇编）。互链 e2022-03-26。
3. **d2025-09-17 Tesla 万亿薪酬包 proxy**——EDGAR 直取（DEF 14A，备案号 0001104659-25-090866）：12 档市值里程碑（首档 $2T→末档 $8.5T）+$400B EBITDA+多年任职绑定，原文三段。互链 e2025-11-06。
4. **d2026-01-29 Tesla 10-K FY2025**——EDGAR 直取（备案号 0001628280-26-003952）：AI 公司定义句（FSD/Robotaxi/Optimus）+Technoking 关键人风险句。
5. **d2026-06-12 SpaceX 424B4 IPO 定价书**——EDGAR 直取（备案号 0001628280-26-042639，Registration 333-296070）：555,555,555 股 × $135.00=约 750 亿美元募资、Nasdaq+Nasdaq Texas 双上市 SPCX、A/B 双层 10:1、受控公司豁免、募资用途首位=AI 算力。**站内此前对 SpaceX 上市零覆盖，本轮补上最大缺口。**
6. **d2026-06-22 SpaceX senior notes 8-K**——EDGAR 直取（launch 044489/pricing 044955）：五档 2031–2056 合计 250 亿美元（5.35%–6.65%），8-K 链三连（launch FD 披露→pricing→closing）。

## 环境探测记录（如实）
- **xAI 披露**：EDGAR full-text search "xAI Holdings" 56 命中经核为 SpaceX 相关文件（333-296740 注册号即 SpaceX 2026 IPO 注册）；x.ai 关联实体多个 CIK（0002023090 等 5 个）存在但无可立条披露文书——如实记 EXPANSION，不硬凑。
- **Starship 官方更新信**：SpaceX 自 IPO 后披露通道已转为 SEC 备案（8-K/10-Q），官网无 2025–2026 独立更新信——EDGAR 备案即近年化最优锚，任务书目标以 424B4/8-K 达成。

## 验证
- verify.py 9/9 全绿（终态：版本一致性 11.8.0/检索索引 383=124+37+51+44+5+53+4+16+49/时间轴/语录卡/修订历史 250 锚点/CHANGELOG 首条/EPUB 新鲜度）。
- **CDP 探针 25/25 一次全绿**（tools/v12r07-probe.js，端口 9353）：文件级 9（六新 id 入索引/一手文档 37/总数 383/版本戳）/结构 4/逐字 6（六条英文锚句）/双语+口径戳 2/时序 12 邻居链+互链 3/390 溢出 1。
- QA 截图 2 张：desktop-spcx-424b4.png / mobile-390-pif.png。

## 首跑修正（如实记录）
- 集成断言 1 挂：口径戳全页计数——基线已含 R06 的 4 个"2026-10-06 核验"，加本轮 6 个=10，非 6（跨轮累计型断言须计基线）。
- pricing 8-K 首取 347B（404 壳）：accession 目录 index.json 查得真实文件名 spcx-pricing8xk.htm 后重取成功。

## 版本
- 11.7.0 → 11.8.0（VERSION/app.js/15 span，bump 打印计数在案）。
