# SDTM IG v3.4 Variables - PR Domain

**Domain Code:** `PR`

**Total Variables:** 45

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `PRSEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `PRGRPID` | Group ID | Char | Perm | Identifier | Used to link together a block of related records within a subject in a domain. |
| `PRSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. Example: preprinted line identifier on a CRF, record identifier defined in the sponsor's operational database. |
| `PRLNKID` | Link ID | Char | Perm | Identifier | Used to facilitate identification of relationships between records. |
| `PRLNKGRP` | Link Group ID | Char | Perm | Identifier | Used to facilitate identification of relationships between records. |
| `PRTRT` | Reported Name of Procedure | Char | Req | Topic | Name of procedure performed, either preprinted or collected on a CRF. |
| `PRDECOD` | Standardized Procedure Name | Char | Perm | Synonym Qualifier | Standardized or dictionary-derived name of PRTRT. If the codelist "PROCEDUR" is not used, the sponsor is expected to provide the dictionary name and version used to map the terms in the external codelist element in the Define-XML document. If an intervention term does not have a decode value, then PRDECOD will be null. |
| `PRCAT` | Category | Char | Perm | Grouping Qualifier | Used to define a category of procedure values. |
| `PRSCAT` | Subcategory | Char | Perm | Grouping Qualifier | Used to define a further categorization of PRCAT values. |
| `PRPRESP` | Pre-specified | Char | Perm | Variable Qualifier | Used when a specific procedure is pre-specified on a CRF. Values should be "Y" or null. |
| `PROCCUR` | Occurrence | Char | Perm | Record Qualifier | Used to record whether a prespecified procedure occurred when information about the occurrence of a specific procedure is solicited. |
| `PRINDC` | Indication | Char | Perm | Record Qualifier | Denotes the indication for the procedure (e.g., why the procedure was performed). |
| `PRDOSE` | Dose | Num | Perm | Record Qualifier | Amount of PRTRT administered. Not populated when PRDOSTXT is populated. |
| `PRDOSTXT` | Dose Description | Char | Perm | Record Qualifier | Dosing information collected in text form. Examples: "<1", "200-400". Not populated when PRDOSE is populated. |
| `PRDOSU` | Dose Units | Char | Perm | Variable Qualifier | Units for PRDOSE, PRDOSTOT, or PRDOSTXT. |
| `PRDOSFRM` | Dose Form | Char | Perm | Variable Qualifier | Dose form for PRTRT. |
| `PRDOSFRQ` | Dosing Frequency per Interval | Char | Perm | Record Qualifier | Usually expressed as the number of doses given per a specific interval. |
| `PRDOSRGM` | Intended Dose Regimen | Char | Perm | Record Qualifier | Text description of the intended schedule or regimen for the procedure. |
| `PRROUTE` | Route of Administration | Char | Perm | Variable Qualifier | Route of administration for PRTRT. |
| `PRLOC` | Location of Procedure | Char | Perm | Record Qualifier | Anatomical location of a procedure. |
| `PRLAT` | Laterality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing laterality. |
| `PRDIR` | Directionality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing directionality. |
| `PRPORTOT` | Portion or Totality | Char | Perm | Variable Qualifier | Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, apportioning of. |
| `VISITNUM` | Visit Number | Num | Perm | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| `VISIT` | Visit Name | Char | Perm | Timing | Protocol-defined description of a clinical encounter. |
| `VISITDY` | Planned Study Day of Visit | Num | Perm | Timing | Planned study day of VISIT. Should be an integer. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the procedure. |
| `PRSTDTC` | Start Date/Time of Procedure | Char | Exp | Timing | Start date/time of the procedure represented in ISO 8601 character format. |
| `PRENDTC` | End Date/Time of Procedure | Char | Perm | Timing | End date/time of the procedure represented in ISO 8601 character format. |
| `PRSTDY` | Study Day of Start of Procedure | Num | Perm | Timing | Study day of start of procedure expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `PRENDY` | Study Day of End of Procedure | Num | Perm | Timing | Study day of end of procedure expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `PRDUR` | Duration of Procedure | Char | Perm | Timing | Collected duration of a procedure represented in ISO 8601 character format. Used only if collected on the CRF and not derived from start and end date/times. |
| `PRTPT` | Planned Time Point Name | Char | Perm | Timing | Text description of time when a procedure should be performed. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PRTPTNUM and PRTPTREF. |
| `PRTPTNUM` | Planned Time Point Number | Num | Perm | Timing | Numerical version of planned time point used in sorting. |
| `PRELTM` | Planned Elapsed Time from Time Point Ref | Char | Perm | Timing | Planned elapsed time in ISO 8601 format relative to a planned fixed reference (PRTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration. |
| `PRTPTREF` | Time Point Reference | Char | Perm | Timing | Description of the fixed reference point referred to by PRELTM, PRTPTNUM, and PRTPT. |
| `PRRFTDTC` | Date/Time of Reference Time Point | Char | Perm | Timing | Date/time for a fixed reference time point defined by PRTRTREF in ISO 8601 character format. |
| `PRSTRTPT` | Start Relative to Reference Time Point | Char | Perm | Timing | Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable PRSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `PRSTTPT` | Start Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by PRSTRTPT. Examples: "2003-12-15", "VISIT 1". |
| `PRENRTPT` | End Relative to Reference Time Point | Char | Perm | Timing | Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable PRENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `PRENTPT` | End Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by PRENRTPT. Examples: "2003-12-25", "VISIT 2". |
