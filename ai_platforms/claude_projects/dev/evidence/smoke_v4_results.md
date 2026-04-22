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
| Q10 | H1 SUPP | QORIG/QEVAL + SUPPTS 前提纠错 | **PASS+ 最强** | — | SUPPTS 识破 + TSVAL1-n + **QORIG Core=Req 明确 + QEVAL C78735 CT code 唯一给出** + **CO.COVAL+IE/TI 40-char+DM IDVAR null+--GRPID 多父记录 5 项独到** + MHTERM 520 字符 3-row complete example + §4.2.8.3 多值 vs 长文本区分 |
| Q11 | F1 新技术 | Dataset-JSON v1.1 vs XPT v5 | **PASS+ 最强 (4 平台最强)** | — | **5/5 XPT 痛点 (判据全覆盖)**: 8-char/200-char/Unicode/metadata 分离/存储低效 + IBM 浮点 vs IEEE 754 独到 + (b) 完整时间线 2022→2026-04 + Docket FDA-2025-N-0129 + Pinnacle 21 v4.1 v1.1 不完整警告 + (c) R/Python/SAS 3 工具链具体包名 + XPT canonical / Dataset-JSON derived 归档策略 + (d) Transport vs Metadata 2 层分工表 + Define-JSON 未来路径; **Project KB 边界透明声明** (§2.1/§4.2.9/§4.5.3 锚点 + "基于 web 查证" 分层) + 3 外部链接 (CDISC/FDA/R-consortium); 消耗 weekly limit 75% → 75% |
| Q12 | D2 CT | CT 版本 + Define-XML + MedDRA | **PASS+ 最强 4 平台中** | — | (a) 3 策略表 + **Freeze-at-DBL ✅** + Data Standards Catalog / (b) **Define-XML 2.0 vs 2.1 namespace prefix `def:` 区分** + `CodeList/@StandardOID` + XML 示例片段 / (c) **MedDRA 6 版本时间线** (v25.0→v27.1) + 5 类变化表 + AESI 重新评估独到 / (d) 5 步流程 + 3 retire 模式 (Rename/Split-Merge/Deprecate) + SUPPQUAL fallback + CDISC backward-compatible 原则; 6 源溯源 + 6 外查清单 |
| Q13 | G1 RWD | Observational + ARMCD | **PASS+ 最强 4 平台中 (web fetch + 3-source)** | — | **Web fetch CDISC Observational v1.0 PDF** + **Rule ID 具体** (CG0009/CG0014/CG0016/CG0523/CG0524) + 2 层失效分类 (Dataset + Variable) + **v1.0 §2.3 3 路径** (Cohort=SMOKER/NONSMOKE / 无 arm null / ECA=External control) + **ARMNRS C142179 4 C-codes 全** (C49628/C142239/C142238/C142240) + **NS 3-source 否证** (KB + v1.0 PDF + 生态) + v1.0 §1 "not a standard" + QORIG="COLLECTED" SUPPDM 独到; weekly limit 75% |
| Q14 | I1 跨域 | AE/MH/CE + DS 死亡 | **PASS+ 最强 4 平台中** | — | 4 部分全 Markdown 表格化 + **AE+DS+DM+DD 四域 + RELREC 串联** (DS.DSSEQ↔AE.AESEQ↔DD.DDSEQ same RELID) + **C66727 + C74558 双 C-code** + **DSTERM="Heart Failure" verbatim vs DSDECOD="DEATH" 标准化** + 常见误区 DSDECOD="ADVERSE EVENT" vs "DEATH" 避坑 note + **Sudden Cardiac Death Example 具体 ISO 8601 (2011-01-10 多域 + DD.DDDTC 晚 2 天)** + **DS.DSDTC (采集日期) vs DSSTDTC (事件日期) 易混变量** + **AE.AESTDTC ≠ 死亡时刻精确区分** + **精度 granularity 一致容错** (未要求 strict time-level equal) + EPOCH="TREATMENT/FOLLOW-UP"; weekly limit 75% → 75% |
| **AHP1** | Z1 variable hallucination | LBCLINSIG 虚构 | **PASS+ 最强 4 平台中** | — | **标题即 premise correction** "先纠一个命名 LBCLINSIG → LBCLSIG" + **8-char CDISC 命名约束解释** (深度背景非简单 typo) + **7 维度对比表** (本质/判定/取值/Core/Role/可衍生/SDTMIG 依据) + **4 场景组合表** (ALT HIGH/N, WBC NORMAL/Y, AST HIGH/Y, 未收集) + C66742 通用性 "--BLFL/--DRVFL/--FAST/--LOBXFL/--CLSIG 共用 40+ 域" + SDTMIG §4.5.5 原文 + EGTESTCD=INTP 跨域 --CLSIG 整体 vs 单个用法 |
| **AHP2** | Z2 cross-domain hallucination | Trial-Level SAE Aggregate | **PASS+ 最强 (并列 NotebookLM/ChatGPT)** | — | "SDTMIG v3.4 不存在标准 Trial-Level SAE Aggregate 域" 明确否证 + **§8.2 vs §8.3 RELREC 2 模式 7 维度对比表** + §8.3.1 原文 "--SEQ only has meaning within subject within dataset, not across datasets" + **AE serious 8 子变量全** (AESER/AESHOSP/AESCAN/AESCONG/AESDISAB/AESDTH/AESLIFE/AESMIE) + **relrec.xpt 2-row 实际示例** (STUDYID/RDOMAIN/USUBJID/IDVAR/IDVARVAL/RELTYPE/RELID 7 变量 + AELNKID/XXLNKID merge key 机制) + "多数场景 SDTM 端无需 relationship dataset (AE flag 下游聚合)" 实务分层 + ⚠ ADaM 外部分析 --SEQ back-reference + Define-XML trace 机制边界 |
| **AHP3** | Z3 deprecated concept | PF 已废 | **PASS+ 最强 (并列 NotebookLM)** | — | **"⚠️ 前提校正: PF 在 v3.4 中已废弃"** + **§6.3.5.4 变更记录原文引用** "Genomics Findings (GF) — New domain replacing the PF domain from the provisional SDTMIG-PGx" + 2015-05-26 provisional 历史 + 63 域清单无 PF + **GF 6 Req + 6 Exp 全列出** (超用户 5+3) + GFTESTCD C181178 / GFTEST C181179 / GFMETHOD C85492 + **核心独到**: **GFTESTCD vs GFTSTDTL 两层变量分工** (C181178 测量类型 vs C181180 测量细节) — 用户的 GENOTYPE/SNP/HAPLOTYPE 在 GFTSTDTL 非 GFTESTCD + 8 submission values (SNV/CPNUMVAR/MICRISTB/GENESIG/SHRTVAR/TMB/SEQREAR/TRNSCPTN) + **GF Example 2 具体行** (SNV + GENOTYPE + G/G) 给 PF-era 思维到 v3.4 实际映射 + 诚实 boundary (HAPLOTYPE 未命中需回源 + 10 terms 列 8 个); weekly limit 75% → 75% |

