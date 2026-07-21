# SDTM v2.0 — Study Data Tabulation Model — Part 2

> **Source:** SDTM_v2.0.pdf | **Version:** 2.0 Final | **Date:** 2021-11-29
> **Publisher:** CDISC Submission Data Standards Team
> **Purpose:** Complete specification text optimized for search and retrieval
> **Split:** Part 2/2 — Sections 3.2-9: Special-purpose Domains, Associated Persons, Study-level Data, Relationships, Appendices
> **Original:** `SDTM20_FullText.md`
> **Related:** `SDTM20a_FullText.md`

---

## 3.2 Special-purpose Domains

### 3.2.1 Demographics


**Demographics Domain Variables—One Record per Subject**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | SUBJID | Subject Identifier for the Study | Char | Topic |  |  |  |
| 5 | RFSTDTC | Subject Reference Start Date/Time | Char | Record Qualifier |  |  | C83395 |
| 6 | RFENDTC | Subject Reference End Date/Time | Char | Record Qualifier |  |  | C83394 |
| 7 | RFXSTDTC | Date/Time of First Study Treatment | Char | Record Qualifier |  |  | C170502 |
| 8 | RFXENDTC | Date/Time of Last Study Treatment | Char | Record Qualifier |  |  | C170501 |
| 9 | RFCSTDTC | Date/Time of First Challenge Agent Admin | Char | Record Qualifier |  |  |  |
| 10 | RFCENDTC | Date/Time of Last Challenge Agent Admin | Char | Record Qualifier |  |  |  |
| 11 | RFICDTC | Date/Time of Informed Consent | Char | Record Qualifier |  | Not in nonclinical trials | C117452 |
| 12 | RFPENDTC | Date/Time of End of Participation | Char | Record Qualifier |  | Not in nonclinical trials | C117453 |
| 13 | DTHDTC | Date/Time of Death | Char | Record Qualifier |  | Not in nonclinical trials | C117450 |
| 14 | DTHFL | Subject Death Flag | Char | Record Qualifier |  | Not in nonclinical trials | C117451 |
| 15 | SITEID | Study Site Identifier | Char | Record Qualifier |  |  | C83081 |
| 16 | INVID | Investigator Identifier | Char | Record Qualifier |  | Not in nonclinical trials |  |
| 17 | INVNAM | Investigator Name | Char | Synonym Qualifier | INVID | Not in nonclinical trials |  |
| 18 | BRTHDTC | Date/Time of Birth | Char | Record Qualifier |  |  | C83217 |
| 19 | AGE | Age | Num | Record Qualifier |  |  | C170981 |
| 20 | AGETXT | Age Text | Char | Record Qualifier |  |  | C170982 |
| 21 | AGEU | Age Units | Char | Variable Qualifier | AGE; AGETXT |  | C50400 |
| 22 | SEX | Sex | Char | Record Qualifier |  |  |  |
| 23 | RACE | Race | Char | Record Qualifier |  | Not in nonclinical trials |  |
| 24 | ETHNIC | Ethnicity | Char | Record Qualifier |  | Not in nonclinical trials |  |
| 25 | SPECIES | Species | Char | Record Qualifier |  | Not in human clinical trials | C96433 |
| 26 | STRAIN | Strain/Substrain | Char | Record Qualifier |  | Not in human clinical trials | C14419 |
| 27 | SBSTRAIN | Strain/Substrain Details | Char | Variable Qualifier | STRAIN | Not in human clinical trials | C90460 |
| 28 | ARMCD | Planned Arm Code | Char | Record Qualifier |  |  | C83216 |
| 29 | ARM | Description of Planned Arm | Char | Synonym Qualifier | ARMCD |  | C170984 |
| 30 | ACTARMCD | Actual Arm Code | Char | Record Qualifier |  | Not in nonclinical trials | C117449 |
| 31 | ACTARM | Description of Actual Arm | Char | Synonym Qualifier | ACTARMCD | Not in nonclinical trials | C117448 |
| 32 | ARMNRS | Reason Arm and/or Actual Arm is Null | Char | Record Qualifier |  |  |  |
| 33 | ACTARMUD | Description of Unplanned Actual Arm | Char | Record Qualifier |  |  |  |
| 34 | SETCD | Set Code | Char | Record Qualifier |  |  | C117457 |
| 35 | RPATHCD | Planned Repro Path Code | Char | Record Qualifier |  | Not in human clinical trials | C170503 |
| 36 | COUNTRY | Country | Char | Record Qualifier |  | Not in nonclinical trials | C170990 |
| 37 | DMDTC | Date/Time of Collection | Char | Timing |  |  | C83243 |
| 38 | DMDY | Study Day of Collection | Num | Timing |  |  | C83244 |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "DM".
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SUBJID**: *Notes:* Subject identifier, which must be unique within the study. Often the ID of the subject as recorded on a CRF.
- **RFSTDTC**: The start date or date and time of the sponsor-defined study reference period, represented in a standardized character format. | *Notes:* Usually equivalent to date/time when subject was first exposed to study treatment. Required for all randomized subjects; will be null for all subjects who did not meet the milestone the date requires, such as screen failures or unassigned subjects.
- **RFENDTC**: The end date or date and time of the sponsor-defined study reference period, represented in a standardized character format. | *Notes:* Usually equivalent to the date/time when a subject was determined to have ended the trial. Often equivalent to either date/time of last exposure to study treatment or date/time of last contact with the subject. Required for all randomized subjects;
- **RFXSTDTC**: The start date or date and time of the first exposure to any protocol- specified treatment or therapy, represented in a standardized character format.
- **RFXENDTC**: The end date or date and time of the last exposure to any protocol- specified treatment or therapy, represented in a standardized character format.
- **RFCSTDTC**: *Notes:* The start date or date and time of the first exposure to any protocol-specified challenge agent that induces the disease or condition that the investigational treatment is intended to cure, mitigate, treat, or prevent, represented in a standardized character format. Equal to the earliest value of AGSTDTC for the challenge agent.
- **RFCENDTC**: *Notes:* The end date or date and time of the last exposure to any protocol-specified challenge agent that induces the disease or condition that the investigational treatment is intended to cure, mitigate, treat, or prevent, represented in a standardized character format. Equal to the latest value of AGENDTC for the challenge agent.
- **RFICDTC**: The date or date and time of informed consent, represented in a standardized character format.
- **RFPENDTC**: The date or date and time of last contact with or information about a subject in a trial, represented in a standardized character format. | *Notes:* Should correspond to the last known date of contact.
- **DTHDTC**: The date or date and time of death, represented in a standardized character format. | *Notes:* Should represent the date/time that is captured in the clinical-trial database.
- **DTHFL**: An indication that the subject died. | *Notes:* A value of "Y" indicates the subject died. Should be "Y" or null. Should be populated even when the death date is unknown.
- **SITEID**: A sequence of characters used to uniquely identify the facility associated with study-specific activities.
- **INVID**: *Notes:* An identifier to describe the Investigator for the study. May be used in addition to the SITEID. Not needed if SITEID is equivalent to INVID.
- **INVNAM**: *Notes:* Name of the investigator for a site.
- **BRTHDTC**: The date or date and time of birth, represented in a standardized character format.
- **AGE**: A numeric representation of the elapsed time since birth at a specific point in time defined for the trial, used for study data tabulation. | *Notes:* May be derived as (RFSTDTC-BRTHDTC), but BRTHDTC may not be available in all cases (due to subject privacy concerns).
- **AGETXT**: The age at a specific point in time defined for the trial, expressed as a range. | *Notes:* The age of the subject at study start, as planned, expressed as a range. If an age integer value is available, then populate the age variable instead. Either the AGE or AGETXT variable should be populated, but not both.
- **AGEU**: The unit of time used to express the age, using standardized values.
- **SEX**: *Notes:* Sex of the subject.
- **RACE**: *Notes:* Race of the subject. Sponsors should refer to FDA guidance regarding the collection of race data.
- **ETHNIC**: *Notes:* The ethnicity of the subject. Sponsors should refer to FDA guidance regarding the collection of ethnicity data.
- **SPECIES**: The common (non-taxonomic) name for an animal used as the test system in a study. | *Examples:* "MOUSE", "RAT", "DOG", "MONKEY"
- **STRAIN**: The vendor-supplied species/strain/substrain designation for the test system under study. It may | *Examples:* "C57BL/6", "A/J", "B6.129- Pparg<tm2Rev>/J",
- **SBSTRAIN**: Additional clarifying details regarding the test system under study, such as a description of a phenotypic alteration associated with the specific genetic modification captured or collected in the Strain/Substrain variable.
- **ARMCD**: A short sequence of characters that represents the planned arm to which the subject was assigned. | *Notes:* Limited to 20 characters.
- **ARM**: The name of the planned arm to which the subject was assigned.
- **ACTARMCD**: A short sequence of characters that represents the arm in which the subject actually participated. | *Notes:* Limited to 20 characters.
- **ACTARM**: The name of the arm in which the subject actually participated.
- **ARMNRS**: *Notes:* The reason why the actual arm variables are null or why both the planned and actual arm variables are null. It is assumed that if the arm and actual arm variables are null, the same reason applies to both. | *Examples:* "SCREEN FAILURE", "NOT ASSIGNED", "NOT TREATED", "UNPLANNED TREATMENT"
- **ACTARMUD**: *Notes:* A description of actual treatment for a subject who did not receive treatment described in one of the planned trial arms.
- **SETCD**: The standardized or dictionary- derived short sequence of characters used to represent the trial set. | *Notes:* Defined by the sponsor (see Section 5.1.2, Trial Sets). Maximum of 8 characters. This represents the code for the trial set for which parameters are being submitted.
- **RPATHCD**: A short sequence of characters that represents the planned reproductive path to which the subject was assigned. | *Notes:* Limited to 20 characters.
- **COUNTRY**: The country in which the investigational site is located.
- **DMDTC**: The date or date and time of demographic data collection,
- **DMDY**: The actual study day of demographic data collection derived relative to the sponsor-defined reference start date. | *Notes:* The sponsor-defined reference start date is RFSTDTC.

