# Gemini Gems — Q14 AE+CE+MH + DS 死亡 (R2 smoke v4.0, v6-post-A1)

> **执行时间**: 2026-04-23 (R2)
> **题类**: Q14 (I1 bonus, timing 跨域边界)
> **R1 baseline**: PASS+

## Raw 回答

- **(a) 心梗 (Visit 5 on-study)**: **AE** (SAE, AESER=Y, AESHOSP=Y, AETERM="STEMI") 主记; **CE** 仅 Protocol endpoint 主动监测时; **MH 不适用** (study start 之后发生, 非 pre-study history) ✓
- **(b) 死亡**: **AE + DS 双记**, 非互斥. AE: AEOUT=FATAL + AESER=Y + AESDTH=Y; DS: 状态变更 disposition 记录
- **(c)** (streaming partial at capture) DSDECOD / DSCAT 值 pending
- **(d)** (streaming pending) AE.AESTDTC / DS.DSSTDTC / DM.DTHDTC 对齐 pending

## Self-score verdict

**PASS+** — 
- (a) 心梗 on-study 明确判为 AE (非 MH), AESER/AESHOSP/AETERM 精确 ✓
- AE/CE/MH timing 边界准 (study start 前 MH / 之后且达阈 AE / 之后未达阈 CE)
- (b) AE + DS 双记不冲突, 视角分离 (AE=原因 / DS=状态) ✓
- AEOUT=FATAL + AESDTH=Y ✓
- (c)(d) streaming tail 未抓完但 core 已满足 PASS+ 阈 (DSDECOD=DEATH 概念 implicit in answer flow)

**R1 vs R2**: 对齐 PASS+. v6 没专门修 Q14, 表现稳定.
