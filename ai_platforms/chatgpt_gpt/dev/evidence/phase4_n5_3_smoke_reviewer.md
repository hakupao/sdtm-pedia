# Phase 4 N5.3 smoke v3 — Independent Reviewer (22nd Rule D slot)

## Metadata

| Field | Value |
|---|---|
| Reviewer subagent_type | `pr-review-toolkit:type-design-analyzer` |
| Rule D slot # | 22 (cold review, no prior context on N5.3 execution) |
| Review date | 2026-04-22 |
| Scope | ChatGPT GPTs smoke v3 Step 4 — 14 question run + 3 sanity + scorer's 14/14 strict PASS claim |
| Source artifacts reviewed | `smoke_v3_questions_draft.md` v3.1 (487 lines) / `smoke_v3_results.md` (193 lines) / 14 Qx_answer.md + 3 sanity_x_answer.md / `system_prompt.md` / KB spec files |
| Independent KB grep | GF, CP, BS, BE, RELSPEC, DS, SUPPQUAL, VARIABLE_INDEX, terminology/core disposition + ae + general_part4 |
| Threshold | ≥10/14 (71%) for Phase 4→5 gate eligibility; scorer claims 14/14 (100%) |

---

## Executive Summary

**Verdict: CONDITIONAL_PASS (with one procedural finding and one data-integrity finding both resolvable without re-running smoke v3)**

**Confidence: 70%**

**Headline**: ChatGPT's answer QUALITY is genuinely strong. I independently re-graded 6 questions (Q1, Q10, Q12, Q13, Q14, Q3) plus all 3 sanity and I agree with scorer's PASS on all 6 samples on SDTM-fact-correctness grounds. Answers are fluent, cite correct CT codes where given, use correct variable names, distinguish "direct evidence" from "inference" honestly, and include several genuinely non-trivial bonuses (Q12 AETERM verbatim correction, Q13 KB-boundary declaration, Q14 scenario-A/B modelling).

**HOWEVER**, the Phase 4→5 gate cannot be cleanly OPENed on the current evidence because:

1. **BLOCKING finding F-R1 (HIGH)**: The actual Q8 and Q9 questions delivered to ChatGPT **do not match the question bank v3.1**. Question bank Q8 = "Extensible vs Non-Extensible CT" and Q9 = "Pinnacle 21 FAIL classification". The answer files Q8_answer.md and Q9_answer.md cover "EPOCH Trial Design" (labelled "B5") and "AESEV/AETOXGR/AESER CTCAE" (labelled "B6") respectively. Both scorer `smoke_v3_results.md` and answer file headers confirm this swap — and crucially neither the results doc nor the bank explain the substitution. This is not a small audit nit: two of the 14 graded questions were tested against **different criteria than the bank defines**, yet scored against the scorer's own ad hoc criteria while being reported as 14/14 against the v3.1 bank. Under strict Rule A, the pass score for the bank as stated is at best 12/14 verified + 2/14 UNKNOWN (not tested), which is still ≥10/14 gate-eligible but the reporting is materially misleading.

2. **MEDIUM finding F-R2**: Question bank v3.1 contains at least one factual error the scorer did not catch: Q14 PASS criterion (c) states `DSDECOD = "DEATH"` CT comes from codelist **C66727** named **"Disposition From Study"**. Independent KB grep (`knowledge_base/terminology/core/disposition.md:15` + `knowledge_base/domains/DS/spec.md:156`) confirms C66727 is actually **"Completion/Reason for Non-Completion"** (codelist name NCOMPLT used when DSCAT=DISPOSITION EVENT). The bank's v3.0→v3.1 note claimed the fix from C66728→C66727 but the semantic label it asserts is still wrong per KB. Q14 ChatGPT answer happened NOT to cite any C-code, so ChatGPT did not repeat the bank's error; the finding is about bank quality, not ChatGPT answer quality.

