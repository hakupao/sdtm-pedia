# SDTMIG v3.4 --- Domain Models: Events — Part 1

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 1/2 — 6.2.1-6.2.3: AE, BE, CE
> **Original:** `SDTMIG34_05_DomainModels_Events.md`
> **Related:** `SDTMIG34_05b_DomainModels_Events.md`

---

## 6.2.1 Adverse Events (AE)

### AE — Description/Overview

An events domain that captures adverse events, defined as any untoward medical occurrence in a subject administered a pharmaceutical product, regardless of whether a causal relationship with the treatment is established. AE records represent individual occurrences or periods of constant severity for adverse events and include coding, severity, seriousness criteria, causality, actions taken, and outcome information.

### AE — Specification

**ae.xpt, Adverse Events — Events, One record per adverse event per subject, Tabulation.**

| # | Variable | Label | Type | Controlled Terms / Format | Role | Core | CDISC Notes |
|---|----------|-------|------|---------------------------|------|------|-------------|
| 1 | STUDYID | Study Identifier | Char | | Identifier | Req | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | AE | Identifier | Req | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | | Identifier | Req | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | | Identifier | Perm | A sequence of characters used by the sponsor to uniquely identify a specific device. Used to represent a device associated in some way with the adverse event. SPDEVID values are defined in the Device Identifiers (DI) domain. |
| 5 | AESEQ | Sequence Number | Num | | Identifier | Req | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 6 | AEGRPID | Group ID | Char | | Identifier | Perm | Used to tie together a block of related records in a single domain for a subject. |
| 7 | AEREFID | Reference ID | Char | | Identifier | Perm | Internal or external identifier such as a serial number on an SAE reporting form. |
| 8 | AESPID | Sponsor-Defined Identifier | Char | | Identifier | Perm | Sponsor-defined identifier. It may be preprinted on the CRF as an explicit line identifier or defined in the sponsor's operational database. Example: Line number on an Adverse Events CRF page. |
| 9 | AETERM | Reported Term for the Adverse Event | Char | | Topic | Req | Verbatim name of the event. |
| 10 | AEMODIFY | Modified Reported Term | Char | | Synonym Qualifier | Perm | If AETERM is modified to facilitate coding, then AEMODIFY will contain the modified text. |
| 11 | AELLT | Lowest Level Term | Char | MedDRA | Variable Qualifier | Exp | Dictionary-derived text description of the lowest level term. |
| 12 | AELLTCD | Lowest Level Term Code | Num | MedDRA | Variable Qualifier | Exp | Dictionary-derived code for the lowest level term. |
| 13 | AEDECOD | Dictionary-Derived Term | Char | MedDRA | Synonym Qualifier | Req | Dictionary-derived text description of AETERM or AEMODIFY. Equivalent to the Preferred Term (PT in MedDRA). The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document. |
| 14 | AEPTCD | Preferred Term Code | Num | MedDRA | Variable Qualifier | Exp | Dictionary-derived code for the preferred term. |
| 15 | AEHLT | High Level Term | Char | MedDRA | Variable Qualifier | Exp | Dictionary-derived text description of the high level term for the primary system organ class (SOC). |
| 16 | AEHLTCD | High Level Term Code | Num | MedDRA | Variable Qualifier | Exp | Dictionary-derived code for the high level term for the primary SOC. |
| 17 | AEHLGT | High Level Group Term | Char | MedDRA | Variable Qualifier | Exp | Dictionary-derived text description of the high level group term for the primary SOC. |
| 18 | AEHLGTCD | High Level Group Term Code | Num | MedDRA | Variable Qualifier | Exp | Dictionary-derived code for the high level group term for the primary SOC. |
| 19 | AECAT | Category for Adverse Event | Char | | Grouping Qualifier | Perm | Used to define a category of related records. Examples: "BLEEDING", "NEUROPSYCHIATRIC". |
| 20 | AESCAT | Subcategory for Adverse Event | Char | | Grouping Qualifier | Perm | A further categorization of adverse event. Example: "NEUROLOGIC". |
| 21 | AEPRESP | Pre-Specified Adverse Event | Char | C66742 | Variable Qualifier | Perm | A value of "Y" indicates that this adverse event was prespecified on the CRF. Values are null for spontaneously reported events (i.e., those collected as free-text verbatim terms). |
| 22 | AEBODSYS | Body System or Organ Class | Char | | Record Qualifier | Exp | Dictionary derived. Body system or organ class used by the sponsor from the coding dictionary (e.g., MedDRA). When using a multi-axial dictionary such as MedDRA, this should contain the SOC used for the sponsor's analyses and summary tables, which may not necessarily be the primary SOC. |
| 23 | AEBDSYCD | Body System or Organ Class Code | Num | MedDRA | Variable Qualifier | Exp | Dictionary derived. Code for the body system or organ class used by the sponsor. |
| 24 | AESOC | Primary System Organ Class | Char | MedDRA | Variable Qualifier | Exp | Dictionary-derived text description of the primary SOC. Will be the same as AEBODSYS if the primary SOC was used for analysis. |
| 25 | AESOCCD | Primary System Organ Class Code | Num | MedDRA | Variable Qualifier | Exp | Dictionary-derived code for the primary SOC. Will be the same as AEBDSYCD if the primary SOC was used for analysis. |
| 26 | AELOC | Location of Event | Char | C74456 | Record Qualifier | Perm | Describes anatomical location relevant for the event (e.g., "ARM" for skin rash). |
| 27 | AESEV | Severity/Intensity | Char | C66769 | Record Qualifier | Perm | The severity or intensity of the event. Examples: "MILD", "MODERATE", "SEVERE". |
| 28 | AESER | Serious Event | Char | C66742 | Record Qualifier | Exp | Is this a serious event? Valid values are "Y" and "N". |
| 29 | AEACN | Action Taken with Study Treatment | Char | C66767 | Record Qualifier | Exp | Describes changes to the study treatment as a result of the event. AEACN is specifically for the relationship to study treatment. Examples: "DRUG WITHDRAWN", "DOSE REDUCED", "DOSE INCREASED", "DOSE NOT CHANGED", "UNKNOWN", "NOT APPLICABLE". |
| 30 | AEACNOTH | Other Action Taken | Char | | Record Qualifier | Perm | Describes other actions taken as a result of the event that are unrelated to dose adjustments of study treatment. Usually reported as free text. Example: "TREATMENT UNBLINDED. PRIMARY CARE PHYSICIAN NOTIFIED". |
| 31 | AEACNDEV | Action Taken with Device | Char | C111110 | Record Qualifier | Perm | An action taken with a device as the result of the event. The device may or may not be a device under study. |
| 32 | AEREL | Causality | Char | | Record Qualifier | Exp | Records the investigator's opinion as to the causality of the event to the treatment. ICH E2A and E2B examples include terms such as "NOT RELATED", "UNLIKELY RELATED", "POSSIBLY RELATED", "RELATED". |
| 33 | AERLDEV | Relationship of Event to Device | Char | | Record Qualifier | Perm | A judgment as to the likelihood that the device caused the adverse event. |
| 34 | AERELNST | Relationship to Non-Study Treatment | Char | | Record Qualifier | Perm | Records the investigator's opinion as to whether the event may have been due to a treatment other than study drug. |
| 35 | AEPATT | Pattern of Adverse Event | Char | | Record Qualifier | Perm | Used to indicate the pattern of the event over time. Examples: "INTERMITTENT", "CONTINUOUS", "SINGLE EVENT". |
| 36 | AEOUT | Outcome of Adverse Event | Char | C66768 | Record Qualifier | Perm | Description of the outcome of an event. |
| 37 | AESCAN | Involves Cancer | Char | C66742 | Record Qualifier | Perm | Was the serious event associated with the development of cancer? Valid values are "Y" and "N". Legacy seriousness criterion not in ICH E2A or E2B. |
| 38 | AESCONG | Congenital Anomaly or Birth Defect | Char | C66742 | Record Qualifier | Perm | Was the serious event associated with congenital anomaly or birth defect? Valid values are "Y" and "N". |
| 39 | AESDISAB | Persist or Signif Disability/Incapacity | Char | C66742 | Record Qualifier | Perm | Did the serious event result in persistent or significant disability/incapacity? Valid values are "Y" and "N". |
| 40 | AESDTH | Results in Death | Char | C66742 | Record Qualifier | Perm | Did the serious event result in death? Valid values are "Y" and "N". |
| 41 | AESHOSP | Requires or Prolongs Hospitalization | Char | C66742 | Record Qualifier | Perm | Did the serious event require or prolong hospitalization? Valid values are "Y" and "N". |
| 42 | AESLIFE | Is Life Threatening | Char | C66742 | Record Qualifier | Perm | Was the serious event life-threatening? Valid values are "Y" and "N". |
| 43 | AESOD | Occurred with Overdose | Char | C66742 | Record Qualifier | Perm | Did the serious event occur with an overdose? Valid values are "Y" and "N". Legacy seriousness criterion not in ICH E2A or E2B. |
| 44 | AESMIE | Other Medically Important Serious Event | Char | C66742 | Record Qualifier | Perm | Do additional categories for seriousness apply? Valid values are "Y" and "N". |
| 45 | AESINTV | Needs Intervention to Prevent Impairment | Char | C66742 | Record Qualifier | Perm | Records whether medical or surgical intervention was necessary to preclude permanent impairment of a body function, or to prevent permanent damage to a body structure. Part of the US federal government definition of a serious adverse event; see 21 CFR Part 803.3(w)(3). |
| 46 | AEUNANT | Unanticipated Adverse Device Effect | Char | C66742 | Record Qualifier | Perm | Any serious adverse effect on health or safety or any life-threatening problem or death caused by or associated with a device, if that effect, problem, or death was not previously identified in the investigational plan or application. (21 CFR Part 812.3(s)). |
| 47 | AERLPRT | Rel of AE to Non-Dev-Rel Study Activity | Char | | Record Qualifier | Perm | The investigator's opinion as to the causality of the event as related to other protocol-required activities, actions, or assessments. |
| 48 | AERLPRC | Rel of AE to Device-Related Procedure | Char | | Record Qualifier | Perm | The investigator's opinion as to the likelihood that the device-related study procedure caused the AE. |
| 49 | AECONTRT | Concomitant or Additional Trtmnt Given | Char | C66742 | Record Qualifier | Perm | Was another treatment given because of the occurrence of the event? Valid values are "Y" and "N". |
| 50 | AETOXGR | Standard Toxicity Grade | Char | | Record Qualifier | Perm | Toxicity grade according to a standard toxicity scale (e.g., CTCAE). If value is from a numeric scale, represent only the number (e.g., "2", not "Grade 2"). |
| 51 | TAETORD | Planned Order of Element within Arm | Num | | Timing | Perm | Number that gives the planned order of the element within the arm. |
| 52 | EPOCH | Epoch | Char | C99079 | Timing | Perm | Epoch associated with the start date/time of the adverse event. Examples: "SCREENING", "TREATMENT", "FOLLOW-UP". |
| 53 | AESTDTC | Start Date/Time of Adverse Event | Char | ISO 8601 | Timing | Exp | Start date/time of the adverse event represented in ISO 8601 character format. |
| 54 | AEENDTC | End Date/Time of Adverse Event | Char | ISO 8601 | Timing | Exp | End date/time of the adverse event represented in ISO 8601 character format. |
| 55 | AESTDY | Study Day of Start of Adverse Event | Num | | Timing | Perm | Study day of start of adverse event relative to the sponsor-defined RFSTDTC. |
| 56 | AEENDY | Study Day of End of Adverse Event | Num | | Timing | Perm | Study day of end of event relative to the sponsor-defined RFSTDTC. |
| 57 | AEDUR | Duration of Adverse Event | Char | ISO 8601 | Timing | Perm | Collected duration and unit of an adverse event. Used only if collected on the CRF and not derived from start and end date/times. Example: "P1DT2H" (for 1 day, 2 hours). |
| 58 | AEENRF | End Relative to Reference Period | Char | C66728 | Timing | Perm | Describes the end of the event relative to the sponsor-defined reference period. See Section 4.4.7. |
| 59 | AEENRTPT | End Relative to Reference Time Point | Char | C66728 | Timing | Perm | Identifies the end of the event as being before or after the reference time point defined by variable AEENTPT. See Section 4.4.7. |
| 60 | AEENTPT | End Reference Time Point | Char | | Timing | Perm | Description of date/time in ISO 8601 character format of the reference point referred to by AEENRTPT. Examples: "2003-12-25", "VISIT 2". |

