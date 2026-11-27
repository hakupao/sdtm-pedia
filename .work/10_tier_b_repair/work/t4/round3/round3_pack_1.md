# T4.1 第三轮补检包 1 — R3_IG34_EQUIV (25 条; 编号 T1-T25)

> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).

### T1. `ig34_p0046_a017` — r3:R3_IG34_EQUIV

- PDF 页 46 · 原子类型 CODE_LITERAL · 所在节 `§4.4.10 [Representing Time Points]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
PT30M
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0046.txt` 第 25-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 24| VSTPTNUM     VSTPT    VSELTM       VSTPTREF                VSRFTDTC               VSDTC
 25| 1            30 MIN   PT30M        DOSE ADMINISTRATION     2006-08-01T08:00       2006-08-01T08:30
 26| 2            60 MIN   PT1H         DOSE ADMINISTRATION     2006-08-01T08:00       2006-08-01T09:01
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1097` (来源: live valid_hits):

~~~~
1097| | 1 | 30 MIN | PT30M | DOSE ADMINISTRATION | 2006-08-01T08:00 | 2006-08-01T08:30 |
~~~~

### T2. `ig34_p0046_a021` — r3:R3_IG34_EQUIV

- PDF 页 46 · 原子类型 CODE_LITERAL · 所在节 `§4.4.10 [Representing Time Points]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
PT1H30M
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0046.txt` 第 27-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26| 2            60 MIN   PT1H         DOSE ADMINISTRATION     2006-08-01T08:00       2006-08-01T09:01
 27| 3            90 MIN   PT1H30M      DOSE ADMINISTRATION     2006-08-01T08:00       2006-08-01T09:32
 28| 
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1099` (来源: live valid_hits):

~~~~
1099| | 3 | 90 MIN | PT1H30M | DOSE ADMINISTRATION | 2006-08-01T08:00 | 2006-08-01T09:32 |
~~~~

### T3. `ig34_p0073_a014` — r3:R3_IG34_EQUIV

- PDF 页 73 · 原子类型 CODE_LITERAL · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
dm.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0073.txt` 第 42-42 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 41| 
 42| The value of RACE is used to represent the high-level racial designation as a single collected value per CDISC Controlled Terminology in dm.xpt. When more
 43| than 1 choice is selected, the value is represented with "MULTIPLE" as shown in this example. Note: Only those variables relevant to this example are shown.
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:5,30,74` (来源: live valid_hits):

~~~~
   5| **dm.xpt**
  30| **dm.xpt**
  74| **dm.xpt**
~~~~

### T4. `ig34_p0075_a015` — r3:R3_IG34_EQUIV

- PDF 页 75 · 原子类型 CODE_LITERAL · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
CRACE05-CRACE10
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0074.txt` 第 14-14 行 (自动定位, 词覆盖 0.5; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 13| 3     ABC789    DM         ABC789-010-047                          CRACE8      Collected Race 8     CHINESE     CRF
 14| 4     ABC789    DM         ABC789-010-047                          CRACE10     Collected Race 10    KOREAN      CRF
 15| 5     ABC789    DM         ABC789-010-047                          CRACE21     Collected Race 21    RUSSIAN     CRF
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:170,190,190` (来源: live valid_hits):

~~~~
 170| > If the study participant answered ASIAN, subcategories (CRACE05-CRACE10) are presented: ASIAN AMERICAN, ASIAN INDIAN, BANGLADESHI, CHINESE, JAPANESE, KOREAN.
 190| | CRACE05-CRACE10 | 11 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "ASIAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ASIAN AMERICAN; ASIAN INDIAN; BANGLADESHI; CHINESE; JAPANESE; KOREAN; | | | checkbox | CRACE05-CRACE10 |
~~~~

### T5. `ig34_p0116_a008` — r3:R3_IG34_EQUIV

- PDF 页 116 · 原子类型 CODE_LITERAL · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ec.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0116.txt` 第 10-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  9| The EC dataset shows administrations as collected.
 10| ec.xpt
 11| Row STUDYID DOMAIN USUBJID ECSEQ ECTRT                 ECPRESP ECOCCUR ECDOSE ECDOSU                  ECDOSFRM          ECDOSFRQ ECROUTE EPOCH       ECSTDTC    ECENDTC    ECSTDY ECENDY ECTPT        ECELTM ECTPTREF
~~~~

KB 现文: `knowledge_base/domains/EC/examples.md:3` (来源: live valid_hits):

~~~~
   3| > See [EX Examples](../EX/examples.md) for this example set (SDTMIG v3.4 §6.1.3.3 Exposure/Exposure as Collected Examples, Examples 1-8, including all ec.xpt tables).
~~~~

### T6. `ig34_p0124_a014` — r3:R3_IG34_EQUIV

- PDF 页 124 · 原子类型 CODE_LITERAL · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ml.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0124.txt` 第 32-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| The dataset below shows the food-card data collected for the first 3 weeks for a subject.
 32| ml.xpt
 33| Row      STUDYID        DOMAIN   USUBJID        MLSEQ      MLTRT                                VISITNUM     VISIT      MLSTDTC
