# ChatGPT GPTs — smoke v3 (N5.3 Full A/B + Generalization Probe) 14 题结果

> **⚠️ SUPERSEDED 2026-04-22 by smoke v4.0** — 本文件记录 smoke v3.1/v3.2 结果, 已于 2026-04-22 PM 因 `ai_platforms/smoke_v3_audit_notes.md` 第 11 种 subagent_type (document-specialist) audit 发现题目前提错作整块 **SUPERSEDED**.
>
> **核心 audit findings**:
> - Q10 (b) SUPPTS 题干 + 判据基于错前提 (SUPPTS 不是 SDTMIG v3.4 定义的 dataset; TS 属 Trial Design, 长 TSVAL 用 TSVAL1-n 内部派生)
> - Q13 (c) "NS (Non-Standard Domain)" 是虚构概念 (WebFetch CDISC Observational RWD v1.0 PDF 2024-02 确认无此概念, 只有既有 NSV variable-level)
> - Q8 LBNRIND 被错列 Non-Ext (实际 C78736 Extensible=Yes); AETERM 被写"用 MedDRA" 错位 (MedDRA 绑 AEDECOD/AELLT/AEHLT 等 --DECOD 变量, AETERM 是 verbatim free text)
> - Q4 FAIL 场景 A PARTIAL 规则过宽 (IS/assumptions.md 2 是 v3.4 显文, 非"版本迁移无显文")
> - Q14 "三域互斥"过强 + 死亡日期"严格相等"过严 (应日级对齐, time offset 需 Reviewers Guide)
>
> **不回溯重评分**: 本文件实际 14/14 或 12/14+2subst 结果 frozen 作历史 trace; Phase 4 跨平台对比 baseline 用 **smoke v4.0** (在 `ai_platforms/smoke_v3_questions_draft.md` 内已 bundled patch + 新增 AHP × 3). 4 平台 (Claude/ChatGPT/Gemini/NotebookLM) smoke v4 R1 重跑.
>
> **本文件作 historical reference only**.

---

> Date: 2026-04-22
> 题库: `ai_platforms/smoke_v3_questions_draft.md` v3.1 (14 题, Q1-Q10 双平台共用 + Q11-Q14 ChatGPT 专属)
> 前置 commit: `7edcb1c` (Phase 4 N5.3 C5.3a 题库设计 + 双 reviewer 审 + v3.1 修)
> 执行者: Bojiang + claude cowork MCP Chrome JS `ClipboardEvent('paste')`
> 合格阈: **≥10/14 (71%)** → Phase 4→5 Gate 开闸候选
> 预期 strict score: 10-13/14 (ChatGPT RAG + batch 2 terminology 优势)
> **实际 strict score**: **14/14 PASS (100%)** ✓

---

## 总体得分

| 维度 | 数值 |
|---|---|
| **Strict PASS** | **14/14 (100%)** |
| 宽判 (含 PARTIAL) | 14/14 (100%) |
| FAIL | 0/14 |
| 阈值 ≥10/14 | **YES, 远超** |
| sanity 3/3 PASS | YES (底座未回归) |
| 04 引用率 (依赖单文件 ≤4 题为佳) | 04 章节多次引用但配合 spec/assumptions/examples 等多源, 非过度依赖, generalization 为真 |
| 思考时长分布 | 1m 43s ~ 4m 55s (中位 ~2m 30s); Q13 最长 4m 55s (KB 0 文档外推断) |

## sanity 3 题 (底座验证, 全 PASS)

| ID | 期望 | 结果 | 文件 |
|---|---|---|---|
| sanity_1 | AESER Core = Exp | ✓ Exp | `dev/evidence/smoke_v3_answers/sanity_1_answer.md` |
| sanity_2 | LBNRIND submission values = HIGH/LOW/NORMAL/ABNORMAL | ✓ 全列出 (C78736) | `dev/evidence/smoke_v3_answers/sanity_2_answer.md` |
| sanity_3 | CMINDC = concomitant medication indication | ✓ 显式命名 | `dev/evidence/smoke_v3_answers/sanity_3_answer.md` |

底座未回归, smoke 进入 Step 3.

## 14 题逐题结果

