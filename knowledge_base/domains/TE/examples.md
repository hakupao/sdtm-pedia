# TE — Examples

Both of the trials in TA Examples 1 and 2 (see Section 7.2.1, Trial Arms) are assumed to have fixed-duration elements. The wording in TESTRL is intended to separate the description of the event that starts the element into the part that would be visible to a blinded participant in the trial (e.g., "First dose of a treatment epoch") from the part that is revealed when the study is unblinded (e.g., "where dose is 5 mg"). Care must be taken in choosing these descriptions to be sure that they are arm- and epoch-neutral. For instance, in a crossover trial such as TA Example Trial 3, where an element may appear in 1 of multiple epochs, the wording must be appropriate for all possible epochs (e.g., "OPEN LABEL TREATMENT"). The SDS Team is considering adding a separate variable to the TE dataset that would hold information on the treatment that is associated with an element. This would make it clearer which elements are "treatment elements" and, therefore, which epochs contain treatment elements and thus are "treatment Epochs."

## Example 1

This example shows the TE dataset for TA Example Trial 1.

**te.xpt**

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
|-----|---------|--------|------|---------|--------|--------|-------|
| 1 | EX1 | TE | SCRN | Screen | Informed consent | 1 week after start of Element | P7D |
| 2 | EX1 | TE | RI | Run-In | Eligibility confirmed | 2 weeks after start of Element | P14D |
| 3 | EX1 | TE | P | Placebo | First dose of study drug, where drug is placebo | 2 weeks after start of Element | P14D |
| 4 | EX1 | TE | A | Drug A | First dose of study drug, where drug is Drug A | 2 weeks after start of Element | P14D |
| 5 | EX1 | TE | B | Drug B | First dose of study drug, where drug is Drug B | 2 weeks after start of Element | P14D |

## Example 2

This example shows the TE dataset for TA Example Trial 2.

**te.xpt**

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
|-----|---------|--------|------|---------|--------|--------|-------|
| 1 | EX2 | TE | SCRN | Screen | Informed consent | 2 weeks after start of Element | P14D |
| 2 | EX2 | TE | P | Placebo | First dose of a treatment Epoch, where dose is placebo | 2 weeks after start of Element | P14D |
| 3 | EX2 | TE | 5 | 5 mg | First dose of a treatment Epoch, where dose is 5 mg drug | 2 weeks after start of Element | P14D |
| 4 | EX2 | TE | 10 | 10 mg | First dose of a treatment Epoch, where dose is 10 mg drug | 2 weeks after start of Element | P14D |
| 5 | EX2 | TE | REST | Rest | 48 hrs after last dose of preceding treatment Epoch | 1 week after start of Element | P7D |
| 6 | EX2 | TE | FU | Follow-up | 48 hrs after last dose of third treatment Epoch | 3 weeks after start of Element | P21D |

## Example 3

The TE dataset for TA Example Trial 4 illustrates element end rules for elements that are not all of fixed duration. The screen element in this study can be up to 2 weeks long, but because it may end earlier it is not of fixed duration. The rest element has a variable length, depending on how quickly WBC recovers. Note that the start rules for the A and B elements have been written to be suitable for a blinded study.

**te.xpt**

| Row | STUDYID | DOMAIN | ETCD | ELEMENT | TESTRL | TEENRL | TEDUR |
|-----|---------|--------|------|---------|--------|--------|-------|
| 1 | EX4 | TE | SCRN | Screen | Informed Consent | Screening assessments are complete, up to 2 weeks after start of Element | |
| 2 | EX4 | TE | A | Trt A | First dose of treatment Element, where drug is Treatment A | 5 days after start of Element | P5D |
| 3 | EX4 | TE | B | Trt B | First dose of treatment Element, where drug is Treatment B | 5 days after start of Element | P5D |
| 4 | EX4 | TE | REST | Rest | Last dose of previous treatment cycle + 24 hrs | At least 16 days after start of Element and WBC recovered | |
| 5 | EX4 | TE | FU | Follow-up | Decision not to treat further | 4 weeks | P28D |

## Trial Elements Issues

### Granularity of Trial Elements

Deciding how finely to divide trial time when identifying trial elements is a matter of judgment, as illustrated by the following examples:

1. TA Example Trial 2 was represented using 3 treatment epochs separated by 2 washout epochs and followed by a follow-up epoch. This might have been modeled using 3 treatment epochs that included both the 2-week treatment period and the 1-week rest period. Because the first week after the third treatment period would be included in the third treatment epoch, the follow-up epoch would then have a duration of 2 weeks.

2. In TA Example Trials 4, 5, and 6, separate treatment and rest elements were identified. However, the combination of treatment and rest could be represented as a single element.

3. A trial might include a dose titration, with subjects receiving increasing doses on a weekly basis until certain conditions are met. The trial design could be modeled in any of the following ways:
    a. Using several 1-week elements at specific doses, followed by an element of variable length at the chosen dose
    b. As a titration element of variable length followed by a constant dosing element of variable length
    c. One element with dosing determined by titration.

The choice of elements used to represent this dose titration will depend on the objectives of the trial and how the data will be analyzed and reported. If it is important to examine side effects or lab values at each individual dose, the first model is appropriate. If it is important only to identify the time to completion of titration, the second model might be appropriate. If the titration process is routine and is of little interest, the third model might be adequate for the purposes of the trial.

### Distinguishing Elements, Study Cells, and Epochs

It is easy to confuse elements, which are reusable trial building blocks, with study cells (which contain the elements for a particular epoch and Arm) and with epochs (which are time periods for the trial as a whole). In part, this is because many trials have epochs for which the same element appears in all arms. In other words, in the trial design matrix for many trials, there are columns (Epochs) in which all the study cells have the same contents. It also is natural to use the same name (e.g., screen, follow-up) for both such an epoch and the single element that appears within it.

Confusion can also arise from the fact that in the blinded treatment portions of blinded trials, blinded participants do not know which element a subject is in, but do know what epoch the subject is in.

In describing a trial, one way to avoid confusion between elements and epochs is to include "Element" or "Epoch" in the values of ELEMENT or EPOCH when these values (e.g., screening, follow-up) would otherwise be the same. It becomes tedious to do this in every case, but can be useful to resolve confusion when it arises or is likely to arise.

The difference between epoch and element is perhaps clearest in crossover trials. In TA Example Trial 2, as for most crossover trials, the analysis of pharmacokinetic (PK) results would include both treatment and period effects in the model. "Treatment effect" derives from element (placebo, 5 mg, 10 mg), whereas "period effect" derives from the epoch (first, second, or third treatment epoch).

### Transitions Between Elements

The transition between one element and the next can be thought of as a 3-step process:

| Step | Step question | How step question is answered by information in the TA datasets |
|------|---|---|
| 1 | Should the subject leave the current element? | The criteria for ending the current element are in TEENRL in the TE dataset. |
| 2 | Which element should the subject enter next? | If there is a branch at this point in the trial, evaluate criteria described in TABRANCH (e.g., randomization results) in the TA dataset. Otherwise, if TATRANS in the TA dataset is populated in this arm at this point, follow those instructions. Otherwise, move to the next element in this arm as specified by TAETORD in the TA dataset. |
| 3 | What does the subject do to enter the next element? | The action or event that marks the start of the next element is specified in TESTRL in the TE dataset. |

Note that the subject is not "in limbo" during this process. The subject remains in the current element until step 3, at which point the subject transitions to the new element. There are no gaps between elements.
