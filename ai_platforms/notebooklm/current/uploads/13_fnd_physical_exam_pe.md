# 13_fnd_physical_exam_pe

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `13`
> - **Concept**: Findings: PE (physical exam)
> - **Merged files**: 3
> - **Words**: 2,147
> - **Chars**: 13,840
> - **Sources**:
>   - `domains/PE/spec.md`
>   - `domains/PE/assumptions.md`
>   - `domains/PE/examples.md`

---
## Source: `domains/PE/spec.md`

# PE — Physical Examination

> Class: Findings | Structure: One record per body system or abnormality per visit per subject

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

### PESEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number.

### PEGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records in a single domain for a subject.

### PESPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. Perhaps preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF.

### PETESTCD
- **Order:** 7
- **Label:** Body System Examined Short Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of a part of the body examined in a physical examination. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HEAD", "ENT". If the results of the entire physical examination are represented in one record, value should be "PHYSEXAM".

### PETEST
- **Order:** 8
- **Label:** Body System Examined
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name of a part of the body examined in a physical examination. The value in PETEST cannot be longer than 40 characters. Examples: "Head", "Ear/Nose/Throat". If the results of the entire physical examination are represented in one record, value should be "Physical Examination".

### PEMODIFY
- **Order:** 9
- **Label:** Modified Reported Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If the value of PEORRES is modified for coding purposes, then the modified text is placed here.

### PECAT
- **Order:** 10
- **Label:** Category for Examination
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Example: "GENERAL".

### PESCAT
- **Order:** 11
- **Label:** Subcategory for Examination
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of --CAT values.

### PEBODSYS
- **Order:** 12
- **Label:** Body System or Organ Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Body system or organ class (e.g., MedDRA SOC) that is involved for a finding from the standard hierarchy for dictionary-coded results.

### PEORRES
- **Order:** 13
- **Label:** Verbatim Examination Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Text description of any abnormal findings. If the examination was completed and there were no abnormal findings, the value should be "NORMAL". If the examination was not performed on a particular body system, or at the subject level, then the value should be null, and "NOT DONE" should appear in PESTAT.

### PEORRESU
- **Order:** 14
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for PEORRES.

### PESTRESC
- **Order:** 15
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** If there are findings for a body system, then either the dictionary preferred term (if findings are coded using a dictionary) or PEORRES (if findings are not encoded) should appear here. If PEORRES is null, PESTRESC must be null.

### PESTAT
- **Order:** 16
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate exam not done. Must be null if a result exists in PEORRES/PESTRESC.

### PEREASND
- **Order:** 17
- **Label:** Reason Not Examined
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why an examination was not performed or why a body system was not examined. Example: "SUBJECT REFUSED". Used in conjunction with PESTAT when value is "NOT DONE".

### PELOC
- **Order:** 18
- **Label:** Location of Physical Exam Finding
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Example: "ARM" for skin rash.

### PELAT
- **Order:** 19
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterallity. Examples: "RIGHT", "LEFT", "BILATERAL".

### PEMETHOD
- **Order:** 20
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "PALPATION", "PERCUSSION".

### PELOBXFL
- **Order:** 21
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.

### PEBLFL
- **Order:** 22
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** A baseline defined by the sponsor (could be derived in the same manner as PELOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that PEBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### PEEVAL
- **Order:** 23
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR".

### VISITNUM
- **Order:** 24
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 25
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 26
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 27
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 28
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the observation date/time of the physical exam finding.

### PEDTC
- **Order:** 29
- **Label:** Date/Time of Examination
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of the physical examination represented in ISO 8601 character format.

### PEDY
- **Order:** 30
- **Label:** Study Day of Examination
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
---

## Cross References

### Controlled Terminology
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — PELOBXFL, PEBLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — PESTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — PEORRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — PELOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — PEEVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — PEMETHOD
- [Laterality (C99073)](../../terminology/core/general_part2.md) — PELAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

## Source: `domains/PE/assumptions.md`

# PE — Assumptions

1. PE findings reflect the presence or absence of physical signs of disease or abnormality observed during a general physical examination. Multiple body systems are assessed during a physical examination, often starting at the head and ending at the toes, where the body is evaluated by inspection, palpation (feeling with the hands), percussion (tapping with fingers), and auscultation (listening). The examination often includes macro assessments (e.g., normal/abnormal) of appearance, general health, behavior, and body system review from head to toe.
   a. Evaluation of targeted body systems (e.g., cardiovascular, ophthalmic, reproductive) as part of therapeutic specific assessments should be represented in the appropriate body system domain (e.g., CV, OE, RP, respectively).
   b. See CDASHIG Section 8.3.11, PE - Physical Examination (available at https://www.cdisc.org/standards/foundational/cdash/), for additional collection guidance.

2. Abnormalities observed during a physical examination may be encoded. When collected/reported as a PE finding, the verbatim value is represented in PEORRES and the encoded value in PESTRESC. When collected/reported as medical history or an adverse event, the verbatim value is represented in MHTERM or AETERM and the encoded value is represented in MHDECOD or AEDECOD, respectively.

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PE domain, but the following qualifiers would generally not be used: --XFN, --NAM, --LOINC, --FAST, --TOX, --TOXGR.

## Source: `domains/PE/examples.md`

# PE — Examples

## Example 1

This example shows data for 1 subject collected at 1 visit. The data come from a general physical examination.

**Rows 1-2, 6:** Show how PESTRESC is populated if result is "NORMAL".
**Rows 3-5:** Show how PESPID is used to show the sponsor-defined identifier, which in this case is the CRF sequence number used for identifying abnormalities within a body system. Additionally, the abnormalities were encoded; PESTRESC represents the MedDRA Preferred Term and PEBODSYS represents the MedDRA system organ class.

**pe.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PESEQ | PESPID | PETESTCD | PETEST | PELOC | PELAT | PEBODSYS | PEORRES | PESTRESC | VISITNUM | VISIT | VISITDY | PEDTC | PEDY |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|-------|----------|---------|----------|----------|-------|---------|-------|------|
| 1 | ABC | PE | ABC-001-001 | 1 | | HEAD | Head | | | | NORMAL | NORMAL | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 2 | ABC | PE | ABC-001-001 | 2 | | ENT | Ear/Nose/Throat | | | | NORMAL | NORMAL | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 3 | ABC | PE | ABC-001-001 | 3 | 1 | SKIN | Skin | FACE | | Skin and subcutaneous tissue disorder | ACNE | Acne | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 4 | ABC | PE | ABC-001-001 | 4 | 2 | SKIN | Skin | HANDS | | Skin and subcutaneous tissue disorder | DERMATITIS | Dermatitis | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 5 | ABC | PE | ABC-001-001 | 5 | 3 | SKIN | Skin | ARM | LEFT | Skin and subcutaneous tissue disorder | SKIN RASH | Rash | -1 | BASELINE | -1 | 1999-06-06 | -3 |
| 6 | ABC | PE | ABC-001-001 | 6 | | HEART | Heart | | | | NORMAL | NORMAL | -1 | BASELINE | -1 | 1999-06-06 | -3 |
