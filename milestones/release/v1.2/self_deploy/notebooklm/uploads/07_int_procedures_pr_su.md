# 07_int_procedures_pr_su

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `07`
> - **Concept**: Interventions: PR + SU
> - **Merged files**: 6
> - **Words**: 6,168
> - **Chars**: 40,319
> - **Sources**:
>   - `domains/PR/spec.md`
>   - `domains/PR/assumptions.md`
>   - `domains/PR/examples.md`
>   - `domains/SU/spec.md`
>   - `domains/SU/assumptions.md`
>   - `domains/SU/examples.md`

---
## Source: `domains/PR/spec.md`

# PR — Procedures

> Class: Interventions | Structure: One record per recorded procedure per occurrence per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### PRSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### PRGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain.

### PRSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. Example: preprinted line identifier on a CRF, record identifier defined in the sponsor's operational database.

### PRLNKID
- **Order:** 7
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to facilitate identification of relationships between records.

### PRLNKGRP
- **Order:** 8
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to facilitate identification of relationships between records.

### PRTRT
- **Order:** 9
- **Label:** Reported Name of Procedure
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Name of procedure performed, either preprinted or collected on a CRF.

### PRDECOD
- **Order:** 10
- **Label:** Standardized Procedure Name
- **Type:** Char
- **Controlled Terms:** C101858
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized or dictionary-derived name of PRTRT. If the codelist "PROCEDUR" is not used, the sponsor is expected to provide the dictionary name and version used to map the terms in the external codelist element in the Define-XML document. If an intervention term does not have a decode value, then PRDECOD will be null.

### PRCAT
- **Order:** 11
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of procedure values.

### PRSCAT
- **Order:** 12
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of PRCAT values.

### PRPRESP
- **Order:** 13
- **Label:** Pre-specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when a specific procedure is pre-specified on a CRF. Values should be "Y" or null.

### PROCCUR
- **Order:** 14
- **Label:** Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to record whether a prespecified procedure occurred when information about the occurrence of a specific procedure is solicited.

### PRINDC
- **Order:** 15
- **Label:** Indication
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Denotes the indication for the procedure (e.g., why the procedure was performed).

### PRDOSE
- **Order:** 16
- **Label:** Dose
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of PRTRT administered. Not populated when PRDOSTXT is populated.

### PRDOSTXT
- **Order:** 17
- **Label:** Dose Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Dosing information collected in text form. Examples: "<1", "200-400". Not populated when PRDOSE is populated.

### PRDOSU
- **Order:** 18
- **Label:** Dose Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Units for PRDOSE, PRDOSTOT, or PRDOSTXT.

### PRDOSFRM
- **Order:** 19
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Dose form for PRTRT.

### PRDOSFRQ
- **Order:** 20
- **Label:** Dosing Frequency per Interval
- **Type:** Char
- **Controlled Terms:** C71113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Usually expressed as the number of doses given per a specific interval.

### PRDOSRGM
- **Order:** 21
- **Label:** Intended Dose Regimen
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the intended schedule or regimen for the procedure.

### PRROUTE
- **Order:** 22
- **Label:** Route of Administration
- **Type:** Char
- **Controlled Terms:** C66729
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Route of administration for PRTRT.

### PRLOC
- **Order:** 23
- **Label:** Location of Procedure
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of a procedure.

### PRLAT
- **Order:** 24
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality.

### PRDIR
- **Order:** 25
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality.

### PRPORTOT
- **Order:** 26
- **Label:** Portion or Totality
- **Type:** Char
- **Controlled Terms:** C99075
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, apportioning of.

### VISITNUM
- **Order:** 27
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 28
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 29
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 30
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 31
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the procedure.

### PRSTDTC
- **Order:** 32
- **Label:** Start Date/Time of Procedure
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of the procedure represented in ISO 8601 character format.

### PRENDTC
- **Order:** 33
- **Label:** End Date/Time of Procedure
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the procedure represented in ISO 8601 character format.

### PRSTDY
- **Order:** 34
- **Label:** Study Day of Start of Procedure
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of procedure expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### PRENDY
- **Order:** 35
- **Label:** Study Day of End of Procedure
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of procedure expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### PRDUR
- **Order:** 36
- **Label:** Duration of Procedure
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of a procedure represented in ISO 8601 character format. Used only if collected on the CRF and not derived from start and end date/times.

