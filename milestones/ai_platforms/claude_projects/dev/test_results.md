# v2 A/B 测试结果矩阵

> 用户每阶段后回填; 主控写入并归档到 evidence_v2/stage_v2.X_audit.md + evidence_v2/checkpoints/ckpt_v2.X.md

## T1-T8 回归 (源自 v1)

| # | 题目 | 期望 | v1 答案 | v2.1 答案 | v2.2 答案 | 精度 vs v1 | 精度 vs v2.1 | 阶段 |
|---|-----|------|--------|----------|----------|-----------|-------------|------|
| T1 | AE.AEDECOD 的 Core 属性是什么? | Req (mega_spec + variable_index) | Core=Req, 引 05 mega_spec §AE + 04 variable_index(Sy/R) + 02 §4.3.6 | 同 v1, 来源等同 | Core=Req + §4.3.6 三元 (AETERM/AEMODIFY/AEDECOD) + AEDECOD 在其他 Events 域为 Perm 对比 + AEPTCD 配套 | 持平 | 持平 (略 ↑) | v2.2 |
| T2 | AE 严重程度变化如何记录? | AEGRPID 方案 | 3 方案 A/B/C + E2B/CTCAE 延伸 | 同 3 方案 + 5 处章节锚点 (§4.2.1/§4.3.6/§8.6.3/assum7e/AE3b) | ↑ | v2.1 |
| T3 | PC↔PP 通过 RELREC 关联的 4 种方法? | Method A-D | 声明 §6.3.5.9.3 不在 Project, 基于通用规则重建 3+1 方法 (含推测标注) | **严格拒答完整 4 种**; 仅引 §8.3 MANY/MANY 一句; 边界模板触发 | v2.3 **↑ 显著**: 保边界诚实 (明标 §6.3.5.9.3 narrative 不在) + 从 09 PC relrec 数据推导 4 粒度 (Group↔Group / Seq→Group / Group→Seq / Seq↔Seq) + dataset-level 附录 + 推断 Method A/B/C/D 映射; 共 5 张完整 relrec.xpt | 跨批累积激活 | v2.3 |
| T4 | 哪些域有 EPOCH 变量? | 44 个域 | 44 域按 class 分组 + CT C99079(44) + 19 不含域 | 同 44 域分组, 增 §4.1.3.1 EPOCH-Capable Domains 原文锚点 | ↑ | v2.1 |
| T5 | 如何判断变量是否需要提交到 SUPP--? | ch08 §8.4 规则 | 7 级优先级决策树 + §8.4.4 4 条禁令 | 5 步决策树 (合并 step 6/7) + §8.4.4 + SUPP-- spec 表格 | 持平 | v2.1 |
| T6 | AE Example 2 的具体数据是什么? | 数据表 | 严格拒答 (07 是目录), 给标签+演示意图 | 同严格拒答, 额外给 6 个 AE Examples catalog 表 | ↑ | v2.1 |
| T7 | CT Code C66742 有哪些具体值? | 完整 Term 表 | 高信心推测 Y/N/U/NA, 引 §4.3.7 + 05 mega_spec | 同推测, 增 §4.3.7 "Y or N extended to U or NA" 原文 | ↑ (轻微) | v2.1 |
| T8 | CV 域所有变量值范围? | "需查 examples/terminology" | 42 变量按 6-Role 分层 + CT 引用 + 边界 | 同 42 变量重组为 4-class value-range; CT 等同 | ↑ (轻微, 组织维度) | v2.1 |

## T9-T20 新增 (覆盖 v2 五批)