### Q1 (A1 — GF 域 EGFR 基因变异)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e82f89-64e8-83a7-b934-24851670bc3d
- 完整回答: `dev/evidence/smoke_v3_answers/Q1_answer.md`
- 思考时长: 2m 53s
- 判据对齐: 域 GF ✓ / Req+Exp 字段全 ✓ / GFGENSR / GFPVRID / GFGENREF / GFINHERT 命中
- **Verdict: PASS**
- 归因: Pure generalization (KB 0 直接 GF 文档), 模型由 v3.4 Findings observation class 推出 GF 全字段集

### Q2 (A2 — CP 域, PBMC 流式分析活化 helper T)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83120-7270-83a9-b1cf-73b6af7da6fd
- 完整回答: `dev/evidence/smoke_v3_answers/Q2_answer.md`
- 思考时长: 2m 13s
- 判据对齐: CP 是 Cell Phenotype Findings 域 ✓ / cell type / marker / activation state 多 qualifier 处理
- **Verdict: PASS**
- 归因: Pure generalization

### Q3 (A3 — BE + BS + RELSPEC 生物样本采集→运输→DNA 提取场景)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e832ef-db6c-83a9-82b4-d3bf32f06bbb
- 完整回答: `dev/evidence/smoke_v3_answers/Q3_answer.md`
- 思考时长: 1m 59s
- 判据对齐: BS=Biospecimen / BE=Biospecimen Events / RELSPEC 链接 source-derived sample ✓
- **Verdict: PASS**
- 归因: Pure generalization

### Q4 (B1 — LB vs MB vs IS 三场景域归属)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8340a-8568-83a4-b9d3-d1731338f6ec
- 完整回答: `dev/evidence/smoke_v3_answers/Q4_answer.md`
- 思考时长: 2m 27s
- 判据对齐: LB (临床实验室化学/血液) / MB (微生物菌群) / IS (免疫学/疫苗 Ab/Ag) 三域边界正确
- **Verdict: PASS**

### Q5 (B2 — FA vs QS vs CE 三场景域归属)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8353e-1974-83ab-a8a7-dd4309e79d68
- 完整回答: `dev/evidence/smoke_v3_answers/Q5_answer.md`
- 思考时长: 2m 50s
- 判据对齐: FA=findings about / QS=questionnaire score / CE=clinical event 边界清晰
- **Verdict: PASS**

### Q6 (B3 — PC Timing "服药后 4 小时采血" 5 件套)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83684-dbb8-83a2-b014-32f6dacd5010
- 完整回答: `dev/evidence/smoke_v3_answers/Q6_answer.md`
- 思考时长: 2m 57s
- 判据对齐: PC Timing 五件套 (TPT/TPTNUM/TPTREF/ELTM/RFTDTC) 全对; ISO 8601 duration PT4H 正确写出; planned vs actual 区分 (PCELTM vs PCDTC)
- **Verdict: PASS**

### Q7 (B4 — Partial date ISO 8601 + Imputation, CM 部分日期)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83822-a2b8-83a9-b66d-e130948b5659
- 完整回答: `dev/evidence/smoke_v3_answers/Q7_answer.md`
- 思考时长: 2m 2s
- 判据对齐: partial date 三档 (YYYY-MM / YYYY / null); SDTM vs ADaM 边界明确 (SDTM 原值 vs ADaM derivation); 相对时序变量 CMSTRTPT/CMENRTPT 兜底
- **Verdict: PASS**

### Q8 (B5 — EPOCH Trial Design 与 Subject-level 关系)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83966-48c0-83ab-9060-f923a4d02c36
- 完整回答: `dev/evidence/smoke_v3_answers/Q8_answer.md`
- 思考时长: ~3-4 min
- 判据对齐: TA/TE 计划 vs subject-level 实际, SE 桥梁 ✓; Findings (--DTC) vs Events (--STDTC) 区分; C99079 codelist + Define-XML permissible values 双层; wash-out epoch sponsor 设计粒度判断; 不能 impute EPOCH → null
- **Verdict: PASS**

### Q9 (B6 — AESEV vs AETOXGR vs AESER NCI CTCAE 严重度)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83b36-4f8c-83a7-9ee0-17f82f06bdd1
- 完整回答: `dev/evidence/smoke_v3_answers/Q9_answer.md`
- 思考时长: ~3 min
- 判据对齐: AE 三维 (severity / toxicity grade / seriousness) 完全分清, 不机械等价; CTCAE Grade 5 → AESER=Y 单向关系正确; AESEV 留空策略正确 (不 impute)
- **Verdict: PASS**

