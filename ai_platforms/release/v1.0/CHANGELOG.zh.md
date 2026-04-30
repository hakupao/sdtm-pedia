---
lang: zh
slug: changelog
order: 60
title: "更新日志"
---

# 更新日志 — SDTM AI 知识库发布版

## v1.0 — 2026-04-27 (公司发布版)

### 新增

- 发布 4 个平台的部署包:
  - Claude Projects v2.6
  - ChatGPT GPTs v2.2 LIVE
  - Gemini Gems v7.1 LIVE
  - NotebookLM Custom mode
- 发布三语 onboarding 文档:
  - `README`
  - `USER_GUIDE`
  - `PLATFORM_COMPARISON`
  - `DEMO_QUESTIONS`
  - `GLOSSARY`
  - `METHODOLOGY`
  - `KNOWN_LIMITATIONS`
- 发布 10 题 demo set (D0-D9)，供同事快速验收部署质量。
- 发布每个平台的 self-deploy tutorial，说明上传文件、配置 prompt 和 smoke test 的步骤。

### 质量基线 (17 题评测，R1+R2)

| 平台 | 分数 | 状态 |
|---|:---:|---|
| Claude Projects | 17/17 | LIVE |
| ChatGPT GPTs | 16.5/17 | LIVE |
| Gemini Gems | 16/17 | LIVE |
| NotebookLM | 15/17 | LIVE |

### 方法论参考

- 完整方法论与验证说明见 `METHODOLOGY`。
- 已知限制与绕行方案见 `KNOWN_LIMITATIONS`。
- 每个平台的部署边界与适用场景见 `PLATFORM_COMPARISON`。

### 源知识库

- 源内容来自 CDISC SDTMIG v3.4、SDTM Model v2.0 与 CDISC Controlled Terminology。
- 发布包不重新分发 CDISC 原始资料。
- 知识库内容在 repo 中保持 traceable，并可回到 `knowledge_base/` 与验证记录进行审计。

### 发布工件

- 4 个 zip bundle 通过 GitHub releases 分发。
- Web 站点展示三语 landing、文档、比较表与下载入口。

### 已知限制

- QS long-tail codelist 未完全覆盖。
- 巨型 codelist 使用 stub + NCI EVS pointer，而不是完整 term 展开。
- NotebookLM 是 in-KB-only 架构，对实时 Web 内容会 PUNT。

## 预发布历史 (摘要)

- 完成知识库构建与验证。
- 完成 4 个平台部署。
- 完成 17 题 baseline 测试。
- 完成 v1.0 release package 与同事 onboarding 文档。
