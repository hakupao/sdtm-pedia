# Phase 0 Research — Independent Review (Rule D Pass 1)

> Reviewer: `critic` subagent (Rule D 异 type, writer = main session)
> Review date: 2026-05-22
> Documents reviewed: PLAN.md, EXECUTION_PLAN.md, research/chunker_feasibility_2026-05-22.md, research/llm_providers_2026-05-22.md
> Upstream: `docs/DESIGN_RAG_KG.md` (Approved 2026-04-16)
> Mode: Started THOROUGH, escalated to ADVERSARIAL after surfacing 3+ MAJOR findings (multiple unverified numerical claims + missing risk categories + internal inconsistency).

## Pre-commitment Predictions

Before deep reading, based on the project type (RAG + KG plan over an established KB) and prior project rhythm (Tier 2 / Rule D / CLAUDE.md 严), I predicted these high-probability problem areas:

1. **Numerical claims in `chunker_feasibility` not actually verified end-to-end against KB** — research drafts in this project repeatedly cite "实测" numbers that don't survive re-grepping.
2. **Internal inconsistency PLAN ↔ EXECUTION_PLAN** — different counts/phases/PASS rules between the two writer products of the same session.
3. **Risk list will miss "soft" operational risks** — API key management, rate limits, data volume bounds, KB-RAG sync trigger, single-user assumption.
4. **Workload estimates too tight** — Tier 2 with Rule D isolation overhead is consistently underestimated by 30-50% in past 06 phases.
5. **Rule D / PASS wording drift** — CLAUDE.md (user global) defines "PASS 四条"; project plans may have inflated to "PASS 五条" without explanation.

Actual outcome: **all 5 predictions hit**. Multiple HIGH-confidence findings in each area.

## Verdict

**CONDITIONAL_PASS** — 方向、研究方法、整体落地化判断都正确, **但有 3 处必修 HIGH (数字事实错误 + 内部矛盾 + 规则术语错位)** 必须在用户 ack 前修掉, 否则 Phase 1A 启动会带着错误前提进。

## Findings Summary

- HIGH: 3
- MEDIUM: 7
- LOW: 6
- INFO: 4

---

## 1. M-1 对齐上游设计

### 1.1 5 处偏离的 evidence 支撑度

| 偏离 # | PLAN 描述 | evidence 是否充分 | 评判 |
|--------|-----------|-------------------|------|
| A-1 (examples.md domain-aware) | chunker_feasibility §3.2 (PC H4 嵌套实证) | ✅ 强 | PASS |
| A-2 (INDEX.md system prompt 注入) | chunker_feasibility §7.2 | ✅ 强 (16.7KB / ~4K token 验证) | PASS |
| A-3 (默 LLM = Sonnet 4.6) | llm_providers §6 | ✅ 强 | PASS |
| B-1 (eval 提前到 Step 2 后) | "个人判断 + Tier 2 流程" | ⚠️ 弱 — 没有可量化前案对比 | MED finding (见 F-4) |
| B-2 (Phase 2 KG defer + 12 题 < 50% gate) | "个人判断 + 成本/价值评估" | ⚠️ 弱 — 50% 的阈值无量化推导 | MED finding (见 F-5) |

### 1.2 未声明的隐式偏离 (writer 没说自己偏了的地方)

