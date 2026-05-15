# SDTM Knowledge Base — Release v1.1 Changelog (EN)

> Tag: `v1.1-company-release` (cut 2026-05-15)
> Previous tag: `v1.0-company-release` (2026-04-27)
> Driver: Incorporate `06_deep_verification` branch fixes (closed 2026-05-12)

## Summary

v1.1 is a content refresh of the v1.0 company release. The methodology, system prompts, tutorials, glossary, demo questions, and platform comparison documents are unchanged. **Only the four AI-platform upload bundles (`self_deploy/*/uploads/`) have been rebuilt** from the post-06-verification `knowledge_base/`.

## What changed in the knowledge base (sources of this release)

The `06_deep_verification` side-branch performed atom-level audit and repair of the knowledge base. Net effect on `knowledge_base/`: **43 files modified, +1,405 / -234 lines**.

Highlights:

- **New domain added: DI (Device Identifiers, SDTMIG-MD)** — a study reference dataset for medical devices. KB now covers **64 domains** (was 63).
- **PC/assumptions.md** — added §6.3.5.9 "Relating PP Records to PC Records" (RELREC) section, including 4 methods (A/B/C/D) for linking PC and PP records (+118 lines).
- **TA/assumptions.md** — substantially extended (+175 lines).
- **chapters/{ch02_fundamentals, ch04_general_assumptions, ch08_relationships, ch10_appendices}** — content strengthening per atom-level coverage audit.
- **TI / TS / TU / TV / SC / NV / TV examples / others** — section-level gaps filled (P6 T4 Tier A repair).
- Coverage rate post-repair: **99.02%** (adjusted denominator); 0 hallucinated atoms.

Full retrospective: `branches/06_deep_verification/RETROSPECTIVE.md`.

## Per-platform bundle changes

### Claude Projects (`self_deploy/claude/uploads/`)

19 files. Refreshed bundles incorporating 06 fixes:
- `02_chapters.md` — full chapters re-extracted
- `05_mega_spec.md` — 64 domain specs (DI has no spec, retains 63)
- `06_assumptions.md` — 64 domain assumptions (includes new DI)
- `07_examples_catalog.md` — examples catalog (PC RELREC examples added)
- `09_examples_data_high.md` + `10_examples_data_others.md` — example tables refreshed
- `03_model.md` — model refresh (observation_classes touched)

Unchanged: `00_routing.md`, `01_index.md`, `04_variable_index.md`, `08_terminology_map.md`, `11/12/13` terminology bundles.

### ChatGPT GPTs (`self_deploy/chatgpt/uploads/`)

9 files. Refreshed:
- `02_chapters_all.md` (+12.4 KB)
- `03_model_all.md` (small refresh)
- `05_domain_assumptions_all.md` (+74.2 KB — DI added, 64 segments)
- `06_domain_examples_all.md` (+18.5 KB — PC RELREC etc.)

Unchanged: `01_navigation.md`, `04_domain_specs_all.md`, `07/08/09` terminology.

### Gemini Gems (`self_deploy/gemini/uploads/`)

3 KB-derived files (the 4th file `04_business_scenarios_and_cross_domain.md` is writer-authored and unchanged). All 3 refreshed:
- `01_navigation_and_quick_reference.md` (+13.9 KB — chapters/model/indexes)
- `02_domains_spec_and_assumptions.md` (+74.2 KB — DI added)
- `03_domains_examples.md` (+18.5 KB — PC RELREC etc.)

### NotebookLM (`self_deploy/notebooklm/uploads/`)

42 buckets. **22 buckets refreshed** (all buckets containing 06-touched KB files):
- `03_sp_demographics_subject`, `04_sp_se_sm_sv_co`, `06_int_concomitant_cm_ag_ml`,
- `09_ev_disposition_ds_dv_ce`, `10_ev_history_mh_ho_be`,
- `11_fnd_lab_lb`, `13_fnd_physical_exam_pe`, `15_fnd_biomarkers_mb_mi_ms_mk`,
- `16_fnd_pharma_pc_pp` (notable: PC §6.3.5.9 RELREC added),
- `17_fnd_oncology_tr_tu_rs_oe`, `21_fnd_other_nv_re_rp`,
- `25_td_meta_ti_ts_oi` (DI added — bucket renamed to include DI; SDTMIG-MD device identifier domain)

Total NotebookLM word count: 1,599,397 (was 1,599,332; +65 words from DI).

## Unchanged from v1.0

- All metadata documents: `METHODOLOGY.{en,zh,ja}.md`, `USER_GUIDE.{en,zh,ja}.md`, `KNOWN_LIMITATIONS.{en,zh,ja}.md`, `PLATFORM_COMPARISON.{en,zh,ja}.md`, `DEMO_QUESTIONS.{en,zh,ja}.md`, `GLOSSARY.{en,zh,ja}.md`, `README.{en,zh,ja}.md`.
- All system prompts and tutorials (`self_deploy/*/system_prompt.md`, `tutorial.{en,zh,ja}.md`).

## Verification

- Each platform rebuild was diffed against its v1.0 baseline; deltas match the scope of the 06 branch KB changes (see `.work/07_release_v1_1/evidence/diff_summary.md` in repo).
- A Rule D independent reviewer (subagent_type ≠ main session) approved the rebuild (see `.work/07_release_v1_1/evidence/rule_d_review.md` in repo).

## Migration from v1.0 → v1.1

For self-hosting users:
1. Re-upload `self_deploy/<platform>/uploads/*.md` to your deployed instance.
2. No changes needed to system prompts, tutorials, or other metadata.
3. Existing chat sessions on each platform will need re-indexing after the re-upload.
