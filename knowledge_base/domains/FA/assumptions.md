# FA — Assumptions

1. The Findings About domain shares all qualities and conventions of findings observations.

2. See Section 6.4.1, When to Use Findings About Events or Interventions; and Section 8.6.3, Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions; for guidance on deciding between the use of the FA domain and other SDTM structures.

3. See Section 6.4.2, Naming Findings About Domains, for advice on splitting the FA domain.

4. Some variables in the events and interventions domains (e.g., OCCUR, SEV, TOXGR) represent findings about the whole of the event or intervention. When FA is used to represent findings about a part of the event or intervention (i.e., the assessment has different timing from the event as a whole), the FATEST and FATESTCD values should be the same as the variable name and variable label in the corresponding event or intervention domain. See Section 6.4.3, Variables Unique to Findings About.
   a. Associations between some findings about cardiovascular interventions or events and their response codelists are described in the CV codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

5. When data collection establishes a relationship between FA records and an events or interventions record, the relationship should be represented in RELREC.
   a. The FAOBJ variable alone is not sufficient to establish a relationship, because an events or interventions dataset may have multiple records for the same topic (e.g., --TERM or --DECOD, --TRT or --DECOD).

6. Any Identifier variables, Timing variables, or Findings general observation-class qualifiers may be added to the FA domain, but the following qualifiers should generally not be used: --BODSYS, --MODIFY, --SEV, --TOXGR.

## §6.4.1 When to Use Findings About Events or Interventions

The Findings About Events or Interventions structure (or "FA structure") is intended, as its name implies, to be used when findings about an event or intervention need to be captured.

**Criterion 1: Data or observations that have different timing from an associated event or intervention as a whole**

Per Section 6.2.1, Adverse Events, assumption 7.e, "It is the sponsor's responsibility to define an event." One common practice is to define an event as the collection of symptoms related to a reported adverse event. Typically, the event (and its AE record) has timing equal to the worst point in time, but symptoms are measured at multiple time points.

A finding that is about part of an event, rather than the event as a whole, meets this criterion for the use of FA. An assessment of the severity of an individual symptom at a specific point in time is a finding about the event.

Repeated assessments of disease or treatment-related symptoms, particularly symptoms that are likely to be intermittent, meet this criterion.

Occasionally, data collection will include questions about the occurrence of prespecified events which are of naturally short duration (e.g., infusion-related reactions, seizures) for which repeated assessments at fixed time points are made after the occurrence of the event.

A finding which is a summary of multiple occurrences of a particular kind of event meets this criterion. For example, the maximum severity of headache during a specified time period after each dose is a summary of all headache events during that period.

For events that have not ended at the time of an assessment, "event as a whole" means the event up to the time of the assessment.

Assessments of parts of events (snapshots or slices) are represented in FA and may or may not have parent records (e.g., individual symptoms of an adverse event may or may not have a parent adverse event record), depending on whether the overall event is also recorded.

This criterion is less likely to apply to interventions records than to events records. Interventions records often represent a single administration of a drug or procedure, and an assessment such as blood pressure taken during the administration would have timing specific to a time within the administration.

**Criterion 2: An observation about an event or intervention which requires more than 1 variable for its representation, preventing its inclusion as a supplemental qualifier**

The need to represent data which require more than 1 variable in a findings about structure, rather than by adding 2 or more supplemental qualifiers to the parent record, is the basis for this criterion.

**Criterion 3: Data or information that indicate the occurrence of pre-specified AEs**

Previous versions of the SDTMIG included the criterion, "Data or observations about an Event or Intervention for which no Event or Intervention record exists." This criterion has been removed from the SDTMIG, as data that were formerly represented by this criterion can now be best represented using only the FA domain.

Previous versions of the SDTMIG included the criterion, "Data or information about an Event or Intervention that indicates the occurrence of a pre-specified AE." This criterion is being replaced with Criterion 3 above.

an event or interventions record. If data do meet criteria to be represented in the findings about structure, FAOBJ will be populated with the name of the event or intervention about which the finding was made.

The term "symptom" is often used loosely to refer to both symptoms (reported by the subject) and signs (observable by others). While SDTM does not specifically differentiate between symptoms and signs, the discussion above refers to findings about an event, where those findings can be symptoms or signs.

**Points to Consider**

The choice between representing a data item as a supplemental qualifier or as a finding about an event or intervention may not always be obvious. Here are some considerations:

- Does the data item have its own timing, separate from the timing of the event or intervention? If the data item represents a specific observation at a specific time, the FA structure may be appropriate.
- Are there several items which would be clearer if they could be grouped together? If so, the FA structure allows the use of FACAT and FASCAT to group related items.
- Is the data item alone in a particular study, but related to other data items likely to be collected in other studies? If so, the FA structure may be preferable for consistency.
- Are there multiple evaluators for a data item that could otherwise be represented as a supplemental qualifier? If so, FA is more appropriate.

## §6.4.2 Naming Findings About Domains

## §6.4.3 Variables Unique to Findings About

## §6.4.4 FA – Description/Overview

A findings domain that contains the findings about an event or intervention that cannot be represented within an events or interventions record.

## §6.4.5 Skin Response (SR)
