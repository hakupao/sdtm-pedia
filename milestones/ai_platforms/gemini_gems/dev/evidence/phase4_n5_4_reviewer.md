# Phase 4 N5.4 Cross-Platform AB Report — Independent Reviewer Report (Rule D, 25th subagent_type)

## 1. METADATA

- **Date**: 2026-04-22
- **Reviewer subagent_type**: feature-dev:code-explorer (Rule D 25th independent slot)
- **Reviewer role strength**: Tracing execution paths, mapping architecture layers, understanding data dependency chains, documenting cross-component relationships — applied here to trace the evidence dependency chain across AB_REPORT sections and verify cross-platform reasoning integrity
- **File reviewed (primary)**: `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/ab_reports/STAGE_PHASE4_AB_REPORT.md` (264 lines, 8 sections)
- **Auxiliary files independently read** (not relying on writer's descriptions):
  - `ai_platforms/gemini_gems/dev/evidence/smoke_v3_results.md` — baseline 10-question results
  - `ai_platforms/gemini_gems/dev/evidence/smoke_v3_answers/Q1_v5c_answer.md` — delta Q1 raw answer
  - `ai_platforms/gemini_gems/dev/evidence/smoke_v3_answers/Q2_v5c_answer.md` — delta Q2 raw answer
  - `ai_platforms/gemini_gems/dev/evidence/smoke_v3_answers/Q3_v5c_answer.md` — delta Q3 raw answer
  - `ai_platforms/gemini_gems/dev/evidence/smoke_v3_v5c_delta.md` — delta synthesis report
  - `ai_platforms/gemini_gems/dev/evidence/phase4_n5_3_smoke_reviewer.md` — reviewer 23 report (read for chain validation, not adopted as authority)
  - `ai_platforms/gemini_gems/dev/evidence/_progress.json` — N5.4 block + N5.3 block
  - `ai_platforms/gemini_gems/current/system_prompt.md` — v5c live (CO-4 section read in full)
  - `ai_platforms/gemini_gems/current/system_prompt_v5c_draft.md` — existence check (file does not exist — deletion confirmed)
  - `knowledge_base/domains/GF/spec.md` — independent variable grep (GFGENSR/GFPVRID/GFGENREF/GFINHERT)
  - `knowledge_base/domains/CP/spec.md` — independent variable grep (CPSBMRKS/CPCELSTA/CPCSMRKS)
  - `knowledge_base/domains/BE/spec.md` — independent Class + BETERM + BECAT grep
  - `knowledge_base/domains/BS/spec.md` — independent Class + BSTESTCD + BSORRES grep
- **Verdict**: **PASS**

---

## 2. VERDICT

**PASS** — The AB_REPORT is internally consistent, evidence-anchored, and the cross-platform reasoning is sufficiently qualified. The v5c CO-4 fix is real and verifiable in the live system_prompt. The v3.4 KB variables cited are independently confirmed. The "equivalent 10/10" claim for Q4-Q10 is explicitly flagged as an inference with stated assumptions, not asserted as fact. Three findings are raised (1 MEDIUM, 2 LOW) but none are blockers.

**Confidence: 91%**

---

## 3. CROSS-SECTION DEPENDENCY CHAIN TRACE

This is the core code-explorer contribution: tracing the data flow from evidence through inference to conclusion, identifying any broken links.

```
[KB spec files] ──grep──► [§4.1 Root cause attribution: (B)/(A)/(C)]
                                │
                                ▼
[smoke_v3_results.md] ──────► [§1 Q1-Q10 matrix: 7/10 baseline]
         │                          │
         │                          ▼
         │                  [§3 Cross-platform matrix: Gemini 7/10 vs ChatGPT 10/10]
         │                          │
         │                          ▼
         │                  [§4 Architectural diff: RAG select vs attention-compete]
         │
         ▼
[Q1/Q2/Q3_v5c_answer.md] ──► [§5.1 Delta matrix: 3/3 PASS]
         │                          │
         │                          ▼
         │                  [§5.2 CO-4 efficacy judgment: "≥3/3 threshold met"]
         │                          │
         │              ┌───────────┘
         │              │   [INFERENCE NODE]
         │              ▼   Q4-Q10 equivalent 10/10
         │          (not rerun — stated assumption)
         │                          │
         │                          ▼
         │                  [§5.4 Cross-platform post-v5c: 10/10 vs 10/10, gap 0pp]
         │                          │
         ▼                          ▼
[smoke_v3_v5c_delta.md] ──────► [§6 Phase 5 carry-overs: O-1/O-2/O-3, G-1/G-2/G-3, D-1/D-2/D-3]
         │
         ▼
[system_prompt.md v5c] ──────► [§7 Evidence paths: "current/system_prompt.md v5c live"]
         │
         ▼
[_progress.json N5.4 block] ──► [§8 Next steps alignment]
```

**Chain integrity assessment**:

- `§1 → §3`: Data link is intact. §3 matrix is a direct derivative of §1 Q1-Q10 table, with ChatGPT baseline values consistent with what is stated in the cross-platform context. No fabricated values detected.
- `§3 → §4`: The architectural reasoning (RAG select-retrieve vs full-context attention-compete) is a qualitative inference. It is not itself verifiable from the files in scope, but it is consistent with the observed data pattern and correctly scoped as an explanation, not a proven mechanism.
- `§4 → §5.1`: The v5c delta answers (Q1/Q2/Q3_v5c_answer.md) are real files with Gemini raw answers. The delta matrix accurately summarizes what is in those files. Chain is intact with evidence backing.
- `§5.1 → §5.2 (INFERENCE NODE)`: The "equivalent 10/10" for Q4-Q10 is the most important judgment call in the report. The report states the assumption explicitly in `smoke_v3_v5c_delta.md §2`: "v5c 只加 CO-4 不动其他 CO 段 + KB uploads 不变, 无回归风险假设". This is a reasonable but unverified assumption. The report does flag it: "若要严格验证无回归, Phase 5 可选跑 'v5c 全 10 题' 全量回归, 作为 RETROSPECTIVE 补证." The inference is qualified — this is acceptable for a gate decision but should be noted in Phase 5 carry-over.
- `§5.2 → §5.4`: Cross-platform closure claim "gap 30pp → 0pp" follows directly from the 3/3 PASS delta + Q4-Q10 equivalence assumption. The chain is structurally sound given the stated premise.
- `§5 → §6`: Phase 5 carry-overs (O-1/O-2/O-3, G-1/G-2/G-3, D-1/D-2/D-3) are well-grounded in the evidence sections. No carry-over appears to have been fabricated or to lack a traceable origin in §1-§5.
- `§6 → §7`: Evidence path list is independently verifiable. All files listed under §7 were found to exist. The one claim "current/system_prompt_v5c_draft.md — 已删" was independently verified: the file does not exist at `ai_platforms/gemini_gems/current/system_prompt_v5c_draft.md`.

**No broken links found in the dependency chain.**

---

## 4. SECTION-BY-SECTION INDEPENDENT REVIEW

### §1 — Gemini Smoke v3 10-Question Matrix (Baseline v5)

**Review**: The §1 matrix aligns exactly with `smoke_v3_results.md`. The sanity 4/4 PASS claims (LBNRIND full-write, AESER Core=Exp, ACTARMCD Core=Exp) are consistent with the v5+v5b system_prompt CO-1/CO-2/CO-2c anchors which I independently read in `current/system_prompt.md`. The 04 citation rate (6/10, 60%) and CO-2 trigger count (3) match the smoke_v3_results.md table.

One minor observation: the §1.2 table cites "source: `dev/evidence/smoke_v3_results.md`" but does not embed per-question answer file links. This is a documentation style choice, not a data integrity issue — the 14 answer files are all listed in §7.

**Verdict**: PASS. Data accurately sourced and internally consistent.

### §2 — Rule D Independent Reviewer (23rd subagent_type, code-architect)

**Review**: The reviewer 23 report at `dev/evidence/phase4_n5_3_smoke_reviewer.md` is real and independently read. The N=7 Rule A sample size, 0 HIGH + 2 MEDIUM + 2 LOW finding counts, and BORDERLINE PASS CONFIRMED 88% verdict all match what is in the actual report file. The two MEDIUM findings (MED-1: CO-4 anchor injection recommendation; MED-2: Q10 QVAL split mechanism) are accurately described in §2's finding table. MED-1 disposition ("v5c applied to Gem UI 2026-04-22") is confirmed by the live system_prompt.md CO-4 section.

**Verdict**: PASS. Reviewer 23 summary is accurate.

### §3 — Cross-Platform Q1-Q10 Matrix (Baseline Era)

**Review**: The 3-row FAIL pattern (Q1 GF / Q2 CP / Q3 BE/BS) and 7-row PASS pattern are correctly represented. The ChatGPT 10/10 baseline is referenced as a known fact established by ChatGPT-side evidence (not independently verifiable from Gemini-side files alone, but consistent with the cross-platform context). The Q8/Q9 "F-R1 substitution" footnote (ChatGPT used EPOCH and CTCAE variant questions) is correctly noted as equivalent without creating a false equivalence — the report acknowledges the substitution was formally recorded in smoke_v3_questions_draft.md v3.2.

**Verdict**: PASS. Matrix is accurate.

### §4 — FAIL Attribution + Architectural Diff

**Review**: The three-factor attribution (Primary B: system_prompt anchor gap; Secondary A: attention competition; Ruled out C: KB coverage) is the most analytically complex section. The "Ruled out C" claim is the most critical and most verifiable.

Independent KB grep results (this reviewer):
- GFGENSR: Order 32, Core=Perm, confirmed in `GF/spec.md`
- GFPVRID: Order 34, Core=Perm, confirmed
- GFGENREF: Order 27, Core=Perm, confirmed
- GFINHERT: Order 26, Core=Perm, CT=C181177, confirmed
- CPSBMRKS: Order 12, Core=Perm, confirmed in `CP/spec.md`
- CPCELSTA: Order 13, Core=Perm, CT=C181172, confirmed
- CPCSMRKS: Order 14, Core=Perm, confirmed
- BE Class=Events, BETERM Core=Req (Order 9), BECAT Core=Perm (Order 12), examples include COLLECTION/PREPARATION/TRANSPORT — confirmed in `BE/spec.md`
- BS Class=Findings, BSTESTCD Core=Req (Order 9), CT=C124300, examples VOLUME/RIN — confirmed in `BS/spec.md`

All 10 variables independently verified. "Ruled out C: KB coverage" is correct.

One nuance: the report states the AB_REPORT §1.3 attributes the FAIL pattern to "reviewer 23 独立 grep 核". This reviewer independently duplicated that grep and reached identical conclusions — the attribution is correct.

The §4.2 reasoning on why ChatGPT passes Q1-Q3 (RAG top-k=20 can precisely retrieve rare-token spec segments) is qualitatively plausible and consistent with the architecture descriptions in both platforms. It is an inference, not a directly testable claim from these files — but it is not asserted as proven fact.

**Verdict**: PASS. Attribution is well-reasoned and the "KB ruled out" claim is independently confirmed.

### §5 — v5c CO-4 Delta (Post-Fix)

**Review**: This is the most evidence-heavy section. Three sub-checks:

**5a. v5c content in live system_prompt.md**: CO-4 section is present and complete in `current/system_prompt.md` lines 85-136. It contains:
- GF subsection with GFGENSR/GFPVRID/GFGENREF/GFINHERT by name, Core=Perm, with CT=C181177 for GFINHERT, and explicit "禁止臆造" list including GFLOC/GFREFVER/GFSTYPE
- CP subsection with CPSBMRKS/CPCELSTA/CPCSMRKS by name, Core=Perm, with CT=C181172 for CPCELSTA, CPTEST "Sub" suffix rule
- BE subsection with BETERM Core=Req, BECAT examples COLLECTION/PREPARATION/TRANSPORT/EXTRACTION
- BS subsection with BSTESTCD/BSTEST Core=Req, CT=C124300, examples VOLUME/RIN
- BE vs BS boundary table with 5 scenario rows and RELSPEC (not RELREC) for specimen hierarchy
- 4 execution rules

This matches the §5 report description exactly.

**5b. Draft file deleted**: `current/system_prompt_v5c_draft.md` does not exist. Deletion confirmed.

**5c. Delta answer quality**: Q1_v5c_answer.md, Q2_v5c_answer.md, Q3_v5c_answer.md all contain raw Gemini answers that demonstrate:
- Correct variable naming (GFGENSR/GFPVRID/GFGENREF/GFINHERT for Q1; CPSBMRKS/CPCELSTA/CPCSMRKS for Q2; BETERM/BECAT/BSTESTCD for Q3)
- Active echo of negative anchors ("绝对不能套用 GFLOC/GFREFVER/GFSTYPE" in Q1; "无需使用 SUPPCP 补充记录" in Q2; "v3.4 中不存在且严禁臆造 BM 域" in Q3)
- The source paths cited by Gemini in the answers point to `knowledge_base/domains/{GF|CP|BE|BS}/spec.md` rather than the aggregated `02_domains_spec_and_assumptions.md` — indicating the CO-4 anchor caused deeper spec routing

**5d. The Q4-Q10 equivalence inference**: The report explicitly and repeatedly qualifies this as an inference, not a retest result, in the delta report: "v5c 只加 CO-4 不动其他 CO 段 + KB uploads 不变, 无回归风险假设". The `smoke_v3_v5c_delta.md` §2 table makes this explicit with a "假设 (未重测但低风险)" header and proposes "Phase 5 可选跑 'v5c 全 10 题' 全量回归" as a补证 option. This is appropriately scoped. The claim "等价 10/10" is a conditional, not an asserted empirical result — and it is represented as such.

**Verdict**: PASS. Delta evidence is real. CO-4 content is verified in live system_prompt. Draft deletion confirmed. Equivalence assumption is explicitly scoped.

### §6 — Phase 5 Carry-Overs

**Review**: The three finding dimensions (O observations, G gaps, D decision reviews) map correctly to the evidence:

- O-1 (7 PASS on non-v3.4 layers): Grounded in §1 Q4-Q10 results
- O-2 (04 60% citation rate as supplement not substitute): Grounded in §1.4 citation data
- O-3 (Sanity 4/4 stable): Grounded in §1.1 sanity results
- G-1 (v5 had no v3.4 anchor): Grounded in §4.1 primary root cause
- G-2 (v5c no negative examples initially): This is a prospective concern that was rendered moot by 3/3 PASS — the report notes this but accurately presents it as "若 delta ≤1/3 PASS, 需补负例" (conditional on test outcome). Since outcome was 3/3 PASS, this gap is effectively resolved but preserved as a general pattern note for future domains.
- G-3 (attention competition in full-context underestimated): Grounded in §4.3
- D-1 (C strategy was right for non-v3.4 layers, not sufficient for new-domain variable layer): The nuance here is correct — the report notes the terminology drop was a tradeoff, not a mistake, while acknowledging it removed the secondary CT anchor for v3.4 new domains. This is a defensible balanced judgment.
- D-2 (v5c parallel production): Confirmed correct in hindsight given 3/3 PASS.
- D-3 (Gate OPEN at 7/10 borderline): Already confirmed by reviewer 23.

**Verdict**: PASS. All carry-overs are traceable to evidence.

### §7 — Evidence Paths

**Review**: All files listed under "主 evidence" and "v5c 资产" and "跨平台对照" either exist (verified) or have confirmed deletion status. The smoke_v3_answers directory files (14 answer files) are all listed in `_progress.json` evidence_paths under the N5.3 step block. The delta files (Q1/Q2/Q3_v5c_answer.md, smoke_v3_v5c_delta.md) exist and were read. The cross-platform reference files are listed accurately.

**Verdict**: PASS.

### §8 — Next Steps

**Review**: The §8 list was authored before the delta was executed (it was the "pre-fill" section). At report completion, steps 1-3 (user Web UI rerun + delta fill + progress write-back) are marked DONE in `_progress.json`. The remaining steps (Phase 4→5 gate confirm + Phase 5 RETROSPECTIVE + Rule D 24/25 audit) are appropriately sequenced.

**Verdict**: PASS. Next steps accurately represent the state at time of authoring and are consistent with _progress.json.

---

## 5. FINDINGS

### MEDIUM-1: Q4-Q10 Equivalence Claim Needs Phase 5 Verification Task to Be Formally Registered

**Severity**: MEDIUM
**Description**: The "等价 10/10" claim for Q4-Q10 post-v5c is logically sound given the scoped assumption (CO-4 only adds a new section, doesn't touch CO-1/CO-1b/CO-2/CO-2c/CO-3, KB unchanged). However, this is an unverified inference presented alongside verified delta results (3/3 retest). The risk is that a Phase 5 reader treats "10/10 (等价)" as an empirical result equal in weight to "3/3 PASS 完全生效".

The delta report does qualify this in `smoke_v3_v5c_delta.md §2` and the AB_REPORT §5.4 footnote. However, there is no formal Phase 5 carry-over item in §6 that specifically names "v5c full 10-question regression as optional verification task". G-2 partially covers this but frames it around negative examples, not around regression completeness.

**Recommendation**: Phase 5 RETROSPECTIVE should include an explicit entry: "Optional verification: run all 10 smoke v3 questions against v5c to confirm zero regression on Q4-Q10 (currently equivalent-assumed)." This is non-blocking for the gate but should be registered as a named carry-over.

**Disposition**: Phase 5 carry-forward, non-blocking.

### LOW-1: AB_REPORT Order Numbers in §4.1 "Ruled Out C" Are Slightly Inconsistent with KB

**Severity**: LOW
**Description**: AB_REPORT §4.1 states that the reviewer cited "KB spec Order 26/27/32/34" for GFINHERT/GFGENREF/GFGENSR/GFPVRID. This reviewer independently confirmed all four variables exist, but notes the AB_REPORT's §1.2 table header states "Order 26/27/32/34" while the reviewer 23 report and the actual spec.md assign: GFINHERT=Order 26, GFGENREF=Order 27, GFGENSR=Order 32, GFPVRID=Order 34. This matches. However, the AB_REPORT TL;DR at line 40 states "(KB spec Order 26/27/32/34 全存在)" — the order assignment is correct but the label reads ambiguously because the report uses "Order" as a shorthand citation without mapping which Order goes to which variable in that summary line. A reader checking independently might need to grep to reconcile.

**Impact**: No factual error. Minor traceability friction.
**Recommendation**: Future AB_REPORT summaries could spell out variable-to-Order mapping explicitly in the TL;DR line.

### LOW-2: §4.2 ChatGPT "RAG top-k=20" Claim Is Unverified from Gemini-Side Files

**Severity**: LOW
**Description**: §4.2 states "ChatGPT top-k=20 可在 2.53M tokens corpus 定向 pull v3.4 新域专属 spec 段". This is a cross-platform architectural claim. This reviewer did not read ChatGPT-side evidence files (Rule D independence requires not mixing the two platform lanes). The claim is plausible and consistent with the ChatGPT platform architecture as described in the Gemini-side _progress.json context, but from the perspective of the Gemini-side evidence chain, this is an externally asserted fact.

**Impact**: If the ChatGPT RAG configuration is actually different (e.g., top-k is not 20, or the terminology batch coverage is different), the attribution in §4.2 could be incorrect. This would not change the Gemini-side conclusions but could weaken the cross-platform architectural argument.

**Recommendation**: The cross-review by the main session (after receiving both #24 ChatGPT-side and #25 Gemini-side reports) should verify that the ChatGPT-side claims in this report match what reviewer #24 independently confirmed from the ChatGPT lane.

---

## 6. v3.4 NEW DOMAIN KB INDEPENDENT VERIFICATION RESULTS

This section contains this reviewer's direct KB grep results, performed independently without relying on reviewer 23's findings.

### GF Domain (Genomics Findings)

Source: `knowledge_base/domains/GF/spec.md`

| Variable | Order | Core | CT | Notes Label | Confirmed |
|---|---|---|---|---|---|
| GFGENSR | 32 | Perm | (none) | Genetic Sub-Region | YES — "Exon 15", "Kinase domain" examples match Q1 scenario |
| GFPVRID | 34 | Perm | (none) | Published Variant Identifier | YES — "rs2231142", "COSM41596" examples match Q1 scenario |
| GFGENREF | 27 | Perm | (none) | Genome Reference | YES — "GRCh38.p13" example matches Q1 scenario |
| GFINHERT | 26 | Perm | C181177 | Inheritability | YES — "whether variation can be passed to next generation" |

Fabricated variables from baseline (v5) confirmed absent:
- GFLOC: does not exist. Closest real variable is GFGENLOC (Order 31) or GFGENSR (Order 32) — Gemini conflated these.
- GFREFVER: does not exist. GFGENREF (Order 27) is the correct variable.
- GFSTYPE: does not exist in GF spec.
- Note: GFREFID (Order 8, Core=Exp) does exist but is for "assayed genetic specimen" identifier, not dbSNP variant IDs — Gemini's usage was semantically wrong.

**AB_REPORT claim verified**: "KB spec Order 26/27/32/34 全存在" — CONFIRMED.

### CP Domain (Cell Phenotype Findings)

Source: `knowledge_base/domains/CP/spec.md`

| Variable | Order | Core | CT | Notes Label | Confirmed |
|---|---|---|---|---|---|
| CPSBMRKS | 12 | Perm | (none) | Sublineage Marker String | YES — "CCR2+CD16-" example; explicitly for marker-defined sublineages |
| CPCELSTA | 13 | Perm | C181172 | Cell State | YES — "ACTIVATED", "PROLIFERATING", "SENESCENT" literal examples |
| CPCSMRKS | 14 | Perm | (none) | Cell State Marker String | YES — Ki67+ example matches Q2 question exactly |

CPTEST "Sub" suffix rule: confirmed in CPTEST (Order 11) CDISC Notes — "when the test is for a sublineage...the value in CPTEST is suffixed with 'Sub' to denote that it is a subset". This is in the spec file, not only in assumptions, meaning CO-4's reference to this rule is grounded in the primary spec.

**AB_REPORT claim verified**: "KB spec Order 12/13/14 全存在" — CONFIRMED. Baseline Gemini claim "SDTM 主域没有独立原生的 --MARKER/--SUBSET 变量" is a factual error directly contradicted by KB spec.

### BE Domain (Biospecimen Events)

Source: `knowledge_base/domains/BE/spec.md`

- Class: Events — confirmed in file header "Class: Events | Structure: One record per instance per biospecimen event..."
- BETERM (Order 9, Core=Req): "Topic variable for an event observation" — confirmed
- BECAT (Order 12, Core=Perm): "Category for Biospecimen Event. Example: COLLECTION, PREPARATION, TRANSPORT" — confirmed. Note: KB examples list COLLECTION/PREPARATION/TRANSPORT (3 examples), while CO-4 adds EXTRACTION as a 4th. The v5c Q3 answer correctly uses all 4. EXTRACTION is a reasonable extension of the PREPARATION/TRANSPORT pattern and is not contradicted by the spec's open "Example:" framing.

### BS Domain (Biospecimen Findings)

Source: `knowledge_base/domains/BS/spec.md`

- Class: Findings — confirmed in file header "Class: Findings | Structure: One record per measurement per biospecimen identifier per subject"
- BSTESTCD (Order 9, Core=Req, CT=C124300): "Short character value for BSTEST... Examples: VOLUME, RIN" — confirmed
- BSTEST (Order 10, Core=Req, CT=C124299): confirmed
- BSORRES (Order 13, Core=Exp), BSORRESU (Order 14, Core=Exp), BSSTRESC (Order 15, Core=Exp), BSSTRESN (Order 16, Core=Exp) — all confirmed

**AB_REPORT claim verified**: BE=Events, BS=Findings, BSTESTCD CT=C124300, examples VOLUME/RIN — all CONFIRMED. Baseline Gemini inversion (BS as Events, fabricated BM domain) is a documented factual error against the spec.

---

## 7. RULE D INDEPENDENCE SELF-CERTIFICATION

This reviewer (feature-dev:code-explorer, slot #25) operated under the following independence constraints:

1. Did not read the ChatGPT-side AB_REPORT or its reviewer #24's output — the cross-platform claims in this report are assessed only from the Gemini-side evidence chain.
2. Did not adopt reviewer 23's KB grep results as authoritative — all four KB domain spec files were read independently and variables located by this reviewer directly.
3. Did not read the previous 24 subagent_type reports in the Rule D chain. The reviewer 23 report (`phase4_n5_3_smoke_reviewer.md`) was read only to verify that the AB_REPORT's summary of reviewer 23's findings was accurate — not to adopt reviewer 23's reasoning as this reviewer's own.
4. This reviewer's perspective is architectural and dependency-chain-oriented: the core contribution is mapping data flows across AB_REPORT sections, identifying inference nodes, and assessing whether inferences are adequately qualified. This is distinct from: code correctness review (executor/debugger), semantic precision review (scientist/analyst), or test coverage review (test-engineer/tracer).
5. The "equivalent 10/10" inference node was flagged by this reviewer independently — it is a known pattern in dependency chain analysis where a downstream conclusion (cross-platform closure at 0pp gap) inherits the uncertainty of an upstream unverified assumption (Q4-Q10 no regression). This would be invisible to a reviewer focused purely on the verified delta results.

---

## 8. PHASE 5 RETROSPECTIVE ENTRY QUALITY ASSESSMENT

The AB_REPORT §5 and §6 collectively propose 3 primary findings for Phase 5 RETROSPECTIVE. This reviewer assesses the argument quality of each.

### F1: CO-4 Pattern Effective on Full-Context Architecture

**AB_REPORT argument**: system_prompt head-section anchor (~3K chars) corrected 3/3 new-domain variable naming FAIL in a 616K-token full-context architecture. This "推翻 baseline reviewer 23 悲观假设" (KB negative examples or 04 expansion needed).

**Argument quality assessment**: STRONG. The evidence is direct and unambiguous — three independently recorded Gemini answers show the exact variable names from CO-4, including active echo of negative anchors. The "pushin reviewer 23's pessimistic assumption" claim is honest — reviewer 23 did propose more aggressive strategies as a contingency. The result shows the minimal intervention was sufficient. This finding is correctly described as empirical evidence, not theory.

**One nuance worth noting**: The finding is only tested against 3 questions in 1 session. If Gemini had answered slightly differently on a different session (LLM non-determinism), the result might differ. The report does not acknowledge this. For Phase 5 this could be noted as: "CO-4 efficacy confirmed in 1 execution run of 3 questions; multi-run stability is untested."

**Verdict**: Argument is sufficient for Phase 5 RETROSPECTIVE. The non-determinism caveat is a minor addition, not a rewrite.

### F2: Prime Position Weight >> Capacity (Head Anchor > Tail Rare-Token)

**AB_REPORT argument**: System_prompt head anchor of ~3K chars has higher effective weight than 616K tokens of tail context for rare-token variable names. "Attention 竞争本质是 prime 位置问题非容量问题."

**Argument quality assessment**: PLAUSIBLE but THEORETICAL. This is the mechanistic explanation for why CO-4 worked, inferred from the result. It is consistent with known attention mechanism properties (recency bias, primacy bias, positional encoding). However, it is not directly measurable from these test results — the report conflates "CO-4 worked" (empirical) with "because prime position > capacity" (theoretical mechanism). These are separable claims.

The argument would be stronger if it acknowledged: we observe CO-4 worked; the prime position hypothesis is one explanatory mechanism; the alternative (CO-4 simply provided the right vocabulary tokens which KB also had but at lower attention-recall probability) cannot be distinguished from these results.

**Verdict**: Argument is sufficient for Phase 5 RETROSPECTIVE use. The mechanistic claim should be presented as a hypothesis, not a proven mechanism. The AB_REPORT does say "证 attention 竞争本质是 prime 位置问题" — the word "证" (proves) is slightly overstrong. Recommend softening to "suggests" in Phase 5 write-up.

### F3: Writer Checklist Gap + CO-4 4-Segment Structure for Template

**AB_REPORT argument**: The N4 writer producing v5 did not check whether new-domain spec variables were anchored in system_prompt. Phase 5 must add a writer checklist item: "每新域 spec 是否在 system_prompt 锚到". CO-4's 4-segment structure (positive variable list + negative prohibition + execution rules + CT binding) should be templated in `_template/`.

**Argument quality assessment**: STRONG for the checklist gap finding. Weak for the template recommendation in terms of specificity. The checklist gap is directly evidenced: v5 had CO-1/CO-1b/CO-2/CO-2c for pre-existing domains but nothing for GF/CP/BE/BS. The systemic failure is clear.

The template recommendation is the right direction but the AB_REPORT does not specify where in `_template/` this should go, what file, or what the exact trigger condition is (e.g., "when a new domain is added to KB uploads"). This is appropriate for a Phase 5 RETROSPECTIVE action item rather than a completed specification.

**Verdict**: Both the finding (checklist gap) and the recommendation (template) are adequately argued for Phase 5 use. The template spec should be fleshed out in Phase 5 as an action item.

---

## 9. SUMMARY TABLE

| Check | Result | Notes |
|---|---|---|
| §1→§3→§5→§6 dependency chain integrity | PASS | No broken links; inference node at §5.2 Q4-Q10 is qualified |
| §5 v5c delta evidence (3 answer files exist and match claims) | PASS | Q1/Q2/Q3_v5c_answer.md all verified |
| Draft file deleted | PASS | system_prompt_v5c_draft.md does not exist |
| CO-4 in live system_prompt.md | PASS | Lines 85-136, all 4 domain subsections present |
| GF variables independently grepped | PASS | GFGENSR/GFPVRID/GFGENREF/GFINHERT all confirmed, Order/Core/CT match |
| CP variables independently grepped | PASS | CPSBMRKS/CPCELSTA/CPCSMRKS all confirmed, Order/Core/CT match |
| BE Class=Events + BETERM/BECAT | PASS | Confirmed in BE/spec.md |
| BS Class=Findings + BSTESTCD/BSORRES | PASS | Confirmed in BS/spec.md, CT=C124300 confirmed |
| Q4-Q10 equivalence claim properly qualified | PASS with note | Report does qualify as assumption; MEDIUM-1 finding raised for Phase 5 registration |
| _progress.json N5.4 block consistency with AB_REPORT | PASS | Block confirms 3/3 PASS, v5c sync, and pending Rule D 24/25 review |
| Phase 5 F1/F2/F3 finding argument quality | F1 STRONG / F2 PLAUSIBLE / F3 STRONG | F2 "证" language slightly overstrong; non-determinism caveat missing |
| Rule D independence maintained | PASS | ChatGPT-side files not read; KB grep performed independently |

---

## 10. FILES ESSENTIAL TO UNDERSTANDING THIS REVIEW

- `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/ab_reports/STAGE_PHASE4_AB_REPORT.md` — primary reviewed artifact
- `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/evidence/smoke_v3_results.md` — baseline source
- `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/evidence/smoke_v3_v5c_delta.md` — delta synthesis
- `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/evidence/smoke_v3_answers/Q1_v5c_answer.md`
- `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/evidence/smoke_v3_answers/Q2_v5c_answer.md`
- `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/evidence/smoke_v3_answers/Q3_v5c_answer.md`
- `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/current/system_prompt.md` — v5c live with CO-4 (lines 85-136)
- `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/evidence/phase4_n5_3_smoke_reviewer.md` — reviewer 23 (for chain validation)
- `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/gemini_gems/dev/evidence/_progress.json` — N5.4 block
- `/Users/bojiangzhang/MyProject/SDTM-compare/knowledge_base/domains/GF/spec.md`
- `/Users/bojiangzhang/MyProject/SDTM-compare/knowledge_base/domains/CP/spec.md`
- `/Users/bojiangzhang/MyProject/SDTM-compare/knowledge_base/domains/BE/spec.md`
- `/Users/bojiangzhang/MyProject/SDTM-compare/knowledge_base/domains/BS/spec.md`

---

*Reviewer: feature-dev:code-explorer, Rule D slot #25. Read-only. Report prepared without reference to ChatGPT-side AB_REPORT or reviewer #24 output; chain independence maintained.*