~~~~

KB 现文: `knowledge_base/domains/ML/examples.md:37,61` (来源: live valid_hits):

~~~~
  37| **ml.xpt**
  61| **ml.xpt**
~~~~

### T7. `ig34_p0142_a013` — r3:R3_IG34_EQUIV

- PDF 页 142 · 原子类型 CODE_LITERAL · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ae.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0142.txt` 第 1-1 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| ae.xpt
  2| Row        STUDYID     DOMAIN       USUBJID      AESEQ    AEGRPID AETERM                     AEBODSYS                      AESEV         AESER     AEACN                    AEREL                      AESTDTC      AEENDTC
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:11,27,41` (来源: live valid_hits):

~~~~
  11| **ae.xpt**
  27| **ae.xpt**
  41| **ae.xpt**
~~~~

### T8. `ig34_p0228_a004` — r3:R3_IG34_EQUIV

- PDF 页 228 · 原子类型 CODE_LITERAL · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
gf.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0228.txt` 第 6-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5|                 (lysine).
  6| gf.xpt
  7| Row STUDYID DOMAIN USUBJID GFSEQ GFREFID     NHOID                      GFLNKID   GFTESTCD GFTEST                  GFTSTDTL                   GFORRES GFSTRESC GFSYM GFGENLOC GFSEQID GFSPEC GFMETHOD VISITNUM VISIT    GFDTC
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:25,60,84` (来源: live valid_hits):

~~~~
  25| **gf.xpt**
  60| **gf.xpt**
  84| **gf.xpt**
~~~~

### T9. `ig34_p0234_a020` — r3:R3_IG34_EQUIV

- PDF 页 234 · 原子类型 CODE_LITERAL · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
is.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0234.txt` 第 5-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  4|                ADA that bind to endogenous molecules, leading to diminished or negated function; in some cases, they may also bind and negate the function of the study drug. They are a subset of the total ADAs.
  5| is.xpt
  6| Row STUDYID DOMAIN USUBJID ISSEQ       ISREFID ISGRPID ISTESTCD ISTEST           ISBDAGNT        ISTSTOPO ISCAT          ISSCAT      ISORRES      ISORRESU ISSTRESC ISSTRESN     ISSTRESU    ISSPEC    ISMETHOD                      VISITNUM VISIT    ISDTC
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:15,38,60` (来源: live valid_hits):

~~~~
  15| **is.xpt**
  38| **is.xpt**
  60| **is.xpt**
~~~~

### T10. `ig34_p0248_a006` — r3:R3_IG34_EQUIV

- PDF 页 248 · 原子类型 CODE_LITERAL · 所在节 `§6.3.5.6 Laboratory Test Results (LB)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
lb.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0248.txt` 第 6-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5| Row 3:             Shows the quantification of the cannabinoids.
  6| lb.xpt
  7| Row STUDYID DOMAIN USUBJID            LBGRPID LBSEQ LBTESTCD LBTEST       LBTSTOPO LBCAT                      LBORRES LBORRESU LBSTRESC LBSTRESN LBSTRESU LBLOINC LBSPEC LBMETHOD                            LBLOBXFL LBDTC        VISITNUM VISIT
~~~~

KB 现文: `knowledge_base/domains/LB/examples.md:20,50,65` (来源: live valid_hits):

~~~~
  20| **lb.xpt**
  50| **lb.xpt**
  65| **lb.xpt**
~~~~

### T11. `ig34_p0254_a002` — r3:R3_IG34_EQUIV

- PDF 页 254 · 原子类型 CODE_LITERAL · 所在节 `§6.3.5.7.2 Microbiology Susceptibility (MS)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
MSNAM
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0254.txt` 第 4-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3|                                               or Format1
  4| MSNAM          Laboratory/Vendor         Char                     Record      Name or identifier of the vendor (e.g., laboratory) that provided the test results.                          Perm
  5|                Name                                               Qualifier
