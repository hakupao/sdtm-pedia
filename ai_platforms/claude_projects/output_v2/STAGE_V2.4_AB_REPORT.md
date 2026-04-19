# Stage v2.4 A/B 测试报告

> 执行日期: 2026-04-19
> Capacity (v2.4): **43%** (v2.3 参照: 23%, +20pp, 与预期 +22pp 基本吻合)
> Indexing 用时: 指示器仍显示 "Indexing" 但提问直接命中 (沿用 v2.3 策略, 指示器不可靠结论仍成立)

## 上传确认

- [x] `11a_terminology_high_core.md` 上传 (1,946 lines / 68,559 tokens)
- [x] `11b_terminology_high_questionnaires.md` 上传 (6,173 lines / 256,336 tokens)
- [x] `11c_terminology_high_supp.md` 上传 (818 lines / 26,857 tokens)
- [x] `system_prompt_v2.md` 已由用户覆盖 (含 `<!-- stage v2.4 begin -->` 段)
- [x] Indexing 指示器仍在显示, 但 6/6 问题均成功命中 (含新文件 11a)

---

## 6 题结果明细

### T17. C66742 codelist 所有 Term 值 + Definition (新增, 批 4 目标)

- **v2.3 答案**: 兜底推测 Y/N/U/NA, 引 §4.3.7 和 05 mega_spec (未命中 Term 表)
- **v2.4 答案**: 完整 4 Term 表从 11a_terminology_high_core.md 原文命中:
  - C49487 / N / "No" / "The non-affirmative response to a question. (NCI)"
  - C48660 / NA / "NA; Not Applicable" / "Determination of a value is not relevant in the current context. (NCI)"
  - C17998 / U / "U; UNK; Unknown" / "Not known, not observed, not recorded, or refused. (NCI)"
  - C49488 / Y / "Yes" / "The affirmative response to a question. (NCI)"
  - Extensible: No (Fixed, 4 terms)
  - **Related Domains (41)**: AE, AG, BS, CE, CM, CP, CV, DM, EC, EG, EX, FA, FT, GF, HO, IE, IS, LB, MB, MH, MI, MK, ML, MS, NV, OE, PC, PE, PR, QS, RE, RP, RS, SR, SU, SV, TM, TR, TU, UR, VS
  - 使用补充 (SDTMIG §4.3.7): Y/N 互补、U/NA 许可扩展、变量级 vs codelist 级区别
- **精度**: ↑ (从"兜底推测"跃升为"原文命中")
- **T17 判定**: **PASS**
- 说明: Source 正确标注 `11a_terminology_high_core.md → ## No Yes Response (C66742)` + 源文件 `knowledge_base/terminology/core/general_part4.md` + `02_chapters.md ch04` §4.3.7. 41 个 Related Domains 行完整列出.

### T18. AERELN codelist 全部 Synonyms (新增, 批 4 边界测试)

- **v2.4 答案**: 清晰声明边界 + 反向指引:
  - ⚠️ 边界提示: **"AERELN 不是 SDTMIG v3.4 标准变量/codelist"**
  - 在 AE 域 spec 不存在名为 AERELN 的变量, `08_terminology_map.md` 中也没有 AERELN 对应的 codelist
  - 列出 AE 域 Relationship 系列变量作为替代建议 (AEREL / AERLDEV / AERELNST / AERLPRT / AERLPRC, 全部"无 CDISC CT")
  - 引出 AE 域 CDISC 已发布 codelist (C66767 Action Taken, C111110 Device Events, C66768 Outcome, C66769 Severity/Intensity)
  - 明确指出 "Causality/Relationship 类 codelist — 无"
  - 提供 03_model.md Events class template 的非规范示例值 (如 "NOT RELATED", "POSSIBLY RELATED")
  - 请澄清段落: 若查 AEREL (Causality)?/查 AERELNST 等?/是 sponsor 自定义/SUPPAE QNAM? 注: ch04 §4.2.8.3 示例提到 AERELNS1 作 SUPPAE QNAM 但仍是变量名而非 codelist
