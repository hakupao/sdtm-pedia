# 23_td_arms_ta_tv

> **NotebookLM Source Metadata** (由 merge_sources.py 生成, 供 NotebookLM 索引 + citation 反查)
>
> - **Bucket ID**: `23`
> - **Concept**: Trial Design: TA + TV (arms + visits)
> - **Merged files**: 6
> - **Words**: 9,078
> - **Chars**: 50,393
> - **Sources**:
>   - `domains/TA/spec.md`
>   - `domains/TA/assumptions.md`
>   - `domains/TA/examples.md`
>   - `domains/TV/spec.md`
>   - `domains/TV/assumptions.md`
>   - `domains/TV/examples.md`

---
## Source: `domains/TA/spec.md`

# TA — Trial Arms

> Class: Trial Design | Structure: One record per planned Element per Arm

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### ARMCD
- **Order:** 3
- **Label:** Planned Arm Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than that for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20.

### ARM
- **Order:** 4
- **Label:** Description of Planned Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Name given to an arm or treatment group.

### TAETORD
- **Order:** 5
- **Label:** Planned Order of Element within Arm
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** Number that gives the order of the element within the arm.

### ETCD
- **Order:** 6
- **Label:** Element Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Req
- **CDISC Notes:** ETCD (the companion to ELEMENT) is limited to 8 characters and does not have special character restrictions. These values should be short for ease of use in programming, but it is not expected that ETCD will need to serve as a variable name.

### ELEMENT
- **Order:** 7
- **Label:** Description of Element
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** The name of the element. The same element may occur more than once within an arm.

### TABRANCH
- **Order:** 8
- **Label:** Branch
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Exp
- **CDISC Notes:** Condition subject met, at a "branch" in the trial design at the end of this element, to be included in this arm (e.g., "Randomization to DRUG X").

### TATRANS
- **Order:** 9
- **Label:** Transition Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Exp
- **CDISC Notes:** If the trial design allows a subject to transition to an element other than the next element in sequence, then the conditions for transitioning to those other elements, and the alternative element sequences, are specified in this rule (e.g., "Responders go to washout").

### EPOCH
- **Order:** 10
- **Label:** Epoch
- **Type:** Char
- **Controlled Terms:** C99079
- **Role:** Timing
- **Core:** Req
- **CDISC Notes:** Name of the trial epoch with which this element of the arm is associated.
---

## Cross References

### Controlled Terminology
- [Epoch (C99079)](../../terminology/core/general_part2.md) — EPOCH

### Related Domains
- **Same class (Trial Design):** TD, TE, TI, TM, TS, TV
- **Trial Design:** [TE](../TE/) — arms use elements
- **Trial Design:** [TV](../TV/) — arms define visit schedules

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

## Source: `domains/TA/assumptions.md`

# TA — Assumptions

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

## Source: `domains/TA/examples.md`

# TA — Examples

The core of the Trial Design Model is the TA dataset. For each arm of the trial, the TA dataset contains 1 record for each occurrence of an element in the path of the arm.

Although the TA dataset has 1 record for each trial element traversed by subjects assigned to an arm, it is generally more useful to work out the overall design of the trial at the study cell level first, then to work out the elements within each study cell, and finally to develop the definitions of the elements that are contained in the Trial Elements (TE) table.

This section uses example trials of increasing complexity to illustrate the concepts of trial design. For each example trial, the process of working out the TA table is illustrated by means of a series of diagrams and tables, including:

- A diagram showing the branching structure of the trial in a "study schema" format
- A diagram that shows the "prospective" view of the trial (i.e., the view of those participating in the trial), with epochs and elements
- A diagram that shows the "retrospective" view of the trial (i.e., the view of the analyst reporting on the trial), arm-centered showing elements within each study cell
- If the trial is blinded, a diagram showing the trial as it appears to a blinded participant
- A trial design matrix, an alternative format showing arms and epochs with study cells
- The TA dataset

Example 1 should be reviewed before reading other examples, as it explains the conventions used for all diagrams and tables in the examples.

## Example 1

A simple parallel trial with 3 arms (Placebo, Drug A, Drug B), 3 epochs (Screening, Run-In, Treatment). Each study cell contains exactly 1 element. Randomization occurs at the end of the Run-In element.

**Study Schema**

```mermaid
graph LR
    S[Screen] --> RI[Run-In]
    RI -->|"Randomized to Placebo"| P[Placebo]
    RI -->|"Randomized to Drug A"| A[Drug A]
    RI -->|"Randomized to Drug B"| B[Drug B]
    style S fill:#fef3cd,stroke:#333
    style RI fill:#d4edda,stroke:#333
    style P fill:#cce5ff,stroke:#333
    style A fill:#cce5ff,stroke:#333
    style B fill:#f8d7da,stroke:#333
```

**Prospective View**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        S[Screen]
    end
    subgraph RE["Run-In Epoch"]
        RI[Run-In]
    end
    subgraph TE["Treatment Epoch"]
        P[Placebo]
        A[Drug A]
        B[Drug B]
    end
    S --> RI
    RI --> P
    RI --> A
    RI --> B
```

**Retrospective View**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        SP[Screen]
        SA[Screen]
        SB[Screen]
    end
    subgraph RE["Run-In Epoch"]
        RIP[Run-In]
        RIA[Run-In]
        RIB[Run-In]
    end
    subgraph TE["Treatment Epoch"]
        P[Placebo]
        A[Drug A]
        B[Drug B]
    end
    SP --> RIP --> P
    SA --> RIA --> A
    SB --> RIB --> B
```

**Blinded View**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        S[Screen]
    end
    subgraph RE["Run-In Epoch"]
        RI[Run-In]
    end
    subgraph TE["Treatment Epoch"]
        SD[Study Drug]
    end
    S --> RI --> SD
