---
lang: en
slug: changelog
order: 60
title: "Changelog"
---

# SDTM Knowledge Base — Release v1.4 Changelog (EN)

> Tag: `v1.4-company-release` (cut 2026-05-22)
> Previous tag: `v1.3-company-release` (2026-05-20)
> Driver: Prompt full-stack refactor — 4-platform v3/v9 clean rewrite (fossil-layer removal + KB-grounding default) + 4 minor v1.3 carries (C1-C4) + Claude bundle pipeline architectural fix. Gemini MAINTAINED_NO_SANITY_TEST per user 2026-05-22 decision.

## Summary

v1.4 is a **prompt-pass-level** release of SDTM Pedia — the three maintained AI platforms (ChatGPT GPTs, Claude Projects, NotebookLM) receive a full-stack clean rewrite of their system prompts / instructions, stripping the v1.0-v1.3 iteration fossil layers and restoring KB-grounding as the primary path. The Gemini Gems platform shifts to "maintained-but-no-sanity-test" mode from v1.4 (per user decision 2026-05-22). Four v1.3 minor carries (C1-C4) fold in. A Claude bundle pipeline architectural fix repairs the §N.N.N capture gap (a Phase 6.5 reorg-A path regression caught during the C4 rebuild).

## v1.4 (2026-05-22) — Prompt pass + Minor carries + Pipeline fix

**Type**: prompt-pass + minor carries (vs v1.3 KB-pass; the main work sits in the prompt layer; only 1 KB file changed)

### Prompt changes (4-platform system_prompt / instructions)

Driver: v1.3 RETRO §二 8-carry list — the main carry is the 4-platform prompt full-stack refactor (Gemini v8.1 525 lines contains 17 CO-N fossil rules + parallel accumulation in the other 3 platforms). v1.4 main carry is fossil removal + KB-grounding first.

