## v10.8.0 — 2026-10-02 · V10-15 N08/15：email 库消化 I——四封诉讼证物信（文档 19→23）

**主题包成果（V10-15 N08 · 第一手信息线）**
- **+4 份入册（文档 19→23，索引 323→327，全部「诉讼证物」口径注明）**：
  ①**d2015-11-22** OpenAI 创立期邮件「$1B 承诺」（"I think we should say that we are starting with a $1B funding commitment. This is real. I will cover whatever anyone else doesn't provide." + 比 $100M 大以免「听起来毫无希望」）——Musk v. Altman 反驳证据；
  ②**d2017-09-13** 控制权邮件（"I would unequivocally have initial control of the company, but this will change quickly."）——OpenAI 2024-12 官方博客公开文件（WaPo 同步报道）；
  ③**d2017-09-21**「最后一根稻草」（"This is the final straw. Either go do something on your own or continue with OpenAI as a nonprofit. I will no longer fund OpenAI…"）——**2026 联邦法院判决书原文引用**（FindLaw 在档）+ techemails.com 存档，三源；
  ④**d2022-04-09** 马斯克致 Agrawal 三连短信（"What did you get done this week? … I'm not joining the board. This is a waste of time. Will make an offer to take Twitter private."）——Delaware 衡平法院 2022-09 解封证物（BBC/Business Insider 逐字引用）。
- **双源核验**：每封=镜像底本（elonmuskarchive.org/email，web_reader 渲染——curl 拿不到 SSR 正文，正文在客户端流；镜像自带法庭 Exhibit 标注）+ 独立第二逐字源（muskvsaltman.com 法庭文件存档 / OpenAI 官方公开 / FindLaw 判决 / BBC-BI 报道），2026-10-02 核验逐字吻合。
- 其余 39 封（Twitter 收购私信其余件/Tesla 冲刺信等）留 N09。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 327）；CDP 探针 tools/v10n08-probe.js 7/7（23 卡/四信逐字/诉讼证物口径/双语成对/时序/检索 final straw/390）；版本三件套 10.7.0→10.8.0（自动派生版 bump）；EPUB 重跑（228,004 B）。本轮仅本地提交，不推送。


## 工程记录

- **email 正文提取管线**：curl 拿到的镜像 /email/{id} 详情页为 Next.js SSR，正文不在 HTML（仅 meta）——**web_reader（带 JS 渲染）可取正文**，且镜像自带法庭 Exhibit 标注（Delaware Superior Court / Chancery 编号）——「诉讼证物」口径有了第一手标注。
- 双源核验记录：①1b-commitment ↔ muskvsaltman.com（法庭文件存档站）②initial-control ↔ OpenAI 官方博客公开文件+WaPo ③final-straw ↔ techemails.com+FindLaw 法院判决引用 ④agrawal ↔ Delaware 解封文件（BBC/BI 引用）。
- 集成脚本简化为「构造四卡+三处精确插入」。

## 提交

- 成果提交：`[V10-15 N08]`（本地，不推送）；第二提交：账本回填+revisions+EPUB 重刷。
