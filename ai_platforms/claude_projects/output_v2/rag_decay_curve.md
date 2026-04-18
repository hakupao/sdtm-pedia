# RAG 质量 vs 规模曲线 (Phase 6.5 v2 一等产物)

> 目标: 建立 Claude Project RAG 质量随集合规模变化的曲线
> 用途: Phase 7 RAG 拓扑设计参考 + 决定是否在 Phase 6.5+ 推到 70%
> 触发: capacity_research §6.3 第 2 条疑点 ("RAG 检索质量随集合增大如何衰减?" 未实测)

## 数据点

| 阶段 | tokens | 文件数 | Capacity % (UI 实测) | T1-T8 PASS | T9-T20 PASS | 平均答题精度 (主控判) |
|------|-------|-------|---------------------|-----------|-----------|----------------------|
| v1   | 192,036 | 11 | 12% | 8/8 | N/A | baseline |
| v2.1 | TBD | 11 | TBD | TBD | T9-T12 TBD | TBD |
| v2.2 | TBD | 12 | TBD | TBD | T13-T14 TBD | TBD |
| v2.3 | TBD | 13-14 | TBD | TBD | T15-T16 TBD | TBD |
| v2.4 | TBD | 14-17 | TBD | TBD | T17-T18 TBD | TBD |
| v2.5 | TBD | 16-19 | TBD | TBD | T19-T20 TBD | TBD |

## 观察

(每阶段后追加 1-3 句关键观察)

## 结论 (终态后填)

- v2 终态推到 X% 的 RAG 质量是否仍 PASS?
- 衰减拐点 (如有) 在 ~Y% capacity?
- 对 Phase 7 的 actionable insight?