### 3.2.2 Comments

Comments are collected during the conduct of many studies. When collected, comments should be submitted in a single Comments domain.


**Comments Domain Variables**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | RDOMAIN | Related Domain Abbreviation | Char | Record Qualifier |  |  |  |
| 4 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 5 | POOLID | Pool Identifier | Char | Identifier |  |  | C117053 |
| 6 | SPDEVID | Sponsor Device Identifier | Char | Identifier |  |  | C117060 |
| 7 | COSEQ | Sequence Number | Num | Identifier |  |  |  |
| 8 | IDVAR | Identifying Variable | Char | Record Qualifier |  |  |  |
| 9 | IDVARVAL | Identifying Variable Value | Char | Record Qualifier |  |  |  |
| 10 | COREF | Comment Reference | Char | Record Qualifier |  |  |  |
| 11 | COVAL | Comment | Char | Topic |  |  |  |
| 12 | COEVAL | Evaluator | Char | Record Qualifier |  |  |  |
| 13 | COEVALID | Evaluator Identifier | Char | Variable Qualifier | COEVAL |  |  |
| 14 | CODTC | Date/Time of Comment | Char | Timing |  |  |  |
| 15 | CODY | Study Day of Comment | Num | Timing |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "CO".
- **RDOMAIN**: *Notes:* Domain abbreviation of the parent record(s). Null for records collected on general comments or additional information section of CRF.
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **POOLID**: A sequence of characters used to uniquely identify a group of subjects that have been pooled together. | *Notes:* The result is not assignable to any one individual.
- **SPDEVID**: A sequence of characters used by the sponsor to uniquely identify a specific device.
- **COSEQ**: *Notes:* Sequence number to ensure uniqueness within the dataset.
- **IDVAR**: *Notes:* Identifying variable in the parent dataset that identifies the record(s) to which the comment applies (e.g., AESEQ, CMGRPID). Used only when individual comments are
- **IDVARVAL**: *Notes:* Value of identifying variable of the parent record(s). Null for comments collected on separate CRFs.
- **COREF**: *Notes:* Sponsor-defined reference associated with the comment. | *Examples:* A CRF page number (e.g., 650), a module name (e.g., "DEMOG"), or a combination of information that identifies the reference (e.g., "650-VITALS- VISIT 2")
- **COVAL**: *Notes:* The text of the comment. Text over 200 characters can be added to additional columns COVAL1- COVALn.
- **COEVAL**: *Notes:* Used to describe the originator of the comment. | *Examples:* "CENTRAL REVIEWER"
- **COEVALID**: *Notes:* Used to distinguish multiple evaluators with the same role recorded in --EVAL. | *Examples:* "RADIOLOGIST1", "RADIOLOGIST2"
- **CODTC**: *Notes:* Date or date and time of comment on dedicated comment form, if collected. Should be null if this is a child record of another domain or if comment date was not collected.
- **CODY**: *Notes:* Actual study day of the comment, in integer days. The algorithm for calculations must be relative to the sponsor-defined RFSTDTC variable in the Demographics (DM) domain.

### 3.2.3 Subject Summary Domains

#### 3.2.3.1 Subject Elements

Describes the actual order of elements traversed by the subject, together with start/end date/time for each.


**Subject Elements—One Record per Actual Element per Subject**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | SESEQ | Sequence Number | Num | Identifier |  |  |  |
| 5 | ETCD | Element Code | Char | Topic |  |  |  |
| 6 | ELEMENT | Description of Element | Char | Synonym Qualifier | ETCD |  |  |
| 7 | TAETORD | Planned Order of Element within Arm | Num | Timing |  |  | C83438 |
| 8 | EPOCH | Epoch | Char | Timing |  |  | C71738 |
| 9 | SESTDTC | Start Date/Time of Element | Char | Timing |  |  |  |
| 10 | SEENDTC | End Date/Time of Element | Char | Timing |  |  |  |
| 11 | SESTDY | Study Day of Start of Element | Num | Timing |  |  |  |
| 12 | SEENDY | Study Day of End of Element | Num | Timing |  |  |  |
| 13 | SEUPDES | Description of Unplanned Element | Char | Synonym Qualifier | ETCD |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic- specific commonality. | *Notes:* 2-character abbreviation, which must be "SE".
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SESEQ**: *Notes:* Sequence number to ensure uniqueness within the dataset. Should be assigned to be in a consistent chronological order.
- **ETCD**: *Notes:* ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.
- **ELEMENT**: *Notes:* The name of the element. If ETCD has a value of "UNPLAN" then ELEMENT should be null.
- **TAETORD**: An assigned numeric identifier that gives the planned order of the element within the trial arm of the study. | *Notes:* Value for the element within the subject's assigned arm.
- **EPOCH**: A time period defined in the protocol with a study-specific purpose. | *Notes:* Value for the element within the subject's assigned arm.
- **SESTDTC**: *Notes:* Start date or start date and time for an element for each subject.
- **SEENDTC**: *Notes:* End date/time of an element for each subject.
- **SESTDY**: *Notes:* Study day of start of element relative to the sponsor-defined RFSTDTC.
- **SEENDY**: *Notes:* Study day of end of element relative to the sponsor-defined RFSTDTC.
- **SEUPDES**: *Notes:* Description of what happened to the subject during an unplanned element. Used only if ETCD has the value of "UNPLAN".

#### 3.2.3.2 Subject Repro Stages

Not for use with human clinical trials. Describes actual order of repro stages experienced by the subject.


**Subject Repro Stages—One Record per Actual Repro Stage per Subject**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | SESEQ | Sequence Number | Num | Identifier |  |  |  |
| 5 | ETCD | Element Code | Char | Topic |  |  |  |
| 6 | ELEMENT | Description of Element | Char | Synonym Qualifier | ETCD |  |  |
| 7 | TAETORD | Planned Order of Element within Arm | Num | Timing |  |  | C83438 |
| 8 | EPOCH | Epoch | Char | Timing |  |  | C71738 |
| 9 | SESTDTC | Start Date/Time of Element | Char | Timing |  |  |  |
| 10 | SEENDTC | End Date/Time of Element | Char | Timing |  |  |  |
| 11 | SESTDY | Study Day of Start of Element | Num | Timing |  |  |  |
| 12 | SEENDY | Study Day of End of Element | Num | Timing |  |  |  |
| 13 | SEUPDES | Description of Unplanned Element | Char | Synonym Qualifier | ETCD |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic- specific commonality. | *Notes:* 2-character abbreviation, which must be "SE".
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SESEQ**: *Notes:* Sequence number to ensure uniqueness within the dataset. Should be assigned to be in a consistent chronological order.
- **ETCD**: *Notes:* ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.
- **ELEMENT**: *Notes:* The name of the element. If ETCD has a value of "UNPLAN" then ELEMENT should be null.
- **TAETORD**: An assigned numeric identifier that gives the planned order of the element within the trial arm of the study. | *Notes:* Value for the element within the subject's assigned arm.
- **EPOCH**: A time period defined in the protocol with a study-specific purpose. | *Notes:* Value for the element within the subject's assigned arm.
- **SESTDTC**: *Notes:* Start date or start date and time for an element for each subject.
- **SEENDTC**: *Notes:* End date/time of an element for each subject.
- **SESTDY**: *Notes:* Study day of start of element relative to the sponsor-defined RFSTDTC.
- **SEENDY**: *Notes:* Study day of end of element relative to the sponsor-defined RFSTDTC.
- **SEUPDES**: *Notes:* Description of what happened to the subject during an unplanned element. Used only if ETCD has the value of "UNPLAN".

