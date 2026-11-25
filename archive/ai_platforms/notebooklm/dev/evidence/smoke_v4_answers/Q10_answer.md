# Q10 — SUPPTS 前提纠错 (NotebookLM, smoke v4 R1, 2026-04-22 晚)

> Verdict: **PASS+** (premise correction caught + canonical TSVAL1-TSVALn given)

## Prompt (v4.0)
SDTM 的 SUPP-- (Supplemental Qualifiers) 家族里, 请回答:
(a) QNAM/QLABEL/QVAL/QORIG/QEVAL — QORIG/QEVAL 必填/不填时机 + 含义
(b) SUPPQUAL scope + TS 长文本 (>200) 处理 + "SUPPTS" 吗?
(c) SUPPAE → AE 父记录定位 (RDOMAIN + IDVAR + IDVARVAL), USUBJID 用法
(d) QVAL 长度上限 + 拆分

## Raw Answer (DOM 回读)

基于 SDTMIG v3.4 及相关规范，关于 SUPP-- (Supplemental Qualifiers) 的问题解答如下：

### (a) QORIG 和 QEVAL 的填写时机与含义

**QORIG (Origin):**
- 含义: 指示数据的来源（例如：CRF, Derived, Assigned）[27_rel_suppqual.md]。因为 QVAL 中可能混合了在 CRF 上收集的、算法派生的或指定的非标准变量数据，所以必须声明其来源 [27_rel_suppqual.md]。
- 填写时机: 它的 Core 值是 **Req（Required）**，这意味着它**始终必填**，在任何一条 SUPP-- 记录中都不能为 null [27_rel_suppqual.md]。

**QEVAL (Evaluator):**
- 含义: 评估者的角色，指示是谁给出了该数据的评估或解释（例如：ADJUDICATION COMMITTEE, SPONSOR, STATISTICIAN）[27_rel_suppqual.md]。
- 填写时机: 它的 Core 值是 **Exp（Expected）**。它**仅在结果是主观判断时必填**（即由特定人员或小组指定的值）。如果该记录包含的是客观收集或程序派生（objectively collected or derived）的数据，则 QEVAL **必须为空 (null)** [27_rel_suppqual.md]。

### (b) SUPPQUAL 的适用 Scope 及 TS 的长文本处理

**SUPPQUAL 适用数据集 Scope:** SUPPQUAL 机制设计用于为 **General Observation Classes (Events, Findings, Interventions)** 以及特定特殊用途域 **Demographics (DM)** 和 **Subject Visits (SV)** 捕获非标准变量 (NSVs) 并将其关联回父记录 [27_rel_suppqual.md]。

**不适用 SUPPQUAL 的 TS 域如何处理长文本 (>200 字符):**
- **不要使用 SUPPTS。** TS 域的数据不是受试者级别的数据，不适用 SUPP-- 机制 [25_td_meta_ti_ts_oi.md]。
- 当 TSVAL 的文本超过 200 字符上限时，必须**在 TS 域内部**进行字段拆分。
- 前 200 个字符保存在 **TSVAL** 中，后续文本每 200 个字符分割一次（并且必须在单词之间拆分/Split between words），存入同一条 TS 域记录的附加列 **TSVAL1**，**TSVAL2** 直至 **TSVALn** 中 [25_td_meta_ti_ts_oi.md], [29_ig_ch04_general_assumptions.md]。
- 同时，TSVAL1 到 TSVALn 的变量 Label 必须保持为 "Parameter Value" [29_ig_ch04_general_assumptions.md]。

### (c) SUPPAE 如何定位到具体的 AE 父记录

一条 SUPPAE 记录通过一组标准的复合键 **(STUDYID, RDOMAIN, USUBJID, IDVAR, IDVARVAL)** 来关联回其在 AE 域中的父记录 [27_rel_suppqual.md]：
- **USUBJID**: 填充与 AE 父记录中完全相同的 USUBJID（Unique Subject Identifier），用于将关系锚定到具体的单个受试者 [27_rel_suppqual.md]。
- **RDOMAIN**: 填充被关联父记录所在的域的两个字母缩写，这里必须填 **AE** [27_rel_suppqual.md]。
- **IDVAR (Identifying Variable)**: 填充用于在 AE 域中唯一标识那条父记录的变量名（名称本身）。通常是 **AESEQ**（或在按组关联时使用 AEGRPID）[27_rel_suppqual.md]。
- **IDVARVAL (Identifying Variable Value)**: 填充父记录中那个标识变量的实际值。比如如果 IDVAR 指定为 AESEQ，那么 IDVARVAL 就填入具体的序列号值（例如 "1" 或 "5"）[27_rel_suppqual.md]。
- 通过这 4 个字段的组合，加上 STUDYID，审查者就可以精准 Join/Merge 回 AE 数据集里那条唯一的记录 [27_rel_suppqual.md]。

### (d) QVAL 长度上限与拆分规则

- **长度上限**: QVAL 的最大长度受 SAS V5 传输文件格式的限制，**最大不得超过 200 字符** [29_ig_ch04_general_assumptions.md]。
- **超过 200 字符的拆分规则:**
  - 拆分方式: 文本应截断为每段最多 200 个字符，且必须**在单词之间拆分 (Split between words)**，以保证可读性 [29_ig_ch04_general_assumptions.md]。
  - QNAM 命名: 第一段文本使用原始不带数字后缀的补充变量名作为 QNAM；对于附加的后续文本，应在原 QNAM 名称后追加 1 位整数后缀（从 1 开始，如 1, 2, 3）。如果原始的 QNAM 已经达到了 8 个字符的最大限制，则**替换最后一个字符为数字**（例如 AEACNOT1、AEACNOT2）[29_ig_ch04_general_assumptions.md]。
  - QLABEL 的保留: 所有拆分出的后续记录，其 QLABEL（Qualifier Variable Label）必须与原始域变量的标签完全一致，绝不要在 Label 后面追加任何数字或后缀，因为它们在概念上依然是同一个变量 [29_ig_ch04_general_assumptions.md]。

## Verdict 打分

| 判据 | 结果 |
|---|---|
| (a) QORIG Req always / QEVAL Exp subjective | ✅ 完全对 |
| (b) SUPPQUAL scope = GOC + DM + SV | ✅ 原文 |
| (b) **不要使用 SUPPTS + TSVAL1-n 内部派生** | ✅✅ **premise correction caught** |
| (c) STUDYID + RDOMAIN=AE + USUBJID + IDVAR=AESEQ + IDVARVAL | ✅ 完整 5 键 (比判据多 STUDYID) |
| (d) 200 字符上限 + split between words + QNAM 后缀规则 + QLABEL 保持 | ✅ 超判据 |
| FAIL triggers | 无 |

**最终**: **PASS+ (1 分 + 0.25 bonus)**, 在 4 小题均答对基础上, 额外给出 QNAM 8 字符满时"替换末位字符"高级规则 + QLABEL 保留细节, citation 5+ 分布 ch04/ch08/ch27/25_ts.

## Citations
[27_rel_suppqual.md] × 多次 / [25_td_meta_ti_ts_oi.md] × 3 / [29_ig_ch04_general_assumptions.md] × 多次 — 3 source 交叉支撑, NBL 定位精准.