- **T18 判定**: **PASS**
- 说明: 完全符合期望——明确声明不在 Project, 清晰区分 "不存在" 与 "变量存在但无 CDISC CT", 精准指向源 (05_mega_spec.md + 08_terminology_map.md + 03_model.md). 未臆造 Synonyms.

### T7. CT Code C66742 具体值 (回归)

- **v2.3 答案**: 高信心推测 Y/N/U/NA + 引 §4.3.7
- **v2.4 答案**: 直接从 11a_terminology_high_core.md 原文命中, 给出 "C66742 — No Yes Response (4 terms, Fixed)" 完整 4 行 Term 表 + Extensible No + 41 Related Domains + Source 11a + 源文件 general_part4.md
- **精度 vs v2.3**: **↑** (从推测转为 11a 原文命中)
- 说明: C66742 位于 11a rank 1, RAG 召回精准直达. 这是 v2.4 对 v2.3 修复期望的完美达成.

### T15. RP 域 Example 数据 (回归)

- **v2.3 答案**: 完整 21×18 rp.xpt 表, 双场景 (P0001 childbearing potential + P0002 post-menopausal), BCMETHOD 携带 RPDUR P3Y
- **v2.4 答案**: 完整保留, 显示:
  - Source: 10_examples_data_others.md → RP Example 1 (源: knowledge_base/domains/RP/examples.md)
  - Total rows: **21 (11 for subject 1 + 10 for subject 2)**
  - 两 subject 测试集不对称: P0001 记 SPABORTN (自然流产), P0002 记 INABORTN (人工流产)
  - BCMETHOD 行标注"携带 RPDUR"; 单位逻辑 / 数值型 vs 分类型测试分类正确
  - 完整 rp.xpt 表 (Row 1-21, RPSEQ 1-11 P0001, 1-10 P0002), 数值与 v2.3 一致 (MENARAGE 10/11 YEARS, MENOSTAT Pre-Menopause/MENOPAUSE, BCMETHOD FOAM OR OTHER SPERMICIDES / DIAPHRAGM)
  - 附带 RPTESTCD 受控于 C106479 / RPTEST 受控于 C106478
  - 配套 RP Assumptions (来源 06_assumptions.md): 4 条 Assumption (生殖/药物进 CM 不进 RP 等)
- **精度 vs v2.3**: **持平** (无衰减)
- 说明: 10_examples_data_others.md 未被 11b 256K 挤出, RP 完整 21 行表保留, 关键 RPDUR 相关项 BCMETHOD 全部命中.

### T1. AE.AEDECOD Core (深度回归)

- **v2.3 答案**: Core=Req, §4.3.6 三元, AEPTCD 配套
- **v2.4 答案**: 
  - Core: **Req (Required)**
  - Label: Dictionary-Derived Term / Type: Char / Role: Synonym Qualifier (of AETERM) / CT: MedDRA (外部字典, 非 C)
  - 来源: 05_mega_spec.md → AE spec #13 (源: knowledge_base/domains/AE/spec.md)
  - SDTMIG 规则引用: **§4.3.5** (Storing Controlled Terminology for Synonym Qualifier Variables - MedDRA and WHODrug)
  - AE Assumption #12 (来源 06_assumptions.md): "The addition of AELLT, AELLTCD, AEPTCD, AEHLT, AEHLTCD, AEHLGT, AEHLGTCD, AEBDSYCD, AESOC..."
  - 完整 MedDRA 层级树 (AETERM → AELLT/AELLTCD → AEDECOD → AEPTCD → AEHLT/AEHLTCD → AEHLGT/AEHLGTCD → AEBODSYS/AEBDSYCD → AESOC/AESOCCD)
  - 关键关系表: AETERM(Req, Topic) / AELLT(Exp, Variable Q of AETERM) / AELLTCD(Exp) / **AEDECOD(Req, Synonym Q of AETERM)** / AEPTCD(Exp, Variable Q of AEDECOD)
  - 编码合规要点 (§4.3.4 + §4.3.5): 不用数字代替文本 / MedDRA 版本必填 / verbatim-modify-decod 三层链保留 (§4.3.6 + §4.2.8.1) / SOC 双重表达
  - Source: 05/06/02/03/04 五份文件完整列出