### AE — Assumptions

1. The Adverse Events dataset includes clinical data describing "any untoward medical occurrence in a patient or clinical investigation subject administered a pharmaceutical product and which does not necessarily have to have a causal relationship with this treatment" (ICH E2A). In consultation with regulatory authorities, sponsors may extend or limit the scope of adverse event collection. The events included in the AE dataset should be consistent with the protocol requirements. Adverse events may be captured either as free text or via a prespecified list of terms.

2. **AE description and coding**
   - **(a)** AETERM captures the verbatim term collected for the event. It is the topic variable for the AE dataset. AETERM is a required variable and must have a value.
   - **(b)** AEMODIFY is a permissible variable and should be included if the sponsor's procedure permits modification of a verbatim term for coding. The modified term is listed in AEMODIFY. The variable should be populated as per the sponsor's procedures.
   - **(c)** AEDECOD is the preferred term derived by the sponsor from the coding dictionary. It is a required variable and must have a value. It is expected that the reported term (AETERM) will be coded using a standard dictionary such as MedDRA. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.
   - **(d)** AEBODSYS is the system organ class (SOC) from the coding dictionary associated with the adverse event by the sponsor. This value may differ from the primary SOC designated in the coding dictionary's standard hierarchy. It is expected that this variable will be populated.

3. **Additional categorization and grouping**
   - **(a)** AECAT and AESCAT should not be redundant with the domain code or dictionary classification provided by AEDECOD and AEBODSYS (i.e., they should provide a different means of defining or classifying AE records). AECAT and AESCAT are intended for categorizations that are defined in advance. For example, a sponsor may have a CRF page for AEs of special interest and another page for all other AEs. AECAT and AESCAT should not be used for after-the-fact categorizations such as "clinically significant." In cases where a category of AEs of special interest resembles a part of the dictionary hierarchy (e.g., "CARDIAC EVENTS"), the categorization represented by AECAT and AESCAT may differ from the categorization derived from the coding dictionary.
   - **(b)** AEGRPID may be used to link (or associate) different records together to form a block of related records at the subject level within the AE domain; see Section 4.2.6, Grouping Variables and Categorization.

4. **Prespecified terms; presence or absence of events**
   - **(a)** Adverse events are generally collected in 2 different ways, either by recording free text or using a prespecified list of terms. In the latter case, the solicitation of information on specific adverse events may affect the frequency at which they are reported; therefore, the fact that a specific adverse event was solicited may be of interest to reviewers. An AEPRESP value of "Y" is used to indicate that the event in AETERM was prespecified on the CRF.
   - **(b)** If it is important to know which adverse events from a prespecified list were not reported as well as those that did occur, these data should be submitted in a Findings class dataset such as Findings About Events and Interventions (see Section 6.4). A record should be included in that Findings dataset for each prespecified adverse-event term. Records for adverse events that actually occurred should also exist in the AE dataset with AEPRESP set to "Y."
   - **(c)** If a study collects both prespecified adverse events and free-text events, the value of AEPRESP should be "Y" for all prespecified events and null for events reported as free text. AEPRESP is a permissible field and may be omitted from the dataset if all adverse events were collected as free text.
   - **(d)** When adverse events are collected with the recording of free text, a record may be entered into the sponsor's data management system to indicate "no adverse events" for a specific subject. For these subjects, do not include a record in the AE submission dataset to indicate that there were no events. Records should be included in the submission AE dataset only for adverse events that have actually occurred.

5. **Timing variables**
   - **(a)** Relative timing assessment "Ongoing" is common in the collection of AE information. AEENRF may be used when this relative timing assessment is made coincident with the end of the study reference period for the subject represented in the Demographics (DM) dataset (RFENDTC). AEENRTPT with AEENTPT may be used when "Ongoing" is relative to another date (e.g., the final safety follow-up visit date). See Section 4.4.7, Use of Relative Timing Variables.
   - **(b)** Additional timing variables (e.g., AEDTC) may be used when appropriate.

6. **Actions taken**
   - **(a)** AECONTRT is a Y/N variable. If the non-study treatment is collected, the name and other information about the treatment should be represented in the appropriate Interventions domain — usually Concomitant/Prior Medications (CM) or Procedures (PR) — and linked to the AE record with RELREC.
   - **(b)** Actions other than concomitant treatments are recorded in:
     - AEACN, only for actions taken with study treatment
     - AEACNDEV, for actions with a device
     - AEACNOTH, for actions that do not involve treatment or a device

