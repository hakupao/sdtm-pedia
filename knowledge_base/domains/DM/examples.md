# DM — Examples

## Example 1

**dm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SUBJID | RFSTDTC | RFENDTC | RFXSTDTC | RFXENDTC | RFICDTC | RFPENDTC | SITEID | INVNAM | BRTHDTC | AGE | AGEU | SEX | RACE | ETHNIC | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD | COUNTRY |
|-----|---------|--------|---------|--------|---------|---------|----------|----------|---------|----------|--------|--------|---------|-----|------|-----|------|--------|-------|-----|----------|--------|--------|----------|---------|
| 1 | ABC123 | DM | ABC12301001 | 01001 | 2006-01-12 | 2006-03-10 | 2006-01-12 | 2006-03-10 | 2006-01-03 | 2006-04-01 | 01 | JOHNSON, M | 1948-12-13 | 57 | YEARS | M | WHITE | HISPANIC OR LATINO | A | Drug A | A | Drug A | | | USA |
| 2 | ABC123 | DM | ABC12301002 | 01002 | 2006-01-15 | 2006-02-28 | 2006-01-15 | 2006-02-28 | 2006-01-04 | 2006-03-26 | 01 | JOHNSON, M | 1955-03-22 | 50 | YEARS | M | WHITE | NOT HISPANIC OR LATINO | P | Placebo | P | Placebo | | | USA |
| 3 | ABC123 | DM | ABC12301003 | 01003 | 2006-01-16 | 2006-03-19 | 2006-01-18 | 2006-03-19 | 2006-01-02 | 2006-03-19 | 01 | JOHNSON, M | 1938-01-19 | 68 | YEARS | F | BLACK OR AFRICAN AMERICAN | NOT HISPANIC OR LATINO | P | Placebo | P | Placebo | | | USA |
| 4 | ABC123 | DM | ABC12301004 | 01004 | | | | | 2006-01-07 | 2006-01-08 | 01 | JOHNSON, M | 1941-07-02 | | M | ASIAN | NOT HISPANIC OR LATINO | | | | | SCREEN FAILURE | | USA |
| 5 | ABC123 | DM | ABC12302001 | 02001 | 2006-02-02 | 2006-03-31 | 2006-02-02 | 2006-03-31 | 2006-01-15 | 2006-04-12 | 02 | GONZALEZ, E | 1950-06-23 | 55 | YEARS | F | AMERICAN INDIAN OR ALASKA NATIVE | NOT HISPANIC OR LATINO | P | Placebo | P | Placebo | | | USA |
| 6 | ABC123 | DM | ABC12302002 | 02002 | 2006-02-03 | 2006-04-05 | 2006-02-03 | 2006-04-05 | 2006-01-10 | 2006-04-25 | 02 | GONZALEZ, E | 1956-05-05 | 49 | YEARS | F | NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDERS | NOT HISPANIC OR LATINO | A | Drug A | A | Drug A | | | USA |

## Example 2

This example Demographics dataset does not include all the DM required and expected variables, only those that illustrate the variables that represent arm information. The following example illustrates values of ARMCD for subjects in Example Trial 1, described in Section 7.2.1, Trial Arms. This study included 2 elements, screen and run-in, before subjects were randomized to treatment. For this study, the sponsor submitted data on all subjects, including screen-failure subjects.

**Row 1:** Subject 001 was randomized to arm "Drug A". As shown in the SE dataset, this subject completed the "Drug A" element, so their actual arm was also "Drug A".

**Row 2:** Subject 002 was randomized to arm "Drug B". As shown in the SE dataset, their actual arm was consistent with their randomization.

**Row 3:** Subject 003 was a screen failure, so they were not assigned to an arm or treated. The arm actual arm variables are null, and ARMNRS="SCREEN FAILURE".

**Row 4:** Subject 004 withdrew during the run-in element. Like subject 003, they were not assigned to an arm or treated. However, they were not considered a screen failure, and ARMNRS="NOT ASSIGNED".

**Row 5:** Subject 005 was randomized but dropped out before being treated. Thus, the actual arm variables are not populated and ARMNRS="ASSIGNED, NOT TREATED".

