# Q8 — CT Extensible + AETERM vs MedDRA edge

| 平台 | Verdict | Ext语义 | NY/AESEV NonExt | AETERM≠MedDRA | AEDECOD=MedDRA | Define-XML 扩 | len |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Gemini | PASS | ✅ | ✅ | ✅ | ✅ | ✅ | 1559 |
| ChatGPT | PASS+ | ✅ | ✅ | ✅ verbatim | ✅ | ✅ def:ExtendedValue + LBTESTCD C65047 | 2511 |
| NotebookLM | PASS+ | ✅ | ✅ | ✅ | ✅ | ✅ | 1936 |
| Claude | PASS+ | ✅ | ✅ | ✅ | ✅ | ✅ | 3519 |

R1: 4/4 PASS. R3: 4/4 PASS, 0 regression. **关键 AHP probe** (AETERM 不绑 MedDRA) **4/4 通过** — anti-misspeak 锚有效.
