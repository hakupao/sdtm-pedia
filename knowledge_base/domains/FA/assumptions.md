# FA — Assumptions

1. The Findings About domain shares all qualities and conventions of findings observations.

2. See Section 6.4.1, When to Use Findings About Events or Interventions; and Section 8.6.3, Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions; for guidance on deciding between the use of the FA domain and other SDTM structures.

3. See Section 6.4.2, Naming Findings About Domains, for advice on splitting the FA domain.

4. Some variables in the events and interventions domains (e.g., OCCUR, SEV, TOXGR) represent findings about the whole of the event or intervention. When FA is used to represent findings about a part of the event or intervention (i.e., the assessment has different timing from the event as a whole), the FATEST and FATESTCD values should be the same as the variable name and variable label in the corresponding event or intervention domain. See Section 6.4.3, Variables Unique to Findings About.
   a. Associations between some findings about cardiovascular interventions or events and their response codelists are described in the CV codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

5. When data collection establishes a relationship between FA records and an events or interventions record, the relationship should be represented in RELREC.
   a. The FAOBJ variable alone is not sufficient to establish a relationship, because an events or interventions dataset may have multiple records for the same topic (e.g., --TERM or --DECOD, --TRT or --DECOD).

6. Any Identifier variables, Timing variables, or Findings general observation-class qualifiers may be added to the FA domain, but the following qualifiers should generally not be used: --BODSYS, --MODIFY, --SEV, --TOXGR.
