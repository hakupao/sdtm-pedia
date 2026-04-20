# Gemini Gems — Phase 1 前置调研 (Research, 简化 3+1+2 问版, Attempt 2)

> Phase: 1 (调研) · Tier 1-2
> Writer: oh-my-claudecode:executor subagent (Attempt 2 成功)
> 最后更新: 2026-04-20

---

## 必答 3 问

### Q1. 1M 窗口全量可用性 + 末尾召回衰减 (关键)

**结论 (综合官方 + 社区实测)**:

Gemini 1.5 的官方 needle-in-the-haystack 测试显示 >99.7% 单条信息召回率直到 1M tokens, 但这个数据有三个重要限制条件:

1. **"单条针"测试 ≠ 多条信息召回**. Google 官方文档明确承认: "In cases where you might have multiple 'needles' or specific pieces of information you are looking for, the model does not perform with the same accuracy." 官方建议把多条召回拆分为多个独立 query.

2. **官方基准测试环境 ≠ 实际使用**. 官方测试是静态"haystack"注入, 而非动态对话+复杂推理场景. 社区和开发者论坛的实测数据显示实际降级门槛远低于 1M.

3. **上下文位置依然影响质量**. Google 官方长上下文文档建议: **"put your query/question at the end of the prompt (after all the other context)"**, 暗示查询前置于内容尾部效果更好 — 即模型在处理前置查询时对上下文尾部内容仍有 recency bias.

**末尾召回实测数字** (来自多个来源综合):

| 来源 | 描述 | 降级门槛 |
|------|------|---------|
| Google 官方 (arxiv 2403.05530) | 单条 needle 召回 | >99.7% at 1M tokens (官方基准) |
| Google 官方 (多针任务) | 100 条 needle 召回 @ 1M tokens | ~60% (单针降至多针) |
| Google 官方 (ai.google.dev) | 多条信息召回建议 | 拆分 query, 不保证多针准确 |
| 社区实测 (developer forum) | 代码生成/编辑任务 | 100-150K tokens 开始降级 |
| 社区实测 (gemini-cli GitHub) | 对话+代码任务 | 20% 窗口使用后出现 "context rot" |
| Chroma 研究 (2025, 18 模型) | 通用长上下文评测 | Gemini 2.5 系列均出现位置偏差退化 |

**关键分析**: F-1 的 "末 100K-200K 区域下降" 估算有一定合理性, 但更准确的描述是:
- **中间位置** (buried in the middle) 才是最危险区, 这是 "Lost in the Middle" 效应 (Liu et al. 2023, TACL 2024)
- **尾部 (最后放置)** 因 recency bias 相对安全 — Google 官方也建议 query 放最后
- **对 SDTM KB 的影响**: terminology 放文件尾部 (如 profile.md 已建议) 是正确策略; 但若 terminology 体量超大 (713K tokens Rule E Q4=A), 需确保最关键的 terminology 块不被 "淹没在中间"

