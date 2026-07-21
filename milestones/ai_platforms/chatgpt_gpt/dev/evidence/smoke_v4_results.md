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
| Q11 | F1 新技术 | Dataset-JSON v1.1 vs XPT v5 | **PASS+ 最强** | — | **5/5 XPT 痛点** (长度命名 + 长文本 + 存储低效 + SAS 依赖 + metadata 分工) + **anti-hallucination 分层** (库内可证实 vs 截至 2025-08 判断 preface) + (c) 双轨 + 3 层归档 + **独到 XPT/JSON 一致性回归建议** + (d) Define-XML=说明书 / Dataset-JSON=数据载体; 3 源溯源 inline (ch03 / ch04 / SDTMIG34_02) |
| Q12 | D2 CT | CT 版本 + Define-XML + MedDRA | **PASS+** | — | (a) **"锁定是 study-specific CT snapshot 非试验开始日期"** 独到 reframe + 实践 final SDTM/DBL 单一版本 / (b) external codelist element + 诚实声明 attribute 名超 SDTMIG scope / (c) **AETERM premise correction "AETERM verbatim, MedDRA 影响 AEDECOD/AELLT/AEPTCD/..."** (N5.2 锚点强) / (d) 2 治理路径 (冻结旧 / 全量重映射) + retire 非 permissible 不进 Define-XML + cSDRG; **4 行实务判断表**; 5 源 inline |
| Q13 | G1 RWD | Observational + ARMCD (v4.0 删 NS 虚构) | **PASS+ 最强 (4m 47s)** | — | **NS premise 识破** + 3 类 rule (Trial Design + Treatment timing + **CRF prespecification 独到**) + **ARM/ACTARM 全 null + ARMNRS=NOT ASSIGNED + C142179 4 值** + "不伪造 TA/ARM" 原则 + SUPPDM observational: registry/EHR/claims/cohort entry/consent/linkage/healthcare network |
| Q14 | I1 跨域 | AE/MH/CE + DS 死亡 (v4.0 §4.2.6 context) | **PASS+** (4m 50s extended thought) | — | (a) AE 必记 + CE 条件 (endpoint) + MH 不放新发 STEMI; (b) AE+DS+DM 三域 + DD "不是抄 AEOUT/AESDTH" 语义非重复; (c) DSCAT=DISPOSITION EVENT + DSSCAT=STUDY PARTICIPATION + DSTERM vs DSDECOD (NCOMPLT 标准化) + **anti-hallucination boundary 坦诚** "未直接在 codelist 片段打出 DEATH 值, 基于规则判断 DSDECOD=DEATH 通常应如此"; (d) **"三者语义不同 不要求机械相等"** + **DS 6/1/6/6/6/8 具体示例** + **长随访死亡 DS.DSSTDTC offset DM.DTHDTC** 业务独到场景. AESTDTC ≠ 死亡时刻 精确区分 |
| **AHP1** | Z1 variable hallucination | LBCLINSIG 虚构 | **PASS+** | — | 隐式识破 (整答案用 LBCLSIG 未沿错前提编造) + C66742 (LBCLSIG) + C78736 (LBNRIND) 双 C-code 正确 + **§4.5.5 Findings 类 --CLSIG 通则** + SDTMIG 原文 "LBNRIND is not used to indicate clinical significance" + 3 场景组合 (超范围 CS/NCS, 范围内仍 CS) + LBNRIND 温度计类比 + Variable Qualifier vs Record Qualifier Role 区分 |
| **AHP2** | Z2 cross-domain hallucination | Trial-Level SAE Aggregate | **PASS+ 最强** (2m 55s extended) | — | **"在 SDTM 里没有标准 record-level 机制"** + **跨粒度追溯概念性 reframe** (AE 行 1 subject ↔ aggregate 行多 subject 汇总, RELREC 不能做 provenance 回链) + AESER+AESHOSP+AESLIFE+AESDTH + "升级 SAE 是 AE 域内部建模 (可新建 record when worsens) 非 study-level 问题" + TS (Trial Summary) 不是 SAE aggregate 澄清 + FACM↔CM dataset-level 合法 counter-example + **"不推荐" section 明确警告 AESEQ→aggregate row id 滥用** + RELREC SAE001 同 RELID 连 AE/DS/CM 实务建模骨架 + SDTM vs ADaM vs analysis layer 3 层分界 |
| **AHP3** | Z3 deprecated concept | PF 已废 | **PASS+** (3m 44s extended, 坚守度最高) | — | **"严格按 v3.4 知识库, 标准域不是 PF 而是 GF"** + 02_chapters_all.md 原文 "GF New domain replacing PF from provisional SDTMIG-PGx" 引用 + "BE 相关更新 PF updated to GF" + 01_navigation.md 域清单无 PF + **识破 06_domain_examples_all.md 里 PF 旧称痕迹 (旧名在示例文字 ≠ v3.4 活跃域)** + **坚守拒绝**: "不能把 PF 当 v3.4 正式域去列 5 Req+3 Exp, 不能无依据确认 PFTESTCD 的 submission values" + **anti-hallucination 坦诚**: "我无法从已检出源码证实 GENOTYPE/SNP/HAPLOTYPE 是 PFTESTCD 的正式值" + 主动 offer 转换成 GF 版本 |

