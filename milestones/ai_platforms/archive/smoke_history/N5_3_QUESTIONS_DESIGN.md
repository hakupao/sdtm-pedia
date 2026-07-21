# N5.3 Smoke v3 题库设计文档 (Generalization Probe)

> **建立日期**: 2026-04-21
> **背景**: N5.2 PASS (ChatGPT 10/10 + Gemini 9/10 + Q3 补测 PASS = 等价 10/10), Phase 4 Gate CONFIRM
> **N5.3 任务**: Full A/B 矩阵 (ChatGPT 14 题 + Gemini 10 题), 作为 Phase 4→5 Gate 的 PASS 比 ≥ 90% 实证
> **用户约束 (2026-04-21)**: (1) **题源联网** 不靠 Claude 训练记忆 (2) **不参考 04_business_scenarios** scenario 预设, 防作弊嫌疑
> **对应 _progress.json**: Gemini `n5_3_design_open_question_raised_by_user_2026_04_21`

---

## §1. 为什么要 generalization probe

### 1.1 用户在 N5.2 session 末提出的疑虑

用户 04 业务弹药包 (`ai_platforms/gemini_gems/current/uploads/04_business_scenarios_and_cross_domain.md`) 已预设 26 scenarios (§1.1-§1.25) + 21 pitfalls (§2.1-§2.21) + 12 深化章节 (§12-§24) 覆盖 Trial Design / IE / RECIST / AG / PR / 影像 / Events / SUPPQUAL / Specialty 等.

**smoke v2/v2.1 10 题完全落入 04 §1.1-§1.10 预设 scenario 范围** (每题甚至有 §1.X 对应标注). 双平台 Q 都 PASS 不等于模型真会 SDTM, **只证模型会背 04 pre-cook 答案**.

### 1.2 Generalization probe 要测的是什么

> 题目不在 04 预设里, 但 **01/02/03 (navigation + spec + examples) 里有支撑原材料**, 测 Gemini 1M 窗口能否利用"非预压缩"的原始 knowledge, 非单纯背 04.

**ChatGPT 侧同步测**: ChatGPT 有 RAG + 5 文件 batch 2 (assumptions + examples + terminology 3 档), 不像 Gemini 靠 04 弹药包. generalization probe 对 ChatGPT 同样是 "RAG 在 04 外场景是否依然能路由".

---

## §2. 题源策略 (联网取材, 非 Claude 记忆)

### 2.1 禁区 (04 已覆盖范围, grep 验)

| 04 章节 | 已覆盖主题 | N5.3 禁命中 |
|---------|----------|-----------|
| §1.1 CM 多药 | smoke Q1 | CM 同题或变体 |
| §1.2 AE SAE 住院 | smoke Q2 | AESER 子变量填写基础 |
| §1.3 LB HbA1c | smoke Q3 | LBNRIND 基础映射 |
| §1.4 AESEV CTCAE | smoke Q4 | AESEV 档位 + CTCAE 映射 |
| §1.5 PK LLOQ | smoke Q5 | PK PCORRES/PCSTRESN |
| §1.6 DM ARM | smoke Q6 | ARM/ARMCD/ACTARM 基础 |
| §1.7 MH+CM | smoke Q7 | 高血压+降压药拆分 |
| §1.8 AESTDTC ISO | smoke Q8 | ISO 8601 精度 + Day 1 |
| §1.9 SUPPAE QNAM | smoke Q9 | SUPPAE 基础用法 |
| §1.10 RELREC vs SUPP | smoke Q10 | RELREC 基础选择 |
| §1.11-§1.25 | EX/EC, Obs Class, RFSTDTC, NULL/UK, VS/EG/EX/DS/TA-TE-TV, LBBLFL, CO, RACE, QS vs FA, DV, 长文本, FA, SV, PP, BE+MB 基础 | 避开这些基础题 |
| §12 深化 | TS/TI/TA/TE/TM/TV 基础 | 避开基础 Trial Design |
| §13 IE | 基础 IE | 避开基础 IE |
| §14 RECIST | TU/TR/RS/BOR 基础 | 避开基础 RECIST |
| §15-§17 | AG / PR / 影像 | 避开基础 PR/AG |
| §18-§19 | Events class / SUPPQUAL 深化 | 避开 MH vs CE 基础 |
| §20-§24 | 命名 / EDC专项 / Specialty | 避开基础命名 |

