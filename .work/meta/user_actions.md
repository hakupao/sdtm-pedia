# 用户操作指南

> 最后更新: 2026-04-15
> 项目状态：知识库构建已完成，验证 Step 0-3.6 完成，Step 4 (汇总报告) 待执行

---

## 项目完成总结

知识库构建已于 2026-04-13 全部完成，共产出 293 个 Markdown 文件。

| 类别 | 数量 | 说明 |
|------|------|------|
| spec.md | 63 | 从 xlsx 自动生成，已通过自动校验 |
| assumptions.md | 63 | 从 PDF 提取（11 批次 + TU/TR 补漏） |
| examples.md | 63 | 从 PDF 提取（11 批次 + TU/TR 补漏） |
| terminology/ | 91 | 从 xlsx 自动生成（core/questionnaires/supplementary） |
| model/ | 6 | 从 SDTM v2.0 PDF 提取 |
| chapters/ | 6 | 从 SDTMIG v3.4 PDF 提取 |
| INDEX.md | 1 | 全局索引 |

质量问题：**0**

---

## 后续可选操作

### 精度抽查

如需进一步验证内容精度，建议：
- 抽查 2-3 个 `assumptions.md`，与 PDF 对应页码逐条对照
- 抽查 2-3 个 `examples.md`，重点检查数据表格完整性
- 页码映射参见 `.work/02_indexing/page_index.json`

### 搭建 Claude Project

参见 `docs/claude_project_setup.md` 和 `docs/claude_project_instructions.md`。
> 注意：这两个文件引用的是旧版 `project_knowledge_base/` 结构，如需使用新版 `knowledge_base/` 结构上传到 Claude Project，需要更新文件引用。

---

## 参考文件

| 文件 | 内容 |
|------|------|
| `docs/PROGRESS.md` | 总体进度看板 |
| `.work/progress.json` | 程序化进度追踪 |
| `.work/meta/worklog.md` | 完整工作日志 |
| `.work/00_planning/restructure_plan.md` | 完整方案文档 |
| `.work/meta/findings.md` | 质量问题记录（0 个问题） |
| `.work/meta/mapping.md` | 源文件→输出文件映射 |
