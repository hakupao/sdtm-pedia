# Checkpoint: A3 Claude Project system_prompt v3 Writer

> Phase: A.A3
> Date: 2026-05-20
> Writer subagent: oh-my-claudecode:executor (Rule D isolated — writer only, not reviewer)
> Status: **WRITER_PASS_REVIEWER_PENDING**

---

## Task

Clean rewrite of Claude Project system_prompt v2.6 (125L) → v3 (~80-100L target, hard cap 120L).

Per design spec § 1 + § 2.3:
- 0 fossil annotation
- 5 essential rules (R1-R5)
- regex-gated CO-N table (4 triggers)
- Header style per § 1.5
- Claude-specific carry-over: 7-file KB structure + artifact-friendly response style

---

## Output Files

| File | Path |
|------|------|
| system_prompt_v3.md | `ai_platforms/claude_projects/dev/v3_draft/system_prompt_v3.md` |
| v3_design_rationale.md | `ai_platforms/claude_projects/dev/v3_draft/v3_design_rationale.md` |
| This checkpoint | `.work/07_release_v1_4/evidence/checkpoints/a3_claude_v3_writer.md` |

---

## Rule A Self-Spot-Check Results (5 probes)

| Probe | Description | Result |
|-------|-------------|--------|
| 1 | R1-R5 all present | PASS — each rule has `### R1` … `### R5` heading (grep verified) |
| 2 | regex-gated CO-N 4 triggers | PASS — biospecimen / file format / IS scope shift / SDTM-shaped var all present |
| 3 | 0 fossil annotation | PASS — grep for `v[0-9]+ 新增`, `post-R[0-9]`, `(NEW v`, `CO-[0-9]`, `v2.1`, `v2.2` → 0 matches. Header `Replaces v2.6` is allowed per spec § 1.5 (current-version reference, not iteration history). |
| 4 | Claude carry-over | PASS — 7-file KB table (00_routing through 07_examples all present); `markdown` artifact-friendly style in R4 |
| 5 | Line count 64-120L | PASS — 120 lines (at upper bound) |

All 5 probes: **PASS**

---

## Key Design Decisions

1. **7-file KB table** — v2.6 stated "9 compressed files" but Claude Project actual upload set is 7 files (00-07). v3 corrects this to 7, matching reality. Internal high/low-frequency example archives are routing-only and stay in KB Coverage Notes (not user-visible).

2. **AHP-V1/V2/V3 preserved** — The three-layer anti-hallucination mechanism validated in v1.3 R4 sanity 5/5 is carried forward intact under R2.

3. **CO-N stack replaced** — v2.6 had scattered prose constraints across multiple sections. v3 replaces these with R1-R5 + the regex-gated trigger table under R3, matching design spec § 1.3-1.4 exactly.

4. **Fossil `v2.6` mention** — The single occurrence is in the header line `Replaces v2.6` which is explicitly required by design spec § 1.5 header format. This is not a fossil annotation.

5. **Note on A3.1** — The pipeline fix (`extract_examples_data.py` capture of `## §N.N.N` section headings) is a separate task handled by the main session. This writer subagent touched only the system_prompt, per task scope.

---

## Reviewer Pending

Next step: A5 Rule D reviewer (oh-my-claudecode:critic, Rule D slot #24) audits this draft.
Reviewer must verify: 5 essential rules / 0 fossil / regex table / KB carry-over / line count.