7. **Other qualifier variables**
   - **(a)** If categories of serious events are collected secondarily to a leading question, the values of the variables that capture reasons an event is considered serious (e.g., AESCAN, AESCONG) may be null:

     > For example, if "Serious?" is answered "No", the values for these variables may be null. However, if "Serious?" is answered "Yes", at least one of them will have a "Y" response. Others may be "N" or null, according to the sponsor's convention.
     >
     > CRF example:
     > - Serious? [ ] Yes [ ] No
     > - If yes, check all that apply: [ ] Fatal [ ] Life-threatening [ ] Inpatient hospitalization... [ ] etc.

     On the other hand, if the CRF is structured so that a response is collected for each seriousness category, all category variables (e.g., AESDTH, AESHOSP) would be populated and AESER would be derived.

   - **(b)** The serious categories "Involves Cancer" (AESCAN) and "Occurred with Overdose" (AESOD) are not part of the ICH definition of a serious adverse event, but these categories are available for use in studies conducted under guidelines that existed prior to the FDA's adoption of the ICH definition.
   - **(c)** When a description of "Other Medically Important Serious Adverse Events" category is collected on a CRF, sponsors should place the description in the SUPPAE dataset using the standard supplemental qualifier name code AESOSP as described in Section 8.4 and Appendix C1.
   - **(d)** In studies using toxicity grade according to a standard toxicity scale such as the CTCAE, published by the NCI, AETOXGR should be used instead of AESEV. In most cases, either AESEV or AETOXGR is populated but not both. There may be cases when a sponsor may need to populate both variables. The sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document.
   - **(e)** The structure of the AE domain is 1 record per adverse event per subject. It is the sponsor's responsibility to define an event. This definition may vary based on the sponsor's requirements for characterizing and reporting product safety and is usually described in the protocol. Examples of dataset structure include:
     - **(i)** One record per adverse event per subject for each unique event. Multiple adverse event records reported by the investigator are submitted as summary records "collapsed" to the highest level of severity, causality, seriousness, and the final outcome.
     - **(ii)** One record per adverse event per subject. Changes over time in severity, causality, or seriousness are submitted as separate events. Alternatively, these changes may be submitted in a separate dataset based on the Findings About Events and Interventions model (see Section 6.4).
     - **(iii)** Other approaches may also be reasonable as long as they meet the sponsor's safety evaluation requirements and each submitted record represents a unique event. The domain-level metadata (see Section 3.2) should clarify the structure of the dataset.

8. **Use of EPOCH and TAETORD:** When EPOCH is included in the AE domain, it should be the epoch of the start of the adverse event. In other words, it should be based on AESTDTC, rather than AEENDTC. The computational method for EPOCH in the Define-XML document should describe any assumptions made. Similarly, if TAETORD is included, it should be the value for the start of the adverse event.

9. Any additional identifier variables may be added to the AE domain.

10. The following qualifiers would not be used in AE: --OCCUR, --STAT, and --REASND. They are the only qualifiers from the SDTM Events class not in the AE domain. They are not permitted because the AE domain contains only records for adverse events that actually occurred. See Assumption 4b for information on how to deal with negative responses or missing responses to probing questions for prespecified adverse events.

11. Variable order in the domain should follow the rules as described in Section 4.1.4, Order of the Variables, and the order described in Section 1.1, Purpose.

12. The addition of AELLT, AELLTCD, AEPTCD, AEHLT, AEHLTCD, AEHLGT, AEHLGTCD, AEBDSYCD, AESOC, and AESOCCD is applicable to submissions coded in MedDRA only. Data items are not expected for non-MedDRA coding.

### AE — Examples

#### Example 1

This example illustrates data from an AE CRF that collected AE terms as free text. AEs were coded using MedDRA, and the sponsor's procedures include the possibility of modifying the reported term to aid in coding. The CRF was structured so that seriousness category variables (e.g., AESDTH, AESHOSP) were checked only when AESER is answered "Y." In this study, the study reference period started at the start of study treatment. Three AEs were reported for this subject.

- **Rows 1-2:** Show examples of modifying the reported term for coding purposes, with the modified term in AEMODIFY. These adverse events were not serious, so the seriousness criteria variables are null. Note that for the event in Row 2, AESTDY = "1". Day 1 was the day treatment started; the AE start and end times, as well as dates, were collected to allow comparison of the AE timing to the start of treatment.
- **Row 3:** Shows an example of the overall seriousness question AESER answered with "Y" and the relevant corresponding seriousness category variables (AESHOSP and AESLIFE) answered "Y". The other seriousness category variables are left blank. This row also shows AEENRF being populated because the AE was marked as "Continuing" as of the end of the study reference period for the subject (see Section 4.4.7).

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEMODIFY | AEDECOD | AEBODSYS | AESEV | AESER | AEACN | AEREL | AEOUT | AESCONG | AESDISAB | AESDTH | AESHOSP | AESLIFE | AESMIE | EPOCH | AESTDTC | AEENDTC | AESTDY | AEENDY | AEENRF |
|-----|---------|--------|---------|-------|--------|----------|---------|----------|-------|-------|-------|-------|-------|---------|----------|--------|---------|---------|--------|-------|---------|---------|--------|--------|--------|
| 1 | ABC123 | AE | 123101 | 1 | POUNDING HEADACHE | HEADACHE | Headache | Nervous system disorders | SEVERE | N | NOT APPLICABLE | DEFINITELY NOT RELATED | RECOVERED/RESOLVED | | | | | | | SCREENING | 2005-10-12 | 2005-10-12 | -1 | -1 | |
| 2 | ABC123 | AE | 123101 | 2 | BACK PAIN FOR 6 HOURS | BACK PAIN | Back pain | Musculoskeletal and connective tissue disorders | MODERATE | N | DOSE REDUCED | PROBABLY RELATED | RECOVERED/RESOLVED | | | | | | | TREATMENT | 2005-10-13T13:05 | 2005-10-13T19:00 | 1 | 1 | |
| 3 | ABC123 | AE | 123101 | 3 | PULMONARY EMBOLISM | | Pulmonary embolism | Vascular disorders | MODERATE | Y | DOSE REDUCED | PROBABLY NOT RELATED | RECOVERING/RESOLVING | | | | Y | Y | | TREATMENT | 2005-10-21 | | 9 | | AFTER |

#### Example 2

This example illustrates data from an AE CRF using a prespecified list of AE terms. The AEPRESP value of "Y" indicates that the event was prespecified. Free-text events would have a null value for AEPRESP.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEDECOD | AEPRESP | AEBODSYS | AESEV | AESER | AEACN | AEREL | AEOUT | EPOCH | AESTDTC | AEENDTC | AESTDY | AEENDY |
|-----|---------|--------|---------|-------|--------|---------|---------|----------|-------|-------|-------|-------|-------|-------|---------|---------|--------|--------|
| 1 | ABC123 | AE | 123101 | 1 | NAUSEA | Nausea | Y | Gastrointestinal disorders | SEVERE | N | DOSE REDUCED | RELATED | RECOVERED/RESOLVED | TREATMENT | 2005-10-12 | 2005-10-13 | 2 | 3 |
| 2 | ABC123 | AE | 123101 | 2 | VOMITING | Vomiting | Y | Gastrointestinal disorders | MODERATE | N | DOSE REDUCED | RELATED | RECOVERED/RESOLVED | TREATMENT | 2005-10-13T13:00 | 2005-10-13T19:00 | 3 | 3 |
| 3 | ABC123 | AE | 123101 | 3 | HEADACHE | Headache | | Nervous system disorders | MILD | N | DOSE NOT CHANGED | POSSIBLY RELATED | RECOVERED/RESOLVED | TREATMENT | 2005-10-21 | 2005-10-21 | 11 | 11 |

#### Example 3

In this example, a CRF module that asked whether or not nausea, vomiting, or diarrhea occurred was included in the study only once. In the context of this study, the conditions that occurred were reportable as adverse events. No additional data about these events was collected. No other AE information was collected via general questions. The responses to the probing questions "Yes", "No", or "Not Done" were represented in the FA domain (see Section 6.4, Findings About Events or Interventions). This is an example of unusually sparse AE data collection; the AE dataset is populated with the term and the flag indicating that it was prespecified, but timing information is limited to the date of collection, and other expected qualifiers are not available. RELREC may be used to relate AE records and FA records.

The subject shown in this example experienced nausea and vomiting. The subject did not experience diarrhea, so no record for that term exists in the AE dataset.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEDECOD | AEPRESP | AEBODSYS | AESER | AEACN | AEREL | AEDTC | AESTDTC | AEENDTC | AEDY |
|-----|---------|--------|---------|-------|--------|---------|---------|----------|-------|-------|-------|-------|---------|---------|------|
| 1 | ABC123 | AE | 123101 | 1 | NAUSEA | Nausea | Y | Gastrointestinal disorders | | | | 2005-10-29 | | | 19 |
| 2 | ABC123 | AE | 123101 | 2 | VOMITING | Vomiting | Y | Gastrointestinal disorders | | | | 2005-10-29 | | | 19 |

#### Example 4

In this example, the investigator was instructed to create a new AE record each time the severity of an adverse event changed. The sponsor used AEGRPID to identify the group of records related to a single event for a subject.

