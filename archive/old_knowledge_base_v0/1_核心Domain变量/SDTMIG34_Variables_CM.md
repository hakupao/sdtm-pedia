# SDTM IG v3.4 Variables - CM Domain

**Domain Code:** `CM`

**Total Variables:** 41

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `CMSEQ` | Sequence Number | Num | Req | Identifier | Sequence number to ensure uniqueness of subject records within a domain. May be any valid number. |
| `CMGRPID` | Group ID | Char | Perm | Identifier | Used to tie together a block of related records in a single domain for a subject. |
| `CMSPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined reference number. Example: a number preprinted on the CRF as an explicit line identifier or record identifier defined in the sponsor's operational database. Example: line number on a concomitant medication page. |
| `CMTRT` | Reported Name of Drug, Med, or Therapy | Char | Req | Topic | Verbatim medication name that is either preprinted or collected on a CRF. |
| `CMMODIFY` | Modified Reported Name | Char | Perm | Synonym Qualifier | If CMTRT is modified to facilitate coding, then CMMODIFY will contain the modified text. |
| `CMDECOD` | Standardized Medication Name | Char | Perm | Synonym Qualifier | Standardized or dictionary-derived text description of CMTRT or CMMODIFY. Equivalent to the generic drug name in WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then CMDECOD will be left blank. |
| `CMCAT` | Category for Medication | Char | Perm | Grouping Qualifier | Used to define a category of medications/treatment. Examples: "PRIOR", "CONCOMITANT", "ANTI-CANCER MEDICATION", "GENERAL CONMED". |
| `CMSCAT` | Subcategory for Medication | Char | Perm | Grouping Qualifier | A further categorization of medications/treatment. Examples: "CHEMOTHERAPY", "HORMONAL THERAPY", "ALTERNATIVE THERAPY". |
| `CMPRESP` | CM Pre-specified | Char | Perm | Variable Qualifier | Used to indicate whether ("Y"/null) information about the use of a specific medication was solicited on the CRF. |
| `CMOCCUR` | CM Occurrence | Char | Perm | Record Qualifier | When the use of a specific medication is solicited. CMOCCUR is used to indicate whether ("Y"/"N") use of the medication occurred. Values are null for medications not specifically solicited. |
| `CMSTAT` | Completion Status | Char | Perm | Record Qualifier | Used to indicate that a question about the occurrence of a prespecified intervention was not answered. Should be null or have a value of "NOT DONE". |
| `CMREASND` | Reason Medication Not Collected | Char | Perm | Record Qualifier | Reason not done. Used in conjunction with CMSTAT when value is "NOT DONE". |
| `CMINDC` | Indication | Char | Perm | Record Qualifier | Denotes why a medication was taken or administered. Examples: "NAUSEA", "HYPERTENSION". |
| `CMCLAS` | Medication Class | Char | Perm | Variable Qualifier | Drug class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit CMCLAS. |
| `CMCLASCD` | Medication Class Code | Char | Perm | Variable Qualifier | Class code corresponding to CMCLAS. Drug class. May be obtained from coding. When coding to a single class, populate with class code. If using a dictionary and coding to multiple classes, then follow Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit CMCLASCD. |
| `CMDOSE` | Dose per Administration | Num | Perm | Record Qualifier | Amount of CMTRT given. Not populated when CMDOSTXT is populated. |
| `CMDOSTXT` | Dose Description | Char | Perm | Record Qualifier | Dosing amounts or a range of dosing information collected in text form. Units may be stored in CMDOSU. Examples: "200-400", "15-20". Not populated when CMDOSE is populated. |
| `CMDOSU` | Dose Units | Char | Perm | Variable Qualifier | Units for CMDOSE, CMDOSTOT, or CMDOSTXT. Examples: "ng", "mg", "mg/kg". |
| `CMDOSFRM` | Dose Form | Char | Perm | Variable Qualifier | Dose form for CMTRT. Examples: "TABLET", "LOTION". |
| `CMDOSFRQ` | Dosing Frequency per Interval | Char | Perm | Record Qualifier | Usually expressed as the number of repeated administrations of CMDOSE within a specific time period. Examples: "BID" (twice daily), "Q12H" (every 12 hours). |
| `CMDOSTOT` | Total Daily Dose | Num | Perm | Record Qualifier | Total daily dose of CMTRT using the units in CMDOSU. Used when dosing is collected as total daily dose. Total dose over a period other than day could be recorded in a separate supplemental qualifier variable. |
| `CMDOSRGM` | Intended Dose Regimen | Char | Perm | Record Qualifier | Text description of the (intended) schedule or regimen for the Intervention. Example: "TWO WEEKS ON, TWO WEEKS OFF". |
| `CMROUTE` | Route of Administration | Char | Perm | Variable Qualifier | Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS". |
| `CMADJ` | Reason for Dose Adjustment | Char | Perm | Record Qualifier | Describes reason or explanation of why a dose is adjusted. Examples: "ADVERSE EVENT", "INSUFFICIENT RESPONSE", "NON-MEDICAL REASON". |
| `CMRSDISC` | Reason the Intervention Was Discontinued | Char | Perm | Record Qualifier | When dosing of a treatment is recorded over multiple successive records, this variable is applicable only for the (chronologically) last record for the treatment. |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the medication administration started. Null for medications that started before study participation. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the medication administration. Null for medications that started before study participation. |
| `CMSTDTC` | Start Date/Time of Medication | Char | Perm | Timing | Start date/time of the medication administration represented in ISO 8601 character format. |
| `CMENDTC` | End Date/Time of Medication | Char | Perm | Timing | End date/time of the medication administration represented in ISO 8601 character format. |
| `CMSTDY` | Study Day of Start of Medication | Num | Perm | Timing | Study day of start of medication relative to the sponsor-defined RFSTDTC. |
| `CMENDY` | Study Day of End of Medication | Num | Perm | Timing | Study day of end of medication relative to the sponsor-defined RFSTDTC. |
| `CMDUR` | Duration | Char | Perm | Timing | Collected duration for a treatment episode. Used only if collected on the CRF and not derived from start and end date/times. |
| `CMSTRF` | Start Relative to Reference Period | Char | Perm | Timing | Describes the start of the medication relative to sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR" was collected, this information may be translated into CMSTRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `CMENRF` | End Relative to Reference Period | Char | Perm | Timing | Describes the end of the medication relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING, or "CONTINUING" was collected, this information may be translated into CMENRF. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `CMSTRTPT` | Start Relative to Reference Time Point | Char | Perm | Timing | Identifies the start of the medication as being before or after the sponsor-defined reference time point defined by variable CMSTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `CMSTTPT` | Start Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by CMSTRTPT. Examples: "2003-12-15", "VISIT 1". |
| `CMENRTPT` | End Relative to Reference Time Point | Char | Perm | Timing | Identifies the end of the medication as being before or after the sponsor-defined reference time point defined by variable CMENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `CMENTPT` | End Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by CMENRTPT. Examples: "2003-12-25", "VISIT 2". |