- **ChatGPT v3 system_prompt** (`self_deploy/chatgpt/system_prompt.md`): 120→119 lines + a 4-line Method label anchor mapping (L77-80). Removes v1.0-v1.3 iteration annotations, makes KB-grounding the default. A=Many-Many (PCGRPID/PPGRPID) / B=One-Many (PCSEQ/PPGRPID) / C=Many-One (PCGRPID/PPSEQ) / D=One-One (PCSEQ/PPSEQ).
- **Claude v3 system_prompt** (`self_deploy/claude/system_prompt.md`): 125→133 lines. 5 essential rules + regex-gated CO-N + the Files A-S 19-file table preserved in full (critic reviewer caught attempt 1's truncated 19→7 file table → attempt 2 surgical fix landed PASS_WITH_OBSERVATIONS).
- **NotebookLM v3 instructions** (`self_deploy/notebooklm/instructions.md`): 157→156 lines. Footer Sources citation kept semantically equivalent (not byte-exact; behavior preserved). v1.0-v1.3 iteration fossils removed.
- **Gemini v9 system_prompt** (`self_deploy/gemini/system_prompt.md`): 525→292 lines (including the 2026-05-22 Method label anchor increment). **MAINTAINED_NO_SANITY_TEST** — optimization continues, testing stops (see KNOWN_LIMITATIONS §0.A).

### KB changes (1 file modified)

- **PP/examples.md** — §6.3.5.9.3 gains a 13-line explicit Method label mapping table (A/B/C/D × IDVAR1+IDVAR2 in 4 rows + header). KB + prompt dual-layer anchor resolving the v1.3 Q-S2 ChatGPT PARTIAL label drift (C4).

### Platform bundle changes

- **chatgpt**: `06_domain_examples_all.md` rebuilt (now contains the PP/examples §6.3.5.9.3 Method label table); manifest updated.
- **claude**: `09_examples_data_high.md` rebuilt (2922→3268 lines, A3.1 §N.N.N capture working for the first time post the pipeline fix). Includes the Method label table + 3 newly captured §N.N.N segments.
- **notebooklm**: bucket 16 (`16_fnd_pharma_pc_pp.md`) rebuilt (includes the Method label table).
- **gemini**: bundle delta syncs the KB change (gem auto-pulls via KB grounding).

### Pipeline / build script fixes (critical)

- **`ai_platforms/claude_projects/dev/scripts/extract_examples_data.py`** parents[3]→parents[4] path bugfix: a Phase 6.5 reorg-A path regression (the script moved one level deeper, but the parents[] index did not move with it). Impact: all 28 domains were reported missing; the A3.1 smoke test missed it because it ran from a different working config (smoke in dev/, production path different). Triggered in real combat during the C4 rebuild → fix → 3 bundles rebuilt successfully + 3268-line examples bundle (with §N.N.N capture).

### Verification

- **B1 UI sanity** (Chrome MCP fire-and-forget): 4 questions × 3 platforms = 12 cells = **10 PASS+ + 2 PASS + 0 PARTIAL + 0 FAIL = 100% PASS** (Gemini 4 cells excluded per §0.A).
  - Q-S1 BECAT EXTRACTION: 3/3 PASS
  - Q-S2 PP RELREC Method (v1.3→v1.4 main trigger): 3/3 PASS+ (Claude paper PARTIAL → UI PASS+ post A3.1 pipeline fix)
  - Q-S3 TR TRSTRESN/TRSTRESU typo: 3/3 PASS
  - Q-S4 DI domain (NotebookLM bucket 25): 3/3 PASS
- **B2 R4 17-question full regression** (Gemini-only scope originally): **N/A** — Gemini sanity testing has stopped (see §0.A; optimization continues, testing does not).
- **Q-S2 post-rebuild sanity recheck**: SKIPPED per user (grep-level content verification deemed sufficient).
- **C2 UNSOURCED N=80 sampling**: 75 RI + 0 XLSX + 0 HALLUCINATED + 5 NEEDS_REVIEW (cumulative N=80; v1.3 N=40 HIGH + v1.4 +40 LOW; HIGH pool was exhausted in v1.3).
- **C1 section_coverage**: P4b deterministic rerun done — FULL_COVERAGE 101→137, SKELETON 67→46. md_atoms remain in their pre-v1.3 state (LLM pipeline rerun deferred to v1.5 as C1-bis).

### Known issues (deferred to v1.5 — see KNOWN_LIMITATIONS §0)

- **C1-bis full pipeline LLM rerun**: P2 increment + P4a forward matcher + P4b (the deterministic portion landed in C1).
- **C1-ter post-P6 Makefile gate**: section_coverage stability gate.
- **C2 KB_INTERNAL_CROSSREF new classification category**: the N=80 sample exposes the need for a new category beyond the current 4-class classifier.
- **C2 3 deep-paraphrase atoms manual review**: 3 of the 5 NEEDS_HUMAN_REVIEW atoms are deep paraphrases pending human judgment.
- **C3 NotebookLM screenshot tutorial (Chrome MCP)**: v1.4 DEPLOY_GUIDE carries a text-level reminder; screenshot capture deferred.
- **Tier B 156 sections + full 437 UNSOURCED + Phase 7 RAG+KG**: all carries from v1.3 §二.

### Migration from v1.3 → v1.4

For self-hosting users:

1. **3 sanity-covered platforms (ChatGPT / Claude / NotebookLM)**: replace the platform's system prompt with `self_deploy/<platform>/system_prompt.md` (or `instructions.md`); replace uploads with the corresponding bundle files in `self_deploy/<platform>/uploads/`. Step-by-step in `.work/07_release_v1_4/V1_4_DEPLOY_GUIDE.md`.
2. **Gemini**: user self-verify. v1.4 ships a v9 system_prompt + Method label anchor + KB delta increment, but this platform has **no sanity test coverage** — please self-verify answer correctness; for high-correctness use cases prefer the other 3 platforms.
3. **NotebookLM bucket 25** (v1.3 carry): if your existing deployment still contains the old source `25_td_meta_ti_ts_oi.md`, after uploading `25_td_meta_ti_ts_oi_di.md` **please manually delete the old source** (43 → 42). v1.4 DEPLOY_GUIDE carries a prominent reminder.

**Tag**: `v1.4-company-release`

---

# SDTM Knowledge Base — Release v1.3 Changelog (EN)

> Tag: `v1.3-company-release` (cut 2026-05-20)
> Previous tag: `v1.2-company-release` (2026-05-19)
> Driver: KB pass — PP RELREC OA-4 gap + BECAT extraction prompt-KB drift + Tier B partial repair + 4-platform rebuild + light sanity 14-15/16 PASS

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
