# CO — Examples

## Example 1

**Row 1:** Shows a comment collected on a separate comments page. Since it was unrelated to any specific domain or record, RDOMAIN, IDVAR, and IDVARVAL are null.

**Row 2:** Shows a comment that was collected on the bottom of the PE page for Visit 7, without any indication of specific records it applied to. Since the comment related to a specific domain, RDOMAIN is populated. Since it was related to a specific visit, VISIT, COREF is "VISIT 7". However, since it does not relate to a specific record, IDVAR and IDVARVAL are null.

**Row 3:** Shows a comment related to a single AE record having its AESEQ=7.

**Row 4:** Shows a comment related to multiple EX records with EXGRPID = "COMBO1".

**Row 5:** Shows a comment related to multiple VS records with VSGRPID = "VS2".

**Row 6:** Shows one option for representing a comment collected on a visit-specific comments page not associated with a particular domain. In this case, the comment is linked to the Subject Visit record in SV (RDOMAIN = "SV") and IDVAR and IDVARVAL are populated link the comment to the particular visit.

**Row 7:** Shows a second option for representing a comment associated only with a visit. In this case, COREF is used to show that the comment is related to the particular visit.

**Row 8:** Shows a third option for representing a comment associated only with a visit. In this case, the VISITNUM variable was populated to indicate that the comment was associated with a particular visit.

**co.xpt**

| Row | STUDYID | DOMAIN | RDOMAIN | USUBJID | COSEQ | IDVAR | IDVARVAL | COREF | COVAL | COVAL1 | COVAL2 | COEVAL | VISITNUM | CODTC |
|-----|---------|--------|---------|---------|-------|-------|----------|-------|-------|--------|--------|--------|----------|-------|
| 1 | 1234 | CO | | AB-99 | 1 | | | | Comment text | | | PRINCIPAL INVESTIGATOR | | 2003-11-08 |
| 2 | 1234 | CO | PE | AB-99 | 2 | | | VISIT 7 | Comment text | | | PRINCIPAL INVESTIGATOR | | 2004-01-14 |
| 3 | 1234 | CO | AE | AB-99 | 3 | AESEQ | 7 | PAGE 650 | First 200 characters | Next 200 characters | Remaining text | PRINCIPAL INVESTIGATOR | | |
| 4 | 1234 | CO | EX | AB-99 | 4 | EXGRPID | COMBO1 | PAGE 320-355 | First 200 characters | | Remaining text | PRINCIPAL INVESTIGATOR | | |
| 5 | 1234 | CO | VS | AB-99 | 5 | VSGRPID | VS2 | | Comment text | | | PRINCIPAL INVESTIGATOR | | |
| 6 | 1234 | CO | SV | AB-99 | 6 | VISITNUM | 4 | | Comment Text | | | PRINCIPAL INVESTIGATOR | | |
| 7 | 1234 | CO | | AB-99 | 7 | | | VISIT 4 | Comment Text | | | PRINCIPAL INVESTIGATOR | | |
| 8 | 1234 | CO | | AB-99 | 8 | | | | Comment Text | | | PRINCIPAL INVESTIGATOR | 4 | |
