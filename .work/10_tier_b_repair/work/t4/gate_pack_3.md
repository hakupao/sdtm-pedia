# T4.1 总闸样本包 3/4 (行 43-63 / 84)

> 由 `scripts/t4/t4_sample.py` (seed 20261127) 生成, `scripts/t4/t4_render.py` 渲染. 只读材料.

### 43. `ig34_p0236_a008` — gate:VALUE_DIFF

- PDF 页 236 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **VALUE_DIFF** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `S1-R1` · 批 `T1/T2-errata`
- 原子抽错登记: R1 → ATOM_ERR; 依据: B-IS review: verbatim 漏 ISSCAT; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-IS_review.md:70`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISORRES | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 21-21 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20| is.xpt
 21| Row STUDYID DOMAIN USUBJID           ISSEQ   ISREFID ISGRPID   ISTESTCD ISTEST               ISBDAGNT                  ISTSTOPO ISCAT                   ISSCAT     ISORRES ISSTRESC ISSTRESN ISSTRESU ISSPEC ISMETHOD VISITNUM VISIT    ISDTC
 22| 1   RSV1230 IS     RSV1230-          1       13668   1         MBIGGAB Microbial-induced     HUMAN RESPIRATORY         SCREEN   STUDY VACCINE-RELATED   HUMORAL    POSITIVE POSITIVE                  SERUM ELISA     1        BASELINE 2017-
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:113-113` (来源: near triage kb_loc knowledge_base/domains/IS/examples.md:113 (score 1.0)):

~~~~
 113| | Row | STUDYID | DOMAIN | USUBJID | ISSEQ | ISREFID | ISGRPID | ISTESTCD | ISTEST | ISBDAGNT | ISTSTOPO | ISCAT | ISSCAT | ISORRES | ISSTRESC | ISSTRESN | ISSTRESU | ISSPEC | ISMETHOD | VISITNUM | VISIT | ISDTC |
~~~~

### 44. `ig34_p0236_a010` — gate:VALUE_DIFF

- PDF 页 236 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-IS`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | 1 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:25 | 25 | 25 | titer | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 23-25 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 22| 1   RSV1230 IS     RSV1230-          1       13668   1         MBIGGAB Microbial-induced     HUMAN RESPIRATORY         SCREEN   STUDY VACCINE-RELATED   HUMORAL    POSITIVE POSITIVE                  SERUM ELISA     1        BASELINE 2017-
 23|                    011                                                  IgG Antibody         SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                        05-27
 24|                                                                                              B
 25| 2        RSV1230   IS     RSV1230-   2       13668   1         MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         QUANTIFY STUDY VACCINE-RELATED   HUMORAL    1:25     25         25    titer    SERUM   ELISA   1        BASELINE 2017-
 26|                           011                                            IgG Antibody        SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                        05-27
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:116` (来源: decision.evidence.hit):

~~~~
 116| | 2 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | 1 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN B | QUANTIFY | STUDY VACCINE-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:25 | 25 | 25 | titer | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
~~~~

### 45. `ig34_p0236_a012` — gate:VALUE_DIFF

