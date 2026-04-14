# MH — Examples

## Example 1

In this example, a General Medical History CRF collected verbatim descriptions of conditions and events by body system (e.g., endocrine, metabolic), did not collect start date, but asked whether or not the condition was ongoing at the time of the visit. Another CRF page was used for cardiac history events. This page asked for date of onset of symptoms and date of diagnosis, but did not include the ongoing question.

**Rows 1-3:** MHCAT indicates that these data were collected on the General Medical History CRF, and MHSCAT displays the body systems specified on the CRF. The reported events were coded using a standard dictionary. MHDECOD and MHBODSYS display the preferred term and body system assigned through the coding process. MHENRTPT was populated based on the response to the "Ongoing at Study Start" question on the General Medical History CRF. MHENTPT displays the reference date for MHENRTPT, that is, the date the information was collected. If "Yes" was specified for Ongoing, MHENRTPT = "ONGOING"; if "No" was checked, MHENRTPT = "BEFORE". See Section 4.4.7, Use of Relative Timing Variables, for further guidance.

**Rows 4-5:** MHCAT indicates that these data were collected on the Cardiac Medical History CRF. MHSTDTC was populated with the date and time at which the event occurred. Because 2 kinds of start date were collected for congestive heart failure, there are 2 records for this event, with start dates with MHEVDTYP = "SYMPTOM ONSET" and MHEVDTYP = "DIAGNOSIS". The sponsor grouped these 2 records using the MHGRPID value "CHF".

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHGRPID | MHTERM | MHDECOD | MHCAT | MHSCAT | MHBODSYS | MHSTDTC | MHENRTPT | MHENTPT |
|-----|---------|--------|---------|-------|---------|--------|---------|-------|--------|----------|---------|----------|---------|
| 1 | ABC123 | MH | 123101 | 1 | | ASTHMA | Asthma | GENERAL MEDICAL HISTORY | RESPIRATORY | Respiratory system disorders | 2004-09-18 | ONGOING | |
| 2 | ABC123 | MH | 123101 | 2 | | FREQUENT HEADACHES | Headache | GENERAL MEDICAL HISTORY | CNS | Central and peripheral nervous system disorders | 2004-09-18 | ONGOING | |
| 3 | ABC123 | MH | 123101 | 3 | | BROKEN LEG | Bone fracture | GENERAL MEDICAL HISTORY | OTHER | Musculoskeletal system disorders | 2004-09-18 | BEFORE | |
| 4 | ABC123 | MH | 123101 | 4 | CHF | CONGESTIVE HEART FAILURE | Cardiac failure congestive | CARDIAC MEDICAL HISTORY | | Cardiac disorders | 2004-09-17 | | |
| 5 | ABC123 | MH | 123101 | 5 | CHF | CONGESTIVE HEART FAILURE | Cardiac failure congestive | CARDIAC MEDICAL HISTORY | | Cardiac disorders | 2004-09-19 | | |

## Example 2

In this example, data from 3 CRF modules related to medical history were collected:

- A General Medical History CRF collected descriptions of conditions and events by body system (e.g., endocrine, metabolic) and asked whether the conditions were ongoing at study start. The reported events were coded using a standard dictionary.
- A second CRF collected stroke history. Terms were selected from a list of terms taken from the standard dictionary.
- A third CRF asked whether the subject had any of a list of 4 specific risk factors.

In all of the records shown below, MHCAT is populated with the CRF module (general medical history, stroke history, or risk factors) through which the data were collected. MHPRESP and MHOCCUR were populated only when the term was prespecified, in keeping with MH assumption 4.

**Rows 1-3:** Show records from the General Medical History CRF. MHSCAT displays the body systems specified on the CRF. The coded terms are represented in MHDECOD. MHENRF has been populated based on the response to the "Ongoing at Study Start" question on the CRF. If "Yes" was specified, MHENRF = "DURING/AFTER"; if "No" was checked, MHENRF = "BEFORE". See Section 4.4.7, Use of Relative Timing Variables, for further guidance.

**Row 4:** Shows the record from the Stroke History CRF. MHSTDTC was populated with the date and time at which the event occurred.

