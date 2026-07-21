# SDTM Knowledge Base — Release v1.2 Changelog (EN)

> Tag: `v1.2-company-release` (cut 2026-05-19)
> Previous tag: `v1.1-company-release` (2026-05-15)
> Driver: SMOKE_V4 R3 (2026-05-19) regression on Gemini v7.1 → v8.1 system prompt fix

## Summary

v1.2 is a **Gemini-only system prompt refresh** of v1.1. The knowledge base, all four AI-platform upload bundles, all metadata documents, and three of the four platform system prompts (Claude / ChatGPT / NotebookLM) are unchanged from v1.1. **Only `self_deploy/gemini/system_prompt.md` has been replaced** (v7.1 → v8.1, 422 → 525 lines, +24%).

## Driver: SMOKE_V4 R3 regression on Gemini

After deploying v1.1 to the four AI platforms, a full regression test (SMOKE_V4 R3) was run on 2026-05-19. Three of four platforms held their R1 baseline:

- **Claude v2.6**: 17/17 (sustained)
- **ChatGPT v2.2**: 17/17 (slight improvement over R1)
- **NotebookLM v2**: 15.5/17 (RAG architectural limits on Q9 PUNT and Q11 PARTIAL — both expected)
- **Gemini v7.1**: **13/17 (4 FAIL)** — regression vs R1 16/17

The four Gemini failures:

| # | Topic | v7.1 failure mode |
|---|---|---|
| Q3 | BE / BS / RELSPEC (biospecimen handling) | Off-topic response on AE / AESEV / AEGRPID (1,541 chars) |
| Q4 Scenario A | Anti-measles IgG titer | Routed to LB instead of IS (regression of R2 fix) |
| Q11 | Dataset-JSON v1.1 vs XPT v5 | Off-topic response on AE / CM (1,436 chars) |
| AHP1 | LBCLINSIG variable hallucination probe | Off-topic response on CM polypharmacy / MH (1,485 chars) |

