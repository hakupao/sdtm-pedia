# P0 Pilot T1 — 收官报告

> 日期: 2026-04-24
> 范围: T1 only (SDTM_v2.0.pdf p.50 + model/04_associated_persons.md 38 行)
> Gate verdict: **FAIL (70% Rule D < 80% 门槛) → 建议路线 B (升 prompt v1.1 + T1 回归)**

---

## 0. Executive Summary

P0 Pilot 按计划跑通 T1 完整流程 (writer ×2 → matcher ×2 → reviewer ×1), **产 42 原子 + 42 ledger entries + 1 section aggregate + 1 reviewer report**. Rule D reviewer 在 10 原子抽样上判 70% (FAIL), 定位出 **3 HIGH + 3 MEDIUM + 2 LOW bug**, **全部可通过 prompt v1.1 修复**, 无 PLAN 级架构缺陷.

**核心价值兑现**: 即便仅在 T1 (17 PDF + 25 MD 原子) 范围, pipeline 已端到端抓到 **真实 CONTENT_TRUNCATED 案例** — MD 版把 PDF 12 列 spec 表简化为 5 列, 丢失 Variable C-code / Format / Examples 等关键列, 这是 Step 0-4 "按节按要点"验证完全没审出来的. 证明 "原子级 + 字面级" 方法论本身 work.

**但**: Pilot 本身也暴露 matcher 有 3 类机制问题 (external knowledge 幻觉 + 正反向不一致 + KEYWORD 机制误用), 必须先修 prompt v1.1 再推 T2/T3, 否则 P1 会把 bug 放大 300×.

---

## 1. 数据流快照

| Step | Subagent Type | Rule D Slot | 输入 | 产物 | 状态 |
|---|---|---|---|---|---|
| PDF Writer | Explore | #3 (writer) | `SDTM_v2.0.pdf` p.50 | 17 原子 | ✅ 但 M1+M2 2 bug |
| MD Writer | oh-my-claudecode:explore | #4 (writer) | `model/04_associated_persons.md` 全 38 行 | 25 原子 | ✅ (T1 findings 4 minor, 非 blocking) |
| Forward Matcher | feature-dev:code-explorer | #5 (matcher) | 17 PDF + 25 MD | 17 ledger_forward | ⚠️ H1+H3 2 bug |
| Reverse Matcher | oh-my-claudecode:document-specialist | #6 (matcher) | 25 MD + 17 PDF | 25 ledger_reverse | ⚠️ H2 (与 forward 矛盾) |
| Section Aggregate | manual (main session) | — | ledger_forward | 1 section_coverage entry | ✅ |
| Rule D Reviewer | oh-my-claudecode:code-reviewer | #7 (reviewer) | 42 原子 + 42 ledger + PDF + MD | reviewer_report.md (70% FAIL) | ✅ |

**Rule D roster used (累计本 session)**: 
1. `oh-my-claudecode:critic` (PLAN v0.2 审)
2. `oh-my-claudecode:verifier` (PLAN v0.3 审)
3. `Explore` (T1 PDF writer)
4. `oh-my-claudecode:explore` (T1 MD writer)
5. `feature-dev:code-explorer` (T1 forward matcher)
6. `oh-my-claudecode:document-specialist` (T1 reverse matcher)
7. `oh-my-claudecode:code-reviewer` (T1 Rule D reviewer)

**7 种独立 subagent_type 烧** (目标 ≥15, 当前 7/15 + 9 可用池).

---

## 2. Section-level aggregate (§4 Associated Persons Data)

| 字段 | 值 |
|---|---|
| pdf_atom_count | 17 (含 1 HEADING) |
| md_atom_count_matched (EXACT + EQUIVALENT) | 8 |
| md_atom_count_partial | 8 |
| md_atom_count_missing | 1 |
| md_atom_count_synthesized (结构性标题 + metadata) | 6 |
| coverage_density (strict) | **0.47** |
| coverage_density (partial-weighted) | 0.71 |
| child_sections | {} (T1 PDF 单节, MD 的 `##`/`###` 均 SYNTHESIZED) |
| keyword_flag | **true** (shall/required/will 三处 Level 1 丢失, 但 H3 待纠正) |
| table_column_drop | 12 → 5 (丢 7 列, 含 Variable C-code) |
| **aggregate_verdict** | **`CONTENT_TRUNCATED`** |
| failure_patterns | [CONTENT_TRUNCATED, TABLE_COLUMN_COMPRESSED, KEYWORD_LEVEL1_MISSING] |
| gate_decision | MUST_OPEN_ISSUE 5 |

**即使 Rule D FAIL, F-T1-5 (table column drop) 与 a009 MISSING 两个核心发现在 reviewer 独判后依然成立** — 这些不是 matcher 机制 bug, 是真实的 KB 内容缺口.

---

## 3. 暴露的 bug 汇总

### HIGH (3, 必改 prompt v1.1 才能继续)

| ID | 涉及 | 根因 | Fix |
|---|---|---|---|
| H1 | `P0_matcher_v1.md` forward | matcher 在 `sv20_p0050_a012` discrepancy 里引入 "C55361" (APID 的 CDISC C-code), PDF p.50 上该列实际空白. LLM 从训练数据带入 external knowledge | prompt 强制 discrepancy 仅可引用 `source_atom.verbatim` 与 `candidate.verbatim` 两段字面文本, 禁引外部事实 |
| H2 | `P0_matcher_v1.md` forward + reverse | 正向 a009→MISSING, 反向却 md_a012/a013 SOURCED from a009. 逻辑矛盾 | 主 session 增脚本 `ledger_consistency_check.py`, 任何 "A→{} 但 {B,C}→A" flag 人工 |
| H3 | `P0_matcher_v1.md` | `[KEYWORD_MISSING: shall/required/will]` 三处, 但 PDF verbatim 实际不含字面词, matcher 把语义规则性缺失当成字面词缺失 | prompt 明示 KEYWORD_MISSING 仅当关键词在 PDF verbatim 中**字面出现**且 MD 未出现才标; 语义性规则缺失走 verdict 本身 |

