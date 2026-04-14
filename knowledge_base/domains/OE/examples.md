# OE — Examples

## Example 1

This example shows a general anterior segment examination performed on each eye at 1 visit, with the purpose of evaluating general abnormalities.

**Rows 1-2:** Represent an overall interpretation (i.e., normal/abnormal) finding from the anterior segment examination, using OETESTCD="INTP". OELOC indicates that the assessor examined the lens and OELAT indicates which lens was examined.
**Row 3:** Represents an abnormality observed during the anterior segment examination of the right eye. OEDIR="MULTIPLE" and indicates multiple directionality values are applicable. OELOC, OELAT, and the multiple OEDIR values specify the location of the abnormality represented in OEORRES and OESTRESC. This observed abnormality (i.e., red spot visible) was determined to be clinically significant (OECLSIG="Y").

**oe.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FOCID | OESEQ | OETESTCD | OETEST | OEORRES | OESTRESC | OELOC | OELAT | OEDIR | OEMETHOD | OEEVAL | OECLSIG | VISITNUM | VISIT | OEDTC |
|-----|---------|--------|---------|-------|-------|----------|--------|---------|----------|-------|-------|-------|----------|--------|---------|----------|-------|-------|
| 1 | XXX | OE | XXX-450-110 | OS | 1 | INTP | Interpretation | NORMAL | NORMAL | LENS | LEFT | | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-03-20 |
| 2 | XXX | OE | XXX-450-110 | OD | 2 | INTP | Interpretation | ABNORMAL | ABNORMAL | LENS | RIGHT | | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-03-20 |
| 3 | XXX | OE | XXX-450-110 | OD | 3 | OEEXAM | Ophthalmic Examination | RED SPOT VISIBLE | RED SPOT VISIBLE | CONJUNCTIVA | RIGHT | MULTIPLE | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR | Y | 1 | SCREENING | 2012-03-20 |

The supplemental qualifier dataset represents the multiple directionality values, further describing the anatomical location where the abnormality was observed.

**suppoe.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|
| 1 | XXX | OE | XXX-450-110 | OESEQ | 3 | OEDIRT | Directionality 1 | SUPERIOR |
| 2 | XXX | OE | XXX-450-110 | OESEQ | 3 | OEDIR2 | Directionality 2 | TEMPORAL |

## Example 2

This example shows:
- Different assessments, from the front to the back of the eye, for 1 subject at 1 visit
- The use of the supplemental qualifier non-standard variable (NSV) OEEDILST (Eye Dilation Status)

The test for iris color is in the OE domain because in this use case, the medication is likely to change the result over the course of the study. Otherwise, iris color should be represented in the Subject Characteristics (SC) domain (see Section 6.3.10, Subject Characteristics).

**Rows 1-2:** Show assessments of the color of the iris (OELOC="IRIS") for the right and left eyes, respectively.
**Rows 3-4:** Show assessments of the status of the lens (OELOC="LENS") for the right and left eyes, respectively. This status assessment is to determine whether the lens of the eye is the natural lens (OEORRES="PHAKIC") or a replacement (OEORRES="PSEUDOPHAKIC").
**Rows 5-6:** Show assessments looking for the presence of hyperemia (increased blood flow). The fact that OELOC="CONJUNCTIVA" even for the left eye, where hyperemia was absent, suggests that this examination was specifically an examination of the conjunctiva. Hyperemia was identified in the right eye and was judged to be clinically significant.
**Rows 7-8:** Show measurements of the cup-to-disc ratio for the right and left eyes, respectively.

**oe.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FOCID | OESEQ | OETESTCD | OETEST | OEORRES | OEORRESU | OESTRESC | OESTRESN | OESTRESU | OELOC | OELAT | OEMETHOD | OEEVAL | OECLSIG | VISITNUM | VISIT | OEDTC |
|-----|---------|--------|---------|-------|-------|----------|--------|---------|----------|----------|----------|----------|-------|-------|----------|--------|---------|----------|-------|-------|
| 1 | XXX | OE | XXX-450-120 | OD | 1 | COLOR | Color | BLUE | | BLUE | | | IRIS | RIGHT | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-04-20 |
| 2 | XXX | OE | XXX-450-120 | OS | 2 | COLOR | Color | BLUE | | BLUE | | | IRIS | LEFT | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-04-20 |
| 3 | XXX | OE | XXX-450-120 | OD | 3 | LENSSTAT | Lens Status | PHAKIC | | PHAKIC | | | LENS | RIGHT | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-04-20 |
| 4 | XXX | OE | XXX-450-120 | OS | 4 | LENSSTAT | Lens Status | PSEUDOPHAKIC | | PSEUDOPHAKIC | | | LENS | LEFT | SLIT LAMP BIOMICROSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-04-20 |
| 5 | XXX | OE | XXX-450-120 | OD | 5 | HYPERMIA | Hyperemia | PRESENT | | PRESENT | | | CONJUNCTIVA | RIGHT | OPHTHALMOSCOPY | INVESTIGATOR | Y | 1 | SCREENING | 2012-04-20 |
| 6 | XXX | OE | XXX-450-120 | OS | 6 | HYPERMIA | Hyperemia | ABSENT | | ABSENT | | | CONJUNCTIVA | LEFT | OPHTHALMOSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-04-20 |
| 7 | XXX | OE | XXX-450-120 | OD | 7 | CUPDISC | Cup-to-Disc Ratio | 0.5 | RATIO | 0.5 | 0.5 | RATIO | OPTIC DISC | RIGHT | OPHTHALMOSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-04-20 |
| 8 | XXX | OE | XXX-450-120 | OS | 8 | CUPDISC | Cup-to-Disc Ratio | 0.6 | RATIO | 0.6 | 0.6 | RATIO | OPTIC DISC | LEFT | OPHTHALMOSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-04-20 |

