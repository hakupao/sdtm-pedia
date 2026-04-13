# Pharmacokinetics Codelists (Part 1)

> Codelists in this file: 2

## PK Analytical Method (C172330)

Extensible: Yes

| Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |
|------|----------------------|-------------------|------------------|
| C172579 | LIN-LOG TRAPEZOIDAL METHOD | Linear-Logarithmic Trapezoidal Method | An AUC calculation method that utilizes the linear trapezoidal interpolation rule up to the maximum concentration (Cmax) and Logarithmic trapezoidal interpolation for the remainder of the concentration curve. |
| C172582 | LINEAR TRAPEZOIDAL - LOG INTERPOLATION METHOD | Linear Trapezoidal - Logarithmic Interpolation Method | An AUC calculation method that utilizes the linear trapezoidal interpolation rule for the entire concentration curve, except when partial areas are selected with no measured endpoint, then logarithmic interpolation is used to calculate the missing data. |
| C172580 | LINEAR TRAPEZOIDAL METHOD |  | An AUC calculation method that utilizes the linear trapezoidal interpolation rule for the entire concentration curve. |
| C172581 | LINEAR UP LOG DOWN METHOD |  | An AUC calculation method that utilizes linear trapezoidal interpolation between two points any time the measured concentration increases and logarithmic trapezoidal interpolation between two points any time the concentration decreases over the entire concentration curve. |

## PK Parameters (C85493)

Extensible: Yes

| Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |
|------|----------------------|-------------------|------------------|
| C154838 | Absolute Bioavailability | Absolute Bioavailability | The fraction of the treatment dose that reaches the systemic circulation; this is the ratio of the amount of drug in the system (area under the curve) after extravascular administration of a test formulation divided by the drug in the system (area under the curve) after IV administration. |
| C170611 | Accum Ratio AUC Infinity Obs | Accum Ratio AUC Infinity Obs | The area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration divided by the area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration during the initial dosing interval. |
| C170612 | Accum Ratio AUC Infinity Pred | Accum Ratio AUC Infinity Pred | The area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration divided by the area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration during the initial dosing interval. |
| C132436 | Accum Ratio AUC T1 to T2 norm by dose | Accum Ratio AUC T1 to T2 norm by dose | The area under the curve from T1 to T2 at steady state divided by the area under the curve from T1 to T2 during the initial dosing interval, each divided by the associated dose. |
| C139129 | Accum Ratio AUC to Last Nonzero Conc | Accum Ratio AUC to Last Nonzero Conc | The area under the curve (AUC) from the time of dosing to the last measurable concentration divided by the area under the curve from the time of dosing to the last measurable concentration during the initial dosing interval. |
| C170613 | Accum Ratio AUCIFO Norm by Dose | Accum Ratio AUCIFO Norm by Dose | The area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration divided by the area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration during the initial dosing interval, each divided by the associated dose. |
| C170614 | Accum Ratio AUCIFP Norm by Dose | Accum Ratio AUCIFP Norm by Dose | The area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration divided by the area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration during the initial dosing interval, each divided by the associated dose. |
| C132435 | Accum Ratio AUCTAU norm by dose | Accum Ratio AUCTAU norm by dose | The area under the curve (AUCTAU) at steady state divided by the area under the curve (AUCTAU) over the initial dosing interval, each divided by the associated dose. |
| C132437 | Accum Ratio Cmax norm by dose | Accum Ratio Cmax norm by dose | The maximum concentration at steady state divided by the maximum concentration during the initial dosing interval, each divided by the associated dose. |
| C132438 | Accum Ratio Cmin norm by dose | Accum Ratio Cmin norm by dose | The minimum concentration at steady state divided by the minimum concentration during the initial dosing interval, each divided by the associated dose. |
| C132439 | Accum Ratio Ctrough norm by dose | Accum Ratio Ctrough norm by dose | The trough concentration at steady state divided by the trough concentration during the initial dosing interval, each divided by the associated dose. |
| C114234 | Accumulation Index using Lambda z | Accumulation Index using Lambda z | Predicted accumulation ratio for area under the curve (AUC) calculated using the Lambda z estimated from single dose data. |
| C122329 | Accumulation Ratio AUC from T1 to T2 | Accumulation Ratio AUC from T1 to T2 | The area under the curve from T1 to T2 at steady state divided by the area under the curve from T1 to T2 during the initial dosing interval. |
| C102356 | Accumulation Ratio AUCTAU | Accumulation Ratio AUCTAU | The area under the curve over the dosing interval at steady state divided by the area under the curve over the initial dosing interval. |
| C102357 | Accumulation Ratio Cmax | Accumulation Ratio Cmax | The maximum concentration at steady state divided by the maximum concentration during the initial dosing interval. |
| C102358 | Accumulation Ratio Cmin | Accumulation Ratio Cmin | The minimum concentration at steady state divided by the minimum concentration during the initial dosing interval. |
| C102426 | Accumulation Ratio Ctrough | Accumulation Ratio Ctrough | The trough concentration at steady state divided by the trough concentration during the initial dosing interval. |
| C181513 | Amt of Analyte at Steady State | Amt of Analyte at Steady State | The amount of analyte in the body at steady state. |
| C181514 | Amt of Analyte at Time T | Amt of Analyte at Time T | The amount of analyte in the body at any time t. |
| C102360 | Amt Rec from T1 to T2 Norm by BMI | Amt Rec from T1 to T2 Norm by BMI | The cumulative amount recovered from the specimen type specified in PPSPEC over the interval from T1 to T2 divided by body mass index. |
| C102361 | Amt Rec from T1 to T2 Norm by SA | Amt Rec from T1 to T2 Norm by SA | The cumulative amount recovered from the specimen type specified in PPSPEC over the interval from T1 to T2 divided by surface area. |
| C102362 | Amt Rec from T1 to T2 Norm by WT | Amt Rec from T1 to T2 Norm by WT | The cumulative amount recovered from the specimen type specified in PPSPEC over the interval from T1 to T2 divided by weight. |
| C102359 | Amt Rec from T1 to T2 | Amt Rec from T1 to T2 | The cumulative amount recovered from the specimen type specified in PPSPEC over the interval from T1 to T2. |
| C112223 | Amt Rec Infinity Obs Norm by BMI | Amt Rec Infinity Obs Norm by BMI | The cumulative amount recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the body mass index. |
| C112224 | Amt Rec Infinity Obs Norm by SA | Amt Rec Infinity Obs Norm by SA | The cumulative amount recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the surface area. |
| C112225 | Amt Rec Infinity Obs Norm by WT | Amt Rec Infinity Obs Norm by WT | The cumulative amount recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the weight. |
| C112032 | Amt Rec Infinity Obs | Amt Rec Infinity Obs | The cumulative amount recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the observed value of the last non-zero concentration. |
| C112226 | Amt Rec Infinity Pred Norm by BMI | Amt Rec Infinity Pred Norm by BMI | The cumulative amount recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the body mass index. |
| C112227 | Amt Rec Infinity Pred Norm by SA | Amt Rec Infinity Pred Norm by SA | The cumulative amount recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the surface area. |
| C112228 | Amt Rec Infinity Pred Norm by WT | Amt Rec Infinity Pred Norm by WT | The cumulative amount recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the weight. |
| C112033 | Amt Rec Infinity Pred | Amt Rec Infinity Pred | The cumulative amount recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the predicted value of the last non-zero concentration. |
| C102364 | Amt Rec Over Dosing Interval Norm by BMI | Amt Rec Over Dosing Interval Norm by BMI | The cumulative amount recovered from the specimen type specified in PPSPEC between doses (TAU) divided by body mass index. |
| C102365 | Amt Rec Over Dosing Interval Norm by SA | Amt Rec Over Dosing Interval Norm by SA | The cumulative amount recovered from the specimen type specified in PPSPEC between doses (TAU) divided by surface area. |
| C102366 | Amt Rec Over Dosing Interval Norm by WT | Amt Rec Over Dosing Interval Norm by WT | The cumulative amount recovered from the specimen type specified in PPSPEC between doses (TAU) divided by weight. |
| C102363 | Amt Rec Over Dosing Interval | Amt Rec Over Dosing Interval | The cumulative amount recovered from the specimen type specified in PPSPEC between doses (TAU). |
| C174346 | Amt Rec to Last Nonzero Conc | Amt Rec to Last Nonzero Conc | The cumulative amount recovered from the specimen type specified in PPSPEC, from the time of dosing to the last non-zero concentration. |
| C154844 | Apparent CL for Unbound Drug | Apparent CL for Unbound Drug | The total apparent clearance of the unbound fraction of drug, adjusted for bioavailability. |
| C85763 | AUC %Back Extrapolation Obs | AUC %Back Extrapolation Obs | Applies only for intravascular bolus dosing. The area under the curve (AUC) from the first measured concentration value back extrapolated to the concentration value at time zero as a percentage of the area under the curve extrapolated to infinity using the observed value of the last non-zero concentration. |
| C85787 | AUC %Back Extrapolation Pred | AUC %Back Extrapolation Pred | Applies only for intravascular bolus dosing. The area under the curve (AUC) from the first measured concentration value back extrapolated to the concentration value at time zero as a percentage of the area under the curve extrapolated to infinity using the predicted value of the last non-zero concentration. |
| C85764 | AUC %Extrapolation Obs | AUC %Extrapolation Obs | The area under the curve (AUC) from the last observed non-zero concentration value to infinity as a percentage of the area under the curve extrapolated to infinity. |
| C85788 | AUC %Extrapolation Pred | AUC %Extrapolation Pred | The area under the curve (AUC) from the last predicted non-zero concentration value to infinity as a percentage of the area under the curve extrapolated to infinity. |
| C92362 | AUC All Norm by BMI | AUC All Norm by BMI | The area under the curve (AUC) from the time of dosing to the time of the last observation divided by the body mass index, regardless of whether the last concentration is measurable or not. |
| C92306 | AUC All Norm by Dose | AUC All Norm by Dose | The area under the curve (AUC) from the time of dosing to the time of the last observation divided by the dose, regardless of whether the last concentration is measurable or not. |
| C92307 | AUC All Norm by SA | AUC All Norm by SA | The area under the curve (AUC) from the time of dosing to the time of the last observation divided by the surface area, regardless of whether the last concentration is measurable or not. |
| C92308 | AUC All Norm by WT | AUC All Norm by WT | The area under the curve (AUC) from the time of dosing to the time of the last observation divided by the weight, regardless of whether the last concentration is measurable or not. |
| C85564 | AUC All | AUC All | The area under the curve (AUC) from the time of dosing to the time of the last observation, regardless of whether the last concentration is measurable or not. |
| C92312 | AUC from T1 to T2 Norm by BMI | AUC from T1 to T2 Norm by BMI | The area under the curve (AUC) over the interval from T1 to T2 divided by the body mass index. |
| C92313 | AUC from T1 to T2 Norm by Dose | AUC from T1 to T2 Norm by Dose | The area under the curve (AUC) over the interval from T1 to T2 divided by the dose. |
| C92314 | AUC from T1 to T2 Norm by SA | AUC from T1 to T2 Norm by SA | The area under the curve (AUC) over the interval from T1 to T2 divided by the surface area. |
| C92315 | AUC from T1 to T2 Norm by WT | AUC from T1 to T2 Norm by WT | The area under the curve (AUC) over the interval from T1 to T2 divided by the weight. |
| C85566 | AUC from T1 to T2 | AUC from T1 to T2 | The area under the curve (AUC) over the interval from T1 to T2. |
| C161413 | AUC Infinity Obs LN Transformed | AUC Infinity Obs LN Transformed | The natural log transformed area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration. |
| C92316 | AUC Infinity Obs Norm by BMI | AUC Infinity Obs Norm by BMI | The area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the body mass index. |
| C96695 | AUC Infinity Obs Norm by Dose | AUC Infinity Obs Norm by Dose | The area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the dose. |
| C174345 | AUC Infinity Obs Norm by Dose/WT | AUC Infinity Obs Norm by Dose/WT | The area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration divided by the body weight-adjusted dose. |
| C92317 | AUC Infinity Obs Norm by SA | AUC Infinity Obs Norm by SA | The area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the surface area. |
| C92318 | AUC Infinity Obs Norm by WT | AUC Infinity Obs Norm by WT | The area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the weight. |
| C85761 | AUC Infinity Obs | AUC Infinity Obs | The area under the curve (AUC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration. |
| C154845 | AUC Infinity Obs, Unbound Drug | AUC Infinity Obs, Unbound Drug | The portion of observed AUC to infinity, represented by the unbound fraction of drug. |
| C92319 | AUC Infinity Pred Norm by BMI | AUC Infinity Pred Norm by BMI | The area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the body mass index. |
| C85786 | AUC Infinity Pred Norm by Dose | AUC Infinity Pred Norm by Dose | The area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the dose. |
| C92320 | AUC Infinity Pred Norm by SA | AUC Infinity Pred Norm by SA | The area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the surface area. |
| C92321 | AUC Infinity Pred Norm by WT | AUC Infinity Pred Norm by WT | The area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the weight. |
| C85785 | AUC Infinity Pred | AUC Infinity Pred | The area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration. |
| C154846 | AUC Infinity Pred, Unbound Drug | AUC Infinity Pred, Unbound Drug | The portion of predicted AUC to infinity, represented by the unbound fraction of drug. |
| C92322 | AUC Over Dosing Interval Norm by BMI | AUC Over Dosing Interval Norm by BMI | The area under the curve (AUC) for the defined interval between doses (TAU) divided by the body mass index. |
| C92323 | AUC Over Dosing Interval Norm by Dose | AUC Over Dosing Interval Norm by Dose | The area under the curve (AUC) for the defined interval between doses (TAU) divided by the dose. |
| C92324 | AUC Over Dosing Interval Norm by SA | AUC Over Dosing Interval Norm by SA | The area under the curve (AUC) for the defined interval between doses (TAU) divided by the surface area. |
| C92325 | AUC Over Dosing Interval Norm by WT | AUC Over Dosing Interval Norm by WT | The area under the curve (AUC) for the defined interval between doses (TAU) divided by the weight. |
| C85567 | AUC Over Dosing Interval | AUC Over Dosing Interval | The area under the curve (AUC) for the defined interval between doses (TAU). |
| C161414 | AUC to Last Nonzero Conc LN Transformed | AUC to Last Nonzero Conc LN Transformed | The natural log transformed area under the curve (AUC) from the time of dosing to the last measurable concentration. |
| C92309 | AUC to Last Nonzero Conc Norm by BMI | AUC to Last Nonzero Conc Norm by BMI | The area under the curve (AUC) from the time of dosing to the last measurable concentration divided by the body mass index. |
| C92310 | AUC to Last Nonzero Conc Norm by Dose | AUC to Last Nonzero Conc Norm by Dose | The area under the curve (AUC) from the time of dosing to the last measurable concentration divided by the dose. |
| C92311 | AUC to Last Nonzero Conc Norm by SA | AUC to Last Nonzero Conc Norm by SA | The area under the curve (AUC) from the time of dosing to the last measurable concentration divided by the surface area. |
| C92305 | AUC to Last Nonzero Conc Norm by WT | AUC to Last Nonzero Conc Norm by WT | The area under the curve (AUC) from the time of dosing to the last measurable concentration divided by the weight. |
| C85565 | AUC to Last Nonzero Conc | AUC to Last Nonzero Conc | The area under the curve (AUC) from the time of dosing to the last measurable concentration. |
| C154847 | AUC to Last Nonzero Conc, Unbound Drug | AUC to Last Nonzero Conc, Unbound Drug | The portion of the area under the curve (AUC) from the time of dosing to the last measurable concentration, represented by the unbound fraction of drug. |
| C174349 | AUCIFPDW Norm by Dose/WT | AUC Infinity Pred Norm by Dose per Body Weight; AUCIFPDW Norm by Dose/WT | The area under the curve (AUC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration divided by the body weight-adjusted dose. |
| C174348 | AUCINT Norm by Dose/WT | AUC from T1 to T2 Norm by Dose per Body Weight; AUCINT Norm by Dose/kg WT | The area under the curve (AUC) over the interval from T1 to T2 divided by the body weight-adjusted dose. |
| C174347 | AUCLST Norm by Dose/WT | AUC to Last Nonzero Conc Norm by Dose per Body Weight; AUCLST Norm by Dose/WT | The area under the curve (AUC) from the time of dosing to the last measurable concentration divided by the body weight-adjusted dose. |
| C174350 | AUCTAU Norm by Dose/WT | AUC Over Dosing Interval Norm by Dose per Body Weight; AUCTAU Norm by Dose/WT | The area under the curve (AUC) for the defined interval between doses (TAU) divided by the body weight-adjusted dose. |
| C85766 | AUMC % Extrapolation Obs | AUMC % Extrapolation Obs | The area under the moment curve (AUMC) from the last observed non-zero concentration value to infinity as a percentage of the area under the moment curve extrapolated to infinity. |
| C85790 | AUMC % Extrapolation Pred | AUMC % Extrapolation Pred | The area under the moment curve (AUMC) from the last predicted non-zero concentration value to infinity as a percentage of the area under the moment curve extrapolated to infinity. |
| C92330 | AUMC Infinity Obs Norm by BMI | AUMC Infinity Obs Norm by BMI | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the body mass index. |
| C92331 | AUMC Infinity Obs Norm by Dose | AUMC Infinity Obs Norm by Dose | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the dose. |
| C92332 | AUMC Infinity Obs Norm by SA | AUMC Infinity Obs Norm by SA | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the surface area. |
| C92333 | AUMC Infinity Obs Norm by WT | AUMC Infinity Obs Norm by WT | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the weight. |
| C85765 | AUMC Infinity Obs | AUMC Infinity Obs | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the observed value of the last non-zero concentration. |
| C92334 | AUMC Infinity Pred Norm by BMI | AUMC Infinity Pred Norm by BMI | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the body mass index. |
| C92335 | AUMC Infinity Pred Norm by Dose | AUMC Infinity Pred Norm by Dose | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the dose. |
| C92336 | AUMC Infinity Pred Norm by SA | AUMC Infinity Pred Norm by SA | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the surface area. |
| C92337 | AUMC Infinity Pred Norm by WT | AUMC Infinity Pred Norm by WT | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the weight. |
| C85789 | AUMC Infinity Pred | AUMC Infinity Pred | The area under the moment curve (AUMC) extrapolated to infinity, calculated using the predicted value of the last non-zero concentration. |
| C92338 | AUMC Over Dosing Interval Norm by BMI | AUMC Over Dosing Interval Norm by BMI | The area under the first moment curve (AUMC) for the defined interval between doses (TAU) divided by the body mass index. |
| C92339 | AUMC Over Dosing Interval Norm by Dose | AUMC Over Dosing Interval Norm by Dose | The area under the first moment curve (AUMC) for the defined interval between doses (TAU) divided by the dose. |
| C92340 | AUMC Over Dosing Interval Norm by SA | AUMC Over Dosing Interval Norm by SA | The area under the first moment curve (AUMC) for the defined interval between doses (TAU) divided by the surface area. |
| C92341 | AUMC Over Dosing Interval Norm by WT | AUMC Over Dosing Interval Norm by WT | The area under the first moment curve (AUMC) for the defined interval between doses (TAU) divided by the weight. |
| C85570 | AUMC Over Dosing Interval | AUMC Over Dosing Interval | The area under the first moment curve (AUMC) for the defined interval between doses (TAU). |
| C92326 | AUMC to Last Nonzero Conc Norm by BMI | AUMC to Last Nonzero Conc Norm by BMI | The area under the moment curve (AUMC) from the time of dosing to the last measurable concentration divided by the body mass index. |
| C92327 | AUMC to Last Nonzero Conc Norm by Dose | AUMC to Last Nonzero Conc Norm by Dose | The area under the moment curve (AUMC) from the time of dosing to the last measurable concentration divided by the dose. |
| C92328 | AUMC to Last Nonzero Conc Norm by SA | AUMC to Last Nonzero Conc Norm by SA | The area under the moment curve (AUMC) from the time of dosing to the last measurable concentration divided by the surface area. |
| C92329 | AUMC to Last Nonzero Conc Norm by WT | AUMC to Last Nonzero Conc Norm by WT | The area under the moment curve (AUMC) from the time of dosing to the last measurable concentration divided by the weight. |
| C85569 | AUMC to Last Nonzero Conc | AUMC to Last Nonzero Conc | The area under the moment curve (AUMC) from the time of dosing to the last measurable concentration. |
| C85768 | AURC % Extrapolation Obs | AURC % Extrapolation Obs | The area under the excretion rate curve (AURC) from the last observed non-zero rate value to infinity as a percentage of the area under the excretion rate curve extrapolated to infinity. |
| C85792 | AURC % Extrapolation Pred | AURC % Extrapolation Pred | The area under the excretion rate curve (AURC) from the last predicted non-zero rate value to infinity as a percentage of the area under the excretion rate curve extrapolated to infinity. |
| C92342 | AURC All Norm by BMI | AURC All Norm by BMI | The area under the excretion rate curve (AURC) from time zero to the last measurable rate divided by the body mass index. |
| C92343 | AURC All Norm by Dose | AURC All Norm by Dose | The area under the excretion rate curve (AURC) from time zero to the last measurable rate divided by the dose. |
| C92344 | AURC All Norm by SA | AURC All Norm by SA | The area under the excretion rate curve (AURC) from time zero to the last measurable rate divided by the surface area. |
| C92345 | AURC All Norm by WT | AURC All Norm by WT | The area under the excretion rate curve (AURC) from time zero to the last measurable rate divided by the weight. |
| C85841 | AURC All | AURC All | The area under the excretion rate curve (AURC) from time zero to the time of the last observation, regardless of whether the last observation is a measurable concentration or not. |
| C92346 | AURC Dosing to Last Conc Norm by BMI | AURC to Last Nonzero Rate Norm by BMI | The area under the excretion rate curve (AURC) from time zero to the last measurable rate, divided by the body mass index. |
| C92347 | AURC Dosing to Last Conc Norm by Dose | AURC to Last Nonzero Rate Norm by Dose | The area under the excretion rate curve (AURC) from time zero to the last measurable rate, divided by the dose. |
| C92348 | AURC Dosing to Last Conc Norm by SA | AURC to Last Nonzero Rate Norm by SA | The area under the excretion rate curve (AURC) from time zero to the last measurable rate, divided by the surface area. |
| C92349 | AURC Dosing to Last Conc Norm by WT | AURC to Last Nonzero Rate Norm by WT | The area under the excretion rate curve (AURC) from time zero to the last measurable rate, divided by the weight. |
| C92350 | AURC from T1 to T2 Norm by BMI | AURC from T1 to T2 Norm by BMI | The area under the excretion rate curve (AURC) over the interval from T1 to T2 divided by the body mass index. |
| C92351 | AURC from T1 to T2 Norm by Dose | AURC from T1 to T2 Norm by Dose | The area under the excretion rate curve (AURC) over the interval from T1 to T2 divided by the dose. |
| C92352 | AURC from T1 to T2 Norm by SA | AURC from T1 to T2 Norm by SA | The area under the excretion rate curve (AURC) over the interval from T1 to T2 divided by the surface area. |
| C92353 | AURC from T1 to T2 Norm by WT | AURC from T1 to T2 Norm by WT | The area under the excretion rate curve (AURC) over the interval from T1 to T2 divided by the weight. |
| C85572 | AURC from T1 to T2 | AURC from T1 to T2 | The area under the excretion rate curve (AURC) over the interval from T1 to T2. |
| C92354 | AURC Infinity Obs Norm by BMI | AURC Infinity Obs Norm by BMI | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the observed value of the last excretion rate, divided by the body mass index. |
| C92355 | AURC Infinity Obs Norm by Dose | AURC Infinity Obs Norm by Dose | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the observed value of the last excretion rate, divided by the dose. |
| C92356 | AURC Infinity Obs Norm by SA | AURC Infinity Obs Norm by SA | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the observed value of the last excretion rate, divided by the surface area. |
| C92357 | AURC Infinity Obs Norm by WT | AURC Infinity Obs Norm by WT | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the observed value of the last excretion rate, divided by the weight. |
| C85767 | AURC Infinity Obs | AURC Infinity Obs | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the observed value of the last excretion rate. |
| C92358 | AURC Infinity Pred Norm by BMI | AURC Infinity Pred Norm by BMI | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the predicted value of the last non-zero excretion rate, divided by the body mass index. |
| C92359 | AURC Infinity Pred Norm by Dose | AURC Infinity Pred Norm by Dose | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the predicted value of the last non-zero excretion rate, divided by the dose. |
| C92360 | AURC Infinity Pred Norm by SA | AURC Infinity Pred Norm by SA | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the predicted value of the last non-zero excretion rate, divided by the surface area. |
| C92361 | AURC Infinity Pred Norm by WT | AURC Infinity Pred Norm by WT | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the predicted value of the last non-zero excretion rate, divided by the weight. |
| C85791 | AURC Infinity Pred | AURC Infinity Pred | The area under the excretion rate curve (AURC) extrapolated to infinity, calculated using the predicted value of the last non-zero excretion rate. |
| C85571 | AURC to Last Nonzero Rate | AURC to Last Nonzero Rate | The area under the excretion rate curve (AURC) from time zero to the time of the last measurable concentration. |
| C132440 | Average Conc from T1 to T2 Norm by BMI | Average Conc from T1 to T2 Norm by BMI | The area under the curve over the interval from T1 to T2 (AUCINT) divided by the length of the interval and then divided by the body mass index. |
| C132441 | Average Conc from T1 to T2 Norm by Dose | Average Conc from T1 to T2 Norm by Dose | The area under the curve over the interval from T1 to T2 (AUCINT) divided by the length of the interval and then divided by the dose. |
| C132442 | Average Conc from T1 to T2 Norm by SA | Average Conc from T1 to T2 Norm by SA | The area under the curve over the interval from T1 to T2 (AUCINT) divided by the length of the interval and then divided by the surface area. |
| C132443 | Average Conc from T1 to T2 Norm by WT | Average Conc from T1 to T2 Norm by WT | The area under the curve over the interval from T1 to T2 (AUCINT) divided by the length of the interval and then divided by the weight. |
| C132302 | Average Conc from T1 to T2 | Average Conc from T1 to T2 | The area under the curve over the interval from T1 to T2 (AUCINT) divided by the length of the interval. |
| C92367 | Average Conc Norm by BMI | Average Conc Norm by BMI | AUCTAU divided by TAU and then divided by the body mass index. |
| C92368 | Average Conc Norm by Dose | Average Conc Norm by Dose | AUCTAU divided by TAU and then divided by the dose. |
| C92369 | Average Conc Norm by SA | Average Conc Norm by SA | AUCTAU divided by TAU and then divided by the surface area. |
| C92370 | Average Conc Norm by WT | Average Conc Norm by WT | AUCTAU divided by TAU and then divided by the weight. |
| C174351 | Average Concentration Norm by Dose/WT | Average Concentration Norm by Dose/WT | AUCTAU divided by TAU divided by the body weight-adjusted dose. |
| C85575 | Average Concentration | Average Concentration | AUCTAU divided by TAU. |
| C181516 | Average of Conc Trough | Average of Conc Trough | The arithmetic average of two or more trough concentrations. |
| C174352 | CAVGINT Norm by Dose/WT | Average Conc from T1 to T2 Norm by Dose per Body Weight; CAVGINT Norm by Dose/WT | The area under the curve over the interval from T1 to T2 (AUCINT) divided by the length of the interval divided by the body weight-adjusted dose. |
| C102367 | Conc by BMI | Conc by BMI | The concentration divided by body mass index. |
| C102368 | Conc by Dose | Conc by Dose | The concentration divided by dose. |
| C102369 | Conc by SA | Conc by SA | The concentration divided by surface area. |
| C102370 | Conc by WT | Conc by WT | The concentration divided by weight. |
| C102395 | Conc Trough by BMI | Conc Trough by BMI | The trough concentration divided by body mass index. |
| C102396 | Conc Trough by Dose | Conc Trough by Dose | The trough concentration divided by dose. |
| C102397 | Conc Trough by SA | Conc Trough by SA | The trough concentration divided by surface area. |
| C102398 | Conc Trough by WT | Conc Trough by WT | The trough concentration divided by weight. |
| C102394 | Conc Trough | Conc Trough | Concentration at end of dosing interval. |
| C181515 | Concentration at End Infusion | Concentration at End Infusion | The observed concentration at the end of the infusion. |
| C135489 | Concentration at Half Tmax | Concentration at Half Tmax | The concentration that occurs at the midpoint time between dosing time and Tmax. |
| C85821 | Correlation Between TimeX and Log ConcY | Correlation Between TimeX and Log ConcY | The correlation between time (X) and log concentration (Y) for the points used in the estimation of lambda z. |
| C176355 | Dosing Interval | Dosing Interval | The duration of time between two doses. |
| C95007 | Effective Half-Life | Effective Half-Life | The drug half-life that quantifies the accumulation ratio of a drug following multiple dosing. |
| C105450 | Excret Rate from T1 to T2 Norm by BMI | Excret Rate from T1 to T2 Norm by BMI | The excretion rate over the interval from T1 to T2 divided by the body mass index, determined for the specimen type specified in PPSPEC. |
| C105451 | Excret Rate from T1 to T2 Norm by Dose | Excret Rate from T1 to T2 Norm by Dose | The excretion rate over the interval from T1 to T2 divided by the dose, determined for the specimen type specified in PPSPEC. |
| C105452 | Excret Rate from T1 to T2 Norm by SA | Excret Rate from T1 to T2 Norm by SA | The excretion rate over the interval from T1 to T2 divided by the surface area, determined for the specimen type specified in PPSPEC. |
| C105453 | Excret Rate from T1 to T2 Norm by WT | Excret Rate from T1 to T2 Norm by WT | The excretion rate over the interval from T1 to T2 divided by the weight, determined for the specimen type specified in PPSPEC. |
| C105449 | Excret Rate from T1 to T2 | Excret Rate from T1 to T2 | The excretion rate over the interval from T1 to T2, determined for the specimen type specified in PPSPEC. |
| C85581 | Fluctuation% | Fluctuation% | The difference between Cmin and Cmax standardized to Cavg, between dose time and Tau. |
| C156576 | Fract Excr from T1 to T2 | Fract Excr from T1 to T2 | The fraction of the administered dose that is recovered from the specimen type specified in PPSPEC, over the interval between T1 and T2. |
| C154840 | Fraction Bound | Fraction Bound | The percent or ratio of bound substance concentration to the total concentration. |
| C184704 | Fraction of the Dose Metabolized | Fraction of the Dose Metabolized | The fraction of the bioavailable dose which has been metabolized. |
| C135490 | Fraction Unbound | Fraction Unbound | The percent or ratio of free substance concentration to the total concentration. (NCI) |
| C135491 | Half Tmax | Half Tmax | The midpoint time between dosing time and Tmax. |
| C172583 | Half-Life Distribution | Half-Life Distribution | Half-life calculated from the distributional phase. |
| C85818 | Half-Life Lambda z | Half-Life Lambda z | Terminal half-life. |
| C147483 | Half-Life TAU | Half-Life TAU | Half-life calculated within a dosing interval. |
| C112287 | Hemodialysis Clearance | Hemodialysis Clearance | The clearance of a substance from the blood during a hemodialysis session. |
| C116213 | Hemodialysis Extraction Ratio | Hemodialysis Extraction Ratio | The fractional content of a substance removed from the blood during a hemodialysis session. |
| C92383 | Initial Conc Norm by BMI | Initial Conc Norm by BMI | Initial concentration divided by the body mass index. Given only for bolus IV models. |
| C92384 | Initial Conc Norm by Dose | Initial Conc Norm by Dose | Initial concentration divided by the dose. Given only for bolus IV models. |
| C92385 | Initial Conc Norm by SA | Initial Conc Norm by SA | Initial concentration divided by the surface area. Given only for bolus IV models. |
| C92386 | Initial Conc Norm by WT | Initial Conc Norm by WT | Initial concentration divided by the weight. Given only for bolus IV models. |
| C85644 | Initial Conc | Initial Conc | Initial concentration. Given only for bolus IV models. |
| C172584 | K Slope of Distribution | K Slope of Distribution | The distribution rate constant. |
| C147479 | Lambda z Lower Limit TAU | Lambda z Lower Limit TAU | The lower limit on time for values to be included in the calculation of Lambda z, calculated within a dosing interval. |
| C85653 | Lambda z Lower Limit | Lambda z Lower Limit | The lower limit on time for values to be included in the calculation of Lambda z. |
| C135492 | Lambda z Span | Lambda z Span | The interval of time covered by the data points used in the terminal disposition phase regression analysis, divided by half life. This yields the terminal disposition phase duration expressed as the number of half lives. |
| C147481 | Lambda z TAU | Lambda z TAU | The first order rate constant associated with the terminal (log-linear) portion of the curve, calculated within a dosing interval. |
| C147482 | Lambda z Upper Limit TAU | Lambda z Upper Limit TAU | The upper limit on time for values to be included in the calculation of Lambda z, calculated within a dosing interval. |
| C85654 | Lambda z Upper Limit | Lambda z Upper Limit | The upper limit on time for values to be included in the calculation of Lambda z. |
| C85652 | Lambda z | Lambda z | The first order rate constant associated with the terminal (log-linear) portion of the curve. |
| C92391 | Last Meas Excretion Rate Norm by BMI | Last Meas Excretion Rate Norm by BMI | The last measurable (positive) excretion rate divided by the body mass index. |
| C92392 | Last Meas Excretion Rate Norm by Dose | Last Meas Excretion Rate Norm by Dose | The last measurable (positive) excretion rate divided by the dose. |
| C92393 | Last Meas Excretion Rate Norm by SA | Last Meas Excretion Rate Norm by SA | The last measurable (positive) excretion rate divided by the surface area. |
| C92394 | Last Meas Excretion Rate Norm by WT | Last Meas Excretion Rate Norm by WT | The last measurable (positive) excretion rate divided by the weight. |
| C85656 | Last Meas Excretion Rate | Last Meas Excretion Rate | The last measurable (positive) excretion rate determined for the specimen type specified in PPSPEC. |
| C92387 | Last Nonzero Conc Norm by BMI | Last Nonzero Conc Norm by BMI | The concentration corresponding to Tlast divided by the body mass index. |
| C92388 | Last Nonzero Conc Norm by Dose | Last Nonzero Conc Norm by Dose | The concentration corresponding to Tlast divided by the dose. |
| C92389 | Last Nonzero Conc Norm by SA | Last Nonzero Conc Norm by SA | The concentration corresponding to Tlast divided by the surface area. |
| C92390 | Last Nonzero Conc Norm by WT | Last Nonzero Conc Norm by WT | The concentration corresponding to Tlast divided by the weight. |
| C85655 | Last Nonzero Conc | Last Nonzero Conc | The concentration corresponding to Tlast. |
| C161415 | Max Conc LN Transformed | Max Conc LN Transformed | The natural log transformed maximum concentration occurring at Tmax. |
| C92371 | Max Conc Norm by BMI | Max Conc Norm by BMI | The maximum concentration occurring at Tmax, divided by the body mass index. |
| C85698 | Max Conc Norm by Dose | Max Conc Norm by Dose | The maximum concentration occurring at Tmax, divided by the dose. |
| C174353 | Max Conc Norm by Dose/WT | Max Conc Norm by Dose/WT | The maximum concentration occurring at Tmax divided by the body weight-adjusted dose. |
| C92372 | Max Conc Norm by SA | Max Conc Norm by SA | The maximum concentration occurring at Tmax, divided by the surface area. |
| C92373 | Max Conc Norm by WT | Max Conc Norm by WT | The maximum concentration occurring at Tmax, divided by the weight. |
| C70918 | Max Conc | Max Conc | The maximum concentration occurring at Tmax. |
| C154848 | Max Conc, Unbound Drug | Max Conc, Unbound Drug | The maximum concentration represented by the unbound fraction of drug, occurring at Tmax. |
| C92395 | Max Excretion Rate Norm by BMI | Max Excretion Rate Norm by BMI | The maximum excretion rate divided by the body mass index. |
| C92396 | Max Excretion Rate Norm by Dose | Max Excretion Rate Norm by Dose | The maximum excretion rate divided by the dose. |
| C92397 | Max Excretion Rate Norm by SA | Max Excretion Rate Norm by SA | The maximum excretion rate divided by the surface area. |
| C92398 | Max Excretion Rate Norm by WT | Max Excretion Rate Norm by WT | The maximum excretion rate divided by the weight. |
| C85699 | Max Excretion Rate | Max Excretion Rate | The maximum excretion rate determined for the specimen type specified in PPSPEC. |
| C120723 | Mean Absorption Time | Mean Absorption Time | Mean absorption time of a substance administered by extravascular dosing. |
| C85580 | Midpoint of Interval of Last Nonzero ER | Midpoint of Interval of Last Nonzero ER | The midpoint of collection interval associated with last measurable excretion rate. |
| C85823 | Midpoint of Interval of Maximum ER | Midpoint of Interval of Maximum ER | The midpoint of collection interval associated with the maximum excretion rate. |
| C92374 | Min Conc Norm by BMI | Min Conc Norm by BMI | The minimum concentration between dose time and dose time plus Tau (at Tmin) divided by the body mass index. |
| C92375 | Min Conc Norm by Dose | Min Conc Norm by Dose | The minimum concentration between dose time and dose time plus Tau (at Tmin) divided by the dose. |
| C174354 | Min Conc Norm by Dose/WT | Min Conc Norm by Dose/WT | The minimum concentration between dose time and dose time plus Tau (at Tmin) divided by the body weight-adjusted dose. |
| C92376 | Min Conc Norm by SA | Min Conc Norm by SA | The minimum concentration between dose time and dose time plus Tau (at Tmin) divided by the surface area. |
| C92377 | Min Conc Norm by WT | Min Conc Norm by WT | The minimum concentration between dose time and dose time plus Tau (at Tmin) divided by the weight. |
| C85579 | Min Conc | Min Conc | The minimum concentration between dose time and dose time plus Tau (at Tmin). |
| C120724 | MRT Extravasc Infinity Obs | MRT Extravasc Infinity Obs | The mean residence time (MRT) extrapolated to infinity for a substance administered by extravascular dosing, calculated using the observed value of the last non-zero concentration. Extravascular MRT includes Mean Absorption Time (MAT). |
| C120725 | MRT Extravasc Infinity Pred | MRT Extravasc Infinity Pred | The mean residence time (MRT) extrapolated to infinity for a substance administered by extravascular dosing, calculated using the predicted value of the last non-zero concentration. Extravascular MRT includes Mean Absorption Time (MAT). |
| C120726 | MRT Extravasc to Last Nonzero Conc | MRT Extravasc to Last Nonzero Conc | Mean residence time (MRT) from the time of dosing to the time of the last measurable concentration for a substance administered by extravascular dosing. Extravascular MRT includes Mean Absorption Time (MAT). |
| C121134 | MRT IV Bolus Infinity Obs | MRT IV Bolus Infinity Obs | The mean residence time (MRT) extrapolated to infinity for a substance administered by intravascular bolus dosing, calculated using the observed value of the last non-zero concentration. |
| C121136 | MRT IV Bolus Infinity Pred | MRT IV Bolus Infinity Pred | The mean residence time (MRT) extrapolated to infinity for a substance administered by intravascular bolus dosing, calculated using the predicted value of the last non-zero concentration. |
| C121137 | MRT IV Bolus to Last Nonzero Conc | MRT IV Bolus to Last Nonzero Conc | Mean residence time (MRT) from the time of dosing to the time of the last measurable concentration, for a substance administered by intravascular bolus dosing. |
| C181517 | MRT IV Cont Inf Infinity Obs | MRT IV Cont Inf Infinity Obs | The mean residence time (MRT) extrapolated to infinity for a substance administered by constant rate of continuous intravascular infusion, calculated using the observed value of the last non-zero concentration. |
| C181518 | MRT IV Cont Inf Infinity Pred | MRT IV Cont Inf Infinity Pred | The mean residence time (MRT) extrapolated to infinity for a substance administered by constant rate of continuous intravascular infusion, calculated using the predicted value of the last non-zero concentration. |
| C181519 | MRT IV Cont Inf to Last Nonzero Conc | MRT IV Cont Inf to Last Nonzero Conc | Mean residence time (MRT) from the time of dosing to the time of the last measurable concentration, for a substance administered by constant rate of continuous intravascular infusion. |
| C105454 | Nonrenal CL Norm by BMI | Nonrenal CL Norm by BMI | The total clearance of a substance from the blood minus the renal clearance divided by the body mass index. |
| C105455 | Nonrenal CL Norm by Dose | Nonrenal CL Norm by Dose | The total clearance of a substance from the blood minus the renal clearance divided by the dose. |
| C105456 | Nonrenal CL Norm by SA | Nonrenal CL Norm by SA | The total clearance of a substance from the blood minus the renal clearance divided by the surface area. |
| C105457 | Nonrenal CL Norm by WT | Nonrenal CL Norm by WT | The total clearance of a substance from the blood minus the renal clearance divided by the weight. |
| C102376 | Nonrenal CL | Nonrenal CL | The total clearance of a substance from the blood less the renal clearance. |
| C147480 | Number of Points for Lambda z TAU | Number of Points for Lambda z TAU | The number of time points used in computing Lambda z determined in a dosing interval. |
| C85816 | Number of Points for Lambda z | Number of Points for Lambda z | The number of time points used in computing Lambda z. |
| C102383 | Pct Rec from T1 to T2 Norm by BMI | Pct Rec from T1 to T2 Norm by BMI | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC, over the interval between T1 and T2 divided by body mass index. |
| C102384 | Pct Rec from T1 to T2 Norm by SA | Pct Rec from T1 to T2 Norm by SA | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC, over the interval between T1 and T2 divided by surface area. |
| C102385 | Pct Rec from T1 to T2 Norm by WT | Pct Rec from T1 to T2 Norm by WT | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC, over the interval between T1 and T2 divided by weight. |
| C102382 | Pct Rec from T1 to T2 | Pct Rec from T1 to T2 | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC, over the interval between T1 and T2. |
| C112389 | Pct Rec Infinity Obs Norm by BMI | Pct Rec Infinity Obs Norm by BMI | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the body mass index. |
| C112390 | Pct Rec Infinity Obs Norm by SA | Pct Rec Infinity Obs Norm by SA | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the surface area. |
| C112391 | Pct Rec Infinity Obs Norm by WT | Pct Rec Infinity Obs Norm by WT | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the observed value of the last non-zero concentration, divided by the weight. |
| C112034 | Pct Rec Infinity Obs | Pct Rec Infinity Obs | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the observed value of the last non-zero concentration. |
| C112392 | Pct Rec Infinity Pred Norm by BMI | Pct Rec Infinity Pred Norm by BMI | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the body mass index. |
| C112393 | Pct Rec Infinity Pred Norm by SA | Pct Rec Infinity Pred Norm by SA | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the surface area. |
| C112394 | Pct Rec Infinity Pred Norm by WT | Pct Rec Infinity Pred Norm by WT | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the predicted value of the last non-zero concentration, divided by the weight. |
| C112035 | Pct Rec Infinity Pred | Pct Rec Infinity Pred | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC extrapolated to infinity, calculated using the predicted value of the last non-zero concentration. |
| C102387 | Pct Rec Over Dosing Interval Norm by BMI | Pct Rec Over Dosing Interval Norm by BMI | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC, between doses (TAU) divided by the body mass index. |
| C102388 | Pct Rec Over Dosing Interval Norm by SA | Pct Rec Over Dosing Interval Norm by SA | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC, between doses (TAU) divided by surface area. |
| C102389 | Pct Rec Over Dosing Interval Norm by WT | Pct Rec Over Dosing Interval Norm by WT | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC, between doses (TAU) divided by weight. |
| C102386 | Pct Rec Over Dosing Interval | Pct Rec Over Dosing Interval | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC, between doses (TAU). |
| C166075 | Pct Rec to Last Nonzero Conc | Pct Rec to Last Nonzero Conc | The percentage of the administered dose that is recovered from the specimen type specified in PPSPEC, from the time of dosing to the last non-zero concentration. |
| C102381 | Peak Trough Ratio | Peak Trough Ratio | The maximum concentration during a dosing interval divided by the concentration at the end of the dosing interval. |
| C85553 | R Squared Adjusted | R Squared Adjusted | The goodness of fit statistic for the terminal elimination phase, adjusted for the number of time points used in the estimation of Lambda z. |
| C85542 | R Squared | R Squared | The goodness of fit statistic for the terminal elimination phase. |
| C176347 | Ratio Amt Rec from T1 to T2 | Ratio Amt Rec from T1 to T2 | The ratio of two amount recovered from T1 to T2 values. |
| C176354 | Ratio Amt Rec Infinity Obs | Ratio Amt Rec Infinity Obs | The ratio of two amount recovered infinity observed values. |
| C176344 | Ratio AUC All | Ratio AUC All | The ratio of two AUC All values. |
| C176349 | Ratio AUC from T1 to T2 Norm by Dose | Ratio AUC from T1 to T2 Norm by Dose | The ratio of two AUC from T1 to T2 normalized by dose values. |
| C176236 | Ratio AUC from T1 to T2 | Ratio AUC from T1 to T2 | The ratio of two AUC from T1 to T2 values. |
| C176348 | Ratio AUC Infinity Obs Norm by Dose | Ratio AUC Infinity Obs Norm by Dose | The ratio of two AUC infinity observed normalized by dose values. |
| C156578 | Ratio AUC Infinity Obs | Ratio AUC Infinity Obs | The ratio of two AUC infinity observed values. |
| C156577 | Ratio AUC Infinity Pred | Ratio AUC Infinity Pred | The ratio of two AUC infinity predicted values. |
| C176351 | Ratio AUC Over Dosing Interval | Ratio AUC Over Dosing Interval | The ratio of two AUCTAU values. |
| C176237 | Ratio AUC to Last Nonzero Conc | Ratio AUC to Last Nonzero Conc | The ratio of two AUC to last nonzero concentration values. |
| C156471 | Ratio AUC | Ratio AUC | The ratio of two AUC values. |
| C176345 | Ratio Average Concentration | Ratio Average Concentration | The ratio of two average concentration values. |
| C156579 | Ratio CMAX | Ratio CMAX | The ratio of two Cmax values. |
| C176353 | Ratio Conc Trough | Ratio Conc Trough | The ratio of two CTROUGH values. |
| C176235 | Ratio Concentration | Ratio Concentration | The ratio of two concentration values. |
| C176352 | Ratio Max Conc Norm by Dose | Ratio Max Conc Norm by Dose | The ratio of two maximum concentration normalized by dose values. |
| C176346 | Ratio Min Conc | Ratio Min Conc | The ratio of two cmin values. |
| C156580 | Ratio of CMAX to CMIN | Ratio of CMAX to CMIN | The ratio of Cmax value to Cmin value. |
| C176350 | RatioAUC to Last Nonzero Conc NormByDose | Ratio AUC to Last Nonzero Conc Norm by Dose | The ratio of two AUC to last nonzero concentration normalized by dose values. |
| C154839 | Relative Bioavailability | Relative Bioavailability | The fraction of the treatment dose that reaches the systemic circulation relative to a reference route or reference formulation. The ratio of the amount of drug in the system (area under the curve) after administration of a test formulation divided by the drug in the system after a non-IV administration of a reference formulation and/or reference route. |
| C154849 | Renal CL as Pct CL EV | Renal CL as Pct CL EV | The portion of total clearance attributed to the kidneys expressed as a percentage, following extravascular administration. |
| C154850 | Renal CL as Pct CL IV | Renal CL as Pct CL IV | The portion of total clearance attributed to the kidneys expressed as a percentage, following intravenous administration. |
| C122334 | Renal CL for Dose Int Norm by BMI | Renal CL for Dose Int Norm by BMI | The clearance of a substance from the blood by the kidneys, calculated using AUCTAU, divided by the body mass index. |
| C122335 | Renal CL for Dose Int Norm by Dose | Renal CL for Dose Int Norm by Dose | The clearance of a substance from the blood by the kidneys, calculated using AUCTAU, divided by the dose. |
| C122336 | Renal CL for Dose Int Norm by SA | Renal CL for Dose Int Norm by SA | The clearance of a substance from the blood by the kidneys, calculated using AUCTAU, divided by the surface area. |
| C122337 | Renal CL for Dose Int Norm by WT | Renal CL for Dose Int Norm by WT | The clearance of a substance from the blood by the kidneys, calculated using AUCTAU, divided by the weight. |
| C122050 | Renal CL for Dose Int | Renal CL for Dose Int | The clearance of a substance from the blood by the kidneys, calculated using AUCTAU. |
| C154843 | Renal CL for Unbound Drug | Renal CL for Unbound Drug | The unbound fraction of drug within the portion of total clearance attributed to the kidneys. |
| C122330 | Renal CL from T1 to T2 Norm by BMI | Renal CL from T1 to T2 Norm by BMI | The clearance of a substance from the blood by the kidneys over the interval from T1 to T2 divided by the body mass index. |
| C122331 | Renal CL from T1 to T2 Norm by Dose | Renal CL from T1 to T2 Norm by Dose | The clearance of a substance from the blood by the kidneys over the interval from T1 to T2 divided by the dose. |
| C122332 | Renal CL from T1 to T2 Norm by SA | Renal CL from T1 to T2 Norm by SA | The clearance of a substance from the blood by the kidneys over the interval from T1 to T2 divided by the surface area. |
| C122333 | Renal CL from T1 to T2 Norm by WT | Renal CL from T1 to T2 Norm by WT | The clearance of a substance from the blood by the kidneys over the interval from T1 to T2 divided by the weight. |
| C122049 | Renal CL from T1 to T2 | Renal CL from T1 to T2 | The clearance of a substance from the blood by the kidneys over the interval from T1 to T2. |
| C105458 | Renal CL Norm by BMI | Renal CL Norm by BMI | The clearance of a substance from the blood by the kidneys divided by the body mass index. |
| C105459 | Renal CL Norm by Dose | Renal CL Norm by Dose | The clearance of a substance from the blood by the kidneys divided by the dose. |
| C105460 | Renal CL Norm by SA | Renal CL Norm by SA | The clearance of a substance from the blood by the kidneys divided by the surface area. |
| C105461 | Renal CL Norm by WT | Renal CL Norm by WT | The clearance of a substance from the blood by the kidneys divided by the weight. |
| C75913 | Renal CL | Renal CL | The clearance of a substance from the blood by the kidneys. |
| C122338 | Stationarity Ratio AUC | Stationarity Ratio AUC | The area under the curve (AUCTAU) at steady state divided by the area under the curve extrapolated to infinity for the initial dosing interval. |
| C85817 | Sum of Urine Vol | Sum of Urine Vol | The sum of urine volumes that are used for PK parameters. |
| C161416 | Swing | Swing | The difference between Cmax and Cmin standardized to Cmin within a dosing interval. |
| C70919 | Time of CMAX | Time of CMAX | The time of maximum observed concentration sampled during a dosing interval. |
| C85825 | Time of CMIN Observation | Time of CMIN Observation | The time of minimum concentration sampled during a dosing interval. |
| C85822 | Time of Last Nonzero Conc | Time of Last Nonzero Conc | The time of the last measurable (positive) concentration. |
| C85824 | Time Until First Nonzero Conc | Time Until First Nonzero Conc | The time prior to the first measurable (non-zero) concentration. |
| C114227 | Total CL by F for Dose Int Norm by BMI | Total CL by F for Dose Int Norm by BMI | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU, divided by the body mass index. |
| C114226 | Total CL by F for Dose Int Norm by Dose | Total CL by F for Dose Int Norm by Dose | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU, divided by the dose. |
| C114228 | Total CL by F for Dose Int Norm by SA | Total CL by F for Dose Int Norm by SA | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU, divided by the surface area. |
| C114229 | Total CL by F for Dose Int Norm by WT | Total CL by F for Dose Int Norm by WT | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU, divided by the weight. |
| C114121 | Total CL by F for Dose Int | Total CL by F for Dose Int | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU. |
| C114231 | Total CL for Dose Int Norm by BMI | Total CL for Dose Int Norm by BMI | The total body clearance for intravascular administration, calculated using AUCTAU, divided by the body mass index. |
| C114230 | Total CL for Dose Int Norm by Dose | Total CL for Dose Int Norm by Dose | The total body clearance for intravascular administration, calculated using AUCTAU, divided by the dose. |
| C114232 | Total CL for Dose Int Norm by SA | Total CL for Dose Int Norm by SA | The total body clearance for intravascular administration, calculated using AUCTAU, divided by the surface area. |
| C114233 | Total CL for Dose Int Norm by WT | Total CL for Dose Int Norm by WT | The total body clearance for intravascular administration, calculated using AUCTAU, divided by the weight. |
| C114122 | Total CL for Dose Int | Total CL for Dose Int | The total body clearance for intravascular administration, calculated using AUCTAU. |
| C92399 | Total CL Obs by F Norm by BMI | Total CL Obs by F Norm by BMI | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration, divided by the body mass index. |
| C92400 | Total CL Obs by F Norm by Dose | Total CL Obs by F Norm by Dose | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration, divided by the dose. |
| C92401 | Total CL Obs by F Norm by SA | Total CL Obs by F Norm by SA | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration, divided by the surface area. |
| C92402 | Total CL Obs by F Norm by WT | Total CL Obs by F Norm by WT | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration, divided by the weight. |
| C85772 | Total CL Obs by F | Total CL Obs by F | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration. |
| C154842 | Total CL Obs for Unbound Drug | Total CL Obs for Unbound Drug | The total body clearance for intravascular administration divided by the fraction of drug unbound, calculated using the observed value of the last non-zero concentration. |
| C92403 | Total CL Obs Norm by BMI | Total CL Obs Norm by BMI | The total body clearance for intravascular administration, calculated using the observed value of the last non-zero concentration, divided by the body mass index. |
| C92404 | Total CL Obs Norm by Dose | Total CL Obs Norm by Dose | The total body clearance for intravascular administration, calculated using the observed value of the last non-zero concentration, divided by the dose. |
| C92405 | Total CL Obs Norm by SA | Total CL Obs Norm by SA | The total body clearance for intravascular administration, calculated using the observed value of the last non-zero concentration, divided by the surface area. |
| C92406 | Total CL Obs Norm by WT | Total CL Obs Norm by WT | The total body clearance for intravascular administration, calculated using the observed value of the last non-zero concentration, divided by the weight. |
| C85773 | Total CL Obs | Total CL Obs | The total body clearance for intravascular administration, calculated using the observed value of the last non-zero concentration. |
| C92417 | Total CL Pred by F Norm by BMI | Total CL Pred by F Norm by BMI | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration, divided by body mass index. |
| C92418 | Total CL Pred by F Norm by Dose | Total CL Pred by F Norm by Dose | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration, divided by the dose. |
| C92419 | Total CL Pred by F Norm by SA | Total CL Pred by F Norm by SA | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration, divided by the surface area. |
| C92420 | Total CL Pred by F Norm by WT | Total CL Pred by F Norm by WT | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration, divided by the weight. |
| C85796 | Total CL Pred by F | Total CL Pred by F | The total body clearance for extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration. |
| C154841 | Total CL Pred for Unbound Drug | Total CL Pred for Unbound Drug | The total body clearance for intravascular administration divided by the fraction of drug unbound, calculated using the predicted value of the last non-zero concentration. |
| C92421 | Total CL Pred Norm by BMI | Total CL Pred Norm by BMI | The total body clearance for intravascular administration, calculated using the predicted value of the last non-zero concentration, divided by the body mass index. |
| C92422 | Total CL Pred Norm by Dose | Total CL Pred Norm by Dose | The total body clearance for intravascular administration, calculated using the predicted value of the last non-zero concentration, divided by the dose. |
| C92423 | Total CL Pred Norm by SA | Total CL Pred Norm by SA | The total body clearance for intravascular administration, calculated using the predicted value of the last non-zero concentration, divided by the surface area. |
| C92424 | Total CL Pred Norm by WT | Total CL Pred Norm by WT | The total body clearance for intravascular administration, calculated using the predicted value of the last non-zero concentration, divided by the weight. |
| C85797 | Total CL Pred | Total CL Pred | The total body clearance for intravascular administration, calculated using the predicted value of the last non-zero concentration. |
| C122339 | Trough Peak Ratio | Trough Peak Ratio | The concentration at the start of a dosing interval divided by the maximum concentration during the dosing interval. |
| C102372 | Vol Dist Initial Norm by BMI | Vol Dist Initial Norm by BMI | The initial volume of distribution for a substance administered by bolus intravascular dosing divided by the body mass index. |
| C102373 | Vol Dist Initial Norm by Dose | Vol Dist Initial Norm by Dose | The initial volume of distribution for a substance administered by bolus intravascular dosing divided by the dose. |
| C102374 | Vol Dist Initial Norm by SA | Vol Dist Initial Norm by SA | The initial volume of distribution for a substance administered by bolus intravascular dosing divided by the surface area. |
| C102375 | Vol Dist Initial Norm by WT | Vol Dist Initial Norm by WT | The initial volume of distribution for a substance administered by bolus intravascular dosing divided by the weight. |
| C102371 | Vol Dist Initial | Vol Dist Initial | The initial volume of distribution for a substance administered by bolus intravascular dosing. |
| C156574 | Vol Dist Steady State Obs by B | Vol Dist Steady State Obs by B | The volume of distribution at steady state based on the observed CLST for a substance administered, divided by the fraction of bound drug. |
| C156570 | Vol Dist Steady State Obs by F | Vol Dist Steady State Obs by F | The volume of distribution at steady state based on the observed CLST for a substance administered by extravascular dosing, divided by the fraction of dose absorbed. |
| C156572 | Vol Dist Steady State Obs by UB | Vol Dist Steady State Obs by UB | The volume of distribution at steady state based on the observed CLST for a substance administered, divided by the fraction of unbound drug. |
| C102377 | Vol Dist Steady State Obs Norm by BMI | Vol Dist Steady State Obs Norm by BMI | The volume of distribution at steady state based on the observed CLST for a substance administered by intravascular dosing divided by the body mass index. |
| C102378 | Vol Dist Steady State Obs Norm by Dose | Vol Dist Steady State Obs Norm by Dose | The volume of distribution at steady state based on the observed CLST for a substance administered by intravascular dosing divided by the dose. |
| C102379 | Vol Dist Steady State Obs Norm by SA | Vol Dist Steady State Obs Norm by SA | The volume of distribution at steady state based on the observed CLST for a substance administered by intravascular dosing divided by the surface area. |
| C102380 | Vol Dist Steady State Obs Norm by WT | Vol Dist Steady State Obs Norm by WT | The volume of distribution at steady state based on the observed CLST for a substance administered by intravascular dosing divided by the weight. |
| C85770 | Vol Dist Steady State Obs | Vol Dist Steady State Obs | The volume of distribution at steady state based on the observed CLST for a substance administered by intravascular dosing. |
| C156575 | Vol Dist Steady State Pred by B | Vol Dist Steady State Pred by B | The volume of distribution at steady state based on the predicted CLST for a substance administered, divided by the fraction of bound drug. |
| C156571 | Vol Dist Steady State Pred by F | Vol Dist Steady State Pred by F | The volume of distribution at steady state based on the predicted CLST for a substance administered by extravascular dosing, divided by the fraction of dose absorbed. |
| C156573 | Vol Dist Steady State Pred by UB | Vol Dist Steady State Pred by UB | The volume of distribution at steady state based on the predicted CLST for a substance administered, divided by the fraction of unbound drug. |
| C102390 | Vol Dist Steady State Pred Norm by BMI | Vol Dist Steady State Pred Norm by BMI | The volume of distribution at steady state based on the predicted CLST for a substance administered by intravascular dosing divided by the body mass index. |
| C102391 | Vol Dist Steady State Pred Norm by Dose | Vol Dist Steady State Pred Norm by Dose | The volume of distribution at steady state based on the predicted CLST for a substance administered by intravascular dosing divided by the dose. |
| C102392 | Vol Dist Steady State Pred Norm by SA | Vol Dist Steady State Pred Norm by SA | The volume of distribution at steady state based on the predicted CLST for a substance administered by intravascular dosing divided by the surface area. |
| C102393 | Vol Dist Steady State Pred Norm by WT | Vol Dist Steady State Pred Norm by WT | The volume of distribution at steady state based on the predicted CLST for a substance administered by intravascular dosing divided by the weight. |
| C85794 | Vol Dist Steady State Pred | Vol Dist Steady State Pred | The volume of distribution at steady state based on the predicted CLST for a substance administered by intravascular dosing. |
| C111365 | Vz for Dose Int by F Norm by BMI | Vz for Dose Int by F Norm by BMI | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU, divided by the body mass index. |
| C111366 | Vz for Dose Int by F Norm by Dose | Vz for Dose Int by F Norm by Dose | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU, divided by the dose. |
| C111367 | Vz for Dose Int by F Norm by SA | Vz for Dose Int by F Norm by SA | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU, divided by the surface area. |
| C111368 | Vz for Dose Int by F Norm by WT | Vz for Dose Int by F Norm by WT | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU, divided by the weight. |
| C111364 | Vz for Dose Int by F | Vz for Dose Int by F | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using AUCTAU. |
| C111369 | Vz for Dose Int Norm by BMI | Vz for Dose Int Norm by BMI | The volume of distribution associated with the terminal slope following intravascular administration, calculated using AUCTAU, divided by the body mass index. |
| C111370 | Vz for Dose Int Norm by Dose | Vz for Dose Int Norm by Dose | The volume of distribution associated with the terminal slope following intravascular administration, calculated using AUCTAU, divided by the dose. |
| C111371 | Vz for Dose Int Norm by SA | Vz for Dose Int Norm by SA | The volume of distribution associated with the terminal slope following intravascular administration, calculated using AUCTAU, divided by the surface area. |
| C111372 | Vz for Dose Int Norm by WT | Vz for Dose Int Norm by WT | The volume of distribution associated with the terminal slope following intravascular administration, calculated using AUCTAU, divided by the weight. |
| C111333 | Vz for Dose Int | Vz for Dose Int | The volume of distribution associated with the terminal slope following intravascular administration, calculated using AUCTAU. |
| C156581 | Vz Obs by F for UB | Vz Obs by F for UB | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration and corrected for unbound drug. |
| C92410 | Vz Obs by F Norm by BMI | Vz Obs by F Norm by BMI | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration, divided by the body mass index. |
| C102729 | Vz Obs by F Norm by Dose | Vz Obs by F Norm by Dose | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration, divided by the dose. |
| C92411 | Vz Obs by F Norm by SA | Vz Obs by F Norm by SA | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration, divided by the surface area. |
| C92412 | Vz Obs by F Norm by WT | Vz Obs by F Norm by WT | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration, divided by the weight. |
| C85775 | Vz Obs by F | Vz Obs by F | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the observed value of the last non-zero concentration. |
| C158265 | Vz Obs for UB | Vz Obs for UB | The volume of distribution associated with the terminal slope following administration, calculated using the observed value of the last non-zero concentration and corrected for unbound drug. |
| C92407 | Vz Obs Norm by BMI | Vz Obs Norm by BMI | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the observed value of the last non-zero concentration, divided by the body mass index. |
| C102683 | Vz Obs Norm by Dose | Vz Obs Norm by Dose | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the observed value of the last non-zero concentration, divided by the dose. |
| C92408 | Vz Obs Norm by SA | Vz Obs Norm by SA | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the observed value of the last non-zero concentration, divided by the surface area. |
| C92409 | Vz Obs Norm by WT | Vz Obs Norm by WT | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the observed value of the last non-zero concentration, divided by the weight. |
| C85774 | Vz Obs | Vz Obs | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the observed value of the last non-zero concentration. |
| C158267 | Vz Pred by F for UB | Vz Pred by F for UB | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value at the time of the last non-zero concentration and corrected for unbound drug. |
| C92428 | Vz Pred by F Norm by BMI | Vz Pred by F Norm by BMI | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration, divided by the body mass index. |
| C102730 | Vz Pred by F Norm by Dose | Vz Pred by F Norm by Dose | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration, divided by the dose. |
| C92429 | Vz Pred by F Norm by SA | Vz Pred by F Norm by SA | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration, divided by the surface area. |
| C92430 | Vz Pred by F Norm by WT | Vz Pred by F Norm by WT | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration, divided by the weight. |
| C85799 | Vz Pred by F | Vz Pred by F | The volume of distribution associated with the terminal slope following extravascular administration divided by the fraction of dose absorbed, calculated using the predicted value of the last non-zero concentration. |
| C158266 | Vz Pred for UB | Vz Pred for UB | The volume of distribution associated with the terminal slope following administration, calculated using the predicted value at the time of the last non-zero concentration and corrected for unbound drug. |
| C92425 | Vz Pred Norm by BMI | Vz Pred Norm by BMI | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the predicted value of the last non-zero concentration, divided by the body mass index. |
| C102696 | Vz Pred Norm by Dose | Vz Pred Norm by Dose | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the predicted value of the last non-zero concentration, divided by the dose. |
| C92426 | Vz Pred Norm by SA | Vz Pred Norm by SA | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the predicted value of the last non-zero concentration, divided by the surface area. |
| C92427 | Vz Pred Norm by WT | Vz Pred Norm by WT | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the predicted value of the last non-zero concentration, divided by the weight. |
| C85798 | Vz Pred | Vz Pred | The volume of distribution associated with the terminal slope following intravascular administration, calculated using the predicted value of the last non-zero concentration. |

