# ChatGPT GPTs — smoke v4.0 R1 Results

> **题库**: `ai_platforms/SMOKE_V4.md §2` v4.0 (17 题 = Q1-Q14 + AHP1-3)
> **执行 plan**: `ai_platforms/SMOKE_V4.md §1 §2.3`
> **平台**: ChatGPT GPTs (Plus 账号)
> **Custom GPT**: SDTM Expert (`https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert`)
> **system_prompt**: v2 (7568 bytes, N5.2 lock — R1 不动)
> **knowledge files**: 9 files (N4 batch 2)
> **方法**: Chrome MCP cowork paste (ClipboardEvent 绕 DataTransfer)
> **执行时间**: 2026-04-22 PM —
> **阈值**: ≥12/17 (71%) 全量 gate
> **答案存档**: `dev/evidence/smoke_v4_answers/`

---

## Sanity preflight

| # | 题 | Verdict | 备注 |
|:---:|---|:---:|---|
| sanity_01 | AESER Core=Exp | **PASS** | Core=Exp + AE/spec.md + 提到 04_domain_specs_all.md 合并文件 |
| sanity_02 | LBNRIND 全值 | **PASS** | 4 值 + Ext=Yes + LB/spec.md + general_part4.md |
| sanity_03 | CMINDC | **PASS** | CRF "Other, specify" + SUPPCM QNAM=CMINDOTH 精确机制 + ch04 §4.2.7.1 |

---

## 正式 17 题 (Q1-Q14 + AHP1-3)

| # | Type | 主题 | Verdict | 触发 FAIL 判据 | 备注 |
|:---:|---|---|:---:|---|---|
| Q1 | A1 v3.4 新域 | GF EGFR 变异 | **PARTIAL (0.5)** | (d) GFINHERTG 拼写错 (应 GFINHERT) | 域 ✓ + 5 Req + 3 Exp + (a)(b)(c) ✓ + L858R 临床纠错 bonus; Extended 推理 ~3 min |
| Q2 | A2 v3.4 新域 | CP 流式 CD4+ | **PASS** | — | 全 5 部分 + Ki67+ PROLIFERATING 精度 note |
| Q3 | A3 v3.4 新域 | BE+BS+RELSPEC | **PASS+** | — | BEREFID → child specimen 精确规则 + BE Example 2 plasma→RNA 模板 |
| Q4 | B1 域边界 | LB vs MB vs IS | **PASS** | — | A=IS/B=IS/C=MB 全对 + 理由 + Topic 变量 + v3.4 边界规则 3 步 + 3 关键例外; IS baseline ISCAT 条件区分 study-related vs non-study-related |
| Q5 | B2 域边界 | FA vs QS vs CE | **PASS** | — | A=FA/B=QS/C=CE + 结论表 + 源溯源 + SDTMIG §8.6.3 锚点 + 补判断 (A not CE / C not AE) |
| Q6 | C1 Timing | PK --TPT 四件套 | **PASS+** | — | 2 周期表 + 5 vars 全对 (4H/4/PERIOD-DOSE/PT4H/ISO datetime) + abcd 全对 + Pre-dose=-1 编码 + planned vs actual |
| Q7 | C2 Timing | Partial date SDTM/ADaM | **PASS+** | — | 3 场景全对 + §4.4.2 锚点 + 相对 timing 完整清单 (STRTPT/STTPT/ENRTPT/ENTPT) + SDTM/ADaM 边界清晰 |
| Q8 | D1 CT | Extensible + MedDRA 绑定 (v4.0 AETERM fix) | **PASS+** | — | (a)(b)(c)(d) 全对 + C-code 全对 (C66769/C66768/C111110/C124307) + AETERM 不绑 CT 精确纠偏 + Define-XML LB 扩充 5 条 |
| Q9 | E1 实战 | Pinnacle 21 FAIL 分类 | **PASS+** | — | 6 类 FAIL + 三问法决策 + Must Fix / Explain and Keep 两篮 + 坦诚标注非 P21 官方分组 |
| Q10 | H1 SUPP | QORIG/QEVAL + SUPPTS 前提纠错 (v4.0 HIGH fix) | **PASS+ 最强** | — | SUPPTS 识破 + TSVAL1-n + GOC+DM+SV 完整 scope + **§4.2.8.4 Trial Design 多值参数 bonus** (TTYPE=EFFICACY/SAFETY 独到) + **场景 A/B 区分** (标准父变量 vs SUPP 自己 NSV) + 5 source 精准 citation |
| Q11 | F1 新技术 | Dataset-JSON v1.1 vs XPT v5 | TBD | — | — |
| Q12 | D2 CT | CT 版本 + Define-XML + MedDRA | TBD | — | — |
| Q13 | G1 RWD | Observational + ARMCD (v4.0 删 NS 虚构) | TBD | — | — |
| Q14 | I1 跨域 | AE/MH/CE + DS 死亡 (v4.0 §4.2.6 context) | TBD | — | — |
| **AHP1** | Z1 variable hallucination | LBCLINSIG 虚构 | TBD | — | — |
| **AHP2** | Z2 cross-domain hallucination | Trial-Level SAE Aggregate | TBD | — | — |
| **AHP3** | Z3 deprecated concept | PF 已废 | TBD | — | — |

---

## 总分

| 指标 | 值 |
|---|---|
| 总题数 | 17 |
| PASS (1 分) | TBD |
| PASS+ (1 + 0.25) | TBD |
| PARTIAL (0.5) | TBD |
| FAIL (0) | TBD |
| **总分** | TBD/17 |
| 阈值 | ≥12/17 (71%) |
| **Gate** | TBD |

---

## 主结论 (R1 跑完填)

- system_prompt v2 AHP 表现 (ChatGPT + web search + MedDRA 知识强可能易编): TBD
- Q13 v4.0 删 NS + 修 ARMCD 对之前 14/14 的稳定性: TBD
- Q11-Q14 9-file KB (batch 2) 覆盖充分性: TBD
- Q10 SUPPTS 前提纠错能力 (v4.0 patch): TBD
- F-1/F-3 carry-over: TBD
