# NotebookLM — Q3 BE+BS+RELSPEC (R1 smoke v4.0)

> **执行时间**: 2026-04-22 PM | **题类**: Q3 (A3 v3.4 新域)

## Raw 回答摘要

- **(a)** 3 阶段全 BE 域 + **BETERM** (Topic Req):
  - 采血 BETERM = "Collecting"
  - 运输 BETERM = "Shipping"
  - DNA 提取 BETERM = "Extracting"
- **(b)** BS 域 + **BSTESTCD/BSTEST** (Topic Req):
  - 体积: BSTESTCD="VOLUME", BSTEST="Volume", BSORRES="5", BSORRESU="mL"
  - RIN: BSTESTCD="RIN", BSTEST="RNA Integrity Number", BSORRES="9.2"
- **(c)** **RELSPEC** (not RELREC) — Specimen lineage 专用:
  - REFID = DNA-001 (子)
  - PARENT = BS-001 (父)
  - LEVEL = 2 (原始=1, 派生=2)

**Citation**: 多 inline (BE/BS/RELSPEC 源 bucket)

## Verdict: **PASS+** (全 3 部分 + RELSPEC REFID/PARENT/LEVEL 完整机制)
