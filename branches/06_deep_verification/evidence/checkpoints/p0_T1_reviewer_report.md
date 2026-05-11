# P0 Pilot T1 — Rule D Reviewer Report

- **Reviewer**: `oh-my-claudecode:code-reviewer` (Rule D slot #5)
- **Sample**: 10 原子 (6 forward + 2 forward PARTIAL + 2 reverse, 分层)
- **Date**: 2026-04-24
- **Mode**: 只读独立判, 先独判再对比 matcher
- **Sources checked**: `SDTM_v2.0.pdf` p.50 (视觉确认) + `knowledge_base/model/04_associated_persons.md`

---

## 总体

| 指标 | 值 |
|---|---|
| CONFIRM | 6 |
| OVERRIDE | 2 |
| AMBIGUOUS | 2 |
| Matcher 准确率 | (6 + 2×0.5) / 10 = **70%** |
| **Rule D PASS 门槛 ≥80%** | ❌ **FAIL (70%)** |

**结论速览**: matcher 内容判断大体合理, 但 (a) KEYWORD_MISSING 标记机制误用导致两处噪声 flag, (b) verdict 枚举缺 `TABLE_SIMPLIFIED` / `EDITORIAL_ADDITION` 两类边界的专门表达, (c) 一处 MISSING 判定在更严的 pilot context 下应是 PARTIAL. 这些是**机制问题, 非内容判读失败**. 建议升 prompt v1.1 + 扩 schema 后回归.

---

## 逐条 10 原子 (摘要, 全文见 session transcript)

### 1. `sv20_p0050_a009` (MISSING + KEYWORD shall) — **AMBIGUOUS, 倾向 PARTIAL**
- PDF verbatim 不含字面 "shall", matcher 的 `[KEYWORD_MISSING: shall]` 是**语义联想**非字面事实
- 正反向 ledger **矛盾**: 反向说 md_a012/a013 SOURCED from a009, 正向说 a009 MISSING
- Issue HIGH (H2 + H3)

### 2. `sv20_p0050_a011` (TABLE_HEADER PARTIAL 0.42) — CONFIRM
- 但 verdict 枚举缺类: 应有 `TABLE_SIMPLIFIED` 专门表结构退化 (12→5 列) 的情形
- Issue MEDIUM (schema 扩充)

### 3. `sv20_p0050_a012` (APID TABLE_ROW PARTIAL 0.72) — **OVERRIDE → AMBIGUOUS, 倾向 EQUIVALENT**
- APID 所有有信息列保留, 丢的是空列 + 行号 metadata
- **matcher discrepancy 里主张 "C55361 absent in MD" 是幻觉** — PDF p.50 上 APID 行 Variable C-code 列实际也是空的, C55361 从未在 atom.verbatim 出现
- Issue HIGH (H1) — discrepancy 引入 external knowledge

### 4. `sv20_p0050_a002` (EXACT 1.0) — CONFIRM ✓

### 5. `sv20_p0050_a001` (EQUIVALENT heading) — CONFIRM ✓

### 6. `sv20_p0050_a016` (EXACT 1.0) — CONFIRM (LOW: hyperlink 丢失未记)

### 7. `sv20_p0050_a005` (PARTIAL 0.45 non-table) — **OVERRIDE → MISSING**
- PDF a005 说"implementers will follow AP assumptions for Identifier variables"
- matcher 关联到 MD a009 "APID 移出 Section 3.1.4", 主题完全不同, 只共享名词
- 真实语义重叠 ≤0.20, 应 MISSING 非 PARTIAL
- Issue MEDIUM (M3) — PARTIAL 阈值过宽

### 8. `sv20_p0050_a008` (PARTIAL 0.60) — CONFIRM ✓

### 9. `md_model_04_a002` (SYNTHESIZED Source metadata) — CONFIRM ✓

### 10. `md_model_04_a003` (SYNTHESIZED Overview heading) — CONFIRM ✓

---

## Schema 冻结建议

| 项 | 判定 |
|---|---|
| 原子 schema 字段完备 | **YES** |
| `atom_type` 9 种够用 | **PARTIAL** — 仅测到 5 种, FIGURE/CROSS_REF/CODE_LITERAL/NOTE 未覆盖 (pilot 单页原因, 非缺陷) |
| verdict 枚举够用 | **NO, 建议 v1.1 补丁** |

**v1.1 补丁 (新增 verdict + 机制)**:
1. **`TABLE_SIMPLIFIED`** — 表结构从 M 列退化到 N 列 (N<M) 专用. PARTIAL 留给非表格场景.
2. **`EDITORIAL_ADDITION`** (辅助标签) — MD 添加的编辑说明 (如 md_a009 "APID was removed from Section 3.1.4"), 机读记录.
3. **KEYWORD_MISSING 机制收紧** — 仅当关键词字面在 PDF verbatim 出现且 MD 未出现时才标, 禁止"语义联想"触发.

**是否冻结 schema**: **YES with v1.1 小补丁**

---

## 改进建议 (→ prompt v1.1)

### P0 必改 (HIGH)

**H1. matcher discrepancy 禁入 external knowledge** — `sv20_p0050_a012` 引入 "C55361" 是经典幻觉. Fix: discrepancy 模板严格限制在 "diff PDF atom.verbatim 与 MD atom.verbatim 两段文字本身", 禁引 CT/CDISC 外部事实.

**H2. 正反向 ledger 一致性 gate** — `sv20_p0050_a009` 正向 MISSING 但反向 md_a012/a013 双双 SOURCED from a009, 矛盾. Fix: matcher 收尾跑对齐脚本, 任何 "A→{} 但 {B,C}→A" flag 人工复核.

**H3. KEYWORD_MISSING 字面化** — 当前把语义性缺失错编为字面词 missing. Fix: matcher prompt 明示仅当关键词在 atom.verbatim 中**字面出现**才可标.

### P1 应改 (MEDIUM)

**M1. PDF writer 漏表前 caption HEADING** — PDF p.50 "Associated Persons—Additional Identifier Variables" 表格子标题是 HEADING 原子但 writer 未生成. Fix: writer prompt 加 "表前 bold caption / section heading 单独提取为 HEADING atom".

**M2. PDF writer 句号断章漏** — a010 只写 1 句但 PDF 跟有 2 句说明 (APID/RSUBJID/RDEVID/SREL 段落). Fix: writer 按 paragraph 断非句号.

**M3. PARTIAL 阈值下限 ≥0.50** — a005→a009 的 0.45 实际语义重叠 ~0.20 不该是 PARTIAL. Fix: PARTIAL ≥0.50 真实重叠 hard gate.

### P2 建议 (LOW)

**L1. Hyperlink 保留** — cross_refs 字段可扩 `link_target`.
**L2. SYNTHESIZED 细分** — `SYNTHESIZED_METADATA` vs `SYNTHESIZED_STRUCTURE`.

---

## P0 Gate 建议

| Gate | 状态 |
|---|---|
| 工具链可运行 | ✅ PASS |
| 9 种原子类型 ≥6 种覆盖 | ❌ FAIL (5/9) |
| schema 可冻结 | ✅ YES w/ v1.1 补丁 |
| Rule D ≥80% | ❌ FAIL (70%) |
| subagent_type drift ≥80% | 未测 |

**最终 Gate 建议: 路线 B** — 升 prompt v1.1 按 H1/H2/H3/M1/M2/M3 修 → 同 T1 回归.

理由: Rule D 70% < 80% 门槛, 但 OVERRIDE 根因**集中在 matcher discrepancy 机制问题** (C55361 幻觉 + KEYWORD_MISSING 机制误用 + PARTIAL 阈值过宽), 非题库/抽样缺陷. 修 v1.1 后 T1 同页回归, 若 ≥80% 再扩 T2/T3 补剩余原子类型 + drift 校准.

**不建议路线 C (激进直进 P1)**: 机制 bug 放大 300× (17 → ~5000 原子) 代价过高.

**不建议路线 A (原态扩 T2/T3)**: T2/T3 会遇同类 C-code 幻觉 + keyword 误标, 返工成本更高.

---

## 总体 findings (按严重度)

**HIGH (3)**:
- H1 matcher 引入 "C55361" external knowledge 幻觉
- H2 正反向 ledger 矛盾 (a009)
- H3 KEYWORD_MISSING 机制误标 (shall/required/will 三处)

**MEDIUM (3)**:
- M1 PDF writer 漏表格 caption HEADING
- M2 PDF writer a010 paragraph 断章漏 2 句
- M3 PARTIAL 阈值过宽 (建议 ≥0.50)

**LOW (2)**:
- L1 hyperlink 保留
- L2 SYNTHESIZED 细分

---

## Rule D 合规声明

- slot #5 subagent_type: `oh-my-claudecode:code-reviewer` ✓
- 与前 4 atom-level slot 不同 type ✓ (Explore / oh-my-claudecode:explore / feature-dev:code-explorer / oh-my-claudecode:document-specialist)
- 独判后再对比 matcher ✓
- 只读, 未 Write 文件 ✓
- 未读 PLAN.md ✓
- 所有 verdict 附 PDF/MD 证据 ✓

**Rule D PASS 门槛 (≥80%): ❌ FAIL at 70%. 建议路线 B 升 v1.1 回归.**
