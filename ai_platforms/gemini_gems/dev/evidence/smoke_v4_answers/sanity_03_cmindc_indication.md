# Gemini Gems — sanity_03 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM
> **执行者**: Bojiang + claude cowork MCP Chrome (Quill editor)
> **会话 URL**: https://gemini.google.com/u/1/gem/3b572e310813/abff4ea883a6d4b5
> **题类**: sanity preflight

## 发送 prompt

CMINDC (Concomitant Medication Indication) 这个变量在 SDTMIG v3.4 的 CM 域下用于什么业务场景? 请简短说明 + 引用 KB 源.

## Raw 回答 (最终答复, 不含推理过程)

在 SDTMIG v3.4 中，关于 CMINDC 的使用场景如下:

**业务场景**: CMINDC 用于记录受试者使用该合并用药的医学适应症或具体用药原因 (例如: 因"头痛"服用对乙酰氨基酚，或因"高血压"服用降压药)。

(注: 在跨域业务场景中，如果该用药原因在研究中同时也作为不良事件 (AE) 或既往病史 (MH) 被收集，CMINDC 域会直接记录适应症的文本描述; 如果需要建立精确的数据追溯关系，通常会额外使用 RELREC 域将该 CM 记录与具体的 AE 或 MH 记录进行关联。)

KB 具体源路径: knowledge_base/domains/CM/spec.md

**Citation 数**: 0 inline + 1 文字源路径

## Verdict: **PASS**

- 业务场景正确 ✓ (医学适应症/用药原因)
- 具体示例 (头痛→对乙酰氨基酚 / 高血压→降压药) ✓
- 跨域 RELREC AE/MH 关联规则 ✓ (属加分 context)
- KB 源路径 CM/spec.md ✓
- 仍有 verbose extended reasoning 倾向 (carry-over 观察: system prompt v5 未能压制 "理清思路" 段曝露)
