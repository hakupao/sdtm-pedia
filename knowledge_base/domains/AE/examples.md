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
