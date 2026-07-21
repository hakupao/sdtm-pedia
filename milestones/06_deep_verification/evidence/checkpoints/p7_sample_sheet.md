# P7 人工抽样复检工作表
> 生成时间: 2026-05-12  |  总计: 60 原子  |  seed=20260512
> **用户复检说明**: 每条原子阅读「PDF 原文」和「匹配 KB 内容」，在「你的判定」栏填 `CORRECT` 或 `WRONG: <建议verdict>`
> 误判容限: ≤3/60 → PASS；4+ → 需 root cause 分析

---

## EXACT (12 atoms)

### #1 `ig34_p0354_a019`
- **Source**: SDTMIG_v3.4 p.354  |  **Type**: TABLE_ROW  |  **Section**: §6.3.12.3 Tumor Identification/Tumor Results Examples
- **Verdict**: `EXACT`  |  **Similarity**: 0.900

**PDF 原文**:
> | 4 | ABC | TU | 44444 | 4 | | T04 | TUMIDENT | Tumor Identification | TARGET | TARGET | SKIN OF THE TRUNK | | PHOTOGRAPHY | INVESTIGATOR | 10 | SCREEN | 2010-01-03 | -1 |

**匹配 KB 内容**:
  - `md_dmTU_ex_a037` [knowledge_base/domains/TU/examples.md]
    > | 4 | ABC | TU | 44444 | 4 | | T04 | TUMIDENT | Tumor Identification | TARGET | TARGET | SKIN OF THE TRUNK | | PHOTOGRAPHY | INVESTIGATOR | 10 | SCREEN | 2010-01-03 | -1 |

**你的判定**: CORRECT

---

### #2 `ig34_p0274_a017`
- **Source**: SDTMIG_v3.4 p.274  |  **Type**: TABLE_ROW  |  **Section**: §6.3.5.9.2 Pharmacokinetics Parameters (PP)
- **Verdict**: `EXACT`  |  **Similarity**: 1.000

**PDF 原文**:
> 5 | ABC-123 | PP | 123-1001 | PPSEQ | 5 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected |

**匹配 KB 内容**:
  - `md_dmPP_ex_a037` [knowledge_base/domains/PP/examples.md]
    > | 1 | ABC-123 | PP | 123-1001 | PPSEQ | 1 | PKCOND | Condition of PK Analysis | MULTIPLE DOSE, STEADY STATE | Collected | |

**你的判定**: WRONG: PARTIAL

---

### #3 `ig34_p0148_a012`
- **Source**: SDTMIG_v3.4 p.148  |  **Type**: LIST_ITEM  |  **Section**: §6.2.2 [Biospecimen Events (BE)]
- **Verdict**: `EXACT`  |  **Similarity**: 1.000

**PDF 原文**:
> Cerkovnik P, Perhavec A, Zgajnar J, Novakovic S. Optimization of an RNA isolation procedure from plasma samples. Int J Mol Med. 2007;20(3):293-300. doi:10.3892/ijmm.20.3.293

**匹配 KB 内容**:
  - `md_dmBE_ex_a121` [knowledge_base/domains/BE/examples.md]
    > 2. Cerkovnik P, Perhavec A, Zgajnar J, Novakovic S. Optimization of an RNA isolation procedure from plasma samples. Int J Mol Med. 2007;20(3):293-300. doi:10.3892/ijmm.20.3.293

**你的判定**: WRONG: EQUIVALENT

---

### #4 `ig34_p0074_a022`
- **Source**: SDTMIG_v3.4 p.74  |  **Type**: TABLE_ROW  |  **Section**: §5.2 [Demographics (DM)]
- **Verdict**: `EXACT`  |  **Similarity**: 1.000

**PDF 原文**:
> 2 | ABC789 | DM | ABC789-010-047 | 010-047 | 24 | YEARS | F | ASIAN | NOT HISPANIC OR LATINO

**匹配 KB 内容**:
  - `md_dmDM_ex_a127` [knowledge_base/domains/DM/examples.md]
    > | 2 | ABC789 | DM | ABC789-010-047 | 010-047 | 24 | YEARS | F | ASIAN | NOT HISPANIC OR LATINO |

**你的判定**: CORRECT

---

### #5 `ig34_p0339_a020`
- **Source**: SDTMIG_v3.4 p.339  |  **Type**: TABLE_ROW  |  **Section**: §6.3.9.3.2 Clinical Classifications Use Case
- **Verdict**: `EXACT`  |  **Similarity**: 0.900

**PDF 原文**:
> | 12 | STUDYX | RS | P0001 | 12 | GCS0105H | GCS01-Confounder: Unknown | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED | | Y | 1 | 2012-11-16 |

**匹配 KB 内容**:
  - `md_dmRS_ex_a062` [knowledge_base/domains/RS/examples.md]
    > | 12 | STUDYX | RS | P0001 | 12 | GCS0105H | GCS01-Confounder: Unknown | GCS NINDS VERSION | NOT CHECKED | NOT CHECKED | | Y | 1 | 2012-11-16 |

**你的判定**: CORRECT

---

### #6 `sv20_p0064_a003`
- **Source**: SDTM_v2.0 p.64  |  **Type**: SENTENCE  |  **Section**: §6 [DATASETS FOR REPRESENTING RELATIONSHIPS]
- **Verdict**: `EXACT`  |  **Similarity**: 0.900

**PDF 原文**:
> The SDTM includes the following relationship datasets:

**匹配 KB 内容**:
  - `md_model06_a005` [knowledge_base/model/06_relationship_datasets.md]
    > The SDTM includes the following relationship datasets:

**你的判定**: CORRECT

---

### #7 `ig34_p0396_a016`
- **Source**: SDTMIG_v3.4 p.396  |  **Type**: TABLE_ROW  |  **Section**: §7.2.1 Trial Arms (TA) – Example 4
- **Verdict**: `EXACT`  |  **Similarity**: 1.000

