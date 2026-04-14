# FA — Examples

## Example 1

The following example CRF collects severity and symptoms data at multiple time points about a migraine event, relative to dosing.

In this example trial, migraines and symptoms associated with migraines were considered clinical events rather than reportable adverse events. The migraine, its sponsor identifier (i.e., the "Migraine Reference Number" on the CRF), and its start date were represented in a CE record.

**ce.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CESEQ | CESPID | CETERM | CEDECOD | CESTDTC |
|-----|---------|--------|---------|-------|--------|--------|---------|---------|
| 1 | ABC | CE | ABC-123 | 1 | 90567 | Migraine | Migraine | 2007-05-16T10:30 |

The time the migraine medication was taken was recorded in the Exposure (EX) domain. This date also serves as the reference time point for the symptom assessments.

**ex.xpt**

| Row | STUDYID | DOMAIN | USUBJID | EXSEQ | EXSPID | EXTRT | EXDOSE | EXDOSU | EXDOSFRM | EXDOSFRQ | EXROUTE | EPOCH | EXSTDTC | EXENDTC |
|-----|---------|--------|---------|-------|--------|-------|--------|--------|----------|----------|---------|-------|---------|---------|
| 1 | ABC | EX | ABC-123 | 1 | 4 | CURALL | 50 | mg | TABLET | ONCE | ORAL | TREATMENT | 2007-05-16T11:05 | 2007-05-16T11:05 |

The remaining data on the CRF were "snapshots" taken at 3 time points; in accordance with Section 6.4.1, When to Use Findings About Events or Interventions, criterion 1, these were represented as findings about events. The FACAT value "MIGRAINE SYMPTOMS" was used to represent the fact that these data were collected in a CRF module called "Migraine Symptoms Diary."

**Rows 1, 6, 11:** Severity of the migraine was represented with FATESTCD="SEV". This FATESTCD value is derived from the events class variable name --SEV, and represents the same assessment as CESEV, except that this assessment is at a point in time rather than for the event as a whole.
**Rows 2-5, 7-10, 12-15:** The presence of symptoms associated with migraine was represented with the name of the symptom in FAOBJ, as the data collected is about the occurrence of a particular symptom. The test code value "OCCUR" is derived from the events class variable name --OCCUR, but is an assessment at a point in time, rather than about the event as a whole. The relationship of these symptoms to migraine is represented in FACAT, which indicates that these data were collected in the Migraine Symptoms Diary.

**face.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FACAT | FAORRES | FASTRESC | FADTC | FATPT | FATPTNUM | FAELTM | FATPTREF |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|-------|---------|----------|-------|-------|----------|--------|----------|
| 1 | ABC | FA | ABC-123 | 1 | 90567 | SEV | Severity/Intensity | Migraine | MIGRAINE SYMPTOMS | SEVERE | SEVERE | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 2 | ABC | FA | ABC-123 | 2 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Light | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 3 | ABC | FA | ABC-123 | 3 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Sound | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 4 | ABC | FA | ABC-123 | 4 | 90567 | OCCUR | Occurrence Indicator | Nausea | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 5 | ABC | FA | ABC-123 | 5 | 90567 | OCCUR | Occurrence Indicator | Aura | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 5M PRE-DOSE | 1 | -PT5M | DOSING |
| 6 | ABC | FA | ABC-123 | 6 | 90567 | SEV | Severity/Intensity | Migraine | MIGRAINE SYMPTOMS | MODERATE | MODERATE | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 7 | ABC | FA | ABC-123 | 7 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Light | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 8 | ABC | FA | ABC-123 | 8 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Sound | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 9 | ABC | FA | ABC-123 | 9 | 90567 | OCCUR | Occurrence Indicator | Nausea | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 10 | ABC | FA | ABC-123 | 10 | 90567 | OCCUR | Occurrence Indicator | Aura | MIGRAINE SYMPTOMS | Y | Y | 2007-05-16 | 30M POST-DOSE | 2 | PT30M | DOSING |
| 11 | ABC | FA | ABC-123 | 11 | 90567 | SEV | Severity/Intensity | Migraine | MIGRAINE SYMPTOMS | MILD | MILD | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 12 | ABC | FA | ABC-123 | 12 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Light | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 13 | ABC | FA | ABC-123 | 13 | 90567 | OCCUR | Occurrence Indicator | Sensitivity To Sound | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 14 | ABC | FA | ABC-123 | 14 | 90567 | OCCUR | Occurrence Indicator | Nausea | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |
| 15 | ABC | FA | ABC-123 | 15 | 90567 | OCCUR | Occurrence Indicator | Aura | MIGRAINE SYMPTOMS | N | N | 2007-05-16 | 90M POST-DOSE | 3 | PT90M | DOSING |

