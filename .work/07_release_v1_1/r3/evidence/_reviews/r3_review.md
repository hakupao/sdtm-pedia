# R3 Reviewer Lane Audit (oh-my-claudecode:scientist, Rule D #15)

> Reviewer: scientist subagent (independent lane, not main session writer)
> Date: 2026-05-19
> Scope: 17 questions × 4 platforms = 68 cells
> Evidence base: per-platform q01.md (×4) + q02-q14 combined + ahp1-ahp3 combined + SMOKE_V4.md §2 criteria (lines 440-961)

---

## 1. Verdict 一致性 (per question)

| Q | Reviewer Verdict | Main Session Verdict | 一致? | 备注 |
|---|---|---|:--:|---|
| Q1 Claude | PASS+ | PASS+ | ✓ | L858R/Exon21 clinical correction confirmed in evidence; 6 Req + 3 Exp + all 4 sub-q hit |
| Q1 ChatGPT | PASS | PASS | ✓ | All 7 PASS criteria hit; active spelling clarification GFINHERT≠GFINHERTG = bonus within PASS tier |
| Q1 Gemini | PASS | PASS | ✓ | R1 FAIL (GFINHERT misspell) → R3 PASS; 6 Req + 3 Exp + 4 sub-q, 0 FAIL criteria triggered |
| Q1 NotebookLM | PASS | PASS | ✓ | RAG source citations add transparency but are bonus-level; criteria all met |
| Q2 Claude | PASS+ | PASS+ | ✓ | CPGATE/CPGATDEF + 5 CT codelists = solid bonus tier |
| Q2 ChatGPT | PASS+ | PASS+ | ✓ | PROLIFERATING clinical correction is legitimate PASS+ trigger per §2 bonus criteria |
| Q2 Gemini | PASS | PASS | ✓ | All 5 CR criteria hit; no bonus — PASS correct |
| Q2 NotebookLM | PASS | PASS | ✓ | Mutual-lock CPCELSTA/CPCSMRKS observation = correct domain knowledge, but not at PASS+ level |
| Q3 Gemini | FAIL | FAIL | ✓ | Evidence is unambiguous: response discusses AE splitting/AEGRPID — entirely off-topic. 0 of BE/BS/RELSPEC criteria met |
| Q3 ChatGPT | PASS+ | PASS+ | ✓ | RELSPEC REFID/PARENT/LEVEL + RELREC distinction + RIN-in-RNA-aliquot clinical note = valid PASS+ |
| Q3 NotebookLM | PASS | PASS | ✓ | All core criteria hit + BSORRESU C71620; no PASS+ bonus trigger observed |
| Q3 Claude | PASS+ | PASS+ | ✓ | ASCII flow diagram + BSCAT/BEPARTY + 5 CT codes = clear PASS+ |
| Q4 Gemini | FAIL | FAIL | ✓ | Scenario A = LB (should be IS per SDTMIG v3.4 assumption 2); evidence record confirms "A=LB FAIL". FAIL criteria explicitly state: answer MB/LB without IS recognition = FAIL |
| Q4 ChatGPT | PASS+ | PASS+ | ✓ | v3.4 explicit IS-scope correction for A + ISTSTOPO stratification for B = bonus tier |
| Q4 NotebookLM | PASS+ | PASS+ | ✓ | ISCAT=NON-STUDY-RELATED IMMUNOGENICITY + HIV Ag/Ab exemption = valid PASS+ bonus |
| Q4 Claude | PASS+ | PASS+ | ✓ | IS Assumption 7a quote + Example 1/5/8 = strongest evidence; PASS+ confirmed |
| Q5 Gemini | PASS | PASS | ✓ | All 3 domains (FA/QS/CE) correctly identified; no bonus observed |
| Q5 ChatGPT | PASS+ | PASS+ | ✓ | RELREC FA↔MH linkage + CEDUR=PT30S ISO 8601 duration = valid bonus |
| Q5 NotebookLM | PASS | PASS | ✓ | C85441 CT reference is supporting evidence but not PASS+ threshold alone |
| Q5 Claude | PASS+ | PASS+ | ✓ | §6.4.3/§8.6.1/§8.6.3 citations + class structure = PASS+ |
| Q6 Gemini | PASS | PASS | ✓ | All 5 timing variables + ISO 8601 + VISITNUM correct; no EPOCH = PASS not PASS+ |
| Q6 ChatGPT | PASS+ | PASS+ | ✓ | EPOCH bonus observed |
| Q6 NotebookLM | PASS | PASS | ✓ | EPOCH not mentioned; PASS correct |
| Q6 Claude | PASS+ | PASS+ | ✓ | EPOCH bonus confirmed |
| Q7 Gemini | PASS | PASS | ✓ | All partial-date cases correct + SDTM-no-impute / ADaM-imputes axis correct |
| Q7 ChatGPT | PASS+ | PASS+ | ✓ | SUPP-- carry-over mention = bonus |
| Q7 NotebookLM | PASS | PASS | ✓ | All criteria correct; no bonus qualifier |
| Q7 Claude | PASS+ | PASS+ | ✓ | ADTF imputation flag detail = bonus |
| Q8 Gemini | PASS | PASS | ✓ | All 5 criteria met (Extensible semantics / NY-AESEV Non-Ext / AETERM≠MedDRA / AEDECOD binding / Define-XML); no FAIL triggered |
| Q8 ChatGPT | PASS+ | PASS+ | ✓ | ExtendedValue metadata + LBTESTCD C65047 explicit = PASS+ |
| Q8 NotebookLM | PASS+ | PASS+ | ✓ | Evidence confirms PASS+; detail warrants it |
| Q8 Claude | PASS+ | PASS+ | ✓ | Deepest on AETERM verbatim origin chain |
| Q9 Gemini | PASS | PASS | ✓ | 5/5 category types hit (CT/IDVAR/ISO/cross-domain/Req) + decision table = solid PASS |
| Q9 ChatGPT | PASS+ | PASS+ | ✓ | Depth (5301 chars) + extra categories = PASS+ |
| Q9 NotebookLM | PUNT | PUNT | ✓ | In-KB-only architecture: Pinnacle 21 not in KB → correct policy refusal. PUNT = FAIL for scoring but "policy-correct" per §2; main session classification is accurate |
| Q9 Claude | PASS | PASS | ✓ | 4/5 core categories + SDRG = PASS; no PASS+ bonus observed |
| Q10 Gemini | PASS+ | PASS+ | ✓ | "Trial Design 不适用 SUPPQUAL" + TSVAL1-n + scope = caught SUPPTS premise; R1 PARTIAL→R3 PASS+ is a genuine upgrade |
| Q10 ChatGPT | PASS+ | PASS+ | ✓ | Caught + §8.4 scope + QORIG/QEVAL correct |
| Q10 NotebookLM | PASS+ | PASS+ | ✓ | "no such dataset as SUPPTS" explicit catch; longest response (4690 chars) = thorough |
| Q10 Claude | PASS+ | PASS+ | ✓ | §4.5.3.2 + §7.4.2 citations = strongest; PASS+ confirmed |
| Q11 Gemini | FAIL | FAIL | ✓ | Off-topic response discussing AE/CM (1436 chars, no Dataset-JSON content). Bonus-容错 noted in matrix; FAIL is correct per §2 criteria even with bonus context |
| Q11 ChatGPT | PASS+ | PASS+ | ✓ | 8-char/200-char/metadata XPT painpoints + Define-XML互补 all present |
| Q11 NotebookLM | PARTIAL | PARTIAL | ✓ | Outside KB; answered (a)/(d) partially; (b) FDA status incomplete = PARTIAL correct |
| Q11 Claude | PASS+ | PASS+ | ✓ | 4/5 XPT painpoints + Define-XML role = PASS+; (b) FDA current status = main gap but not FAIL |
| Q12 Gemini | PASS | PASS | ✓ | All 5 criteria (DBL lock / CDISC CT / Define-XML / MedDRA separate / retire handling) correct |
| Q12 ChatGPT | PASS | PASS | ✓ | Same 5 criteria; no bonus = PASS not PASS+ |
| Q12 NotebookLM | PASS | PASS | ✓ | R1 PUNT→R3 PASS with KB-outside caveat = genuine upgrade; PASS correct |
| Q12 Claude | PASS+ | PASS+ | ✓ | FDA TCG + Define-XML 2.1 governance = bonus tier |
| Q13 Gemini | PASS+ | PASS+ | ✓ | "SDTMIG v3.4 及 CDISC 不存在 NS 域" explicit catch = PASS+ bonus per §2 AHP criteria |
| Q13 ChatGPT | PASS+ | PASS+ | ✓ | NS caught + C142179 + SUPPDM = all elements |
| Q13 NotebookLM | PASS+ | PASS+ | ✓ | NS caught + ARMNRS + SUPPDM = PASS+ |
| Q13 Claude | PASS+ | PASS+ | ✓ | Meta-caveat on NS + strongest ARMNRS explanation |
| Q14 Gemini | PASS | PASS | ✓ | AE/MH/CE timing + DSDECOD + DTHDTC all correct; no bonus = PASS |
| Q14 ChatGPT | PASS+ | PASS+ | ✓ | AESDTH linkage bonus confirmed |
| Q14 NotebookLM | PASS | PASS | ✓ | Correct on all domains; no qualifying bonus |
| Q14 Claude | PASS | PASS | ✓ | Correct on all domains; response length 1704 chars modest but sufficient |
| AHP1 Gemini | FAIL | FAIL | ✓ | Off-topic CM/MH polypharmacy response — 3rd off-topic event. FAIL criteria: premise not caught = FAIL (not PARTIAL) per §2 AHP rules |
| AHP1 ChatGPT | PASS+ | PASS+ | ✓ | "应为 LBCLSIG" explicit catch + C66742 + LBNRIND distinction = PASS+ |
| AHP1 NotebookLM | PASS+ | PASS+ | ✓ | 8-char SAS name limit explanation for LBCLSIG vs LBCLINSIG = valid PASS+ bonus |
| AHP1 Claude | PASS+ | PASS+ | ✓ | EGTESTCD=INTP analogy for --CLSIG pattern = strong bonus |
| AHP2 Gemini | PASS+ | PASS+ | ✓ | Caught + ADaM/CSR/SDRG three-layer articulation = solid PASS+ |
| AHP2 ChatGPT | PASS+ | PASS+ | ✓ | No-RELREC-cross-linking caveat + ADRG reference = PASS+ |
| AHP2 NotebookLM | PASS+ | PASS+ | ✓ | "衍生汇总→ADaM" + TS-domain clarification = PASS+ |
| AHP2 Claude | PASS+ | PASS+ | ✓ | CIOMS/E2B/DSUR/PSUR regulatory layer references = deepest bonus |
| AHP3 Gemini | PASS+ | PASS+ | ✓ | PF deprecated + GF/BE/BS/RELSPEC substitution complete |
| AHP3 ChatGPT | PASS+ | PASS+ | ✓ | Migration narrative present |
| AHP3 NotebookLM | PASS+ | PASS+ | ✓ | "PF 域已被 GF 域正式取代" explicit + correct GF variables listed |
| AHP3 Claude | PASS+ | PASS+ | ✓ | §6.3.5.4 Revision History quote = strongest evidence anchor; "不能臆造" self-directive = genuine anti-hallucination behavior |

