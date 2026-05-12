# P5 反向比对 初始报告

> 生成时间: 2026-05-12
> 阶段: P5 reverse matching (MD → PDF)
> 脚本: scripts/p5_reverse_match.py v1.1

## 数据概况

| 指标 | 值 |
|---|---|
| 总 MD 原子数 | 10,435 |
| 总 reverse_ledger 条目 | 10,435 (100%) |
| reverse_ledger 文件 | reverse_ledger.jsonl |

## P5 分类结果

| Verdict | 数量 | % | 说明 |
|---|---|---|---|
| SOURCED | 5,548 | 53.2% | P4a EXACT/EQUIVALENT 命中 |
| SYNTHESIZED | 3,172 | 30.4% | 自动规则分类 |
| UNSOURCED_CANDIDATE | 928 | 8.9% | 待 agent 审查 |
| SOURCED_PARTIAL | 545 | 5.2% | P4a PARTIAL 命中 |
| SOURCED_P4A_MISSED | 121 | 1.2% | Fuzzy lookup 补回 |
| SOURCED_MISPLACED | 108 | 1.0% | P4a MISPLACED 命中 |
| SOURCED_ERROR | 13 | 0.1% | P4a ERROR 命中 |

**SOURCED 合计**: 6,335 (60.7%)

## SYNTHESIZED 自动规则详情

| 规则 | 说明 | 预估数量 |
|---|---|---|
| auto:synthesized_file | VARIABLE_INDEX.md / INDEX.md / ROUTING.md | ~1,840 |
| auto:synthesized_type:HEADING | 结构标题锚点 | 227 |
| auto:synthesized_type:TABLE_HEADER | 表列头 | 254 |
| auto:synthesized_type:FIGURE | Mermaid 图 | 18 |
| auto:synthesized_type:CROSS_REF | 交叉引用 | 1 |
| auto:examples_data_row | 示例数据集行 (≥5 管道符) | ~510 |
| auto:source_header_annotation | "Source: SDTMIG v3.4…" 元数据行 | ~100 |
| auto:bold_only_nav_anchor | `**section title**` 导航锚 | ~150 |
| auto:domain_spec_overview_header | domain.xpt overview 行 | ~72 |

## UNSOURCED_CANDIDATE 分布 (928 个)

### 按 atom_type
| 类型 | 数量 |
|---|---|
| SENTENCE | 421 |
| TABLE_ROW | 345 |
| LIST_ITEM | 115 |
| NOTE | 44 |
| CODE_LITERAL | 3 |

### 按文件 (top 15)
| 文件 | 数量 | 风险 |
|---|---|---|
| model/02_observation_classes.md | 129 | MEDIUM (sv20 adapted) |
| chapters/ch04_general_assumptions.md | 120 | HIGH (ig34 content) |
| chapters/ch08_relationships.md | 93 | HIGH (ig34 content) |
| domains/PC/examples.md | 63 | LOW (example narrative) |
| model/06_relationship_datasets.md | 52 | MEDIUM (sv20 adapted) |
| model/05_study_level_data.md | 51 | MEDIUM (sv20 adapted) |
| model/03_special_purpose_domains.md | 43 | MEDIUM (sv20 adapted) |
| domains/MB/examples.md | 34 | LOW |
| model/01_concepts_and_terms.md | 31 | MEDIUM (sv20 adapted) |
| domains/AE/examples.md | 24 | LOW |

## 方法论

### 分类算法 (4 步)

1. **reverse_idx lookup** (from coverage_ledger): md_atom_id 出现在任何 pdf_atom 的 md_atom_ids → SOURCED/PARTIAL/MISPLACED/ERROR
2. **Auto-SYNTHESIZED rules**: 文件类型 + atom_type + verbatim 模式 → SYNTHESIZED
3. **Fuzzy lookup**:
   - Step 3a: 同 parent_section fuzzy (threshold 0.65)
   - Step 3b: 全量 sv20 global fuzzy (model/* 文件)
   - Step 3c: 章节 prefix ig34 pool (chapters/* 文件)
4. **UNSOURCED_CANDIDATE**: 上述均未命中 → 待 agent 审查

### SOURCED_P4A_MISSED 说明

121 个原子经 fuzzy 补找有 PDF 源。这些是 P4a 的 false negative（即 P4a 未能把这些 PDF atoms 匹配到这些 MD atoms）。P4a 质量问题，非内容问题。

## 下一步

1. Rule A 独审 (oh-my-claudecode:scientist, 100 atoms, running) → ≥95% gate
2. UNSOURCED_CANDIDATE 批次审查 → 分类 SYNTHESIZED/SOURCED/UNSOURCED/HALLUCINATED
3. HALLUCINATED → 开 Issue 5+ (HIGH)
4. Rule D gate reviewer 确认
5. trace.jsonl P5 phase_report

## 初步风险评估

基于样本观察，UNSOURCED_CANDIDATE 主要由两类组成：
- **SYNTHESIZED_ADAPTED** (预期 ~70%): KB 作者对 sv20/ig34 内容的改写/摘要，非 verbatim 复制
- **SOURCED_P4A_MISSED_BELOW_THRESHOLD** (预期 ~25%): 有 PDF 源但 fuzzy similarity < 0.65
- **GENUINELY_UNSOURCED** (预期 <5%): 合理编辑添加内容
- **HALLUCINATED** (预期 ~0%): 目前样本中未见

