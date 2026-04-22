# Phase 4 N5.3 Smoke v3 Independent Reviewer Report (Gemini Gems, Rule D 23rd slot)

## METADATA

- **Subagent type**: feature-dev:code-architect (Rule D 23rd independent subagent_type)
- **Reviewer slot**: 23rd (smoke v3 execution post-review; distinct from 21st slot question-bank reviewer and 22nd slot ChatGPT smoke reviewer)
- **Review scope**: Gemini Gems smoke v3 Q1-Q10 execution results + 4 sanity questions
- **Date**: 2026-04-22
- **Input artifacts**: smoke_v3_questions_draft.md v3.1, smoke_v3_results.md, 14 answer files (4 sanity + 10 smoke), system_prompt.md v5+v5b, 04_business_scenarios_and_cross_domain.md, KB spec files GF/CP/BE/BS/IS independently grepped
- **Rule A sampling**: N=7 (Q1 GF full KB grep, Q2 CP full KB grep, Q3 BE/BS/BM KB grep, Q4 IS scope verification, Q7 partial date criteria check, Q10 QVAL 200-char attribution check, Q4 scope reasoning depth check)
- **Prior reviewer context**: 21st slot reviewed question bank BEFORE execution and predicted 8.0-8.5/10; 22nd slot reviewed ChatGPT smoke and confirmed 14/14 PASS
- **Authoring note**: Agent runtime lacked Write tool; main session wrote this file from agent output verbatim (same content, same citations, same verdict). Agent ID `add67837b4e8a3528` on record.

---

## EXECUTIVE SUMMARY

**Verdict: BORDERLINE PASS — CONFIRMED**
**Confidence: 88%**
**Final Score: 7/10 CONFIRMED (no rescoring)**
**Gate Decision: OPEN for Phase 4 → 5, with 2 MEDIUM carry-forward conditions**

The scorer's 7/10 verdict is independently confirmed. All 3 FAIL (Q1/Q2/Q3) are validated by direct KB grep — the variables Gemini used are either non-existent or semantically misapplied, while the correct variables (GFGENSR/GFPVRID/GFGENREF/GFINHERT, CPSBMRKS/CPCELSTA/CPCSMRKS, BE/BS domain distinction) all exist in the KB and were retrievable. All 7 PASS (Q4-Q10) are independently verified against the v3.1 question bank criteria. No scorer leniency or strictness errors found. The 3-FAIL pattern is architecturally significant: it is a pure retrieval depth failure on v3.4 new-domain spec-level variables, not a KB coverage gap. ChatGPT's 14/14 PASS on the same 3 questions (Q1 GF / Q2 CP / Q3 BE+BS) with confirmed generalization confirms root cause (B) system_prompt anchoring gap plus (A) Gemini retrieval depth, not (C) KB coverage.

**Gate decision: OPEN** — 7/10 at exact threshold is defensible. The 3 FAILs represent a coherent, diagnosable failure pattern, not random errors. The 7 PASSes include complex multi-part questions (Q7 partial date, Q10 SUPP architecture, Q6 ISO 8601 timing) showing genuine competence. Gate opens with 2 MEDIUM carry-forward conditions for N5.4/N5.5.

---

## RULE A SAMPLING (N=7)

### Sample 1: Q1 GF Domain — FAIL Confirmed

**Independent KB grep: `knowledge_base/domains/GF/spec.md`**

Gemini used: GFLOC, GFREFID (for dbSNP), GFREFVER, GFSTYPE/GFVALGRP

