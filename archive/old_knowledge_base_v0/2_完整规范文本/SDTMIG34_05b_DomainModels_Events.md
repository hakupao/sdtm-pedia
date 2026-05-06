# SDTMIG v3.4 --- Domain Models: Events — Part 2

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 2/2 — 6.2.4-6.2.7: DS, HO, MH, DV
> **Original:** `SDTMIG34_05_DomainModels_Events.md`
> **Related:** `SDTMIG34_05a_DomainModels_Events.md`

---

## 6.2.4 Disposition (DS)

### DS — Description/Overview

An events domain that contains information encompassing and representing data related to subject disposition.

### DS — Specification

**ds.xpt, Disposition — Events, One record per disposition status or protocol milestone per subject, Tabulation.**

| # | Variable | Label | Type | Controlled Terms / Format | Role | Core | CDISC Notes |
|---|----------|-------|------|---------------------------|------|------|-------------|
| 1 | STUDYID | Study Identifier | Char | | Identifier | Req | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | DS | Identifier | Req | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | | Identifier | Req | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | DSSEQ | Sequence Number | Num | | Identifier | Req | Sequence number given to ensure uniqueness of subject records within a domain. May be any valid number. |
| 5 | DSGRPID | Group ID | Char | | Identifier | Perm | Used to tie together a block of related records in a single domain for a subject. |
| 6 | DSREFID | Reference ID | Char | | Identifier | Perm | Internal or external identifier. |
| 7 | DSSPID | Sponsor-Defined Identifier | Char | | Identifier | Perm | Sponsor-defined reference number. Example: Line number on a Disposition page. |
| 8 | DSTERM | Reported Term for the Disposition Event | Char | | Topic | Req | Verbatim name of the event or protocol milestone. Some terms in DSTERM will match DSDECOD, but others, such as "Subject moved", will map to controlled terminology in DSDECOD, such as "LOST TO FOLLOW-UP". |
| 9 | DSDECOD | Standardized Disposition Term | Char | C66727; C114118; C150811 | Synonym Qualifier | Req | Controlled terminology for the name of disposition event or protocol milestone. There are separate codelists: "NCOMPLT" for disposition events, "PROTMLST" for protocol milestones, and "OTHEVENT" for other events. |
| 10 | DSCAT | Category for Disposition Event | Char | C74558 | Grouping Qualifier | Exp | Used to define a category of related records. |
| 11 | DSSCAT | Subcategory for Disposition Event | Char | C170443 | Grouping Qualifier | Perm | A further categorization of DSCAT (e.g., "STUDY PARTICIPATION", "STUDY TREATMENT" when DSCAT = "DISPOSITION EVENT"). |
| 12 | EPOCH | Epoch | Char | C99079 | Timing | Perm | Epoch associated with the start date/time of the event. |
| 13 | DSDTC | Date/Time of Collection | Char | ISO 8601 | Timing | Perm | Collection date and time of the disposition observation. |
| 14 | DSSTDTC | Start Date/Time of Disposition Event | Char | ISO 8601 | Timing | Exp | Start date/time of the disposition event. |
| 15 | DSDY | Study Day of Collection | Num | | Timing | Perm | Study day of collection of event relative to the sponsor-defined RFSTDTC. |
| 16 | DSSTDY | Study Day of Start of Disposition Event | Num | | Timing | Exp | Study day of start of event relative to the sponsor-defined RFSTDTC. |

### DS — Assumptions

1. The Disposition (DS) dataset provides an accounting for all subjects who entered the study and may include protocol milestones, such as randomization, as well as the subject's completion status or reason for discontinuation for the entire study or each phase or segment of the study, including screening and post-treatment follow-up. Sponsors may choose which disposition events and milestones to submit for a study. See ICH E3, Section 10.1.

