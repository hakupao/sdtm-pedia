# P4a Session S4 Report

> Date: 2026-05-12
> Session: S4 (batch_076~100)
> Status: **COMPLETE**
> Kickoff: `multi_session/P4a_session_04_kickoff.md`

## Coverage Progress

| Metric | Value |
|--------|-------|
| S4 atoms processed | 2,500 |
| coverage_ledger.jsonl total | 10,000 (80.1% of 12,487) |
| S4 batches | batch_076~100 (25 batches) |
| Writer rotation | even=writer / odd=executor |
| Re-run required | none |

## S4 Verdict Distribution

| Verdict | Count | % |
|---------|-------|---|
| EXACT | 812 | 32.5% |
| EQUIVALENT | 864 | 34.6% |
| PARTIAL | 283 | 11.3% |
| MISSING | 517 | 20.7% |
| MISPLACED | 8 | 0.3% |
| ERROR | 16 | 0.6% |
| INTENTIONAL_EXCLUDE | 0 | 0.0% |
| **Total** | **2,500** | 100% |

Coverage rate (EXACT+EQUIV): 67.0% | With PARTIAL: 78.4%

> S4 MISSING rate (20.7%) lower than S3 (35%) — domains in this range (OE/RP/SR/FA/TA) have better KB coverage than S3's Findings domains.

## Cumulative S1+S2+S3+S4

| Metric | Value |
|--------|-------|
| Total atoms | 10,000 (80.1% of 12,487) |
| EXACT | 3,061 (30.6%) |
| EQUIVALENT | 2,864 (28.6%) |
| PARTIAL | 1,665 (16.7%) |
| MISSING | 1,877 (18.8%) |
| MISPLACED | 198 (2.0%) |
| ERROR | 92 (0.9%) |
| INTENTIONAL_EXCLUDE | 243 (2.4%) |
| Matched (EXACT+EQUIV) | 59.3% |
| Matched+Partial | 75.9% |

## Key Findings (S4)

### Systematic Gap — Domain Spec Tables MISSING (continued pattern)
Same pattern from S2/S3 confirmed across additional domains:
- batch_079: 65% MISSING — RP domain spec TABLE_ROW atoms (KB only has assumptions/examples)
- batch_087: 72% MISSING — SS domain spec table entirely absent; TU spec table absent
- batch_091: 54% MISSING — §6.4 Findings About (FA) decision-criteria text not in KB

→ **P6 Triage (HIGH carry-forward)**: KB systematically omits domain spec variable tables for RP, SS domains.

### §6.4 Findings About Events or Interventions — Decision Criteria MISSING (batch_091) — HIGH
- Atoms 33–100 cover §6.4.1 "When to Use FA" criteria and §6.4.2–6.4.3 naming guidance
- KB has only scattered example narratives; the "When to Use FA" decision flow text is absent

→ **P6 Triage Issue (HIGH)**: FA chapter decision criteria (§6.4.1–§6.4.3) not captured in KB.

### VS Temperature Value Errors (batch_091) — HIGH
2 ERROR verdicts in VS domain Example 1 (p.362):
- atom ig34_p0362_a006: VS VSORRES = "36.2°C" (PDF) vs "38.2°C" (KB)
- atom ig34_p0362_a007: same row VSSTRESC discrepancy

→ **P6 Triage Issue (HIGH)**: VS domain Example 1 temperature values corrupted in KB (36.2→38.2).

### FA FATESTCD Code Errors (batch_093) — HIGH
3 ERROR verdicts in FA domain Examples 2–5 (pp.370-373):
- atom ig34_p0371_a014: FATESTCD "PAPRNG" (PDF) vs "FAPRNG" (KB) — wrong domain prefix
- atom ig34_p0371_a021: same PAPRNG→FAPRNG discrepancy  
- atom ig34_p0373_a100: FATESTCD "NUMEPISD" (PDF) vs "NUMEPISO" (KB) — typo

→ **P6 Triage Issue (HIGH)**: FA domain FATESTCD values have wrong codes in KB (PAPRNG/NUMEPISD vs FAPRNG/NUMEPISO).

### §7.1 Trial Design Model — Intro Prose MISSING (batch_096) — MEDIUM
- batch_096: 61% MISSING + 8 ERRORs — §7.1.x introductory prose not captured in KB
- KB covers Trial Design at higher abstraction; detailed §7.1 explanatory sentences absent
- 8 ERRORs: TV domain variable values incorrect (highest S4 ERROR concentration)

→ **P6 Triage Issue (MEDIUM)**: §7.1 Trial Design intro prose absent from KB; TV variable values need review.

### SR Domain Data Errors (batch_095) — MEDIUM
3 ERRORs in SR domain Examples 2/3 (pp.378-381):
- atom 025: SROBJ dose value wrong in MD row 1 of Example 2
- atom 030: Extra "PAPULES" in MD SRORRES value for row 6
- atom 073: SRTESTCD "DRLDOM" (KB) vs "IDRLIAM" (PDF) + timestamp discrepancy

→ **P6 Triage Issue (MEDIUM)**: SR domain example data rows have factual errors in KB.

### MISPLACED Cluster — Generic Headings (batches 085, 089)
- batch_085: 3 MISPLACED — RS domain "Example 1/2/3" headings matched CM domain by Jaccard
- batch_089: 5 MISPLACED — TR/TU domain SUPP table headers matched wrong domain sections

→ Low severity (heading-level only); P4b section aggregation will handle domain alignment.

### High-Coverage Batches (reference)
- batch_077: EXACT=33 EQUIV=63 (96% coverage) — NV VEP examples + OE domain
- batch_078: EXACT=14 EQUIV=75 PARTIAL=11 (100% coverage) — OE domain well-covered
- batch_082: EXACT=27 EQUIV=61 PARTIAL=12 (100% coverage) — PE/SR domain
- batch_083: EXACT=28 EQUIV=67 PARTIAL=1 (96% coverage) — FT/QS domain
- batch_088: EXACT=35 EQUIV=65 (100% coverage) — TU Assumptions/Examples
- batch_097: EXACT=57 EQUIV=22 PARTIAL=8 (87% coverage) — TA Examples 1-4

### Agent Notes
- No re-runs required; all 25 agents completed on first attempt ✓
- No unauthorized _progress.json modifications ✓
- No git commits made ✓
- batch_076: 0% MISSING (all PARTIAL or better) — notable high coverage

## Output Files

| File | Status |
|------|--------|
| batch_076~100 ledger.jsonl | ✅ 25 files × 100 lines |
| batch_076~100 trace (in trace.jsonl) | ✅ appended |
| coverage_ledger.jsonl | ✅ 10,000 lines |
| _progress.json | ✅ S4 stats written |

## Next Step (S5)

```bash
python3 scripts/p4a_build_batches.py --range 101-125
```
然后派发 25 agents (batch_101~125) → 累计 12,487 atoms (100%) → P4a COMPLETE → Exit Gate
