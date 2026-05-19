# Q5 — Cross-Platform Combined (FA/QS/CE 三场景)

| 平台 | Verdict | A=FA (DAS28) | B=QS (SF-36) | C=CE (dizziness) | Bonus |
|---|:--:|:--:|:--:|:--:|---|
| Gemini | PASS | ✅ FATESTCD=DAS28 | ✅ QSCAT=SF-36 | ✅ CE | — |
| ChatGPT | PASS+ | ✅ + RELREC FA↔MH | ✅ QSCAT/QSTESTCD | ✅ + CEDUR=PT30S ISO | RELREC FA-MH + CEDUR |
| NotebookLM | PASS | ✅ | ✅ + C85441 CE codelist | ✅ | RAG 5 KB files |
| Claude | PASS+ | ✅ | ✅ + C100174 SF-36 CT | ✅ | ch04 §6.4.3 / §8.6.1 / §8.6.3 + class refs |

**R1→R3 delta**: All PASS R1→R3, 0 regression, 2 PASS+ upgrade.

Raw lens: G:1196 / Cgt:1156 / N:1262 / C:2823
