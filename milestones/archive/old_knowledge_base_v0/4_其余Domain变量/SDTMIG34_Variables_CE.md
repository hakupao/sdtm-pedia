# SDTM IG v3.4 Variables - CE Domain

**Domain Code:** `CE`

**Total Variables:** 32

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `USUBJID` | Unique Subject Identifier | Char | Req | Identifier | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| `CESEQ` | Sequence Number | Num | Req | Identifier | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| `CEGRPID` | Group ID | Char | Perm | Identifier | Used to link together a block of related records for a subject within a domain. |
| `CEREFID` | Reference ID | Char | Perm | Identifier | Internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or medical image). |
| `CESPID` | Sponsor-Defined Identifier | Char | Perm | Identifier | Sponsor-defined identifier. |
| `CETERM` | Reported Term for the Clinical Event | Char | Req | Topic | Term for the medical condition or event. Most likely preprinted on CRF. |
| `CEDECOD` | Dictionary-Derived Term | Char | Perm | Synonym Qualifier | Controlled terminology for the name of the clinical event. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. |
| `CECAT` | Category for the Clinical Event | Char | Perm | Grouping Qualifier | Used to define a category of related records. |
| `CESCAT` | Subcategory for the Clinical Event | Char | Perm | Grouping Qualifier | A further categorization of the condition or event. |
| `CEPRESP` | Clinical Event Pre-specified | Char | Perm | Variable Qualifier | Used to indicate whether the event in CETERM was prespecified. Value is "Y" for prespecified events and null for spontaneously reported events. |
| `CEOCCUR` | Clinical Event Occurrence | Char | Perm | Record Qualifier | Used when the occurrence of specific events is solicited, to indicate whether or not a clinical event occurred. Values are null for spontaneously reported events. |
| `CESTAT` | Completion Status | Char | Perm | Record Qualifier | The status indicates that a question from a prespecified list was not answered. |
| `CEREASND` | Reason Clinical Event Not Collected | Char | Perm | Record Qualifier | Describes the reason clinical event data was not collected. Used in conjunction with CESTAT when value is "NOT DONE". |
| `CEBODSYS` | Body System or Organ Class | Char | Perm | Record Qualifier | Dictionary-derived. Body system or organ class that is involved in an event or measurement from a standard hierarchy (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables, which may not necessarily be the primary SOC. |
| `CESEV` | Severity/Intensity | Char | Perm | Record Qualifier | The severity or intensity of the event. Examples: "MILD", "MODERATE", "SEVERE". |
| `CETOXGR` | Standard Toxicity Grade | Char | Perm | Record Qualifier | Toxicity grade according to a standard toxicity scale (e.g., Common Terminology Criteria for Adverse Events (CTCAE) v3.0). Sponsor should specify name of the scale and version used in the metadata. If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). |
| `TAETORD` | Planned Order of Element within Arm | Num | Perm | Timing | Number that gives the planned order of the element within the arm for the element in which the clinical event started. |
| `EPOCH` | Epoch | Char | Perm | Timing | Epoch associated with the start date/time of the clinical event. |
| `CEDTC` | Date/Time of Event Collection | Char | Perm | Timing | Collection date and time for the clinical event observation represented in ISO 8601 character format. |
| `CESTDTC` | Start Date/Time of Clinical Event | Char | Perm | Timing | Start date/time of the clinical event represented in ISO 8601 character format. |
| `CEENDTC` | End Date/Time of Clinical Event | Char | Perm | Timing | End date/time of the clinical event, represented in ISO 8601 character format. |
| `CEDY` | Study Day of Event Collection | Num | Perm | Timing | Study day of clinical event collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission. |
| `CESTDY` | Study Day of Start of Event | Num | Perm | Timing | Actual study day of start of the clinical event expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `CEENDY` | Study Day of End of Event | Num | Perm | Timing | Actual study day of end of the clinical event expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| `CESTRF` | Start Relative to Reference Period | Char | Perm | Timing | Describes the start of the clinical event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `CEENRF` | End Relative to Reference Period | Char | Perm | Timing | Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `CESTRTPT` | Start Relative to Reference Time Point | Char | Perm | Timing | Identifies the start of the observation as being before or after the reference time point defined by variable CESTTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `CESTTPT` | Start Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by --STRTPT. Examples: "2003-12-15", "VISIT 1". |
| `CEENRTPT` | End Relative to Reference Time Point | Char | Perm | Timing | Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable CEENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables. |
| `CEENTPT` | End Reference Time Point | Char | Perm | Timing | Description or date/time in ISO 8601 character format of the reference point referred to by CEENRTPT. Examples: "2003-12-25", "VISIT 2". |