**每题成稿后强制 grep 04**, 若命中 04 某 §X 直接答 >50% → 换题.

### 2.2 允许区 (04 未深入或未覆盖, 01/02/03 有原材料)

| 类型 | 方向 | 联网源 |
|------|------|--------|
| **A. SDTMIG v3.4 新增域** | GF (Genomics Findings), CP (Cell Phenotype), BE/BS/RELSPEC 三件套 (from SDTMIG-PGx v1.0), IS scope 变化, DI (Device Identifiers) | CDISC SDTMIG v3.4 official + PhUSE DS10 "What's New in SDTMIG v3.4 and SDTM v2.0" |
| **B. 跨域 scope 边界** (04 各自浅提, 未对比) | LB vs MB vs IS (LDH / 病原菌 / 抗药抗体); PR vs CM vs EX (介入 vs 伴随 vs 实验用药); FA vs QS vs CE (病人报告 vs 问卷 vs 临床事件) | CDISC LB/MB/IS scope change webinar + PharmaSUG papers |
| **C. Timing 深化** (04 基础未深) | --TPT/--TPTREF/--STTPT/--ENTPT 四件套; Partial date 约定 + imputation; VISITNUM vs VISIT vs SVSTDTC | SDTMIG v3.4 §4.1.4 Timing Variables |
| **D. Controlled Terminology 深化** | Extensible vs Non-Extensible (AETERM MedDRA 的 extensible 含义 vs LBTESTCD 的 CT); CT 版本锁定 submission; C66735 Route of Admin 非标值处理 | NCI EVS Browser + CDISC CT submission guidance |
| **E. Pinnacle 21 / Validation** (04 0 覆盖) | 常见 rule 违反 (SD0001/SD0002/SD1001 等) + 对应 SDTM 修正; FDA BIMO 审 SDTM 常 finding | Pinnacle 21 Certara blog + PharmaSUG 2025 SI-180/SI-224 validation papers |
| **F. Dataset-JSON** (04 0 覆盖, 2025 新) | 2025 fall FDA 首次接受 Dataset-JSON; XPT v5 vs JSON 格式选择 | CDISC Dataset-JSON v1.1 + R Consortium FDA pilot |
| **G. RWD/Observational** (04 0 覆盖) | RWD 下哪些 conformance rule 失效; SUPPDM 对 observational 补偿; IE/SE/TV 可选性 | CDISC "Considerations for SDTM Implementation in Observational Studies and RWD v1.0" |
| **H. SUPP 深化** (04 基础未深) | QORIG / QEVAL / QLABEL 三字段何时填何时不填; SUPPTS (research-level) vs SUPP-- (subject-level); SUPP-- RDOMAIN + IDVAR 联动 | SDTMIG v3.4 §8.4 + PharmaSUG |

### 2.3 联网源优先级

1. **CDISC 官方** (标准源): SDTMIG v3.4 HTML, CT quarterly release, webinar transcripts, official guidance documents (e.g., Observational Studies doc)
2. **PhUSE / PharmaSUG 2023-2025 论文**: DS10 (v3.4 新东西), DS-114 (Subject Visits), SI-180 / SI-224 (validation), DS-134 (v3.4 implementation), DV-181 (data quality check)
3. **NCI EVS Browser**: CT code 查询 + codelist 范围
4. **Pinnacle 21 / Certara blog**: 实战 validation rule
5. **不采信**: Stack Overflow / Reddit / 博客非官方 (generalization 要真实 SDTM 用户问题, 但答案必须锚到标准源)

---

## §3. 题型分布 (ChatGPT 14 题 / Gemini 10 题 / 共用 10 + ChatGPT 专属 4)

### 3.1 题型矩阵

