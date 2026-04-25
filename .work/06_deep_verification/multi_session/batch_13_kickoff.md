# Batch 13 Kickoff (Multi-Session Parallel — Session B)

> 你是 multi-session parallel 实验的 **session B (batch 13)**.
> 同时还有 session C (batch 14) + session D (batch 15) 在其他终端跑.
> 你只负责 p.121-130, 不动 root 文件 / audit_matrix / _progress.json.

═══════════════════════════════════════════════════════════════════
## STEP 0 — 必读 (并行 4 文件)
═══════════════════════════════════════════════════════════════════

并行 Read 以下文件 (本 session 不读 MANIFEST/worklog/issues_found, 直接进 P1 旁枝):

1. `.work/06_deep_verification/multi_session/MULTI_SESSION_PROTOCOL.md` (full — 你的协议)
2. `.work/06_deep_verification/audit_matrix.md` (READ-ONLY, 看 Rule D roster + 历史 batch 模式)
3. `.work/06_deep_verification/evidence/checkpoints/P1_batch_12_report.md` (上批 lessons)
4. `.work/06_deep_verification/subagent_prompts/v1.3_patch_candidates.md` (cumulative R-rules 候选)

读完报告: 当前 pages_done=120 / atoms_done=3200 / batches_done=12 / findings=35 / Rule D=21. 你将贡献 batch 13.

═══════════════════════════════════════════════════════════════════
## STEP 1 — TOC Ground Truth (已 PDF p.4 提取, 直接用)
═══════════════════════════════════════════════════════════════════

TOC for batch 13 + 边界:

| § | Title | Pages | Heading Level | Sibling Index |
|---|---|---|---|---|
| §6.1.3.3 | Exposure/Exposure as Collected Examples | p.111-120 | L4 sib=3 under §6.1.3 | (上 batch 12 已处理, batch 13 不动) |
| **§6.1.4** | **Meal Data (ML)** | **p.121-124** | **L3 sib=4 under §6.1** | **batch 13 SCOPE 起头** |
| **§6.1.5** | **Procedures (PR)** | **p.125-128** | **L3 sib=5 under §6.1** | **batch 13 SCOPE 中** |
| **§6.1.6** | **Substance Use (SU)** | **p.129-132 (p.131-132 入 batch 14)** | **L3 sib=6 under §6.1** | **batch 13 SCOPE 末 (p.129-130 仅)** |
| §6.2 | MODELS FOR EVENTS DOMAINS | p.133 | L2 sib=2 under §6 | (batch 14 处理) |

### parent_section 规则 (R5 anchor):
- p.121-124 atoms → `§6.1.4 [Meal Data (ML)]` (除 §6.1.4 heading 自己 → `§6.1 [Models for Interventions Domains]`)
- p.125-128 atoms → `§6.1.5 [Procedures (PR)]` (除 §6.1.5 heading 自己 → `§6.1 [Models for Interventions Domains]`)
- p.129-130 atoms → `§6.1.6 [Substance Use (SU)]` (除 §6.1.6 heading 自己 → `§6.1 [Models for Interventions Domains]`)

### Sub-headings 内部 convention (各 domain 起头页):
- 每 domain 起头有: `<DOMAIN> – Description/Overview` (HEADING L4 sib=1) + `<DOMAIN> – Specification` (HEADING L4 sib=2) + `<DOMAIN> – Assumptions` (HEADING L4 sib=3) + `<DOMAIN> – Examples` (HEADING L4 sib=4) [若有]
- 类似前 batch §6.1.1 AG / §6.1.2 CM / §6.1.3.1 EX 等 pattern
- ⚠️ ML/PR/SU 都是 L3 (`§6.1.4`/`§6.1.5`/`§6.1.6`), 子 sub-heading L4 sib=1/2/3/4 (depth+1 convention from batch 11 O-P1-29)

═══════════════════════════════════════════════════════════════════
## STEP 2 — Dispatch Strategy (Option C parallel, alternation)
═══════════════════════════════════════════════════════════════════

Per O-P1-13 default + alternation pattern (batch 12 = executor+writer, batch 13 切换):

- **13a = `oh-my-claudecode:writer` × p.121-125** (writer 家族先验 R14 fix continuity post 12b breakthrough)
- **13b = `oh-my-claudecode:executor` × p.126-130**

并行派 (单 message 双 Agent tool call). 每 agent 收到完整 self-contained prompt 含 14 R-rules + R15 NEW + TOC anchor for batch 13 + heading_level convention table + 9-enum gate + JSONL schema + R14 self-validation reminder.

