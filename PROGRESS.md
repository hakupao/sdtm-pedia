# 进度看板

> 最后更新: 2026-04-13

## 总体状态

**项目已全部完成 ✓**

## 阶段进度

| # | 阶段 | 产出 | 状态 |
|---|------|------|------|
| 0 | 分析与方案设计 | `.work/analysis/` | **已完成** |
| 1 | xlsx 自动生成 | `domains/*/spec.md` + `terminology/` | **已完成** |
| 2 | PDF 页码索引 | `.work/page_index.json` | **已完成** |
| 3 | PDF 逐批提取 | `domains/*/assumptions.md` + `examples.md` | **已完成** (全部11批次) |
| 4 | 补充内容 | `model/` + `chapters/` | **已完成** |
| 5 | 验证与收尾 | 验证报告 + `INDEX.md` | **已完成** |

## Phase 1 明细

| 步骤 | 产出 | 状态 |
|------|------|------|
| Python 生成 spec.md（63 domain） | `domains/*/spec.md` (63个) | **已完成** |
| Python 生成 terminology/ | `terminology/core/` `questionnaires/` `supplementary/` (91个文件) | **已完成** |
| spec.md 自动校验 | 63 domain / 1917 变量 / 13419 字段 全部 PASS | **已完成** |

## Phase 3 批次明细

| 批次 | Class | Domain 数 | 状态 |
|------|-------|----------|------|
| 1 | Special Purpose | 5 (CO, DM, SE, SM, SV) | **已完成** |
| 2 | Interventions | 7 (AG, CM, EC, EX, ML, PR, SU) | **已完成** |
| 3 | Events | 7 (AE, BE, CE, DS, DV, HO, MH) | **已完成** |
| 4 | Findings General | 4 (DA, DD, EG, IE) | **已完成** |
| 5 | Specimen-based Findings | 7 (BS, CP, GF, IS, LB, MB, MS) | **已完成** |
| 6 | Specimen-based Findings 2 | 3 (MI, PC, PP) | **已完成** |
| 7 | Morphology/Physiology | 7 (CV, MK, NV, OE, RE, RP, UR) | **已完成** |
| 8 | Other Findings | 7 (PE, FT, QS, RS, SC, SS, VS) | **已完成** |
| 9 | Findings About | 2 (FA, SR) | **已完成** |
| 10 | Trial Design | 7 (TA, TD, TE, TI, TM, TS, TV) | **已完成** |
| 11 | Relationships + Study Ref | 5 (RELREC, RELSPEC, RELSUB, OI, SUPPQUAL) | **已完成** |
| — | TU/TR 补漏 | 2 (TU, TR) | **已完成** |

## Phase 6: 检索精度优化（TODO）

> 目标：提升 knowledge_base 的 AI 检索精度，减少幻觉

| # | 任务 | 说明 | 预估工作量 | 状态 |
|---|------|------|-----------|------|
| 6.1 | ROUTING.md 问题路由索引 | 创建问题类型→文件路径的路由规则，让 AI 按规则查找而非靠猜 | 1-2 小时 | 待开始 |
| 6.2 | 交叉引用 | 在每个 domain 文件末尾添加关联指针（相关 CT、关联 domain、通用规则等） | 3-4 小时 | 待开始 |
| 6.3 | 变量级反向索引 | 创建 VARIABLE_INDEX.md，建立变量名→domain→定义位置的映射表 | 半天 | 待开始 |
| 6.4 | 结构化元数据 | 将 spec.md 转为 YAML/JSON 元数据，支持程序化查询，为未来扩展打基础 | 数天 | 待开始 |

---

## 文件统计

| 类型 | 预计数量 | 已完成 | 质量问题 |
|------|---------|--------|---------|
| spec.md | 63 | **63** | 0 |
| assumptions.md | 63 | **63** | 0 |
| examples.md | 63 | **63** | 0 |
| terminology/ | 91 | **91** | 0 |
| model/ | 6 | **6** | 0 |
| chapters/ | 6 | **6** | 0 |
| INDEX.md | 1 | **1** | 0 |
| **总计** | **293** | **293** | **0** |