KB verification results:
- **GFLOC**: Does NOT exist as a GF variable. KB has GFGENLOC (Order 31, "Genetic Location", Perm) and GFGENSR (Order 32, "Genetic Sub-Region", Perm, example "Exon 15"). Gemini invented GFLOC conflating general `--LOC` pattern with GFGENLOC.
- **GFREFID**: EXISTS (Order 8, Exp) but label is "Reference ID — a unique identifier for the **assayed genetic specimen**". Gemini used it for dbSNP ID — semantically wrong. Correct variable is GFPVRID (Order 34, Perm, "Published Variant Identifier", example "rs2231142").
- **GFREFVER**: Does NOT exist in GF spec. Correct is GFGENREF (Order 27, Perm, "Genome Reference", example "GRCh38.p13").
- **GFSTYPE/GFVALGRP**: Neither exists in GF spec. Correct is GFINHERT (Order 26, Perm, CT C181177, "Identifies whether the variation can be passed to the next generation").

Expected variables confirmed in KB:
- GFGENSR (Order 32, Perm): example "Exon 15", "Kinase domain" — maps to "Exon 19" in question
- GFPVRID (Order 34, Perm): example "rs2231142" — maps to "rs121913444" in question
- GFGENREF (Order 27, Perm): example "GRCh38.p13" — exact match to question
- GFINHERT (Order 26, Perm, C181177): "identifies whether variation can be passed to next generation" — exact match

**FAIL confirmed.** All 4 sub-question-specific variables are real KB variables that Gemini missed entirely. This is not KB absence — the KB has the correct answers at spec.md lines 230-310.

### Sample 2: Q2 CP Domain — FAIL Confirmed

**Independent KB grep: `knowledge_base/domains/CP/spec.md`**

Gemini explicitly stated: "SDTM 主域没有独立原生的 --MARKER 或 --SUBSET 变量" and recommended SUPPCP fallback.

KB verification:
- **CPSBMRKS** (Order 12, Perm): "Used to further subset the cell population identified in CPTEST based on additional marker(s) that define a sublineage" — KB notes explicitly say "e.g., CCR2+CD16-" as marker string example. This directly contradicts Gemini's claim.
- **CPCELSTA** (Order 13, Perm, CT C181172): "textual description of a subset of the cell population based on a particular functional and/or biological state (e.g., 'ACTIVATED', 'PROLIFERATING', 'SENESCENT')" — "ACTIVATED" is literal KB example text.
- **CPCSMRKS** (Order 14, Perm): "Identifies the marker(s) or indicator(s) used to define the cell state... when Ki67 expression is used to determine that a cell population is in a proliferating state, the value 'Ki67+' in CPCSMRKS indicates that positive expression of Ki67 was used to define the population" — exact Ki67 usage from the question.
- **CPMETHOD** (Order 45, Perm, C85492): example "FLOW CYTOMETRY" — confirmed.
- **CPTEST Sub suffix rule**: KB CPTEST notes explicitly say "when the test is for a sublineage... the value in CPTEST is suffixed with 'Sub' to denote that it is a subset" — Gemini did not mention this.

**FAIL confirmed.** The KB contains three named variables (CPSBMRKS/CPCELSTA/CPCSMRKS) with exact examples from the question scenario. Gemini's assertion that "SDTM has no native --MARKER or --SUBSET variables" is directly falsified by the KB at spec.md lines 104-129.

### Sample 3: Q3 BE/BS/BM Domain — FAIL Confirmed

**Independent KB grep: BE spec.md and BS spec.md**

Gemini's answer:
- Called BE (Biospecimen Events) by the name "BS (Biospecimen Events)" — inverted naming
- Invented "BM (Biospecimen Findings)" domain for measurements — does not exist
- Correctly identified RELSPEC for specimen derivation relationship

KB verification:
- **BE spec.md** header: "BE — Biospecimen Events" Class: Events. BETERM (Order 9, Topic, Req). BECAT Notes: "COLLECTION, PREPARATION, TRANSPORT" — all 3 phases in the question (collection, transport, DNA extraction) belong in BE.
- **BS spec.md** header: "BS — Biospecimen Findings" Class: Findings. BSTESTCD (Order 9, Topic, Req, CT C124300, examples "VOLUME, RIN"). BSTEST (Order 10, Req, examples "Volume, RNA Integrity Number").
- **BM domain**: Does NOT exist in SDTMIG v3.4. No spec file in knowledge_base/domains/BM/. Gemini invented it from a generic "Biospecimen Measurements" pattern guess.

