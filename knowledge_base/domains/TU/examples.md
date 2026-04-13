# TU — Examples

Note: TU and TR share examples. See also [TR Examples](../TR/examples.md).

## Example 1

This is an example of using the TU domain to represent non-cancerous lesions identified in the heart.

Subject 40913 had a peripheral vascular intervention (PVI) procedure on February 1, 2007. A target lesion (L01) was identified in the infrarenal aorta within the aorto-iliac vessel (L01-1). During the same PVI procedure, the subject also had a target graft lesion (L01-G) identified in the left femoro-popliteal graft (L01-G1). The lesion location was noted within the graft anastomosis proximal, the type was a synthetic graft composed of Gore-Tex, and the anastomosis was in the left popliteal artery.

**Rows 1-2:** Show the target lesion located in the infrarenal aorta and within the aorto-iliac vessel.

**Row 3:** Shows the PVI target limb in which the graft lesion is located identified by the investigator.

**Rows 4-5:** Show the target graft lesion located in the left femoro-popliteal graft and within the femoro-popliteal vessel.

**tu.xpt**

| Row | STUDYID | DOMAIN | USUBJID | TUSEQ | TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTRESC | TULOC | TULAT | TUMETHOD | TUEVAL | VISITNUM | VISIT | TUDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|---------|----------|-------|-------|----------|--------|----------|-------|-------|
| 1 | STUDY01 | TU | 40913 | 1 | L01 | LESIDENT | Lesion Identification | TARGET | TARGET | INFRARENAL AORTA | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
| 2 | STUDY01 | TU | 40913 | 2 | L01-1 | VSIDENT | Vessel Lesion Identification | TARGET | TARGET | AORTO-ILIAC PERIPHERAL ARTERY | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
| 3 | STUDY01 | TU | 40913 | 3 | L01-2 | LMLIDENT | Limb Location Identification | TARGET | TARGET | LEG | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
| 4 | STUDY01 | TU | 40913 | 4 | L01-G | GRLIDENT | Graft Lesion Identification | TARGET | TARGET | FEMORO-POPLITEAL PERIPHERAL ARTERY | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |
| 5 | STUDY01 | TU | 40913 | 5 | L01-G1 | VSIDENT | Vessel Lesion Identification | TARGET | TARGET | FEMORO-POPLITEAL PERIPHERAL ARTERY | LEFT | ANGIOGRAPHY | INVESTIGATOR | 1 | SCREEN | 2007-02-01 |

Additional information about the lesion (e.g., lesion location within the graft, graft anastomosis) as well as details regarding the graft type and material are given using supplemental qualifiers.

**supptu.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL | QORIG | QEVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|-------|-------|
| 1 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUPAGLL | Peripheral Graft Lesion Location | GRAFT ANASTOMOSIS PROXIMAL | CRF | |
| 2 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUPAGAR | Peripheral Artery Graft Anastomosis | LEFT POPLITEAL ARTERY | CRF | |
| 3 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUOTHLDS | Other Lesion Description | LESION IS 5MM FROM THE ORIGIN OF THE GRAFT | CRF | |
| 4 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUPAGT | Peripheral Artery Graft Type | SYNTHETIC GRAFT | CRF | |
| 5 | STUDY01 | TU | 40913 | TUSEQ | 4 | TUPAGSM | Peripheral Artery Graft Synthetic Material | GORE-TEX | CRF | |

## Example 2

This is an example of tumors identified and tracked using RECIST 1.1 criteria.

TU shows the target and non-target tumors identified by an investigator at a screening visit and also shows that the investigator determined at the week 6 visit that 1 of the previously identified tumors had split.

**Rows 1-6:** Show for subject 44444 the target and non-target tumors identified by the investigator at the screening visit.

**Rows 7-8:** Show the investigator determined that a tumor (TULNKID = "T04" at screening) had split into 2 separate tumors at the week 6 visit. The 2 distinct pieces of the original tumor were then tracked independently from that point in the study forward.

**tu.xpt**