**PDF 原文**:
> | 1 | EX4 | TA | A | A | 1 | SCRN | Screen | Randomized to A | | SCREENING |

**匹配 KB 内容**:
  - `md_dmTA_ex_a135` [knowledge_base/domains/TA/examples.md]
    > | 1 | EX4 | TA | A | A | 1 | SCRN | Screen | Randomized to A | | SCREENING |

**你的判定**: CORRECT

---

### #8 `ig34_p0124_a003`
- **Source**: SDTMIG v3.4 (no header footer).pdf p.124  |  **Type**: TABLE_ROW  |  **Section**: §6.1.4 [Meal Data (ML)]
- **Verdict**: `EXACT`  |  **Similarity**: 1.000

**PDF 原文**:
> 4 | XYZ | ML | XYZ-001-001 | 4 | WILD MUSHROOMS | DILI EVALUATION | Y | Y | | | 2015-12-27 | 2015-12-24 | | -P1W | | | |

**匹配 KB 内容**:
  - `md_dmML_ex_a028` [knowledge_base/domains/ML/examples.md]
    > | 4 | XYZ | ML | XYZ-001-001 | 4 | WILD MUSHROOMS | DILI EVALUATION | Y | Y | | | 2015-12-27 | 2015-12-24 | | -P1W | | | |

**你的判定**: CORRECT

---

### #9 `ig34_p0154_a0005`
- **Source**: SDTMIG_v3.4 p.154  |  **Type**: TABLE_HEADER  |  **Section**: §6.2.3 [Clinical Events]
- **Verdict**: `EXACT`  |  **Similarity**: 0.900

**PDF 原文**:
> | Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |

**匹配 KB 内容**:
  - `md_ch04_a104` [knowledge_base/chapters/ch04_general_assumptions.md]
    > | Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |

**你的判定**: CORRECT

---

### #10 `ig34_p0399_a019`
- **Source**: SDTMIG_v3.4 p.399  |  **Type**: TABLE_ROW  |  **Section**: §7.2.1 Trial Arms (TA) – Example 6
- **Verdict**: `EXACT`  |  **Similarity**: 1.000

**PDF 原文**:
> | 17 | EX6 | TA | B | B | 7 | RESTB | Rest B | | | TREATMENT |

**匹配 KB 内容**:
  - `md_dmTA_ex_a216` [knowledge_base/domains/TA/examples.md]
    > | 17 | EX6 | TA | B | B | 7 | RESTB | Rest B | | | TREATMENT |

**你的判定**: CORRECT

---

### #11 `ig34_p0375_a012`
- **Source**: SDTMIG_v3.4 p.375  |  **Type**: TABLE_HEADER  |  **Section**: FA – Examples
- **Verdict**: `EXACT`  |  **Similarity**: 1.000

**PDF 原文**:
> | Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FAORRES | FACOLSRT | VISITNUM | VISIT | FADTC | FAEVINTX |

**匹配 KB 内容**:
  - `md_dmFA_ex_a148` [knowledge_base/domains/FA/examples.md]
    > | Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FAORRES | FACOLSRT | VISITNUM | VISIT | FADTC | FAEVINTX |
|-----|---------|--------|---------|-------|--------|------

**你的判定**: WRONG: EQUIVALENT

---

### #12 `ig34_p0301_a018`
- **Source**: SDTMIG_v3.4 p.301  |  **Type**: LIST_ITEM  |  **Section**: §6.3.7.5 Ophthalmic Examinations (OE)
- **Verdict**: `EXACT`  |  **Similarity**: 0.855

**PDF 原文**:
> Row 3: Represents an abnormality observed during the anterior segment examination of the right eye. OEDIR="MULTIPLE" and indicates multiple directionality values are applicable. OELOC, OELAT, and the multiple OEDIR values specify the location of the abnormality represented in the observed abnormality (i.e., red visible) was determined to be clinically significant (OECLSIG="Y").

**匹配 KB 内容**:
  - `md_dmOE_ex_a005` [knowledge_base/domains/OE/examples.md]
    > **Row 3:** Represents an abnormality observed during the anterior segment examination of the right eye. OEDIR="MULTIPLE" and indicates multiple directionality values are applicable. OELOC, OELAT, and 

**你的判定**: WRONG: EQUIVALENT

---

## EQUIVALENT (18 atoms)

### #13 `ig34_p0356_a018`
- **Source**: SDTMIG_v3.4 p.356  |  **Type**: TABLE_ROW  |  **Section**: §6.3.12.3 Tumor Identification/Tumor Results Examples
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.900

**PDF 原文**:
> | 3 | ABC | TU | 55555 | 3 | R1-T03 | TUMIDENT | Tumor Identification | TARGET | TARGET | THYROID GLAND | RIGHT | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | -3 |

**匹配 KB 内容**:
  - `md_dmTU_ex_a061` [knowledge_base/domains/TU/examples.md]
    > | 3 | ABC | TU | 55555 | 3 | R1-T03 | TUMIDENT | Tumor Identification | TARGET | TARGET | THYROID GLAND | RIGHT | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-0

**你的判定**: WRONG: PARTIAL

---

### #14 `ig34_p0074_a002`
- **Source**: SDTMIG_v3.4 p.74  |  **Type**: SENTENCE  |  **Section**: §5.2 [Demographics (DM)]
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.823

**PDF 原文**:
> Collected race, which is the specific race subcategory (or subcategories) selected by each subject, is represented in SUPPDM to ensure subject self-identification and/or country-specific requirements are available for reference.

**匹配 KB 内容**:
  - `md_dmDM_ex_a164` [knowledge_base/domains/DM/examples.md]
    > Collected race, which is the specific race subcategory for each subject, is represented in SUPPDM to ensure subject self-identification and/or country-specific requirements are available for reference

