# CE — Examples

## Example 1

In this example, data were collected about prespecified events that, in the context of this study, were not reportable as AEs. The data were collected in a log independent of visits, rather than in visit-based CRF modules, so visit and date of collection (CEDTC) data were not collected.

**CRF: CE Example 1 — Prespecified Clinical Events**

Record start dates of any of the following signs that occurred during the study.

| Clinical Sign | Did it occur? | Start Date of First Episode |
|---------------|--------------|---------------------------|
| Rash | ( ) No  ( ) Yes | ___ / ___ / ___ |
| Wheezing | ( ) No  ( ) Yes | ___ / ___ / ___ |
| Edema | ( ) No  ( ) Yes | ___ / ___ / ___ |
| Conjunctivitis | ( ) No  ( ) Yes | ___ / ___ / ___ |

**Rows 1-3:** Show 3 symptoms which occurred and their start dates.

**Row 4:** Shows that conjunctivitis did not occur. Because there was no event, there is no start date.

**ce.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CESEQ | CETERM | CEPRESP | CEOCCUR | CESTDTC |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|
| 1 | ABC123 | CE | 123 | 1 | Rash | Y | Y | 2006-05-03 |
| 2 | ABC123 | CE | 123 | 2 | Wheezing | Y | Y | 2006-05-03 |
| 3 | ABC123 | CE | 123 | 3 | Edema | Y | Y | 2006-05-03 |
| 4 | ABC123 | CE | 123 | 4 | Conjunctivitis | Y | N | |

## Example 2

In this example, the CRF included both questions about prespecified clinical events (events not reportable as AEs in the context of this study) and places for specifying additional clinical events. No explicit evaluation interval is given, but the implicit time frame for the question is "during the study." Although this example CRF shows only 1 row for each symptom, if a symptom occurred more than once, data would be collected for each time it occurred.

These data are about the event as a whole, so they are represented in the CE domain.

In this example, the use of "Other, Specify" for clinical events is likely to require manual review of the data, to be sure that none of the write-in terms should have been reported as adverse events based on the sponsor's criteria for this study.

**CRF: CE Example 2 — Clinical Events with Severity**

| Event | | Date Started | Date Ended | Severity |
|-------|---|-------------|-----------|----------|
| Nausea | ( ) Yes  ( ) No | ___ / ___ / ___ (dd/mmm/yyyy) | ___ / ___ / ___ (dd/mmm/yyyy) | ( ) Mild  ( ) Moderate  ( ) Severe |
| Vomit | ( ) Yes  ( ) No | ___ / ___ / ___ (dd/mmm/yyyy) | ___ / ___ / ___ (dd/mmm/yyyy) | ( ) Mild  ( ) Moderate  ( ) Severe |
| Diarrhea | ( ) Yes  ( ) No | ___ / ___ / ___ (dd/mmm/yyyy) | ___ / ___ / ___ (dd/mmm/yyyy) | ( ) Mild  ( ) Moderate  ( ) Severe |
| Other, Specify: ___ | | ___ / ___ / ___ (dd/mmm/yyyy) | ___ / ___ / ___ (dd/mmm/yyyy) | ( ) Mild  ( ) Moderate  ( ) Severe |

**Rows 1-2:** Show records for 2 instances of the prespecified clinical event, nausea. The CEPRESP value of "Y" indicates that there was a probing question; the response to the probe (CEOCCUR) was "Yes". CEPRESP and CEOCCUR are included in both records for "Nausea". The record includes additional data about the event.

**Row 3:** Shows a record for the prespecified clinical event, vomit. The CEPRESP value of "Y" indicates that there was a probing question; the response to the question (CEOCCUR) was "No". Because there was no event, severity and start and end dates are null.

**Row 4:** Shows a record for the prespecified clinical event, diarrhea. The value "Y" for CEPRESP indicates it was prespecified. The CESTAT value of NOT DONE indicates that the probing question was not asked or that there was no answer.

**Row 5:** Shows a record for a write-in clinical event recorded in the "Other, Specify" space. Because this event was not prespecified, CEPRESP and CEOCCUR are null. See Section 4.2.7.3, "Specify" Values for Topic Variables, for further information on populating the topic variable when "Other, Specify" is used on the CRF.

**ce.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CESEQ | CETERM | CEDECOD | CEPRESP | CEOCCUR | CESTAT | CESEV | CESTDTC | CEENDTC |
|-----|---------|--------|---------|-------|--------|---------|---------|---------|--------|-------|---------|---------|
| 1 | ABC123 | CE | 123 | 1 | NAUSEA | Nausea | Y | Y | | MODERATE | 2005-10-12 | |
| 2 | ABC123 | CE | 123 | 2 | NAUSEA | Nausea | Y | Y | | MODERATE | 2005-10-14 | 2005-10-15 |
| 3 | ABC123 | CE | 123 | 3 | VOMIT | Vomiting | Y | N | | | | |
| 4 | ABC123 | CE | 123 | 4 | DIARRHEA | Diarrhoea | Y | | NOT DONE | | | |
| 5 | ABC123 | CE | 123 | 5 | SEVERE HEAD PAIN | Headache | | | | SEVERE | 2005-10-09 | 2005-10-11 |

