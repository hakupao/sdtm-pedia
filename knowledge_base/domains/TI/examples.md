# TI — Examples

## Example 1

This example shows records for a trial with 2 versions of inclusion/exclusion criteria.

**Rows 1-3:** Show the 2 inclusion criteria and 1 exclusion criterion for version 1 of the protocol.

**Rows 4-6:** Show the inclusion/exclusion criteria for version 2.2 of the protocol, which changed the minimum age for entry from 21 to 18.

**ti.xpt**

| Row | STUDYID | DOMAIN | IETESTCD | IETEST | IECAT | TIVERS |
|-----|---------|--------|----------|--------|-------|--------|
| 1 | XYZ | TI | INCL01 | Has disease under study | INCLUSION | 1 |
| 2 | XYZ | TI | INCL02 | Age 21 or greater | INCLUSION | 1 |
| 3 | XYZ | TI | EXCL01 | Pregnant or lactating | EXCLUSION | 1 |
| 4 | XYZ | TI | INCL01 | Has disease under study | INCLUSION | 2.2 |
| 5 | XYZ | TI | INCL02A | Age 18 or greater | INCLUSION | 2.2 |
| 6 | XYZ | TI | EXCL01 | Pregnant or lactating | EXCLUSION | 2.2 |
