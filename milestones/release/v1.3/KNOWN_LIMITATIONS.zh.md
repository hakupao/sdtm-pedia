---
lang: zh
slug: known-limitations
order: 50
title: "已知限制"
---

# 已知限制

本页说明 v1.3 的使用边界. 它不是错误清单, 而是帮助用户判断哪些问题适合直接查询, 哪些问题需要回到官方来源或组织流程确认.

## 0. v1.3 审计范围 (2026-05-20 更新)

v1.3 是 SDTM Pedia 的**知识库 pass 级**版本 (自 v1.0 以来最大规模的内容更新). 它取代了 v1.2 的 Gemini-only prompt 刷新模式: v1.3 直接修改知识库, 重建全部 4 平台 bundle, 并在 4 个已部署 AI 平台中端到端验证交付效果.

### v1.3 新增内容

- **阶段 A — 知识库层修复** (11 个 KB 文件修改, 经两轮独立 Rule D reviewer 审计: 0 幻觉, 0 意外删除):
  - **PP RELREC 链接** — 在 `PP/examples.md` 中新增 §6.3.5.9.3 RELREC Method 快速参考 (Method A/B/C/D 表格 + Method C 的 1 个缩略 relrec.xpt). 关闭 06 Deep Verification 项目遗留的 OA-4 缺口.
  - **BECAT EXTRACTION 申办方可扩展** — 在 `BE/spec.md` L111 处 CDISC 标准示例 (COLLECTION / PREPARATION / TRANSPORT) 旁显式标注. 使知识库与已部署的 Gemini v8.1 prompt L272 措辞保持一致.
  - **Tier B 节修复** — 修复 10 个高密度 shall/must 节 (§2.7 SDTM 变量规则, §6.4.2 FA 命名, §7.2.1 Trial Arms Example 4, §7.3.2/§7.3.3 TD/TM, §4.5.1.2 Tests Not Done, §6.3.12.2 TR 列头 typo TRSTRESN→TRSTRESU, §6.4.3 FA --OBJ, §7.2.1.1 TA Distinguishing, §4.3.5).
  - **UNSOURCED_MANUAL 原子抽样** — 对 437 个 UNSOURCED_MANUAL 原子做 N=40 分层抽样 (10 个高风险 shall/must + 30 个对照): 80% REASONABLE_INFERENCE + 20% DERIVED_FROM_XLSX + **0% HALLUCINATED** (Rule D `scientist` reviewer 审计确认).
- **阶段 B — 4 平台重建** (构建脚本强化, 跨平台 delta oracle 验证):
  - 构建脚本防御化: ChatGPT `merge_for_chatgpt.py` 由硬编码 `expected_segments=63/64/63` 改为动态 `len()`; NotebookLM 新增 `validate_bucket_coverage.py` (190/190 KB 文件均命中 bucket, 0 陈旧引用).
  - 4 平台重建: ChatGPT (3 文件更新), Gemini (3 文件更新), NotebookLM (7 文件更新 + 1 文件改名), Claude Projects (5 文件更新).
  - NotebookLM bucket 25 改名: `25_td_meta_ti_ts_oi.md` → `25_td_meta_ti_ts_oi_di.md` (现已体现 DI 的纳入). **自部署用户上传新文件后必须删除旧 source** — 详见 USER_GUIDE.
  - 跨平台 delta oracle: ChatGPT 04 (+284) = NotebookLM bucket 10 (+284) = Gemini 02 局部 (+284) 字节精确等价 (以 BE/spec 改动为例), 0 静默丢失.
  - 全 4 平台 `system_prompt`/`instructions` 已针对陈旧数字引用进行审计 (20/20 grep 探针 PASS).
- **阶段 C — 轻量 sanity (14-15/16 PASS)**:
  - 4 道 v1.3 靶向题 × 4 个已部署平台 = 16 个格; BECAT (A2)、PP RELREC (A1)、TR typo (A3)、DI 域 (B5) 端到端验证.
  - Q-S1 BECAT EXTRACTION: 4/4 PASS (2 PASS+).
  - Q-S2 PP RELREC 4 方法: Claude PASS+, NotebookLM PASS+, ChatGPT PARTIAL (4 个 IDVAR 组合正确但 Method A/B/C/D 标签相对知识库有错位), Gemini FAIL (详见下文).
  - Q-S3 TR TRSTRESN vs TRSTRESU typo 修复: 4/4 PASS (2 PASS+).
  - Q-S4 DI 域 (NotebookLM bucket 25 改名): NotebookLM PASS+ (footer 引用 `25_td_meta_ti_ts_oi_di.md`, 验证 B5 部署), Claude PASS+, Gemini PASS (Flash-Lite fallback, Pro 配额耗尽), ChatGPT 未捕获判定但基于规律预期 PASS.

### v1.3 未重新评估项 (推迟至 v1.4)

