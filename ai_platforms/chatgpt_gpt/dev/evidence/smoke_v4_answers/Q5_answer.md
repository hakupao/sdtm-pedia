# ChatGPT GPTs — Q5 FA vs QS vs CE 边界 (V5C post-apply v2.2 LIVE)

> **执行时间**: 2026-04-24 (V5C regression)
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69ead46d-6800-83a8-b309-6b67ba120c40
> **题类**: Q5 (B2 — FA/QS/CE 三场景选域)

## Raw (DOM readback)

**结论: A → FA; B → QS; C → CE.**

| 场景 | 域 | 理由 | Topic 变量值示例 |
|---|---|---|---|
| A (DAS28 对 MH) | **FA** | 对一条既往 MH 事件的量化 finding, 不是新 AE, 不是问卷. FA 存"关于某事件/干预的 findings", 若 FA 与 MH 关系已收集, 应通过 **RELREC** 关联, 不只靠 FAOBJ | FATESTCD=DAS28; FATEST="DAS28 Score"; FAOBJ="RHEUMATOID ARTHRITIS"; FAORRES=4.2 |
| B (SF-36) | **QS** | SF-36 是 QRS instrument. QS 结构: "受试者 × 访视 × 问卷 × 题目/评分" 一条记录. instrument 名放 --CAT, 题目/评分放 --TESTCD/--TEST | QSCAT="SF36 V2.0 STANDARD"; 8 维度 QSTESTCD=SF36312 Physical Functioning / SF36313 Role Physical / SF36314 Bodily Pain / SF36315 General Health / SF36316 Vitality / SF36317 Social Functioning / SF36318 Role Emotional / SF36319 Mental Health |
| C (轻微头晕 sub-AE) | **CE** | 方案/EDC 明确不作为 AE, 但仍收 clinical event of interest. CE 用于 protocol-defined, not considered AE. CE assumption 提醒 write-in CE 谨慎, 确保真 AE 进 AE | CETERM=DIZZINESS; CEDECOD=Dizziness; CEDUR=PT30S (ISO duration, 30 秒) |

**关键判定**: A = "关于既有事件的 finding" → FA; B = "问卷工具" → QS; C = "非 AE 的临床事件本身" → CE

**源路径**: FA/spec.md + assumptions.md; QS/spec.md + assumptions.md; terminology/questionnaires/questionnaires_part39.md (SF-36 v2.0 STANDARD QSTESTCD); CE/spec.md + assumptions.md

## Self-score verdict

- **Verdict**: **PASS**
- **对照 PASS 判据**:
  - A=FA ✓ (未答 QS / SUPPMH)
  - B=QS ✓
  - C=CE ✓ (未答 AE / DV)
- **触发 FAIL?** 无
- **加分**:
  - A 提 RELREC 作 FA-MH 关系更精确连接 (超 PASS 要求)
  - B 提供精确 SF36312-319 8 维度 QSTESTCD (N5.2 baseline 持平或更厚)
  - C 提 CEDUR=PT30S ISO duration 精确 timing (超要求)
- **v5c→v2.2 delta**: 无 regression, 深度保持或略强于 N5.2 baseline
