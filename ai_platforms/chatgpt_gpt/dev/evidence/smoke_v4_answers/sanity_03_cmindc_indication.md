# ChatGPT GPTs — sanity_03 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM
> **执行者**: Bojiang + claude cowork MCP Chrome
> **会话 URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8a045-163c-83ab-9e9b-67af11039862
> **题类**: sanity preflight

## 发送 prompt

CMINDC (Concomitant Medication Indication) 这个变量在 SDTMIG v3.4 的 CM 域下用于什么业务场景? 请简短说明 + 引用 KB 源.

## Raw 回答

CMINDC 在 CM 域里用于表示**并用药的适应症/用途**，也就是"这次 concomitant medication 是拿来治疗什么的"。

在 SDTMIG v3.4 里，KB 具体给的业务场景是: CRF 用预设选项收集 analgesic 的 indication，并带 "Other, specify"; 此时 CMINDC 用来存该 indication，而 "Other" 的补充文本可按申办方规则放到 SUPPCM (如 QNAM=CMINDOTH)，或编码后直接写入 CMINDC。

KB 源路径:
- knowledge_base/chapters/ch04_general_assumptions.md (§4.2.7.1 中的 CMINDC 示例)
- 对应合并文件: 02_chapters_all.md

**Citation 数**: 2 文字源路径 (ch04 §4.2.7.1 + 合并 02_chapters_all.md)

## Verdict: **PASS**

- 业务场景清晰 ✓
- 具体 CRF "Other, specify" + SUPPCM QNAM=CMINDOTH 示例 ✓ (精确 SUPP-- 机制)
- ch04 §4.2.7.1 精确章节引用 ✓
- 合并文件溯源对照 ✓
- **无 FAIL**
