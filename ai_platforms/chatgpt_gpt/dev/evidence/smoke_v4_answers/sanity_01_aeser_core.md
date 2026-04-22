# ChatGPT GPTs — sanity_01 (R1 smoke v4.0)

> **题库版本**: v4.0 (见 `ai_platforms/SMOKE_V4.md §2`)
> **执行时间**: 2026-04-22 PM
> **执行者**: Bojiang + claude cowork MCP Chrome
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8a045-163c-83ab-9e9b-67af11039862
> **题类**: sanity preflight

---

## 题目原文

AESER Core 属性 (sanity preflight).

## 发送给模型的 prompt

在 SDTMIG v3.4 下, AE 域变量 AESER (Serious Adverse Event) 的 Core 属性是什么 (Req / Exp / Perm)? 请简短给出值 + 引用 KB 具体源路径.

---

## 模型 raw 回答 (DOM readback 原文)

AESER 的 Core = Exp。

KB 具体源路径：knowledge_base/domains/AE/spec.md（合并文件 04_domain_specs_all.md 的 AE 规格段中，AESER 条目明确写的是 Core: Exp）

**Citation 数**: 0 条 inline (文字源路径引用 2 处: 规范路径 + 合并文件)

---

## Self-score verdict

- **Verdict**: PASS
- **理由**:
  - 正确答 Core=Exp ✓
  - 指向正确源路径 AE/spec.md + 合并文件 04_domain_specs_all.md ✓
  - 简短 ✓
- **触发 FAIL 判据?** 无
- **F-* carry-over 观察**: 无