### PRTPT
- **Order:** 37
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a procedure should be performed. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PRTPTNUM and PRTPTREF.

### PRTPTNUM
- **Order:** 38
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of planned time point used in sorting.

### PRELTM
- **Order:** 39
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time in ISO 8601 format relative to a planned fixed reference (PRTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### PRTPTREF
- **Order:** 40
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by PRELTM, PRTPTNUM, and PRTPT.

### PRRFTDTC
- **Order:** 41
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by PRTRTREF in ISO 8601 character format.

### PRSTRTPT
- **Order:** 42
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable PRSTTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### PRSTTPT
- **Order:** 43
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by PRSTRTPT. Examples: "2003-12-15", "VISIT 1".

### PRENRTPT
- **Order:** 44
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable PRENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### PRENTPT
- **Order:** 45
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by PRENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Procedure (C101858)](../../terminology/core/interventions.md) — PRDECOD
- [Pharmaceutical Dosage Form (C66726)](../../terminology/core/interventions.md) — PRDOSFRM
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — PRSTRTPT, PRENRTPT
- [Route of Administration Response (C66729)](../../terminology/core/interventions.md) — PRROUTE
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — PRPRESP, PROCCUR
- [Frequency (C71113)](../../terminology/core/interventions.md) — PRDOSFRQ
- [Unit (C71620)](../../terminology/core/general_part5.md) — PRDOSU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — PRLOC
- [Laterality (C99073)](../../terminology/core/general_part2.md) — PRLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — PRDIR
- [Portion/Totality (C99075)](../../terminology/core/general_part4.md) — PRPORTOT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Interventions):** AG, CM, EC, EX, ML, SU

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Interventions class definition](../../model/02_observation_classes.md)

## Source: `domains/PR/assumptions.md`

# PR — Assumptions

1. Some examples of procedures, by type, include the following:
   a. Disease screening (e.g., mammogram, pap smear)
   b. Endoscopic examinations (e.g., arthroscopy, diagnostic colonoscopy, therapeutic colonoscopy, diagnostic laparoscopy, therapeutic laparoscopy)
   c. Diagnostic tests (e.g., amniocentesis, biopsy, catheterization, cutaneous oximetry, finger stick, fluorophotometry, imaging techniques (e.g., DXA scan, CT scan, MRI), phlebotomy, pulmonary function test, skin test, stress test, tympanometry)
   d. Therapeutic procedures (e.g., ablation therapy, catheterization, cryotherapy, mechanical ventilation, phototherapy, radiation therapy/radiotherapy, thermotherapy)
   e. Surgical procedures (e.g., curative surgery, diagnostic surgery, palliative surgery, therapeutic surgery, prophylactic surgery, resection, stenting, hysterectomy, tubal ligation, implantation)

   The Procedures domain is based on the Interventions observation class. The extent of physiological effect may range from observable to microscopic. Regardless of the extent of effect or whether it is collected in the study, all collected procedures are represented in this domain. The protocol design should specify whether procedure information will be collected. Measurements obtained from procedures are to be represented in their respective Findings domain(s). For example, a biopsy may be performed to obtain a tissue sample that is then evaluated histopathologically. In this case, details of the biopsy procedure can be represented in the PR domain and the histopathology findings in the Microscopic Findings (MI) domain. Describing the relationship between PR and MI records (in RELREC) in this example is dependent on whether the relationship is collected, either explicitly or implicitly.

2. In the Findings Observation Class, the test method is represented in the --METHOD variable (e.g., electrophoresis, gram stain, polymerase chain reaction). At times, the test method overlaps with diagnostic/therapeutic procedures (e.g., ultrasound, MRI, x-ray) in-scope for the PR domain. The following is recommended: If timing (start, end or duration) or an indicator populating PROCCUR, PRSTAT, or PRREASND is collected, then a PR record should be created. If only the findings from a procedure are collected, then --METHOD in the Findings domain(s) may be sufficient to reflect the procedure and a related PR record is optional. It is at the sponsor's discretion whether to represent the procedure as both a test method (--METHOD) and related PR record.

