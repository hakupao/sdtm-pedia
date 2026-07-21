# Claude Projects — sanity_01 (R1 smoke v4.0)

> **题库版本**: v4.0 (见 `ai_platforms/SMOKE_V4.md §2`)
> **执行时间**: 2026-04-22 PM
> **执行者**: Bojiang + claude cowork MCP Chrome
> **会话 URL**: https://claude.ai/chat/ecf613ab-4028-4488-a55d-a1de5b206d61 (Project: SDTM Knowledge Base 019da929-2822-77c9-af9a-febc22c83255)
> **题类**: sanity preflight

---

## 题目原文

AESER Core 属性 (sanity preflight).

## 发送给模型的 prompt

在 SDTMIG v3.4 下, AE 域变量 AESER (Serious Adverse Event) 的 Core 属性是什么 (Req / Exp / Perm)? 请简短给出值 + 引用 KB 具体源路径.

---

## 模型 raw 回答 (DOM readback 原文)

AE.AESER Core = Exp (Expected)

| 字段 | 值 |
|---|---|
| Variable | AESER |
| Label | Serious Event |
| Type | Char |
| Role | Record Qualifier |
| Core | Exp |
| CT | C66742 (No Yes Response, Y/N) |
| Notes | Vals: "Y" and "N" |

源溯源: knowledge_base/domains/AE/spec.md (row #28, 见 05_mega_spec.md:44)

注: AE 域中 AETERM 才是 Req; AESER / AESEV / AEREL / AEOUT 等安全性评估字段均为 Exp — 临床试验通常必填, 但 SDTMIG 层面允许 null (如观察期外收集的非 SAE)。

**Citation 数**: 2 条文字源路径 (AE/spec.md + 05_mega_spec.md:44)

---

## Self-score verdict

- **Verdict**: PASS
- **理由**:
  - 正确答 Core=Exp ✓
  - 引用 2 个源路径 (AE/spec.md row#28 + 05_mega_spec.md:44) ✓
  - 补充 7 字段完整 metadata 表 + 额外 context (AETERM=Req 对比) — 超出要求
- **触发 FAIL 判据?** 无
- **PASS+ 加分?** 可给 (额外 metadata 准确 + 对比教学)
- **F-* carry-over 观察**: Claude v2.6 回答最详 (table + context + row/line #), 有助人审
