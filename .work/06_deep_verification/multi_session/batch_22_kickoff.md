# Batch 22 Kickoff (Multi-Session Parallel — Session D, Round 3)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成本 batch 全部 atoms (~250-300 expected) 之前, 任何中间产物都不是终点.**
> **每 atom 完成后立即继续下一个 atom — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一的合法收尾信号是 STEP 8 echo 出 `PARALLEL_SESSION_22_DONE atoms=N failures=F repair_cycles=C rule_a=X% drift_cal=skipped findings_added=...` 单行.
>
> 在那之前若你 (a) ask user 任何问题 / (b) summarize 进度 / (c) 停下等 confirmation / (d) 说 "I'll continue in next session" / (e) 中间 echo 类似 DONE 字串 — **全部禁止**.
>
> 唯一合法中途暂停 = halt condition (writer failure rate >15% / Rule A raw <70% / ctx >80% / 预分配 reviewer 不可派发 / 任何 shared file write 尝试) → 写 `halt_state_batch_22.md` 含 recommended_fallback 字段 + echo 单行 `HALT_BATCH_22 reason=<X>` 给 reconciler 决策, **不要** 自己 retry / fallback / 改派.
>
> The boulder never stops. 失败也算前进, 只要归档. 只有写出 `PARALLEL_SESSION_22_DONE` 才能停.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel 实验 round 3 的 **session D**, 跑 batch 22 (p.211-220).
> 你不知道 session B/C 的状态. 你只读你自己 scope 的输入 + 写你自己 scope 的输出.
> Round 3 sustain round 1+2 protocol + G-MS-11 (NEW6 dual-form 显式) + G-MS-12 (density alarm threshold 显式) 修补.

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` — master 协议 (round 1-2-3 通用)
2. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_2.md` — round 2 retro 三段式
3. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.2.md` — writer prompt v1.2 base (v1.3 cut 仍 deferred per Rule D, inline R10-R15 + O-P1-26 + NEW1-NEW7 prepend 继续)
4. `.work/06_deep_verification/audit_matrix.md` — 19 batches roster, n=110 cumulative anchored audit, slot #1-#28 burned, vercel-family pool exhausted
5. `source/SDTMIG v3.4 (no header footer).pdf` p.4 (TOC) for §6.3.x sub-domains in p.211-220 range — 主 session pre-dispatch verify, 候 §6.4 NEW chapter 若 §6.3 sub-domains 完结

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth + R-Rules + R15 Cross-Batch Sibling Context
═══════════════════════════════════════════════════════════════════

### TOC (主 session PDF p.4 PRE-VERIFIED 2026-04-26, ground truth 已填入):

**Batch 22 page range 与 section 对应** (PDF p.4 TOC 实证):

```
p.211-219 : §6.3.5.3 Cell Phenotype Findings (CP) tail — 续 batch 21 (CP 跨 p.199-219 共 21 页)
p.220     : §6.3.5.4 Genomics Findings (GF) NEW sub-domain transition — TOC: §6.3.5.4 = p.220, §6.3.5.5 IS = p.228, 故 GF 跨 p.220-227 共 8 页 (batch 22 仅触 GF head 1 页 p.220)
```

**结构特点**: batch 22 大部分仍 inside §6.3.5.3 CP (p.211-219 = 9 pages CP tail), 只有 p.220 触发 §6.3.5.4 GF NEW sub-domain transition. **不**进 §6.4 chapter NEW (TOC: §6.4 Findings About Events or Interventions = p.361, far beyond batch 22 scope).

### 关键结构 (sustained from batch 20+21 round 3 NEW deep-nesting):

§6.3.5 group container 下 §6.3.5.X nested L4 sub-domains 模型继续:
- §6.3.5.3 CP = L4 sib=3 under §6.3.5 (不动 from batch 20+21)
- §6.3.5.4 GF = **L4 sib=4 RESTART under §6.3.5** (NEW p.220, batch 22 触发)
  - parent='§6.3.5 Specimen-based Findings Domains'
- GF L5 sub-section chain at p.220 head: **Description=1 RESTART** under §6.3.5.4 GF

**Level 模型 round 3 deep-nesting** (sustained):
- §6.3.5.X domain = L4
- 各 domain Description / Spec / Assump / Examples = L5 (NEW7 chain)
- 各 domain Examples N = L6

### R15 Cross-batch sibling context (batch 21 终态 PDF-confirmed → batch 22 起点):

**Batch 21 末态预期** (per PDF p.4 TOC + batch 21 全 inside §6.3.5.3 CP):
- batch 21 末 atom 应在 §6.3.5.3 CP middle/tail (p.210), 仍 parent='§6.3.5.3 Cell Phenotype Findings (CP)'
- §6.3.5.3 CP L5 sub-section chain progression: batch 20 触 Description=1 + Spec head; batch 21 触 Spec body / Assumptions=3 / Examples=4 part; batch 22 续 Examples N tail until p.220 GF NEW transition

**Batch 22 起点 R15 chain (大部分 inside §6.3.5.3 CP, 末 NEW transition §6.3.5.4 GF)**:
- **§6.3 [MODELS FOR FINDINGS DOMAINS]** L2 sib=3 (不动)
- **§6.3.5 Specimen-based Findings Domains** L3 sib=5 (不动) — parent='§6.3 [MODELS FOR FINDINGS DOMAINS]'
- **§6.3.5.3 Cell Phenotype Findings (CP)** L4 sib=3 (不动 batch 22 p.211-219) — parent='§6.3.5 Specimen-based Findings Domains'
- **§6.3.5.3 CP L5 chain at p.211-219**: 续 batch 21 末 sib=K+1 (likely K=3 if batch 21 ended in CP-Assumptions, batch 22 起 L5 sib=4 CP-Examples; OR sib continuation if Assumptions / Examples spans pages — sub-session 自己读 PDF + 验前缀 atoms 续号)
- **§6.3.5.3 CP L6 Examples chain**: 若 batch 22 在 CP-Examples 范围, L6 Examples N 续号 from batch 21 末 sib=K+1 (independent per domain, but cross-batch within same domain continues)
- **§6.3.5.4 Genomics Findings (GF) NEW transition at p.220** (R12 sub-domain-level transition discipline, ≥8 atoms 期望):
  - L4 sib=4 RESTART under §6.3.5 (NEW)
  - parent='§6.3.5 Specimen-based Findings Domains' (L3 group canonical full-form per NEW6)
  - L5 sub-section chain restart Description=1 under §6.3.5.4 GF — parent='§6.3.5.4 Genomics Findings (GF)'
  - L6 Examples chain restart sib=1 RESTART per domain

### NEW6 parent_section canonical format DUAL-FORM (round 2 G-MS-11 修补, 显式 codified):

**Rule**: parent_section format dual-form per level:
- **Chapter-level parent** (L2 / L3 atoms whose parent is §6 / §6.2 / §6.3 / §6.4 chapter): use **`§N.N [TITLE-ALL-CAPS]` short-bracket all-caps form** per root convention (e.g., `§6.3 [MODELS FOR FINDINGS DOMAINS]`, `§6 [Domain Models Based on the General Observation Classes]`, **若 §6.4 NEW chapter then `§6.4 [TITLE-ALL-CAPS]` per PDF TOC**)
- **Sub-domain parent** (L4 / L5 atoms whose parent is §6.3.x XX / §6.4.y YY / etc): use **`§N.N.N Title (CODE)` canonical full-form** (e.g., `§6.3.K X (XX)`)

**Anti-pattern禁止**:
- 禁止 `§6.3 Models for Findings Domains` (no-bracket sentence-case for chapter — round 2 batch 18 deviation, reconciler Option H 修了)
- 禁止 `§6.3.K [XX]` (short-bracket for sub-domain — round 1 batch 16 deviation, Option H 修了)

### NEW7 L4 sub-section sib chain deterministic (round 1 batch 16 NEW7, round 2 reaffirmed 6/6 domains):

For each §6.3.x / §6.4.y sub-domain, L4 sub-sections use this sib chain:
- Description / Overview = sib 1
- Specification = sib 2
- Assumptions = sib 3
- Examples = sib 4
- (Optional) References = sib 5 (per batch 15 BE precedent / batch 18 DV 5-sub case)

### NEW1 drift cal: NOT mandatory 本 batch (last cal batch 21, next mandatory batch 24). Skip.

### Density alarm threshold (round 2 G-MS-12 NEW spec):

For sub-batch 5 pages, expected baseline = 25-30 atoms/page (event-domain narrative+spec) OR 20-30 atoms/page (finding-domain narrative+spec). **Trigger main-session PDF cross-check + Option E rerun consideration BEFORE Rule A dispatch IF**:
- Observed atoms/page < 60% of baseline (e.g. <15-18 atoms/page)
- OR continuous 3+ pages all <20 atoms/page
- OR sub-batch total <100 atoms for 5 pages

Round 2 batch 19 caught writer 19b under-extraction via this alarm pattern (77 atoms / 5 pages = 15/page = 50% deficit triggered Option E full-batch rerun). DO NOT skip the alarm even if Rule A 100% PASS.

### R-Rules cumulative (R1-R15 unchanged from round 2 — 同 batch 20/21 STEP 1):

R1-R14 same as batch 12 + R15 cross-batch sibling continuity. 详见 `MULTI_SESSION_PROTOCOL.md` §R-Rules block + each prior batch_NN_kickoff.md inline section.

### Reviewer slot pre-allocation (Rule D HARDCODED 不可改):

| Batch | Slot # | 候选 Agent | Mode | Family Pivot |
|---|---|---|---|---|
| 22 | **#31** | `oh-my-claudecode:git-master` | AUDIT (NOT git operations / NOT commit / NOT rebase / NOT history management / NOT atomic commits) | omc-family **5th burn** (12th AUDIT-mode pivot, omc-family pool depth 5 — has all tools incl. Write) |

如 oh-my-claudecode:git-master 不可派发, **halt** + 报告 (per Round 1 R-MS-1 + Round 2 reaffirmed: 不要私自选 fallback 避免 cross-session Rule D 撞).

═══════════════════════════════════════════════════════════════════
## STEP 2 — Sub-Batch 22a (writer A) Dispatch
═══════════════════════════════════════════════════════════════════

**alternation per sub-plan §B.2 batch 22 (偶 → executor+executor parallel per round 2 batch 18 0-pre-Rule-A-cycle precedent + writer-family multi-page corruption history rounds 1+2)**:

`subagent_type: oh-my-claudecode:executor`
`model: sonnet`
`pages: p.211-215` (前半)

**Full prompt** (主 session prepend + dispatch — see `subagent_prompts/P0_writer_pdf_v1.2.md` for v1.2 base):
- TOC anchor inline-prepended (per STEP 1 §TOC)
- R-rules R1-R15 + O-P1-26 + NEW1-NEW7 cumulative inline-prepended
- NEW6 dual-form codification inline (per STEP 1 §NEW6) — 含 §6.4 chapter form 若 applicable
- R15 cross-batch sibling context inline (per STEP 1 §R15)
- Density alarm baseline expectation inline (per STEP 1 §Density)
- Output target: `evidence/checkpoints/pdf_atoms_batch_22a.jsonl` + echo `DONE atoms=N failures=F` 单行 strict R7+R14 self-validation

═══════════════════════════════════════════════════════════════════
## STEP 3 — Sub-Batch 22b (writer B) Dispatch (parallel with 22a)
═══════════════════════════════════════════════════════════════════

`subagent_type: oh-my-claudecode:executor` (alternation 偶 → executor+executor)
`model: sonnet`
`pages: p.216-220` (后半)

**Full prompt** 同 22a but pages=p.216-220 + R15 cross-batch sibling context inline-prepended for boundary (e.g., 若 batch 22a 终态 §6.3.K X-Examples sib=N, batch 22b 起 续号 OR 若进入 §6.3.K+1 / §6.4.1 NEW sub-domain, RESTART L4 chain from sib=1).

**主 session pre-dispatch action**: parallel dispatch 22a + 22b. Wait both. Do NOT Rule-A dispatch until both back.

═══════════════════════════════════════════════════════════════════
## STEP 4 — Schema Validation + Density Alarm + R15 Sibling Sweep + NEW6/NEW7 Format Sweep + R12 NEW5 chapter-level Transition Sweep (主 session pre-Rule-A 自审)
═══════════════════════════════════════════════════════════════════

读 22a + 22b output:
1. **Schema validation**: 0 schema error (JSON parse + 9-enum + R1 atom_id 4-digit format) + 0 atom_id collision within batch + 0 atom_id collision with root pdf_atoms.jsonl + 0 frame tag (`</content>` etc) contamination
2. **R12 transition page check**: 验 p.220 §6.3.5.3 CP → §6.3.5.4 GF sub-domain transition 3-zone partition (CP tail / §6.3.5.4 GF L4 HEADING / GF Description head). 期望 ≥8 atoms on transition page per R12. (注: batch 22 NOT 触 §6.4 chapter — TOC §6.4 = p.361 远超 batch scope)
3. **Density alarm**: 算 atoms/page per page. 若 <60% baseline 25-30 = <15-18 atoms/page on any 1+ page → 主 session PDF cross-check that page + decide Option E rerun
4. **NEW6 format sweep**: grep all parent_section values for 22a + 22b. 验 chapter-parent (§6 / §6.2 / §6.3 / **§6.4 若 NEW chapter**) 全用 `[BRACKET-ALL-CAPS]` short-bracket form + sub-domain parent (§N.N.N XX (CODE)) 全用 canonical full-form. Inline Option H fix any deviation.
5. **NEW7 L4 chain check**: 验 §6.3.x / §6.4.y X-L4 chain restart Description=1/Spec=2/Assump=3/Examples=4 (若 batch 22 进入新 sub-domain).
6. **R15 cross-batch sibling check**: 验 §6.3.K X L3 sib=K under §6.3 chapter (continues batch 18-21 chain) + **若 §6.4 NEW chapter, 验 §6.4 L2 sib=4 under §6 RESTART + §6.4.1 L3 sib=1 RESTART under §6.4**.

任何 violation → Inline Option H fix + Rule B `.bak` backup preserved.

**特别注意 §6.4 chapter NEW transition** (若 applicable): R12 NEW5 chapter-level transition strengthening 严验 + 期望 ≥8 atoms on transition page (per round 1 batch 14 §6.2 NEW + round 2 batch 18 §6.3 NEW precedents).

═══════════════════════════════════════════════════════════════════
## STEP 5 — Option E rerun if needed (writer-family multi-bug pattern triggers)
═══════════════════════════════════════════════════════════════════

若 STEP 4 触发 Option E (density alarm OR multi-page systemic verbatim drift OR R12 transition under-extraction):
- Dispatch `subagent_type: oh-my-claudecode:executor` model=sonnet 专门 wholesale rerun of affected page range
- Apply **NEW3 outer-pipe + explicit null-key inline-required** in rerun prompt (round 1 G-MS-5 lesson, round 2 batch 17/19 successful precedents)
- Write rerun output to `pdf_atoms_batch_22a.jsonl` OR `pdf_atoms_batch_22b.jsonl` wholesale replace (Rule B `.pre-OptionE-pXXX.bak` backup preserved)
- Repair cycle counter +1

═══════════════════════════════════════════════════════════════════
## STEP 6 — Drift Cal Skip (per cadence)
═══════════════════════════════════════════════════════════════════

Drift cal NOT mandatory this batch (per cadence: last cal batch 21, next mandatory batch 24). Skip.

═══════════════════════════════════════════════════════════════════
## STEP 7 — Rule A 10-atom 1/page Stratified Audit (slot #31 oh-my-claudecode:git-master AUDIT-mode pivot 12th)
═══════════════════════════════════════════════════════════════════

**seed = 20260515** (round 3 batch 22 base seed)

**Sample design**: 10 atoms 1/page coverage (p.211-220 = 10 pages, 1/page strict). Atom_type stratification target: include p.220 §6.3.5.4 GF sub-domain NEW transition HEADING (R12 NEW5 sub-domain-level) + §6.3.5.3 CP L5 chain HEADING (NEW7 deep-nesting at L5) + cross-batch sib continuation HEADING (R15) + at least 4-5 TABLE_ROW (R8/R10/R11/NEW2 verbatim, CP spec/example heavy + GF head) + 2-3 HEADING (R12 GF NEW + R15 CP continuation + NEW7 deep-nesting chain) + 1-2 (CODE_LITERAL / LIST_ITEM / SENTENCE).

**Reviewer dispatch**: `subagent_type: oh-my-claudecode:git-master` (has all tools — direct file write OK).

**Reviewer prompt prepend**:
- "Mode: AUDIT for PDF atomization quality, NOT git operations / NOT commit / NOT rebase / NOT history management / NOT atomic commits."
- TOC anchor for batch 22 page range (per STEP 1)
- R-rules R1-R15 + O-P1-26 + NEW1-NEW7 verbatim
- 10-atom sample inline + 4-dimension verdict template (atom_type / verbatim / parent_section / heading_fields)
- Output target:
  - `evidence/checkpoints/rule_a_batch_22_verdicts.jsonl`
  - `evidence/checkpoints/rule_a_batch_22_summary.md`

**Threshold**: ≥90% weighted (PASS + 0.5 × PARTIAL); raw FAIL <90% → Option H repair if real bug OR Option E rerun if systemic.

═══════════════════════════════════════════════════════════════════
## STEP 8 — Sub-Progress JSON + Batch Report + Final Message (强制完成)
═══════════════════════════════════════════════════════════════════

写 `evidence/checkpoints/_progress_batch_22.json` 完整 round 3 schema 含:
- top-level batch_id/session_id/round=3/status="completed"/scope_pages/atoms_done/atoms_breakdown
- failures/repair_cycles/repair_cycle_notes
- rule_a block (reviewer_slot=31, reviewer_type=oh-my-claudecode:git-master, reviewer_audit_pivot_index=12, sample_size, raw_pass/partial/fail, weighted_pct, verdict)
- drift_cal block (triggered=false, next_mandatory=batch 24, rationale)
- findings_added (with finding_id_range_allocated O-P1-63..66 per round 3 G-MS-7)
- rule_d_slot_used + rule_d_audit_pivot_count_post_batch
- files_written + files_NOT_touched
- halt_state=null
- **round_3_compliance** block: G_MS_4_halt_fallback / G_MS_7_finding_id_range_pre_allocation / G_MS_11_NEW6_dual_form_codified / G_MS_12_density_alarm_check_applied
- **若 §6.4 NEW chapter transition observed**: dedicated section logging chapter_transition_pXXX (zone partition + L2 sib=4 + §6.4.1 sib=1 RESTART + 4 HEADING atoms NEW7 chain validation)

写 `evidence/checkpoints/P1_batch_22_report.md` 完整 batch report (~22-25KB per round 2 pattern).

Echo 单行:
```
PARALLEL_SESSION_22_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>
```

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 写 root `pdf_atoms.jsonl` / `audit_matrix.md` / `_progress.json` (那是 reconciler 的事)
- 写 sister batch files (`pdf_atoms_batch_20*` / `pdf_atoms_batch_21*`)
- 改 `subagent_prompts/*` / `schema/*.json` / `PLAN.md` / `plans/*.md` / `CLAUDE.md`
- 私自 pick fallback reviewer (Rule D 撞风险)
- Run git commit / push (留 user 决定)
- Ask user 任何 confirmation / 收尾询问 / 中间总结
- 在 STEP 8 echo 之前停下

**唯一合法停止 = `PARALLEL_SESSION_22_DONE ...` 单行 echo OR `HALT_BATCH_22 reason=<X>` halt 信号.**

The boulder never stops. 继续干. 第一步 STEP 0 并行 5-file Read.