3. PRINDC is used to represent a medical indication, a medical condition which makes a treatment advisable. The reason for a procedure may be something other than a medical indication. For example, an x-ray might be taken to determine whether a fracture was present. Reasons other than medical indications should be represented using the supplemental qualifier PRREAS (see Appendix C1, Supplemental Qualifiers Name Codes).

4. Any identifier variables, timing variables, or interventions general observation-class qualifiers may be added to the PR domain, but the following qualifiers would generally not be used: --MOOD, --LOT.

## Source: `domains/PR/examples.md`

# PR — Examples

## Example 1

A procedures log CRF may collect verbatim values (procedure names) and dates performed. This example shows a subject who had 5 procedures collected and represented in the PR domain. In this study, the sponsor chose to consider verbatim text in PRTRT as long text represented in mixed case. See Section 4.2.4, Text Case in Submitted Data.

**pr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRTRT | PRSTDTC | PRENDTC |
|-----|---------|--------|---------|-------|-------|---------|---------|
| 1 | XYZ | PR | XYZ789-002 | 1 | Wisdom Teeth Extraction | 2010-06-08 | 2010-06-08 |
| 2 | XYZ | PR | XYZ789-002 | 2 | Reset Broken Arm | 2010-08-06 | 2010-08-06 |
| 3 | XYZ | PR | XYZ789-002 | 3 | Prostate Examination | 2010-12-12 | 2010-12-12 |
| 4 | XYZ | PR | XYZ789-002 | 4 | Endoscopy | 2010-12-12 | 2010-12-12 |
| 5 | XYZ | PR | XYZ789-002 | 5 | Heart Transplant | 2011-08-29 | 2011-08-29 |

## Example 2

This example shows data from a 24-hour Holter monitor, an ambulatory electrocardiography device that records a continuous electrocardiographic rhythm pattern.

The start and end of the Holter monitoring procedure are represented in the PR domain.

**pr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRLNKID | PRTRT | PRDECOD | PRPRESP | PROCCUR | PRSTDTC | PRENDTC |
|-----|---------|--------|---------|-------|---------|-------|---------|---------|---------|---------|---------|
| 1 | ABC123 | PR | ABC123-001 | 1 | 20110101_20110102 | 24-HOUR HOLTER MONITOR | HOLTER CONTINUOUS ECG RECORDING | Y | Y | 2011-01-01T08:00 | 2011-01-02T09:45 |

The heart rate findings from the procedure are represented in the ECG Test Results (EG) domain.

**eg.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EGSEQ | EGLNKID | EGTESTCD | EGTEST | EGORRES | EGORRESU | EGMETHOD | EGDTC | EGENDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|---------|----------|----------|-------|---------|
| 1 | ABC123 | EG | ABC123-001 | 1 | 20110101_20110102 | EGHRMIN | ECG Minimum Heart Rate | 70 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |
| 2 | ABC123 | EG | ABC123-001 | 2 | 20110101_20110102 | EGHRMAX | ECG Maximum Heart Rate | 100 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |
| 3 | ABC123 | EG | ABC123-001 | 3 | 20110101_20110102 | EGHRMEAN | ECG Mean Heart Rate | 75 | beats/min | HOLTER CONTINUOUS ECG RECORDING | 2011-01-01T08:00 | 2011-01-02T09:45 |

The relrec.xpt reflects a one-to-many dataset-level relationship between PR and EG using --LNKID.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC123 | PR | | PRLNKID | | ONE | 1 |
| 2 | ABC123 | EG | | EGLNKID | | MANY | 1 |

## Example 3

This example shows data for 3 subjects who had on-study radiotherapy. Dose, dose unit, location, and timing are represented. In this study, the sponsor chose to consider verbatim text in PRTRT as long text represented in mixed case. See Section 4.2.4, Text Case in Submitted Data.

