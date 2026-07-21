# P4a Session S3 Report

> Date: 2026-05-12
> Session: S3 (batch_051~075)
> Status: **COMPLETE**
> Kickoff: `multi_session/P4a_session_03_kickoff.md`

## Coverage Progress

| Metric | Value |
|--------|-------|
| S3 atoms processed | 2,500 |
| coverage_ledger.jsonl total | 7,500 (60.1% of 12,487) |
| S3 batches | batch_051~075 (25 batches) |
| Writer rotation | even=writer / odd=executor |
| Re-run required | batch_063 (first attempt incomplete) |

## S3 Verdict Distribution

| Verdict | Count | % |
|---------|-------|---|
| MISSING | 875 | 35.0% |
| EQUIVALENT | 721 | 28.8% |
| PARTIAL | 423 | 16.9% |
| EXACT | 416 | 16.6% |
| MISPLACED | 57 | 2.3% |
| ERROR | 6 | 0.2% |
| INTENTIONAL_EXCLUDE | 2 | 0.1% |
| **Total** | **2,500** | 100% |

Coverage rate (EXACT+EQUIV): 45.5% | With PARTIAL: 62.4%

> ⚠️ S3 MISSING rate (35%) significantly higher than S1 (10.5%) and S2 (8.9%).
> Reflects systematic spec table gaps in §6.3.x Findings domains (batches 051-075 span p.195-294).

## Cumulative S1+S2+S3

| Metric | Value |
|--------|-------|
| Total atoms | 7,500 (60.1% of 12,487) |
| EXACT | 2,249 (30.0%) |
| EQUIVALENT | 2,000 (26.7%) |
| PARTIAL | 1,382 (18.4%) |
| MISSING | 1,360 (18.1%) |
| MISPLACED | 190 (2.5%) |
| ERROR | 76 (1.0%) |
| INTENTIONAL_EXCLUDE | 243 (3.2%) |
| Matched (EXACT+EQUIV) | 56.7% |
| Matched+Partial | 75.1% |

## Key Findings (S3)

### Systematic Gap — RELREC Cross-Reference Dataset Rows (HIGH severity)
§6.3.5.9.3 PP/PC relating-records section rows entirely absent from KB:
- batch_069: 49% MISSING — PC concentration table rows (atoms 74-97) + RELREC methodology text
- batch_071: 98% MISSING — PP RELREC linking tables (relrec.xpt) + Methods A/B/C/D descriptions (pp.279-281)
- batch_073: 77% MISSING — PP/PC RELREC Example 4 data rows + PC-PP Conclusions guidance (pp.283-286)

→ **P6 Triage Issue (HIGH)**: KB omits RELREC cross-reference dataset rows and Method A/B/C/D guidance for PP/PC domain. Only `pp.xpt` parameter table headings captured; `relrec.xpt` rows and methodology entirely absent.

### Systematic Gap — Domain Variable Spec Tables MISSING (continued from S2)
S3 confirmed the same pattern across additional domains:
- BS domain (batch_051): variable spec table rows all MISSING (assumptions + examples covered)
- MS domain (batch_063): 82% MISSING — spec TABLE_ROW candidates retrieved example rows instead of spec.md
- LB domain (batch_061): spec rows missing, assumptions/examples covered
- PC domain (batch_067): spec table rows (atoms 40-82, 44 atoms) all MISSING

→ Same issue as S2 — KB only captured assumptions.md + examples.md, spec table rows not indexed properly. Retriever surfaces example data rows when searching for spec variable definitions.

### CP Domain Column Rename Error (batch_053) — MEDIUM
16 cp.xpt Example 1a TABLE_ROWs are PARTIAL due to systematic column rename:
- `CPSTRESU` (PDF) → `CPRESU` (KB) — column header differs
- Additional marker-string discrepancies in rows 8, 9, 12, 13, 16

→ **P6 Triage Issue (MEDIUM)**: CP domain KB has wrong column name `CPRESU` where PDF uses `CPSTRESU`.

### MS Domain Factual Errors — MIC Values (batch_065) — HIGH
6 ERROR verdicts in MS domain (§6.3.5.7 Microbiology, pp.258-262):
- Numeric MIC values differ: e.g., 0.023 mg/L (PDF) vs 0.125/4.9 mg/L (KB)
- Susceptibility categories differ: INTERMEDIATE (PDF) vs SUSCEPTIBLE (KB)

→ **P6 Triage Issue (HIGH)**: MS domain MIC example data values factually wrong in KB.

### MISPLACED Cluster — §6.3.x Findings Sections (batches 068-073)
- batch_068: 24 MISPLACED
- batch_070: 14 MISPLACED (EQUIV=82 but cross-domain)
- batch_073: 13 MISPLACED — MO/morphology content filed under §10.E Revision History or §3.1.x SDTM model sections instead of §6.3.x domain sections

→ **P6 Triage Issue (MEDIUM)**: KB has content but under wrong section headings for MO domain.

### CP Domain — Example Coverage Gap (batch_055)
- CP Examples 7/8/9 (DC/flow cytometry, receptor occupancy data rows): 71% MISSING
- KB only has Examples 1a/1b; PDF Examples 7-9 rows not captured

→ **P6 Triage Issue (MEDIUM)**: CP domain KB covers examples 1a/1b only, not examples 7-9.

### High-Coverage Batches (reference)
- batch_057: EXACT=27, EQUIV=49 — GF domain + IS domain well-covered (IS vars as `### VARNAME` prose)
- batch_059: EXACT=31, EQUIV=45, PARTIAL=23, MISSING=1 — best S3 coverage
- batch_075: EXACT=45, EQUIV=50, PARTIAL=2, MISSING=3 — MK domain excellent

### Agent Notes
- batch_063 first attempt: incomplete (agent printed "Now let me process the batch using Python" and exited); re-run successful
- All other agents obeyed no-git-commit constraint ✅
- No unauthorized _progress.json modifications ✅

## Output Files

| File | Status |
|------|--------|
| batch_051~075 ledger.jsonl | ✅ 25 files × 100 lines |
| batch_051~075 trace (in trace.jsonl) | ✅ appended |
| coverage_ledger.jsonl | ✅ 7,500 lines |
| _progress.json | ✅ S3 stats written |

## Next Step (S4)

```bash
python3 scripts/p4a_build_batches.py --range 76-100
```
然后派发 25 agents (batch_076~100) → 累计 10,000 atoms (80%)