- **Row 1:** Shows an adverse event of nausea, for which severity was moderate.
- **Rows 2-4:** Show AEGRPID used to group records related to a single event of "VOMITING".
- **Rows 5-6:** Show AEGRPID used to group records related to a single event of "DIARRHEA".

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AEGRPID | AETERM | AEBODSYS | AESEV | AESER | AEACN | AEREL | AESTDTC | AEENDTC |
|-----|---------|--------|---------|-------|---------|--------|----------|-------|-------|-------|-------|---------|---------|
| 1 | ABC123 | AE | 123101 | 1 | | NAUSEA | Gastrointestinal disorders | MODERATE | N | DOSE NOT CHANGED | RELATED | 2005-10-13 | 2005-10-14 |
| 2 | ABC123 | AE | 123101 | 2 | 1 | VOMITING | Gastrointestinal disorders | MILD | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-14 | 2005-10-16 |
| 3 | ABC123 | AE | 123101 | 3 | 1 | VOMITING | Gastrointestinal disorders | SEVERE | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-16 | 2005-10-17 |
| 4 | ABC123 | AE | 123101 | 4 | 1 | VOMITING | Gastrointestinal disorders | MILD | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-17 | 2005-10-20 |
| 5 | ABC123 | AE | 123101 | 5 | 2 | DIARRHEA | Gastrointestinal disorders | SEVERE | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-16 | 2005-10-17 |
| 6 | ABC123 | AE | 123101 | 6 | 2 | DIARRHEA | Gastrointestinal disorders | MODERATE | N | DOSE NOT CHANGED | POSSIBLY RELATED | 2005-10-17 | 2005-10-21 |

#### Example 5

This study was evaluating artificial hip joints made of a novel material. The protocol specified that only 1 hip could be replaced in a subject, and that subjects should be encouraged to begin walking within 2 days after surgery. This subject was walking on day 5 and tripped and sprained her left ankle. A few days later, she developed an infection in the hip bone adjacent to the implant. The implant was removed and replaced by a different product. She never regained full use of her hip, and was left with a limp. This example shows the use of the device-related variables indicating if the AE was unanticipated (AEUNANT), if it was related to the procedure that implanted the device rather than the device itself (AERLPRC), or if it was related to some other procedure or activity required by the protocol (AERLPRT). These are used to determine if the AE was an unanticipated serious device event, a designation required by some regulatory authorities. Device Identifiers (DI) and other related device domains have not been modeled here; for more information about device domains, see the SDTMIG-MD.

- **Row 1:** Shows an AE of "Twisted left ankle". The location and laterality are specified as it may be important to know if it occurred on the same or opposite side of the body.
- **Row 2:** Shows an AE of "Osteomyelitis right hip". The location and laterality are specified and it is considered a serious adverse event. The device was removed as the AE was probably related to the event.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | AESEQ | AESPID | AETERM | AEDECOD | AELOC | AELAT | AESER | AESEV | AEACNDEV | AERLDEV | AEOUT | AESCONG | AESHOSP | AESDISAB | AESDTH | AESLIFE | AESMIE | AESINTV | AEUNANT | AERLPRC | AERLPRT | AESTDTC | AEENDTC | AESTDY | AEENDY |
|-----|---------|--------|---------|---------|-------|--------|--------|---------|-------|-------|-------|-------|----------|---------|-------|---------|---------|----------|--------|---------|--------|---------|---------|---------|---------|---------|---------|--------|--------|
| 1 | T002 | AE | 002 | HipX22 | 1 | AE0099 | Twisted left ankle | SPRAIN | ANKLE JOINT | LEFT | N | MILD | NONE | NOT RELATED | RECOVERED/RESOLVED | N | N | N | N | N | N | N | Y | N | Y | 2018-04-21 | 2018-04-26 | 5 | 10 |
| 2 | T002 | AE | 002 | HipX22 | 2 | AE0033 | Osteomyelitis right hip | OSTEOMYELITIS | HIP | RIGHT | Y | MODERATE | REMOVED | PROBABLE | RECOVERED/RESOLVED WITH SEQUELAE | N | Y | Y | N | N | N | Y | Y | N | N | 2018-05-01 | 2018-05-10 | 15 | 25 |

#### Example 6

This study was testing an implanted cardiac pacemaker that was paired with a transmitting sensor that was attached to the participant's skin. The sensor picked up transmitted measurements from the pacemaker and relayed them to a cell network and then to the subject's and investigator's smart phones. The devices were the focus of the study. The DI domain and other related device domains have not been modeled here; for further information about the device domains, see the SDTMIG-MD.

- **Row 1:** Shows the use of the variables for the relationship of the device to the AE (AERLDEV), and the action taken with the device as a result of the AE (AEACNDEV). The sponsor has chosen to use the ISO 14155 controlled terminology for Relationship of AE to Device. The sensor attachment to the skin caused some skin irritation, which was considered to be caused by the device; the action taken was to reposition the device, and the subject recovered.
- **Row 2:** Shows an adverse event of infection at the sensor site. In the Microbiology Specimen (MB) domain (not shown), a record shows that the infection was caused by a microbe with partial resistance to common antibiotics, and so the subject was hospitalized to receive intravenous treatment. The event was considered to be probably related to the device, and was serious. The seriousness criteria included hospitalization, and the device-specific criterion of requiring intervention to prevent progression to life-threatening or fatal conditions (AESINTV).

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | AESEQ | AESPID | AETERM | AEDECOD | AESER | AESEV | AEACNDEV | AERLDEV | AEOUT | AESCONG | AESHOSP | AESDISAB | AESDTH | AESLIFE | AESMIE | AESINTV | AESTDTC | AEENDTC | AESTDY | AEENDY |
|-----|---------|--------|---------|---------|-------|--------|--------|---------|-------|-------|----------|---------|-------|---------|---------|----------|--------|---------|--------|---------|---------|---------|--------|--------|
| 1 | T001 | AE | 002 | Sensor123 | 1 | AE0007 | Skin redness | ERYTHEMA | N | MILD | SENSOR REPOSITIONED | CAUSAL | RECOVERED/RESOLVED | N | N | N | N | N | N | N | 2018-09-01 | 2018-09-07 | 27 | 33 |
| 2 | T001 | AE | 001 | Sensor123 | 2 | AE0049 | Infection at sensor site | INFECTION | Y | MODERATE | SENSOR REPLACED AND REPOSITIONED | PROBABLE | RECOVERED/RESOLVED | N | Y | N | N | N | N | Y | 2018-10-24 | 2018-11-27 | 78 | 113 |

---

## 6.2.2 Biospecimen Events (BE)

> BE, BS, and RELSPEC domain specifications, assumptions, and examples were copied and minimally updated from the provisional SDTMIG-PGx, published 2015-05-26. This was done in preparation for the retirement of the SDTMIG-PGx upon publication of SDTMIG v3.4. These domains are currently under extensive revision for inclusion in a future SDTMIG publication, after v3.4.

### BE — Description/Overview

An events domain that documents actions taken that affect or may affect a specimen (e.g., specimen collection, freezing and thawing, aliquoting, transportation).

### BE — Specification

**be.xpt, Biospecimen Events — Events, One record per instance per biospecimen event per biospecimen identifier per subject, Tabulation.**

| # | Variable | Label | Type | Controlled Terms / Format | Role | Core | CDISC Notes |
|---|----------|-------|------|---------------------------|------|------|-------------|
| 1 | STUDYID | Study Identifier | Char | | Identifier | Req | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | BE | Identifier | Req | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | | Identifier | Req | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | SPDEVID | Sponsor Device Identifier | Char | | Identifier | Perm | Sponsor-defined identifier for a device. |
| 5 | BESEQ | Sequence Number | Num | | Identifier | Req | Sequence number to ensure uniqueness of records within a dataset for a subject. |
| 6 | BEGRPID | Group ID | Char | | Identifier | Perm | Optional group identifier, used to link together a block of related records within a subject in a domain. |
| 7 | BEREFID | Reference ID | Char | | Identifier | Exp | Internal or external identifier for the specimen affected or created by the event. |
| 8 | BESPID | Sponsor-Defined Identifier | Char | | Identifier | Perm | Optional sponsor-defined reference number. Example: Line number on a CRF page. |
| 9 | BETERM | Reported Term for the Biospecimen Event | Char | | Topic | Req | Topic variable for an event observation, which is the verbatim or pre-specified name of the event. |
| 10 | BEMODIFY | Modified Reported Term | Char | | Synonym Qualifier | Perm | If the value for BETERM is modified for coding purposes, then the modified text is placed here. |
| 11 | BEDECOD | Dictionary-Derived Term | Char | C124297 | Synonym Qualifier | Perm | Dictionary-derived text description of BETERM or BEMODIFY, if applicable. |
| 12 | BECAT | Category for Biospecimen Event | Char | | Grouping Qualifier | Perm | Used to define a category of topic-variable values. Example: COLLECTION, PREPARATION, TRANSPORT. |
| 13 | BESCAT | Subcategory for Biospecimen Event | Char | | Grouping Qualifier | Perm | A further categorization of BECAT values. |
| 14 | BELOC | Anatomical Location of Event | Char | C74456 | Record Qualifier | Perm | Describes the anatomical location relevant for the event (e.g., BRAIN, LUNG). |
| 15 | BEPARTY | Accountable Party | Char | | Record Qualifier | Perm | Party accountable for the transferable object (e.g., specimen) as a result of the activity performed in the associated BETERM variable. |
| 16 | BEPRTYID | Identification of Accountable Party | Char | | Record Qualifier | Perm | Identification of the specific party accountable for the transferable object after the action in BETERM is taken. Used in conjunction with BEPARTY. |
| 17 | VISITNUM | Visit Number | Num | | Timing | Exp | Clinical encounter number. Numeric version of VISIT, used for sorting. |
| 18 | VISIT | Visit Name | Char | | Timing | Perm | Protocol-defined description of clinical encounter. |
| 19 | VISITDY | Planned Study Day of Visit | Num | | Timing | Perm | Planned study day of VISIT. Should be an integer. |
| 20 | BEDTC | Date/Time of Specimen Collection | Char | ISO 8601 | Timing | Exp | Date and time of specimen collection. |
| 21 | BESTDTC | Start Date/Time of Biospecimen Event | Char | ISO 8601 | Timing | Exp | Start date/time of the event. |
| 22 | BEENDTC | End Date/Time of Biospecimen Event | Char | ISO 8601 | Timing | Exp | End date/time of the event. |
| 23 | BESTDY | Study Day of Start of Biospecimen Event | Num | | Timing | Perm | Actual study day of start of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 24 | BEENDY | Study Day of End of Biospecimen Event | Num | | Timing | Perm | Actual study day of end of observation expressed in integer days relative to the sponsor-defined RFSTDTC in Demographics. |
| 25 | BEDUR | Duration of Biospecimen Event | Char | ISO 8601 | Timing | Perm | Collected duration and unit of a biospecimen event. Used only if collected on the CRF and not derived from start and end date/times. Example: P1DT2H. |

