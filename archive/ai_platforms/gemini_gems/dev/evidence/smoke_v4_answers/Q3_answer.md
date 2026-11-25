# Gemini Gems — Q3 BE+BS+RELSPEC (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM | **题类**: Q3 (A3 v3.4 新域)

## Raw 回答摘要

- **(a)** 3 阶段全 BE (Events class) + Topic **BETERM** + 分类 **BECAT**:
  - 采血: BETERM="Blood Collection", BECAT="COLLECTION"
  - 运输: BETERM="Transport to Central Lab", BECAT="TRANSPORT"
  - DNA 提取: BETERM="DNA Extraction", BECAT="EXTRACTION" / "PREPARATION"
- **(b)** BS (Findings) + **BSTESTCD/BSTEST** (Req, CT C124300):
  - 体积: BSTESTCD="VOLUME" / BSORRES=5 / BSORRESU="mL"
  - RIN: BSTESTCD="RIN" / BSORRES=9.2
  - **边界提示**: 同一天采血行为+测量必双域并行 (BE + BS)
  - **Anti-hallucination**: "绝对禁止臆造 BM (Biospecimen Measurements) 域, v3.4 测量一律走 BS"
- **(c)** **RELSPEC** (not RELREC) — specimen lineage 专用

**Citation**: 0 inline, 文字源路径

## Verdict: **PASS** (全 3 部分正确 + 主动识破 BM 虚构域 anti-hallucination 加分)