**pr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRTRT | PRDOSE | PRDOSU | PRLOC | PRLAT | PRSTDTC | PRENDTC |
|-----|---------|--------|---------|-------|-------|--------|--------|-------|-------|---------|---------|
| 1 | ABC123 | PR | ABC123-1001 | 1 | External beam radiation therapy | 70 | Gy | BREAST | RIGHT | 2011-06-01 | 2011-06-25 |
| 2 | ABC123 | PR | ABC123-2002 | 1 | Brachytherapy | 25 | Gy | PROSTATE | | 2011-07-15 | 2011-07-15 |
| 3 | ABC123 | PR | ABC123-3003 | 1 | Radiotherapy | 300 | cGy | BONE | | 2011-08-19 | 2011-08-22 |

## Source: `domains/SU/spec.md`

# SU — Substance Use

> Class: Interventions | Structure: One record per substance type per reported occurrence per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### SUSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### SUGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### SUSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Tobacco & Alcohol Use CRF page.

### SUTRT
- **Order:** 7
- **Label:** Reported Name of Substance
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Substance name. Examples: "CIGARETTES", "COFFEE".

### SUMODIFY
- **Order:** 8
- **Label:** Modified Substance Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If SUTRT is modified, then the modified text is placed here.

### SUDECOD
- **Order:** 9
- **Label:** Standardized Substance Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized or dictionary-derived text description of SUTRT or SUMODIFY if the sponsor chooses to code the substance use. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

### SUCAT
- **Order:** 10
- **Label:** Category for Substance Use
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records. Examples: "TOBACCO", "ALCOHOL", or "CAFFEINE".

### SUSCAT
- **Order:** 11
- **Label:** Subcategory for Substance Use
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of substance use. Examples: "CIGARS", "CIGARETTES", "BEER", "WINE".

### SUPRESP
- **Order:** 12
- **Label:** SU Pre-Specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether ("Y"/null) information about the use of a specific substance was solicited on the CRF.

### SUOCCUR
- **Order:** 13
- **Label:** SU Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** When the use of specific substances is solicited, SUOCCUR is used to indicate whether ("Y"/"N") a particular prespecified substance was used. Values are null for substances not specifically solicited.

### SUSTAT
- **Order:** 14
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** When the use of prespecified substances is solicited, the completion status indicates that there was no response to the question about the prespecified substance. When there is no prespecified list on the CRF, then the completion status indicates that substance use was not assessed for the subject.

### SUREASND
- **Order:** 15
- **Label:** Reason Substance Use Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason substance use was not collected. Used in conjunction with SUSTAT when value of SUSTAT is "NOT DONE".

### SUCLAS
- **Order:** 16
- **Label:** Substance Use Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Substance use class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit SUCLAS.

### SUCLASCD
- **Order:** 17
- **Label:** Substance Use Class Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Code corresponding to SUCLAS. May be obtained from coding.

### SUDOSE
- **Order:** 18
- **Label:** Substance Use Consumption
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of SUTRT consumed. Not populated if SUDOSTXT is populated.

### SUDOSTXT
- **Order:** 19
- **Label:** Substance Use Consumption Text
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Substance use consumption amounts or a range of consumption information collected in text form. Not populated if SUDOSE is populated.

### SUDOSU
- **Order:** 20
- **Label:** Consumption Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Units for SUDOSE, SUDOSTOT, or SUDOSTXT. Examples: "oz", "CIGARETTE", "PACK", "g".

### SUDOSFRM
- **Order:** 21
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Dose form for SUTRT. Examples: "INJECTABLE", "LIQUID", "POWDER".

### SUDOSFRQ
- **Order:** 22
- **Label:** Use Frequency Per Interval
- **Type:** Char
- **Controlled Terms:** C71113
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Usually expressed as the number of repeated administrations of SUDOSE within a specific time period. Example: "Q24H" (every day).

### SUDOSTOT
- **Order:** 23
- **Label:** Total Daily Consumption
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Total daily use of SUTRT using the units in SUDOSU. Used when dosing is collected as total daily dose. If a sponsor needs to aggregate the data over a period other than daily, then the aggregated total could be recorded in a supplemental qualifier variable.

### SUROUTE
- **Order:** 24
- **Label:** Route of Administration
- **Type:** Char
- **Controlled Terms:** C66729
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Route of administration for SUTRT. Examples: "ORAL", "INTRAVENOUS".

### TAETORD
- **Order:** 25
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the substance use started. Null for substances that started before study participation.