**来源**:
- [Google AI: Needle in Haystack Test](https://cloud.google.com/blog/products/ai-machine-learning/the-needle-in-the-haystack-test-and-how-gemini-pro-solves-it): Gemini 1.5 Pro >99.7% at 1M (单针), 60% at 1M (100 针任务)
- [Gemini 1.5 技术报告 (arxiv 2403.05530)](https://arxiv.org/html/2403.05530v2): 官方基准, 1M tokens 100% recall 直到 530K, >99.7% at 1M
- [Google 官方长上下文文档](https://ai.google.dev/gemini-api/docs/long-context): 多针任务建议拆分; 查询放最后 best practice
- [Liu et al. 2023 "Lost in the Middle" (TACL 2024)](https://aclanthology.org/2024.tacl-1.9/): 中间位置降级最严重 (U 形曲线). **注意**: 该论文测的是 GPT-3.5/4 和 Command, 不是 Gemini, 推广到 Gemini 须谨慎, 但 Gemini 类似现象已有社区实测印证
- [Google Developers Forum — "1M context window lie"](https://discuss.ai.google.dev/t/the-1m-context-window-lie/79861): 用户报告 100-150K tokens 后代码任务降级; Gemini 1.5 Pro 在 ~1.2M 开始 non-sensical
- [Chroma Context Rot Research (2025)](https://www.trychroma.com/research/context-rot): 18 模型含 Gemini 2.5, 全部在 position accuracy 出现衰减

**对 PLAN 的影响**:

- **1 批全上策略可维持**: 1M 窗口足够放 SDTM KB 全部内容 (估算 <800K tokens)
- **文件内容排列优化**: terminology 放文件尾部已是正确策略; 若 1 批全上导致 terminology 被夹在大量 domain 文件"中间", 需考虑合并文件结构确保 terminology 不落在 middle position
- **A/B 矩阵必含末尾召回测试**: 建议放 2 道 "末尾 codelist 精确 term" 题, 覆盖实际 terminology 块所在位置
- **多针任务预期**: SDTM KB 场景经常需要跨域多条信息 (e.g. "所有域中使用 EPOCH 的, 列出 Core 属性"), 这类 query 可能触达官方承认的多针降级区 (~60% @ 1M). 建议 Phase 3 实测量化

---

### Q2. 文件数 + 单文件大小限制 + pricing URL

**精确限制** (Gemini Gems Knowledge 功能):

| 参数 | 限制 | 来源 |
|------|------|------|
| 文件数上限 (per Gem) | **最多 10 个文件** | 官方文档 + 多个来源一致 |
| 单文件大小上限 | **100 MB** | 官方文档 |
| 总 Gem Knowledge 容量 | 未找到官方数字 (间接推算 ≤1G, 但受 1M tokens 窗口约束) | 未决 |
| 支持文件类型 | .txt, .md (text), .doc/.docx, .pdf, .rtf, .dot/.dotx, .hwp/.hwpx, .xls/.xlsx, .csv, .tsv, Google Docs, Google Sheets | 官方 |
| Google Drive 文件 | 支持 (自动同步最新版本) | 官方 |
| 订阅要求 | **Gemini Advanced** (Google One AI Premium, 即 Google AI Pro/Ultra) | 官方 |

**注意**: Gems Knowledge 文件上传功能最初 (2024-11) 首先向 Workspace (Business/Enterprise/Education) 用户推出, 后续扩展到 Gemini Advanced (Google AI Pro) 个人用户. 截至 2026-04, 个人 Google AI Pro 订阅用户均可使用.

**套餐差异**:

| 套餐 | 价格 (US) | Gems 可用? | Knowledge 上传? |
|------|-----------|-----------|----------------|
| Free | $0 | 可使用预设 Gems | 否 (仅 Gemini Advanced 有) |
| Google AI Plus | $7.99/月 | 可创建 Gems | 待确认 (可能仅有限) |
| Google AI Pro | $19.99/月 | 可创建 Gems + Knowledge 上传 | Yes (10 files, 100MB each) |
| Google AI Ultra | $249.99/月 | 同 Pro, 更高使用量 | Yes, Higher limits |
| Workspace (Business/Enterprise) | 按席位 | Yes (+ 团队分享) | Yes |

**注**: 价格以 US 为准, 日本/中国等区域按当地货币定价不同 (上述 `one.google.com/about/plans` 显示日元 ¥290/¥1,450/¥2,900).

**Google One pricing URL 有效性核实** (carry-over A):
- `https://one.google.com/about/plans` — **有效**, 但该页面主要显示 Google One 存储套餐
- 更准确的 AI 计划入口: `https://one.google.com/about/google-ai-plans/` — 显示 Plus/Pro/Ultra AI 计划
- 最直接的 Gemini 订阅页: `https://gemini.google/subscriptions/`

**对 PLAN 的影响**:

- 10 文件硬限 — 对 SDTM KB 影响重大: 必须把 293 个 .md 文件合并为 ≤10 个合并文件. 这与 profile.md H section "3-5 主题合并文件" 的预判完全吻合
- 100MB 单文件上限 — 预估合并后单文件 <5MB (text/markdown), 不构成瓶颈
- 1M tokens 窗口是真实约束 (不是 10 文件 × 100MB 的 MB 意义上的约束), 合并后需用 token 计数器验证不超 1M

**来源**:
- [Gemini Advanced now lets you add files to Gems (9to5Google, 2024-11)](https://9to5google.com/2024/11/12/gemini-advanced-gems-files/): 10 files, 支持文件类型列表
- [Google Workspace Blog — New Gems features](https://workspace.google.com/blog/product-announcements/new-gemini-gems-deeper-knowledge-and-business-context): Workspace 先行推出
- [one.google.com/about/google-ai-plans/](https://one.google.com/about/google-ai-plans/): AI 计划价格 (US $19.99/月 Pro)
- [gemini.google/subscriptions/](https://gemini.google/subscriptions/): Google AI Pro & Ultra 定价页
- [support.google.com/gemini answer 16275805](https://support.google.com/gemini/answer/16275805?hl=en): 各套餐使用限制 (prompts/day 等)

---

### Q3. Gems 分享机制 + 未来 roadmap

**官方现状** (截至 2026-04-20):

Gems 分享于 **2025-09-18** 正式推出, 相比 profile.md 撰写时 (2026-04-20 前调研假设"仅个人") **已发生重大变化**. 当前状态:

| 分享模型 | 支持? | 备注 |
|---------|------|------|
| 私有 (仅自己) | Yes | 默认 |
| 链接分享 (any link) | **Yes** (2025-09 新增) | 无需登录可使用 |
| 公开分享 (Google 可搜索) | **Yes** (2025-09 新增) | 任何人无需登录可发现 |
| 组织内分享 (Workspace) | **Yes** | 须管理员启用 |
| 非组织外部共享 | Yes (如 Drive 政策允许) | 管理员可限制 |
| Marketplace/Store 发布 | **未找到官方信息** | 未决 |

**权限细节**:
- 分享时可设 Viewer (可使用 Gem) 或 Editor (可修改 Gem Instructions + 分享他人)
- 使用 Google Drive 同一技术底层, 界面与 Drive 分享体验一致
- **重要限制**: Gems with uploaded files 只有在使用 "device files" 或 "Google Drive files" 时才能分享; 其他文件类型会导致分享按钮置灰 (grayed out)
- 免费用户是否可分享: 未明确官方说明, 但 Google 博客"you can now share the Gems you make"措辞未限定付费

**对 PLAN 的影响**:

Profile.md 中 E section 的 "仅个人" 结论在 2025-09 之后已过时, 需更新. 关键更新:
1. 链接分享和公开分享**已支持** (对于 device/Drive 上传的文件)
2. SDTM KB 使用 device 上传 .md 文件 → 满足分享条件, 可以生成分享链接
3. 团队共享 (Workspace 场景) 也已支持

**但实际分享的 use case 要慎重**:
- Editor 权限者可修改 Gem → 不适合给不信任方
- 分享后如果知识文件泄露 SDTM 内部研究数据 → 根据 CDISC 是否 open source 决定是否分享

**Roadmap**: Google 无明确公开 roadmap. 2025-09 的 Workspace 分享更新显示 Google 在持续扩大 Gems 用途; 基于此趋势推断 Marketplace 类功能 (类 ChatGPT Store) 在未来有可能, 但无时间表.

**来源**:
- [Google Blog — Sharing Gems (2025-09-18)](https://blog.google/products-and-platforms/products/gemini/sharing-gems/): 官方发布公告
- [Google Workspace Updates — Gem sharing (2025-09)](https://workspaceupdates.googleblog.com/2025/09/gem-sharing-gemini-app-workspace.html): Workspace 管理员控制细节
- [support.google.com — Share a Gem](https://support.google.com/gemini/answer/16504957?hl=en&co=GENIE.Platform%3DDesktop): 分享步骤 + 权限级别 + 文件类型限制

---

## 可选 Q4. Gemini API 能否复用 Gem Knowledge?

**结论**: **否. Gems 是 Web UI 功能, Gemini API 无法访问 Gem Knowledge.**

- Gems (包括其 Knowledge 文件) 存在于 gemini.google.com Web 界面, 不暴露 API 端点
- Gemini API (ai.google.dev) 是独立的开发者 API, 使用 Gemini 模型但与 Gems 无直接关联
- API 层有自己的 File API (files.upload / files.list), 但这些文件与 Gem Knowledge 不共享
- 社区讨论证实: 用户询问 "Are Gems available via API?" 的帖子被频繁发问, 表明官方无此能力

**对 Phase 7 的影响**:
- Gemini Gems 部署 (Phase 6.5) 与未来 RAG/KG pipeline (Phase 7) **完全独立路径**
- Phase 7 若用 Gemini API, 需要自行管理文件上传/context 注入, 不能复用 Gem Knowledge
- Phase 7 接口建议直接使用 Gemini API + 自定义 context injection, 无需考虑 Gem 路径

**来源**:
- [Google AI Developers Forum — Are Gems available via API?](https://support.google.com/gemini/thread/313792663/are-gems-available-via-api?hl=en): 社区讨论确认无 API 访问
- [Gemini API reference](https://ai.google.dev/api): 独立 API 文档, 无 Gems 相关端点

---

## 未决问题

1. **总 Gem Knowledge 容量上限** (MB 意义): 未找到官方数字. 10 files × 100MB = 1GB 理论上限, 但 1M tokens 窗口才是实际约束 (MD 文本格式下 1M tokens ≈ 700-800MB 原始文本). 建议 Phase 3 实测上传确认.

2. **Google AI Plus ($7.99/月) 是否支持 Gems Knowledge 上传**: 官方说明 Knowledge 上传面向 "Gemini Advanced" 用户, 但 Plus 与 Pro 之间的 Gems 差异边界不够清晰. 建议 Phase 2 或 3 前确认当前可用套餐.

3. **公开分享后 Gem 使用者是否受限于 Gemini Advanced 订阅**: 若分享给无 Gemini Advanced 的用户, 他们是否可以使用该 Gem? 官方说明不明确. ChatGPT Store 中免费用户可使用 Plus 创建的 GPT, Gemini 是否类似? 未决.

4. **实际文件数/token 计数**: 官方说 10 files, 但 Gems 知识不等于 context window 全量. token 到底如何计算尚不透明. 建议 Phase 3 实测校准 (与 Claude capacity calibration 类比).

---

## 对 PLAN 的修订

| # | 原假设 (profile.md) | 调研后事实 | 修订建议 |
|---|-------------------|----------|---------|
| 1 | E section: "支持团队共享 = 否 (当前 Gems 仅个人)" | 2025-09 起已支持链接/公开/组织内分享 | 更新 profile.md E section; 更新对 PLAN 的影响段落 |
| 2 | E section: "支持公开发布 = 否" | 已支持 Public sharing (可被 Google 搜索发现) | 同上 |
| 3 | F-1: "末 100K-200K 区域响应质量下降" (无来源) | 官方数字: 单针 99.7% at 1M; 多针 60% at 1M; 社区实测 100-150K 开始降级 (代码任务) | F-1 更新注明来源区间 + 加注"经验估算, Phase 3 实测校准" |
| 4 | H section: "文件切分粒度 3-5 主题合并文件" | 硬限 10 文件确认, ≤10 文件是硬约束 | 原估算 3-5 文件正确且有余量; 无需修改策略, 但应在 PLAN 中标注此为硬限 |
| 5 | C section: "单文件大小上限 数百 MB (待 P1 精确)" | 精确值: 100 MB per file | 更新 C section |
| 6 | A section: pricing URL 待复核 | 原 URL `one.google.com/about/plans` 有效但指向存储套餐; AI 功能更准确 URL 见 `one.google.com/about/google-ai-plans/` | 更新 A section URL + 价格 $19.99/月 (Google AI Pro, US) |
| 7 | B section: "容量硬上限 1M tokens" | 确认: 1M tokens (Gemini Advanced); Gemini 2.0 Pro API 支持 2M tokens, 但 Gems Web UI 以 1M 为标准 | 维持原假设, 标注 2M 仅 API 层 |
| 8 | Q4 可选: API 复用 | 无法复用, Gems 与 Gemini API 完全独立 | Phase 7 需独立设计 API context 注入方案 |

---

## 对 profile.md 的反馈 (Phase 0 carry-over 关闭状态)

| Carry-over | 来源 | 结论 | 动作 |
|-----------|------|-----|------|
| F-1: 末尾 100K-200K 数字来源 | Q1 | **partial** — 官方数字 (99.7% single, 60% multi-needle @ 1M); 社区实测 100-150K 降级; F-1 估算有部分依据, 但"末尾 100K-200K"说法不够精准 (应描述为"多针任务降级 + 中间位置最危险") | 更新 F-1 缓解措施注释, 加 "(经验估算, Phase 3 实测校准)". carry-over status: **partial → transfer_to_phase3** (Phase 3 实测量化) |
| A: Google One pricing URL 有效性 | Q2 | **close** — `one.google.com/about/plans` URL 有效, 页面存在 (日元价格). 更准确 AI 计划 URL 为 `one.google.com/about/google-ai-plans/` | 更新 profile.md A section URL 为 AI Plans URL; carry-over status: **close** |

---

## 与 ChatGPT 侧 cross-reference

**本平台独有结论**:
- **无 RAG, 全量注入** — 与 ChatGPT GPTs File Search (RAG 机制) 根本不同; 优点: 无检索失误; 风险: 多针任务降级
- **1M tokens 单批** vs ChatGPT 20 文件/512MB 两批 — 操作上 Gemini 更简单
- **已支持公开分享** (2025-09) — 类似 ChatGPT GPT Store 但更简单; 无专属 Store/Marketplace, 通过 Google 搜索发现
- **API 不可复用 Gem Knowledge** — ChatGPT 的 Assistants API 可以复用 GPT 的 knowledge store, 这是本平台明显劣势

**共通 A/B 题**:
- 边界诚实测试 (两平台均需 2 道) — 防 hallucination
- 精确术语查询 (codelist term) — 两平台均测基础召回
- 差异: Gemini 侧加强 "全域对比" 类题型 (充分利用 1M 全量注入优势); ChatGPT 侧加强 "chunk 检索一致性" 类题型

---

*Attempt 2 (Attempt 1 失败归档: `dev/evidence/failures/stage_phase1_attempt_1.md`). 规则 B.*