### Q10 (H1 — SUPP-- 家族 5 字段综合场景)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83d0b-fad8-83a3-aaae-4114f855615d
- 完整回答: `dev/evidence/smoke_v3_answers/Q10_answer.md`
- 思考时长: 2m 2s
- 判据对齐: QORIG=Req 每条都填; QEVAL=Exp 仅主观时填; SUPPAE subject-level vs TS study-level (诚实指出 v3.4 中 TS 不在 SUPP-- 适用域); 5 件套定位 (STUDYID+RDOMAIN+USUBJID+IDVAR+IDVARVAL); QVAL 200 char SAS V5 限 + QNAM/QNAM1/QNAM2 顺序后缀; QLABEL 保持原标; 8-char 满长替换末字符 (AEACNOTH→AEACNOT1)
- **Verdict: PASS**
- 归因加分: TS 不在 SUPP-- 标准适用域的诚实约束 + 8-char QNAM 替换末字符细节

### Q11 (F1 — Dataset-JSON v1.1 vs SAS XPT v5, ChatGPT 专属)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83e5c-c2e4-83a5-a12c-3b545c698994
- 完整回答: `dev/evidence/smoke_v3_answers/Q11_answer.md`
- 思考时长: 1m 43s
- 判据对齐: 4 痛点 (8-char names / 200 char QVAL / 大文件低效 / SAS 专有依赖) ✓; XPT 仍是 FDA 必需 (诚实声明无法实时核验 2026 状态); 实操 4 步 (开发/归档/提交/验证); Define-XML 元数据合同 vs Dataset-JSON 数据载体互补不替代
- **Verdict: PASS**
- 归因加分: 主动声明 FDA 2026 状态无法实时核验 (没瞎编 binding 接受范围)

### Q12 (D2 — CT 版本锁定 + MedDRA + Define-XML, ChatGPT 专属)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e83fdf-5248-83a8-9f9e-20290097d9b5
- 完整回答: `dev/evidence/smoke_v3_answers/Q12_answer.md`
- 思考时长: 2m 51s
- 判据对齐: study-specific CT snapshot 单一版本贯穿全研究 ✓; Define-XML external codelist element/attributes (诚实标记精确 attribute 名属 Define-XML spec 不属 SDTMIG); **主动纠正用户前提 AETERM = verbatim 不是 MedDRA 编码字段, MedDRA 影响 AEDECOD/AELLT/AEPTCD/AEBODSYS**; MedDRA v25→v27 全研究统一 recode + Define-XML 准确声明字典版本; retire/alias 两路径 (冻结旧版本 / 全量 remap), 禁止混用 old/new term, cSDRG 兜底
- **Verdict: PASS**
- 归因加分: **(c) 主动纠正用户问题中的概念错误 (AETERM ≠ MedDRA 字段) — 教练员级别指正**, 非 trivial 加分项, 体现 SDTM 专家级精确度

### Q13 (G1 — RWD/Observational SDTM 2024 文档, ChatGPT 专属)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e8413d-0950-83a3-b189-e1e05bca9efb
- 完整回答: `dev/evidence/smoke_v3_answers/Q13_answer.md`
- 思考时长: **4m 55s (本批最长)**
- 判据对齐: 3 类失效规则 (Trial Arm / Planned Visit / EPOCH+TAETORD) ✓; ARMCD=null + ARM=null + ACTARM=null + ARMNRS="NOT ASSIGNED" ✓; NS vs SUPPQUAL 5 维度对照表 ✓; SUPPDM 适合/不适合边界 + SC 对照 + 时间轴决定独立域
- **Verdict: PASS** (Constrained generalization)
- 归因加分: **本批最高诚实度** — 直接声明 2024 RWD 文档不在 KB, 外部检索不可用, 标注 "基于 SDTMIG v3.4 推断"; 仍能用原生 trial design / DM ARM / SUPP-- / ch02 custom domain 概念把 4 子问题答完整; (c) 5 维度 NS vs SUPPQUAL 对照表是非 trivial 加分项

### Q14 (I1 — AE+CE+MH 同事件 + DS 死亡 + 跨域时间对齐, ChatGPT 专属)

