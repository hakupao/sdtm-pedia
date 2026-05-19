# Q11 — Dataset-JSON v1.1 vs XPT v5 (Gemini bonus)

| 平台 | Verdict | Dataset-JSON | XPT 痛点 | XPT 仍需 | Define-XML 互补 | len |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Gemini | **FAIL** | ❌ 跑题答 AE/CM | ❌ | ❌ | ❌ | 1436 (bonus 容错允许 — Q11-Q14 Gemini 弱项) |
| ChatGPT | PASS+ | ✅ | ✅ 8/200/metadata | ✅ | ✅ | 2804 |
| NotebookLM | PARTIAL | KB outside, 但答 (a)/(d) | ✅ 8/无 Unicode | — | ✅ | 1629 |
| Claude | PASS+ | ✅ | ✅ 8/200/Unicode/metadata | partial | ✅ | 3964 |

R1: C:PASS / G:PASS / Cgt:PASS / N:PUNT. R3: 2 PASS+, Gemini bonus FAIL, NotebookLM PARTIAL. **关键 finding**: Gemini Q11 跑题 = 2nd 跑题事件 (Q3 + Q11), 都在 KB 外/邻域题. v8 prompt 需加 "题外 SDTM 知识 → 必须 ground 在 KB 或 web search 而非 hallucinate" 锚.
