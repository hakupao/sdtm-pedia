<!-- reviewer: independent verifier subagent (Rule D) — did NOT read writer's doc before deriving numbers -->
# T1 Top-K Ablation — Independent Review

> Date: 2026-06-08  
> Reviewer: verifier subagent (Rule D, distinct from writer session)  
> Method: recomputed all metrics from raw `results[]` arrays; writer's doc read only AFTER independent numbers were fixed.

---

## 1. Recomputed Per-Category Source Recall (from `results[]` arrays, not `summary` field)

| K | overall | concept | cross_domain | mixed | single_domain |
|---|---------|---------|--------------|-------|---------------|
| 15 | 82.1% | 76.9% | 61.5% | 92.3% | 96.4% |
| 20 | 83.0% | 76.9% | 65.4% | 92.3% | 96.4% |
| 30 | 83.0% | 76.9% | 65.4% | 92.3% | 96.4% |
| 50 | 87.7% | 84.6% | 76.9% | 92.3% | 96.4% |
| 100 | 93.4% | 92.3% | 92.3% | 92.3% | 96.4% |

Category sizes: single_domain n=14, concept n=13, cross_domain n=13, mixed n=13.

**Discrepancy vs writer's table: NONE.** All values match to 4 decimal places (rounding differences ≤0.0005).  
**K=15 vs baseline `1d_report_retrieval.json`: exact match** on all 53 questions, all categories.

---

## 2. Failing / Recovered / Still-Missing Question Sets

### Fail at K=15 (n=12)

| ID | Category | K=15 | K=50 | K=100 |
|----|----------|------|------|-------|
| q07 | cross_domain | 0.000 | 0.000 | **1.000** |
| q09 | cross_domain | 0.000 | 0.000 | **1.000** |
| q10 | cross_domain | 0.500 | **1.000** | 1.000 |
| q16 | mixed | 0.500 | 0.500 | 0.500 |
| q32 | cross_domain | 0.500 | **1.000** | 1.000 |
| q33 | cross_domain | 0.000 | **1.000** | 1.000 |
| q34 | cross_domain | 0.000 | 0.000 | 0.000 |
| q37 | concept | 0.000 | 0.000 | 0.000 |
| q38 | concept | 0.000 | 0.000 | **1.000** |
| q39 | concept | 0.000 | **1.000** | 1.000 |
| s04 | mixed | 0.500 | 0.500 | 0.500 |
| s05 | single_domain | 0.500 | 0.500 | 0.500 |

### Recovered: fail@K=15 → perfect@K=100 (n=7)
q07, q09, q10, q32, q33 (all cross_domain), q38, q39 (both concept).

### Still missing @K=100 (n=5)
q16 (mixed), q34 (cross_domain), q37 (concept), s04 (mixed), s05 (single_domain).

**Match to writer's claim: exact** (same 7 recovered, same 5 missing, same IDs).

---

## 3. Verdict: Central Claim — "cross_domain/concept low recall is mainly a RANKING problem"

**Verdict: CONDITIONAL PASS**

**For the claim:**
- Monotonicity check: all 53 questions are strictly non-decreasing across K=15→20→30→50→100. Zero violations. This is necessary (though not sufficient) evidence that the deficits are ranking, not representation.
- 7 of 12 failing questions (58%) reach source_recall=1.0 by K=100, confirming the correct chunks exist in the vector space and are retrievable at sufficient K.
- cross_domain recovery: 61.5% → 92.3% (+30.8pt); concept: 76.9% → 92.3% (+15.4pt). Both categories show strong monotonic gains.
- q07, q09 (cross_domain) and q38 (concept) still scored 0.0 at K=50 but recovered to 1.0 at K=100 — correct chunks are present but ranked beyond position 50. This is the strongest evidence for a ranking diagnosis.

**Against / Caveats:**
- "mainly" is accurate for cross_domain (5 of 8 failing questions recovered = 62.5%) and for concept (2 of 4 failing questions recovered = 50%). The claim is directionally sound but the split is not dominant for concept (50/50).
- K=20 and K=30 give no gain over K=15 for concept and only marginal gain for cross_domain. The relevant ranking band is K=30–100, which is unusually deep. A reranker with candidate pool K=50 captures the majority but not all of the ranking-recoverable cases (q07, q09, q38 need K>50).
- The claim that "rerank (T2) is the right fix" is supported but requires the candidate pool to be ≥100 (not 50) to recover all ranking-problem cases. The doc notes this correctly.

---

## 4. Verdict: Secondary Claim — "5 missing @K=100 are representation gaps tied to oversized terminology chunks + VARIABLE_INDEX embedding"

**Verdict: PARTIAL PASS — one claim is incorrect, two are overstated**

### q34 (VARIABLE_INDEX.md) — SUPPORTED
VARIABLE_INDEX.md is chunked into 65 domain-level sections (~588 tokens avg). A query about "variables shared across domains" hits general chapter chunks instead (top5 sims: 0.64–0.59, not one VI chunk). The domain-level H3 chunking dilutes cross-domain variable signal. Representation gap is real. Writer's "巨型索引文件" diagnosis is directionally correct (file is 131KB / ~33k tokens total; chunk count 65 is large).

