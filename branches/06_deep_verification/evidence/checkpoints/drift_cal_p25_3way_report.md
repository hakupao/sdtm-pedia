# Drift Calibration p.25 — 3-Way Analysis (tiebreaker applied)

> Date: 2026-04-24
> Baseline: executor (batch 03), re-run: writer, tiebreaker: general-purpose
> Threshold: ≥80% (PLAN §9.1 P1)

## Samples

| Writer type | Source | Atoms |
|---|---|---|
| executor (sonnet) | `pdf_atoms.jsonl` batch 03 | 40 |
| writer (sonnet) | `drift_cal_p25_writer_rerun.jsonl` | 40 |
| general-purpose (sonnet) | `drift_cal_p25_general_purpose_rerun.jsonl` | 40 |

## Pairwise strict agreement (atom_type + verbatim exact)

| Pair | Matches | Symmetric agreement |
|---|---|---|
| Executor ↔ Writer | 27 | **67.5%** |
| Executor ↔ Gen-purpose | 15 | **37.5%** |
| Writer ↔ Gen-purpose | 15 | **37.5%** |

## 3-way consensus

- Unanimous (in all 3 sets): **15**
- ≥2/3 majority: **27**
- Only 1/3 (outlier): 51
- Union: 78
- **3-way unanimous rate**: 19.2%
- **≥2/3 majority rate**: 34.6%

## atom_type distribution (3-way)

| type | executor | writer | gen-purpose |
|---|---|---|---|
| CODE_LITERAL | 4 | 4 | 4 |
| HEADING | 6 | 6 | 6 |
| TABLE_HEADER | 4 | 4 | 4 |
| TABLE_ROW | 26 | 26 | 26 |

## Outlier attribution

- Executor-unique atoms: 13
- Writer-unique atoms:   13
- Gen-purpose-unique atoms: 25

Executor∩GP = 15; Writer∩GP = 15. Tied. 无主导偏差方, 任务本身 (QS 稀疏表格字面解析) 有歧义.

## Verdict: **FAIL**

- Best pairwise agreement: 67.5%
- ≥2/3 majority rate: 34.6%
- Threshold: 80%

### 决策语义

**FAIL**: 3 writer 产物分叉, 任务语义本身不明确. halt, 派 architect 重新审 prompt TABLE_ROW 规则.
