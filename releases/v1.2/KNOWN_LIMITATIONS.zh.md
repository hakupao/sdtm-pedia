---
lang: zh
slug: known-limitations
order: 50
title: "已知限制"
---

# 已知限制

本页说明 v1.2 的使用边界. 它不是错误清单, 而是帮助用户判断哪些问题适合直接查询, 哪些问题需要回到官方来源或组织流程确认.

## 0. v1.2 审计范围 (2026-05-19 更新)

v1.2 是 v1.1 的 Gemini-only system prompt 刷新 (v7.1 → v8.1, 422 → 525 行). 知识库 / 4 平台 uploads / 全部元文档 / Claude / ChatGPT / NotebookLM 的 prompt 均 byte-identical 继承 v1.1.

### v1.2 已验证项

- **SMOKE_V4 R3 (2026-05-19)** — v1.1 部署后 4 平台 × 17 题完整回归测. 结果: Claude 17/17, ChatGPT 17/17, NotebookLM 15.5/17 (Q9 PUNT 和 Q11 PARTIAL 是 RAG 架构限制), **Gemini v7.1: 13/17, 4 道 FAIL** (Q3 BE/BS/RELSPEC 跑题到 AE; Q4 场景 A 答 LB 而非 IS; Q11 Dataset-JSON 跑题到 AE/CM; AHP1 LBCLINSIG 跑题到 CM/MH). 独立 reviewer (`oh-my-claudecode:scientist`, Rule D #15) 核对 68/68 cell 一致.
- **Gemini v8.1 对 R3 4 道 FAIL 的 dry-run (2026-05-19 16:35-16:40 PM)** — 4 道全在 Gemini 3.1 Pro (与 R3 baseline 同 model) 上 PASS. Q3/Q4/Q11/AHP1 经 Rule D #17 reviewer (`oh-my-claudecode:verifier`) APPROVE, 0 blocker.
- **Rule A 覆盖扩展** — v1.1 抽检时 N=5 KB 文件 (留 v1.1 audit). v1.1 post-cut audit (2026-05-16) 将其提升至 **N=20 KB 文件 × 4 平台 = 124 grep probes, 100% PASS**.

### v1.2 未重新评估项 (留 v1.2 post-cut)

- **Gemini v8.1 的 R4 17 题全量回归** — 仅 v7.1 4 道 FAIL 题重测, Gemini 上 13 道 v7.1 PASS 题未在 v8.1 下测试; CO-5 默认反思 regex 与候选数限在多变量题上未独立验证. 风险: 低 (v8.1 改动是 anchor 扩展, 不动 PASS 题的核心 rule), 但完整确认需 R4.
- **M2 候选数限独立验证** — 4 道 dry-run 题候选数 < 5, 没真触发 threshold. 留 R4.
- **BECAT EXTRACTION KB-prompt 注释** — v8.1 prompt L272 把 `"EXTRACTION"` 列入 BECAT 示例, KB BE / spec L111 只 inline 3 个标准 examples (`COLLECTION` / `PREPARATION` / `TRANSPORT`). 部署答案已标注 sponsor-extensible, 未来 prompt 修订可加显式来源引用防 prompt-KB 分叉.
- **Gemini `04_business_scenarios_and_cross_domain.md`** — writer 手写, v1.2 不变, 已在 2026-05-16 post-v1.1 audit pass 中审过, 无需进一步动作.
- **06 P5 阶段 437 个 `UNSOURCED_MANUAL` 原子** — 未最终定性. 不影响部署回答但代表 KB 中来源未验证的内容.
- **166 个 KB 节 Tier B 推迟** — 56 个缺兄弟节点, 110 个内容截断. 06 深度验证在覆盖率 gate (99.02%) 达标时仅完成 Tier A 修复. 这些节的回答可能不如其他区域完整. Tier B 修复计划在未来 KB pass 完成.

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