**Rows 5-8:** Show records from the Risk Factors CRF. MHPRESP values of "Y" indicate that each risk factor was prespecified on the CRF. MHOCCUR is populated with "Y" or "N", corresponding to the CRF response to the questions for the 4 prespecified risk factors. The terms used to describe these risk factors were chosen to have associated codes in the standard dictionary.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHCAT | MHSCAT | MHBODSYS | MHPRESP | MHOCCUR | MHSTDTC | MHENRF |
|-----|---------|--------|---------|-------|--------|---------|-------|--------|----------|---------|---------|---------|--------|
| 1 | ABC123 | MH | 123101 | 1 | ASTHMA | Asthma | GENERAL MEDICAL HISTORY | RESPIRATORY | Respiratory system disorders | | | | DURING/AFTER |
| 2 | ABC123 | MH | 123101 | 2 | FREQUENT HEADACHES | Headache | GENERAL MEDICAL HISTORY | CNS | Central and peripheral nervous system disorders | | | | DURING/AFTER |
| 3 | ABC123 | MH | 123101 | 3 | BROKEN LEG | Bone fracture | GENERAL MEDICAL HISTORY | OTHER | Musculoskeletal system disorders | | | | BEFORE |
| 4 | ABC123 | MH | 123101 | 4 | ISCHEMIC STROKE | Ischaemic Stroke | STROKE HISTORY | | | | | 2004-09-17T07:30 | |
| 5 | ABC123 | MH | 123101 | 5 | DIABETES | Diabetes mellitus | RISK FACTORS | | | Y | Y | | |
| 6 | ABC123 | MH | 123101 | 6 | HYPERCHOLESTEROLEMIA | Hypercholesterolemia | RISK FACTORS | | | Y | Y | | |
| 7 | ABC123 | MH | 123101 | 7 | HYPERTENSION | Hypertension | RISK FACTORS | | | Y | Y | | |
| 8 | ABC123 | MH | 123101 | 8 | TIA | Transient ischaemic attack | RISK FACTORS | | | Y | N | | |

## Example 3

This is an example of a medical history CRF where the history of specific (prespecified) conditions is solicited. The conditions were not coded using a standard dictionary. The data were collected as part of the screening visit.

**Rows 1-9:** MHPRESP = "Y" indicates that these conditions were specifically queried. Presence or absence of the condition is represented in MHOCCUR.

**Row 10:** There was also a specific question about asthma, as indicated by MHPRESP = "Y", but this question was not asked. Because the question was not asked, MHOCCUR is null and MHSTAT = "NOT DONE". In this case, a reason for the absence of a response was collected, and this is represented in MHREASND.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHPRESP | MHOCCUR | MHSTAT | MHREASND | VISITNUM | VISIT | MHDTC | MHDY |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|--------|----------|----------|-------|-------|------|
| 1 | ABC123 | MH | 101002 | 1 | HISTORY OF EARLY CORONARY ARTERY DISEASE (<55 YEARS OF AGE) | Coronary Artery Disease | Y | N | | | 1 | SCREEN | 2006-04-22 | -5 |
| 2 | ABC123 | MH | 101002 | 2 | CONGESTIVE HEART FAILURE | Congestive Heart Failure | Y | N | | | 1 | SCREEN | 2006-04-22 | -5 |
| 3 | ABC123 | MH | 101002 | 3 | PERIPHERAL VASCULAR DISEASE | Peripheral Vascular Disease | Y | N | | | 1 | SCREEN | 2006-04-22 | -5 |
| 4 | ABC123 | MH | 101002 | 4 | TRANSIENT ISCHEMIC ATTACK | Transient Ischemic Attack | Y | Y | | 1 | | SCREEN | 2006-04-22 | -5 |
| 5 | ABC123 | MH | 101002 | 5 | ASTHMA | Asthma | Y | Y | | | 1 | SCREEN | 2006-04-22 | -5 |
| 6 | ABC123 | MH | 101003 | 1 | HISTORY OF EARLY CORONARY ARTERY DISEASE (<55 YEARS OF AGE) | Coronary Artery Disease | Y | Y | | | 1 | SCREEN | 2006-05-03 | -3 |
| 7 | ABC123 | MH | 101003 | 2 | CONGESTIVE HEART FAILURE | Congestive Heart Failure | Y | N | | | 1 | SCREEN | 2006-05-03 | -3 |
| 8 | ABC123 | MH | 101003 | 3 | PERIPHERAL VASCULAR DISEASE | Peripheral Vascular Disease | Y | N | | | 1 | SCREEN | 2006-05-03 | -3 |
| 9 | ABC123 | MH | 101003 | 4 | TRANSIENT ISCHEMIC ATTACK | Transient Ischemic Attack | Y | N | | | 1 | SCREEN | 2006-05-03 | -3 |
| 10 | ABC123 | MH | 101003 | 5 | ASTHMA | Asthma | Y | | NOT DONE | FORGOT TO ASK | 1 | SCREEN | 2006-05-03 | -3 |