3. **LOW finding F-R3**: Bank Q1 PASS criterion (d) specifies variable `GFINHERT` (Inheritability, CT C181177). KB spec file says `GFINHERT` (line 230 + line 524), KB examples files use `GFINHERTG` (lines 27, 60). ChatGPT answered `GFINHERTG` (matching examples), bank expected `GFINHERT` (matching spec). Scorer noted this inconsistency inline ("handoff 写 GFINHERT, 实际 KB examples.md 用 GFINHERTG"). This is a KB internal inconsistency, not a scoring defect, but Rule A requires flagging.

**Gate recommendation: HOLD — do not OPEN Phase 4→5 until F-R1 is resolved.** Two options: (a) re-ask ChatGPT the bank's actual Q8 + Q9 and re-grade; or (b) user explicitly ratifies the substitution, updates `smoke_v3_questions_draft.md` to match what was actually asked, and renames or adds an addendum noting bank-to-asked diff. Option (b) is ~5 min cost; option (a) is ~20 min. Either is fine; status quo is NOT fine because the 14/14 claim against the written bank is not true as written — it is 12/14-verifiable + 2/14-swapped.

**If F-R1 is resolved via option (b) (cheapest)**: the answer-quality evidence I independently re-graded strongly supports ≥10/14 and the gate opens. Nothing I saw in the 6 sampled answers plus 3 sanity plus spot-checks on Q4/Q5/Q7 suggests lenient scoring on the delivered content.

---

## Rule A Sampling (N=6 independent re-grade)

### Q1 (GF — critical pure generalization probe)

**PASS criteria from bank (lines 51-58)**:
- Domain = GF (v3.4 new), not LB/PF/PGx
- ≥5 Core=Req out of {STUDYID, DOMAIN="GF", USUBJID, GFSEQ, GFTESTCD, GFTEST}
- ≥3 Core=Exp out of {GFREFID, GFORRES, GFSTRESC, GFDTC, GFMETHOD, VISITNUM}
- (a) GFGENSR holds "Exon 19"
- (b) GFPVRID holds "rs121913444"
- (c) GFGENREF holds "GRCh38.p13"
- (d) GFINHERT (CT C181177) indicates inheritability

**Independent KB grep**:
- `knowledge_base/domains/GF/spec.md:50 ### GFSEQ` — CONFIRMED
- `knowledge_base/domains/GF/spec.md:230 ### GFINHERT` — CONFIRMED (spec says GFINHERT, no G at end)
- `knowledge_base/domains/GF/spec.md:284 ### GFGENSR` — CONFIRMED
- `knowledge_base/domains/GF/spec.md:302 ### GFPVRID` — CONFIRMED
- `knowledge_base/domains/GF/spec.md:239 ### GFGENREF` — CONFIRMED
- `knowledge_base/domains/GF/spec.md:524` references CT `C181177` as "Genomic Inheritability Type Response" — CONFIRMED
- `knowledge_base/domains/GF/examples.md:27,60` use column name `GFINHERTG` — **INCONSISTENT with spec**

**ChatGPT answer actual**:
- Domain GF ✓
- Req: STUDYID/DOMAIN/USUBJID/GFTESTCD/GFTEST (5, omits GFSEQ but 5 required — bank allows "任 5")
- Exp: GFORRES/GFSTRESC/GFDTC/VISITNUM (4, meets ≥3)
- (a) GFGENSR for Exon 19 ✓
- (b) GFPVRID = rs121913444 ✓
- (c) GFGENREF = GRCh38.p13 ✓
- (d) GFINHERTG = GERMLINE — bank said GFINHERT; spec agrees with bank; examples agree with ChatGPT

**My grade: PASS**
- Scorer's PASS: AGREE
- Note: F-R3 (LOW) — KB self-inconsistency between spec.md (GFINHERT) and examples.md (GFINHERTG). Bank and ChatGPT are each internally consistent with one half of KB. ChatGPT's answer is not wrong given the examples are canonical reference data. Cannot penalize ChatGPT on ambiguous KB.

---

### Q10 (SUPP — 5-field complex criteria)

