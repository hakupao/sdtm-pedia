# Batch 20 Kickoff (Multi-Session Parallel — Session B, Round 3)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成本 batch 全部 atoms (~250-300 expected) 之前, 任何中间产物都不是终点.**
> **每 atom 完成后立即继续下一个 atom — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一的合法收尾信号是 STEP 8 echo 出 `PARALLEL_SESSION_20_DONE atoms=N failures=F repair_cycles=C rule_a=X% drift_cal=skipped findings_added=...` 单行.
>
> 在那之前若你 (a) 想 ask user 任何问题 / (b) 想 summarize 进度 / (c) 想停下等 confirmation / (d) 想说 "I'll continue in next session" / (e) 在中间 echo 任何类似 DONE 的字串 — **全部禁止**.
>
> 唯一合法的中途暂停是 halt condition (writer failure rate >15% / Rule A raw <70% / ctx >80% / 预分配 reviewer 不可派发 / 任何 shared file write 尝试) → 写 `halt_state_batch_20.md` 含 recommended_fallback 字段 + echo 单行 `HALT_BATCH_20 reason=<X>` 给 reconciler 决策, **不要** 自己 retry / fallback / 改派.
>
> The boulder never stops. 失败也算前进, 只要归档. 只有写出 `PARALLEL_SESSION_20_DONE` 才能停.
>
> ═══════════════════════════════════════════════════════════════════

> 你是 multi-session parallel 实验 round 3 的 **session B**, 跑 batch 20 (p.191-200).
> 你不知道 session C/D 的状态. 你只读你自己 scope 的输入 + 写你自己 scope 的输出.
> Round 3 sustain round 1+2 protocol 不变 + 吸收 round 2 retro G-MS-11/G-MS-12 修补 (NEW6 chapter-parent dual-form 显式 + density alarm threshold 显式).

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读
═══════════════════════════════════════════════════════════════════

