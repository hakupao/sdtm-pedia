# Gemini Gems — Q4 LB vs MB vs IS 三场景 (R1 smoke v4.0)

> **执行时间**: 2026-04-22 晚 | **题类**: Q4 (B1 域边界) | **Fresh chat**: ✓ (URL `/gem/3b572e310813/2bbb634b7a72c83b`)

## Raw 回答摘要

给出了通用三域归类原则, **但未显式映射到题目 A/B/C 三场景**, 也未列 Topic 变量示例.

- 通用原则表:
  - 常规化学/血液学/尿液 → LB
  - 病原体检测/鉴定 → MB
  - 免疫原性/血清学 → IS
- 边界规则提到:
  - LB vs IS 细胞因子/补体例外
  - IS vs MB Ag/Ab 组合检测 → MB
  - MB vs MS 药敏测试 → MS
  - IS vs CP 流式细胞术 → CP

**KB 源**: LB/assumptions.md + MB/assumptions.md + IS/assumptions.md

## Verdict: **PARTIAL (0.5)**

- 通用分类原则正确 ✓
- 边界规则明确 ✓ (含 v3.4 细节)
- **未满足题目要求: 没有明确说"场景 A→IS / B→IS / C→MB"** + 没给 Topic 变量示例 ✗
- 可能是 Gemini 对题目理解偏差 (回答了"三类原则", 没回答"具体 3 场景")
- FAIL 判据 (未触): 没答错域归类 — 只是不完整
- **R2 改点**: system prompt 可加 "对多场景题必须逐个场景显式回答, 不可给通用原则"