A dataset-level relationship in RELREC is based on the sponsor ID (--SPID) value, which was populated with a system-generated identifier unique to each iteration of this form.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | CE | | CESPID | | ONE | 1 |
| 2 | ABC | FA | | FASPID | | MANY | 1 |

## Example 2

This CRF collects details about injection site rash events at each visit, until resolved.

In this scenario, the injection site rash event was considered a reportable adverse event; therefore, the rash itself was represented in the AE domain. The rash assessment form collects a reference number for the AE, represented in AESPID. Certain required or expected variables have been omitted from the example dataset in consideration of space and clarity.

Additional data about the rash were collected at visits 3 and 4, which occurred 2 days and 9 days after the start of the rash. These data were represented in an FA dataset because they were not about the event as a whole (see Section 6.4.1, When to Use Findings About Events or Interventions, criterion 1). In addition, the measurement of the rash requires multiple variables (value and unit) for its representation and the numbers of various kinds of lesions within the rash are a set of similar assessments of the event (see Section 6.4.1, When to Use Findings About Events or Interventions, criterion 2).

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AESPID | AETERM | AEBODSYS | AELOC | AELAT | AESEV | AESER | AEACN | AESTDTC |
|-----|---------|--------|---------|-------|--------|--------|----------|-------|-------|-------|-------|-------|---------|
| 1 | XYZ | AE | XYZ-789 | 47869 | 5 | Injection site rash | General disorders and administration site conditions | ARM | LEFT | MILD | N | NOT APPLICABLE | 2007-05-10 |

**faae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FAORRES | FAORRESU | FASTRESC | FASTRESU | VISITNUM | FADTC |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|---------|----------|----------|----------|----------|-------|
| 1 | XYZ | FA | XYZ-789 | 123451 | 5 | LDIAM | Longest Diameter | Injection Site Rash | 2.5 | IN | 2.5 | IN | 3 | 2007-05-12 |
| 2 | XYZ | FA | XYZ-789 | 123452 | 5 | MACRNG | Number of Macules Range | Injection Site Rash | 26 to 100 | | 26 to 100 | | 3 | 2007-05-12 |
| 3 | XYZ | FA | XYZ-789 | 123453 | 5 | FAPRNG | Number of Papules Range | Injection Site Rash | 1 to 25 | | 1 to 25 | | 3 | 2007-05-12 |
| 4 | XYZ | FA | XYZ-789 | 123454 | 5 | VESRNG | Number of Vesicles Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 5 | XYZ | FA | XYZ-789 | 123455 | 5 | PUSRNG | Number of Pustules Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 6 | XYZ | FA | XYZ-789 | 123456 | 5 | SCBRNG | Number of Scabs Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 7 | XYZ | FA | XYZ-789 | 123457 | 5 | SCRRNG | Number of Scars Range | Injection Site Rash | 0 | | 0 | | 3 | 2007-05-12 |
| 8 | XYZ | FA | XYZ-789 | 123459 | 5 | LDIAM | Longest Diameter | Injection Site Rash | 1 | IN | 1 | IN | 4 | 2007-05-19 |
| 9 | XYZ | FA | XYZ-789 | 123460 | 5 | MACRNG | Number of Macules Range | Injection Site Rash | 1 to 25 | | 1 to 25 | | 4 | 2007-05-19 |
| 10 | XYZ | FA | XYZ-789 | 123461 | 5 | FAPRNG | Number of Papules Range | Injection Site Rash | 1 to 25 | | 1 to 25 | | 4 | 2007-05-19 |
| 11 | XYZ | FA | XYZ-789 | 123462 | 5 | VESRNG | Number of Vesicles Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |
| 12 | XYZ | FA | XYZ-789 | 123463 | 5 | PUSRNG | Number of Pustules Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |
| 13 | XYZ | FA | XYZ-789 | 123464 | 5 | SCBRNG | Number of Scabs Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |
| 14 | XYZ | FA | XYZ-789 | 123465 | 5 | SCRRNG | Number of Scars Range | Injection Site Rash | 0 | | 0 | | 4 | 2007-05-19 |

