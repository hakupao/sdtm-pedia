# Q4 — Cross-Platform Combined Evidence

> Q4 (B1 — LB vs MB vs IS): 3 场景 (麻疹 IgG / ADA / Mtb 培养) 归域
> R1 baseline: C:PASS / G:PARTIAL→R2 PASS / Cgt:PASS / N:PASS
> R3 关键: v3.4 IS scope 变化 — anti-microbial antibody 全归 IS (assumption 2)

## Verdict 矩阵

| 平台 | Verdict | A 麻疹 IgG | B ADA | C Mtb |
|---|:--:|---|---|---|
| Gemini Gem | **FAIL** ⚠️ | **LB** ❌ (错, 应 IS per assumption 2) | IS ✓ | MB ✓ |
| ChatGPT GPT | PASS+ | **IS** ✓ + v3.4 显文纠错防呆 + ISBDAGNT=MEASLES VIRUS | IS + ISTSTOPO SCREEN/CONFIRM/QUANTIFY | MB + MBTSTDTL/MBSPEC/MBMETHOD |
| NotebookLM | PASS+ | IS + ISCAT=NON-STUDY-RELATED IMMUNOGENICITY | IS + ADA_BAB/ADA_NAB | MB + MTB |
| Claude Project | PASS+ | IS + MBIGGAB + ISBDAGNT=MEASLES + ISCAT=NSR IMMUNOGENICITY + ISSCAT=HUMORAL IMMUNITY + ISTSTOPO=QUANTIFY + ISORRES=1:128 + 引 IS Example 5/8 | IS + 分层 SCREEN/CONFIRM/QUANTIFY + 引 IS Assumption 7a 原文 + Example 1 | MB + MCORGIDN + SPUTUM + MICROBIAL CULTURE |

## R1 vs R3 Delta

| 平台 | R1 | R3 | Delta |
|---|:--:|:--:|---|
| Gemini | PARTIAL→R2 PASS | **FAIL** | ⚠️ **REGRESSION** (R2 修过的 A 场景退回 LB) |
| ChatGPT | PASS | PASS+ | ↑ |
| NotebookLM | PASS | PASS+ | ↑ (HIV Ag/Ab 豁免 bonus) |
| Claude | PASS | PASS+ | ↑ (Assumption 7a + Example 1/5/8 引用) |

## Gemini regression 根因 (Q3+Q4 共性)

**两题连续 regression 模式**:
- Q3: 跑题答 AE 而非 BE/BS/RELSPEC
- Q4: A 场景答 LB 而非 IS

**共性**: Gemini Pro 在 v7.1 system prompt 下, 对"间接 IS/BE 类话题"走通用 SDTM 兜底路径 (AE/LB), 没有充分锚定 v3.4 scope 变化 (IS assumption 2, BE/BS/RELSPEC PGx 新域).

→ **R3 RETRO 关键 finding**: Gemini v7.1 CO 锚未 cover 到 IS scope shift (v3.3→v3.4) + PGx specimen 新域. Follow-up = v8 cut 加 CO-N 专项锚.

## Raw response paths

- Gemini: 1597 chars (A=LB FAIL, B/C 对)
- ChatGPT: 1938 chars (3/3 对)
- NotebookLM: 2250 chars (3/3 对 + HIV 豁免)
- Claude: 3762 chars (3/3 对 + Assumption 原文引用)
