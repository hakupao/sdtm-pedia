# 08_ev_adverse_ae

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `08`
> - **Concept**: Events: AE (单独 — 重要域, 单独 slot 提高精度)
> - **Merged files**: 3
> - **Words**: 7,354
> - **Chars**: 46,527
> - **Sources**:
>   - `domains/AE/spec.md`
>   - `domains/AE/assumptions.md`
>   - `domains/AE/examples.md`

---
## Source: `domains/AE/spec.md`

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

## Source: `domains/AE/assumptions.md`

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

## Source: `domains/AE/examples.md`

# AE — Examples

## Example 1

This example illustrates data from an AE CRF that collected AE terms as free text. AEs were coded using MedDRA, and the sponsor's procedures include the possibility of modifying the reported term to aid in coding. The CRF was structured so that seriousness category variables (e.g., AESDTH, AESHOSP) were checked only when AESER is answered "Y." In this study, the study reference period started at the start of study treatment. Three AEs were reported for this subject.

**Rows 1-2:** Show examples of modifying the reported term for coding purposes, with the modified term in AEMODIFY. These adverse events were not serious, so the seriousness criteria variables are null. Note that for the event in row 2, AESTDY = "1". Day 1 was the day treatment started; the AE start and end times, as well as dates, were collected to allow comparison of the AE timing to the start of treatment.

**Row 3:** Shows an example of the overall seriousness question AESER answered with "Y" and the relevant corresponding seriousness category variables (AESHOSP and AESLIFE) answered "Y". The other seriousness category variables are left blank. This row also shows AEENRF being populated because the AE was marked as "Continuing" as of the end of the study reference period for the subject (see Section 4.4.7, Use of Relative Timing Variables).

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEMODIFY | AEDECOD | AEBODSYS | AESEV | AESER | AEACN | AEREL | AEOUT | AESCONG | AESDISAB | AESDTH | AESHOSP | AESLIFE | AESMIE | EPOCH | AESTDTC | AEENDTC | AESTDY | AEENDY | AEENRF |
|-----|---------|--------|---------|-------|--------|----------|---------|----------|-------|-------|-------|-------|-------|---------|----------|--------|---------|---------|--------|-------|---------|---------|--------|--------|--------|
| 1 | ABC123 | AE | 123101 | 1 | POUNDING HEADACHE | Headache | Headache | Nervous system disorders | SEVERE | N | | NOT APPLICABLE | DEFINITELY NOT RELATED | RECOVERED/RESOLVED | | | | | | SCREENING | 2005-10-12 | 2005-10-12 | -1 | -1 | |
| 2 | ABC123 | AE | 123101 | 2 | BACK PAIN FOR 5 HOURS | Back pain | Back pain | Musculoskeletal and connective tissue disorders | MODERATE | N | DOSE REDUCED | RELATED | PROBABLY RELATED | RECOVERED/RESOLVED | | | | | | TREATMENT | 2005-10-13T13:05 | 2005-10-13T19:00 | 1 | 1 | |
| 3 | ABC123 | AE | 123101 | 3 | PULMONARY EMBOLISM | | Pulmonary embolism | Vascular disorders | MODERATE | Y | DOSE REDUCED | PROBABLY NOT RELATED | RECOVERING/RESOLVING | | | | Y | Y | | TREATMENT | 2005-10-21 | | 9 | | AFTER TREATMENT |

## Example 2

In this example, a CRF module included at several visits asked whether nausea, vomiting, or diarrhea occurred. The responses to the probing questions "Yes", "No", or "Not Done" were represented in the Findings About (FA) domain (see Section 6.4, Findings About Events and Interventions). If "Yes", the investigator was instructed to complete the AE CRF. In the AE dataset, data on AEs solicited by prespecification on the CRF have an AEPRESP value of "Y". For AEs solicited by a general question, AEPRESP is null. RELREC may be used to relate AE records and FA records.

**Rows 1-2:** Show that nausea and vomiting were prespecified on a CRF, as indicated by AEPRESP = "Y". The subject did not experience diarrhea, so no record for that term exists in the AE dataset.