### EPOCH
- **Order:** 26
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the substance use. Null for substances that started before study participation.

### SUSTDTC
- **Order:** 27
- **Label:** Start Date/Time of Substance Use
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of the substance use represented in ISO 8601 character format.

### SUENDTC
- **Order:** 28
- **Label:** End Date/Time of Substance Use
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the substance use represented in ISO 8601 character format.

### SUSTDY
- **Order:** 29
- **Label:** Study Day of Start of Substance Use
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of substance use relative to the sponsor-defined RFSTDTC.

### SUENDY
- **Order:** 30
- **Label:** Study Day of End of Substance Use
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of substance use relative to the sponsor-defined RFSTDTC.

### SUDUR
- **Order:** 31
- **Label:** Duration of Substance Use
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of substance use in ISO 8601 format. Used only if collected on the CRF and not derived from start and end date/times.

### SUSTRF
- **Order:** 32
- **Label:** Start Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the start of the substance use relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR" was collected, this information may be translated into SUSTRF.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### SUENRF
- **Order:** 33
- **Label:** End Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the end of the substance use with relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into SUENRF.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### SUSTRTPT
- **Order:** 34
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the substance as being before or after the reference time point defined by variable SUSTTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7 , Use of Relative Timing Variables.

### SUSTTPT
- **Order:** 35
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by SUSTRTPT. Examples: "2003-12-15", "VISIT 1".

### SUENRTPT
- **Order:** 36
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the substance as being before or after the reference time point defined by variable SUENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7 , Use of Relative Timing Variables.

### SUENTPT
- **Order:** 37
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by SUENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Pharmaceutical Dosage Form (C66726)](../../terminology/core/interventions.md) — SUDOSFRM
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — SUSTRF, SUENRF, SUSTRTPT, SUENRTPT
- [Route of Administration Response (C66729)](../../terminology/core/interventions.md) — SUROUTE
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — SUPRESP, SUOCCUR
- [Not Done (C66789)](../../terminology/core/general_part4.md) — SUSTAT
- [Frequency (C71113)](../../terminology/core/interventions.md) — SUDOSFRQ
- [Unit (C71620)](../../terminology/core/general_part5.md) — SUDOSU
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Interventions):** AG, CM, EC, EX, ML, PR

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Interventions class definition](../../model/02_observation_classes.md)

## Source: `domains/SU/assumptions.md`

# SU — Assumptions

1. Substance use information may be independent of planned study evaluations, or may be a key outcome (e.g., planned evaluation) of a clinical trial.
   a. In many clinical trials, detailed substance use information as provided for in the domain model above may not be required (e.g., the only information collected may be a response to the question "Have you ever smoked tobacco?"); in such cases, many of the qualifier variables would not be submitted.
   b. SU may contain responses to questions about use of prespecified substances as well as records of substance use collected as free text.

2. SU description and coding
   a. SUTRT captures the verbatim or the prespecified text collected for the substance. It is the topic variable for the SU dataset. SUTRT is a required variable and must have a value.
   b. SUMODIFY is a permissible variable and should be included if coding is performed and the sponsor's procedure permits modification of a verbatim substance use term for coding. The modified term is listed in SUMODIFY. The variable may be populated as per the sponsor's procedures.
   c. SUDECOD is the preferred term derived by the sponsor from the coding dictionary if coding is performed. It is a permissible variable. Where deemed necessary by the sponsor, the verbatim term (SUTRT) should be coded using a standard dictionary such as WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

3. Additional categorization and grouping
   a. SUCAT and SUSCAT should not be redundant with the domain code or dictionary classification provided by SUDECOD, or with SUTRT. That is, they should provide a different means of defining or classifying SU records. For example, a sponsor may be interested in identifying all substances that the investigator feels might represent opium use, and to collect such use on a separate CRF page. This categorization might differ from the categorization derived from the coding dictionary.
   b. SUGRPID may be used to link (or associate) different records together to form a block of related records within SU at the subject level (see Section 4.2.6, Grouping Variables and Categorization). It should not be used in place of SUCAT or SUSCAT.

