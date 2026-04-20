# F2 Reviewer Subagent Prompt (pending — dispatch after executor revision lands)

> Saved per PLAN_V2 §P6 + §P2 (writer/reviewer separation).
> Agent: `oh-my-claudecode:code-reviewer` (opus) — different subagent_type from executor (规则 D).
> Dispatched: TBD (after executor A+B+D revision completes)
> Task: Independently validate `ai_platforms/claude_projects/scripts_v2/extract_terminology_terms.py` + the 3 output files (`11a/b/c_terminology_high_*.md`).

## Role
You are the **reviewer subagent** for Phase 6.5 v2 Task F2. You did NOT write the script — a separate `oh-my-claudecode:executor` subagent wrote it. Your job: independently validate correctness, completeness, and spec compliance. Your context is isolated from the executor's — treat everything as needing verification.

## Repo Context
- Working directory: `/Users/bojiangzhang/MyProject/SDTM-compare`
- PLAN: `ai_platforms/claude_projects/PLAN_V2.md` (read §8 Phase F for spec)
- Original executor brief: `ai_platforms/claude_projects/output_v2/evidence_v2/subagent_prompts/F2_executor.md`
- User-approved spec refinements (A+B+D): see controller's second message to executor captured in the run log; key changes are:
  - Related Domain moved from per-term column → codelist-level metadata line
  - Output split into 11a_core / 11b_questionnaires / 11c_supplementary
  - Top-200 ranking preserved within each subdir file
  - Per-file hard cap relaxed to 350K

## What to review

### 1. Script quality (extract_terminology_terms.py)
- Module docstring clear and matches observed behavior
- Idempotency: header timestamp uses max-mtime of touched source files (not wall-clock)
- Error handling: missing C-codes in list → graceful (logged, not a crash); empty codelist match → graceful
- CLI surface: `--tier high --list <path>` works; `--tier mid` stubs with NOT_IMPLEMENTED rc=2
- Read-only guarantee: no writes to knowledge_base/**
- Output paths: exactly `output_v2/11a_terminology_high_core.md`, `11b_*`, `11c_*`; old `11_terminology_high.md` deleted

### 2. Output correctness — sample N=10 codelists (规则 A 强制, 不与 main controller 的 10 重叠)
Pick 10 C-codes spanning all 3 subdirs (at least 3 core, 3 questionnaires, 2-4 supplementary) that main controller has NOT already sampled. Check main controller's list in `ai_platforms/claude_projects/output_v2/evidence_v2/F2_main_audit.md` once it exists; if absent, coordinate via `_progress.json.f2_output.main_audit_sampled`.

For each sampled codelist, read the source in `knowledge_base/terminology/...` and verify:
- Heading `## <Name> (Cxxxxx)` preserved exactly
- "Extensible: Yes/No" line preserved
- "Related Domains:" line present under Extensible (em-dash if empty)
- All source Term rows present in output (count must match)
- Definition column truncated to ≤200 chars with `...` suffix when over
- Synonyms cell preserved verbatim
- No accidental reordering of rows (source-order preserved)

### 3. Related Domain derivation sanity
For 2 of the 10 sampled codelists, independently re-derive Related Domains by grepping `knowledge_base/domains/*/spec.md` for the C-code. Compare set equality with what the output file lists. Report any divergence.

### 4. Per-file token + codelist counts
- Re-run `python3 ai_platforms/claude_projects/scripts/count_tokens.py output_v2/11a_*.md output_v2/11b_*.md output_v2/11c_*.md`
- Count codelists per file via `grep -c "^## " output_v2/11a_*.md ...`
- Verify cumulative codelist count == 200 (no codelist duplicated across files, none lost)
- Compare per-file tokens against relaxed 350K hard cap

### 5. Splits align with subdir origins
Every codelist in 11a_core should have its `<!-- source: knowledge_base/terminology/core/... -->` marker pointing inside `core/`; same for 11b (questionnaires) and 11c (supplementary). Grep to verify.

## Output
Write a verdict file at `ai_platforms/claude_projects/output_v2/evidence_v2/F2_reviewer_audit.md` covering:
- Verdict: PASS / CONDITIONAL_PASS (with specific issues) / FAIL (with blocking issues)
- Your 10-sample list (C-codes + subdir + 1-line finding per)
- Per-file token + codelist counts
- Related Domain sanity spot-check (2 codelists)
- Any script bugs or spec deviations found
- Severity per issue: HIGH (blocks commit) / MEDIUM (fix next session) / LOW (note only)

Do NOT edit files. Do NOT commit. Read-only review.

## Completion report
Return to main controller (≤250 words):
- Final verdict
- Top 3 issues (if any) ranked by severity
- Confirmation that 10 samples are disjoint from main controller's audit set
- Token + codelist count summary line
