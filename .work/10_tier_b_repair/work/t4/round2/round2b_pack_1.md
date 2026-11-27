# T4.1 第二轮补检包 b1 — TYPO_SIB2 (20 条; 编号 S1-S20)

> 由 `scripts/t4/t4_round2b_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号前缀 S.

### S1. `ig34_p0010_a020` — r2:TYPO_SIB2

- PDF 页 10 · 原子类型 SENTENCE · 所在节 `§1.5 [Known Issues]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-ch01 T-2`: PDF 写 "MANY → --LNKID (and not --LNKGRP)" → KB 写 "--LNKGRP (and not --LNKID)" (处理: KB 写正确值; 依据: 同段前句 + p31 §4 定义, 两名对调; KB `knowledge_base/chapters/ch01_introduction.md:109`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This is being evaluated for clarification in a future release of the SDTMIG and/or Model document.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010.txt` 第 33-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32| Although it is implicit in the general concept of a derived record that there is no collected result (--ORRES should
 33| be null), this is not an explicit requirement currently stated in published CDISC material. This is being evaluated for
 34| clarification in a future release of the SDTMIG and/or Model document.
 35| Use of --LNKID and --LNKGRP
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:105` (来源: live valid_hits):

~~~~
 105| Although it is implicit in the general concept of a derived record that there is no collected result (--ORRES should be null), this is not an explicit requirement currently stated in published CDISC material. This is being evaluated for clarification in a future release of the SDTMIG and/or Model document.
~~~~

### S2. `ig34_p0010_a022` — r2:TYPO_SIB2

- PDF 页 10 · 原子类型 SENTENCE · 所在节 `§1.5 [Known Issues]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-ch01 T-2`: PDF 写 "MANY → --LNKID (and not --LNKGRP)" → KB 写 "--LNKGRP (and not --LNKID)" (处理: KB 写正确值; 依据: 同段前句 + p31 §4 定义, 两名对调; KB `knowledge_base/chapters/ch01_introduction.md:109`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The definition of --LNKID says that it is "used to identify a record," and the definition of --LNKGRP says that it is "used to identify a group of records."
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010.txt` 第 36-37 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35| Use of --LNKID and --LNKGRP
 36| The definition of --LNKID says that it is "used to identify a record," and the definition of --LNKGRP says that it is
 37| "used to identify a group of records." This implies that when setting up a relationship in RELREC, a row where
 38| RELTYPE = ONE will have an IDVAR of --LNKID (and not --LNKGRP); a row where RELTYPE = MANY will
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:109` (来源: live valid_hits):

~~~~
 109| The definition of --LNKID says that it is "used to identify a record," and the definition of --LNKGRP says that it is "used to identify a group of records." This implies that when setting up a relationship in RELREC, a row where RELTYPE = ONE will have an IDVAR of --LNKID (and not --LNKGRP); a row where RELTYPE = MANY will have an IDVAR of --LNKGRP (and not --LNKID). The examples in this version of the SDTMIG have not been systematically reviewed to implement this distinction between --LNKID and --LNKGRP. This distinction between --LNKID and --LNKGRP, and the appropriateness of using other identification variables for linking, will be clarified in a future release of the SDTMIG and/or Model document, and at that time examples in the SDTMIG will be systematically reviewed and updated to reflect that clarification.
~~~~

### S3. `ig34_p0010_a024` — r2:TYPO_SIB2

- PDF 页 10 · 原子类型 SENTENCE · 所在节 `§1.5 [Known Issues]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-ch01 T-2`: PDF 写 "MANY → --LNKID (and not --LNKGRP)" → KB 写 "--LNKGRP (and not --LNKID)" (处理: KB 写正确值; 依据: 同段前句 + p31 §4 定义, 两名对调; KB `knowledge_base/chapters/ch01_introduction.md:109`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The examples in this version of the SDTMIG have not been systematically reviewed to implement this distinction between --LNKID and --LNKGRP.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0010.txt` 第 39-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38| RELTYPE = ONE will have an IDVAR of --LNKID (and not --LNKGRP); a row where RELTYPE = MANY will
 39| have an IDVAR of --LNKID (and not --LNKGRP). The examples in this version of the SDTMIG have not been
 40| systematically reviewed to implement this distinction between --LNKID and --LNKGRP. This distinction between -
 41| -LNKID and --LNKGRP, and the appropriateness of using other identification variables for linking, will be clarified
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:109` (来源: live valid_hits):

~~~~
 109| The definition of --LNKID says that it is "used to identify a record," and the definition of --LNKGRP says that it is "used to identify a group of records." This implies that when setting up a relationship in RELREC, a row where RELTYPE = ONE will have an IDVAR of --LNKID (and not --LNKGRP); a row where RELTYPE = MANY will have an IDVAR of --LNKGRP (and not --LNKID). The examples in this version of the SDTMIG have not been systematically reviewed to implement this distinction between --LNKID and --LNKGRP. This distinction between --LNKID and --LNKGRP, and the appropriateness of using other identification variables for linking, will be clarified in a future release of the SDTMIG and/or Model document, and at that time examples in the SDTMIG will be systematically reviewed and updated to reflect that clarification.
~~~~

### S4. `ig34_p0037_a002` — r2:TYPO_SIB2

- PDF 页 37 · 原子类型 SENTENCE · 所在节 `§4.3.2 Controlled Terminology Text Case`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-ch04 T-3`: PDF 写 "the case that appears the source" → KB 写 "appears in the source" (处理: KB 写正确值; 依据: 语法补全; KB `knowledge_base/chapters/ch04_general_assumptions.md:668`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Terms from controlled terminology should be in the case that appears the source codelist or code system (e.g., CDISC codelist or external code system such as MedDRA).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0037.txt` 第 2-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| 4.3.2 Controlled Terminology Text Case
  2| Terms from controlled terminology should be in the case that appears the source codelist or code system (e.g.,
  3| CDISC codelist or external code system such as MedDRA). See Section 4.2.4, Text Case in Submitted Data.
  4| 
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:668-668` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 668| Terms from controlled terminology should be in the case that appears in the source codelist or code system (e.g., CDISC codelist or external code system such as MedDRA). See Section 4.2.4, Text Case in Submitted Data.
~~~~

### S5. `ig34_p0043_a015` — r2:TYPO_SIB2

- PDF 页 43 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-CH4 T-10d`: PDF 写 "variables.As" → KB 写 "正常空格" (处理: KB 写正确值; 依据: 纯排版空格, KB 保留正确写法; KB `knowledge_base/chapters/ch04_general_assumptions.md:947`)
- 登记 `S-CH4 T-10e`: PDF 写 "CMSTRF.Some" → KB 写 "正常空格" (处理: KB 写正确值; 依据: 纯排版空格, KB 保留正确写法; KB `knowledge_base/chapters/ch04_general_assumptions.md:947`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Although "COINCIDENT" and "ONGOING" are in the STENRF codelist, they describe timing relative to a point in time rather than an interval of time, so are not appropriate for use with --STRF variables.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0043.txt` 第 20-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| Allowable values for --STRF are "BEFORE", "DURING", "DURING/AFTER", "AFTER", and "UNKNOWN".
 20| Although "COINCIDENT" and "ONGOING" are in the STENRF codelist, they describe timing relative to a point in
 21| time rather than an interval of time, so are not appropriate for use with --STRF variables. It would be unusual for an
 22| event or intervention to be recorded as starting "AFTER" the study reference period, but could be possible,
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:943` (来源: live valid_hits):

~~~~
 943| Allowable values for --STRF are "BEFORE", "DURING", "DURING/AFTER", "AFTER", and "UNKNOWN". Although "COINCIDENT" and "ONGOING" are in the STENRF codelist, they describe timing relative to a point in time rather than an interval of time, so are not appropriate for use with --STRF variables. It would be unusual for an event or intervention to be recorded as starting "AFTER" the study reference period, but could be possible, depending on how the study reference period is defined in a particular study.
~~~~

### S6. `ig34_p0043_a019` — r2:TYPO_SIB2

- PDF 页 43 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-CH4 T-10d`: PDF 写 "variables.As" → KB 写 "正常空格" (处理: KB 写正确值; 依据: 纯排版空格, KB 保留正确写法; KB `knowledge_base/chapters/ch04_general_assumptions.md:947`)
- 登记 `S-CH4 T-10e`: PDF 写 "CMSTRF.Some" → KB 写 "正常空格" (处理: KB 写正确值; 依据: 纯排版空格, KB 保留正确写法; KB `knowledge_base/chapters/ch04_general_assumptions.md:947`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Although "COINCIDENT" and "ONGOING" are in the STENRF codelist, they describe timing relative to a point in time rather than an interval of time, so are not appropriate for use with --ENRF variables.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0043.txt` 第 26-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| ENRF is used, then --ENRF = "AFTER" means that the event did not end before or during the study reference
 26| period. Although "COINCIDENT" and "ONGOING" are in the STENRF codelist, they describe timing relative to a
 27| point in time rather than an interval of time, so are not appropriate for use with --ENRF variables.As an example, a
 28| CRF checkbox that identifies concomitant medication use that began prior to the study reference period would
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:947` (来源: live valid_hits):

~~~~
 947| Although "COINCIDENT" and "ONGOING" are in the STENRF codelist, they describe timing relative to a point in time rather than an interval of time, so are not appropriate for use with --ENRF variables. As an example, a CRF checkbox that identifies concomitant medication use that began prior to the study reference period would translate into CMSTRF = "BEFORE", if selected. Note that in this example, the information collected is with respect to the start of the concomitant medication use only, and therefore the collected data corresponds to variable CMSTRF, not CMENRF. Note also that the information collected is relative to the study reference period, which meets the definition of CMSTRF.
~~~~

### S7. `ig34_p0044_a010` — r2:TYPO_SIB2

- PDF 页 44 · 原子类型 SENTENCE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-CH4 T-10d`: PDF 写 "variables.As" → KB 写 "正常空格" (处理: KB 写正确值; 依据: 纯排版空格, KB 保留正确写法; KB `knowledge_base/chapters/ch04_general_assumptions.md:947`)
- 登记 `S-CH4 T-10e`: PDF 写 "CMSTRF.Some" → KB 写 "正常空格" (处理: KB 写正确值; 依据: 纯排版空格, KB 保留正确写法; KB `knowledge_base/chapters/ch04_general_assumptions.md:947`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Although "DURING" and "DURING/AFTER" are in the STENRF codelist, they describe timing relative to an interval of time rather than a point in time, so are not allowable for use with --STRTPT and --ENRTPT variables.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0044.txt` 第 16-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15|          or it can be UNKNOWN when it ended or if it was ongoing.
 16| Although "DURING" and "DURING/AFTER" are in the STENRF codelist, they describe timing relative to an
 17| interval of time rather than a point in time, so are not allowable for use with --STRTPT and --ENRTPT variables.
 18| Examples of --STRTPT, --STTPT, --ENRTPT, and --ENTPT
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:979` (来源: live valid_hits):

~~~~
 979| Although "DURING" and "DURING/AFTER" are in the STENRF codelist, they describe timing relative to an interval of time rather than a point in time, so are not allowable for use with --STRTPT and --ENRTPT variables.
~~~~

### S8. `ig34_p0069_a002` — r2:TYPO_SIB2

- PDF 页 69 · 原子类型 SENTENCE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-DM T-3`: PDF 写 "Ex3 Row 1 叙述 ACTRMCD" → KB 写 "ACTARMCD" (处理: KB 写正确值; 依据: 同页表头/Row 3 叙述/spec; KB `knowledge_base/domains/DM/examples.md:68`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 1: Subject 001 was randomized to arm A.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 28-33 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27|                ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.
 28| Row 3:         Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind
 29|                treatment epoch, they were assigned to rescue treatment. ARMCD shows the result of their
 30|                assignments, "AR"; ACTARMCD shows their actual treatment, "BR".
 31| dm.xpt
 32| Row      STUDYID   DOMAIN   USUBJID     ARMCD    ARM        ACTARMCD   ACTARM   ARMNRS ACTARMUD
 33| 1        DEF       DM       001         AA       A-OPEN A   AA         A-OPEN A
 34| 2        DEF       DM       002         A        A          A          A
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:20-20` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  20| **Row 1:** Subject 001 was randomized to arm "Drug A". As shown in the SE dataset, this subject completed the "Drug A" element, so their actual arm was also "Drug A".
~~~~

### S9. `ig34_p0069_a003` — r2:TYPO_SIB2

- PDF 页 69 · 原子类型 SENTENCE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-DM T-3`: PDF 写 "Ex3 Row 1 叙述 ACTRMCD" → KB 写 "ACTARMCD" (处理: KB 写正确值; 依据: 同页表头/Row 3 叙述/spec; KB `knowledge_base/domains/DM/examples.md:68`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
At the end of the double-blind treatment epoch, they were assigned to open label A; thus, their ARMCD is "AA".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 21-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20| Example 3
 21| Row 1:         Subject 001 was randomized to drug A. At the end of the double-blind treatment epoch, they were
 22|                assigned to open label A; thus, their ARMCD is "AA". They received the treatment to which they were
 23|                assigned, so ACTRMCD is also "AA".
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:68` (来源: live valid_hits):

~~~~
  68| **Row 1:** Subject 001 was randomized to drug A. At the end of the double-blind treatment epoch, they were assigned to open label A; thus, their ARMCD is "AA". They received the treatment to which they were assigned, so ACTARMCD is also "AA".
~~~~

### S10. `ig34_p0069_a004` — r2:TYPO_SIB2

- PDF 页 69 · 原子类型 SENTENCE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-DM T-3`: PDF 写 "Ex3 Row 1 叙述 ACTRMCD" → KB 写 "ACTARMCD" (处理: KB 写正确值; 依据: 同页表头/Row 3 叙述/spec; KB `knowledge_base/domains/DM/examples.md:68`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
They received the treatment to which they were assigned, so ACTRMD is also "AA".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 22-23 行 (自动定位, 词覆盖 0.923; 版式以原 PDF 为准):

~~~~
 21| Row 1:         Subject 001 was randomized to drug A. At the end of the double-blind treatment epoch, they were
 22|                assigned to open label A; thus, their ARMCD is "AA". They received the treatment to which they were
 23|                assigned, so ACTRMCD is also "AA".
 24| Row 2:         Subject 002 was randomized to drug A. They were lost to follow-up during the double-blind treatment
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:68-68` (来源: fuzzy locate (score 0.923)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  68| **Row 1:** Subject 001 was randomized to drug A. At the end of the double-blind treatment epoch, they were assigned to open label A; thus, their ARMCD is "AA". They received the treatment to which they were assigned, so ACTARMCD is also "AA".
~~~~

### S11. `ig34_p0069_a006` — r2:TYPO_SIB2

- PDF 页 69 · 原子类型 SENTENCE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-DM T-3`: PDF 写 "Ex3 Row 1 叙述 ACTRMCD" → KB 写 "ACTARMCD" (处理: KB 写正确值; 依据: 同页表头/Row 3 叙述/spec; KB `knowledge_base/domains/DM/examples.md:68`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
They were lost to follow-up during the double-blind treatment epoch, so never reached the open label epoch, when they would have been assigned to either the open drug A or the rescue element.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 24-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23|                assigned, so ACTRMCD is also "AA".
 24| Row 2:         Subject 002 was randomized to drug A. They were lost to follow-up during the double-blind treatment
 25|                epoch, so never reached the open label epoch, when they would have been assigned to either the open
 26|                drug A or the rescue element. Their ARMCD is "A". This case illustrates the exception to the rule that
 27|                ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:70` (来源: live valid_hits):

~~~~
  70| **Row 2:** Subject 002 was randomized to drug A. They were lost to follow-up during the double-blind treatment epoch, so never reached the open label epoch, when they would have been assigned to either the open drug A or the rescue element. Their ARMCD is "A". This case illustrates the exception to the rule that ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.
~~~~

### S12. `ig34_p0069_a009` — r2:TYPO_SIB2

- PDF 页 69 · 原子类型 SENTENCE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-DM T-3`: PDF 写 "Ex3 Row 1 叙述 ACTRMCD" → KB 写 "ACTARMCD" (处理: KB 写正确值; 依据: 同页表头/Row 3 叙述/spec; KB `knowledge_base/domains/DM/examples.md:68`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 3: Subject "003" was randomized to drug A, but received drug B.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 28-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27|                ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.
 28| Row 3:         Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind
 29|                treatment epoch, they were assigned to rescue treatment. ARMCD shows the result of their
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:72` (来源: live valid_hits):

~~~~
  72| **Row 3:** Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind treatment epoch, they were assigned to rescue treatment. ARMCD shows the result of their assignments, "AR"; ACTARMCD shows their actual treatment, "BR".
~~~~

### S13. `ig34_p0069_a010` — r2:TYPO_SIB2

- PDF 页 69 · 原子类型 SENTENCE · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-DM T-3`: PDF 写 "Ex3 Row 1 叙述 ACTRMCD" → KB 写 "ACTARMCD" (处理: KB 写正确值; 依据: 同页表头/Row 3 叙述/spec; KB `knowledge_base/domains/DM/examples.md:68`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
At the end of the double-blind treatment epoch, they were assigned to rescue treatment.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0069.txt` 第 28-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27|                ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.
 28| Row 3:         Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind
 29|                treatment epoch, they were assigned to rescue treatment. ARMCD shows the result of their
 30|                assignments, "AR"; ACTARMCD shows their actual treatment, "BR".
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:72` (来源: live valid_hits):

~~~~
  72| **Row 3:** Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind treatment epoch, they were assigned to rescue treatment. ARMCD shows the result of their assignments, "AR"; ACTARMCD shows their actual treatment, "BR".
~~~~

### S14. `ig34_p0118_a016` — r2:TYPO_SIB2

- PDF 页 118 · 原子类型 SENTENCE · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-EX T-6`: PDF 写 "Scheduled dose is represented in mg/mL" → KB 写 "mg/kg" (处理: KB 写正确值; 依据: 同句 (mg/kg) + Ex7 ec ECDOSU=mg/kg; KB `knowledge_base/domains/EX/examples.md:362`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1, 3, 5:  Show the collected intended dose levels (mg/kg) and ECMOOD is "SCHEDULED".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0118.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| The EC dataset shows both intended and actual doses of Drug Z, as collected.
 20| Rows 1, 3, 5: Show the collected intended dose levels (mg/kg) and ECMOOD is "SCHEDULED". Scheduled dose is represented in mg/mL.
 21| Rows 2, 4:       Show the collected actual administration amounts (mL) and ECMOOD is "PERFORMED". Actual doses are represented using dose in mL and concentration (pharmaceutical strength) in mg/mL.
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:362` (来源: live valid_hits):

~~~~
 362| **Rows 1, 3, 5:** Show the collected intended dose levels (mg/kg) and ECMOOD is "SCHEDULED". Scheduled dose is represented in mg/kg.
~~~~

### S15. `ig34_p0201_a005` — r2:TYPO_SIB2

- PDF 页 201 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `S-SPC1 CP T-20`: PDF 写 "CPCELSTA Notes CPSMRKS" → KB 写 "CPCSMRKS" (处理: KB 写正确值; 依据: 同句已列 CPSBMRKS; asm 4; KB `knowledge_base/domains/CP/spec.md:120`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| CPCELSTA | Cell State | Char | (CELSTATE) | Variable Qualifier | A textual description of a subset of the cell population identified in CPTEST based on a particular functional and/or biological state (e.g., "ACTIVATED", "PROLIFERATING", "SENESCENT"). When populated, the values in CPCELSTA and CPSBMRKS, in combination with the values in CPTEST and CPSBMRKS, fully describe the cell population being measured. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0201.txt` 第 15-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|                                                                              subpopulation.
 15| CPCELSTA      Cell State                 Char (CELSTATE)         Variable    A textual description of a subset of the cell population identified in CPTEST based on a particular             Perm
 16|                                                                  Qualifier   functional and/or biological state (e.g., "ACTIVATED", "PROLIFERATING", "SENESCENT"). When
 17|                                                                              populated, the values in CPCELSTA and CPSMRKS, in combination with the values in CPTEST and
 18|                                                                              CPSBMRKS, fully describe the cell population being measured.
 19| CPCSMRKS      Cell State Marker String   Char                    Variable    Identifies the marker(s) or indicator(s) used to define the cell state (i.e., the value in CPCELSTA).           Perm
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:107-109` (来源: fuzzy locate (score 0.575)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 107| When considering the need to use the CPSBMRKS variable, it is important to note that CPTEST is populated with the hierarchically lowest (most granular) named population, to which "Sub" is then appended. This ensures that CPSBMRKS contains only those additional marker(s) required to further differentiate subset(s) within the named population identified in CPTEST. For example, if 2 additional markers, CDxx and CDyy, are used to further classify T lymphocyte helper 2 cells into CDxx+CDyy- and CDxx-CDyy+ sublineages, CPTEST would contain the most granular named population (TLymHelp 2) appended with "Sub" in each of the 2 records (i.e., "TLym Help 2 Sub"), and CPSBMRKS would contain "CDxx+CDyy-" in 1 of the records and "CDxx-CDyy+" in the other.
 108| 
 109| **Rows 1-3:** Show use of CPCELSTA and CPCSMRKS to further subset the named cell population in CPTEST. In row 1, the total monocyte population, based on expression of CD14, is measured without any further subsetting. Rows 2 and 3 show that the monocyte population is further subdivided, based on the cell state, into "proliferating" and "non-proliferating" subpopulations as indicated by the CPCELSTA value. The value "Monocytes" in CPTEST for these rows is appended with "Sub" to "Monocytes Sub" to indicate that the record pertains to a subpopulation of monocytes (i.e., proliferating or non-proliferating). CPCELSTA is used to indicate that row 2 contains data for the proliferating subpopulation and row 3 contains data for the non-proliferating subpopulation. The CPCSMRKS variable is used to indicate that positive expression of the Ki67 marker (i.e., Ki67+) is used to identify the proliferating subpopulation and cells that do not express the Ki67 marker (i.e., Ki67-) is used to identify the non-proliferating subpopulation. The full set of markers used for the test are included in CPMRKSTR, and the cell gating strategy is identified in CPGATE and CPGATDEF using the pipe character (|) to separate each level of the gate in CPGATDEF.
~~~~

### S16. `ig34_p0210_a026` — r2:TYPO_SIB2

- PDF 页 210 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABCD | CP | ABCD-001-001 | 2 | LYM | Lymphocytes | CD45+FSC SSC | LEUK | CD45+ | IMMUNOPHENOTYPING | 1710 | 10^6/L | 1710 | 10^6/L | 1710 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0210.txt` 第 51-52 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 50|                    001-001                                                                                                                                                                               CONCENTRATION           CYTOMETRY     16T04:20
 51| 2   ABCD    CP     ABCD-         2       LYM        Lymphocytes            CD45+FSC      LEUK      CD45+     IMMUNOPHENOTYPING 1710       10^6/L         1710       10^6/L         1710     QUANTITATIVE NUMBER           BLOOD  FLOW          2021-08-
 52|                    001-001                                                 SSC                                                                                                                           CONCENTRATION           CYTOMETRY     16T04:20
 53| 3   ABCD    CP     ABCD-         3       LYMLE      Lymphocytes/Leukocytes CD45+FSC      LEUK      CD45+     IMMUNOPHENOTYPING 25.8       %              25.8       %              25.8     QUANTITATIVE NUMBER           BLOOD  FLOW          2021-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:63` (来源: live valid_hits):

~~~~
  63| | 2 | ABCD | CP | ABCD-001-001 | 2 | LYM | Lymphocytes | CD45+FSC SSC | LEUK | CD45+ | IMMUNOPHENOTYPING | 1710 | 10^6/L | 1710 | 10^6/L | 1710 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2021-08-16T04:20 |
~~~~

### S17. `ig34_p0212_a001` — r2:TYPO_SIB2

- PDF 页 212 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-5`: PDF 写 "Ex2 r6 CPDTC 2020-08-16T04:20" → KB 写 "2020-08-16T12:20" (处理: KB 写正确值; 依据: 同表其余行同一受试者同一检测均 T12:20; KB `knowledge_base/domains/CP/examples.md:92`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 6 | IM001-123 | CP | 0005 00542 | 6 | 1 | LYSLY | Lym Sub/Lym | APOPTOTIC | ANXV+ | CD45+ANXV+/CD45+FSC SSC |  | LYM FSC SSC/CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 21 | % | 21 | % | 21 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T04:20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0212.txt` 第 2-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Row   STUDYID   DOMAIN   USUBJID   CPSEQ   CPGRPID   CPTESTCD   CPTEST       CPCELSTA    CPCSMRKS   CPMRKSTR              CPGATE   CPGATDEF    CPCAT               CPTSTPNL    CPORRES   CPORRESU   CPSTRESC   CPSTRESU   CPSTRESN   CPRESSCL       CPRESTYP        CPSPEC   CPMETHOD    CPDTC
  2| 6     IM001-    CP       0005      6       1         LYSLY      Lym          APOPTOTIC   ANXV+      CD45+ANXV+/CD45+FSC   LYM      FSC         IMMUNOPHENOTYPING   LYM         21        %          21         %          21         QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
  3|       123                00542                                  Sub/Lym                             SSC                            SSC|CD45+                       APOPTOSIS                                                                        FRACTION                 CYTOMETRY   16T04:20
  4|                                                                                                                                                                    COUNT
  5| 7     IM001-    CP       0005      7       1         LYS        Lym Sub      VIABLE;     7AAD-      CD45+7AAD-ANXV+       LYM      FSC         IMMUNOPHENOTYPING   LYM         665       10^6/L     665        10^6/L     665        QUANTITATIVE   NUMBER          BLOOD    FLOW        2020-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:92-92` (来源: fuzzy locate (score 0.966)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  92| | 6 | IM001-123 | CP | 0005 00542 | 6 | 1 | LYSLY | Lym Sub/Lym | APOPTOTIC | ANXV+ | CD45+ANXV+/CD45+FSC SSC | LYM | FSC SSC\|CD45+ | IMMUNOPHENOTYPING | LYM APOPTOSIS COUNT | 21 | % | 21 | % | 21 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T12:20 |
~~~~

### S18. `ig34_p0213_a008` — r2:TYPO_SIB2

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC-123 | CP | ABCD-001-001 | 1 | 1 | MONO | Monocytes |  |  |  | CD14+ | MONO FSC+SSC+CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 394 | 10^6/L | 394 | 10^6/L | 394 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 21-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20| Row   STUDYID   DOMAIN   USUBJID   CPSEQ   CPGRPID   CPTESTCD   CPTEST        CPSBMRKS     CPCELSTA        CPCSMRKS   CPMRKSTR                CPGATE   CPGATDEF         CPCAT               CPTSTPNL     CPORRES   CPORRESU   CPSTRESC   CPSTRESU   CPSTRESN   CPRESSCL       CPRESTYP        CPSPEC   CPMETHOD      CPDTC
 21| 1     ABC-123   CP       ABCD-     1       1         MONO       Monocytes                                             CD14+                   MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    394       10^6/L     394        10^6/L     394        QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 22|                          001-001                                                                                                                                                                                                                                              CONCENTRATION            CYTOMETRY     16T08:00
 23| 2     ABC-123   CP       ABCD-     2       1         MNS        MonoSub                    PROLIFERATING   Ki67+      CD14+Ki67+              MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    50        10^6/L     50         10^6/L     50         QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:129-129` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 129| | 1 | ABC-123 | CP | ABCD-001-001 | 1 | 1 | MONO | Monocytes | | | | CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 394 | 10^6/L | 394 | 10^6/L | 394 | QUANTITATIVE | NUMBER CONCENTRATION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### S19. `ig34_p0213_a011` — r2:TYPO_SIB2

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | ABC-123 | CP | ABCD-001-001 | 4 | 1 | MNSMN | Mono Sub/Mono |  | PROLIFERATING | Ki67+ | CD14+Ki67/CD14+ | MONO FSC+SSC+CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 12.69 | % | 12.69 | % | 12.69 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 27-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26|                          001-001                                                           PROLIFERATING                                                                                                                                                                      CONCENTRATION            CYTOMETRY     16T08:00
 27| 4     ABC-123   CP       ABCD-     4       1         MNSMN      Mono                       PROLIFERATING   Ki67+      CD14+Ki67+/CD14+        MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    12.69     %          12.69      %          12.69      QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 28|                          001-001                                Sub/Mono                                                                                                                                                                                                      FRACTION                 CYTOMETRY     16T08:00
 29| 5     ABC-123   CP       ABCD-     5       1         MNSMN      Mono                       NON-            Ki67-      CD14+Ki67-/CD14+        MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    87.31     %          87.31      %          87.31      QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:132-132` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 132| | 4 | ABC-123 | CP | ABCD-001-001 | 4 | 1 | MNSMN | Mono Sub/Mono | | PROLIFERATING | Ki67+ | CD14+Ki67+/CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 12.69 | % | 12.69 | % | 12.69 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

### S20. `ig34_p0213_a012` — r2:TYPO_SIB2

- PDF 页 213 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`
- 登记 `B-CP T-6`: PDF 写 "Ex3 r2 CPTEST MonoSub" → KB 写 "Mono Sub" (处理: KB 写正确值; 依据: 同 CPTESTCD MNS 的 r3/r8/r9/r12 均 Mono Sub; KB `knowledge_base/domains/CP/examples.md:130`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 5 | ABC-123 | CP | ABCD-001-001 | 5 | 1 | MNSMN | Mono Sub/Mono |  | NON-PROLIFERATING | Ki67- | CD14+Ki67-/CD14+ | MONO FSC+SSC+CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 87.31 | % | 87.31 | % | 87.31 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0213.txt` 第 29-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28|                          001-001                                Sub/Mono                                                                                                                                                                                                      FRACTION                 CYTOMETRY     16T08:00
 29| 5     ABC-123   CP       ABCD-     5       1         MNSMN      Mono                       NON-            Ki67-      CD14+Ki67-/CD14+        MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    87.31     %          87.31      %          87.31      QUANTITATIVE   NUMBER          BLOOD    FLOW          2020-08-
 30|                          001-001                                Sub/Mono                   PROLIFERATING                                                                                                                                                                      FRACTION                 CYTOMETRY     16T08:00
 31| 6     ABC-123   CP       ABCD-     6       1         MNPMNNP    Mono                                                  CD14+Ki67+/CD14+Ki67-   MONO     FSC+SSC+|CD14+   IMMUNOPHENOTYPING   MONOCYTES    0.15                 0.15                  0.15       QUANTITATIVE   RATIO           BLOOD    CALCULATION   2020-08-
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:133-133` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 133| | 5 | ABC-123 | CP | ABCD-001-001 | 5 | 1 | MNSMN | Mono Sub/Mono | | NON-PROLIFERATING | Ki67- | CD14+Ki67-/CD14+ | MONO | FSC+SSC+\|CD14+ | IMMUNOPHENOTYPING | MONOCYTES | 87.31 | % | 87.31 | % | 87.31 | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY | 2020-08-16T08:00 |
~~~~

