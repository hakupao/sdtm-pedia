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
