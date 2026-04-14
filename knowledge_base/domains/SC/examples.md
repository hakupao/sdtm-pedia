# SC — Examples

## Example 1

This example shows data collected once per subject that does not fit into the Demographics (DM) domain. For this example, national origin and marital status were collected.

**sc.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SCSEQ | SCTESTCD | SCTEST | SCORRES | SCSTRESC | SCDTC |
|-----|---------|--------|---------|-------|----------|--------|---------|----------|-------|
| 1 | ABC | SC | ABC-001-001 | 1 | NATORIG | National Origin | UNITED STATES | USA | 1999-06-19 |
| 2 | ABC | SC | ABC-001-001 | 2 | MARISTAT | Marital Status | DIVORCED | DIVORCED | 1999-06-19 |
| 3 | ABC | SC | ABC-001-002 | 1 | NATORIG | National Origin | CANADA | CAN | 1999-03-19 |
| 4 | ABC | SC | ABC-001-002 | 2 | MARISTAT | Marital Status | MARRIED | MARRIED | 1999-03-19 |
| 5 | ABC | SC | ABC-001-003 | 1 | NATORIG | National Origin | USA | USA | 1999-05-03 |
| 6 | ABC | SC | ABC-001-003 | 2 | MARISTAT | Marital Status | NEVER MARRIED | NEVER MARRIED | 1999-05-03 |
| 7 | ABC | SC | ABC-001-201 | 1 | NATORIG | National Origin | JAPAN | JPN | 1999-06-14 |
| 8 | ABC | SC | ABC-002-001 | 2 | MARISTAT | Marital Status | WIDOWED | WIDOWED | 1999-06-14 |

## Example 2

In this example, only infants were study subjects. However, with the possible exception of USUBJID values, the example would be unchanged for a study in which mothers were study subjects. If these data were collected for an infant who was an associated person, they would be represented in the APSC domain and the dataset would include APID, RSUBJID, and SREL, rather than USUBJID.

Although there is a test for gestational age in the CDISC Controlled Terminology for Reproductive Findings, gestational age is an attribute of the fetus or infant, and is not a finding about their reproductive system; in this example, gestational age is represented in the Subject Characteristics (SC) domain. The structure of the SC domain formerly was 1 record per characteristic (test) per subject, but with this version of the SDTMIG the structure has changed to allow multiple records per test. This example shows multiple estimates of gestational age for the same subject. Not all of the values of METHOD shown in this example are currently in the METHOD codelist.

Gestational age is often expressed (and sometimes collected) in weeks and days. SDTM does not support the recording of an individual finding result with mixed units (e.g., "20 weeks and 5 days"), so the gestational age would be converted to days for representation in SDTM.

**sc.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SCSEQ | SCTESTCD | SCTEST | SCCAT | SCORRES | SCORESU | SCSTRESC | SCSTRESN | SCSTRESU | SCMETHOD | VISITNUM | SCDTC | SCDY |
|-----|---------|--------|---------|-------|----------|--------|-------|---------|---------|----------|----------|----------|----------|----------|-------|------|
| 1 | ABC-123 | SC | 101 | 1 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 100 | DAYS | 100 | 100 | DAYS | MENSTRUAL HISTORY | 10 | 2017-03-02 | 196 |
| 2 | ABC-123 | SC | 101 | 2 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 135 | DAYS | 135 | 135 | DAYS | ULTRASOUND | 11 | 2017-04-01 | 226 |
| 3 | ABC-123 | SC | 101 | 3 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 265 | DAYS | 265 | 265 | DAYS | BALLARD | 13.1 | 2017-06-10 | 297 |

## Example 3

This example shows data from a multi-year study in which marital status and whether the subject was a student were collected annually.

**sc.xpt**

| Row | STUDYID | DOMAIN | USUBJID | SCSEQ | SCTESTCD | SCTEST | SCORRES | SCSTRESC | SCDTC | SCDY |
|-----|---------|--------|---------|-------|----------|--------|---------|----------|-------|------|
| 1 | ABC123 | SC | 305 | 1 | MARISTAT | Marital Status | NEVER MARRIED | NEVER MARRIED | 2012-01-14 | -2 |
| 2 | ABC123 | SC | 305 | 2 | STDNTIND | Student Indicator | Y | Y | 2012-01-14 | -2 |
| 3 | ABC123 | SC | 305 | 3 | MARISTAT | Marital Status | DOMESTIC PARTNER | DOMESTIC PARTNER | 2013-01-22 | 374 |
| 4 | ABC123 | SC | 305 | 4 | STDNTIND | Student Indicator | Y | Y | 2013-01-22 | 374 |
| 5 | ABC123 | SC | 305 | 5 | MARISTAT | Marital Status | MARRIED | MARRIED | 2014-01-16 | 734 |
| 6 | ABC123 | SC | 305 | 6 | STDNTIND | Student Indicator | N | N | 2014-01-16 | 734 |
