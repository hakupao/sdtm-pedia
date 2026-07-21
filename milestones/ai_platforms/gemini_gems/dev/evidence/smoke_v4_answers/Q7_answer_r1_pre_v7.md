# Gemini Q7 answer — Partial date SDTM/ADaM

**Verdict**: **PARTIAL (0.5)** — 3 场景+(d) 对, 但 (e) 有**关键 layer 混淆幻觉** (称 SDTM 要记 --DTF, 实际 --DTF 是 ADaM-only)

## 3 场景填写 ✓

| 场景 | 填值 | 原则 |
|---|---|---|
| A: AE 2024-06 无日 | `"2024-06"` | 保留已知精度, 省略日 |
| B: CM 2024 无月日 | `"2024"` | 仅保留年 |
| C: 完全 Unknown | NULL (空值) | 可用 --STRF / --STRTPT 描述时序 (如 "BEFORE") |

## (d) SDTM --STDTC imputation? ✓
**不需要**. 原则: 如实反映原始收集数据 (Data as originally collected). SDTMIG 明确不应在 SDTM 变量中进行日期补录. Epoch 可依 CRF 结构 assign, 不通过补日期实现.

## (e) ADaM imputation 时 SDTM 额外记什么? ✗ **HALLUCINATION**

Gemini 答: "需要记录 --DTF (Date/Time Imputation Flag), 如 AEDTF 或 CMDTF".

**❌ 错误**:
1. **--DTF 不是 SDTM 变量** — 是 ADaM 级 (ASTDTF / AENDTF 等 ADaM IG v1.3 §3.1.4 定义)
2. **AEDTF / CMDTF 不存在于 SDTMIG v3.4 任何域 spec**
3. 正确做法 (Claude/ChatGPT 答): SDTM **保持 partial date 忠实如实**, 不加 imputation flag 列; ADaM 在自己的 ASTDTF 做派生 + 记 Y/M/D imputation flag

Gemini 把 ADaM *DTF 机制误植入 SDTM 层, 违反 SDTMIG §4.4.2 "SDTM 不做 imputation" 的边界原则.

## 源路径 (Gemini 给出)
- ch04_general_assumptions.md §4.4.1 (ISO 8601)
- ch04 §4.4.2 (Date/Time Precision)
- ch04 §4.1.3.1 (EPOCH & Imputation Guidance)
- VARIABLE_INDEX.md §Timing Variables (--DTF role) ← **此条为虚构 path reference**

## 评分要点
- ✓ 3 场景全对 (2024-06/2024/null)
- ✓ (d) SDTM 不 imputation + 原则正确
- ✗ **(e) 层混淆幻觉** — 误称 SDTM 有 --DTF 变量
- △ 未提相对 timing 变量完整清单 (--STRTPT/--STTPT/--ENRTPT/--ENTPT)
- △ 未提 solidus 区间表达
- △ 未显式 §4.4.7 Example 3 范本

## R2 改 prompt 建议
system prompt 加锚点: "SDTM does NOT have --DTF variable; --DTF is ADaM-only. SDTM preserves partial date as-is; imputation flag belongs in ADaM ASTDTF/AENDTF."

## 与其他平台对比
- ChatGPT: PASS+ (3 场景 + §4.4.2 锚点 + 相对 timing 清单 + SDTM/ADaM 边界清晰)
- Claude: PASS+ (3 场景 + §4.4.2 truncation 表 + Solidus 区间 + §4.4.7 Ex3 AE Unknown 范本 + ADaM ASTDTF 机制正确引为"超 Project 范围")
- Gemini: PARTIAL (3 场景对, (e) 把 ADaM *DTF 误植入 SDTM)
