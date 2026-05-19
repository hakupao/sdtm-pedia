# Q9 — Pinnacle 21 5 大类 FAIL + 修 vs SDRG

| 平台 | Verdict | 5 cats | SDRG | bonus | len |
|---|:--:|:--:|:--:|:--:|:--:|
| Gemini | PASS | 5/5 (CT/IDVAR/ISO/跨域/Req) | ✅ | 决策表 | 1684 |
| ChatGPT | PASS+ | 4/5 + extra | ✅ | 5301 chars 最深 | 5301 |
| NotebookLM | **PUNT** | 0/5 | ✅ (KB 未覆盖) | policy-correct in-KB-only 拒答 | 610 |
| Claude | PASS | 4/5 + SDRG | ✅ | — | 2702 |

R1: C:PASS / G:PASS / Cgt:PASS / N:PARTIAL. R3: 3/4 PASS, N:PUNT (架构限制, 与 R1 PARTIAL 等价 — RAG 限制, 非 regression).
