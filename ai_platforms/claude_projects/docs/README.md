# docs/ — 方法论 & 一等参考文档

## 内容概览

| 文件 | 类型 | 给谁看 | 长度 |
|------|------|-------|------|
| [PLAN_V2.md](PLAN_V2.md) | 执行计划 | 复盘者, 想理解"怎么做到这里" | 1852 行 |
| [RETROSPECTIVE_V2.md](RETROSPECTIVE_V2.md) | 复盘 (Rule C 产物) | 下个类似项目的负责人 | 7 章 |
| [rag_decay_curve.md](rag_decay_curve.md) | 一等数据产物 | Phase 7 RAG 设计者 | 7 数据点 + 4 段跨批观察 + 结论 |
| [phase7_handoff.md](phase7_handoff.md) | 向下游交接 | Phase 7 启动时 | 6 actionable + 5 问题 + 5 步待办 |
| [capacity_research.md](capacity_research.md) | 容量调研 | 任何要推高 capacity 的人 | 200K 假设修正记录 |

## 阅读顺序建议

**想接 Phase 7?** 按这个顺序 (总 < 30 分钟):
1. [phase7_handoff.md](phase7_handoff.md) §0 TL;DR + §3 6 条 actionable
2. [rag_decay_curve.md](rag_decay_curve.md) 结论段 + 关键发现
3. [RETROSPECTIVE_V2.md](RETROSPECTIVE_V2.md) §3 关键决策复盘 (5 条)

**想复盘这次项目?** 按这个顺序:
1. [RETROSPECTIVE_V2.md](RETROSPECTIVE_V2.md) 全文
2. [PLAN_V2.md](PLAN_V2.md) 挑关键阶段段细读
3. [../dev/evidence/_phase_summary.md](../dev/evidence/_phase_summary.md) 执行时间线

**想推高 capacity?**
1. [capacity_research.md](capacity_research.md)
2. [rag_decay_curve.md](rag_decay_curve.md) §3 Phase 7 insight #2 (推高 ROI)

## 关于路径引用

[PLAN_V2.md](PLAN_V2.md) 和 [RETROSPECTIVE_V2.md](RETROSPECTIVE_V2.md) 头部有 "post-reorg note" — 内部路径引用保留 reorg 前语境 (如 `output_v2/xxx.md`), 当前实际位置见各文件头的映射表或 [../dev/README.md](../dev/README.md).

[rag_decay_curve.md](rag_decay_curve.md) 和 [phase7_handoff.md](phase7_handoff.md) 路径已更新为 reorg 后状态.

---

*更新: 2026-04-20 晚 reorg.*
