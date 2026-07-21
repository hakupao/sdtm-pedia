---
lang: en
slug: user-guide
order: 10
title: "User Guide"
---

# User Guide

## 1. What This Is

SDTM Pedia is an AI-assisted knowledge base for CDISC SDTM. It organizes commonly needed material from SDTMIG, the SDTM Model, and CDISC Controlled Terminology into a question-and-answer experience.

Think of it as a conversational SDTM reference. It is useful for questions such as "What does this variable mean?", "Which domain fits this scenario?", "Is this controlled terminology applicable?", or "Is this a standard SDTM variable?"

## 2. Who It Is For

- Clinical data management, statistical programming, standards governance, and medical data review teams.
- Project members who need to understand SDTM domains, variables, and controlled terminology.
- Teams doing early review of SDTM mapping decisions.
- Trainers or users demonstrating common SDTM lookup patterns.

If you are new to SDTM, start with the example questions. If you already know SDTM, use it as a traceable lookup assistant.

## 3. Good Questions To Ask

| Scenario | Example |
| --- | --- |
| Variable definition | `What is AESER? What is its Core attribute?` |
| Domain boundary | `How should LB, MB, and IS be distinguished?` |
| Controlled terminology | `What submission values are allowed for LBNRIND?` |
| Cross-domain relationship | `How should death be represented across AE and DS?` |
| Premise check | `Is SUPPTS defined in SDTMIG v3.4?` |

You can ask in Chinese, English, or Japanese. For variable names, domain codes, C-codes, and submission values, keep the original English code so the answer can be checked against CDISC sources.

## 4. Which Platform To Use

| Need | Recommended Platform | Why |
| --- | --- | --- |
| Complex standards reasoning and cross-domain explanation | Claude Projects | Strong fit for longer explanations and multi-step interpretation. |
| Team sharing and everyday lookup | ChatGPT GPTs | Familiar entry point for many organizations. |
| Long-context synthesis and broad comparison | Gemini Gems | Useful for broader source synthesis. |
| Strict source boundary and citation review | NotebookLM | Best when answers should stay close to uploaded source material. |

Most users should start with the instance their team already provides. Read the administrator guides only if you need to configure, maintain, or verify an instance.

## 5. How To Judge an Answer

A work-ready reference answer should usually:

- Identify the relevant SDTM domain, variable, controlled terminology, or standard path.
- Treat non-applicable or non-existent premises cautiously rather than inventing details.
- Provide reviewable support, such as an SDTMIG section, variable name, C-code, or source note.
- State when a question falls outside the current knowledge base.

For regulatory submissions, critical mapping decisions, or formal deliverables, use the answer as a starting point and confirm it through official sources and internal review.

## 6. Quick Start

Try these first:

1. `What is AESER? What are its Core attribute and controlled terminology?`
2. `How do LB, MB, and IS differ? Which domain fits a microbiology culture result?`
3. `Is SUPPTS defined in SDTMIG v3.4? If TSVAL is too long, what should be considered?`

More examples are available in [Example Questions](./DEMO_QUESTIONS.en.md).

## 7. Boundary of Use

SDTM Pedia does not replace CDISC publications, controlled terminology release sources, medical judgment, statistical programming review, or internal SOPs. Formal submission decisions should always be confirmed through official standards and your organization's process.
