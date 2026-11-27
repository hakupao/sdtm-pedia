# T4.1 Q9 扩检包 7 — Q9_IG34_EQUIV (26 条; 编号 Q154-Q179)

> 由 `scripts/t4/t4_q9_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (加前缀 Q).

### Q154. `ig34_p0029_a010` — q9:Q9_IG34_EQUIV

- PDF 页 29 · 原子类型 SENTENCE · 所在节 `§4.2.3 [Use of "Subject" and USUBJID]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This means that no 2 or more subjects, across all trials in the submission, may have the same USUBJID.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0029.txt` 第 12-13 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11| The unique subject identifier (USUBJID) is required in all datasets containing subject-level data. USUBJID values
 12| must be unique for each trial participant (subject) across all trials in the submission. This means that no 2 or more
 13| subjects, across all trials in the submission, may have the same USUBJID. In addition, the same person who
 14| participates in multiple clinical trials (when this is known) must be assigned the same USUBJID value in all trials.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:296` (来源: live valid_hits):

~~~~
 296| The unique subject identifier (USUBJID) is required in all datasets containing subject-level data. USUBJID values must be unique for each trial participant (subject) across all trials in the submission. This means that no 2 or more subjects, across all trials in the submission, may have the same USUBJID. In addition, the same person who participates in multiple clinical trials (when this is known) must be assigned the same USUBJID value in all trials.
~~~~

### Q155. `ig34_p0048_a024` — q9:Q9_IG34_EQUIV

- PDF 页 48 · 原子类型 SENTENCE · 所在节 `§4.4.10 [Representing Time Points]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
However, because --ELTM can only be populated with ISO 8601 periods of time (as described in Section 4.4.3, Intervals of Time and Use of Duration for --DUR Variables), --ELTM may not be populated for all time points.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0048.txt` 第 28-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27| Within the context that defines uniqueness for a time point, there is likely to be a one-to-one relationship between
 28| most values of --TPT and --ELTM. However, because --ELTM can only be populated with ISO 8601 periods of
 29| time (as described in Section 4.4.3, Intervals of Time and Use of Duration for --DUR Variables), --ELTM may not
 30| be populated for all time points. For example, --ELTM is likely to be null for time points described by text such as
 31| "pre-dose" or "before breakfast." When --ELTM is populated, if 2 subjects have records with the same values of
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1177` (来源: live valid_hits):

~~~~
1177| Within the context that defines uniqueness for a time point, there is likely to be a one-to-one relationship between most values of --TPT and --ELTM. However, because --ELTM can only be populated with ISO 8601 periods of time (as described in Section 4.4.3, Intervals of Time and Use of Duration for --DUR Variables), --ELTM may not be populated for all time points. For example, --ELTM is likely to be null for time points described by text such as "pre-dose" or "before breakfast." When --ELTM is populated, if 2 subjects have records with the same values of DOMAIN, VISITNUM, --TPTREF, and --TPTNUM, then these records may not have different values in --ELTM.
~~~~

### Q156. `ig34_p0057_a006` — q9:Q9_IG34_EQUIV

- PDF 页 57 · 原子类型 SENTENCE · 所在节 `§4.5.4 [Evaluators in the Interventions and Events Observation Classes]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
See Section 8.4, Relating Non-standard Variable Values to a Datasets.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0056.txt` 第 54-60 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 53| evaluation into the standard domain dataset and data from the secondary evaluation into the Supplemental Qualifier
 54| datasets (SUPP--). Within each SUPP-- record, the value for QNAM should be formed by appending a "1" to the
 55| corresponding standard domain variable name. In cases where the standard domain variable name is already 8
 56| characters in length, sponsors should replace the last character with a "1" (incremented for each additional
 57| attribution).
 58| This example illustrates a case where an adjudication committee evaluated an adverse event. The evaluations of the
 59| adverse event by the primary investigator were represented in the standard AE dataset. The evaluations of the
 60| adjudication committee were represented in SUPPAE. See Section 8.4, Relating Non-standard Variable Values to a
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:568-570` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 568| The SDTM permits 1 value for each qualifier variable per record. If multiple values exist (e.g., due to a "Check all that apply" instruction on a CRF), then the value for the qualifier variable should be "MULTIPLE" and SUPP-- should be used to store the individual responses. It is recommended that the SUPP-- QNAM value reference the corresponding standard domain variable with an appended number or letter. In some cases, the standard variable name will be shortened to meet the 8-character variable name requirement, or it may be clearer to append a meaningful character string as shown in the second Adverse Events (AE) example below, where the first 3 characters of the drug name are appended. Likewise, the QLABEL value should be similar to the standard label. The values stored in QVAL should be consistent with the controlled terminology associated with the standard variable. See Section 8.4, Relating Non-standard Variable Values to a Parent Domain, for additional guidance on maintaining appropriately unique QNAM values.
 569| 
 570| The following example includes selected variables from the ae.xpt and suppae.xpt datasets for a rash with locations on the face, neck, and chest.
