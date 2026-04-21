# Q2 — AE 域 SAE 判定类变量 (AESER + 6 子变量)

**URL**: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e6eec8-fa68-83aa-abeb-ef0d3d552545
**Title**: SDTM Expert - SAE 变量填写
**Run**: 2026-04-21 (第二轮 JS paste 成功)

## 原题

一位受试者服药后出现严重皮疹并因此住院 3 天治疗. Investigator 判断为药物相关的严重不良事件. 请问 SDTM AE 域中, 该如何记录这条事件的严重性相关变量 (AESER 及其子变量)? 请列出需要填写的 SAE 判定类变量 (AESER / AESCONG / AESDISAB / AESHOSP / AESLIFE / AESDTH / AESMIE) 各自的含义和本例取值, "Y" 还是 "N"?

## ChatGPT 答案

| 变量 | 含义 | 本例取值 | 理由 |
|------|------|---------|------|
| AESER | 是否为严重不良事件 (overall seriousness) | Y | Investigator 已判 SAE |
| AESCONG | 是否导致先天异常/出生缺陷 | N | 本例无此信息 |
| AESDISAB | 是否导致持续性或显著残疾/失能 | N | 本例无此信息 |
| AESHOSP | 是否需要住院或延长住院 | Y | 事件后住院 3 天 |
| AESLIFE | 是否危及生命 | N | 题干未提 life-threatening |
| AESDTH | 是否导致死亡 | N | 未死亡 |
| AESMIE | 是否属于其他医学上重要的严重事件 | N | 已被住院满足, 无需 MIE 兜底 |

额外加分: 主动区分 seriousness (AESER) vs severity (AESEV), 提醒"本例很可能既 AESEV=SEVERE, 又 AESER=Y".

## PASS 判据自检

- [x] AESER = Y (严重事件) ✓
- [x] AESHOSP = Y (导致住院) ✓
- [x] AESLIFE = N (非危及生命) ✓
- [x] AESDTH = N (非导致死亡) ✓
- [x] AESDISAB = N (非致残) ✓
- [x] AESCONG = N (非先天异常) ✓
- [x] AESMIE = N (非重要医学事件, 住院已覆盖) ✓
- [x] 每变量有简短中文/英文含义 ✓

## FAIL 判据自检

- [ ] AESER 填错? **否** (Y 正确)
- [ ] AESHOSP 填 N? **否** (Y 正确)
- [ ] 子变量缺失 >=2 个未说明? **否** (7 变量全列含义+取值+理由)

## Verdict: **PASS**

7/7 子变量取值全对 + 每变量含义清晰 + 额外区分 seriousness vs severity (加分). 无任何 FAIL 判据命中.
