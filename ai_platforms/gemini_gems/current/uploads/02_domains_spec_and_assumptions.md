# 02 Domains Spec & Assumptions (63 domains, spec+assumptions interleaved)

> Generated: 2026-04-21T02:11:47Z
> Source files: 126
> Total tokens (cl100k_base): 240,362

> Source order is preserved for traceability. `<!-- source: ... -->` comments mark each segment's origin file (relative to repo root).

---
<!-- source: knowledge_base/domains/AE/spec.md -->
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
- **CDISC Notes:** A judgment as to the likelihood that the device caused the adverse event. The relationship is to a device identified in the data (i.e., has an SPDEVID). The device may be ancillary or under study.  Terminology:  * In the EU, follow the European Commission Guidelines on Medical Devices, Clinical Investigations: SAE Reporting (MEDDEV 2.7/3) (e.g., Not Related, Unlikely, Possible, Probable, Causal Relationship), with device-specific definitions.  * No required Controlled Terminology in US.

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
- **CDISC Notes:** Any serious adverse effect on health or safety or any life-threatening problem or death caused by or associated with a device, if that effect, problem, or death was not previously identified in nature, severity, or degree of incidence in the investigational plan or application (including a supplementary plan or application),  or  any other unanticipated serious problem associated with a device that relates to the rights, safety, or welfare of subjects. (21 CFR Part 812.3(s)).  This variable applies only to serious AEs and should hold collected data; if the value is derived, it should be held in ADaM.

### AERLPRT
- **Order:** 47
- **Label:** Rel of AE to Non-Dev-Rel Study Activity
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The investigator's opinion as to the causality of the event as related to other protocol-required activities, actions, or assessments (e.g., medication changes, tests/assessments, other procedures). The relationship is to a protocol-specified, non-device-related activity where the device is identified in the data (i.e., has an SPDEVID). The device may be ancillary or under study.  Terminology:  * In the EU, follow the European Commission Guidelines on Medical Devices, Clinical Investigations: SAE Reporting (MEDDEV 2.7/3) (e.g., Not Related, Unlikely, Possible, Probable, Causal Relationship), with device-specific definitions.  * No required Controlled Terminology in US.

### AERLPRC
- **Order:** 48
- **Label:** Rel of AE to Device-Related Procedure
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The investigator's opinion as to the likelihood that the device-related study procedure (e.g., implant/insertion, revision/adjustment, explant/removal) caused the AE. The relationship is to a device-related procedure where the device is identified in the data (i.e., has an SPDEVID). The device may be ancillary or under study.  Terminology:  * In the EU, follow the European Commission Guidelines on Medical Devices, Clinical Investigations: SAE Reporting (MEDDEV 2.7/3) (e.g., Not Related, Unlikely, Possible, Probable, Causal Relationship), with device-specific definitions.  * No required Controlled Terminology in US.

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
- **CDISC Notes:** Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point (RFSTDTC) and a discrete ending point (RFENDTC) of the trial.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AEENRTPT
- **Order:** 59
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the event as being before or after the reference time point defined by variable AEENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AEENTPT
- **Order:** 60
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of date/time in ISO 8601 character format of the reference point referred to by AEENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Device Events Action Taken with Device (C111110)](../../terminology/core/ae.md) — AEACNDEV
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — AEENRF, AEENRTPT
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — AEPRESP, AESER, AESCAN, AESCONG, AESDISAB ... (13 total)
- [Action Taken with Study Treatment (C66767)](../../terminology/core/ae.md) — AEACN
- [Outcome of Event (C66768)](../../terminology/core/ae.md) — AEOUT
- [Severity/Intensity Scale for Adverse Events (C66769)](../../terminology/core/ae.md) — AESEV
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — AELOC
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Events):** BE, CE, DS, DV, HO, MH
- **Findings About:** [FA](../FA/) — prespecified AE findings (AEPRESP)
- **Treatment:** [CM](../CM/) — concomitant medications linked via RELREC
- **Treatment:** [PR](../PR/) — procedures linked via RELREC

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Events class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/AE/assumptions.md -->
# AE — Assumptions

1. The Adverse Events dataset includes clinical data describing "any untoward medical occurrence in a patient or clinical investigation subject administered a pharmaceutical product and which does not necessarily have to have a causal relationship with this treatment" (ICH E2A). In consultation with regulatory authorities, sponsors may extend or limit the scope of adverse event collection (e.g., collecting pre-treatment events related to trial conduct, not collecting events that are assessed as efficacy endpoints). The events included in the AE dataset should be consistent with the protocol requirements. Adverse events may be captured either as free text or via a prespecified list of terms.

2. **AE description and coding**
   a. AETERM captures the verbatim term collected for the event. It is the topic variable for the AE dataset. AETERM is a required variable and must have a value.
   b. AEMODIFY is a permissible variable and should be included if the sponsor's procedure permits modification of a verbatim term for coding. The variable should be populated as per the sponsor's procedures.
   c. AEDECOD is the preferred term derived by the sponsor from the coding dictionary. It is a required variable and must have a value. It is expected that the reported term (AETERM) will be coded using a standard dictionary such as MedDRA. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.
   d. AEBODSYS is the system organ class (SOC) from the coding dictionary associated with the adverse event by the sponsor. This value may differ from the primary SOC designated in the coding dictionary's standard hierarchy. It is expected that this variable will be populated.

3. **Additional categorization and grouping**
   a. AECAT and AESCAT should not be redundant with the domain code or dictionary classification provided by AEDECOD and AEBODSYS (i.e., they should provide a different means of defining or classifying AE records). AECAT and AESCAT are intended for categorizations that are defined in advance. For example, a sponsor may have a CRF page for AEs of special interest and another page for all other AEs. AECAT and AESCAT should not be used for after-the-fact categorizations such as "clinically significant." In cases where a category of AEs of special interest resembles a part of the dictionary hierarchy (e.g., "CARDIAC EVENTS"), the categorization represented by AECAT and AESCAT may differ from the categorization derived from the coding dictionary.
   b. AEGRPID may be used to link (or associate) different records together to form a block of related records at the subject level within the AE domain, see Section 4.2.6, Grouping Variables and Categorization.

4. **Prespecified terms; presence or absence of events**
   a. Adverse events are generally collected in 2 different ways, either by recording free text or using a prespecified list of terms. In the latter case, the solicitation of information on specific adverse events may affect the frequency at which they are reported; therefore, the fact that a specific adverse event was solicited may be of interest to reviewers. An AEPRESP value of "Y" is used to indicate that the event in AETERM was prespecified on the CRF.
   b. If it is important to know which adverse events from a prespecified list were not reported as well as those that did occur, these data should be submitted in a Findings class dataset such as Findings About Events and Interventions (see Section 6.4, Findings About Events or Interventions). A record should be included in that Findings dataset for each prespecified adverse-event term. Records for adverse events that actually occurred should also exist in the AE dataset with AEPRESP set to "Y."
   c. If a study collects both prespecified adverse events and free-text events, the value of AEPRESP should be "Y" for all prespecified events and null for events reported as free text. AEPRESP is a permissible field and may be omitted from the dataset if all adverse events were collected as free text.
   d. When adverse events are collected with the recording of free text, a record may be entered into the sponsor's data management system to indicate "no adverse events" for a specific subject. For these subjects, do not include a record in the AE submission dataset to indicate that there were no events. Records should be included in the submission AE dataset only for adverse events that have actually occurred.

5. **Timing variables**
   a. Relative timing assessment "Ongoing" is common in the collection of AE information. AEENRF may be used when this relative timing assessment is made coincident with the end of the study reference period for the subject represented in the Demographics (DM) dataset (RFENDTC). AEENRTPT with AEENTPT may be used when "Ongoing" is relative to another date (e.g., the final safety follow-up visit date). See Section 4.4.7, Use of Relative Timing Variables.
   b. Additional timing variables (e.g., AEDTC) may be used when appropriate.

6. **Actions taken**
   a. AECONTRT is a Y/N variable. If the non-study treatment is collected, the name and other information about the treatment should be represented in the appropriate Interventions domain—usually Concomitant/Prior Medications (CM) or Procedures (PR)—and linked to the AE record with RELREC.
   b. Actions other than concomitant treatments are recorded in:
      - AEACN, only for actions taken with study treatment
      - AEACNDEV, for actions with a device
      - AEACNOTH, for actions that do not involve treatment or a device

7. **Other qualifier variables**
   a. If categories of serious events are collected secondarily to a leading question the values of the variables that capture reasons an event is considered serious (e.g., AESCAN, AESCONG) may be null. For example, if "Serious?" is answered "No", the values for these variables may be null. However, if "Serious?" is answered "Yes", at least one of them will have a "Y" response. Others may be "N" or null, according to the sponsor's convention.

      **CRF: AE Seriousness Classification**

      | Serious? | [ ] Yes  [ ] No |
      |----------|-----------------|
      | If yes, check all that apply: | [ ] Fatal  [ ] Life-threatening  [ ] Inpatient hospitalization or prolongation of existing hospitalization  [ ] Persistent or significant disability/incapacity  [ ] Congenital anomaly/birth defect  [ ] Other medically important serious event |

      On the other hand, if the CRF is structured so that a response is collected for each seriousness category, all category variables (e.g., AESDTH, AESHOSP) would be populated and AESER would be derived.
   b. The serious categories "Involves cancer" (AESCAN) and "Occurred with overdose" (AESOD) are not part of the ICH definition of a serious adverse event, but these categories are available for use in studies conducted under guidelines that existed prior to the FDA's adoption of the ICH definition.
   c. When a description of "Other Medically Important Serious Adverse Events" category is collected on a CRF, sponsors should place the description in the SUPPAE dataset using the standard supplemental qualifier name code AEOSOSP as described in Section 8.4, Relating Non-Standard Variables Values to a Parent Domain, and in Appendix C1, Supplemental Qualifiers Name Codes.
   d. In studies using toxicity grade according to a standard toxicity scale such as the Common Terminology Criteria for Adverse Events v3.0 (CTCAE), published by the National Cancer Institute (NCI; available at https://ctep.cancer.gov/protocoldevelopment/), AETOXGR should be used instead of AESEV. In most cases, either AESEV or AETOXGR is populated but not both. There may be cases when a sponsor may need to populate both variables. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.
   e. The structure of the AE domain is 1 record per adverse event per subject. It is the sponsor's responsibility to define an event. This definition may vary based on the sponsor's requirements for characterizing and reporting product safety and is usually described in the protocol. For example, the sponsor may submit 1 record that covers an adverse event from start to finish. Alternatively, if there is a need to evaluate AEs at a more granular level, a sponsor may submit a new record when severity, causality, or seriousness changes or worsens. By submitting these individual records, the sponsor indicates that each is considered to represent a different event. The submission dataset structure may differ from the structure at the time of collection. For example, a sponsor might collect data at each visit in order to meet operational needs, but submit records that summarize the event and contain the highest level of severity, causality, seriousness, and so on. Examples of dataset structure include:
      i. One record per adverse event per subject for each unique event. Multiple adverse event records reported by the investigator are submitted as summary records "collapsed" to the highest level of severity, causality, seriousness, and the final outcome.
      ii. One record per adverse event per subject. Changes over time in severity, causality, or seriousness are submitted as separate events. Alternatively, these changes may be submitted in a separate dataset based on the Findings About Events and Interventions model (see Section 6.4, Findings About Events or Interventions).
      iii. Other approaches may also be reasonable as long as they meet the sponsor's safety evaluation requirements and each submitted record represents a unique event. The domain-level metadata (see Section 3.2, Using the CDISC Domain Models in Regulatory Submissions – Dataset Metadata) should clarify the structure of the dataset.

8. Use of EPOCH and TAETORD: When EPOCH is included in the AE domain, it should be the epoch of the start of the adverse event. In other words, it should be based on AESTDTC, rather than AEENDTC. The computational method for EPOCH in the Define-XML document should describe any assumptions made to handle cases where an adverse event starts on the same day that a subject starts an epoch, if AESTDTC and SESTDTC are not captured with enough precision to determine the epoch of the onset of the adverse event unambiguously. Similarly, if TAETORD is included in the AE domain, it should be the value for the start of the adverse event, and the computational method in the Define-XML document should describe any assumptions.

9. Any additional identifier variables may be added to the AE domain.

10. The following qualifiers would not be used in AE: --OCCUR, --STAT, and--REASND. They are the only qualifiers from the SDTM Events class not in the AE domain. They are not permitted because the AE domain contains only records for adverse events that actually occurred. See Assumption 4b for information on how to deal with negative responses or missing responses to probing questions for prespecified adverse events.

11. Variable order in the domain should follow the rules as described in Section 4.1.4, Order of the Variables, and the order described in Section 1.1, Purpose.

12. The addition of AELLT, AELLTCD, AEPTCD, AEHLT, AEHLTCD, AEHLGT, AEHLGTCD, AEBDSYCD, AESOC, and AESOCD is applicable to submissions coded in MedDRA only. Data items are not expected for non-MedDRA coding.

<!-- source: knowledge_base/domains/AG/spec.md -->
# AG — Procedure Agents

> Class: Interventions | Structure: One record per recorded intervention occurrence per subject

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

### AGSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### AGGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### AGSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the procedure or test page.

### AGLNKID
- **Order:** 7
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains.This may be a one-to-one or a one-to-many relationship.

### AGLNKGRP
- **Order:** 8
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains.This will usually be a many-to-one relationship.

### AGTRT
- **Order:** 9
- **Label:** Reported Agent Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim medication name that is either preprinted or collected on a CRF.

### AGMODIFY
- **Order:** 10
- **Label:** Modified Reported Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If AGTRT is modified to facilitate coding, then AGMODIFY will contain the modified text.

### AGDECOD
- **Order:** 11
- **Label:** Standardized Agent Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized or dictionary-derived text description of AGTRT or AGMODIFY. Equivalent to the generic medication name in WHO Drug. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then AGDECOD will be left blank.

### AGCAT
- **Order:** 12
- **Label:** Category for Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of agent. Examples: "CHALLENGE AGENT", "PET TRACER".

### AGSCAT
- **Order:** 13
- **Label:** Subcategory for Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Further categorization of agent.

### AGPRESP
- **Order:** 14
- **Label:** AG Pre-Specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether ("Y"/null) information about the use of a specific agent was solicited on the CRF.

### AGOCCUR
- **Order:** 15
- **Label:** AG Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** When the use of specific agent is solicited, AGOCCUR is used to indicate whether ("Y"/"N") use of the agent occurred. Values are null for agents not specifically solicited.

### AGSTAT
- **Order:** 16
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question about a prespecified agent was not answered. Should be null or have a value of "NOT DONE".

### AGREASND
- **Order:** 17
- **Label:** Reason Procedure Agent Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason a response to a question about the occurrence of a procedure agent was not collected. Used in conjunction with AGSTAT when value is "NOT DONE".

### AGCLAS
- **Order:** 18
- **Label:** Agent Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Drug class. May be obtained from coding. When coding to a single class, populate with class value. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLAS.

### AGCLASCD
- **Order:** 19
- **Label:** Agent Class Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Class code corresponding to AGCLAS. Drug class. May be obtained from coding. When coding to a single class, populate with class code. If using a dictionary and coding to multiple classes, follow guidance in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable, or omit AGCLASCD.

### AGDOSE
- **Order:** 20
- **Label:** Dose per Administration
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of AGTRT taken.

### AGDOSTXT
- **Order:** 21
- **Label:** Dose Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Dosing amounts or a range of dosing information collected in text form. Units may be stored in AGDOSU. Examples: "200-400", "15-20".

### AGDOSU
- **Order:** 22
- **Label:** Dose Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Units for AGDOSE and AGDOSTXT. Examples: "ng", "mg", "mg/kg".

### AGDOSFRM
- **Order:** 23
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Dose form for AGTRT. Examples: "TABLET", "AEROSOL".

### AGDOSFRQ
- **Order:** 24
- **Label:** Dosing Frequency per Interval
- **Type:** Char
- **Controlled Terms:** C71113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Usually expressed as the number of repeated administrations of AGDOSE within a specific time period. Example: "ONCE".

### AGROUTE
- **Order:** 25
- **Label:** Route of Administration
- **Type:** Char
- **Controlled Terms:** C66729
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Route of administration for AGTRT. Example: "ORAL".

### VISITNUM
- **Order:** 26
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** 1. Clinical encounter number.  2. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 27
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** 1. Protocol-defined description of clinical encounter.  2. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 28
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 29
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the agent administration started.

### EPOCH
- **Order:** 30
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the agent administration started.

### AGSTDTC
- **Order:** 31
- **Label:** Start Date/Time of Agent
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The date/time when administration of the treatment indicated by AGTRT and the dosing variables began.

### AGENDTC
- **Order:** 32
- **Label:** End Date/Time of Agent
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The date/time when administration of the treatment indicated by AGTRT and the dosing variables ended.

### AGSTDY
- **Order:** 33
- **Label:** Study Day of Start of Agent
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of agent relative to the sponsor-defined RFSTDTC.

### AGENDY
- **Order:** 34
- **Label:** Study Day of End of Agent
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of agent relative to the sponsor-defined RFSTDTC.

### AGDUR
- **Order:** 35
- **Label:** Duration of Agent
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration for an agent episode. Used only if collected on the CRF and not derived from start and end date/times.

### AGSTRF
- **Order:** 36
- **Label:** Start Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the start of the agent relative to sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGSTRF.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AGENRF
- **Order:** 37
- **Label:** End Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the end of the agent relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics). If information such as "PRIOR", "ONGOING", or "CONTINUING" was collected, this information may be translated into AGENRF.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AGSTRTPT
- **Order:** 38
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the agent as being before or after the sponsor-defined reference time point defined by variable AGSTTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AGSTTPT
- **Order:** 39
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by AGSTRTPT. Examples: "2003-12-15", "VISIT 1".

### AGENRTPT
- **Order:** 40
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the agent as being before or after the reference time point defined by variable AGENTPT. Identifies the end of the agent as being before or after the sponsor-defined reference time point defined by variable AGENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### AGENTPT
- **Order:** 41
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by AGENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Pharmaceutical Dosage Form (C66726)](../../terminology/core/interventions.md) — AGDOSFRM
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — AGSTRF, AGENRF, AGSTRTPT, AGENRTPT
- [Route of Administration Response (C66729)](../../terminology/core/interventions.md) — AGROUTE
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — AGPRESP, AGOCCUR
- [Not Done (C66789)](../../terminology/core/general_part4.md) — AGSTAT
- [Frequency (C71113)](../../terminology/core/interventions.md) — AGDOSFRQ
- [Unit (C71620)](../../terminology/core/general_part5.md) — AGDOSU
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Interventions):** CM, EC, EX, ML, PR, SU

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Interventions class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/AG/assumptions.md -->
# AG — Assumptions

1. Purpose of the domain: Some tests involve administration of substances, and it has been unclear in which domain these should be represented.
   a. The Concomitant/Prior Medications (CM) domain seemed particularly inappropriate when the substance was one that would never be given as a medication. Even substances that are medications are not being used as such when they are given as part of a testing procedure.
   b. The Exposure (EX) domain also seemed inappropriate; although the testing procedure might be part of the study plan, these data would not be used or analyzed in the same way as data about study treatments. The AG domain was created to fill this gap.
   c. The AG domain has advantages over the Procedures (PR) domain for this purpose. It allows recording of multiple substance administrations for a single testing procedure. It also separates data about substance administrations from data about procedures that do not involve substance administration.
   d. Information about the conduct of the procedure with which the procedure agent administration was associated, if collected, should be represented in the PR domain.

2. Examples and structure
   a. Examples of agents administered as part of a procedure include a short-acting bronchodilator administered as part of a reversibility assessment and contrast agents or radio-labeled substances used in imaging studies.
   b. The structure of the AG domain is 1 record per agent intervention episode, or prespecified agent assessment per subject. It is the sponsor's responsibility to define an intervention episode. This definition may vary based on the sponsor's requirements for review and analysis.

3. AG description and coding
   a. AGTRT captures the name of the agent and it is the topic variable. It is a required variable and must have a value. AGTRT should include only the agent name, and should not include dosage, formulation, or other qualifying information. For example, "ALBUTEROL 2 PUFF" is not a valid value for AGTRT. This example should be expressed as AGTRT = "ALBUTEROL", AGDOSE = "2", AGDOSU = "PUFF", and AGDOSFRM = "AEROSOL".
   b. AGMODIFY should be included if the sponsor's procedure permits modification of a verbatim term for coding.
   c. AGDECOD is the standardized agent term derived by the sponsor from the coding dictionary. It is possible that the reported term (AGTRT) or the modified term (AGMODIFY) can be coded using a standard dictionary. In such cases, sponsors are expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

4. Prespecified terms; presence or absence of procedure agents
   a. AGPRESP is used to indicate whether an agent was prespecified.
   b. AGOCCUR is used to indicate whether a prespecified agent was used. A value of "Y" indicates that the agent was used and "N" indicates that it was not.
   c. If an agent was not prespecified, the value of AGOCCUR should be null. AGPRESP and AGOCCUR are permissible fields and may be omitted from the dataset if all agents were collected as free text. Values of AGOCCUR may also be null for prespecified agents if no Y/N response was collected; in this case, AGSTAT = "NOT DONE", and AGREASND could be used to describe the reason the answer was missing.

5. Any identifier variables, timing variables, or interventions general observation-class qualifiers may be added to the AG domain.
   a. However, --INDC, although allowed, would not generally be used because substance administrations represented in AG are given as part of a testing procedure rather than with therapeutic intent.
   b. The variables --DOSTOT and --DOSRGM, although allowed, would generally not be used because procedure agents are likely to be recorded at the level of single administrations.

<!-- source: knowledge_base/domains/BE/spec.md -->
# BE — Biospecimen Events

> Class: Events | Structure: One record per instance per biospecimen event per biospecimen identifier per subject

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
- **CDISC Notes:** Sponsor-defined identifier for a device.

### BESEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### BEGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### BEREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Internal or external identifier for the specimen affected or created by the event.

### BESPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional sponsor-defined reference number. Example: Line number on a CRF page.

### BETERM
- **Order:** 9
- **Label:** Reported Term for the Biospecimen Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Topic variable for an event observation, which is the verbatim or pre-specified name of the event.

### BEMODIFY
- **Order:** 10
- **Label:** Modified Reported Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If the value for BETERM is modified for coding purposes, then the modified text is placed here.

### BEDECOD
- **Order:** 11
- **Label:** Dictionary-Derived Term
- **Type:** Char
- **Controlled Terms:** C124297
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary-derived text description of BETERM or BEMODIFY, if applicable.

### BECAT
- **Order:** 12
- **Label:** Category for Biospecimen Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Example: COLLECTION, PREPARATION, TRANSPORT.

### BESCAT
- **Order:** 13
- **Label:** Subcategory for Biospecimen Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of BECAT values.

### BELOC
- **Order:** 14
- **Label:** Anatomical Location of Event
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the anatomical location relevant for the event (e.g. BRAIN, LUNG).

### BEPARTY
- **Order:** 15
- **Label:** Accountable Party
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Party accountable for the transferable object (e.g. specimen) as a result of the activity performed in the associated BETERM variable. The party could be an individual (e.g., subject), an organization (e.g., sponsor), or a location that is a proxy for an individual or organization (e.g., site). It is usually a somewhat general term that is further identified in the BEPRTYID variable.

### BEPRTYID
- **Order:** 16
- **Label:** Identification of Accountable Party
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identification of the specific party accountable for the transferable object (e.g. Specimen) after the action in BETERM is taken. Used in conjunction with BEPARTY.

### VISITNUM
- **Order:** 17
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 18
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter.

### VISITDY
- **Order:** 19
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### BEDTC
- **Order:** 20
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of specimen collection.

### BESTDTC
- **Order:** 21
- **Label:** Start Date/Time of Biospecimen Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of the event.

### BEENDTC
- **Order:** 22
- **Label:** End Date/Time of Biospecimen Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time of the event.

### BESTDY
- **Order:** 23
- **Label:** Study Day of Start of Biospecimen Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### BEENDY
- **Order:** 24
- **Label:** Study Day of End of Biospecimen Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### BEDUR
- **Order:** 25
- **Label:** Duration of Biospecimen Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration and unit of a biospecimen event. Used only if collected on the CRF and not derived from start and end date/times. Example: P1DT2H (for 1 day, 2 hours).
---

## Cross References

### Controlled Terminology
- [Biospecimen Events Dictionary Derived Term (C124297)](../../terminology/core/other_part1.md) — BEDECOD
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — BELOC

### Related Domains
- **Same class (Events):** AE, CE, DS, DV, HO, MH
- **Specimen:** [BS](../BS/) — biospecimen data for the event

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Events class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/BE/assumptions.md -->
# BE — Assumptions

1. The BE domain contains data about actions taken that affect or may affect a specimen, such as specimen collection, freezing and thawing, aliquoting, and transportation. This domain is intended to be applicable to any specimen tracking data, regardless of the reason for specimen collection.

2. The value in BEREFID identifies the specimen most affected by the event. For aliquoting, this would be the child specimen(s) created by the event, rather than the parent specimen. BEREFID should not contain any identifiers other than specimen IDs.

3. BELOC holds the relevant anatomic location of the subject, so it should only be populated when the subject participates in and is directly affected by the event given in BETERM.

4. BEPARTY and BEPRTYID together identify the individual or organization that takes responsibility for the biospecimen as a result of the action in BETERM. For example, if BETERM is COLLECTED, BEPARTY would be a general term defining the type of responsible party, such as SITE, and BEPRTYID would contain the site identifier, such as 02. If BEPARTY is sufficient to uniquely identify the party (such as SPONSOR in a single-sponsor study), then BEPRTYID may be null.

5. Usually BEPARTY and BEPRTYID refer to who has possession of the biospecimen after the action in BETERM. In the cases where a biospecimen is lost or destroyed for example, BEPARTY and BEPRTYID may be null.

6. Timing variables:
   a. BESTDTC and BEENDTC hold the start and end date/times for the event given in BETERM. If the end date/time is the same as the start date/time for the event, then BEENDTC is null.
   b. Unlike other Events domains, BEDTC does not hold the date/time of data collection. Instead, it holds the date/time of specimen collection, in alignment with the use of --DTC for specimen-related findings. BEDTC values for extracted or otherwise derived specimens are copied from that of the parent specimen.
   c. VISITNUM, VISIT, and VISITDY values for all records refer to the visit in which the originally collected specimen was collected.

7. The following variables generally would not be used in BE: dictionary coding variables (--LLT, --LLTCD, --PTCD, --HLT, --HLTCD, --HLGT, --HLGTCD), AE-specific variables (--SEV, --SER, --ACN, --ACNOTH, --ACNDEV, --REL, --RELNST, --PATT, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --CONTRT), toxicity variables (--TOX, --TOXGR).

<!-- source: knowledge_base/domains/BS/spec.md -->
# BS — Biospecimen Findings

> Class: Findings | Structure: One record per measurement per biospecimen identifier per subject

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
- **CDISC Notes:** Sponsor-defined identifier for a device.

### BSSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### BSGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### BSREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Internal or external identifier such as lab specimen ID.

### BSSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### BSTESTCD
- **Order:** 9
- **Label:** Biospecimen Test Short Name
- **Type:** Char
- **Controlled Terms:** C124300
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for BSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: VOLUME, RIN.

### BSTEST
- **Order:** 10
- **Label:** Biospecimen Test Name
- **Type:** Char
- **Controlled Terms:** C124299
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for BSTESTCD. Examples: Volume, RNA Integrity Number.

### BSCAT
- **Order:** 11
- **Label:** Category for Biospecimen Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of topic-variable values. Example: MEASUREMENT, QUALITY.

### BSSCAT
- **Order:** 12
- **Label:** Subcategory for Biospecimen Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of BSCAT values.

### BSORRES
- **Order:** 13
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### BSORRESU
- **Order:** 14
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Unit for BSORRES. Examples: mg, mL.

### BSSTRESC
- **Order:** 15
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from BSORRES in a standard format or standard units. BSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in BSSTRESN.

### BSSTRESN
- **Order:** 16
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from BSSTRESC. BSSTRESN should store all numeric test results or findings.

### BSSTRESU
- **Order:** 17
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for BSSTRESC and BSSTRESN.

### BSSTAT
- **Order:** 18
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a test was not done, or was attempted but did not generate a result. Should be null or have a value of NOT DONE.

### BSREASND
- **Order:** 19
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with BSSTAT when value is NOT DONE.

### BSNAM
- **Order:** 20
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor (e.g., laboratory) that provided the test results.

### BSSPEC
- **Order:** 21
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734; C111114
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: SERUM, PLASMA, URINE, SOFT TISSUE.

### BSANTREG
- **Order:** 22
- **Label:** Anatomical Region of Specimen
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the specific anatomical or biological region of a tissue, organ specimen or the region from which the specimen is obtained, as defined in the protocol, such as a section or part of what is described in the BSSPEC variable. Examples: CORTEX, MEDULLA, MUCOSA.

### BSSPCCND
- **Order:** 23
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the condition of the specimen. Examples: HEMOLYZED, ICTERIC, LIPEMIC.

### BSMETHOD
- **Order:** 24
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: SPECTROPHOTOMETRY, ELECTROPHORESIS.

### BSBLFL
- **Order:** 25
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value.

### VISITNUM
- **Order:** 26
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 27
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter.

### VISITDY
- **Order:** 28
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### BSDTC
- **Order:** 29
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of specimen collection.

### BSDY
- **Order:** 30
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection relative to the sponsor-defined RFSTDTC.

### BSTPT
- **Order:** 31
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See BSTPTNUM and BSTPTREF.

### BSTPTNUM
- **Order:** 32
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of BSTPT used in sorting.

### BSELTM
- **Order:** 33
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Elapsed time relative to a planned fixed reference (BSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration.

### BSTPTREF
- **Order:** 34
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by BSELTM, BSTPTNUM, and BSTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL.

### BSRFTDTC
- **Order:** 35
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by BSTPTREF.
---

## Cross References

### Controlled Terminology
- [Genetic Sample Type (C111114)](../../terminology/core/general_part2.md) — BSSPEC
- [Biospecimen Characteristics Test Name (C124299)](../../terminology/core/other_part1.md) — BSTEST
- [Biospecimen Characteristics Test Code (C124300)](../../terminology/core/other_part1.md) — BSTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — BSBLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — BSSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — BSORRESU, BSSTRESU
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — BSSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — BSSPEC
- [Method (C85492)](../../terminology/core/general_part3.md) — BSMETHOD

### Related Domains
- **Same class (Findings):** CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Event:** [BE](../BE/) — biospecimen events
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/BS/assumptions.md -->
# BS — Assumptions

1. The BS domain is used to store findings related to specimen handling and specimen characteristics such as type, amount, or size. BS is not restricted to PGx-related specimens.

2. For biospecimens of genetic material, BSSPEC values are drawn from the GENSMP (C111114) codelist.

3. Non-genetic BSSPEC values are drawn from the SPEC (C77529) codelist, which is part of the SEND terminology listing. BSANTREG is used to further define BSSPEC when it is desirable to identify a specific region within an organ.

4. To adapt BS for use with the SDTMIG, use the SPECTYPE (C78734) codelist in BSSPEC, add --LOC, --LAT, --DIR, and --PORTOT as applicable, and remove BSANTREG. Values that would otherwise have gone in BSANTREG may be placed in a supplemental qualifier that is almost identical to that variable, but which further qualifies BSLOC instead of BSSPEC.

5. The following variables generally would not be used in BS: --POS, --ORNLO, --ORNHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --LEAD, --CSTATE, --ACPTFL, --FAST, --TOX, --TOXGR, --SEV, --DTHREL.

<!-- source: knowledge_base/domains/CE/spec.md -->
# CE — Clinical Events

> Class: Events | Structure: One record per event per subject

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

### CESEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### CEGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records for a subject within a domain.

### CEREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or medical image).

### CESPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### CETERM
- **Order:** 8
- **Label:** Reported Term for the Clinical Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Term for the medical condition or event. Most likely preprinted on CRF.

### CEDECOD
- **Order:** 9
- **Label:** Dictionary-Derived Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Controlled terminology for the name of the clinical event. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

### CECAT
- **Order:** 10
- **Label:** Category for the Clinical Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records.

### CESCAT
- **Order:** 11
- **Label:** Subcategory for the Clinical Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the condition or event.

### CEPRESP
- **Order:** 12
- **Label:** Clinical Event Pre-specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether the event in CETERM was prespecified. Value is "Y" for prespecified events and null for spontaneously reported events.

### CEOCCUR
- **Order:** 13
- **Label:** Clinical Event Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when the occurrence of specific events is solicited, to indicate whether or not a clinical event occurred. Values are null for spontaneously reported events.

### CESTAT
- **Order:** 14
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The status indicates that a question from a prespecified list was not answered.

### CEREASND
- **Order:** 15
- **Label:** Reason Clinical Event Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason clinical event data was not collected. Used in conjunction with CESTAT when value is "NOT DONE".

### CEBODSYS
- **Order:** 16
- **Label:** Body System or Organ Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary-derived. Body system or organ class that is involved in an event or measurement from a standard hierarchy (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables, which may not necessarily be the primary SOC.

### CESEV
- **Order:** 17
- **Label:** Severity/Intensity
- **Type:** Char
- **Controlled Terms:** C165643
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The severity or intensity of the event. Examples: "MILD", "MODERATE", "SEVERE".

### CETOXGR
- **Order:** 18
- **Label:** Standard Toxicity Grade
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Toxicity grade according to a standard toxicity scale (e.g., Common Terminology Criteria for Adverse Events (CTCAE) v3.0). Sponsor should specify name of the scale and version used in the metadata. If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2").

### TAETORD
- **Order:** 19
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the clinical event started.

### EPOCH
- **Order:** 20
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the clinical event.

### CEDTC
- **Order:** 21
- **Label:** Date/Time of Event Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time for the clinical event observation represented in ISO 8601 character format.

### CESTDTC
- **Order:** 22
- **Label:** Start Date/Time of Clinical Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of the clinical event represented in ISO 8601 character format.

### CEENDTC
- **Order:** 23
- **Label:** End Date/Time of Clinical Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the clinical event, represented in ISO 8601 character format.

### CEDY
- **Order:** 24
- **Label:** Study Day of Event Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of clinical event collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.

### CESTDY
- **Order:** 25
- **Label:** Study Day of Start of Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of start of the clinical event expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### CEENDY
- **Order:** 26
- **Label:** Study Day of End of Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of the clinical event expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### CESTRF
- **Order:** 27
- **Label:** Start Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the start of the clinical event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics).  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CEENRF
- **Order:** 28
- **Label:** End Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics).  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CESTRTPT
- **Order:** 29
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the observation as being before or after the reference time point defined by variable CESTTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CESTTPT
- **Order:** 30
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by --STRTPT. Examples: "2003-12-15", "VISIT 1".

### CEENRTPT
- **Order:** 31
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable CEENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### CEENTPT
- **Order:** 32
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by CEENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Severity Response (C165643)](../../terminology/core/other_part4.md) — CESEV
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — CESTRF, CEENRF, CESTRTPT, CEENRTPT
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — CEPRESP, CEOCCUR
- [Not Done (C66789)](../../terminology/core/general_part4.md) — CESTAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Events):** AE, BE, DS, DV, HO, MH

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Events class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/CE/assumptions.md -->
# CE — Assumptions

1. The determination of events to be considered clinical events versus adverse events should be done carefully and with reference to regulatory guidelines or consultation with a regulatory review division. Events of clinical interest as defined by the protocol that are not considered AEs should be reflected as CEs.
   a. Events considered to be clinical events may include episodes of symptoms of the disease under study (often known as "signs and symptoms"), or events that do not constitute adverse events in themselves, though they might lead to the identification of an adverse event. For example, in a study of an investigational treatment for migraine headaches, migraine headaches may not be considered to be adverse events per protocol. The occurrence of migraines or associated signs and symptoms might be reported in CE.
   b. In vaccine trials, certain adverse events may be considered to be signs or symptoms and accordingly determined to be clinical events. If any event is considered serious, then the serious variable (--SER) and the serious adverse event flags (--SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE) would be required in the CE domain.
   c. Other studies might track the occurrence of specific events as efficacy endpoints. For example, in a study of an investigational treatment for prevention of ischemic stroke, all occurrences of TIA, stroke, and death might be captured as clinical events and assessed as to whether they meet endpoint criteria. Note that other information about these events may be reported in other datasets. For example, the event leading to death would also be reported as a reason for study discontinuation in the Disposition (DS) domain.

2. CEOCCUR and CEPRESP are used together to indicate whether the event in CETERM was prespecified and whether it occurred. CEPRESP can be used to separate records that correspond to probing questions for prespecified events from those that represent spontaneously reported events, whereas CEOCCUR contains the responses to such questions. The following table shows how these variables are populated in various situations.

   | Situation | Value of CEPRESP | Value of CEOCCUR | Value of CESTAT |
   |-----------|-----------------|-----------------|----------------|
   | Spontaneously reported event occurrence | | | |
   | Prespecified event occurred | Y | Y | |
   | Prespecified event did not occur | Y | N | |
   | Prespecified event has no response | Y | | NOT DONE |

3. The collection of write-in events on a CE CRF should be considered with caution. Sponsors must ensure that all adverse events are recorded in the AE domain.

4. Any identifier variable may be added to the CE domain.

5. Timing variables
   a. Relative timing assessments "Prior" or "Ongoing" are common in the collection of CE information. CESTRF or CEENRF may be used when this timing assessment is relative to the study reference period for the subject represented in the Demographics (DM) dataset (RFENDTC). CESTRTPT with CESTTPT and/or CEENRTPT with CEENTPT may be used when "Prior" or "Ongoing" are relative to specific dates other than the start and end of the study reference period. See Section 4.4.7, Use of Relative Timing Variables.
   b. Additional timing variables may be used when appropriate.

6. The clinical events domain is based on the Events general observation class and thus can use any variables in the Events class, including those found in the AE domain specification table.

<!-- source: knowledge_base/domains/CM/spec.md -->
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

<!-- source: knowledge_base/domains/CM/assumptions.md -->
# CM — Assumptions

1. The structure of the CM domain is 1 record per medication intervention episode, constant-dosing interval, or prespecified medication assessment per subject. It is the sponsor's responsibility to define an intervention episode. This definition may vary based on the sponsor's requirements for review and analysis. The submission dataset structure may differ from the structure used for collection. One common approach is to submit a new record when there is a change in the dosing regimen. Another approach is to collapse all records for a medication to a summary level with either a dose range or the highest dose level. Other approaches may also be reasonable as long as they meet the sponsor's evaluation requirements.

2. CM description and coding
   a. CMTRT is the topic variable and captures the name of the concomitant medication/therapy or the prespecified term used to collect information about the occurrence of any of a group of medications and/or therapies. It is a required variable and must have a value. CMTRT only includes the medication/therapy name and does not include dosage, formulation, or other qualifying information. For example, "ASPIRIN 100MG TABLET" is not a valid value for CMTRT. This example should be expressed as CMTRT= "ASPIRIN", CMDOSE= "100", CMDOSU= "MG", and CMDOSFRM= "TABLET". When referring to a prespecified group of medications/therapies, CMTRT contains the description of the group used to solicit the occurrence response.
   b. CMMODIFY should be included if the sponsor's procedure permits modification of a verbatim term for coding.
   c. CMDECOD is the standardized medication/therapy term derived by the sponsor from the coding dictionary. It is expected that the reported term (CMTRT) or the modified term (CMMODIFY) will be coded using a standard dictionary. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. If an intervention term does not have a decode value in the dictionary, then CMDECOD will be left blank.
   d. When CMDECOD values from the WHODrug Dictionary are longer than 200 characters, split the values at semicolons rather than spaces when implementing guidance in Section 4.5.3.2, Text Strings Greater than 200 Characters.

3. Prespecified terms; presence or absence of concomitant medications
   a. Information on concomitant medications is generally collected in 2 different ways, either by recording free text or using a prespecified list of terms. Because the solicitation of information on specific concomitant medications may affect the frequency at which they are reported, the fact that a specific medication was solicited may be of interest to reviewers. CMPRESP and CMOCCUR are used together to indicate the intervention in CMTRT was prespecified and whether it occurred, respectively.
   b. CMOCCUR is used to indicate whether a prespecified medication was used. A value of "Y" indicates that the medication was used and "N" indicates that it was not.
   c. If a medication was not prespecified, the value of CMOCCUR should be null. CMPRESP and CMOCCUR are permissible fields and may be omitted from the dataset if all medications were collected as free text. Values of CMOCCUR may also be null for prespecified medications if no Y/N response was collected; in such cases, CMSTAT = "NOT DONE", and CMREASND could be used to describe the reason the answer was missing.

4. Variables for timing relative to a time point
   a. CMSTRTPT, CMSTTPT, CMENRTPT, and CMENTPT may be populated as necessary to indicate when a medication was used relative to specified time points. For example, assume a subject uses birth control medication. The subject has used the same medication for many years and continues to do so. The date the subject began using the medication (or at least a partial date) would be stored in CMSTDTC. CMENDTC is null because the end date is unknown/has not yet happened. This fact can be recorded by setting CMENTPT = "2007-04-30" (the date the assessment was made) and CMENRTPT = "ONGOING".

5. Although any identifier, timing variables, or interventions general observation-class qualifiers may be added to the CM domain, the following qualifiers would generally not be used: --MOOD, --LOT.

<!-- source: knowledge_base/domains/CO/spec.md -->
# CO — Comments

> Class: Special-Purpose | Structure: One record per comment per subject

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

### RDOMAIN
- **Order:** 3
- **Label:** Related Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** C66734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Two-character abbreviation for the domain of the parent record(s). Null for comments collected on a general comments or additional information CRF page.

### USUBJID
- **Order:** 4
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### COSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence Number given to ensure uniqueness of subject records within a domain. May be any valid number.

### IDVAR
- **Order:** 6
- **Label:** Identifying Variable
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifying variable in the parent dataset that identifies the record(s) to which the comment applies. Examples AESEQ or CMGRPID. Used only when individual comments are related to domain records. Null for comments collected on separate CRFs.

### IDVARVAL
- **Order:** 7
- **Label:** Identifying Variable Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Value of identifying variable of the parent record(s). Used only when individual comments are related to domain records. Null for comments collected on separate CRFs.

### COREF
- **Order:** 8
- **Label:** Comment Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference associated with the comment. May be the CRF page number (e.g., 650), or a module name (e.g., DEMOG), or a combination of information that identifies the reference (e.g. 650-VITALS-VISIT 2).

### COVAL
- **Order:** 9
- **Label:** Comment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** The text of the comment. Text over 200 characters can be added to additional columns COVAL1-COVALn. See Assumption 3.

### COEVAL
- **Order:** 10
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Example: "INVESTIGATOR".

### COEVALID
- **Order:** 11
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST", "RADIOLOGIST 1", "RADIOLOGIST 2".

### CODTC
- **Order:** 12
- **Label:** Date/Time of Comment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of comment on dedicated comment form. Should be null if this is a child record of another domain or if comment date was not collected.

### CODY
- **Order:** 13
- **Label:** Study Day of Comment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the comment, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.
---

## Cross References

### Controlled Terminology
- [SDTM Domain Abbreviation (C66734)](../../terminology/core/general_part4.md) — RDOMAIN
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — COEVAL
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — COEVALID

### Related Domains
- **Same class (Special-Purpose):** DM, SE, SM, SV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)

<!-- source: knowledge_base/domains/CO/assumptions.md -->
# CO — Assumptions

1. The Comments special-purpose domain provides a solution for submitting free-text comments related to data in 1 or more SDTM domains (as described in Section 8.5, Relating Comments to a Parent Domain) or collected on a separate CRF page dedicated to comments. Comments are generally not responses to specific questions; instead, comments usually consist of voluntary free-text or unsolicited observations.

2. Although the structure for the Comments domain in the SDTM is "One record per comment", USUBJID is required in the comments domain for human clinical trials, so the structure of the Comments domain in the SDTMIG is "One record per comment per subject."

3. The CO dataset accommodates 3 sources of comments:
   a. Those unrelated to a specific domain or parent record(s), in which case the values of the variables RDOMAIN, IDVAR, and IDVARVAL are null. CODTC should be populated if captured. See Example 1, row 1.
   b. Those related to a domain but not to specific parent record(s), in which case the value of the variable RDOMAIN is set to the DOMAIN code of the parent domain and the variables IDVAR and IDVARVAL are null. CODTC should be populated if captured. See Example 1, row 2.
   c. Those related to a specific parent record or group of parent records, in which case the value of the variable RDOMAIN is set to the DOMAIN code of the parent record(s) and the variables IDVAR and IDVARVAL are populated with the key variable name and value of the parent record(s). Assumptions for populating IDVAR and IDVARVAL are further described in Section 8.5, Relating Comments to a Parent Domain. CODTC should be null because the timing of the parent record(s) is inherited by the comment record. See Example 1, rows 3-5.

4. When the comment text is longer than 200 characters, the first 200 characters of the comment will be in COVAL, the next 200 in COVAL1, and additional text stored as needed to COVALn. See Example 1, rows 3-4. Additional information about how to relate comments to parent SDTM records is provided in Section 8.5, Relating Comments to a Parent Domain.

5. The variable COREF may be null unless it is used to identify the source of the comment. See Example 1, rows 1 and 5.

6. Identifier variables and Timing variables may be added to the CO domain, but the following qualifiers would generally not be used in CO: --GRPID, --REFID, --SPID, TAETORD, --TPT, --TPTNUM, --ELTM, --TPTREF, --RFTDTC.

<!-- source: knowledge_base/domains/CP/spec.md -->
# CP — Cell Phenotype Findings

> Class: Findings | Structure: One record per test per specimen per timepoint per visit per subject

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

### CPSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of subject records within a domain. May be any valid number.

### CPGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### CPREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier.

### CPSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the lab page.

### CPLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### CPLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### CPTESTCD
- **Order:** 10
- **Label:** Test or Examination Short Name
- **Type:** Char
- **Controlled Terms:** C181173
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in CPTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). CPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MONO", "MNS".

### CPTEST
- **Order:** 11
- **Label:** Name of Measurement, Test or Examination
- **Type:** Char
- **Controlled Terms:** C181174
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for CPTESTCD. For cell phenotyping, the name (often abbreviated) of the cell population, as it is generally accepted by the scientific community, is populated (rather than a colloquial designation based on a primary marker, e.g., TLym Help rather than CD4). When the test is for a sublineage which can only be identified by specifying additional markers (i.e., has not been given a name) or which is further restricted to a subpopulation based on a particular cell state (e.g., activated, proliferating, apoptotic), the Sublineage Marker String (CPSBMRKS), Cell State (CPCELSTA), and Cell State Marker String (CPCSMRKS) variables are additionally populated and the value in CPTEST is suffixed with "Sub" to denote that it is a subset of the population identified in CPTEST (e.g., Monocytes Sub).  The value in CPTEST cannot be longer than 40 characters.

### CPSBMRKS
- **Order:** 12
- **Label:** Sublineage Marker String
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to further subset the cell population identified in CPTEST based on the use of additional marker(s) that define a sublineage. The value in CPSBMRKS is used in combination with values in CPTEST and CPCELSTA to fully describe the cell population being measured. As such, it is an essential component of the full test name.  For example, three unnamed sublineages of monocytes have been identified as: CCR2+CD16-, CCR2-CD16+, and CCR2+CD16+. Whereas the entire monocyte cell population can be defined as CD14+ cells, the additional CCR2 and CD16 markers are used to differentiate one sublineage from another. As none of these sublineages have been given names, they are only known by the CCR2 and CD16 marker combinations. By associating the CPTEST value of "Monocytes Sub" with, for example, a value of "CCR2+CD16-" in CPSBMRKS, the full test is defined to be the CCR2+CD16- monocyte subpopulation.

### CPCELSTA
- **Order:** 13
- **Label:** Cell State
- **Type:** Char
- **Controlled Terms:** C181172
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A textual description of a subset of the cell population identified in CPTEST based on a particular functional and/or biological state (e.g., "ACTIVATED", "PROLIFERATING", "SENESCENT"). When populated, the values in CPCELSTA and CPSMRKS, in combination with the values in CPTEST and CPSBMRKS, fully describe the cell population being measured.

### CPCSMRKS
- **Order:** 14
- **Label:** Cell State Marker String
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies the marker(s) or indicator(s) used to define the cell state (i.e., the value in CPCELSTA).  For example, when Ki67 expression is used to determine that a cell population is in a proliferating state (i.e., CPCELSTA value="PROLIFERATING"), the value "Ki67+" in CPCSMRKS indicates that positive expression of Ki67 was used to define the population as proliferating. Similarly, a value of "Ki67-" in CPCSMRKS would indicate that lack of expression of Ki67 defined the "NON-PROLIFERATING" cell state in CPCELSTA. The CPCSMRKS value is useful for quickly determining which marker(s) were used to classify (i.e., operationally define) a cell population based on a functional/biological state.

### CPTSTCND
- **Order:** 15
- **Label:** Test Condition
- **Type:** Char
- **Controlled Terms:** C181175
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed. --TSTCND is generally used to distinguish between two or more records where the same assay is performed under varying (as opposed to fixed) conditions, usually for the purpose of making a comparison. For example, when the same assay (identified in --TEST) is performed under stimulated and non-stimulated conditions, the --TSTCND variable is used distinguish between the records.

### CPCNDAGT
- **Order:** 16
- **Label:** Test Condition Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent, if applicable, used to impose the condition identified in CPTSTCND. For example, records might be produced for the same assay run under stimulating (CPTSTCND value = "STIMULATED") conditions produced by different stimulating agents (e.g., phorbol myristate acetate, concanavalin A, PHA-P, TNF-alpha, Ionomycin, candida antigen).

### CPBDAGNT
- **Order:** 17
- **Label:** Binding Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent that is binding to the entity in the CPTEST variable. The CPBDAGNT variable is used to indicate that there is a binding relationship between the entities in the CPTEST and CPBDAGNT variables, regardless of direction.  The binding agent may be, but is not limited to, a test article; a portion of a test article; a substance related to a test article; an endogenous molecule; an allergen; an infectious agent; or a reagent (e.g., primary antibody) that confers the binding specificity for the measurement defined in CPTEST when it is needed to uniquely identify the test.

### CPABCLID
- **Order:** 18
- **Label:** Antibody Clone Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies the antibody clone (e.g., supplier-provided catalog name) used to confer specificity for the binding agent specified in CPBDAGNT.

### CPMRKSTR
- **Order:** 19
- **Label:** Marker String
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** The text string identifying the full set of markers/indicators used by the laboratory to operationally define the complete test based on the combination of CPTEST, CPSBMRKS, and CPCELSTA. Because laboratories often use different markers/indicators to identify a cell population, the relationship between a named cell population in CPTEST (as combined with CPSBMRKS and CPCELSTA values) and the set of markers used to identify that population is many-to-one. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different sets of markers, it is necessary to operationally define the test in terms of the complete set of markers/indicators used to perform that test.

### CPGATE
- **Order:** 20
- **Label:** Gate
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The sponsor-defined name assigned to a gate. Gates are electronic (i.e., a device setting or software-defined) boundaries set by a user to virtually parse a specimen into discrete populations based on a set of defined characteristics (e.g., presence, absence, or intensity of expression of various markers; physical size; internal complexity or granularity). Gates are used to constrain data collection or analysis to a specific cell population or region of interest within the specimen.

### CPGATDEF
- **Order:** 21
- **Label:** Gate Definition
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The text string identifying the set of parameters and the order in which they are applied to define the gating strategy. In practice, a series of 2-dimensional sub-gates based on different cell characteristics (i.e., markers/indicators/physical properties) are most often combined until the cell population of interest is sufficiently resolved (i.e., electronically isolated) from other cell populations contained within the specimen.  For complex analyses, differences in gating strategies can produce subtle differences in results obtained for a test. To ensure nuances important for accurately interpreting the data are accounted for and which arise from the use of different gating strategies, it is often necessary to qualify the test in terms of the gating strategy. For some purposes, however, and at the discretion of the sponsor, only the ultimate or penultimate gate is identified. When specifying the gating strategy in CPGATDEF, each sub-gate should be listed in the order it was applied and separated from the next sub-gate using the pipe/vertical line ("|") character.

### CPSPTSTD
- **Order:** 22
- **Label:** Sponsor Test Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Sponsor's description of a test. The variable is intended to contain highly structured test description metadata used by a sponsor to unambiguously define (label) a test. Such values generally reside in a sponsor/laboratory test metadata repository. CPSPTSTD is not intended for unstructured (spontaneous) free text.  An example of appropriate usage is when it is necessary to include identifying information for a target cell population on which a test is conducted when the target population is not part of the test name, e.g., tests for quantitative expression of a particular marker on a specific cell population.

### CPCAT
- **Order:** 23
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** C181171
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values across subjects. Examples: "IMMUNOPHENOTYPING", "CELL FUNCTION", "TARGET ENGAGEMENT".

### CPSCAT
- **Order:** 24
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of CPCAT.

### CPTSTPNL
- **Order:** 25
- **Label:** Test Panel
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined textual description used to group tests run together as part of a test panel. Can be used with --GRPID to ensure that relationships between associated tests are accurately identified.

### CPORRES
- **Order:** 26
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### CPORRESU
- **Order:** 27
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for CPORRES. Examples: "10^6/L", "%", "MESF".

### CPRESSCL
- **Order:** 28
- **Label:** Result Scale
- **Type:** Char
- **Controlled Terms:** C177910
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the scale of the original result value with respect to whether the result is quantitative, ordinal, nominal, or narrative.

### CPRESTYP
- **Order:** 29
- **Label:** Result Type
- **Type:** Char
- **Controlled Terms:** C179588
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the kind of result (i.e., property type) originally reported for the test. Examples: "NUMBER CONCENTRATION", "NUMBER FRACTION", "RATIO".

### CPCOLSRT
- **Order:** 30
- **Label:** Collected Summary Result Type
- **Type:** Char
- **Controlled Terms:** C177908
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the type of collected summary result. This includes source summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived using individual source data records, this summary result should be represented in ADaM. If a sponsor has both a collected summary result and a derived summary result, the collected summary result should be represented in SDTM and the derived summary result should be represented in ADaM.

### CPORNRLO
- **Order:** 31
- **Label:** Reference Range Lower Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### CPORNRHI
- **Order:** 32
- **Label:** Reference Range Upper Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### CPSTRESC
- **Order:** 33
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from CPORRES in a standard format or in standard units. CPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CPSTRESN.

### CPSTRESN
- **Order:** 34
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from CPSTRESC. CPSTRESN should store all numeric test results or findings.

### CPSTRESU
- **Order:** 35
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for CPSTRESC or CPSTRESN.

### CPSTNRLO
- **Order:** 36
- **Label:** Reference Range Lower Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of reference range for continuous measurements for CPSTRESC/CPSTRESN in standardized units. Should be populated only for continuous results.

### CPSTNRHI
- **Order:** 37
- **Label:** Reference Range Upper Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.

### CPNRIND
- **Order:** 38
- **Label:** Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates where the value falls with respect to reference range defined by CPORNRLO and CPORNRHI, CPSTNRLO and CPSTNRHI, or by CPSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether CPNRIND refers to the original or standard reference ranges and results. CPNRIND should not be used to indicate clinical significance.

### CPSTAT
- **Order:** 39
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that the test was not performed or that it was attempted but did not generate a result. Should be null if a result exists in CPORRES.

### CPREASND
- **Order:** 40
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a test was not performed, e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED", "SPECIMEN LOST". Used in conjunction with CPSTAT when value is "NOT DONE".

### CPNAM
- **Order:** 41
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the laboratory that performed the test.

### CPLOINC
- **Order:** 42
- **Label:** LOINC Code
- **Type:** Char
- **Controlled Terms:** LOINC
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Code for the test from the LOINC code system. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the Define-XML external codelist attributes.

### CPSPEC
- **Order:** 43
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "BLOOD", "BONE MARROW".

### CPSPCCND
- **Order:** 44
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The physical state or quality of a specimen for an assessment. Example: "CLOTTED".

### CPMETHOD
- **Order:** 45
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Example: "FLOW CYTOMETRY".

### CPANMETH
- **Order:** 46
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result.

### CPLOBXFL
- **Order:** 47
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### CPBLFL
- **Order:** 48
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null.

### CPDRVFL
- **Order:** 49
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or do not come from the CRF, or are not as originally received or collected are examples of records that might be derived for the submission datasets. If CPDRVFL = "Y", then CPORRES may be null, with CPSTRESC and (if numeric) CPSTRESN having the derived value.

### CPCLSIG
- **Order:** 50
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgement.

### VISITNUM
- **Order:** 51
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 52
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 53
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer.

### TAETORD
- **Order:** 54
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 55
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### CPDTC
- **Order:** 56
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection represented in ISO 8601 character format.

### CPDY
- **Order:** 57
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC value in Demographics.

### CPTPT
- **Order:** 58
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a specimen is to be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF). Example: "1 hour post".

### CPTPTNUM
- **Order:** 59
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of CPTPT to aid in sorting. When CPTPT is represented as an elapsed time relative to a fixed reference point (i.e., to the value in CPTPTREF), the values in CPTPTNUM should be assigned in ascending order relative to the value in CPTPTREF. For example, records for time points where CPTPT = "5 minutes post", 1 hour post", and "4 hours post" could be represented in CPTPTNUM as "1", "2", and "3", which maintains the order between CPTPT and CPTPTNUM with respect to the fixed time point reference in CPTPTREF.

### CPELTM
- **Order:** 60
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to the planned fixed reference value in CPTPTREF, represented in ISO 8601 duration format. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by CPTPTREF, "T8H" to represent 8 hours after the reference time point represented by CPTPTREF.

### CPTPTREF
- **Order:** 61
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Descriptive name of the fixed reference point referred to by CPTPT, CPTPTNUM, and CPELTM. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### CPRFTDTC
- **Order:** 62
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by CPTPTREF.
---

## Cross References

### Controlled Terminology
- [Collected Summarized Value Type Response (C177908)](../../terminology/core/general_part2.md) — CPCOLSRT
- [Result Scale Response (C177910)](../../terminology/core/general_part4.md) — CPRESSCL
- [Result Type Response (C179588)](../../terminology/core/general_part4.md) — CPRESTYP
- [Category for Cell Phenotyping (C181171)](../../terminology/core/cp_part1.md) — CPCAT
- [Cell State Response (C181172)](../../terminology/core/cp_part2.md) — CPCELSTA
- [Cell Phenotyping Test Code (C181173)](../../terminology/core/cp_part1.md) — CPTESTCD
- [Cell Phenotyping Test Name (C181174)](../../terminology/core/cp_part2.md) — CPTEST
- [Test Condition Response (C181175)](../../terminology/core/general_part4.md) — CPTSTCND
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — CPLOBXFL, CPBLFL, CPDRVFL, CPCLSIG
- [Not Done (C66789)](../../terminology/core/general_part4.md) — CPSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — CPORRESU, CPSTRESU
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — CPSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — CPSPEC
- [Reference Range Indicator (C78736)](../../terminology/core/general_part4.md) — CPNRIND
- [Method (C85492)](../../terminology/core/general_part3.md) — CPMETHOD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Related Findings:** [LB](../LB/) — cardiac electrophysiology vs lab tests

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/CP/assumptions.md -->
# CP — Assumptions

1. The Cell Phenotype domain captures cell phenotyping and related data based on cell expression markers and other indicators (e.g., stains/dyes) in disseminated tissue specimens and cell suspensions.

2. The CP domain is only used for tests which include a phenotyping component that relies on using cell markers to identify a specific population of cells (e.g., quantitative cell phenotyping), or on which the test is conducted (e.g., quantitative single marker expression, target/receptor occupancy). For example, a test which measures gamma-interferon expression in helper T lymphocytes defined as the CD45+CD3+CD4+CD8- population is an appropriate test for including in CP, whereas a test which measures gamma interferon secretion in an undefined "PBMC" (peripheral blood mononuclear cell) population is not appropriate.

3. A value which is calculated and reported by a lab according to its procedures is considered collected rather than derived; the Derived Flag (CPDRVFL) should be null for these results.

4. CPCELSTA is used in conjunction with CPCSMRKS. When CPCELSTA is populated, CPCSMRKS must also be populated. Conversely, when CPCSMRKS is populated, CPCELSTA must be populated.

5. The combination of values in CPTEST, CPSBMRKS, CPCELSTA, and CPCSMRKS are used to uniquely identify a test. When 1 or more of the variables CPSBMRKS, CPCELSTA, or CPCSMRKS are populated, the Test Name (CPTEST) must be populated with the test name variant containing the "Sub" suffix to indicate that the finding/result pertains to a subpopulation of the cell type named in CPTEST.

6. Populating the CPTEST and CPMRKSTR variables: The general structure of CPTEST and CPMRKSTR depends on the use case (e.g., immunophenotyping, quantitative marker expression, target/receptor occupancy), which is generally conveyed by the CPCAT and/or CPSCAT value(s). Currently, CP supports the following use cases for which guidance on CPTEST and CPMRKSTR values are given:
   a. Immunophenotyping
      i. CPTEST is populated with the name of the cell type being measured, not with the set of markers used to define the cell type.
      ii. It is expected that CPMRKSTR is populated, and that it contains the entire set of markers used to define the test, including those that are also present in CPSBMRKS and/or CPCSMRKS.
      iii. Marker strings follow, as closely as possible, formatting recommendations presented in assumption 8.
   b. Quantitative single-marker expression
      i. CPTEST begins with the identity of the marker (e.g., CD99), followed by the word "Expression" (e.g., "CD99 Expression").
      ii. It is expected that CPMRKSTR is populated, and that it starts by identifying the marker being quantified (e.g. "CD99"). This is followed by a delimiter (described below) and then the entire marker string used to define the cell population on which the marker is measured, including the marker being quantified, since it also defines the cell population.
      iii. The general form of the delimiter used to separate the marker being quantified from the cell population on which it is measured is "<space>xxxx<space>", where "xxxx" represents a character string used as delimiting text. It is recommended that the delimiting text is the abbreviation for the unit of measure used to report the level of expression of the quantified marker (e.g., "MESF", "MdFI"). An example which follows this guidance is: CPTEST = "CD99 Expression" and CPMRKSTR = "CD99 MESF CD45+CD3-CD19+CD99+", where "MESF" is the text delimiter and is followed by the entire marker string defining the cell population on which CD99 was measured, which includes the CD99 marker itself.
      iv. Marker strings follow, as closely as possible, formatting recommendations presented in assumption 8.
   c. Other use cases (e.g., target/receptor occupancy), refer to the examples section and to published Controlled Terminology supporting CP. In the case of target/receptor occupancy a more generalized test value is populated into CPTEST (e.g., "Total Bound") and the identity of the target/receptor is included in another variable, such as CPBNDAGT and/or CPTSTPNL (refer to examples). CDISC will continue to develop examples for other use cases as they are identified and modeled.

7. Specifying viability:
   a. Because the majority of cell phenotyping tests of interest are for viable cells, the word "Viable" is not generally included in the test name (CPTEST) and usually does not need to be explicitly stated in CPCELSTA. Because populating CPCELSTA and CSMRKS with viability information necessitates appending the "Sub" suffix to the value in CPTEST (assumption 5), it is recommended that CPCELSTA and CPCSMRKS generally not be used unless a selective viability stain was included in the test in order to differentiate the record for viable cells from record(s) for cells in a different vital state. For example, when viable cells are being compared to apoptotic and/or non-viable cells, it is necessary to differentiate those records using CPCELSTA and CPCSMRKS. In such cases where CPCELSTA and CPCSMRKS are populated, the "Sub" suffix is appended to the value in CPTEST (assumption 5).
   b. Viability marker(s) used to define a test are included in the full marker string in CPMRKSTR regardless of whether the viability status is stated explicitly in CPCELSTA. Moreover, if viability is explicitly stated in CPGATE, marker(s) used to designate viability are included in CPGATDEF. For example, if the value in CPGATE is "Lymphocytes, Viable" and 7AAD- was used to define the viable state, 7AAD- is included in CPGATDEF, in addition to being included in the complete marker string in CPMRKSTR.

8. Recommended formatting of marker string variables CPMRKSTR, CPSBMRKS, and CPCSMRKS: The marker string variables provide critical information for defining a test. Although there are no current plans to control their values through CDISC Controlled Terminology codelists, adherence to the following formatting guidelines helps to preclude ambiguities that can lead to uncertainty in uniquely understanding a test and its associated result.
   a. Marker strings do not contain delimiting characters (e.g., ",", space, "/", ")") to separate individual markers within the string, nor do they contain punctuation (e.g., hyphens) within individual markers, as these can be confused with symbols used to designate levels of expression and/or make it difficult to distinguish between the individual markers that comprise the string. For example, although the scientific literature often uses "HLA-DR", this is represented in CP marker strings as "HLADR".
   b. Forward slash "/" is only used to separate the portion of the marker string defining a numerator from the portion defining a denominator.
   c. When referring to a marker using the cluster of differentiation (CD) designation, "CD" should be included as part of the marker reference. For example, a marker string for helper T lymphocytes comprising CD45, CD3, CD4, and CD8 markers would be "CD45+CD3+CD4+CD8-" (rather than "45+3+4+8-").
   d. The order of markers within a string is consistent across similar tests, generally proceeding in the order that defines the cell hierarchy from highest to lowest, followed by additional non-lineage-defining markers, and ending with cell state and viability markers. This order maintains alignment with how a test is identified using the ordered combination of CPTEST, CPSMRKS, and CPCELSTA. For example, a test for proliferating viable activated central memory helper T-lymphocytes would be operationally defined in CPMRKSTR as similar to "CD45+CD3+CD19-CD4+CD8-CD197+CD45RA-CD278+Ki67+7AAD-", where the order of markers in the string is "CD45" (leukocyte), "CD3+CD19-" (T lymphocyte), "CD4+CD8-" (helper), "CD197+CD45RA-" (central memory), "CD278+" (activated), Ki67+ (proliferating), 7AAD- (viable). Corresponding to this marker-based definition of the test, and using the appropriate Controlled Terminology terms, CPTEST is "TLym Help Cen Mem Sub", CPCELSTA is "ACTIVATED; PROLIFERATING", and CPCSMRKS is "CD278+Ki67+". If the sponsor also chose to include the viability status as a cell state in addition to the activation and proliferative states, CPCELSTA would be similar to "ACTIVATED; PROLIFERATING; VIABLE" and the corresponding CPCSMRKS value would be "CD278+Ki67+7AAD-". In this example, the named cell population in CPTEST has not been further divided into an unnamed sublineage based on additional sublineage markers; therefore, CPSBMRKS is null.
   e. Forward (FSC) and Side (SSC) light scatter: These parameters are generally used to perform initial gating to exclude debris non-singlets and are often reapplied to differentiate cell subpopulations in the "inclusion" gate. However, FSC and SSC are often not included in marker string definitions as it is generally taken for granted that they were used. In contrast, they are usually included in a descriptions of a gating strategy, and would generally be included in CPGATDEF when the full gating strategy is shown. Labs/sponsors may choose whether to include FSC and SSC parameters in CPMRKSTR. It is recommended to include them when they are needed to differentiate one test from another. For example, because there is no universal expression marker specific for lymphocytes, FSC and SSC are used to define the lymphocyte subpopulation within a CD45+ leukocyte population. A test of "Lymphocytes/Leukocytes" defined only in terms of CD45 expression would not make sense as it would be "CD45+/CD45+". In this case, it makes sense to define lymphocytes as "CD45+SSClo" so that the value in CPMRKSTR is "CD45+SSClo/CD45+".
   f. Indicating the expression level of individual markers included in a marker string: A variety of formats are used in the scientific literature for indicating the level of expression of a marker on or within a cell. For example, after identifying a marker such as CD4, its level of expression might be represented as 1 of the following:
      i. neg, min, or - to denote the absence or minimal expression (e.g., CD4neg, CD4min, CD4-)
      ii. pos or + to denote that the marker is expressed (e.g., CD4pos, CD4+)
      iii. high, hi, or ++ to denote that the marker is expressed at a very high level relative to simply being "positive" (e.g., CD4high, CD4hi, CD4++)
      iv. other formats (e.g., -/low, -/lo, low, lo, mid, -/+, +++)
   g. Because categories for expression levels are subjective in the sense that they are relative to one another, various formats often overlap, which can create ambiguities. Some degree of consistency in formats used to represent relative expression levels is warranted to mitigate ambiguity, at least to the extent that relative expression levels used to define cell lineages/sublineages are similar across studies and laboratories in order to enable comparisons. Five designations are recommended for use in SDTM datasets:
      i. "-" (the marker is not expressed; at times, the use of "-lo" may be justified to indicate that the marker is either not expressed or is present in a negligible amount)
      ii. "lo" (the marker is expressed at a low level)
      iii. "mid" (the marker is expressed somewhere between a low and "normal" positive level for that cell type)
      iv. "+" (the marker is expressed at a normal positive level for that cell type)
      v. "hi" (the marker is expressed at a distinctly higher level than in cells that are "+", such that they are distinguishable from the "+" population and define their own subpopulation)
      vi. Although these designations are expected to be useful in the majority of cases, it is recognized that designations not listed here may be more appropriate in some cases. The data provider must determine the best way to designate an expression level suited to the purpose of the test, while striving to mitigate ambiguities resulting from lack of consistency of use.
   h. Explicitly indicating the cellular sublocation for a marker: In most cases, the location of a marker on or within a cell is not necessary; however, there are situations in which a marker can be expressed in more than a single cellular compartment and there is a need for the test to distinguish between marker expression in one compartment versus another. To accommodate this, using a lowercase letter in front of the marker is recommended. The cell sublocations are usually related to the cell surface (plasma membrane), cytoplasm, and nucleus. Use m, c, or n in front of the marker to denote "membrane", "cytoplasm", and "nucleus", respectively. An example of a marker often associated with a need to indicate cell location is CD152 (CTLA4), where cytoplasmic expression may define a test to distinguish it from whole cell expression. In this case, "cCD152" is used to denote that it is the cytoplasmic expression of CD152 that is measured for the test.

9. CPNRIND can be added to indicate where a result falls with respect to a reference range defined by CPORNRLO and CPORNRHI (e.g., "HIGH", "LOW").

10. The variable CPORRESU uses the UNIT codelist. This means that sponsors should be submitting a term from the CDISC Submission Value column in the published Controlled Terminology maintained for CDISC by NCI EVS. When sponsors have units that are not in this column, they should first check to see if their unit is mathematically synonymous with an existing unit and submit their lab values using that unit. If this is not the case, then a request for a new term (see https://ncitermform.nci.nih.gov/) should be submitted.

<!-- source: knowledge_base/domains/CV/spec.md -->
# CV — Cardiovascular System Findings

> Class: Findings | Structure: One record per finding or result per time point per visit per subject

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

### CVSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### CVGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### CVREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier.

### CVSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. Example: a preprinted line identifier on a CRF.

### CVLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### CVLNKGRP
- **Order:** 9
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### CVTESTCD
- **Order:** 10
- **Label:** Short Name of Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** C101847
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in CVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in CVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" would not be valid). CVTESTCD cannot contain characters other than letters, numbers, or underscores.

### CVTEST
- **Order:** 11
- **Label:** Name of Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** C101846
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name For CVTESTCD. The value in CVTEST cannot be longer than 40 characters.

### CVCAT
- **Order:** 12
- **Label:** Category for Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values.

### CVSCAT
- **Order:** 13
- **Label:** Subcategory for Cardiovascular Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of CVCAT values.

### CVPOS
- **Order:** 14
- **Label:** Position of Subject During Observation
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### CVORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### CVORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. Unit for CVORRES.

### CVSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived, from CVORRES in a standard format or in standard units. CVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in CVSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in CVORRES and these results effectively have the same meaning, they could be represented in standard format in CVSTRESC as "NEGATIVE".

### CVSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from CVSTRESC. CVSTRESN should store all numeric test results or findings.

### CVSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for CVSTRESC and CVSTRESN.

### CVSTAT
- **Order:** 20
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### CVREASND
- **Order:** 21
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed (e.g., "BROKEN EQUIPMENT", "SUBJECT REFUSED"). Used in conjunction with CVSTAT when value is "NOT DONE".

### CVLOC
- **Order:** 22
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Examples: "HEART", "LEFT VENTRICLE".

### CVLAT
- **Order:** 23
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL", "UNILATERAL".

### CVDIR
- **Order:** 24
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### CVMETHOD
- **Order:** 25
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method used to create the result.

### CVLOBXFL
- **Order:** 26
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### CVBLFL
- **Order:** 27
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that CVBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### CVDRVFL
- **Order:** 28
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (i.e., a record that represents the average of other records, such as a computed baseline). Should be "Y" or null.

### CVEVAL
- **Order:** 29
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", " INDEPENDENT ASSESSOR", "RADIOLOGIST".

### CVEVALID
- **Order:** 30
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in CVEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2".

### VISITNUM
- **Order:** 31
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 32
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 33
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 34
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 35
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### CVDTC
- **Order:** 36
- **Label:** Date/Time of Test
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation.

### CVDY
- **Order:** 37
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### CVTPT
- **Order:** 38
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See CVTPTNUM and CVTPTREF.

### CVTPTNUM
- **Order:** 39
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### CVELTM
- **Order:** 40
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (CVTPTREF). Examples: "PREVIOUS DOSE", "PREVIOUS MEAL". This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### CVTPTREF
- **Order:** 41
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by CVELTM, CVTPTNUM, and CVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### CVRFTDTC
- **Order:** 42
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by CVTPTREF.
---

## Cross References

### Controlled Terminology
- [Cardiovascular Test Name (C101846)](../../terminology/core/other_part1.md) — CVTEST
- [Cardiovascular Test Code (C101847)](../../terminology/core/other_part1.md) — CVTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — CVLOBXFL, CVBLFL, CVDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — CVSTAT
- [Position (C71148)](../../terminology/core/interventions.md) — CVPOS
- [Unit (C71620)](../../terminology/core/general_part5.md) — CVORRESU, CVSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — CVLOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — CVEVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — CVMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — CVEVALID
- [Laterality (C99073)](../../terminology/core/general_part2.md) — CVLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — CVDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/CV/assumptions.md -->
# CV — Assumptions

1. The Cardiovascular System Findings domain is used to represent results and findings of cardiovascular diagnostic procedures. Information about the conduct of the procedure(s), if collected, is submitted in the Procedures (PR) domain.

2. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the CV domain, but the following qualifiers would generally not be used: --MODIFY, --BODSYS, --FAST, --ORNRLO, --ORNRHI, --TNRLO, --STNRHI, and --LOINC.

<!-- source: knowledge_base/domains/DA/spec.md -->
# DA — Product Accountability

> Class: Findings | Structure: One record per product accountability finding per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study within the submission.

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

### DASEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DAGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### DAREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier such as a code from the product packaging (e.g., bottle label, package label, kit label).

### DASPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Examples: Line number on the Product Accountability CRF page, a code from the product packaging (e.g., bottle label, package label, kit label).

### DALNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### DALNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### DATESTCD
- **Order:** 10
- **Label:** Short Name of Accountability Assessment
- **Type:** Char
- **Controlled Terms:** C78732
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for DATEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters and cannot begin with a number or contain characters other than letters, numbers, or underscores. Examples: "DISPAMT", "RETAMT".

### DATEST
- **Order:** 11
- **Label:** Name of Accountability Assessment
- **Type:** Char
- **Controlled Terms:** C78731
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name corresponding to the topic variable of the test or examination used to obtain the product accountability assessment. The value in DATEST cannot be longer than 40 characters. Examples: "Dispensed Amount", "Returned Amount".

### DACAT
- **Order:** 12
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Examples: "STUDY MEDICATION", "RESCUE MEDICATION".

### DASCAT
- **Order:** 13
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization level for a group of related records.

### DAORRES
- **Order:** 14
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the product accountability assessment as originally received or collected.

### DAORRESU
- **Order:** 15
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for DAORRES.

### DASTRESC
- **Order:** 16
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all product accountability assessments copied or derived from DAORRES, in a standard format or in standard units. DASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in DASTRESN.

### DASTRESN
- **Order:** 17
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from DASTRESC. DASTRESN should store all numeric test results or findings.

### DASTRESU
- **Order:** 18
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for DASTRESC and DASTRESN.

### DASTAT
- **Order:** 19
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a product accountability assessment was not done. Should be null or have a value of "NOT DONE".

### DAREASND
- **Order:** 20
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with DASTAT when value is "NOT DONE".

### VISITNUM
- **Order:** 21
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 22
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 23
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit, based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 24
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm (see Section 7.2.1, Trial Arms).

### EPOCH
- **Order:** 25
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### DADTC
- **Order:** 26
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of the product accountability assessment represented in ISO 8601 character format.

### DADY
- **Order:** 27
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of product accountability assessment, measured in integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC in Demographics.
---

## Cross References

### Controlled Terminology
- [Not Done (C66789)](../../terminology/core/general_part4.md) — DASTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — DAORRESU, DASTRESU
- [Drug Accountability Test Name (C78731)](../../terminology/core/other_part1.md) — DATEST
- [Drug Accountability Test Code (C78732)](../../terminology/core/other_part1.md) — DATESTCD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/DA/assumptions.md -->
# DA — Assumptions

1. This domain records the amount of study product transferred to or from the study subject.
   a. Transfers of devices are not represented in this domain, but in the Device Tracking and Disposition (DT) domain. See the SDTMIG for Medical Devices (available at https://www.cdisc.org/standards/foundational/medical-devices-sdtmig/).
   b. For drugs, transfers are usually recorded using the tests "Dispensed Amount" and "Returned Amount".
   c. Test terminology for other products may be different; for example, for nutrition, the tests might be "Prepared Amount" and "Unused Amount".

2. DACAT may be used to differentiate transfers of different groups of products (e.g., rescue medications vs. investigational medications).

3. DAREFID and DASPID are both available for capturing label information.

4. The following qualifiers would not generally be used in DA: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --NAM, --LOINC, --SPEC, --SPCCND, --METHOD, --BLFL, --FAST, --DRVRL, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/DD/spec.md -->
# DD — Death Details

> Class: Findings | Structure: One record per finding per subject

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

### DDSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DDTESTCD
- **Order:** 5
- **Label:** Death Detail Assessment Short Name
- **Type:** Char
- **Controlled Terms:** C116108
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in DDTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in DDTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). DDTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRCDTH", "SECDTH".

### DDTEST
- **Order:** 6
- **Label:** Death Detail Assessment Name
- **Type:** Char
- **Controlled Terms:** C116107
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for DDTESTCD. The value in DDTEST cannot be longer than 40 characters. Examples: "Primary Cause of Death", "Secondary Cause of Death".

### DDORRES
- **Order:** 7
- **Label:** Result or Finding as Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the test defined in DDTEST, as originally received or collected.

### DDSTRESC
- **Order:** 8
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result or finding copied or derived from DDORRES in a standard format.

### DDRESCAT
- **Order:** 9
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding. Examples: "TREATMENT RELATED", "NONTREATMENT RELATED", "UNDETERMINED", "ACCIDENTAL".

### DDEVAL
- **Order:** 10
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation.

### DDDTC
- **Order:** 11
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of collection of the diagnosis or other death assessment data in ISO 8601 format. This is not necessarily the date of death.

### DDDY
- **Order:** 12
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.
---

## Cross References

### Controlled Terminology
- [SDTM Death Diagnosis and Details Test Name (C116107)](../../terminology/core/other_part4.md) — DDTEST
- [SDTM Death Diagnosis and Details Test Code (C116108)](../../terminology/core/other_part4.md) — DDTESTCD
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — DDEVAL

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/DD/assumptions.md -->
# DD — Assumptions

1. There may be more than 1 cause of death. If so, these may be separated into primary and secondary causes and/or other appropriate designations. DD may also include other details about the death, such as where the death occurred and whether it was witnessed.

2. Death details are typically collected on designated CRF pages. The DD domain is not intended to collate data that are collected in standard variables in other domains, such as AE.AEOUT (Outcome of Adverse Event), AE.AESDTH (Results in Death) or DS.DSTERM (Reported Term for the Disposition Event). Data from other domains that relates to the death can be linked to DD using RELREC.

3. This domain is not intended to include data obtained from autopsy. An autopsy is a procedure from which there will usually be findings. Autopsy information should be handled as per recommendations in the Procedures (PR) domain.

4. There are separate codelists for DD tests and responses. Associations between the DD tests and response codelists are described in the DD codeable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).

5. Any identifiers, timing variables, or findings general observation-class qualifiers may be added to the DD domain, but the following qualifiers would not generally be used: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --NAM, --LOINC, --SPEC, --SPCCND, --LOBXFL, --BLFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/DM/spec.md -->
# DM — Demographics

> Class: Special-Purpose | Structure: One record per subject

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
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. This must be a unique value, and could be a compound identifier formed by concatenating STUDYID-SITEID-SUBJID.

### SUBJID
- **Order:** 4
- **Label:** Subject Identifier for the Study
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Subject identifier, which must be unique within the study. Often the ID of the subject as recorded on a CRF.

### RFSTDTC
- **Order:** 5
- **Label:** Subject Reference Start Date/Time
- **Type:** DateTime
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Reference start date/time for the subject in ISO 8601 character format. Usually equivalent to date/time when subject was first exposed to study treatment. See assumption 9 for additional detail on when RFSTDTC may be null.

### RFENDTC
- **Order:** 6
- **Label:** Subject Reference End Date/Time
- **Type:** DateTime
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Reference end date/time for the subject in ISO 8601 character format. Usually equivalent to the date/time when subject was determined to have ended the trial, and often equivalent to date/time of last exposure to study treatment. Required for all randomized subjects; null for screen failures or unassigned subjects.

### RFXSTDTC
- **Order:** 7
- **Label:** Date/Time of First Study Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** First date/time of exposure to any protocol-specified treatment or therapy, equal to the earliest value of EXSTDTC.

### RFXENDTC
- **Order:** 8
- **Label:** Date/Time of Last Study Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Last date/time of exposure to any protocol-specified treatment or therapy, equal to the latest value of EXENDTC (or the latest value of EXSTDTC if EXENDTC was not collected or is missing).

### RFCSTDTC
- **Order:** 9
- **Label:** Date/Time of First Challenge Agent Admin
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used only when protocol specifies a challenge agent to induce a condition that the investigational treatment is intended to cure, mitigate, treat, or prevent. Equal to the earliest value of AGSTDTC for the challenge agent.

### RFCENDTC
- **Order:** 10
- **Label:** Date/Time of Last Challenge Agent Admin
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used only when protocol specifies a challenge agent to induce a condition that the investigational treatment is intended to cure, mitigate, treat, or prevent. Equal to the latest value of AGENDTC for the challenge agent (or the latest value of AGSTDTC if AGENDTC was not collected or is missing).

### RFICDTC
- **Order:** 11
- **Label:** Date/Time of Informed Consent
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Date/time of informed consent in ISO 8601 character format. This will be the same as the date of informed consent in the Disposition domain, if that protocol milestone is documented. Would be null only in studies not collecting the date of informed consent.

### RFPENDTC
- **Order:** 12
- **Label:** Date/Time of End of Participation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Date/time when subject ended participation or follow-up in a trial, as defined in the protocol, in ISO 8601 character format. Should correspond to the last known date of contact. Examples include completion date, withdrawal date, last follow-up, date recorded for lost to follow up, and death date.

### DTHDTC
- **Order:** 13
- **Label:** Date/Time of Death
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Date/time of death for any subject who died, in ISO 8601 format. Should represent the date/time that is captured in the clinical-trial database.

### DTHFL
- **Order:** 14
- **Label:** Subject Death Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates the subject died. Should be "Y" or null. Should be populated even when the death date is unknown.

### SITEID
- **Order:** 15
- **Label:** Study Site Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a site within a study.

### INVID
- **Order:** 16
- **Label:** Investigator Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** An identifier to describe the Investigator for the study. May be used in addition to SITEID. Not needed if SITEID is equivalent to INVID.

### INVNAM
- **Order:** 17
- **Label:** Investigator Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Name of the investigator for a site.

### BRTHDTC
- **Order:** 18
- **Label:** Date/Time of Birth
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Date/time of birth of the subject.

### AGE
- **Order:** 19
- **Label:** Age
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Age expressed in AGEU. May be derived from RFSTDTC and BRTHDTC, but BRTHDTC may not be available in all cases (due to subject privacy concerns).

### AGEU
- **Order:** 20
- **Label:** Age Units
- **Type:** Char
- **Controlled Terms:** C66781
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Units associated with AGE.

### SEX
- **Order:** 21
- **Label:** Sex
- **Type:** Char
- **Controlled Terms:** C66731
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Sex of the subject.

### RACE
- **Order:** 22
- **Label:** Race
- **Type:** Char
- **Controlled Terms:** C74457
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Race of the subject. Sponsors should refer to the FDA guidance2 regarding the collection of race. See assumption below regarding RACE.

### ETHNIC
- **Order:** 23
- **Label:** Ethnicity
- **Type:** Char
- **Controlled Terms:** C66790
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The ethnicity of the subject. Sponsors should refer to the FDA guidance1 regarding the collection of ethnicity.

### ARMCD
- **Order:** 24
- **Label:** Planned Arm Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** ARMCD is limited to 20 characters. It is not subject to the character restrictions that apply to TESTCD. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. If the subject was not assigned to a trial arm, ARMCD is null and ARMNRS is populated.  With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial Arms dataset.

### ARM
- **Order:** 25
- **Label:** Description of Planned Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Exp
- **CDISC Notes:** Name of the arm to which the subject was assigned. If the subject was not assigned to an arm, ARM is null and ARMNRS is populated.  With the exception of studies which use multistage arm assignments, must be a value of ARM in the Trial Arms dataset.

### ACTARMCD
- **Order:** 26
- **Label:** Actual Arm Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Code of actual arm. ACTARMCD is limited to 20 characters. It is not subject to the character restrictions that apply to TESTCD. The maximum length of ACTARMCD is longer than for other short variables to accommodate the kind of values that are likely to be needed for crossover trials.  With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial Arms dataset.  If the subject was not assigned to an arm or followed a course not described by any planned arm, ACTARMCD is null and ARMNRS is populated.

### ACTARM
- **Order:** 27
- **Label:** Description of Actual Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Exp
- **CDISC Notes:** Description of actual arm.  With the exception of studies which use multistage arm assignments, must be a value of ARM in the Trial Arms dataset.  If the subject was not assigned to an arm or followed a course not described by any planned arm, ACTARM is null and ARMNRS is populated.

### ARMNRS
- **Order:** 28
- **Label:** Reason Arm and/or Actual Arm is Null
- **Type:** Char
- **Controlled Terms:** C142179
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** A coded reason that arm variables (ARM and ARMCD) and/or actual arm variables (ACTARM and ACTARMCD) are null. Examples: "SCREEN FAILURE", "NOT ASSIGNED", "ASSIGNED, NOT TREATED", "UNPLANNED TREATMENT". It is assumed that if the arm and actual arm variables are null, the same reason applies to both arm and actual arm.

### ACTARMUD
- **Order:** 29
- **Label:** Description of Unplanned Actual Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** A description of actual treatment for a subject who did not receive treatment described in a planned trial arm.

### COUNTRY
- **Order:** 30
- **Label:** Country
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Country of the investigational site in which the subject participated in the trial.   Generally represented using ISO 3166-1 Alpha-3. Note that regulatory agency specific requirements (e.g., US FDA) may require other terminologies; in such cases, follow regulatory requirements.

### DMDTC
- **Order:** 31
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of demographic data collection.

### DMDY
- **Order:** 32
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of collection measured as integer days.
---

## Cross References

### Controlled Terminology
- [Arm Null Reason (C142179)](../../terminology/core/dm.md) — ARMNRS
- [Sex (C66731)](../../terminology/core/dm.md) — SEX
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — DTHFL
- [Age Unit (C66781)](../../terminology/core/dm.md) — AGEU
- [Ethnic Group (C66790)](../../terminology/core/dm.md) — ETHNIC
- [Race (C74457)](../../terminology/core/dm.md) — RACE

### Related Domains
- **Same class (Special-Purpose):** CO, SE, SM, SV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)

<!-- source: knowledge_base/domains/DM/assumptions.md -->
# DM — Assumptions

1. Investigator and site identification: Companies use different methods to distinguish sites and investigators. CDISC assumes that SITEID will always be present, with INVID and INVNAM used as necessary. This should be done consistently and the meaning of the variable made clear in the Define-XML document.

2. Every subject in a study must have a subject identifier (SUBJID). In some cases a subject may participate in more than 1 study. To identify a subject uniquely across all studies for all applications or submissions involving the product, a unique identifier (USUBJID) must be included in all datasets. Subjects occasionally change sites during the course of a clinical trial. Sponsors must decide how to populate variables such as USUBJID, SUBJID and SITEID based on their operational and analysis needs, but only 1 DM record should be submitted for each subject. The Supplemental Qualifiers dataset may be used if appropriate to provide additional information.

3. Concerns for subject privacy suggest caution regarding the collection of variables like BRTHDTC. This variable is included in the Demographics model in the event that a sponsor intends to submit it; however, sponsors should follow regulatory guidelines and guidance as appropriate.

4. With the exception of trials that use multistage processes to assign subjects to arms as described below, ARM and ACTARM must be populated with ARM values from the Trial Arms (TA) dataset and ARMCD and ACTARMCD must be populated with ARMCD values from the TA dataset or be null. The ARM and ARMCD values in the TA dataset have a one-to-one relationship, and that one-to-one relationship must be preserved in the values used to populate ARM and ARMCD in DM, and to populate the values of ACTARM and ACTARMCD in DM.
   a. Rules for the arm-related variables:
      i. If ARMCD is null, then ARM must be null and ARMNRS must be populated with the reason ARMCD is null.
      ii. If ACTARMCD is null, then ACTARM must be null and ARMNRS must be populated with the reason ACTARMCD is null. Both ARMCD and ACTARMCD will be null for subjects who were not assigned to treatment. The same reason will provide the reason that both are null.
      iii. ARMNRS may not be populated if both ARMCD and ACTARMCD are populated. ARMCD and ACTARMCD will be populated if the subject was assigned to an arm and received treatment consistent with 1 of the arms in the TA dataset. If ARMCD and ACTARMCD are not the same, that is sufficient to explain the situation; ARMNRS should not be populated.
      iv. If ARMNRS is populated with "UNPLANNED TREATMENT", ACTARMUD should be populated with a description of the unplanned treatment received.
   b. Multistage assignment to treatment: Some trials use a multistage process for assigning a subject to an arm (see Section 7.2.1, Trial Arms, Example Trial 3). In such a case, best practice is to create ARMCD values composed of codes representing the results of the multiple stages of the treatment assignment process. If a subject is partially assigned, then truncated codes representing the stages completed can be used in ARMCD, and similar truncated codes can be used in ACTARMCD. The descriptions used to populate ARM and ACTARM should be similarly truncated, and the one-to-one relationship between these truncated codes should be maintained for all affected subjects in the trial. Example 3 below provides an example of this situation; see also Section 5.3, Subject Elements, Example 2. Note that this use of values not in the TA dataset is allowable only for trials with multistage assignment to arms and to subjects in those trials who do not complete all stages of the assignment.
   c. Examples illustrating the arm-related variables
      i. Example 1 below shows how to handle a subject who was a screen failure and was never treated.
      ii. The Subject Elements (SE) dataset records the series of elements a subject passed through in the course of a trial, and these determine the value of ACTARMCD. The following examples include sample data for both datasets to illustrate this relationship.
         1. Example 2 below shows how subjects who started the trial but were never assigned to an arm would be handled.
         2. Section 5.3, Subject Elements, Example 1 illustrates a situation for a subject who received a treatment that was not the one to which they were assigned.
         3. Section 5.3, Subject Elements, Example 2 illustrates a situation in which a subject received a set of treatments different from that for any of the planned arms.

5. Study population flags should not be included in SDTM data. The standard supplemental qualifiers included in previous versions of the SDTMIG (COMPLT, FULLSET, ITT, PPROT, SAFETY) should not be used. Note: The ADaM Subject-level Analysis Dataset (ADSL) specifies standard variable names for the most common populations and requires the inclusion of these flags when necessary for analysis; consult the ADaMIG for more information about these variables.

6. Submission of multiple race responses should be represented in the Demographics (DM) domain and Supplemental Qualifiers (SUPPDM) dataset as described in Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable. If multiple races are collected, then the value of RACE should be "MULTIPLE" and the additional information will be included in the Supplemental Qualifiers dataset. Controlled terminology for RACE should be used in both DM and SUPPDM so that consistent values are available for summaries regardless of whether the data are found in a column or row. If multiple races were collected and 1 was designated as primary, RACE in DM should be the primary race and additional races should be reported in SUPPDM. When additional free-text information is reported about subject's race using "Other, Specify", sponsors should refer to Section 4.2.7.1, "Specify" Values for Non-Result Qualifier Variables. If race was collected via an "Other, Specify" field and the sponsor chooses not to map the value as described in the current FDA guidance (see CDISC Notes for RACE in the domain specification), then the value of RACE should be "OTHER". For subjects who refuse to provide or do not know their race information, the value of RACE could be "UNKNOWN". See DM Example 4, DM Example 5, DM Example 6, and DM Example 7.
   a. The Racec-Ethnicc Codetable (available at https://www.cdisc.org/standards/terminology/controlled-terminology) represents associations between collected race values and published race Controlled Terminology, as well as collected ethnicity values and published ethnicity Controlled Terminology.

7. RFSTDTC, RFENDTC, RFXSTDTC, RFXENDTC, RFCSTDTC, RFCENDTC, RFICDTC, RFPENDTC, DTHDTC, and BRTHDTC represent date/time values, but they are considered to have a record qualifier role in DM. They are not considered to be timing variables because they are not intended for use in the general observation classes.

8. Additional permissible identifier, qualifier, and timing variables:
   a. Only the following timing variables are permissible and may be added as appropriate: VISITNUM, VISIT, VISITDY. The record qualifier DMXFN (External File Name) is the only additional qualifier variable that may be added, which is adopted from the Findings general observation class, may also be used to refer to an external file, such as a patient narrative.
   b. The order of these additional variables within the domain should follow the rules as described in Section 4.1.4, Order of the Variables, and the order described in Section 4.2, General Variable Assumptions.

9. As described in Section 4.1.4, Order of the Variables, RFSTDTC is used to calculate study day variables. RFSTDTC is usually defined as the date/time when a subject was first exposed to study drug. This definition applies for most interventional studies, when the start of treatment is the natural and preferred starting point for study day variables and thus the logical value for RFSTDTC. In such studies, when data are submitted for subjects who are ineligible for treatment (e.g., screen failures with ARMNRS = "SCREEN FAILURE"), subjects who were enrolled but not assigned to an arm (e.g., ARMNRS = "NOT ASSIGNED"), or subjects who were randomized but not treated (e.g., ARMNRS = "NOT TREATED"), RFSTDTC will be null. For studies with designs that include a substantial portion of subjects who are not expected to be treated, a different protocol milestone may be chosen as the starting point for study day variables. Some examples include non-interventional or observational studies, studies with a no-treatment arm, and studies where there is a delay between randomization and treatment.

10. The DM domain contains several pairs of reference period variables: RFSTDTC and RFENDTC, RFXSTDTC and RFXENDTC, RFCSTDTC and RFCENDTC, and RFICDTC and RFPENDTC. There are 4 sets of reference variables to accommodate distinct reference-period definitions and there are instances when the values of the variables may be exactly the same, particularly with RFSTDTC-RFENDTC and RFXSTDTC-RFXENDTC.
    a. RFSTDTC and RFENDTC: This pair of variables is sponsor-defined, but usually represents the date/time of first and last study exposure. However, there are certain study designs where the start of the reference period is defined differently, such as studies that have a washout period before randomization or have a medical procedure required during screening (e.g., biopsy). In these cases, RFSTDTC may be the enrollment date, which is prior to first dose. Because study day values are calculated using RFSTDTC, in this case study days would not be based on the date of first dose.
    b. RFXSTDTC and RFXENDTC: This pair of variables defines a consistent reference period for all interventional studies and is not open to customization. RFXSTDTC and RFXENDTC always represent the date/time of first and last study exposure. The study reference period often duplicates the reference period defined in RFSTDTC and RFENDTC, but not always. Therefore, this pair of variables is important as they guarantee that a reviewer will always be able to reference the first and last study exposure reference period. RFXSTDTC should be the same as SESTDTC for the first treatment element described in the SE dataset. RFXENDTC may often be the same as the SEENDTC for the last treatment element described in the SE dataset.
    c. RFCSTDTC and RFCENDTC: This pair of variables is used only when the study uses a protocol-specified challenge agent to induce a condition that the investigational treatment is intended to cure, mitigate, treat, or prevent. RFCSTDTC and RFCENDTC always represent the date/time of first and last exposure to the challenge agent.
    d. RFICDTC and RFPENDTC: The definitions of this pair of variables are consistent in every study in which they are used: They represent the entire period of a subject's involvement in a study, from providing informed consent through the last participation event or activity. There may be times when this period coincides with other reference periods but that is unusual. An example of when these periods might coincide with the study reference period, RFSTDTC to RFENDTC, might be an observational trial where no study intervention is administered. RFICDTC should correspond to the date of the informed consent protocol milestone in Disposition (DS), if that protocol milestone is documented in DS. In the event that there are multiple informed consents, this will be the date of the first. RFPENDTC will be the last date of participation for a subject for data included in a submission. This should be the last date of any record for the subject in the database at the time it is locked for submission. As such, it may not be the last date of participation in the study if the submission includes interim data.

<!-- source: knowledge_base/domains/DS/spec.md -->
# DS — Disposition

> Class: Events | Structure: One record per disposition status or protocol milestone per subject

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

### DSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### DSREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier.

### DSSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Disposition page.

### DSTERM
- **Order:** 8
- **Label:** Reported Term for the Disposition Event
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim name of the event or protocol milestone. Some terms in DSTERM will match DSDECOD, but others, such as "Subject moved", will map to controlled terminology in DSDECOD, such as "LOST TO FOLLOW-UP".

### DSDECOD
- **Order:** 9
- **Label:** Standardized Disposition Term
- **Type:** Char
- **Controlled Terms:** C66727; C114118; C150811
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Controlled terminology for the name of disposition event or protocol milestone. Examples of protocol milestones: "INFORMED CONSENT OBTAINED", "RANDOMIZED". There are separate codelists used for DSDECOD where the choice depends on the value of DSCAT. Codelist "NCOMPLT" is used for disposition events, codelist "PROTMLST" is used for protocol milestones, and codelist "OTHEVENT" is used for other events.

### DSCAT
- **Order:** 10
- **Label:** Category for Disposition Event
- **Type:** Char
- **Controlled Terms:** C74558
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of related records.

### DSSCAT
- **Order:** 11
- **Label:** Subcategory for Disposition Event
- **Type:** Char
- **Controlled Terms:** C170443
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of DSCAT (e.g., "STUDY PARTICIPATION", "STUDY TREATMENT" when DSCAT = "DISPOSITION EVENT"). The variable may be subject to controlled terminology for other categories of disposition event records.

### EPOCH
- **Order:** 12
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the event.

### DSDTC
- **Order:** 13
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the disposition observation represented in ISO 8601 character format.

### DSSTDTC
- **Order:** 14
- **Label:** Start Date/Time of Disposition Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of the disposition event in ISO 8601 character format.

### DSDY
- **Order:** 15
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of collection of event relative to the sponsor-defined RFSTDTC.

### DSSTDY
- **Order:** 16
- **Label:** Study Day of Start of Disposition Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Study day of start of event relative to the sponsor-defined RFSTDTC.
---

## Cross References

### Controlled Terminology
- [Protocol Milestone (C114118)](../../terminology/core/disposition.md) — DSDECOD
- [Other Disposition Event Response (C150811)](../../terminology/core/disposition.md) — DSDECOD
- [Subcategory for Disposition Event (C170443)](../../terminology/core/disposition.md) — DSSCAT
- [Completion/Reason for Non-Completion (C66727)](../../terminology/core/disposition.md) — DSDECOD
- [Category of Disposition Event (C74558)](../../terminology/core/disposition.md) — DSCAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Events):** AE, BE, CE, DV, HO, MH
- **Demographics:** [DM](../DM/) — disposition dates relate to DM reference dates

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Events class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/DS/assumptions.md -->
# DS — Assumptions

1. The Disposition (DS) dataset provides an accounting for all subjects who entered the study and may include protocol milestones, such as randomization, as well as the subject's completion status or reason for discontinuation for the entire study or each phase or segment of the study, including screening and post-treatment follow-up. Sponsors may choose which disposition events and milestones to submit for a study. See ICH E3, Section 10.1, for information about disposition events.

2. **Categorization**
   a. DSCAT is used to distinguish between disposition events, protocol milestones, and other events. The controlled terminology for DSCAT consists of "DISPOSITION EVENT", "PROTOCOL MILESTONE", and "OTHER EVENT".
   b. An event with DSCAT = "DISPOSITION EVENT" describes either disposition of study participation or of a study treatment. It describes whether a subject completed study participation or a study treatment and, if not, the reason they did not complete it. Dispositions may be described for each epoch (e.g., screening, initial treatment, washout, cross-over treatment, follow-up) or for the study as a whole. If disposition events for both study participation and study treatment(s) are to be represented, then DSCAT provides this distinction. For records with DSCAT = "DISPOSITION EVENT",
      i. DSSCAT = "STUDY PARTICIPATION" is used to represent disposition of study participation.
      ii. DSSCAT = "STUDY TREATMENT" is used when a study has only a single treatment.
      iii. If a study has multiple treatments, then DSSCAT should name the individual treatment.
   c. DSSCAT may be used when DSCAT = "PROTOCOL MILESTONE" or "OTHER EVENT", but would be subject to additional CDISC Controlled Terminology.
   d. An event with DSCAT = "PROTOCOL MILESTONE" is a protocol-specified, point-in-time event. Common protocol milestones include "INFORMED CONSENT OBTAINED" and "RANDOMIZED." DSSCAT may be used for subcategories of protocol milestones.
   e. An event with DSCAT = "OTHER EVENT" is another important event that occurred during a trial, but was not driven by protocol requirements and was not captured in another Events or Interventions class dataset. "TREATMENT UNBLINDED" is an example of an event that would be represented with DSCAT = "OTHER EVENT".
   f. Associations between DSCAT and some DSDECOD codelist values are described in the DS Codetable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).

3. **DS description and coding**
   a. DSDECOD values are drawn from controlled terminology. The controlled terminology depends on the value of DSCAT.
   b. When DSCAT = "DISPOSITION EVENT" DSTERM contains either "COMPLETED" or, if the subject did not complete, specific verbatim information about the reason for non-completion.
      i. When DSTERM = "COMPLETED", DSDECOD is the term "COMPLETED" from the Controlled Terminology codelist NCOMPLT.
      ii. When DSTERM contains verbatim text, DSDECOD will use the extensible Controlled Terminology Codelist NCOMPLT. For example, DSTERM = "Subject moved" might be coded to DSDECOD = "LOST TO FOLLOW-UP".
   c. When DSCAT = "PROTOCOL MILESTONE", DSTERM contains the verbatim (as collected) and/or standardized text, DSDECOD will use the extensible Controlled Terminology codelist PROTMLST.
   d. When DSCAT = "OTHER EVENT", DSTERM and DSDECOD uses sponsor terminology.
      i. If a reason for the event was collected, the reason for the event is in DSTERM and the DSDECOD is a term from sponsor terminology. For example, if treatment was unblinded due to investigator error, this might be represented in a record with DSTERM = "INVESTIGATOR ERROR" and DSDECOD = "TREATMENT UNBLINDED".
      ii. If no reason was collected, then DSTERM should be populated with the value in DSDECOD.

4. **Timing variables**
   a. DSSTDTC is expected and is used for the date/time of the disposition event. Events represented in the DS domain do not have end dates; disposition events do not span an interval, but rather occur at a single date/time (e.g., randomization date, disposition of study participation or study treatment).
   b. DSSTDTC documents the date/time that a protocol milestone, disposition event, or other event occurred. For an event with DSCAT = "DISPOSITION EVENT" where DSTERM is not "COMPLETED", the reason for non-completion may be related to an observation reported in another dataset. DSSTDTC is the date/time that the Epoch was completed and is not necessarily the same as the date/time, start date/time, or end date/time of the observation that led to discontinuation.

      For example, a subject reported severe vertigo on June 1, 2006 (AESTDTC). After ruling out other possible causes, the investigator decided to discontinue study treatment on June 6, 2006 (DSSTDTC). The subject reported that the vertigo had resolved on June 8, 2006 (AEENDTC).
   c. EPOCH may be included as a timing variable as in other general observation-class domains. In DS, EPOCH is based on DSSTDTC. The values of EPOCH are drawn from the Trial Arms (TA) dataset (see Section 7.2.1, Trial Arms).

5. Reasons for termination: ICH E3 Section 10.1 indicates that "the specific reason for discontinuation" should be presented, and that summaries should be grouped by treatment and by major reason." The CDISC SDS Team interprets this guidance as requiring 1 standardized disposition term (DSDECOD) per disposition event. If multiple reasons are reported, the sponsor should identify a primary reason and use that to populate DSTERM and DSDECOD. Additional reasons should be submitted in SUPPDS.

   For example, in a case where DSTERM = "SEVERE NAUSEA" and DSDECOD = "ADVERSE EVENT", the supplemental qualifiers dataset might include records with

   SUPPDS QNAM = "DSTERM1", SUPPDS QLABEL = "Reported Term for Disposition Event 1", and SUPPDS QVAL = "SUBJECT REFUSED FURTHER TREATMENT"

   SUPPDS QNAM = "DSDECOD1", SUPPDS QLABEL = "Standardized Disposition Term 1", and SUPPDS QVAL = "WITHDREW CONSENT"

6. Any identifier variables, timing variables, or Events general observation-class qualifiers may be added to the DS domain, but the following Qualifiers would generally not be used: --PRESP, --OCCUR, --STAT, --REASND, --BODSYS, --LOC, --SEV, --SER, --ACN, --ACNOTH, --REL, --RELNST, --PATT, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --CONTRT, --TOXGR.

<!-- source: knowledge_base/domains/DV/spec.md -->
# DV — Protocol Deviations

> Class: Events | Structure: One record per protocol deviation per subject

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

### DVSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### DVREFID
- **Order:** 5
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier.

### DVSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page.

### DVTERM
- **Order:** 7
- **Label:** Protocol Deviation Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim name of the protocol deviation criterion. Example: "IVRS PROCESS DEVIATION - NO DOSE CALL PERFORMED". DVTERM values will map to the controlled terminology in DVDECOD (e.g., "TREATMENT DEVIATION").

### DVDECOD
- **Order:** 8
- **Label:** Protocol Deviation Coded Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Controlled terminology for the name of the protocol deviation. Examples: "SUBJECT NOT WITHDRAWN AS PER PROTOCOL", "SELECTION CRITERIA NOT MET", "EXCLUDED CONCOMITANT MEDICATION", "TREATMENT DEVIATION".

### DVCAT
- **Order:** 9
- **Label:** Category for Protocol Deviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Category of the protocol deviation criterion.

### DVSCAT
- **Order:** 10
- **Label:** Subcategory for Protocol Deviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the protocol deviation.

### TAETORD
- **Order:** 11
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 12
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the deviation. Examples: "TREATMENT", "SCREENING", "FOLLOW-UP".

### DVSTDTC
- **Order:** 13
- **Label:** Start Date/Time of Deviation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of deviation represented in ISO 8601 character format.

### DVENDTC
- **Order:** 14
- **Label:** End Date/Time of Deviation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of deviation represented in ISO 8601 character format.

### DVSTDY
- **Order:** 15
- **Label:** Study Day of Start of Deviation Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of event relative to the sponsor-defined RFSTDTC.

### DVENDY
- **Order:** 16
- **Label:** Study Day of End of Deviation Event
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of event relative to the sponsor-defined RFSTDTC.
---

## Cross References

### Controlled Terminology
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Events):** AE, BE, CE, DS, HO, MH

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Events class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/DV/assumptions.md -->
# DV — Assumptions

1. The DV domain is an Events model for collected protocol deviations and not for derived protocol deviations that are more likely to be part of analysis. Events typically include what the event was, captured in --TERM (the topic variable), and when it happened (captured in its start and/or end dates). The intent of the domain model is to capture protocol deviations that occurred during the course of the study (see ICH E3, Section 10.2[1]). Usually these are deviations that occur after the subject has been randomized or received the first treatment.

2. This domain should not be used to collect entry-criteria information. Violated inclusion/exclusion criteria are stored in IE. The Deviations domain is for more general deviation data. A protocol may indicate that violating an inclusion/exclusion criterion during the course of the study (after first dose) is a protocol violation. In this case, this information would go into DV.

3. Any identifier variables, timing variables, or Events general observation-class qualifiers may be added to the DV domain, but the following qualifiers would generally not be used: --PRESP, --OCCUR, --STAT, --REASND, --BODSYS, --LOC, --SEV, --SER, --ACN, --ACNOTH, --REL, --RELNST, --PATT, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --CONTRT, --TOXGR.

<!-- source: knowledge_base/domains/EC/spec.md -->
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

<!-- source: knowledge_base/domains/EC/assumptions.md -->
# EC — Assumptions

1. The EC domain model reflects protocol-specified study treatment administrations, as collected.
   a. EC should be used in all cases where collected exposure information cannot or should not be directly represented in the Exposure (EX) domain. For example, administrations collected in tablets when the protocol-specified unit is mg, or administrations collected in mL when the protocol-specified unit is mg/kg. Product accountability details (e.g., amount dispensed, amount returned) are represented in the DA domain, not in EC.
   b. Collected exposure data are in most cases represented in a combination of 1 or more of EC, DA, or Findings About Events or Interventions (FA) domains. If the entire EC dataset is an exact duplicate of the entire EX dataset, then EC is optional and at the sponsor's discretion.
   c. Collected exposure log data points descriptive of administrations typically reflect amounts at the product-level (e.g., number of tablets, number of mL).

2. Treatment description (ECTRT) is sponsor-defined and should reflect how the protocol-specified study treatment is known or referred to in data collection. In an open-label study, ECTRT should store the treatment name. In a masked study, if treatment is collected and known as tablet A to the subject or administrator, then ECTRT = "TABLET A". If, in a masked study, the treatment is not known by a synonym and the data are to be exchanged between sponsors, partners, and/or regulatory agency(s), then assign ECTRT the value of "MASKED".

3. ECMOOD is permissible; when implemented, it must be populated for all records.
   a. Values of ECMOOD, to date include:
      i. "SCHEDULED" (for collected subject-level intended dose records)
      ii. "PERFORMED" (for collected subject-level actual dose records)
   b. Qualifier variables should be populated with equal granularity across scheduled and performed records when known. For example, if ECDOSU and ECDOSFRQ are known at scheduling and administration, then the variables would be populated on both records. If ECLOC is determined at the time of administration, then it would be populated on the Performed record only.
   c. Appropriate timing variable(s) should be populated. Note: Details on Scheduled records may describe timing at a higher level than Performed records.
   d. ECOCCUR is generally not applicable for Scheduled records.
   e. An activity may be rescheduled or modified multiple times before being performed. Representation of Scheduled records is dependent on the collected, available data. If each rescheduled or modified activity is collected, then multiple Scheduled records may be represented. If only the final scheduled activity is collected, then it would be the only Scheduled record represented.

4. Doses not taken, not given, or missed
   a. The record qualifier --OCCUR, with value of "N", is available in domains based on the Interventions and Events General Observation Classes as the standard way to represent whether an intervention or event did not happen. In the EC domain, ECOCCUR value of "N" indicates a dose was not taken, not given, or missed. For example, if zero tablets are taken within a timeframe or zero mL is infused at a visit, then ECOCCUR = "N" is the standard representation of the collected doses not taken, not given, or missed. Dose amount variables (e.g., ECDOSE, ECDOSTXT) must not be set to zero (0) as an alternative method for indicating doses not taken, not given, or missed.
   b. The population of qualifier variables (e.g., grouping, record) and additional timing variables (e.g., date of collection, visit, time point) for records representing information collected about doses not taken, not given, or missed should be populated with equal granularity as administered records, when known and/or applicable. Qualifiers that indicate dose amount (e.g., ECDOSE, ECDOSTXT) may be populated with positive (non-zero) values in cases where the sponsor feels it is necessary and/or appropriate to represent specific dose amounts not taken, not given, or missed.
   c. If a reason why a dose was not given is collected, it is represented in ECREASOC, the reason why ECOCCUR = "N".

5. Timing variables
   a. Timing variables in the EC domain should reflect administrations by the intervals they were collected (e.g., constant-dosing intervals, visits, targeted dates like first dose, last dose).
   b. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, ECSTDTC should be copied to ECENDTC.

6. The degree of summarization of records from EC to EX is sponsor-defined to support study purpose and analysis. When the relationship between EC and EX records can be described in RELREC, then it should be defined. EX derivations must be described in the Define-XML document.

7. Additional interventions qualifiers
   a. --DOSTOT is under evaluation for potential deprecation and replacement with a mechanism to describe total dose over any interval of time (e.g., day, week, month). Sponsors considering ECDOSTOT may want to consider using other dose amount variables (ECDOSE or ECDOSTXT) in combination with frequency (ECDOSFRQ) and timing variables to represent the data.
   b. Any identifier variables, timing variables, or findings general observation-class qualifiers may be added to the EC domain, but the following qualifiers would generally not be used: --STAT and --REASND.

<!-- source: knowledge_base/domains/EG/spec.md -->
# EG — ECG Test Results

> Class: Findings | Structure: One record per ECG observation per replicate per time point or one record per ECG observation per beat per visit per subject

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
- **CDISC Notes:** Sponsor-defined identifier for a device.

### EGSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### EGGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### EGREFID
- **Order:** 7
- **Label:** ECG Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external ECG identifier. Example: "334PT89".

### EGSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the ECG page.

### EGBEATNO
- **Order:** 9
- **Label:** ECG Beat Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** A sequence number that identifies the beat within an ECG.

### EGTESTCD
- **Order:** 10
- **Label:** ECG Test or Examination Short Name
- **Type:** Char
- **Controlled Terms:** C71153; C120523
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in EGTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in EGTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). EGTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "PRAG", "QRSAG".  Test codes are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTESTCD) and one 1 tests based on Holter monitoring (HETESTCD).

### EGTEST
- **Order:** 11
- **Label:** ECG Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C71152; C120524
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in EGTEST cannot be longer than 40 characters. Examples: "PR Interval, Aggregate", "QRS Duration, Aggregate".  Test names are in 2 separate codelists, 1 for tests based on regular 10-second ECGs (EGTEST) and 1 for tests based on Holter monitoring (HETEST).

### EGCAT
- **Order:** 12
- **Label:** Category for ECG
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize ECG observations across subjects. Examples: "MEASUREMENT", "FINDING", "INTERVAL".

### EGSCAT
- **Order:** 13
- **Label:** Subcategory for ECG
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the ECG.

### EGPOS
- **Order:** 14
- **Label:** ECG Position of Subject
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### EGORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the ECG measurement or finding as originally received or collected. Examples of expected values are "62" or "0.151" when the result is an interval or measurement, or "ATRIAL FIBRILLATION" or "QT PROLONGATION" when the result is a finding.

### EGORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for EGORRES. Examples: "sec", "msec".

### EGSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C71150; C120522; C101834
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from EGORRES, in a standard format or standard units. EGSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in EGSTRESN. For example, if a test has results of 62 beats/min, then EGORRES = "62", EGORRESU = "beats/min", EGSTRESC = "62", EGSTRESN = 62, and EGSTRESU = "beats/min" . For other examples, see Original and Standardized Results. Additional examples of result data: "SINUS BRADYCARDIA", "ATRIAL FLUTTER", "ATRIAL FIBRILLATION".  Test results are in 3 separate codelists: EGSTRESC for abnormal test results based on regular 10-second ECGs; HESTRESC for abnormal test results based on Holter monitoring, and NORMABNM for generic test results and/or responses to EGTEST = "Interpretation".

### EGSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from EGSTRESC. EGSTRESN should store all numeric test results or findings.

### EGSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for EGSTRESC and EGSTRESN.

### EGSTAT
- **Order:** 20
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate an ECG was not done, or an ECG measurement was not taken. Should be null if a result exists in EGORRES.

### EGREASND
- **Order:** 21
- **Label:** Reason ECG Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with EGSTAT when value is "NOT DONE".

### EGXFN
- **Order:** 22
- **Label:** ECG External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** File name and path for the external ECG waveform file.

### EGNAM
- **Order:** 23
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the laboratory or vendor providing the test results.

### EGMETHOD
- **Order:** 24
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C71151
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the ECG test. Example: "12-LEAD STANDARD".

### EGLEAD
- **Order:** 25
- **Label:** Lead Location Used for Measurement
- **Type:** Char
- **Controlled Terms:** C90013
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The lead used for the measurement. Examples: "LEAD 1", "LEAD 2", "LEAD rV2", "LEAD V1".

### EGLOBXFL
- **Order:** 26
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### EGBLFL
- **Order:** 27
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that EGBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### EGDRVFL
- **Order:** 28
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If EGDRVFL="Y", then EGORRES could be null, with EGSTRESC and EGSTRESN (if the result is numeric) having the derived value.

### EGEVAL
- **Order:** 29
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR".

### EGEVALID
- **Order:** 30
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in EGEVAL. Examples: "RADIOLOGIST 1" or "RADIOLOGIST 2".

### EGCLSIG
- **Order:** 31
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgment.

### EGREPNUM
- **Order:** 32
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.

### VISITNUM
- **Order:** 33
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 34
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 35
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 36
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 37
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### EGDTC
- **Order:** 38
- **Label:** Date/Time of ECG
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/Time of ECG.

### EGDY
- **Order:** 39
- **Label:** Study Day of ECG
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the ECG, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### EGTPT
- **Order:** 40
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EGTPTNUM and EGTPTREF. Examples: "Start", "5 min post".

### EGTPTNUM
- **Order:** 41
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of EGTPT to aid in sorting.

### EGELTM
- **Order:** 42
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a fixed time point reference (EGTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by EGTPTREF.

### EGTPTREF
- **Order:** 43
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by EGELTM, EGTPTNUM, and EGTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### EGRFTDTC
- **Order:** 44
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by EGTPTREF.
---

## Cross References

### Controlled Terminology
- [Normal Abnormal Response (C101834)](../../terminology/core/eg_part3.md) — EGSTRESC
- [Holter ECG Results (C120522)](../../terminology/core/eg_part3.md) — EGSTRESC
- [Holter ECG Test Code (C120523)](../../terminology/core/eg_part3.md) — EGTESTCD
- [Holter ECG Test Name (C120524)](../../terminology/core/eg_part3.md) — EGTEST
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — EGLOBXFL, EGBLFL, EGDRVFL, EGCLSIG
- [Not Done (C66789)](../../terminology/core/general_part4.md) — EGSTAT
- [Position (C71148)](../../terminology/core/interventions.md) — EGPOS
- [ECG Result (C71150)](../../terminology/core/eg_part1.md) — EGSTRESC
- [ECG Test Method (C71151)](../../terminology/core/eg_part2.md) — EGMETHOD
- [ECG Test Name (C71152)](../../terminology/core/eg_part2.md) — EGTEST
- [ECG Test Code (C71153)](../../terminology/core/eg_part2.md) — EGTESTCD
- [Unit (C71620)](../../terminology/core/general_part5.md) — EGORRESU, EGSTRESU
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — EGEVAL
- [ECG Lead (C90013)](../../terminology/core/eg_part1.md) — EGLEAD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — EGEVALID
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Related Findings:** [CP](../CP/) — ECG vs cardiac electrophysiology

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/EG/assumptions.md -->
# EG — Assumptions

1. EGREFID is intended to store an identifier (e.g., UUID) for the associated ECG tracing. EGXFN is intended to store the name of and path to the electrocardiogram (ECG) waveform file when it is submitted.

2. There are separate codelists for tests and results based on regular 10-second ECGs and for tests and results based on Holter monitoring.
   a. Associations between some ECG abnormality tests and response codelists are described in the ECG codetable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).

3. For non-individual ECG beat data and for aggregate ECG parameter results (e.g., "QT interval", "RR", "PR", "QRS"), EGREFID is populated for all unique ECGs, so that submitted SDTM data can be matched to the actual ECGs stored in the ECG warehouse. Therefore, this variable is expected for these types of records.

4. For individual-beat parameter results, waveform data will not be stored in the warehouse, so there will be no associated identifier for these beats.

5. The method for QT interval correction is specified in the test name by controlled terminology: EGTESTCD = "QTCFAG" and EGTEST = "QTcF Interval, Aggregate" is used for Fridericia's formula; EGTESTCD = "QTCBAG" and EGTEST = "QTcB Interval, Aggregate", is used for Bazett's formula.

6. EGBEATNO is used to differentiate between beats in beat-to-beat records.

7. EGREPNUM is used to differentiate between multiple repetitions of a test within a given time frame.

8. EGNRIND can be added to indicate where a result falls with respect to reference range defined by EGORNRLO and EGORNRHI. Examples: "HIGH", "LOW". Clinical significance would be represented as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data, in EGCLSIG (see also EG Example 1).

9. When "QTcF Interval, Aggregate" or "QTcB Interval, Aggregate" is derived by the sponsor, the derived flag (EGDRVFL) is set to "Y". However, when the "QTcF Interval, Aggregate" or "QTcB Interval, Aggregate" is received from a central provider or vendor, the value would go into EGORRES and EGDRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).

10. If this domain is used in conjunction with the ECG QT Correction Model Data (QT) domain:
    a. For each QT correction method used in the study, values of EGTESTCD and EGTEST are assigned at the study level.
    b. The sponsor should assign values for EGTESTCD/EGTEST appropriately with clear documentation on what each test code represents. For example, if the protocol calls for computing the top two best fit models, the sponsor could choose to name the top best fit model QTCIAG1 and the second best fit model QTCIAG2, in rank order.

11. Any identifiers, timing variables, or findings general observation-class qualifiers may be added to the EG domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --SPEC, --SPCCND, --FAST, --SEV. It is recommended that --LOINC not be used.

<!-- source: knowledge_base/domains/EX/spec.md -->
# EX — Exposure

> Class: Interventions | Structure: One record per protocol-specified study treatment, constant-dosing interval, per subject

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

### EXSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### EXGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### EXREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier (e.g., kit number, bottle label, vial identifier).

### EXSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF page.

### EXLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains.

### EXLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related, grouped records across domains.

### EXTRT
- **Order:** 10
- **Label:** Name of Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Name of the protocol-specified study treatment given during the dosing period for the observation.

### EXCAT
- **Order:** 11
- **Label:** Category of Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of EXTRT values.

### EXSCAT
- **Order:** 12
- **Label:** Subcategory of Treatment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of EXCAT values.

### EXDOSE
- **Order:** 13
- **Label:** Dose
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Amount of EXTRT when numeric. Not populated when EXDOSTXT is populated.

### EXDOSTXT
- **Order:** 14
- **Label:** Dose Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of EXTRT when non-numeric. Dosing amounts or a range of dosing information collected in text form. Example: "200-400". Not populated when EXDOSE is populated.

### EXDOSU
- **Order:** 15
- **Label:** Dose Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Units for EXDOSE, EXDOSTOT, or EXDOSTXT representing protocol-specified values. Examples: "ng", "mg", "mg/kg", "mg/m2".

### EXDOSFRM
- **Order:** 16
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Dose form for EXTRT. Examples: "TABLET", "LOTION".

### EXDOSFRQ
- **Order:** 17
- **Label:** Dosing Frequency per Interval
- **Type:** Char
- **Controlled Terms:** C71113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Usually expressed as the number of repeated administrations of EXDOSE within a specific time period. Examples: "Q2H", "QD", "BID".

### EXDOSRGM
- **Order:** 18
- **Label:** Intended Dose Regimen
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the intended schedule or regimen for the Intervention. Example: "TWO WEEKS ON, TWO WEEKS OFF".

### EXROUTE
- **Order:** 19
- **Label:** Route of Administration
- **Type:** Char
- **Controlled Terms:** C66729
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Route of administration for the intervention. Examples: "ORAL", "INTRAVENOUS".

### EXLOT
- **Order:** 20
- **Label:** Lot Number
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Lot number of the intervention product.

### EXLOC
- **Order:** 21
- **Label:** Location of Dose Administration
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Specifies location of administration. Examples: "ARM", "LIP".

### EXLAT
- **Order:** 22
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing laterality of the intervention administration. Examples: "LEFT", "RIGHT".

### EXDIR
- **Order:** 23
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL", "UPPER".

### EXFAST
- **Order:** 24
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status. Examples: "Y", "N".

### EXADJ
- **Order:** 25
- **Label:** Reason for Dose Adjustment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes reason or explanation of why a dose is adjusted.

### TAETORD
- **Order:** 26
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 27
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Trial epoch of the exposure record. Examples: "RUN-IN", "TREATMENT".

### EXSTDTC
- **Order:** 28
- **Label:** Start Date/Time of Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** The date/time when administration of the treatment indicated by EXTRT and EXDOSE began.

### EXENDTC
- **Order:** 29
- **Label:** End Date/Time of Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** The date/time when administration of the treatment indicated by EXTRT and EXDOSE ended. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, EXSTDTC should be copied to EXENDTC as the standard representation.

### EXSTDY
- **Order:** 30
- **Label:** Study Day of Start of Treatment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of EXSTDTC relative to DM.RFSTDTC.

### EXENDY
- **Order:** 31
- **Label:** Study Day of End of Treatment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of EXENDTC relative to DM.RFSTDTC.

### EXDUR
- **Order:** 32
- **Label:** Duration of Treatment
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of administration. Used only if collected on the CRF and not derived from start and end date/times.

### EXTPT
- **Order:** 33
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when administration should occur. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See EXTPTNUM and EXTPTREF.

### EXTPTNUM
- **Order:** 34
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of EXTPT to aid in sorting.

### EXELTM
- **Order:** 35
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to the planned fixed reference (EXTPTREF). This variable is useful where there are repetitive measures. Not a clock time.

### EXTPTREF
- **Order:** 36
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by EXELTM, EXTPTNUM, and EXTPT. Examples: PREVIOUS DOSE, PREVIOUS MEAL.

### EXRFTDTC
- **Order:** 37
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by EXTPTREF.
---

## Cross References

### Controlled Terminology
- [Pharmaceutical Dosage Form (C66726)](../../terminology/core/interventions.md) — EXDOSFRM
- [Route of Administration Response (C66729)](../../terminology/core/interventions.md) — EXROUTE
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — EXFAST
- [Frequency (C71113)](../../terminology/core/interventions.md) — EXDOSFRQ
- [Unit (C71620)](../../terminology/core/general_part5.md) — EXDOSU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — EXLOC
- [Laterality (C99073)](../../terminology/core/general_part2.md) — EXLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — EXDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Interventions):** AG, CM, EC, ML, PR, SU
- **Shared Dataset:** [EC](../EC/) — exposure vs exposure as collected

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Interventions class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/EX/assumptions.md -->
# EX — Assumptions

1. EX structure and use
   a. Examples of treatments represented in the EX domain include but are not limited to placebo, active comparators, and investigational products. Treatments that are not protocol-specified should be represented in the Concomitant/Prior Medications (CM) or another Interventions domain as appropriate.
   b. The EX domain is recognized in most cases as a derived dataset where EXDOSU reflects the protocol-specified unit per study treatment. Collected data points (e.g., number of tablets, total volume infused) along with additional inputs (e.g., randomization file, concentration, dosage strength, product accountability) are used to derive records in the EX domain.
   c. The EX domain is required for all studies that include protocol-specified study treatment. Exposure records may be directly or indirectly determined; metadata should describe how the records were derived. Common methods for determining exposure (from most direct to least direct) include the following:
      i. Derived from actual observation of the administration of drug by the investigator
      ii. Derived from automated dispensing device that records administrations
      iii. Derived from subject recall
      iv. Derived from product accountability data
      v. Derived from the protocol. When a study is still masked and protocol-specified study treatment doses cannot yet be reflected in the protocol-specified unit due to blinding requirements, then the EX domain is not expected to be populated.
   d. The EX domain should contain 1 record per constant-dosing interval per subject. Sponsors define the constant-dosing interval, which may include any period of time that can be described in terms of a known treatment given at a consistent dose, frequency, infusion rate, and so on. For example, for a study with once-a-week administration of a standard dose for 6 weeks, exposure may be represented as:
      i. a single record per subject, spanning the entire 6-week treatment phase, if information about each dose is not collected; or
      ii. up to 6 records (1 for each weekly administration), if the sponsor monitors each treatment administration.

2. Exposure treatment description
   a. EXTRT captures the name of the protocol-specified study treatment and is the topic variable. It is a required variable and must have a value. EXTRT must include only the treatment name and must not include dosage, formulation, or other qualifying information. For example, "ASPIRIN 100MG TABLET" is not a valid value for EXTRT. This example should be expressed as EXTRT = "ASPIRIN", EXDOSE = "100", EXDOSU = "mg", and EXDOSFRM = "TABLET".
   b. Doses of placebo should be represented by EXTRT = "PLACEBO" and EXDOSE = "0" (indicating 0 mg of active ingredient was taken or administered).

3. Categorization and grouping
   a. EXCAT and EXSCAT may be used when appropriate to categorize treatments into categories and subcategories. For example, if a study contains several active comparator medications, EXCAT may be set to "ACTIVE COMPARATOR". Such categorization may not be useful in all studies, so these variables are permissible.

4. Timing variables
   a. The timing of exposure to study treatment is captured by the start/end date and start/end time of each constant-dosing interval. If the subject is only exposed to study medication within a clinical encounter (e.g., if an injection is administered at the clinic), VISITNUM may be added to the domain as an additional timing variable. VISITDY and VISIT would then also be permissible qualifiers. However, if the beginning and end of a constant-dosing interval is not confined within the time limits of a clinical encounter (e.g., if a subject takes pills at home), then it is not appropriate to include VISITNUM in the EX domain. This is because EX is designed to capture the timing of exposure to treatment, not the timing of dispensing treatment. Further, VISITNUM should not be used to indicate that treatment began at a particular visit and continued for a period of time. The SDTM does not have any provision for recording "start visit" and "end visit" of exposure.
   b. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, EXSTDTC should be copied to EXENDTC as the standard representation.

5. Collected exposure data points are to be represented in the Exposure as Collected (EC) domain. When the relationship between EC and EX records can be described in RELREC, then it should be defined. EX derivations must be described in the Define-XML document.

6. Additional interventions qualifiers
   a. EX contains medications received; the inclusion of administrations not taken, not given, or missed is under evaluation. Because EX includes only treatments received, --MOOD would generally not be used in EX.
   b. --DOSTOT is under evaluation for potential deprecation and replacement with a mechanism to describe total dose over any interval of time (e.g., day, week, month). Sponsors considering use of EXDOSTOT may want to consider using other dose-amount variables (EXDOSE or EXDOSTXT) in combination with frequency (EXDOSFRQ) and timing variables to represent the data.
   c. When the EC domain is implemented in conjunction with the EX domain, EXVAMT and EXVAMTU would not be used in EX; collected values instead would be represented in ECDOSE and ECDOSU (and ECVAMT and ECVAMTU as needed).
   d. Any identifier variables, timing variables, or findings general observation-class qualifiers may be added to the EX domain, but the following qualifiers would generally not be used: --PRESP, --OCCUR, --STAT, and --REASND.

<!-- source: knowledge_base/domains/FA/spec.md -->
# FA — Findings About Events or Interventions

> Class: Findings About | Structure: One record per finding, per object, per time point, per visit per subject

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

### FASEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### FAGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### FASPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a CRF.

### FATESTCD
- **Order:** 7
- **Label:** Findings About Test Short Name
- **Type:** Char
- **Controlled Terms:** C101832
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in FATEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in FATESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FATESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SEV", "OCCUR". Note that controlled terminology is in a FATESTCD general codelist and in several therapeutic area-specific codelists.

### FATEST
- **Order:** 8
- **Label:** Findings About Test Name
- **Type:** Char
- **Controlled Terms:** C101833
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in FATEST cannot be longer than 40 characters. Examples: "Severity/Intensity", "Occurrence". Note that controlled terminology is in a FATEST general codelist and in several therapeutic area-specific codelists.

### FAOBJ
- **Order:** 9
- **Label:** Object of the Observation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the term (e.g., "Acne") describing a clinical sign or symptom that is being measured by a severity test; an event (e.g., "VOMIT, where the volume of vomit is being measured by a VOLUME test).

### FACAT
- **Order:** 10
- **Label:** Category for Findings About
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records. Examples: "GERD", "PRE-SPECIFIED AE".

### FASCAT
- **Order:** 11
- **Label:** Subcategory for Findings About
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of FACAT.

### FAORRES
- **Order:** 12
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the test as originally received or collected.

### FAORRESU
- **Order:** 13
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for FAORRES.

### FASTRESC
- **Order:** 14
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from FAORRES in a standard format or standard units. FASTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FASTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in FAORRES, and these results effectively have the same meaning; they could be represented in standard format in FASTRESC as "NEGATIVE".

### FASTRESN
- **Order:** 15
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from FASTRESC. FASTRESN should store all numeric test results or findings.

### FASTRESU
- **Order:** 16
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for FASTRESC and FASTRESN.

### FASTAT
- **Order:** 17
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that the measurement was not done. Should be null if a result exists in FAORRES.

### FAREASND
- **Order:** 18
- **Label:** Reason Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a question was not answered. Example: "Subject refused". Used in conjunction with FASTAT when value is "NOT DONE".

### FALOC
- **Order:** 19
- **Label:** Location of the Finding About
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to specify the location of the clinical evaluation. Example: "ARM".

### FALAT
- **Order:** 20
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### FALOBXFL
- **Order:** 21
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### FABLFL
- **Order:** 22
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null. Note that FABLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### FAEVAL
- **Order:** 23
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR".

### VISITNUM
- **Order:** 24
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** 1. Clinical encounter number.  2. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 25
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** 1. Protocol-defined description of clinical encounter.  2. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 26
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 27
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 28
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP".

### FADTC
- **Order:** 29
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of findings assessment represented in ISO 8601 character format.

### FADY
- **Order:** 30
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** 1. Study day of collection, measured as integer days.  2. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.
---

## Cross References

### Controlled Terminology
- [Findings About Test Code (C101832)](../../terminology/core/findings_about.md) — FATESTCD
- [Findings About Test Name (C101833)](../../terminology/core/findings_about.md) — FATEST
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — FALOBXFL, FABLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — FASTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — FAORRESU, FASTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — FALOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — FAEVAL
- [Laterality (C99073)](../../terminology/core/general_part2.md) — FALAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings About):** SR
- **Source Domain:** [AE](../AE/) — findings about adverse events
- **Source Domain:** [CM](../CM/) — findings about concomitant medications
- **Source Domain:** [PR](../PR/) — findings about procedures
- **Source Domain:** [EX](../EX/) — findings about exposure
- **Source Domain:** [EC](../EC/) — findings about exposure as collected
- **Source Domain:** [ML](../ML/) — findings about meals
- **Source Domain:** [SU](../SU/) — findings about substance use

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings About class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/FA/assumptions.md -->
# FA — Assumptions

1. The Findings About domain shares all qualities and conventions of findings observations.

2. See Section 6.4.1, When to Use Findings About Events or Interventions; and Section 8.6.3, Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions; for guidance on deciding between the use of the FA domain and other SDTM structures.

3. See Section 6.4.2, Naming Findings About Domains, for advice on splitting the FA domain.

4. Some variables in the events and interventions domains (e.g., OCCUR, SEV, TOXGR) represent findings about the whole of the event or intervention. When FA is used to represent findings about a part of the event or intervention (i.e., the assessment has different timing from the event as a whole), the FATEST and FATESTCD values should be the same as the variable name and variable label in the corresponding event or intervention domain. See Section 6.4.3, Variables Unique to Findings About.
   a. Associations between some findings about cardiovascular interventions or events and their response codelists are described in the CV codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

5. When data collection establishes a relationship between FA records and an events or interventions record, the relationship should be represented in RELREC.
   a. The FAOBJ variable alone is not sufficient to establish a relationship, because an events or interventions dataset may have multiple records for the same topic (e.g., --TERM or --DECOD, --TRT or --DECOD).

6. Any Identifier variables, Timing variables, or Findings general observation-class qualifiers may be added to the FA domain, but the following qualifiers should generally not be used: --BODSYS, --MODIFY, --SEV, --TOXGR.

<!-- source: knowledge_base/domains/FT/spec.md -->
# FT — Functional Tests

> Class: Findings | Structure: One record per Functional Test finding per time point per visit per subject

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

### FTSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number.

### FTGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### FTREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier.

### FTSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the Test page.

### FTTESTCD
- **Order:** 8
- **Label:** Short Name of Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for FTTEST, which can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). FTTESTCD cannot contain characters other than letters, numbers, or underscores.  Controlled terminology for FTTESTCD is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTESTCD. Examples: "W250101", "W25F0102".

### FTTEST
- **Order:** 9
- **Label:** Name of Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the question used to obtain the finding. The value in FTTEST cannot be longer than 40 characters.  Controlled terminology for FTTEST is published in separate codelists for each instrument. See https://www.cdisc.org/standards/terminology/controlled-terminology for values for FTTEST. Examples: "W2501-25 Foot Walk Time", "W25F-More Than Two Attempts".

### FTCAT
- **Order:** 10
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** C115304
- **Role:** Grouping Qualifier
- **Core:** Req
- **CDISC Notes:** Used to specify the functional test in which the functional test question identified by FTTEST and FTTESTCD was included.

### FTSCAT
- **Order:** 11
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of FTCAT values.

### FTPOS
- **Order:** 12
- **Label:** Position of Subject During Observation
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during the test. Examples: "SUPINE", "STANDING", "SITTING".

### FTORRES
- **Order:** 13
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### FTORRESU
- **Order:** 14
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. Unit for FTORRES.

### FTSTRESC
- **Order:** 15
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from FTORRES in a standard format or in standard units. FTSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in FTSTRESN.

### FTSTRESN
- **Order:** 16
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from FTSTRESC. FTSTRESN should store all numeric test results or findings.

### FTSTRESU
- **Order:** 17
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for FTSTRESC and FTSTRESN.

### FTSTAT
- **Order:** 18
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### FTREASND
- **Order:** 19
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a test was not done, or a test was attempted but did not generate a result. Used in conjunction with FTSTAT when value is "NOT DONE".

### FTXFN
- **Order:** 20
- **Label:** External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** File path to an external file.

### FTNAM
- **Order:** 21
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor or laboratory that provided the test results.

### FTMETHOD
- **Order:** 22
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C158113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination.

### FTLOBXFL
- **Order:** 23
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### FTBLFL
- **Order:** 24
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** A baseline defined by the sponsor (could be derived in the same manner as FTLOBXFL or ABLFL, but is not required to be). The value should be "Y" or null. Note that FTBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### FTDRVFL
- **Order:** 25
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### FTREPNUM
- **Order:** 26
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.

### VISITNUM
- **Order:** 27
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
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
- **CDISC Notes:** Planned study day of VISIT based upon RFSTDTC in Demographics. Should be an integer.

### TAETORD
- **Order:** 30
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 31
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the observation date/time of the functional tests finding.

### FTDTC
- **Order:** 32
- **Label:** Date/Time of Test
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of functional test.

### FTDY
- **Order:** 33
- **Label:** Study Day of Test
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of test expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### FTTPT
- **Order:** 34
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken, as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See FTTPTNUM and FTTPTREF.

### FTTPTNUM
- **Order:** 35
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### FTELTM
- **Order:** 36
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (FTTPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### FTTPTREF
- **Order:** 37
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by FTELTM, FTTPTNUM, and FTTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### FTRFTDTC
- **Order:** 38
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by FTTPTREF.
---

## Cross References

### Controlled Terminology
- [Category of Functional Test (C115304)](../../terminology/core/other_part1.md) — FTCAT
- [QRS Method (C158113)](../../terminology/core/general_part4.md) — FTMETHOD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — FTLOBXFL, FTBLFL, FTDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — FTSTAT
- [Position (C71148)](../../terminology/core/interventions.md) — FTPOS
- [Unit (C71620)](../../terminology/core/general_part5.md) — FTORRESU, FTSTRESU
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/FT/assumptions.md -->
# FT — Assumptions

The following assumptions are unique to the FT domain:

1. A functional test is not a subjective assessment of how the subject generally performs a task, but rather an objective measurement of the performance of the task by the subject in a specific instance.

2. Functional tests have documented methods for administration and analysis and require a subject to perform specific activities that are evaluated and recorded. Most often, functional tests are direct quantitative measurements. Examples of functional tests include the Timed 25-Foot Walk, 9-Hole Peg Test, and the Hauser Ambulation Index.

## QRS Shared Assumptions

The following assumptions are common to the FT and QS domains as well as the Clinical Classifications use case of the RS domain (not the Disease Response use case of RS):

1. The name of a QRS instrument is described under the variable --CAT in the relevant QRS domain (i.e., FT, QS, RS), and may be either abbreviations or longer names. For example, "ADAS-COG", "BPI SHORT FORM", and "APACHE II" are all --CATs which are shortened names for the instruments they represent, whereas "4 STAIR ASCEND" is the FTCAT for the instrument of the same name. Sponsors should always reference CDISC Controlled Terminology.
   a. The QRS Naming Rules for --CAT, --TEST, and --TESTCD and the list of QRS instruments that have published CDISC Controlled Terminology with NCI/EVS are available at: https://www.cdisc.org/standards/terminology/controlled-terminology.
   b. Refer to the following CDISC Controlled Terminology codelists for QRS instrument --CAT terminology:
      i. Category of Clinical Classification
      ii. Category of Functional Test
      iii. Category of Questionnaire
   c. QRS --TESTCD/--TEST terminology codelists are listed separately by instrument name.

2. Names of subcategories for groups of items/questions are described under the --SCAT variable.
   a. --SCAT values are not included in the CDISC Controlled Terminology system but rather controlled as described in the QRS supplements in which they are used.

3. There are cases where QRS CRFs do not include numeric "standardized responses" assigned to text responses (e.g., mild, moderate, severe being 1, 2, 3). It is clearly in everyone's best interest to include the numeric "standardized responses" in the SDTMIG QRS dataset. This is only done when the numeric "standardized responses" are documented in the QRS CRF instructions, a user manual, a website specific to the QRS instrument, or another reference document that provides a clear explanation and rationale for providing them in the SDTMIG QRS dataset.

4. Sponsors should always consult published QRS supplements for guidance on submitting derived information in a SDTMIG QRS domain. Derived variable results in QRS are usually considered captured data. If sponsors operationally derive variable results, then the derived records that are submitted in a QRS domain should be flagged by --DRVFL.
   a. The following rules apply for "total"-type scores in QRS datasets.
      i. QRS subtotal, total, etc. scores listed on the CRF are considered captured data and are included in the instrument's controlled terminology.
      ii. QRS subtotal, total, etc. scores not listed on the CRF but documented in an associated instrument manual or reference paper are considered captured data and are included in the instrument's controlled terminology.
      iii. QRS subtotal, total, etc. scores not listed on the CRF, but known to be included in eData by sponsors are considered as captured data, are included in the instrument's controlled terminology. The QRS instrument's CT is considered extensible for this case and the subtotal or total score should be requested to be added.
         1. Any imputations/calculations done to numeric "standardized responses" to produce the total score via transforming numeric "standardized responses" in any way would be done as ADaM derivations.
   b. The QRS instrument subtotal or total score, which is the sum of the numeric responses for an instrument, is populated in --ORRES, --STRESC, and --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor-data management processes related to the score.
      i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).

5. The variable --REPNUM variable is populated when there are multiple repeats of the same question. When records are related to the first trial of the question, the variable --REPNUM should be set to "1". When records are related to the second trial of the same question, --REPNUM should be set to "2", and so forth.

6. The actual version number of an instrument is represented in the --CAT value as designated by the QRS Terminology Team. If it is determined that this is not the case for an instrument:
   a. Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing a resolution on how the situation will be handled.
   b. Consider the use of the --GRPID variable to indicate the instrument's version number prior to a decision by the QRS Terminology Team.
   c. The sponsor is expected to provide information about the version used for each QRS instrument in the metadata (using the Comments column in the Define-XML document). This could be provided as value-level metadata for --CAT.
   d. The sponsor is expected to provide information about the scoring rules in the metadata.

7. If the variable --TEST is represented with verbatim text >40 characters, represent the abbreviated meaningful text in --TEST within 40 characters and describe the full text of the item in the study metadata. If the verbatim item response (e.g., --QSORRES) is >200 characters, represent the abbreviated meaningful text in QSORRES within the 200 characters and describe the full text in the study metadata; see Section 4 of the QRS supplement. See Section 4.5.3, Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables, for further information.
   a. The instrument's annotated CRF can also be used as a reference for the full text in both of these situations.

8. --EVAL and --EVALID must not be used to model QRS data in SDTM. These variables have had various interpretations on QRS CRFs and were used to represent a multitude of evaluator information about QRS instruments. This has made it more difficult for users of SDTM QRS data to interpret this data and more difficult to pool data for analyses. If needed, supplemental qualifiers may be used to represent this data. Updated information on a proposed solution to this issue will be posted on the CDISC QRS webpage (https://www.cdisc.org/standards/foundational/qrs).

9. All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the controlled terminology and defining instrument-specific standardized values for qualifier, timing, and result variables to populate the SDTMIG FT, QS, and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always consult the CDISC website to review the terminology and supplements prior to modeling any QRS instrument.
   a. Sponsors may participate and/or request the development of additional QRS supplements and terminology through the CDISC SDS QRS subteam and the Controlled Terminology QRS subteam.
      i. Once generated, the QRS supplement is posted on the CDISC website (https://www.cdisc.org/standards/foundational/qrs).
      ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.

10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/GF/spec.md -->
# GF — Genomics Findings

> Class: Findings | Structure: One record per finding per observation per biospecimen per subject

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
- **CDISC Notes:** Sponsor-defined identifier for a device.

### NHOID
- **Order:** 5
- **Label:** Non-Host Organism Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.

### GFSEQ
- **Order:** 6
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### GFGRPID
- **Order:** 7
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain.

### GFREFID
- **Order:** 8
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** A unique identifier for the assayed genetic specimen.

### GFSPID
- **Order:** 9
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### GFLNKID
- **Order:** 10
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### GFLNKGRP
- **Order:** 11
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### GFTESTCD
- **Order:** 12
- **Label:** Short Name of Genomic Measurement
- **Type:** Char
- **Controlled Terms:** C181178
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in GFTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in GFTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). GFTESTCD cannot contain characters other than letters, numbers, or underscores.

### GFTEST
- **Order:** 13
- **Label:** Name of Genomic Measurement
- **Type:** Char
- **Controlled Terms:** C181179
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for GFTESTCD. The value in GFTEST cannot be longer than 40 characters.

### GFTSTDTL
- **Order:** 14
- **Label:** Measurement, Test, or Examination Detail
- **Type:** Char
- **Controlled Terms:** C181180
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of a reportable qualifying the assessment in GFTESTCD and GFTEST.

### GFCAT
- **Order:** 15
- **Label:** Category for Genomic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values.

### GFSCAT
- **Order:** 16
- **Label:** Subcategory for Genomic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of GFCAT values.

### GFORRES
- **Order:** 17
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### GFORRESU
- **Order:** 18
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for GFORRES.

### GFORREF
- **Order:** 19
- **Label:** Reference Result in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for the result or finding as originally received or collected. GFORREF uses the same units as GFORRES, if applicable.

### GFSTRESC
- **Order:** 20
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from GFORRES, in a standard format or in standard units. GFSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in GFSTRESN.

### GFSTRESN
- **Order:** 21
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from GFSTRESC. GFSTRESN should store all numeric test results or findings.

### GFSTRESU
- **Order:** 22
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for GFSTRESC, GFSTRESN, GFSTREFC, and GFSTREFN.

### GFSTREFC
- **Order:** 23
- **Label:** Reference Result in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for the result or finding copied or derived from GFORREF in a standard format.

### GFSTREFN
- **Order:** 24
- **Label:** Numeric Reference Result in Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for continuous or numeric results or findings in standard format or in standard units. GFSTREFN uses the same units as GFSTRESN, if applicable.

### GFRESCAT
- **Order:** 25
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding.

### GFINHERT
- **Order:** 26
- **Label:** Inheritability
- **Type:** Char
- **Controlled Terms:** C181177
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies whether the variation can be passed to the next generation.

### GFGENREF
- **Order:** 27
- **Label:** Genome Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** An identifier for the genome reference used to generate the reported result. For example, Genome Reference Consortium Human Build 38 patch release 13 may be represented as "GRCh38.p13".

### GFCHROM
- **Order:** 28
- **Label:** Chromosome Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The designation (name or number) of the chromosome or contig on which the variant or other feature appears (e.g., "17"; "X").

### GFSYM
- **Order:** 29
- **Label:** Genomic Symbol
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A published symbol for the portion of the genome serving as a locus for the experiment/test.

### GFSYMTYP
- **Order:** 30
- **Label:** Genomic Symbol Type
- **Type:** Char
- **Controlled Terms:** C181176
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A description of the type of genomic entity that is represented by the published symbol in GFSYM.

### GFGENLOC
- **Order:** 31
- **Label:** Genetic Location
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Specifies the location within a sequence for the observed value in GFORRES.

### GFGENSR
- **Order:** 32
- **Label:** Genetic Sub-Region
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The portion of the locus in which the variation was found. Examples: "Exon 15", "Kinase domain".

### GFSEQID
- **Order:** 33
- **Label:** Sequence Identifier 
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A unique identifier for the sequence used as the reference to identify the genetic variation in the result. Examples: "NM_001234", "ENSG00000182533", "ENST00000343849.2".

### GFPVRID
- **Order:** 34
- **Label:** Published Variant Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A unique identifier for the variation that has been publicly characterized in an external database. Examples: "rs2231142", "COSM41596".

### GFCOPYID
- **Order:** 35
- **Label:** Copy Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** An arbitrary identifier used to differentiate between copies of a genetic target of interest present on homologous chromosomes.

### GFSTAT
- **Order:** 36
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### GFREASND
- **Order:** 37
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with GFSTAT when value is "NOT DONE".

### GFXFN
- **Order:** 38
- **Label:** External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The filename and/or path to external data not stored in the same format and possibly not the same location as the other data for a study.

### GFNAM
- **Order:** 39
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor that provided the test result. When more than 1 vendor is involved in the generation of the result, additional vendors should be represented as supplemental qualifiers.

### GFSPEC
- **Order:** 40
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C111114
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies the type of genetic material used for the measurement.

### GFMETHOD
- **Order:** 41
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** The test method by which the examination is performed by the wet lab in order to yield the result reported in the dataset.

### GFRUNID
- **Order:** 42
- **Label:** Run ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** A unique identifier for a particular run of a test performed by the wet lab on a particular batch of samples. This identifier can be used to distinguish between records for the same test performed at different times.

### GFANMETH
- **Order:** 43
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** C181181
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The method of secondary processing performed by the dry lab to yield the result reported in the dataset.

### GFBLFL
- **Order:** 44
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null.

### GFDRVFL
- **Order:** 45
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### GFLLOQ
- **Order:** 46
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units will be those used for GFSTRESU.

### GFREPNUM
- **Order:** 47
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The instance number of a test that is repeated within a given timeframe for the same test performed by the wet lab.

### VISITNUM
- **Order:** 48
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 49
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter.

### VISITDY
- **Order:** 50
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### GFDTC
- **Order:** 51
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of specimen collection.

### GFDY
- **Order:** 52
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### GFTPT
- **Order:** 53
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See GFTPTNUM and GFTPTREF.

### GFTPTNUM
- **Order:** 54
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of GFTPT used in sorting.

### GFELTM
- **Order:** 55
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Elapsed time relative to a planned fixed reference (GFTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable, but an interval, represented as ISO duration.

### GFTPTREF
- **Order:** 56
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by GFELTM, GFTPTNUM, and GFTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### GFRFTDTC
- **Order:** 57
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by GFTPTREF.
---

## Cross References

### Controlled Terminology
- [Genetic Sample Type (C111114)](../../terminology/core/general_part2.md) — GFSPEC
- [Genomic Symbol Type Response (C181176)](../../terminology/core/gf.md) — GFSYMTYP
- [Genomic Inheritability Type Response (C181177)](../../terminology/core/gf.md) — GFINHERT
- [Genomic Findings Test Code (C181178)](../../terminology/core/gf.md) — GFTESTCD
- [Genomic Findings Test Name (C181179)](../../terminology/core/gf.md) — GFTEST
- [Genomic Findings Test Detail (C181180)](../../terminology/core/gf.md) — GFTSTDTL
- [Genomic Findings Analytical Method Calculation Formula (C181181)](../../terminology/core/gf.md) — GFANMETH
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — GFBLFL, GFDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — GFSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — GFORRESU, GFSTRESU
- [Method (C85492)](../../terminology/core/general_part3.md) — GFMETHOD

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Related Findings:** [IS](../IS/) — genomics/genetics vs immunogenicity

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/GF/assumptions.md -->
# GF — Assumptions

1. The Genomics Findings domain is used to represent findings related to the structure, function, evolution, mapping, and editing of subject and non-host organism genomic material of interest. This domain includes but is not limited to assessments and results for genetic variation and transcription, and summary measures derived from these assessments. The GF domain is used for findings from characteristics assessed from nucleic acids and may include subsequent inferences and/or predictions about related proteins/amino acids. However, direct assessments of proteins (e.g., assessments of amino acids) are out of scope for this domain.

2. Regarding genetic testing on non-host organisms (including but not limited to bacteria, viruses, and parasites), the following additional assumptions apply:
   a. Tests that give genetic results (e.g., expressed in terms of genetic variation, specific sequence information) on non-host organisms that have been identified in subject samples should be represented in GF. To distinguish these findings from subject genetic data, the variable NHOID must be populated to identify the non-host organism as the focus of the record (see Section 9.2, Non-host Organism Identifiers, assumption 2 for more information).
   b. If the purpose of the test is to detect or determine the identity of a viable, non-host organism or infectious agent in a subject sample, data should be represented in the Microbiology Specimen (MB) domain.
   c. Tests that are used to determine the resistance/susceptibility of a non-host organism to a drug on a genetic basis should be represented in the Microbiology Susceptibility (MS) domain.
   d. If the test provides both genetic data and susceptibility/resistance data, genetic data should be represented in GF and the susceptibility/resistance data should be represented in the MS domain (See Section 6.3.5.7.2, Microbiology Susceptibility, assumption 1b for more information).

3. The platform used to detect the finding may be represented in SPDEVID. Attributes used in conjunction with a platform (e.g., assay panel, reagents) may be represented in the Device Identifiers (DI) domain and other associated device domains. See the SDTM Implementation Guide for Medical Devices (SDTMIG-MD) for further information about SPDEVID and the device domains.

4. Values populated in GFCAT and GFSCAT are sponsor-defined and there is no CDISC Controlled Terminology for these variables.

5. Genomic symbols are represented in GFSYM.
   a. GFTESTCD and GFTEST should not include genomic names or symbols, including but not limited to official gene symbols.
   b. For human genetic data, standard nomenclature populated in variable GFSYM must be obtained from the genomic symbol list maintained in the HUGO Gene Nomenclature Committee (HGNC) database (www.genenames.org).

6. When populating GFGENSR, caution should be exercised for annotations of loci where more than 1 annotation applies. In such cases, the source of the annotation should be captured and documented in Define-XML. In addition, the value populated in GFGENSR may be dependent on the precision of the value populated in GFSEQID.

7. Values populated in GFGENREF, GFSEQID, and GFPVRID should reflect the level of granularity collected (e.g., version, build, patch, release) to support interpretation of the reported result.

8. GFMETHOD lists wet lab techniques for the execution of genomics or genetic testing. Methods related to specimen processing or reagents are not represented in GFMETHOD.

9. The following variables generally would not be used in GF: --POS, --BODSYS, --ORNRLO, ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --CHRON, --DISTR, --ANTREG, --LOC, --LAT, --DIR, --PORTOT, --LEAD, --CSTATE, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/HO/spec.md -->
# HO — Healthcare Encounters

> Class: Events | Structure: One record per healthcare encounter per subject

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

### HOSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### HOGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### HOREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external healthcare encounter identifier.

### HOSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Healthcare Encounters CRF page.

### HOTERM
- **Order:** 8
- **Label:** Healthcare Encounter Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim or preprinted CRF term for the healthcare encounter.

### HODECOD
- **Order:** 9
- **Label:** Dictionary-Derived Term
- **Type:** Char
- **Controlled Terms:** C171444
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary or sponsor-defined derived text description of HOTERM or the modified topic variable (HOMODIFY).

### HOCAT
- **Order:** 10
- **Label:** Category for Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-related values.

### HOSCAT
- **Order:** 11
- **Label:** Subcategory for Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of HOCAT values.

### HOPRESP
- **Order:** 12
- **Label:** Pre-Specified Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A value of "Y" indicates that this healthcare encounter event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms).

### HOOCCUR
- **Order:** 13
- **Label:** Healthcare Encounter Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when the occurrence of specific healthcare encounters is solicited, to indicate whether an encounter occurred. Values are null for spontaneously reported events.

### HOSTAT
- **Order:** 14
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The status indicates that the prespecified question was not answered.

### HOREASND
- **Order:** 15
- **Label:** Reason Healthcare Encounter Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason data for a prespecified event were not collected. Used in conjunction with HOSTAT when value is "NOT DONE".

### TAETORD
- **Order:** 16
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 17
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the healthcare encounter. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP".

### HODTC
- **Order:** 18
- **Label:** Date/Time of Event Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the healthcare encounter.

### HOSTDTC
- **Order:** 19
- **Label:** Start Date/Time of Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of the healthcare encounter (e.g., date of admission).

### HOENDTC
- **Order:** 20
- **Label:** End Date/Time of Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the healthcare encounter (e.g., date of discharge).

### HODY
- **Order:** 21
- **Label:** Study Day of Event Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of event collection relative to the sponsor-defined RFSTDTC.

### HOSTDY
- **Order:** 22
- **Label:** Study Day of Start of Encounter
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the start of the healthcare encounter relative to the sponsor-defined RFSTDTC.

### HOENDY
- **Order:** 23
- **Label:** Study Day of End of Healthcare Encounter
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the end of the healthcare encounter relative to the sponsor-defined RFSTDTC.

### HODUR
- **Order:** 24
- **Label:** Duration of Healthcare Encounter
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of the healthcare encounter. Used only if collected on the CRF and not derived from the start and end date/times. Example: "P1DT2H" (for 1 day, 2 hours).

### HOSTRTPT
- **Order:** 25
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable --STTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### HOSTTPT
- **Order:** 26
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by STRTPT. Examples: "2003-12-15", "VISIT 1".

### HOENRTPT
- **Order:** 27
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the event as being before or after the reference time point defined by variable HOENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### HOENTPT
- **Order:** 28
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by HOENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Health Care Encounters Dictionary Derived Term (C171444)](../../terminology/core/other_part1.md) — HODECOD
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — HOSTRTPT, HOENRTPT
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — HOPRESP, HOOCCUR
- [Not Done (C66789)](../../terminology/core/general_part4.md) — HOSTAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Events):** AE, BE, CE, DS, DV, MH
- **Event:** [DS](../DS/) — healthcare encounters relate to disposition

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Events class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/HO/assumptions.md -->
# HO — Assumptions

1. The Healthcare Encounters (HO) dataset includes inpatient and outpatient healthcare events (e.g., hospitalizations, nursing home stays, rehabilitation facility stays, ambulatory surgery).

2. Values of HOTERM typically describe the location or place of the healthcare encounter (e.g., "HOSPITAL" rather than "HOSPITALIZATION"). HOSTDTC should represent the start or admission date and HOENDTC the end or discharge date.

3. Data collected about healthcare encounters may include the reason for the encounter. The following supplemental qualifiers may be appropriate for representing such data:
   a. The supplemental qualifier with QNAM = "HOINDC" would be used to represent the indication/medical condition for the encounter (e.g., stroke). Note that --INDC is an Interventions class variable, so is not a standard variable for HO, which is an Events class domain.
   b. The supplemental qualifier with QNAM = "HOREAS" would be used to represent a reason for the encounter other than a medical condition (e.g., annual checkup).

4. If collected data includes the name of the provider or the facility where the encounter took place, this may be represented using the supplemental qualifier with QNAM = "HONAM". Note that --NAM is a Findings class variable, so is not a standard variable for HO, which is an Events class domain.

5. Any identifier variables, timing variables, or Events general observation-class qualifiers may be added to the HO domain, but the following Qualifiers would generally not be used: --SER, --ACN, --ACNOTH, --REL, --RELNST, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --BODSYS, --LOC, --SEV, --TOX, --TOXGR, --PATT, --CONTRT.

<!-- source: knowledge_base/domains/IE/spec.md -->
# IE — Inclusion/Exclusion Criteria Not Met

> Class: Findings | Structure: One record per inclusion/exclusion criterion not met per subject

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

### IESEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### IESPID
- **Order:** 5
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Inclusion or exclusion criteria number from CRF.

### IETESTCD
- **Order:** 6
- **Label:** Inclusion/Exclusion Criterion Short Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the criterion described in IETEST. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "IN01", "EX01".

### IETEST
- **Order:** 7
- **Label:** Inclusion/Exclusion Criterion
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim description of the inclusion or exclusion criterion that was the exception for the subject within the study. IETEST cannot be longer than 200 characters.

### IECAT
- **Order:** 8
- **Label:** Inclusion/Exclusion Category
- **Type:** Char
- **Controlled Terms:** C66797
- **Role:** Grouping Qualifier
- **Core:** Req
- **CDISC Notes:** Used to define a category of related records across subjects.

### IESCAT
- **Order:** 9
- **Label:** Inclusion/Exclusion Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or for to categorize as a major or minor exceptions. Examples: "MAJOR", "MINOR".

### IEORRES
- **Order:** 10
- **Label:** I/E Criterion Original Result
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Result Qualifier
- **Core:** Req
- **CDISC Notes:** Original response to inclusion/exclusion criterion question, i.e., whether the inclusion or exclusion criterion was met.

### IESTRESC
- **Order:** 11
- **Label:** I/E Criterion Result in Std Format
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Result Qualifier
- **Core:** Req
- **CDISC Notes:** Response to inclusion/exclusion criterion result, in standard format.

### VISITNUM
- **Order:** 12
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 13
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 14
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 15
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 16
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the observation date/time of the inclusion/exclusion finding.

### IEDTC
- **Order:** 17
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the inclusion/exclusion criterion represented in ISO 8601 character format.

### IEDY
- **Order:** 18
- **Label:** Study Day of Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of collection of the inclusion/exclusion exceptions, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.
---

## Cross References

### Controlled Terminology
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — IEORRES, IESTRESC
- [Category of Inclusion/Exclusion (C66797)](../../terminology/core/general_part2.md) — IECAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/IE/assumptions.md -->
# IE — Assumptions

1. The intent of the IE domain model is to collect responses to only those criteria that the subject did not meet, and not the responses to all criteria. For the complete list of inclusion/exclusion criteria, see Section 7.4.1, Trial Inclusion/Exclusion Criteria.

2. This domain should be used to document the exceptions to inclusion or exclusion criteria at the time that eligibility for study entry is determined (e.g., at the end of a run-in period or immediately before randomization). This domain should not be used to collect protocol deviations/violations incurred during the course of the study, typically after randomization or start of study medication. See Section 6.2.7, Protocol Deviations, for the model that is used to submit protocol deviations/violations.

3. IETEST is to be used only for the verbatim description of the inclusion or exclusion criteria. If the text is no more than 200 characters, it goes in IETEST; if the text is more than 200 characters, put meaningful text in IETEST and describe the full text in the study metadata. See Section 4.5.3.1, Test Name (--TEST) Greater than 40 Characters, for further information.

4. The following qualifiers would generally not be used in IE: --MODIFY, --POS, --BODSYS, --ORRESU, --ORNRLO, --ORNRHI, --STRESN, --STRESU, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --NAM, --LOINC, --SPEC, --SPCCND, --LOC, --METHOD, --BLFL, --LOBXFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV, --STAT.

<!-- source: knowledge_base/domains/IS/spec.md -->
# IS — Immunogenicity Specimen Assessments

> Class: Findings | Structure: One record per test per visit per subject

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

### NHOID
- **Order:** 4
- **Label:** Non-host Organism ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.

### ISSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### ISGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### ISREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier. Example: "458975-01".

### ISSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### ISTESTCD
- **Order:** 9
- **Label:** Immunogenicity Test/Exam Short Name
- **Type:** Char
- **Controlled Terms:** C120525
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in ISTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in ISTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). ISTESTCD cannot contain characters other than letters, numbers, or underscores.

### ISTEST
- **Order:** 10
- **Label:** Immunogenicity Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C120526
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in ISTEST cannot be longer than 40 characters. Example: "Immunoglobulin E".

### ISTSTCND
- **Order:** 11
- **Label:** Test Condition
- **Type:** Char
- **Controlled Terms:** C181175
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed.

### ISCNDAGT
- **Order:** 12
- **Label:** Test Condition Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent used to impose a test condition. Examples are different stimulating agents used in immunoassays such as those in the Interferon Gamma Response assay (e.g., Mycobacterium tuberculosis ESAT-6, CFP-10, TB 7.7, Mitogen).

### ISBDAGNT
- **Order:** 13
- **Label:** Binding Agent
- **Type:** Char
- **Controlled Terms:** C85491; C181169
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the agent that is binding to the entity in the ISTEST variable. ISBDAGNT is used to indicate that there is a binding relationship between the entities in the ISTEST and ISBDAGNT variables, regardless of direction.  ISBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in ISTEST and ISBDAGNT. In other words, the combination of ISTEST and ISBDAGNT should describe the entity or the analyte being measured, without the need for additional variables.  The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, an endogenous molecule, an allergen, or an infectious agent.

### ISTSTOPO
- **Order:** 14
- **Label:** Test Operational Objective
- **Type:** Char
- **Controlled Terms:** C181170
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the high-level purpose of the test at the operational level. If populated, valid values are "SCREEN", "CONFIRM", and "QUANTIFY".

### ISMSCBCE
- **Order:** 15
- **Label:** Molecule Secreted by Cells
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the entity secreted by the cells represented in ISTEST. The combination of ISTEST and ISMSCBCE should describe the entity or the analyte being measured, without the need for additional variables.

### ISTSTDTL
- **Order:** 16
- **Label:** Test Detail
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of ISTESTCD and ISTEST.

### ISCAT
- **Order:** 17
- **Label:** Category for Immunogenicity Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values across subjects. Example: "SEROLOGY".

### ISSCAT
- **Order:** 18
- **Label:** Subcategory for Immunogenicity Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of ISCAT.

### ISORRES
- **Order:** 19
- **Label:** Results or Findings in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### ISORRESU
- **Order:** 20
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for ISORRES. Examples: "Index Value", "gpELISA", "unit/mL".

### ISORNRLO
- **Order:** 21
- **Label:** Reference Range Lower Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### ISORNRHI
- **Order:** 22
- **Label:** Reference Range Upper Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### ISSTRESC
- **Order:** 23
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from ISORRES, in a standard format or in standard units. ISSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in ISSTRESN.

### ISSTRESN
- **Order:** 24
- **Label:** Numeric Results/Findings in Std. Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from ISSTRESC. ISSTRESN should store all numeric test results or findings.

### ISSTRESU
- **Order:** 25
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized units used for ISSTRESC and ISSTRESN. Examples: "Index Value", "gpELISA", "unit/mL".

### ISSTNRLO
- **Order:** 26
- **Label:** Reference Range Lower Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurements for ISSTRESC/ISSTRESN in standardized units. Should be populated only for continuous results.

### ISSTNRHI
- **Order:** 27
- **Label:** Reference Range Upper Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.

### ISSTNRC
- **Order:** 28
- **Label:** Reference Range for Char Rslt-Std Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE".

### ISNRIND
- **Order:** 29
- **Label:** Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates where the value falls with respect to reference range defined by ISORNRLO and ISORNRHI, ISSTNRLO and ISSTNRHI, or by ISSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW".  Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether ISNRIND refers to the original or standard reference ranges and results.  Should not be used to indicate clinical significance.

### ISSTAT
- **Order:** 30
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a test was not done. Should be null if a result exists in ISORRES.

### ISREASND
- **Order:** 31
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Used in conjunction with ISSTAT when value is "NOT DONE".

### ISNAM
- **Order:** 32
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the laboratory or vendor who provided the test results.

### ISSPEC
- **Order:** 33
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the types of specimen used for a measurement. Example: "SERUM".

### ISSPCCND
- **Order:** 34
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".

### ISSPCUFL
- **Order:** 35
- **Label:** Specimen Usability for the Test
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable.

### ISMETHOD
- **Order:** 36
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "ELISA", "ELISPOT".

### ISLOBXFL
- **Order:** 37
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### ISBLFL
- **Order:** 38
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that ISBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### ISDRVFL
- **Order:** 39
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Examples of records that might be derived for the submission datasets include those that represent the average of other records, do not come from the CRF, or are not as originally received or collected. If ISDRVFL="Y", then ISORRES may be null, with ISSTRESC and (if numeric) ISSTRESN having the derived value.

### ISLLOQ
- **Order:** 40
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units will be those used for ISSTRESU.

### VISITNUM
- **Order:** 41
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 42
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 43
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 44
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 45
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### ISDTC
- **Order:** 46
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation.

### ISENDTC
- **Order:** 47
- **Label:** End Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the observation.

### ISDY
- **Order:** 48
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to sponsor-defined RFSTDTC in Demographics.

### ISENDY
- **Order:** 49
- **Label:** Study Day of End of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### ISTPT
- **Order:** 50
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See ISTPTNUM and ISTPTREF. Examples: "Start", "5 min post".

### ISTPTNUM
- **Order:** 51
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of ISTPT to aid in sorting.

### ISELTM
- **Order:** 52
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (ISTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by ISTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by ISTPTREF.

### ISTPTREF
- **Order:** 53
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by ISELTM, ISTPTNUM, and ISTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### ISRFTDTC
- **Order:** 54
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, ISTPTREF.
---

## Cross References

### Controlled Terminology
- [Immunogenicity Specimen Assessments Test Code (C120525)](../../terminology/core/is_domain_part1.md) — ISTESTCD
- [Immunogenicity Specimen Assessments Test Name (C120526)](../../terminology/core/is_domain_part1.md) — ISTEST
- [Binding Agent for Immunogenicity Tests (C181169)](../../terminology/core/is_domain_part1.md) — ISBDAGNT
- [Test Operational Objective (C181170)](../../terminology/core/general_part4.md) — ISTSTOPO
- [Test Condition Response (C181175)](../../terminology/core/general_part4.md) — ISTSTCND
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — ISSPCUFL, ISLOBXFL, ISBLFL, ISDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — ISSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — ISORRESU, ISSTRESU
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — ISSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — ISSPEC
- [Reference Range Indicator (C78736)](../../terminology/core/general_part4.md) — ISNRIND
- [Microorganism (C85491)](../../terminology/core/is_domain_part2.md) — ISBDAGNT
- [Method (C85492)](../../terminology/core/general_part3.md) — ISMETHOD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Specimen:** [BS](../BS/) — immunogenicity specimen data
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/IS/assumptions.md -->
# IS — Assumptions

1. The Immunogenicity Specimen Assessments (IS) domain holds assessments that describe whether a therapy (e.g., biologic, drug, vaccine) provoked/caused/induced an immune response in a subject. The response can be either positive or negative. For example, a vaccine is expected to induce a beneficial immune response, whereas a cellular therapy (e.g., erythropoiesis-stimulating agents) may cause an adverse immune response.

2. The IS domain also holds assessments that describe whether an allergen, microorganism, or endogenous molecule provoked/caused/induced an immune response in a subject, such as a subject's antibody reaction (autoantibodies) against auto/self-antigens for autoimmune studies or antibody production in response to allergens in allergy tests. Expected outputs can be positive or negative, present or absent for the antibody of interest, as well as quantification of the antibody. Assessments pertaining to antibodies produced in response to microbial infection will also be represented in the IS domain.

3. Assessments about all other types of "induced" humoral (antibody) immune response in a subject (e.g., antibodies against human leukocyte antigen (HLA) proteins) will also be represented in the IS domain.

4. Certain types of cellular immune responses will also be modeled in IS using non-flow cytometry techniques (see example 6). Flow cytometry data should be modeled in the Cell Phenotype Findings (CP) domain, section 6.3.5.3.

5. An exception is made to the class of antigen/antibody (Ag/Ab) combination assays. Microbial antigen/antibody (Ag/Ab) combination tests should be represented in the Microbiology Specimen (MB) domain. An example is fourth-generation HIV Ag/Ab combination tests, which are commonly seen as HIV identification or detection assays rather than tests that provide additional details on and characterization of a subject's immunological responses. The outputs of these assays can be expected as reactive, non-reactive, or indeterminate. Whereas some tests generate separate outputs for antigen and antibody, others just indicate "reactive" when either or both are detected. Output is generally based on relative light units, where a result of "reactive" typically requires the signal to cutoff ratio to be greater than 1.

6. Measurements of cytokines, chemokines, and complement proteins should be represented in the Laboratory Test Results (LB) domain.

7. The IS domain variable ISBDAGNT (Binding Agent) is currently supported by 2 Controlled Terminology codelists: Microorganism (MICROORG) and Binding Agent for Immunogenicity Tests (ISBDAGT). Controlled Terminology Rules for Immunogenicity Tests describes how and when to use each codelist (see https://www.cdisc.org/standards/terminology/controlled-terminology).
   a. For antidrug antibody (ADA) tests, the ISBDAGNT variable is used to represent the free-text description of the name/identity of the therapy the antidrug antibody targets. CDISC does not control study therapy names (e.g., drugs, biologics). For ADA tests as a part of regulatory agency submissions, the proprietary binding study therapy name(s) should be considered as extended values of the ISBDAGT codelist when represented in Define-XML.
   b. For mixed-allergens panel tests, submission values represented in the ISBDAGNT variable should follow this format: "XXX, Multiple" (e.g., Dairy Mix Antigens, Multiple; Animal Mix Antigens, Multiple; use the plural form for the word "antigen" if needed). Should the sponsor wish to specify the individual antigens in a mixed antigen panel (e.g., ISBDAGNT = "Animal Mix Antigens, Multiple"), put the names of the specific antigens in Suppqual (e.g., Cat, Dog, Cow, Horse; see example 11).

8. The IS domain variable ISTSTOPO (Test Operational Objective) is supported by a nonextensible Controlled Terminology codelist containing the values SCREEN, CONFIRM, and QUANTIFY.

9. For vaccine studies, in order to distinguish collected data between study vaccine-induced immunogenicity and immunogenicity findings unrelated to the study vaccine (i.e., immunity as a result of natural infection or previous vaccination), the following ISCAT and ISSCAT values are recommended (see example 5):
   a. For immunological data pertaining to the study vaccine, ISCAT = STUDY VACCINE-RELATED IMMUNOGENICITY.
   b. For immunological data collected during the vaccine trial but which are not assessments about the study vaccine, ISCAT = NON-STUDY-RELATED IMMUNOGENICITY.
   c. For assessments measuring the induced-antibody response, ISSCAT = HUMORAL IMMUNITY.
   d. For assessments measuring the induced-cellular response, ISSCAT = CELLULAR IMMUNITY.

10. Any Identifier variables, Timing variables, or Findings general observation class qualifiers may be added to the IS domain.

<!-- source: knowledge_base/domains/LB/spec.md -->
# LB — Laboratory Test Results

> Class: Findings | Structure: One record per lab test per time point per visit per subject

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

### LBSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### LBGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### LBREFID
- **Order:** 6
- **Label:** Specimen ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier. Example: specimen ID.

### LBSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on the Lab page.

### LBTESTCD
- **Order:** 8
- **Label:** Lab Test or Examination Short Name
- **Type:** Char
- **Controlled Terms:** C65047
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in LBTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in LBTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). LBTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ALT", "LDH".

### LBTEST
- **Order:** 9
- **Label:** Lab Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C67154
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. Note: Any test normally performed by a clinical laboratory is considered a lab test. The value in LBTEST cannot be longer than 40 characters. Examples: "Alanine Aminotransferase", "Lactate Dehydrogenase".

### LBTSTCND
- **Order:** 10
- **Label:** Test Condition
- **Type:** Char
- **Controlled Terms:** C181175
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Identifies any planned condition imposed by the assay system on the specimen at the time the test is performed.

### LBBDAGNT
- **Order:** 11
- **Label:** Binding Agent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The textual description of the agent that is binding to the entity in the LBTEST variable. The LBBDAGNT variable is used to indicate that there is a binding relationship between the entities in the LBTEST and LBBDAGNT variables, regardless of direction.  LBBDAGNT is not a method qualifier. It should only be used when the actual interest of the measurement is the binding interaction between the 2 entities in LBTEST and LBBDAGNT. In other words, the combination of LBTEST and LBBDAGNT should describe the thing, the entity, or the analyte being measured, without the need for additional variables.  The binding agent may be (but is not limited to) a test article, a portion of the test article, a related compound, or an endogenous molecule.

### LBTSTOPO
- **Order:** 12
- **Label:** Test Operational Objective
- **Type:** Char
- **Controlled Terms:** C181170
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Text description of the high-level purpose of the test at the operational level.

### LBCAT
- **Order:** 13
- **Label:** Category for Lab Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of related records across subjects. Examples: "HEMATOLOGY", "URINALYSIS", "CHEMISTRY".

### LBSCAT
- **Order:** 14
- **Label:** Subcategory for Lab Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of a test category. Examples: "DIFFERENTIAL", "COAGULATION", "LIVER FUNCTION", "ELECTROLYTES".

### LBORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### LBORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for LBORRES. Example: "g/L".

### LBRESSCL
- **Order:** 17
- **Label:** Result Scale
- **Type:** Char
- **Controlled Terms:** C177910
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the scale of the original result value; for example, whether the result is ordinal, nominal, quantitative, or narrative.

### LBRESTYP
- **Order:** 18
- **Label:** Result Type
- **Type:** Char
- **Controlled Terms:** C179588
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Classifies the kind of result (i.e., property type) originally reported for the test. Examples include substance concentration, proportion, mass rate, and arbitrary concentration.

### LBCOLSRT
- **Order:** 19
- **Label:** Collected Summary Result Type
- **Type:** Char
- **Controlled Terms:** C177908
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the type of collected summary result. This includes source summary results collected on a CRF or provided by an external vendor (e.g., central lab). If the summary result is derived by the sponsor using individual source data records from SDTM, the derived summary result is represented in ADaM. If the summary result is produced and reported by the lab, the collected summary result is represented in SDTM.

### LBORNRLO
- **Order:** 20
- **Label:** Reference Range Lower Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### LBORNRHI
- **Order:** 21
- **Label:** Reference Range Upper Limit in Orig Unit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurement in original units. Should be populated only for continuous results.

### LBLLOD
- **Order:** 22
- **Label:** Lower Limit of Detection
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** The lowest threshold (as originally received or collected) for reliably detecting the presence or absence of substance measured by a specific test. The value for the field will be as described in documentation from the instrument or lab vendor.

### LBSTRESC
- **Order:** 23
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C102580
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from LBORRES in a standard format or standard units. LBSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in LBSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in LBORRES and these results effectively have the same meaning, they could be represented in standard format in LBSTRESC as "NEGATIVE". For other examples, see Original and Standardized Results.

### LBSTRESN
- **Order:** 24
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from LBSTRESC. LBSTRESN should store all numeric test results or findings.

### LBSTRESU
- **Order:** 25
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for LBSTRESC or LBSTRESN.

### LBSTNRLO
- **Order:** 26
- **Label:** Reference Range Lower Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Lower end of reference range for continuous measurements for LBSTRESC/LBSTRESN in standardized units. Should be populated only for continuous results.

### LBSTNRHI
- **Order:** 27
- **Label:** Reference Range Upper Limit-Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Upper end of reference range for continuous measurements in standardized units. Should be populated only for continuous results.

### LBSTNRC
- **Order:** 28
- **Label:** Reference Range for Char Rslt-Std Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** For normal range values that are character in ordinal scale or if categorical ranges were supplied. Examples: "-1 to +1", "NEGATIVE TO TRACE".

### LBNRIND
- **Order:** 29
- **Label:** Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates where the value falls with respect to reference range defined by LBORNRLO and LBORNRHI, LBSTNRLO and LBSTNRHI, or by LBSTNRC. Examples: "NORMAL", "ABNORMAL", "HIGH", "LOW". Sponsors should specify in the study metadata (Comments column in the Define-XML document) whether LBNRIND refers to the original or standard reference ranges and results. LBNRIND is not used to indicate clinical significance.

### LBSTAT
- **Order:** 30
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate exam not done. Should be null if a result exists in LBORRES.

### LBREASND
- **Order:** 31
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED", or "SPECIMEN LOST". Used in conjunction with LBSTAT when value is "NOT DONE".

### LBNAM
- **Order:** 32
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the laboratory that performed the test.

### LBLOINC
- **Order:** 33
- **Label:** LOINC Code
- **Type:** Char
- **Controlled Terms:** LOINC
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Code for the lab test from the LOINC code system. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the Define-XML external codelist attributes.

### LBSPEC
- **Order:** 34
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE".

### LBSPCCND
- **Order:** 35
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The physical state or quality of a sample for an assessment. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".

### LBSPCUFL
- **Order:** 36
- **Label:** Specimen Usability for the Test
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the usability of the specimen for the test. The value will be "N" if the specimen is not usable, and null if the specimen is usable.

### LBMETHOD
- **Order:** 37
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "EIA" (enzyme immunoassay), "ELECTROPHORESIS", "DIPSTICK".

### LBANMETH
- **Order:** 38
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** C160922
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., a calculation used to measure eGFR).

### LBTMTHSN
- **Order:** 39
- **Label:** Test Method Sensitivity
- **Type:** Char
- **Controlled Terms:** C179589
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The sensitivity of the test methodology with respect to observation, detection, or quantification.

### LBLOBXFL
- **Order:** 40
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### LBBLFL
- **Order:** 41
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that LBBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### LBFAST
- **Order:** 42
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status. Examples: "Y", "N".

### LBDRVFL
- **Order:** 43
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, or do not come from the CRF, or are not as originally received or collected are examples of records that might be derived for the submission datasets. If LBDRVFL="Y", then LBORRES may be null, with LBSTRESC and (if numeric) LBSTRESN having the derived value.

### LBTOX
- **Order:** 44
- **Label:** Toxicity
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of toxicity quantified by LBTOXGR. The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.

### LBTOXGR
- **Order:** 45
- **Label:** Standard Toxicity Grade
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Records toxicity grade value using a standard toxicity scale (e.g., the NCI CTCAE). If value is from a numeric scale, represent only the number (e.g., "2" not "Grade 2"). The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.

### LBCLSIG
- **Order:** 46
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgment.

### VISITNUM
- **Order:** 47
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 48
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 49
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 50
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 51
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### LBDTC
- **Order:** 52
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection represented in ISO 8601 character format.

### LBENDTC
- **Order:** 53
- **Label:** End Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of specimen collection represented in ISO 8601 character format.

### LBDY
- **Order:** 54
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.

### LBENDY
- **Order:** 55
- **Label:** Study Day of End of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### LBTPT
- **Order:** 56
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See LBTPTNUM and LBTPTREF. Examples: "Start", "5 min post".

### LBTPTNUM
- **Order:** 57
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of LBTPT to aid in sorting.

### LBELTM
- **Order:** 58
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (LBTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable. Represented as ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by LBTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by LBTPTREF.

### LBTPTREF
- **Order:** 59
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by LBELTM, LBTPTNUM, and LBTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### LBRFTDTC
- **Order:** 60
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, LBTPTREF.

### LBPTFL
- **Order:** 61
- **Label:** Point in Time Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** An indication that the specimen was collected at a single point in time. The value is "Y" or null. The intent of this variable in the LB domain is to aid mapping to LOINC codes in the dataset, when LOINC part "Time Aspect" = "Pt".

### LBPDUR
- **Order:** 62
- **Label:** Planned Duration
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned duration of specimen collection. If LBPTFL is "Y" then LBPDUR is null.
---

## Cross References

### Controlled Terminology
- [Laboratory Test Standard Character Result (C102580)](../../terminology/core/lb_part4.md) — LBSTRESC
- [Laboratory Analytical Method Calculation Formula (C160922)](../../terminology/core/lb_part1.md) — LBANMETH
- [Collected Summarized Value Type Response (C177908)](../../terminology/core/general_part2.md) — LBCOLSRT
- [Result Scale Response (C177910)](../../terminology/core/general_part4.md) — LBRESSCL
- [Result Type Response (C179588)](../../terminology/core/general_part4.md) — LBRESTYP
- [Test Method Sensitivity (C179589)](../../terminology/core/lb_part4.md) — LBTMTHSN
- [Test Operational Objective (C181170)](../../terminology/core/general_part4.md) — LBTSTOPO
- [Test Condition Response (C181175)](../../terminology/core/general_part4.md) — LBTSTCND
- [Laboratory Test Code (C65047)](../../terminology/core/lb_part2.md) — LBTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — LBSPCUFL, LBLOBXFL, LBBLFL, LBFAST, LBDRVFL ... (7 total)
- [Not Done (C66789)](../../terminology/core/general_part4.md) — LBSTAT
- [Laboratory Test Name (C67154)](../../terminology/core/lb_part3.md) — LBTEST
- [Unit (C71620)](../../terminology/core/general_part5.md) — LBORRESU, LBSTRESU
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — LBSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — LBSPEC
- [Reference Range Indicator (C78736)](../../terminology/core/general_part4.md) — LBNRIND
- [Method (C85492)](../../terminology/core/general_part3.md) — LBMETHOD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Specimen:** [BS](../BS/) — laboratory specimen data
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/LB/assumptions.md -->
# LB — Assumptions

1. This domain captures laboratory data collected on the CRF or received from a central provider or vendor.

2. For lab tests that do not have continuous numeric results (e.g., urine protein as measured by dipstick, descriptive tests such as urine color), LBSTNRC could be populated either with normal range values that are a range of character values for an ordinal scale (e.g., "NEGATIVE to TRACE") or a delimited set of values that are considered to be normal (e.g., "YELLOW", "AMBER"). LBORNRLO, LBORNRHI, LBSTNRLO, and LBSTNRHI should be null for these types of tests.

3. LBNRIND can be added to indicate where a result falls with respect to reference range defined by LBORNRLO and LBORNRHI. Examples: "HIGH", "LOW". If toxicity grading is available, values would be represented in the variables LBTOX and LBTOXGR. Clinical significance would be represented as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data, in LBCLSIG (see also LB Example 1).

4. For lab tests where the specimen is collected over time (e.g., 24-hour urine collection), the start date/time of the collection goes into LBDTC and the end date/time of collection goes into LBENDTC. See Section 4.4.8, Date and Time Reported in a Domain Based on Findings.

5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the LB domain, but the following qualifiers would not generally be used: --BODSYS, --SEV.

6. A value derived by a central lab according to its procedures is considered collected rather than derived. See Section 4.1.8.1, Origin Metadata for Variables.

7. The variable LBORRESU uses the UNIT codelist. This means that sponsors should be submitting a term from the CDISC Submission Value column in the published Controlled Terminology List that is maintained for CDISC by NCI EVS. When sponsors have units that are not in this column, they should first check to see if their unit is mathematically synonymous with an existing/published unit from the UNIT codelist and submit their lab values using the published CDISC submission value. Example: "g/L" and "mg/mL" are mathematically synonymous, but only "g/L" is the submission value in the CDISC Unit codelist. If this is not the case, the unit must be added as a codelist extensible value in the Define.xml, and a new-term request must be submitted.
   a. CDISC Controlled Terminology Rules for Lab and Unit are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

8. The LBLOINC variable contains a code from the Logical Observation Identifiers Names and Codes (LOINC) database that identifies a specific laboratory test. The LOINC to LB Mapping Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology, may be used to identify appropriate CDISC CT values for a test with a particular LOINC code. In addition to LBTEST, LBSPEC, LBMETHOD, and LBORRESU, the aspects of a test that are associated with a LOINC code may be represented in the variables LBTPT, LBANMETH, LBTSTCND, LBBDAGNT, LBTSTOPO, LBRESSCL, LBRESTYP, LBCOLSRT, LBLLOD, LBPTFL, and LBPDUR. These additional variables are only required to be populated when necessary to provide a semantically meaningful distinction between records with different LBLOINC values.

<!-- source: knowledge_base/domains/MB/spec.md -->
# MB — Microbiology Specimen

> Class: Findings | Structure: One record per microbiology specimen finding per time point per visit per subject

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

### FOCID
- **Order:** 4
- **Label:** Focus of Study-Specific Interest
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed. The value in this variable should have inherent semantic meaning.

### MBSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number.

### MBGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### MBREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier (e.g., sample ID for a subject sample from which a microbial culture was generated).

### MBSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.

### MBLNKID
- **Order:** 9
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed.

### MBLNKGRP
- **Order:** 10
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### MBTESTCD
- **Order:** 11
- **Label:** Microbiology Test or Finding Short Name
- **Type:** Char
- **Controlled Terms:** C120527
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or finding described in MBTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MBTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MBTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MCORGIDN" for Microbial Organism Identification "GMNCOC" for Gram Negative Cocci.

### MBTEST
- **Order:** 12
- **Label:** Microbiology Test or Finding Name
- **Type:** Char
- **Controlled Terms:** C120528
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in MBTEST cannot be longer than 40 characters. Examples: "Microbial Organism Identification", "Gram Negative Cocci", "HIV-1 RNA".

### MBTSTDTL
- **Order:** 13
- **Label:** Measurement, Test or Examination Detail
- **Type:** Char
- **Controlled Terms:** C174225
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of MBTESTCD and MBTEST. Example: "VIRAL LOAD" when MBTESTCD represents viral genetic material, such as "HCRNA", "QUANTIFICATION" when MBTESTCD represents any organism being quantified.

### MBCAT
- **Order:** 14
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records.

### MBSCAT
- **Order:** 15
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of MBCAT values.

### MBORRES
- **Order:** 16
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the microbiology measurement or finding as originally received or collected. Examples for "GRAM STAIN" findings: "+3 MODERATE", "+2 FEW", "<10". Examples for "CULTURE PLATE" findings: "KLEBSIELLA PNEUMONIAE", "STREPTOCOCCUS PNEUMONIAE".

### MBORRESU
- **Order:** 17
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original unit for MBORRES. Example: "mcg/mL".

### MBSTRESC
- **Order:** 18
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from MBORRES, in a standard format or standard units. MBSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MBSTRESN. For example, if a test has results "+3 MODERATE", "MOD", and "MODERATE" in MBORRES and these results effectively have the same meaning, they could be represented in standard format in MBSTRESC as "MODERATE".

### MBSTRESN
- **Order:** 19
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from MBSTRESC. MBSTRESN should store all numeric test results or findings.

### MBSTRESU
- **Order:** 20
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for MBSTRESC and MBSTRESN.

### MBRESCAT
- **Order:** 21
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding in a standard format.

### MBSTAT
- **Order:** 22
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### MBREASND
- **Order:** 23
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with MBSTAT when value is NOT DONE. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED".

### MBNAM
- **Order:** 24
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor (e.g., laboratory) that provided the test results.

### MBLOINC
- **Order:** 25
- **Label:** LOINC Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable (e.g., lab test).

### MBSPEC
- **Order:** 26
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "SPUTUM", "BLOOD", "PUS".

### MBSPCCND
- **Order:** 27
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Free or standardized text describing the condition of the specimen. Example: "CONTAMINATED".

### MBLOC
- **Order:** 28
- **Label:** Specimen Collection Location
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location relevant to the collection of the measurement.

### MBLAT
- **Order:** 29
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for specimen collection location further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### MBDIR
- **Order:** 30
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for specimen collection location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### MBMETHOD
- **Order:** 31
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Method of the test or examination. Examples: "GRAM STAIN", "MICROBIAL CULTURE, LIQUID", "QUANTITATIVE REVERSE TRANSCRIPTASE POLYMERASE CHAIN REACTION".

### MBLOBXFL
- **Order:** 32
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### MBBLFL
- **Order:** 33
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that MBBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### MBFAST
- **Order:** 34
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant.

### MBDRVFL
- **Order:** 35
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### VISITNUM
- **Order:** 36
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 37
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 38
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 39
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element which the specimen collection occurred.

### EPOCH
- **Order:** 40
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the specimen was collected.

### MBDTC
- **Order:** 41
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection.

### MBDY
- **Order:** 42
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.

### MBTPT
- **Order:** 43
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MBTPTNUM and MBTPTREF. Examples: "Start", "5 min post".

### MBTPTNUM
- **Order:** 44
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of MBTPT used in sorting.

### MBELTM
- **Order:** 45
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (MBTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by MBTPTREF, or "PT8H" to represent the period of 8 hours after the reference point indicated by MBTPTREF.

### MBTPTREF
- **Order:** 46
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by MBELTM, MBTPTNUM, and MBTPT. Example: "PREVIOUS DOSE".

### MBRFTDTC
- **Order:** 47
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point, MBTPTREF.
---

## Cross References

### Controlled Terminology
- [Microbiology Test Code (C120527)](../../terminology/core/microbiology_part2.md) — MBTESTCD
- [Microbiology Test Name (C120528)](../../terminology/core/microbiology_part3.md) — MBTEST
- [Microbiology Findings Test Details (C174225)](../../terminology/core/microbiology_part1.md) — MBTSTDTL
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MBLOBXFL, MBBLFL, MBFAST, MBDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MBSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — MBORRESU, MBSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — MBLOC
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — MBSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — MBSPEC
- [Method (C85492)](../../terminology/core/general_part3.md) — MBMETHOD
- [Laterality (C99073)](../../terminology/core/general_part2.md) — MBLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — MBDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Shared Dataset:** [MS](../MS/) — microbiology susceptibility results
- **Related Findings:** [MI](../MI/) — microbiology microscopic findings
- **Specimen:** [BS](../BS/) — microbiology specimen data
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/MB/assumptions.md -->
# MB — Assumptions

1. Representation of findings in the Microbiology Specimen domain should be handled as follows:
   a. In cases of tests that target an organism, group of organisms, or antigen for identification, MBTEST equals the name of the organism/antigen targeted by the identification assay, and
      i. MBTSTDTL should be "DETECTION".
      ii. The result should generally be "PRESENT"/"ABSENT", "POSITIVE"/"NEGATIVE", or "INDETERMINATE". However, there may be cases where a test differentiates between 2 or more similar organisms, in which case it would be appropriate for the result to be the name of the organism detected. For example, a test may look for influenza A or influenza B antigen. In this case, MBTEST would be "Influenza A/B Antigen"; the result could be "INFLUENZA A ANTIGEN", "INFLUENZA B ANTIGEN", or "INFLUENZA A/B ANTIGEN".
   b. For non-targeted identification of organisms (i.e., tests that have the ability to identify a range of organisms without specifically targeting any), the value for MBTESTCD/MBTEST should be "MCORGIDN"/"Microbial Organism Identification", and the result should be the name of the organism or group of organisms found to be present (e.g., "INFLUENZA A VIRUS SUBTYPE H1N1"; "CLONORCHIS SINENSIS"). In this scenario MBORRES is populated with values from the Microorganism Codelist (C85491).
   c. Culture characteristics covers concepts such as growth/no growth, colony quantification measures, colony color, colony morphology, and so on. **Note that this does not include drug susceptibility testing, which is represented in the Microbiology Susceptibility (MS) domain.**
      i. MBTESTCD/MBTEST should be the name of the organism or group of organisms being characterized.
      ii. MBTSTDTL should be the name of the characteristic being described (e.g., "COLONY COUNT", "VIRAL LOAD").
      iii. MBGRPID should be used to group characteristic records with the identification record of the organism to which the characteristics apply.
      iv. CDISC Controlled Terminology Rules for Microbiology (MB/MS) domains are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

2. MBDTC represents the date the specimen was collected.

3. If the specimen was cultured, the start and end date of culture are represented in the Biospecimen Events (BE) domain in BESTDTC and BEENDTC respectively. The variable --REFID represents the sample ID as originally assigned in the BE domain. See BE domain assumptions in the SDTMIG v3.4, section 6.2.2, for guidelines on assigning --REFID values to samples and subsamples.
   a. Culture dates can be connected to the MB record via MBREFID and BEREFID.
   b. If the same sample is associated with many biospecimen events and tests, users may need to make use of additional linking variables such as --LNKID.

4. The variable NHOID is not allowed for use in the MB domain. Any additional Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MB domain, but the following variables would not generally be used: --MODIFY, --BODSYS, --FAST, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/MH/spec.md -->
# MH — Medical History

> Class: Events | Structure: One record per medical history event per subject

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

### MHSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### MHGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### MHREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external medical history identifier.

### MHSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on a Medical History CRF page.

### MHTERM
- **Order:** 8
- **Label:** Reported Term for the Medical History
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim or preprinted CRF term for the medical condition or event.

### MHMODIFY
- **Order:** 9
- **Label:** Modified Reported Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** If MHTERM is modified to facilitate coding, then MHMODIFY will contain the modified text.

### MHDECOD
- **Order:** 10
- **Label:** Dictionary-Derived Term
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary-derived text description of MHTERM or MHMODIFY. Equivalent to the Preferred Term (PT in MedDRA). The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.

### MHEVDTYP
- **Order:** 11
- **Label:** Medical History Event Date Type
- **Type:** Char
- **Controlled Terms:** C124301
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Specifies the aspect of the medical condition or event by which MHSTDTC and/or the MHENDTC is defined. Examples: "DIAGNOSIS", "SYMPTOMS", "RELAPSE", "INFECTION".

### MHCAT
- **Order:** 12
- **Label:** Category for Medical History
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records. Examples: "CARDIAC", "GENERAL".

### MHSCAT
- **Order:** 13
- **Label:** Subcategory for Medical History
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the condition or event.

### MHPRESP
- **Order:** 14
- **Label:** Medical History Event Pre-Specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** A value of "Y" indicates that this medical history event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms).

### MHOCCUR
- **Order:** 15
- **Label:** Medical History Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when the occurrence of specific medical history conditions is solicited, to indicate whether ("Y"/"N") a medical condition (MHTERM) had ever occurred. Values are null for spontaneously reported events.

### MHSTAT
- **Order:** 16
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The status indicates that the prespecified question was not asked/answered.

### MHREASND
- **Order:** 17
- **Label:** Reason Medical History Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason why data for a prespecified condition was not collected. Used in conjunction with MHSTAT when value is "NOT DONE".

### MHBODSYS
- **Order:** 18
- **Label:** Body System or Organ Class
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Dictionary-derived. Body system or organ class that is involved in an event or measurement from a standard hierarchy (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables which may not necessarily be the primary SOC.

### TAETORD
- **Order:** 19
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 20
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the medical history event.

### MHDTC
- **Order:** 21
- **Label:** Date/Time of History Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the medical history observation represented in ISO 8601 character format.

### MHSTDTC
- **Order:** 22
- **Label:** Start Date/Time of Medical History Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of the medical history event represented in ISO 8601 character format.

### MHENDTC
- **Order:** 23
- **Label:** End Date/Time of Medical History Event
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the medical history event.

### MHDY
- **Order:** 24
- **Label:** Study Day of History Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of medical history collection, measured as integer day. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics. This formula should be consistent across the submission.

### MHENRF
- **Order:** 25
- **Label:** End Relative to Reference Period
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Describes the end of the event relative to the sponsor-defined reference period. The sponsor-defined reference period is a continuous period of time defined by a discrete starting point and a discrete ending point (represented by RFSTDTC and RFENDTC in Demographics).  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### MHENRTPT
- **Order:** 26
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the event as being before or after the reference time point defined by variable MHENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### MHENTPT
- **Order:** 27
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the reference point referred to by MHENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Medical History Event Date Type (C124301)](../../terminology/core/other_part1.md) — MHEVDTYP
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — MHENRF, MHENRTPT
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MHPRESP, MHOCCUR
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MHSTAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Events):** AE, BE, CE, DS, DV, HO

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Events class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/MH/assumptions.md -->
# MH — Assumptions

1. Prior treatments, including prior medications and procedures, should be submitted in an appropriate dataset from the Interventions class (e.g., Concomitant/Prior Medications (CM) or Procedures (PR)).

2. **MH description and coding**
   a. MHTERM is the topic variable and captures the verbatim term collected for the condition or event or the prespecified term used to collect information about the occurrence of any of a group of conditions or events. MHTERM is a required variable and must have a value.
   b. MHMODIFY is a permissible variable and should be included if the sponsor's procedure permits modification of a verbatim term for coding. The variable should be populated as per the sponsor's procedures; null values are permitted.
   c. If the sponsor codes the reported term (MHTERM) using a standard dictionary, then MHDECOD will be populated with the preferred term derived from the dictionary. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.
   d. MHBODSYS is the system organ class (SOC) from the coding dictionary associated with the adverse event by the sponsor. This value may differ from the primary SOC designated in the coding dictionary's standard hierarchy. It is expected that this variable will be populated.
   e. If a CRF collects medical history by prespecified body systems and the sponsor also codes reported terms using a standard dictionary, then MHDECOD and MHBODSYS are populated using the standard dictionary. MHCAT and MHSCAT should be used for the prespecified body systems.

3. **Additional categorization and grouping**
   a. MHCAT and MHSCAT may be populated with the sponsor's predefined categorization of medical history events, which are often prespecified on the CRF. Note that even if the sponsor uses the body system terminology from the standard dictionary, MHBODSYS and MHCAT may differ; MHBODSYS is derived from the coding system, whereas MHCAT is effectively assigned when the investigator records a condition under the prespecified category.
      i. This categorization should not group all records (within the MH domain) into one generic group such as "Medical Medical History" or "General Medical History" because this is redundant information with the domain code. If no smaller categorization can be applied, then it is not necessary to include or populate this variable.
      ii. Examples of MHCAT could include "General Medical History" (see above assumption; if "General Medical History" is an MHCAT value, then there should be other MHCAT values), "Allergy Medical History," and "Reproductive Medical History".
   b. MHGRPID may be used to link (or associate) different records together to form a block of related records at the subject level within the MH domain. It should not be used in place of MHCAT or MHSCAT, which are used to group data across subjects. For example, if a group of syndromes reported for a subject were related to a particular disease, then the MHGRPID variable could be populated with the appropriate text.

4. **Prespecified terms; presence or absence of events**
   a. Information on medical history is generally collected in 2 different ways, either by recording free text or using a prespecified list of terms. The solicitation of information on specific medical history events may affect the frequency at which they are reported; therefore, the fact that a specific medical history event was solicited may be of interest to reviewers. MHPRESP and MHOCCUR are used together to indicate whether the condition in MHTERM was prespecified and whether it occurred. A value of "Y" in MHPRESP indicates that the term was prespecified.
   b. MHOCCUR is used to indicate whether a prespecified medical condition occurred; a value of "Y" indicates that the event occurred and "N" indicates that it did not.
   c. If a medical history event was reported using free text, the values of MHPRESP and MHOCCUR should be null. MHPRESP and MHOCCUR are permissible fields and may be omitted from the dataset if all medical history events were collected as free text.
   d. MHSTAT and MHREASND provide information about prespecified medical history questions for which no response was collected. MHSTAT and MHREASND are permissible fields and may be omitted from the dataset if all medications were collected as free text or if all prespecified conditions had responses in MHOCCUR.

      | Situation | MHPRESP | MHOCCUR | MHSTAT |
      |-----------|---------|---------|--------|
      | Spontaneously reported event occurred | | | |
      | Pre-specified event occurred | Y | Y | |
      | Pre-specified event did not occur | Y | N | |
      | Pre-specified event has no response | Y | | NOT DONE |

   e. When medical history events are collected with the recording of free text, a record may be entered into the data management system to indicate "no medical history" for a specific subject or prespecified body system category (e.g., gastrointestinal). For these subjects or categories within subject, do not include a record in the MH dataset to indicate that there were no events.

5. **Timing variables**
   a. Relative timing assessments such as "Ongoing" or "Active" are common in the collection of MH information. MHENRF may be used when this relative timing assessment is coincident with the start of the study reference period for the subject represented in the Demographics (DM) dataset (RFSTDTC). MHENRTPT and MHENTPT may be used when "Ongoing" is relative to another date such as the screening visit date. See the examples in this section and in Section 4.4.7, Use of Relative Timing Variables.
   b. Additional timing variables (e.g., MHSTRF) may be used when appropriate.

6. **MH event date type**
   a. MHEVDTYP is a domain-specific variable that can be used to indicate the aspect of the event that is represented in the event start and/or end date/times (MHSTDTC and/or MHENDTC). If a start date and/or end date is collected without further specification of what constitutes the start or end of the event, then MHEVDTYP is not needed. However, when data collection specifies how the start or end date is to be reported, MHEVDTYP can be used to provide this information. For example, when collecting the date of diagnosis, it would be used to populate MHSTDTC; MHEVDTYP would be populated with "DIAGNOSIS". If MHEVDTYP is not needed for any collected data, it need not be included in the dataset. If MHEVDTYP is included in the dataset, it should be populated only when the data collection specifies the aspect of the event that is to be used to populate the start and/or end date; otherwise, it should be null.
   b. When data collected about an event includes 2 different dates that could be considered the start or end of an event, then an MH record will be created for each. For example, if data collection included both a date of onset of symptoms and a date of diagnosis, there would be 2 records for the event, one with MHSTDTC the date of onset of symptoms and MHEVDTYP = "SYMPTOMS" and a second with MHSTDTC the date of diagnosis and MHENDTYP = "DIAGNOSIS". In such a case, it is recommended that the 2 records be linked by means such as a common value of MHSPID or MHGRPID.

> **Note:** PDF 原文此处写的是 MHENDTYP，但根据 assumption 6a 的定义、MH spec 变量表以及所有 MH/SM/FA examples 中的用法，该变量名应为 MHEVDTYP。MHENDTYP 不是 SDTM 标准变量，疑为 PDF 原文笔误。

7. Any identifiers, timing variables, or Events general observation-class qualifiers may be added to the MH domain, but the following Qualifiers would generally not be used: --SER, --ACN, --ACNOTH, --REL, --RELNST, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE.

<!-- source: knowledge_base/domains/MI/spec.md -->
# MI — Microscopic Findings

> Class: Findings | Structure: One record per finding per specimen per subject

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

### MISEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### MIGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject. This is not the treatment group number.

### MIREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier. Example: specimen barcode number.

### MISPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be printed on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: line number from the MI Findings page.

### MITESTCD
- **Order:** 8
- **Label:** Microscopic Examination Short Name
- **Type:** Char
- **Controlled Terms:** C132263
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in MITEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MITESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MITESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "HER2", "BRCA1", "TTF1".

### MITEST
- **Order:** 9
- **Label:** Microscopic Examination Name
- **Type:** Char
- **Controlled Terms:** C132262
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in MITEST cannot be longer than 40 characters. Examples: "Human Epidermal Growth Factor Receptor 2", "Breast Cancer Susceptibility Gene 1", "Thyroid Transcription Factor 1".

### MITSTDTL
- **Order:** 10
- **Label:** Microscopic Examination Detail
- **Type:** Char
- **Controlled Terms:** C125922
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of the test performed in producing the MI result. This would be used to represent specific attributes, such as intensity score or percentage of cells displaying presence of the biomarker or compound.

### MICAT
- **Order:** 11
- **Label:** Category for Microscopic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records.

### MISCAT
- **Order:** 12
- **Label:** Subcategory for Microscopic Finding
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of MICAT.

### MIORRES
- **Order:** 13
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the histopathology measurement or finding as originally received or collected.

### MIORRESU
- **Order:** 14
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original unit for MIORRES.

### MISTRESC
- **Order:** 15
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from MIORRES in a standard format or standard units. MISTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MISTRESN.

### MISTRESN
- **Order:** 16
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from MISTRESC. MISTRESN should store all numeric test results or findings.

### MISTRESU
- **Order:** 17
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for MISTRESC and MISTRESN.

### MIRESCAT
- **Order:** 18
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding. Examples: "MALIGNANT" or "BENIGN" for tumor findings.

### MISTAT
- **Order:** 19
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate examination not done or result is missing. Should be null if a result exists in MIORRES or have a value of "NOT DONE" when MIORRES = "NULL".

### MIREASND
- **Order:** 20
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with MISTAT when value is NOT DONE. Examples: "SAMPLE AUTOLYZED", "SPECIMEN LOST".

### MINAM
- **Order:** 21
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor (e.g., laboratory) that provided the test results.

### MISPEC
- **Order:** 22
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Subject of the observation. Defines the type of specimen used for a measurement. Examples: "TISSUE", "BLOOD", "BONE MARROW".

### MISPCCND
- **Order:** 23
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Free or standardized text describing the condition of the specimen. Example: "AUTOLYZED".

### MILOC
- **Order:** 24
- **Label:** Specimen Collection Location
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Location relevant to the collection of the specimen. Examples: "LUNG", "KNEE JOINT", "ARM", "THIGH".

### MILAT
- **Order:** 25
- **Label:** Specimen Laterality within Subject
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for laterality of the location of the specimen in MILOC. Examples: "LEFT", "RIGHT", "BILATERAL".

### MIDIR
- **Order:** 26
- **Label:** Specimen Directionality within Subject
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for directionality of the location of the specimen in MILOC. Examples: "DORSAL", "PROXIMAL".

### MIMETHOD
- **Order:** 27
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. This could include the technique or type of staining used for the slides. Examples: "IHC", "Crystal violet", "Safranin", "Trypan blue", or "Propidium iodide".

### MILOBXFL
- **Order:** 28
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### MIBLFL
- **Order:** 29
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null. Note that MIBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### MIEVAL
- **Order:** 30
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Example: "PATHOLOGIST", "PEER REVIEW", "SPONSOR PATHOLOGIST".

### VISITNUM
- **Order:** 31
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 32
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 33
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 34
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 35
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the specimen was collected.

### MIDTC
- **Order:** 36
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection, in ISO 8601 format.

### MIDY
- **Order:** 37
- **Label:** Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.
---

## Cross References

### Controlled Terminology
- [Microscopic Findings Test Details (C125922)](../../terminology/core/mi.md) — MITSTDTL
- [SDTM Microscopic Findings Test Name (C132262)](../../terminology/core/mi.md) — MITEST
- [SDTM Microscopic Findings Test Code (C132263)](../../terminology/core/mi.md) — MITESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MILOBXFL, MIBLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MISTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — MIORRESU, MISTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — MILOC
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — MISPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — MISPEC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — MIEVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — MIMETHOD
- [Laterality (C99073)](../../terminology/core/general_part2.md) — MILAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — MIDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Related Findings:** [MB](../MB/) — microbiology organism identification

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/MI/assumptions.md -->
# MI — Assumptions

1. This domain holds findings resulting from the microscopic examination of tissue samples. These examinations are performed on a specimen, usually one that has been prepared with some type of stain. Some examinations of cells in fluid specimens (e.g., blood, urine) are classified as lab tests and should be stored in the Laboratory Test Results (LB) domain. Biomarkers assessed by histologic or histopathological examination (by employing cytochemical/immunocytochemical stains) are stored in the MI domain.

2. When biomarker results are represented in MI, MITESTCD reflects the biomarker of interest (e.g., "BRCA1", "HER2", "TTF1"), and MITSTDTL further qualifies the record. MITSTDTL is used to represent details descriptive of staining results (e.g., "H SCORE TOTAL SCORE", "STAINING INTENSITY", "PERCENT POSITIVE CELL").

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MI domain, but the following qualifiers would generally not be used: --POS, --MODIFY, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --LEAD, --CSTATE, --BLFL, --FAST, --DRVFL, --LLOQ, --ULOQ.

<!-- source: knowledge_base/domains/MK/spec.md -->
# MK — Musculoskeletal System Findings

> Class: Findings | Structure: One record per assessment per visit per subject

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

### MKSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1.

### MKGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain.

### MKREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier such as lab specimen ID or a medical image.

### MKSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. Example: Preprinted line identifier on a Concomitant Medications page.

### MKLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### MKLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### MKTESTCD
- **Order:** 10
- **Label:** Short Name of Musculoskeletal Test
- **Type:** Char
- **Controlled Terms:** C127269
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for MKTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The value in MKTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MKTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TNDRIND", "SWLLIND", "SGJSNSCR".

### MKTEST
- **Order:** 11
- **Label:** Name of Musculoskeletal Test
- **Type:** Char
- **Controlled Terms:** C127270
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name For MKTESTCD. Examples: "Tenderness Indicator", "Swollen Indicator", "Sharp/Genant JSN Score".

### MKCAT
- **Order:** 12
- **Label:** Category for Musculoskeletal Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Examples: "SWOLLEN/TENDER JOINT ASSESSMENT".

### MKSCAT
- **Order:** 13
- **Label:** Subcategory for Musculoskeletal Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of MKCAT values.

### MKPOS
- **Order:** 14
- **Label:** Position of Subject
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### MKORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### MKORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for MKORRES.

### MKSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from MKORRES in a standard format or in standard units. MKSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MKSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in MKORRES and these results effectively have the same meaning, they could be represented in standard format in MKSTRESC as "NEGATIVE".

### MKSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from MKSTRESC. MKSTRESN should store all numeric test results or findings.

### MKSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for MKSTRESC and MKSTRESN.

### MKSTAT
- **Order:** 20
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or that a test was attempted but did not generate a result. Should be null if a result exists in MKORRES.

### MKREASND
- **Order:** 21
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with MKSTAT when value is "NOT DONE".

### MKLOC
- **Order:** 22
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Examples: "INTERPHALANGEAL JOINT 1", "SHOULDER JOINT".

### MKLAT
- **Order:** 23
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### MKDIR
- **Order:** 24
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### MKMETHOD
- **Order:** 25
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "X-RAY", "MRI", "CT SCAN".

### MKLOBXFL
- **Order:** 26
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### MKBLFL
- **Order:** 27
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that MKBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### MKDRVFL
- **Order:** 28
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### MKEVAL
- **Order:** 29
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".

### MKEVALID
- **Order:** 30
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in MKEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2".

### VISITNUM
- **Order:** 31
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 32
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 33
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 34
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 35
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### MKDTC
- **Order:** 36
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation.

### MKDY
- **Order:** 37
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### MKTPT
- **Order:** 38
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See MKTPTNUM and MKTPTREF.

### MKTPTNUM
- **Order:** 39
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### MKELTM
- **Order:** 40
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned Elapsed time relative to a planned fixed reference (MKTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### MKTPTREF
- **Order:** 41
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by MKELTM, MKTPTNUM, and MKTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### MKRFTDTC
- **Order:** 42
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by MKTPTREF.
---

## Cross References

### Controlled Terminology
- [Musculoskeletal System Finding Test Code (C127269)](../../terminology/core/other_part2.md) — MKTESTCD
- [Musculoskeletal System Finding Test Name (C127270)](../../terminology/core/other_part2.md) — MKTEST
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MKLOBXFL, MKBLFL, MKDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MKSTAT
- [Position (C71148)](../../terminology/core/interventions.md) — MKPOS
- [Unit (C71620)](../../terminology/core/general_part5.md) — MKORRESU, MKSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — MKLOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — MKEVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — MKMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — MKEVALID
- [Laterality (C99073)](../../terminology/core/general_part2.md) — MKLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — MKDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/MK/assumptions.md -->
# MK — Assumptions

1. The Musculoskeletal System Findings domain should not be used for oncology data related to the musculoskeletal system (e.g., bone lesions). Such data should be placed in the appropriate oncology domains: Tumor/Lesion Identification (TU), Tumor/Lesion Results (TR), and/or Disease Response and Clinical Classification (RS).

2. Musculoskeletal assessment examples that may have results represented in the MK domain include the following: morphology/physiology observations (e.g., swollen/tender joint count, limb movement, strength/grip measurements).

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MK domain, but the following qualifiers would generally not be used: --MODIFY, --BODSYS, --LOINC, --TOX, --TOXGR, --FAST, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --ORREF, --STREFC, --STREFN.

<!-- source: knowledge_base/domains/ML/spec.md -->
# ML — Meal Data

> Class: Interventions | Structure: One record per food product occurrence or constant intake interval per subject

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

### MLSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### MLGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### MLSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. Examples: a number preprinted on the CRF as an explicit line identifier, record identifier defined in the sponsor's operational database.

### MLTRT
- **Order:** 7
- **Label:** Name of Meal
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Verbatim food product name that is either preprinted or collected on a CRF.

### MLCAT
- **Order:** 8
- **Label:** Category for Meal
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of MLTRT values.

### MLSCAT
- **Order:** 9
- **Label:** Subcategory for Meal
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of MLCAT values.

### MLPRESP
- **Order:** 10
- **Label:** ML Pre-specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used when a specific meal is prespecified on a CRF. Values should be "Y" or null.

### MLOCCUR
- **Order:** 11
- **Label:** ML Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to record whether a prespecified meal occurred when information about the occurrence of a specific meal is solicited.

### MLSTAT
- **Order:** 12
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate when a question about the occurrence of a prespecified meal was not answered. Should be null or have a value of "NOT DONE".

### MLREASND
- **Order:** 13
- **Label:** Reason Meal Not Collected
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes the reason a response to a question about the occurrence of a meal was not collected. Used in conjunction with MLSTAT when value is "NOT DONE".

### MLDOSE
- **Order:** 14
- **Label:** Dose
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount of MLTRT consumed. Not populated when MLDOSTXT is populated.

### MLDOSTXT
- **Order:** 15
- **Label:** Dose Description
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Amount description of MLTRT consumed, collected in text form. Not populated when MLDOSE is populated. Examples: "<1 per day", "200-400".

### MLDOSU
- **Order:** 16
- **Label:** Dose Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Units for MLDOSE, MLDOSTOT, or MLDOSTXT.

### MLDOSFRM
- **Order:** 17
- **Label:** Dose Form
- **Type:** Char
- **Controlled Terms:** C66726
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Dosage form for MLTRT. Example: "BAR, CHEWABLE".

### VISITNUM
- **Order:** 18
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 19
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 20
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 21
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the meal started.

### EPOCH
- **Order:** 22
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the meal.

### MLDTC
- **Order:** 23
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the meal represented in ISO 8601 character format.

### MLSTDTC
- **Order:** 24
- **Label:** Start Date/Time of Meal
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Start date/time of the meal represented in ISO 8601 character format.

### MLENDTC
- **Order:** 25
- **Label:** End Date/Time of Meal
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of the meal represented in ISO 8601 character format.

### MLDY
- **Order:** 26
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of the visit/collection expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### MLSTDY
- **Order:** 27
- **Label:** Study Day of Start of Meal
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of start of the meal expressed in integer days relative to sponsor-defined RFSTDTC in Demographics.

### MLENDY
- **Order:** 28
- **Label:** Study Day of End of Meal
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of the meal expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### MLDUR
- **Order:** 29
- **Label:** Duration of Meal
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of the meal represented in ISO 8601 character format. Used only if collected on the CRF and not derived.

### MLTPT
- **Order:** 30
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point. See MLTPTNUM and MLTPTREF.

### MLTPTNUM
- **Order:** 31
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### MLELTM
- **Order:** 32
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to the planned fixed reference (MLTPTREF). This variable is useful when there are repetitive measures. Not a clock time or a date/time variable. Represented as an ISO 8601 duration.

### MLTPTREF
- **Order:** 33
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by MLELTM, MLTPTNUM, and MLTPT.

### MLRFTDTC
- **Order:** 34
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by MLTPTREF in ISO 8601 character format.

### MIDS
- **Order:** 35
- **Label:** Disease Milestone Instance Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The name of a specific instance of a disease milestone type (MIDSTYPE) described in the Trial Disease Milestones dataset. This should be unique within a subject. Used only in conjunction with RELMIDS and MIDSDTC.

### RELMIDS
- **Order:** 36
- **Label:** Temporal Relation to Milestone Instance
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The temporal relationship of the observation to the disease milestone instance name in MIDS. Examples: "IMMEDIATELY BEFORE", "AT TIME OF", "AFTER".

### MIDSDTC
- **Order:** 37
- **Label:** Disease Milestone Instance Date/Time
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The start date/time of the disease milestone instance name in MIDS, in ISO 8601 format.
---

## Cross References

### Controlled Terminology
- [Pharmaceutical Dosage Form (C66726)](../../terminology/core/interventions.md) — MLDOSFRM
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MLPRESP, MLOCCUR
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MLSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — MLDOSU
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Interventions):** AG, CM, EC, EX, PR, SU

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Interventions class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/ML/assumptions.md -->
# ML — Assumptions

1. The ML domain is used to represent consumption of any food or nutritional item that would not be represented in the exposure domains (EC/EX), Concomitant/Prior Medications (CM), Procedure Agents (AG), or Substance Use (SU). Examples of nutritional items that would be represented in other domains include:
   a. Investigational nutritional products (represented in EC/EX)
   b. Food or drink used to treat hypoglycemic events (represented in CM)
   c. Glucose given as part of a glucose tolerance test (represented in AG)
   d. Caffeinated drinks (represented in SU)

   The nutritional items represented in ML may be prospectively defined within a protocol, collected retrospectively as potential precipitants of clinical events, and/or to describe nutritional intake.

2. Additional timing variables
   a. Any additional timing variables may be added to this domain.
   b. Consumption of a food product is considered to occur over an interval of time (as opposed to a point in time). If start and end date/times are collected, they should be represented in MLSTDTC and MLENDTC, respectively. If only a start date/time is collected, it should not be copied to MLENDTC.

3. Any identifier variables, timing variables, or findings general observation-class qualifiers may be added to the ML domain, but the following qualifiers would generally not be used: --MOOD, --LOT, --LOC, --LAT, --DIR, --PORTOT.

<!-- source: knowledge_base/domains/MS/spec.md -->
# MS — Microbiology Susceptibility

> Class: Findings | Structure: One record per microbiology susceptibility test (or other organism-related finding) per organism found in MB

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

### NHOID
- **Order:** 4
- **Label:** Non-host Organism ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism which should only be used when the organism is the subject of the TEST. This variable should be populated with an intuitive name based on the identity of the non-host organism as reported by a lab (e.g., "A/California/7/2009 (H1N1)"). It is not to be used as a qualifier of the result in the record on which it appears.

### MSSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1.

### MSGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain. In SDTMIG v3.2 this was an Expected variable. In this version, the core designation has been changed to Permissible.

### MSREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier (e.g., an identifier for the culture/isolate being tested for susceptibility).

### MSSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.

### MSLNKID
- **Order:** 9
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship. For example, it may be used to link genetic findings (in the PF domain) about a microbe to the original culture of that microbe (in MB), or to susceptibility records (in MS) if needed.

### MSTESTCD
- **Order:** 10
- **Label:** Short Name of Assessment
- **Type:** Char
- **Controlled Terms:** C128688
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for MSTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in MSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). MSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MIC" for Minimum Inhibitory Concentration; "MICROSUS" for Microbial Susceptibility.

### MSTEST
- **Order:** 11
- **Label:** Name of Assessment
- **Type:** Char
- **Controlled Terms:** C128687
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in MSTEST cannot be longer than 40 characters. Examples: "Minimum Inhibitory Concentration", "Microbial Susceptibility".

### MSAGENT
- **Order:** 12
- **Label:** Agent Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** The name of the agent for which resistance is tested. The agent specified may be based on genetic markers or direct phenotypic drug sensitivity testing. Examples: "Penicillin", name of study drug.

### MSCONC
- **Order:** 13
- **Label:** Agent Concentration
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Numeric concentration of agent listed in MSAGENT.

### MSCONCU
- **Order:** 14
- **Label:** Agent Concentration Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Units for value of the agent concentration listed in MSCONC. Example: "mg/L".

### MSTSTDTL
- **Order:** 15
- **Label:** Measurement, Test or Examination Detail
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of MSTESTCD and MSTEST.

### MSCAT
- **Order:** 16
- **Label:** Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of MSTEST values.

### MSSCAT
- **Order:** 17
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of MSCAT values.

### MSORRES
- **Order:** 18
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### MSORRESU
- **Order:** 19
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for MSORRES. Examples: "ug/mL".

### MSSTRESC
- **Order:** 20
- **Label:** Result or Finding in Standard Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from MSORRES in a standard format or in standard units. MSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in MSSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in MSORRES and these results effectively have the same meaning, they could be represented in standard format in MSSTRESC as "NEGATIVE".

### MSSTRESN
- **Order:** 21
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from MSSTRESC. MSSTRESN should store all numeric test results or findings.

### MSSTRESU
- **Order:** 22
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for MSSTRESC and MSSTRESN. Example: "mol/L".

### MSNRIND
- **Order:** 23
- **Label:** Normal/Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the value is outside the normal range or reference range. May be defined by MSORNRLO and MSORNRHI or other objective criteria. Examples: "Y", "N", "HIGH", "LOW", "NORMAL". "ABNORMAL".

### MSRESCAT
- **Order:** 24
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** C85495
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding. In SDTMIG v3.2, MSRESCAT was used to categorize a numeric susceptibility result represented in MSORRES as either "SUSCEPTIBLE", "INTERMEDIATE", or "RESISTANT". However, results from some susceptibility tests may report only a categorical result and not a numeric result. Thus, in order for susceptibility results to be represented consistently, MSRESCAT should no longer be used for this purpose. In this version, the core designation has been changed from Expected to Permissible.

### MSSTAT
- **Order:** 25
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### MSREASND
- **Order:** 26
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with MSSTAT when value is "NOT DONE".

### MSXFN
- **Order:** 27
- **Label:** External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Filename for an external file.

### MSNAM
- **Order:** 28
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the vendor (e.g., laboratory) that provided the test results.

### MSLOINC
- **Order:** 29
- **Label:** LOINC Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Logical Observation Identifiers Names and Codes (LOINC) code for the topic variable such as a lab test.

### MSSPEC
- **Order:** 30
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Example: "SPUTUM".

### MSSPCCND
- **Order:** 31
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the condition of the specimen. Example: "CLOUDY".

### MSLOC
- **Order:** 32
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement.

### MSLAT
- **Order:** 33
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### MSDIR
- **Order:** 34
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### MSMETHOD
- **Order:** 35
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "EPSILOMETER", "MACRO BROTH DILUTION".

### MSANMETH
- **Order:** 36
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result (e.g., an image or a genetic sequence).

### MSLOBXFL
- **Order:** 37
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### MSBLFL
- **Order:** 38
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that MSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### MSFAST
- **Order:** 39
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status. Valid values include "Y", "N", "U", or null if not relevant.

### MSDRVFL
- **Order:** 40
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### MSEVAL
- **Order:** 41
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "MICROSCOPIST".

### MSEVALID
- **Order:** 42
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in MSEVAL. Examples: "RADIOLOGIST1" or "RADIOLOGIST2".

### MSACPTFL
- **Order:** 43
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than 1 assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null.

### MSLLOQ
- **Order:** 44
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units will be those used for MSSTRESU.

### MSULOQ
- **Order:** 45
- **Label:** Upper Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates the upper limit of quantitation for an assay. Units will be those used for MSSTRESU.

### MSREPNUM
- **Order:** 46
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.

### VISITNUM
- **Order:** 47
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 48
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 49
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 50
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the specimen was collected.

### EPOCH
- **Order:** 51
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the specimen was collected.

### MSDTC
- **Order:** 52
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of an observation.

### MSDY
- **Order:** 53
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### MSDUR
- **Order:** 54
- **Label:** Duration
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of an event, intervention, or finding. Used only if collected on the CRF and not derived.

### MSTPT
- **Order:** 55
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See MSTPTNUM and MSTPTREF.

### MSTPTNUM
- **Order:** 56
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### MSELTM
- **Order:** 57
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (MSTPTREF; e.g., previous dose, previous meal). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### MSTPTREF
- **Order:** 58
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by MSELTM, MSTPTNUM, and MSTPT. Example: "PREVIOUS DOSE".

### MSRFTDTC
- **Order:** 59
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by MSTPTREF.

### MSEVLINT
- **Order:** 60
- **Label:** Evaluation Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Duration of interval associated with an observation such as a finding MSTESTCD. Example: "-P2M" to represent a period of the past 2 months before the assessment.

### MSEVINTX
- **Order:** 61
- **Label:** Evaluation Interval Text
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS".
---

## Cross References

### Controlled Terminology
- [Microbiology Susceptibility Test Name (C128687)](../../terminology/core/microbiology_part1.md) — MSTEST
- [Microbiology Susceptibility Test Code (C128688)](../../terminology/core/microbiology_part1.md) — MSTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — MSLOBXFL, MSBLFL, MSFAST, MSDRVFL, MSACPTFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — MSSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — MSCONCU, MSORRESU, MSSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — MSLOC
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — MSSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — MSSPEC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — MSEVAL
- [Reference Range Indicator (C78736)](../../terminology/core/general_part4.md) — MSNRIND
- [Method (C85492)](../../terminology/core/general_part3.md) — MSMETHOD
- [Microbiology Susceptibility Testing Result Category (C85495)](../../terminology/core/microbiology_part1.md) — MSRESCAT
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — MSEVALID
- [Laterality (C99073)](../../terminology/core/general_part2.md) — MSLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — MSDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Shared Dataset:** [MB](../MB/) — microbiology organism identification
- **Specimen:** [BS](../BS/) — susceptibility specimen data
- **Specimen Relationship:** [RELSPEC](../RELSPEC/) — specimen hierarchy

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/MS/assumptions.md -->
# MS — Assumptions

1. Microbiology Susceptibility testing includes testing of the following types:
   a. Phenotypic drug susceptibility testing (qualitative), which may involve determining susceptibility/resistance (qualitative) at a predefined concentration of drug, or determining a specific dose (quantitative) at which a drug inhibits organism growth or some other process associated with virulence.
      i. For studies using qualitative testing methods, MSAGENT, MSCONC, and MSCONCU are used to represent the predefined drug, concentration, and units, respectively. Results are represented with values such as "SUSCEPTIBLE" or "RESISTANT".
      ii. For studies using quantitative testing methods, MSAGENT is used to represent the drug being tested; MSCONC and MSCONCU are not used. The concentration at which growth is inhibited is the result in these cases (MSORRES, MSSTRESC/MSSTRESN), with units being represented in MSORRESU/MSSTRESU.
      iii. As in 1.a.ii, MSAGENT should be populated with the drug whose action would be affected by the genetic marker being assessed via the genotypic test. MSCONC and MSCONCU are null in these records.
   b. Genetic tests that provide results in terms of susceptible/resistant only (e.g., nucleic acid amplification tests (NAAT)). Genotypic tests that provide results in terms of specific changes to nucleotides, codons, or amino acids of genes/gene products associated with resistance should be represented in the Genomic Findings (GF) domain, as that domain structure contains the variables necessary to accommodate data of this type. If a test provides both mutation data and susceptibility data, the mutation results should be represented in GF and the susceptibility information should be represented in MS. In these cases, the GF records should be linked via RELREC to susceptibility records in MS.
   c. CDISC Controlled Terminology Rules for Microbiology (MB/MS) domains are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

2. MSDTC represents the date the specimen was collected.

3. If the specimen was cultured, the start and end date of culture are represented in the Biospecimen Events (BE) domain in BESTDTC and BEENDTC respectively. --REFID represents the sample ID as originally assigned in the BE domain. See BE domain assumptions in the SDTMIG v3.4, Section 6.2.2, for guidelines on assigning --REFID values to samples and subsamples.
   a. Culture dates can be connected to the MS record via MSREFID and BEREFID.
   b. If the same sample is associated with many biospecimen events and tests, users may need to make use of additional linking variables such as --LNKID.

4. NHOID is a sponsor-defined, intuitive name of the non-host organism being tested. It should only be populated with values representing what is known about the identity of the organism before the results of the test are determined. It should therefore never be used as a qualifier of result.

5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the MS domain, but the following variables would not generally be used: --MODIFY, --BODSYS, --TOX, --TOXGR --SEV.

<!-- source: knowledge_base/domains/NV/spec.md -->
# NV — Nervous System Findings

> Class: Findings | Structure: One record per finding per location per time point per visit per subject

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

### FOCID
- **Order:** 4
- **Label:** Focus of Study-Specific Interest
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed, such as a drug application site (e.g., "Injection site 1", "Biopsy site 1", "Treated site 1") or a more specific focus (e.g., "OD" (right eye), "Upper left quadrant of the back"). The value in this variable should have inherent semantic meaning.

### NVSEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### NVGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### NVREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external procedure identifier.

### NVSPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page.

### NVLNKID
- **Order:** 9
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link a procedure to the assessment results over the course of the study.

### NVLNKGRP
- **Order:** 10
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### NVTESTCD
- **Order:** 11
- **Label:** Short Name of Nervous System Test
- **Type:** Char
- **Controlled Terms:** C116104
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in NVTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in NVTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). NVTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SUVR", "N75LAT", "P100LAT","N145LAT".

### NVTEST
- **Order:** 12
- **Label:** Name of Nervous System Test
- **Type:** Char
- **Controlled Terms:** C116103
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in NVTEST cannot be longer than 40 characters. Examples: "Standard Uptake Value Ratio", "N75 Latency", "P100 Latency", "N145 Latency".

### NVCAT
- **Order:** 13
- **Label:** Category for Nervous System Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Example: "VISUAL EVOKED POTENTIAL".

### NVSCAT
- **Order:** 14
- **Label:** Subcategory for Nervous System Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of NVCAT values.

### NVORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the procedure measurement or finding as originally received or collected.

### NVORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for NVORRES.

### NVSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from NVORRES, in a standard format or standard units. NVSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in NVSTRESN.

### NVSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from NVSTRESC. NVSTRESN should store all numeric test results or findings.

### NVSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for NVSTRESC or NVSTRESN.

### NVSTAT
- **Order:** 20
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a test was not done, or a measurement was not taken. Should be null if a result exists in NVORRES.

### NVREASND
- **Order:** 21
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with NVSTAT when value is "NOT DONE".

### NVLOC
- **Order:** 22
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Examples: "BRAIN", "EYE", "PRECUNEUS", "CINGULATE CORTEX".

### NVLAT
- **Order:** 23
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### NVDIR
- **Order:** 24
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### NVMETHOD
- **Order:** 25
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "EEG", "PET/CT SCAN ", "FDGPET".

### NVLOBXFL
- **Order:** 26
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### NVBLFL
- **Order:** 27
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that NVBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### NVDRVFL
- **Order:** 28
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### NVEVAL
- **Order:** 29
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".

### NVEVALID
- **Order:** 30
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in NVEVAL. Examples: "RADIOLOGIST 1", "RADIOLOGIST 2".

### VISITNUM
- **Order:** 31
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 32
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 33
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 34
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 35
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### NVDTC
- **Order:** 36
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date of procedure or test.

### NVDY
- **Order:** 37
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the procedure or test, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### NVTPT
- **Order:** 38
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See NVTPTNUM and NVTPTREF. Examples: "START", "5 MIN POST".

### NVTPTNUM
- **Order:** 39
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of NVTPT to aid in sorting.

### NVELTM
- **Order:** 40
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a fixed time point reference (NVTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by NVTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by NVTPTREF.

### NVTPTREF
- **Order:** 41
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by NVELTM, NVTPTNUM, and NVTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### NVRFTDTC
- **Order:** 42
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by --TPTREF in ISO 8601 character format.
---

## Cross References

### Controlled Terminology
- [Nervous System Findings Test Name (C116103)](../../terminology/core/other_part2.md) — NVTEST
- [Nervous System Findings Test Code (C116104)](../../terminology/core/other_part2.md) — NVTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — NVLOBXFL, NVBLFL, NVDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — NVSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — NVORRESU, NVSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — NVLOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — NVEVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — NVMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — NVEVALID
- [Laterality (C99073)](../../terminology/core/general_part2.md) — NVLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — NVDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/NV/assumptions.md -->
# NV — Assumptions

1. Methods of assessment for nervous system findings may include nerve conduction studies, electroencephalogram (EEG), electromyography (EMG), and imaging.

2. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the NV domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --LOINC, --TOX, --TOXGR.

<!-- source: knowledge_base/domains/OE/spec.md -->
# OE — Ophthalmic Examinations

> Class: Findings | Structure: One record per ophthalmic finding per method per location, per time point per visit per subject

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

### FOCID
- **Order:** 4
- **Label:** Focus of Study-Specific Interest
- **Type:** Char
- **Controlled Terms:** C119013
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identification of a focus of study-specific interest on or within a subject or specimen as called out in the protocol for which a measurement, test, or examination was performed.

### OESEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### OEGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### OELNKID
- **Order:** 7
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### OELNKGRP
- **Order:** 8
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### OETESTCD
- **Order:** 9
- **Label:** Short Name of Ophthalmic Test or Exam
- **Type:** Char
- **Controlled Terms:** C117743
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for OETEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in OETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). OETESTCD cannot contain characters other than letters, numbers, or underscores. Example: "NUMLCOR".

### OETEST
- **Order:** 10
- **Label:** Name of Ophthalmic Test or Exam
- **Type:** Char
- **Controlled Terms:** C117742
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name for the test or examination used to obtain the measurement or finding. The value in OETEST cannot be longer than 40 characters. Example: "Number of Letters Correct" for OETESTCD = "NUMLCOR".

### OETSTDTL
- **Order:** 11
- **Label:** Ophthalmic Test or Exam Detail
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of OETESTCD and OETEST.

### OECAT
- **Order:** 12
- **Label:** Category for Ophthalmic Test or Exam
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Examples: "VISUAL ACUITY", "CONTRAST SENSITIVITY", "OCULAR COMFORT".

### OESCAT
- **Order:** 13
- **Label:** Subcategory for Ophthalmic Test or Exam
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of OECAT values. Example: "HIGH CONTRAST" or "LOW CONTRAST" when OECAT is "VISUAL ACUITY".

### OEORRES
- **Order:** 14
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected. Examples: "120", "<1, NORMAL", "RED SPOT VISIBLE".

### OEORRESU
- **Order:** 15
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original unit for OEORRES. Examples: "mm", "um".

### OEORNRLO
- **Order:** 16
- **Label:** Normal Range Lower Limit-Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of normal range or reference range for results stored in OEORRES.

### OEORNRHI
- **Order:** 17
- **Label:** Normal Range Upper Limit-Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of normal range or reference range for results stored in OEORRES.

### OESTRESC
- **Order:** 18
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from OEORRES, in a standard format or in standard units. OESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in OESTRESN.

### OESTRESN
- **Order:** 19
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from OESTRESC. OESTRESN should store all numeric test results or findings.

### OESTRESU
- **Order:** 20
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized units used for OESTRESC and OESTRESN. Examples: "mm", "um".

### OESTNRLO
- **Order:** 21
- **Label:** Normal Range Lower Limit-Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Lower end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU).

### OESTNRHI
- **Order:** 22
- **Label:** Normal Range Upper Limit-Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Upper end of normal range or reference range for standardized results (e.g., OESTRESC, OESTRESN) represented in standardized units (OESTRESU).

### OESTNRC
- **Order:** 23
- **Label:** Normal Range for Character Results
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Normal range or reference range for results stored in OESTRESC that are character in ordinal or categorical scale. Example: "Negative to Trace".

### OENRIND
- **Order:** 24
- **Label:** Normal/Reference Range Indicator
- **Type:** Char
- **Controlled Terms:** C78736
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the value is outside the normal range or reference range. May be defined by OEORNRLO and OEORNRHI or other objective criteria. Examples: "Y", "N"; "HIGH", "LOW"; "NORMAL", "ABNORMAL".

### OERESCAT
- **Order:** 25
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding or medical status per interpretation of test results. Examples: "POSITIVE", "NEGATIVE". The variable OERESCAT is not meant to replace the use of OENRIND for cases where normal ranges are provided.

### OESTAT
- **Order:** 26
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### OEREASND
- **Order:** 27
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with OESTAT when value is "NOT DONE".

### OEXFN
- **Order:** 28
- **Label:** External File Path
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Filename for an external file, such as one for a retinal OCT image.

### OELOC
- **Order:** 29
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Examples: "EYE" for a finding record relative to the complete eye, "RETINA" for a measurement or assessment of only the retina.

### OELAT
- **Order:** 30
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### OEDIR
- **Order:** 31
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### OEPORTOT
- **Order:** 32
- **Label:** Portion or Totality
- **Type:** Char
- **Controlled Terms:** C99075
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing the distribution (i.e., arrangement of, apportioning of). Examples: "ENTIRE", "SINGLE", "SEGMENT", "MANY".

### OEMETHOD
- **Order:** 33
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Method of the test or examination. Example: "ETDRS EYE CHART" for OETESTCD = "NUMLCOR". The different methods may offer different functionality or granularity, affecting the set of results and associated meaning.

### OELOBXFL
- **Order:** 34
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### OEBLFL
- **Order:** 35
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that OEBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### OEDRVFL
- **Order:** 36
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### OEEVAL
- **Order:** 37
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "INDEPENDENT ASSESSOR", "INVESTIGATOR".

### OEEVALID
- **Order:** 38
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in OEEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2".

### OEACPTFL
- **Order:** 39
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than one assessor provides an evaluation of a result or response, this flag identifies the record that is considered, by an independent assessor, to be the accepted evaluation. Expected to be "Y" or null.

### OEREPNUM
- **Order:** 40
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The incidence number of a test that is repeated within a given timeframe for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Examples: multiple measurements of blood pressure, multiple analyses of a sample.

### VISITNUM
- **Order:** 41
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 42
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 43
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 44
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 45
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### OEDTC
- **Order:** 46
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date/time of the observation.

### OEDY
- **Order:** 47
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Actual study day of observation/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### OETPT
- **Order:** 48
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point.

### OETPTNUM
- **Order:** 49
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### OEELTM
- **Order:** 50
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (OETPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### OETPTREF
- **Order:** 51
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by OETPT, OETPTNUM, and OEELTM.

### OERFTDTC
- **Order:** 52
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, OETPTREF.
---

## Cross References

### Controlled Terminology
- [Ophthalmic Exam Test Name (C117742)](../../terminology/core/other_part2.md) — OETEST
- [Ophthalmic Exam Test Code (C117743)](../../terminology/core/other_part2.md) — OETESTCD
- [Ophthalmic Focus of Study Specific Interest (C119013)](../../terminology/core/other_part2.md) — FOCID
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — OELOBXFL, OEBLFL, OEDRVFL, OEACPTFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — OESTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — OEORRESU, OESTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — OELOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — OEEVAL
- [Reference Range Indicator (C78736)](../../terminology/core/general_part4.md) — OENRIND
- [Method (C85492)](../../terminology/core/general_part3.md) — OEMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — OEEVALID
- [Laterality (C99073)](../../terminology/core/general_part2.md) — OELAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — OEDIR
- [Portion/Totality (C99075)](../../terminology/core/general_part4.md) — OEPORTOT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/OE/assumptions.md -->
# OE — Assumptions

1. In ophthalmic studies, the eyes are usually sites of treatment. It is appropriate to identify sites using the variable FOCID. When FOCID is used to identify the eyes, it is recommended that the values "OD" (oculus dexter, right eye), "OS" (oculus sinister, left eye), and "OU" (oculus uterque, both eyes) be used in FOCID. These terms are the exclusively preferred terms used by the ophthalmology community as abbreviations for the expanded Latin terms, and are included in the nonextensible CDISC Ophthalmic Focus of Study Specific Interest (OEFOCUS) codelist.

2. In any study that uses FOCID, FOCID would be included in records in any subject-level domain representing findings, interventions, or events (e.g., Adverse Events) related to the eyes. Whether or not FOCID is used in a study, --LOC and --LAT should be populated in records related to the eyes. The value in OELOC may be "EYE" but may also be a part of the eye (e.g., "RETINA", "CORNEA").

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the OE domain, but the following qualifiers would not generally be used: --MODIFY, --NSPCES, --POS, --BODSYS, --ORREF, --STREFC, --STREFN, --CHRON, --DISTR, --ANTREG, --LEAD, --FAST, --TOX, --TOXGR, --LLOQ, --ULOQ.

<!-- source: knowledge_base/domains/OI/spec.md -->
# OI — Non-host Organism Identifiers

> Class: Study Reference | Structure: One record per taxon per non-host organism

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

### NHOID
- **Order:** 3
- **Label:** Non-host Organism Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sponsor-defined identifier for a non-host organism. NHOID should be populated with an intuitive name based on the identity of the organism as reported by the lab. It must be unique for each unique organism as defined by the specific values of the organism's entire known taxonomy described by pairs of OIPARMCD and OIVAL .

### OISEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to given to ensure uniqueness within a parameter within an organism (NHOID) within dataset.

### OIPARMCD
- **Order:** 5
- **Label:** Non-host Organism ID Element Short Name
- **Type:** Char
- **Controlled Terms:** C179591
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the taxon being described. Examples: "GROUP", "GENTYP", "SUBTYP".

### OIPARM
- **Order:** 6
- **Label:** Non-host Organism ID Element Name
- **Type:** Char
- **Controlled Terms:** C179590
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name of the taxon being described. Examples: "Group", "Genotype", "Subtype".

### OIVAL
- **Order:** 7
- **Label:** Non-host Organism ID Element Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Req
- **CDISC Notes:** Value for the taxon in OIPARMCD/OIPARM for the organism identified by NHOID.
---

## Cross References

### Controlled Terminology
- [Non-host Organism Identifier Parameters (C179590)](../../terminology/core/oi.md) — OIPARM
- [Non-host Organism Identifier Parameters Code (C179591)](../../terminology/core/oi.md) — OIPARMCD

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Study Reference class definition](../../model/05_study_level_data.md)

<!-- source: knowledge_base/domains/OI/assumptions.md -->
# OI — Assumptions

A special-purpose domain containing information that identifies levels of taxonomic nomenclature of microbes or parasites that have been either experimentally determined in the course of a study or are previously known, as in the case of lab strains used as reference in the study.

The biological classification of a non-host organism typically stops at the taxonomic rank of "species." Scientific taxonomic nomenclature below the rank of species is not clearly defined, lacks a globally accepted standard terminology, and is frequently organism-dependent. Therefore, the OI domain addresses organism taxonomy with a series of parameters that name the taxa appropriate to the organism and the granularity with which the organism has been identified in the particular study.

1. Non-host organisms include viruses and organisms such as pathogens or parasites, but also non-pathogenic organisms such as normal intestinal flora. Non-host organism identifiers are not to be used for host species identification (e.g., for animals used in preclinical studies), nor should they be used to represent other, non-taxonomy characteristics of non-host species (e.g., drug susceptibility, growth rates).

2. NHOID is sponsor-defined, with the following constraints:
    a. A unique NHOID must represent a unique identity as represented in its combination of OIPARMCD/OIVAL pairs. If 2 organisms share the same first 2 levels of taxonomy with regard to OIPARMCD/OIVAL, but 1 is identified to a third level and the other is not, they should be assigned 2 unique NHOIDs.
    b. Study sponsors should populate NHOID with intuitive name values based on either
        i. the name of the organism as reported by a lab or specified by the investigator, or
        ii. published references/databases where applicable and appropriate (e.g., when reference strain H77 is used in a HCV study, NHOID for this strain should be populated with "H77" or "HCV1a-H77").

3. NHOID can be used in any domain where observations about these organisms are being represented, allowing end users to determine what is known about the organism's identity by merging on NHOID, or by otherwise referring to the OI domain.

4. OIPARMCD and OIPARM must represent parameters for the identification of non-host organisms with regard to nomenclature only.
    a. Mostly, this will represent taxonomic ranks (i.e., species) as well as commonly used grouping terms (taxa that are not officially ranked, e.g., subtype, group, strain).
    b. They may also include other nomenclature terms that are less widely known but are used frequently for organism identification in a specific field of study (e.g., spoligotype in tuberculosis).
    c. They should be listed in the OI dataset in hierarchical order of least to most specific with increasing OISEQ values.

5. Variables not listed in the OI domain specification table should not be used in OI data sets.

<!-- source: knowledge_base/domains/PC/spec.md -->
# PC — Pharmacokinetics Concentrations

> Class: Findings | Structure: One record per sample characteristic or time-point concentration per reference time point or per analyte per subject

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

### PCSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### PCGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain to support relationships within the domain and between domains.

### PCREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier.

### PCSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number.

### PCTESTCD
- **Order:** 8
- **Label:** Pharmacokinetic Test Short Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the analyte or specimen characteristic. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "ASA", "VOL", "SPG".

### PCTEST
- **Order:** 9
- **Label:** Pharmacokinetic Test Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name of the analyte or specimen characteristic. Note any test normally performed by a clinical laboratory is considered a lab test. The value in PCTEST cannot be longer than 40 characters. Examples: "Acetylsalicylic Acid", "Volume", "Specific Gravity".

### PCCAT
- **Order:** 10
- **Label:** Test Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records. Examples: "ANALYTE", "SPECIMEN PROPERTY".

### PCSCAT
- **Order:** 11
- **Label:** Test Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of a test category.

### PCORRES
- **Order:** 12
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### PCORRESU
- **Order:** 13
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C85494
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for PCORRES. Example: "mg/L".

### PCSTRESC
- **Order:** 14
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from PCORRES in a standard format or standard units. PCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in PCORRES, and these results effectively have the same meaning, they could be represented in standard format in PCSTRESC as "NEGATIVE". For other examples, see general assumptions.

### PCSTRESN
- **Order:** 15
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from PCSTRESC. PCSTRESN should store all numeric test results or findings.

### PCSTRESU
- **Order:** 16
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C85494
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for PCSTRESC and PCSTRESN.

### PCSTAT
- **Order:** 17
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a result was not obtained. Should be null if a result exists in PCORRES.

### PCREASND
- **Order:** 18
- **Label:** Reason Test Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a result was not obtained, such as "SPECIMEN LOST". Used in conjunction with PCSTAT when value is "NOT DONE".

### PCNAM
- **Order:** 19
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Name or identifier of the laboratory or vendor who provides the test results.

### PCSPEC
- **Order:** 20
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE".

### PCSPCCND
- **Order:** 21
- **Label:** Specimen Condition
- **Type:** Char
- **Controlled Terms:** C78733
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Free or standardized text describing the condition of the specimen. Examples: "HEMOLYZED", "ICTERIC", "LIPEMIC".

### PCMETHOD
- **Order:** 22
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination. Examples: "HPLC/MS", "ELISA". This should contain sufficient information and granularity to allow differentiation of various methods that might have been used within a study.

### PCFAST
- **Order:** 23
- **Label:** Fasting Status
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify fasting status.

### PCDRVFL
- **Order:** 24
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records, which do not come from the CRF, are examples of records that would be derived for the submission datasets. If PCDRVFL = "Y", then PCORRES may be null with PCSTRESC, and PCSTRESN (if the result is numeric) having the derived value.

### PCLLOQ
- **Order:** 25
- **Label:** Lower Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Indicates the lower limit of quantitation for an assay. Units should be those used in PCSTRESU.

### PCULOQ
- **Order:** 26
- **Label:** Upper Limit of Quantitation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates the upper limit of quantitation for an assay. Units should be those used in PCSTRESU.

### VISITNUM
- **Order:** 27
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 28
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 29
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

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
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### PCDTC
- **Order:** 32
- **Label:** Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of specimen collection represented in ISO 8601 character format. If there is no end time, then this will be the collection time.

### PCENDTC
- **Order:** 33
- **Label:** End Date/Time of Specimen Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** End date/time of specimen collection represented in ISO 8601 character format. If there is no end time, the collection time should be stored in PCDTC, and PCENDTC should be null.

### PCDY
- **Order:** 34
- **Label:** Actual Study Day of Specimen Collection
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of specimen collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### PCENDY
- **Order:** 35
- **Label:** Study Day of End of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### PCTPT
- **Order:** 36
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when specimen should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See PCTPTNUM and PCTPTREF. Examples: "Start", "5 min post".

### PCTPTNUM
- **Order:** 37
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of PCTPT to aid in sorting.

### PCELTM
- **Order:** 38
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (PCTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date time variable.

### PCTPTREF
- **Order:** 39
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point used as a basis for PCTPT, PCTPTNUM, and PCELTM. Example: "MOST RECENT DOSE".

### PCRFTDTC
- **Order:** 40
- **Label:** Date/Time of Reference Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point described by PCTPTREF.

### PCEVLINT
- **Order:** 41
- **Label:** Evaluation Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation Interval associated with a PCTEST record represented in ISO 8601 character format. Example: "-PT2H" to represent an evaluation interval of 2 hours prior to a PCTPT.
---

## Cross References

### Controlled Terminology
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — PCFAST, PCDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — PCSTAT
- [Specimen Condition (C78733)](../../terminology/core/general_part4.md) — PCSPCCND
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — PCSPEC
- [Method (C85492)](../../terminology/core/general_part3.md) — PCMETHOD
- [PK Units of Measure (C85494)](../../terminology/core/other_part3.md) — PCORRESU, PCSTRESU
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Shared Dataset:** [PP](../PP/) — pharmacokinetic concentrations → parameters

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/PC/assumptions.md -->
# PC — Assumptions

1. This domain can be used to represent specimen properties (e.g., volume, pH) in addition to drug and metabolite concentration measurements.

2. CDISC Controlled Terminology Rules for Pharmacokinetics are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PC domain, but the following Qualifiers would not generally be used: --BODSYS, --SEV.

<!-- source: knowledge_base/domains/PE/spec.md -->
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

<!-- source: knowledge_base/domains/PE/assumptions.md -->
# PE — Assumptions

1. PE findings reflect the presence or absence of physical signs of disease or abnormality observed during a general physical examination. Multiple body systems are assessed during a physical examination, often starting at the head and ending at the toes, where the body is evaluated by inspection, palpation (feeling with the hands), percussion (tapping with fingers), and auscultation (listening). The examination often includes macro assessments (e.g., normal/abnormal) of appearance, general health, behavior, and body system review from head to toe.
   a. Evaluation of targeted body systems (e.g., cardiovascular, ophthalmic, reproductive) as part of therapeutic specific assessments should be represented in the appropriate body system domain (e.g., CV, OE, RP, respectively).
   b. See CDASHIG Section 8.3.11, PE - Physical Examination (available at https://www.cdisc.org/standards/foundational/cdash/), for additional collection guidance.

2. Abnormalities observed during a physical examination may be encoded. When collected/reported as a PE finding, the verbatim value is represented in PEORRES and the encoded value in PESTRESC. When collected/reported as medical history or an adverse event, the verbatim value is represented in MHTERM or AETERM and the encoded value is represented in MHDECOD or AEDECOD, respectively.

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PE domain, but the following qualifiers would generally not be used: --XFN, --NAM, --LOINC, --FAST, --TOX, --TOXGR.

<!-- source: knowledge_base/domains/PP/spec.md -->
# PP — Pharmacokinetics Parameters

> Class: Findings | Structure: One record per PK parameter per time-concentration profile per modeling method per subject

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

### PPSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### PPGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain to support relationships within the domain and between domains.

### PPTESTCD
- **Order:** 6
- **Label:** Parameter Short Name
- **Type:** Char
- **Controlled Terms:** C85839
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the pharmacokinetic parameter. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in PPTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). PPTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "AUCALL", "TMAX", "CMAX".

### PPTEST
- **Order:** 7
- **Label:** Parameter Name
- **Type:** Char
- **Controlled Terms:** C85493
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name of the pharmacokinetic parameter. The value in PPTEST cannot be longer than 40 characters. Examples: "AUC All", "Time of CMAX", "Max Conc".

### PPCAT
- **Order:** 8
- **Label:** Parameter Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of related records. For PP, this should be the name of the analyte in PCTEST whose profile the parameter is associated with.

### PPSCAT
- **Order:** 9
- **Label:** Parameter Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Categorization of the model type used to calculate the PK parameters. Examples: "COMPARTMENTAL", "NON-COMPARTMENTAL".

### PPORRES
- **Order:** 10
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### PPORRESU
- **Order:** 11
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C85494; C128684; C128683; C128685; C128686
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for PPORRES. Example: "ng/L". See PP Assumption 3.

### PPSTRESC
- **Order:** 12
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from PPORRES in a standard format or standard units. PPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in PPSTRESN.

### PPSTRESN
- **Order:** 13
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from PPSTRESC. PPSTRESN should store all numeric test results or findings.

### PPSTRESU
- **Order:** 14
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C85494; C128684; C128683; C128685; C128686
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for PPSTRESC and PPSTRESN. See PP Assumption 3.

### PPSTAT
- **Order:** 15
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a parameter was not calculated. Should be null if a result exists in PPORRES.

### PPREASND
- **Order:** 16
- **Label:** Reason Parameter Not Calculated
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a parameter was not calculated, such as "INSUFFICIENT DATA". Used in conjunction with PPSTAT when value is "NOT DONE".

### PPSPEC
- **Order:** 17
- **Label:** Specimen Material Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Defines the type of specimen used for a measurement. If multiple specimen types are used for a calculation (e.g., serum and urine for renal clearance), then this field should be left blank. Examples: "SERUM", "PLASMA", "URINE".

### PPANMETH
- **Order:** 18
- **Label:** Analysis Method
- **Type:** Char
- **Controlled Terms:** C172330
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Analysis method applied to obtain a summarized result. Analysis method describes the method of secondary processing applied to a complex observation result. Example: A named formula used to calculate AUC, such as "LIN-LOG TRAPEZOIDAL METHOD".  Sponsor-defined formulas can also be represented by this variable. Example: Calculating ratio AUCs where the PPANMETH may be "DRUG METABOLITE 1 TO DRUG PARENT" or "DRUG METABOLITE 2 TO METABOLITE 1".

### TAETORD
- **Order:** 19
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 20
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the observation, or the date/time of collection if start date/time is not collected.

### PPDTC
- **Order:** 21
- **Label:** Date/Time of Parameter Calculations
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Nominal date/time of parameter calculations.

### PPDY
- **Order:** 22
- **Label:** Study Day of Parameter Calculations
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the collection, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.

### PPTPTREF
- **Order:** 23
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The description of a time point that acts as a fixed reference for a series of planned time points.

### PPRFTDTC
- **Order:** 24
- **Label:** Date/Time of Reference Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of the reference time point from the PC records used to calculate a parameter record. The values in PPRFTDTC should be the same as that in PCRFTDTC for related records.

### PPSTINT
- **Order:** 25
- **Label:** Planned Start of Assessment Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The start of a planned evaluation or assessment interval relative to the time point reference.

### PPENINT
- **Order:** 26
- **Label:** Planned End of Assessment Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** The end of a planned evaluation or assessment interval relative to the time point reference.
---

## Cross References

### Controlled Terminology
- [PK Units of Measure - Weight kg (C128683)](../../terminology/core/pk_part4.md) — PPORRESU, PPSTRESU
- [PK Units of Measure - Weight g (C128684)](../../terminology/core/pk_part3.md) — PPORRESU, PPSTRESU
- [PK Units of Measure - Dose mg (C128685)](../../terminology/core/pk_part3.md) — PPORRESU, PPSTRESU
- [PK Units of Measure - Dose ug (C128686)](../../terminology/core/pk_part3.md) — PPORRESU, PPSTRESU
- [PK Analytical Method (C172330)](../../terminology/core/pk_part1.md) — PPANMETH
- [Not Done (C66789)](../../terminology/core/general_part4.md) — PPSTAT
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — PPSPEC
- [PK Parameters (C85493)](../../terminology/core/pk_part1.md) — PPTEST
- [PK Units of Measure (C85494)](../../terminology/core/other_part3.md) — PPORRESU, PPSTRESU
- [PK Parameters Code (C85839)](../../terminology/core/pk_part2.md) — PPTESTCD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, QS, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Shared Dataset:** [PC](../PC/) — pharmacokinetic parameters ← concentrations

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/PP/assumptions.md -->
# PP — Assumptions

1. Pharmacokinetics Parameters is a derived dataset, and may be produced from an analysis dataset with a different structure. As a result, some sponsors may need to normalize their analysis dataset in order for it to fit into the SDTM-based PP domain.

2. Information pertaining to all parameters (e.g., number of exponents, model weighting) should be submitted in the SUPPPP dataset.

3. There are separate codelists used for PPORRESU/PPSTRESU where the choice depends on whether the value of the pharmacokinetic parameter is normalized.
   a. Codelist "PKUNIT" is used for non-normalized parameters.
   b. Codelists "PKUDMG" and "PKUDUG" are used when parameters are normalized by dose amount in milligrams or micrograms, respectively.
   c. Codelists "PKUWG" and "PKUWKG" are used when parameters are normalized by weight in grams or kilograms, respectively.

4. Multiple subset codelists were created for the unique unit expressions of the same concept across codelists. This approach allows study-context appropriate use of unit values for pharmacokinetics (PK) analysis subtypes. Controlled Terminology Rules for PK are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PP domain, but the following qualifiers would not generally be used: --BODSYS, --SEV.

<!-- source: knowledge_base/domains/PR/spec.md -->
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

<!-- source: knowledge_base/domains/PR/assumptions.md -->
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

<!-- source: knowledge_base/domains/QS/spec.md -->
# QS — Questionnaires

> Class: Findings | Structure: One record per questionnaire per question per time point per visit per subject

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

### QSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### QSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### QSSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Question number on a questionnaire.

### QSTESTCD
- **Order:** 7
- **Label:** Question Short Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Topic variable for QS. Short name for the value in QSTEST, which can be used as a column name when converting the dataset from a vertical format to a horizontal format. The value in QSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). QSTESTCD cannot contain characters other than letters, numbers, or underscores.  Controlled terminology for QSTESTCD is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTESTCD. Examples: "ADCCMD01", "BPR0103".

### QSTEST
- **Order:** 8
- **Label:** Question Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the question or group of questions used to obtain the measurement or finding. The value in QSTEST cannot be longer than 40 characters.  Controlled terminology for QSTEST is published in separate codelists for each questionnaire. See https://www.cdisc.org/standards/semantics/terminology for values for QSTEST. Example: "BPR01 - Emotional Withdrawal".

### QSCAT
- **Order:** 9
- **Label:** Category of Question
- **Type:** Char
- **Controlled Terms:** C100129
- **Role:** Grouping Qualifier
- **Core:** Req
- **CDISC Notes:** Used to specify the questionnaire in which the question identified by QSTEST and QSTESTCD was included. Examples: "ADAS-COG", "MDS-UPDRS".

### QSSCAT
- **Order:** 10
- **Label:** Subcategory for Question
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the questions within the category. Examples: "MENTAL HEALTH" , "DEPRESSION", "WORD RECALL".

### QSORRES
- **Order:** 11
- **Label:** Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Finding as originally received or collected (e.g., "RARELY", "SOMETIMES"). When sponsors apply codelist to indicate that code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores.

### QSORRESU
- **Order:** 12
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for QSORRES, such as minutes or seconds or the units associated with a visual analog scale.

### QSSTRESC
- **Order:** 13
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the finding for all questions or subscores copied or derived from QSORRES, in a standard format or standard units. QSSTRESC should store all findings in character format; if findings are numeric, they should also be stored in numeric format in QSSTRESN. If question scores are derived from the original finding, then the standard format is the score. Examples: "0", "1".  When sponsors apply codelist to indicate the code values are statistically meaningful standardized scores (which are defined by sponsors or by valid methodologies, e.g., SF36 questionnaires), QSORRES will contain the decode format; QSSTRESC and QSSTRESN may contain the standardized code values or scores.

### QSSTRESN
- **Order:** 14
- **Label:** Numeric Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric findings in standard format; copied in numeric format from QSSTRESC. QSSTRESN should store all numeric results or findings.

### QSSTRESU
- **Order:** 15
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for QSSTRESC or QSSTRESN.

### QSSTAT
- **Order:** 16
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not done or was not answered. Should be null if a result exists in QSORRES.

### QSREASND
- **Order:** 17
- **Label:** Reason Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a question was not answered. Used in conjunction with QSSTAT when value is "NOT DONE". Example: "SUBJECT REFUSED".

### QSMETHOD
- **Order:** 18
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C158113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination.

### QSLOBXFL
- **Order:** 19
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.

### QSBLFL
- **Order:** 20
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that QSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### QSDRVFL
- **Order:** 21
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or questionnaire subscores that do not come from the CRF are examples of records that would be derived for the submission datasets. If QSDRVFL = "Y", then QSORRES may be null with QSSTRESC and (if numeric) QSSTRESN having the derived value.

### VISITNUM
- **Order:** 22
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 23
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 24
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 25
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 26
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the observation date/time of the physical exam finding.

### QSDTC
- **Order:** 27
- **Label:** Date/Time of Finding
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date of questionnaire.

### QSDY
- **Order:** 28
- **Label:** Study Day of Finding
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of finding collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### QSTPT
- **Order:** 29
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when questionnaire should be administered. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See QSTPTNUM and QSTPTREF.

### QSTPTNUM
- **Order:** 30
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of QSTPT to aid in sorting.

### QSELTM
- **Order:** 31
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (QSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by QSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by QSTPTREF.

### QSTPTREF
- **Order:** 32
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by QSELTM, QSTPTNUM, and QSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### QSRFTDTC
- **Order:** 33
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, QSTPTREF.

### QSEVLINT
- **Order:** 34
- **Label:** Evaluation Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation interval associated with a QSTEST question represented in ISO 8601 character format. Example: "-P2Y" to represent an interval of 2 years in the question "Have you experienced any episodes in the past 2 years?".

### QSEVINTX
- **Order:** 35
- **Label:** Evaluation Interval Text
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS".
---

## Cross References

### Controlled Terminology
- [Category of Questionnaire (C100129)](../../terminology/core/qs_part1.md) — QSCAT
- [QRS Method (C158113)](../../terminology/core/general_part4.md) — QSMETHOD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — QSLOBXFL, QSBLFL, QSDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — QSSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — QSORRESU, QSSTRESU
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, RE, RP, RS, SC, SS, TR, TU, UR, VS
- **Findings About:** [FA](../FA/) — findings about questionnaire responses

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/QS/assumptions.md -->
# QS — Assumptions

There are no additional QS-specific assumptions; all are included in the QRS Shared Assumptions.

## QRS Shared Assumptions

The following assumptions are common to the FT and QS domains as well as the Clinical Classifications use case of the RS domain (not the Disease Response use case of RS):

1. The name of a QRS instrument is described under the variable --CAT in the relevant QRS domain (i.e., FT, QS, RS), and may be either abbreviations or longer names. For example, "ADAS-COG", "BPI SHORT FORM", and "APACHE II" are all --CATs which are shortened names for the instruments they represent, whereas "4 STAIR ASCEND" is the FTCAT for the instrument of the same name. Sponsors should always reference CDISC Controlled Terminology.
   a. The QRS Naming Rules for --CAT, --TEST, and --TESTCD and the list of QRS instruments that have published CDISC Controlled Terminology with NCI/EVS are available at: https://www.cdisc.org/standards/terminology/controlled-terminology.
   b. Refer to the following CDISC Controlled Terminology codelists for QRS instrument --CAT terminology:
      i. Category of Clinical Classification
      ii. Category of Functional Test
      iii. Category of Questionnaire
   c. QRS --TESTCD/--TEST terminology codelists are listed separately by instrument name.

2. Names of subcategories for groups of items/questions are described under the --SCAT variable.
   a. --SCAT values are not included in the CDISC Controlled Terminology system but rather controlled as described in the QRS supplements in which they are used.

3. There are cases where QRS CRFs do not include numeric "standardized responses" assigned to text responses (e.g., mild, moderate, severe being 1, 2, 3). It is clearly in everyone's best interest to include the numeric "standardized responses" in the SDTMIG QRS dataset. This is only done when the numeric "standardized responses" are documented in the QRS CRF instructions, a user manual, a website specific to the QRS instrument, or another reference document that provides a clear explanation and rationale for providing them in the SDTMIG QRS dataset.

4. Sponsors should always consult published QRS supplements for guidance on submitting derived information in a SDTMIG QRS domain. Derived variable results in QRS are usually considered captured data. If sponsors operationally derive variable results, then the derived records that are submitted in a QRS domain should be flagged by --DRVFL.
   a. The following rules apply for "total"-type scores in QRS datasets.
      i. QRS subtotal, total, etc. scores listed on the CRF are considered captured data and are included in the instrument's controlled terminology.
      ii. QRS subtotal, total, etc. scores not listed on the CRF but documented in an associated instrument manual or reference paper are considered captured data and are included in the instrument's controlled terminology.
      iii. QRS subtotal, total, etc. scores not listed on the CRF, but known to be included in eData by sponsors are considered as captured data, are included in the instrument's controlled terminology. The QRS instrument's CT is considered extensible for this case and the subtotal or total score should be requested to be added.
         1. Any imputations/calculations done to numeric "standardized responses" to produce the total score via transforming numeric "standardized responses" in any way would be done as ADaM derivations.
   b. The QRS instrument subtotal or total score, which is the sum of the numeric responses for an instrument, is populated in --ORRES, --STRESC, and --STRESN. It is considered a captured subtotal or total score without any knowledge of the sponsor-data management processes related to the score.
      i. If operationally derived by the sponsor, it is the sponsor's responsibility to set the --DRVFL flag based on their eCRF process to derive subtotal and total scores. An investigator-derived score written on a CRF will be considered a captured score and not flagged. When subtotal and total scores are derived by the sponsor, the derived flag (--DRVFL) is set to "Y". However, when the subtotal and total scores are received from a central provider or vendor, the value would go into --ORRES and --DRVFL would be null (see Section 4.1.8.1, Origin Metadata for Variables).

5. The variable --REPNUM variable is populated when there are multiple repeats of the same question. When records are related to the first trial of the question, the variable --REPNUM should be set to "1". When records are related to the second trial of the same question, --REPNUM should be set to "2", and so forth.

6. The actual version number of an instrument is represented in the --CAT value as designated by the QRS Terminology Team. If it is determined that this is not the case for an instrument:
   a. Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing a resolution on how the situation will be handled.
   b. Consider the use of the --GRPID variable to indicate the instrument's version number prior to a decision by the QRS Terminology Team.
   c. The sponsor is expected to provide information about the version used for each QRS instrument in the metadata (using the Comments column in the Define-XML document). This could be provided as value-level metadata for --CAT.
   d. The sponsor is expected to provide information about the scoring rules in the metadata.

7. If the variable --TEST is represented with verbatim text >40 characters, represent the abbreviated meaningful text in --TEST within 40 characters and describe the full text of the item in the study metadata. If the verbatim item response (e.g., --QSORRES) is >200 characters, represent the abbreviated meaningful text in QSORRES within the 200 characters and describe the full text in the study metadata; see Section 4 of the QRS supplement. See Section 4.5.3, Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables, for further information.
   a. The instrument's annotated CRF can also be used as a reference for the full text in both of these situations.

8. --EVAL and --EVALID must not be used to model QRS data in SDTM. These variables have had various interpretations on QRS CRFs and were used to represent a multitude of evaluator information about QRS instruments. This has made it more difficult for users of SDTM QRS data to interpret this data and more difficult to pool data for analyses. If needed, supplemental qualifiers may be used to represent this data. Updated information on a proposed solution to this issue will be posted on the CDISC QRS webpage (https://www.cdisc.org/standards/foundational/qrs).

9. All standard QRS supplement development is coordinated with the CDISC SDS QRS Subteam as the governing body. The process involves drafting the controlled terminology and defining instrument-specific standardized values for qualifier, timing, and result variables to populate the SDTMIG FT, QS, and RS domains. These supplements are developed based on user demand and therapeutic area standards development needs. Sponsors should always consult the CDISC website to review the terminology and supplements prior to modeling any QRS instrument.
   a. Sponsors may participate and/or request the development of additional QRS supplements and terminology through the CDISC SDS QRS subteam and the Controlled Terminology QRS subteam.
      i. Once generated, the QRS supplement is posted on the CDISC website (https://www.cdisc.org/standards/foundational/qrs).
      ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.

10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/RE/spec.md -->
# RE — Respiratory System Findings

> Class: Findings | Structure: One record per finding or result per time point per visit per subject

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
- **CDISC Notes:** Sponsor-defined identifier for a device.

### RESEQ
- **Order:** 5
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### REGRPID
- **Order:** 6
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### REREFID
- **Order:** 7
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external procedure identifier.

### RESPID
- **Order:** 8
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.

### RELNKID
- **Order:** 9
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### RELNKGRP
- **Order:** 10
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### RETESTCD
- **Order:** 11
- **Label:** Short Name of Respiratory Test
- **Type:** Char
- **Controlled Terms:** C111106
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination. It can be used as a column name when converting a dataset from a vertical format to a horizontal format. The value in RETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). RETESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "FEV1", "FVC".

### RETEST
- **Order:** 12
- **Label:** Name of Respiratory Test
- **Type:** Char
- **Controlled Terms:** C111107
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in RETEST cannot be longer than 40 characters. Examples: "Forced Expiratory Volume in 1 Second", "Forced Vital Capacity".

### RECAT
- **Order:** 13
- **Label:** Category for Respiratory Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize observations across subjects.

### RESCAT
- **Order:** 14
- **Label:** Subcategory for Respiratory Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization.

### REPOS
- **Order:** 15
- **Label:** Position of Subject During Observation
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### REORRES
- **Order:** 16
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the procedure measurement or finding as originally received or collected.

### REORRESU
- **Order:** 17
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original units in which the data were collected. The unit for REORRES and REORREF.

### REORREF
- **Order:** 18
- **Label:** Reference Result in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference result for continuous measurements in original units. Should be collected only for continuous results.

### RESTRESC
- **Order:** 19
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from REORRES in a standard format or in standard units. RESTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RESTRESN.

### RESTRESN
- **Order:** 20
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from RESTRESC. RESTRESN should store all numeric test results or findings.

### RESTRESU
- **Order:** 21
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for RESTRESC, RESTRESN and RESTREFN.

### RESTREFC
- **Order:** 22
- **Label:** Character Reference Result
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference value for the result or finding copied or derived from --ORREF in a standard format.

### RESTREFN
- **Order:** 23
- **Label:** Numeric Reference Result in Std Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Reference result for continuous measurements in standard units. Should be populated only for continuous results.

### RESTAT
- **Order:** 24
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a test was not done or a measurement was not taken. Should be null if a result exists in REORRES.

### REREASND
- **Order:** 25
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with RESTAT when value is "NOT DONE".

### RELOC
- **Order:** 26
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement. Examples: "LUNG", "BRONCHUS".

### RELAT
- **Order:** 27
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Side of the body used to collect measurement. Examples: "RIGHT", "LEFT".

### REDIR
- **Order:** 28
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### REMETHOD
- **Order:** 29
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method used to create the result.

### RELOBXFL
- **Order:** 30
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### REBLFL
- **Order:** 31
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be Y or null. Note that REBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### REDRVFL
- **Order:** 32
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. Should be "Y" or null. Records that represent the average of other records, or that do not come from the CRF, or are not as originally collected or received are examples of records that would be derived for the submission datasets. If REDRVFL = "Y", then REORRES could be null, with RESTRESC and (if numeric) RESTRESN having the derived value.

### REEVAL
- **Order:** 33
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".

### REEVALID
- **Order:** 34
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in REEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2".

### REREPNUM
- **Order:** 35
- **Label:** Repetition Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The instance number of a test that is repeated within a given time frame for the same test. The level of granularity can vary (e.g., within a time point, within a visit). Example: multiple measurements of pulmonary function.

### VISITNUM
- **Order:** 36
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 37
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 38
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 39
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 40
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### REDTC
- **Order:** 41
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date/time of procedure or test.

### REDY
- **Order:** 42
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### RETPT
- **Order:** 43
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., "TIME OF LAST DOSE"). See RETPTNUM and RETPTREF. Examples: "START", "5 MINUTES POST".

### RETPTNUM
- **Order:** 44
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of RETPT to aid in sorting.

### REELTM
- **Order:** 45
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (RETPTREF). Not a clock time or a date/time variable, but an interval, represented as ISO duration. Examples: "-PT15M" to represent 15 minutes prior to the reference time point indicated by RETPTREF, "PT8H" to represent 8 hours after the reference time point represented by RETPTREF.

### RETPTREF
- **Order:** 46
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by REELTM, RETPTNUM, and RETPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### RERFTDTC
- **Order:** 47
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by RETPTREF.
---

## Cross References

### Controlled Terminology
- [Respiratory Test Code (C111106)](../../terminology/core/other_part4.md) — RETESTCD
- [Respiratory Test Name (C111107)](../../terminology/core/other_part4.md) — RETEST
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — RELOBXFL, REBLFL, REDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — RESTAT
- [Position (C71148)](../../terminology/core/interventions.md) — REPOS
- [Unit (C71620)](../../terminology/core/general_part5.md) — REORRESU, RESTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — RELOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — REEVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — REMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — REEVALID
- [Laterality (C99073)](../../terminology/core/general_part2.md) — RELAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — REDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RP, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/RE/assumptions.md -->
# RE — Assumptions

1. The Respiratory System Findings domain is used to represent the results/findings of respiratory diagnostic procedures (e.g., spirometry). Information about the conduct of the procedure(s), if collected, should be submitted in the Procedures (PR) domain.

2. Many respiratory assessments require the use of a device. When data about the device used for an assessment or additional information about its use in the assessment are collected, SPDEVID should be included in the record. See the SDTMIG for Medical Devices (SDTMIG-MD, available at https://www.cdisc.org/standards/foundational/medical-devices-sdtmig/) for further information about SPDEVID and the Device domains.

3. Any Identifier, Timing variables, or Findings general observation class qualifiers may be added to the RE domain, but the following qualifiers would generally not be used: --MODIFY, --BODSYS, and --FAST.

<!-- source: knowledge_base/domains/RELREC/spec.md -->
# RELREC — Related Records

> Class: Relationship | Structure: One record per related record, group of records or dataset

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### RDOMAIN
- **Order:** 2
- **Label:** Related Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** C66734
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Abbreviation for the domain of the parent record(s).

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### IDVAR
- **Order:** 4
- **Label:** Identifying Variable
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Name of the identifying variable in the general-observation-class dataset that identifies the related record(s). Examples: --SEQ, --GRPID.

### IDVARVAL
- **Order:** 5
- **Label:** Identifying Variable Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Value of identifying variable described in IDVAR. If --SEQ is the variable being used to describe this record, then the value of --SEQ would be entered here.

### RELTYPE
- **Order:** 6
- **Label:** Relationship Type
- **Type:** Char
- **Controlled Terms:** C78737
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Identifies the hierarchical level of the records in the relationship. Values should be either "ONE" or "MANY". Used only when identifying a relationship between datasets (as described in Section 8.3, Relating Datasets).

### RELID
- **Order:** 7
- **Label:** Relationship Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Unique value within USUBJID that identifies the relationship. All records for the same USUBJID that have the same RELID are considered related/associated. RELID can be any value the sponsor chooses, and is only meaningful within the RELREC dataset to identify the related/associated domain records.
---

## Cross References

### Controlled Terminology
- [SDTM Domain Abbreviation (C66734)](../../terminology/core/general_part4.md) — RDOMAIN
- [Relationship Type (C78737)](../../terminology/core/other_part4.md) — RELTYPE

### Related Domains
- **Same class (Relationship):** RELSPEC, RELSUB, SUPPQUAL

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Relationship class definition](../../model/06_relationship_datasets.md)

<!-- source: knowledge_base/domains/RELREC/assumptions.md -->
# RELREC — Assumptions

The Related Records (RELREC) special-purpose dataset is used to describe relationships between records for a subject (relating peer records) and relationships between datasets (relating datasets). In both cases, relationships represented in RELREC are collected relationships, either by explicit references or checkboxes on the CRF, or by design of the CRF (e.g., vital signs captured during an exercise stress test).

A relationship is defined by adding a record to RELREC for each record to be related and by assigning a unique character identifier value for the relationship. Each record in the RELREC special-purpose dataset contains keys that identify a record (or group of records) and the relationship identifier, which is stored in the RELID variable. The value of RELID is chosen by the sponsor, but must be identical for all related records within USUBJID. It is recommended that the sponsor use a standard system or naming convention for RELID (e.g., all letters, all numbers, capitalized).

## Relating Peer Records

Records expressing a relationship are specified using the key variables STUDYID, RDOMAIN (the domain code of the record in the relationship), and USUBJID, along with IDVAR and IDVARVAL. Single records can be related by using a unique-record-identifier variable such as --SEQ in IDVAR. Groups of records can be related by using grouping variables such as --GRPID in IDVAR. IDVARVAL would contain the value of the variable described in IDVAR. Using --GRPID can be a more efficient method of representing relationships in RELREC, such as when relating an adverse event (or events) to a group of concomitant medications taken to treat the adverse event(s).

The RELREC dataset should be used to represent either:
- explicit relationships, such as concomitant medications taken as a result of an adverse event; or
- information of a nature that necessitates using multiple datasets, as described in Section 8.3, Relating Datasets.

The following are examples of variables that could be used in IDVAR:
- The sequence number (--SEQ) variable uniquely identifies a record for a given USUBJID within a domain. The variable --SEQ is required in all domains except DM.
- The reference identifier (--REFID) variable can be used to capture a sponsor-defined or external identifier. Some examples are lab-specimen identifiers and ECG identifiers. --REFID is permissible in all general observation-class domains, but is never required. Values for --REFID are sponsor-defined.
- The grouping identifier (--GRPID) variable, used to link related records for a subject within a domain, is explained in Section 8.1, Relating Groups of Records Within a --GRPID Variable.

## Relating Datasets

The Related Records (RELREC) special-purpose dataset can also be used to identify relationships between datasets (e.g., a one-to-many or parent-child relationship). The relationship is defined by including a single record for each related dataset that identifies the key(s) of the dataset that can be used to relate the respective records.

Relationships between datasets should only be recorded in the RELREC dataset when the sponsor has found it necessary to split information between datasets that are related, and that may need to be examined together for analysis or proper interpretation. Note that it is not necessary to use the RELREC dataset to identify associations from data in the SUPP-- datasets or the Comments (CO) dataset to their parent general-observation class dataset records or special-purpose domain records, as both these datasets include the key variable identifiers of the parent record(s) that are necessary to make the association.

The variable RELTYPE identifies the type of relationship between the datasets. The allowable values are ONE and MANY (controlled terminology is expected). This information defines how a merge/join would be written, and what would be the result of the merge/join. The possible combinations are:

1. **ONE and ONE.** This combination indicates that there is **NO** hierarchical relationship between the datasets and the records in the datasets. Only 1 record from each dataset will potentially have the same value of the IDVAR within USUBJID.

2. **ONE and MANY.** This combination indicates that there **IS** a hierarchical (parent-child) relationship between the datasets. One record within USUBJID in the dataset identified by RELTYPE = "ONE" will potentially have the same value of the IDVAR with many (1 or more) records in the dataset identified by RELTYPE = "MANY".

3. **MANY and MANY.** This combination is unusual and challenging to manage in a merge/join, and may represent a relationship that was never intended to convey a usable merge/join, such as described in Section 6.3.5.9.3, Relating PP Records to PC Records.

<!-- source: knowledge_base/domains/RELSPEC/spec.md -->
# RELSPEC — Related Specimens

> Class: Relationship | Structure: One record per specimen identifier per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### USUBJID
- **Order:** 2
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### REFID
- **Order:** 3
- **Label:** Specimen ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Specimen identifier, unique within USUBJID.

### SPEC
- **Order:** 4
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734; C111114
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the type of specimen used for a measurement. Examples: "SERUM", "PLASMA", "URINE", "SOFT TISSUE".

### PARENT
- **Order:** 5
- **Label:** Specimen Parent
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifies the REFID of the parent of a specimen to support tracking its genealogy.

### LEVEL
- **Order:** 6
- **Label:** Specimen Level
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Req
- **CDISC Notes:** Identifies the generation number of the sample where the collected sample is considered the first generation.
---

## Cross References

### Controlled Terminology
- [Genetic Sample Type (C111114)](../../terminology/core/general_part2.md) — SPEC
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — SPEC

### Related Domains
- **Same class (Relationship):** RELREC, RELSUB, SUPPQUAL

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Relationship class definition](../../model/06_relationship_datasets.md)

<!-- source: knowledge_base/domains/RELSPEC/assumptions.md -->
# RELSPEC — Assumptions

BE, BS, and RELSPEC domain specifications, assumptions, and examples were copied and minimally updated from the provisional SDTMIG-PGx, published 2015-05-26. This was done in preparation for the retirement of the SDTMIG-PGx upon publication of SDTMIG v3.4. These domains are currently under extensive revision for inclusion in a future SDTMIG.

A dataset used to represent relationships between specimens.

1. The RELSPEC dataset is not used to manage relationships between any other datasets or domains.

2. The RELSPEC dataset is only used to maintain relationships between specimens, therefore it does not require any additional variables such as those used in RELREC.

3. There are three CDISC controlled terminology codelists that may be applicable to SPEC: SPEC (C77529), SPECTYPE (C78734), and GENSMP (C111114). Sponsors are responsible for determining the most appropriate codelist(s) for their submission.

<!-- source: knowledge_base/domains/RELSUB/spec.md -->
# RELSUB — Related Subjects

> Class: Relationship | Structure: One record per relationship per related subject per subject

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### USUBJID
- **Order:** 2
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. Either USUBJID or POOLID must be populated.

### POOLID
- **Order:** 3
- **Label:** Pool Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to identify a pool of subjects. If POOLID is entered, POOLDEF records must exist for each subject in the pool and USUBJID must be null. Either USUBJID or POOLID must be populated.

### RSUBJID
- **Order:** 4
- **Label:** Related Subject or Pool Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to identify a related subject or pool of subjects. RSUBJID will be populated with either the USUBJID of the related subject or the POOLID of the related pool.

### SREL
- **Order:** 5
- **Label:** Subject Relationship
- **Type:** Char
- **Controlled Terms:** C100130
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Describes the relationship of the subject identified in USUBJID or the pool identified in POOLID to the subject or pool identified in RSUBJID.
---

## Cross References

### Controlled Terminology
- [Relationship to Subject (C100130)](../../terminology/core/other_part4.md) — SREL

### Related Domains
- **Same class (Relationship):** RELREC, RELSPEC, SUPPQUAL

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Relationship class definition](../../model/06_relationship_datasets.md)

<!-- source: knowledge_base/domains/RELSUB/assumptions.md -->
# RELSUB — Assumptions

A dataset used to represent relationships between study subjects.

Some studies include subjects who are related to each other, and in some cases it is important to record those relationships. A study in which pregnant women are treated and both the mother and her child(ren) are study subjects is the most common case in which relationships between subjects are collected. There are also studies of genetically based diseases where subjects who are related to each other are enrolled, and the relationships between subjects are recorded.

1. RELSUB is used to represent relationships between persons, both of whom are study subjects. A relationship between a study subject and a person who is not a study subject may not be represented in RELSUB; this may only be reported in APRELSUB. The existence of the RELSUB dataset should not affect whether relationships are collected; that should remain a decision based on the needs of the particular study.

2. The variable POOLID was developed for nonclinical studies, where assessments may be made for groups of animals, and identifiers are needed for those groups (pools). It is included here because POOLID can be used for human clinical trials, if necessary. If POOLID is submitted, the POOLDEF dataset must be submitted.

3. If POOLID is submitted, then in any record, 1 and only 1 of USUBJID and POOLID must be populated.

4. If a study does not include the use of POOLID, then USUBJID must be populated in every record.

5. RSUBJID must be a USUBJID value present in the Demographics (DM) domain. RSUBJID must be populated in every record.

6. Values of SREL should be taken from the CDISC Controlled Terminology codelist RELSUB wherever possible. However, if an appropriate term does not exist in the codelist, another term may be used. The SREL term should not be less specific than the verbatim term collected. For instance, it would be inappropriate to record a relationship using the term "RELATIVE, FIRST DEGREE" when the collected relationship was "brother".

7. Every relationship between 2 study subjects is represented in RELSUB as 2 directional relationships: (1) with the first subject's identifier in USUBJID and the second subject's identifier in RSUBJID, and (2) with the second subject's identifier in USUBJID and the first subject's identifier in RSUBJID. The SREL values in the 2 records will describe the same relationship, but from the viewpoint of each subject (e.g., "MOTHER, BIOLOGICAL"; "CHILD, BIOLOGICAL").

8. All collected relationships between subjects should be recorded in RELSUB. In some cases, 2 subjects may have more than 1 relationship. For instance, a woman might be both maternal aunt and wet nurse to an infant. When there are multiple relationships between 2 subjects, each relationship will be represented by 2 records in RELSUB.

<!-- source: knowledge_base/domains/RP/spec.md -->
# RP — Reproductive System Findings

> Class: Findings | Structure: One record per finding or result per time point per visit per subject

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

### RPSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject (or within a parameter, in the case of the Trial Summary domain). May be any valid number (including decimals) and does not have to start at 1.

### RPGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain. Also used to link together a block of related records in the Trial Summary dataset.

### RPREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or a medical image).

### RPSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. Example: Preprinted line identifier on a CRF.

### RPLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### RPLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### RPTESTCD
- **Order:** 10
- **Label:** Short Name of Reproductive Test
- **Type:** Char
- **Controlled Terms:** C106479
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for RPTEST used as a column name when converting a dataset from a vertical format to a horizontal format. The short value can be up to 8 characters. Examples: "CHILDPOT", "BCMETHOD", "MENARAGE".

### RPTEST
- **Order:** 11
- **Label:** Name of Reproductive Test
- **Type:** Char
- **Controlled Terms:** C106478
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name For RPTESTCD. Examples: "Childbearing Potential", "Birth Control Method", "Menarche Age".

### RPCAT
- **Order:** 12
- **Label:** Category for Reproductive Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values. Example: "No use case to date, but values would be relative to reproduction tests grouping".

### RPSCAT
- **Order:** 13
- **Label:** Subcategory for Reproductive Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of RPCAT values. Example: "No use case to date, but values would be relative to reproduction tests grouping".

### RPORRES
- **Order:** 14
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected. Examples: "120", "<1", "POS".

### RPORRESU
- **Order:** 15
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for RPORRES. Examples: "in", "LB", "kg/L".

### RPSTRESC
- **Order:** 16
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from RPORRES, in a standard format or in standard units. RPSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in RPSTRESN. For example, if various tests have results "NONE", "NEG", and "NEGATIVE" in RPORRES, and these results effectively have the same meaning, they could be represented in standard format in RPSTRESC as "NEGATIVE".

### RPSTRESN
- **Order:** 17
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from RPSTRESC. RPSTRESN should store all numeric test results or findings.

### RPSTRESU
- **Order:** 18
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for RPSTRESC and RPSTRESN. Example: "mol/L".

### RPSTAT
- **Order:** 19
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### RPREASND
- **Order:** 20
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with RPSTAT when value is "NOT DONE".

### RPLOBXFL
- **Order:** 21
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### RPBLFL
- **Order:** 22
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that RPBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### RPDRVFL
- **Order:** 23
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records which represent the average of other records or which do not come from the CRF are examples of records that would be derived for the submission datasets. If RPDRVFL = "Y", then RPORRES may be null, with RPSTRESC and (if numeric) RPSTRESN having the derived value.

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
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

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
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### RPDTC
- **Order:** 29
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation.

### RPDY
- **Order:** 30
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### RPDUR
- **Order:** 31
- **Label:** Duration
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collected duration of an event, intervention, or finding represented in ISO 8601 character format. Used only if collected on the CRF and not derived.

### RPTPT
- **Order:** 32
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose.

### RPTPTNUM
- **Order:** 33
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### RPELTM
- **Order:** 34
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time in ISO 8601 character format relative to a planned fixed reference (RPTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### RPTPTREF
- **Order:** 35
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by RPELTM, RPTPTNUM, and RPTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### RPRFTDTC
- **Order:** 36
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by RPTPTREF in ISO 8601 character format.
---

## Cross References

### Controlled Terminology
- [Reproductive System Findings Test Name (C106478)](../../terminology/core/other_part4.md) — RPTEST
- [Reproductive System Findings Test Code (C106479)](../../terminology/core/other_part4.md) — RPTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — RPLOBXFL, RPBLFL, RPDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — RPSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — RPORRESU, RPSTRESU
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RS, SC, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/RP/assumptions.md -->
# RP — Assumptions

1. Reproductive System Findings domain contains information regarding a subject's reproductive ability and reproductive history (e.g., number of previous pregnancies, number of births, pregnant during the study).

2. Information on medications related to reproduction (e.g., contraceptives, fertility treatments) should be included in the Concomitant/Prior Medications (CM) domain; see Section 6.1.2.

3. There are separate codelists for RP tests, responses, and units.
   a. Associations between RP tests and response codelists are described in the RP Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

4. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the RP domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --LOINC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/RS/spec.md -->
# RS — Disease Response and Clin Classification

> Class: Findings | Structure: One record per response assessment or clinical classification assessment per time point per visit per subject per assessor per medical evaluator

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

### RSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number.

### RSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain.

### RSREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier.

### RSSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### RSLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** An identifier used to link the response assessment to the related measurement record in another domain which was used to determine the response result. LNKID values group records within USUBJID.

### RSLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** A grouping identifier used to link the response assessment to a group of measurement/assessment records which were used in the assessment of the response. LNKGRP values group records within USUBJID.

### RSTESTCD
- **Order:** 10
- **Label:** Assessment Short Name
- **Type:** Char
- **Controlled Terms:** C96782
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the TEST in RSTEST. The value in RSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). RSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TRGRESP", "NTRGRESP", "OVRLRESP", "SYMPTDTR", "CPS0102".  There are separate codelists used for RSTESTCD where the choice depends on the value of RSCAT. Codelist "ONCRTSCD" is used for oncology response criteria (when RSCAT is a term in codelist "ONCRSCAT"). Examples: TRGRESP, "NTRGRESP, "OVRLRESP". For Clinical Classifications (when RSCAT is a term in codelist "CCCAT"), QRS Naming Rules apply. These instruments have individual dedicated terminology codelists.

### RSTEST
- **Order:** 11
- **Label:** Assessment Name
- **Type:** Char
- **Controlled Terms:** C96781
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the response assessment. The value in RSTEST cannot be longer than 40 characters.  There are separate codelists used for RSTEST where the choice depends on the value of RSCAT. Codelist "ONCRTS" is used for oncology response criteria (when RSCAT is a term in codelist "ONCRSCAT"). Examples: "Target Response", "Non-target Response", "Overall Response", "Symptomatic Deterioration". For Clinical Classifications (when RSCAT is a term in codelist "CCCAT"), QRS Naming Rules apply. These instruments have individual dedicated terminology codelists.

### RSCAT
- **Order:** 12
- **Label:** Category for Assessment
- **Type:** Char
- **Controlled Terms:** C124298; C118971
- **Role:** Grouping Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to define a category of related records across subjects. Examples: "RECIST 1.1", "CHILD-PUGH CLASSIFICATION". There are separate codelists used for RSCAT where the choice depends on whether the related records are about an oncology response criterion or another clinical classification.  RSCAT is required for clinical classifications other than oncology response criteria.

### RSSCAT
- **Order:** 13
- **Label:** Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of RSCAT values.

### RSORRES
- **Order:** 14
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the response assessment as originally received, collected, or calculated.

### RSORRESU
- **Order:** 15
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for RSORRES.

### RSSTRESC
- **Order:** 16
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C96785
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for the response assessment, copied, or derived from RSORRES in a standard format or standard units. RSSTRESC should store all results or findings in character format.  For Clinical Classifications, this may be a score.

### RSSTRESN
- **Order:** 17
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from --STRESC. --STRESN should store all numeric test results or findings. For Clinical Classifications, this may be a score.

### RSSTRESU
- **Order:** 18
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for RSSTRESC and RSSTRESN.

### RSSTAT
- **Order:** 19
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate the response assessment was not performed. Should be null if a result exists in RSORRES.

### RSREASND
- **Order:** 20
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a response assessment was not performed. Examples: "All target tumors not evaluated", "Subject does not have non-target tumors". Used in conjunction with RSSTAT when value is "NOT DONE".

### RSNAM
- **Order:** 21
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the vendor that performed the response assessment. This column can be left null when the investigator provides the complete set of data in the domain.

### RSMETHOD
- **Order:** 22
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C158113
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination.

### RSLOBXFL
- **Order:** 23
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.  When a clinical classification is assessed at multiple times, including baseline, RSLOBXFL should be included in the dataset.

### RSBLFL
- **Order:** 24
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that --BLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### RSDRVFL
- **Order:** 25
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### RSEVAL
- **Order:** 26
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".  RSEVAL is expected for oncology response criteria. It can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from one or more independent assessors is included, meaning that the rows attributed to the investigator should contain a value of "INVESTIGATOR".

### RSEVALID
- **Order:** 27
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in RSEVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumptions in Section 6.3.9.3.1, Disease Response Use Case.

### RSACPTFL
- **Order:** 28
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provides an evaluation of response, this flag identifies the record that is considered to be the accepted evaluation.

### VISITNUM
- **Order:** 29
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 30
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 31
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 32
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 33
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### RSDTC
- **Order:** 34
- **Label:** Date/Time of Assessment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of the assessment represented in ISO 8601 character format.

### RSDY
- **Order:** 35
- **Label:** Study Day of Assessment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### RSTPT
- **Order:** 36
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See RSTPTNUM and RSTPTREF.

### RSTPTNUM
- **Order:** 37
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### RSELTM
- **Order:** 38
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time in ISO 8601 character format relative to a planned fixed reference (RSTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### RSTPTREF
- **Order:** 39
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by RSELTM, RSTPTNUM, and RSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### RSRFTDTC
- **Order:** 40
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by RSTPTREF in ISO 8601 character format.

### RSEVLINT
- **Order:** 41
- **Label:** Evaluation Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Duration of interval associated with an observation such as a finding RSTESTCD, represented in ISO 8601 character format. Example: "-P2M" to represent a period of the past 2 months as the evaluation interval.

### RSEVINTX
- **Order:** 42
- **Label:** Evaluation Interval Text
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Evaluation interval associated with an observation, where the interval is not able to be represented in ISO 8601 format. Examples: "LIFETIME", "LAST NIGHT", "RECENTLY", "OVER THE LAST FEW WEEKS".

### RSSTRTPT
- **Order:** 43
- **Label:** Start Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the start of the observation as being before or after the sponsor-defined reference time point defined by variable RSSTTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### RSSTTPT
- **Order:** 44
- **Label:** Start Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by RSSTRTPT. Examples: "2003-12-15", "VISIT 1".

### RSENRTPT
- **Order:** 45
- **Label:** End Relative to Reference Time Point
- **Type:** Char
- **Controlled Terms:** C66728
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Identifies the end of the observation as being before or after the sponsor-defined reference time point defined by variable RSENTPT.  Not all values of the codelist are allowable for this variable. See Section 4.4.7, Use of Relative Timing Variables.

### RSENTPT
- **Order:** 46
- **Label:** End Reference Time Point
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description or date/time in ISO 8601 character format of the sponsor-defined reference point referred to by RSENRTPT. Examples: "2003-12-25", "VISIT 2".
---

## Cross References

### Controlled Terminology
- [Category of Clinical Classification (C118971)](../../terminology/core/oncology_part1.md) — RSCAT
- [Category of Oncology Response Assessment (C124298)](../../terminology/core/oncology_part1.md) — RSCAT
- [QRS Method (C158113)](../../terminology/core/general_part4.md) — RSMETHOD
- [Relation to Reference Period (C66728)](../../terminology/core/general_part4.md) — RSSTRTPT, RSENRTPT
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — RSLOBXFL, RSBLFL, RSDRVFL, RSACPTFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — RSSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — RSORRESU, RSSTRESU
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — RSEVAL
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — RSEVALID
- [Oncology Response Assessment Test Name (C96781)](../../terminology/core/oncology_part2.md) — RSTEST
- [Oncology Response Assessment Test Code (C96782)](../../terminology/core/oncology_part1.md) — RSTESTCD
- [Oncology Response Assessment Result (C96785)](../../terminology/core/oncology_part1.md) — RSSTRESC
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, SC, SS, TR, TU, UR, VS
- **Related Findings:** [TR](../TR/) — disease response ← tumor results
- **Related Findings:** [TU](../TU/) — disease response ← tumor identification

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/RS/assumptions.md -->
# RS — Assumptions

## RS — Disease Response Use Case Assumptions

The following assumptions are unique to the RS domain disease response use case:

1. RSCAT is used to group a set of assessments based on a disease response criterion (published or protocol-defined). One of the codelists for RSCAT is ONCRSCAT. The ONCRSCAT codelist contains controlled terminology for oncology disease response assessments.

2. Oncology response criteria assess the change in tumor burden, an important feature of the clinical evaluation of cancer therapeutics: Both tumor shrinkage (objective response) and disease progression are useful endpoints in cancer clinical trials. The RS domain is applicable for representing responses to assessment criteria such as RECIST[1] or Lugano classification.[2] The SDTM domain examples provided reference RECIST. Disease Response supplements will be developed as 1 supplement per response criterion and will contain criterion-specific guidance and examples.
   a. CDISC submission values and definitions in the ONCRSRR codelist have been developed to facilitate reuse by keeping the definitions focused on the meaning of the result rather than on relating them to a specific published criterion or a particular tumor type. CDISC submission values and definitions are intended to apply across multiple tumor types, imaging modalities, therapeutic agents, and published criterion. This means that there may be cases where the appropriate ONCRSRR CDISC submission value may not exactly match the term used in the published criterion. It is expected that clinicians should use the precise criterion definitions outlined in the individual papers to assign the appropriate response according to the CDISC submission values.
   b. The terms "response" and "remission" are commonly used to describe functionally synonymous terms. "Response" is used in CDISC submission values based on the following agreement: FDA, CDISC, NCI-EVS, and select academic experts came to consensus that because the words "response" (used in solid tumors as an indicator of a favorable change in tumor burden) and "remission" (used in non-solid tumors) were functionally synonymous, 2 distinct terms were not required to be added to the ONCRSRR codelist. Instead, "remission" has been added as a synonym in all instances where "response" is used in a CDISC submission value, for response values used in both solid and non-solid tumors. The FDA expects a single CDISC submission value to be submitted for both solid and non-solid tumors.
   c. Refer to the Controlled Terminology Rules for Oncology for more information (available at https://www.cdisc.org/standards/terminology/controlled-terminology).
   d. RSTESTCD/RSTEST values for this domain are published as Controlled Terminology. For some RSTESTCD/RSTEST values, CDISC CT includes codelists for use with RSORRES. The associations between the test values and results are in the Oncology codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

3. The RS domain disease response criteria use case may include records derived by the investigator or with a data collection tool, but not sponsor-derived records. Sponsor-derived records and results should be provided in an analysis dataset (ADaM).
   a. For disease response criteria, the BEST Response assessment records are included in the RS domain only when provided by the investigator or an independent assessor (i.e., Best responses that are derived by the sponsor for the analysis are not included in the RS domain).

4. The RSLNKGRP variable is used to provide a link between the records in a findings domain (e.g., Tumor/Lesion Results, TR; Laboratory Test Results, LB) that contribute to a record in the RS domain. Records should exist in the RELREC dataset to support this relationship. A RELREC relationship could also be defined using RSLNKID when a response evaluation or clinical classification measure relates back to another source dataset (e.g., tumor assessment in TR). The domain in which data that contribute to an assessment of response reside should not affect whether a link to the RS record through a RELREC relationship is created. For example, a set of oncology response criteria might require lab results in the LB domain, not only tumor results in the TR domain.

5. When using the RS domain to represent response evaluation or clinical classification instruments that incorporate data from other domains:
   a. Whenever possible, all source data must be represented in the topic-based domain(s) to which they pertain. For example, if a lab test value is collected and then scored for a response evaluation, the lab test value must be recorded in the LB domain using the rules that apply to that domain and the tests being represented.
   b. In the oncology setting, the response to therapy would often be determined, at least in part, from data in the TR domain. Data from other sources (in other SDTM domains) might also be used in an assessment of response (e.g., lab test results, assessments of symptoms).
   c. Oncology response assessments sometimes include symptomatic deterioration. Symptomatic deterioration may be considered as non-radiologic evidence of progressive disease. Symptomatic deterioration is recorded in RS with RSTEST = "Symptomatic Deterioration" and the standardized response (e.g., "PD") in RSSTRESC.
   d. In all cases, RSSTRESC should be populated as indicated in controlled terminology.

6. Best response, duration of response, or the progression to prior therapies and follow-up therapies may be represented in the RS domain.
   a. The record in RS may be related and linked to record(s) in Concomitant/Prior Medications (CM) using CMLNKGRP and RSLNKGRP. Likewise, the link to Procedures (PR; e.g., radiotherapy, surgery) would be made using PRLNKGRP.
   b. If the criteria used to determine the response is unknown or not collected, this is represented as RSCAT = "UNSPECIFIED".

7. The evaluator identifier variable (RSEVALID) can be used in conjunction with RSEVAL to provide additional detail of who is providing the assessment. For example, RSEVAL = "INDEPENDENT ASSESSOR" and RSEVALID = "RADIOLOGIST 1" may further qualify the RSEVALID variable. RSEVALID may be subject to controlled terminology but may also represent free text values depending on the use case. When used with disease response data, RSEVALID is subject to MEDEVAL controlled terminology.

8. In cases where an independent assessor identifies one of multiple assessments/measurements to be the accepted one, the accepted record flag variable (RSACPTFL) identifies records that have been determined to be the accepted assessments/measurements by an independent assessor. This flag would be provided by an independent assessor when multiple assessors (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provide assessments or evaluations at the same time point or for an overall evaluation.
   a. RSACPTFL should not be derived by the sponsor. If a derivation is needed to make the record selection, then this derivation should be done in the analysis dataset (ADaM).

9. Disease recurrence can be represented in the RS domain using RSTEST = "Disease Recurrence Indicator" to indicate that there was an assessment of whether there was disease recurrence. The RSCAT = "PROTOCOL DEFINED RESPONSE CRITERIA" can be used to indicate that the response assessment of disease recurrence was based on protocol-specified criteria rather than published response criteria.

10. When a disease response result is based on multiple procedures/scans/images/physical exams performed on different dates, RSDTC may be derived.

11. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the RS domain, but the following qualifiers would not generally be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

## RS — Clinical Classifications Use Case Assumptions

The following assumptions are unique to the RS domain clinical classifications use case:

1. Clinical classifications are named instruments whose output is an ordinal or categorical score that serves as a surrogate for or ranking of disease status or other physiological or biological status.
   a. Clinical classifications may be based solely on objective data from clinical records, or they may involve a clinical judgment or interpretation of directly observable signs, behaviors, or other physical manifestations related to a condition or subject status. These physical manifestations may be findings (e.g., lab results, vital signs, clinical events) that are typically represented in other SDTM domains.

2. RSCAT is used to group a set of assessments based on a clinical classification. One of the codelists for RSCAT is CCCAT. The CCCAT codelist contains CDISC Controlled Terminology for clinical classifications instruments.

3. When using the RS domain to represent a clinical classification instrument that incorporates data from other domains:
   a. Whenever possible, all source data must be represented in the topic-based domain(s) to which they pertain. For example, if a lab test value is collected and then scored for a response evaluation or clinical classification instrument, the lab test value must be recorded in the LB domain using the rules that apply to that domain and the tests being represented.
   b. If the source value is directly collected on the clinical classification instrument, then the values from the source record may be transcribed to the corresponding RS record, with RSORRES and RSORRESU populated to agree with the units shown on the clinical classification instrument, which may be different from the sponsor's usual practice for original and standard units.
   c. If a clinical classification uses a source value by comparing it to a range (e.g., "2-5", ">3"), then the source value will exist only in the source domain; the range is represented in the corresponding RS record in RSORRES and RSORRESU.
   d. In all cases, RSSTRESC/RSSTRESN should be populated with the assigned ordinal score as indicated on the instrument.

## QRS Shared Assumptions

The QRS Shared Assumptions (see FT assumptions) also apply to the Clinical Classifications use case of the RS domain, but not the Disease Response use case.

<!-- source: knowledge_base/domains/SC/spec.md -->
# SC — Subject Characteristics

> Class: Findings | Structure: One record per characteristic per visit per subject.

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

### SCSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### SCGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### SCSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.

### SCTESTCD
- **Order:** 7
- **Label:** Subject Characteristic Short Name
- **Type:** Char
- **Controlled Terms:** C74559
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in SCTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SCTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SCTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "MARISTAT", "NATORIG".

### SCTEST
- **Order:** 8
- **Label:** Subject Characteristic
- **Type:** Char
- **Controlled Terms:** C103330
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in SCTEST cannot be longer than 40 characters. Examples: "Marital Status", "National Origin".

### SCCAT
- **Order:** 9
- **Label:** Category for Subject Characteristic
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records.

### SCSCAT
- **Order:** 10
- **Label:** Subcategory for Subject Characteristic
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the subject characteristic.

### SCORRES
- **Order:** 11
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the subject characteristic as originally received or collected.

### SCORRESU
- **Order:** 12
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Original unit in which the data were collected. The unit for SCORRES.

### SCSTRESC
- **Order:** 13
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from SCORRES, in a standard format or standard units. SCSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SCSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in SCORRES, and these results effectively have the same meaning, they could be represented in standard format in SCSTRESC as "NEGATIVE".

### SCSTRESN
- **Order:** 14
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from SCSTRESC. SCSTRESN should store all numeric test results or findings.

### SCSTRESU
- **Order:** 15
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized unit used for SCSTRESC or SCSTRESN.

### SCSTAT
- **Order:** 16
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that the measurement was not done. Should be null if a result exists in SCORRES.

### SCREASND
- **Order:** 17
- **Label:** Reason Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why the observation has no result. Example: "Subject refused". Used in conjunction with SCSTAT when value is "NOT DONE".

### VISITNUM
- **Order:** 18
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 19
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 20
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 21
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 22
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time at which the assessment was made.

### SCDTC
- **Order:** 23
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Collection date and time of the subject characteristic represented in ISO 8601 character format.

### SCDY
- **Order:** 24
- **Label:** Study Day of Examination
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of collection, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
---

## Cross References

### Controlled Terminology
- [Subject Characteristic Test Name (C103330)](../../terminology/core/other_part5.md) — SCTEST
- [Not Done (C66789)](../../terminology/core/general_part4.md) — SCSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — SCORRESU, SCSTRESU
- [Subject Characteristic Test Code (C74559)](../../terminology/core/other_part5.md) — SCTESTCD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SS, TR, TU, UR, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/SC/assumptions.md -->
# SC — Assumptions

1. The structure of subject characteristics is based on the Findings general observation class and is an extension of the demographics data, including socioeconomic or other broad characteristics. The structure for demographic data is fixed and includes date of birth, age, sex, race, ethnicity, and country. Subject characteristics may be collected periodically over time. Some examples of subject characteristics include education level, marital status, and national origin.

2. Associations between some subject characteristic tests and response codelists are described in the SC Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

3. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the SC domain, but the following qualifiers would generally not be used in SC: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --NAM, --LOINC, --SPEC, --SPCCND, --BLFL, --LOBXFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/SE/spec.md -->
# SE — Subject Elements

> Class: Special-Purpose | Structure: One record per actual Element per subject

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

### SESEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. Should be assigned to be consistent chronological order.

### ETCD
- **Order:** 5
- **Label:** Element Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** 1. ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.  2. If an encountered element differs from the planned element to the point that it is considered a new element, then use "UNPLAN" as the value for ETCD to represent this element.

### ELEMENT
- **Order:** 6
- **Label:** Description of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** The name of the element. If ETCD has a value of "UNPLAN", then ELEMENT should be null.

### TAETORD
- **Order:** 7
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the subject's assigned trial arm.

### EPOCH
- **Order:** 8
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned.

### SESTDTC
- **Order:** 9
- **Label:** Start Date/Time of Element
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** Start date/time for an element for each subject.

### SEENDTC
- **Order:** 10
- **Label:** End Date/Time of Element
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time for an element for each subject.

### SESTDY
- **Order:** 11
- **Label:** Study Day of Start of Element
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of start of element relative to the sponsor-defined RFSTDTC.

### SEENDY
- **Order:** 12
- **Label:** Study Day of End of Element
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of end of element relative to the sponsor-defined RFSTDTC.

### SEUPDES
- **Order:** 13
- **Label:** Description of Unplanned Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of what happened to the subject during an unplanned element. Used only if ETCD has the value of "UNPLAN".
---

## Cross References

### Controlled Terminology
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Special-Purpose):** CO, DM, SM, SV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)

<!-- source: knowledge_base/domains/SE/assumptions.md -->
# SE — Assumptions

Submission of the SE dataset is strongly recommended, as it provides information needed by reviewers to place observations in context within the study. As noted in the SE - Description/Overview, the TE and TA datasets should also be submitted, as these define the design and the terms referenced by the SE dataset.

The SE domain allows the submission of data on the timing of the trial elements a subject actually passed through in their participation in the trial. Section 7.2.2, Trial Elements, and Section 7.2.1, Trial Arms, provide additional information on these datasets, which define a trial's planned elements and describe the planned sequences of elements for the arms of the trial.

1. For any particular subject, the dates in the SE table are the dates when the transition events identified in the TE table occurred. Judgment may be needed to match actual events in a subject's experience with the definitions of transition events (i.e., events that mark the start of new elements) in the TE table; actual events may vary from the plan. For instance, in a single-dose pharmacokinetics (PK) study, the transition events might correspond to study drug doses of 5 and 10 mg. If a subject actually received a dose of 7 mg when they were scheduled to receive 5 mg, a decision will have to be made on how to represent this in the SE domain.

2. If the date/time of a transition element was not collected directly, the method used to infer the element start date/time should be explained in the Comments column of the Define-XML document.

3. Judgment will also have to be used in deciding how to represent a subject's experience if an element does not proceed or end as planned. For instance, the plan might identify a trial element that is to start with the first of a series of 5 daily doses and end after 1 week, when the subject transitions to the next treatment element. If the subject actually started the next treatment epoch (see Section 7.1, Introduction to Trial Design Model Datasets, and Section 7.1.2, Definitions of Trial Design Concepts) after 4 weeks, the sponsor would have to decide whether to represent this as an abnormally long element, or as a normal element plus an unplanned non-treatment element.

4. If the sponsor decides that the subject's experience for a particular period of time cannot be represented with one of the planned elements, then that period of time should be represented as an unplanned element. The value of ETCD for an unplanned element is "UNPLAN" and SEUPDES should be populated with a description of the unplanned element.

5. The values of SESTDTC provide the chronological order of the actual subject elements. SESEQ should be assigned to be consistent with the chronological order. Note that the requirement that SESEQ be consistent with chronological order is more stringent than in most other domains, where --SEQ values need only be unique within subject.

6. When TAETORD is included in the SE domain, it represents the planned order of an element in an arm. This should not be confused with the actual order of the elements, which will be represented by their chronological order and SESEQ. TAETORD will not be populated for subject elements that are not planned for the arm to which the subject was assigned. Thus, TAETORD will not be populated for any element with an ETCD value of "UNPLAN". TAETORD also will not be populated if a subject passed through an element that, although defined in the TE dataset, was out of place for the arm to which the subject was assigned. For example, if a subject in a parallel study of drug A vs. drug B was assigned to receive drug A but received drug B instead, then TAETORD would be left blank for the SE record for their drug B element. If a subject was assigned to receive the sequence of elements A, B, C, D, and instead received A, D, B, C, then the sponsor would have to decide for which of these SE records TAETORD should be populated. The rationale for this decision should be documented in the Comments column of the Define-XML document.

7. For subjects who follow the planned sequence of elements for the arm to which they were assigned, the values of EPOCH in the SE domain will match those associated with the elements for the subject's arm in the TA dataset. The sponsor will have to decide what value, if any, of EPOCH to assign SE records for unplanned elements and in other cases where the subject's actual elements deviate from the plan. The sponsor's methods for such decisions should be documented in the Define-XML document, in the row for EPOCH in the SE dataset table.

8. Because there are, by definition, no gaps between elements, the value of SEENDTC for one element will always be the same as the value of SESTDTC for the next element.

9. Note that SESTDTC is required, although --STDTC is not required in any other subject-level dataset. The purpose of the dataset is to record the elements a subject actually passed through. If it is known that a subject passed through a particular element, then there must be some information (perhaps imprecise) on when it started. Thus, SESTDTC may not be null, although some records may not have all the components (e.g., year, month, day, hour, minute) of the date/time value collected.

10. The following identifier variables are permissible and may be added as appropriate: --GRPID, --REFID, --SPID.

11. Care should be taken in adding additional timing variables:
    a. The purpose of --DTC and --DY is to record the date and study day on which data was collected. Elements are generally "derived" in the sense that they are a secondary use of data collected elsewhere; it is not generally useful to know when those date/times were recorded.
    b. --DUR could be added only if the duration of an element was collected, not derived.
    c. It would be inappropriate to add the variables that support time points (--TPT, --TPTNUM, --ELTM, --TPTREF, and --RFTDTC), because the topic of this dataset is elements.

<!-- source: knowledge_base/domains/SM/spec.md -->
# SM — Subject Disease Milestones

> Class: Special-Purpose | Structure: One record per Disease Milestone per subject

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

### SMSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of subject records. Should be assigned to be consistent chronological order.

### MIDS
- **Order:** 5
- **Label:** Disease Milestone Instance Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Name of the specific disease milestone. For types of disease milestones that can occur multiple times, the name will end with a sequence number. Example: "HYPO1".

### MIDSTYPE
- **Order:** 6
- **Label:** Disease Milestone Type
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** The type of disease milestone. Example: "HYPOGLYCEMIC EVENT".

### SMSTDTC
- **Order:** 7
- **Label:** Start Date/Time of Milestone
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of milestone instance (if milestone is an intervention or event) or date of milestone (if Milestone is a finding).

### SMENDTC
- **Order:** 8
- **Label:** End Date/Time of Milestone
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time of disease milestone instance.

### SMSTDY
- **Order:** 9
- **Label:** Study Day of Start of Milestone
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Study day of start of disease milestone instance, relative to the sponsor-defined RFSTDTC.

### SMENDY
- **Order:** 10
- **Label:** Study Day of End of Milestone
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Study day of end of disease milestone instance, relative to the sponsor-defined RFSTDTC.
---

## Cross References

### Related Domains
- **Same class (Special-Purpose):** CO, DM, SE, SV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)

<!-- source: knowledge_base/domains/SM/assumptions.md -->
# SM — Assumptions

1. Disease milestones are observations or activities whose timings are of interest in the study. The types of disease milestones are defined at the study level in the TM dataset. The purpose of the SM dataset is to provide a summary timeline of the milestones for a particular subject.

2. The name of the disease milestone is recorded in MIDS.
   a. For disease milestones that can occur only once (TMRPT = "N"), the value of MIDS may be the value in MIDSTYPE or may an abbreviated version.
   b. For types of disease milestones that can occur multiple times, MIDS will usually be an abbreviated version of MIDSTYPE and will always end with a sequence number. Sequence numbers should start with 1 and indicate the chronological order of the instances of this type of disease milestone.

3. The timing variables SMSTDTC and SMENDTC hold start and end date/times of data collected for the disease milestone(s) for each subject. SMSTDY and SMENDY represent the corresponding study day variables.
   a. The start date/time of the disease milestone is the critical date/time, and must be populated. If the disease milestone is an event, then the meaning of "start date" for the event may need to be defined.
   b. The start study day will not be populated if the start date/time includes only a year or only a year and month.
   c. The end date/time for the disease milestone is less important than the start date/time. It will not be populated if the disease milestone is a finding without an end date/time or if it is an event or intervention for which an end date/time has not yet occurred or was not collected.
   d. The end study day will not be populated if the end date/time includes only a year or only a year and month.

<!-- source: knowledge_base/domains/SR/spec.md -->
# SR — Skin Response

> Class: Findings About | Structure: One record per finding, per object, per time point, per visit per subject

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

### SRSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### SRGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### SRREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external specimen identifier. Example: "Specimen ID".

### SRSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### SRTESTCD
- **Order:** 8
- **Label:** Skin Response Test or Exam Short Name
- **Type:** Char
- **Controlled Terms:** C112024
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in SRTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SRTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SRTESTCD cannot contain characters other than letters, numbers, or underscores.

### SRTEST
- **Order:** 9
- **Label:** Skin Response Test or Examination Name
- **Type:** Char
- **Controlled Terms:** C112023
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in SRTEST cannot be longer than 40 characters. Example: "Wheal Diameter".

### SROBJ
- **Order:** 10
- **Label:** Object of the Observation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Used to describe the object or focal point of the findings observation that is represented by --TEST. Examples: the dose of the immunogenic material or the allergen associated with the response (e.g., "Johnson Grass IgE 0.15 BAU mL").

### SRCAT
- **Order:** 11
- **Label:** Category for Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values across subjects.

### SRSCAT
- **Order:** 12
- **Label:** Subcategory for Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of SRCAT values.

### SRORRES
- **Order:** 13
- **Label:** Results or Findings in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Results of measurement or finding as originally received or collected.

### SRORRESU
- **Order:** 14
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for SRORRES. Example: "mm".

### SRSTRESC
- **Order:** 15
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from SRORRES, in a standard format or in standard units. SRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in SRSTRESN.

### SRSTRESN
- **Order:** 16
- **Label:** Numeric Results/Findings in Std. Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from SRSTRESC. SRSTRESN should store all numeric test results or findings.

### SRSTRESU
- **Order:** 17
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized units used for SRSTRESC and SRSTRESN. Example: "mm".

### SRSTAT
- **Order:** 18
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate exam not done. Should be null if a result exists in SRORRES.

### SRREASND
- **Order:** 19
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Used in conjunction with SRSTAT when value is "NOT DONE".

### SRNAM
- **Order:** 20
- **Label:** Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Name or identifier of the laboratory or vendor who provided the test results.

### SRSPEC
- **Order:** 21
- **Label:** Specimen Type
- **Type:** Char
- **Controlled Terms:** C78734
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Defines the types of specimen used for a measurement. Example: "SKIN".

### SRLOC
- **Order:** 22
- **Label:** Location Used for Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Location relevant to the collection of the measurement.

### SRLAT
- **Order:** 23
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location further detailing laterality of intervention administration. Examples: "RIGHT", "LEFT", "BILATERAL".

### SRMETHOD
- **Order:** 24
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of test or examination. Examples: "ELISA", "EIA", "MICRONEUTRALIZATION ASSAY", "PLAQUE REDUCTION NEUTRALIZATION ASSAY".

### SRLOBXFL
- **Order:** 25
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### SRBLFL
- **Order:** 26
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. The value should be "Y" or null. Note that SRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### SREVAL
- **Order:** 27
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of person who provided evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "INVESTIGATOR", "ADJUDICATION COMMITTEE", "VENDOR".

### VISITNUM
- **Order:** 28
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 29
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 30
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 31
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 32
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time of the observation. Examples: "SCREENING", "TREATMENT", and "FOLLOW-UP".

### SRDTC
- **Order:** 33
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation represented in ISO 8601.

### SRDY
- **Order:** 34
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to sponsor- defined RFSTDTC in Demographics.

### SRTPT
- **Order:** 35
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point, such as time of last dose. See SRTPTNUM and SRTPTREF. Examples: "START", "5 MIN POST".

### SRTPTNUM
- **Order:** 36
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of SRTPT to aid in sorting.

### SRELTM
- **Order:** 37
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a fixed time point reference (SRTPTREF). Not a clock time or a date time variable. Represented as an ISO 8601 duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by EGTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by SRTPTREF.

### SRTPTREF
- **Order:** 38
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by SRELTM, SRTPTNUM, and SRTPT. Example: "INTRADERMAL INJECTION".

### SRRFTDTC
- **Order:** 39
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, SRTPTREF.
---

## Cross References

### Controlled Terminology
- [Skin Response Test Name (C112023)](../../terminology/core/findings_about.md) — SRTEST
- [Skin Response Test Code (C112024)](../../terminology/core/findings_about.md) — SRTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — SRLOBXFL, SRBLFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — SRSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — SRORRESU, SRSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — SRLOC
- [Specimen Type (C78734)](../../terminology/core/general_part4.md) — SRSPEC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — SREVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — SRMETHOD
- [Laterality (C99073)](../../terminology/core/general_part2.md) — SRLAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings About):** FA
- **Source Domain:** [AE](../AE/) — device-related findings about AEs
- **Source Domain:** [CM](../CM/) — device-related findings about treatments
- **Source Domain:** [PR](../PR/) — device-related findings about procedures

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings About class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/SR/assumptions.md -->
# SR — Assumptions

1. The Skin Response (SR) domain is used to represent findings about an intervention, but it has its own domain code, SR, rather than the domain code FA.

2. This domain is intended specifically for tests of the immune response to substances that are intended to provoke such a response (e.g., allergens used in allergy testing). SR is not intended for other injection-site reactions, including reactogenicity events that may follow a vaccine administration.

3. Because a subject is typically exposed to many test materials at the same time, SROBJ is needed to represent the test material for each response record. The method of assessment could be a skin-prick test, a skin-scratch test, or other method of introducing the challenge substance into the skin.

4. Any Identifier variables, Timing variables, or Findings general observation class qualifiers may be added to the SR domain, but the following qualifiers would not generally be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --LOINC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/SS/spec.md -->
# SS — Subject Status

> Class: Findings | Structure: One record per status per visit per subject

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

### SSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### SSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### SSSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number from the Procedure or Test page.

### SSTESTCD
- **Order:** 7
- **Label:** Status Short Name
- **Type:** Char
- **Controlled Terms:** C124305
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the status assessment described in SSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in SSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). SSTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "SURVSTAT".

### SSTEST
- **Order:** 8
- **Label:** Status Name
- **Type:** Char
- **Controlled Terms:** C124306
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the status assessment used to obtain the finding. The value in SSTEST cannot be longer than 40 characters. Example: "Survival Status".

### SSCAT
- **Order:** 9
- **Label:** Category for Assessment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize observations across subjects.

### SSSCAT
- **Order:** 10
- **Label:** Subcategory for Assessment
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization.

### SSORRES
- **Order:** 11
- **Label:** Result or Finding Original Result
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the status assessment finding as originally received or collected.

### SSSTRESC
- **Order:** 12
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C124304
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from SSORRES, in a standard format.

### SSSTAT
- **Order:** 13
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a status assessment was not done. Should be null if a result exists in SSORRES.

### SSREASND
- **Order:** 14
- **Label:** Reason Assessment Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why an assessment was not performed. Example: "Subject refused". Used in conjunction with SSSTAT when value is "NOT DONE".

### SSEVAL
- **Order:** 15
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain collected or derived data. Examples: "CAREGIVER", "ADJUDICATION COMMITTEE", "FRIEND".

### VISITNUM
- **Order:** 16
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 17
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 18
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 19
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm.

### EPOCH
- **Order:** 20
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the start date/time of the subject status assessment.

### SSDTC
- **Order:** 21
- **Label:** Date/Time of Assessment
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of the subject status assessment represented in ISO 8601 character format.

### SSDY
- **Order:** 22
- **Label:** Study Day of Assessment
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the subject status assessment, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
---

## Cross References

### Controlled Terminology
- [Subject Status Response (C124304)](../../terminology/core/other_part5.md) — SSSTRESC
- [Subject Status Test Code (C124305)](../../terminology/core/other_part5.md) — SSTESTCD
- [Subject Status Test Name (C124306)](../../terminology/core/other_part5.md) — SSTEST
- [Not Done (C66789)](../../terminology/core/general_part4.md) — SSSTAT
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — SSEVAL
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, TR, TU, UR, VS
- **Related Domain:** [DS](../DS/) — subject status vs disposition

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/SS/assumptions.md -->
# SS — Assumptions

1. Details about the circumstances of a subject's status are stored in the appropriate separate domain(s), even when collection is triggered by the response to the status assessment. For example, if a subject's survival status is "DEAD", the date of death must be stored in DM and within a final disposition record in DS. Only the status collection date, the status question, and the status response are stored in SS.

2. RELREC may be used to link assessments in SS with data in other domains that were collected as a result of the subject's status assessment.

3. There are separate codelists for SS tests and responses.
   a. Associations between the SS tests and response codelists are described in the SS Codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

4. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the SS domain, but the following qualifiers would generally not be used: --MODIFY, --POS, --BODSYS, --ORRESU, --ORNRLO, --ORNRHI, --STRESN, --STRESU, --STNRLO, --STNRHI, --STNRC, --NRIND, --RESCAT, --XFN, --NAM, --LOINC, --SPEC, --SPCCND, --LOC, --METHOD, --BLFL, --FAST, --DRVFL, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/SU/spec.md -->
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

<!-- source: knowledge_base/domains/SU/assumptions.md -->
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

<!-- source: knowledge_base/domains/SUPPQUAL/spec.md -->
# SUPPQUAL — Supplemental Qualifiers for [domain name]

> Class: Relationship | Structure: One record per supplemental qualifier per related parent domain record(s)

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Study identifier of the parent record(s).

### RDOMAIN
- **Order:** 2
- **Label:** Related Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** C66734
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain of the parent record(s).

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. This is the value of USUBJID in the parent record(s).

### IDVAR
- **Order:** 4
- **Label:** Identifying Variable
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifying variable in the dataset that identifies the related record(s). Examples: --SEQ, --GRPID.

### IDVARVAL
- **Order:** 5
- **Label:** Identifying Variable Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Value of identifying variable of the parent record(s).

### QNAM
- **Order:** 6
- **Label:** Qualifier Variable Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** The short name of the qualifier variable, which is used as a column name in a domain view with data from the parent domain. The value in QNAM cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). QNAM cannot contain characters other than letters, numbers, or underscores. This will often be the column name in the sponsor's operational dataset.

### QLABEL
- **Order:** 7
- **Label:** Qualifier Variable Label
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** This is the long name or label associated with QNAM. The value in QLABEL cannot be longer than 40 characters. This will often be the column label in the sponsor's original dataset.

### QVAL
- **Order:** 8
- **Label:** Data Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Req
- **CDISC Notes:** Result of, response to, or value associated with QNAM. A value for this column is required; no records can be in SUPP-- with a null value for QVAL.

### QORIG
- **Order:** 9
- **Label:** Origin
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Because QVAL can represent a mixture of collected (on a CRF), derived, or assigned items, QORIG is used to indicate the origin of this data. Examples: "CRF", "Assigned", "Derived". See Section 4.1.8, Origin Metadata.

### QEVAL
- **Order:** 10
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain objectively collected or derived data. Examples: "ADJUDICATION COMMITTEE", "STATISTICIAN", "DATABASE ADMINISTRATOR", "CLINICAL COORDINATOR".
---

## Cross References

### Controlled Terminology
- [SDTM Domain Abbreviation (C66734)](../../terminology/core/general_part4.md) — RDOMAIN
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — QEVAL

### Related Domains
- **Same class (Relationship):** RELREC, RELSPEC, RELSUB

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Relationship class definition](../../model/06_relationship_datasets.md)

<!-- source: knowledge_base/domains/SUPPQUAL/assumptions.md -->
# SUPPQUAL — Assumptions

The SDTM does not allow the addition of new variables. Therefore, the Supplemental Qualifiers special-purpose dataset model is used to capture non-standard variables (NSVs) and their association to parent records in general-observation class datasets (Events, Findings, Interventions), Demographics (DM), and Subject Visits (SV). Supplemental qualifiers are represented as separate SUPP-- datasets for each dataset containing sponsor-defined variables (see Section 8.4.2, Submitting Supplemental Qualifiers in Separate Datasets).

SUPP-- represents the metadata and data for each NSV/value combination. As the name suggests, this dataset is intended to capture additional qualifiers for an observation. Data that represent separate observations should be treated as separate observations. The Supplemental Qualifiers dataset is structured similarly to the RELREC dataset, in that it uses the same set of keys to identify parent records. Each SUPP-- record also includes the name of the qualifier variable being added (QNAM), the label for the variable (QLABEL), the actual value for each instance or record (QVAL), the origin (QORIG) of the value (see Section 4.1.8, Origin Metadata), and the evaluator (QEVAL) to specify the role of the individual who assigned the value (e.g., "ADJUDICATION COMMITTEE", "SPONSOR"). Controlled terminology for certain expected values for QNAM and QLABEL is included in Appendix C1, Supplemental Qualifiers Name Codes.

SUPP-- datasets are also used to capture attributions. An attribution is typically an interpretation or subjective classification of 1 or more observations by a specific evaluator, such as a flag that indicates whether an observation was considered to be clinically significant. It is possible that different attributions may be necessary in some cases; SUPP-- provides a mechanism for incorporating as many attributions as are necessary. A SUPP-- dataset can contain both objective data (where values are collected or derived algorithmically) and subjective data (attributions where values are assigned by a person or committee). For objective data, the value in QEVAL will be null. For subjective data, the value in QEVAL should reflect the role of the person or institution assigning the value (e.g., "SPONSOR", "ADJUDICATION COMMITTEE").

The combined set of values for the first 6 columns (STUDYID...QNAM) should be unique for every record. That is, there should not be multiple records in a SUPP-- dataset for the same QNAM value, as it relates to IDVAR/IDVARVAL for a USUBJID in a domain. For example, if 2 individuals (e.g., the investigator and an independent adjudicator) provide a determination regarding whether an adverse event is treatment-emergent, then separate QNAM values should be used for each set of information (e.g., "AETRTEMI", "AETRTEMA"). This is necessary to ensure that reviewers can join/merge/transpose the information back with the records in the original domain without risk of losing information.

A record in a SUPP-- dataset relates back to its parent record(s) via the key identified by the STUDYID, RDOMAIN, USUBJID, and IDVAR/IDVARVAL variables. An exception is SUPP-- dataset records that are related to Demographics (DM) records, where both IDVAR and IDVARVAL will be null because the key variables STUDYID, RDOMAIN, and USUBJID are sufficient to identify the unique parent record in DM (DM has 1 record per USUBJID).

All records in the SUPP-- datasets must have a value for QVAL. Transposing source variables with missing/null values may generate SUPP-- records with null values for QVAL, causing the SUPP-- datasets to be extremely large. When this happens, the sponsor must delete the records where QVAL is null prior to submission.

## Submitting Supplemental Qualifiers in Separate Datasets

There is a one-to-one correspondence between a domain dataset and its Supplemental Qualifier dataset. The single SUPPQUAL dataset option that was introduced in SDTMIG v3.1 was deprecated. The set of supplemental qualifiers for each domain is included in a separate dataset with the name SUPP-- (where "--" denotes the source domain which the supplemental qualifiers relate back to). For example, Demographics (DM) qualifiers would be submitted in suppdm.xpt. When data have been split into multiple datasets (see Section 4.1.7, Splitting Domains), longer names such as SUPPFAMH may be needed.

## When Not to Use Supplemental Qualifiers

The following are examples of data that should **not** be submitted as supplemental qualifiers:

- Subject-level objective data that fit in Subject Characteristics (SC; e.g., national origin, twin type)
- Findings interpretations that should be added as an additional test code and result. An example of this would be a record for electrocardiogram interpretation where EGTESTCD = "INTP", and the same EGGRPID or EGREFID value would be assigned for all records associated with that ECG (see Section 4.5.5, Clinical Significance for Findings Observation Class Data).
- Comments related to a record or records contained within a parent domain. Although they may have been collected in the same record by the sponsor, comments should instead be captured in the CO special-purpose domain.
- Data not directly related to records in a parent domain. Such records should instead be captured in either a separate general observation class domain or special-purpose domain.

<!-- source: knowledge_base/domains/SV/spec.md -->
# SV — Subject Visits

> Class: Special-Purpose | Structure: One record per actual or planned visit per subject

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
- **CDISC Notes:** Two-character abbreviation for the domain most relevant to the observation. The domain abbreviation is also used as a prefix for variables to ensure uniqueness when datasets are merged.

### USUBJID
- **Order:** 3
- **Label:** Unique Subject Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product.

### VISITNUM
- **Order:** 4
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 5
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### SVPRESP
- **Order:** 6
- **Label:** Pre-specified
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to indicate whether the visit was planned (i.e., visits specified in the TV domain). Value is "Y" for planned visits, null for unplanned visits.

### SVOCCUR
- **Order:** 7
- **Label:** Occurrence
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to record whether a planned visit occurred. The value is null for unplanned visits.

### SVREASOC
- **Order:** 8
- **Label:** Reason for Occur Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The reason for the value in SVOCCUR. If SVOCCUR="N", SVREASOC is the reason the visit did not occur.

### SVCNTMOD
- **Order:** 9
- **Label:** Contact Mode
- **Type:** Char
- **Controlled Terms:** C171445
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The way in which the visit was conducted. Examples: "IN PERSON", "TELEPHONE CALL", "IVRS".

### SVEPCHGI
- **Order:** 10
- **Label:** Epi/Pandemic Related Change Indicator
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicates whether the visit was changed due to an epidemic or pandemic.

### VISITDY
- **Order:** 11
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### SVSTDTC
- **Order:** 12
- **Label:** Start Date/Time of Observation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Start date/time of an observation represented in IS0 8601 character format.

### SVENDTC
- **Order:** 13
- **Label:** End Date/Time of Observation
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** End date/time of the observation represented in IS0 8601 character format.

### SVSTDY
- **Order:** 14
- **Label:** Study Day of Start of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### SVENDY
- **Order:** 15
- **Label:** Study Day of End of Observation
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### SVUPDES
- **Order:** 16
- **Label:** Description of Unplanned Visit
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of what happened to the subject during an unplanned visit. Only populated for unplanned visits.
---

## Cross References

### Controlled Terminology
- [Mode of Subject Contact (C171445)](../../terminology/core/special_purpose.md) — SVCNTMOD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — SVPRESP, SVOCCUR, SVEPCHGI

### Related Domains
- **Same class (Special-Purpose):** CO, DM, SE, SM

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Special-Purpose class definition](../../model/03_special_purpose_domains.md)

<!-- source: knowledge_base/domains/SV/assumptions.md -->
# SV — Assumptions

1. The Subject Visits domain allows the submission of data on the timing of the trial visits for a subject, including both those visits they actually passed through in their participation in the trial and those visits that did not occur. Refer to Section 7.3.1, Trial Visits (TV), as the TV dataset defines the planned visits for the trial.

2. Subjects can have 1 and only 1 record per VISITNUM.

3. Subjects who screen fail, withdraw, die, or otherwise discontinue study participation will not have records for planned visits subsequent to their final disposition event.

4. Planned and unplanned visits with a subject, whether or not they are physical visits to the investigational site, are represented in this domain.
   a. SVPRESP = "Y" identifies rows for planned visits.
   b. For planned visits, SVOCCUR indicates whether the visit occurred.
   c. For unplanned visits, SVPRESP and SVOCCUR are null.
   d. See Section 4.5.7, Presence or Absence of Prespecified Interventions and Events, for more information on the use of --PRESP and --OCCUR.

5. The identification of an actual visit with a planned visit sometimes calls for judgment. In general, data collection forms are prepared for particular visits, and the fact that data was collected on a form labeled with a planned visit is sufficient to make the association. Occasionally, the association will not be so clear, and the sponsor will need to make decisions about how to label actual visits. The sponsor's rules for making such decisions should be documented in the Define-XML document.

6. Records for unplanned visits should be included in the SV dataset. For unplanned visits, SVUPDES can be populated with a description of the reason for the unplanned visit. Some judgment may be required to determine what constitutes an unplanned visit. When data are collected outside a planned visit, that act of collecting data may or may not be described as a "visit." The encounter should generally be treated as a visit if data from the encounter are included in any domain for which VISITNUM is included; a record with a missing value for VISITNUM is generally less useful than a record with VISITNUM populated. If the occasion is considered a visit, its date/times must be included in the SV table and a value of VISITNUM must be assigned. Refer to Section 4.4.5, Clinical Encounters and Visits, for information on the population of visit variables for unplanned visits.

7. The variable SVCNTMOD is used to record the way in which the visit was conducted. For example, for visits to a clinic, SVCNTMOD = "IN PERSON", visits conducted remotely might have values such as "TELEPHONE", "REMOTE AUDIO VIDEO", or "IVRS". If there are multiple contact modes, refer to Section 4.2.8.3, Multiple Values for a Non-result Qualifier Variable.

8. The planned study day of visit variable (VISITDY) should not be populated for unplanned visits.

9. If SVSTDY is included, it is the actual study day corresponding to SVSTDTC. In studies for which VISITDY has been populated, it may be desirable to populate SVSTDY, as this will facilitate the comparison of planned (VISITDY) and actual (SVSTDY) study days for the start of a visit.

10. If SVENDY is included, it is the actual day corresponding to SVENDTC.

11. For many studies, all visits are assumed to occur within 1 calendar day, and only 1 date is collected for the visit. In such a case, the values for SVENDTC duplicate values in SVSTDTC. However, if the data for a visit is actually collected over several physical visits and/or over several days, then SVSTDTC and SVENDTC should reflect this fact. Note that it is fairly common for screening data to be collected over several days, but for the data to be treated as belonging to a single planned screening visit, even in studies for which all other visits are single-day visits.

12. Differentiating between planned and unplanned visits may be challenging if unplanned assessments (e.g., repeat labs) are performed during the time period of a planned visit.

13. Algorithms for populating SVSTDTC and SVENDTC from the dates of assessments performed at a visit may be particularly challenging for screening visits, since baseline values collected at a screening visit are sometimes historical data from tests performed before the subject started screening for the trial. Therefore dates prior to informed consent are not part of the determination of SVSTDTC.

14. The following Identifier variables are permissible and may be added as appropriate: --SEQ, --GRPID, --REFID, and --SPID.

15. Care should be taken in adding additional timing variables:
    a. If TAETORD and/or EPOCH are added, then the values must be those at the start of the visit.
    b. The purpose of --DTC and --DY in other domains with start and end dates (Event and Intervention Domains) is to record the date on which data was collected. For a visit that occurred, it is not necessary to submit the date on which information about the visit was collected. When SVPRESP = "Y" and SVOCCUR = "N", --DTC and --DY are available for use to represent the date on which it was recorded that the visit did not take place.
    c. --DUR could be added if the duration of a visit was collected.
    d. It would be inappropriate to add the variables that support time points (--TPT, --TPTNUM, --ELTM, --TPTREF, and --RFTDTC), because the topic of this dataset is visits.
    e. --STRF and --ENRF could be used to say whether a visit started and ended before, during, or after the study reference period, although this seems unnecessary.
    f. --STRTPT, --STTPT, --ENRTPT, and --ENTPT could be used to say that a visit started or ended before or after particular dates, although this seems unnecessary.

16. SVOCCUR = "N" records are only to be created for planned visits that were expected to occur before the end of the subject's participation.

<!-- source: knowledge_base/domains/TA/spec.md -->
# TA — Trial Arms

> Class: Trial Design | Structure: One record per planned Element per Arm

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

### ARMCD
- **Order:** 3
- **Label:** Planned Arm Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than that for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20.

### ARM
- **Order:** 4
- **Label:** Description of Planned Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name given to an arm or treatment group.

### TAETORD
- **Order:** 5
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** Number that gives the order of the element within the arm.

### ETCD
- **Order:** 6
- **Label:** Element Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.

### ELEMENT
- **Order:** 7
- **Label:** Description of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** The name of the element. The same element may occur more than once within an arm.

### TABRANCH
- **Order:** 8
- **Label:** Branch
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Exp
- **CDISC Notes:** Condition subject met, at a "branch" in the trial design at the end of this element, to be included in this arm (e.g., "Randomization to DRUG X").

### TATRANS
- **Order:** 9
- **Label:** Transition Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Exp
- **CDISC Notes:** If the trial design allows a subject to transition to an element other than the next element in sequence, then the conditions for transitioning to those other elements, and the alternative element sequences, are specified in this rule (e.g., "Responders go to washout").

### EPOCH
- **Order:** 10
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** Name of the trial epoch with which this element of the arm is associated.
---

## Cross References

### Controlled Terminology
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Trial Design):** TD, TE, TI, TM, TS, TV
- **Trial Design:** [TE](../TE/) — arms use elements
- **Trial Design:** [TV](../TV/) — arms define visit schedules

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

<!-- source: knowledge_base/domains/TA/assumptions.md -->
# TA — Assumptions

The TA and TE datasets are interrelated, and they provide the building blocks for the development of subject-level treatment information (see Sections 5.2, Demographics (DM), and 5.3, Subject Elements (SE), for the subject's actual study treatment information).

1. TAETORD is an integer. In general, the value of TAETORD is 1 for the first element in each arm, 2 for the second element in each arm, and so on. Occasionally, it may be convenient to skip some values (see Example Trial 6). Although the values of TAETORD need not always be sequential, their order must always be the correct order for the elements in the arm path.

2. Elements in different arms with the same value of TAETORD may or may not be at the same time, depending on the design of the trial. The example trials illustrate a variety of possible situations. The same element may occur more than once within an arm.

3. TABRANCH describes the outcome of a branch decision point in the trial design for subjects in the arm. A branch decision point takes place between epochs, and is associated with the element that ends at the decision point. For instance, if subjects are assigned to an arm where they receive treatment A through a randomization at the end of element X, the value of TABRANCH for element X would be "Randomized to A."

4. Branch decision points may be based on decision processes other than randomizations (e.g., clinical evaluations of disease response, subject choice).

5. There is usually some gap in time between the performance of a randomization and the start of randomized treatment. However, in many trials this gap in time is small and it is highly unlikely that subjects will leave the trial between randomization and treatment. In these circumstances, the trial does not need to be modeled with this time period between randomization and start of treatment as a separate element.

6. Some trials include multiple paths that are closely enough related so that they are all considered to belong to 1 arm. In general, this set of paths will include a "complete" path along with shorter paths that skip some elements. The sequence of elements represented in the trial arms should be the complete, longest path. TATRANS describes the decision points that may lead to a shortened path within the arm.

7. If an element does not end with a decision that could lead to a shortened path within the arm, then TATRANS will be blank. If there is such a decision, TATRANS will be in a form like, "If condition X is true, then go to epoch Y" or "If condition X is true, then go to element with TAETORD = 'Z'".

8. EPOCH is not strictly necessary for describing the sequence of elements in an arm path, but it is the conceptual basis for comparisons between arms and also provides a useful way to talk about what is happening in a blinded trial while it is blinded. During periods of blinded treatment, blinded participants will not know which arm and element a subject is in, but EPOCH should provide a description of the time period that does not depend on knowing arm.

9. EPOCH should be assigned in such a way that elements from different arms with the same value of EPOCH are "comparable" in some sense. The degree of similarity of epochs across arms varies considerably in different trials, as illustrated in the examples.

10. EPOCH values for multiple similar epochs:
    a. When a study design includes multiple epochs with the same purpose (e.g., multiple similar treatment epochs), it is recommended that the EPOCH values be terms from controlled terminology, but with numbers appended. For example, multiple treatment epochs could be represented using "TREATMENT 1", "TREATMENT 2", and so on. Because the codelist is extensible, this convention allows multiple similar epochs to be represented without adding numbered terms to the CDISC Controlled Terminology for epoch. The inclusion of multiple numbered terms in the EPOCH codelist is not considered to add value.
    b. Note that the controlled terminology does include some more granular terms for distinguishing between epochs that differ in ways other than mere order, and these terms should be used where applicable, as they are more informative. For example, when "BLINDED TREATMENT" and "OPEN LABEL TREATMENT" are applicable, those terms would be preferred over "TREATMENT 1" and "TREATMENT 2".

11. Note that study cells are not explicitly defined in the TA dataset. A set of records with a common value of both ARMCD and EPOCH constitute the description of a study cell. Transition rules within this set of records are also part of the description of the study cell.

12. EPOCH may be used as a timing variable in other datasets, such as Exposure (EX) and Disposition (DS), and values of EPOCH must be different for different epochs. For instance, in a crossover trial with 3 treatment epochs, each must be given a distinct name; all 3 cannot be called "TREATMENT".

<!-- source: knowledge_base/domains/TD/spec.md -->
# TD — Trial Disease Assessments

> Class: Trial Design | Structure: One record per planned constant assessment period

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

### TDORDER
- **Order:** 3
- **Label:** Sequence of Planned Assessment Schedule
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** A number given to ensure ordinal sequencing of the planned assessment schedules within a trial.

### TDANCVAR
- **Order:** 4
- **Label:** Anchor Variable Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** A reference to the date variable name that provides the start point from which the planned disease assessment schedule is measured. This must be a referenced from the ADaM ADSL dataset (e.g., "ANCH1DT"). Note: TDANCVAR will contain the name of a reference date variable.

### TDSTOFF
- **Order:** 5
- **Label:** Offset from the Anchor
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** A fixed offset from the date provided by the variable referenced in TDANCVAR. This is used when the timing of planned cycles does not start on the exact day referenced in the variable indicated in TDANCVAR. The value of this variable will be either zero or a positive value and will be represented in ISO 8601 character format.

### TDTGTPAI
- **Order:** 6
- **Label:** Planned Assessment Interval
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** The planned interval between disease assessments represented in ISO 8601 character format.

### TDMINPAI
- **Order:** 7
- **Label:** Planned Assessment Interval Minimum
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** The lower limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format.

### TDMAXPAI
- **Order:** 8
- **Label:** Planned Assessment Interval Maximum
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** The upper limit of the allowed range for the planned interval between disease assessments represented in ISO 8601 character format.

### TDNUMRPT
- **Order:** 9
- **Label:** Maximum Number of Actual Assessments
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** This variable must represent the maximum number of actual assessments for the analysis that this disease assessment schedule describes. In a trial where the maximum number of assessments is not defined explicitly in the protocol (e.g., assessments occur until death), TDNUMRPT should represent the maximum number of disease assessments that support the efficacy analysis encountered by any subject across the trial at that point in time.
---

## Cross References

### Related Domains
- **Same class (Trial Design):** TA, TE, TI, TM, TS, TV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

<!-- source: knowledge_base/domains/TD/assumptions.md -->
# TD — Assumptions

The purpose of the Trial Disease Assessments (TD) domain is to provide information on planned scheduling of disease assessments when the scheduling of disease assessments is not necessarily tied to the scheduling of visits. In oncology studies, good compliance with the disease-assessment schedule is essential to reduce the risk of "assessment time bias." The TD domain makes possible an evaluation of assessment time bias from the SDTM, in particular for studies with progression-free survival (PFS) endpoints. TD has limited utility in oncology and was developed specifically with RECIST in mind and where an assessment-time bias analysis is appropriate. It is understood that extending this approach to Cheson and other criteria may not be appropriate or may pose difficulties. It is also understood that this approach may not be necessary in non-oncology studies, although it is available for use if appropriate.

1. The purpose of the Trial Disease Assessments (TD) domain is to provide information on planned scheduling of disease assessments when the scheduling of disease assessments is not necessarily tied to the scheduling of visits. In oncology studies, good compliance with the disease-assessment schedule is essential to reduce the risk of "assessment time bias." The TD domain makes possible an evaluation of assessment time bias from the SDTM, in particular for studies with progression-free survival (PFS) endpoints.

2. A planned schedule of assessments will have a defined start point; the TDANCVAR variable is used to identify the variable in the ADaM subject-level dataset (ADSL) that holds the "anchor" date. By default, the anchor variable for the first pattern is ANCH1DT. An anchor date must be provided for each pattern of assessments, and each anchor variable must exist in ADSL. TDANCVAR is therefore a Required variable. Anchor date variable names should adhere to ADaM variable naming conventions (e.g., ANCH1DT, ANCH2DT). One anchor date may be used to anchor more than 1 pattern of disease assessments. When that is the case, the appropriate offset for the start of a subsequent pattern, represented as an ISO 8601 duration value, should be provided in the TDSTOFF variable.

3. The TDSTOFF variable is used in conjunction with the anchor date value (from the anchor date variable identified in TDANCVAR). If the pattern of disease assessments does not start exactly on a date collected on the CRF, this variable will represent the offset between the anchor date value and the start date of the pattern of disease assessments. This may be a positive or zero interval value represented in an ISO 8601 format.

4. A pattern of assessments consists of a series of intervals of equal duration, each followed by an assessment. Thus, the first assessment in a pattern is planned to occur at the anchor date (given by the variable named in TDANCVAR) plus the offset (TDSTOFF) plus the target assessment interval (TDTGTPAI). A baseline evaluation is usually not preceded by an interval, and would therefore not be considered part of an assessment pattern.

5. This domain should not be created when the disease assessment schedule may vary for individual subjects (e.g., when completion of the first phase of a study is event-driven).

<!-- source: knowledge_base/domains/TE/spec.md -->
# TE — Trial Elements

> Class: Trial Design | Structure: One record per planned Element

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

### ETCD
- **Order:** 3
- **Label:** Element Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.

### ELEMENT
- **Order:** 4
- **Label:** Description of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** The name of the element.

### TESTRL
- **Order:** 5
- **Label:** Rule for Start of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Req
- **CDISC Notes:** Describes condition for beginning element.

### TEENRL
- **Order:** 6
- **Label:** Rule for End of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Perm
- **CDISC Notes:** Describes condition for ending element. Either TEENRL or TEDUR must be present for each element.

### TEDUR
- **Order:** 7
- **Label:** Planned Duration of Element
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned duration of element in ISO 8601 format. Used when the rule for ending the element is applied after a fixed duration.
---

## Cross References

### Related Domains
- **Same class (Trial Design):** TA, TD, TI, TM, TS, TV
- **Trial Design:** [TA](../TA/) — elements compose arms

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

<!-- source: knowledge_base/domains/TE/assumptions.md -->
# TE — Assumptions

The Trial Elements (TE) dataset contains the definitions of the elements that appear in the Trial Arms (TA) dataset. An element may appear multiple times in the TA table because it appears either (1) in multiple arms, (2) multiple times within an arm, or (3) both. However, an element will appear only once in the TE table.

Each row in the TE dataset may be thought of as representing a "unique element" in the same sense of "unique" as a CRF template page for a collecting certain type of data referred to as "unique page."

An element is a building block for creating study cells, and an arm is composed of study cells. Trial elements represent an interval of time that serves a purpose in the trial and are associated with certain activities affecting the subject. "Week 2 to week 4" is not a valid trial element.

1. There are no gaps between elements. The instant one element ends, the next element begins. A subject spends no time "between" elements.

2. The ELEMENT (Description of the Element) variable usually indicates the treatment being administered during an element, or, if no treatment is being administered, the other activities that are the purpose of this period of time (e.g., "Screening", "Follow-up", "Washout"). In some cases, this time period may be quite passive (e.g., "Rest"; "Wait, for disease episode").

3. The TESTRL (Rule for Start of Element) variable identifies the event that marks the transition into this element. For elements that involve treatment, this is the start of treatment.

4. For elements that do not involve treatment, TESTRL can be more difficult to define. For washout and follow-up elements, which always follow treatment elements, the start of the element may be defined relative to the end of a preceding treatment. For example, a washout period might be defined as starting 24 or 48 hours after the last dose of drug for the preceding treatment element or epoch. This definition is not totally independent of the TA dataset, because it relies on knowing where in the trial design the element is used, and that it always follows a treatment element. Defining a clear starting point for the start of a non-treatment element that always follows another non-treatment element can be particularly difficult. The transition may be defined by a decision-making activity such as enrollment or randomization.

5. TESTRL for a treatment element may be thought of as "active" whereas the start rule for a non-treatment element—particularly a follow-up or washout element—may be "passive." The start of a treatment element will not occur until a dose is given, no matter how long that dose is delayed. Once the last dose is given, the start of a subsequent non-treatment element is inevitable, as long as another dose is not given.

6. Note that the date/time of the event described in TESTRL will be used to populate the date/times in the Subject Elements (SE) dataset, so the date/time of the event should be captured in the CRF.

7. Specifying TESTRL for an element that serves the first element of an arm in the TA dataset involves defining the start of the trial. In the examples in this document, obtaining informed consent has been used as "Trial Entry."

8. TESTRL should be expressed without referring to arm. If the element appears in more than 1 arm in the TA dataset, then the element description (ELEMENT) **must not** refer to any arms.

9. TESTRL should be expressed without referring to epoch. If the element appears in more than 1 epoch in the TA dataset, then the Element description (ELEMENT) **must not** refer to any epochs.

10. For a blinded trial, it is useful to describe TESTRL in terms that separate the properties of the event that are visible to blinded participants from the properties that are visible only to those who are unblinded. For treatment elements in blinded trials, wording such as the following is suitable: "First dose of study drug for a treatment epoch, where study drug is X."

11. Element end rules are rather different from element start rules. The actual end of one element is the beginning of the next element. Thus, the element end rule does not give the conditions under which an element does end, but the conditions under which it should end or is planned to end.

12. At least 1 of TEENRL and TEDUR must be populated. Both may be populated.

13. TEENRL describes the circumstances under which a subject should leave this element. Element end rules may depend on a variety of conditions. For instance, a typical criterion for ending a rest element between oncology chemotherapy-treatment element would be, "15 days after start of element and WBC counts have recovered." The TA dataset, not the TE dataset, describes where the subject moves next, so TEENRL must be expressed without referring to arm.

14. TEDUR serves the same purpose as TEENRL for the special (but very common) case of an element with a fixed duration. TEDUR is expressed in ISO 8601 format. For example, a TEDUR value of P6W is equivalent to a TEENRL of "6 weeks after the start of the element."

15. Note that elements that have different start and end rules are different elements and must have different values of ELEMENT and ETCD. For instance, elements that involve the same treatment but have different durations are different elements. The same applies to non-treatment elements.

<!-- source: knowledge_base/domains/TI/spec.md -->
# TI — Trial Inclusion/Exclusion Criteria

> Class: Trial Design | Structure: One record per I/E criterion

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

### IETESTCD
- **Order:** 3
- **Label:** Incl/Excl Criterion Short Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name IETEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). IETESTCD cannot contain characters other than letters, numbers, or underscores. The prefix "IE" is used to ensure consistency with the IE domain.

### IETEST
- **Order:** 4
- **Label:** Inclusion/Exclusion Criterion
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Full text of the inclusion or exclusion criterion. The prefix "IE" is used to ensure consistency with the IE domain.

### IECAT
- **Order:** 5
- **Label:** Inclusion/Exclusion Category
- **Type:** Char
- **Controlled Terms:** C66797
- **Role:** Grouping Qualifier
- **Core:** Req
- **CDISC Notes:** Used for categorization of the inclusion or exclusion criteria.

### IESCAT
- **Order:** 6
- **Label:** Inclusion/Exclusion Subcategory
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of the exception criterion. Can be used to distinguish criteria for a sub-study or to categorize as major or minor exceptions. Examples: "MAJOR", "MINOR".

### TIRL
- **Order:** 7
- **Label:** Inclusion/Exclusion Criterion Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Perm
- **CDISC Notes:** Rule that expresses the criterion in computer-executable form. See Assumption 4.

### TIVERS
- **Order:** 8
- **Label:** Protocol Criteria Versions
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The number of this version of the Inclusion/Exclusion criteria. May be omitted if there is only 1 version.
---

## Cross References

### Controlled Terminology
- [Category of Inclusion/Exclusion (C66797)](../../terminology/core/general_part2.md) — IECAT

### Related Domains
- **Same class (Trial Design):** TA, TD, TE, TM, TS, TV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

<!-- source: knowledge_base/domains/TI/assumptions.md -->
# TI — Assumptions

The variable TIRL was included in the Trial Inclusion/Exclusion Criteria (TI) domain in anticipation of developing a way to represent eligibility criteria in a computer-executable manner. However, such a method has not been developed, and it is not clear that an SDTM dataset would be the best place to represent such a computer-executable representation.

TI contains all the inclusion and exclusion criteria for the trial, and thus provides information that may not be present in the subject-level data on inclusion and exclusion criteria. The IE domain (described in Section 6.3.4, Inclusion/Exclusion Criteria Not Met) contains records only for inclusion and exclusion criteria that subjects did not meet.

1. If inclusion/exclusion criteria were amended during the trial, then each complete set of criteria must be included in the TI domain. TIVERS is used to distinguish between the versions.

2. Protocol version numbers should be used to identify criteria versions, although there may be more versions of the protocol than versions of the inclusion/exclusion criteria. For example, a protocol might have versions 1, 2, 3, and 4, but if the inclusion/exclusion criteria in version 1 were unchanged through versions 2 and 3, and changed only in version 4, then there would be 2 sets of inclusion/exclusion criteria in TI: one for version 1 and one for version 4.

3. Individual criteria do not have versions. If a criterion changes, it should be treated as a new criterion, with a new value for IETESTCD. If criteria have been numbered and values of IETESTCD are generally of the form INCL00n or EXCL00n, and new versions of a criterion have not been given new numbers, separate values of IETESTCD might be created by appending letters (e.g., INCL003A, INCL003B).

4. IETEST contains the text of the inclusion/exclusion criterion. However, because entry criteria are rules, the variable TIRL has been included in anticipation of the development of computer-executable rules.

5. If a criterion text is <200 characters, it goes in IETEST; if the text is >200 characters, put meaningful text in IETEST and describe the full text in the study metadata. See Section 4.5.3.1, Test Name (--TEST) Greater than 40 Characters, for further information.

<!-- source: knowledge_base/domains/TM/spec.md -->
# TM — Trial Disease Milestones

> Class: Trial Design | Structure: One record per Disease Milestone type

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
- **CDISC Notes:** Two-character abbreviation for the domain, which must be TM.

### MIDSTYPE
- **Order:** 3
- **Label:** Disease Milestone Type
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** The type of disease milestone. Example: "HYPOGLYCEMIC EVENT".

### TMDEF
- **Order:** 4
- **Label:** Disease Milestone Definition
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Req
- **CDISC Notes:** Definition of the disease milestone.

### TMRPT
- **Order:** 5
- **Label:** Disease Milestone Repetition Indicator
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** Indicates whether this is a disease milestone that can occur only once ("N") or a type of disease milestone that can occur multiple times ("Y").
---

## Cross References

### Controlled Terminology
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — TMRPT

### Related Domains
- **Same class (Trial Design):** TA, TD, TE, TI, TS, TV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

<!-- source: knowledge_base/domains/TM/assumptions.md -->
# TM — Assumptions

A trial design domain that is used to describe disease milestones, which are observations or activities anticipated to occur in the course of the disease under study, and which trigger the collection of data.

1. Disease milestones may be things that would be expected to happen before the study, or things that are anticipated to happen during the study. The occurrence of disease milestones for particular subjects are represented in the Subject Disease Milestones (SM) dataset.

2. The Trial Disease Milestones (TM) dataset contains a record for each type of disease milestone. The disease milestone is defined in TMDEF.

<!-- source: knowledge_base/domains/TR/spec.md -->
# TR — Tumor/Lesion Results

> Class: Findings | Structure: One record per tumor measurement/assessment per visit per subject per assessor

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

### TRSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number.

### TRGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain.

### TRREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier.

### TRSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### TRLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifier used to link the assessment result records to the individual tumor/lesion identification record in TU domain.

### TRLNKGRP
- **Order:** 9
- **Label:** Link Group
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to group and link all of the measurement/assessment records used in the assessment of the response record in the RS domain.

### TRTESTCD
- **Order:** 10
- **Label:** Tumor/Lesion Assessment Short Name
- **Type:** Char
- **Controlled Terms:** C96779
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the TEST in TRTEST. TRTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "TUMSTATE", "DIAMETER", "LESSCIND", "LESRVIND". See assumption 3.

### TRTEST
- **Order:** 11
- **Label:** Tumor/Lesion Assessment Test Name
- **Type:** Char
- **Controlled Terms:** C96778
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in TRTEST cannot be longer than 40 characters. Examples: "Tumor State", "Diameter", "Volume", "Lesion Success Indicator", "Lesion Revascularization Indicator". See assumption 3.

### TRORRES
- **Order:** 12
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the tumor/lesion measurement/assessment as originally received or collected.

### TRORRESU
- **Order:** 13
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for TRORRES. Example: "mm".

### TRSTRESC
- **Order:** 14
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** C124309
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from TRORRES, in a standard format or standard units. TRSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in TRSTRESN.

### TRSTRESN
- **Order:** 15
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from TRSTRESC. TRSTRESN should store all numeric test results or findings.

### TRSTRESU
- **Order:** 16
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for TRSTRESN.

### TRSTAT
- **Order:** 17
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Should be null if a result exists in TRORRES.

### TRREASND
- **Order:** 18
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a scan/image/physical exam was not performed or a tumor/lesion measurement was not taken. Examples: "SCAN NOT PERFORMED", "NOT ASSESSABLE: IMAGE OBSCURED TUMOR". Used in conjunction with TRSTAT when value is "NOT DONE".

### TRNAM
- **Order:** 19
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the vendor that performed the tumor/lesion measurement or assessment. This column can be left null when the investigator provides the complete set of data in the domain.

### TRMETHOD
- **Order:** 20
- **Label:** Method Used to Identify the Tumor/Lesion
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Method used to measure the tumor/lesion/location of interest. Examples: "MRI", "CT SCAN", "PET SCAN", "Coronary angiography".

### TRLOBXFL
- **Order:** 21
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally-derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.

### TRBLFL
- **Order:** 22
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that TRBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### TREVAL
- **Order:** 23
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR".

### TREVALID
- **Order:** 24
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in TREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 6.

### TRACPTFL
- **Order:** 25
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment.

### VISITNUM
- **Order:** 26
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 27
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 28
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

### TAETORD
- **Order:** 29
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### EPOCH
- **Order:** 30
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the element in the planned sequence of elements for the arm to which the subject was assigned.

### TRDTC
- **Order:** 31
- **Label:** Date/Time of Tumor/Lesion Measurement
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** The date of the scan/image/physical exam. TRDTC does not represent the date that the image was read to identify tumors/lesions. TRDTC also does not represent the VISIT date.

### TRDY
- **Order:** 32
- **Label:** Study Day of Tumor/Lesion Measurement
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
---

## Cross References

### Controlled Terminology
- [Tumor or Lesion Properties Test Result (C124309)](../../terminology/core/oncology_part2.md) — TRSTRESC
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — TRLOBXFL, TRBLFL, TRACPTFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — TRSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — TRORRESU, TRSTRESU
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — TREVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — TRMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — TREVALID
- [Tumor or Lesion Properties Test Name (C96778)](../../terminology/core/oncology_part2.md) — TRTEST
- [Tumor or Lesion Properties Test Code (C96779)](../../terminology/core/oncology_part2.md) — TRTESTCD
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TU, UR, VS
- **Shared Dataset:** [TU](../TU/) — tumor results ← tumor identification
- **Related Findings:** [RS](../RS/) — tumor results → disease response

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/TR/assumptions.md -->
# TR — Assumptions

A findings domain that represents quantitative measurements and/or qualitative assessments of the tumors, lesions, or locations of interest identified in the Tumor/Lesion Identification (TU) domain. The TR domain represents quantitative measurements and/or qualitative assessments of the tumors, lesions, or locations of interest (e.g., tumors, cardiovascular culprit lesions, organs, bone marrow, other sites of disease such as lymph nodes) identified in the Tumor/Lesion Identification (TU) domain. These measurements or qualitative assessments may be recorded at baseline and then at each subsequent assessment to support response evaluations. A typical record in the TR domain contains the following information: a unique tumor/lesion/location of interest ID value, test and result, method used, role of the individual making the assessment, and timing information.

Clinically accepted evaluation criteria expect that a tumor/lesion/location of interest identified by the ID is the same tumor/lesion/location of interest at each subsequent assessment. The TR domain does not include anatomical location information on each measurement/assessment record, because this would duplicate information represented in TU. The multi-domain approach to representing oncology assessment data was developed largely to reduce duplication of stored information.

1. TRLNKID is used to relate records in the TR domain to an identification record in TU domain. The organization of data across the TU and TR domains requires a RELREC relationship to link the related data rows. A dataset-to-dataset link would be the most appropriate linking mechanism. Utilizing 1 of the existing ID variables is not possible, because --GRPID, --REFID, and --SPID may be used for other purposes, per the SDTM. The --LNKID variable is used for values that support a RELREC dataset-to-dataset relationship and to provide a unique code for each identified tumor/lesion/location of interest.

2. TRLNKGRP is used to relate records in the TR domain to a response assessment record in the RS domain. The organization of data across the TR and RS domains requires a RELREC relationship to link the related data rows. A dataset-to-dataset link would be the most appropriate linking mechanism. Utilizing 1 of the existing ID variables is not possible because --GRPID, --REFID, and --SPID may be used for other purposes, per the SDTM. The --LNKGRP variable is used for values that support a RELREC dataset-to-dataset relationship and to provide a unique code for each response and associated tumor/lesion measurements/assessments.

3. TRTESTCD/TRTEST values for this domain are published as Controlled Terminology. For some TRTESTCD/TRTEST values, CDISC CT includes codelists for use with TRORRES. The associations between the test values and results are in the Oncology codetable, which, along with the Controlled Terminology Rules for Oncology, is available at https://www.cdisc.org/standards/terminology/controlled-terminology. The sponsor should not derive results for any test (e.g., percent change from nadir in sum of diameter) if the result was not collected. Tests would be included in the domain only if those data points have been collected on a CRF, presented by the CRF collection system, or supplied by an external assessor as part of an electronic data transfer. It is not intended that the sponsor would create derived records to supply those values in the TR domain. Derived records/results (outside the CRF) should be provided in the analysis dataset (ADaM).

4. In order to support data value standardization it is sometimes appropriate to standardize an original result value in TRORRES to a standardized result value in TRSTRESC and TRSTRESN. For example, in the published RECIST criteria, a standardized value of 5 mm is used in the calculation to determine response when a tumor is "too small to measure." The original or collected value "TOO SMALL TO MEASURE" should be represented in the TRORRES variable and the standardized value should be represented in the TRSTRESC and TRSTRESN variables. The information should be represented on a single row of data showing the standardization between the original result, TRORRES, and the standard results, TRSTRESC/TRSTRESN, as follows:

    | TRLNKID | TRTESTCD | TRTEST | TRORRES | TRORRESU | TRSTRESC | TRSTRESN | TRSTRESN |
    |---------|----------|--------|---------|----------|----------|----------|----------|
    | T01 | DIAMETER | Diameter | TOO SMALL TO MEASURE | mm | 5 | 5 | mm |

    **Note:** This is an exception to SDTMIG general variable rule 4.1.5.1, Original and Standardized Results of Findings and Tests Not Done.

5. The acceptance flag variable (TRACPTFL) identifies those records that have been determined to be the accepted assessments/measurements by an independent assessor. This flag would be provided by an independent assessor and when multiple assessors (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provide assessments or evaluations at the same time point or an overall evaluation. This flag should not be used by a sponsor for any other purpose. It is not expected that the TRACPTFL flag would be populated by the sponsor; instead, that type of record selection should be handled in the analysis dataset (ADaM).

6. The evaluator-specified variable (TREVALID) is used in conjunction with TREVAL to provide additional detail of who is providing measurements or assessments (e.g., TREVAL = "INDEPENDENT ASSESSOR", TREVALID = "RADIOLOGIST 1"). The TREVALID variable is subject to controlled terminology. **Note:** TREVAL must also be populated when TREVALID is populated.

7. When additional data are collected about a procedure (e.g., imaging procedure) from which tumor/lesion results are determined, the data about the procedure is stored in the PR domain and the link between the tumor/lesion results and the procedure should be recorded using RELREC.

8. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the TR domain, but the following qualifiers would not generally be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/TS/spec.md -->
# TS — Trial Summary

> Class: Trial Design | Structure: One record per trial summary parameter value

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

### TSSEQ
- **Order:** 3
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a parameter. Allows inclusion of multiple records for the same TSPARMCD.

### TSGRPID
- **Order:** 4
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a group of related records.

### TSPARMCD
- **Order:** 5
- **Label:** Trial Summary Parameter Short Name
- **Type:** Char
- **Controlled Terms:** C66738
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** TSPARMCD (the companion to TSPARM) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that TSPARMCD will need to serve as variable names. Examples: "AGEMIN", "AGEMAX".

### TSPARM
- **Order:** 6
- **Label:** Trial Summary Parameter
- **Type:** Char
- **Controlled Terms:** C67152
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Term for the trial summary parameter. The value in TSPARM cannot be longer than 40 characters. Examples: "Planned Minimum Age of Subjects", "Planned Maximum Age of Subjects".

### TSVAL
- **Order:** 7
- **Label:** Parameter Value
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Value of TSPARM. Example: "ASTHMA" when TSPARM value is "Trial Indication". TSVAL can only be null when TSVALNF is populated. Text over 200 characters can be added to additional columns TSVAL1-TSVALn. See Assumption 8.

### TSVALNF
- **Order:** 8
- **Label:** Parameter Value Null Flavor
- **Type:** Char
- **Controlled Terms:** ISO 21090 NullFlavor
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Null flavor for the value of TSPARM, to be populated only if TSVAL is null.

### TSVALCD
- **Order:** 9
- **Label:** Parameter Value Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** This is the code of the term in TSVAL. For example, "6CW7F3G59X" is the code for gabapentin; "C49488" is the code for Y. The length of this variable can be longer than 8 to accommodate the length of the external terminology.

### TSVCDREF
- **Order:** 10
- **Label:** Name of the Reference Terminology
- **Type:** Char
- **Controlled Terms:** C66788
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** The name of the reference terminology from which TSVALCD is taken. For example; CDISC CT, SNOMED, ISO 8601.

### TSVCDVER
- **Order:** 11
- **Label:** Version of the Reference Terminology
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** The version number of the reference terminology, if applicable.
---

## Cross References

### Controlled Terminology
- [Trial Summary Parameter Test Code (C66738)](../../terminology/core/trial_design.md) — TSPARMCD
- [Dictionary Name (C66788)](../../terminology/core/trial_design.md) — TSVCDREF
- [Trial Summary Parameter Test Name (C67152)](../../terminology/core/trial_design.md) — TSPARM

### Related Domains
- **Same class (Trial Design):** TA, TD, TE, TI, TM, TV

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

<!-- source: knowledge_base/domains/TS/assumptions.md -->
# TS — Assumptions

The Trial Summary (TS) dataset allows the sponsor to submit a summary of the trial in a structured format. Each record in the TS dataset contains the value of a parameter, a characteristic of the trial. For example, TS is used to record basic information about the study such as trial phase, protocol title, and trial objectives. The TS dataset contains information about the planned and actual trial characteristics.

1. The intent of this dataset is to provide a summary of trial information. This is not subject-level data.

2. Recipients may specify their requirements for which trial summary parameters should be included under which conditions. For example, the US FDA includes such information in their Study Data Technical Conformance Guide.

3. The order of parameters in the examples of TS datasets should not be taken as a requirement. There are no requirements or expectations about the order of parameters within the TS dataset.

4. The method for treating text >200 characters in TS is similar to that used for the Comments (CO) special-purpose domain (Section 5.1, Comments). If TSVAL is >200 characters, then it should be split into multiple variables, TSVAL-TSVALn. See Section 4.5.3.2, Text Strings Greater than 200 Characters in Other Variables.

5. A list of values for TSPARM and TSPARMCD can be found in CDISC Controlled Terminology, available at https://www.cancer.gov/research/resources/terminology/cdisc.

6. Controlled terminology for TSPARM is extensible. The meaning of any added parameters should be explained in the metadata for the TS dataset.

7. For a particular trial summary parameter, responses (values in TSVAL) may be numeric, datetimes or amounts of time represented in ISO8601 format, or text. For some parameters, textual responses may be taken from controlled terminology; for others, responses may be free text.

8. For some trial summary parameters, CDISC Controlled Terminology includes codelists for use with TSVAL. The associations between trial summary parameters and response codelists are in the TS codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology. Recipients may also specify controlled terminology for TSVAL. These specifications may be for trial summary parameters for which there is no CDISC Controlled Terminology or they may replace CDISC Controlled Terminology for a trial summary parameter. For example, the US FDA Data Standards Catalog includes terminologies to be used for certain trial summary parameters.

9. There is a code value for TSVALCD only when there is controlled terminology for TSVAL. For example, when TSPARMCD = "PLANSUB" (Planned Number of Subjects) or TSPARMCD = "TITLE" (Trial Title), then TSVALCD will be null.

10. TSVALNF contains a "null flavor," a value that provides additional coded information when TSVAL is null. For example, for TSPARM = "AGEMAX" (Planned Maximum Age of Subjects), there is no value if a study does not specify a maximum age. In this case, the appropriate null flavor is "PINF", which stands for "positive infinity." In a clinical pharmacology study conducted in healthy volunteers for a drug where indications are not yet established, the appropriate null flavor for TSPARM = "INDIC" (Trial Disease/Condition Indication) would be "NA" (i.e., not applicable). TSVALNF can also be used in a case where the value of a particular parameter is unknown.

11. Some codelists used for TSVAL include terms which are also null flavors. For example, the Pharmaceutical Dosage Form codelist includes the values "UNKNOWN" and "NOT APPLICABLE". In such cases, TSVAL should have the term from the codelist and TSVALNF should be null.

12. For some trials, there will be multiple records in the TS dataset for a single parameter. For example, a trial that addresses both safety and efficacy could have 2 records with TSPARMCD = "TTYPE" (Trial Type), one with the TSVAL = "SAFETY" and the other with TSVAL = "EFFICACY". TSSEQ has a different value for each record for the same parameter.

    Note that this is different from datasets that contain subject data, where the --SEQ variable has a different value for each record for the same subject.

13. TS does not contain subject-level data, so there is no restriction analogous to the requirement in subject-level datasets that the blocks bound by TSGRPID are within a subject. TSGRPID can be used to tie together any block of records in the TS dataset. TSGRPID is most likely to be used when the TS dataset includes multiple records for the same parameter.

    For example, if a trial compared administration of a total daily dose given once a day to that dose split over 2 administrations, the TS dataset might include the following records. There are 2 records each for TSPARMCD = "Dose" and TSPARMCD = "DOSFREQ". Records with the same TSGRPID are associated with each other. In this example, dose units are the same for both administration schedules, so only 1 record for DOSU is needed.

    | TSSEQ | TSGRPID | TSPARMCD | TSPARM | TSVAL |
    |-------|---------|----------|--------|-------|
    | 1 | A | DOSE | Dose per Administration | 50 |
    | 1 | A | DOSFREQ | Dosing Frequency | BID |
    | 2 | B | DOSE | Dose per Administration | 100 |
    | 2 | B | DOSFREQ | Dosing Frequency | Q24H |
    | 1 | | DOSU | Dose Units | mg |

14. Protocols vary in how they describe objectives. If the protocol does not provide information about which objectives meet the definition of TSPARM = "OBJPRIM" (Trial Primary Objective; i.e., the principal purpose of the trial), then the objectives should be provided as values of TSPARM = "OBJPRIM". Consult the controlled terminology for trial summary parameters for appropriate parameter values for representing other objective designations (e.g., secondary, exploratory).

15. As per the definitions, the primary outcome measure is associated with the primary objective, the secondary outcome measure is associated with the secondary objective, and the exploratory outcome measure is associated with the exploratory objective. It is possible for the same outcome measure to be associated with more than 1 objective. For example, 2 objectives could use the same outcome measure at different time points, or using different analysis methods.

16. If a primary objective is assessed by means of multiple outcome measures, then all of these outcome measures should be provided as values of TSPARM = "OUTMSPR" (Primary Outcome Measure). Similarly, all outcome measures used to assess secondary objectives should be provided as values of TSPARM = "OUTMSSEC" (Secondary Outcome Measure), and all outcome measures used to assess exploratory objectives should be provided as values of TSPARM = "OUTMSEXP" (Exploratory Outcome Measure). Additional key measures of a study that are not designated as primary, secondary, or exploratory should be provided as values of TSPARM = "OUTMSADD" (Additional Outcome Measure).

17. Trial indication: Values for TSVAL when TSPARMCD = "INDIC" would indicate the condition, disease, or disorder the trial is intended to investigate or address. A vaccine study of healthy subjects, with the intended purpose of preventing influenza infection, would have TSVAL = "Influenza". A clinical pharmacology study of healthy volunteers, with the purpose of collecting pharmacokinetic data, would have TSVAL be null and TSVALNF = "NA" if TS contains a row where TSPARMCD = "INDIC".

18. Values for TSVAL when TSPARMCD = "REGID" (Registry Identifier) will be identifiers assigned by the registry (e.g., ClinicalTrials.gov, EudraCT).

### Use of Null Flavor

The variable TSVALNF is based on the idea of a "null flavor" as embodied in the ISO 21090 standard. A null flavor is an ancillary piece of data that provides additional information when its primary piece of data is null (has a missing value). There is controlled terminology for the null flavor data item which includes such familiar values as "Unknown", "Other", and "Not Applicable" among its 14 terms.

The controlled terminology for null flavor, which supersedes Appendix C1, Supplemental Qualifiers Name Codes, is included below.

**NullFlavor Enumeration (OID: 2.16.840.1.113883.5.1008)**

| Rank | Code | Display Name | Definition |
|------|------|---|---|
| 1 | NI | No information | The value is exceptional (i.e., missing, omitted, incomplete, improper). No information as to the reason for being an exceptional value is provided. This is the most general exceptional value. It is also the default exceptional value. |
| 2 | INV | Invalid | The value as represented in the instance is not a member of the set of permitted data values in the constrained value domain of a variable. |
| 3 | OTH | Other | The actual value is not a member of the set of permitted data values in the constrained value domain of a variable (e.g., concept not provided by required code system). |
| 4 | PINF | Positive infinity | Positive infinity of numbers |
| 4 | NINF | Negative infinity | Negative infinity of numbers |
| 3 | UNC | Unencoded | No attempt has been made to encode the information correctly, but the raw source information is represented (usually in original Text). |
| 3 | DER | Derived | An actual value may exist, but it must be derived from the information provided (usually an expression is provided directly). |
| 2 | UNK | Unknown | A proper value is applicable, but not known. |
| 3 | ASKU | Asked but unknown | Information was sought but not found (e.g., patient was asked but didn't know). |
| 4 | NAV | Temporarily unavailable | Information is not available at this time, but is expected to be available later. |
| 3 | NASK | Not asked | This information has not been sought (e.g., patient was not asked). |
| 3 | QS | Sufficient quantity | The specific quantity is not known, but is known to be non-zero and is not specified because it makes up the bulk of the material. For example, if directions said, "Add 10 mg of ingredient X, 50 mg of ingredient Y, and sufficient quantity of water to 100 ml", the null flavor "QS" would be used to express the quantity of water. |
| 3 | TRC | Trace | The content is greater than zero, but too small to be quantified. |
| 2 | MSK | Masked | There is information on this item available, but it has not been provided by the sender due to security, privacy or other reasons. There may be an alternate mechanism for gaining access to this information. |

<!-- source: knowledge_base/domains/TU/spec.md -->
# TU — Tumor/Lesion Identification

> Class: Findings | Structure: One record per identified tumor per subject per assessor

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

### TUSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness within a dataset for a subject. May be any valid number.

### TUGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to link together a block of related records within a subject in a domain. Can be used to group split or merged tumors/lesions which have been identified.

### TUREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Internal or external identifier (e.g., medical image ID number).

### TUSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier.

### TULNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Exp
- **CDISC Notes:** Identifier used to link identified tumor/lesion/location of interest to the assessment results (in TR domain) over the course of the study.

### TULNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### TUTESTCD
- **Order:** 10
- **Label:** Tumor/Lesion ID Short Name
- **Type:** Char
- **Controlled Terms:** C96784
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the TEST in TUTEST. TUTESTCD cannot be longer than 8 characters nor can start with a number. TUTESTCD cannot contain characters other than letters, numbers, or underscores. Example: "TUMIDENT". See assumption 3.

### TUTEST
- **Order:** 11
- **Label:** Tumor/Lesion ID Test Name
- **Type:** Char
- **Controlled Terms:** C96783
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test for the tumor/lesion identification. The value in TUTEST cannot be longer than 40 characters. Example: "Tumor identification". See assumption 3.

### TUORRES
- **Order:** 12
- **Label:** Tumor/Lesion ID Result
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the tumor/lesion identification. The result of tumor/lesion identification is a classification of the identified tumor/lesion. Example: When TUTESTCD = "TUMIDENT", values of TUORRES might be "TARGET", "NON-TARGET", "NEW", or "BENIGN ABNORMALITY".

### TUSTRESC
- **Order:** 13
- **Label:** Tumor/Lesion ID Result Std. Format
- **Type:** Char
- **Controlled Terms:** C123650
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from TUORRES in a standard format.

### TUNAM
- **Order:** 14
- **Label:** Laboratory/Vendor Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** The name or identifier of the vendor that performed the tumor/lesion Identification. This column can be left null when the investigator provides the complete set of data in the domain.

### TULOC
- **Order:** 15
- **Label:** Location of the Tumor/Lesion
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Used to specify the anatomical location of the identified tumor/lesion (e.g., "LIVER").  Note: When anatomical location is broken down and collected as distinct pieces of data that when combined provide the overall location information (e.g., laterality/directionality/distribution), then additional anatomical location qualifiers should be used. See assumption 3.

### TULAT
- **Order:** 16
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality (e.g., "LEFT", "RIGHT", "BILATERAL").

### TUDIR
- **Order:** 17
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality (e.g., "UPPER", "INTERIOR").

### TUPORTOT
- **Order:** 18
- **Label:** Portion or Totality
- **Type:** Char
- **Controlled Terms:** C99075
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing the distribution, which means arrangement of, or apportioning of. Examples: "ENTIRE", "SINGLE", "SEGMENT", "MULTIPLE".

### TUMETHOD
- **Order:** 19
- **Label:** Method of Identification
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Method used to identify the tumor/lesion. Examples: "MRI", "CT SCAN".

### TULOBXFL
- **Order:** 20
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.

### TUBLFL
- **Order:** 21
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that TUBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### TUEVAL
- **Order:** 22
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Role of the person who provided the evaluation. Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR".  This column can be left null when the investigator provides the complete set of data in the domain. However, the column should contain no null values when data from 1 or more independent assessors is included. For example, the rows attributed to the investigator should contain a value of "INVESTIGATOR".

### TUEVALID
- **Order:** 23
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in --EVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2". See assumption 9.

### TUACPTFL
- **Order:** 24
- **Label:** Accepted Record Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** In cases where more than 1 independent assessor (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATION COMMITTEE") provide independent assessments at the same time point, this flag identifies the record that is considered to be the accepted assessment.

### VISITNUM
- **Order:** 25
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 26
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 27
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics. Should be an integer.

### TAETORD
- **Order:** 28
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the assessment was made.

### EPOCH
- **Order:** 29
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the assessment was made.

### TUDTC
- **Order:** 30
- **Label:** Date/Time of Tumor/Lesion Identification
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** TUDTC variable represents the date of the scan/image/physical exam. TUDTC does not represent the date that the image was read to identify tumors. TUDTC also does not represent the VISIT date.

### TUDY
- **Order:** 31
- **Label:** Study Day of Tumor/Lesion Identification
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of the scan/image/physical exam, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.
---

## Cross References

### Controlled Terminology
- [Tumor or Lesion Identification Test Results (C123650)](../../terminology/core/oncology_part2.md) — TUSTRESC
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — TULOBXFL, TUBLFL, TUACPTFL
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — TULOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — TUEVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — TUMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — TUEVALID
- [Tumor or Lesion Identification Test Name (C96783)](../../terminology/core/oncology_part2.md) — TUTEST
- [Tumor or Lesion Identification Test Code (C96784)](../../terminology/core/oncology_part2.md) — TUTESTCD
- [Laterality (C99073)](../../terminology/core/general_part2.md) — TULAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — TUDIR
- [Portion/Totality (C99075)](../../terminology/core/general_part4.md) — TUPORTOT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, UR, VS
- **Shared Dataset:** [TR](../TR/) — tumor identification → tumor results
- **Related Findings:** [RS](../RS/) — tumor identification → disease response

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/TU/assumptions.md -->
# TU — Assumptions

A findings domain that represents data that uniquely identifies tumors, lesions, or locations of interest under study. The TU domain represents data that uniquely identifies tumors, lesions, or locations of interest (e.g., tumors, cardiovascular culprit lesions, organs, bone marrow, other sites of disease such as lymph nodes). Commonly, tumors/lesions/locations of interest are identified by an investigator and/or independent assessor and classified according to the disease assessment criteria. For example, an oncology study using RECIST criteria would identify target, non-target, and new tumors.

1. The TU domain should contain only 1 record for each unique tumor/lesion/location of interest identified by an assessor (e.g., investigator, independent assessor) per medical evaluator. The initial identification of a tumor/lesion/location of interest is done once, usually at baseline (e.g., identification of target and non-target tumors/lesions) or first appearance of new tumor/lesion. The identification information, including the location description, must not be repeated for every visit. A record is required in TU to identify and create the TULNKID when there are associated records in TR with matching TRLNKID. The following are examples of when post-baseline records might be included in the TU domain:
    a. A new tumor/lesion may emerge at any time during a study; therefore, a new post-baseline record would represent the identification of the new tumor/lesion.
    b. If a tumor/lesion identified at baseline subsequently splits into separate distinct tumors/lesions, then additional post-baseline records can be included to distinctly identify the split tumors/lesions.
    c. In situations where a re-baseline of targets and non-targets is required (e.g., a cross-over study), then a separate set of target and non-target tumors/lesions might be identified and those identification records would be represented.

2. TRLNKID is used to relate an identification record in the TU domain to assessment records in the Tumor/Lesion Results (TR) domain. The organization of data across the TU and TR domains requires a linking mechanism. The TULNKID variable is used to provide a unique code for each identified tumor/lesion. The values of TULNKID are compound values that may carry the following information: an indication of the role (or assessor) providing the data record, when it is someone other than the principal investigator; an indication of whether the data record is for a target or non-target tumor/lesion; a tracking identifier or number; and an indication of whether the tumor/lesion has split (see assumption 3 for details on splitting). A RELREC relationship record can be created to describe the link, probably as a dataset-to-dataset link.

    TUTESTCD/TUTEST values for this domain are published as Controlled Terminology. For some TUTESTCD/TUTEST values, CDISC CT includes codelists for use with TUORRES. The associations between the test values and results are in the Oncology codetable, which, along with the CT Rules for Oncology, is available at https://www.cdisc.org/standards/terminology/controlled-terminology.

    During the course of a trial, a tumor/lesion identified at baseline might split into one or more distinct tumors/lesions, or 2 or more tumors/lesions might merge to form a single tumor/lesion. The following example shows the preferred approach for representing split lesions in TU. However, the approach depends on how the data for split and merged tumors/lesions are captured. The preferred approach requires the measurements of each distinct tumor/lesion to be captured individually.

    Example target tumor T04, identified at the screening visit, splits into 2 at week 16. Two new records are created with TUTEST = "Tumor Split"; TULNKID reflects the split by adding 0.1 and 0.2 to the original TULNKID value.

    | TULNKID | TUTESTCD | TUTEST | TUORRES | VISIT |
    |---------|----------|--------|---------|-------|
    | T01 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
    | T02 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
    | T03 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
    | T04 | TUMIDENT | Tumor Identification | TARGET | SCREEN |
    | NT01 | TUMIDENT | Tumor Identification | NON-TARGET | SCREEN |
    | NT02 | TUMIDENT | Tumor Identification | NON-TARGET | SCREEN |
    | T04.1 | TUSPLIT | Tumor Split | TARGET | WEEK 16 |
    | T04.2 | TUSPLIT | Tumor Split | TARGET | WEEK 16 |
    | NEW01 | TUMIDENT | Tumor Identification | NEW | WEEK 32 |

    If the data collection does not support this approach (i.e., measurements of split tumors/lesions are reported as a summary under the "parent" tumor/lesion), then it may not be possible to include a record in the TU domain. In this situation, the assessments of split and merge tumors/lesions would be represented only in the TR domain.

3. For some response criteria (e.g., Lugano, Kumar IMWG 2016), tumors are assessed by location of interest. A record is required in TU in order to link the assessments of the particular location of interest in TR. In TULNKID = "L01", the spleen is identified as a location of interest using computerized tomography (CT) scan. In TULNKID = "L04", the whole body is identified as a location of interest using positron emission tomography (PET) scan.

    | TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TUMETHOD |
    |---------|----------|--------|---------|-------|----------|
    | L01 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | SPLEEN | CT SCAN |
    | L02 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | LIVER | CT SCAN |
    | L03 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | BONE MARROW | PET SCAN |
    | L04 | TUMIDENT | Tumor Identification | LOCATION OF INTEREST | BODY | PET SCAN |

4. During the course of a trial, when a new tumor/lesion is identified, information about that new tumor/lesion may be collected to different levels of detail. For example, if anatomical location of a new tumor/lesion is not collected, TULOC will be blank. All new tumors/lesions are to be represented in TU and TR domains.

5. The additional anatomical location variables --LAT, --DIR, --PORTOT were added from the SDTM. These extra variables allow for more detailed information to be collected that further clarifies the value of the TULOC variable.

6. In the oncology setting, when a new tumor is identified, a record must be included in both the TU and TR domains. At a minimum, the TR record would contain TRLNKID = "NEW0" and TRTESTCD = "TUMSTATE" and TRORRES = "PRESENT" for unequivocal new tumors. The TU record may contain different levels of detail depending upon the data collection methods employed. Although it is possible that a sponsor may have a different chosen method, the following are the most common scenarios:
    a. The occurrence of a new tumor/lesion is the sole piece of information that a sponsor collects, because this is a sign of disease progression; no further details are required. In such cases, a record would be created where TUTEST = "Tumor Identification" and TUORRES = "NEW", and the identifier, TULNKID, would be populated in order to link to the associated information in the TR domain.
    b. The occurrence of a new tumor/lesion and the anatomical location of that newly identified tumor/lesion are the only collected pieces of information. In this case, it is expected that a record would be created where TUTEST = "Tumor Identification" and TUORRES = "NEW"; the TULOC variable would be populated with the anatomical location information (the additional location variables may be populated depending on the level of detail collected), and the identifier, TULNKID, would be populated in order to link to the associated information in the TR domain.
    c. The sponsor records the occurrence of a new tumor/lesion to the same level of detail as target tumors/lesions. For example, with the occurrence of a new tumor, its anatomical location and its measurement might be recorded. In this case, it is expected that a record would be created where TUTEST = "Tumor Identification" and TUORRES = "NEW". The TULOC variable would be populated with the anatomical location information (the additional location variables may be populated depending on the level of detail collected) and the identifier, TULNKID, would be populated in order to link to the associated information in the TR domain. In this scenario, measurements/assessments would also be recorded in the TR domain.

7. The acceptance flag variable (TUACPTFL) identifies records that have been determined to be the accepted assessments/measurements by an independent assessor. This flag would be provided by an independent assessor and when multiple evaluators (e.g., "RADIOLOGIST 1", "RADIOLOGIST 2", "ADJUDICATOR") provide assessments or evaluations at the same time point or an overall evaluation. This flag should not be used by a sponsor for any other purpose. It is not expected that the TUACPTFL flag would be populated by the sponsor; instead, that type of record selection should be handled in the analysis dataset (ADaM).

8. The evaluator-specified variable TUEVALID is used in conjunction with TUEVAL to provide additional detail regarding who is providing tumor identification information (e.g., TUEVAL = "INDEPENDENT ASSESSOR", TUEVALID = "RADIOLOGIST 1"). The TUEVALID variable is subject to controlled terminology. **Note:** TUEVAL must also be populated when TUEVALID is populated.

9. If indicator questions for specific types of tumor or lesions are collected (e.g., Does the subject have target tumors? Does the subject have any non-targets? Did the subject have metastatic disease at screening?), then these TUTESTs will be included in TU. If indicator questions are not collected, do not introduce them into TU.

    This example shows indicator TUTESTs for a subject with non-target lesions only.

    | TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TUMETHOD |
    |---------|----------|--------|---------|-------|----------|
    | | NTIND | Non-Target Indicator | Y | | CT SCAN |
    | | TIND | Target Indicator | N | | CT SCAN |
    | NT01 | TUMIDENT | Tumor Identification | NON-TARGET | LUNG | CT SCAN |

    This example shows indicator TUTESTs for the identification of the sites of metastatic disease sites at baseline.

    | TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTAT | TULOC | TUMETHOD | VISIT |
    |---------|----------|--------|---------|--------|-------|----------|-------|
    | | METIND | Metastatic Tumor Site Indicator | Y | | LIVER | CT SCAN | BASELINE |
    | | METIND | Metastatic Tumor Site Indicator | N | | BRAIN | MRI | BASELINE |
    | | METIND | Metastatic Tumor Site Indicator | NOT DONE | | PLEURAL CAVITY | | BASELINE |

10. Disease recurrence can be represented in the TU domain as an identification for the appearance of new tumors. The TUTEST Disease Recurrence Relative Location is used identify the region or relative location for the disease recurrence. The image identifier is in TUREFID and may match a PRREFID in the Procedures (PR) domain. The PR domain would contain the scans performed per protocol at each assessment; only when new tumors appear would records be included in TU.

    This example shows disease recurrence data in an adjuvant breast cancer study where the subject was initially diagnosed with cancer in the left breast only. This example shows a case where disease recurrence was identified in various locations. TUTEST=Disease Recurrence Relative Location is used to identify the reference location of the recurrence (e.g., LOCAL, REGIONAL, DISTANT, LOCOREGIONAL). A local disease recurrence was identified in the left breast, regional disease recurrence was identified in the ipsilateral internal mammary and the ipsilateral infraclavicular nodes, distant disease recurrence was identified in the liver and colon, and contralateral disease recurrence was identified in the right breast.

    | TUREFID | TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TULAT | TUMETHOD |
    |---------|---------|----------|--------|---------|-------|-------|----------|
    | IMG-00007 | LOC01 | DRCRLLTC | Disease Recurrence Relative Location | LOCAL | BREAST | LEFT | CT SCAN |
    | IMG-00007 | REG01 | DRCRLLTC | Disease Recurrence Relative Location | REGIONAL | INTERNAL MAMMARY LYMPH NODE | | CT SCAN |
    | IMG-00007 | REG02 | DRCRLLTC | Disease Recurrence Relative Location | REGIONAL | INFRACLAVICULAR LYMPH NODE | | CT SCAN |
    | IMG-00007 | DIS01 | DRCRLLTC | Disease Recurrence Relative Location | DISTANT | LIVER | | CT SCAN |
    | IMG-00007 | DIS02 | DRCRLLTC | Disease Recurrence Relative Location | DISTANT | COLON | | CT SCAN |
    | IMG-00007 | CON01 | DRCRLLTC | Disease Recurrence Relative Location | CONTRALATE RAL | BREAST | RIGHT | CT SCAN |

11. The following proposed supplemental qualifiers would be used for oncology studies to represent information regarding previous irradiation of a tumor when that information is captured in association with a specific tumor.

    | QNAM | QLABEL | Definition |
    |------|--------|------------|
    | TUPREVIR | Previously Irradiated | Indication of previous irradiation to a tumor |
    | TUPREISP | Irradiated then Subsequent Progression | Indication of documented progression subsequent to irradiation |

12. When additional data are collected about a procedure used for tumor/lesion identification, the data about the procedure are stored in the PR domain; the link between the tumor/lesion identification and the procedure should be recorded using RELREC.

13. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the TU domain, but the following qualifiers would not generally be used: --MODIFY, --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV.

<!-- source: knowledge_base/domains/TV/spec.md -->
# TV — Trial Visits

> Class: Trial Design | Structure: One record per planned Visit per Arm

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

### VISITNUM
- **Order:** 3
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 4
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Description of clinical encounter. This is often defined in the protocol. Used in addition to VISITNUM and/or VISITDY as a text description of the clinical encounter.

### VISITDY
- **Order:** 5
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Due to its sequential nature, used for sorting.

### ARMCD
- **Order:** 6
- **Label:** Planned Arm Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** 1. ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20.  2. If the timing of visits for a trial does not depend on which arm a subject is in, then ARMCD should be null.

### ARM
- **Order:** 7
- **Label:** Description of Planned Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** 1. Name given to an arm or treatment group.  2. If the timing of visits for a trial does not depend on which arm a subject is in, then Arm should be left blank.

### TVSTRL
- **Order:** 8
- **Label:** Visit Start Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Req
- **CDISC Notes:** Rule describing when the visit starts, in relation to the sequence of elements.

### TVENRL
- **Order:** 9
- **Label:** Visit End Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Perm
- **CDISC Notes:** Rule describing when the visit ends, in relation to the sequence of elements.
---

## Cross References

### Related Domains
- **Same class (Trial Design):** TA, TD, TE, TI, TM, TS
- **Trial Design:** [TA](../TA/) — visits reference arms
- **Trial Design:** [SE](../SE/) — planned visits vs actual subject elements

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

<!-- source: knowledge_base/domains/TV/assumptions.md -->
# TV — Assumptions

1. Although the general structure of the Trial Visits (TV) dataset is "One Record per Planned Visit per Arm," for many clinical trials—particularly blinded clinical trials—the schedule of visits is the same for all arms, and the structure of the TV dataset will be "One Record per Planned Visit." If the schedule of visits is the same for all arms, ARMCD should be left blank for all records in the TV dataset. For trials with trial visits that are different for different arms (e.g., Example Trial 7 in Section 7.2.1, Trial Arms), ARMCD and ARM should be populated for all records. If some visits are the same for all arms, and some visits differ by arm, then ARMCD and ARM should be populated for all records, to ensure clarity, even though this will mean creating near-duplicate records for visits that are the same for all arms.

2. A visit may start in one element and end in another. This means that a visit may start in one epoch and end in another. For example, if one of the activities planned for a visit is the administration of the first dose of study drug, the visit might start in the screen epoch and end in a treatment epoch.

3. TVSTRL describes the scheduling of the visit and should reflect the wording in the protocol. In many trials, all visits are scheduled relative to the study's day 1 (RFSTDTC). In such trials, it is useful to include VISITDY, which is, in effect, a special case representation of TVSTRL.

4. Note that there is a subtle difference between the following 2 examples. In the first case, if visit 3 were delayed for some reason, visit 4 would be unaffected. In the second case, a delay to visit 3 would result in visit 4 being delayed as well.
    a. Case 1: Visit 3 starts 2 weeks after RFSTDTC. Visit 4 starts 4 weeks after RFSTDTC.
    b. Case 2: Visit 3 starts 2 weeks after RFSTDTC. Visit 4 starts 2 weeks after visit 3.

5. Many protocols do not give any information about visit end times because visits are assumed to end on the same day they start. In such a case, TVENRL may be left blank to indicate that the visit ends on the same day it starts. Care should be taken to assure that this is appropriate; common practice may be to record data collected over more than 1 day as occurring within a single visit. Screening visits may be particularly prone to collection of data over multiple days. The examples for this domain show how TVENRL could be populated.

6. The values of VISITNUM in the TV dataset are the valid values of VISITNUM for planned visits. Any values of VISITNUM that appear in subject-level datasets that are not in the TV dataset are assumed to correspond to unplanned visits. This applies, in particular, to the subject-level dataset; see Section 5.5, Subject Visits, for additional information about handling unplanned visits. If a subject-level dataset includes both VISITNUM and VISIT, then records that include values of VISITNUM that appear in the TV dataset should also include the corresponding values of VISIT from the TV dataset.

<!-- source: knowledge_base/domains/UR/spec.md -->
# UR — Urinary System Findings

> Class: Findings | Structure: One record per finding per location per per visit per subject

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

### URSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number to ensure uniqueness of records within a dataset for a subject. May be any valid number (including decimals) and does not have to start at 1.

### URGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional group identifier, used to link together a block of related records within a subject in a domain.

### URREFID
- **Order:** 6
- **Label:** Reference ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Optional internal or external identifier (e.g., lab specimen ID, universally unique identifier (UUID) for a medical image).

### URSPID
- **Order:** 7
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined identifier. Example: Preprinted line identifier.

### URLNKID
- **Order:** 8
- **Label:** Link ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This may be a one-to-one or a one-to-many relationship.

### URLNKGRP
- **Order:** 9
- **Label:** Link Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Identifier used to link related records across domains. This will usually be a many-to-one relationship.

### URTESTCD
- **Order:** 10
- **Label:** Short Name of Urinary Test
- **Type:** Char
- **Controlled Terms:** C129942
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short character value for URTEST used as a column name when converting a dataset from a vertical format to a horizontal format. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in URTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). URTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "COUNT", "LENGTH", "RBLDFLW".

### URTEST
- **Order:** 11
- **Label:** Name of Urinary Test
- **Type:** Char
- **Controlled Terms:** C129941
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Long name For URTESTCD. Examples: "Count", "Length", "Renal Blood Flow".

### URTSTDTL
- **Order:** 12
- **Label:** Urinary Test Detail
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Further description of URTESTCD and URTEST.

### URCAT
- **Order:** 13
- **Label:** Category for Urinary Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of topic-variable values.

### URSCAT
- **Order:** 14
- **Label:** Subcategory for Urinary Test
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a further categorization of URCAT values.

### URORRES
- **Order:** 15
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the measurement or finding as originally received or collected.

### URORRESU
- **Order:** 16
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Unit for URORRES.

### URSTRESC
- **Order:** 17
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings copied or derived from URORRES, in a standard format or in standard units. URSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in URSTRESN.

### URSTRESN
- **Order:** 18
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from URSTRESC. URSTRESN should store all numeric test results or findings.

### URSTRESU
- **Order:** 19
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C71620
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Standardized units used for URSTRESC and URSTRESN.

### URRESCAT
- **Order:** 20
- **Label:** Result Category
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to categorize the result of a finding.

### URSTAT
- **Order:** 21
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a question was not asked or a test was not done, or a test was attempted but did not generate a result. Should be null or have a value of "NOT DONE".

### URREASND
- **Order:** 22
- **Label:** Reason Not Done
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Reason not done. Used in conjunction with URSTAT when value is "NOT DONE".

### URLOC
- **Order:** 23
- **Label:** Location Used for the Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Anatomical location of the subject relevant to the collection of the measurement.

### URLAT
- **Order:** 24
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### URDIR
- **Order:** 25
- **Label:** Directionality
- **Type:** Char
- **Controlled Terms:** C99074
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing directionality. Examples: "ANTERIOR", "LOWER", "PROXIMAL".

### URMETHOD
- **Order:** 26
- **Label:** Method of Test or Examination
- **Type:** Char
- **Controlled Terms:** C85492
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Method of the test or examination.

### URLOBXFL
- **Order:** 27
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null.

### URBLFL
- **Order:** 28
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** A baseline defined by the sponsor The value should be "Y" or null. Note that URBLFL is retained for backward compatibility. The authoritative baseline flag for statistical analysis is in an ADaM dataset.

### URDRVFL
- **Order:** 29
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record (e.g., a record that represents the average of other records such as a computed baseline). Should be "Y" or null.

### UREVAL
- **Order:** 30
- **Label:** Evaluator
- **Type:** Char
- **Controlled Terms:** C78735
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Role of the person who provided the evaluation. Used only for results that are subjective (e.g., assigned by a person or a group). Examples: "ADJUDICATION COMMITTEE", "INDEPENDENT ASSESSOR", "RADIOLOGIST".

### UREVALID
- **Order:** 31
- **Label:** Evaluator Identifier
- **Type:** Char
- **Controlled Terms:** C96777
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to distinguish multiple evaluators with the same role recorded in UREVAL. Examples: "RADIOLOGIST1", "RADIOLOGIST2".

### VISITNUM
- **Order:** 32
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 33
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of a clinical encounter.

### VISITDY
- **Order:** 34
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Should be an integer.

### TAETORD
- **Order:** 35
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Number that gives the planned order of the element within the arm for the element in which the observation was made.

### EPOCH
- **Order:** 36
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Epoch associated with the date/time at which the observation was made.

### URDTC
- **Order:** 37
- **Label:** Date/Time of Collection
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Collection date and time of an observation.

### URDY
- **Order:** 38
- **Label:** Study Day of Visit/Collection/Exam
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics.

### URTPT
- **Order:** 39
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when a measurement or observation should be taken as defined in the protocol. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See URTPTNUM and URTPTREF.

### URTPTNUM
- **Order:** 40
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numeric version of planned time point used in sorting.

### URELTM
- **Order:** 41
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time relative to a planned fixed reference (URTPTREF; e.g., "PREVIOUS DOSE", "PREVIOUS MEAL"). This variable is useful where there are repetitive measures. Not a clock time or a date/time variable, but an interval, represented as ISO duration.

### URTPTREF
- **Order:** 42
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Description of the fixed reference point referred to by URELTM, URTPTNUM, and URTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### URRFTDTC
- **Order:** 43
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time for a fixed reference time point defined by URTPTREF.
---

## Cross References

### Controlled Terminology
- [Urinary System Test Name (C129941)](../../terminology/core/other_part5.md) — URTEST
- [Urinary System Test Code (C129942)](../../terminology/core/other_part5.md) — URTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — URLOBXFL, URBLFL, URDRVFL
- [Not Done (C66789)](../../terminology/core/general_part4.md) — URSTAT
- [Unit (C71620)](../../terminology/core/general_part5.md) — URORRESU, URSTRESU
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — URLOC
- [Evaluator (C78735)](../../terminology/core/general_part2.md) — UREVAL
- [Method (C85492)](../../terminology/core/general_part3.md) — URMETHOD
- [Medical Evaluator Identifier (C96777)](../../terminology/core/general_part2.md) — UREVALID
- [Laterality (C99073)](../../terminology/core/general_part2.md) — URLAT
- [Directionality (C99074)](../../terminology/core/general_part2.md) — URDIR
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, VS

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/UR/assumptions.md -->
# UR — Assumptions

1. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the UR domain, but the following qualifiers would not generally be used: --MODIFY, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --NRIND, --LOINC, --SPCCND, --FAST, --TOX, --TOXGR, --SEV, --LLOQ.

<!-- source: knowledge_base/domains/VS/spec.md -->
# VS — Vital Signs

> Class: Findings | Structure: One record per vital sign measurement per time point per visit per subject

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

### VSSEQ
- **Order:** 4
- **Label:** Sequence Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number.

### VSGRPID
- **Order:** 5
- **Label:** Group ID
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Used to tie together a block of related records in a single domain for a subject.

### VSSPID
- **Order:** 6
- **Label:** Sponsor-Defined Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Perm
- **CDISC Notes:** Sponsor-defined reference number. May be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database.

### VSTESTCD
- **Order:** 7
- **Label:** Vital Signs Test Short Name
- **Type:** Char
- **Controlled Terms:** C66741
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Short name of the measurement, test, or examination described in VSTEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in VSTESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST" is not valid). VSTESTCD cannot contain characters other than letters, numbers, or underscores. Examples: "SYSBP", "DIABP", "BMI".

### VSTEST
- **Order:** 8
- **Label:** Vital Signs Test Name
- **Type:** Char
- **Controlled Terms:** C67153
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Verbatim name of the test or examination used to obtain the measurement or finding. The value in VSTEST cannot be longer than 40 characters. Examples: "Systolic Blood Pressure", "Diastolic Blood Pressure", "Body Mass Index".

### VSCAT
- **Order:** 9
- **Label:** Category for Vital Signs
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to define a category of related records.

### VSSCAT
- **Order:** 10
- **Label:** Subcategory for Vital Signs
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Grouping Qualifier
- **Core:** Perm
- **CDISC Notes:** A further categorization of a measurement or examination.

### VSPOS
- **Order:** 11
- **Label:** Vital Signs Position of Subject
- **Type:** Char
- **Controlled Terms:** C71148
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Position of the subject during a measurement or examination. Examples: "SUPINE", "STANDING", "SITTING".

### VSORRES
- **Order:** 12
- **Label:** Result or Finding in Original Units
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Result of the vital signs measurement as originally received or collected.

### VSORRESU
- **Order:** 13
- **Label:** Original Units
- **Type:** Char
- **Controlled Terms:** C66770
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Original units in which the data were collected. The unit for VSORRES. Examples: "in", "LB", "beats/min".

### VSSTRESC
- **Order:** 14
- **Label:** Character Result/Finding in Std Format
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Contains the result value for all findings, copied or derived from VSORRES in a standard format or standard units. VSSTRESC should store all results or findings in character format; if results are numeric, they should also be stored in numeric format in VSSTRESN. For example, if a test has results "NONE", "NEG", and "NEGATIVE" in VSORRES, and these results effectively have the same meaning, they could be represented in standard format in VSSTRESC as "NEGATIVE".

### VSSTRESN
- **Order:** 15
- **Label:** Numeric Result/Finding in Standard Units
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Result Qualifier
- **Core:** Exp
- **CDISC Notes:** Used for continuous or numeric results or findings in standard format; copied in numeric format from VSSTRESC. VSSTRESN should store all numeric test results or findings.

### VSSTRESU
- **Order:** 16
- **Label:** Standard Units
- **Type:** Char
- **Controlled Terms:** C66770
- **Role:** Variable Qualifier
- **Core:** Exp
- **CDISC Notes:** Standardized unit used for VSSTRESC and VSSTRESN.

### VSSTAT
- **Order:** 17
- **Label:** Completion Status
- **Type:** Char
- **Controlled Terms:** C66789
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate that a vital sign measurement was not done. Should be null if a result exists in VSORRES.

### VSREASND
- **Order:** 18
- **Label:** Reason Not Performed
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Describes why a measurement or test was not performed. Examples: "BROKEN EQUIPMENT", "SUBJECT REFUSED". Used in conjunction with VSSTAT when value is "NOT DONE".

### VSLOC
- **Order:** 19
- **Label:** Location of Vital Signs Measurement
- **Type:** Char
- **Controlled Terms:** C74456
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Location relevant to the collection of vital signs measurement. Example: "ARM" for blood pressure.

### VSLAT
- **Order:** 20
- **Label:** Laterality
- **Type:** Char
- **Controlled Terms:** C99073
- **Role:** Result Qualifier
- **Core:** Perm
- **CDISC Notes:** Qualifier for anatomical location or specimen further detailing laterality. Examples: "RIGHT", "LEFT", "BILATERAL".

### VSLOBXFL
- **Order:** 21
- **Label:** Last Observation Before Exposure Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. Should be "Y" or null.

### VSBLFL
- **Order:** 22
- **Label:** Baseline Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Indicator used to identify a baseline value. Should be "Y" or null. Note that VSBLFL is retained for backward compatibility. The authoritative baseline for statistical analysis is in an ADaM dataset.

### VSDRVFL
- **Order:** 23
- **Label:** Derived Flag
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate a derived record. The value should be "Y" or null. Records that represent the average of other records or that do not come from the CRF are examples of records that would be derived for the submission datasets. If VSDRVFL = "Y," then VSORRES may be null, with VSSTRESC and (if numeric) VSSTRESN having the derived value.

### VSTOX
- **Order:** 24
- **Label:** Toxicity
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Variable Qualifier
- **Core:** Perm
- **CDISC Notes:** Description of toxicity quantified by VSTOXGR. The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.

### VSTOXGR
- **Order:** 25
- **Label:** Standard Toxicity Grade
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Records toxicity grade value using a standard toxicity scale (e.g., NCI CTCAE). If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). The sponsor is expected to provide the name of the scale and version used to map the terms, utilizing the external codelist element in the Define-XML document.

### VSCLSIG
- **Order:** 26
- **Label:** Clinically Significant, Collected
- **Type:** Char
- **Controlled Terms:** C66742
- **Role:** Record Qualifier
- **Core:** Perm
- **CDISC Notes:** Used to indicate whether a collected observation is clinically significant based on judgment.

### VISITNUM
- **Order:** 27
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 28
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.

### VISITDY
- **Order:** 29
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of the visit based upon RFSTDTC in Demographics.

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
- **CDISC Notes:** Epoch associated with the start date/time at which the assessment was made.

### VSDTC
- **Order:** 32
- **Label:** Date/Time of Measurements
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Exp
- **CDISC Notes:** Date and time of the vital signs assessment represented in ISO 8601 character format.

### VSDY
- **Order:** 33
- **Label:** Study Day of Vital Signs
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Study day of vital signs measurements, measured as integer days. Algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in Demographics.

### VSTPT
- **Order:** 34
- **Label:** Planned Time Point Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Text description of time when measurement should be taken. This may be represented as an elapsed time relative to a fixed reference point (e.g., time of last dose). See VSTPTNUM and VSTPTREF. Examples: "START", "5 MIN POST".

### VSTPTNUM
- **Order:** 35
- **Label:** Planned Time Point Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Numerical version of VSTPT to aid in sorting.

### VSELTM
- **Order:** 36
- **Label:** Planned Elapsed Time from Time Point Ref
- **Type:** Char
- **Controlled Terms:** ISO 8601 duration
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned elapsed time (in ISO 8601) relative to a planned fixed reference (VSTPTREF). This variable is useful where there are repetitive measures. Not a clock time or a date time variable. Represented as an ISO 8601 Duration. Examples: "-PT15M" to represent the period of 15 minutes prior to the reference point indicated by VSTPTREF, "PT8H" to represent the period of 8 hours after the reference point indicated by VSTPTREF.

### VSTPTREF
- **Order:** 37
- **Label:** Time Point Reference
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Name of the fixed reference point referred to by VSELTM, VSTPTNUM, and VSTPT. Examples: "PREVIOUS DOSE", "PREVIOUS MEAL".

### VSRFTDTC
- **Order:** 38
- **Label:** Date/Time of Reference Time Point
- **Type:** Char
- **Controlled Terms:** ISO 8601 datetime or interval
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Date/time of the reference time point, VSTPTREF.
---

## Cross References

### Controlled Terminology
- [Vital Signs Test Code (C66741)](../../terminology/core/vs.md) — VSTESTCD
- [No Yes Response (C66742)](../../terminology/core/general_part4.md) — VSLOBXFL, VSBLFL, VSDRVFL, VSCLSIG
- [Units for Vital Signs Results (C66770)](../../terminology/core/vs.md) — VSORRESU, VSSTRESU
- [Not Done (C66789)](../../terminology/core/general_part4.md) — VSSTAT
- [Vital Signs Test Name (C67153)](../../terminology/core/vs.md) — VSTEST
- [Position (C71148)](../../terminology/core/interventions.md) — VSPOS
- [Anatomical Location (C74456)](../../terminology/core/general_part1.md) — VSLOC
- [Laterality (C99073)](../../terminology/core/general_part2.md) — VSLAT
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Findings):** BS, CP, CV, DA, DD, EG, FT, GF, IE, IS, LB, MB, MI, MK, MS, NV, OE, PC, PE, PP, QS, RE, RP, RS, SC, SS, TR, TU, UR

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Findings class definition](../../model/02_observation_classes.md)

<!-- source: knowledge_base/domains/VS/assumptions.md -->
# VS — Assumptions

1. In cases where the LOINC dictionary is used for vital sign tests, the permissible variable VSLOINC may be used. Sponsors are expected to provide the dictionary name and version used to map terms using the external codelist element in the Define-XML document.

2. If a reference range is available for a vital signs test, the variables VSORNRLO, VSORNRHI, VSNRIND from the Findings observation class may be added to the domain. VSORNRLO and VSORNRHI would represent the reference range, and VSNRIND would be used to indicate where a result falls with respect to the reference range (e.g., "HIGH", "LOW"). If toxicity grading is available, values would be represented in the variables VSTOX and VSTOXGR. Clinical significance would be represented in VSCLSIG, as described in Section 4.5.5, Clinical Significance for Findings Observation Class Data.

3. Associations between some vital sign tests and qualifier codelists are described in the VS codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

4. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the VS domain, but the following qualifiers would not generally be used: --BODSYS, --XFN, --SPEC, --SPCCND, --FAST.