| # | 类型 | 题数 | ChatGPT 专属 / 双平台共用 | 难度 |
|---|------|:---:|:---:|:---:|
| **A1** | GF (Genomics Findings) 新域变量 + 与 LB 边界 | 1 | 共用 | 中 |
| **A2** | CP (Cell Phenotype) + 流式细胞场景 | 1 | 共用 | 中 |
| **A3** | BE/BS/RELSPEC 三件套协同 | 1 | 共用 | 中-难 |
| **B1** | LB vs MB vs IS 边界 (LDH / 病原菌 / 抗药抗体) | 1 | 共用 | 难 |
| **B2** | FA vs QS vs CE (病人报告 vs 问卷 vs 临床事件) | 1 | 共用 | 中-难 |
| **C1** | --TPT/--TPTREF/--STTPT/--ENTPT Timing 四件套 (PK 复杂场景) | 1 | 共用 | 中-难 |
| **C2** | Partial date 约定 (---DTC imputation) | 1 | 共用 | 中 |
| **D1** | Extensible vs Non-Extensible codelist (MedDRA 混入) | 1 | 共用 | 中 |
| **E1** | Pinnacle 21 常见 rule 违反修正 (SD0001/SD1001 等) | 1 | 共用 | 难 (ChatGPT batch 2 优势) |
| **H1** | QORIG/QEVAL/QLABEL 何时填 + SUPPTS vs SUPP-- | 1 | 共用 | 难 |
| **F1** | Dataset-JSON v1.1 vs XPT v5 submission | 1 | ChatGPT 专属 | 中 (新话题 RAG 优势) |
| **G1** | RWD 下哪些 conformance rule 失效 | 1 | ChatGPT 专属 | 难 |
| **D2** | CT 版本锁定 submission + 跨 CT 版本 AETERM 一致性 | 1 | ChatGPT 专属 | 中 |
| **I1** | AE + CE + MH 三域能否同时记同一临床事件 + DSDECOD vs DSCAT | 1 | ChatGPT 专属 | 中 |

**总计**: 双平台共用 10 题 (A1/A2/A3/B1/B2/C1/C2/D1/E1/H1) + ChatGPT 专属 4 题 (F1/G1/D2/I1) = ChatGPT 14 / Gemini 10.

### 3.2 每题 PASS 判据模板

```
PASS 判据 (核心事实必中):
- [业务判断] 核心答案 (e.g., "GF 的 Topic 变量是 GFTEST, 记变异基因名")
- [变量级] 列出 N 个关键变量 + Core 属性
- [跨域边界] 若涉及多域, 说明各自职责不混淆
- [CT 值] 若涉及 CT 值, 给 codelist 名 + NCI EVS Browser 外链路径 (不内嵌 term)

FAIL 判据:
- 答错域 (比如把 GF 说成 PGx-MD 旧域)
- 臆造变量名 (比如 GF 域编个 GFGENE, 其实是 GFTEST)
- 错用 Core (比如说 GFSEQ 是 Exp 其实是 Req)
- 把 04 场景答案机械套用 (比如答 BE/BS 直接抄 AE/SAE 模板)
```

### 3.3 generalization 合格度自测

- **≥10/14 PASS (ChatGPT) + ≥7/10 PASS (Gemini)** → generalization probe PASS, Phase 4→5 Gate 开闸候选
- **< 阈值** → 列 carry-over, Phase 4 fix loop (不直接进 Phase 5)
- **04 重叠命中 ≥3 题** → N5.3 题库作废重设 (主 session 责任)

---

## §4. 执行流程 (N5.3 内部 5 步)

