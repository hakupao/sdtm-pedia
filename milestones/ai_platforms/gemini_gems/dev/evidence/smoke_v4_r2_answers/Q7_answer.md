# Gemini Gems — Q7 Partial Date + ADaM 边界 (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/d8cbade729ca7909
> **题类**: Q7 (C2 Partial date, R1 PARTIAL)
> **R1 baseline**: PARTIAL (未显式 --DTF ADaM-only)
> **v6 target fix**: "SDTM vs ADaM 边界 --DTF ADaM-only" 明示

## Raw 回答

- **A (2024-06)**: AESTDTC = "2024-06" ✓
- **B (2024)**: CMSTDTC = "2024" ✓
- **C (Unknown)**: null (空值) ✓
- **(d) SDTM --STDTC 不做 imputation** — SDTM 保原始精度 (YYYY-MM-DD / YYYY-MM / YYYY). Imputation 是 ADaM 层职责 (派生 ASTDT)
- **(e) --DTF 属 ADaM-only** (AEDTF / CMDTF 对应 ADaM 标准 ASTDTF / AENDTF), **不是 SDTM 标准变量**. SDTM 职责仅反映精度缺失 — "2024-06" 本身向 ADaM 传递"日"缺失信息, 不需额外 flag

## Self-score verdict

**PASS** — **R1 PARTIAL → R2 PASS 修复生效**

- 3 场景日期 null/YYYY/YYYY-MM 全对 ✓
- (d) SDTM 不 imputation ✓ + ADaM 派生变量名 ASTDT ✓
- **(e) v6 "--DTF ADaM-only" 规则明确生效** — 显式标 "AEDTF/CMDTF 是 ADaM-only" + 对应 ADaM 标准变量名 ASTDTF/AENDTF ✓
- ISO 8601 部分精度 3 档规则

**R1 vs R2**: PARTIAL → PASS. **v6 Q7 micro-fix 明确生效**. 关键改善: 显式识别 --DTF 是 ADaM-only 非 SDTM, 给出 ASTDTF/AENDTF 对应名.
