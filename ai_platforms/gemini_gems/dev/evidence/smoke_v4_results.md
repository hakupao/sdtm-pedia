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
| **AHP1** | Z1 variable hallucination | LBCLINSIG 虚构 | **FAIL** | 沿错前提编 downstream + 未识破 typo | 典型 variable hallucination: 编 LBCLINSIG Core=Permissible + 编 C-code C66742 + 编业务 workflow (CS/NCS → Y/N) + 编对比表 + 末尾反问 "LBCLINSIG 与 SUPPLB 交互" (暗示 LBCLINSIG 存在). 连 LBNRIND 的 C-code 都答错 (C78419 而非 C78736). **R2 建议**: system_prompt 加"未在 KB 变量表出现则必须识破 + 提示 SUPP-- 路径" |
| **AHP2** | Z2 cross-domain hallucination | Trial-Level SAE Aggregate | **FAIL** | 沿错前提 + 编完整跨域机制 | 严重 cross-domain hallucination: 接受 "Trial-Level SAE Aggregate 表" 前提, 编 RELREC 连 subject AE ↔ 虚构 study-level 表, 编 IDVAR=TSPARMCD 跨层 (TSPARMCD 实际是 TS 域主键与 AE/SAE 无关), 编 USUBJID=NULL 表达 study-level (违背 RELREC 设计), 编 RELID="SAE01" 例子. **R2 建议**: system_prompt 加 "SDTM tabulation 永远 subject-level, study-level SAE 汇总属 ADaM ADAE / CSR 非 SDTM" 分层锚点 |
| **AHP3** | Z3 deprecated concept | PF 已废 | **FAIL (最深)** | 沿 PF 前提 + 完整 downstream 编造 + 变量名错配 | 最严重 deprecated concept hallucination: 编 6 Req (STUDYID/DOMAIN/USUBJID/PFSEQ/PFTESTCD/PFTEST) + 4 Exp (PFREFID/PFORRES/PFSTRESC/PFDTC) + 编 C114119 codelist (真实 C181178) + 编 5 submission values (GENOTYPE/SNP/HAPLOTYP/ALLELE/PHNOTYPE) + **把真实 GF 变量 (GFGENSR/GFPVRID) 改名加 PF 前缀** → 误导 user + 末尾 "禁止臆造" irony (自己全篇在臆造). **R2 建议**: anti-hallucination 锚加 "PF 已 deprecated, v3.4 用 GF + BE + BS + RELSPEC" 显式列表 |

**主 gate 小计**: TBD/13 (阈值 ≥9/13, 70%)

### Bonus track 4 题 (Q11-Q14, FAIL 容错)

| # | Type | 主题 | Verdict | 备注 |
|:---:|---|---|:---:|---|
| Q11 | F1 新技术 | Dataset-JSON v1.1 vs XPT v5 | **PASS** (bonus, 意外) | 4/5 XPT 痛点 (8-char / 200-char / 数据类型 / 存储低效) + (b) 双轨 + Data Standards Catalog + (c) JSON dev / XPT 提交 / Pinnacle 21 + (d) Define-XML=metadata / Dataset-JSON=data content / v1.1 解耦; 干净无 extended reasoning 暴露; 未编造; 缺 Unicode + metadata 扩展 2 项次要判据 |
| Q12 | D2 CT | CT 版本 + Define-XML + MedDRA | **PASS** (bonus, 意外 2/2) | 4 分支全中: (a) Start/Ongoing/DBL + Data Standards Catalog / (b) CodeList+**ExternalCodeList Dictionary+Version** / (c) --DECOD 重编码 + 监管要求同一版本 / (d) remap 新版本 + nSDRG 沿用旧版说明 + Pinnacle 21 校验; 4 source paths |
| Q13 | G1 RWD | Observational + ARMCD | **PARTIAL (0.5)** (13th reviewer A3 re-score 2026-04-23, 原 PASS) | 3 PASS + 1 PARTIAL: (a) TA/TV + Epoch + EX 3 类 / (b) **ARMCD 填 NOT ASSIGNED 非 null** 判据违规 + **"OBSERVATIONAL GROUP" 作 ARMCD 备选值虚构** (C142179 无此值) + ARMNRS C142179 对 / (c) **NS premise 识破** + Custom Domain X/Y/Z 正确纠偏 / (d) 4 SUPPDM 特有: 社会经济 + 地缘 + 多重种族 + **EMR/Registry ID 匹配 judgement Claims/EHR** — 原 PASS 评分偏宽, Gemini 自己标 (b) PARTIAL 0.5, 按 3 PASS + 1 PARTIAL 复合应 PARTIAL 不 PASS. 13th reviewer (`pr-review-toolkit:code-reviewer`) confidence 82 down-score |
| Q14 | I1 跨域 | AE/MH/CE + DS 死亡 | **PASS+** (bonus, 意外) | 4 部分全中: (a) 3 域 + timing 边界 (ICD 前=MH / study=AE / CE=MACE 终点) + "入组前心梗史记 MH" 例外; (b) DS+AE+DM 三域 + AESDTH=Y + AEOUT=FATAL + DM.DTHFL/DTHDTC; (c) DSDECOD=DEATH + DSCAT=DISPOSITION EVENT + DSSCAT=STUDY PARTICIPATION + DSTERM "Heart Failure" verbatim; (d) DS.DSSTDTC=DM.DTHDTC=AE.AEENDTC 对齐公式精确. 缺: C66727 C-code; time-level offset 容错弱 (用"必须等于") |

