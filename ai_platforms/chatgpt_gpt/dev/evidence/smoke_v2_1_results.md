# ChatGPT GPTs Smoke v2.1 Regression — Results Summary

**Platform**: ChatGPT Custom GPT "SDTM Expert"
**GPT ID**: g-69e635b99e848191a2818cd8e8e7e9cc
**Base URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert
**System prompt version**: v2.1 (7568 bytes, 2 批投喂完整)
**Smoke spec**: `ai_platforms/SMOKE_QUESTIONS_V2.md`
**Executor**: main session via Claude-in-Chrome MCP
**Date**: 2026-04-21
**Mode**: 每题独立 new conversation (避免 cross-contamination)

## Final Score

| 指标 | 结果 |
|------|------|
| **Strict PASS** | **10 / 10** |
| Q3 (LBNRIND = HIGH 回归) | ✅ PASS |
| Q7 (CMINDC 必显式命名回归) | ✅ PASS |
| 平均 "Thought for" | ~2m 15s (1m 28s - 3m 22s) |

## 逐题结果

| # | 题目关键词 | Thought | 核心判据命中 | Verdict |
|---|-----------|---------|-------------|---------|
| Q1 | AE SAE 最小强制变量 | ~2m | AESER=Y + AESHOSP / AESCONG / AELIFE / AEDTH / AESDISAB / AESMIE + AEACN + AESTDTC + AETERM (Exp 标) | ✅ PASS |
| Q2 | AE CTCAE Grade 3 AETOXGR | ~2m | AETOXGR = "3" 字符型 + AESEV 映射 "SEVERE" (severity ≠ seriousness 边界) | ✅ PASS |
| Q3 | LB 高血糖 LBNRIND | ~2m | **LBNRIND = HIGH** (v2.1 L62 bullet 回归命中) + LBORNRLO/LBORNRHI + LBORRES 超限判定 | ✅ **PASS** 🎯 |
| Q4 | AE 死亡 AEOUT/AESDTH | ~1m 50s | AEOUT = "FATAL" + AESDTH = "Y" + DM.DTHDTC + DM.DTHFL = "Y" + DS 死亡记录 | ✅ PASS |
| Q5 | PC BLQ LLOQ 填法 | ~1m 35s | PCORRES = BLQ / PCSTRESC = BLQ / **PCSTRESN = null (不填 0)** / PCLLOQ = 0.10 + ADaM 分层 | ✅ PASS |
| Q6 | DM ARMCD/ARM + 换组 SE/TA | ~1m 28s | ARMCD 短代号 + ARM human-readable + ACTARMCD/ACTARM + **ARMNRS="UNPLANNED TREATMENT"** + **SE ETCD="UNPLAN"+SEUPDES** | ✅ PASS |
| Q7 | MH + CM 双域 + **CMINDC 必名** | ~2m 45s | **两域都进** + MHTERM/MHDECOD + CMTRT/CMDECOD + **CMINDC = 高血压 (显式命名 2 次)** + MHENRTPT/CMENRTPT = "ONGOING" 加分 | ✅ **PASS** 🎯 |
| Q8 | AE ISO 8601 + AESTDTC/AESTDY | ~2m 13s | AESTDTC = "YYYY-MM-DDT14:00" 分钟精度 + EDC-日精度不补 T00:00 + AESTDY 公式两分支 + **Day 1 起始 (无 Day 0)** + 三示例 | ✅ PASS |
| Q9 | SUPPAE 边界 + QNAM/QLABEL/QVAL | ~3m 4s | SUPPAE = NSV 补充 + **QNAM=AESMDESC / QLABEL=Other MIE Description / QVAL=HIGH RISK OF AIRWAY OBSTRUCTION** + IDVAR=AESEQ 连接 + 3 步决策树 | ✅ PASS |
| Q10 | RELREC vs SUPP-- (AE↔CM) | ~3m 22s | **选 RELREC** + 7 字段齐 (STUDYID/USUBJID/RDOMAIN/IDVAR/IDVARVAL/RELTYPE/RELID) + **AESEQ/CMSEQ 双向配对+共享 RELID** + CMGRPID 多对多 | ✅ PASS |

## 关键回归验证 (v2.1 强化 bullets)

### 1. Q3 LBNRIND = HIGH 回归