~~~~

KB 现文: `knowledge_base/domains/MS/examples.md:11,21` (来源: live valid_hits):

~~~~
  11| After E. faecalis was identified in the subject sample, drug susceptibility testing was performed at each of the labs using both the sponsor's investigational drug and amoxicillin. Because an identified organism is the subject of the test, the NHOID variable is populated with "ENTEROCOCCUS FAECALIS". Between the 2 labs (MSNAM), a total of 3 susceptibility testing methods were used: epsilometer, disk diffusion, and macro broth dilution (MSMETHOD). Epsilometer and disk diffusion both use agar diffusion methods, in which an agar plate is inoculated with the microorganism of interest and either a strip (epsilometer) or discs (disk diffusion) containing various concentrations of the drug are placed on the agar plate. The epsilometer test method provides both a minimum inhibitory concentration (MSTESTCD = "MIC"), the lowest concentration of a drug that inhibits the growth of a microorganism, and a qualitative interpretation (MSTESTCD = "MICROSUS") such as susceptible, intermediate, or resistant. The disk diffusion test method provides the diameter of the zone of inhibition (MSTESTCD = "DIAZOINH") and a qualitative interpretation such as susceptible, intermediate, or resistant (MSTESTCD = " MICROSUS" ). The quantitative and qualitative results are grouped together using MSGRPID.
  21| | Row | STUDYID | DOMAIN | USUBJID | NHOID | MSGRPID | MSSEQ | MSREFID | MSLNKGRP | MSTESTCD | MSTEST | MSAGENT | MSCONC | MSCONCU | MSORRES | MSORRESU | MSSTRESC | MSSTRESN | MSSTRESU | MSNAM | MSMETHOD | MSDTC |
~~~~

### T12. `ig34_p0263_a007` — r3:R3_IG34_EQUIV

- PDF 页 263 · 原子类型 CODE_LITERAL · 所在节 `§6.3.5.7 Microbiology Domains`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
relrec.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0263.txt` 第 9-9 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8| susceptibility results (MS) from the NAAT, using --REFID.
  9| relrec.xpt
 10| Row      STUDYID   RDOMAIN USUBJID IDVAR    IDVARVAL RELTYPE                 RELID
~~~~

KB 现文: `knowledge_base/domains/AG/examples.md:66` (来源: live valid_hits):

~~~~
  66| **relrec.xpt**
~~~~

### T13. `ig34_p0263_a024` — r3:R3_IG34_EQUIV

- PDF 页 263 · 原子类型 CODE_LITERAL · 所在节 `§6.3.5.7.3 Microbiology Specimen/Microbiology Susceptibility Examples`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
suppmb.xpt
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0263.txt` 第 34-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 33| The culture-contamination indicator flag is shown in SUPPMB.
 34| suppmb.xpt
 35| Row      STUDYID    RDOMAIN     USUBJID        IDVAR     IDVARVAL    QNAM            QLABEL                             QVAL   QORIG
~~~~

KB 现文: `knowledge_base/domains/MB/examples.md:85,196,248` (来源: live valid_hits):

~~~~
  85| **suppmb.xpt**
 196| **suppmb.xpt**
 248| **suppmb.xpt**
~~~~

### T14. `ig34_p0400_a009` — r3:R3_IG34_EQUIV