Independent reviewer (`oh-my-claudecode:scientist`, Rule D #15) confirmed the matrix and identified four anchor coverage gaps in v7.1:

1. **Q3** — No biospecimen-keyword entry guard, so Gemini fell back to high-frequency SDTM domains (AE / CM).
2. **Q4 A** — No sticky anchor for the v3.3 → v3.4 IS scope shift; the R2 fix decayed.
3. **Q11** — No file-format ground rule; Gemini substituted SDTM domain content for the file-format question.
4. **AHP1** — Anti-hallucination anchor only fired when the question contained a reflection scaffold; plain factual probes missed.

## What changed in v8.1

### 4-prong fix

- **CO-4 entry guard (NEW)**: When the question contains biospecimen keywords (13 Chinese / English patterns), anchor the response to BE / BS / RELSPEC and forbid the AE / CM fallback path.
- **CO-2f file-format ground rule (NEW)**: When the question is about XPT / Dataset-JSON / Define-XML / submission format, ground the response in CDISC published specifications. Includes an end-of-response off-topic guard.
- **CO-1e IS scope shift v3.3 → v3.4 (NEW)**: Anti-microbial antibody assessments (measles / HBsAb / HCV / COVID / ADA, regardless of timing) belong to IS, not LB or MB. HIV Ag / Ab combination assays exception → MB (per KB IS Assumption 5). ISTSTOPO three-layer structure under IS Assumption 8.
- **CO-5 default reflection (MOD)**: Any token matching SDTM-shaped regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` triggers a mandatory KB double-check independent of question phrasing. If the token is not in the KB, the AHP-V1 dismissal template fires. A negation list and a CO-2f priority gate prevent over-triggering.

### 6 reviewer-driven refinements (Rule D #16 PASS_WITH_OBSERVATIONS reconcile)

- **H1**: HIV Ag / Ab combination → MB, not LB (KB IS Assumption 5).
- **H2**: CO-2f file-format anchor takes priority over CO-5 regex variable-hallucination path.
- **M1**: Regex negation list — common non-SDTM acronyms (`FDA`, `CDISC`, `XPT`, `JSON`, etc.) and SDTM domain abbreviations skip the KB double-check.
- **M2**: When more than five candidate identifiers appear, only the explicitly named 3-5 run the double-check.
- **L1**: ISTSTOPO correctly cited as IS Assumption 8 (was previously labeled Assumption 7a).
- **L2**: BECAT example `"EXTRACTION"` annotated as sponsor-extensible (KB BE / spec only inlines COLLECTION / PREPARATION / TRANSPORT).

## Dry-run verification (Gemini 3.1 Pro, 2026-05-19 16:35-16:40 PM)

The four v7.1 failure questions were re-tested on Gemini 3.1 Pro (same model as the R3 baseline) immediately after the Pro quota reset. All four are PASS:

| # | v7.1 R3 | v8.1 dry-run | Prong + Fix verified |
|---|---|---|---|
| Q3 | FAIL (AE off-topic) | PASS (1,439 chars, 47.6s) | Prong 1 + L2 |
| Q4 | FAIL (A = LB) | PASS (1,763 chars, 52.7s) | Prong 3 + H1 + L1 |
| Q11 | FAIL (AE/CM off-topic) | PASS (3,768 chars, 30.6s) | Prong 2 + H2 |
| AHP1 | FAIL (CM/MH off-topic) | PASS (694 chars, 46.6s) | Prong 4 + M1 — 7/7 AHP-V1 elements fired |

An independent Rule D #17 reviewer (`oh-my-claudecode:verifier`) confirmed all four PASS verdicts against the KB sources and approved promotion with no blockers.

## Per-platform bundle changes

### Gemini Gems (`self_deploy/gemini/`)

- **system_prompt.md**: replaced (v7.1 → v8.1, 422 → 525 lines).
- **uploads/*.md**: **unchanged** (byte-identical inherit from v1.1; KB has not been modified since v1.1).
- **tutorial.{en,zh,ja}.md**: unchanged.

### Claude Projects / ChatGPT GPTs / NotebookLM

- All files byte-identical inherit from v1.1. No KB rebuild and no prompt change.

## Unchanged from v1.1

- All knowledge base content (`knowledge_base/` is identical to v1.1).
- All upload bundles for all four platforms.
- All metadata documents (`METHODOLOGY`, `USER_GUIDE`, `PLATFORM_COMPARISON`, `DEMO_QUESTIONS`, `GLOSSARY`, `README` in en/zh/ja).
- System prompts and tutorials for Claude, ChatGPT, NotebookLM.

## Verification

- v8.1 dry-run: 4 / 4 PASS on Gemini 3.1 Pro (same model as R3 baseline).
- Rule D writer-side reviewer (`pr-review-toolkit:code-reviewer`, #16): PASS_WITH_OBSERVATIONS with six reconcile fixes applied.
- Rule D dry-run-side reviewer (`oh-my-claudecode:verifier`, #17): PASS_WITH_OBSERVATIONS — APPROVE with no blockers.
- Full audit evidence: `ai_platforms/gemini_gems/dev/v8_draft/dry_run_2026-05-19/` (4 question evidence + verdict + reviewer audit).

## Known caveats (deferred to post-v1.2)

- **R4 17-question full regression**: only the four v7.1 FAIL questions were re-tested; the 13 v7.1 PASS questions were not. The CO-5 default-reflection regex and candidate-count cap are not yet independently validated on multi-variable questions. Planned for v1.2 post-cut.
- **BECAT EXTRACTION KB-prompt note**: v8.1 prompt L272 lists `"EXTRACTION"` among BECAT examples; KB BE / spec L111 only inlines three canonical examples. The response correctly annotates it as sponsor-extensible, but a future prompt revision may add an explicit source citation.
- **M2 candidate-count cap**: not independently exercised in the four-question dry-run; the test set had fewer than five candidates per question. Planned for R4 multi-variable question coverage.

## Migration from v1.1 → v1.2

For self-hosting users:

1. Replace the Gemini Gem system instructions with `self_deploy/gemini/system_prompt.md` (525 lines).
2. **No other action required.** Upload bundles, other platform prompts, tutorials, and metadata documents are unchanged.
3. Existing Gemini Gem chat sessions will use the new prompt automatically on the next message.