The suppoe.xpt dataset represents the testing condition (i.e., dilated eyes) qualifying the cup-to-disc ratio tests.

**suppoe.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|
| 1 | XXX | OE | XXX-450-120 | OESEQ | 7 | OEEDILST | Eye Dilation Status | DILATED |
| 2 | XXX | OE | XXX-450-120 | OESEQ | 8 | OEEDILST | Eye Dilation Status | DILATED |

## Example 3

This example shows:
- Partial results of the macula examination performed by the site investigator, as well as results provided by an independent assessor, for 1 visit
- The use of the NSV EVLDTC
- The use of the Procedures (PR) domain to represent the optical coherence tomography (OCT) procedure details, with specific device characteristics in the DI domain
- The relationship between the OE and PR domains in the RELREC dataset

**Rows 1-2:** Represent the assessments performed by the investigator. OECLSIG represents the investigator's assessment of clinical significance. OEDTC represents the ophthalmoscopy exam date.
**Rows 3-6:** Represent the assessments performed by an independent assessor. OEDTC represents the OCT image date.

**oe.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FOCID | OESEQ | OELNKID | OETESTCD | OETEST | OEORRES | OEORRESU | OESTRESC | OESTRESN | OESTRESU | OELOC | OELAT | OEMETHOD | OEEVAL | OECLSIG | VISITNUM | VISIT | OEDTC |
|-----|---------|--------|---------|-------|-------|---------|----------|--------|---------|----------|----------|----------|----------|-------|-------|----------|--------|---------|----------|-------|-------|
| 1 | XYZ | OE | XYZ-100-001 | OS | 1 | | EDEMA | Edema | PRESENT | | PRESENT | | | MACULA | LEFT | OPHTHALMOSCOPY | INVESTIGATOR | N | 1 | SCREENING | 2012-04-25 |
| 2 | XYZ | OE | XYZ-100-001 | OD | 2 | | EDEMA | Edema | ABSENT | | ABSENT | | | MACULA | LEFT | OPHTHALMOSCOPY | INVESTIGATOR | | 1 | SCREENING | 2012-04-25 |
| 3 | XYZ | OE | XYZ-100-001 | OS | 3 | 1 | EDEMA | Edema | PRESENT | | PRESENT | | | MACULA | LEFT | OPTICAL COHERENCE TOMOGRAPHY | INDEPENDENT ASSESSOR | | 1 | SCREENING | 2012-04-25 |
| 4 | XYZ | OE | XYZ-100-001 | OD | 4 | 2 | EDEMA | Edema | ABSENT | | ABSENT | | | MACULA | RIGHT | OPTICAL COHERENCE TOMOGRAPHY | INDEPENDENT ASSESSOR | | 1 | SCREENING | 2012-04-25 |
| 5 | XYZ | OE | XYZ-100-001 | OS | 5 | 1 | THICK | Thickness | 1030 | um | 1030 | 1030 | um | MACULA | LEFT | OPTICAL COHERENCE TOMOGRAPHY | INDEPENDENT ASSESSOR | | 1 | SCREENING | 2012-04-25 |
| 6 | XYZ | OE | XYZ-100-001 | OD | 6 | 2 | THICK | Thickness | 1005 | um | 1005 | 1005 | um | MACULA | RIGHT | OPTICAL COHERENCE TOMOGRAPHY | INDEPENDENT ASSESSOR | | 1 | SCREENING | 2012-04-25 |

The suppoe.xpt dataset represents the date the independent assessor performed the evaluation of the OCT image.

**suppoe.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|
| 1 | XYZ | OE | XYZ-100-001 | OELNKID | 1 | OEEVLDTC | Evaluation Date | 2012-04-30 |
| 2 | XYZ | OE | XYZ-100-001 | OELNKID | 2 | OEEVLDTC | Evaluation Date | 2012-04-30 |

**Rows 1-4:** Represent OCT procedures performed at screening and visit 1 on the right and left eyes. SPDEVID identifies the device used in performing these tests.
**Row 5:** Indicates that an OCT procedure was not performed at visit 2. The reason the procedure was not performed was collected and is represented in PRREASOC.

