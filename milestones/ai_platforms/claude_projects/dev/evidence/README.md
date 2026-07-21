# v2 Evidence 三层体系

| 层 | 文件 | 写入频率 |
|----|------|---------|
| L1 状态 | `_progress.json` | 每 Step 完成 |
| L2 轨迹 | `trace.jsonl` (append-only) | 每事件实时 |
| L3 证据 | `stage_v2.X_*.md`, `batch_NN_*.md` | 每 Stage/Batch 完成 |

子目录:
- `checkpoints/` 用户互动归档
- `subagent_prompts/` 完整 prompt 归档 (executor + reviewer)
- `failures/` 失败 attempt 归档 (规则 B 强制)
- `rag_decay_observations/` 每阶段 RAG 衰减观察

参照: v1 `output/evidence/README.md` 同结构 + PLAN_V2.md §1 P1-P10