**你的判定**: CORRECT

---

### #15 `ig34_p0113_a016`
- **Source**: SDTMIG v3.4 (no header footer).pdf p.113  |  **Type**: TABLE_ROW  |  **Section**: §6.1.3.3 [Exposure/Exposure as Collected Examples]
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.900

**PDF 原文**:
> 2 | ABC | EC | ABC4001 | 2 | BOTTLE C | Y | Y | 1 | TABLET | QD | TREATMENT | 2011-01-14 | 2011-01-28 | 1 | 15

**匹配 KB 内容**:
  - `md_dmEC_ex_a027` [knowledge_base/domains/EC/examples.md]
    > | 1 | ABC | EC | ABC4001 | 1 | BOTTLE A | Y | Y | 1 | TABLET | QD | TREATMENT | 2011-01-14 | 2011-01-28 | 1 | 15 |

**你的判定**: WRONG: PARTIAL

---

### #16 `ig34_p0253_a006`
- **Source**: SDTMIG_v3.4 p.253  |  **Type**: CODE_LITERAL  |  **Section**: §6.3.5.7.2 Microbiology Susceptibility (MS)
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.232

**PDF 原文**:
> MSAGENT

**匹配 KB 内容**:
  - `md_dmMS_ex_a027` [knowledge_base/domains/MS/examples.md]
    > | Row | STUDYID | DOMAIN | USUBJID | NHOID | MSGRPID | MSSEQ | MSREFID | MSTESTCD | MSTEST | MSAGENT | MSORRES | MSORRESU | MSSTRESC | MSSTRESN | MSSTRESU | MSNAM | MSMETHOD | VISITNUM | VISIT | MSDTC

**你的判定**: WRONG: PARTIAL

---

### #17 `ig34_p0357_a010`
- **Source**: SDTMIG_v3.4 p.357  |  **Type**: TABLE_ROW  |  **Section**: §6.3.12.3 Tumor Identification/Tumor Results Examples
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.900

**PDF 原文**:
> | 11 | ABC | TR | 55555 | 11 | TARGET | A2 | | SUMDIAM | Sum of Diameter | 25 | mm | 25 | 25 | mm | ACE IMAGING | | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |

**匹配 KB 内容**:
  - `md_dmTR_ex_a066` [knowledge_base/domains/TR/examples.md]
    > | 11 | ABC | TR | 55555 | 11 | TARGET | A2 | | SUMDIAM | Sum of Diameter | 25 | mm | 25 | 25 | mm | | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | | |

**你的判定**: WRONG: PARTIAL

---

### #18 `ig34_p0200_a013`
- **Source**: SDTMIG_v3.4 p.200  |  **Type**: TABLE_ROW  |  **Section**: §6.3.5.3 Cell Phenotype Findings (CP)
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.438

**PDF 原文**:
> | DOMAIN | Domain Abbreviation | Char | CP | Identifier | Two-character abbreviation for the domain. | Req |

**匹配 KB 内容**:
  - `md_dmCP_ex_a023` [knowledge_base/domains/CP/examples.md]
    > | 7 | ABCD | CP | ABCD-001-001 | 7 | TLYLY | TLym/Lym | CD45+CD3+CD19-CD14-CD56-/CD45+FSC SSC | IMMUNOPHENOTYPING | 64.8 | % | 64.8 | 64.8 | | QUANTITATIVE | NUMBER FRACTION | BLOOD | FLOW CYTOMETRY |

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

### #19 `ig34_p0129_a002`
- **Source**: SDTMIG v3.4 (no header footer).pdf p.129  |  **Type**: HEADING  |  **Section**: §6.1.6 [Substance Use (SU)]
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.486
- **Discrepancy**: Section heading equivalent (score=0.486)

**PDF 原文**:
> SU – Description/Overview

**匹配 KB 内容**:
  - `md_dmSU_assn_a001` [knowledge_base/domains/SU/assumptions.md]
    > # SU — Assumptions

**你的判定**: WRONG: MISPLACED

---

### #20 `ig34_p0324_a012`
- **Source**: SDTMIG_v3.4 p.324  |  **Type**: TABLE_ROW  |  **Section**: §6.3.9.2 Questionnaires (QS) — QS-Specification
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.432

**PDF 原文**:
> | DOMAIN | Domain Abbreviation | Char | QS | Identifier | Two-character abbreviation for the domain. | Req |

**匹配 KB 内容**:
  - `md_dmQS_ex_a009` [knowledge_base/domains/QS/examples.md]
    > | 2 | CDISC01 | QS | CDISC01.100008 | 2 | SWLS0102 | SWLS01-My Life Conditions are Excellent | SWLS | Neither agree nor disagree | 4 | 4 | Y | 1 | 2003-04-15 | 1 |

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

### #21 `ig34_p0447_a017`
- **Source**: SDTMIG_v3.4 p.447  |  **Type**: SENTENCE  |  **Section**: Appendix C: Controlled Terminology
- **Verdict**: `EQUIVALENT`  |  **Similarity**: —
- **Discrepancy**: [T5: confirmed present in KB after T4b Wave1/2/3 repairs]

**PDF 原文**:
> Appendix C1 will be considered for expansion in the next version, to contain a complete list of supplemental qualifiers used in the SDTMIG.

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: CORRECT

---

### #22 `ig34_p0271_a006`
- **Source**: SDTMIG_v3.4 p.271  |  **Type**: TABLE_ROW  |  **Section**: §6.3.5.9.1 Pharmacokinetics Concentrations (PC)
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.684

