# Phase 1B5 — Sanity Eval Evidence Checkpoint

> Date: 2026-05-24
> Owner: main session (15 questions) + scientist subagent (5 questions, Rule A 4.b)
> Status: **PASS** (overall 92.5% ≥ 80% threshold)

## Results Summary

| Metric | Value |
|--------|-------|
| Questions | 20 (15 main + 5 scientist) |
| Source recall (avg) | **85.0%** |
| Fact recall (avg) | **100.0%** |
| Overall (src+fact avg) | **92.5%** |
| Threshold | 80% |
| Verdict | **PASS** |
| Total tokens | 318,022 |
| Model | claude-sonnet-4-6 |

## By Category

| Category | Source Recall | Fact Recall | Questions |
|----------|-------------|-------------|-----------|
| single_domain | 100% | 100% | 5 |
| concept | 100% | 100% | 5 |
| mixed | 90% | 100% | 5 |
| cross_domain | 50% | 100% | 5 |

## Source Misses (4/20 questions)

| ID | Category | Source Miss | Notes |
|----|----------|-----------|-------|
| q07 | cross_domain | VARIABLE_INDEX.md | EPOCH query → chunks from spec.md instead |
| q09 | cross_domain | domains/RELREC/spec.md | RELREC query → related domains retrieved |
| q10 | cross_domain | domains/TR/spec.md | Only TR/assumptions.md found, not spec |
| q16 | mixed | terminology/core/ae.md | AESEV → AE/spec.md found, codelist file missed |

All 4 misses have 100% fact recall — the LLM answers correctly from alternative context.
Cross-domain weak spot (50% source recall) aligns with Phase 2 KG decision gate.

## Rule A 4.b — Scientist Independence Check

Scientist (opus, subagent_type=scientist) independently wrote 5 questions:
- q05: PE domain PETESTCD (single_domain)
- q10: TR-RS-TU linking (cross_domain)
- q15: Core Perm handling rules (concept)
- q19: DS DSDECOD codelist C66727 (mixed)
- q20: DM RFSTDTC vs RFXSTDTC (mixed)

**Topic overlap with main's 15**: 3/5 (60%) ≥ 50% threshold
- q10 (TR linking) ↔ q09 (RELREC linking): both test cross-domain relationships
- q15 (Core Perm rules) ↔ q12 (Core definitions): same topic area
- q20 (DM reference periods) ↔ q02 (DM variables): same domain

**Rule A 4.b: PASS** — independent agreement on key topics validates ground truth quality.

## Files

- `eval/test_set_v0.yml` — 20 questions (YAML)
- `eval/run_eval.py` — evaluation runner (retrieval-only + full modes)
- `eval/baseline_report_v0_full.json` — full results (per-question + summary)

## Decision: Phase 1B5.3 (chunker/Top-K adjustment)

Overall 92.5% ≥ 80% → **no adjustment needed**. Proceeding to Phase 1C.

Cross-domain source recall (50%) is a known limitation of pure embedding-based retrieval.
Tracked for Phase 2 KG decision gate (PLAN §5: RELATION 召回 < 50% → KG 启动).

## PASS Five Conditions

1. ✅ evidence: 20 questions + baseline report + recall ≥ 80%
2. ✅ writer (main + scientist) products compliant
3. ⏳ independent verifier PASS (Rule D — to be dispatched)
4. ✅ Rule A 4.b: scientist 5 questions, 60% topic overlap ≥ 50%
5. ⏳ user Bojiang ack
