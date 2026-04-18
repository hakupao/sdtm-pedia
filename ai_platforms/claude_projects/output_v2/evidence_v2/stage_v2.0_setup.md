# Stage v2.0 — Setup

> 完成日期: 2026-04-18
> Tasks: A1-A3
> Commits: c7e558c (A1 baseline) + 9ce83bc (A2 skeleton) + (A3 pending)

## 输入
- v1 baseline (`output/` 11 文件, md5 全部与 output_v1_baseline 一致, A1 Step 3 验证 11/11 PASS)
- knowledge_base/ (只读, 未触)

## 产出
- `output_v1_baseline/` 11 文件 + README (A1, md5 与 output/ 全部一致)
- `output_v2/` 9 文件 (8 v1 不变 00/01/03-08 + 1 system_prompt_v2)
- `output_v2/evidence_v2/` 三层体系骨架 (_progress.json + trace.jsonl + 4 子目录 + README)
- `scripts_v2/` 空骨架 (.gitkeep)
- 5 份元文档骨架:
  - `output_v2/upload_manifest_v2.md`
  - `output_v2/test_results_v2.md` (T1-T20 占位)
  - `output_v2/rag_decay_curve.md` (v1 baseline 已填, 192K / 11 / 12% / 8/8)
  - `output_v2/evidence_v2/README.md`
  - `output_v2/evidence_v2/_progress.json`

## 复核
- A1 Step 3: 11/11 PASS (baseline md5)
- A3 Step 1: 9/9 PASS (output_v2 copied files md5, 含 system_prompt→system_prompt_v2)
- find output_v2 -type f: 15 files (9 v1 不变 + 5 元文档 + 1 trace.jsonl)

## 偏差
- 无. 与 PLAN §3 Task A1-A3 完全一致.

## Checkpoint
无 (Setup 阶段 soft checkpoint, 预授权连续推进到 Phase B Tooling)

## 下一步
进入 Phase B (Tooling) Task B1: 验证 count_tokens.py 复用 (跑 v1 脚本测 output_v2/*.md)
