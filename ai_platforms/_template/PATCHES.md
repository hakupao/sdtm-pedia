# `_template/` 补丁应用历史 (Patches Applied)

> **用途**: 集中登记 `_template/` 范本自 2026-04-20 就绪以来吸收的全部补丁候选 + 补丁内容详述.
> **原则**: 补丁是 Phase 6.5 多平台部署实践中发现的**范本缺陷**或**跨平台 cross-pollination 成果**, 逐条验证后合入; 每条补丁必含 (a) 来源 retro 位置 (b) 严重度 (c) 适用 `_template/` 维度 (d) 核心内容 (e) apply 状态.
> **最后更新**: 2026-04-24 晚 (NotebookLM async lane Phase 5 SIGN-OFF 同批产出 16-19)

---

## 补丁索引表

| ID | Severity | 源 | 适用维度 | 状态 | 核心 |
|----|----------|-----|----------|------|------|
| **10a** | HIGH | NotebookLM v1→v2 pivot (2026-04-21) | `03_research.md` Writer 立场警示 | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 | Writer 叙事合成伪约束防护 — 约束来源必 WebFetch 官方原文, 非 Writer "我读 Research 出来的模式" |
| **10b.1** | HIGH | NotebookLM v1→v2 pivot | `04_plan.md` planner 接 research 时 "核心约束原文回溯" 段 | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 | Reviewer 独立 WebFetch 约束验证 — Reviewer 不能只审 Writer 语义合规, 必独立核 factual base |
| **10b.2** | HIGH | NotebookLM v1→v2 pivot | `04_plan.md` + `06_review.md` "Phase 2 PASS 前用户反问 gate" | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 | 用户反问作 Rule D 外部触发 — Writer/Reviewer 基于同 factual base 时, user 视角反问 = Rule E cross-check 的 off-chain 版 |
| **11a** | HIGH | Gemini v6 CO-5 anti-hallucination (R2, 2026-04-23) | `05_solution.md` system_prompt 章节模板 | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 | Anti-hallucination guardrail 作 system_prompt 级 default 章节 (3 AHP 子 + 6 执行规则 + 边界模板 + Step 0/10 工作流) |
| **11b** | HIGH | Gemini v6 CO-4 §GF 单负向失衡 (R2 G5-1) | `05_solution.md` + `03_research.md` 新域变量清单 | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 | 正向清单 + 负向清单**双锚** — 新域变量必同时含 "Core=Exp 完整正向" + "禁止臆造 负向" |
| **11c** | MEDIUM | R1/R2 Gemini AHP 0/3 vs 16/17 bonus 解耦 | `06_review.md` A/B 矩阵 | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 | 双硬 gate 设计 — 核心能力 (≥70%) + anti-hallucination (≥67%) 分开判, 不 summing |
| **12** | MEDIUM | Rule D 27-chain saturation 观察 | `07_agent_dispatch.md` + `README.md` | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 | Rule D chain 数字 > 12 种 saturation 信号 — "连续 2 个 slot 0 HIGH/MEDIUM finding 时宣告饱和" |
| **13** | MEDIUM | R1/R2 阈值设计 | `06_review.md` A/B 评分规则 | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 | Bonus 题 vs main gate 解耦模板 — Q1-Q10 主 gate + Q11-Q14 bonus + AHP hard gate |
| **14** | MEDIUM | R5-1 Rule E 候选 (4 平台 cross-check ground truth) | `02_workflow.md` + `06_review.md` | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 | 4 平台 cross-check ground truth 机制文档化 — in-KB-only 作 truth / web-search 作 coverage / 训练数据作 depth / prompt 锚控作受控对照 |
| **15** | LOW | NotebookLM P3.9 三档切换实测 (2026-04-23) | `00_platform_profile.md` §D 分享档位 | ✅ **APPLIED** via PHASE5_RETROSPECTIVE §4 + P3.9 drill 新发现扩展 | 分享档位切换作 single-notebook 多 scope 新范式; **Public ≠ auto gallery 广播** (比 GPT Store "全网广播" 保守, 隐私友好性更高, 适合小圈+定向外发) |
| **16** | MEDIUM | NotebookLM R-NBL-2 (42 bucket concept cluster) | `05_solution.md` 内容策略 | 🟡 **NEW candidate 2026-04-24** | Concept cluster 优先于 domain/字母切 — 跨平台通用排布原则 |
| **17** | MEDIUM | NotebookLM G-NBL-2 (P3.8 Rule A N 未明示) + reviewer category error | `02_workflow.md` + `06_review.md` | 🟡 **NEW candidate 2026-04-24** | Rule A N 阈值建议矩阵 + meta-evidence trace ≠ N 独立抽检 category error 警示 |
| **18** | LOW | NotebookLM R-NBL-6 (AHP × 3 全 PASS+ 最强) | `00_platform_profile.md` §G 边界行为 + `06_review.md` | 🟡 **NEW candidate 2026-04-24** | in-KB-only 架构天然 anti-hallucination 优势 vs prompt-level anchor — 架构优势非 prompt 优势, 互补非替代 |
| **19** | LOW | NotebookLM G-NBL-5 (F-3 citation dropout T2 偏向) | `06_review.md` A/B 评分规则 + 系统性弱点记录 | 🟡 **NEW candidate 2026-04-24** | Citation dropout T2 题型偏向观察 — 业务场景/举例类 T2 题易丢 inline cite, 平台侧限制非 prompt 修复 |