| Step | 动作 | 产物 | 谁做 |
|------|------|------|------|
| **1** | 主 session 本 design doc + 联网深度取材 (3-5 WebFetch 取 PharmaSUG 精细论文 + CDISC Observational doc) | 本文件 + `smoke_v3_questions_draft.md` | 主 session |
| **2** | 用户 review 本 design doc + 题目 draft, ack 或调整 | 用户口头 ack | 用户 |
| **3** | 派 2 reviewer 独立 subagent_type (第 20+21 种 Rule D) 审 smoke_v3_questions.md 题目 SDTM 事实正确性 + 04 非重叠 + PASS 判据合理性 | 2 份 `phase4_n5_3_questions_reviewer.md` | subagent |
| **4** | 用户 + Chrome MCP 跑双平台 Web UI (ChatGPT 14 题 / Gemini 10 题), 每题独立 conversation, DOM 回读, 落档 `smoke_v3_results.md` + `smoke_v3_answers/Q*.md` | 双平台答案包 | 用户 |
| **5** | 派 2 reviewer 独立 subagent_type (第 22+23 种 Rule D) 审答题 + 计算 PASS 比 + Phase 4→5 Gate decision. 主 session 汇 `STAGE_PHASE4_AB_REPORT.md` 双份 | Phase 4 AB_REPORT + Gate decision | subagent + 主 session |

---

## §5. Risk / 回退

| 风险 | 信号 | 回退 |
|------|------|------|
| 题目 SDTM 事实错 | reviewer 独立审发现 ≥1 硬知识错 | 换题 (不强过) |
| 04 重叠命中 >30% | 反向 grep 04 发现直接答 | 换题 / reframe |
| Gemini 7/10 且 ChatGPT 10/14 (差距偏大) | N5.3 AB_REPORT | 分析 B 类 (域边界) 是否对 Gemini 04 弹药包不充分 — 若是, 接受差距记录 RETROSPECTIVE, 不强改弹药包 |
| ChatGPT <10/14 | N5.3 AB_REPORT | batch 2 terminology 未足覆盖, 启 N5.1 fix 类似 loop (不常, Phase 3 已过) |
| Dataset-JSON / Pinnacle 21 题过新两平台都不会 | N5.3 双平台 FAIL | 标记 "超出 SDTM 核心范围, 排除评分", 题目作废 |
| generalization probe 整体 < 目标阈值 | Phase 4 reviewer HOLD | carry-over Phase 5 retrospective 记录 "04 预压缩降低 Gemini 真实 generalization", 不强过 Phase 4 |

---

## §6. 04 非重叠 audit 方法

对每道题 draft, 执行:
```
1. 提取题目核心变量 (e.g., GFTEST, GFCAT)
2. 提取题目场景 keyword (e.g., "遗传变异", "基因分型")
3. Grep 04 变量 + keyword 各一轮
4. 若变量 hit 04 且 keyword hit 04 同一段 → 重叠 (换题)
5. 若变量 hit 04 但 keyword 不 hit → 04 只列变量名不深入 (allow, generalization OK)
6. 若变量 + keyword 都 0 hit → pure generalization (最佳)
7. 产 audit 表 smoke_v3_overlap_audit.md
```

---

## §7. Rule D subagent_type 规划 (N5.3 要新增 4 种)

已累计 19 种 (Rule D 独立链). N5.3 需用 4 种新的:

| 用途 | 候选 subagent_type | 备选 |
|------|--------------------|------|
| Step 3 Q 正确性 reviewer (ChatGPT 侧) | **第 20 种**: `oh-my-claudecode:scientist` (Rule D 独立, 数据科学验证风格) | `oh-my-claudecode:debugger` |
| Step 3 Q 正确性 reviewer (Gemini 侧) | **第 21 种**: `feature-dev:code-explorer` (新) | `oh-my-claudecode:sciomc` |
| Step 5 答题 reviewer (ChatGPT 侧) | **第 22 种**: `oh-my-claudecode:critic` (已 N2 用, 本身对答案判准严格; 若严格不重复用 `pr-review-toolkit:type-design-analyzer`) | `superpowers:receiving-code-review` |
| Step 5 答题 reviewer (Gemini 侧) | **第 23 种**: `pr-review-toolkit:type-design-analyzer` 或 `vercel:ai-architect` | `oh-my-claudecode:explore` |

**锁定** (执行时按可用性调整, 遵规则 D 精神即独立判断非绝对不重复):
- N5.3 Step 3: `scientist` (ChatGPT Q 审) + `feature-dev:code-explorer` (Gemini Q 审)
- N5.3 Step 5: `critic` (ChatGPT 答审, 跨任务范围 vs N2) + `pr-review-toolkit:type-design-analyzer` (Gemini 答审)

