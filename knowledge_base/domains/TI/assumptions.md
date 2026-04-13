# TI — Assumptions

The variable TIRL was included in the Trial Inclusion/Exclusion Criteria (TI) domain in anticipation of developing a way to represent eligibility criteria in a computer-executable manner. However, such a method has not been developed, and it is not clear that an SDTM dataset would be the best place to represent such a computer-executable representation.

TI contains all the inclusion and exclusion criteria for the trial, and thus provides information that may not be present in the subject-level data on inclusion and exclusion criteria. The IE domain (described in Section 6.3.4, Inclusion/Exclusion Criteria Not Met) contains records only for inclusion and exclusion criteria that subjects did not meet.

1. If inclusion/exclusion criteria were amended during the trial, then each complete set of criteria must be included in the TI domain. TIVERS is used to distinguish between the versions.

2. Protocol version numbers should be used to identify criteria versions, although there may be more versions of the protocol than versions of the inclusion/exclusion criteria. For example, a protocol might have versions 1, 2, 3, and 4, but if the inclusion/exclusion criteria in version 1 were unchanged through versions 2 and 3, and changed only in version 4, then there would be 2 sets of inclusion/exclusion criteria in TI: one for version 1 and one for version 4.

3. Individual criteria do not have versions. If a criterion changes, it should be treated as a new criterion, with a new value for IETESTCD. If criteria have been numbered and values of IETESTCD are generally of the form INCL00n or EXCL00n, and new versions of a criterion have not been given new numbers, separate values of IETESTCD might be created by appending letters (e.g., INCL003A, INCL003B).

4. IETEST contains the text of the inclusion/exclusion criterion. However, because entry criteria are rules, the variable TIRL has been included in anticipation of the development of computer-executable rules.

5. If a criterion text is <200 characters, it goes in IETEST; if the text is >200 characters, put meaningful text in IETEST and describe the full text in the study metadata. See Section 4.5.3.1, Test Name (--TEST) Greater than 40 Characters, for further information.