**dm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD |
|-----|---------|--------|---------|-------|-----|----------|--------|--------|----------|
| 1 | ABC | DM | 001 | A | Drug A | A | Drug A | | |
| 2 | ABC | DM | 002 | B | Drug B | B | Drug B | | |
| 3 | ABC | DM | 003 | | | | | SCREEN FAILURE | |
| 4 | ABC | DM | 004 | | | | | NOT ASSIGNED | |
| 5 | ABC | DM | 005 | A | Drug A | | | ASSIGNED, NOT TREATED | |

**Rows 1-3:** Subject 001 completed all the elements for arm A.

**Rows 4-6:** Subject 002 completed all the elements for arm B.

**Row 7:** Subject 003 was a screen failure, who participated only in the "Screen" element.

**Rows 8-9:** Subject 004 withdrew during the "Run-in" element, before they could be randomized.

**Rows 10-11:** Subject 005 withdrew after they were randomized, but did not start treatment.

**se.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SESEQ | ETCD | ELEMENT | SESTDTC | SEENDTC |
|-----|---------|--------|---------|-------|------|---------|---------|---------|
| 1 | ABC | SE | 001 | 1 | SCRN | Screen | 2006-06-01 | 2006-06-07 |
| 2 | ABC | SE | 001 | 2 | RI | Run-In | 2006-06-07 | 2006-06-21 |
| 3 | ABC | SE | 001 | 3 | A | Drug A | 2006-06-21 | 2006-07-05 |
| 4 | ABC | SE | 002 | 1 | SCRN | Screen | 2006-05-03 | 2006-05-10 |
| 5 | ABC | SE | 002 | 2 | RI | Run-In | 2006-05-10 | 2006-05-24 |
| 6 | ABC | SE | 002 | 3 | B | Drug B | 2006-05-24 | 2006-06-07 |
| 7 | ABC | SE | 003 | 1 | SCRN | Screen | 2006-06-27 | 2006-06-30 |
| 8 | ABC | SE | 004 | 1 | SCRN | Screen | 2006-05-14 | 2006-05-21 |
| 9 | ABC | SE | 004 | 2 | RI | Run-In | 2006-05-21 | 2006-05-26 |
| 10 | ABC | SE | 005 | 1 | SCRN | Screen | 2006-05-14 | 2006-05-21 |
| 11 | ABC | SE | 005 | 2 | RI | Run-In | 2006-05-21 | 2006-05-26 |

## Example 3

**Row 1:** Subject 001 was randomized to drug A. At the end of the double-blind treatment epoch, they were assigned to open label A; thus, their ARMCD is "AA". They received the treatment to which they were assigned, so ACTRMCD is also "AA".

**Row 2:** Subject 002 was randomized to drug A. They were lost to follow-up during the double-blind treatment epoch, so never reached the open label epoch, when they would have been assigned to either drug A or the rescue element. Their ARMCD is "A". This case illustrates the exception to the rule that ARMCD, ARM, ACTARMCD, and ACTARM must be populated with values from the TA dataset.

**Row 3:** Subject "003" was randomized to drug A, but received drug B. At the end of the double-blind treatment epoch, they were assigned to rescue treatment. ARMCD shows the result of their assignments, "AR"; ACTARMCD shows their actual treatment, "BR".

**dm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD |
|-----|---------|--------|---------|-------|-----|----------|--------|--------|----------|
| 1 | DEF | DM | 001 | AA | A-OPEN A | AA | A-OPEN A | | |
| 2 | DEF | DM | 002 | A | A | A | A | | |
| 3 | DEF | DM | 003 | AR | A-RESCUE | BR | B-RESCUE | | |

The following example illustrates values of ARMCD for subjects in Example Trial 3, described in Section 7.2.1, Trial Arms.

**Rows 1-3:** Show that the subject passed through all 3 elements for the AA arm.

**Rows 4-5:** Show the 2 elements ("Screen" and "Treatment A") the subject passed through.

**Rows 6-8:** Show that the subject passed through the 3 elements associated with the "B-Rescue" arm.

