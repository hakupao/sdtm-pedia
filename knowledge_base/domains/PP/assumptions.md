# PP — Assumptions

1. Pharmacokinetics Parameters is a derived dataset, and may be produced from an analysis dataset with a different structure. As a result, some sponsors may need to normalize their analysis dataset in order for it to fit into the SDTM-based PP domain.

2. Information pertaining to all parameters (e.g., number of exponents, model weighting) should be submitted in the SUPPPP dataset.

3. There are separate codelists used for PPORRESU/PPSTRESU where the choice depends on whether the value of the pharmacokinetic parameter is normalized.
   a. Codelist "PKUNIT" is used for non-normalized parameters.
   b. Codelists "PKUDMG" and "PKUDUG" are used when parameters are normalized by dose amount in milligrams or micrograms, respectively.
   c. Codelists "PKUWG" and "PKUWKG" are used when parameters are normalized by weight in grams or kilograms, respectively.

4. Multiple subset codelists were created for the unique unit expressions of the same concept across codelists. This approach allows study-context appropriate use of unit values for pharmacokinetics (PK) analysis subtypes. Controlled Terminology Rules for PK are available at https://www.cdisc.org/standards/terminology/controlled-terminology.

5. Any Identifiers, Timing variables, or Findings general observation class qualifiers may be added to the PP domain, but the following qualifiers would not generally be used: --BODSYS, --SEV.
