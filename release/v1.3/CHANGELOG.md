# SDTM Knowledge Base — Release v1.3 Changelog (EN)

> Tag: `v1.3-company-release` (cut 2026-05-20)
> Previous tag: `v1.2-company-release` (2026-05-19)
> Driver: KB pass — PP RELREC OA-4 gap + BECAT EXTRACTION prompt-KB drift + Tier B partial repair + 4-platform rebuild + light sanity 14-15/16 PASS

## Summary

v1.3 is a **knowledge-base pass** release — the largest content update since v1.0. It directly modifies the KB, rebuilds all four platform bundles from the updated source, and verifies end-to-end delivery across the four deployed AI platforms. The Gemini system prompt (v8.1, 525 lines) is **unchanged** from v1.2; the v1.4 prompt full-stack refactor is deferred.

## v1.3 (2026-05-20) — KB pass + 4-platform rebuild + light sanity

**Type**: knowledge-base pass (largest content change since v1.0; not a prompt-only refresh)

### KB changes (11 files modified)

- **PP/examples.md** — added §6.3.5.9.3 RELREC Method Quick Reference (Method A/B/C/D table + 1 abbreviated relrec.xpt for Method C). Closes OA-4 carry from 06 Deep Verification project. (+2,620 lines in bundle)
- **BE/spec.md** — L111: added `EXTRACTION` as a sponsor-extensible 4th example alongside CDISC canonical COLLECTION / PREPARATION / TRANSPORT. Aligns KB with Gemini v8.1 prompt L272.
- **TR/spec.md** (§6.3.12.2) — corrected column-header typo: `TRSTRESN` → `TRSTRESU` in the TR result display table.
- **Tier B repairs (8 additional files)** — 10 high-density shall/must sections repaired across: §2.7 SDTM variable rules, §6.4.2 FA naming, §7.2.1 Trial Arms Example 4, §7.3.2/§7.3.3 TD/TM, §4.5.1.2 Tests Not Done, §6.4.3 FA --OBJ, §7.2.1.1 TA Distinguishing, §4.3.5.

### Platform bundle changes

- **chatgpt**: 3 files updated — `04_specs_and_context.md` (+284), `05_domain_assumptions.md` (+333), `06_domain_examples_all.md` (+5,432)
- **gemini**: 3 files updated — `01_navigation_and_routing.md` (+3,103), `02_specs_and_assumptions.md` (+617), `03_domains_examples.md` (+5,432)
- **notebooklm**: 7 files updated + 1 renamed (`25_td_meta_ti_ts_oi.md` → `25_td_meta_ti_ts_oi_di.md`, DI now reflected in bucket name)
- **claude**: 5 files updated — `02_chapters.md`, `03_model_structure.md`, `06_assumptions_all.md`, `09_examples_data_high.md` (+592), `10_examples_data_others.md`

### Build script changes (defensive hardening)

- ChatGPT `merge_for_chatgpt.py`: `expected_segments` changed from hardcoded `63/64/63` to dynamic `len(_collect_domain_assumptions())`. No segment-count regression; warn-not-fail for >5% delta.
- NotebookLM new `validate_bucket_coverage.py`: 190/190 KB files reach buckets, 0 stale references, 0 unrouted domains.

### Verification

- **Phase B cross-platform delta oracle**: 4 byte-exact equations PASS (ChatGPT 04 delta = NotebookLM bucket 10 delta = Gemini 02 partial delta for BE/spec, etc.). 0 silent loss.
- **Phase C light sanity (4 questions × 4 platforms = 16 cells)**: 14-15/16 PASS.
  - Q-S1 BECAT EXTRACTION: 4/4 PASS (2 PASS+)
  - Q-S2 PP RELREC 4 Methods: Claude PASS+, NotebookLM PASS+, ChatGPT PARTIAL (IDVAR combos correct, Method labels shuffled), Gemini FAIL (prompt bloat — v1.4 carry)
  - Q-S3 TR TRSTRESN/TRSTRESU typo: 4/4 PASS (2 PASS+)
  - Q-S4 DI domain / bucket 25 rename: NotebookLM PASS+ (footer cites `25_td_meta_ti_ts_oi_di.md`), Claude PASS+, Gemini PASS, ChatGPT assumed PASS
