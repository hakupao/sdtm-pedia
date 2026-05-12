# TA — Assumptions

## Trial Design Model Overview (§7.1)

### §7.1.1 Purpose of the Trial Design Model

ICH E3, Guidance for Industry, Structure and Content of Clinical Study Reports (available at http://www.ich.org/products/guidelines/), Section 9.1, calls for a brief, clear description of the overall plan and design of the study, and supplies examples of charts and diagrams for this purpose in Annex IIIa and Annex IIIb.

Each Annex corresponds to an example trial, and each shows a diagram describing the study design and a table showing the schedule of assessments.

The Trial Design Model provides a standardized way to describe those aspects of the planned conduct of a clinical trial shown in the study design diagrams of these examples.

The standard Trial Design Datasets will allow reviewers to:
- Clearly and quickly grasp the design of a clinical trial
- Compare the designs of different trials
- Search a data warehouse for clinical trials with certain features
- Compare planned and actual treatments and visits for subjects in a clinical trial

Modeling a clinical trial in this standardized way requires the explicit statement of certain decision rules that may not be addressed or may be vague or ambiguous in the usual prose protocol document.

Prospective modeling of the design of a clinical trial should lead to a clearer, better protocol.

Retrospective modeling of the design of a clinical trial should ensure a clear description of how the trial protocol was interpreted by the sponsor.

### §7.1.2 Definitions of Trial Design Concepts

A clinical trial is a scientific experiment involving human subjects, intended to address certain scientific questions (i.e., the objectives of the trial).

See the CDISC Glossary (https://www.cdisc.org/standards/glossary) for more complete definitions of clinical trial and objective.

| Concept | Definition |
|---------|------------|
| Trial design | The design of a clinical trial is a plan for what will be done to subjects and what data will be collected about them, in the course of the trial, to address the trial's objectives. |
| Epoch | As part of the design of a trial, the planned period of subjects' participation in the trial is divided into epochs. Each epoch is a period of time that serves a purpose in the trial as a whole. That purpose will be at the level of the primary objectives of the trial. Typically, the purpose of an epoch will be to expose subjects to a treatment or to prepare for such a treatment period (e.g., determine subject eligibility, washout previous treatments), or to gather data on subjects after a treatment has ended. Note that at this high level, a "treatment" is a treatment strategy, which may be simple (e.g., exposure to a single drug at a single dose) or complex. Complex treatment strategies could involve tapering through several doses, titrating dose according to clinical criteria, complex regimens involving multiple drugs, or strategies for adding or dropping drugs according to clinical criteria. |
| Arm | An arm is a planned path through the trial. This path covers the entire time of the trial. The group of subjects assigned to a planned path is also often colloquially called an "arm." The group of subjects assigned to an arm is also often called a "treatment group"; in this sense, an arm is equivalent to a treatment group. |
| Study cell | Each planned path through the trial (i.e., each arm) is divided into pieces, 1 for each epoch. Each of these pieces is called a study cell. Thus, there is a study cell for each combination of arm and epoch. Each study cell represents an implementation of the purpose of its associated epoch. For an epoch whose purpose is to expose subjects to treatment, each study cell associated with the epoch has an associated treatment strategy. For example, a 3-arm parallel trial might have a treatment epoch whose purpose is to expose subjects to 1 of 3 study treatments: placebo, investigational product, or active control. There would be 3 study cell associated with the treatment epoch, 1 for each arm. Each of these study cells exposes the subject to 1 of the 3 study treatments. Another example involving more complex treatment strategies would be a trial comparing the effects of cycles of chemotherapy drug A given alone or in combination with drug B, where drug B is given as a pretreatment to each cycle of drug A. |
| Element | An element is a basic building block in the trial design. It involves administering a planned intervention, which may be treatment or no treatment, during a period of time. Elements for which the planned intervention is "no treatment" would include elements for screening, washout, and follow-up. |
| Study cells and elements | Many (perhaps most) clinical trials involve a single, simple administration of a planned intervention within a study cell. For some trials, however, the treatment strategy associated with a study cell involves a complex series of administrations of treatment. In such cases it may be important to track the component steps in a treatment strategy operationally; secondary objectives and safety analyses also might require that data be grouped by the treatment step during which it was collected. The steps within a treatment strategy may involve different doses of drug, different drugs, or different kinds of care (e.g., preoperative, operative, and post-operative periods surrounding surgery). When the treatment strategy for a study cell is simple, the study cell will contain a single element, and for many purposes there is little value in distinguishing between the study cell and the element. However, when the treatment strategy for a study cell consists of a complex series of treatments, a study cell can contain multiple elements. There may be a fixed sequence of elements, or a repeating cycle of elements, or some other complex pattern. In these cases, the distinction between a study cell and an element is very useful. |
| Branch | In a trial with multiple arms, the protocol plans for each subject to be assigned to 1 arm. The time within the trial at which this assignment takes place is the point at which the arm paths of the trial diverge, and so is called a branch point. For many trials, the assignment to an arm happens all at one time, so the trial has 1 branch point. For other trials, there may be 2 or more branches that collectively assign a subject to an arm. The process that makes this assignment may be a randomization, but it need not be. |
| Treatments | The word "treatment" may be used in connection with epochs, study cells, or elements, but has somewhat different meanings in each context: Because epochs cut across arms, an epoch treatment is at a high level that does not specify anything that differs between arms. For example, in a 3-period crossover study of 3 doses of drug X, each treatment epoch is associated with drug X, but not with a specific dose. A study cell treatment is specific to a particular arm. For example, a parallel trial might have study cell treatments placebo and drug X, without any additional detail (e.g., dose, frequency, route of administration) being specified. A study cell treatment is at a relatively high level, the level at which treatments might be planned in an early conceptual draft of the trial, or in the title or objectives of the trial. An element treatment may be fairly detailed. For example, for an element representing a cycle of chemotherapy, element treatment might specify 5 daily 100 mg doses of drug X. The distinctions between these levels are not rigid, and depend on the objectives of the trial. For example, route is generally a detail of dosing, but in a bioequivalence trial comparing IV and oral administration of drug X, route is clearly part of study cell treatment. |
| Visit | The notion of a visit—a clinical encounter—derives from trials with outpatients, where subjects interact with the investigator during visits to the investigator's clinical site. However, the term is used in other trials, where a trial visit may not correspond to a physical visit. For example, in a trial with inpatients, time may be subdivided into visits, even though subjects are in hospital throughout the trial. For example, data for a screening visit may be collected over the course of more than 1 physical visit. One of the main purposes of visits is the performance of assessments, but not all assessments need take place at clinic visits; some assessments may be performed by means of telephone contacts, electronic devices, or call-in systems. The protocol should specify what contacts are considered visits and how they are defined. |

### §7.1.3 Current and Future Contents of the Trial Design Model

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

Some dose-escalation studies enroll a new cohort of subjects for each new dose, and so, at the planning stage, have an indefinite number of arms.

Other dose-escalation studies give new doses to a continuing group of subjects, and so are planned with an indefinite number of epochs.

There may also be limitations in representing other patterns of Elements within a Study Cell that are more complex than a simple sequence.

For the purpose of submissions about trials that have already completed, these limitations are not critical, so it is expected that development of the Trial Design Model to address these limitations will have a minimal impact on the SDTM.

## Trial Arms and Trial Elements (§7.2)

### §7.2.1 Trial Arms (TA) – Description/Overview

A trial design domain that contains each planned arm in the trial.

This section contains:
- The Trial Arms dataset and assumptions
- A series of example trials, which illustrate the development of the TA dataset
- Advice on various issues in the development of the TA dataset
- A recap of the TA dataset and the function of its variables

### §7.2.1 Trial Arms (TA) – Example 2

The following diagram for a crossover trial does not use the crossing slanted lines sometimes used to represent crossover trials, because the order of the blocks is sufficient to represent the design of the trial. Slanted lines are used only to represent the branch point at randomization, when a subject is assigned to a sequence of treatments. As in most crossover trials, the arms are distinguished by the order of treatments, with the same treatments present in each arm. Note that even though all 3 arms of this trial end with the same block (i.e., the block for the follow-up element), the diagram does not show the arms converging into one block. Also note that the same block (the "rest" element) occurs twice within each arm. Elements are conceived of as "reusable" and can appear in more than 1 arm, in more than 1 epoch, and more than once in an arm.

The next diagram for this crossover trial shows the prospective view of the trial; it identifies the epoch and arms of the trial, and gives each a name. As for most crossover studies, the objectives of the trial will be addressed by comparisons between the arms and by within-subject comparisons between treatments. Because the design depends on differentiating the periods during which the subject receives the 3 different treatments, there are 3 different treatment epochs. The fact that the rest periods are identified as separate epochs suggests that these also play an important part in the design of the trial; they are probably designed to allow subjects to return to "baseline," with data collected to show that this occurred. Note that epochs are not considered reusable; each epoch has a different name, even though all the treatment epochs are similar and both the rest epochs are similar. As with the first example trial, there is a one-to-one relationship between the epochs of the trial and the elements in each arm.

The next diagram shows the retrospective view of the trial.

The last diagram for this trial shows the trial from the viewpoint of blinded participants. As in the simple parallel trial in Example Trial 1, blinded participants see only 1 sequence of elements; during the treatment epochs they do not know which of the treatment elements a subject is in.

The following table illustrates the trial design matrix for this crossover example trial. It corresponds closely to the preceding retrospective diagram.

It is straightforward to produce the TA dataset for this crossover trial from the diagram showing arms and epochs, or from the trial design matrix.

### §7.2.1.1 Trial Arms Issues – Distinguishing Between Branches and Transitions

Both the Branch and Transition columns contain rules, but the 2 columns represent 2 different types of rules.

Branch rules represent forks in the trial flowchart, giving rise to separate arms.

The rule underlying a branch in the trial design appears in multiple records, once for each "fork" of the branch.

Within any one record, there is no choice (no "if" clause) in the value of the branch condition.

For example, the value of TABRANCH for a record in arm A is "Randomized to Arm A" because a subject in arm A must have been randomized to arm A.

Transition rules are used for choices within an arm.

The value for TATRANS does contain a choice (an "if" clause).

In Example Trial 4, subjects who receive 1, 2, 3, or 4 cycles of treatment A are all considered to belong to arm A.

In modeling a trial, decisions may have to be made about whether a decision point in the flow chart represents the separation of paths that represent different arms, or paths that represent variations within the same arm, as illustrated in the discussion of Example Trial 7.

This decision will depend on the comparisons of interest in the trial.

Some trials refer to groups of subjects who follow a particular path through the trial as "cohorts," particularly if the groups are formed successively over time.

The term "cohort" is used with different meanings in different protocols and does not always correspond to an arm.

### §7.2.2.1 Trial Elements Issues – Distinguishing Elements, Study Cells, and Epochs

It is easy to confuse elements, which are reusable trial building blocks, with study cells (which contain the elements for a particular epoch and Arm) and with epochs (which are time periods for the trial as a whole).

In part, this is because many trials have epochs for which the same element appears in all arms.

In other words, in the trial design matrix for many trials, there are columns (Epochs) in which all the study cells have the same contents.

It also is natural to use the same name (e.g., screen, follow-up) for both such an epoch and the single element that appears within it.

Confusion can also arise from the fact that in the blinded treatment portions of blinded trials, blinded participants do not know which element a subject is in, but do know what epoch the subject is in.

In describing a trial, one way to avoid confusion between elements and epochs is to include "Element" or "Epoch" in the values of ELEMENT or EPOCH when these values (e.g., screening, follow-up) would otherwise be the same.

It becomes tedious to do this in every case, but can be useful to resolve confusion when it arises or is likely to arise.

The difference between epoch and element is perhaps clearest in crossover trials.

In TA Example Trial 2, as for most crossover trials, the analysis of pharmacokinetic (PK) results would include both treatment and period effects in the model.

“Treatment effect” derives from element (placebo, 5 mg, 10 mg), whereas “period effect” derives from the epoch (first, second, or third treatment epoch).

### §7.2.2.1 Trial Elements Issues – Transitions Between Elements

The transition between one element and the next can be thought of as a 3-step process:

Note that the subject is not "in limbo" during this process.

The subject remains in the current element until step 3, at which point the subject transitions to the new element.

There are no gaps between elements.

As illustrated in the table, executing a transition depends on information that is split between the TE and the TA datasets.

It can be useful, in the process of working out the Trial Design (TD) datasets, to create a dataset that supplements the TA dataset with the TESTRL, TEENRL, and TEDUR variables, so that full information on the transitions is easily accessible.

However, such a working dataset is not an SDTM dataset, and should not be submitted.

The following table shows a fragment of such a table for TA Example Trial 4.

Note that
- for all records that contain a particular element, all the TE variable values are exactly the same; and
- when both TABRANCH and TATRANS are blank, the implicit decision in step 2 is that the subject moves to the next element in sequence for the arm.

Note that rows 2 and 4 of this dataset involve the same element (Trt A); thus, TESTRL is the same for both.

The activity that marks a subject's entry into the fourth element in arm A is "First dose of treatment Element, where drug is Treatment A."

This is not the subject's very first dose of treatment A, but it is their first dose in this element.

## TA-Specific Assumptions

The TA and TE datasets are interrelated, and they provide the building blocks for the development of subject-level treatment information (see Sections 5.2, Demographics (DM), and 5.3, Subject Elements (SE), for the subject's actual study treatment information).

1. TAETORD is an integer. In general, the value of TAETORD is 1 for the first element in each arm, 2 for the second element in each arm, and so on. Occasionally, it may be convenient to skip some values (see Example Trial 6). Although the values of TAETORD need not always be sequential, their order must always be the correct order for the elements in the arm path.

2. Elements in different arms with the same value of TAETORD may or may not be at the same time, depending on the design of the trial. The example trials illustrate a variety of possible situations. The same element may occur more than once within an arm.

3. TABRANCH describes the outcome of a branch decision point in the trial design for subjects in the arm. A branch decision point takes place between epochs, and is associated with the element that ends at the decision point. For instance, if subjects are assigned to an arm where they receive treatment A through a randomization at the end of element X, the value of TABRANCH for element X would be "Randomized to A."

4. Branch decision points may be based on decision processes other than randomizations (e.g., clinical evaluations of disease response, subject choice).

5. There is usually some gap in time between the performance of a randomization and the start of randomized treatment. However, in many trials this gap in time is small and it is highly unlikely that subjects will leave the trial between randomization and treatment. In these circumstances, the trial does not need to be modeled with this time period between randomization and start of treatment as a separate element.

6. Some trials include multiple paths that are closely enough related so that they are all considered to belong to 1 arm. In general, this set of paths will include a "complete" path along with shorter paths that skip some elements. The sequence of elements represented in the trial arms should be the complete, longest path. TATRANS describes the decision points that may lead to a shortened path within the arm.

7. If an element does not end with a decision that could lead to a shortened path within the arm, then TATRANS will be blank. If there is such a decision, TATRANS will be in a form like, "If condition X is true, then go to epoch Y" or "If condition X is true, then go to element with TAETORD = 'Z'".

8. EPOCH is not strictly necessary for describing the sequence of elements in an arm path, but it is the conceptual basis for comparisons between arms and also provides a useful way to talk about what is happening in a blinded trial while it is blinded. During periods of blinded treatment, blinded participants will not know which arm and element a subject is in, but EPOCH should provide a description of the time period that does not depend on knowing arm.

9. EPOCH should be assigned in such a way that elements from different arms with the same value of EPOCH are "comparable" in some sense. The degree of similarity of epochs across arms varies considerably in different trials, as illustrated in the examples.

10. EPOCH values for multiple similar epochs:
    a. When a study design includes multiple epochs with the same purpose (e.g., multiple similar treatment epochs), it is recommended that the EPOCH values be terms from controlled terminology, but with numbers appended. For example, multiple treatment epochs could be represented using "TREATMENT 1", "TREATMENT 2", and so on. Because the codelist is extensible, this convention allows multiple similar epochs to be represented without adding numbered terms to the CDISC Controlled Terminology for epoch. The inclusion of multiple numbered terms in the EPOCH codelist is not considered to add value.
    b. Note that the controlled terminology does include some more granular terms for distinguishing between epochs that differ in ways other than mere order, and these terms should be used where applicable, as they are more informative. For example, when "BLINDED TREATMENT" and "OPEN LABEL TREATMENT" are applicable, those terms would be preferred over "TREATMENT 1" and "TREATMENT 2".

11. Note that study cells are not explicitly defined in the TA dataset. A set of records with a common value of both ARMCD and EPOCH constitute the description of a study cell. Transition rules within this set of records are also part of the description of the study cell.

12. EPOCH may be used as a timing variable in other datasets, such as Exposure (EX) and Disposition (DS), and values of EPOCH must be different for different epochs. For instance, in a crossover trial with 3 treatment epochs, each must be given a distinct name; all 3 cannot be called "TREATMENT".
