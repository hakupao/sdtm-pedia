# Q10 — SUPPTS AHP probe (premise hallucination)

| 平台 | Verdict | SUPPTS caught | TSVAL1-n | SUPPQUAL scope | QORIG/QEVAL | len |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Gemini | **PASS+** | ✅ "Trial Design 不适用 SUPPQUAL" | ✅ | ✅ E/F/I + DM + SV | ✅ | 1506 |
| ChatGPT | PASS+ | ✅ "不应建 SUPPTS" | ✅ | ✅ §8.4 | ✅ | 2174 |
| NotebookLM | PASS+ | ✅ "no such dataset as SUPPTS" | ✅ | ✅ E/F/I + DM + SV | ✅ Req/Exp 角色明 | 4690 |
| Claude | PASS+ | ✅ + §4.5.3.2 + §7.4.2 引用 | ✅ + 拆分规则 + Label 一致 | ✅ | ✅ | 4729 |

**Q10 = 4/4 PASS+** ✅. R1: G:PARTIAL→R2 PASS / Cgt:PASS+ / C:PASS / N:PASS+. R3: **all 4 PASS+, Gemini 从 R1 PARTIAL 升 R3 PASS+** (anti-hallucination 锚有效).
