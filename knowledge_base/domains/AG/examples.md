# AG — Examples

## Example 1

This example captures data about the allergen administered to the subject as part of a bronchial allergen challenge (BAC) test. Prior to the BAC, the subject had a skin-prick allergen test to help identify the allergen to be used for the BAC test. The skin-prick test identified grass as the allergen to be used in the BAC test. Data from the allergen skin test are not shown, but the CRF for the BAC includes collection of the allergen chosen for use in the BAC. A predetermined set of ascending doses of the chosen allergen was used in the screening BAC test. The results of the screening BAC are not shown, but would be represented in the Respiratory System Findings (RE) domain.

**Row 1:** The first dose given in the BAC was saline.

**Rows 2-4:** Three successively higher doses of grass allergen were given.

**ag.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AGSEQ | AGTRT | AGPRESP | AGOCCUR | AGDOSE | AGDOSU | AGROUTE | VISIT | AGENDTC |
|-----|---------|--------|---------|-------|-------|---------|---------|--------|--------|---------|-------|---------|
| 1 | XYZ | AG | XYZ-001-001 | 1 | SALINE | Y | Y | 0 | SQ-u/mL | RESPIRATORY (INHALATION) | SCREENING | 2010-11-07T10:56:00 |
| 2 | XYZ | AG | XYZ-001-001 | 2 | GRASS | Y | Y | 250 | SQ-u/mL | RESPIRATORY (INHALATION) | SCREENING | 2010-11-07T11:19:00 |
| 3 | XYZ | AG | XYZ-001-001 | 3 | GRASS | Y | Y | 1000 | SQ-u/mL | RESPIRATORY (INHALATION) | SCREENING | 2010-11-07T11:43:00 |
| 4 | XYZ | AG | XYZ-001-001 | 4 | GRASS | Y | Y | 2000 | SQ-u/mL | RESPIRATORY (INHALATION) | SCREENING | 2010-11-07T12:06:00 |

## Example 2

In this example, first there was a check that the subject had not taken a short-acting bronchodilator in the previous 4 hours (Concomitant/Prior Medications (CM) domain). Then the procedure agent (AG domain) was given as part of a reversibility assessment. Spirometry measurements (RE domain) were obtained before and after agent administration. An identifier was assigned to the reversibility test and this identifier was used to be link data across the multiple SDTM domains in which the data are represented.

The question as to whether a short-acting bronchodilator was administered in the 4 hours prior to the reversibility assessment is represented in the CM domain because this prior administration would have been for therapeutic effect, not as part of the procedure. The question asked was about the administration of any short-acting bronchodilator, rather than a specific medication, so both CMTRT and CMCAT are populated with "SHORT-ACTING BRONCHODILATOR", which describes a group of medications. The CMSPID value RV1 was used to indicate that this question was associated with the reversibility test.

**cm.xpt**

| Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMSPID | CMTRT | CMCAT | CMPRESP | CMOCCUR | CMEVLINT |
|-----|---------|--------|---------|-------|--------|-------|-------|---------|---------|----------|
| 1 | XYZ | CM | XYZ-001-001 | 1 | RV1 | SHORT-ACTING BRONCHODILATOR | SHORT-ACTING BRONCHODILATOR | Y | N | -PT4H |

The administration of albuterol as part of the reversibility procedure is represented in the AG domain. The AGSPID value RV1 was used to indicate that this administration was associated with the reversibility test.

**ag.xpt**

| Row | STUDYID | DOMAIN | USUBJID | AGSEQ | AGSPID | AGTRT | AGPRESP | AGOCCUR | AGDOSE | AGDOSFRM | AGDOSFRQ | AGROUTE | VISIT | AGSTDTC |
|-----|---------|--------|---------|-------|--------|-------|---------|---------|--------|----------|----------|---------|-------|---------|
| 1 | XYZ | AG | XYZ-001-001 | 1 | RV1 | ALBUTEROL | Y | Y | 2 | PUFF | AEROSOL | ONCE | RESPIRATORY (INHALATION) | VISIT 2 | 2013-06-18T10:05 |

The sponsor populated REGRPID with RV1 to indicate that these pulmonary function tests were associated with the reversibility test. The spirometer used in the testing is identified in SPDEVID. See the SDTM-MD (available at https://www.cdisc.org/standards/foundational/medical-devices-sdtmig/) for information about representing device-related information.

**Row 1:** Shows the results for the pre-bronchodilator FEV1 test performed as part of a reversibility assessment. The timing reference variables RETPT, RETPTNUM, REELTM, RETPTREF, and RERFTDTC show that this test was performed 5 minutes before the bronchodilator challenge.

**Row 2:** Shows the results for FEV1 test performed 20 minutes after the bronchodilator challenge.

**Row 3:** Because the percentage reversibility was collected on the CRF, it is included in the SDTM dataset.

**re.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SPDEVID | RESEQ | REGRPID | RETESTCD | RETEST | REORRES | REORRESU | RESTRESC | RESTRESN | RESTRESU | VISIT | REDTC | RETPT | RETPTNUM | REELTM | RETPTREF | RERFTDTC |
|-----|---------|--------|---------|---------|-------|---------|----------|--------|---------|----------|----------|----------|----------|-------|-------|-------|----------|--------|----------|----------|
| 1 | XYZ | RE | XYZ-001-001 | ABC001 | 1 | RV1 | FEV1 | Forced Expiratory Volume in 1 Second | 2.43 | L | 2.43 | 2.43 | L | VISIT 2 | 2013-06-18T10:00 | PRE-BRONCHODILATOR ADMINISTRATION | 1 | -PT5M | BRONCHODILATOR ADMINISTRATION | 2013-06-18T10:05 |
| 2 | XYZ | RE | XYZ-001-001 | ABC001 | 2 | RV1 | FEV1 | Forced Expiratory Volume in 1 Second | 2.77 | L | 2.77 | 2.77 | L | VISIT 2 | 2013-06-18T10:00 | POST-BRONCHODILATOR ADMINISTRATION | 2 | PT20M | BRONCHODILATOR ADMINISTRATION | 2013-06-18T10:05 |
| 3 | XYZ | RE | XYZ-001-001 | ABC001 | 3 | RV1 | PTCREV | Percentage Reversibility | 13.99 | % | 13.99 | 13.99 | % | VISIT 2 | 2013-06-18T10:00 | | | | BRONCHODILATOR ADMINISTRATION | 2013-06-18T10:05 |

The identifier for the device used in the test was established in the Device Identifier (DI) domain.

**di.xpt**

| Row | STUDYID | DOMAIN | SPDEVID | DISEQ | DIPARMCD | DIPARM | DIVAL |
|-----|---------|--------|---------|-------|----------|--------|-------|
| 1 | XYZ | DI | ABC001 | 1 | TYPE | Device Type | SPIROMETER |

The relationship of the test agent to the spirometry measurements obtained before and after its administration and to the prior occurrence of short acting bronchodilator administration is recorded by means of a relationship in RELREC.

**relrec.xpt**

| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
|-----|---------|---------|---------|-------|----------|---------|-------|
| 1 | XYZ | AG | XYZ-001-001 | AGSPID | RV1 | | 1 |
| 2 | XYZ | RE | XYZ-001-001 | REGRPID | RV1 | | 1 |
| 3 | XYZ | CM | XYZ-001-001 | CMSPID | RV1 | | 1 |