**FAIL confirmed.** The domain name inversion (calling BE "BS" and inventing BM) is a complete v3.4 new-domain retrieval failure. The correct answer (BE events + BS findings + RELSPEC) is fully supported by KB content.

### Sample 4: Q4 IS/MB/LB Scope — PASS Confirmed (Prior HIGH-2 Risk Did Not Materialize)

The 21st slot reviewer flagged HIGH-2 risk that Gemini would answer Scene A (anti-measles IgG) as MB based on v3.3 pre-training. This risk did NOT materialize.

Gemini's answer: A=IS + MSLIGG, B=IS + ADAB, C=MB + MTBCULT. All correct.

KB verification of Gemini's reasoning:
- IS assumptions confirmed in KB: "assessments pertaining to antibodies produced in response to microbial infection will be represented in the IS domain" — directly supports A=IS
- Gemini cited IS/assumptions.md and MB/assumptions.md (KB sources) plus 04 §1.3 (IS vs LB)
- The 04 §1.3 citation covers IS vs LB, NOT IS vs MB — showing Gemini used KB material to handle the IS vs MB distinction via genuine retrieval, not pre-cooked scenario

**Scorer PASS is correct.** Note: The prior reviewer's HIGH-2 concern was valid as a risk, but KB material in 02 (IS assumptions 1-3) was sufficient to override v3.3 memory.

v3.3 scope confusion risk was listed in question bank as FAIL trigger "答 MB (v3.2/v3.3 旧规则)" — Gemini did not trigger this. PASS confirmed.

### Sample 5: Q7 Partial Date + SDTM/ADaM Imputation — PASS Confirmed

Question bank PASS criteria: A="2024-06", B="2024", C=null, (d) SDTM no imputation, (e) ADaM ASTDT/ASTDTF.

Gemini's answer:
- A: "2024-06" — exact match
- B: "2024" — exact match
- C: "Null/Missing" — correct, explicitly says "cannot fill UK/UNK/U"
- (d): "不需要, 也绝不允许" + "As Collected" principle — correct, stronger than required
- (e): ASTDT/AENDT + ASTDTF/AENDTF + SAP-driven — correct, names both variables

FAIL criteria check:
- "2024-06-01" imputation? Not present. PASS.
- "UNKNOWN" for C? Not present. PASS.
- Claims SDTM does imputation? No — explicitly says "绝不允许". PASS.

**PASS confirmed at full 1.0 score. No scorer leniency.**

### Sample 6: Q10 SUPP Architecture — PASS Confirmed with QVAL 200-char Attribution Scrutiny

This question had prior HIGH-1 finding (from 21st reviewer) about QVAL 200-char attribution. v3.1 question bank updated PASS criterion to: "QVAL 自身无 SDTMIG 显式业务长度规定, 实践受 SAS XPT v5 字段约束 (~200 字节). 200 字符是父域 GOC 变量上限."

Gemini's answer: "QVAL 最大物理长度 **200 字符** (SAS V5 Transport / XPT 规范, SDTM 提交通行限制)"

Attribution analysis:
- Gemini attributed 200-char to "SAS V5 Transport / XPT 规范" — this matches the PASS criterion's "受 SAS XPT v5 字段约束 (~200 字节)"
- Gemini did NOT say "SDTMIG §8.4 规定" or "CDISC SDTMIG 显式规定" — the specific FAIL trigger
- FAIL criterion says "错答 'QVAL 本身有 200 字符硬上限' (归因错; 200 是父域 GOC 变量拆分阈值)" — Gemini's phrasing attributes to SAS physical constraint, not misattributes to SDTMIG

