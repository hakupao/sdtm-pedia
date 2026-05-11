<!-- chain: F (深度验证旁枝链 v2)
  修改本文件后, 必须检查:
  → ../_progress.json                       (程序化进度: phases.P2 字段 + current_phase)
  → ../evidence/checkpoints/                (P2 pilot 快照 / batch 报告)
  → ../audit_matrix.md                      (新增 P2 section + 每 batch 行)
  → ../trace.jsonl                          (P2 dispatch + phase_report)
  → ../PLAN.md §13 changelog                (P2 sub-plan 版本同步)
-->

# P2 — MD 原子化 Sub-Plan

> Version: **v1.0 (2026-04-29 user ack'd, post P1 CLOSURE 535/535 100%)** — Writer 池修正: 2-type alternation 沿用 P1 v1.0 lock (document-specialist 物理无 Write tool, 与 P1 §0 carry-forward 同禁)
> 父 PLAN: `.work/06_deep_verification/PLAN.md` v0.6 (P1 CLOSURE post round 14)
> 前置: P1 ✅ CLOSURE (12487 atoms / 535 pages / 55 batches / 121 findings)
> 目标: 141 in-scope MD 全量原子化, 产 `md_atoms.jsonl` (P0 Pilot 已 baseline T1/T2/T3 三文件; P2 扩到剩余 138 文件)
> Tier 3 (高 stakes, 多 session)
> Changelog: v0.1 DRAFT (2026-04-29, P1 closure 当天起草)

---

## 0. 入参 & 预估

| 项 | 值 |
|---|---|
| In-scope MD 总数 | **141** (assumptions×63 + examples×63 + model×6 + chapters×6 + top-level×3, 见父 PLAN §0.2) |
| P0 Pilot 已 baseline | 3 文件 (model/04 + ch08 §8.2 局部 + AE/assumptions 局部) — P2 重做全文全量 (而非 P0 scope 子集) |
| 待 P2 新增 | **138 文件** (141 − 3 P0 重叠, 但 P0 是局部, P2 仍重做全文; baseline 子集作 calibration) |
| 单文件原子均值 (P0 实测外推) | ~2 atoms/行, 短文件 ~30-200 atoms, 长文件 ch04 ~1395 行 → ~2500-3000 atoms |
| 预估总原子 | **8000-12000** (141 文件 × ~70 均值 + ch04/VARIABLE_INDEX 长文件加权) |
| 预估 session 数 | **2-3 sessions** (P1 用了 14 round 是因为 PDF 页粒度细 + multi-session 并行; MD 文件粒度粗 + writer-family 池可用) |
| Batch 粒度 | **1 batch = 5-10 文件** 或 **~500-1000 原子** (取早达条件); 大文件 (≥500 行) 单文件 1 batch |
| 总 batch 数 | **~20-30 batch** (短文件批量打包, 长文件单独 batch) |
| Writer 池 (v1.0 修正 2026-04-29) | **2-type alternation 沿用 P1 v1.0 lock**: `oh-my-claudecode:executor` ↔ `oh-my-claudecode:writer`. Document-specialist 物理无 Write tool (Tools: All except Write/Edit), 与 P1 §0 ban 同 carry-forward. MD-side 3-type rotation 设想被物理工具能力否决, 放弃. Drift cal fallback: <80% 一致率派 `general-purpose` (带 Write tool) 作 tiebreaker. |
| Reviewer 池 (Rule D) | 与 P1 同 (scientist / tracer / architect / ai-slop-cleaner / code-reviewer / critic / verifier / planner / Plan / codex:codex-rescue) |
| 输出 | `md_atoms.jsonl` (新文件, root 级) + 每 batch checkpoint + Rule A verdicts |

---

## 1. Phase A — Pilot (session 1, ≤1 session, **强制先 ack 再进 bulk**)

### A.1 Pilot Target 选择 (3 NEW 文件 + 1 P0 baseline 重做)

| # | 文件 | 行数 | 类别 | Pilot 目的 |
|---|---|---|---|---|
| **T1'** | `knowledge_base/model/01_concepts_and_terms.md` | 102 | model/ | 短窄 narrative, 测术语密集 + 9-enum atom_type 在 MD-side 落点 |
| **T2'** | `knowledge_base/chapters/ch04_general_assumptions.md` lines 1-300 | 300 (of 1395) | chapters/ | **切片测试** — 验证父 PLAN §6.1 "≤300 行/段" 切片规则 + 段间 sibling_index 连续 |
| **T3a'** | `knowledge_base/domains/CM/assumptions.md` | 19 | assumptions/ | 短 domain assumptions, 测 CM (Concomitant Medications) 域 — 与 P0 的 AE 域形成对比 (slot A) |
| **T3b'** | `knowledge_base/domains/CM/examples.md` | 103 | examples/ | domain examples (P0 未覆盖), 测 example 表/代码 atom 类型分布 (slot B) |

**Writer 分配** (v1.0 修正 2026-04-29 2-type lock):
- **Writer A `oh-my-claudecode:executor`**: T1' + T-baseline + T3a' (3 短文件 = 102 + 38 + 19 = 159 行)
- **Writer B `oh-my-claudecode:writer`**: T2' + T3b' (1 切片 + 1 examples = 300 + 103 = 403 行)
- 原计划 Writer C = `document-specialist` 已废弃 (无 Write tool); T3 拆给 A/B 平摊保持负载均衡
| **T-baseline** | P0 重做 model/04 全文 (38 行) | 38 | calibration | P0 vs P2 同文件 atom diff (验证 v1.0→v1.8 prompt 演化是否引入回归) |

**Pilot scope 总计**: ~560 行 MD, 估 **400-600 原子**. 比 P0 Pilot (257) 大 ~2x, 比单 P1 batch (~100) 大 ~5x — 适合 pilot 规模.

**类别覆盖**: model + chapters + assumptions + examples = **4/5 in-scope 类别** (top-level INDEX/ROUTING/VARIABLE_INDEX 留 bulk).

### A.2 Pilot Steps (mirror P0 Pilot 8 步)

1. 主 session 写 `evidence/checkpoints/p2_pilot_kickoff.md` 含 4 target 路径 + 切片说明 + writer/reviewer 派发表
2. 派 writer subagent_type **A** (`oh-my-claudecode:executor`) 处理 T1' + T-baseline (短文件批) → `evidence/checkpoints/p2_pilot_T1_md_atoms.jsonl` + `p2_pilot_baseline_md_atoms.jsonl`
3. 派 writer subagent_type **B** (`oh-my-claudecode:writer`) 处理 T2' (ch04 lines 1-300, 切片测试; 派发输入需明确 line range + sibling_index 起始) → `p2_pilot_T2_md_atoms.jsonl`
4. 派 writer subagent_type **C** (`oh-my-claudecode:document-specialist`) 处理 T3a' + T3b' (CM 域对) → `p2_pilot_T3_md_atoms.jsonl`
5. 主 session 合并 + dedup + sibling_index 连续性校验, 输出 `p2_pilot_md_atoms_combined.jsonl` (~400-600 atoms)
6. 派 Rule A reviewer **D** (`oh-my-claudecode:scientist`) 抽 30 atom 分层独审 (HEADING/SENTENCE/LIST_ITEM/TABLE_ROW/CODE_LITERAL 各 ≥4) → `p2_pilot_rule_a_verdicts.jsonl` + summary
7. 派 Rule D 独立 reviewer **E** (不同 subagent_type, 建议 `oh-my-claudecode:code-reviewer`) 跑端到端审查 (schema 合规 + atom_type 分布 + sibling_index 连续 + 与 P0 baseline diff 合理性) → `p2_pilot_review_report.md`
8. 主 session 写 `p2_pilot_report.md` (类似 P0): 4 target 实测 atom 数 / 9-enum 覆盖率 / 切片测试结果 / drift 校准 (3 writer type 对 T1' 同 10 原子) / 已发现 prompt 缺陷 / v1.9 候选

### A.3 Pilot Gate (必须全 PASS 才进 Phase B Bulk)

- [ ] 4 target 全产 atom (无文件 0 atoms)
- [ ] 切片测试: ch04 lines 1-300 单段 atom 输出, sibling_index 0-N 连续无 gap, parent_section L1/L2 active-heading 跨段持续 (验证 N28 MD-side)
- [ ] **9-enum atom_type 至少命中 7 种** (P0 命中 9/9, P2 pilot 短文件比例可能差异 — 7/9 是底线)
- [ ] schema 合规 100% (atom_id 唯一 + verbatim 非空 + parent_section 含 §N [TITLE] 形式)
- [ ] Rule A scientist 抽检 ≥90% PASS (P1 v1.1 升级门槛)
- [ ] Rule D code-reviewer 独立 PASS
- [ ] **drift 校准 ≥80%**: 3 writer type 对 T1' 同 10 原子一致率 (atom_type + verbatim hash)
- [ ] 用户 ack "p2 pilot 看起来合理"

**任一未 PASS → 不得进 Phase B**, 走 Rule B 失败归档 + prompt v1.9 cut session.

---

## 2. Phase B — Bulk Dispatch (session 2-3, 主战, **post pilot ack**)

### B.1 文件分片

| Chunk | 文件集合 | 文件数 | 估 atom |
|---|---|---|---|
| **B-01** | `model/*.md` 剩 5 (除 model/04 已 baseline; 含 model/01 已 pilot 重做) | 5 | ~700 |
| **B-02** | `chapters/*.md` 剩 5 (除 ch04 lines 1-300 已 pilot, 但 ch04 lines 301-1395 是巨型长 batch) | 5 + ch04 续段 | ~2500 |
| **B-03..B-08** | `domains/*/assumptions.md` × 62 (除 AE 已 P0; CM 已 pilot) | 62 | ~2000 |
| **B-09..B-14** | `domains/*/examples.md` × 62 (除 CM 已 pilot) | 62 | ~3500 |
| **B-15** | top-level: `INDEX.md` + `ROUTING.md` + `VARIABLE_INDEX.md` | 3 | ~700 |
| **总计** | | **~138 + ch04 续** | **~9000-10000** |

### B.2 Batch Roster 轮换 (Rule D §8 + v1.0 P1 alternation extended to 3-type)

**3-type rotation** (writer 池, MD-side N21 不适用):

| Batch 序号 | Writer subagent_type | 备注 |
|---|---|---|
| B-01 | `oh-my-claudecode:executor` | 同 P1 starter |
| B-02 | `oh-my-claudecode:writer` | |
| B-03 | `oh-my-claudecode:document-specialist` | 适合 narrative-heavy domain assumptions |
| B-04 | `oh-my-claudecode:executor` | 循环 |
| ... | (3-type rotation) | 连续 2 batch 不得同 type |

**Reviewer 池**: 沿用 P1 burned slot pool (避免 collision, 保持 P1 cross-round Rule D zero-collision invariant); 优先用 P1 未饱和 family (planner / Plan / 部分 omc 家族).

### B.3 Per-batch 产物

- `md_atoms.jsonl` 追加 ~500-1000 行
- `evidence/checkpoints/P2_batch_<NN>_report.md`
- `evidence/checkpoints/_progress_batch_<NN>.json`
- `evidence/checkpoints/rule_a_batch_<NN>_*` (sample + verdicts + summary)
- `trace.jsonl` 追加 ~5-10 行 (每文件 1 条 + 1 条 batch_report)
- `audit_matrix.md` 追加 1 行

### B.4 长文件 ch04 特殊处理

- ch04 全文 1395 行, **必须切片** (父 PLAN §6.1 "≤300 行/段")
- 切片方案: lines 1-300 (pilot 已做) / 301-600 / 601-900 / 901-1200 / 1201-1395 = **5 段**
- 每段 1 次 writer 调用, sibling_index 跨段连续 (段 N 起始 sibling_index = 段 N-1 末尾 + 1)
- parent_section L1 active-heading 跨段持续 (HEADING 原子在段首明示, 段中无新 HEADING 时 children 继承上段 active L2)
- 5 段合并 1 batch (B-02 expanded), 单 writer 完成全文连续性

---

## 3. Phase C — Drift 校准 (间隔 5 batch, 强制)

### C.1 5-batch 校准 (vs P1 3-batch)

P2 batch 数 (~25) 比 P1 (~55) 少, 但单 batch 原子量大 (~500-1000 vs P1 ~100), 校准间隔放宽到 **每 5 batch (~3000-5000 原子)** 派 3 种 writer type 平行 re-atomize 同一 10 原子小样.

**步骤同 P1 §C.1**, 阈值 **≥80%** 一致率, <80% halt.

### C.2 每 batch 末 quick sample (沿用 P1 §C.2)

writer 自己追加 `batch_quality_sample` 5 atom 到 `trace.jsonl` (atom_id + atom_type + verbatim 前 50 字符 + hash).

---

## 4. Phase D — Failure 归档 (Rule B, 沿用 P1 §4)

- `evidence/failures/P2_batch_<NN>_attempt_<M>.md` 含输入/产物/技术判定/业务判定/下次输入
- Hard stop 同 P1 §9.3: batch failure >15% / 连续 2 session <5% / trace 连续 3 写失败 / drift >20%

---

## 5. Phase E — Rule A 抽检 (沿用 P1 v1.1 cadence)

### E.1 每 batch 后 10-atom 分层独审

- 频率: **每 1 batch 后** 派独立 reviewer 跑 10-atom 分层 (按 atom_type 出现比例)
- 门槛: **≥90% PASS** (≥9/10)
- Reviewer 轮换池: 沿用 P1 v1.1 §E.2 (scientist / tracer / architect / ai-slop-cleaner / code-reviewer 等)
- Output: `evidence/checkpoints/rule_a_P2_batch_<NN>_verdicts.jsonl` + `_summary.md`
- <90% halt P2, 读 fail 原子原因, 升 v1.9 prompt 或回炉 batch

### E.2 P0 baseline diff 校验 (P2 特有, vs P1 无)

P2 重做 P0 已 baseline 的 3 文件 (model/04 + ch08 §8.2 + AE/assumptions). 主 session 跑 `p0_baseline_vs_p2 diff` 脚本 (或手工):

- atom 数差 ≤ ±20% (允许 v1.0→v1.8 prompt 改良引入合理差异)
- atom_type 分布同 P0 baseline 对照不应丢失 atom_type (回归信号)
- verbatim 文本一致 (除非 KB 文件本身在 P0 后被修改)

差异 >±20% 或 atom_type 丢失 → halt, 评估是 prompt 改良还是回归.

---

## 6. Phase F — P2 Exit Gate

| 条件 | 门槛 |
|---|---|
| 文件覆盖率 | 100% (141 文件全有 atom 或显式 FAILURE 归档) |
| 失败归档率 | ≤2% |
| Rule A per-batch 一致率 | ≥90% |
| subagent_type drift 校准 | 每 5 batch ≥80% 一致 |
| atom_type 分布 hit 9/9 | 是 (短文件批可能命中 ≤7 但全 P2 累计应 9/9) |
| sibling_index 连续 | 长文件切片段间无 gap |
| parent_section §N [TITLE] 规范 (N27/N28) | 100% L1+L2 atom 合规 |
| trace.jsonl 完整 | batch_id + subagent_type + role + ts 全不空 |
| phase_report 入 trace | P2 末写 phase_report 事件 |
| P0 baseline diff 校验 | atom 数差 ≤±20% + atom_type 无丢失 |

---

## 7. Session 边界 & 交接

### 7.1 Session 切换 protocol (沿用 P1 §7.1)

每 session 末写 `evidence/checkpoints/P2_session_<N>_handoff.md` 含本 session 完成 batch / 下一 batch 起始文件 / trace 尾 ts / `_progress.json` phases.P2 实时字段 / 未解 blocker.

### 7.2 Recovery hint (沿用 P1 §7.2)

`_progress.json` `recovery_hint` 字段必含: 下一 batch id / 起始文件路径 / 上次 writer_type / trace 尾 ts / 失败 attempt 列表.

---

## 8. 依赖 & 风险

| 依赖 | 状态 |
|---|---|
| `subagent_prompts/P0_writer_md_v1.8.md` | ✅ 就绪 (2026-04-30 cut) |
| `schema/atom_schema.json` | ✅ frozen v1.2 (P0 锁定) |
| `schema/ledger_schema.json` | ✅ frozen v1.2 (P0 锁定) |
| `_progress.json` phases.P2 字段开 | ⚠️ Pilot 启动前必加 (current_phase: "P2_pilot") |
| `audit_matrix.md` P2 section | ⚠️ Pilot 启动前必创建 |
| `md_atoms.jsonl` 空文件 (append mode) | ⚠️ Pilot 启动前 touch |
| Pilot 用户 ack | ⚠️ Pilot 跑完用户 review 才进 Phase B |

| 风险 | 缓解 |
|---|---|
| MD-side N21 不适用 → writer-family 引入 hallucination 风险 (vs P1 PDF-side N21 全禁) | drift cal 加密 (5 batch 一次) + Rule A 每 batch ≥90% 严格 + P0 baseline diff 校验 (回归 detect) |
| 长文件 ch04 切片段间 sibling_index drift / parent_section active-heading 漂移 | Pilot T2' 专测此场景; 失败则 v1.9 加 Hook 23 段间连续性 pre-DONE 校验 |
| P0 vs P1→P2 prompt 演化引入 atom 数 / atom_type drift (回归 vs 改良不分) | Phase E.2 baseline diff 校验 + 主 session 人工评估 |
| top-level INDEX/ROUTING/VARIABLE_INDEX 是脚本/AI 产物, atomization 可能产 SYNTHESIZED 原子 (反向 P5 麻烦) | 留 bulk B-15, 单独标记 `extracted_by.note: "auto-generated source"` 字段, P5 阶段反向匹配可批量 SYNTHESIZED verdict |
| ch04 长 batch (~2500 atom) 单 writer call 可能 token 超限 | 5 段切片 + 每段独立 call, 段间靠 sibling_index 续接, 单 call 不超 IR1 (≤300 行) |
| MD-side multi-axis motif (N24 cross-format) 首次出现 | 默认 0 累计 (P0+P1 cumulative 0); pilot drift cal 三 type 平行 re-atomize 是首次 MD-side 校准, 若有 motif 走 v1.9 cut |

---

## 9. 启动 Checklist (P2 Pilot kickoff)

### 9.1 Pilot 启动前 (一次性, ≤30 min)

- [ ] 本 sub-plan v0.1 用户 ack 升 v1.0
- [ ] `_progress.json` 加 `phases.P2` 字段 (status: "pilot_pending" → "pilot_in_progress") + `current_phase: "P2_pilot"`
- [ ] `_progress.json` `recovery_hint` 更新到 P2 pilot 上下文
- [ ] `audit_matrix.md` 追加 `## P2 — MD 原子化` section + pilot table 头
- [ ] `md_atoms.jsonl` touch 空文件 (append mode 待 pilot batch 写入)
- [ ] `evidence/checkpoints/p2_pilot_kickoff.md` 写主 session kickoff (4 target + writer/reviewer 派发表)
- [ ] PLAN.md §13 changelog 追 v0.7 (P2 pilot 启动) — 或留到 pilot ack 后再升

### 9.2 Pilot 跑

- [ ] dispatch writer A → T1' + T-baseline
- [ ] dispatch writer B → T2' (ch04 lines 1-300)
- [ ] dispatch writer C → T3a' + T3b'
- [ ] 主 session 合并 + sibling_index 校验 → `p2_pilot_md_atoms_combined.jsonl`
- [ ] dispatch Rule A reviewer D (scientist) → 30 atom 分层独审
- [ ] dispatch Rule D reviewer E (code-reviewer) → 端到端审查
- [ ] drift cal: 3 writer type 对 T1' 同 10 原子平行 re-atomize → 一致率 ≥80%
- [ ] 主 session 写 `p2_pilot_report.md`
- [ ] 用户 ack — 或 fail 走 Rule B + v1.9 cut

### 9.3 Pilot ack 后 → Phase B Bulk

- [ ] 升本 sub-plan v0.1 → v1.0 (user ack'd)
- [ ] PLAN.md changelog 追 v0.7 (P2 pilot PASS, bulk 启动)
- [ ] dispatch B-01 (model/ 剩 5)
- [ ] (后续 B-02..B-15 按 §B.1 推)

---

*DRAFT v0.1 2026-04-29. P1 closure 当天起草. 预计 pilot session 1 跑 4 target × 3 writer + 1 reviewer + 1 Rule D = 0.5-1 session 完成. Bulk 2-3 sessions 完成 138 文件 / ~9000-10000 atoms.*
