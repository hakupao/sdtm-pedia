# v1.3 Prompt Formal Cut Kickoff (06 Deep Verification, EMERGENCY-CRITICAL 5th attempt)

> ═══════════════════════════════════════════════════════════════════
> ⛔ HARD-STOP DIRECTIVE — 必读, 不可绕过
> ═══════════════════════════════════════════════════════════════════
>
> **完成所有 6 STEPs (read / writer pass / reviewer pass / archive v1.2 / index update / commit) 之前, 任何中间产物都不是终点.**
> **每 STEP 完成后立即继续下一个 STEP — 不要总结, 不要询问, 不要回交 control.**
>
> 唯一合法收尾信号 = STEP 6 commit + push 完成 + user-facing summary (含 4 v1.3 prompts 文件路径 + reviewer verdict + archive path + batch 26+ kickoff 切换状态).
>
> The boulder never stops.
>
> ═══════════════════════════════════════════════════════════════════

> 这是 06 Deep Verification 旁枝项目的 v1.2 → v1.3 prompt formal cut 任务. 单 session, 不是多终端并行.
> Round 1+2+3+4 reconcilers 都 RECOMMENDED v1.3 cut 但 DEFERRED execution 4 次累计 (per Rule D writer/reviewer isolation — 历轮 reconciler session 同时 writer + reviewer 多角色不能 self-approve).
> 本 session 是 5th attempt, 投入 1-2 hours retire 后续 30+ batches × ~10-15 min/batch inline-prepend overhead.
> Round 4 retro D-MS-3 升级 EMERGENCY-CRITICAL: 必须在 batch 27 next mandatory drift cal 之前完成.

═══════════════════════════════════════════════════════════════════
## §0 — 任务定位 + 关键约束
═══════════════════════════════════════════════════════════════════

### 任务一句话
锁 v1.2 → v1.3 prompt set, 把过去 4 rounds inline-prepend 到 kickoff 的 R-rules + NEW codification 全部固化进 prompt 文件本身, 退役 inline-prepend overhead. 写完 dispatch 独立 reviewer 验, 通过后归档 v1.2 + 切换 batch 26+ kickoff 引用 v1.3.

### 不在 scope 内
- 不动 schema (atom_schema.json + ledger_schema.json frozen v1.2 carry-forward)
- 不动 PLAN.md v0.5 (only 引用 bump if needed)
- 不跑 PDF atomization / Rule A audit / drift cal
- 不动 root pdf_atoms.jsonl / audit_matrix.md / _progress.json (除 STEP 5 引用更新)
- 不动 round 5 kickoff 文件 except STEP 5 引用切换

### 🔴 Rule D 强制 (writer/reviewer isolation)
**主 session = writer**: 写 4 个 v1.3 prompt 文件.
**Dispatched reviewer = 不同 subagent_type**: 验 4 个 prompt 文件.
**禁止主 session 自审**: 即使两 turns 也不行. Reviewer 必须独立 agent.

候选 reviewer (按推荐顺序):
1. `oh-my-claudecode:critic` (Opus, READ-ONLY) — 多角度结构化, 推荐首选
2. `oh-my-claudecode:document-specialist` — 文档质量专精
3. `pr-review-toolkit:code-reviewer` — 严谨 PR-style 审查
4. `superpowers:code-reviewer` — 已 burned for code, 但 doc review 不撞 Rule D Roster

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 (并行 Read, 不要省)
═══════════════════════════════════════════════════════════════════

**File set 必读** (10 files 并行 Read):