```

**Trial Design Matrix**

|  | Screen | Run-in | Treatment |
|---|---|---|---|
| **Placebo** | Screen | Run-in | PLACEBO |
| **A** | Screen | Run-in | DRUG A |
| **B** | Screen | Run-in | DRUG B |

**ta.xpt**

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
|-----|---------|--------|-------|-----|---------|------|---------|----------|---------|-------|
| 1 | EX1 | TA | P | Placebo | 1 | SCRN | Screen | | | SCREENING |
| 2 | EX1 | TA | P | Placebo | 2 | RI | Run-In | Randomized to Placebo | | RUN-IN |
| 3 | EX1 | TA | P | Placebo | 3 | P | Placebo | | | TREATMENT |
| 4 | EX1 | TA | A | A | 1 | SCRN | Screen | | | SCREENING |
| 5 | EX1 | TA | A | A | 2 | RI | Run-In | Randomized to Drug A | | RUN-IN |
| 6 | EX1 | TA | A | A | 3 | A | Drug A | | | TREATMENT |
| 7 | EX1 | TA | B | B | 1 | SCRN | Screen | | | SCREENING |
| 8 | EX1 | TA | B | B | 2 | RI | Run-In | Randomized to Drug B | | RUN-IN |
| 9 | EX1 | TA | B | B | 3 | B | Drug B | | | TREATMENT |

## Example 2

A crossover trial comparing 3 treatments (Placebo, 5 mg, 10 mg) with 7 epochs: Screening, 3 Treatment Epochs with 3 Rest (washout) Epochs between them, and a Follow-up Epoch. Each arm represents a different order of treatments.

**Study Schema**

```mermaid
graph LR
    S[Screen]
    S -->|"P-5-10"| a1[Placebo] --> a2[Rest] --> a3[5 mg] --> a4[Rest] --> a5[10 mg] --> a6[Follow]
    S -->|"5-P-10"| b1[5 mg] --> b2[Rest] --> b3[Placebo] --> b4[Rest] --> b5[10 mg] --> b6[Follow]
    S -->|"5-10-P"| c1[5 mg] --> c2[Rest] --> c3[10 mg] --> c4[Rest] --> c5[Placebo] --> c6[Follow]
    style S fill:#fef3cd,stroke:#333
```

**Prospective View**

```mermaid
graph LR
    subgraph SE["Screening"]
        s1[Screen]
        s2[Screen]
        s3[Screen]
    end
    subgraph T1["1st Treatment"]
        t1a[Placebo]
        t1b[5 mg]
        t1c[5 mg]
    end
    subgraph W1["1st Washout"]
        w1a[Rest]
        w1b[Rest]
        w1c[Rest]
    end
    subgraph T2["2nd Treatment"]
        t2a[5 mg]
        t2b[Placebo]
        t2c[10 mg]
    end
    subgraph W2["2nd Washout"]
        w2a[Rest]
        w2b[Rest]
        w2c[Rest]
    end
    subgraph T3["3rd Treatment"]
        t3a[10 mg]
        t3b[10 mg]
        t3c[Placebo]
    end
    subgraph FU["Follow-up"]
        f1[Follow]
        f2[Follow]
        f3[Follow]
    end
    s1 --> t1a --> w1a --> t2a --> w2a --> t3a --> f1
    s2 --> t1b --> w1b --> t2b --> w2b --> t3b --> f2
    s3 --> t1c --> w1c --> t2c --> w2c --> t3c --> f3
```

**Retrospective View**

Same structure as the Prospective View (one-to-one relationship between epochs and elements in each arm for this crossover design). Arm labels: P-L-H, L-P-H, L-H-P.

**Blinded View**

```mermaid
graph LR
    subgraph SE["Screening"]
        S[Screen]
    end
    subgraph T1["1st Treatment"]
        D1[Drug]
    end
    subgraph W1["1st Rest"]
        R1[Rest]
    end
    subgraph T2["2nd Treatment"]
        D2[Drug]
    end
    subgraph W2["2nd Rest"]
        R2[Rest]
    end
    subgraph T3["3rd Treatment"]
        D3[Drug]
    end
    subgraph FU["Follow-up"]
        F[Follow]
    end
    S --> D1 --> R1 --> D2 --> R2 --> D3 --> F
```

**Trial Design Matrix**

|  | Screen | First Treatment | First Rest | Second Treatment | Second Rest | Third Treatment | Follow-up |
|---|---|---|---|---|---|---|---|
| **P-5-10** | Screen | Placebo | Rest | 5 mg | Rest | 10 mg | Follow-up |
| **5-P-10** | Screen | 5 mg | Rest | Placebo | Rest | 10 mg | Follow-up |
| **5-10-P** | Screen | 5 mg | Rest | 10 mg | Rest | Placebo | Follow-up |

**ta.xpt**

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
|-----|---------|--------|-------|-----|---------|------|---------|----------|---------|-------|
| 1 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 1 | SCRN | Screen | Randomized to Placebo - 5 mg - 10 mg | | SCREENING |
| 2 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 2 | P | Placebo | | | TREATMENT 1 |
| 3 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 3 | REST | Rest | | | WASHOUT 1 |
| 4 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 4 | 5 | 5 mg | | | TREATMENT 2 |
| 5 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 5 | REST | Rest | | | WASHOUT 2 |
| 6 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 6 | 10 | 10 mg | | | TREATMENT 3 |
| 7 | EX2 | TA | P-5-10 | Placebo-5mg-10mg | 7 | FU | Follow-up | | | FOLLOW-UP |
| 8 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 1 | SCRN | Screen | Randomized to 5 mg - Placebo - 10 mg | | SCREENING |
| 9 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 2 | 5 | 5 mg | | | TREATMENT 1 |
| 10 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 3 | REST | Rest | | | WASHOUT 1 |
| 11 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 4 | P | Placebo | | | TREATMENT 2 |
| 12 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 5 | REST | Rest | | | WASHOUT 2 |
| 13 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 6 | 10 | 10 mg | | | TREATMENT 3 |
| 14 | EX2 | TA | 5-P-10 | 5mg-Placebo-10mg | 7 | FU | Follow-up | | | FOLLOW-UP |
| 15 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 1 | SCRN | Screen | Randomized to 5 mg - 10 mg - Placebo | | SCREENING |
| 16 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 2 | 5 | 5 mg | | | TREATMENT 1 |
| 17 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 3 | REST | Rest | | | WASHOUT 1 |
| 18 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 4 | 10 | 10 mg | | | TREATMENT 2 |
| 19 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 5 | REST | Rest | | | WASHOUT 2 |
| 20 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 6 | P | Placebo | | | TREATMENT 3 |
| 21 | EX2 | TA | 5-10-P | 5mg-10mg-Placebo | 7 | FU | Follow-up | | | FOLLOW-UP |

## Example 3

A trial with multiple branches: randomization at screening plus response evaluation after blinded treatment. This results in 4 arms (A-Open A, A-Rescue, B-Open A, B-Rescue). TABRANCH is populated for 2 records in each arm reflecting the 2 branch points.

**Study Schema**

```mermaid
graph LR
    S[Screen]
    S -->|"Randomized to A"| DA[Drug A]
    S -->|"Randomized to B"| DB[Drug B]
    DA -->|"Response: Open A"| OA1[Open A]
    DA -->|"Response: Rescue"| R1[Rescue]
    DB -->|"Response: Open A"| OA2[Open A]
    DB -->|"Response: Rescue"| R2[Rescue]
    style S fill:#fef3cd,stroke:#333
    style DA fill:#cce5ff,stroke:#333
    style DB fill:#d4edda,stroke:#333
    style R1 fill:#f8d7da,stroke:#333
    style R2 fill:#f8d7da,stroke:#333