2. **Categorization**
   - **(a)** DSCAT is used to distinguish between disposition events, protocol milestones, and other events. The controlled terminology for DSCAT consists of "DISPOSITION EVENT", "PROTOCOL MILESTONE", and "OTHER EVENT".
   - **(b)** An event with DSCAT = "DISPOSITION EVENT" describes either disposition of study participation or of a study treatment. If disposition events for both study participation and study treatment(s) are to be represented, then DSSCAT provides this distinction:
     - **(i)** DSSCAT = "STUDY PARTICIPATION" is used to represent disposition of study participation.
     - **(ii)** DSSCAT = "STUDY TREATMENT" is used when a study has only a single treatment.
     - **(iii)** If a study has multiple treatments, then DSSCAT should name the individual treatment.
   - **(c)** DSSCAT may be used when DSCAT = "PROTOCOL MILESTONE" or "OTHER EVENT", but would be subject to additional CDISC Controlled Terminology.
   - **(d)** An event with DSCAT = "PROTOCOL MILESTONE" is a protocol-specified, point-in-time event. Common protocol milestones include "INFORMED CONSENT OBTAINED" and "RANDOMIZED."
   - **(e)** An event with DSCAT = "OTHER EVENT" is another important event that occurred during a trial, but was not driven by protocol requirements and was not captured in another Events or Interventions class dataset. "TREATMENT UNBLINDED" is an example.
   - **(f)** Associations between DSCAT and some DSDECOD codelist values are described in the DS Codetable (available at https://www.cdisc.org/standards/terminology/controlled-terminology).

3. **DS description and coding**
   - **(a)** DSDECOD values are drawn from controlled terminology. The controlled terminology depends on the value of DSCAT.
   - **(b)** When DSCAT = "DISPOSITION EVENT", DSTERM contains either "COMPLETED" or specific verbatim information about the reason for non-completion.
     - **(i)** When DSTERM = "COMPLETED", DSDECOD is the term "COMPLETED" from the Controlled Terminology codelist NCOMPLT.
     - **(ii)** When DSTERM contains verbatim text, DSDECOD will use the extensible Controlled Terminology codelist NCOMPLT. For example, DSTERM = "Subject moved" might be coded to DSDECOD = "LOST TO FOLLOW-UP".
   - **(c)** When DSCAT = "PROTOCOL MILESTONE", DSTERM contains the verbatim/standardized text, DSDECOD will use the extensible Controlled Terminology codelist PROTMLST.
   - **(d)** When DSCAT = "OTHER EVENT", DSDECOD uses sponsor terminology.
     - **(i)** If a reason for the event was collected, the reason is in DSTERM and the DSDECOD is a term from sponsor terminology.
     - **(ii)** If no reason was collected, then DSTERM should be populated with the value in DSDECOD.

4. **Timing variables**
   - **(a)** DSSTDTC is expected and is used for the date/time of the disposition event. Events represented in the DS domain do not have end dates; disposition events do not span an interval, but rather occur at a single date/time.
   - **(b)** DSSTDTC documents the date/time that a protocol milestone, disposition event, or other event occurred. For an event with DSCAT = "DISPOSITION EVENT" where DSTERM is not "COMPLETED", the reason for non-completion may be related to an observation reported in another dataset. DSSTDTC is the date/time that the Epoch was completed and is not necessarily the same as the date/time of the observation that led to discontinuation.

     > For example, a subject reported severe vertigo on June 1, 2006 (AESTDTC). After ruling out other possible causes, the investigator decided to discontinue study treatment on June 6, 2006 (DSSTDTC). The subject reported that the vertigo had resolved on June 8, 2006 (AEENDTC).

   - **(c)** EPOCH may be included as a timing variable. In DS, EPOCH is based on DSSTDTC. The values of EPOCH are drawn from the Trial Arms (TA) dataset (see Section 7.2.1).

5. **Reasons for termination:** ICH E3 Section 10.1 indicates that "the specific reason for discontinuation" should be presented. The CDISC SDS Team interprets this guidance as requiring 1 standardized disposition term (DSDECOD) per disposition event. If multiple reasons are reported, the sponsor should identify a primary reason and use that to populate DSTERM and DSDECOD. Additional reasons should be submitted in SUPPDS.

   > For example, in a case where DSTERM = "SEVERE NAUSEA" and DSDECOD = "ADVERSE EVENT", SUPPDS might include:
   > - QNAM = "DSTERM1", QLABEL = "Reported Term for Disposition Event 1", QVAL = "SUBJECT REFUSED FURTHER TREATMENT"
   > - QNAM = "DSDECOD1", QLABEL = "Standardized Disposition Term 1", QVAL = "WITHDREW CONSENT"

6. Any identifier variables, timing variables, or Events general observation-class qualifiers may be added to the DS domain, but the following Qualifiers would generally not be used: --PRESP, --OCCUR, --STAT, --REASND, --BODSYS, --LOC, --SEV, --SER, --ACN, --ACNOTH, --REL, --RELNST, --PATT, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --CONTRT, --TOXGR.

### DS — Examples

#### Example 1

In this example, disposition of study participation was collected for each epoch of a trial. Disposition of study participation is indicated by DSCAT = "DISPOSITION EVENT". EPOCH was taken from the CRF. Data about disposition of study treatment was not collected, but the sponsor populated DSSCAT with "STUDY PARTICIPATION". Data were also collected about several protocol milestones represented with DSCAT = "PROTOCOL MILESTONE".

- **Rows 1, 2, 6, 8, 9, 12, 13, 17, 18:** Show records for protocol milestones. DSTERM and DSDECOD are populated with the same value. Note that for randomization events, EPOCH = "SCREENING", because randomization occurred before the start of treatment.
- **Rows 3-5:** Show 3 records for a subject who completed 3 stages of the study ("SCREENING", "TREATMENT", "FOLLOW-UP").
- **Row 7:** Shows disposition of a subject who was a screen failure. The verbatim reason is in DSTERM. DSDECOD is "PROTOCOL VIOLATION".
- **Rows 10-11:** Show disposition of a subject who completed screening but did not complete the treatment stage.
- **Rows 14-16:** Show disposition of a subject who completed treatment, but did not complete follow-up. Note that DSDTC was different from DSSTDTC for the death event.
- **Rows 19-21:** Show disposition of a subject who discontinued treatment due to an adverse event, but completed the follow-up phase.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSDTC | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|-------|---------|
| 1 | ABC123 | DS | 123101 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-09-21 | 2003-09-21 |
| 2 | ABC123 | DS | 123101 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2003-09-30 | 2003-09-30 |
| 3 | ABC123 | DS | 123101 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-09-30 | 2003-09-29 |
| 4 | ABC123 | DS | 123101 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2003-10-31 | 2003-10-31 |
| 5 | ABC123 | DS | 123101 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2003-11-15 | 2003-11-15 |
| 6 | ABC123 | DS | 123102 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-11-21 | 2003-11-21 |
| 7 | ABC123 | DS | 123102 | 2 | SUBJECT DENIED MRI PROCEDURE | PROTOCOL VIOLATION | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-11-22 | 2003-11-20 |
| 8 | ABC123 | DS | 123103 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-09-15 | 2003-09-15 |
| 9 | ABC123 | DS | 123103 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2003-09-30 | 2003-09-30 |
| 10 | ABC123 | DS | 123103 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-09-30 | 2003-09-22 |
| 11 | ABC123 | DS | 123103 | 4 | SUBJECT MOVED | LOST TO FOLLOW-UP | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2003-10-31 | 2003-10-31 |
| 12 | ABC123 | DS | 123104 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-09-15 | 2003-09-15 |
| 13 | ABC123 | DS | 123104 | 3 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2003-09-30 | 2003-09-30 |
| 14 | ABC123 | DS | 123104 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-09-30 | 2003-09-22 |
| 15 | ABC123 | DS | 123104 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2003-10-15 | 2003-10-15 |
| 16 | ABC123 | DS | 123104 | 5 | AUTOMOBILE ACCIDENT | DEATH | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2003-10-31 | 2003-10-29 |
| 17 | ABC123 | DS | 123105 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-09-28 | 2003-09-28 |
| 18 | ABC123 | DS | 123105 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2003-10-02 | 2003-10-02 |
| 19 | ABC123 | DS | 123105 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-10-02 | 2003-10-02 |
| 20 | ABC123 | DS | 123105 | 4 | ANEMIA | ADVERSE EVENT | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2003-10-17 | 2003-10-17 |
| 21 | ABC123 | DS | 123105 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2003-11-02 | 2003-11-02 |

#### Example 2

In this example, the sponsor has chosen to simply submit whether or not subjects completed the study, so there is only 1 record per subject. The sponsor did not collect disposition of treatment and did not include DSSCAT. EPOCH was populated as a timing variable, and represents the epoch during which the subject discontinued.

- **Row 1:** Subject 456101 completed the study. EPOCH = "FOLLOW-UP", which was the last epoch in the design of this study.
- **Rows 2-3:** Subjects 456102 and 456103 discontinued. Both discontinued participation during the treatment epoch.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|---------|
| 1 | ABC456 | DS | 456101 | 1 | COMPLETED | COMPLETED | DISPOSITION EVENT | FOLLOW-UP | 2003-09-21 |
| 2 | ABC456 | DS | 456102 | 1 | SUBJECT TAKING STUDY MED ERRATICALLY | PROTOCOL VIOLATION | DISPOSITION EVENT | TREATMENT | 2003-09-29 |
| 3 | ABC456 | DS | 456103 | 1 | LOST TO FOLLOW-UP | LOST TO FOLLOW-UP | DISPOSITION EVENT | TREATMENT | 2003-10-15 |

#### Example 3

In this study, disposition of study participation was collected for the treatment and follow-up epochs. For these records, the value in EPOCH was taken from the CRF. Data on screen failures were not submitted for this study, so all submitted subjects completed screening; the sponsor chose not to collect data on disposition of the screening epoch. Data on protocol milestones were not collected, but data were collected if a subject's treatment was unblinded. For these records, EPOCH represents the epoch during which the blind was broken.

- **Row 1, 2:** Subject 789101 completed the treatment and follow-up phases.
- **Rows 3, 5:** Subject 789102 did not complete the treatment phase but did complete the follow-up phase.
- **Row 4:** Subject 789102's treatment was unblinded. The date of the unblinding is represented in DSSTDTC. Maintaining the blind as per protocol was not considered to be an "event" because there was no change in the subject's state.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|---------|
| 1 | ABC789 | DS | 789101 | 1 | COMPLETED | COMPLETED | DISPOSITION EVENT | TREATMENT | 2004-09-12 |
| 2 | ABC789 | DS | 789101 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | FOLLOW-UP | 2004-12-20 |
| 3 | ABC789 | DS | 789102 | 1 | SKIN RASH | ADVERSE EVENT | DISPOSITION EVENT | TREATMENT | 2004-09-30 |
| 4 | ABC789 | DS | 789102 | 2 | SUBJECT HAD SEVERE RASH | TREATMENT UNBLINDED | OTHER EVENT | TREATMENT | 2004-10-01 |
| 5 | ABC789 | DS | 789102 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | FOLLOW-UP | 2004-12-28 |

#### Example 4

In this example, the CRF included collection of an AE number when study participation was incomplete due to an adverse event. The relationship between the DS record and the AE record was represented in a RELREC dataset. The DS domain represents the end of the subject's participation in the study, due to their death from heart failure. In this case, the disposition was collected (DSDTC) on the same day that death occurred and the subject's study participation ended (DSSTDTC).

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | EPOCH | DSDTC | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|-------|---------|
| 1 | ABC123 | DS | 123102 | 1 | Heart Failure | DEATH | DISPOSITION EVENT | TREATMENT | 2003-09-29 | 2003-09-29 |

The heart failure is represented as an adverse event. In order to save space, only 2 of the MedDRA coding variables for the adverse event have been included.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AESTDTC | AEENDTC | AEDECOD | AESOC | AESEV | AESER | AEACN | AEREL | AEOUT | AESCAN | AESCONG | AESDISAB | AESDTH | AESHOSP | AESLIFE | AESOD | AESMIE |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|-------|-------|-------|-------|-------|-------|--------|---------|----------|--------|---------|---------|-------|--------|
| 1 | ABC123 | AE | 123102 | 1 | Heart Failure | 2003-09-29 | 2003-09-29 | HEART FAILURE | CARDIOVASCULAR SYSTEM | SEVERE | Y | NOT APPLICABLE | DEFINITELY NOT RELATED | FATAL | N | N | N | Y | N | N | N | N |

The relationship between the DS and AE records is represented in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC123 | DS | 123102 | DSSEQ | 1 | | 1 |
| 2 | ABC123 | AE | 123102 | AESEQ | 1 | | 1 |

> **Note:** The subject's DM record is not shown, but included DTHFL = "Y" and the date of death.

#### Example 5

This example represents a multidrug (isoniazid and levofloxacin) investigational treatment trial for multidrug-resistant tuberculosis (MDR-TB). The protocol allows for a subject to discontinue levofloxacin and continue single treatment of isoniazid throughout the remainder of the study. Disposition of study participation and disposition of each drug was collected. Whether a record with DSCAT = "DISPOSITION EVENT" represents disposition of the subject's participation in the study or disposition of a study treatment is represented in DSSCAT. In this example, disposition of the study and of each drug a subject received for each of the study's 2 treatment epochs.

- **Row 1:** Indicates that the physician, per protocol, removed levofloxacin treatment due to high-level positive cultures. This record represents the treatment discontinuation for levofloxacin, for the first treatment epoch. Note that because this subject did not receive levofloxacin during the second treatment epoch, there is no record for DSSCAT = "LEVOFLOXACIN" with EPOCH = "TREATMENT 2".
- **Rows 2, 4:** Represent the treatment continuation and completion for isoniazid each treatment epoch, as indicated by DSSCAT = "ISONIAZID".
- **Rows 3, 5:** Represent the study disposition for each treatment epoch, as indicated by DSSCAT = "STUDY PARTICIPATION".

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | PERSISTENT HIGH-LEVEL POSITIVE CULTURES, PER PROTOCOL, LEVOFLOXACIN REMOVAL RECOMMENDED | PHYSICIAN DECISION | DISPOSITION EVENT | LEVOFLOXACIN | TREATMENT 1 | 2016-02-15 |
| 2 | XXX | DS | XXX-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | ISONIAZID | TREATMENT 1 | 2016-02-15 |
| 3 | XXX | DS | XXX-767-001 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-02-25 |
| 4 | XXX | DS | XXX-767-001 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | ISONIAZID | TREATMENT 2 | 2016-03-14 |
| 5 | XXX | DS | XXX-767-001 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-03-24 |

#### Example 6

This example is for a study of a multidrug (isoniazid and levofloxacin) investigational treatment for MDR-TB. The protocol allowed a subject to discontinue levofloxacin and continue single treatment of isoniazid throughout the remainder of the study. Disposition of study participation and of each study treatment was collected. For records of disposition of the subject's participation in the study DSSCAT = "STUDY PARTICIPATION", whereas for records of disposition of a study treatment DSSCAT is the name of the treatment.

- **Row 1:** Represents the final treatment disposition for levofloxacin, as indicated by DSSCAT = "LEVOFLOXACIN". The physician removed levofloxacin treatment due to high-level positive cultures, as allowed by the protocol.
- **Row 2:** Represents the final treatment completion of isoniazid within the trial, which is indicated by DSSCAT = "ISONIAZID".
- **Row 3:** Represents the final study completion within the trial, which is indicated by DSSCAT = "STUDY PARTICIPATION".

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | PERSISTENT HIGH-LEVEL POSITIVE CULTURES, PER PROTOCOL, LEVOFLOXACIN REMOVAL RECOMMENDED | PHYSICIAN DECISION | DISPOSITION EVENT | LEVOFLOXACIN | TREATMENT 1 | 2016-02-15 |
| 2 | XXX | DS | XXX-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | ISONIAZID | TREATMENT 2 | 2016-03-14 |
| 3 | XXX | DS | XXX-767-001 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-03-24 |

#### Example 7

This is an example of a trial with a single investigative treatment. The sponsor used the generic DSSCAT value "STUDY TREATMENT" rather than the name of the treatment. This subject discontinued both treatment and study participation due to an adverse event.

- **Rows 1, 3:** Represent the disposition of treatment for each treatment epoch, as indicated by DSSCAT = "STUDY TREATMENT".
- **Rows 2, 4:** Represent the disposition of study participation continuation for each treatment epoch, as indicated by DSSCAT = "STUDY PARTICIPATION".

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY TREATMENT | TREATMENT 1 | 2016-02-15 |
| 2 | XXX | DS | XXX-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-02-15 |
| 3 | XXX | DS | XXX-767-001 | 3 | SKIN RASH | ADVERSE EVENT | DISPOSITION EVENT | STUDY TREATMENT | TREATMENT 2 | 2016-03-14 |
| 4 | XXX | DS | XXX-767-001 | 4 | SKIN RASH | ADVERSE EVENT | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-03-14 |

#### Example 8

This example represents data for an ongoing blinded study in which each subject received 2 treatments, identified by the sponsor as "BLINDED DRUG A" and "BLINDED DRUG B". Disposition of study participation and of each of the 2 blinded treatments was collected for each of the 2 treatment epochs in the study. The subject in this example completed study participation and both treatments for both treatment epochs.

- **Rows 1, 2, 4, 5:** Represent the disposition of the blinded treatments for each of the 2 treatment epochs for each of the 2 treatments, indicated by DSSCAT = "BLINDED DRUG A" and DSSCAT = "BLINDED DRUG B".
- **Rows 3, 6:** Represent the disposition of study participation for each of the 2 treatment epochs, as indicated by DSSCAT = "STUDY PARTICIPATION".

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | COMPLETED | COMPLETED | DISPOSITION EVENT | BLINDED DRUG A | TREATMENT 1 | 2016-02-15 |
| 2 | XXX | DS | XXX-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | BLINDED DRUG B | TREATMENT 1 | 2016-02-15 |
| 3 | XXX | DS | XXX-767-001 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-02-25 |
| 4 | XXX | DS | XXX-767-001 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | BLINDED DRUG A | TREATMENT 2 | 2016-03-14 |
| 5 | XXX | DS | XXX-767-001 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | BLINDED DRUG B | TREATMENT 2 | 2016-03-14 |
| 6 | XXX | DS | XXX-767-001 | 6 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-03-24 |

#### Example 9

This example is for a study in which multiple informed consents were collected. DSTERM is populated with a full description of the informed consent. DSDECOD is populated with the standardized value "INFORMED CONSENT OBTAINED" from the Protocol Milestone (PROTMLST) codelist. For all informed consent records, DSCAT = "PROTOCOL MILESTONE". The sponsor chose to include the EPOCH timing variable, to indicate the epoch during which each protocol milestone occurred.

- **Row 1:** Shows the obtaining of the initial study informed consent.
- **Row 2:** Shows randomization, another event with DSCAT = "PROTOCOL MILESTONE".
- **Rows 3-5:** Show 3 additional informed consents obtained during the trial.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | INFORMED CONSENT FOR STUDY ENROLLMENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | SCREENING | 2016-02-22 |
| 2 | XXX | DS | XXX-767-001 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | SCREENING | 2016-02-26 |
| 3 | XXX | DS | XXX-767-001 | 3 | INFORMED CONSENT FOR AMENDMENT ONE OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | TREATMENT 1 | 2016-04-12 |
| 4 | XXX | DS | XXX-767-001 | 4 | INFORMED CONSENT FOR PHARMACOGENETIC RESEARCH OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | TREATMENT 2 | 2016-06-08 |
| 5 | XXX | DS | XXX-767-001 | 5 | INFORMED CONSENT FOR PK SUB-STUDY OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | TREATMENT 2 | 2016-06-23 |

#### Example 10

This example represents data for 2 subjects who participated in a study with multiple treatment periods. During the first treatment period, subjects were randomized to drug 1 or drug 2. The second treatment phase added the investigational drug to drug 1 and drug 2. Disposition of study drugs and study participation was collected at the end of each epoch. DSSCAT was used to distinguish between disposition of study drugs vs. study participation. The supporting Demographics (DM), Exposure (EX), Trial Elements (TE), Trial Arms (TA), and Subject Elements (SE) datasets have been provided for additional context. Not all records are shown in the supporting example datasets.

The elements used in the TA dataset are defined in the TE dataset.

**te.xpt**

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
|-----|---------|--------|------|---------|--------|--------|-------|
| 1 | XYZ | TE | SCRN | Screen | Informed Consent | 1 week after start of Element | P7D |
| 2 | XYZ | TE | DRUG1 | Drug 1 | First dose of Drug 1 | 4 weeks after start of Element | P28D |
| 3 | XYZ | TE | DRUG2 | Drug 2 | First dose of Drug 2 | 4 weeks after start of Element | P28D |
| 4 | XYZ | TE | DG1INDG | Drug 1 + Investigation Drug | First dose of Investigational Drug, where Investigational Drug is given with Drug 1. | 1 week after start of Element | P7D |
| 5 | XYZ | TE | DG2INDG | Drug 2 + Investigation Drug | First dose of Investigational Drug, where Investigational Drug is given with Drug 2. | 1 week after start of Element | P7D |
| 6 | XYZ | TE | FU | Follow-up | One day after last administration of study drug. | | |

The TA dataset describes the design of the study.

**ta.xpt**

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
|-----|---------|--------|-------|-----|---------|------|---------|----------|---------|-------|
| 1 | XYZ | TA | DG1INDG | Drug-1+Investigation-Drug | 1 | SCRN | Screen | Randomized to DG1INDG | | SCREENING |
| 2 | XYZ | TA | DG1INDG | Drug-1+Investigation-Drug | 2 | DRUG1 | Drug-1 | | | TREATMENT 1 |
| 3 | XYZ | TA | DG1INDG | Drug-1+Investigation-Drug | 3 | DG1INDG | Drug 1 + Investigation Drug | | | TREATMENT 2 |
| 4 | XYZ | TA | DG1INDG | Drug-1+Investigation-Drug | 4 | FU | Follow-up | | | FOLLOW-UP |
| 5 | XYZ | TA | DG2INDG | Drug-2+Investigation-Drug | 1 | SCRN | Screen | Randomized to DG2INDG | | SCREENING |
| 6 | XYZ | TA | DG2INDG | Drug-2+Investigation-Drug | 2 | DRUG2 | Drug-2 | | | TREATMENT 1 |
| 7 | XYZ | TA | DG2INDG | Drug-2+Investigation-Drug | 3 | DG2INDG | Drug 2 + Investigation Drug | | | TREATMENT 2 |
| 8 | XYZ | TA | DG2INDG | Drug-2+Investigation-Drug | 4 | FU | Follow-up | | | FOLLOW-UP |

The DM dataset includes the arm to which the subjects were randomized, and the dates of informed consent, start of study treatment, end of study treatment, and end of study participation.

**dm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SUBJID | RFXSTDTC | RFXENDTC | RFICDTC | RFPENDTC | SITEID | INVNAM | ARMCD | ARM | ACTARMCD | ACTARM |
|-----|---------|--------|---------|--------|----------|----------|---------|----------|--------|--------|-------|-----|----------|--------|
| 1 | XYZ | DM | XYZ-767-001 | 001 | 2016-02-14 | 2016-04-19 | 2016-02-02 | 2016-04-24 | 01 | ADAMS, M | DG1INDG | Drug-1+Investigation-Drug | DG1INDG | Drug-1+Investigation-Drug |
| 3 | XYZ | DM | XYZ-767-002 | 002 | 2016-02-21 | 2016-04-24 | 2016-02-04 | 2016-04-29 | 01 | ADAMS, M | DG2INDG | Drug-2+Investigation-Drug | DG2INDG | Drug-2+Investigation-Drug |

The EX dataset shows the administration of study treatments.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXTRT | EXDOSE | EXDOSU | EPOCH | EXSTDTC | EXENDTC |
|-----|---------|--------|---------|-------|-------|--------|--------|-------|---------|---------|
| 1 | XYZ | EX | XYZ-767-001 | 1 | Drug 1 | 500 | mg | TREATMENT 1 | 2016-02-14 | 2016-03-13 |
| 2 | XYZ | EX | XYZ-767-001 | 2 | Drug 1 | 500 | mg | TREATMENT 2 | 2016-03-14 | 2016-04-19 |
| 3 | XYZ | EX | XYZ-767-001 | 3 | Investigational Drug | 1000 | mg | TREATMENT 2 | 2016-03-14 | 2016-04-19 |
| 4 | XYZ | EX | XYZ-767-002 | 1 | Drug 2 | 500 | mg | TREATMENT 1 | 2016-02-21 | 2016-03-23 |
| 5 | XYZ | EX | XYZ-767-002 | 2 | Drug 2 | 500 | mg | TREATMENT 2 | 2016-03-24 | 2016-04-24 |
| 6 | XYZ | EX | XYZ-767-002 | 3 | Investigational Drug | 1000 | mg | TREATMENT 2 | 2016-03-24 | 2016-04-24 |

The SE dataset shows the dates for the elements for each subject.

- **Rows 1, 5:** Represent the subjects' actual screening elements.
- **Rows 2, 6:** Represent the subjects' actual first treatment epochs. The 2 subjects were in different elements in the first treatment epoch.
- **Rows 3, 7:** Represent the subjects' actual second treatment epochs.
- **Rows 4, 8:** Represent the subjects' actual follow-up elements.

**se.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SDSEQ | ETCD | ELEMENT | SESTDTC | SEENDTC | TAETORD | EPOCH |
|-----|---------|--------|---------|-------|------|---------|---------|---------|---------|-------|
| 1 | XYZ | SE | XYZ-767-001 | 1 | SCREEN | Screen | 2016-02-02 | 2016-02-14 | 1 | SCREENING |
| 2 | XYZ | SE | XYZ-767-001 | 2 | DRUG1 | Drug-1 | 2016-02-14 | 2016-03-14 | 2 | TREATMENT 1 |
| 3 | XYZ | SE | XYZ-767-001 | 3 | DG1INDG | Drug 1 + Investigational Drug | 2016-03-14 | 2016-04-24 | 3 | TREATMENT 2 |
| 4 | XYZ | SE | XYZ-767-001 | 4 | FU | Follow-up | 2016-04-24 | 2016-04-24 | 4 | FOLLOW-UP |
| 5 | XYZ | SE | XYZ-767-002 | 1 | SCREEN | Screen | 2016-02-04 | 2016-02-21 | 1 | SCREENING |
| 6 | XYZ | SE | XYZ-767-002 | 2 | DRUG2 | Drug-2 | 2016-02-21 | 2016-03-24 | 2 | TREATMENT 1 |
| 7 | XYZ | SE | XYZ-767-002 | 3 | DG2INDG | Drug 2 + Investigational Drug | 2016-03-24 | 2016-04-29 | 3 | TREATMENT 2 |
| 8 | XYZ | SE | XYZ-767-002 | 4 | FU | Follow-up | 2016-04-29 | 2016-04-29 | 4 | FOLLOW-UP |

The DS dataset shows the disposition events and protocol milestones for each subject.

- **Rows 1, 8:** Show randomization to either DRUG 1 or DRUG 2 in the study.
- **Rows 2, 9:** Represent the completion of the screening phase of the study.
- **Rows 3, 5, 10, 12:** Represent the completion of drug for each EPOCH, where DSSCAT has the name of the drug(s). The DSSTDTC is the end date of study treatment for the epoch.
- **Rows 4, 6, 11, 13:** Represent the completion of study participation for each epoch. The DSSTDTC is the end date of study participation for the epoch. There was a 1-day evaluation post-treatment.
- **Rows 7, 14:** Represent the completion of the study participation follow-up epoch.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XYZ | DS | XYZ-767-001 | 1 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2016-02-13 |
| 2 | XYZ | DS | XYZ-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2016-02-13 |
| 3 | XYZ | DS | XYZ-767-001 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | DRUG1 | TREATMENT 1 | 2016-03-13 |
| 4 | XYZ | DS | XYZ-767-001 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-03-14 |
| 5 | XYZ | DS | XYZ-767-001 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | DG1INDG | TREATMENT 2 | 2016-04-19 |
| 6 | XYZ | DS | XYZ-767-001 | 6 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-04-20 |
| 7 | XYZ | DS | XYZ-767-001 | 7 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2016-04-24 |
| 8 | XYZ | DS | XYZ-767-002 | 1 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2016-02-20 |
| 9 | XYZ | DS | XYZ-767-002 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2016-02-20 |
| 10 | XYZ | DS | XYZ-767-002 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | DRUG2 | TREATMENT 1 | 2016-03-23 |
| 11 | XYZ | DS | XYZ-767-002 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-03-24 |
| 12 | XYZ | DS | XYZ-767-002 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | DG2INDG | TREATMENT 2 | 2016-04-24 |
| 13 | XYZ | DS | XYZ-767-002 | 6 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-04-25 |
| 14 | XYZ | DS | XYZ-767-002 | 7 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2016-04-29 |

#### Example 11

The study in this example had 4 cycles of treatment within the treatment epoch, and each cycle was represented as an element. The study compared a current standard treatment with drugs A and B to treatment with drugs A, B, and C. The protocol allowed for drug doses to be reduced under specified criteria. For drug C, these dose modifications could include dropping the drug. When drug C is dropped, the subject may transition to treatment with drugs A and B or to follow-up.

**te.xpt**

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
|-----|---------|--------|------|---------|--------|--------|-------|
| 1 | DS10 | TE | SCRN | Screen | Informed Consent | Screening assessments are complete, up to 2 weeks after start of Element | |
| 2 | DS10 | TE | AB | Trt AB | First dose of treatment Element, where treatment is AB | 4 weeks after start of Element | P4W |
| 3 | DS10 | TE | ABC | Trt ABC | First dose of treatment Element, where treatment AB +C | 4 weeks after start of Element | P4W |
| 4 | DS10 | TE | FU | Follow-up | Four weeks after start of last treatment element | Death, withdrawal of consent, or loss to follow-up. | |

The TA dataset describes the design of the study. The sponsor chose to number elements starting with zero for the screening element. For the ABC arm, if drug C is dropped, the subject may transition to an AB element or follow-up.

**ta.xpt**

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
|-----|---------|--------|-------|-----|---------|------|---------|----------|---------|-------|
| 1 | DS10 | TA | AB | AB | 0 | SCRN | Screen | Randomized to AB | | SCREENING |
| 2 | DS10 | TA | AB | AB | 1 | AB | Trt AB | | If disease progression, go to follow-up epoch. | TREATMENT |
| 3 | DS10 | TA | AB | AB | 2 | AB | Trt AB | | If disease progression, go to follow-up epoch. | TREATMENT |
| 4 | DS10 | TA | AB | AB | 3 | AB | Trt AB | | If disease progression, go to follow-up epoch. | TREATMENT |
| 5 | DS10 | TA | AB | AB | 4 | AB | Trt AB | | | TREATMENT |
| 6 | DS10 | TA | AB | AB | 5 | FU | Follow-up | | | FOLLOW-UP |
| 7 | DS10 | TA | ABC | ABC | 0 | SCRN | Screen | Randomized to ABC | | SCREENING |
| 8 | DS10 | TA | ABC | ABC | 1 | ABC | Trt ABC | | If disease progression, go to follow-up. If drug C is dropped, go to element with TAETORD = "5". | TREATMENT |
| 9 | DS10 | TA | ABC | ABC | 2 | ABC | Trt ABC | | If disease progression, go to follow-up. If drug C is dropped, go to element with TAETORD = "6". | TREATMENT |
| 10 | DS10 | TA | ABC | ABC | 3 | ABC | Trt ABC | | If disease progression, go to follow-up. If drug C is dropped, go to element with TAETORD = "7". | TREATMENT |
| 11 | DS10 | TA | ABC | ABC | 4 | ABC | Trt ABC | | Go to follow-up epoch. | TREATMENT |
| 12 | DS10 | TA | ABC | ABC | 5 | AB | Trt AB | | | TREATMENT |
| 13 | DS10 | TA | ABC | ABC | 6 | AB | Trt AB | | | TREATMENT |
| 14 | DS10 | TA | ABC | ABC | 7 | AB | Trt AB | | | TREATMENT |
| 15 | DS10 | TA | ABC | ABC | 8 | FU | Follow-up | | | FOLLOW-UP |

This example shows data for a subject who was randomized to treatment ABC. Drug C was dropped after cycle 2 due to toxicity associated with drug C. Treatment with drugs A and B was stopped after cycle 3 due to disease progression. The subject died during follow-up.

The SE dataset records the elements this subject experienced.

- **Rows 1-4:** The subject participated in the screening epoch and 3 elements of the treatment epoch.
- **Row 5:** The subject's fifth element was not "ABC" or "AB", as would have been expected if they received all 4 cycles of therapy, but "FU".

**se.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SESEQ | ETCD | SESTDTC | SEENDTC | SEUPDES | TAETORD | EPOCH |
|-----|---------|--------|---------|-------|------|---------|---------|---------|---------|-------|
| 1 | DS10 | SE | 101 | 1 | SCRN | 2015-01-21 | 2015-02-01 | | 0 | SCREENING |
| 2 | DS10 | SE | 101 | 2 | ABC | 2015-02-01 | 2015-03-01 | | 1 | TREATMENT |
| 3 | DS10 | SE | 101 | 3 | ABC | 2015-03-01 | 2015-03-29 | | 2 | TREATMENT |
| 4 | DS10 | SE | 101 | 4 | AB | 2015-03-29 | 2015-04-26 | | 6 | TREATMENT |
| 5 | DS10 | SE | 101 | 5 | FU | 2015-04-26 | 2015-09-19 | | 8 | FOLLOW-UP |

In this study, disposition of each treatment was collected, and disposition of study participation was collected for each epoch of the trial. The date of disposition for study treatment was defined as the date of the last dose of that treatment.

- **Rows 1-2:** Show that informed consent was obtained and randomization occurred during the screening epoch.
- **Row 3:** Shows disposition of study participation for the screening epoch. The subject completed this epoch.
- **Row 4:** Shows that drug C was ended during the second cycle (TAETORD = "2") of the treatment epoch.
- **Row 5:** Shows that drugs A and B were ended on the same day during the third cycle (TAETORD = "6") of the treatment epoch.
- **Row 6:** Shows disposition of study participation in the treatment epoch. The subject did not complete treatment, due to disease progression. The date of disposition of the treatment epoch, DSSTDTC, is the date the subject started the follow-up epoch.
- **Row 7:** Shows disposition of study participation in the follow-up epoch. The subject died.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | TAETORD | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|---------|-------|---------|
| 1 | DS10 | DS | 101 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | 1 | SCREENING | 2015-01-21 |
| 2 | DS10 | DS | 101 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | 1 | SCREENING | 2015-02-01 |
| 3 | DS10 | DS | 101 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | 1 | SCREENING | 2015-02-01 |
| 4 | DS10 | DS | 101 | 4 | Toxicity | ADVERSE EVENT | DISPOSITION EVENT | DRUG C | 2 | TREATMENT | 2015-03-06 |
| 5 | DS10 | DS | 101 | 5 | Disease progression | PROGRESSIVE DISEASE | DISPOSITION EVENT | DRUGS A & B | 6 | TREATMENT | 2015-04-14 |
| 6 | DS10 | DS | 101 | 6 | Disease progression | PROGRESSIVE DISEASE | DISPOSITION EVENT | STUDY PARTICIPATION | 6 | TREATMENT | 2015-04-26 |
| 7 | DS10 | DS | 101 | 7 | Death due to cancer | DEATH | DISPOSITION EVENT | STUDY PARTICIPATION | 8 | FOLLOW-UP | 2015-09-19 |

---

## 6.2.5 Healthcare Encounters (HO)

### HO — Description/Overview

An events domain that contains data for inpatient and outpatient healthcare events (e.g., hospitalization, nursing home stay, rehabilitation facility stay, ambulatory surgery).

### HO — Specification

**ho.xpt, Healthcare Encounters — Events, One record per healthcare encounter per subject, Tabulation.**

| # | Variable | Label | Type | Controlled Terms / Format | Role | Core | CDISC Notes |
|---|----------|-------|------|---------------------------|------|------|-------------|
| 1 | STUDYID | Study Identifier | Char | | Identifier | Req | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | HO | Identifier | Req | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | | Identifier | Req | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | HOSEQ | Sequence Number | Num | | Identifier | Req | Sequence number given to ensure uniqueness of subject records within a domain. |
| 5 | HOGRPID | Group ID | Char | | Identifier | Perm | Used to tie together a block of related records in a single domain for a subject. |
| 6 | HOREFID | Reference ID | Char | | Identifier | Perm | Internal or external healthcare encounter identifier. |
| 7 | HOSPID | Sponsor-Defined Identifier | Char | | Identifier | Perm | Sponsor-defined identifier. Example: Line number on a Healthcare Encounters CRF page. |
| 8 | HOTERM | Healthcare Encounter Term | Char | | Topic | Req | Verbatim or preprinted CRF term for the healthcare encounter. |
| 9 | HODECOD | Dictionary-Derived Term | Char | C171444 | Synonym Qualifier | Perm | Dictionary or sponsor-defined derived text description of HOTERM. |
| 10 | HOCAT | Category for Healthcare Encounter | Char | | Grouping Qualifier | Perm | Used to define a category of topic-related values. |
| 11 | HOSCAT | Subcategory for Healthcare Encounter | Char | | Grouping Qualifier | Perm | A further categorization of HOCAT values. |
| 12 | HOPRESP | Pre-Specified Healthcare Encounter | Char | C66742 | Variable Qualifier | Perm | A value of "Y" indicates this event was prespecified on the CRF. Values are null for spontaneously reported events. |
| 13 | HOOCCUR | Healthcare Encounter Occurrence | Char | C66742 | Record Qualifier | Perm | Used when the occurrence of specific encounters is solicited, to indicate whether an encounter occurred. |
| 14 | HOSTAT | Completion Status | Char | C66789 | Record Qualifier | Perm | Indicates that the prespecified question was not answered. |
| 15 | HOREASND | Reason Healthcare Encounter Not Done | Char | | Record Qualifier | Perm | Describes the reason data for a prespecified event were not collected. Used with HOSTAT when value is "NOT DONE". |
| 16 | TAETORD | Planned Order of Element within Arm | Num | | Timing | Perm | Number that gives the planned order of the element within the arm. |
| 17 | EPOCH | Epoch | Char | C99079 | Timing | Perm | Epoch associated with the start date/time of the healthcare encounter. |
| 18 | HODTC | Date/Time of Event Collection | Char | ISO 8601 | Timing | Perm | Collection date and time of the healthcare encounter. |
| 19 | HOSTDTC | Start Date/Time of Healthcare Encounter | Char | ISO 8601 | Timing | Exp | Start date/time of the healthcare encounter (e.g., date of admission). |
| 20 | HOENDTC | End Date/Time of Healthcare Encounter | Char | ISO 8601 | Timing | Perm | End date/time of the healthcare encounter (e.g., date of discharge). |
| 21 | HODY | Study Day of Event Collection | Num | | Timing | Perm | Study day of event collection relative to the sponsor-defined RFSTDTC. |
| 22 | HOSTDY | Study Day of Start of Encounter | Num | | Timing | Perm | Study day of the start of the healthcare encounter relative to RFSTDTC. |
| 23 | HOENDY | Study Day of End of Healthcare Encounter | Num | | Timing | Perm | Study day of the end of the healthcare encounter relative to RFSTDTC. |
| 24 | HODUR | Duration of Healthcare Encounter | Char | ISO 8601 | Timing | Perm | Collected duration of the healthcare encounter. Used only if collected on the CRF and not derived. Example: "P1DT2H". |
| 25 | HOSTRTPT | Start Relative to Reference Time Point | Char | C66728 | Timing | Perm | Identifies the start of the observation as being before or after the reference time point defined by HOSTTPT. See Section 4.4.7. |
| 26 | HOSTTPT | Start Reference Time Point | Char | | Timing | Perm | Description or date/time in ISO 8601 of the reference point referred to by HOSTRTPT. |
| 27 | HOENRTPT | End Relative to Reference Time Point | Char | C66728 | Timing | Perm | Identifies the end of the event as being before or after the reference time point defined by HOENTPT. See Section 4.4.7. |
| 28 | HOENTPT | End Reference Time Point | Char | | Timing | Perm | Description or date/time in ISO 8601 of the reference point referred to by HOENRTPT. |

### HO — Assumptions

1. The Healthcare Encounters (HO) dataset includes inpatient and outpatient healthcare events (e.g., hospitalizations, nursing home stays, rehabilitation facility stays, ambulatory surgery).

2. Values of HOTERM typically describe the location or place of the healthcare encounter (e.g., "HOSPITAL" rather than "HOSPITALIZATION"). HOSTDTC should represent the start or admission date and HOENDTC the end or discharge date.

3. **Data collected about healthcare encounters** may include the reason for the encounter. The following supplemental qualifiers may be appropriate:
   - **(a)** The supplemental qualifier with QNAM = "HOINDC" would be used to represent the indication/medical condition for the encounter (e.g., stroke). Note that --INDC is an Interventions class variable, so is not a standard variable for HO.
   - **(b)** The supplemental qualifier with QNAM = "HOREAS" would be used to represent a reason for the encounter other than a medical condition (e.g., annual checkup).

4. If collected data includes the name of the provider or the facility where the encounter took place, this may be represented using the supplemental qualifier with QNAM = "HONAM". Note that --NAM is a Findings class variable, so is not a standard variable for HO.

5. Any identifier variables, timing variables, or Events general observation-class qualifiers may be added to the HO domain, but the following Qualifiers would generally not be used: --SER, --ACN, --ACNOTH, --REL, --RELNST, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --BODSYS, --LOC, --SEV, --TOX, --TOXGR, --PATT, --CONTRT.

### HO — Examples

#### Example 1

In this example, a healthcare encounter CRF collects verbatim descriptions of the encounter.

- **Rows 1-2:** Subject ABC123101 was hospitalized and then moved to a nursing home.
- **Rows 3-5:** Subject ABC123102 was in a hospital in the general ward and then in the intensive care unit. This same subject was transferred to a rehabilitation facility.
- **Rows 6-7:** Subject ABC123103 has 2 hospitalization records.
- **Row 8:** Subject ABC123104 was seen in the cardiac catheterization laboratory.
- **Rows 9-12:** Subject ABC123105 and subject ABC123106 were each seen in the cardiac catheterization laboratory and then transferred to another hospital.

**ho.xpt**

| Row | STUDYID | DOMAIN | USUBJID | HOSEQ | HOTERM | EPOCH | HOSTDTC | HOENDTC | HODUR |
|-----|---------|--------|---------|-------|--------|-------|---------|---------|-------|
| 1 | ABC | HO | ABC123101 | 1 | HOSPITAL | TREATMENT | 2011-06-08 | 2011-06-13 | |
| 2 | ABC | HO | ABC123101 | 2 | NURSING HOME | TREATMENT | | | P6D |
| 3 | ABC | HO | ABC123102 | 1 | GENERAL WARD | TREATMENT | 2011-08-06 | 2011-08-08 | |
| 4 | ABC | HO | ABC123102 | 2 | INTENSIVE CARE | TREATMENT | 2011-08-08 | 2011-08-15 | |
| 5 | ABC | HO | ABC123102 | 3 | REHABILITATION FACILITY | TREATMENT | 2011-08-15 | 2011-08-20 | |
| 6 | ABC | HO | ABC123103 | 1 | HOSPITAL | TREATMENT | 2011-09-09 | 2011-09-11 | |
| 7 | ABC | HO | ABC123103 | 2 | HOSPITAL | TREATMENT | 2011-09-11 | 2011-09-15 | |
| 8 | ABC | HO | ABC123104 | 1 | CARDIAC CATHETERIZATION LABORATORY | TREATMENT | 2011-10-10 | 2011-10-10 | |
| 9 | ABC | HO | ABC123105 | 1 | CARDIAC CATHETERIZATION LABORATORY | TREATMENT | 2011-10-11 | 2011-10-11 | |
| 10 | ABC | HO | ABC123105 | 2 | HOSPITAL | TREATMENT | 2011-10-11 | 2011-10-15 | |
| 11 | ABC | HO | ABC123106 | 1 | CARDIAC CATHETERIZATION LABORATORY | FOLLOW-UP | 2011-11-07 | 2011-11-07 | |
| 12 | ABC | HO | ABC123106 | 2 | HOSPITAL | FOLLOW-UP | 2011-11-07 | 2011-11-09 | |

- **Row 1:** For the first encounter recorded for subject ABC123101, the indication/medical condition for hospitalization was recorded.
- **Row 2:** For the second encounter recorded for subject ABC123101, the reason for admission to a nursing home was for rehabilitation.
- **Rows 3-4:** For the 2 encounters recorded for subject ABC123103, the names of the facilities were recorded.
- **Row 5:** For the first encounter for subject ABC123105, the indication/medical condition for the hospitalization was recorded.
- **Row 6:** For the second encounter for subject ABC123105, the name of the hospital was recorded.

**suppho.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | HO | ABC123101 | HOSEQ | 1 | HOINDC | Indication | CONGESTIVE HEART FAILURE | CRF | |
| 2 | ABC | HO | ABC123101 | HOSEQ | 2 | HOREAS | Reason | REHABILITATION | CRF | |
| 3 | ABC | HO | ABC123103 | HOSEQ | 1 | HONAM | Provider Name | GENERAL HOSPITAL | CRF | |
| 4 | ABC | HO | ABC123103 | HOSEQ | 2 | HONAM | Provider Name | EMERSON HOSPITAL | CRF | |
| 5 | ABC | HO | ABC123105 | HOSEQ | 1 | HOINDC | Indication | ATRIAL FIBRILLATION | CRF | |
| 6 | ABC | HO | ABC123105 | HOSEQ | 2 | HONAM | Provider Name | ROOSEVELT HOSPITAL | CRF | |

#### Example 2

In this example, the dates of an initial hospitalization are collected as well as the date/time of ICU stay. Subsequent to discharge from the initial hospitalization, follow-up healthcare encounters, including admission to a rehabilitation facility, visits with healthcare providers, and home nursing visits were collected. Repeat hospitalizations are categorized separately.

**ho.xpt**

| Row | STUDYID | DOMAIN | USUBJID | HOSEQ | HOTERM | HOCAT | HOSTDTC | HOENDTC | HOENRTPT | HOENTPT |
|-----|---------|--------|---------|-------|--------|-------|---------|---------|----------|---------|
| 1 | ABC | HO | ABC123101 | 1 | HOSPITAL | INITIAL HOSPITALIZATION | 2011-06-08 | 2011-06-12 | | |
| 2 | ABC | HO | ABC123101 | 2 | ICU | INITIAL HOSPITALIZATION | 2011-06-08T11:00 | 2011-06-09T14:30 | | |
| 3 | ABC | HO | ABC123101 | 3 | REHABILITATION FACILITY | FOLLOW-UP CARE | 2011-06-12 | 2011-06-22 | | |
| 4 | ABC | HO | ABC123101 | 4 | CARDIOLOGY UNIT | FOLLOW-UP CARE | 2011-06-25 | 2011-06-25 | | |
| 5 | ABC | HO | ABC123101 | 5 | OUTPATIENT PHYSICAL THERAPY | FOLLOW-UP CARE | 2011-06-27 | 2011-06-27 | | |
| 6 | ABC | HO | ABC123101 | 6 | OUTPATIENT PHYSICAL THERAPY | FOLLOW-UP CARE | 2011-07-12 | 2011-07-12 | | |
| 7 | ABC | HO | ABC123101 | 7 | HOSPITAL | REPEAT HOSPITALIZATION | 2011-07-23 | 2011-07-24 | | |
| 8 | ABC | HO | ABC123102 | 1 | HOSPITAL | INITIAL HOSPITALIZATION | 2011-06-19 | 2011-07-02 | | |
| 9 | ABC | HO | ABC123102 | 2 | ICU | INITIAL HOSPITALIZATION | 2011-06-19T22:00 | 2011-06-23T09:30 | | |
| 10 | ABC | HO | ABC123102 | 3 | ICU | INITIAL HOSPITALIZATION | 2011-06-25T10:00 | 2011-06-29T19:30 | | |
| 11 | ABC | HO | ABC123102 | 4 | SKILLED NURSING FACILITY | FOLLOW-UP CARE | 2011-07-02 | | ONGOING | END OF STUDY |

The indication/medical condition for subject ABC123101's repeat hospitalization was represented as a supplemental qualifier.

**suppho.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | HO | ABC123101 | HOSEQ | 7 | HOINDC | Indication | STROKE | CRF | |

---

## 6.2.6 Medical History (MH)

### MH — Description/Overview

An events domain that contains data that includes the subject's prior medical history at the start of the trial.

### MH — Specification

**mh.xpt, Medical History — Events, One record per medical history event per subject, Tabulation.**

| # | Variable | Label | Type | Controlled Terms / Format | Role | Core | CDISC Notes |
|---|----------|-------|------|---------------------------|------|------|-------------|
| 1 | STUDYID | Study Identifier | Char | | Identifier | Req | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | MH | Identifier | Req | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | | Identifier | Req | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | MHSEQ | Sequence Number | Num | | Identifier | Req | Sequence number given to ensure uniqueness of subject records within a domain. |
| 5 | MHGRPID | Group ID | Char | | Identifier | Perm | Used to tie together a block of related records in a single domain for a subject. |
| 6 | MHREFID | Reference ID | Char | | Identifier | Perm | Internal or external medical history identifier. |
| 7 | MHSPID | Sponsor-Defined Identifier | Char | | Identifier | Perm | Sponsor-defined reference number. Example: Line number on a Medical History CRF page. |
| 8 | MHTERM | Reported Term for the Medical History | Char | | Topic | Req | Verbatim or preprinted CRF term for the medical condition or event. |
| 9 | MHMODIFY | Modified Reported Term | Char | | Synonym Qualifier | Perm | If MHTERM is modified to facilitate coding, then MHMODIFY will contain the modified text. |
| 10 | MHDECOD | Dictionary-Derived Term | Char | | Synonym Qualifier | Perm | Dictionary-derived text description of MHTERM or MHMODIFY. Equivalent to the Preferred Term (PT in MedDRA). |
| 11 | MHEVDTYP | Medical History Event Date Type | Char | C124301 | Variable Qualifier | Perm | Specifies the aspect of the medical condition or event by which MHSTDTC and/or MHENDTC is defined. Examples: "DIAGNOSIS", "SYMPTOMS", "RELAPSE", "INFECTION". |
| 12 | MHCAT | Category for Medical History | Char | | Grouping Qualifier | Perm | Used to define a category of related records. Examples: "CARDIAC", "GENERAL". |
| 13 | MHSCAT | Subcategory for Medical History | Char | | Grouping Qualifier | Perm | A further categorization of the condition or event. |
| 14 | MHPRESP | Medical History Event Pre-Specified | Char | C66742 | Variable Qualifier | Perm | A value of "Y" indicates this medical history event was prespecified on the CRF. Values are null for spontaneously reported events. |
| 15 | MHOCCUR | Medical History Occurrence | Char | C66742 | Record Qualifier | Perm | Used when the occurrence of specific medical history conditions is solicited, to indicate whether ("Y"/"N") a medical condition had ever occurred. Values are null for spontaneously reported events. |
| 16 | MHSTAT | Completion Status | Char | C66789 | Record Qualifier | Perm | Indicates that the prespecified question was not asked/answered. |
| 17 | MHREASND | Reason Medical History Not Collected | Char | | Record Qualifier | Perm | Describes the reason why data for a prespecified condition was not collected. Used with MHSTAT when value is "NOT DONE". |
| 18 | MHBODSYS | Body System or Organ Class | Char | | Record Qualifier | Perm | Dictionary-derived. Body system or organ class from a standard hierarchy (e.g., MedDRA). |
| 19 | TAETORD | Planned Order of Element within Arm | Num | | Timing | Perm | Number that gives the planned order of the element within the arm. |
| 20 | EPOCH | Epoch | Char | C99079 | Timing | Perm | Epoch associated with the start date/time of the medical history event. |
| 21 | MHDTC | Date/Time of History Collection | Char | ISO 8601 | Timing | Perm | Collection date and time of the medical history observation. |
| 22 | MHSTDTC | Start Date/Time of Medical History Event | Char | ISO 8601 | Timing | Perm | Start date/time of the medical history event. |
| 23 | MHENDTC | End Date/Time of Medical History Event | Char | ISO 8601 | Timing | Perm | End date/time of the medical history event. |
| 24 | MHDY | Study Day of History Collection | Num | | Timing | Perm | Study day of medical history collection, measured as integer day relative to RFSTDTC. |
| 25 | MHENRF | End Relative to Reference Period | Char | C66728 | Timing | Perm | Describes the end of the event relative to the sponsor-defined reference period. See Section 4.4.7. |
| 26 | MHENRTPT | End Relative to Reference Time Point | Char | C66728 | Timing | Perm | Identifies the end of the event as being before or after the reference time point defined by MHENTPT. See Section 4.4.7. |
| 27 | MHENTPT | End Reference Time Point | Char | | Timing | Perm | Description or date/time in ISO 8601 of the reference point referred to by MHENRTPT. Examples: "2003-12-25", "VISIT 2". |

### MH — Assumptions

1. Prior treatments, including prior medications and procedures, should be submitted in an appropriate dataset from the Interventions class (e.g., CM or PR).

2. **MH description and coding**
   - **(a)** MHTERM is the topic variable and captures the verbatim term collected for the condition or event or the prespecified term used to collect information about the occurrence of any of a group of conditions or events. MHTERM is a required variable and must have a value.
   - **(b)** MHMODIFY is a permissible variable and should be included if the sponsor's procedure permits modification of a verbatim term for coding. The modified term is listed in MHMODIFY. The variable should be populated as per the sponsor's procedures; null values are permitted.
   - **(c)** If the sponsor codes the reported term (MHTERM) using a standard dictionary, then MHDECOD will be populated with the preferred term derived from the dictionary. The sponsor is expected to provide the dictionary name and version used in the Define-XML document.
   - **(d)** MHBODSYS is the system organ class (SOC) from the coding dictionary associated with the condition by the sponsor. This value may differ from the primary SOC designated in the coding dictionary's standard hierarchy.
   - **(e)** If a CRF collects medical history by prespecified body systems and the sponsor also codes reported terms using a standard dictionary, then MHDECOD and MHBODSYS are populated using the standard dictionary. MHCAT and MHSCAT should be used for the prespecified body systems.

3. **Additional categorization and grouping**
   - **(a)** MHCAT and MHSCAT may be populated with the sponsor's predefined categorization of medical history events.
     - **(i)** This categorization should not group all records into one generic group such as "Medical History" or "General Medical History" because this is redundant with the domain code.
     - **(ii)** Examples of MHCAT: "General Medical History", "Allergy Medical History", "Reproductive Medical History".
   - **(b)** MHGRPID may be used to link different records together. It should not be used in place of MHCAT or MHSCAT.

4. **Prespecified terms; presence or absence of events**
   - **(a)** Information on medical history is generally collected in 2 different ways, either by recording free text or using a prespecified list of terms. MHPRESP and MHOCCUR are used together to indicate whether the condition in MHTERM was prespecified and whether it occurred.
   - **(b)** MHOCCUR is used to indicate whether a prespecified medical condition occurred; "Y" indicates that the event occurred and "N" indicates that it did not.
   - **(c)** If a medical history event was reported using free text, the values of MHPRESP and MHOCCUR should be null.
   - **(d)** MHSTAT and MHREASND provide information about prespecified medical history questions for which no response was collected.

| Situation | MHPRESP | MHOCCUR | MHSTAT |
|-----------|---------|---------|--------|
| Spontaneously reported event occurred | | | |
| Pre-specified event occurred | Y | Y | |
| Pre-specified event did not occur | Y | N | |
| Pre-specified event has no response | Y | | NOT DONE |

   - **(e)** When medical history events are collected with the recording of free text, a record may be entered into the data management system to indicate "no medical history" for a specific subject. For these subjects, do not include a record in the MH dataset to indicate that there were no events.

5. **Timing variables**
   - **(a)** Relative timing assessments such as "Ongoing" or "Active" are common in the collection of MH information. MHENRF may be used when this relative timing assessment is coincident with the start of the study reference period for the subject represented in the Demographics (DM) dataset (RFSTDTC). MHENRTPT and MHENTPT may be used when "Ongoing" is relative to another date such as the screening visit date. See Section 4.4.7.
   - **(b)** Additional timing variables (e.g., MHSTRF) may be used when appropriate.

6. **MH event date type**
   - **(a)** MHEVDTYP is a domain-specific variable that can be used to indicate the aspect of the event that is represented in the event start and/or end date/times (MHSTDTC and/or MHENDTC). If a start date and/or end date is collected without further specification, MHEVDTYP is not needed. However, when data collection specifies how the start or end date is to be reported, MHEVDTYP can be used to provide this information. For example, when collecting the date of diagnosis, it would populate MHSTDTC; MHEVDTYP would be "DIAGNOSIS".
   - **(b)** When data collected about an event includes 2 different dates that could be considered the start or end of an event, then an MH record will be created for each. For example, if data collection included both a date of onset of symptoms and a date of diagnosis, there would be 2 records for the event, one with MHEVDTYP = "SYMPTOMS" and a second with MHEVDTYP = "DIAGNOSIS". The 2 records should be linked by a common value of MHSPID or MHGRPID.

7. Any identifiers, timing variables, or Events general observation-class qualifiers may be added to the MH domain, but the following Qualifiers would generally not be used: --SER, --ACN, --ACNOTH, --REL, --RELNST, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE.

### MH — Examples

#### Example 1

In this example, a General Medical History CRF collected verbatim descriptions of conditions and events by body system (e.g., endocrine, metabolic), did not collect start date, but asked whether or not the condition was ongoing at the time of the visit. Another CRF page was used for cardiac history events. This page asked for date of onset of symptoms and date of diagnosis, but did not include the ongoing question.

- **Rows 1-3:** MHCAT indicates that these data were collected on the General Medical History CRF, and MHSCAT indicates the body system for which the event was collected. The reported events were coded using a standard dictionary. MHDECOD and MHBODSYS display the preferred term and body system assigned through the coding process. MHENRTPT was populated based on the response to the "Ongoing" question on the General Medical History CRF. MHENTPT displays the reference date for MHENRTPT, that is, the date the information was collected. If "Yes" was specified for Ongoing, MHENRTPT = "ONGOING"; if "No" was checked, MHENRTPT = "BEFORE". See Section 4.4.7.
- **Rows 4-5:** MHCAT indicates that these data were collected on the Cardiac Medical History CRF. Because 2 kinds of start date were collected for congestive heart failure, there are 2 records for this event, with MHEVDTYP = "SYMPTOM ONSET" and MHEVDTYP = "DIAGNOSIS". The sponsor grouped these 2 records using MHGRPID = "CHF".

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHGRPID | MHTERM | MHDECOD | MHEVDTYP | MHCAT | MHSCAT | MHBODSYS | MHSTDTC | MHENRTPT | MHENTPT |
|-----|---------|--------|---------|-------|---------|--------|---------|----------|-------|--------|----------|---------|----------|---------|
| 1 | ABC123 | MH | 123101 | 1 | | ASTHMA | Asthma | | GENERAL MEDICAL HISTORY | RESPIRATORY | Respiratory system disorders | | ONGOING | 2004-09-18 |
| 2 | ABC123 | MH | 123101 | 2 | | FREQUENT HEADACHES | Headache | | GENERAL MEDICAL HISTORY | CNS | Central and peripheral nervous system disorders | | ONGOING | 2004-09-18 |
| 3 | ABC123 | MH | 123101 | 3 | | BROKEN LEG | Bone fracture | | GENERAL MEDICAL HISTORY | OTHER | Musculoskeletal system disorders | | BEFORE | 2004-09-18 |
| 4 | ABC123 | MH | 123101 | 4 | CHF | CONGESTIVE HEART FAILURE | Cardiac failure congestive | SYMPTOM ONSET | CARDIAC MEDICAL HISTORY | | Cardiac disorders | 2004-09-17 | | |
| 5 | ABC123 | MH | 123101 | 5 | CHF | CONGESTIVE HEART FAILURE | Cardiac failure congestive | DIAGNOSIS | CARDIAC MEDICAL HISTORY | | Cardiac disorders | 2004-09-19 | | |

#### Example 2

In this example, data from 3 CRF modules related to medical history were collected:

- A General Medical History CRF collected descriptions of conditions and events by body system (e.g., endocrine, metabolic) and asked whether the conditions were ongoing at study start. The reported events were coded using a standard dictionary.
- A second CRF collected stroke history. Terms were selected from a list of terms taken from the standard dictionary.
- A third CRF asked whether the subject had any of a list of 4 specific risk factors.

In all of the records shown below, MHCAT is populated with the CRF module (general medical history, stroke history, or risk factors) through which the data were collected. MHPRESP and MHOCCUR were populated only when the term was prespecified, in keeping with MH assumption 4.

- **Rows 1-3:** Show records from the General Medical History CRF. MHSCAT displays the body systems specified on the CRF. The coded terms are represented in MHDECOD. MHENRF has been populated based on the response to the "Ongoing at Study Start" question. If "Yes" was specified, MHENRF = "DURING/AFTER"; if "No" was checked, MHENRF = "BEFORE". See Section 4.4.7.
- **Row 4:** Shows the record from the Stroke History CRF. MHSTDTC was populated with the date and time at which the event occurred.
- **Rows 5-8:** Show records from the Risk Factors CRF. MHPRESP values of "Y" indicate that each risk factor was prespecified on the CRF. MHOCCUR is populated with "Y" or "N", corresponding to the CRF response for the 4 prespecified risk factors.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHCAT | MHSCAT | MHPRESP | MHOCCUR | MHBODSYS | MHSTDTC | MHENRF |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|---------|---------|----------|---------|--------|
| 1 | ABC123 | MH | 123101 | 1 | ASTHMA | Asthma | GENERAL MEDICAL HISTORY | RESPIRATORY | | | Respiratory system disorders | | DURING/AFTER |
| 2 | ABC123 | MH | 123101 | 2 | FREQUENT HEADACHES | Headache | GENERAL MEDICAL HISTORY | CNS | | | Central and peripheral nervous system disorders | | DURING/AFTER |
| 3 | ABC123 | MH | 123101 | 3 | BROKEN LEG | Bone fracture | GENERAL MEDICAL HISTORY | OTHER | | | Musculoskeletal system disorders | | BEFORE |
| 4 | ABC123 | MH | 123101 | 4 | ISCHEMIC STROKE | Ischaemic Stroke | STROKE HISTORY | | | | | 2004-09-17T07:30 | |
| 5 | ABC123 | MH | 123101 | 5 | DIABETES | Diabetes mellitus | RISK FACTORS | | Y | Y | | | |
| 6 | ABC123 | MH | 123101 | 6 | HYPERCHOLESTEROLEMIA | Hypercholesterolemia | RISK FACTORS | | Y | Y | | | |
| 7 | ABC123 | MH | 123101 | 7 | HYPERTENSION | Hypertension | RISK FACTORS | | Y | Y | | | |
| 8 | ABC123 | MH | 123101 | 8 | TIA | Transient ischaemic attack | RISK FACTORS | | Y | N | | | |

#### Example 3

This is an example of a medical history CRF where the history of specific (prespecified) conditions is solicited. The conditions were not coded using a standard dictionary. The data were collected as part of the screening visit.

- **Rows 1-9:** MHPRESP = "Y" indicates that these conditions were specifically queried. Presence or absence of the condition is represented in MHOCCUR.
- **Row 10:** There was also a specific question about asthma, as indicated by MHPRESP = "Y", but this question was not asked. Because the question was not asked, MHOCCUR is null and MHSTAT = "NOT DONE". In this case, a reason for the absence of a response was collected, and this is represented in MHREASND.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHPRESP | MHOCCUR | MHSTAT | MHREASND | VISITNUM | VISIT | MHDTC | MHDY |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|--------|----------|----------|-------|-------|------|
| 1 | ABC123 | MH | 101002 | 1 | HISTORY OF EARLY CORONARY ARTERY DISEASE (<55 YEARS OF AGE) | Coronary Artery Disease | Y | N | | | 1 | SCREEN | 2006-04-22 | -5 |
| 2 | ABC123 | MH | 101002 | 2 | CONGESTIVE HEART FAILURE | Congestive Heart Failure | Y | N | | | 1 | SCREEN | 2006-04-22 | -5 |
| 3 | ABC123 | MH | 101002 | 3 | PERIPHERAL VASCULAR DISEASE | Peripheral Vascular Disease | Y | N | | | 1 | SCREEN | 2006-04-22 | -5 |
| 4 | ABC123 | MH | 101002 | 4 | TRANSIENT ISCHEMIC ATTACK | Transient Ischemic Attack | Y | Y | | | 1 | SCREEN | 2006-04-22 | -5 |
| 5 | ABC123 | MH | 101002 | 5 | ASTHMA | Asthma | Y | Y | | | 1 | SCREEN | 2006-04-22 | -5 |
| 6 | ABC123 | MH | 101003 | 1 | HISTORY OF EARLY CORONARY ARTERY DISEASE (<55 YEARS OF AGE) | Coronary Artery Disease | Y | Y | | | 1 | SCREEN | 2006-05-03 | -3 |
| 7 | ABC123 | MH | 101003 | 2 | CONGESTIVE HEART FAILURE | Congestive Heart Failure | Y | N | | | 1 | SCREEN | 2006-05-03 | -3 |
| 8 | ABC123 | MH | 101003 | 3 | PERIPHERAL VASCULAR DISEASE | Peripheral Vascular Disease | Y | Y | | | 1 | SCREEN | 2006-05-03 | -3 |
| 9 | ABC123 | MH | 101003 | 4 | TRANSIENT ISCHEMIC ATTACK | Transient Ischemic Attack | Y | N | | | 1 | SCREEN | 2006-05-03 | -3 |
| 10 | ABC123 | MH | 101003 | 5 | ASTHMA | Asthma | Y | | NOT DONE | FORGOT TO ASK | 1 | SCREEN | 2006-05-03 | -3 |

#### Example 4

This diabetes study included subjects with both type 1 diabetes and type 2 diabetes. Data collection included which kind of diabetes the subject had and the date of diagnosis of the condition.

- **Rows 1-2:** Show that subject XYZ-001-001 had type 1 diabetes, and did not have type 2 diabetes. The start date in Row 1 is the date of diagnosis, as indicated by MHEVDTYP = "DIAGNOSIS". Because this subject did not have type 2 diabetes, no start date for type 2 diabetes was collected, so MHEVDTYP in Row 2 is blank.
- **Rows 3-4:** Show that subject XYZ-001-002 had type 2 diabetes, and did not have type 1 diabetes. The start date in Row 4 is the date of diagnosis, as indicated by MHEVDTYP = "DIAGNOSIS".

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHEVDTYP | MHCAT | MHPRESP | MHOCCUR | MHDTC | MHSTDTC |
|-----|---------|--------|---------|-------|--------|---------|----------|-------|---------|---------|-------|---------|
| 1 | XYZ | MH | XYZ-001-001 | 1 | TYPE 1 DIABETES MELLITUS | Type 1 diabetes mellitus | DIAGNOSIS | DIABETES | Y | Y | 2010-09-26 | 2010-03-25 |
| 2 | XYZ | MH | XYZ-001-001 | 2 | TYPE 2 DIABETES MELLITUS | Type 2 diabetes mellitus | | DIABETES | Y | N | 2010-09-26 | |
| 3 | XYZ | MH | XYZ-001-002 | 1 | TYPE 1 DIABETES MELLITUS | Type 1 diabetes mellitus | | DIABETES | Y | N | 2010-10-26 | |
| 4 | XYZ | MH | XYZ-001-002 | 2 | TYPE 2 DIABETES MELLITUS | Type 2 diabetes mellitus | DIAGNOSIS | DIABETES | Y | Y | 2010-10-26 | 2010-04-25 |

#### Example 5 — Respiratory Infections

This example shows data from a study in which data were collected about whether subjects had had any respiratory infections in the prior 6 months and, if they had, collected data on those respiratory infections. The example shows data for 2 subjects.

- **Row 1:** Shows that subject 203 had no respiratory infections during the evaluation interval (the prior 6 months). The same value ("Respiratory Infections") in both MHTERM and MHCAT indicates that the occurrence question was about a group of medical conditions rather than a specific single medical condition.
- **Row 2:** Shows that subject 204 did have at least 1 respiratory infection during the evaluation interval.
- **Row 3:** Shows that subject 204 had a common cold during the evaluation interval. They did not provide an end date, but indicated that the infection had ended.
- **Row 4:** Shows that subject 204 had bronchitis during the evaluation interval, and that an end date for the infection was provided.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHCAT | MHPRESP | MHOCCUR | MHDTC | MHENDTC | MHDY | MHEVLINT | MHENRTPT | MHENTPT |
|-----|---------|--------|---------|-------|--------|-------|---------|---------|-------|---------|------|----------|----------|---------|
| 1 | XYZ234 | MH | 203 | 1 | RESPIRATORY INFECTIONS | RESPIRATORY INFECTIONS | Y | N | 2019-11-02 | | -2 | -P6M | | |
| 2 | XYZ234 | MH | 204 | 1 | RESPIRATORY INFECTIONS | RESPIRATORY INFECTIONS | Y | Y | 2019-12-08 | | -1 | -P6M | | |
| 3 | XYZ234 | MH | 204 | 2 | COMMON COLD | RESPIRATORY INFECTIONS | | | 2019-12-08 | | -1 | -P6M | BEFORE | 2019-12-08 |
| 4 | XYZ234 | MH | 204 | 3 | BRONCHITIS | RESPIRATORY INFECTIONS | | | 2019-12-08 | 2019-10-20 | -1 | -P6M | | |

---

## 6.2.7 Protocol Deviations (DV)

### DV — Description/Overview

An events domain that contains protocol violations and deviations during the course of the study.

### DV — Specification

**dv.xpt, Protocol Deviations — Events, One record per protocol deviation per subject, Tabulation.**

| # | Variable | Label | Type | Controlled Terms / Format | Role | Core | CDISC Notes |
|---|----------|-------|------|---------------------------|------|------|-------------|
| 1 | STUDYID | Study Identifier | Char | | Identifier | Req | Unique identifier for a study. |
| 2 | DOMAIN | Domain Abbreviation | Char | DV | Identifier | Req | Two-character abbreviation for the domain. |
| 3 | USUBJID | Unique Subject Identifier | Char | | Identifier | Req | Identifier used to uniquely identify a subject across all studies for all applications or submissions involving the product. |
| 4 | DVSEQ | Sequence Number | Num | | Identifier | Req | Sequence number given to ensure uniqueness of subject records within a domain. |
| 5 | DVREFID | Reference ID | Char | | Identifier | Perm | Internal or external identifier. |
| 6 | DVSPID | Sponsor-Defined Identifier | Char | | Identifier | Perm | Sponsor-defined reference number. Example: Line number on a CRF page. |
| 7 | DVTERM | Protocol Deviation Term | Char | | Topic | Req | Verbatim name of the protocol deviation criterion. Example: "IVRS PROCESS DEVIATION - NO DOSE CALL PERFORMED". |
| 8 | DVDECOD | Protocol Deviation Coded Term | Char | | Synonym Qualifier | Perm | Controlled terminology for the name of the protocol deviation. Examples: "SUBJECT NOT WITHDRAWN AS PER PROTOCOL", "SELECTION CRITERIA NOT MET", "EXCLUDED CONCOMITANT MEDICATION", "TREATMENT DEVIATION". |
| 9 | DVCAT | Category for Protocol Deviation | Char | | Grouping Qualifier | Perm | Category of the protocol deviation criterion. |
| 10 | DVSCAT | Subcategory for Protocol Deviation | Char | | Grouping Qualifier | Perm | A further categorization of the protocol deviation. |
| 11 | TAETORD | Planned Order of Element within Arm | Num | | Timing | Perm | Number that gives the planned order of the element within the arm. |
| 12 | EPOCH | Epoch | Char | C99079 | Timing | Perm | Epoch associated with the start date/time of the deviation. Examples: "TREATMENT", "SCREENING", "FOLLOW-UP". |
| 13 | DVSTDTC | Start Date/Time of Deviation | Char | ISO 8601 | Timing | Perm | Start date/time of deviation. |
| 14 | DVENDTC | End Date/Time of Deviation | Char | ISO 8601 | Timing | Perm | End date/time of deviation. |
| 15 | DVSTDY | Study Day of Start of Deviation Event | Num | | Timing | Perm | Study day of start of event relative to the sponsor-defined RFSTDTC. |
| 16 | DVENDY | Study Day of End of Deviation Event | Num | | Timing | Perm | Study day of end of event relative to the sponsor-defined RFSTDTC. |

### DV — Assumptions

1. The DV domain is an Events model for collected protocol deviations and not for derived protocol deviations that are more likely to be part of analysis. Events typically include what the event was, captured in --TERM (the topic variable), and when it happened (captured in its start and/or end dates). The intent is to capture protocol deviations that occurred during the course of the study (see ICH E3, Section 10.2). Usually these are deviations that occur after the subject has been randomized or received the first treatment.

2. This domain should not be used to collect entry-criteria information. Violated inclusion/exclusion criteria are stored in IE. The Deviations domain is for more general deviation data. A protocol may indicate that violating an inclusion/exclusion criterion during the course of the study (after first dose) is a protocol violation. In this case, this information would go into DV.

3. Any identifier variables, timing variables, or Events general observation-class qualifiers may be added to the DV domain, but the following qualifiers would generally not be used: --PRESP, --OCCUR, --STAT, --REASND, --BODSYS, --LOC, --SEV, --SER, --ACN, --ACNOTH, --REL, --RELNST, --PATT, --OUT, --SCAN, --SCONG, --SDISAB, --SDTH, --SHOSP, --SLIFE, --SOD, --SMIE, --CONTRT, --TOXGR.

### DV — Examples

#### Example 1

This is an example of data that was collected on a protocol-deviations CRF. The DVDECOD column is for controlled terminology, whereas the DVTERM is free text.

- **Rows 1, 3:** Show examples of a TREATMENT DEVIATION type of protocol deviation.
- **Row 2:** Shows an example of a deviation due to the subject taking a prohibited concomitant medication.
- **Row 4:** Shows an example of a medication that should not be taken during the study.

**dv.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DVSEQ | DVTERM | DVDECOD | DVCAT | DVSCAT | EPOCH | DVSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | ABC123 | DV | 123101 | 1 | SUBJECT MISSED 2 DOSES | TREATMENT DEVIATION | TREATMENT | DOSING | TREATMENT | 2003-10-05 |
| 2 | ABC123 | DV | 123102 | 1 | SUBJECT TOOK ASPIRIN | EXCLUDED CONCOMITANT MEDICATION | MEDICATION | CONCOMITANT | TREATMENT | 2003-10-12 |
| 3 | ABC123 | DV | 123103 | 1 | DOSE NOT ADMINISTERED PER SCHEDULE | TREATMENT DEVIATION | TREATMENT | DOSING | TREATMENT | 2003-10-15 |
| 4 | ABC123 | DV | 123104 | 1 | SUBJECT TOOK PROHIBITED MEDICATION | EXCLUDED CONCOMITANT MEDICATION | MEDICATION | PROHIBITED | TREATMENT | 2003-10-20 |