| # | 批 | 题目 | 期望 | v1 答案 | v2.1 答案 | 精度 | PASS? |
|---|----|-----|------|--------|----------|------|-------|
| T9  | 1 | ch01 SDTM 整体架构 + Foundational concepts? | 完整段落 | PASS with 边界, §1.1-§1.4 + ch02 §2.1-§2.8 + 原则 | **PASS**, 纠正前提 "ch01 is Introduction" + §1.1-§1.5 + byte-exact ch01 p.7-12 | ↑ (轻微) | **PASS** ✅ |
| T10 | 1 | ch02 §2.6 创建新 domain 的所有步骤? | 完整列表 | PASS, §2.6 item 1/2/3 + 11 子步骤 a-k (部分简化) + 4 Key Rules | **PASS**, 完整 11 子步骤 a-k 表格 + 4 Key Rules + **v3.4 新增 SA/SQ 变更条目** + §2.5/§2.7 约束 | ↑ | **PASS** ✅ |
| T11 | 1 | (变体 — v1: ch08 §8.3 RELREC; v2: ch03 §3.1.2.2 虚构 section) | 完整规则+示例 / 虚构检出 | PASS w/caveat, 区分 §8.2 vs §8.3 + RELTYPE 3 值 + 7 延伸 | **PASS**, 立即检出虚构 §3.1.2.2 + 完整 ch03 TOC + 10 条命名规则映射到 §2.2/§4.1.6/§4.1.7/§4.2.1/§4.2.2/§8.4.2/Appendix D | **PASS v2.2**: ch08 §8.3 全文 (§8.2 vs §8.3 对照表 + §8.3.1 TU↔TR relrec.xpt + 5-step 工作流 + 4 应用场景 + 4 提醒), 持平或略 ↑ | N/A (变体) | **PASS** ✅ (各自) |
| T12 | 1 | (变体 — v1: ch10 附录 entity; v2: ch04 §4.4 Timing 变量) | 完整清单 / 完整 §4.4 | PASS, Appendix A-E 完整 + C1 v3.4 已 removed TS 标记 + 9 行边界表 | **PASS**, §4.4.1-§4.4.10 全覆盖 + **§4.4.8 "--STDTC 禁用于 Findings" v3.4 新增** + v3.4 变更对照表 | N/A (变体) | **PASS** ✅ (各自) |
| T13 | 2 | DM 的 Example 1 完整数据表? | 表格 | (兜底模板, 回落到源路径) | (v2.1 09 未在, 同 v1) | **PASS v2.2**: 6×25 dm.xpt 完整表 + Row 4 SCREEN FAILURE ARMNRS 用法 + RACE 6 CT 值覆盖, Source 标 09 | ↑ | **PASS** ✅ |
| T14 | 2 | EX 剂量调整 Example 数据怎么写? | 表格 | (兜底, 回落源路径) | (v2.1 09 未在, 同 v1) | **PASS v2.2**: Ex4 完整 6×14 ex.xpt 表 (EXADJ "Reduced due to toxicity" / "Increased due to suboptimal efficacy") + 3 建模要点 + EC/EX Ex7 延伸, Source 标 09 | ↑ | **PASS** ✅ |
| T15 | 3 | RP 域 Example 数据? | 表格 | (兜底) | **PASS v2.3**: 完整 21×18 rp.xpt (2 受试者 × 3 访视, Pre-Menopause CHILDPOT/PREGST + MENOPAUSE 场景, RPDUR ISO 8601 期间 P3Y), Source 标 10 | ↑ | **PASS** ✅ |
| T16 | 3 | FT 域 Example 数据? | 表格 | (兜底) | **PASS v2.3**: 完整 6×16 ft.xpt (6MWT SIXMW101-106 分钟级 TESTCD) + suppft.xpt 1×10 (FTASSTDV=CANE 辅助设备), Source 标 10; 附 QRS Naming Rules 引自 06 | ↑ | **PASS** ✅ |
| T17 | 4 | C66742 codelist 所有 Term 值 + Definition? | 完整 Term 表 | (兜底) | **PASS v2.4 ↑**: 完整 4 Term 表 (C49487 N / C48660 NA / C17998 U / C49488 Y) + Extensible No + 41 Related Domains (AE/AG/BS/CE/CM/CP/CV/DM/EC/EG/EX/FA/FT/GF/HO/IE/IS/LB/MB/MH/MI/MK/ML/MS/NV/OE/PC/PE/PR/QS/RE/RP/RS/SR/SU/SV/TM/TR/TU/UR/VS) + §4.3.7 Y/N/U/NA 使用规则; Source 标 `11a_terminology_high_core.md → ## No Yes Response (C66742)` + 源 `knowledge_base/terminology/core/general_part4.md` + `02_chapters.md §4.3.7` | ↑ (从"推测"→"11a 原文命中") | **PASS** ✅ |
| T18 | 4 | AERELN codelist 全部 Synonyms? (边界) | "不在源"声明 + 替代 | TBD | **PASS v2.4**: 明确声明 "AERELN 不是 SDTMIG v3.4 标准变量/codelist", 08_terminology_map.md 也无对应项; 列 AE Relationship 系列变量 (AEREL/AERLDEV/AERELNST/AERLPRT/AERLPRC 全部"无 CDISC CT") + 已发布 AE 相关 codelist (C66767 Action Taken / C111110 Device Events / C66768 Outcome / C66769 Severity) + ch04 §4.2.8.3 AERELNS1 SUPPAE QNAM 说明 + 请澄清段落; 零臆造 Synonyms | — | **PASS** ✅ |
| T19 | 5 | FREQ codelist (中频) 全部 Term + Code? | 表格 | TBD | TBD (Stage v2.5) | TBD | TBD |
| T20 | 5 | PROBLEM_TYPE codelist (中频) 全部值? | 表格 | TBD | TBD (Stage v2.5) | TBD | TBD |