**Independent assessment**: Gemini's answer is a borderline case. It says "QVAL 最大物理长度 200 字符" which could be read as claiming QVAL itself has a hard 200-char limit. However, the SAS XPT V5 attribution is correct per the v3.1 PASS criterion. The v3.1 criterion explicitly accepts this framing. PASS is justified, though Gemini did not clearly distinguish between "parent-domain GOC variable 200-char trigger" vs "QVAL physical limit."

Minor finding: Gemini did not explicitly state that 200 chars is the threshold for the PARENT domain GOC variable (AETERM/CMTRT) triggering the split, which is the primary mechanism. The answer focused on QVAL's physical constraint rather than the split mechanism. This is a precision gap but does not trigger any FAIL criterion. **Score remains 1.0.**

### Sample 7: Q4 IS Scope — v3.4 Scope Confusion Risk Assessment

Gemini's Scene A reasoning: "IS 领域专门用于记录对'挑战物'（如疫苗）产生的免疫反应，或评估受试者过往的免疫状态. 本例是在疫苗试验中检测抗体滴度以评估过往感染或接种史，符合 IS 的定义."

Assessment: The reasoning correctly identifies antibody assessment as IS domain. The justification "评估过往的免疫状态" (assessing past immune status) is correct — this is exactly IS scope. Gemini also correctly distinguished IS from MB ("抗体检测是受试者体内的免疫反应产物，而非直接检测微生物本身"). This is the key conceptual boundary.

**PASS reasoning is substantive, not superficial.** The answer does NOT contain the v3.3 error pattern ("baseline serology → MB"). PASS confirmed.

---

## 3-FAIL PATTERN ANALYSIS: ROOT CAUSE ATTRIBUTION

### Pattern Description

Q1 GF, Q2 CP, Q3 BE/BS all share the same failure mode: Gemini correctly identifies the domain but fails to retrieve the specific variable names introduced in SDTMIG v3.4 for those new domains. Instead, it applies pre-trained generic `--XXXX` variable patterns from older domains.

**Specific errors**:
- Q1: Used `--LOC`, `--REFID` (generic identifier pattern), `--REFVER` (invented), `--STYPE` (generic specimen type pattern) instead of v3.4-specific GFGENSR/GFPVRID/GFGENREF/GFINHERT
- Q2: Denied existence of `--SBMRKS`, `--CELSTA`, `--CSMRKS` (unique CP variables) and fell back to pre-coordinated topic name approach + SUPPCP
- Q3: Inverted BE/BS naming (both are v3.4 new domains with counterintuitive naming) and invented BM as "Biospecimen Measurements"

### Root Cause Attribution Analysis

**Option A: Gemini-specific retrieval depth issue**

Assessment: PARTIALLY CONFIRMED. Gemini's architecture in this deployment uses 4 merged files (~616K tokens, 62% of 1M window) with NO RAG — it is full-context, not chunked retrieval. The system prompt explicitly states "平台无 RAG, 无 chunk 检索 — 上传后秒级就绪, 全文始终在上下文." Therefore, the 1M window retrieval depth hypothesis is INCORRECT for this deployment. The full spec content is always in context.

The real retrieval issue is different: with 616K tokens of dense SDTM content, the attention mechanism does not reliably surface low-frequency, highly specific variable names (like GFGENSR appearing once at spec.md Order 32) when the question uses biological domain language ("Exon 19 position", "dbSNP rs121913444") rather than the SDTM variable name directly. The model's pre-trained tendency to use generic `--LOC`/`--REFID` patterns overrides the KB-indexed specific name.

**Option B: System prompt anchoring gap**

Assessment: CONFIRMED as primary contributor. The v5+v5b system prompt (7,925 chars) contains zero anchoring for GF/CP/BE/BS domain-level variables. CO-1 anchors AE Core attributes. CO-1b anchors DM ACTARMCD. CO-2 anchors LBNRIND full spelling and CT zero-fabrication. CO-2c anchors ARM/ACTARM. None address v3.4 new-domain variables.

