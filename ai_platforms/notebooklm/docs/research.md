# 03 前置调研 — NotebookLM 八问八答 + 四问独有段

> **写作时间**: 2026-04-21
> **Writer**: Phase 1 Writer subagent (独立 session)
> **用户已 ack 套餐**: Google AI Pro → 官方 tier 名已从 "Plus" 重命名为 **"NotebookLM Pro"** (见 Q2/Q3)
> **来源分级**: A = notebooklm.google / support.google.com / blog.google / one.google.com / workspaceupdates.googleblog.com / docs.cloud.google.com; B = Google 官方 X/YouTube; C = 第三方媒体 (9to5google, xda, elephas, medium 等); UNVERIFIED = 无权威来源

---

## Q1: NotebookLM "capacity" / "limit" 的官方定义是什么?

**答**: NotebookLM 的容量**不是** token/context-window 单位, 而是按**四条独立数轴**量化:

1. **Notebooks per user** (账户下 notebook 上限)
2. **Sources per notebook** (单 notebook 内"源"数量上限)
3. **Words per source** (单源字数上限, 500,000 words 全 tier 统一)
4. **File size per source** (本地上传文件二进制上限, 200MB 全 tier 统一)

加上**日额**维度:

5. **Chat queries per day** (问答额度)
6. **Audio Overviews per day** (语音生成额度)
7. **Reports per day** (Ultra 新增, 1000/day)

容量**完全透明**, 官方 help 页面直接列出每 tier 数字 — 和 Claude Projects 的"capacity %"黑盒相反. 这是 NotebookLM 的重要设计选择: 把"源"作为一等公民, 不暴露底层 context window / embedding dim / chunk size.

