# NotebookLM Studio 三件套 — Post-Project ICEBOX 触发 Handoff

> **触发时间**: 2026-04-24 晚 (Daisy 主动触发, Phase 5 SIGN-OFF 之后)
> **状态**: 🟢 **TRIGGERED — Daisy 在其他终端实操 lane** (不污染主 retrospective)
> **上游 trigger**: PLAN §10 "Post-project ICEBOX" 重开流程 + RETROSPECTIVE §7.5 ICEBOX 条款
> **归档原则** (Rule B + PLAN §10): 本 lane 产物回灌主 retro Appendix, 不重写主 retro 正文
> **不污染主 retrospective**: 本 lane 所有新增文件限定在 `notebooklm/post_project_icebox/` 目录, 主 retro (`docs/RETROSPECTIVE.md` v1.0 FINAL) **不改**; 评估 finding 统一作 **Appendix C** (新增章节) 回灌

---

## §0 前置声明

### 为什么触发 ICEBOX

用户 2026-04-22 PM ack 方案 A+保留时决策 Studio 三件套 (P3.5 Audio Overview / P3.6 Mind Map / P3.7 Study Guide) 挪 post-project optional. 归因:
- 无跨 4 平台对比价值 (Claude/ChatGPT/Gemini 无等价功能)
- 问答维度 (P3.4/P3.4.5/P3.8/P3.9) 才是跨平台核心
- 全项目收束后小概率回头精雕

**2026-04-24 晚 Daisy 主动触发** — 用户判定此时有精力 + 无新优先级, 决定做 Studio 三件套. 触发路径合 PLAN §10 正式流程 (用户主动提出 "回头精雕 NotebookLM Studio 三件套").

### 负外部性 (已在主 retro D-NBL-2 PARTIAL 负外部性段记录)

ICEBOX 触发前的关键担忧: "ICEBOX 触发条件 weak → 实际可能永不做". Daisy 触发本 lane 直接**证伪**此负外部性, 实际路径: Phase 5 sign-off (2026-04-24 晚) → ICEBOX 同晚触发 (无拖延).

### 本 handoff 的适用性

- **Writer**: Daisy 在**其他终端** (Chrome MCP / NotebookLM Web UI 实操) 生成 3 类产物
- **Reviewer**: 本 session (主 session 2026-04-24 晚) **暂不做 reviewer**, 等 Daisy 生成产物后按 Rule D 派独立 subagent_type 审 (候选见 §5)
- **本文件自身**: 主 session writer (非 subagent) 起草 — 与主 retro writer 同范式

---

## §1 P3.5 Audio Overview × 3 (Deep Dive podcast)

### 1.1 任务定义 (复用 PLAN §6 P3.5 + §3.5 原设计)

生成 3 期 Deep Dive 长 podcast, 每期 30-45 min, 主题分化:

| # | 主题 | 建议 source 复用 | 时长目标 |
|---|------|-----------------|---------|
| Audio-1 | **SAFETY group** (安全性 domain 族: AE / CE / MH / DS / DD / HO) | bucket 07-08 events_* + bucket 03 dm 部分 | 30-45 min |
| Audio-2 | **EFFICACY group** (疗效 domain 族: FA / QS / RS / PR / EG / VS / VS + 相关 timing) | bucket 13-16 findings_vitals / findings_ecg / qs / fa + bucket 23-25 timing | 30-45 min |
| Audio-3 | **PK group** (药代 domain 族: PC / PP / EX / CM 剂量信息 + ARM + EPOCH) | bucket 06 ex / bucket 11 pc_pp / bucket 26 trial_design_ta | 30-45 min |

### 1.2 操作步骤 (Daisy 侧 NotebookLM Web UI)