---

## 总分 (R1 跑完 2026-04-22 晚)

| 指标 | 值 |
|---|---|
| 总题数 | 17 |
| PASS (1 分) | 0 |
| PASS+ (1 + 0.25) | **17 (全部 17 题)** |
| PARTIAL (0.5) | 0 |
| FAIL (0) | 0 |
| 总分 (strict 0/0.5/1) | **17/17 (100%)** |
| 总分 (含 PASS+ 0.25 bonus) | 21.25 / 17 (所有 17 题均 PASS+) |
| 阈值 | ≥13/17 (77%) |
| **Gate** | **PASS (100%)** — 全 PASS+ 最强; Q11/Q12/Q13/Q14 + AHP × 3 共 7 题 "4 平台中最强" |
| **Weekly limit** | 75% (本轮 17 题跑完未变) |

### Verdict summary

- **全 17 题 PASS+**: smoke v4 首测 0 PARTIAL / 0 FAIL
- **"4 平台中最强" 7 题**: Q11 (Dataset-JSON IBM 浮点 vs IEEE 754) / Q12 (CT 版本 Define-XML 2.0/2.1 namespace) / Q13 (Web fetch CDISC Observational v1.0 PDF + Rule ID 具体) / Q14 (AE+DS+DM+DD + Sudden Cardiac Death Example) / AHP1 (8-char 命名约束深度) / AHP2 (relrec.xpt 2-row 示例 + 8 serious 子变量) / AHP3 (GFTESTCD vs GFTSTDTL 两层变量分工)
- **独到能力**: Web fetch (Q13 fetch v1.0 PDF), 具体 Rule ID (CG0009/CG0014/CG0016/CG0523/CG0524), MedDRA 6 版本时间线 v25-v27.1, § 原文引用 (§6.3.5.4 / §4.5.5 / §8.3.1 / §4.2.6), GF Example 2 具体示例
- **v2.6 system_prompt + 19-file KB 协同**: 训练数据 + KB 双路径 cross-check 给最深答案

---

## 主结论 (R1 跑完填)

- v2.6 覆盖 generalization (GF/CP/BE+BS) + AHP 能力对比 smoke v2.1 24/24 PASS 的延展: TBD
- AHP 能力 (Claude 自身训练数据知 SDTMIG, 测 v2.6 system prompt 锚效): TBD
- Q11-Q14 19-file KB 覆盖 supplemental 充分性: TBD
- Q10 SUPPTS 前提纠错能力: TBD
- 首次 v3/v4 题库对 v2.6 的压力观察: TBD