#### 3.2.3.3 Subject Visits

Describes actual start and end date/time for each visit of each individual subject.


**Subject Visits—One Record per Subject Visit, per Subject**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | VISITNUM | Visit Number | Num | Topic |  |  | C83101 |
| 5 | VISIT | Visit Name | Char | Synonym Qualifier | VISITNUM |  | C171010 |
| 6 | SVPRESP | Pre-Specified | Char | Variable Qualifier | VISITNUM |  |  |
| 7 | SVOCCUR | Occurrence | Char | Record Qualifier |  |  |  |
| 8 | SVREASOC | Reason for Occur Value | Char | Record Qualifier |  |  |  |
| 9 | SVCNTMOD | Contact Mode | Char | Record Qualifier |  |  |  |
| 10 | SVEPCHGI | Epi/Pandemic Related Change Indicator | Char | Record Qualifier |  |  |  |
| 11 | VISITDY | Planned Study Day of Visit | Num | Timing |  |  | C171011 |
| 12 | SVSTDTC | Start Date/Time of Visit | Char | Timing |  |  |  |
| 13 | SVENDTC | End Date/Time of Visit | Char | Timing |  |  |  |
| 14 | SVSTDY | Study Day of Start of Visit | Num | Timing |  |  |  |
| 15 | SVENDY | Study Day of End of Visit | Num | Timing |  |  |  |
| 16 | SVUPDES | Description of Unplanned Visit | Char | Record Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "SV".
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **VISITNUM**: An assigned numeric identifier that aligns to the chronological order of a clinical encounter. | *Notes:* Decimal numbering may be useful for inserting unplanned visits. Used for sorting.
- **VISIT**: The label for a protocol-defined clinical encounter. | *Notes:* May be used in addition to VISITNUM and/or VISITDY.
- **SVPRESP**: *Notes:* An indication that the visit is planned. Values should be "Y" or null.
- **SVOCCUR**: *Notes:* An indication as to whether a prespecified (planned) visit has occurred.
- **SVREASOC**: *Notes:* The reason for the value in SVOCCUR. If SVOCCUR="N", SVREASOC is the reason the visit did not occur.
- **SVCNTMOD**: *Notes:* The way in which the visit or contact was conducted. | *Examples:* "IN PERSON", "TELEPHONE", "IVRS".
- **SVEPCHGI**: *Notes:* Indicates whether the visit was changed due to an epidemic or pandemic.
- **VISITDY**: The planned study day of a clinical encounter relative to the sponsor-defined reference start date. | *Notes:* The reference start date is RFSTDTC in Demographics.
- **SVSTDTC**: *Notes:* Start date or start date and time for a subject's visit.
- **SVENDTC**: *Notes:* End date/time of a subject's visit.
- **SVSTDY**: *Notes:* Study day of start of visit relative to the sponsor-defined RFSTDTC.
- **SVENDY**: *Notes:* Study day of end of visit relative to the sponsor-defined RFSTDTC.
- **SVUPDES**: *Notes:* Description of what happened to the subject during an unplanned visit. Null for protocol-defined visits.

#### 3.2.3.4 Subject Disease Milestones

Records the timing, for each subject, of defined trial disease milestones.


**Subject Disease Milestones—One Record per Disease Milestone, per Subject**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | SMSEQ | Sequence Number | Num | Identifier |  |  |  |
| 5 | MIDS | Disease Milestone Instance Name | Char | Topic |  |  |  |
| 6 | MIDSTYPE | Disease Milestone Type | Char | Record Qualifier |  |  |  |
| 7 | SMSTDTC | Start Date/Time of Milestone | Char | Timing |  |  |  |
| 8 | SMENDTC | End Date/Time of Milestone | Char | Timing |  |  |  |
| 9 | SMSTDY | Study Day of Start of Milestone | Num | Timing |  |  |  |
| 10 | SMENDY | Study Day of End of Milestone | Num | Timing |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "SM".
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SMSEQ**: *Notes:* Sequence number given to ensure uniqueness of subject records. Should be assigned to be consistent with chronological order.
- **MIDS**: *Notes:* Name of the specific disease milestone. For disease milestones that can occur multiple times, the name will end with a sequence number. | *Examples:* "HYPO1"
- **MIDSTYPE**: *Notes:* The type of disease milestone. | *Examples:* "HYPOGLYCEMIC EVENT"
- **SMSTDTC**: *Notes:* Start date or start date and time of milestone instance (if milestone is an intervention or event), or date of milestone if the milestone is a finding.
- **SMENDTC**: *Notes:* End date/time of disease milestone Instance.
- **SMSTDY**: *Notes:* Study day of start of disease milestone instance, relative to the sponsor-defined RFSTDTC.
- **SMENDY**: *Notes:* Study day of end of disease milestone instance, relative to the sponsor-defined RFSTDTC.

---

# 4 Associated Persons Data

Associated persons are individuals other than study subjects who can be associated with a study, a particular study subject, or a device used in the study.

- AP will be the prefix for the domain and dataset name
- The Associated Persons Identifier (APID) will be required in all AP datasets
- The SDTMIG-AP provides implementation rules, advice, and examples


**Associated Persons—Additional Identifier Variables**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | APID | Associated Persons Identifier | Char | Identifier |  |  |  |
| 2 | RSUBJID | Related Subject or Pool Identifier | Char | Identifier |  |  |  |
| 3 | RDEVID | Related Device Identifier | Char | Identifier |  |  |  |
| 4 | SREL | Subject, Device, or Study Relationship | Char | Identifier |  |  |  |

**Variable Definitions:**

- **APID**: *Notes:* Identifier for a single associated person, a group of associated persons, or a pool of associated persons. If APID identifies a pool, POOLDEF records must exist for each associated person (see Section 6.3, Pool Definition Dataset, and Section 4, Associated Persons Data).
- **RSUBJID**: *Notes:* Identifier for a related subject or pool of subjects. RSUBJID may be populated with the USUBJID of the related subject or the POOLID of the related pool. RSUBJID will be null for data about associated persons who are related to the study but not to any study subjects.
- **RDEVID**: *Notes:* Identifier for a related device. RDEVID will be populated with the SPDEVID of the related device.
- **SREL**: *Notes:* If RSUBJID is populated, describes the relationship of the associated person(s) identified in APID to the subject or pool identified in RSUBJID. If RDEVID is populated, describes the relationship of the associated person(s) identified in APID to the device identified in RDEVID. If RSUBJID and RDEVID are null, SREL describes the relationship of the associated person(s) identified in APID to the study identified in STUDYID.

---

# 5 Study-level Data

The SDTM includes 2 types of study-level data: trial design data and study reference data.

## 5.1 The Trial Design Model

Defines a standard structure for representing the planned sequence of activities and the treatment plan.

#### 5.1.1.1 Trial Elements


**Trial Elements—One Record per Element**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | ETCD | Element Code | Char | Topic |  |  |  |
| 4 | ELEMENT | Description of Element | Char | Synonym Qualifier | ETCD |  |  |
| 5 | TESTRL | Rule for Start of Element | Char | Rule |  |  |  |
| 6 | TEENRL | Rule for End of Element | Char | Rule |  |  |  |
| 7 | TEDUR | Planned Duration of Element | Char | Timing |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "TE".
- **ETCD**: *Notes:* ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character
- **ELEMENT**: *Notes:* The name of the element.
- **TESTRL**: *Notes:* Expresses the rule for beginning the element.
- **TEENRL**: *Notes:* Expresses the rule for ending the element. Either TEENRL or TEDUR must be present for each element.
- **TEDUR**: *Notes:* Used when the rule for ending the element is applied after a fixed duration.