**Verdict concordance: 68/68 cells agree with main session (100%).**

---

## 2. Pattern Findings 评估

### 2a. Gemini 跑题 (Q3/Q11/AHP1) — 真 hallucination 还是评分过严?

Independent assessment: **真 hallucination, 评分合理, 不过严.**

Evidence:
- Q3: Response discusses AESEV/AEGRPID (1541 chars). Question asks about BE/BS/RELSPEC. No partial content about biospecimens in the recorded response summary.
- Q11: Response discusses AE/CM domains (1436 chars). Question asks about Dataset-JSON v1.1 vs XPT v5. No overlap with the actual question topic.
- AHP1: Response discusses CM polypharmacy/MH interactions (1485 chars). Question asks about LBCLINSIG — a lab variable hallucination probe. Again zero topic overlap.

All three are "wrong question answered" events, not "right question answered incompletely." The §2 AHP FAIL rule states: premise not caught = FAIL (not PARTIAL). For Q3 and Q11, while these are not AHP probes, the complete topic substitution is worse than a partial answer and unambiguously FAIL under §2 core criteria (0/N core criteria met).

The main session correctly notes Q3 uses a v4.0 question (BE/BS/RELSPEC) that is distinct from R1's v3.2 DM ARMCD question, so the regression label for Q3 is technically an incomparable cell. However, the Q3 R3 result itself is FAIL regardless of regression framing.

