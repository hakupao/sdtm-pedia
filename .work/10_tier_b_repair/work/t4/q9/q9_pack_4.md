# T4.1 Q9 扩检包 4 — Q9_SV20_EQUIV (26 条; 编号 Q79-Q104)

> 由 `scripts/t4/t4_q9_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (加前缀 Q).

### Q79. `sv20_p0054_a020` — q9:Q9_SV20_EQUIV

- PDF 页 54 · 原子类型 SENTENCE · 所在节 `§5.1.3.2 Trial Repro Paths`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Trial Repro Paths describes each planned repro path in a repro study, with the ordered sequence of repro stages that comprise each repro path, as well as specification of repro phase and reference start day of the repro phase applicable to the repro stage within the repro path.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0054.txt` 第 40-41 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39| Note: Not for use with human clinical trials.
 40| Trial Repro Paths describes each planned repro path in a repro study, with the ordered sequence of repro stages that comprise each repro path, as well as
 41| specification of repro phase and reference start day of the repro phase applicable to the repro stage within the repro path.
 42| 
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:113` (来源: live valid_hits):

~~~~
 113| Trial Repro Paths describes each planned repro path in a repro study, with the ordered sequence of repro stages that comprise each repro path, as well as specification of repro phase and reference start day of the repro phase applicable to the repro stage within the repro path.
~~~~

### Q80. `sv20_p0055_a005` — q9:Q9_SV20_EQUIV

- PDF 页 55 · 原子类型 TABLE_ROW · 所在节 `§5.1.3.2 Trial Repro Paths`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
3 | RPATHCD | Planned Repro Path Code | Char | | Topic | | Not in human clinical trials | C170503 | A short sequence of characters that represents the planned reproductive path to which the subject was assigned. | Limited to 20 characters. Should be populated in Demographics when repro paths have been defined in this domain. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0055.txt` 第 15-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|                                                                                                         commonality.
 15| 3   RPATHCD      Planned Repro      Char        Topic                      Not in human      C170503    A short sequence of              Limited to 20 characters. Should be populated in
 16|                  Path Code                                                 clinical trials              characters that represents the   Demographics when repro paths have been
 17|                                                                                                         planned reproductive path to     defined in this domain.
 18|                                                                                                         which the subject was
 19|                                                                                                         assigned.
 20| 4   RPATH        Description of     Char        Synonym      RPATHCD       Not in human                                                  Name of the planned repro path.
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### Q81. `sv20_p0055_a006` — q9:Q9_SV20_EQUIV