~~~~

### Q157. `ig34_p0061_a009` — q9:Q9_IG34_EQUIV

- PDF 页 61 · 原子类型 SENTENCE · 所在节 `§5.1 [Comments (CO)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Assumptions for populating IDVAR and IDVARVAL are further described in Section 8.5, Relating Comments to a Parent Domain.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0061.txt` 第 14-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13|                of the parent record(s) and the variables IDVAR and IDVARVAL are populated with the key variable name and value of the parent record(s).
 14|                Assumptions for populating IDVAR and IDVARVAL are further described in Section 8.5, Relating Comments to a Parent Domain. CODTC should
 15|                be null because the timing of the parent record(s) is inherited by the comment record. See Example 1, rows 3-5.
~~~~

KB 现文: `knowledge_base/domains/CO/assumptions.md:26` (来源: live valid_hits):

~~~~
  26|    c. Those related to a specific parent record or group of parent records, in which case the value of the variable RDOMAIN is set to the DOMAIN code of the parent record(s) and the variables IDVAR and IDVARVAL are populated with the key variable name and value of the parent record(s). Assumptions for populating IDVAR and IDVARVAL are further described in Section 8.5, Relating Comments to a Parent Domain. CODTC should be null because the timing of the parent record(s) is inherited by the comment record. See Example 1, rows 3-5.
~~~~

### Q158. `ig34_p0065_a026` — q9:Q9_IG34_EQUIV

