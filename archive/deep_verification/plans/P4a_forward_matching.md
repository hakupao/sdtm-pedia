<!-- chain: F (深度验证旁枝链 v2)
  修改本文件后, 必须检查:
  → ../_progress.json                       (phases.P4a_forward_matching 字段)
  → ../evidence/checkpoints/                (P4a 产物快照)
  → ../PLAN.md §5                           (phase 状态更新)
  → ../audit_matrix.md                      (P4a section 新增)
  → ../trace.jsonl                          (phase_report 追加)
-->

# P4a — 正向匹配 PDF→MD Sub-Plan

> Version: **v1.0 DRAFT (2026-05-11, post P3 gate ALL PASS)**
> 父 PLAN: `branches/06_deep_verification/PLAN.md` v0.6
> 前置: P3 ✅ COMPLETE (p3_candidates.jsonl 12,487行; zero_cand 0.0%, avg_cands 5.30, top1_mean 0.702)
> 目标: 12,487 pdf_atoms 全量正向匹配, 产 `coverage_ledger.jsonl` (12,487 条 forward entries)
> Tier 3 (高 stakes, 多 session) / 预估 **4-6 sessions**
> 匹配 prompt: `subagent_prompts/P0_matcher_v1.9.4.md` (角色 = P4a 正向)

---

## 0. 输入 / 输出契约

| 项 | 值 |
|---|---|
| 输入 1 | `p3_candidates.jsonl` (12,487行 × {pdf_atom_id, pdf_atom_type, pdf_parent_section, candidates[≤5]}) |
| 输入 2 | `pdf_atoms.jsonl` (verbatim + page + parent_section 原文, 12,487 atoms) |
| 输入 3 | `md_atoms.jsonl` (md verbatim 原文 lookup, 10,435 atoms) |
| 批次输入 (pre-built) | `evidence/p4a_batches/batch_NNN_input.jsonl` (见 §1.1 批预处理) |
| 主产物 | `coverage_ledger.jsonl` (append, 一行/atom, forward entries) |
| 辅助产物 | `discrepancies.md` (MISPLACED 聚合) + `evidence/checkpoints/p4a_*_report.md` |
| 消费方 | P4b section aggregation reads `coverage_ledger.jsonl` |

### 0.1 coverage_ledger.jsonl 行格式 (来自父 PLAN §4.3)

```jsonc
{
  "pdf_atom_id": "ig34_p0425_a012",
  "md_atom_ids": ["md_relrec_ass_a003"],   // 空 = MISSING
  "verdict": "EQUIVALENT",
  "similarity_score": 0.92,
  "discrepancy": null,                      // 非 EXACT 时填; MISPLACED 时含 section 对比
  "exclusion_reason": null,                 // 仅 INTENTIONAL_EXCLUDE
  "matched_by": {
    "subagent_type": "oh-my-claudecode:executor",
    "batch_id": "batch_001",
    "ts": "2026-05-11T..."
  },
  "audited_by": []                          // P4a batch reviewer 填; Rule A 独审后追加
}
```

**verdict 合法枚举**: `EXACT | EQUIVALENT | PARTIAL | MISPLACED | MISSING | ERROR | INTENTIONAL_EXCLUDE`

---

## 1. 批次计划

12,487 atoms ÷ 100/batch = **125 batches** (batch_001~batch_124 各 100 atoms; batch_125 = 87 atoms)

处理顺序: p3_candidates.jsonl 行序 (与 P1 pdf_atoms 原子化页序一致: ig34 p.1→461 → sv20 p.1→74)

| Session (预估) | Batch 范围 | Atoms | 累计覆盖率 |
|---|---|---|---|
| S1 | batch_001~025 | 2,500 | 20% |
| S2 | batch_026~050 | 2,500 | 40% |
| S3 | batch_051~075 | 2,500 | 60% |
| S4 | batch_076~100 | 2,500 | 80% |
| S5 | batch_101~125 | 2,487 | 100% |

每 session 末: 写 checkpoint + 更新 `_progress.json` + `trace.jsonl` session_report 条目.

### 1.1 批预处理 (每 session 开始前, 主 session 执行)

为避免 matcher agent 在 large JSONL 中查找 verbatim (12K+ 行), 主 session 先用脚本预构建批次输入:

