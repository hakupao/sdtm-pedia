# T4.1 第二轮补检包 3 — TYPO_SIB (25 条; 编号 R28-R52)

> 由 `scripts/t4/t4_round2_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 R).

### R28. `ig34_p0043_a010` — r2:TYPO_SIB

- PDF 页 43 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-CH4 T-8`: PDF 写 ""ONGOING"', (多撇号)" → KB 写 ""ONGOING"," (处理: KB 写正确值; 依据: 同句其余三项格式; KB `knowledge_base/chapters/ch04_general_assumptions.md:932`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The variables --STRF and --ENRF represent the timing of an observation relative to the sponsor-defined study reference period, when information such as "BEFORE", "PRIOR", "ONGOING", or "CONTINUING" is collected in lieu of a date and this collected information is in relation to the sponsor-defined study reference period.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0043.txt` 第 12-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11| --STRF and --ENRF
 12| The variables --STRF and --ENRF represent the timing of an observation relative to the sponsor-defined study
 13| reference period, when information such as "BEFORE", "PRIOR", "ONGOING"', or "CONTINUING" is collected
 14| in lieu of a date and this collected information is in relation to the sponsor-defined study reference period. The
 15| sponsor-defined study reference period is the continuous period of time defined by the discrete starting point,
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:932` (来源: live valid_hits):

~~~~
 932| The variables --STRF and --ENRF represent the timing of an observation relative to the sponsor-defined study reference period, when information such as "BEFORE", "PRIOR", "ONGOING", or "CONTINUING" is collected in lieu of a date and this collected information is in relation to the sponsor-defined study reference period. The sponsor-defined study reference period is the continuous period of time defined by the discrete starting point, RFSTDTC, and the discrete ending point, RFENDTC, for each subject in the Demographics (DM) dataset.
~~~~

### R29. `ig34_p0043_a022` — r2:TYPO_SIB

- PDF 页 43 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-ch04`
- 登记 `S-CH4 T-10e`: PDF 写 "CMSTRF.Some" → KB 写 "正常空格" (处理: KB 写正确值; 依据: 纯排版空格, KB 保留正确写法; KB `knowledge_base/chapters/ch04_general_assumptions.md:947`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Note also that the information collected is relative to the study reference period, which meets the definition of CMSTRF.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0043.txt` 第 31-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 30| respect to the start of the concomitant medication use only, and therefore the collected data corresponds to variable
 31| CMSTRF, not CMENRF. Note also that the information collected is relative to the study reference period, which
 32| meets the definition of CMSTRF.Some sponsors may wish to derive --STRF and --ENRF for analysis or reporting
 33| purposes even when dates are collected. Sponsors are cautioned that doing so in conjunction with directly collecting
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:947` (来源: decision.evidence.hit):

~~~~
 947| Although "COINCIDENT" and "ONGOING" are in the STENRF codelist, they describe timing relative to a point in time rather than an interval of time, so are not appropriate for use with --ENRF variables. As an example, a CRF checkbox that identifies concomitant medication use that began prior to the study reference period would translate into CMSTRF = "BEFORE", if selected. Note that in this example, the information collected is with respect to the start of the concomitant medication use only, and therefore the collected data corresponds to variable CMSTRF, not CMENRF. Note also that the information collected is relative to the study reference period, which meets the definition of CMSTRF.
~~~~

### R30. `ig34_p0047_a008` — r2:TYPO_SIB

- PDF 页 47 · 原子类型 LIST_ITEM · 所在节 `§4.4.10 [Representing Time Points]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-CH4 T-9`: PDF 写 "(–TPTREF (en dash)" → KB 写 "(--TPTREF" (处理: KB 写正确值; 依据: 同句 --ELTM 双连字符; KB `knowledge_base/chapters/ch04_general_assumptions.md:1121`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A trial may have only 1 reference time point per visit, and all reference time points may be similar, so that only 1 value of --TPTREF (e.g., "DOSE") is needed. (--TPTREF would be populated, but would not contribute to uniqueness.)
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0047.txt` 第 12-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11|          time point variables would be populated.)
 12|     •    A trial may have only 1 reference time point per visit, and all reference time points may be similar, so that
 13|          only 1 value of --TPTREF (e.g., "DOSE") is needed. (--TPTREF would be populated, but would not
 14|          contribute to uniqueness.)
 15|     •    A trial may have time points not related to a reference time point. For instance, --TPTNUM values could be
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1121` (来源: live valid_hits):

~~~~
1121| - A trial may have only 1 reference time point per visit, and all reference time points may be similar, so that only 1 value of --TPTREF (e.g., "DOSE") is needed. (--TPTREF would be populated, but would not contribute to uniqueness.)
~~~~

### R31. `ig34_p0047_a009` — r2:TYPO_SIB

- PDF 页 47 · 原子类型 LIST_ITEM · 所在节 `§4.4.10 [Representing Time Points]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-CH4 T-9`: PDF 写 "(–TPTREF (en dash)" → KB 写 "(--TPTREF" (处理: KB 写正确值; 依据: 同句 --ELTM 双连字符; KB `knowledge_base/chapters/ch04_general_assumptions.md:1121`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
A trial may have time points not related to a reference time point. For instance, --TPTNUM values could be used to distinguish first, second, and third repeats of a measurement scheduled without any relationship to dosing (--TPTREF and --ELTM would not be included.) In this case, where the protocol calls for repeated measurements but does not specify timing of the measurements, the --REPNUM variable could be used instead of time-point variables.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0047.txt` 第 15-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|          contribute to uniqueness.)
 15|     •    A trial may have time points not related to a reference time point. For instance, --TPTNUM values could be
 16|          used to distinguish first, second, and third repeats of a measurement scheduled without any relationship to
 17|          dosing (–TPTREF and --ELTM would not be included.) In this case, where the protocol calls for repeated
 18|          measurements but does not specify timing of the measurements, the --REPNUM variable could be used
 19|          instead of time-point variables.
 20| For trials with many time points, the requirement to provide uniqueness using only VISITNUM, --TPTREF, and --
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1122` (来源: live valid_hits):

~~~~
1122| - A trial may have time points not related to a reference time point. For instance, --TPTNUM values could be used to distinguish first, second, and third repeats of a measurement scheduled without any relationship to dosing (--TPTREF and --ELTM would not be included.) In this case, where the protocol calls for repeated measurements but does not specify timing of the measurements, the --REPNUM variable could be used instead of time-point variables.
~~~~

### R32. `ig34_p0064_a012` — r2:TYPO_SIB

- PDF 页 64 · 原子类型 NOTE · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **REAL_GAP** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `S-SPEC1`
- 登记 `S-SPEC1 T-3`: PDF 写 "脚注² URL 后孤立 )" → KB 写 "删 )" (处理: KB 写正确值; 依据: 脚注全文无对应开括号 (改判); KB `knowledge_base/domains/DM/spec.md:296`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2Food and Drug Administration. Collection of Race and Ethnicity Data in Clinical Trials. US Department of Health and Human Services;2016. Accessed January 8, 2020. https://www.fda.gov/downloads/regulatoryinformation/guidances/ucm126396.pdf
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0064.txt` 第 40-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39|  In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.
 40| 2Food and Drug Administration. Collection of Race and Ethnicity Data in Clinical Trials. US Department of Health and Human Services;2016. Accessed January 8,
 41| 
 42| 2020. https://www.fda.gov/downloads/regulatoryinformation/guidances/ucm126396.pdf)
 43| 
