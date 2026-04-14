# DS — Examples

## Example 1

In this example, disposition of study participation was collected for each epoch of a trial. Disposition of study participation is indicated by DSCAT = "DISPOSITION EVENT". EPOCH was taken from the CRF, which asked about completion of each epoch of the study. Data about disposition of study treatment was not collected, but the sponsor populated DSSCAT with "STUDY PARTICIPATION" to emphasize that these represent disposition of study participation.

Data were also collected about several protocol milestones represented with DSCAT = "PROTOCOL MILESTONE".

**Rows 1, 2, 6, 8, 9, 12, 13, 17, 18:** Show records for protocol milestones. DSTERM and DSDECOD are populated with the same value, the name of the milestone. Note that for randomization events, EPOCH = "SCREENING", because randomization occurred before the start of treatment, during the screening epoch.

**Rows 3-5:** Show 3 records for a subject who completed 3 stages of the study ("SCREENING", "TREATMENT", "FOLLOW-UP").

**Row 7:** Shows disposition of a subject who was a screen failure. The verbatim reason the subject was a screen failure is represented in DSTERM. Because the subject did not complete the screening epoch, DSDECOD is not "COMPLETED" but another appropriate controlled term, "PROTOCOL VIOLATION". The date of discontinuation is in DSSTDTC. The protocol deviation event itself would be represented in the DV dataset.

**Rows 10-11:** Show disposition of a subject who completed the screening stage but did not complete the treatment stage. For completed epochs, both DSTERM and DSDECOD are "COMPLETED". For epochs that were not completed, the verbatim reason for the treatment epoch is in DSTERM, while the value from controlled terminology is in DSDECOD.

