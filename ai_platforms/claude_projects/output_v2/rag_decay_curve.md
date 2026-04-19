# RAG 质量 vs 规模曲线 (Phase 6.5 v2 一等产物)

> 目标: 建立 Claude Project RAG 质量随集合规模变化的曲线
> 用途: Phase 7 RAG 拓扑设计参考 + 决定是否在 Phase 6.5+ 推到 70%
> 触发: capacity_research §6.3 第 2 条疑点 ("RAG 检索质量随集合增大如何衰减?" 未实测)

## 数据点

| 阶段 | tokens (9 实体) | 文件数 | Capacity % (UI 实测) | T1-T8 PASS | T9-T20 PASS | 平均答题精度 (主控判) |
|------|---------------:|-------|---------------------|-----------|-----------|----------------------|
| v1   | 192,036 | 11 (9 实体 + system_prompt + upload_manifest) | 12% | 8/8 | N/A | baseline |
| v2.1 | **205,895** | **11** (9 实体 + 2 meta, 与 v1 同文件数, 02_chapters 替换为全展开) | **13%** | **7/8** (T3 ↓) | **T9-T12: 4/4 PASS** | **5 ↑ / 2 持平 / 1 ↓** (T1-T8) |
| v2.2 | **318,592** (+112.7K 09) | **10 实体** (12 含 meta) | **20%** | **7/8** (T1 持平, T3 ↓ 未修, 余同 v2.1) | **T13-T14: 2/2 PASS ↑** | **T13/T14 ↑, T1/T11 持平, 0 衰减** |
| v2.3 | **367,489** (+48.9K 10) | **11 实体** (13 含 meta) | **23%** | **7/8** (T3 ↓→改善: v2 累积视角 **转 PASS**) | **T15-T16: 2/2 PASS ↑** | **T15/T16 ↑, T3 ↑ 显著, T11 持平略 ↑, 0 衰减** |
| v2.4 | **719,241** (+351.8K 11a/b/c) | **14 实体** (16 含 meta) | **43%** | **8/8** (T1/T3/T15 零衰减, T7 从推测→11a 原文命中 ↑) | **T17-T18: 2/2 PASS ↑** | **T17/T7/T3 ↑, T15/T1 持平, 0 衰减** |
| v2.5 | TBD (+12) | 16-19 | TBD | TBD | T19-T20 TBD | TBD |

## 观察

**v2.0→v2.1 (chapters 全展开)**:
- Token 增量 +7.2% (192K → 205.9K), capacity 增 +1pp (12% → 13%). 子线性关系确认 RAG 容量桶化/分块显示.
- T9-T12 全 PASS 证明 **byte-exact 章节展开路径有效** — v2 能精确引用 §4.4.8/§2.6 SA/SQ/§1.5 等 v3.4 新增或细节条目, 这些是 v1 压缩版 structural 丢失.
- T11 **主动检出虚构 §3.1.2.2** 是 chapter 全展开独有能力 — v1 无完整 TOC, 不可能做 section 存在性校验.
- T3 单点衰减的原因是 §6.3.5.9.3 PC↔PP examples 仍未收录 (v2.1 只展开 chapters, 未展开 examples); v2.1 边界模板因此触发拒答。**不是 RAG 衰减, 是覆盖缺口.** Batch 2 (v2.2) 将补齐该区域.
- T2/T4/T7/T8 的 ↑ 均来自 chapter 章节锚点精确化 (§4.2.1/§4.3.6/§8.6.3/§4.1.3.1/§4.3.7), 证明 RAG 能同时命中章节原文 + mega_spec 表格, 未出现"新文件挤掉旧文件"的相互竞争.

**v2.2→v2.3 (examples 其余 35 域 +48.9K 10 文件)**:
- Token 增量 +15.3% (318.6K → 367.5K), capacity 增 +3pp (20% → 23%). 比例匹配 (3pp/7pp ≈ 48K/112K ≈ 0.43), 子线性趋势继续.
- T15 (RP) / T16 (FT) 均命中 10_examples_data_others.md, 完整 rp.xpt (21×18) / ft.xpt (6×16) + suppft.xpt (1×10) 返回. 63 SDTM 域 examples 侧覆盖率 **0 → 100%** (批 2 的 28 + 批 3 的 35).
- "09 > 10 > 07" Instructions 优先级被 Claude 正确解读, RP/FT 不在 09 时自动回落 10, 无一 fallback 到 v1 源路径模板.
- **T3 正向数据点 (跨批累积激活)**: v2.1/v2.2 因 §6.3.5.9.3 narrative 未收录硬拒答, v2.3 在 Instructions 未变的情况下突破, 能:
  - 保持边界诚实 (明标 Chapter 6 narrative 不在 Project, Method A-D 官方命名属推断)
  - 从 09 (批 2 D2 上传) 的 PC relrec 数据自主推导 4 种粒度结构 (Group↔Group / Seq→Group / Group→Seq / Seq↔Seq) + dataset-level 附录, 共 5 张完整 relrec.xpt
  - 推断 Method A/B/C/D 映射并声明需原文校验
  → RAG 不是被动"查哪个文件", 当多批累积后, 模型**自发跨文件重建缺失 narrative 的能力被激活**. 解读: 批 2 的 09 把 PC 数据铺进 RAG, 批 3 的 10 + Instructions 升级触发召回广度扩张, Claude 从"拒答"切到"从数据推导". 这是 RAG decay curve 的**正向二阶效应**.