The FA records were linked to the parent CE record via the AE reference number, which was used to populate both AESPID and FASPID.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | XYZ | AE | | AESPID | | ONE | 23 |
| 2 | XYZ | FA | | FASPID | | MANY | 23 |

## Example 3

This CRF collects information about rheumatoid arthritis. In this scenario, rheumatoid arthritis is a prerequisite for participation in an osteoporosis trial and was not collected as a Medical History (MH) event.

In this study, data were collected only at baseline. Because the occurrence and severity apply to the symptoms as a whole, they are represented in the MH domain. Note that the average duration of early morning stiffness cannot be represented in MHDUR because MHDUR would be the duration of the entire event, rather than the average of daily durations.

**Row 1:** Because the CRF specifically collected date of diagnosis for rheumatoid arthritis, MHEVDTYP is populated with DIAGNOSIS to indicate that the date in MHSTDTC is the date of diagnosis.
**Rows 2-6:** No start or end dates were collected for the symptoms, so the variable MHEVDTYP is not relevant for those records. MHEVDTYP is used only to specify the aspect of the event used to determine start and/or end dates.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHEVDTYP | MHCAT | MHSCAT | MHPRESP | MHOCCUR | MHSEV | MHDTC | MHSTDTC | MHEVLINT |
|-----|---------|--------|---------|-------|--------|---------|----------|-------|--------|---------|---------|-------|-------|---------|----------|
| 1 | ABC | MH | 001-001 | 1 | RHEUMATOID ARTHRITIS | Rheumatoid arthritis | DIAGNOSIS | RHEUMATOID ARTHRITIS HISTORY | | Y | Y | | | 2003 | -P6M |
| 2 | ABC | MH | 001-001 | 2 | JOINT STIFFNESS | Joint stiffness | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | Y | SEVERE | 2006-08-13 | | -P6M |
| 3 | ABC | MH | 001-001 | 3 | JOINT SWELLING | Joint swelling | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | Y | MODERATE | 2006-08-13 | | -P6M |
| 4 | ABC | MH | 001-001 | 4 | JOINT PAIN | Arthralgia | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | Y | MODERATE | 2006-08-13 | | -P6M |
| 5 | ABC | MH | 001-001 | 5 | MALAISE | Malaise | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | Y | MILD | 2006-08-13 | | -P6M |
| 6 | ABC | MH | 001-001 | 6 | EARLY MORNING STIFFNESS | Stiffness | | RHEUMATOID ARTHRITIS HISTORY | SYMPTOMS | Y | | | 2006-08-13 | | -P6M |

The average duration of early morning stiffness would be represented in ISO 8601 duration format as a supplemental qualifier.

**suppmh.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | ABC | MH | 001-001 | MHSEQ | 6 | MHAVDDUR | Average Daily Duration | PT1H30M | CRF | |

## Example 4

In this example, the occurrence of prespecified adverse events was solicited at every visit and the visit date was used as the date of collection. The data collected meet criterion 3 in Section 6.4.1, When to Use Findings About Events or Interventions; that is, data that indicate the occurrence of prespecified AEs.