#### 5.1.1.2 Trial Arms


**Trial Arms—One Record per Planned Element per Arm**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | ARMCD | Planned Arm Code | Char | Topic |  |  | C83216 |
| 4 | ARM | Description of Planned Arm | Char | Synonym Qualifier | ARMCD |  | C170984 |
| 5 | TAETORD | Planned Order of Element within Arm | Num | Timing |  |  | C83438 |
| 6 | ETCD | Element Code | Char | Record Qualifier |  |  |  |
| 7 | ELEMENT | Description of Element | Char | Synonym Qualifier | ETCD |  |  |
| 8 | TABRANCH | Branch | Char | Rule |  |  |  |
| 9 | TATRANS | Transition Rule | Char | Rule |  |  |  |
| 10 | EPOCH | Epoch | Char | Timing |  |  | C71738 |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "TA".
- **ARMCD**: A short sequence of characters that represents the planned arm to which the subject was assigned. | *Notes:* ARMCD is limited to 20 characters and does not have special character restrictions.
- **ARM**: The name of the planned arm to which the subject was assigned.
- **TAETORD**: An assigned numeric identifier that gives the planned order of the element within the trial arm of the study.
- **ETCD**: *Notes:* ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.
- **ELEMENT**: *Notes:* The name of the element.
- **TABRANCH**: *Notes:* Condition subjects meet, at a "branch" in the trial design at the end of this element, to be included in this arm. | *Examples:* "Randomization to DRUG X"
- **TATRANS**: *Notes:* If the trial design allows a subject to transition to an element other than the next element in sequence, then the conditions for transitioning to those other elements, and the alternative element sequences, are specified in this rule. | *Examples:* "Responders go to washout"
- **EPOCH**: A time period defined in the protocol with a study- specific purpose. | *Notes:* The epoch associated with the value in ELEMENT and the value in ARMCD.

### 5.1.2 Trial Sets


**Trial Sets—One Record per Trial Set Parameter per Set**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | SETCD | Set Code | Char | Identifier |  |  |  |
| 4 | SET | Set Description | Char | Synonym Qualifier | SETCD |  |  |
| 5 | TXSEQ | Sequence Number | Num | Identifier |  |  |  |
| 6 | TXPARMCD | Trial Set Parameter Short Name | Char | Topic |  |  |  |
| 7 | TXPARM | Trial Set Parameter | Char | Synonym Qualifier | TXPARMCD |  |  |
| 8 | TXVAL | Trial Set Parameter Value | Char | Result Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "TX".
- **SETCD**: *Notes:* Short name of a specific trial set, as defined by the sponsor. Maximum 8 characters. This represents the trial set for which parameters are being submitted.
- **SET**: *Notes:* Long description of a specific trial set, as defined by the sponsor.
- **TXSEQ**: *Notes:* Unique number for this record within this dataset.
- **TXPARMCD**: *Notes:* Short character value for the trial set parameter described in TXPARM. Maximum 8 characters.
- **TXPARM**: *Notes:* Term for the trial set parameter. Maximum 40 characters.
- **TXVAL**: *Notes:* Value of the trial set parameter. Some parameters may be subject to controlled terminology. | *Examples:* "Fed ad libitum" or "Restricted Feeding" when TXPARM is "FEEDREG"

#### 5.1.3.1 Trial Repro Stages


**Trial Repro Stages—One Record per Planned Repro Stage**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | RSTGCD | Repro Stage Code | Char | Topic |  | Not in human clinical trials |  |
| 4 | RSTAGE | Description of Repro Stage | Char | Synonym Qualifier | RSTGCD | Not in human clinical trials |  |
| 5 | TTSTRL | Rule for Start of Repro Stage | Char | Rule |  | Not in human clinical trials |  |
| 6 | TTENRL | Rule for End of Repro Stage | Char | Rule |  | Not in human clinical trials |  |
| 7 | TTDUR | Planned Duration of Repro Stage | Char | Timing |  | Not in human clinical trials |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: A sequence of characters used by the sponsor to uniquely identify the study. | *Notes:* 2-character abbreviation, which must be "TT".
- **RSTGCD**: *Notes:* Short name of the repro stage, used for programming and sorting. Maximum 8 characters.
- **RSTAGE**: *Notes:* The name of the repro stage.
- **TTSTRL**: *Notes:* Expresses the rule for beginning the repro stage.
- **TTENRL**: *Notes:* Expresses the rule for ending the repro stage. Either TTENRL or TTDUR must be present for each repro stage.
- **TTDUR**: *Notes:* Used when the rule for ending the repro stage is applied after a fixed duration.

#### 5.1.3.2 Trial Repro Paths


**Trial Repro Paths—One Record per Planned Repro Path**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | RPATHCD | Planned Repro Path Code | Char | Topic |  | Not in human clinical trials | C170503 |
| 4 | RPATH | Description of Planned Repro Path | Char | Synonym Qualifier | RPATHCD | Not in human clinical trials |  |
| 5 | TPSTGORD | Order of Repro Stage within Repro Path | Num | Timing |  | Not in human clinical trials |  |
| 6 | RSTGCD | Repro Stage Code | Char | Topic |  | Not in human clinical trials |  |
| 7 | RSTAGE | Description of Repro Stage | Char | Synonym Qualifier | RSTGCD | Not in human clinical trials |  |
| 8 | TPBRANCH | Branch | Char | Rule |  | Not in human clinical trials |  |
| 9 | RPHASE | Repro Phase | Char | Timing |  | Not in human clinical trials |  |
| 10 | RPRFDY | Repro Phase Start Reference Day | Num | Timing |  | Not in human clinical trials |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "TP".
- **RPATHCD**: A short sequence of characters that represents the planned reproductive path to which the subject was assigned. | *Notes:* Limited to 20 characters. Should be populated in Demographics when repro paths have been defined in this domain.
- **RPATH**: *Notes:* Name of the planned repro path.
- **TPSTGORD**: *Notes:* Number that gives the planned order of the repro stage within the repro path.
- **RSTGCD**: *Notes:* Short name of the repro stage used for programming and sorting. Maximum 8 characters. The values of RSTGCD used in the Trial Paths dataset must match values for the same repro stage in the Trial Stages dataset.
- **RSTAGE**: *Notes:* The name of the repro stage.
- **TPBRANCH**: *Notes:* Conditions subjects meet, occurring at the end of a repro stage, which cause a repro path to branch off from another repro path.
- **RPHASE**: *Notes:* Name of the reproductive phase with which this repro stage of the repro path is associated.
- **RPRFDY**: *Notes:* Sponsor protocol-defined first day of repro phase. Should be zero or 1.

#### 5.1.4.1 Trial Visits


**Trial Visits—One Record per Planned Visit per Arm**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | VISITNUM | Visit Number | Num | Topic |  |  | C83101 |
| 4 | VISIT | Visit Name | Char | Synonym Qualifier | VISITNUM |  | C171010 |
| 5 | VISITDY | Planned Study Day of Visit | Num | Timing |  |  | C171011 |
| 6 | ARMCD | Planned Arm Code | Char | Record Qualifier |  |  | C83216 |
| 7 | ARM | Description of Planned Arm | Char | Synonym Qualifier | ARMCD |  | C170984 |
| 8 | TVSTRL | Visit Start Rule | Char | Rule |  |  |  |
| 9 | TVENRL | Visit End Rule | Char | Rule |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic- specific commonality. | *Notes:* 2-character abbreviation, which must be "TV".
- **VISITNUM**: An assigned numeric identifier that aligns to the chronological order of a clinical encounter. | *Notes:* Numeric version of VISIT can be used for sorting.
- **VISIT**: The label for a protocol-defined clinical encounter. | *Notes:* May be used in addition to VISITNUM and/or VISITDY.
- **VISITDY**: The planned study day of a clinical encounter relative to the sponsor-defined reference start date. | *Notes:* Due to its sequential nature can be used for sorting.
- **ARMCD**: A short sequence of characters that represents the planned arm to which the subject was assigned. | *Notes:* ARMCD is limited to 20 characters and does not have special character restrictions. If the timing of visits for a trial does not depend on which Arm a subject is in, then ARMCD should be null.
- **ARM**: The name of the planned arm to which the subject was assigned.
- **TVSTRL**: *Notes:* Rule describing when the visit starts, in relation to the sequence of elements.
- **TVENRL**: *Notes:* Rule describing when the visit ends, in relation to the sequence of elements.

