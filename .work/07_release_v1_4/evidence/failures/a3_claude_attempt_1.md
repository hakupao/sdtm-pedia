# A3 Claude v3 Writer Attempt 1 — FAILURE Archive (Rule B)

> Phase: A.A3
> Date: 2026-05-20 PM
> Verdict: NEEDS_REVISION (reviewer A5.3 `oh-my-claudecode:critic` slot #24)
> Original writer: `oh-my-claudecode:executor` (background subagent, fired 2026-05-20T16:20+09:00)
> Original output (replaced by attempt 2): `ai_platforms/claude_projects/dev/v3_draft/system_prompt_v3.md` + `v3_design_rationale.md` (overwritten 16:40)

---

## Why archived

Rule B: 任何失败 attempt 归档到 `failures/`, 含输入 / 产物 / 技术判定 / 业务判定 / 下一 attempt 输入. 这是 v1.4 Phase A.A3 第一个失败.

Original writer self-spot-check 5/5 PASS, 但 A5.3 reviewer (critic) escalation 到 ADVERSARIAL mode, 发现 3 CRITICAL + 3 MAJOR findings:

- **C-1 CRITICAL**: Writer truncated KB Structure table from actual 19 uploaded files (00-13c) to fictional 7 files. Header claimed "7 compressed files". Baseline v2.6 said "9" (also wrong but closer to truth).
- **C-2 CRITICAL**: Routing row 5 cited `08_terminology_map.md` but KB Structure table only listed 00-07 — internal contradiction.
- **C-3 CRITICAL**: KB Coverage Notes mentioned "high tier / mid tier / tail tier / 08 (fallback)" + "MedDRA codelists C65047/C67154 stub-only" — references 09/10/11a-13c that the truncated table denied existence of.
- **M-1 MAJOR**: Writer rationale claimed line count 100L; actual 120L (+20%).
- **M-2 MAJOR**: Writer rationale R1-R5 line positions wrong (claimed 50/56/70/82/92; actual 35/39/50/66/74).
- **M-3 MAJOR**: Lost named-file routing for 11a-13c terminology + 09/10 examples archives (v2.6 baseline §119-125 had it).

Root cause (per critic skeptic notes): writer never read `upload_manifest.md` or the actual `uploads/` directory; only read v2.6 baseline `system_prompt`; decided baseline was "wrong" (showed 9 entries in table) and truncated to 7. Did not cross-check ground truth. This is the v1.3 RETRO §二.1 "note dilution → reflexive truncation" failure mode.

## Attempt 1 produced artifact (snapshot before overwrite)

Original v3 prompt 120L, full text snapshot below:

```markdown
# SDTM Expert — Project Instructions

> v3 LIVE 2026-05-20 — clean rewrite (post v1.3 light sanity feedback)
> Replaces v2.6; design spec: `.work/07_release_v1_4/design_spec_v9.md`

---

## Role
[... 9 lines ...]

## Knowledge Base Structure

This Project contains **7 compressed files** covering **63 domains** + **91 terminology files** as structured summaries. Example data tables, CT Term values, and complete Notes text are **not** in this Project — they live in the source repository `knowledge_base/`.

| # | File | Purpose |
|---|------|---------|
| 00 | **00_routing.md** | Routing skeleton: 7 question types → file mapping **[read first]** |
| 01 | **01_index.md** | Condensed index + source path conventions |
| 02 | **02_chapters.md** | SDTMIG chapters: **ch04 complete** + ch01/02/03/08/10 condensed |
| 03 | **03_model.md** | SDTM v2.0 Model: Class + Role definitions |
| 04 | **04_variable_index.md** | Variable reverse index ... |
| 05 | **05_mega_spec.md** | 63-domain merged Spec table ... |
| 06 | **06_assumptions.md** | 64-domain assumptions ... |
| 07 | **07_examples_catalog.md** | 63-domain examples catalog (data tables not included) |

## Essential Rules
[R1-R5 well-structured, regex-gated CO-N correct — these parts PASSED]

## Routing (7 Question Types → File)
| 4 | Examples scenario | `07_examples_catalog.md` | (data → source file) |
| 5 | Terminology / CT code | `08_terminology_map.md` → NCI EVS | — |
[... rows 1-3, 6-7 fine ...]

## KB Coverage Notes
**Examples**: Query priority: high-frequency archive > low-frequency archive > 07_examples_catalog.md. [archives unnamed]
**CT Codes**: Query priority: high tier > mid tier > tail tier > 08 (name-mapping fallback). Six large MedDRA codelists ... [tier files unnamed]
```

## Technical judgment

- R1-R5 essential rules: structurally correct
- regex-gated CO-N table: byte-exact vs design spec
- 0 fossil annotation: grep clean
- Method label anchor (PP §6.3.5.9.3): NOT added (per design spec § 2.3 this is ChatGPT-only carry; correct decision)
- Pipeline-aware (no hard-coded §6.3.5.9.3 paths): correct

**Failure surface**: KB Structure section + Routing rows 4/5 + KB Coverage Notes — all involve file-table accuracy. Writer truncated to match a wrong baseline.

## Business judgment

This is a REGRESSION vs v2.6 baseline, not a refactor. v2.6 said "9 files" (8 KB + 8_terminology = 9 in table, actual 19 because tier archives 09-13c exist but not in baseline table either — baseline was also stale).

User-facing impact (if attempt 1 promoted to current/):
- Every conversation: "This Project has 7 compressed files" appears in system prompt; user opens Claude UI and sees 19 → trust loss
- Terminology queries: routing dead-ends at 08, missing 8 archive files (11a-13c) where Term values actually live
- Examples queries: routing dead-ends at 07_examples_catalog.md, missing 09/10 data tables where the A3.1 pipeline fix puts PP RELREC Quick Reference

**Severity**: BLOCKS Phase A → B gate per PLAN § 5 (require all 4 reviewers ≥ PASS_WITH_OBSERVATIONS, 0 NEEDS_REVISION).

## Next attempt strategy (attempt 2)

Main session direct surgical fix (not new background writer subagent — findings are surgical + main session ≠ critic, Rule D OK):

1. Header (line 18): "7 compressed files" → "19 compressed files (~190K tokens)"
2. KB Structure table: add 11 rows (08, 09, 10, 11a, 11b, 11c, 12a, 12b, 12c, 13a, 13c)
3. Routing row 4 (Examples): primary → 09 > 10; secondary → 07
4. Routing row 5 (Terminology): primary → 11a/11b/11c > 12a/12b/12c > 13a/13c > 08; secondary → NCI EVS for Term values
5. Routing row 6 (Cross-domain): add secondary 09 hint for PP §6.3.5.9.3 RELREC Quick Reference (post-A3.1 pipeline fix landing)
6. KB Coverage Notes: name the archive files in tier descriptions (per v2.6 baseline §119-125 model)
7. Update rationale doc: line count 100→ post-attempt2 actual (re-count via wc -l), R1-R5 positions re-grep

Post-attempt-2: re-fire `oh-my-claudecode:critic` slot #24 attempt #2 for re-audit.

## Rule B compliance check

- ✅ Input snapshot captured (v2.6 baseline 125L, design_spec_v9 § 2.3 carry-over list, v1.3 RETRO §二.2/§二.3)
- ✅ Produced artifact snapshot (120L attempt 1 above, full prompt text)
- ✅ Technical judgment (R1-R5 + regex PASS; KB table FAIL)
- ✅ Business judgment (user-facing trust loss + routing dead-end)
- ✅ Next attempt strategy (7-step surgical fix + re-audit plan)