---

## §8. 下一步 (等用户 ack 后)

1. 主 session 联网深度取 3-5 篇 PharmaSUG 2024-2025 核心论文 + CDISC Observational doc + Pinnacle 21 rule 列表, 补进题目 draft
2. 产 `ai_platforms/smoke_v3_questions_draft.md` (14 题全文, 含 PASS/FAIL 判据 + 源锚点 + 04 非重叠自证)
3. 反向 grep 04 跑 overlap audit, 产 `smoke_v3_overlap_audit.md`
4. 派 2 reviewer 独立审题
5. 汇报用户 ack → 进 Step 4 Web UI 跑 smoke

---

*来源: N5.2 用户 generalization probe 疑虑 (2026-04-21 session 末 Gemini _progress.json `n5_3_design_open_question_raised_by_user_2026_04_21`) + 联网 WebSearch 3 路 (PharmaSUG 2025 / CDISC SDTM mapping / SDTMIG v3.4 specialty) + PHASE4_PLAN.md §3 N5.3 row + CLAUDE.md 锁步规则.*

## 附录: 已联网采集的初步题源 (WebSearch 3 路)

### 附录 A. PharmaSUG 2024-2025 相关论文 (需 WebFetch 深读)
- [PharmaSUG China 2025 DS-134 — Implementing CDISC SDTMIG v3.4: Practical Strategies and Lessons](https://www.lexjansen.com/pharmasug-cn/2025/DS/Pharmasug-China-2025-DS134.pdf)
- [PharmaSUG 2025 SI-159 — SDTM programming timing / validation patterns](https://pharmasug.org/proceedings/2025/SI/PharmaSUG-2025-SI-159.pdf)
- [PharmaSUG 2025 SI-180 — Data quality patterns](https://pharmasug.org/proceedings/2025/SI/PharmaSUG-2025-SI-180.pdf)
- [PharmaSUG 2025 SI-224 — Elevating Clinical Research validation](https://pharmasug.org/proceedings/2025/SI/PharmaSUG-2025-SI-224.pdf)
- [PharmaSUG China 2025 DV-181 — Real-time SDTM Data Quality Check](https://www.lexjansen.com/pharmasug-cn/2025/DV/Pharmasug-China-2025-DV181.pdf)
- [PhUSE 2024 DS10 — What's New in the SDTMIG v3.4 and the SDTM v2.0](https://www.lexjansen.com/phuse-us/2024/ds/PAP_DS10.pdf)
- [PharmaSUG 2023 DS-114 — CDISC SDTM IG v3.4: Subject Visits](https://pharmasug.org/proceedings/2023/DS/PharmaSUG-2023-DS-114.pdf)

### 附录 B. CDISC 官方资源
- [SDTMIG v3.4 official](https://www.cdisc.org/standards/foundational/sdtmig/sdtmig-v3-4)
- [Considerations for SDTM Implementation in Observational Studies and RWD v1.0](https://www.cdisc.org/sites/default/files/2024-02/Considerations%20for%20SDTM%20Implementation%20in%20Observational%20Studies%20and%20Real-World%20Data%20v1.0.pdf)
- [LB/MB/IS Domain Scope Changes webinar](https://www.cdisc.org/events/webinar/lb-mb-domain-scope-changes-sdtmig-v3-4-and-impact-controlled-terminology)
- [IS Domain Scope Update article](https://www.cdisc.org/kb/articles/domain-scope-update-sdtmig-v3-4-development-history-and-difficulties-standardizing)
- [SDTM Metadata Submission Guidelines v2.0](https://www.cdisc.org/standards/foundational/sdtm/sdtm-metadata-submission-guidelines-v2-0)

### 附录 C. 验证 / 实战资源
- [Pinnacle 21 by Certara — SDTM Mapping Process Simplified](https://www.certara.com/blog/the-sdtm-mapping-process-simplified/)
- [IntuitionLabs — CDISC Standards: SDTM and ADaM](https://intuitionlabs.ai/articles/cdisc-sdtm-adam-guide)
