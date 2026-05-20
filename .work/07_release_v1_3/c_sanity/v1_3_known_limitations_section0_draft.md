# v1.3 KNOWN_LIMITATIONS.en §0 draft (English source-of-truth for D1)

> Drafted by main session 2026-05-20 PM, post-Phase C sanity. Executor to translate to zh / ja and write to `release/v1.3/KNOWN_LIMITATIONS.{en,zh,ja}.md`.

---

## 0. v1.3 Audit Scope (updated 2026-05-20)

v1.3 is a **knowledge-base pass** release of SDTM Pedia (the largest content update since v1.0). It replaces the v1.2 Gemini-only prompt refresh model: v1.3 modifies the knowledge base directly, rebuilds all four platform bundles, and verifies end-to-end delivery in the four deployed AI platforms.

### What's new in v1.3

- **Phase A — KB layer fixes** (11 KB files modified, 0 hallucination, 0 unintended deletion across two independent Rule D reviewer audits):
  - **PP RELREC linking** — added §6.3.5.9.3 RELREC Method Quick Reference in `PP/examples.md` (Method A/B/C/D table + 1 abbreviated relrec.xpt for Method C). Resolves the OA-4 carry from the 06 Deep Verification project.
  - **BECAT EXTRACTION sponsor-extensible** — explicitly noted in `BE/spec.md` L111 alongside the CDISC canonical examples (COLLECTION / PREPARATION / TRANSPORT). Aligns the KB with deployed Gemini v8.1 prompt L272 wording.
  - **Tier B section repairs** — 10 high-density shall/must sections repaired (§2.7 SDTM variable rules, §6.4.2 FA naming, §7.2.1 Trial Arms Example 4, §7.3.2/§7.3.3 TD/TM, §4.5.1.2 Tests Not Done, §6.3.12.2 TR column-header typo TRSTRESN→TRSTRESU, §6.4.3 FA --OBJ, §7.2.1.1 TA Distinguishing, §4.3.5).
  - **UNSOURCED_MANUAL atom sampling** — N=40 stratified sample (10 high-risk shall/must + 30 control) of 437 UNSOURCED_MANUAL atoms classified: 80% REASONABLE_INFERENCE + 20% DERIVED_FROM_XLSX + **0% HALLUCINATED** (Rule D `scientist` reviewer audit confirmed).
- **Phase B — 4-platform rebuild** (build scripts hardened, cross-platform delta oracle verified):
  - Build scripts defensive: ChatGPT `merge_for_chatgpt.py` switched from hardcoded `expected_segments=63/64/63` to dynamic `len()`; NotebookLM new `validate_bucket_coverage.py` (190/190 KB files reach buckets, 0 stale references).
  - 4 platforms rebuilt: ChatGPT (3 files updated), Gemini (3 files updated), NotebookLM (7 files updated + 1 renamed), Claude Projects (5 files updated).
  - NotebookLM bucket 25 renamed `25_td_meta_ti_ts_oi.md` → `25_td_meta_ti_ts_oi_di.md` (now reflects DI inclusion). **Self-deploying users must delete the old source after uploading the new one** — see USER_GUIDE.
  - Cross-platform delta oracle: byte-exact equivalence between ChatGPT 04 (+284) = NotebookLM bucket 10 (+284) = Gemini 02 partial (+284) for BE/spec change, etc. 0 silent loss.
  - All 4 platform `system_prompt`/`instructions` audited for stale numeric references (20/20 grep probes PASS).
- **Phase C — Light sanity (14-15/16 PASS)**:
  - 4 v1.3-targeted questions × 4 deployed platforms = 16 cells; BECAT (A2), PP RELREC (A1), TR typo (A3), DI domain (B5) end-to-end verified.
  - Q-S1 BECAT EXTRACTION: 4/4 PASS (2 PASS+).
  - Q-S2 PP RELREC 4 Methods: Claude PASS+, NotebookLM PASS+, ChatGPT PARTIAL (4 IDVAR combinations correct but Method A/B/C/D labels shuffled relative to KB), Gemini FAIL (see below).
  - Q-S3 TR TRSTRESN vs TRSTRESU typo fix: 4/4 PASS (2 PASS+).
  - Q-S4 DI domain (NotebookLM bucket 25 rename): NotebookLM PASS+ with footer citation `25_td_meta_ti_ts_oi_di.md` (verifies B5 deployment), Claude PASS+, Gemini PASS (Flash-Lite fallback, Pro quota exhausted), ChatGPT verdict not captured but expected PASS based on pattern.