- PDF 页 236 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-IS`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 4 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | 2 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | QUANTIFY | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:120 | 120 | 120 | titer | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0236.txt` 第 29-31 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| 3        RSV1230   IS     RSV1230-   1       13668   2         MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         SCREEN   NON-STUDY-RELATED       HUMORAL    POSITIVE POSITIVE                  SERUM   ELISA   1        BASELINE 2017-
 29|                           011                                            IgG Antibody        SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                        05-27
 30|                                                                                              Z
 31| 4        RSV1230   IS     RSV1230-   2       13668   2         MBIGGAB   Microbial-induced   HUMAN RESPIRATORY         QUANTIFY NON-STUDY-RELATED       HUMORAL    1:120    120        120   titer    SERUM   ELISA   1        BASELINE 2017-
 32|                           011                                            IgG Antibody        SYNCYTIAL VIRUS-PROTEIN            IMMUNOGENICITY          IMMUNITY                                                                        05-27
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:118` (来源: decision.evidence.hit):

~~~~
 118| | 4 | RSV1230 | IS | RSV1230-011 | 2 | 13668 | 2 | MBIGGAB | Microbial-induced IgG Antibody | HUMAN RESPIRATORY SYNCYTIAL VIRUS-PROTEIN Z | QUANTIFY | NON-STUDY-RELATED IMMUNOGENICITY | HUMORAL IMMUNITY | 1:120 | 120 | 120 | titer | SERUM | ELISA | 1 | BASELINE | 2017-05-27 |
~~~~

### 46. `ig34_p0247_a022` — gate:VALUE_DIFF

- PDF 页 247 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.6 Laboratory Test Results (LB)`
- triage 类 **VALUE_DIFF** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `C7-atom-not-in-PDF` · 批 `B-LB`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC | LB | ABC-001-002 | 1 | HCG | Choriogonadotropin Beta | CHEMISTRY | | | Ord | PtFtv | | | | | | | | | NOT DONE | NOT APPLICABLE (SUBJECT MALE) | 2106-3 | URINE | | 1 | BASELINE | 1999-06-24T08:00 | Y |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0247.txt` 第 73-74 行 (自动定位, 词覆盖 0.962; 版式以原 PDF 为准):

~~~~
 72|                                            001                                                       Beta                                                                                                                                                                                                                                                                                                                                                                                                                                19T04:00
 73| 2       ABC               LB               ABC-001-         1            HCG                         Choriogonadotropin                CHEMISTRY                                               Ord                  PrThr                                                                                                                                                                            NOT           NOT APPLICABLE                    2106-3          URINE                           1                 BASELINE          1999-06-               Y
 74|                                            002                                                       Beta                                                                                                                                                                                                                                                                                            DONE          (SUBJECT MALE)                                                                                                        24T08:00
 75| 
~~~~

KB 现文: `knowledge_base/domains/LB/examples.md:37-39` (来源: near triage kb_loc knowledge_base/domains/LB/examples.md:51 (score 0.538)):

~~~~
  37| | 14 | ABC | LB | ABC-001-001 | 14 | | PH | pH | | URINALYSIS | | 7.5 | | QUANTITATIVE | LOG SUBSTANCE CONCENTRATION | | 5.0 | 9.0 | | 7.5 | | | 5.00 | 9.00 | | | | | 5803-2 | URINE | TEST STRIP | | Y | Y | | | 1 | Week 1 | 1999-06-19 | Y | |
  38| | 15 | ABC | LB | ABC-001-001 | 15 | | ALB | Albumin | | CHEMISTRY | | | | QUANTITATIVE | MASS CONCENTRATION | | | | | | | | | | | | NOT DONE | INSUFFICIENT SAMPLE | 2862-1 | SERUM | ELECTROPHORESIS | | | | | | 2 | Week 2 | 1999-07-21 | Y | |
  39| | 16 | ABC | LB | ABC-001-001 | 16 | | CHOL | Cholesterol | | CHEMISTRY | | 229 | mg/dL | QUANTITATIVE | MASS CONCENTRATION | | 0 | <200 | | 229 | 229 | mg/dL | 0 | 199 | | | | | 2093-3 | SERUM | | | | | | | 2 | Week 2 | 1999-07-21 | Y | |
~~~~

### 47. `ig34_p0353_a016` — gate:VALUE_DIFF

- PDF 页 353 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-TU`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | STUDY01 | TU | 40913 | 3 | L01-2 | LMLIDENT | Limb Lesion Identification | TARGET | TARGET | LEG | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0353.txt` 第 31-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 30|                                                                                                  ARTERY
 31| 3        STUDY01 TU      40913    3       L01-2     LMLIDENT   Limb Lesion      TARGET  TARGET   LEG           LEFT   ANGIOGRAPHY INVESTIGATOR 1      SCREEN 2007-
 32|                                                                Identification                                                                                02-01
 33| 4        STUDY01 TU      40913    4       L01-G     GRLIDENT   Graft Lesion     TARGET   TARGET   FEMORO-      LEFT   ANGIOGRAPHY INVESTIGATOR 1      SCREEN 2007-
~~~~

KB 现文: `knowledge_base/domains/TU/examples.md:25` (来源: decision.evidence.hit):

~~~~
  25| | 3 | STUDY01 | TU | 40913 | 3 | L01-2 | LMLIDENT | Limb Lesion Identification | TARGET | TARGET | LEG | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
~~~~

### 48. `ig34_p0355_a014` — gate:VALUE_DIFF

- PDF 页 355 · 原子类型 TABLE_ROW · 所在节 `§6.3.12.3 Tumor Identification/Tumor Results Examples`
- triage 类 **VALUE_DIFF** · 终态 **PDF_TYPO** (T3 前 PARTIAL) · 判定规则 `writer-Tn-registry` · 批 `B-TR`
- PDF 笔误登记: `B-TR T-1` (见 `work/t2_pdf_typo_registry.jsonl`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 13 | ABC | TR | 44444 | 13 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0355.txt` 第 27-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 26|                                                                                                                                                                                                                            02-19
 27| 13       ABC   TR      44444    13     TARGET    A2         T04.1    DIAMETER     Diameter      6              mm       6              6        mm                              PHOTOGRAPHY INVESTIGATOR 40      WEEK 6    2010-   48
 28|                                                                                                                                                                                                                            02-20
 29| 14       ABC   TR      44444    14     TARGET    A2         T04.2    DIAMETER     Diameter      7              mm       7              7        mm                              PHOTOGRAPHY INVESTIGATOR 40      WEEK 6    2010-   48
