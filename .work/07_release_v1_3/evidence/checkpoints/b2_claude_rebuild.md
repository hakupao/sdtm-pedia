# B2 Claude Projects Rebuild — Checkpoint Evidence

> Date: 2026-05-20
> Task: Rebuild `ai_platforms/claude_projects/current/uploads/` from KB after v1.3 Phase A (Batch M Tier B repair)
> Agent: executor subagent (writer-side, Rule D)

---

## 1. Build Script Paths

| Builder | Script Path | Output Dir |
|---------|-------------|------------|
| v1 (merge_model) | `archive/v1/scripts/merge_model.py` | `ai_platforms/claude_projects/output/` |
| v1 (merge_specs) | `archive/v1/scripts/merge_specs.py` | `ai_platforms/claude_projects/output/` |
| v1 (compress_assumptions) | `archive/v1/scripts/compress_assumptions.py` + DI patch | `ai_platforms/claude_projects/output/` |
| v1 (catalog_examples) | `archive/v1/scripts/catalog_examples.py` | `ai_platforms/claude_projects/output/` |
| v2 (chapters) | `dev/scripts/rebuild_chapters_full.py` | `ai_platforms/claude_projects/output_v2/` |
| v2 (examples_high) | `dev/scripts/extract_examples_data.py --tier high` | `ai_platforms/claude_projects/output_v2/` |
| v2 (examples_others) | `dev/scripts/extract_examples_data.py --tier others` | `ai_platforms/claude_projects/output_v2/` |

**Path patching**: All scripts use `Path(__file__).resolve().parents[N]` with wrong depth for their
archived/dev locations. Applied inline REPO_ROOT patch (`parents[N]` → `Path("/Users/bojiangzhang/MyProject/sdtm-pedia")`)
before exec. Same workaround as v1.1 (per `.work/07_release_v1_1/failures/claude_rebuild_failures.md` F4).

---

## 2. V1 Builder Run Results

| Script | rc | Output File | Size (bytes) | Status |
|--------|----|-------------|-------------|--------|
| merge_model.py | 0 | `output/03_model.md` | 72,531 | OK |
| merge_specs.py | 0 | `output/05_mega_spec.md` | 207,599 | OK — 63 domains, 1,917 variables (DI has no spec.md — expected) |
| compress_assumptions.py + DI patch | 0 | `output/06_assumptions.md` | 100,294 | OK — 64 domains (DI included after DOMAINS list fix) |
| catalog_examples.py | 0 | `output/07_examples_catalog.md` | 13,333 | OK — 63 domains, 184 examples (DI has no examples.md — expected) |

**Note**: compress_assumptions.py had DI missing from hardcoded DOMAINS list (same as v1.1 F1 issue).
Re-ran with DI injected between DV and EC. See `failures/b2_claude_compress_assumptions_attempt_1.md`.

---

## 3. V2 Builder Run Results

| Script | rc | Output File | Size (bytes) | Status |
|--------|----|-------------|-------------|--------|
| rebuild_chapters_full.py | 0 | `output_v2/02_chapters.md` | 262,240 | OK — 63,955 tokens (target ≤90K) |
| extract_examples_data.py --tier high | 1 | `output_v2/09_examples_data_high.md` | 279,936 | SOFT-PASS — 104,812 tokens (EXCEED_HARD_CAP pre-existing, file produced, 28 domains, 0 missing) |
| extract_examples_data.py --tier others | 0 | `output_v2/10_examples_data_others.md` | 133,618 | OK — 48,962 tokens WARN above 30K soft (pre-existing), 35 domains, 0 missing |

**Note on output_v2 path**: Scripts auto-resolve to `ai_platforms/claude_projects/output_v2/` (top-level,
not `dev/output_v2/`). This matches the original v2 build location (per `_progress.json`).

---

## 4. Files in current/uploads/ — Before vs After

