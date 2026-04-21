# Q10 — RELREC vs SUPP-- (AE/CM 跨记录关系建模) (v2.1)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e7432f-8b04-83ab-83c1-8c7be4153087
**Date**: 2026-04-21
**Thought for**: 3m 22s

## 原题

某 AE (头晕) 研究者判断 "可能与受试者正在服用的一种 CM (复方降压药) 有关". 这种跨域 (AE ↔ CM) 记录间关联, 应该用 SDTM 的 RELREC 还是 SUPPAE / SUPPCM 来表达? 分别说明 RELREC 与 SUPP-- 的设计分工.

## ChatGPT 答案 (完整)

**结论**: 这个 "AE 由某条 CM 引起/相关" 的关联, 应使用 **RELREC**, 不是用 SUPPAE / SUPPCM 来表达.

更准确地说:

- AE 放这次不良事件本身 (例如 AETERM=头晕, AEDECOD, AEREL / AERELNST 若研究有采集)
- CM 放那条合并用药本身 (例如 CMTRT, CMDECOD, CMINDC)
- **RELREC 放 "这条 AE 关联到这条 CM" 的记录间关系**
- SUPPAE / SUPPCM 只用于给某一条父记录补充非标准变量/补充属性, **不负责表达 AE 记录与 CM 记录之间的正式关联**

### 两者差异

| 工具 | 负责什么 | 不负责什么 |
|------|---------|-----------|
| **RELREC** | 记录 ↔ 记录 (同域或跨域) 的关系 | 不存"补充变量" |
| **SUPPAE / SUPPCM** | 某条 AE / CM 父记录自己的补充字段 (QNAM/QLABEL/QVAL) | 不建模独立的跨域关系 |

SDTMIG Chapter 8 明确把 RELREC 定义为用于描述受试者内、同域或跨域记录之间的关系; 而且举的典型例子就是 AE 与 CM 的关系. RELREC 通过 **STUDYID / RDOMAIN / USUBJID / IDVAR / IDVARVAL / RELID** 来把相关记录连起来; 如果是一组 CM, 也可以用 CMGRPID 之类的分组键提高表达效率. 相对地, SUPP-- 是用来存某条父记录的非标准变量值; 若数据其实代表"另一条独立观察/另一条记录", 就不应放进 SUPP--. 依据见 Section 8.2 / 8.4 与 Section 4.2.8.3.

### 为什么本场景应选 RELREC

你的场景 "AE 头晕" 与 "CM 复方降压药" 是两条分别存在的独立记录:
- 头晕作为 AE 独立存在
- 复方降压药作为 CM 独立存在
- "这两条记录之间有因果/相关性" → 这是**跨记录关系**, 不是对单条记录的补充限定

所以:
- "复方降压药的详细组成说明"、"investigator 额外因果说明文本" 这类内容, 可能放 SUPPCM 或 SUPPAE
- 但 **"AESEQ=5 这条头晕 与 CMSEQ=12 这条复方降压药有关"** 这个事实本身, 仍然应该放 RELREC

### 实操上怎么建

**若是一条 AE 对一条 CM**: RELREC 可按单记录关系建, 核心字段至少包括:
- STUDYID
- USUBJID
- RDOMAIN
- IDVAR
- IDVARVAL
- RELTYPE
- RELID

对单条记录, 通常可用:
- AE 侧: RDOMAIN=AE, IDVAR=AESEQ, IDVARVAL=<该 AESEQ>
- CM 侧: RDOMAIN=CM, IDVAR=CMSEQ, IDVARVAL=<该 CMSEQ>
- **两条记录共享同一个 RELID**

**若一个 AE 同时关联多条 CM**, 或一个组合用药由多条 CM 组成, 可考虑先在 CM.CMGRPID 分组, 再在 RELREC 中用 IDVAR=CMGRPID 关联, SDTMIG 也明确提到这是一种更高效的做法.

### 一个容易混淆的点

SUPPAE 里确实可以看到类似 AERELX、AEACNX 这种例子, 用来补充同一条 AE 记录针对另一种药物的次要因果性/处置值. 但那仍然是:
- AE 父记录的补充 qualifier
- **不是标准化的 AE ↔ CM 记录关系 表达**

而且标准文本还特别提醒: 这种关联必须在 metadata / aCRF 中清楚说明. 也正因为语义不如 RELREC 直观、可连接, 所以你的这个场景不应把 SUPPAE 当成主方案.

### 源溯源

- `knowledge_base/chapters/ch08_relationships.md`
- `knowledge_base/chapters/ch04_general_assumptions.md`
- `knowledge_base/domains/AE/assumptions.md` (AE 与非研究治疗链接到 CM/PR 并用 RELREC)
- `knowledge_base/domains/AE/spec.md` (AE 规格中 "CM linked via RELREC" 交叉引用)

## 判据对齐 (v2.1)

- ✅ **选 RELREC** (核心结论对) — 不是 SUPPAE / SUPPCM
- ✅ **分工清晰**: RELREC = 记录 ↔ 记录关系; SUPP-- = 单条父记录的补充变量
- ✅ **RELREC 核心字段 7 个命名齐全**: STUDYID / USUBJID / RDOMAIN / IDVAR / IDVARVAL / RELTYPE / RELID
- ✅ **AE 侧 + CM 侧**双向建模示例: IDVAR=AESEQ/CMSEQ, IDVARVAL=<value>, **共享 RELID** (v2.1 变量必显式命名 + 一对一配对, 完整)
- ✅ **加分**: CMGRPID 分组 → RELREC 多对一/多对多处理 (SDTMIG 8.2/8.4 高效做法, 示例级知识)
- ✅ **加分**: AEREL / AERELNST 提示 AE 自身标准字段存在 (避免把因果标志误放 SUPP)
- ✅ **加分**: SUPPAE 里 AERELX/AEACNX 边界说明 (SUPP-- 确可放次级补充因果, 但**不是跨记录关系主方案**) — 非常专业的边界辨析
- ✅ SDTMIG Chapter 8 / Section 8.2 / 8.4 / 4.2.8.3 原文引用
- ✅ 引 4 源 (ch08 + ch04 + AE/assumptions + AE/spec)

## Verdict: **PASS** (1/1)

## 归因

系统 prompt v2.1 + ch08_relationships + AE 知识命中: RELREC 使命 + SUPP-- 边界 + 跨域 vs 单记录分工 + 7 字段完整命名 + AESEQ/CMSEQ 双向对应 + RELID 共享 + CMGRPID 多对多加分 + SUPPAE AERELX/AEACNX 边界辨析 (超判据基线). 4 源溯源完整.
