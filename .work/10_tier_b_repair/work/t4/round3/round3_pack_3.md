# T4.1 第三轮补检包 3 — R3_IG34_EQUIV (25 条; 编号 T51-T75)

> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).

### T51. `ig34_p0046_a014` — r3:R3_IG34_EQUIV

- PDF 页 46 · 原子类型 SENTENCE · 所在节 `§4.4.10 [Representing Time Points]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Values for these variables for vital signs measurements taken at 30, 60, and 90 minutes after dosing would look like the following.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0046.txt` 第 22-23 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 21| 
 22| Values for these variables for vital signs measurements taken at 30, 60, and 90 minutes after dosing would look like
 23| the following.
 24| VSTPTNUM     VSTPT    VSELTM       VSTPTREF                VSRFTDTC               VSDTC
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1093` (来源: live valid_hits):

~~~~
1093| Values for these variables for vital signs measurements taken at 30, 60, and 90 minutes after dosing would look like the following.
~~~~

### T52. `ig34_p0077_a021` — r3:R3_IG34_EQUIV

- PDF 页 77 · 原子类型 SENTENCE · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
CDASH recommended QNAM-QLABEL values have been provided.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0077.txt` 第 47-48 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 46| Collected race, which is the specific race subcategory for each subject, is represented in SUPPDM to ensure subject self-identification and/or country-specific
 47| requirements are available for reference. In this example, each subject selected 1 race and 1 race subcategory. CDASH recommended QNAM-QLABEL values
 48| have been provided.
 49| 
~~~~

KB 现文: `knowledge_base/domains/DM/examples.md:212,214,216` (来源: live valid_hits):

~~~~
 212| When a subject selects multiple race values, as USUBJID ABC789-010-047 did, the values selected are represented in SUPPDM. Collected race, which is the specific race subcategory (or subcategories) selected by each subject, is represented in SUPPDM to ensure subject self-identification and/or country-specific requirements are available for reference. CDASH recommended QNAM-QLABEL values have been provided.
 214| **Rows 1, 2:** Show that USUBJID ABC789-010-047 selected 2 RACE values, "ASIAN" and "WHITE". CDASH recommended QNAM-QLABEL values have been provided.
 216| **Rows 3-5:** Show that USUBJID ABC789-010-047 selected 3 collected race (CRACE) values, "CHINESE", "KOREAN", and "RUSSIAN". CDASH recommended QNAM-QLABEL values have been provided.
~~~~

### T53. `ig34_p0101_a009` — r3:R3_IG34_EQUIV