**Rows 1, 4:** "Headache" was reported at both visits.
**Rows 2, 5:** "Respiratory infection" was not present at either visit.
**Row 3:** The investigator did not ask the subject about the occurrence of nausea. This was represented by FASTAT="NOT DONE".
**Row 6:** "Nausea" was reported at visit 3.

**faae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FATESTCD | FATEST | FAOBJ | FAORRES | FASTRESC | FASTAT | VISITNUM | VISIT | FADTC | FAEVINTX |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|----------|--------|----------|-------|-------|----------|
| 1 | ABC101 | FA | 1234 | 1 | OCCUR | Occurrence Indicator | Headache | Y | Y | | 2 | VISIT 2 | 2005-10-01 | SINCE LAST VISIT |
| 2 | ABC101 | FA | 1234 | 2 | OCCUR | Occurrence Indicator | Respiratory Infection | N | N | | 2 | VISIT 2 | 2005-10-01 | SINCE LAST VISIT |
| 3 | ABC101 | FA | 1234 | 3 | OCCUR | Occurrence Indicator | Nausea | | | NOT DONE | 2 | VISIT 2 | 2005-10-01 | SINCE LAST VISIT |
| 4 | ABC101 | FA | 1234 | 4 | OCCUR | Occurrence Indicator | Headache | Y | Y | | 3 | VISIT 3 | 2005-10-10 | SINCE LAST VISIT |
| 5 | ABC101 | FA | 1234 | 5 | OCCUR | Occurrence Indicator | Respiratory Infection | N | N | | 3 | VISIT 3 | 2005-10-10 | SINCE LAST VISIT |
| 6 | ABC101 | FA | 1234 | 6 | OCCUR | Occurrence Indicator | Nausea | Y | Y | | 3 | VISIT 3 | 2005-10-10 | SINCE LAST VISIT |

For each prespecified adverse event for which FAORRES = "Y", the adverse event has a record in the AE domain with AEPRESP = "Y". No relationship was collected to link the FAAE record for the occurrence indicator test with the AE entries, so no RELREC was created.

Note that not all AE expected variables are included in the following example.

**ae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AESEQ | AETERM | AEDECOD | AEPRESP | AEBODSYS | AESEV | AEACN | AESTDTC | AEENDTC |
|-----|---------|--------|---------|-------|--------|---------|---------|----------|-------|-------|---------|---------|
| 1 | ABC101 | AE | 1234 | 1 | Headache | Headache | Y | Nervous system disorders | MILD | NONE | 2005-09-30 | 2005-10-03 |
| 2 | ABC101 | AE | 1234 | 2 | Nausea | Nausea | Y | Gastrointestinal disorders | MODERATE | NONE | 2005-10-08 | 2005-10-09 |

**Row 1:** Comparison of this AE record with the FA dataset records for "Headache" shows that there are 2 records with FAOBJ="Headache". FAORRES="Y" indicates that this AE record is associated with both FA records, because this headache started before visit 2 and ended between visits 2 and 3.

**Row 2:** Comparison of this AE record with the FA dataset shows that this AE started and ended in the time between visits 2 and 3, and is consistent with the FA response for FAOBJ="Nausea" for visit 3.

## Example 5

In this example, data about prespecified symptoms of the disease under study were collected on a daily basis. Although the date of the assessment was captured in the CRF header (not shown), start and end timing of the prespecified symptoms was not.

The collected data were represented in FA because they meet criterion 1 in Section 6.4.1, When to Use Findings About Events or Interventions, that is, data that do not describe an event or intervention as a whole. In addition, the volume of vomit data met criterion 2 data ("about" an event or intervention), having qualifiers that can be represented in Findings variables (e.g., units, method).

This SDTM example represents data from 2 visits for 1 subject. FAEVINTX indicates that assessments were for the previous 24 hours.

