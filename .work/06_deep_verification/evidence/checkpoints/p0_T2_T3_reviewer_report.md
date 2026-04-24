# P0 Pilot T2+T3 Rule D Reviewer Report

- **Reviewer**: `feature-dev:code-reviewer` (Rule D slot #11)
- **Sample**: 16 原子 (T2×8 + T3×8)
- **Date**: 2026-04-24
- **Mode**: 只读独立判, 基于 atom/ledger 数据 (未读 PDF 视觉 — 本次评估足够)

## 总体

| 指标 | 值 |
|---|---|
| CONFIRM | 13 |
| OVERRIDE | 2 |
| AMBIGUOUS | 1 |
| Matcher 准确率 | (13 + 1×0.5) / 16 = **81.25%** |
| **Rule D PASS ≥80%** | ✅ **PASS** |

## v1.1 Fix 持续验证

| Fix | T1 v1.1 | T2 | T3 |
|---|---|---|---|
| H1 禁外部知识 | ✅ | 0/8 violation | 0/8 violation |
| H3 KEYWORD 字面 | ✅ | 2/8 含 (见 M1) | 0/8 |
| M3 PARTIAL ≥0.50 | ✅ | 7/7 ≥0.50 | 3/3 ≥0.50 |
| TABLE_SIMPLIFIED | ✅ T1 | T2=0 (md 保全列) | T3=1 (AE 表格→散文) |

## 新 findings (T2+T3 首次暴露)

### [HIGH] H1 — CODE_LITERAL 被 MD writer 误分类为 NOTE (cm.xpt 案例)
PDF a017 `cm.xpt` = CODE_LITERAL; MD a038 `cm.xpt:` = NOTE (writer 加了冒号后归 NOTE). Matcher 宽判 EQUIVALENT 0.92 掩盖. P1 需 writer prompt 明示 `*.xpt` / codelist 常量必 CODE_LITERAL.

### [HIGH] H2 — Reverse ledger verdict/field 不一致 bug
T3 reverse a002-a005 的 `pdf_atom_ids` 非空但 verdict=UNSOURCED. 内部矛盾: matcher 既找到对应又宣告无源. **Reverse matcher 须 forward pass 后跑, 用 forward 结果校验 reverse verdict**. P1 前必修.

### [MEDIUM] M1 — KEYWORD_MISSING 错标为 PDF typo 修正
T2 a013/a015 标 `[KEYWORD_MISSING: GMGRPID]` 但 PDF `GMGRPID` 是 typo (应 `CMGRPID`, CM domain 的 Group ID). MD 修正 typo = 好事, 但 matcher 反着标. 需新 verdict **`EDITORIAL_CORRECTION`** 区分 "MD 修正 PDF typo" 与 "MD 内容缺失".

### [MEDIUM] M2 — MD 示例表数据精度损失 (CMDOSE 19→100, "Generic Med A"→"Generic Med")
T2 TABLE_ROW a019-a021 判 PARTIAL 0.72. **这是真数据 corruption**: MD writer 重建示例表时截断字段或改数字, 属规范示例不可接受的错误. 建议 P1 对 examples.md 全表做字面 diff.

### [MEDIUM] M3 — CROSS_REF 多对一映射致 reverse 不对称
T3 PDF a014/a017 (完全相同的 §4.4.7 cross-ref) 都 forward EQUIVALENT to MD a038, 但 a038 reverse 判 UNSOURCED 0.11. Reverse matcher 未参考 forward 结果.

### [LOW] M4 / M5 — 结构性 MISSING (非质量问题)
T3 大量 CODE_LITERAL MISSING (ISO 8601, RFSTDTC 等) 是因为 AE 变量定义在 `domains/AE/variables.md` 而非 `assumptions.md`. P1 要按文件类型配对比对域.

## P0 Pilot 整体 Gate

| 条件 | 结果 |
|---|---|
| Rule D ≥80% | ✅ **81.25%** |
| 9 种原子 ≥6 种 | ✅ **8/9** (FIGURE 缺, 接受延后 P1) |
| schema 可冻结 | ⚠️ **CONDITIONAL** (+EDITORIAL_CORRECTION verdict) |
| v1.1 fix 在 T2/T3 持续 | ✅ |
| **最终** | **CONDITIONAL_PASS** — FIGURE P1 抽样验, Finding H2 P1 前必修 |

## 下一步建议

1. **FIGURE 延后到 P1 抽样** (不阻塞 P0 收尾)
2. **P1 前必修 H2** (reverse forward-aware 一致性 gate)
3. **v1.2 新增 `EDITORIAL_CORRECTION` verdict** (PDF typo 修正场景)
4. **v1.2 writer prompt 扩**: *.xpt 文件名必 CODE_LITERAL
5. **T3 结构性 MISSING 问题**: P1 要调配对策略 (变量 in variables.md, 非 assumptions.md)