### BE — Assumptions

1. The BE domain contains data about actions taken that affect or may affect a specimen, such as specimen collection, freezing and thawing, aliquoting, and transportation. This domain is intended to be applicable to any specimen tracking data, regardless of the reason for specimen collection.

2. The value in BEREFID identifies the specimen most affected by the event. For aliquoting, this would be the child specimen(s) created by the event, rather than the parent specimen. BEREFID should not contain any identifiers other than specimen IDs.

3. BELOC holds the relevant anatomic location of the subject, so it should only be populated when the subject participates in and is directly affected by the event given in BETERM.

4. BEPARTY and BEPRTYID together identify the individual or organization that takes responsibility for the biospecimen as a result of the action in BETERM. For example, if BETERM is COLLECTED, BEPARTY would be a general term defining the type of responsible party, such as SITE, and BEPRTYID would contain the site identifier, such as 02. If BEPARTY is sufficient to uniquely identify the party (such as SPONSOR in a single-sponsor study), then BEPRTYID may be null.

5. Usually BEPARTY and BEPRTYID refer to who has possession of the biospecimen after the action in BETERM. In the cases where a biospecimen is lost or destroyed for example, BEPARTY and BEPRTYID may be null.

6. **Timing variables:**
   - **(a)** BESTDTC and BEENDTC hold the start and end date/times for the event given in BETERM. If the end date/time is the same as the start date/time for the event, then BEENDTC is null.
   - **(b)** Unlike other Events domains, BEDTC does not hold the date/time of data collection. Instead, it holds the date/time of specimen collection, in alignment with the use of --DTC for specimen-related findings. BEDTC values for extracted or otherwise derived specimens are copied from that of the parent specimen.
   - **(c)** VISITNUM, VISIT, and VISITDY values for all records refer to the visit in which the originally collected specimen was collected.

7. The following variables generally would not be used in BE: dictionary coding variables (--LLT, --LLTCD, --PTCD, --HLT, --HLTCD, --HLGT, --HLGTCD), AE-specific variables (--SEV, --SER, --ACN, --ACNOTH, --ACNDEV, --REL, --RELNST, --PATT, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --CONTRT), toxicity variables (--TOX, --TOXGR).

### BE — Examples

#### Example 1

In this example, a specimen is collected, flash frozen, thawed, and shipped to another location. Some tests are very sensitive to specimen handling processes such as flash freezing or time spent in transit. Therefore, it is important to record when the processes were started and completed.

- **Row 1:** Shows specimen collection. The value in SPDEVID for this row identifies the vessel into which the specimen is collected.
- **Rows 2-4:** Show the start and end date/times of flash freezing, storing while frozen, and thawing. The value in SPDEVID for Row 3 identifies the freezer in which the specimen is stored.
- **Row 5:** Records the transportation of a biospecimen. Because there is only one ABC Lab, BEPRTYID is null. The value in SPDEVID for this row identifies the shipping container.

**be.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | BESEQ | BEREFID | BETERM | BEDECOD | BEPARTY | BEPRTYID | BECAT | BELOC | VISITNUM | VISIT | BEDTC | BESTDTC | BEENDTC |
|-----|---------|--------|---------|---------|-------|---------|--------|---------|---------|----------|-------|-------|----------|-------|-------|---------|---------|
| 1 | ABC134 | BE | 43871 | TS409871 | 1 | 1148.267 | Collecting | COLLECTING | SITE | 01 | COLLECTION | BRAIN | 1 | BASELINE | 2005-03-20 | 2005-03-20T15:07 | |
| 2 | ABC134 | BE | 43871 | | 2 | 1148.267 | Flash Freezing | FLASH FREEZING | SITE | 01 | PREPARATION | | 1 | BASELINE | 2005-03-20 | 2005-03-20T15:07 | 2005-03-20T15:09 |
| 3 | ABC134 | BE | 43871 | 309827 | 3 | 1148.267 | Storing | STORING | SITE | 01 | STORING | | 1 | BASELINE | 2005-03-20 | 2005-03-20T15:09 | 2005-03-21T10:29 |
| 4 | ABC134 | BE | 43871 | | 4 | 1148.267 | Thawing | THAWING | SITE | 01 | PREPARATION | | 1 | BASELINE | 2005-03-20 | 2005-03-21T10:29 | 2005-03-21T10:36 |
| 5 | ABC134 | BE | 43871 | LN43871 | 5 | 1148.267 | Shipping | SHIPPING | ABC LAB | | TRANSPORT | | 1 | BASELINE | 2005-03-20 | 2005-03-21T11:00 | 2005-03-21T15:00 |

**suppbe.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC134 | BE | 43871 | BEREFID | 1148.267 | BESPEC | SPECIMEN TYPE | TISSUE | CRF | |

Findings related to specimen handling processes are stored in the Biospecimen (BS) domain. These processes can be important to maintain the integrity of the specimens used in genetic variation and gene expression testing.

- **Row 1:** Shows the volume of the biospecimen.
- **Rows 2-3:** Show the flash freeze temperature and material, associated via RELREC with BE Row 2.

**bs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | BSSEQ | BSGRPID | BSREFID | BSTESTCD | BSTEST | BSCAT | BSORRES | BSORRESU | BSSTRESC | BSSTRESN | BSSTRESU | BSSPEC | BSANTREG | VISITNUM | BSDTC |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|----------|-------|
| 1 | ABC134 | BS | 43871 | 1 | | 1148.267 | VOLUME | Volume | SPECIMEN MEASUREMENT | 2 | cm3 | 2 | 2 | cm3 | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |
| 2 | ABC134 | BS | 43871 | 2 | 267FF | 1148.267 | TEMP | Temperature | SPECIMEN HANDLING | -80 | C | -80 | -80 | C | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |
| 3 | ABC134 | BS | 43871 | 3 | 267FF | 1148.267 | FFRZMAT | Flash Freeze Material | SPECIMEN HANDLING | DRY ICE/ISOPROPANOL | | DRY ICE/ISOPROPANOL | | | BRAIN | CEREBRAL AQUEDUCT | 1 | 2005-03-20 |

RELREC relates the records in BE and BS to each other.

- **Rows 1-2:** Tie the specimen's volume to its collection, when the measurement was made.
- **Rows 3-4:** Tie the temperature to which the specimen was flash frozen to the event of its occurrence.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC134 | BE | 43871 | BESEQ | 1 | | 1 |
| 2 | ABC134 | BS | 43871 | BSSEQ | 1 | | 1 |
| 3 | ABC134 | BE | 43871 | BESEQ | 2 | | 2 |
| 4 | ABC134 | BS | 43871 | BSGRPID | 267FF | | 2 |

> **Note:** The Device Identifiers (DI) dataset (required with the use of SPDEVID) is not shown in this example.

#### Example 2

Cell-free RNA, which can be obtained from plasma, may be useful for some tumor-specific cancer detection, but has poor integrity. In this example, a blood sample was drawn, centrifuged to get plasma, and stored in a pretreated container before being shipped to the lab. The lab then extracted and purified RNA from the plasma, divided the RNA into 3 aliquots, and sequenced 1 aliquot immediately while freezing and storing the other 2 for later use.

