# TI — Assumptions

## §7.4 Trial Eligibility and Summary (TI, TS) — Introduction

This section contains the Trial Design (TD) datasets that describe:

- Subject eligibility criteria for trial participation (Section 7.4.1, Trial Inclusion/Exclusion Criteria (TI))
- The characteristics of the trial (Section 7.4.2, Trial Summary (TS))

The TI and TS datasets are tabular synopses of parts of the study protocol.

## TI – Assumptions

The variable TIRL was included in the Trial Inclusion/Exclusion Criteria (TI) domain in anticipation of developing a way to represent eligibility criteria in a computer-executable manner. However, such a method has not been developed, and it is not clear that an SDTM dataset would be the best place to represent such a computer-executable representation.

TI contains all the inclusion and exclusion criteria for the trial, and thus provides information that may not be present in the subject-level data on inclusion and exclusion criteria. The IE domain (described in Section 6.3.4, Inclusion/Exclusion Criteria Not Met) contains records only for inclusion and exclusion criteria that subjects did not meet.

1. If inclusion/exclusion criteria were amended during the trial, then each complete set of criteria must be included in the TI domain. TIVERS is used to distinguish between the versions.

2. Protocol version numbers should be used to identify criteria versions, although there may be more versions of the protocol than versions of the inclusion/exclusion criteria. For example, a protocol might have versions 1, 2, 3, and 4, but if the inclusion/exclusion criteria in version 1 were unchanged through versions 2 and 3, and changed only in version 4, then there would be 2 sets of inclusion/exclusion criteria in TI: one for version 1 and one for version 4.

3. Individual criteria do not have versions. If a criterion changes, it should be treated as a new criterion, with a new value for IETESTCD. If criteria have been numbered and values of IETESTCD are generally of the form INCL00n or EXCL00n, and new versions of a criterion have not been given new numbers, separate values of IETESTCD might be created by appending letters (e.g., INCL003A, INCL003B).

4. IETEST contains the text of the inclusion/exclusion criterion. However, because entry criteria are rules, the variable TIRL has been included in anticipation of the development of computer-executable rules.

5. If a criterion text is <200 characters, it goes in IETEST; if the text is >200 characters, put meaningful text in IETEST and describe the full text in the study metadata. See Section 4.5.3.1, Test Name (--TEST) Greater than 40 Characters, for further information.

## §7.5 How to Model the Design of a Clinical Trial

The following steps allow the modeler to move from more-familiar concepts, such as arms, to less-familiar concepts, such as elements and epochs.

The actual process of modeling a trial may depart from these numbered steps.

Some steps will overlap; there may be several iterations; and not all steps are relevant for all studies.

1. Start from the flow chart or schema diagram usually included in the trial protocol. This diagram will show how many arms the trial has, and the branch points or decision points where the arms diverge.
2. Write down the decision rule for each branching point in the diagram. Does the assignment of a subject to an arm depend on a randomization? On whether the subject responded to treatment? On some other criterion?
3. If the trial has multiple branching points, check whether all the branches that have been identified really lead to different arms. The arms will relate to the major comparisons the trial is designed to address. For some trials, there may be a group of somewhat different paths through the trial that are all considered to belong to a single arm.
4. For each arm, identify the major time periods of treatment and non-treatment a subject assigned to that arm will go through. These are the elements, or building blocks, of which the arm is composed.
5. Define the starting point of each element. Define the rule for how long the element should last. Determine whether the element is of fixed duration.
6. Re-examine the sequences of elements that make up the various arms and consider alternative element definitions. Would it be better to "split" some elements into smaller pieces or "lump" some elements into larger pieces? Such decisions will depend on the aims of the trial and plans for analysis.
7. Compare the various arms. In most clinical trials, especially blinded trials, the pattern of elements will be similar for all arms, and it will make sense to define trial epochs. Assign names to these epochs. During the conduct of a blinded trial, it will not be known which arm a subject has been assigned to, or which treatment elements they are experiencing, but the epochs they are passing through will be known.
8. Identify the visits planned for the trial. Define the planned start timings for each visit, expressed relative to the ordered sequences of elements that make up the arms. Define the rules for when each visit should end.
9. For oncology trials or other trials with disease assessments that are not necessarily tied to visits, find the planned timing of disease assessments in the protocol and record it in the Trial Disease Assessments (TD) dataset.
10. If the protocol includes data collection that is triggered by the occurrence of certain events, interventions, or findings, record those triggers in the Trial Disease Milestones (TM) dataset. Note that disease milestones may be pre- (e.g., disease diagnosis) or on-study.
11. Identify the inclusion and exclusion criteria to be able to populate the Trial Inclusion/Exclusion Criteria (TI) dataset. If inclusion and exclusion criteria were amended so that subjects entered under different versions, populate TIVERS to represent the different versions.
12. Populate the TS dataset with summary information.
