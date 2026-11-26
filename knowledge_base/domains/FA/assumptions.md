# FA — Assumptions

## §6.4 Findings About Events or Interventions

Findings About Events or Interventions is a specialization of the Findings general observation class. As such, it shares all qualities and conventions of Findings observations but is specialized by the addition of the --OBJ variable.

## §6.4.1 When to Use Findings About Events or Interventions

The Findings About Events or Interventions structure (or "FA structure") is intended, as its name implies, to be used when collected data represent “findings about” an event or intervention that cannot be represented within an event or intervention record or as a supplemental qualifier to such a record. Not all findings associated with an event or intervention should be represented in the FA structure. The following are criteria for using the FA structure.

**Criterion 1:** Data or observations that have different timing from an associated event or intervention as a whole

Per Section 6.2.1, Adverse Events, assumption 7.e, "It is the sponsor's responsibility to define an event." One common practice is to define an event as the period of time during which an adverse event has a constant severity (or, sometimes, other properties). In this approach, a single medical condition may be represented by multiple AE records (see AE Example 4), each with a start and end date, and FA records with a test of severity would not be applicable. Another common practice is to define an adverse event as the whole of a medical condition, even if severity (and other properties) change over time. With this approach, FA records may be used to represent data about severity (or other properties) of the adverse event that have timing different from the medical condition as a whole.

A finding that is about part of an event, rather than the event as a whole, meets this criterion for the use of FA. An assessment of an event that is not about the whole of an event may be a "snapshot," an assessment at a point in time, or a "slice," an assessment over a period of time (i.e., evaluation interval) during the event. In Section 6.4.4, Findings About Events or Interventions, Example 1 shows snapshot assessments at 3 points in time. The timing variables used to represent a snapshot assessment generally include FADTC, along with visit and time point variables as applicable, but not FAEVLINT or FAEVINTX. FA Example 5 shows assessments over 24-hour slices of the event. Slice assessments use an evaluation interval, so the timing variables used would generally include FADTC and either FAEVLINT or FAEVINTX.

Repeated assessments of disease or treatment-related symptoms, particularly symptoms that are likely to be intermittent, generally produce results that apply to only part of an event; these are represented as findings about clinical events. For example, if severity of an AE is collected at scheduled time points (e.g., per visit) throughout the duration of the AE, as in Section 6.4.4, Findings About Events or Interventions, Example 6, the severities have timing that are different from that of the AE as a whole. Instead, the collected severities represent snapshots or slices of the AE over time.

Occasionally, data collection will include questions about the occurrence of prespecified events which are of naturally short duration, so that even though the assessments are repeated during the study, each assessment will provide information about an event as a whole. These type of assessments can be represented in the Events domain.

A finding which is a summary of multiple occurrences of a particular kind of event meets this criterion. For example, the number of episodes of vomiting during a particular time period is a finding about vomiting.

For events that have not ended at the time of an assessment, "event as a whole" means the event up to the time of the assessment. An event need not have ended for information about the event to be considered information about the event as a whole. Data about medical conditions collected before start of study treatment are usually about the event as a whole and are usually represented in Medical History (MH). See Section 6.4.4, Findings About Events or Interventions, Example 3.

Assessments of parts of events (snapshots or slices) are represented in FA and may or may not have parent records (e.g., FA Example 5). If the FA dataset is split by parent domain, the sponsor must decide which Events domain would have held a parent record for a parent-less FA record. A sponsor may consider that symptoms of the disease under study would be considered clinical events represented in the CE domain, so that FA records for symptoms of the disease under study would be in the FACE split of the FA domain.

This criterion is less likely to apply to interventions records than to events records. Interventions records often represent a series of individual substance administrations. When there is a change in dosing or other characteristics during the series, the most appropriate solution may be to represent the series of individual administrations in 2 records, one for the administrations before the change and a second for administrations after the change, rather than to create findings about records.

**Criterion 2:** An observation about an event or intervention which requires more than 1 variable for its representation, particularly when the observation may be represented with Findings class variables (e.g., units, method)

The need to represent data which require more than 1 variable in a findings about structure, rather than by adding 2 or more supplemental qualifiers to an Events or Interventions domain, is driven by the fact that each supplemental qualifier is in a separate record that links only to the parent record. For example, if the size of a rash is measured, then the result and measurement unit (e.g., centimeters, inches) can be represented in an FA domain in a single record; other information regarding the rash (e.g., start and end times) would, if collected, appear in an Event record. See, for example, the longest diameter measurements in Section 6.4.4, Findings About Events or Interventions, Example 2.

**Criterion 3:** Data or information that indicate the occurrence of pre-specified AEs