- PDF 页 65 · 原子类型 SENTENCE · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Example 3 below provides an example of this situation; see also Section 5.3, Subject Elements, Example 2.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0065.txt` 第 40-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39|              between these truncated codes should be maintained for all affected subjects in the trial. Example 3
 40|              below provides an example of this situation; see also Section 5.3, Subject Elements, Example 2. Note
 41|              that this use of values not in the TA dataset is allowable only for trials with multistage assignment to
~~~~

KB 现文: `knowledge_base/domains/DM/assumptions.md:25` (来源: live valid_hits):

~~~~
  25|    b. Multistage assignment to treatment: Some trials use a multistage process for assigning a subject to an arm (see Section 7.2.1, Trial Arms, Example Trial 3). In such a case, best practice is to create ARMCD values composed of codes representing the results of the multiple stages of the treatment assignment process. If a subject is partially assigned, then truncated codes representing the stages completed can be used in ARMCD, and similar truncated codes can be used in ACTARMCD. The descriptions used to populate ARM and ACTARM should be similarly truncated, and the one-to-one relationship between these truncated codes should be maintained for all affected subjects in the trial. Example 3 below provides an example of this situation; see also Section 5.3, Subject Elements, Example 2. Note that this use of values not in the TA dataset is allowable only for trials with multistage assignment to arms and to subjects in those trials who do not complete all stages of the assignment.
~~~~

### Q159. `ig34_p0068_a014` — q9:Q9_IG34_EQUIV

- PDF 页 68 · 原子类型 SENTENCE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This study included 2 elements, screen and run-in, before subjects were randomized to treatment.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0068.txt` 第 28-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27| This example Demographics dataset does not include all the DM required and expected variables, only those that illustrate the variables that represent arm information. The following example illustrates values of
 28| ARMCD for subjects in Example Trial 1, described in Section 7.2.1, Trial Arms. This study included 2 elements, screen and run-in, before subjects were randomized to treatment. For this study,
 29| the sponsor submitted data on all subjects, including screen-failure subjects.
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:18` (来源: live valid_hits):

~~~~
  18| This example Demographics dataset does not include all the DM required and expected variables, only those that illustrate the variables that represent arm information. The following example illustrates values of ARMCD for subjects in Example Trial 1, described in Section 7.2.1, Trial Arms. This study included 2 elements, screen and run-in, before subjects were randomized to treatment. For this study, the sponsor submitted data on all subjects, including screen-failure subjects.
~~~~

### Q160. `ig34_p0101_a010` — q9:Q9_IG34_EQUIV

- PDF 页 101 · 原子类型 SENTENCE · 所在节 `§6.1.2 [Concomitant/Prior Medications (CM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The date the subject began using the medication (or at least a partial date) would be stored in CMSTDTC.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0101.txt` 第 10-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9|                 specified time points. For example, assume a subject uses birth control medication. The subject has used the same medication for many years and
 10|                 continues to do so. The date the subject began using the medication (or at least a partial date) would be stored in CMSTDTC. CMENDTC is null
 11|                 because the end date is unknown/has not yet happened. This fact can be recorded by setting CMENTPT = "2007-04-30" (the date the assessment
~~~~

KB 现文: `knowledge_base/domains/CM/assumptions.md:27` (来源: live valid_hits):

~~~~
  27|    a. CMSTRTPT, CMSTTPT, CMENRTPT, and CMENTPT may be populated as necessary to indicate when a medication was used relative to specified time points. For example, assume a subject uses birth control medication. The subject has used the same medication for many years and continues to do so. The date the subject began using the medication (or at least a partial date) would be stored in CMSTDTC. CMENDTC is null because the end date is unknown/has not yet happened. This fact can be recorded by setting CMENTPT = "2007-04-30" (the date the assessment was made) and CMENRTPT = "ONGOING".
~~~~

### Q161. `ig34_p0115_a028` — q9:Q9_IG34_EQUIV

- PDF 页 115 · 原子类型 SENTENCE · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The following CRFs show data for 2 subjects.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0115.txt` 第 32-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| minutes prior to a standardized breakfast. There was a 6-day washout period between treatments.
 32| The following CRFs show data for 2 subjects.
 33| Subject 56789001
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:239` (来源: live valid_hits):

~~~~
 239| The following CRFs show data for 2 subjects.
~~~~

### Q162. `ig34_p0121_a003` — q9:Q9_IG34_EQUIV

- PDF 页 121 · 原子类型 SENTENCE · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
An interventions domain that contains information describing a subject's food product consumption.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0121.txt` 第 3-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| ML – Description/Overview
  3| An interventions domain that contains information describing a subject's food product consumption.
  4| ML – Specification
~~~~

KB 现文: `knowledge_base/domains/ML/assumptions.md:5` (来源: live valid_hits):

~~~~
   5| An interventions domain that contains information describing a subject's food product consumption.
~~~~

### Q163. `ig34_p0248_a011` — q9:Q9_IG34_EQUIV

- PDF 页 248 · 原子类型 SENTENCE · 所在节 `§6.3.5.6 Laboratory Test Results (LB)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Example 5
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0248.txt` 第 15-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| 
 15| Example 5
 16| This example illustrates the use of the LBBDAGNT variable for a single agent. Note: More complex use cases may require additional concepts for complete modeling. In this simple target engagement assessment,
~~~~

KB 现文: `knowledge_base/domains/LB/examples.md:88` (来源: live valid_hits):

~~~~
  88| ## Example 5
~~~~

### Q164. `ig34_p0279_a036` — q9:Q9_IG34_EQUIV

- PDF 页 279 · 原子类型 SENTENCE · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8 relationships are the same as in Example 1, they are not included here.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0279.txt` 第 40-41 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39| for the 2 excluded PC records, PCGRPID = "EXCLUDE"; for other PC records, PCGRPID = "DY1_DRGX".
 40| All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8
 41| relationships are the same as in Example 1, they are not included here.
 42| Method A (Many to Many, Using PCGRPID and PPGRPID)
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### Q165. `ig34_p0282_a026` — q9:Q9_IG34_EQUIV

- PDF 页 282 · 原子类型 SENTENCE · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 4`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Only some records in PC were used to calculate parameters; time point 5 was excluded from Tmax, time point 6 from Cmax, and time points 11 and 12 from AUC.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0282.txt` 第 28-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27| Example 4
 28| Only some records in PC were used to calculate parameters; time point 5 was excluded from Tmax, time point 6
 29| from Cmax, and time points 11 and 12 from AUC.
 30| This example uses --GRPID values in the PCGRPID (Example 4) and PPGRPID (Example 4) columns. Note that 4
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### Q166. `ig34_p0297_a034` — q9:Q9_IG34_EQUIV

- PDF 页 297 · 原子类型 SENTENCE · 所在节 `§6.3.7.4 Nervous System Findings (NV)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
To interpret, each VEP component is compared against normative values established by the laboratory using healthy controls.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0297.txt` 第 38-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37| POTENTIAL". Several latencies from each eye—including N75, P100, and N145, as well as the P100 peak-to-peak amplitude (75-100)—are collected and should be represented in NVTESTCD/NVTEST. Details
 38| about the VEP equipment including the checkerboard size should be represented in the appropriate device domains. To interpret, each VEP component is compared against normative values established by the
 39| laboratory using healthy controls.
 40| In this example, a VEP component is considered abnormal if it falls outside of 3 standard deviations from the normative lab mean. These low and high values are stored in NVORNRLO and NVORNRHI,
~~~~

KB 现文: `knowledge_base/domains/NV/examples.md:61` (来源: live valid_hits):

~~~~
  61| This example shows how to represent components of a pattern-reversal visual evoked-potential (VEP) test elicited by checkerboard stimuli for a subject with optic neuritis. VEPs are detected via an EEG using leads that are placed on the back of the subject’s head. It is important to note that the nature of VEP testing is such that NVMETHOD should be equal to "EEG", and that NVCAT should be equal to "VISUAL EVOKED POTENTIAL". Several latencies from each eye—including N75, P100, and N145, as well as the P100 peak-to-peak amplitude (75-100)—are collected and should be represented in NVTESTCD/NVTEST. Details about the VEP equipment including the checkerboard size should be represented in the appropriate device domains. To interpret, each VEP component is compared against normative values established by the laboratory using healthy controls.
~~~~

### Q167. `ig34_p0311_a024` — q9:Q9_IG34_EQUIV

- PDF 页 311 · 原子类型 SENTENCE · 所在节 `§6.3.7.7 Respiratory System Findings (RE)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The spirometry report also included an indicator that 1 of the attempts was considered to have produced an inadequate result, with the reasons the result was considered inadequate.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0311.txt` 第 25-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24| attempts to be made, and for the best result to be used in analyses. In this example, the spirometry report included an indicator of which was the best result. The
 25| spirometry report also included an indicator that 1 of the attempts was considered to have produced an inadequate result, with the reasons the result was
 26| considered inadequate.
~~~~

KB 现文: `knowledge_base/domains/RE/examples.md:42` (来源: live valid_hits):

~~~~
  42| In this example, a subject made 4 attempts at the FEV1 pulmonary function test, and data about all attempts were collected. It is standard practice for multiple attempts to be made, and for the best result to be used in analyses. In this example, the spirometry report included an indicator of which was the best result. The spirometry report also included an indicator that 1 of the attempts was considered to have produced an inadequate result, with the reasons the result was considered inadequate.
~~~~

### Q168. `ig34_p0399_a033` — q9:Q9_IG34_EQUIV

- PDF 页 399 · 原子类型 SENTENCE · 所在节 `§7.2.1 Trial Arms (TA) – Example 7`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The following diagram is based on the text "schema" in the protocol, with the 5 options it names.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0399.txt` 第 46-47 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 45| who do not have disease progression will necessarily receive surgery. If they are poor candidates for surgery or do
 46| not wish to receive surgery, they will not receive surgery, but will receive further chemotherapy. The following
 47| diagram is based on the text “schema” in the protocol, with the 5 options it names. The diagram in this form might
 48| suggest that the trial has 5 arms.
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:869` (来源: live valid_hits):

~~~~
 869| Example Trial 7, RTOG 93-09, involves treatment of lung cancer with chemotherapy and radiotherapy, with or without surgery. The protocol (RTOG-93-09), which was provided by the Radiation Oncology Therapy Group (RTOG), does not include a study schema diagram, but does include a text-based representation of diverging “options” to which a subject may be assigned. All subjects go through the branch point at randomization, when they are assigned to either chemotherapy plus radiotherapy (CR) or chemotherapy and radiotherapy plus surgery (CRS). All subjects receive induction chemotherapy and radiation, with a slight difference between those randomized to the 2 arms during the second cycle of chemotherapy. Those randomized to the non-surgery arm are evaluated for disease somewhat earlier, to avoid delays in administering the radiation boost to those whose disease has not progressed. After induction chemotherapy and radiation, subjects are evaluated for disease progression, and those whose disease has progressed stop treatment, but enter follow-up. Not all subjects randomized to receive surgery who do not have disease progression will necessarily receive surgery. If they are poor candidates for surgery or do not wish to receive surgery, they will not receive surgery, but will receive further chemotherapy. The following diagram is based on the text “schema” in the protocol, with the 5 options it names. The diagram in this form might suggest that the trial has 5 arms.
~~~~

### Q169. `ig34_p0406_a014` — q9:Q9_IG34_EQUIV

- PDF 页 406 · 原子类型 SENTENCE · 所在节 `§7.2.2.1 Trial Elements Issues – Distinguishing Elements, Study Cells, and Epochs`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
It becomes tedious to do this in every case, but can be useful to resolve confusion when it arises or is likely to arise.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0406.txt` 第 19-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18| the values of ELEMENT or EPOCH when these values (e.g., screening, follow-up) would otherwise be the same. It
 19| becomes tedious to do this in every case, but can be useful to resolve confusion when it arises or is likely to arise.
 20| The difference between epoch and element is perhaps clearest in crossover trials. In TA Example Trial 2, as for most
~~~~

KB 现文: `knowledge_base/domains/TE/examples.md:71` (来源: live valid_hits):

~~~~
  71| In describing a trial, one way to avoid confusion between elements and epochs is to include "Element" or "Epoch" in the values of ELEMENT or EPOCH when these values (e.g., screening, follow-up) would otherwise be the same. It becomes tedious to do this in every case, but can be useful to resolve confusion when it arises or is likely to arise.
~~~~

### Q170. `ig34_p0042_a024` — q9:Q9_IG34_EQUIV

- PDF 页 42 · 原子类型 LIST_ITEM · 所在节 `§4.4.5 [Clinical Encounters and Visits]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
VISITDY must not be populated for unplanned visits; VISITDY is, by definition, the planned study day of visit. The actual study day of an unplanned visit belongs in a --DY variable.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0042.txt` 第 44-45 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 43|           visits, or individual values may be assigned to different unplanned visits.
 44|     •     VISITDY must not be populated for unplanned visits; VISITDY is, by definition, the planned study day of
 45|           visit. The actual study day of an unplanned visit belongs in a --DY variable.
 46| The following lb.xpt sample rows show how visit identifiers might be used for lab data.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:912` (来源: live valid_hits):

~~~~
 912| - VISITDY must not be populated for unplanned visits; VISITDY is, by definition, the planned study day of visit. The actual study day of an unplanned visit belongs in a --DY variable.
~~~~

### Q171. `ig34_p0052_a023` — q9:Q9_IG34_EQUIV

- PDF 页 52 · 原子类型 LIST_ITEM · 所在节 `§4.5.1.2 [Tests Not Done]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
LBTESTCD would be "LBALL"
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0052.txt` 第 27-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26| For example, if urinalysis tests were not done, then:
 27|     •    LBTESTCD would be "LBALL"
 28|     •    LBTEST would be "Laboratory Test Results"
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1298` (来源: live valid_hits):

~~~~
1298| - LBTESTCD would be "LBALL"
~~~~

### Q172. `ig34_p0055_a013` — q9:Q9_IG34_EQUIV

- PDF 页 55 · 原子类型 LIST_ITEM · 所在节 `§4.5.3.2 [Text Strings Greater than 200 Characters in Other Variables]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The value for QNAMs for additional text (>200 characters) should contain a sequential variable name, which is formed by appending a 1-digit integer, beginning with 1, to the original domain variable name.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0055.txt` 第 20-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19|          the NSV without any numeric suffix.
 20|     •    The value for QNAMs for additional text (>200 characters) should contain a sequential variable name,
 21|          which is formed by appending a 1-digit integer, beginning with 1, to the original domain variable name.
 22|     •    The value for QLABEL should be the original domain variable label.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1410` (来源: live valid_hits):

~~~~
1410| - The value for QNAMs for additional text (>200 characters) should contain a sequential variable name, which is formed by appending a 1-digit integer, beginning with 1, to the original domain variable name.
~~~~

### Q173. `ig34_p0055_a017` — q9:Q9_IG34_EQUIV

- PDF 页 55 · 原子类型 LIST_ITEM · 所在节 `§4.5.3.2 [Text Strings Greater than 200 Characters in Other Variables]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In cases where the standard domain variable name is already 8 characters in length, sponsors should replace the last character with a digit when creating values for QNAM. As an example, for Other Action Taken in Adverse Events (AEACNOTH), values for QNAM for the SUPPAE records would have the values AEACNOT1, AEACNOT2, and so on.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0055.txt` 第 30-33 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 29|               they represent multiple values for a single variable.
 30|          o    In cases where the standard domain variable name is already 8 characters in length, sponsors should
 31|               replace the last character with a digit when creating values for QNAM. As an example, for Other
 32|               Action Taken in Adverse Events (AEACNOTH), values for QNAM for the SUPPAE records would
 33|               have the values AEACNOT1, AEACNOT2, and so on.
 34| Example 1
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1414` (来源: live valid_hits):

~~~~
1414|   - In cases where the standard domain variable name is already 8 characters in length, sponsors should replace the last character with a digit when creating values for QNAM. As an example, for Other Action Taken in Adverse Events (AEACNOTH), values for QNAM for the SUPPAE records would have the values AEACNOT1, AEACNOT2, and so on.
~~~~

### Q174. `ig34_p0065_a021` — q9:Q9_IG34_EQUIV

- PDF 页 65 · 原子类型 LIST_ITEM · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
b. Multistage assignment to treatment: Some trials use a multistage process for assigning a subject to an arm (see Section 7.2.1, Trial Arms, Example Trial 3).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0065.txt` 第 33-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32|                  populated with a description of the unplanned treatment received.
 33|         b.   Multistage assignment to treatment: Some trials use a multistage process for assigning a subject to an
 34|              arm (see Section 7.2.1, Trial Arms, Example Trial 3). In such a case, best practice is to create ARMCD
 35|              values composed of codes representing the results of the multiple stages of the treatment assignment
~~~~

KB 现文: `knowledge_base/domains/DM/assumptions.md:25` (来源: live valid_hits):

~~~~
  25|    b. Multistage assignment to treatment: Some trials use a multistage process for assigning a subject to an arm (see Section 7.2.1, Trial Arms, Example Trial 3). In such a case, best practice is to create ARMCD values composed of codes representing the results of the multiple stages of the treatment assignment process. If a subject is partially assigned, then truncated codes representing the stages completed can be used in ARMCD, and similar truncated codes can be used in ACTARMCD. The descriptions used to populate ARM and ACTARM should be similarly truncated, and the one-to-one relationship between these truncated codes should be maintained for all affected subjects in the trial. Example 3 below provides an example of this situation; see also Section 5.3, Subject Elements, Example 2. Note that this use of values not in the TA dataset is allowable only for trials with multistage assignment to arms and to subjects in those trials who do not complete all stages of the assignment.
~~~~

### Q175. `ig34_p0071_a016` — q9:Q9_IG34_EQUIV

- PDF 页 71 · 原子类型 LIST_ITEM · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
AFRICAN
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0071.txt` 第 6-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5| 
  6| If the study participant answered: BLACK OR AFRICAN AMERICAN
  7| 
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:11,120,136` (来源: live valid_hits):

~~~~
  11| | 3 | ABC123 | DM | ABC12301003 | 01003 | 2006-01-16 | 2006-03-19 | 2006-01-16 | 2006-03-19 | 2006-01-02 | 2006-03-19 | 01 | JOHNSON, M | 1938-01-19 | 68 | YEARS | F | BLACK OR AFRICAN AMERICAN | NOT HISPANIC OR LATINO | P | Placebo | P | Placebo | | | USA |
 120|     R3["☐ BLACK OR AFRICAN AMERICAN"]
 136|     SC3["Subcategories CRACE11-17 → SUPPDM.QVAL<br/>☐ AFRICAN  ☐ AFRICAN AMERICAN<br/>☐ AFRICAN CARIBBEAN  ☐ BAHAMIAN<br/>☐ BARBADIAN  ☐ BLACK<br/>☐ BLACK CENTRAL AMERICAN"]
~~~~

### Q176. `ig34_p0218_a018` — q9:Q9_IG34_EQUIV

- PDF 页 218 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 7-8:	Show values for background (i.e. non-specific) binding of the labeled detection antibody to the CDxx-expressing cells of interest by using an isotype control belonging to the same immunoglobulin class/subclass as the therapeutic antibody. This is indicated in CPBDAGNT and is also shown for how the sponsor chose to represent it in CPMRKSTR.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0218.txt` 第 29-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28|                      CDxx available to be occupied by the therapeutic antibody,
 29| Rows 7-8:            Show values for background (i.e. non-specific) binding of the labeled detection antibody to the CDxx-expressing cells of interest by using an isotype control belonging to the same immunoglobulin
 30|                      class/subclass as the therapeutic antibody. This is indicated in CPBDAGNT and is also shown for how the sponsor chose to represent it in CPMRKSTR.
 31| Rows 9-11: Rows 9 and 10 show values for specific binding of the therapeutic antibody (CDxx antibody) in the unaltered (native) specimen (Row 9) and the specimen to which excess CDxx antibody was added
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:273` (来源: live valid_hits):

~~~~
 273| **Rows 7-8:** Show values for background (i.e. non-specific) binding of the labeled detection antibody to the CDxx-expressing cells of interest by using an isotype control belonging to the same immunoglobulin class/subclass as the therapeutic antibody. This is indicated in CPBDAGNT and is also shown for how the sponsor chose to represent it in CPMRKSTR.
~~~~

### Q177. `ig34_p0224_a018` — q9:Q9_IG34_EQUIV

- PDF 页 224 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 5: Shows the percent variant read depth to total read depth.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0224.txt` 第 29-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| Row 4:         Shows the number of times the locus specified in variables GFCHROM and GFGENLOC was observed.
 29| Row 5:         Shows the percent variant read depth to total read depth.
 30| Row 6:         Shows the number of copies of the gene of interest within the genome of the tumor cell.
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:15` (来源: live valid_hits):

~~~~
  15| **Row 5:** Shows the percent variant read depth to total read depth.
~~~~

### Q178. `ig34_p0283_a009` — q9:Q9_IG34_EQUIV

- PDF 页 283 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 4`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 24-35:	The relationship with RELID "3" includes PC records with PCSEQ values "1" through "10" and PP records with PPSEQ = "3".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0283.txt` 第 12-13 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11| Rows 13-24: The relationship with RELID "2" includes PC records with PCSEQ values "1" through "5" and "7"
 12|             through "12" and PP records with PPSEQ = "2".
 13| Rows 24-35: The relationship with RELID "3" includes PC records with PCSEQ values "1" through "10" and PP
 14|             records with PPSEQ = "3".
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### Q179. `ig34_p0284_a014` — q9:Q9_IG34_EQUIV

- PDF 页 284 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Do any parameters use the same concentrations, but not as consistently as shown in Examples 1 and 2? If so, refer to Example 3. Assign a GRPID value to the PP records that use the same concentrations. More than 1 PPGRPID value may be necessary. Assign as many PCGRPID values in the PC domain as needed to group these records. Create records in RELREC for each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0284.txt` 第 38-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37|             ones that were used and a PCGRPID value for those that were not used. Create records in RELREC for
 38|             each PCGRPID value and each PPGRPID value (method A). Use RELID to show which PCGRPID and
 39|             PPGRPID records are related. Consider RELREC methods B, C, and D as applicable.
 40|       3.    Do any parameters use the same concentrations, but not as consistently as shown in Examples 1 and 2? If
 41|             so, refer to Example 3. Assign a GRPID value to the PP records that use the same concentrations. More
 42|             than 1 PPGRPID value may be necessary. Assign as many PCGRPID values in the PC domain as needed to
 43|             group these records. Create records in RELREC for each PCGRPID value and each PPGRPID value
 44|             (method A). Use RELID to show which PCGRPID and PPGRPID records are related. Consider RELREC
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