```

**Prospective View**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        s1[Screen]
        s2[Screen]
        s3[Screen]
        s4[Screen]
    end
    subgraph DB["Double Blind Treatment Epoch"]
        da1[Drug A]
        da2[Drug A]
        db1[Drug B]
        db2[Drug B]
    end
    subgraph OL["Open Treatment Epoch"]
        oa1[Open A]
        r1[Rescue]
        oa2[Open A]
        r2[Rescue]
    end
    s1 --> da1 --> oa1
    s2 --> da2 --> r1
    s3 --> db1 --> oa2
    s4 --> db2 --> r2
```

**Retrospective View**

Same epoch structure as Prospective View. 4 arms: A-Open (Screen→Drug A→Open A), A-Rescue (Screen→Drug A→Rescue), B-Open (Screen→Drug B→Open A), B-Rescue (Screen→Drug B→Rescue).

**Blinded View**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        S[Screen]
    end
    subgraph DB["Double Blind Treatment Epoch"]
        D[Drug]
    end
    subgraph OL["Open Treatment Epoch"]
        OA[Open A]
        R[Rescue]
    end
    S --> D
    D --> OA
    D --> R
```

**Trial Design Matrix**

|  | Screen | Double Blind | Open Label |
|---|---|---|---|
| **A-Open A** | Screen | Treatment A | Open Drug A |
| **A-Rescue** | Screen | Treatment A | Rescue |
| **B-Open A** | Screen | Treatment B | Open Drug A |
| **B-Rescue** | Screen | Treatment B | Rescue |

**ta.xpt**

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
|-----|---------|--------|-------|-----|---------|------|---------|----------|---------|-------|
| 1 | EX3 | TA | AA | A-Open A | 1 | SCRN | Screen | Randomized to Treatment A | | SCREENING |
| 2 | EX3 | TA | AA | A-Open A | 2 | DBA | Treatment A | Assigned to Open Drug A on basis of response evaluation | | BLINDED TREATMENT |
| 3 | EX3 | TA | AA | A-Open A | 3 | OA | Open Drug A | | | OPEN LABEL TREATMENT |
| 4 | EX3 | TA | AR | A-Rescue | 1 | SCRN | Screen | Randomized to Treatment A | | SCREENING |
| 5 | EX3 | TA | AR | A-Rescue | 2 | DBA | Treatment A | Assigned to Rescue on basis of response evaluation | | BLINDED TREATMENT |
| 6 | EX3 | TA | AR | A-Rescue | 3 | RSC | Rescue | | | OPEN LABEL TREATMENT |
| 7 | EX3 | TA | BA | B-Open A | 1 | SCRN | Screen | Randomized to Treatment B | | SCREENING |
| 8 | EX3 | TA | BA | B-Open A | 2 | DBB | Treatment B | Assigned to Open Drug A on basis of response evaluation | | BLINDED TREATMENT |
| 9 | EX3 | TA | BA | B-Open A | 3 | OA | Open Drug A | | | OPEN LABEL TREATMENT |
| 10 | EX3 | TA | BR | B-Rescue | 1 | SCRN | Screen | Randomized to Treatment B | | SCREENING |
| 11 | EX3 | TA | BR | B-Rescue | 2 | DBB | Treatment B | Assigned to Rescue on basis of response evaluation | | BLINDED TREATMENT |
| 12 | EX3 | TA | BR | B-Rescue | 3 | RSC | Rescue | | | OPEN LABEL TREATMENT |

## Example 4

A cyclical chemotherapy oncology trial with repeating treatment/rest elements until disease progression. 2 arms (Drug A, Drug B), 3 epochs (Screening, Treatment, Follow-Up). The TATRANS variable represents the "repeat until disease progression" skip-forward rule.

Maximum of 4 cycles assumed in this example.

**Study Schema**

```mermaid
graph LR
    S[Screen]
    S -->|"Randomized to A"| DA[Drug A] --> RA[Rest] --> FA[Follow]
    S -->|"Randomized to B"| DB[Drug B] --> RB[Rest] --> FB[Follow]
    RA -.->|"Repeat until<br/>disease progression"| DA
    RB -.->|"Repeat until<br/>disease progression"| DB
    style S fill:#fef3cd,stroke:#333
```

**Prospective View**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        s1[Screen]
        s2[Screen]
    end
    subgraph TE["Treatment Epoch"]
        da["Drug A | Rest<br/>Repeat until disease progression"]
        db["Drug B | Rest<br/>Repeat until disease progression"]
    end
    subgraph FU["Follow-up Epoch"]
        f1[Follow]
        f2[Follow]
    end
    s1 --> da --> f1
    s2 --> db --> f2
```

