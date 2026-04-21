# 00 平台适配层 — NotebookLM (v2, 2026-04-21 架构 pivot 后)

> **v2 更新**: 2026-04-21 架构 pivot (3 notebook → 1 notebook × ≤50 sources) 后重写. v1 (3 notebook 架构) 冻结在 `archive/v1_3notebook_SUPERSEDED_2026-04-21/`. 背景见 `archive/v1_.../ARCHITECTURE_PIVOT_RECORD.md`.
> Phase 0 初稿 (2026-04-21) → Phase 1 调研补全 → Phase 2 v1 ×3 notebook (已归档) → Phase 2 v2 ×1 notebook (current).

---

## A. 平台身份

| 字段 | 值 | 来源 |
|------|----|------|
| 平台名称 | NotebookLM | Google |
| 订阅套餐 | **Pro** (via Google AI Pro 订阅; 2025 H2 官方重命名: 原 "Plus" → **"Pro"**, 现 "Plus" 另指 Google AI Plus 订阅的中档) — 2026-04-21 用户 ack; 本次 unlock: 500 notebooks × 300 sources × 500 chat × 20 audio/day | A: support.google.com/notebooklm/answer/16213268 + C: 9to5google 2026-04-11 |
| 使用界面 | Web UI (notebooklm.google.com) + 移动 App (iOS/Android) | 官方 |
| 是否支持 API 调用 | **No (本次不用)** — 2026-04-21 用户 ack 仅 Web UI; Consumer 无 GA API, Enterprise v1alpha 不在本次 scope | 用户 ack + research.md §12 |

---

## B. 检索机制

| 字段 | 值 | 置信度 |
|------|-----|-------|
| RAG 类型 | 内置 grounded retrieval (Gemini backbone + source citation) | 高 |
| 注入粒度 | chunk-level, 生成时强制 inline citation 回指源 | 高 |
| 容量单位 | **sources 数 + words per source** (非 token 单位) | 高 |
| 容量硬上限 | **四档** (详见 `docs/research.md` Q2): Standard 50 / Plus 100 / **Pro 300 (本次)** / Ultra 600 sources/notebook; 500K words/source 全档统一 | A: support.google.com/notebooklm/answer/16213268 |
| capacity 不透明? | **透明** — 官方明示 sources/words 限额, 无需 calibration | 高 |
| **本次实际使用** | **≤50 sources** (Pro 300 slot 的 16.7%), 主动压缩至 Free tier 兼容水位 (详 §H) | v2 架构决定 |

**对 PLAN 的含义**: 相比 Claude 的 capacity% 黑盒, NotebookLM 是硬指标清晰型, 范本 `00_platform_profile.md §H` 的 "capacity calibration" 决策**跳过**.

---

## C. 文件管理

| 字段 | 值 |
|------|----|
| 文件数上限 (per notebook) | Pro 300 (本次) — 但主动压缩到 **≤50** 见 §H |
| 单文件大小上限 | 500K words/source (中/英字数, 非 tokens) |
| 文件类型支持 | PDF, .txt, .md, Google Docs, Google Slides, 网页 URL (爬取), YouTube URL (字幕), 音频文件 (mp3/mp4/wav, 转写) |
| 是否支持重命名 | Yes (notebook 内 source 可重命名) |
| 上传方式 | 拖拽 / 选择器 / URL 粘贴 / Google Drive 选取 |
| 上传后等待时间 | `<Phase 3 实测>` — 通常几秒-几分钟, PDF/YouTube 较慢 |
| Indexing indicator 可靠吗? | **No** — 官方承认 silent fail (见 research.md Q5), Phase 3 实测前置 gate |

**SDTM 场景含义**: `knowledge_base/` 293 md **不一对一上传**, 而是按 concept cluster 合并到 ≤50 source (见 §H + PLAN §3). 单文件均远 <500K words, 不触发单源 cap.

---

## D. System Prompt / Instructions

| 字段 | 值 |
|------|----|
| 有无 Custom Instructions? | **No** (传统意义的 system prompt 不存在) |
| 长度限制 | N/A |
| 是否单独计量? | N/A |
| 是否可包含路由规则? | **No** (不能在 notebook 层面配"文件 N 优先于 M") |
| 修改后是否立即生效? | N/A |
| **退化机制 (最接近的)** | **Chat custom goals** 三档 (Default / Learning Guide / **Custom**), Custom 10,000 char 可定 SDTM 专家角色/目标/口吻 — 2025-10-29 blog.google 发布, 全档开放 |

**退化映射**: NotebookLM 的 "notebook 级 system prompt 等价物":

1. **Chat custom goals Custom 模式** (10,000 char) — 本次选**此模式**, SDTM 专家系统 prompt 写入
2. **Audio Overview Instructions** (Plus+): 指定播客长度/风格, 仅影响 Audio Overview
3. **Notebook Guide 自动 Suggested Questions**: 不能直接编辑
4. **Per-chat prompt engineering**: 每次 chat 里写, 每 session 重来

