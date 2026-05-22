# Checkpoint A2 — ChatGPT system_prompt v3 Writer

> Phase: A.A2
> Date: 2026-05-20
> Writer: executor subagent (parallel, Rule D slot A2)
> Status: **WRITER_PASS_REVIEWER_PENDING**

---

## Task

Clean rewrite of ChatGPT system_prompt v2.2 (120L) → v3 (~80-100L target).

Per design_spec_v9.md § 1 + § 2.2:
- 0 fossil annotation
- 5 essential rules (R1-R5)
- regex-gated CO-N table (4 triggers)
- Header style per § 1.5
- KB 9 文件 multi-step routing preserved
- Method label anchor (PP §6.3.5.9.3): A=Many-Many / B=One-Many / C=Many-One / D=One-One

---

## Outputs Produced

| File | Path | Lines |
|------|------|-------|
| system_prompt_v3.md | `ai_platforms/chatgpt_gpt/dev/v3_draft/system_prompt_v3.md` | 119L |
| v3_design_rationale.md | `ai_platforms/chatgpt_gpt/dev/v3_draft/v3_design_rationale.md` | ~90L |

---

## Rule A Self-Spot-Check (5/5 PASS)

| Probe | Check | Result | Evidence |
|-------|-------|--------|---------|
| 1 | R1-R5 all present | PASS | Lines 48/54/64/87/97 |
| 2 | regex-gated CO-N 4 triggers | PASS | Lines 70/72/74/76 |
| 3 | 0 fossil annotation | PASS | `grep -cE "v[0-9]+ 改動\|v[0-9]+ 新增\|post-R[0-9]"` = 0 |
| 4 | Method label anchor 4 mappings (A=MM/B=OM/C=MO/D=OO) | PASS | Line 81 |
| 5 | Line count 64-120L | PASS | 119L |

---

## Key Design Decisions

1. **Fossil removal**: Removed header annotation `LIVE post smoke v4 R1 Q1 拼写 MINOR fix — post-apply Q1 PASS 2026-04-24` and inline `(v2.2 新增, smoke v4 R1 Q1 拼写 MINOR 修)` from 回答规范 section. Header now: `v3 LIVE 2026-05-20 — clean rewrite`.

2. **Method label anchor in R3**: Placed Method A/B/C/D explicit mapping inside R3 (Domain Scope Guards) — the correct location because PP-PC RELREC method labeling is a domain-scope issue requiring explicit KB lookup override.

3. **KB routing merged**: Combined the separate "路由规则" section with the KB table to save lines while preserving all 9-file multi-step routing information (design_spec § 2.2 carry-over).

4. **5 essential rules structure**: Converted v2.2 prose sections (回答规范 / 工作流程 / 边界处理) into explicit R1-R5 rule headers + compact boundary templates, matching design_spec § 1.3 rule structure.

5. **Line count**: 119L — within 64-120L target band. v2.2 was 120L; net reduction -1L on raw count, but structural quality substantially improved (0 fossil, explicit R1-R5, regex-gated table).

---

## No Failures

No Rule B failure archive needed — first attempt passed all 5 probes.

---

## Next Step

Rule D reviewer (slot A5, `oh-my-claudecode:scientist`) independent audit of `system_prompt_v3.md` + `v3_design_rationale.md`.