**Retrospective View**

Same epoch structure as the Prospective View: 2 arms (Drug A, Drug B), each cycling through Treatment Epoch until disease progression, then entering Follow-up.

**Retrospective View with Explicit Repeats**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        s1[Screen]
        s2[Screen]
    end
    subgraph TE["Treatment Epoch"]
        a1[A] --> r1[Rest] --> a2[A] --> r2[Rest] --> a3[A] --> r3[Rest] --> a4[A] --> r4[Rest]
        b1[B] --> r5[Rest] --> b2[B] --> r6[Rest] --> b3[B] --> r7[Rest] --> b4[B] --> r8[Rest]
    end
    subgraph FU["Follow-up Epoch"]
        f1[Follow]
        f2[Follow]
    end
    s1 --> a1
    r4 --> f1
    s2 --> b1
    r8 --> f2
    r1 -.->|"If disease progression"| f1
    r2 -.->|"If disease progression"| f1
    r3 -.->|"If disease progression"| f1
    r5 -.->|"If disease progression"| f2
    r6 -.->|"If disease progression"| f2
    r7 -.->|"If disease progression"| f2
```

**Blinded View**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        S[Screen]
    end
    subgraph TE["Treatment Epoch"]
        rx1[Rx] --> re1[Rest] --> rx2[Rx] --> re2[Rest] --> rx3[Rx] --> re3[Rest] --> rx4[Rx] --> re4[Rest]
    end
    subgraph FU["Follow-up Epoch"]
        F[Follow]
    end
    S --> rx1
    re4 --> F
    re1 -.->|"If disease progression"| F
    re2 -.->|"If disease progression"| F
    re3 -.->|"If disease progression"| F
```

**Trial Design Matrix**

|  | Screen | Treatment | | | | | | | | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|
| **A** | Screen | Trt A | Rest | Trt A | Rest | Trt A | Rest | Trt A | Rest | Follow-up |
| **B** | Screen | Trt B | Rest | Trt B | Rest | Trt B | Rest | Trt B | Rest | Follow-up |

**ta.xpt**

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
|-----|---------|--------|-------|-----|---------|------|---------|----------|---------|-------|
| 1 | EX4 | TA | A | A | 1 | SCRN | Screen | Randomized to A | | SCREENING |
| 2 | EX4 | TA | A | A | 2 | A | Trt A | | | TREATMENT |
| 3 | EX4 | TA | A | A | 3 | REST | Rest | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 4 | EX4 | TA | A | A | 4 | A | Trt A | | | TREATMENT |
| 5 | EX4 | TA | A | A | 5 | REST | Rest | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 6 | EX4 | TA | A | A | 6 | A | Trt A | | | TREATMENT |
| 7 | EX4 | TA | A | A | 7 | REST | Rest | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 8 | EX4 | TA | A | A | 8 | A | Trt A | | | TREATMENT |
| 9 | EX4 | TA | A | A | 9 | REST | Rest | | | TREATMENT |
| 10 | EX4 | TA | A | A | 10 | FU | Follow-up | | | FOLLOW-UP |
| 11 | EX4 | TA | B | B | 1 | SCRN | Screen | Randomized to B | | SCREENING |
| 12 | EX4 | TA | B | B | 2 | B | Trt B | | | TREATMENT |
| 13 | EX4 | TA | B | B | 3 | REST | Rest | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 14 | EX4 | TA | B | B | 4 | B | Trt B | | | TREATMENT |
| 15 | EX4 | TA | B | B | 5 | REST | Rest | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 16 | EX4 | TA | B | B | 6 | B | Trt B | | | TREATMENT |
| 17 | EX4 | TA | B | B | 7 | REST | Rest | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 18 | EX4 | TA | B | B | 8 | B | Trt B | | | TREATMENT |
| 19 | EX4 | TA | B | B | 9 | REST | Rest | | | TREATMENT |
| 20 | EX4 | TA | B | B | 10 | FU | Follow-up | | | FOLLOW-UP |

## Example 5

Similar to Example 4, but treatment A has longer duration than treatment B, so the trial cannot be blinded. Maximum of 3 cycles assumed. Different rest elements (RESTA, RESTB) are used for the 2 arms since cycle lengths differ.

**Study Schema**

```mermaid
graph LR
    S[Screen]
    S -->|"Randomized to A"| DA[Drug A] --> RA[Rest] --> FA[Follow]
    S -->|"Randomized to B"| DB[B] --> RB[Rest] --> FB[Follow]
    RA -.->|"Repeat until<br/>disease progression"| DA
    RB -.->|"Repeat until<br/>disease progression"| DB
    note1["Total length Drug A cycle: 3 weeks"]
    note2["Total length Drug B cycle: 3 weeks"]
    style S fill:#fef3cd,stroke:#333
    style note1 fill:#fff,stroke:#999,stroke-dasharray:5 5
    style note2 fill:#fff,stroke:#999,stroke-dasharray:5 5
```

**Retrospective View**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        s1[Screen]
        s2[Screen]
    end
    subgraph TE["Treatment Epoch"]
        da["Drug A | Rest A<br/>Repeat until disease progression"]
        db["B | Rest B<br/>Repeat until disease progression"]
    end
    subgraph FU["Follow-up Epoch"]
        f1[Follow]
        f2[Follow]
    end
    s1 --> da --> f1
    s2 --> db --> f2
