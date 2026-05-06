# SDTMIG v3.4 --- Trial Design Model Datasets — Part 1

> **Source:** SDTMIG v3.4-FINAL_2022-07-21.pdf | **Version:** 3.4 Final | **Date:** 2021-11-29
> **Part of:** SDTM Implementation Guide for Human Clinical Trials
> **Split:** Part 1/2 — 7.1-7.2: Introduction, Experimental Design (TA, TE)
> **Original:** `SDTMIG34_08_TrialDesign.md`
> **Related:** `SDTMIG34_08b_TrialDesign.md`

---

## 7 Trial Design Model Datasets


### 7.1 Introduction to Trial Design Model Datasets


#### 7.1.1 Purpose of the Trial Design Model

ICH E3, Guidance for Industry, Structure and Content of Clinical Study Reports (available at [http://www.ich.org/products/guidelines/](http://www.ich.org/products/guidelines/)), Section 9.1, calls for a brief, clear description of the overall plan and design of the study, and supplies examples of charts and diagrams for this purpose in Annex IIIa and Annex IIIb.

Each Annex corresponds to an example trial, and each shows a diagram describing the study design and a table showing the schedule of assessments. The Trial Design Model provides a standardized way to describe those aspects of the planned conduct of a clinical trial shown in the study design diagrams of these examples. The standard Trial Design Datasets will allow reviewers to:

- Clearly and quickly grasp the design of a clinical trial
- Compare the designs of different trials
- Search a data warehouse for clinical trials with certain features
- Compare planned and actual treatments and visits for subjects in a clinical trial

Modeling a clinical trial in this standardized way requires the explicit statement of certain decision rules that may not be addressed or may be vague or ambiguous in the usual prose protocol document. Prospective modeling of the design of a clinical trial should lead to a clearer, better protocol. Retrospective modeling of the design of a clinical trial should ensure a clear description of how the trial protocol was interpreted by the sponsor.

#### 7.1.2 Definitions of Trial Design Concepts

A clinical trial is a scientific experiment involving human subjects, intended to address certain scientific questions (i.e., the objectives of the trial). See the CDISC Glossary (https://www.cdisc.org/standards/glossary) for more complete definitions of clinical trial and objective.

| Concept | Definition |
| --- | --- |
| Trial design | The design of a clinical trial is a plan for what will be done to subjects and what data will be collected about them, in the course of the trial, to address the trial's objectives. |
| Epoch | As part of the design of a trial, the planned period of subjects' participation in the trial is divided into epochs. Each epoch is a period of time that serves a purpose in the trial as a whole. That purpose will be at the level of the primary objectives of the trial. Typically, the purpose of an epoch will be to expose subjects to a treatment or to prepare for such a treatment period (e.g., determine subject eligibility, washout previous treatments), or to gather data on subjects after a treatment has ended.<br><br>Note that at this high level, a "treatment" is a treatment strategy, which may be simple (e.g., exposure to a single drug at a single dose) or complex. Complex treatment strategies could involve tapering through several doses, titrating dose according to clinical criteria, complex regimens involving multiple drugs, or strategies for adding or dropping drugs according to clinical criteria. |
| Arm | An arm is a planned path through the trial. This path covers the entire time of the trial. The group of subjects assigned to a planned path is also often colloquially called an "arm." The group of subjects assigned to an arm is also often called a "treatment group"; in this sense, an arm is equivalent to a treatment group. |
| Study cell | Each planned path through the trial (i.e., each arm) is divided into pieces, 1 for each epoch. Each of these pieces is called a study cell. Thus, there is a study cell for each combination of arm and epoch.<br><br>Each study cell represents an implementation of the purpose of its associated epoch. For an epoch whose purpose is to expose subjects to treatment, each study cell associated with the epoch has an associated treatment strategy. For example, a 3-arm parallel trial might have a treatment epoch whose purpose is to expose subjects to one of 3 study treatments: placebo, investigational product, or active control. There would be 3 study cells associated with the treatment epoch, 1 for each arm. Each of these study cells exposes the subject to 1 of the 3 study treatments. Another example involving more complex treatment strategies would be a trial comparing the effects of cycles of chemotherapy drug A given alone or in combination with drug B, where drug B is given as a pretreatment to each cycle of drug A. |
| Element | An element is a basic building block in the trial design. It involves administering a planned intervention, which may be treatment or no treatment, during a period of time. Elements for which the planned intervention is "no treatment" would include elements for screening, washout, and follow-up. |
| Study cells and elements | Many (perhaps most) clinical trials involve a single, simple administration of a planned intervention within a study cell. For some trials, however, the treatment strategy associated with a study cell involves a complex series of administrations of treatment. In such cases it may be important to track the component steps in a treatment strategy operationally; secondary objectives and safety analyses also might require that data be grouped by the treatment step during which it was collected. The steps within a treatment strategy may involve different doses of drug, different drugs, or different kinds of care (e.g., preoperative, operative, and post-operative periods surrounding surgery). When the treatment strategy for a study cell is simple, the study cell will contain a single element, and for many purposes there is little value in distinguishing between the study cell and the element. However, when the treatment strategy for a study cell consists of a complex series of treatments, a study cell can contain multiple elements. There may be a fixed sequence of elements, or a repeating cycle of elements, or some other complex pattern. In these cases, the distinction between a study cell and an element is very useful. |
| Branch | In a trial with multiple arms, the protocol plans for each subject to be assigned to 1 arm. The time within the trial at which this assignment takes place is the point at which the arm paths of the trial diverge, and so is called a branch point. For many trials, the assignment to an arm happens all at one time, so the trial has 1 branch point. For other trials, there may be 2 or more branches that collectively assign a subject to an arm. The process that makes this assignment may be a randomization, but it need not be. |
| Treatments | The word "treatment" may be used in connection with epochs, study cells, or elements, but has somewhat different meanings in each context:<br><br>- Because epochs cut across arms, an epoch treatment is at a high level that does not specify anything that differs between arms. For example, in a 3-period crossover study of 3 doses of drug X, each treatment epoch is associated with drug X, but not with a specific dose.<br>- A study cell treatment is specific to a particular arm. For example, a parallel trial might have study cell treatments placebo and drug X, without any additional detail (e.g., dose, frequency, route of administration) being specified. A study cell treatment is at a relatively high level, the level at which treatments might be planned in an early conceptual draft of the trial, or in the title or objectives of the trial.<br>- An element treatment may be fairly detailed. For example, for an element representing a cycle of chemotherapy, element treatment might specify 5 daily 100 mg doses of drug X.<br><br>The distinctions between these levels are not rigid, and depend on the objectives of the trial. For example, route is generally a detail of dosing, but in a bioequivalence trial comparing IV and oral administration of drug X, route is clearly part of study cell treatment. |
| Visit | The notion of a visit, a clinical encounter, derives from trials with outpatients, where subjects interact with the investigator during visits to the investigator's clinical site. However, the term is used in other trials, where a trial visit may not correspond to a physical visit. For example, in a trial with inpatients, time may be subdivided into visits, even though subjects are in hospital throughout the trial. For example, data for a screening visit may be collected over the course of more than 1 physical visit. One of the main purposes of visits is the performance of assessments, but not all assessments need take place at clinic visits; some assessments may be performed by means of telephone contacts, electronic devices, or call-in systems. The protocol should specify what contacts are considered visits and how they are defined. |

#### 7.1.3 Current and Future Contents of the Trial Design Model

Datasets currently in the Trial Design Model include:

- Trial Arms: Describes the sequences of elements in each epoch for each arm, and thus describes the complete sequence of elements in each arm
- Trial Elements: Describes the elements used in the trial
- Trial Visits: Describes the planned schedule of visits
- Trial Disease Assessment: Provides information on the protocol-specified disease assessment schedule, and is used for comparison with the actual occurrence of the efficacy assessments in order to determine whether there was good compliance with the schedule
- Trial Disease Milestones: Describes observations or activities identified for the trial which are anticipated to occur in the course of the disease under study and which trigger the collection of data
- Trial Inclusion/Exclusion Criteria: Describes the criteria used to screen subjects
- Trial Summary: Lists key facts (parameters) about the trial that are likely to appear in a registry of clinical trials

The Trial Inclusion/Exclusion Criteria (TI) dataset is discussed in Section 7.4.1, Trial Inclusion/Exclusion Criteria.

The Inclusion/Exclusion Criteria Not Met (IE) domain described in Section 6.3.4, Inclusion/Exclusion Criteria Not Met, contains the actual exceptions to those criteria for enrolled subjects.

The current Trial Design Model has limitations in representing protocols, which include:

- Plans for indefinite numbers of repeating elements (e.g., indefinite numbers of chemotherapy cycles)
- Indefinite numbers of visits (e.g., periodic follow-up visits for survival)
- Indefinite numbers of epochs
- Indefinite numbers of arms

The last 2 situations arise in dose-escalation studies where increasing doses are given until stopping criteria are met.

Some dose-escalation studies enroll a new cohort of subjects for each new dose, and so, at the planning stage, have an indefinite number of arms. Other dose-escalation studies give new doses to a continuing group of subjects, and so are planned with an indefinite number of epochs.

There may also be limitations in representing other patterns of Elements within a Study Cell that are more complex than a simple sequence. For the purpose of submissions about trials that have already completed, these limitations are not critical, so it is expected that development of the Trial Design Model to address these limitations will have a minimal impact on the SDTM.

### 7.2 Experimental Design (TA and TE)

This subsection contains the Trial Design datasets that describe the planned design of the study, and provide the representation of study treatment in its most granular components (Section 7.2.2, Trial Elements (TE)), as well as the representation of all sequences of these components (Section 7.2.1, Trial Arms (TA)) as specified by the study protocol.
The TA and TE datasets are interrelated, and they provide the building blocks for the development of subject-level treatment information (see Sections 5.2, Demographics (DM), and 5.3, Subject Elements (SE), for the subject’s actual study treatment information).

#### 7.2.1 Trial Arms (TA)

##### TA – Description/Overview
A trial design domain that contains each planned arm in the trial. This section contains:

- The Trial Arms dataset and assumptions
- A series of example trials, which illustrate the development of the TA dataset
- Advice on various issues in the development of the TA dataset
- A recap of the TA dataset and the function of its variables

##### TA – Specification
ta.xpt, Trial Arms — Trial Design. One record per planned Element per Arm, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
| --- | --- | --- | --- | --- | --- | --- |
| STUDYID | Study Identifier | Char | Identifier |  | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | TA | Identifier | Two-character abbreviation for the domain. | Req |
| ARMCD | Planned Arm Code | Char | * | Topic | ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than that for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. | Req |
| ARM | Description of Planned Arm | Char | * | Synonym Qualifier | Name given to an arm or treatment group. | Req |
| TAETORD | Planned Order of Element within Arm | Num |  | Timing | Number that gives the order of the element within the arm. | Req |
| ETCD | Element Code | Char | * | Record Qualifier | ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name. | Req |
| ELEMENT | Description of Element | Char | * | Synonym Qualifier | The name of the element. The same element may occur more than once within an arm. | Perm |
| TABRANCH | Branch | Char |  | Rule | Condition subject met, at a "branch" in the trial design at the end of this element, to be included in this arm (e.g., "Randomization to DRUG X"). | Exp |
| TATRANS | Transition Rule | Char |  | Rule | If the trial design allows a subject to transition to an element other than the next element in sequence, then the conditions for transitioning to those other elements, and the alternative element sequences, are specified in this rule (e.g., "Responders go to washout"). | Exp |
| EPOCH | Epoch | Char | (EPOCH) | Timing | Name of the trial epoch with which this element of the arm is associated. | Req |

1 In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

##### TA – Assumptions
1. TAETORD is an integer. In general, the value of TAETORD is 1 for the first element in each arm, 2 for the second element in each arm, and so on. Occasionally, it may be convenient to skip some values (see Example Trial 6). Although the values of TAETORD need not always be sequential, their order must always be the correct order for the elements in the arm path.
2. Elements in different arms with the same value of TAETORD may or may not be at the same time, depending on the design of the trial. The example trials illustrate a variety of possible situations. The same element may occur more than once within an arm.
3. TABRANCH describes the outcome of a branch decision point in the trial design for subjects in the arm. A branch decision point takes place between epochs, and is associated with the element that ends at the decision point. For instance, if subjects are assigned to an arm where they receive treatment A through a randomization at the end of element X, the value of TABRANCH for element X would be "Randomized to A."
4. Branch decision points may be based on decision processes other than randomizations (e.g., clinical evaluations of disease response, subject choice).
5. There is usually some gap in time between the performance of a randomization and the start of randomized treatment. However, in many trials this gap in time is small and it is highly unlikely that subjects will leave the trial between randomization and treatment. In these circumstances, the trial does not need to be modeled with this time period between randomization and start of treatment as a separate element.
6. Some trials include multiple paths that are closely enough related so that they are all considered to belong to 1 arm. In general, this set of paths will include a "complete" path along with shorter paths that skip some elements. The sequence of elements represented in the trial arms should be the complete, longest path. TATRANS describes the decision points that may lead to a shortened path within the arm.
7. If an element does not end with a decision that could lead to a shortened path within the arm, then TATRANS will be blank. If there is such a decision, TATRANS will be in a form like, "If condition X is true, then go to epoch Y" or "If condition X is true, then go to element with TAETORD = 'Z'".
8. EPOCH is not strictly necessary for describing the sequence of elements in an arm path, but it is the conceptual basis for comparisons between arms and also provides a useful way to talk about what is happening in a blinded trial while it is blinded. During periods of blinded treatment, blinded participants will not know which arm and element a subject is in, but EPOCH should provide a description of the time period that does not depend on knowing arm.
9. EPOCH should be assigned in such a way that elements from different arms with the same value of EPOCH are "comparable" in some sense. The degree of similarity across arms varies considerably in different trials, as illustrated in the examples.
10. EPOCH values for multiple similar epochs:
    a. When a study design includes multiple epochs with the same purpose (e.g., multiple similar treatment epochs), it is recommended that the EPOCH values be terms from controlled terminology, but with numbers appended. For example, multiple treatment epochs could be represented using "TREATMENT 1", "TREATMENT 2", and so on. Because the codelist is extensible, this convention allows multiple similar epochs to be represented without adding numbered terms to the CDISC Controlled Terminology for epoch. The inclusion of multiple numbered terms in the EPOCH codelist is not considered to add value.
    b. Note that the controlled terminology does include some more granular terms for distinguishing between epochs that differ in ways other than mere order, and these terms should be used where applicable, as they are more informative. For example, when "BLINDED TREATMENT" and "OPEN LABEL TREATMENT" are applicable, those terms would be preferred over "TREATMENT 1" and "TREATMENT 2".
11. Note that study cells are not explicitly defined in the TA dataset. A set of records with a common value of both ARMCD and EPOCH constitute the description of a study cell. Transition rules within this set of records are also part of the description of the study cell.
12. EPOCH may be used as a timing variable in other datasets, such as Exposure (EX) and Disposition (DS), and values of EPOCH must be different for different epochs. For instance, in a crossover trial with 3 treatment epochs, each must be given a distinct name; all 3 cannot be called "TREATMENT".
##### TA – Examples
The core of the Trial Design Model is the TA dataset. For each arm of the trial, the TA dataset contains 1 record for each occurrence of an element in the path of the arm.

Although the TA dataset has 1 record for each trial element traversed by subjects assigned to the arm, it is generally more useful to work out the overall design of the trial at the study cell level first, then to work out the elements within each study cell, and finally to develop the definitions of the elements that are contained in the Trial Elements (TE) table.

When working out the design of a trial, it is generally useful to draw diagrams such as those mentioned in ICH E3. The protocol may include a diagram that can serve as a starting point. Such a diagram can then be converted into a trial design matrix that displays the study cells and which in turn can be converted into the TA dataset.

This section uses example trials of increasing complexity to illustrate the concepts of trial design. For each example trial, the process of working out the TA table is illustrated by means of a series of diagrams and tables, including:

- A diagram showing the branching structure of the trial in a "study schema" format such as might appear in a protocol.
- A diagram that shows the "prospective" view of the trial (i.e., the view of those participating in the trial). This is similar to the study schema view in that it usually shows a single pool of subjects at the beginning of the trial, with the pool of subjects being split into separate treatment groups at randomizations and other branches. Such diagrams include the epochs of the trial, and, for each group of subjects and each epoch, the sequence of elements within each epoch for that treatment group. The arms are also indicated on these diagrams.
- A diagram that shows the "retrospective" view of the trial (i.e., the view of the analyst reporting on the trial). This style of diagram looks more like a matrix; it is also more like the structure of the TA dataset. The retrospective view is arm-centered and shows, for each study cell (epoch or arm combination), the sequence of elements within that study cell. It can be thought of as showing, for each arm, the elements traversed by a subject who completed that arm as intended.
- If the trial is blinded, a diagram that shows the trial as it appears to a blinded participant.
- A trial design matrix, an alternative format for representing most of the information in the diagram that shows arms and epochs, and which emphasizes the study cells.
- The TA dataset.

The original PDF includes diagrams associated with each example. The Markdown version below preserves the accompanying explanatory text, trial design matrices, and `ta.xpt` examples.

Example 1 should be reviewed before reading other examples, as it explains the conventions used for all diagrams and tables in the examples.

###### Example 1

Diagrams that represent study schemas generally conceive of time as moving from left to right, using horizontal lines to represent periods of time and slanting lines to represent branches into separate treatments, convergence into a common follow-up, or crossover to a different treatment.

In this type of document, diagrams are drawn using "blocks" corresponding to trial elements rather than horizontal lines. Trial elements are the various treatment and non-treatment time periods of the trial and we want to emphasize the separate trial elements that might otherwise be "hidden" in a single horizontal line. See Section 7.2.2, Trial Elements (TE), for more information about defining trial elements. In general, the elements of a trial will be fairly clear. However, in the process of working out a trial design, alternative definitions of trial elements may be considered, in which case diagrams for each alternative may be constructed.

In the study schema diagrams in this example, the only slanting lines used are those that represent branches (i.e., decision points where subjects are divided into separate treatment groups). One advantage of this style of diagram, which does not show convergence of separate paths into a single block, is that the number of arms in the trial can be determined by counting the number of parallel paths at the right end of the diagram.

As illustrated in the study schema diagram for Example Trial 1, this simple parallel trial has 3 arms, corresponding to the 3 possible left-to-right paths through the trial. Each path corresponds to 1 of the 3 treatment elements at the right end of the diagram. Randomization is represented by the 3 red arrows leading from the Run-in block.

The next diagram for this trial shows the 3 epochs of the trial, indicates the 3 arms, and shows the sequence of elements for each group of subjects in each epoch. The arrows are at the right side of the diagram because it is at the end of the trial that all the separate paths through the trial can be seen. Note that, in this diagram, randomization, which was shown using 3 red arrows connecting the Run-in block with the 3 treatment blocks in the first diagram, is indicated by a note with an arrow pointing to the line between 2 epochs.

The next diagram can be thought of as the retrospective view of a trial, the view back from a point in time when a subject's assignment to an arm is known. In this view, the trial appears as a grid, with an arm represented by a series of study cells, one for each epoch, and a sequence of elements within each study cell. In this example, as in many trials, there is exactly 1 element in each study cell. Later examples will illustrate that this is not always the case.

The next diagram shows the trial from the viewpoint of blinded participants. To blinded participants in this trial, all arms look alike. They know when a subject is in the screen element or the run-in element, but when a subject is in the treatment epoch, participants know only that the subject is receiving a study drug, not which study drug, and therefore not which element.

A trial design matrix is a table with a row for each arm in the trial and a column for each epoch in the trial. It is closely related to the retrospective view of the trial, and many users may find it easier to construct a table than to draw a diagram. The cells in the matrix represent the study cells, which are populated with trial elements. In this trial, each study cell contains exactly 1 element.

As illustrated in the following table, the columns of a trial design matrix are the epochs of the trial, the rows are the arms of the trial, and the cells of the matrix, the study cells, contain elements. Note that randomization is not represented in the trial design matrix. All of the preceding diagrams and the trial design matrix are alternative representations of the trial design. None of them contains all the information that will be in the finished TA dataset; users may find it useful to draw some or all of these diagrams when working out the dataset.

**Trial Design Matrix**

| Arm | Screen | Run-in | Treatment |
| --- | --- | --- | --- |
| Placebo | Screen | Run-in | PLACEBO |
| A | Screen | Run-in | DRUG A |
| B | Screen | Run-in | DRUG B |

For Example Trial 1, the conversion of the trial design matrix into the TA dataset is straightforward. For each cell of the matrix, there is a record in the TA dataset. `ARM`, `EPOCH`, and `ELEMENT` can be populated directly from the matrix. `TAETORD` acts as a sequence number for the elements within an arm, so it can be populated by counting across the cells in the matrix. The randomization information, which is not represented in the trial design matrix, is held in `TABRANCH` in the TA dataset. `TABRANCH` is populated only if there is a branch at the end of an element for the arm. When `TABRANCH` is populated, it describes how the decision at the branch point would result in a subject being in this arm.

`ta.xpt`

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX1 | TA | P | Placebo | 1 | SCRN | Screen |  |  | SCREENING |
| 2 | EX1 | TA | P | Placebo | 2 | RI | Run-In | Randomized to Placebo |  | RUN-IN |
| 3 | EX1 | TA | P | Placebo | 3 | P | Placebo |  |  | TREATMENT |
| 4 | EX1 | TA | A | A | 1 | SCRN | Screen |  |  | SCREENING |
| 5 | EX1 | TA | A | A | 2 | RI | Run-In | Randomized to Drug A |  | RUN-IN |
| 6 | EX1 | TA | A | A | 3 | A | Drug A |  |  | TREATMENT |
| 7 | EX1 | TA | B | B | 1 | SCRN | Screen |  |  | SCREENING |
| 8 | EX1 | TA | B | B | 2 | RI | Run-In | Randomized to Drug B |  | RUN-IN |
| 9 | EX1 | TA | B | B | 3 | B | Drug B |  |  | TREATMENT |

###### Example 2

The following diagram for a crossover trial does not use the crossing slanted lines sometimes used to represent crossover trials, because the order of the blocks is sufficient to represent the design of the trial. Slanted lines are used only to represent the branch point at randomization, when a subject is assigned to a sequence of treatments. As in most crossover trials, the arms are distinguished by the order of treatments, with the same treatments present in each arm. Note that even though all 3 arms of this trial end with the same block, i.e., the block for the follow-up element, the diagram does not show the arms converging into one block. Also note that the same block, the `Rest` element, occurs twice within each arm. Elements are conceived of as reusable and can appear in more than 1 arm, in more than 1 epoch, and more than once in an arm.

The next diagram for this crossover trial shows the prospective view of the trial; it identifies the epoch and arms of the trial, and gives each a name. As for most crossover studies, the objectives of the trial will be addressed by comparisons between the arms and by within-subject comparisons between treatments. Because the design depends on differentiating the periods during which the subject receives the 3 different treatments, there are 3 different treatment epochs. The fact that the rest periods are identified as separate epochs suggests that these also play an important part in the design of the trial; they are probably designed to allow subjects to return to baseline, with data collected to show that this occurred. Note that epochs are not considered reusable; each epoch has a different name, even though all the treatment epochs are similar and both the rest epochs are similar. As with the first example trial, there is a one-to-one relationship between the epochs of the trial and the elements in each arm.

The next diagram shows the retrospective view of the trial.

The last diagram for this trial shows the trial from the viewpoint of blinded participants. As in the simple parallel trial in Example Trial 1, blinded participants see only 1 sequence of elements; during the treatment epochs they do not know which of the treatment elements a subject is in.

The following table illustrates the trial design matrix for this crossover example trial. It corresponds closely to the preceding retrospective diagram.

**Trial Design Matrix**

| Arm | Screen | First Treatment | First Rest | Second Treatment | Second Rest | Third Treatment | Follow-up |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P-5-10 | Screen | Placebo | Rest | 5 mg | Rest | 10 mg | Follow-up |
| 5-P-10 | Screen | 5 mg | Rest | Placebo | Rest | 10 mg | Follow-up |
| 5-10-P | Screen | 5 mg | Rest | 10 mg | Rest | Placebo | Follow-up |

It is straightforward to produce the TA dataset for this crossover trial from the diagram showing arms and epochs, or from the trial design matrix.

`ta.xpt`

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 1 | SCRN | Screen | Randomized to Placebo - 5 mg - 10 mg |  | SCREENING |
| 2 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 2 | P | Placebo |  |  | TREATMENT 1 |
| 3 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 3 | REST | Rest |  |  | WASHOUT 1 |
| 4 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 4 | 5 | 5 mg |  |  | TREATMENT 2 |
| 5 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 5 | REST | Rest |  |  | WASHOUT 2 |
| 6 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 6 | 10 | 10 mg |  |  | TREATMENT 3 |
| 7 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 7 | FU | Follow-up |  |  | FOLLOW-UP |
| 8 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 1 | SCRN | Screen | Randomized to 5 mg - Placebo - 10 mg |  | SCREENING |
| 9 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 2 | 5 | 5 mg |  |  | TREATMENT 1 |
| 10 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 3 | REST | Rest |  |  | WASHOUT 1 |
| 11 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 4 | P | Placebo |  |  | TREATMENT 2 |
| 12 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 5 | REST | Rest |  |  | WASHOUT 2 |
| 13 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 6 | 10 | 10 mg |  |  | TREATMENT 3 |
| 14 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 7 | FU | Follow-up |  |  | FOLLOW-UP |
| 15 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 1 | SCRN | Screen | Randomized to 5 mg - 10 mg - Placebo |  | SCREENING |
| 16 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 2 | 5 | 5 mg |  |  | TREATMENT 1 |
| 17 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 3 | REST | Rest |  |  | WASHOUT 1 |
| 18 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 4 | 10 | 10 mg |  |  | TREATMENT 2 |
| 19 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 5 | REST | Rest |  |  | WASHOUT 2 |
| 20 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 6 | P | Placebo |  |  | TREATMENT 3 |
| 21 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 7 | FU | Follow-up |  |  | FOLLOW-UP |

###### Example 3

Each of the paths for the trial illustrated in the following diagram goes through one branch point at randomization, and then through another branch point when response is evaluated. This results in 4 arms, corresponding to the number of possible paths through the trial, and also to the number of blocks at the right end of the diagram. The fact that there are only 2 kinds of block at the right end, `Open DRUG X` and `Rescue`, does not affect the fact that there are 4 paths and thus 4 arms.

The next diagram for this trial is the prospective view. It shows the epochs of the trial and how the initial group of subjects is split into 2 treatment groups for the double-blind treatment epoch, and how each of those initial treatment groups is split in 2 at the response evaluation, resulting in the 4 arms of this trial. The names of the arms have been chosen to represent the outcomes of the successive branches that, together, assign subjects to arms. These compound names were chosen to facilitate description of subjects who may drop out of the trial after the first branch and before the second branch. Example 7 in Section 5.2, Demographics, illustrates DM and Subject Elements (SE) data for such subjects.

The next diagram shows the retrospective view. As with the first 2 example trials, there is 1 element in each study cell.

The last diagram for this trial shows the trial from the viewpoint of blinded participants. Since the prospective view is the view most relevant to study participants, the blinded view shown here is a prospective view. Because blinded participants can tell which treatment a subject receives in the Open Label epoch, they see 2 possible element sequences.

The trial design matrix for this trial can be constructed easily from the diagram showing arms and epochs.

**Trial Design Matrix**

| Arm | Screen | Double Blind | Open Label |
| --- | --- | --- | --- |
| A-Open A | Screen | Treatment A | Open Drug A |
| A-Rescue | Screen | Treatment A | Rescue |
| B-Open A | Screen | Treatment B | Open Drug A |
| B-Rescue | Screen | Treatment B | Rescue |

Creating the TA dataset for this example trial is similarly straightforward. Note that because there are 2 branch points in this trial, `TABRANCH` is populated for 2 records in each arm. Note also that the values of `ARMCD`, like the values of `ARM`, reflect the 2 separate processes that result in a subject's assignment to an arm.

`ta.xpt`

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX3 | TA | AA | A-Open A | 1 | SCRN | Screen | Randomized to Treatment A |  | SCREENING |
| 2 | EX3 | TA | AA | A-Open A | 2 | DBA | Treatment A | Assigned to Open Drug A on basis of response evaluation |  | BLINDED TREATMENT |
| 3 | EX3 | TA | AA | A-Open A | 3 | OA | Open Drug A |  |  | OPEN LABEL TREATMENT |
| 4 | EX3 | TA | AR | A-Rescue | 1 | SCRN | Screen | Randomized to Treatment A |  | SCREENING |
| 5 | EX3 | TA | AR | A-Rescue | 2 | DBA | Treatment A | Assigned to Rescue on basis of response evaluation |  | BLINDED TREATMENT |
| 6 | EX3 | TA | AR | A-Rescue | 3 | RSC | Rescue |  |  | OPEN LABEL TREATMENT |
| 7 | EX3 | TA | BA | B-Open A | 1 | SCRN | Screen | Randomized to Treatment B |  | SCREENING |
| 8 | EX3 | TA | BA | B-Open A | 2 | DBB | Treatment B | Assigned to Open Drug A on basis of response evaluation |  | BLINDED TREATMENT |
| 9 | EX3 | TA | BA | B-Open A | 3 | OA | Open Drug A |  |  | OPEN LABEL TREATMENT |
| 10 | EX3 | TA | BR | B-Rescue | 1 | SCRN | Screen | Randomized to Treatment B |  | SCREENING |
| 11 | EX3 | TA | BR | B-Rescue | 2 | DBB | Treatment B | Assigned to Rescue on basis of response evaluation |  | BLINDED TREATMENT |
| 12 | EX3 | TA | BR | B-Rescue | 3 | RSC | Rescue |  |  | OPEN LABEL TREATMENT |

See Section 7.2.1.1 Trial Arms Issues, Distinguishing Between Branches and Transitions, for additional discussion regarding when a decision point in a trial design should be considered to give rise to a new arm.

###### Example 4

The following diagram uses a new symbol, a large curved arrow representing the fact that the chemotherapy treatment, `A` or `B`, and the rest period that follows it are to be repeated. In this trial, the chemotherapy cycles are to be repeated until disease progression. Although some chemotherapy trials specify a maximum number of cycles, protocols that allow an indefinite number of repeats are not uncommon.

The next diagram shows the prospective view of this trial. Note that, in spite of the repeating element structure, this is, at its core, a 2-arm parallel study, and thus has 2 arms. In SDTMIG 3.1.1, there was an implicit assumption that each element must be in a separate epoch, and trials with cyclical chemotherapy were difficult to handle. The introduction of the concept of study cells and the dropping of the assumption that elements and epochs have a one-to-one relationship resolved these difficulties. This trial is best treated as having just 3 epochs, since the main objectives of the trial involve comparisons between the 2 treatments and do not require data to be considered cycle by cycle.

The next diagram shows the retrospective view of this trial.

For the purpose of developing a TA dataset for this oncology trial, the diagram must be redrawn to explicitly represent multiple treatment and rest elements. If a maximum number of cycles is not given by the protocol, then for the purposes of constructing an SDTM TA dataset for submission, which can only take place after the trial is complete, the number of repeats included in the TA dataset should be the maximum number of repeats that occurred in the trial. The next diagram assumes that the maximum number of cycles that occurred in this trial was 4. Some subjects will not have received all 4 cycles, because their disease progressed. The rule that directed that they receive no further cycles of chemotherapy is represented by a set of green arrows, 1 at the end of each rest epoch, that shows that a subject skips forward if their disease progresses. In the TA dataset, each skip-forward instruction is a transition rule, recorded in the `TATRANS` variable; when `TATRANS` is not populated, the rule is to transition to the next element in sequence.

The logistics of dosing mean that few oncology trials are blinded; the next diagram, however, shows the trial from the viewpoint of blinded participants if this trial is blinded.

The trial design matrix for this example trial corresponds to the diagram showing the retrospective view, with explicit repeats of the treatment and rest elements. As previously noted, the trial design matrix does not include information regarding when randomization occurs; similarly, information corresponding to the skip-forward rules is not represented in the trial design matrix.

**Trial Design Matrix**

| Arm | Screen | Treatment | Follow-up |
| --- | --- | --- | --- |
| A | Screen | Trt A -> Rest -> Trt A -> Rest -> Trt A -> Rest -> Trt A -> Rest | Follow-up |
| B | Screen | Trt B -> Rest -> Trt B -> Rest -> Trt B -> Rest -> Trt B -> Rest | Follow-up |

The TA dataset for this example trial requires the use of the `TATRANS` variable to represent the repeat until disease progression feature. In the TA dataset, `TATRANS` is populated for each element with a green arrow in the diagram. In other words, if there is a possibility that a subject will, at the end of this element, skip forward to a later part of the arm, then `TATRANS` is populated with the rule describing the conditions under which a subject will go to a later element. If the subject always goes to the next element in the arm, see Example Trials 1-3, then `TATRANS` is null. The TA dataset presented below corresponds to the trial design matrix.

`ta.xpt`

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX4 | TA | A | A | 1 | SCRN | Screen | Randomized to A |  | SCREENING |
| 2 | EX4 | TA | A | A | 2 | A | Trt A |  |  | TREATMENT |
| 3 | EX4 | TA | A | A | 3 | REST | Rest |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 4 | EX4 | TA | A | A | 4 | A | Trt A |  |  | TREATMENT |
| 5 | EX4 | TA | A | A | 5 | REST | Rest |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 6 | EX4 | TA | A | A | 6 | A | Trt A |  |  | TREATMENT |
| 7 | EX4 | TA | A | A | 7 | REST | Rest |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 8 | EX4 | TA | A | A | 8 | A | Trt A |  |  | TREATMENT |
| 9 | EX4 | TA | A | A | 9 | REST | Rest |  |  | TREATMENT |
| 10 | EX4 | TA | A | A | 10 | FU | Follow-up |  |  | FOLLOW-UP |
| 11 | EX4 | TA | B | B | 1 | SCRN | Screen | Randomized to B |  | SCREENING |
| 12 | EX4 | TA | B | B | 2 | B | Trt B |  |  | TREATMENT |
| 13 | EX4 | TA | B | B | 3 | REST | Rest |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 14 | EX4 | TA | B | B | 4 | B | Trt B |  |  | TREATMENT |
| 15 | EX4 | TA | B | B | 5 | REST | Rest |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 16 | EX4 | TA | B | B | 6 | B | Trt B |  |  | TREATMENT |
| 17 | EX4 | TA | B | B | 7 | REST | Rest |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 18 | EX4 | TA | B | B | 8 | B | Trt B |  |  | TREATMENT |
| 19 | EX4 | TA | B | B | 9 | REST | Rest |  |  | TREATMENT |
| 20 | EX4 | TA | B | B | 10 | FU | Follow-up |  |  | FOLLOW-UP |

###### Example 5

Example Trial 5 is much like Example Trial 4, in that the 2 treatments being compared are given in cycles, and the total length of the cycle is the same for both treatments. In this trial, however, treatment A is given over longer duration than treatment B. Because of this difference in treatment patterns, this trial cannot be blinded.

The assumption of a one-to-one relationship between elements and epochs makes such situations difficult to handle. However, without that assumption, this trial is essentially the same as Trial 4. The next diagram shows the retrospective view of this trial.

The trial design matrix for this trial is almost the same as for Example Trial 4; the only difference is that the maximum number of cycles for this trial was assumed to be 3.

**Trial Design Matrix**

| Arm | Screen | Treatment | Follow-up |
| --- | --- | --- | --- |
| A | Screen | Trt A -> Rest A -> Trt A -> Rest A -> Trt A -> Rest A | Follow-up |
| B | Screen | Trt B -> Rest B -> Trt B -> Rest B -> Trt B -> Rest B | Follow-up |

The TA dataset for this trial shown below corresponds to the trial design matrix.

`ta.xpt`

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX5 | TA | A | A | 1 | SCRN | Screen | Randomized to A |  | SCREENING |
| 2 | EX5 | TA | A | A | 2 | A | Trt A |  |  | TREATMENT |
| 3 | EX5 | TA | A | A | 3 | RESTA | Rest A |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 4 | EX5 | TA | A | A | 4 | A | Trt A |  |  | TREATMENT |
| 5 | EX5 | TA | A | A | 5 | RESTA | Rest A |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 6 | EX5 | TA | A | A | 6 | A | Trt A |  |  | TREATMENT |
| 7 | EX5 | TA | A | A | 7 | RESTA | Rest A |  |  | TREATMENT |
| 8 | EX5 | TA | A | A | 8 | FU | Follow-up |  |  | FOLLOW-UP |
| 9 | EX5 | TA | B | B | 1 | SCRN | Screen | Randomized to B |  | SCREENING |
| 10 | EX5 | TA | B | B | 2 | B | Trt B |  |  | TREATMENT |
| 11 | EX5 | TA | B | B | 3 | RESTB | Rest B |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 12 | EX5 | TA | B | B | 4 | B | Trt B |  |  | TREATMENT |
| 13 | EX5 | TA | B | B | 5 | RESTB | Rest B |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 14 | EX5 | TA | B | B | 6 | B | Trt B |  |  | TREATMENT |
| 15 | EX5 | TA | B | B | 7 | RESTB | Rest B |  |  | TREATMENT |
| 16 | EX5 | TA | B | B | 8 | FU | Follow-up |  |  | FOLLOW-UP |

###### Example 6

Example Trial 6 is an oncology trial comparing 2 types of chemotherapy that are given using cycles of different lengths with different internal patterns. Treatment A is given in 3-week cycles with a longer duration of treatment and a short rest; treatment B is given in 4-week cycles with a short duration of treatment and a long rest.

The design of this trial is very similar to that for Example Trials 4 and 5. The main difference is that there are 2 different rest elements: the short one used with drug A and the long one used with drug B. The next diagram shows the retrospective view of this trial.

The trial design matrix for this trial assumes that there was a maximum of 4 cycles of drug A and a maximum of three cycles of drug B.

**Trial Design Matrix**

| Arm | Screen | Treatment | Follow-up |
| --- | --- | --- | --- |
| A | Screen | Trt A -> Rest A -> Trt A -> Rest A -> Trt A -> Rest A -> Trt A -> Rest A | Follow-up |
| B | Screen | Trt B -> Rest B -> Trt B -> Rest B -> Trt B -> Rest B | Follow-up |

In the following TA dataset, because the treatment epoch for arm A has more elements than the treatment epoch for arm B, `TAETORD` is 10 for the follow-up element in arm A, but 8 for the follow-up element in arm B. It would also be possible to assign a `TAETORD` value of 10 to the follow-up element in arm B. The primary purpose of `TAETORD` is to order elements within an arm; leaving gaps in the series of `TAETORD` values does not interfere with this purpose.

`ta.xpt`

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX6 | TA | A | A | 1 | SCRN | Screen | Randomized to A |  | SCREENING |
| 2 | EX6 | TA | A | A | 2 | A | Trt A |  |  | TREATMENT |
| 3 | EX6 | TA | A | A | 3 | RESTA | Rest A |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 4 | EX6 | TA | A | A | 4 | A | Trt A |  |  | TREATMENT |
| 5 | EX6 | TA | A | A | 5 | RESTA | Rest A |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 6 | EX6 | TA | A | A | 6 | A | Trt A |  |  | TREATMENT |
| 7 | EX6 | TA | A | A | 7 | RESTA | Rest A |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 8 | EX6 | TA | A | A | 8 | A | Trt A |  |  | TREATMENT |
| 9 | EX6 | TA | A | A | 9 | RESTA | Rest A |  |  | TREATMENT |
| 10 | EX6 | TA | A | A | 10 | FU | Follow-up |  |  | FOLLOW-UP |
| 11 | EX6 | TA | B | B | 1 | SCRN | Screen | Randomized to B |  | SCREENING |
| 12 | EX6 | TA | B | B | 2 | B | Trt B |  |  | TREATMENT |
| 13 | EX6 | TA | B | B | 3 | RESTB | Rest B |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 14 | EX6 | TA | B | B | 4 | B | Trt B |  |  | TREATMENT |
| 15 | EX6 | TA | B | B | 5 | RESTB | Rest B |  | If disease progression, go to Follow-up Epoch | TREATMENT |
| 16 | EX6 | TA | B | B | 6 | B | Trt B |  |  | TREATMENT |
| 17 | EX6 | TA | B | B | 7 | RESTB | Rest B |  |  | TREATMENT |
| 18 | EX6 | TA | B | B | 8 | FU | Follow-up |  |  | FOLLOW-UP |

###### Example 7

In open trials, there is no requirement to maintain a blind, and the arms of a trial may be quite different from each other. In such a case, changes in treatment in one arm may differ in number and timing from changes in treatment in another, so that there is nothing like a one-to-one match between the elements in the different arms. In such a case, epochs are likely to be defined as broad intervals of time, spanning several elements, and chosen to correspond to periods of time that will be compared in analyses of the trial.

Example Trial 7, RTOG 93-09, involves treatment of lung cancer with chemotherapy and radiotherapy, with or without surgery. The protocol, `RTOG-93-09`, which was provided by the Radiation Oncology Therapy Group (RTOG), does not include a study schema diagram, but does include a text-based representation of diverging options to which a subject may be assigned. All subjects go through the branch point at randomization, when they are assigned to either chemotherapy plus radiotherapy (`CR`) or chemotherapy and radiotherapy plus surgery (`CRS`). All subjects receive induction chemotherapy and radiation, with a slight difference between those randomized to the 2 arms during the second cycle of chemotherapy. Those randomized to the non-surgery arm are evaluated for disease somewhat earlier, to avoid delays in administering the radiation boost to those whose disease has not progressed. After induction chemotherapy and radiation, subjects are evaluated for disease progression, and those whose disease has progressed stop treatment, but enter follow-up. Not all subjects randomized to receive surgery who do not have disease progression will necessarily receive surgery. If they are poor candidates for surgery or do not wish to receive surgery, they will not receive surgery, but will receive further chemotherapy. The following diagram is based on the text schema in the protocol, with the 5 options it names. The diagram in this form might suggest that the trial has 5 arms.

However, the objectives of the trial make it clear that this trial is designed to compare 2 treatment strategies, chemotherapy and radiation with and without surgery, so this study is better modeled as a 2-arm trial, but with major skip-forward arrows for some subjects, as illustrated in the following diagram. This diagram also shows more detail within the `Induction Chemo + RT` and `Additional Chemo` blocks than the preceding diagram. Both the induction and additional chemotherapy are given in 2 cycles. The second induction cycle is different for the 2 arms, since radiation therapy for those assigned to the non-surgery arm includes a boost which those assigned to the surgery arm do not receive.

The next diagram shows the prospective view of this trial. The protocol conceives of treatment as being divided into 2 parts, induction and continuation, so these have been treated as 2 different epochs. This is also an important point in the trial operationally, the point when subjects are registered a second time, and when subjects who will skip forward are identified, i.e., because of disease progression or ineligibility for surgery.

The next diagram shows the retrospective view of this trial. The fact that the elements in the study cell for the `CR` arm in the continuation treatment epoch do not fill the space in the diagram is an artifact of the diagram conventions. Those subjects who do receive surgery will in fact spend a longer time completing treatment and moving into follow-up. Although it is tempting to think of the horizontal axis of these diagrams as a timeline, this can sometimes be misleading. The diagrams are not necessarily to scale in the sense that the length of the block representing an element represents its duration, and elements that line up on the same vertical line in the diagram may not occur at the same relative time within the study.

The following table shows the trial design matrix for this 2-arm example trial.

**Trial Design Matrix**

| Arm | Screen | Induction | Continuation | Follow-up |
| --- | --- | --- | --- | --- |
| CR | Screen | Initial Chemo + RT -> Chemo + RT (non-Surgery) | Chemo -> Chemo | Off Treatment Follow-up |
| CRS | Screen | Initial Chemo + RT -> Chemo + RT (Surgery) | 3-5 week Rest -> Surgery -> 4-6 week Rest -> Chemo -> Chemo | Off Treatment Follow-up |

The TA dataset reflects that this is a 2-arm trial.

`ta.xpt`

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX7 | TA | 1 | CR | 1 | SCRN | Screen | Randomized to CR |  | SCREENING |
| 2 | EX7 | TA | 1 | CR | 2 | ICR | Initial Chemo + RT |  |  | INDUCTION TREATMENT |
| 3 | EX7 | TA | 1 | CR | 3 | CRNS | Chemo + RT (non-Surgery) |  | If progression, skip to Follow-up. | INDUCTION TREATMENT |
| 4 | EX7 | TA | 1 | CR | 4 | C | Chemo |  |  | CONTINUATION TREATMENT |
| 5 | EX7 | TA | 1 | CR | 5 | C | Chemo |  |  | CONTINUATION TREATMENT |
| 6 | EX7 | TA | 1 | CR | 6 | FU | Off Treatment Follow-up |  |  | FOLLOW-UP |
| 7 | EX7 | TA | 2 | CRS | 1 | SCRN | Screen | Randomized to CRS |  | SCREENING |
| 8 | EX7 | TA | 2 | CRS | 2 | ICR | Initial Chemo + RT |  |  | INDUCTION TREATMENT |
| 9 | EX7 | TA | 2 | CRS | 3 | CRS | Chemo + RT (Surgery) |  | If progression, skip to Follow-up. If no progression, but subject is ineligible for or does not consent to surgery, skip to Chemo. | INDUCTION TREATMENT |
| 10 | EX7 | TA | 2 | CRS | 4 | R3 | 3-5 week rest |  |  | CONTINUATION TREATMENT |
| 11 | EX7 | TA | 2 | CRS | 5 | SURG | Surgery |  |  | CONTINUATION TREATMENT |
| 12 | EX7 | TA | 2 | CRS | 6 | R4 | 4-6 week rest |  |  | CONTINUATION TREATMENT |
| 13 | EX7 | TA | 2 | CRS | 7 | C | Chemo |  |  | CONTINUATION TREATMENT |
| 14 | EX7 | TA | 2 | CRS | 8 | C | Chemo |  |  | CONTINUATION TREATMENT |
| 15 | EX7 | TA | 2 | CRS | 9 | FU | Off Treatment Follow-up |  |  | FOLLOW-UP |

##### 7.2.1.1 Trial Arms Issues

###### Distinguishing Between Branches and Transitions

Both the Branch and Transition columns contain rules, but the 2 columns represent 2 different types of rules.

Branch rules represent forks in the trial flowchart, giving rise to separate arms. The rule underlying a branch in the trial design appears in multiple records, once for each "fork" of the branch. Within any one record, there is no choice (no "if" clause) in the value of the branch condition. For example, the value of TABRANCH for a record in arm A is "Randomized to Arm A" because a subject in arm A must have been randomized to arm A.

Transition rules are used for choices within an arm. The value for TATRANS does contain a choice (an "if" clause). In Example Trial 4, subjects who receive 1, 2, 3, or 4 cycles of treatment A are all considered to belong to arm A.

In modeling a trial, decisions may have to be made about whether a decision point in the flow chart represents the separation of paths that represent different arms, or paths that represent variations within the same arm, as illustrated in the discussion of Example Trial 7. This decision will depend on the comparisons of interest in the trial.

Some trials refer to groups of subjects who follow a particular path through the trial as "cohorts," particularly if the groups are formed successively over time. The term "cohort" is used with different meanings in different protocols and does not always correspond to an arm.

###### Subjects Not Assigned to an Arm

Some trial subjects may drop out of the study before they reach all of the branch points in the trial design. In the Demographics (DM) domain, the values of ARM and ARMCD must be supplied for such subjects, but the special values used for these subjects should not be included in the Trial Arms (TA) dataset; only complete arm paths should be described in the TA dataset.

In Section 5.2, Demographics, assumption 4 describes special ARM and ARMCD values used for subjects who do not reach the first branch point in a trial. When a trial design includes 2 or more branches, special values of ARM and ARMCD may be needed for subjects who pass through the first branch point, but drop out before the final branch point. See DM Example 3 for how to represent ARM and ARMCD values for such trials.

###### Defining Epochs

The series of examples for the TA dataset provides a variety of scenarios and guidance about how to assign epoch in those scenarios. In general, assigning epochs for blinded trials is easier than for unblinded trials. The blinded view of the trial will generally make the possible choices clear. For unblinded trials, the comparisons that will be made between arms can guide the definition of epochs. For trials that include many variant paths within an arm, comparisons of arms will mean that subjects on a variety of paths will be included in the comparison, and this is likely to lead to definition of broader epochs.

###### Rule Variables

The Branch and Transition columns shown in the example tables are variables with a Role of "Rule." The values of a Rule variable describe conditions under which something is planned to happen. At the moment, values of Rule variables are text. At some point in the future, it is expected that a mechanism to provide machine-readable rules will become available. Other Rule variables are present in the Trial Elements (TE) and Trial Visits (TV) datasets.

#### 7.2.2 Trial Elements (TE)

##### TE – Description/Overview
A trial design domain that contains the element code that is unique for each element, the element description, and the rules for starting and ending an element.

The Trial Elements (TE) dataset contains the definitions of the elements that appear in the Trial Arms (TA) dataset.

An element may appear multiple times in the TA table because it appears either (1) in multiple arms, (2) multiple times within an arm, or (3) both. However, an element will appear only once in the TE table.

Each row in the TE dataset may be thought of as representing a "unique element" in the same sense of "unique" as a CRF template page for a collecting certain type of data referred to as "unique page." For instance, a CRF might be described as containing 87 pages, but only 23 unique pages. By analogy, the trial design matrix in Example Trial 1 (see Section 7.2.1, Trial Arms) has 9 study cells, each of which contains 1 element, but the same trial design matrix contains only 5 unique elements, so the TE dataset for that trial has only 5 records.

An element is a building block for creating study cells, and an arm is composed of study cells. Or, from another point of view, an arm is composed of elements; that is, the trial design assigns subjects to arms, which comprise a sequence of steps called elements.

Trial elements represent an interval of time that serves a purpose in the trial and are associated with certain activities affecting the subject. “Week 2 to week 4” is not a valid element. A valid element has a name that describes the purpose of the element and includes a description of the activity or event that marks the subject's transition into the element as well as the conditions for leaving the element.

##### TE – Specification
te.xpt, Trial Elements — Trial Design. One record per planned Element, Tabulation.

| Variable Name | Variable Label | Type | Controlled Terms, Codelist or Format1 | Role | CDISC Notes | Core |
| --- | --- | --- | --- | --- | --- | --- |
| STUDYID | Study Identifier | Char | Identifier |  | Unique identifier for a study. | Req |
| DOMAIN | Domain Abbreviation | Char | TE | Identifier | Two-character abbreviation for the domain. | Req |
| ETCD | Element Code | Char | * | Topic | ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name. | Req |
| ELEMENT | Description of Element | Char | * | Synonym Qualifier | The name of the element. | Req |
| TESTRL | Rule for Start of Element | Char |  | Rule | Describes condition for beginning element. | Req |
| TEENRL | Rule for End of Element | Char |  | Rule | Describes condition for ending element. Either TEENRL or TEDUR must be present for each element. | Perm |
| TEDUR | Planned Duration of Element | Char | ISO 8601 duration | Timing | Planned duration of element in ISO 8601 format. Used when the rule for ending the element is applied after a fixed duration. | Perm |

1 In this column, an asterisk (*) indicates that the variable may be subject to controlled terminology. CDISC/NCI codelist values are enclosed in parentheses.

##### TE – Assumptions
1. There are no gaps between elements. The instant one element ends, the next element begins. A subject spends no time "between" elements.
2. The ELEMENT (Description of the Element) variable usually indicates the treatment being administered during an element, or, if no treatment is being administered, the other activities that are the purpose of this period of time (e.g., "Screening", "Follow-up", "Washout"). In some cases, this time period may be quite passive (e.g., "Rest"; "Wait, for disease episode").
3. The TESTRL (Rule for Start of Element) variable identifies the event that marks the transition into this element. For elements that involve treatment, this is the start of treatment.
4. For elements that do not involve treatment, TESTRL can be more difficult to define. For washout and follow-up elements, which always follow treatment elements, the start of the element may be defined relative to the end of a preceding treatment. For example, a washout period might be defined as starting 24 or 48 hours after the last dose of drug for the preceding treatment element or epoch. This definition is not totally independent of the TA dataset, because it relies on knowing where in the trial design the element is used, and that it always follows a treatment element. Defining a clear starting point for the start of a non-treatment element that always follows another non-treatment element can be particularly difficult. The transition may be defined by a decision-making activity such as enrollment or randomization. For example, every arm of a trial that involves treating disease episodes might start with a screening element followed by an element that consists of waiting until a disease episode occurs. The activity that marks the beginning of the wait element might be randomization.
5. TESTRL for a treatment element may be thought of as "active" whereas the start rule for a non-treatment element-particularly a follow-up or washout element-may be "passive." The start of a treatment element will not occur until a dose is given, no matter how long that dose is delayed. Once the last dose is given, the start of a subsequent non-treatment element is inevitable, as long as another dose is not given.
6. Note that the date/time of the event described in TESTRL will be used to populate the date/times in the Subject Elements (SE) dataset, so the date/time of the event should be captured in the CRF.
7. Specifying TESTRL for an element that serves the first element of an arm in the TA dataset involves defining the start of the trial. In the examples in this document, obtaining informed consent has been used as "Trial Entry."
8. TESTRL should be expressed without referring to arm. If the element appears in more than 1 arm in the TA dataset, then the element description (ELEMENT) must not refer to any arms.
9. TESTRL should be expressed without referring to epoch. If the element appears in more than 1 epoch in the TA dataset, then the Element description (ELEMENT) must not refer to any epochs.
10. For a blinded trial, it is useful to describe TESTRL in terms that separate the properties of the event that are visible to blinded participants from the properties that are visible only to those who are unblinded. For treatment elements in blinded trials, wording such as the following is suitable: "First dose of study drug for a treatment epoch, where study drug is X."
11. Element end rules are rather different from element start rules. The actual end of one element is the beginning of the next element. Thus, the element end rule does not give the conditions under which an element does end, but the conditions under which it should end or is planned to end.
12. At least 1 of TEENRL and TEDUR must be populated. Both may be populated.
13. TEENRL describes the circumstances under which a subject should leave this element. Element end rules may depend on a variety of conditions. For instance, a typical criterion for ending a rest element between oncology chemotherapy-treatment element would be, "15 days after start of element and after WBC values have recovered." The TA dataset, not the TE dataset, describes where the subject moves next, so TEENRL must be expressed without referring to arm.
14. TEDUR serves the same purpose as TEENRL for the special (but very common) case of an element with a fixed duration. TEDUR is expressed in ISO 8601. For example, a TEDUR value of P6W is equivalent to a TEENRL of "6 weeks after the start of the element."
15. Note that elements that have different start and end rules are different elements and must have different values of ELEMENT and ETCD. For instance, elements that involve the same treatment but have different durations are different elements. The same applies to non-treatment elements. For instance, a washout with a fixed duration of 14 days is different from a washout that is to end after 7 days if drug cannot be detected in a blood sample, or after 14 days otherwise.
##### TE – Examples
Both of the trials in TA Examples 1 and 2 (see Section 7.2.1, Trial Arms) are assumed to have fixed-duration elements. The wording in TESTRL is intended to separate the description of the event that starts the element into the part that would be visible to a blinded participant in the trial (e.g., "First dose of a treatment epoch") from the part that is revealed when the study is unblinded (e.g., "where dose is 5 mg"). Care must be taken in choosing these descriptions to be sure that they are arm- and epoch-neutral. For instance, in a crossover trial such as TA Example Trial 3, where an element may appear in 1 of multiple epochs, the wording must be appropriate for all possible epochs (e.g., "OPEN LABEL TREATMENT"). The SDS Team is considering adding a separate variable to the TE dataset that would hold information on the treatment that is associated with an element. This would make it clearer which elements are "treatment elements" and, therefore, which epochs contain treatment elements and thus are "treatment epochs."

###### Example 1

This example shows the TE dataset for TA Example Trial 1.

`te.xpt`

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX1 | TE | SCRN | Screen | Informed consent | 1 week after start of Element | P7D |
| 2 | EX1 | TE | RI | Run-In | Eligibility confirmed | 2 weeks after start of Element | P14D |
| 3 | EX1 | TE | P | Placebo | First dose of study drug, where drug is placebo | 2 weeks after start of Element | P14D |
| 4 | EX1 | TE | A | Drug A | First dose of study drug, where drug is Drug A | 2 weeks after start of Element | P14D |
| 5 | EX1 | TE | B | Drug B | First dose of study drug, where drug is Drug B | 2 weeks after start of Element | P14D |

###### Example 2

This example shows the TE dataset for TA Example Trial 2.

`te.xpt`

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX2 | TE | SCRN | Screen | Informed consent | 2 weeks after start of Element | P14D |
| 2 | EX2 | TE | P | Placebo | First dose of a treatment Epoch, where dose is placebo | 2 weeks after start of Element | P14D |
| 3 | EX2 | TE | 5 | 5 mg | First dose of a treatment Epoch, where dose is 5 mg drug | 2 weeks after start of Element | P14D |
| 4 | EX2 | TE | 10 | 10 mg | First dose of a treatment Epoch, where dose is 10 mg drug | 2 weeks after start of Element | P14D |
| 5 | EX2 | TE | REST | Rest | 48 hrs after last dose of preceding treatment Epoch | 1 week after start of Element | P7D |
| 6 | EX2 | TE | FU | Follow-up | 48 hrs after last dose of third treatment Epoch | 3 weeks after start of Element | P21D |

###### Example 3

The TE dataset for TA Example Trial 4 illustrates element end rules for elements that are not all of fixed duration. The screen element in this study can be up to 2 weeks long, but because it may end earlier it is not of fixed duration. The rest element has a variable length, depending on how quickly WBC recovers. Note that the start rules for the A and B elements have been written to be suitable for a blinded study.

`te.xpt`

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | EX4 | TE | SCRN | Screen | Informed Consent | Screening assessments are complete, up to 2 weeks after start of Element |  |
| 2 | EX4 | TE | A | Trt A | First dose of treatment Element, where drug is Treatment A | 5 days after start of Element | P5D |
| 3 | EX4 | TE | B | Trt B | First dose of treatment Element, where drug is Treatment B | 5 days after start of Element | P5D |
| 4 | EX4 | TE | REST | Rest | Last dose of previous treatment cycle + 24 hrs | At least 16 days after start of Element and WBC recovered |  |
| 5 | EX4 | TE | FU | Follow-up | Decision not to treat further | 4 weeks | P28D |
##### 7.2.2.1 Trial Elements Issues

###### Granularity of Trial Elements

Deciding how finely to divide trial time when identifying trial elements is a matter of judgment, as illustrated by the following examples:

1. TA Example Trial 2 was represented using 3 treatment epochs separated by 2 washout epochs and followed by a follow-up epoch. This might have been modeled using 3 treatment epochs that included both the 2-week treatment period and the 1-week rest period. Because the first week after the third treatment period would be included in the third treatment epoch, the follow-up epoch would then have a duration of 2 weeks.
2. In TA Example Trials 4, 5, and 6, separate treatment and rest elements were identified. However, the combination of treatment and rest could be represented as a single element.
3. A trial might include a dose titration, with subjects receiving increasing doses on a weekly basis until certain conditions are met. The trial design could be modeled in any of the following ways:
    a. Using several 1-week elements at specific doses, followed by an element of variable length at the chosen dose
    b. As a titration element of variable length followed by a constant dosing element of variable length
    c. One element with dosing determined by titration

The choice of elements used to represent this dose titration will depend on the objectives of the trial and how the data will be analyzed and reported. If it is important to examine side effects or lab values at each individual dose, the first model is appropriate. If it is important only to identify the time to completion of titration, the second model might be appropriate. If the titration process is routine and is of little interest, the third model might be adequate for the purposes of the trial.

###### Distinguishing Elements, Study Cells, and Epochs

It is easy to confuse elements, which are reusable trial building blocks, with study cells (which contain the elements for a particular epoch and arm) and with epochs (which are time periods for the trial as a whole). In part, this is because many trials have epochs for which the same element appears in all arms. In other words, in the trial design matrix for many trials, there are columns (epochs) in which all the study cells have the same contents. It also is natural to use the same name (e.g., screen, follow-up) for both such an epoch and the single element that appears within it.

Confusion can also arise from the fact that in the blinded treatment portions of blinded trials, blinded participants do not know which element a subject is in, but do know what epoch the subject is in.

In describing a trial, one way to avoid confusion between elements and epochs is to include "Element" or "Epoch" in the values of ELEMENT or EPOCH when these values (e.g., screening, follow-up) would otherwise be the same. It becomes tedious to do this in every case, but can be useful to resolve confusion when it arises or is likely to arise.

The difference between epoch and element is perhaps clearest in crossover trials. In TA Example Trial 2, as for most crossover trials, the analysis of pharmacokinetic (PK) results would include both treatment and period effects in the model. "Treatment effect" derives from element (placebo, 5 mg, 10 mg), whereas "period effect" derives from the epoch (first, second, or third treatment epoch).

###### Transitions Between Elements

The transition between one element and the next can be thought of as a 3-step process:

| Step | Step question | How step question is answered by information in the TA datasets |
| --- | --- | --- |
| 1 | Should the subject leave the current element? | The criteria for ending the current element are in TEENRL in the TE dataset. |
| 2 | Which element should the subject enter next? | If there is a branch point at this point in the trial, evaluate criteria described in TABRANCH (e.g., randomization results) in the TA dataset. Otherwise, if TATRANS in the TA dataset is populated in this arm at this point, follow those instructions. Otherwise, move to the next element in this arm as specified by TAETORD in the TA dataset. |
| 3 | What does the subject do to enter the next element? | The action or event that marks the start of the next element is specified in TESTRL in the TE dataset. |

Note that the subject is not "in limbo" during this process. The subject remains in the current element until step 3, at which point the subject transitions to the new element. There are no gaps between elements.

As illustrated in the table, executing a transition depends on information that is split between the TE and the TA datasets.

It can be useful, in the process of working out the Trial Design (TD) datasets, to create a dataset that supplements the TA dataset with the TESTRL, TEENRL, and TEDUR variables, so that full information on the transitions is easily accessible. However, such a working dataset is not an SDTM dataset, and should not be submitted.

The following table shows a fragment of such a table for TA Example Trial 4.

Note that

- for all records that contain a particular element, all the TE variable values are exactly the same; and
- when both TABRANCH and TATRANS are blank, the implicit decision in step 2 is that the subject moves to the next element in sequence for the arm.

special.xpt
| Row | ARM | EPOCH | TAETORD | ELEMENT | TESTRL | TEENRL | TEDUR | TABRANCH | TATRANS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | A | Screen | 1 | Screen | Informed Consent | Screening assessments are complete, up to 2 weeks after start of Element |  | Randomized to A |  |
| 2 | A | Treatment | 2 | Trt A | First dose of treatment in Element, where drug is Treatment A | 5 days after start of Element | P5D |  |  |
| 3 | A | Treatment | 3 | Rest | Last dose of previous treatment cycle + 24 hrs | 16 days after start of Element and WBC recovers |  |  | If disease progression, go to Follow-up Epoch |
| 4 | A | Treatment | 4 | Trt A | First dose of treatment in Element, where drug is Treatment A | 5 days after start of Element | P5D |  |  |

Note that rows 2 and 4 of this dataset involve the same element (Trt A); thus, TESTRL is the same for both. The activity that marks a subject's entry into the fourth element in arm A is "First dose of treatment Element, where drug is Treatment A." This is not the subject's very first dose of treatment A, but it is their first dose in this element.

