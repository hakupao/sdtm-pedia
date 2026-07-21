# Q1 — CM 域拆记录 + Core=Req 变量 (v2.1)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e734e6-23f4-83a7-b7a4-1731b76f1ec0
**Date**: 2026-04-21
**Thought for**: 3m 13s

## 原题

受试者在同一天开始服用两种降压药 (氯沙坦 50 mg/日 + 氨氯地平 5 mg/日), 计划持续服用整个试验期, 目的是控制高血压. 请问在 SDTM CM 域里应该拆成几条记录? 每条记录至少要填哪些 Core=Req 变量? 简要说明字段含义 (不需要给具体 NCI Code).

## ChatGPT 答案 (完整)

我先核对 CM 域的规范和 assumptions，重点看"同一天开始的两种药物是否分两条"和"Core=Req 最少变量集合"。

我已经确认一条关键规则：Interventions/Event 的 topic 变量若一次报告多个值，提交时应拆成多条记录；CM 例子里也把组合治疗拆成多条药物记录，并可用 CMGRPID 关联。接下来我补齐 CM 域的 Req 变量清单和 ongoing 用法出处。

**Thought for 3m 13s**

**结论：拆成 2 条 CM 记录。**
一条记录表示 氯沙坦，另一条记录表示 氨氯地平。

原因是 CM 属于 Interventions 类，CM.CMTRT 是 Topic 变量；当一次报告里有多个用药时，SDTM 要求把多个 topic 值拆成多条记录，而不是塞进一条里。CM 的组合治疗示例也是"每个药一条"，必要时可用 CMGRPID 把同一联合方案的几条记录在同一受试者内分组。

来源：`<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`，`<!-- source: knowledge_base/domains/CM/examples.md -->`

### 每条记录至少要填哪些 Core=Req 变量

在 CM 域里，每条记录最少要有这 5 个 Core=Req 变量：

| 变量 | 角色 / Core | 含义 |
|------|-------------|------|
| STUDYID | Identifier / Req | 研究编号，标识是哪项试验 |
| DOMAIN | Identifier / Req | 域名，固定为 CM |
| USUBJID | Identifier / Req | 受试者唯一标识 |
| CMSEQ | Identifier / Req | 该受试者在 CM 域内的序号，用来保证记录唯一 |
| CMTRT | Topic / Req | 报告的药名/治疗名，即这条记录"说的是哪一个药" |

这也符合 SDTM 对 Req 的定义：用于识别记录的关键变量 + topic 变量，必须存在且不能为空。
来源：`<!-- source: knowledge_base/domains/CM/spec.md -->`，`<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`

### 你的例子可理解成什么样

至少会是：
- 记录 1：CMTRT = 氯沙坦
- 记录 2：CMTRT = 氨氯地平
- 两条记录的 STUDYID / DOMAIN / USUBJID 相同，CMSEQ 不同。

### 这几个信息虽然不是 Req，但实际通常会补

- **CMSTDTC**: 开始日期/时间 (同一天开始)
- **CMENDTC**: 结束日期/时间 (若一直吃到试验结束)
- **CMENRTPT / CMENTPT**: 若采集的是"到某个参考时间点仍在继续"，可用来表示 ongoing
- **CMINDC**: 用药适应症/原因；你这个例子里的"控制高血压"通常放这里
- **CMDOSE / CMDOSU / CMDOSFRQ**: 剂量、单位、给药频率 (50 mg/日、5 mg/日)
- **CMDECOD**: 标准化药名/通用名 (非 Req 但 assumptions 建议)

### 实务提醒

若想明确告诉审评者"两药联合降压方案"，可以给两条记录加同一个 CMGRPID。但 CMGRPID 是 Perm，非必填。

### 源溯源

- `<!-- source: knowledge_base/domains/CM/spec.md -->`
- `<!-- source: knowledge_base/chapters/ch04_general_assumptions.md -->`
- `<!-- source: knowledge_base/domains/CM/examples.md -->`

## 判据对齐 (v2.1)

- ✅ 两条 CM 记录 (拆分, 不合并)
- ✅ STUDYID / DOMAIN / USUBJID / CMTRT 4 个 Req 全列
- ✅ CMSEQ / CMSTDTC / CMINDC 三者都提到
- ✅ CMINDC 指征 = 高血压
- ✅ 未误列 CMCAT/CMSCAT 为 Req
- ✅ 未臆造变量
- ✅ 源溯源齐全 (CM/spec.md + CM/examples.md + ch04)

## Verdict: **PASS** (1/1)

## 归因

系统提示 v2.1 + CM knowledge base 命中, 核心结论正确 + 变量清单精确 + 源溯源完备.