**se.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SESEQ | ETCD | ELEMENT | SESTDTC | SEENDTC |
|-----|---------|--------|---------|-------|------|---------|---------|---------|
| 1 | DEF | SE | 001 | 1 | SCRN | Screen | 2006-01-07 | 2006-01-12 |
| 2 | DEF | SE | 001 | 2 | DBA | Treatment A | 2006-01-12 | 2006-04-10 |
| 3 | DEF | SE | 001 | 3 | OA | Open Drug A | 2006-04-10 | 2006-07-05 |
| 4 | DEF | SE | 002 | 1 | SCRN | Screen | 2006-02-03 | 2006-02-10 |
| 5 | DEF | SE | 002 | 2 | DBA | Treatment A | 2006-02-10 | 2006-03-24 |
| 6 | DEF | SE | 003 | 1 | SCRN | Screen | 2006-02-22 | 2006-03-01 |
| 7 | DEF | SE | 003 | 2 | DBB | Treatment B | 2006-03-01 | 2006-06-27 |
| 8 | DEF | SE | 003 | 3 | RSC | Rescue | 2006-06-27 | 2006-09-24 |

## Example 4

The CRF in this example is annotated to show the CDASH variable name and the target SDTMIG variable. Data that are collected using the same variable name as defined in the SDTMIG are in RED. If the CDASHIG variable differs from the one defined in the SDTMIG, the CDASHIG variable is in GREY.

See the CDASH Model and Implementation Guide for additional information: https://www.cdisc.org/standards/foundational/cdash.

This example shows multiple race categories and subcategories. Only a subset of options is shown for this instrument due to space constraints.

**Demographics Sample aCRF for Race with Additional Granularity**

The CRF presents 7 race questions (RACE01-RACE07) with checkbox options:
- RACE01: AMERICAN INDIAN OR ALASKA NATIVE
- RACE02: ASIAN
- RACE03: BLACK OR AFRICAN AMERICAN
- RACE04: NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER
- RACE05: WHITE
- RACE06: NOT REPORTED
- RACE07: UNKNOWN

If the study participant answered AMERICAN INDIAN OR ALASKA NATIVE, subcategories (CRACE01-CRACE04) from the RACEC codelist are presented: ALASKA NATIVE, AMERICAN INDIAN, CARIBBEAN INDIAN, CENTRAL AMERICAN INDIAN.

If the study participant answered ASIAN, subcategories (CRACE05-CRACE10) are presented: ASIAN AMERICAN, ASIAN INDIAN, BANGLADESHI, CHINESE, JAPANESE, KOREAN.

If the study participant answered BLACK OR AFRICAN AMERICAN, subcategories (CRACE11-CRACE17) are presented: AFRICAN, AFRICAN AMERICAN, AFRICAN CARIBBEAN, BAHAMIAN, BARBADIAN, BLACK, BLACK CENTRAL AMERICAN.

If the study participant answered WHITE, subcategories (CRACE18-CRACE21) are presented: ARAB, EUROPEAN, MIDDLE EASTERN, RUSSIAN.

**CRF Metadata**