#### 5.1.4.2 Trial Disease Assessments


**Trial Disease Assessments**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | TDORDER | Sequence of Planned Assessment Schedule | Num | Timing |  |  |  |
| 5 | TDSTOFF | Offset from the Anchor | Char | Timing |  |  |  |
| 6 | TDTGTPAI | Planned Assessment Interval | Char | Timing |  |  |  |
| 7 | TDMINPAI | Planned Assessment Interval Minimum | Char | Timing |  |  |  |
| 8 | TDMAXPAI | Planned Assessment Interval Maximum | Char | Timing |  |  |  |
| 9 | TDNUMRPT | Maximum Number of Actual Assessments | Num | Record Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "TD".
- **TDORDER**: *Notes:* A number given to ensure ordinal sequencing of the planned assessment schedules within a trial.
- **TDSTOFF**: *Notes:* A fixed offset from the date provided by the variable referenced in TDANCVAR. This is used when the timing of planned cycles does not start on the exact day referenced in the variable indicated in TDANCVAR. The value of this variable will be a non-negative duration.
- **TDTGTPAI**: *Notes:* The planned interval between disease assessments.
- **TDMINPAI**: *Notes:* The lower limit of the allowed range for the planned interval between disease assessments.
- **TDMAXPAI**: *Notes:* The upper limit of the allowed range for the planned interval between disease assessments.
- **TDNUMRPT**: *Notes:* This variable must represent the maximum number of actual assessments for the analysis that this disease assessment schedule describes. In a trial where the maximum number of assessments is not defined explicitly in the protocol (e.g., assessments occur until death), TDNUMRPT should represent the maximum number of disease assessments that support the efficacy analysis, encountered by any subject across the trial at that point in time.

#### 5.1.4.3 Trial Disease Milestones


**Trial Disease Milestones—One Record per Disease Milestone Type**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | IETESTCD | Inclusion/Exclusion Criterion Short Name | Char | Topic |  |  |  |
| 4 | IETEST | Inclusion/Exclusion Criterion | Char | Synonym Qualifier | IETESTCD |  |  |
| 5 | IECAT | Inclusion/Exclusion Category | Char | Grouping Qualifier |  |  |  |
| 6 | IESCAT | Inclusion/Exclusion Subcategory | Char | Grouping Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "TI".
- **IETESTCD**: *Notes:* Short name IETEST. It can be used as a column name when converting a dataset from a vertical to a horizontal format. The value in IETESTCD cannot be longer than 8 characters, nor can it start with a number (e.g., "1TEST"). IETESTCD cannot contain characters other than letters, numbers, or underscores. The prefix "IE" is used to ensure consistency with the IE domain.
- **IETEST**: *Notes:* Full text of the inclusion or exclusion criterion. The prefix "IE" (rather than TI) is used to ensure consistency with the IE domain.
- **IECAT**: *Notes:* Used for categorization of the inclusion or exclusion criterion. The prefix "IE" (rather than TI) is used to ensure consistency with the IE domain. | *Examples:* "INCLUSION", "EXCLUSION"
- **IESCAT**: *Notes:* A further categorization of the exception criterion. Can be used to distinguish criteria for a substudy or to categorize major or minor exceptions. The prefix "IE" | *Examples:* "MAJOR", "MINOR"

### 5.1.5 Trial Inclusion/Exclusion Criteria


**Trial Inclusion/Exclusion—One Record per Criterion**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | TSSEQ | Sequence Number | Num | Identifier |  |  |  |
| 4 | TSGRPID | Group ID | Char | Identifier |  |  |  |
| 5 | TSPARMCD | Trial Summary Parameter Short Name | Char | Topic |  |  |  |
| 6 | TSPARM | Trial Summary Parameter | Char | Synonym Qualifier | TSPARMCD |  |  |
| 7 | TSVAL | Parameter Value | Char | Result Qualifier |  |  |  |
| 8 | TSVALNF | Parameter Null Flavor | Char | Result Qualifier |  |  |  |
| 9 | TSVALCD | Parameter Value Code | Char | Result Qualifier |  | Not in nonclinical trials |  |
| 10 | TSVCDREF | Name of the Reference Terminology | Char | Result Qualifier |  | Not in nonclinical trials |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "TS".
- **TSSEQ**: *Notes:* Sequence number to ensure uniqueness within the dataset.
- **TSGRPID**: *Notes:* Used to tie together a group of related records.
- **TSPARMCD**: *Notes:* TSPARMCD (the companion to TSPARM) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that TSPARMCD will need to serve as variable names. | *Examples:* "AGEMIN", "AGEMAX"
- **TSPARM**: *Notes:* Term for the trial summary parameter. The value in TSPARM cannot be longer than 40 characters. | *Examples:* "Planned Minimum Age of Subjects", "Planned Maximum Age of Subjects"
- **TSVAL**: *Notes:* Value of TSPARM. If TSVAL is null, a value is required for TSVALNF. Text over 200 characters can be added to additional columns TSVAL1-TSVALn. | *Examples:* "ASTHMA" when TSPARM value is "Trial Indications"
- **TSVALNF**: *Notes:* Null flavor for the value of TSVAL describing the reason the value is null, to be populated only if TSVAL is null.
- **TSVALCD**: *Notes:* Code of the term in TSVAL from the reference terminology cited in TSVCDREF.
- **TSVCDREF**: *Notes:* The name of the reference terminology or standard format from which TSVALCD is taken. | *Examples:* "CDISC CT", "SNOMED", "ISO 8601"

### 5.1.6 Trial Summary Information


**Trial Summary—One Record per Trial Summary Parameter**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | ACSEQ | Sequence Number | Num | Identifier |  |  |  |
| 4 | ACGRPID | Group ID | Char | Identifier |  |  |  |
| 5 | ACPARMCD | Challenge Agent Parameter Short Name | Char | Topic |  |  |  |
| 6 | ACPARM | Challenge Agent Parameter | Char | Synonym Qualifier | ACPARMCD |  |  |
| 7 | ACVAL | Parameter Value | Char | Result Qualifier |  |  |  |
| 8 | ACVALU | Parameter Units | Char | Variable Qualifier | ACVAL |  |  |
| 9 | ACVALNF | Parameter Null Flavor | Char | Result Qualifier |  |  |  |
| 10 | ACVALCD | Parameter Value Code | Char | Result Qualifier |  |  |  |
| 11 | ACVCDREF | Name of the Reference Terminology | Char | Result Qualifier |  |  |  |
| 12 | ACVCDVER | Version of the Reference Terminology | Char | Result Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "AC".
- **ACSEQ**: *Notes:* Sequence number given to ensure uniqueness within a dataset. Allows inclusion of multiple records for the same ACPARMCD.
- **ACGRPID**: *Notes:* Used to tie together a group of related records.
- **ACPARMCD**: *Notes:* ACPARMCD (the companion to ACPARM) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ACPARMCD will need to serve as variable names.
- **ACPARM**: *Notes:* Term for the challenge agent characterization parameter. The value in ACPARM cannot be longer than 40 characters.
- **ACVAL**: *Notes:* Value of ACPARM.
- **ACVALU**: *Notes:* Units for the value in ACVAL, if applicable.
- **ACVALNF**: *Notes:* Null flavor for the value of ACPARM, to be populated if and only if ACVAL is null.
- **ACVALCD**: *Notes:* This is the code of the term in ACVAL.
- **ACVCDREF**: *Notes:* The name of the reference terminology from which ACVALCD is taken. | *Examples:* "CDISC," "ISO 8601"
- **ACVCDVER**: *Notes:* The version number of the reference terminology cited in ACVCDREF, if applicable.

### 5.1.7 Challenge Agent Characterization