**Row 3:** Shows an example of an AE (headache) that was not prespecified on a CRF, as indicated by a null value for AEPRESP.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEDECOD | AEPRESP | AEBODSYS | AESEV | AESER | AEACN | AEREL | AEOUT | EPOCH | AESTDTC | AEENDTC | AESTDY | AEENDY |
|-----|---------|--------|---------|-------|--------|---------|---------|----------|-------|-------|-------|-------|-------|-------|---------|---------|--------|--------|
| 1 | ABC123 | AE | 123101 | 1 | NAUSEA | Nausea | Y | Gastrointestinal disorders | SEVERE | N | DOSE REDUCED | RELATED | RECOVERED/RESOLVED | TREATMENT | 2005-10-12 | 2005-10-13 | 2 | 3 |
| 2 | ABC123 | AE | 123101 | 2 | VOMITING | Vomiting | Y | Gastrointestinal disorders | MODERATE | N | DOSE REDUCED | RELATED | RECOVERED/RESOLVED | TREATMENT | 2005-10-13T13:05 | 2005-10-13T19:00 | 3 | 3 |
| 3 | ABC123 | AE | 123101 | 3 | HEADACHE | Headache | | Nervous system disorders | MILD | N | DOSE NOT CHANGED | POSSIBLY RELATED | RECOVERED/RESOLVED | TREATMENT | 2005-10-21 | | 11 | 11 |

## Example 3

In this example, a CRF module that asked whether or not nausea, vomiting, or diarrhea occurred was included in the study only once. In the context of this study, the conditions that occurred were reportable as adverse events. No additional data about these events was collected. No other AE information was collected via general questions. The responses to the probing questions "Yes", "No", or "Not Done" were represented in the FA domain (see Section 6.4, Findings About Events and Interventions). This is an example of unusually sparse AE data collection; the AE dataset is populated with the term and the flag indicating that it was prespecified, but timing information is limited to the date of collection, and other expected qualifiers are not available. RELREC may be used to relate AE records and FA records.

The subject shown in this example experienced nausea and vomiting. The subject did not experience diarrhea, so no record for that term exists in the AE dataset.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEDECOD | AEPRESP | AEBODSYS | AESER | AEDTC | AESTDY |
|-----|---------|--------|---------|-------|--------|---------|---------|----------|-------|-------|--------|
| 1 | ABC123 | AE | 123101 | 1 | NAUSEA | Nausea | Y | Gastrointestinal disorders | | 2005-10-29 | 19 |
| 2 | ABC123 | AE | 123101 | 2 | VOMITING | Vomiting | Y | Gastrointestinal disorders | | 2005-10-29 | 19 |

## Example 4

In this example, the investigator was instructed to create a new AE record each time the severity of an adverse event changed. The sponsor used AEGRPID to identify the group of records related to a single event for a subject.

**Row 1:** Shows an adverse event of nausea, for which severity was moderate.

**Rows 2-4:** Show AEGRPID used to group records related to a single event of "VOMITING".

**Rows 5-6:** Show AEGRPID used to group records related to a single event of "DIARRHEA".

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AEGRPID | AETERM | AEBODSYS | AESEV | AESER | AEACN | AEREL | AESTDTC | AEENDTC |
|-----|---------|--------|---------|-------|---------|--------|----------|-------|-------|-------|-------|---------|---------|
| 1 | ABC123 | AE | 123101 | 1 | | NAUSEA | Gastrointestinal disorders | MODERATE | N | DOSE NOT CHANGED | RELATED | 2005-10-13 | 2005-10-14 |
| 2 | ABC123 | AE | 123101 | 2 | 1 | VOMITING | Gastrointestinal disorders | MILD | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-14 | 2005-10-15 |
| 3 | ABC123 | AE | 123101 | 3 | 1 | VOMITING | Gastrointestinal disorders | SEVERE | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-16 | 2005-10-17 |
| 4 | ABC123 | AE | 123101 | 4 | 1 | VOMITING | Gastrointestinal disorders | MILD | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-17 | 2005-10-20 |
| 5 | ABC123 | AE | 123101 | 5 | 2 | DIARRHEA | Gastrointestinal disorders | SEVERE | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-16 | 2005-10-17 |
| 6 | ABC123 | AE | 123101 | 6 | 2 | DIARRHEA | Gastrointestinal disorders | MODERATE | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-17 | 2005-10-21 |

## Example 5