~~~~

KB 现文: `knowledge_base/domains/DM/spec.md:296` (来源: decision.evidence.hit):

~~~~
 296| > ²Food and Drug Administration. Collection of Race and Ethnicity Data in Clinical Trials. US Department of Health and Human Services;2016. Accessed January 8, 2020. https://www.fda.gov/downloads/regulatoryinformation/guidances/ucm126396.pdf
~~~~

### R33. `ig34_p0069_a008` — r2:TYPO_SIB

- PDF 页 69 · 原子类型 SENTENCE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-DM T-3`: PDF 写 "Ex3 Row 1 叙述 ACTRMCD" → KB 写 "ACTARMCD" (处理: KB 写正确值; 依据: 同页表头/Row 3 叙述/spec; KB `knowledge_base/domains/DM/examples.md:68`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This case illustrates the exception to the rule that ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 26-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25|                epoch, so never reached the open label epoch, when they would have been assigned to either the open
 26|                drug A or the rescue element. Their ARMCD is "A". This case illustrates the exception to the rule that
 27|                ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.
 28| Row 3:         Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:70` (来源: live valid_hits):

~~~~
  70| **Row 2:** Subject 002 was randomized to drug A. They were lost to follow-up during the double-blind treatment epoch, so never reached the open label epoch, when they would have been assigned to either the open drug A or the rescue element. Their ARMCD is "A". This case illustrates the exception to the rule that ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.