| CDASH Variable | Order | Question Text | Prompt | CRF Completion Instructions | Type | SDTMIG Target Variable | SDTM Target Mapping | Controlled Terminology Code List Name | Permissible Values | List Style |
|---|---|---|---|---|---|---|---|---|---|---|
| RACE01 | 1 | Which of the following racial designations best describes you? (More than one choice is acceptable.) | Race | Study participants should self-report race, with race being asked about after ethnicity. | Text | RACE | | (RACE) | AMERICAN INDIAN OR ALASKA NATIVE | checkbox |
| RACE02 | 2 | (same) | Race | (same) | Text | RACE | | (RACE) | ASIAN | checkbox |
| RACE03 | 3 | (same) | Race | (same) | Text | RACE | | (RACE) | BLACK OR AFRICAN AMERICAN | checkbox |
| RACE04 | 4 | (same) | Race | (same) | Text | RACE | | (RACE) | NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER | checkbox |
| RACE05 | 5 | (same) | Race | (same) | Text | RACE | | (RACE) | WHITE | checkbox |
| RACE06 | 6 | (same) | Race | (same) | Text | RACE | | (RACE) | NOT REPORTED | checkbox |
| RACE07 | 7 | (same) | Race | (same) | Text | RACE | | (RACE) | UNKNOWN | checkbox |
| CRACE01-CRACE04 | 10 | (same) | Race | Select each value that applies if the subject answered "AMERICAN INDIAN OR ALASKA NATIVE". Check all that apply. | Text | SUPPDM.QVAL | For each value that applies, SUPPDM.QVAL where SUPPDM.QNAM ="CRACEn" and SUPPDM.QLABEL = "Collected Race n" where n is the choice value. | (RACEC) | ALASKA NATIVE; AMERICAN INDIAN; CARIBBEAN INDIAN; CENTRAL AMERICAN INDIAN | checkbox |
| CRACE05-CRACE10 | 11 | (same) | Race | Select each value that applies if the subject answered "ASIAN". Check all that apply. | Text | SUPPDM.QVAL | (same mapping pattern) | (RACEC) | ASIAN AMERICAN; ASIAN INDIAN; BANGLADESHI; CHINESE; JAPANESE; KOREAN | checkbox |
| CRACE11-CRACE17 | 12 | (same) | Race | Select each value that applies if the subject answered "BLACK OR AFRICAN AMERICAN". Check all that apply. | Text | SUPPDM.QVAL | (same mapping pattern) | (RACEC) | AFRICAN; AFRICAN AMERICAN; AFRICAN CARIBBEAN; BAHAMIAN; BARBADIAN; BLACK; BLACK CENTRAL AMERICAN | checkbox |
| CRACE18-CRACE21 | 13 | (same) | Race | Select each value that applies if the subject answered "WHITE". Check all that apply. | Text | SUPPDM.QVAL | (same mapping pattern) | (RACEC) | ARAB; EUROPEAN; MIDDLE EASTERN; RUSSIAN | checkbox |

The value of RACE is used to represent the high-level racial designation as a single collected value per CDISC Controlled Terminology in dm.xpt. When more than 1 choice is selected, the value is represented with "MULTIPLE" as shown in this example. **Note:** Only those variables relevant to this example are shown.

**Row 1:** Shows that USUBJID ABC789-010-045 designated 1 race, "WHITE", as the value that best describes their race.

**Row 2:** Shows that USUBJID ABC789-010-046 designated 1 race, "ASIAN", as the value that best describes their race.

**Row 3:** Shows that USUBJID ABC789-010-047 designated multiple races as the values that best describe their race. "MULTIPLE" is assigned in RACE.

**dm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SUBJID | RACE |
|-----|---------|--------|---------|--------|------|
| 1 | ABC789 | DM | ABC789-010-045 | 010-045 | WHITE |
| 2 | ABC789 | DM | ABC789-010-046 | 010-046 | ASIAN |
| 3 | ABC789 | DM | ABC789-010-047 | 010-047 | MULTIPLE |

When a subject selects multiple race values, as USUBJID ABC789-010-047 did, the values selected are represented in SUPPDM. Collected race, which is the specific race subcategory (or subcategories) selected by each subject, is represented in SUPPDM to ensure subject self-identification and/or country-specific requirements are available for reference. CDASH recommended QNAM-QLABEL values have been provided.

**Rows 1, 2:** Show that USUBJID ABC789-010-047 selected 2 RACE values, "ASIAN" and "WHITE". CDASH recommended QNAM-QLABEL values have been provided.

**Rows 3-5:** Show that USUBJID ABC789-010-047 selected 3 collected race (CRACE) values, "CHINESE", "KOREAN", and "RUSSIAN". CDASH recommended QNAM-QLABEL values have been provided.

**suppdm.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC789 | DM | ABC789-010-047 | | | RACE2 | Race 2 | ASIAN | CRF | |
| 2 | ABC789 | DM | ABC789-010-047 | | | RACE5 | Race 5 | WHITE | CRF | |
| 3 | ABC789 | DM | ABC789-010-047 | | | CRACE8 | Collected Race 8 | CHINESE | CRF | |
| 4 | ABC789 | DM | ABC789-010-047 | | | CRACE10 | Collected Race 10 | KOREAN | CRF | |
| 5 | ABC789 | DM | ABC789-010-047 | | | CRACE21 | Collected Race 21 | RUSSIAN | CRF | |