```

**Trial Design Matrix**

|  | Screen | Treatment | | | | | | Follow-up |
|---|---|---|---|---|---|---|---|---|
| **A** | Screen | Trt A | Rest A | Trt A | Rest A | Trt A | Rest A | Follow-up |
| **B** | Screen | Trt B | Rest B | Trt B | Rest B | Trt B | Rest B | Follow-up |

**ta.xpt**

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
|-----|---------|--------|-------|-----|---------|------|---------|----------|---------|-------|
| 1 | EX5 | TA | A | A | 1 | SCRN | Screen | Randomized to A | | SCREENING |
| 2 | EX5 | TA | A | A | 2 | A | Trt A | | | TREATMENT |
| 3 | EX5 | TA | A | A | 3 | RESTA | Rest A | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 4 | EX5 | TA | A | A | 4 | A | Trt A | | | TREATMENT |
| 5 | EX5 | TA | A | A | 5 | RESTA | Rest A | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 6 | EX5 | TA | A | A | 6 | A | Trt A | | | TREATMENT |
| 7 | EX5 | TA | A | A | 7 | RESTA | Rest A | | | TREATMENT |
| 8 | EX5 | TA | A | A | 8 | FU | Follow-up | | | FOLLOW-UP |
| 9 | EX5 | TA | B | B | 1 | SCRN | Screen | Randomized to B | | SCREENING |
| 10 | EX5 | TA | B | B | 2 | B | Trt B | | | TREATMENT |
| 11 | EX5 | TA | B | B | 3 | RESTB | Rest B | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 12 | EX5 | TA | B | B | 4 | B | Trt B | | | TREATMENT |
| 13 | EX5 | TA | B | B | 5 | RESTB | Rest B | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 14 | EX5 | TA | B | B | 6 | B | Trt B | | | TREATMENT |
| 15 | EX5 | TA | B | B | 7 | RESTB | Rest B | | | TREATMENT |
| 16 | EX5 | TA | B | B | 8 | FU | Follow-up | | | FOLLOW-UP |

## Example 6

An oncology trial with cycles of different lengths: Drug A in 3-week cycles (longer treatment, short rest), Drug B in 4-week cycles (short treatment, long rest). Maximum 4 cycles of Drug A, 3 cycles of Drug B.

Because the treatment epoch for arm A has more elements than arm B, TAETORD is 10 for the follow-up element in arm A, but 8 for follow-up in arm B. Gaps in TAETORD values are acceptable.

**Study Schema**

```mermaid
graph LR
    S[Screen]
    S -->|"Randomized to A"| DA[Drug A] --> RA[Rest] --> FA[Follow]
    S -->|"Randomized to B"| DB[B] --> RB[Rest] --> FB[Follow]
    RA -.->|"Repeat until<br/>disease progression"| DA
    RB -.->|"Repeat until<br/>disease progression"| DB
    note1["Total length Drug A cycle: 3 weeks"]
    note2["Total length Drug B cycle: 4 weeks"]
    style S fill:#fef3cd,stroke:#333
    style note1 fill:#fff,stroke:#999,stroke-dasharray:5 5
    style note2 fill:#fff,stroke:#999,stroke-dasharray:5 5
```

**Retrospective View**

```mermaid
graph LR
    subgraph SE["Screening Epoch"]
        s1[Screen]
        s2[Screen]
    end
    subgraph TE["Treatment Epoch"]
        da["Drug A | Rest A<br/>Repeat until disease progression<br/>(3-week cycles)"]
        db["B | Rest B<br/>Repeat until disease progression<br/>(4-week cycles)"]
    end
    subgraph FU["Follow-up Epoch"]
        f1[Follow]
        f2[Follow]
    end
    s1 --> da --> f1
    s2 --> db --> f2
```

**Trial Design Matrix**

|  | Screen | Treatment | | | | | | | | Follow-up |
|---|---|---|---|---|---|---|---|---|---|---|
| **A** | Screen | Trt A | Rest A | Trt A | Rest A | Trt A | Rest A | Trt A | Rest A | Follow-up |
| **B** | Screen | Trt B | Rest B | Trt B | Rest B | Trt B | Rest B | | | Follow-up |

**ta.xpt**

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
|-----|---------|--------|-------|-----|---------|------|---------|----------|---------|-------|
| 1 | EX6 | TA | A | A | 1 | SCRN | Screen | Randomized to A | | SCREENING |
| 2 | EX6 | TA | A | A | 2 | A | Trt A | | | TREATMENT |
| 3 | EX6 | TA | A | A | 3 | RESTA | Rest A | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 4 | EX6 | TA | A | A | 4 | A | Trt A | | | TREATMENT |
| 5 | EX6 | TA | A | A | 5 | RESTA | Rest A | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 6 | EX6 | TA | A | A | 6 | A | Trt A | | | TREATMENT |
| 7 | EX6 | TA | A | A | 7 | RESTA | Rest A | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 8 | EX6 | TA | A | A | 8 | A | Trt A | | | TREATMENT |
| 9 | EX6 | TA | A | A | 9 | RESTA | Rest A | | | TREATMENT |
| 10 | EX6 | TA | A | A | 10 | FU | Follow-up | | | FOLLOW-UP |
| 11 | EX6 | TA | B | B | 1 | SCRN | Screen | Randomized to B | | SCREENING |
| 12 | EX6 | TA | B | B | 2 | B | Trt B | | | TREATMENT |
| 13 | EX6 | TA | B | B | 3 | RESTB | Rest B | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 14 | EX6 | TA | B | B | 4 | B | Trt B | | | TREATMENT |
| 15 | EX6 | TA | B | B | 5 | RESTB | Rest B | | If disease progression, go to Follow-up Epoch | TREATMENT |
| 16 | EX6 | TA | B | B | 6 | B | Trt B | | | TREATMENT |
| 17 | EX6 | TA | B | B | 7 | RESTB | Rest B | | | TREATMENT |
| 18 | EX6 | TA | B | B | 8 | FU | Follow-up | | | FOLLOW-UP |

## Example 7

Example Trial 7, RTOG 93-09, involves treatment of lung cancer with chemotherapy and radiotherapy, with or without surgery. This is a complex 2-arm trial (CR = Chemotherapy and Radiation; CRS = Chemotherapy, Radiation, and Surgery) with 4 epochs (Screening, Induction Treatment, Continuation Treatment, Follow-up) and major "skip forward" arrows for disease progression.

Both the induction and additional chemotherapy are given in 2 cycles. The second induction cycle is different for the 2 arms, since radiation therapy for those assigned to the non-surgery arm includes a "boost" which those assigned to the surgery arm do not receive.

**Study Schema (2-arm model)**

```mermaid
graph LR
    S[Screen]
    S -->|"Randomized to CR"| ICR1["Initial<br/>Chemo+RT"] --> CRNS["Chemo+RT<br/>(non-Surgery)"]
    CRNS --> C1[Chemo] --> C2[Chemo] --> FU1[Follow-up]
    CRNS -.->|"If progression"| FU1

    S -->|"Randomized to CRS"| ICR2["Initial<br/>Chemo+RT"] --> CRS["Chemo+RT<br/>(Surgery)"]
    CRS --> R3["3-5w Rest"] --> SURG[Surgery] --> R4["4-6w Rest"] --> C3[Chemo] --> C4[Chemo] --> FU2[Follow-up]
    CRS -.->|"If progression"| FU2
    CRS -.->|"Not eligible<br/>for surgery"| C3

    style S fill:#fef3cd,stroke:#333
    style SURG fill:#f8d7da,stroke:#333