### Cross-Batch Sibling Continuity Pre-Context (R15 NEW)

⚠️ Prepend 到两个 writer prompt: "Prior batch (12) terminal HEADING context for sibling continuity:
- Last `Example N` sibling: Example 8 sib=8 under §6.1.3.3 (p.119)
- §6.1.3.3 itself: L4 sib=3 under §6.1.3 (p.111)
- §6.1.3 itself: L3 sib=3 under §6.1 (p.103)
- §6.1.2 [CM]: L3 sib=2 under §6.1 (p.98)
- §6.1.1 [AG]: L3 sib=1 under §6.1 (p.92)

Therefore in batch 13:
- §6.1.4 [ML] = L3 sib=4 under §6.1 (NEW, sib continuity from §6.1.3 sib=3)
- §6.1.5 [PR] = L3 sib=5 (NEW)
- §6.1.6 [SU] = L3 sib=6 (NEW)

Within each new domain, sub-heading numbering RESTARTS at sib=1 for that domain's own L4 children."

═══════════════════════════════════════════════════════════════════
## STEP 3 — Schema Validation (post-DONE, before Rule A)
═══════════════════════════════════════════════════════════════════

每 batch DONE 后, 主 session 串 Bash + Python 检:
1. `wc -l` 各 batch file vs DONE atoms=N 严格一致 (R7+R14)
2. JSON parse + 9-enum atom_type + R1 atom_id 4-digit/3-digit format
3. parent_section vs TOC anchor 一致性
4. atom_id 内 batch + 跨 batch (13a vs 13b) 0 collision
5. **不要** 检 vs root pdf_atoms.jsonl (那是 reconciler 的事)
6. heading_level + sibling_index discipline (L3 §6.1.4-6.1.6 / L4 sub-headings sib 重置)

发现问题 → Option H inline 修 (在 batch file 自己范围内, 不动 root).

═══════════════════════════════════════════════════════════════════
## STEP 4 — Drift Cal: NOT triggered batch 13
═══════════════════════════════════════════════════════════════════

Per cadence "every 3 batches", last cal batch 12 p.118, next mandatory batch 15 (session D 处理). 你跳过.

⚠️ 例外: 若 schema validation 中发现 dense TABLE_ROW 页 anomaly (e.g. atom count vs PDF 严重不匹配, suspected page-shift 类 batch 12 p.118/p.119), 主 session 可 ad-hoc 触发 Option E rerun 该单页 — 同 batch 11 p.103 / batch 12 p.119 precedent. **不要** 无理由触发 drift cal.

═══════════════════════════════════════════════════════════════════
## STEP 5 — Rule A Audit (slot #22 = vercel:performance-optimizer AUDIT-mode)
═══════════════════════════════════════════════════════════════════

预分配 reviewer (Rule D unique, 不可改): `vercel:performance-optimizer`