- PDF 页 400 · 原子类型 FIGURE · 所在节 `§7.2.1 Trial Arms (TA) – Example 7`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 7, RTOG-93-09 Prospective View — diagram showing Screen Epoch, Induction Treatment Epoch (Chemo+Rad/Chemo+Rad* boxes and Chemo+Rad/Chemo+Rad** boxes), Continuation Treatment Epoch (upper CR arm: Chemo+Boost → Chemo with 'If disease progression' skip arrow to FU; lower CRS arm: If not eligible for surgery skip + 3-5w Rest → Surgery → 4-6w Rest → Chemo → Chemo with 'If disease progression' skip arrow to FU), Follow Epoch (FU boxes); CR label 'Chemotherapy and Radiation Arm'; CRS label 'Chemotherapy, Radiation and Surgery Arm'; *Disease evaluation earlier **Disease evaluation later; Randomization arrow]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0400.txt` 第 13-26 行 (自动定位, 词覆盖 0.529; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 12| detail within the Induction Chemo + RT and Additional Chemo blocks than the preceding diagram. Both the
 13| induction and additional chemotherapy are given in 2 cycles. The second induction cycle is different for the 2 arms,
 14| since radiation therapy for those assigned to the non-surgery arm includes a “boost” which those assigned to the
 15| surgery arm do not receive.
 16| The next diagram shows the prospective view of this trial. The protocol conceives of treatment as being divided into
 17| 2 parts, induction and continuation, so these have been treated as 2 different epochs. This is also an important point
 18| in the trial operationally, the point when subjects are “registered” a second time, and when subjects who will skip
 19| forward are identified (i.e., because of disease progression or ineligibility for surgery).
 20| 
 21| Example Trial 7, RTOG-93-09 Prospective View
 22| 
 23| 
 24| 
 25| 
 26| *Disease evaluation earlier **Disease evaluation later
 27| 
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:869-873` (来源: fuzzy locate (score 0.549)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 869| Example Trial 7, RTOG 93-09, involves treatment of lung cancer with chemotherapy and radiotherapy, with or without surgery. The protocol (RTOG-93-09), which was provided by the Radiation Oncology Therapy Group (RTOG), does not include a study schema diagram, but does include a text-based representation of diverging “options” to which a subject may be assigned. All subjects go through the branch point at randomization, when they are assigned to either chemotherapy plus radiotherapy (CR) or chemotherapy and radiotherapy plus surgery (CRS). All subjects receive induction chemotherapy and radiation, with a slight difference between those randomized to the 2 arms during the second cycle of chemotherapy. Those randomized to the non-surgery arm are evaluated for disease somewhat earlier, to avoid delays in administering the radiation boost to those whose disease has not progressed. After induction chemotherapy and radiation, subjects are evaluated for disease progression, and those whose disease has progressed stop treatment, but enter follow-up. Not all subjects randomized to receive surgery who do not have disease progression will necessarily receive surgery. If they are poor candidates for surgery or do not wish to receive surgery, they will not receive surgery, but will receive further chemotherapy. The following diagram is based on the text “schema” in the protocol, with the 5 options it names. The diagram in this form might suggest that the trial has 5 arms.
 870| 
 871| **Study Schema with 5 "options"**
 872| 
 873| > KB note (not in SDTMIG): the following Mermaid diagram is a KB rendering of the PDF figure "Example Trial 7, RTOG 93-09 Study Schema with 5 "options"".
~~~~

### T15. `ig34_p0009_a017` — r3:R3_IG34_EQUIV

- PDF 页 9 · 原子类型 LIST_ITEM · 所在节 `§1.4.1 [How to Read a Domain Specification]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Variable Name
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0009.txt` 第 35-35 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34| they are a set of variables that the SDS Team considered likely to be included. The columns of the table are:
 35|     •    Variable Name
 36|          o   For variables that do not include a domain prefix, this name is taken directly from the SDTM.
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:74` (来源: live valid_hits):

~~~~
  74| - Variable Name
~~~~

### T16. `ig34_p0009_a020` — r3:R3_IG34_EQUIV

- PDF 页 9 · 原子类型 LIST_ITEM · 所在节 `§1.4.1 [How to Read a Domain Specification]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Variable Label: A longer name for the variable
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0009.txt` 第 38-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37|          o   For variables with a "--" placeholder in the SDTM, the "--" is replaced by the 2-character domain code.
 38|     •    Variable Label: A longer name for the variable
 39|          o   This may be the same as the label in the SDTM, or it may be customized for the domain.
~~~~

KB 现文: `knowledge_base/chapters/ch01_introduction.md:77` (来源: live valid_hits):

~~~~
  77| - Variable Label: A longer name for the variable
~~~~

### T17. `ig34_p0061_a002` — r3:R3_IG34_EQUIV

- PDF 页 61 · 原子类型 LIST_ITEM · 所在节 `§5.1 [Comments (CO)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
1. The Comments special-purpose domain provides a solution for submitting free-text comments related to data in 1 or more SDTM domains (as described in Section 8.5, Relating Comments to a Parent Domain) or collected on a separate CRF page dedicated to comments.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0061.txt` 第 2-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| CO – Assumptions
  2|      1.   The Comments special-purpose domain provides a solution for submitting free-text comments related to data in 1 or more SDTM domains (as described
  3|           in Section 8.5, Relating Comments to a Parent Domain) or collected on a separate CRF page dedicated to comments. Comments are generally not
  4|           responses to specific questions; instead, comments usually consist of voluntary free-text or unsolicited observations.
~~~~

KB 现文: `knowledge_base/domains/CO/assumptions.md:19` (来源: live valid_hits):

~~~~
  19| 1. The Comments special-purpose domain provides a solution for submitting free-text comments related to data in 1 or more SDTM domains (as described in Section 8.5, Relating Comments to a Parent Domain) or collected on a separate CRF page dedicated to comments. Comments are generally not responses to specific questions; instead, comments usually consist of voluntary free-text or unsolicited observations.
~~~~

### T18. `ig34_p0070_a018` — r3:R3_IG34_EQUIV

- PDF 页 70 · 原子类型 LIST_ITEM · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
RAC607 BAC - UNKNOWN <RACE codelist>
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0070.txt` 第 7-7 行 (自动定位, 词覆盖 0.2; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  6| information: https://www.cdisc.org/standards/foundational/cdash.
  7| This example shows multiple race categories and subcategories. Only a subset of options is shown for this
  8| instrument due to space constraints.
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### T19. `ig34_p0070_a023` — r3:R3_IG34_EQUIV

- PDF 页 70 · 原子类型 LIST_ITEM · 所在节 `§5.2 [DM – Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ALASKA NATIVE
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0070.txt` 第 15-15 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| 
 15| If the study participant answered: AMERICAN INDIAN OR ALASKA NATIVE
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:13,118,134` (来源: live valid_hits):

~~~~
  13| | 5 | ABC123 | DM | ABC12302001 | 02001 | 2006-02-02 | 2006-03-31 | 2006-02-02 | 2006-03-31 | 2006-01-15 | 2006-04-12 | 02 | GONZALEZ, E | 1950-06-23 | 55 | YEARS | F | AMERICAN INDIAN OR ALASKA NATIVE | NOT HISPANIC OR LATINO | P | Placebo | P | Placebo | | | USA |
 118|     R1["☐ AMERICAN INDIAN OR ALASKA NATIVE"]
 134|     SC1["Subcategories CRACE01-04 → SUPPDM.QVAL<br/>☐ ALASKA NATIVE<br/>☐ AMERICAN INDIAN<br/>☐ CARIBBEAN INDIAN<br/>☐ CENTRAL AMERICAN INDIAN"]
~~~~

### T20. `ig34_p0071_a006` — r3:R3_IG34_EQUIV

- PDF 页 71 · 原子类型 LIST_ITEM · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
ASIAN INDIAN
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0072.txt` 第 6-13 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  5|                                                                                                                 Name
  6| RACE01      1       Which of the following Race    Study             Text   RACE                                (RACE)        AMERICAN INDIAN OR                                checkbox
  7|                     racial designations            participants                                                               ALASKA NATIVE
  8|                     best describes you?            should self-
  9|                     (More than one                 report race, with
 10|                     choice is acceptable.)         race being
 11|                                                    asked about
 12|                                                    after ethnicity.
 13| RACE02         2       Which of the following Race Study             Text   RACE                                (RACE)        ASIAN                                             checkbox
 14|                        racial designations         participants
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:135,170,190` (来源: live valid_hits):

~~~~
 135|     SC2["Subcategories CRACE05-10 → SUPPDM.QVAL<br/>☐ ASIAN AMERICAN  ☐ ASIAN INDIAN<br/>☐ BANGLADESHI  ☐ CHINESE<br/>☐ JAPANESE  ☐ KOREAN"]
 170| > If the study participant answered ASIAN, subcategories (CRACE05-CRACE10) are presented: ASIAN AMERICAN, ASIAN INDIAN, BANGLADESHI, CHINESE, JAPANESE, KOREAN.
 190| | CRACE05-CRACE10 | 11 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "ASIAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ASIAN AMERICAN; ASIAN INDIAN; BANGLADESHI; CHINESE; JAPANESE; KOREAN; | | | checkbox | CRACE05-CRACE10 |
~~~~

### T21. `ig34_p0075_a020` — r3:R3_IG34_EQUIV

- PDF 页 75 · 原子类型 LIST_ITEM · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
CHINESE
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0074.txt` 第 7-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  6|            recommended QNAM-QLABEL values have been provided.
  7| Rows 3-5:    Show that USUBJID ABC789-010-047 selected 3 collected race (CRACE) values, "CHINESE",
  8|              "KOREAN", and "RUSSIAN". CDASH recommended QNAM-QLABEL values have been provided.
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:135,170,190` (来源: live valid_hits):

~~~~
 135|     SC2["Subcategories CRACE05-10 → SUPPDM.QVAL<br/>☐ ASIAN AMERICAN  ☐ ASIAN INDIAN<br/>☐ BANGLADESHI  ☐ CHINESE<br/>☐ JAPANESE  ☐ KOREAN"]
 170| > If the study participant answered ASIAN, subcategories (CRACE05-CRACE10) are presented: ASIAN AMERICAN, ASIAN INDIAN, BANGLADESHI, CHINESE, JAPANESE, KOREAN.
 190| | CRACE05-CRACE10 | 11 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "ASIAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ASIAN AMERICAN; ASIAN INDIAN; BANGLADESHI; CHINESE; JAPANESE; KOREAN; | | | checkbox | CRACE05-CRACE10 |
~~~~

### T22. `ig34_p0075_a021` — r3:R3_IG34_EQUIV

- PDF 页 75 · 原子类型 LIST_ITEM · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
JAPANESE
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0075.txt` 第 ? 行 (自动定位, 词覆盖 0; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
(未定位, 请直接看该页)
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:135,170,190` (来源: live valid_hits):

~~~~
 135|     SC2["Subcategories CRACE05-10 → SUPPDM.QVAL<br/>☐ ASIAN AMERICAN  ☐ ASIAN INDIAN<br/>☐ BANGLADESHI  ☐ CHINESE<br/>☐ JAPANESE  ☐ KOREAN"]
 170| > If the study participant answered ASIAN, subcategories (CRACE05-CRACE10) are presented: ASIAN AMERICAN, ASIAN INDIAN, BANGLADESHI, CHINESE, JAPANESE, KOREAN.
 190| | CRACE05-CRACE10 | 11 | Which of the following racial designations best describes you? | Race | Select each value that applies if the subject answered "ASIAN". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ASIAN AMERICAN; ASIAN INDIAN; BANGLADESHI; CHINESE; JAPANESE; KOREAN; | | | checkbox | CRACE05-CRACE10 |
~~~~

### T23. `ig34_p0075_a033` — r3:R3_IG34_EQUIV

- PDF 页 75 · 原子类型 LIST_ITEM · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
BLACK
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0075.txt` 第 14-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| 
 14| If the study participant answered: BLACK OR AFRICAN AMERICAN
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:11,120,136` (来源: live valid_hits):

~~~~
  11| | 3 | ABC123 | DM | ABC12301003 | 01003 | 2006-01-16 | 2006-03-19 | 2006-01-16 | 2006-03-19 | 2006-01-02 | 2006-03-19 | 01 | JOHNSON, M | 1938-01-19 | 68 | YEARS | F | BLACK OR AFRICAN AMERICAN | NOT HISPANIC OR LATINO | P | Placebo | P | Placebo | | | USA |
 120|     R3["☐ BLACK OR AFRICAN AMERICAN"]
 136|     SC3["Subcategories CRACE11-17 → SUPPDM.QVAL<br/>☐ AFRICAN  ☐ AFRICAN AMERICAN<br/>☐ AFRICAN CARIBBEAN  ☐ BAHAMIAN<br/>☐ BARBADIAN  ☐ BLACK<br/>☐ BLACK CENTRAL AMERICAN"]
~~~~

### T24. `ig34_p0113_a010` — r3:R3_IG34_EQUIV

- PDF 页 113 · 原子类型 LIST_ITEM · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
1 tablet from bottles A and C on 2011-01-21 and 2011-01-22
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0113.txt` 第 12-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11|       •     0 tablets from bottle B on 2011-01-21, then 2 tablets on 2011-01-22
 12|       •     1 tablet from bottles A and C on 2011-01-21 and 2011-01-22
 13|       •     1 tablet from ottles A, B and C from 2011-01-23 to 2011-01-28
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:117` (来源: live valid_hits):

~~~~
 117| - 1 tablet from bottles A and C on 2011-01-21 and 2011-01-22
~~~~

### T25. `ig34_p0141_a025` — r3:R3_IG34_EQUIV

- PDF 页 141 · 原子类型 LIST_ITEM · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 2-4: Show AEGRPID used to group records related to a single event of "VOMITING".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0141.txt` 第 43-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 42| Row 1:          Shows an adverse event of nausea, for which severity was moderate.
 43| Rows 2-4:       Show AEGRPID used to group records related to a single event of "VOMITING".
 44| Rows 5-6:       Show AEGRPID used to group records related to a single event of "DIARRHEA".
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:54` (来源: live valid_hits):

~~~~
  54| **Rows 2-4:** Show AEGRPID used to group records related to a single event of "VOMITING".
~~~~