```

**Prospective View**

```mermaid
graph LR
    subgraph SE["Screen Epoch"]
        s1[Screen]
        s2[Screen]
    end
    subgraph IE["Induction Treatment Epoch"]
        cr1["Chemo+Rad"] --> cr2["Chemo+Rad*"]
        cs1["Chemo+Rad"] --> cs2["Chemo+Rad**"]
    end
    subgraph CE["Continuation Treatment Epoch"]
        cb["Chemo+Boost"] --> cc1[Chemo]
        r3["3-5w Rest"] --> sg[Surgery] --> r4["4-6w Rest"] --> cc3[Chemo] --> cc4[Chemo]
    end
    subgraph FE["Follow-up Epoch"]
        f1[FU]
        f2[FU]
    end
    s1 --> cr1
    cr2 --> cb
    cc1 --> f1
    s2 --> cs1
    cs2 --> r3
    cc4 --> f2
    cr2 -.->|"If progression"| f1
    cs2 -.->|"If progression"| f2
    cs2 -.->|"Not eligible for surgery"| cc3
```

> *Disease evaluation earlier, **Disease evaluation later

**Retrospective View**

Same epoch structure as the Prospective View. The elements in the Continuation Treatment Epoch for the CR arm do not fill the space compared to the CRS arm, reflecting different treatment durations between the 2 arms.

**Trial Design Matrix**

|  | Screen | Induction | Continuation | | | | Follow-up |
|---|---|---|---|---|---|---|---|
| **CR** | Screen | Initial Chemo + RT | Chemo + RT (non-Surgery) | Chemo | Chemo | | Off Treatment Follow-up |
| **CRS** | Screen | Initial Chemo + RT | Chemo + RT (Surgery) | 3-5 w Rest | Surgery | 4-6 w Rest | Chemo | Chemo | Off Treatment Follow-up |

**ta.xpt**

| Row | STUDYID | DOMAIN | ARMCD | ARM | TAETORD | ETCD | ELEMENT | TABRANCH | TATRANS | EPOCH |
|-----|---------|--------|-------|-----|---------|------|---------|----------|---------|-------|
| 1 | EX7 | TA | 1 | CR | 1 | SCRN | Screen | Randomized to CR | | SCREENING |
| 2 | EX7 | TA | 1 | CR | 2 | ICR | Initial Chemo + RT | | | INDUCTION TREATMENT |
| 3 | EX7 | TA | 1 | CR | 3 | CRNS | Chemo+RT (non-Surgery) | | If progression, skip to Follow-up. | INDUCTION TREATMENT |
| 4 | EX7 | TA | 1 | CR | 4 | C | Chemo | | | CONTINUATION TREATMENT |
| 5 | EX7 | TA | 1 | CR | 5 | C | Chemo | | | CONTINUATION TREATMENT |
| 6 | EX7 | TA | 1 | CR | 6 | FU | Off Treatment Follow-up | | | FOLLOW-UP |
| 7 | EX7 | TA | 2 | CRS | 1 | SCRN | Screen | Randomized to CRS | | SCREENING |
| 8 | EX7 | TA | 2 | CRS | 2 | ICR | Initial Chemo + RT | | | INDUCTION TREATMENT |
| 9 | EX7 | TA | 2 | CRS | 3 | CRS | Chemo+RT (Surgery) | | If progression, skip to Follow-up. If no progression, but subject is ineligible for or does not consent to surgery, skip to Chemo. | INDUCTION TREATMENT |
| 10 | EX7 | TA | 2 | CRS | 4 | R3 | 3-5 week rest | | | CONTINUATION TREATMENT |
| 11 | EX7 | TA | 2 | CRS | 5 | SURG | Surgery | | | CONTINUATION TREATMENT |
| 12 | EX7 | TA | 2 | CRS | 6 | R4 | 4-6 week rest | | | CONTINUATION TREATMENT |
| 13 | EX7 | TA | 2 | CRS | 7 | C | Chemo | | | CONTINUATION TREATMENT |
| 14 | EX7 | TA | 2 | CRS | 8 | C | Chemo | | | CONTINUATION TREATMENT |
| 15 | EX7 | TA | 2 | CRS | 9 | FU | Off Treatment Follow-up | | | FOLLOW-UP |

## Trial Arms Issues

### Distinguishing Between Branches and Transitions

Both the Branch and Transition columns contain rules, but the 2 columns represent 2 different types of rules. **Branch rules** represent forks in the trial flowchart, giving rise to separate arms. The rule underlying a branch appears in multiple records, once for each "fork" of the branch. **Transition rules** are used for choices within an arm. The value for TATRANS does contain a choice (an "if" clause). In Example Trial 4, subjects who receive 1, 2, 3, or 4 cycles of treatment A are all considered to belong to arm A.

### Subjects Not Assigned to an Arm

Some trial subjects may drop out of the study before they reach all of the branch points in the trial design. In the Demographics (DM) domain, the values of ARM and ARMCD must be supplied for such subjects, but the special values used for these subjects should not be included in the Trial Arms (TA) dataset; only complete arm paths should be described in the TA dataset. See DM Example 3 for how to represent ARM and ARMCD values for such trials.

### Defining Epochs

The series of examples for the TA dataset provides a variety of scenarios and guidance about how to assign epoch in those scenarios. In general, assigning epochs for blinded trials is easier than for unblinded trials. The blinded view of the trial will generally make the possible choices clear. For unblinded trials, the comparisons that will be made between arms can guide the definition of epochs.

### Rule Variables

The Branch and Transition columns shown in the example tables are variables with a Role of "Rule." The values of a Rule variable describe conditions under which something is planned to happen. At the moment, values of Rule variables are text. At some point in the future, it is expected that a mechanism to provide machine-readable rules will become available. Other Rule variables are present in the Trial Elements (TE) and Trial Visits (TV) datasets.

## Source: `domains/TV/spec.md`

# TV — Trial Visits

> Class: Trial Design | Structure: One record per planned Visit per Arm

### STUDYID
- **Order:** 1
- **Label:** Study Identifier
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Unique identifier for a study.

### DOMAIN
- **Order:** 2
- **Label:** Domain Abbreviation
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Identifier
- **Core:** Req
- **CDISC Notes:** Two-character abbreviation for the domain.

### VISITNUM
- **Order:** 3
- **Label:** Visit Number
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Topic
- **Core:** Req
- **CDISC Notes:** Clinical encounter number. Numeric version of VISIT, used for sorting.

### VISIT
- **Order:** 4
- **Label:** Visit Name
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Req
- **CDISC Notes:** Description of clinical encounter. This is often defined in the protocol. Used in addition to VISITNUM and/or VISITDY as a text description of the clinical encounter.

### VISITDY
- **Order:** 5
- **Label:** Planned Study Day of Visit
- **Type:** Num
- **Controlled Terms:** 
- **Role:** Timing
- **Core:** Perm
- **CDISC Notes:** Planned study day of VISIT. Due to its sequential nature, used for sorting.

### ARMCD
- **Order:** 6
- **Label:** Planned Arm Code
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Record Qualifier
- **Core:** Exp
- **CDISC Notes:** 1. ARMCD is limited to 20 characters and does not have special character restrictions. The maximum length of ARMCD is longer than for other "short" variables to accommodate the kind of values that are likely to be needed for crossover trials. For example, if ARMCD values for a 7-period crossover were constructed using 2-character abbreviations for each treatment and separating hyphens, the length of ARMCD values would be 20.  2. If the timing of visits for a trial does not depend on which arm a subject is in, then ARMCD should be null.

### ARM
- **Order:** 7
- **Label:** Description of Planned Arm
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Synonym Qualifier
- **Core:** Perm
- **CDISC Notes:** 1. Name given to an arm or treatment group.  2. If the timing of visits for a trial does not depend on which arm a subject is in, then Arm should be left blank.

### TVSTRL
- **Order:** 8
- **Label:** Visit Start Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Req
- **CDISC Notes:** Rule describing when the visit starts, in relation to the sequence of elements.

### TVENRL
- **Order:** 9
- **Label:** Visit End Rule
- **Type:** Char
- **Controlled Terms:** 
- **Role:** Rule
- **Core:** Perm
- **CDISC Notes:** Rule describing when the visit ends, in relation to the sequence of elements.
---

## Cross References

### Related Domains
- **Same class (Trial Design):** TA, TD, TE, TI, TM, TS
- **Trial Design:** [TA](../TA/) — visits reference arms
- **Trial Design:** [SE](../SE/) — planned visits vs actual subject elements

### General References
- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules
- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name

### Model Definition
- [Trial Design class definition](../../model/05_study_level_data.md)

## Source: `domains/TV/assumptions.md`

# TV — Assumptions

1. Although the general structure of the Trial Visits (TV) dataset is "One Record per Planned Visit per Arm," for many clinical trials—particularly blinded clinical trials—the schedule of visits is the same for all arms, and the structure of the TV dataset will be "One Record per Planned Visit." If the schedule of visits is the same for all arms, ARMCD should be left blank for all records in the TV dataset. For trials with trial visits that are different for different arms (e.g., Example Trial 7 in Section 7.2.1, Trial Arms), ARMCD and ARM should be populated for all records. If some visits are the same for all arms, and some visits differ by arm, then ARMCD and ARM should be populated for all records, to ensure clarity, even though this will mean creating near-duplicate records for visits that are the same for all arms.

2. A visit may start in one element and end in another. This means that a visit may start in one epoch and end in another. For example, if one of the activities planned for a visit is the administration of the first dose of study drug, the visit might start in the screen epoch and end in a treatment epoch.

3. TVSTRL describes the scheduling of the visit and should reflect the wording in the protocol. In many trials, all visits are scheduled relative to the study's day 1 (RFSTDTC). In such trials, it is useful to include VISITDY, which is, in effect, a special case representation of TVSTRL.

4. Note that there is a subtle difference between the following 2 examples. In the first case, if visit 3 were delayed for some reason, visit 4 would be unaffected. In the second case, a delay to visit 3 would result in visit 4 being delayed as well.
    a. Case 1: Visit 3 starts 2 weeks after RFSTDTC. Visit 4 starts 4 weeks after RFSTDTC.
    b. Case 2: Visit 3 starts 2 weeks after RFSTDTC. Visit 4 starts 2 weeks after visit 3.

5. Many protocols do not give any information about visit end times because visits are assumed to end on the same day they start. In such a case, TVENRL may be left blank to indicate that the visit ends on the same day it starts. Care should be taken to assure that this is appropriate; common practice may be to record data collected over more than 1 day as occurring within a single visit. Screening visits may be particularly prone to collection of data over multiple days. The examples for this domain show how TVENRL could be populated.

6. The values of VISITNUM in the TV dataset are the valid values of VISITNUM for planned visits. Any values of VISITNUM that appear in subject-level datasets that are not in the TV dataset are assumed to correspond to unplanned visits. This applies, in particular, to the subject-level dataset; see Section 5.5, Subject Visits, for additional information about handling unplanned visits. If a subject-level dataset includes both VISITNUM and VISIT, then records that include values of VISITNUM that appear in the TV dataset should also include the corresponding values of VISIT from the TV dataset.

## Source: `domains/TV/examples.md`

# TV — Examples

## Example 1

The following diagram represents visits as numbered "flags" with visit numbers. Each flag has 2 supports, one at the beginning of the visit and the other at the end of the visit. Note that visits 2 and 3 span epoch transitions. In other words, the transition event that marks the beginning of the run-in epoch (confirmation of eligibility) occurs during visit 2, and the transition event that marks the beginning of the treatment epoch (the first dose of study drug) occurs during visit 3.

This example is based on TA Example Trial 1, a Parallel Design with 3 arms (Placebo, Drug A, Drug B).

**Parallel Design Planned Visits**

```mermaid
graph TD
    subgraph Epochs
        direction LR
        SE["Screening<br/>Epoch"] --- RE["Run-In<br/>Epoch"] --- TE["Treatment<br/>Epoch"]
    end

    V1(("V1")) -.->|"Start of<br/>Screen Epoch"| SE
    V2(("V2")) -.->|"Spans Screen<br/>→ Run-In"| SE
    V2 -.-> RE
    V3(("V3")) -.->|"Spans Run-In<br/>→ Treatment"| RE
    V3 -.-> TE
    V4(("V4")) -.->|"1 wk after<br/>Treatment start"| TE
    V5(("V5")) -.->|"2 wk after<br/>Treatment start"| TE

    style V1 fill:#fff,stroke:#333
    style V2 fill:#fff,stroke:#333
    style V3 fill:#fff,stroke:#333
    style V4 fill:#fff,stroke:#333
    style V5 fill:#fff,stroke:#333
    style SE fill:#fef3cd,stroke:#333
    style RE fill:#d4edda,stroke:#333
    style TE fill:#cce5ff,stroke:#333
