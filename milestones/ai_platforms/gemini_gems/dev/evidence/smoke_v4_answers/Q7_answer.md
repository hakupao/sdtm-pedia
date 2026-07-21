# Gemini Gems — Q7 Partial Date + SDTM vs ADaM imputation (V5C post-apply v7 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/61dd423872acb8bc
> **题类**: Q7 (C2 — Partial date 精度)

## Raw (DOM readback)

根据 SDTMIG v3.4 ISO 8601 规范及 Chapter 4 通用假设:

### 1. 场景填充

SDTM 日期变量 (--DTC) 保持收集到的原始精度, 不臆造.

| 场景 | 归域 | 变量填充 | 处理逻辑 |
|---|---|---|---|
| A. AE 开始于 2024 年 6 月 | AE | **AESTDTC="2024-06"** | 只保"年-月"精度 |
| B. 服药 2024 年 | CM | **CMSTDTC="2024"** | 只保"年"精度 |
| C. AE 开始日完全未知 | AE | **AESTDTC=null** | 日期完全缺失设 null |

### 2. 规则解析

- **(d) SDTM --STDTC 需要 imputation?** **不需要**. SDTM 是 Tabulation 层, 职责是忠实反映采集原始数据. SDTM 变量**严禁** imputation. 任何补齐必须在 ADaM 完成.
- **(e) ADaM imputation 时 SDTM 要记什么?** **不需要**. **--DTF** (如 AEDTF / CMDTF) 不是 SDTM standard variable. ADaM 创建对应 ASTDTF/AENDTF 标记补齐精度. SDTM 边界: 不记补齐标记, 也不提供 Imputation Flag 标准位置. 若 sponsor 认为非标 metadata 必须提交, 走 SUPP-- 路径 (但标准实践应留 ADaM 处理).

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §4.1.4.1 (Date/Time Formats); `AE/spec.md` §AESTDTC; `CM/spec.md` §CMSTDTC

**依据**: ISO 8601 精度 (YYYY / YYYY-MM / YYYY-MM-DD); SDTM vs ADaM 边界 (Imputation 是 ADaM 核心任务, SDTM 只展示原始 tabulation)

## Self-score verdict

- **Verdict**: **PASS**
- **对照 PASS 判据**:
  - A "2024-06" ✓
  - B "2024" ✓
  - C null ✓
  - (d) SDTM 不做 imputation ✓
  - (e) --DTF 不是 SDTM standard; ADaM 创 ASTDTF; SUPP-- 可选 ✓
- **触发 FAIL?** 无
- **加分**:
  - 明确说 --DTF 不是 SDTM standard (精确 anti-hallucination)
  - SDTM vs ADaM 边界明确
- **v5c→v7 delta**: 无 regression. Gemini 比 ChatGPT 简洁但精度同等.