---

## 新候选补丁详述 (16-19, 2026-04-24 本次加入)

### 补丁 16 (MEDIUM) — Concept cluster 排布原则

**来源**: NotebookLM `docs/RETROSPECTIVE.md` §1 R-NBL-2 "42 bucket concept cluster 策略 (63/63 + 176/176 ∅ gap)"

**适用维度**: `_template/05_solution.md` 内容策略章节

**问题**: 当平台有 source 数硬限 (NotebookLM 300 cap / ChatGPT 20 硬限 / Gemini 10 硬限等) 需要把 295 md / 200+ md / 多源 concept 聚合合并为 ≤N source 时, 按什么粒度合?

**历史做法误区** (跨平台观察到 3 次):
- 按 **domain 字母**切 (AB_*/CD_*/EF_*...): 信息碎片化, RAG 跨 source 查询成本高
- 按 **文件类型**切 (all_specs.md + all_terms.md + all_examples.md): 语义跨度过大, 单 source 内异质信息混淆 citation
- 按 **页码/size** 均分: 更糟糕 — 跨 domain 边界随机切断

**正确做法** (NotebookLM v2 实测 PASS):
> **按 concept 聚合** — "events_ae" + "findings_lb_quantitative" + "trial_design_ta_te_tv" 这类 concept-level bucket. 每 bucket 内部 domain/spec/assumptions/examples/terminology **同 concept 合并**, bucket 间 concept **正交**.

**验证结果**:
- NotebookLM 42 bucket × 63 domain × 176 Req = ∅ gap (A4 结构级 PASS)
- 语义级 P3.4.5 CONDITIONAL_PASS 8.5/10 (语义 10/10 顶阈值 + citation 7/10)
- P3.4 indexing smoke 10/10 顶阈值 (每 bucket metadata header 帮 citation 反查)

**通用规则** (写入 `05_solution.md`):
1. 先按用户**问答场景**而非物理文件分类, 列 concept 清单 (events / findings / timing / CT / relationships / trial design ...)
2. 每 concept 一个 bucket, 跨 domain 聚合所有相关源文件
3. bucket 边界原则: **正交** (一个源文件属且仅属一个 concept bucket, 无重复无遗漏)
4. 每 bucket 顶部加 "source metadata header" (domain list / key topics) 便于 citation 反查
5. **对比不采用 concept cluster 的情况**: 源数 ≤ 20 且 无跨 domain 聚合需求 (如 ChatGPT 20 硬限), 可按 batch 1 (spec+CT) + batch 2 (chapters+examples) 两轴分

**验收**: Q1 红线 (Req 变量 ∅ gap) 结构级 + 语义级双锚

---

### 补丁 17 (MEDIUM) — Rule A N 阈值建议矩阵 + category error 警示

**来源**: 
- NotebookLM `docs/RETROSPECTIVE.md` §2 G-NBL-2 "P3.8 Rule A 独立抽检 N 未在 PLAN §6 明示"
- NotebookLM reviewer Finding #3 "meta-evidence trace ≠ N 独立样本抽检 category error"

**适用维度**: `_template/02_workflow.md` Rule A 执行 + `_template/06_review.md` 审查规则

**问题 1 (N 阈值矩阵)**: Rule A 原文 "压缩率 >50% 必 N 样本独立抽检, N 写进 PLAN" 未定 N 具体数. 不同压缩率应有不同 N:

**建议矩阵** (写入 `02_workflow.md`):