**Rows 1-4:** Show the results for the vomiting tests at visit 1. Because the number of episodes was recorded as ">10", this is represented in FASTRESC but not in FASTRESN.
**Rows 5-7:** Show the results for the diarrhea tests at visit 1.
**Rows 8-10:** Show the results for the nausea tests at visit 1.
**Row 11:** Shows that vomiting did not occur in the 24 hours before visit 2; thus, volume, number of episodes, and severity were not applicable.
**Rows 12-14:** Show the results for the diarrhea tests at visit 2.
**Row 15:** Indicates that the occurrence of nausea was not assessed at visit 2.

**face.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FATESTCD | FATEST | FAOBJ | FACAT | FAORRES | FAORRESU | FASTRESC | FASTRESN | FASTRESU | FASTAT | VISITNUM | VISIT | FADTC | FAEVLINT |
|-----|---------|--------|---------|-------|----------|--------|-------|-------|---------|----------|----------|----------|----------|--------|----------|-------|-------|----------|
| 1 | XYZ | FA | XYZ-701-002 | 1 | OCCUR | Occurrence Indicator | Vomiting | GERD SYMPTOMS | Y | | Y | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 2 | XYZ | FA | XYZ-701-002 | 2 | VOL | Volume | Vomiting | GERD SYMPTOMS | 250 | mL | 250 | 250 | mL | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 3 | XYZ | FA | XYZ-701-002 | 3 | NUMEPISO | Number of Episodes | Vomiting | GERD SYMPTOMS | >10 | | >10 | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 4 | XYZ | FA | XYZ-701-002 | 4 | SEV | Severity/Intensity | Vomiting | GERD SYMPTOMS | SEVERE | | SEVERE | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 5 | XYZ | FA | XYZ-701-002 | 5 | OCCUR | Occurrence Indicator | Diarrhea | GERD SYMPTOMS | Y | | Y | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 6 | XYZ | FA | XYZ-701-002 | 6 | NUMEPISO | Number of Episodes | Diarrhea | GERD SYMPTOMS | 2 | | 2 | 2 | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 7 | XYZ | FA | XYZ-701-002 | 7 | SEV | Severity/Intensity | Diarrhea | GERD SYMPTOMS | SEVERE | | SEVERE | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 8 | XYZ | FA | XYZ-701-002 | 8 | OCCUR | Occurrence Indicator | Nausea | GERD SYMPTOMS | Y | | Y | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 9 | XYZ | FA | XYZ-701-002 | 9 | NUMEPISO | Number of Episodes | Nausea | GERD SYMPTOMS | 1 | | 1 | 1 | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 10 | XYZ | FA | XYZ-701-002 | 10 | SEV | Severity/Intensity | Nausea | GERD SYMPTOMS | MODERATE | | MODERATE | | | | 1 | VISIT 1 | 2006-02-02 | -PT24H |
| 11 | XYZ | FA | XYZ-701-002 | 11 | OCCUR | Occurrence Indicator | Vomiting | GERD SYMPTOMS | N | | N | | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 12 | XYZ | FA | XYZ-701-002 | 12 | OCCUR | Occurrence Indicator | Diarrhea | GERD SYMPTOMS | Y | | Y | | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 13 | XYZ | FA | XYZ-701-002 | 13 | NUMEPISO | Number of Episodes | Diarrhea | GERD SYMPTOMS | 1 | | 1 | 1 | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 14 | XYZ | FA | XYZ-701-002 | 14 | SEV | Severity/Intensity | Diarrhea | GERD SYMPTOMS | SEVERE | | SEVERE | | | | 2 | VISIT 2 | 2006-02-03 | -PT24H |
| 15 | XYZ | FA | XYZ-701-002 | 15 | OCCUR | Occurrence Indicator | Nausea | GERD SYMPTOMS | | | | | | NOT DONE | 2 | VISIT 2 | 2006-02-03 | -PT24H |

## Example 6

In this example, the sponsor's definition of "event" meant that 1 record would be created for each adverse event, covering it from start to finish (see Section 6.2.1, Adverse Events, assumption 6.4). The AE module also collected information about severity at each visit.

