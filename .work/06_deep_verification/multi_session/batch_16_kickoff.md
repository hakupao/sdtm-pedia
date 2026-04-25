# Batch 16 Kickoff (Multi-Session Parallel — Session B, Round 2)

> 你是 multi-session parallel 实验 round 2 的 **session B (batch 16)**.
> 同时还有 session C (batch 17) + session D (batch 18) 在其他终端跑.
> 你只负责 p.151-160, 不动 root 文件 / audit_matrix / _progress.json.
> Round 2 实验 — 吸收 round 1 (batches 13-15) MULTI_SESSION_RETRO.md G-MS-4 (halt fallback) + G-MS-7 (finding ID range pre-allocation) 两条缺口修.

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 (并行 5 文件)
═══════════════════════════════════════════════════════════════════

并行 Read (本 session 不读 MANIFEST/worklog/issues_found, 直接进 P1 旁枝):

1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (round 1 master 协议, 你 round 2 沿用)
2. `.work/06_deep_verification/multi_session/MULTI_SESSION_RETRO.md` (round 1 retro 三段式, 重点 §2 G-MS-4 + G-MS-7 你必须修的两条缺口)
3. `.work/06_deep_verification/audit_matrix.md` (READ-ONLY, 看 Rule D roster 24 + 历史 batch 模式)
4. `.work/06_deep_verification/evidence/checkpoints/P1_batch_15_report.md` (上批 lessons + drift cal value-add 5th 案例)
5. `.work/06_deep_verification/subagent_prompts/v1.3_patch_candidates.md` (cumulative R-rules + NEW1-NEW5)

读完报告: 当前 pages_done=150 / atoms_done=3877 / batches_done=15 / findings=39 / Rule D=24. 你将贡献 batch 16.

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth (PDF p.4 + page_index.json verified, 直接用)
═══════════════════════════════════════════════════════════════════

⚠️ Batch 16 含 **1 chapter-internal transition** (§6.2.3 CE → §6.2.4 DS at p.155). R12 transition discipline 高压.

| § | Title | Pages (page_index.json) | Heading Level | Sibling Index |
|---|---|---|---|---|
| §6.2.3 | Clinical Events (CE) | p.148-155 (p.151-155 batch 16 SCOPE 起头, p.148-150 已 batch 15 处理) | L3 sib=3 under §6.2 | (heading 在 p.148 batch 15, batch 16 仅 CE tail content) |
| **§6.2.4** | **Disposition (DS)** | **p.155-167 (p.155-160 batch 16 SCOPE 中末)** | **L3 sib=4 under §6.2** | **batch 16 SCOPE NEW** |
| §6.2.5 | Healthcare Encounters (HO) | p.167-171 | L3 sib=5 under §6.2 | (batch 17 处理) |

### parent_section 规则 (R5 anchor):
- p.151-154 atoms → `§6.2.3 [Clinical Events (CE)]` (CE tail content, including CE Examples N if any continuation from p.148-150)
- p.155 atoms (transition page possibility, **R12 critical**):
  - CE last bit if any → `§6.2.3 [Clinical Events (CE)]`
  - §6.2.4 heading 自己 → `§6.2 [MODELS FOR EVENTS DOMAINS]`
  - DS Description/Overview/Spec content → `§6.2.4 [Disposition (DS)]`
- p.156-160 atoms → `§6.2.4 [Disposition (DS)]` (除 sub-headings 自己)

### Sub-headings convention (depth +1):
- §6.2.3 sub: L4 sib=1/2/3/4/5 (CE – Description/Overview / Specification / Assumptions / Examples / References — note batch 15 set References sib=5 per R15 sweep) — heading 在 batch 15, batch 16 仅 CE tail content
- §6.2.4 sub: L4 sib=1/2/3/4 (DS – Description/Overview / Specification / Assumptions / Examples 若有)

### Cross-Batch Sibling Continuity Pre-Context (R15 NEW)

⚠️ Prepend 到两个 writer prompt: "Prior batches HEADING continuity (post round-1 reconciler merge):
- §6.2 [MODELS FOR EVENTS DOMAINS] = L2 sib=2 under §6 (set in batch 14 p.133)
- §6.2.1 [Adverse Events (AE)] = L3 sib=1 under §6.2 (batch 14)
- §6.2.2 [Biospecimen Events (BE)] = L3 sib=2 under §6.2 (batch 15)
- §6.2.3 [Clinical Events (CE)] = L3 sib=3 under §6.2 (batch 15 起头 p.148)
- §6.2.4 [Disposition (DS)] = L3 sib=4 under §6.2 (NEW in batch 16, sib continuity from §6.2.3 sib=3)
- (CE Examples N sibling sequence inside §6.2.3 if any continuation — sib chain from batch 15 baseline; batch 16 continues sib=N+1 if more CE Examples)
- DS Examples N sibling RESTARTS from sib=1 within §6.2.4 (independent of CE Examples sequence)"