**Challenge Agent Characterization**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | ACSEQ | Sequence Number | Num | Identifier |  |  |  |
| 4 | ACGRPID | Group ID | Char | Identifier |  |  |  |
| 5 | ACPARMCD | Challenge Agent Parameter Short Name | Char | Topic |  |  |  |
| 6 | ACPARM | Challenge Agent Parameter | Char | Synonym Qualifier | ACPARMCD |  |  |
| 7 | ACVAL | Parameter Value | Char | Result Qualifier |  |  |  |
| 8 | ACVALU | Parameter Units | Char | Variable Qualifier | ACVAL |  |  |
| 9 | ACVALNF | Parameter Null Flavor | Char | Result Qualifier |  |  |  |
| 10 | ACVALCD | Parameter Value Code | Char | Result Qualifier |  |  |  |
| 11 | ACVCDREF | Name of the Reference Terminology | Char | Result Qualifier |  |  |  |
| 12 | ACVCDVER | Version of the Reference Terminology | Char | Result Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "AC".
- **ACSEQ**: *Notes:* Sequence number given to ensure uniqueness within a dataset. Allows inclusion of multiple records for the same ACPARMCD.
- **ACGRPID**: *Notes:* Used to tie together a group of related records.
- **ACPARMCD**: *Notes:* ACPARMCD (the companion to ACPARM) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ACPARMCD will need to serve as variable names.
- **ACPARM**: *Notes:* Term for the challenge agent characterization parameter. The value in ACPARM cannot be longer than 40 characters.
- **ACVAL**: *Notes:* Value of ACPARM.
- **ACVALU**: *Notes:* Units for the value in ACVAL, if applicable.
- **ACVALNF**: *Notes:* Null flavor for the value of ACPARM, to be populated if and only if ACVAL is null.
- **ACVALCD**: *Notes:* This is the code of the term in ACVAL.
- **ACVCDREF**: *Notes:* The name of the reference terminology from which ACVALCD is taken. | *Examples:* "CDISC," "ISO 8601"
- **ACVCDVER**: *Notes:* The version number of the reference terminology cited in ACVCDREF, if applicable.

## 5.2 Study References

### 5.2.1 Device Identifiers Dataset


**Device Identifiers Dataset**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | SPDEVID | Sponsor Device Identifier | Char | Identifier |  |  |  |
| 4 | DISEQ | Sequence Number | Num | Identifier |  |  |  |
| 5 | DIPARMCD | Device Identifier Element Short Name | Char | Topic |  |  |  |
| 6 | DIPARM | Device Identifier Element Name | Char | Synonym Qualifier | DIPARMCD |  |  |
| 7 | DIVAL | Device Identifier Element Value | Char | Result Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "DI".
- **SPDEVID**: *Notes:* Sponsor-defined identifier for the device.
- **DISEQ**: *Notes:* Sequence number given to ensure uniqueness within a parameter within a device (SPDEVID).
- **DIPARMCD**: *Notes:* Short name of the identifier characteristic of the device.
- **DIPARM**: *Notes:* Name of the identifier characteristic of the device.
- **DIVAL**: *Notes:* Value for the parameter.

### 5.2.2 Non-host Organism Identifiers Dataset


**Non-host Organism Identifiers Dataset**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | NHOID | Non-Host Organism Identifier | Char | Identifier |  |  |  |
| 4 | OISEQ | Sequence Number | Num | Identifier |  |  |  |
| 5 | OIPARMCD | Non-Host Organism ID Element Short Name | Char | Topic |  |  |  |
| 6 | OIPARM | Non-Host Organism ID Element Name | Char | Synonym Qualifier | OIPARMCD |  |  |
| 7 | OIVAL | Non-Host Organism ID Element Value | Char | Result Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **DOMAIN**: An abbreviation for a collection of observations, with a topic- specific commonality. | *Notes:* 2-character abbreviation, which must be "OI".
- **NHOID**: *Notes:* Sponsor-defined identifier for a non-host organism.
- **OISEQ**: *Notes:* Sequence number given to ensure uniqueness within a parameter within an organism (NHOID).
- **OIPARMCD**: *Notes:* Short name of the taxon being described.
- **OIPARM**: *Notes:* Name of the taxon being described.
- **OIVAL**: *Notes:* Value for the taxon in OIPARMCD/OIPARM for the organism identified by NHOID.

---

# 6 Datasets for Representing Relationships

## 6.1 Related Records Dataset


**RELREC Dataset**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | RDOMAIN | Related Domain Abbreviation | Char | Identifier |  |  |  |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | APID | Associated Persons Identifier | Char | Identifier |  |  |  |
| 5 | POOLID | Pool Identifier | Char | Identifier |  |  | C117053 |
| 6 | SPDEVID | Sponsor Device Identifier | Char | Identifier |  |  | C117060 |
| 7 | IDVAR | Identifying Variable | Char | Identifier |  |  |  |
| 8 | IDVARVAL | Identifying Variable Value | Char | Identifier |  |  |  |
| 9 | RELTYPE | Relationship Type | Char | Record Qualifier |  |  |  |
| 10 | RELID | Relationship Identifier | Char | Record Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **RDOMAIN**: *Notes:* 2-character abbreviation for the domain of the parent record(s).
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **APID**: *Notes:* Identifier for a single associated person, a group of associated persons, or a pool of associated persons. If APID identifies a pool, POOLDEF records must exist for each associated person (see Section 6.3, Pool Definition Dataset, and Section 4, Associated Persons Data).
- **POOLID**: A sequence of characters used to uniquely identify a group of subjects that have been pooled together.
- **SPDEVID**: A sequence of characters used by the sponsor to uniquely identify a specific device.
- **IDVAR**: *Notes:* Name of the identifying variable in the general-observation- class dataset that identifies the related record(s). | *Examples:* --SEQ and --GRPID
- **IDVARVAL**: *Notes:* Value of identifying variable described in IDVAR. If --SEQ is the variable being used to describe this record, then the value of --SEQ is entered here.
- **RELTYPE**: *Notes:* Identifies the hierarchical level of the records in the relationship. Values should be either ONE or MANY. However, values are only necessary when identifying a relationship between datasets.
- **RELID**: *Notes:* RELID value should be unique within the ID variable (e.g., USUBJID, APID, POOLID, SPDEVID) that is the subject of the relationship. All records with this ID variable that have the same RELID are considered related/associated. RELID can be any value the sponsor chooses, and is only meaningful within the RELREC dataset to identify the related/associated Domain records.

## 6.2 Supplemental Qualifiers Dataset


**SUPP--Dataset**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | RDOMAIN | Related Domain Abbreviation | Char | Identifier |  |  |  |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | APID | Associated Persons Identifier | Char | Identifier |  |  |  |
| 5 | POOLID | Pool Identifier | Char | Identifier |  |  |  |
| 6 | SPDEVID | Sponsor Device Identifier | Char | Identifier |  |  | C117060 |
| 7 | IDVAR | Identifying Variable | Char | Identifier |  |  |  |
| 8 | IDVARVAL | Identifying Variable Value | Char | Identifier |  |  |  |
| 11 | QVAL | Data Value | Char | Result Qualifier |  |  |  |
| 12 | QORIG | Origin | Char | Record Qualifier |  |  |  |
| 13 | QEVAL | Evaluator | Char | Record Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **RDOMAIN**: *Notes:* 2-character abbreviation for the domain of the parent record(s).
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **APID**: *Notes:* Identifier for a single associated person, a group of associated persons, or a pool of associated persons. If APID identifies a pool, POOLDEF records must exist for
- **POOLID**: A sequence of characters used to uniquely identify a group of subjects that have been pooled together.
- **SPDEVID**: A sequence of characters used by the sponsor to uniquely identify a specific device.
- **IDVAR**: *Notes:* Identifying variable in the parent dataset that identifies the related record(s). | *Examples:* --SEQ, --GRPID
- **IDVARVAL**: *Notes:* Value of identifying variable of the parent record(s).
- **QVAL**: *Notes:* Result of, response to, or value associated with QNAM. A value for this column is required; no records can be in a SUPP--dataset with a null value for QVAL.
- **QORIG**: *Notes:* Because QVAL can represent a mixture of collected (on a CRF), derived, or assigned items, QORIG is used to indicate the origin of this data.
- **QEVAL**: *Notes:* Used only for results that are subjective (e.g., assigned by a person or a group). Should be null for records that contain objectively collected or derived data. | *Examples:* "ADJUDICATION COMMITTEE", "STATISTICIAN", "DATABASE ADMINISTRATOR", "CLINICAL COORDINATOR"

## 6.3 Pool Definition Dataset