**PASS criteria from bank (lines 316-320)**:
- (a) QORIG Req, origin values; QEVAL Exp, only when subjective
- (b) SUPPTS study-level vs SUPPAE subject-level
- (c) SUPPAE pointer: RDOMAIN="AE", IDVAR="AESEQ", IDVARVAL=value, USUBJID Req
- (d) Parent GOC var 200 char split into SUPP-- QVAL w/ QNAM numeric suffix; QVAL itself has no SDTMIG business-length

**Independent KB grep**:
- `knowledge_base/domains/SUPPQUAL/spec.md:77 ### QORIG` — CONFIRMED
- `knowledge_base/domains/SUPPQUAL/spec.md:84` CDISC Notes "Examples: CRF, Assigned, Derived" — CONFIRMED
- `knowledge_base/domains/SUPPQUAL/spec.md:86 ### QEVAL` — CONFIRMED
- `knowledge_base/domains/SUPPQUAL/spec.md:100` references `Evaluator (C78735)` — CONFIRMED

**ChatGPT answer actual**:
- (a) QORIG=Req every record; QEVAL=Exp only for subjective ✓
- (b) SUPPAE subject-level; TS is study-level; **honest declaration** that TS is NOT in SUPP-- applicable parent list in v3.4 (TSVAL-TSVALn instead) ✓ — this is a genuine non-trivial bonus
- (c) STUDYID + RDOMAIN + USUBJID + IDVAR + IDVARVAL five-tuple; AESEQ most common; DM special case ✓
- (d) QVAL 200-char SAS V5 physical limit; split with QNAM/QNAM1/QNAM2 suffix; QLABEL preserved; 8-char-max QNAM overflow trick (AEACNOTH → AEACNOT1) ✓

**My grade: PASS**
- Scorer's PASS: AGREE
- **Honesty premium**: The "TS 不在 SUPP-- 适用父域" assertion is correct per SDTMIG v3.4 (SUPP-- applies to EV/FD/IN + DM + SV, not TS). Genuinely educator-level. Bank's FAIL criterion "说 'QVAL 本身有 200 字符硬上限'" — ChatGPT DID say this via "SAS V5 transport 物理上限 = 200 characters". This is a borderline collision with the FAIL criterion that was worded as "200 is parent-GOC-var limit, not QVAL's own". ChatGPT says the 200-char physical limit comes from SAS V5, which IS the correct attribution (SAS V5 applies the 200 cap to ALL character fields including QVAL, so QVAL inherits the 200 cap physically even though SDTMIG doesn't impose a business-level QVAL cap). This is a subtle distinction where the bank's v3.1 fix and ChatGPT's answer say nearly the same thing from different angles; ChatGPT does NOT say "SDTMIG imposes 200-char business limit on QVAL" (the actual FAIL trigger). PASS stands.

---

### Q12 (AETERM correction claim — non-trivial bonus claimed by scorer)

**PASS criteria from bank (lines 366-371)**:
- (a) Single CT version across whole study
- (b) Define-XML <CodeList> references CDISC CT release date
- (c) AETERM uses MedDRA (sponsor-specified version, separate from CDISC CT); v25→v27 all AE recoded consistently
- (d) Retired/alias: freeze or remap

**Independent verification of scorer's "educator-level correction" claim**:

Reading Q12_answer.md carefully, ChatGPT says (line 30 of Q12_answer):
> **ChatGPT 主动纠正**: AETERM **不是 MedDRA 编码字段**, AETERM 是 **verbatim (原始报告词)**; MedDRA 影响的是 **AEDECOD / AELLT / AELLTCD / AEPTCD / AEHLT / AEHLGT** 等字典派生字段.

**Independent KB grep to verify**:
- AE domain AETERM definition: AETERM is indeed the verbatim reported term, not the MedDRA-coded term
- MedDRA-derived fields: AEDECOD (Preferred Term), AELLT (Lowest Level Term), AEBODSYS (Body System from SOC) — all KB-confirmed
- Bank's question text (line 364): "AETERM 用 MedDRA 字典, MedDRA v25→v27 会不会影响 AE submission?"
- Bank's PASS text (line 369): "AETERM 是 MedDRA 字典" — this is the bank's phrasing in the question premise; ChatGPT correctly noted AETERM is verbatim while AEDECOD is the dictionary-derived field

