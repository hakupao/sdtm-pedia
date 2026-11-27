# T4.1 补检包 1/8 — PRE_EXISTING (29 条, 全检, 不抽样)

> 由 `scripts/t4/t4_supp_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续.

### 1. `ig34_p0032_a013` — supp:PRE_EXISTING

- PDF 页 32 · 原子类型 SENTENCE · 所在节 `§4.2.7.1 "Specify" Values for Non-result Qualifier Variables`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
For example, consider a CRF that collects the indication for an analgesic concomitant medication (CMINDC) using a list of prespecified values and an "Other, specify" field :
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0032.txt` 第 18-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| on the sponsor's coding practice and analysis requirements.
 18| For example, consider a CRF that collects the indication for an analgesic concomitant medication (CMINDC) using
 19| a list of prespecified values and an "Other, specify" field :
 20| Indication for analgesic     o    Post-operative pain
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:423-423` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 423| For example, consider a CRF that collects the indication for an analgesic concomitant medication (CMINDC) using a list of prespecified values and an "Other, specify" field:
~~~~

### 2. `ig34_p0073_a001` — supp:PRE_EXISTING

- PDF 页 73 · 原子类型 TABLE_ROW · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[continuation CRACE01-04] | | | | "AMERICAN INDIAN OR ALASKA NATIVE". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ALASKA NATIVE; AMERICAN INDIAN; CARIBBEAN INDIAN; CENTRAL AMERICAN INDIAN; | | | checkbox |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0073.txt` 第 5-15 行 (自动定位, 词覆盖 0.853; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  4|                                                                                                                     Name
  5|                                                      "AMERICAN                              SUPPDM.QLABEL =
  6|                                                      INDIAN OR                              "Collected Race
  7|                                                      ALASKA                                 n" where n is the
  8|                                                      NATIVE". Check                         choice value.
  9|                                                      all that apply.
 10| If study participant answered: ASIAN
 11| CRACE05- 11            Which of the following Race   Select each       Text   SUPPDM.QVAL   For each value that     (RACEC)       ASIAN AMERICAN; ASIAN                           checkbox CRACE05-
 12| CRACE10                racial designations           value that                             applies,                              INDIAN;                                                  CRACE10
 13|                        best describes you?           applies if the                         SUPPDM.QVAL where                     BANGLADESHI; CHINESE;
 14|                                                      subject                                SUPPDM.QNAM                           JAPANESE; KOREAN;
 15|                                                      answered                               ="CRACEn" and
 16|                                                      "ASIAN". Check                         SUPPDM.QLABEL =
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:188-188` (来源: fuzzy locate (score 0.941)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 188| | CRACE01-CRACE04 | 10 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "AMERICAN INDIAN OR ALASKA NATIVE". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ALASKA NATIVE; AMERICAN INDIAN; CARIBBEAN INDIAN; CENTRAL AMERICAN INDIAN; | | | checkbox | |
~~~~

### 3. `ig34_p0076_a002` — supp:PRE_EXISTING

- PDF 页 76 · 原子类型 TABLE_HEADER · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
CDASH Variable | Order | Question Text | Prompt | CRF Completion Instructions | Type | SDTMIG Target Variable | SDTM Target Mapping | Controlled Terminology Code List Name | Pre-specified Value | Query Display Style | List | Hidden
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0076.txt` 第 2-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| CRF Metadata
  2| CDASH       Order Question Text        Prompt CRF             Type SDTMIG Target SDTM Target   Controlled    Permissible Values       Pre-      Query   List       Hidden
  3| Variable                                      Completion           Variable      Mapping       Terminology                            specified Display Style
  4|                                               Instructions                                     Code List                              Value
  5|                                                                                                Name
  6| RACE01      3      Which of the        Race    Study          Text   RACE                      (RACE)        AMERICAN INDIAN OR                         checkbox
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:178-178` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 178| | CDASH Variable | Order | Question Text | Prompt | CRF Completion Instructions | Type | SDTMIG Target Variable | SDTM Target Mapping | Controlled Terminology Code List Name | Permissible Values | Pre-specified Value | Query Display | List Style | Hidden |
~~~~

### 4. `ig34_p0101_a030` — supp:PRE_EXISTING

- PDF 页 101 · 原子类型 TABLE_ROW · 所在节 `§6.1.2 [Concomitant/Prior Medications (CM)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
7 | ABC | CM | ABC-0002 | 1 | ASPIRIN | 100 | mg | BID | 2004-01-07 | 2004-01-07
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0101.txt` 第 36-37 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 35| 6      ABC           CM       ABC-0001   6       ASPIRIN   100        mg          ONCE       2004-01-09   2004-01-09
 36| 7      ABC           CM       ABC-0002   1       ASPIRIN   100        mg          QD         2004-01-01   2004-01-03
 37| 8      ABC           CM       ABC-0002   2       ASPIRIN   100        mg          BID        2004-01-07   2004-01-07
 38| 
~~~~

KB 现文: `knowledge_base/domains/CM/examples.md:25-26` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  25| | 7 | ABC | CM | ABC-0002 | 1 | ASPIRIN | 100 | mg | QD | 2004-01-01 | 2004-01-03 |
  26| | 8 | ABC | CM | ABC-0002 | 2 | ASPIRIN | 100 | mg | BID | 2004-01-07 | 2004-01-07 |
~~~~

### 5. `ig34_p0123_a009` — supp:PRE_EXISTING

- PDF 页 123 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
X Snack | Nutritional drink | Meal | | 2015 Jun 03 | 14:15 | CE001
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 16-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15|                    Type                  If Nutritional Drink, Volume (ounces) Start Date    Start Time   Event ID
 16|  X Snack        Nutritional drink   Meal                                       2015 Jun 03   14:15        CE001
 17|    Snack X Nutritional drink        Meal 8 oz                                  2015 Sep 03   8:30         CE002
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:16-16` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  16| | [X] Snack | [ ] Nutritional drink | [ ] Meal | | 2015 Jun 03 | 14:15 | CE001 |
~~~~

### 6. `ig34_p0123_a010` — supp:PRE_EXISTING

- PDF 页 123 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Snack X Nutritional drink | Meal | 8 oz | 2015 Sep 03 | 8:30 | CE002
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 17-17 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 16|  X Snack        Nutritional drink   Meal                                       2015 Jun 03   14:15        CE001
 17|    Snack X Nutritional drink        Meal 8 oz                                  2015 Sep 03   8:30         CE002
 18|    Snack        Nutritional drink X Meal                                       2015 Dec 31   19:00        CE003
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:17-17` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  17| | [ ] Snack | [X] Nutritional drink | [ ] Meal | 8 oz | 2015 Sep 03 | 8:30 | CE002 |
~~~~

### 7. `ig34_p0123_a011` — supp:PRE_EXISTING

- PDF 页 123 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Snack | Nutritional drink | X Meal | | 2015 Dec 31 | 19:00 | CE003
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 18-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17|    Snack X Nutritional drink        Meal 8 oz                                  2015 Sep 03   8:30         CE002
 18|    Snack        Nutritional drink X Meal                                       2015 Dec 31   19:00        CE003
 19| Click here to add a row: ADD ROW
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:18-18` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  18| | [ ] Snack | [ ] Nutritional drink | [X] Meal | | 2015 Dec 31 | 19:00 | CE003 |
~~~~

### 8. `ig34_p0123_a016` — supp:PRE_EXISTING

- PDF 页 123 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Wild mushrooms | X Yes | No | 2015 DEC 24
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 25-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24|        Type          Occurrence If yes, Date
 25|  Wild mushrooms X Yes         No 2015 DEC 24
 26|  Ackee fruit           Yes X No
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:27-27` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  27| | Wild mushrooms | [X] Yes | [ ] No | 2015 DEC 24 |
~~~~

### 9. `ig34_p0123_a017` — supp:PRE_EXISTING

- PDF 页 123 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Ackee fruit | Yes | X No | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 26-26 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25|  Wild mushrooms X Yes         No 2015 DEC 24
 26|  Ackee fruit           Yes X No
 27|  Cycad seeds           Yes X No
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:28-28` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  28| | Ackee fruit | [ ] Yes | [X] No | |
~~~~

### 10. `ig34_p0123_a018` — supp:PRE_EXISTING

- PDF 页 123 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Cycad seeds | Yes | X No | |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0123.txt` 第 27-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26|  Ackee fruit           Yes X No
 27|  Cycad seeds           Yes X No
 28| 
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:29-29` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  29| | Cycad seeds | [ ] Yes | [X] No | |
~~~~

### 11. `ig34_p0141_a005` — supp:PRE_EXISTING

- PDF 页 141 · 原子类型 TABLE_ROW · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | ABC123 | AE | 123101 | 3 | PULMONARY EMBOLISM | | Pulmonary embolism | Vascular disorders | MODERATE | Y | DOSE REDUCED | PROBABLY NOT RELATED | RECOVERING/ RESOLVING | | Y | Y | | | | TREATMENT | 2005-10-21 | | 9 | | AFTER |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0141.txt` 第 9-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8|                                             HOURS                               tissue disorders
  9| 3     ABC123    AE       123101    3        PULMONARY               Pulmonary   Vascular           MODERATE    Y        DOSE           PROBABLY     RECOVERING/                                   Y         Y                   TREATMENT   2005-10-                9                      AFTER
 10|                                             EMBOLISM                embolism    disorders                               REDUCED        NOT          RESOLVING                                                                               21
 11|                                                                                                                                        RELATED
 12| 
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:17-17` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  17| | 3 | ABC123 | AE | 123101 | 3 | PULMONARY EMBOLISM | | Pulmonary embolism | Vascular disorders | MODERATE | Y | DOSE REDUCED | PROBABLY NOT RELATED | RECOVERING/RESOLVING | | | | Y | Y | | TREATMENT | 2005-10-21 | | 9 | | AFTER |
~~~~

### 12. `ig34_p0141_a013` — supp:PRE_EXISTING

- PDF 页 141 · 原子类型 TABLE_ROW · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC123 | AE | 123101 | 2 | VOMITING | Vomiting | Y | Gastrointestinal disorders | MODERATE | N | DOSE REDUCED | RELATED | RECOVERED/RESOLVED | TREATMENT | 2005-10-13T13:00 | 2005-10-19:00 | 3 | 3 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0141.txt` 第 23-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 22|                                                                          disorders
 23| 2     ABC123       AE       123101     2        VOMITING Vomiting Y      Gastrointestinal                          MODERATE N                 DOSE REDUCED        RELATED               RECOVERED/RESOLVED TREATMENT 2005-10-                          2005-10-          3             3
 24|                                                                          disorders                                                                                                                                   13T13:00                          13T19:00
 25| 3     ABC123       AE       123101     3        HEADACHE Headache        Nervous system                            MILD           N           DOSE NOT            POSSIBLY              RECOVERED/RESOLVED TREATMENT 2005-10-21                        2005-10-21        11            11
 26|                                                                          disorders                                                            CHANGED             RELATED
 27| 
 28| Example 3
 29| In this example, a CRF module that asked whether or not nausea, vomiting, or diarrhea occurred was included in the study only once. In the context of this study, the conditions that occurred were reportable as
 30| adverse events. No additional data about these events was collected. No other AE information was collected via general questions. The responses to the probing questions "Yes", "No", or "Not Done" were
 31| represented in the FA domain (see Section 6.4, Findings About Events or Interventions). This is an example of unusually sparse AE data collection; the AE dataset is populated with the term and the flag indicating
 32| that it was prespecified, but timing information is limited to the date of collection, and other expected qualifiers are not available. RELREC may be used to relate AE records and FA records.
 33| The subject shown in this example experienced nausea and vomiting. The subject did not experience diarrhea, so no record for that term exists in the AE dataset.
 34| ae.xpt
 35| Row      STUDYID     DOMAIN       USUBJID     AESEQ     AETERM       AEDECOD         AEPRESP        AEBODSYS                          AESER     AEACN    AEREL     AEDTC         AESTDTC         AEENDTC        AEDY
 36| 1        ABC123      AE           123101      1         NAUSEA       Nausea          Y              Gastrointestinal disorders                                     2005-10-29                                   19
 37| 2        ABC123      AE           123101      2         VOMITING     Vomiting        Y              Gastrointestinal disorders                                     2005-10-29                                   19
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:32-32` (来源: fuzzy locate (score 0.955)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  32| | 2 | ABC123 | AE | 123101 | 2 | VOMITING | Vomiting | Y | Gastrointestinal disorders | MODERATE | N | DOSE REDUCED | RELATED | RECOVERED/RESOLVED | TREATMENT | 2005-10-13T13:00 | 2005-10-13T19:00 | 3 | 3 |
~~~~

### 13. `ig34_p0146_a003` — supp:PRE_EXISTING

- PDF 页 146 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC134 | BS | 43871 | 1 | | 1148.267 | VOLUME | Volume | SPECIMEN MEASUREMENT | | | cm3 | | cm3 | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0146.txt` 第 3-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| Row STUDYID DOMAIN USUBJID BSSEQ BSGRPID BSREFID BSTESTCD BSTEST                               BSCAT                BSORRES           BSORRESU BSSTRESC              BSSTRESN BSSTRESU BSSPEC BSANTREG          VISITNUM BSDTC
  3| 1   ABC134  BS     43871   1             1148.267 VOLUME  Volume                               SPECIMEN             2                 cm3      2                     2        cm3      BRAIN  CEREBRAL          1        2005-03-
  4|                                                                                                MEASUREMENT                                                                                    AQUEDUCT                   20
  5| 2     ABC134       BS       43871   2       267FF    1148.267    TEMP       Temperature        SPECIMEN HANDLING    -80               C         -80                  -80      C        BRAIN  CEREBRAL          1        2005-03-
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:41-41` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  41| | 1 | ABC134 | BS | 43871 | 1 | | 1148.267 | VOLUME | Volume | SPECIMEN MEASUREMENT | 2 | cm3 | 2 | 2 | cm3 | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |
~~~~

### 14. `ig34_p0146_a004` — supp:PRE_EXISTING

- PDF 页 146 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC134 | BS | 43871 | 2 | 267FF | 1148.267 | TEMP | Temperature | SPECIMEN HANDLING | -80 | C | -80 | | C | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0146.txt` 第 4-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3| 1   ABC134  BS     43871   1             1148.267 VOLUME  Volume                               SPECIMEN             2                 cm3      2                     2        cm3      BRAIN  CEREBRAL          1        2005-03-
  4|                                                                                                MEASUREMENT                                                                                    AQUEDUCT                   20
  5| 2     ABC134       BS       43871   2       267FF    1148.267    TEMP       Temperature        SPECIMEN HANDLING    -80               C         -80                  -80      C        BRAIN  CEREBRAL          1        2005-03-
  6|                                                                                                                                                                                               AQUEDUCT                   20
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:42-42` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  42| | 2 | ABC134 | BS | 43871 | 2 | 267FF | 1148.267 | TEMP | Temperature | SPECIMEN HANDLING | -80 | C | -80 | -80 | C | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |
~~~~

### 15. `ig34_p0146_a030` — supp:PRE_EXISTING

- PDF 页 146 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | 3441271 | BE | MU-298 | PURKIT | 4 | 298R1-R0 | Extracting | EXTRACTING | ABC LAB | | EXTRACTION | 2 | 2010-04-01T11:50 | 2010-04-02T9:00 | 2010-04-05T13:50 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0146.txt` 第 39-39 行 (自动定位, 词覆盖 0.95; 版式以原 PDF 为准):

~~~~
 38| 3        3441271     BE        MU-298                3          298B1-1     Shipping       SHIPPING     ABC LAB               TRANSPORT     2          2010-04-01T11:50   2010-04-01T15:00   2010-04-02T8:00
 39| 4        3441271     BE        MU-298    PURKIT      4          298R1-1R0   Extracting     EXTRACTING   ABC LAB               EXTRACTION    2          2010-04-01T11:50   2010-04-02T9:00    2010-04-05T13:50
 40| 5        3441271     BE        MU-298                5          298R1-1R1   Aliquoting     ALIQUOTING   ABC LAB               PREPARATION   2          2010-04-01T11:50   2010-04-05T13:50
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:85-85` (来源: fuzzy locate (score 0.95)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  85| | 4 | 3441271 | BE | MU-298 | PURKIT | 4 | 298R1-1R0 | Extracting | EXTRACTING | ABC LAB | | EXTRACTION | 2 | 2010-04-01T11:50 | 2010-04-02T9:00 | 2010-04-05T13:50 |
~~~~

### 16. `ig34_p0147_a024` — supp:PRE_EXISTING

- PDF 页 147 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | 3441271 | BS | MU-298 | 2 | 298B1 | VOLUME | Volume | SPECIMEN MEASUREMENT | 7 | mL | | | mL | PLASMA | 2 | 2010-04-01T11:50 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0147.txt` 第 29-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| 1        3441271   BS        MU-298       1        298B1         VOLUME       Volume                 SPECIMEN MEASUREMENT         12        mL            6               6           mL            BLOOD        2          2010-04-01T11:50
 29| 2        3441271   BS        MU-298       2        298B1-1       VOLUME       Volume                 SPECIMEN MEASUREMENT         7         mL            6               6           mL            PLASMA       2          2010-04-01T11:50
 30| 3        3441271   BS        MU-298       3        298B1-1R0     VOLUME       Volume                 SPECIMEN MEASUREMENT         6         mL            6               6           mL            RNA          2          2010-04-01T11:50
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:123-123` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 123| | 2 | 3441271 | BS | MU-298 | 2 | 298B1-1 | VOLUME | Volume | SPECIMEN MEASUREMENT | 7 | mL | 6 | 6 | mL | PLASMA | 2 | 2010-04-01T11:50 |
~~~~

### 17. `ig34_p0147_a025` — supp:PRE_EXISTING

- PDF 页 147 · 原子类型 TABLE_ROW · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | 3441271 | BS | MU-298 | 3 | 298R1-1R0 | VOLUME | Volume | SPECIMEN MEASUREMENT | 6 | mL | | | mL | RNA | 2 | 2010-04-01T11:50 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0147.txt` 第 30-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 29| 2        3441271   BS        MU-298       2        298B1-1       VOLUME       Volume                 SPECIMEN MEASUREMENT         7         mL            6               6           mL            PLASMA       2          2010-04-01T11:50
 30| 3        3441271   BS        MU-298       3        298B1-1R0     VOLUME       Volume                 SPECIMEN MEASUREMENT         6         mL            6               6           mL            RNA          2          2010-04-01T11:50
 31| 4        3441271   BS        MU-298       4        298B1-1R0     RIN          RNA Integrity Number   QUALITY CONTROL              9.3                     9.3             9.3                       RNA          2          2010-04-01T11:50
 32| 5        3441271   BS        MU-298       5        298R1-1R1     VOLUME       Volume                 SPECIMEN MEASUREMENT         2         mL            2               2           mL            RNA          2          2010-04-01T11:50
 33| 6        3441271   BS        MU-298       6        298R1-1R2     VOLUME       Volume                 SPECIMEN MEASUREMENT         2         mL            2               2           mL            RNA          2          2010-04-01T11:50
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:124-124` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 124| | 3 | 3441271 | BS | MU-298 | 3 | 298R1-1R0 | VOLUME | Volume | SPECIMEN MEASUREMENT | 6 | mL | 6 | 6 | mL | RNA | 2 | 2010-04-01T11:50 |
~~~~

### 18. `ig34_p0153_a0002` — supp:PRE_EXISTING

- PDF 页 153 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Which fracture? | o Pre-study fracture, reference number____ |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0153.txt` 第 2-2 行 (自动定位, 词覆盖 0.857; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  1| Bone Fracture Assessment
  2| Which fracture?                                               ○ Pre-study fracture, reference number_____
  3|                                                               ○ On-study fracture, reference number_____
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:74-74` (来源: fuzzy locate (score 0.857)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  74| | Which fracture? | ○ Pre-study fracture, reference number ___  ○ On-study fracture, reference number ___ |
~~~~

### 19. `ig34_p0182_a007` — supp:PRE_EXISTING

- PDF 页 182 · 原子类型 TABLE_ROW · 所在节 `§6.3.1 Product Accountability (DA)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC | DA | ABC-01001 | 2 | XBYCC-E990A | A375827 | RETAMT | Returned Amount | Study Medication | Bottle A | 5 | | TABLET | 5 | | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0182.txt` 第 8-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7| 1     ABC          DA       ABC-01001   1       XBYCC-E990A     A375827   DISPAMT     Dispensed Amount    Study Medication    Bottle A   30        TABLET     30         30         TABLET      1          Study Med Period 1   2004-06-15
  8| 2     ABC          DA       ABC-01001   2       XBYCC-E990A     A375827   RETAMT      Returned Amount     Study Medication    Bottle A   5         TABLET     5          5          TABLET      2          Study Med Period 1   2004-07-15
  9| 3     ABC          DA       ABC-01001   3       XBYCC-E990B     A227588   DISPAMT     Dispensed Amount    Study Medication    Bottle B   15        TABLET     15         15         TABLET      1          Study Med Period 1   2004-06-15
~~~~

KB 现文: `knowledge_base/domains/DA/examples.md:12-12` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  12| | 2 | ABC | DA | ABC-01001 | 2 | XBYCC-E990A | A375827 | RETAMT | Returned Amount | Study Medication | Bottle A | 5 | TABLET | 5 | 5 | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
~~~~

### 20. `ig34_p0182_a009` — supp:PRE_EXISTING

- PDF 页 182 · 原子类型 TABLE_ROW · 所在节 `§6.3.1 Product Accountability (DA)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | ABC | DA | ABC-01001 | 4 | XBYCC-E990B | A227588 | RETAMT | Returned Amount | Study Medication | Bottle B | 10 | | TABLET | 10 | | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0182.txt` 第 10-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9| 3     ABC          DA       ABC-01001   3       XBYCC-E990B     A227588   DISPAMT     Dispensed Amount    Study Medication    Bottle B   15        TABLET     15         15         TABLET      1          Study Med Period 1   2004-06-15
 10| 4     ABC          DA       ABC-01001   4       XBYCC-E990B     A227588   RETAMT      Returned Amount     Study Medication    Bottle B   0         TABLET     0          0          TABLET      2          Study Med Period 1   2004-07-15
 11| 5     ABC          DA       ABC-01001   5                                 DISPAMT     Dispensed Amount    Rescue Medication              10        TABLET     10         10         TABLET      1          Study Med Period 1   2004-06-15
 12| 6     ABC          DA       ABC-01001   6                                 RETAMT      Returned Amount     Rescue Medication              10        TABLET     10         10         TABLET      2          Study Med Period 1   2004-07-15
~~~~

KB 现文: `knowledge_base/domains/DA/examples.md:14-15` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  14| | 4 | ABC | DA | ABC-01001 | 4 | XBYCC-E990B | A227588 | RETAMT | Returned Amount | Study Medication | Bottle B | 0 | TABLET | 0 | 0 | TABLET | 2 | Study Med Period 1 | 2004-07-15 |
  15| | 5 | ABC | DA | ABC-01001 | 5 | | | DISPAMT | Dispensed Amount | Rescue Medication | | 10 | TABLET | 10 | 10 | TABLET | 1 | Study Med Period 1 | 2004-06-15 |
~~~~

### 21. `ig34_p0182_a016` — supp:PRE_EXISTING

- PDF 页 182 · 原子类型 TABLE_ROW · 所在节 `§6.3.1 Product Accountability (DA)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC | DA | ABC-01001 | 1 | AB001 | DISPAMT | Dispensed Amount | Study Medication | Drug A | 1 | | CONTAINER | 1 | | | 1 | 2004-06-15 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0182.txt` 第 19-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18| Row STUDYID DOMAIN USUBJID   DASEQ DASPID DATESTCD DATEST                              DACAT              DASCAT DAORRES DAORRESU           DASTRESC DASTRESN DASTRESU       VISITNUM DADTC
 19| 1   ABC     DA     ABC-01001 1     AB001  DISPAMT  Dispensed Amount                    Study Medication   Drug A 1       CONTAINER          1        1        CONTAINER      1        2004-06-15
 20| 2   ABC     DA     ABC-01001 2     AB002  DISPAMT  Dispensed Amount                    Study Medication   Drug B 1       CONTAINER          1        1        CONTAINER      1        2004-06-15
~~~~

KB 现文: `knowledge_base/domains/DA/examples.md:26-26` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  26| | 1 | ABC | DA | ABC-01001 | 1 | AB001 | DISPAMT | Dispensed Amount | Study Medication | Drug A | 1 | CONTAINER | 1 | 1 | CONTAINER | 1 | 2004-06-15 |
~~~~

### 22. `ig34_p0182_a017` — supp:PRE_EXISTING

- PDF 页 182 · 原子类型 TABLE_ROW · 所在节 `§6.3.1 Product Accountability (DA)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC | DA | ABC-01001 | 2 | AB002 | DISPAMT | Dispensed Amount | Study Medication | Drug B | 1 | | CONTAINER | 1 | | | 1 | 2004-06-15 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0182.txt` 第 20-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19| 1   ABC     DA     ABC-01001 1     AB001  DISPAMT  Dispensed Amount                    Study Medication   Drug A 1       CONTAINER          1        1        CONTAINER      1        2004-06-15
 20| 2   ABC     DA     ABC-01001 2     AB002  DISPAMT  Dispensed Amount                    Study Medication   Drug B 1       CONTAINER          1        1        CONTAINER      1        2004-06-15
 21| 
~~~~

KB 现文: `knowledge_base/domains/DA/examples.md:27-27` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  27| | 2 | ABC | DA | ABC-01001 | 2 | AB002 | DISPAMT | Dispensed Amount | Study Medication | Drug B | 1 | CONTAINER | 1 | 1 | CONTAINER | 1 | 2004-06-15 |
~~~~

### 23. `ig34_p0182_a025` — supp:PRE_EXISTING

- PDF 页 182 · 原子类型 TABLE_ROW · 所在节 `§6.3.1 Product Accountability (DA)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC | DA | 101 | 1 | | | PREPAMT | Prepared Amount | Study Product | 100 | mL | | 100 | mL | 2017-05-19 | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0182.txt` 第 29-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| Row      STUDYID   DOMAIN   USUBJID     DASEQ   DAGRPID    DASPID   DATESTCD      DATEST             DACAT           DAORRES     DAORRESU    DASTRESC   DASTRESN   DASTRESU    DADTC        DADY
 29| 1        ABC       DA       101         1       1          1        PREPAMT       Prepared Amount    Study Product   100         mL          100        100        mL          2017-05-19   1
 30| 2        ABC       DA       101         2       1          1        REMAMT        Remaining Amount   Study Product   15          mL          15         15         mL          2017-05-19   1
~~~~

KB 现文: `knowledge_base/domains/DA/examples.md:43-43` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | 1 | ABC | DA | 101 | 1 | 1 | 1 | PREPAMT | Prepared Amount | Study Product | 100 | mL | 100 | 100 | mL | 2017-05-19 | 1 |
~~~~

### 24. `ig34_p0182_a026` — supp:PRE_EXISTING

- PDF 页 182 · 原子类型 TABLE_ROW · 所在节 `§6.3.1 Product Accountability (DA)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC | DA | 101 | 2 | | | REMAMT | Remaining Amount | Study Product | 15 | mL | | 15 | mL | 2017-05-19 | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0182.txt` 第 30-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 29| 1        ABC       DA       101         1       1          1        PREPAMT       Prepared Amount    Study Product   100         mL          100        100        mL          2017-05-19   1
 30| 2        ABC       DA       101         2       1          1        REMAMT        Remaining Amount   Study Product   15          mL          15         15         mL          2017-05-19   1
 31| 3        ABC       DA       101         3       2          2        PREPAMT       Prepared Amount    Study Product   100         mL          100        100        mL          2017-05-19   1
~~~~

KB 现文: `knowledge_base/domains/DA/examples.md:44-44` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  44| | 2 | ABC | DA | 101 | 2 | 1 | 1 | REMAMT | Remaining Amount | Study Product | 15 | mL | 15 | 15 | mL | 2017-05-19 | 1 |
~~~~

### 25. `ig34_p0182_a028` — supp:PRE_EXISTING

- PDF 页 182 · 原子类型 TABLE_ROW · 所在节 `§6.3.1 Product Accountability (DA)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | ABC | DA | 101 | 4 | 2 | | REMAMT | Remaining Amount | Study Product | 25 | mL | | 25 | 25 | mL | 2017-05-19 | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0182.txt` 第 32-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| 3        ABC       DA       101         3       2          2        PREPAMT       Prepared Amount    Study Product   100         mL          100        100        mL          2017-05-19   1
 32| 4        ABC       DA       101         4       2          2        REMAMT        Remaining Amount   Study Product   25          mL          25         25         mL          2017-05-19   1
 33| 5        ABC       DA       101         5       3          1        PREPAMT       Prepared Amount    Study Product   100         mL          100        100        mL          2017-05-20   2
~~~~

KB 现文: `knowledge_base/domains/DA/examples.md:46-46` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  46| | 4 | ABC | DA | 101 | 4 | 2 | 2 | REMAMT | Remaining Amount | Study Product | 25 | mL | 25 | 25 | mL | 2017-05-19 | 1 |
~~~~

### 26. `ig34_p0190_a014` — supp:PRE_EXISTING

- PDF 页 190 · 原子类型 TABLE_ROW · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 12 | XYZ | EG | XYZ-US-701-002 | 12 | 334PT89 | INTP | Interpretation | | SUPINE | ABNORMAL | | ABNORMAL | | | | | | | | 1 | Screening | 2003-04-15T11:58 | -36 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0190.txt` 第 26-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25|                                                                                                                 PLACEMENT                         PLACEMENT
 26| 12    XYZ       EG       XYZ-US-   12      334PT89   INTP        Interpretation                        SUPINE   ABNORMAL                          ABNORMAL                                                                                           1          Screening   2003-04-    -36
 27|                          701-002                                                                                                                                                                                                                                1           15T11:58
 28| 
~~~~

KB 现文: `knowledge_base/domains/EG/examples.md:36-36` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  36| | 12 | XYZ | EG | XYZ-US-701-002 | 12 | 334PT89 | INTP | Interpretation | | SUPINE | ABNORMAL | | ABNORMAL | | | | | | | | 1 | Screening 1 | 2003-04-15T11:58 | -36 |
~~~~

### 27. `ig34_p0191_a001` — supp:PRE_EXISTING

- PDF 页 191 · 原子类型 TABLE_ROW · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | STUDY01 | EG | 2324-P0001 | 4 | .. | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 440 | msec | 440 | 440 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | .. | 1 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0191.txt` 第 2-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Row STUDYID DOMAIN USUBJID         EGSEQ … EGTESTCD EGTEST                EGCAT    EGPOS EGORRES EGORRESU EGSTRESC EGSTRESN EGSTRESU EGMETHOD    EGLEAD EGLOBXFL VISITNUM VISIT   EGDTC         EGTPT … EGREPNUM
  2| 4   STUDY01 EG     2324-           4     … QTAG     QT Interval,          INTERVAL SUPINE 440    msec     440      440      msec     12 LEAD     LEAD II         2        VISIT   2014-03-      1 HR  … 1
  3|                    P0001                            Aggregate                                                                        STANDARD                             2       22T10:00:21
  4| 5   STUDY01 EG     2324-           5     … PRAG     PR Interval,          INTERVAL SUPINE 176    msec     176      176      msec     12 LEAD     LEAD II         2        VISIT   2014-03-      1 HR     … 2
~~~~

KB 现文: `knowledge_base/domains/EG/examples.md:67-67` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  67| | 4 | STUDY01 | EG | 2324-P0001 | 4 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 440 | msec | 440 | 440 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:00:21 | 1 HR | ... | 1 |
~~~~

### 28. `ig34_p0191_a003` — supp:PRE_EXISTING

- PDF 页 191 · 原子类型 TABLE_ROW · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 6 | STUDY01 | EG | 2324-P0001 | 6 | .. | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 679 | msec | 679 | 679 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | .. | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0191.txt` 第 5-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  4| 5   STUDY01 EG     2324-           5     … PRAG     PR Interval,          INTERVAL SUPINE 176    msec     176      176      msec     12 LEAD     LEAD II         2        VISIT   2014-03-      1 HR     … 2
  5|                    P0001                            Aggregate                                                                        STANDARD                             2       22T10:01:35
  6| 6   STUDY01 EG     2324-           6     … RRAG     RR Interval,          INTERVAL SUPINE 679    msec     679      679      msec     12 LEAD     LEAD II         2        VISIT   2014-03-      1 HR     … 2
  7|                    P0001                            Aggregate                                                                        STANDARD                             2       22T10:01:35
~~~~

KB 现文: `knowledge_base/domains/EG/examples.md:69-69` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  69| | 6 | STUDY01 | EG | 2324-P0001 | 6 | ... | RRAG | RR Interval, Aggregate | INTERVAL | SUPINE | 679 | msec | 679 | 679 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
~~~~

### 29. `ig34_p0191_a005` — supp:PRE_EXISTING

- PDF 页 191 · 原子类型 TABLE_ROW · 所在节 `§6.3.3 ECG Test Results (EG)`
- triage 类 **-** · 终态 **EXACT** (T3 前 EXACT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 8 | STUDY01 | EG | 2324-P0001 | 8 | .. | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 389 | msec | 389 | 389 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | .. | 2 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0191.txt` 第 9-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8| 7   STUDY01 EG     2324-           7     … QRSAG    QRS Duration,         INTERVAL SUPINE 95     msec     95       95       msec     12 LEAD     LEAD II         2        VISIT   2014-03-      1 HR     … 2
  9|                    P0001                            Aggregate                                                                        STANDARD                             2       22T10:01:35
 10| 8   STUDY01 EG     2324-           8     … QTAG     QT Interval,          INTERVAL SUPINE 389    msec     389      389      msec     12 LEAD     LEAD II         2        VISIT   2014-03-      1 HR     … 2
 11|                    P0001                            Aggregate                                                                        STANDARD                             2       22T10:01:35
~~~~

KB 现文: `knowledge_base/domains/EG/examples.md:71-71` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  71| | 8 | STUDY01 | EG | 2324-P0001 | 8 | ... | QTAG | QT Interval, Aggregate | INTERVAL | SUPINE | 389 | msec | 389 | 389 | msec | 12 LEAD STANDARD | LEAD II | | 2 | VISIT 2 | 2014-03-22T10:01:35 | 1 HR | ... | 2 |
~~~~

