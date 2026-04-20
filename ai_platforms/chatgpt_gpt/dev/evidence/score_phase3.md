# ChatGPT GPTs Phase 3 打分结果 (v1.1 加法公式)

> Generated: 2026-04-20T08:55:30Z
> Script: `dev/scripts/score_chatgpt_priority.py`
> Formula: `score = (priority_weight × coverage_weight) + audience_bonus + novelty_bonus`
> Floor: score < 0.15 → 0.15 (仅 coverage 严重降级兜底)
> Source: PLAN.md §3.1 v1.1 + §3.2 v1.1 + §2.4 (9 合并文件清单)

## 打分明细 (按 score 降序)

| rank | # | 文件 | coverage | priority | 核心 (pri×cov) | audience | novelty | score | 批次 |
|:----:|:-:|------|:--------:|:--------:|:--------------:|:--------:|:-------:|:-----:|:----:|
| 1 | 01 | navigation.md | 1.0 | P0 (3.0) | 3.0 | +0.2 | +0.2 | **3.4** | 1 |
| 2 | 02 | chapters_all.md | 1.0 | P0 (3.0) | 3.0 | +0.2 | +0.2 | **3.4** | 1 |
| 3 | 03 | model_all.md | 1.0 | P0 (3.0) | 3.0 | +0.2 | +0.0 | **3.2** | 1 |
| 4 | 04 | domain_specs_all.md | 1.0 | P0 (3.0) | 3.0 | +0.0 | +0.2 | **3.2** | 1 |
| 5 | 06 | examples_all.md | 1.0 | P1 (1.5) | 1.5 | +0.2 | +0.2 | **1.9** | 2 |
| 6 | 05 | assumptions_all.md | 1.0 | P1 (1.5) | 1.5 | +0.0 | +0.0 | **1.5** | 2 |
| 7 | 07 | terminology_core.md | 1.0 | P2 (1.0) | 1.0 | +0.2 | +0.0 | **1.2** | 2 |
| 8 | 08 | terminology_questionnaires.md | 1.0 | P2 (1.0) | 1.0 | +0.2 | +0.0 | **1.2** | 2 |
| 9 | 09 | terminology_supplementary.md | 1.0 | P2 (1.0) | 1.0 | +0.2 | +0.0 | **1.2** | 2 |

## 排序语义验证 (v1.1)

- P0 核心 (01/02=3.4 > 03=04=3.2) > P1 辅助 (06=1.9 > 05=1.5) > P2 查表 (07-09=1.2)
- 与 PLAN §3.2 数字应精确一致 (Phase 2 reviewer 认可).
- floor 规则本次未触发 (所有文件 coverage=1.0, 核心分 ≥ 1.0).

## Phase 3 Node 1 note

- 本脚本为 Node 1 产出的静态打分器 (字段硬编码 PLAN §3.2 v1.1).
- 若后续 coverage 因合并失败降级 (0.7 / 0.3), 本脚本可直接重跑, 会自动反映降级 score 与 floor 行为.
