# ChatGPT GPTs — 平台适配层 (Platform Profile)

> 范本: [`../../_template/00_platform_profile.md`](../../_template/00_platform_profile.md)
> 状态: **Phase 0 初稿** (部分字段待 Phase 1 调研确认)
> 最后更新: 2026-04-20

---

## A. 平台身份

| 字段 | 值 | 来源 |
|------|----|------|
| 平台名称 | ChatGPT GPTs (Custom GPTs) | 官方产品名 |
| 订阅套餐 | ChatGPT Plus / Team / Enterprise | [OpenAI pricing](https://openai.com/chatgpt/pricing) (待 P1 复核) |
| 使用界面 | Web UI (chat.openai.com) + mobile | 官方 |
| 是否支持 API 调用 | **部分** (Assistants API 类似但不完全等同) | [OpenAI docs](https://platform.openai.com/docs/assistants) (待 P1 复核) |

---

## B. 检索机制 (核心)

| 字段 | 值 |
|------|---|
| RAG 类型 | 内置 RAG (File Search / Retrieval) |
| 注入粒度 | chunk 级 (embeddings 检索 top-K 片段) |
| 容量单位 | 文件数 + 单文件大小 + 总 GB |
| 容量硬上限 | **20 文件** / 单文件 **512MB** / 总量无官方硬上限 (Team/Enterprise 可能更高, 待 P1 确认) |
| "capacity 不透明" 问题 | **否** (硬指标清晰) → 不需要 capacity calibration 实验 |

**对 PLAN 的影响**: 不需要 Claude 那种 5+1 批渐进拐点测试. 2 批 (P0 + P1-P2) 到位即可.

---

## C. 文件管理

| 字段 | 值 |
|------|---|
| 文件数上限 | **20 (硬限)** |
| 单文件大小上限 | 512 MB |
| 文件类型支持 | .md .txt .pdf .docx .json .csv .html (待 P1 精确列表) |
| 是否支持重命名 | Yes |
| 上传方式 | Web UI 拖拽 / GPT Builder 选择器 / Assistants API |
| 上传后等待时间 | 短 (~数秒到数分钟 embedding) |
| Indexing indicator 可靠吗? | **待 P1 实测** (推测可靠, 相比 Claude) |

---

## D. System Prompt / Instructions

| 字段 | 值 |
|------|---|
| 有无 Custom Instructions? | Yes (GPT Builder 配置) |
| 长度限制 | 估算 ~8K tokens (待 P1 确认) |
| 是否在 Knowledge 之外单独计量? | 是 |
| 是否可包含路由规则? | Yes |
| 修改后是否立即生效? | Yes |

---

## E. 分享 & 访问控制 (本平台相对优势)

| 字段 | 值 |
|------|---|
| 支持个人私有 | Yes |
| 支持团队共享 | Yes (Team / Enterprise 套餐) |
| 支持公开发布 | **Yes (GPT Store)** — 相对 Claude / Gemini 的独有能力 |
| 链接可否生成 | **Yes** — 公开 GPT 有可分享 URL |
| 权限粒度 | 读 / 编辑 (owner) |
| Store 发布门槛 | 需 OpenAI 审核 (待 P1 查具体流程) |

---

## F. 失败模式 (Known Issues, Phase 0 预判)

| # | 现象 | 缓解 |
|---|------|------|
| 1 | 合并文件后表格被 chunker 切断 (常见 GPT RAG 坑) | md-heading 分段 + TableAwareChunker + 单表不跨 heading |
| 2 | 跨 chunk 检索表格断裂导致 Term 列 hallucinate | Instructions 强调 "数据表查 `domain_examples_all.md` 优先" |
| 3 | 20 文件硬限下某批再新增文件无法容纳 | 合并粒度必须事先规划到 8-10, 预留 spare |
| 4 | 公开 GPT 被 Store 搜索暴露未定稿内容 | 先 Private 测试, 所有 A/B PASS 再公开 |
| 5 | Custom Actions 如接 NCI EVS 被 rate limit | 可选, 不接也能工作, 风险低 |

---

## G. A/B 矩阵侧重 (本平台独有能力测试)

| 题型 | 样题 (Phase 2 设计, 初稿) |
|------|---------------------------|
| 跨 chunk 检索准确度 | "列出 AE 域所有 Core=Req 变量" (需跨 chunk 汇总) |
| Conversation Starter 命中 | 4 个预设 starter 各跑一次, 首答 PASS |
| 公开分享语气 | "简单解释 RELREC 是什么" (非专业用户场景) |
| GPT Actions (如实现) | "查询 NCI EVS C66742 最新版本" (接外部 API) |
| 边界诚实 (继承 Claude) | "AERELN codelist 所有 Synonyms?" |

---

## H. 内容策略的关键决策

| 决策 | 本平台选择 | 原因 |
|------|-----------|------|
| 是否分批? | **2 批** (P0 + P1-P2) | 20 文件硬限明确, 不需要拐点测试 |
| 是否需要 Deferred stub? | **否** (暂定) | 512MB/文件足够 inline MedDRA 级大表 (待 P1 确认总 GB 限制) |
| 是否需要 capacity calibration? | **否** | 硬指标清晰, 无需实验 |
| A/B 矩阵大小? | **10-15 题** (Tier 2) | 含 4 Conversation Starter + 5-6 路由题 + 2-3 边界题 |
| 批次间是否跨批正向激活? | 未知, **每批实测** | 内置 RAG 行为可能与 Claude 不同 |

---

## I. 本平台相对 Claude/Gemini 的差异速查

| 维度 | Claude Projects | **ChatGPT GPTs** | Gemini Gems |
|------|-----------------|------------------|-------------|
| RAG | 自动分片 (不透明) | **内置 File Search (embeddings)** | 无, 全量注入 |
| 容量 | ~3-4M tokens 等值 | **20 文件 / 512MB 单文件** | 1M tokens |
| 分批数 | 5+1 (拐点测试) | **2** (P0 + P1-P2) | 1 (全上) |
| 分享 | 私有 / 团队 | **私有 / 团队 / 公开 (Store)** | 仅个人 |
| 链接生成 | No | **Yes** | No |
| A/B 侧重 | RAG 衰减 | **chunk 检索 + 公开分享** | 全域对比 |

---

## J. Phase 1 调研必补字段

以下字段**必须在 Phase 1 `research.md` 八问八答中回答**, 否则 Phase 2 PLAN 无法定稿:

- [ ] Assistants API 和 GPT Builder 的 Knowledge 是同一套数据吗?
- [ ] File Search chunk 默认大小 / overlap?
- [ ] embeddings 模型是 text-embedding-3-small/large? 可选?
- [ ] 检索 top-K 默认值? 可调吗?
- [ ] Team vs Plus vs Enterprise 三套餐文件数限制差异?
- [ ] GPT Store 发布审核标准 + 时间?
- [ ] Conversation Starters 上限个数?
- [ ] Indexing indicator 是否可靠 (相对 Claude)?

---

*来源: 范本 `../../_template/00_platform_profile.md` + 2026-04-16 原 ROADMAP 平台特性段 + 2026-04-20 Phase 0 填空.*