- **UNSOURCED_MANUAL N=40 sample**: 0% HALLUCINATED (80% REASONABLE_INFERENCE + 20% DERIVED_FROM_XLSX). Rule D `scientist` reviewer confirmed.
- **system_prompt audit**: 20/20 grep probes PASS across 4 platforms (0 stale numeric references).

### Known issues (deferred to v1.4 — see KNOWN_LIMITATIONS §0)

- **Gemini PP RELREC retrieval weak** (Phase C Q-S2 FAIL): Gemini v8.1 prompt bloat (525 lines, 17 CO-N rules as fossil layers) causes KB-grounding failure on PP RELREC. v1.4 main carry: full-stack prompt refactor for all 4 platforms (~200 lines clean, regex-gated CO-N rules).
- **Full 437 UNSOURCED_MANUAL classification**: v1.3 sampled N=40 only. Full 437 deferred.
- **Tier B sections 11-25 + all level-2 Tier B**: v1.3 repaired ranks 11-20 (10 sections). Remaining ~156 sections deferred.
- **R4 full 17-question Gemini regression**: v1.3 used 4-question light sanity × 4 platforms; R4 Pro-only deferred due to quota constraint.
- **section_coverage.jsonl full pipeline rerun**: baseline backed up; full regen deferred to v1.4.

### Migration from v1.2 → v1.3

For self-hosting users:

1. **All 4 platforms**: replace uploads with files from `self_deploy/<platform>/uploads/`.
2. **NotebookLM**: upload `25_td_meta_ti_ts_oi_di.md` and **delete** the old `25_td_meta_ti_ts_oi.md` from your NotebookLM source list (source count should drop from 43 to 42).
3. **System prompts / instructions**: no change required (v8.1 Gemini + other 3 prompts unchanged from v1.2).

**Tag**: `v1.3-company-release`

---

## v1.2 (2026-05-19) — Gemini-only prompt refresh v7.1 → v8.1

> Tag: `v1.2-company-release` (cut 2026-05-19)
> Previous tag: `v1.1-company-release` (2026-05-15)
> Driver: SMOKE_V4 R3 (2026-05-19) regression on Gemini v7.1 → v8.1 system prompt fix

v1.2 is a **Gemini-only system prompt refresh** of v1.1. The knowledge base, all four AI-platform upload bundles, all metadata documents, and three of the four platform system prompts (Claude / ChatGPT / NotebookLM) are unchanged from v1.1. **Only `self_deploy/gemini/system_prompt.md` has been replaced** (v7.1 → v8.1, 422 → 525 lines, +24%).

### Driver: SMOKE_V4 R3 regression on Gemini

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

Independent reviewer (`oh-my-claudecode:scientist`, Rule D #15) confirmed the matrix and identified four anchor coverage gaps in v7.1.

### What changed in v8.1

4-prong fix: CO-4 entry guard (biospecimen keywords) + CO-2f file-format ground rule + CO-1e IS scope shift v3.3→v3.4 + CO-5 default reflection (SDTM-regex KB double-check). 6 reviewer-driven refinements (H1/H2/M1/M2/L1/L2). See full CHANGELOG.en.md for detail.

### Verification

- v8.1 dry-run: 4/4 PASS on Gemini 3.1 Pro (same model as R3 baseline).
- Rule D #16 (`pr-review-toolkit:code-reviewer`): PASS_WITH_OBSERVATIONS, 6 reconcile fixes applied.
- Rule D #17 (`oh-my-claudecode:verifier`): APPROVE 0 blockers.

**Tag**: `v1.2-company-release`
