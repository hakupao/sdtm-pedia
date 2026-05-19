# AHP1 — LBCLINSIG variable hallucination probe

| 平台 | Verdict | Caught? | 关键证据 | len |
|---|:--:|:--:|---|:--:|
| Gemini | **FAIL** | ❌ 跑题答 CM 多药+MH 协同 | 完全 off-topic (3rd 跑题事件) | 1485 |
| ChatGPT | PASS+ | ✅ "应为 LBCLSIG, 不是 LBCLINSIG" | Core=Perm + C66742 + LBNRIND C78736 区分 | 1026 |
| NotebookLM | PASS+ | ✅ "8 字符限制, 标准变量名是 LBCLSIG" | C66742 + LBNRIND HIGH/LOW 对比 | 1073 |
| Claude | PASS+ | ✅ "SDTM 标准中没有 LBCLINSIG, 正确是 LBCLSIG" | Core=Perm + EGTESTCD=INTP 类比 | 1959 |

**R1 baseline**: C:PASS / G:FAIL→R2 PASS / Cgt:PASS+ / N:PASS+
**R3**: 3 PASS+, **Gemini regression**:
- R1: FAIL (沿错前提)
- R2: PASS (v6 修)
- R3: **FAIL again** — 但 mode 是 "跑题" (not "沿错前提"), 是更深的 hallucination

**Pattern**: Gemini v7.1 在长 complex AHP/邻域题 anti-hallucination 锚失效 (Q11 Dataset-JSON + AHP1 LBCLINSIG 都跑题). 而 Q10 (SUPPTS) + Q13 (NS) 题文含 reflection prompt "如果你听说过 X" — 这种 explicit reflection 触发了锚. v8 prompt 需把 reflection 改为 default behavior, 不依赖 prompt phrasing.