## 阶段汇总

### v2.1 (2026-04-18 → 2026-04-19, chapters 全展开 batch)

- **Capacity 实测**: 13% (v1 = 12%, +1pp)
- **T1-T8 分布**: 5 ↑ / 2 持平 / **1 ↓** (T3)
- **T9-T12 分布**: 4/4 PASS
- **T1-T8 整体健康度**: 7/8 无衰减, 符合 "<2 ↓ 继续" 门槛, 但触发 "1 ↓ → 询问用户" 分支
- **关键收益**: chapter byte-exact 展开让 v2 能精确引用 §4.4.8/§2.6 SA/SQ 等 v3.4 新增条目; 主动检出虚构 §3.1.2.2
- **代价**: T3 拒答 (§6.3.5.9.3 未收录时 v2.1 不再重建), 边界严谨换 T3 实用性
- **决议**: 待用户 ack 继续/调整/暂停 (详 `evidence_v2/checkpoints/ckpt_v2.1.md`)
- **后续修复路径**: batch 2 (Task D1-D4) 纳入 ch06 PP/PC examples + ch04 §4.3.6 AE Examples 全展开, 可同时修 T3+T6 缺口

### v2.2 (2026-04-19, examples 高频 28 域 batch)

- **Capacity 实测**: **20%** (v2.1 = 13%, +7pp, 精确匹配规划 20-22% 预期)
- **上传文件**: 9 v2.1 不变 + 1 新 (09_examples_data_high.md, 112,697 tokens, 28 域数据表全量), 总 10 文件 / 318,592 tokens
- **T13 DM Ex1 数据**: **PASS ↑** — 命中 09, 完整 6×25 dm.xpt 表 (含 Row 4 SCREEN FAILURE 场景 + ARMNRS 字段用法 + RACE 6 CT 全覆盖)
- **T14 EX 剂量调整**: **PASS ↑** — 命中 09, Ex4 完整 ex.xpt 表 + EXADJ 真实 free-text ("Reduced due to toxicity" / "Increased due to suboptimal efficacy") + 3 建模要点 + EC/EX Ex7 延伸对照
- **T1 AEDECOD (回归)**: 持平 (Core=Req 稳定, v2.2 增 §4.3.6 三元结构 + 跨域 DECOD 对比 + AEPTCD 配套, 非衰减)
- **T11 ch08 §8.3 RELREC (回归)**: 持平 (ch08 全文未变, v2.2 增 §8.2 vs §8.3 对照 example, 非衰减)
- **回归衰减 ↓**: **0 / 2** (门槛 ≥2 停, ≥1 询问; 本批无衰减)
- **新增 PASS**: **2 / 2**
- **关键观察**:
  - Examples 查询优先级规则 "09 > 07" 被 Instructions 正确解读, 无一 fallback 到 v1 模板
  - 112K 新文件对 05_mega_spec / 02_chapters 召回无挤出/遮蔽
  - +7pp capacity 精确匹配 (13%→20%), 验证 Option A 容量预算
- **异常**: Chrome MCP file_upload 对 sandbox/绝对路径均 `Not allowed`, 本次用户手工拖拽完成; indexing indicator 不可靠, 上传后立即提问即可命中
- **决议**: T1/T11 无 ↓ + T13+T14 = 2/2 PASS → **继续 Task E1 批 3 (examples 剩余域)**

### v2.3 (2026-04-19, examples 剩余 35 域 batch)