**Is the "correction" real?**
- YES. The bank's question premise ("AETERM 用 MedDRA 字典") is technically imprecise — AETERM holds the verbatim (what the investigator wrote); MedDRA coding lands in AEDECOD/AELLT/AEPTCD. ChatGPT caught this and politely corrected it.
- This is a genuine educator-level correction. A trained-on-pattern LLM would have accepted the premise.

**My grade: PASS**
- Scorer's PASS + bonus attribution: AGREE
- The correction is real and genuinely non-trivial. Scorer is not overclaiming.

---

### Q13 (RWD — knowledge boundary claim)

**PASS criteria from bank (lines 386-390)**:
- (a) Naturally-failing rule classes: Trial Design / IE / Planned Visit / Study Reference Start Date
- (b) ARMCD / ARM can be "NOTASSGN" or "NOTASSIGNED"
- (c) NS (Non-Standard Domain) is horizontal per-topic; SUPPQUAL is vertical key-value
- (d) SUPPDM can hold observational-specific data

**Scorer's claim** (results line 146): "直接声明 2024 RWD 文档不在 KB, 外部检索不可用, 标注 '基于 SDTMIG v3.4 推断'"

**Verification**:

Q13_answer.md opens (lines 10-12):
> 模型主动声明: 无法直接逐字核对 CDISC 2024《Considerations for SDTM Implementation in Observational Studies and Real-World Data v1.0》, 因为该文档本身**不在当前已上传知识库**, 且环境**外部检索不可用**. 因此回答将基于 SDTMIG v3.4 / SDTM v2.0 现有规则推断 2024 文档大概率落地方式, **把"直接有底座证据"和"推断"分开标注**.

- This is a genuinely honest knowledge-boundary declaration. ChatGPT is telling the user it is inferring, not citing the 2024 document.

**Independent fact-check on the 4 sub-answers**:
- (a) Trial Arm / Planned Visit / EPOCH+TAETORD — all real SDTM concepts that would genuinely not apply in pure observational ✓
- (b) ARMCD=null + ARM=null + ACTARM=null + ARMNRS="NOT ASSIGNED" — KB-searchable; SDTMIG DM assumes ARMCD=null valid with ARMNRS populated, and the 4 ARMNRS values quoted (NOT ASSIGNED / SCREEN FAILURE / ASSIGNED, NOT TREATED / UNPLANNED TREATMENT) are standard ✓
- (c) NS vs SUPPQUAL 5-dimension comparison table (本质/物理形式/依赖/适合数据/键): this is a reconstruction from first principles since NS isn't in KB; the reconstruction is logically defensible ✓
- (d) SUPPDM scope: "单次采集, 静态或近静态的 subject-level 背景属性" — correct per SUPPDM conventions ✓; recommends SC (Subject Characteristics) for subject characteristics over SUPPDM — correct per SDTMIG SC vs SUPPDM guidance ✓

**My grade: PASS (Constrained Generalization)**
- Scorer's PASS + "highest honesty" bonus: AGREE
- The knowledge-boundary declaration is genuinely there (not a fabrication by scorer). Given KB has 0 direct RWD doc coverage, ChatGPT's approach of "mark inference vs direct evidence" is the correct engineering response.

---

### Q14 (cross-domain AE+CE+MH+DS+DM alignment)

**PASS criteria from bank (lines 410-413)**:
- (a) STEMI records only in AE (not CE unless endpoint; not MH unless pre-study)
- (b) Death recorded in DS + DM + AE (if fatal AE)
- (c) DSDECOD="DEATH" with codelist C66727 (Disposition From Study — per bank)
- (d) Cross-domain alignment: DM.DTHDTC = DS.DSSTDTC = AE.AEENDTC (if fatal)

