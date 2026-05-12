# SS — Examples

##### Example 1

In this example, subjects complete a 10-week treatment regimen and are then contacted by phone every month for 3 months. The phone contact assesses the subject's survival status. If the survival status is "DEAD", additional information is collected in order to complete the subject's final disposition record in DS and to record the date of death in DM (DS and DM records are not shown here).

| Row | STUDYID | DOMAIN | USUBJID | SSSEQ | SSTESTCD | SSTEST | SSORRES | SSSTRESC | VISITNUM | VISIT | SSDTC |
|-----|---------|--------|---------|-------|----------|--------|---------|----------|----------|-------|-------|
| 1 | XYZ | SS | XYZ-333-009 | 1 | SURVSTAT | Survival Status | ALIVE | ALIVE | 10 | MONTH 1 | 2010-04-15 |
| 2 | XYZ | SS | XYZ-333-009 | 2 | SURVSTAT | Survival Status | ALIVE | ALIVE | 20 | MONTH 2 | 2010-05-12 |
| 3 | XYZ | SS | XYZ-333-009 | 3 | SURVSTAT | Survival Status | ALIVE | ALIVE | 30 | MONTH 3 | 2010-06-15 |
| 4 | XYZ | SS | XYZ-428-021 | 1 | SURVSTAT | Survival Status | ALIVE | ALIVE | 10 | MONTH 1 | 2010-08-03 |
| 5 | XYZ | SS | XYZ-428-021 | 2 | SURVSTAT | Survival Status | DEAD | DEAD | 20 | MONTH 2 | 2010-09-06 |
