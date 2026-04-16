# CM — Concomitant/Prior Medications

> Class: Interventions | Structure: One record per recorded intervention occurrence or constant-dosing interval per subject

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

### CMSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of subject records within a domain. May be any valid number.

### CMGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### CMSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. Example: a number preprinted on the CRF as an explicit line identifier or record identifier defined in the sponsor's operational database. Example: line number on a concomitant medication page.

### CMTRT
- **Order:** 7
- **Label:** Reported Name of Drug, Med, or Therapy
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim medication name that is either preprinted or collected on a CRF.

### CMMODIFY
- **Order:** 8
- **Label:** Modified Reported Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If CMTRT is modified to facilitate coding, then CMMODIFY will contain the modified text.

### CMDECOD
- **Order:** 9
- **Label:** Standardized Medication Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized or dictionary-derived text description of CMTRT or CMMODIFY. Equivalent to the generic drug name in WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then CMDECOD will be left blank.

### CMCAT
- **Order:** 10
- **Label:** Category for Medication
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of medications/treatment. Examples: "PRIOR", "CONCOMITANT", "ANTI-CANCER MEDICATION", "GENERAL CONMED".

### CMSCAT
- **Order:** 11
- **Label:** Subcategory for Medication
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of medications/treatment. Examples: "CHEMOTHERAPY", "HORMONAL THERAPY", "ALTERNATIVE THERAPY".

### CMPRESP
- **Order:** 12
- **Label:** CM Pre-specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether ("Y"/null) information about the use of a specific medication was solicited on the CRF.

### CMOCCUR
- **Order:** 13
- **Label:** CM Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** When the use of a specific medication is solicited. CMOCCUR is used to indicate whether ("Y"/"N") use of the medication occurred. Values are null for medications not specifically solicited.

### CMSTAT
- **Order:** 14
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question about the occurrence of a prespecified intervention was not answered. Should be null or have a value of "NOT DONE".

### CMREASND
- **Order:** 15
- **Label:** Reason Medication Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with CMSTAT when value is "NOT DONE".

### CMINDC
- **Order:** 16
- **Label:** Indication
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Denotes why a medication was taken or administered. Examples: "NAUSEA", "HYPERTENSION".

### CMCLAS
- **Order:** 17
- **Label:** Medication Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Drug class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit CMCLAS.

### CMCLASCD
- **Order:** 18
- **Label:** Medication Class Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Class code corresponding to CMCLAS. Drug class. May be obtained from coding. When coding to a single class, populate with class code. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit CMCLASCD.

### CMDOSE
- **Order:** 19
- **Label:** Dose per Administration
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of CMTRT given. Not populated when CMDOSTXT is populated.

### CMDOSTXT
- **Order:** 20
- **Label:** Dose Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Dosing amounts or a range of dosing information collected in text form. Units may be stored in CMDOSU. Examples: "200-400", "15-20". Not populated when CMDOSE is populated.

### CMDOSU
- **Order:** 21
- **Label:** Dose Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Units for CMDOSE, CMDOSTOT, or CMDOSTXT. Examples: "ng", "mg", "mg/kg".

### CMDOSFRM
- **Order:** 22
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Dose form for CMTRT. Examples: "TABLET", "LOTION".

### CMDOSFRQ
- **Order:** 23
- **Label:** Dosing Frequency per Interval
- **Type:** Char
- **Controlled Terms:** C71113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Usually expressed as the number of repeated administrations of CMDOSE within a specific time period. Examples: "BID" (twice daily), "Q12H" (every 12 hours).

### CMDOSTOT
- **Order:** 24
- **Label:** Total Daily Dose
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Total daily dose of CMTRT using the units in CMDOSU. Used when dosing is collected as total daily dose. Total dose over a period other than day could be recorded in a separate supplemental qualifier variable.

### CMDOSRGM
- **Order:** 25
- **Label:** Intended Dose Regimen
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the (intended) schedule or regimen for the Intervention. Example: "TWO WEEKS ON, TWO WEEKS OFF".

### CMROUTE
- **Order:** 26
- **Label:** Route of Administration
- **Type:** Char
- **Controlled Terms:** C66729
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS".

### CMADJ
- **Order:** 27
- **Label:** Reason for Dose Adjustment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes reason or explanation of why a dose is adjusted. Examples: "ADVERSE EVENT", "INSUFFICIENT RESPONSE", "NON-MEDICAL REASON".

### CMRSDISC
- **Order:** 28
- **Label:** Reason the Intervention Was Discontinued
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** When dosing of a treatment is recorded over multiple successive records, this variable is applicable only for the (chronologically) last record for the treatment.

### TAETORD
- **Order:** 29
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the medication administration started. Null for medications that started before study participation.

### EPOCH
- **Order:** 30
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the medication administration. Null for medications that started before study participation.

### CMSTDTC
- **Order:** 31
- **Label:** Start Date/Time of Medication
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of the medication administration represented in ISO 8601 character format.

### CMENDTC
- **Order:** 32
- **Label:** End Date/Time of Medication
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the medication administration represented in ISO 8601 character format.

### CMSTDY
- **Order:** 33
- **Label:** Study Day of Start of Medication
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of medication relative to the sponsor-defined RFSTDTC.

### CMENDY
- **Order:** 34
- **Label:** Study Day of End of Medication
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of medication relative to the sponsor-defined RFSTDTC.

### CMDUR
- **Order:** 35
- **Label:** Duration
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration for a treatment episode. Used only if collected on the CRF and not derived from start and end date/times.

### CMSTRF
- **Order:** 36
- **Label:** Start Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the start of the medication relative to sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR" was collected, this information may be translated into CMSTRF.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CMENRF
- **Order:** 37
- **Label:** End Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the end of the medication relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING, or "CONTINUING" was collected, this information may be translated into CMENRF.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CMSTRTPT
- **Order:** 38
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the medication as being before or after the sponsor-defined reference time point defined by variable CMSTTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CMSTTPT
- **Order:** 39
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by CMSTRTPT. Examples: "2003-12-15", "VISIT 1".

### CMENRTPT
- **Order:** 40
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the medication as being before or after the sponsor-defined reference time point defined by variable CMENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CMENTPT
- **Order:** 41
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by CMENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Pharmaceutical Dosage Form (C66726)](../../terminology/core/interventions.md) — CMDOSFRM
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — CMSTRF, CMENRF, CMSTRTPT, CMENRTPT
- [Route of Administration Response (C66729)](../../terminology/core/interventions.md) — CMROUTE
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — CMPRESP, CMOCCUR
- [Not Done (C66789)](../../terminology/core/general_part4.md) — CMSTAT
- [Frequency (C71113)](../../terminology/core/interventions.md) — CMDOSFRQ
- [Unit (C71620)](../../terminology/core/general_part5.md) — CMDOSU
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Interventions):** AG, EC, EX, ML, PR, SU
- **Event:** [AE](../AE/) — adverse events treated by concomitant medication
- **Exposure:** [EC](../EC/) — protocol-specified vs concomitant treatments

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Interventions class definition](../../model/02_observation_classes.md)