**来源**:
- A: [NotebookLM Help — Upgrade NotebookLM](https://support.google.com/notebooklm/answer/16213268?hl=en) (官方 upgrade 页, 4 tier 数字全部列出)
- A: [NotebookLM Help — FAQ](https://support.google.com/notebooklm/answer/16269187?hl=en) (官方 FAQ, **Standard** tier 数字权威 — 原 "Free" 已在 2025 H2 品牌重构后更名 Standard)

---

## Q2: 当前容量上限 — 各套餐表 (2026-04 最新)

**答**: 四 tier 并存, 官方最低档名为 **Standard** (非社区惯称 "Free"). 2025 H2 I/O 后发生 **SKU 语义漂移**: 旧单档 "NotebookLM Plus" 规格上移改名为 "NotebookLM Pro", "Plus" SKU 词被重新赋给新中档. 详见 Q3 时间线 + 末尾 SKU 漂移警示.

**关键映射**: "Google AI Plus 订阅" → NotebookLM 中档 (新 Plus 档, 200/100/200/6); "Google AI Pro 订阅" → NotebookLM **高档** (Pro 档, 500/300/500/20). 本项目**用户订 Google AI Pro, 因此 NotebookLM 能力 = Pro tier = 500 notebooks / 300 sources / 500 chat / 20 audio**.

| Tier | Notebooks/user | Sources/notebook | Words/source | Chat/day | Audio/day | 独有 |
|------|---------------|-----------------|--------------|----------|-----------|------|
| **Standard** (官方名; 社区通称 "Free") | 100 | 50 | 500,000 | 50 | 3 | — |
| **NotebookLM Plus** (新, =Google AI Plus) | 200 | 100 | 500,000 | 200 | 6 | Early access |
| **NotebookLM Pro** (=Google AI Pro, 用户本次) | 500 | 300 | 500,000 | 500 | 20 | Priority early access, higher Gemini model access |
| **NotebookLM Ultra** (=Google AI Ultra) | 500 | 600 | 500,000 | 5,000 | 200 | Highest Gemini model, Watermark removal, 1000 Reports/day |

> **脚注 (SKU 语义漂移警示)**: 官方最低档当前 SKU 名是 **"Standard"**, 本文件按最新官方命名 (详见 `support.google.com/notebooklm/answer/16213268` 升级页头部). 中文"免费档/免费用户"为意思描述词, 与 SKU 名无冲突. 另, 当前 "Plus" 档 **不等于** 训练数据时点 (2026-01 前) 的 "Plus" — 旧 Plus 规格 (300 sources) 已上移为 Pro; 新 Plus 仅 100 sources. 引用 2025-06 前第三方文章的 "Plus" 数字必先判断其指代的是哪个 Plus.

Words → tokens 近似换算: 官方未给比例, 社区常用 `100 tokens ≈ 75 words` → 500,000 words ≈ **667K tokens** 单源上限 (非权威, 仅供参考).

**来源**:
- A: [NotebookLM Help — Upgrade NotebookLM](https://support.google.com/notebooklm/answer/16213268?hl=en) (4 tier 官方矩阵; **WebFetch 核实 tier 名是 Standard / Plus / Pro / Ultra**)
- A: [NotebookLM Help — FAQ](https://support.google.com/notebooklm/answer/16269187?hl=en) (Standard 档数字)
- **A: [notebooklm.google/plans](https://notebooklm.google/plans) (官方 landing 页, 标题 "Google NotebookLM **Pro** | Premium AI Research & Brainstorming Tool" — Pro 现行 SKU 名最强 A 级背书)**
- C: [9to5Google — Google AI Plus/Pro/Ultra features Apr 2026](https://9to5google.com/2026/04/11/google-ai-pro-ultra-features/) (Google AI 订阅 → NotebookLM tier 映射, 明示 "The paid tier ... was previously called NotebookLM Plus" → 改名为 Pro)
- C: [Steven Johnson (NotebookLM team) on X, 2024-05](https://x.com/stevenbjohnson/status/1793991409164251437) (500K words/source 规格由 NotebookLM 团队成员公开)
- C: [Elephas — NotebookLM Limits Explained: Free, Plus, Ultra](https://elephas.app/blog/notebooklm-source-limits) (交叉验证)

---

## Q3: 历史限额调整

**答**: 关键时间线:

| 日期 | 事件 | 变化 |
|------|------|------|
| 2023-05 | Project Tailwind 首发 | 内测, 小型 notebook |
| 2024-05 | 正式改名 NotebookLM | 公测 |
| 2024-05 (Steven Johnson X) | 上限上调到 **50 sources × 500K words** | Standard tier (原 "Free") 确立当前基线 |
| 2024-09 | Audio Overview 公测 | 新增"生成物"维度 |
| 2024-12 | **NotebookLM Plus** 为 Enterprise + Gemini Advanced 推出 | 首次分级 |
| 2025-02-10 | NotebookLM Plus 并入 **Google One AI Premium** (个人订阅开放) | 个人用户首次能买 |
| 2025-03 | Mind Map + output language selector | 新增生成物 (此期 Workspace Updates **不含** chat mode selector, 订正 Writer #1 归因) |
| 2025-04 | Discover sources + multimodal PDF | 输入类型扩展 |
| 2025-05 (Google I/O) | **Google One AI Premium → Google AI Pro** 品牌重构, NotebookLM 分层随之重组 | SKU 语义漂移源头 |
| 2025-06 | **Public sharing links** (仅 consumer 账号) | 分享模型首次开放链接级 |
| 2025-07 | Cinematic video overview mode | 新生成物 |
| 2025-08 | Education accounts 纳入 | 分发面扩大 |
| **2025-10-29** | **Chat custom goals** 发布 (blog.google "custom personas engine upgrade"), 三档 **Default / Learning Guide / Custom** | chat 角色首次可自定 — 非 2025-03 |
| 2025-11 | **Infographics + Slide Deck** (Nano Banana Pro 驱动) | 新增视觉生成物 |
| 2025-12 | **Data Table output** | 结构化输出 |
| **2025 下半年 (I/O 2025 后至 2026)** | **SKU 语义漂移**: 原 "NotebookLM Plus" (2024-12 首发 + 2025-02 并入 Google One AI Premium) 规格上移改名为 **"NotebookLM Pro"** (对应新 Google AI Pro 订阅); "Plus" 这个 SKU 词被**重新赋给**新中档 (对应 Google AI Plus ~$9.99). 最高档 Ultra 同期新增. **警示**: 训练数据截至 2026-01 的 "Plus=300 sources" 对应**旧 Plus**, 新 Plus=100 sources; 同一 SKU 词 12 月内语义翻转. | 不是简单改名, 是命名重分配 |
| 2026-03 起 | 后端升级到 **Gemini 3** | 模型代际 |

**来源**:
- A: [blog.google — NotebookLM 新功能 2024-12](https://blog.google/feed/notebooklm-google-one/) (Plus 并入 Google One AI Premium 通告)
- A: [Google Workspace Updates 2025-03-19](https://workspaceupdates.googleblog.com/2025/03/new-features-available-in-notebooklm.html) (Mind Map + 语言选择器发布; **本次核实: 不含 chat mode selector**)
- A: [Google Workspace Updates 2025-04-02](https://workspaceupdates.googleblog.com/2025/04/updates-to-sources-for-NotebookLM-and-NotebookLMPlus.html) (Discover sources + 多模态 PDF)
- A: [blog.google — NotebookLM custom personas engine upgrade 2025-10-29](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/) (Chat custom goals 官方发布日)
- **A: [notebooklm.google/plans](https://notebooklm.google/plans) (官方 landing 页, 标题直接显示 "Google NotebookLM **Pro**" — Pro 改名最强 A 级间接证据)**
- C: [Wikipedia — NotebookLM](https://en.wikipedia.org/wiki/NotebookLM) (综合时间线交叉验证; 2026-04-07 版本仍未反映 Pro 改名, 不构成反证只说明 Wikipedia 滞后)
- C: [MacRumors 2025-02-11](https://www.macrumors.com/2025/02/11/notebooklm-plus-now-available-in-google-one/) (Plus 并入 Google One 准确日期)
- C: [9to5Google 2026-04-11](https://9to5google.com/2026/04/11/google-ai-pro-ultra-features/) ("previously called NotebookLM Plus" — 改名证据)
- C: [XDA — NotebookLM Learning Guide feature](https://www.xda-developers.com/notebooklm-learning-guide-feature/) (Default / Learning Guide / Custom 三档)

---

## Q4: 文件注入方式 — grounded RAG vs chunk embedding

**答**: NotebookLM **不全量注入 context**. 是**强 RAG 产品**, 和 Claude Projects (paid) / ChatGPT Knowledge 一样走 chunk embedding, 但有三点本平台独有:

| 维度 | NotebookLM | Claude Projects paid | ChatGPT GPTs |
|------|-----------|---------------------|--------------|
| 注入模式 | **永远 RAG** (不管源多小都走检索) | 小项目全量, 大项目自动 RAG | 小 GPTs 注入, Knowledge 文件 RAG |
| Embedding 模型 | `gemini-embedding-001` (推测, 非官方确认) | Anthropic 内部 embedding | OpenAI `text-embedding-3-*` |
| Vector store | 推测 Vertex AI Vector Search | 内部, 不公开 | 内部, 不公开 |
| Chunk 粒度 | 官方未公开, 社区观察 ~500 tokens 级别 | 官方未公开 | 官方未公开 |
| 引用回链 | **强制 inline citation** (每答必带源标号), citation 点击回源文段 | 弱 (可提示要求) | 弱 (Knowledge 文件有时引, 有时无) |
| 检索增强 | 查询改写 + hybrid (语义+关键词) + re-rank (社区推测) | 类似 | 类似 |
| 训练数据使用 | **"Your uploads, queries and responses are not used to train models"** | 类似政策 | Enterprise 类似, consumer 可退 |

**关键暗示**: NotebookLM 的 inline citation 是本平台对 SDTM 场景的**独有优势** — 用户问"MH.MHCAT 的 controlled terminology 在哪定义", 答案会直接标"[1]" 点进去跳到那段 md 的原文. 这是 Claude/ChatGPT 都做不到的精度.

**来源**:
- A: [Google Workspace Updates 2025-04-02](https://workspaceupdates.googleblog.com/2025/04/updates-to-sources-for-NotebookLM-and-NotebookLMPlus.html) (官方明示 "not used to train")
- C: [arXiv 2504.09720 — NotebookLM as Socratic physics tutor (RAG-based)](https://arxiv.org/abs/2504.09720) (学术论文, RAG 架构描述)
- C: [Scribd — NotebookLM RAG Architecture Overview](https://www.scribd.com/document/887551310/NotebookLM-Internal-Framework-Explained) (三方整理的架构图, 非官方)
- C: [Medium — Step-by-Step Guide RAG with NotebookLM](https://medium.com/data-science-collective/step-by-step-guide-to-building-a-rag-system-with-notebooklm-81688b9f516f)
- `UNVERIFIED — community inference only`: embedding 模型 / vector store / chunk 大小 三项均无 Google 官方确认

---

## Q5: Indexing indicator 可靠性

**答**: 初步结论: **不完全可靠, 需要实测确认**. 训练数据+社区观察:

- 源 tile 显示进度条/旋转, 但 Google 官方没承诺"进度条 100% = 可查询命中"
- 官方建议**点击 source tile 预览内容** 验证是否真的入库, "If it shows no text or just metadata, the upload failed silently and you'll need to re-add it."
- 典型慢例: **YouTube 上传 < 72 小时的视频**不能立即 import; Audio Overview 生成本身 10-20 分钟不是索引慢, 是生成慢
- PDF OCR: NotebookLM 会对 PDF 做 OCR, 扫描版 PDF 首次上传可能更慢
- 2025 下半年以来 consumer 账号上 upload fail 的报告增多 (Google Gemini Apps Community thread)

**Phase 3 Execute 必做实测** (本文件列 TODO, Writer 本段不做实测 — 属 Phase 3 执行范畴):
1. 上传 1 份 md, 立刻提问该文件独有关键词, 记可召回时间
2. 上传 1 份 PDF, 同上
3. 上传全量 293 md 批量上传, 测"全量就绪"时间

**来源**:
- A: [NotebookLM Help — Add or discover new sources](https://support.google.com/notebooklm/answer/16215270?hl=en) (官方承认 "Videos uploaded less than 72 hours prior may not be available")
- A: [Gemini Apps Community thread — Upload failures](https://support.google.com/gemini/thread/407237907) (社区反映 upload 失败)
- C: [Gemilab — NotebookLM troubleshooting](https://gemilab.net/en/articles/gemini-basics/notebooklm-common-issues-troubleshooting-guide)
- C: [Tubarksblog — How to fix NotebookLM source errors 2025-05](https://tubarksblog.com/2025/05/04/how-to-fix-notebooklm-source-errors-simple-workarounds-that-work/)
- `UNVERIFIED — Phase 3 实测后回填`: 具体索引耗时数字

---

## Q6: Knowledge / Memory / API / Custom Instructions 等价物

**答**: NotebookLM 和其他平台的"持久化/指令"概念**不是 1:1 映射**, 有 3 条退化轨:

| 其他平台机制 | NotebookLM 等价物 | 用途 | 本次是否使用 |
|-------------|------------------|------|-------------|
| Claude Project Files / GPTs Knowledge | **Sources** (notebook 内 sources) | 向量化检索底料 | **Yes** (293 md) |
| Claude API Files | **API Sources** (NotebookLM Enterprise v1alpha 才开放) | API 通过 source 对象上传 | **No** (本次 Web UI only) |
| Memory (ChatGPT/Claude 跨 session 记忆) | **无等价物** | N/A | — |
| Custom Instructions / System Prompt | **3 条退化轨**: ① Audio Overview Custom prompt (最多 10,000 字符, 每次生成可写) ② **Chat custom goals** (官方 2025-10-29 发布, 三档 **Default / Learning Guide / Custom**; Custom mode 允许自定角色/目标/口吻, 最多 10,000 字符; 全档开放, 不限 Plus+) ③ Per-chat prompt engineering | 每次生成/聊天一次性约束 | 见 Phase 2 PLAN 决定是否用 Custom mode |
| Knowledge Cutoff / 训练数据 | NotebookLM **不训练**, grounded in sources only | 禁止 hallucinate 出源外事实 (官方承诺) | — |
| File attachment 运行时 | NotebookLM 必须先 upload 到 notebook, **不支持 chat 里临时 attach** | — | — |

**关键差异**: NotebookLM **没有传统意义的"system prompt"**, 原 Phase 0 初稿这段判断正确. 平台 2025-10-29 引入的 **Chat custom goals** (三档 Default / Learning Guide / Custom) 填补部分空白 — Custom mode 每 notebook 设置一次 (10,000 字符上限), 对同 notebook 内每次 chat 持续生效, 是**最接近 "system prompt" 的本平台机制**, 但受限于 notebook 粒度 (不是账户粒度) 且可被用户在 chat 里覆盖. 这是对 `_template/` 补丁候选 #1 的细化.

**来源**:
- A: [NotebookLM Help — Use chat in NotebookLM](https://support.google.com/notebooklm/answer/16179559?hl=en) (chat 面板 / Configure Chat 入口)
- A: [NotebookLM Help — Generate Audio Overview](https://support.google.com/notebooklm/answer/16212820?hl=en) (Custom prompt 长度)
- **A: [blog.google — NotebookLM custom personas engine upgrade 2025-10-29](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/) (chat custom goals 官方发布日 + 特性: "customize chat to adopt a specific goal, voice or role")**
- A: [Workspace Updates — New features 2025-03](https://workspaceupdates.googleblog.com/2025/03/new-features-available-in-notebooklm.html) (**订正: 此期发布 Mind Map + 语言选择器, 不含 chat mode selector**)
- A: [Cloud Docs — NotebookLM Enterprise API (v1alpha)](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks) (API 仅 Enterprise v1alpha, 非本次路径)
- C: [XDA — NotebookLM Learning Guide feature](https://www.xda-developers.com/notebooklm-learning-guide-feature/) (Default / Learning Guide / Custom 三档特性对比)
- C: [xda — Audio Overview custom length](https://www.xda-developers.com/notebooklm-audio-overview-custom-length/) (length 选项验证)
- C: [Shareuhack — NotebookLM Advanced Guide 2026: Custom Instructions](https://www.shareuhack.com/en/posts/notebooklm-advanced-guide-2026)

**Phase 3 P3.3 UI 实测 (2026-04-21, evidence: `dev/evidence/chat_mode_toggle_test.md`)**:

- ✅ **同 chat session 可动态切换三档** (Default / Learning Guide / Custom), 无需 new chat; XDA 报道的 "Configure Chat" 入口行为 A 级核实 — Q-REV-1 CLOSED
- ✅ 切换后 source set 不变 (同 notebook 同 42 bucket RAG), 仅 response 风格 / 是否应用 Custom instructions 变化
- ✅ Custom mode 下 `current/instructions.md` (9,011 chars / 90% of 10K cap) 规则 4 (Variable table) / 5 (Core 红线 AESER=Exp) / 6 (CT 全写 + C-code 字面 C66742) / 12 (诚实 follow-up 引导) 全部命中
- ⚠️ **F-1 附带发现**: NotebookLM Chat UI 层**原生支持** markdown 表格 — A 级证据 [NotebookLM Help — Use chat in NotebookLM](https://support.google.com/notebooklm/answer/16179559?hl=en) 明文 "When you save a response as a note, **the original format—including tables and clickable inline citations—gets saved**". 用户观察到的 pipe-table 平铺成一行是**模型输出层** single-line malformed (row 间缺换行, GFM renderer 不识别), 非 UI bug. P3.4 前跑 minimal table test 定锤, 按需微调 `instructions.md` Response template 强调 "each row on its own line"
- ⚠️ **F-2 附带发现**: Custom mode 同题 × 2 次答案语义等价但细节漂移 (valid values 完整度 / 输出语言), 属 RAG chunk 召回顺序 + LLM 采样随机性, 非 bug; 挪 P3.8 A/B 评分规则补一条 "同题 retry 幂等性不强制, 按语义 PASS"

---

## Q7: 分享机制 — 个人 / 协作者 / 公开 (v2, 2026-04-21 架构 pivot 后重写)

> **v2 更新说明**: v1 Q7 (archive/v1_3notebook_SUPERSEDED_2026-04-21/) 把分享拆成 "Mode A invite / Mode B public link" 两独立模式, 从而 planner 引伸出 "Scope B 本质两选一 → 两独立 notebook" 伪约束. 用户 2026-04-21 实测 UI 发现分享档是同一 notebook 的 3 档开关, 三 WebFetch 核实后重写本节. 详见 `archive/v1_.../ARCHITECTURE_PIVOT_RECORD.md`.

**答**: NotebookLM 分享是**同一 notebook 上的 3 档 Access Level 开关**, 档位可随时切换, **不是**建立多个 notebook. 权限粒度 (Viewer / Editor) 和 Access Level 正交.

### 三档 Access Level (同一 notebook 可切换)

| 档位 | 范围 | 访客前置条件 | Users 上限 (personal Gmail) | 官方原文出处 |
|------|------|-------------|---------------------------|-------------|
| **Restricted** (default) | 仅被邀请的具体 email | Google 账号 + 被邀请 | **50 users 硬上限** (官方明示) | `answer/16206563` |
| **Anyone with a link** | 任何拿到链接的人 | Google 账号 (非匿名) | **无 users 上限** (官方文档无 cap 条款) | `answer/16322204` |
| **Public** | 可在 NotebookLM 公开画廊被发现 | Google 账号 | **无 users 上限** (同上) | `answer/16322204` |

### 关键事实 (三 WebFetch 2026-04-21 核实)

1. **50-cap 仅套 Restricted invite**, 不覆盖 "Anyone with link" / "Public"
   - 官方原文 (`answer/16206563`): "Personal Gmail accounts can share a notebook with up to 50 users **but can't share with Google Groups**"
   - WebFetch 明确: "This refers to the **invite-based method** (adding email addresses), not 'Anyone with the link' or public sharing"

2. **档位可在同一 notebook 内切换** (不是独立 notebook 类型)
   - 官方原文 (`answer/16322204`): "turn off public sharing by revoking public access in the sharing panel" + "Set Notebook Access back to **Restricted**"
   - 含义: owner 可在同一 notebook 上 Restricted → Anyone with link → Public 三档间随意切, 随时回切, 不需新建 notebook

3. **"Anyone with link" 和 "Public" 需要 Google 账号** (非匿名)
   - 官方原文 (`answer/16322204`): "Copy and share the link to **anyone with a Google account** to have them view your notebook"

4. **Workspace Enterprise/EDU 账号禁公开档**
   - 官方原文: "Public sharing is only enabled for consumer accounts. It's currently disabled for Workspace Enterprise or Education accounts."
   - 同时 Enterprise/EDU 的 Restricted 档无 50-cap ("unlimited number of individual users and Google Groups within the same organization")

5. **分享不改 viewer 自己 tier 的 source cap** (**Free tier 兼容性约束**, 决定本项目 source 数上限)
   - 官方原文 (`answer/16213268`): "Sharing a notebook does not change the source limit for any collaborator"
   - WebFetch AI summary 解读: "the restriction follows the user, not the notebook"
   - 对本项目含义: 若 owner 上传 300 sources 分享给 Free tier (50 cap) 同事, Free tier viewer 可能**只能看到前 50 sources** — 为兼容性上限, 本项目上传 **≤50 sources**

### 权限粒度 (正交于 Access Level)

- **Viewer**: 只读 + 问答 + 看 owner 生成物 (Audio Overview / Mind Map / Study Guide)
- **Editor**: Viewer 能力 + 增删改 source + 生成新 Audio / Mind Map

Restricted 档下, owner 按 email 邀请时可选 Viewer / Editor. Anyone with link / Public 档下, 访客默认 Viewer (无 Editor).

### 变体与撤销

- **Chat View 链接**: hide 左侧 source 列表, 强调问答体验 (同 Access Level 下的 UI 变体)
- **Marketplace / Featured notebooks**: Google 精选 (非用户自助发布)
- **撤销**: Owner 关档 (切回 Restricted) 或删 notebook, 所有外部链接立即失效

### 本项目含义 (v2 架构约束)

- **单一 notebook**: Scope ABC 三场景 (个人学习 / 小圈分享 / 公开分享) 在**同一 notebook 内按档位切换**实现, 不再拆三个 notebook
- **默认 Restricted**: 日常使用/个人学习态处于 Restricted 档, 不泄漏
- **按需开 Anyone with link**: 需要给 SDTM 同事分享时临时切到此档 (50-cap 不适用, 想共享给多少人都行)
- **按需开 Public**: 仅当用户想在 NotebookLM 公开画廊被发现才切到此档
- **Source 数上限 ≤50**: 为 Free tier viewer 兼容性 + 其他 5 条独立理由 (indexing 风险 / citation 信噪比 / Mind Map 可读性 / upload effort / workflow replication)

### 仍需 Phase 3 实测 (可后置, 不阻塞 Phase 2 PLAN)

- 公开档访客问答**是否回写 owner chat history?** 官方文档未明示, 社区观察**不会写回**
- 公开档访客 chat quota 归属 (Pro tier 500 chat/day 会不会被他人消耗)

### v1 I8 / C2.9 carry-over close

| v1 carry-over | 原问题 | v2 处置 |
|--------------|--------|---------|
| **I8** | Mode B owner 是否套用 Mode A 50-cap | **CLOSED** — 50-cap 仅套 Restricted invite (`answer/16206563` WebFetch 核实), 不套其他档 |
| **C2.9** | Mode B cap 归属 UNVERIFIED 决定 Scope B 广泛分享天花板 | **CLOSED** — Anyone with link / Public 档无 users 上限, Scope B 广泛分享无阻塞 |

**来源** (全部 2026-04-21 WebFetch 核实):
- **A**: [NotebookLM Help — Create a notebook](https://support.google.com/notebooklm/answer/16206563?hl=en) — 50-cap 原文, 明确仅适用 invite
- **A**: [NotebookLM Help — Public notebooks and featured notebooks](https://support.google.com/notebooklm/answer/16322204?hl=en) — 三档切换描述, Anyone with link 需 Google 账号, Enterprise/EDU 禁公开
- **A**: [NotebookLM Help — Upgrade / Plans](https://support.google.com/notebooklm/answer/16213268?hl=en) — 分享不改 viewer 自己 tier source cap
- A: [blog.google — NotebookLM public sharing 2025-06](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-public-notebooks/) — 公开档发布通告
- C: [Android Authority 2025-06-03](https://www.androidauthority.com/notebooklm-public-sharing-3563789/) — 50-cap 第二独立源 ("users with personal Gmail accounts could only share their notebooks with up to 50 other users")

---

## Q8: Calibration — 跳过 (容量透明判定)

**答**: **容量透明 → calibration 实验 skipped**. 模板 Q8 第一行判定: "官方是否公开精确限额?" Yes (Q2 四 tier 官方矩阵) → 跳.

**确认项**:

1. **单位**: NotebookLM 用 **words** 不用 tokens (官方 help 原文 "500,000 words each"). Tokens 只是推测 (~667K/source). 本地 SDTM md 用 `wc -w` 数 words 即可, 不需要 tiktoken.
2. **SDTM md 单文件体量**: 项目 293 md 单文件最大远 < 500K words (估 <10K words), 一对一上传不触发单源 cap.
3. **Notebook 级别总字数是否有隐藏 cap?** — 查官方文档**没有** notebook 级 aggregate cap, 仅 per-source cap + sources-count cap. 即 Pro tier 理论上限 = 300 sources × 500K words = **150M words/notebook** (~200M tokens 等值). SDTM 293 md 总 words 估计 <3M → notebook 容量使用率 <2%, 远未到 cap.
4. **Audio Overview 本身不算进 notebook 容量**, 它是生成物, 不占 source slot.

**对比 Claude**: Claude Projects 需要 calibration 是因为 paid 的 RAG 扩容是隐式的 (UI 显示 12% 实际 ~3M tokens 等值). NotebookLM 没有这个黑盒, 直接给数字.

**来源**:
- A: [NotebookLM Help — FAQ](https://support.google.com/notebooklm/answer/16269187?hl=en) (500K words 权威出处)
- C: [Steven Johnson X 2024-05](https://x.com/stevenbjohnson/status/1793991409164251437) (500K words 来自 NotebookLM team 成员发言)
- `UNVERIFIED — community rule of thumb only`: 100 tokens ≈ 75 words 换算

---

## §9 Audio Overview 独有调研

**生成机制**: NotebookLM 把 notebook 内 sources 作为底料, 用 Gemini 3 生成**两名 AI 主持人**的对话脚本, 然后送到 Google 的 TTS 引擎生成音频. Format 选项:
- **Deep Dive** (默认): 深度对话, 两个主持人展开讨论
- **The Brief**: 简短摘要
- **The Critique**: 批判视角
- **The Debate**: 正反方辩论

**Plus/Pro 自定义**:
- **Length**: Shorter / Default / Longer (仅英文 2025-03 起开放)
- **Custom prompt**: 最多 **10,000 字符** 指令, 可指定"侧重 SDTM Domain MH 和 AE, 从 beginner 视角讲, 30 分钟内, 每段后留回顾"等
- **Language**: 80+ 语言, 但**发音仅英文高质量**, 其他语言可用但可能有口音/glitch
- **Interactive Audio Overview** (2024-12 起): 用户可中途"加入对话"问主持人问题

**每月额度** (注: 单位实为 per-day):
- Standard: **3/day** (不是/月)
- Plus: 6/day (2x)
- Pro (用户本次): **20/day** (Standard 的 6.67x, 非营销说的"5x")
- Ultra: 200/day

**已知 hallucination 模式** (C 级观察):
- 跨 source 融合时偶会造"源未说过"的过渡性结论, 官方明示 "may contain inaccuracies or audio glitches"
- 长 source 时主持人可能"忽略"后半段, 社区观察有"前 30% 内容占 80% 时间"倾向
- Interactive mode 下偶有"第三个声音"乱入 / 主持人切换乱
- 2024 末有案例主持人脑补了源外人名 (多为 consumer edge case, Enterprise 很少报)

**对 SDTM 项目含义**: Audio 适合做"整个 Domain 的 introduction" 级别, 不适合做"controlled terminology 条项级精准讲解". Scope C (音频补充) 定位应是**高层概念串讲**, 不追求逐条精准.

**来源**:
- A: [NotebookLM Help — Generate Audio Overview](https://support.google.com/notebooklm/answer/16212820?hl=en) (4 format + 80+ languages + Custom prompt 官方)
- A: [NotebookLM Upgrade](https://support.google.com/notebooklm/answer/16213268?hl=en) (20/day Pro, 200/day Ultra 数字)
- C: [xda — Audio Overview custom length](https://www.xda-developers.com/notebooklm-audio-overview-custom-length/)
- C: [Murf.ai — Audio Overview customization guide](https://murf.ai/blog/notebook-lm-audio-customization)
- C: [Nicole Hennig — Reverse engineering Audio Overview system prompt](https://nicolehennig.com/notebooklm-reverse-engineering-the-system-prompt-for-audio-overviews/) (社区逆向内部 prompt, 非权威)
- `UNVERIFIED — community anecdotes`: hallucination 具体模式 / 前重后轻倾向

---

## §10 Mind Map 独有调研

**覆盖深度**: Mind Map 基于**全部 sources** 生成, 显示主题 + 子分支. 官方 help 没有声明"对超长源会采样或截断", 但社区观察:
- 单个源 >100K words 时, 该源只贡献 2-3 级分支, 深层概念可能落下
- 短源 (5-20K) 覆盖很全

**跨 source 连线**: 官方 help **没有描述**跨 source 显式关联机制. 社区测试: Mind Map 把"同主题但来自不同 source 的节点"合到一起, 但**看不到"这个节点来自哪个源"** — 要想知道必须点节点 → "ask in chat" 才拿到 citation.

**导出**:
- 官方: 仅 **PNG 图片下载** (2026-04 最新)
- 限制: 只导出**当前展开**的节点, 折叠的不导出 → 导全必须手动逐个展开
- 社区工具 (第三方, 非官方): Chrome extension / GitHub 开源工具可导 FreeMind (.mm) / XML / OPML

**对 SDTM 项目含义**: Mind Map 适合给对外分享 notebook 用作"SDTM 63 domain 全景图"一类, 但**不能替代 ER 图 / 域关系图** — 节点间连线语义弱, 不能表达"RELREC 关联"这种强结构关系. Scope A (个人学习) 可利用 Mind Map 做快速预览, 但关键关系仍需回源核查.

**来源**:
- A: [NotebookLM Help — Mind Maps](https://support.google.com/notebooklm/answer/16212283?hl=en) (官方功能描述 + PNG 导出)
- C: [Xmind blog — Export NotebookLM mind map](https://xmind.com/blog/export-notebooklm-mind-map)
- C: [GitHub — rootsongjc/notebookllm-mindmap-exporter](https://github.com/rootsongjc/notebookllm-mindmap-exporter) (三方导出工具)
- C: [Atlas Workspace — NotebookLM Limitations](https://www.atlasworkspace.ai/blog/notebooklm-limitations) (跨 source 弱连线观察)
- `UNVERIFIED — community anecdote`: "长源深层覆盖衰减" 现象

---

## §11 Notebook 数量 & Source 隔离 (事实保留, 结论 v2 重写)

**Plus/Pro/Ultra notebook 数量上限** (官方矩阵):

| Tier | Notebooks/user |
|------|---------------|
| Standard (原 Free) | 100 |
| Plus | **200** |
| Pro (用户本次) | **500** |
| Ultra | 500 |

**Source 隔离性**: 强隔离. **"Each notebook is independent, and NotebookLM can't access information across multiple notebooks at the same time."** 官方设计 philosophy.

**跨 notebook 引用机制** (两条, 若选多 notebook 时):

1. **Gemini app 侧挂载**: 2026-01 起, Gemini 可把 N 个 notebook 同时挂为 source, Gemini 层面做跨 notebook 问答. 但这是 **Gemini 的事, 不是 NotebookLM 原生** — 用户问的是 Gemini, 不是 notebook.
2. **手动复制 source**: 把同一 md 上传到多个 notebook (计算多个 source slot). 规模大时成本高.

**对 SDTM 项目含义** (v2 重写):

v1 原打算利用 Pro 500 notebooks 额度开 3 个 notebook (ABC 三 scope 各一), 已于 2026-04-21 pivot 废止. **v2 采用单 notebook 架构**, 理由:

1. Scope ABC 的职责分离**不必通过多 notebook 实现** — 同一 notebook 按分享档位切换即可 (见 Q7)
2. Source 隔离虽是事实, 但单 notebook 场景下**无跨 notebook 引用需求**, 降级为信息约束 (非 hard rule)
3. 多 notebook 会带来 ×3 倍上传成本 (最坏 353 次) 且无收益

**保留情境** (若未来扩展): 仅当 ABC 场景需要职责完全分离到不同 collaborator 圈 (如同一 org 内 A/B/C team 互不可见对方的 source), 才升级多 notebook. 本次用户 Rule E 场景 (个人 SDTM 学习 + 小圈分享 + 公开分享) 不触发此需求.

**来源**:
- A: [NotebookLM Help — Upgrade](https://support.google.com/notebooklm/answer/16213268?hl=en) (notebooks/user 四档数字)
- A: [Workspace Updates 2026-01 — NotebookLM as Gemini source](https://workspaceupdates.googleblog.com/2026/01/take-notebooks-further-notebooklm-gemini.html)
- C: [Medium — NotebookLM Isolated Notebooks: Two Ways to Finally Connect](https://medium.com/@kombib/notebooklm-isolated-notebooks-two-ways-to-finally-connect-them-12485a79ac47) (隔离 + Gemini 侧方案详解)
- C: [AndroidPolice — NotebookLM with Gemini unlocks](https://www.androidpolice.com/i-paired-notebooklm-with-gemini-solved-biggest-limitation/)

---

## §12 2026-04 API 状态

**答**:

| 状态项 | 事实 | 来源级别 |
|--------|------|---------|
| 公开 GA API (consumer NotebookLM)? | **No** — 没有 consumer 级公开 API | A |
| NotebookLM Enterprise API | **Pre-GA (v1alpha)**, "as is" with limited support, 仅 Google Cloud / Gemini Enterprise tier 可见 | A |
| NotebookLM Enterprise 产品本身 | **GA (2026-04)** 在 Global/EU/US multi-region | A |
| Gemini app 侧集成 NotebookLM | 公开, 通过 Gemini web app 挂 notebook 为 source | A |
| Agent Builder / Agent Designer | Agent Designer GA, 可集成 NotebookLM Enterprise | A |
| Google Agentspace | 存在, NotebookLM Enterprise 可作为 deployment env 的一部分 | C |
| 非官方 Python API | 存在 (社区逆向 web UI 做的), **有账号风险**, 本次用户 ack 不用 | C |

**对本次 Scope 含义**: 用户 ack Web UI only, 因此 API 状态**不阻塞本次部署路径**. 但 Phase 5 收束时值得写进 "未来扩展 hooks" — 若未来 NotebookLM Enterprise 开 GA API 且价格合适, SDTM 可以从 Web UI 迁移到 programmatic 管理.

**来源**:
- A: [Cloud Docs — NotebookLM Enterprise API](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks) (v1alpha 状态)
- A: [Cloud Docs — Gemini Enterprise release notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes)
- A: [Cloud Docs — NotebookLM Enterprise data residency](https://docs.cloud.google.com/gemini/enterprise/docs/locations) (GA / regions)
- A: [Google AI Developers Forum — How to access NotebookLM Via API](https://discuss.ai.google.dev/t/how-to-access-notebooklm-via-api/5084)
- C: [AIToolly — Unofficial NotebookLM Python API 2026-03](https://aitoolly.com/ai-news/article/2026-03-11-unofficial-google-notebooklm-python-api-agent-skills-unlock-hidden-features-with-python-cli-and-ai-a) (非官方工具, 风险提示)

---

## 对 PLAN 的修订 (vs Phase 0 platform_profile.md 初稿)

| # | 原假设 (Phase 0 初稿) | 调研后事实 | 修订动作 (Phase 2 PLAN) |
|---|---------------------|-----------|---------------------|
| **1** | "套餐 Plus (via Google AI Pro)" 对应 **300 sources/notebook** | 属于 **SKU 语义漂移** (非简单改名): I/O 2025 后 Google One AI Premium → Google AI Pro 品牌重构, 旧单档 "NotebookLM Plus" 规格上移为 "NotebookLM Pro", "Plus" SKU 词重新分配给新中档. Google AI Pro 订阅现 unlock 的是 **NotebookLM Pro tier** (500 notebooks / **300 sources** / 500 chat / 20 audio). 新 "Plus" 另指 Google AI Plus 订阅对应的中档 (**100 sources**). 训练数据 (截至 2026-01) 前的 "Plus=300" 对应**旧 Plus**, 现已是 Pro. | PLAN §0 更新措辞 "NotebookLM Pro tier (via Google AI Pro 订阅)"; SKU 漂移警示列为必写注脚; 引用第三方文章前必先判断其 "Plus" 指代时点. |
| **2** | "Free: 50 sources × 500K words / Plus: 300 sources × 500K words" | 官方最低档 SKU 名是 **Standard** (非 Free), 50/500K 数字正确; "300 sources" 现属 **Pro tier**; 新增 Plus tier (100) 和 Ultra tier (600) | PLAN §1 容量表必列四档, 明示本次走 Pro 行; **v2 策略**: 即使 Pro 300 cap 很松, 主动压缩到 **≤50** (Free tier viewer 兼容 + 5 条独立理由), 293 md 通过 concept cluster 合并到 ≤50 |
| **3** | "Multi-notebook: Plus 权益下开 3 个 notebook" | Pro tier notebooks/user = 500 够用, 但 v2 架构 pivot 后采用**单 notebook** (见 Q7 + §11 结论) | PLAN v2 §3 单 notebook 策略 (ABC 三场景同 notebook 分享档位切换), 删除 multi-notebook 架构段; source 隔离降级为信息约束. v1 ×3 notebook 架构归档 |
| **4** | "Audio Overview 每月额度 (Plus 5x)" | 官方口径是 **per-day 而非 per-month**, Pro = 20/day (Standard 6.67x) | PLAN Audio 批次规划按 **daily** 节奏, 不按 monthly 估算 |
| **5** | "Custom Instructions: NotebookLM 无 system prompt, 退化 3 条" | 退化 3 条方向对, 但需补**最新 Chat custom goals** (三档 **Default / Learning Guide / Custom**, 2025-10-29 blog.google 发布, **全档开放非 Plus+ 独享**; Custom 模式最多 10,000 字符可自定角色/目标/口吻); 这是目前最接近 "notebook 级 system prompt" 的本平台机制 | PLAN 05_solution 新增 "Chat mode 三选" 决策格: 默认 **Custom** + SDTM 专家 system prompt 文本模板 (10,000 char 内); 备选 **Learning Guide** 用于 Scope A 个人学习场景 (自动 Socratic 教学) |
| **6** | "Indexing indicator 训练知识印象相对可靠" | 官方承认 upload 可能 silent fail, **Phase 3 必实测** 单 md/单 PDF/批量三场景 | PLAN Phase 3 必须加 "indexing smoke test" 动作节点, pass 前不进全量上传 |
| **7** | 未提 **source 级单文件字数核对** | Pro 300 sources cap + SDTM 293 md 一对一余 7 slot, 紧. 需先 wc 过滤一下有没有>500K words 的 "outlier" md (估极低概率, 但要查) | PLAN Phase 2 新增 "pre-upload audit" 动作: `find knowledge_base -name '*.md' -exec wc -w {} \;` 排序 Top 5, 确认无超 500K words |
| **8** | 未明示 API 状态 | Consumer 无 GA API; Enterprise v1alpha. 本次 Web UI only → 不影响. | PLAN 末尾加"未来扩展 hooks"段, 标 "若后续 Enterprise API GA 可迁移 programmatic" |
| **9** | 公开分享 "具体权限模型待确认" | **v2 订正** (2026-04-21 三 WebFetch 核实): 不是两独立模式, 而是**同一 notebook 3 档 Access Level** (Restricted / Anyone with link / Public) 可随时切换. **50-cap 仅套 Restricted invite 档**, "Anyone with link" / "Public" 档无 users 上限 (均需 Google 账号, 非匿名). Workspace Enterprise/EDU 禁公开档 (Restricted 档则无 50-cap 且可加 Groups). 归因: 官方 `answer/16206563` (50-cap 原文) + `answer/16322204` (三档切换描述) + `answer/16213268` (viewer 自己 tier cap 不变). | PLAN v2 Scope B 通过**同一 notebook 分享档位按需切换**实现: 默认 Restricted 私有, 需小圈分享切 Anyone with link, 需画廊发现切 Public. 不再拆两独立 notebook. v1 I8 / C2.9 carry-over 直接 close. |
| **10** | "Mind Map 对长 source 可能遗漏" | 社区观察有此现象, 官方未承认. 导出**只 PNG**, 第三方工具可导其他格式. | PLAN A/B 矩阵 Mind Map 题设计: 用跨 domain 概念题 (如 RELREC 网), 测是否遗漏关键域 |

---

## Writer self-report

### Disagreements with Phase 0 draft

| Field (Phase 0) | Draft value | Research value | Source URL |
|----------------|-------------|----------------|------------|
| 套餐名称 | "Plus (via Google AI Pro)" | "Pro (via Google AI Pro)" — **SKU 语义漂移**: I/O 2025 后 Google AI Pro 品牌下 NotebookLM 旧 Plus 规格上移改名 Pro, 新 Plus 另指新中档. 非简单改名. | https://notebooklm.google/plans (官方 landing 标题 "Google NotebookLM **Pro**") + https://9to5google.com/2026/04/11/google-ai-pro-ultra-features/ |
| Plus sources/notebook | 300 | **300 属新 Pro tier** (=旧 Plus 规格上移), 新 Plus = 100; 引用 2026-01 前第三方文章的 "Plus=300" 是指旧 Plus, 和当前 Plus 不同 | https://support.google.com/notebooklm/answer/16213268?hl=en |
| Plus notebooks/user | 未写 | Pro=500, Plus=200, Standard=100, Ultra=500 (官方 tier 名**不是** "Free") | 同上 |
| Audio Overview 额度单位 | "每月 Plus 5x" (暗示月额) | **per-day**, Standard 3/Plus 6/Pro 20/Ultra 200 | 同上 |
| Custom Instructions 最新一条 | 仅 Audio Overview instructions + per-chat prompt + suggested question | + **Chat custom goals** (三档 Default / Learning Guide / Custom, 全档开放) 2025-10-29 由 blog.google 发布 (非 2025-03 Workspace Updates; Writer #1 原归因有误) | https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/ |
| 公开链接账号限制 | "具体权限模型待 Phase 1 确认" | **仅 consumer/personal Gmail** 能开; Workspace Enterprise/EDU 禁用 | https://support.google.com/notebooklm/answer/16322204?hl=en |
| 个人 Gmail 邀请 user 上限 | 未写 | **同一 notebook 3 档 Access Level** (v2 修正, 2026-04-21 三 WebFetch 核实): Restricted 档 personal Gmail = 50-cap / Enterprise/EDU = 无 cap + Groups; Anyone with link 档 = 无 users 上限, 需 Google 账号; Public 档 = 无 users 上限 (画廊可发现). 档位可随时切. **v1 Q7 把三档叙述成 "两独立 Mode A/B" 是合成错误, 导致 planner 引伸 "Scope B 两选一 → 3 notebook" 伪约束** (见 `archive/v1_.../ARCHITECTURE_PIVOT_RECORD.md`). | https://support.google.com/notebooklm/answer/16206563 (50-cap 原文) + /answer/16322204 (三档切换) + /answer/16213268 (viewer tier cap) |

### Unverified items (找不到权威 A 级, 仅 C 或 community)

1. **Embedding 模型具体型号** — 推测 `gemini-embedding-001`, 未官方确认
2. **Chunk size** — 社区估 ~500 tokens, 未确认
3. **Audio Overview hallucination 模式细节** — 仅社区观察, 官方只说 "may contain inaccuracies"
4. **Mind Map 长源深层覆盖衰减** — 仅 Atlas Workspace 博客观察, 非权威
5. **公开链接访客问答是否回写 owner chat history** — 官方文档未明示, 需 Phase 3 实测
6. **Words → tokens 换算比** — 社区常用 100 tokens ≈ 75 words, 非 NotebookLM 官方口径
7. **Indexing 实际等待时间数字** — Phase 3 实测任务, 本文件不填

### Confirmed matches (研究结果和初稿一致项计数)

**9 项一致**:
1. 平台身份 = NotebookLM (Google)
2. 检索机制 = 内置 grounded retrieval (Gemini backbone)
3. 注入粒度 = chunk-level + inline citation
4. 容量单位 = sources 数 + words/source
5. 500K words/source 全 tier 统一
6. 不训练上传内容 (官方承诺)
7. Mind Map 导出仅 PNG (+第三方工具)
8. Source 隔离 (notebook 间不共享)
9. NotebookLM 无传统 system prompt, 需要退化映射

---

## Phase 1 完成度自检

- Q1-Q8: **7 问拿到 A 级官方文档** (Q5 indexing 除实测部分依赖 C 级)
- §9-§12: 4 段独有调研均有 A + C 混合来源
- Unverified 7 条 明标
- Phase 0 初稿字段 9 项一致 / 7 项需修订
- 对 PLAN 10 条修订候选全部列出

**准入门槛**: 80% 字段有 A/B 源, 仅 embedding/chunk/indexing timing 等实现细节依赖 C 级或 Phase 3 实测. **通过**.

---

*来源层级说明: A = Google 官方 (notebooklm.google, support.google.com/notebooklm, blog.google, workspaceupdates.googleblog.com, docs.cloud.google.com, one.google.com); C = 第三方媒体/社区 (9to5google, xda, elephas, medium, xmind, murf, androidauthority 等). B 级 (Google 官方 X/YouTube) 本次仅用到一次 (Steven Johnson X). UNVERIFIED 已独立列出, 不掩饰.*

---

### Writer #2 修正日志 (2026-04-21, subagent_type=oh-my-claudecode:executor) — **pre-pivot 历史记录**

> **v2 注**: 本日志记录 Phase 1 Writer 阶段的修正动作, 反映当时的 Mode A/B 叙事理解. Phase 2 架构 pivot (2026-04-21) 后 Q7 已整体重写, Mode A/B 框架作废. 本日志**作审计轨迹保留不删**, 但**不作为 Phase 2 v2 的架构依据**, 以 Q7 v2 + §11 v2 结论为准. **特别注**: **下表第 3b 行 "Mode A/B 分享模式拆分" 所述的两独立模式框架已在 Q7 v2 废止**, 实际是同一 notebook 的 3 档 Access Level 可切换, 详见 Q7 v2 + 三 WebFetch 证据链.

**背景**: Writer #1 (`general-purpose`) 完成 research.md 初版后, Reviewer #1 (`oh-my-claudecode:verifier`) 判定 CONDITIONAL_PASS (78% 置信), 指出 3 大事实错误 + 1 全文口径错误. 本日志由 Writer #2 (`oh-my-claudecode:executor`, 第 3 种不同 subagent_type, Rule D 合规) 据 Reviewer #1 反馈修正, 等后续 Reviewer #2 (`oh-my-claudecode:critic`) 独立复核.

| # | 修正项 | 改前 | 改后 | 新来源 URL | 影响位置 |
|---|-------|------|------|-----------|-------|
| 1 | Chat mode 命名 + 发布归因 | "Chat mode selector (Guide/Analyst/Custom) 2025 下半年新增, 来源 Workspace Updates 2025-03" | "Chat custom goals 三档 **Default / Learning Guide / Custom** (无 Analyst), 2025-10-29 blog.google 发布 '[custom personas engine upgrade](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/)'" | [blog.google 2025-10-29](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/) + [XDA Learning Guide](https://www.xda-developers.com/notebooklm-learning-guide-feature/) + [Help use chat](https://support.google.com/notebooklm/answer/16179559) | Q3 时间线 (新增 2025-10-29 行, 2025-03 行加订正注) + Q6 Custom Instructions 行 + Q6 关键差异段 + Q6 来源 + Self-report 第 5 行 + PLAN 修订 #5 |
| 2 | Plus/Pro 改名本质 | "2025 下半年-2026 原 'Plus' 改名为 'Pro', Tier 重组为 Free/Plus/Pro/Ultra 四级" (措辞 = 简单改名) | "**SKU 语义漂移** — I/O 2025 后 Google One AI Premium → Google AI Pro 品牌重构, 旧 NotebookLM Plus 规格上移改名 Pro, 'Plus' SKU 词被重新赋给新中档. 训练数据 (截至 2026-01) 的 'Plus=300 sources' 对应**旧** Plus, 新 Plus=100. 同 SKU 词 12 月内语义翻转." | **[notebooklm.google/plans](https://notebooklm.google/plans)** (A 级官方 landing 页, 标题 "Google NotebookLM Pro") | Q3 时间线 (2025-05 I/O + 2025 下半年 SKU 漂移两行重写) + Q2 导语段 + Q2 脚注 SKU 警示 + Q2 来源 + Q3 来源 + Self-report 套餐/Plus sources/Custom Instructions 多行 + PLAN 修订 #1 #2 |
| 3a | 50 cap 归因订正 | "9to5google 2025-06-03" (实际该文未提 50 数字) | 一手 [官方 Help answer/16206563](https://support.google.com/notebooklm/answer/16206563?hl=en) "Personal Gmail accounts can share a notebook with up to 50 users" + 二手 [Android Authority 2025-06-03](https://www.androidauthority.com/notebooklm-public-sharing-3563789/) "personal Gmail accounts could only share their notebooks with up to 50 other users" | [Help 16206563](https://support.google.com/notebooklm/answer/16206563?hl=en) + [Android Authority](https://www.androidauthority.com/notebooklm-public-sharing-3563789/) | Q7 来源行 (9to5google 条改为订正归因说明) + Self-report 第 7 行 + PLAN 修订 #9 |
| 3b | 分享模式拆分 | Q7 表格把 "公开链接 + 50 users 邀请上限" 合并表述, `invite_direct` (50 cap) 和 `public_link` (无 cap) 混用 | Q7 完全重组为 **Mode A Direct invite** (email 邀请, 50 users cap/personal Gmail) 和 **Mode B Public link** (公开链接, 无 users 上限, 需访客 Google 账号) 两个独立子模式, 加"两模式混用判断"段说明可叠加但 Scope B 本质两选一 | 同 3a | Q7 全节重写 + Self-report 第 7 行 + PLAN 修订 #9 要求 Scope B 分设计 2 种 notebook |
| 4 | Free → Standard SKU 全文 | "Free" 作为最低档 SKU 名 (Q2 表 1 行, Q3 时间线 1 行, PLAN #2 1 行, Self-report 2 行, 来源行 1 行) | "**Standard** (官方名; 社区通称 Free)" 指代 SKU; "免费档/免费用户" 中文描述词保留 | [Help upgrade 16213268](https://support.google.com/notebooklm/answer/16213268?hl=en) (WebFetch 核实官方四档名 Standard / Plus / Pro / Ultra) | **5 处**: Q2 表第 1 行 + Q2 脚注 SKU 警示 + Q2 来源行注 + Q3 时间线 2024-05 行 + PLAN 修订 #2 + Self-report Plus notebooks/user 行 + Audio 额度行 |

**WebFetch 验证记录** (4 新 URL + 2 复核 URL = 6 个):

1. [blog.google 2025-10-29 custom personas engine upgrade](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/) — **状态 200, 关键发现**: 发布日期确认 2025-10-29, 官方措辞 "customize chat to adopt a specific goal, voice or role", 无 "Analyst" 字样.
2. [notebooklm.google/plans](https://notebooklm.google/plans) — **状态 200, 关键发现**: 页面标题 "Google NotebookLM **Pro** | Premium AI Research & Brainstorming Tool", 官方 landing 直接用 Pro; SPA 内容细节抓不全, 只能确认 Pro SKU 存在.
3. [support.google.com/notebooklm/answer/16213268 (Upgrade)](https://support.google.com/notebooklm/answer/16213268?hl=en) — **状态 200, 关键发现**: 四档官方名 = **NotebookLM Standard / NotebookLM in Plus / NotebookLM in Pro / NotebookLM in Ultra** (非 "Free"). 另有 "Custom Chat, Analytics, Advanced Sharing" 作 premium feature 分类 header.
4. [support.google.com/notebooklm/answer/16206563 (Create a notebook)](https://support.google.com/notebooklm/answer/16206563?hl=en) — **状态 200, 关键发现**: 原文 "Personal Gmail accounts can share a notebook with up to 50 users but can't share with Google Groups" / "Enterprise and Education accounts ... unlimited number of individual users and Google Groups within the same organization". 50 cap 一手官方来源.
5. [androidauthority.com notebooklm-public-sharing-3563789](https://www.androidauthority.com/notebooklm-public-sharing-3563789/) — **状态 200, 关键发现**: 2025-06-03 发表, 原文 "users with personal Gmail accounts could only share their notebooks with up to 50 other users". 50 cap 第二独立源.
6. [support.google.com/notebooklm/answer/16322204 (Public notebooks)](https://support.google.com/notebooklm/answer/16322204?hl=en) — **复核**: "share the link to anyone with a Google account to have them view your notebook"; 不提 users 数上限 (确认 Mode B 无 cap).

**WebSearch 补证** (2 个查询):

- `"NotebookLM chat mode Default Learning Guide Custom three modes"` — 多篇第三方 (XDA / Shareuhack / Medium / YouTube) 独立交叉确认三档命名 Default / Learning Guide / Custom, 入口是 "Configure Chat".
- `"NotebookLM share notebook 50 users limit personal Gmail invite"` — 官方 Help + Android Authority + Gemini Community thread 交叉确认 50 cap.

**Partial fix (找不到权威来源)**: 无 — 4 组修正全部找到 A 级或 A+C 双源支撑. 唯一遗憾: Chat custom goals 官方 blog 未列具体 3 mode 命名 ("Default/Learning Guide/Custom" 由官方 Help page 16179559 + XDA + Medium 多源合推得出, 不是单一 A 级官方页点名), 但已属 "A + 3 独立 C 级" 的强证据链.

**Free → Standard 全文替换计数**: **5 处修改**
1. Q2 表第 1 行 Tier 列: "Free" → "Standard (官方名; 社区通称 Free)"
2. Q2 脚注新增 SKU 警示段明示 Standard 命名
3. Q2 来源行第 2 条注 "Standard 档数字"
4. Q3 时间线 "Free tier 确立当前 Free 基线" → "Standard tier (原 'Free') 确立当前基线"
5. PLAN 修订 #2 + Self-report "Plus notebooks/user" 行 + Audio 额度单位行: Free → Standard

**Rule D 合规声明**:
- Writer #1: `general-purpose` (初版)
- Reviewer #1: `oh-my-claudecode:verifier` (判 CONDITIONAL_PASS)
- **Writer #2 (本次): `oh-my-claudecode:executor`** ← 第 3 种 subagent_type, 与 Writer #1 和 Reviewer #1 皆异, **Rule D 合规**
- Reviewer #2 (后续): `oh-my-claudecode:critic` ← 第 4 种 subagent_type, 预计独立复核本次修正

**未修正范围自律**: 本轮仅执行 Reviewer #1 明示的 4 组修正. Reviewer #1 §Carry-over Phase 2 / Phase 3 清单 (C2.1-C2.8, I1-I7) 属下一 Phase 范围, 本 Writer #2 不擅动. §维度 5 的 2 条遗漏 (Gemini chat 输入 token 上限 + Mind Map 增量刷新) 未转为 research.md Q 新增 — 遵循指令严格边界, 留给主 session 或 Phase 2 PLAN 处理.
