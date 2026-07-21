# NotebookLM — sanity_01 (R1 smoke v4.0)

> **题库版本**: v4.0 (见 `ai_platforms/SMOKE_V4.md §2`)
> **执行时间**: 2026-04-22 PM
> **执行者**: Bojiang + claude cowork MCP Chrome (main session auto-driven)
> **会话 URL**: https://notebooklm.google.com/notebook/3f87a93e-9a65-407e-8292-c28706fc6287
> **题类**: sanity preflight

---

## 题目原文

AESER Core 属性 (sanity preflight, 与 P3.8 相同).

## 发送给模型的 prompt (实际粘贴文本)

在 SDTMIG v3.4 下, AE 域变量 AESER (Serious Adverse Event) 的 Core 属性是什么 (Req / Exp / Perm)? 请简短给出值 + 引用 KB 具体源路径.

---

## 模型 raw 回答 (DOM readback 原文)

在 SDTMIG v3.4 下，AE 域变量 AESER (Serious Event) 的 Core 属性是 Exp (Expected)¹。

引用来源： [08_ev_adverse_ae.md]¹

**Citation 数**: 1 条 ([08_ev_adverse_ae.md])

---

## Self-score verdict

- **Verdict**: PASS
- **理由**:
  - 正确答 Core=Exp ✓
  - 引用正确源文件 ✓
  - 简短 + 有 citation ✓
- **触发 FAIL 判据?** 无
- **F-* carry-over 观察**: F-3 citation count=1 (单条, 合规)