## Example 3

In this study, a prior fracture in the previous 5 years was a requirement for study entry. Details about bone-fracture events were collected about pre-study fractures in the previous 5 years, and about any fracture events that occurred during the study.

**CRF: CE Example 3 — Bone Fracture Assessment**

| Question | Response Options |
|----------|-----------------|
| Which fracture? | ( ) Pre-study fracture, reference number ___  ( ) On-study fracture, reference number ___ |
| Date of collection | -- / --- / -- |
| Date of fracture | -- / --- / -- |
| How did fracture occur? | ( ) Pathologic  ( ) Fall  ( ) Other trauma  ( ) Unknown |
| What was the location of the fracture? | ___ |
| What was the laterality? | ( ) Left  ( ) Right  ( ) Not applicable |
| Were therapeutic measures required? | ( ) Yes  ( ) No  ( ) Unknown |
| If therapeutic measures were required, select all that apply. | [ ] Casting/immobilization  [ ] Traction  [ ] Surgery |
| Were there any complications of the fracture? | ( ) Yes  ( ) No  ( ) Unknown |
| If there were complications, select all that apply. | [ ] Infection of fracture site  [ ] Improper healing requiring bone reset  [ ] Soft tissue damage, specify location ___ |

The collected data do not meet criteria for representation in FA. Data about the most recent pre-study fracture were represented in the Medical History (MH) domain, and data about fractures during the study were represented in the CE domain.

The supplemental qualifier MHCAUSE or CECAUSE (depending on domain) was used to represent the response to the question, "How did the fracture occur?"

The supplemental qualifier MHCPLIND or CECPLIND (depending on domain) was used to represent the response to the question, "Were there any complications of the fracture?"

The codelist used for AECONTRT (NY) was used for MHCONTRT and CECONTRT.

**Row 1:** The subject had only 1 fracture in the last 5 years. This fracture required treatment (MHCONTRT = "Y").

**Row 2:** This subject had a complication (see supplemental qualifier MHCPLIND in suppmh.xpt dataset), which was represented as a separate medical history event. MHGRPID was used to group this with the fracture for which it was a complication. No separate start date for this complication was collected, so MHSTDTC is blank.

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

**Row 1:** Shows the subject's first on-study fracture. Although it healed normally (as indicated by the lack of complications, supplemental qualifier CECPLIND = "N"), it required additional treatment, as indicated by CECONTRT = "Y".

**Rows 2-3:** Show the subject's second fracture and its associated complication. The 2 events were linked using CEGRPID.

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

**Row 1:** The subject's pre-study fracture required one of the prespecified therapeutic procedures. The sponsor populated PRSPID with the value in MHSPID for the fracture. PRDTC is populated with the date on which medical history was collected, which also appeared in MHDTC.

**Rows 2-3:** The subject's first on-study fracture required 2 of the prespecified therapeutic procedures. For these procedures, PRSPID was populated with a CESPID value. PRDTC is the same as CEDTC for the associated fracture.

**pr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | PRSEQ | PRSPID | PRTRT | PRCAT | PRPRESP | PROCCUR | PRDTC | PRSTDTC |
|-----|---------|--------|---------|-------|--------|-------|-------|---------|---------|-------|---------|
| 1 | ABC | PR | ABC-US-701-002 | 1 | MH1 | Casting/Immobilization | FRACTURE TREATMENTS | Y | Y | 2006-05-13 | |
| 2 | ABC | PR | ABC-US-701-002 | 2 | CE1 | Surgery | FRACTURE TREATMENTS | Y | Y | 2006-07-09 | |
| 3 | ABC | PR | ABC-US-701-002 | 3 | CE1 | Traction | FRACTURE TREATMENTS | Y | Y | 2006-07-09 | |

The therapeutic measures are linked to the fracture events in the RELREC dataset. The sponsor anticipated the need to link procedures either to an MH record or a CE record, so included domain prefixes in the values of MHSPID and CESPID and used those in populating PRSPID.

**Rows 1-2:** Show the dataset-to-dataset relationship between MH and PR records.

**Rows 3-4:** Show the relationship between CE and PR records.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | ABC | MH | | MHSPID | | ONE | 1 |
| 2 | ABC | PR | | PRSPID | | MANY | 1 |
| 3 | ABC | CE | | CESPID | | ONE | 2 |
| 4 | ABC | PR | | PRSPID | | MANY | 2 |