### q37 (model/04_special_purpose.md) — INCORRECT DIAGNOSIS
**The expected source `model/04_special_purpose.md` does not exist in the knowledge base or the vector index (0 chunks).** The actual KB file is `model/03_special_purpose_domains.md` (7 chunks indexed). The retrieved content (model/03_special_purpose_domains.md appears in q37's top5 at K=100) is semantically correct material, but the eval's substring match `"model/04_special_purpose.md" in retrieved_source` will always return False.  
**This is a test-set gold-label error, not a retrieval failure.** q37's source_recall=0.0 is permanently fixed regardless of any retrieval improvement. The writer attributes it to "chunk 语义与 query 距离远" — that diagnosis is wrong.

### q16 / s04 (terminology/core/ae.md) — OVERSTATED
ae.md is indexed as 4 separate small chunks (201–330 tokens each). The relevant chunk (ae.md#3, "Severity/Intensity Scale for Adverse Events", 201 tokens) is well within embedding limits. The writer claims "超大 terminology chunk (>8191 tok embedding 截断)" — **this is false for ae.md**: all 4 chunks are small. The actual failure mode is a semantic retrieval gap: the query "AESEV codelist code" does not rank ae.md#3 within K=100 despite the chunk containing the correct MILD/MODERATE/SEVERE table. The correct diagnosis is embedding semantic distance (the chunk header says "C66769" not "AESEV"), not token truncation.

### s05 (terminology/core/vs.md) — OVERSTATED
vs.md is indexed as 3 chunks. The largest is vs.md#2 ("Vital Signs Test Name", 2727 tokens) and vs.md#1 ("Vital Signs Test Code", 2620 tokens). Neither exceeds the 8191-token embedding limit. Token truncation is not occurring. The miss is again a semantic distance issue (the relevant codelist chunk is not ranking within K=100 for the VSTESTCD codelist query). Writer's "超大 chunk 截断" diagnosis does not hold for vs.md either.

**Summary of secondary claim errors:**
| Sub-claim | Status |
|-----------|--------|
| q34: VARIABLE_INDEX representation gap | CORRECT |
| q37: semantic distance / chunk gap | WRONG — gold-label error in test set |
| q16/s04: ae.md token truncation | WRONG — ae.md chunks are 138–330 tokens, no truncation |
| s05: vs.md token truncation | WRONG — vs.md chunks are 1209–2727 tokens, no truncation |

---

## 5. Methodology Flags

### Flag 1 — Substring matching is correct but asymmetric
`any(exp in src for src in retrieved_sources)` where `exp = "terminology/core/ae.md"` and `src` is a relative path like `"terminology/core/ae.md"`. This works correctly because the RAG engine strips the KB root prefix (line 123 of `server/rag.py`). No bias introduced here.

### Flag 2 — q37 gold-label error inflates "representation gap" count by 1
The file `model/04_special_purpose.md` does not exist. The correct KB file is `model/03_special_purpose_domains.md`. The effective K=100 ceiling is **overall 95.3%** (52 of 53 evaluable questions, discounting q37), not 93.4%. The "5 questions missing" count should be treated as "4 genuine retrieval failures + 1 test-set bug."

### Flag 3 — Token truncation claim is not supported by evidence
Writer invokes "embedding truncation at >8191 tokens" as the root cause for ae.md/vs.md misses. The actual indexed chunks are 138–2727 tokens — all well within limit. The correct diagnosis for these misses is semantic retrieval distance (variable name "AESEV"/"VSTESTCD" not appearing in the chunk header or being close enough in embedding space to the chunk's section title).

### Flag 4 — n=13 per category limits statistical precision
At n=13, each question = 7.7 percentage points. The "65.4%" vs "61.5%" difference (K=20 vs K=15 in cross_domain) is exactly 1 question. Claims about gradient shape (e.g., "K=20/30 几乎无增益") are correct numerically but reflect discrete step-function behavior at this sample size, not a smooth plateau. This is noted as a framing caution, not an error.

### Flag 5 — top5_sources is the only per-question retrieval evidence stored in JSON
The JSON records only the top-5 source paths. The `source_misses` field is authoritative (computed over all K chunks by the eval runner), but there is no way to audit which rank position the missed chunk appears at (or confirm it is absent vs. ranked 6-100). This makes the "ranked >15" claim for individual questions unverifiable from the stored artifacts alone. The K-sweep aggregate monotonicity is the only available proxy.

---

## 6. Overall Verdict

| Claim | Verdict |
|-------|---------|
| Central claim: cross_domain/concept deficits are mainly a ranking problem → rerank is appropriate | **CONDITIONAL PASS** — supported by 7/12 recovery and full monotonicity, but concept recovery is only 50/50 and candidate pool must be K≥100 to capture all recoverable cases |
| Secondary claim: 5 K=100 misses are representation gaps tied to token truncation + VARIABLE_INDEX chunking | **PARTIAL PASS** — q34/VARIABLE_INDEX diagnosis is correct; q37 is a gold-label test-set error; ae.md and vs.md token-truncation claims are factually wrong (chunks are small, failure is semantic distance) |

**Required corrections before the doc is used as a decision artifact:**
1. Fix q37 gold-label: update `test_set_v1.yml` to point to `model/03_special_purpose_domains.md`. The true K=100 ceiling is ~95.3% (not 93.4%), which already exceeds the 95% goal if q37 is excluded — this changes the T5/reranking urgency assessment.
2. Remove "embedding truncation" as root cause for ae.md/vs.md misses. Replace with "semantic distance between variable-name queries and codelist section headers."
3. Note that "rerank 候选池需 ~100" not "≥50" to capture all ranking-recoverable questions (q07, q09 still at 0.0 at K=50).