## Example 5

This example shows different Chinese regional ethnicity subcategorizations (majority and minority).

**CRF Mock Example**

The CRF collects ETHNIC (Hispanic or Latino / Not Hispanic or Latino) with subcategories for Chinese regional ethnicity: HAN CHINESE, MANCHU, MIAO, UYGHUR, ZHUANG.

In this CRF example, subcategorizations of ethnicity are made available.

RACE is identified as "ASIAN" and ETHNIC as "NOT HISPANIC OR LATINO".

**dm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SUBJID | AGE | AGEU | SEX | RACE | ETHNIC |
|-----|---------|--------|---------|--------|-----|------|-----|------|--------|
| 1 | ABC789 | DM | ABC789-010-045 | 010-045 | 20 | YEARS | M | ASIAN | NOT HISPANIC OR LATINO |
| 2 | ABC789 | DM | ABC789-010-047 | 010-047 | 24 | YEARS | F | ASIAN | NOT HISPANIC OR LATINO |

**Row 1:** Ethnicity subcategorization of subject self-identification being "HAN CHINESE". CDASH recommended QNAM-QLABEL values have been provided.

**Rows 2-3:** Ethnicity subcategorization of subject self-identification being "MIAO" and "ZHUANG". CDASH recommended QNAM-QLABEL values have been provided.

**suppdm.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC789 | DM | ABC789-010-045 | | | ETHNIC1 | Collected Ethnicity 1 | HAN CHINESE | CRF | |
| 2 | ABC789 | DM | ABC789-010-047 | | | ETHNIC1 | Collected Ethnicity 1 | MIAO | CRF | |
| 3 | ABC789 | DM | ABC789-010-047 | | | ETHNIC2 | Collected Ethnicity 2 | ZHUANG | CRF | |

## Example 6

The CRF in this example is annotated to show the CDASH variable name and the target SDTMIG variable. Data that are collected using the same variable name as defined in the SDTMIG are in RED. If the CDASHIG variable differs from the one defined in the SDTMIG, the CDASHIG variable is in GREY.

See the CDASH Model and Implementation Guide for additional information: https://www.cdisc.org/standards/foundational/cdash.

This example shows race categories and subcategories. Only a subset of options are shown for this instrument due to space constraints. For a complete aCRF example see the CDASHIG v2.1, Section 7.3.

**Demographics Sample aCRF for Race with Additional Granularity**

The CRF presents 7 race questions (RACE01-RACE07) with the same structure as Example 4, plus subcategory questions for ASIAN (CRACE05-CRACE10), BLACK OR AFRICAN AMERICAN (CRACE11-CRACE17), and other categories.

**CRF Metadata**

Same structure as Example 4 CRF Metadata, with the following key mappings:
- RACE01-RACE07 → RACE (using RACE codelist)
- CRACE05-CRACE10 (ASIAN subcategories) → SUPPDM.QVAL (using RACEC codelist): ASIAN AMERICAN, ASIAN INDIAN, BANGLADESHI, CHINESE, JAPANESE, KOREAN
- CRACE11-CRACE17 (BLACK OR AFRICAN AMERICAN subcategories) → SUPPDM.QVAL (using RACEC codelist): AFRICAN, AFRICAN AMERICAN, AFRICAN CARIBBEAN, BAHAMIAN, BARBADIAN, BLACK, BLACK CENTRAL AMERICAN

The value of RACE is used to represent the high-level racial designation as a single collected value per CDISC Controlled Terminology in dm.xpt. In this example, subjects chose to select 1 high-level racial designation.

**Note:** Only those variables relevant to this example are shown.

**Row 1:** Shows that USUBJID ABC789-010-001 designated 1 race, "ASIAN", as the value that best describes their race.

**Row 2:** Shows that USUBJID ABC789-010-002 designated 1 race, "BLACK OR AFRICAN AMERICAN", as the value that best describes their race.