```bash
# 示例: 构建 batch_001~025 (S1)
python3 scripts/p4a_build_batches.py \
  --candidates p3_candidates.jsonl \
  --pdf_atoms pdf_atoms.jsonl \
  --md_atoms md_atoms.jsonl \
  --batch_size 100 \
  --range 1-25 \
  --outdir evidence/p4a_batches/
```

每个输出文件 `evidence/p4a_batches/batch_NNN_input.jsonl` 每行包含:

```jsonc
{
  "pdf_atom_id": "...",
  "pdf_atom_type": "SENTENCE",
  "pdf_source": "SDTMIG_v3.4",
  "pdf_page": 42,
  "pdf_parent_section": "§4.1 ...",
  "pdf_verbatim": "...",
  "candidates": [
    {
      "md_atom_id": "...",
      "md_file": "knowledge_base/...",
      "md_atom_type": "SENTENCE",
      "md_parent_section": "...",
      "md_verbatim": "...",    // 从 md_atoms.jsonl lookup join
      "score": 0.82,
      "match_basis": "verbatim_token+domain_route"
    }
  ]
}
```

**FIGURE 原子截断 (父 PLAN Appendix B + v0.4 Fix Gap 3)**:
- `pdf_verbatim` 取前 200 字符 + `figure_ref` (pdf_page + 区域)
- `md_verbatim` 同样取前 200 字符
- 全量 Mermaid 不进 batch_input (防 IR1 context overflow)

**脚本路径**: `branches/06_deep_verification/scripts/p4a_build_batches.py` (P4a S1 开始前产)

---

## 2. 原子类型分布 (P3 实测, 决定 reviewer 抽样权重)

| atom_type | count | % | top1_mean | P4a 匹配难度说明 |
|---|---|---|---|---|
| TABLE_ROW | 5,526 | 44.3% | 0.670 | 中 — spec 表行相似度高但跨表混淆风险; MISPLACED 主要来源 |
| SENTENCE | 2,534 | 20.3% | 0.715 | 中 |
| LIST_ITEM | 1,944 | 15.6% | 0.806 | 低 |
| HEADING | 876 | 7.0% | 0.747 | 低 — 结构锚, 通常 EXACT/EQUIVALENT |
| CODE_LITERAL | 604 | 4.8% | 0.527 | 高 — 字面精确; KB 改写导致 PARTIAL 风险 |
| TABLE_HEADER | 560 | 4.5% | 0.811 | 低 |
| CROSS_REF | 297 | 2.4% | 0.583 | 高 — KB cross-ref 格式不一; 易 MISSING |
| NOTE | 106 | 0.8% | 0.577 | 高 — NOTE 常被折入 SENTENCE 或省略 |
| FIGURE | 40 | 0.3% | 0.491 | 高 — 特殊 verbatim 截断规则 (§3.3) |

---

## 3. Writer / Reviewer 分配

### 3.1 Writer 池 (carry-forward from P1/P2 物理约束 — 不变)

**2-type alternation only**: `oh-my-claudecode:executor` ↔ `oh-my-claudecode:writer`

连续两 batch 不得同 type (奇 batch → executor, 偶 batch → writer 或反之).

**绝对禁用** (P1/P2 教训, carry-forward):
- Explore / oh-my-claudecode:explore / feature-dev:code-explorer (Write tool 缺失, 丢 JSONL 20%+)
- document-specialist / architect / code-reviewer 家族 (Tools: All except Write/Edit)
- planner / Plan / designer (role 不匹配)

### 3.2 Reviewer 池 (P4a 内 ≥3 种, Rule D phase-scoped)

P4a 内各 reviewer 首次出现即记入 `audit_matrix.md` P4a section + `trace.jsonl`.

| 推荐 slot | type | 建议用途 | 项目已烧? |
|---|---|---|---|
| P4a-R1 | `oh-my-claudecode:scientist` | batch 质量抽样 (10 原子 × 3-type drift 校准) | 未烧 (首次) |
| P4a-R2 | `oh-my-claudecode:critic` | 每 session 末深度批次审查 | 已烧 (P0) |
| P4a-R3 | `oh-my-claudecode:verifier` | Rule A 最终 100 原子分层审 | 已烧 (P0) |
| P4a-R4 | `feature-dev:code-reviewer` | drift 校准第 3 type | 已烧 (P2) |

