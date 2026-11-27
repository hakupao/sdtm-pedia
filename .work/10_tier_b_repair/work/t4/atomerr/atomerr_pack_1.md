# T4 加查包 1 — ATOM_ERR (S1-R1) (21 条, 全检; 编号 E1-E21)

> 由 `scripts/t4/t4_atomerr_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 E).

### E1. `ig34_p0009_a024` — ae:S1R1_ATOM_ERR

- PDF 页 9 · 原子类型 LIST_ITEM · 所在节 `§1.4.1 [How to Read a Domain Specification]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-ch01 review: 原子缺逗号; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ch01_review.md:22`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Controlled Terms, Codelist or Format
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0009.txt` 第 43-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 42|     •    Type: One of the 2 SAS datatypes, "Num" or "Char". These values are taken directly from the SDTM.
 43|     •    Controlled Terms, Codelist, or Format
 44|          o   Controlled Terms
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:81-81` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  81| - Controlled Terms, Codelist, or Format
~~~~

### E2. `ig34_p0018_a046` — ae:S1R1_ATOM_ERR

- PDF 页 18 · 原子类型 TABLE_ROW · 所在节 `§3.2.1 Dataset-level Metadata`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-ch03 writer: 原子漏 'specimen'; KB 正确; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ch03_audit.md:33`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
MB | Microbiology Specimen | Findings | One record per microbiology finding per time point per visit per subject | Tabulation | STUDYID, USUBJID, MBTESTCD, VISITNUM, MBTPTREF, MBTPTNUM | mb.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0018.txt` 第 61-64 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 60|                                                                                              LBTPTNUM
 61| MB        Microbiology          Findings     One record per microbiology          Tabulation STUDYID, USUBJID,     mb.xpt
 62|           Specimen                           specimen finding per time point per             MBTESTCD, VISITNUM,
 63|                                              visit per subject                               MBTPTREF,
 64|                                                                                              MBTPTNUM
 65| MI        Microscopic Findings Findings      One record per finding per           Tabulation STUDYID, USUBJID,     mi.xpt
~~~~

KB 现文: `knowledge_base/chapters/ch03_submitting_data.md:54-54` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  54| | MB | Microbiology Specimen | Findings | One record per microbiology specimen finding per time point per visit per subject | Tabulation | STUDYID, USUBJID, MBTESTCD, VISITNUM, MBTPTREF, MBTPTNUM | mb.xpt |
~~~~

### E3. `ig34_p0056_a006` — ae:S1R1_ATOM_ERR

- PDF 页 56 · 原子类型 TABLE_ROW · 所在节 `§4.5.3.2 [Text Strings Greater than 200 Characters in Other Variables]`
- triage 类 **REAL_GAP** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T4 U-2 A (委托代裁): 原子第 2/3 格漏 'to improve readability' 与句点; PDF p56:37-40 与 KB ch04:1478 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t4_user_decisions.md:33`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
When splitting a text string into several records, the text should be split between words to improve readability | When splitting a text string into several records, the text should be split between words | When splitting a text string into several records, the text should be split between words | Not applicable
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0056.txt` 第 37-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36| the SUPP-- dataset                     to COVALn.                          to TSVALn.
 37| When splitting a text string into      When splitting a text string into   When splitting a text string into   Not applicable.
 38| several records, the text should be    several records, the text should    several records, the text should
 39| split between words to improve         be split between words to improve   be split between words to
 40| readability.                           readability.                        improve readability.
 41| The value for QLABEL should be the     The variable labels for COVAL1 to   The variable labels for TSVAL1 to   Not applicable.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1362` (来源: triage kb_loc knowledge_base/chapters/ch04_general_assumptions.md:1362 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
1360| | 6 | PRAG | PR Interval, Aggregate | | | | | | NOT DONE | 2 | 2015-03-14 |
1361| | 7 | EGALL | ECG Test Results | | | | | | NOT DONE | 3 | 2015-03-21 |
1362| 
1363| **Example 3**
1364| 
~~~~

### E4. `ig34_p0079_a004` — ae:S1R1_ATOM_ERR

- PDF 页 79 · 原子类型 SENTENCE · 所在节 `§5.3 [Subject Elements]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: S-SPREL SE asm 按 p79 渲染改词 (epochs and elements); 原子抄自旧错 KB | errata: t3_atom_err | new_target: domains/SE/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:2`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The Subject Elements dataset consolidates information about the timing of each subject's progress through the study elements of the trial.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0079.txt` 第 13-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12| A special-purpose domain that contains the actual order of elements followed by the subject, together with the start date/time and end date/time for each element.
 13| The Subject Elements dataset consolidates information about the timing of each subject’s progress through the epochs and elements of the trial. For elements that
 14| involve study treatments, the identification of which element the subject passed through (e.g., drug X vs. placebo) is likely to derive from data in the Exposure
 15| domain or another Interventions domain. The dates of a subject’s transition from one element to the next will be taken from the Interventions domain(s) and from
~~~~

KB 现文: `knowledge_base/domains/SE/assumptions.md:7-9` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
   7| The Subject Elements dataset consolidates information about the timing of each subject’s progress through the epochs and elements of the trial.
   8| 
   9| For elements that involve study treatments, the identification of which element the subject passed through (e.g., drug X vs. placebo) is likely to derive from data in the Exposure domain or another Interventions domain.
~~~~

### E5. `ig34_p0079_a006` — ae:S1R1_ATOM_ERR

- PDF 页 79 · 原子类型 SENTENCE · 所在节 `§5.3 [Subject Elements]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: S-SPREL SE asm 按 p79 渲染改词 (definitions (TESTRL values)); 原子抄自旧错 KB | errata: t3_atom_err | new_target: domains/SE/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:3`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The dates of a subject's transition from one element to the next will be taken from the Interventions domain(s) and from other relevant domains, according to the definitions of ELEMENT values in the Trial Elements (TE) dataset (see Section 7.2.2, Trial Elements).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0079.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| involve study treatments, the identification of which element the subject passed through (e.g., drug X vs. placebo) is likely to derive from data in the Exposure
 15| domain or another Interventions domain. The dates of a subject’s transition from one element to the next will be taken from the Interventions domain(s) and from
 16| other relevant domains, according to the definitions (TESTRL values) in the Trial Elements (TE) dataset (see Section 7.2.2, Trial Elements).
 17| The SE dataset is particularly useful for studies with multiple treatment periods, such as crossover studies. The SE dataset contains the date/times at which a
~~~~

KB 现文: `knowledge_base/domains/SE/assumptions.md:11-11` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  11| The dates of a subject’s transition from one element to the next will be taken from the Interventions domain(s) and from other relevant domains, according to the definitions (TESTRL values) in the Trial Elements (TE) dataset (see Section 7.2.2, Trial Elements).
~~~~

### E6. `ig34_p0079_a009` — ae:S1R1_ATOM_ERR

- PDF 页 79 · 原子类型 LIST_ITEM · 所在节 `§5.3 [Subject Elements]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: S-SPREL SE asm 按 p79 渲染 (--DTC); 原子抄自旧错 KB | errata: t3_atom_err | new_target: domains/SE/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:4`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Comparison of the – DTC of a finding observation to the element transition dates (values of SESTDTC and SEENDTC) identifies which element the subject was in at the time of the finding. Similarly, one can determine the element during which an event or intervention started or ended.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0079.txt` 第 21-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20| through the trial.
 21|      •    Comparison of the --DTC of a finding observation to the element transition dates (values of SESTDTC and SEENDTC) identifies which element the
 22|           subject was in at the time of the finding. Similarly, one can determine the element during which an event or intervention started or ended.
 23|      •    “Day within Element” or “Day within Epoch” can be derived. Such variables relate an observation to the start of an element or epoch in the same
~~~~

KB 现文: `knowledge_base/domains/SE/assumptions.md:17-17` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  17| - Comparison of the --DTC of a finding observation to the element transition dates (values of SESTDTC and SEENDTC) identifies which element the subject was in at the time of the finding. Similarly, one can determine the element during which an event or intervention started or ended.
~~~~

### E7. `ig34_p0079_a010` — ae:S1R1_ATOM_ERR

- PDF 页 79 · 原子类型 LIST_ITEM · 所在节 `§5.3 [Subject Elements]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: S-SPREL SE asm 按 p79 渲染 (Such variables relate / --DY); 原子抄自旧错 KB | errata: t3_atom_err | new_target: domains/SE/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=False; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:5`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
"Day within Element" or "Day within Epoch" can be derived. Such variables can relate an observation to the start of an element or epoch in the same way that study day (–DY) variables relate it to the reference start date (RFSTDTC) for the study as a whole. See Section 4.4.4, Use of the "Study Day" Variables.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0079.txt` 第 23-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 22|           subject was in at the time of the finding. Similarly, one can determine the element during which an event or intervention started or ended.
 23|      •    “Day within Element” or “Day within Epoch” can be derived. Such variables relate an observation to the start of an element or epoch in the same
 24|           way that study day (--DY) variables relate it to the reference start date (RFSTDTC) for the study as a whole. See Section 4.4.4, Use of the "Study Day"
 25|           Variables.
~~~~

KB 现文: `knowledge_base/domains/SE/assumptions.md:18-18` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  18| - “Day within Element” or “Day within Epoch” can be derived. Such variables relate an observation to the start of an element or epoch in the same way that study day (--DY) variables relate it to the reference start date (RFSTDTC) for the study as a whole. See Section 4.4.4, Use of the "Study Day" Variables.
~~~~

### E8. `ig34_p0086_a011` — ae:S1R1_ATOM_ERR

- PDF 页 86 · 原子类型 SENTENCE · 所在节 `§5.5 [Subject Visits (SV)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-SM audit: verbatim 错, 以渲染图为准 (SV Description); 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-SM_audit.md:26`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Comparison of an individual subject's SV dataset with the TV dataset, which describes the planned visits for the trial, supports the identification of planned but not completed visits.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0086.txt` 第 19-20 行 (自动定位, 词覆盖 0.955; 版式以原 PDF 为准):

~~~~
 18| studies, a visit may reflect data collection over a multiday period.
 19| The SV dataset provides reviewers with a summary of a subject’s visits over the course of their participation in a study. Comparison of an individual subject’s
 20| SV dataset with the TV dataset, which describes the planned visits for the trial, supports the identification of planned but not expected visits due to a subject not
 21| completing the study. Comparison of the values of SVSTDY and SVENDY to VISIT and/or VISITDY can often highlight departures from the planned timing of
~~~~

KB 现文: `knowledge_base/domains/SV/assumptions.md:9-9` (来源: fuzzy locate (score 0.955)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
   9| The SV dataset provides reviewers with a summary of a subject’s visits over the course of their participation in a study. Comparison of an individual subject’s SV dataset with the TV dataset, which describes the planned visits for the trial, supports the identification of planned but not expected visits due to a subject not completing the study. Comparison of the values of SVSTDY and SVENDY to VISIT and/or VISITDY can often highlight departures from the planned timing of visits.
~~~~

### E9. `ig34_p0122_a015` — ae:S1R1_ATOM_ERR

- PDF 页 122 · 原子类型 NOTE · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-ML review: 原子 verbatim 写成 NCIBI; KB 与 PDF 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ML_review.md:70`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCIBI codelist values are enclosed in parentheses.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0122.txt` 第 33-33 行 (自动定位, 词覆盖 0.955; 版式以原 PDF 为准):

~~~~
 32| 1
 33|  In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.
 34| 
~~~~

KB 现文: `knowledge_base/domains/ML/spec.md:339-339` (来源: fuzzy locate (score 0.955)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 339| > ¹In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.
~~~~

### E10. `ig34_p0122_a017` — ae:S1R1_ATOM_ERR

- PDF 页 122 · 原子类型 LIST_ITEM · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-ML review: 原子 verbatim 多 'not'; KB 与 PDF 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ML_review.md:70`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The ML domain is used to represent consumption of any food or nutritional item that would not be represented in the exposure domains (EC/EX), Concomitant/Prior Medications (CM), Procedure Agents (AG), or Substance Use (SU). Examples of nutritional items that would not be represented in other domains include:
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0122.txt` 第 36-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35| ML – Assumptions
 36|      1.   The ML domain is used to represent consumption of any food or nutritional item that would not be represented in the exposure domains (EC/EX),
 37|           Concomitant/Prior Medications (CM), Procedure Agents (AG), or Substance Use (SU). Examples of nutritional items that would be represented in other
 38|           domains include:
 39|           a.    Investigational nutritional products (represented in EC/EX)
~~~~

KB 现文: `knowledge_base/domains/ML/assumptions.md:13-13` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  13| 1. The ML domain is used to represent consumption of any food or nutritional item that would not be represented in the exposure domains (EC/EX), Concomitant/Prior Medications (CM), Procedure Agents (AG), or Substance Use (SU). Examples of nutritional items that would be represented in other domains include:
~~~~

### E11. `ig34_p0123_a012` — ae:S1R1_ATOM_ERR

- PDF 页 123 · 原子类型 NOTE · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-ML review: 原子 verbatim 写成 'row.'; KB 与 PDF 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ML_review.md:70`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Click here to add a row. ADD ROW
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 19-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18|    Snack        Nutritional drink X Meal                                       2015 Dec 31   19:00        CE003
 19| Click here to add a row: ADD ROW
 20| 
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:19-19` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  19| | Click here to add a row: **ADD ROW** | | | | | | |
~~~~

### E12. `ig34_p0124_a001` — ae:S1R1_ATOM_ERR

- PDF 页 124 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-ML review: 原子 verbatim MIDSDTC 截断; KB 与 PDF 一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-ML_review.md:70`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2 | XYZ | ML | XYZ-001-001 | 2 | NUTRITIONAL DRINK | HYPOGLYCEMIA EVALUATION | Y | Y | 8 | oz | | 2015-09-03T08:30 | | | LAST MEAL PRIOR TO | HYPO2 | 2015-09-03T17:00
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0124.txt` 第 2-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Row STUDYID DOMAIN USUBJID MLSEQ MLTRT                         MLCAT             MLPRESP MLOCCUR MLDOSE MLDOSU MLDTC MLSTDTC                      MLENDTC MLEVLINT RELMIDS   MIDS  MIDSDTC
  2| 2   XYZ     ML     XYZ-001- 2    NUTRITIONAL                   HYPOGLYCEMIA      Y       Y       8      oz           2015-09-                                      LAST      HYPO2 2015-09-
  3|                    001           DRINK                         EVALUATION                                            03T08:30                                      MEAL            03T17:00
  4|                                                                                                                                                                    PRIOR
  5|                                                                                                                                                                    TO
  6| 3     XYZ          ML       XYZ-001-   3       MEAL            HYPOGLYCEMIA      Y          Y                                         2015-12-                     LAST      HYPO3 2016-01-
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:42` (来源: decision.evidence.hit):

~~~~
  42| | 2 | XYZ | ML | XYZ-001-001 | 2 | NUTRITIONAL DRINK | HYPOGLYCEMIA EVALUATION | Y | Y | 8 | oz | | 2015-09-03T08:30 | | | LAST MEAL PRIOR TO | HYPO2 | 2015-09-03T17:00 |
~~~~

### E13. `ig34_p0133_a003` — ae:S1R1_ATOM_ERR

- PDF 页 133 · 原子类型 TABLE_ROW · 所在节 `§6.1.6 [Substance Use (SU)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-SU review: 原子 verbatim 串列 (多 '2006-01-01'); KB 按渲染图正确; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-SU_review.md:28`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | 1234 | SU | 1234005 | 1 | CIGARETTES | TOBACCO | | | | 2 | PACK | QD | | | 2006-01-01 | | 2006-01-01 | BEFORE | 2006-01-01 | ONGOING |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0133.txt` 第 3-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| Row STUDYID DOMAIN USUBJID SUSEQ SUTRT      SUCAT   SUSTAT SUREASND                        SUDOSE SUDOSU SUDOSFRQ SUSTDTC SUENDTC SUSTTPT SUSTRTPT SUENTPT SUENRTPT
  3| 1   1234    SU     1234005 1     CIGARETTES TOBACCO                                        2      PACK   QD                         2006-01- BEFORE 2006-01- ONGOING
  4|                                                                                                                                     01              01
~~~~

KB 现文: `knowledge_base/domains/SU/examples.md:37-37` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  37| | 1 | 1234 | SU | 1234005 | 1 | CIGARETTES | TOBACCO | | | 2 | PACK | QD | | | 2006-01-01 | BEFORE | 2006-01-01 | ONGOING |
~~~~

### E14. `ig34_p0150_a007` — ae:S1R1_ATOM_ERR

- PDF 页 150 · 原子类型 LIST_ITEM · 所在节 `§6.2.3 [Clinical Events (CE)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-CE writer: 原子抽错, KB 按渲染图正确; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CE.md:63`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
(a) Events considered to be clinical events may include episodes of symptoms of the disease under study (often known as "signs and symptoms"), or events that do not constitute adverse events in themselves, though they might lead to the identification of an adverse event. For example, in a study of an investigational treatment for migraine headaches, migraine headaches may not be considered as adverse events per protocol. The occurrence of migraines or associated signs and symptoms might be reported in CE.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0150.txt` 第 19-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18|            CEs.
 19|            a.   Events considered to be clinical events may include episodes of symptoms of the disease under study (often known as "signs and symptoms"), or
 20|                 events that do not constitute adverse events in themselves, though they might lead to the identification of an adverse event. For example, in a study
 21|                 of an investigational treatment for migraine headaches, migraine headaches may not be considered to be adverse events per protocol. The
 22|                 occurrence of migraines or associated signs and symptoms might be reported in CE.
 23|            b.   In vaccine trials, certain adverse events may be considered to be signs or symptoms and accordingly determined to be clinical events. If any event is
~~~~

KB 现文: `knowledge_base/domains/CE/assumptions.md:14-14` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  14|    a. Events considered to be clinical events may include episodes of symptoms of the disease under study (often known as "signs and symptoms"), or events that do not constitute adverse events in themselves, though they might lead to the identification of an adverse event. For example, in a study of an investigational treatment for migraine headaches, migraine headaches may not be considered to be adverse events per protocol. The occurrence of migraines or associated signs and symptoms might be reported in CE.
~~~~

### E15. `ig34_p0150_a008` — ae:S1R1_ATOM_ERR

- PDF 页 150 · 原子类型 LIST_ITEM · 所在节 `§6.2.3 [Clinical Events (CE)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-CE writer: 原子抽错, KB 按渲染图正确; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CE_audit.md:19`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
(b) In vaccine trials, certain adverse events may be considered to be signs of symptomatology and accordingly determined to be clinical events. If any event is considered serious, then the serious adverse event flag (--SER) and the serious adverse event flags (--SCAT, --SCOD, --SDTH, --SDHSP, --SLIFE, --SOD, --SMIE) would be required in the CE domain.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0150.txt` 第 22-25 行 (自动定位, 词覆盖 0.872; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 21|                 of an investigational treatment for migraine headaches, migraine headaches may not be considered to be adverse events per protocol. The
 22|                 occurrence of migraines or associated signs and symptoms might be reported in CE.
 23|            b.   In vaccine trials, certain adverse events may be considered to be signs or symptoms and accordingly determined to be clinical events. If any event is
 24|                 considered serious, then the serious variable (--SER) and the serious adverse event flags (--SCAN, --SCONG, --SDTH, --SHOSP, --SDISAB, --
 25|                 SLIFE, --SOD, --SMIE) would be required in the CE domain.
 26|            c.   Other studies might track the occurrence of specific events as efficacy endpoints. For example, in a study of an investigational treatment for
~~~~

KB 现文: `knowledge_base/domains/CE/assumptions.md:14-15` (来源: fuzzy locate (score 0.872)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  14|    a. Events considered to be clinical events may include episodes of symptoms of the disease under study (often known as "signs and symptoms"), or events that do not constitute adverse events in themselves, though they might lead to the identification of an adverse event. For example, in a study of an investigational treatment for migraine headaches, migraine headaches may not be considered to be adverse events per protocol. The occurrence of migraines or associated signs and symptoms might be reported in CE.
  15|    b. In vaccine trials, certain adverse events may be considered to be signs or symptoms and accordingly determined to be clinical events. If any event is considered serious, then the serious variable (--SER) and the serious adverse event flags (--SCAN, --SCONG, --SDTH, --SHOSP, --SDISAB, --SLIFE, --SOD, --SMIE) would be required in the CE domain.
~~~~

### E16. `ig34_p0150_a009` — ae:S1R1_ATOM_ERR

- PDF 页 150 · 原子类型 LIST_ITEM · 所在节 `§6.2.3 [Clinical Events (CE)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EQUIVALENT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-CE writer: 原子抽错, KB 按渲染图正确; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CE.md:63 (页级行; 该批以范围/页号记这组原子)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
(c) Other studies might track the occurrence of specific events as efficacy endpoints. For example, in a study of an investigational treatment for prevention of ischemic stroke, all occurrences of TIA, stroke, and death might be captured as clinical events and assessed as to whether they meet endpoint criteria. Note that other information about these events may be reported in other datasets. For example, the event leading to death would be reported in AE; death would also be a record in the Disposition (DS) domain.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0150.txt` 第 26-29 行 (自动定位, 词覆盖 0.982; 版式以原 PDF 为准):

~~~~
 25|                 SLIFE, --SOD, --SMIE) would be required in the CE domain.
 26|            c.   Other studies might track the occurrence of specific events as efficacy endpoints. For example, in a study of an investigational treatment for
 27|                 prevention of ischemic stroke, all occurrences of TIA, stroke, and death might be captured as clinical events and assessed as to whether they meet
 28|                 endpoint criteria. Note that other information about these events may be reported in other datasets. For example, the event leading to death would be
 29|                 reported in AE; death would also be a reason for study discontinuation in the Disposition (DS) domain.
 30|      2.    CEOCCUR and CEPRESP are used together to indicate whether the event in CETERM was prespecified and whether it occurred. CEPRESP can be
~~~~

KB 现文: `knowledge_base/domains/CE/assumptions.md:16-16` (来源: fuzzy locate (score 0.982)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  16|    c. Other studies might track the occurrence of specific events as efficacy endpoints. For example, in a study of an investigational treatment for prevention of ischemic stroke, all occurrences of TIA, stroke, and death might be captured as clinical events and assessed as to whether they meet endpoint criteria. Note that other information about these events may be reported in other datasets. For example, the event leading to death would be reported in AE; death would also be a reason for study discontinuation in the Disposition (DS) domain.
~~~~

### E17. `ig34_p0150_a012` — ae:S1R1_ATOM_ERR

- PDF 页 150 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events (CE)]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-CE writer: 原子抽错, KB 按渲染图正确; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-CE.md:63 (页级行; 该批以范围/页号记这组原子)`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Spontaneously reported event occurrence | | Y | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0150.txt` 第 35-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34|                                                                   CEPRESP                      CEOCCUR                      CESTAT
 35|             Spontaneously reported event occurrence
 36|             Prespecified event occurred                                Y                            Y
 37|             Prespecified event did not occur                           Y                            N
~~~~

KB 现文: `knowledge_base/domains/CE/assumptions.md:22-23` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  22|    | Spontaneously reported event occurrence | | | |
  23|    | Prespecified event occurred | Y | Y | |
~~~~

### E18. `ig34_p0153_a0034` — ae:S1R1_ATOM_ERR

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `B-CE`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | errata: t3_atom_err | in_atom_err=False in_remap=False; 出处 `.work/10_tier_b_repair/evidence/t2_fp_expected_regressions.md:62`
- 登记 `B-CE T-2`: PDF 写 "USUBJID ABC -US-701-002 (mh/ce/pr 8 格)" → KB 写 "照录" (处理: 照录+T4; 依据: USUBJID 惯例不含空格; PDF 8 处一致带空格 (O44: 3.5pt 字距说法不成立); KB `knowledge_base/domains/CE/examples.md:101`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC | MH | ABC-US-701-002 | 1 | 1 | MH1 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | RIB 3 | RIGHT | Y | 2006-05-13 | 2005-08-18 | -P5Y |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 39-41 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38| Row STUDYID DOMAIN USUBJID          MHSEQ MHGRPID MHSPID MHTERM             MHCAT         MHSCAT              MHPRESP MHOCCUR MHLOC MHLAT MHCONTRT MHDTC MHSTDTC MHEVLINT
 39| 1   ABC     MH     ABC -US-         1     1       MH1    Fracture           FRACTURE-                         Y       Y       RIB 3 RIGHT Y        2006- 2005-08- -P5Y
 40|                    701-002                                                  RELATED                                                                05-13 18
 41|                                                                             EVENTS
 42| 
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:101` (来源: registry B-CE T-2 kb_line_now):

~~~~
 101| | 1 | ABC | MH | ABC -US-701-002 | 1 | 1 | MH1 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | RIB 3 | RIGHT | Y | 2006-05-13 | 2005-08-18 | -P5Y |
~~~~

### E19. `ig34_p0154_a0002` — ae:S1R1_ATOM_ERR

- PDF 页 154 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `B-CE`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | errata: t3_atom_err | in_atom_err=False in_remap=False; 出处 `.work/10_tier_b_repair/evidence/t2_fp_expected_regressions.md:63`
- 登记 `B-CE T-2`: PDF 写 "USUBJID ABC -US-701-002 (mh/ce/pr 8 格)" → KB 写 "照录" (处理: 照录+T4; 依据: USUBJID 惯例不含空格; PDF 8 处一致带空格 (O44: 3.5pt 字距说法不成立); KB `knowledge_base/domains/CE/examples.md:101`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC | MH | ABC-US-701-002 | 2 | 1 | | Soft Tissue Damage | FRACTURE-RELATED EVENTS | COMPLICATIONS | Y | Y | LUNG | | | 2006-05-13 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0154.txt` 第 2-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Row STUDYID DOMAIN USUBJID          MHSEQ MHGRPID MHSPID MHTERM            MHCAT           MHSCAT        MHPRESP MHOCCUR MHLOC MHLAT MHCONTRT MHDTC MHSTDTC MHEVLINT
  2| 2   ABC     MH     ABC -US-         2     1              Soft              FRACTURE-       COMPLICATIONS Y       Y       LUNG                 2006-
  3|                    701-002                               Tissue            RELATED                                                            05-13
  4|                                                          Damage            EVENTS
  5| 
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:101` (来源: registry B-CE T-2 kb_line_now):

~~~~
 101| | 1 | ABC | MH | ABC -US-701-002 | 1 | 1 | MH1 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | RIB 3 | RIGHT | Y | 2006-05-13 | 2005-08-18 | -P5Y |
~~~~

### E20. `ig34_p0154_a0013` — ae:S1R1_ATOM_ERR

- PDF 页 154 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `B-CE`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | errata: t3_atom_err | in_atom_err=False in_remap=False; 出处 `.work/10_tier_b_repair/evidence/t2_fp_expected_regressions.md:64`
- 登记 `B-CE T-2`: PDF 写 "USUBJID ABC -US-701-002 (mh/ce/pr 8 格)" → KB 写 "照录" (处理: 照录+T4; 依据: USUBJID 惯例不含空格; PDF 8 处一致带空格 (O44: 3.5pt 字距说法不成立); KB `knowledge_base/domains/CE/examples.md:101`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC | CE | ABC-US-701-002 | 1 | | CE1 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | HUMERUS | RIGHT | Y | 2006-07-09 | 2006-07-03 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0154.txt` 第 18-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| Row STUDYID DOMAIN USUBJID              CESEQ CEGRPID CESPID CETERM            CECAT          CESCAT            CEPRESP CEOCCUR CELOC   CELAT CECONTRT CEDTC CESTDTC
 18| 1   ABC     CE     ABC -US-             1             CE1    Fracture          FRACTURE-                        Y       Y       HUMERUS RIGHT Y        2006- 2006-07-
 19|                    701-002                                                     RELATED                                                                 07-09 03
 20|                                                                                EVENTS
 21| 2        ABC       CE        ABC -US-   2        1        CE2      Fracture    FRACTURE-                        Y       Y            FIBULA      LEFT      N         2006-   2006-10-
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:101` (来源: registry B-CE T-2 kb_line_now):

~~~~
 101| | 1 | ABC | MH | ABC -US-701-002 | 1 | 1 | MH1 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | RIB 3 | RIGHT | Y | 2006-05-13 | 2005-08-18 | -P5Y |
~~~~

### E21. `ig34_p0154_a0014` — ae:S1R1_ATOM_ERR

- PDF 页 154 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **-** · 终态 **ATOM_ERR** (T3 前 EXACT) · 判定规则 `S1-R1` · 批 `B-CE`
- 原子抽错登记: R1 → ATOM_ERR; 依据: T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2 照录, T4 主控裁定) | errata: t3_atom_err | in_atom_err=False in_remap=False; 出处 `.work/10_tier_b_repair/evidence/t2_fp_expected_regressions.md:65`
- 登记 `B-CE T-2`: PDF 写 "USUBJID ABC -US-701-002 (mh/ce/pr 8 格)" → KB 写 "照录" (处理: 照录+T4; 依据: USUBJID 惯例不含空格; PDF 8 处一致带空格 (O44: 3.5pt 字距说法不成立); KB `knowledge_base/domains/CE/examples.md:101`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC | CE | ABC-US-701-002 | 2 | 1 | CE2 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | FIBULA | LEFT | N | 2006-10-23 | 2006-10-15 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0154.txt` 第 20-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19|                    701-002                                                     RELATED                                                                 07-09 03
 20|                                                                                EVENTS
 21| 2        ABC       CE        ABC -US-   2        1        CE2      Fracture    FRACTURE-                        Y       Y            FIBULA      LEFT      N         2006-   2006-10-
 22|                              701-002                                           RELATED                                                                               10-23   15
 23|                                                                                EVENTS
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:101` (来源: registry B-CE T-2 kb_line_now):

~~~~
 101| | 1 | ABC | MH | ABC -US-701-002 | 1 | 1 | MH1 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | RIB 3 | RIGHT | Y | 2006-05-13 | 2005-08-18 | -P5Y |
~~~~

