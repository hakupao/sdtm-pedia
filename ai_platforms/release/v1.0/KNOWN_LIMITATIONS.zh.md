---
lang: zh
slug: known-limitations
order: 50
title: "已知限制"
---

# 已知限制 — SDTM AI 知识库 v1.0

> 本页列出当前版本的限制。每条限制包括影响平台、证据/复现方式，以及建议绕行方案。

## 跨平台限制

### L1 — Questionnaires (QS) codelist 覆盖不完整

**影响**: 4 个平台全部受影响，Claude Projects v2.6 上最明显。
**详情**: 296 个长尾 QS codelist (PROMIS / EORTC item-bank 风格) 因容量限制未在任何部署中完整展开。Claude Projects 覆盖约 55.8% 的 QS codelist，其余回退到 NCI EVS Browser 链接。
**绕行方案**: 对覆盖子集之外的 QS codelist 查询，让 AI 指向 NCI EVS Browser URL。AI 应识别自己只有 stub。Phase 7 自托管 RAG 将补齐这一缺口。

### L2 — 巨型 codelist (LB / MedDRA 级) 以 stub 返回，而不是完整 term 列表

**影响**: 4 个平台全部受影响。
**详情**: 6 个巨型 codelist，例如 LB Test Code C65047 含 2,536 个 terms，当前存储为 stub-with-pointer，而不是逐项展开。询问“列出 C65047 的全部 terms”时，应返回 stub 声明 + NCI EVS Browser 链接，不能编造 term 列表。
**绕行方案**: 这是可接受行为。如果平台在这里编造 terms，请重新检查 system prompt 的 Stage 6 Deferred Stub 规则 (Claude) 或等价的反编造锚点。

### L3 — 实时 Web 查询 (FDA / Pinnacle 21 / dbSNP / NCI EVS) 未内置

**影响**: NotebookLM (in-KB-only 架构)；ChatGPT/Gemini/Claude 如启用联网，可自行 Web search。
**详情**: 对于变化中的标准更新，例如 Dataset-JSON catalog 状态或 Pinnacle 21 rule release notes，知识库内容反映的是 2026-04-22 baseline 状态。
**绕行方案**: 对时间敏感答案，请人工交叉核对 CDISC.org / FDA.gov / standards.pinnacle21.certara.net。AI 通常会给出引用；若引用早于 6 个月，请再次核对。

## 各平台限制

### Claude Projects (v2.6)

- **L4-Cl1**: 容量约 77% (1.29M tokens / 19 files)，接近 paid-tier soft cap。若要加入更多内容，需要删除现有低优先级文件，见 UPLOAD_TUTORIAL §8 downgrade path。
- **L4-Cl2**: Indexing 指示不可靠。即使 UI 显示 "Indexing"，查询也可能已经能命中新内容。不要等待，直接用 smoke questions 测试。
- **L4-Cl3**: 无公开分享链接。Team/Enterprise plan 成员共享同一个 Project；Pro plan 用户需要各自部署。

### ChatGPT GPTs (v2.2 LIVE)

- **L4-CG1**: 20-file hard limit。当前部署使用 9 files，仍有增长空间。源文件已合并，例如 63 个 domain specs 合并为 `04_domain_specs_all.md`。
- **L4-CG2**: File search RAG chunk strategy 不能由用户配置。部分长尾 terminology queries 如果埋在表格中部，可能 miss chunks。
- **L4-CG3**: GPT Store 发布需要 OpenAI review。Custom GPT 可分享到 org/team 且不需 review，推荐公司内部使用。

### Gemini Gems (v7.1 LIVE)

- **L4-GE1**: 仅上传 4 个文件，合并最激进。更大的 context window 可以补偿，但冷启动时 first-token latency 可能更慢。
- **L4-GE2**: 绑定个人账号。Gem 默认不能直接分享到团队，Workspace plan 可能提供部分共享能力。每位同事需要自部署。
- **L4-GE3**: 反幻觉严格度 baseline 低于 Claude/NotebookLM。R1→R2 升级 (v6→v7 system prompt) 将分数从 65% 提升到 94%；**所有同事部署时必须逐字使用 v7.1 system prompt** 才能继承 AHP guardrail。

### NotebookLM

- **L4-NB1**: 50-source hard cap (Pro plan)。当前部署 42/50，剩余 8 个 source headroom。
- **L4-NB2**: 设计上 in-KB-only。无法回答 42 个 sources 之外的问题，例如部署日期之后的 breaking news。优点是天然具备反幻觉保护。
- **L4-NB3**: Q9 (Pinnacle 21 categories) PUNT。NotebookLM 会安全声明“本知识库中没有”，而不是从 Pinnacle 21 网页作答。这是**正确安全行为**，不是 bug。
- **L4-NB4**: Sources panel ≠ Chat。问题应输入 Chat (mat-input-0)，不是 "Discover sources" search。
- **L4-NB5**: Q11 (Dataset-JSON v1.1) 与 Q12 (CT version locking + MedDRA) 为 PARTIAL；这些补充主题超出 42 sources 范围。PUNT 是安全答案；如果平台试图自信作答，应谨慎对待。

## 题型表现参考

基于 SMOKE_V4 R1+R2 结果 (2026-04-22 至 2026-04-24):

| 题型 | Claude | ChatGPT | Gemini (R2) | NotebookLM |
|---|:---:|:---:|:---:|:---:|
| 新域 (GF/CP/BE/BS) | PASS+ | PASS | PASS | PASS+ |
| 域边界 (LB/MB/IS) | PASS+ | PASS | PASS+ | PASS |
| Timing 模型 (--TPT) | PASS | PASS | PASS | PASS |
| CT 机制 (Ext + dictionary) | PASS+ | PARTIAL→PASS (post v2.2) | PASS | PASS+ |
| 前提纠错 (SUPPTS) | PASS+ | PASS | PASS+ (post v7.1) | PASS+ |
| 反幻觉 (LBCLINSIG) | PASS+ | PASS | PASS+ (post v7) | PASS+ (in-KB-only) |
| 反幻觉 (SAE Aggregate) | PASS | PASS | PASS+ | PASS+ |
| 废弃 PF | PASS+ | PASS | PASS+ | PASS+ |
| 跨域死亡时间 | PASS+ | PASS | PASS | PASS |
| 实时 / 补充主题 (Q11/Q12) | PASS | PASS | PARTIAL | PUNT (正确) |

## 报告新的限制

如果你遇到本页未覆盖的幻觉、事实错误或范围缺口:
1. 保存完整问题 + AI 回复 (截图 + 文本)。
2. 记录平台 + 版本，例如 "ChatGPT GPT v2.2 LIVE 2026-04-24"。
3. 邮件联系 Bojiang Zhang，或在项目 tracker 中提交 issue 并附上上述材料。
4. 包含 expected vs actual，并引用 SDTMIG v3.4 spec section 或 CDISC CT C-code。

我们会在 `./CHANGELOG.md` 中追踪这些问题，供下一个 minor release 使用。