1. `.work/06_deep_verification/_progress.json` — recovery_hint 完整 round 4 narrative ~14500 chars (current state authoritative source post round 4)
2. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_4.md` — 12 R-MS retain + 6 G-MS gap + 7 D-MS decision (Rule C 三段式 26180 bytes)
3. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_3.md` — NEW7 L7 + G-MS-11.b + G-MS-13 NEW gap origin
4. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_2.md` — G-MS-11 NEW6 dual-form 起源 + G-MS-12 density alarm 起源
5. `.work/06_deep_verification/subagent_prompts/v1.3_patch_candidates.md` — 188 行 base candidates (round 1-2 NEW1-NEW5 spec) + round 3 NEW7-NEW8 + round 4 NEW8.b/c/G-MS-12.a 加 (本 session 必须完整吸收)
6. `.work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.2.md` — writer base
7. `.work/06_deep_verification/subagent_prompts/P0_writer_md_v1.2.md` — md writer base
8. `.work/06_deep_verification/subagent_prompts/P0_matcher_v1.2.md` — matcher base
9. `.work/06_deep_verification/subagent_prompts/P0_reviewer_v1.2.md` — reviewer base
10. `.work/06_deep_verification/schema/atom_schema.json` + `ledger_schema.json` — v1.2 schema, frozen carry-forward (v1.3 link 不改)

**附读** (verify-only, 验 round 4 reconciler-side fix evidence):
- `.work/06_deep_verification/multi_session/sibling_continuity_sweep_report_round4.md` — round 4 reconciler safety net 4-atom Option H NEW7 L6 LB-Examples drift O-P1-79 detail
- `.work/06_deep_verification/evidence/checkpoints/_progress_batch_25.json` — round 4 batch 25 terminal sib state for sub-batch handoff template reference

═══════════════════════════════════════════════════════════════════
## STEP 1 — Writer Pass: 写 v1.3 4 个 Prompts (主 session writer 角色)
═══════════════════════════════════════════════════════════════════

### 产出文件 (路径: `.work/06_deep_verification/subagent_prompts/`)
1. `P0_writer_pdf_v1.3.md` ★ 主体 — PDF atomization writer (executor/writer alternation)
2. `P0_writer_md_v1.3.md` — MD-side atomization writer
3. `P0_matcher_v1.3.md` — Forward/reverse matcher
4. `P0_reviewer_v1.3.md` — Rule A 10-atom reviewer

### v1.3 必须 codify 全部 13 项 (A-M):

**(A) R-rules R1-R15 全块 inline 完整** (替代 v1.2 narrative):
- R1: atom_id 4-digit page + 3-digit atom index `ig34_p<NNNN>_a<NNN>`, autofix 3-digit → 4-digit on output
- R2: agent DONE single-line `DONE atoms=N failures=F` (writer/executor return contract)
- R3: HEADING vs LIST_ITEM TOC-anchored (parent_section MUST match PDF p.4 TOC ground truth)
- R4: lettered list dedup (无重复 'a' / '1' across same parent)
- R5: TOC anchor parent_section dual-form (per NEW6 below)
- R6: codelist literal verbatim (no paraphrase, no normalize)
- R7: output JSONL pure (1 JSON / line, no comments / blanks) + DONE strict match wc -l
- R8: TABLE_ROW empty cell `\| \|` (preserve trailing pipes)
- R9: dataset filename HEADING vs CODE_LITERAL — physical-page parent codification (round 1 NEW4)
- R10: verbatim 严格字面 strict no-paraphrase / no synonym substitution / no whitespace normalization (round 4 batch 24 verbatim 41.2% FAIL exposed writer-family SENTENCE paraphrase risk)
- R11: spec table wrap-cell artifact handling (multi-line cell collapse)
- R12: transition page 3-zone partition + ≥8 atoms full-content discipline (round 1+ R12)
- R13: numbered list item discipline regardless of bold (preserve bold without converting to HEADING)
- R14: writer DONE atoms=N self-validation (count match output line count)
- R15: cross-batch sibling_index continuity (sib chain per parent across batches; round 1+2+3+4 EFFECTIVE)

**(B) O-P1-26 codification** — PDF→KB 字面级深审旁枝 spec carry-forward (frozen)

**(C) NEW1 dual-threshold drift cal mandatory**:
- strict count overlap ≥80% AND verbatim hash overlap ≥80%
- Both ≥80% → PASS; Either <80% → FAIL + DIRECTION analysis + writer-family motif
- Round 1+2+3+4 STRONGLY VALIDATED 4× (drift cal value-add 9 precedents)

**(D) NEW2 single-character iteration self-validation**:
- Cyrillic → Latin substitution catch (e.g. CPCЕЛSTA → CPCELSTA)
- Limitation noted: misses adjacent Latin-Latin swap (e.g. CPCSMRKS↔CPSCMRKS) — see NEW8 below

**(E) NEW3-NEW5 from round 1-2** (per v1.3_patch_candidates.md):
- NEW3 Option E rerun outer-pipe + null-key correction
- NEW4 dataset filename HEADING-vs-CODE_LITERAL physical-page parent codification
- NEW5 R12 chapter-level transition strengthening

**(F) NEW6 + NEW6.b dual-form parent_section** (round 2 G-MS-11 + round 3 G-MS-11.b extension EFFECTIVE 4× round 4):
- Chapter-level (§6 / §6.2 / §6.3): `§N.N [TITLE-ALL-CAPS]` short-bracket all-caps
- L3 sub-domain group (§6.3.5): canonical full-form `§6.3.5 Specimen-based Findings Domains` (no CODE)
- L4 §6.3.5.X individual domain HEADING: `§6.3.5.X Title (CODE)` canonical full-form
- L4 §6.3.5.X group container (e.g. §6.3.5.7 Microbiology Domains): canonical full-form (no CODE since plural group)
- **🔴 L4 sub-domain section-start HEADING parent = L3 group canonical full-form `§6.3.5 Specimen-based Findings Domains` (NEVER self-parent)** ← NEW6.b extension, round 4 4× EFFECTIVE proactive (IS p.228 + LB p.241 + Microbiology Domains p.248 + GF p.220 round 3 post-detection)
- L5+ atom parent: same canonical full-form as L4 domain

**(G) 🔴 NEW7 deep-nesting chain procedural enforcement (PRIORITY — 2× RECURRENCE round 3+4 = formal codification mandatory)**:
- L5 chain per §6.3.5.X domain: Description=1 / Specification=2 / Assumptions=3 / Examples=4 (± References=5)
- **L6 'Examples N' HEADING ALWAYS heading_level=6 sibling_index=1..N RESTART per §6.3.5.X domain (NEVER SENTENCE)** ← round 3 batch 23 O-P1-68 + round 4 batch 25 O-P1-79 reconciler-side fix = 2 occurrences within 2 rounds
- L7 sub-example: Example Na/Nb under Example N = hl=7 sib=1, 2 RESTART (round 3 NEW7 L7 precedent batch 21)
- **L4 group-container branch (round 4 NEW)**: when L4 is plural group container (e.g. §6.3.5.7 Microbiology Domains), internal §N.N.N.N sub-domain RESTART at L5 sib=1..N under L4 group; each own L6 chain Description=1/Spec=2/Assump=3/Examples=4 (round 4 O-P1-75 INFO precedent §6.3.5.7.1 MB)
- **🔴 Procedural sub-batch handoff template (mandatory in dispatch prompt)**: 主 session dispatch sub-batch B prompt MUST inline-prepend prior sub-batch A 终态:
  ```
  PRIOR SUB-BATCH A HEADING STATE (sub-batch B MUST continue, NOT restart):
  - Last L4 sib used (under §N.N): <N>
  - Last L5 sib used: <M>
  - Last L6 Example sib used: <K>
  - Convention: Example N+1 = HEADING hl=6 sib=K+1 (ALWAYS, NEVER SENTENCE)
  - §N.N.N.Examples HEADING ALWAYS hl=5 sib=4
  - L4 sub-domain section-start HEADING parent = L3 group canonical full-form NEVER self-parent
  ```

**(H) NEW8 substring n-gram cross-check** vs canonical CDISC variable list (round 3 catches CPSCMRKS adjacent-letter swap that NEW2 misses; round 4 catches 6+ ISBDAGNT/ISTSTDTL/ISTSTOPO/ISORRESU/ISSTRESN/ISDTC multi-char drops):
- 实现: 写手 / executor agent self-validate by checking each [A-Z]{3,} variable identifier in output against canonical CDISC variable list (subset of SDTMIG v3.4 master list)
- Catch threshold: any uppercase identifier of length ≥3 not in canonical list flagged for re-verification

**(I) NEW8.b SENTENCE-trigram extension** (round 4 NEW v1.4 candidate from O-P1-72):
- Whole-SENTENCE trigram comparison vs baseline atom (drift cal context primarily)
- Catches paraphrase / synonym substitution / re-summarization (NEW8 single-variable focus too narrow for SENTENCE-level drift)

**(J) NEW8.c TABLE_HEADER column-set validation** (round 4 NEW v1.4 candidate from O-P1-74):
- 验 TABLE_HEADER column SET (membership not just individual variable spell) matches expected canonical column set per PDF + per CDISC IS spec
- Catches missing-column / extra-column errors (e.g. NHOID missing + ISORRESU spurious in IS Example 7 ELISPOT table)

**(K) G-MS-12 density alarm threshold spec**:
- Per-page floor: 15 atoms (alarm fires if <15)
- Per-sub-batch floor: 100 atoms
- Alarm → 主 session PDF cross-check (Read tool `pages: "<N>"`) + adjudicate FALSE / TRUE POSITIVE
- TRUE POSITIVE → Option E full-page rerun
- Round 2-4 validated 3× FALSE POSITIVE (batch 20 p.192 sparse eg.xpt + batch 24 p.232 list-only IS-Assumptions + batch 21 p.208 TRUE POSITIVE → Option E rerun 10→23 atoms +130%)

**(L) G-MS-12.a content-type-aware density floor (v1.4 candidate)** — round 4 NEW codified now (ahead of v1.4):
- list-only pages floor=8 (not 15)
- spec-table pages floor=15 (current default)
- transition pages floor=8 (R12 ≥8 atoms 3-zone partition)

**(M) G-MS-13 finding ID range cross-validation table kickoff prepend** (round 4 EFFECTIVE 0 mis-allocation):
- Multi-session kickoff template MUST include 3-batch range table at top:
  ```
  | Session | Batch | Range | 本 batch 用 |
  |---|---|---|---|
  | B | NN | O-P1-XX..YY | ✅ / ❌ |
  ```
- Self-validation gate at STEP 7 of each batch kickoff: any finding_id outside reserved range → STOP fix

### Schema link (no schema change)
v1.3 prompts MUST reference (not duplicate):
- `schema/atom_schema.json` (JSON Schema 2020-12, 9-enum atom_type frozen)
- `schema/ledger_schema.json` (9 forward verdict + 5 reverse verdict frozen)

### v1.3 vs v1.2 diff requirement
v1.3 MUST be codification of items A-M, NOT behavior change. Output JSONL format / atom_type 9-enum / heading_level + sibling_index semantics / DONE single-line contract / Rule B backup discipline = all carry-forward unchanged.

═══════════════════════════════════════════════════════════════════
## STEP 2 — Reviewer Pass (Rule D 强制 ISOLATION)
═══════════════════════════════════════════════════════════════════

### Dispatch reviewer agent (主 session 不能自审)
推荐: `oh-my-claudecode:critic` (Opus, READ-ONLY)

### Reviewer prompt 必须包含

```
Mode: AUDIT for prompt completeness verification, NOT general criticism / NOT plan critique.

