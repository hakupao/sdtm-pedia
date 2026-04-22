# Q_sanity_3 — Gemini SDTM Expert 回答

> 题: ACTARMCD 在哪个域? Core 属性?
> 期望: DM 域 Order=26 Core=Exp; 若答 ADaM/EX 错层, 说明 §1.6 硬锚点失效
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/566fc0d916b4f97f
> 时间: 2026-04-22
> 账号: bojiang.zhang.0904@gmail.com (Pro)
> Mode: Pro

## 完整回答

结论：
ACTARMCD 位于 DM (Demographics) 域，其 Core 属性为 Exp (Expected)。

依据：
在 SDTMIG v3.4 的 DM 域规范中，关于治疗臂（Arm）的变量区分如下：

ARMCD 和 ARM：属于计划的治疗臂（Planned Arm），其 Core 属性为 Req。

ACTARMCD 和 ACTARM：属于受试者实际接受的治疗臂（Actual Arm），其 Core 属性为 Exp。

虽然受试者在研究中必然会有实际治疗分配，但在 SDTM 标准定义中，这两个实际组变量被归类为 Expected 而非 Required。此外，这两个变量属于 protocol-specific 文本，无 CDISC CT codelist 约束。

源路径：
knowledge_base/domains/DM/spec.md §ACTARMCD
knowledge_base/chapters/ch04_general_assumptions.md (见 CO-1b 修正说明)

## Verdict

**PASS** — DM 域 + Core=Exp 完全命中期望; 额外正确区分 Planned (ARMCD/ARM, Req) vs Actual (ACTARMCD/ACTARM, Exp) 4 变量; protocol-specific 无 CT codelist 约束陈述准确; §1.6 DM 域硬锚点未回归.
(注: Order=26 未显式列出, 但问题只问"哪个域"+"Core 属性", 两项均对.)
