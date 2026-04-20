# Gemini Gems — 平台适配层 (Platform Profile)

> 范本: [`../../_template/00_platform_profile.md`](../../_template/00_platform_profile.md)
> 状态: **Phase 1 关闭** (Q1-Q4 已答, E section 已根据 Q3 调研更新)
> 最后更新: 2026-04-20 (Phase 1 post-update: 分享机制从"仅个人"→支持链接/公开/Workspace, 2025-09-18 Gems Sharing 发布)

---

## A. 平台身份

| 字段 | 值 | 来源 |
|------|----|------|
| 平台名称 | Gemini Gems | Google 官方产品名 |
| 订阅套餐 | Gemini Advanced (Google One AI Premium) | [Google One pricing](https://one.google.com/about/plans) (待 P1 复核) |
| 使用界面 | Web (gemini.google.com) + mobile | 官方 |
| 是否支持 API 调用 | **否** (Gems 是 Gemini Advanced Web 功能, API 用 Gemini API 不同) | 待 P1 复核 |

---

## B. 检索机制 (核心)

| 字段 | 值 |
|------|---|
| RAG 类型 | **无** (全量注入超长上下文) |
| 注入粒度 | 全量 (不切 chunk, 不检索) |
| 容量单位 | tokens (上下文窗口) + MB (单文件) |
| 容量硬上限 | **1M tokens 上下文窗口** / 单文件数百 MB (待 P1 精确确认) |
| "capacity 不透明" 问题 | **否** (官方明确 1M 窗口) → 不需要 calibration 实验 |

**对 PLAN 的影响**:
- **无需分批** (相对 Claude 5+1 批), 1 批直接全上
- **无需 Deferred stub** (1M 窗口可 inline 大量 terminology)
- **需验长上下文末尾召回** (Gemini 已知衰减区)

---

## C. 文件管理

| 字段 | 值 |
|------|---|
| 文件数上限 | 待 P1 精确 (估算 ~10 份文件足够, 并不硬限) |
| 单文件大小上限 | 数百 MB (待 P1 精确) |
| 文件类型支持 | .md .txt .pdf .docx .csv (待 P1 精确列表) |
| 是否支持重命名 | 待 P1 |
| 上传方式 | Web UI (Gems 创建界面) |
| 上传后等待时间 | 估算 秒级 (无 indexing, 全量注入) |
| Indexing indicator 可靠吗? | **不适用** (无 indexing 概念) |

---

## D. System Prompt / Instructions

| 字段 | 值 |
|------|---|
| 有无 Custom Instructions? | Yes (Gem Instructions) |
| 长度限制 | 估算 ~8K-16K tokens (待 P1 确认) |
| 是否在 Knowledge 之外单独计量? | 待 P1 (估算是, 类 Claude/ChatGPT) |
| 是否可包含路由规则? | Yes, 但因无 RAG, 路由作用更多是"引用规范" |
| 修改后是否立即生效? | Yes |

---

## E. 分享 & 访问控制

| 字段 | 值 |
|------|---|
| 支持个人私有 | Yes (默认) |
| 支持团队共享 | **Yes** (2025-09 起, Workspace 场景, 管理员可启用/限制) |
| 支持公开发布 | **Yes** (2025-09 起, 链接公开, 无需登录可使用) |
| 链接可否生成 | **Yes** (2025-09 起, 要求 device 或 Google Drive 上传的知识文件) |
| 权限粒度 | Viewer (可用 Gem) / Editor (可改 Instructions + 再分享) |

**对 PLAN 的影响**: 分享能力已可用 (Phase 1 Q3 调研确认, Google 2025-09-18 官方发布 [Sharing Gems](https://blog.google/products-and-platforms/products/gemini/sharing-gems/)), 但本次发布 **Phase 5 默认保持私有** (Rule E Q3=C/Q4=A 决策时假设个人深度使用). 若用户后续想分享, Phase 5 一键开关即可, 不影响 Phase 2-4 PLAN 主线. 本项目用 device 上传 .md 文件 → 满足分享条件; 若切换到 Google Drive 路径也 OK.

> **更新记录**: 2026-04-20 Phase 1 Q3 调研关闭本 section carry-over. 原 Phase 0 记录 "仅个人 / 链接 No / 公开 No" 在 2025-09 Gemini 分享功能发布后已过时.

---

## F. 失败模式 (Known Issues, Phase 0 预判)

| # | 现象 | 缓解 |
|---|------|------|
| 1 | **长上下文末尾召回衰减** (Gemini 已知问题, 末 100K-200K 区域响应质量下降) | 关键内容前置: 导航层 / 核心 spec 放文件头部, terminology 放尾部 |
| 2 | 上下文稀释: 太多无关内容在窗口内, 具体问题命中率下降 | Instructions 强调"精确匹配源文件, 不做全扫" |
| 3 | Gemini hallucinate 倾向 (相对 Claude) | A/B 必含零臆造测试题, 边界题至少 2 道 |
| 4 | 1M 窗口接近上限响应变慢 / truncate | Phase 3 上传后测极长查询响应时间 |
| 5 | 分享时受文件类型约束: 非 device/Drive 上传的知识会使分享按钮置灰 | 用 device 上传 .md 文件 (本项目默认) 即满足条件; 若未来需切换路径, 保持上传源一致 |

---

## G. A/B 矩阵侧重 (本平台独有能力测试)

| 题型 | 样题 |
|------|------|
| **全域对比** (本平台独有) | "所有域中哪些使用了 EPOCH 变量? 列出 Core 属性差异" |
| **跨域 assumptions 搜索** | "哪些域的 assumptions 提到了 RELREC?" |
| **examples 模式识别** | "EX/EC, MB/MS, TU/TR, PC/PP 四对域的 examples section 有什么相似结构?" |
| **长上下文末尾召回** | 末段某 codelist 精确 Term (验证末尾召回) |
| **大规模对比** | "比较 Events 类 7 个域的 assumptions 结构" |
| 边界诚实 (继承 Claude) | "AERELN codelist 所有 Synonyms?" |

---

## H. 内容策略的关键决策

| 决策 | 本平台选择 | 原因 |
|------|-----------|------|
| 是否分批? | **1 批全上** | 1M 窗口够, 无硬限需分批 |
| 是否需要 Deferred stub? | **否** (暂定) | 1M 窗口可 inline 高频 codelist; 若超再评估 |
| 是否需要 capacity calibration? | **否** | 官方 1M 窗口明确 |
| A/B 矩阵大小? | **10 题** (Tier 1-2) | 含 3-4 全域对比 + 2 末尾召回 + 2 边界 + 2-3 精确查询 |
| 文件切分粒度? | **3-5 主题合并文件** | 减少文件数, 让上下文结构清晰 |

---

## I. 本平台相对 Claude/ChatGPT 的差异速查

| 维度 | Claude Projects | ChatGPT GPTs | **Gemini Gems** |
|------|-----------------|--------------|-----------------|
| RAG | 自动分片 | 内置 File Search | **无, 全量注入** |
| 容量 | ~3-4M 等值 | 20 文件/512MB | **1M tokens 窗口** |
| 分批数 | 5+1 | 2 | **1** |
| 分享 | 私有/团队 | 私有/团队/**公开 (Store)** | **私有/链接/公开/Workspace** (2025-09 起) |
| 链接生成 | No | Yes | **Yes** (2025-09 起, device/Drive 文件) |
| A/B 侧重 | RAG 衰减 | chunk 检索 | **全域对比 + 末尾召回** |
| Tier | 3 | 2 | **1-2** (本系列最轻) |

---

## J. Phase 1 调研必补字段 (3 问简化版)

本平台 Tier 轻, 调研可压缩为 3 问 (相对范本八问八答):

- [x] **Q1**: 1M 窗口是否真的全量可用? 有无隐藏 chunk 退化? 末尾召回实测衰减程度? — **已答** (`docs/research.md §Q1`). F-1 数字 partial_close → Phase 3 实测校准 (末尾 codelist 精确 term 2 道).
- [x] **Q2**: 单文件/总文件数的精确硬限? 套餐间差异? — **已答** (`§Q2`). Google AI Pro: 10 files / 100MB each; Workspace 更高限额.
- [x] **Q3**: Gems 分享机制官方态度? 未来会开放团队/公开吗? — **已答** (`§Q3`). **2025-09-18 起已支持链接/公开/Workspace 分享**, E section 已同步更新.

可选补问 (Tier 2 拔高):
- [x] Q4: Gemini API (非 Gems) 能否复用本 Gem 的 Knowledge? — **已答** (`§Q4`). 无法直接复用 (Gems 知识存储与 API Files 分离), 但架构可迁移.

---

## K. 预计工作量 (Phase 0 估算, 相对其他平台)

| 指标 | Claude (已完成) | ChatGPT (预计) | **Gemini (预计)** |
|------|----------------:|--------------:|------------------:|
| 批次数 | 5+1 | 2 | **1** |
| A/B 矩阵题数 | 24 | 10-15 | **10** |
| 脚本数 | 6+ | 3-5 | **2-3** (合并 + 校验) |
| 预计壁钟 | ~3 天 | 1-2 天 | **半天-1 天** |
| Tier | 3 | 2 | **1-2** |

---

*来源: 范本 `../../_template/00_platform_profile.md` + 2026-04-16 原 ROADMAP 平台特性段 + 2026-04-20 Phase 0 填空.*
