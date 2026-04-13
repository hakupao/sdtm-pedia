# FT — Examples

CDISC publishes supplements for individual functional tests (at https://www.cdisc.org/standards/foundational/qrs). Additional FT examples can be found in supplements on that webpage.

## Example 1

**6-Minute Walk Test (SIX MINUTE WALK)**

The example represents the distance (in meters) that were walked at each minute of the 6-Minute Walk Test. The assistive device the subject used during the test is represented in the SUPPFT dataset.

**ft.xpt**

| Row | STUDYID | DOMAIN | USUBJID | FTSEQ | FTGRPID | FTTESTCD | FTTEST | FTCAT | FTORRES | FTORRESU | FTSTRESC | FTSTRESN | FTSTRESU | FTBLFL | VISITNUM | FTDTC |
|-----|---------|--------|---------|-------|---------|----------|--------|-------|---------|----------|----------|----------|----------|--------|----------|-------|
| 1 | STUDYX | FT | MS01-01 | 1 | 1 | SIXMW101 | SIXMW1-Distance at 1 Minute | SIX MINUTE WALK | 101 | m | 101 | 101 | m | Y | 1 | 2014-03-10 |
| 2 | STUDYX | FT | MS01-01 | 2 | 1 | SIXMW102 | SIXMW1-Distance at 2 Minutes | SIX MINUTE WALK | 201 | m | 201 | 201 | m | Y | 1 | 2014-03-10 |
| 3 | STUDYX | FT | MS01-01 | 3 | 1 | SIXMW103 | SIXMW1-Distance at 3 Minutes | SIX MINUTE WALK | 299 | m | 299 | 299 | m | Y | 1 | 2014-03-10 |
| 4 | STUDYX | FT | MS01-01 | 4 | 1 | SIXMW104 | SIXMW1-Distance at 4 Minutes | SIX MINUTE WALK | 396 | m | 396 | 396 | m | Y | 1 | 2014-03-10 |
| 5 | STUDYX | FT | MS01-01 | 5 | 1 | SIXMW105 | SIXMW1-Distance at 5 Minutes | SIX MINUTE WALK | 493 | m | 493 | 493 | m | Y | 1 | 2014-03-10 |
| 6 | STUDYX | FT | MS01-01 | 6 | 1 | SIXMW106 | SIXMW1-Distance at 6 Minutes | SIX MINUTE WALK | 597 | m | 597 | 597 | m | | 1 | 2014-03-10 |
