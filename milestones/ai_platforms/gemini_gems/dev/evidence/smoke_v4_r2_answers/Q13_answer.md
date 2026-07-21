# Gemini Gems — Q13 RWD/Observational + NS 前提 (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **题类**: Q13 (G1 bonus, AHP-V1 adjacent)
> **R1 baseline**: PARTIAL (0.5) post 13th reviewer A3 re-score (原 PASS, ARMCD 值错 + OBSERVATIONAL GROUP 虚构)

## Raw 回答

- **(a)** 3 类失效: Planned Treatment Rules (ARM) / Trial Design (TE/TA) / Timing Relative to Intervention (--STRF/--ENRF)
- **(b)** **ARMCD = "NOTASSGN"** ❌ / **ARM = "NOT ASSIGNED"** ❌ / **ARMNRS = "NOT APPLICABLE" (C66770)** ❌
- **(c)** SUPPQUAL + NSV 机制仍适用 (ch08 §8.4). NS 识破部分 (streaming partial)
- **(d)** (streaming tail) SUPPDM 补 observational 特有数据

## Self-score verdict

**PARTIAL (0.5)** — **与 R1 reviewer A3 verdict 同样 FAIL defect** + v6 未补 ARMCD null 锚

**FAIL 判据触发**:
1. **ARMCD = "NOTASSGN"** — SMOKE_V4.md L818 明文 FAIL 判据: "答 ARMCD 填 'NOTASSGN'" (错, CT 规范要求 ARMCD null + ARMNRS 填全称)
2. **ARM = "NOT ASSIGNED"** — 应 null (ARM 值 null, 语义在 ARMNRS)
3. **ARMNRS CT = C66770** — 错 codelist. 正确 codelist 是 **C142179** (ARMNRS Reason Arm Null, Ext=Yes, 值含 "NOT ASSIGNED"/"SCREEN FAILURE"/"ASSIGNED, NOT TREATED"/"UNPLANNED TREATMENT")

**保留点** (避免 FAIL 全评):
- (a) 3 类失效 conformance rule 合理 ✓
- (c) SUPPQUAL scope 正确 + NSV 机制
- NS identification 待 streaming 完成评判

**R1 vs R2 对比**: Gemini R2 复制 R1 (b) ARMCD/ARMNRS 同款错. v6 CO-4 未补 ARMCD-null 锚 (v6 只修 Q4/Q7/Q8/CO-5 AHP × 3, Q13 ARMCD 规则未覆盖). **Q13 是 v7 新 carry-over**.

**对 R1 reviewer A3 finding 的独立验证**: R1 13th reviewer (`pr-review-toolkit:code-reviewer`) confidence 82 down-score PASS → PARTIAL 的判断得到 R2 independent 复现证实 — Gemini 稳定在 ARMCD 规则上 FAIL, 非 R1 偶发, 是系统性 prompt gap.