~~~~

KB 现文: `knowledge_base/domains/TR/examples.md:30` (来源: registry B-TR T-1 kb_line_now):

~~~~
  30| | 12 | ABC | TR | 44444 | 12 | TARGET | A2 | T04.1 | DIAMETER | Diameter | 6 | mm | 6 | 6 | mm | | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
~~~~

### 49. `ig34_p0121_a016` — gate:IE

- PDF 页 121 · 原子类型 TABLE_ROW · 所在节 `§6.1.4 [Meal Data (ML)]`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_030`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
MLPRESP | ML Pre-specified | Char | (NY) | Variable Qualifier | Used when a specific meal is prespecified on a CRF. Values should be "Y" or null. | Perm
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0121.txt` 第 21-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20| MLSCAT         Subcategory for Meal         Char *                      Grouping     Used to define a further categorization of MLCAT values.                                        Perm
 21|                                                                         Qualifier
 22| MLPRESP        ML Pre-specified             Char (NY)                   Variable     Used when a specific meal is prespecified on a CRF. Values should be "Y" or null.               Perm
 23|                                                                         Qualifier
~~~~

KB 现文: `knowledge_base/domains/ML/spec.md:88-93` (来源: near triage kb_loc knowledge_base/domains/ML/spec.md:86 (score 0.958)):

~~~~
  88| - **Label:** ML Pre-specified
  89| - **Type:** Char
  90| - **Controlled Terms:** (NY) C66742
  91| - **Role:** Variable Qualifier
  92| - **Core:** Perm
  93| - **CDISC Notes:** Used when a specific meal is prespecified on a CRF. Values should be "Y" or null.
~~~~

### 50. `ig34_p0135_a001` — gate:IE

- PDF 页 135 · 原子类型 TABLE_HEADER · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_018`
- IE 类别 `SPEC_TABLE_HEADER` · 排除理由: Tier B T1 IE (SPEC_TABLE_HEADER; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0135.txt` 第 1-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Variable      Variable Label          Type Controlled          Role        CDISC Notes                                                                                                      Core
  2| Name                                       Terms, Codelist
  3|                                            or Format1
  4| AEBDSYCD      Body System or Organ    Num MedDRA               Variable    Dictionary derived. Code for the body system or organ class used by the sponsor. When using a multi-             Exp
~~~~

KB 现文: `knowledge_base/domains/AE/spec.md:115-120` (来源: fuzzy locate (score 0.846)):

~~~~
 115| - **Label:** Dictionary-Derived Term
 116| - **Type:** Char
 117| - **Controlled Terms:** MedDRA
 118| - **Role:** Synonym Qualifier
 119| - **Core:** Req
 120| - **CDISC Notes:** Dictionary-derived text description of AETERM or AEMODIFY. Equivalent to the Preferred Term (PT in MedDRA). The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.
~~~~

### 51. `ig34_p0148_a028` — gate:IE

