# Checkpoint D — release/v1.4/ cut

> Phase D executor subagent, completed 2026-05-22.
> Scope: 3 KNOWN_LIMITATIONS §0 reconcile + 4 CHANGELOG v1.4 entry prepend + BUILD_MANIFEST.json refresh.

## Deliverables

### 1. KNOWN_LIMITATIONS.{zh,en,ja}.md (3 files)

| File | v1.3 lines | v1.4 lines | Δ | Verify |
|---|---|---|---|---|
| `release/v1.4/KNOWN_LIMITATIONS.zh.md` | 80 | 109 | +29 | §0 replaced (v1.4 reconcile from DRAFT); §1-§6 byte-exact inherit |
| `release/v1.4/KNOWN_LIMITATIONS.en.md` | 80 | 109 | +29 | §0 translated (technical en, v1.3 §0 en vocab/style); §1-§6 byte-exact inherit |
| `release/v1.4/KNOWN_LIMITATIONS.ja.md` | 80 | 109 | +29 | §0 translated (technical ja, v1.3 §0 ja vocab/style); §1-§6 byte-exact inherit |

§1-§6 byte-exact inherit verified via `diff <(sed -n '/^## 1\./,/$/p' v1.3) <(sed -n '/^## 1\./,/$/p' v1.4)` → 0 diff for all 3 languages.

Frontmatter: `release: v1.4` added, `draft_status` removed (from DRAFT).

§0 content reconciled with v1.4 reality:
- §0.A Gemini MAINTAINED_NO_SANITY_TEST framing (not ABANDONED)
- §0.B v1.4 deliverables (Phase A prompts + B sanity 12/12 + C 4 carries)
- §0.C v1.3 §0 item reconcile table (7 rows)
- §0.D v1.4 not-done list (7 items defer to v1.5)
- §0.E deployment notes (Gemini self-verify, NotebookLM bucket 25, ChatGPT Method label)

### 2. CHANGELOG.{md,en,zh,ja}.md (4 files)

| File | v1.3 lines | v1.4 lines | Δ |
|---|---|---|---|
| `release/v1.4/CHANGELOG.md` | 103 | 174 | +71 |
| `release/v1.4/CHANGELOG.en.md` | 103 | 174 | +71 |
| `release/v1.4/CHANGELOG.zh.md` | 92 | 163 | +71 |
| `release/v1.4/CHANGELOG.ja.md` | 92 | 163 | +71 |

v1.4 entry prepended before v1.3 entry. Structure mirrors v1.3 entry sections:
- 概要/Summary
- 类型/Type/タイプ
- Prompt 改动 (4-platform v3/v9)
- 知识库改动 (1 file: PP/examples.md +13 lines Method label table)
- 各平台 bundle 变更 (4 platforms)
- Pipeline / build script 修复 (`extract_examples_data.py` parents[3]→[4] bugfix)
- 验证 (B1 12/12 PASS, B2 N/A Gemini, Q-S2 SKIPPED, C2 N=80, C1 P4b)
- 已知问题 (defer v1.5: C1-bis, C1-ter, C2 KB_INTERNAL_CROSSREF, C2 3 deep-paraphrase, C3 screenshot, Tier B 156, full 437 UNSOURCED, Phase 7)
- 升级方法 (3 sanity-covered + Gemini self-verify + NotebookLM bucket 25)

v1.3 entry preserved verbatim (3 instances of `v1.3-company-release` retained in each file).

### 3. BUILD_MANIFEST.json (1 file)

| Field | v1.3 | v1.4 |
|---|---|---|
| release_tag | `v1.3-company-release` | `v1.4-company-release` |
| release_date | 2026-05-20 | 2026-05-22 |
| previous_tag | v1.2-company-release | v1.3-company-release |
| previous_date | 2026-05-19 | 2026-05-20 |
| release_type | `knowledge_base_pass` | `prompt_pass` |
| files lines | 113 | 152 |

New v1.4 sections added:
- `sanity_coverage`: covered=[chatgpt, claude, notebooklm], excluded=[gemini], rationale (user 2026-05-22 decision)
- `phase_c_carries` (4 entries): C1 COMPLETE_WITH_CAVEAT, C2 COMPLETE_WITH_FINDING, C3 PARTIAL, C4 COMPLETE
- `pipeline_bugs_fixed` (1 entry): extract_examples_data.py parents[3]→[4] path bugfix
- `unsourced_manual_n80_sample`: cumulative N=80 stats (75 RI + 0 XLSX + 0 HALLUCINATED + 5 NEEDS_HUMAN_REVIEW; Rule A 10/10)
- Platform sections updated: each system_prompt status reflects v3/v9 clean rewrite; gemini gains `sanity_status: MAINTAINED_NO_SANITY_TEST`

JSON validated: `python3 -c "import json; json.load(open(...))"` → valid.

## Rule A probes (5 sampled)

1. **zh KNOWN_LIMITATIONS §0 — Gemini MAINTAINED_NO_SANITY framing**: PASS (MAINTAINED_NO_SANITY count=1, ABANDONED count=0).
2. **en KNOWN_LIMITATIONS §0 — Gemini MAINTAINED_NO_SANITY framing**: PASS (MAINTAINED_NO_SANITY count=1, ABANDONED count=0).
3. **ja KNOWN_LIMITATIONS §0 — Gemini MAINTAINED_NO_SANITY framing**: PASS (MAINTAINED_NO_SANITY count=1, ABANDONED count=0).
4. **CHANGELOG v1.4 entry present (all 4 files)**: PASS (`v1.4 (2026-05-22)` count=1 per file, v1.3 entry preserved with 3 occurrences of `v1.3-company-release` per file).
5. **BUILD_MANIFEST.json validation**: PASS — valid JSON, `release_tag = "v1.4-company-release"`, `release_type = "prompt_pass"`, `sanity_coverage.platforms_covered = ['chatgpt', 'claude', 'notebooklm']`, `phase_c_carries` has 4 entries, `pipeline_bugs_fixed` has 1 entry.

5/5 Rule A probes PASS.

## Constraints honored

- Read-only on `release/v1.4/self_deploy/` (already populated by main session).
- No git tag.
- No modification to `release/v1.3/`.

## Next steps (main session)

- Phase E: post-audit pass (Rule D #26).
- Phase F: RETROSPECTIVE + sync + commit.
- Tag `v1.4-company-release` after verification + audit.

**Exit verdict**: RELEASE_CUT_READY.
