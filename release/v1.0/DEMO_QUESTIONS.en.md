---
lang: en
slug: demo-questions
order: 30
title: "Example Questions"
---

# Example Questions

Use these questions to learn how to ask SDTM Pedia for useful answers. They are not an exam and not a formal validation plan. For formal work, confirm against official CDISC materials and internal procedures.

## Starter Questions

### 1. What is AESER?

Suggested question:

> What does AESER mean in the AE domain? What are its Core attribute and controlled terminology?

Look for:

- An explanation that AESER relates to serious events.
- A distinction among variable definition, Core attribute, and controlled terminology.
- Reviewable support.

### 2. How do LB, MB, and IS differ?

Suggested question:

> How should LB, MB, and IS be distinguished? Which domain should be considered for serum antibody titer, anti-drug antibody, and bacterial culture results?

Look for:

- Clear boundaries among laboratory, microbiology, and immunology findings.
- Scenario-based explanation rather than definitions only.

### 3. How should --TPT variables in PC be understood?

Suggested question:

> In the PC domain, what do PCTPT, PCTPTNUM, PCELTM, and PCTPTREF represent?

Look for:

- A distinction among planned time point, time point number, elapsed time, and reference point.
- Explanation of their role in pharmacokinetic sampling.

## Intermediate Questions

### 4. How do AETERM and MedDRA variables work together?

Suggested question:

> In the AE domain, what is the relationship among AETERM, AEDECOD, AELLT, AEHLT, AEHLGT, and AESOC?

Look for:

- A distinction between verbatim CRF text, coded term, and hierarchy levels.
- Recognition that MedDRA and CDISC Controlled Terminology are not the same thing.

### 5. Does SUPPQUAL apply to TS?

Suggested question:

> If TSVAL is too long, should SUPPTS be used? Is SUPPTS defined in SDTMIG v3.4?

Look for:

- A clear statement that SUPPTS is not an SDTMIG v3.4 dataset.
- An explanation that Trial Design cases should follow the applicable Trial Design rule rather than a subject-level SUPP-- pattern.

### 6. Is LBCLINSIG an LB standard variable?

Suggested question:

> Is LBCLINSIG a standard LB-domain variable in SDTMIG v3.4? If clinical significance needs to be represented, what should be considered?

Look for:

- Recognition that the variable name is not a standard LB variable.
- Avoidance of invented Core attributes or C-codes.

## Cross-Domain Questions

### 7. Can the same clinical event involve AE, MH, and CE?

Suggested question:

> When would the same myocardial infarction concept be represented in MH, AE, or CE? If it occurs on-study and leads to hospitalization, what should be considered?

Look for:

- Explanation based on timing and reporting threshold.
- A clear distinction among event-type domains.

### 8. How should death be represented in AE and DS?

Suggested question:

> If an AE leads to death, should both AE and DS be recorded? What does each domain represent?

Look for:

- A distinction between the fatal adverse event in AE and subject disposition status in DS.
- A reminder that date consistency and project-level review matter.

## Follow-Up Prompts

After any answer, you can ask:

- `Please provide the basis for that answer.`
- `Does this apply to SDTMIG v3.4?`
- `When should I check the official standard?`
- `If my CRF field is written this way, what should I watch for during mapping?`

These follow-ups help turn an explanation into a reviewable work reference.
