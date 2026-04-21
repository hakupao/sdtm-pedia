# NotebookLM Deployment Roadmap

## 状态 (首屏)

- **当前状态**: Phase 0 进行中 (2026-04-21 起跑)
- **目标 Tier**: **Tier 2** (5-15 步, 半天-1 天 / 可能 Tier 2 偏轻, Phase 1 调研后复核)
- **模式**: 异步 (不参与 `SYNC_BOARD.md` 2-way 锁步)
- **参考基线**: Claude v2.6 方法论 + ChatGPT/Gemini 范本补丁 (待两平台收束后合入)

## 六问首屏

### 1. 状态 + 日期
- **进行中** (2026-04-21 Phase 0 脚手架完成, 等用户规则 E ack 后进 Phase 1 调研)

### 2. 着重方向 (本平台独有优势)
- **Audio Overview 培训产物**: SDTM 初学者 30 分钟可听完一期"SDTM Domain 速览"播客, 和 Claude 的长文对答形成互补
- **Mind Map 关系可视化**: 跨 domain 的 RELREC / --STAT / Supplemental Qualifier 依赖关系, 图形化胜过 Markdown 表
- **Grounded citation 默认强**: 每句都能点回源 chunk, 对"SDTM 标准依据"类问题是最稳的平台
- **Study Guide / Briefing Doc 自动化**: 问卷式学习产出, 和 ChatGPT 的 conversation starter 形成不同入口

### 3. 平台特性 (RAG / 容量 / 分享) — 待 Phase 1 调研确认

| 维度 | 暂定 (基于训练知识, Phase 1 校验) |
|------|-----------------------------|
| RAG | 内置 grounded retrieval, chunk-level inline citation |
| 套餐 | Free / Plus (Google One AI Premium 捆绑 或 NotebookLM Plus 独立) |
| Source 数上限 | Free: 50 sources/notebook / Plus: 300 sources/notebook |
| 单 source 大小 | 500K words/source (远超 SDTM 单 md 规模) |
| 文件类型 | PDF, .txt, .md, Google Docs/Slides, 网页 URL, YouTube URL, 音频文件 |
| 分享 | 公开 notebook 链接 (view-only) / 协作者 (Plus) |
| Custom Instructions | **无** (Plus 有 tone/length + Audio Overview instructions) |
| API | 2025 年尚无公开 GA API (Phase 1 需确认最新状态) |

### 4. 内容策略 (待 Phase 2 定)
- **候选 A**: 把 `knowledge_base/` 293 个 md 合并到 ≤50 sources (Free 档即可), 按 domain group + 标准概念 group 分
- **候选 B**: 直接上 Plus 档 300 sources, 一对一映射 (开销最小, 需用户确认 Plus 订阅)
- **关键决策点**: 取决于规则 E 用户业务优先级 — 若"个人学习为主" → A (Free 够用); 若"对外分享培训" → B (更精细)

### 5. 执行步骤 (Phase A-H 概览, Phase 1 后细化)
- Phase 0 脚手架 ✓
- Phase 1 八问八答调研 (特别: Audio Overview hallucination 基线 / Mind Map 覆盖率 / citation 回链命中率)
- Phase 2 PLAN (候选 A vs B 决策 + A/B 矩阵扩维度)
- Phase 3 单批上传 + 独有产出质量 A/B (Audio Overview / Mind Map / Study Guide 各 3-5 题)
- Phase 4 回归 + 和 Claude/ChatGPT/Gemini 跨平台同题对比
- Phase 5 RETROSPECTIVE + `_template/` 缺陷补丁 + handoff

### 6. 验收标准 (A/B 矩阵 PASS 条件) — 待 Phase 2 明确
- 10 题同 `SMOKE_QUESTIONS_V2.md` + 5 题独有生成物评估 (Audio Overview 2 + Mind Map 2 + Study Guide 1)
- PASS 阈值: ≥13/15 (~87%) 业务正确 + 每个独有产出至少 1 题精确命中

## 实际产出 (收束时填)

- 文件数: _pending_
- 总 tokens: _pending_
- 容量占用: _pending_ (NotebookLM 容量不是 token 单位, 是 sources + words)
- A/B PASS: _pending_
- 跨平台对比: _pending_
- `_template/` 补丁: _pending_

---

*更新规则: 每 Phase 收束时刷新本文件首屏 + 在 CHANGELOG 段 append 一条.*