- **Capacity 实测**: **23%** (v2.2 = 20%, +3pp, 比 v2.1→v2.2 的 +7pp 小; 比例匹配新增 48.9K / v2.2 的 112K)
- **上传文件**: 10 v2.2 不变 + 1 新 (10_examples_data_others.md, 48,897 tokens, 35 域 examples 全覆盖), 总 11 文件 / 367,489 tokens
- **T15 RP Example**: **PASS ↑** — 命中 10, 完整 21×18 rp.xpt, 覆盖 Pre-Menopause CHILDPOT/PREGST/育龄期前期/已绝经双场景 + RPDUR P3Y ISO 8601 期间
- **T16 FT Example**: **PASS ↑** — 命中 10, 完整 6×16 ft.xpt (SIXMW 6-Minute Walk Test) + suppft.xpt 配套 (FTASSTDV=CANE); 引 06 QRS Naming Rules 佐证, 多文件协同
- **T3 PC↔PP RELREC 4 方法 (v2.1/v2.2 硬拒答历史)**: **↑ 显著** — v2.3 不再硬拒答, 从 09 的 PC relrec 数据推导出 4 种粒度模式 (Group↔Group / Seq→Group / Group→Seq / Seq↔Seq) + dataset-level 附录, 共 5 张完整 relrec.xpt, 并推断 Method A/B/C/D 映射 (标明需原文校验). 保边界诚实前提下突破
- **T11 ch08 §8.3 RELREC (回归)**: 持平略 ↑ — ch08 在 02_chapters.md 未变, v2.3 多了 --SEQ 禁用原文直引 + TR Example 2 实测数据 (USUBJID=44444, TULNKID=T01) 来自 09 作交叉佐证. 多文件协同 (02+09+06+03) 正常
- **回归衰减 ↓**: **0 / 2** (门槛 ≥2 停, ≥1 询问; 本批零衰减且 T3 反向 ↑)
- **新增 PASS**: **2 / 2**
- **关键观察**:
  - "09 > 10 > 07" Instructions 优先级被正确解读, RP/FT 不在 09 时自动回落 10, 无一 fallback 到 v1 源路径模板
  - **T3 跨批累积正向激活**: v2 累积视角下 "拒答 → 从数据推导" 的跳变是 **RAG decay curve 二阶正向效应** (批 2 09 数据 + 批 3 10 + Instructions 升级触发). 详见 `rag_decay_curve.md` v2.2→v2.3 观察段
  - 48.9K 新文件对 02/05/06 老文件无挤出, 所有 Source 溯源仍准确
- **异常**: Indexing indicator 继续显示但不 gating 提问, 沿用 v2.2 结论; 本批用户本地上传, 无 Chrome MCP file_upload 受限触发
- **决议**: T11 无 ↓ + T15+T16 = 2/2 PASS + T3 反向 ↑ → **继续 Task F1 批 4 (terminology 高频)**

### v2.4 (2026-04-19, terminology 高频 top 200 codelist 完整 Term batch)

