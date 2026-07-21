# Q7 — Gemini SDTM Expert 回答 (C2 — Partial date + Imputation 职责)

> 期望核心: A=2024-06 + B=2024 + C=null + (d) SDTM 不 imputation + (e) ADaM 做 ASTDT/AENDT + ADTF flag
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/913c953039b0f7d5
> 时间: 2026-04-22
> Mode: Pro

## 完整回答

### 结论

在 SDTM 中，时间变量（如 --STDTC, --ENDTC, --DTC）必须遵循 ISO 8601 格式标准。ISO 8601 原生支持通过"从右向左截断"来表达不完整的时间（Partial Dates），而无需使用占位符。

同时，SDTM 层面绝对不进行 Date/Time Imputation（插补）。SDTM 的核心原则是"如实反映收集到的原始数据"（As Collected）。所有的插补逻辑、插补后的数值以及插补标识（Imputation Flags）都属于分析需求，必须在 ADaM 中实现。

### 场景解答

- **场景 A** ("AE 开始于 2024 年 6 月", 无日): **2024-06**。直接截去缺失的日部分，保留 YYYY-MM。
- **场景 B** ("服药开始于 2024 年", 无月日): **2024**。截去缺失的月和日部分，仅保留 YYYY。
- **场景 C** (完全未知): **留空 (Null / Missing)**。不能填 UK、UNK 或 U 等非 ISO 8601 字符。如有收集到类似"未知"的文本选项且确需保留原始勾选痕迹，通常在 EDC 层面解决，或在特定情况下记录于 SUPP--，但主域的 --STDTC 必须留空。

### 附加问题解答

(d) **SDTM 的 --STDTC 需要做 imputation 吗？**
不需要，也绝不允许。SDTMIG 明确规定数据呈现应反映实际收集的信息。对于不完整的日期，在 SDTM 中就应该保持为 Partial Date（如 2024-06）。Imputation 是为了推导分析基准（如计算准确的 Study Day 或 Duration），这是统计分析的范畴。

(e) **如果 ADaM 需要 imputation, SDTM 还需要额外记什么吗？**
不需要。SDTM 不需要为 ADaM 的插补行为做任何预设或额外记录。在 ADaM (ADAE, ADCM 等) 阶段，ADaM 程序员会读取 SDTM 中的 partial --STDTC，根据 SAP (Statistical Analysis Plan) 的规则生成完整的分析日期（如 ASTDT / AENDT），并同步生成对应的分析级别插补标识符（如 ASTDTF / AENDTF 来标记补了年、月还是日）。这些推导变量完全属于 ADaM 域。

### 依据与溯源

- SDTMIG v3.4 明确指出所有日期时间变量必须符合 ISO 8601 标准。
- 源路径: knowledge_base/chapters/ch04_general_assumptions.md Section 4.1.4 (Dates, Times, and Date/Times 规则说明)

## 判据对齐

| 维度 | 期望 | 实际 | Hit |
|------|------|------|-----|
| A 年月 | "2024-06" | "2024-06" | ✅ |
| B 年 | "2024" | "2024" | ✅ |
| C 完全未知 | null / 空 (禁 "UNKNOWN") | Null/Missing + 明确禁 UK/UNK/U + SUPP-- 可选兜底 | ✅ |
| (d) SDTM 不 imputation | SDTM 保真不 imputation | "不需要, 也绝不允许" + "As Collected" 原则 | ✅ |
| (e) ADaM imputation flag | ASTDT / AENDT + ADTF flag | ASTDT/AENDT + ASTDTF/AENDTF + SAP 驱动 | ✅ |

## Verdict

**PASS** — 3 场景 + 2 附加问题全部精准命中. Partial date ISO 8601 "从右向左截断" 原则正确 + SDTM/ADaM 职责边界清晰 + Imputation flag 命名 (ASTDTF/AENDTF) 具体且符合 ADaM 实践. "As Collected" vs "Analysis Derivation" 的哲学对比到位. Pure generalization 完成度高.

- 04 引用: 0 次 (仅 ch04 §4.1.4 ISO 基础, 非 04 业务弹药包)
- CO-2 触发: 无
- Score: 1 / 1