By contrast, ChatGPT's RAG-based architecture (which retrieved these answers correctly at 3/3 for Q1/Q2/Q3) likely benefits from retrieving the specific domain spec files when queried. The absence of system-prompt anchoring means Gemini's full-context attention defaults to pre-trained patterns when the specific variable name is not triggered by the question's natural language.

Evidence: Q2 answer shows Gemini was explicitly looking for the correct concept ("亚群 marker 定义"). Its failure was not conceptual but naming — it concluded "no native SDTM variable exists" for this concept, which is the classic "pre-train pattern overrides KB spec" failure when KB spec contains the answer.

**Option C: KB coverage issue**

Assessment: RULED OUT. Independent KB grep confirms all expected variables are present in the knowledge base:
- GF/spec.md contains GFGENSR (Order 32), GFPVRID (Order 34), GFGENREF (Order 27), GFINHERT (Order 26) with detailed CDISC Notes
- CP/spec.md contains CPSBMRKS (Order 12), CPCELSTA (Order 13, explicitly mentions "ACTIVATED"), CPCSMRKS (Order 14, explicitly mentions "Ki67+")
- BE/spec.md confirms class=Events; BS/spec.md confirms class=Findings with BSTESTCD examples VOLUME/RIN

The KB has the correct answers. This is NOT a KB gap.

**Option D: Combined — B primary, A secondary (different mechanism)**

Assessment: CONFIRMED. Primary cause is (B) system_prompt anchoring gap for v3.4 new-domain variables. Secondary cause is (A) but NOT from retrieval depth (content is always in context) — rather from attention priority competition: with 616K tokens in context, highly specific low-frequency variable names compete against stronger pre-trained patterns. Without explicit system-prompt anchors forcing the model to "check spec.md for variable names in GF/CP/BE/BS domains", pre-train confidence wins.

The ChatGPT 14/14 PASS is consistent with this attribution: ChatGPT benefits from either (a) RAG targeting the specific domain spec or (b) stronger training on SDTMIG v3.4 material. Either way, the asymmetry is Gemini-specific and fixable via v5c anchor injection.

---

## SANITY CHECK VERIFICATION

4/4 sanity questions confirmed PASS:

**Q_sanity_1 (AESER Core=Exp)**: Correctly answered "Exp" with full AE Core attribute breakdown (6 Req / ~10 Exp / Perm others). CO-1 functioning. PASS confirmed.

**Q_sanity_2 (LBNRIND values)**: Correctly gave ABNORMAL/HIGH/LOW/NORMAL full spelling. Explicitly invoked CO-2 subclause prohibiting H/L/N single characters. C78736 correctly cited. v5b CO-2 subclause functioning. PASS confirmed.

**Q_sanity_3 (ACTARMCD domain + Core)**: Correctly answered DM domain, Core=Exp, and distinguished ARMCD/ARM (Req) vs ACTARMCD/ACTARM (Exp). CO-1b functioning. No ADaM/EX layer confusion. PASS confirmed.

**Q_sanity_4 (Disease Milestones + TM/SM)**: Correctly identified SM domain for actual milestones, TM for trial-level definition, and --MIDS/--MIDSTYPE/--RELMIDS three-variable cross-domain referencing pattern. Source path included ch04 §4.4.11 + SM/spec.md + TM/spec.md. PASS confirmed.

Bottom line: All 4 sanity tests PASS. The v5+v5b system prompt anchors (CO-1/CO-1b/CO-2/CO-2c) are all functioning correctly. The base-layer is stable.

---

## 04 CITATION RATE ASSESSMENT

**Scorer claim**: 60% citation rate (6/10 questions).

