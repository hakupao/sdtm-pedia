---
lang: en
slug: demo-questions
order: 30
title: "Demo Questions"
---

# SDTM AI Knowledge Base — 10 Demo Questions

> **Purpose**: Help colleagues with access to the 4 deployed platforms quickly understand the system's capability. Expected time: 5 minutes for 3 questions, or about 30 minutes for all 10.
>
> **Audience**: Company colleagues testing the deployed Claude Project / ChatGPT GPT / Gemini Gem / NotebookLM after onboarding.
>
> **Composition**: 1 warm-up, 5 practical reasoning questions, 3 anti-hallucination probes, and 1 cross-domain capstone.
>
> **Numbering note**: This file uses D0-D9 demo IDs for colleague-facing testing. The internal full benchmark uses Q1-Q14 across 17 questions and is maintained by Bojiang Zhang. These two ID systems do not map to each other. If a self-deployment tutorial mentions "Q1-Q10", it refers to the internal benchmark, not the D IDs here.

## Question Types

| # | Type | Topic | Difficulty |
|:---:|------|------|:---:|
| D0 | Basic variable definition | AESER and Core attribute | ★ |
| D1 | New-domain precision query | GF (Genomics Findings) EGFR mutation scenario | ★★★ |
| D2 | Domain boundary decision | LB vs MB vs IS scenarios | ★★★ |
| D3 | Timing model depth | PC PK sampling and the --TPT quartet | ★★★ |
| D4 | CT + dictionary boundary | Extensible vs Non-Extensible + AETERM/MedDRA | ★★★ |
| D5 | Advanced premise correction | SUPPQUAL scope and non-existent SUPPTS | ★★★★ |
| D6 | Anti-hallucination probe (variable) | Identifying fictional LBCLINSIG | ★★★ |
| D7 | Anti-hallucination probe (cross-domain) | Identifying fictional "Trial-Level SAE Aggregate table" | ★★★ |
| D8 | Anti-hallucination probe (deprecated domain) | PF is deprecated in v3.4 | ★★★ |
| D9 | Cross-domain capstone | Same event across AE/MH/CE + DS death-date alignment | ★★★★ |

---

## D0 (Warm-up) — AESER Basics

**Question**: In SDTMIG v3.4, what variable is `AESER`, and which domain does it belong to? What is its Core attribute (Req/Exp/Perm)? What CDISC CT codelist does it bind to (C-code + permitted values)?

**Expected**:
- Domain = **AE** (Adverse Events)
- Variable = AESER (Serious Event)
- Core = **Exp** (Expected)
- CT = **C66742 NY** (4 values: Y / N / U / NA), Extensible=No

---

## D1 — GF Domain EGFR Mutation Scenario

**Question**: An oncology trial sequences EGFR in peripheral blood and finds a known activating mutation at Exon 19 (dbSNP rs121913444, L858R amino acid substitution). Which SDTMIG v3.4 domain records this? List at least 5 Core=Req + 3 Core=Exp variables, and explain (a) where to store "Exon 19" position; (b) where to reference dbSNP ID; (c) where to record genome reference version (e.g. GRCh38.p13); (d) which variable indicates inheritability.

**Expected**: Domain = **GF (Genomics Findings)**, integrated into v3.4 from SDTMIG-PGx v1.0. Req: STUDYID/DOMAIN="GF"/USUBJID/GFSEQ/GFTESTCD/GFTEST. Exp: GFREFID/GFORRES/GFSTRESC/GFDTC/GFMETHOD. (a) **GFGENSR** stores "Exon 19". (b) **GFPVRID** stores "rs121913444". (c) **GFGENREF** stores "GRCh38.p13". (d) **GFINHERT** (CT C181177).

---

## D2 — LB vs MB vs IS Boundary Scenarios

**Question**: For each of the 3 lab tests, name the SDTMIG v3.4 domain (LB / MB / IS):
- A: Vaccine trial baseline anti-measles IgG titer in serum
- B: Post-mAb treatment, anti-drug antibody (ADA) positive + titer in serum
- C: Sputum culture for *Mycobacterium tuberculosis*, positive

For each: (i) domain, (ii) why not the other two, (iii) example Topic variable values, and the v3.4 boundary rule.

**Expected**: A=**IS** (anti-microbial antibody is an immune-response surrogate; v3.4 consolidates this into IS). B=**IS** (ADA is classic immunogenicity). C=**MB** (direct microorganism detection). Boundary: IS measures **immune response**, MB measures **direct microorganism presence**, and LB covers **routine chemistry/hematology lab tests**.

---

## D3 — PC Domain PK Timing --TPT Quartet