- PDF 页 148 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events (CE)]`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_010`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| CEDECOD | Dictionary-Derived Term | Char | * | Synonym Qualifier | Controlled terminology for the name of the clinical event. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0148.txt` 第 39-41 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38|               Clinical Event
 39| CEDECOD       Dictionary-Derived      Char *                    Synonym         Controlled terminology for the name of the clinical event. The sponsor is expected to provide the        Perm
 40|               Term                                              Qualifier       dictionary name and version used to map the terms utilizing the external codelist element in the Define-
 41|                                                                                 XML document.
 42| CECAT         Category for the        Char *                    Grouping        Used to define a category of related records.                                                            Perm
~~~~

KB 现文: `knowledge_base/domains/CE/spec.md:79-84` (来源: near triage kb_loc knowledge_base/domains/CE/spec.md:77 (score 0.971)):

~~~~
  79| - **Label:** Dictionary-Derived Term
  80| - **Type:** Char
  81| - **Controlled Terms:** *
  82| - **Role:** Synonym Qualifier
  83| - **Core:** Perm
  84| - **CDISC Notes:** Controlled terminology for the name of the clinical event. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.
~~~~

### 52. `ig34_p0149_a018` — gate:IE

- PDF 页 149 · 原子类型 TABLE_ROW · 所在节 `§6.2.3 [Clinical Events (CE)]`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_010`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| CEENRF | End Relative to Reference Period | Char | (STNREF) | Timing | Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0149.txt` 第 40-44 行 (自动定位, 词覆盖 0.978; 版式以原 PDF 为准):

~~~~
 39| CESTRF        Start Relative to       Char (STENRF)             Timing       Describes the start of the clinical event relative to the sponsor-defined reference period. The sponsor-    Perm
 40|               Reference Period                                               defined reference period is a continuous period of time defined by a discrete starting point and a
 41|                                                                              discrete ending point (represented by RFSTDTC and RFENDTC in Demographics).
 42|                                                                              Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing
 43|                                                                              Variables.
 44| CEENRF        End Relative to         Char (STENRF)             Timing       Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined        Perm
 45|               Reference Period                                               reference period is a continuous period of time defined by a discrete starting point and a discrete
~~~~

KB 现文: `knowledge_base/domains/CE/spec.md:251-255` (来源: near triage kb_loc knowledge_base/domains/CE/spec.md:248 (score 0.957)):

~~~~
 251| - **Type:** Char
 252| - **Controlled Terms:** (STENRF) C66728
 253| - **Role:** Timing
 254| - **Core:** Perm
 255| - **CDISC Notes:** Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics).  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.
~~~~

### 53. `ig34_p0168_a0001` — gate:IE

- PDF 页 168 · 原子类型 TABLE_ROW · 所在节 `§6.2.5 Healthcare Encounters (HO)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_007`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| USUBJID | Unique Subject Identifier | Char | | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. | Req |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0168.txt` 第 3-4 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| Name                                            Codelist or Format1
  3| USUBJID        Unique Subject Identifier   Char                         Identifier   Identifier used to uniquely identify a subject across all studies for all applications or           Req
  4|                                                                                      submissions involving the product.
  5| HOSEQ          Sequence Number             Num                          Identifier   Sequence number given to ensure uniqueness of subject records within a domain. May be               Req
~~~~

KB 现文: `knowledge_base/domains/HO/spec.md:25-30` (来源: near triage kb_loc knowledge_base/domains/HO/spec.md:23 (score 0.952)):

~~~~
  25| - **Label:** Unique Subject Identifier
  26| - **Type:** Char
  27| - **Controlled Terms:** 
  28| - **Role:** Identifier
  29| - **Core:** Req
  30| - **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.
~~~~

### 54. `ig34_p0193_a006` — gate:IE

