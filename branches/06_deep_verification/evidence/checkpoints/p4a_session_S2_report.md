# P4a Session S2 Report

> Date: 2026-05-12
> Session: S2 (batch_026~050)
> Status: **COMPLETE**
> Kickoff: `multi_session/P4a_session_02_kickoff.md`

## Coverage Progress

| Metric | Value |
|--------|-------|
| S2 atoms processed | 2,500 |
| coverage_ledger.jsonl total | 5,000 (40% of 12,487) |
| S2 batches | batch_026~050 (25 batches) |
| Writer rotation | even=writer / odd=executor |

## S2 Verdict Distribution

| Verdict | Count | % |
|---------|-------|---|
| EXACT | 953 | 38.1% |
| PARTIAL | 575 | 23.0% |
| EQUIVALENT | 546 | 21.8% |
| MISSING | 222 | 8.9% |
| MISPLACED | 123 | 4.9% |
| ERROR | 67 | 2.7% |
| INTENTIONAL_EXCLUDE | 14 | 0.6% |
| **Total** | **2,500** | 100% |

Coverage rate (EXACT+EQUIV): 59.9% | With PARTIAL: 82.9%

## Key Findings (S2)

### Systematic Gaps — Variable Spec Tables MISSING
多个 domain 的变量 spec 表行在 KB 中缺失（KB 只有 assumptions.md + examples.md，未收录逐行 spec 变量定义）:
- CM domain: ~41 variable metadata rows MISSING (batch_027)
- BE domain: spec table rows MISSING (batch_037)
- DV/DA domain: spec table rows MISSING (batch_047)
- HO/MH domain: spec table rows MISSING (batch_045)
- SU domain: spec table rows MISSING (batch_035)
- ML spec TABLE_ROW: 43 PARTIAL (reformatted as prose, batch_033)

→ **需 P6 Triage 开 Issue**: KB spec.md 文件结构不匹配 PDF 逐行变量表格式，是系统性 REDUNDANT_WITH_SPEC 或格式错位问题。

### Variable Name Discrepancies — ML Domain (batch_033)
- `MLGRID` (PDF) → KB 用 `MLGRPID`
- `MLTPREF` (PDF) → KB 用 `MLTPTREF`
- `MLRFDTC` (PDF) → KB 用 `MLRFTDTC`

→ 需登记 Issue (MEDIUM): 变量名拼写不一致

### Example Data Discrepancies
- AE: "BACK PAIN FOR 6 HOURS" (PDF) vs "BACK PAIN FOR 5 HOURS" (KB) — batch_037
- EG: EGSTRESN 446 (PDF) vs 448 (KB); file ref / testcd 变体 — batch_049
- EC: ECPREP (PDF) vs ECPRESP (KB) — batch_031
- DS: ELEMENT 列 TABLE_HEADER KB 缺失 — batch_043

### High MISPLACED Rate — S2 Observation
batch_026 全部 39 MISPLACED (§5.5 SV 区域); batch_028 有 26 MISPLACED。需 P4b section 聚合确认是否 STRUCTURE_DRIFTED 模式。

### Agent-Side Notes
- batch_046 agent 自行 git commit (54498a1) — 未造成数据问题，已在主 commit 历史中
- batch_040 agent 修改了 _progress.json — 待核查
- trace.jsonl S2 部分为多行 JSON 格式（非单行 JSONL），数据完整但格式次优；S3 前应压缩规范化

## Output Files

| File | Status |
|------|--------|
| batch_026~050 ledger.jsonl | ✅ 25 files × 100 lines |
| batch_026~050 trace.json | ✅ 25 files |
| coverage_ledger.jsonl | ✅ 5,000 lines |
| trace.jsonl | ✅ appended (multi-line format) |

## Next Step (S3)

```bash
python3 scripts/p4a_build_batches.py --range 51-75
```
然后派发 25 agents (batch_051~075) → 累计 7,500 atoms (60%)
