# Gemini Gems — smoke v4.0 R1 Results

> **题库**: `ai_platforms/SMOKE_V4.md §2` v4.0 (17 题 = Q1-Q14 + AHP1-3, **Q11-Q14 bonus 容错**)
> **执行 plan**: `ai_platforms/SMOKE_V4.md §1 §2.2`
> **平台**: Gemini Gems (bojiang.zhang.0904@gmail.com / Gemini Pro)
> **Gem**: SDTM Expert (`https://gemini.google.com/gem/3b572e310813`)
> **Mode**: Pro (Gemini 3.1 Pro) per question
> **方法**: Chrome MCP full-auto (Quill editor + execCommand + InputEvent + wait 2s + click 分离)
> **system_prompt**: v5 (7925/8000 chars, N5.2 lock — R1 不动)
> **knowledge files**: 4 files (N4 + N5.1 04 v5b)
> **执行时间**: 2026-04-22 PM —
> **阈值** (双阈值机制):
> - **主 gate** (Q1-Q10 + AHP1-3 = 13 题): ≥9/13 (70%) 必 PASS
> - **Bonus track** (Q11-Q14 = 4 题): FAIL 容错, PASS 加分
> **答案存档**: `dev/evidence/smoke_v4_answers/`

---

## Sanity preflight (底座稳定性 4 题, 若复用 smoke v3 sanity 1-4 可 skip)

| # | 题 | Verdict | 备注 |
|:---:|---|:---:|---|
| sanity_01 | AESER Core=Exp | **PASS** | Core=Exp + AE/spec.md 文字引用; 无 inline citation (Gemini 特性) |
| sanity_02 | LBNRIND 全值 | **PARTIAL (0.5)** | 4 值 ✓ / Extensible 答"KB 未明确" ✗ (general_part4.md L63-72 其实有, Gemini 04_business_scenarios 未覆盖该属性); verbose extended reasoning 暴露 |
| sanity_03 | CMINDC indication | **PASS** | 业务场景 + RELREC AE/MH 关联 + CM/spec.md; 仍有 extended reasoning 暴露 |

---

## 正式 17 题 (Q1-Q14 + AHP1-3)

### 主 gate 13 题 (Q1-Q10 + AHP1-3)

| # | Type | 主题 | Verdict | 触发 FAIL 判据 | 备注 |
|:---:|---|---|:---:|---|---|
| Q1 | A1 v3.4 新域 | GF EGFR 变异 | **PASS** | — | 域 ✓ + 5 Req + 3 Exp (GFSTAT 分类 borderline) + abcd 全对 + C181177; extended reasoning 暴露 |
| Q2 | A2 v3.4 新域 | CP 流式 CD4+ | **PASS** | — | 全 5 部分正确; 本次干净答复无 extended reasoning 暴露 |
| Q3 | A3 v3.4 新域 | BE+BS+RELSPEC | **PASS** | — | BECAT 三档 + BS C124300 + RELSPEC + anti-hallucination 识破 BM 虚构 |
| Q4 | B1 域边界 | LB vs MB vs IS | **PARTIAL (0.5)** | 未显式映射 A/B/C + 缺 Topic | 给通用原则 + 边界规则正确, 但题目要求的分场景答法未满足; R2 改点: prompt 加"多场景题逐个显式答" |
| Q5 | B2 域边界 | FA vs QS vs CE | **PASS** | — | A=FA/B=QS/C=CE + 理由 + Topic 变量; 无 extended reasoning 暴露 (较 sanity early 好转); 未显式 §8.6.3 锚点 |
| Q6 | C1 Timing | PK --TPT 四件套 | **PASS** | — | 5 vars + abcd 全对 (PT4H + VISIT+TPTREF+EPOCH) + 干净无 extended reasoning; R2 显式分场景答有效 |
| Q7 | C2 Timing | Partial date SDTM/ADaM | **PARTIAL (0.5)** | (e) 层混淆幻觉: 称 SDTM 要记 --DTF (AEDTF/CMDTF), 实际 --DTF 是 ADaM-only (ASTDTF/AENDTF) | 3 场景 + (d) 对, (e) HALLUCINATION |
| Q8 | D1 CT | Extensible + MedDRA 绑定 | **PARTIAL (0.5)** | (b) C66767 Action Taken 错分 Ext=Yes (实际 Non-Ext) + C66742 只列 Y/N (缺 U/NA) | (a)(c)(d) 对; 2 个 (b) 错误降 Partial |
| Q9 | E1 实战 | Pinnacle 21 FAIL 分类 | **PASS** | — | 5 类 + 修 vs 文档化 清晰 + Non-Ext 必修 / Ext 文档化; 缺 Rule ID + 无 TRC 层 |
| Q10 | H1 SUPP | QORIG/QEVAL + SUPPTS 前提纠错 | **PASS** | (a) QORIG/QEVAL Core=Perm 错 (应 Req/Exp) + (b) scope 漏 SV | **"严禁使用 SUPPTS (SDTM 不存在)"** + TSVAL1-n 替代 ✅ 识破; (c)(d) 对 (含数值→字符/8-char AEREMAR1); SUPPTS 识破作 bonus 抵一项 Core attr 硬伤 |
| **AHP1** | Z1 variable hallucination | LBCLINSIG 虚构 | TBD | — | — |
| **AHP2** | Z2 cross-domain hallucination | Trial-Level SAE Aggregate | TBD | — | — |
| **AHP3** | Z3 deprecated concept | PF 已废 | TBD | — | — |

**主 gate 小计**: TBD/13 (阈值 ≥9/13, 70%)

### Bonus track 4 题 (Q11-Q14, FAIL 容错)

| # | Type | 主题 | Verdict | 备注 |
|:---:|---|---|:---:|---|
| Q11 | F1 新技术 | Dataset-JSON v1.1 vs XPT v5 | TBD | 4-file KB 不含, FAIL 容错 |
| Q12 | D2 CT | CT 版本 + Define-XML + MedDRA | TBD | 4-file KB 不含, FAIL 容错 |
| Q13 | G1 RWD | Observational + ARMCD | TBD | 4-file KB 不含, FAIL 容错 |
| Q14 | I1 跨域 | AE/MH/CE + DS 死亡 | TBD | 4-file KB 不含, FAIL 容错 |

**Bonus 小计**: TBD/4

---

## 总分

| 指标 | 值 |
|---|---|
| 总题数 | 17 (13 主 + 4 bonus) |
| 主 gate 分 | TBD/13 |
| Bonus 分 | TBD/4 |
| **全量分** | TBD/17 |
| 主 gate 阈值 | ≥9/13 (70%) |
| **Gate** | TBD |

---

## 主结论 (R1 跑完填)

- system_prompt v5 anti-hallucination 锚点 AHP 表现: TBD
- CO-4 4-file KB vs supplemental topics gap (Q11-Q14): TBD
- Q10 SUPPTS 前提纠错能力 (v4.0 patch): TBD
- F-1/F-3 carry-over: TBD