1. 登 [notebooklm.google.com](https://notebooklm.google.com), 打开 "SDTM Knowledge Base" notebook (42 sources, Custom mode instructions.md 已贴)
2. 右侧 **Studio** panel → **Audio Overview** → **Customize** / "Deep Dive" 模式
3. **Audio-1 prompt 建议** (粘到 Customize 框):
   > "Generate a 30-45 min Deep Dive podcast covering SDTM Safety domain family (Adverse Events AE, Clinical Events CE, Medical History MH, Disposition DS, Death Details DD, Healthcare Encounters HO). Focus on: (a) domain-level structure and key Req variables; (b) cross-domain relationships via RELREC; (c) SAE/死亡事件的跨域对齐 (AE+DS+DM+DD + RELREC); (d) AESER Core=Exp 非 Req 这类高频易错锚点. Aim for 2-host conversational style, not monologue. Cite source files inline when discussing specific variables."
4. 点 "**Generate**", 等 5-15 min (per-day 20 audio cap 内充裕)
5. **生成后立即下载** 或 **stream 回听** — NotebookLM Audio 在 Studio 持久化, 但建议本地 mp3 存一份作 Rule B evidence
6. **重复 Audio-2 / Audio-3**, 每期独立 prompt

### 1.3 评估标准 (复用 PLAN §7 U1/U2 原定义)

| # | 题 | 评估方式 | PASS 标准 |
|---|---|---------|----------|
| U1 | Audio-1 SAFETY fidelity (高覆盖期) | 抽听 15 min, 勾事实错误 | ≤3 错误 PASS |
| U2 | Audio-3 PK fidelity (边界期 — PK domain 数少, 测边界) | 抽听 10 min | ≤2 错误 PASS |

**Audio-2 EFFICACY** 不在原 U1/U2 评估范围, 作**增量参考** (非 gate, 记录用户主观 ≤5 行感受).

### 1.4 事实错误类型 (抽听时 check list)

- ❌ 变量名错 (如 AESER → AESR, LBNRIND → LBCLIND)
- ❌ Core 属性错 (如 AESER 答成 Req 非 Exp)
- ❌ domain class 错 (如 CE 归 Events 没错, 但"CE 是 Findings" 就错)
- ❌ codelist 值遗漏 (如 NY 答成 Y/N 缺 U)
- ❌ 跨域关系错 (如 RELREC 三件套错位)
- ❌ 虚构外部资源 (超 42 sources 边界但未声明 "未收录")
- ✅ **自我纠错**: Audio 中途自发修正前句 (这是 PASS+ 表现, 扣负分不给, 加分给 0.5)

---

## §2 P3.6 Mind Map + 跨域关系验证

### 2.1 任务定义 (复用 PLAN §6 P3.6 + §3.5 原设计)

在 notebook 内生成 Mind Map, **63 domain 跨域关系全景图**, 优先回答:
- "X domain 依赖哪些? Y domain 被哪些引用?"
- RELREC / RELSPEC / RELSUB 三件套的覆盖完整性
- SUPPQUAL extension pattern 的 63 domain 覆盖

### 2.2 操作步骤

1. notebook 右侧 **Studio** → **Mind Map** → **Generate**
2. 等生成 (通常 < 5 min)
3. **导出 PNG** (Studio panel 通常有 download 按钮)
4. 本地存一份作 Rule B evidence

### 2.3 评估标准 (复用 PLAN §7 U3/U4 原定义)

| # | 题 | 评估方式 | PASS 标准 |
|---|---|---------|----------|
| U3 | Mind Map coverage (RELREC 关系) | 查 "RELREC 关系" 是否覆盖所有会出现 RELREC 的 domain (AE/CM/MH/DS 等 10+) | ≥9/10 核心 domain 命中 PASS |
| U4 | Mind Map coverage (SUPPQUAL 扩展) | 查 "SUPPQUAL 扩展" 是否覆盖所有 63 domain 的 SUPP-- pattern | ≥80% 有 SUPP 例的 domain 有标注 PASS |

### 2.4 checklist 对照基线

- **RELREC 常见 10+ domain**: AE / CE / MH / CM / EX / SU / PR / DS / HO / ML / DA (药物关联场景) — 对照 Mind Map 看多少命中
- **SUPPQUAL 覆盖 SDTMIG v3.4 scope**: Events (AE/CE/MH/...) + Findings (FA/QS/RS/...) + Interventions (CM/EX/...) + DM + SV — 共 ~50 domain 典型含 SUPP 例

### 2.5 Mind Map 常见失败模式

- 孤岛 domain (如 Trial Design 族 TA/TE/TV 与业务域无连线)
- RELREC 连线标签缺失 (只连不注释)
- SUPPQUAL pattern 只标 AE 一个 domain (漏 63 中大部分)

---

## §3 P3.7 Study Guide × 3

### 3.1 任务定义 (复用 PLAN §6 P3.7 + §3.5 原设计)

生成 3 份 Study Guide (Socratic 引导), 每份 1 domain:

| # | Study Guide | 覆盖层 | 建议 prompt 内容 |
|---|-------------|--------|------------------|
| SG-1 | **AE domain** Study Guide | Standard → IG → Examples 三层 | "Create a Socratic Study Guide for SDTM AE (Adverse Events) domain. Cover: (1) Standard-level structure (Topic AETERM + Qualifier AESER Core=Exp + Timing); (2) IG-level rules (ch04 general assumptions + ch08 SUPPAE); (3) Example-level data table (one SAE subject cross-domain AE+DS+DM+DD)." |
| SG-2 | **LB domain** Study Guide | Standard → IG → Examples | LB Quantitative vs Qualitative / LBCAT / LBTESTCD C65047 / LBNRIND 4 值 / partial datetime / baseline flag LBBLFL |
| SG-3 | **CM domain** Study Guide | Standard → IG → Examples | CMTRT (Topic) + CMINDC (indication, 非 CMTRT 融合) + SUPPCM Other-specify 工作流 + CMDOSE/CMDOSU + RELREC to AE |

### 3.2 操作步骤

1. notebook 右侧 **Studio** → **Study Guide** → **Customize**
2. 贴对应 prompt
3. Generate, 等 5-10 min
4. 通常 Study Guide 格式: 10-20 Socratic 问题 + reference answers
5. 本地存 .md / .pdf 作 evidence

### 3.3 评估标准 (复用 PLAN §7 U5 原定义)

| # | 题 | 评估方式 | PASS 标准 |
|---|---|---------|----------|
| U5 | Study Guide 分层 (以 SG-1 AE 为例) | 检查覆盖 Standard → IG → Examples 三层 | 三层齐全 PASS |

**SG-2 LB / SG-3 CM** 原 U5 题不评估, 作增量 (非 gate, 仅记录主观感受).

### 3.4 分层标志

- **Standard 层**: 域结构 / Topic / Qualifier / Role / Core 属性 / Variable table 完整
- **IG 层**: SDTMIG v3.4 §4.X / §8.X / §10.X 章节引用 + business rules (如 AE 升 SAE 规则)
- **Example 层**: ≥ 1 具体数据表 (subject 行 + 变量列值填) 或 narrative 案例

---

## §4 per-day rate limit 约束 (NotebookLM Pro)

- **Audio ≤ 20/day**: 3 Audio 单日充裕, retry 预算余 17
- **Chat ≤ 500/day**: Study Guide 和 Mind Map 走 chat 通道, 每次 ~1-3 chat call, 不 hit cap
- **Source 上限不变**: 42/300, 不需要加 source

若 Audio-1 生成失败 retry → 按 Rule B 归档:
- 新增文件: `notebooklm/post_project_icebox/failures/audio_1_attempt_1.md`
- 记: 输入 (prompt 原文) / 产物 (retry 触发的 error 截图或 "Failed to generate") / 技术判定 / 业务判定 / 下一 attempt 输入调整

---

## §5 Reviewer 派遣 (Rule D async lane, 独立于主 retro reviewer)

Daisy 完成 Studio 三件套生成 + U1-U5 自评后, 主 session 派独立 reviewer 审本 ICEBOX lane 产物.

### Reviewer 候选 (避免 self-review)

已 burned subagent_type (Rule D 全局 29-slot roster, 跨 4 + NotebookLM async + 本次主 retro):
- #1 general-purpose / #2 verifier (reuse in R2 → #27) / #3 executor / #4 critic (reuse in Phase 5 28th + async lane 独审 → 本 retro v0.2)
- #5 planner / #6 analyst / #7 code-architect (reuse #21) / #8 code-reviewer (reuse #26)
- #9 architect / #10 scientist (reuse #14)
- #11 feature-dev:code-reviewer (reuse #25 P3.8 reviewer)
- #10 debugger / #11 (original) feature-dev:code-reviewer / #12 comment-analyzer / #13 pr-test-analyzer
- #15 superpowers:code-reviewer / #16 tracer / #17 test-engineer
- #18 silent-failure-hunter / #19 security-reviewer / #20 type-design-analyzer
- #22 oh-my-claudecode:code-reviewer / #23 code-explorer
- #24 document-specialist

### Studio 三件套 ICEBOX lane reviewer 候选 (未 burned 或 reuse 新 evidence)

- 🎯 **`oh-my-claudecode:designer`** (UI/UX 视角 — 适合 Audio 对话质量 + Mind Map 布局 + Study Guide 分层审美)
- 🎯 **`pr-review-toolkit:comment-analyzer`** reuse #12 (for Study Guide text 分层 + Audio transcript 事实核对, 不同 evidence)
- 🎯 **`oh-my-claudecode:writer`** (Writer mode reviewer, 对 Audio 2-host conversational 风格 + Study Guide Socratic 引导质量敏感)

**推荐**: `oh-my-claudecode:designer` (全新 subagent_type, Rule D 合规 — 本 lifecycle 从未派过).

### Reviewer prompt 骨架

```
你是 NotebookLM Studio 三件套 ICEBOX lane 独立 reviewer. 
Context: 主项目 Phase 5 SIGN-OFF 已闭环 (2026-04-24), ICEBOX 在同日触发.
你审的产物:
- Daisy 在 NotebookLM Web UI 生成的 Audio-1/2/3 (有 stream/下载, 或 transcript 文本)
- Mind Map PNG + domain 覆盖 checklist 对照
- Study Guide × 3 (.md / .pdf)
- Daisy 自评 U1-U5 结果 (PASS/FAIL + 理由)

评估:
- U1-U5 阈值判断 (事实错误数 / domain 命中率 / 分层完整)
- Studio 产物的跨 source 信息组织质量 (是否真正体现 42 bucket concept cluster 优势)
- 新补丁候选 (若有) — 登入 PATCHES.md §新候选 20+

输出: final message markdown, PASS / CONDITIONAL_PASS / FAIL + 5-10 行摘要. 父 session 手工落档.
```

---

## §6 回灌主 retro Appendix (不改正文)

Daisy 完成 + reviewer APPROVE 后, 主 session 把 ICEBOX lane 成果作 **Appendix C** 加到主 retro `docs/RETROSPECTIVE.md` 末尾:

```markdown
## Appendix C — Post-project ICEBOX Studio 三件套成果 (触发 2026-04-24 晚)

> **触发路径**: Phase 5 SIGN-OFF 同晚 Daisy 主动触发 (证伪 D-NBL-2 "ICEBOX 触发条件 weak 负外部性" 的担忧)
> **产物**: Audio × 3 / Mind Map / Study Guide × 3
> **Evaluation**: U1-U5 [PASS/FAIL]
> **Reviewer**: [subagent_type], [verdict]
> **新补丁候选** (若有): 补丁 20+ 登入 `_template/PATCHES.md`

[具体 U1-U5 结果 + 观察 + 新发现]
```

**主 retro v1.0 FINAL 正文不改** — 仅追加 Appendix C. 版本升 v1.1-appendix 或保持 v1.0 (视改动粒度, 建议加 v1.1 中间态 audit trail).

---

## §7 下一步 (Daisy 侧)

Daisy 按顺序在其他终端实操:

1. **§1.2 Audio-1 SAFETY** → 生成 + 抽听 15 min 记 U1 事实错误数 → 若 ≤ 3 PASS
2. **§1.2 Audio-3 PK** → 生成 + 抽听 10 min 记 U2 事实错误数 → 若 ≤ 2 PASS
3. **§1.2 Audio-2 EFFICACY** (增量, 非 gate)
4. **§2 Mind Map** → 导出 PNG + 对照 §2.4 checklist → 记 U3/U4 命中率
5. **§3 Study Guide × 3** → 生成 + 读 SG-1 AE 记 U5 分层 PASS/FAIL → SG-2/SG-3 增量
6. Daisy 把 **U1-U5 结果 + 主观感受 5-10 行** 发给主 session
7. 主 session 派 §5 reviewer → 审完 → 回灌 §6 Appendix C

**无时间压力** — 本 lane 完全 optional, Daisy 随时可暂停 / 永久 ICEBOX. 主 retro v1.0 FINAL 不依赖.

---

## §8 相关文档

| 文件 | 路径 | 用途 |
|------|------|------|
| 主 retro (不改) | `docs/RETROSPECTIVE.md` v1.0 FINAL | D-NBL-2 + §7.5 ICEBOX 条款 + Appendix C 回灌点 |
| 跨 4 retro (不改) | `../retrospectives/PHASE5_RETROSPECTIVE.md` v1.0 FINAL | 本 lane 不涉跨 4, 仅作参考 |
| PLAN (不改) | `docs/PLAN.md` §10 Post-project ICEBOX + §6 P3.5/P3.6/P3.7 原 Task + §7 U1-U5 原评估 | 任务定义源 |
| UPLOAD_TUTORIAL (不改) | `current/UPLOAD_TUTORIAL.md` §10.3 ICEBOX | Daisy 实操前快速 reference (如何打开 Studio) |
| _template PATCHES (可能追加) | `../_template/PATCHES.md` | 本 lane 若产出补丁 20+, 登在此 |
| 本 handoff | 本文件 | 独立 lane trigger + 全手顺 |
| 本 lane state tracker (可选) | `notebooklm/post_project_icebox/STATE.md` | 若 Daisy 想 log 生成进度 |
| 本 lane failures (Rule B) | `notebooklm/post_project_icebox/failures/` | retry 归档 |

---

*v1.0 FINAL 2026-04-24 晚. Daisy 主动触发 Studio 三件套 post-project ICEBOX lane. 主 session writer 起草 handoff (单独 lane 不污染主 retro). Daisy 在其他终端实操生成产物 → 主 session 派 §5 reviewer → 回灌 §6 Appendix C. 本 handoff 是 PLAN §10 "Post-project ICEBOX 重开流程" 的物化 instance.*