- T11 (回归, 基于 02_chapters.md): 持平略 ↑, 多了 --SEQ 禁用原文直引 ("only has meaning within a subject within a dataset") + 来自 09 的 TR Example 2 (USUBJID=44444, TULNKID=T01, 17mm→0mm→0mm) 作交叉佐证. 多文件协同 (02+09+06+03) 正常, 48.9K 新文件对 02/05/06 老文件无挤出.
- Indexing indicator 在 v2.3 仍不可靠 (显示 "Indexing" 但提问立即命中), 沿用 v2.2 结论.

**v2.3→v2.4 (terminology high top 200 codelist 完整 Term, +351.8K 11a/b/c 三文件)**:
- Token 增量 +95.7% (367.5K → 719.2K, 本批是 v2 token 跃升最大阶段), capacity 增 +20pp (23% → 43%). 比例匹配 (20pp/3pp ≈ 351.8K/48.9K ≈ 7.2x), +20pp 实测 vs +22pp 投影 = ~91% 吻合, 无 RAG 结构异常.
- **T17 (C66742 Term 表, 批 4 核心修复目标) 质变 PASS**: v2.1/v2.2/v2.3 三连高信心推测 Y/N/U/NA (因 08 只映射), v2.4 在 11a rank 1 直接命中完整 4 Term 表 (C49487 N / C48660 NA / C17998 U / C49488 Y) + 41 Related Domains 行 + Extensible No. Source 标 `11a_terminology_high_core.md`. 从 "推测" 跃升为 "原文命中", PLAN §F4 对批 4 的修复期望完美达成.
- **T18 (AERELN, 批 4 边界测试) 质变 PASS**: F1 audit 已确认 AERELN 不在 knowledge_base 源, v2.4 坦诚声明 "AERELN 不是 SDTMIG v3.4 标准变量/codelist" + 列相邻 AE Relationship 系列变量 (AEREL/AERLDEV/AERELNST/AERLPRT/AERLPRC 全部 "无 CDISC CT") + 引 AE 域已发布 codelist (C66767/C66768/C66769/C111110) + SUPPAE QNAM 可能性 + ch04 §4.2.8.3 交叉引用. 零臆造 Synonyms, 边界感知远超 PLAN 最低要求.
- **T3 跨批累积三阶正向激活**: v2.2 硬拒答 → v2.3 从 09 数据推导 4 粒度 + 推断 Method A/B/C/D (保边界) → v2.4 **显式 Method A/B/C/D 独立段 + 每方法完整 relrec.xpt 数据表 + A-D 汇总矩阵 (IDVAR/RELID 数/relrec 行数/粒度/溯源能力) + 粒度选择建议 (D>C>B>A)**. Claude 3 次独立子查询精准命中, 11b 256K 大文件**未**挤出 09 召回. 这是 v2 最显著的 RAG 跨批累积正向二阶效应.
- **11b 256K 单文件挤出风险假设被反驳**: T1 (AEDECOD Core, 敏感度最高的深度回归) 持平或略 ↑ — v2.4 同时引 §4.3.5 (Synonym Qualifier for MedDRA/WHODrug) + §4.3.4 + §4.3.6 + §4.2.8.1 + AE Assumption #12, 比 v2.3 仅 §4.3.6 更全. T15 (RP 21×18 rp.xpt) 完整命中 10, 零衰减. 11b 256K 是当前 v2 单文件 token 最大记录 (vs v2.3 最大 112.7K 09), 未造成 RAG 稀释.
- Source 溯源一致性保持: 每题 "Project 文件 + knowledge_base 源文件 + SDTMIG 章节" 三层引用, CT Code 查询优先级规则 `11*>08` (v2.4 新 Instructions 段) 被 Claude 正确解读.
- Indexing indicator 在 v2.4 仍不可靠 (指示器持续显示 "Indexing" 但 6/6 题立即命中), 沿用 v2.2/v2.3 结论. PLAN §Step 4 对 "11b 256K tokens, indexing 可能 >30 分钟" 的风险预警未触发.

## 结论 (终态后填)

- v2 终态推到 X% 的 RAG 质量是否仍 PASS?
- 衰减拐点 (如有) 在 ~Y% capacity?
- 对 Phase 7 的 actionable insight?