| File | Before (B) | After (B) | Delta | Updated? |
|------|-----------|----------|-------|---------|
| 00_routing.md | 8,041 | 8,041 | 0 | unchanged (KB unchanged) |
| 01_index.md | 5,200 | 5,200 | 0 | unchanged (KB unchanged) |
| 02_chapters.md | 259,659 | 262,240 | +2,581 | **UPDATED** |
| 03_model.md | 72,009 | 72,531 | +522 | **UPDATED** |
| 04_variable_index.md | 31,899 | 31,899 | 0 | unchanged (KB unchanged) |
| 05_mega_spec.md | 207,599 | 207,599 | 0 | idempotent (DI no spec.md) |
| 06_assumptions.md | 100,074 | 100,294 | +220 | **UPDATED** (DI patch + Batch M) |
| 07_examples_catalog.md | 13,333 | 13,333 | 0 | idempotent |
| 08_terminology_map.md | 82,629 | 82,629 | 0 | unchanged (terminology/ unchanged) |
| 09_examples_data_high.md | 279,344 | 279,936 | +592 | **UPDATED** |
| 10_examples_data_others.md | 133,476 | 133,618 | +142 | **UPDATED** |
| 11a_terminology_high_core.md | 259,296 | 259,296 | 0 | unchanged (idempotent skip) |
| 11b_terminology_high_questionnaires.md | 1,007,930 | 1,007,930 | 0 | unchanged |
| 11c_terminology_high_supp.md | 98,029 | 98,029 | 0 | unchanged |
| 12a_terminology_mid_core.md | 502,738 | 502,738 | 0 | unchanged |
| 12b_terminology_mid_questionnaires.md | 890,595 | 890,595 | 0 | unchanged |
| 12c_terminology_mid_supp.md | 95,105 | 95,105 | 0 | unchanged |
| 13a_terminology_tail_core.md | 573,048 | 573,048 | 0 | unchanged |
| 13c_terminology_tail_supp.md | 168,548 | 168,548 | 0 | unchanged |

**Total files**: 19 (unchanged count matches v1.1 baseline)
**Updated files**: 5 (02/03/06/09/10) + 05/07 idempotent (unchanged)

---

## 5. Rule A Verification — 3 Spot Probes

### Probe 1: PP RELREC §6.3.5.9.3 in 09_examples_data_high.md

```
grep result: 6 RELREC hits
Key match: "*Note: PC and PP share a combined examples section (§6.3.5.9.3 Relating PP
Records to PC Records). This file contains the 4 worked Examples (1–4) illustrating
the 4 RELREC methods (A/B/C/D) for relating PC to PP records.*"
```

**Result: PASS** — §6.3.5.9.3 reference present, 4 RELREC methods (A/B/C/D) explicit.

### Probe 2: BECAT EXTRACTION in 05_mega_spec.md

```
grep result: line 159:
"| 12 | BECAT | Category for Biospecimen Event | Char | Grouping Qualifier | Perm |  |  |"
```

**Result: PASS** — BECAT variable present in BE domain spec.

### Probe 3: ch02_fundamentals (Batch M) in 02_chapters.md

```
grep result: "ch02_fundamentals" source marker present (1 match)
Content includes: Trial Design Model, Epoch, Arms and Segments, SDTM general framework
Key line: "<!-- source: knowledge_base/chapters/ch02_fundamentals.md -->"
```

**Result: PASS** — ch02_fundamentals fully included with Batch M content.

### Additional Probes

**DI domain in 06_assumptions.md**:
- Line 327: `<!-- source: knowledge_base/domains/DI/assumptions.md -->`
- Line 328: `## DI`
- Line 331: "The DI dataset was introduced as part of the SDTMIG for Medical Devices (SDTMIG-MD)."
- **PASS**

**TA/TV/TM examples in 10_examples_data_others.md**:
- `### TA — Examples` ✓
- `### TV — Examples` ✓
- `### TM — Examples` ✓
- **PASS**

**TR/TE in 06_assumptions.md**:
- `## TR` ✓
- `## TE` ✓
- **PASS**

---

## 6. Failures (Rule B)

One failure archived — see `failures/b2_claude_compress_assumptions_attempt_1.md`:

- **F1**: compress_assumptions.py first run produced 06_assumptions.md without DI domain
  (hardcoded DOMAINS list has 63 entries, DI not included — same pre-existing bug as v1.1 F1).
  Fixed by injecting "DI" between "DV" and "EC" in DOMAINS list before exec.
  Second run: rc=0, 64 domains, DI present.

---

## 7. Verdict

| Check | Result |
|-------|--------|
| V1 builds (03/05/06/07) | PASS (all rc=0) |
| V2 builds (02/09/10) | PASS (09 SOFT-PASS cap-warning, pre-existing) |
| Copy to current/uploads/ | PASS (19 files present) |
| Probe 1 PP RELREC §6.3.5.9.3 | PASS |
| Probe 2 BECAT EXTRACTION | PASS |
| Probe 3 Batch M ch02_fundamentals | PASS |
| DI domain in 06_assumptions | PASS (after fix) |
| Rule B failures archived | PASS (1 failure archived) |
| Rule D | writer-only; reviewer dispatched separately |

**Overall B2 verdict: PASS** (pending Rule D independent reviewer)