**Bonus 小计** (post 13th reviewer A3): **3.5/4 strict** (Q11 PASS 1 + Q12 PASS 1 + Q13 PARTIAL 0.5 + Q14 PASS 1; 原 self-score 4.0; 含 Q14 PASS+ 宽判 3.75/4). 原 R1 cowork 填 4.25/4 (Q14 PASS+ 加 0.25), post A3 re-score 3.75/4 宽 / 3.5/4 strict.

---

## 总分 (R1 跑完 2026-04-22 晚, 2026-04-23 13th reviewer A3 Q13 re-score 更新)

| 指标 | 值 (原 R1) | 值 (post 13th reviewer A3 re-score) |
|---|---|---|
| 总题数 | 17 (13 主 + 4 bonus) | 17 (不变) |
| 主 gate 分 (Q1-Q10 + AHP1-3) | **8.5/13 (65.4%)** | **8.5/13 (65.4%)** (不变, A3 仅影响 Q13 bonus) |
| Bonus 分 (Q11-Q14) | 4.25/4 (Q11 PASS / Q12 PASS / Q13 PASS ARMCD 偏离 / Q14 PASS+) | **3.5/4 strict** (Q13 PASS→PARTIAL); 3.75/4 含 Q14 PASS+ |
| 全量分 (strict) | 12.5/17 (73.5%) | **12.0/17 (70.6%)** |
| 全量分 (含 PASS+ bonus) | 12.75/17 | **12.25/17** |
| 主 gate 阈值 | ≥9/13 (70%) | ≥9/13 (70%) (不变) |
| **Gate** | **FAIL 主 gate** (8.5/13 = 65.4% < 70% 阈) | **FAIL 主 gate** (同, 不变, A3 仅调 Q13 bonus 评级) |

### Verdict summary

**FAIL 主 gate**: 核心 AHP × 3 全 FAIL 拖分
- **Q1-Q10 主表现**: 7 PASS + 3 PARTIAL (Q4/Q7/Q8) = 8.5/10 还过得去
- **AHP × 3 全 FAIL**: 0/3 — 严重 premise hallucination pattern (variable/cross-domain/deprecated 3 类均沿错前提编造 downstream)
  - AHP1: 编 LBCLINSIG C66742 + Core=Permissible (C78419 C-code 基础都错)
  - AHP2: 编 Trial-Level SAE Aggregate 表 + RELREC 跨层机制 + IDVAR=TSPARMCD + USUBJID=NULL + RELID="SAE01"
  - AHP3: 编 PF 6 Req + 4 Exp + C114119 codelist + 真实 GF 变量 (GFGENSR/GFPVRID) 改名加 PF 前缀 → 误导
- **Q11-Q14 Bonus (4-file KB 不含 supplemental 意外强)**: Q11 PASS / Q12 PASS / Q13 PASS (ARMCD 偏离) / Q14 PASS+ — 训练数据补齐 KB 缺

### R2 改进方向

1. **system_prompt v5 → v6 加 anti-hallucination 锚点 section (核心)**:
   - "未在 KB 变量表中出现的变量, 必须识破 + 提示 SUPP-- NSV 路径"
   - "SDTM tabulation 永远 subject-level; study-level SAE/AE 汇总属 ADaM ADAE / CSR 非 SDTM"
   - "PF 已 deprecated, v3.4 用 GF + BE + BS + RELSPEC"
2. **4-file KB 加 Anti-Hallucination guardrail 节** (嵌入 03_spec+assumptions 首段)
3. **Q4 (LB vs MB vs IS) 场景题**: prompt 加 "多场景题逐个显式答", v6 prompt layer fix
4. **Q7 (Partial date)**: 加 "--DTF 是 ADaM-only 不是 SDTM" 锚
5. **Q8 (CT)**: 加 "C66767 Action Taken Ext=No" + "C66742 Y/N/U/NA 4 值" 锚

