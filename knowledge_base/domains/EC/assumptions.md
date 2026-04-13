# EC — Assumptions

1. The EC domain model reflects protocol-specified study treatment administrations, as collected.
   a. EC should be used in all cases where collected exposure information cannot or should not be directly represented in the Exposure (EX) domain. For example, administrations collected in tablets when the protocol-specified unit is mg, or administrations collected in mL when the protocol-specified unit is mg/kg. Product accountability details (e.g., amount dispensed, amount returned) are represented in the DA domain, not in EC.
   b. Collected exposure data are in most cases represented in a combination of 1 or more of EC, DA, or Findings About Events or Interventions (FA) domains. If the entire EC dataset is an exact duplicate of the entire EX dataset, then EC is optional and at the sponsor's discretion.
   c. Collected exposure log data points descriptive of administrations typically reflect amounts at the product-level (e.g., number of tablets, number of mL).

2. Treatment description (ECTRT) is sponsor-defined and should reflect how the protocol-specified study treatment is known or referred to in data collection. In an open-label study, ECTRT should store the treatment name. In a masked study, if treatment is collected and known as tablet A to the subject or administrator, then ECTRT = "TABLET A". If, in a masked study, the treatment is not known by a synonym and the data are to be exchanged between sponsors, partners, and/or regulatory agency(s), then assign ECTRT the value of "MASKED".

3. ECMOOD is permissible; when implemented, it must be populated for all records.
   a. Values of ECMOOD, to date include:
      i. "SCHEDULED" (for collected subject-level intended dose records)
      ii. "PERFORMED" (for collected subject-level actual dose records)
   b. Qualifier variables should be populated with equal granularity across scheduled and performed records when known. For example, if ECDOSU and ECDOSFRQ are known at scheduling and administration, then the variables would be populated on both records. If ECLOC is determined at the time of administration, then it would be populated on the Performed record only.
   c. Appropriate timing variable(s) should be populated. Note: Details on Scheduled records may describe timing at a higher level than Performed records.
   d. ECOCCUR is generally not applicable for Scheduled records.
   e. An activity may be rescheduled or modified multiple times before being performed. Representation of Scheduled records is dependent on the collected, available data. If each rescheduled or modified activity is collected, then multiple Scheduled records may be represented. If only the final scheduled activity is collected, then it would be the only Scheduled record represented.

4. Doses not taken, not given, or missed
   a. The record qualifier --OCCUR, with value of "N", is available in domains based on the Interventions and Events General Observation Classes as the standard way to represent whether an intervention or event did not happen. In the EC domain, ECOCCUR value of "N" indicates a dose was not taken, not given, or missed. For example, if zero tablets are taken within a timeframe or zero mL is infused at a visit, then ECOCCUR = "N" is the standard representation of the collected doses not taken, not given, or missed. Dose amount variables (e.g., ECDOSE, ECDOSTXT) must not be set to zero (0) as an alternative method for indicating doses not taken, not given, or missed.
   b. The population of qualifier variables (e.g., grouping, record) and additional timing variables (e.g., date of collection, visit, time point) for records representing information collected about doses not taken, not given, or missed should be populated with equal granularity as administered records, when known and/or applicable. Qualifiers that indicate dose amount (e.g., ECDOSE, ECDOSTXT) may be populated with positive (non-zero) values in cases where the sponsor feels it is necessary and/or appropriate to represent specific dose amounts not taken, not given, or missed.
   c. If a reason why a dose was not given is collected, it is represented in ECREASOC, the reason why ECOCCUR = "N".

5. Timing variables
   a. Timing variables in the EC domain should reflect administrations by the intervals they were collected (e.g., constant-dosing intervals, visits, targeted dates like first dose, last dose).
   b. For administrations considered given at a point in time (e.g., oral tablet, pre-filled syringe injection), where only an administration date/time is collected, ECSTDTC should be copied to ECENDTC.

6. The degree of summarization of records from EC to EX is sponsor-defined to support study purpose and analysis. When the relationship between EC and EX records can be described in RELREC, then it should be defined. EX derivations must be described in the Define-XML document.

7. Additional interventions qualifiers
   a. --DOSTOT is under evaluation for potential deprecation and replacement with a mechanism to describe total dose over any interval of time (e.g., day, week, month). Sponsors considering ECDOSTOT may want to consider using other dose amount variables (ECDOSE or ECDOSTXT) in combination with frequency (ECDOSFRQ) and timing variables to represent the data.
   b. Any identifier variables, timing variables, or findings general observation-class qualifiers may be added to the EC domain, but the following qualifiers would generally not be used: --STAT and --REASND.