**PDF 原文**:
> 26 | ABC-123 | PC | 123-0001 | 26 | Day 11 | A554134- 19 | PH | PH | SPECIMEN PROPERTY | URINE | 5.5 | | 5.5 | | | | | 3 | DAY 11 | 11 | 2001-02- 11T14:03 | 2001-02- 11T20:10 | 11 | 12H | 12 | Day 11 Dose | 2001-02- 11T08:00 | PT12H | -PT6H |

**匹配 KB 内容**:
  - `md_dmPC_ex_a035` [knowledge_base/domains/PC/examples.md]
    > | 20 | ABC-123 | PC | 1235154 | 20 | DRUGA_DAY11 | 625154 | PH | PH | SPECIMEN PROPERTY | 6.1 | | 6.1 | 6.1 | | URINE | | | | 2001-03-07 | 2001-03-07 | 11 | 12h post | 12 | Day 11 Dose | 2001-03-07T08

**你的判定**: WRONG: PARTIAL

---

### #23 `ig34_p0170_a0012`
- **Source**: ? p.170  |  **Type**: TABLE_ROW  |  **Section**: §6.2.5 Healthcare Encounters (HO)
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 1.000
- **Discrepancy**: PDF missing HOENDTC (2011-07-02); extra empty column separator

**PDF 原文**:
> | 8 | ABC | HO | ABC123102 | 1 | HOSPITAL | | INITIAL HOSPITALIZATION | 2011-06-19 | | | |

**匹配 KB 内容**:
  - `md_dmHO_ex_a047` [knowledge_base/domains/HO/examples.md]
    > | 8 | ABC | HO | ABC123102 | 1 | HOSPITAL | INITIAL HOSPITALIZATION | 2011-06-19 | 2011-07-02 | | |

**你的判定**: WRONG: PARTIAL

---

### #24 `ig34_p0018_a026`
- **Source**: SDTMIG_v3.4 p.18  |  **Type**: TABLE_ROW  |  **Section**: §3.2.1 Dataset-level Metadata
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.900

**PDF 原文**:
> CP | Cell Phenotype Findings | Findings | One record per test per specimen per timepoint per visit per subject | Tabulation | STUDYID, USUBJID, CPTESTCD, CPSPEC, VISITNUM, CPTPTREF, CPTPTNUM | cp.xpt

**匹配 KB 内容**:
  - `md_ch03_a045` [knowledge_base/chapters/ch03_submitting_data.md]
    > | CP | Cell Phenotype Findings | Findings | One record per test per specimen per timepoint per visit per subject | Tabulation | STUDYID, USUBJID, CPTESTCD, CPSPEC, VISITNUM, CPTPTREF, CPTPTNUM | cp.xp

**你的判定**: CORRECT

---

### #25 `ig34_p0198_a009`
- **Source**: SDTMIG_v3.4 p.198  |  **Type**: HEADING  |  **Section**: §6.3.5.2 Biospecimen Findings (BS)
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 1.000

**PDF 原文**:
> BS – Assumptions

**匹配 KB 内容**:
  - `md_dmBS_assn_a001` [knowledge_base/domains/BS/assumptions.md]
    > # BS — Assumptions

**你的判定**: CORRECT

---

### #26 `ig34_p0038_a016`
- **Source**: SDTMIG_v3.4 p.38  |  **Type**: NOTE  |  **Section**: §4.3.7 Use of "Yes" and "No" Values
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.900

**PDF 原文**:
> Note: Permissible values for variables with controlled terms of "Y" or "N" may be extended to include "U" or "NA" if it is the sponsor's practice to explicitly collect or derive values indicating "Unknown" or "Not Applicable" for that variable.

**匹配 KB 内容**:
  - `md_ch04_a473` [knowledge_base/chapters/ch04_general_assumptions.md]
    > > **Note:** Permissible values for variables with controlled terms of "Y" or "N" may be extended to include "U" or "NA" if it is the sponsor's practice to explicitly collect or derive values indicatin

**你的判定**: CORRECT

---

### #27 `ig34_p0175_a0004`
- **Source**: SDTMIG_v3.4 p.175  |  **Type**: LIST_ITEM  |  **Section**: §6.2.6 Medical History (MH)
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.638

**PDF 原文**:
> Rows 1-3: MHCAT indicates that these data were collected on the General Medical History CRF, and MHSCAT indicates the body system for which the event was collected. The reported events were coded using a standard dictionary. MHDECOD and MHBODSYS display the preferred term and body system assigned through the coding process. MHENRTPT was populated based on the response to the "Ongoing" question on 

**匹配 KB 内容**:
  - `md_dmMH_assn_a008` [knowledge_base/domains/MH/assumptions.md]
    >    e. If a CRF collects medical history by prespecified body systems and the sponsor also codes reported terms using a standard dictionary, then MHDECOD and MHBODSYS are populated using the standard d
  - `md_dmMH_assn_a010` [knowledge_base/domains/MH/assumptions.md]
    >    a. MHCAT and MHSCAT may be populated with the sponsor's predefined categorization of medical history events, which are often prespecified on the CRF. Note that even if the sponsor uses the body sys
  - `md_dmMH_assn_a015` [knowledge_base/domains/MH/assumptions.md]
    >    a. Information on medical history is generally collected in 2 different ways, either by recording free text or using a prespecified list of terms. The solicitation of information on specific medica

**你的判定**: CORRECT

---

### #28 `ig34_p0278_a040`
- **Source**: SDTMIG_v3.4 p.278  |  **Type**: TABLE_ROW  |  **Section**: §6.3.5.9.3 Relating PP Records to PC Records — Example 1
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.500

**PDF 原文**:
> 7 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 6 | | 1

**匹配 KB 内容**:
  - `md_dmPP_ex_a043` [knowledge_base/domains/PP/examples.md]
    > | 7 | ABC-123 | PP | 123-1001 | PPSEQ | 7 | PKCOND | Condition of PK Analysis | SINGLE DOSE | Collected | |