**Row 3:** Shows that USUBJID ABC789-010-003 designated 1 race, "BLACK OR AFRICAN AMERICAN", as the value that best describes their race.

**dm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SUBJID | RACE |
|-----|---------|--------|---------|--------|------|
| 1 | ABC789 | DM | ABC789-010-001 | 010-001 | ASIAN |
| 2 | ABC789 | DM | ABC789-010-002 | 010-002 | BLACK OR AFRICAN AMERICAN |
| 3 | ABC789 | DM | ABC789-010-003 | 010-003 | BLACK OR AFRICAN AMERICAN |

Collected race, which is the specific race subcategory for each subject, is represented in SUPPDM to ensure subject self-identification and/or country-specific requirements are available for reference. In this example, each subject selected 1 race and 1 race subcategory. CDASH recommended QNAM-QLABEL values have been provided.

**Row 1:** Shows USUBJID ABC789-010-001 selected "JAPANESE" as the specific ASIAN race collected.

**Row 2:** Shows USUBJID ABC789-010-002 selected "AFRICAN AMERICAN" as the specific BLACK OR AFRICAN AMERICAN race collected.

**Row 3:** Shows USUBJID ABC789-010-003 selected "BLACK" as the specific BLACK OR AFRICAN AMERICAN race collected.

**suppdm.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC789 | DM | ABC789-010-001 | | | CRACE3 | Collected Race 3 | JAPANESE | CRF | |
| 2 | ABC789 | DM | ABC789-010-002 | | | CRACE5 | Collected Race 5 | AFRICAN AMERICAN | CRF | |
| 3 | ABC789 | DM | ABC789-010-003 | | | CRACE8 | Collected Race 8 | BLACK | CRF | |

## Example 7

**CRF Mock Example**

The CRF presents 5 racial designations plus "Unknown" and "Other" options:
- American Indian or Alaska Native
- Asian
- Black or African American
- Native Hawaiian or Other Pacific Islander
- White
- Unknown
- Other

Additional fields: "What was the other race?" (RACEOTH → SUPPDM.QVAL where SUPPDM.QNAM = "RACEOTH") and "If Unknown, please specify:" (RACEREAS → SUPPDM.QVAL where SUPPDM.QNAM = "RACEREAS").

**Rows 1-2:** Subjects self-identify to 1 of the first 5 race options on the CRF form.

**Row 3:** Subject did not self-identify to 1 of the existing race options and selected "Other". RACE was populated with "OTHER" in this case.

**Row 4:** Subject could not self-identify to any of the race options including identification of an "Other". RACE was populated with "UNKNOWN" in this case.

**Note:** Not all DM variables are shown.

**dm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SUBJID | AGE | AGEU | SEX | RACE | ETHNIC |
|-----|---------|--------|---------|--------|-----|------|-----|------|--------|
| 1 | ABC789 | DM | ABC789-010-045 | 010-045 | 20 | YEARS | M | WHITE | HISPANIC OR LATINO |
| 2 | ABC789 | DM | ABC789-010-046 | 010-046 | 21 | YEARS | F | ASIAN | NOT HISPANIC OR LATINO |
| 3 | ABC789 | DM | ABC789-010-047 | 010-047 | 24 | YEARS | F | OTHER | HISPANIC OR LATINO |
| 4 | ABC789 | DM | ABC789-010-048 | 010-048 | 33 | YEARS | M | UNKNOWN | HISPANIC OR LATINO |

**Row 1:** Sponsor allowed for an "Other" option to be collected, where its specify details are in SUPPDM.

**Row 2:** Sponsor allowed for an "Unknown" option to be collected, where its reason is collected in SUPPDM.

**Note:** Recommended QNAM-QLABEL values have been provided.

**suppdm.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC789 | DM | ABC789-010-047 | | | RACEOTH | Race, Other | BRAZILIAN | CRF | |
| 2 | ABC789 | DM | ABC789-010-048 | | | RACEREAS | Race, Reason Details | REFUGEE - DO NOT KNOW MY RACE | CRF | |
