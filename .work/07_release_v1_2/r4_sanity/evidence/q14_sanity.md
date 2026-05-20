# R4 Sanity Q14 — AE+CE+MH+DS 跨域 (Gemini v8.1 LIVE, 3.1 Flash-Lite)

**Date**: 2026-05-20 morning
**Platform**: Gemini Gem v8.1 LIVE (SDTM Knowledge Base Gem)
**Model**: **Gemini 3.1 Flash-Lite** ⚠️ (Pro/Flash quota 用光; 用户决定用 Flash-Lite 跑)
**Conversation URL**: https://gemini.google.com/u/1/gem/3b572e310813/dd7bfa02bd8e790c
**Question source**: `ai_platforms/SMOKE_V4.md:841-866`

---

## 题目

> 受试者 Visit 5 突发心梗 (STEMI) 住院, 治疗 3 天出院, 在 Visit 7 因心衰死亡. 请回答: (a) 这一系列事件里, **心梗本身**可以同时记在哪些域 (AE / CE / MH)? 各自的业务边界什么? (b) "死亡" 这个 terminal event 同时应该记 AE 和 DS 还是只一个? (c) DS 域的 **DSDECOD** vs **DSCAT** 在"死亡"场景下值各是什么? (d) 死亡时间的 ISO 8601 怎么跨域对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)?

---

## Gemini v8.1 + Flash-Lite 答案

⚠️ **Flash-Lite 引入无关 framing**: "此问题涉及临床研究中受试者病史 (MH) 与合并用药 (CM) 的 SDTM 映射规则" — CM 在本场景完全不相关, 是 Flash-Lite hallucinated intro. 但后续答案没 follow-through CM, 不影响核心 verdict.

**(a) 心梗 (STEMI) 域映射**:
- **MH**: 如果心梗是入组前既往史 → MHTERM="ST Elevation Myocardial Infarction", MHSTDTC=发生日期, MHENRF="BEFORE"
- **AE**: 如果 Visit 5 突发 → AETERM, **AESER="Y"** (住院 Serious), **AESHOSP="Y"**, AEACN
- **CE**: 通常记方案定义的非 AE 事件; 除非方案规定心梗不计 AE, 否则不首选 CE
- **业务边界**: MH vs AE 以时间点区分 (入组前 MH / 入组后 AE); AE vs CE 默认心梗 AE

**(b) 死亡 AE 与 DS**:
同时记录, 职责不同:
- AE: **AEOUT="FATAL"**, **AESDTH="Y"**
- DS: DSTERM="DEATH", **DSDECOD="DEATH"**, **DSCAT="DISPOSITION EVENT"**
- 原则: AE 侧重临床安全性, DS 侧重生命周期状态变动

**(c) DS 死亡场景取值**:
- **DSCAT** = "DISPOSITION EVENT" (依据 DS assumptions §2.b)
- **DSDECOD** = "DEATH", 属于 **C66727** (Completion/Reason for Non-Completion) codelist

**(d) ISO 8601 对齐**:
- AE.AESTDTC: 死亡事件发生日期/时间
- DS.DSSTDTC: 死亡日期/时间
- DM.DTHDTC: 死亡日期
- **对齐要求**: 三域死亡日期部分必须完全一致, 不得存在冲突; 若数据库精度为分钟, 三域均应体现到分钟 (如 2026-05-20T11:40)

**额外合规**: AE 与 DS 应通过 **RELREC** 建立关联 (同一 RELID 绑定)

**来源**: AE/DS/DM spec.md + ch04_general_assumptions.md §4.4 (ISO 8601)

---

## Strict 判据 evaluation

| 项 | 判据 | v8.1 答案 | 命中 |
|---|---|---|:---:|
| 1 | (a) MH = study start 之前 | ✅ "入组前为 MH", MHENRF="BEFORE" | ✓ |
| 2 | (a) AE = study start 之后 + reportable AE 阈值 (SAE) | ✅ AESER=Y + AESHOSP=Y | ✓ |
| 3 | (a) CE = study start 之后未达 AE 阈值 | ⚠️ 答案"除非方案规定不计 AE 否则不首选 CE" — 措辞偏离判据但概念正确 | ✓ (concept) |
| 4 | (a) 同一事件同一时间点单域 (本题 AE) | ✅ 隐含 (按时间点二选一) | ✓ |
| 5 | (b) 死亡必记 DS + AE.AESDTH=Y | ✅ "同时记录 AE 和 DS, 职责不同", AESDTH=Y + AEOUT=FATAL | ✓ |
| 6 | (c) DSDECOD="DEATH" | ✅ DSDECOD="DEATH" + 引用 C66727 | ✓ |
| 7 | (c) DSCAT="DISPOSITION EVENT" sponsor 约定 | ✅ DSCAT="DISPOSITION EVENT" + 引用 DS assumptions §2.b | ✓ |
| 8 | (d) AE/DS/DM 三域日级对齐 | ✅ "死亡日期部分必须完全一致" | ✓ |
| 9 | FAIL: 同一事件同一时点 AE+CE+MH 三都记? | ✅ 无, 按时间点分域 | ✓ |
| 10 | FAIL: 死亡只记 AE 不记 DS? | ✅ 无, 强调同时 | ✓ |
| 11 | FAIL: DSDECOD 自定义 term? | ✅ 无, 标准 "DEATH" + CT C66727 | ✓ |
| 12 | FAIL: 三域日期不同? | ✅ 无, 要求一致 | ✓ |
| 13 | FAIL: 三域 time-level 严格相等过严? | ⚠️ 答案条件性 "若精度为分钟则到分钟", 没主动允许 offset, 略偏严 | ✓ (边界, 非硬错) |

**13/13 命中, 0 硬 FAIL**

---

## Flash-Lite Caveat List (3 项 LOW/INFO)

1. ⚠️ 开头无关引入 "CM 合并用药" framing — Flash-Lite hallucinated intro, 但没 follow-through, 不影响核心答案. (LOW)
2. ⚠️ (d) 没主动允许 AE.AEENDTC vs DTHDTC 的 time-level offset (业界允小时级 offset) — 略偏严. (LOW)
3. ℹ️ CE 边界描述与判据 wording 不同 (但概念正确). (INFO)

---

## Conclusion

**Verdict: PASS** (Strict 判据 13/13, 0 硬 FAIL; 3 个 Flash-Lite caveat 全 LOW/INFO 不影响通过)

**Regression status (with model caveat)**:
- R3 v7.1 + Pro baseline 是 PASS
- R4 v8.1 + Flash-Lite 也 PASS
- 不直接可比 (model 不同), 但 v8.1 + Flash-Lite 已 PASS 表明 v8.1 prompt 在低能模型上仍 KB grounded + 跨域逻辑清晰

**v8.1 表现亮点**:
- 主动 **RELREC** 关联 AE-DS (合规深度, 超判据要求)
- KB citation 文件级精确 (AE/DS/DM/ch04)
- AESDTH=Y + AEOUT="FATAL" 双 AE 死亡标识完整
- MHENRF 主动给 MH timing 修饰变量

**Flash-Lite 弱项**:
- 不带 default reflection (vs Pro Q1 PASS+ 的 5 个 anti-hallucination cases)
- 偶有无关 framing 引入 (CM)
- 略简化判据细节 (CE 措辞, time-level offset)