- **设计文档 §3.1 VARIABLE_INDEX 策略 = "Split by alphabetical groups"** vs **PLAN §6.5 / chunker_feasibility §8.3** 改成了 "§一 1 chunk + §二 24 H3 域各 1 chunk + §三 字母段 ~5 chunk"。这是一个**实质性偏离**但既没列在 §1 5 处偏离表里, 也没作为 A-N 编号纳入偏离清单。**evidence 即 chunker_feasibility 实测 ≠ 设计假设**, 修正合理, 但**必须显式声明为偏离 A-4 或 A-5**。详见 F-2。
- **设计文档 §3.1 chapters 策略 = "By `##` section, large sections split at `###`"** vs **PLAN §6.3 size-aware (>50KB → ### / ≤50KB → ## / ≤20KB → 整文件)**。这是把设计文档的二档规则改成三档可量化规则, 是合理细化, 但同样**没列在偏离清单**。
- **设计文档 §2 仓库布局 = `sdtm-rag/` sibling project**, PLAN §2.1 改成 `branches/07_rag_kg/sdtm-rag/`. 这条 PLAN 明示了 (用户 ack), OK。

### 1.3 设计 Step 1-12 → PLAN Phase 映射

逐一核对设计文档 §7 roadmap → PLAN §5 Phase:

| 设计 Step | PLAN 映射 | 完整性 |
|-----------|-----------|--------|
| Step 1 仓库脚手架 | Phase 1A.1 | ✅ |
| Step 2 ingest | Phase 1A.3-1A.5 | ✅ |
| Step 3 Q&A 服务 | Phase 1B | ✅ |
| Step 4 dataset validation | Phase 1C | ✅ |
| Step 5 Streamlit | 散在 1B.4 + 1C.5 | ✅ |
| Step 6 evaluation | Phase 1B5 (sanity) + Phase 1D (full) | ✅ (B-1 改了顺序) |
| Step 7-12 (KG) | Phase 2 (deferred) | ✅ (有 gate) |

映射**完整**。

---

## 2. M-2 调研充分性 (T2 + T3 evidence 吸收度)

### 2.1 chunker_feasibility R-1~R-4 在 PLAN 落地度

| Research 风险 | PLAN §8 风险表 | PLAN §6 chunker 规范 | 评判 |
|---------------|-------------------|----------------------|------|
| R-1 examples.md heading level (PC H4) | ✅ R-1 (§8) | ✅ §6.2 (domain-aware ExamplesChunker) | 双落地 |
| R-2 TA mermaid + table 混排 | ✅ R-2 (§8) | ✅ §6.2 (split point 保护) | 双落地 |
| R-3 LB part | ✅ R-3 (§8) | ✅ §6.4 (TerminologyChunker LB 兜底) | 双落地 |
| R-4 ch04 130KB | ✅ R-4 (§8) | ✅ §6.3 (size-aware) | 双落地 |

调研充分性: **PASS**。

### 2.2 llm_providers §6 决策表落地

PLAN §4.2 LLM 表 vs llm_providers §6 推荐:

- ✅ Sonnet 4.6 主答 → PLAN 接住
- ✅ Opus 4.7 难题 → PLAN 接住
- ✅ Haiku 4.5 轻分类 → PLAN 接住
- ✅ DeepSeek V4-Flash 复检 (非思考模式) → PLAN 接住 (含明确避 V4-Pro multi-turn bug)
- ✅ ChatGPT Plus 代理不入生产 + 留 base_url 接口 → PLAN §4.2 + Open Issue 接住
- ✅ LiteLLM Issue #26395 + v1.84.0 breaking changes → PLAN §4.4 表接住, 1A.2 sanity 测试

调研充分性: **PASS**。

### 2.3 [UNVERIFIED] 项 follow-up 处理

llm_providers §7 列了 5 个 [UNVERIFIED] 项, chunker_feasibility §13 列了 6 个未验证项。

**PLAN 处理度**:
- ✅ V4 Pro bug 验证 → Phase 1A.2 (litellm sanity) 已安排
- ✅ V4 Pro 折扣到期 → R-9 风险 + runtime 监控
- ⚠️ Haiku 4.5 context window 200K 推测 → **PLAN 完全没提**, R-13 未建 (见 F-7)
- ⚠️ LiteLLM v1.84.0 breaking changes 细节 → PLAN §4.4 仅说 "单机 SDK 模式可能不影响", 没明示验证步 (见 F-8)
- ⚠️ general_part1.md / qs_part1.md / questionnaires/ 43 文件 H2 实测 → **chunker_feasibility §13 列了, PLAN §8 风险表完全没接住**, 没标 Phase 1A 必查 (见 F-3, HIGH)
- ⚠️ mermaid 嵌套 / 表格变体 / tiktoken 实测差 → 同上, PLAN 没接

总评: **PASS 但缺 4 个 follow-up 钩子**, 一项 HIGH (F-3)。

---

## 3. M-3 风险清单完整性

### 3.1 你建议清单的逐条核查

| 你点名风险 | PLAN 是否覆盖 | 评判 |
|-----------|---------------|------|
| Embedding rate limit (OpenAI text-embedding-3-small) | ❌ 完全未提 | MED (F-9) |
| Chroma persistence / 备份策略 | ❌ 完全未提 (data/chroma/ 仅 .gitignore) | MED (F-10) |
| LLM API key 泄漏 / `.env` 管理 | ❌ 完全未提 | MED (F-11) |
| 上传文件大小限制 (用户传 100GB CSV) | ❌ 完全未提 | LOW (F-12) |
| 多用户并发 (Phase 1 单用户?) | ❌ 完全未提 | LOW (F-13) |
| Reingest 触发机制 (KB 改但没人触发) | ⚠️ metadata 有 kb_commit_sha 但**没 trigger 设计** (R-7 仅 "runtime", 没 step) | MED (F-14) |

### 3.2 R-12 ChatGPT Plus 评估准确性

llm_providers §3 的 5 类代理方案 + ToS 三条违规 + 5 项实际风险 (账号封禁 / 极低稳定性 / 零并发 / 数据安全 / 长跑生产) 评估**扎实, 有 ToS 引文**。PLAN §4.2 + R-12 风险表落地为 "不接入生产 + chatgpt.com 网页用 Plus + 留 `openai/` base_url 接口"。

**这是正确的处理**, 没有误判用户诉求 — 用户已付了订阅, 调研给的"网页直接用 + 独立 API 账户 + DeepSeek 顶替"三档分层非常合理, PLAN 接住了。

**唯一可挑剔点**: PLAN §4.2 最后一句 "daily prototype / 人工测试 → 用户直接在 chatgpt.com 网页用 Plus 配额" 隐含假设用户**愿意手工切上下文**。如果用户实际诉求是 "把 Plus 直接接到 IDE 让 Claude Code 调", 那 PLAN 没解决, 但这不是 PLAN 的锅, 是诉求边界问题。归 INFO。

### 3.3 我额外发现的缺漏风险

- **R-NEW-1**: `metadata.cdisc_section_id` 跨 chunk 一致性 — 06 P5 reverse_ledger 用的 `§6.3.5.9.3` 格式 PLAN 也用, 但 spec.md / model/ / chapters/ 等没 section_id 时 metadata 是 `null` 还是省略字段, PLAN §7 schema 没明示。MED (F-15)。
- **R-NEW-2**: pyreadstat (Phase 1C XPT/SAS7BDAT 解析) 在 Apple Silicon Python 3.11+ 安装可能 build 失败 (依赖 ReadStat C lib) — 历史 known issue。PLAN §4.3 直选, 没列风险。LOW (F-16)。
- **R-NEW-3**: Streamlit 上传同时 RAG 检索 + LLM 调用, **超时 (>60s) UX 处理**没设计 — Streamlit 默认 stream 行为 + LiteLLM stream=False, 用户上传 50MB CSV 时可能 30s+ 等待无反馈。LOW (F-17)。
- **R-NEW-4**: Phase 1D.2 "跨模型对比 (Sonnet vs Opus vs DeepSeek V4-Pro)" — V4-Pro 在 thinking 模式有 LiteLLM bug, PLAN §4.2 自己说复检用 V4-Flash, 但 1D.2 又跑 V4-Pro。**自相矛盾**。MED (F-6)。

---

## 4. M-4 工期估算合理性

### 4.1 与 06 P2 实绩比对

06 P2 chunker round 复杂度 (B-03c) 据我观察的 reverse_ledger 规模 (10,435 atoms), 是真正大规模处理。但 P2 B-03c **不是 chunker 实现**, 是 atom 反向匹配。**PLAN.md 把 06 P2 当 chunker round 引用 (§5 Phase 1A.6)** 是误植。06 P5 的 reverse_ledger 才是 atom ground truth, P5 才是抽检对照源, 1A.6 描述 "06 P5 reverse_ledger.jsonl" 是对的, **但 PLAN §10 没明示 P5 vs P2 区别**。这是 LOW finding (F-18)。

### 4.2 Phase 1A 2.5-3 d 合理性

| 1A 子步 | PLAN 工期 | 现实评估 |
|---------|-----------|---------|
| 1A.1 脚手架 | 0.3 d | OK |
| 1A.2 LiteLLM sanity | 0.2 d | OK |
| 1A.3 chunker 6 类实现 (并列 3 批) | 1.5 d (并列 0.9) | **过紧** — examples.md alone (domain-aware + mermaid 保护 + 配置 + metadata 7 字段) 单 batch B 就要 0.6-0.8 d, terminology LB part 模式识别 + 巨型 codelist 切片 batch C 要 0.6 d, 并列后实际 ~1.0-1.2 d |
| 1A.4 测试套件 | 0.5 d | **过紧** — 4 domain × 2-3 边界 case 各一, 失败回归在内 ≥ 0.7 d |
| 1A.5 ingest 全量 + sample 10 验证 | 0.3 d | OK (假设 OpenAI API 顺) |
| 1A.6 Rule A 抽检 (N=10) | 0.2 d | OK |

**实际 1A**: 直列 ~4.0 d, 并列 ~2.8-3.5 d, **PLAN 估 2.5-3 d 偏紧, 应放到 3-3.5 d**。MED (F-19)。

### 4.3 Phase 1C 3.5-4 d 合理性

7 类规则 + RAG 评审 + 假错误集 20 例 + UI = 3.5-4 d, 估计**严重过紧**:
- 1C.2.x 规则引擎边界 case (空表 / 重复主键 / 缺列 / Char 列出现 Num / Date 格式不一) ≥ 1.5 d
- 1C.3 RAG 语义评审 + 5 类语义检查 + 假错误集 20 例标注 (这 20 例本身就需 0.5 d 设计) ≥ 1.5 d
- 1C.5 UI 不止 0.3 d (上传组件 + 进度条 + 报告渲染 + 边界 UX)

**实际 1C**: ~5-6 d。PLAN 3.5-4 d 是 30-40% 偏低。MED (F-20)。

### 4.4 Phase 1 总 10-13 d 整体合理性

- 写作误差 30-50% 在 Tier 2 项目里是常见的, EXECUTION_PLAN §9 自己列的 "16 d 直列 → 10-13 d 并列" 已用了乐观假设 (Rule D 反复 + 失败 attempt 没乘 1.5 系数)。
- 06 P2 实绩并行只压缩 15% — PLAN 估 20-38% 是**显著高估**。EXECUTION_PLAN §9 25-37% 是 fan-out 三批 chunker writer 的并行, 但主 session 集成 + Rule D reviewer 串行, 实际可压缩 15-25%。
- **建议**: 总工期上限改 **13-16 d** 而不是 10-13 d。MED (F-21)。

### 4.5 并行 20-38% 是否过夸

EXECUTION_PLAN §9 显式列了 Phase 1A 25-37% 的来源 = "1A.3 三并列"。但实际:
- 三 batch 各 ~0.5-0.7 d, 集成 + Rule D 反复 ~0.3 d, 实际 ~1.0-1.2 d
- 比直列 1.5 d 压缩 ~25%, 不是 40%

**所以 Phase 1A 25% 压缩可以接受, 但 Phase 1 总 20-38% 是把 Phase 1B / 1B5 / 1D 没并行空间的工期也按比例压, 没区分**。MED (F-22)。

---

## 5. M-5 PASS 五条可执行性

### 5.1 PASS 五条 vs CLAUDE.md "PASS 四条" 术语不一致 ★ HIGH

CLAUDE.md (project root) 第 73 行明确写: `**PASS 四条** (规则 D 强制): evidence 存在 / writer 产物合规 / 独立 reviewer subagent PASS / 用户口头 ack`.

PLAN §9 / EXECUTION_PLAN 多处用 "PASS 五条"。两者实质内容是**项目 PLAN 在 CLAUDE.md 四条之外加了**:
- 规则 A 抽检 PASS (压缩率 > 50% 时 N 样本抽检)

这是**合理的本项目细化**, 但**没有显式说明 "本旁枝在 CLAUDE.md PASS 四条之外, 加规则 A 抽检为第五条"**, 读者会迷惑到底是哪个。

**修法**: PLAN §9 开头加一句: "项目根 CLAUDE.md 定义 PASS 四条 (evidence / writer / reviewer / 用户 ack); 本旁枝 RAG 项目因含 chunker 高压缩率步, 加 '规则 A 抽检' 为第五条, 合计五条。" 见 F-1。

### 5.2 各 Phase PASS 适用性

PLAN §9 五条**全 Phase 通用**, 没按 Phase 细分 (e.g. Phase 0 PASS 在 §5 单列了, Phase 1A PASS 在 EXECUTION_PLAN §1A 末尾, Phase 1B 没列, Phase 1B5 没列, Phase 1D 没列)。**EXECUTION_PLAN 在 1A 末尾和 1C 末尾列了 PASS 五条, 但 1B / 1B5 / 1D / 收口都没列**。MED (F-23)。

### 5.3 规则 A 抽检在 RAG 场景的定义

PLAN §9.4: "本 RAG 项目: chunker 改了走 N≥10 sample 验; eval 数据集走 N≥5 ground truth 独立 verify"

**够具体吗?** 部分够:
- ✅ chunker 改了 N≥10 — 具体
- ⚠️ "eval 数据集 N≥5" — 模糊。Phase 1B5 是 20 题, Phase 1D 是 50 题, 抽 5 ground truth 是抽哪 5? 是 reviewer 独立写 5 个 ground truth 对照 writer 写的 20/50 题? 还是 reviewer 从 writer 已写的 20/50 题里抽 5 题独立验 LLM 答?
- ❌ Phase 1C 规则引擎 (20 例假错误集) 抽检 N 没明示

**修法**: §9.4 加细化, 或在每个 Phase 末尾的 PASS 描述里显式写 N 和定义。MED (F-24)。

### 5.4 独立 reviewer subagent_type 矩阵

EXECUTION_PLAN §2.1 矩阵列了 9 行 writer ↔ reviewer 配对, 全部异 type, OK。

**漏的一类**: Phase 0 自己的 PLAN reviewer — 矩阵第 1 行写 "writer = main session, reviewer = architect 或 critic", 但 main session 不是 subagent_type, 是**主 session**。Rule D 原文 "Writer 和 Reviewer 不能是同一 agent 同一 session **自审**", main session writer + architect/critic subagent reviewer 显然不是同 session 自审。**OK 但矩阵格式不严谨**, 建议把 main session 标 `<main>` 或 "Bojiang/Claude main" 而不是空。LOW (F-25)。

---

## 6. M-6 内部一致性 (PLAN vs EXECUTION_PLAN)

### 6.1 工期一致性

| Phase | PLAN.md | EXECUTION_PLAN.md §9 | 一致? |
|-------|---------|----------------------|-------|
| Phase 0 | 1 d | 1 d | ✅ |
| Phase 1A | 2.5-3 d | 2.5-3 d (并列), 4 d (直列) | ✅ |
| Phase 1B | 2 d | 2 d | ✅ |
| Phase 1B5 | 0.7-1.5 d | 0.7-1.5 d | ✅ |
| Phase 1C | 3.5-4 d | 3.5-4 d (并列), 4.5 d (直列) | ✅ |
| Phase 1D | 2 d | 2 d | ✅ |
| 收口 | 1 d | 1 d | ✅ |
| Phase 1 总 | 10-13 d | 10-13 d (16 d 直列) | ✅ |

工期: **PASS**.

### 6.2 决策表一致性

PLAN §4.2 LLM 表 vs llm_providers §6 vs EXECUTION_PLAN 引用 全模型 ID / 价格一致。

### 6.3 Phase 1A.1-1A.6 编号 / 命名一致性: **PASS**

### 6.4 KB 文件数 vs Chunk 总数 ★ HIGH (F-2 主因)

详见 Findings 详表 F-2。

### 6.5 chunker_feasibility 自身数字内部冲突

- §0 TL;DR: "实际 chunk 总数估算 **~3500-4200**"
- §9 表总计: "**~4150-4500 chunks**"
- §12 输入 PLAN: "合计 ~4150 chunks"
- §14 结论: "预计 chunk 总数 **~4150**"
- PLAN §3 TOTAL: "**~4319 chunks**"

跨度 ~25%, §0 TL;DR 是错的, 应改为 ~4150。MED (F-26)。

### 6.6 chunker_feasibility 内事实错误 (HIGH 主因, 详见 F-2)

详 Findings 详表 F-2。

---

## 7. M-7 CLAUDE.md 项目规则遵守

### 7.1 规则 A: 不在 chunker 触发 (chunking 不重写), 但 Phase 1C reviewer.py LLM 输出大概率触发, PLAN §9.4 没明示 MED (F-27)
### 7.2 规则 B: EXECUTION_PLAN §6 完整, PLAN 仅 1 句 Note, LOW (F-28)
### 7.3 规则 C: Phase 1 收口写了, Phase 0 closure 短 retro 建议但非硬要求 INFO (F-29)
### 7.4 规则 D: 矩阵覆盖正确, "main session" 注解可改 LOW (F-25)
### 7.5 写作规则不适用于 Tier 2 PLAN/EXECUTION_PLAN, _progress.json + CHANGELOG 不膨胀 OK

---

## Findings 详表

| # | Severity | 维度 | 文件 | 位置 | Finding | 建议 |
|---|----------|------|------|------|---------|------|
| **F-1** | **HIGH** | M-5 | CLAUDE.md vs PLAN.md / EXECUTION_PLAN.md | PLAN §9 / EXECUTION_PLAN 多处 | PLAN 用 "PASS 五条" 但项目根 CLAUDE.md 明确 "PASS 四条"; 没说明本旁枝在 CLAUDE.md 4 条之外加 "规则 A 抽检" 为第 5 条, 读者会困惑哪个对 | PLAN §9 开头加: "项目根 CLAUDE.md 定义 PASS 四条 (evidence / writer / reviewer / 用户 ack); 本旁枝因含 chunker 高压缩率步, 加 '规则 A 抽检' 为第五条" |
| **F-2** | **HIGH** | M-2 / M-6 | chunker_feasibility_2026-05-22.md + PLAN.md | chunker_feasibility §6.1 / §8.1 / §3.2; PLAN §3 / §6.5 | chunker_feasibility 多处 "实测" 数字与 KB 真实状态不符: (a) lb_part4 漏列 (实测有 2 个 H2 codelist, chunker 假设只 lb_part1-3); (b) VARIABLE_INDEX H3 写 24 实测 63; (c) PC examples H4 写 16 实测 14; (d) supplementary 命名写 general_part* 实测 supplementary_part1-6. PLAN §3 / §6.5 直接吃错数. 这些事实错误会让 chunker 实现少处理 lb_part4 + 假定 24 H3 (代码 unit test 将失败) | (1) chunker_feasibility 修正 4 处事实 (2) PLAN §3 / §6.5 同步更新 (3) 加 1 行声明: "Phase 1A 写 chunker 前 main session 必须 re-grep 验证 H2/H3/H4 实际数值, 不信任 chunker_feasibility 估算" |
| **F-3** | **HIGH** | M-2 | chunker_feasibility §13 + PLAN.md §8 | PLAN §8 风险表 | chunker_feasibility §13 列了 6 个 [UNVERIFIED] (general_part / qs_part / questionnaires 43 文件 H2 实测 / mermaid 嵌套 / 表格变体 / tiktoken 实测), **PLAN §8 风险清单完全没接住任一项 follow-up**. 没有 R-13 / R-14 / R-15 等. 等 Phase 1A 写代码时才发现 questionnaires/ 43 文件结构不明就太晚 | PLAN §8 加 R-13 ~ R-17 风险, 标 "Phase 1A.3 前 main session 必须 grep verify". 或加 PLAN §13 Next Actions 第 6 条: "Phase 1A.0 sanity: re-grep verify 6 个 [UNVERIFIED] 项再开 1A.3 chunker writer" |
| F-4 | MED | M-1 | PLAN.md | §1 B-1 行依据 | B-1 (eval 提前到 Step 2 后) evidence 描述是 "个人判断 + Tier 2 evidence-driven 流程", 缺可量化的前案对比 | 加引用 06 P5 P6 RAGAS 验证证明早 eval 价值; 或承认 "工程经验判断, 无强 evidence" |
| F-5 | MED | M-1 | PLAN.md | §1 B-2 + §5 Phase 2 gate | B-2 "RELATION 类 12 题召回 < 50% 才启动 KG" 阈值无量化推导 | 加 "50% 基于 RAGAS RELATION baseline 文献" 或 "1D 后 main + Bojiang 再校准阈值, 不锁死" |
| F-6 | MED | M-1 / M-6 | PLAN.md vs EXECUTION_PLAN.md | PLAN §4.2 vs EXECUTION_PLAN §Phase 1D.2 | EXECUTION_PLAN §1D.2 "跨模型对比 (Sonnet vs Opus vs V4-Pro Reasoner vs V4 Flash)" Reasoner 即 V4-Pro 思考模式, 与 PLAN §4.2 自己说 "复检用 V4-Flash 非思考模式" 自相矛盾 | EXECUTION_PLAN §1D.2 改 "V4-Pro 非思考 single-turn" |
| F-7 | MED | M-2 | llm_providers §7 + PLAN.md | PLAN §8 | Haiku 4.5 context window 仅推测 200K | PLAN §8 加 R-13: Haiku context 验证 |
| F-8 | MED | M-2 | llm_providers §7 + PLAN.md §4.4 | PLAN §4.4 + 1A.2 | LiteLLM v1.84.0 breaking changes 没明示验证步 | 1A.2 加 sub-step: "跑 LiteLLM Router 2 轮对话 验证 fallback chain" |
| F-9 | MED | M-3 | PLAN.md §8 缺漏 | — | OpenAI embedding rate limit (3000 RPM Tier 1) 没列风险 | 加 R-13b + ingest.py 限速 + 缓存 |
| F-10 | MED | M-3 | PLAN.md §2.2 / §8 | — | Chroma data 没备份策略 | 加 R-13c + ingest.py 加 backup ckpt |
| F-11 | MED | M-3 | PLAN.md §2.2 + 1A.1 | — | LLM API key / .env 管理没明示 | 1A.1.c: .env / .env.example + .gitignore + README env vars 列表 |
| F-12 | LOW | M-3 | PLAN.md §1C | 1C.1 | 上传文件大小上限未定 | 加 100MB 上限 + chunksize 流式 |
| F-13 | LOW | M-3 | PLAN.md §0.2 | — | 单用户假设未明示 | PLAN §0.2 加 "Phase 1 单用户/单租户" |
| F-14 | MED | M-3 | PLAN.md §8 R-7 | — | reingest trigger 没设计 | 1A.5.d: server/main.py 启动比对 git HEAD; 或明示 Out-of-scope |
| F-15 | MED | M-3 | PLAN.md §7 | — | metadata.cdisc_section_id 跨 chunk null vs omit 未明示 | schema 加注: 不适用字段一律 None, 不省略字段 |
| F-16 | LOW | M-3 | PLAN.md §4.3 | — | pyreadstat on Apple Silicon Py 3.11+ build issue | 1A.1 加 sanity 测试 + sas7bdat fallback |
| F-17 | LOW | M-3 | PLAN.md §1C | 1C.5 | Streamlit 超时 UX 未设计 | st.status / st.progress + 60s warning |
| F-18 | LOW | M-4 | PLAN.md §5 | 1A.6 | "06 P2 round 复杂度" 应改 "06 P5 reverse_ledger" | 改 P5 |
| F-19 | MED | M-4 | PLAN.md §5 | Phase 1A 工期 | 2.5-3 d 偏紧 | 改 3-3.5 d |
| F-20 | MED | M-4 | PLAN.md §5 | Phase 1C 工期 | 3.5-4 d 严重过紧 | 改 5-6 d |
| F-21 | MED | M-4 | PLAN.md §10 + EXECUTION_PLAN §9 | — | Phase 1 总 10-13 d 未含 Tier 2 仪式 + Rule D 反复 overhead | 改 12-15 d (或 13-16 d 含失败回归) |
| F-22 | MED | M-4 | EXECUTION_PLAN §9 表 | — | Phase 1 总 20-38% 压缩过夸 | 表加注: 总压缩主要 Phase 1A (25%) + 1C (15%) |
| F-23 | MED | M-5 | PLAN.md §9 + EXECUTION_PLAN | — | PASS 五条没按 Phase 细分 (1B/1B5/1D/收口缺) | EXECUTION_PLAN 每 Phase 子段加 PASS |
| F-24 | MED | M-5 | PLAN.md §9.4 | — | "eval N≥5 ground truth" 不够具体 | §9.4 细化 (a) 1B5/1D: reviewer 独立 N=5 ground truth; (b) 1C: verifier 独立 N=5 错误标注 |
| F-25 | LOW | M-5 | EXECUTION_PLAN §2.1 | — | 矩阵 "main session" 缺类型注解 | 矩阵注: main 视为非 subagent, 与任意 subagent_type 异 type |
| F-26 | MED | M-6 | chunker_feasibility | §0 | §0 TL;DR "~3500-4200" vs §9/§14 "~4150" 跨 25% 不一致 | §0 改 ~4150 |
| F-27 | MED | M-7 | PLAN.md §9.4 | — | Phase 1C reviewer.py LLM 输出大幅压缩, 规则 A 应触发, PLAN 没明示 | §9.4 加 (c) 1C reviewer.py 抽 N≥5 user-data-row 验业务规则准确率 |
| F-28 | LOW | M-7 | PLAN.md §13 | — | 失败回路仅 Note, 没引用 EXECUTION_PLAN §6 完整规范 | PLAN 加引用 → EXECUTION_PLAN §6 |
| F-29 | INFO | M-7 | PLAN.md §5 | Phase 0 | Phase 0 closure 短 retro 非硬要求 | 建议加, 但非阻断 |
| F-30 | INFO | M-3 | PLAN.md §0.2 | — | H-1 仅引用不显示 | 加 (H-1: knowledge_base/ 严格只读) 内嵌定义 |
| F-31 | LOW | M-3 | PLAN.md §3 / §6 | — | chunk 总数 4319 vs chunker_feasibility 4150 差 4% 没解释 | PLAN 统一 ~4150-4300 |
| F-32 | INFO | M-1 | PLAN.md | §0.1 | "06 P7 99.02% coverage" 表述歧义 (atom coverage vs KB coverage) | 改 "06 P7 字段验证 atom coverage 99.02%" |

## CONDITIONAL_PASS 条件

### 必修 (HIGH, 用户 ack PLAN 前必须修)

1. **F-1**: PLAN §9 加 "PASS 四条 → 本旁枝加规则 A 为第 5 条" 说明
2. **F-2**: chunker_feasibility 修 4 处事实错误, PLAN §3 / §6.5 同步, 加 "Phase 1A.0 re-grep verify" 安全网
3. **F-3**: PLAN §8 风险表加 R-13~R-17, 或 §13 Next Actions 加 "Phase 1A.0 sanity re-grep"

### 强烈建议 (MED, 用户 ack 前最好修)

4. F-6: V4-Pro Reasoner 改非思考
5. F-7: Haiku context window 验证 risk
6. F-9 / F-10 / F-11: embedding rate limit + Chroma backup + .env 管理
7. F-14: KB → RAG reingest trigger
8. F-19 / F-20 / F-21: 工期调整
9. F-23 / F-24: PASS 五条 + 规则 A 抽检 N 明示
10. F-27: 1C reviewer.py 规则 A

### Nice-to-have (LOW / INFO, 可后补)

11. F-12 / F-13: 文件大小 + 单用户假设
12. F-15 / F-16 / F-17 / F-18 / F-25 / F-26 / F-28 / F-29 / F-30 / F-31 / F-32: 文档润色

修完 F-1 / F-2 / F-3 三个 HIGH + 至少一半 MED 后, Phase 0 可发用户 ack 请求, Phase 1A 可启动。

## Reviewer 自我隔离声明

- Rule D 隔离: writer = main session, reviewer = `critic` subagent (异 type) ✅
- 0 context inheritance: 不假定 writer 任何判断正确, 全部独立 grep 重验 ✅
- 未参与 writer 阶段 ✅
- 独立 grep 验证关键事实 (lb_part4 / VARIABLE_INDEX H3 / PC H4 / supplementary 命名 / TA mermaid / spec 变量 2164 / terminology 1005 / KB 296 md / ch04 130KB) ✅

---

**审完, 等用户 ack 这份 review + 由 main session 决定哪些 HIGH/MED 修订后再发 Phase 0 closure commit**。
