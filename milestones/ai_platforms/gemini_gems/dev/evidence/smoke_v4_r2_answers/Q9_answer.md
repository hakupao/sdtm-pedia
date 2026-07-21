# Gemini Gems — Q9 Pinnacle 21 FAIL 分类 (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/82ca29544421d25c
> **题类**: Q9 (E1 Pinnacle 21)
> **R1 baseline**: PASS

## Raw 回答

**6 大类 FAIL**:
- ① **Structural**: Variable not in SDTM model (e.g., LBCLSIG 非标变量)
- ② **Missing Required**: Req variable 空 (e.g., DM.ARMCD 空)
- ③ **CT Violations**: Value not in codelist (e.g., AESEV="VERY SEVERE" 非 {MILD/MODERATE/SEVERE})
- ④ **Date Logic / ISO 8601**: AEENDTC < AESTDTC; 格式错 (01-JAN-2026 vs 2026-01-01)
- ⑤ **Cross-Domain**: USUBJID in EX not in DM (DM 锚点)
- ⑥ **RELREC & SUPP-- Errors** (streaming partial)

**修 vs 文档化决策** (expected tail of answer): 真数据错 → 修; 标准不匹配但数据真实 (如 RWD 无 planned arm / sponsor legit extension) → Reviewers Guide (csdrg.pdf) 文档化保留.

## Self-score verdict

**PASS** — 6 大类 ≥ PASS 阈 5 + 每类典型例子 + 结构/Req/CT/Date/Cross-Domain/RELREC 5 大类核心命中. Example "LBCLSIG" 与 AHP1 NSV 路径一致 (非臆造). R1 对齐 PASS.
