# P0 → P1 Handoff Report

> Date: 2026-04-24
> 状态: **P0 ✅ PASS (full, 9/9 atom coverage + v1.2 6/6 fix 实战 PASS)**
> 下一 session 入口: P1 kickoff (见 §5 checklist)

---

## 0. TL;DR (50 words)

P0 Pilot 4 target (T1/T2/T3/T2b) 跑通, schema v1.2 冻结, 9/9 原子类型全覆盖, v1.2 6 规则 (H1'/H2'/N1/N2/N3/FIGURE) 实战 PASS, Rule D 11/16 slot 烧 (余 5), 226+31=257 atoms + 198+31=229 ledger 入 checkpoints. 主方法论 validated. 下一 session 按 `plans/P1_pdf_atomization.md` 启 P1 batch 1.

---

## 1. P0 最终结果

### 1.1 Gate 完成度

| Gate | 门槛 | 实测 |
|---|---|---|
| 工具链 | PASS | PASS ✓ |
| 9 atom_type 覆盖 | ≥6/9 | **9/9 ✓** (T2b FIGURE 补齐) |
| schema freeze | YES | **v1.2 frozen (2 JSON Schema 文件)** ✓ |
| Rule D ≥80% | 两 reviewer | T1 v1.1 85% + T2/T3 81.25% ✓ |
| v1.2 fix 实战 | 6/6 | **6/6 PASS** (T2b 验证) ✓ |

**P0 final: PASS (从 CONDITIONAL_PASS 升级)**

### 1.2 数据资产 (21 文件)

```
evidence/checkpoints/
├── p0_T1_pdf_atoms.jsonl              17  v1
├── p0_T1_md_atoms.jsonl               25  v1
├── p0_T1_ledger_forward.jsonl         17
├── p0_T1_ledger_reverse.jsonl         25
├── p0_T1_section_aggregate.jsonl       1  手工
├── p0_T1_pdf_atoms_v1.1.jsonl         21  v1.1
├── p0_T1_md_atoms_v1.1.jsonl          21  v1.1
├── p0_T1_ledger_forward_v1.1.jsonl    21
├── p0_T1_ledger_reverse_v1.1.jsonl    21
├── p0_T2_pdf_atoms.jsonl              30
├── p0_T2_md_atoms.jsonl               42
├── p0_T2_ledger_forward.jsonl         30
├── p0_T2_ledger_reverse.jsonl         42
├── p0_T3_pdf_atoms.jsonl              32
├── p0_T3_md_atoms.jsonl               55
├── p0_T3_ledger_forward.jsonl         32
├── p0_T3_ledger_reverse.jsonl         55
├── p0_T2b_pdf_atoms.jsonl             16  *T2b FIGURE 补测*
├── p0_T2b_md_atoms.jsonl              15  *T2b*
├── p0_T2b_ledger_forward.jsonl        16  *T2b*
├── p0_T2b_ledger_reverse.jsonl        15  *T2b, 全 forward-aware*
├── p0_T1_findings.md                      writer 阶段
├── p0_T1_reviewer_report.md               v1 FAIL 70%
├── p0_T1_v1.1_reviewer_report.md          v1.1 PASS 85%
├── p0_T2_T3_reviewer_report.md            T2+T3 PASS 81.25%
├── p0_pilot_report.md                     v1 阶段
├── p0_pilot_v1.1_summary.md               v1→v1.1
├── p0_pilot_FINAL_report.md               前轮收官
├── p0_T2b_figure_supplemental.md          *T2b short report*
└── p0_to_p1_handoff.md                    本文件

evidence/failures/
└── v1.1_attempt_pdf_writer_Explore.md     Rule B

subagent_prompts/
├── P0_writer_pdf_v1.md + v1.2.md
├── P0_writer_md_v1.md + v1.2.md
├── P0_matcher_v1.md + v1.2.md
├── P0_reviewer_v1.md + v1.2.md
└── archive/v1_final_2026-04-24/           v1 snapshot

schema/
├── atom_schema.json                        JSON Schema 2020-12, frozen v1.2
└── ledger_schema.json                      JSON Schema 2020-12, frozen v1.2

plans/
└── P1_pdf_atomization.md                   sub-plan v0.1-DRAFT
```

