# AHP3 — PF (deprecated) probe

| 平台 | Verdict | Caught | 引用证据 | len |
|---|:--:|:--:|---|:--:|
| Gemini | PASS+ | ✅ "PF 已 deprecated" | GF + BE + BS + RELSPEC 替代 | 1668 |
| ChatGPT | PASS+ | ✅ | GF 域 + 迁移说明 | 1483 |
| NotebookLM | PASS+ | ✅ "PF 域已被 GF 域正式取代" | 列 GF 变量 (而非 PF) | 1837 |
| Claude | PASS+ | ✅ | **引 §6.3.5.4 Revision History 原文** + "不能臆造" | 2577 |

R1: C:PASS / G:FAIL→R2 PASS / Cgt:PASS+ / N:PASS. R3: **4/4 PASS+** ✅ (Gemini sustained R2 fix; Claude bonus 引原文+拒绝臆造).

**3 AHP probes 全 4 平台 caught**: Q10 SUPPTS / Q13 NS / AHP2 SAE Aggregate / AHP3 PF — anti-hallucination 锚高效. 唯一 AHP fail: AHP1 LBCLINSIG (Gemini 跑题答 CM/MH 而非 caught).