Every record in the AE domain must represent an event that actually occurred. Therefore, AE probing questions that are answered in the negative (e.g., did not occur, unknown, not done) cannot be stored in the AE domain. All answers to probing questions about the occurrence of pre-specified adverse events can be stored in the FA domain. (See Section 6.4.4, Findings About Events or Interventions, Example 4.) For each "Y" response to a probing question there should be a record in the AE domain. The FA record and the AE record may be linked via RELREC. The responses to all AE occurrence questions—whether "Y", "N", or "NOT DONE"—are represented in FAAE. This approach supports summarization of incidence directly from the FA dataset.

Previous versions of the SDTMIG included the criterion, "Data or observations about an Event or Intervention for which no Event or Intervention record has been collected or created." This criterion has been removed, because the amount of data collected about an event or intervention should not determine whether data are represented in an FA dataset. Data that can be represented in an event or intervention record, particularly data for which standard variables exist, should be represented in the appropriate Event or Intervention domain, even if the record is sparse. The absence of a "parent" event or intervention record does not prevent representing data about an event or intervention in an FA dataset. One situation that previously used this criterion was the collection of a diagnosis date or symptom onset date for the disease under study when the occurrence of the disease was collected in an inclusion criterion, rather than as medical history. That situation can now be represented in an MH record that includes MHEVDTYP. Events identified during a physical examination would, in accordance with CDASH best practices, be recorded in medical history or adverse events CRFs.

Previous versions of the SDTMIG included the criterion, "Data or information about an Event or Intervention that indicate the occurrence of related symptoms or therapies." This criterion has been removed because information about related symptoms or therapies is more appropriately represented as information about those symptoms or therapies rather than as information about the event or intervention to which they are thought be related. Data about related symptoms or interventions should be evaluated against the above Criterion 1 - 3 to determine whether they should be represented in an FA dataset. If data do not meet one of the criteria above, they should be represented in an event or interventions record. If data do meet criteria to be represented in the findings about structure, FAOBJ will be the name of the symptom. The relationship to the disease under study may be represented in FACAT or FASCAT, as in FA Example 5.

The term "symptom" is often used loosely to refer to both symptoms (reported by the subject) and signs (observable by others). When data about signs is collected via questions about the subject's past experience, signs are appropriately represented as SDTM events. However, when a sign is identified or assessed during an examination at a point in time, it may be more appropriate to represent it as an SDTM finding.

**Points to Consider**

The choice between representing a data item as a supplemental qualifier or as a finding about an event or intervention may not be clear-cut. The following questions may help in making a decision.

- Does the data item have its own timing, separate from the timing of the event or intervention? If the data item represents some action during or after the event or intervention, it may be considered to have its own timing, and meet Criterion 1.
  - If the event or intervention is a disease milestone, then RELMIDS is not included in this event or intervention record. Is the relationship of a data item to the disease milestone (RELMIDS) needed? If so, it can be represented in FA, but not as a supplemental qualifier to the parent record.
- Are there several items which would be clearer if they could be grouped together? If so, the FA structure allows the use of FAGRPID, FACAT, or FASCAT to group the items.
- Is the data item alone in a particular study, but related to other data items likely to be collected in other studies? If so, it may be preferable to represent the item in FA, where other FA variables might be needed for related items in the future. For example, the response to "Was a rechallenge conducted?" might be represented as a supplemental qualifier, but if additional information about the rechallenge (e.g., When?, What was the result?) were collected, then the FA structure would be needed.
- Are there multiple evaluators for a data item that could otherwise be represented as a supplemental qualifier? If so, FA may provided a clearer representation of the multiple opinions, and would also allow the use of FAEVALID.

## §6.4.2 Naming Findings About Domains

Findings About domains are defined to store findings about events or interventions. Sponsors may choose to represent FA data collected in the study in a single FA dataset (potentially splitting the FA domain into physically separate datasets following the guidance described in Section 4.1.6, Additional Guidance on Dataset Naming), or separate datasets, assigning unique custom 2-character domain codes (see examples in Section 6.4.5, Skin Response).

For example, if findings about clinical events and findings about medical history are collected in a study, these could be represented as:

1. A single FA domain, perhaps separated with different FACAT and/or FASCAT values
2. A split FA domain following the guidance in Section 4.1.7, Splitting Domains:
   - The DOMAIN value would be “FA”.
   - Variables that require a prefix would use “FA”.
   - The dataset names would be the domain name plus up to 2 additional characters indicating the parent domain (e.g., FACE for Findings About Clinical Events, FAMH for Findings About Medical History). This naming convention may be used for an FA domain that has a parent domain even when the study has only 1 FA dataset that is not being split.
   - FASEQ must be unique within USUBJID for all records across the split datasets.
   - Supplemental qualifier datasets would need to be managed at the split-file level (e.g., suppface.xpt, suppfamh.xpt). Within each supplemental qualifier dataset, RDOMAIN would be "FA".
   - If a dataset-level RELREC is defined (e.g., between the CE and FACE datasets), then RDOMAIN may contain up to 4 characters to effectively describe the relationship between the CE parent records and the FACE child records.