Task: Verify v1.3 4 prompts (P0_writer_pdf_v1.3.md / P0_writer_md_v1.3.md / P0_matcher_v1.3.md / P0_reviewer_v1.3.md) against round 4 retro requirements.

Inputs to read:
1. .work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.3.md (NEW main writer)
2. .work/06_deep_verification/subagent_prompts/P0_writer_md_v1.3.md
3. .work/06_deep_verification/subagent_prompts/P0_matcher_v1.3.md
4. .work/06_deep_verification/subagent_prompts/P0_reviewer_v1.3.md
5. .work/06_deep_verification/multi_session/MULTI_SESSION_RETRO_ROUND_4.md (12 R-MS + 6 G-MS + 7 D-MS)
6. .work/06_deep_verification/subagent_prompts/v1_3_cut_kickoff.md §STEP 1 codification list A-M
7. .work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.2.md (v1.2 base for diff)

Verification per item A-M (13 items from STEP 1 spec):
For each item, return PASS / FAIL / CONDITIONAL_PASS verdict + concrete evidence (line numbers / quoted bullet).

Critical items requiring strict scrutiny:
- (G) NEW7 L6 procedural sub-batch handoff template — MUST be procedural (concrete handoff state block) not narrative; round 3+4 RECURRENCE = mandatory
- (F) NEW6.b L4 self-parent extension — MUST have explicit "NEVER self-parent" bullet
- (M) G-MS-13 cross-validation table — MUST be kickoff template not just narrative
- (C) NEW1 dual-threshold — MUST specify both strict ≥80% AND verbatim ≥80% (not OR)
- (H) NEW8 substring n-gram — MUST reference canonical CDISC variable list as oracle