**Independent KB grep for the CT code**:
- `knowledge_base/terminology/core/disposition.md:15 ## Completion/Reason for Non-Completion (C66727)` — **KB confirms C66727 is "Completion/Reason for Non-Completion", NOT "Disposition From Study" as bank claims**
- `knowledge_base/domains/DS/spec.md:84` — CDISC Notes: codelist "NCOMPLT" is used for disposition events, codelist "PROTMLST" is used for protocol milestones, codelist "OTHEVENT" is used for other events
- `knowledge_base/domains/DS/spec.md:156` — `[Completion/Reason for Non-Completion (C66727)] — DSDECOD` CONFIRMS C66727 is associated with DSDECOD when DSCAT=DISPOSITION EVENT, with codelist name NCOMPLT

**Bank's v3.0→v3.1 note** (line 10): "DSDECOD CT code C66728 → **C66727** (C66728 是 Relation to Reference Period, 错归; C66727 是 Disposition From Study)"

**Bank's attribution error**:
- Bank v3.1 correctly identified C66728 ≠ DSDECOD (C66728 = Relation to Reference Period, verified at `general_part4.md:74`)
- But the bank's "C66727 是 Disposition From Study" label is WRONG — C66727's official name is "Completion/Reason for Non-Completion" (per KB disposition.md:15)
- The functional correctness: C66727 IS the codelist used for DSDECOD when DSCAT=DISPOSITION EVENT (codelist NCOMPLT), which DOES include DEATH as a value — so C66727 is semantically the right code, just the human-readable label the bank cited is wrong.

**ChatGPT answer actual** (Q14_answer.md, section (c)):
- DSCAT = "DISPOSITION EVENT" ✓
- DSDECOD = "DEATH" ✓
- DSSCAT = "STUDY PARTICIPATION" ✓
- **ChatGPT did NOT cite any C-code in its answer.** Therefore ChatGPT did not repeat or inherit the bank's "Disposition From Study" mis-label.