**你的判定**: WRONG: ERROR

---

### #29 `ig34_p0048_a019`
- **Source**: SDTMIG_v3.4 p.48  |  **Type**: TABLE_ROW  |  **Section**: §4.4.10 [Representing Time Points]
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.825

**PDF 原文**:
> PERIOD 2, DAY 1 | 5 | 1H | 2 | PM DOSE

**匹配 KB 内容**:
  - `md_ch04_a737` [knowledge_base/chapters/ch04_general_assumptions.md]
    > | PERIOD 1 | 3 | PRE-DOSE | 1 | DAY 1, AM DOSE |

**你的判定**: WRONG: ERROR

---

### #30 `ig34_p0278_a035`
- **Source**: SDTMIG_v3.4 p.278  |  **Type**: TABLE_ROW  |  **Section**: §6.3.5.9.3 Relating PP Records to PC Records — Example 1
- **Verdict**: `EQUIVALENT`  |  **Similarity**: 0.500

**PDF 原文**:
> 2 | ABC-123 | PP | ABC-123-0001 | PPSEQ | 1 | | 1

**匹配 KB 内容**:
  - `md_dmPP_ex_a043` [knowledge_base/domains/PP/examples.md]
    > | 7 | ABC-123 | PP | 123-1001 | PPSEQ | 7 | PKCOND | Condition of PK Analysis | SINGLE DOSE | Collected | |

**你的判定**: WRONG: ERROR

---

## PARTIAL (12 atoms)

### #31 `ig34_p0119_a013`
- **Source**: SDTMIG v3.4 (no header footer).pdf p.119  |  **Type**: CODE_LITERAL  |  **Section**: §6.1.3.3 [Exposure/Exposure as Collected Examples]
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.690

**PDF 原文**:
> relrec.xpt

**匹配 KB 内容**:
  - `md_ch04_a062` [knowledge_base/chapters/ch04_general_assumptions.md]
    > **relrec.xpt**

**你的判定**: WRONG: EXACT

---

### #32 `sv20_p0006_a012`
- **Source**: SDTM_v2.0 p.6  |  **Type**: SENTENCE  |  **Section**: §1.4 Significant Changes from Prior Versions
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.395
- **Discrepancy**: SDTM v2.0 combined tables for GOC; KB covers domain specification table structure

**PDF 原文**:
> For each general observation class, 1 table of variables was created by combining former tables for the topic variable and the qualifier variables.

**匹配 KB 内容**:
  - `md_ch01_a067` [knowledge_base/chapters/ch01_introduction.md]
    > A domain specification table includes rows for all required and expected variables and for a set of permissible variables.

**你的判定**: WRONG: ERROR

---

### #33 `sv20_p0011_a020`
- **Source**: SDTM_v2.0 p.11  |  **Type**: SENTENCE  |  **Section**: §3.1 The General Observation Classes
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.461

**PDF 原文**:
> As a general rule, any valid identifier or timing variable is permissible for use in any dataset based on a general observation class.

**匹配 KB 内容**:
  - `md_ch03_a009` [knowledge_base/chapters/ch03_submitting_data.md]
    > The domain models in Section 6, Domain Models Based on the General Observation Classes, illustrate how to apply the SDTM when creating a specific domain dataset.

**你的判定**: WRONG: ERROR

---

### #34 `ig34_p0193_a006`
- **Source**: SDTMIG_v3.4 p.193  |  **Type**: TABLE_HEADER  |  **Section**: §6.3.4 Inclusion/Exclusion Criteria Not Met (IE)
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.406
- **Discrepancy**: Best match score 0.4065 below equivalence threshold

**PDF 原文**:
> | Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |

**匹配 KB 内容**:
  - `md_dmIE_ex_a007` [knowledge_base/domains/IE/examples.md]
    > | Row | STUDYID | DOMAIN | USUBJID | IESEQ | IESPID | IETESTCD | IETEST | IECAT | IEORRES | IESTRESC | VISITNUM | VISIT | VISITDY | IEDTC | IEDY |
|-----|---------|--------|---------|-------|--------|

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

### #35 `ig34_p0044_a013`
- **Source**: SDTMIG_v3.4 p.44  |  **Type**: SENTENCE  |  **Section**: §4.4.7 [Use of Relative Timing Variables]
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.510
- **Discrepancy**: Candidate contains partial match of PDF content

**PDF 原文**:
> Assumptions:

**匹配 KB 内容**:
  - `md_ch04_a814` [knowledge_base/chapters/ch04_general_assumptions.md]
    > ## 4.5 Other Assumptions

**你的判定**: WRONG: MISPLACED

---

### #36 `ig34_p0037_a016`
- **Source**: SDTMIG_v3.4 p.37  |  **Type**: HEADING  |  **Section**: §4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.785
- **Discrepancy**: MD covers subset of PDF content (score 0.78)

**PDF 原文**:
> 4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables

**匹配 KB 内容**:
  - `md_ch04_a441` [knowledge_base/chapters/ch04_general_assumptions.md]
    > ### 4.3.5 Storing Controlled Terminology for Synonym Qualifier Variables (MedDRA and WHODrug)

**你的判定**: WRONG: EQUIVALENT

---

### #37 `ig34_p0134_a008`
- **Source**: SDTMIG_v3.4 p.134  |  **Type**: TABLE_ROW  |  **Section**: §6.2.1 [Adverse Events (AE)]
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.429

**PDF 原文**:
> | AESEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. | Req |

**匹配 KB 内容**:
  - `md_dmAE_ex_a018` [knowledge_base/domains/AE/examples.md]
    > | 2 | ABC123 | AE | 123101 | 2 | BACK PAIN FOR 5 HOURS | Back pain | Back pain | Musculoskeletal and connective tissue disorders | MODERATE | N | DOSE REDUCED | RELATED | PROBABLY RELATED | RECOVERED/

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