并行 Read:
1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` — master 协议 (round 1-2-3 通用)
2. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_2.md` — round 2 retro 三段式, round 3 是 G-MS-11/G-MS-12 修补的实测
3. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.2.md` — writer prompt v1.2 base (v1.3 cut 仍 deferred per Rule D, inline R10-R15 + O-P1-26 + NEW1-NEW7 prepend 继续)
4. `.work/06_deep_verification/audit_matrix.md` — 19 batches roster, n=110 cumulative anchored audit, slot #1-#28 burned, vercel-family pool exhausted
5. `source/SDTMIG v3.4 (no header footer).pdf` p.4 (TOC) for §6.3.3 EG Examples tail / §6.3.4 IE / §6.3.5+ exact boundaries

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth + R-Rules + R15 Cross-Batch Sibling Context (主 session 已 prepend)
═══════════════════════════════════════════════════════════════════

### TOC (主 session PDF p.4 PRE-VERIFIED 2026-04-26, ground truth 已填入):

**Batch 20 page range 与 section 对应** (PDF p.4 TOC 实证):

```
p.191-192 : §6.3.3 ECG Test Results (EG) tail — 续 batch 19 EG-Examples 内容 (batch 19 末 atom p.190 a032 仍在 §6.3.3 EG-Examples L5 sib=3 dataset TABLE_ROWs)
p.193     : §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) — 通常 1 页超短 sub-domain (TOC: §6.3.4 = p.193, §6.3.5 = p.194)
p.194-195 : §6.3.5 Specimen-based Findings Domains (group container intro) + §6.3.5.1 Generic Specimen-based Lab Findings Domain Specification (spec template, p.194-195)
p.196-198 : §6.3.5.2 Biospecimen Findings (BS) — TOC: §6.3.5.2 = p.196, §6.3.5.3 = p.199
p.199-200 : §6.3.5.3 Cell Phenotype Findings (CP) head — TOC: §6.3.5.3 = p.199, §6.3.5.4 = p.220 (CP 超长 21 页 covers batch 20 head + batch 21 全 + batch 22 tail)
```

### 关键结构升级 (round 3 NEW): §6.3.5 group container deep-nesting

**§6.3.5 Specimen-based Findings Domains 是 group container**, 不是 individual domain. §6.3.5.X (BS/CP/GF/IS/LB/Microbiology/MI/Pharmacokinetics 9 个 sub-domains) 是 **nested L4 children under §6.3.5**, 而非 §6.3.1-4 那样 flat L3.

**Level 模型 round 3 deep-nesting**:
- §6.3 = L2 chapter (sib=3 under §6)
- §6.3.5 group container = **L3 sib=5 under §6.3** (新 chapter-internal section)
- §6.3.5.X individual domains = **L4 sib=1..9 under §6.3.5** (新 nested sub-domain level)
- 各 §6.3.5.X 的 Description / Specification / Assumptions / Examples = **L5** (NEW深一层 vs §6.3.1-4 的 L4 NEW7 chain)
- 各 §6.3.5.X.Examples.N = **L6** (NEW深一层 vs §6.3.1-4 的 L5)

**NEW7 deterministic chain 仍 hold**, 但 level 自动 +1 for §6.3.5.X children:
- §6.3.5.2 BS / §6.3.5.3 CP / etc 各 L5 sub-section chain: Description=1 / Specification=2 / Assumptions=3 / Examples=4 ± References=5

**§6.3.5.1 special**: Generic Specimen-based Lab Findings Domain Specification 是 **shared spec template**, 不是真 domain — 它没有完整 Description/Spec/Assump/Examples chain, 主要内容是 generic spec 表 (后续 §6.3.5.2-9 domains 引用 inheritance). Treat §6.3.5.1 = L4 sib=1 under §6.3.5 with simplified content (likely SENTENCE intro + TABLE_HEADER + TABLE_ROW spec template).

### R15 Cross-batch sibling context (batch 19 终态 PDF-confirmed → batch 20 起点):

**Batch 19 末态** (verified 2026-04-26):
- p.190 a015 L5 sib=2 + p.190 a026 L5 sib=3 + p.190 a032 last atom = TABLE_ROW under §6.3.3 EG-Examples (Example 3 dataset rows continuing into batch 20 p.191)
- §6.3.3 EG-Examples L4 sib=4 已 set (batch 19 p.189 a003)
- §6.3.3 EG L4 chain: Description=1 / Specification=2 / Assumptions=3 / Examples=4 全 set 不动

**Batch 20 起点 R15 chain**:
- **§6.3 [MODELS FOR FINDINGS DOMAINS]** chapter L2 sib=3 under §6 (不动)
- **§6.3.3 ECG Test Results (EG)** L3 sib=3 under §6.3 (不动)
- **§6.3.3 EG L5 Examples chain at p.191-192**:
  - 若 p.191 起仍在 Example 3 dataset rows 内 (无新 HEADING), sib=3 不变, 续 TABLE_ROW atoms parent='§6.3.3 ECG Test Results (EG)'
  - 若 p.191 / p.192 出现 "Example 4" L5 NEW HEADING, sib=4 NEW under §6.3.3 EG-Examples
  - 若 EG 章节 p.192 末结束 (§6.3.4 IE 在 p.193 NEW), 触发 R12 transition discipline
- **§6.3.4 Inclusion/Exclusion Criteria Not Met (IE)** at p.193:
  - L3 sib=4 RESTART under §6.3 chapter (NEW chapter-internal sub-domain post EG)
  - L4 chain restart Description=1 / Specification=2 / Assumptions=3 / Examples=4 (NEW7) — IE 通常仅 1 页, 可能不全有 4 个 sub-sections (e.g. 只有 Description + Spec + 没 Examples)
- **§6.3.5 Specimen-based Findings Domains (group container)** at p.194:
  - L3 sib=5 RESTART under §6.3 chapter (NEW chapter-internal group)
  - parent='§6.3 [MODELS FOR FINDINGS DOMAINS]' (chapter-form short-bracket all-caps per NEW6)
  - **L4 sub-domain chain under §6.3.5** (NEW deep-nesting layer):
    - **§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification** L4 sib=1 (special spec template, p.194-195) — parent='§6.3.5 Specimen-based Findings Domains' (L3 group canonical full-form)
    - **§6.3.5.2 Biospecimen Findings (BS)** L4 sib=2 under §6.3.5 (p.196 NEW)
    - **§6.3.5.3 Cell Phenotype Findings (CP)** L4 sib=3 under §6.3.5 (p.199 NEW)
- **§6.3.5.2 BS L5 chain** (round 3 deep-nesting): Description=1 / Specification=2 / Assumptions=3 / Examples=4 RESTART under §6.3.5.2 BS — parent='§6.3.5.2 Biospecimen Findings (BS)'
- **§6.3.5.2 BS L6 Examples chain**: independent restart sib=1 per domain
- **§6.3.5.3 CP L5 chain at p.199-200 head**: Description=1 RESTART under §6.3.5.3 CP — parent='§6.3.5.3 Cell Phenotype Findings (CP)'

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

### NEW1 drift cal dual-threshold (round 2 STRONGLY VALIDATED):

Drift cal NOT mandatory this batch (next mandatory batch 21). Skip.

### Density alarm threshold (round 2 G-MS-12 NEW spec):

For sub-batch 5 pages, expected baseline = 25-30 atoms/page (event-domain narrative+spec) OR 20-30 atoms/page (finding-domain narrative+spec). **Trigger main-session PDF cross-check + Option E rerun consideration BEFORE Rule A dispatch IF**:
- Observed atoms/page < 60% of baseline (e.g. <15-18 atoms/page)
- OR continuous 3+ pages all <20 atoms/page
- OR sub-batch total <100 atoms for 5 pages

Round 2 batch 19 caught writer 19b under-extraction via this alarm pattern (77 atoms / 5 pages = 15/page = 50% deficit triggered Option E full-batch rerun). DO NOT skip the alarm even if Rule A 100% PASS.

### R-Rules cumulative (R1-R15 unchanged from round 2):

R1-R14 同 round 2. R15 NEW from batch 12 (cross-batch sib continuity). 详见 `MULTI_SESSION_PROTOCOL.md` §R-Rules block + each prior batch_NN_kickoff.md inline section.

### Reviewer slot pre-allocation (Rule D HARDCODED 不可改):

| Batch | Slot # | 候选 Agent | Mode | Family Pivot |
|---|---|---|---|---|
| 20 | **#29** | `plugin-dev:skill-reviewer` | AUDIT (NOT skill review) | plugin-dev family **3rd burn — 完成 plugin-dev family pool** (10th AUDIT-mode pivot post round 2 #28) — write-tool-less Bash heredoc adaptation per #25 plugin-validator + #27 agent-creator precedent |

如 plugin-dev:skill-reviewer 不可派发, **halt** + 报告 (per Round 1 R-MS-1 + Round 2 reaffirmed: 不要私自选 fallback 避免 cross-session Rule D 撞).

═══════════════════════════════════════════════════════════════════
## STEP 2 — Sub-Batch 20a (writer A) Dispatch
═══════════════════════════════════════════════════════════════════

**alternation per sub-plan §B.2 batch 20 (偶 — 主 session executor-led recommendation per round 2 batch 18 0-pre-Rule-A-cycle precedent + writer-family multi-page corruption history rounds 1+2):**

`subagent_type: oh-my-claudecode:executor`
`model: sonnet`
`pages: p.191-195` (前半)

**Full prompt** (主 session prepend + dispatch — 此处省略 v1.2 base, see `subagent_prompts/P0_writer_pdf_v1.2.md`):
- TOC anchor inline-prepended (per STEP 1 §TOC)
- R-rules R1-R15 + O-P1-26 + NEW1-NEW7 cumulative inline-prepended
- NEW6 dual-form codification inline (per STEP 1 §NEW6)
- R15 cross-batch sibling context inline (per STEP 1 §R15)
- Density alarm baseline expectation inline (per STEP 1 §Density)
- Output target: `evidence/checkpoints/pdf_atoms_batch_20a.jsonl` + echo `DONE atoms=N failures=F` 单行 strict R7+R14 self-validation

═══════════════════════════════════════════════════════════════════
## STEP 3 — Sub-Batch 20b (writer B) Dispatch (parallel with 20a)
═══════════════════════════════════════════════════════════════════

`subagent_type: oh-my-claudecode:executor` (per alternation 20 偶 → executor+executor)
`model: sonnet`
`pages: p.196-200` (后半)

**Full prompt** 同 20a but pages=p.196-200 + **R15 cross-batch sibling context inline-prepended for boundary** (e.g., 若 batch 20a 终态 §6.3.4 IE-Examples sib=K, batch 20b 起 §6.3.4 IE-Examples sib=K+1 续号 OR 若进入 §6.3.5 NEW sub-domain, RESTART L4 chain from sib=1).

**主 session pre-dispatch action**: parallel dispatch 20a + 20b. Wait both. Do NOT Rule-A dispatch until both back.

═══════════════════════════════════════════════════════════════════
## STEP 4 — Schema Validation + Density Alarm + R15 Sibling Sweep + NEW6/NEW7 Format Sweep (主 session 自审 pre-Rule-A)
═══════════════════════════════════════════════════════════════════

读 20a + 20b output:
1. **Schema validation**: 0 schema error (JSON parse + 9-enum + R1 atom_id 4-digit format) + 0 atom_id collision within batch + 0 atom_id collision with root pdf_atoms.jsonl + 0 frame tag (`</content>` etc) contamination
2. **R12 transition page check**: 若 page transition 跨 §6.3.x sub-domain boundary (e.g. §6.3.3 EG → §6.3.4 IE), 验 transition page 3-zone partition (prev domain tail / chapter or chapter-internal HEADING / new domain head). 期望 ≥8 atoms on transition page per R12.
3. **Density alarm**: 算 atoms/page per page. 若 <60% baseline 25-30 = <15-18 atoms/page on any 1+ page → 主 session PDF cross-check that page + decide Option E rerun
4. **NEW6 format sweep**: grep all parent_section values for 20a + 20b. 验 chapter-parent (§6 / §6.2 / §6.3) 全用 `[BRACKET-ALL-CAPS]` short-bracket form + sub-domain parent (§6.3.x XX (CODE)) 全用 canonical full-form. Inline Option H fix any deviation.
5. **NEW7 L4 chain check**: 验 §6.3.x EG-Examples 续号 (若 batch 20 续 batch 19 EG L4) OR §6.3.4 X L4 chain restart Description=1/Spec=2/Assump=3/Examples=4 (若 batch 20 进入新 sub-domain).
6. **R15 cross-batch sibling check**: 验 §6.3.4 X L3 sib=4 under §6.3 chapter (continues batch 18+19 §6.3.1 DA=1 / §6.3.2 DD=2 / §6.3.3 EG=3 chain).

任何 violation → Inline Option H fix + Rule B `.bak` backup preserved.

═══════════════════════════════════════════════════════════════════
## STEP 5 — Option E rerun if needed (writer-family multi-bug pattern triggers)
═══════════════════════════════════════════════════════════════════

若 STEP 4 触发 Option E (density alarm OR multi-page systemic verbatim drift OR R12 transition under-extraction):
- Dispatch `subagent_type: oh-my-claudecode:executor` model=sonnet 专门 wholesale rerun of affected page range
- Apply **NEW3 outer-pipe + explicit null-key inline-required** in rerun prompt (round 1 G-MS-5 lesson, round 2 batch 17/19 successful precedents)
- Write rerun output to `pdf_atoms_batch_20a.jsonl` OR `pdf_atoms_batch_20b.jsonl` wholesale replace (Rule B `.pre-OptionE-pXXX.bak` backup preserved)
- Repair cycle counter +1

═══════════════════════════════════════════════════════════════════
## STEP 6 — Drift Cal Skip
═══════════════════════════════════════════════════════════════════

Drift cal NOT mandatory this batch (per cadence: last cal batch 18 p.180, next mandatory batch 21). Skip.

═══════════════════════════════════════════════════════════════════
## STEP 7 — Rule A 10-atom 1/page Stratified Audit (slot #29 plugin-dev:skill-reviewer AUDIT-mode pivot 10th)
═══════════════════════════════════════════════════════════════════

**seed = 20260505** (round 3 base seed +5 per round / +5 per batch = round 3 batch 20 → 20260505)

**Sample design**: 10 atoms 1/page coverage (p.191-200 = 10 pages, 1/page strict). Atom_type stratification target: TABLE_ROW × 4-5 (R8/R10/R11/NEW2 verbatim) + HEADING × 3-4 (R12 transition + R15 cross-batch sib + NEW7 L4 deterministic + NEW6 format) + 1-2 of (CODE_LITERAL / LIST_ITEM / SENTENCE) per available type distribution.

**Reviewer dispatch**: `subagent_type: plugin-dev:skill-reviewer` (Read/Grep/Glob only, NO Write tool — adapt via Bash heredoc per #25 + #27 precedent).

**Reviewer prompt prepend**:
- "Mode: AUDIT for PDF atomization quality, NOT skill review / NOT skill quality assessment / NOT skill description optimization."
- TOC anchor for batch 20 page range (per STEP 1)
- R-rules R1-R15 + O-P1-26 + NEW1-NEW7 verbatim
- 10-atom sample inline + 4-dimension verdict template (atom_type / verbatim / parent_section / heading_fields)
- Output target via Bash heredoc:
  - `cat > evidence/checkpoints/rule_a_batch_20_verdicts.jsonl <<EOF ... EOF`
  - `cat > evidence/checkpoints/rule_a_batch_20_summary.md <<EOF ... EOF`

**Threshold**: ≥90% weighted (PASS + 0.5 × PARTIAL); raw FAIL <90% → Option H repair if real bug OR Option E rerun if systemic.

═══════════════════════════════════════════════════════════════════
## STEP 8 — Sub-Progress JSON + Batch Report + Final Message (强制完成)
═══════════════════════════════════════════════════════════════════

写 `evidence/checkpoints/_progress_batch_20.json` 完整 round 3 schema 含:
- top-level batch_id/session_id/round=3/status="completed"/scope_pages/atoms_done/atoms_breakdown
- failures/repair_cycles/repair_cycle_notes
- rule_a block (reviewer_slot=29, reviewer_type=plugin-dev:skill-reviewer, reviewer_audit_pivot_index=10, sample_size, raw_pass/partial/fail, weighted_pct, verdict)
- drift_cal block (triggered=false, next_mandatory=batch 21, rationale)
- findings_added (with **finding_id_range_allocated: "O-P1-55..58"** per round 3 G-MS-7 pre-allocation; sister batches 21=O-P1-59..62 + 22=O-P1-63..66)
- rule_d_slot_used + rule_d_audit_pivot_count_post_batch
- files_written + files_NOT_touched
- halt_state=null
- **round_3_compliance** block: G_MS_4_halt_fallback / G_MS_7_finding_id_range_pre_allocation / G_MS_11_NEW6_dual_form_codified / G_MS_12_density_alarm_check_applied

写 `evidence/checkpoints/P1_batch_20_report.md` 完整 batch report.

Echo 单行:
```
PARALLEL_SESSION_20_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>
```

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 写 root `pdf_atoms.jsonl` / `audit_matrix.md` / `_progress.json` (那是 reconciler 的事)
- 写 sister batch files (`pdf_atoms_batch_21*` / `pdf_atoms_batch_22*`)
- 改 `subagent_prompts/*` / `schema/*.json` / `PLAN.md` / `plans/*.md` / `CLAUDE.md`
- 私自 pick fallback reviewer (Rule D 撞风险)
- Run git commit / push (留 user 决定)
- Ask user 任何 confirmation / 收尾询问 / 中间总结
- 在 STEP 8 echo 之前停下

**唯一合法停止 = `PARALLEL_SESSION_20_DONE ...` 单行 echo OR `HALT_BATCH_20 reason=<X>` halt 信号.**

The boulder never stops. 继续干. 第一步 STEP 0 并行 5-file Read.