- **Row 1:** Shows the collection of the blood sample.
- **Row 2:** Shows the extraction of the plasma via centrifuge. SPDEVID holds the identifier for the container into which the plasma is placed.
- **Row 3:** Shows the transportation of the plasma from the site to the lab.
- **Row 4:** Shows the extraction of the RNA, which includes purification and quality control testing to make sure the sample is of a high enough quality to be viable. SPDEVID holds the identifier for the purification kit.
- **Rows 5-7:** Show the aliquoting of the RNA.
- **Row 8:** Shows the sequencing of the first RNA aliquot.
- **Rows 9-10:** Show the freezing of the second and third RNA aliquots.

**be.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | BESEQ | BEREFID | BETERM | BEDECOD | BEPARTY | BEPRTYID | BECAT | VISITNUM | BEDTC | BESTDTC | BEENDTC |
|-----|---------|--------|---------|---------|-------|---------|--------|---------|---------|----------|-------|----------|-------|---------|---------|
| 1 | 3441271 | BE | MU-298 | 293USHE8 | 1 | 298B1 | Collecting | COLLECTING | SITE | 05 | COLLECTION | 2 | 2010-04-01T11:50 | 2010-04-01T11:50 | |
| 2 | 3441271 | BE | MU-298 | PURKIT | 2 | 298B1-1 | Extracting | EXTRACTING | SITE | 05 | EXTRACTION | 2 | 2010-04-01T11:50 | 2010-04-01T12:10 | 2010-04-02T08:00 |
| 3 | 3441271 | BE | MU-298 | | 3 | 298B1-1 | Shipping | SHIPPING | ABC LAB | | TRANSPORT | 2 | 2010-04-01T11:50 | 2010-04-01T15:00 | 2010-04-05T13:50 |
| 4 | 3441271 | BE | MU-298 | PURKIT | 4 | 298R1-1R0 | Extracting | EXTRACTING | ABC LAB | | EXTRACTION | 2 | 2010-04-01T11:50 | 2010-04-02T09:00 | 2010-04-05T13:50 |
| 5 | 3441271 | BE | MU-298 | | 5 | 298R1-1R1 | Aliquoting | ALIQUOTING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |
| 6 | 3441271 | BE | MU-298 | | 6 | 298R1-1R2 | Aliquoting | ALIQUOTING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |
| 7 | 3441271 | BE | MU-298 | | 7 | 298R1-1R3 | Aliquoted | ALIQUOTING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |
| 8 | 3441271 | BE | MU-298 | | 8 | 298R1-1R1 | Sequenced | SEQUENCING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | 2010-04-06T10:30 |
| 9 | 3441271 | BE | MU-298 | | 9 | 298R1-1R2 | Frozen | FREEZING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |
| 10 | 3441271 | BE | MU-298 | | 10 | 298R1-1R3 | Frozen | FREEZING | ABC LAB | | PREPARATION | 2 | 2010-04-01T11:50 | 2010-04-05T13:50 | |

The specimen type is given in a supplemental qualifier that mimics the standard findings variable --SPEC, and draws from the 2 codelists (GENSMP and SPECTYPE) for its values.

- **Rows 1-2:** Give the specimen types for the first 2 specimens as blood and plasma, respectively. These values come from the SPECTYPE codelist.
- **Rows 3-6:** Give the specimen type for all subsequent specimens as RNA. "RNA" is one of the terms in the GENSMP codelist.

**suppbe.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | 3441271 | BE | MU-298 | BEREFID | 298B1 | BESPEC | Specimen Type | BLOOD | CRF | |
| 2 | 3441271 | BE | MU-298 | BEREFID | 298B1-1 | BESPEC | Specimen Type | PLASMA | CRF | |
| 3 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R0 | BESPEC | Specimen Type | RNA | Collected | |
| 4 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R1 | BESPEC | Specimen Type | RNA | Collected | |
| 5 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R2 | BESPEC | Specimen Type | RNA | Collected | |
| 6 | 3441271 | BE | MU-298 | BEREFID | 298R1-1R3 | BESPEC | Specimen Type | RNA | Collected | |

- **Row 1:** Shows the volume of the blood sample.
- **Row 2:** Shows the volume of the plasma sample.
- **Rows 3-4:** Show the volume and purity (integrity) of the RNA sample.
- **Rows 5-7:** Show the volumes of the RNA aliquots.

**bs.xpt**

| Row | STUDYID | DOMAIN | USUBJID | BSSEQ | BSREFID | BSTESTCD | BSTEST | BSCAT | BSORRES | BSORRESU | BSSTRESC | BSSTRESN | BSSTRESU | BSSPEC | VISITNUM | BSDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|
| 1 | 3441271 | BS | MU-298 | 1 | 298B1 | VOLUME | Volume | SPECIMEN MEASUREMENT | 12 | mL | 6 | 6 | mL | BLOOD | 2 | 2010-04-01T11:50 |
| 2 | 3441271 | BS | MU-298 | 2 | 298B1-1 | VOLUME | Volume | SPECIMEN MEASUREMENT | 7 | mL | 6 | 6 | mL | PLASMA | 2 | 2010-04-01T11:50 |
| 3 | 3441271 | BS | MU-298 | 3 | 298B1-1R0 | VOLUME | Volume | SPECIMEN MEASUREMENT | 6 | mL | 6 | 6 | mL | RNA | 2 | 2010-04-01T11:50 |
| 4 | 3441271 | BS | MU-298 | 4 | 298B1-1R0 | RIN | RNA Integrity Number | QUALITY CONTROL | 9.3 | | 9.3 | 9.3 | | RNA | 2 | 2010-04-01T11:50 |
| 5 | 3441271 | BS | MU-298 | 5 | 298R1-1R1 | VOLUME | Volume | SPECIMEN MEASUREMENT | 2 | mL | 2 | 2 | mL | RNA | 2 | 2010-04-01T11:50 |
| 6 | 3441271 | BS | MU-298 | 6 | 298R1-1R2 | VOLUME | Volume | SPECIMEN MEASUREMENT | 2 | mL | 2 | 2 | mL | RNA | 2 | 2010-04-01T11:50 |
| 7 | 3441271 | BS | MU-298 | 7 | 298R1-1R3 | VOLUME | Volume | SPECIMEN MEASUREMENT | 2 | mL | 2 | 2 | mL | RNA | 2 | 2010-04-01T11:50 |

The RELSPEC dataset preserves the specimen hierarchy.

**relspec.xpt**

| Row | STUDYID | USUBJID | REFID | SPEC | PARENT | LEVEL |
|-----|---------|---------|-------|------|--------|-------|
| 1 | 3441271 | MU-298 | 298B1 | BLOOD | | 1 |
| 2 | 3441271 | MU-298 | 298B1-1 | PLASMA | 298B1 | 2 |
| 3 | 3441271 | MU-298 | 298R1-1R0 | RNA | 298B1-1 | 3 |
| 4 | 3441271 | MU-298 | 298R1-1R1 | RNA | 298R1-1R0 | 4 |
| 5 | 3441271 | MU-298 | 298R1-1R2 | RNA | 298R1-1R0 | 4 |
| 6 | 3441271 | MU-298 | 298R1-1R3 | RNA | 298R1-1R0 | 4 |

The relationship between BE and BS is often many-to-many because any given biospecimen may have multiple findings about it and may undergo multiple events.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | 3441271 | BE | | BEREFID | | MANY | 1 |
| 2 | 3441271 | BS | | BSREFID | | MANY | 1 |
| 3 | 3441271 | BE | MU-298 | BESEQ | 8 | | 2 |
| 4 | 3441271 | GF | MU-298 | GFSEQ | 1 | | 2 |
| 5 | 3441271 | GF | MU-298 | GFSEQ | 2 | | 2 |
| 6 | 3441271 | GF | MU-298 | GFSEQ | 3 | | 2 |

> **Note:** The results from the sequencing procedure are stored in the PF domain, which is not shown in this example. See GF examples for examples of GF datasets.

---

## 6.2.3 Clinical Events (CE)

### CE — Description/Overview

An events domain that contains clinical events of interest that would not be classified as adverse events.

### CE — Specification

**ce.xpt, Clinical Events — Events, One record per event per subject, Tabulation.**

