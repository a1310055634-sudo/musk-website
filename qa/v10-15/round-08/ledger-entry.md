## 第 8 轮工作记录（N08 email 库消化 I）— complete（2026-10-02）

- **+4 份入册（文档 19→23，索引 323→327，全部「诉讼证物」口径）**：d2015-11-22（OpenAI $1B 承诺：starting with a $1B funding commitment…cover whatever anyone else doesn't provide + 比 $100M 大的口径逻辑）/ d2017-09-13（控制权：unequivocally have initial control…but this will change quickly）/ d2017-09-21（final straw：不再资助 until 结构承诺）/ d2022-04-09（致 Agrawal 三连短信：What did you get done this week→not joining the board→will make an offer）。
- **双源核验（全部 2026-10-02 逐字吻合）**：①muskvsaltman.com 法庭文件存档（Musk v. Altman 公开文件）②OpenAI 官方博客 2024-12 公开文件+WaPo ③techemails.com+FindLaw 2026 法院判决书原文引用（最强第二源）④Delaware 衡平法院 2022-09 解封文件（BBC/BI 引用）。
- **email 正文提取管线打通**：镜像 /email/{id} 详情页为 Next.js SSR、curl 拿不到正文（仅 meta）——**web_reader（JS 渲染）可取正文**，且镜像自带法庭 Exhibit 标注（「诉讼证物」口径的第一手标注源）——N09 沿用。
- 其余 39 封留 N09（Tesla 冲刺信/SpaceX 余量/Twitter 收购私信其余件）。
- **验证**：verify 9/9（38 页/索引 327）；探针 7/7（tools/v10n08-probe.js 端口 9394）；版本三件套 10.7.0→10.8.0（自动派生版）；sync-changelog 217 条；EPUB 228,004B；修订史 215 锚点（文档 23 入轨）。
- **提交**：成果 `4b1b411`（v10.8.0）；本回填+revisions+EPUB 重刷为第二提交。
- **下一轮预告**：N09 email 库消化 II（v10.9.0）——Tesla 生产冲刺信（soufflé/sabotage/record quarter/go all out 等）/ SpaceX 全员信余量；同双源纪律；完成后 email 库 47 封全部有归宿（立条/弃收/留档）。