### MEDIUM (3, 应改)

| ID | 涉及 | 根因 | Fix |
|---|---|---|---|
| M1 | `P0_writer_pdf_v1.md` | PDF p.50 "Associated Persons—Additional Identifier Variables" 表前 caption 是独立子标题, writer 未抽作 HEADING atom | writer prompt 加 "表前 bold caption / subsection heading 必作 HEADING atom" |
| M2 | `P0_writer_pdf_v1.md` | PDF a010 只抽 1 句 "The variables in the following table..." 但 PDF 跟有 2 句说明段落 (APID/RSUBJID/...), writer 按句号断章丢了 | writer prompt 改 "按段落断, 一段多句各成 SENTENCE atom, 不在句号处 early-stop" |
| M3 | `P0_matcher_v1.md` | PARTIAL 阈值 30-99% 过宽, `sv20_p0050_a005 → md_a009` 真实语义重叠 ~0.20 也被判 PARTIAL | prompt 硬 gate: PARTIAL 需 ≥0.50 真实语义重叠; <0.50 归 MISSING |

### LOW (2, 可延后)

| ID | Fix |
|---|---|
| L1 | schema 增 `cross_refs` 子字段 `link_target` 保留 hyperlink |
| L2 | SYNTHESIZED 细分 `_METADATA` vs `_STRUCTURE` |

### 原子类型覆盖缺口 (非 bug, 待 T2/T3)

T1 仅测 5/9: HEADING / SENTENCE / LIST_ITEM / TABLE_HEADER / TABLE_ROW
未测: **FIGURE / CROSS_REF / CODE_LITERAL / NOTE** — T2 (ch08 §8.2, 有 figure + cross_ref) + T3 (AE, 有 code_literal + note) 应能补

---

## 4. Schema 扩充建议 (→ v1.1)

verdict 枚举新增 2 个:
- `TABLE_SIMPLIFIED` (正向, 表结构从 M 列退化到 N<M)
- `EDITORIAL_ADDITION` (反向辅助标签, MD 添加的编辑说明)

`cross_refs` 字段扩:
- `link_target` (optional, hyperlink URL)
- `ref_type` (optional, "external_url" | "internal_section" | "figure")

SYNTHESIZED 可选细分 (v1.2+):
- `SYNTHESIZED_METADATA` (Source: ... / 版本号)
- `SYNTHESIZED_STRUCTURE` (KB 自加的 ## 标题)

---

## 5. P0 Gate Verdict

| Gate | 门槛 | 实测 | 结果 |
|---|---|---|---|
| 工具链可运行 | PASS | PASS | ✅ |
| 9 种原子类型 ≥6 种覆盖 | ≥6/9 | 5/9 | ❌ (单 target 原因, 非缺陷) |
| schema 可冻结 | YES | YES w/ v1.1 补丁 | ✅ |
| Rule D reviewer ≥80% | ≥80% | 70% | ❌ |
| subagent_type drift ≥80% | ≥80% | 未测 (T1 未跑 3-type 校准) | — |

**最终 Gate: ❌ FAIL (2/4 硬条件不过)**

**推荐下一步: 路线 B** — 升 prompt v1.1 (fix H1/H2/H3/M1/M2/M3) + schema v1.1 (TABLE_SIMPLIFIED + EDITORIAL_ADDITION) → T1 回归 → Rule D ≥80% → 再扩 T2/T3.

**不推荐**:
- 路线 A (原态扩 T2/T3): T2/T3 会遇同类 matcher 机制 bug, 规模性返工
- 路线 C (激进进 P1): bug 放大 300×, Issue 3 同类错误风险高

---

## 6. 下一步决策 (待用户)

**路线 B (推荐)**: 升 prompt v1.1 + schema v1.1 → T1 回归 → Gate PASS → 扩 T2/T3 → 真正冻结 schema → P0 结束

**路线 A**: 接受 T1 pilot 的 FAIL 作为 "已知 pilot 级偏差", 直接扩 T2/T3 用 v1 prompt + 同时修 v1.1 → 并行推进 (风险高, 但时间节省)

**路线 C**: 今天到此歇, 明天修 v1.1

路线 B 是最严谨路径. 用户拍板.

---

## 7. 数据资产清单 (本 Pilot 产出)

```
.work/06_deep_verification/evidence/checkpoints/
├── p0_T1_pdf_atoms.jsonl           (17 原子, 8954 bytes)
├── p0_T1_md_atoms.jsonl            (25 原子, 13226 bytes)
├── p0_T1_ledger_forward.jsonl      (17 entries)
├── p0_T1_ledger_reverse.jsonl      (25 entries)
├── p0_T1_section_aggregate.jsonl   (1 entry, §4 aggregate)
├── p0_T1_findings.md               (writer 阶段 7 finding)
├── p0_T1_reviewer_report.md        (Rule D slot #5 report)
└── p0_pilot_report.md              (本文件, 收官)
```

8 files total, Pilot 全数据 append-only.