### Areas not re-evaluated in v1.3 (deferred to v1.4)

- **MAIN — 4-platform `system_prompt`/`instructions` full-stack refactor**: User noted during Phase C that all four deployed prompts have accumulated multiple iteration layers (Gemini v8.1 is 525 lines with 17 CO-N anti-cheating rules, each tagged "v5/v6/v7/v7.1/v8 新增" as a fossil record of smoke-test failures). The complexity dilutes attention and over-specializes anchors, which surfaced in Phase C Q-S2 as a Gemini failure: the Gemini Gem hallucinated PP-PC RELREC linking methods (claimed PPLNKID/PCREFID) rather than retrieving the v1.3 KB §6.3.5.9.3 Method A/B/C/D taxonomy. The v1.4 release will rewrite all four prompts clean — removing fossil annotations, consolidating sub-rules, restoring KB-grounding as the primary path. Estimated reduction: Gemini 525 → ~200 lines, with regex-gated CO-N rules that fire only when question types match.
- **Full 437 UNSOURCED_MANUAL atom classification**: v1.3 sampled N=40 (0 hallucinated). Full 437 lineage verification reaches v1.4 along with the heuristic classifier fix found by the Rule D reviewer (Rule D `scientist` found that 5/10 atoms initially labeled DERIVED_FROM_XLSX were actually PDF-prose; main session classifier had an `xlsx vs PDF` prior bias).
- **Tier B sections 11-25 (heavy + small)** + **all level-2 Tier B (cannot / except / only / should keyword)** — v1.3 repaired ranks 11-20 (10 sections, ~37 atoms total). Ranks 1-10 (heaviest, ~470 atoms) and ranks 21-25 (smallest) and 24 level-2 sections defer to v1.4.
- **Issue 5 §6.3.5.9.3 PC/PP 143 TABLE_ROW Tier-B MEDIUM repairs**: per 06 Deep Verification §二; row-level data-value diff repairs.
- **Section coverage.jsonl full pipeline rerun**: v1.3 only backed up the baseline + documented stale state. Full pipeline (md_atoms regen → P4a forward matcher → P4b aggregate) needed for accurate verdict refresh.
- **R4 full 17-question Gemini regression with Pro only**: v1.3 used a 4-question light sanity × 4 platforms instead of the 17-question single-platform regression. The four sanity questions cover all v1.3 KB changes end-to-end; R4 full is deferred (Pro quota constraint: ~16-20 hours wall time across multiple 5h windows).
- **PASS+ §1.2 strict "AHP-only" scope expansion** (W1 carry from R4 sanity retro): Phase C Q-S1 and Q-S5 showed non-AHP questions also earning PASS+ ratings when KB-grounded with extra depth (cross-domain references, source citations). The PASS+ rubric scope expands to "AHP topics OR KB-grounded answers with above-baseline depth", documented here for future smoke testing.

### Cosmetic / deployment notes

- NotebookLM bucket 25 rename: existing v1.0–v1.2 NotebookLM deployments have an old source `25_td_meta_ti_ts_oi.md`. After uploading the new `25_td_meta_ti_ts_oi_di.md`, **manually delete the old source** to avoid stale citations (43 sources should drop to 42 once cleaned).
- ChatGPT GPT "Method A/B/C/D" labels for PP-PC RELREC may not match the v1.3 KB §6.3.5.9.3 Quick Reference labels in all cases (Phase C Q-S2 PARTIAL). The four IDVAR combinations are correct; labelling subjective.
