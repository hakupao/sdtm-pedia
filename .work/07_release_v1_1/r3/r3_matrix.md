# SMOKE_V4 R3 — Cross-Platform Matrix (17 × 4 = 68 cells)

> 跑题后填. 单元格格式: `PASS` / `PASS+` / `PARTIAL` / `FAIL` / `PUNT` / `—` (未跑)
> 详细每题 verdict 见 `evidence/<platform>/q<NN>.md`

| # | 题 (1 行简述) | Claude v2.6 | ChatGPT v2.2 | Gemini v7.1 | NotebookLM v2 | R1 基线 (对比) |
|:-:|---|:--:|:--:|:--:|:--:|---|
| Q1  | GF 域变量拼写 (GFINHERT) + Core | PASS+ | PASS | PASS | PASS | C:PASS / G:FAIL / Cgt:Q1拼写 R1 / N:PASS |
| Q2  | CP 细胞表型 (CPCSMRKS 等) | PASS+ | PASS+ | PASS | PASS | C:PASS / G:PASS / Cgt:PASS / N:PASS |
| Q3  | BE+BS+RELSPEC 生物样本 (v4.0 题, 非 v3.2 R1 DM ARMCD) | PASS+ | PASS+ | FAIL⚠️ | PASS | v3.2 R1 不同题 (DM ARMCD 4/4 PASS), 不可直接 regression 比较; R3 v4.0 = 3/4 PASS, Gemini 跑题 |
| Q4  | LB vs MB vs IS 三场景 (麻疹/ADA/Mtb) | PASS+ | PASS+ | FAIL⚠️ | PASS+ | C:PASS / G:PARTIAL→PASS R2 / Cgt:PASS / N:PASS — ⚠️ Gemini A 答 LB 退回 R2 修复前 |
| Q5  | FA/QS/CE 三场景 (DAS28/SF-36/dizziness) | PASS+ | PASS+ | PASS | PASS | C:PASS / G:PASS / Cgt:PASS / N:PASS — 4/4 ✓ |
| Q6  | PK 时间窗 PCTPT/PCTPTREF 四件套 | PASS+ | PASS+ | PASS | PASS | C:PASS / G:PASS / Cgt:PASS / N:PASS — 4/4 ✓ |
| Q7  | DTC imputation (partial date) | PASS+ | PASS+ | PASS | PASS | C:PASS / G:PASS / Cgt:PASS / N:PASS — 4/4 ✓ |
| Q8  | CT Extensible + AETERM≠MedDRA | PASS+ | PASS+ | PASS | PASS+ | C:PASS / G:PASS / Cgt:PASS+ / N:PASS+ — 4/4 ✓ |
| Q9  | Pinnacle 21 FAIL 5 类 + SDRG | PASS | PASS+ | PASS | PUNT | C:PASS / G:PASS / Cgt:PASS / N:PARTIAL — 3 PASS + N:PUNT (in-KB 限制持平) |
| Q10 | SUPPTS 前提纠错 (AHP) | PASS+ | PASS+ | PASS+ | PASS+ | C:PASS / G:PARTIAL→PASS R2 / Cgt:PASS+ / N:PASS+ — 4/4 PASS+ ★ |
| Q11 | Dataset-JSON v1.1 (bonus) | PASS+ | PASS+ | FAIL (跑题) | PARTIAL | C:PASS / G:PASS / Cgt:PASS / N:PUNT (bonus) — Gemini 跑题 (2nd 跑题事件) |
| Q12 | CT 版本锁定 (bonus) | PASS+ | PASS | PASS | PASS | C:PASS / G:PASS / Cgt:PASS / N:PUNT — 4/4 ✓ (N 升级) |
| Q13 | RWD + ARMNRS + NS premise AHP | PASS+ | PASS+ | PASS+ | PASS+ | C:PASS / G:FAIL R1→PASS R2 / Cgt:PASS / N:PASS — **4/4 PASS+ ★** |
| Q14 | AE+CE+MH timing + DS 死亡跨域 | PASS | PASS+ | PASS | PASS | C:PASS / G:PASS / Cgt:PASS / N:PASS — 4/4 ✓ |
| AHP1 | LBCLINSIG var hallucination | PASS+ | PASS+ | **FAIL** | PASS+ | C:PASS / G:FAIL R1→PASS R2 / Cgt:PASS / N:PASS — Gemini regression⚠️ 跑题 |
| AHP2 | Trial-Level SAE Aggregate 表 | PASS+ | PASS+ | PASS+ | PASS+ | C:PASS / G:FAIL R1→PASS R2 / Cgt:PASS / N:PASS — **4/4 PASS+ ★** |
| AHP3 | PF deprecated→GF (AHP) | PASS+ | PASS+ | PASS+ | PASS+ | C:PASS / G:FAIL R1→PASS R2 / Cgt:PASS+ / N:PASS — **4/4 PASS+ ★** |

**汇总** (R3 完成 2026-05-19):

| 平台 | R3 PASS 计数 | R3 PASS+ 计数 | R3 总分 (PASS+=1, PASS=1, PARTIAL=0.5, FAIL/PUNT=0) | R1 基线分 | R3 vs R1 delta | Gate (R3 ≥ R1?) |
|------|:-:|:-:|:-:|:-:|:-:|:-:|
| Claude v2.6 | 17 | 11 | **17/17** | 17/17 | = 持平 (11 题 PASS+ 升级) | ✅ |
| ChatGPT v2.2 | 17 | 13 | **17/17** | 16.5/17 | ↑ +0.5 | ✅ |
| Gemini v7.1 | 13 + PARTIAL=0 | 5 | **13/17 (76%)** | 16/17 (94%) | ↓ -3 ⚠️ | ⚠️ regression |
| NotebookLM v2 | 15 + PARTIAL/PUNT=0.5 | 11 | **15.5/17 (91%)** | 15/17 | = 持平 | ✅ |

**Gemini regression detail** (R1 16/17 → R3 13/17):
- Q3 跑题 (v4.0 题不同, 不可直比)
- Q4 A scenario 答 LB (R2 修过的退回)
- Q11 跑题 (bonus 容错允许)
- AHP1 跑题 (R2 修过的退回 LBCLINSIG 不识破)

**Gemini sustained R2 fix**:
- Q10 SUPPTS premise: caught ✓
- Q13 NS premise: caught ✓
- AHP2 SAE Aggregate: caught ✓
- AHP3 PF deprecated: caught ✓

**关键 finding**: Gemini AHP probe **4/5 caught** (Q10/Q13/AHP2/AHP3). AHP1 FAIL pattern = 题文短 + 无 reflection prompt 时, v7.1 anti-hallucination 锚失效. v8 应将 reflection 改为 default.

**R3 通过判定**: 3/4 平台 (Claude/ChatGPT/NotebookLM) PASS gate, Gemini regression 但 4/5 AHP 仍 caught — 整体可接受, 待 v1.2 修 Gemini v8 prompt.
