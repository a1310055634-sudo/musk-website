## v10.6.0 — 2026-10-02 · V10-15 N06/15：早期年代 II——文档馆补空（+1 份 DEFM14A 回避记录）

**主题包成果（V10-15 N06 · 第一手信息线）**
- **+1 份入册（文档 18→19，索引 319→320）**：**d2016-10-12**「SolarCity Form DEFM14A（合并委托书 · 马斯克回避表决记录）」——EDGAR 备案 0001193125-16-736379（SolarCity Corp CIK 1408356，被收购方备案），「Background of the Merger」章三段逐字摘录：①董事会回避决定（evaluation/negotiation/approval 全回避+二人不在场审议权）②执行（recused themselves and left the meeting→0.122-0.131 换股比初步提案）③终局（缺席已回避下批准合并协议「fair to, advisable and in the best interests」）——马斯克关联交易治理争议的第一手程序证据。doc-article 模板三段 EN+zh 对照。
- **其余候选处置（如实留档）**：2016-04-21 年度委托书经全文检索无 recusal 措辞（常规关联披露）不立；2009–2010 Tesla 博客存档（tesla.com Akamai/web.archive TLS 双受限）与 2013 爬坡信（需媒体双源）留档 EXPANSION，重验条件不变。
- **检索细节**：2016 合并委托书在**被收购方 SolarCity（CIK 1408356）**而非 Tesla 名下——首次 CIK 检索误中匹兹堡同名公司，经公司名搜索修正（坑：按公司简称猜 CIK 不可靠）。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 320）；CDP 探针 tools/v10n06-probe.js 8/8（19 卡/三段逐字/双语对照/meta 三徽标/时间序/检索 recuse 命中/390 两处零溢出）；版本三件套 10.5.0→10.6.0（**bump 脚本重构为自动前滚版**——三步法代码化，彻底告别手动档位坑）；EPUB 重跑（225,293 B）。本轮仅本地提交，不推送。


## 工程记录

- 集成断言三修（documents 无 legacy 条目 18=18；插入锚 d2017 不存在改 d2018-08-07；after 计数 18+1=19）。
- bump 脚本重构为自动前滚版（v10n06-bump.py：运行后自动把正则滚到 NEW）——五轮档位坑的终局解。
- 账本回填用 Write 工具（N05 教训执行）。

## 提交

- 成果提交：`[V10-15 N06]`（本地，不推送）；第二提交：账本回填+revisions+EPUB 重刷。
