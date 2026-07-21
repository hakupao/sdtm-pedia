---
lang: en
slug: known-limitations
order: 50
title: "Known Limitations"
release: v1.4
---

# Known Limitations

This page explains the boundaries of v1.4. These are not simply defects; they help users decide which questions are suitable for direct lookup and which require official-source or internal-process confirmation.

## 0. v1.4 Audit Scope (updated 2026-05-22)

v1.4 is a **prompt-pass-level** release of SDTM Pedia — a full-stack clean rewrite of system prompts / instructions for the three maintained AI platforms (ChatGPT GPTs, Claude Projects, NotebookLM), removing fossil layers accumulated across multiple iteration rounds and restoring KB-grounding as the primary path. It also folds in four minor v1.3 carries.

**Important change — the Gemini Gems platform shifts to a "maintained-but-no-sanity-test" mode starting v1.4**; see §0.A below.

### 0.A. Gemini Gems platform — MAINTAINED_NO_SANITY_TEST (v1.4 onwards)

From v1.4, **SDTM Pedia no longer runs sanity / R4 regression tests against Gemini Gems**, but **continues best-effort maintenance**:

- **Decision date**: 2026-05-22 (user verbal clarification)
- **Triggers**: v1.4 Phase B B1 light sanity exposed that the Gemini v9 prompt fully hallucinates on the PP RELREC Method A/B/C/D question (4/4 mappings wrong). Combined with the long-standing Gemini Pro quota constraint (~4 questions per 5h rolling window) blocking the full 17-question R4 regression, the decision is: **tests stop** (avoid quota waste); **optimization continues** (KB delta + critical prompt fixes).
- **v1.4 Gemini deliverables**:
  - v9 system_prompt gains a Method label anchor block (paralleling ChatGPT v3 L77-80): A=Many-Many (PCGRPID/PPGRPID) / B=One-Many (PCSEQ/PPGRPID) / C=Many-One (PCGRPID/PPSEQ) / D=One-One (PCSEQ/PPSEQ).
  - The v1.4 KB delta (PP/examples §6.3.5.9.3 mapping table) propagates to Gemini gem behavior via KB grounding (even without a bundle re-upload, the modified prompt steers the gem's reasoning toward this table).
- **Maintenance boundaries**:
  - **Continues ✅**: KB delta flows into Gemini gem instructions (release/ ships the Gemini bundle delta); critical prompt fixes (anchor / wrong mapping / other visible KB-grounding repairs).
  - **Stops ❌**: running the sanity test set (B1 4 questions × Gemini, R4 17-question Gemini Pro full regression, smoke probes); the lockstep dashboard (the R3+ maintenance dashboard has been downgraded; Phase 0-5 gates are kept for historical reference only); user-level validation is delegated to self-deploy users.
- **Retained**: `release/v1.3/self_deploy/gemini/` remains the last sanity-verified baseline (v8.1 LIVE, 16/17 R3 PASS). The v1.4 Gemini gem adds v9 refactor + Method label anchor on top of this baseline, but **without sanity coverage** — users self-verify.

### 0.B. v1.4 deliverables (3 platforms in scope)

- **Phase A — Prompt clean rewrite** (3-platform system prompt / instructions clean rewrite, audited by an independent Rule D reviewer):
  - **ChatGPT v3 system_prompt** (120→119 lines + an explicit 4-line Method label anchor mapping): removes v1.0–v1.3 iteration annotations, makes KB-grounding the default-first path, A=Many-Many (PCGRPID/PPGRPID) / B=One-Many (PCSEQ/PPGRPID) / C=Many-One (PCGRPID/PPSEQ) / D=One-One (PCSEQ/PPSEQ).
  - **Claude v3 system_prompt** (125→133 lines; critic reviewer caught attempt 1's truncated 19→7 file table → attempt 2 surgical fix landed PASS_WITH_OBSERVATIONS): 5 essential rules + regex-gated CO-N + the Files A-S table preserved in full.
  - **NotebookLM v3 instructions** (157→156 lines): footer Sources citation kept semantically equivalent (not byte-exact, but behavior preserved); v1.0–v1.3 iteration fossils removed.
  - **A3.1 Claude bundle pipeline architectural fix** (`extract_examples_data.py` SECTION_HDR_RE capture): fixes the `## §N.N.N` heading capture gap that the v1.3 Phase D verifier flagged. Landed in real combat at B1 UI sanity Q-S2 Claude (paper PARTIAL → UI PASS+).

- **Phase B — Light sanity (3 platforms 12/12 PASS; the 4 Gemini cells are excluded due to the drop)**:
  - B1 UI-level (Chrome MCP fire-and-forget): 4 questions × 3 platforms = 12 cells = **10 PASS+ + 2 PASS + 0 PARTIAL + 0 FAIL = 100% PASS**.
  - Question set: Q-S1 BECAT EXTRACTION (v1.3 carry), Q-S2 PP RELREC Method (v1.3 trigger for the v1.4 main refactor), Q-S3 TR TRSTRESN/TRSTRESU typo, Q-S4 DI domain (NotebookLM bucket 25 rename).
  - B2 R4 17-question full regression (Gemini-only scope): **N/A — Gemini sanity testing has stopped** (see §0.A; optimization continues, testing does not).

- **Phase C — Minor carries (4 items)**:
  - **C1 section_coverage.jsonl full pipeline rerun** — closes the v1.3 A5 baseline-stale carry. The P4b deterministic rerun is done (FULL_COVERAGE 101→137, SKELETON 67→46); the full LLM pipeline rerun (P2 increment + P4a forward matcher) is deferred to v1.5 as C1-bis.
  - **C2 UNSOURCED heuristic classifier fix + N=80 sampling** — fixes the DERIVED_FROM_XLSX→REASONABLE_INFERENCE bias that the v1.3 Rule D `scientist` reviewer found; extends from N=40 (v1.3 HIGH stratum) to +40 (v1.4 LOW stratum). Results: 75 RI + 0 XLSX + 0 HALLUCINATED + 5 NEEDS_HUMAN_REVIEW (cumulative N=80); Rule A 10/10 PASS; the bias fix now extends from HIGH to the LOW stratum.
  - **C3 NotebookLM bucket 25 UX tutorial + screenshot** — v1.3 deployment surfaced users forgetting to delete the old source (43 → should be 42); v1.4 `.work/07_release_v1_4/V1_4_DEPLOY_GUIDE.md` adds a prominent reminder; the Chrome MCP screenshot tutorial is deferred to v1.5.
  - **C4 ChatGPT PP RELREC Method label KB anchor** — `PP/examples.md §6.3.5.9.3` gains an explicit 4-row mapping table, resolving the v1.3 Q-S2 ChatGPT PARTIAL label drift (KB + prompt dual-layer anchor). 3-platform bundle rebuild + Gemini v9 system_prompt anchor sync (post 2026-05-22 user clarification).

### 0.C. Reconcile of v1.3 §0 items

| v1.3 §0 item | v1.4 status |
|---|---|
| 4-platform system_prompt/instructions full-stack refactor (main line) | **resolved** — all 4 platforms (ChatGPT/Claude/NotebookLM/Gemini) finished the v3/v9 clean rewrite; Gemini v9 gains a Method label anchor (Phase A main body + 2026-05-22 increment); only Gemini sanity testing has stopped (see §0.A) |
| Full 437 UNSOURCED_MANUAL classification | **partially resolved** — heuristic bias fix + N=80 sampling done; the per-atom full 437 review still defers to v1.5 |
| Tier B sections 11-25 + all level-2 (~156 sections) | **defer to v1.5** — scope exceeds v1.4 (~5-7 working days for a standalone KB pass cycle); will ship as an independent release |
| Issue 5 §6.3.5.9.3 PC/PP 143 TABLE_ROW Tier-B MEDIUM repair | **defer to v1.5** — see 06 Deep Verification §二; folded in with the Tier B full sweep |
| section_coverage.jsonl full pipeline rerun | **partially resolved** — P4b deterministic portion done (C1); full LLM pipeline rerun (C1-bis) defers to v1.5 |
| R4 full 17-question Gemini Pro regression | **N/A — Gemini sanity testing has stopped** (Pro quota constraint + tests stop; optimization continues) |
| PASS+ §1.2 strict "AHP-only" scope expansion | **acknowledged** — the expanded definition (KB-grounding + above-baseline depth = PASS+) continues to apply in v1.4 sanity; future smoke design will formally incorporate it |

### 0.D. v1.4 items not done (deferred to v1.5+)

- **Tier B 156 sections** (Batch H ranks 1-10 ~470 atoms + Batch S 21-25 ~10 atoms + 24 level-2 sections ~600 atoms) — scope exceeds v1.4; standalone KB pass cycle.
- **Per-atom full 437 UNSOURCED_MANUAL classification** — v1.4 ships only the heuristic fix + N=80 sample; the full-precision pass defers to v1.5.
- **Phase 7 RAG + KG kickoff** — not economical to run in parallel with the prompt refactor; standalone phase (design already complete in `docs/DESIGN_RAG_KG.md`).
- **C1-bis full LLM pipeline rerun** — P2 increment + P4a forward matcher (the deterministic portion landed in C1).
- **C2 KB_INTERNAL_CROSSREF new classification category** — the 5 NEEDS_HUMAN_REVIEW atoms from the N=80 sample expose the need for a new category beyond the current 4-class classifier.
- **C2 3 deep-paraphrase atoms manual review** — N=80 carry (3 of the 5 NEEDS_HUMAN_REVIEW atoms are deep paraphrases pending human judgment).
- **C3 NotebookLM screenshot tutorial (Chrome MCP)** — v1.4 DEPLOY_GUIDE has a text-level reminder + skeleton; screenshot capture defers to the next sprint.

### 0.E. Cosmetic / deployment notes

- **Gemini users**: v1.4 ships a Gemini gem delta (system_prompt v9 clean rewrite + Method label anchor + KB delta). However this platform has **no sanity test coverage** — please self-verify answer correctness. For high-correctness use cases, prefer ChatGPT / Claude / NotebookLM (this release has sanity coverage for these three).
- **NotebookLM bucket 25** (v1.3 carry, v1.4 tutorial strengthening): if your existing v1.0–v1.3 NotebookLM deployment still contains the old source `25_td_meta_ti_ts_oi.md`, after uploading `25_td_meta_ti_ts_oi_di.md` **please manually delete the old source** (43 → 42 once cleaned). v1.4 `.work/07_release_v1_4/V1_4_DEPLOY_GUIDE.md` carries a prominent reminder (screenshot tutorial deferred to v1.5).
- **ChatGPT PP RELREC Method label**: v1.4 KB + prompt dual-layer anchor now covers this (C4 resolved); the v1.3 PARTIAL drift should be resolved (sanity recheck deferred to user grep-level verification).

## 1. Not a Replacement for Official Standards

SDTM Pedia is a reference aid. Regulatory submission decisions, standards interpretation, terminology version confirmation, and critical mapping decisions should use CDISC publications, NCI EVS, licensed MedDRA resources, regulatory requirements, and internal SOPs.

## 2. Real-Time External Updates Are Not Guaranteed

This release reflects the knowledge scope prepared at release time. For later changes, such as new CDISC versions, Pinnacle 21 rule updates, Dataset-JSON status, or external database changes, check the relevant official source.

## 3. Long-Tail Terminology May Require Official Lookup

Some very large codelists and long-tail questionnaire terminology are not fully expanded on every platform. A good answer should state the boundary and point you back to NCI EVS or another authoritative source rather than generating an unverified full term list.

## 4. Platform Answer Styles Differ

Claude, ChatGPT, Gemini, and NotebookLM differ in style, citation display, and conservatism. NotebookLM tends to stay closest to the uploaded source set; other platforms may be better for explanation and synthesis, but still require human judgment.

## 5. Internal Organization Rules Are Not Covered

Sponsors, CROs, and data standards teams may have internal mapping conventions, Define-XML practices, Reviewers Guide wording, and quality workflows. SDTM Pedia can help with standards lookup, but it does not replace those conventions.

## 6. High-Risk Scenarios Require Human Review

Use human review for:

- Decisions affecting formal submission structure or variable mapping.
- Medical coding, serious adverse events, death, discontinuation, or other critical clinical concepts.
- Project-specific CRFs, SAPs, data management plans, or sponsor standards.
- Answers without clear support, or answers that conflict with team standards.

If you find an apparent error or gap, record the question, platform, answer, and expected source so maintainers can review it.
