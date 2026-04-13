# SM — Assumptions

1. Disease milestones are observations or activities whose timings are of interest in the study. The types of disease milestones are defined at the study level in the TM dataset. The purpose of the SM dataset is to provide a summary timeline of the milestones for a particular subject.

2. The name of the disease milestone is recorded in MIDS.
   a. For disease milestones that can occur only once (TMRPT = "N"), the value of MIDS may be the value in MIDSTYPE or may an abbreviated version.
   b. For types of disease milestones that can occur multiple times, MIDS will usually be an abbreviated version of MIDSTYPE and will always end with a sequence number. Sequence numbers should start with 1 and indicate the chronological order of the instances of this type of disease milestone.

3. The timing variables SMSTDTC and SMENDTC hold start and end date/times of data collected for the disease milestone(s) for each subject. SMSTDY and SMENDY represent the corresponding study day variables.
   a. The start date/time of the disease milestone is the critical date/time, and must be populated. If the disease milestone is an event, then the meaning of "start date" for the event may need to be defined.
   b. The start study day will not be populated if the start date/time includes only a year or only a year and month.
   c. The end date/time for the disease milestone is less important than the start date/time. It will not be populated if the disease milestone is a finding without an end date/time or if it is an event or intervention for which an end date/time has not yet occurred or was not collected.
   d. The end study day will not be populated if the end date/time includes only a year or only a year and month.