```

> Visit 2 spans the Screen → Run-In epoch transition (confirmation of eligibility). Visit 3 spans the Run-In → Treatment epoch transition (first dose of study drug). Below the timeline, 3 arms (Placebo, Drug A, Drug B) share the same visit schedule.

Two TV datasets are shown for this trial. The first shows a somewhat idealized situation, where the protocol has provided specific timings for the visits. The second shows a more common situation, where the timings have been described only loosely.

**tv.xpt (specific timings)**

| Row | STUDYID | DOMAIN | VISITNUM | TVSTRL | TVENRL |
|-----|---------|--------|----------|--------|--------|
| 1 | EX1 | TV | 1 | Start of Screen Epoch | 1 hour after start of Visit |
| 2 | EX1 | TV | 2 | 30 minutes before end of Screen Epoch | 30 minutes after start of Run-in Epoch |
| 3 | EX1 | TV | 3 | 30 minutes before end of Run-in Epoch | 1 hour after start of Treatment Epoch |
| 4 | EX1 | TV | 4 | 1 week after start of Treatment Epoch | 1 hour after start of Visit |
| 5 | EX1 | TV | 5 | 2 weeks after start of Treatment Epoch | 1 hour after start of Visit |

**tv.xpt (loosely described timings)**

| Row | STUDYID | DOMAIN | VISITNUM | TVSTRL | TVENRL |
|-----|---------|--------|----------|--------|--------|
| 1 | EX1 | TV | 1 | Start of Screen Epoch | |
| 2 | EX1 | TV | 2 | On the same day as, but before, the end of the Screen Epoch | On the same day as, but after, the start of the Run-in Epoch |
| 3 | EX1 | TV | 3 | On the same day as, but before, the end of the Run-in Epoch | On the same day as, but after, the start of the Treatment Epoch |
| 4 | EX1 | TV | 4 | 1 week after start of Treatment Epoch | |
| 5 | EX1 | TV | 5 | 2 weeks after start of Treatment Epoch | At Trial Exit |

Although the start and end rules in this example reference the starts and ends of epochs, the start and end rules of some visits for trials with epochs that span multiple elements will need to reference elements rather than epochs. When an arm includes repetitions of the same element, it may be necessary to use TAETORD as well as an element name to specify when a visit is to occur.

## Trial Visits Issues

### Identifying Trial Visits

In general, a trial's visits are defined in its protocol. The term "visit" reflects the fact that data in outpatient studies is usually collected during a physical visit by the subject to a clinic. Sometimes a trial visit defined by the protocol may not correspond to a physical visit. It may span multiple physical visits, as when screening data is collected over several clinic visits but recorded under one TV name (VISIT) and number (VISITNUM). A trial visit may represent only a portion of an extended physical visit, as when a trial of in-patients collects data under multiple trial visits for a single hospital admission.

### Trial Visit Rules

Visit start rules are different from element start rules in that they usually describe when a visit should occur; element start rules describe the moment at which an element is considered to start. There are usually gaps between visits, periods of time that do not belong to any visit, so it is usually not necessary to identify the moment when one visit stops and another starts.

Visit start rules are usually expressed relative to the start or end of an element or epoch (e.g., "1-2 hours before end of First Wash-out", "8 weeks after end of 2nd Treatment Epoch"). Note that the visit may or may not occur during the element used as the reference for the visit start rule.

### Visit Schedules Expressed with Ranges

Ranges may be used to describe the planned timing of visits (e.g., 12-16 days after the start of 2nd Element), but this is different from the "windows" that may be used in selecting data points to be included in an analysis associated with that visit.

### Contingent Visits

Some data collection is contingent on the occurrence of a "trigger" event or disease milestone (see Section 7.3.3, Trial Disease Milestones (TM)). When such planned data collection involves an additional clinic visit, a "contingent" visit may be included in the TV table, with a rule that describes the circumstances under which it will take place. Because values of VISITNUM must be assigned to all records in the TV dataset, a contingent visit included in the TV dataset must have a VISITNUM, but the VISITNUM value might not be a "chronological" value. If contingent visits are not included in the TV dataset, then they would be treated as unplanned visits in the Subject Visits (SV) domain (see Section 6.2.8, Subject Visits).