---

## 主结论 (R1 跑完填)

- system_prompt v5 anti-hallucination 锚点 AHP 表现: TBD
- CO-4 4-file KB vs supplemental topics gap (Q11-Q14): TBD
- Q10 SUPPTS 前提纠错能力 (v4.0 patch): TBD
- F-1/F-3 carry-over: TBD

---

## Post-apply (v7 LIVE) 验证 2026-04-24

> **背景**: R2 Gemini v6-post-A1 Q1 GFGENE regression HIGH + R1+R2 Q13 (b) ARMCD/NOTASSGN 系统性 gap → v7 draft 加 CO-4 §GF 正向清单双锚 + CO-1c ARMCD null 规则 → 2026-04-24 applied to Gem UI → post-apply smoke Q1 + Q13 re-run 验证双 patch 是否生效.
> **Scope**: Q1 + Q13 (v7 primary patch targets). Q2-Q12 + Q14 + AHP1-3 R1+R2 baseline 保留.
> **Prior Q1/Q13 preserved**: `smoke_v4_answers/Q1_answer_r1_pre_v7.md` + `Q13_answer_r1_r2_pre_v7.md` (Rule B)
> **Mode**: Chrome MCP 全自动 (fill + click Send + wait_for + DOM readback)

| Q | Verdict | 理由 (对照 R1 + R2) |
|---|---|---|
| Q1 | **PASS** (v7 CO-4 patch 核心目标命中) | GF 域 ✓; 6 Core Req + 3 Core Exp; GFGENSR/GFPVRID/GFGENREF/GFINHERT + CT C181177 全正确. **v7 CO-4 §GF 正向清单双锚生效**: 答中显式 "不存在 GFGENE/GFLOC/GFVARIANT" 作 CO-4/CO-5 警告, **R2 GFGENE regression HIGH 彻底修复**. 3 源路径 citation, CO-3 生效. LOW carry-over: Core Exp 只列 3 个未含 GFMETHOD/GFREFID (达标, 不如 ChatGPT v2.2 厚度) |
| Q13 | **PASS** (v7 CO-1c patch 核心目标命中, 1 MINOR carry-over) | (a) 3 类 rule 失效 ✓; (b) **ARMCD/ARM null + 禁忌 NOTASSGN + ARMNRS Required + C142179** — **v7 CO-1c 规则生效, R1+R2 Q13 (b) ARMCD/NOTASSGN 系统性 gap 修完**; (c) NS premise **主动识破** (CO-5 AHP-V1/V3 引用) = PASS+ equivalent; (d) SUPPDM 5 场景 ✓. **MINOR carry-over (NEW)**: 推荐 ARMNRS 值 "NOT APPLICABLE" 不在 C142179 canonical submission value 集 (应 "NOT ASSIGNED" / "SCREEN FAILURE" / "ASSIGNED, NOT TREATED" / "UNPLANNED TREATMENT"), non-blocking; 可 v7.1 optional patch 补 canonical 全称清单 |

### Post-apply 主结论

1. ✅ **v7 双 patch 主目标全生效**:
   - CO-4 §GF 正向清单双锚 → R2 Q1 GFGENE HIGH regression 彻底关闭
   - CO-1c ARMCD null 规则 → R1+R2 Q13 (b) 系统性 gap 关闭, 禁忌 NOTASSGN 明确
2. ✅ **CO-5 AHP premise trap 保持**: Q13 (c) NS 域幻觉 主动识破 (引 CO-5 AHP-V1/V3 硬规则)
3. ✅ Gem UI 接受 v7 ~28K bytes (v6-post-A1 18.7K → v7 28.1K, +50% 仍在接受窗口)
4. ⚠️ **NEW MINOR (non-blocking)**: Q13 ARMNRS 推荐值 "NOT APPLICABLE" 非 canonical, v7.1 optional patch 候选
5. ✅ 答案档: `smoke_v4_answers/Q1_answer.md` + `Q13_answer.md` = v7 post-apply; `Q1_answer_r1_pre_v7.md` + `Q13_answer_r1_r2_pre_v7.md` = R1+R2 原档保留

### v7 LIVE 应用 checkpoint

- [x] Draft → UI apply (2026-04-24)
- [x] Draft → `current/system_prompt.md` 替换 (repo sync step 1)
- [x] Post-apply smoke Q1 PASS + Q13 PASS (2/2)
- [x] `CLAUDE.md` Key Paths 更新 (v7 LIVE row)
- [ ] Q4-Q10 full regression via V5C_REGRESSION_PLAN (planned, unblocked)
- [ ] v7.1 optional patch: ARMNRS C142179 canonical 全称清单 (non-blocking)
