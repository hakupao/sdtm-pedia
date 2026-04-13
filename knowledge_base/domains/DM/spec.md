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
- **CDISC Notes:** ARMCD is limited to 20 characters. It is not subject to the character restrictions that apply to TESTCD. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. If the subject was not assigned to a trial arm, ARMCD is null and ARMNRS is populated. \n With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial Arms dataset.

### ARM
- **Order:** 25
- **Label:** Description of Planned Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Exp
- **CDISC Notes:** Name of the arm to which the subject was assigned. If the subject was not assigned to an arm, ARM is null and ARMNRS is populated. \n With the exception of studies which use multistage arm assignments, must be a value of ARM in the Trial Arms dataset.

### ACTARMCD
- **Order:** 26
- **Label:** Actual Arm Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** Code of actual arm. ACTARMCD is limited to 20 characters. It is not subject to the character restrictions that apply to TESTCD. The maximum length of ACTARMCD is longer than for other short variables to accommodate the kind of values that are likely to be needed for crossover trials. \n With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial Arms dataset. \n If the subject was not assigned to an arm or followed a course not described by any planned arm, ACTARMCD is null and ARMNRS is populated.

### ACTARM
- **Order:** 27
- **Label:** Description of Actual Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Exp
- **CDISC Notes:** Description of actual arm. \n With the exception of studies which use multistage arm assignments, must be a value of ARM in the Trial Arms dataset. \n If the subject was not assigned to an arm or followed a course not described by any planned arm, ACTARM is null and ARMNRS is populated.

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
- **CDISC Notes:** Country of the investigational site in which the subject participated in the trial. \n \n Generally represented using ISO 3166-1 Alpha-3. Note that regulatory agency specific requirements (e.g., US FDA) may require other terminologies; in such cases, follow regulatory requirements.

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
