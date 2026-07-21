# P4b Section Aggregation — Initial Report

> Date: 2026-05-12
> Phase: P4b (Section Aggregation)
> Script: `scripts/p4b_section_aggregate.py`
> Status: **Script COMPLETE — reviewer running, gate pending**

---

## Run Summary

| Item | Value |
|---|---|
| Input: pdf_atoms.jsonl | 12,487 atoms |
| Input: coverage_ledger.jsonl | 12,476 entries (11 atoms unlisted → default MISSING) |
| Input: md_atoms.jsonl | 10,435 atoms |
| Output: section_coverage.jsonl | **399 sections** |
| Sections with aggregate_verdict | 399 / 399 = 100% ✅ |

---

## Aggregate Verdict Distribution

| Verdict | Count | % |
|---|---|---|
| FULL_COVERAGE | 101 | 25.3% |
| MOSTLY_COMPLETE | 42 | 10.5% |
| CONTENT_TRUNCATED | 110 | 27.6% |
| SIBLING_DROPPED | 56 | 14.0% |
| SKELETON_ONLY | 67 | 16.8% |
| STRUCTURE_DRIFTED | 23 | 5.8% |
| HEADING_MISSING | 0 | 0.0% |
| **Total** | **399** | **100%** |

**Healthy (FULL_COVERAGE + MOSTLY_COMPLETE): 143 sections (35.8%)**

---

## Failure Pattern Summary

| Pattern | Sections |
|---|---|
| CONTENT_TRUNCATED (pattern) | 132 |
| SKELETON_ONLY (pattern) | 80 |
| SIBLING_DROPPED (pattern) | 76 |
| STRUCTURE_DRIFTED (pattern) | 23 |

Note: One section can have multiple patterns. `aggregate_verdict` = highest-priority pattern.

---

## SKELETON_ONLY Triage (67 sections)

| Category | Count | Action |
|---|---|---|
| sv20 sections (SDTM v2.0, KB built from ig34) | 20 | INTENTIONAL_EXCLUDE: `SDTM_V2_SYSTEMATIC_GAP` |
| EDITORIAL_META (Cover / TOC) | 3 | INTENTIONAL_EXCLUDE: `EDITORIAL_META` |
| Domain spec/overview stubs (out-of-scope per PLAN §0.2) | 20 | INTENTIONAL_EXCLUDE: `REDUNDANT_WITH_SPEC` |
| Small stubs (≤2 content atoms) | 6 | Monitor; likely structural section boundaries |
| **Real gaps (ig34, ≥3 atoms)** | **18** | → P6 Triage → Issue 5+ |

**Top real gaps by atom count:**

| Section | Atoms | Density |
|---|---|---|
| §6.3.5.9.3 — Example 4 | 88 | 0.0 |
| §6.3.5.9.3 — Example 3 | 84 | 0.0 |
| §6.3.5.7.1 Microbiology Specimen (MB) | 89 | 0.169 |
| §6.3.5.9.3 — Example 2 | 50 | 0.0 |
| §5 [General Observation Classes] | 28 | 0.0 |
| §6.3.10 Subject Characteristics (SC) | 28 | 0.036 |
| §6.4.1 When to Use Findings About Events | 25 | 0.0 |
| §7 [Changes SDTM v1.8→v2.0] (sv20) | 90 | 0.156 |

---

## STRUCTURE_DRIFTED (23 sections, misplaced_rate ≥ 10%)

| Section | Drift Rate | Atoms |
|---|---|---|
| §6.1.3 [Exposure Domains] | 100% | 2 |
| §6.3 [MODELS FOR FINDINGS DOMAINS] | 100% | 1 |
| §6.3.6 Morphology (MO) | 100% | 4 |
| §8.3.1 RELREC Dataset Relationship Example | 40% | 20 |
| §6.3.7.1 Generic Morphology/Physiology Spec | 35% | 20 |
| §6.3.5.9.2 PP Parameters | 15.5% | 110 |
| §6.3.5.9.3 Relating PP Records to PC Records | 17.3% | 75 |
| §3.1.3 The Findings Observation Class | 21.8% | 101 |
| §6.1.1 [Procedure Agents (AG)] | 22.1% | 104 |
| §5.5 [Subject Visits (SV)] | 13.2% | 121 |
| ... (13 more) | | |

Note: 100%-drift sections have ≤4 atoms — likely structural boundary atoms that all landed in adjacent sections. Low-volume noise.

---

## Level-1 Keyword Flag (43 sections)

43 sections have MISSING atoms containing "shall", "must", or "required" — these were flagged
for mandatory triage in P6 per PLAN §4.5 Level-1 keyword upgrade rule.

---

## Gate Status

| Gate Condition | Status |
|---|---|
| 399/399 sections have aggregate_verdict | ✅ |
| Rule A 30-section reviewer (≥95% agree) | 🔄 running |
| SKELETON_ONLY white-listing / Issues | ⏳ P6 |
| STRUCTURE_DRIFTED Issues logged | ⏳ P6 |
| trace.jsonl phase_report P4b | ⏳ this session |

---

## Known Limitations of Current Script

1. **Child-section status for density < 0.60**: Per PLAN, SIBLING_DROPPED triggers when a child is CONTENT_TRUNCATED < 0.60. The script currently marks ALL CONTENT_TRUNCATED children as SIBLING_DROPPED triggers (conservative). The reviewer should note cases where the child density is 0.60-0.80 which are technically CONTENT_TRUNCATED but shouldn't trigger SIBLING_DROPPED per the strict reading.

2. **Non-§-numbered sections**: Domain sections ("FA – Assumptions") and Appendix sections don't get child_sections populated (no numeric hierarchy to traverse). Their aggregate_verdict is based solely on content atom verdicts.

3. **sv20/ig34 HEADING verbatim matching**: HEADING_MISSING detection only works for §-numbered sections with an identifiable parent. Domain/Appendix sections get heading_missing_detected = False by default.