## Example 4

This diabetes study included subjects with both type 1 diabetes and type 2 diabetes. Data collection included which kind of diabetes the subject had and the date of diagnosis of the condition.

**Rows 1-2:** Show that subject XYZ-001-001 had type 1 diabetes, and did not have type 2 diabetes. The start date in row 1 is the date of diagnosis, as indicated by MHEVDTYP="DIAGNOSIS". Because this subject did not have type 2 diabetes, no start date for type 2 diabetes was collected, so MHEVDTYP in row 2 is blank.

**Rows 3-4:** Show that subject XYZ-001-002 had type 2 diabetes, and did not have type 1 diabetes. The start date in row 4 is the date of diagnosis, as indicated by MHEVDTYP="DIAGNOSIS".

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHDECOD | MHEVDTYP | MHCAT | MHPRESP | MHOCCUR | MHDTC | MHSTDTC |
|-----|---------|--------|---------|-------|--------|---------|----------|-------|---------|---------|-------|---------|
| 1 | XYZ | MH | XYZ-001-001 | 1 | TYPE 1 DIABETES MELLITUS | Type 1 diabetes mellitus | DIAGNOSIS | DIABETES | Y | | 2010-09-26 | 2010-03-25 |
| 2 | XYZ | MH | XYZ-001-001 | 2 | TYPE 2 DIABETES MELLITUS | Type 2 diabetes mellitus | | DIABETES | Y | N | 2010-09-26 | |
| 3 | XYZ | MH | XYZ-001-002 | 1 | TYPE 1 DIABETES MELLITUS | Type 1 diabetes mellitus | | DIABETES | Y | N | 2010-10-26 | |
| 4 | XYZ | MH | XYZ-001-002 | 2 | TYPE 2 DIABETES MELLITUS | Type 2 diabetes mellitus | DIAGNOSIS | DIABETES | Y | | 2010-10-26 | 2010-04-25 |

## Example 5

This example shows data from a study in which data were collected about whether subjects had had any respiratory infections in the prior 6 months and, if they had, collected data on those respiratory infections. The example shows data for 2 subjects.

**Row 1:** Shows that subject 203 had no respiratory infections during the evaluation interval (the prior 6 months). The same value ("Respiratory Infections") in both MHTERM and MHCAT indicates that the occurrence question was about a group of medical conditions rather than a specific single medical condition.

**Row 2:** Shows that subject 204 did have at least 1 respiratory infection during the evaluation interval.

**Row 3:** Shows that subject 204 had a common cold during the evaluation interval. They did not provide an end date, but indicated that the infection had ended.

**Row 4:** Shows that subject 204 had bronchitis during the evaluation interval, and that an end date for the infection was provided.

**mh.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MHSEQ | MHTERM | MHCAT | MHPRESP | MHOCCUR | MHDTC | MHENDTC | MHDY | MHEVLINT | MHENRTPT | MHENTPT |
|-----|---------|--------|---------|-------|--------|-------|---------|---------|-------|---------|------|----------|----------|---------|
| 1 | XYZ234 | MH | 203 | 1 | RESPIRATORY INFECTIONS | RESPIRATORY INFECTIONS | Y | N | 2019-11-02 | | -2 | -P6M | | |
| 2 | XYZ234 | MH | 204 | 1 | RESPIRATORY INFECTIONS | RESPIRATORY INFECTIONS | Y | Y | 2019-12-08 | | -1 | -P6M | | |
| 3 | XYZ234 | MH | 204 | 2 | COMMON COLD | RESPIRATORY INFECTIONS | | | 2019-12-08 | | -1 | -P6M | BEFORE | 2019-12-08 |
| 4 | XYZ234 | MH | 204 | 3 | BRONCHITIS | RESPIRATORY INFECTIONS | | | 2019-12-08 | 2019-10-20 | -1 | -P6M | BEFORE | 2019-12-08 |
