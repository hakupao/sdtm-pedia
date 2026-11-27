# T4.1 补检包 6/8 — FIG + TRIAGE_RELOCATE + TRIAGE_LOCATE + RULE_C1-manual-PDF+KB + RULE_C7-K4-rereview + RULE_T2-fix+deltaRereviewPASS+auditPASS + RULE_T1-two-agent (27 条, 全检, 不抽样)

> 由 `scripts/t4/t4_supp_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续.

### 133. `ig34_p0044_a023` — supp:FIG

- PDF 页 44 · 原子类型 FIGURE · 所在节 `§4.4.7 [Use of Relative Timing Variables]`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 PARTIAL) · 判定规则 `FIGURE` · 批 `T1:pack_028`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Timeline diagram showing MHENTPT as 'Assessment Date and Reference Time Point of 2006-11-02' with 2002 start marker at left; box at 2006-11-02 shows MHDTC=2006-11-02, MHSTDTC=2002, MHENRTPT=ONGOING, MHENTPT=2006-11-02; annotation: Medical event began in 2002 and was ongoing at the reference time point of 2006-11-02. The medical event may or may not have ended at any time after that.]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0044.txt` 第 14-27 行 (自动定位, 词覆盖 0.628; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 13|     •    End values: An observation can end BEFORE the reference point, can end COINCIDENT with the
 14|          reference point, can end AFTER the reference point, can be known that it did not end but was ONGOING,
 15|          or it can be UNKNOWN when it ended or if it was ongoing.
 16| Although "DURING" and "DURING/AFTER" are in the STENRF codelist, they describe timing relative to an
 17| interval of time rather than a point in time, so are not allowable for use with --STRTPT and --ENRTPT variables.
 18| Examples of --STRTPT, --STTPT, --ENRTPT, and --ENTPT
 19| Example 1: Medical History
 20| Assumptions:
 21|     •    CRF contains "Year Started" and checkbox for "Active"
 22|     •    "Date of Assessment" is collected
 23| Example when "Active" is checked:
 24|     •    MHDTC = date of assessment value (e.g., "2006-11-02")
 25|     •    MHSTDTC = year of condition start (e.g., "2002")
 26|     •    MHENRTPT = "ONGOING"
 27|     •    MHENTPT = date of assessment value (e.g., "2006-11-02")
 28| Figure. Example of --ENRTPT and --ENTPT for Medical History
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:933` (来源: triage kb_loc knowledge_base/chapters/ch04_general_assumptions.md:933 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 931| 
 932| The variables --STRF and --ENRF represent the timing of an observation relative to the sponsor-defined study reference period, when information such as "BEFORE", "PRIOR", "ONGOING", or "CONTINUING" is collected in lieu of a date and this collected information is in relation to the sponsor-defined study reference period. The sponsor-defined study reference period is the continuous period of time defined by the discrete starting point, RFSTDTC, and the discrete ending point, RFENDTC, for each subject in the Demographics (DM) dataset.
 933| 
 934| --STRF is used to identify the start of an observation relative to the sponsor-defined study reference period. --ENRF is used to identify the end of an observation relative to the sponsor-defined study reference period.
 935| 
~~~~

### 134. `ig34_p0387_a011` — supp:FIG

- PDF 页 387 · 原子类型 FIGURE · 所在节 `§7.2.1 Trial Arms (TA) – Example 1`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 MISSING) · 判定规则 `FIGURE` · 批 `T1:pack_014`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 1, Parallel Design Study Schema — block diagram showing Screen block (pink) leading via arrow to Run-In block (blue) with 3 red arrows branching to Placebo (green), Drug A (yellow), Drug B (light blue) blocks. Randomization label with upward arrow at bottom.]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0387.txt` 第 25-35 行 (自动定位, 词覆盖 0.579; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 24| to the 3 possible left-to-right "paths" through the trial. Each path corresponds to 1 of the 3 treatment elements at the
 25| right end of the diagram. Randomization is represented by the 3 red arrows leading from the Run-in block.
 26| Example Trial 1, Parallel Design Study Schema
 27| 
 28| 
 29| 
 30| 
 31| The next diagram for this trial shows the 3 epochs of the trial, indicates the 3 arms, and shows the sequence of
 32| elements for each group of subjects in each epoch. The arrows are at the right side of the diagram because it is at the
 33| end of the trial that all the separate paths through the trial can be seen. Note that, in this diagram, randomization—
 34| which was shown using 3 red arrows connecting the Run-in block with the 3 treatment blocks in the first diagram—
 35| is indicated by a note with an arrow pointing to the line between 2 epochs.
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:26-30` (来源: near triage kb_loc knowledge_base/domains/TA/examples.md:32 (score 0.526)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  26| In this type of document, diagrams are drawn using "blocks" corresponding to trial elements rather than horizontal lines. Trial elements are the various treatment and non-treatment time periods of the trial and we want to emphasize the separate trial elements might otherwise be "hidden" in a single horizontal line. See Section 7.2.2, Trial Elements (TE), for more information about defining trial elements. In general, the elements of a trial will be fairly clear. However, in the process of working out a trial design, alternative definitions of trial elements may be considered, in which case diagrams for each alternative may be constructed.
  27| 
  28| In the study schema diagrams in this example, the only slanting lines used are those that represent branches (i.e., decision points where subjects are divided into separate treatment groups). One advantage of this style of diagram, which does not show convergence of separate paths into a single block, is that the number of arms in the trial can be determined by counting the number of parallel paths at the right end of the diagram.
  29| 
  30| As illustrated in the study schema diagram for Example Trial 1, this simple parallel trial has 3 arms, corresponding to the 3 possible left-to-right "paths" through the trial. Each path corresponds to 1 of the 3 treatment elements at the right end of the diagram. Randomization is represented by the 3 red arrows leading from the Run-in block.
~~~~

### 135. `ig34_p0388_a001` — supp:FIG

- PDF 页 388 · 原子类型 FIGURE · 所在节 `§7.2.1 Trial Arms (TA) – Example 1`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 MISSING) · 判定规则 `FIGURE` · 批 `T1:pack_014`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 1, Parallel Design Prospective View — grid diagram with 3 columns (Screening Epoch, Run-in Epoch, Treatment Epoch) and 3 rows (Placebo arm, Drug A arm, Drug B arm). Each cell shows element block. Arms labeled with arrows (Placebo, Drug A, Drug B) on right. Randomization label with upward arrow at bottom.]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0389.txt` 第 32-44 行 (自动定位, 词覆盖 0.561; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 31| 6        EX1       TA       A       A         3         A      Drug A                                        TREATMENT
 32| 7        EX1       TA       B       B         1         SCRN   Screen                                        SCREENING
 33| 8        EX1       TA       B       B         2         RI     Run-In      Randomized to Drug B              RUN-IN
 34| 9        EX1       TA       B       B         3         B      Drug B                                        TREATMENT
 35| 
 36| Example 2
 37| The following diagram for a crossover trial does not use the crossing slanted lines sometimes used to represent
 38| crossover trials, because the order of the blocks is sufficient to represent the design of the trial. Slanted lines are
 39| used only to represent the branch point at randomization, when a subject is assigned to a sequence of treatments. As
 40| in most crossover trials, the arms are distinguished by the order of treatments, with the same treatments present in
 41| each arm. Note that even though all 3 arms of this trial end with the same block (i.e., the block for the follow-up
 42| element), the diagram does not show the arms converging into one block. Also note that the same block (the “rest”
 43| element) occurs twice within each arm. Elements are conceived of as “reusable” and can appear in more than 1 arm,
 44| in more than 1 epoch, and more than once in an arm.
 45| 
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:49-53` (来源: near triage kb_loc knowledge_base/domains/TA/examples.md:47 (score 0.634)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  49| The next diagram for this trial shows the 3 epochs of the trial, indicates the 3 arms, and shows the sequence of elements for each group of subjects in each epoch. The arrows are at the right side of the diagram because it is at the end of the trial that all the separate paths through the trial can be seen. Note that, in this diagram, randomization—which was shown using 3 red arrows connecting the Run-in block with the 3 treatment blocks in the first diagram—is indicated by a note with an arrow pointing to the line between 2 epochs.
  50| 
  51| **Prospective View**
  52| 
  53| > KB note (not in SDTMIG): the following Mermaid diagram is a KB rendering of the PDF figure "Example Trial 1, Parallel Design Prospective View".
~~~~

### 136. `ig34_p0388_a003` — supp:FIG

- PDF 页 388 · 原子类型 FIGURE · 所在节 `§7.2.1 Trial Arms (TA) – Example 1`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 MISSING) · 判定规则 `FIGURE` · 批 `T1:pack_014`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 1, Parallel Design Retrospective View — grid with 3 rows (Placebo arm, Drug A arm, Drug B arm) and 3 columns (Screening Epoch, Run-in Epoch, Treatment Epoch). Each cell shows labeled element block (Screen, Run-In, Placebo/Drug A/Drug B). Arms labeled (Placebo, Drug A, Drug B) with arrows on right. Randomization label at bottom.]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0388.txt` 第 7-18 行 (自动定位, 词覆盖 0.59; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  6| The next diagram can be thought of as the retrospective view of a trial, the view back from a point in time when a
  7| subject’s assignment to an arm is known. In this view, the trial appears as a grid, with an arm represented by a series
  8| of study cells, one for each epoch, and a sequence of elements within each study cell. In this example (as in many
  9| trials), there is exactly 1 element in each study cell. Later examples will illustrate that this is not always the case.
 10| 
 11| Example Trial 1, Parallel Design Retrospective View
 12| 
 13| 
 14| 
 15| 
 16| The next diagram shows the trial from the viewpoint of blinded participants. To blinded participants in this trial, all
 17| arms look alike. They know when a subject is in the screen element or the run-in element, but when a subject is in
 18| the treatment epoch, participants know only that the subject is receiving a study drug, not which study drug, and
 19| therefore not which element.
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:68` (来源: triage kb_loc knowledge_base/domains/TA/examples.md:68 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  66|         B[Drug B]
  67|     end
  68|     S --> RI
  69|     RI --> P
  70|     RI --> A
~~~~

### 137. `ig34_p0388_a005` — supp:FIG

- PDF 页 388 · 原子类型 FIGURE · 所在节 `§7.2.1 Trial Arms (TA) – Example 1`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 MISSING) · 判定规则 `FIGURE` · 批 `T1:pack_014`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 1, Parallel Design Blinded View — single row grid with 3 columns (Screening Epoch, Run-In Epoch, Treatment Epoch). Elements shown: Screen (pink), Run-In (blue), Study Drug (light blue). Blind label (orange) on right. Randomization label at bottom.]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0387.txt` 第 21-34 行 (自动定位, 词覆盖 0.514; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 20| decision points where subjects are divided into separate treatment groups). One advantage of this style of diagram,
 21| which does not show convergence of separate paths into a single block, is that the number of arms in the trial can be
 22| determined by counting the number of parallel paths at the right end of the diagram.
 23| As illustrated in the study schema diagram for Example Trial 1, this simple parallel trial has 3 arms, corresponding
 24| to the 3 possible left-to-right "paths" through the trial. Each path corresponds to 1 of the 3 treatment elements at the
 25| right end of the diagram. Randomization is represented by the 3 red arrows leading from the Run-in block.
 26| Example Trial 1, Parallel Design Study Schema
 27| 
 28| 
 29| 
 30| 
 31| The next diagram for this trial shows the 3 epochs of the trial, indicates the 3 arms, and shows the sequence of
 32| elements for each group of subjects in each epoch. The arrows are at the right side of the diagram because it is at the
 33| end of the trial that all the separate paths through the trial can be seen. Note that, in this diagram, randomization—
 34| which was shown using 3 red arrows connecting the Run-in block with the 3 treatment blocks in the first diagram—
 35| is indicated by a note with an arrow pointing to the line between 2 epochs.
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:92` (来源: triage kb_loc knowledge_base/domains/TA/examples.md:92 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  90|         SB[Screen]
  91|     end
  92|     subgraph RE["Run-In Epoch"]
  93|         RIP[Run-In]
  94|         RIA[Run-In]
~~~~

### 138. `ig34_p0397_a005` — supp:FIG

- PDF 页 397 · 原子类型 FIGURE · 所在节 `§7.2.1 Trial Arms (TA) – Example 5`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 MISSING) · 判定规则 `FIGURE` · 批 `T1:pack_014`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 5, Different Chemo Durations Study Schema — diagram showing Screen block at left branching at Randomization to Drug A arm (Drug A box + Rest box → Follow box, with curved arrow 'Repeat until disease progression', label 'Total length Drug A cycle: 3 weeks') and Drug B arm (B box + Rest box → Follow box, label 'Total length Drug B cycle: 3 weeks')]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0396.txt` 第 9-22 行 (自动定位, 词覆盖 0.513; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  8| 
  9| The trial design matrix for this example trial corresponds to the diagram showing the retrospective view, with
 10| explicit repeats of the treatment and rest elements. As previously noted, the trial design matrix does not include
 11| information regarding when randomization occurs; similarly, information corresponding to the skip-forward rules is
 12| not represented in the trial design matrix.
 13| Trial Design Matrix
 14| 
 15|      Screen Treatment                                      Follow-up
 16| A Screen Trt A Rest Trt A Rest Trt A Rest Trt A Rest Follow-up
 17| B Screen Trt B Rest Trt B Rest Trt B Rest Trt B Rest Follow-up
 18| 
 19| The TA dataset for this example trial requires the use of the TATRANS variable to represent the "repeat until
 20| disease progression" feature (the green "skip forward" arrow represented this rule in the diagrams). In the TA
 21| dataset, TATRANS is populated for each element with a green arrow in the diagram. In other words, if there is a
 22| possibility that a subject will, at the end of this element, skip forward to a later part of the arm, then TATRANS is
 23| populated with the rule describing the conditions under which a subject will go to a later element. If the subject
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:500` (来源: triage kb_loc knowledge_base/domains/TA/examples.md:500 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 498| | **A-Rescue** | Screen | Treatment A | Rescue |
 499| | **B-Open A** | Screen | Treatment B | Open Drug A |
 500| | **B-Rescue** | Screen | Treatment B | Rescue |
 501| 
 502| Creating the TA dataset for this example trial is similarly straightforward. Note that because there are 2 branch points in this trial, TABRANCH is populated for 2 records in each arm. Note also that the values of ARMCD, like the values of ARM, reflect the 2 separate processes that result in a subject's assignment to an arm.
~~~~

### 139. `ig34_p0397_a009` — supp:FIG

- PDF 页 397 · 原子类型 FIGURE · 所在节 `§7.2.1 Trial Arms (TA) – Example 5`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 PARTIAL) · 判定规则 `FIGURE` · 批 `T1:pack_014`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 5, Cyclical Chemotherapy Retrospective View — diagram showing Screening Epoch, Treatment Epoch (Drug A/Rest with 'Repeat until disease progression' label; B/Rest with 'Repeat until disease progression' label), Follow-up Epoch; arms Drug A and Drug B; Randomization arrow]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0396.txt` 第 9-20 行 (自动定位, 词覆盖 0.69; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  8| 
  9| The trial design matrix for this example trial corresponds to the diagram showing the retrospective view, with
 10| explicit repeats of the treatment and rest elements. As previously noted, the trial design matrix does not include
 11| information regarding when randomization occurs; similarly, information corresponding to the skip-forward rules is
 12| not represented in the trial design matrix.
 13| Trial Design Matrix
 14| 
 15|      Screen Treatment                                      Follow-up
 16| A Screen Trt A Rest Trt A Rest Trt A Rest Trt A Rest Follow-up
 17| B Screen Trt B Rest Trt B Rest Trt B Rest Trt B Rest Follow-up
 18| 
 19| The TA dataset for this example trial requires the use of the TATRANS variable to represent the "repeat until
 20| disease progression" feature (the green "skip forward" arrow represented this rule in the diagrams). In the TA
 21| dataset, TATRANS is populated for each element with a green arrow in the diagram. In other words, if there is a
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:523-527` (来源: near triage kb_loc knowledge_base/domains/TA/examples.md:516 (score 0.724)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 523| ## Example 4
 524| 
 525| > KB note (not in SDTMIG): A cyclical chemotherapy oncology trial with repeating treatment/rest elements until disease progression. 2 arms (Drug A, Drug B), 3 epochs (Screening, Treatment, Follow-Up). The TATRANS variable represents the "repeat until disease progression" skip-forward rule.
 526| 
 527| The following diagram uses a new symbol, a large curved arrow representing the fact that the chemotherapy treatment (A or B) and the rest period that follows it are to be repeated. In this trial, the chemotherapy cycles are to be repeated until disease progression. Although some chemotherapy trials specify a maximum number of cycles, protocols that allow an indefinite number of repeats are not uncommon.
~~~~

### 140. `ig34_p0398_a012` — supp:FIG

- PDF 页 398 · 原子类型 FIGURE · 所在节 `§7.2.1 Trial Arms (TA) – Example 6`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 MISSING) · 判定规则 `FIGURE` · 批 `T1:pack_014`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 6, Different Cycle Durations Study Schema — diagram showing Screen block branching at Randomization to Drug A arm (Drug A + Rest → Follow, curved arrow 'Repeat until disease progression', label 'Total length Drug A cycle: 3 weeks') and Drug B arm (B + Rest → Follow, label 'Total length Drug B cycle: 4 weeks')]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0398.txt` 第 6-17 行 (自动定位, 词覆盖 0.5; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  5| 12     EX5     TA       B       B     4         B     Trt B                                                   TREATMENT
  6| 13     EX5     TA       B       B     5         RESTB Rest B                  If disease progression, go to   TREATMENT
  7|                                                                               Follow-up Epoch
  8| 14     EX5     TA       B       B     6         B     Trt B                                                   TREATMENT
  9| 15     EX5     TA       B       B     7         RESTB Rest B                                                  TREATMENT
 10| 16     EX5     TA       B       B     8         FU    Follow-up                                               FOLLOW-UP
 11| 
 12| Example 6
 13| Example Trial 6 is an oncology trial comparing 2 types of chemotherapy that are given using cycles of different
 14| lengths with different internal patterns. Treatment A is given in 3-week cycles with a longer duration of treatment
 15| and a short rest; treatment B is given in 4-week cycles with a short duration of treatment and a long rest.
 16| 
 17| Example Trial 6, Different Cycle Durations Study Schema
 18| 
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:570` (来源: triage kb_loc knowledge_base/domains/TA/examples.md:570 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 568|     rand["Randomization"] -.-> SE
 569|     style rand fill:#fff,stroke:#999,stroke-dasharray:5 5
 570| ```
 571| 
 572| The next diagram shows the retrospective view of this trial.
~~~~

### 141. `ig34_p0398_a016` — supp:FIG

- PDF 页 398 · 原子类型 FIGURE · 所在节 `§7.2.1 Trial Arms (TA) – Example 6`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 PARTIAL) · 判定规则 `FIGURE` · 批 `T1:pack_014`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 6, Cyclical Chemotherapy Retrospective View — diagram showing Screening Epoch, Treatment Epoch (Drug A/Rest with 'Repeat until disease progression' label, label 'Total length Drug A cycle: 3 weeks'; B/Rest with 'Repeat until disease progression' label, label 'Total length Drug B cycle: 4 weeks'), Follow-up Epoch; arms Drug A and Drug B; Randomization arrow]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0398.txt` 第 6-17 行 (自动定位, 词覆盖 0.514; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  5| 12     EX5     TA       B       B     4         B     Trt B                                                   TREATMENT
  6| 13     EX5     TA       B       B     5         RESTB Rest B                  If disease progression, go to   TREATMENT
  7|                                                                               Follow-up Epoch
  8| 14     EX5     TA       B       B     6         B     Trt B                                                   TREATMENT
  9| 15     EX5     TA       B       B     7         RESTB Rest B                                                  TREATMENT
 10| 16     EX5     TA       B       B     8         FU    Follow-up                                               FOLLOW-UP
 11| 
 12| Example 6
 13| Example Trial 6 is an oncology trial comparing 2 types of chemotherapy that are given using cycles of different
 14| lengths with different internal patterns. Treatment A is given in 3-week cycles with a longer duration of treatment
 15| and a short rest; treatment B is given in 4-week cycles with a short duration of treatment and a long rest.
 16| 
 17| Example Trial 6, Different Cycle Durations Study Schema
 18| 
~~~~

KB 现文: `knowledge_base/domains/TA/examples.md:586` (来源: triage kb_loc knowledge_base/domains/TA/examples.md:586 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 584|     subgraph TE["Treatment Epoch"]
 585|         da["Drug A | Rest<br/>Repeat until disease progression"]
 586|         db["Drug B | Rest<br/>Repeat until disease progression"]
 587|     end
 588|     subgraph FU["Follow-up Epoch"]
~~~~

### 142. `ig34_p0409_a007` — supp:FIG

- PDF 页 409 · 原子类型 FIGURE · 所在节 `§7.3.1 Trial Visits (TV) – Example 1`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 MISSING) · 判定规则 `FIGURE` · 批 `T1:pack_017`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Example Trial 1, Parallel Design Planned Visits — diagram showing 3 arms (Placebo, Drug A, Drug B) with 5 visit number flags across Screening Epoch, Run-In Epoch, and Treatment Epoch, with Randomization arrow at transition between Run-In and Treatment epochs]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0409.txt` 第 3-14 行 (自动定位, 词覆盖 0.618; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  2| Example 1
  3| The following diagram represents visits as numbered "flags" with visit numbers. Each flag has 2 supports, one at the
  4| beginning of the visit and the other at the end of the visit. Note that visits 2 and 3 span epoch transitions. In other
  5| words, the transition event that marks the beginning of the run-in epoch (confirmation of eligibility) occurs during
  6| visit 2, and the transition event that marks the beginning of the treatment epoch (the first dose of study drug) occurs
  7| during visit 3.
  8| 
  9| Example Trial 1, Parallel Design Planned Visits
 10| 
 11| 
 12| 
 13| 
 14| Two TV datasets are shown for this trial. The first shows a somewhat idealized situation, where the protocol has
 15| provided specific timings for the visits. The second shows a more common situation, where the timings have been
~~~~

KB 现文: `knowledge_base/domains/TV/examples.md:5-9` (来源: near triage kb_loc knowledge_base/domains/TV/examples.md:9 (score 0.706)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
   5| The following diagram represents visits as numbered "flags" with visit numbers. Each flag has 2 supports, one at the beginning of the visit and the other at the end of the visit. Note that visits 2 and 3 span epoch transitions. In other words, the transition event that marks the beginning of the run-in epoch (confirmation of eligibility) occurs during visit 2, and the transition event that marks the beginning of the treatment epoch (the first dose of study drug) occurs during visit 3.
   6| 
   7| > KB note (not in SDTMIG): This example is based on TA Example Trial 1, a Parallel Design with 3 arms (Placebo, Drug A, Drug B).
   8| 
   9| **Example Trial 1, Parallel Design Planned Visits**
~~~~

### 143. `ig34_p0440_a009` — supp:FIG

- PDF 页 440 · 原子类型 NOTE · 所在节 `RELSPEC – Examples`
- triage 类 **FIGURE** · 终态 **FIGURE_DEFERRED** (T3 前 PARTIAL) · 判定规则 `FIGURE` · 批 `T1:pack_033`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
[FIGURE: Sample Specimen Relationship — specimen lineage diagram showing parent-child relationships between specimens identified by REFID values SPC-001, SPC-001-A, SPC-001-B, SPC-001-B-1, SPC-003, SPC-003-A]
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0440.txt` 第 10-22 行 (自动定位, 词覆盖 0.545; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
  9| Example 1
 10| This example uses the sample specimen lineage illustrated below.
 11| 
 12| Figure. Sample Specimen Relationship
 13| 
 14| 
 15| 
 16| 
 17| A specimen with a LEVEL value of "1" and a blank value for PARENT indicates a collected sample. All other
 18| values represent a derived sample. SPEC reflects the specimen type for the sample regardless of whether it is
 19| collected or derived.
 20| relspec.xpt
 21| Row        STUDYID   USUBJID   REFID         SPEC     PARENT      LEVEL
 22| 1          ABC-123   001-01    SPC-001       TISSUE               1
 23| 2          ABC-123   001-01    SPC-001-A     TISSUE   SPC-001     2
~~~~

KB 现文: `knowledge_base/domains/RELSPEC/examples.md:9` (来源: triage kb_loc knowledge_base/domains/RELSPEC/examples.md:9 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
   7| This example uses the sample specimen lineage illustrated below.
   8| 
   9| **Figure. Sample Specimen Relationship**
  10| 
  11| > KB note (not in SDTMIG): the following Mermaid diagram is a KB rendering of the PDF figure (Figure. Sample Specimen Relationship); level labels from the figure's row captions are shown as subgroup titles.
~~~~

### 144. `ig34_p0363_a014` — supp:TRIAGE_RELOCATE

- PDF 页 363 · 原子类型 LIST_ITEM · 所在节 `§6.4.2 Naming Findings About Domains`
- triage 类 **RELOCATE** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-FA`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2. A split FA domain following the guidance in Section 4.1.7, Splitting Domains:
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0363.txt` 第 37-37 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36|     1.   A single FA domain, perhaps separated with different FACAT and/or FASCAT values
 37|     2.   A split FA domain following the guidance in Section 4.1.7, Splitting Domains:
 38|          o   The DOMAIN value would be “FA”.
~~~~

KB 现文: `knowledge_base/domains/FA/assumptions.md:60` (来源: decision.evidence.hit):

~~~~
  60| 2. A split FA domain following the guidance in Section 4.1.7, Splitting Domains:
~~~~

### 145. `ig34_p0364_a003` — supp:TRIAGE_RELOCATE

- PDF 页 364 · 原子类型 LIST_ITEM · 所在节 `§6.4.2 Naming Findings About Domains`
- triage 类 **RELOCATE** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-FA`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The DOMAIN value is sponsor-defined and does not begin with FA, following examples in Section 6.4.5, Skin Response, which has a domain code of SR.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0364.txt` 第 5-6 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  4|     3.   Separate domains where:
  5|          o    The DOMAIN value is sponsor-defined and does not begin with FA, following examples in Section
  6|               6.4.5, Skin Response, which has a domain code of SR.
  7|          o    All published FA guidance applies, specifically:
~~~~

KB 现文: `knowledge_base/domains/FA/assumptions.md:68` (来源: decision.evidence.hit):

~~~~
  68|    - The DOMAIN value is sponsor-defined and does not begin with FA, following examples in Section 6.4.5, Skin Response, which has a domain code of SR.
~~~~

### 146. `ig34_p0364_a011` — supp:TRIAGE_RELOCATE

- PDF 页 364 · 原子类型 SENTENCE · 所在节 `§6.4.3 Variables Unique to Findings About`
- triage 类 **RELOCATE** · 终态 **EXACT** (T3 前 PARTIAL) · 判定规则 `live-hit` · 批 `B-FA`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The variable --OBJ is unique to Findings About. In conjunction with FATESTCD, it describes what the topic of the observation is; therefore, both are required to be populated for every record. FATESTCD describes the measurement/evaluation and FAOBJ describes the event or intervention that the measurement/evaluation is about.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0364.txt` 第 18-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| 6.4.3 Variables Unique to Findings About
 18| The variable --OBJ is unique to Findings About. In conjunction with FATESTCD, it describes what the topic of the
 19| observation is; therefore, both are required to be populated for every record. FATESTCD describes the
 20| measurement/evaluation and FAOBJ describes the event or intervention that the measurement/evaluation is about.
 21| When collected data fit a qualifier variable (see SDTM Sections 3.1.1, 3.1.2, and 3.1.3) and are represented in the
~~~~

KB 现文: `knowledge_base/domains/FA/assumptions.md:79` (来源: decision.evidence.hit):

~~~~
  79| The variable --OBJ is unique to Findings About. In conjunction with FATESTCD, it describes what the topic of the observation is; therefore, both are required to be populated for every record. FATESTCD describes the measurement/evaluation and FAOBJ describes the event or intervention that the measurement/evaluation is about.
~~~~

### 147. `ig34_p0039_a014` — supp:RULE_C1-manual-PDF+KB

- PDF 页 39 · 原子类型 LIST_ITEM · 所在节 `§4.4.1 Formats for Date/Time Variables`
- triage 类 **PRESENT** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `C1-manual-PDF+KB` · 批 `T3-C1`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The SDTM and the SDTMIG require use of the ISO 8601 extended format, which requires hyphen delimiters for date components and colon delimiters for time components.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0039.txt` 第 15-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 14|      •   ISO 8601 represents times as a text string using the notation hh:mm:ss(.n+)?(((+|-)hh:mm)|Z)?.
 15|      •   The SDTM and the SDTMIG require use of the ISO 8601 extended format, which requires hyphen
 16|          delimiters for date components and colon delimiters for time components. The ISO 8601 basic format,
 17|          which does not require delimiters, should not be used in SDTM datasets.
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:721-723` (来源: near triage kb_loc knowledge_base/chapters/ch04_general_assumptions.md:722 (score 0.6)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 721| An SDTM DTC variable may include data that is represented in ISO 8601 format as a complete date/time, a partial date/time, or an incomplete date/time.
 722| 
 723| The SDTMIG template uses ISO 8601 for calendar dates and times of day, which are expressed as follows:
~~~~

### 148. `ig34_p0057_a001` — supp:RULE_C1-manual-PDF+KB

- PDF 页 57 · 原子类型 SENTENCE · 所在节 `§4.5.4 [Evaluators in the Interventions and Events Observation Classes]`
- triage 类 **PRESENT** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `C1-manual-PDF+KB` · 批 `T3-C1`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The QEVAL variable can be used to describe the evaluator for any data item in a SUPP-- dataset.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0056.txt` 第 50-50 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 49| which do not include the --EVAL variable, all data are assumed to be attributed to the principal investigator. The
 50| QEVAL variable can be used to describe the evaluator for any data item in a SUPP-- dataset (see Section 8.4.1,
 51| Supplemental Qualifiers – SUPP-- Datasets), but is not required when the data are objective. For observations that
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1369` (来源: triage kb_loc knowledge_base/chapters/ch04_general_assumptions.md:1369 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
1367| - **Rows 4-5:** Two measurements for VSTESTCD = "SYSBP" were done at visit 1.
1368| - **Row 6:** A third measurement for VSTESTCD = "SYSBP" at visit 1 was a derived record, as indicated by VSDRVFL = "Y".
1369| - **Row 7:** At visit 2, there were no Vital Signs results, as indicated by VSTESTCD = "VSALL" and VSSTAT = "NOT DONE".
1370| 
1371| vs.xpt
~~~~

### 149. `ig34_p0441_a003` — supp:RULE_C1-manual-PDF+KB

- PDF 页 441 · 原子类型 SENTENCE · 所在节 `§9 [STUDY REFERENCES]`
- triage 类 **PRESENT** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `C1-manual-PDF+KB` · 批 `T3-C1`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The following situations have been identified thus far:
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0441.txt` 第 3-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| There are occasions when it is necessary to establish study-specific terminology that will be used in tabulated data.
  3| The following situations have been identified thus far:
  4|      •     Identifiers for devices
~~~~

KB 现文: `knowledge_base/chapters/ch10_appendices.md:66` (来源: triage kb_loc knowledge_base/chapters/ch10_appendices.md:66 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  64| | Michael Schmitz | Bayer AG |
  65| | Dave Scocca | Rho, Inc. |
  66| | Maria Sekac | PRA Health Sciences |
  67| | Kalai Selvanathan | Boehringer Ingelheim |
  68| | Mihaela Simion | Biogen |
~~~~

### 150. `ig34_p0196_a006` — supp:RULE_C7-K4-rereview

- PDF 页 196 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **REAL_GAP** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `C7-K4-rereview` · 批 `T3-C7`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| --LOBXFL | Last Observation Before Exposure Flag | Char | * | Record Qualifier | Operationally defined indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. | Perm |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0196.txt` 第 13-20 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12|               Examination                                                  Qualifier
 13| --LOBXFL      Last Observation Before        Char   *                      Record           Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value           Perm
 14|               Exposure Flag                                                Qualifier        should be "Y" or null.
 15| --LLOQ        Lower Limit of Quantitation    Num                           Variable         Indicates the lower limit of quantitation for an assay. Units will be those used for --STRESU.                     Perm
 16|                                                                            Qualifier
 17| --ULOQ        Upper Limit of Quantitation    Num                           Variable         Indicates the upper limit of quantitation for an assay. Units will be those used for --STRESU.                     Perm
 18|                                                                            Qualifier
 19| VISITNUM      Visit Number                   Num                           Timing           Clinical encounter number. Numeric version of VISIT, used for sorting.                                             Perm
 20| VISIT         Visit Name                     Char                          Timing           Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY.            Perm
 21| VISITDY       Planned Study Day of Visit     Num                           Timing           Planned study day of the visit based upon RFSTDTC in Demographics.                                                 Perm
~~~~

KB 现文: `knowledge_base/domains/LB/assumptions.md:43-47` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  43| | --LOBXFL | Last Observation Before Exposure Flag | Char | * | Record Qualifier | Operationally derived indicator used to identify the last non-missing value prior to RFXSTDTC. The value should be "Y" or null. | Perm |
  44| | --LLOQ | Lower Limit of Quantitation | Num | | Variable Qualifier | Indicates the lower limit of quantitation for an assay. Units will be those used for --STRESU. | Perm |
  45| | --ULOQ | Upper Limit of Quantitation | Num | | Variable Qualifier | Indicates the upper limit of quantitation for an assay. Units will be those used for --STRESU. | Perm |
  46| | VISITNUM | Visit Number | Num | | Timing | Clinical encounter number. Numeric version of VISIT, used for sorting. | Perm |
  47| | VISIT | Visit Name | Char | | Timing | Protocol-defined description of clinical encounter. May be used in addition to VISITNUM and/or VISITDY. | Perm |
~~~~

### 151. `ig34_p0247_a021` — supp:RULE_C7-K4-rereview

- PDF 页 247 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.6 Laboratory Test Results (LB)`
- triage 类 **VALUE_DIFF** · 终态 **ATOM_ERR** (T3 前 PARTIAL) · 判定规则 `C7-K4-rereview` · 批 `T3-C7`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 1 | ABC | LB | ABC-001-001 | 1 | HCG | Choriogonadotropin Beta | CHEMISTRY | - | | Ord | PtFtv | | | NEGATIVE | | | | | | | | 2106-3 | URINE | Y | 1 | BASELINE | 1999-05-15T04:00 | Y |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0247.txt` 第 71-72 行 (自动定位, 词覆盖 0.85; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 70| Row     STUDYID           DOMAIN           USUBJID          LBSEQ        LBTESTCD                    LBTEST                            LBCAT                  LBORRES        LBORRESU          LBRESSCL             LBRESTYP            LBORNRLO                     LBORNRHI           LBSTRESC         LBSTRESN           LBSTRESU          LBSTNRLO             LBSTRNHI          LBNRIND         LBSTAT        LBREASND                          LBLOINC         LBSPEC          LBLOBXFL        VISITNUM          VISIT             LBDTC                  LBPTFL
 71| 1       ABC               LB               ABC-001-         1            HCG                         Choriogonadotropin                CHEMISTRY              -                                Ord                  PrThr                                                               NEGATIVE                                                                                                                                                     2106-3          URINE           Y               1                 BASELINE          1999-06-               Y
 72|                                            001                                                       Beta                                                                                                                                                                                                                                                                                                                                                                                                                                19T04:00
 73| 2       ABC               LB               ABC-001-         1            HCG                         Choriogonadotropin                CHEMISTRY                                               Ord                  PrThr                                                                                                                                                                            NOT           NOT APPLICABLE                    2106-3          URINE                           1                 BASELINE          1999-06-               Y
~~~~

KB 现文: `knowledge_base/domains/LB/examples.md:37-41` (来源: near triage kb_loc knowledge_base/domains/LB/examples.md:50 (score 0.55)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  37| | 14 | ABC | LB | ABC-001-001 | 14 | | PH | pH | | URINALYSIS | | 7.5 | | QUANTITATIVE | LOG SUBSTANCE CONCENTRATION | | 5.0 | 9.0 | | 7.5 | | | 5.00 | 9.00 | | | | | 5803-2 | URINE | TEST STRIP | | Y | Y | | | 1 | Week 1 | 1999-06-19 | Y | |
  38| | 15 | ABC | LB | ABC-001-001 | 15 | | ALB | Albumin | | CHEMISTRY | | | | QUANTITATIVE | MASS CONCENTRATION | | | | | | | | | | | | NOT DONE | INSUFFICIENT SAMPLE | 2862-1 | SERUM | ELECTROPHORESIS | | | | | | 2 | Week 2 | 1999-07-21 | Y | |
  39| | 16 | ABC | LB | ABC-001-001 | 16 | | CHOL | Cholesterol | | CHEMISTRY | | 229 | mg/dL | QUANTITATIVE | MASS CONCENTRATION | | 0 | <200 | | 229 | 229 | mg/dL | 0 | 199 | | | | | 2093-3 | SERUM | | | | | | | 2 | Week 2 | 1999-07-21 | Y | |
  40| | 17 | ABC | LB | ABC-001-001 | 17 | | WBC | Leukocytes | | HEMATOLOGY | | 5.9 | 10^9/L | QUANTITATIVE | NUMBER CONCENTRATION | | 4 | 11 | | 5.9 | 5.9 | 10^9/L | 4 | 11 | | | | | 6690-2 | BLOOD | AUTOMATED COUNT | | | Y | | | 2 | Week 2 | 1999-07-21 | Y | |
  41| | 18 | ABC | LB | ABC-001-001 | 18 | | PROT | Protein | | URINALYSIS | | MODERATE | | ORDINAL | PRESENCE OR THRESHOLD | | | | | MODERATE | | | | | NEGATIVE to TRACE | ABNORMAL | | | 20454-5 | URINE | TEST STRIP | | | | | N | 2 | Week 2 | 1999-07-21 | Y | |
~~~~

### 152. `ig34_p0195_a004` — supp:RULE_T2-fix+deltaRereviewPASS+auditPASS

- PDF 页 195 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **REAL_GAP** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T2-fix+deltaRereviewPASS+auditPASS` · 批 `B-LB`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
o Individual domains include additional variables with specific Controlled Terminology codelists and domain-specific Core values.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0195.txt` 第 8-8 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  7|            laboratory findings domains to uniquely describe a measurement, test, or examination of a biological specimen.
  8|            o     Individual domains include additional variables with specific Controlled Terminology codelists and domain-specific Core values.
  9|            o     The Findings general observation class includes additional permissible variables that may be added when representing specimen-based laboratory
~~~~

KB 现文: `knowledge_base/domains/LB/assumptions.md:14-14` (来源: fuzzy locate (score 0.933)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  14|   - Individual domains include additional variables with specific Controlled Terminology codelists and domain-specific Core values.
~~~~

### 153. `ig34_p0195_a005` — supp:RULE_T2-fix+deltaRereviewPASS+auditPASS

- PDF 页 195 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **REAL_GAP** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T2-fix+deltaRereviewPASS+auditPASS` · 批 `B-LB`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
o The Findings general observation class includes additional permissible variables that may be added when representing specimen-based laboratory findings.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0195.txt` 第 9-9 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  8|            o     Individual domains include additional variables with specific Controlled Terminology codelists and domain-specific Core values.
  9|            o     The Findings general observation class includes additional permissible variables that may be added when representing specimen-based laboratory
 10|                  findings.
~~~~

KB 现文: `knowledge_base/domains/LB/assumptions.md:15-15` (来源: fuzzy locate (score 0.947)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  15|   - The Findings general observation class includes additional permissible variables that may be added when representing specimen-based laboratory findings.
~~~~

### 154. `ig34_p0195_a006` — supp:RULE_T2-fix+deltaRereviewPASS+auditPASS

- PDF 页 195 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification`
- triage 类 **REAL_GAP** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T2-fix+deltaRereviewPASS+auditPASS` · 批 `B-LB`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
o Permissible identifier and timing variables may be added to represent details (e.g., identifiers to describe related records, planned time points, actual timing).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0195.txt` 第 11-11 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 10|                  findings.
 11|            o     Permissible identifier and timing variables may be added to represent details (e.g., identifiers to describe related records, planned time points, actual
 12|                  timing).
~~~~

KB 现文: `knowledge_base/domains/LB/assumptions.md:16-16` (来源: fuzzy locate (score 0.955)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  16|   - Permissible identifier and timing variables may be added to represent details (e.g., identifiers to describe related records, planned time points, actual timing).
~~~~

### 155. `ig34_p0211_a009` — supp:RULE_T2-fix+deltaRereviewPASS+auditPASS

- PDF 页 211 · 原子类型 SENTENCE · 所在节 `§6.3.5.3 Cell Phenotype Findings (CP)`
- triage 类 **REAL_GAP** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T2-fix+deltaRereviewPASS+auditPASS` · 批 `B-CP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Because the ratio in row 11 is based on counts of both the viable (row 9) and the non-viable (row 10) lymphocyte subpopulations, it is not appropriate to use the CPCELSTA variable. Instead, the viability information is pre-coordinated into the value in CPTEST. Additionally, because the cell state (i.e., "VIABLE" or "NON-VIABLE") is pre-coordinated into the Test Name in row 11, the suffix "Sub" is no longer needed in CPTEST (i.e., the Test Name is "Lymphocytes Viable/Lymphocytes NonViable" rather than "Lymphocytes Sub Viable/Lymphocytes Sub NonViable". CPGRPID is used to group the related records for the ratio (row 11) with those used to calculate it (rows 9 and 10).
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0211.txt` 第 26-29 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 25|            ratio of viable to nonviable lymphocytes in row 11 is calculated using data from rows 9 and 10.
 26|                  Because the ratio in row 11 is based on counts of both the viable (row 9) and the non-viable (row 10) lymphocyte subpopulations, it is not appropriate to use the CPCELSTA variable. Instead, the
 27|                  viability information is pre-coordinated into the value in CPTEST. Additionally, because the cell state (i.e., "VIABLE" or "NON-VIABLE") is pre-coordinated into the Test Name in row 11, the suffix
 28|                  "Sub" is no longer needed in CPTEST (i.e., the Test Name is "Lymphocytes Viable/Lymphocytes NonViable" rather than "Lymphocytes Sub Viable/Lymphocytes Sub NonViable". CPGRPID is used to
 29|                  group the related records for the ratio (row 11) with those used to calculate it (rows 9 and 10).
 30| cp.xpt
~~~~

KB 现文: `knowledge_base/domains/CP/examples.md:81-81` (来源: fuzzy locate (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  81| Because the ratio in row 11 is based on counts of both the viable (row 9) and the non-viable (row 10) lymphocyte subpopulations, it is not appropriate to use the CPCELSTA variable. Instead, the viability information is pre-coordinated into the value in CPTEST. Additionally, because the cell state (i.e., "VIABLE" or "NON-VIABLE") is pre-coordinated into the Test Name in row 11, the suffix "Sub" is no longer needed in CPTEST (i.e., the Test Name is "Lymphocytes Viable/Lymphocytes NonViable" rather than "Lymphocytes Sub Viable/Lymphocytes Sub NonViable"). CPGRPID is used to group the related records for the ratio (row 11) with those used to calculate it (rows 9 and 10).
~~~~

### 156. `ig34_p0277_a003` — supp:RULE_T2-fix+deltaRereviewPASS+auditPASS

- PDF 页 277 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records`
- triage 类 **VALUE_DIFF** · 终态 **EQUIVALENT** (T3 前 MISPLACED) · 判定规则 `T2-fix+deltaRereviewPASS+auditPASS` · 批 `B-PCPP`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row | STUDYID | DOMAIN | USUBJID | PPSEQ | PPGRPID (Example 1) | PPGRPID (Example 2) | PPGRPID (Example 3) | PPGRPID (Example 4) | PPTESTCD | PPTEST | PPCAT | PPORRES | PPORRESU | PPSTRESC | PPSTRESN | PPSTRESU | PPSPEC | PPNOMDY | PPRFTDTC
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0277.txt` 第 3-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  2| pp.xpt
  3| Row   STUDYID   DOMAIN   USUBJID        PPSEQ   PPGRPID (Example 1)   PPGRPID (Example 2)   PPGRPID (Example 3)   PPGRPID (Example 4)   PPTESTCD   PPTEST               PPCAT    PPORRES   PPORRESU   PPSTRESC   PPSTRESN   PPSTRESU   PPSPEC   PPNOMDY   PPRFTDTC
  4| 1     ABC-123   PP       ABC-123-0001   1       DY1DRGX               DY1DRGX               DY1DRGX_A             TMAX                  TMAX       Time of CMAX         DRUG X   1.87      h          1.87       1.87       h          PLASMA   1         2001-02-01T08:35
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:112` (来源: triage kb_loc knowledge_base/domains/PP/examples.md:112 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 110| *See PC examples for the full description of RELREC Methods A through D and their corresponding relrec.xpt tables.*
 111| 
 112| > See [PC/examples.md](../PC/examples.md#63593-relating-pp-records-to-pc-records--worked-examples) for the RELREC Methods A-D worked examples (SDTMIG v3.4 §6.3.5.9.3).
~~~~

### 157. `ig34_p0048_a012` — supp:RULE_T1-two-agent

- PDF 页 48 · 原子类型 TABLE_ROW · 所在节 `§4.4.10 [Representing Time Points]`
- triage 类 **PRESENT** · 终态 **EQUIVALENT** (T3 前 None) · 判定规则 `T1-two-agent` · 批 `T1:pack_028`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
PERIOD 1, DAY 5 | 4 | PRE-DOSE | 1 | PM DOSE
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0048.txt` 第 6-9 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5|                          4H                3
  6|                          PRE-DOSE          1          PM DOSE
  7|                          1H                2
  8|                          4H                3
  9| PERIOD 1, DAY 5 4        PRE-DOSE          1          AM DOSE
 10|                          1H                2
~~~~

KB 现文: `knowledge_base/chapters/ch04_general_assumptions.md:1086` (来源: triage kb_loc knowledge_base/chapters/ch04_general_assumptions.md:1086 (T1 行号, 未定位, 显示 ±2 行)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
1084| | --RFTDTC | Date/Time of Reference Time Point |
1085| 
1086| ```mermaid
1087| graph LR
1088|     REF["Reference Time Point (Usually a Dose) --TPTREF (Description) --RFTDTC (Date/Time)"]
~~~~

### 158. `ig34_p0064_a001` — supp:RULE_T1-two-agent

- PDF 页 64 · 原子类型 TABLE_ROW · 所在节 `§5.2 [Demographics (DM)]`
- triage 类 **PRESENT** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent` · 批 `T1:pack_004`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
(ARMCD continued) | ARMCD values would be 20. If the subject was not assigned to a trial arm, ARMCD is null and ARMNRS is populated. With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial Arms dataset.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0064.txt` 第 4-7 行 (自动定位, 词覆盖 0.971; 版式以原 PDF 为准):

~~~~
  3|                                         Format1
  4|                                                                            ARMCD values would be 20. If the subject was not assigned to a trial arm, ARMCD is null and ARMNRS is
  5|                                                                            populated.
  6|                                                                            With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial
  7|                                                                            Arms dataset.
  8| ARM            Description of      Char *                     Synonym      Name of the arm to which the subject was assigned. If the subject was not assigned to an arm, ARM is null         Exp
~~~~

KB 现文: `knowledge_base/domains/DM/spec.md:219-219` (来源: near triage kb_loc knowledge_base/domains/DM/spec.md:219 (score 0.971)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 219| - **CDISC Notes:** ARMCD is limited to 20 characters. It is not subject to the character restrictions that apply to TESTCD. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20. If the subject was not assigned to a trial arm, ARMCD is null and ARMNRS is populated.  With the exception of studies which use multistage arm assignments, must be a value of ARMCD in the Trial Arms dataset.
~~~~

### 159. `ig34_p0115_a030` — supp:RULE_T1-two-agent

- PDF 页 115 · 原子类型 TABLE_HEADER · 所在节 `§6.1.3.3 [Exposure/Exposure as Collected Examples]`
- triage 类 **REWRITE_OK** · 终态 **EQUIVALENT** (T3 前 PARTIAL) · 判定规则 `T1-two-agent` · 批 `T1:pack_013`

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Period 1: Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time | Period 2: Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0115.txt` 第 34-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 33| Subject 56789001
 34| Period 1                                                              Period 2
 35| Day Bottle 1         Bottle 2       Start Date/Time   End Date/Time   Day Bottle 1         Bottle 2       Start Date/Time     End Date/Time
 36|      # of capsules   # of tablets                                          # of capsules   # of tablets
 37| 1    1               1              2002-07-01T07:30 2002-07-01T07:30 1    1               1              2002-07-09T07:30 2002-07-09T07:30
~~~~

KB 现文: `knowledge_base/domains/EX/examples.md:245-247` (来源: near triage kb_loc knowledge_base/domains/EX/examples.md:243 (score 1.0)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
 245| | Period 1 | | | | | Period 2 | | | | |
 246| |---|---|---|---|---|---|---|---|---|---|
 247| | Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time | Day | Bottle 1 # of capsules | Bottle 2 # of tablets | Start Date/Time | End Date/Time |
~~~~

