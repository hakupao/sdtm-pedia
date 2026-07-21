# ChatGPT GPTs — Phase 1 前置调研 (Research)

> Phase: 1 (调研) · Tier 2
> Writer: oh-my-claudecode:executor subagent
> 最后更新: 2026-04-20
> 承接: Phase 0 profile 97% + reviewer 3 LOW carry-over + Rule E ack

---

## 八问八答 (10 条, 含 Phase 0 carry-over)

### Q1. Assistants API 与 GPT Builder Knowledge 是否同一套?

**答**: **不完全相同, 但底层技术同源**. GPT Builder 的 Knowledge 是封装好的"无代码"File Search (内置 vector store), 用户通过 Web UI 上传文件即可使用. Assistants API v2 的 File Search 则需要开发者手动创建 vector store、上传文件、关联 assistant, 提供更细粒度的控制. 两者使用相同的 vector store 技术基础 (embedding + keyword 混合检索), 但**存储不共享** — GPT Builder 的文件存在 ChatGPT 产品侧, Assistants API 的 vector store 存在 platform.openai.com API 侧, 两者相互独立, 不互通.

重要背景: OpenAI 已宣布 Assistants API 将在 2026 年上半年某时间点 sunset, 新版统一使用 Responses API + file_search 工具.

**来源**:
- [OpenAI community: Feature Request - Custom GPT Parity (vector store 差异讨论)](https://community.openai.com/t/feature-request-support-multiple-vector-stores-per-run-in-assistants-api-custom-gpt-parity/1265310)
- [OpenAI Assistants Vector Stores and File Storage explainer](https://www.likeminds.community/blog/openai-assistants-vector-stores-and-file-storage-tool)
- [OpenAI for Developers 2025 (Assistants API sunset 声明)](https://developers.openai.com/blog/openai-for-developers-2025)

**对 PLAN 的影响**: SDTM 项目使用 GPT Builder (ChatGPT Plus), 不使用 Assistants API. 两者存储独立, 无法"借用" API 侧存储来突破 GPT Builder 的 20 文件上限. Profile F3 失败模式的"预留 spare"策略保持有效.

---

### Q2. File Search chunk 策略?

**答**: **chunk 大小 800 tokens, overlap 400 tokens (默认)**. 这两个参数在 Assistants API/Responses API 侧可通过 `chunking_strategy: {type: "static", max_chunk_size_tokens: N, chunk_overlap_tokens: M}` 调整; `chunk_overlap_tokens` 不得超过 `max_chunk_size_tokens / 2`. **GPT Builder 侧用户无法配置 chunk 参数**, 使用平台默认值.

单文件超过 chunk 大小时按 800/400 分片; 若文件内容总量小于一个 chunk, 则整个文件为一个 chunk (不强制分片).

**来源**:
- [OpenAI community: Customizing chunk size for file_search tool (含默认值确认)](https://community.openai.com/t/customizing-chunk-size-for-file-search-tool/1148708)
- [OpenAI community: chunk size and chunk overlap Q&A](https://community.openai.com/t/dear-all-i-have-the-questions-about-the-openai-assistant-chunk-size-and-chunk-overlap-of-file-search-tool/831342)

**对 PLAN 的影响**: 800 token chunk 意味着合并文件中单个表格行 (~20-50 tokens) 很可能与相邻内容混入同一 chunk. Profile F1 失败模式 (表格被 chunker 切断) 风险确认存在 — md-heading 分段策略有效. 合并文件时建议每个域的表格不跨 heading, 避免跨 chunk 断裂.

---

### Q3. Embeddings 模型及可选性?

**答**: File Search (vector store) 使用 **text-embedding-3-large** (256 维) 做语义嵌入, 同时结合 **text-embedding-3-small** 做混合检索中的关键词语义分量. OpenAI 自动选择, **用户/开发者不可在 GPT Builder 侧选择或替换** embedding 模型. Assistants API 侧同样无法指定 embedding 模型 (由平台固定).

Hybrid search: 检索时结合 vector 语义相似度 (`hybrid_search.embedding_weight`) 与关键词文本匹配 (`hybrid_search.text_weight`), 但 GPT Builder 侧两个权重均不可配.

**来源**:
- [OpenAI community: chunk size Q&A (mentions text-embedding-3-large at 256 dims)](https://community.openai.com/t/customizing-chunk-size-for-file-search-tool/1148708)
- [OpenAI: new embedding models announcement (text-embedding-3-large/small)](https://openai.com/index/new-embedding-models-and-api-updates/)
- [OpenAI: file search guide (hybrid search description)](https://developers.openai.com/api/docs/guides/tools-file-search)
- [Medium: RAG with OpenAI Vector Store and File Search](https://medium.com/@pirasanna.ravi/supercharging-ai-a-guide-to-rag-with-openais-vector-store-and-file-search-fe209063cbb8)

**对 PLAN 的影响**: text-embedding-3-large 质量较高, 对 SDTM 专业术语语义检索有利. 无需担心模型质量不足问题. 合并文件策略不需因模型限制做特殊处理.

---

### Q4. 检索 top-K 默认值及可调性?

**答**: **默认 top-K = 20 chunks** (针对 gpt-4* 和 o-series 模型); gpt-3.5-turbo 默认 5 chunks. 在 Assistants API/Responses API 侧可通过 `file_search.ranking_options` 调整, 支持指定 ranker (`"auto"` 或 `"default_2024_08_21"`) 和最低得分阈值. **GPT Builder 侧用户无法调整 top-K**, 固定使用默认 20.

**来源**:
- [OpenAI community: Customizing chunk size for file_search (top-K = 20 confirmed)](https://community.openai.com/t/customizing-chunk-size-for-file-search-tool/1148708)
- [WebSearch 摘要引自 Assistants API docs: "outputs up to 20 chunks for gpt-4* and o-series models"](https://platform.openai.com/docs/assistants/tools/file-search)

**对 PLAN 的影响**: top-K = 20 chunks × 800 tokens = 最多 16,000 tokens 检索内容注入 context, 加上 Instructions 和对话历史, 实际可用 context 仍充裕. 对 SDTM 域表格检索 (如 "列出 AE 所有 Core=Req 变量") 需要跨多 chunk 汇总 — top-K=20 理论上覆盖同一文件内多个相邻 chunk, 但跨文件检索精度需 A/B 实测验证.

---

### Q5. Plus / Team / Enterprise 三套餐文件数/容量限制差异?

**答**: 根据现有社区讨论和文档,  **20 文件/GPT 的硬限在 Plus、Team、Enterprise 三个套餐中相同**, 无套餐差异. 其他限制:

| 限制维度 | Plus | Team (Business) | Enterprise |
|---------|------|-----------------|------------|
| 知识文件数/GPT | **20 (硬限)** | **20 (硬限)** | **20 (硬限)** |
| 单文件大小 | 512 MB | 512 MB | 512 MB |
| 单文件 token 上限 | 2M tokens | 2M tokens | 2M tokens |
| 总存储 (per user) | 10 GB | 10 GB | 未找到官方差异数据 |
| 总存储 (per org) | — | 100 GB | 未找到官方差异数据 |
| GPT Store 发布 | **支持** | 支持 (workspace admin 可控) | 支持 (admin 控制) |
| 权限粒度 | 私有/链接/公开 | 私有/团队内/链接/公开 | 私有/组织内/链接/公开 (admin 可限制) |

**注意**: Enterprise 套餐的存储上限官方未明确公开与 Plus 的差异; Team 套餐"文件上传大小 50MB (对话上传)" 的提升针对的是**对话上传**而非 GPT Knowledge 文件上限 (Knowledge 文件上限仍为 512MB).

**来源**:
- [OpenAI community: knowledge file limits — 20 files applies across ChatGPT, Teams, and Custom GPTs](https://community.openai.com/t/what-is-the-knowledge-file-limit-that-can-be-uploaded-to-train-custom-gpts/653244)
- [docs-to-md.com: "ChatGPT, ChatGPT Teams, and Custom GPTs all share the same 20 file limit"](https://www.docs-to-md.com/blog/breaking-chatgpt-file-limitations-business)
- [OpenAI community: Data Limits for Custom GPTs (10 GB/user, 100 GB/org)](https://community.openai.com/t/data-limits-for-custom-gpts/845036)
- [ChatGPT advanced plans comparison 2025](https://www.datastudios.org/post/chatgpt-advanced-plans-plus-team-pro-and-enterprise-in-2025)

**对 PLAN 的影响**: 20 文件硬限在所有套餐一致, 合并粒度设计 (8-10 合并文件 + spare) 策略不需按套餐分支. Phase 0 carry-over E (权限粒度) 见下文 §对 profile 的反馈.

---

### Q6. GPT Store 发布审核标准 + 审核时间?

**答**: GPT Store 发布需满足以下条件:

**资格要求**:
- 必须是 ChatGPT Plus、Pro 订阅用户, 或 Enterprise/Team workspace 成员 (workspace admin 可控制发布权限)
- 必须完成 Builder Profile 设置 (姓名/组织名, 部分情况需域名验证)
- 若 GPT 包含 Actions, 必须填写有效的 Privacy Policy URL

**内容审核标准**:
- 禁止: 名称含粗俗语言、宣扬暴力、色情陪伴类、从事受监管活动 (金融/法律建议等)
- 要求: GPT 必须可靠实现其声称功能; 不得误导性描述功能; 遵守 OpenAI Usage Policies

**审核流程与时间**:
- 提交后进入审核队列, 可在 Dashboard 查看状态, 状态变更发邮件通知
- 社区和第三方报道: **典型审核 2-5 个工作日**; 复杂 GPT 可能更长
- 注意: 2025 年末 OpenAI 推出新的 "ChatGPT Apps" 框架 (Apps SDK), 与传统 GPT Store 并行, 新 Apps 框架审核标准更严格

**来源**:
- [OpenAI: Sharing and publishing GPTs (官方 Help Center, 内容通过 WebSearch 摘要)](https://help.openai.com/en/articles/8798878-building-and-publishing-a-gpt)
- [OpenAI: Usage Policies](https://openai.com/policies/usage-policies/)
- [OpenAI: Submitting apps to ChatGPT app directory](https://help.openai.com/en/articles/20001040-submitting-apps-to-the-chatgpt-app-directory)
- [MakeAIHQ: ChatGPT App Store Submission Guide 2025](https://makeaihq.com/guides/pillar/chatgpt-app-store-submission-complete-guide)
- [Community: app review process timelines](https://community.openai.com/t/app-review-process-timelines-for-chatgpt-app-store/1378947)

**对 PLAN 的影响**: Phase 5 发布阶段需提前准备 Builder Profile + Privacy Policy URL. SDTM 知识库 GPT 属于"教育/专业参考"类, 无明显违规风险, 审核时间预估 2-5 工作日. 建议 Phase 3 测试阶段先以"仅链接"分享, Phase 5 再申请公开 Store 发布.

---

### Q7. Conversation Starters 上限个数?

**答**: **GPT Builder 界面显示上限为 4 个**. 用户在 Configure 页面可以输入超过 4 条, 但 GPT 对话框中只显示前 4 条 (超出部分被截断不展示). 官方文档未明确声明"最多 4 个"为硬限, 但实际行为等同于 4 个上限.

该限制自 2023 年 11 月 GPT Builder 发布以来未见官方变更公告.

**来源**:
- [OpenAI community: Conversation starters — maximum of four? (2023-11, 确认 4 个显示上限)](https://community.openai.com/t/conversation-starters-maximum-of-four/521728)
- [OpenAI community: GPT Conversation Starter Question](https://community.openai.com/t/gpt-conversation-starter-question/495710)

**对 PLAN 的影响**: Rule E Q2=C (混合受众, 降新手门槛) 要求 4 个 Conversation Starter. 4 个上限与需求完全匹配, 无需妥协. A/B 矩阵中"4 个 Starter 各跑一次首答 PASS"测试保持有效, 全部 4 个均可使用.

---

### Q8. Indexing indicator 是否可靠?

**答**: **部分可靠, 但有已知可靠性问题, 建议以实际问答测试为准**.

社区报告显示: 文件上传后在 Configure 页面可见 (显示存在), 但 GPT 实际对话中无法检索到文件内容 — 表现为 GPT 声称"无法访问文件"或转而网络搜索. 此类问题在 2024-2025 年有多起社区报告, 重新上传文件后通常恢复正常.

官方未提供 indexing 完成的明确 UI 状态指示器 (不同于 Claude Projects 的进度条概念). 文件在 Configure 页面显示为"已上传"并不等于"已完成 embedding 且可检索".

**对比 Claude**: Claude Projects 的 indexing indicator 同样不可靠 (capacity_research.md 记录), GPT Builder 侧社区报告的问题模式相似 — 两平台在这一点上均需以问答实测验证, 不能仅凭 UI 状态判断.

**推荐验证方法**: 每次上传文件后, 立即提问文件中某个特定且唯一的术语 (如某个 SDTM 域的变量名), 验证 GPT 是否能准确引用该文件内容.

**来源**:
- [OpenAI community: Created GPT doesn't access uploaded documents in knowledge base](https://community.openai.com/t/created-gpt-doesnt-access-uploaded-documents-in-knowledge-base/1084695)
- [OpenAI community: Does GPT performance degrade over time? (重新上传修复问题)](https://community.openai.com/t/does-gpt-performance-degrade-over-time-do-gpts-benefit-from-re-indexing-or-reuploading-knowledge-documents/1289226)

**对 PLAN 的影响**: Phase 3 执行阶段每批上传后必须做实际问答验证 (不能仅看 UI 状态). A/B 矩阵应包含针对新上传文件的"直接命中"测试题.

---

### Q9. ChatGPT Knowledge 总量是否真无官方硬上限? 总 GB 限制来源?

**答 (Phase 0 carry-over B)**: 找到官方来源. **总量有上限**: 10 GB per user / 100 GB per organization, 该上限**跨所有使用场景共享** (对话附件 + Projects 文件 + Custom GPT Knowledge 文件共享同一存储池).

单 GPT 20 文件 × 512 MB = 理论上限 10,240 MB (~10 GB), 与 per-user 10 GB 存储上限基本吻合 — 实际上单个用户的 GPT 知识库总量受 per-user 10 GB 存储上限约束. 对于 SDTM 项目 (20 合并文件, 每文件预计 < 5 MB), 总量远低于 10 GB 上限, **不构成限制**.

Enterprise 套餐的存储上限官方未明确公布与 Plus 的差异. 100 GB/org 适用于 Team 套餐组织级别.

**来源**:
- [OpenAI community: knowledge file limits — "10 GB per user / 100 GB per org" 官方 help 文章引用](https://community.openai.com/t/what-is-the-knowledge-file-limit-that-can-be-uploaded-to-train-custom-gpts/653244)
- [OpenAI: File Uploads FAQ (help.openai.com, 通过 WebSearch 摘要确认)](https://help.openai.com/en/articles/8555545-file-uploads-faq)

**对 PLAN 的影响**: Profile B section "总量无官方硬上限" 描述不准确, 应修订为 "10 GB per user / 100 GB per org". 但对 SDTM 项目实际使用无影响 (远低于上限). Profile H section "是否需要 Deferred stub? 否 (暂定)" 决策维持有效.

---

### Q10. 权限粒度是否有 Team/Enterprise 更细分级?

**答 (Phase 0 carry-over E)**: **有差异**. 三套餐权限粒度如下:

| 套餐 | 私有 | 链接共享 | 团队/组织内共享 | GPT Store 公开 |
|------|------|---------|----------------|---------------|
| Plus | ✓ | ✓ | — | ✓ (需 Builder Profile) |
| Team (Business) | ✓ | ✓ | ✓ (workspace 内) | ✓ (admin 可禁用) |
| Enterprise | ✓ | ✓ | ✓ (组织内, admin 精细控制) | ✓ (admin 可禁用) |

GPT Builder 本身的编辑权限只有**owner** (创建者), 无协作编辑功能 — 不存在"读/写/管理"三级编辑权限. Team/Enterprise 增加的是**访问范围**控制 (谁能使用 GPT), 而非编辑权限分级.

Enterprise workspace admin 可以: 禁止成员将 GPT 发布到 Store, 限制外部 GPT 的使用, 管理组织内 GPT 目录.

**来源**:
- [OpenAI: Managing GPT access in Enterprise and Edu workspaces](https://help.openai.com/en/articles/8555535-gpts-chatgpt-enterprise-version)
- [OpenAI community: GPT Store publishing eligibility discussion](https://community.openai.com/t/publishing-custom-gpts-making-your-gpt-available-in-the-public-store/619493)
- [ChatGPT advanced plans comparison 2025](https://www.datastudios.org/post/chatgpt-advanced-plans-plus-team-pro-and-enterprise-in-2025)

**对 PLAN 的影响**: SDTM 项目使用 Plus 套餐, 权限模型为: 开发阶段 Private → 测试阶段 Link-only → Phase 5 Store 公开. 此路径在 Plus 套餐下完全支持. Profile E section "权限粒度: 读/编辑 (owner)" 描述需修订为更准确的"访问范围 (私有/链接/公开) + 编辑仅 owner".

---

## 未决问题 (调研未果, 转 Phase 3 实测)

1. **Indexing 完成确认方法**: GPT Builder 是否有明确的"embedding 完成"状态信号? 官方文档未找到. Phase 3 实测时以"上传后立即提问唯一术语"作为验证标准.

2. **Hybrid search 权重在 GPT Builder 侧行为**: text vs semantic 权重默认比例官方未公开用于 GPT Builder 侧. 影响: SDTM 术语 (专有名词) 是否更依赖 keyword 匹配? 需 A/B 实测 (e.g. 对比精确变量名查询 vs. 语义描述查询的命中率).

3. **Enterprise 存储上限确切数字**: 官方未公开 Enterprise 套餐 per-user/per-org 存储上限. 对本项目无影响 (使用 Plus), 记录存疑.

4. **GPT Store "传统 GPT" vs "新 Apps SDK"**: 2025 年末 OpenAI 推出新的 Apps SDK 框架并行于传统 GPT Store. 两者关系、传统 GPT 未来是否迁移、审核标准是否统一, 官方说明仍不清晰. **建议 Phase 5 发布前重新确认 Store 政策**.

---

## 对 PLAN 的修订 (关键)

基于以上调研, Phase 2 PLAN 需要修订/确认的内容:

| # | 原 profile 假设 | 调研后事实 | Phase 2 PLAN 修订 |
|---|----------------|-----------|------------------|
| 1 | Profile B "总量无官方硬上限" | 10 GB per user / 100 GB per org (共享存储池) | PLAN 标注存储上限; SDTM 项目 (~100 MB 以内) 不受影响, 无需 Deferred stub |
| 2 | Profile D "Instructions 长度限制 ~8K tokens (估算)" | 8,000 字符 (社区多次确认), 约 ~2,000 tokens | PLAN 系统提示设计控制在 7,500 字符以内留 buffer; 路由规则 + 域引导合并设计需测量字符数 |
| 3 | Profile C "Conversation Starters 上限待 P1 确认" | 显示上限 4 个 (与需求完全匹配) | A/B 矩阵 4 题 Starter 命中全部使用, 无需妥协 |
| 4 | Profile B "chunk 参数待 P1 确认" | 800 tokens chunk / 400 tokens overlap (固定, 用户不可调) | 合并文件时单表格不跨 heading, 避免跨 chunk 断裂; 每文件建议 < 500KB (约 ~300K tokens) 以控制 chunk 数量 |
| 5 | Profile B "top-K 待 P1 确认" | 默认 20 chunks (~16,000 tokens 检索内容) | A/B 矩阵跨 chunk 汇总题 (e.g. "列出 AE 所有 Core=Req 变量") 理论上 top-K=20 可覆盖, 实测验证 |
| 6 | Assistants API 与 GPT Builder 是否同源 | 底层同源但存储独立; Assistants API 将 sunset 2026H1 | 项目仅使用 GPT Builder, 不依赖 Assistants API; sunset 不影响本项目 |
| 7 | GPT Store 审核时间 "待 P1 确认" | 典型 2-5 工作日 | Phase 5 时间线预留 1 周审核缓冲; Phase 3 先用链接共享测试 |
| 8 | Profile E 权限粒度描述不完整 | Plus 套餐: 私有/链接/Store 公开三级; Team/Enterprise 增加组织内共享 | PLAN 发布路径: Private (Phase 3) → Link (Phase 4 A/B) → Store Public (Phase 5); Plus 套餐完全支持 |

**新增修订建议 2 条** (超出原 profile 范围, Phase 1 调研新发现):

- **修订 9**: PLAN 应明确指出 GPT Builder 侧 chunk/embedding 参数**不可配置** — 合并文件质量 (格式规范、heading 结构、表格完整性) 是唯一可控优化变量, 而非检索参数调优. 文件格式规范应提升为 PLAN P11 核心约束.
- **修订 10**: PLAN Phase 3 执行检查清单中必须加入"上传后实际问答验证" (不接受仅 UI 显示), 对应 Q8 indexing reliability 发现.

---

## 对 profile 的反馈 (Phase 0 carry-over 关闭状态)

| Carry-over | 来源问题 | 结论 | 状态 |
|-----------|---------|------|------|
| B 总量无官方硬上限来源 | Q9 | 有上限: 10 GB/user, 100 GB/org; 官方 File Uploads FAQ 来源; SDTM 项目不受影响 | **CLOSED** — 来源补齐, profile B 需小修 |
| E 权限粒度 Team/Enterprise 分级 | Q10 | Plus: 私有/链接/公开; Team: 加组织内共享 (admin 可控); Enterprise: 加精细 admin 管控. 编辑权限仅 owner, 无三级编辑分级 | **CLOSED** — 粒度确认, profile E 需小修 |
| C Indexing indicator 实测 | Q8 | 官方无明确 UI 完成指示器; 社区报告显示"显示已上传"≠"可检索"; 建议以问答实测替代 UI 状态判断 | **PARTIAL CLOSE → Phase 3 实测** — 文档层面已有社区证据, Phase 3 上传后需执行实测验证步骤 |

---

## 与 Gemini 侧 cross-reference (若适用)

**本平台独有结论 (Gemini Gems 不适用)**:

1. **20 文件硬限 + chunk RAG**: Gemini 是全量注入 (1M token 窗口), 无 chunk 概念. GPT 的 top-K=20 chunks 机制意味着跨文件长表汇总需要特别设计, Gemini 侧无此问题.

2. **GPT Store 公开发布**: Gemini Gems 仅支持个人私有. GPT 平台的 Store 发布路径 (含 2-5 工作日审核 + Builder Profile + Privacy Policy 要求) 是 Gemini 侧没有的流程成本.

3. **Conversation Starters 4 个固定上限**: Gemini Gems 的类似功能 (Conversation Starters / Suggested prompts) 限制待 Gemini 侧 Phase 1 调研确认, 不能直接借用 GPT 数据.

4. **Instructions 8,000 字符上限**: Gemini Gems system instruction 限制待 Gemini 侧确认. GPT 的 8K 字符约束需要在 Instructions 设计上做取舍 (详细路由规则 vs. 简洁原则).

**需要 Gemini 侧也确认的结论** (用于 cross-platform 对比):

- Conversation Starters 数量上限 (Gemini 侧 Phase 1 对应问题)
- System instruction 字符/token 上限
- 文件索引完成可靠性

---

*来源: 范本 `../../_template/03_research.md` 八问八答 + profile J + Phase 0 carry-over. 调研方法: WebSearch (help.openai.com 403 blocked, 改用 WebSearch 摘要 + community.openai.com WebFetch). 调研日期: 2026-04-20.*