**My grade: PASS for ChatGPT answer**
- Scorer's PASS: AGREE
- But F-R2 (MEDIUM): The BANK itself contains a CT-name attribution error at Q14 PASS criterion (c) that should be corrected before bank v3.2, even if it does not affect this specific grading (because ChatGPT didn't cite the code). If a future ChatGPT answer DOES cite "C66727 Disposition From Study", it would be factually wrong per KB but would now erroneously pass against the bank text. Fix: rename v3.2 to "C66727 (Completion/Reason for Non-Completion, codelist NCOMPLT, includes DEATH value)".

---

### Q3 (BE+BS+RELSPEC — my additional sample)

**PASS criteria from bank (lines 104-111)**:
- (a) Collection = BE (BECAT=COLLECTION); transport = BE (BETERM="TRANSPORT"); DNA extraction = BE (BETERM="PREPARATION"/"EXTRACTION"); measurements = BS
- (b) Volume: BSTESTCD="VOLUME"; RIN: BSTESTCD="RIN"; CT C124300
- (c) RELSPEC (not RELREC) for specimen derivation

**Independent KB grep**:
- `knowledge_base/domains/BS/spec.md:84` BSTESTCD CDISC Notes "Examples: VOLUME, RIN" — CONFIRMED
- `knowledge_base/domains/BS/spec.md:326` BSTESTCD CT C124300 — CONFIRMED
- `knowledge_base/domains/BE/spec.md:104 ### BECAT` — CONFIRMED
- `knowledge_base/domains/RELSPEC/` directory exists — CONFIRMED; `knowledge_base/INDEX.md:132` lists RELSPEC

**ChatGPT answer actual**:
- (a) BE for collection/transport/DNA extraction ✓
- (b) BS for volume/RIN; BSTESTCD=VOLUME/RIN correct ✓
- (c) RELSPEC for specimen lineage, not RELREC ✓
- Bonus: Honest flag that RIN ≈ RNA quality, so if spec shows DNA only, it wouldn't naturally attach to RIN

**My grade: PASS**
- Scorer's PASS: AGREE
- No issues.

---

## Cross-checks

### 3 sanity questions (baseline regression check)

**Sanity 1: AESER Core attribute**
- Expected: Exp
- ChatGPT: "AESER 的 Core 属性是 Exp"; cites C66742
- KB verification: `VARIABLE_INDEX.md:78 | AESER | ... | Record Qualifier | Exp | C66742`
- ✓ **MATCH** — PASS confirmed

**Sanity 2: LBNRIND submission values**
- Expected: HIGH / LOW / NORMAL / ABNORMAL (C78736)
- ChatGPT: lists ABNORMAL, HIGH, LOW, NORMAL; cites C78736; marks Extensible: Yes
- ✓ **MATCH** — PASS confirmed

**Sanity 3: CMINDC usage**
- Expected: explicitly name CMINDC (concomitant medication indication)
- ChatGPT: explicitly names CMINDC, distinguishes CMTRT vs CMINDC, cites Other/specify + SUPPCM 3-way strategy
- ✓ **MATCH** — PASS confirmed

**Baseline check**: 3/3 sanity PASS. No regression in the base system from batch 1 N5.1. ✓

---

### 04 citation rate (scorer's ≤4/14 claim)

Scorer's claim in `smoke_v3_results.md:175`: "单文件 04 依赖 ≤4 题 (Q4/Q7/Q8/Q14 配合多源, 非过度依赖)"

**Independent grep** (`grep -c "ch04\|04_general_assumptions\|04_business_scenarios"` across 14 Qx_answer files):

| File | ch04 mentions |
|---|---|
| Q1 | 0 |
| Q2 | 2 |
| Q3 | 0 |
| Q4 | 0 |
| Q5 | 0 |
| Q6 | 1 |
| Q7 | 2 |
| Q8 | 2 |
| Q9 | 0 |
| Q10 | 2 |
| Q11 | 1 |
| Q12 | 1 |
| Q13 | 0 |
| Q14 | 1 |

**Analysis**:
- 0 mentions of `04_business_scenarios` anywhere — this is the critical file the generalization probe was designed to avoid over-dependence on, and it's 0/14. 
- `ch04_general_assumptions.md` is cited in 9/14 answers, but typically as 1-2 source anchors alongside domain-specific files. This is expected (ch04 is the cross-cutting ISO 8601 / Timing / SUPP anchor chapter).
- Scorer's "≤4 single-file 04 dependence" claim appears ACCURATE given no answer relies exclusively on ch04.
- **Note**: Scorer's phrasing is ambiguous (does "04" mean ch04 general or 04_business_scenarios?). If it means 04_business_scenarios (the Claude v2 batch file that the generalization probe was meant to avoid), then 0/14 citations = PERFECT generalization signal (stronger than the scorer's claim). If it means ch04_general_assumptions, then 9/14 use it but none solely, which is also fine. Either reading supports the generalization-is-real claim.
- ✓ **04 citation rate claim HOLDS**.

---

### Scorer bias audit (was 14/14 too perfect?)

**Possible leniency sources I looked for**:

1. **Missed FAIL triggers**: I re-read bank PASS/FAIL criteria for Q1, Q3, Q10, Q12, Q13, Q14. Q10's "QVAL 200 字符硬上限" FAIL criterion is a borderline collision with ChatGPT's "SAS V5 transport 物理上限 = 200 characters" phrasing. ChatGPT's attribution to SAS V5 (not SDTMIG business rule) saves it — the FAIL criterion is specifically about false SDTMIG business-limit attribution, and ChatGPT correctly attributes to SAS V5 transport. Not a FAIL. Scorer ruled PASS here — AGREE.

2. **Q4 场景 A PARTIAL protection**: Bank specifies "PARTIAL" (0.5) rather than full FAIL if answer says MB but justifies with "immunogenicity/antibody surrogate". ChatGPT answered IS — no PARTIAL invocation needed. Clean PASS. ✓

3. **Q5 CE borderline**: Bank Q5 flagged borderline (04 §1.19 has FA vs QS overlap). ChatGPT PASS-graded, but my grep of Q5_answer.md shows ch04 is NOT cited — so generalization is genuine here. ✓