- PDF 页 55 · 原子类型 TABLE_ROW · 所在节 `§5.1.3.2 Trial Repro Paths`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
4 | RPATH | Description of Planned Repro Path | Char | | Synonym Qualifier | RPATHCD | Not in human clinical trials | | | Name of the planned repro path. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0055.txt` 第 20-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19|                                                                                                         assigned.
 20| 4   RPATH        Description of     Char        Synonym      RPATHCD       Not in human                                                  Name of the planned repro path.
 21|                  Planned Repro                  Qualifier                  clinical trials
 22|                  Path
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:124-124` (来源: fuzzy locate (score 0.889)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 124| | 4 | RPATH | Description of Planned Repro Path | Char | Synonym Qualifier (RPATHCD) | Not in human clinical trials |
~~~~

### Q82. `sv20_p0055_a007` — q9:Q9_SV20_EQUIV

- PDF 页 55 · 原子类型 TABLE_ROW · 所在节 `§5.1.3.2 Trial Repro Paths`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5 | TPSTGORD | Order of Repro Stage within Repro Path | Num | | Timing | | Not in human clinical trials | | | Number that gives the planned order of the repro stage within the repro path. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0055.txt` 第 23-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 22|                  Path
 23| 5   TPSTGORD     Order of Repro     Num         Timing                     Not in human                                                  Number that gives the planned order of the repro
 24|                  Stage within                                              clinical trials                                               stage within the repro path.
 25|                  Repro Path
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:124-125` (来源: fuzzy locate (score 0.8)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 124| | 4 | RPATH | Description of Planned Repro Path | Char | Synonym Qualifier (RPATHCD) | Not in human clinical trials |
 125| | 5 | TPSTGORD | Order of Repro Stage within Repro Path | Num | Timing | Not in human clinical trials |
~~~~

### Q83. `sv20_p0055_a008` — q9:Q9_SV20_EQUIV

- PDF 页 55 · 原子类型 TABLE_ROW · 所在节 `§5.1.3.2 Trial Repro Paths`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
6 | RSTGCD | Repro Stage Code | Char | | Topic | | Not in human clinical trials | | | Short name of the repro stage used for programming and sorting. Maximum 8 characters. The values of RSTGCD used in the Trial Paths dataset must match values for the same repro stage in the Trial Stages dataset. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0055.txt` 第 26-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25|                  Repro Path
 26| 6   RSTGCD       Repro Stage        Char        Topic                      Not in human                                                  Short name of the repro stage used for
 27|                  Code                                                      clinical trials                                               programming and sorting. Maximum 8
 28|                                                                                                                                          characters. The values of RSTGCD used in the
 29|                                                                                                                                          Trial Paths dataset must match values for the
 30|                                                                                                                                          same repro stage in the Trial Stages dataset.
 31| 7   RSTAGE       Description of     Char        Synonym      RSTGCD        Not in human                                                  The name of the repro stage.
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### Q84. `sv20_p0055_a009` — q9:Q9_SV20_EQUIV

- PDF 页 55 · 原子类型 TABLE_ROW · 所在节 `§5.1.3.2 Trial Repro Paths`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
7 | RSTAGE | Description of Repro Stage | Char | | Synonym Qualifier | RSTGCD | Not in human clinical trials | | | The name of the repro stage. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0055.txt` 第 31-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 30|                                                                                                                                          same repro stage in the Trial Stages dataset.
 31| 7   RSTAGE       Description of     Char        Synonym      RSTGCD        Not in human                                                  The name of the repro stage.
 32|                  Repro Stage                    Qualifier                  clinical trials
 33| 8   TPBRANCH     Branch             Char        Rule                       Not in human                                                  Conditions subjects meet, occurring at the end of
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:127-127` (来源: fuzzy locate (score 0.882)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 127| | 7 | RSTAGE | Description of Repro Stage | Char | Synonym Qualifier (RSTGCD) | Not in human clinical trials |
~~~~

### Q85. `sv20_p0055_a010` — q9:Q9_SV20_EQUIV

- PDF 页 55 · 原子类型 TABLE_ROW · 所在节 `§5.1.3.2 Trial Repro Paths`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
8 | TPBRANCH | Branch | Char | | Rule | | Not in human clinical trials | | | Conditions subjects meet, occurring at the end of a repro stage, which cause a repro path to branch off from another repro path. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0055.txt` 第 33-35 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32|                  Repro Stage                    Qualifier                  clinical trials
 33| 8   TPBRANCH     Branch             Char        Rule                       Not in human                                                  Conditions subjects meet, occurring at the end of
 34|                                                                            clinical trials                                               a repro stage, which cause a repro path to
 35|                                                                                                                                          branch off from another repro path.
 36| 9   RPHASE       Repro Phase        Char        Timing                     Not in human                                                  Name of the reproductive phase with which this
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:125-128` (来源: fuzzy locate (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 125| | 5 | TPSTGORD | Order of Repro Stage within Repro Path | Num | Timing | Not in human clinical trials |
 126| | 6 | RSTGCD | Repro Stage Code | Char | Topic | Not in human clinical trials |
 127| | 7 | RSTAGE | Description of Repro Stage | Char | Synonym Qualifier (RSTGCD) | Not in human clinical trials |
 128| | 8 | TPBRANCH | Branch | Char | Rule | Not in human clinical trials |
~~~~

### Q86. `sv20_p0055_a011` — q9:Q9_SV20_EQUIV

- PDF 页 55 · 原子类型 TABLE_ROW · 所在节 `§5.1.3.2 Trial Repro Paths`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
9 | RPHASE | Repro Phase | Char | | Timing | | Not in human clinical trials | | | Name of the reproductive phase with which this repro stage of the repro path is associated. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0055.txt` 第 36-37 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35|                                                                                                                                          branch off from another repro path.
 36| 9   RPHASE       Repro Phase        Char        Timing                     Not in human                                                  Name of the reproductive phase with which this
 37|                                                                            clinical trials                                               repro stage of the repro path is associated.
 38| 10 RPRFDY        Repro Phase        Num         Timing                     Not in human                                                  Sponsor protocol-defined first day of repro
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:125-129` (来源: fuzzy locate (score 0.636)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 125| | 5 | TPSTGORD | Order of Repro Stage within Repro Path | Num | Timing | Not in human clinical trials |
 126| | 6 | RSTGCD | Repro Stage Code | Char | Topic | Not in human clinical trials |
 127| | 7 | RSTAGE | Description of Repro Stage | Char | Synonym Qualifier (RSTGCD) | Not in human clinical trials |
 128| | 8 | TPBRANCH | Branch | Char | Rule | Not in human clinical trials |
 129| | 9 | RPHASE | Repro Phase | Char | Timing | Not in human clinical trials |
~~~~

### Q87. `sv20_p0055_a012` — q9:Q9_SV20_EQUIV

- PDF 页 55 · 原子类型 TABLE_ROW · 所在节 `§5.1.3.2 Trial Repro Paths`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
10 | RPRFDY | Repro Phase Start Reference Day | Num | | Timing | | Not in human clinical trials | | | Sponsor protocol-defined first day of repro phase. Should be zero or 1. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0055.txt` 第 38-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37|                                                                            clinical trials                                               repro stage of the repro path is associated.
 38| 10 RPRFDY        Repro Phase        Num         Timing                     Not in human                                                  Sponsor protocol-defined first day of repro
 39|                  Start Reference                                           clinical trials                                               phase. Should be zero or 1.
 40|                  Day
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:130-134` (来源: fuzzy locate (score 0.667)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 130| | 10 | RPRFDY | Repro Phase Start Reference Day | Num | Timing | Not in human clinical trials |
 131| 
 132| ### 5.1.4 Trial Planned Data Collection
 133| 
 134| The datasets in this section describe parts of a study's schedule of activities.
~~~~

### Q88. `sv20_p0056_a002` — q9:Q9_SV20_EQUIV

- PDF 页 56 · 原子类型 SENTENCE · 所在节 `§5.1.4.1 Trial Visits`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Trial Visits describes the planned order and number of visits in the study.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0056.txt` 第 6-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5| 5.1.4.1 Trial Visits
  6| Trial Visits describes the planned order and number of visits in the study. Trial Visits also describes the allowable or planned values for VISIT, VISITNUM, and
  7| VISITDY in the trial (which are subsequently used as timing variables for the collected study data), and rules for starting and ending each visit. In most blinded
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:142` (来源: live valid_hits):

~~~~
 142| Trial Visits describes the planned order and number of visits in the study. Trial Visits also describes the allowable or planned values for VISIT, VISITNUM, and VISITDY in the trial (which are subsequently used as timing variables for the collected study data), and rules for starting and ending each visit. In most blinded trials, the timing of visits is the same for all subjects in all arms. In the case where visits vary for each arm, there would be a separate record per visit per arm.
~~~~

### Q89. `sv20_p0056_a012` — q9:Q9_SV20_EQUIV

- PDF 页 56 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.1 Trial Visits`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5 | VISITDY | Planned Study Day of Visit | Num | | Timing | | | C171011 | The planned study day of a clinical encounter relative to the sponsor-defined reference start date. | Due to its sequential nature can be used for sorting. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0056.txt` 第 23-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 22|                                               Qualifier                                            clinical encounter.                  VISITDY.
 23| 5 VISITDY      Planned Study      Num         Timing                                    C171011    The planned study day of a           Due to its sequential nature can be used for
 24|                Day of Visit                                                                        clinical encounter relative to the   sorting.
 25|                                                                                                    sponsor-defined reference start
 26|                                                                                                    date.
 27| 6 ARMCD        Planned Arm        Char        Record                                    C83216     A short sequence of characters       ARMCD is limited to 20 characters and does not
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### Q90. `sv20_p0056_a013` — q9:Q9_SV20_EQUIV

- PDF 页 56 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.1 Trial Visits`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
6 | ARMCD | Planned Arm Code | Char | | Record Qualifier | | | C83216 | A short sequence of characters that represents the planned arm to which the subject was assigned. | ARMCD is limited to 20 characters and does not have special character restrictions. If the timing of visits for a trial does not depend on which Arm a subject is in, then ARMCD should be null. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0056.txt` 第 27-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26|                                                                                                    date.
 27| 6 ARMCD        Planned Arm        Char        Record                                    C83216     A short sequence of characters       ARMCD is limited to 20 characters and does not
 28|                Code                           Qualifier                                            that represents the planned arm      have special character restrictions. If the timing of
 29|                                                                                                    to which the subject was             visits for a trial does not depend on which Arm a
 30|                                                                                                    assigned.                            subject is in, then ARMCD should be null.
 31| 7 ARM          Description of     Char        Synonym      ARMCD                        C170984    The name of the planned arm
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### Q91. `sv20_p0056_a015` — q9:Q9_SV20_EQUIV

- PDF 页 56 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.1 Trial Visits`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
8 | TVSTRL | Visit Start Rule | Char | | Rule | | | | | Rule describing when the visit starts, in relation to the sequence of elements. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0056.txt` 第 34-35 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 33|                                                                                                    assigned.
 34| 8 TVSTRL       Visit Start Rule   Char        Rule                                                                                      Rule describing when the visit starts, in relation to
 35|                                                                                                                                         the sequence of elements.
 36| 9 TVENRL       Visit End Rule     Char        Rule                                                                                      Rule describing when the visit ends, in relation to
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:43-47` (来源: fuzzy locate (score 0.562)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | 7 | TEDUR | Planned Duration of Element | Char | Timing |
  44| 
  45| #### 5.1.1.2 Trial Arms (TA)
  46| 
  47| Trial Arms describes each planned arm in a trial. An arm is an ordered sequence of elements; the same element may occur more than once in a given arm. In order to accommodate complex trial designs, this dataset allows for rules for branching from one element to another when a choice is available, and a rule for transitions to allow a subject to skip ahead to another element rather than proceed linearly.
~~~~

### Q92. `sv20_p0056_a016` — q9:Q9_SV20_EQUIV

- PDF 页 56 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.1 Trial Visits`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
9 | TVENRL | Visit End Rule | Char | | Rule | | | | | Rule describing when the visit ends, in relation to the sequence of elements. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0056.txt` 第 35-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34| 8 TVSTRL       Visit Start Rule   Char        Rule                                                                                      Rule describing when the visit starts, in relation to
 35|                                                                                                                                         the sequence of elements.
 36| 9 TVENRL       Visit End Rule     Char        Rule                                                                                      Rule describing when the visit ends, in relation to
 37|                                                                                                                                         the sequence of elements.
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:42-47` (来源: fuzzy locate (score 0.625)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  42| | 6 | TEENRL | Rule for End of Element | Char | Rule |
  43| | 7 | TEDUR | Planned Duration of Element | Char | Timing |
  44| 
  45| #### 5.1.1.2 Trial Arms (TA)
  46| 
  47| Trial Arms describes each planned arm in a trial. An arm is an ordered sequence of elements; the same element may occur more than once in a given arm. In order to accommodate complex trial designs, this dataset allows for rules for branching from one element to another when a choice is available, and a rule for transitions to allow a subject to skip ahead to another element rather than proceed linearly.
~~~~

### Q93. `sv20_p0056_a018` — q9:Q9_SV20_EQUIV

- PDF 页 56 · 原子类型 SENTENCE · 所在节 `§5.1.4.2 Trial Disease Assessments`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Trial Disease Assessments provides information on the planned protocol-specified disease assessment schedule when those disease assessments cannot be expressed using Trial Visits.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0056.txt` 第 41-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 40| 5.1.4.2 Trial Disease Assessments
 41| Trial Disease Assessments provides information on the planned protocol-specified disease assessment schedule when those disease assessments cannot be
 42| expressed using Trial Visits.
 43| In oncology studies, compliance with the disease-assessment schedule is essential to reduce the risk of assessment time bias. The TD domain makes possible an
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:160` (来源: live valid_hits):

~~~~
 160| Trial Disease Assessments provides information on the planned protocol-specified disease assessment schedule when those disease assessments cannot be expressed using Trial Visits.
~~~~

### Q94. `sv20_p0057_a005` — q9:Q9_SV20_EQUIV

- PDF 页 57 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.2 Trial Disease Assessments`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
3 | TDORDER | Sequence of Planned Assessment Schedule | Num | | Timing | | | | | A number given to ensure ordinal sequencing of the planned assessment schedules within a trial. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0057.txt` 第 18-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17|                                                                                                         commonality.
 18| 3 TDORDER       Sequence of        Num             Timing                                                                     A number given to ensure ordinal sequencing of the planned
 19|                 Planned                                                                                                       assessment schedules within a trial.
 20|                 Assessment
 21|                 Schedule
 22| 4 TDANCVAR      Anchor Variable    Char            Timing                                                                     A reference to the date variable name that provides the start
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:170-172` (来源: fuzzy locate (score 0.5)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 170| | 3 | TDORDER | Sequence of Planned Assessment Schedule | Num | Timing |
 171| | 4 | TDANCVAR | Anchor Variable Name | Char | Timing |
 172| | 5 | TDSTOFF | Offset from the Anchor | Char | Timing |
~~~~

### Q95. `sv20_p0057_a008` — q9:Q9_SV20_EQUIV

- PDF 页 57 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.2 Trial Disease Assessments`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
6 | TDTGTPAI | Planned Assessment Interval | Char | ISO 8601 duration | Timing | | | | | The planned interval between disease assessments. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0057.txt` 第 32-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31|                                                                                                                               the variable indicated in TDANCVAR. The value of this
 32|                                                                                                                               variable will be a non-negative duration.
 33| 6 TDTGTPAI Planned                 Char ISO        Timing                                                                     The planned interval between disease assessments.
 34|            Assessment                   8601
 35|            Interval                     duration
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:172-176` (来源: fuzzy locate (score 0.643)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 172| | 5 | TDSTOFF | Offset from the Anchor | Char | Timing |
 173| | 6 | TDTGTPAI | Planned Assessment Interval | Char | Timing |
 174| | 7 | TDMINPAI | Planned Assessment Interval Minimum | Char | Timing |
 175| | 8 | TDMAXPAI | Planned Assessment Interval Maximum | Char | Timing |
 176| | 9 | TDNUMRPT | Maximum Number of Actual Assessments | Num | Record Qualifier |
~~~~

### Q96. `sv20_p0057_a009` — q9:Q9_SV20_EQUIV

- PDF 页 57 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.2 Trial Disease Assessments`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
7 | TDMINPAI | Planned Assessment Interval Minimum | Char | ISO 8601 duration | Timing | | | | | The lower limit of the allowed range for the planned interval between disease assessments. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0057.txt` 第 36-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35|            Interval                     duration
 36| 7 TDMINPAI Planned                 Char ISO        Timing                                                                     The lower limit of the allowed range for the planned interval
 37|            Assessment                   8601                                                                                  between disease assessments.
 38|            Interval                     duration
 39|            Minimum
 40| 8 TDMAXPAI Planned                 Char ISO        Timing                                                                     The upper limit of the allowed range for the planned interval
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:172-176` (来源: fuzzy locate (score 0.524)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 172| | 5 | TDSTOFF | Offset from the Anchor | Char | Timing |
 173| | 6 | TDTGTPAI | Planned Assessment Interval | Char | Timing |
 174| | 7 | TDMINPAI | Planned Assessment Interval Minimum | Char | Timing |
 175| | 8 | TDMAXPAI | Planned Assessment Interval Maximum | Char | Timing |
 176| | 9 | TDNUMRPT | Maximum Number of Actual Assessments | Num | Record Qualifier |
~~~~

### Q97. `sv20_p0057_a010` — q9:Q9_SV20_EQUIV

- PDF 页 57 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.2 Trial Disease Assessments`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
8 | TDMAXPAI | Planned Assessment Interval Maximum | Char | ISO 8601 duration | Timing | | | | | The upper limit of the allowed range for the planned interval between disease assessments. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0057.txt` 第 40-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39|            Minimum
 40| 8 TDMAXPAI Planned                 Char ISO        Timing                                                                     The upper limit of the allowed range for the planned interval
 41|            Assessment                   8601                                                                                  between disease assessments.
 42|            Interval                     duration
 43|            Maximum
 44| 9 TDNUMRPT Maximum                 Num             Record                                                                     This variable must represent the maximum number of actual
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:175-180` (来源: fuzzy locate (score 0.619)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 175| | 8 | TDMAXPAI | Planned Assessment Interval Maximum | Char | Timing |
 176| | 9 | TDNUMRPT | Maximum Number of Actual Assessments | Num | Record Qualifier |
 177| 
 178| #### 5.1.4.3 Trial Disease Milestones (TM)
 179| 
 180| Trial Disease Milestones is used to describe observations or activities expected to occur in the course of the disease under study, the timing of which is of interest for the study.
~~~~

### Q98. `sv20_p0057_a013` — q9:Q9_SV20_EQUIV

- PDF 页 57 · 原子类型 SENTENCE · 所在节 `§5.1.4.3 Trial Disease Milestones`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Trial Disease Milestones is used to describe observations or activities expected to occur in the course of the disease under study, the timing of which is of interest for the study.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0057.txt` 第 55-56 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 54| 5.1.4.3 Trial Disease Milestones
 55| Trial Disease Milestones is used to describe observations or activities expected to occur in the course of the disease under study, the timing of which is of interest
 56| for the study.
 57| 
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:180` (来源: live valid_hits):

~~~~
 180| Trial Disease Milestones is used to describe observations or activities expected to occur in the course of the disease under study, the timing of which is of interest for the study.
~~~~

### Q99. `sv20_p0058_a005` — q9:Q9_SV20_EQUIV

- PDF 页 58 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.3 Trial Disease Milestones`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
3 | MIDSTYPE | Disease Milestone Type | Char | | Topic | | | | | The type of disease milestone. | | "HYPOGLYCEMIC EVENT"
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0058.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|                                                                                                            commonality.
 15| 3 MIDSTYPE      Disease Milestone    Char        Topic                                                                                       The type of disease milestone.            "HYPOGLYCEMIC
 16|                 Type                                                                                                                                                                   EVENT"
 17| 4 TMDEF         Disease Milestone    Char        Variable      MIDSTYPE                                                                      Definition of the disease milestone.
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:188-188` (来源: fuzzy locate (score 0.636)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 188| | 3 | MIDSTYPE | Disease Milestone Type | Char | Topic |
~~~~

### Q100. `sv20_p0058_a006` — q9:Q9_SV20_EQUIV

- PDF 页 58 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.3 Trial Disease Milestones`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
4 | TMDEF | Disease Milestone Definition | Char | | Variable Qualifier | MIDSTYPE | | | | Definition of the disease milestone. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0058.txt` 第 17-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 16|                 Type                                                                                                                                                                   EVENT"
 17| 4 TMDEF         Disease Milestone    Char        Variable      MIDSTYPE                                                                      Definition of the disease milestone.
 18|                 Definition                       Qualifier
 19| 5 TMRPT         Disease Milestone    Char        Record                                                                                      Indicates whether this is a disease
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:189-194` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 189| | 4 | TMDEF | Disease Milestone Definition | Char | Variable Qualifier (MIDSTYPE) |
 190| | 5 | TMRPT | Disease Milestone Repetition Indicator | Char | Record Qualifier |
 191| 
 192| ### 5.1.5 Trial Inclusion/Exclusion Criteria (TI)
 193| 
 194| Trial Inclusion/Exclusion contains 1 record for each of the inclusion and exclusion criterion for the trial. If eligibility criteria change during a trial, each version of the eligibility criteria may be represented.
~~~~

### Q101. `sv20_p0058_a007` — q9:Q9_SV20_EQUIV

- PDF 页 58 · 原子类型 TABLE_ROW · 所在节 `§5.1.4.3 Trial Disease Milestones`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5 | TMRPT | Disease Milestone Repetition Indicator | Char | | Record Qualifier | | | | | Indicates whether this is a disease milestone that can occur only once ("N") or one that can occur multiple times ("Y"). | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0058.txt` 第 19-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18|                 Definition                       Qualifier
 19| 5 TMRPT         Disease Milestone    Char        Record                                                                                      Indicates whether this is a disease
 20|                 Repetition                       Qualifier                                                                                   milestone that can occur only once
 21|                 Indicator                                                                                                                    ("N") or one that can occur multiple
 22|                                                                                                                                              times ("Y").
 23| 
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### Q102. `sv20_p0058_a009` — q9:Q9_SV20_EQUIV

- PDF 页 58 · 原子类型 SENTENCE · 所在节 `§5.1.5 Trial Inclusion/Exclusion Criteria`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Trial Inclusion/Exclusion contains 1 record for each of the inclusion and exclusion criterion for the trial.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0058.txt` 第 26-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| 5.1.5 Trial Inclusion/Exclusion Criteria
 26| Trial Inclusion/Exclusion contains 1 record for each of the inclusion and exclusion criterion for the trial. If eligibility criteria change during a trial, each version
 27| of the eligibility criteria may be represented.
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:194` (来源: live valid_hits):

~~~~
 194| Trial Inclusion/Exclusion contains 1 record for each of the inclusion and exclusion criterion for the trial. If eligibility criteria change during a trial, each version of the eligibility criteria may be represented.
~~~~

### Q103. `sv20_p0058_a015` — q9:Q9_SV20_EQUIV

- PDF 页 58 · 原子类型 TABLE_ROW · 所在节 `§5.1.5 Trial Inclusion/Exclusion Criteria`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
3 | IETESTCD | Inclusion/Exclusion Criterion Short Name | Char | | Topic | | | | | Short name IETEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST"). IETESTCD cannot contain characters other than letters, numbers, or underscores. The prefix "IE" is used to ensure consistency with the IE domain. | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0058.txt` 第 41-47 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 40|                                                                                                          commonality.
 41| 3 IETESTCD     Inclusion/Exclusion  Char          Topic                                                                          Short name IETEST. It can be used as a column name
 42|                Criterion Short Name                                                                                              when converting a dataset from a vertical to a
 43|                                                                                                                                  horizontal format. The value in IETESTCD cannot be
 44|                                                                                                                                  longer than 8 characters, nor can it start with a number
 45|                                                                                                                                  (e.g., "1TEST"). IETESTCD cannot contain characters
 46|                                                                                                                                  other than letters, numbers, or underscores. The prefix
 47|                                                                                                                                  "IE" is used to ensure consistency with the IE domain.
 48| 4 IETEST       Inclusion/Exclusion    Char        Synonym       IETESTCD                                                         Full text of the inclusion or exclusion criterion. The
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### Q104. `sv20_p0058_a017` — q9:Q9_SV20_EQUIV

- PDF 页 58 · 原子类型 TABLE_ROW · 所在节 `§5.1.5 Trial Inclusion/Exclusion Criteria`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5 | IECAT | Inclusion/Exclusion Category | Char | | Grouping Qualifier | | | | | Used for categorization of the inclusion or exclusion criterion. The prefix "IE" (rather than TI) is used to ensure consistency with the IE domain. | | "INCLUSION", "EXCLUSION"
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0058.txt` 第 51-53 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 50|                                                                                                                                  with the IE domain.
 51| 5 IECAT        Inclusion/Exclusion    Char        Grouping                                                                       Used for categorization of the inclusion or exclusion        "INCLUSION",
 52|                Category                           Qualifier                                                                      criterion. The prefix "IE" (rather than TI) is used to       "EXCLUSION"
 53|                                                                                                                                  ensure consistency with the IE domain.
 54| 6 IESCAT       Inclusion/Exclusion    Char        Grouping                                                                       A further categorization of the exception criterion. Can     "MAJOR",
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

