# C5 — 3-platform bundle rebuild post C4 (2026-05-22)

> **Phase**: C
> **Task**: Task #7
> **Trigger**: C4 KB anchor added Method label mapping table to `PP/examples.md` §6.3.5.9.3
> **Scope**: ChatGPT + Claude + NotebookLM (Gemini ABANDONED, not rebuilt)

## 1. ChatGPT bundle rebuild ✓

Script: `ai_platforms/chatgpt_gpt/dev/scripts/merge_for_chatgpt.py --stage batch2`

- `06_domain_examples_all.md`: 225,614 tokens, 63 sources, manifest updated
- Verification: `grep "Method label mapping" 06_domain_examples_all.md` ✓ 1 match (within PP block)
- Output: `ai_platforms/chatgpt_gpt/current/uploads/06_domain_examples_all.md`
- Other batch2 files: 05/07/08/09 manifest skipped (same)

## 2. NotebookLM bucket rebuild ✓

Script: `ai_platforms/notebooklm/dev/scripts/merge_sources.py` (all 42 buckets)

- Bucket 16 `16_fnd_pharma_pc_pp.md` contains Method label table (verified via grep)
- Total: 42 buckets, 1,601,033 words, 9.35 MiB
- Over-cap buckets (>500K words): 0
- Output: `ai_platforms/notebooklm/current/uploads/`
- All 42 buckets regenerated (idempotent reseed of other 41 buckets is harmless)

## 3. Claude bundle rebuild ⚠️ — path bug fixed + size concern

Script: `ai_platforms/claude_projects/dev/scripts/extract_examples_data.py --tier high --domain-list ai_platforms/claude_projects/dev/evidence/D1_domain_list.md`

### 3.A. Path bug discovered + fixed (uncommitted)

- **Bug**: `REPO_ROOT = Path(__file__).resolve().parents[3]` resolves to `/ai_platforms` (after Phase 6.5 reorg-A moved script from `scripts_v2/` to `dev/scripts/`, adding one more directory level), causing all 28 domains to be flagged "missing examples.md" — script wrote header-only 706-token file.
- **Root cause**: Commit `87573bd Phase 6.5 v2 reorg-A: restructure claude_projects/ into current/docs/dev/archive layout` moved the script but didn't update `parents[N]`.
- **A3.1 smoke test miss**: v1.4 Phase A A3.1 verdict "PASS 3/3 smoke (PP/PC/MB §N.N.N captured)" — smoke likely ran in a different working configuration, didn't catch path bug.
- **Fix**: `parents[3]` → `parents[4]` (uncommitted edit in `extract_examples_data.py`)
- **Result post-fix**: 28 domains included, 0 missing, Method label table captured ✓

### 3.B. Size: 112K tokens exceeds script HARD_CAP=50K

- New `09_examples_data_high.md`: 3,268 lines, 112,918 tokens
- Previous file (May 20 pre-rebuild): 2,922 lines (~102K tokens already, the HARD_CAP=50K was always violated — likely aspirational from a prior tier definition)
- A3.1 §N.N.N capture added 3 sections: `#### §6.3.5.7.3 Microbiology Specimen and Microbiology Susceptibility Examples`, `#### §6.3.5.9.3 Relating PP Records to PC Records — Worked Examples`, `#### §6.3.5.9.3 RELREC Method Quick Reference (PP-side view)` — +346 lines (~10K tokens)
- **Decision needed (user)**:
  - (a) Raise HARD_CAP to 120K (or remove cap) — Claude Projects accepts files this size
  - (b) Selectively skip §N.N.N capture for some domains
  - (c) Accept current 112K as-is, note as v1.4 known caveat
  - **Recommended**: (a) — Claude Projects per-file limit is multi-MB; 50K cap was a relic
- Verification: `grep "Method label mapping" output_v2/09_examples_data_high.md` ✓ 1 match
- Output: `ai_platforms/claude_projects/output_v2/09_examples_data_high.md` (then synced to `current/uploads/`)

### 3.C. Sync to current/uploads/

`cp output_v2/09_examples_data_high.md → current/uploads/09_examples_data_high.md` ✓ Method label table present.

## 4. Gemini — NOT rebuilt (ABANDONED)

per `c0_gemini_drop_ack.md`, Gemini bundle stays at v1.3 baseline. v9 prompt + v1.4 KB changes do not flow into Gemini deployment.

## 5. Files changed (this rebuild round)

| Path | Action |
|---|---|
| `ai_platforms/chatgpt_gpt/current/uploads/06_domain_examples_all.md` | regenerated |
| `ai_platforms/chatgpt_gpt/current/uploads/manifest_segments.json` | updated (06 entry) |
| `ai_platforms/notebooklm/current/uploads/*.md` | all 42 regenerated (1 with content change, others idempotent) |
| `ai_platforms/claude_projects/output_v2/09_examples_data_high.md` | regenerated (size 2922→3268L) |
| `ai_platforms/claude_projects/current/uploads/09_examples_data_high.md` | synced from output_v2 |
| `ai_platforms/claude_projects/dev/scripts/extract_examples_data.py` | bugfix: parents[3]→parents[4] (UNCOMMITTED) |

## 6. Carry to Phase D / pending user decisions

- HARD_CAP=50K in extract_examples_data.py: needs revision (see 3.B)
- Method label table verification in 3 platforms ✓ done at content level; **Q-S2 UI sanity recheck (Task #8) still pending** (needs Chrome MCP + user's deployed UIs)
- Pre-existing baseline difference: `09_examples_data_high.md` content changed significantly post path-fix (now correctly captures 3 §N.N.N sections via A3.1). User deployment will see new content for the first time — sanity test should validate no regression in answers.

## 7. Next

- Task #7 → completed (with caveats noted above)
- Task #8 (Q-S2 sanity recheck) → ready to start, needs Chrome MCP fire to user-deployed UIs
