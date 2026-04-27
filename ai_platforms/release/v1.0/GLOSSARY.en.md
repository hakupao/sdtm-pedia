---
lang: en
slug: glossary
order: 40
title: "Glossary"
---

# Glossary — SDTM AI Knowledge Base

> One-page lookup. When you encounter an unfamiliar term, return here. Three categories: SDTM industry / AI platform / project-internal.

## 1. SDTM Industry Terms

| Term | Explanation |
|---|---|
| **SDTM** | Study Data Tabulation Model. One of the CDISC standards. Defines how clinical trial data is organized into tables (domains / variables / codelists). |
| **SDTMIG v3.4** | SDTM Implementation Guide. Turns the SDTM model into concrete specifications: which domain has which variables, and what Core attribute each variable carries. v3.4 (2021) is the mainstream version used in this project. |
| **CDISC** | Clinical Data Interchange Standards Consortium. Governs SDTM, ADaM, CDASH, and related standards. Required for FDA submissions. |
| **Domain** | SDTM divides clinical data by topic into 63 domains — e.g. AE (Adverse Events) / DM (Demographics) / LB (Lab) / EX (Exposure). Each domain is one table. |
| **Variable** | A column within a domain. For example, the AE domain includes AESER (serious event flag) / AETERM (verbatim term as reported) / AEDECOD (MedDRA decoded term), among others. |
| **Core attribute** | The "required level" of each variable: **Req** (Required — must be populated) / **Exp** (Expected — should be present; absence needs justification) / **Perm** (Permissible — optional). Examples: USUBJID Core=Req, AESER Core=Exp, AESEV Core=Perm. |
| **CT (Controlled Terminology)** | The list of allowed values for a given variable, as defined by CDISC. For example, AESER may only contain Y / N / U / NA — writing "yes" or "是" is not permitted. |
| **C-code** | A unique NCI EVS identifier for each codelist. For example, the NY codelist = C66742; the AESEV codelist = C66769. These C-codes are recognized across SDTMIG, NCI EVS Browser, and Pinnacle 21. |
| **Extensible** | Indicates whether a codelist allows sponsor-defined additions. **Extensible=Yes** (e.g. LBNRIND has 4 standard values and sponsors may add new ones) vs. **Non-Extensible** (e.g. NY is strictly Y / N / U / NA — no additions allowed). |
| **Codelist** | A named set of allowed values. For example, the LBNRIND codelist contains 4 standard values: {HIGH / LOW / NORMAL / ABNORMAL}. Used interchangeably with "CT." |
| **SUPPQUAL / SUPP--** | Supplemental qualifier domains. When standard SDTM variables cannot accommodate a data point, the SUPPQUAL structure (IDVAR / IDVARVAL / QNAM / QVAL) is used as a four-piece supplement. Every standard domain has a corresponding SUPP-- (e.g. AE ↔ SUPPAE / LB ↔ SUPPLB). |
| **NSV** | Non-Standard Variable — a variable that can only go into SUPPQUAL, not into the parent domain. SUPP-- is the container for NSVs. |
| **RELREC / RELSPEC / RELSUB** | The three-piece SDTM cross-domain relationship mechanism. RELREC = record-level linkage (e.g. one AE record linked to one EX record); RELSPEC = specimen-level; RELSUB = subject-level. |
| **MedDRA** | Medical Dictionary for Regulatory Activities. The internationally used medical terminology dictionary. AE domain variables such as AEDECOD / AEHLT / AEHLGT are bound to MedDRA. Not part of CDISC CT, but the AE domain depends on it heavily. |
| **NCI EVS** | National Cancer Institute Enterprise Vocabulary Services. The official CDISC CT publication site: [browser.evs.nci.nih.gov](https://browser.evs.nci.nih.gov). Use this for real-time lookup of long-tail codelists. |
| **Pinnacle 21** | An industry-standard automated compliance-checking tool that validates SDTM datasets against the standard — essentially a "linter for SDTM." This project does not connect to Pinnacle 21 directly; hands-on validation requires cdisc.org or the tool itself. |
| **ISO 8601** | The international standard for date and time formats (e.g. `2026-04-27T13:45Z`, `2026-04-27`, `--MM-DD`). All SDTM `--DTC` variables must be populated in ISO 8601 format. |

## 2. AI Platform / RAG Terms

| Term | Explanation |
|---|---|
| **System Prompt / Instructions** | The "operating manual" given to an AI: defines its identity, priorities, gating rules, and anchors. Called differently across platforms — ChatGPT: Instructions / Custom Instructions; Claude: System Prompt; Gemini: Gem instructions; NotebookLM: Custom mode. |
| **Custom mode** | One of NotebookLM Chat's three modes (Default / Learning Guide / Custom). The only mode that accepts a system prompt, with a cap of 10K chars. This deployment loads `instructions.md` via Custom mode. |
| **RAG** | Retrieval-Augmented Generation. When the AI receives a question, it first retrieves relevant passages from the knowledge base, then generates an answer grounded in those passages — not from memory alone. All 4 platforms use RAG (NotebookLM enforces the strictest in-KB-only form). |
| **Indexing** | After uploading the knowledge base, the AI reads all content and builds a vector index before chat becomes available. Timing varies by platform (Gemini ~1–3 min / ChatGPT ~5–15 min / Claude / NotebookLM ~2–10 min). |
| **in-KB-only** | NotebookLM's design principle: answers may only come from uploaded sources — no web search, no parametric recall. Questions outside the KB will be declined (PUNT). |
| **PUNT** | NotebookLM jargon for "I don't know — this isn't in my uploaded sources." **PUNT is a feature, not a bug** — it is preferable to hallucination. |
| **Hallucination** | When an AI fabricates plausible-sounding but factually incorrect information to fill a knowledge gap. Preventing hallucination is a core focus of this project. |
| **Anti-Hallucination Probe (AHP)** | Test questions that deliberately embed a false premise (e.g. asking "What variables are in the PF domain?" when PF has been retired), to see whether the AI catches the error rather than playing along. This project uses 3 AHP questions per platform. |
| **PASS+** | A rating above PASS. PASS = the core facts are correct; PASS+ = correct answer AND the AI proactively identifies the false premise in the question. AHP questions are evaluated primarily on PASS+. |
| **Smoke test** | A lightweight pre-deployment check — "turn it on and confirm the basics work" — without aiming for full coverage. In this project, passing demo questions D0 / D1 / D5 counts as a smoke test pass. |
| **token** | The internal counting unit for LLMs. Roughly: 1 Chinese character ≈ 0.5–1 token; 1 English word ≈ 1–2 tokens. Claude Projects capacity is ~3–4M tokens; Gemini has a 1M context window. |
| **Context window** | The maximum number of tokens an LLM can "remember" in one session. Content beyond the limit is dropped. Gemini 1M ≈ ~1,000 pages at once; Claude ~200K–1M. |

## 3. Project-Internal Terms

| Term | Explanation |
|---|---|
| **17 questions / internal full question set** | The SDTM question set used to evaluate each platform: 14 general questions + 3 Anti-Hallucination Probes. See `../../SMOKE_V4.md` §2. |
| **D0–D9 / Demo** | A 10-question quick-demo pack for colleagues, located at `./DEMO_QUESTIONS.md`. Not the same as the internal 17-question set — question numbers do not correspond between the two. |
| **4 quality rules** | Internal process disciplines governing how outputs are produced and reviewed (e.g. "rewrite rate >50% requires independent sampling audit," "failed attempts are archived, never deleted," "every final deliverable requires a retrospective," "self-review is not allowed"). Colleagues don't need to know the details. |
| **LIVE** | A platform that has been fully deployed, run through the complete 17-question evaluation, and passed all quality gates — ready for end-user use. All 4 platforms are currently LIVE. |
| **baseline** | The officially measured score for a given platform on the standard question set. After deploying your own instance, running the same questions should reproduce this score (±2 points tolerance). |

---

## Want to Dig Deeper?

| Topic | Path |
|---|---|
| Full question set + per-platform answers | `../../SMOKE_V4.md` + each platform's `dev/evidence/smoke_v4_answers/` |
| Full limitations list | [`./KNOWN_LIMITATIONS.en.md`](./KNOWN_LIMITATIONS.en.md) |
| Project methodology | `../../claude_projects/docs/RETROSPECTIVE_V2.md` (Claude v2 final retrospective) + `../../notebooklm/docs/RETROSPECTIVE.md` (NotebookLM retrospective) |
| Cross-platform retrospective (4 platforms) | `../../retrospectives/PHASE5_RETROSPECTIVE.md` (v1.0 FINAL) |

> ⚠️ Note: Paths shown as `../../...` or `dev/evidence/...` in this section refer to project-internal artifacts retained by Daisy; they are NOT included in this release pack. Contact Daisy for access if needed.

---
*v1.1 — 2026-04-27 — Maintained by Daisy*
