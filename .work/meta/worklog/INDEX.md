# Worklog Index — 按 phase 拆分入口

> 本目录为 `.work/meta/worklog.md` 重构后产物 (refactor v1 段 2 close 2026-05-06). 原单文件 2498 行已按以下方式拆分:
>
> - **历史段 (frozen)**: `historical_2026_04.md` — 原 worklog.md 的 lines 207-1936, 涵盖 Phase 0-4 generation + Phase 5 verification + Phase 6 P0-P2 + Phase 7 design + Phase 6.5 Claude/NotebookLM. 不再写入.
> - **活跃 phase 文件**: 按主题拆分, 新 entry append 到对应文件.
> - **元数据**: `_meta.md` — 原 worklog.md 的 header (恢复指引 + 项目参数 + 执行阶段 + 工作记录 H1).

## 文件清单

| 文件 | 主题 | 行数 | 最新 entry | 写入策略 |
|------|------|------|------------|----------|
| `_meta.md` | 恢复指引 + 项目参数 + 执行阶段总览 | 206 | (元数据) | 仅在阶段总览变化时改 |
| `historical_2026_04.md` | Phase 0-4 + Phase 5 + Phase 6.5 + Phase 7 design (frozen) | 1738 | 2026-04-28 | **不要 append**, frozen 历史 |
| `phase06_deep_verification.md` | 06 字面级 PDF→KB 深审 (P1 close + P2 进行中) | 448 | 2026-05-05 | 06 round/batch close 时 append |
| `phase07_website.md` | 07 公开发布版站点 (sdtm-pedia.pages.dev) | 40 | 2026-04-28 | 07 phase close 时 append (Phase 6/7/8/9/10/11 已 closed) |
| `phase_07_release.md` | 07 Release v1.0 + v1.1 (公司发布版 release/) | (new) | 2026-05-15 | release cut 时 append |
| `phase_jp_delivery.md` | docs/jp/ iTMS 様 納品 (Chain J) | 98 | 2026-06-15 | **FROZEN** — 线 CLOSED 冻结, 不再 append |
| `phase_07_rag_kg.md` | Phase 7 RAG+KG 旁枝 (milestones/07_rag_kg/, Chain 07_RAG) | (新生成 2026-05-22) | 2026-06-16 | Phase close 时 append |
| `phase_meta_refactor.md` | refactor v1 段 1/2/3 (Chain REFACTOR-v1) | (生成) | 2026-05-06 | 段 close 时 append, 段 3 close 后可归档 |

## 按 Phase 反向查找

| 项目 Phase | 主要文件 | 备注 |
|------------|----------|------|
| Phase 0 (planning) | `historical_2026_04.md` | 早期方案, frozen |
| Phase 1 (generation) | `historical_2026_04.md` | xlsx 自动生成, frozen |
| Phase 2 (indexing) | `historical_2026_04.md` | PDF 页码索引, frozen |
| Phase 3-4 (extraction) | `historical_2026_04.md` | PDF 提取, frozen |
| Phase 5 (verification) | `historical_2026_04.md` | Step 0-4 + Issue 2/3/4 修复, frozen |
| Phase 6 (optimization) | `historical_2026_04.md` | P0-P2 完成, frozen; P3 → Phase 7 |
| Phase 6.5 (AI 平台部署) | `historical_2026_04.md` + `phase_07_release.md` | **线 CLOSED 冻结** 2026-06-15 (4 平台 signed-off + Release v1.4) |
| Phase 7 (RAG + KG) | `historical_2026_04.md` | 设计完成, 实施待启 |
| 06 旁枝 (Deep Verification) | `phase06_deep_verification.md` | P7 COMPLETE 2026-05-12 |
| 07 旁枝 (RAG+KG) | `phase_07_rag_kg.md` | **active** — Phase 0 closed 2026-05-22 |
| 07 旁枝 (Website) | `phase07_website.md` | Phase 6/7/8/9/10/11 closed |
| 07 Release (公司发布) | `phase_07_release.md` | **CLOSED 冻结** — v1.0-v1.4 全 closed (tag v1.4-company-release) |
| docs/jp 旁枝 | `phase_jp_delivery.md` | **CLOSED 冻结** 2026-06-15 — 停于 P0 2/4 + 01 v1.1-draft |
| refactor v1 (临时) | `phase_meta_refactor.md` | 段 2 close 2026-05-06 |

## 写入约定

1. **新 entry 格式**: `## YYYY-MM-DD <topic> <verb>` (H2), 内部用 H3 列细节
2. **大事件 (cycle close, milestone)** 单独成条
3. **小修小补** 可合并到当日条目末尾
4. **不要往 `historical_2026_04.md` 写** — 它是 frozen 历史, 改它会破坏溯源
5. **链路同步** 见 `.work/MANIFEST.md` Chain B
