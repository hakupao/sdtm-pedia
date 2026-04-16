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