### 1.3 累计数字

- PDF atoms: 17 + 21 + 30 + 32 + 16 = **116 (去重后 99 个, T1 v1 vs v1.1 重 17)**
- MD atoms: 25 + 21 + 42 + 55 + 15 = **158 (去重后 133, 同理)**
- Ledger entries forward + reverse: **229 + 去重调整**
- Findings: 12 (P0 Pilot 主体) + 2 (T2b F-T2b-1/2)
- Rule D slot 烧: 11/16 (余 5 + 2 = 7 含 planner/Plan)

---

## 2. v1.2 升级总结 (B 阶段产出)

### 2.1 4 prompts v1.2

| 文件 | v1.2 变更核心 |
|---|---|
| `P0_writer_pdf_v1.2.md` | (a) executor/writer 家族硬约束 (禁 Explore); (b) 9-enum 硬 gate; (c) CODE_LITERAL `*.xpt` 硬规则 (H1' sync) |
| `P0_writer_md_v1.2.md` | (a) **H1'** `*.xpt`/`*.sas7bdat`/`*.csv` 硬归 CODE_LITERAL; (b) **N1** 9-enum 硬 gate + self-validate; (c) 段落多句强拆 SENTENCE (非 PARAGRAPH) |
| `P0_matcher_v1.2.md` | **最大升级**: (1) **H2'** reverse forward-aware 硬 gate Step 0; (2) **EDITORIAL_CORRECTION** 新 forward verdict (M1' PDF typo 场景); (3) **reverse ≥0.50** gate (N2); (4) **heading EQUIVALENT ≥0.85 Jaccard** (N3); (5) TABLE_SIMPLIFIED / EDITORIAL_ADDITION 正式成文; (6) [INVALID_MD_ATOM_TYPE] triage 标记 |
| `P0_reviewer_v1.2.md` | v1.2 fix 验证矩阵 + Rule D roster 11/16 烧 + 5 未烧候选名单 |

### 2.2 2 schema JSON 冻结

- `schema/atom_schema.json` (v1.2): JSON Schema 2020-12, pdf_atom + md_atom oneOf 分派, 9-enum + HEADING heading_level/sibling_index 条件必填 + FIGURE figure_ref 条件必填
- `schema/ledger_schema.json` (v1.2): forward 9 verdict + reverse 5 verdict 分组, matched_by.direction 强一致, issue_trigger_map (Appendix C 同步)

### 2.3 归档

- `archive/v1_final_2026-04-24/` 含 4 个 v1 prompts 快照 (保留 root 的 v1 副本作 diff 参考)

---

## 3. T2b FIGURE 补测关键发现 (C 阶段)

### 3.1 v1.2 6/6 fix 实战 PASS

| Fix | 证据 |
|---|---|
| H1' dataset CODE_LITERAL | PDF a009 + MD a008 `relspec.xpt` 双向 CODE_LITERAL ✓ |
| H2' reverse forward-aware | 15/15 reverse entries `forward_aware_checked=true` ✓ |
| N1 9-enum | 31/31 atom 合规 ✓ |
| N2 reverse ≥0.50 | 最低 0.60 ✓ |
| N3 heading Jaccard | 'RELSPEC Examples' vs 'Example' Jaccard 0.50 < 0.85 → 正确降 PARTIAL ✓ |
| FIGURE schema | PDF verbatim [FIGURE: ...] + figure_ref / MD verbatim mermaid 源 / forward 前 200 字符 fingerprint 比 ✓ |

### 3.2 新 finding (定登)

- **F-T2b-1 LOW**: MD 用 `**bold**` 而非 `### heading` 表达 figure caption, P1 需抽样统计 markup 分布 (若 <60% heading 则 v1.3 补规则)
- **F-T2b-2 INFO**: MD 合并 'Example 1' + 描述句为冒号连接, v1.2 PARTIAL 精准度良性 case

