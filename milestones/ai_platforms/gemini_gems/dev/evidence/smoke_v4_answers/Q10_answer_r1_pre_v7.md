# Q10 — SUPPTS 前提纠错 (Gemini Gems, smoke v4 R1, 2026-04-22 晚)

> Verdict: **PASS** (premise correction 识破 SUPPTS, 但 (a) Core attr Perm 错为 minor)

## Prompt (v4.0)
(同 SMOKE_V4.md §2 Q10)

## Raw Answer (Gemini SDTM Expert Gem)

作为 SDTM Expert，针对 SUPP-- (Supplemental Qualifiers) 家族的结构与业务逻辑，基于 knowledge_base/chapters/ch04_general_assumptions.md 和各域 spec 的规则，回答如下：

### (a) QORIG 与 QEVAL 的填写规则与含义

这两个变量在 SUPP-- 中通常为 **Permissible (Perm)**，但具有明确的业务指导意义：

| 变量 | 含义 | 必填/填法场景 |
|---|---|---|
| QORIG | Origin (数据来源) | 建议必填。用于追溯该非标变量的源头。取值常为 CRF（来自原始采集）、DERIVED（系统计算）、ASSIGNED（人工指派）或 PROTOCOL。|
| QEVAL | Evaluator (评价者) | 按需填写。当 QVAL 的值带有主观判断属性时必填（如 AE 的严重性由谁判定）。常用值如 INVESTIGATOR、INDEPENDENT ASSESSOR。如果数据是客观测量结果（如 lab），通常留空。|

### (b) SUPPQUAL 适用范围与 TS 长文本处理

**SUPPQUAL 适用范围**: 在 SDTMIG v3.4 中, SUPP-- 机制适用于 General Observation Classes (Events, Interventions, Findings) 以及部分 Special Purpose 域（如 DM）. 它用于存储父域中无法容纳的"非标准变量"(NSVs).

**Trial Design (如 TS) 的长文本处理**:
- **重点: Trial Design 域 (TS, TA, TE, TV, TI) 通常不使用 SUPP-- 机制.**
- **TS 记录方式**: TS 域本身的设计就是"三元组"(TSPARMCD, TSPARM, TSVAL). 如果 TSVAL 的值超过 200 字符, **严禁使用 SUPPTS (SDTM 标准中不存在 SUPPTS)**.
- **处理规则**: 根据 ch04_general_assumptions.md §4.5.3.2, 长文本应在 TSVAL 中存入前 200 字符, 余下部分依次存入 **TSVAL1, TSVAL2... TSVALn**. 这些变量 (TSVAL1-n) 是 TS 域的水平扩展变量, 而非 SUPP 记录.

### (c) SUPPAE 定位父记录的逻辑

SUPPAE 通过以下 Identifier 变量链条与父域 AE 实现"主从关联":
- **RDOMAIN**: 填父域代码 "AE", 指明补充的是 AE 域的数据
- **USUBJID**: 核心键值. 确保补充信息关联到正确的受试者
- **IDVAR**: 存放父域中用于唯一标识记录的变量名, 通常填 "AESEQ"
- **IDVARVAL**: 存放该变量具体的值
- **注意**: 即便 AESEQ 在 AE 域是数值型, 在 SUPPAE.IDVARVAL 中也必须转为字符型 (如 "5")

**定位公式**: SUPPAE (USUBJID + IDVAR + IDVARVAL) ⇔ AE (USUBJID + AESEQ)

### (d) QVAL 长度上限与拆分规则

**长度上限**: 单个 QVAL 变量的长度上限是 200 字符 (这是 SAS Transport XPT v5 文件的标准限制).

**超过 200 字符的拆分 (Long Text Truncation)**:
- 第一段 (1-200 字符) 存入 QNAM = "XXXX" 的 QVAL
- 后续段落存入 QNAM 带有 1 位数字后缀 的新记录中: "XXXX1", "XXXX2"... 以此类推
- **示例**: 如果备注 (QNAM="AEREMARK") 长 350 字符, SUPPAE 中会有两条记录, QNAM 分别为 "AEREMARK" 和 "AEREMAR1" (8-char truncate rule)

**源路径**:
- knowledge_base/chapters/ch04_general_assumptions.md §4.5.3.2 (Long Text), §8.4 (SUPP)
- knowledge_base/domains/TS/spec.md (TSVAL 扩展规则)
- knowledge_base/domains/AE/spec.md (AESEQ 关联规则)

## Verdict 打分

| 判据 | 结果 |
|---|---|
| (a) QORIG Req / QEVAL Exp | ❌ 说 Perm (业务对, Core attr 硬伤) |
| (b) SUPPQUAL scope = GOC + DM + SV | ⚠️ GOC + DM, 漏 SV |
| (b) **识破 SUPPTS 前提错 + TSVAL1-n** | ✅✅ **premise correction caught** |
| (c) RDOMAIN + IDVAR + IDVARVAL + USUBJID | ✅ (多给 数值→字符 细节) |
| (d) 200 字符 + QNAM 后缀 + 8-char truncate | ✅ (示例 AEREMAR1 精准) |
| FAIL triggers | 无 (Perm 错不触 FAIL 判据) |

**最终**: **PASS** (1 分)
- SUPPTS 前提纠错 caught → 原本应 PASS+ bonus
- 但 (a) Core=Perm 硬伤 (判据 PASS 要 Req/Exp) 抵消 bonus
- SV 漏一项也是 minor

**R2 改点**:
1. System prompt 加 "QORIG Core=Req 始终必填 / QEVAL Core=Exp 主观判断时填" 锚点
2. SUPPQUAL scope 加 "+ SV (Subject Visits)" 锚点

## Citations in answer
ch04 §4.5.3.2 + §8.4 / TS/spec / AE/spec — attribution 合理