- **v2.0 表现**: 给了 LBORNRLO/LBORNRHI + 超限判定, 但未点 LBNRIND 字段名
- **v2.1 表现**: 直接命名 **LBNRIND = "HIGH"** (CT code 值) + LBORNRLO/LBORNRHI 对比同时列出
- **判据**: ✅ 显式命名 + 与 CT/LBTESTCD/GLU 联动理解
- **归因**: v2.1 system_prompt L62 "变量必显式命名" bullet 起效

### 2. Q7 CMINDC 必显式命名回归

- **v2.0 表现**: 说 "CM 记录用药原因", 但未点 CMINDC 具体字段名
- **v2.1 表现**: **CMINDC = 高血压** 在表格主行立即显式, 并在详细解释中再次"CMINDC = 高血压; CM 示例里就有 CMINDC 记录适应症/用药指征的用法" (显式 2 次)
- **判据**: ✅ 显式命名 + 给值 + 引 examples.md 类比
- **归因**: v2.1 system_prompt L62 bullet + CM/examples.md 2 批上传完整命中

## 加分项汇总 (超判据基线)

| 加分维度 | Q# | 具体内容 |
|---------|---|---------|
| CDISC CT code 准确值 | Q2, Q3, Q4 | AETOXGR="3", LBNRIND="HIGH", AEOUT="FATAL" |
| SDTM 示例级知识 | Q6, Q9 | ETCD="UNPLAN"+SEUPDES, ARMNRS="UNPLANNED TREATMENT"+ACTARMUD, MHENRTPT/CMENRTPT="ONGOING" |
| ADaM 分层边界 | Q5 | BLQ 不写 0; 插补归 ADaM 层, SDTM 只忠实保留原始 |
| 多对多关系表达 | Q10 | CMGRPID 分组提效 (SDTMIG 8.2/8.4 原文) |
| 分类模型层分工 | Q7 | MH=Events / CM=Interventions + --TERM vs --TRT 主题变量对比 |
| 坦诚边界 (Rule D) | Q5 | 指出 PC assumptions 原文没单独"BLQ 不写 0"句, 依据是 Findings 通则 + PC 示例合推 |

## 源溯源质量 (平均每题)

- **3-6 源**, 命名均为 `knowledge_base/...` 路径形式
- 覆盖层次: chapters (模型级) + domains/spec (字段定义级) + domains/assumptions (规则级) + domains/examples (示例级)
- 对齐 "3 条源至少有 1 条 not-chapters" 的 v2.1 要求

## 归因 & 结论

**v2.1 10/10 strict PASS, 两关键回归 (Q3 LBNRIND / Q7 CMINDC) 均命中**. 系统 prompt v2.1 "变量必显式命名" bullet + 2 批知识文件 (spec / assumptions / examples / chapters / terminology) 全栈投喂到位, 应答质量达到了 Claude Projects v2.6 相当水平 (参照 `ai_platforms/claude_projects/dev/ab_reports/STAGE_V2.6_AB_REPORT.md` 24/24 PASS 基线).

ChatGPT GPT "SDTM Expert" **已具备发布 (GPT Store 或个人链接分享) 的最低质量门槛**.

## 下一步建议

1. **可选**: 上 20 题硬 benchmark (参照 Claude v2.6 扩展题池) 作为 stress test 补充
2. **可选**: A/B 对比 Gemini Gems 同题结果 (待 Gemini 部署完成后)
3. **发布**: 按 `ai_platforms/chatgpt_gpt/README.md` 路径进入 Phase 5 (审查 + 发布)

## Evidence 文件清单

```
ai_platforms/chatgpt_gpt/dev/evidence/smoke_v2_1_answers/
├── Q1_answer.md   (AE SAE 最小强制变量)
├── Q2_answer.md   (AETOXGR CTCAE)
├── Q3_answer.md   (LBNRIND = HIGH) 🎯 v2.1 回归
├── Q4_answer.md   (AE 死亡 AEOUT/AESDTH)
├── Q5_answer.md   (PC BLQ LLOQ)
├── Q6_answer.md   (DM ARMCD/ARM + SE/TA)
├── Q7_answer.md   (MH+CM 双域 + CMINDC 必名) 🎯 v2.1 回归
├── Q8_answer.md   (ISO 8601 + AESTDY)
├── Q9_answer.md   (SUPPAE QNAM/QLABEL/QVAL)
└── Q10_answer.md  (RELREC vs SUPP-- AE↔CM)
```

每题独立 conversation URL 保存在各自 Q{N}_answer.md 头部, 可复现.