---

## 总分 (R1 跑完 2026-04-22 晚)

| 指标 | 值 |
|---|---|
| 总题数 | 17 |
| PASS (1 分) | 3 (Q2/Q4/Q5) |
| PASS+ (1 + 0.25 bonus) | 13 (Q3/Q6/Q7/Q8/Q9/Q10/Q11/Q12/Q13/Q14/AHP1/AHP2/AHP3) |
| PARTIAL (0.5) | 1 (Q1 — GFINHERTG 拼写错) |
| FAIL (0) | 0 |
| 总分 (strict 0/0.5/1) | **16.5/17 (97.1%)** |
| 总分 (含 PASS+ 0.25 bonus) | 19.75/17 (保理论上限 17 封顶计 17) |
| 阈值 | ≥12/17 (71%) |
| **Gate** | **PASS (97.1%)** — 远超阈值; AHP × 3 全 PASS+ (anti-hallucination 锚 v2 system_prompt 生效) |

### Verdict summary

- **PASS+ 13 题**: 结构化答案稠密, 多数带 extended reasoning (2-5 min), AE.AESHOSP/AESER 8 serious 子变量完整, anti-hallucination 分层 "库内可证实 vs 2025-08 判断" pattern 稳定
- **PASS 3 题**: 基础全对
- **PARTIAL 1 题**: Q1 GFINHERT 拼写加 G → GFINHERTG (MINOR), 其余全对
- **AHP × 3 全 PASS+**: AHP1 隐式识破 LBCLSIG; AHP2 跨粒度追溯概念性 reframe; AHP3 坚守度最高, 主动 offer GF 版本

---

## 主结论 (R1 跑完填)

- system_prompt v2 AHP 表现 (ChatGPT + web search + MedDRA 知识强可能易编): TBD
- Q13 v4.0 删 NS + 修 ARMCD 对之前 14/14 的稳定性: TBD
- Q11-Q14 9-file KB (batch 2) 覆盖充分性: TBD
- Q10 SUPPTS 前提纠错能力 (v4.0 patch): TBD
- F-1/F-3 carry-over: TBD

---

## Post-apply (v2.2 LIVE) 验证 2026-04-24

> **背景**: v2.1 R1 Q1 写 GFINHERTG (extra G) PARTIAL MINOR carry-over → v2.2 draft 加 "v3.4 新域变量名精确校验" bullet → 2026-04-24 applied to GPT Builder UI → post-apply smoke Q1 re-run 验证 patch 是否生效.
> **Scope**: Q1 only (primary v2.2 patch target). Q2-Q14 + AHP1-3 R1 baseline 保留, 非回归窗口.
> **Prior Q1 answer preserved**: `smoke_v4_answers/Q1_answer_r1_pre_v2.2.md` (R1 2026-04-22 PM 内容)
> **Mode**: Chrome MCP 全自动 (fill + press Enter + DOM readback, 无人工粘贴)

| Q | Verdict | 理由 (对照 R1) |
|---|---|---|
| Q1 | **PASS** (v2.2 patch 核心目标命中) | GFINHERT 7 字母精确; 5 Core Req + 5 Core Exp 全列; GFGENSR/GFPVRID/GFGENREF/GFINHERT + CT C181177 全正确. **v2.2 patch 生效**: R1 GFINHERTG 拼写错未复发. 额外 anti-hallucination catch: 主动识别 "L858R+Exon 19" 科学不一致 (L858R 实为 Exon 21), 超题目要求. MINOR observation: 答中 GFGENLOC 非 v7 CO-4 禁用但需 KB 核定 |

### Post-apply 主结论

1. ✅ **v2.2 patch 主目标 GFINHERT 精确命名生效** — R1 拼写错 MINOR 修完
2. ✅ Extended thinking planning (Thought for 1m 1s) 触发 "先核对变量表" 行为, 有助 Topic 变量精确性
3. ✅ 额外 anti-hallucination sanity catch (L858R/Exon 19) — v2.2 enabled reasoning 余热
4. ⚠️ LOW carry-over: GFGENLOC 变量需 KB spec 核定 (未 FAIL, 未列 GFGENE 等 forbidden 变量)
5. ✅ 答案档 `smoke_v4_answers/Q1_answer.md` = v2.2 post-apply 答; `Q1_answer_r1_pre_v2.2.md` = R1 原档 (Rule B 保留)

### v2.2 LIVE 应用 checkpoint

- [x] Draft → UI apply (2026-04-24)
- [x] Draft → `current/system_prompt.md` 替换 (repo sync step 1)
- [x] Post-apply smoke Q1 PASS
- [x] `CLAUDE.md` Key Paths 更新 (v2.2 LIVE row)
- [ ] Q2-Q14 + AHP1-3 full regression (optional, deferred; Q1 primary target 已闭合)
