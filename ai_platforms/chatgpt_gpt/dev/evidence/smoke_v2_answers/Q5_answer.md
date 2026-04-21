# Q5 — PK LLOQ 以下值的记录

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef3a-50dc-83a9-82cb-04556d699bd6
**Title**: SDTM Expert - PK研究 LLOQ 填写指南

## 原题

药代动力学 (PK) 研究中, 采样点的血药浓度检测值低于实验室定量下限 (LLOQ). 按 SDTMIG v3.4 PC 域 assumptions, 应该如何填写 PCORRES (原始结果) / PCSTRESN (标准数值) / PCSTRESC (标准字符) / PCLLOQ (定量下限)? 为什么不能直接写 0?

## ChatGPT 答案

**结论：**

| 变量 | 建议填写 |
|---|---|
| PCORRES | 保留原始采集结果，例如 BLQ / BQL / <0.050（按原始采集方式） |
| PCSTRESC | 填标准化后的字符结果；如果原始结果就是 BLQ，通常可仍为 BLQ；如果原始结果是不等式，如 <0.050 ng/mL，标准单位换算后应仍保留 < 号，例如 <0.05 ug/L |
| PCSTRESN | **留空（null）** |
| PCLLOQ | 填该条记录对应分析方法的 LLOQ 数值 |

**为什么不能直接写 0：** 0 表示"实测结果等于零"，而 <LLOQ / BLQ 表示"低于方法可定量范围，真实值未知，只知道小于某个阈值"。这两个含义完全不同。

SDTM Findings 通则要求：--ORRES 保存原始结果；只要 --ORRES 有值，--STRESC 也必须有值；只有当 --STRESC 是真正数值时，才转到 --STRESN。若结果是字符结果（如 BLQ）或不等式（如 <0.1），--STRESN 应为空。SDTMIG 的示例明确给了两类模式：
- 收集到 BLQ 时，复制到 --STRESC，--STRESN 为空
- 收集到不等式时，< 号在 --STRESC 中保留，--STRESN 为空

SDTM 对缺失/不可得值的约定是用 null，不是用人为替代值；把 <LLOQ 强行写成 0 会丢失"左删失（left-censored）"信息，也会误导后续审评和分析。

**落地例：**
- 原始：<0.050 ng/mL → PCORRES = <0.050 / PCSTRESC = <0.050 / PCSTRESN = null / PCLLOQ = 0.050
- 原始：BLQ（LLOQ = 0.050）→ PCORRES = BLQ / PCSTRESC = BLQ / PCSTRESN = null / PCLLOQ = 0.050

坦诚说明：我这次检索里没有命中一条单独写明"PC 域 LLOQ 必须如何填"的 PC 域级原文句子，但命中了 SDTMIG v3.4 的 Findings 通则和 BLQ / 不等式示例。PC 是 Findings 类域, 规则同样适用。

## PASS 判据自检

- [x] PCORRES = "<LLOQ" 或 BLQ 字符 (带 "<" 符号) ✓ (给两种形式)
- [x] PCSTRESC 字符保留 ✓
- [x] PCSTRESN = NULL / 空 ✓
- [x] PCLLOQ = LLOQ 数值 (0.050) ✓
- [x] 解释不能写 0 的原因 ✓ (左删失/left-censored 概念精确)

## Verdict: **PASS**

全中 + 额外亮点: (1) 明确"left-censored"统计概念; (2) 具体单位换算示例 (0.050 ng/mL → 0.05 ug/L); (3) 坦诚未命中 PC 域级原文, 引用 Findings 通则 — Rule A 认识论谦虚典范.