**pr.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FOCID | SPDEVID | PRSEQ | PRLNKID | PRTRT | PRPRESP | PROCCUR | PRREASOC | PRLOC | PRLAT | PRSTDTC | VISITNUM | VISIT |
|-----|---------|--------|---------|-------|---------|-------|---------|-------|---------|---------|----------|-------|-------|---------|----------|-------|
| 1 | XYZ | PR | XYZ-100-001 | OS | 100 | 1 | 1 | OCT | Y | Y | | EYE | LEFT | 2012-04-25T09:30:00 | 1 | SCREENING |
| 2 | XYZ | PR | XYZ-100-001 | OD | 100 | 2 | 2 | OCT | Y | Y | | EYE | RIGHT | 2012-04-25T10:10:00 | 1 | SCREENING |
| 3 | XYZ | PR | XYZ-100-001 | OS | 100 | 3 | 3 | OCT | Y | Y | | EYE | LEFT | 2012-05-25T08:30:00 | 2 | VISIT 1 |
| 4 | XYZ | PR | XYZ-100-001 | OD | 100 | 4 | 4 | OCT | Y | Y | | EYE | RIGHT | 2012-05-25T08:30:00 | 2 | VISIT 1 |
| 5 | XYZ | PR | XYZ-100-001 | OU | | 5 | | OCT | Y | N | PATIENT WAS SICK FOR SEVERAL WEEKS | | | | 3 | VISIT 2 |

Identifying information for the device with SPDEVID = "100" included in the PR domain is represented in the Device Identifiers (DI) domain.

**di.xpt**

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
|-----|---------|--------|---------|-------|----------|--------|-------|
| 1 | XYZ | DI | 100 | 1 | TYPE | Device Type | OCT |
| 2 | XYZ | DI | 100 | 2 | MANUF | Manufacturer | ZEISS |
| 3 | XYZ | DI | 100 | 3 | MODEL | Model | CIRRUS |
| 4 | XYZ | DI | 100 | 4 | SERIAL | Serial Number | yyyyyy |

The many-to-one relationship between records in the PR and OE domains is described in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | XYZ | PR | | PRLNKID | | ONE | 13 |
| 2 | XYZ | OE | | OELNKID | | MANY | 13 |

## Example 4

This example shows:
- A CRF that collects subject's comfort of a lubricant eye drop for keratoconjunctivitis sicca (dry eye) on a numeric scale (i.e., 1 to 10, with 1 meaning most comfortable and 10 meaning most uncomfortable)
- The use of the NSV OERESCRT, to describe the numeric scale
- A subject who experienced an adverse event on the eye. The FOCID variable is included in the AE domain to allow the grouping of all ophthalmic observations.

**Row 1:** Represents the subject's assessment of ocular comfort in the right eye, upon instillation of a lubricant eye drop for dry eye.
**Row 2:** Represents the subject's assessment of ocular comfort in the right eye, 1 minute post-instillation of a lubricant eye drop for dry eye.
**Row 3:** Represents the subject's assessment of ocular comfort in the left eye, upon instillation of a lubricant eye drop for dry eye.
**Row 4:** Represents the subject's assessment of ocular comfort in the left eye, 1 minute post-instillation of a lubricant eye drop for dry eye.

**oe.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FOCID | OESEQ | OETESTCD | OETEST | OECAT | OEORRES | OESTRESC | OESTRESN | OELOC | OELAT | OEMETHOD | OEEVAL | VISITNUM | VISIT | OEDTC | OETPT | OETPTNUM |
|-----|---------|--------|---------|-------|-------|----------|--------|-------|---------|----------|----------|-------|-------|----------|--------|----------|-------|-------|-------|----------|
| 1 | XYZ | OE | XYZ-100-0001 | OD | 1 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 1 | 1 | 1 | EYE | RIGHT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-02-11T09:00 | UPON INSTILLATION | 1 |
| 2 | XYZ | OE | XYZ-100-0001 | OD | 2 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 10 | 10 | 10 | EYE | RIGHT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-02-11T09:01 | 1 MINUTE POST-INSTILLATION | 2 |
| 3 | XYZ | OE | XYZ-100-0001 | OS | 1 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 1 | 1 | 1 | EYE | LEFT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-05-01T09:00 | UPON INSTILLATION | 1 |
| 4 | XYZ | OE | XYZ-100-0001 | OS | 2 | EYDCOMGR | Eye Drop Comfort Grade | OCULAR COMFORT | 10 | 10 | 10 | EYE | LEFT | VISUAL ANALOG SCALE | STUDY SUBJECT | 1 | VISIT 1 | 2011-05-01T09:01 | 1 MINUTE POST-INSTILLATION | 2 |

The suppoe.xpt dataset represents the scale used for the ocular comfort rating.

**suppoe.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|
| 1 | XYZ | OE | XYZ-100-0001 | OECAT | OCULAR COMFORT | OERESCRT | Rating Scale | 10-point VAS (1=Best, 10=Worst) |
