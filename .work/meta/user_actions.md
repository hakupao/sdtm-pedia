# 用户操作指南

> 最后更新: 2026-04-28
> 项目状态: 知识库构建完成 + 检索优化完成 + 4 平台 AI 部署完成 + Release v1.0 公司发布版交付

---

## 项目完成总结

### 知识库（2026-04-13 完成 / 2026-04-16 验证关门）

共产出 **293 个 Markdown 文件** + 检索优化产物（ROUTING.md + VARIABLE_INDEX.md + 域间 Cross References）。

| 类别 | 数量 | 说明 |
|------|------|------|
| spec.md | 63 | 从 xlsx 自动生成，已通过自动校验 |
| assumptions.md | 63 | 从 PDF 提取（11 批次 + TU/TR 补漏） |
| examples.md | 63 | 从 PDF 提取（11 批次 + TU/TR 补漏） |
| terminology/ | 91 | 从 xlsx 自动生成（core/questionnaires/supplementary） |
| model/ | 6 | 从 SDTM v2.0 PDF 提取 |
| chapters/ | 6 | 从 SDTMIG v3.4 PDF 提取 |
| INDEX.md | 1 | 全局索引（Phase 5） |
| ROUTING.md | 1 | 问题路由索引（Phase 6.1） |
| VARIABLE_INDEX.md | 1 | 变量级反向索引（Phase 6.3，1,523 变量） |

知识库质量问题：**0**（详见 `.work/meta/findings.md`）。

### AI 平台部署（2026-04-27 完成）

4 个 AI 平台全部完成 Phase 5 sign-off：

| 平台 | 状态 | 文件 |
|------|------|------|
| Claude Projects | v2.6 终态（24/24 A/B PASS, capacity 77%） | 19 上传 |
| ChatGPT GPTs | Phase 5 完成（v2.2 system prompt） | 9 上传 |
| Gemini Gems | Phase 5 完成（v7.1 system prompt） | 4 上传 |
| NotebookLM | Phase 5 完成（Custom mode 8,925 chars） | 42 上传 |

### 07 Release v1.0（2026-04-27 交付）

公司发布版打包：`ai_platforms/release/v1.0/`（自包含 26M，4 平台 deploy bundle）

| 内容 | 数量 |
|------|------|
| 顶层文档 | 12（README × 3 + USER_GUIDE × 3 + GLOSSARY × 3 + DEMO_QUESTIONS + KNOWN_LIMITATIONS.en + CHANGELOG） |
| self_deploy 文档 | 15（README × 3 + 4 平台 tutorial × 3） |
| 4 平台 deploy bundle | 75 上传 + 各自 system_prompt 或 instructions |

git tag：`v1.0-company-release`

---

## 后续可选操作

### 1. 公司发布版分发（推荐）

把 `ai_platforms/release/v1.0/` 整目录上公司云盘 / 内部文档站，同事自助选平台部署。
入口：`ai_platforms/release/v1.0/README.zh.md` → `self_deploy/README.zh.md` 决策树 → `self_deploy/<平台>/tutorial.zh.md` 跟做。

### 2. 直接挂载 Claude Code

将 Claude Code 指向 `knowledge_base/` 目录即可，会通过 `INDEX.md` + `ROUTING.md` 自动导航。

### 3. 精度抽查（如需）

- 抽查 2-3 个 `assumptions.md`，与 PDF 对应页码逐条对照
- 抽查 2-3 个 `examples.md`，重点检查数据表格完整性
- 页码映射参见 `.work/02_indexing/page_index.json`
- 系统级深审进行中：`.work/06_deep_verification/`（atom 级 PDF→KB 字面对照，~340 / 535 页完成）

### 4. Phase 7 RAG + 知识图谱（待实施）

设计文档：`docs/DESIGN_RAG_KG.md`。一期 RAG + 数据集校验、二期知识图谱 + 混合路由。

---

## 参考文件

| 文件 | 内容 |
|------|------|
| `docs/PROGRESS.md` | 总体进度看板 |
| `.work/MANIFEST.md` | 文件清单与变更链 |
| `.work/progress.json` | 程序化进度追踪（Phase 1-5） |
| `.work/meta/worklog.md` | 完整工作日志（含 06 旁枝 + 07 Release） |
| `.work/meta/retrospective.md` | 阶段性反思 + 四条预防规则（必读） |
| `.work/meta/findings.md` | 质量问题记录（0 个问题） |
| `.work/meta/mapping.md` | 源文件→输出文件映射 |
| `.work/00_planning/restructure_plan.md` | 完整方案文档 |
| `.work/07_release/PLAN.md` | Release v1.0 计划 |
| `.work/07_release/RETROSPECTIVE.md` | Release v1.0 复盘（Rule C 三段） |
| `ai_platforms/release/v1.0/CHANGELOG.md` | Release 历史 |
| `ai_platforms/release/v1.0/KNOWN_LIMITATIONS.en.md` | 已知限制 |
