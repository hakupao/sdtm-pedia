# Q9 — SUPPAE 边界 + QNAM/QLABEL/QVAL 典型例子

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6ef9a-07c4-83a7-b6ea-c6084bc9c48d
**Title**: SDTM Expert - SUPPAE 使用场景解析

## 原题

SUPPAE (Supplemental Qualifiers for AE) 的作用是什么? 什么情况下应该走 SUPPAE 而不是直接加 AE 域变量? 请举一个典型例子, 给出 QNAM / QLABEL / QVAL 三字段的完整示例 (场景自选, 无需 NCI Code).

## ChatGPT 答案

**结论先说**: SUPPAE 的作用是: 把某一条 AE 记录上的非标准变量值 (non-standard variable values) 单独存成 Supplemental Qualifiers 记录, 再通过 RDOMAIN=AE、IDVAR=AESEQ、IDVARVAL 等键挂回那条 AE 记录. SDTMIG 明确把主域 + SUPP-- 看成同一个逻辑域的两种物理承载方式, 而 QNAM 就是这个非标准变量的"变量名".

**什么时候走 SUPPAE, 而不是直接往 AE 加列** (4 类典型场景):

1. **如果数据项已经有标准 AE 变量可放, 先放 AE 本体** — SDTMIG 说明: 只要某个数据项能用标准里的 Permissible variable 表达, 就应该直接放进该 SDTM 域. AESEV、AESER、AEREL、AEACN、AESMIE 能进 AE 就进 AE.
2. **如果是"补充标准变量"的自由文本 / 说明字段, 走 SUPPAE** — 最典型就是 CRF 上的 "Other, specify". SDTMIG 给了 AE 的官方例子: AESMIE="Y" 时, 补充说明放到 SUPPAE.
3. **如果一个 AE qualifier 有多个值, 主表只放一个"主值"或放 "MULTIPLE", 其余值走 SUPPAE** — 每条记录的每个 qualifier 只能有 1 个值.
4. **如果是第二评价者/第二套判断, 走 SUPPAE** — Events/Interventions 没有 --EVAL; 若同一 AE 同时有研究者判断和 adjudication committee 判断, 次要判断放 SUPPAE, 并用 QEVAL 标明评价者.
5. **如果文本太长 (>200 字符), 溢出的部分走 SUPPAE**.

**什么时候不要走 SUPPAE**:
- AE topic 本身有多个事件词, 不要用 SUPPAE 硬挂说明; 应拆成多条 AE 记录. 例如 "Headache and nausea" 不应做成 1 条 AE + 1 条 SUPPAE.
- 已经有标准 AE 变量可承载时, 不要新造 sponsor-defined AE 列, 也不要把本该在 AE 的内容塞进 SUPPAE.

**典型例子**:

场景: CRF 先问是否属于 Other Medically Important Serious Adverse Event. 标准 AE 里只能表达这个类别存在: AESMIE = "Y"; 但具体"为什么 medically important"是自由文本, 不属于标准 AE 变量, 因此应放 SUPPAE.

**AE 主表**: AESMIE = "Y"

**SUPPAE 完整示例**:

| QNAM | QLABEL | QVAL |
|---|---|---|
| **AESOSP** | Other Medically Important SAE | HIGH RISK FOR ADDITIONAL THROMBOSIS |

三个字段含义:
- QNAM: 补充变量名, 8 字符规则适用, 作用类似 --TESTCD
- QLABEL: 补充变量的人类可读标签
- QVAL: 真正的补充值, 即这条非标准变量的内容

**一句话判断法**: 能落到标准 AE 变量, 就落 AE; 落不进去、但又是"附着在某条 AE 记录上的补充属性/补充说明", 就走 SUPPAE.

## PASS 判据自检

- [x] SUPPAE 存非标 AE 变量 ✓
- [x] 标准 AE 变量能放下的不走 SUPPAE ✓
- [x] 典型例子 QNAM/QLABEL/QVAL 三字段完整 ✓ (AESOSP / Other Medically Important SAE / HIGH RISK FOR ADDITIONAL THROMBOSIS)
- [x] QNAM 是短代号 (8 字符规则) ✓
- [x] QLABEL 是 label, QVAL 是实际值 ✓
- [x] 未误把 AE 标准变量当 SUPPAE 示例 (AESOSP 是非标变量) ✓
- [x] QNAM 未用 "AE" 前缀超 8 字符 (AESOSP 只 6 字符) ✓

## Verdict: **PASS**

核心判据全中 + 超额 4 大亮点:
1. 4 种 SUPPAE 使用场景系统分类 (Other specify / 多值 / 第二评价者 / 长文本)
2. 反例: Headache and nausea 应拆 AE 非 SUPPAE (Rule A 反知识)
3. 例子直接引用 SDTMIG 官方 (AESOSP/AESMIE=Y)
4. 一句话判断法收尾

是 10 题里**最完整**的一题. 答案结构、示例、反例、判断法都齐全.