**POOLDEF Dataset**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 3 | POOLID | Pool Identifier | Char | Identifier |  |  | C117053 |
| 4 | RSUBJID | Related Subject or Pool Identifier | Char | Identifier |  |  |  |
| 5 | SREL | Subject Relationship | Char | Record Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product. | *Notes:* Either USUBJID or POOLID must be populated.
- **POOLID**: A sequence of characters used to uniquely identify a group of subjects that have been pooled together. | *Notes:* If POOLID is entered, POOLDEF records must exist for each subject in the pool and USUBJID must be null. Either USUBJID or POOLID must be populated.
- **RSUBJID**: *Notes:* Identifier used to identify a related subject or pool of subjects. RSUBJID will be populated with either the USUBJID of the related subject or the POOLID of the related pool.
- **SREL**: *Notes:* Describes the relationship of the subject identified in USUBJID or the pool identified in POOLID to the subject or pool identified in RSUBJID.

## 6.4 Related Subjects Dataset


**RELSUB Dataset**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 3 | POOLID | Pool Identifier | Char | Identifier |  |  | C117053 |
| 4 | RSUBJID | Related Subject or Pool Identifier | Char | Identifier |  |  |  |
| 5 | SREL | Subject Relationship | Char | Record Qualifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product. | *Notes:* Either USUBJID or POOLID must be populated.
- **POOLID**: A sequence of characters used to uniquely identify a group of subjects that have been pooled together. | *Notes:* If POOLID is entered, POOLDEF records must exist for each subject in the pool and USUBJID must be null. Either USUBJID or POOLID must be populated.
- **RSUBJID**: *Notes:* Identifier used to identify a related subject or pool of subjects. RSUBJID will be populated with either the USUBJID of the related subject or the POOLID of the related pool.
- **SREL**: *Notes:* Describes the relationship of the subject identified in USUBJID or the pool identified in POOLID to the subject or pool identified in RSUBJID.

## 6.5 Device-Subject Relationships Dataset


**DEVSUB Dataset**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | DOMAIN | Domain Abbreviation | Char | Identifier |  |  | C49558 |
| 3 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 4 | SPDEVID | Sponsor Device Identifier | Char | Identifier |  |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study. | *Notes:* Study identifier of the domain record(s).
- **DOMAIN**: An abbreviation for a collection of observations, with a topic-specific commonality. | *Notes:* 2-character abbreviation, which must be "DR".
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **SPDEVID**: *Notes:* Sponsor-defined identifier for the device. It must be unique for each tracked unit of the device under study, and can be at whatever level of granularity the device should be identified (e.g., model or serial number, combination of identifiers) as defined in DI.

## 6.6 Associated Persons Relationships


**APREL Dataset**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 3 | REFID | Reference ID | Char | Identifier |  |  | C82531 |
| 4 | SPEC | Specimen Type | Char | Variable Qualifier | REFID |  | C70713 |
| 5 | PARENT | Specimen Parent | Char | Identifier |  |  |  |
| 6 | LEVEL | Specimen Level | Num | Variable Qualifier | REFID |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **REFID**: A sequence of characters used to uniquely identify a source of information.
- **SPEC**: The type of sample material taken from a biological entity.
- **PARENT**: *Notes:* Identifies the REFID of the parent of a specimen to support tracking its genealogy.
- **LEVEL**: *Notes:* Identifies the generation number of the sample where the collected sample is considered the first generation.

## 6.7 Related Specimens Dataset


**RELSPEC Dataset**

| # | Variable | Label | Type | Role | Qualified | Restrictions | C-code |
|---|---|---|---|---|---|---|---|
| 1 | STUDYID | Study Identifier | Char | Identifier |  |  | C83082 |
| 2 | USUBJID | Unique Subject Identifier | Char | Identifier |  |  | C69256 |
| 3 | REFID | Reference ID | Char | Identifier |  |  | C82531 |
| 4 | SPEC | Specimen Type | Char | Variable Qualifier | REFID |  | C70713 |
| 5 | PARENT | Specimen Parent | Char | Identifier |  |  |  |
| 6 | LEVEL | Specimen Level | Num | Variable Qualifier | REFID |  |  |

**Variable Definitions:**

- **STUDYID**: A sequence of characters used by the sponsor to uniquely identify the study.
- **USUBJID**: A sequence of characters used to uniquely identify a subject across all studies for all applications or submissions involving the product.
- **REFID**: A sequence of characters used to uniquely identify a source of information.
- **SPEC**: The type of sample material taken from a biological entity.
- **PARENT**: *Notes:* Identifies the REFID of the parent of a specimen to support tracking its genealogy.
- **LEVEL**: *Notes:* Identifies the generation number of the sample where the collected sample is considered the first generation.

---hanges from SDTM v1.8 to SDTM v2.0
Minor updates to the introduction were made to broaden the use cases and describe the relationship to older versions
of the SDTM. A concept map showing the organization of the model was also added.
In examples of qualifier types, specific variable names have been replaced with descriptions because the variables
are introduced later in the document. The description of Synonym Qualifiers was updated to reflect that some
variables are synonym qualifiers of multiple variables.
The relationships domain Related Specimens (RELSPEC) was added.
Sections were reordered and regrouped, which resulted in the renumbering of sections and the elimination of some
unnecessary section layers. The metadata tables now have Variable(s) Qualified, Usage Restrictions, Variable C-
code, Definition, and Examples columns. The Notes column replaces the former Description column. A section
called Table Structure has been added to show the variable metadata included in the tables.
The section header Version History was removed. It was an unnecessary extra layer, because this section deals only
with the changes from one version to the next. The Variable, Dataset, and Section Changes and Additions subsection
was removed, as this was also an unnecessary extra layer.
Table numbers were removed, as they are redundant with section numbers.
Usage restrictions of "Not in nonclinical trials" were added.
A new section, Study Subject Data, was created which groups the general observation classes and special-purpose
domains.
The variable APID was removed from Section 3.1.4, Identifiers for All Classes, because APID is only allowed in
AP domains. It is still listed in new Section 4, Associated Persons Data.
The variables qualified for --DOSFRM, --DOSFRQ, and --DOSRGM were changed from --DOSE, --DOSTXT, and
--DOSTOT to --TRT.
Because the role of the domain-specific variable --BEATNO was changed to Identifier, it was moved from Section
3.1.3, The Findings Observation Class, to Section 3.1.4, Identifiers for All Classes. --LNKID and --LNKGRP have
been revised to clarify that the relationships are within a subject.
The special-purpose Subject Visits (SV) domain remains a special-purpose domain, but additional variables have
been added to address the effect of an epidemic or pandemic on visits.
The role of the --LOINC variable was changed from Synonym Qualifier of --TESTCD to Record Qualifier. A single
variable of --TESTCD may be associated with multiple values of --LOINC, depending on the values of other
variables, such as --SPEC and --METHOD. The order of --METHOD was changed so that the variable appears after
--PORTOT, rather than after --LOC.
The Trial Design Model has been reorganized and revised. Text in the top-level section was revised to replace a
specific list of trial design concepts with a more general statement about the use of variables from trial design
domains being used in subject-level domains.
The role of the Trial Disease Milestones variable TMDEF was changed to Variable Qualifier with MIDSTYPE as
the variable qualified.
New variables have been added to the following sections. Many of these are restricted to use in particular domains,
as noted in the Usage Restrictions column.
- Section 3.1.1, The Interventions Observation Class
o
--REASOC, Reason for Occur Value
o
--CNTMOD, Contact Mode
o
--EPCHGI, Epi/Pandemic Change Indicator
- Section 3.1.2, The Events Observation Class
o
--REASOC, Reason for Occur Value