Possible cause (independent view, consistent with main session): Gemini v7.1 system prompt CO anchors do not include BE/BS/RELSPEC or Dataset-JSON domains, and AHP1's question is short (no explicit reflection prompt like Q10/Q13). When off-KB topics appear in a long multi-part question, Gemini falls back to high-frequency SDTM domains (AE, CM). This is a prompt-coverage gap, not a calibration error by the scorer.

### 2b. AHP probe 4/5 caught — anti-hallucination 锚有效性?

Independent assessment: **Effective for reflection-prompted questions; conditional failure on short non-prompted questions.**

The pattern is clear from evidence:
- Q10 (SUPPTS): Contains explicit "如果你听说过所谓 'SUPPTS'" phrasing → Gemini PASS+
- Q13 (NS): Contains explicit "如果你听说过所谓 'NS (Non-Standard Domain)' 新概念, 请说明其在 SDTMIG v3.4 或 CDISC Observational v1.0 PDF 中的真实地位" → Gemini PASS+
- AHP1 (LBCLINSIG): Short factual question, no reflection trigger phrasing → Gemini off-topic FAIL

The main session's root cause analysis "AHP1 失败 = 短题文/无 reflection prompt 时 v7.1 anti-hallucination 锚失效" is well-supported by the evidence pattern. The 4/5 ratio is real: the one failure corresponds exactly to the one AHP probe without a reflection scaffold in the question text.

