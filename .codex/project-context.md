# Project Context

## Goal

将 CDISC SDTM 源文件转换为结构化 Markdown 知识库，供后续检索、映射和规则查询使用。

## Source Of Truth

- `source/SDTMIG_v3.4.xlsx`
  - 已生成 `knowledge_base/domains/*/spec.md`
  - 已生成 `knowledge_base/terminology/**/*`
- `source/SDTMIG v3.4 (no header footer).pdf`
  - 已生成 `knowledge_base/domains/*/assumptions.md`
  - 已生成 `knowledge_base/domains/*/examples.md`
  - 已生成 `knowledge_base/chapters/*`
- `source/SDTM_v2.0.pdf`
  - 已生成 `knowledge_base/model/*`

## Confirmed Status

**项目已全部完成 ✓**（2026-04-13）

- `spec.md` 已有自动校验脚本：`.work/scripts/validate_spec.py`，63 domain / 1917 变量 / 13419 字段全部 PASS
- `terminology/` 已生成 91 个文件（core 42 + questionnaires 43 + supplementary 6）
- `assumptions.md` + `examples.md` 已完成全部 63 domain（11 批次 + TU/TR 补漏）
- `model/` 已完成 6 个文件（SDTM v2.0 全部章节）
- `chapters/` 已完成 6 个文件（SDTMIG v3.4 通用章节）
- Phase 5 全量验证通过，INDEX.md 已生成

## Current Output Snapshot

- 全部 63 个 domain 均已包含完整三件套（`spec.md` + `assumptions.md` + `examples.md`）
- 产出文件总计：293 个（63 spec + 63 assumptions + 63 examples + 91 terminology + 6 model + 6 chapters + 1 INDEX.md）
- 质量问题：0

## Review Priority

如需后续精度审计，优先级从高到低：

1. `assumptions.md`
2. `examples.md`
3. `terminology/**/*`
4. `spec.md`（已有强校验，优先级最低）
