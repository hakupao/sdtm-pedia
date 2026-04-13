# DD — Examples

## Example 1

This example shows the primary cause of death for 3 subjects. The CRF also collected the location of the subject's death and a secondary cause of death.

**Rows 1-2:** Show the primary cause of death and location of death for a subject. DDDTC is the date of assessment.

**Rows 3-4:** Show records for primary cause of death and location of death for another subject for whom the information was not known.

**Rows 5-7:** Show primary and secondary cause of death and location of death for a third subject.

**dd.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DDSEQ | DDTESTCD | DDTEST | DDORRES | DDSTRESC | DDDTC |
|-----|---------|--------|---------|-------|----------|--------|---------|----------|-------|
| 1 | ABC123 | DD | ABC12301001 | 1 | PRCDTH | Primary Cause of Death | SUDDEN CARDIAC DEATH | SUDDEN CARDIAC DEATH | 2011-01-12 |
| 2 | ABC123 | DD | ABC12301001 | 2 | LOCDTH | Location of Death | HOME | HOME | 2011-01-12 |
| 3 | ABC123 | DD | ABC12301002 | 1 | PRCDTH | Primary Cause of Death | UNKNOWN | UNKNOWN | 2011-03-15 |
| 4 | ABC123 | DD | ABC12301002 | 2 | LOCDTH | Location of Death | UNKNOWN | UNKNOWN | 2011-03-15 |
| 5 | ABC123 | DD | ABC12301023 | 1 | PRCDTH | Primary Cause of Death | CARDIAC ARRHYTHMIA | CARDIAC ARRHYTHMIA | 2011-09-09 |
| 6 | ABC123 | DD | ABC12301023 | 2 | SECDTH | Secondary Cause of Death | CHF | CONGESTIVE HEART FAILURE | 2011-09-09 |
| 7 | ABC123 | DD | ABC12301023 | 3 | LOCDTH | Location of Death | MEMORIAL HOSPITAL | HOSPITAL | 2011-09-09 |

## Example 2

This example illustrates how the DD, Disposition (DS), and AE data for a subject were linked using RELREC. Note that each of these domains serves a different purpose, even though the information is related. This subject had a fatal adverse event, represented in the AE domain.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AESTDTC | AEENDTC | AEDECOD | AEBODSYS | AEOUT | AESER | AESDTH |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|----------|-------|-------|--------|
| 1 | ABC123 | AE | ABC12301001 | 6 | SUDDEN CARDIAC DEATH | 2011-01-10 | 2011-01-10 | SUDDEN CARDIAC DEATH | CARDIOVASCULAR SYSTEM | FATAL | Y | Y |

The primary cause of death was collected and is represented in DD. In this case, the result for primary cause of death is the same as the term in the AE record.

**dd.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DDSEQ | DDTESTCD | DDTEST | DDORRES | DDSTRESC | DDDTC |
|-----|---------|--------|---------|-------|----------|--------|---------|----------|-------|
| 1 | ABC123 | DD | ABC12301001 | 1 | PRCDTH | Primary Cause of Death | SUDDEN CARDIAC DEATH | SUDDEN CARDIAC DEATH | 2011-01-12 |

The subject's death is also represented in the DS domain as the reason for withdrawal from the study.

**Rows 1-2:** Show typical protocol milestones and disposition events.

**Row 3:** Shows the date the death event occurred (DSSTDTC) and was recorded (DSDTC).

**ds.xpt**

| Row | STUDYID | DOMAIN | USUBJID | DSSEQ | DSTERM | DSDECOD | DSCAT | DSDTC | DSSTDTC |
|-----|---------|--------|---------|-------|--------|---------|-------|-------|---------|
| 1 | ABC123 | DS | ABC12301001 | 1 | INFORMED CONSENT OBTAINED | INFORMED CONSENT OBTAINED | PROTOCOL MILESTONE | 2011-01-02 | 2011-01-02 |
| 2 | ABC123 | DS | ABC12301001 | 2 | RANDOMIZED | RANDOMIZED | PROTOCOL MILESTONE | 2011-01-03 | 2011-01-03 |
| 3 | ABC123 | DS | ABC12301001 | 3 | SUDDEN CARDIAC DEATH | DEATH | DISPOSITION EVENT | 2011-01-10 | 2011-01-10 |

The relationship between the DS, AE, and DD records that reflect the subject's death is represented in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC123 | DS | ABC12301001 | DSSEQ | 3 | | 1 |
| 2 | ABC123 | AE | ABC12301001 | AESEQ | 6 | | 1 |
| 3 | ABC123 | DD | ABC12301001 | DDSEQ | 1 | | 1 |
