# DM1 Task 3 attempt 1 — mapping-set regression on dm05 (archived per Rule B, do not delete)

裁定 (controller): 非 T3 缺陷, 由 T4 域级定义保底席修复; T3 按 140q 零回归通过, dm05 在 T8 闸复核。

Context: Task 3 (D1) — case- and anchor-aware domain code detection in
`StructuredLookup._query_domains`. Implemented exactly per brief
(`.superpowers/sdd/2026-09-15-domain-mapping-retrieval/task-3-brief.md`):
new `_ANCHORED_CODE_RE` / `_PREFIXED_CODE_RE` / `_LOWER_CODE_BLOCKLIST`
constants near `server/structured_lookup.py:58`, `_query_domains` extended
to scan them after the uppercase-token pass. No other file touched besides
the test file.

## Input (exact commands run)

```bash
.venv/bin/python -m pytest scripts/tests/test_structured_lookup.py -q -k Anchored   # RED, then GREEN after impl
.venv/bin/python -m pytest scripts/tests/test_structured_lookup.py -q               # 58 passed (full file)

.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup \
  --output eval/runs/dm1_cdisc_t3.json
.venv/bin/python eval/compare_runs.py eval/runs/dm1_cdisc_before.json eval/runs/dm1_cdisc_t3.json

.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_domain_mapping_v1.yml --retrieval-only --hybrid \
  --structured-lookup --study-lookup --federated --corpus both \
  --output data/study/st01/eval/runs/dm1_mapping_t3.json
grep "Source recall" data/study/st01/eval/runs/dm1_mapping_t3.log
```

## Result (technical)

**CDISC 140-question set: zero regression.** `compare_runs.py` shows both
runs at avg=0.9917, 0 pairwise diff. Inline per-question script confirms
`worse: [] better: []`.

**Mapping 8-question set: 1 question regressed.** Source recall avg dropped
10.0% → 7.5%.

| id   | before | after | Δ |
|------|--------|-------|---|
| dm01 | 0.0    | 0.0   | — |
| dm02 | 0.0    | 0.0   | — |
| dm03 | 0.2    | 0.2   | — |
| dm04 | 0.2    | 0.2   | — |
| **dm05** | **0.2** | **0.0** | **WORSE** |
| dm06 | 0.0    | 0.0   | — |
| dm07 | 0.0    | 0.0   | — |
| dm08 | 0.2    | 0.2   | — |

dm05 = "In our study, which collected data items belong in the ae domain?"
(EN, lowercase code `ae`, domain=AE) — this is literally the question the
Task 3 brief's test-case row `dm05 | AE | en | 小写码 \`ae\` | our study`
targets. The detection itself works as designed; the regression is a
downstream interaction, not a detection bug.

## Root cause (confirmed, not speculative)

Checked directly against the live `StructuredLookup`/`RAGEngine` code:

```
lookup._query_domains(dm05_query)  ->  ['AE']          # NEW (was [] before Task 3)
lookup.resolve(dm05_query)         ->  ['domains/AE/spec.md']
```

`server/rag.py:452-469` (`_apply_structured_lookup`, untouched by this task,
pre-existing S1 behavior): when `resolve()` returns **exactly one** target
and it is a domain's `spec.md` (`_is_domain_spec`), the engine treats this
as a "pure single-domain ask" and injects `_SINGLE_DOMAIN_SPEC_CHUNKS = 4`
chunks of that file's `spec.md`, **prepended so they cannot be crowded out**
(comment at rag.py:444-445, 456-459). That heuristic is correct for genuine
CDISC single-domain questions ("what are the required variables in DM") —
the gold *is* spec.md there.

For `domain_mapping` questions the shape is different: "ae domain" here
means "which of **our study's data** goes into AE", and the gold is
`domains/AE/assumptions.md` + several `st01__AE__*` study variable pages —
**never** `domains/AE/spec.md`. Before Task 3, `_query_domains` returned
`[]` for lowercase "ae domain" (undetected), so S1 never fired, and pure
cosine happened to land `domains/AE/assumptions.md` in the top-5 (the 0.2
hit). After Task 3, the anchor now fires as designed, `resolve()` returns
`['domains/AE/spec.md']`, and the 4 forced spec.md chunks push the lucky
cosine hit for `assumptions.md` out of the top-k window — net loss, 0.2 → 0.
Confirmed via `top5_sources` in the run JSON: before had
`domains/AE/examples.md` ×2 + `domains/FA/examples.md` ×2 +
`domains/DS/examples.md`; after has `domains/AE/spec.md` ×4 +
`domains/FA/examples.md` — i.e. exactly the 4 injected spec.md chunks
replacing the previous cosine top-4.

This is the same "挤占" (crowding-out) tension already flagged as an open
question in `sdtm-rag/evidence/checkpoints/crowding_and_gold_integrity.md`
("挤占是否有害仍未知") — Task 3 is the first case where it demonstrably
hurts a mapping-set question.

## Business judgment

REJECT as passing per the gate in the brief ("If any question is worse, do
NOT commit"). Not committed. `_query_domains` itself matches spec exactly
(all TDD steps green, zero CDISC regression); the fault is in the
single-domain enrichment heuristic in `_apply_structured_lookup`
(`server/rag.py`), which is explicitly out of scope for Task 3 (brief only
authorizes touching `_query_domains` + the new constants). Fixing it
would need a decision at the controller/plan level: e.g. gate the
single-spec-enrichment heuristic on the CDISC corpus only, or on the
absence of a `domain_mapping`-shaped query signal, or accept the loss as
a known tradeoff (dm05 still nets a code detection win — the CDISC channel
is unaffected and 4/8 other mapping questions are unaffected). Left for the
controller to decide; no speculative fix attempted from this seat.

## Next attempt input (if authorized)

- Reproduce with: `lookup._query_domains(q)` / `lookup.resolve(q)` snippet above.
- Candidate fix directions (not evaluated, for the next attempt to weigh):
  1. In `_apply_structured_lookup`, skip the single-spec 4-chunk enrichment
     when the corpus is study/federated-both (mapping-shaped queries only
     ever ask "study data -> domain", never "tell me about domain X").
  2. Have `resolve()` also union-add `domains/{code}/assumptions.md` when
     the single-spec heuristic fires, since assumptions.md is the actual
     gold home for domain_mapping questions.
  3. Narrow `_query_domains`'s anchored pass to fire only for the CDISC
     structured-lookup instance, not when `study_lookup`/federated routing
     is active (StructuredLookup itself has no corpus-mode signal today —
     would need one threaded in).