### #38 `ig34_p0136_a011`
- **Source**: SDTMIG_v3.4 p.136  |  **Type**: TABLE_ROW  |  **Section**: §6.2.1 [Adverse Events (AE)]
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.452

**PDF 原文**:
> | AETOXGR | Standard Toxicity Grade | Char | * | Record Qualifier | Toxicity grade according to a standard toxicity scale (e.g., Common Terminology Criteria for Adverse Events, CTCAE). Sponsors should specify the name of the scale and version used in the metadata (see assumption 7d). If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). | Perm |

**匹配 KB 内容**:
  - `md_dmAE_assn_a029` [knowledge_base/domains/AE/assumptions.md]
    >       | If yes, check all that apply: | [ ] Fatal  [ ] Life-threatening  [ ] Inpatient hospitalization or prolongation of existing hospitalization  [ ] Persistent or significant disability/incapacity 

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

### #39 `ig34_p0043_a018`
- **Source**: SDTMIG_v3.4 p.43  |  **Type**: SENTENCE  |  **Section**: §4.4.7 [Use of Relative Timing Variables]
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.465
- **Discrepancy**: Candidate contains partial match of PDF content

**PDF 原文**:
> If --ENRF is used, then --ENRF = "AFTER" means that the event did not end before or during the study reference period.

**匹配 KB 内容**:
  - `md_ch04_a662` [knowledge_base/chapters/ch04_general_assumptions.md]
    > *Medical event began in 2002 and was ongoing at the reference time point of 2006-11-02. The event may or may not have ended at any time after that.*

**你的判定**: CORRECT

---

### #40 `ig34_p0355_a019`
- **Source**: SDTMIG_v3.4 p.355  |  **Type**: TABLE_ROW  |  **Section**: §6.3.12.3 Tumor Identification/Tumor Results Examples
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.900
- **Discrepancy**: TRSEQ differs: PDF=18, MD=17

**PDF 原文**:
> | 18 | ABC | TR | 44444 | 18 | TARGET | A2 | | ACNSD | Absolute Change Nadir in Sum of Diam | -32 | mm | -32 | -32 | mm | | | | INVESTIGATOR | 40 | WEEK 6 | | |

**匹配 KB 内容**:
  - `md_dmTR_ex_a031` [knowledge_base/domains/TR/examples.md]
    > | 17 | ABC | TR | 44444 | 17 | TARGET | A2 | | ACNSD | Absolute Change Nadir in Sum of Diam | -32 | mm | -32 | -32 | mm | | | | INVESTIGATOR | 40 | | WEEK 6 | |

**你的判定**: CORRECT

---

### #41 `ig34_p0265_a010`
- **Source**: SDTMIG_v3.4 p.265  |  **Type**: TABLE_ROW  |  **Section**: §6.3.5.8 Microscopic Findings (MI)
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.432
- **Discrepancy**: Candidate contains partial match; review required

**PDF 原文**:
> VISITNUM | Visit Number | Num | | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. | Exp

**匹配 KB 内容**:
  - `md_dmMI_ex_a025` [knowledge_base/domains/MI/examples.md]
    > | 1 | ABC | MI | ABC-1001 | 1 | 1 | ESTRCPT | Estrogen Receptor | ALLRED PROPORTION POSITIVE SCORE | 3 | 3 | 3 | TISSUE | BREAST | IHC | | SCREENING | 2001-06-15 |

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

### #42 `ig34_p0250_a025`
- **Source**: SDTMIG_v3.4 p.250  |  **Type**: TABLE_ROW  |  **Section**: §6.3.5.7.1 Microbiology Specimen (MB)
- **Verdict**: `PARTIAL`  |  **Similarity**: 0.450
- **Discrepancy**: Table structure differs

**PDF 原文**:
> | MBTPT | Planned Time Point Name | Char | | Timing | Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MBTPTNUM and MBTPTREF. Examples: "Start", "5 min post". | Perm |

**匹配 KB 内容**:
  - `md_dmMB_ex_a045` [knowledge_base/domains/MB/examples.md]
    > | 4 | ABC | BE | ABC-01-101 | BEREFID | SP01 | BECLMETH | Specimen Collection Method | EXPECTORATION | CRF |

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

## MISPLACED (4 atoms)

### #43 `sv20_p0005_a010`
- **Source**: SDTM_v2.0 p.5  |  **Type**: HEADING  |  **Section**: §1.4 Significant Changes from Prior Versions
- **Verdict**: `MISPLACED`  |  **Similarity**: 0.575
- **Discrepancy**: MISPLACED: pdf §1.4 sub-heading 'Reorganization of Content' vs md §1.2 'Organization of this Document'

**PDF 原文**:
> Reorganization of Content

**匹配 KB 内容**:
  - `md_ch01_a010` [knowledge_base/chapters/ch01_introduction.md]
    > ## 1.2 Organization of this Document

**你的判定**: CORRECT

---

### #44 `sv20_p0061_a011`
- **Source**: SDTM_v2.0 p.61  |  **Type**: TABLE_ROW  |  **Section**: §5.2.1 Device Identifiers Dataset
- **Verdict**: `MISPLACED`  |  **Similarity**: 0.543
- **Discrepancy**: MISPLACED: pdf §5.2.1 Device Identifiers Dataset vs md §8.2.1 Related Records (RELREC)

**PDF 原文**:
> 1 | STUDYID | Study Identifier | Char | | Identifier | | | C83082 | A sequence of characters used by the sponsor to uniquely identify the study. | | | |

**匹配 KB 内容**:
  - `md_ch08_a073` [knowledge_base/chapters/ch08_relationships.md]
    > | STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |

**你的判定**: CORRECT

---

