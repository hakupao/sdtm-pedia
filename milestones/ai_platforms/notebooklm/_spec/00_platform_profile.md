# 00 平台适配层 (Platform Profile)

> 新平台部署的第一步: 填空本表, 建立"本平台 vs 其他平台"的差异画像.
> 本文件**必须在 Phase 1 调研之前填写到至少 80% 完整**, 否则 PLAN 无法正确设计内容策略.

---

## A. 平台身份

| 字段 | 值 | 来源 |
|------|----|------|
| 平台名称 | `<PLATFORM_NAME>` (e.g. Claude Projects, ChatGPT GPTs, Gemini Gems) | 用户给定 |
| 订阅套餐 | `<PLAN>` (e.g. Pro / Plus / Team / Enterprise / Advanced) | 用户确认 |
| 使用界面 | Web UI / API / CLI / Plugin | 官方文档 |
| 是否支持 API 调用 | Yes / No / Partial | 官方文档 |

---

## B. 检索机制

**最关键的 5 个字段, 决定内容策略.**

| 字段 | 说明 | Claude Projects 示例 | ChatGPT GPTs 示例 | Gemini Gems 示例 |
|------|------|---------------------|-------------------|------------------|
| RAG 类型 | 自动/手动/无 | 自动分片 (paid 套餐) | 内置 RAG (File Search) | 无, 全量注入 |
| 注入粒度 | 全量 / chunk / 文件级 | 混合 (小项目全量, 大项目 RAG) | chunk 级 (embeddings) | 全量注入 1M 窗口 |
| 容量单位 | tokens / MB / 文件数 | capacity % (不透明, 约 3-4M tokens 等值) | 20 文件 + 512MB/文件 | 1M tokens 窗口 |
| 容量硬上限 | 最高能塞多少 | 实测 77% 未触拐点 | 20 文件硬限 | ~1M tokens 软限 |
| 本平台的 "capacity 不透明" 问题 | 是否需做 calibration 实验 | 是 (capacity% 与 local tiktoken 差 8x, G2) | 否 (硬指标清晰) | 否 |

---

## C. 文件管理

| 字段 | 值 |
|------|---|
| 文件数上限 | `<N_FILES_MAX>` |
| 单文件大小上限 | `<FILE_SIZE_MAX>` |
| 文件类型支持 | `<FILE_TYPES>` (e.g. .md / .txt / .pdf / .docx) |
| 是否支持重命名 | Yes / No |
| 上传方式 | 拖拽 / 选择器 / API / MCP |
| 上传后等待时间 | `<WAIT_TIME>` (e.g. "Indexing ~30min", "立即可用") |
| Indexing indicator 可靠吗? | Yes / No / 部分 (G3 教训: Claude 全程不可信) |

---

## D. System Prompt / Instructions

| 字段 | 值 |
|------|---|
| 有无 Custom Instructions? | Yes / No |
| 长度限制 | `<PROMPT_TOKENS>` (e.g. 8K tokens) |
| 是否在 Knowledge 之外单独计量? | Yes / No |
| 是否可包含路由规则? | Yes (e.g. "文件 N 优先于文件 M") / No |
| 修改后是否立即生效? | Yes / No (需要重索引) |

---

## E. 分享 & 访问控制

| 字段 | 值 |
|------|---|
| 支持个人私有 | Yes / No |
| 支持团队共享 | Yes / No (需套餐) |
| 支持公开发布 | Yes / No (e.g. ChatGPT GPT Store) |
| 链接可否生成 | Yes / No (Claude: No, ChatGPT: Yes) |
| 权限粒度 | 读 / 写 / 管理 |

---

## F. 失败模式 (Known Issues)

列出已知的平台行为异常, 在 PLAN §约束条件里规避.

| # | 现象 | 缓解 |
|---|------|------|
| 1 | (e.g. Indexing indicator 不可信) | 不等 indicator, 直接试问判可用 |
| 2 | (e.g. 文件合并断表) | 用 TableAwareChunker 或 md-heading 分段 |
| 3 | (e.g. 长上下文末尾召回衰减) | 关键内容前置 |
| 4 | ... | ... |

---

## G. A/B 矩阵侧重

每平台 A/B 矩阵应覆盖的独有能力:

| 平台 | 独有能力测试题 |
|------|---------------|
| Claude Projects | RAG 衰减 / 边界诚实 / 跨文件 narrative 重建 / Deferred stub 识别 |
| ChatGPT GPTs | 跨 chunk 检索准确度 / 公开分享语气 / Conversation Starter 命中率 |
| Gemini Gems | 全域对比 / 跨域模式识别 / 长上下文末尾召回 / 大规模比较 |

---

## H. 内容策略的关键决策点

根据 A-G 填空结果, 自动推导下列决策:

| 决策 | 规则 |
|------|------|
| 是否分批? | 容量硬限/软限 < 1.2x 源量 → 单批; 否则多批 |
| 是否需要 Deferred stub? | 存在单表 >500 条目 + 容量硬限 → 用 stub; 无限则可 inline |
| 是否需要 capacity calibration? | 容量不透明 → 做 3 组 known-N 实验; 透明则跳过 |
| A/B 矩阵大小? | Tier 1: 3-5 题 / Tier 2: 10-15 题 / Tier 3: 20+ 题 |
| 批次间是否跨批正向激活? | 仅 Claude 类自动 RAG 平台观察到 (本范本不做假设, 每平台实测) |

---

## 填空示例: Claude Projects (已完成, 供参考)

```
A 平台身份:
- 名称: Claude Projects
- 套餐: Pro
- 界面: Web UI (claude.ai)
- API: No

B 检索机制:
- RAG: 自动分片 (paid 套餐)
- 粒度: 混合
- 单位: capacity % (不透明)
- 上限: 实测 77% 未触拐点
- 不透明: 是, 需 calibration

C 文件管理:
- N_FILES_MAX: 未公开硬限, 实测 19 文件无压力
- FILE_SIZE_MAX: 未公开, 实测 256K tokens 单文件可用
- 类型: .md .txt .pdf .docx .csv
- 重命名: Yes
- 上传: 拖拽 / 选择器
- 等待: Indexing 30-60 min, 但不必真等
- Indicator 可靠: No (G3)

D System Prompt:
- 有: Yes (Custom Instructions)
- 长度: 估算 8K tokens
- 单独计量: 否 (含在 capacity)
- 路由规则: Yes
- 立即生效: Yes

E 分享:
- 私有: Yes
- 团队: Yes (Team/Enterprise)
- 公开: No
- 链接: No
- 粒度: 读/写/管理

F 失败模式:
1. Indexing indicator 全程不可信 → 直接试问
2. local tiktoken 与 UI capacity 不一致 → calibration
3. 6 个 MedDRA 级 codelist 走 inline 会挤占 >100K → Deferred stub

G A/B 侧重:
- RAG 衰减拐点 / 边界诚实 / 跨批 narrative 重建 / stub 识别
```

---

## 输出

填完后存在: `<platform>/docs/platform_profile.md` (或合并进 `docs/research.md`).

后续 PLAN, solution, review 的所有决策都应能**追溯到本表某个字段**. 追溯不到的决策是 hallucinated 决策.