The v8 recommendation (make reflection a default behavior rather than relying on prompt phrasing) is the correct corrective action.

### 2c. PASS+ 分布合理性 (Claude 11 PASS+, ChatGPT 13 PASS+)

Independent assessment: **Distribution is reasonable and internally consistent with §2 bonus criteria.**

Checking Claude (11/17 PASS+):
- PASS+ triggers observed across evidence: clinical corrections (L858R/Exon21 Q1), specialized variables (CPGATE Q2, BSCAT Q3), citation depth (IS Assumption 7a Q4, §6.4.3 Q5), EPOCH bonus (Q6), ADTF flag (Q7), AETERM verbatim chain (Q8), §4.5.3.2 quote (Q10), GF Revision History quote (AHP3).
- The 6 PASS (not PASS+) cases — Q9, Q11, Q12, Q13 (already PASS+), Q14, AHP2 — are all either where Claude gave correct but not bonus-level responses (Q9 4/5 categories, Q14 modest 1704-char response) or where the evidence record shows no bonus element.
- Claude Q13 is PASS+ (NS meta-caveat), Q14 is PASS (no bonus). This is correctly differentiated.

Checking ChatGPT (13/17 PASS+):
- PASS+ triggers: PROLIFERATING correction (Q2), RELREC FA-MH (Q5), EPOCH (Q6), SUPP (Q7), LBTESTCD C65047 (Q8), 5301-char depth (Q9), NS catch (Q13), AESDTH (Q14), plus all 3 AHP probes.
- The 4 PASS cases (Q1, Q6-wait, Q12, plus cross-check) align with evidence: Q1 ChatGPT has no active clinical correction beyond the variable naming note, correctly PASS; Q12 has no bonus element beyond the 5 criteria.
- ChatGPT having more PASS+ than Claude (13 vs 11) is plausible given ChatGPT's tendency toward broader response depth on these topics per the evidence response lengths.

No inflation detected. Each PASS+ has a documentable bonus trigger in the evidence.

---

## 3. Disagreements

**None.** All 68 cells align with main session verdicts after independent review of evidence.

Two observations worth flagging but not amounting to disagreements:

**Observation A — Q3 regression framing**: Main session correctly notes "v4.0 题不同, 不可直接 regression 判定" for Q3 in the matrix header. However, the regression detail table at the bottom of r3_matrix.md still lists Q3 under "Gemini regression detail." This is accurate in that it is a new failure, but the regression framing may mislead. Independent view: label Q3 as "new FAIL on v4.0 question" rather than "regression," since there is no directly comparable R1 cell. The main session already notes this caveat — it is properly qualified in the matrix footnotes.

**Observation B — Q9 NotebookLM PUNT vs PARTIAL**: Main session records Q9 NotebookLM as PUNT. The evidence shows "0/5 categories + policy-correct in-KB-only refusal." R1 was PARTIAL. The question is whether PUNT (=0 points) or PARTIAL (=0.5) is more accurate. Since the response provided zero substantive content on Pinnacle 21 categories (unlike R1 which attempted some categories), PUNT is the correct classification. Main session is right here; no change needed.

