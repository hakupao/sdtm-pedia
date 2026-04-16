# EC — Exposure as Collected

> Class: Interventions | Structure: One record per protocol-specified study treatment, collected-dosing interval, per subject, per mood

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

### ECSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### ECGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### ECREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier (e.g., kit number, bottle label, vial identifier).

### ECSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page.

### ECLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains.

### ECLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related, grouped records across domains.

### ECTRT
- **Order:** 10
- **Label:** Name of Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Name of the intervention treatment known to the subject and/or administrator.

### ECMOOD
- **Order:** 11
- **Label:** Mood
- **Type:** Char
- **Controlled Terms:** C125923
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Mode or condition of the record specifying whether the intervention (activity) is intended to happen or has happened. Values align with BRIDG pillars (e.g., scheduled context, performed context) and HL7 activity moods (e.g., intent, event). Examples: "SCHEDULED", "PERFORMED".

### ECCAT
- **Order:** 12
- **Label:** Category of Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related ECTRT values.

### ECSCAT
- **Order:** 13
- **Label:** Subcategory of Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of ECCAT values.

### ECPRESP
- **Order:** 14
- **Label:** Pre-Specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when a specific intervention is prespecified. Values should be "Y" or null.

### ECOCCUR
- **Order:** 15
- **Label:** Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a treatment occurred when information about the occurrence is solicited. ECOCCUR = "N" when a treatment was not taken, not given, or missed.

### ECREASOC
- **Order:** 16
- **Label:** Reason for Occur Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The reason for the value in --OCCUR. If --OCCUR = "N", this is the reason the exposure did not occur.

### ECDOSE
- **Order:** 17
- **Label:** Dose
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Amount of ECTRT when numeric. Not populated when ECDOSTXT is populated.

### ECDOSTXT
- **Order:** 18
- **Label:** Dose Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of ECTRT when non-numeric. Dosing amounts or a range of dosing information collected in text form. Example: "200-400". Not populated when ECDOSE is populated.

### ECDOSU
- **Order:** 19
- **Label:** Dose Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Units for ECDOSE, ECDOSTOT, or ECDOSTXT.

### ECDOSFRM
- **Order:** 20
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dose form for ECTRT. Examples: "TABLET", "LOTION".

### ECDOSFRQ
- **Order:** 21
- **Label:** Dosing Frequency per Interval
- **Type:** Char
- **Controlled Terms:** C71113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Usually expressed as the number of repeated administrations of ECDOSE within a specific time period. Examples: "Q2H", "QD", "BID".

### ECDOSTOT
- **Order:** 22
- **Label:** Total Daily Dose
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Total daily dose of ECTRT using the units in ECDOSU. Used when dosing is collected as total daily dose.

### ECDOSRGM
- **Order:** 23
- **Label:** Intended Dose Regimen
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the intended schedule or regimen for the Intervention. Example: "TWO WEEKS ON", "TWO WEEKS OFF".

### ECROUTE
- **Order:** 24
- **Label:** Route of Administration
- **Type:** Char
- **Controlled Terms:** C66729
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS".

### ECLOT
- **Order:** 25
- **Label:** Lot Number
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Lot number of the ECTRT product.

### ECLOC
- **Order:** 26
- **Label:** Location of Dose Administration
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Specifies location of administration. Example: "ARM", "LIP".

### ECLAT
- **Order:** 27
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing laterality of the intervention administration. Examples: "LEFT", "RIGHT".

### ECDIR
- **Order:** 28
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL", "UPPER".

### ECPORTOT
- **Order:** 29
- **Label:** Portion or Totality
- **Type:** Char
- **Controlled Terms:** C99075
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing distribution (i.e., arrangement of, apportioning of). Examples: "ENTIRE", "SINGLE", "SEGMENT".

### ECFAST
- **Order:** 30
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status. Examples: "Y", "N".

### ECPSTRG
- **Order:** 31
- **Label:** Pharmaceutical Strength
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of an active ingredient expressed quantitatively per dosage unit, per unit of volume, or per unit of weight, according to the pharmaceutical dose form.

### ECPSTRGU
- **Order:** 32
- **Label:** Pharmaceutical Strength Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for ECPSTRG. Examples: "mg/TABLET", "mg/mL".

### ECADJ
- **Order:** 33
- **Label:** Reason for Dose Adjustment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes reason or explanation of why a dose is adjusted.

### TAETORD
- **Order:** 34
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 35
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Trial epoch of the exposure as collected record. Examples: "RUN-IN", "TREATMENT".

### ECSTDTC
- **Order:** 36
- **Label:** Start Date/Time of Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** The date/time when administration of the treatment indicated by ECTRT and ECDOSE began.

### ECENDTC
- **Order:** 37
- **Label:** End Date/Time of Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** The date/time when administration of the treatment indicated by ECTRT and ECDOSE ended. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, ECSTDTC should be copied to ECENDTC as the standard representation.

### ECSTDY
- **Order:** 38
- **Label:** Study Day of Start of Treatment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of ECSTDTC relative to the sponsor-defined DM.RFSTDTC.

### ECENDY
- **Order:** 39
- **Label:** Study Day of End of Treatment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of ECENDTC relative to the sponsor-defined DM.RFSTDTC.

### ECDUR
- **Order:** 40
- **Label:** Duration of Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of administration. Used only if collected on the CRF and not derived from start and end date/times.

### ECTPT
- **Order:** 41
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when administration should occur. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ECTPTNUM and ECTPTREF.

### ECTPTNUM
- **Order:** 42
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of ECTPT to aid in sorting.

### ECELTM
- **Order:** 43
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to the planned fixed reference (ECTPTREF). This variable is useful where there are repetitive measures. Not a clock time.

### ECTPTREF
- **Order:** 44
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by ECELTM, ECTPTNUM, and ECTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### ECRFTDTC
- **Order:** 45
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by ECTPTREF.
---

## Cross References

### Controlled Terminology
- [BRIDG Activity Mood (C125923)](../../terminology/core/interventions.md) — ECMOOD
- [Pharmaceutical Dosage Form (C66726)](../../terminology/core/interventions.md) — ECDOSFRM
- [Route of Administration Response (C66729)](../../terminology/core/interventions.md) — ECROUTE
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — ECPRESP, ECOCCUR, ECFAST
- [Frequency (C71113)](../../terminology/core/interventions.md) — ECDOSFRQ
- [Unit (C71620)](../../terminology/core/general_part5.md) — ECDOSU, ECPSTRGU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — ECLOC
- [Laterality (C99073)](../../terminology/core/general_part2.md) — ECLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — ECDIR
- [Portion/Totality (C99075)](../../terminology/core/general_part4.md) — ECPORTOT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Interventions):** AG, CM, EX, ML, PR, SU
- **Shared Dataset:** [EX](../EX/) — exposure as collected vs exposure

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Interventions class definition](../../model/02_observation_classes.md)
