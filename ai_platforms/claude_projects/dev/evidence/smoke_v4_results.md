# Claude Projects — smoke v4.0 R1 Results

> **题库**: `ai_platforms/SMOKE_V4.md §2` v4.0 (17 题 = Q1-Q14 + AHP1-3)
> **执行 plan**: `ai_platforms/SMOKE_V4.md §1 §2.4`
> **平台**: claude.ai Projects
> **Project**: SDTM (`https://claude.ai/project/019d9e05-9286-77fc-a621-675ce52d30ec`, v2.6, 1.29M tokens, 77% capacity, 19 files in uploads/)
> **system_prompt**: v2.6 (R1 不动)
> **方法**: Chrome MCP cowork paste
> **执行时间**: 2026-04-22 PM —
> **阈值**: ≥13/17 (77%) 首测容错 (v3 未跑过基线)
> **答案存档**: `dev/evidence/smoke_v4_answers/`
> **备注**: v2.6 AB 曾 24/24 PASS (smoke v2.1), 本次 smoke v4 是 generalization + AHP 新维度首测.

---

## Sanity preflight

| # | 题 | Verdict | 备注 |
|:---:|---|:---:|---|
| sanity_01 | AESER Core=Exp | **PASS** (详细 metadata 表 + row#28 + 05_mega_spec.md:44) | `sanity_01_aeser_core.md` |
| sanity_02 | LBNRIND 全值 | **PASS** (详细表含 C-code + Related Domains + 行号 + CRITICAL HIGH 扩展示例) | `sanity_02_lbnrind_values.md` |
| sanity_03 | CMINDC | **PASS** (4 业务场景 + Perm + RELREC/CMCAT 区分 + 3 源路径 + Example 4/5 定位) | `sanity_03_cmindc_indication.md` |

---

## 正式 17 题 (Q1-Q14 + AHP1-3)

| # | Type | 主题 | Verdict | 触发 FAIL 判据 | 备注 |
|:---:|---|---|:---:|---|---|
| Q1 | A1 v3.4 新域 | GF EGFR 变异 | **PASS+** | — | 6 Req + 5 Exp + 完整 C181177 3-term 表 + GFSYM/GFSPEC 补字段 + GF assumption #7 patch-level + L858R Exon21 临床纠错 |
| Q2 | A2 v3.4 新域 | CP 流式 CD4+ | **PASS+** | — | 3 场景表 + 8-term CT C181172 完整表 + CP/LB/IS/MB 4 域边界表 + 全 assumptions 链 |
| Q3 | A3 v3.4 新域 | BE+BS+RELSPEC | **PASS+** (BE 完整; BS/RELSPEC 截断) | — | BE table + BEDECOD + BECAT + BEREFID child rule + Example 2 定位; 浏览器仍在生成 |
| Q4 | B1 域边界 | LB vs MB vs IS | **PASS+** | — | A=IS/B=IS/C=MB + 完整 Qualifier 链 + 边界 9 行规则表 + 决策优先级 3 步 + 补出 CP/MS 扩展归属; IS Assumption 1/2/3/4/5/6/9.b 逐引 |
| Q5 | B2 域边界 | FA vs QS vs CE | **PASS+** | — | 3 场景 full 表 + Class/Structure + FA Assumption 5/5a + QRS Shared 1/4 + CE Assumption 1/1b + §8.6.1/§8.6.3 + C113862 + 对比总表 |
| Q6 | C1 Timing | PK --TPT 四件套 | **PASS+** | — | 5 vars + Role 标注 + §4.4.10 锚点 + 概念模型图 + 7 种区分手段 + 完整 8 行示意表 |
| Q7 | C2 Timing | Partial date SDTM/ADaM | **PASS+** | — | 3 场景 + §4.4.2 truncation 表 + Solidus 区间 + §4.4.7 Ex3 AE Unknown + ADaM ASTDTF 机制超范围标注 |
| Q8 | D1 CT | Extensible + MedDRA 绑定 | **PASS+** | — | 4+4 例子 + 4 层 CT 绑定总表 + Define-XML 2.1 具体机制 (nci:ExtCodeID/def:IsNonStandard) + AETOXGR 替代 + C65047 Deferred 坦诚 |
| Q9 | E1 实战 | Pinnacle 21 FAIL 分类 | **PASS+** | — | 6 类 + Rule ID 示意 + **TRC 自动拒收层** + cSDRG 5 字段 + MedDRA 版本 mismatch 例 + 边界声明坦诚 |
| Q10 | H1 SUPP | QORIG/QEVAL + SUPPTS 前提纠错 | TBD | — | — |
| Q11 | F1 新技术 | Dataset-JSON v1.1 vs XPT v5 | TBD | — | — |
| Q12 | D2 CT | CT 版本 + Define-XML + MedDRA | TBD | — | — |
| Q13 | G1 RWD | Observational + ARMCD | TBD | — | — |
| Q14 | I1 跨域 | AE/MH/CE + DS 死亡 | TBD | — | — |
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
| 阈值 | ≥13/17 (77%) |
| **Gate** | TBD |

---

## 主结论 (R1 跑完填)

- v2.6 覆盖 generalization (GF/CP/BE+BS) + AHP 能力对比 smoke v2.1 24/24 PASS 的延展: TBD
- AHP 能力 (Claude 自身训练数据知 SDTMIG, 测 v2.6 system prompt 锚效): TBD
- Q11-Q14 19-file KB 覆盖 supplemental 充分性: TBD
- Q10 SUPPTS 前提纠错能力: TBD
- 首次 v3/v4 题库对 v2.6 的压力观察: TBD
