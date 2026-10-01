# 待发布清单 · RELEASE CHECKLIST v10.0.0（V9-20 收官）

生成：2026-10-02（R20 收官轮）。**本清单只读不执行——推送由用户自行决定与操作。**

## 一、待推内容

- **范围**：`24020fe..HEAD`（V8 R10 本地版收官提交 → V9-20 R20 账本回填提交）
- **数量**：以 `git rev-list --count 355fc0d..HEAD` 实时输出为准（R20 收官时应为 41）
- **首尾提交**：
  - 最早：`24020fe` [V8 R10] 全站验收 v8.0.0 本地版
  - 最新：见 `git log --oneline -1`
- **内容构成**：V8 十轮第一手回捞（v7.1.0→v8.0.0）+ V9-20 二十轮（第一手扩充 R02–R09 / 资源板块 R10–R14 / 美术升级 R15–R19 / 收官 R20），版本阶梯 v8.1.0 → v10.0.0 每轮一档。

## 二、一条推送命令

```
git push origin main
```

（当前 origin/main = `355fc0d`，v7.9.0 时代。推送为 Fast-forward，无冲突风险。）

## 三、推送后 1–3 分钟 Pages 验证步骤

1. `curl -s https://a1310055634-sudo.github.io/musk-website/VERSION` → 应输出 **10.0.0**
2. `curl -s -o /dev/null -w "%{http_code}" https://a1310055634-sudo.github.io/musk-website/resources.html` → **200**（第 38 页首次上线）
3. 三个专题页 200：`survival-2008.html` / `timeline.html` / `capital-evolution.html`
4. span 抽查：`curl -s .../index.html | grep -o 'site-version-val">[^<]*'` → **10.0.0**
5. 浏览器实访资源页：36 卡渲染、分类筛选可用、`?q=` 检索命中类型「社区资源」

## 四、已知事项（推送前知悉）

- 本地验证全绿：verify.py 9/9（38 页/索引 318）；全站终检探针 15/15（主路径/双语/file:// 离线/114 视口组合零溢出/print）。
- tesla.com 全站与 SAE J3400 在本机不可核活（Akamai/JS 壳），资源卡如实注明核活路径——线上环境若可直访，可按 EXPANSION.md 重验条款补录。
- 站内「引语复核声明」尚未上站（属 V10-15 N03 交付）——当前口径以各账本「核实来源留档」为准。

## 五、后续

- V10-15 内容精修计划已开工（N01–N15，终点 v11.0.0）：推送与否不影响其本地推进；v11.0.0 收官时将输出「待发布清单 v2」（合并累计范围）。