~~~~

### R34. `ig34_p0069_a011` — r2:TYPO_SIB

- PDF 页 69 · 原子类型 SENTENCE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-DM T-3`: PDF 写 "Ex3 Row 1 叙述 ACTRMCD" → KB 写 "ACTARMCD" (处理: KB 写正确值; 依据: 同页表头/Row 3 叙述/spec; KB `knowledge_base/domains/DM/examples.md:68`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ARMCD shows the result of their assignment, "AR"; ACTARMCD shows their actual treatment, "BR".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 29-30 行 (自动定位, 词覆盖 0.917; 版式以原 PDF 为准):

~~~~
 28| Row 3:         Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind
 29|                treatment epoch, they were assigned to rescue treatment. ARMCD shows the result of their
 30|                assignments, "AR"; ACTARMCD shows their actual treatment, "BR".
 31| dm.xpt
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:72-72` (来源: fuzzy locate (score 0.917)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  72| **Row 3:** Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind treatment epoch, they were assigned to rescue treatment. ARMCD shows the result of their assignments, "AR"; ACTARMCD shows their actual treatment, "BR".
~~~~

### R35. `ig34_p0078_a022` — r2:TYPO_SIB

- PDF 页 78 · 原子类型 TABLE_ROW · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-DM T-1`: PDF 写 "Ex7 dm Row 列重复 3" → KB 写 "4" (处理: KB 写正确值; 依据: 同表连续编号 + 叙述 Row 4; KB `knowledge_base/domains/DM/examples.md:440`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
4 | ABC789 | DM | ABC789-010-048 | 010-048 | 33 | YEARS | M | UNKNOWN | HISPANIC OR LATINO
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0078.txt` 第 18-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| Row 3:         Subject did not self-identify to 1 of the existing race options and selected "Other". RACE was populated with "OTHER" in this case.
 18| Row 4:         Subject could not self-identify to any of the race options including identification of an "Other". RACE was populated with "UNKNOWN" in this
 19|                case.
 20| Note: Not all DM variables are shown.
 21| dm.xpt
 22| Row      STUDYID    DOMAIN     USUBJID             SUBJID    AGE    AGEU       SEX    RACE          ETHNIC
 23| 1        ABC789     DM         ABC789-010-045      010-045   20     YEARS      M      WHITE         HISPANIC OR LATINO
 24| 2        ABC789     DM         ABC789-010-046      010-046   21     YEARS      F      ASIAN         NOT HISPANIC OR LATINO
 25| 3        ABC789     DM         ABC789-010-047      010-047   24     YEARS      F      OTHER         HISPANIC OR LATINO
 26| 3        ABC789     DM         ABC789-010-048      010-048   33     YEARS      M      UNKNOWN       HISPANIC OR LATINO
 27| 
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:440` (来源: live valid_hits):

~~~~
 440| | 4 | ABC789 | DM | ABC789-010-048 | 010-048 | 33 | YEARS | M | UNKNOWN | HISPANIC OR LATINO |
~~~~

### R36. `ig34_p0085_a009` — r2:TYPO_SIB

- PDF 页 85 · 原子类型 SENTENCE · 所在节 `§5.4 [Subject Disease Milestones (SM)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-SM T-3`: PDF 写 "hyypoglycemic" → KB 写 "hypoglycemic" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/SM/examples.md:22`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this study, the disease milestones of interest were initial diagnosis and hypoglycemic events, as shown in Section 7.3.3, Trial Disease Milestones, Example 1.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0085.txt` 第 13-13 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12| Example 1
 13| In this study, the disease milestones of interest were initial diagnosis and hypoglycemic events, as shown in Section 7.3.3, Trial Disease Milestones, Example 1.
 14| Row 1:          Shows that subject 001's initial diagnosis of diabetes occurred in October 2005. Because this is a partial date, SMDY is not populated. No end
~~~~

KB 现文: `knowledge_base/domains/SM/examples.md:5` (来源: live valid_hits):

~~~~
   5| In this study, the disease milestones of interest were initial diagnosis and hypoglycemic events, as shown in Section 7.3.3, Trial Disease Milestones, Example 1.
~~~~

### R37. `ig34_p0085_a011` — r2:TYPO_SIB

- PDF 页 85 · 原子类型 SENTENCE · 所在节 `§5.4 [Subject Disease Milestones (SM)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-SM T-3`: PDF 写 "hyypoglycemic" → KB 写 "hypoglycemic" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/SM/examples.md:22`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 2-3: Show that subject 001 had 2 hypoglycemic events. In this case, only start date/times have been collected. Because these date/times include full dates, SMSTDY has been populated in each case.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0085.txt` 第 16-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15|                 date/time was recorded for this milestone.
 16| Rows 2-3:       Show that subject 001 had 2 hypoglycemic events. In this case, only start date/times have been collected. Because these date/times include full
 17|                 dates, SMSTDY has been populated in each case.
 18| Row 4:          Shows that subject 002’s initial diagnosis of diabetes occurred on May 15, 2010. Because a full date was collected, the study day of this milestone
~~~~

KB 现文: `knowledge_base/domains/SM/examples.md:9` (来源: live valid_hits):

~~~~
   9| **Rows 2-3:** Show that subject 001 had 2 hypoglycemic events. In this case, only start date/times have been collected. Because these date/times include full dates, SMSTDY has been populated in each case.
~~~~

### R38. `ig34_p0085_a012` — r2:TYPO_SIB

- PDF 页 85 · 原子类型 SENTENCE · 所在节 `§5.4 [Subject Disease Milestones (SM)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-SM T-3`: PDF 写 "hyypoglycemic" → KB 写 "hypoglycemic" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/SM/examples.md:22`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 4: Shows that subject 002's initial diagnosis of diabetes occurred on May 15, 2010. Because a full date was collected, the study day of this milestone was populated. Diagnosis was pre-study, so the study day of the disease milestone is negative. No hypoglycemic events were recorded for this subject.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0085.txt` 第 18-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17|                 dates, SMSTDY has been populated in each case.
 18| Row 4:          Shows that subject 002’s initial diagnosis of diabetes occurred on May 15, 2010. Because a full date was collected, the study day of this milestone
 19|                 was populated. Diagnosis was pre-study, so the study day of the disease milestone is negative. No hypoglycemic events were recorded for this
 20|                 subject.
~~~~

KB 现文: `knowledge_base/domains/SM/examples.md:11` (来源: live valid_hits):

~~~~
  11| **Row 4:** Shows that subject 002’s initial diagnosis of diabetes occurred on May 15, 2010. Because a full date was collected, the study day of this milestone was populated. Diagnosis was pre-study, so the study day of the disease milestone is negative. No hypoglycemic events were recorded for this subject.
~~~~

### R39. `ig34_p0113_a008` — r2:TYPO_SIB

- PDF 页 113 · 原子类型 LIST_ITEM · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-EX T-3`: PDF 写 "from ottles A, B and C" → KB 写 "bottles" (处理: KB 写正确值; 依据: 同列表其他项 bottles; KB `knowledge_base/domains/EX/examples.md:118`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
1 tablet from bottles A, B and C from 2011-01-14 to 2011-01-20
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0113.txt` 第 10-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9| from bottles A, B, and C taken together once daily. The subject in this example took:
 10|       •     1 tablet from bottles A, B and C from 2011-01-14 to 2011-01-20
 11|       •     0 tablets from bottle B on 2011-01-21, then 2 tablets on 2011-01-22
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:115` (来源: live valid_hits):

~~~~
 115| - 1 tablet from bottles A, B and C from 2011-01-14 to 2011-01-20
~~~~

### R40. `ig34_p0114_a003` — r2:TYPO_SIB

- PDF 页 114 · 原子类型 SENTENCE · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-EX T-4`: PDF 写 "protocol specified unit" → KB 写 "protocol-specified unit" (处理: KB 写正确值; 依据: 本节 p111/113/114/118 均 protocol-specified; KB `knowledge_base/domains/EX/examples.md:207`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The EX dataset shows administrations collected in the protocol-specified unit, mg. No EC dataset was needed because the open-label administrations were collected in the protocol-specified unit; EC would be an exact duplicate of the entire EX domain.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0114.txt` 第 4-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| Dose adjustments were allowed as needed in response to tolerability or efficacy issues.
  4| The EX dataset shows administrations collected in the protocol-specified unit, mg. No EC dataset was needed because the open-label administrations were
  5| collected in the protocol-specified unit; EC would be an exact duplicate of the entire EX domain.
  6| ex.xpt
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:154` (来源: live valid_hits):

~~~~
 154| The EX dataset shows administrations collected in the protocol-specified unit, mg. No EC dataset was needed because the open-label administrations were collected in the protocol-specified unit; EC would be an exact duplicate of the entire EX domain.
~~~~

### R41. `ig34_p0119_a017` — r2:TYPO_SIB

- PDF 页 119 · 原子类型 TABLE_ROW · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-EX T-1`: PDF 写 "Ex7 relrec Row 1,2,6,3,4,6" → KB 写 "1-6 连续" (处理: KB 写正确值; 依据: 同表连续编号 + 叙述 Rows 1-3/4-6; KB `knowledge_base/domains/EX/examples.md:413`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 6 | ABC123 | VS | | VSLNKID | | ONE | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0119.txt` 第 21-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20| 2        ABC123    EX              EXLNKID           ONE                1
 21| 6        ABC123    VS              VSLNKID           ONE                1
 22| 3        ABC123    EC              ECLNKGRP          MANY               2
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:413-416` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 413| | 3 | ABC123 | VS | | VSLNKID | | ONE | 1 |
 414| | 4 | ABC123 | EC | | ECLNKGRP | | MANY | 2 |
 415| | 5 | ABC123 | EX | | EXLNKGRP | | ONE | 2 |
 416| | 6 | ABC123 | VS | | VSLNKGRP | | ONE | 2 |
~~~~

### R42. `ig34_p0124_a023` — r2:TYPO_SIB

- PDF 页 124 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **PRESENT** · 终态 **EXACT** (T3 前 MISPLACED) · 判定规则 `live-hit` · 批 `T1:pack_030`
- 登记 `B-ML T-1`: PDF 写 "Ex2 r2 MLTRT WHTE MILK" → KB 写 "WHITE MILK" (处理: KB 写正确值; 依据: 同表 r8 / 叙述 white milk; KB `knowledge_base/domains/ML/examples.md:66`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
8 | ABC123 | ML | ABC123-001 | 8 | WHITE MILK | 3 | WEEK 3 | 2015-09-22
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0124.txt` 第 41-41 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 40| 7        ABC123         ML       ABC123-001     7          APPLE                                3            WEEK 3     2015-09-22
 41| 8        ABC123         ML       ABC123-001     8          WHITE MILK                           3            WEEK 3     2015-09-22
 42| 9        ABC123         ML       ABC123-001     9          SALAD                                3            WEEK 3     2015-09-22
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:72` (来源: decision.evidence.hit):

~~~~
  72| | 8 | ABC123 | ML | ABC123-001 | 8 | WHITE MILK | 3 | WEEK 3 | 2015-09-22 |
~~~~

### R43. `ig34_p0142_a022` — r2:TYPO_SIB

- PDF 页 142 · 原子类型 TABLE_HEADER · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-AE T-4`: PDF 写 "Ex5 表头首格空白" → KB 写 "Row" (处理: KB 写正确值; 依据: 同文件其他表首格均为 Row; 列下为行号; KB `knowledge_base/domains/AE/examples.md:79`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | AESEQ | AETERM | AEDECOD | AESER | AESEV | AEACNDEV | AERLDEV | AEOUT | AESCONG | AESHOSP | AESDISAB | AESDTH | AESLIFE | AESMIE | AESINTV | AESTDTC | AEENDTC | AESTDY | AEENDY |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0142.txt` 第 40-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39| ae.xpt
 40| Row STUDYID DOMAIN USUBJID SPDEVID AESEQ                         AESPID       AETERM         AEDECOD  AESER AESEV            AEACNDEV                  AERLDEV  AEOUT                 AESCONG AESHOSP AESDISAB AESDTH AESLIFE AESMIE AESINTV AESTDTC                            AEENDTC      AESTDY AEENDY
 41| 1   T001    AE     002     Sensor123 1                           AE0007       Skin           ERYTHEMA N     MILD             SENSOR                    CAUSAL   RECOVERED/            N       N       N        N      N       N      N       2018-09-                           2018-09-     27     33
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:79-79` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  79| | Row | STUDYID | DOMAIN | USUBJID | SPDEVID | AESEQ | AESPID | AETERM | AEDECOD | AELOC | AELAT | AESER | AESEV | AEACNDEV | AERLDEV | AEOUT | AESCONG | AESHOSP | AESDISAB | AESDTH | AESLIFE | AESMIE | AESINTV | AEUNANT | AERLPRC | AERLPRT | AESTDTC | AEENDTC | AESTDY | AEENDY |
~~~~

### R44. `ig34_p0147_a013` — r2:TYPO_SIB

- PDF 页 147 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-BE T-3`: PDF 写 "Ex2 bs r3-4 BSREFID 298B1-1R0" → KB 写 "298R1-1R0" (处理: KB 写正确值; 依据: be r4 BEREFID、suppbe、relspec REFID/PARENT 均 298R1-1R0; KB `knowledge_base/domains/BE/examples.md:124`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R0 | BESPEC | Specimen Type | RNA | Collected | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0147.txt` 第 15-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| 2        3441271   BE          MU-298      BEREFID    298B1-1       BESPEC     Specimen Type     PLASMA   CRF
 15| 3        3441271   BE          MU-298      BEREFID    298R1-1R0     BESPEC     Specimen Type     RNA      Collected
 16| 4        3441271   BE          MU-298      BEREFID    298R1-1R1     BESPEC     Specimen Type     RNA      Collected
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:105` (来源: live valid_hits):

~~~~
 105| | 3 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R0 | BESPEC | Specimen Type | RNA | Collected | |
~~~~

### R45. `ig34_p0147_a026` — r2:TYPO_SIB

- PDF 页 147 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-BE T-3`: PDF 写 "Ex2 bs r3-4 BSREFID 298B1-1R0" → KB 写 "298R1-1R0" (处理: KB 写正确值; 依据: be r4 BEREFID、suppbe、relspec REFID/PARENT 均 298R1-1R0; KB `knowledge_base/domains/BE/examples.md:124`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | 3441271 | BS | MU-298 | 4 | 298R1-1R0 | RIN | RNA Integrity Number | QUALITY CONTROL | 9.3 | | 9.3 | 9.3 | | RNA | 2 | 2010-04-01T11:50 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0147.txt` 第 31-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 30| 3        3441271   BS        MU-298       3        298B1-1R0     VOLUME       Volume                 SPECIMEN MEASUREMENT         6         mL            6               6           mL            RNA          2          2010-04-01T11:50
 31| 4        3441271   BS        MU-298       4        298B1-1R0     RIN          RNA Integrity Number   QUALITY CONTROL              9.3                     9.3             9.3                       RNA          2          2010-04-01T11:50
 32| 5        3441271   BS        MU-298       5        298R1-1R1     VOLUME       Volume                 SPECIMEN MEASUREMENT         2         mL            2               2           mL            RNA          2          2010-04-01T11:50
 33| 6        3441271   BS        MU-298       6        298R1-1R2     VOLUME       Volume                 SPECIMEN MEASUREMENT         2         mL            2               2           mL            RNA          2          2010-04-01T11:50
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:125` (来源: live valid_hits):

~~~~
 125| | 4 | 3441271 | BS | MU-298 | 4 | 298R1-1R0 | RIN | RNA Integrity Number | QUALITY CONTROL | 9.3 | | 9.3 | 9.3 | | RNA | 2 | 2010-04-01T11:50 |
~~~~

### R46. `ig34_p0147_a036` — r2:TYPO_SIB

- PDF 页 147 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-BE T-3`: PDF 写 "Ex2 bs r3-4 BSREFID 298B1-1R0" → KB 写 "298R1-1R0" (处理: KB 写正确值; 依据: be r4 BEREFID、suppbe、relspec REFID/PARENT 均 298R1-1R0; KB `knowledge_base/domains/BE/examples.md:124`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | 3441271 | MU-298 | 298R1-1R0 | RNA | 298B1-1 | 3 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0147.txt` 第 42-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 41| 2        3441271   MU-298    298B1-1      PLASMA     298B1        2
 42| 3        3441271   MU-298    298R1-1R0    RNA        298B1-1      3
 43| 4        3441271   MU-298    298R1-1R1    RNA        298R1-1R0    4
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:140` (来源: live valid_hits):

~~~~
 140| | 3 | 3441271 | MU-298 | 298R1-1R0 | RNA | 298B1-1 | 3 |
~~~~

### R47. `ig34_p0147_a037` — r2:TYPO_SIB

- PDF 页 147 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-BE T-3`: PDF 写 "Ex2 bs r3-4 BSREFID 298B1-1R0" → KB 写 "298R1-1R0" (处理: KB 写正确值; 依据: be r4 BEREFID、suppbe、relspec REFID/PARENT 均 298R1-1R0; KB `knowledge_base/domains/BE/examples.md:124`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | 3441271 | MU-298 | 298R1-1R1 | RNA | 298R1-1R0 | 4 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0147.txt` 第 43-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 42| 3        3441271   MU-298    298R1-1R0    RNA        298B1-1      3
 43| 4        3441271   MU-298    298R1-1R1    RNA        298R1-1R0    4
 44| 5        3441271   MU-298    298R1-1R2    RNA        298R1-1R0    4
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:141` (来源: live valid_hits):

~~~~
 141| | 4 | 3441271 | MU-298 | 298R1-1R1 | RNA | 298R1-1R0 | 4 |
~~~~

### R48. `ig34_p0147_a038` — r2:TYPO_SIB

- PDF 页 147 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-BE T-3`: PDF 写 "Ex2 bs r3-4 BSREFID 298B1-1R0" → KB 写 "298R1-1R0" (处理: KB 写正确值; 依据: be r4 BEREFID、suppbe、relspec REFID/PARENT 均 298R1-1R0; KB `knowledge_base/domains/BE/examples.md:124`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 5 | 3441271 | MU-298 | 298R1-1R2 | RNA | 298R1-1R0 | 4 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0147.txt` 第 44-44 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 43| 4        3441271   MU-298    298R1-1R1    RNA        298R1-1R0    4
 44| 5        3441271   MU-298    298R1-1R2    RNA        298R1-1R0    4
 45| 6        3441271   MU-298    298R1-1R3    RNA        298R1-1R0    4
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:142` (来源: live valid_hits):

~~~~
 142| | 5 | 3441271 | MU-298 | 298R1-1R2 | RNA | 298R1-1R0 | 4 |
~~~~

### R49. `ig34_p0147_a039` — r2:TYPO_SIB

- PDF 页 147 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-BE T-3`: PDF 写 "Ex2 bs r3-4 BSREFID 298B1-1R0" → KB 写 "298R1-1R0" (处理: KB 写正确值; 依据: be r4 BEREFID、suppbe、relspec REFID/PARENT 均 298R1-1R0; KB `knowledge_base/domains/BE/examples.md:124`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 6 | 3441271 | MU-298 | 298R1-1R3 | RNA | 298R1-1R0 | 4 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0147.txt` 第 45-45 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 44| 5        3441271   MU-298    298R1-1R2    RNA        298R1-1R0    4
 45| 6        3441271   MU-298    298R1-1R3    RNA        298R1-1R0    4
 46| 
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:143` (来源: live valid_hits):

~~~~
 143| | 6 | 3441271 | MU-298 | 298R1-1R3 | RNA | 298R1-1R0 | 4 |
~~~~

### R50. `ig34_p0170_a0007` — r2:TYPO_SIB

- PDF 页 170 · 原子类型 TABLE_ROW · 所在节 `§6.2.5 Healthcare Encounters (HO)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-HO T-1`: PDF 写 "REHABILIATION FACILITY" → KB 写 "REHABILITATION FACILITY" (处理: KB 写正确值; 依据: Ex2 r3 / 叙述 / Assumption 1; KB `knowledge_base/domains/HO/examples.md:25`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | ABC | HO | ABC123101 | 3 | REHABILITATION FACILITY | | FOLLOW-UP CARE | 2011-06-12 | 2011-06-22 | | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0170.txt` 第 41-41 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 40| 2        ABC       HO        ABC123101   2       ICU                                  INITIAL HOSPITALIZATION   2011-06-08T11:00   2011-06-09T14:30
 41| 3        ABC       HO        ABC123101   3       REHABILITATION FACILITY              FOLLOW-UP CARE            2011-06-12         2011-06-22
 42| 4        ABC       HO        ABC123101   4       CARDIOLOGY UNIT                      FOLLOW-UP CARE            2011-06-25         2011-06-25
~~~~

KB 现文: `knowledge_base/domains/HO/examples.md:65` (来源: live valid_hits):

~~~~
  65| | 3 | ABC | HO | ABC123101 | 3 | REHABILITATION FACILITY | FOLLOW-UP CARE | 2011-06-12 | 2011-06-22 | | |
~~~~

### R51. `ig34_p0205_a006` — r2:TYPO_SIB

- PDF 页 205 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-SPC1 CP T-16b`: PDF 写 "asm 4 CPSCMRKS ×3" → KB 写 "CPCSMRKS" (处理: KB 写正确值; 依据: spec 变量 CPCSMRKS; KB `knowledge_base/domains/CP/assumptions.md:58`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5. The combination of values in CPTEST, CPSBMRKS, CPCELSTA, and CPCSMRKS are used to uniquely identify a test. When 1 or more of the variables CPSBMRKS, CPCELSTA, or CPCSMRKS are populated, the Test Name (CPTEST) must be populated with the test name variant containing the "Sub" suffix to indicate that the finding/result pertains to a subpopulation of the cell type named in CPTEST.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0205.txt` 第 15-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|         also be populated. Conversely, when CPSCMRKS is populated, CPCELSTA must be populated.
 15|    5.   The combination of values in CPTEST, CPSBMRKS, CPCELSTA, and CPCSMRKS are used to uniquely
 16|         identify a test. When 1 or more of the variables CPSBMRKS, CPCELSTA, or CPCSMRKS are populated,
 17|         the Test Name (CPTEST) must be populated with the test name variant containing the "Sub" suffix to
 18|         indicate that the finding/result pertains to a subpopulation of the cell type named in CPTEST.
 19|    6.   Populating the CPTEST and CPMRKSTR variables: The general structure of CPTEST depends on the use
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:60` (来源: live valid_hits):

~~~~
  60| 5. The combination of values in CPTEST, CPSBMRKS, CPCELSTA, and CPCSMRKS are used to uniquely identify a test. When 1 or more of the variables CPSBMRKS, CPCELSTA, or CPCSMRKS are populated, the Test Name (CPTEST) must be populated with the test name variant containing the "Sub" suffix to indicate that the finding/result pertains to a subpopulation of the cell type named in CPTEST.
~~~~

### R52. `ig34_p0205_a010` — r2:TYPO_SIB

- PDF 页 205 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-SPC1 CP T-16b`: PDF 写 "asm 4 CPSCMRKS ×3" → KB 写 "CPCSMRKS" (处理: KB 写正确值; 依据: spec 变量 CPCSMRKS; KB `knowledge_base/domains/CP/assumptions.md:58`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ii. It is expected that CPMRKSTR is populated, and that it contains the entire set of markers used to define the test, including those that are also present in CPSBMRKS and/or CPCSMRKS.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0205.txt` 第 26-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25|                  used to define the cell type.
 26|              ii. It is expected that CPMRKSTR is populated, and that it contains the entire set of markers used to
 27|                  define the test, including those that are also present in CPSBMRKS and/or CPCSMRKS.
 28|              iii. Marker strings follow, as closely as possible, formatting recommendations presented in
~~~~

KB 现文: `knowledge_base/domains/CP/assumptions.md:65` (来源: live valid_hits):

~~~~
  65|       ii. It is expected that CPMRKSTR is populated, and that it contains the entire set of markers used to define the test, including those that are also present in CPSBMRKS and/or CPCSMRKS.
~~~~