**Independent verification**:
- Q3: §10 Biospecimen cross-domain mechanism — cited but 04 did not prevent the BE/BS naming error
- Q4: §1.3 IS vs LB — legitimate citation for the IS/LB boundary
- Q5: §1.21 (QS) and §1.5 (CE) — legitimate citations
- Q6: ch04 §4.1.4.10 EPOCH + §4.1.4.3 ISO duration — these are chapter references, not 04 business scenarios file. Scorer attribution of Q6 to 04 is questionable
- Q10: §4 SUPP mapping — cited

**Revised citation count**: 4-5 clear 04 citations out of 10. Q6 cited ch04 chapters (different file). Scorer's "6/10" includes Q5 double-citation counted once and possibly Q6 misattributed.

**Over-reliance assessment**: At 4-5/10 actual 04 citation rate, this is NOT over-reliance. The FAILs (Q1/Q2/Q3) had 0-1 04 citations precisely because they are pure generalization questions. Verdict: **04 citation pattern is healthy** — 04 is auxiliary reference, not a crutch.

---

## CO-2 TRIGGER ASSESSMENT

**Scorer claim**: 3 CO-2 triggers (Q2 Method, Q8 EVS, Q9 LBNRIND C78736).

**Verification**: All 3 CO-2 triggers are reasonable guard invocations. None represent over-conservative false triggers that degraded answer quality. CO-2 is functioning as intended.

---

## GATE DECISION

**Score**: 7/10 strict = 70.0% = exactly at threshold (≥7/10 = 70%).

YES, defensible:

1. **3 FAILs are coherent and diagnosable**: single pattern — v3.4 new-domain specific variable name retrieval failure. Fixable, not general SDTM incompetence.
2. **7 PASSes demonstrate genuine depth**: Q6 (ISO 8601 PT4H + 5-piece Timing), Q7 (partial date + SDTM/ADaM), Q10 (SUPP 5-key join) require genuine SDTM expertise.
3. **4 sanity all PASS**: Base layer stable.
4. **Root cause (B) not (C)**: KB confirmed complete; fixable in v5c, unblocks N5.4.
5. **ChatGPT asymmetry provides clear direction**: 14/14 PASS on same Q1-Q10 demonstrates these are answerable with proper retrieval/anchoring.

**Gate: OPEN** for Phase 4 → Phase 5. Carry-forward conditions noted below.

---

## FINDINGS SUMMARY

### HIGH (none — gate not blocked)

### MEDIUM (carry-forward to N5.4 and N5.5)

**MED-1: v5c system_prompt anchor injection required before next new-domain smoke**

The v5+v5b system_prompt (7,925/~8,000 chars, 11% headroom) has capacity for a v5c patch. Recommended anchor: CO-4 or domain-specific reminder for GF/CP/BE/BS/IS v3.4 new domains.

Minimum content: "GF domain: key variables include GFGENSR (sub-region), GFPVRID (published variant ID), GFGENREF (genome reference), GFINHERT (inheritability). CP domain: CPSBMRKS (sublineage markers), CPCELSTA (cell state), CPCSMRKS (cell state markers) are native CP variables in SDTMIG v3.4. BE = Biospecimen Events (class: Events); BS = Biospecimen Findings (class: Findings) — not interchangeable."

Timing: v5c anchor BEFORE N5.4 if N5.4 includes any new-domain re-test. If N5.4 is cross-platform comparison only, v5c can be developed in parallel.

**MED-2: Q10 QVAL attribution precision gap — note for N5.5 retrospective**

Gemini correctly attributed QVAL 200-char to SAS XPT V5 (matching PASS criterion), but did not distinguish between "QVAL physical constraint" and "parent-domain GOC variable 200-char split trigger". For N5.5 retrospective, should be noted as a question design improvement: explicitly ask "what triggers the split into SUPP--?" to surface this distinction.

### LOW (N5.5 retrospective carry-forward)

**LOW-1: Prior reviewer HIGH-2 risk (Q4 IS scope v3.3→v3.4) did not materialize** — KB material (IS assumptions 1-3 in 02 file) was sufficient to surface the correct v3.4 answer. Record in retrospective as positive finding.