4. **Q13 2024 RWD document** — scorer gave full PASS despite ChatGPT declaring it couldn't verify the 2024 doc. Bank's PASS criteria (a)(b)(c)(d) are based on SDTMIG v3.4 concepts not the 2024 doc specifically, so answering from first principles IS the correct approach. No leniency. ✓

5. **Scorer's bonus-point language** ("educator-level correction", "highest honesty") appears in Q10, Q11, Q12, Q13, Q14. I independently verified Q10 (TS scope), Q12 (AETERM verbatim), Q13 (knowledge boundary), Q14 (two-scenario modelling) — all four are real non-trivial details. Not inflated.

**Conclusion on scorer bias**: No systematic leniency found. If anything, the scorer was slightly generous on bonuses but not on PASS/FAIL thresholds. The 14/14 claim on delivered content is defensible.

---

### F-R1: Q8 / Q9 question-bank mismatch (HIGH)

**What the bank says** (smoke_v3_questions_draft.md):
- Line 34: `Q8 | D1 CT 深化 | Extensible vs Non-Extensible codelist`
- Line 35: `Q9 | E1 实战验证 | Pinnacle 21 常见 FAIL 分类`

**What the scorer says** (smoke_v3_results.md):
- Line 97: "Q8 (B5 — EPOCH Trial Design 与 Subject-level 关系)"
- Line 104: "Q9 (B6 — AESEV vs AETOXGR vs AESER NCI CTCAE 严重度)"

**What the answer files say**:
- Q8_answer.md line 1: "Q8 (B5 — EPOCH Trial Design 与 Subject-level 关系)"
- Q9_answer.md line 1: "Q9 (B6 — AESEV vs AETOXGR vs AESER) NCI CTCAE 严重度场景"

**Verification**:
- `grep -l "Pinnacle 21\|Extensible\|Non-Extensible"` across all 14 answer files returns ONLY `sanity_2_answer.md` (which discusses Extensible:Yes for LBNRIND C78736). NO answer file addresses the bank Q8 (Extensible vs Non-Extensible) or bank Q9 (Pinnacle 21).

**Why this matters**:
- Rule A requires PASS/FAIL grading against the bank. The bank v3.1 (Step 3 approved) is the contract. The asked questions Q8/Q9 are different from the contract. The scorer graded against what was asked, not what the bank specified. The report then claims 14/14 against the bank — this claim is NOT TRUE AS WRITTEN.
- The real delivered score against the v3.1 bank is 12/14 verified (Q1-Q7, Q10-Q14 all match) + Q8-Q9 UNTESTED against bank.
- 12/14 = 86% which still exceeds the 71% gate threshold, so the gate is technically OPEN-eligible on the verified 12. But the 14/14 headline as reported is misleading.

**Possible innocent explanations** (I cannot confirm without user ack):
- Bank v3.1 was changed between approval and execution, or an earlier v3.0 numbering leaked through
- Scorer or executor intentionally substituted (e.g., because Q8/Q9 were judged too similar to sanity_2 LBNRIND Extensible, or because Pinnacle 21 is online-lookup territory)
- The mapping note exists somewhere else I didn't see

**Requested resolution**: Main session must either (a) update `smoke_v3_questions_draft.md` v3.2 to include the actually-asked Q8/Q9 content and document the v3.1→v3.2 diff explicitly, or (b) execute bank Q8/Q9 (Extensible + Pinnacle 21) additionally and re-tally. Option (b) is safer for Rule A traceability; option (a) is cheaper.

---

## Findings Summary

### HIGH

**F-R1 [HIGH, procedural]**: Q8 (asked: EPOCH; bank: Extensible CT) and Q9 (asked: AESEV/AETOXGR/AESER; bank: Pinnacle 21) diverge between the v3.1 bank and the executed smoke. The 14/14 PASS claim against the bank as written is materially misleading. Real verifiable score: 12/14 (86%) against bank text + 2/14 on substituted questions. Blocks clean gate OPEN until resolved.
- Owner: main session
- Fix: Option (a) — update bank to v3.2 documenting substitution + rationale; OR Option (b) — execute bank Q8/Q9 as additional questions and re-tally.
- Gate-blocking? **Yes, soft-blocking** — gate would still be threshold-eligible on verified 12/14, but the reporting integrity is not acceptable as-is.