规则: 每 batch 的 reviewer ≠ 当 batch writer type (hard).

### 3.3 Drift 校准 (每 3 batch 一次, 来自父 PLAN §9.1 P4a-drift)

触发条件: 完成 batch 003 / 006 / 009 / ... (每 3 batch)

操作:
1. 从最近 3 batch 末尾各抽 3~4 atoms (合计 10 atoms)
2. 派 3 种 writer type 各独立判 verdict (3 个 subagent 并行)
3. 计算 3-type 间 verdict 一致率
4. 写 trace.jsonl `drift_check` 事件 (含 batch_ids + 10 atom_ids + 一致率)

**Gate**: ≥80% 一致 → 继续; <80% → halt, 调 prompt, 升 PLAN version

### 3.4 Batch Quality Sample (每 batch 末写入 trace.jsonl)

```jsonc
{
  "ts": "...", "phase": "P4a", "slot": "batch_quality_sample",
  "batch_id": "batch_NNN",
  "subagent_type": "oh-my-claudecode:executor",
  "samples": [
    {"pdf_atom_id": "...", "verdict": "EQUIVALENT", "top1_score": 0.82}
    // × 5 atoms
  ]
}
```

---

## 4. 特殊原子处理规则

### 4.1 FIGURE 原子 (40 个)

- matcher 输入: verbatim 前 200 字符 + `figure_ref` (pdf_page + 区域描述) — 不传全量 Mermaid
- md 候选: 同样前 200 字符截断
- verdict 产出正常写入 `coverage_ledger.jsonl`
- **若 reviewer 需全量对比**: 单独派 `oh-my-claudecode:document-specialist` L2 深审 (非常规流程, 仅高争议时触发)

### 4.2 零候选 (此版 p3 = 0 条, 逻辑保留)

`candidate_count = 0` → 跳过 matcher agent, 直接写:
```jsonc
{"pdf_atom_id": "...", "md_atom_ids": [], "verdict": "MISSING", ...}
```

### 4.3 MISPLACED 检测 (父 PLAN v0.3 Fix F-2 强制)

matcher 比对时必检 `pdf_parent_section` vs `md_parent_section`:
- 文本 EXACT/EQUIVALENT 但 parent section 不对齐 → `verdict=MISPLACED`
- MISPLACED 不开独立 Issue; 写入 `coverage_ledger.jsonl` discrepancy 字段 (格式: `MISPLACED: pdf §X.Y vs md §Z.W`) + 追加 `discrepancies.md` 聚合表一行

**MISPLACED ↔ STRUCTURE_DRIFTED 去重** (父 PLAN Appendix C v0.4 Gap 1):
- 原子层 MISPLACED: 不开 Issue (仅 tracking_comment)
- 聚合层 (P4b): 触发 STRUCTURE_DRIFTED → 开父 Issue

### 4.4 INTENTIONAL_EXCLUDE (预批 category 可自填)

父 PLAN Appendix D 预批 category (matcher agent 可直接填, 无需用户逐条 ack):
- `VERSION_MISMATCH` — SDTM v2.0 内容被 SDTMIG v3.4 取代
- `EDITORIAL_META` — 封面/目录/致谢/版本说明页

填写格式: `exclusion_reason="<原因>" + category="VERSION_MISMATCH" + approved_by="pre-approved-category"`

**逐条审批 category** (matcher 不可自填, 须用户 ack 后写入):
- `REDUNDANT_WITH_SPEC` — PDF 正文与 xlsx spec 重复
- `FIGURE_ALREADY_CONVERTED` — Mermaid 已存其他位置

---

## 5. Exit Gate (P4a)

来自父 PLAN §9.1 + §9.2:

| Gate 条件 | 阈值 | 验证方式 |
|---|---|---|
| `coverage_ledger.jsonl` 行数 | = 12,487 | `wc -l coverage_ledger.jsonl` |
| 每行 verdict ∈ 合法枚举 | 100% | JSON schema validate (脚本) |
| `INTENTIONAL_EXCLUDE` 全有 whitelist 对应 | 100% | grep + whitelist diff |
| Rule A 分层 100 原子独审 | ≥95% 一致率 | 独立 reviewer (P4a-R3) |
| 末次 drift check 一致率 | ≥80% | trace.jsonl grep drift_check |
| `trace.jsonl` P4a `phase_report` 条目 | ≥1 | grep phase_report |
| Rule D ≥3 种 reviewer type | P4a 内 ≥3 种不同 type | audit_matrix.md |
| MISPLACED 全部有 discrepancies.md 对应 | 100% | 脚本 cross-check |

**Rule A 分层采样** (父 PLAN §9.1 P4a 行):
100 原子 分层: HEADING 20 + SENTENCE 20 + TABLE_ROW 20 + LIST_ITEM 20 + CODE_LITERAL 20
抽样时机: coverage_ledger.jsonl 100% 填充后, gate 验证前

---

## 6. 产物目录

```
branches/06_deep_verification/
├── coverage_ledger.jsonl              ← P4a 主产物 (每 batch append)
├── discrepancies.md                   ← MISPLACED 聚合表
├── scripts/
│   └── p4a_build_batches.py           ← 批预处理脚本 (S1 前产)
├── evidence/
│   ├── p4a_batches/
│   │   ├── batch_001_input.jsonl      ← pre-built, 一行/atom (verbatim join)
│   │   └── ...
│   └── checkpoints/
│       ├── p4a_session_S1_report.md   ← 每 session 末
│       └── p4a_final_report.md        ← gate 验证报告
├── trace.jsonl                        ← batch_dispatch + drift_check + phase_report 追加
└── audit_matrix.md                    ← 新增 P4a section
```

---

## 7. Multi-Session 调用入口

每 session 开始时, 主 session 写 `multi_session/P4a_session_NN_kickoff.md`, 内容:

```markdown
# P4a Session NN Kickoff
- Session 范围: batch_NNN ~ batch_NNN
- 当前 coverage_ledger.jsonl 行数: XXX (已完成 atoms)
- 上次 drift check 结果: batch_NNN, 一致率 XX%
- 本 session writer_type 起始: executor|writer
- Writer 轮换规则: 奇 batch=executor / 偶 batch=writer (或延续上 session 序列)
- Reviewer 本 session: P4a-RN (type)
```

---

## 8. Recovery Hint

恢复步骤:
1. `python3 -c "import json; d=json.load(open('_progress.json')); print(d['phases']['P4a_forward_matching'])"`
2. `wc -l coverage_ledger.jsonl` → 已完成原子数 → batch 起点 = ceil(count/100) + 1
3. `tail -20 trace.jsonl | python3 -m json.tool` → 确认无脏写 (status≠failed)
4. `ls evidence/checkpoints/p4a_*` → 最新 session checkpoint
5. `grep '"slot":"drift_check"' trace.jsonl | tail -3` → 最新 drift 状态

---

## 9. Hard Stop 条件 (来自父 PLAN §9.3)

| 条件 | 行动 |
|---|---|
| Drift 一致率 <80% | halt, 调 P0_matcher prompt, 升本 PLAN version |
| Subagent 失败率 >15% per batch | 调 prompt 或切 writer type |
| `coverage_ledger.jsonl` 出现不合 schema 行 | halt, human review, 归档到 failures/ |
| 连续 2 session 完成率 <5% | halt, re-evaluate strategy |
| `trace.jsonl` 连续 ≥3 条写入失败 | halt, 审 trace pipeline |
| P4a Rule A 一致率 <95% | halt (P4a gate 未过, 不进 P4b) |

---

## 10. 下一步 (sub-plan 就绪后)

1. **用户 ack 本 sub-plan** — 确认 gate 阈值 / writer 池 / drift 频率
2. **写 p4a_build_batches.py** — 批预处理脚本 (S1 前)
3. **P4a S1 kickoff** — 写 `multi_session/P4a_session_01_kickoff.md` + 派 batch_001~025

---

## Changelog

| Version | Date | Change |
|---|---|---|
| v1.0 DRAFT | 2026-05-11 | Initial draft, post P3 gate ALL PASS. Writer池/Reviewer池/Drift/批预处理/特殊原子规则 全设计 |