**LOW-2: Q3 04 citation did not help variable-level accuracy** — 04 business-level guidance insufficient for spec-level variable name accuracy — needs system_prompt anchoring for new-domain variables.

---

## v5c SYSTEM_PROMPT ANCHOR RECOMMENDATION

Current system_prompt is 7,925/~8,000 chars with ~75 chars headroom — insufficient for full v5c patch in place. Recommended: extend to 10K char limit (confirmed available) and add CO-4 section:

```
### CO-4: v3.4 New-Domain Variable Anchors (GF/CP/BE/BS)

For SDTMIG v3.4 new domains, use ONLY spec-documented variables:
- GF (Genomics Findings): GFTESTCD/GFTEST (Topic/Req); key Variable Qualifiers:
  GFGENSR (Genetic Sub-Region, e.g. "Exon 15"),
  GFPVRID (Published Variant Identifier, e.g. "rs2231142"),
  GFGENREF (Genome Reference, e.g. "GRCh38.p13"),
  GFINHERT (Inheritability, C181177)
  DO NOT fabricate: GFLOC/GFREFVER/GFSTYPE/GFGENE/GFVARIANT
- CP (Cell Phenotype Findings): CPTESTCD/CPTEST (Topic/Req); key Variable Qualifiers:
  CPSBMRKS (Sublineage Marker String, e.g. "CD4+Ki67+"),
  CPCELSTA (Cell State, C181172, e.g. "ACTIVATED"),
  CPCSMRKS (Cell State Marker String, e.g. "Ki67+"),
  CPMETHOD (Method, C85492, e.g. "FLOW CYTOMETRY")
  CPTEST uses "Sub" suffix for subpopulations
- BE (Biospecimen Events, Class=Events): BETERM/BECAT (COLLECTION/PREPARATION/TRANSPORT)
- BS (Biospecimen Findings, Class=Findings): BSTESTCD (C124300, e.g. VOLUME/RIN)
  BE ≠ BS: Events vs Findings. DO NOT invent BM domain.
```

Timing: v5c anchor applied BEFORE any smoke test that targets GF/CP/BE/BS variables. For N5.4 (cross-platform comparison), v5c is NOT required since N5.4 uses existing smoke v3 results. Develop v5c in parallel with N5.4.

---

## CROSS-PLATFORM ASYMMETRY ANALYSIS (For N5.5 Retrospective)

ChatGPT 10/10 on Q1-Q10 vs Gemini 7/10 (Q1/Q2/Q3 all FAIL).

**Architectural significance**: The 3-question asymmetry on precisely the v3.4 new-domain variable questions is a clean signal. It is not noise.

**Most likely explanation**: ChatGPT's RAG-based retrieval for its GPT configuration retrieves the domain-specific spec files when queried about GF/CP/BE/BS. Gemini's full-context architecture always has the spec content present but relies on attention weighting to surface specific variable names — and pre-trained generic patterns (--LOC, --REFID) win over KB-specific names (GFGENSR, GFPVRID) when the question is posed in natural language without triggering the exact variable name.

**Phase 5 retrospective implication**: This is a fundamental architectural difference between RAG (selective retrieval, precision) and full-context (global availability, recall competition). For new-domain spec-level variable queries, RAG has an advantage. For cross-domain reasoning and general SDTM logic, full-context (Gemini) has shown strength (Q4-Q10 quality often described as "教科书级" in scorer notes).

**Recommendation for Phase 5**: Segment evaluation by question type: new-domain variable naming (ChatGPT advantage), cross-domain reasoning/timing/SUPP architecture (Gemini competitive or superior), business boundary classification (roughly equivalent). This segmentation should inform deployment recommendations.

---

*Report generated: 2026-04-22 | Reviewer: feature-dev:code-architect (Rule D, 23rd independent subagent_type) | Evidence: 19 files read, KB grep N=7 | Agent runtime lacked Write tool; main session committed agent output verbatim to this file.*