### #45 `ig34_p0104_a011`
- **Source**: SDTMIG_v3.4 p.104  |  **Type**: TABLE_ROW  |  **Section**: §6.1.3.1 [Exposure (EX)]
- **Verdict**: `MISPLACED`  |  **Similarity**: 0.439
- **Discrepancy**: MISPLACED: pdf §§6.1.3.1 [Exposure (EX)] vs md §§EX.2 [Example 2]

**PDF 原文**:
> EXSEQ | Sequence Number | Num | | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

**匹配 KB 内容**:
  - `md_dmEX_ex_a061` [knowledge_base/domains/EX/examples.md]
    > | 1 | ABC | EX | ABC3001 | 1 | | V3 | DRUG X | 3 | mg/kg | INJECTION | ONCE | SUBCUTANEOUS | ABDOMEN | 3 | VISIT 3 | TREATMENT | 2009-05-10 | 2009-05-10 | 21 | 21 |

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

### #46 `ig34_p0094_a011`
- **Source**: SDTMIG_v3.4 p.94  |  **Type**: LIST_ITEM  |  **Section**: §6.1.1 [Procedure Agents (AG)]
- **Verdict**: `MISPLACED`  |  **Similarity**: 1.000
- **Discrepancy**: MISPLACED: pdf §§6.1.1 [Procedure Agents (AG)] vs md §§AG [AG — Assumptions]

**PDF 原文**:
> b. The Exposure (EX) domain also seemed inappropriate; although the testing procedure might be part of the study plan, these data would not be used or analyzed in the same way as data about study treatments. The AG domain was created to fill this gap.

**匹配 KB 内容**:
  - `md_dmAG_assn_a004` [knowledge_base/domains/AG/assumptions.md]
    >    b. The Exposure (EX) domain also seemed inappropriate; although the testing procedure might be part of the study plan, these data would not be used or analyzed in the same way as data about study t

**你的判定**: WRONG: EQUIVALENT

---

## ERROR (4 atoms)

### #47 `ig34_p0126_a001`
- **Source**: SDTMIG v3.4 (no header footer).pdf p.126  |  **Type**: TABLE_HEADER  |  **Section**: §6.1.5 [Procedures (PR)]
- **Verdict**: `ERROR`  |  **Similarity**: 0.435

**PDF 原文**:
> | Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format¹ | Role | CDISC Notes | Core |

**匹配 KB 内容**:
  - `md_dmPR_ex_a025` [knowledge_base/domains/PR/examples.md]
    > | Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

### #48 `ig34_p0126_a020`
- **Source**: SDTMIG v3.4 (no header footer).pdf p.126  |  **Type**: TABLE_ROW  |  **Section**: §6.1.5 [Procedures (PR)]
- **Verdict**: `ERROR`  |  **Similarity**: 0.428

**PDF 原文**:
> | PRRFTDTC | Date/Time of Reference Time Point | Char | ISO 8601 datetime or interval | Timing | Date/time for a fixed reference time point defined by PRTRTREF in ISO 8601 character format. | Perm |

**匹配 KB 内容**:
  - `md_dmPR_ex_a021` [knowledge_base/domains/PR/examples.md]
    > | 2 | ABC123 | EG | ABC123-001 | 2 | 20110101_20110102 | EGHRMAX | ECG Maximum Heart Rate | 100 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

### #49 `ig34_p0383_a004`
- **Source**: SDTMIG_v3.4 p.383  |  **Type**: TABLE_ROW  |  **Section**: §7.1.2 Definitions of Trial Design Concepts
- **Verdict**: `ERROR`  |  **Similarity**: 0.424
- **Discrepancy**: ERROR: KB entry contradicts PDF source

**PDF 原文**:
> | Treatments | The word "treatment" may be used in connection with epochs, study cells, or elements, but has somewhat different meanings in each context: Because epochs cut across arms, an epoch treatment is at a high level that does not specify anything that differs between arms. For example, in a 3-period crossover study of 3 doses of drug X, each treatment epoch is associated with drug X, but n

**匹配 KB 内容**:
  - `md_ch10_a230` [knowledge_base/chapters/ch10_appendices.md]
    > | 7.4.2 | Trial Summary (TS) | Changed the CDISC Notes for TSSEQ to reflect that the sequence number is to ensure uniqueness within a parameter; revisions to most TS assumptions to remove references t

**你的判定**: CORRECT

---

### #50 `ig34_p0126_a018`
- **Source**: SDTMIG v3.4 (no header footer).pdf p.126  |  **Type**: TABLE_ROW  |  **Section**: §6.1.5 [Procedures (PR)]
- **Verdict**: `ERROR`  |  **Similarity**: 0.432