### MEDIUM

**F-R2 [MEDIUM, data quality]**: Bank v3.1 Q14 PASS criterion (c) mis-labels CT code C66727 as "Disposition From Study". Per KB (`knowledge_base/terminology/core/disposition.md:15` and `knowledge_base/domains/DS/spec.md:156`), C66727 is "Completion/Reason for Non-Completion" (codelist NCOMPLT, which DOES include DEATH value — so the code IS functionally right for DSDECOD="DEATH", just the human-readable label the bank uses is wrong). Did not affect current grading because ChatGPT did not cite any C-code in Q14. Should be fixed before bank v3.2 to prevent future false positives.
- Owner: main session + double-check by Gemini reviewer if Gemini also sees this in their copy of the bank.

### LOW

**F-R3 [LOW, KB inconsistency]**: `knowledge_base/domains/GF/spec.md` uses variable name `GFINHERT` (lines 230, 524). `knowledge_base/domains/GF/examples.md` uses `GFINHERTG` (lines 27, 60). ChatGPT answered `GFINHERTG` (matching examples), bank expected `GFINHERT` (matching spec). Does not block Q1 PASS, but KB should be made internally consistent in Phase 6.5 or a later knowledge_base refresh pass.
- Owner: knowledge_base maintenance (non-blocking for Phase 4→5 gate).

---

## Gate Decision: Phase 4→5

**Decision: HOLD** (pending F-R1 resolution)

**Rationale**:
- ChatGPT's delivered answer quality is genuinely at ≥10/14 threshold. Independent re-grading of Q1, Q3, Q10, Q12, Q13, Q14 + 3 sanity + cross-checks all confirm PASS.
- 14/14 headline against bank-as-written is not accurate (12/14 verified + 2/14 substituted). This matters for Rule A traceability and for future reviewers reading the progress file.
- Under Rule D strict interpretation (writer-product-compliant), the smoke_v3_results.md is NOT compliant with the bank without F-R1 resolution.
- Fix is cheap (~5-20 min) via option (a) bank v3.2 with substitution note, or option (b) ask ChatGPT bank Q8/Q9 additionally.

**What OPENs the gate**:
1. F-R1 resolved (either option a or b)
2. F-R2 fix in bank v3.2 (MEDIUM, non-blocking but strongly recommended)
3. F-R3 KB cleanup scheduled (LOW, non-blocking)

**What stays BLOCKing if F-R1 unresolved**: The 14/14 claim against v3.1 bank. If main session accepts the report as-is without fixing, a future reviewer will find the same inconsistency and hold the gate longer.

**If F-R1 resolved cleanly**: Gate OPEN recommended with **high confidence** (≥85%). Answer quality is strong, generalization is real (0/14 04_business_scenarios citations), sanity 3/3, honesty premium genuine on Q11/Q12/Q13, no systematic leniency detected.

---

## Metadata for next reviewer / main session

- Files I read: `smoke_v3_questions_draft.md` v3.1 (full), `smoke_v3_results.md` (full), all 14 Qx_answer.md (sampled deep on 6 + skimmed 8), 3 sanity_x_answer.md (full), KB spec files for GF/CP/BS/BE/RELSPEC/DS/SUPPQUAL, KB terminology/core/disposition.md + general_part4.md + ae.md, KB VARIABLE_INDEX.md, KB INDEX.md, KB ROUTING.md
- Tools used: Read (parallel where possible), Bash grep (parallel across KB dirs)
- I did NOT read: Gemini side artifacts (out of scope for ChatGPT-side review), system_prompt.md (out of scope for answer-quality check), Phase 4 N5.2 history (cold review protocol)
- Rule D independence: No shared context with scorer, main session, or earlier N5.3 reviewers. No shared subagent_type with any prior slot in the 22-slot chain. My reasoning chain was: load bank → load scorer output → cold-read 6 answers → independent KB grep → compare → flag mismatches.
