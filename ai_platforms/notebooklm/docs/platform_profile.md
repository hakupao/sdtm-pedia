# 00 平台适配层 — NotebookLM

> Phase 0 初稿 (2026-04-21). 标 `<待 Phase 1 调研确认>` 字段在八问八答后回填.
> 本文件填到 ≥80% 完整是 Phase 1 的准入门槛.

---

## A. 平台身份

| 字段 | 值 | 来源 |
|------|----|------|
| 平台名称 | NotebookLM | Google |
| 订阅套餐 | **Pro** (via Google AI Pro 订阅; 2025 H2 官方重命名: 原 "Plus" → **"Pro"**, 现 "Plus" 另指 Google AI Plus 订阅的中档) — 2026-04-21 用户 ack; 本次 unlock: 500 notebooks × 300 sources × 500 chat × 20 audio/day | A: support.google.com/notebooklm/answer/16213268 + C: 9to5google 2026-04-11 |
| 使用界面 | Web UI (notebooklm.google.com) + 移动 App (iOS/Android, 2024-2025 起) | 官方 |
| 是否支持 API 调用 | **No (本次不用)** — 2026-04-21 用户 ack 仅 Web UI; API 最新状态仍作 Phase 1 知识补充 (不影响本次部署路径) | 用户 ack + Phase 1 补充 |

---

## B. 检索机制

| 字段 | 值 (初稿) | 置信度 |
|------|----------|-------|
| RAG 类型 | 内置 grounded retrieval (Gemini backbone + source citation) | 高 |
| 注入粒度 | chunk-level, 生成时强制 inline citation 回指源 | 高 |
| 容量单位 | **sources 数 + words per source** (非 token 单位) | 高 |
| 容量硬上限 | **四档** (详见 `docs/research.md` Q2): Free 50 / Plus 100 / **Pro 300 (本次)** / Ultra 600 sources/notebook; 500K words/source 全档统一; notebooks/user: Free 100 / Plus 200 / Pro 500 / Ultra 500 | A: support.google.com/notebooklm/answer/16213268 |
| capacity 不透明? | **透明** — 官方明示 sources/words 限额, 无需 calibration | 高 |

**对 PLAN 的暗示**: 相比 Claude 的 capacity% 黑盒, NotebookLM 是硬指标清晰型, 范本 `00_platform_profile.md §H` 的 "capacity calibration" 决策**跳过**.

---

## C. 文件管理

| 字段 | 值 (初稿) |
|------|---------|
| 文件数上限 (per notebook) | Free 50 / Plus 100 / **Pro 300 (本次)** / Ultra 600 — 见 `docs/research.md` Q2 |
| 单文件大小上限 | 500K words/source (中文/英文字数, 非 tokens) |
| 文件类型支持 | PDF, .txt, .md, Google Docs, Google Slides, 网页 URL (爬取), YouTube URL (字幕), 音频文件 (mp3/mp4/wav, 转写) |
| 是否支持重命名 | Yes (notebook 内 source 可重命名) |
| 上传方式 | 拖拽 / 选择器 / URL 粘贴 / Google Drive 选取 |
| 上传后等待时间 | `<待 Phase 1 实测>` — 通常几秒-几分钟, PDF/YouTube 较慢 |
| Indexing indicator 可靠吗? | `<待 Phase 1 实测>` — 训练知识印象里是相对可靠, 但 Claude 的 G3 教训要求实测不盲信 |

**SDTM 场景含义**: `knowledge_base/` 293 md 单文件均远 <500K words, 无需拆分或合并到单源上限. 决策点只在"合并到 ≤50 还是直接上 300 (Plus)".

---

## D. System Prompt / Instructions

| 字段 | 值 |
|------|---|
| 有无 Custom Instructions? | **No** (传统意义的 system prompt 概念不存在) |
| 长度限制 | N/A |
| 是否单独计量? | N/A |
| 是否可包含路由规则? | **No** (不能在 notebook 层面配"文件 N 优先于 M") |
| 修改后是否立即生效? | N/A |

**退化映射**: NotebookLM 的"Custom Instructions 等价物"有三条, 但**都不是真正的 system prompt**:

1. **Audio Overview Instructions** (Plus 独有): 可指定播客长度 / 风格 / 侧重话题, 仅影响 Audio Overview 生成, 不影响 chat 回答
2. **Notebook Guide 自动生成的 Suggested Questions**: 不能直接编辑, 但可通过上传"引导性"source 间接影响
3. **Per-chat prompt engineering**: 在每次 chat 里写"请用 SDTM 专家口吻"等 prompt, 每 session 重来

**对 PLAN 的暗示**: 范本 `05_solution.md` 的 "System Prompt 累积" 段在本平台**基本作废**, 改为 "Notebook 首源设计 + Audio Overview instructions 模板". 这条是 `_template/` 的**缺陷补丁候选**.

---

## E. 分享 & 访问控制

| 字段 | 值 | 来源 |
|------|----|------|
| 支持个人私有 | Yes (默认) | A: support.google.com/notebooklm |
| 支持协作者 | Yes (Pro 级 via collaborator invite), View/Edit 权限 | A: support.google.com/notebooklm |
| 支持公开链接 | Yes, **但仅 personal Gmail 账号** (Workspace Enterprise/EDU 禁用) | A: support.google.com/notebooklm/answer/16322204 |
| 公开链接邀请上限 | **50 users** (personal Gmail); Enterprise/EDU 无 user 上限 (但不开公开链接) | C: 9to5google 2025-06-03 |
| 链接可否生成 | Yes — 和 Claude Projects (No) 不同, 本平台 2025-06 起开放 | A: blog.google |
| 权限粒度 | Owner edit / Collaborator view+chat / Public link viewer (read+chat) | A: support.google.com |
| **账号类型 ack (用户 2026-04-21)** | **Personal Gmail** — Scope B 公开链接可用, 3-notebook 架构无降级 | 用户 ack |
| **Scope B fallback** | 若任一 notebook 未来受限, 通过 `current/UPLOAD_TUTORIAL.md` + 打包 `uploads/` 让接收者自建复刻 (即 "workflow_replication 分享" — 补丁候选 #6) | 用户 ack 2026-04-21 |

---

## F. 失败模式 (Known Issues) — Phase 1 调研补全

初稿 (待实测验证):

| # | 现象 | 缓解 |
|---|------|------|
| 1 | Audio Overview 会在生成播客时 hallucinate 细节 (社区观察) | 听完后做一次 citation 核对, 或 Plus 版用 instructions 约束 |
| 2 | Mind Map 对长 source 可能遗漏深层概念 | 分层上传 (核心概念单独一个 source) |
| 3 | YouTube / 长音频转写偶有丢段 | 不依赖音频源做关键测试 |
| 4 | 公开 link 访问者的 chat 历史不写回 notebook 本体 | 收集分享场景反馈单独做 |
| 5 | `<Phase 1 八问八答补>` | ... |

---

## G. A/B 矩阵侧重 — 本平台独有能力

| 能力 | 测试题类型 | 评估方式 |
|------|----------|---------|
| Audio Overview 内容保真 | 随机选 1 个 domain, 生成 Audio Overview, 人工听一遍勾事实错误数 | Plus 版加 instructions "基于 source 绝不脑补" 后再测, 对比 |
| Mind Map 完整度 | 选一个跨 domain 概念 (如 RELREC 关系网), 看 Mind Map 是否覆盖全部相关 domain | 人工对照源文件 checklist |
| Study Guide 分层深度 | 选一个 domain 生成 Study Guide, 检查是否覆盖 Standard → IG → Examples 三层 | 对照知识库源文件 |
| Citation 回链精确度 | 问具体条款, 看引用是否精确指向对应 md 行区间 | 随机 5 题, 点每个 citation 核对 |
| Timeline / Briefing Doc 质量 | 选"SDTM IG 历史版本演进" 类题 | 人工检查事实 |

范本 `06_review.md` 的标准 A/B 矩阵 (10 题问答) + 本段 5 题独有产出 = 本平台 A/B 题量 **15**.

---

## H. 内容策略的关键决策点

| 决策 | 本平台适用 |
|------|----------|
| 是否分批? | **不分批** — 单次 50/300 source 一次上完, 无 RAG 衰减曲线可摸 |
| 是否需要 Deferred stub? | **不需要** — 单 source 500K words 上限, SDTM terminology 最大表也远低于此 |
| 是否需要 capacity calibration? | **不需要** — 容量透明 |
| **Multi-notebook 策略?** | **Yes** — Pro 权益 500 notebooks cap (用 3 占 0.6%), source 严格隔离 (每 notebook 独立 300 source 预算): ①主训练 (SDTM 293 md 一对一/少合并, 余 7 slot) ②对外分享 (合并到 ≤30, personal Gmail 公开链接 + 50 users 邀请上限) ③音频专用 (10-15 核心源跑 Audio Overview daily ≤20) |
| A/B 矩阵大小? | 15 题 (10 标准 + 5 独有产出), **每 notebook 独立判定 PASS**, 全量 3 notebook × 15 题 = 45 题次 |
| 批次间是否跨批正向激活? | N/A (单批) |
| **Pre-upload source audit 必做?** | **Yes** — SDTM 293 md vs Pro 300 cap 仅余 7 slot; 必须 `wc -w` 排序 Top 5 outlier md 确认无 >500K words (单源上限), 否则拆分或合并 |

---

## 对 `_template/` 的缺陷补丁候选

本平台揭示的范本盲区 (收束时合并回 `ai_platforms/_template/`):

1. **00_platform_profile §D** 把 "Custom Instructions" 作为必答字段, 但对无 system prompt 概念的平台 (NotebookLM 类) 没有退化路径. 补丁: 加"等价物映射"子段
2. **00_platform_profile §G** A/B 侧重只列了 Claude/ChatGPT/Gemini 的 chat-first 能力, 未覆盖"平台独有生成物"(Audio / Mind Map / Study Guide / Briefing 等). 补丁: 加"生成物类平台"子节
3. **05_solution.md** 的"System Prompt 累积段设计"对 NotebookLM 不适用. 补丁: 加 if/else 分支, 无 system prompt 平台改为"Notebook 首源设计"
4. **03_research.md Q8 calibration** 对容量透明平台是浪费. 补丁: Q8 加"前置判定: 官方是否公开精确限额? Yes → 跳过 calibration 实验"
5. **范本通篇假设"一个平台 = 一套知识库"** — Pro 级 NotebookLM 揭示 multi-notebook 架构 (同平台多 notebook 服务不同场景). 补丁: `01_directory_structure.md` 加"多实例平台"子节 (每 notebook 独立 `uploads_N/` + `instructions_N.md` + A/B 报告), `05_solution.md` 加"多 notebook 分工矩阵"模板
6. **范本"分享"维度只建模了链接分享** (`00_platform_profile §E`) — 未覆盖 "workflow_replication 分享" 作为 fallback. 场景: NotebookLM Workspace 账号禁公开链接时, 仍可通过 `current/UPLOAD_TUTORIAL.md` + 打包 `uploads/` 让接收者自建 notebook 复刻 (用户 2026-04-21 明示). 补丁: `00_platform_profile §E` 加 `share_mode` 子段区分 `direct_link` / `workflow_replication` 两档; `09_closure.md` UPLOAD_TUTORIAL 强调"可独立复刻"目标
7. **范本未对齐"tier 重命名漂移"风险** — NotebookLM 原 "Plus" 2025 H2 改名 "Pro", 现 Plus 另指 Google AI Plus 订阅档. 同一 SKU 词在 12 个月内语义翻转. 补丁: `03_research.md` Q2 容量表加"历史重命名警示"条, 要求 writer 核对 source 日期区间; Phase 1 调研强制列时间线 (本平台 Q3 已做, 作范例).

---

## 填空完成度

- A 身份: 100% (套餐 Plus / API No / 界面 Web UI 均用户 ack 2026-04-21)
- B 检索机制: 85% (限额数字待官方 URL 验证)
- C 文件管理: 80% (Indexing / 等待时间待实测)
- D Prompt: 95% (结论明确, 仅等 Plus 订阅状态)
- E 分享: 100% (账号 ack personal Gmail + 公开链接可用 + workflow_replication fallback 2026-04-21)
- F 失败模式: 40% (初稿 4 条, Phase 1 补)
- G A/B 侧重: 90%
- H 决策: 90%

**加权平均 ~92%** (A + E 均 100%, B/H 已填研究数字, C/F 待 Phase 3 实测) → Phase 1 Writer 完成 2026-04-21. 待 Reviewer lane 独立核对 (Rule D), 验通后进 Phase 2 PLAN.

---

*来源: 训练知识 (截至 2026-01, 2025 年底观察) + Claude v2 方法论. Phase 1 八问八答将用官方文档链接替换本文件中所有"置信度=中/待确认"字段.*
