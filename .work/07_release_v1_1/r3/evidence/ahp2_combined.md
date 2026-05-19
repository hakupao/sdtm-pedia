# AHP2 — Trial-Level SAE Aggregate 表 (cross-domain hallucination)

| 平台 | Verdict | Caught | 真位置说明 | len |
|---|:--:|:--:|---|:--:|
| Gemini | PASS+ | ✅ "SDTM Tabulation 层无汇总表" | ADAE / CSR / SDRG | 1351 |
| ChatGPT | PASS+ | ✅ "不要用 RELREC 跨接" | ADRG / Define-XML / ADaM | 1702 |
| NotebookLM | PASS+ | ✅ "衍生汇总→ADaM, 不在 SDTM" | + TS 域澄清 | 1661 |
| Claude | PASS+ | ✅ "没有 Trial-Level SAE Aggregate 域" | + CIOMS/E2B/DSUR/PSUR refs | 2470 |

R1: C:PASS / G:FAIL→R2 PASS / Cgt:PASS / N:PASS. R3: **4/4 PASS+** ✅. Gemini sustained R2 fix this time (vs AHP1 regression).