派发 prompt 显式 "Mode: AUDIT, NOT performance optimization. You are an INDEPENDENT REVIEWER for PDF atomization quality. Do NOT analyze performance, do NOT touch code." (类 slot #20 code-simplifier / #21 debugger AUDIT pivot pattern).

### Sample build (Bash + Python):
- Seed = 20260470
- 10 atoms 1/page stratified (p.121-130)
- Atom_type 优先: TABLE_ROW × 5-6 (R11 trailing empty + R8 empty cell 验证) + HEADING × 2-3 (sib continuity 验证 §6.1.4/5/6 起头 + sub-heading L4 sib=1) + 其他 1-2
- 输出 `rule_a_batch_13_sample.jsonl`

### Reviewer prompt (类 batch 12 #21 prompt 结构) 含:
- 4-dimension verdict (atom_type / verbatim / parent_section / heading_level+sibling_index)
- TOC ground truth prepend (§6.1.4 / §6.1.5 / §6.1.6 anchors)
- 14+1 R-rules embedded (R1-R14 + R15 NEW cross-batch sibling continuity)
- Output: `rule_a_batch_13_verdicts.jsonl` + `rule_a_batch_13_summary.md`
- Final message: `RULE_A_DONE pass=N partial=N fail=N weighted=X.XX`
- Threshold ≥90% weighted → PASS; ≥80% <90% → CONDITIONAL_PASS (你需 Option H 修 + verify); <80% → FAIL halt + report 等 reconciler 决定

═══════════════════════════════════════════════════════════════════
## STEP 6 — Repair (if any finding)
═══════════════════════════════════════════════════════════════════

按 Rule A finding 严重度:
- HIGH/MEDIUM → Option H inline 修 in your batch file (类 batch 12 4-atom drift cal Option H pattern)
- LOW non-blocking → defer 到 reconciler / Phase 4a (类 F-12-02 BOTTLE\\n2 defer pattern)
- 系统性 / page-shift 类 → Option E mini-rerun (oh-my-claudecode:executor × N 单页) wholesale replace (类 batch 12 p.119 31-atom rerun)

每个 repair backup pre-fix 文件 (Rule B): `pdf_atoms_batch_13[ab].jsonl.pre-<reason>.bak`

═══════════════════════════════════════════════════════════════════
## STEP 7 — Sub-progress + Batch Report
═══════════════════════════════════════════════════════════════════

写 `.work/06_deep_verification/evidence/checkpoints/_progress_batch_13.json`:
```json
{
  "batch_id": 13,
  "session_id": "B",
  "status": "completed",
  "pages": "121-130",
  "atoms": <N>,
  "atoms_a": <Na>,
  "atoms_b": <Nb>,
  "writer_a_type": "oh-my-claudecode:writer",
  "writer_b_type": "oh-my-claudecode:executor",
  "reviewer_slot": 22,
  "reviewer_type": "vercel:performance-optimizer",
  "rule_a_pass": <N>,
  "rule_a_partial": <N>,
  "rule_a_fail": <N>,
  "rule_a_weighted": <float>,
  "rule_a_verdict": "PASS|CONDITIONAL_PASS|FAIL",
  "drift_cal_triggered": false,
  "drift_cal_reason": "every-3-batches cadence skip; next at batch 15 (session D)",
  "repair_cycles": <N>,
  "findings_added": ["O-P1-36 ...", "O-P1-37 ..."],
  "atom_type_dist": {"HEADING": ..., "SENTENCE": ..., ...},
  "parent_section_dist": {...},
  "atom_id_collision_within_batch": 0,
  "writer_a_done_strict_match": true,
  "writer_b_done_strict_match": true,
  "frame_tag_contamination": 0,
  "files_written": [
    "pdf_atoms_batch_13a.jsonl",
    "pdf_atoms_batch_13b.jsonl",
    "_progress_batch_13.json",
    "P1_batch_13_report.md",
    "rule_a_batch_13_sample.jsonl",
    "rule_a_batch_13_verdicts.jsonl",
    "rule_a_batch_13_summary.md"
  ],
  "files_NOT_touched": [
    "pdf_atoms.jsonl (root)",
    "audit_matrix.md",
    "_progress.json"
  ],
  "last_updated": "2026-04-25"
}
```

写 `.work/06_deep_verification/evidence/checkpoints/P1_batch_13_report.md` (类 batch 12 report 结构: Metrics + Execution summary + Rule A gate + Findings added + Post-batch state + Session budget + Handoff to reconciler).

═══════════════════════════════════════════════════════════════════
## STEP 8 — Final Message
═══════════════════════════════════════════════════════════════════

Echo 单行 (类 batch agent DONE format, 给 reconciler 读):
```
PARALLEL_SESSION_13_DONE atoms=<N> failures=<F> repair_cycles=<C> rule_a=<weighted>% drift_cal=skipped findings_added=<list>
```

═══════════════════════════════════════════════════════════════════
## Halt Conditions (per protocol)
═══════════════════════════════════════════════════════════════════

任一触发 halt + 详细 report 等 reconciler 决定:
- writer failure rate >15%
- Rule A raw <70% (CONDITIONAL_PASS 仍可 continue, 但 Option H 修 + 文档)
- ctx 用量 >80%
- 预分配 reviewer `vercel:performance-optimizer` 不可派发 (e.g. agent type not registered)
- 任何尝试触动 root pdf_atoms.jsonl / audit_matrix.md / _progress.json 的 code path → halt 立即

═══════════════════════════════════════════════════════════════════
## NEVER DO
═══════════════════════════════════════════════════════════════════

- 写 root `pdf_atoms.jsonl` (留 reconciler)
- 写 `audit_matrix.md` (留 reconciler)
- 写 `_progress.json` (留 reconciler)
- cut formal v1.3 prompt (留 reconciler 决定)
- Self-pick reviewer slot (用 #22 vercel:performance-optimizer hardcoded, 不撞)
- Touch sister batch (14/15) files
- Touch CLAUDE.md / MEMORY / project meta files
- Skip TOC anchor prepend (4 consecutive batch 验证 0 inversion 不能丢)
- Skip R14 wc -l self-validation step in writer prompts
- Modify any *.bak backup file
- Run `git commit` / `git push` (留 user 决定)

开干. 第一步 STEP 0 并行 4-file Read.