- **Capacity 实测**: **43%** (v2.3 = 23%, +20pp, 本批是 v2 token 跃升最大阶段; 投影 +22pp, 实测 +20pp, 匹配度 ~91%)
- **上传文件**: 11 v2.3 不变 + 3 新 (`11a_terminology_high_core.md` 68,559 tokens / 29 codelist + `11b_terminology_high_questionnaires.md` 256,336 tokens / 152 QRS codelist + `11c_terminology_high_supp.md` 26,857 tokens / 19 Device/FT/Discharge codelist), 总 14 实体文件 / **719,241 tokens** (+351,752 增量)
- **T17 C66742 Term 表 (新, 批 4 核心修复)**: **PASS ↑ (质变)** — v2.1/v2.2/v2.3 三连高信心推测 Y/N/U/NA (08 只映射), v2.4 在 11a rank 1 直接命中完整 4 Term 表 (C49487 N / C48660 NA / C17998 U / C49488 Y) + Extensible No + 41 Related Domains 行 + §4.3.7 使用规则; Source 三层溯源 (`11a` + `general_part4.md` + `02_chapters §4.3.7`). 从"推测"跃升为"原文命中", PLAN §F4 修复期望完美达成
- **T18 AERELN 边界 (新, 批 4 边界测试)**: **PASS** — 坦诚 "AERELN 不是 SDTMIG v3.4 标准变量/codelist" + 列相邻 AE Relationship 系列 (AEREL/AERLDEV/AERELNST/AERLPRT/AERLPRC 全"无 CDISC CT") + 已发布 AE codelist (C66767 Action Taken / C111110 Device Events / C66768 Outcome / C66769 Severity) + SUPPAE QNAM 可能性 + ch04 §4.2.8.3 交叉引用; 零臆造 Synonyms; 边界感知远超 PLAN 最低要求
- **T7 CT Code C66742 (回归, 批 4 关键修复期望)**: **↑ 质变** — v2.3 高信心推测, v2.4 从 11a 原文 4 Term 表直接命中 + 41 Related Domains + 源文件 `general_part4.md`. 这是 v2.4 对 v2.3 修复期望的完美达成
- **T15 RP Example (回归)**: **持平** — 完整 21×18 rp.xpt 双场景 (P0001 childbearing potential + P0002 post-menopausal) + BCMETHOD 携带 RPDUR P3Y + 数值无衰减 + RP Assumptions 4 条配套, 10_examples_data_others.md 未被 11b 256K 挤出
- **T1 AEDECOD Core (深度回归, 敏感度最高)**: **持平或略 ↑** — Core=Req 稳定, v2.4 同时引 §4.3.5 (Synonym Qualifier for MedDRA/WHODrug) + §4.3.4 + §4.3.6 + §4.2.8.1 + AE Assumption #12 + 完整 MedDRA 层级树, 比 v2.3 仅 §4.3.6 更全; 05_mega_spec + 06_assumptions + 02_chapters 召回零衰减
- **T3 PC↔PP RELREC (深度回归, v2.3 ↑ 点)**: **继续 ↑** — v2.4 显式 Method A/B/C/D 独立段 + 每方法完整 relrec.xpt 数据表 + A-D 汇总矩阵 (IDVAR/RELID 数/relrec 行数/粒度/溯源能力) + 粒度选择建议 (D>C>B>A); 3 次独立子查询 ("RELREC four approaches"/"PCGRPID PPGRPID"/"Method A B C D dataset level") 精准命中 09, 11b 256K 未挤出; 坦诚声明 §6.3.5.9.3 prose 未抽入 Project (技术债信号转接 G1/H1)
- **回归衰减 ↓**: **0 / 4** (T7 从推测→命中算 ↑; T15/T1/T3 零衰减, T3 继续 ↑; 门槛 ≥1 衰减停, 本批零衰减)
- **新增 PASS**: **2 / 2** (T17/T18)
- **关键观察**:
  - **11b 256K 单文件挤出风险假设反驳**: 11b 是当前 v2 单文件 token 最大记录 (vs v2.3 最大 112.7K 09), 未造成 05/02/09 老文件召回稀释; PLAN §F4 最敏感的 T1/T15/T3 三题零衰减 + T3 继续 ↑
  - **CT Code 查询优先级 `11*>08` (v2.4 新 Instructions 段) 被 Claude 正确解读**, T17/T7 Source 均直达 11a rank 1
  - **T3 跨批累积三阶正向激活**: v2.2 硬拒答 → v2.3 从数据推导 → v2.4 显式 Method 独立段, 是 v2 最显著的 RAG 正向二阶效应
  - **Capacity 爬升曲线匹配**: v2.3 23% + 351.8K / 16K-per-pp ≈ +22pp 投影, 实测 +20pp (43%), 91% 匹配度
- **异常/警告**: 无 RAG 衰减拐点; **T3 SDTMIG §6.3.5.9.3 "Method A/B/C/D" prose 未抽入 Project** (Claude 主动声明, 优先级中等, 建议 G1/H1 考虑是否在 02_chapters 或 06_assumptions 补段); Indexing indicator 仍不可靠, 沿用前两批结论
- **独立复核 (Rule D)**: `code-reviewer` subagent (与 Cowork writer + 主控 writer 独立的第三条 lane) 对 STAGE_V2.4_AB_REPORT.md 7 维度审计全 PASS — 覆盖/T17 证据/T18 边界/Capacity 数学/决策矩阵/Rule D/无幻觉引用
- **决议**: T1/T15/T3 零衰减 + T7 ↑ 质变 + T17+T18 = 2/2 PASS + T3 继续 ↑ → **继续 Task G1 批 5 (terminology mid 频 codelist, rank 201-500)**
