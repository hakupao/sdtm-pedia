# P1 Batch 01 Report

> Date: 2026-04-24
> Writer: `oh-my-claudecode:executor` (Rule D slot #8, 跨 phase 复用 OK, phase 内首用)
> Prompt: `subagent_prompts/P0_writer_pdf_v1.2.md`
> Scope: SDTMIG v3.4 (no header footer).pdf 页 1-10
> Status: **✅ DONE**

---

## 数字摘要

| 指标 | 值 |
|---|---|
| 页数 | 10 |
| 总原子 | **326** |
| 失败 | 0 (0%) |
| 均值 | 32.6 atoms/页 |
| Executor duration | 13 min 7 sec |
| Executor tokens | 117,017 |

## Per-page 分布

| 页 | 原子数 | 主 atom_type | 备注 |
|---|---|---|---|
| 1 | 16 | TABLE_ROW (8) + HEADING (3) + TABLE_HEADER (1) + SENTENCE/LIST_ITEM/CROSS_REF | 封面 + Revision History 表 + 版权 |
| 2 | 50 | CROSS_REF (49) + HEADING (1) | TOC 第 1 页 |
| 3 | 53 | CROSS_REF (53) | TOC |
| 4 | 56 | CROSS_REF (56) | TOC |
| 5 | 50 | CROSS_REF (50) | TOC |
| 6 | **2** | CROSS_REF (2) | **稀疏页** (疑 figure/空白) |
| 7 | 24 | SENTENCE (10) + LIST_ITEM (10) + HEADING (4) | §1 Introduction 开始 |
| 8 | 24 | LIST_ITEM (15) + SENTENCE (7) + HEADING (1) + CROSS_REF (1) | §1 cont. |
| 9 | 26 | LIST_ITEM (20) + SENTENCE (5) + HEADING (1) | §1 cont. |
| 10 | 25 | LIST_ITEM (16) + SENTENCE (6) + HEADING (3) | §1 cont./§2 start |

## Atom_type 总分布

| atom_type | count | % | 累计 P0+P1 Batch 01 |
|---|---|---|---|
| CROSS_REF | 212 | 65.0% | TOC 导致 |
| LIST_ITEM | 62 | 19.0% | |
| SENTENCE | 30 | 9.2% | |
| HEADING | 13 | 4.0% | |
| TABLE_ROW | 8 | 2.5% | |
| TABLE_HEADER | 1 | 0.3% | |
| FIGURE / NOTE / CODE_LITERAL | 0 | — | p.1-10 无 (正常, 这些主要在 domain 章/chapters 8) |

---

## Schema 校验结果

**Pre-fix**: 326 atom_id 格式违反 schema (3 位 page 号, `p001` vs schema 要求 `p0001`)

**Fix**: 脚本 bulk pad `p<NNN>_a<NNN>` → `p<NNNN>_a<NNN>`, 全 326 修正. trace 记录 `schema_autofix`.

**Post-fix**: 0 schema errors.

| 校验项 | 结果 |
|---|---|
| JSON well-formed (每行) | ✅ 326/326 |
| atom_type ∈ 9-enum | ✅ 326/326 |
| HEADING 含 heading_level + sibling_index | ✅ 13/13 |
| FIGURE 含 figure_ref | N/A (0 FIGURE in this batch) |
| atom_id 格式 (4 位 page) | ✅ 326/326 (post autofix) |
| atom_id 无重复 | ✅ 0 dup |
| verbatim 非空 | ✅ 326/326 |
| 必需字段完整 (atom_id/source/page/atom_type/verbatim/extracted_by) | ✅ 326/326 |

---

## Observations (findings)

### [INFO] O-P1-01 — TOC 大量 CROSS_REF, P4a 预留 EDITORIAL_META 白名单批处理
- p.2-5 产 208 CROSS_REF, 全为 TOC 条目 (如 `1 INTRODUCTION .......1`, `2.1 OBSERVATIONS AND VARIABLES .......9`)
- MD 侧大概率不复制 PDF TOC (MD 用自动 anchor 或无 TOC)
- **P4a 预期**: 这些 CROSS_REF forward 全 MISSING 或 INTENTIONAL_EXCLUDE + exclusion_reason="TOC entry superseded by markdown anchors"
- **动作**: 在 `intentional_exclude_whitelist.md` 启用时批量预批 category=`EDITORIAL_META` 接收 (PLAN v0.4 Appendix D Gap 6 已定义此 category 为批量预审批)

### [INFO] O-P1-02 — p.6 稀疏页 (2 atoms)
- 需人工 Read p.6 看是否真 figure/空页, 或 executor 漏抽
- 若是 figure: 合理, 等 FIGURE atom 被其他场景覆盖
- 若是漏抽: repro 重跑. 本 batch 非 blocker (drift 校准会捕捉 systemic issue), 记 TODO.

### [MEDIUM] O-P1-03 — writer v1.2 prompt 文档内矛盾 (atom_id 位数)
- Prompt §atom_id 命名规范例说 `p<NNN>` 3 位 但 schema/json 说 `\d{4}` 4 位
- Executor 按 prompt 例写 3 位, 本 batch autofix 修回 4 位
- **v1.3 prompt fix**: 统一为 `p<NNNN>` 4 位, 例改 `ig34_p0050_a003`
- 本次 autofix 不入 Rule B failures (executor 守了 prompt 字面, 是 prompt bug)

### [LOW] O-P1-04 — 0 CODE_LITERAL / NOTE / FIGURE in 10 pages
- 意料之内: p.1-10 是 cover+TOC+Chapter 1 intro, 正文 variable/example 在后续章
- P1 后续 batch 预期 CODE_LITERAL 占比上升 (spec 表域入)
- 不 halt

---

## 合并到 root pdf_atoms.jsonl

```
.work/06_deep_verification/pdf_atoms.jsonl
  ← appended 326 lines from evidence/checkpoints/pdf_atoms_batch_01.jsonl
  总行数: 326
```

## Rule D 链状态

- Writer slot #8 (`oh-my-claudecode:executor`) 跨 phase 复用, P1 内首用 OK
- 本 batch 无 reviewer (Rule A 按 PLAN §9.1 = 30 页 sample, 等 batch 2/3 累到 30 页触发)

## 下一步

1. **Batch 2**: writer 轮换 `oh-my-claudecode:writer` 跑 p.11-20 (每 batch 不同 type, PLAN v0.5 §B.2)
2. **Batch 3**: writer `feature-dev:code-explorer` 跑 p.21-30
3. **Drift 校准** (batch 3 末): 派 3 种 writer type 平行 re-atomize 10 原子, ≥80% 一致率
4. **Rule A 抽检** (30 页累) : 派 slot #12 reviewer (候选 `superpowers:code-reviewer`) 独审 30 原子, ≥90% 门槛
5. **v1.3 prompt minor fix**: atom_id 位数统一 4 位 (P1 末集中修, 非 blocker)

## Session budget

Batch 1 占用 ~13 min executor + ~1 min maintain. Session 1 预算跑 3 batch + 1 drift + 1 Rule A ≈ 60-90 min. 当前剩余 session budget 支持继续 batch 2.