| 压缩率 | N 建议 | 理由 |
|--------|--------|------|
| 50-70% | N ≥ 3 | 结构级 ∅ gap + 3 样本独立抽检足够 catch 粗粒度错 |
| 70-85% | N ≥ 5 (50%) | 压缩越高 risk 越大, 5 样本覆盖关键维度 |
| ≥ 85% | N ≥ 7 或全覆盖 | NotebookLM 86% 压缩实际只抽 3/10 (30%) 在边缘, reviewer 已 flag |

**执行面** (写入 `06_review.md`):
- N 写进 PLAN §XX Task (非事后补登)
- 独立抽检样本必与 writer 抽过的**不重合**
- 独立 reviewer (非 writer 自审) 审抽检结果

**问题 2 (category error 警示)**: 多 retro 实践中出现 "meta-evidence trace 当 Rule A" 的类别错误 — retro trace 前序产物 (如 A4 ∅ gap audit / P3.4.5 语义级) 作 evidence base, 这是**合规**但**不等于** Rule A 严格意义的 "N 独立样本抽检 (N 写进 PLAN, 独立抽新样本审)".

**警示文本** (写入 `06_review.md` Rule A 章节, 复制粘贴备用):
> **Rule A 合规 vs meta-evidence trace 的 category 差异**: trace 前序产物 (如 ∅ gap audit / 语义级审) 证明 "已有 evidence 闭合", N 独立抽检证明 "新样本再打一次也稳". 两者**正交互补**, **不能互替**. Retro 若仅列 trace 不说 "N 独立抽检未做", 容易在 reviewer category error 上被抓.

**验证**:
- NotebookLM Phase 5 retro §6 Rule A 已补 category error 承认 (同跨 4 retro 28th reviewer F3 fix)
- 本补丁把这条**前置到范本**, 避免未来新平台重踩

---

### 补丁 18 (LOW) — in-KB-only 架构优势 vs prompt-level anchor

**来源**: NotebookLM `docs/RETROSPECTIVE.md` §1 R-NBL-6 "smoke v4 AHP × 3 全 PASS+ 最强 (in-KB-only 天然反虚构优势)"

**适用维度**: `_template/00_platform_profile.md` §G 边界行为 + `_template/06_review.md` A/B 评估维度

**核心 insight**: 
**Anti-hallucination 有两种实现路径**, 架构优势 ≠ prompt 优势, 互补非替代:

| 路径 | 平台典型 | 机制 | 强弱 |
|------|---------|------|------|
| **架构级 (in-KB-only)** | NotebookLM | 模型被强约束只能从 sources 答, 训练数据 + web 无访问 | AHP 天然 PASS+ 最强 (NotebookLM smoke v4 R1 AHP 3/3, Claude 3/3 含 web/训练补全) |
| **Prompt 级 (anchor)** | ChatGPT / Gemini | System prompt 写 "遇虚构前提先纠错" 类锚点 | 需 prompt 工程, 锚缺就 FAIL (Gemini R1 AHP 0/3 → R2 CO-5 单点修 → 3/3) |
| **混合 (训练 + anchor)** | Claude | 训练数据深度 + prompt 锚补 | 中间偏上 (17/17 但部分题靠 web 补, 不纯架构) |

**写入 `_template/00_platform_profile.md` §G 边界行为**, 新增字段:

```markdown
### G.X Anti-hallucination 机制 (补丁 18)

- [ ] 架构级 in-KB-only (NotebookLM 型)
- [ ] Prompt 级 anchor (ChatGPT/Gemini 型)  
- [ ] 混合 (Claude 型)

**若选 Prompt 级**: A/B 矩阵必含 AHP × 3 (变量虚构 / 跨域虚构 / deprecated 虚构), 阈值 ≥ 67% (2/3) 硬 gate.
**若选架构级**: AHP × 3 仍测, 但预期 PASS+ 最强, 同时记录 "supplemental topics PUNT" 架构限制 (如 NotebookLM Q9 Pinnacle 21).
**若选混合**: 两者兼测, 留意 AHP PASS 是否来自 web/训练 vs prompt 锚.
```

**写入 `_template/06_review.md` A/B 评估维度**:
- A/B 矩阵设计时主 gate + bonus + AHP 三分开判
- AHP 结果按平台架构分类注释 (别误归因)

**验证**: 跨 4 平台 smoke v4 R1 AHP 矩阵 (Claude 3/3 混合 / ChatGPT PARTIAL prompt / Gemini R1 0/3 prompt 锚缺→R2 3/3 / NotebookLM 3/3 PASS+ 最强架构级)

