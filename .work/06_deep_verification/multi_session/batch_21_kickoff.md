# Batch 21 Kickoff (Multi-Session Parallel — Session C, Round 3)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成本 batch 全部 atoms (~250-300 expected) + 1 mandatory drift cal 之前, 任何中间产物都不是终点.**
> **每 atom 完成后立即继续下一个 atom — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一的合法收尾信号是 STEP 8 echo 出 `PARALLEL_SESSION_21_DONE atoms=N failures=F repair_cycles=C rule_a=X% drift_cal=triggered_dual_threshold findings_added=...` 单行.
>
> 在那之前若你 (a) ask user 任何问题 / (b) summarize 进度 / (c) 停下等 confirmation / (d) 说 "I'll continue in next session" / (e) 中间 echo 类似 DONE 字串 — **全部禁止**.
>
> Drift cal MANDATORY 本 batch (cadence + cumulative ≥300 atoms). NEW1 dual-threshold 必跑 (strict ≥80% AND verbatim hash overlap ≥80%, both must pass OR investigate root cause).
>
> 唯一合法中途暂停 = halt condition (writer failure rate >15% / Rule A raw <70% / ctx >80% / 预分配 reviewer 不可派发 / 任何 shared file write 尝试) → 写 `halt_state_batch_21.md` 含 recommended_fallback 字段 + echo 单行 `HALT_BATCH_21 reason=<X>` 给 reconciler 决策, **不要** 自己 retry / fallback / 改派.
>
> The boulder never stops. 失败也算前进, 只要归档. 只有写出 `PARALLEL_SESSION_21_DONE` 才能停.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel 实验 round 3 的 **session C**, 跑 batch 21 (p.201-210).
> 你不知道 session B/D 的状态. 你只读你自己 scope 的输入 + 写你自己 scope 的输出.
> Round 3 sustain round 1+2 protocol + G-MS-11 (NEW6 dual-form 显式) + G-MS-12 (density alarm threshold 显式) 修补 + drift cal MANDATORY at this batch (every-3-batches cadence post batch 18 p.180 + cumulative ≥300 atoms post-p.180).

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` — master 协议 (round 1-2-3 通用)
2. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_2.md` — round 2 retro 三段式, round 3 是 G-MS-11/G-MS-12 修补的实测
3. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.2.md` — writer prompt v1.2 base (v1.3 cut 仍 deferred per Rule D, inline R10-R15 + O-P1-26 + NEW1-NEW7 prepend 继续)
4. `.work/06_deep_verification/audit_matrix.md` — 19 batches roster, n=110 cumulative anchored audit, slot #1-#28 burned, vercel-family pool exhausted
5. `source/SDTMIG v3.4 (no header footer).pdf` p.4 (TOC) for §6.3.x sub-domains in p.201-210 range — 主 session pre-dispatch verify

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth + R-Rules + R15 Cross-Batch Sibling Context
═══════════════════════════════════════════════════════════════════

### TOC (主 session PDF p.4 PRE-VERIFIED 2026-04-26, ground truth 已填入):

**Batch 21 page range 与 section 对应** (PDF p.4 TOC 实证):

```
p.201-210 : §6.3.5.3 Cell Phenotype Findings (CP) middle 全 10 页 — TOC: §6.3.5.3 = p.199, §6.3.5.4 GF = p.220, 故 CP 跨 p.199-219 共 21 页. Batch 21 全在 CP 内部, 无 sub-domain transition.
```

**结构特点**: batch 21 整批 inside §6.3.5.3 CP, parent_section 全部为 `§6.3.5.3 Cell Phenotype Findings (CP)` (sub-domain canonical full-form per NEW6). 无 chapter-level transition / 无 sub-domain transition / R12 仅 inside-CP 章节内 transitions (e.g. CP-Specification → CP-Assumptions → CP-Examples L5 sub-section transitions).

### 关键结构 (sustained from batch 20 round 3 NEW deep-nesting):

§6.3.5 是 group container (L3 sib=5 under §6.3). §6.3.5.X 是 nested L4 children. **§6.3.5.3 CP 在 §6.3.5 group 下 L4 sib=3** (parent=`§6.3.5 Specimen-based Findings Domains`).

**Level 模型 round 3 deep-nesting**:
- §6.3.5.3 CP = L4 sib=3 under §6.3.5
- CP-Description / Specification / Assumptions / Examples = **L5** chain Description=1/Spec=2/Assump=3/Examples=4 (NEW7 deterministic, 但 level 自动 +1 vs §6.3.1-4 flat L4)
- CP-Examples N = **L6** (NEW深一层)

### R15 Cross-batch sibling context (batch 20 终态 PDF-confirmed → batch 21 起点):

**Batch 20 末态预期** (per PDF p.4 TOC + batch 20 kickoff 推算):
- batch 20 末 atom 应在 §6.3.5.3 CP 头 (p.199-200), 可能在 CP-Description 或 CP-Specification head L5 sib=1 或 sib=2 范围
- §6.3.5 group (L3 sib=5 under §6.3) 已 set
- §6.3.5.1 Generic Spec template (L4 sib=1) 已 set
- §6.3.5.2 BS (L4 sib=2 under §6.3.5) 已 set
- §6.3.5.3 CP (L4 sib=3 under §6.3.5) 已 set 为 batch 20 末 sub-domain

**Batch 21 起点 R15 chain (整批 inside §6.3.5.3 CP)**:
- **§6.3 [MODELS FOR FINDINGS DOMAINS]** L2 sib=3 (不动)
- **§6.3.5 Specimen-based Findings Domains** L3 sib=5 (不动) — parent='§6.3 [MODELS FOR FINDINGS DOMAINS]'
- **§6.3.5.3 Cell Phenotype Findings (CP)** L4 sib=3 (不动) — parent='§6.3.5 Specimen-based Findings Domains'
- **CP L5 sub-section chain**: 续 batch 20 末 sib=K+1 (likely K=2 if batch 20 ended in CP-Specification, so batch 21 起 L5 sib=3 CP-Assumptions OR sib=2 continuation if Spec spans pages — sub-session 自己读 PDF + 验前缀 atoms 续号)
- **CP L6 Examples chain**: 若 batch 21 进入 CP-Examples, L6 Examples N sib=1 RESTART under §6.3.5.3 CP (independent per domain)
- **NO chapter / sub-domain transitions inside batch 21** — 全 inside §6.3.5.3 CP

### NEW6 parent_section canonical format DUAL-FORM (round 2 G-MS-11 修补, 显式 codified):

**Rule**: parent_section format dual-form per level:
- **Chapter-level parent** (L2 / L3 atoms whose parent is §6 / §6.2 / §6.3 chapter): use **`§N.N [TITLE-ALL-CAPS]` short-bracket all-caps form** per root convention (e.g., `§6.3 [MODELS FOR FINDINGS DOMAINS]`, `§6 [Domain Models Based on the General Observation Classes]`)
- **Sub-domain parent** (L4 / L5 atoms whose parent is §6.3.3 EG / §6.3.4 X / etc): use **`§N.N.N Title (CODE)` canonical full-form** (e.g., `§6.3.3 ECG Test Results (EG)`, `§6.3.4 Inclusion-Exclusion Criteria (IE)`)

**Anti-pattern禁止**:
- 禁止 `§6.3 Models for Findings Domains` (no-bracket sentence-case for chapter — round 2 batch 18 deviation, reconciler Option H 修了)
- 禁止 `§6.3.3 [EG]` (short-bracket for sub-domain — round 1 batch 16 deviation, Option H 修了)

### NEW7 L4 sub-section sib chain deterministic (round 1 batch 16 NEW7, round 2 reaffirmed 6/6 domains):

For each §6.3.x sub-domain, L4 sub-sections use this sib chain:
- Description / Overview = sib 1
- Specification = sib 2
- Assumptions = sib 3
- Examples = sib 4
- (Optional) References = sib 5 (per batch 15 BE precedent / batch 18 DV 5-sub case)

### NEW1 drift cal dual-threshold (MANDATORY 本 batch, round 2 STRONGLY VALIDATED):

**Trigger**: every-3-batches cadence (last cal batch 18 p.180 → next mandatory batch 21) + cumulative atoms post-p.180 (batch 19 226 + batch 20 ~280-320 = ~506-546 ≥300 双触发 mandatory).

**Target page selection**: **p.205 (CP middle dense spec table or examples)** — selected per PDF p.4 TOC + CP 21-page span (p.199-219) means p.205 is mid-CP; likely CP-Specification table or CP-Examples dense dataset. 候选 dense TABLE_ROW (≥20 atoms expected per round 2 batch 18 p.180 DA spec 23-atom precedent). 若 sub-session 读 p.205 后判断该页非 dense (e.g. <15 atoms), 可 fallback 到 p.207 / p.209 邻近 dense page; 但 priority p.205.

**Method**: 2-way drift cal — baseline = 21b output (or 21a if 21b doesn't cover that page) + rerun = oh-my-claudecode:writer (alternation: writer-family rerun if executor baseline; executor rerun if writer baseline).

**Threshold**: dual NEW1 — strict ≥80% AND verbatim hash overlap ≥80%. Both must pass; either fails → investigate root cause (writer-family character-drop / interpretation-shift / marker-drop / quote-drop motifs known from O-P1-21/23/34/36/37/38/46).

**Tiebreaker**: not auto-triggered if root cause definitive (per round 1 + round 2 6 precedents).

**Report**: `drift_cal_batch_21_p<XXX>_report.md` 含 dual-threshold verdicts + root cause analysis + action (NO root file repair if baseline correct OR Option E rerun if baseline drift confirmed).

### Density alarm threshold (round 2 G-MS-12 NEW spec):

For sub-batch 5 pages, expected baseline = 25-30 atoms/page (event-domain narrative+spec) OR 20-30 atoms/page (finding-domain narrative+spec). **Trigger main-session PDF cross-check + Option E rerun consideration BEFORE Rule A dispatch IF**:
- Observed atoms/page < 60% of baseline (e.g. <15-18 atoms/page)
- OR continuous 3+ pages all <20 atoms/page
- OR sub-batch total <100 atoms for 5 pages

Round 2 batch 19 caught writer 19b under-extraction via this alarm pattern (77 atoms / 5 pages = 15/page = 50% deficit triggered Option E full-batch rerun). DO NOT skip the alarm even if Rule A 100% PASS.

### R-Rules cumulative (R1-R15 unchanged from round 2):

R1-R14 same as batch 12 (atom_id 4-digit/3-digit / DONE single-line / HEADING vs LIST_ITEM TOC-anchored / lettered list dedup / TOC anchor parent_section / codelist literal verbatim / output JSONL pure + DONE strict match / TABLE_ROW empty cell `\| \|` / dataset filename CODE_LITERAL physical-page parent / spec table wrap-cell artifact / TABLE_ROW trailing empty cell preservation / transition page full-content discipline / numbered list item discipline regardless of bold / writer DONE atoms=N self-validation).

**R15** Cross-batch sibling_index continuity. Parallel writer agents lack each other's HEADING state. Main session post-merge sweeps cross-batch sibling continuity for HEADING atoms (Examples N / Subject XXX / sub-headings sib=1,2,3,...). Each kickoff prompt includes prior batch's terminal HEADING list as context.

### Reviewer slot pre-allocation (Rule D HARDCODED 不可改):

| Batch | Slot # | 候选 Agent | Mode | Family Pivot |
|---|---|---|---|---|
| 21 | **#30** | `oh-my-claudecode:test-engineer` | AUDIT (NOT test design / NOT TDD / NOT integration test / NOT flaky test hardening) | omc-family **4th burn** (11th AUDIT-mode pivot, omc-family pool depth 4 — has all tools incl. Write) |

如 oh-my-claudecode:test-engineer 不可派发, **halt** + 报告 (per Round 1 R-MS-1 + Round 2 reaffirmed: 不要私自选 fallback 避免 cross-session Rule D 撞).

═══════════════════════════════════════════════════════════════════
## STEP 2 — Sub-Batch 21a (writer A) Dispatch
═══════════════════════════════════════════════════════════════════

**alternation per sub-plan §B.2 batch 21 (奇 → 21a=executor + 21b=writer)**:

`subagent_type: oh-my-claudecode:executor`
`model: sonnet`
`pages: p.201-205` (前半)

**Full prompt** (主 session prepend + dispatch — see `subagent_prompts/P0_writer_pdf_v1.2.md` for v1.2 base):
- TOC anchor inline-prepended (per STEP 1 §TOC)
- R-rules R1-R15 + O-P1-26 + NEW1-NEW7 cumulative inline-prepended
- NEW6 dual-form codification inline (per STEP 1 §NEW6)
- R15 cross-batch sibling context inline (per STEP 1 §R15)
- Density alarm baseline expectation inline (per STEP 1 §Density)
- Output target: `evidence/checkpoints/pdf_atoms_batch_21a.jsonl` + echo `DONE atoms=N failures=F` 单行 strict R7+R14 self-validation

═══════════════════════════════════════════════════════════════════
## STEP 3 — Sub-Batch 21b (writer B) Dispatch (parallel with 21a)
═══════════════════════════════════════════════════════════════════

`subagent_type: oh-my-claudecode:writer` (writer-family per alternation 奇 → executor + writer)
`model: sonnet`
`pages: p.206-210` (后半)

**主 session pre-dispatch action on 21b**: pre-warn writer-family R10 verbatim drift history (rounds 1+2 batches 14/15/17/19 multi-page systemic corruption). Inline prepend extra:
- NEW2 character-level self-validation extension (writer must spell-check variable names + CDISC standard tokens like STUDYID/USUBJID/DOMAIN before DONE)
- NEW3 outer-pipe + explicit null-key required (per round 1 G-MS-5 lesson)
- NEW6 dual-form codification (per STEP 1)
- Density alarm baseline 25-30 atoms/page (alarm if <60% baseline = <15-18/page)
- R10 verbatim accuracy prepend with worked examples (e.g. `STUDIID` typo from batch 15, `DALKID` N-drop from batch 18 drift cal, `HETSTESTCD` extra-ST from batch 19)

**Full prompt** 同 21a but pages=p.206-210 + R15 cross-batch sibling context inline-prepended for boundary (e.g., 若 batch 21a 终态 §6.3.K X-Examples sib=N, batch 21b 起 续号 OR 若进入 §6.3.K+1 NEW sub-domain, RESTART L4 chain from sib=1).

**主 session pre-dispatch action**: parallel dispatch 21a + 21b. Wait both. Do NOT Rule-A dispatch until both back.

═══════════════════════════════════════════════════════════════════
## STEP 4 — Schema Validation + Density Alarm + R15 Sibling Sweep + NEW6/NEW7 Format Sweep (主 session pre-Rule-A 自审)
═══════════════════════════════════════════════════════════════════

读 21a + 21b output:
1. **Schema validation**: 0 schema error (JSON parse + 9-enum + R1 atom_id 4-digit format) + 0 atom_id collision within batch + 0 atom_id collision with root pdf_atoms.jsonl + 0 frame tag (`</content>` etc) contamination
2. **R12 transition page check**: 若 page transition 跨 §6.3.x sub-domain boundary (e.g. §6.3.K → §6.3.K+1), 验 transition page 3-zone partition (prev domain tail / next domain HEADING / new domain head). 期望 ≥8 atoms on transition page per R12.
3. **Density alarm**: 算 atoms/page per page. 若 <60% baseline 25-30 = <15-18 atoms/page on any 1+ page → 主 session PDF cross-check that page + decide Option E rerun
4. **NEW6 format sweep**: grep all parent_section values for 21a + 21b. 验 chapter-parent (§6 / §6.2 / §6.3) 全用 `[BRACKET-ALL-CAPS]` short-bracket form + sub-domain parent (§6.3.x XX (CODE)) 全用 canonical full-form. Inline Option H fix any deviation.
5. **NEW7 L4 chain check**: 验 §6.3.x X-L4 chain restart Description=1/Spec=2/Assump=3/Examples=4 (若 batch 21 进入新 sub-domain).
6. **R15 cross-batch sibling check**: 验 §6.3.K X L3 sib=K under §6.3 chapter (continues batch 18-20 chain).

任何 violation → Inline Option H fix + Rule B `.bak` backup preserved.

═══════════════════════════════════════════════════════════════════
## STEP 5 — Option E rerun if needed (writer-family multi-bug pattern triggers)
═══════════════════════════════════════════════════════════════════

若 STEP 4 触发 Option E (density alarm OR multi-page systemic verbatim drift OR R12 transition under-extraction) — 历史 round 1+2 writer 21b 类 dispatch 5 次先例 (batch 06/11/12/14/15/17/19):
- Dispatch `subagent_type: oh-my-claudecode:executor` model=sonnet 专门 wholesale rerun of affected page range
- Apply **NEW3 outer-pipe + explicit null-key inline-required** in rerun prompt (round 1 G-MS-5 lesson, round 2 batch 17/19 successful precedents)
- Write rerun output to `pdf_atoms_batch_21a.jsonl` OR `pdf_atoms_batch_21b.jsonl` wholesale replace (Rule B `.pre-OptionE-pXXX.bak` backup preserved)
- Repair cycle counter +1

═══════════════════════════════════════════════════════════════════
## STEP 6 — Drift Cal MANDATORY (NEW1 dual-threshold)
═══════════════════════════════════════════════════════════════════

**主 session action**:
1. Pick target page (per STEP 1 §NEW1) — 优 dense TABLE_ROW spec/example mix
2. Identify baseline (21a OR 21b output for that page) + rerun agent (executor if writer baseline, writer if executor baseline)
3. Dispatch rerun agent (subagent_type: oh-my-claudecode:writer or oh-my-claudecode:executor) for that single page only
4. Compute strict count match (rerun atoms / baseline atoms)
5. Compute verbatim hash overlap (e.g. SHA256 per atom content + sort + intersect set ratio)
6. Apply NEW1 dual-threshold (both ≥80% PASS, otherwise investigate)
7. Root cause analysis if FAIL — categorize:
   - writer-family character-drop motif (per O-P1-23 DSDTC / O-P1-34 ECNKID / O-P1-36 STUDIID / O-P1-46 DALKID)
   - interpretation-shift motif (per O-P1-21 SVCNTMOD / O-P1-46 paraphrases)
   - marker-drop motif (per O-P1-46 `*` Grouping Qualifier)
   - quote-drop motif (per O-P1-46 quote marks)
   - direction-reversed precedent (baseline correct, rerun introduces drift — round 2 batch 18 6th precedent)
   - convention-drift (e.g. inner-pipe vs outer-pipe per round 1 batch 14 O-P1-37)
8. Action: NO root repair if baseline correct (per round 2 batch 18 precedent) OR Option E rerun if baseline drift confirmed OR Option H bulk fix if multi-atom systemic
9. Write `drift_cal_batch_21_p<XXX>_report.md` 含 dual-threshold verdicts + root cause + action

═══════════════════════════════════════════════════════════════════
## STEP 7 — Rule A 10-atom 1/page Stratified Audit (slot #30 oh-my-claudecode:test-engineer AUDIT-mode pivot 11th)
═══════════════════════════════════════════════════════════════════

**seed = 20260510** (round 3 batch 21 base seed)

**Sample design**: 10 atoms 1/page coverage (p.201-210 = 10 pages, 1/page strict). Atom_type stratification target: include drift cal target page + transition pages (R12) + sub-domain L4 chain HEADING (NEW7) + cross-batch sib continuation HEADING (R15) + at least 4-5 TABLE_ROW (R8/R10/R11/NEW2 verbatim) + 2-3 HEADING (R12 + R15 + NEW7) + 1-2 (CODE_LITERAL / LIST_ITEM / SENTENCE).

**Reviewer dispatch**: `subagent_type: oh-my-claudecode:test-engineer` (has Write tool — direct file write OK, no Bash heredoc needed).

**Reviewer prompt prepend**:
- "Mode: AUDIT for PDF atomization quality, NOT test strategy / NOT TDD / NOT integration test / NOT flaky test hardening."
- TOC anchor for batch 21 page range (per STEP 1)
- R-rules R1-R15 + O-P1-26 + NEW1-NEW7 verbatim
- 10-atom sample inline + 4-dimension verdict template (atom_type / verbatim / parent_section / heading_fields)
- Output target:
  - `evidence/checkpoints/rule_a_batch_21_verdicts.jsonl`
  - `evidence/checkpoints/rule_a_batch_21_summary.md`

**Threshold**: ≥90% weighted (PASS + 0.5 × PARTIAL); raw FAIL <90% → Option H repair if real bug OR Option E rerun if systemic.

═══════════════════════════════════════════════════════════════════
## STEP 8 — Sub-Progress JSON + Batch Report + Final Message (强制完成)
═══════════════════════════════════════════════════════════════════

写 `evidence/checkpoints/_progress_batch_21.json` 完整 round 3 schema 含:
- top-level batch_id/session_id/round=3/status="completed"/scope_pages/atoms_done/atoms_breakdown
- failures/repair_cycles/repair_cycle_notes
- rule_a block (reviewer_slot=30, reviewer_type=oh-my-claudecode:test-engineer, reviewer_audit_pivot_index=11, sample_size, raw_pass/partial/fail, weighted_pct, verdict)
- **drift_cal block (triggered=true, page=<XXX>, dual-threshold strict + verbatim metrics, root_cause, action, report_file)**
- findings_added (with finding_id_range_allocated O-P1-59..62 per round 3 G-MS-7)
- rule_d_slot_used + rule_d_audit_pivot_count_post_batch
- files_written + files_NOT_touched
- halt_state=null
- **round_3_compliance** block: G_MS_4_halt_fallback / G_MS_7_finding_id_range_pre_allocation / G_MS_11_NEW6_dual_form_codified / G_MS_12_density_alarm_check_applied / NEW1_dual_threshold_drift_cal

写 `evidence/checkpoints/P1_batch_21_report.md` 完整 batch report (~22-25KB per round 2 pattern).

Echo 单行:
```
PARALLEL_SESSION_21_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=triggered_dual_threshold findings_added=<list>
```

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 写 root `pdf_atoms.jsonl` / `audit_matrix.md` / `_progress.json` (那是 reconciler 的事)
- 写 sister batch files (`pdf_atoms_batch_20*` / `pdf_atoms_batch_22*`)
- 改 `subagent_prompts/*` / `schema/*.json` / `PLAN.md` / `plans/*.md` / `CLAUDE.md`
- 私自 pick fallback reviewer (Rule D 撞风险)
- Run git commit / push (留 user 决定)
- Ask user 任何 confirmation / 收尾询问 / 中间总结
- 在 STEP 8 echo 之前停下

**唯一合法停止 = `PARALLEL_SESSION_21_DONE ...` 单行 echo OR `HALT_BATCH_21 reason=<X>` halt 信号.**

The boulder never stops. 继续干. 第一步 STEP 0 并行 5-file Read.
