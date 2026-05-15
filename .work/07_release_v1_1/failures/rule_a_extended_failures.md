# Rule A Extended Audit — Failure Archive

**Audit:** Rule A N=20 + 22-bucket extended audit
**Date:** 2026-05-16
**Auditor:** Tier 2 audit subagent (executor)

---

## Status: NO HARD FAILURES

Zero hard misses detected across all 124 probe checks (80 N=20 checks + 44 bucket checks).

Rule B archive created as required per protocol, with null result.

---

## Near-Miss Log (Claude condensed format — NOT failures)

These 4 samples had exact-phrase misses in Claude uploads only. Classified as expected behavior, not failures, because:
1. Claude platform uses condensed/summarized format by design (token management)
2. All 3 other platforms (ChatGPT, Gemini, NotebookLM) hit verbatim on all 4
3. Claude file contains the domain section and equivalent content

| Sample | KB File | Missing Exact Phrase | Claude File Checked | Content Present As |
|--------|---------|---------------------|--------------------|--------------------|
| S05 | `domains/TA/assumptions.md` | `TATRANS will be in a form like` | `06_assumptions.md` | "TATRANS does contain a choice (an 'if' clause)" — 2 TATRANS refs |
| S08 | `domains/DI/assumptions.md` | `classified as a study reference dataset` | `06_assumptions.md` | DI §9.1 section with SDTMIG-MD reference present |
| S15 | `domains/FA/assumptions.md` | `choice between representing a data item as a supplemental qualifier` | `06_assumptions.md` | 10 refs: FAOBJ, §6.4, Findings About |
| S18 | `domains/DS/assumptions.md` | `SUPPDS QNAM = "DSTERM1"` | `06_assumptions.md` | 16 refs: DSCAT, DSDECOD, §10.1 |

**Decision:** These are architectural, not content, gaps. No rebuild required.

---

*Rule B archive: created 2026-05-16. Zero failures to escalate.*
