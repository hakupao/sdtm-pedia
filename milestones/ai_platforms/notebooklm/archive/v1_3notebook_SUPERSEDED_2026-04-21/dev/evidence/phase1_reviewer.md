# Phase 1 Reviewer 报告 — NotebookLM research.md 独立核对

- 审核日期: 2026-04-21
- Reviewer subagent: oh-my-claudecode:verifier (opus)
- Writer subagent: general-purpose (已完成, Rule D 合规 — 不同 subagent_type)
- 审核对象: `ai_platforms/notebooklm/docs/research.md` (392 行, 8 问 + 4 独有段 + PLAN 修订 + Writer self-report)
- 核对手段: WebFetch × 9 个 URL + WebSearch × 4 个独立关键词

---

## 维度 1 — 链接有效性 (WebFetch 抽样)

| # | URL | HTTP | 核对点 | 一致度 |
|---|-----|------|--------|--------|
| 1 | `support.google.com/notebooklm/answer/16213268` (Upgrade) | 200 | 四 tier 数字 (500/300/500/20 Pro) | ✅ **完全一致** |
| 2 | `support.google.com/notebooklm/answer/16322204` (Public notebooks) | 200 | 公开链接 consumer-only, 禁 Workspace Enterprise/EDU, 访客需 Google 账号 | ✅ **完全一致** (原文 "Public sharing is only enabled for consumer accounts") |
| 3 | `blog.google/feed/notebooklm-google-one/` | 200 | Plus 并入 Google One AI Premium | ⚠️ **部分** (Plus 并入属实, 但页面未给精确日期; 未提 "改名 Pro") |
| 4 | `workspaceupdates.googleblog.com/2025/03/new-features-available-in-notebooklm.html` | 200 | 2025-03 Mind Map + output language selector | ⚠️ **部分** (Mind Map + language 属实, 但**未**发布 chat mode selector — Writer Q6 此处归因错误, 见维度 2 #6) |
| 5 | `9to5google.com/2026/04/11/google-ai-pro-ultra-features/` | 200 | Plus → Pro 改名 + Pro tier 数字 | ✅ **完全一致** 原文 "The paid tier for Google's research tool was previously called NotebookLM Plus" |
| 6 | `9to5google.com/2025/06/03/notebooklm-public-links/` | 200 | 50 users 上限 + personal Gmail | ⚠️ **链接存在但不支撑 Writer 断言** (WebFetch 读到的 2025-06-03 文章**未提** 50-users 上限, 该数字实际来自官方 Help 页 + androidauthority; Writer 引用归因有误) |
| 7 | `en.wikipedia.org/wiki/NotebookLM` | 200 | Plus → Pro 改名时间线 | ⚠️ **反证** (Wikipedia 截至 2026-04-07 仍只提 "NotebookLM Plus", 未更新改名 — 不构成否认改名, 但不能作为 Q3 改名证据) |
| 8 | `support.google.com/notebooklm/answer/16269187` (FAQ) | 200 | 500K words/source 限额 | ✅ **权威来源** 原文 "The current limit is 500,000 words per source or up to 200MB for local uploads" |
| 9 | `blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/` | 200 | Chat custom goals 发布日期 | 🆕 **新证据** 发布于 **2025-10-29**, "custom goals" feature, 官方未把它叫 "mode selector", 而 help 页当前 3 mode: Default / Learning Guide / Custom (无 Analyst) |

**额外抽样 (C 级)**:
- `notebooklm.google/plans` WebFetch 返回 content 不全 (页面 SPA, 抓不到详细表), 但标题直接显示 "Google NotebookLM **Pro** | Premium AI Research..." — **官方 landing page 已用 "Pro"**, 是 Pro 改名的最强 A 级间接证据.

---

## 维度 2 — 关键数字断言核验

| # | 断言 | 预期位置 | 核验结果 | 依据 |
|---|------|---------|---------|------|
| 1 | Pro tier = 500 notebooks × 300 sources × 500 chat × 20 audio/day | Q2 四档表 | ✅ | 官方 Upgrade 页 + 9to5google 2026-04-11 双独立源完全吻合 |
| 2 | Free/Standard = 100 notebooks × 50 sources × 50 chat × 3 audio | Q2 Free 行 | ⚠️ (数字对, 名称错) | 官方 Upgrade 页用 **"Standard"** 而非 "Free"; research.md Q2 全程用 "Free". 虽然社区通用 "Free", 但官方正名是 Standard, Phase 2 PLAN 应明示这点漂移 |
| 3 | 500K words/source 全档统一 | Q2 脚注 + Steven Johnson X | ✅ | 官方 FAQ 页明示 "500,000 words per source", WebSearch 进一步确认 "the individual source word limit of 500,000 words remains consistent across all plans"; Upgrade 页表里确实没列 words/source (Writer 原话"官方 upgrade 页 4 tier 数字全部列出"略过头), 实际 words 数据仅 FAQ 页有. 结论数字对, 归因溯源稍粗 |
| 4 | Audio 单位 per-day 而非 per-month | Q2 + Writer self-report | ✅ | 官方 Upgrade 页原文 "Daily quotas are reset after 24 hours; monthly quotas are reset after 30 days" |
| 5 | 公开链接仅 personal Gmail (Workspace Enterprise/EDU 禁) | Q7 + Writer self-report | ✅ | 官方 Help 原文 "Public sharing is only enabled for consumer accounts. It's currently disabled for Workspace Enterprise or Education accounts." |
| 6 | 50 users 邀请上限 (personal Gmail) | Q7 + 9to5google 2025-06-03 | ⚠️ (事实对, 归因错) | 事实: 50-users **仅指直接邀请上限**, 公开链接本身**无 users 上限**, 需 Google 账号即可. Writer Q7 "公开链接 ... 50 users 邀请上限" 合并两概念, 分享模型需分开表述. 归因: 9to5google 2025-06-03 WebFetch 显示该文章**未**提 50 数字, 数字实际源自官方 Help + androidauthority. Phase 2 PLAN Scope B 必须区分 `invite_direct` (50 cap) vs `public_link` (无 users cap) 两模式. |
| 7 | 原 "Plus" 2025 H2 改名 "Pro" | Q3 时间线 + 9to5google 2026-04-11 | ✅ (属实, 见维度 4) | 9to5google 2026-04-11 明说 "previously called NotebookLM Plus"; notebooklm.google/plans 页标题现为 "Google NotebookLM Pro"; WebSearch 补充 "At I/O 2025 ... rebranded". 三独立源. |
| 8 | Chat mode selector (Guide/Analyst/Custom) 2025 H2 新增 | Q6 + Workspace Updates 2025-03 | ❌ **重大错误** | Writer Q6 把 chat mode selector 归为 "Workspace Updates 2025-03 新增". 实际: (a) 2025-03 Workspace Updates 只发 Mind Map + output language selector, **无** mode selector; (b) 官方 chat 页当前只有 Default / Learning Guide / Custom **3 mode 非 4**, 无 Analyst (Analyst 来自三方文章混入); (c) "custom goals" 实际 blog.google 2025-10-29 发布, 非 2025-03. 需 Writer 在 Q3 时间线 + Q6 + self-report 三处更正. |

---

## 维度 3 — Unverified 清单严格性

Writer self-report 列 7 条 Unverified, 逐条审查:

| # | Unverified 项 | 审查结论 | 建议动作 |
|---|--------------|---------|---------|
| 1 | Embedding 模型具体型号 (`gemini-embedding-001` 推测) | **合理 Unverified** — Google 确无公开确认, 仅推测合理 | 维持 UNVERIFIED, Phase 3 不实测 (黑盒) |
| 2 | Chunk size (~500 tokens 社区估) | **合理 Unverified** — 无官方披露 | 维持 UNVERIFIED |
| 3 | Audio Overview hallucination 模式细节 | **可实测消除** — Phase 3 可上 1 domain, 听一遍打分 | 升级为 Phase 3 实测 item (A/B 矩阵 audio fidelity 题已涵盖, 但要加 "hallucination 模式分类" 维度) |
| 4 | Mind Map 长源深层覆盖衰减 | **可实测消除** — SDTM 有 293 md 体量可直接验证 | 升级为 Phase 3 实测 (A/B mind map coverage 题需含 "长 md vs 短 md 覆盖差异"子题) |
| 5 | 公开链接访客问答是否回写 owner chat history | **可实测消除** — 造 1 sandbox notebook 开公开链接自测 | 升级为 Phase 3 实测, 列入 Scope B 专项 |
| 6 | Words → tokens 换算比 (100 tokens ≈ 75 words) | **合理 Unverified** — 官方无口径, 本项目用 `wc -w` 数 words 即可, 不需 tokens 换算 | 维持 UNVERIFIED, Phase 2 PLAN 明示"不做 tokens 换算" |
| 7 | Indexing 实际等待时间数字 | **可实测消除** — Phase 3 三场景 (单 md / 单 PDF / 批量) 实测即可 | 已在 research.md Q5 列 TODO, Phase 2 PLAN Phase 3 节点需 explicit |

**判断**: Writer 对 "无官方披露" 部分标 Unverified 保守合理; 但 4 条可实测项 (3/4/5/7) 应升级为 Phase 3 action items 而非停留 Unverified 状态. 这不是 Writer 漏查, 是归档细度问题.

---

## 维度 4 — Plus/Pro 改名证据充分性

**WebSearch 独立来源搜索**:

| 来源 | 证据强度 | 原文 |
|------|---------|------|
| `notebooklm.google/plans` 页标题 | **A 级 (官方 landing)** | 标题 "Google NotebookLM **Pro** | Premium AI Research & Brainstorming Tool" — 官方已直接用 Pro |
| 9to5google 2026-04-11 | C 级 (Writer 已引) | "The paid tier for Google's research tool was previously called NotebookLM Plus" |
| WebSearch "NotebookLM Plus renamed Pro" 结果汇总 | C 级 (第二独立源) | "At I/O 2025, Google One AI Premium (and Gemini Advanced) became 'Google AI Pro,' and AI Pro bundles access to NotebookLM Pro features"; "NotebookLM Plus was renamed to NotebookLM Pro as part of Google's broader rebranding of its AI subscription tiers in 2025" |
| Wikipedia (2026-04-07 最新) | C 级 (反证) | 仍只提 "NotebookLM Plus", 未更新改名条目 — **不否认** 但需注意 Wikipedia 滞后 |
| 官方 Upgrade Help 页 | A 级 | 四档表用 Standard / Plus / Pro / Ultra 四档**现行**名称 (不含 "Plus 曾改名 Pro" 的 erratum 说明) |

**结论**: **改名属实** (1 A 级官方 landing + 1 A 级 help 表 + 2 独立 C 级背书) — 但有 nuance 需 Writer 修订:

- 当前 tier 结构是 **Standard / Plus / Pro / Ultra 四档并存** (不是 "Plus→Pro 的 2 档改名"), 原 "NotebookLM Plus" (对应旧 Google One AI Premium, 当时只 1 档付费) 在 Google AI Pro/Ultra 新两档出现后, 名字重新分配给中档 (~$19.99 AI Pro 下游是 NotebookLM Pro, ~$9.99 AI Plus 下游是 NotebookLM Plus 新档).
- Writer Q3 时间线末尾说 "2025 下半年-2026 原 'Plus' 改名为 'Pro', Tier 重组为 Free/Plus/Pro/Ultra 四级" 描述基本正确但口径粗, 未说明"原 Plus 规格直接上移变 Pro, 新中档用 Plus 这个原名"的漂移本质.
- Wikipedia 未更新**不是**改名存疑, 是 Wikipedia 滞后, 但 PLAN_V2 / platform_profile §A 的 `tier_naming_drift` 补丁候选需重写:**警示的不是 "改名了"**, 而是**"同一 SKU 词语义在 12 月内翻转"**, 训练数据 (截至 2026-01) 前时点的 "Plus=300 sources" 到当前时点的 "Plus=100 sources" 数字不同.

**最终判定**: 改名属实, **但 Writer 措辞需修订**为"SKU 命名语义漂移" (Plus 从最高档下沉到中档, Pro 从不存在变最高档, 规格上移).

---

## 维度 5 — 重大遗漏排查

| # | 维度 | 研究覆盖? | 证据/建议 |
|---|-----|----------|---------|
| 1 | Audio Overview 输出语言 (SDTM 内容英文, 用户中文, 能否双语?) | ⚠️ 部分 | §9 提了 "80+ languages, 但发音仅英文高质量, 其他语言可用但可能有口音/glitch". 但**未明示** "notebook sources 英文 + Audio 输出中文"是否可行 — 这是 SDTM 特有场景. **建议 Phase 3 实测**: 上 1 英文 domain 源, 生成中文 Audio Overview, 评估可读性 + 术语准确率. Scope C (音频补充) 设计决策点. |
| 2 | Pro tier 每 chat 的上下文窗口 (500 chat/day 是频次, 每 chat 能吃多少 token?) | ❌ **遗漏** | research.md 没涉及单次 chat 输入/输出 token 上限. Gemini backbone 理论 1M 输入 + 64K 输出 (Gemini 2.5 Pro 起), 但 NotebookLM 封装层可能下调. **建议 Phase 1 补充一问** 或 **Phase 3 smoke test 最大输入长度**. |
| 3 | Mind Map / Study Guide / Briefing Doc 更新节奏 (上传新 source 后是否自动刷新?) | ❌ **遗漏** | research.md §10 只讲 mind map 生成, 没讲增量 source 触发重新生成的机制. 对 SDTM 批量上传 + 后续补丁场景至关重要. **建议 Phase 3 实测**: 先建 notebook 生成 Mind Map, 再加 1 source, 看 Mind Map 是否自动/手动刷新. |
| 4 | source 修改后 Indexing 增量还是全量 | ❌ **遗漏** | research.md Q5 只讲初次 indexing, 不讲 source **修改** (re-upload) 后的 re-index 机制. 训练数据里模糊, 需 Phase 3 实测 — 特别是对有 "v1→v2 知识库更新" 计划的项目 (本项目未来可能更新). **建议 Phase 3 加 1 场景**: 修改 1 md 重新上传, 测问"该 md 新增片段"的召回. |
| 5 | 公开链接受众是否需 Google 账号 (Writer 已说"Google 账号无匿名") | ✅ | Q7 + WebFetch 官方 Help 原文 "share the link to anyone with a Google account to have them view your notebook" 已明确. |

**4/5 项存在遗漏或需实测**, 遗漏集中在 "运行时/增量行为" 这块 — Writer 做了 well-grounded 的静态调研, 但对 "notebook 运行起来之后" 的动态行为没深入. 建议 Phase 2 PLAN 加一段 "运行时行为实测 item 清单".

---

## 最终判定

- **判定**: **CONDITIONAL_PASS**
- **置信度**: **78%** (数字主干对, 但 1 个重大事实错误 + 1 个归因错误 + 2 个口径错误 + 2 个遗漏需补)
- **Rule D 合规**: ✅ (Writer = general-purpose, Reviewer = oh-my-claudecode:verifier, 不同 subagent_type)
- **为何不直接 PASS**: Writer Q6 把 chat mode selector 错归为 2025-03 发布 (实际 2025-10-29 custom goals, 且当前 3 mode 无 Analyst) 属事实错误; 维度 5 有 2 项遗漏影响 Phase 2 PLAN 完整性. 这两项**必须回记后才能进 Phase 2**.
- **为何不 FAIL**: 主干数字 (Pro tier 四列 + 公开链接规则 + 500K words + per-day audio) 全部核对通过, 核心 PLAN 修订 10 条方向正确, 不构成 Phase 2 重启.

### 需回记 (按严重度降序, 主 session 执行)

**重度 (必改, 否则 Phase 2 PLAN 基础不牢)**:

1. **research.md Q6 + Q3 时间线 + self-report 三处修订 chat mode selector 归因**:
   - Q6 "Chat mode selector (Guide/Analyst/Custom) 2025 下半年新增" → "Chat custom goals (Default / Learning Guide / Custom 3 mode, 其中 Custom 模式 Plus+ 可自定 goal/voice/role) 2025-10-29 由 blog.google 发布"
   - Q3 时间线 "2025-03 Mind Map + output language selector" 后**删除** "chat mode selector" 的暗示; 2025-10 一行新增 "Chat custom goals 发布"
   - Writer self-report 相关条 URL 换成 `blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/` (不再用 workspaceupdates 2025-03 为 mode selector 背书)
   - 证据: WebFetch 两页对比

2. **research.md Q3 + PLAN 修订 #1 + platform_profile §A + _progress.json tier_naming_drift 四处修订 Plus/Pro 改名口径**:
   - 措辞 "原 'Plus' 改名 'Pro'" → "SKU 命名语义漂移: 原单档 NotebookLM Plus (对应旧 Google One AI Premium) 在 I/O 2025 Google AI Pro/Ultra 两档引入后, 规格上移改名为 NotebookLM Pro; 'Plus' 这个 SKU 词被重新赋给新中档 (对应 Google AI Plus ~$9.99)"
   - platform_profile §A 套餐行补一句 "⚠️ 训练数据截至 2026-01 的 '100 sources/notebook' 对应旧 Plus, **不** 等于新 Pro 的 300"

3. **research.md Q7 + PLAN 修订 #9 两处分离"邀请"与"公开链接"两种分享模式**:
   - 当前 "公开链接 + 50 users 邀请上限" 合并表述, 应拆成:
     - 模式 A: **个人邀请** (直接加 email) → personal Gmail 50 users 上限, Workspace Enterprise/EDU 无上限
     - 模式 B: **公开链接** ("Anyone with a link") → 仅 personal Gmail 可开, 无访问者数字上限, 需 Google 账号
   - 50 users 数字的 WebFetch 归因修正: 来自官方 Help + Android Authority, **不是** 9to5google 2025-06-03

**中度 (应改, 影响完整度)**:

4. **research.md Q2 + platform_profile §A 免费档命名**: "Free" → "Standard (官方命名; 社区通称 Free)"; 或至少在 Q2 首次出现处注一句 "Free tier 官方名 Standard, 后文沿用社区惯例 Free"

5. **research.md Q2 溯源细化**: "官方 upgrade 页 4 tier 数字全部列出" → "官方 upgrade 页列 notebooks/sources/chat/audio 四维四档; 500K words/source 规格见 FAQ 页 `answer/16269187`" (分开两个 Help URL 的责任)

**低度 (补充到 Phase 3 action items 清单即可, 不回灌 Phase 1)**:

6. **research.md 末尾新增一段 "Phase 3 运行时实测 item 清单"** (收集所有可实测 Unverified):
   - I1: 单 md / 单 PDF / 批量 293 md 三场景 indexing 耗时
   - I2: 修改 1 source 重传, re-index 增量/全量判定
   - I3: 添加 source 后 Mind Map / Study Guide 自动刷新 vs 手动
   - I4: 英文 sources + 中文 Audio Overview 可读性 + 术语准确率
   - I5: 公开链接访客问答是否回写 owner chat history
   - I6: 单次 chat 最大输入长度 (Pro tier 实际 cap)
   - I7: Audio Overview hallucination 模式分类 (跨 source / 长 source / interactive 三子类)

7. **_progress.json notes 数组新增一条** 记录本次 reviewer 发现的 chat mode selector 归因错误, 供 retrospective 参考.

---

## Carry-over 到 Phase 2 (PLAN 必做项)

- C2.1 PLAN §0 套餐行采用 "Pro (via Google AI Pro 订阅)" 口径, 注脚 tier_naming_drift 警示 (参考维度 4 的 SKU 语义漂移本质)
- C2.2 PLAN Scope B 分享章节**明确区分** `invite_direct` (50 users cap) vs `public_link` (无 cap, 需 Google 账号) 两模式
- C2.3 PLAN §1 容量表四档必列, 本次路径用 Pro 高亮; Free 行名称标 "Standard (社区通称 Free)"
- C2.4 PLAN §custom_instructions 章节把 "Chat mode selector" 改为 "Chat custom goals" (发布日 2025-10-29), 3 mode + Custom mode Plus+ 独有
- C2.5 PLAN Pre-upload source audit 节点保留 (wc -w 排序 Top 5 outlier md), Phase 2 即做不留 Phase 3
- C2.6 PLAN Phase 3 节点挂 I1-I7 清单 (见回记第 6 条), 每 item 明示 pass 判据
- C2.7 PLAN multi-notebook 架构段明确 source 严格隔离 (每 notebook 独立 300 source 预算, notebook 2/3 不能引用 notebook 1 source)
- C2.8 PLAN A/B 矩阵 15 题定型: 10 smoke v2 + 5 独有 (2 audio + 2 mind map + 1 study guide), 每 notebook 独立判 PASS, 阈值 13/15 (~87%)

---

## Carry-over 到 Phase 3 (实测项)

- I1 (indexing): 单 md 上传即时提问独有关键词, 记召回时间; 单 PDF 同测; 批量 293 md 测"全量就绪"时间
- I2 (re-index): 修改 1 md 重传, 测"新增片段"召回
- I3 (mind map 刷新): 建 notebook 生成 Mind Map, 加 1 source, 观察自动/手动刷新
- I4 (audio 双语): 英文 sources 生成中文 Audio Overview, 人工评估术语准确率 / 口音 / glitch 率
- I5 (公开链接回写): sandbox notebook 开公开链接, 另账号匿名问 3 题, 测 owner chat history 是否写入
- I6 (chat 输入长度): 分别以 50K / 200K / 500K words 量级 prompt 测 Pro tier 单次 chat 上限
- I7 (audio hallucination): 跨 source / 长 source / interactive 三子类各生成 1 次, 人工标注 hallucination 条数
- 回归 A/B 15 题矩阵 × 3 notebook = 45 题次

---

*本次 Reviewer lane 作业独立完成, 产物仅本文件; 不改 research.md / platform_profile.md / _progress.json, 由主 session 决定回记节奏.*