**对 PLAN 的含义**: 范本 `05_solution.md` 的 "System Prompt 累积段" 在本平台**基本作废**, 改为 "**Chat custom goals Custom 模式文本** (≤10K char) + 精选 source 的首源导航设计". 这是 `_template/` **补丁候选 #1** 和 **#3**.

---

## E. 分享 & 访问控制 (v2 重写)

| 字段 | 值 | 来源 |
|------|-----|------|
| 分享模型 | **同一 notebook 3 档 Access Level 切换** (非多 notebook 独立模式) | A: support.google.com/notebooklm/answer/16322204 |
| 三档 | **Restricted** (邀请, 50-cap personal Gmail) / **Anyone with link** (无 users 上限, 需 Google 账号) / **Public** (画廊可发现, 无 users 上限) | 同上 |
| 档位切换 | 随时切换, 同一 notebook 内 toggle, 不建新 notebook | A: "Set Notebook Access back to Restricted" |
| 50-cap 适用范围 | **仅 Restricted 档 invite**, **不**覆盖 Anyone with link / Public | A: answer/16206563 + 2026-04-21 WebFetch |
| 匿名访问 | **No** — Anyone with link / Public 均需访客 Google 账号 | A: answer/16322204 |
| Workspace Enterprise/EDU 限制 | 禁公开档; Restricted 档无 50-cap (unlimited users + Groups) | A: answer/16206563 |
| Viewer 可见 source 数 | **follows viewer own tier** — Free viewer 看共享 notebook 也最多看 50 sources (来自 "Sharing a notebook does not change the source limit for any collaborator") | A: answer/16213268 |
| **账号类型 ack (用户 2026-04-21)** | **Personal Gmail** — 三档均可用 | 用户 ack |
| **Scope B fallback** | 若未来账号变动限制分享, 通过 `current/UPLOAD_TUTORIAL.md` + 打包 `uploads/` 让接收者自建复刻 (即 "workflow_replication 分享" — 补丁候选 #6) | 用户 ack 2026-04-21 |
| **v2 使用策略** | 默认 Restricted 档私有; 需小圈分享时邀请同事 (50-cap 内); 需广覆盖时切 Anyone with link; 需画廊发现时切 Public | v2 架构 |

---

## F. 失败模式 (Known Issues) — Phase 1 调研补全

| # | 现象 | 缓解 |
|---|------|------|
| 1 | Audio Overview 会在生成播客时 hallucinate 细节 (社区观察) | 听完后做一次 citation 核对, 或 Pro 版用 instructions 约束 |
| 2 | Mind Map 对长 source 可能遗漏深层概念 | 分层合并 source (核心概念 bucket 独立) |
| 3 | Indexing silent fail (官方承认) | 单 source 上传后点 tile 预览确认, 批量后做 smoke 问答验命中 |
| 4 | YouTube / 长音频转写偶有丢段 | 不依赖音频源做关键测试 (本项目只用 md 源) |
| 5 | 公开档访客的 chat 历史不写回 notebook 本体 | 收集分享场景反馈单独做 (Phase 3 实测后置) |

---

## G. A/B 矩阵侧重 — 本平台独有能力

| 能力 | 测试题类型 | 评估方式 |
|------|----------|---------|
| Audio Overview 内容保真 | 随机选 1 个 domain, 生成 Audio Overview, 人工听一遍勾事实错误数 | Pro 版加 instructions "基于 source 绝不脑补" 后再测, 对比 |
| Mind Map 完整度 | 选一个跨 domain 概念 (如 RELREC 关系网), 看 Mind Map 是否覆盖全部相关 domain | 人工对照源文件 checklist |
| Study Guide 分层深度 | 选一个 domain 生成 Study Guide, 检查是否覆盖 Standard → IG → Examples 三层 | 对照知识库源文件 |
| Citation 回链精确度 | 问具体条款, 看引用是否精确指向对应 md 行区间 | 随机 5 题, 点每个 citation 核对 |
| Timeline / Briefing Doc 质量 | 选"SDTM IG 历史版本演进" 类题 | 人工检查事实 |

范本 `06_review.md` 的标准 A/B 矩阵 (10 题问答) + 本段 5 题独有产出 = 本平台 A/B 题量 **15** (**单 notebook**, 总 15 题次; 非 v1 的 3×15=45).

---

## H. 内容策略的关键决策点 (v2 重写)

| 决策 | 本平台适用 |
|------|----------|
| 是否分批? | **不分批** — 单次 ≤50 source 一次上完 |
| 是否需要 Deferred stub? | **不需要** — 单 source 500K words 上限远超 SDTM 最大单文件 |
| 是否需要 capacity calibration? | **不需要** — 容量透明 |
| **Multi-notebook 策略?** | **No — 1 notebook 足够** — ABC 三场景 (个人学习 / 小圈分享 / 公开分享) 在同一 notebook 内按 §E 分享档位切换实现. 决策依据: UI 3 档可切 + 50-cap 仅 Restricted + Free tier viewer 兼容性 + 操作复杂度 + source 数压缩带来的 indexing/citation/Mind Map 质量提升. 详 `archive/v1_.../ARCHITECTURE_PIVOT_RECORD.md` 假设推翻 + v2 PLAN §3 |
| A/B 矩阵大小? | **15 题** (10 标准 + 5 独有产出), **单 notebook 独立判定 PASS** |
| 批次间是否跨批正向激活? | N/A (单批) |
| **Pre-upload audit 必做?** | **Yes** — 即使 Pro 300 cap 很松, 压缩到 ≤50 必须走 concept cluster 重 bucket, `wc -w` 排序确认每 source <500K words 仍是前置步骤 |
| **Source 数上限?** | **≤50** (主动压缩到 Free tier 兼容水位) — 6 条独立理由: (1) Free tier viewer 兼容 (2) indexing silent fail 风险随 source 数线性 (3) citation 信噪比 (4) Mind Map 可读性 (5) upload effort (6) workflow replication 复刻 cap. **Q1 红线反而更易守**: 50 slot 比原 v1 的 30 slot 宽松. 详 PLAN §3 |
| **Chat mode 决策?** | **Custom** 模式 (10K char, SDTM 专家系统 prompt) — 单 notebook 下只能一个 mode, 选最接近 system prompt 的 Custom |

---

## 对 `_template/` 的缺陷补丁候选 (v2 更新)

本平台揭示的范本盲区 (收束时合并回 `ai_platforms/_template/`):

1. **00_platform_profile §D** 把 "Custom Instructions" 作为必答字段, 但对无 system prompt 概念的平台 (NotebookLM 类) 没有退化路径. 补丁: 加"等价物映射"子段
2. **00_platform_profile §G** A/B 侧重只列了 Claude/ChatGPT/Gemini 的 chat-first 能力, 未覆盖"平台独有生成物"(Audio / Mind Map / Study Guide / Briefing 等). 补丁: 加"生成物类平台"子节
3. **05_solution.md** 的"System Prompt 累积段设计"对 NotebookLM 不适用. 补丁: 加 if/else 分支, 无 system prompt 平台改为"首源导航 + Chat custom goals 文本"
4. **03_research.md Q8 calibration** 对容量透明平台是浪费. 补丁: Q8 加"前置判定: 官方是否公开精确限额? Yes → 跳过 calibration"
5. **"一个平台 = 一套知识库" 隐含假设不全** — 但 v1 原打算升级为 "默认 multi-notebook", v2 修正: 加 "**multi-notebook 是否必要的决策树**" — 典型场景 1 notebook 足够, 仅当 ABC 场景需职责分离到不同 collaborator 圈 (e.g. 同 org 内不同 team 互不可见) 才升级多 notebook. 补丁: `05_solution.md` 加 multi-notebook 决策树 + 典型反例 (本平台 1 notebook)
6. **"分享" 维度只建模链接分享** — 未覆盖 "workflow_replication 分享" 作为 fallback (Workspace 账号禁公开链接时, 通过 UPLOAD_TUTORIAL + 打包 uploads/ 复刻). 补丁: `00_platform_profile §E` 加 `share_mode` 子段 (direct_link / workflow_replication)
7. **未对齐 "tier 重命名漂移" 风险** — NotebookLM "Plus" 2025 H2 改名 "Pro". 同 SKU 词 12 月内语义翻转. 补丁: `03_research.md` Q2 加 "历史重命名警示", Phase 1 强制列时间线 (本平台 Q3 作范例)
8. (v1 补丁候选 #8 "per-day rate limit") — **保留** (独立于架构)
9. (v1 补丁候选 #9 "source 隔离 hard rule") — **降级** — source 隔离仍是事实, 但单 notebook 下无跨 notebook 引用需求, 不再是 hard rule. 改为 "**若选多 notebook 必须认识 source 隔离代价**" 信息段
10. (v2 新增) **"Writer 叙事合成易生伪约束" 范例** — v1 Q7 把 "Mode A vs Mode B 可叠加" 叙事合成成 "本质两选一", 引伸出 3 notebook 架构. 补丁: `03_research.md` 末尾加"Writer 立场警示" — 陈述事实 (两模式可叠加) 到结论 (必须两 notebook) 跳跃一步必须质询

---

## 填空完成度

- A 身份: 100%
- B 检索机制: 95% (Phase 3 实测 indexing 时间占 5%)
- C 文件管理: 85% (Phase 3 实测 indexing 时间 + 上传耗时)
- D Prompt: 100% (Chat custom goals Custom mode 敲定)
- E 分享: 100% (v2 三档模型 + 档位切换策略敲定)
- F 失败模式: 80% (Phase 3 补)
- G A/B 侧重: 90%
- H 决策: 100% (1 notebook × ≤50 v2 策略敲定)

**加权平均 ~94%** → Phase 1 Writer 完成 2026-04-21, Reviewer 已过 (Rule D), Phase 2 PLAN v2 可启.

---

*v2 重写日期: 2026-04-21 (架构 pivot 同日). 来源: Phase 1 research.md v2 八问八答 + 用户 UI 实测 + 三 WebFetch 核实.*