- 对话 URL: https://chatgpt.com/g/g-69e635b99e848191a2818cd8e8e7e9cc-sdtm-expert/c/69e84368-2684-83a9-8583-abef0193a541
- 完整回答: `dev/evidence/smoke_v3_answers/Q14_answer.md`
- 思考时长: 3m 3s
- 判据对齐: AE/MH/CE 三域边界完整 (AE 默认主域 / MH 仅研究前 / CE 仅方案 endpoint); 死亡跨 AE+DS+DM 三域协同 + AESDTH=Y + AEOUT=FATAL + DTHFL+DTHDTC; DSCAT=DISPOSITION EVENT + DSDECOD=DEATH + DSSCAT=STUDY PARTICIPATION; 三变量语义全对 + DS.DSSTDTC = DM.DTHDTC 对齐 + AE.AESTDTC 不必等于 DTHDTC
- **Verdict: PASS**
- 归因加分: **情形 A vs 情形 B 双场景建模** (恢复后另起致死事件 vs 持续恶化致死) + ISO 8601 跨域精度一致性原则 + AESHOSP=Y 在 STEMI 例子明示

## 维度小计

| 维度 | 题号 | 结果 |
|---|---|---|
| Q1-Q3 (v3.4 新域 A1/A2/A3) | Q1 (GF) / Q2 (CP) / Q3 (BE+BS+RELSPEC) | **3/3 PASS** |
| Q4-Q5 (域边界 B1/B2) | Q4 (LB/MB/IS) / Q5 (FA/QS/CE) | **2/2 PASS** |
| Q6-Q7 (Timing C1/C2) | Q6 (PC Timing 5 件套) / Q7 (Partial date) | **2/2 PASS** |
| Q8 (Trial Design D1) | Q8 (EPOCH 与 Subject-level) | **1/1 PASS** |
| Q9-Q10 (CTCAE + SUPP H1) | Q9 (AESEV/AETOXGR/AESER) / Q10 (SUPP-- 5 字段) | **2/2 PASS** |
| Q11-Q14 (ChatGPT 专属 F1/G1/D2/I1) | Q11 (Dataset-JSON) / Q12 (CT+MedDRA+Define-XML) / Q13 (RWD) / Q14 (AE+CE+MH+DS 死亡) | **4/4 PASS** |

## 03 generalization 真实性自查

- 题库 v3.1 设计原则: 禁 filename 提示 / 禁位置提示 / 禁字典查 / 业务场景驱动
- ChatGPT 回答源溯源命中分布:
  - ch01_introduction.md / ch02_fundamentals.md / ch04_general_assumptions.md / ch08_relationships.md (general 章节, 多题命中)
  - 各域 spec.md / assumptions.md / examples.md (按题对应域)
  - terminology/ 命中较少 (符合 generalization 期望: 不靠字典查)
- 单文件 04 依赖 ≤4 题 (Q4/Q7/Q8/Q14 配合多源, 非过度依赖); 04 引用率自查通过
- 非 trivial 加分项:
  - Q10: TS 不在 SUPP-- 适用域的诚实约束 / 8-char QNAM 末字符替换细节
  - Q11: 主动声明 FDA 2026 状态无法实时核验
  - Q12: **主动纠正用户前提 AETERM ≠ MedDRA 字段** (本批最高加分)
  - Q13: **本批最高诚实度** (KB 0 文档主动声明 + 仍用原生概念答完 4 子问题)
  - Q14: 双场景建模 + ISO 8601 跨域精度一致性

## 结论

ChatGPT GPT "SDTM Expert" smoke v3 14 题 **strict score 14/14 (100%) PASS**, 远超合格阈 ≥10/14 (71%).

- **Generalization 真实**: KB 0 直接覆盖的 v3.4 新域 (Q1 GF / Q2 CP / Q3 BE+BS) + 2024+ 新议题 (Q11 Dataset-JSON / Q13 RWD/NS) 全 PASS, 非靠预 cook
- **诚实约束**: Q11/Q12/Q13 多题主动声明知识边界 (无法核验 / 不属 SDTMIG / KB 外文档), 没瞎编
- **教练员级别**: Q12 主动纠正用户错误前提 (AETERM verbatim vs AEDECOD MedDRA 编码) 是非 trivial 加分项, 一般 LLM 会顺着错误前提答
- **复杂跨域协同**: Q14 AE+CE+MH+DS+DM 五域 + ISO 8601 跨域时间对齐双场景建模

**Phase 4→5 Gate: 推荐 OPEN**, 候选 N5.3 答题 reviewer (第 22 种 subagent_type) 确认.
