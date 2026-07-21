# Phase 1D — Full Eval Evidence Checkpoint

> Date: 2026-05-24
> Owner: main session (48 questions) + scientist subagent (5 questions, Rule A 4.c)
> Status: **PASS** (overall 88.5% ≥ 85% threshold)
> Model: deepseek/deepseek-chat (Anthropic API credits exhausted; Sonnet/Opus deferred)

## Results Summary

| Metric | Value |
|--------|-------|
| Questions | 53 (48 main + 5 scientist) |
| Source recall (avg) | **82.1%** |
| Fact recall (avg) | **94.8%** |
| Overall (src+fact avg) | **88.5%** |
| Threshold | 85% |
| Verdict | **PASS** |
| Total tokens | 676,011 |
| Model | deepseek/deepseek-chat |
| Validation scenarios | **5/5 PASS** |

## By Category

| Category | Source Recall | Fact Recall | Questions |
|----------|-------------|-------------|-----------|
| single_domain | 96.4% | 94.0% | 14 |
| mixed | 92.3% | 96.2% | 13 |
| concept | 76.9% | 93.1% | 13 |
| cross_domain | 61.5% | 96.2% | 13 |
| **Overall** | **82.1%** | **94.8%** | **53** |

## Source Misses (12/53 questions)

| ID | Category | Source Miss | Notes |
|----|----------|-----------|-------|
| q07 | cross_domain | VARIABLE_INDEX.md | EPOCH query → domain spec files retrieved instead |
| q09 | cross_domain | domains/RELREC/spec.md | RELREC query → chapters/ch08, RELREC/examples/assumptions |
| q10 | cross_domain | domains/TR/spec.md | TR-RS linking → only TR/assumptions found |
| q16 | mixed | terminology/core/ae.md | AESEV codelist → AE/spec.md found, codelist file missed |
| q32 | cross_domain | domains/SV/spec.md | SV query → SV/assumptions found, spec missed |
| q33 | cross_domain | domains/RELSPEC/spec.md | RELSPEC → not in top-15 |
| q34 | cross_domain | VARIABLE_INDEX.md | NY codelist C66742 → domain specs retrieved instead |
| q37 | concept | model/04_special_purpose.md | Special-Purpose → ch04 retrieved instead |
| q38 | concept | chapters/ch02 | Domain codes → ch04 retrieved instead |
| q39 | concept | model/02_observation_classes.md | Findings About → FA/spec retrieved instead |
| s04 | mixed | terminology/core/ae.md | AEACN codelist → AE/spec found, codelist file missed |
| s05 | mixed | terminology/core/vs.md | VS codelist → VS/spec found, codelist file missed |

**Pattern analysis**: 3 categories of source misses:
1. **VARIABLE_INDEX.md** (2 misses) — cross-domain index not retrieved for variable-level queries
2. **terminology/core/ files** (3 misses) — codelist-specific files missed when domain spec already provides the CT code
3. **model/ + chapters/ files** (4 misses) — conceptual documents not retrieved for concept-level queries
4. **Specific domain specs** (3 misses) — RELREC/RELSPEC/TR/SV spec files missed in cross-domain queries

All 12 misses have high fact recall (most 100%) — the LLM answers correctly from alternative retrieved context.

## Cross-Model Comparison

| Model | Status | Source Recall | Fact Recall | Overall | Verdict |
|-------|--------|-------------|-------------|---------|---------|
| deepseek/deepseek-chat | **Complete** | 82.1% | 94.8% | 88.5% | **PASS** |
| anthropic/claude-sonnet-4-6 | Blocked | — | — | — | API credits exhausted |
| anthropic/claude-opus-4-7 | Blocked | — | — | — | API credits exhausted |
| (retrieval-only) | Complete | 82.1% | n/a | n/a | Baseline |

**Note**: Source recall is model-independent (depends only on embedding retrieval), confirmed identical at 82.1% across DeepSeek and retrieval-only runs. Sonnet/Opus would differ only in fact recall. Based on Phase 1B5 (Sonnet 100% fact recall on 20 questions), Sonnet is expected to match or exceed DeepSeek's 94.8% fact recall.