o
--CNTMOD, Contact Mode
o
--EPCHGI, Epi/Pandemic Change Indicator
o
--RELDEV, Relationship of Event to Device
o
--SINTV, Needs Intervention to Prevent Impairment
o
--UNANT, Unanticipated Adverse Effect/Event
o
--RLPRT, Rel of AE to Device-Related Procedure
o
--RLPRC, Rel of AE to Non-Dev-Rel Study Activity
- Section 3.1.3, The Findings Observation Class
o
--SBMRKS, Sublineage Marker String
o
--CELSTA, Cell State
o
--CSMRKS, Cell State Marker String
o
--CNTMOD, Contact Mode
o
--EPCHGI, Epi/Pandemic Related Change Indicator
o
--TSTCND, Test Condition
o
--CNDAGT, Test Condition Agent
o
--BDAGNT, Binding Agent
o
--ABCLID, Antibody Clone Identifier
o
--MRKSTR, Marker String
o
--GATE, Gate
o
--GATEDEF, Gate Definition
o
--TSTOPO, Test Operational Objective
o
--MSCBCE, Molecule Secreted by Cells
o
--SPTSTD, Sponsor Test Description
o
--TSTPNL, Test Panel
o
--RESSCL, Result Scale
o
--RESTYP, Result Type
o
--COLSRT, Collected Summary Result Type
o
--LLOD, Lower Limit of Detection
o
--INHERT, Inheritability
o
--GENREF, Genome Reference
o
--CHROM, Chromosome Identifier
o
--SYM, Genomic Symbol
o
--SYMTYP, Genomic Symbol Type
o
--GENLOC, Genetic Location
o
--GENSR, Genetic Sub-Region
o
--SEQID, Sequence Identifier
o
--PRVID, Published Variant Identifier
o
--COPYID, Copy Identifier
o
--TMTHSN, Test Method Sensitivity

o
--CLSIG, Clinically Significant, Collected
o
--REASPF, Reason Test Performed
- Section 3.1.5, Timing Variables for All Classes.
o
--PTFL, Point in Time Flag
o
--PDUR, Planned Duration
- Section 3.2.3.2, Subject Elements
o
SESTDY, Study Day of Start of Element
o
SEENDY, Study Day of End of Element
- Section 3.2.3.3, Subject Visits
o
SVPRESP, Pre-Specified
o
SVOCCUR, Occurrence
o
SVREASOC, Reason for Occur Value
o
SVCNTMOD, Contact Mode
o
SVEPCHGI, Epi/Pandemic Related Change Indicator
The following new section was added:
Section 6.7, Related Specimens Dataset


---

# 8 Proposed Future Changes to the SDTM

The following changes are proposed for the next version of the SDTM:
- The variable --BLFL will be considered for deprecation as a qualifier for findings class domains.
- The variable --MODIFY will be considered for deprecation as a qualifier for findings class domains. The
variable --MODIFY will remain as a qualifier for the events and interventions classes.
- The findings variable --BODSYS may be restricted to use in nonclinical trials.
- The variable TIRL will be considered for removal from the Trial Inclusion/Exclusion (TI) domain.
- The variable --TSTDTL may be made domain-specific, for use only in the Microbiology Specimen (MB),
Microscopic Findings (MI), and Genetic Findings (GF) domains.
The findings variable --LOBXFL was introduced in SDTM v1.7. In the accompanying SDTMIG v3.3, for domains
where --BLFL had been included as an expected variable,  --BLFL was made permissible, while --LOBXFL was
added as an expected variable. Future deprecation was not announced in SDTM v1.7 in order to provide a sufficient
transition period. Deprecation in the next version of the SDTM with an accompanying SDTMIG is proposed as this
should provide a sufficient transition period.
As a findings variable, --MODIFY was originally included for use in the Physical Examination (PE) domain in the
SDTMIG to support coding of an abnormality recorded as a result of a physical examination. However,
abnormalities found during a physical examination are now more commonly recorded as events in the Medical
History (MH) domain or the Adverse Events (AE) domain, where the full range of coding variables are available.
This is consistent with the best-practice scenario described in the Clinical Data Acquisition Standards
Harmonization Implementation Guide (CDASHIG). After --MODIFY is deprecated as a findings qualifier, an
implementer coding abnormalities found at a physical exam will not be able to represent the coding in PE domain,
but will be able to represent coding in the appropriate events domain. No use cases other than in the PE domain have
been identified for --MODIFY as a findings variable.
The rationale for removing --BODSYS as a qualifier for use in clinical trials is the same as the rationale for
removing --MODIFY. If deprecated, the variable will still be available for use in nonclinical trials, where it has been
used to classify the body system of the organ represented as a value of --SPEC.
The variable TIRL was included in the Trial Inclusion/Exclusion Criteria (TI) domain in anticipation of developing
a way to represent eligibility criteria in a computer-executable manner. However, such a method has not been
developed, and it is not clear that an SDTM dataset would be the best place to represent such a computer-executable
representation.


---

# 9 Appendices

## Appendix A: Representations and Warranties, Limitations of Liability, and Disclaimers

Liability, and Disclaimers

CDISC Patent Disclaimers
It is possible that implementation of and compliance with this standard may require use of subject matter covered by
patent rights. By publication of this standard, no position is taken with respect to the existence or validity of any
claim or of any patent rights in connection therewith. CDISC, including the CDISC Board of Directors, shall not be
responsible for identifying patent claims for which a license may be required in order to implement this standard or
for conducting inquiries into the legal validity or scope of those patents or patent claims that are brought to its
attention.
Representations and Warranties
“CDISC grants open public use of this User Guide (or Final Standards) under CDISC’s copyright.”
Each Participant in the development of this standard shall be deemed to represent, warrant, and covenant, at the time
of a Contribution by such Participant (or by its Representative), that to the best of its knowledge and ability: (a) it
holds or has the right to grant all relevant licenses to any of its Contributions in all jurisdictions or territories in
which it holds relevant intellectual property rights; (b) there are no limits to the Participant’s ability to make the
grants, acknowledgments, and agreements herein; and (c) the Contribution does not subject any Contribution, Draft
Standard, Final Standard, or implementations thereof, in whole or in part, to licensing obligations with additional
restrictions or requirements inconsistent with those set forth in this Policy, or that would require any such
Contribution, Final Standard, or implementation, in whole or in part, to be either: (i) disclosed or distributed in
source code form; (ii) licensed for the purpose of making derivative works (other than as set forth in Section 4.2 of
the CDISC Intellectual Property Policy (“the Policy”)); or (iii) distributed at no charge, except as set forth in
Sections 3, 5.1, and 4.2 of the Policy. If a Participant has knowledge that a Contribution made by any Participant or
any other party may subject any Contribution, Draft Standard, Final Standard, or implementation, in whole or in
part, to one or more of the licensing obligations listed in Section 9.3, such Participant shall give prompt notice of the
same to the CDISC President who shall promptly notify all Participants.
No Other Warranties/Disclaimers. ALL PARTICIPANTS ACKNOWLEDGE THAT, EXCEPT AS PROVIDED
UNDER SECTION 9.3 OF THE CDISC INTELLECTUAL PROPERTY POLICY, ALL DRAFT STANDARDS
AND FINAL STANDARDS, AND ALL CONTRIBUTIONS TO FINAL STANDARDS AND DRAFT
STANDARDS, ARE PROVIDED “AS IS” WITH NO WARRANTIES WHATSOEVER, WHETHER EXPRESS,
IMPLIED, STATUTORY, OR OTHERWISE, AND THE PARTICIPANTS, REPRESENTATIVES, THE CDISC
PRESIDENT, THE CDISC BOARD OF DIRECTORS, AND CDISC EXPRESSLY DISCLAIM ANY
WARRANTY OF MERCHANTABILITY, NONINFRINGEMENT, FITNESS FOR ANY PARTICULAR OR
INTENDED PURPOSE, OR ANY OTHER WARRANTY OTHERWISE ARISING OUT OF ANY PROPOSAL,
FINAL STANDARDS OR DRAFT STANDARDS, OR CONTRIBUTION.
Limitation of Liability
IN NO EVENT WILL CDISC OR ANY OF ITS CONSTITUENT PARTS (INCLUDING, BUT NOT LIMITED
TO, THE CDISC BOARD OF DIRECTORS, THE CDISC PRESIDENT, CDISC STAFF, AND CDISC
MEMBERS) BE LIABLE TO ANY OTHER PERSON OR ENTITY FOR ANY LOSS OF PROFITS, LOSS OF
USE, DIRECT, INDIRECT, INCIDENTAL, CONSEQUENTIAL, OR SPECIAL DAMAGES, WHETHER
UNDER CONTRACT, TORT, WARRANTY, OR OTHERWISE, ARISING IN ANY WAY OUT OF THIS
POLICY OR ANY RELATED AGREEMENT, WHETHER OR NOT SUCH PARTY HAD ADVANCE NOTICE
OF THE POSSIBILITY OF SUCH DAMAGES.

Note: The CDISC Intellectual Property Policy can be found at
http://www.cdisc.org/system/files/all/article/application/pdf/cdisc_20ip_20policy_final.pdf