| # | Variable | Label | Type | Controlled Terms / Format | Role | Core | CDISC Notes |
|---|----------|-------|------|---------------------------|------|------|-------------|
| 1 | STUDYID | Study Identifier | Char | | Identifier | Req | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | CE | Identifier | Req | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | | Identifier | Req | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | CESEQ | Sequence Number | Num | | Identifier | Req | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | CEGRPID | Group ID | Char | | Identifier | Perm | Used to link together a block of related records for a subject within a domain. |
| 6 | CEREFID | Reference ID | Char | | Identifier | Perm | Internal or external identifier (e.g., lab specimen ID, UUID for an ECG waveform or medical image). |
| 7 | CESPID | Sponsor-Defined Identifier | Char | | Identifier | Perm | Sponsor-defined identifier. |
| 8 | CETERM | Reported Term for the Clinical Event | Char | | Topic | Req | Term for the medical condition or event. Most likely preprinted on CRF. |
| 9 | CEDECOD | Dictionary-Derived Term | Char | | Synonym Qualifier | Perm | Controlled terminology for the name of the clinical event. |
| 10 | CECAT | Category for the Clinical Event | Char | | Grouping Qualifier | Perm | Used to define a category of related records. |
| 11 | CESCAT | Subcategory for the Clinical Event | Char | | Grouping Qualifier | Perm | A further categorization of the condition or event. |
| 12 | CEPRESP | Clinical Event Pre-specified | Char | C66742 | Variable Qualifier | Perm | Used to indicate whether the event in CETERM was prespecified. Value is "Y" for prespecified events and null for spontaneously reported events. |
| 13 | CEOCCUR | Clinical Event Occurrence | Char | C66742 | Record Qualifier | Perm | Used when the occurrence of specific events is solicited, to indicate whether or not a clinical event occurred. Values are null for spontaneously reported events. |
| 14 | CESTAT | Completion Status | Char | C66789 | Record Qualifier | Perm | The status indicates that a question from a prespecified list was not answered. |
| 15 | CEREASND | Reason Clinical Event Not Collected | Char | | Record Qualifier | Perm | Describes the reason clinical event data was not collected. Used in conjunction with CESTAT when value is "NOT DONE". |
| 16 | CEBODSYS | Body System or Organ Class | Char | | Record Qualifier | Perm | Dictionary-derived. Body system or organ class from a standard hierarchy (e.g., MedDRA). |
| 17 | CESEV | Severity/Intensity | Char | C165643 | Record Qualifier | Perm | The severity or intensity of the event. Examples: "MILD", "MODERATE", "SEVERE". |
| 18 | CETOXGR | Standard Toxicity Grade | Char | | Record Qualifier | Perm | Toxicity grade according to a standard toxicity scale (e.g., CTCAE). |
| 19 | TAETORD | Planned Order of Element within Arm | Num | | Timing | Perm | Number that gives the planned order of the element within the arm for the element in which the clinical event started. |
| 20 | EPOCH | Epoch | Char | C99079 | Timing | Perm | Epoch associated with the start date/time of the clinical event. |
| 21 | CEDTC | Date/Time of Event Collection | Char | ISO 8601 | Timing | Perm | Collection date and time for the clinical event observation. |
| 22 | CESTDTC | Start Date/Time of Clinical Event | Char | ISO 8601 | Timing | Perm | Start date/time of the clinical event. |
| 23 | CEENDTC | End Date/Time of Clinical Event | Char | ISO 8601 | Timing | Perm | End date/time of the clinical event. |
| 24 | CEDY | Study Day of Event Collection | Num | | Timing | Perm | Study day of clinical event collection, measured as integer days relative to the sponsor-defined RFSTDTC. |
| 25 | CESTDY | Study Day of Start of Event | Num | | Timing | Perm | Actual study day of start of the clinical event relative to the sponsor-defined RFSTDTC. |
| 26 | CEENDY | Study Day of End of Event | Num | | Timing | Perm | Actual study day of end of the clinical event relative to the sponsor-defined RFSTDTC. |
| 27 | CESTRF | Start Relative to Reference Period | Char | C66728 | Timing | Perm | Describes the start of the clinical event relative to the sponsor-defined reference period. See Section 4.4.7. |
| 28 | CEENRF | End Relative to Reference Period | Char | C66728 | Timing | Perm | Describes the end of the event relative to the sponsor-defined reference period. See Section 4.4.7. |
| 29 | CESTRTPT | Start Relative to Reference Time Point | Char | C66728 | Timing | Perm | Identifies the start of the observation as being before or after the reference time point defined by variable CESTTPT. See Section 4.4.7. |
| 30 | CESTTPT | Start Reference Time Point | Char | | Timing | Perm | Description or date/time in ISO 8601 of the reference point referred to by CESTRTPT. Examples: "2003-12-15", "VISIT 1". |
| 31 | CEENRTPT | End Relative to Reference Time Point | Char | C66728 | Timing | Perm | Identifies the end of the observation as being before or after the reference time point defined by variable CEENTPT. See Section 4.4.7. |
| 32 | CEENTPT | End Reference Time Point | Char | | Timing | Perm | Description or date/time in ISO 8601 of the reference point referred to by CEENRTPT. Examples: "2003-12-25", "VISIT 2". |

### CE — Assumptions

1. The determination of events to be considered clinical events versus adverse events should be done carefully and with reference to regulatory guidelines or consultation with a regulatory review division. Events of clinical interest as defined by the protocol that are not considered AEs should be reflected as CEs.
   - **(a)** Events considered to be clinical events may include episodes of symptoms of the disease under study (often known as "signs and symptoms"), or events that do not constitute adverse events in themselves, though they might lead to the identification of an adverse event. For example, in a study of an investigational treatment for migraine headaches, migraine headaches may not be considered to be adverse events per protocol.
   - **(b)** In vaccine trials, certain adverse events may be considered to be signs or symptoms and accordingly determined to be clinical events. If any event is considered serious, then the serious variable (--SER) and the serious adverse event flags (--SCAN, --SCONG, --SDTH, --SHOSP, --SDISAB, --SLIFE, --SOD, --SMIE) would be required in the CE domain.
   - **(c)** Other studies might track the occurrence of specific events as efficacy endpoints. For example, in a study of an investigational treatment for prevention of ischemic stroke, all occurrences of TIA, stroke, and death might be captured as clinical events and assessed as to whether they meet endpoint criteria.

2. **CEOCCUR and CEPRESP** are used together to indicate whether the event in CETERM was prespecified and whether it occurred. The following table shows how these variables are populated in various situations:

   | Situation | CEPRESP | CEOCCUR | CESTAT |
   |-----------|---------|---------|--------|
   | Spontaneously reported event occurred | | | |
   | Prespecified event occurred | Y | Y | |
   | Prespecified event did not occur | Y | N | |
   | Prespecified event has no response | Y | | NOT DONE |

3. The collection of write-in events on a CE CRF should be considered with caution. Sponsors must ensure that all adverse events are recorded in the AE domain.

4. Any identifier variable may be added to the CE domain.

5. **Timing variables**
   - **(a)** Relative timing assessments "Prior" or "Ongoing" are common in the collection of CE information. CESTRF or CEENRF may be used when this timing assessment is relative to the study reference period for the subject represented in the Demographics (DM) dataset (RFENDTC). CESTRTPT with CESTTPT and/or CEENRTPT with CEENTPT may be used when "Prior" or "Ongoing" are relative to specific dates other than the start and end of the study reference period. See Section 4.4.7.
   - **(b)** Additional timing variables may be used when appropriate.

6. The clinical events domain is based on the Events general observation class and thus can use any variables in the Events class, including those found in the AE domain specification table.

### CE — Examples

#### Example 1

In this example, data were collected about prespecified events that, in the context of this study, were not reportable as AEs. The data were collected in a log independent of visits, rather than in visit-based CRF modules, so visit and date of collection (CEDTC) data were not collected.

> **CRF:** Record start dates of any of the following signs that occurred during the study.
>
> | Clinical Sign | Did it occur? | Start Date of First Episode |
> |---------------|---------------|-----------------------------|
> | Rash | No / Yes | __ / ___ / ____ |
> | Wheezing | No / Yes | __ / ___ / ____ |
> | Edema | No / Yes | __ / ___ / ____ |
> | Conjunctivitis | No / Yes | __ / ___ / ____ |

- **Rows 1-3:** Show 3 symptoms which occurred and their start dates.
- **Row 4:** Shows that conjunctivitis did not occur. Because there was no event, there is no start date.

**ce.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CESEQ | CETERM | CEPRESP | CEOCCUR | CESTDTC |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|
| 1 | ABC123 | CE | 123 | 1 | Rash | Y | Y | 2006-05-03 |
| 2 | ABC123 | CE | 123 | 2 | Wheezing | Y | Y | 2006-05-03 |
| 3 | ABC123 | CE | 123 | 3 | Edema | Y | Y | 2006-05-03 |
| 4 | ABC123 | CE | 123 | 4 | Conjunctivitis | Y | N | |

#### Example 2

In this example, the CRF included both questions about prespecified clinical events (events not reportable as AEs in the context of this study) and places for specifying additional clinical events. No explicit evaluation interval is given, but the implicit time frame for the question is "during the study."

> **CRF:**
>
> | Event | Date Started | Date Ended | Severity |
> |-------|-------------|------------|----------|
> | Nausea: Yes / No | dd/mmm/yyyy | dd/mmm/yyyy | Mild / Moderate / Severe |
> | Vomit: Yes / No | dd/mmm/yyyy | dd/mmm/yyyy | Mild / Moderate / Severe |
> | Diarrhea: Yes / No | dd/mmm/yyyy | dd/mmm/yyyy | Mild / Moderate / Severe |
> | Other, Specify: _____ | dd/mmm/yyyy | dd/mmm/yyyy | Mild / Moderate / Severe |