Diff scrutiny:
- v1.3 vs v1.2 MUST be codification not behavior change
- Schema link unchanged
- Output format unchanged

Optimality question:
- Could v1.3 retire MORE inline-prepend overhead than codified items?
- Are any items in round 4 retro 6 G-MS gap missing from v1.3?

Output format:
- Per-item table: PASS / FAIL / CONDITIONAL_PASS + 1-line evidence
- Overall verdict: PASS / FAIL / CONDITIONAL_PASS
- Required follow-ups (if FAIL or CONDITIONAL_PASS)

Be terse but rigorous. <500 words.
```

### Verdict handling
- **PASS**: 直接 STEP 3
- **CONDITIONAL_PASS**: 主 session writer 修 follow-ups (same writer can re-edit; re-审同 reviewer 不同 turn OK = single-reviewer multi-pass model)
- **FAIL**: writer 重写 affected sections, reviewer 重审 (loop 直到 PASS)

═══════════════════════════════════════════════════════════════════
## STEP 3 — Archive v1.2
═══════════════════════════════════════════════════════════════════

```bash
# Use absolute date (YYYY-MM-DD) in archive dir name
DATE=$(date +%Y-%m-%d)
mkdir -p ".work/06_deep_verification/subagent_prompts/archive/v1.2_final_${DATE}"
cp .work/06_deep_verification/subagent_prompts/P0_writer_pdf_v1.2.md ".work/06_deep_verification/subagent_prompts/archive/v1.2_final_${DATE}/"
cp .work/06_deep_verification/subagent_prompts/P0_writer_md_v1.2.md ".work/06_deep_verification/subagent_prompts/archive/v1.2_final_${DATE}/"
cp .work/06_deep_verification/subagent_prompts/P0_matcher_v1.2.md ".work/06_deep_verification/subagent_prompts/archive/v1.2_final_${DATE}/"
cp .work/06_deep_verification/subagent_prompts/P0_reviewer_v1.2.md ".work/06_deep_verification/subagent_prompts/archive/v1.2_final_${DATE}/"
```

(do NOT delete v1.2 from primary location — keep both v1.2 + v1.3 side-by-side until next cleanup; archive is provenance copy)

═══════════════════════════════════════════════════════════════════
## STEP 4 — Update batch 26+ Kickoff References
═══════════════════════════════════════════════════════════════════

替代 inline-prepend, kickoff §2 改为 1 句引用:

### Edit `.work/06_deep_verification/multi_session/batch_26_kickoff.md`
- §2 Cumulative R-Rules section: 替换 narrative R1-R15 + NEW1-NEW8 详 inline → 1 句 `see subagent_prompts/P0_writer_pdf_v1.3.md for full R-rules + NEW codification (A-M items)`
- 保留 §2 中 "🔴 NEW7 L6 Sub-Batch Handoff (PROCEDURAL ENFORCEMENT)" block (kickoff-level reminder, 因 sub-batch handoff state 是 dispatch-time 必须 inline-prepend, prompt 文件本身不能预知 sister sub-batch 终态)
- 保留 §2 G-MS-13 Finding ID Range Cross-Validation 段 (kickoff-level template)

### 同样 edit batch_27/28_kickoff.md + reconciler_kickoff_round5.md

### Edit `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md`
若 master protocol 文件引用 v1.2 → bump v1.3

═══════════════════════════════════════════════════════════════════
## STEP 5 — Update Index Files (Chain B)
═══════════════════════════════════════════════════════════════════

1. **`.work/06_deep_verification/_progress.json`**:
   - 加 `v1_3_cut_completed: "<date>"` 字段
   - Update recovery_hint: 加 "v1.3 cut completed <date>; inline-prepend overhead retired" 段
   - status string: append `_v1_3_cut_completed`

2. **`.work/06_deep_verification/PLAN.md`** v0.5 → v0.6 (若引用 v1.2):
   - bump 版本 + note "v1.3 prompts active 2026-04-XX"
   - keep v0.5 changelog history

3. **`CLAUDE.md` Key Paths table**:
   - 06 Deep Verification 旁枝入口 entry: 替换 "v1.2 schema frozen + v1.2 prompts" → "v1.2 schema frozen + v1.3 prompts active <date>"
   - 06 Deep Verification v1.2 prompts entry: 替换 v1.2 → v1.3 path + add v1.2 archived path

4. **`.work/06_deep_verification/subagent_prompts/v1.3_patch_candidates.md`**:
   - 顶部 prepend "STATUS: EXECUTED <date> — see v1.3 prompts in parent dir"
   - cleanup 候选 (但本 cut 不删, 保留作 trace)

5. **`.work/MANIFEST.md`** header:
   - update "最后更新" line append v1.3 cut entry

6. **`.work/meta/worklog.md`**:
   - 加 entry "<date> v1.3 prompt formal cut + archive v1.2 + retire inline-prepend overhead"

7. **`docs/PROGRESS.md`** header:
   - update with v1.3 cut completion

═══════════════════════════════════════════════════════════════════
## STEP 6 — Commit + Push + User Report
═══════════════════════════════════════════════════════════════════

### Commit (single commit, descriptive message)
```bash
git add .work/06_deep_verification/subagent_prompts/ \
  .work/06_deep_verification/_progress.json \
  .work/06_deep_verification/PLAN.md \
  .work/06_deep_verification/multi_session/ \
  .work/MANIFEST.md \
  .work/meta/worklog.md \
  CLAUDE.md \
  docs/PROGRESS.md