---

### 补丁 19 (LOW) — Citation dropout T2 题型偏向观察

**来源**: NotebookLM `docs/RETROSPECTIVE.md` §2 G-NBL-5 "F-3 citation dropout T2 题型偏向 (系统性弱点)"

**适用维度**: `_template/06_review.md` A/B 评分规则 + 系统性弱点记录章节

**现象**: NotebookLM (source-grounded only 架构) 在 **T2 题型 (业务场景 / 举例类)** 上 **citation 数明显低于 T1 (事实查询类)**.

**数据**:
- P3.4.5 语义级 N=10: 语义 10/10 顶阈值 + citation **7/10** (偏低)
- P3.8 smoke v3 Q1-Q10: T1 题 citation 平均 ≥ 10, T2 题 citation 3-5

**根因**: 业务场景 T2 题的 "source 支撑" 是 **spread across multiple bucket** 的 inference, 不是单一引文可覆盖; NotebookLM 倾向"答语义正确但省 inline cite".

**处置选项** (写入 `_template/06_review.md` 评分规则):

1. **A/B 评分不扣 T2 citation** (NotebookLM 本项目做法): 语义等价即 PASS, citation 缺不减分, 但在 retro/review 记录"系统性弱点"
2. **调 Custom mode instructions.md 加"业务例后强制 cite source"规则**: 占 ~300 char, 未实测效果
3. **报告给平台提 feature request**: 超项目 scope

**建议**: 本补丁优先采用**选项 1** (最小干预) + 在 A/B 评分规则注明 "T2 citation dropout 系统性弱点, 不扣语义分", 记录观察数据. 选项 2 作 ICEBOX 备用.

**写入 `_template/06_review.md` A/B 评分章节**:

```markdown
### T2 题型 citation 豁免 (补丁 19)

业务场景/举例类 T2 题若答**语义正确**但 citation 数 **< T1 题均值**, 不扣分 (系统性现象非单题失误). 在 retro §缺口 登记作平台系统性弱点 (如 NotebookLM G-NBL-5 / F-3).
```

**验证**: NotebookLM P3.4.5 评分规则已 embed 此豁免, smoke v3 A/B 评分规则同 (`dev/evidence/smoke_v3_results.md` 说明).

---

## 补丁应用路径 (未来新平台部署)

**新平台起步**:
1. `cp -r _template/* <new_platform>/_spec/`
2. 读 `PATCHES.md` (本文件) 了解已吸收补丁
3. 起草 PLAN 时 embed 补丁 16-19 (还是新候选状态, 视平台架构调整)
4. 若发现本范本还有新缺陷, 在平台 retro §4 加候选补丁 20+, sign-off 时再合入

**补丁升 stable 的门槛**:
- 至少 **2 个独立项目**证据
- 至少 **1 次跨平台 cross-check**
- 用户 ack

**补丁 16-19 当前状态**: 🟡 单平台 (NotebookLM) 证据, 待**第 2 平台 apply 后**升 stable (APPLIED).

---

## 补丁合入范本原文的操作清单 (post-ack to-do)

用户 ack 本 PATCHES.md 后, 按此清单把 16-19 内容合入对应 `0N_*.md` 原文件:

- [ ] 补丁 16 (concept cluster): `05_solution.md` 内容策略章节加 "concept cluster 排布原则" 小节 + 示例
- [ ] 补丁 17 (Rule A N 阈值 + category error): `02_workflow.md` Rule A 执行段加 "N 阈值建议矩阵" + `06_review.md` Rule A 章节加 "category error 警示"
- [ ] 补丁 18 (in-KB-only vs prompt anchor): `00_platform_profile.md` §G 新增字段 + `06_review.md` A/B 维度说明
- [ ] 补丁 19 (T2 citation 豁免): `06_review.md` A/B 评分章节新增 "T2 citation dropout 豁免" 段

**合入原则**: 不大改已有文件结构, 以"新增小节"形式追加, 保持范本向后兼容.

---

*PATCHES.md v1.0 2026-04-24 晚. NotebookLM async lane Phase 5 SIGN-OFF 同批产出. 跨 4 retro §4 "10 补丁候选" 的物化版本 — 10a/10b.1/10b.2/11a/11b/11c/12/13/14/15 已 APPLIED, 16-19 🟡 NEW candidate 待第 2 平台印证后升 stable.*