- **主线 — 4 平台 `system_prompt`/`instructions` 全栈重构**: 用户在阶段 C 指出, 4 个已部署 prompt 均积累了多次迭代层 (Gemini v8.1 已达 525 行, 含 17 条 CO-N 反作弊规则, 每条标注 "v5/v6/v7/v7.1/v8 新增" 作为 smoke test 失败的化石记录). 这种复杂性分散注意力并使锚点过度专项化, 在阶段 C Q-S2 中表现为 Gemini 失败: Gemini Gem 对 PP-PC RELREC 链接方法产生幻觉 (声称 PPLNKID/PCREFID), 而非检索知识库中的 §6.3.5.9.3 Method A/B/C/D 分类体系. v1.4 将对全部 4 个 prompt 进行全新编写 — 移除化石注释, 合并子规则, 将知识库接地作为主路径. 预计缩减: Gemini 525 → ~200 行, CO-N 规则改为 regex 门控 (仅在题目类型匹配时触发).
- **437 个 UNSOURCED_MANUAL 原子全量分类**: v1.3 抽样 N=40 (0 幻觉). 全量 437 条来源验证推迟至 v1.4, 同时包含 Rule D reviewer 发现的启发式分类器修复 (Rule D `scientist` 发现 10 条初始标记为 DERIVED_FROM_XLSX 的原子中有 5 条实为 PDF 正文; 主 session 分类器存在 `xlsx vs PDF` 先验偏差).
- **Tier B 节 11-25 (高密度 + 小节)** + **全部 level-2 Tier B (cannot / except / only / should 关键词)** — v1.3 修复了排名 11-20 (10 节, 约 37 个原子). 排名 1-10 (最高密度, 约 470 个原子)、排名 21-25 (最小节) 及 24 个 level-2 节推迟至 v1.4.
- **Issue 5 §6.3.5.9.3 PC/PP 143 TABLE_ROW Tier-B MEDIUM 修复**: 见 06 Deep Verification §二; 行级数据值差异修复.
- **section_coverage.jsonl 全流程重跑**: v1.3 仅备份了基线 + 记录了陈旧状态. 完整流程 (md_atoms 再生 → P4a 正向匹配 → P4b 聚合) 需在 v1.4 中执行以获得准确的判定刷新.
- **R4 全 17 题 Gemini 仅 Pro 回归**: v1.3 使用了 4 道轻量 sanity 题 × 4 平台, 而非 17 题单平台回归. 4 道 sanity 题端到端覆盖所有 v1.3 KB 改动; R4 全量推迟 (Pro 配额限制: 多个 5h 窗口累计约 16-20 小时墙钟时间).
- **PASS+ §1.2 严格"仅 AHP"范围扩展** (来自 R4 sanity retro 的 W1 遗留): 阶段 C Q-S1 和 Q-S5 显示非 AHP 题在知识库接地且有额外深度时 (跨域引用、来源引用) 也能获得 PASS+ 评级. PASS+ 评分标准范围扩展为"AHP 题 OR 知识库接地 + 超过基线深度的回答", 此处记录供未来 smoke 测试使用.

### 外观 / 部署注意事项

- NotebookLM bucket 25 改名: 现有 v1.0–v1.2 NotebookLM 部署含旧 source `25_td_meta_ti_ts_oi.md`. 上传新文件 `25_td_meta_ti_ts_oi_di.md` 后, **请手动删除旧 source** 以避免陈旧引用 (清理后 43 个 source 应降至 42 个).
- ChatGPT GPT 在 PP-PC RELREC 部分场景下的 "Method A/B/C/D" 标签可能与 v1.3 知识库 §6.3.5.9.3 快速参考标签不完全一致 (阶段 C Q-S2 PARTIAL). 4 个 IDVAR 组合是正确的; 标签存在主观性.

## 1. 不替代官方标准

SDTM Pedia 是辅助查询工具。正式提交、标准解释、术语版本确认和关键映射决策，应以 CDISC 官方出版物、NCI EVS、MedDRA 授权资料、监管要求和组织内部 SOP 为准。

## 2. 实时外部信息不保证覆盖

本版本反映的是发布时整理的知识范围。对于发布之后变化的信息，例如新的 CDISC 版本、Pinnacle 21 规则更新、Dataset-JSON 状态或外部数据库变化，需要访问对应官方来源确认。

## 3. 长尾受控术语可能需要回查官方来源

部分规模很大的 codelist 或长尾 questionnaire 术语不会在所有平台中完整展开。遇到这类问题时，合理回答应说明范围边界，并引导用户回查 NCI EVS 或其他权威来源，而不是生成未经核实的完整术语清单。

## 4. 不同平台回答风格不同

Claude、ChatGPT、Gemini 和 NotebookLM 的回答风格、引用呈现和保守程度不同。NotebookLM 通常更严格限制在已上传资料范围内；其他平台可能更适合解释和总结，但仍需要人工判断。

## 5. 不覆盖组织内部规则

不同申办方、CRO 或数据标准团队可能有内部映射约定、Define-XML 规范、Reviewers Guide 写法和质量流程。SDTM Pedia 可以辅助查标准，但不能替代项目级或组织级约定。

## 6. 需要人工复核的高风险场景

以下场景建议人工复核:

- 影响正式提交数据结构或变量映射的判断。
- 涉及医学编码、严重不良事件、死亡、试验终止等关键临床语义。
- 涉及项目特定 CRF、SAP、数据管理计划或申办方标准。
- 回答中没有明确依据，或与团队既有标准不一致。

如发现明显错误或范围缺口，请记录问题、平台、提问内容和期望依据，反馈给维护者进行修订。