An electronic data collection instrument would probably be constructed as 2 related modules:
- A module for the adverse event, where a record would be entered for each event
- A module for the severity assessment, where a record would be entered for each assessment

*Note: The FA Example 6 CRF shows severity assessed at Visits 2-6 for up to 3 concurrent AEs per subject. The data collected about severity at each visit represents snapshots or slices of the AE over time, meeting criterion 1 for When to Use Findings About Events or Interventions.*

AE collection started after visit 1, so the first severity data was collected at visit 2.

The collected data met criterion 1 in Section 6.4.1, When to Use Findings About Events or Interventions, for data that do not describe an event or intervention as a whole.

In this example, the sponsor populated AESEV with the maximum severity over the course of the event. This was not directly collected, but rather determined from the weekly maximum severity assessments collected on the CRF. For clarity, only selected variables in the AE dataset are shown here.

**ae.xpt**

| Row | DOMAIN | USUBJID | AESEQ | AESPID | AETERM | AEDECOD | AESEV | AESTDTC | AEENDTC |
|-----|--------|---------|-------|--------|--------|---------|-------|---------|---------|
| 1 | AE | 123 | 1 | 1 | Morning queasiness | Nausea | MODERATE | 2006-02-01 | 2006-02-23 |
| 2 | AE | 123 | 2 | 2 | Watery stools | Diarrhea | MILD | 2006-02-01 | 2006-02-15 |

The values in FAOBJ are the values from AEDECOD, which were assigned during coding, rather than directly collected. The values in FASPID are the AE identifiers from AESPID. FAEVINTX indicates that the evaluation was for the period since the last visit.

**Rows 1-4:** Show severity data collected at the 4 visits that occurred between the start and end of the AE "Morning queasiness". FAOBJ=NAUSEA, which is the value of AEDECOD in the associated AE record.

**Rows 5-6:** Show severity data collected at the 2 visits that occurred between the start and end of the AE "Watery stools." FAOBJ=DIARRHEA, which is the value of AEDECOD in the associated AE record.

**faae.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FASEQ | FASPID | FATESTCD | FATEST | FAOBJ | FAORRES | FACOLSRT | VISITNUM | VISIT | FADTC | FAEVINTX |
|-----|---------|--------|---------|-------|--------|----------|--------|-------|---------|----------|----------|-------|-------|----------|
| 1 | XYZ | FA | XYZ-US-701-002 | 1 | 1 | SEV | Severity/Intensity | Nausea | MILD | MAXIMUM | 2 | VISIT 2 | 2006-02-02 | SINCE LAST VISIT |
| 2 | XYZ | FA | XYZ-US-701-002 | 2 | 1 | SEV | Severity/Intensity | Nausea | MODERATE | MAXIMUM | 3 | VISIT 3 | 2006-02-09 | SINCE LAST VISIT |
| 3 | XYZ | FA | XYZ-US-701-002 | 3 | 1 | SEV | Severity/Intensity | Nausea | MODERATE | MAXIMUM | 4 | VISIT 4 | 2006-02-16 | SINCE LAST VISIT |
| 4 | XYZ | FA | XYZ-US-701-002 | 4 | 1 | SEV | Severity/Intensity | Nausea | MILD | MAXIMUM | 5 | VISIT 5 | 2006-02-23 | SINCE LAST VISIT |
| 5 | XYZ | FA | XYZ-US-701-002 | 5 | 2 | SEV | Severity/Intensity | Diarrhea | MILD | MAXIMUM | 2 | VISIT 2 | 2006-02-02 | SINCE LAST VISIT |
| 6 | XYZ | FA | XYZ-US-701-002 | 6 | 2 | SEV | Severity/Intensity | Diarrhea | MILD | MAXIMUM | 3 | VISIT 3 | 2006-02-09 | SINCE LAST VISIT |

Because the AE identifier (AESPID) was included in the FA dataset, AE and FA data can be related with a dataset-to-dataset relationship.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | AE | | AESPID | | ONE | 1 |
| 2 | ABC | FA | | FASPID | | MANY | 1 |