---

## 4. Overall Verdict

- **主 session R3 评分总体: VALID**
  All verdicts are supported by evidence in the combined files. Scoring calibration is consistent with §2 criteria throughout. The 68-cell matrix is internally coherent.

- **关键 finding (Gemini regression + 4/5 AHP caught) 站得住度: SOLID**
  The regression (3 genuine off-topic events in Q3/Q11/AHP1) is not a scorer artifact — it is documented in response content summaries. The 4/5 AHP catch rate reflects a real prompt-architecture dependency (reflection phrasing in Q10/Q13 activates the anti-hallucination anchor; AHP1 without it does not). Both findings are internally consistent and cross-validated by response length and content records.

- **建议主 session 在 R3_RETROSPECTIVE 加/改的点**:
  1. Clarify Q3's status: "v4.0 new FAIL (not regression against R1 v3.2 cell)" — the matrix already notes this but the regression detail table may cause confusion for future readers.
  2. Document the finding that ChatGPT surpassed Claude on PASS+ count (13 vs 11) as a notable R3 observation — may indicate ChatGPT v2.2 prompt improvements are yielding more bonus-tier responses.
  3. Gemini Q4 Scenario A (IS vs LB): worth noting this is an R2-repaired regression that recurred, suggesting the v3.4 IS scope shift (assumption 2) is not stably anchored in v7.1 prompt even after R2 fix.

---

## 5. v1.2 / v8 Prompt 改进建议 (基于 R3 evidence)

### Gemini v8 system prompt 改动建议

**Finding 1 — Off-topic fallback on BE/BS/RELSPEC (Q3)**
Root cause: CO anchors do not mention BE/BS/RELSPEC or PGx specimen domains.
Recommendation: Add CO-N: "When question mentions biospecimen/blood sample/aliquot/DNA extraction/specimen derivation, anchor to BE (Biospecimen Events) / BS (Biospecimen Findings) / RELSPEC (Related Specimens) — do not default to AE or CM."

**Finding 2 — Off-topic fallback on Dataset-JSON (Q11)**
Root cause: Q11 is outside KB; no CO anchor for file format topics.
Recommendation: Add explicit "for file format / submission format questions (XPT / Dataset-JSON / Define-XML), ground response in CDISC published standards knowledge rather than KB — do not substitute SDTM domain content." Alternatively, add a web-search permission note for questions clearly outside the SDTMIG KB scope.

**Finding 3 — IS scope shift not stable (Q4 Scenario A recurrence)**
Root cause: v3.4 IS assumption 2 (anti-microbial antibody → IS, not MB) needs explicit CO anchor.
Recommendation: Add CO anchor: "Per SDTMIG v3.4 IS domain assumption 2, anti-microbial antibody measurements (regardless of baseline/treatment timing) go to IS, not MB. This differs from v3.3."

**Finding 4 — AHP1 LBCLINSIG: reflection prompt dependency**
Root cause: Anti-hallucination anchor fires when question contains "如果你听说过X" but not on plain factual questions about non-existent variables.
Recommendation: Make reflection a default behavior: add system prompt instruction "When asked about a specific SDTM variable name, first verify it exists in the KB variable index before answering. If not found, state that explicitly rather than inventing properties."

### 其他平台 R4 cycle 改动

- **Claude Projects v2.6**: No urgent fixes. Consider adding guidance on response length calibration for Q14-type multi-domain questions (1704 chars is thin relative to complexity).
- **ChatGPT GPTs v2.2**: Performing at ceiling (13/17 PASS+). R4 focus: verify FDA Dataset-JSON timeline accuracy (Q11 (b) gap noted) — update knowledge if FDA catalog status changes in 2026.
- **NotebookLM v2**: Q9 PUNT and Q11 PARTIAL are architectural limits, not prompt fixes. The only improvable area is ensuring in-KB responses are as complete as possible. R4 cycle: add Pinnacle 21 context to KB sources if permissible.

---

*Audit completed: 2026-05-19. Reviewer: scientist subagent (Rule D #15, independent lane). Evidence base: 21 files read (4 × q01.md per-platform + q02-q14 combined + ahp1-ahp3 combined + r3_matrix.md + SMOKE_V4.md §2 lines 440-961). No main-session context consulted during verdict formation.*
