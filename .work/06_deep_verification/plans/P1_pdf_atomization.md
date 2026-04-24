# P1 — PDF 原子化 Sub-Plan

> Version: v0.1-DRAFT (2026-04-24)
> 父 PLAN: `.work/06_deep_verification/PLAN.md` v0.5
> 前置: P0 Pilot ✅ PASS (9/9 原子类型 + v1.2 6/6 fix 实战 PASS)
> 目标: SDTMIG v3.4 461 页 + SDTM v2.0 74 页 = **535 页** PDF 全量原子化, 产 `pdf_atoms.jsonl`
> Tier 3 (高 stakes, 多 session)

---

## 0. 入参 & 预估

| 项 | 值 |
|---|---|
| 总页数 | 535 |
| 原子/页 均值 (P0 实测外推) | ~8-12 atoms/页 (T1 21 atoms/单页稠密, T2 30, T3 32, T2b 16 figure 区) |
| 预估总原子 | **4300-6400** (按 8-12/页) |
| 预估 session 数 | 3-5 sessions |
| Batch 粒度 | 100 原子 = 1 batch (~10-12 页) |
| 总 batch 数 | ~55 batch |
| Writer 池 | `oh-my-claudecode:executor` (主力) / `oh-my-claudecode:writer` / `feature-dev:code-explorer` (轮换) |
| **绝对禁用 writer** | `Explore` / `oh-my-claudecode:explore` (20%+ drift 丢 JSONL, P0 failures/ 教训) |

---

## 1. Phase A — Page Range 分片 (session 0, 准备)

### A.1 页码池划分

- **Pool 1 SDTMIG v3.4 (461 页)**:
  - Chunk 1: p.1-100 (章 1-3, intro, general assumptions 局部)
  - Chunk 2: p.101-200 (章 4 intervention/event/finding 局部)
  - Chunk 3: p.201-300 (章 5-6 trial design / special purpose)
  - Chunk 4: p.301-400 (章 7 relationships start + 各域 spec/assumptions 中段)
  - Chunk 5: p.401-461 (章 8 relationships + 章 9 CT ref + appendices)
- **Pool 2 SDTM v2.0 (74 页)**:
  - Chunk 6: p.1-74 (model intro + 特殊域 + associated persons 已 P0 覆盖)

### A.2 历史页跳过

- P0 Pilot 已原子化页 (non-gap, 作 baseline 不重跑): sv20 p.50 / ig34 p.137 (前 30 行 scope) / ig34 p.428 (前 50 行 scope) / ig34 p.440 (figure 区 scope)
- P1 重做上述 4 页**全页全量** (而非 P0 scope 子集), 产 new atoms 和 P0 子集 diff, 作 calibration 样本

### A.3 Spec 表处理策略 (重要)

SDTMIG v3.4 内 63 域各有 `Specification` 表 (变量 spec 行), xlsx 脚本已独立派生 `knowledge_base/domains/*/spec.md`.

**决策 (v0.5 待用户 ack)**:
- **Option A** (推荐): P1 PDF spec 表也全量原子化作 TABLE_HEADER + TABLE_ROW, 与 `knowledge_base/domains/*/spec.md` 做 side-by-side diff (P4a/P5 阶段), 验证 xlsx 脚本产物 vs PDF ground truth 一致性
- Option B: 跳过 spec 表, 仅原子化 narrative 部分, 接受 xlsx 脚本 PASS 历史
- Option C: 采样 spec 表 (每域抽 3-5 行) 做 sanity, 非全量

**默认 Option A** (高 stakes + xlsx 脚本亦 AI 输出, 字面校验有价值).

---

## 2. Phase B — Batch Dispatch Pattern (session 1-5, 主战)

### B.1 单 batch 定义

- **1 batch = 连续 10-12 页 PDF × 1 writer subagent = ~100 原子产出**
- Writer subagent 单次 input: 1 PDF 页 (IR1 硬约束), batch 内分 10-12 次调用同一 subagent 跑完
- Writer 完成后 Write 自己的 batch 段到 `pdf_atoms.jsonl` (追加, not overwrite)

### B.2 Batch roster 轮换 (Rule D §8 + v0.3 F-4)

| Batch 序号 mod 5 | Writer subagent_type |
|---|---|
| 0 | `oh-my-claudecode:executor` |
| 1 | `oh-my-claudecode:writer` |
| 2 | `feature-dev:code-explorer` |
| 3 | `oh-my-claudecode:executor` (重复, 池不够大时可接受; 但不得两连续 batch 同 type) |
| 4 | `oh-my-claudecode:document-specialist` (多模态, 对含 FIGURE 多的页更强) |

**连续 2 batch 禁用同 type** (硬).

### B.3 Per-batch 产物

- `pdf_atoms.jsonl` 追加 ~100 行
- `trace.jsonl` 追加 ~10-12 行 (每页 1 条 subagent call) + 1 条 batch_report
- `audit_matrix.md` 追加 1 行 (batch_id + writer_type + atom_count + 失败数)

---

## 3. Phase C — Drift 校准 (间隔 3 batch, 强制)

### C.1 300-atom 校准 (v0.4 NF-2 Gap 2)

每完成 3 batch (~300 原子, ~30 页), 派**不同 3 种 writer type** 平行 re-atomize 同一 10 原子小样, 比对一致率.

**Step**:
1. 主 session 选 10 个已原子化的 atom_id (分层: HEADING/SENTENCE/TABLE_ROW/LIST_ITEM/CODE_LITERAL 各 2)
2. 派 writer type A / B / C 各独立 re-atomize 对应原 PDF 页 (不看 baseline)
3. 主 session 脚本 (或手工) 比 atom_type + verbatim hash, 算三型一致率
4. 一致率阈值 **≥80%** (PLAN §9.1 P0 drift calibration 同门槛)
5. <80% → halt, 分析偏离原因, 调 prompt 或换 writer type