- PDF 页 193 · 原子类型 TABLE_HEADER · 所在节 `§6.3.4 Inclusion/Exclusion Criteria Not Met (IE)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_008`
- IE 类别 `SPEC_TABLE_HEADER` · 排除理由: Tier B T1 IE (SPEC_TABLE_HEADER; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0193.txt` 第 6-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5| ie.xpt, Inclusion/Exclusion Criteria Not Met — Findings. One record per inclusion/exclusion criterion not met per subject, Tabulation.
  6| Variable       Variable Label                Type Controlled Terms,       Role          CDISC Notes                                                                                                Core
  7| Name                                              Codelist or
  8|                                                   Format1
  9| STUDYID        Study Identifier              Char                         Identifier    Unique identifier for a study.                                                                             Req
~~~~

KB 现文: `knowledge_base/domains/IE/spec.md:52-57` (来源: fuzzy locate (score 0.769)):

~~~~
  52| - **Label:** Inclusion/Exclusion Criterion Short Name
  53| - **Type:** Char
  54| - **Controlled Terms:** *
  55| - **Role:** Topic
  56| - **Core:** Req
  57| - **CDISC Notes:** Short name of the criterion described in IETEST. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "IN01", "EX01".
~~~~

### 55. `ig34_p0243_a011` — gate:IE

- PDF 页 243 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.6 Laboratory Test Results (LB)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_008`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| LBNRIND | Reference Range Indicator | Char | (NRIND) | Variable Qualifier | Indicates where the value falls with respect to reference range defined by LBORNRLO and LBORNRHI, LBSTNRLO and LBSTNRHI, or by LBSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether LBNRIND refers to the original or standard reference ranges and results. LBNRIND is not used to indicate clinical significance. | Exp |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0243.txt` 第 35-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34|               Units
 35| LBNRIND       Reference Range       Char (NRIND)            Variable    Indicates where the value falls with respect to reference range defined by LBORNRLO and LBORNRHI,                Exp
 36|               Indicator                                     Qualifier   LBSTNRLO and LBSTNRHI, or by LBSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW".
 37|                                                                         Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether
 38|                                                                         LBNRIND refers to the original or standard reference ranges and results. LBNRIND is not used to indicate
 39|                                                                         clinical significance.
 40| LBSTAT        Completion Status     Char (ND)               Record      Used to indicate exam not done. Should be null if a result exists in LBORRES.                                    Perm
~~~~

KB 现文: `knowledge_base/domains/LB/spec.md:259-264` (来源: near triage kb_loc knowledge_base/domains/LB/spec.md:257 (score 1.0)):

~~~~
 259| - **Label:** Reference Range Indicator
 260| - **Type:** Char
 261| - **Controlled Terms:** (NRIND) C78736
 262| - **Role:** Variable Qualifier
 263| - **Core:** Exp
 264| - **CDISC Notes:** Indicates where the value falls with respect to reference range defined by LBORNRLO and LBORNRHI, LBSTNRLO and LBSTNRHI, or by LBSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether LBNRIND refers to the original or standard reference ranges and results. LBNRIND is not used to indicate clinical significance.
~~~~

### 56. `ig34_p0264_a005` — gate:IE

- PDF 页 264 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.8 Microscopic Findings (MI)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_006`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0264.txt` 第 6-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5|                                            Format1
  6| STUDYID       Study Identifier        Char                      Identifier   Unique identifier for a study.                                                                                Req
  7| DOMAIN        Domain Abbreviation     Char MI                   Identifier   Two-character abbreviation for the domain.                                                                    Req
~~~~

KB 现文: `knowledge_base/domains/MI/spec.md:8-12` (来源: near triage kb_loc knowledge_base/domains/MI/spec.md:5 (score 0.875)):

~~~~
   8| - **Type:** Char
   9| - **Controlled Terms:** 
  10| - **Role:** Identifier
  11| - **Core:** Req
  12| - **CDISC Notes:** Unique identifier for a study.
~~~~

### 57. `ig34_p0264_a021` — gate:IE

- PDF 页 264 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.8 Microscopic Findings (MI)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_006`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
MISTRESU | Standard Units | Char | (UNIT) | Variable Qualifier | Standardized unit used for MISTRESC and MISTRESN. | Perm
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0264.txt` 第 40-41 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 39| MISTRESN      Numeric Result/Finding Num                        Result       Used for continuous or numeric results or findings in standard format; copied in numeric format from       Perm
 40|               in Standard Units                                 Qualifier    MISTRESC. MISTRESN should store all numeric test results or findings.
 41| MISTRESU      Standard Units         Char (UNIT)                Variable     Standardized unit used for MISTRESC and MISTRESN.                                                          Perm
 42|                                                                 Qualifier
~~~~

KB 现文: `knowledge_base/domains/MI/spec.md:151-156` (来源: near triage kb_loc knowledge_base/domains/MI/spec.md:149 (score 0.929)):

~~~~
 151| - **Label:** Standard Units
 152| - **Type:** Char
 153| - **Controlled Terms:** (UNIT) C71620
 154| - **Role:** Variable Qualifier
 155| - **Core:** Perm
 156| - **CDISC Notes:** Standardized unit used for MISTRESC and MISTRESN.
~~~~

### 58. `ig34_p0265_a015` — gate:IE

- PDF 页 265 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.8 Microscopic Findings (MI)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_006`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
MIDTC | Date/Time of Specimen Collection | Char | ISO 8601 datetime or interval | Timing | Date/time of specimen collection, in ISO 8601 format. | Exp
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0265.txt` 第 30-31 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 29|   EPOCH         Epoch                       Char (EPOCH)                 Timing        Epoch associated with the date/time at which the specimen was collected.                                    Perm
 30|   MIDTC         Date/Time of Specimen Char ISO 8601 datetime Timing                    Date/time of specimen collection, in ISO 8601 format.                                                       Exp
 31|                 Collection                          or interval
 32|   MIDY          Study Day of Specimen Num                                Timing        Study day of specimen collection, in integer days. The algorithm for calculations must be relative to the   Perm
~~~~

KB 现文: `knowledge_base/domains/MI/spec.md:323-327` (来源: near triage kb_loc knowledge_base/domains/MI/spec.md:320 (score 0.938)):

~~~~
 323| - **Type:** Char
 324| - **Controlled Terms:** ISO 8601 datetime or interval
 325| - **Role:** Timing
 326| - **Core:** Exp
 327| - **CDISC Notes:** Date/time of specimen collection, in ISO 8601 format.
~~~~

### 59. `ig34_p0309_a007` — gate:IE

- PDF 页 309 · 原子类型 TABLE_ROW · 所在节 `§6.3.7.7 Respiratory System Findings (RE)`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_016`
- IE 类别 `SPEC_TABLE_ROW` · 排除理由: Tier B T1 IE (SPEC_TABLE_ROW; writer)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| RELAT | Laterality | Char | (LAT) | Variable Qualifier | Side of the body used to collect measurement. Examples: "RIGHT", "LEFT". | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0309.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14| RELOC          Location Used for the     Char (LOC)             Record            Anatomical location of the subject relevant to the collection of the measurement. Examples: "LUNG",       Perm
 15|                Measurement                                      Qualifier         "BRONCHUS".
 16| RELAT          Laterality                Char (LAT)             Variable          Side of the body used to collect measurement. Examples: "RIGHT", "LEFT".                                  Perm
 17|                                                                 Qualifier
~~~~

KB 现文: `knowledge_base/domains/RE/spec.md:241-246` (来源: near triage kb_loc knowledge_base/domains/RE/spec.md:239 (score 0.944)):

~~~~
 241| - **Label:** Laterality
 242| - **Type:** Char
 243| - **Controlled Terms:** (LAT) C99073
 244| - **Role:** Variable Qualifier
 245| - **Core:** Perm
 246| - **CDISC Notes:** Side of the body used to collect measurement. Examples: "RIGHT", "LEFT".
~~~~

### 60. `sv20_p0047_a003` — gate:IE

- PDF 页 47 · 原子类型 TABLE_ROW · 所在节 `§3.2.3.2 [Subject Repro Stages]`
- triage 类 **IE** · 终态 **INTENTIONAL_EXCLUDE** (T3 前 PARTIAL) · 判定规则 `IE-ack` · 批 `T1:pack_032`
- IE 类别 `VERSION_MISMATCH` · 排除理由: Tier B T1 IE (VERSION_MISMATCH; ruling:R1-row)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
1 | STUDYID | Study Identifier | Char | | Identifier | | | C83082 | A sequence of characters used by the sponsor to uniquely identify the study. | | 
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/sv20_p0047.txt` 第 8-9 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7|     Name                                                         Qualified     Restrictions      C-code
  8| 1   STUDYID     Study Identifier   Char             Identifier                                   C83082     A sequence of characters used by
  9|                                                                                                             the sponsor to uniquely identify the
 10|                                                                                                             study.
~~~~

KB 现文: `knowledge_base/model/03_special_purpose_domains.md:133` (来源: triage kb_loc knowledge_base/model/03_special_purpose_domains.md:133 (T1 行号, 未定位, 显示 ±2 行)):

~~~~
 131| | 3 | USUBJID | Unique Subject Identifier | Char | Identifier | |
 132| | 4 | SESEQ | Sequence Number | Num | Identifier | |
 133| | 5 | ETCD | Element Code | Char | Topic | Code for the Element (from TE) |
 134| | 6 | ELEMENT | Description of Element | Char | Synonym Qualifier (ETCD) | |
 135| | 7 | TAETORD | Planned Order of Element within Arm | Num | Timing | C83438 |
~~~~

### 61. `ig34_p0042_a004` — gate:CONTROL

- PDF 页 42 · 原子类型 SENTENCE · 所在节 `§4.4.4 [Use of the Study Day Variables]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This algorithm for determining Study Day is consistent with how people typically describe sequential days relative to a fixed reference point, but creates problems if used for mathematical calculations because it does not allow for a day 0.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0042.txt` 第 3-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| for each date following RFSTDTC. Dates prior to RFSTDTC are decreased by 1, with the date preceding RFSTDTC
  3| designated as study day -1 (there is no study day 0). This algorithm for determining Study Day is consistent with
  4| how people typically describe sequential days relative to a fixed reference point, but creates problems if used for
  5| mathematical calculations because it does not allow for a day 0. As such, Study Day is not suited for use in
  6| subsequent numerical computations, such as calculating duration. The raw date values should be used rather than
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:883` (来源: live valid_hits):

~~~~
 883| This algorithm for determining Study Day is consistent with how people typically describe sequential days relative to a fixed reference point, but creates problems if used for mathematical calculations because it does not allow for a day 0. As such, Study Day is not suited for use in subsequent numerical computations, such as calculating duration. The raw date values should be used rather than Study Day in those calculations.
~~~~

### 62. `ig34_p0076_a005` — gate:CONTROL

- PDF 页 76 · 原子类型 TABLE_ROW · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
RACE03 | 5 | Which of the following racial designations best describes you? (More than one choice is acceptable.) | Race | Study participants should self-report race, with race being asked with race being asked about after ethnicity. | Text | RACE | | (RACE) | BLACK OR AFRICAN AMERICAN | | checkbox
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0076.txt` 第 16-23 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15|                    following                   participants
 16|                    racial designations         should self-
 17|                    best describes you?         report race,
 18|                    (More than one              with race
 19|                    choice is                   being asked
 20|                    acceptable.)                about after
 21|                                                ethnicity.
 22| RACE03      5      Which of the        Race    Study          Text   RACE                      (RACE)        BLACK OR AFRICAN                           checkbox
 23|                    following racial            participants                                                  AMERICAN
 24|                    designations best           should self-
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:334-334` (来源: fuzzy locate (score 1.0)):

~~~~
 334| | RACE03 | 5 | Which of the following racial designations best describes you? (More than one choice is acceptable.) | Race | Study participants should self-report race, with race being asked about after ethnicity. | Text | RACE | | (RACE) | BLACK OR AFRICAN AMERICAN | | | checkbox | |
~~~~

### 63. `ig34_p0141_a021` — gate:CONTROL

- PDF 页 141 · 原子类型 TABLE_ROW · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC123 | AE | 123101 | 2 | VOMITING | Vomiting | Y | Gastrointestinal disorders | | | | 2005-10-29 | | | 19 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0141.txt` 第 37-37 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36| 1        ABC123      AE           123101      1         NAUSEA       Nausea          Y              Gastrointestinal disorders                                     2005-10-29                                   19
 37| 2        ABC123      AE           123101      2         VOMITING     Vomiting        Y              Gastrointestinal disorders                                     2005-10-29                                   19
 38| 
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:46` (来源: live valid_hits):

~~~~
  46| | 2 | ABC123 | AE | 123101 | 2 | VOMITING | Vomiting | Y | Gastrointestinal disorders | | | | 2005-10-29 | | | 19 |
~~~~

