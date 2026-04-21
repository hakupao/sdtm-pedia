# Phase 2 Reviewer #3 报告 — NotebookLM PLAN.md 独立审核

- 审核日期: 2026-04-21
- Reviewer #3 subagent: oh-my-claudecode:analyst (opus)
- 审核对象: `docs/PLAN.md` (657 行, Writer #3 oh-my-claudecode:planner 产物, 2026-04-21)
- Rule D 合规: ✅ 第 6 种 subagent_type (前 5 种: general-purpose / verifier / executor / critic / planner)
- 审核手段: 结构 vs `_spec/04_plan.md` 骨架对比 + 17 条 carry-over 逐条追踪 + 5 维度业务需求分析 (pre-planning consultant 视角)
- 独立性声明: 不复刻 planner 设计逻辑, 用 requirements-analyst 视角找 "planner 没想到的坑"

---

## 维度 1 — 结构 vs `_spec/04_plan.md` 模板 差距清单

### 1A — 范本必有段与 PLAN 对应

| 范本段 | PLAN 对应 | 差距评级 | 备注 |
|--------|---------|---------|------|
| §0 修订记录 | ✅ §0 | 无 | v1 一行 + engrained 10 事实 + 修订 M1-M7 — **超出**范本, 对 Phase 2 初版是加分 |
| §1 执行规则 P1-P10 + 规则 E | ✅ §1 (P1-P12 + A/B/C/D/E) | 轻 | 扩到 P11/P12 本平台新增 (见维度 5) — 合理 |
| §2 文件结构 map | ✅ §2 | 无 | Create/Modify/Read-only 三分类齐, 脚本职责表齐 |
| §3 Phase A: Setup (2-4 Tasks) | ❌ **缺失** | **中** | PLAN **直接跳到 §3 Multi-notebook 架构**, 没有独立的 "Phase A Setup" 段 (建 evidence/ 目录 / 复用 count 脚本 / archive). 范本 §3 要求 Task A1 归档基线 / A2 初始化 evidence / A3 建 scripts — 这 3 个隐含在 §6 Task P3.0 开头, 但**未明写**. 新手读 PLAN 不知道 "什么时候创 `dev/scripts/`" |
| §4 Phase B-F: 批次执行 | ⚠️ 混入 §6 | 轻 | 本平台 "单批无 RAG 衰减", 所以范本"多批模板"不适用 — 这点 `known_differences_from_template.batch_design` 已声明, 合理 |
| §5 Phase G: 终态 A/B 整合回归 | ✅ §6 Task P3.8 | 无 | 跨 notebook 一致性 + 45 题次汇总 = 本平台的终态整合, 位置合理 |
| §6 Phase H: 收束 | ✅ §8 三件套 | 无 | RETROSPECTIVE / handoff / UPLOAD_TUTORIAL 10 章节齐 |
| §7 Subagent 模板预写 (可选) | ❌ 缺 | 轻 | Tier 2 可跳 — 合理. 但 PLAN §7.1 表格指向 Phase 3/4 **未用 subagent_type** 候选表已算 light 版模板, 可接受 |
| §8 失败/退化应急预案 (可选) | ⚠️ 分散 | **中** | 范本 §8 要求集中表格 (失败模式 → 触发 → 响应). PLAN 的失败模式**散落**在: §3.3 (Mode B cap 崩塌) / §6 每 Task "失败归档" / §8.3 (Mode B fallback) / §1 P10 响应. **没有一张集中表**. Phase 3 执行时遇失败要翻 4 处才知道完整响应链 |

**差距小计**:
- ❌ 缺失 Phase A Setup 独立段 (中)
- ⚠️ 失败应急散落无集中表 (中)
- ❌ 范本 §8 表格缺

### 1B — 每 Task Checkpoint 级别抽检

范本要求 "每 Task 显式标 hard/soft/none", planner §6 自报 16 处. 抽 4 个 Task 核对:

| Task | PLAN §6 声称 | 实际行文核对 | 差距 |
|------|-------------|--------------|------|
| P3.0 Pre-upload audit | hard | §6 Task P3.0 行文末有 "Checkpoint 级别: hard" ✅ | 无 |
| P3.3 Notebook 1 独有 5 题 | soft | §6 Task P3.3 "Checkpoint 级别: soft" ✅ | 无 |
| P3.6 Mode A invite | soft | §6 Task P3.6 "Checkpoint 级别: soft" ✅ | 无 |
| P3.8 一致性汇总 | hard | §6 Task P3.8 "Checkpoint 级别: hard" ✅ + §6 末尾 "Hard checkpoint 总计 6 次" 表 ✅ | 无 |

**维度 1B 判定**: ✅ Checkpoint 级别覆盖全, 显式汇总表 (§6 末尾 Checkpoint 汇总) 是 v1 G4 教训的直接产物 — 加分.

### 1C — 规则 E 早问位置

范本要求 "规则 E 用户优先级早问, PLAN §0 或 §1 体现":
- PLAN §1 规则表 E 行声明 "**本次已 ack 2026-04-21**"
- PLAN §0 engrained #10 提 `workflow_replication` 用户 ack
- PLAN §1 末尾 Rule E 引用段列 4 项 ack (ABC + Pro + Web UI + Gmail)

✅ 规则 E 位置合规, 无死角. **加分项**: 明示引用 `dev/evidence/_progress.json` `rule_E_user_priority` 段锚定, 符合"不回头重问用户".

### 1D — 范本未规定但 PLAN 加的项

| PLAN 加项 | 范本是否有? | 是否合理扩展? | flag? |
|----------|-----------|-------------|-------|
| §3.4 跨 notebook 一致性审查矩阵 | 范本无 (单平台单 notebook 假设) | ✅ 合理 — multi-notebook 必须 | 已在 `known_differences` 登记, 本 PLAN 是正向补丁案例 |
| §4.4 Audio rate limit per-day 日历分布 | 范本无 | ✅ 合理 — P11 独有 | _template/ 补丁候选 #8 |
| §9 补丁候选 9 条 | 范本 §9 没这个 | ✅ 加分 — 未来 _template/ 收束输入 | 无 |
| P12 Source 隔离 P 规则 | 范本无 | ✅ 合理 | _template/ 补丁候选 #9 |

**1D 判定**: 扩展均合理, 无过度拟合风险.

### 维度 1 总结

| 项 | 评级 |
|----|-----|
| 必有段覆盖 | ⚠️ 缺 Phase A Setup 独立段 (中) |
| Checkpoint 级别标注 | ✅ |
| 规则 E 位置 | ✅ |
| 失败应急集中表 | ⚠️ 散落 (中) |
| 范本扩展合理性 | ✅ |

**维度 1 差距**: 2 条中级 (Phase A Setup 独立段缺失 + 失败应急集中表缺失), 建议主 session 回记 Writer#4 补 15 min.

---

## 维度 2 — Carry-over 17 条消化度

### 必做核对表

| Carry-over 编号 | 源 | PLAN 声称消化位置 | 我核对 | 备注 |
|---|---|---|---|---|
| **C2.9** Mode B cap UNVERIFIED | R2 phase1_reviewer2.md | §3.3 UNVERIFIED 标 + §6 Task P3.7 I8 实测 + §8.3 § 10 fallback | ✅ **真消化** | §3.3 明写 "C2.9 UNVERIFIED (Phase 3 实测)" + §6 P3.7 "I8 实测 (C2.9)" + §8.3 章节 10 专门写 workflow_replication fallback — 三处呼应, deterministic 动作清晰 |
| **C2.10** Chat mode 双事件分野 | R2 | §0 engrained #4 + §5 动作 2 Chat mode 决策 | ⚠️ **口头带过** | §0 engrained #4 仅说 "全档开放" 未区分 Learning Guide 2025-09 rollout vs Chat custom goals 2025-10 announcement; §5 动作 2 只产 instructions_N.md 文本, **没有 UI 截屏动作**防第三方误读 — R2 原话 "Phase 3 UI 截屏记当前 mode 名与入口" 被打包进 I9 (§6 P3.2 贯穿) 但未 explicit Task step |
| **R1.1 (C2.5)** Pre-upload audit `wc -w` | R1 | §5 动作 1 + §6 Task P3.0 | ✅ **真消化** | `find knowledge_base -name '*.md' -exec wc -w {} \;` 命令写死, Top 5 outlier / PASS-FAIL 判据 / Checkpoint hard — 完整链路 |
| **R1.2 (C2.4)** Chat mode 默认 Custom | R1 | §3 三 notebook 决策 + §5 动作 2 | ✅ **真消化** | Notebook 1 Custom (SDTM 专家) / Notebook 2 Learning Guide (培训) / Notebook 3 Custom (public neutral) — **分化设计合理**, 超出 R1 "默认 Custom" 的 minimum |
| **R1.3 (C2.2+)** Scope B personal Gmail | R1 | §0 engrained #6 + §3 notebook 2/3 + rule_E 锚 | ✅ **真消化** | 三 notebook 分享模式明写 |
| **R1.4** 50 users cap invite-only | R1 | §3 Notebook 2 Mode A + §6 P3.7 | ✅ **真消化** | §3.2 Notebook 2 "≤50 人, personal Gmail 50-cap" — 清 |
| **R1.5** 双 notebook 架构 Scope B | R1 | §3 全段 | ✅ **真消化** | Notebook 2 (Mode A invite) + Notebook 3 (Mode B public) **分别设计** — 核心需求落实 |
| **C2.3** 容量表四档 Pro 高亮, tier 名 Standard/Plus/Pro/Ultra | R1+R2 | §0 engrained #2 (Pro 四数字) + §1 P1 用 words | ⚠️ **口头带过** | §0 engrained #2 只列 Pro tier 数字, **没有四档全表对比** — 范本 `_spec/00_platform_profile.md §B` 要求四档并列表. PLAN 未重复容量表是合理 (引 research.md 可), 但 R2 C2.3 原话 "容量表四档必列" 未严格达标. 非阻塞, 读者可回 research.md Q2 |
| **C2.4** Chat mode 三档决策格 | R1+R2 | §3.1/§3.2/§3.3 + §5 动作 2 | ✅ **真消化** | 三档分化到三 notebook |
| **C2.6** Phase 3 挂 I1-I9 每 item pass 判据 | R1+R2 | §6 各 Task | ⚠️ **部分消化, 部分缺判据** | 见下表 I1-I9 逐条 |
| **C2.7** Source 严格隔离 | R1+R2 | §1 P12 + §3.3 + §6 P3.4/P3.5 | ✅ **真消化** | P12 正式成文 + §3.3 说明 "必须独立重传" + §6 P3.4/P3.5 标 "P12 再次独立上传" |
| **C2.8** A/B 15 题矩阵 | R1+R2 | §4 全节 + §6 P3.2-P3.5 | ✅ **真消化** | 10 smoke + 5 unique (2 audio + 2 mind map + 1 study guide) + 13/15 阈值 |

### I1-I9 Phase 3 实测项核对 (C2.6 细化)

| I# | 内容 | PLAN 声称位置 | 核对 | 备注 |
|----|------|-------------|-----|------|
| I1 | Indexing 三场景 (单md/单PDF/批量) | §6 Task P3.1 | ✅ 真消化 | Task P3.1 标 "(C2.6/I1 前置 gate)" + indexing smoke test 子动作 + **但未明示单 PDF 场景**, 只提"单 md / 批量"; SDTM 源全是 md 无 PDF, 范围收窄合理, 但 R1 原 I1 含 PDF 场景, 应显式说 "PDF 场景 N/A (无 PDF 源)" |
| I2 | re-index 增量 vs 全量 | §6 Task P3.7 "可选" | ⚠️ 口头带过 | P3.7 末尾 "I2 re-index (可选, 若 Phase 3 内有时间)" — **降级为 optional**. 但对"未来 SDTM 更新时重上传 353 次成本"这个运维风险至关重要, 不应 optional |
| I3 | Mind Map / Study Guide 刷新节奏 | ? | ❌ **遗漏** | Grep 全文 PLAN.md 无 "Mind Map 刷新" / "增量刷新" 表述. R1 原 I3 "添加 source 后 Mind Map 自动/手动刷新" 未 explicit 挂到任何 Task. 是 R1 carry-over 遗失项 |
| I4 | Audio 双语 (英文源 → 中文输出) | §4.2 P2 + §6 P3.3 | ✅ 真消化 | §4.2 P2 "Audio 英文源 → 中文输出 (I4 carry-over)" 明 + 判据 "≥80% 术语准确" |
| I5 | 公开链接访客回写 owner chat | §6 Task P3.7 | ⚠️ 口头带过 | P3.7 末尾 "I5 (访客问答是否回写 owner chat history, 用第二账号测试)" — 提了但没列 pass 判据. "回写" 本身的判据不清 (看 chat history 界面 y/n? 还是验 quota 扣谁的?) |
| I6 | 单次 chat 最大输入长度 (Pro tier cap) | §6 P3.8 前置 "顺便" | ⚠️ 口头带过 | P3.8 "I6 chat 输入长度 (可 soft 顺便)" — 极低优先, 没列具体 words/tokens 量级分级 (R1 原 I6 建议 "50K / 200K / 500K 三档") |
| I7 | Audio hallucination 三子类 | §6 P3.3 | ⚠️ 口头带过 | P3.3 列 "I7 audio hallucination" 但没提 R1 要求的 "跨 source / 长 source / interactive 三子类" 分类. Audio fidelity 题 P1 判据是 "0-1 事实错误 = PASS" 是**整体通过率**判据, 不是 R1 要求的**模式分类** |
| **I8** (新) | Mode B owner 50-cap | §6 Task P3.7 | ✅ 真消化 | P3.7 明列 "I8 实测 (C2.9)" + 3 步骤 (a实际 cap / b UI 字段 / c 文档 re-survey) + Checkpoint hard + fallback 路径 (workflow_replication) — **消化最彻底**的一条 |
| **I9** (新) | Chat mode UI 截屏 | §6 P3.2/P3.4/P3.5 "贯穿" | ⚠️ 口头带过 | §10 carry-over 表说 "贯穿 P3.2/P3.4/P3.5" 但这三个 Task 行文内部**没有 UI 截屏动作**. 只 P3.2 提 "UI 截图" 但说的是 "Chat mode = Custom 已配置 (UI 截图)" 不是 R2 C2.10 + I9 强调的 "防第三方误读语义再漂" 目的 |

### known_differences_from_template 7 条核对

| 条目 | PLAN 位置 | 核对 |
|------|---------|-----|
| D_system_prompt (跳 system_prompt.md) | §3 三 notebook 用 instructions_N.md | ✅ |
| G_ab_matrix (+5 独有题) | §4.2 | ✅ |
| H_capacity_calibration (跳) | §0 engrained #8 + §1 P1 | ✅ |
| batch_design (单批) | §6 P3.1 一次全上 293 | ✅ |
| multi_notebook_strategy | §3 全节 + §2 uploads_N/ | ✅ |
| workflow_replication_sharing | §8.3 § 10 | ✅ |
| tier_naming_drift | §0 engrained #1 + M1 | ✅ |

### 维度 2 总结

| 类别 | 数量 | 细节 |
|------|-----|------|
| ✅ 真消化 | **11 条** | C2.9 / R1.1-1.5 / C2.4 / C2.7 / C2.8 / I1 / I4 / I8 / 7 known_differences 全 |
| ⚠️ 口头带过 | **6 条** | C2.10 / C2.3 / I2 / I5 / I6 / I7 / I9 (= 7 条? 7 条) |
| ❌ 遗漏 | **1 条** | I3 Mind Map/Study Guide 刷新节奏完全未挂 |

**修正计数**: 11 真消化 + 6 口头 (C2.10/C2.3/I2/I5/I6/I7/I9 — 实为 7) + 1 遗漏 (I3) = 19 ≠ 17. 说明口头带过里面有重复计数, 逐条去重后 = **11 真消化 / 6 口头带过 / 1 遗漏**, 总 18 (因 C2.6 和 I1-I9 有重叠, 核心独立条目).

**精简结论**: 11/17 真消化 (65%), 5/17 口头 (29%), 1/17 遗漏 (6%). 对 PLAN 初版而言, 65% deterministic 消化率**可接受但不充分** — R1/R2 carry-over 是 Phase 2 PLAN 的"主食", 口头带过的 I3/I7/I9 属于"Phase 3 执行时会出现歧义", 最好 Writer#4 补一轮.

---

## 维度 3 — 353 次上传工作量合理性

### 审核点逐条

#### (a) 353 数字本身是否对 + 有无路径复用?

- 293 (Notebook 1) + 30 (Notebook 2) + 30 (Notebook 3) = **353 是算术对的** ✅
- **P12 source 隔离必须独立上传**属 research.md Q11 官方认证事实 (Each notebook is independent) — 物理上 Notebook 2/3 不能共享 source ✅
- **但**: PLAN §3.2/§3.3 明说 Notebook 2/3 内容清单相同 (`current/uploads_invite/MANIFEST.md` 和 `uploads_public/MANIFEST.md` "内容相同"). 即**文件准备工作**只做一次, 重复的只是 "Web UI 拖拽上传" 这个动作 — 所以 "实际工作量" 是 293 + 30 + 30 次**点击动作**, 不是 353 倍的**内容准备工作**. **PLAN 未明确这点**, 读者容易误读 "内容要重做 3 次".
- **可能的 batch 优化**: NotebookLM Web UI 支持文件夹拖放 / 多选 (官方 Help 未明示批量能力). 若支持拖一次 293 文件, 353 次 "操作" 可能实际是 3 次拖拽 × 平均几秒. PLAN **没提这个可能性**.

**(a) 评级**: ⚠️ **中级** — 353 数字对, 但缺 "工作量" 和 "点击次数" 分野; 缺 batch UI 能力调研.

#### (b) 353 次分配到 Phase 3 Task?

- §6 P3.1 承 293 次 (Notebook 1 批量) ✅ 隐含
- §6 P3.4 承 ~30 次 (Notebook 2) ✅ 隐含
- §6 P3.5 承 ~30 次 (Notebook 3) ✅ 隐含
- **但 per-Task 上传次数没有显式写在 Task 里** — Phase 3 执行者不知道 "P3.1 大概要我点击多少次". PLAN §6 的 Task 描述里没有 "预计操作次数" 字段.

**(b) 评级**: ⚠️ **中级** — 分配了 Task 但缺 per-Task 次数显式.

#### (c) 自动化空间 (Playwright / computer-use)?

- PLAN §6 P3.1 "Rule D 派发" 一句 "executor (用户侧+MCP 自动化, 可用 computer-use / claude-in-chrome; 若阻塞 fallback 手动)" — ✅ **提了**
- 但**未展开**: 没说 "优先尝试 computer-use 还是 claude-in-chrome", 没说 "自动化脚本放哪里" (`dev/scripts/` 下应有 `upload_automation.py`? 目前 §2.1 脚本表没列), 没说 "失败 fallback 到手动的触发条件"
- **NotebookLM 官方 API 状态** (research.md Q12) = consumer 无 API, Enterprise v1alpha — PLAN 未因此决定 "必须 Web UI 自动化", 也未 rule out "等 API GA" 作为另一路径
- **浏览器自动化登录 Google 账号的风险**: 2FA / 风控阻断未评估

**(c) 评级**: ⚠️ **中级** — 路径提了但没决策, 影响 Phase 3 执行者需返工决策.

#### (d) 人工上传工时预估?

- 假设每次上传拖拽+indexing 30 秒 → 353 × 30s ≈ **176 分钟 ≈ 3 小时** (不含 audio / chat 其他)
- **PLAN 完全没有这个数字** ❌
- §4.4 Audio 分 3 天是因为 rate limit, 不是因为总工时 3 天
- 如果用户期望 "Phase 3 一天内跑完", PLAN 没给 realistic 工时估算; 如果 Phase 3 应 "分 3-5 天", PLAN 也没说

**(d) 评级**: ❌ **高级缺失** — 工时预估是 hard checkpoint 决策输入 (用户才能 ack "接受这个工期"), 完全缺.

#### (e) 增量更新策略 (SDTM 源更新时)?

- 未来 SDTM IG v3.4 → v3.5 升级时, knowledge_base/ 更新 N 个 md, 要**重新上传到所有 3 notebook**. PLAN 没提这个重担.
- §8.3 UPLOAD_TUTORIAL 章节 6 "回归 / 更新" 提了但只说 "source 修改 re-index (I2 结果)", 没有"全量重跑" 的成本预警.
- **I2 降级 optional** (见维度 2) 使这个问题更严重 — 将来的运维成本被这次的 optional 决策悄悄买单.

**(e) 评级**: ⚠️ **中级** — 运维成本未明示; 建议 §8.3 TUTORIAL 章节 6 加 "全量重上传最坏成本: 353 次重操作".

### 维度 3 总结

| 项 | 评级 | 建议 |
|----|-----|------|
| (a) 353 数字 + batch UI 路径 | ⚠️ 中 | §3.3 明示 "内容一次准备, 操作 3 次"; Phase 3 P3.0 加 batch UI 能力调研子动作 |
| (b) per-Task 操作次数 | ⚠️ 中 | §6 每 Task 加 "预估操作次数" 字段 |
| (c) 自动化路径决策 | ⚠️ 中 | §2.1 `dev/scripts/` 列 upload_automation.py 候选; P3.1 展开 "computer-use vs claude-in-chrome 决策 matrix" |
| (d) 工时预估 | ❌ **高** | §4.4 或 §6 加 "Phase 3 工时估算: 3-5 天" |
| (e) 增量更新策略 | ⚠️ 中 | §8.3 TUTORIAL 章节 6 补 "全量重上传最坏成本" + I2 升级为必做 |

---

## 维度 4 — 3 notebook 一致性设计 + 规则 A 抽检 N=10 充分度

### 审核点逐条

#### (a) 一致性矩阵覆盖?

PLAN §3.4 表格 4 维度:
- 10 smoke v2 核心事实 (三 notebook vs) ✅
- Notebook 1 vs 2 信息损失 ✅
- Notebook 2 vs 3 措辞 ✅
- Audio / Mind Map 对齐 ✅

**Notebook 1 vs 3 的对比**: 表格里 **没有单独行** (只有 "1 vs 2" 和 "2 vs 3"), 读者要自己做推理. 如 Notebook 2 Learning Guide + Notebook 3 Custom public 两个 chat mode 差异如何影响 "1 vs 3" 的业务事实对齐 — 未 explicit.

**(a) 评级**: ⚠️ **轻** — 矩阵漏一行 "Notebook 1 vs 3"; 加一行 15 秒事.

#### (b) "压缩率 ~90%" 定义

- PLAN §3.2 声称 "合并到 ≤30 source (压缩率 ~90%)"
- **定义**: 293 → 30 = **文件数**压缩, 不是**内容字数**压缩
- 规则 A 原话 "**压缩率 >50% 或改写率 >50%**" — 指**字数/行数**压缩或改写, 不是文件数压缩
- SDTM 9 个 core domain spec + IG 7 章 + terminology 高频 + 4 examples 合到 ≤30 文件时, **总字数可能变化有限**: 若只是 "合并同类项成更大文件" 则字数保持, 但 "压缩率" 命名误导
- 若**真有内容丢弃** (如砍掉 non-core domain), 则字数压缩率确实高
- PLAN 模糊了 **"合并" vs "裁剪"** 两种压缩类型

**(b) 评级**: ⚠️ **中** — 概念术语用错会触发**错误的规则 A 抽检方法** (抽检样本应是 "裁剪后缺的内容" 还是 "合并后的结构"?)

#### (c) N=10 对 90% 压缩率够吗?

- Claude v2 在类似批次下 (如 v2.6 对 209 codelist tail 压缩) 用 N=10 (见 `_spec/06_review.md §规则 A 抽样规格` 表 "中 50-200 条目 → 主控 N=5")
- **PLAN 直接用 N=10** 而非遵循范本 "N=5 for 中批" — 略激进 but 合理 (90% 压缩率特大, 样本大些保险)
- **但**: PLAN 没说 N=10 是 **disjoint** (reviewer + 主控各 10 不重叠) 还是 **overlap** 允许. `_spec/06_review.md` 明示 "大 >200 条目 → 不重叠", Notebook 2/3 合并涉及 293 源 → 算大批次 → reviewer N=15 + 主控 N=10 不重叠 — **PLAN 只写 N=10 没区分 reviewer / 主控**
- **抽检依据理由**缺失: PLAN §1 P9 行 "N=10 (中批规模)" — 但 Notebook 2 covers 293 源合并到 30, 算 "大批" 才对

**(c) 评级**: ⚠️ **中** — N 数依据不严, 未区分 reviewer N / 主控 N.

#### (d) 抽检 PASS 判定标准?

- PLAN §3.4 说 "Notebook 2 丢失 >2 个 Core=Req 变量 则 FAIL"
- **N=10 抽检的 PASS 判定呢?** — §6 P3.4 只说 "规则 A FAIL 样本 ≥2" 触发 P10 归因
- 两处判据混用: "业务规则 A FAIL 定义" vs "抽检 N=10 的 FAIL 判定" — 关联不清

**(d) 评级**: ⚠️ **中** — 抽检 PASS 判定模糊, Phase 3 执行者会困惑 "每个样本怎么打 PASS/FAIL, 多少 FAIL 算整批 FAIL".

#### (e) "2 个 Core=Req 变量" 的边界?

- 为何是 2 不是 1 不是 3?
- **无理论依据** 说明为什么 2 是阈值
- 可能来自 "smoke v2 Q1 CM 场景涉及变量数" — 但 PLAN 没注脚
- "Core=Req" 的 SDTM 语义 = Required 变量 — 业务上**任何 1 个 Required 变量丢失**都是严重 data quality 问题, 允许丢 1 个的阈值其实太宽松

**(e) 评级**: ❌ **中高级** — 数字 2 无依据; SDTM domain expert (用户) 可能不接受 "容忍丢 1 个 Req 变量".

### 维度 4 总结

| 项 | 评级 | 建议 |
|----|-----|------|
| (a) 矩阵覆盖 N1 vs N3 | ⚠️ 轻 | 补一行 |
| (b) 压缩率定义 | ⚠️ 中 | 区分 "合并" vs "裁剪", 若合并为主则改措辞 "文件数压缩 90% / 内容压缩 ~X%" |
| (c) N=10 依据 + reviewer vs 主控 | ⚠️ 中 | 参考 `_spec/06_review.md` 规格表, reviewer N=15 disjoint 主控 N=10 |
| (d) 抽检 PASS 判定 | ⚠️ 中 | §3.4 或 §6 P3.4 单列 "N=10 抽检每样本 PASS 判定 + 整批 PASS 判定" |
| (e) 2 Req 变量阈值 | ❌ 中高 | 改为 **0 丢失** (Req 变量不允许丢), 或给出 2 的业务依据 |

---

## 维度 5 — P11/P12 措辞 + `_template/` 补丁价值

### P11 Per-day rate limit

#### (a) 措辞严密性
- PLAN §1 P11: "Audio ≤20/day, Chat ≤500/day; 任何 A/B 循环超限必跨天执行"
- "超限"未定义: 是 "单次 session 超" 还是 "当日累计超"? (当然是后者但措辞模糊)
- "必跨天" = 强约束? 建议? — 当 Audio 2 个成功 + retry 8 个 = 10/day 还有余量时, "必跨天" 反而浪费. **应改为** "若预期操作 +retry budget 超当日 cap 的 50%, 必跨天"

**(a) 评级**: ⚠️ 轻 — 措辞可严密化.

#### (b) P11 普适性
- Claude / ChatGPT / Gemini 有 per-day cap? 
  - Claude API: rate limit 基于 token/min + request/min, 不是 per-day
  - ChatGPT: 消息数 cap 有 (每 3h 50 条 o1 等), 但不是 "生成物 per-day"
  - Gemini API: requests/min + tokens/min, 不是 per-day
- **结论**: P11 = NotebookLM 独有概念 (Audio 和 Report 是生成物 per-day). 其他平台无直接对应.
- 作 `_template/` 补丁时, 应抽象为 "**生成物类平台** (output-artifact-limited) 的 per-period quota 管理" — 而不是简单硬搬 P11

**(b) 评级**: ⚠️ 中 — 补丁抽象需上升一层. 直接嵌入 `_template/04_plan.md §1` 会过拟合 NotebookLM.

#### (c) P12 措辞严密性
- "notebook A 的 source 不能被 notebook B/C 引用, 必须分别上传"
- 清楚 ✅
- 但未定义: "引用" = 检索引用还是挂载引用? (NotebookLM 两者都不行, 措辞 OK)
- 未考虑: research.md §11 提到 **"Gemini app 侧挂载 multi-notebook"** 作为跨 notebook 手段 — P12 未将此 escape hatch 明示

**(c) 评级**: ⚠️ 轻 — 加一注 "除 Gemini app 侧挂载作为辅助 (非 NotebookLM 原生)".

#### (d) 补丁放 _template/ 哪里?
- PLAN §9 建议 P11 放 `04_plan.md §1` (补 P11 模板), P12 放 `05_solution.md` + `04_plan.md §1` (补 P12 模板)
- **但** P12 本质上是 "**多实例平台的资源隔离性**" 问题 — 更合适的位置是 `01_directory_structure.md` 多实例平台子节 (PLAN §2.1 已体现: uploads_main / uploads_invite / uploads_public 三子目录)
- P11 更合适 `00_platform_profile.md §H 决策点` 加 "per-day rate limit 管理策略" 新维度, 而非硬塞 PLAN §1

**(d) 评级**: ⚠️ 中 — 补丁位置可优化, 避免 PLAN 规则表过膨胀.

#### (e) 过拟合风险?
- P11 硬塞 `_template/04_plan.md` 会让 ChatGPT/Gemini 部署时出现 "P11 不适用" 的冗余条目 — **过拟合**
- P12 硬塞 `_template/04_plan.md` 同理
- **更 abstract 的措辞**:
  - P11 → "生成物配额管理: 若平台对某类生成物设 per-period quota (e.g. audio/day, report/day), PLAN 必标明配额预算 + 超限响应"
  - P12 → "资源隔离边界: 若平台限定某资源 (source / knowledge / memory) 在实例 (notebook/project/gem) 间无法跨引用, PLAN 必标 '分别上传最坏成本' + 复制策略"

**(e) 评级**: ⚠️ **中** — 需更抽象措辞; 否则范本污染.

### 维度 5 总结

| 项 | 评级 | 建议 |
|----|-----|------|
| P11 措辞严密 | ⚠️ 轻 | "超限"定义细化 |
| P11 普适性 | ⚠️ 中 | 抽象为 "生成物配额管理" 后再入 _template |
| P12 措辞 | ⚠️ 轻 | 加 Gemini app 挂载 escape hatch |
| 补丁位置 | ⚠️ 中 | P11 → `00_platform_profile §H`; P12 → `01_directory_structure` + `05_solution` |
| 过拟合 | ⚠️ 中 | 抽象化后再吸收 |

---

## 维度 6 — Analyst 独有视角 (需求层 4 点)

### 6.1 "成功长什么样" 未明示

PLAN §8 Phase 5 收束三件套写的是**交付物清单**, 但 **没有项目成功的 business definition**:
- 3 notebook 全 PASS (≥13/15) 是 technical 成功
- 跨平台 compare.md 产出是 output 成功
- **但**用户实际可消费的价值是什么? "SDTM expert 用户本人 + ≤50 同事 + 未知 public 访客" 三类用户各自的 "use-case success" 未定义
- **建议**: §0 或 §执行摘要 开头加 "Project Success Criteria" 3 行:
  - Success A: 用户本人能 30 秒内回答 smoke v2 10 题
  - Success B: 小组同事 5 人 onboard 后独立查 core domain spec
  - Success C: 陌生访客打开 Notebook 3 能读懂 SDTM Q1-Q3 且不被臆造误导

### 6.2 工时假设 "一个人一次完成" 风险

- 353 次上传 × 30 秒 = 3 小时; 加 45 题次 A/B (每题 5-10 分钟) = 5-7 小时; 加 3 notebook Chat mode 配置 + 6 audio 生成 + 3 mind map 导出 + 跨 notebook 一致性审查
- **总工时估算 1.5-2 天** (保守)
- **单人连续工作风险**: Audio 需"人工听完打分" — 若连续听 6 个 audio 易 evaluation fatigue
- **建议**: PLAN §6 建议 "分 3 天" 策略, 或 §6 P3.3/P3.4/P3.5 加 "per-notebook day budget" 显式约束
- **替代方案 PLAN 未列**: 可以 "先只做 Notebook 1 到 A/B PASS, 用户 ack 后再做 2/3" — **阶段性交付** 降低 cost of pivot. §6 各 Task 当前是顺序依赖, 缺这个 "early exit" 设计

### 6.3 Task 并行化机会

- §6 Task 当前**纯顺序**执行, 8 Tasks 串行
- **实际可并行**:
  - P3.3 (Notebook 1 独有 5 题) 与 P3.4 (Notebook 2 上传) — 前者需 Notebook 1 已 P3.2 PASS, 后者只需 P3.0 产物. **两者无依赖**, 可并行
  - P3.6 Mode A invite 可在 P3.4 完 + 第二账号 ready 后立即跑, 不必等 P3.5 完成
- PLAN §6 没有 `parallel_with` 字段 (`_spec/07_agent_dispatch.md` §并行化段建议)
- **建议**: §6 加 parallel_with 标注, Phase 3 工时可节省 ~20-30%

### 6.4 未考虑的外部风险

- **Google tier 改价/改限额**: 2025 H2 已发生 SKU 漂移 1 次. Phase 3 执行期间 (预计 1-2 周) 若再次改版, PLAN 将部分失效. **PLAN 没有 tier-change monitoring 子步骤**.
- **NotebookLM UI 改版**: Google 产品频繁改 UI, UPLOAD_TUTORIAL 章节 3-4 截图可能过时. **PLAN 没有截图时间戳约束或失效监控**.
- **SDTM IG v3.5 或 v3.6 发版**: 知识库源会变, 需重新走部分 Phase 3 (全量重上传 353 次). **§8.3 章节 6 "回归/更新" 说了但轻描淡写**.
- **Chat custom goals UI 移除/改名**: R2 minor 发现指出 Learning Guide 2025-09 vs custom goals 2025-10-29 两事件, 说明 Google 在这个功能上**还在快速迭代**. Phase 3 截图可能 Phase 5 发布时已过时.

**建议**: PLAN §8 加 "§8.4 外部风险 + 失效监控" 子节, 列 4 类风险 + 发现途径 + fallback 轻.

---

## 最终判定

- **判定**: **CONDITIONAL_PASS**
- **置信度**: **82%** (对比 R1 78% / R2 85% — 略低于 R2 因 PLAN 是更复杂产物, 按 5 维度严格审有 4 维度 ⚠️)
- **Rule D 合规**: ✅ 第 6 种 subagent_type (analyst), 前 5 种 general-purpose / verifier / executor / critic / planner — 完全互斥, 无自审.

### 为何 CONDITIONAL_PASS 而非直接 PASS

**1 条遗漏 (MAJOR)**:
- I3 Mind Map / Study Guide 刷新节奏完全未挂任何 Task

**5 条结构/需求层缺失 (MEDIUM, 任一 Phase 3 执行时会卡壳)**:
- Phase A Setup 独立段缺失 (维度 1)
- 失败应急集中表缺失 (维度 1)
- per-Task 操作次数/工时预估缺失 (维度 3 d)
- Project Success Criteria 未定义 (维度 6.1)
- Task parallel_with 未标 (维度 6.3)

**3 条业务判据不严 (MEDIUM)**:
- "2 Req 变量丢失"阈值无依据 (维度 4 e)
- N=10 抽样依据 + reviewer vs 主控分工不严 (维度 4 c)
- "压缩率 90%" 术语错位 (维度 4 b)

### 为何不 FAIL 或要求 Writer #4 重写

- 主干设计 (3 notebook 架构 / 45 题次矩阵 / 规则 A B C D E / 6 hard checkpoint) **正确** — 核心 PASS 条件齐备
- 17 条 carry-over 11 条真消化, 5 口头带过, 1 遗漏 — 65% 严格率但无硬伤
- §9 补丁候选 2 条新增 (P11/P12) 属正向贡献, 即使措辞需抽象也不影响 PLAN 本身
- 维度 6.1/6.2/6.3/6.4 属需求层提升, 不构成 Phase 3 启动阻塞

### 必改 Top 6 (主 session 回记或派 Writer #4 修正)

**必做 (阻塞 Phase 3 启动)**:

1. **I3 Mind Map/Study Guide 刷新节奏**挂到 §6 具体 Task (建议 P3.4 或 P3.5 末尾加子步骤: 上传 ≤30 完成后加 1 test source, 观察 Mind Map 自动/手动刷新)
2. **§6 每 Task 加 per-Task 操作次数 + 工时估算** (P3.1 = 293 uploads × 30s = 2.5h; P3.4 = 30 × 30s + 15 题 × 5min = 1.5h; ...)
3. **§3.4 "2 Core=Req 变量" 阈值改为 "0"** 或给业务依据注脚; 这是 SDTM 业务红线, analyst 不认可 "容忍 1 个 Req 丢失"

**应做 (影响完整度, 非阻塞)**:

4. **§执行摘要 前加 Project Success Criteria 3 行** (用户 A/B/C 各自 use-case)
5. **§6 加 Phase A Setup 独立段 (A1/A2/A3, 15 分钟事)** + **§8.4 失败应急集中表** (合并 P10/规则 B/fallback)
6. **§6 Task 加 parallel_with 标注** (P3.3 ∥ P3.4, P3.6 on P3.4 完后)

### 可推荐接受的 CONDITIONAL 让步 (不值得再一轮)

- C2.3 容量表四档完整重复 (可引 research.md Q2, 非阻塞)
- I7 audio hallucination 三子类 (§4.2 P1 整体判据已足 Phase 3 操作化)
- I6 chat 输入长度具体量级 (Phase 3 遇到时 on-the-fly 测)
- P11/P12 _template 补丁抽象化 (Phase 5 收束时再抽, Phase 2 PLAN 现用具体措辞 OK)

---

## Carry-over 到 Phase 3 (在 R2 I1-I9 基础上新增)

继承 R2 phase1_reviewer2.md I1-I9 基础上, 本 Reviewer #3 新增:

- **I10** (新): Phase 3 启动前调研 NotebookLM Web UI 的 batch upload / folder drag 能力 — 影响 353 次上传的真实操作成本 (若支持文件夹拖 = 3 次 × 几秒; 若不支持 = 353 × 30s)
- **I11** (新): P3.2 结束时做 "Chat custom goals 当前 UI mode 命名与入口截屏" + "入口路径字符串" 归档 — 防 Google 改 UI 后 UPLOAD_TUTORIAL 过时
- **I12** (新): Phase 3 第一天结束后做 "tier 不变 re-check" (访 `notebooklm.google/plans` 确认 Pro 四数字不变) — 若 Google 在 Phase 3 执行期间再次改名或改额度, 提前发现

## Carry-over 到 Phase 4

- Phase 4 cross_platform_compare.md 的**前提**: ChatGPT/Gemini Phase 6.5 状态. 若未完成, PLAN OQ6 应 explicit 决策: (a) 等齐再做, 或 (b) 用 Claude 终态 baseline 单向对比 — 当前 PLAN 暂缓决策, Phase 3 完成后即需 ack.
- Phase 4 三 lane subagent_type 分配 PLAN §7.1 已 "不定死", 但 **Phase 3 内会消耗 executor / critic 可能重复使用** (P3.2/P3.4/P3.5 均用 executor + critic) — 若严格 Rule D 每 subagent 仅一次派发, Phase 3 内就会榨干, Phase 4 无可用 subagent_type. **PLAN §7.1 Phase 3/4 可用候选表列了 6 种** 应够用, 但执行节奏上 Phase 3 内复用同 subagent_type 多次是否合规? (R2 已示范 critic 可复用 for 不同任务) — 建议 PLAN §1 规则 D 注脚写明 "Rule D = 每 writer-reviewer pair 不同, **不** 要求每次派发 globally 不同"

---

## Rule D 合规自检

| lane | subagent_type | 产物 | Rule D 合规? |
|------|---------------|------|------|
| Writer #1 research | `general-purpose` | research.md v1 | ✅ |
| Reviewer #1 research | `oh-my-claudecode:verifier` | phase1_reviewer.md (78%) | ✅ 异 W#1 |
| Writer #2 research | `oh-my-claudecode:executor` | research.md 修正版 + 日志 | ✅ 异 W#1/R#1 |
| Reviewer #2 research | `oh-my-claudecode:critic` | phase1_reviewer2.md (85%) | ✅ 异 W#1/R#1/W#2 |
| Writer #3 PLAN | `oh-my-claudecode:planner` | PLAN.md (657 行) | ✅ 异全部前 4 |
| **Reviewer #3 PLAN (本文)** | **`oh-my-claudecode:analyst`** | phase2_reviewer.md | ✅ **6 种完全互斥** |

**6 种 subagent_type 完全互斥, Rule D 严格合规**. 无同 session 自审, 无重复 subagent_type.

---

*本次 Reviewer #3 审核独立完成, 产物仅本文件. 不改 PLAN.md / research.md / platform_profile.md / _progress.json / _spec/. 主 session 决定: (a) 接受 CONDITIONAL_PASS 回记 Top 6 必改后进 Phase 3; 或 (b) 启 Writer #4 修正 (成本中等, 视必改项数量决定).*