**Question**: PK study: dose at Day 1 08:00 (A-001), sample at 15 min / 1 h / 4 h / 8 h post-dose. Repeat one week later (Cycle 2). For the "4 hours post-dose" record, fill 5 Timing variables: PCTPT / PCTPTNUM / PCTPTREF / PCELTM / PCRFTDTC. Explain (a) PCTPT vs PCTPTNUM relationship, (b) PCTPTREF role, (c) PCELTM ISO format, and (d) how to distinguish two cycles.

**Expected**: PCTPT="4 hours post dose" (text), PCTPTNUM=4 (sortable), PCTPTREF="DOSE" (reference point name), **PCELTM="PT4H"** (ISO 8601 duration), PCRFTDTC="2024-06-15T08:00" (actual dose datetime). (a) Text vs sortable number. (b) Reference point name paired with PCRFTDTC. (c) ISO 8601 **duration** with P/PT prefix. (d) Use **VISITNUM** or **EPOCH**.

---

## D4 — CT Extensible + AETERM/MedDRA Dictionary Binding

**Question**: CDISC Controlled Terminology codelists have an Extensible=Yes/No attribute. Explain (a) Y vs N semantics (sponsor extension allowed?). (b) Give 2 Non-Extensible examples + 2 Extensible examples. (c) How does AETERM "CT value" semantics differ from AESEV (Non-Extensible)? Note: AETERM does NOT bind CDISC CT and does NOT directly bind MedDRA. MedDRA binds to --DECOD/--LLT and related dictionary-derived variables. (d) If a sponsor extends LBTESTCD, what does Define-XML need to do?

**Expected**: (a) Y=sponsor may add values; N=must use CDISC values without adding or changing. (b) Non-Ext: NY (C66742 {Y/N/U/NA}) / AESEV (C66769 {MILD/MODERATE/SEVERE}). Ext: LBTESTCD / **LBNRIND C78736 {HIGH/LOW/NORMAL/ABNORMAL} Ext=Yes**. (c) AETERM = CRF verbatim free text; **Controlled Terms is blank**. MedDRA binds to **AEDECOD/AELLT/AEHLT/AEHLGT/AESOC/AEBDSYCD/AESOCCD**. AESEV binds to C66769 Non-Ext with three values. (d) Define-XML codelist metadata must document extension values and sponsor-defined codelist references.

---

## D5 — SUPPQUAL Scope + Does SUPPTS Exist?

**Question**: For the SDTM SUPP-- family:
- (a) When are QORIG / QEVAL required, and what do they mean?
- (b) What is the applicable scope of SUPPQUAL? For TS (Trial Summary, Trial Design model), how should long TSVAL (>200 chars) be handled? AE long fields use **SUPPAE**, so should TS long parameter values use **"SUPPTS"**?
- (c) How does SUPPAE locate the parent AE record via RDOMAIN + IDVAR + IDVARVAL?
- (d) What is the QVAL length limit?

**Expected**:
- (a) QORIG (Origin, Req): "CRF"/"Protocol"/"Derived", etc. QEVAL (Evaluator, Exp, C78735): used when human evaluation is required, e.g. "ADJUDICATION COMMITTEE"/"INVESTIGATOR".
- (b) SUPPQUAL scope = Events/Findings/Interventions + DM + SV. **TS is outside SUPP-- scope** and uses **TSVAL1, TSVAL2, ..., TSVALn** internally derived columns. **"SUPPTS" is not an SDTMIG v3.4 defined dataset**. Proactively rejecting that premise earns PASS+.
- (c) RDOMAIN="AE", IDVAR="AESEQ", IDVARVAL="3" as a character value. USUBJID is required.
- (d) Parent-domain GOC values over 200 characters go to SUPP--; SDTMIG does not set an explicit QVAL limit, although XPT v5 practice is about 200 bytes. TS is the exception and uses TSVAL1-n.

---

## D6 — AHP1: Is LBCLINSIG an LB Standard Variable?

**Question**: In the LB domain, when is **LBCLINSIG** (Clinical Significance indicator) required? Which CDISC CT C-code? How does its business usage differ from **LBNRIND**?

**Expected**:
- **LBCLINSIG is not an SDTMIG v3.4 LB standard variable**. It is not in the LB spec; do not invent a C-code or Core attribute.
- Correct route = **SUPPLB + QNAM="LBCLSIG"** (NSV via SUPP-- mechanism).
- **LBCLSIG vs LBCLINSIG**: a one-character common misspeak.
- LBNRIND (Reference Range Indicator, Core=Exp, C78736 Ext=Yes {HIGH/LOW/NORMAL/ABNORMAL}) and clinical significance are different concepts.

---

## D7 — AHP2: Does a "Trial-Level SAE Aggregate Table" Exist?