4. Timing variables
   a. SUSTDTC and SUENDTC may be populated as required.
   b. If substance use information is collected more than once within the CRF (indicating that the data are visit-based) then VISITNUM would be added to the domain as an additional timing variable. VISITDY and VISIT would then be permissible variables.

5. Any additional qualifiers from the Interventions class may be added to the SU domain, but the following qualifiers would generally not be used: --MOOD, --LOT.

## Source: `domains/SU/examples.md`

# SU — Examples

## Example 1

This example illustrates how typical SU data could be populated. Here, the CRF collected:

- Smoking data
   - Smoking status of "previous", "current", or "never"
   - If a current or past smoker, number of packs per day
   - If a former smoker, the year the subject quit
- Current caffeine use
   - What caffeine drinks subjects consumed today
   - How many cups today

SUCAT allows the records to be grouped into smoking-related data and caffeine-related data. In this example, the treatments are prespecified on the CRF page, so SUTRT does not require a standardized SUDECOD equivalent.

**Not shown:** A subject who never smoked does not have a tobacco record. Alternatively, a row for the subject could have been included with SUOCCUR = "N" and null dosing and timing fields; the interpretation would be the same. A subject who did not drink any caffeinated drinks on the day of the assessment does not have any caffeine records. A subject who never smoked and did not drink caffeinated drinks on the day of the assessment does not appear in the dataset.

**Row 1:** Subject 1234005 is a 2-pack/day current smoker. "Current" implies that smoking started sometime before the time the question was asked (SUSTTPT = "2006-01-01", SUSTRTPT = "BEFORE") and had not ended as of that date (SUENTPT = "2006-01-01", SUENRTPT = "ONGOING"). See Section 4.4.7, Use of Relative Timing Variables for the use of these variables. Both the beginning and ending reference time points for this question are the date of the assessment.

**Row 2:** Subject 1234005 drank 3 cups of coffee on the day of the assessment.

**Row 3:** Subject 1234006 is a former smoker. The date this subject began smoking is unknown, but it was sometime before the assessment date; this is shown by the values of SUSTTPT and SUSTRTPT. The end date of smoking was collected, so SUENTPT and SUENRTPT are not populated. Instead, the end date is in SUENDTC.

**Row 4:** Subject 1234006 drank tea on the day of the assessment.

**Row 5:** Subject 1234006 drank coffee on the day of the assessment.

**Row 6:** Subject 1234007 had missing data for the smoking questions; this is indicated by SUSTAT = "NOT DONE". The reason is in SUREASND.

**Row 7:** Subject 1234007 also had missing data for all of the caffeine questions.

**su.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SUSEQ | SUTRT | SUCAT | SUSTAT | SUREASND | SUDOSE | SUDOSU | SUDOSFRQ | SUSTDTC | SUENDTC | SUSTTPT | SUSTRTPT | SUENTPT | SUENRTPT |
|-----|---------|--------|---------|-------|-------|-------|--------|----------|--------|--------|----------|---------|---------|---------|----------|---------|----------|
| 1 | 1234 | SU | 1234005 | 1 | CIGARETTES | TOBACCO | | | 2 | PACK | QD | | | 2006-01-01 | BEFORE | 2006-01-01 | ONGOING |
| 2 | 1234 | SU | 1234005 | 2 | COFFEE | CAFFEINE | | | 3 | CUP | QD | 2006-01-01 | 2006-01-01 | | | | |
| 3 | 1234 | SU | 1234006 | 1 | CIGARETTES | TOBACCO | | | 1 | PACK | QD | | 2003 | 2006-03-15 | BEFORE | | |
| 4 | 1234 | SU | 1234006 | 2 | TEA | CAFFEINE | | | 1 | CUP | QD | 2006-03-15 | 2006-03-15 | | | | |
| 5 | 1234 | SU | 1234006 | 3 | COFFEE | CAFFEINE | | | 2 | CUP | QD | 2006-03-15 | 2006-03-15 | | | | |
| 6 | 1234 | SU | 1234007 | 1 | CIGARETTES | TOBACCO | NOT DONE | Subject left office before CRF was completed | | | | | | | | | |
| 7 | 1234 | SU | 1234007 | 2 | CAFFEINE | CAFFEINE | NOT DONE | Subject left office before CRF was completed | | | | | | | | | |