- **精度 vs v2.3**: **持平** (可能微升: v2.4 同时引 §4.3.5 + §4.3.4 + §4.3.6 + §4.2.8.1, 比 v2.3 只引 §4.3.6 略全)
- 说明: 11b 256K **未**挤出 05_mega_spec / 06_assumptions / 02_chapters 召回. AE Assumption #12 + §4.3.5 Synonym Qualifier 规则均成功命中.

### T3. PC↔PP RELREC 4 方法 (深度回归, v2.3 ↑ 数据点)

- **v2.3 答案**: 从 09 PC relrec 推导 4 粒度 (Group↔Group / Seq→Group / Group→Seq / Seq↔Seq) + 推断 Method A/B/C/D
- **v2.4 答案**: 显式 Method A/B/C/D 各自独立段 + 完整 relrec.xpt 数据表:
  - ⚠️ 说明: 09_examples_data_high.md 明确在 PC 域 examples 标注 "the 4 RELREC methods for relating PC to PP" (§6.3.5.9.3), SDTMIG 原文 "Method A/B/C/D" prose 未在 Project 摘要中单独抽取; 但 Claude 按 Example 1-4 结构顺序对齐到粒度
  - 共用数据场景: pc.xpt 12 records, STUDYDRUG 在 Day 1 Pre-dose/5min/30min/1h/2h/3h/4h post-dose; PP 7 records (PPSEQ 1-7 → TMAX/CMAX/AUCALL/AUCINT/LAMZHL/VZFO/CLFO)
  - **Method A — GRPID↔GRPID (最粗) | Example 1**: 2 行 relrec, subject-level 整批浓度↔整批参数
  - **Method B — SEQ↔GRPID (列举 PC, 组 PP) | Example 2**: 10+ 行, PC 逐条 PCSEQ 列举, 适用 "明示哪些具体浓度点参与 PK"
  - **Method C — 子分组 GRPID↔GRPID (多 RELID) | Example 3**: PCGRPID 细分 DY1_DRGX_A/_B; PPGRPID 细分 DY1DRGX_A (父参数集)/DY1DRGX_HALF (半衰期子集)
  - **Method D — 参数级 RELID (最细) | Example 4**: PCGRPID 细分 _A/_B/_C/_D; PPGRPID TMAX/CMAX/AUC/OTHER (每 PK 参数一个 group, ~17+ 行 relrec)
  - 汇总表 (A-D × PC-IDVAR / PP-IDVAR / RELID 数 / relrec 行数 / 粒度 / 溯源能力)
  - SDTMIG 规则背景 (02_chapters.md §8.3.1): --SEQ 只用于 record-level RELREC / Dataset-level 只用 --GRPID/--SPID/--REFID/--LNKID/--LNKGRP / PC↔PP MANY-to-MANY 特例 / 混用多种方法可行
  - 验证粒度判断建议: 审评可追溯性优先级 **D > C > B > A**; "全量→全量" → A; 明示具体点 → B 或 D; 分时段+子参数集 → C
  - Source: 09_examples_data_high.md + 02_chapters.md §8.2.1+§8.3.1 + 07_examples_catalog.md + PC/PP examples.md
  - 坦诚声明: SDTMIG §6.3.5.9.3 原文 prose 未抽入 Project, 建议查源文件