**PDF 原文**:
> | PRELTM | Planned Elapsed Time from Time Point Ref | Char | ISO 8601 duration | Timing | Planned elapsed time in ISO 8601 format relative to a planned fixed reference (PRTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. | Perm |

**匹配 KB 内容**:
  - `md_dmPR_ex_a032` [knowledge_base/domains/PR/examples.md]
    > | 1 | ABC123 | PR | ABC123-1001 | 1 | External beam radiation therapy | 70 | Gy | BREAST | RIGHT | 2011-06-01 | 2011-06-25 |

**你的判定**: WRONG: INTENTIONAL_EXCLUDE

---

## INTENTIONAL_EXCLUDE (8 atoms)

### #51 `ig34_p0306_a002`
- **Source**: SDTMIG_v3.4 p.306  |  **Type**: TABLE_ROW  |  **Section**: §6.3.7.6 Reproductive System Findings (RP)
- **Verdict**: `INTENTIONAL_EXCLUDE`  |  **Similarity**: —
- **Exclusion reason**: Domain variable specification table row in §6.3.7.6 Reproductive System Findings (RP) — KB covers spec via spec.md; Excel is authoritative source

**PDF 原文**:
> | RPSTRESN | Numeric Result/Finding in Standard Units | Num | | Result Qualifier | Used for continuous or numeric results or findings in standard format; copied in numeric format from RPSTRESC. RPSTRESN should store all numeric test results or findings. | Perm |

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: CORRECT

---

### #52 `ig34_p0129_a007`
- **Source**: SDTMIG v3.4 (no header footer).pdf p.129  |  **Type**: TABLE_ROW  |  **Section**: §6.1.6 [Substance Use (SU)]
- **Verdict**: `INTENTIONAL_EXCLUDE`  |  **Similarity**: 0.413
- **Discrepancy**: Variable specification row not found as distinct atom in KB (top score=0.413)
- **Exclusion reason**: Domain variable specification table row in §6.1.6 [Substance Use (SU)] — KB covers spec via spec.md; Excel is authoritative source

**PDF 原文**:
> | STUDYID | Study Identifier | Char | | Identifier | Unique identifier for a study. | Req |

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: CORRECT

---

### #53 `ig34_p0299_a001`
- **Source**: SDTMIG_v3.4 p.299  |  **Type**: HEADING  |  **Section**: §6.3.7.5 Ophthalmic Examinations (OE)
- **Verdict**: `INTENTIONAL_EXCLUDE`  |  **Similarity**: —
- **Discrepancy**: OE Specification heading not present as a distinct section in KB
- **Exclusion reason**: Non-content structural heading (figure caption / table divider): "OE – Specification" in §6.3.7.5 Ophthalmic Examinations (OE)

**PDF 原文**:
> OE – Specification

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: CORRECT

---

### #54 `sv20_p0070_a019`
- **Source**: SDTM_v2.0 p.70  |  **Type**: SENTENCE  |  **Section**: §7 [Changes from SDTM v1.8 to SDTM v2.0]
- **Verdict**: `INTENTIONAL_EXCLUDE`  |  **Similarity**: —
- **Exclusion reason**: SDTM v2.0 content superseded by SDTMIG v3.4 — not included in KB by design

**PDF 原文**:
> The variables qualified for --DOSFRM, --DOSFRQ, and --DOSRGM were changed from --DOSE, --DOSTXT, and --DOSTOT to --TRT.

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: CORRECT

---

### #55 `ig34_p0438_a011`
- **Source**: SDTMIG_v3.4 p.438  |  **Type**: NOTE  |  **Section**: RELSUB – Specification
- **Verdict**: `INTENTIONAL_EXCLUDE`  |  **Similarity**: —
- **Exclusion reason**: Variable specification table covered by xlsx-derived spec.md — not included in KB chapters by design

**PDF 原文**:
> 1 In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: CORRECT

---

### #56 `ig34_p0098_a006`
- **Source**: SDTMIG_v3.4 p.98  |  **Type**: TABLE_HEADER  |  **Section**: §6.1.2 [Concomitant/Prior Medications (CM)]
- **Verdict**: `INTENTIONAL_EXCLUDE`  |  **Similarity**: —
- **Exclusion reason**: Specification table column header row in §6.1.2 [Concomitant/Prior Medications (CM)] — structural metadata, not KB content

**PDF 原文**:
> Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: CORRECT

---

### #57 `ig34_p0445_a023`
- **Source**: SDTMIG_v3.4 p.445  |  **Type**: TABLE_ROW  |  **Section**: Appendix A: CDISC SDS Team
- **Verdict**: `INTENTIONAL_EXCLUDE`  |  **Similarity**: —
- **Exclusion reason**: Appendix A contributor listing: team member name/affiliation not SDTM content knowledge

**PDF 原文**:
> | Daniel Sinnett | Emmes |

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: CORRECT

---

### #58 `ig34_p0253_a033`
- **Source**: SDTMIG_v3.4 p.253  |  **Type**: TABLE_ROW  |  **Section**: §6.3.5.7.2 Microbiology Susceptibility (MS)
- **Verdict**: `INTENTIONAL_EXCLUDE`  |  **Similarity**: —
- **Exclusion reason**: Domain variable specification table row in §6.3.5.7.2 Microbiology Susceptibility (MS) — KB covers spec via spec.md; Excel is authoritative source

**PDF 原文**:
> | MSREASND | Reason Not Done | Char | | Record Qualifier | Reason not done. Used in conjunction with MSSTAT when value is "NOT DONE". | Perm |

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: CORRECT

---

## MISSING (2 atoms)

### #59 `ig34_p0388_a001`
- **Source**: SDTMIG_v3.4 p.388  |  **Type**: FIGURE  |  **Section**: §7.2.1 Trial Arms (TA) – Example 1
- **Verdict**: `MISSING`  |  **Similarity**: —

**PDF 原文**:
> [FIGURE: Example Trial 1, Parallel Design Prospective View — grid diagram with 3 columns (Screening Epoch, Run-in Epoch, Treatment Epoch) and 3 rows (Placebo arm, Drug A arm, Drug B arm). Each cell shows element block. Arms labeled with arrows (Placebo, Drug A, Drug B) on right. Randomization label with upward arrow at bottom.]

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: WRONG: EQUIVALENT

---

### #60 `ig34_p0387_a011`
- **Source**: SDTMIG_v3.4 p.387  |  **Type**: FIGURE  |  **Section**: §7.2.1 Trial Arms (TA) – Example 1
- **Verdict**: `MISSING`  |  **Similarity**: —

**PDF 原文**:
> [FIGURE: Example Trial 1, Parallel Design Study Schema — block diagram showing Screen block (pink) leading via arrow to Run-In block (blue) with 3 red arrows branching to Placebo (green), Drug A (yellow), Drug B (light blue) blocks. Randomization label with upward arrow at bottom.]

**匹配 KB 内容**:
  _(no matched KB atoms)_

**你的判定**: WRONG: EQUIVALENT

---