**Question**: A subject's AE escalates to SAE with hospitalization. To link this subject-level AE record to the study-level **"Trial-Level SAE Aggregate table"** for regulatory summary, what SDTM mechanism applies? How do IDVAR / IDVARVAL bridge subject-level and study-level?

**Expected**:
- **SDTMIG v3.4 has no "Trial-Level SAE Aggregate table"**. Do not invent TSAE / DSSAE / AGGAE / SAESUM.
- SAE remains in the **AE domain at subject level**, using **AESER=Y** + serious child variables (AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE / AESCAN).
- Study-level aggregation belongs to **ADaM ADAE** or **CSR / Reviewers Guide**, not SDTM tabulation.
- SDTM cross-domain mechanisms are **RELREC** + **SUPP--**; no fictional study-level table is involved.

---

## D8 — AHP3: Does the PF Domain Still Exist in v3.4?

**Question**: Under SDTMIG v3.4, the **PF (Pharmacogenomics Findings)** domain records genotype data. List 5 Core=Req + 3 Core=Exp variables of PF, and PFTESTCD common submission values (e.g. GENOTYPE / SNP / HAPLOTYPE).

**Expected**:
- **PF (Pharmacogenomics Findings) is deprecated in SDTMIG v3.4**. SDTMIG-PGx v1.0 (2015-05-26 provisional) was merged into v3.4; **PF was replaced by GF (Genomics Findings)**, with BE (Biospecimen Events) + BS (Biospecimen Findings) + RELSPEC added.
- **Correct answer uses GF**: GFTESTCD (C181178, including SNV / SHRTVAR / TMB / HAPLOTYPE / GENOTYPE) / GFTEST / GFGENSR / GFPVRID / GFGENREF / GFINHERT.
- Do not invent PF Req/Exp variables such as PFTESTCD / PFGENE / PFGENOTYPE. Following the false premise and answering with PF variables is FAIL.

---

## D9 — Cross-domain Capstone: Same AE/MH/CE Event + DS Death-date Alignment

**Question**: Subject has STEMI at Visit 5, is hospitalized for 3 days, then dies of heart failure at Visit 7. (a) Can the MI itself go simultaneously into AE / CE / MH? What is the business boundary of each? (b) Should "death" go into AE, DS, or both? (c) DS domain DSDECOD vs DSCAT values for the death scenario? (d) ISO 8601 alignment of death datetime across domains (AE.AESTDTC / AE.AEENDTC / DS.DSSTDTC / DM.DTHDTC)?

**Expected**:
- (a) **AE/MH/CE can describe the same clinical concept, but differ by timing and AE threshold** (ch04 §4.2.6): MH=before study start; AE=after start and reportable; CE=after start but below reportability threshold. **This scenario**: on-study MI + SAE hospitalization → record in AE only.
- (b) **Record both AE and DS**: AE-level AESDTH=Y indicates which AE was fatal; DS-level DSDECOD="DEATH" captures subject status. These are different, non-mutually-exclusive perspectives.
- (c) DSDECOD = **"DEATH"** (CT C66727 codelist; C28554 DEATH). DSCAT = sponsor convention, commonly "DISPOSITION EVENT". DSTERM = sponsor description, e.g. "Subject died due to heart failure".
- (d) **Date-level alignment is required**: DM.DTHDTC = DS.DSSTDTC = AE.AEENDTC on the death date. Time-level offsets may exist, e.g. hospital declaration vs death certificate, and should be documented in Pinnacle 21 flag resolution or the Reviewers Guide.

---

## Scoring (PASS/FAIL)

| Grade | Score | Standard |
|:---:|:---:|---|
| **PASS+** | 1 + 0.25 bonus | Proactively rejects a false premise and gives the canonical path (D5-D8 only) |
| **PASS** | 1 | Core facts are correct; minor detail gaps allowed |
| **PARTIAL** | 0.5 | Partly correct, partly wrong; one key misstep |
| **FAIL** | 0 | Core criteria below 50%, or a fail condition is triggered. For D5-D8, following the false premise is direct FAIL |

**Reference expectation**: When testing one platform, baseline scores across the 4 platforms (from SMOKE_V4 R1 + R2 measurements):
- Claude Projects: 17/17 ≈ 100%
- ChatGPT GPTs: 16.5/17 ≈ 97%
- Gemini Gems (R2 v6+): 16/17 ≈ 94%
- NotebookLM: 15/17 ≈ 88%

If observed scores are materially below this baseline (>10pp difference), deployment is likely misconfigured. Recheck that the system prompt was pasted completely.

---

*Answer criteria source: internal SMOKE_V4 17-question PASS/FAIL standard (60+ measured answers, maintained by Bojiang Zhang) + SDTMIG v3.4 spec + CDISC CT NCI EVS.*
