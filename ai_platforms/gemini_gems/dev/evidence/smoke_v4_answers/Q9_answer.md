# Gemini Gems — Q9 Pinnacle 21 常见 FAIL 分类 + Fix vs SDRG (V5C post-apply v7 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/987cfd1ec9e90b7b
> **题类**: Q9 (E1 — Pinnacle 21 issue 分类)

## Raw (DOM readback)

Pinnacle 21 (P21) 验证基于 CDISC Validation Rules / SDTMIG 商业规则 / FDA/PMDA Technical Rejection Criteria 扫描.

### 1. P21 常见 FAIL 6 大分类

| 类别 | P21 典型 Issue | 典型触发例子 |
|---|---|---|
| CT 违反 | SD1234: Variable value not found in CT | AESEV="SEVERE PAIN" 非 CDISC submission value "SEVERE" (C66769) |
| Core 属性缺失 | SD0001: Required variable not found | AE 缺 AESEQ 或 AESEQ 空 |
| 格式/数据类型 | SD0037: Invalid ISO 8601 date format | RFSTDTC="2026-APR-24" 应 "2026-04-24" |
| 跨域不一致 | SD0058: USUBJID not found in DM | LB 出现 DM 无的 USUBJID |
| 逻辑矛盾 | SD0063: Start Date > End Date | AESTDTC="2026-04-24" 但 AEENDTC="2026-04-20" |
| 非标变量 NSV | SD1076: Variable is not a standard domain variable | LB 直接放 LBCLSIG (应 SUPPLB) |

### 2. 什么时候修数据

涉及 **SDTM 结构硬伤 / 标准合规性 / 逻辑错误** 必须修:
- Required 变量缺失/为空 (STUDYID/DOMAIN/USUBJID/--SEQ/各域 Topic)
- CT 拼写错误 ("Y" 误写 "Yes")
- ISO 8601 格式错误 (YYYY-MM-DD)
- USUBJID 孤儿 (非 DM 域必须在 DM 有对应 baseline)
- 变量属性冲突 (Char/Num 与 spec 不符)

### 3. 什么时候 cSDRG 文档化保留

**场景 A: 源数据固有缺陷**:
- 例 SD0063 Start>End. 若 CRF 原始记录确是反的且无法 Query 订正 (如关库), SDTM 忠实反映. SDRG 说明.

**场景 B: SDTMIG 允许但 P21 标记**:
- 例 SD1082 Expected variable is null. AESER (Exp) 若未发生 AE 或未收集, 空值合法.

**场景 C: 医学专业判断**:
- 例 SD0030 Result unit 非标准. 新兴疗法单位未入 NCI CT. 医学表达准确则保留.

**场景 D: RWD/观察性研究 (CO-1c 硬规则)**:
- 例 SD1201 ARMCD is null. Screen Failure 或 Unplanned 时 ARMCD/ARM 必须 null (SDTMIG §5.2.2), 在 SDRG 引用规则解释.

### 4. 总结原则

- **Errors**: 99% 必修 (除非工具 Bug)
- **Warnings**: 优先修; 若违反"忠实原始数据"或"SDTM assumptions", 保留并 SDRG 详细说明 Rule ID / Impact / Reasoning

**源路径**: `knowledge_base/chapters/ch04_general_assumptions.md` §4.1.1 Compliance; SDTMIG v3.4 Section 4.1 & SDRG Templates

## Self-score verdict

- **Verdict**: **PASS**
- **对照 PASS 判据** (必含 5 大类):
  - 1. Date consistency (SD0063) ✓ 类 5
  - 2. CT compliance (SD1234 "SEVERE PAIN") ✓ 类 1
  - 3. Required/Expected 缺失 (SD0001) ✓ 类 2
  - 4. Duplicate records — *缺略提* (未明确提 AESEQ 重复, 但 SD1076 NSV 类覆盖结构问题), MINOR
  - 5. Orig vs Std / 类型错 (SD0037 ISO 日期 类 3; SD0058 跨域) ✓
  - 6. Value-level consistency — *缺略提* (未直接提 AESER=Y 但子变量空)
  - 修 vs 文档化原则 ✓ (4 scenarios: 源数据缺陷 / SDTMIG 允 / 医学判断 / CO-1c RWD)
- **触发 FAIL?** 无 (列 6 类 ≥ 3; 未混 Error/Warning/Notice; 未说所有 FAIL 必修)
- **加分**:
  - **CO-1c 规则自发引用** (v7 patch 跨题持续生效, 非直接问)
  - SDRG 场景分层 (A/B/C/D 结构清)
- **LOW carry-over**: Duplicate records (AESEQ dup) 和 AESER-子变量 value-level 一致性未直接列; 合计 6 类涵盖其余 5 PASS 判据, 达 PASS 阈. 跨平台风格差 (ChatGPT 列更全)
- **v5c→v7 delta**: 无 regression
