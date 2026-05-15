# Claude Projects Rebuild — Failures / Skips Log (Rule B)

> Date: 2026-05-15
> Rule B: 失败数据归档，含输入/产物/技术判定/业务判定/下一 attempt 输入

---

## F1 — 05_mega_spec.md: DI domain skipped (no spec.md)

**Input**: archive/v1/scripts/merge_specs.py, 64 domains (63 original + DI)
**Artifact produced**: output/05_mega_spec.md — 63 domains, 1,917 variables (DI excluded)
**Technical judgment**: EXPECTED — DI added in 06 has only assumptions.md. No spec.md exists.
**Business judgment**: ACCEPTABLE — DI variable specs not in KB. 63-domain mega_spec is correct.
**Next attempt**: If DI/spec.md is ever added, re-run merge_specs.py with DI in DOMAINS.

---

## F2 — 07_examples_catalog.md: DI domain skipped (no examples.md)

**Input**: archive/v1/scripts/catalog_examples.py, 64 domains
**Artifact produced**: output/07_examples_catalog.md — 63 domains (DI warned+skipped)
**Technical judgment**: EXPECTED — DI has no examples.md.
**Business judgment**: ACCEPTABLE — Not a regression; baseline also had 63 domains.
**Next attempt**: If DI/examples.md is ever added, re-run catalog_examples.py.

---

## F3 — 09_examples_data_high.md: EXCEED_HARD_CAP (soft failure, file produced)

**Input**: dev/scripts/extract_examples_data.py --tier high, 28 domains
**What happened**: exit 1 (EXCEED_HARD_CAP: 104,548 > 50,000 tokens). File written.
**Artifact produced**: output_v2/09_examples_data_high.md — 104,548 tokens, complete
**Technical judgment**: PRE-EXISTING CAP-WARNING — same behavior as original v2.2 build.
  Per build_v2_stage.py: "rc=1 with output present accepted as soft-pass / cap-warning outcome"
**Business judgment**: ACCEPTABLE — File is complete (28 domains, 0 missing). Pre-existing condition.
**Next attempt**: If cap must be resolved, split high tier into 09a/09b (14+14 domains).

---

## F4 — Script path resolution bugs (infrastructure)

**What happened**: All v1/v2 scripts use wrong parents[N] for REPO_ROOT detection.
  - archive/v1/scripts/ (5 levels): parents[3] = ai_platforms/claude_projects/ (wrong)
  - dev/scripts/ (4 levels): parents[3] = ai_platforms/ (wrong)
**Workaround**: Used inline patching of REPO_ROOT string before exec(). All builds succeeded.
**Technical judgment**: BUG — parents[N] depth incorrect for moved/archived script locations.
**Business judgment**: LOW PRIORITY — Only affects internal build runner. Workaround is stable.
**Next attempt**: Fix parents[N] in each script to correct depth, or add REPO_ROOT env-var override.