- PDF 页 101 · 原子类型 SENTENCE · 所在节 `§6.1.2 [Concomitant/Prior Medications (CM)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The subject has used the same medication for many years and continues to do so.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0101.txt` 第 9-10 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8|            a.   CMSTRTPT, CMSTTPT, CMENRTPT, and CMENTPT may be populated as necessary to indicate when a medication was used relative to
  9|                 specified time points. For example, assume a subject uses birth control medication. The subject has used the same medication for many years and
 10|                 continues to do so. The date the subject began using the medication (or at least a partial date) would be stored in CMSTDTC. CMENDTC is null
 11|                 because the end date is unknown/has not yet happened. This fact can be recorded by setting CMENTPT = "2007-04-30" (the date the assessment
~~~~

KB 现文: `knowledge_base/domains/CM/assumptions.md:27` (来源: live valid_hits):

~~~~
  27|    a. CMSTRTPT, CMSTTPT, CMENRTPT, and CMENTPT may be populated as necessary to indicate when a medication was used relative to specified time points. For example, assume a subject uses birth control medication. The subject has used the same medication for many years and continues to do so. The date the subject began using the medication (or at least a partial date) would be stored in CMSTDTC. CMENDTC is null because the end date is unknown/has not yet happened. This fact can be recorded by setting CMENTPT = "2007-04-30" (the date the assessment was made) and CMENRTPT = "ONGOING".
~~~~

### T54. `ig34_p0119_a012` — r3:R3_IG34_EQUIV

- PDF 页 119 · 原子类型 SENTENCE · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 4-6:    Represent the many-to-one-to-one relationship between many records in EC (both "SCHEDULED" and "PERFORMED"), one record in EX, and one record in VS (for each visit), using --LNKGRP.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0119.txt` 第 16-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15| Rows 1-3:      Represent the one-to-one-to-one relationship between "PERFORMED" records in EC, records in EX, and records in VS using --LNKID, .
 16| Rows 4-6:      Represent the many-to-one-to-one relationship between many records in EC (both "SCHEDULED" and "PERFORMED"), one record in EX, and one record in VS (for each visit), using --LNKGRP.
 17| relrec.xpt
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:405` (来源: live valid_hits):

~~~~
 405| **Rows 4-6:** Represent the many-to-one-to-one relationship between many records in EC (both "SCHEDULED" and "PERFORMED"), one record in EX, and one record in VS (for each visit), using --LNKGRP.
~~~~

### T55. `ig34_p0119_a030` — r3:R3_IG34_EQUIV

- PDF 页 119 · 原子类型 SENTENCE · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 2:    Shows the missed dose on 2012-01-15, which falls within the overall dosing interval.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0119.txt` 第 39-39 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 38| Row 1:         Shows the overall dosing interval from first dose date to last dose date.
 39| Row 2:         Shows the missed dose on 2012-01-15, which falls within the overall dosing interval.
 40| Row 3:         Shows a doubled dose on 2012-01-16, which also falls within the overall dosing interval.
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:437` (来源: live valid_hits):

~~~~
 437| **Row 2:** Shows the missed dose on 2012-01-15, which falls within the overall dosing interval.
~~~~

### T56. `ig34_p0141_a017` — r3:R3_IG34_EQUIV

- PDF 页 141 · 原子类型 SENTENCE · 所在节 `§6.2.1 [Adverse Events (AE)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The subject shown in this example experienced nausea and vomiting. The subject did not experience diarrhea, so no record for that term exists in the AE dataset.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0141.txt` 第 33-33 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32| that it was prespecified, but timing information is limited to the date of collection, and other expected qualifiers are not available. RELREC may be used to relate AE records and FA records.
 33| The subject shown in this example experienced nausea and vomiting. The subject did not experience diarrhea, so no record for that term exists in the AE dataset.
 34| ae.xpt
~~~~

KB 现文: `knowledge_base/domains/AE/examples.md:39` (来源: live valid_hits):

~~~~
  39| The subject shown in this example experienced nausea and vomiting. The subject did not experience diarrhea, so no record for that term exists in the AE dataset.
~~~~

### T57. `ig34_p0146_a017` — r3:R3_IG34_EQUIV

- PDF 页 146 · 原子类型 SENTENCE · 所在节 `§6.2.2 [Biospecimen Events (BE)]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Cell-free RNA, which can be obtained from plasma, may be useful for some tumor-specific cancer detection,[1] but has poor integrity.[2]In this example, a blood sample was drawn, centrifuged to get plasma, and stored in a pretreated container before being shipped to the lab. The lab then extracted and purified RNA from the plasma, divided the RNA into 3 aliquots, and sequenced 1 aliquot immediately while freezing and storing the other 2 for later use.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0146.txt` 第 22-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 21| Example 2
 22| Cell-free RNA, which can be obtained from plasma, may be useful for some tumor-specific cancer detection,[1] but has poor integrity.[2]In this example, a blood sample was drawn, centrifuged to get plasma, and
 23| stored in a pretreated container before being shipped to the lab. The lab then extracted and purified RNA from the plasma, divided the RNA into 3 aliquots, and sequenced 1 aliquot immediately while freezing and
 24| storing the other 2 for later use.
 25| Row 1:             Shows the collection of the blood sample.
~~~~

KB 现文: `knowledge_base/domains/BE/examples.md:62-62` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  62| Cell-free RNA, which can be obtained from plasma, may be useful for some tumor-specific cancer detection,[1] but has poor integrity.[2] In this example, a blood sample was drawn, centrifuged to get plasma, and stored in a pretreated container before being shipped to the lab. The lab then extracted and purified RNA from the plasma, divided the RNA into 3 aliquots, and sequenced 1 aliquot immediately while freezing and storing the other 2 for later use.
~~~~

### T58. `ig34_p0151_a0007` — r3:R3_IG34_EQUIV

- PDF 页 151 · 原子类型 SENTENCE · 所在节 `§6.2.3 [Clinical Events]`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In this example, data were collected about prespecified events that, in the context of this study, were not reportable as AEs.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0151.txt` 第 11-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10| Example 1
 11| In this example, data were collected about prespecified events that, in the context of this study, were not reportable as AEs. The data were collected in a log
 12| independent of visits, rather than in visit-based CRF modules, so visit and date of collection (CEDTC) data were not collected.
~~~~

KB 现文: `knowledge_base/domains/CE/examples.md:5` (来源: live valid_hits):

~~~~
   5| In this example, data were collected about prespecified events that, in the context of this study, were not reportable as AEs. The data were collected in a log independent of visits, rather than in visit-based CRF modules, so visit and date of collection (CEDTC) data were not collected.
~~~~

### T59. `ig34_p0208_a012` — r3:R3_IG34_EQUIV

- PDF 页 208 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Example 1a illustrates use of the CPMRKSTR variable for an assay panel that enumerates several of the major named cell subpopulations of leukocytes.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0208.txt` 第 26-27 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25| Example 1
 26| Example 1a illustrates use of the CPMRKSTR variable for an assay panel that enumerates several of the major
 27| named cell subpopulations of leukocytes. For most cases involving simple phenotyping, and when used in
 28| accordance with CP domain guidance, the CPMRKSTR variable is sufficient for providing the marker information
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:9` (来源: live valid_hits):

~~~~
   9| Example 1a illustrates use of the CPMRKSTR variable for an assay panel that enumerates several of the major named cell subpopulations of leukocytes. For most cases involving simple phenotyping, and when used in accordance with CP domain guidance, the CPMRKSTR variable is sufficient for providing the marker information needed to fully describe a test. As such, CPMRKSTR is the only new CP test qualifier variable having a Core designation of "Expected". In such a case, the sponsor may determine whether to include other permissible CP test qualifier variables, based on the needs of the data recipient. This example presents records that might typically be reported for a panel of tests quantifying T-cell, B-cell, monocyte, and natural killer (NK) cell populations, and for subtyping T-cells. In this example, the sponsor determined that none of the permissible CP test qualifier variables were needed to accurately comprehend or distinguish among tests in the dataset, so chose to include only the CPMRKSTR (complete markers string) information.
~~~~

### T60. `ig34_p0218_a007` — r3:R3_IG34_EQUIV

- PDF 页 218 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The example is a use case for data from a receptor occupancy study based on a direct cell-binding assay method to illustrate the use of several new variables.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0218.txt` 第 12-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11| Example 8
 12| The example is a use case for data from a receptor occupancy study based on a direct cell-binding assay method to illustrate the use of several new variables.
 13| In the example, target engagement is assessed by measuring the extent to which a cell-associated target protein (the hypothetical cell marker CDxx) is occupied by a therapeutic antibody (CDxx antibody) intended to
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:263` (来源: live valid_hits):

~~~~
 263| The example is a use case for data from a receptor occupancy study based on a direct cell-binding assay method to illustrate the use of several new variables.
~~~~

### T61. `ig34_p0219_a016` — r3:R3_IG34_EQUIV

- PDF 页 219 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Under certain circumstances, assessment of changes to free or unoccupied receptor (target) binding over the time-course of drug therapy or use of an indirect assay format may be more appropriate than direct detection of a binding agent (e.g., drug, small molecule ligand, protein) to obtain information on the extent of target engagement. Indirect assays of this sort rely on measuring remaining free (unbound) binding site using a labeled competitive detection probe (e.g., antibody or other ligand) that binds to the remaining available sites on the target; that is, those sites not already occupied by treating with the therapeutic. (Occupancy of the target by the therapeutic agent is then calculated as the difference between the total number of binding sites and the number of free binding sites detected by the probe.) In addition to measuring the free binding sites, a second labeled probe which binds to a non-interfering alternate site on the target (i.e., is non-competitive with the therapeutic molecule) may be used to assess the total amount of the target molecule expressed on cells (not binding sites) in order to monitor whether therapy changed the number of targets available relative to baseline expression. This allows results to be interpreted as a change in occupancy as opposed to a change in the number of targets available.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0219.txt` 第 59-64 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 58| reported.
 59| Under certain circumstances, assessment of changes to free or unoccupied receptor (target) binding over the time-course of drug therapy or use of an indirect assay format may be more appropriate than direct
 60| detection of a binding agent (e.g., drug, small molecule ligand, protein) to obtain information on the extent of target engagement. Indirect assays of this sort rely on measuring remaining free (unbound) binding site
 61| using a labeled competitive detection probe (e.g., antibody or other ligand) that binds to the remaining available sites on the target; that is, those sites not already occupied by treating with the therapeutic. (Occupancy
 62| of the target by the therapeutic agent is then calculated as the difference between the total number of binding sites and the number of free binding sites detected by the probe.) In addition to measuring the free binding
 63| sites, a second labeled probe which binds to a non-interfering alternate site on the target (i.e., is non-competitive with the therapeutic molecule) may be used to assess the total amount of the target molecule expressed
 64| on cells (not binding sites) in order to monitor whether therapy changed the number of targets available relative to baseline expression. This allows results to be interpreted as a change in occupancy as opposed to a
 65| change in the number of targets available.
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:297` (来源: live valid_hits):

~~~~
 297| Under certain circumstances, assessment of changes to free or unoccupied receptor (target) binding over the time-course of drug therapy or use of an indirect assay format may be more appropriate than direct detection of a binding agent (e.g., drug, small molecule ligand, protein) to obtain information on the extent of target engagement. Indirect assays of this sort rely on measuring remaining free (unbound) binding site using a labeled competitive detection probe (e.g., antibody or other ligand) that binds to the remaining available sites on the target; that is, those sites not already occupied by treating with the therapeutic. (Occupancy of the target by the therapeutic agent is then calculated as the difference between the total number of binding sites and the number of free binding sites detected by the probe.) In addition to measuring the free binding sites, a second labeled probe which binds to a non-interfering alternate site on the target (i.e., is non-competitive with the therapeutic molecule) may be used to assess the total amount of the target molecule expressed on cells (not binding sites) in order to monitor whether therapy changed the number of targets available relative to baseline expression. This allows results to be interpreted as a change in occupancy as opposed to a change in the number of targets available.
~~~~

### T62. `ig34_p0227_a019` — r3:R3_IG34_EQUIV

- PDF 页 227 · 原子类型 SENTENCE · 所在节 `§6.3.5.4 Genomics Findings (GF)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Next, a series of virus samples extracted from the subject underwent targeted single nucleotide polymorphism (SNP) testing to determine the feasibility of using the neuraminidase inhibitor oseltamivir to treat the infection (i.e., drug susceptibility testing).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0227.txt` 第 33-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 32| 
 33| Next, a series of virus samples extracted from the subject underwent targeted single nucleotide polymorphism (SNP) testing to determine the feasibility of using the neuraminidase inhibitor oseltamivir to treat the
 34| infection (i.e., drug susceptibility testing).
 35| Findings from this testing provide both genetic data in the form of the genotype identified and the susceptibility/resistance data as inferred phenotype. Genotypic findings are represented in the GF domain, and
~~~~

KB 现文: `knowledge_base/domains/GF/examples.md:147` (来源: live valid_hits):

~~~~
 147| Next, a series of virus samples extracted from the subject underwent targeted single nucleotide polymorphism (SNP) testing to determine the feasibility of using the neuraminidase inhibitor oseltamivir to treat the infection (i.e., drug susceptibility testing).
~~~~

### T63. `ig34_p0233_a008` — r3:R3_IG34_EQUIV

- PDF 页 233 · 原子类型 SENTENCE · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
In order to illustrate the distinctive differences between the 3 tiers of ADA testing, the standard variable ISTSTOPO is used to represent the controlled values SCREEN, CONFIRM, and QUANTIFY.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0233.txt` 第 6-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5| Samples that are positive for ADA in the screen assay are then analyzed in a confirmatory assay (tier 2). The samples that are positive for ADA in both the screen and confirmatory tiers of testing are further tested in
  6| tier 3; this frequently includes analysis of antibody titer and neutralizing activity. In order to illustrate the distinctive differences between the 3 tiers of ADA testing, the standard variable ISTSTOPO is used to
  7| represent the controlled values SCREEN, CONFIRM, and QUANTIFY. These values help to describe the operational objective or the reason behind each testing step/tier, and also to provide uniqueness to each row
  8| of record. The study drug AZ-007, which induces the subject's production of, and is the target of the antidrug antibody, is represented by the variable ISBDAGNT. ISGRPID is used in this example to show that the
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:7` (来源: live valid_hits):

~~~~
   7| Tiered testing scheme for ADA evaluation generally includes the following steps: screening, confirmatory, and "characterization" of the antidrug antibody. In tier 1, all evaluable samples are run in a screening assay. Samples that are positive for ADA in the screen assay are then analyzed in a confirmatory assay (tier 2). The samples that are positive for ADA in both the screen and confirmatory tiers of testing are further tested in tier 3; this frequently includes analysis of antibody titer and neutralizing activity. In order to illustrate the distinctive differences between the 3 tiers of ADA testing, the standard variable ISTSTOPO is used to represent the controlled values SCREEN, CONFIRM, and QUANTIFY. These values help to describe the operational objective or the reason behind each testing step/tier, and also to provide uniqueness to each row of record. The study drug AZ-007, which induces the subject's production of, and is the target of the antidrug antibody, is represented by the variable ISBDAGNT. ISGRPID is used in this example to show that the records are related to each other; in this particular case, tests are done in a tiered, sequential manner from screen to confirm to quantification of the detected antidrug antibody.
~~~~

### T64. `ig34_p0237_a004` — r3:R3_IG34_EQUIV

- PDF 页 237 · 原子类型 SENTENCE · 所在节 `§6.3.5.5 Immunogenicity Specimen Assessments (IS)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Traditional methods such as enzyme-linked immunosorbent assay (ELISA) that monitor humoral immune responses after immunization or infection typically only quantify specific antibody titers in serum. These methods do not provide any information about the actual number and location of the immune cells that secrete antibodies or cytokines.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0237.txt` 第 5-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  4| This example shows data about the assessment of antibody-secreting cells (ASCs).
  5| Traditional methods such as enzyme-linked immunosorbent assay (ELISA) that monitor humoral immune responses after immunization or infection typically only quantify specific antibody titers in serum. These
  6| methods do not provide any information about the actual number and location of the immune cells that secrete antibodies or cytokines.
  7| The enzyme-linked immunospot (ELISpot) assay is a method to detect and quantify analyte-secreting T or B cells. During ELISpot testing, a colored precipitate forms and appears as spots at the sites of analyte
~~~~

KB 现文: `knowledge_base/domains/IS/examples.md:129` (来源: live valid_hits):

~~~~
 129| Traditional methods such as enzyme-linked immunosorbent assay (ELISA) that monitor humoral immune responses after immunization or infection typically only quantify specific antibody titers in serum. These methods do not provide any information about the actual number and location of the immune cells that secrete antibodies or cytokines.
~~~~

### T65. `ig34_p0246_a006` — r3:R3_IG34_EQUIV

- PDF 页 246 · 原子类型 SENTENCE · 所在节 `§6.3.5.6 Laboratory Test Results (LB)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example illustrates the use of previously published LB domain variables and introduces several new variables that were added to SDTMv2.0, including LBTSTCND, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBTMTHSN, LBPTFL, and LBPDUR. These variables, in part, aid in harmonization to LOINC.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0246.txt` 第 12-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 11| Example 1
 12| This example illustrates the use of previously published LB domain variables and introduces several new variables that were added to SDTMv2.0,
 13| including LBTSTCND, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBTMTHSN, LBPTFL, and LBPDUR. These variables, in part, aid in
 14| harmonization to LOINC.
 15| Row 1:           Shows a value collected in 1 unit, but converted to selected standard unit. See Section 4.5.1, Original and Standardized Results of Findings and
~~~~

KB 现文: `knowledge_base/domains/LB/examples.md:5` (来源: live valid_hits):

~~~~
   5| This example illustrates the use of previously published LB domain variables and introduces several new variables that were added to SDTMv2.0, including LBTSTCND, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBTMTHSN, LBPTFL, and LBPDUR. These variables, in part, aid in harmonization to LOINC.
~~~~

### T66. `ig34_p0248_a012` — r3:R3_IG34_EQUIV

- PDF 页 248 · 原子类型 SENTENCE · 所在节 `§6.3.5.6 Laboratory Test Results (LB)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example illustrates the use of the LBBDAGNT variable for a single agent. Note: More complex use cases may require additional concepts for complete modeling. In this simple target engagement assessment, the target protein analytes interact with the binding agent. The use of the word "free" in the descriptions of rows 2 and 4 does not refer to the naturally occurring hepatocyte growth factor receptors or epidermal growth factor receptors, but rather to the receptors not bound to the binding agent. Representing the binding agent shows that what is being measured is the portion of the target receptors not bound to the binding agent, not the concentration of the receptors at their natural state.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0248.txt` 第 16-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 15| Example 5
 16| This example illustrates the use of the LBBDAGNT variable for a single agent. Note: More complex use cases may require additional concepts for complete modeling. In this simple target engagement assessment,
 17| the target protein analytes interact with the binding agent. The use of the word "free" in the descriptions of rows 2 and 4 does not refer to the naturally occurring hepatocyte growth factor receptors or epidermal
 18| growth factor receptors, but rather to the receptors not bound to the binding agent. Representing the binding agent shows that what is being measured is the portion of the target receptors not bound to the binding
 19| agent, not the concentration of the receptors at their natural state.
 20| Row 1:             Shows the total amount of HGFR, both soluble and bound, to the target "ABC-8675309".
~~~~

KB 现文: `knowledge_base/domains/LB/examples.md:90` (来源: live valid_hits):

~~~~
  90| This example illustrates the use of the LBBDAGNT variable for a single agent. **Note:** More complex use cases may require additional concepts for complete modeling. In this simple target engagement assessment, the target protein analytes interact with the binding agent. The use of the word "free" in the descriptions of rows 2 and 4 does not refer to the naturally occurring hepatocyte growth factor receptors or epidermal growth factor receptors, but rather to the receptors not bound to the binding agent. Representing the binding agent shows that what is being measured is the portion of the target receptors not bound to the binding agent, not the concentration of the receptors at their natural state.
~~~~

### T67. `ig34_p0277_a018` — r3:R3_IG34_EQUIV

- PDF 页 277 · 原子类型 SENTENCE · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example uses --GRPID values in the PCGRPID (Example 1) and PPGRPID (Example 1) columns.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0277.txt` 第 19-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18| All PC records used to calculate all pharmacokinetic parameters.
 19| This example uses --GRPID values in the PCGRPID (Example 1) and PPGRPID (Example 1) columns.
 20| Method A (Many to Many, Using PCGRPID and PPGRPID)
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:106-108` (来源: fuzzy locate (score 0.583)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 106| > KB note (not in SDTMIG): The shared PP dataset contains 12 rows showing PK parameters (PPTESTCD TMAX, CMAX, AUCALL, LAMZHL, VZO, CLO) with PPCAT = "DRUG X", for Day 1 and Day 8 (PPNOMDY 1 and 8), with 4 PPGRPID columns, 1 for each of Examples 1-4 of Section 6.3.5.9.3 (shown in PC/examples.md).
 107| 
 108| > See [PC/assumptions.md](../PC/assumptions.md#pc-pp--relating-records) for this table.
~~~~

### T68. `ig34_p0284_a007` — r3:R3_IG34_EQUIV

- PDF 页 284 · 原子类型 SENTENCE · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Relating the datasets (as described in Section 8, Representing Relationships and Data) is the simplest method; however, all time-point concentrations in PC must be used to calculate all parameters for all subjects. If datasets cannot be related, then individual subject records must be related. In either case, the values of PCGRPID and PPGRPID must take into account multiple analytes and multiple reference time points, if they exist.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0284.txt` 第 9-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8| PC-PP Conclusions
  9| Relating the datasets (as described in Section 8, Representing Relationships and Data) is the simplest method;
 10| however, all time-point concentrations in PC must be used to calculate all parameters for all subjects. If datasets
 11| cannot be related, then individual subject records must be related. In either case, the values of PCGRPID and
 12| PPGRPID must take into account multiple analytes and multiple reference time points, if they exist.
 13| Method A is clearly the most efficient in terms of having the least number of RELREC records, but it does require
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### T69. `ig34_p0284_a008` — r3:R3_IG34_EQUIV

- PDF 页 284 · 原子类型 SENTENCE · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Method A is clearly the most efficient in terms of having the least number of RELREC records, but it does require the assignment of --GRPID values (which are optional) in both the PC and PP datasets. Method D, in contrast, does not require the assignment of --GRPID values, relying instead on the required --SEQ values in both datasets to relate the records. Although Method D results in the largest number of RELREC records compared to the other methods, it may be the easiest to implement consistently across the range of complexities shown in the examples. Two additional methods, methods B and C, are also shown for Examples 1-3. They represent hybrid approaches, using --GRPID values in only 1 dataset (PP and PC, respectively) and --SEQ values for the other. These methods are best suited for sponsors who want to minimize the number of RELREC records while not having to assign --GRPID values in both domains. Methods B and C would not be ideal, however, if one expected complex scenarios as shown in Example 4.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0284.txt` 第 13-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12| PPGRPID must take into account multiple analytes and multiple reference time points, if they exist.
 13| Method A is clearly the most efficient in terms of having the least number of RELREC records, but it does require
 14| the assignment of --GRPID values (which are optional) in both the PC and PP datasets. Method D, in contrast, does
 15| not require the assignment of --GRPID values, relying instead on the required --SEQ values in both datasets to relate
 16| the records. Although Method D results in the largest number of RELREC records compared to the other methods, it
 17| may be the easiest to implement consistently across the range of complexities shown in the examples. Two
 18| additional methods, methods B and C, are also shown for Examples 1-3. They represent hybrid approaches, using --
 19| GRPID values in only 1 dataset (PP and PC, respectively) and --SEQ values for the other. These methods are best
 20| suited for sponsors who want to minimize the number of RELREC records while not having to assign --GRPID
 21| values in both domains. Methods B and C would not be ideal, however, if one expected complex scenarios as shown
 22| in Example 4.
 23| Note that an attempt has been made to approximate real pharmacokinetic data; however, the example values are not
~~~~

KB 现文: `(无)` (来源: none):

~~~~
(无 KB 文本; IE 类或未定位)
~~~~

### T70. `ig34_p0297_a029` — r3:R3_IG34_EQUIV

- PDF 页 297 · 原子类型 SENTENCE · 所在节 `§6.3.7.4 Nervous System Findings (NV)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example shows how to represent components of a pattern-reversal visual evoked-potential (VEP) test elicited by checkerboard stimuli for a subject with optic neuritis.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0297.txt` 第 35-35 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34| Example 2
 35| This example shows how to represent components of a pattern-reversal visual evoked-potential (VEP) test elicited by checkerboard stimuli for a subject with optic neuritis. VEPs are detected via an EEG using leads
 36| that are placed on the back of the subject’s head. It is important to note that the nature of VEP testing is such that NVMETHOD should be equal to "EEG", and that NVCAT should be equal to "VISUAL EVOKED
~~~~

KB 现文: `knowledge_base/domains/NV/examples.md:61` (来源: live valid_hits):

~~~~
  61| This example shows how to represent components of a pattern-reversal visual evoked-potential (VEP) test elicited by checkerboard stimuli for a subject with optic neuritis. VEPs are detected via an EEG using leads that are placed on the back of the subject’s head. It is important to note that the nature of VEP testing is such that NVMETHOD should be equal to "EEG", and that NVCAT should be equal to "VISUAL EVOKED POTENTIAL". Several latencies from each eye—including N75, P100, and N145, as well as the P100 peak-to-peak amplitude (75-100)—are collected and should be represented in NVTESTCD/NVTEST. Details about the VEP equipment including the checkerboard size should be represented in the appropriate device domains. To interpret, each VEP component is compared against normative values established by the laboratory using healthy controls.
~~~~

### T71. `ig34_p0298_a021` — r3:R3_IG34_EQUIV

- PDF 页 298 · 原子类型 SENTENCE · 所在节 `§6.3.7.4 Nervous System Findings (NV)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Identifying information would be represented using the DI domain, and any properties of the device that may change between assessments would be represented in the DO and DU domains.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0298.txt` 第 32-33 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31| 
 32| Information about the VEP device is not shown. Identifying information would be represented using the DI domain, and any properties of the device that may change between assessments would be represented in the
 33| DO and DU domains. See the SDTMIG-MD for examples of these domains.
 34| 6.3.7.5 Ophthalmic Examinations (OE)
~~~~

KB 现文: `knowledge_base/domains/NV/examples.md:87` (来源: live valid_hits):

~~~~
  87| Information about the VEP device is not shown. Identifying information would be represented using the DI domain, and any properties of the device that may change between assessments would be represented in the DO and DU domains. See the SDTMIG-MD for examples of these domains.
~~~~

### T72. `ig34_p0332_a004` — r3:R3_IG34_EQUIV

- PDF 页 332 · 原子类型 SENTENCE · 所在节 `§6.3.9.3 Disease Response and Clin Classification (RS)`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Assumptions and examples are different for the disease response and clinical classifications use cases.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0332.txt` 第 14-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13| 
 14| Assumptions and examples are different for the disease response and clinical classifications use cases.
 15| 
~~~~

KB 现文: `knowledge_base/domains/RS/assumptions.md:18` (来源: live valid_hits):

~~~~
  18| Assumptions and examples are different for the disease response and clinical classifications use cases.
~~~~

### T73. `ig34_p0400_a003` — r3:R3_IG34_EQUIV

- PDF 页 400 · 原子类型 SENTENCE · 所在节 `§7.2.1 Trial Arms (TA) – Example 7`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This diagram also shows more detail within the Induction Chemo + RT and Additional Chemo blocks than the preceding diagram.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0400.txt` 第 11-12 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10| chemotherapy and radiation with and without surgery, so this study is better modeled as a 2-arm trial, but with major
 11| "skip forward" arrows for some subjects, as illustrated in the following diagram. This diagram also shows more
 12| detail within the Induction Chemo + RT and Additional Chemo blocks than the preceding diagram. Both the
 13| induction and additional chemotherapy are given in 2 cycles. The second induction cycle is different for the 2 arms,
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:889` (来源: live valid_hits):

~~~~
 889| However, the objectives of the trial make it clear that this trial is designed to compare 2 treatment strategies, chemotherapy and radiation with and without surgery, so this study is better modeled as a 2-arm trial, but with major "skip forward" arrows for some subjects, as illustrated in the following diagram. This diagram also shows more detail within the Induction Chemo + RT and Additional Chemo blocks than the preceding diagram. Both the induction and additional chemotherapy are given in 2 cycles. The second induction cycle is different for the 2 arms, since radiation therapy for those assigned to the non-surgery arm includes a “boost” which those assigned to the surgery arm do not receive.
~~~~

### T74. `ig34_p0400_a010` — r3:R3_IG34_EQUIV

- PDF 页 400 · 原子类型 SENTENCE · 所在节 `§7.2.1 Trial Arms (TA) – Example 7`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The next diagram shows the retrospective view of this trial.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0400.txt` 第 29-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 28| 
 29| The next diagram shows the retrospective view of this trial. The fact that the elements in the study cell for the CR
 30| arm in the continuation treatment epoch do not fill the space in the diagram is an artifact of the diagram conventions.
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:572,721,803` (来源: live valid_hits):

~~~~
 572| The next diagram shows the retrospective view of this trial.
 721| The assumption of a one-to-one relationship between elements and epochs makes such situations difficult to handle. However, without that assumption, this trial is essentially the same as Trial 4. The next diagram shows the retrospective view of this trial.
 803| The design of this trial is very similar to that for Example Trials 4 and 5. The main difference is that there are 2 different rest elements: the short one used with drug A and the long one used with drug B. The next diagram shows the retrospective view of this trial.
~~~~

### T75. `ig34_p0400_a012` — r3:R3_IG34_EQUIV

- PDF 页 400 · 原子类型 SENTENCE · 所在节 `§7.2.1 Trial Arms (TA) – Example 7`
- triage 类 **-** · 终态 **EQUIVALENT** (T3 前 EQUIVALENT) · 判定规则 `(本项目未改, stock)` · 批 `-`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Those subjects who do receive surgery will in fact spend a longer time completing treatment and moving into follow-up.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0400.txt` 第 31-32 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 30| arm in the continuation treatment epoch do not fill the space in the diagram is an artifact of the diagram conventions.
 31| Those subjects who do receive surgery will in fact spend a longer time completing treatment and moving into
 32| follow-up. Although it is tempting to think of the horizontal axis of these diagrams as a timeline, this can sometimes
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:931` (来源: live valid_hits):

~~~~
 931| The next diagram shows the retrospective view of this trial. The fact that the elements in the study cell for the CR arm in the continuation treatment epoch do not fill the space in the diagram is an artifact of the diagram conventions. Those subjects who do receive surgery will in fact spend a longer time completing treatment and moving into follow-up. Although it is tempting to think of the horizontal axis of these diagrams as a timeline, this can sometimes be misleading. The diagrams are not necessarily to scale in the sense that the length of the block representing an element represents its duration, and elements that line up on the same vertical line in the diagram may not occur at the same relative time within the study.
~~~~

