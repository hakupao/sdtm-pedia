# T4.1 第二轮补检包 1 — XDOC (25 条; 编号 R1-R25)

> 由 `scripts/t4/t4_round2_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 R).

### R1. `ig34_p0060_a003` — r2:XDOC

- PDF 页 60 · 原子类型 SENTENCE · 所在节 `§5 [Models for Special-purpose Domains]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Special-purpose domains provide specific, standardized structures to represent additional important information that does not fit any of the general observation classes.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0060.txt` 第 2-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| 5 Models for Special-purpose Domains
  2| Special-purpose Domains is an SDTM class in its own right. Special-purpose domains provide specific, standardized structures to represent additional important
  3| information that does not fit any of the general observation classes.
  4| 
~~~~

KB 现文: `knowledge_base/model/03_special_purpose_domains.md:9-9` (来源: fuzzy locate (score 0.727)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
   9| In addition to the 3 general observation classes, a submission will generally include a set of other special-purpose datasets of specific standardized structures to represent additional important information. A Demographics special-purpose domain is included with human and animal studies (see Section 3.2.1, Demographics). Other special-purpose domains may be included.
~~~~

### R2. `ig34_p0079_a001` — r2:XDOC

- PDF 页 79 · 原子类型 HEADING · 所在节 `§5.3 [Subject Elements]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
5.3 Subject Elements (SE)
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0079.txt` 第 10-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9| 
 10| 5.3 Subject Elements (SE)
 11| SE – Description/Overview
~~~~

KB 现文: `knowledge_base/domains/SE/assumptions.md:31-35` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  31| 1. For any particular subject, the dates in the SE table are the dates when the transition events identified in the TE table occurred. Judgment may be needed to match actual events in a subject's experience with the definitions of transition events (i.e., events that mark the start of new elements) in the TE table; actual events may vary from the plan. For instance, in a single-dose pharmacokinetics (PK) study, the transition events might correspond to study drug doses of 5 and 10 mg. If a subject actually received a dose of 7 mg when they were scheduled to receive 5 mg, a decision will have to be made on how to represent this in the SE domain.
  32| 
  33| 2. If the date/time of a transition element was not collected directly, the method used to infer the element start date/time should be explained in the Comments column of the Define-XML document.
  34| 
  35| 3. Judgment will also have to be used in deciding how to represent a subject's experience if an element does not proceed or end as planned. For instance, the plan might identify a trial element that is to start with the first of a series of 5 daily doses and end after 1 week, when the subject transitions to the next treatment element. If the subject actually started the next treatment epoch (see Section 7.1, Introduction to Trial Design Model Datasets, and Section 7.1.2, Definitions of Trial Design Concepts) after 4 weeks, the sponsor would have to decide whether to represent this as an abnormally long element, or as a normal element plus an unplanned non-treatment element.
~~~~

### R3. `ig34_p0079_a016` — r2:XDOC

- PDF 页 79 · 原子类型 TABLE_ROW · 所在节 `§5.3 [Subject Elements]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
DOMAIN | Domain Abbreviation | Char | SE | Identifier | Two-character abbreviation for the domain. | Req
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0079.txt` 第 32-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| STUDYID       Study Identifier    Char                         Identifier   Unique identifier for a study.                                                                            Req
 32| DOMAIN        Domain Abbreviation Char SE                      Identifier   Two-character abbreviation for the domain.                                                                Req
 33| USUBJID       Unique Subject      Char                         Identifier   Identifier used to uniquely identify a subject across all studies for all applications or submissions     Req
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:202-202` (来源: fuzzy locate (score 0.9)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 202| | RDOMAIN | Related Domain Abbreviation | Char | (DOMAIN) | Identifier | Two-character abbreviation for the domain of the parent record(s). | Req |
~~~~

### R4. `ig34_p0080_a003` — r2:XDOC

- PDF 页 80 · 原子类型 TABLE_ROW · 所在节 `§5.3 [Subject Elements]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
TAETORD | Planned Order of Element within Arm | Num | | Timing | Number that gives the planned order of the elements within the subject's assigned trial arm.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0080.txt` 第 10-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9|                Element                                              Qualifier
 10| TAETORD        Planned Order of       Num                           Timing        Number that gives the planned order of the element within the subject's assigned trial arm.                 Perm
 11|                Element within Arm
 12| EPOCH          Epoch                  Char (EPOCH)                  Timing        Epoch associated with the element in the planned sequence of elements for the arm to which the subject Perm
 13|                                                                                   was assigned.
~~~~

KB 现文: `knowledge_base/model/02_observation_classes.md:322-325` (来源: fuzzy locate (score 0.778)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 322| | 1 | VISITNUM | Visit Number | Num | Timing | Numeric version of VISIT for sorting |
 323| | 2 | VISIT | Visit Name | Char | Timing | Protocol-defined visit name |
 324| | 3 | VISITDY | Planned Study Day of Visit | Num | Timing | Protocol-defined study day |
 325| | 4 | TAETORD | Planned Order of Element Within Arm | Num | Timing | Value for the element within the subject's assigned arm |
~~~~

### R5. `ig34_p0080_a009` — r2:XDOC

- PDF 页 80 · 原子类型 TABLE_ROW · 所在节 `§5.3 [Subject Elements]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
SEUPDES | Description of Unplanned Element | Char | | Synonym Qualifier | Description of what happened to the subject during an unplanned element. Used only if ETCD has the value of "UNPLAN".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0080.txt` 第 22-23 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 21|                 Element
 22|  SEUPDES Description of                  Char                          Synonym         Description of what happened to the subject during an unplanned element. Used only if ETCD has the     Perm
 23|                 Unplanned Element                                      Qualifier       value of "UNPLAN".
 24| 1In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.
~~~~

KB 现文: `knowledge_base/model/03_special_purpose_domains.md:141-145` (来源: fuzzy locate (score 0.818)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 141| | 13 | SEUPDES | Description of Unplanned Element | Char | Synonym Qualifier (ETCD) | Used only if ETCD has a value of "UNPLAN" |
 142| 
 143| ### 3.2.3.2 Subject Repro Stages
 144| 
 145| Subject Repro Stages (not for use with human clinical trials) describes the actual order of repro stages experienced by the subject, together with the start date or start date and time and end date/time for each. Planned repro stages are described in the Trial Design Model (see Section 5.1.3.1, Trial Repro Stages). Because actual data does not always follow the plan, the SDTM allows for descriptions of an unplanned repro stage for subjects (SJUPDES).
~~~~

### R6. `ig34_p0114_a014` — r2:XDOC

- PDF 页 114 · 原子类型 HEADING · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Subject ABC5001
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0114.txt` 第 17-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 16| This is an example of a double-blind study design comparing 10 and 20 mg of drug X vs. placebo taken daily, morning and evening, for a week.
 17| Subject ABC5001
 18| Bottle Time Point     Number of Tablets Taken      Start Date    End Date
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:173` (来源: live valid_hits):

~~~~
 173| **Subject ABC5001**
~~~~

### R7. `ig34_p0114_a018` — r2:XDOC

- PDF 页 114 · 原子类型 HEADING · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Subject ABC5002
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0114.txt` 第 22-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 21| 
 22| Subject ABC5002
 23| Bottle Time Point     Number of Tablets Taken      Start Date    End Date
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:180` (来源: live valid_hits):

~~~~
 180| **Subject ABC5002**
~~~~

### R8. `ig34_p0114_a022` — r2:XDOC

- PDF 页 114 · 原子类型 HEADING · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Subject ABC5003
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0114.txt` 第 27-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26| 
 27| Subject ABC5003
 28| Bottle Time Point     Number of Tablets Taken      Start Date    End Date
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:187` (来源: live valid_hits):

~~~~
 187| **Subject ABC5003**
~~~~

### R9. `ig34_p0115_a029` — r2:XDOC

- PDF 页 115 · 原子类型 HEADING · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Subject 56789001
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0115.txt` 第 33-33 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32| The following CRFs show data for 2 subjects.
 33| Subject 56789001
 34| Period 1                                                              Period 2
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:243,294` (来源: live valid_hits):

~~~~
 243| **Subject 56789001**
 294| **Rows 1-12:** Unblinding revealed that subject 56789001 received placebo-coated tablets during the first treatment epoch and placebo capsules during the second treatment epoch.
~~~~

### R10. `ig34_p0116_a001` — r2:XDOC

- PDF 页 116 · 原子类型 HEADING · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Subject 56789003
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0116.txt` 第 1-1 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Subject 56789003
  2| Period 1                                                              Period 2
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:252,296` (来源: live valid_hits):

~~~~
 252| **Subject 56789003**
 296| **Rows 13-24:** Unblinding revealed that subject 56789003 received placebo capsules during the first treatment epoch and placebo-coated tablets during the second treatment epoch.
~~~~

### R11. `ig34_p0195_a020` — r2:XDOC

- PDF 页 195 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| --ORRESU | Original Units | Char | * | Variable Qualifier | Unit for --ORRES and --ORREF. Subject to domain-specific test code controlled terminology. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0195.txt` 第 34-35 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 33| --ORRES        Result or Finding in Original   Char                       Result       Result of the measurement or finding as originally received or collected.                                             Exp
 34|                Units                                                      Qualifier
 35| --ORRESU       Original Units                  Char   *                   Variable     Unit for --ORRES and --ORREF. Subject to domain-specific test code controlled terminology.                            Perm
 36|                                                                           Qualifier
~~~~

KB 现文: `knowledge_base/model/02_observation_classes.md:192-196` (来源: fuzzy locate (score 0.55)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 192| | 25 | --TSTPNL | Test Panel | Char | Grouping Qualifier | CP domain only |
 193| | 26 | --POS | Position of Subject During Observation | Char | Record Qualifier |  |
 194| | 27 | --BODSYS | Body System or Organ Class | Char | Record Qualifier |  |
 195| | 28 | --ORRES | Result or Finding in Original Units | Char | Result Qualifier | Original collected result |
 196| | 29 | --ORRESU | Original Units | Char | Variable Qualifier (--ORRES/--ORNRLO/--ORNRHI/--ORREF) |  |
~~~~

### R12. `ig34_p0195_a022` — r2:XDOC

- PDF 页 195 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| --STRESC | Result or Finding in Standard Format | Char | | Result Qualifier | Contains the result value for all findings copied or derived from --ORRES, in a standard format or in standard units. --STRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in --STRESN. | Exp |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0195.txt` 第 40-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39|                                                                                        instrument or lab vendor.
 40| --STRESC       Result or Finding in            Char                       Result       Contains the result value for all findings copied or derived from --ORRES, in a standard format or in standard        Exp
 41|                Standard Format                                            Qualifier    units. --STRESC should store all results or findings in character format; if results are numeric, they should
 42|                                                                                        also be stored in numeric format in --STRESN.
 43| --STRESN       Numeric Result/Finding in       Num                        Result       Used for continuous or numeric results or findings in standard format; copied in numeric format from --               Perm
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:327-332` (来源: fuzzy locate (score 0.529)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 327| | What date/times are collected? | • If the dates collected are start and/or end dates, then data are probably about an event or intervention.<br>• If the dates collected are dates of assessments, then data probably represent a finding.<br>• If dates of collection are different from other dates collected, it suggests that data are historical or are about an event or intervention that happened independently of the study schedule for data collection. |
 328| | Is verbatim text collected and then coded? | • A “Yes” answer suggests that this is Events or Interventions general observation class data. However, Findings general observation class data from an examination (e.g., physical examination) that identifies abnormalities may also be coded. Note that for Events and Interventions general observation class data, the topic variable is coded, whereas for Findings general observation class data, the result is coded.<br>• A “No” answer is inconclusive. This does not rule out Events or Interventions general observation class data, because events or interventions are not always collected as verbatim text, but may be prespecified or chosen from a list; it also does not rule out Findings general observation class data. |
 329| | If this is data about an event, does it apply to the event as a whole? | • A “Yes” answer suggests this is traditional Events general observation class data, and it should have a record in an Events domain.<br>• A “No” answer suggests that there are multiple time-based findings about an event, and that these data should be treated as Findings About data. |
 330| | Does this data meet the criteria for representation in a Questionnaires, Ratings, and Scales (QRS) domain? | • The criteria for QRS are available at: https://www.cdisc.org/foundational/qrs.<br>• There are many standard questionnaires and rating scales that collect information about symptoms. The fact that these data are findings about symptoms does not mean that the data should be represented in FA rather than a QRS domain (QS, FT, or RS).<br>• Data about symptoms may be collected in a format that is usually associated with questionnaires and rating scales (e.g., visual analog scale). This format alone does not mean that the data should be represented in a QRS domain. |
 331| 
 332| A record in the Events general observation class is intended to represent the event as a whole. (Note that sponsors may choose how they define the "event as a whole." See Section 6.2.1, Adverse Events, assumption 7e.) Such a record typically includes what the condition was (captured in --TERM, the topic variable) and when it happened (captured in its start and/or end dates). Other qualifier values (e.g., severity, seriousness) apply to the totality of the event.
~~~~

### R13. `ig34_p0195_a024` — r2:XDOC

- PDF 页 195 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| --STRESU | Standard Units | Char | * | Variable Qualifier | Standardized units used for --STRESC, --STRESN, --STREFC, and --STREFN. Subject to domain-specific test code controlled terminology. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0195.txt` 第 45-46 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 44|                Standard Units                                             Qualifier    STRESC. --STRESN should store all numeric test results or findings.
 45| --STRESU       Standard Units                  Char   *                   Variable     Standardized units used for --STRESC, --STRESN, --STREFC, and --STREFN. Subject to domain-specific                    Perm
 46|                                                                           Qualifier    test code controlled terminology.
 47| 
~~~~

KB 现文: `knowledge_base/model/02_observation_classes.md:205-210` (来源: fuzzy locate (score 0.565)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 205| | 38 | --IMPLBL | Implantation Site Label | Char | Record Qualifier | Not in human clinical trials; IC Domain only |
 206| | 39 | --STRESN | Numeric Result/Finding in Standard Units | Num | Result Qualifier | Numeric standardized result |
 207| | 40 | --STRESU | Standard Units | Char | Variable Qualifier (--STRESC/--STRESN/--STNRLO/--STNRHI/--STREFC/--STREFN/--LLOQ/--ULOQ) |  |
 208| | 41 | --STNRLO | Normal Range Lower Limit-Standard Units | Num | Variable Qualifier (--STRESC/--STRESN) | Standard units |
 209| | 42 | --STNRHI | Normal Range Upper Limit-Standard Units | Num | Variable Qualifier (--STRESC/--STRESN) | Standard units |
 210| | 43 | --STNRC | Normal Range for Character Results | Char | Variable Qualifier (--STRESC) | Char reference range |
~~~~

### R14. `ig34_p0196_a001` — r2:XDOC

- PDF 页 196 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| --STAT | Completion Status | Char | * | Record Qualifier | Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE". | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0196.txt` 第 3-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| Name                                              Codelist or Format1
  3| --STAT        Completion Status              Char *                        Record           Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not         Perm
  4|                                                                            Qualifier        generate a result. Should be null or have a value of "NOT DONE".
  5| --REASND      Reason Not Done                Char                          Record           Reason not done. Used in conjunction with --STAT when value is "NOT DONE".                                         Perm
~~~~

KB 现文: `knowledge_base/model/02_observation_classes.md:54-59` (来源: fuzzy locate (score 0.567)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  54| | 10 | --STAT | Completion Status | Char | Record Qualifier | "NOT DONE" or null |
  55| | 11 | --REASND | Reason Not Done | Char | Record Qualifier | Used with --STAT when value is "NOT DONE" |
  56| | 12 | --CNTMOD | Contact Mode | Char | Record Qualifier | Way in which event, visit, or contact was conducted |
  57| | 13 | --EPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier | Whether intervention was changed due to epidemic or pandemic |
  58| | 14 | --INDC | Indication | Char | Record Qualifier | Sign, symptom, or condition that is the basis for treatment initiation |
  59| | 15 | --CLAS | Class | Char | Variable Qualifier (--TRT) | Standardized or dictionary-derived name for a grouping of drugs |
~~~~

### R15. `ig34_p0196_a002` — r2:XDOC

- PDF 页 196 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| --REASND | Reason Not Done | Char |  | Record Qualifier | Reason not done. Used in conjunction with --STAT when value is "NOT DONE". | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0196.txt` 第 4-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| --STAT        Completion Status              Char *                        Record           Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not         Perm
  4|                                                                            Qualifier        generate a result. Should be null or have a value of "NOT DONE".
  5| --REASND      Reason Not Done                Char                          Record           Reason not done. Used in conjunction with --STAT when value is "NOT DONE".                                         Perm
  6|                                                                            Qualifier
~~~~

KB 现文: `knowledge_base/model/02_observation_classes.md:55-56` (来源: fuzzy locate (score 0.875)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  55| | 11 | --REASND | Reason Not Done | Char | Record Qualifier | Used with --STAT when value is "NOT DONE" |
  56| | 12 | --CNTMOD | Contact Mode | Char | Record Qualifier | Way in which event, visit, or contact was conducted |
~~~~

### R16. `ig34_p0196_a009` — r2:XDOC

- PDF 页 196 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| VISITNUM | Visit Number | Num |  | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0196.txt` 第 19-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18|                                                                            Qualifier
 19| VISITNUM      Visit Number                   Num                           Timing           Clinical encounter number. Numeric version of VISIT, used for sorting.                                             Perm
 20| VISIT         Visit Name                     Char                          Timing           Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.            Perm
~~~~

KB 现文: `knowledge_base/model/02_observation_classes.md:322-327` (来源: fuzzy locate (score 0.786)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 322| | 1 | VISITNUM | Visit Number | Num | Timing | Numeric version of VISIT for sorting |
 323| | 2 | VISIT | Visit Name | Char | Timing | Protocol-defined visit name |
 324| | 3 | VISITDY | Planned Study Day of Visit | Num | Timing | Protocol-defined study day |
 325| | 4 | TAETORD | Planned Order of Element Within Arm | Num | Timing | Value for the element within the subject's assigned arm |
 326| | 5 | EPOCH | Epoch | Char | Timing | Time period defined in the protocol with a study-specific purpose |
 327| | 6 | RPHASE | Repro Phase | Char | Timing | Not in human clinical trials |
~~~~

### R17. `ig34_p0196_a010` — r2:XDOC

- PDF 页 196 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| VISIT | Visit Name | Char |  | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0196.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| VISITNUM      Visit Number                   Num                           Timing           Clinical encounter number. Numeric version of VISIT, used for sorting.                                             Perm
 20| VISIT         Visit Name                     Char                          Timing           Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.            Perm
 21| VISITDY       Planned Study Day of Visit     Num                           Timing           Planned study day of the visit based upon RFSTDTC in Demographics.                                                 Perm
~~~~

KB 现文: `knowledge_base/chapters/ch08_relationships.md:277-280` (来源: fuzzy locate (score 0.571)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 277| 1. Values (e.g., CRF page number or name) may be placed in COREF.
 278| 2. Timing variables (e.g., VISITNUM, VISIT) may be added to the CO special-purpose domain. See Section 5.1, Comments, assumption 5 for a complete list of identifier and timing variables that can be added to the CO special-purpose domain.
 279| 
 280| As with Supplemental Qualifiers (SUPP--) and Related Records (RELREC), --GRPID and other grouping variables can be used as the value in IDVAR to identify comments with relationships to multiple domain records, for example a comment that applies to a group of concomitant medications, perhaps taken as a combination therapy. The limitation of this is that a single comment may only be related to a group of records in 1 domain (RDOMAIN can have only 1 value). If a single comment relates to records in multiple domains, the comment may need to be repeated in the CO special-purpose domain to facilitate the understanding of the relationships.
~~~~

### R18. `ig34_p0364_a014` — r2:XDOC

- PDF 页 364 · 原子类型 TABLE_ROW · 所在节 `§6.4.3 Variables Unique to Findings About`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| OCCUR | Occurrence Indicator |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0364.txt` 第 24-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 23| FATESTCD FATEST
 24| OCCUR        Occurrence Indicator
 25| SEV          Severity/Intensity
~~~~

KB 现文: `knowledge_base/model/02_observation_classes.md:52,113` (来源: live valid_hits):

~~~~
  52| | 8 | --OCCUR | Occurrence Indicator | Char | Record Qualifier | Whether a prespecified event or intervention has occurred |
 113| | 15 | --OCCUR | Occurrence Indicator | Char | Record Qualifier | Not in AE domain |
~~~~

### R19. `ig34_p0364_a015` — r2:XDOC

- PDF 页 364 · 原子类型 TABLE_ROW · 所在节 `§6.4.3 Variables Unique to Findings About`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| SEV | Severity/Intensity |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0364.txt` 第 25-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24| OCCUR        Occurrence Indicator
 25| SEV          Severity/Intensity
 26| TOXGR        Toxicity Grade
~~~~

KB 现文: `knowledge_base/model/02_observation_classes.md:129,256` (来源: live valid_hits):

~~~~
 129| | 31 | --SEV | Severity/Intensity | Char | Record Qualifier | "MILD", "MODERATE", "SEVERE" |
 256| | 89 | --SEV | Severity/Intensity | Char | Record Qualifier |  |
~~~~

### R20. `ig34_p0364_a016` — r2:XDOC

- PDF 页 364 · 原子类型 TABLE_ROW · 所在节 `§6.4.3 Variables Unique to Findings About`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| TOXGR | Toxicity Grade |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0364.txt` 第 26-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| SEV          Severity/Intensity
 26| TOXGR        Toxicity Grade
 27| 
~~~~

KB 现文: `knowledge_base/model/02_observation_classes.md:153,255` (来源: live valid_hits):

~~~~
 153| | 55 | --TOXGR | Toxicity Grade | Char | Record Qualifier | A toxicity grade from NCI CTCAE |
 255| | 88 | --TOXGR | Toxicity Grade | Char | Record Qualifier |  |
~~~~

### R21. `ig34_p0441_a004` — r2:XDOC

- PDF 页 441 · 原子类型 LIST_ITEM · 所在节 `§9 [STUDY REFERENCES]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Identifiers for devices
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0441.txt` 第 4-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| The following situations have been identified thus far:
  4|      •     Identifiers for devices
  5|      •     Identifiers for non-host organisms
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:258` (来源: live valid_hits):

~~~~
 258| - Identifiers for devices
~~~~

### R22. `ig34_p0441_a005` — r2:XDOC

- PDF 页 441 · 原子类型 LIST_ITEM · 所在节 `§9 [STUDY REFERENCES]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Identifiers for non-host organisms
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0441.txt` 第 5-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  4|      •     Identifiers for devices
  5|      •     Identifiers for non-host organisms
  6| 
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:259` (来源: live valid_hits):

~~~~
 259| - Identifiers for non-host organisms
~~~~

### R23. `ig34_p0441_a006` — r2:XDOC

- PDF 页 441 · 原子类型 HEADING · 所在节 `§9 [STUDY REFERENCES]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
9.1 Device Identifiers
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0441.txt` 第 7-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| 
  7| 9.1 Device Identifiers
  8| The Device Identifiers (DI) dataset establishes identifiers for devices, which are used to populate the variable
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:261-261` (来源: fuzzy locate (score 0.75)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 261| ### 5.2.1 Device Identifiers Dataset (DI)
~~~~

### R24. `ig34_p0442_a001` — r2:XDOC

- PDF 页 442 · 原子类型 HEADING · 所在节 `§9 [STUDY REFERENCES]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
9.2 Non-host Organism Identifiers (OI)
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0442.txt` 第 1-6 行 (自动定位, 词覆盖 0.857; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  1| OI – Assumptions
  2|       1.     Non-host organisms include viruses and organisms such as pathogens or parasites, but also non-pathogenic
  3|              organisms such as normal intestinal flora. Non-host organism identifiers are not to be used for host species
  4|              identification (e.g., for animals used in preclinical studies), nor should they be used to represent other, non-
  5|              taxonomy characteristics of non-host species (e.g., drug susceptibility, growth rates).
  6|       2.     NHOID is sponsor-defined, with the following constraints:
  7|              a.   A unique NHOID must represent a unique identity as represented in its combination of
~~~~

KB 现文: `knowledge_base/model/05_study_level_data.md:299-299` (来源: fuzzy locate (score 0.857)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 299| ### 5.2.2 Non-host Organism Identifiers Dataset (OI)
~~~~

### R25. `sv20_p0004_a002` — r2:XDOC

- PDF 页 4 · 原子类型 HEADING · 所在节 `§1 [INTRODUCTION]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
1.1 Purpose
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0004.txt` 第 7-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  6| 1 Introduction
  7| 1.1 Purpose
  8| This document describes the Study Data Tabulation Model (SDTM), which defines a standard structure for study
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:5` (来源: live valid_hits):

~~~~
   5| ## 1.1 Purpose
~~~~

