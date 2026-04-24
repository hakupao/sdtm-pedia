# NotebookLM 平台 Phase 5 RETROSPECTIVE

> **Rule C 强制产物** — NotebookLM 平台独立 retro, 与 `ai_platforms/retrospectives/PHASE5_RETROSPECTIVE.md` (跨 4 平台合流版, v1.0 FINAL 2026-04-24 Daisy 认可) 呼应
> **Scope**: NotebookLM v2 架构 lifecycle (2026-04-21 起跑 pivot → 2026-04-23 Phase 4 闭合) async lane
> **Writer**: 主 session (2026-04-24), 非 subagent — 与跨 4 平台 retro 同一作者范式
> **Reviewer**: `oh-my-claudecode:critic` (NotebookLM async lane 独立 reviewer slot, 2026-04-24 完成; Rule D 合规 — critic type 在跨 4 retro #4/#28 已使用, 本次新 context/evidence 作独立 lane reviewer, 不违 "同 context 自审" 原则)
> **Status**: ✅ **v1.0 FINAL** (2026-04-24 PM, Daisy 认可) — v0.1 DRAFT → reviewer CONDITIONAL_PASS 8.0/10 → 1 HIGH + 4 MEDIUM + 3 遗漏 + 2 Open Q 全修 → v0.2 post-reviewer-fix ack-ready → Daisy 读完 ack → v1.0 FINAL sign-off. NotebookLM async lane Phase 5 retro 闭环 ✅. Reviewer 报告: `dev/evidence/phase5_retrospective_reviewer.md`

---

## §0 Phase 5 入参快照

### 0.1 NotebookLM final state

| 维度 | 值 |
|---|---|
| 架构 | **v2: 1 notebook × 42 sources** (pivot from v1 3-notebook × 293 source 架构) |
| Source 数 | 42 / 300 Pro cap (14%) |
| Total words | 1,582,085 (最大 bucket 302K < 500K/source cap, 0 over-cap / 0 missing) |
| Req 变量覆盖 | 176/176 独立 Req (∅ gap, A4 结构级 + P3.4.5 语义级双锚闭合) |
| Domain 覆盖 | 63/63 (全覆盖) |
| Chat Custom mode | instructions.md **8,925 Unicode chars** / 10,000 char limit (**10.75% headroom**); 9,011 utf-8 bytes 作 byte-level reference (reviewer HIGH #1 fix 2026-04-24) |
| smoke v4 R1 | **15/17 (88.2%) strict PASS** (6 PASS + 8 PASS+ + 2 PARTIAL + 1 safety-correct PUNT) |
| AHP × 3 | **3/3 全 PASS+ 最强** (in-KB-only 天然反虚构优势, 并列 Claude) |
| 阈值 | ≥12/17 (71%) R1 首测容错 → 实际 88.2% 远超 |

### 0.2 Lifecycle timeline (3 天 async lane)

| 日期 | 里程碑 |
|---|---|
| 2026-04-21 AM | Phase 0 scaffolding + Phase 1 研究 (v1 draft) |
| **2026-04-21 PM** | **v1 → v2 架构 pivot** (用户反问触发, 3-notebook 伪约束 CLOSED) |
| 2026-04-21 晚 | Phase A Setup (A1-A4 + A5' Web UI 小样实测) + `_progress.json` 锚定 |
| 2026-04-22 AM | P3.1 merge_sources.py → 42 uploads + P3.2 Web UI 上传 42/42 indexed |
| 2026-04-22 PM | P3.3 Custom mode + H3 VERIFIED + P3.4 indexing smoke 10/10 + P3.4.5 Q1 红线语义级 8.5/10 + P3.8 smoke v3 9/10 strict PASS + smoke v3→v4 升级决策 |
| 2026-04-22 晚 | smoke v4 R1 开跑 (sanity 3/3 + Q1-Q10) |
| 2026-04-23 凌晨 | smoke v4 R1 收尾 (Q11-Q14 + AHP1-3 全完) = 15/17 PASS |
| 2026-04-23 PM | P3.8 reviewer (12th slot) 独审 PASS + P3.9 三档切换演练 (5 PASS + 1 PARTIAL + 1 SKIP) |
| 2026-04-23 晚 | Phase 4 闭合, status → READY_FOR_PHASE_5_CROSS_PLATFORM_RETROSPECTIVE_MERGE |
| 2026-04-24 | 跨 4 平台 PHASE5_RETROSPECTIVE v1.0 FINAL (含 NotebookLM contribution) |

### 0.3 Rule D async lane 独立链 (本平台专属 slot)

跨 4 平台 retro Appendix A 列 28 slot, 其中 NotebookLM async lane **独立贡献 2 个 subagent_type instance** (slot #24, #25):
- #24 `oh-my-claudecode:document-specialist` (smoke v3→v4 audit, 11th slot cumulative)
- #25 `feature-dev:code-reviewer` reuse (P3.8 reviewer 12th slot cumulative, 与 #11 不同 context/evidence)

Plus NotebookLM Phase 2-3 独立链 cumulative 10 种 (Phase 2 v2 architect #9 + P3.4.5 scientist #10 本平台内独立, 跨 lane 复用 count 在上述 28 slot roster).

---

## §1 保留下来的做法 (R-NBL-1 to R-NBL-8)

### R-NBL-1. v2 1-notebook × ≤50 架构 + 3 档分享切换

**做法**: 舍 v1 3-notebook 职责隔离架构, 改为单 notebook + 42 bucket concept cluster + 3 档分享 (Restricted / Anyone with link / Public) UI toggle.

**为什么保留**: 三 WebFetch 官方原文核实 (2026-04-21) 推翻 v1 三假设 — (a) 50-cap 仅 Restricted invite 套, (b) Chat custom goals Custom mode UI 3 档可切, (c) viewer 自己 tier cap 不受 owner 分享档位影响. 单 notebook 比 3 notebook:
- **Req 零丢失更易守** (集中审计 vs 3 处分散审计)
- **分享档位按场景切, 无多 notebook 同步维护负担**
- **indexing silent fail 风险降低** (42 source 比 293 source 单文件追踪更可行)
- **citation 信噪比更高** (bucket 概念聚合减少碎片)

**支持证据**: P3.2 42/42 indexed 0 silent fail; P3.4 indexing smoke 10/10 顶阈值 PASS; P3.9 (e) 快速多次 Restricted↔Public 切换无 caching 残留.

### R-NBL-2. 42 bucket concept cluster 策略 (63/63 + 176/176 ∅ gap)

**做法**: 293 md → 42 bucket concept cluster via `merge_sources.py`, 按 concept 聚合 (如 "events_ae", "findings_lb_quantitative", "trial_design_ta_te_tv"), 而非按 domain 或字母排序切.

**为什么保留**: 
- **Q1 红线双锚闭合** — A4 结构级 ∅ gap audit (PASS) + P3.4.5 语义级 Q1 变量业务问答 CONDITIONAL_PASS 8.5/10 (语义 10/10 顶阈值)
- **8 slot headroom** (42/50) — 未来若 KB 扩展有扩容空间, 不需重切
- **每 bucket metadata header 便于 citation 反查** — source 合成时顶部加 "NotebookLM source metadata header"

**对其他平台的启示**: ChatGPT/Gemini 20-file / 10-file 硬限下无法用 42-bucket 这种密度, 但"concept cluster 优先于 domain/字母切"的**排布原则**通用.

### R-NBL-3. Chat Custom mode 8,925 Unicode chars instructions.md (10.75% headroom)

**做法**: 占用 Custom mode 10K char limit 的 **8,925 Unicode chars** (9,011 utf-8 bytes), 13 behavior rules + SDTM 锚点 (AESER=Exp / LBNRIND 全写 / NY C66742 / ISO 8601 / C-code 字面 / Day 1 无 Day 0 / RELREC+RELSPEC+RELSUB 三件套 / SUPP-- 结构) + authoritative layer 优先级 (spec > ch04 > CT > assumptions > examples).

**为什么保留**: Chat Custom mode 是 NotebookLM 唯一可 prompt engineer 的入口 (无 System Instructions). 实际用量 **8,925/10,000 = 89.25%, headroom 10.75%** (reviewer HIGH #1 fix 2026-04-24: 原 v0.1 DRAFT "9,011 chars 11% headroom" 误把 utf-8 bytes 当 Unicode chars; NotebookLM 10K limit 通常按 Unicode char 判, byte-level 9,011 作 reference 保留) 留给未来微调, 但 13 rules 已足够锚住常见幻觉陷阱. P3.3 chat_mode_toggle_test.md 3 组问答 controlled comparison 证明 Custom mode 产生与 Learning Guide 差异化输出 (结构化 vs 教学化), Custom mode 生效.

### R-NBL-4. Phase A + P3.4.5 结构+语义双锚 Q1 红线自证

**做法**: Q1 红线 (0 Req variable loss) 用两层防线自证:
- **结构级**: Phase A A4 `req_vars_coverage_audit.md` — 176/176 独立 Req ∅ gap
- **语义级**: P3.4.5 Q1 红线业务问答 N=10 — 主 session 从 `req_vars_full_set.md` 独立随机抽 10 个 Req 变量构造业务问答, 看 NotebookLM:
  - 是否命中正确 Req 变量 (10/10 必 PASS)
  - citation 是否精确回指 (9/10 PASS 接受)

**为什么保留**: 结构级审计只能证"bucket 里有这个变量名", 不能证"NotebookLM 能召回 + 业务语义理解". 语义级业务问答是 Rule A 严格正本 (用户规则 A "压缩 >50% 必 N 样本独立抽检", 293→42 压缩率 86% 触发). **双锚都不能缺** — P3.4.5 实际结果是 "语义 10/10 顶阈值 + citation 7/10" → CONDITIONAL_PASS 8.5/10, 证明 RAG 召回本身 PASS, citation 精度是次阶段改进空间 (不影响 Q1 红线).

### R-NBL-5. P3.8 smoke v3 9/10 PASS + 主 session 独立复判驱动 v3→v4 升级

**做法**: P3.8 题库 smoke v3 Q1-Q10 (对齐 ChatGPT+Gemini N5.3) 跨 4 平台对比基线, cowork Chrome MCP 代跑 sanity 3/3 + Q1-Q10 9/10 strict PASS. 跑完主 session **独立复判** 暴露 v3.1 Q10 (b) 判据基于错前提 — SUPPTS 在 SDTMIG v3.4 不存在 (TS 属 Trial Design 用 TSVAL1-n 派生), NotebookLM answer Sub-message 3 主动纠错 "SUPPTS 实际在标准中是不存在/不合法的" + 给 TSVAL1-TSVALn 替代方案.

**为什么保留**: "Writer PASS + Reviewer PASS ≠ 业务 PASS" (Rule A 教训) 在此被实证 — cowork writer 自打 9/10 过了 strict PASS 阈值, **但主 session 独立复判才抓出判据 bug**. 这驱动 smoke v3 → v4 升级决策 (加 AHP × 3 测 "给错前提能否纠错" 维度), 是用户 meta insight "常问错前提希望纠错非幻觉" 的直接证据.

**对 Rule A 的深化**: "独立抽检" 不只是重新跑题, 而是**独立对照原始 KB / SDTMIG 原文核实判据本身**. P3.8 reviewer (12th slot) 进一步指出 main session 实际只审 3/10 (30%) 在边缘, 建议 Phase 5 retro 补 "P3.8 Rule A 独立抽检 N 应 ≥ 5 (50%) 或全覆盖" — 见 G-NBL-2.

### R-NBL-6. smoke v4 AHP × 3 全 PASS+ 最强 (in-KB-only 天然反虚构优势)

**做法**: AHP1 (变量虚构 LBCLINSIG, 实际 LBCLSIG) + AHP2 (跨域虚构 Trial-Level SAE Aggregate 表) + AHP3 (deprecated 虚构 PF 域被 GF 替代) — NotebookLM 3/3 全 **PASS+ 最强** (并列 Claude, 超 ChatGPT AHP PARTIAL + 超 Gemini R2 AHP 3/3 PASS).

**为什么保留**: 
- **AHP1**: 开篇第一句直接 premise correction "正确变量名是 LBCLSIG, 而不是 LBCLINSIG" + 引用 SDTMIG 原文 "LBNRIND is not used to indicate clinical significance"
- **AHP2**: 开篇 "未收录 / outside the knowledge base" + 明确 "SDTM 仅 subject-level tabulation, aggregate 应在 ADaM" 分层 + 主动反问引导澄清
- **AHP3**: 开篇 "PF 已被废弃, 被 GF 完全取代" + 未收录 + GF 6 Req 完整 + GFSYM + HGNC (HUGO Gene Nomenclature) 数据库独到

**为什么这是天然优势**: NotebookLM source-grounded only 架构强约束 "边界诚实", 模型被逼只能从 sources 回答, 不能脑补训练数据. 其他 3 平台 (Claude/ChatGPT/Gemini) 能访问训练数据或 web, 反而要 prompt anti-hallucination 锚 (CO-5 章) 才能抗幻觉. 这是**架构级优势非 prompt 优势**.

### R-NBL-7. Rule D async lane 独立链

**做法**: NotebookLM async lane 不参与 ChatGPT+Gemini SYNC_BOARD 锁步, 独立派 subagent_type 作 reviewer. Phase 3-4 贡献 2 个 slot 到跨 4 平台 28-slot roster:
- #24 `oh-my-claudecode:document-specialist` (smoke v3 audit)
- #25 `feature-dev:code-reviewer` reuse (P3.8 reviewer)

Plus 本平台 Phase 2-3 内独立:
- #9 `oh-my-claudecode:architect` (Phase 2 v2 reviewer, CONDITIONAL_PASS 84%)
- #10 `oh-my-claudecode:scientist` (P3.4.5 reviewer, Q1 红线双锚闭合)

**为什么保留**: async lane 的好处是**不受锁步节奏拖**, 主工 Phase 3 上传 + smoke 连续跑满 42 小时, 不需要等 ChatGPT/Gemini gate 同步. 代价是**不能 cross-pollinate** — 但 smoke v4 统一题库解决了 cross-check 问题.

### R-NBL-8. P3.9 三档切换演练 (6 子步 + H3 VERIFIED + Public ≠ gallery 新发现)

**做法**: P3.9 三档切换演练 6 子步骤 (a-f):
- (a) Restricted 默认 ✅ PASS
- (b) Anyone with link + 2 账号测 ✅ 3/3 PASS
- (c) Public + 公开画廊搜 🟡 PARTIAL (**新发现**: Public ≠ auto gallery 广播, 画廊是 curated Featured list)
- (d) 回切 Restricted + 旧链接失效 ✅ PASS (revoke 生效)
- (e) L3 fix 快速多切 ✅ PASS (无 caching 残留)
- (f) Free tier 50-cap 实测 ⚪ SKIP (42 sources ≤50 未触发 cap, 客观无法测)

**为什么保留**: (c) 新发现**修正 v1 时期"Public=广播"假设** — NotebookLM Public 档语义是"允许任何持链接者无需登录访问", **不等同于** "上 public gallery 被动曝光". 画廊是策展 (curated Featured) 非 auto-listed. 这**比 ChatGPT GPT Store "Public=全网广播" 保守, 隐私友好性更高**, 适合小圈内部分享 + 定向外发场景. H3 hypothesis 归档状态: **VERIFIED + 深化**.

---

## §2 必须补上的缺口 (G-NBL-1 to G-NBL-6)

### G-NBL-1. v1 3-notebook 伪约束未被 8 种 subagent_type 的 Rule D 链拦截

**问题**: v1 PLAN 基于 Q7 "Mode A/B 两独立" 叙事派生 "3 notebook 职责隔离" 伪方案, 被 8 种 subagent_type (Rule D slot #1-8) **全部继承**, 无一回 WebFetch 官方原文核对. 用户反问"为什么 3 notebook 不 1 notebook + 分享档位?"才是 pivot 触发点.

**影响**: 1 天 PLAN 写作 sunk cost; 若 Phase 3 开始上传才发现伪约束, 代价更大.

**根因 3 层 (PLAN §11 归因深化)**:
- **层 1 (Writer 叙事范式锁定)**: v1 Q7 叙事是 research 阶段基于官方文档片面理解, Writer 一次 WebFetch 不够深. 这是**范式锁定**问题, 与 subagent_type 多样性无关.
- **层 2 (跨 Phase 回溯盲)**: Reviewer 审查焦点由前 Phase 提供 spec 决定, **不会倒回去质疑 research 源头叙事**. v1 Phase 2 reviewer 只审 planner 推论, 不质疑 research 是否基于完整官方原文.
- **层 3 (用户反问作最后防线)**: 用户 review 是**外部触发**, 不是 Rule D 链的胜利. Rule D 在架构级盲区上不足.

**如何补**: `_template/` 10a + 10b.1 + 10b.2 补丁 (已吸收到跨 4 平台 retro §4):
- 10a: Writer 叙事合成伪约束防护 — 约束来源必 WebFetch 官方原文, 非 Writer "我读 Research 出来的模式"
- 10b.1: Reviewer 独立 WebFetch 约束验证 — Reviewer 不能只审 Writer 语义合规, 必独立核 factual base
- 10b.2: 用户反问作 Rule D 外部触发 — Writer/Reviewer 基于同 factual base 时, user 视角反问 = Rule E cross-check 的 off-chain 版

### G-NBL-2. P3.8 Rule A 独立抽检 N 未在 PLAN §6 明示

**问题**: P3.8 reviewer 12th slot (`feature-dev:code-reviewer`) Finding #4 MEDIUM confidence 82:
> "Rule A 原文 'N 样本独立抽检, N 写进 PLAN'. PLAN v2.2 §6 P3.8 Task 未明示 N; main session 深审实际只抽 3/10 而非覆盖全 10. 建议 Phase 5 retro 补 'P3.8 Rule A 独立抽检 N 应 ≥ 5 (50%) 或全覆盖', 本次 3/10 (30%) 在边缘."

**影响**: P3.8 PASS 判定**稳** (因为主 session 深审的 3 题恰好命中关键判据 bug Q10 SUPPTS), 但 Rule A bookkeeping 弱. 不影响 gate.

**如何补**: 
1. PLAN 未来版本 §6 Task 定义时 explicit 写 "N = X" (本平台若有 Phase 6, apply)
2. `_template/` 增补 "Rule A N 阈值建议矩阵" (压缩率 50-70% → N≥3; 70-85% → N≥5; ≥85% → N≥7 或全覆盖)
3. 本平台 post-hoc 说明: 3/10 独立复判虽在边缘但命中高信息量题 (Q10 判据 bug), ROI acceptable

### G-NBL-3. `_progress.json` `p3_8_user_ack` structured field 缺

**问题**: P3.8 reviewer Finding #5 MEDIUM confidence 80:
> "`_progress.json` p3_8_completion 块缺 structured user_ack field. '用户口头 ack' 作 Rule D PASS 第 4 条 evidence chain 有间接 log (用户决定 smoke v3 → v4 升级证明已 ack 9/10), 但无 timestamp + text_snippet structured 记录."

**影响**: Rule E (用户 ack) 合规性 Partial — 间接证据成立, structured field 缺. 不阻塞 gate.

**如何补**: `_progress.json` 已在 L545-548 补 `p3_8_user_ack` 块 (reviewer 行动项 #5 完成). 本 retro 登记此缺口 + 闭合.

### G-NBL-4. Q9/Q11/Q12 supplemental topics in-KB-only 架构限制

**问题**: smoke v4 R1 实测:
- Q9 (Pinnacle 21 FAIL 分类): safety-correct PUNT, 答 "未收录" + 补 SDTMIG §3.2.2 10 条 upstream
- Q11 (Dataset-JSON v1.1 vs XPT v5): PARTIAL 0.5 (a 3/5 缺 2 项 / b c PUNT / d PASS)
- Q12 (CT 版本锁定 operational): PARTIAL 0.5 (a d PUNT / b PASS Define-XML / c PARTIAL hierarchy)

**影响**: 3 题都是 "supplemental topics in-KB-not-covered" 类, NotebookLM 按架构强约束只能 PUNT. 这是**架构限制非能力 FAIL** — safety-correct 但 generalization 短.

**如何补**: 
- 接受架构限制, Phase 4 scoping 决策 "Q9/Q11/Q12 PUNT 作架构限制分类, 不影响 88.2% 主 gate PASS"
- 若未来扩展覆盖 Pinnacle 21 / Dataset-JSON 文档作 bucket 43-45, 可提升. 但 Phase 7 RAG 自建更合理 (参考 `docs/DESIGN_RAG_KG.md`)
- **这是优势的 flip side** — AHP × 3 能 PASS+ 最强正是因为相同的 in-KB-only 架构

### G-NBL-5. F-3 citation dropout T2 题型偏向 (系统性弱点)

**问题**: P3.4.5 reviewer 新发现 F-3 — citation dropout 在 T2 题型 (业务场景/举例类) 偏向, 业务场景/举例类 T2 题易丢 inline cite. P3.8 进一步证实 (smoke_v3_answers T2 题 citation 数明显低于 T1 事实查询类).

**影响**: A/B 评分规则已处置 (不扣 T2 题分, "语义等价即 PASS"), 不影响主 gate; 但是系统性弱点, Retro 关键教训.

**如何补**: 
- 未来 Custom mode instructions.md 调优 **针对性加 "业务例后强制 cite source" 规则** (当前 13 rules 含 citation 通用约束, 未分题型)
- 或 NotebookLM 平台侧架构改进 (NotebookLM 团队 feature request), 超本项目 scope
- **post-project optional**: 若用户回头精雕 (触发 PLAN §10 ICEBOX 重开), 针对 T2 题型做 A/B 测试 Custom mode 精调

### G-NBL-6. Free tier 50-cap 证据 3 解读 SKIP + 接受残余风险

**问题**: NotebookLM PLAN v2.2 L70 "分享不改 viewer 自己 tier source cap" 证据 MEDIUM (非 A 级官方原文). P3.9 子步骤 (f) 计划用 Free tier 小号实测闭合, 但本 notebook 只上传 42 sources (≤50), **未触发 Free tier 50-cap**, 无法创造 A/B/C 三路径测试条件.

**影响**: ≤50 source 策略的**次要归因** (Free tier 兼容) 悬置. **主要归因** (indexing silent fail + citation 信噪比) 不受影响, 结论不变.

**主归因 vs 次归因分层** (reviewer #6 fix 2026-04-24): ≤50 策略的**主归因 HIGH 证据独立稳固**(indexing silent fail 42/42 0 漏 + P3.4 smoke 10/10 顶阈 + citation 信噪比 P3.4.5 8.5/10 验), 这些证据**不受 Free tier cap 悬置影响**. **次归因 MEDIUM 悬置** (Free tier 兼容 — viewer 自己 tier cap 规则未 A 级官方文档印证). 两层独立 — 次归因 SKIP 不破主归因, 结论"≤50 源策略合理"**不变**. 读者若只看本 retro 可能误以为 Free tier cap 是 ≤50 策略唯一悬置点, 此段明示分层.

**如何补**: Daisy 2026-04-23 接受**残余风险**. 补做路径 (post-Phase-5 optional):
1. 制造 >50 source 测试集 (临时 bucket 分裂 / 重新 merge), 让 notebook 超 50 触发 cap
2. Free tier Gmail 小号 invite 查看
3. 看小号能看到多少 source (A/B/C 判定)

**闭合状态**: 🟡 **SKIP + accepted_residual_risk** (次归因不升 A, 不证伪, 悬置; 主归因不受影响).

---

## §3 关键决策复盘 (D-NBL-1 to D-NBL-6, pivot 作关键案例)

### D-NBL-1. v1 3-notebook → v2 1-notebook × ≤50 架构 pivot — **极正确**

**决策**: 2026-04-21 PM Phase 3 未动工前 pivot, sunk cost = 1 天写 v1 PLAN. 舍 v1 3-notebook 职责隔离架构, 重整为 1 notebook × 42 source cluster + 3 档分享切换.

**回头看**: **极正确**. 若 Phase 3 开始上传才发现伪约束, 293 source × 3 notebook 同步维护 + Req 变量分散审计 = 代价量级升. Pivot 在未动工前触发, ROI 最大.

**关键动作链**:
1. 用户 review Phase 2 v1 PLAN, 质疑 3 notebook 架构过重
2. 主 session 派 3 个 WebFetch 独立验证 (50-cap 规则 / Chat custom goals / 分享档位 viewer 体验)
3. 3 源全部推翻 v1 假设 — "UI 3 档可切" / "50-cap 仅 Restricted" / "viewer 自己 tier cap"
4. 主 session 向用户汇报 pivot 建议 + 用户 ack
5. v1 冻结到 `archive/v1_3notebook_SUPERSEDED_2026-04-21/` + `ARCHITECTURE_PIVOT_RECORD.md` 记录完整证据链 + 被舍弃决策 D1-D10 + 保留资产 A-F
6. v2 PLAN 重写 + 第 9 种 subagent_type `oh-my-claudecode:architect` 独立审 CONDITIONAL_PASS 84% (3 HIGH + 5 MEDIUM + 5 LOW 全修)

**教训作 `_template/` 补丁 10a/10b.1/10b.2** (已登跨 4 平台 retro §4).

### D-NBL-2. v2.1 ICEBOX Studio 三件套 (Audio/Mind Map/Study Guide) — **正确 + PARTIAL 负外部性** (reviewer #4 fix 2026-04-24)

**决策**: 2026-04-22 PM 用户决策 A+保留: P3.5 Audio Overview / P3.6 Mind Map / P3.7 Study Guide **挪 post-project optional**, 不计入 Phase 3 收束 gate, 不计入 Phase 4 跨平台对比.

**回头看**: **正确 (正外部性确立) + PARTIAL 负外部性**.

**正外部性** (原 v0.1 归因, 成立):
- Studio 独有产出 (Audio/Mind Map/Study Guide) **无跨 4 平台对比价值** — Claude/ChatGPT/Gemini 均无等价功能
- 问答维度 (P3.4 indexing smoke + P3.4.5 Req 语义 + P3.8 smoke v3 + P3.9 smoke v4) 才是跨平台核心比较基线
- Phase 3 总工时下调 ~3h (本平台 lifecycle 缩短 0.5 天)
- 用户全项目完成后小概率回头精雕 — PLAN §10 "Post-project ICEBOX" 节保留重开流程

**负外部性** (reviewer #4 新增分析):
- Studio 三件套是 NotebookLM **独有亮点**能力 showcase (Audio Overview 30-45 min 播客对谈 / Mind Map 跨域关系可视化 / Study Guide Socratic 引导) — 其他 3 平台无此能力, 但**无跨平台对比 ≠ 无价值**, 反而是 NotebookLM 差异化卖点
- **ICEBOX 触发条件 weak**: PLAN §10 "用户主动提出回头精雕" — Phase 6.5 收束 → Phase 7 RAG 启动后, 用户很可能把 NotebookLM 视为"已部署完毕", Studio 成 **zombie task** 永不触发
- **实际风险**: 本 Phase 5 retro 决策 ROI 成立 (跨平台 cross-check 聚焦问答维度合理), 但**长期看若用户不触发, NotebookLM 独有能力不进入跨 4 事实 base** — 本项目对 "NotebookLM 平台能力" 的刻画**永久残缺**
- **非推翻 ICEBOX 决策**, 承认负外部性有助于: (a) 未来重评估触发条件是否该升为"强 trigger" (e.g. Phase 7 启动前强制评估一次 Studio post-project 是否启动) (b) 跨 4 retro 的 cross-platform 结论宜加免责 "NotebookLM 独有能力维度未跑" caveat

**保留重开流程** (PLAN §10):
> 用户 ack → 读本节 + §6 / §7 原任务定义 → 开新分支 (不污染主 retrospective) → 生成产物 + 评估 → 补 RETROSPECTIVE Appendix + `_template/` 新补丁候选 (若有).

### D-NBL-3. v2.2 P3.8 题库 smoke v2.1 → v3 Q1-Q10 升级 — **正确**

**决策**: 2026-04-22 PM 用户 ack 选项 A, P3.8 题库从 smoke v2.1 (10 题 ChatGPT 04 业务弹药 §1.1-§1.10 预设 scenario) 升 smoke v3 Q1-Q10 (v3.4 新域 GF/CP/BE+BS + 域边界 + Timing 深化 + Extensible CT + Pinnacle 21 + SUPP 深化).

**回头看**: **正确**. v2.1 10 题全押 ChatGPT 04 预设 scenario = open-book 考试, 对 NotebookLM 42 bucket 全域 RAG **也没鉴别力**. v3 故意避开 04 预设, 测**真 generalization 能力**. 对齐 ChatGPT+Gemini N5.3 同期可比, Phase 4 跨平台对比才有意义.

**阈值保持不降**: ≥9/10 (~90%) 按用户决策不降 — ChatGPT/Gemini 合格阈 71%/70% 是因为题型专属 + 生疏平台 buffer, NotebookLM P3.4.5 已 CONDITIONAL_PASS 8.5/10 验底座稳, **不给额外 buffer**.

### D-NBL-4. smoke v3 → v4 升级 (加 AHP × 3) — **极正确**

**决策**: 2026-04-22 PM 用户 meta insight 驱动:
> "smoke v3 当前只测'给正确前提答对', 缺'给错前提能否纠错'维度. 用户常问错前提希望模型纠错而非幻觉."

主 session 执行 smoke v3 → v4 升级路径 (7 步, `SMOKE_V4_DESIGN_HANDOFF.md`):
1. 审计 smoke_v3_questions_draft.md v3.1 Q1-Q14 前提真实性 (派第 11 种 subagent_type `oh-my-claudecode:document-specialist`)
2. 强制修 Q10 (b) + 其他发现的前提错
3. 新增 AHP × 3 (variable / cross-domain / deprecated-version 三类 trap)
4. v3 历史结果标 SUPERSEDED 不回溯重评分
5. 4 平台 smoke v4 R1 baseline
6. R1 FAIL 改 system prompts (尤其 anti-hallucination 锚点) → R2 retest
7. 跨 4 平台 PHASE5_RETROSPECTIVE 合流

**回头看**: **极正确**. AHP × 3 是 R1 灵魂 — NotebookLM 3/3 全 PASS+ 最强证明 in-KB-only 天然优势, Gemini R1 0/3 AHP FAIL 暴露锚缺 (触发 R2 v6 CO-5 章节单点修 → 3/3 PASS+). **没 AHP × 3 整个 4 平台 R1 都会假 PASS**.

**meta insight 驱动力**: NotebookLM P3.8 Q10 答案主动纠错 SUPPTS 前提是 catalyst — 这个"model-visible anti-hallucination strength" 直接启发 AHP × 3 设计. 本平台 in-KB-only 架构是 smoke v4 进化的**第一推动力**.

### D-NBL-5. P3.9 三档切换 Public 档语义深化 — **正确 + 新发现**

**决策**: Daisy 2026-04-23 执行 P3.9 三档切换演练 6 子步 (a-f); 主 session 根据口述 verdicts 写完整 evidence `share_level_toggle_drill.md` v1.0 FINAL.

**回头看**: **正确且深化原判断**.

**核心结果**: 5 PASS + 1 PARTIAL (c) + 1 SKIP (f), 总体 PASS.

**新发现 (meta-insight)**: **"Public" 档 ≠ auto gallery 广播**. NotebookLM 公开画廊是**策展 (curated Featured list)** 非 auto-listed. Public 档实质语义 = "允许任何持链接者无需登录访问" 而非 "被动曝光给搜索". 这修正了 v1 3-notebook 时期**"Public = 广播"假设** (ARCHITECTURE_PIVOT_RECORD D3 的一部分被 P3.9 实测印证并深化).

**对隐私友好性的启示**: Public 档 reach < 用户预期, 但**反而降低**隐私风险 — 更友好. 这是 single-notebook 多 scope 架构的**实用优势**. 比 ChatGPT GPT Store "Public=全网广播" **保守**, 适合小圈内部分享 + 定向外发场景. 已登跨 4 平台 retro §4.15 补丁.

### D-NBL-6. async lane 独立于 SYNC_BOARD 锁步 — **正确**

**决策**: NotebookLM 不参与 `SYNC_BOARD.md` ChatGPT↔Gemini 2-way 锁步, 独立 lane 推进. Phase 0-1 与 ChatGPT/Gemini 同期 PASS 但不 gate-synced; Phase 2-4 独立推进.

**回头看**: **正确**. 好处:
- **不受锁步节奏拖** — NotebookLM Phase 3 上传 + smoke 连续跑满 42 小时, 不需要等 ChatGPT/Gemini gate
- **吸收前 2 平台收束补丁** — Phase 3 Node 4 "战略转向业务问答优化" 的内容策略 (两平台 `docs/PLAN_V2_C.md` / `PLAN_BATCH2.md`), NotebookLM 的 source 合并粒度**直接借鉴不重踩**
- **方法论独立但 evidence 共享** — smoke v4 统一题库解决了 cross-check 问题, 不需要同步 gate

代价: 不能 cross-pollinate 即时, 但 evidence 共享 (smoke v4 统一题库) 解决了.

---

## §4 `_template/` 补丁贡献 (本平台独有)

### 已吸收到跨 4 平台 retro (v1.0 FINAL 2026-04-24)

| 补丁 | 来源 | 跨 4 平台 retro 位置 | 核心内容 |
|---|---|---|---|
| **10a** | v1→v2 pivot | §4 (已吸收) | Writer 叙事合成伪约束防护 — 约束来源必 WebFetch 官方原文, 非 Writer "我读 Research 出来的模式" |
| **10b.1** | v1→v2 pivot | §4 (已吸收) | Reviewer 独立 WebFetch 约束验证 — Reviewer 不能只审 Writer 语义合规, 必独立核 factual base |
| **10b.2** | v1→v2 pivot | §4 (已吸收) | 用户反问作 Rule D 外部触发 — Writer/Reviewer 基于同 factual base 时, user 视角反问 = Rule E cross-check 的 off-chain 版 |
| **15** | P3.9 实测 | §4.15 | 分享档位切换作 single-notebook 多 scope 新范式 — Public 档 ≠ auto gallery 广播, 比 GPT Store 保守, 隐私友好 |

### 新候选 (本 NotebookLM retro 产出, 待合入 `_template/`)

| 候选 | 源 | 内容 |
|---|---|---|
| **16 (MEDIUM)** | R-NBL-2 | 42 bucket concept cluster 策略 — "concept 聚合优先于 domain/字母切", 通用排布原则 |
| **17 (MEDIUM)** | R-NBL-4 | Rule A N 阈值建议矩阵 — 压缩率 50-70% → N≥3; 70-85% → N≥5; ≥85% → N≥7 或全覆盖 |
| **18 (LOW)** | R-NBL-6 | in-KB-only 架构天然 anti-hallucination 优势 vs prompt-level anchor — 架构优势非 prompt 优势, 互补非替代 |
| **19 (LOW)** | G-NBL-5 | Citation dropout T2 题型偏向观察 — 业务场景/举例类 T2 题易丢 inline cite, 平台侧限制非 prompt 修复 |

**候选 16-19 登记**: 本 retro 本身 — Phase 6.5 收束后若用户 ack, 合入 `ai_platforms/_template/06_review.md` 或 `09_closure.md` 对应章节.

---

## §5 与跨 4 平台 PHASE5_RETROSPECTIVE 的呼应

本 retro 是跨 4 平台 retro 的 **evidence base 之一** (跨 4 retro §0 Phase 5 入参列 7 前置产物, 本 retro 未独立列但在 retro L6-L14 上游参考链中).

### 本平台贡献到跨 4 retro 的具体位置

(reviewer #2 fix 2026-04-24: flat anchor 替代虚构 sub-heading — 跨 4 retro 实际是 §1/§2/§3 下直接并列 R5-*/G5-*/D5-* 而非 §1.1-§1.6 层级)

| 本 retro 章节 | 跨 4 平台 retro 对应位置 | 贡献内容 |
|---|---|---|
| R-NBL-8 (P3.9 三档切换) | §1 R5-6 (flat anchor) | 三档切换 UI 级 VERIFIED 做法 (6 子步 + Public ≠ gallery 新发现) |
| G-NBL-2 (Rule A N 缺) | §2 G5-3 (flat anchor) | NotebookLM P3.8 reviewer 5 action items #3/#4/#5 |
| G-NBL-6 (Free tier cap SKIP) | §2 G5-5 (flat anchor) | Free tier 50-cap 证据 3 SKIP + 接受残余风险 |
| D-NBL-1 (v1→v2 pivot) | §3 D5-6 (flat anchor) | NotebookLM v1→v2 架构 pivot — 正确 (Writer 叙事合成伪约束教训) |
| D-NBL-5 (P3.9 Public 新发现) | §3 D5-7 (flat anchor) | 三档分享实测决策 — 正确 + 深化 (Public ≠ gallery) |
| `_template/` 补丁 10a/10b.1/10b.2/15 | §4 补丁 10a / 10b.1 / 10b.2 / 15 (bullet 而非 heading) | 4 个补丁源自本平台 |

**G5-4 交代** (Open Q1 fix 2026-04-24): 跨 4 retro §2 五缺口中 G5-4 (Q4-Q10 V5C regression) **不涉 NotebookLM**, 仅 ChatGPT + Gemini 双平台议题, 已在跨 4 retro 2026-04-24 标 **CLOSED** (14/14 PASS + 15th Rule D reviewer APPROVE). 本 NotebookLM retro 不对应 G5-4, 不计入本平台缺口.

### 跨 4 retro 对本平台的 cross-link

跨 4 retro §0.2 L35:
> NotebookLM: Phase 4 **COMPLETE** (3/3 items: #1 P3.8 reviewer 12th slot DONE + #2 **P3.9 DONE 2026-04-23** drill PASS + #3 跨 4 平台矩阵 R1 消掉) + **Phase 5 cross-platform 合流 unblocked**

跨 4 retro §1.1 L27:
> NotebookLM v2 (1 notebook × 42 sources) 最终 Score **15/17 (88.2%) R1** + PASS ✅ + lifecycle 2026-04-21 → 2026-04-23 (async lane)

**呼应无偏差**: 跨 4 retro 已正确反映 NotebookLM 状态 + 贡献, 本平台 retro 作独立深挖与补充.

---

## §6 Rule A/B/C/D/E 合规自查

### Rule A (语义抽检强制): **部分满足 + category error 承认**

- **执行面**: 
  - Phase A A4 结构级 ∅ gap audit 176/176 Req 全覆盖
  - P3.4.5 语义级 Q1 红线业务问答 N=10 (CONDITIONAL_PASS 8.5/10, 8 层递 seed + 10 变量约束校验)
  - P3.8 主 session 独立复判 3/10 (30%) — **在边缘**, reviewer 建议 N ≥ 5
- **caveat**: P3.8 reviewer Finding #4 MEDIUM 82, 建议 Phase 5 retro 补 "P3.8 Rule A 独立抽检 N 应 ≥ 5 (50%) 或全覆盖". 本 retro G-NBL-2 登记.
- **Category error 承认** (reviewer #3 fix 2026-04-24, 同步跨 4 retro 28th reviewer F3): 本 retro 的 Rule A trace (Phase A A4 结构级 + P3.4.5 语义级 + P3.8 3/10 复判) 严格说是 **meta-evidence trace** (trace 前序产物作 evidence base), 非 Rule A 原文严格意义的 "**N 独立样本抽检**" (N 写进 PLAN, 独立抽新样本审). 两者有 category 差异: trace 证明 "已有 evidence 闭合", 独立抽检证明 "新样本再打一次"也稳. 跨 4 retro 28th reviewer F3 修过此 category error, 本 retro 同步承认.
- **严格 Rule A 部分满足**: 结构级 + 语义级双锚 PASS, 独立抽检 N 在边缘 + category error 承认. 严格 N≥5 独立样本抽检挪 post-project optional (G-NBL-2 登记 `_template/` 候选补丁 17 "Rule A N 阈值建议矩阵").

### Rule B (失败归档不删): **合规**

- `failures/` dir 空 (P3.8 0 retry; Q10 sub-question 自动拆分不算 retry, 是"分段提交同一题"非"重跑")
- v1→v2 pivot 失败归档 `archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` 完整保留 — sunk cost 1 天 PLAN 不删, 决策 D1-D10 + 保留资产 A-F 留档

### Rule C (Retro 强制): **合规**

- **本文即产物** — Tier 2 async lane 必写, 三段 (§1 保留 R-NBL-1-8 / §2 缺口 G-NBL-1-6 / §3 决策 D-NBL-1-6) 全到位
- Writer = 主 session (2026-04-24), 待派独立 reviewer 审

### Rule D (审阅隔离): **chain 本平台内独立 2 slot + async lane 贡献 2 slot**

**本平台 Phase 2-3 内独立 Rule D 链** (cumulative 10 种 subagent_type 在 NotebookLM 独立 lane):

> **Slot 编号 caveat** (reviewer #7 fix 2026-04-24): 本平台 10-slot 是 NotebookLM lane **内部连续编号**, 与跨 4 平台 Appendix A 28-slot **全局编号不一一对应**. 部分 subagent_type 在不同 phase/lane 被重用 (e.g. 本平台 #10 `scientist` 与跨 4 retro #14 `scientist` 是同 subagent_type 不同 evidence, 各自作独立 reviewer). **跨 4 全局 28-slot roster 以跨 4 retro Appendix A 为准**; 本平台 10-slot 仅作本 lane 审计 trace. 编号 overlap ≠ self-review — 每次都是新 context/evidence.

| # | Subagent type | Phase | 产物 |
|---|---|---|---|
| 1 | `general-purpose` | P1 Writer #1 | research.md 初版 |
| 2 | `oh-my-claudecode:verifier` | P1 Reviewer #1 | phase1_reviewer.md (已归档) |
| 3 | `oh-my-claudecode:executor` | P1 Writer #2 | research.md 修正版 |
| 4 | `oh-my-claudecode:critic` | P1 Reviewer #2 | phase1_reviewer2.md (已归档) |
| 5 | `oh-my-claudecode:planner` | P2v1 Writer #3 | PLAN_v1 (归档 v1_3notebook) |
| 6 | `oh-my-claudecode:analyst` | P2v1 Reviewer #3 | phase2_reviewer.md (归档) |
| 7 | `feature-dev:code-architect` | P2v1 Writer #4 | PLAN v1.1 (归档) |
| 8 | `pr-review-toolkit:code-reviewer` | P2v1 Reviewer #4 | phase2_reviewer2.md (归档) |
| — | 主 session | **P2v2 Writer (pivot)** | PLAN.md v2 |
| 9 | `oh-my-claudecode:architect` | P2v2 Reviewer | phase2_v2_reviewer.md (CONDITIONAL_PASS 84%) |
| 10 | `oh-my-claudecode:scientist` | P3.4.5 Reviewer | phase3_task_P3.4.5_req_semantic_audit.md (Q1 红线语义级 8.5/10) |

**跨 4 平台 28-slot roster 新加 NotebookLM 贡献**:

| # (跨 4) | Subagent type | 产物 |
|---|---|---|
| #24 | `oh-my-claudecode:document-specialist` | smoke v3→v4 audit (`archive/smoke_history/smoke_v3_audit_notes.md`) |
| #25 | `feature-dev:code-reviewer` reuse | P3.8 reviewer (`p3_8_reviewer_notes.md`) |

**本 Phase 5 NotebookLM retro reviewer** (待派):
- 候选: `oh-my-claudecode:critic` (本平台 #4 slot 重用作新 context) 或 `superpowers:code-reviewer` (全新 subagent_type)
- Rule D 要求: writer (主 session) ≠ reviewer context, subagent_type 必须不同.

### Rule E (跨平台 cross-check): **隐式使用成立**

- 本平台 smoke v4 R1 15/17 的校验 **不是** NotebookLM 自 PASS (self-score), 而是 **4 平台 cross-check 矩阵** (`SMOKE_V4.md §3` 17×4 verdict 矩阵)
- NotebookLM AHP × 3 PASS+ 最强在 4 平台对比下**才有意义** — 单平台自跑 3/3 无法证明是架构优势非幸运
- Rule E 草案已在跨 4 平台 retro §5 登, 待 Daisy ack 升 `~/.claude/CLAUDE.md` `<personal_operating_principles>`

---

## §7 下一步 (post sign-off)

### 7.1 本 retro 闭合路径

1. **Writer lane 完成** (本文) — 2026-04-24
2. **Reviewer lane** — 派 `oh-my-claudecode:critic` 或 `superpowers:code-reviewer` 独审, 产 `dev/evidence/phase5_retrospective_reviewer.md`
3. **Daisy ack** → 本 retro v1.0 FINAL
4. **ROADMAP.md 更新**: 状态 "Phase 2 v2 准备中" → "Phase 5 FINAL 已完成 (2026-04-23)" + 实际 source 数 (42) / A/B 数据 (smoke v4 R1 15/17 88.2%) / 3 档切换结果 (PASS) 填入

### 7.2 索引文件同步 (与本 retro 并行)

- **CLAUDE.md Key Paths** — NotebookLM 入口状态从 "Phase 3 P3.8 执行 9/10 PASS (2026-04-22 PM)" → "Phase 5 FINAL 完成 (smoke v4 R1 15/17 88.2% + P3.9 PASS + Rule D async lane 2 slot)"
- **docs/PROGRESS.md** — Phase 6.5 NotebookLM 行状态更新 + 跨 4 平台 Phase 5 sign-off 反映
- **.work/MANIFEST.md** — Plan map § Phase 6.5 NotebookLM 状态行同步

### 7.3 UPLOAD_TUTORIAL.md (Phase 5 待产出, PLAN §9 定义) — **与 retro FINAL 解耦** (reviewer #8 fix 2026-04-24)

- 10 章节用户部署教程 (参考 Claude `UPLOAD_TUTORIAL.md` 范式)
- 单 notebook 路径 + 3 档分享切换使用说明
- Daisy 2026-04-23 已完成实操, 有素材
- **与 PLAN §4 Phase 5 Task 的 scope 关系** (reviewer #8 澄清): PLAN §4 L359 原定义 Phase 5 含 "RETROSPECTIVE + UPLOAD_TUTORIAL + 父目录索引 + _template/ 补丁 PR + commit + push" 整体; 本 retro 升 v1.0 FINAL 仅代表 **RETROSPECTIVE 子 gate 闭合**, UPLOAD_TUTORIAL 仍是 Phase 5 必产物但作独立子 gate. 两种 go-forward 选择:
  - **选项 A (推荐)**: retro v1.0 FINAL 升 + UPLOAD_TUTORIAL 同 Phase 5 批次产出 (Daisy ack retro 后主 session 接着写 TUTORIAL), 两者 bundled 作 Phase 5 整体 sign-off
  - **选项 B (降级)**: 显式修 PLAN §4 把 UPLOAD_TUTORIAL 降级为 post-Phase-5 optional (如 Studio 三件套 ICEBOX 模式), 仅 retro + 索引 + 补丁作 Phase 5 gate
- **当前建议**: 选 A — Daisy 2026-04-23 实操素材在, 1-2h 可写完, 无必要降级 PLAN. 本 retro FINAL 不阻塞 (独立子 gate), 但 Phase 5 整体 sign-off 需 TUTORIAL 同批闭合

### 7.4 `_template/` 补丁 16-19 合入 (本 retro §4 新候选)

- 合入 `ai_platforms/_template/` 对应章节 (`06_review.md` 或 `09_closure.md`)
- 10a/10b.1/10b.2/15 已在跨 4 retro 合入, 16-19 属"额外产出"待用户 ack

### 7.5 P3.5/P3.6/P3.7 Studio 三件套 post-project (v2.1 ICEBOX)

- PLAN §10 "Post-project ICEBOX" 小节保留完整任务定义
- **触发条件**: 用户主动提出 "回头精雕 NotebookLM Studio 三件套"
- **不触发时永久 ICEBOX, 不影响本次 Phase 5 收束完整性**

---

## §8 版本管理

| 版本 | 日期 | 状态 | 触发 |
|---|---|---|---|
| **v0.1** | **2026-04-24 (上午)** | 🟡 **DRAFT** (pending reviewer + Daisy ack) | 主 session writer lane 完成; async lane 独立 retro; Phase 5 闭合路径 Step 1 |
| **v0.2 post-reviewer-fix** | **2026-04-24 (下午)** | 🟡 **post-fix, ack-ready** | 独立 reviewer `oh-my-claudecode:critic` CONDITIONAL_PASS 8.0/10 + 1 HIGH + 4 MEDIUM + 3 遗漏 + 2 Open Q 全修; evidence `dev/evidence/phase5_retrospective_reviewer.md` (reviewer #2 Open Q2 fix: 中间态 audit trail) |
| **v1.0 FINAL** | **2026-04-24 (晚, Daisy 认可)** | ✅ **FINAL** | Daisy 读完 v0.2 post-reviewer-fix + reviewer 报告 → ack → NotebookLM async lane Phase 5 retro sign-off → UPLOAD_TUTORIAL.md v1.0 同批产出 → 父目录索引同步 → commit 闭环 |

---

## Appendix A — 关键 evidence 文件速查

| 文件 | 路径 | 用途 |
|---|---|---|
| Phase 2 v2 reviewer | `dev/evidence/phase2_v2_reviewer.md` | Rule D #9 architect CONDITIONAL_PASS 84% |
| Phase A Req 全集 | `dev/evidence/req_vars_full_set.md` | 176 独立 Req 基线 |
| 42 bucket 配置 | `dev/scripts/bucket_config.json` + `current/uploads/MANIFEST.md` | 295 md → 42 bucket |
| P3.2 上传 log | `dev/evidence/p3_2_upload_log.md` | 42/42 indexed 0 silent fail |
| P3.3 Custom mode | `dev/evidence/chat_mode_toggle_test.md` | H3 初步 VERIFIED |
| P3.4 indexing smoke | `dev/evidence/indexing_smoke.md` | 10/10 顶阈值 PASS |
| P3.4.5 Q1 语义 | `dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md` | 8.5/10 CONDITIONAL_PASS |
| P3.8 smoke v3 | `dev/evidence/smoke_v3_results.md` + `smoke_v3_answers/` | 9/10 strict PASS |
| P3.8 reviewer | `dev/evidence/p3_8_reviewer_notes.md` | Rule D #25 (cross-lane) code-reviewer PASS |
| smoke v4 R1 | `dev/evidence/smoke_v4_results.md` + `smoke_v4_answers/` | 15/17 PASS (88.2%) |
| P3.9 三档演练 | `dev/evidence/share_level_toggle_drill.md` | v1.0 FINAL 5 PASS + 1 PARTIAL + 1 SKIP |
| v1 架构 pivot 记录 | `archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md` | Rule B 失败归档 + D1-D10 + A-F |
| 跨 4 平台 Phase 5 retro | `../../retrospectives/PHASE5_RETROSPECTIVE.md` | v1.0 FINAL 2026-04-24 Daisy 认可 |

---

## Appendix B — 本 retro 自检 (Rule C 元反思)

**元问题**: 本 retro 是否自身有"Writer 叙事合成伪约束"?

- **保留** 8 条 (§1 R-NBL-1-8): 每条含支持证据 + 文件引用, 未脱离 evidence base
- **缺口** 6 条 (§2 G-NBL-1-6): 4 条带 reviewer/审计来源 (G-NBL-2/3/5 来自 P3.8 reviewer, G-NBL-1 来自 PLAN §11, G-NBL-6 来自 P3.9 (f)), 2 条是主 session 归纳 (G-NBL-4 Q9/Q11/Q12 架构限制, G-NBL-5 F-3 T2 偏向, 均有 smoke 数据支持)
- **决策** 6 条 (§3 D-NBL-1-6): D-NBL-1 pivot 是跨 4 平台 retro 已 Daisy ack 的核心教训, D-NBL-2-6 有用户 ack 时间戳 + 决策链 (2026-04-22 PM / 2026-04-23 等)
- **独立 reviewer 未派**: 本 retro v0.1 DRAFT 状态, 待派独立 subagent_type (Rule D 强制), 非 writer self-review

**Self-catch 示例** (reviewer #5 fix 2026-04-24): v0.1 DRAFT R-NBL-3 + §0.1 表原写 "instructions.md 9,011 chars (11% headroom)" — Writer 继承 CLAUDE.md Key Paths 原叙事"9,011 chars 90% of 10K cap"未独立核对. 独立 reviewer `oh-my-claudecode:critic` HIGH #1 抓出 → Python 核实 `len(str) = 8,925 Unicode chars` / `len(utf-8 bytes) = 9,011`, 单位错配, 实际 headroom **10.75%** 非 11%. **这是 G-NBL-1 "Writer 叙事范式锁定" 在本 retro 的当场复现** — Writer 以为 CLAUDE.md 数据已经核对过, 继承即信, 未回 binary / wc 原始核查. 教训: 数值引用即使来自前序已合规产物, retro level 仍需原始重核. 外部 Reviewer lane 不可或缺 (此一条 finding 单独已值回全套 Rule D 独立审). v0.2 post-reviewer-fix 已修, CLAUDE.md 同步修.

**结论**: 本 retro Writer lane v0.1 DRAFT 产出 + Reviewer lane v0.2 post-fix 闭合 (1 HIGH + 4 MEDIUM + 3 遗漏 + 2 Open Q 全修) + 1 Self-catch 作 Appendix B 元反思实证. **等 Daisy ack 升 v1.0 FINAL**. 本 self-check 不能替代独立 reviewer — 本次 self-catch 反而证明这一点 (v0.1 Appendix B 形式化自审未抓出 9,011 chars 错, reviewer 抓出).

---

*DRAFT v0.1 2026-04-24. 主 session writer 产出, async lane Phase 5 retro. 待派第 11-13 种新 subagent_type (候选 `oh-my-claudecode:critic` / `superpowers:code-reviewer`) 独立审 → Daisy ack 升 v1.0 FINAL → Phase 6.5 NotebookLM async lane sign-off.*