### C.2 每 batch 末 quick sample (v0.4 Gap 2 加密)

每 batch 末 writer 自己追加 `batch_quality_sample` 到 `trace.jsonl`: 随机抽 5 原子 (batch 内), 含 atom_id + atom_type + verbatim 前 50 字符 + hash. 主 session 快检是否明显漂 (atom_type 错 / verbatim 含中文 / 空 verbatim 等).

---

## 4. Phase D — Failure 归档 (Rule B)

- Writer 产的 `FAILURE_...` 条目不混入 `pdf_atoms.jsonl`, 单独写 `evidence/failures/P1_batch_<NN>_attempt_<M>.md`
- 含 input (page), 产物 (原始响应), 技术判定 (why 失败), 业务判定 (是否真 unsolvable), 下一 attempt 输入 (换 type / 换 page slice / 拆页半)

**hard stop 条件** (PLAN §9.3):
- 任一 batch failure 率 >15%: halt
- 连续 2 session 完成率 <5%: halt
- trace.jsonl 连续 3 条写入失败: halt

---

## 5. Phase E — Rule A 抽检 (每 batch + 30 页独审)

### E.1 Per-batch (writer 自己)

写入完成后 writer 不再干预. 不对 batch 内 Rule A.

### E.2 每 30 页 = 约 3 batch, 派独立 reviewer 跑 Rule A 抽检

- Reviewer subagent_type (未烧): `superpowers:code-reviewer` / `oh-my-claudecode:scientist` / `oh-my-claudecode:tracer` / `oh-my-claudecode:architect`
- Reviewer 任务: 从 3 batch 中**随机分层抽 30 原子** (各 atom_type 按出现比例), 对 PDF 原页独立 re-atomize 该 10 原子位, 比对 atom_type + verbatim
- **PASS 门槛 ≥90%** 原子一致 (PLAN §9.1 P1 抽样)
- <90%: halt P1, prompt 回炉

---

## 6. Phase F — P1 Exit Gate

| 条件 | 门槛 |
|---|---|
| 页覆盖率 | 100% (535 页全有 atom 或显式 FAILURE 归档) |
| 失败归档率 | ≤2% |
| Rule A 30 页独审一致率 | ≥90% |
| subagent_type drift 校准 | 每 300 atom ≥80% 一致 |
| atom_type 分布 hit 9/9 | 是 (T2b 已证可行) |
| trace.jsonl 完整 | 含 batch_id + subagent_type + role + ts 全不空 (R13 fix) |
| phase_report 入 trace | 是 (v0.4 Gap 7) |

---

## 7. Session 边界 & 交接

### 7.1 Session 切换 protocol

每 session 末写 `evidence/checkpoints/P1_session_<N>_handoff.md` 含:
- 本 session 完成 batch 编号 + 原子数
- 下一 batch 编号 + 起始页
- trace.jsonl 尾 entry_id (recovery 锚)
- `_progress.json` phases.P1.pages_done / atoms_done 实时字段
- 未解 blocker 列表

### 7.2 Recovery hint (R13 写 `_progress.json`)

`recovery_hint` 字段必含: 下一 batch id / 起始页 / 上次 writer_type / trace 尾 ts / 失败 attempt 列表.

---

## 8. 依赖 & 风险

| 依赖 | 状态 |
|---|---|
| `subagent_prompts/P0_writer_pdf_v1.2.md` | ✅ 就绪 (2026-04-24) |
| `schema/atom_schema.json` | ✅ frozen v1.2 |
| `_progress.json` trace_entries 字段启用 | ⚠️ P1 启动前必开 `trace.jsonl` append |
| `audit_matrix.md` | ⚠️ P1 启动前 template 创建 |
| PLAN v0.5 | ⚠️ D 阶段产出中, P1 启动前必 ack |

| 风险 | 缓解 |
|---|---|
| 5000+ 原子 token 成本 | 已接受 "不计成本"; 单 writer call 输入 ~5-7KB, 输出 ~3-5KB, ~50K total/batch |
| PDF OCR 多列排版错 | P1 抽检 Rule A 捕捉; 失败归档重跑 |
| Writer drift 渐累 | 300-atom 校准 + 每 batch quick sample 双层防 |
| FIGURE 原子 P4a 输入超 IR1 | v0.4 Gap 3 截断策略 (前 200 字符 fingerprint) |
| MD caption bold 非 heading (F-T2b-1) | P1 抽样统计 caption markup 分布, 若 <60% heading 语法则 v1.3 补规则 (但不 block P1) |

---

## 9. 启动 Checklist (P1 kickoff)

- [ ] PLAN v0.5 用户 ack
- [ ] `schema/atom_schema.json` + `schema/ledger_schema.json` 冻结文件上链 (gitpush)
- [ ] `subagent_prompts/P0_writer_pdf_v1.2.md` 主 session 加载作派发模板
- [ ] `_progress.json` 初 phases.P1 字段 + trace_entries=0 + current_phase="P1"
- [ ] `audit_matrix.md` 创建 P1 section
- [ ] `trace.jsonl` 创建空文件 (append mode)
- [ ] First batch 派: `oh-my-claudecode:executor` × 10 页 (SDTMIG v3.4 p.1-10)
- [ ] 主 session 启本 session 跑 3 batch (~300 原子), 跑完做 drift 校准 1 次

---

*DRAFT v0.1 2026-04-24. P1 启动前用户 ack 后升 v1.0. 预计首 session (session 1) 跑 3 batch + 1 drift 校准 + 1 Rule A 独审 = 尾阶段提前暴露系统问题.*
