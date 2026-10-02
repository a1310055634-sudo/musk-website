# 待发布清单 v2 · RELEASE CHECKLIST v11.0.0（V10-15 收官）

生成：2026-10-02（N15 收官轮）。**本清单只读不执行——推送由用户自行决定与操作。**
本清单合并并取代 v10.0.0 时的 RELEASE-CHECKLIST-v10.md（该文件仍保留供追溯）。

## 一、待推内容

- **范围**：`24020fe..HEAD`（V8 R10 收官 → V10-15 N15 账本收官）
- **数量**：以 `git rev-list --count 355fc0d..HEAD` 实时输出为准（N15 收官时应为 **80±**）
- **内容构成**：V8 十轮（v7.1.0→v8.0.0）+ V9-20 二十轮（v8.1.0→v10.0.0）+ V10-15 十五轮（v10.1.0→v11.0.0），合计 **45 轮**、版本阶梯 33 档。

## 二、一条推送命令

```
git push origin main
```

（当前 origin/main = `355fc0d`，v7.9.0 时代。推送为 Fast-forward，无冲突风险。）

## 三、推送后 1–3 分钟 Pages 验证步骤

1. `curl -s https://a1310055634-sudo.github.io/musk-website/VERSION` → 应输出 **11.0.0**
2. `curl -s -o /dev/null -w "%{http_code}" https://a1310055634-sudo.github.io/musk-website/resources.html` → **200**（44→49 时代的资源页）
3. 专题页抽查 200：`survival-2008.html` / `timeline.html` / `capital-evolution.html` / `documents.html` / `interviews.html`
4. span 抽查：`curl -s .../index.html | grep -o 'site-version-val">[^<]*'` → **11.0.0**
5. 内容抽查：`documents.html` 应含「诉讼证物」4 封（$1B 承诺/控制权/最终稻草/Agrawal）；`interviews.html` 应含「freaking cool」（i2021-09-28）；`events.html` 应含 16 档案（OpenAI 弧线/xAI 线）。

## 四、已知事项（推送前知悉）

- **本地终验全绿**：verify.py 9/9（38 页/索引 354）；全站终检探针 16/16（主路径六步+双语+file:// 离线+114 视口组合零溢出+print）。
- **引语复核声明已在站**（primary+quotes 双语，2026-10）：镜像来源条目已逐字机核；财报会人工抽样 2/2 吻合；非镜像来源条目 101 块已在 qa/v10-15/round-03/unmatched-itemized.tsv 逐条注明原因（立条时均经逐字源核实）。
- **tesla.com 全站与 SAE J3400 本机不可核活**（Akamai/JS 壳）——资源卡如实注明核活路径；EXPANSION 有重验条款。
- email 库 47 封已全部有归宿（立条 10+在册 1+留档候选 30+不立 2，见 EXPANSION N09 注记）。

## 五、后续

- **45 轮三计划全部收官（v7.1.0 → v11.0.0）**。下次触发按 V10-15-PROGRESS.md 收官规则**静默退出**——不再有计划内轮次；若要新计划需用户另行下发任务书。
- 全部交接入口：DEVLOG.md「V9-20 交接要点」+「V10-15 交接要点」+ 两份账本 + qa/ 证据目录。
