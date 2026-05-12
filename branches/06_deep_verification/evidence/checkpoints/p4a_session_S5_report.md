# P4a Session S5 — Checkpoint Report

> Date: 2026-05-12
> Batches: batch_101 ~ batch_125
> Atoms: 2,487 (ig34_p0407_a001 → sv20 tail)
> Status: **S5 COMPLETE — P4a 100% coverage achieved**

---

## Session Stats

| Verdict | Count |
|---|---|
| EXACT | 686 |
| EQUIVALENT | 575 |
| PARTIAL | 380 |
| MISPLACED | 75 |
| MISSING | 619 |
| ERROR | 1 |
| INTENTIONAL_EXCLUDE | 151 |
| **Total** | **2,487** |

Coverage rate (EXACT+EQUIV): 50.7%  
Coverage rate (with PARTIAL): 66.0%

---

## Cumulative S1–S5 (Full P4a)

| Verdict | Count |
|---|---|
| EXACT | 3,747 |
| EQUIVALENT | 3,439 |
| PARTIAL | 2,045 |
| MISPLACED | 273 |
| MISSING | 2,496 |
| ERROR | 93 |
| INTENTIONAL_EXCLUDE | 394 |
| **Total** | **12,487** |

Coverage rate (EXACT+EQUIV): **57.5%**  
Coverage rate (with PARTIAL): **73.9%**

---

## Merge Fix (2026-05-12 post-S5)

S5 batch ledgers (batch_101~125_ledger.jsonl) were appended to `coverage_ledger.jsonl` in this session.
Prior state: 10,000 lines (S1–S4). Post-merge: 12,487 lines. ✅

---

## P4a Exit Gate Status

| Gate | Status |
|---|---|
| coverage_ledger.jsonl = 12,487 lines | ✅ |
| Every verdict ∈ legal enum | ✅ (batch-level validated) |
| INTENTIONAL_EXCLUDE all have whitelist entry | ⚠️ pending verify |
| Rule A 100-atom stratified audit ≥95% | ❌ not yet executed |
| Drift check ≥80% | ⚠️ only batch_101 entry in trace |
| trace.jsonl P4a phase_report ≥1 | ❌ pending |
| Rule D ≥3 reviewer types in P4a | ⚠️ pending audit_matrix check |
| MISPLACED → discrepancies.md | ⚠️ pending verify |

**Next**: Run P4a Exit Gate formal verification before entering P4b.

---

## Open Issues from S5 Data

- MISPLACED count = 75 in S5 (cumulative 273) — high; discrepancies.md needs verification
- MISSING count = 619 in S5 — sv20 tail sections likely intentional; needs triage
- ERROR count = 1 — single entry, low risk