git commit -m "06 Deep Verification v1.3 prompt formal cut + archive v1.2 + retire inline-prepend overhead (4 v1.3 prompts: P0_writer_pdf/P0_writer_md/P0_matcher/P0_reviewer; 13 codification items A-M including R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6/b dual-form + NEW7 L6 procedural sub-batch handoff PRIORITY round 3+4 RECURRENCE formal mandatory + NEW7 L4 group-container precedent round 4 + NEW8.b SENTENCE-trigram + NEW8.c TABLE_HEADER column-set + G-MS-12 density alarm + G-MS-12.a content-type-aware floor + G-MS-13 cross-validation table; reviewer <slot> verdict <PASS/CONDITIONAL_PASS>; v1.2 archived to archive/v1.2_final_<date>/; batch 26+ kickoff §2 切到 v1.3 reference)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"

git push origin main
```

### User-facing summary (单 echo + 5-8 sentence summary)
```
V1_3_CUT_DONE prompts=4 reviewer_slot=<X> verdict=<PASS|CONDITIONAL_PASS> archive_path=archive/v1.2_final_<date>/ inline_prepend_retired=true
```

Summary 含: 4 v1.3 prompts 写完 + reviewer 总判 + 13 codification items (A-M) coverage + 关键 sticking points (NEW7 L6 procedural mandatory) + archive path + batch 26+ kickoff 切换状态 + 后续效益 (~5-7 hours overhead retired across 30+ batches).

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 主 session 自审 v1.3 prompts (Rule D 违规)
- 改 schema (frozen v1.2 carry-forward)
- 改 PLAN v0.5 内容 (only version bump if needed)
- 删 v1.2 primary 副本 (archive 是 copy 不是 move)
- 跑额外 PDF atomization / Rule A audit (本任务 prompt-only)
- Touch root pdf_atoms.jsonl / audit_matrix.md (除 STEP 5 _progress.json + audit_matrix.md 引用更新 if any)

═══════════════════════════════════════════════════════════════════
## 验收标准
═══════════════════════════════════════════════════════════════════

- ✅ 4 v1.3 prompt files exist (P0_writer_pdf_v1.3.md + P0_writer_md_v1.3.md + P0_matcher_v1.3.md + P0_reviewer_v1.3.md)
- ✅ 13 codification items (A-M) all present + verifiable in v1.3 main writer prompt
- ✅ Independent reviewer (different subagent_type, NOT main session) PASS verdict
- ✅ v1.2 archived to `archive/v1.2_final_<date>/` (4 files copied)
- ✅ batch 26+ kickoff §2 切换 v1.3 reference (4 kickoff files updated)
- ✅ 7 index files synced (_progress.json + PLAN + CLAUDE.md Key Paths + v1.3_patch_candidates.md + MANIFEST.md + worklog.md + docs/PROGRESS.md)
- ✅ Single commit pushed to origin/main
- ✅ User-facing summary echoed

The boulder never stops. 第一步 STEP 0 并行 10-file Read.