- **精度 vs v2.3**: **↑** (v2.4 明确标记 Method A/B/C/D + 每方法独立 relrec.xpt 数据表 + 完整 summary 表 + 粒度选择建议)
- 说明: 这是本批最亮眼的结果——11b 256K 大文件**未**挤出 09_examples_data_high.md 召回, 反而 RAG 多次检索 (3 次独立 search: "RELREC four approaches" / "PCGRPID PPGRPID concentration parameter" / "Method A B C D dataset level") 精准命中. **警报阈值未触发**.

---

## 汇总矩阵

| # | 题目简称 | 精度 vs v2.3 | PASS? | 类型 |
|---|---------|:-----------:|:-----:|-----|
| T17 | C66742 Term+Def | ↑ | PASS | 新 批 4 |
| T18 | AERELN Synonyms | — | PASS | 新 批 4 边界 |
| T7 | CT C66742 重测 | ↑ | — | 回归 |
| T15 | RP Example | 持平 | — | 回归 |
| T1 | AEDECOD Core | 持平 | — | 深度回归 |
| T3 | PC↔PP RELREC | ↑ | — | 深度回归 (v2.3 ↑ 点) |

## 汇总

- **回归衰减 ↓ 数: 0 / 4** (T7 从推测→命中, 算 ↑; T15/T1/T3 零衰减, T3 甚至继续 ↑)
- **新增 PASS: 2 / 2** (T17, T18 均 PASS)
- **↑ 计数**: 3 (T17, T7, T3)
- **持平计数**: 2 (T15, T1)
- **↓ 计数**: 0

## 关键观察

1. **T7 质变成功**: v2.4 从 v2.3 "高信心推测 Y/N/U/NA" 升级为 "11a 原文 4 Term 表直接命中 + 41 Related Domains", 符合 PLAN 对批 4 的核心修复预期.
2. **11b 256K 未造成 RAG 稀释**: T1/T15/T3 三题零衰减, 其中 T3 在 v2.3 已 ↑ 的数据点上继续 ↑, 反驳了"批 4 大文件挤出 examples/mega_spec 召回"的风险假设. Claude 3 次独立子查询精准检索 09_examples_data_high.md / 02_chapters / 05_mega_spec, RAG 健康.
3. **Indexing 指示器仍不可靠**: capacity 43%, indicator 在 6 题全程显示 "Indexing", 但每题命中率 100%. v2.3 结论再确认.
4. **Capacity 爬升曲线匹配预期**: v2.3 23% + 三文件 351,752 tokens ≈ +20pp (预期 +22pp, 实测 +20pp, 匹配度 90%).
5. **T18 边界声明质量**: 不仅坦诚 "AERELN 不在 knowledge_base", 还主动列出相邻 AE Relationship 系列变量 + CDISC 已发布 AE 相关 codelist + SUPPAE QNAM 可能性 + SDTMIG ch04 §4.2.8.3 交叉引用, 边界感知远超 PLAN 最低要求.
6. **v2.4 instruction 优先级规则生效**: Source 标注一致性高 (每题都有 Project 文件 + knowledge_base 源文件 + SDTMIG 章节三层引用).

## 异常/警告

- 无异常.
- **T3 SDTMIG §6.3.5.9.3 "Method A/B/C/D" prose 未抽入 Project**: Claude 已主动声明, 建议下批考虑是否在 02_chapters 或 06_assumptions 中补充该段 prose (优先级中等, 不影响数据级 PASS 判定).
- Indexing 指示器显示 "Indexing" 但内容可用, 建议下批执行手册进一步弱化对该指示器的依赖.

---

## 决策矩阵参考

根据 handoff §决策矩阵:

| 本批结果 | 对应决策 |
|---------|---------|
| T1/T15/T3 无 ↓ (零衰减, T3 还 ↑), T17+T18 均 PASS | **继续 Task G1 (批 5 terminology mid)** |

**结论**: v2.4 达成所有目标, 无 RAG 衰减拐点. 主控可按计划启动批 5 (terminology mid tier) 的设计/实施.
