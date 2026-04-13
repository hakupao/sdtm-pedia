# AE — Adverse Events

> Class: Events | Structure: One record per adverse event per subject

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

### SPDEVID
- **Order:** 4
- **Label:** Sponsor Device Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** A sequence of characters used by the sponsor to uniquely identify a specific device. Used to represent a device associated in some way with the adverse event. SPDEVID values are defined in the Device Identifiers (DI) domain.

### AESEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### AEGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### AEREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier such as a serial number on an SAE reporting form.

### AESPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. It may be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on an Adverse Events CRF page.

### AETERM
- **Order:** 9
- **Label:** Reported Term for the Adverse Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim name of the event.

### AEMODIFY
- **Order:** 10
- **Label:** Modified Reported Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If AETERM is modified to facilitate coding, then AEMODIFY will contain the modified text.

### AELLT
- **Order:** 11
- **Label:** Lowest Level Term
- **Type:** Char
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary-derived text description of the lowest level term.

### AELLTCD
- **Order:** 12
- **Label:** Lowest Level Term Code
- **Type:** Num
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary-derived code for the lowest level term.

### AEDECOD
- **Order:** 13
- **Label:** Dictionary-Derived Term
- **Type:** Char
- **Controlled Terms:** MedDRA
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Dictionary-derived text description of AETERM or AEMODIFY. Equivalent to the Preferred Term (PT in MedDRA). The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

### AEPTCD
- **Order:** 14
- **Label:** Preferred Term Code
- **Type:** Num
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary-derived code for the preferred term.

### AEHLT
- **Order:** 15
- **Label:** High Level Term
- **Type:** Char
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary-derived text description of the high level term for the primary system organ class (SOC).

### AEHLTCD
- **Order:** 16
- **Label:** High Level Term Code
- **Type:** Num
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary-derived code for the high level term for the primary SOC.

### AEHLGT
- **Order:** 17
- **Label:** High Level Group Term
- **Type:** Char
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary-derived text description of the high level group term for the primary SOC.

### AEHLGTCD
- **Order:** 18
- **Label:** High Level Group Term Code
- **Type:** Num
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary-derived code for the high level group term for the primary SOC.

### AECAT
- **Order:** 19
- **Label:** Category for Adverse Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records. Examples: "BLEEDING", "NEUROPSYCHIATRIC".

### AESCAT
- **Order:** 20
- **Label:** Subcategory for Adverse Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of adverse event. Example: "NEUROLOGIC".

### AEPRESP
- **Order:** 21
- **Label:** Pre-Specified Adverse Event
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A value of "Y" indicates that this adverse event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms).