## Phase 2 KG Decision Gate (PLAN §5, 1D.4)

**Criterion**: RELATION-type (cross_domain) 12+ questions source recall < 50% → trigger Phase 2 KG.

**Result**: cross_domain source recall = **61.5% > 50%** → **Phase 2 KG NOT triggered**.

Analysis:
- 8/13 cross_domain questions have 100% source recall
- 5/13 have partial/zero source recall
- Despite source misses, fact recall for cross_domain is **96.2%** — the LLM compensates from alternative context
- VARIABLE_INDEX.md and RELSPEC/RELREC are the weakest retrieval targets
- Phase 2 KG would primarily improve VARIABLE_INDEX cross-referencing and relationship-aware routing

**Recommendation**: Defer Phase 2 KG. The RAG system provides sufficient factual accuracy (96.2% cross-domain fact recall) for practical use. KG would marginally improve source traceability but does not affect answer quality.

## Validation Scenarios (5/5 PASS)

| Scenario | Description | Result |
|----------|-------------|--------|
| V1 | Valid VS dataset → 0 ERROR | PASS |
| V2 | CM dataset with REQ+TYPE errors | PASS |
| V3 | EX dataset with PK duplicate | PASS |
| V4 | AE subjects missing from DM → SUBJ error | PASS |
| V5 | Single-row minimal dataset → no crash | PASS |

## Rule A 4.c — Scientist Independence Check

Scientist (opus subagent_type=scientist) independently wrote 5 questions:
- s01: DM SEX codelist C66731 (single_domain)
- s02: SUPPQUAL QNAM constraints (concept)
- s03: DM-EX RFXSTDTC linkage (cross_domain)
- s04: AE AEACN codelist C66767 (mixed)
- s05: VS VSTESTCD codelist C66741 (single_domain)

**Topic overlap with main's 48**: 5/5 (100%) ≥ 50% threshold
- s01 ↔ q43 (DM SEX) — exact match
- s02 ↔ q06 (SUPPQUAL) — same domain
- s03 ↔ q20 (DM reference periods) — closely related
- s04 ↔ q01/q03/q46 (AE domain) — same domain
- s05 ↔ q22/q44 (VS VSTESTCD) — exact match

**Rule A 4.c: PASS** — independent agreement on key topics validates ground truth quality.

## Files

- `eval/test_set_v1.yml` — 53 questions (48 main + 5 scientist)
- `eval/scientist_questions_1d.yml` — scientist's 5 questions (original, pre-merge)
- `eval/run_eval.py` — evaluation runner (multi-model + retry + threshold)
- `eval/1d_report_deepseek.json` — DeepSeek full results
- `eval/1d_report_retrieval.json` — retrieval-only baseline
- `eval/validation_scenarios.py` — 5 validation scenario tests
- `eval/validation_scenario_results.json` — validation scenario results

## Comparison with Phase 1B5

| Metric | 1B5 (20q, Sonnet) | 1D (53q, DeepSeek) | Delta |
|--------|-------------------|---------------------|-------|
| Source recall | 85.0% | 82.1% | -2.9% |
| Fact recall | 100.0% | 94.8% | -5.2% |
| Overall | 92.5% | 88.5% | -4.0% |
| cross_domain src | 50.0% | 61.5% | +11.5% |
| Threshold | 80% | 85% | +5% |
| Verdict | PASS | PASS | — |

Cross-domain source recall improved from 50% (1B5) to 61.5% (1D) with broader question coverage. Overall dropped slightly due to harder questions and a weaker LLM model, but still clears the stricter 85% threshold.

## PASS Five Conditions

1. ✅ evidence: 53 questions + retrieval baseline + correctness/citation/recall metrics
2. ✅ writer (scientist) ran independently, did not see main's test set
3. ⏳ independent verifier PASS (Rule D — to be dispatched)
4. ✅ Rule A 4.c: scientist 5 questions, 100% topic overlap ≥ 50%
5. ⏳ user Bojiang ack