This study was evaluating artificial hip joints made of a novel material. The protocol specified that only 1 hip could be replaced in a subject, and that subjects should be encouraged to begin walking within 2 days after surgery. This subject was walking on day 5 and tripped and sprained her left ankle. A few days later, she developed an infection in the hip bone adjacent to the implant. The implant was removed and replaced by a different product. She never regained full use of her hip, and was left with a limp. This example shows the use of the device-related variables indicating if the AE was related to the procedure that implanted the device rather than the device itself (AERLPRC), or if it was related to some other procedure or activity required by the protocol (AERLPRT). These are used to determine if the AE was an unanticipated serious device event, a designation required by some regulatory authorities. Device Identifiers (DI) and other related device domains have not been modeled here; for more information about device domains, see the SDTMIG-MD (https://www.cdisc.org/standards/foundational/medical-devices).

**Row 1:** Shows an AE of "Twisted left ankle". The location and laterality are specified as it may be important to know if it occurred on the same or opposite side of the body.

**Row 2:** Shows an AE of "Osteomyelitis right hip". The location and laterality is specified and it is considered a serious adverse event. The device was removed as the AE was probably related to the device.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | AESEQ | AESPID | AETERM | AEDECOD | AELOC | AELAT | AESER | AESEV | AEACNDEV | AERELDEV | AERLPRC | AEREL | AEOUT | AESCONG | AESDISAB | AESDTH | AESHOSP | AESLIFE | AESMIE | AEUNANT | AERLPRT | AESTDTC | AEENDTC | AESTDY | AEENDY |
|-----|---------|--------|---------|---------|-------|--------|--------|---------|-------|-------|-------|-------|----------|----------|---------|-------|-------|---------|----------|--------|---------|---------|--------|---------|---------|---------|---------|--------|--------|
| 1 | T992 | AE | 002 | HipX22 | 1 | AE0099 | Twisted left ankle | ANKLE JOINT SPRAIN | | LEFT | N | MILD | NONE | NOT RELATED | RECOVERED/RESOLVED | N | N | N | N | N | N | Y | | 2015-04-14 | 2015-04-16 | 10 | |
| 2 | T992 | AE | 002 | HipX22 | 2 | AE0033 | Osteomyelitis right hip | OSTEOMYELITIS | HIP | RIGHT | Y | MODERATE | REMOVED | PROBABLE | RECOVERING/RESOLVING | N | Y | N | Y | Y | N | N | | 2015-05-01 | | 15 | 25 |

## Example 6

This study was testing an implanted cardiac pacemaker that was paired with a transmitting sensor that was attached to the participant's skin. The sensor picked up transmitted measurements from the pacemaker and relayed them to a cell network and then to the subject's and investigator's smart phones. The devices were the focus of the study. The DI domain and other related device domains have not been modeled here; for further information about the device domains, see the SDTMIG-MD.

**Row 1:** Shows the use of the variables for the relationship of the device to the AE (AERLDEV), and the action taken with the device as a result of the AE (AEACNDEV). The sponsor has chosen to use the ISO 14155 controlled terminology for Relationship of AE to Device. The sensor attachment to the skin caused some skin irritation, which was considered to be caused by the device; the action taken was to reposition the device, and the subject recovered.

**Row 2:** Shows an adverse event of infection at the sensor site. In the Microbiology Specimen (MB) domain (not shown), a record shows that the infection was caused by a microbe with partial resistance to common antibiotics, and so the subject was hospitalized to receive intravenous treatment. The event was considered to be probably related to the device, and was serious. The seriousness criteria included hospitalization, and the device-specific criterion of requiring intervention to prevent progression to life-threatening or fatal conditions (AESINTV).

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | AESEQ | AESPID | AETERM | AEDECOD | AESER | AESEV | AEACNDEV | AERLDEV | AEOUT | AESCONG | AESDISAB | AESDTH | AESHOSP | AESLIFE | AESMIE | AESINTV | AESTDTC | AEENDTC | AESTDY | AEENDY |
|-----|---------|--------|---------|---------|-------|--------|--------|---------|-------|-------|----------|---------|-------|---------|----------|--------|---------|---------|--------|---------|---------|---------|--------|--------|
| 1 | 1001 | AE | 001 | Sensor123 | 1 | AE0049 | Skin redness | ERYTHEMA | N | MILD | SENSOR REPLACED AND REPOSITIONED | CAUSAL RELATIONSHIP | RECOVERED/RESOLVED | N | N | N | N | N | N | | 2013-09-07 | 2013-09-07 | 23 | 25 |
| 2 | 1001 | AE | 001 | Sensor123 | 2 | AE0049 | Infection at sensor site | INFECTION | Y | MODERATE | SENSOR REPLACED AND REPOSITIONED | PROBABLE | RECOVERED/RESOLVED | N | N | N | Y | N | N | Y | 2014-10-24 | 2014-11-27 | 78 | 113 |