### AEBODSYS
- **Order:** 22
- **Label:** Body System or Organ Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary derived. Body system or organ class used by the sponsor from the coding dictionary (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables, which may not necessarily be the primary SOC.

### AEBDSYCD
- **Order:** 23
- **Label:** Body System or Organ Class Code
- **Type:** Num
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary derived. Code for the body system or organ class used by the sponsor. When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables, which may not necessarily be the primary SOC.

### AESOC
- **Order:** 24
- **Label:** Primary System Organ Class
- **Type:** Char
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary-derived text description of the primary SOC. Will be the same as AEBODSYS if the primary SOC was used for analysis.

### AESOCCD
- **Order:** 25
- **Label:** Primary System Organ Class Code
- **Type:** Num
- **Controlled Terms:** MedDRA
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dictionary-derived code for the primary SOC. Will be the same as AEBDSYCD if the primary SOC was used for analysis.

### AELOC
- **Order:** 26
- **Label:** Location of Event
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes anatomical location relevant for the event (e.g., "ARM" for skin rash).

### AESEV
- **Order:** 27
- **Label:** Severity/Intensity
- **Type:** Char
- **Controlled Terms:** C66769
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The severity or intensity of the event. Examples: "MILD", "MODERATE", "SEVERE".

### AESER
- **Order:** 28
- **Label:** Serious Event
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Is this a serious event? Valid values are "Y" and "N".

### AEACN
- **Order:** 29
- **Label:** Action Taken with Study Treatment
- **Type:** Char
- **Controlled Terms:** C66767
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Describes changes to the study treatment as a result of the event. AEACN is specifically for the relationship to study treatment. AEACNOTH is for actions unrelated to dose adjustments of study treatment. Examples of AEACN values include ICH E2B values: "DRUG WITHDRAWN", "DOSE REDUCED", "DOSE INCREASED", "DOSE NOT CHANGED", "UNKNOWN" and "NOT APPLICABLE".

### AEACNOTH
- **Order:** 30
- **Label:** Other Action Taken
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes other actions taken as a result of the event that are unrelated to dose adjustments of study treatment. Usually reported as free text. Example: "TREATMENT UNBLINDED. PRIMARY CARE PHYSICIAN NOTIFIED".

### AEACNDEV
- **Order:** 31
- **Label:** Action Taken with Device
- **Type:** Char
- **Controlled Terms:** C111110
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** An action taken with a device as the result of the event. The device may or may not be a device under study.

### AEREL
- **Order:** 32
- **Label:** Causality
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Records the investigator's opinion as to the causality of the event to the treatment. ICH does not establish any required or recommended terms for non-device relatedness. ICH E2A and E2B examples include (up-cased here for alignment to SDTM conventions) terms such as "NOT RELATED", "UNLIKELY RELATED", "POSSIBLY RELATED", "RELATED", but these example terms do not establish any conventions or expectations. Controlled terminology may be defined in the future. Check with regulatory authority for population of this variable.

### AERLDEV
- **Order:** 33
- **Label:** Relationship of Event to Device
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** A judgment as to the likelihood that the device caused the adverse event. The relationship is to a device identified in the data (i.e., has an SPDEVID). The device may be ancillary or under study. \n Terminology: \n * In the EU, follow the European Commission Guidelines on Medical Devices, Clinical Investigations: SAE Reporting (MEDDEV 2.7/3) (e.g., Not Related, Unlikely, Possible, Probable, Causal Relationship), with device-specific definitions. \n * No required Controlled Terminology in US.

### AERELNST
- **Order:** 34
- **Label:** Relationship to Non-Study Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Records the investigator's opinion as to whether the event may have been due to a treatment other than study drug. May be reported as free text. Example: "MORE LIKELY RELATED TO ASPIRIN USE".

### AEPATT
- **Order:** 35
- **Label:** Pattern of Adverse Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the pattern of the event over time. Examples: "INTERMITTENT", "CONTINUOUS", "SINGLE EVENT".

### AEOUT
- **Order:** 36
- **Label:** Outcome of Adverse Event
- **Type:** Char
- **Controlled Terms:** C66768
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of the outcome of an event.

### AESCAN
- **Order:** 37
- **Label:** Involves Cancer
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Was the serious event associated with the development of cancer? Valid values are "Y" and "N". This is a legacy seriousness criterion. It is not included in ICH E2A or E2B.

### AESCONG
- **Order:** 38
- **Label:** Congenital Anomaly or Birth Defect
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Was the serious event associated with congenital anomaly or birth defect? Valid values are "Y" and "N".

### AESDISAB
- **Order:** 39
- **Label:** Persist or Signif Disability/Incapacity
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Did the serious event result in persistent or significant disability/incapacity? Valid values are "Y" and "N".

### AESDTH
- **Order:** 40
- **Label:** Results in Death
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Did the serious event result in death? Valid values are "Y" and "N".

### AESHOSP
- **Order:** 41
- **Label:** Requires or Prolongs Hospitalization
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Did the serious event require or prolong hospitalization? Valid values are "Y" and "N".

### AESLIFE
- **Order:** 42
- **Label:** Is Life Threatening
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Was the serious event life-threatening? Valid values are "Y" and "N".

### AESOD
- **Order:** 43
- **Label:** Occurred with Overdose
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Did the serious event occur with an overdose? Valid values are "Y" and "N". This is a legacy seriousness criterion. It is not included in ICH E2A or E2B.

### AESMIE
- **Order:** 44
- **Label:** Other Medically Important Serious Event
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Do additional categories for seriousness apply? Valid values are "Y" and "N".

### AESINTV
- **Order:** 45
- **Label:** Needs Intervention to Prevent Impairment
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Records whether medical or surgical intervention was necessary to preclude permanent impairment of a body function, or to prevent permanent damage to a body structure, with either situation suspected to be due to the use of a medical product. This variable is used in conjunction with the other "seriousness" variables (e.g., fatal, life-threatening). It is part of the US federal government definition of a serious adverse event; see 21 CFR Part 803.3(w)(3).

### AEUNANT
- **Order:** 46
- **Label:** Unanticipated Adverse Device Effect
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Any serious adverse effect on health or safety or any life-threatening problem or death caused by or associated with a device, if that effect, problem, or death was not previously identified in nature, severity, or degree of incidence in the investigational plan or application (including a supplementary plan or application), \n or \n any other unanticipated serious problem associated with a device that relates to the rights, safety, or welfare of subjects. (21 CFR Part 812.3(s)). \n This variable applies only to serious AEs and should hold collected data; if the value is derived, it should be held in ADaM.

### AERLPRT
- **Order:** 47
- **Label:** Rel of AE to Non-Dev-Rel Study Activity
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The investigator's opinion as to the causality of the event as related to other protocol-required activities, actions, or assessments (e.g., medication changes, tests/assessments, other procedures). The relationship is to a protocol-specified, non-device-related activity where the device is identified in the data (i.e., has an SPDEVID). The device may be ancillary or under study. \n Terminology: \n * In the EU, follow the European Commission Guidelines on Medical Devices, Clinical Investigations: SAE Reporting (MEDDEV 2.7/3) (e.g., Not Related, Unlikely, Possible, Probable, Causal Relationship), with device-specific definitions. \n * No required Controlled Terminology in US.

### AERLPRC
- **Order:** 48
- **Label:** Rel of AE to Device-Related Procedure
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The investigator's opinion as to the likelihood that the device-related study procedure (e.g., implant/insertion, revision/adjustment, explant/removal) caused the AE. The relationship is to a device-related procedure where the device is identified in the data (i.e., has an SPDEVID). The device may be ancillary or under study. \n Terminology: \n * In the EU, follow the European Commission Guidelines on Medical Devices, Clinical Investigations: SAE Reporting (MEDDEV 2.7/3) (e.g., Not Related, Unlikely, Possible, Probable, Causal Relationship), with device-specific definitions. \n * No required Controlled Terminology in US.

### AECONTRT
- **Order:** 49
- **Label:** Concomitant or Additional Trtmnt Given
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Was another treatment given because of the occurrence of the event? Valid values are "Y" and "N".

### AETOXGR
- **Order:** 50
- **Label:** Standard Toxicity Grade
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Toxicity grade according to a standard toxicity scale (e.g., Common Terminology Criteria for Adverse Events, CTCAE). Sponsors should specify the name of the scale and version used in the metadata (see assumption 7d). If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2").

### TAETORD
- **Order:** 51
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 52
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the adverse event. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP".

### AESTDTC
- **Order:** 53
- **Label:** Start Date/Time of Adverse Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of the adverse event represented in ISO 8601 character format.

### AEENDTC
- **Order:** 54
- **Label:** End Date/Time of Adverse Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time of the adverse event represented in ISO 8601 character format.

### AESTDY
- **Order:** 55
- **Label:** Study Day of Start of Adverse Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of adverse event relative to the sponsor-defined RFSTDTC.

### AEENDY
- **Order:** 56
- **Label:** Study Day of End of Adverse Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of event relative to the sponsor-defined RFSTDTC.

### AEDUR
- **Order:** 57
- **Label:** Duration of Adverse Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration and unit of an adverse event. Used only if collected on the CRF and not derived from start and end date/times. Example: "P1DT2H" (for 1 day, 2 hours).

### AEENRF
- **Order:** 58
- **Label:** End Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point (RFSTDTC) and a discrete ending point (RFENDTC) of the trial. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AEENRTPT
- **Order:** 59
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the event as being before or after the reference time point defined by variable AEENTPT. \n Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AEENTPT
- **Order:** 60
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of date/time in ISO 8601 character format of the reference point referred to by AEENRTPT. Examples: "2003-12-25", "VISIT 2".
