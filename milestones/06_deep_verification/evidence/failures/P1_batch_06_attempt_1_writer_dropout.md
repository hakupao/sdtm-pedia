# P1 Batch 06 Attempt 1 — Writer Dropout Failure

> Date: 2026-04-25
> Rule: Rule B (失败归档不删)
> Artifact (raw output): `P1_batch_06_attempt_1_writer_dropout.jsonl` (13 KB, 27 atoms, DO NOT merge to root)

---

## 输入

- Writer subagent_type: `oh-my-claudecode:writer` (per 2-type alternation: batch 05 executor → 06 writer)
- Model: sonnet (inherited)
- Scope: SDTMIG v3.4 (no header footer).pdf, pages 51-60
- Prompt: `P0_writer_pdf_v1.2` + batch06_4digit_fix inline
- Expected: ~300 atoms (per prior batch 01-05 avg 26.9-33.0 atoms/页)
- Dispatched: 2026-04-25, 9 min 27 sec wall (566,452 ms)

## 产物 (raw)

- Total atoms: **27** (9% of expected ~300)
- Failures reported: 0 (writer returned `DONE pages=51-60, atoms=27, failures=0` — no self-reported failure)
- Atom_type coverage: **3/9** (SENTENCE 6 / HEADING 18 / LIST_ITEM 3), missing TABLE_HEADER, TABLE_ROW, CODE_LITERAL, CROSS_REF, FIGURE, NOTE
- Per-page distribution:
  - p.51: 11 (normal density — full content covered)
  - p.52: 2 (SENTENCE about --ORRES only)
  - p.53-55, 57-60: 1-3 each (HEADING-only, no content)
  - p.56: 1 (heading only)

## 技术判定 (schema / format)

- JSON well-formed: ✅ 27/27
- atom_id format: ✅ 4-digit page 0-pad correct
- atom_type ∈ 9-enum: ✅ all 3 used types valid
- **但**: `parent_section` 字段**格式 bug** — 双 `§` 前缀 (e.g. `§§4.4 [Linking and Disease Milestones]`) + 方括号标题形式不一致 (spec requires `§X.Y [TITLE]` 单 §). 前 batch 01-05 未见此 bug.

## 业务判定 (完整性 / 质量)

- **FAIL — 严重内容缺失**
- 写手似乎只正常处理了 p.51, 然后对 p.52 做了最小 SENTENCE 覆盖, 剩余 p.53-60 仅抽出节标题 (HEADING), 完全没有抽取正文 SENTENCE / LIST_ITEM / TABLE_ROW 等
- p.53 的 `4.5.1.3 Examples of Original and Standard Units and Test Not Done` 是 example 段, 正文必有 TABLE_HEADER + TABLE_ROW (batch 02-04 模式确证), 本次完全跳过
- 无 FAILURE_... 行, 写手没有自知失败, 返回 `failures=0` 但实际产出空洞
- 对比 batch 05 同 writer type 同样 prompt, batch 05 p.41-50 产 327 atoms 正常覆盖 — 故**非 writer type 固有问题**, 是该 subagent 实例单次 dropout 行为

## Root cause 假设 (hypothesis, 待下次 attempt 排除)

1. **H1**: Subagent 内部预算 / context 限制, p.51 后渐漸 "cutting corners" (心理模型省力)
   - 证据: 28 tool_uses for 10 pages 暗示 Read tool call 可能只跑了 ~10 次 (1/页), 然后 Write 调用减少
   - 证据 2: total_tokens 142K, 不算低但 output tokens 显然集中 p.51
2. **H2**: Read tool 对 p.53-60 某些页返回内容解析失败, 写手静默降级为 "TOC-like HEADING only" 兜底
   - 反驳: 若 Read 失败应写 FAILURE_ig34_p<NNNN> 行 per prompt §失败情形, 未写
3. **H3**: 写手把 batch 任务误解为 "outline mode", 逐页只抽标题
   - 可能, 但 p.51 的完整模式证明写手理解正确语义, 后续是放弃而非误解
4. **H4**: 非确定性 LLM 行为, 单次 run 偶发, 重跑相同参数可能正常

## 下一 attempt 输入候选

**选项 A**: 原 type 原 prompt 重跑, 测 H4 (non-determinism 单次偶发)
- 风险: 再次失败可能浪费时间; 但成本低且能证伪 H1/H2/H3 之一
- 推荐 if 用户接受一次重试

**选项 B**: 换 type 重跑 (用 executor 违反 2-type alternation 严格约束, 但测 H1)
- 若 executor 产 ~300 atoms 正常 → 证实 writer 实例问题或 type 偶发, 不升 systemic
- 若 executor 也产空洞 → H1/H4 均否, 升 systemic (prompt / model 问题)
- 本次 executor 复用代价: roster 链断 alternation, 但 2-type 池本身不排斥 executor 连 (batch 05 = executor, batch 06 = executor 算同 type 连续), 需 §B.2 "连续 2 batch 禁用同 type" 硬约束让步

**选项 C**: 把 batch 06 拆 2 个 mini-batch (p.51-55 + p.56-60, 各 5 页) 2 个 writer 并行派
- 承载 user 刚才的并行建议
- 每个 agent 管 5 页, context 压力减半, 降 H1 风险
- 失败风险独立, 一个挂另一个可能还好
- 2 writer 可用 executor + writer 满足 alternation (内部独立 slot)

**选项 D**: 保留 p.51 的 11 atom (看起来正常), 从 p.52 起派新 writer 重跑 p.52-60 9 页
- 节约 10% 已产正确数据
- 风险: 抽样 Rule A 会"看不到" p.51 失败的 a003 HEADING `Linking and Disease Milestones` (missing heading_level/sibling_index — 需复查) — 若 p.51 输出本身 schema 完整也可

---

## Rule B 归档事实

- 产物 moved 至 `evidence/failures/P1_batch_06_attempt_1_writer_dropout.jsonl` (非 checkpoints/)
- 未 merge 到 root pdf_atoms.jsonl (root 保持 1575)
- `_progress.json` batches_done 维持 5 (不 increment 直到 attempt 2+ 产可合格产物)
- 本 md 为 Rule B 要求的 failures/ 技术+业务判定 记录

## 待决 (用户决策点)

用户刚说"遇到重大分歧点或需要向我报告的, 停下来问我". 本 attempt 是重大分歧 (327 → 27 atom 突降), 申请决策选项 A/B/C/D.