- **Rows 1-2:** Show records for 2 instances of the prespecified clinical event, nausea. The CEPRESP value of "Y" indicates that there was a probing question; the response to the probe (CEOCCUR) was "Yes".
- **Row 3:** Shows a record for the prespecified clinical event, vomit. The CEPRESP value of "Y" indicates that there was a probing question; the response to the question (CEOCCUR) was "No". Because there was no event, severity and start and end dates are null.
- **Row 4:** Shows a record for the prespecified clinical event, diarrhea. The value "Y" for CEPRESP indicates it was prespecified. The CESTAT value of NOT DONE indicates that the probing question was not asked or that there was no answer.
- **Row 5:** Shows a record for a write-in clinical event recorded in the "Other, Specify" space. Because this event was not prespecified, CEPRESP and CEOCCUR are null. See Section 4.2.7.3 for further information.

**ce.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CESEQ | CETERM | CEDECOD | CEPRESP | CEOCCUR | CESTAT | CESEV | CESTDTC | CEENDTC |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|--------|-------|---------|---------|
| 1 | ABC123 | CE | 123 | 1 | NAUSEA | Nausea | Y | Y | | MODERATE | 2005-10-12 | 2005-10-12 |
| 2 | ABC123 | CE | 123 | 2 | NAUSEA | Nausea | Y | Y | | MODERATE | 2005-10-14 | 2005-10-15 |
| 3 | ABC123 | CE | 123 | 3 | VOMIT | Vomiting | Y | N | | | | |
| 4 | ABC123 | CE | 123 | 4 | DIARRHEA | Diarrhoea | Y | | NOT DONE | | | |
| 5 | ABC123 | CE | 123 | 5 | SEVERE HEAD PAIN | Headache | | | | SEVERE | 2005-10-09 | 2005-10-11 |

#### Example 3 — Bone Fracture Study

In this study, a prior fracture in the previous 5 years was a requirement for study entry. Details about bone-fracture events were collected about pre-study fractures in the previous 5 years, and about any fracture events that occurred during the study.

> **CRF — Bone Fracture Assessment:**
>
> | Question | Options |
> |----------|---------|
> | Which fracture? | Pre-study fracture, reference number___ / On-study fracture, reference number___ |
> | Date of collection | dd/mmm/yyyy |
> | Date of fracture | dd/mmm/yyyy |
> | How did fracture occur? | Pathologic / Fall / Other trauma / Unknown |
> | What was the location of the fracture? | _____ |
> | What was the laterality? | Left / Right / Not applicable |
> | Were therapeutic measures required? | Yes / No / Unknown |
> | If therapeutic measures were required, select all that apply. | Casting/immobilization / Traction / Surgery |
> | Were there any complications of the fracture? | Yes / No / Unknown |
> | If there were complications, select all that apply. | Infection of fracture site / Improper healing requiring bone reset / Soft tissue damage, specify location _____ |

The collected data do not meet criteria for representation in FA. Data about the most recent pre-study fracture were represented in the Medical History (MH) domain, and data about fractures during the study were represented in the CE domain.

The supplemental qualifier MHCAUSE or CECAUSE (depending on domain) was used to represent the response to the question, "How did the fracture occur?" The supplemental qualifier MHCPLIND or CECPLIND (depending on domain) was used to represent the response to the question, "Were there any complications of the fracture?" The codelist used for AECONTRT (NY) was used for MHCONTRT and CECONTRT.

- **Row 1:** The subject had only 1 fracture in the last 5 years. This fracture required treatment (MHCONTRT = "Y").
- **Row 2:** This subject had a complication (see supplemental qualifier MHCPLIND in suppmh.xpt dataset), which was represented as a separate medical history event. MHGRPID was used to group this with the fracture for which it was a complication. No separate start date for this complication was collected, so MHSTDTC is blank.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHGRPID | MHSPID | MHTERM | MHCAT | MHSCAT | MHPRESP | MHOCCUR | MHLOC | MHLAT | MHCONTRT | MHDTC | MHSTDTC | MHEVLINT |
|-----|---------|--------|---------|-------|---------|--------|--------|-------|--------|---------|---------|-------|-------|----------|-------|---------|----------|
| 1 | ABC | MH | ABC-US-701-002 | 1 | 1 | MH1 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | RIB 3 | RIGHT | Y | 2006-05-13 | 2005-08-18 | -P5Y |
| 2 | ABC | MH | ABC-US-701-002 | 2 | 1 | | Soft Tissue Damage | FRACTURE-RELATED EVENTS | COMPLICATIONS | Y | Y | LUNG | | | 2006-05-13 | | |

The cause of the fracture and whether there were complications were represented as supplemental qualifiers.

**suppmh.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | MH | 001-001 | MHSEQ | 1 | MHCAUSE | Cause of Event | OTHER TRAUMA | CRF | |
| 2 | ABC | MH | 001-001 | MHSEQ | 1 | MHCPLIND | Complications Indicator | Y | CRF | |

The subject had 2 on-study fractures.

- **Row 1:** Shows the subject's first on-study fracture. Although it healed normally (as indicated by the lack of complications, supplemental qualifier CECPLIND = "N"), it required additional treatment, as indicated by CECONTRT = "Y".
- **Rows 2-3:** Show the subject's second fracture and its associated complication. The 2 events were linked using CEGRPID.

**ce.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CESEQ | CEGRPID | CESPID | CETERM | CECAT | CESCAT | CEPRESP | CEOCCUR | CELOC | CELAT | CECONTRT | CEDTC | CESTDTC |
|-----|---------|--------|---------|-------|---------|--------|--------|-------|--------|---------|---------|-------|-------|----------|-------|---------|
| 1 | ABC | CE | ABC-US-701-002 | 1 | | CE1 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | HUMERUS | RIGHT | Y | 2006-07-09 | 2006-07-03 |
| 2 | ABC | CE | ABC-US-701-002 | 2 | 1 | CE2 | Fracture | FRACTURE-RELATED EVENTS | | Y | Y | FIBULA | LEFT | N | 2006-10-23 | 2006-10-15 |
| 3 | ABC | CE | ABC-US-701-002 | 3 | 1 | CE3 | Infection of fracture site | FRACTURE-RELATED EVENTS | COMPLICATIONS | Y | Y | | | | 2006-10-23 | |

The causes of the fractures and whether there were complications were represented as supplemental qualifiers.

**suppce.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | CE | 001-001 | CESEQ | 1 | CECAUSE | Cause of Event | FALL | CRF | |
| 2 | ABC | CE | 001-001 | CESEQ | 1 | CECPLIND | Complications Indicator | N | CRF | |
| 3 | ABC | CE | 001-001 | CESEQ | 2 | CECAUSE | Cause of Event | OTHER TRAUMA | CRF | |
| 4 | ABC | CE | 001-001 | CESEQ | 2 | CECPLIND | Complications Indicator | Y | CRF | |

The therapeutic measures in this example were procedures represented in the Procedures (PR) domain. PRSTDTC is an expected variable, so it is included in the dataset, although it was not collected in this study.

- **Row 1:** The subject's pre-study fracture required one of the prespecified therapeutic procedures. The sponsor populated PRSPID with the value in MHSPID for the fracture. PRDTC is populated with the date on which medical history was collected, which also appeared in MHDTC.
- **Rows 2-3:** The subject's first on-study fracture required 2 of the prespecified therapeutic procedures. For these procedures, PRSPID was populated with a CESPID value. PRDTC is the same as CEDTC for the associated fracture.

**pr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRSPID | PRTRT | PRCAT | PRPRESP | PROCCUR | PRDTC | PRSTDTC |
|-----|---------|--------|---------|-------|--------|-------|-------|---------|---------|-------|---------|
| 1 | ABC | PR | ABC-US-701-002 | 1 | MH1 | Casting/Immobilization | FRACTURE TREATMENTS | Y | Y | 2006-05-13 | |
| 2 | ABC | PR | ABC-US-701-002 | 2 | CE1 | Surgery | FRACTURE TREATMENTS | Y | Y | 2006-07-09 | |
| 3 | ABC | PR | ABC-US-701-002 | 3 | CE1 | Traction | FRACTURE TREATMENTS | Y | Y | 2006-07-09 | |

The therapeutic measures are linked to the fracture events in the RELREC dataset. The sponsor anticipated the need to link procedures either to an MH record or a CE record, so included domain prefixes in the values of MHSPID and CESPID and used those in populating PRSPID.

- **Rows 1-2:** Show the dataset-to-dataset relationship between MH and PR records.
- **Rows 3-4:** Show the relationship between CE and PR records.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | MH | | MHSPID | | ONE | 1 |
| 2 | ABC | PR | | PRSPID | | MANY | 1 |
| 3 | ABC | CE | | CESPID | | ONE | 2 |
| 4 | ABC | PR | | PRSPID | | MANY | 2 |

---