═══════════════════════════════════════════════════════════════════
## STEP 2 — Dispatch Strategy (Option C parallel, alternation)
═══════════════════════════════════════════════════════════════════

Per O-P1-13 default + alternation pattern (batch 15 = executor+writer 测试 transition page, batch 16 切换):

- **16a = `oh-my-claudecode:writer` × p.151-155** (writer 家族先验 R14 fix continuity post 12b/13a/14a/15a writer-family converged strict-match pattern; R12 critical p.155 CE→DS transition)
- **16b = `oh-my-claudecode:executor` × p.156-160**

并行派 (单 message 双 Agent tool call). 每 agent 收到完整 self-contained prompt 含 15 R-rules + R15 sibling context for batch 16 + heading_level convention table + 9-enum gate + JSONL schema + R14 self-validation reminder + NEW2 spec-table char-level self-validation reminder.

### R12 Transition Discipline (HIGH PRESSURE for p.155)

⚠️ p.155 含 **2-3 个区** (R12 critical):
1. §6.2.3 CE tail content (若有, 跨 p.154/p.155 boundary — CE Examples N 收尾或 References 收尾)
2. §6.2.4 [Disposition (DS)] sub-section HEADING (L3 sib=4) + DS Description/Overview/Specification 起头

writer 必须 atomize 全部 physical content top-to-bottom 不漏 CE tail (类 batch 14 p.133 §6.1.6 SU tail + §6.2 + §6.2.1 chapter-level 3-zone transition CLEAN precedent + batch 15 p.143 §6.2.1→§6.2.2 BE chapter transition CLEAN precedent — NEW5 R12 strengthening 已 v1.3 candidate).

═══════════════════════════════════════════════════════════════════
## STEP 3 — Schema Validation (post-DONE, before Rule A)
═══════════════════════════════════════════════════════════════════

每 batch DONE 后, 主 session 串 Bash + Python 检:
1. `wc -l` 各 batch file vs DONE atoms=N 严格一致 (R7+R14)
2. JSON parse + 9-enum atom_type + R1 atom_id 4-digit/3-digit format
3. parent_section vs TOC anchor 一致性 (§6.2.3 vs §6.2.4 vs §6.2 partition)
4. atom_id 内 batch + 跨 batch (16a vs 16b) 0 collision
5. **不要** 检 vs root pdf_atoms.jsonl (那是 reconciler 的事)
6. heading_level + sibling_index discipline (L3 §6.2.4 sib=4 / L4 sub-headings sib 重置)
7. R12 transition page p.155 atom count >= 8 sanity-check + parent_section 区分清楚 CE tail vs §6.2.4 heading vs DS sub-content

发现问题 → Option H inline 修 (在 batch file 自己范围内, 不动 root). 系统性 / page-shift 类 → Option E mini-rerun.

═══════════════════════════════════════════════════════════════════
## STEP 4 — Drift Cal: NOT triggered batch 16
═══════════════════════════════════════════════════════════════════

Per cadence "every 3 batches", last cal batch 15 p.147, next mandatory batch 18 (session D 处理). 你跳过.

⚠️ 例外 (ad-hoc trigger): 若 schema validation 中发现 dense TABLE_ROW 页 anomaly (e.g. atom count vs PDF 严重不匹配, suspected page-shift / under-extraction / writer-family typo cluster — 类 batch 14 p.137 / batch 15 p.146 precedent), 主 session 可 ad-hoc 触发 Option E rerun 该单页 — 同 7 successful Option E precedents (p.60 / p.103 / p.119 / p.124 / p.136-140 batch / p.146 / p.147 / p.148). **不要** 无理由触发 drift cal.

═══════════════════════════════════════════════════════════════════
## STEP 5 — Rule A Audit (slot #25 = plugin-dev:agent-creator AUDIT-mode)
═══════════════════════════════════════════════════════════════════

预分配 reviewer (Rule D unique, **HARDCODED 不可改, round 2 partition**): `plugin-dev:agent-creator`