3. Separate domains where:
   - The DOMAIN value is sponsor-defined and does not begin with FA, following examples in Section 6.4.5, Skin Response, which has a domain code of SR.
   - All published FA guidance applies, specifically:
     - The --OBJ variable cannot be added to a standard Findings domain. A domain is either a Findings domain or a Findings About domain, not one or the other depending on the situation.
     - When the --OBJ variable is included in a domain, this identifies it as an FA domain, and the --OBJ variable must be populated for all records.
   - All published domain guidance applies, specifically:
     - Variables that require a prefix would use the 2-character domain code chosen.

For the naming of datasets with findings about events or interventions for associated persons, refer to the SDTMIG: Associated Persons (available at https://www.cdisc.org/standards/foundational/sdtm).

## §6.4.3 Variables Unique to Findings About

The variable --OBJ is unique to Findings About. In conjunction with FATESTCD, it describes what the topic of the observation is; therefore, both are required to be populated for every record. FATESTCD describes the measurement/evaluation and FAOBJ describes the event or intervention that the measurement/evaluation is about.

When collected data fit a qualifier variable (see SDTM Sections 3.1.1, 3.1.2, and 3.1.3) and are represented in the FA domain, the name of the variable should be used as the value of FATESTCD. For example,

| FATESTCD | FATEST |
|----------|--------|
| OCCUR | Occurrence Indicator |
| SEV | Severity/Intensity |
| TOXGR | Toxicity Grade |

The use of the same names (e.g., SEV, OCCUR) for both qualifier variables in the observation classes and FATESTCD is deliberate, but should not lead users to conclude that the collection of such data (e.g., severity/intensity, occurrence) must be stored in the FA domain. In fact, data should only be stored in the FA domain if they do not fit in the general observation-class domain. If the data describe the underlying event or intervention as a whole and share its timing, then the data should be stored as a qualifier of the general observation-class record.

A record in FA may or may not have a parent record in an events or interventions domain. If an FA record does have a parent record, the value in FAOBJ should match the value in --TERM or --TRT, unless the parent domain is dictionary coded or subject to controlled terminology, in which case FAOBJ should match the value in --DECOD.

Examples for the FA and Skin Response (SR) domains include the use of RELREC to represent the relationship between an FA domain and a parent domain.

## §6.4.4 FA – Description/Overview

A findings domain that contains the findings about an event or intervention that cannot be represented within an events or interventions domain record or as a supplemental qualifier.

## FA – Specification

fa.xpt, Findings About Events or Interventions — Findings About. One record per finding, per object, per time point, per visit per subject, Tabulation.

## FA – Assumptions

1. The Findings About domain shares all qualities and conventions of findings observations.

2. See Section 6.4.1, When to Use Findings About Events or Interventions; and Section 8.6.3, Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions; for guidance on deciding between the use of the FA domain and other SDTM structures.

3. See Section 6.4.2, Naming Findings About Domains, for advice on splitting the FA domain.

4. Some variables in the events and interventions domains (e.g., OCCUR, SEV, TOXGR) represent findings about the whole of the event or intervention. When FA is used to represent findings about a part of the event or intervention (i.e., the assessment has different timing from the event as a whole), the FATEST and FATESTCD values should be the same as the variable name and variable label in the corresponding event or intervention domain. See Section 6.4.3, Variables Unique to Findings About.
   a. Associations between some findings about cardiovascular interventions or events and their response codelists are described in the CV codetable, available at https://www.cdisc.org/standards/terminology/controlled-terminology.

5. When data collection establishes a relationship between FA records and an events or interventions record, the relationship should be represented in RELREC.
   a. The FAOBJ variable alone is not sufficient to establish a relationship, because an events or interventions dataset may have multiple records for the same topic (e.g., --TERM or --DECOD, --TRT or --DECOD).

6. Any Identifier variables, Timing variables, or Findings general observation-class qualifiers may be added to the FA domain, but the following qualifiers should generally not be used: --BODSYS, --MODIFY, --SEV, --TOXGR.

## §6.4.5 Skin Response (SR)

> See [SR – Assumptions](../SR/assumptions.md) for §6.4.5 Skin Response.
