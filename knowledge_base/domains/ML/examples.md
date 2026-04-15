# ML — Examples

## Example 1

This example shows meal data collected in an effort to understand the causes of 2 different kinds of events.

- Data was collected about the last meal before each hypoglycemic event
- Data was collected about the occurrence of prespecified foods prior to a suspected event of drug-induced liver injury (DILI).

**CRF: Meal Log CRF**

Record the last type of meal/food consumption prior to the hypoglycemic event:

| Type | | | If Nutritional Drink, Volume (ounces) | Start Date | Start Time | Event ID |
|------|---|---|---------------------------------------|------------|------------|----------|
| [X] Snack | [ ] Nutritional drink | [ ] Meal | | 2015 Jun 03 | 14:15 | CE001 |
| [ ] Snack | [X] Nutritional drink | [ ] Meal | 8 oz | 2015 Sep 03 | 8:30 | CE002 |
| [ ] Snack | [ ] Nutritional drink | [X] Meal | | 2015 Dec 31 | 19:00 | CE003 |
| Click here to add a row: **ADD ROW** | | | | | | |

**CRF: DILI Meal CRF**

If suspected DILI, did you consume any of the following in the past week?

| Type | Occurrence | | If yes, Date |
|------|------------|---|-------------|
| Wild mushrooms | [X] Yes | [ ] No | 2015 DEC 24 |
| Ackee fruit | [ ] Yes | [X] No | |
| Cycad seeds | [ ] Yes | [X] No | |

Note that in this example MLENDTC is null. Because no end date was collected, the meal was represented as a point-in-time event, as described in Assumption 2b.

**Rows 1-3:** Show the last meal data for 3 hypoglycemic events.

**Rows 4-6:** Show the meal data collected relative to the suspected DILI.

**ml.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MLSEQ | MLTRT | MLCAT | MLPRESP | MLOCCUR | MLDOSE | MLDOSU | MLDTC | MLSTDTC | MLENDTC | MLEVLINT | RELMIDS | MIDS | MIDSDTC |
|-----|---------|--------|---------|-------|-------|-------|---------|---------|--------|--------|-------|---------|---------|----------|---------|------|---------|
| 1 | XYZ | ML | XYZ-001-001 | 1 | SNACK | HYPOGLYCEMIA EVALUATION | Y | Y | | | | 2015-06-03T14:15 | | | LAST MEAL PRIOR TO | HYPO1 | 2015-06-03T19:20 |
| 2 | XYZ | ML | XYZ-001-001 | 2 | NUTRITIONAL DRINK | HYPOGLYCEMIA EVALUATION | Y | Y | 8 | oz | | 2015-09-03T08:30 | | | LAST MEAL PRIOR TO | HYPO2 | 2015-09-03T17:00 |
| 3 | XYZ | ML | XYZ-001-001 | 3 | MEAL | HYPOGLYCEMIA EVALUATION | Y | Y | | | | 2015-12-31T19:00 | | | LAST MEAL PRIOR TO | HYPO3 | 2016-01-01T10:30 |
| 4 | XYZ | ML | XYZ-001-001 | 4 | WILD MUSHROOMS | DILI EVALUATION | Y | Y | | | 2015-12-27 | 2015-12-24 | | -P1W | | | |
| 5 | XYZ | ML | XYZ-001-001 | 5 | ACKEE FRUIT | DILI EVALUATION | Y | N | | | 2015-12-27 | | | -P1W | | | |
| 6 | XYZ | ML | XYZ-001-001 | 6 | CYCAD SEEDS | DILI EVALUATION | Y | N | | | 2015-12-27 | | | -P1W | | | |

## Example 2

This example describes a study that examines the effect of physical modifications in a cafeteria on selection/consumption among school students.

| Group | Arms | Details |
|-------|------|---------|
| 1 | Control | Students received standard meals in a standard cafeteria environment. |
| 2 | Experimental: choice architecture | Students were exposed to modifications to the physical environment in the cafeteria to "nudge" students towards healthier choices. Physical modifications included: placing vegetables at the beginning of the lunch line; placing fruits in attractive bowls, trays lined with appealing fabric, and fruit options next to cash registers; promoting fruits and vegetables with prominently displayed signage and images; placing white milk selection more predominantly than chocolate milk (e.g., white milk displayed in front of chocolate milk). |

Food-card data was collected over a 7-month period by students receiving a school meal 1 day per week. Students who brought a lunch from home or those not eating lunch in the cafeteria on a study day were excluded.

The dataset below shows the food-card data collected for the first 3 weeks for a subject.

**ml.xpt**

| Row | STUDYID | DOMAIN | USUBJID | MLSEQ | MLTRT | VISITNUM | VISIT | MLSTDTC |
|-----|---------|--------|---------|-------|-------|----------|-------|---------|
| 1 | ABC123 | ML | ABC123-001 | 1 | FRUIT ROLLUP | 1 | WEEK 1 | 2015-09-09 |
| 2 | ABC123 | ML | ABC123-001 | 2 | WHITE MILK | 1 | WEEK 1 | 2015-09-09 |
| 3 | ABC123 | ML | ABC123-001 | 3 | PEANUT BUTTER SANDWICH | 1 | WEEK 1 | 2015-09-09 |
| 4 | ABC123 | ML | ABC123-001 | 4 | BANANA | 2 | WEEK 2 | 2015-09-17 |
| 5 | ABC123 | ML | ABC123-001 | 5 | CHOCOLATE MILK | 2 | WEEK 2 | 2015-09-17 |
| 6 | ABC123 | ML | ABC123-001 | 6 | PIZZA | 2 | WEEK 2 | 2015-09-17 |
| 7 | ABC123 | ML | ABC123-001 | 7 | APPLE | 3 | WEEK 3 | 2015-09-22 |
| 8 | ABC123 | ML | ABC123-001 | 8 | WHITE MILK | 3 | WEEK 3 | 2015-09-22 |
| 9 | ABC123 | ML | ABC123-001 | 9 | SALAD | 3 | WEEK 3 | 2015-09-22 |