| Row | STUDYID | DOMAIN | USUBJID | TUSEQ | TUGRPID | TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTRESC | TULOC | TULAT | TUMETHOD | TUEVAL | VISITNUM | VISIT | TUDTC | TUDY |
|-----|---------|--------|---------|-------|---------|---------|----------|--------|---------|----------|-------|-------|----------|--------|----------|-------|-------|------|
| 1 | ABC | TU | 44444 | 1 | | T01 | TUMIDENT | Tumor Identification | TARGET | TARGET | LIVER | | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 2 | ABC | TU | 44444 | 2 | | T02 | TUMIDENT | Tumor Identification | TARGET | TARGET | KIDNEY | RIGHT | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 3 | ABC | TU | 44444 | 3 | | T03 | TUMIDENT | Tumor Identification | TARGET | TARGET | CERVICAL LYMPH NODE | LEFT | MRI | INVESTIGATOR | 10 | SCREEN | 2010-01-02 | -2 |
| 4 | ABC | TU | 44444 | 4 | | T04 | TUMIDENT | Tumor Identification | TARGET | TARGET | SKIN OF THE TRUNK | | PHOTOGRAPHY | INVESTIGATOR | 10 | SCREEN | 2010-01-03 | -1 |
| 5 | ABC | TU | 44444 | 5 | | NT01 | TUMIDENT | Tumor Identification | NON-TARGET | NON-TARGET | THYROID GLAND | RIGHT | CT SCAN | INVESTIGATOR | 10 | SCREEN | 2010-01-01 | -3 |
| 6 | ABC | TU | 44444 | 6 | | NT02 | TUMIDENT | Tumor Identification | NON-TARGET | NON-TARGET | CEREBELLUM | RIGHT | MRI | INVESTIGATOR | 10 | SCREEN | 2010-01-02 | -2 |
| 7 | ABC | TU | 44444 | 7 | T04 | T04.1 | TUSPLIT | Tumor Split | TARGET | TARGET | SKIN OF THE TRUNK | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |
| 8 | ABC | TU | 44444 | 8 | T04 | T04.2 | TUSPLIT | Tumor Split | TARGET | TARGET | SKIN OF THE TRUNK | | PHOTOGRAPHY | INVESTIGATOR | 40 | WEEK 6 | 2010-02-20 | 48 |

The supplemental qualifier dataset below shows that "T01", "T02", and "T04" were not previously irradiated and "T03" was previously irradiated with subsequent progression after irradiation.

**supptu.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | QNAM | QLABEL | QVAL |
|-----|---------|---------|---------|-------|----------|------|--------|------|
| 1 | ABC | TU | 44444 | TULNKID | T01 | TUPREVIR | Previously Irradiated | N |
| 2 | ABC | TU | 44444 | TULNKID | T02 | TUPREVIR | Previously Irradiated | N |
| 3 | ABC | TU | 44444 | TULNKID | T03 | TUPREVIR | Previously Irradiated | Y |
| 4 | ABC | TU | 44444 | TULNKID | T03 | TUPREISP | Irradiated then Subsequent Progression | Y |
| 5 | ABC | TU | 44444 | TULNKID | T04 | TUPREVIR | Previously Irradiated | N |

## Example 3

This is an example of tumors identified and tracked following RECIST 1.1 criteria, with an additional opinion provided by an independent assessor.

TU shows the target and non-target tumors identified by a radiologist at a screening visit. It also shows that the radiologist identified 2 new tumors: 1 at the week 6 visit and 1 at the week 12 visit.

**Rows 1-5:** Show the target and non-target tumors identified at screening by the independent assessor, Radiologist 1.

**Row 6:** Shows that a new tumor was identified at week 6 by the independent assessor, Radiologist 1.

**Row 7:** Shows that another new tumor was identified at week 12 by the independent assessor, Radiologist 1.

**tu.xpt**

| Row | STUDYID | DOMAIN | USUBJID | TUSEQ | TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTRESC | TULOC | TULAT | TUMETHOD | TUNAM | TUEVAL | TUEVALID | VISITNUM | VISIT | TUDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|---------|----------|-------|-------|----------|-------|--------|----------|----------|-------|-------|
| 1 | ABC | TU | 55555 | 1 | R1-T01 | TUMIDENT | Tumor Identification | TARGET | TARGET | CERVICAL LYMPH NODE | LEFT | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-02 |
| 2 | ABC | TU | 55555 | 2 | R1-T02 | TUMIDENT | Tumor Identification | TARGET | TARGET | LIVER | | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 |
| 3 | ABC | TU | 55555 | 3 | R1-T03 | TUMIDENT | Tumor Identification | TARGET | TARGET | THYROID GLAND | RIGHT | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 |
| 4 | ABC | TU | 55555 | 4 | R1-NT01 | TUMIDENT | Tumor Identification | NON-TARGET | NON-TARGET | KIDNEY | RIGHT | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-01 | 
| 5 | ABC | TU | 55555 | 5 | R1-NT02 | TUMIDENT | Tumor Identification | NON-TARGET | NON-TARGET | CEREBELLUM | LEFT | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 10 | SCREEN | 2010-01-02 |
| 6 | ABC | TU | 55555 | 6 | R1-NEW01 | TUMIDENT | Tumor Identification | NEW | NEW | LUNG | | CT SCAN | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 40 | WEEK 6 | 2010-02-20 |
| 7 | ABC | TU | 55555 | 7 | R1-NEW02 | TUMIDENT | Tumor Identification | NEW | NEW | CEREBELLUM | LEFT | MRI | ACE IMAGING | INDEPENDENT ASSESSOR | RADIOLOGIST 1 | 60 | WEEK 12 | 2010-04-02 |