派发 prompt 显式 "Mode: AUDIT for PDF atomization quality, NOT agent creation. You are an INDEPENDENT REVIEWER for SDTMIG v3.4 PDF atomization quality. Do NOT create agents, do NOT propose plugins, do NOT touch agent configuration files. Tools: Read + Write only — output verdicts JSONL + summary md to designated paths." (类 slot #20 code-simplifier / #21 debugger / #22 performance-optimizer / #23 designer / #24 deployment-expert AUDIT pivot pattern; **6th AUDIT-mode pivot, plugin-dev family FIRST burn**).

### Sample build (Bash + Python):
- Seed = 20260485
- 10 atoms 1/page stratified (p.151-160)
- Atom_type 优先: TABLE_ROW × 5-6 (R11 trailing empty + R8 empty cell + DS spec table 验证) + HEADING × 2-3 (R12 transition validation §6.2.4 sib=4 起头 + sub-heading L4 sib=1) + 其他 1-2
- 输出 `rule_a_batch_16_sample.jsonl`

### Reviewer prompt (类 batch 13-15 #22-#24 prompt 结构) 含:
- 4-dimension verdict (atom_type / verbatim / parent_section / heading_level+sibling_index)
- TOC ground truth prepend (§6.2.3 / §6.2.4 anchors)
- 15 R-rules embedded (R1-R15 cumulative)
- Output: `rule_a_batch_16_verdicts.jsonl` + `rule_a_batch_16_summary.md`
- Final message: `RULE_A_DONE pass=N partial=N fail=N weighted=X.XX`
- Threshold ≥90% weighted → PASS; ≥80% <90% → CONDITIONAL_PASS (你需 Option H 修 + verify); <80% → FAIL halt + report 等 reconciler 决定 (per round 2 G-MS-4 halt fallback, 见下)

═══════════════════════════════════════════════════════════════════
## STEP 6 — Repair (if any finding)
═══════════════════════════════════════════════════════════════════

按 Rule A finding 严重度:
- HIGH/MEDIUM → Option H inline 修 in your batch file (类 batch 13 p.123/p.127 Option H pattern)
- LOW non-blocking → defer 到 reconciler / Phase 4a (类 F-12-02 BOTTLE\\n2 defer pattern)
- 系统性 / page-shift 类 → Option E mini-rerun (oh-my-claudecode:executor × N 单页) wholesale replace (类 batch 13 p.124 22-atom rerun / batch 14 p.136-140 full-batch rerun / batch 15 p.146/p.147/p.148 wholesale rerun)

每个 repair backup pre-fix 文件 (Rule B): `pdf_atoms_batch_16[ab].jsonl.pre-<reason>.bak`

⚠️ Round 2 G-MS-5 NEW lesson absorbed: Option E rerun prompt 必须显式要求 (a) outer-pipe `| field1 | ... |` for TABLE_ROW + TABLE_HEADER + (b) explicit `heading_level: null` + `sibling_index: null` keys for non-HEADING atoms (NEW3 v1.3 candidate, 已 batch 14 O-P1-37 + batch 15 outer-pipe normalization 验证). 防止重蹈 batch 14 91-atom bulk Option H 修工作.

═══════════════════════════════════════════════════════════════════
## STEP 7 — Sub-progress + Batch Report
═══════════════════════════════════════════════════════════════════

写 `.work/06_deep_verification/evidence/checkpoints/_progress_batch_16.json`:
```json
{
  "batch_id": 16,
  "session_id": "B",
  "round": 2,
  "status": "completed",
  "pages": "151-160",
  "atoms": <N>,
  "atoms_a": <Na>,
  "atoms_b": <Nb>,
  "writer_a_type": "oh-my-claudecode:writer",
  "writer_b_type": "oh-my-claudecode:executor",
  "reviewer_slot": 25,
  "reviewer_type": "plugin-dev:agent-creator",
  "reviewer_audit_pivot_index": 6,
  "reviewer_family_first_burn": true,
  "reviewer_family_name": "plugin-dev",
  "rule_a_pass": <N>,
  "rule_a_partial": <N>,
  "rule_a_fail": <N>,
  "rule_a_weighted": <float>,
  "rule_a_verdict": "PASS|CONDITIONAL_PASS|FAIL",
  "drift_cal_triggered": false,
  "drift_cal_reason": "every-3-batches cadence skip; next mandatory at batch 18 (session D)",
  "repair_cycles": <N>,
  "findings_added": ["O-P1-40 ...", "O-P1-41 ..."],
  "finding_id_range_allocated": "O-P1-40..43 (round 2 G-MS-7 pre-allocation, batch 16 reserved 4 IDs)",
  "atom_type_dist": {"HEADING": ..., "SENTENCE": ..., ...},
  "parent_section_dist": {...},
  "atom_id_collision_within_batch": 0,
  "writer_a_done_strict_match": true,
  "writer_b_done_strict_match": true,
  "frame_tag_contamination": 0,
  "r12_transition_p155_clean": true,
  "files_written": [
    "pdf_atoms_batch_16a.jsonl",
    "pdf_atoms_batch_16b.jsonl",
    "_progress_batch_16.json",
    "P1_batch_16_report.md",
    "rule_a_batch_16_sample.jsonl",
    "rule_a_batch_16_verdicts.jsonl",
    "rule_a_batch_16_summary.md"
  ],
  "files_NOT_touched": [
    "pdf_atoms.jsonl (root)",
    "audit_matrix.md",
    "_progress.json"
  ],
  "last_updated": "2026-04-25"
}
```

写 `.work/06_deep_verification/evidence/checkpoints/P1_batch_16_report.md` (类 batch 13-15 report 结构: Metrics + Execution summary + Rule A gate + Findings added + Post-batch state + Session budget + Handoff to reconciler).

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message
═══════════════════════════════════════════════════════════════════

Echo 单行 (类 batch 13-15 DONE format, 给 reconciler 读):
```
PARALLEL_SESSION_16_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list of O-P1-40..43>
```

═══════════════════════════════════════════════════════════════════
## Round 2 Protocol Upgrade — G-MS-7 Finding ID Range Pre-allocation
═══════════════════════════════════════════════════════════════════

Round 1 缺口 G-MS-7: 各 session 用相同 O-P1-NN 累加 ID 易冲突 (round 1 batches 13/14/15 都从 O-P1-36 开始累, reconciler 必须 cross-scoping). Round 2 修:

- **Batch 16 (你)**: 预留 IDs **O-P1-40..43** (4 IDs reserved). 若你新 finding > 4, 用 IDs O-P1-40a/40b/40c suffix 子序列.
- Batch 17 (sister): 预留 IDs O-P1-44..47.
- Batch 18 (sister): 预留 IDs O-P1-48..51.
- Reconciler: 预留 IDs O-P1-52+ for cross-batch / cross-session findings (e.g. R15 sibling continuity sweep 揭).

按预分配 ID 写 `findings_added` 数组 + batch report. **不要** 用 round 1 sister-collision ID 模式 (O-P1-36..39 通用).

═══════════════════════════════════════════════════════════════════
## Round 2 Protocol Upgrade — G-MS-4 Halt Fallback Decision Tree
═══════════════════════════════════════════════════════════════════

Round 1 缺口 G-MS-4: sub-session halt 时 reconciler 决策树未 spec. Round 2 修 (per session 须遵守):

任一 halt condition 触发, **session 必须**:

1. **不要** 删除 partial work — 留所有 batch file / progress / sample / verdicts (Rule B 强制)
2. 写 `.work/06_deep_verification/multi_session/halt_state_batch_16.md` (类 retro 结构):
   - `halt_reason`: 哪个 condition 触发
   - `partial_state`: 当前 atoms / pages / repair cycles 截止
   - `incomplete_steps`: 哪些 STEP 未完
   - `recommended_fallback`: (a) reconciler retry 全 batch / (b) reconciler defer 本 batch + merge sister batches only / (c) reconciler abort experiment
   - `evidence_paths`: partial files 路径
3. echo 单行 (替代 PARALLEL_SESSION_16_DONE):
   ```
   PARALLEL_SESSION_16_HALT reason=<text> partial_atoms=<N> partial_pages=<list> recommended_fallback=<a|b|c>
   ```
4. 不要 etc 等 reconciler — 直接 exit. Reconciler 读 halt_state 决策.

═══════════════════════════════════════════════════════════════════
## Halt Conditions (per protocol, round 2 augmented)
═══════════════════════════════════════════════════════════════════

任一触发则 halt + 写 halt_state per G-MS-4:
- writer failure rate >15% in batch
- Rule A raw FAIL <70% (CONDITIONAL_PASS 仍可 continue, 但 Option H 修 + 文档)
- ctx 用量 >80%
- 预分配 reviewer `plugin-dev:agent-creator` 不可派发 (Rule D 撞风险) — Round 2 NEW: **不要** fallback 自选 alternative reviewer (会 round-2 cross-session Rule D 撞)
- 任何尝试触动 root pdf_atoms.jsonl / audit_matrix.md / _progress.json 的 code path → halt 立即

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 写 root `pdf_atoms.jsonl` (留 reconciler)
- 写 `audit_matrix.md` (留 reconciler)
- 写 `_progress.json` (留 reconciler)
- cut formal v1.3 prompt (留 reconciler / 专用 v1.3 cut session — round 1 retro D-MS-6 已说明)
- Self-pick reviewer slot (用 #25 plugin-dev:agent-creator hardcoded, 不撞)
- Touch sister batch (17/18) files
- Touch CLAUDE.md / MEMORY / project meta files
- Skip TOC anchor prepend (7 consecutive batch 验证 0 inversion 不能丢)
- Skip R14 wc -l self-validation step in writer prompts
- Skip NEW2 spec-table char-level self-validation reminder (writer 14b/15b 5 typos cluster lesson)
- Skip Option E rerun outer-pipe + null-key requirement (NEW3 v1.3 candidate)
- Modify any *.bak backup file
- Run `git commit` / `git push` (留 user 决定)
- Use round 1 ID reuse pattern (O-P1-36..39) — **必须** 用 round 2 G-MS-7 pre-allocation O-P1-40..43

开干. 第一步 STEP 0 并行 5-file Read.
