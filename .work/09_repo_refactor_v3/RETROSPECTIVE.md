# Repo Restructure v3 — RETROSPECTIVE (Rule C)

> 2026-07-21 · Tier 2 · branches/ 解散 → sdtm-rag 顶层 + milestones/ · 13 task 六段时序全 PASS
> spec `docs/superpowers/specs/2026-07-21-repo-restructure-v3-design.md` · plan `docs/superpowers/plans/2026-07-21-repo-restructure-v3.md`

## 1. 保留下来的做法 (下次重构继续用)

- **调研先行 + 破坏面地图**: 动手前 5 路并行只读调研 (结构/垃圾/引用/历史/散件), 把 launchd plist、venv shebang、parent-chain 深度锚、CF Pages 依赖、jp_delivery 零 git 保护这些"移动就炸"的点全部提前摸出。执行期间零意外事故。
- **v1/v2 方法论全套继承有效**: git mv 保历史 · 每段独立 commit 可 revert · tag 兜底 (取代 cp 备份) · sed 前先 grep 全量变体 · active/historical 二分 (历史叙述里的旧路径故意不改 + MANIFEST 总注记) · 全程禁 git stash。
- **危险目录先收编再搬**: jp_delivery (0 tracked 纯磁盘) 先原位 git add + commit 获得 git 保护, 再 git mv — 全程无裸奔窗口。
- **"静默指空"用实测闸住**: parent-chain 锚错了不 crash。验证矩阵强制 reconcile_meta 8/8 锚 + /api/ask 真答 + pytest 全量, 不以"服务活着"为准。事实证明必要 (见缺口 §2)。
- **服务迁移顺序锁死**: bootout → mv → venv 重建 (不搬) → plist 改写 → bootstrap → 四联验。停机 <30 分钟, KeepAlive 无限重启循环零发生。

## 2. 必须补上的缺口 (这次踩到/侥幸)

- **调研漏了 3 类深度锚, 执行期兜住**: ① `_smoke_batch_a/c.py` 的 `parents[5]` (调研只抓到 batch_b); ② **scripts/tests/ 11 个文件的 KB_ROOT parents[5]** — 调研断言 "tests 全部自锚安全" 是错的。后果实证了静默失败模式: 迁移后多数测试**静默 skip** 而非 fail (只有 3 个硬读文件的 FAIL 暴露)。修复后 525 passed > 迁移前 521 — **旧布局下就有 4 个测试在静默 skip 没人发现**。教训: 路径锚调研必须 grep 全量 `parents\[[0-9]\]` + 多连 `.parent` 机械穷举, 不能按目录类型推断"安全"。
- **grep 白名单的 `^./` 前缀陷阱**: 双向 grep 的排除模式带 `^./` 与 grep -rn 实际输出 (无 ./ 前缀) 不匹配, 白名单静默失效输出 141KB。先 `sed 's|^\./||'` 归一化再过滤。教训: 过滤管道先拿 3 行真实输出验证模式, 再上全量。
- **pytest `-q` 叠加 addopts 吞汇总行** (SP4 老坑二次踩): 本仓 pyproject `addopts=-ra -q` + 命令行 `-q` = verbosity -2, 汇总行消失。本仓跑 pytest 一律不带 `-q`。
- **PROGRESS.md 巨行是慢性病**: "轻量看板"纪律在行数上守住、单行长度上完全失守 (14.4K 单行 + 8 行 >2K)。根因: 每次收尾把细节堆进"最后更新"而不是只留指针。已重切 (117→64 行) 并在 CLAUDE.md 收尾规则中有对应闸 — **今后收尾时"最后更新"限一段 ≤600 字符, 细节只进 worklog**。

## 3. 关键决策复盘

- **sdtm-rag 提顶层 (D1 活跃 vs 成果二分)**: 正确。改动面大 (launchd/venv/21 处锚/文档 78 处) 但一次付清; 日常开发路径从 3 层缩到 1 层, 与"唯一活跃线"的实态一致。
- **release/ 进 milestones (D3, 用户选改 web)**: 执行顺利 — web 本地 build 一次过。风险 (CF dashboard watch paths 手动项) 被 release 冻结的事实钝化: 该目录不再变更, watch path 失配无实际触发面。
- **jp_delivery 全量收编 (D5)**: 10M (含 9M zip) 换永久 git 保护, 值。`.gitignore` 注释与现实矛盾的老问题一并消除。
- **eval 旧 run 删除线划在 ≤2026-06-20 且仅 run 输出**: 逐文件枚举 + 保留全部脚本/审查 md/题集/kgval/agg, 无一误删 (保留清单与 plan 预期逐项吻合)。"删除线按日期+类型双维划"比按目录粗删安全。
- **parent-chain 选机械改深度而非收敛重构**: 正确 — scope 可控, 行为等价可验。单点收敛 (config.py 统一 repo-root 发现 + 全部 import 它) 留 backlog, 值得做但不该混进迁移。
- **git gc 提前到段 0**: 146M 全松散 → 42.6M pack, 后续大规模 git mv/commit 显著变快。任何大迁移前先 gc 应成为惯例。
