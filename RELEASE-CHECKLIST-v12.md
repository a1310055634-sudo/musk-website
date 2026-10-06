# RELEASE-CHECKLIST-v12.md · 待发布清单（纯本地，未推送）

生成：2026-10-06 · R20 终章 · 版本 **v12.0.0** · 分支 main · 工作区干净

## 1. 待推提交

- **总数：139 个本地提交未推送**（`git log --format='%h' origin/main..HEAD | wc -l`）
- **哈希范围**：origin/main（`e83e26d` 之后）→ 本地 HEAD `4f4113b`
- 覆盖：V9-20 收官段（v11.1.0 前 45 轮遗产）+ V10-15 + **V12-20 全部 20 轮**（R01 基建→R20 终章）
- 首个待推提交可用 `git log --reverse --format='%h %s' origin/main..HEAD | head -1` 复核

## 2. 推送（一条命令，用户执行）

```
git push origin main
```

（红线说明：V12-20 全程纯本地零 remote 写操作，此命令留给用户决定何时执行。）

## 3. 推送后 1–3 分钟 Pages 验证

1. `curl -s https://a1310055634-sudo.github.io/musk-website/VERSION` → 期望输出 `12.0.0`
2. 三个关键新页 200：
   - `curl -s -o /dev/null -w "%{http_code}" https://a1310055634-sudo.github.io/musk-website/resources.html` → 200（54 条）
   - `…/deep-dive-06.html` → 200（xAI 三年志）
   - `…/deep-dive-07.html` → 200（Robotaxi 落地考）
3. span 抽查（版本三件套线上一致）：
   - `curl -s https://a1310055634-sudo.github.io/musk-website/ | grep -o 'No. <span class="site-version-val">[^<]*'` → `No. <span class="site-version-val">12.0.0`（刊头期号）
   - 任一内页 `grep -c 'site-version-val">12.0.0'` ≥1
4. sitemap 抽查：`…/sitemap.xml` 含 `deep-dive-06.html`（39 URL）
5. 时效件抽查：`…/documents.html` 含 `d2026-06-12`（SpaceX 424B4）；`…/events.html` 含 `e2024-07`（America Party 正反并陈）

## 4. 发布前已知事项（如实）

- **未推提交含 V9-20/V10-15 遗产段**：若远端 Pages 当前显示 v11.1.0 之前的旧版，推送后全站一次性跨 139 提交，版本跨度大属预期。
- preview-v12.html 随仓推送但 sitemap/revisions 双排除（开发试衣间口径，V9-20 R20 既定）。
- revisions.html 保持 noindex。
- EPUB 254,462B / 24 章随推送更新（下载口径 `musk-inc.epub`）。
- 深色主题不存在（复古纸面单主题=美术基线）；R17 dark hatch 覆盖块为死代码（无害）。

## 5. 完成条件八项核验（R20）

| # | 条件 | 状态 |
|---|---|---|
| ① | 20 轮全验收 | ✓ R01–R20 账本全 complete |
| ② | 15 个月 X 帖断代补齐+缺口盘点 | ✓ 34→44；缺口清单 v4（EXPANSION 卷首） |
| ③ | 美术四轮截图可辨 | ✓ before/after 47 张+像素 diff 全 DIFF |
| ④ | 桌面/手机/中英/离线 | ✓ 终检探针 20/20（含 file:// 三断言） |
| ⑤ | 旧页锚点保留（断链零） | ✓ verify「断链」项绿 |
| ⑥ | 事实/资源/图表来源清楚 | ✓ 双源注记/三路法/线宽=生成器值断言 |
| ⑦ | 产物/版本/交接一致 | ✓ 三件套 12.0.0+期号+页脚+EPUB 同步 |
| ⑧ | 本地 v12.0.0 就绪+待发布清单 | ✓ 本文件 |
