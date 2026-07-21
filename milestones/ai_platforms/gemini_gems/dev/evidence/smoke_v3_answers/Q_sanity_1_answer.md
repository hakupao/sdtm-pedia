# Q_sanity_1 — Gemini SDTM Expert 回答

> 题: AESER 的 Core 属性是 Req 还是 Exp?
> 期望: Exp
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/fc02e9cd1e0e188f
> 时间: 2026-04-22
> 账号: bojiang.zhang.0904@gmail.com (Pro)
> Mode: Pro

## 完整回答

在 SDTM AE 域中，AESER 的 Core 属性如下：

结论：AE.AESER 的 Core 属性是 Exp (Expected)。

依据：
根据 SDTMIG v3.4 的 AE 域规范，AE 域的 Core 属性分布并不规则，不能简单类推。AESER (Serious Event) 被定义为 Expected，这意味着如果数据集中存在该信息，则必须包含该变量；如果不存在，则该变量可以为 null，但变量本身必须出现在数据集中。

AE 域 Core 属性分布概览：

Req (6个): STUDYID, DOMAIN, USUBJID, AESEQ, AETERM, AEDECOD

Exp (约10个): 包含 AESER, AEREL, AEACN, AELLT, AEPTCD 等

Perm (其余): 包含 AESEV, AESHOSP, AESLIFE, AESDTH, AEOUT 等

源路径：knowledge_base/domains/AE/spec.md
段落：§AESER

## Verdict

**PASS** — 回答 "Exp (Expected)" 完全命中期望; 额外给出 Req 6 个变量准确枚举 + Exp/Perm 分布概览 + knowledge_base spec.md 源引用; Core 层次底座未回归.