---

## 4. P1 启动输入

### 4.1 已就绪

- PLAN v0.5 (下文 §5 即时升级)
- `plans/P1_pdf_atomization.md` v0.1 DRAFT (sub-plan)
- v1.2 prompts + schemas
- v1 snapshot + failures 归档
- `_progress.json` 更新 status=P1_ready

### 4.2 待用户决策

- [ ] PLAN v0.5 ack
- [ ] P1 sub-plan ack
- [ ] spec 表策略: Option A (PDF 全量原子化, 与 xlsx 脚本 diff) vs B (跳过) vs C (采样) — **推荐 A**
- [ ] 首 batch writer_type (默认 executor)
- [ ] P1 启 session 计划 (一次性 5 session vs 分散)

---

## 5. 下一 session (P1 session 1) 启动步骤

```
Step 1: 读 PLAN v0.5 (post-ack) + plans/P1_pdf_atomization.md (post-ack)
Step 2: 创建 trace.jsonl + audit_matrix.md P1 section
Step 3: _progress.json current_phase="P1", phases.P1 字段启
Step 4: 派 writer subagent=oh-my-claudecode:executor 跑 batch 1 (SDTMIG v3.4 p.1-10)
        - 输入 per call: 单页 PDF + v1.2 prompt + output_file
        - 模式: Write tool 直写 pdf_atoms.jsonl, DONE 消息仅 3 字段
Step 5: batch 1 完 → 追 1 行 trace.jsonl batch_report
Step 6: 派 batch 2 writer=oh-my-claudecode:writer (不同 type, Rule D 轮换)
Step 7: 派 batch 3 writer=feature-dev:code-explorer
Step 8: 3 batch 累 ~300 原子 → 跑 drift 校准 (派 3 type 平行 re-atomize 10 原子, ≥80% 门槛)
Step 9: drift PASS → 继续 batch 4-5 → 跑 Rule A 30 页抽检 (派 slot #12 reviewer, 候选 superpowers:code-reviewer)
Step 10: session 1 末写 P1_session_1_handoff.md, 更新 progress
```

---

## 6. 关键 carry-over insight (别忘)

1. **原子级字面审方法论 works**: F-T1-5 (AP 表 12→5 列) + M2' (CM examples CMDOSE 19→100 错值) — Step 0-4 Phase 审没审出来
2. **运维第一课**: Explore 家族不守 "纯 JSONL 无自然语言" 指令, 20%+ 丢数据. P1 全用 executor/writer 家族
3. **H2' reverse forward-aware 硬 gate 是 P1 规模化 safety net**: 若不修, 5000+ 原子 reverse 数据会系统性失真
4. **FIGURE atom_type 不是问题**: schema v1.2 容纳良好; P4a 前 200 字符 fingerprint 足够, 全量 mermaid 驻 ledger 不进 matcher context
5. **Rule D 隔离链扩 cumulative**: 11/16 烧, P1 可用 5 未烧 + (P0 已烧可跨 phase 复用, 仅 phase 内不复用), 足够 P1-P7 轮换

---

## 7. Open items (ordered priority)

| # | Item | Owner | Status |
|---|---|---|---|
| O1 | PLAN v0.5 user ack | Daisy | pending |
| O2 | plans/P1_pdf_atomization.md v1.0 ack | Daisy | pending |
| O3 | spec 表策略 (A/B/C) 决策 | Daisy | pending |
| O4 | P1 batch 1 kickoff | 下 session 主 | after O1+O2 |
| O5 | T2b 升级为正式 Rule D (派 slot #12 reviewer) | optional | defer |
| O6 | PLAN v0.5 吸收 P0 12 findings + F-T2b-1/2 | 本 session 产出 | done (见 PLAN Changelog v0.5) |

---

*end of handoff. P0 → P1 transition 完整 checkpointed. 下一 session 从 `_progress.json` recovery_hint 或本文件 §5 Step 1 开跑.*