**Rows 14-16:** Show disposition of a subject who completed treatment, but did not complete follow-up. Note that for final disposition event, the date of collection of the event information, DSDTC, was different from the date of the disposition event (the subject's death), DSSTDTC.

**Rows 19-21:** Show disposition of a subject who discontinued the treatment epoch due to an adverse event, but who went on to complete the follow-up phase of the trial.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSDTC | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|-------|---------|
| 1 | ABC123 | DS | 123101 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-09-21 | 2003-09-21 |
| 2 | ABC123 | DS | 123101 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2003-09-30 | 2003-09-30 |
| 3 | ABC123 | DS | 123101 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-09-30 | 2003-09-29 |
| 4 | ABC123 | DS | 123101 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2003-10-31 | 2003-10-15 |
| 5 | ABC123 | DS | 123101 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2003-11-15 | 2003-11-21 |
| 6 | ABC123 | DS | 123102 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-11-21 | 2003-11-21 |
| 7 | ABC123 | DS | 123102 | 2 | SUBJECT DENIED MRI PROCEDURE | PROTOCOL VIOLATION | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-11-22 | 2003-11-22 |
| 8 | ABC123 | DS | 123103 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-09-15 | 2003-09-15 |
| 9 | ABC123 | DS | 123103 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2003-09-30 | 2003-09-30 |
| 10 | ABC123 | DS | 123103 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-09-30 | 2003-09-30 |
| 11 | ABC123 | DS | 123103 | 4 | SUBJECT MOVED | LOST TO FOLLOW-UP | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2003-10-31 | 2003-10-20 |
| 12 | ABC123 | DS | 123104 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-09-15 | 2003-09-15 |
| 13 | ABC123 | DS | 123104 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2003-09-30 | 2003-09-30 |
| 14 | ABC123 | DS | 123104 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-09-30 | 2003-09-30 |
| 15 | ABC123 | DS | 123104 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2003-10-15 | 2003-10-15 |
| 16 | ABC123 | DS | 123104 | 5 | AUTOMOBILE ACCIDENT | DEATH | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2003-10-31 | 2003-10-31 |
| 17 | ABC123 | DS | 123105 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | | SCREENING | 2003-09-28 | 2003-09-28 |
| 18 | ABC123 | DS | 123105 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2003-10-02 | 2003-10-02 |
| 19 | ABC123 | DS | 123105 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2003-10-02 | 2003-10-02 |
| 20 | ABC123 | DS | 123105 | 4 | ANEMIA | ADVERSE EVENT | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT | 2003-10-17 | 2003-10-17 |
| 21 | ABC123 | DS | 123105 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2003-11-02 | 2003-11-02 |

## Example 2

In this example, the sponsor has chosen to simply submit whether or not subjects completed the study, so there is only 1 record per subject. The sponsor did not collect disposition of treatment and did not include DSSCAT. EPOCH was populated as a timing variable, and represents the epoch during which the subject discontinued.

**Row 1:** Subject 456101 completed the study. EPOCH = "FOLLOW-UP", which was the last epoch in the design of this study.

**Rows 2-3:** Subjects 456102 and 456103 discontinued. Both discontinued participation during the treatment epoch.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|---------|
| 1 | ABC456 | DS | 456101 | 1 | COMPLETED | COMPLETED | DISPOSITION EVENT | FOLLOW-UP | 2003-09-21 |
| 2 | ABC456 | DS | 456102 | 1 | SUBJECT TAKING STUDY MED ERRATICALLY | PROTOCOL VIOLATION | DISPOSITION EVENT | TREATMENT | 2003-09-29 |
| 3 | ABC456 | DS | 456103 | 1 | LOST TO FOLLOW-UP | LOST TO FOLLOW-UP | DISPOSITION EVENT | TREATMENT | 2003-10-15 |

## Example 3

In this study, disposition of study participation was collected for the treatment and follow-up epochs. For these records, the value in EPOCH was taken from the CRF. Data on screen failures were not submitted for this study, so all submitted subjects completed screening; the sponsor chose not to collect data on disposition of the screening epoch.

Data on protocol milestones were not collected, but data were collected if a subject's treatment was unblinded. For these records, EPOCH represents the epoch during which the blind was broken.

**Rows 1, 2:** Subject 789101 completed the treatment and follow-up phases.

**Rows 3, 5:** Subject 789102 did not complete the treatment phase but did complete the follow-up phase.

**Row 4:** Subject 789102's treatment was unblinded. The date of the unblinding is represented in DSSTDTC. Maintaining the blind as per protocol was not considered to be an "event" because there was no change in the subject's state.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|---------|
| 1 | ABC789 | DS | 789101 | 1 | COMPLETED | COMPLETED | DISPOSITION EVENT | TREATMENT | 2004-09-12 |
| 2 | ABC789 | DS | 789101 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | FOLLOW-UP | 2004-12-20 |
| 3 | ABC789 | DS | 789102 | 1 | SKIN RASH | ADVERSE EVENT | DISPOSITION EVENT | TREATMENT | 2004-09-30 |
| 4 | ABC789 | DS | 789102 | 2 | SUBJECT HAD SEVERE RASH | TREATMENT UNBLINDED | OTHER EVENT | TREATMENT | 2004-10-01 |
| 5 | ABC789 | DS | 789102 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | FOLLOW-UP | 2004-12-28 |

## Example 4

In this example, the CRF included collection of an AE number when study participation was incomplete due to an adverse event. The relationship between the DS record and AE record is represented in a RELREC dataset.

The DS domain represents the end of the subject's participation in the study, due to their death from heart failure. In this case, the disposition was collected (DSDTC) on the same day that death occurred and the subject's study participation ended. (DSDTDTC).

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | EPOCH | DSDTC | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|-------|---------|
| 1 | ABC123 | DS | 123102 | 1 | Heart Failure | DEATH | DISPOSITION EVENT | TREATMENT | 2003-09-29 | 2003-09-29 |

The heart failure is represented as an adverse event. In order to save space, only 2 of the MedDRA coding variables for the adverse event have been included.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AESTDTC | AEENDTC | AEDECOD | AESOC | AESEV | AESER | AEACN | AEREL | AEOUT | AESCONG | AESDISAB | AESDTH | AESHOSP | AESLIFE | AESOD | AESMIE |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|-------|-------|-------|-------|-------|-------|---------|----------|--------|---------|---------|-------|--------|
| 1 | ABC123 | AE | 123102 | 1 | Heart Failure | 2003-09-28 | 2003-09-29 | HEART FAILURE | CARDIOVASCULAR SYSTEM | SEVERE | Y | NOT APPLICABLE | DEFINITELY NOT RELATED | FATAL | N | N | Y | N | N | N |

The relationship between the DS and AE records is represented in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC123 | DS | 123102 | DSSEQ | 1 | | 1 |
| 2 | ABC123 | AE | 123102 | AESEQ | 1 | | 1 |

The subject's DM record is not shown, but included DTHFL = "Y" and the date of death.

## Example 5

This below represents a multidrug (isoniazid and levofloxacin) investigational treatment trial for multidrug-resistant tuberculosis (MDR-TB). The protocol allows for a subject to discontinue levofloxacin and continue single treatment of isoniazid throughout the remainder of the study. Disposition of study participation and disposition of each drug was collected. Whether a record with DSCAT = "DISPOSITION EVENT" represents disposition of the subject's participation in the study or disposition of a study treatment is represented in DSSCAT. In this example, disposition of the study and of each drug a subject received for each of the study's 2 treatment epochs.

**Row 1:** Indicates that the physician, per protocol, removed levofloxacin treatment due to high-level positive cultures. This record represents the treatment discontinuation for levofloxacin, for the first treatment epoch. Note that because this subject did not receive levofloxacin during the second treatment epoch, there is no record for DSSCAT = "LEVOFLOXACIN" with EPOCH = "TREATMENT 2".

**Rows 2, 4:** Represent the treatment continuation and completion for isoniazid each treatment epoch.

**Rows 3, 5:** Represent the study disposition for each treatment epoch, as indicated by DSSCAT = "STUDY PARTICIPATION".

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | PERSISTENT HIGH-LEVEL POSITIVE CULTURES. PER PROTOCOL, LEVOFLOXACIN REMOVAL RECOMMENDED | PHYSICIAN DECISION | DISPOSITION EVENT | LEVOFLOXACIN | TREATMENT 1 | 2016-02-15 |
| 2 | XXX | DS | XXX-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | ISONIAZID | TREATMENT 1 | 2016-02-15 |
| 3 | XXX | DS | XXX-767-001 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-02-25 |
| 4 | XXX | DS | XXX-767-001 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | ISONIAZID | TREATMENT 2 | 2016-03-14 |
| 5 | XXX | DS | XXX-767-001 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-03-24 |

## Example 6

This example is for a study of a multidrug (isoniazid and levofloxacin) investigational treatment for MDR-TB. The protocol allowed a subject to discontinue levofloxacin and continue single treatment of isoniazid throughout the remainder of the study. Disposition of study participation and of each study treatment was collected. For records of disposition of the subject's participation in the study DSSCAT = "STUDY PARTICIPATION", whereas for records of disposition of a study treatment DSSCAT is the name of the treatment.

**Row 1:** Represents the final treatment disposition for levofloxacin, as indicated by DSSCAT = "LEVOFLOXACIN". The physician removed levofloxacin treatment due to high-level positive cultures, as allowed by the protocol.

**Row 2:** Represents the final treatment completion of isoniazid within the trial, which is indicated by DSSCAT = "ISONIAZID".

**Row 3:** Represents the final study completion within the trial, which is indicated by DSSCAT = "STUDY PARTICIPATION".

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | PERSISTENT HIGH-LEVEL POSITIVE CULTURES. PER PROTOCOL, LEVOFLOXACIN REMOVAL RECOMMENDED | PHYSICIAN DECISION | DISPOSITION EVENT | LEVOFLOXACIN | TREATMENT 1 | 2016-02-15 |
| 2 | XXX | DS | XXX-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | ISONIAZID | TREATMENT 2 | 2016-03-14 |
| 3 | XXX | DS | XXX-767-001 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-03-24 |

## Example 7

This is an example of a trial with a single investigative treatment. The sponsor used the generic DSSCAT value "STUDY TREATMENT" rather than the name of the treatment. This subject discontinued both treatment and study participation due to an adverse event.

**Rows 1, 3:** Represent the disposition of treatment for each treatment epoch, as indicated by DSSCAT = "STUDY TREATMENT".

**Rows 2, 4:** Represent the disposition of study participation continuation for each treatment epoch, as indicated by DSSCAT = "STUDY PARTICIPATION".

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY TREATMENT | TREATMENT 1 | 2016-02-15 |
| 2 | XXX | DS | XXX-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-02-15 |
| 3 | XXX | DS | XXX-767-001 | 3 | SKIN RASH | ADVERSE EVENT | DISPOSITION EVENT | STUDY TREATMENT | TREATMENT 2 | 2016-03-14 |
| 4 | XXX | DS | XXX-767-001 | 4 | SKIN RASH | ADVERSE EVENT | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-03-14 |

## Example 8

This example represents data for an ongoing blinded study in which each subject received 2 treatments, identified by the sponsor as "BLINDED DRUG A" and "BLINDED DRUG B". Disposition of study participation and of each of the 2 blinded treatments was collected for each of the 2 treatment epochs in the study. The subject in this example completed study participation and both treatments for both treatment epochs.

**Rows 1, 2, 4, 5:** Represent the disposition of the blinded treatments for each of the 2 treatment epochs, indicated by DSSCAT = "BLINDED DRUG A" and DSSCAT = "BLINDED DRUG B".

**Rows 3, 6:** Represent the disposition of study participation for each of the 2 treatment epochs, as indicated by DSSCAT = "STUDY PARTICIPATION".

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | COMPLETED | COMPLETED | DISPOSITION EVENT | BLINDED DRUG A | TREATMENT 1 | 2016-02-15 |
| 2 | XXX | DS | XXX-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | BLINDED DRUG B | TREATMENT 1 | 2016-02-15 |
| 3 | XXX | DS | XXX-767-001 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-02-25 |
| 4 | XXX | DS | XXX-767-001 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | BLINDED DRUG A | TREATMENT 2 | 2016-03-14 |
| 5 | XXX | DS | XXX-767-001 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | BLINDED DRUG B | TREATMENT 2 | 2016-03-14 |
| 6 | XXX | DS | XXX-767-001 | 6 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-03-24 |

## Example 9

This example is for a study in which multiple informed consents were collected. DSTERM is populated with a full description of the informed consent. DSDECOD is populated with the standardized value "INFORMED CONSENT OBTAINED" from the Protocol Milestone (PROTMLST) codelist. For all informed consent records, DSCAT = "PROTOCOL MILESTONE". The sponsor chose to include the EPOCH timing variable, to indicate the epoch during which each protocol milestone occurred.

**Row 1:** Shows the obtaining of the initial study informed consent.

**Row 2:** Shows randomization, another event with DSCAT = "PROTOCOL MILESTONE".

**Rows 3-5:** Show 3 additional informed consents obtained during the trial.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|---------|
| 1 | XXX | DS | XXX-767-001 | 1 | INFORMED CONSENT FOR STUDY ENROLLMENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | SCREENING | 2016-02-22 |
| 2 | XXX | DS | XXX-767-001 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | SCREENING | 2016-02-26 |
| 3 | XXX | DS | XXX-767-001 | 3 | INFORMED CONSENT FOR AMENDMENT ONE OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | TREATMENT 1 | 2016-04-10 |
| 4 | XXX | DS | XXX-767-001 | 4 | INFORMED CONSENT FOR PHARMACOGENETIC RESEARCH OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | TREATMENT 2 | 2016-06-08 |
| 5 | XXX | DS | XXX-767-001 | 5 | INFORMED CONSENT FOR PK SUB-STUDY OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | TREATMENT 2 | 2016-06-23 |

## Example 10

The example represents data for 2 subjects who participated in a study with multiple treatment periods. During the first treatment period, subjects were randomized to drug 1 or drug 2. The second treatment phase added the investigational drug to drug 1 and drug 2. Disposition of study drugs and study participation was collected at the end of each epoch. DSSCAT was used to distinguish between disposition of study drugs vs. study participation. The supporting Demographics (DM), Exposure (EX), Trial Elements (TE), Trial Arms (TA), and Subject Elements (SE) datasets have been provided for additional context. Not all records are shown in the supporting example datasets.

The elements used in the TA dataset are defined in the TE dataset.

**Row 1:** Shows the screening element.

**Rows 2, 3:** Show the elements for treatment (either "DRUG1" or "DRUG2"). These appear in the first treatment epoch in the TA dataset.

**Rows 4, 5:** Show the elements for treatment (either "DG1INDG" or "DG2INDG"). These appear in the second treatment epoch in the TA dataset.

**Row 6:** Shows the follow-up element.

**te.xpt**

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
|-----|---------|--------|------|---------|--------|--------|-------|
| 1 | XYZ | TE | SCRN | Screen | Informed Consent | 1 week after start of Element | P7D |
| 2 | XYZ | TE | DRUG1 | Drug 1 | First dose of Drug 1 | 4 weeks after start of Element | P28D |
| 3 | XYZ | TE | DRUG2 | Drug 2 | First dose of Drug 2 | 4 weeks after start of Element | P28D |
| 4 | XYZ | TE | DG1INDG | Drug 1 + Investigation Drug | First dose of Investigational Drug, where Investigational Drug is given with Drug 1 | 1 week after start of Element | P7D |
| 5 | XYZ | TE | DG2INDG | Drug 2 + Investigation Drug | First dose of Investigational Drug, where Investigational Drug is given with Drug 2 | 1 week after start of Element | P7D |
| 6 | XYZ | TE | FU | Follow-up | One day after last administration of study drug | | |

The TA dataset describes the design of the study.

**Rows 1, 5:** Screening portion of the trial arm.

**Rows 2, 6:** Represents the planned initial treatment arm of either "DRUG1" or "DRUG2".

**Rows 3, 7:** Represents the planned second treatment arm of either "DG1INDG" or "DG2INDG".

**Rows 4, 8:** Follow-up portion of the trial arm.

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

| Row | STUDYID | DOMAIN | USUBJID | SUBJID | RFXSTDTC | RFXENDTC | RFICDTC | RFPENDTC | SITEID | INVNAM | ARMCD | ARM | ACTARMCD | ACTARM | ARMNRS | ACTARMUD |
|-----|---------|--------|---------|--------|----------|----------|---------|----------|--------|--------|-------|-----|----------|--------|--------|----------|
| 1 | XYZ | DM | XYZ-767-001 | 001 | 2016-02-14 | 2016-04-19 | 2016-02-02 | 2016-04-24 | 01 | ADAMS, M | DG1INDG | Drug-1+Investigation-Drug | DG1INDG | Drug-1+Investigation-Drug | | |
| 3 | XYZ | DM | XYZ-767-002 | 002 | 2016-02-21 | 2016-04-24 | 2016-02-04 | 2016-04-29 | 01 | ADAMS, M | DG2INDG | Drug-2+Investigation-Drug | DG2INDG | Drug-2+Investigation-Drug | | |

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

**Rows 1, 5:** Represent the subjects' actual screening elements.

**Rows 2, 6:** Represent the subjects' actual first treatment epochs. The 2 subjects were in different elements in the first treatment epoch.

**Rows 3, 7:** Represent the subjects' actual second treatment epochs.

**Rows 4, 8:** Represent the subjects' actual follow-up elements.

**se.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SDSEQ | ETCD | SESTDTC | SEENDTC | TAETORD | EPOCH |
|-----|---------|--------|---------|-------|------|---------|---------|---------|-------|
| 1 | XYZ | SE | XYZ-767-001 | 1 | SCREEN | 2016-02-02 | 2016-02-14 | 1 | SCREENING |
| 2 | XYZ | SE | XYZ-767-001 | 2 | DRUG1 | 2016-02-14 | 2016-03-14 | 2 | TREATMENT 1 |
| 3 | XYZ | SE | XYZ-767-001 | 3 | DG1INDG | 2016-03-14 | 2016-04-24 | 3 | TREATMENT 2 |
| 4 | XYZ | SE | XYZ-767-001 | 4 | FU | 2016-04-19 | 2016-04-29 | 4 | FOLLOW-UP |
| 5 | XYZ | SE | XYZ-767-002 | 1 | SCREEN | 2016-02-21 | 2016-03-23 | 1 | SCREENING |
| 6 | XYZ | SE | XYZ-767-002 | 2 | DRUG2 | 2016-03-23 | 2016-03-24 | 2 | TREATMENT 1 |
| 7 | XYZ | SE | XYZ-767-002 | 3 | DG2INDG | 2016-03-24 | 2016-04-29 | 3 | TREATMENT 2 |
| 8 | XYZ | SE | XYZ-767-002 | 4 | FU | 2016-04-24 | 2016-04-29 | 4 | FOLLOW-UP |

The DS dataset shows the disposition events and protocol milestones for each subject.

**Rows 1, 8:** Show randomization to either DRUG 1 or DRUG 2 in the study.

**Rows 2, 9:** Represent the completion of the screening phase of the study. Note that although a form describing disposition of the screening epoch does not end until treatment starts, the screening epoch does not end until treatment starts.

**Rows 3, 5, 10, 12:** Represent the completion of drug for each EPOCH, where DSSCAT has the name of the drug(s). The DSSTDTC is the end date of study treatment for the epoch.

**Rows 4, 6, 11, 13:** Represent the completion of study participation for each epoch, where DSSCAT has the name of "STUDY PARTICIPATION". The DSSTDTC is the end date of study participation for the epoch. There was a 1-day evaluation post-treatment.

**Rows 7, 14:** Represent the completion of study participation follow-up epoch, where DSSCAT has the name of "STUDY PARTICIPATION". The DSSTDTC is the end date of study participation for the epoch.

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSSCAT | EPOCH | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|-------|---------|
| 1 | XYZ | DS | XYZ-767-001 | 1 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2016-02-13 |
| 2 | XYZ | DS | XYZ-767-001 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2016-03-13 |
| 3 | XYZ | DS | XYZ-767-001 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | DRUG1 | TREATMENT 1 | 2016-03-14 |
| 4 | XYZ | DS | XYZ-767-001 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-03-19 |
| 5 | XYZ | DS | XYZ-767-001 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | DG1INDG | TREATMENT 2 | 2016-04-20 |
| 6 | XYZ | DS | XYZ-767-001 | 6 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-04-20 |
| 7 | XYZ | DS | XYZ-767-001 | 7 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2016-04-24 |
| 8 | XYZ | DS | XYZ-767-002 | 1 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | | SCREENING | 2016-02-20 |
| 9 | XYZ | DS | XYZ-767-002 | 2 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | SCREENING | 2016-03-23 |
| 10 | XYZ | DS | XYZ-767-002 | 3 | COMPLETED | COMPLETED | DISPOSITION EVENT | DRUG2 | TREATMENT 1 | 2016-03-23 |
| 11 | XYZ | DS | XYZ-767-002 | 4 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 1 | 2016-03-24 |
| 12 | XYZ | DS | XYZ-767-002 | 5 | COMPLETED | COMPLETED | DISPOSITION EVENT | DG2INDG | TREATMENT 2 | 2016-04-25 |
| 13 | XYZ | DS | XYZ-767-002 | 6 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | TREATMENT 2 | 2016-04-25 |
| 14 | XYZ | DS | XYZ-767-002 | 7 | COMPLETED | COMPLETED | DISPOSITION EVENT | STUDY PARTICIPATION | FOLLOW-UP | 2016-04-29 |

## Example 11

The study in this example had 4 cycles of treatment within the treatment epoch, and each cycle was represented as an element. Although it is not a general requirement that each cycle is represented as a distinct element, doing so was important for this study. The study compared a current standard treatment with drugs A, B, and C. The protocol allowed for drug doses to be reduced under specified criteria. For drug C, these dose modifications could include dropping the drug. When drug C is dropped, the subject may transition to treatment with drugs A and B or to follow-up.

The TE dataset shows the elements of the trial.

**te.xpt**

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
|-----|---------|--------|------|---------|--------|--------|-------|
| 1 | DS10 | TE | SCRN | Screen | Informed Consent | Screening assessments are complete, up to 2 weeks after start of Element | |
| 2 | DS10 | TE | AB | Trt AB | First dose of treatment Element, where treatment is AB | 4 weeks after start of Element | P4W |
| 3 | DS10 | TE | ABC | Trt ABC | First dose of treatment Element, where treatment is AB+C | 4 weeks after start of Element | P4W |
| 4 | DS10 | TE | FU | Follow-up | Four weeks after start of last treatment element | Death, withdrawal of consent, or loss to follow-up. | |

The TA dataset shows the trial design. The sponsor chose to number elements starting with zero for the screening element. For the AB arm, TAETORD values are not chronological for this arm such that elements with TAETORD values of "2" or "5" would be during "Cycle 2", elements with TAETORD values of "3" or "6" would be during "Cycle 3", and elements with TAETORD values of "4" or "7" would be during "Cycle 4".

This example shows data for a subject who was randomized to treatment ABC. Treatment with drugs A and B was stopped after cycle 2 due to toxicity associated with drug C. The subject died during follow-up.

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
| 8 | DS10 | TA | ABC | ABC | 1 | ABC | Trt ABC | | If disease progression, go to follow-up epoch. If drug C is dropped, go to element with TAETORD = "5". | TREATMENT |
| 9 | DS10 | TA | ABC | ABC | 2 | ABC | Trt ABC | | If disease progression, go to follow-up epoch. If drug C is dropped, go to element with TAETORD = "5". | TREATMENT |
| 10 | DS10 | TA | ABC | ABC | 3 | ABC | Trt ABC | | If disease progression, go to follow-up epoch. If drug C is dropped, go to element with TAETORD = "5". | TREATMENT |
| 11 | DS10 | TA | ABC | ABC | 4 | ABC | Trt ABC | | Go to follow-up epoch. | TREATMENT |
| 12 | DS10 | TA | ABC | ABC | 5 | AB | Trt AB | | | TREATMENT |
| 13 | DS10 | TA | ABC | ABC | 6 | AB | Trt AB | | | TREATMENT |
| 14 | DS10 | TA | ABC | ABC | 7 | AB | Trt AB | | | TREATMENT |
| 15 | DS10 | TA | ABC | ABC | 8 | FU | Follow-up | | | FOLLOW-UP |

The SE dataset records the elements this subject experienced.

**Rows 1-4:** The subject participated in the screening epoch and 3 elements of the treatment epoch.

**Row 5:** The subject's fifth element was not "ABC" or "AB", as would have been expected if they received all 4 cycles of therapy, but "FU".

**se.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SESEQ | ETCD | SESTDTC | SEENDTC | SEUPDES | TAETORD | EPOCH |
|-----|---------|--------|---------|-------|------|---------|---------|---------|---------|-------|
| 1 | DS10 | SE | 101 | 1 | SCRN | 2015-01-21 | 2015-02-01 | 0 | | SCREENING |
| 2 | DS10 | SE | 101 | 2 | ABC | 2015-02-01 | 2015-03-01 | 1 | | TREATMENT |
| 3 | DS10 | SE | 101 | 3 | ABC | 2015-03-01 | 2015-03-29 | 2 | | TREATMENT |
| 4 | DS10 | SE | 101 | 4 | AB | 2015-03-29 | 2015-04-26 | 6 | | TREATMENT |
| 5 | DS10 | SE | 101 | 5 | FU | 2015-04-26 | 2015-09-19 | 8 | | FOLLOW-UP |

In this study, disposition of each treatment was collected, and disposition of study participation was collected for each epoch of the trial. The date of disposition for study treatment was defined as the date of the last dose of that treatment.

**Rows 1-2:** Show that informed consent was obtained and randomization occurred during the screening epoch.

**Row 3:** Shows disposition of study participation for screening epoch. The subject completed this epoch.

**Row 4:** Shows that drug C was ended during the second cycle (TAETORD = "2") of the treatment epoch. The subject did not complete treatment, due to disease progression. The date of disposition of the treatment epoch, DSSTDTC, is the date the subject started the follow-up element. For this study, that was defined as 4 weeks after the start of the last treatment element. This means that although the subject's last dose of treatment was "2015-04-14", the end of the treatment period was later, on "2015-04-26", when the subject started the follow-up treatment.

**Row 5:** Shows that drugs A and B were ended on the same day during the third cycle (TAETORD = "6") of the treatment epoch.

**Row 6:** Shows disposition of study participation in the treatment epoch.

**Row 7:** Shows disposition of study participation in the follow-up epoch. The subject died.

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
