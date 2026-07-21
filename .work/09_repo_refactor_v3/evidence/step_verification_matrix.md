# 段6 验证矩阵 evidence (2026-07-21)

| # | 项 | 结果 |
|---|----|------|
| 1 | 双向 grep 零残留 | PASS — active 文件 0 旧路径; 残留命中全部为有意保留 (PROGRESS/MANIFEST 重构自述注记 + AGENT_GUIDE v1 历史行 + 08_v2 历史计划 + sdtm-rag 内历史 PLAN/DESIGN/evidence 存证); 反向 `ls branches` = No such file |
| 2 | 服务四联 | PASS — api {"status":"ok"} / ui 200 / neo4j 200 / `/api/ask` 真答 sources:15 (TV Required 中文答) |
| 3 | 管线实测 (静默指空强制检查) | PASS — `reconcile_meta.py` 8/8 锚: 63 域 / 1917 / 1523 / 1005 / 37939 / TAETORD→43 / VISITDY→36 / 裸 Order 1917 |
| 4 | pytest 复跑 | PASS — **525 passed, 0 failed** (17.3s; 迁移前 521, +4 = 旧布局下静默 skip 的测试现真跑) |
| 5 | subagent dry-run | (见 step_dryrun_agent.md) |
| 6 | push + CF | PASS — push OK (2380da4..f66d074 + tag pre-restructure-v3); prod 200 (/zh/); 本地同配置 build 过 (T9); **CF dashboard 最新构建绿 (用户确认 2026-07-21)** — release/→milestones/release/ 改动线上构建闭环 |
| 7 | git 状态 | 工作树净; 段级 commit 链完整; tag pre-restructure-v3 已推 |
