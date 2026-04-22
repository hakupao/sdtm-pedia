# Gemini Gems — sanity_01 (R1 smoke v4.0)

> **题库版本**: v4.0 (见 `ai_platforms/SMOKE_V4.md §2`)
> **执行时间**: 2026-04-22 PM
> **执行者**: Bojiang + claude cowork MCP Chrome (main session full-auto via Quill)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/abff4ea883a6d4b5
> **题类**: sanity preflight

---

## 题目原文

AESER Core 属性 (sanity preflight).

## 发送给模型的 prompt

在 SDTMIG v3.4 下, AE 域变量 AESER (Serious Adverse Event) 的 Core 属性是什么 (Req / Exp / Perm)? 请简短给出值 + 引用 KB 具体源路径.

---

## 模型 raw 回答 (DOM readback 原文)

在 SDTMIG v3.4 下，AE 域变量 AESER（Serious Event）的 Core 属性是 Exp（Expected）。

KB 具体源路径：knowledge_base/domains/AE/spec.md。

**Citation 数**: 0 条 inline citation (但给出了源路径文字引用)

---

## Self-score verdict

- **Verdict**: PASS
- **理由**:
  - 正确答 Core=Exp ✓
  - 指向正确源路径 AE/spec.md ✓
  - 简短 ✓
- **触发 FAIL 判据?** 无
- **F-* carry-over 观察**: Gemini 无 inline citation 机制 (不支持), 靠文字引用源路径 — 符合 v5 system prompt 风格
