# Sanity Q1 — AESER Core 属性

> 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e82d2d-bc74-83a7-9b7b-19cbb7bc5dde
> 提交时间: 2026-04-22
> 题: AESER 的 Core 属性是 Req 还是 Exp?
> 期望: Exp
> Verdict: **PASS**

## 完整回答

AESER 的 Core 属性是 Exp，不是 Req。

- AE.AESER = Serious Event
- Role: Record Qualifier
- Core: Exp
- CT: C66742【01_navigation.md 中 AE 变量索引】

补充一点：AE assumptions 也说明了，若 CRF 对各个 serious category（如 AESDTH, AESHOSP）逐项采集，那么 AESER 甚至可以是 derived（推导）出来的，这也和它是 Expected 而不是 Required 一致【05_domain_assumptions_all.md 中 AE assumptions】。

源溯源:
- `<!-- source: knowledge_base/domains/AE/spec.md -->`
- `<!-- source: knowledge_base/domains/AE/assumptions.md -->`

## 判据

- 答 Exp ✓
- 提供 C66742 ✓
- 引 spec + assumptions ✓
- 解释 derived 路径 ✓

PASS — 底座未回归
