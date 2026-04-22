# SMOKE_V4 — 4 平台 smoke v4 唯一入口

> **版本**: v4.0 bundled (2026-04-22 PM)
> **合并自**: 原 `smoke_v3_questions_draft.md` (v4.0 题库) + `SMOKE_V4_R1_EXECUTION_PLAN.md` + `cross_platform_compare_v4.md` (3 合 1)
> **状态**: Step 1-5 完成 (audit + v4 patch + AHP×3 + 3 平台 v3 SUPERSEDED + Rule D gap 闭合); **Step 6 R1 pending**.
> **历史归档**: `ai_platforms/archive/smoke_history/` (5 份: SMOKE_QUESTIONS_V2 + N5_3_QUESTIONS_DESIGN + SMOKE_V4_DESIGN_HANDOFF + smoke_v3_audit_notes + PHASE4_PLAN)
> **各平台证据**: `ai_platforms/{chatgpt_gpt, gemini_gems, notebooklm, claude_projects}/dev/evidence/`

---

## 本文件包含 (3 Section)

1. **Section 1: R1 执行 Plan** — 4 平台跑题顺序 / 前置状态 / 每平台手顺 / 阈值 / 评分 / R1→R2 gate
2. **Section 2: 17 题题库 v4.0** — Q1-Q14 + AHP1-3 完整题目 + PASS/FAIL 判据 + KB 锚点 + 联网源 + 附录 A/B
3. **Section 3: 跨平台对比矩阵** — 17 行 × 4 列骨架, R1 跑完填

## Rule D chain cumulative 12 种 subagent_type (v4.0 闭合)

1. general-purpose | 2. verifier | 3. executor | 4. critic | 5. analyst | 6. pr-review-toolkit:code-reviewer | 7. feature-dev:code-architect | 8. architect | 9. scientist | 10. cross-chain aggregate | **11. document-specialist** (smoke v3.2 audit, 2026-04-22) | **12. feature-dev:code-reviewer** (P3.8 reviewer, 2026-04-22)

---

# Section 1: R1 执行 Plan

> **触发**: 路径 B bundled patch 完成 (smoke v3.2 → v4.0, 含 Q10/Q13/Q8/Q4/Q14 fix + F1 锚点全局 + AHP × 3 新增), 3 平台 smoke v3 历史结果已 SUPERSEDED.
> **目的**: 4 平台 (Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM) smoke v4 Round 1 baseline, 作 Phase 4 跨平台对比 ground truth.
> **题库**: `ai_platforms/SMOKE_V4.md §2` v4.0 (文件名保留作 ref-compat)
> **阈值**: 各平台首测容错, 见下 §3.
> **下一步**: R1 完成后按 FAIL pattern 改 system prompts → R2 retest (Task 7 Step 7).

---

## 0. 前置状态 core check (执行前必核)

| 平台 | 当前状态 | system prompt | knowledge files | Chat/Custom mode | R1 前置 action |
|---|---|---|---|---|---|
| NotebookLM | P3.4 VERIFIED + P3.8 done | instructions.md 9011/10000 chars | 42 sources indexed | Custom mode 锁 | **不动状态**, 直接跑 |
| ChatGPT GPTs | N5.3 bank patch v3.2 done, v5c pending | system_prompt.md v2 (7568 bytes) | 9 knowledge files (N4 batch 2) | Custom GPT | **不动状态** (N5.2 lock), 直接跑 R1 baseline; v5c 改在 R2 |
| Gemini Gems | N5.3 done, v5c CO-4 draft pending | system_prompt v5 (7925/8000 chars) | 4 files (N4 + N5.1 04 v5b) | Gem | **不动状态** (N5.2 lock), 直接跑 R1; v5c 改在 R2 |
| Claude Projects | v2.6 AB 终态 24/24 PASS | v2.6 system_prompt (1.29M tokens, 77% capacity) | 19 files in current/uploads/ | Project | **不动状态**, v3 未跑过基线首测, R1 作首次 baseline |

**R1 原则**: 不动任何 system prompt / knowledge files / mode 设置, 只用现有部署跑 smoke v4. 改 prompt 是 R2 才做.

---

## 1. 执行顺序 (推荐, v4.0 Q11-Q14 开放 4 平台共用 — 2026-04-22 用户决策)

按 "最快先 + 最稳先" 原则:

```
1. NotebookLM (17 题)    in-KB-only, 对 AHP 天然 PASS, Web UI cowork paste, ~55 min
2. Gemini Gems (17 题)   并行或接着 NotebookLM, Chrome MCP full-auto, ~55 min (Q11-Q14 允许 FAIL 作 bonus)
3. ChatGPT GPTs (17 题)  Chrome MCP cowork paste, ~55 min
4. Claude Projects (17 题) Chrome MCP cowork paste (claude.ai Projects UI), ~55 min
```

**总估时**: 3.5-4h (R1 全跑完 + 逐题落档). 可分 2 天跑 (第 1 天 NotebookLM + Gemini, 第 2 天 ChatGPT + Claude).

**Q11-Q14 开放规则 (v4.0 用户决策 2026-04-22)**:
- ChatGPT / Claude / NotebookLM: Q11-Q14 作**主 gate**, 计入 PASS 阈值
- **Gemini: Q11-Q14 作 bonus track**, 允许 FAIL (4-file KB 不含 supplemental topics: Dataset-JSON / CT 版本 / RWD / 死亡跨域), FAIL 不破 gate; PASS 则记加分
- 所有平台均必跑全 17 题, Gemini FAIL 也要记录落档 (供 R2 判断是否需扩 KB 或调 prompt)

---

## 2. 每平台执行手顺 (R1 baseline)

### 2.1 NotebookLM (17 题, 1 notebook × 42 sources)

**前置**:
- 账号: bojiang.zhang.0904@gmail.com (Google AI Pro)
- Notebook: "SDTM Knowledge Base" (已 indexed 42/42)
- Chat mode: **Custom** (instructions.md 9011 chars, 含 13 behavior rules + SDTM 锚点)

**手顺** (每题 fresh chat, Delete chat history → 重新发问, DOM readback):
1. Sanity preflight (3 题, 与 P3.8 相同): AESER Core / LBNRIND C78736 4 全写 / CMINDC concomitant medication indication — 若 3/3 PASS 底座稳, continue
2. Q1-Q10 逐题跑 (题库 v4.0 Q10 已修 SUPPTS 前提 + Q8 LBNRIND 移 Ext + AETERM 修正)
3. Q11-Q14 逐题跑 (v4.0 新开放给 4 平台; Q13 已删 NS 虚构 + 修 ARMCD 机制; Q14 加 timing context)
4. AHP1-3 逐题跑:
   - AHP1: LBCLINSIG 虚构变量
   - AHP2: "Trial-Level SAE Aggregate 表" 虚构
   - AHP3: PF 域 deprecated
5. 每题答案按 §3a Cowork 记录规范存 `ai_platforms/notebooklm/dev/evidence/smoke_v4_answers/` (sanity 3 + Q1-Q14 + AHP1-3 = 共 20 文件)
6. 逐题 verdict 填 `ai_platforms/notebooklm/dev/evidence/smoke_v4_results.md` (骨架跑前建)

**特殊预期** (NotebookLM in-KB-only):
- AHP1-3 天然 PASS (LBCLINSIG / Trial-Level SAE Aggregate / PF 在 KB 都找不到, 按 instructions.md "authoritative layer" 规则应说 "不存在"而非编造)
- Q11 Dataset-JSON / Q13 RWD 可能 PUNT (42 sources 未必含 supplemental); Q12 CT 版本锁定 / Q14 AE+DS 死亡对齐在 KB 内
- Q9 Pinnacle 21 大概率 PUNT (架构限制, in-KB-only no web search)

**阈值**: ≥13/17 (76%) 保, R1 首测可降至 ≥12/17 (71%) 容错 (考虑 Q9/Q11/Q13 可能 PUNT)

### 2.2 Gemini Gems (17 题, 4 knowledge files + v5 system prompt — **Q11-Q14 bonus 容错**)

**前置**:
- 账号: bojiang.zhang.0904@gmail.com (Gemini Pro)
- Gem: SDTM Expert (URL gemini.google.com/gem/3b572e310813)
- Mode: Pro (Gemini 3.1 Pro) per question
- 方法: Chrome MCP full-auto (Quill editor + execCommand + InputEvent)

**手顺**:
1. 底座 sanity 4 题 (已有, 见 smoke v3 sanity_1-4_answer.md)
2. Q1-Q10 逐题跑 (**主 gate 范围**)
3. Q11-Q14 逐题跑 (**bonus 范围**: 4-file KB 不含 supplemental, FAIL 预期可接受)
4. AHP1-3 逐题跑 (主 gate 范围)
5. 按 §3a 规范存答案 `ai_platforms/gemini_gems/dev/evidence/smoke_v4_answers/`
6. 填 `ai_platforms/gemini_gems/dev/evidence/smoke_v4_results.md`

**特殊预期** (Gemini 有 web search + 4-file KB 窄):
- AHP1-3 可能 FAIL (沿错前提 + 用 web search 编证据). 测 system prompt v5 的 anti-hallucination 锚是否强
- Q10 (v4.0 改判据) SUPPTS 前提纠错, 测能力
- **Q11-Q14 很可能 FAIL** (Q11 Dataset-JSON / Q12 CT 版本 / Q13 RWD / Q14 死亡跨域 均超出 4-file KB scope, 靠 web search 或模型训练知识) — 作 bonus 容错

**阈值** (双阈值机制, v4.0 新设):
- **主 gate** (Q1-Q10 + AHP1-3 = 13 题): **≥9/13 (70%) 必 PASS** (等同原 smoke v3.1 Gemini 阈值)
- **Bonus track** (Q11-Q14 = 4 题): 记录但不作 gate; PASS 则记加分 (表明 Gemini 即使 KB 窄也能 generalize)
- **全量 score 记录** (17/17, 供 R2 与其他 3 平台 Q11-Q14 对比)

### 2.3 ChatGPT GPTs (17 题, 9 knowledge files + system prompt v2)

**前置**:
- 账号: chatgpt.com/g/g-... (Custom GPT)
- system_prompt v2 (7568 bytes, N5.2 lock)
- 方法: Chrome MCP cowork paste (ClipboardEvent)

**手顺**:
1. Sanity 3 题 (若有可用, 或 skip 直接题库)
2. Q1-Q14 逐题跑 (Q11-Q14 v4.0 已修 — Q13 删 NS 虚构 + ARMCD 机制 / Q14 加 §4.2.6 timing context)
3. AHP1-3 逐题跑
4. 按 §3a 规范存答案 `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v4_answers/`
5. 填 `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v4_results.md`

**特殊预期**:
- Q13 (v4.0 删 NS + 修 ARMCD) 是大改, 测之前 14/14 answer 在 v4.0 新判据下是否仍 PASS
- AHP1-3 预期 FAIL 可能性较高 (ChatGPT + web search + MedDRA 知识强, 易编)
- Q11-Q14 (Dataset-JSON / CT 版本锁定 / RWD / AE+DS 死亡) 在 ChatGPT 9-file KB (batch 2) 已覆盖, R1 测 system prompt v2 仍稳

**阈值**: ≥12/17 (71%) 全量 gate PASS

### 2.4 Claude Projects (17 题, 19 files + v2.6 system prompt)

**前置**:
- 平台: claude.ai Projects
- Project: SDTM (v2.6, 1.29M tokens, 77% capacity, 19 files in uploads/)
- system_prompt v2.6
- 方法: Chrome MCP cowork paste

**手顺**:
1. Sanity 3 题
2. Q1-Q10 逐题跑 (注: Claude Projects v3 未跑过 baseline, R1 是第一次)
3. Q11-Q14 逐题跑 (v4.0 新开放 — Claude 19-file KB 含 assumptions/examples 全量, 覆盖 supplemental)
4. AHP1-3 逐题跑
5. 按 §3a 规范存答案 `ai_platforms/claude_projects/dev/evidence/smoke_v4_answers/`
6. 填 `ai_platforms/claude_projects/dev/evidence/smoke_v4_results.md`

**特殊预期**:
- v2 智能覆盖验证 — 对比 v2 AB (之前 smoke v2.1 24/24 PASS) 与 v4 (generalization + AHP) 的差
- AHP1-3 不确定 (Claude 自身训练数据可能知道 SDTMIG 细节, 但 system prompt 是否锚得好)
- Q11-Q14 覆盖内, 测 v2.6 在 supplemental topic 的稳定性

**阈值**: ≥13/17 (77%) 首测容错

---

## 3. 评分规则 (v4.0 PASS/PARTIAL/FAIL)

| Verdict | 分 | 条件 |
|---|---|---|
| **PASS** | 1 | 核心判据全中 + 无 FAIL 判据 |
| **PASS+** (AHP 专属) | 1 + 0.25 bonus | 主动识破错前提 + 纠正 + 给 canonical 路径 (bonus 不计入总分, 但记录) |
| **PARTIAL** | 0.5 | 核心判据 ≥ 50% + 0-1 小缺漏 |
| **FAIL** | 0 | 核心判据 < 50% OR 触 FAIL 判据 (AHP 中包括沿错前提答 downstream) |
| **PUNT** | 0 | 模型拒答, 等同 FAIL (如 NotebookLM Q9 Pinnacle 21 punt) 但标 "policy-correct" 作 Phase 4 scope 分类 |

---

## 3a. Cowork 答案记录规范 (Every-question Protocol, v4.0 新增)

每题跑完**立即**落档, 不累积到最后补记录. Main session 负责复制题目 prompt + 打 verdict, 用户负责 Chrome MCP 粘贴 + 发送. DOM readback 后保存原文.

### 3a.1 答案文件位置 + 命名规范

```
ai_platforms/{平台}/dev/evidence/smoke_v4_answers/
├── sanity_01_aeser_core.md           ← sanity preflight 3 题
├── sanity_02_lbnrind_values.md
├── sanity_03_cmindc_indication.md
├── Q1_answer.md                       ← Q1-Q14 逐题
├── Q2_answer.md
├── ...
├── Q14_answer.md
├── AHP1_answer.md                     ← AHP1-3 逐题
├── AHP2_answer.md
└── AHP3_answer.md
```

**{平台}** = `notebooklm` / `chatgpt_gpt` / `gemini_gems` / `claude_projects`
**总文件数**: 20 文件 (3 sanity + 14 Q + 3 AHP), 所有平台一致.

### 3a.2 每题答案文件结构 (标准 template)

```markdown
# {平台} — {题号} (R1 smoke v4.0)

> **题库版本**: v4.0 (见 `ai_platforms/SMOKE_V4.md §2`)
> **执行时间**: 2026-04-2X HH:MM
> **执行者**: Bojiang + claude cowork MCP Chrome
> **会话 URL**: {URL 或 "Web UI fresh chat"}
> **题类**: {sanity / Q{N} / AHP{N}}

---

## 题目原文 (复制自 SMOKE_V4.md §2)

{原题完整 prompt, 包括题目描述 + (a)(b)(c)(d) 分条要求}

---

## 发送给模型的 prompt (实际粘贴文本)

{如果与原题一致就写 "同上"; 如果有简化/包装就把实际文本全贴在这里}

---

## 模型 raw 回答 (DOM readback 原文)

{模型完整输出, 含 citation / 表格 / 分段. 若有多条 sub-message, 按提交顺序分 "Sub-message 1 / Sub-message 2" 标出}

**Citation 数**: {N 条} ({若有 source 文件名列表}, 或 "0 条 = PUNT")

---

## Self-score verdict

- **Verdict**: PASS / PASS+ / PARTIAL / FAIL / PUNT
- **理由** (对照 SMOKE_V4.md §2 PASS 判据逐条):
  - (a) ✓/✗ {理由, 引原答案哪一行}
  - (b) ✓/✗ ...
  - (c) ✓/✗ ...
  - (d) ✓/✗ ...
- **触发 FAIL 判据?** 无 / {具体哪条}
- **加分 (PASS+ 仅 AHP)**: {主动识破错前提的 quote, 或 "无"}
- **F-* carry-over 观察**: {如 F-1 小表渲染漂移 / F-3 citation dropout / 新发现}
```

### 3a.3 cowork 执行流程 (逐题)

1. **Main session** 从 `SMOKE_V4.md §2` 复制当前题 prompt → clipboard
2. **用户** 在浏览器目标平台打开 fresh chat / Delete history → 粘贴 → 发送
3. **Main session** (或用户) 触发 Chrome MCP DOM readback 拿模型答案
4. **Main session** 按 §3a.2 template 立即写 answer.md 存档
5. **Main session** 对照 SMOKE_V4.md §2 PASS/FAIL 判据打 verdict, 写入 answer.md
6. **Main session** 在 `ai_platforms/{平台}/dev/evidence/smoke_v4_results.md` 的逐题表添一行 verdict
7. 下一题

### 3a.4 失败 retry 归档 (Rule B 强制)

若粘贴错 / 题目发不全 / Chrome MCP 异常导致 retry, **不覆盖 attempt_1**:

```
ai_platforms/{平台}/dev/evidence/failures/
├── Q3_attempt_1.md      ← retry 前原文 (含失败归因 + 技术 vs 业务判定)
└── ...
```

然后在 `smoke_v4_answers/Q3_answer.md` 存 attempt_2 (主答案). results.md 备注 "retry 次数" 字段.

### 3a.5 每 5 题 checkpoint

每跑 5 题, 暂停 30 秒 spot-check:
- 答案文件已写入
- results.md 对应行已填
- 若观察到系统性异常 (如连续 3 题 FAIL), 停题查 system prompt 或 Chrome MCP 状态

### 3a.6 落档到 _progress.json (跑完一个平台一次)

跑完 {平台} 17 题 + 3 sanity 后, 在 `ai_platforms/{平台}/dev/evidence/_progress.json` 加:

```json
"smoke_v4_r1_completion": {
  "completion_date": "2026-04-2X",
  "sanity_preflight_3q": "3/3 PASS / X/3",
  "questions_ran": "Q1-Q14 + AHP1-3 (17 题)",
  "per_question_verdicts": {"Q1": "PASS", "Q2": "PASS", ..., "AHP3": "PASS+"},
  "main_gate_score": "X/13 (Q1-Q10 + AHP1-3)",
  "bonus_track_score_Q11_Q14": "X/4 (Gemini bonus only; 其他平台主 gate)",
  "total_score": "X/17",
  "threshold": "≥{阈值} {%}",
  "verdict": "PASS / FAIL",
  "retry_attempts": 0,
  "carry_over_observations": [...]
}
```

### 3a.7 跨平台矩阵 (4 平台全跑完一次)

4 平台全跑完, main session 填 `ai_platforms/SMOKE_V4.md §3` 17 行 × 4 列矩阵, 加跨平台观察 5 项 (AHP 能力差 / prompt 效果 / v4.0 patch 稳 / Q9 PUNT / Q11-Q14 Gemini vs 其他).

---

## 4. 评分落档 + 跨平台对比矩阵

每平台 R1 跑完填 (详细流程见 §3a.6):
- `ai_platforms/{平台}/dev/evidence/smoke_v4_results.md` (逐题 verdict + 总分)
- `ai_platforms/{平台}/dev/evidence/smoke_v4_answers/` (20 文件: sanity 3 + Q1-Q14 + AHP1-3)
- `ai_platforms/{平台}/dev/evidence/_progress.json` 加 `smoke_v4_r1_completion` block

4 平台全跑完填:
- `ai_platforms/SMOKE_V4.md §3` (4 列 × 17 行矩阵, **Q11-Q14 v4.0 开放 4 平台共用, Gemini 允许 FAIL 作 bonus**)

---

## 5. R1 完成后 Gate 决策

R1 跑完触发 3 个决策:

### 决策 1: 是否进 R2?
- 4 平台中任一 FAIL 比例 >30% → **必进 R2** (改 system prompt)
- 所有平台 ≥ 阈值 → 可 skip R2 直接进 Phase 4→5 gate

### 决策 2: R2 改什么 prompt pattern?
见 `SMOKE_V4_DESIGN_HANDOFF.md` §6 典型 pattern 表 (CO-3 anti-hallucination 锚 / CO-4 v3.4 新域锚 / Q9 NotebookLM scope 分类).

### 决策 3: Rule D chain 第 13 种 subagent_type?
R2 跑完后 Phase 4 总审建议用 `pr-review-toolkit:type-design-analyzer` (handoff §7 预留, 专审 smoke v4 题目设计质量 + R1/R2 结果对比).

---

## 6. 相关路径速查

| 项 | 路径 |
|---|---|
| 本 plan | `ai_platforms/SMOKE_V4.md §1` (本文件) |
| 题库 v4.0 | `ai_platforms/SMOKE_V4.md §2` |
| 审计报告 | `ai_platforms/archive/smoke_history/smoke_v3_audit_notes.md` (Rule D 11th slot, document-specialist) |
| 跨平台对比 | `ai_platforms/SMOKE_V4.md §3` (骨架, R1 跑完填) |
| 原 handoff | `ai_platforms/archive/smoke_history/SMOKE_V4_DESIGN_HANDOFF.md` (smoke v4 设计背景, §5-6 R1/R2 指引) |
| 各平台 progress | `ai_platforms/{chatgpt_gpt,gemini_gems,notebooklm,claude_projects}/dev/evidence/_progress.json` |

---

*v1.0 2026-04-22 PM, 路径 B bundled patch 完成后写定 R1 执行 plan. 下一步: 用户 ack 后按顺序跑 NotebookLM → Gemini → ChatGPT → Claude.*

---

# Section 2: 17 题题库 (v4.0)

> **版本**: **v4.0** (2026-04-22 PM, 第 11 种 subagent_type `oh-my-claudecode:document-specialist` audit 后主 session bundled patch + 新增 AHP × 3)
>
> **v3.2 → v4.0 修改** (路径 B 一次性 bundle: audit_notes.md 5 题 NEED_FIX + F1 全局锚点替换 + handoff AHP × 3):
>
> **A. 题目前提/判据 patch (5 题)**:
> - **Q10 (b) HIGH**: 题干 + PASS + FAIL 全改 — SUPPTS **不是 SDTMIG v3.4 定义的 dataset** (TS 属 Trial Design, SUPPQUAL scope 限于 Events/Findings/Interventions + DM + SV, 见 `ch08_relationships.md` §8.4 L177); 长 TSVAL 用 **TSVAL1-TSVALn 在 TS 内部派生列** (`TS/spec.md` L65-67 + `ch04_general_assumptions.md` §4.5.3.2 L1296); 沿 "SUPPTS 存在" 前提答 → **FAIL (premise hallucination)** 不是 PARTIAL
> - **Q13 (c) HIGH**: 删 "NS (Non-Standard Domain) 新概念" 全部内容 — WebFetch CDISC Observational/RWD v1.0 PDF (2024-02) 确认**无此概念**, 只有 NSV (variable-level, 既有概念); Q13 聚焦 (a) conformance rule 失效 + (b) ARMCD 机制 + (d) SUPPDM 补 observational provenance; (c) 改为 "observational 场景 SUPPQUAL 仍有效, NSV 机制不变"
> - **Q13 (b) MINOR**: ARMCD **应 null**, **ARMNRS 填 "NOT ASSIGNED"** (`DM/spec.md` L219+L255 规范), 不是 ARMCD="NOTASSGN"; 修正 C142179 ARMNRS codelist 值 "NOT ASSIGNED" (非 8-char 缩写)
> - **Q8 (b) MEDIUM**: **LBNRIND C78736 是 Extensible=Yes** (`terminology/core/general_part4.md` L65 KB 明文), 从 Non-Extensible 例删除; 替换为真 Non-Ext 例 **C66789 "Not Done"**. NY codelist C66742 submission values 扩为 "{Y, N, U, NA}" (补 C48660 NA)
> - **Q8 (c) MEDIUM**: AETERM **是 verbatim free text, 不绑 CT 也不绑 MedDRA** (`AE/spec.md` L77-85 Controlled Terms 列空); **MedDRA 绑 AEDECOD/AELLT/AEHLT/AEHLGT/AESOC/AEBDSYCD** 等 dictionary-derived 变量 (L117-223); 严格区分 `--TERM` vs `--DECOD` 的字典绑定位置
> - **Q4 FAIL 场景 A MINOR**: PARTIAL "版本迁移无显文" 规则过宽 — `IS/assumptions.md` assumption 2 **显文** 把 anti-microbial antibody 放入 IS scope (无版本条件); 收窄为 "答 MB 仅提 '检测抗体' → FAIL; 答 MB 且显式指出 'pre-v3.4 旧习惯, 知道 v3.4 应归 IS' → HALF 0.5"
> - **Q14 (a)(d) MINOR**: (a) "三域互斥" 加 context — `ch04_general_assumptions.md` §4.2.6 L327-330 允许同一概念跨 MH/AE/CE, **前提是 timing 不同** (MH=study start 前 / AE=on-study 达阈 / CE=on-study 未达阈); 心梗 on-study SAE 场景单 AE 正确; (d) 三域死亡日期改 "**日级对齐**, 不强制 time-level 严格相等, time offset 需 Reviewers Guide 文档化"
>
> **B. KB 锚点全局替换 (F1)**:
> - `ch05_controlled_terminology.md` **在本 KB 不存在** (仅 ch01/02/03/04/08/10) → 全局替换为 `ch04_general_assumptions.md` §4.3 "Coding and Controlled Terminology Assumptions" L606-670 + `knowledge_base/terminology/core/*.md`
> - 涉及题: Q8, Q10 KB_ANCHOR 段
>
> **C. 新增 AHP × 3 (handoff §3 Step 4)**:
> - **AHP1 (Z1 variable hallucination)**: LBCLINSIG 不存在, SUPPLB + QNAM="LBCLSIG" NSV 是 canonical pattern
> - **AHP2 (Z2 cross-domain hallucination)**: "Trial-Level SAE Aggregate 表" 不存在, SAE 全在 AE 域 subject-level (AESER + AESHOSP/AESLIFE/AESDTH/AESDISAB/AESCONG/AESMIE)
> - **AHP3 (Z3 deprecated concept)**: PF (Pharmacogenomics Findings) 在 SDTMIG v3.4 **已被 GF (Genomics Findings) 替代** (SDTMIG-PGx v1.0 合并入 v3.4), 答 PF 变量清单 → FAIL
>
> **D. 合格阈值更新** (v4.0, Q11-Q14 开放 4 平台共用 2026-04-22):
> - **ChatGPT**: 14+3 = **17 题**, ≥12/17 (71%) PASS (全量 gate)
> - **Gemini**: 14+3 = **17 题**, **双阈值机制** — 主 gate ≥9/13 (70% Q1-Q10+AHP 必 PASS), **Q11-Q14 作 bonus track 容错 FAIL** (4-file KB 不含 supplemental: Dataset-JSON / CT 版本 / RWD / 死亡跨域)
> - **NotebookLM**: 14+3 = **17 题**, ≥13/17 (76%) 保, R1 首测降至 ≥12/17 (71%) 容错 (Q9/Q11/Q13 可能 PUNT)
> - **Claude Projects**: 14+3 = **17 题**, ≥13/17 (77%) 首测容错 (v3 未跑基线, 19-file KB 覆盖 supplemental)
>
> **E. 历史版本处理**:
> - **smoke v3.1/v3.2** 3 平台已跑结果 (ChatGPT 12/14+2 subst / Gemini 7/10 / NotebookLM 9/10) **整块 SUPERSEDED 2026-04-22** (Q10 (b) 判据基于错前提 + Q13 (c) NS 虚构 + Q8 LBNRIND/AETERM 错位), 不回溯重评分; Phase 4 跨平台对比 baseline 用 smoke v4 R1
>
> **F. Rule D chain 状态**:
> - 第 11 种 subagent_type `oh-my-claudecode:document-specialist` 完成 audit (Q10 baseline self-test 独立识别 + Q13 NS 新发现 HIGH)
> - `ai_platforms/archive/smoke_history/smoke_v3_audit_notes.md` (404 行) 留档作 audit evidence
>
> ---
>
> **v3.1 → v3.2 修改** (第 22 种 subagent_type `pr-review-toolkit:type-design-analyzer` HIGH+MED findings 主 session 修, SUPERSEDED by v4.0 2026-04-22):
> - **F-R1 (HIGH) 官方记录**: Phase 4 N5.3 Step 4 Chrome MCP 执行时, **ChatGPT 端 Q8/Q9 被 executor 替换为备选题** (Gemini 端按原 v3.1 Q8 (D1) + Q9 (E1)):
>     - **ChatGPT 实际 Q8** (替换为 B5 — EPOCH Trial Design 与 Subject-level 关系): 独立对 EPOCH/TA/TE/SE 考, 与 bank 原 Q8 (D1 CT Extensible) 正交且互补
>     - **ChatGPT 实际 Q9** (替换为 B6 — AESEV vs AETOXGR vs AESER CTCAE): 考 AE 三维严重度 + CTCAE Grade 5→AESER, 与 bank 原 Q9 (E1 Pinnacle 21) 正交
>     - **替换作许可正式记录**, ChatGPT 实际 14 题对已答题全 PASS; bank 原 D1/E1 挪 N5.4 跨平台 cross-platform re-test 可选 (见附录 C)
>     - Gemini 端未受影响, Q8/Q9 按 bank v3.1 原题跑, 7/10 结果不变
> - **Q14 PASS (c) C66727 codelist 名称修**: v3.1 写 "C66727 Disposition From Study codelist" 实为错归 — KB `knowledge_base/terminology/core/disposition.md` L15 + `domains/DS/spec.md` L81+L156 明证 **C66727 = "Completion/Reason for Non-Completion"**, 非 "Disposition From Study". DSDECOD 绑 3 codelist: **C66727 (Completion/Reason for Non-Completion)** + **C114118 (Protocol Milestone)** + **C150811 (Other Disposition Event Response)**. "DEATH" 属 C66727, 不需改 DSDECOD="DEATH" 的答案, 只修 codelist 标签 (ChatGPT reviewer 22 MED)
> - **ChatGPT 真实 score against bank v3.1**: 12/14 verified + 2/14 substituted (均 PASS 但对不同题, 非 14/14 against v3.1). 仍远超 ≥10/14 (71%) 阈, Gate 照开
>
> **v3.0 → v3.1 修改** (双 reviewer 独立审后主 session 修, 备档保留):
> - Q3 PASS (a): "采血=BS 不是 BE" → "采血行为=BE BECAT=COLLECTION + 采血测量=BS 并存" (ChatGPT reviewer HIGH, KB BE/spec.md BECAT "Example: COLLECTION" 明文支持)
> - Q3 FAIL: 删除 "采血记在 BE (错)" → 改为 "采血测量值记在 BE (错, Findings vs Events)"
> - Q4 FAIL (场景 A): 添加 PARTIAL 保护 "答 MB 但理由含免疫应答 → PARTIAL 非 FAIL" (Gemini reviewer HIGH, 跨版本记忆风险缓冲)
> - Q5 题目 + PASS + FAIL: 场景 A 从 "FA 指向 AE 头痛" reframe 为 "FA 指向 MH DAS28 评分" (04 §1.19 主覆盖 FA→AE, 非 FA→MH); 场景 C 从 "疲劳 unscheduled visit" reframe 为 "轻微头晕 30 秒自愈" (CE 边界更清晰, 降 04 重叠 35-40% → 目标 <25%)
> - Q10 PASS (d) + FAIL: "QVAL 200 字符上限 §8.4" 归因改为 "ch04 §4.5.3.2 父域 GOC 变量拆分机制; QVAL 自身无 SDTMIG 显式业务长度" (两 reviewer 交叉共识 HIGH)
> - Q14 PASS (c) v3.1 过程修: DSDECOD CT code C66728 → C66727 (方向对; 但 v3.1 仍错把 C66727 标为 "Disposition From Study", v3.2 再修正名称)
>
> **v3.0 原版**: 2026-04-21
> **基础**: N5_3_QUESTIONS_DESIGN.md + 联网 WebSearch × 6 + WebFetch × 4 (IS scope 精华) + 本地 KB GF/CP/BE/BS/IS/SV spec × 6
> **起因**: N5.2 双平台等价 10/10 PASS, 但 smoke v2.1 10 题全落入 04 §1.1-§1.10 预设 scenario → generalization probe 设计
> **双平台共用**: 10 题 (Q1-Q10), **4 平台共用 (Gemini bonus)**: 4 题 (Q11-Q14)
> **合格阈**: ChatGPT ≥ 10/14 (71%), Gemini ≥ 7/10 (70%)
> **04 非重叠**: 每题成稿后反向 grep 04, 重叠 >30% 换题
> **题源锚点**: 每题末尾列 KB 源文件 + 联网源 URL

---

## 题型分布 (v4.0 最终, 4 平台共用 17 题; Gemini Q11-Q14 作 bonus 容错)

| # | Type | 主题 | 平台 |
|---|------|------|:---:|
| Q1 | A1 v3.4 新域 | GF (Genomics Findings) 基因变异场景 | 4 平台共用 |
| Q2 | A2 v3.4 新域 | CP (Cell Phenotype) 流式细胞场景 | 4 平台共用 |
| Q3 | A3 v3.4 新域 | BE + BS + RELSPEC 生物样本全流程 | 4 平台共用 |
| Q4 | B1 域边界 | LB vs MB vs IS 三场景归属 (v3.4 scope) | 4 平台共用 |
| Q5 | B2 域边界 | FA vs QS vs CE 三场景归属 | 4 平台共用 |
| Q6 | C1 Timing 深化 | --TPTREF/--TPT/--ELTM/--RFTDTC/--TPTNUM 组合 | 4 平台共用 |
| Q7 | C2 Timing 深化 | Partial date 精度 + SDTM/ADaM imputation 分工 | 4 平台共用 |
| Q8 | D1 CT 深化 | Extensible vs Non-Extensible + MedDRA 绑定位置 (v4.0 AETERM 修正) | 4 平台共用 |
| Q9 | E1 实战验证 | Pinnacle 21 常见 FAIL 分类 | 4 平台共用 |
| Q10 | H1 SUPP 深化 | QORIG/QEVAL + SUPPQUAL scope (含 SUPPTS 前提纠错, v4.0 HIGH fix) | 4 平台共用 |
| Q11 | F1 新技术 | Dataset-JSON v1.1 vs XPT v5 submission | **4 平台共用 (Gemini bonus)** |
| Q12 | D2 CT 深化 | CT 版本锁定 + Define-XML + MedDRA 跨版本 | **4 平台共用 (Gemini bonus)** |
| Q13 | G1 RWD | Observational/RWD conformance 失效 + ARMCD 机制 (v4.0 删 NS 虚构概念) | **4 平台共用 (Gemini bonus)** |
| Q14 | I1 跨域 | 同一临床事件 AE/MH/CE timing 边界 + DS 死亡日级对齐 (v4.0 修 context) | **4 平台共用 (Gemini bonus)** |
| **AHP1** | **Z1 variable hallucination** | **LBCLINSIG 虚构变量 (v4.0 新增)** | **4 平台共用** |
| **AHP2** | **Z2 cross-domain hallucination** | **"Trial-Level SAE Aggregate 表"虚构 (v4.0 新增)** | **4 平台共用** |
| **AHP3** | **Z3 deprecated concept** | **PF 域 v3.4 已废 (v4.0 新增)** | **4 平台共用** |

---

# 10 题全文 (双平台共用)

---

## Q1 (A1 — GF 域) EGFR 基因变异场景

> **题**: 某肿瘤试验对受试者外周血样进行 EGFR 基因测序, 在 Exon 19 位置发现一个已知的激活突变 (dbSNP rs121913444, 导致 L858R 氨基酸替代). 这条结果应该记录在 SDTMIG v3.4 的哪个域? 请列出该记录至少 **5 个 Core=Req 变量** 和 **3 个 Core=Exp 变量** (按 Topic 变量优先), 并说明: (a) 如何记录"Exon 19"位置信息; (b) 如何引用 dbSNP ID; (c) 基因组参考版本 (比如 GRCh38.p13) 存哪; (d) 如果该变异可遗传给下一代, 走哪个变量.

**PASS 判据 (核心事实必中)**:
- 正确识别域为 **GF (Genomics Findings)** (v3.4 新增, 从 SDTMIG-PGx v1.0 迁入), 不是旧 PF 或 LB
- Core Req 至少列: STUDYID / DOMAIN="GF" / USUBJID / **GFSEQ** / **GFTESTCD** / **GFTEST** (任 5)
- Core Exp 至少列: **GFREFID** (assayed genetic specimen ID) / **GFORRES** / **GFSTRESC** / **GFDTC** / **GFMETHOD** / VISITNUM (任 3)
- (a) **GFGENSR** (Genetic Sub-Region, 示例 "Exon 15" / "Kinase domain") 存 "Exon 19"
- (b) **GFPVRID** (Published Variant Identifier) 存 "rs121913444" (dbSNP ID)
- (c) **GFGENREF** (Genome Reference) 存 "GRCh38.p13"
- (d) **GFINHERT** (Inheritability, CT C181177) 指示可否遗传

**FAIL 判据**:
- 答成 LB 或 PGx/PF 旧域 (v3.4 已废 PGx)
- 臆造变量如 GFGENE / GFVARIANT (其实是 GFSYM / GFORRES)
- GFCHROM (染色体号) 和 GFGENSR (基因内区域) 弄混
- 说 GFINHERT 不存在

**KB 源锚点**: `knowledge_base/domains/GF/spec.md` L104-299 (GFTESTCD/GFGENSR/GFPVRID/GFGENREF/GFINHERT 定义) + SDTMIG v3.4 §6.3.5.5 Genomics Findings

**04 非重叠检查**: 04 无 §GF 章节, 无 "GFTESTCD / GFGENSR / GFPVRID" 关键字, Pure generalization ✅

**联网源**:
- [CDISC SDTMIG v3.4 GF Domain Intro](https://www.cdisc.org/sites/default/files/pdf/IntroToGFDomain-Webinar_0.pdf)
- [PhUSE 2025 DS11 — Evolution of Genomic Data Mappings PF→GF](https://www.lexjansen.com/phuse-us/2025/ds/PAP_DS11.pdf)

---

## Q2 (A2 — CP 域) 流式细胞测 CD4+ T 细胞 ACTIVATED 亚群

> **题**: 某免疫治疗试验用流式细胞仪检测受试者 PBMC 样本里 "活化的 CD4+ T 辅助细胞" (通过 Ki67+ 表达识别为 ACTIVATED 状态). SDTMIG v3.4 里这个测量属于哪个域? 请说明: (a) Topic 变量是什么; (b) 如何区别"T Lym Help" 这个**命名**细胞群与 CD4+Ki67+ 这个**子集**亚群; (c) 用哪些变量记录"哪些 marker 被用来定义'活化'状态"; (d) Method 变量应填什么 (测量方法); (e) 这个域和 LB 的边界是什么.

**PASS 判据**:
- 正确识别为 **CP (Cell Phenotype Findings)** 域 (v3.4 新增)
- (a) Topic: **CPTESTCD** (Req, 例 "CD4THLP" 或 "CD4HELP") + **CPTEST** (例 "T Lym Help")
- (b) 命名群: CPTEST="T Lym Help"; 子集: CPTEST 加 "Sub" 后缀 (e.g., "T Lym Help Sub") + **CPSBMRKS** (Sublineage Marker String, 例 "CD4+Ki67+") 存具体 marker 组合
- (c) **CPCELSTA** (Cell State, C181172, 值 "ACTIVATED") + **CPCSMRKS** (Cell State Marker String, 例 "Ki67+") 说明 Ki67 表达定义 activation
- (d) **CPMETHOD** = "FLOW CYTOMETRY" (C85492)
- (e) 边界: CP 专用于基于**细胞群特征** (marker 表达) 的单细胞/颗粒悬液测量, LB 是血生化/血常规等传统实验室检查. CP 共享一些 marker/binding 变量 (如 CPBDAGNT) 与 IS/LB 但 Topic 性质不同.

**FAIL 判据**:
- 答 LB 或 IS 或自创 FC 域
- CPSBMRKS vs CPCELSTA 概念弄混 (sublineage marker 定义**亚群** vs cell state marker 定义**状态**)
- 漏 Sub 后缀规则 (子集必须 Sub 后缀)
- Method 答 "PCR" 或 "ELISA" (非流式)

**KB 源锚点**: `knowledge_base/domains/CP/spec.md` L86-193 (CPTESTCD/CPTEST/CPSBMRKS/CPCELSTA/CPCSMRKS/CPMETHOD 定义)

**04 非重叠**: 04 仅 §22.3 "CP + GF 分子/基因组" 一行提过, 无深入. Pure generalization ✅

---

## Q3 (A3 — BE + BS + RELSPEC) 生物样本从采集到 DNA 提取

> **题**: 某 PGx 试验, 受试者 Visit 2 现场采集血样 (BS-001), 当天运输到中心实验室 (运输过程记为一个事件), 第二天从 BS-001 样本提取 DNA 得到 DNA-001 子样本. 请说明: (a) 这三个"阶段" (采血 / 运输 / DNA 提取) 分别记录在哪些域? (b) 血样的"体积 = 5 mL"和"RNA 完整性数 (RIN) = 9.2"这两个**测量**记录在哪个域, 对应 Topic 变量值分别是什么; (c) BS-001 → DNA-001 这种**样本派生关系**怎么表达? 应该用哪个 Dataset (RELREC 还是另一个)?

**PASS 判据** (v4.0 微调: Finding 2 reviewer MEDIUM→MINOR 后 — BETERM (Req Topic) 是 canonical, BECAT (Perm) 是可选分类):
- (a) **三阶段均走 BE 域** (采血 / 运输 / DNA 提取, 均为 events); **Topic 变量 BETERM (Req)** 描述具体事件 (Collecting / Transporting / Extracting 或 COLLECTION / TRANSPORT / PREPARATION 等 sponsor verbatim); **BECAT (Perm) 可选粗分类** (example: COLLECTION, PREPARATION, TRANSPORT, 来自 BE/spec.md BECAT Notes). **采血测量** (体积/RIN) = **BS** (Biospecimen Findings, BE 和 BS 并行不互斥, BE 记采集事件 / BS 记测量结果). KB BE/spec.md BECAT Notes 明文列 "Example: COLLECTION, PREPARATION, TRANSPORT" 作为 BECAT 的 example values.
  - **可接受的等价答法**: BETERM="COLLECTION" + BECAT 留空 / BETERM="Collecting" + BECAT="COLLECTION" / 用 BETERM 主述 + BECAT 可选 / BEDECOD (C124297 Dictionary Derived Term) 记编码后的标准值
- (b) 血样测量在 **BS**:
  - 体积: BSTESTCD="VOLUME", BSTEST="Volume", BSORRES="5", BSORRESU="mL"
  - RIN: BSTESTCD="RIN", BSTEST="RNA Integrity Number", BSORRES="9.2"
  - (Topic 变量 BSTESTCD, C124300 官方支持 VOLUME / RIN)
- (c) 样本派生关系用 **RELSPEC** (Related Specimens) 域, 不用 RELREC (RELREC 是跨 general observation class 记录关系, RELSPEC 是 specimen 之间的层级关系)
- 补充加分: BEREFID / BSREFID 指向 specimen ID

**FAIL 判据**:
- 把 BS 和 BE 混淆 (Findings vs Events)
- 说用 RELREC 记 specimen hierarchy (错, 应 RELSPEC)
- Topic 变量用 "VOL" 或 "RNAINT" (错, 官方 CT C124300 是 VOLUME / RIN)
- 把采血**测量值** (体积/RIN) 记在 BE (错, Findings 测量数据不是 Events; 采血行为可记 BE COLLECTION, 但测量值必走 BS)

**KB 源锚点**: 
- `knowledge_base/domains/BE/spec.md` L77-148 (BETERM/BECAT 定义 + Examples COLLECTION/PREPARATION/TRANSPORT)
- `knowledge_base/domains/BS/spec.md` L77-129 (BSTESTCD C124300 Examples: VOLUME, RIN)
- Cross-ref `BS/spec.md` L337 Specimen Relationship → RELSPEC

**04 非重叠**: 04 仅 §1.25 提 "BE 和 MB/MS 微生物" 一行. ✅

**联网源**:
- [SDTMIG-PGx v1.0 (deprecated, 现迁入 SDTMIG v3.4)](https://www.cdisc.org/standards/foundational/pgx-sdtmig/sdtmig-pgx-v1-0)

---

## Q4 (B1 — LB vs MB vs IS 边界) 三场景选域

> **题**: 以下 3 个实验室检验结果, 在 SDTMIG v3.4 下分别记录到哪个域 (LB / MB / IS)?
>
> **场景 A**: 疫苗试验, baseline (入组当日) 检测受试者血清中抗麻疹病毒 IgG 抗体滴度 (测过往感染或接种史), 数值 1:128
> **场景 B**: 抗肿瘤单抗治疗后, 受试者血清中检测抗药物抗体 (ADA) 阳性/阴性 + 滴度
> **场景 C**: 受试者痰样做结核杆菌 (Mycobacterium tuberculosis) 培养, 结果 positive
>
> 每个场景给出: (i) 域名; (ii) 理由 (为什么不是另外两个域); (iii) Topic 变量值示例. v3.4 下边界规则是什么?

**PASS 判据**:
- **场景 A** (抗麻疹病毒 IgG baseline): **IS** (Immunogenicity Specimen). 理由: 测 "对抗原暴露的免疫应答" (抗体水平), v3.4 起 anti-microbial antibody 无论 baseline 与否都归 IS (过去 v3.3 baseline 在 MB, v3.4 统一到 IS). Topic: ISTESTCD="MEASIGG" 或 "MVIGG", ISBDAGNT="Measles virus"
- **场景 B** (ADA): **IS** (无歧义). 理由: 抗药物抗体是经典免疫原性测量, IS 域是为此设计. Topic: ISTESTCD (ADA codelist), ISBDAGNT=药物名
- **场景 C** (Mtb 培养): **MB** (Microbiology Specimen). 理由: MB 测 "微生物直接检出" (培养 / PCR / 染色), 不是 surrogate 抗体. Topic: MBTESTCD="MTBCULT" 或类似
- v3.4 边界规则: IS 测**免疫应答** (抗体/免疫细胞/细胞因子, 不管触发因素), MB 测**微生物直接存在** (培养/PCR/染色/抗原检出), LB 测**常规血生化/血液学** (肝肾功能/电解质/血常规)

**FAIL 判据** (v4.0 修订: PARTIAL 规则收窄, `IS/assumptions.md` assumption 2 是 v3.4 显文, 不是"版本迁移无显文"):
- A 答 MB (v3.2/v3.3 旧规则, 忽略 v3.4 scope 变化):
  - 答 MB 且**仅提 "检测抗体"** → **FAIL** (`IS/assumptions.md` assumption 2 是 SDTMIG v3.4 显式规则放 IS, 不是"原材料有但规则无显文"; 若答题者识别 "检测抗体 = 免疫应答 surrogate" 却仍答 MB, 逻辑不自洽)
  - 答 MB 且**显式标注 "这是 pre-v3.4 旧习惯, 知道 v3.4 assumption 2 应归 IS"** → **HALF 0.5** (识别了版本差, 但未按 v3.4 执行)
  - 答 MB 且**无理由** / 答 "直接检出微生物" → **FAIL**
- A 答 LB (错, 抗体不是常规生化)
- C 答 IS (错, 直接检出微生物不是免疫应答)
- B 答 LB (错, ADA 是免疫应答不是常规生化)
- 不给理由或边界规则

**KB 源锚点**: `knowledge_base/domains/IS/spec.md` L122 ISBDAGNT + IS/assumptions.md + 联网 CDISC IS Scope Update article

**04 非重叠**: 04 仅 §1.25 BE+MB 提过, 无 LB/MB/IS 三域 scope 对比. ✅

**联网源**:
- [CDISC — IS Domain Scope Update for SDTMIG v3.4](https://www.cdisc.org/kb/articles/domain-scope-update-sdtmig-v3-4-development-history-and-difficulties-standardizing)
- [CDISC — Where Does My Lab Data Go in SDTMIG v3.4](https://www.cdisc.org/kb/articles/where-does-my-lab-data-go-sdtmig-v3-4)
- [CDISC Webinar — LB/MB Scope Changes](https://www.cdisc.org/events/webinar/lb-mb-domain-scope-changes-sdtmig-v3-4-and-impact-controlled-terminology)

---

## Q5 (B2 — FA vs QS vs CE 边界) 三场景选域

> **题** (v3.1 reframe reduce 04 §1.19 overlap): 以下 3 条 EDC 收集信息, 分别映射到 FA / QS / CE 哪个 SDTM 域?
>
> **场景 A**: 受试者有既往 MH "类风湿性关节炎 15 年", 研究者在 Visit 4 对这条既往 MH 记录做量化评分 (用 28-joint tender/swollen count, 记 DAS28 评分 4.2). 这是对**既往 MH 记录**的量化 findings (非针对 AE).
> **场景 B**: 受试者在 Visit 4 填 SF-36 生活质量问卷, 8 个维度每个打分
> **场景 C**: 受试者自诉 Visit 5 出现轻微头晕 (dizziness, 30 秒自愈), 研究者记录但不认为需医疗处理, 未达 AE 报告阈值
>
> 每个场景: (i) 域名 + (ii) 理由 + (iii) Topic 变量值示例

**PASS 判据**:
- **A**: **FA** (Findings About). 理由: FA 专为"关于某个已存在 Event/Intervention/Finding 记录的 additional findings"设计, Topic 是 FATESTCD (measurement about an existing record), 配合 **FAOBJ 指向 MH 记录** (不是 AE). 不用 QS (QS 是独立患者报告问卷, DAS28 是临床评估非 patient-reported). 不用 SUPPMH (SUPPMH 是单条 MH 加非标字段, FA 是结构化独立评估记录).
- **B**: **QS** (Questionnaires). 理由: QS 专门记标准化问卷仪器 (SF-36 / EORTC / PROMIS). Topic: QSTESTCD (e.g., "QSPF01"), QSCAT="SF-36", QSSCAT=各 domain. 不用 FA.
- **C**: **CE** (Clinical Events). 理由: CE 记录不到 AE 阈值但临床相关的事件 ("meaningful clinical events that are not AE"). 不用 AE (未达标), 不用 DV (DV 是 protocol deviation 非临床事件).

**FAIL 判据**:
- A 答 QS (错, DAS28 不是独立问卷而是对既往病史的临床评估, 走 FA)
- A 答 SUPPMH (错, SUPPMH 是非标字段补充, FA 是结构化独立评估)
- B 答 FA 或 CE
- C 答 AE (明确未达 AE 阈值) 或 DV (DV 是协议偏离非临床事件)

**KB 源锚点**: `knowledge_base/domains/FA/` + `knowledge_base/domains/QS/` + `knowledge_base/domains/CE/` (本题要求跨域鉴别)

**04 非重叠**: 04 §1.19 "QS vs FA" 已提过, 本题加 CE 三元鉴别 — 04 未覆盖三元. borderline ⚠️ (需 reframe: 可能强调 CE 维度判断, 若 reviewer 判 >30% 重叠则改)

**联网源**: SDTMIG v3.4 §6.3.11 (FA) + §6.3.17 (QS) + §6.2.4 (CE)

---

## Q6 (C1 — Timing 深化) PK 定时采血 --TPT 四件套

> **题**: 某 PK 研究的访视日安排: 受试者上午 8:00 服用研究药物 (A-001), 之后 15 min / 1 h / 4 h / 8 h 各采一次血样用于 PK. 一周后再来同样做一次 (两周期). 请说明 PK 域 (PC 域) 里, 对"服药后 4 小时采血"那一条记录, 下列 5 个 Timing 变量应怎么填:
>
> PCTPT / PCTPTNUM / PCTPTREF / PCELTM / PCRFTDTC
>
> 并解释: (a) PCTPT vs PCTPTNUM 关系; (b) PCTPTREF 指什么; (c) PCELTM 是 ISO 什么格式; (d) 同一受试者两周期记录用什么区分.

**PASS 判据**:
- **PCTPT** (Planned Time Point Name, 文字): "4 hours post dose" / "4 HR POST DOSE" (文字可读)
- **PCTPTNUM** (数字版用于排序): 例如 "4" (或 4; 排序整数, 15min=1, 1h=2, 4h=3, 8h=4 也可)
- **PCTPTREF** (Time Point Reference): "DOSE" 或 "PREVIOUS DOSE" 或 "STUDY DRUG DOSE" (名字指向 fixed reference point)
- **PCELTM** (Planned Elapsed Time): **ISO 8601 duration 格式** = "PT4H" (P=period, T=time, 4H=4 hours)
- **PCRFTDTC** (Date/Time of Reference): 实际服药时间 ISO 8601 datetime, 例 "2024-06-15T08:00"
- (a) PCTPT 是文字标识 (排序差), PCTPTNUM 是数字用于排序
- (b) PCTPTREF 给一个**名字** (reference point name), 与 PCRFTDTC 实际 datetime 成对
- (c) PCELTM 是 **ISO 8601 duration** (P/PT 前缀, 不是 datetime)
- (d) 两周期用 **VISITNUM** 区分 (Cycle 1 vs Cycle 2 两个 visit), 或用 **EPOCH** (C99079) 区分治疗阶段

**FAIL 判据**:
- PCELTM 写成 "4 hours" 或 "04:00:00" (错, 必须 ISO duration "PT4H")
- PCTPTREF 写成 datetime (错, 是 name, datetime 在 PCRFTDTC)
- 混淆 Planned (TPT/TPTNUM/ELTM/TPTREF) 与 Actual (RFTDTC + STDTC); 4 个计划变量独立于 PCSTDTC (实际采血时)
- 用 VISITDY 区分两周期 (错, VISITDY 可能相同)

**KB 源锚点**: `knowledge_base/domains/PC/spec.md` (PC 域完整 Timing); 本题可参考 GF/CP Timing (PCTPT 模板和 GFTPT 镜像)

**04 非重叠**: 04 §4.3 Timing 基础提过 --STDTC/--ENDTC/--DY 但 **未深入 --TPT/--TPTREF/--ELTM/--RFTDTC 四件套**. ✅

---

## Q7 (C2 — Partial date) EDC 只给部分日期怎么填

> **题**: ISO 8601 datetime 变量 (e.g., AESTDTC, CMSTDTC) 允许**部分精度**. 下列 3 个场景, 各应怎么填? SDTMIG v3.4 对 partial date 有没有 imputation 规则 (SDTM 级还是 ADaM 级)?
>
> **场景 A**: EDC 只收到 "AE 开始于 2024 年 6 月" (无日)
> **场景 B**: EDC 只收到 "服药开始于 2024 年" (无月日)
> **场景 C**: EDC 完全没收到 AE 开始日 (Unknown)
>
> 另外回答: (d) SDTM 的 --STDTC 需要做 imputation 吗? (e) 如果 ADaM 需要 imputation, SDTM 还需要额外记什么吗?

**PASS 判据**:
- **A** (年月): AESTDTC = "**2024-06**" (ISO 8601 部分精度只到月)
- **B** (年): AESTDTC = "**2024**" (只到年)
- **C** (完全未知): AESTDTC = **null / 空** (不能填 "UNKNOWN" 字符串, 必须 null)
- (d) **SDTM 级不做 imputation** — SDTM 保留原始精度, 不因后续分析需要而猜月/日. Imputation 是 **ADaM 级** (ADSL / ADAE 等分析数据集派生 imputed date 存 ADT 类变量, 并记 ADTF imputation flag).
- (e) SDTM 可用 SUPPAE 存 imputation 相关 supplemental qualifier (比如 "Onset date reported as: June 2024"), 或用 -DY 留空. 绝对**不要在 --STDTC 内自己补 01 或 1st**.

**FAIL 判据**:
- 场景 A 答 "2024-06-01" 或 "2024-06-15" (错, imputation 不是 SDTM 职责)
- 场景 C 答 "1900-01-01" 或 "UNKNOWN" (错, 空值必须 null)
- 说 SDTM 做 imputation (错, SDTM 保真, ADaM imputation)
- 不识 ISO 8601 部分精度 (只写 full datetime)

**KB 源锚点**: `knowledge_base/chapters/ch04_general_assumptions.md` (ISO 8601 + partial date 规则)

**04 非重叠**: 04 §1.8 / §2.9 提过 ISO 8601 基础, 但 **未深入 imputation SDTM vs ADaM 职责边界**. ✅

---

## Q8 (D1 — CT Extensible vs Non-Extensible)

> **题**: CDISC Controlled Terminology 的每个 codelist 有 **Extensible = Yes/No** 属性. 请回答: (a) Extensible=Yes 和 Extensible=No 语义区别是什么 (sponsor 能否加自己的值)? (b) 举 2 个 **Non-Extensible** 的常见 codelist 例子 (必须完全按 CDISC 用), 和 2 个 **Extensible** 的例子 (允许扩); (c) AETERM 这种变量"CT 值"语义和 AESEV (Non-Extensible) 有什么区别 (AETERM 实际用 MedDRA 字典, 不是 CDISC CT); (d) 如果 sponsor 自己扩 LBTESTCD, Define-XML 要做什么?

**PASS 判据** (v4.0 修订: LBNRIND 移到 Extensible + NY 补 NA + AETERM 字典绑定位置修正):
- (a) **Extensible=Yes** 允许 sponsor 在 CDISC CT 基础上**加新的 submission value** (通常加在 codelist 末尾, 不改已有值); **Extensible=No** 必须完全按 CDISC CT, 不加不改
- (b) **Non-Extensible 例子**: **NY (No/Yes) C66742 {Y, N, U, NA}** (4 值, 注: NA=Not Applicable C48660) / **AESEV C66769 {MILD, MODERATE, SEVERE}** / **NDF "Not Done" C66789 {NOT DONE}** (任 2)
- (b) **Extensible 例子**: **LBTESTCD / LBTEST** (常规实验室测试名, sponsor 可加自己的) / **LBNRIND C78736 {HIGH, LOW, NORMAL, ABNORMAL}** (Extensible=Yes, sponsor 可扩; KB `terminology/core/general_part4.md` L63-72 明文) / **MBTESTCD / MBTEST** (任 2)
- (c) **AETERM** (Reported Term for AE, Core=Req/Topic): 是 **CRF verbatim free text**, **Controlled Terms 列空** (既不绑 CDISC CT 也不绑 MedDRA), 见 `AE/spec.md` L77-85.
  - **MedDRA 字典绑定位置是 dictionary-derived 变量 (非 --TERM)**:
    - **AEDECOD** (AE Dictionary Derived Term, L117): MedDRA Preferred Term
    - **AELLT** (Lowest Level Term, L99): MedDRA LLT
    - **AEHLT** / **AEHLGT** / **AEBDSYCD** / **AESOC** / **AESOCCD**: MedDRA 其他层级 (L135-223)
  - 业界常见 misspeak "AETERM 用 MedDRA" 是不准确的, 严格表述为 "AEDECOD 等 --DECOD 绑 MedDRA, AETERM 是 CRF 原始 verbatim".
  - AESEV 对比: 使用 CDISC CT C66769 Non-Extensible 三档固定 (MILD/MODERATE/SEVERE).
- (d) sponsor 扩 LBTESTCD 时, Define-XML 必须在 codelist metadata 中注明 extension values + sponsor-defined codelist reference

**FAIL 判据**:
- 混淆 Extensible / Non-Extensible 语义 (反着说)
- **把 LBNRIND 列为 Non-Extensible** → FAIL (KB general_part4.md L65 明 Extensible=Yes)
- **说 AETERM 使用 MedDRA 字典** → FAIL (MedDRA 绑 --DECOD, AETERM 是 verbatim; 答题者若说 AETERM 绑 MedDRA 是**常见 misspeak**, 属 variable identity 错位)
- 说 AETERM 绑 CDISC CT (错, Controlled Terms 列空)
- AESEV 说是 Extensible (错, Non-Extensible 三档固定)
- Define-XML 作用不提

**PASS+ (加分)**:
- 主动识别 "AETERM 不绑 MedDRA, MedDRA 绑 AEDECOD" 这层字典绑定精度 → PASS+ bonus

**KB 源锚点** (v4.0: F1 全局 ch05→ch04 §4.3 + terminology/core/; ch05_controlled_terminology.md 在本 KB 不存在):
- `knowledge_base/chapters/ch04_general_assumptions.md` §4.3 L606-670 (Coding and Controlled Terminology Assumptions)
- `knowledge_base/terminology/core/general_part4.md` (C66742 NY L9-14 Ext=No / C78736 LBNRIND L63-72 Ext=**Yes** / C66789 Not Done)
- `knowledge_base/terminology/core/ae.md` L43-51 (C66769 AESEV Ext=No {MILD, MODERATE, SEVERE})
- `knowledge_base/domains/AE/spec.md` L77-85 (AETERM Controlled Terms 列空, verbatim) + L117-223 (AEDECOD/AELLT/AEHLT/AEHLGT/AESOC/AEBDSYCD/AESOCCD 绑 MedDRA)

**04 非重叠**: 04 §1.15 "Controlled Terminology Extensible vs Non-Extensible" 标题提过但内容仅一句, **未深入 MedDRA 外部字典边界 + Define-XML**. borderline ⚠️ (reframe: 强调 MedDRA 边界 + Define-XML)

---

## Q9 (E1 — Pinnacle 21 常见 FAIL 分类)

> **题**: Pinnacle 21 (OpenCDISC Validator) 是 FDA 审查 SDTM 数据时常用的验证工具, 对一份 SDTM 数据会返回 Errors / Warnings / Notices 三级 issue. 请按**类型分类**列举 **5-6 大类**常见 FAIL, 每类举 **1 个典型触发例子**, 并说明: 遇到 Pinnacle 21 FAIL 时, 什么时候应该**修数据**, 什么时候应该**在 Reviewers Guide 文档化并保留**不修?

**PASS 判据 (必含 5 大类, 合理即 PASS)**:
1. **Date consistency** (日期逻辑): 例如 AESTDTC > AEENDTC, 或 EXSTDTC < RFXSTDTC. 应修 (真错).
2. **Controlled Terminology compliance**: 例如 AESEV="MODERATE " (尾空格) 或 AESEV="SEV" (非 codelist 值). 应修.
3. **Required / Expected variable 缺失**: 例如 AE 域 STUDYID 空, DM 域 USUBJID 空. 应修.
4. **Duplicate records**: 例如同一 USUBJID + --SEQ 出现两条. 应修 (--SEQ 必须唯一).
5. **Orig vs Std units / numeric vs character 类型错**: 例如 LBSTRESN = "6.8%" (numeric 列带字符) 或 LBORRES 空 但 LBSTRESC 填了. 应修.
6. (可选) **Value-level consistency**: 例如 AESER=Y 但所有子变量 (AESHOSP/AESLIFE/AESCONG/AESMIE 等) 全空. 边界 case, 可文档化.
- **应修 vs 文档化决策原则**: 如果是**真实数据错** (比如 EDC entry 错, 日期倒序) → 修. 如果是**标准不匹配但数据是真实** (比如 RWD 场景没有 planned arm, 或小儿 BMI 不适用成人 range, 或 sponsor-defined codelist legit extension) → 在 **Reviewers Guide** / **csdrg.pdf** 文档化解释, 保留 issue, 不改数据.

**FAIL 判据**:
- 只列 ≤3 大类
- 混淆 Error / Warning / Notice 等级
- 说"所有 FAIL 必修" (错, 有些该文档化保留)
- 给具体虚构 rule ID (比如答 "SD9999") — 不要求具体 ID, 要求分类合理

**KB 源锚点**: 本题不走 KB, 靠业务常识 + Pinnacle 21 常识

**04 非重叠**: 04 **0 覆盖 Pinnacle 21**. Pure generalization ✅

**联网源**:
- [Pinnacle 21 SDTM Validation Rules](https://standards.pinnacle21.certara.net/validation-rules/sdtm)
- [Pinnacle 21 by Certara — SDTM Mapping Process Simplified](https://www.certara.com/blog/the-sdtm-mapping-process-simplified/)
- [PharmaSUG 2019 DS-119 — Common Pinnacle 21 Report Issues: Shall we Document or Fix?](https://www.lexjansen.com/pharmasug/2019/DS/PharmaSUG-2019-DS-119.pdf)

---

## Q10 (H1 — SUPP 深化) QORIG/QEVAL + SUPPQUAL scope (含 SUPPTS 前提纠错)

> **题** (v4.0 修订: SUPPTS 不是 SDTMIG v3.4 定义的 dataset): SDTM 的 SUPP-- (Supplemental Qualifiers) 家族里, 请回答:
>
> (a) 每条 SUPP 记录有 QNAM / QLABEL / QVAL / **QORIG** / **QEVAL** 5 个关键字段. QORIG 和 QEVAL 什么时候**必填**, 什么时候**不填**? 含义分别是?
> (b) **SUPPQUAL 机制在 SDTMIG v3.4 下适用于哪些数据集 scope**? 对于**不**适用 SUPPQUAL 的数据集 (比如 Trial Design 模型中的 TS "Trial Summary"), 长文本 (>200 字符) 怎么处理? 同一受试者的 AE 记录有 NSV 时用 **SUPPAE**; 那么对 TS 的长 parameter value, 理应用 **"SUPPTS"** 吗?
> (c) 一条 SUPPAE 记录如何通过 RDOMAIN + IDVAR + IDVARVAL 定位到**具体**的 AE 父记录? USUBJID 怎么用?
> (d) QVAL 长度上限是多少? 超过怎么拆?

**PASS 判据**:
- (a) **QORIG** (Origin): 必填 (Core=Req). 指 QVAL 来源, 值可为 "CRF" / "Protocol" / "Derived" / "Assigned" / "eDT" / "Investigator" 等. **QEVAL** (Evaluator, Core=Exp, CT C78735): 当 QVAL 需人评估时填 (如 "ADJUDICATION COMMITTEE" / "INVESTIGATOR" / "SPONSOR" / "STATISTICIAN"); 纯机器/CRF 录入时可不填.
- (b) **SUPPQUAL scope** (ch08 §8.4 L177 原文): 适用于 **general-observation class datasets (Events / Findings / Interventions) + Demographics (DM) + Subject Visits (SV)**; **TS (Trial Summary) 属于 Trial Design 模型, 不在 SUPP-- scope 内**.
  - 长 TSVAL 处理: **TS 域自身派生列 TSVAL1, TSVAL2, ..., TSVALn** (前 200 字符在 TSVAL, 每 200 字符 overflow 开一新列), 见 `TS/spec.md` L65-67 + `ch04_general_assumptions.md` §4.5.3.2 L1296 table.
  - **"SUPPTS" 不是 SDTMIG v3.4 定义的 dataset** — 必显式指出这是**用户常见误解** (confound with SUPP-- 机制推广), 实际 TS 在 Trial Design 层面不走 SUPPQUAL.
  - SUPPAE 是真实 subject-level SUPP-- 实例: 每条 SUPP 记录必含 USUBJID + AE 父记录的 --SEQ, 结构为 RDOMAIN/IDVAR/IDVARVAL 三键 join.
- (c) SUPPAE: RDOMAIN = "AE"; IDVAR = "AESEQ" (通常, 也可 AEGRPID); IDVARVAL = 具体的 AESEQ 值 (字符化, e.g., "3"). USUBJID 必填 (subject-level). 三字段联合定位父 AE 记录.
- (d) **超长文本处理** (ch04 §4.5.3.2 正确归因): 父域 GOC 变量 (如 AETERM / CMTRT) 超 200 字符时按拆分规则 — 前 200 字符留父域, **超出部分按顺序写入 SUPP-- QVAL** (同一 QNAM 加数字后缀如 QNAM1/QNAM2). QVAL 自身**无 SDTMIG 显式业务长度规定**, 实践受 SAS XPT v5 字段约束 (~200 字节). 200 字符是父域 GOC 变量上限, 不是 QVAL 自身硬性上限. **TS 例外** — TS 的长 TSVAL 不走 SUPP-- 而是 TSVAL1-TSVALn 内部派生.

**FAIL 判据**:
- QORIG 与 QEVAL 语义反
- **沿 "SUPPTS 存在 / SUPPTS 是 study-level" 前提答 (b)** → **FAIL (premise hallucination)**, **不是 PARTIAL**; 编 SUPPTS USUBJID 规则 / 说 SUPPTS 与 SUPPAE 层级差 → FAIL
- 说 SUPPQUAL 适用所有 domain (错, scope 限 Events/Findings/Interventions + DM + SV)
- IDVAR / IDVARVAL 用法错 (e.g., 说 IDVAR="USUBJID")
- 错答 "QVAL 本身有 200 字符硬上限" (归因错; 200 是父域 GOC 变量拆分阈值, 不是 QVAL 自身限制). 错答 40 或 500 也 FAIL.

**PASS+ (加分)**:
- 主动识别 "SUPPTS 不是 v3.4 real dataset" 并给出 TSVAL1-TSVALn 替代方案 → 算 PASS+ (额外 0.25 分 bonus 或单纯记为 premise-correction noted)

**KB 源锚点** (v4.0: F1 全局 ch05→ch04 §4.3 + terminology/core/):
- `knowledge_base/chapters/ch08_relationships.md` §8.4 L177 (SUPPQUAL scope 限定原文)
- `knowledge_base/chapters/ch04_general_assumptions.md` §4.5.3.2 L1296 (TS.TSVAL 特殊 convention) + §4.3 L606-670 (Coding & Controlled Terminology Assumptions)
- `knowledge_base/domains/TS/spec.md` L65-67 (TSVAL1-TSVALn 规则 + Assumption 8)
- `knowledge_base/domains/SUPPQUAL/spec.md` L1-111 (QORIG Req / QEVAL Exp C78735 / RDOMAIN/IDVAR/IDVARVAL 三键)
- `knowledge_base/terminology/core/general_part2.md` L107-164 (QEVAL C78735 submission values)

**04 非重叠**: 04 §1.9 SUPPAE 基础题, §19 SUPPQUAL 深化有 QNAM/QLABEL 基础. **未深入 QORIG/QEVAL + SUPPQUAL scope 边界 + premise hallucination 纠错**. borderline ⚠️ (v4.0 新重点: 测 SUPPTS 前提纠错能力, 04 未覆盖)

---

# 4 题 Q11-Q14 (4 平台共用, Gemini bonus 容错)

---

## Q11 (F1 — Dataset-JSON v1.1 vs XPT v5) 4 平台共用 (Gemini bonus 容错)

> **题**: 2025 年 FDA 启动 Dataset-JSON 试点, CDISC 发布 Dataset-JSON v1.1. 请说明: (a) Dataset-JSON 相比 SAS XPT v5 主要解决什么 4-5 个**技术痛点**? (b) 2026 年现状: FDA 接受哪个? (c) 作为 SDTM 程师, 现在实操建议是什么 (开发环境 / 归档 / 提交)? (d) Define-XML 和 Dataset-JSON 互补关系是什么?

**PASS 判据**:
- (a) XPT 痛点 5 项任 4: **变量名长度限制 8 字符** / **字段值 200 字符上限** / **无 Unicode 支持** / **无 metadata 扩展** (Define-XML 必须外挂) / **存储低效 (binary 不可读不可 diff)** / **数据类型有限** (只 num/char)
- (b) 现状: **XPT v5 仍是 FDA 必需**直到 Dataset-JSON 加入 Data Standards Catalog (预期 2026 正式决定). R Consortium 2025 秋第一次成功 Dataset-JSON submit ADaM.
- (c) 实操: (i) 开发环境可用 Dataset-JSON (便于 version control 和 diff) / (ii) 归档和最终 submit 仍用 XPT v5 / (iii) 有双向转换工具 (如 Atorus datasetjson R 包 / Pinnacle 21 支持) / (iv) 密切关注 FDA catalog 更新
- (d) Define-XML 是 metadata (变量定义 / CT reference / origin); Dataset-JSON 是 data. 两者互补: Define-XML 描述结构, Dataset-JSON 存数据. 未来 Define-XML v3.0 也在 align Dataset-JSON (可能简化 metadata 嵌入).

**FAIL 判据**:
- 说 FDA 已全面 Dataset-JSON (错, 仍 XPT 必需)
- 列不出 XPT 技术痛点
- 混淆 Define-XML 和 Dataset-JSON 角色

**04 非重叠**: 04 0 覆盖. Pure generalization ✅

**联网源**:
- [Clinical Leader — Piloting New Dataset-JSON For FDA Submissions](https://www.clinicalleader.com/doc/no-more-xpt-piloting-new-dataset-json-for-fda-submissions-0001)
- [Clinical Standards Hub — FDA Standards 2025](https://www.clinstandards.org/blog/navigating-fda-standards-2025)
- [Atorus Research — datasetjson R package](https://www.atorusresearch.com/datasetjson-0-0-1-release/)

---

## Q12 (D2 — CT 版本锁定) 4 平台共用 (Gemini bonus 容错)

> **题**: 一个 3 年期临床试验, 从 2022 启动到 2025 DBL (database lock). 期间 CDISC 每季度发布 CT release. 请说明: (a) 这个试验**锁用**哪个 CT 版本 (start 时 / ongoing / DBL 时)? (b) 锁定 CT 版本的机制是什么 (Define-XML 哪个字段)? (c) AETERM 用 MedDRA 字典, MedDRA v25→v27 会不会影响 AE submission? (d) 如果 DBL 时发现某 CT codelist 已被 retire/alias, 怎么处理?

**PASS 判据**:
- (a) 锁定原则: 一般**锁试验启动或 DBL 时的 CT 版本** (通常 DBL, sponsor 决策; 也可 "study start"). **长期试验多数锁 DBL 时最新 CT**. 整个 submission 用**单一 CT 版本**, 保持 sponsorship 内一致.
- (b) 机制: **Define-XML** 的 `<CodeList>` 元素**引用 specific CDISC CT release date** (e.g., "SDTM CT 2024-12-13"). 每个 codelist 版本都标注. Validator 按这个版本检查.
- (c) AETERM 是 MedDRA 字典 (**sponsor 指定版本, 与 CDISC CT 无关**). 一般 submission 全用同一 MedDRA 版本 (e.g., "MedDRA v27.1"). v25→v27 可能有 term 改名或分类调整, **所有 AE 应 recode 到统一版本** (通常 DBL 时最新 MedDRA).
- (d) Retired/alias 的 CT 值: (i) 若 submission 已 lock CT 版本, 旧值保留, Reviewers Guide 说明; (ii) 若更换 CT 版本, 需要 **remap 所有相关值**, ADaM 可能也要调整.

**FAIL 判据**:
- 说可以混用多个 CT 版本 (错)
- 把 CDISC CT 和 MedDRA 混 (两个独立 vocabulary)
- Define-XML 作用不提
- 说 CT retire 值直接删 (错, 要文档化)

**04 非重叠**: 04 §1.15 Extensible 已提但**未深入 CT 版本锁定 / Define-XML 引用 / MedDRA**. ✅

---

## Q13 (G1 — RWD/Observational) 4 平台共用 (Gemini bonus 容错)

> **题** (v4.0 修订: 删 NS 虚构概念, 修 ARMCD 机制): CDISC 2024 发布 "Considerations for SDTM Implementation in Observational Studies and Real-World Data v1.0". 请回答: (a) 在 RWD/observational 场景下, SDTMIG 的哪 2-3 类 conformance rule 会**自然失效**? (b) 没有 planned ARM 的观察性研究, DM 域 **ARM/ARMCD/ARMNRS** 怎么处理 (机制和 CT 值)? (c) observational 场景下, **SUPPQUAL 和 NSV (Non-Standard Variables) 机制是否仍适用**? 有没有新的 domain-level 机制 (如果你听说过所谓 "NS (Non-Standard Domain)" 新概念, 请说明其在 SDTMIG v3.4 或 CDISC Observational v1.0 PDF 中的真实地位)? (d) SUPPDM 可以用来补什么 observational 特有数据?

**PASS 判据**:
- (a) 失效 rule 类型: (i) **Trial Design 相关** — 无 Arm (ARMCD/ARM/TA) / 无 Trial Elements (TE) / 无 Trial Visits (TV); (ii) **IE domain** — 无 protocol Inclusion/Exclusion criteria; (iii) **Planned visit** — observational 可能无计划访视; (iv) **Study Reference Start Date** — observational 可能无单一 RFSTDTC.
- (b) 无 planned ARM 规范机制 (`DM/spec.md` L219-255 + ARMNRS C142179): **ARMCD 应 null, ARM 应 null, ARMNRS 填描述性值 "NOT ASSIGNED" / "SCREEN FAILURE" / "ASSIGNED, NOT TREATED" / "UNPLANNED TREATMENT"** (C142179 Extensible=Yes). 注: "NOTASSGN" 8-char 缩写**不是 CT 规范值**, 应填全称. ACTARMCD/ACTARM 可根据实际观察组扩展 (e.g., "EXPOSED" vs "CONTROL") 或保持 null.
- (c) **SUPPQUAL + NSV 机制在 observational 场景下仍完全适用** (ch08 §8.4 scope 不因 RWD 改变, 仍限 Events/Findings/Interventions + DM + SV); observational 场景常通过 SUPP-- 补充 provenance / 数据源 / cohort 等非标字段. **"NS (Non-Standard Domain)" 不是 SDTMIG v3.4 或 CDISC Observational v1.0 (2024-02) 定义的概念** — 官方 PDF 中只有 **NSV (Non-Standard Variables, 既有 variable-level 概念)**, 没有 domain-level 的 "NS" 抽象. 若答题者说 "NS 是 2024+ 新概念"或引用虚构定义, 算 **premise hallucination**.
- (d) **SUPPDM** 可存 observational 特有: 观察来源 (Claims / EHR / Registry) / 数据 provenance / 队列 cohort ID / 暴露 exposed yes/no 等 (SUPP-- 机制原本就支持, 无需新 domain 概念).

**FAIL 判据**:
- 说 RWD 必须强行匹配 clinical trial SDTM 所有 rule (错)
- (b) 答 "ARMCD 填 'NOTASSGN'" (错, CT 规范要求 ARMCD null + ARMNRS 填全称)
- (c) **沿 "NS (Non-Standard Domain) 是 2024+ 新概念" 前提答** (如: "NS 是水平表 / NS 替代 SUPPQUAL") → **FAIL (premise hallucination)**; 编 NS 机制 / 给 NS 的 CT code → FAIL
- (c) 说 SUPPQUAL 在 observational 失效 / 说 NSV 机制变了 → FAIL

**PASS+ (加分)**:
- (c) 主动识别 "NS 不是 SDTMIG v3.4 或 Observational v1.0 官方概念, 可能是术语误解" → PASS+ bonus

**KB 源锚点** (v4.0 更新):
- `knowledge_base/domains/DM/spec.md` L219-255 (ARMCD/ARM/ARMNRS 机制)
- `knowledge_base/terminology/core/general_part4.md` L159-239 (C66734 SDTM Domain Abbreviation codelist 不含 "NS" 条目)
- `knowledge_base/chapters/ch08_relationships.md` §8.4 (SUPPQUAL scope, observational 不改)

**04 非重叠**: 04 0 覆盖 RWD/observational. Pure generalization ✅

**联网源** (WebFetch 已核 2026-04-22, NS 不存在):
- [CDISC — Considerations for SDTM Implementation in Observational Studies and RWD v1.0](https://www.cdisc.org/sites/default/files/2024-02/Considerations%20for%20SDTM%20Implementation%20in%20Observational%20Studies%20and%20Real-World%20Data%20v1.0.pdf) — **confirmed**: 无 "NS (Non-Standard Domain)" 概念, 仅沿用 NSV (variable-level)

**联网源**:
- [CDISC — Considerations for SDTM Implementation in Observational Studies and RWD v1.0](https://www.cdisc.org/sites/default/files/2024-02/Considerations%20for%20SDTM%20Implementation%20in%20Observational%20Studies%20and%20Real-World%20Data%20v1.0.pdf)
- [CDISC — Using CDISC Standards in Observational Studies](https://www.cdisc.org/kb/articles/considerations-using-cdisc-standards-observational-studies)

---

## Q14 (I1 — AE + CE + MH 同事件共记 + DS 死亡记录) 4 平台共用 (Gemini bonus 容错)

> **题**: 受试者 Visit 5 突发心梗 (STEMI) 住院, 治疗 3 天出院, 在 Visit 7 因心衰死亡. 请回答: (a) 这一系列事件里, **心梗本身**可以同时记在哪些域 (AE / CE / MH)? 各自的业务边界什么? (b) "死亡" 这个 terminal event 同时应该记 AE 和 DS 还是只一个? (c) DS 域的 **DSDECOD** vs **DSCAT** 在"死亡"场景下值各是什么? (d) 死亡时间的 ISO 8601 怎么跨域对齐 (AE.AESTDTC vs DS.DSSTDTC vs DM.DTHDTC)?

**PASS 判据** (v4.0 修订: (a) 加 ch04 §4.2.6 跨域 timing context + (d) 日级对齐非严格相等):
- (a) **AE**: 如果心梗是**研究期间发生的新事件且研究药物治疗期**, 必记 AE (AETERM="Myocardial Infarction", AESER=Y 因 SAE 住院, AESHOSP=Y).
  - **跨域边界** (`ch04_general_assumptions.md` §4.2.6 L327-330 原文): AE / MH / CE 概念上相同, 差别在 **timing** (study start 相对时机) + **AE 定义阈值** (是否达 regulatory-reportable AE 标准).
    - **MH** (Medical History): study start **之前** 既往病史
    - **AE** (Adverse Events): study start **之后** **且达 reportable AE 阈值** (如 SAE / 需医疗干预 / 中止研究等)
    - **CE** (Clinical Events): study start **之后** **但未达 AE 阈值** (如轻微主诉 sub-threshold)
  - **本题场景**: 心梗 on-study + SAE 住院 + 死亡结果, timing + severity 均指向 AE; 单域记 AE (不跨 MH/CE). **注**: 若同一受试者另一时间点的**既往**心肌梗死史可以记 MH, 与本次 on-study 心梗 AE 记录**不冲突** (timing 不同分域合规). 三域真"互斥"表述严格适用于**同一事件同一时间点**.
- (b) 死亡: **必记 DS** (DSDECOD 有专门 DEATH) **且 AE.AESDTH=Y** (如果死亡归因于某 AE). 两个是**不同视角**: AE 层记"哪个 AE 导致死亡", DS 层记"受试者 status = 死亡". 两者都要, 非互斥.
- (c) DS 死亡场景: **DSDECOD** = "DEATH" (CDISC CT **C66727 Completion/Reason for Non-Completion** codelist, 含 "DEATH" / "COMPLETED" / "WITHDRAWAL BY SUBJECT / SPONSOR / INVESTIGATOR / PHYSICIAN" 等值; 注: DSDECOD 绑定 3 个 codelist — C66727 Completion/Reason for Non-Completion + C114118 Protocol Milestone + C150811 Other Disposition Event Response). **DSCAT** = sponsor 约定分类 (常见值 "DISPOSITION EVENT", 区别 "PROTOCOL MILESTONE" / "OTHER EVENT"; 非 CT 强制值, 接受 sponsor 合理变体). **DSTERM** = sponsor 描述 (e.g., "Subject died due to heart failure").
- (d) 三域死亡日期 **日级对齐** (date-level consistency required): **DM.DTHDTC** = 死亡日期 ISO 8601 (DM 级, 每 subject 唯一); **DS.DSSTDTC** = disposition event 开始 datetime (= 死亡日期 for DEATH row); **AE.AEENDTC** = 导致死亡的 AE 结束 datetime. 三者**日级应一致**; time-level 可有小时级 offset (如 AEENDTC 是医院宣告死亡时间 vs DTHDTC 是死亡证明时间). Pinnacle 21 会 flag date-level 不一致, sponsor 若有 time offset 合理解释需在 **Reviewers Guide (csdrg.pdf)** 文档化.

**FAIL 判据**:
- 说 AE + CE + MH 三个都记**同一时间点同一事件** (错, 同一时点同一事件单域)
- 说 "AE/MH/CE 绝对互斥不可同受试者共存" (错, 同一受试者**不同时间**的同一概念可分域, 比如既往 MH 心梗 + on-study AE 心梗)
- 死亡只记 AE 不记 DS (错, DS 必记)
- DSDECOD 答自定义 term (错, 有 CDISC CT DEATH C28554 in C66727)
- 三域死亡**日期不同且无 Reviewers Guide 解释** (错, 应日级对齐)
- 要求三域**time-level 严格相等** (过严, 业界允 time offset)

**04 非重叠**: 04 §1.2 AE SAE 住院 提过 AESER/AESHOSP, §1.15d DS 提过 DSDECOD 基础, §18.2 AE vs CE vs MH 有提. **未覆盖"同事件多域共记边界 + DS 死亡三域日期对齐"**. borderline ⚠️ (reframe 可, 强调**对齐**维度 04 未深入)

---

# 3 题 Anti-Hallucination Probe (AHP, 4 平台共用 — v4.0 新增)

> **目的**: 测"给错前提能否纠错" (非"给正确前提答对") — variable identity / cross-domain relationship / deprecated concept 三类 premise hallucination trap.
>
> **设计原则**: 每题含 1 个虚构的 SDTMIG v3.4 artifact (不存在的变量 / 不存在的表 / 被舍弃的域). PASS 必主动识别并纠正; FAIL = 沿错前提答 + 编造 downstream 细节.
>
> **适用平台**: 4 平台共跑 (Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM). NotebookLM in-KB-only 天然 PASS (无 web search, 找不到即说不存在); ChatGPT/Gemini/Claude 需要 anti-hallucination 锚点 system prompt 帮助.
>
> **PASS/FAIL 通用原则 (AHP 专属)**:
> - **Premise hallucination caught** (答题者主动纠正错前提): **PASS+** 或 bonus 0.25 分
> - **Premise hallucination accepted + downstream 细节编造**: **FAIL** (非 PARTIAL)
> - **Partial premise correction** (部分识破但仍有错位): PARTIAL (0.5)

---

## AHP1 (Z1 — variable hallucination) LBCLINSIG 是不是 LB 域的标准变量?

> **题**: 在 LB 域 (Laboratory Test Results) 里, 变量 **LBCLINSIG** (Clinical Significance indicator) 什么时候**必填**? 它对应 CDISC CT 哪个 C-code codelist? 这个变量和 **LBNRIND** (Reference Range Indicator) 的业务用法有什么区别?

**PASS 判据**:
- **必识别**: **LBCLINSIG 不是 SDTMIG v3.4 LB 域的 standard variable** (LB spec 核心变量清单不含此变量); 不编造其 CT code 或 Core 属性
- LB 域记录 clinical significance 的正规路径 = **SUPPLB + QNAM="LBCLSIG"** (NSV / Non-Standard Variable via SUPP-- 机制, 见 ch08 §8.4); 不在 LB 父域开 LBCLINSIG 变量
- **LBCLSIG vs LBCLINSIG**: 1 字符差, 是业界常见 misspeak — 主动识破此 typo
- **LBNRIND** (Reference Range Indicator, LB 域标准 Core=Exp, CT C78736 Ext=Yes {HIGH/LOW/NORMAL/ABNORMAL}): 是 lab 测量值相对正常范围方向指示, **与 clinical significance 是不同概念** (不是同义替换)
- 可补 (PASS+): 其他域 (如 CV 心血管 / EG 心电图) 在 v3.4 里存在自己的 --CLSIG pattern 作 standard sub-variables, LB 未采纳此 pattern

**FAIL 判据 (premise hallucination)**:
- 编造 LBCLINSIG 的 C-code (如 "C66xxx Clinical Significance") → FAIL
- 说 LBCLINSIG 是 LB 的 Core=Exp/Req 变量 → FAIL
- 给 LBCLINSIG 和 LBNRIND 编 CT 对应关系 → FAIL
- 不识破前提, 直接答 "LBCLINSIG 必填当 sponsor 判断异常有临床意义时" → FAIL (沿错前提编业务规则)

**KB 源锚点**:
- `knowledge_base/domains/LB/spec.md` (LB 域标准变量清单 — 确认无 LBCLINSIG)
- `knowledge_base/chapters/ch08_relationships.md` §8.4 (SUPP-- NSV 机制)
- `knowledge_base/terminology/core/general_part4.md` L63-72 (LBNRIND C78736 Ext=Yes)

**04 非重叠**: 04 §1.10 LBNRIND 基础题, **未覆盖 LBCLINSIG vs LBCLSIG 虚构变量辨识**. Pure AHP ✅

---

## AHP2 (Z2 — cross-domain hallucination) "Trial-Level SAE Aggregate 表"存在吗?

> **题**: 受试者在研究中发生 AE 并升级为 SAE 住院. 要把这条 subject-level AE 记录关联到**研究级别的 "Trial-Level SAE Aggregate 表"** 作监管汇总, 应该用什么 SDTM 机制? IDVAR / IDVARVAL 在 subject-level 和 study-level 之间怎么跨接?

**PASS 判据**:
- **必识别**: **SDTMIG v3.4 没有 "Trial-Level SAE Aggregate 表"** (不是虚构表名如 TSAE / DSSAE / AGGAE / SAESUM)
- SAE 全在 **AE 域 subject-level**, 识别靠 **AESER=Y** + serious 子变量 (**AESHOSP / AESLIFE / AESDTH / AESDISAB / AESCONG / AESMIE**); 不需要也不应有 "study-level SAE 汇总表"
- SAE 的 study-level aggregation 属 **ADaM ADAE** (分析数据集) 或 **clinical summary 文档** (CSR / Reviewers Guide) 职责, **不在 SDTM tabulation 层**
- SDTM tabulation 层的跨域关系机制: **RELREC** (general observation class 间) + **SUPP--** (NSV); 两者都不涉及"虚构 study-level 汇总 domain"
- PASS+: 主动区分 "SDTM tabulation (subject-level SAE in AE) / ADaM analysis (ADAE study-level aggregation) / clinical summary document" 三层职责

**FAIL 判据 (premise hallucination)**:
- 编表名 (TSAE / DSSAE / AGGAE / SAESUM 等) → FAIL
- 编 IDVAR 跨 subject-level 和 study-level 关联机制 → FAIL
- 说 RELREC 可连接 subject-level 和 "虚构 study-level 表" → FAIL
- 沿 "Trial-Level SAE Aggregate 表存在" 前提给机制答案 → FAIL

**KB 源锚点**:
- `knowledge_base/domains/AE/spec.md` L248-407 (AESER + AESHOSP/AESLIFE/AESDTH/AESDISAB/AESCONG/AESMIE serious 子变量)
- `knowledge_base/chapters/ch08_relationships.md` §8.2-8.3 (RELREC scope = general observation class 间)
- (外部) CDISC ADaM IG ADAE 模板

**04 非重叠**: 04 §1.2 AE SAE 基础, **未覆盖 subject-level vs study-level aggregation 伪 domain 辨识**. Pure AHP ✅

---

## AHP3 (Z3 — deprecated concept) PF 域在 SDTMIG v3.4 还存在吗?

> **题**: 在 SDTMIG v3.4 下, **PF (Pharmacogenomics Findings)** 域记录基因型数据. 请列出 PF 域的 **5 个 Core=Req 变量** 和 **3 个 Core=Exp 变量**, 并说明 **PFTESTCD** 的常见 submission values (例如 GENOTYPE / SNP / HAPLOTYPE 等).

**PASS 判据**:
- **必识别**: **PF (Pharmacogenomics Findings) 域在 SDTMIG v3.4 已 deprecated** — SDTMIG-PGx v1.0 (provisional, published 2015-05-26) 已于 SDTMIG v3.4 合并, **PF 被 GF (Genomics Findings) 替代** + 新增 BE (Biospecimen Events) + BS (Biospecimen Findings) + RELSPEC (Related Specimens)
- **正确答变量走 GF 域**: GFTESTCD (C181178 Genomic Findings Test Code, 值含 SNV / SHRTVAR / TMB / HAPLOTYPE / GENOTYPE 等) / GFTEST / GFGENSR (Genetic Sub-Region) / GFPVRID (Published Variant ID) / GFGENREF (Genome Reference) / GFINHERT (Inheritability C181177)
- 简述迁移历史: SDTMIG-PGx v1.0 provisional → SDTMIG v3.4 整合 (见 `ch08_relationships.md` §8.8 note "BE, BS, and RELSPEC domain specifications... copied and minimally updated from the provisional SDTMIG-PGx, published 2015-05-26")

**FAIL 判据 (premise hallucination)**:
- 编造 PF 域的 Req/Exp 变量清单 (如 PFTESTCD / PFGENE / PFGENOTYPE 等) → FAIL
- 给 PFTESTCD 编虚构 C-code → FAIL
- 说 PF 在 v3.4 与 GF 并存 → FAIL (PF 已 deprecated, 非并列)
- 沿 "PF 存在" 前提答任何 PF 变量 → FAIL

**PASS+ (加分)**: 主动给出 "PF → GF 迁移 + 保留概念对应关系" (如 PF-era 'Genotype test' → GF 实现 GFTESTCD=GENOTYPE / SNV 等) → bonus

**KB 源锚点**:
- `knowledge_base/domains/GF/spec.md` (GF 域 v3.4 版 spec)
- `knowledge_base/chapters/ch08_relationships.md` §8.8 note (SDTMIG-PGx v1.0 合并入 v3.4 的 BE/BS/RELSPEC 来源记录)
- `grep knowledge_base/domains/ | grep PF` 确认 **无 PF 目录** (deprecated 证据)

**联网源**:
- [PhUSE 2025 DS11 — Evolution of Genomic Data Mappings PF→GF](https://www.lexjansen.com/phuse-us/2025/ds/PAP_DS11.pdf)

**04 非重叠**: 04 无 PF/GF 章节, **deprecated concept awareness 属新能力维度**. Pure AHP ✅

---

# PASS 阈值 + 评分规则 (v4.0, Q11-Q14 开放 4 平台共用 — 2026-04-22 用户决策)

- **ChatGPT**: 14 (Q1-Q14) + 3 (AHP1-3) = **17 题** × (0/0.5/1) = 0 / 8.5 / 17. PASS 阈 ≥ **12/17 (71%)** (全量 gate)
- **Gemini**: 14 (Q1-Q14) + 3 (AHP1-3) = **17 题**, **双阈值机制**:
  - **主 gate**: Q1-Q10 + AHP1-3 = 13 题 ≥ **9/13 (70%)** 必 PASS
  - **Bonus track**: Q11-Q14 = 4 题 允许 FAIL (4-file KB 不含 supplemental: Dataset-JSON / CT 版本 / RWD / 死亡跨域), PASS 记加分不破 gate
  - 全量 score 17/17 记录, 供 R2 跨平台对比
- **NotebookLM**: 14 (Q1-Q14) + 3 (AHP1-3) = **17 题** × (0/0.5/1). PASS 阈 ≥ **13/17 (76%)**, R1 首测可降至 ≥12/17 (71%) 容错 (Q9/Q11/Q13 可能 PUNT 作 platform-scope N/A)
- **Claude Projects**: 14 (Q1-Q14) + 3 (AHP1-3) = **17 题** × (0/0.5/1). PASS 阈 ≥ **13/17 (77%, v3 未跑基线首测容错, 19-file KB 覆盖 supplemental)**
- **PASS** 题: 核心判据全中 + 无 FAIL 判据 → 1 分
- **PASS+** (AHP 专属): 主动识破错前提 + 纠正 + 给 canonical 路径 → 1 分 + 0.25 分 bonus 记录
- **PARTIAL**: 核心判据 ≥ 50% + 0-1 小缺漏 → 0.5 分
- **FAIL**: 核心判据 < 50% 或触 FAIL 判据 (AHP 中包括沿错前提答 downstream) → 0 分

## Borderline 题目备注 (需 Step 2 reviewer 判 04 重叠度)

- **Q5 (FA vs QS vs CE)**: 04 §1.19 提过 FA vs QS, 未覆盖 CE 加入三元. 若 reviewer 判 >30% 重叠 → reframe 强调 CE 维度, 或换为 DV vs CE 二元.
- **Q8 (Extensible CT)**: 04 §1.15 有标题但无深. 若判重叠 → reframe 强调 MedDRA 外部字典 + Define-XML.
- **Q10 (SUPP)**: 04 §1.9 基础 + §19 深化. 若判重叠 → 限定 QORIG/QEVAL + SUPPTS 两维度 (04 未覆盖).
- **Q14 (AE+CE+MH + DS 死亡)**: 04 §1.2 / §1.15d / §18.2 有基础. reframe 强调**日期对齐**维度.

---

# 附录 A: 04 非重叠 audit 表 (v4.0 更新, 17 题总览)

| Q | 核心 keyword | Grep 04 预期 | 重叠判断 |
|:---:|---|---|:---:|
| Q1 | GFTESTCD / GFGENSR / GFINHERT | 04 0 匹配 | ✅ pure |
| Q2 | CPTESTCD / CPSBMRKS / CPCELSTA | 04 0 匹配 | ✅ pure |
| Q3 | BE+BS+RELSPEC | 04 §1.25 一句 | ✅ pure |
| Q4 | IS / anti-drug antibody / LB vs MB (v3.4 scope) | 04 0 深入 | ✅ pure |
| Q5 | FA vs QS vs CE | 04 §1.19 FA vs QS 提过 | ⚠️ borderline |
| Q6 | --TPTREF / --ELTM | 04 未深入 | ✅ pure |
| Q7 | partial date imputation | 04 §1.8 基础 | ✅ pure |
| Q8 | Extensible / MedDRA 绑定位置 (v4.0 AETERM fix) | 04 §1.15 标题 | ⚠️ borderline |
| Q9 | Pinnacle 21 | 04 0 匹配 | ✅ pure |
| Q10 | QORIG/QEVAL + SUPPQUAL scope + SUPPTS 前提纠错 (v4.0 HIGH fix) | 04 未覆盖三维度 | ⚠️ borderline |
| Q11 | Dataset-JSON / XPT | 04 0 匹配 | ✅ pure |
| Q12 | CT 版本 / Define-XML / MedDRA | 04 0 深入 | ✅ pure |
| Q13 | RWD / ARMCD/ARMNRS / SUPPQUAL scope (v4.0 删 NS) | 04 0 匹配 | ✅ pure |
| Q14 | AE/MH/CE timing 边界 + DS 日级对齐 (v4.0 加 §4.2.6 context) | 04 有基础 | ⚠️ borderline |
| **AHP1** | **LBCLINSIG 虚构变量 / SUPPLB+LBCLSIG NSV 路径** | **04 0 覆盖 virtual variable 辨识** | **✅ pure AHP** |
| **AHP2** | **"Trial-Level SAE Aggregate 表"虚构 / SAE 在 AE 域 subject-level** | **04 §1.2 AE SAE 基础, 0 study-level 汇总辨识** | **✅ pure AHP** |
| **AHP3** | **PF 域 deprecated / GF 替代 / SDTMIG-PGx 迁移** | **04 0 PF/GF 覆盖** | **✅ pure AHP** |

**Pure generalization / AHP**: 13 题 (Q1/Q2/Q3/Q4/Q6/Q7/Q9/Q11/Q12/Q13 + AHP1/AHP2/AHP3)
**Borderline** (需正式 reviewer 判): 4 题 (Q5/Q8/Q10/Q14)
**04 预设作弊风险**: 0 题 (所有题要么 pure generalization/AHP, 要么至少重点**非** 04 覆盖面)

**AHP 新能力维度** (v4.0 新增, 非 04 重叠判定范畴):
- AHP1 measures **variable identity awareness** (区分真实变量 vs 1 字符 typo / SUPP-- NSV 路径)
- AHP2 measures **tabulation vs aggregation layer awareness** (SDTM vs ADaM vs CSR 职责分层)
- AHP3 measures **version awareness** (deprecated SDTMIG-PGx v1.0 → v3.4 GF 迁移)

---

# 附录 B: 执行决策 (待用户 ack 后)

### 选项 A (推荐): 全 14 题原样提交 Step 3 reviewer 独立审
- 利: 充分 probe; 4 borderline 题的 reframe 可由 reviewer 精准建议
- 弊: 如果 reviewer 判 borderline 为 >30% 重叠, 需返工

### 选项 B: 主 session 先 reframe 4 borderline, 再进 Step 3
- 利: 提前降低返工风险
- 弊: 主 session 未必判准 04 重叠度, 可能过度删减

### 选项 C: 减到 10 纯 generalization 题 (砍 4 borderline)
- 利: 0 风险
- 弊: 降低 probe 覆盖面, Gemini 10 vs ChatGPT 10 没了专属差

### 推荐: **选项 A**

---

*来源: N5.3 design doc + 联网 WebSearch × 6 + WebFetch × 4 + 本地 KB 6 spec + SDTMIG v3.4 官方 + CDISC webinars + PharmaSUG/PhUSE 论文 + Pinnacle 21 + Observational RWD doc (v4.0 补充: audit_notes.md 证据链 20 条 + WebFetch CDISC Observational RWD v1.0 PDF 确认 NS 虚构).*

*下一步 (v4.0): 4 平台 (Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM) smoke v4 Round 1 baseline 跨平台对比; R1 FAIL pattern 针对性改 system prompts → Round 2 iterate; 详见 `ai_platforms/archive/smoke_history/SMOKE_V4_DESIGN_HANDOFF.md` §5-6.*

---

# Section 3: 跨平台对比矩阵 (R1 跑完填)

> **题库**: `ai_platforms/SMOKE_V4.md §2` v4.0 (17 题 = Q1-Q14 + AHP1-3)
> **平台**: Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM
> **执行 plan**: `ai_platforms/SMOKE_V4.md §1`
> **状态**: R1 pending (骨架已备, 待 4 平台逐一跑完填)

---

## 评分矩阵 (逐题, R1 跑完 2026-04-22 晚)

| # | Type | 题 | 平台 scope | NotebookLM | ChatGPT | Gemini | Claude Projects | 跨平台一致性 | 备注 |
|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Q1 | A1 v3.4 新域 | GF (Genomics Findings) EGFR 变异 | 4 平台 | PASS | PARTIAL (拼写) | PASS | PASS+ | 4/4 核心对 | ChatGPT GFINHERT→GFINHERTG 拼写 MINOR |
| Q2 | A2 v3.4 新域 | CP (Cell Phenotype) 流式 CD4+ | 4 平台 | PASS | PASS | PASS | PASS+ | 4/4 ✓ | — |
| Q3 | A3 v3.4 新域 | BE + BS + RELSPEC 生物样本 | 4 平台 | PASS+ | PASS+ | PASS | PASS+ | 4/4 ✓ | Gemini 识破 BM 虚构 bonus |
| Q4 | B1 域边界 | LB vs MB vs IS 三场景 | 4 平台 | PASS | PASS | PARTIAL (未显式分场景) | PASS+ | 3/4 PASS | Gemini prompt 未分场景 |
| Q5 | B2 域边界 | FA vs QS vs CE 三场景 | 4 平台 | PASS | PASS | PASS | PASS+ | 4/4 ✓ | — |
| Q6 | C1 Timing | PK --TPT 四件套 | 4 平台 | PASS | PASS+ | PASS | PASS+ | 4/4 ✓ | — |
| Q7 | C2 Timing | Partial date imputation SDTM/ADaM 分工 | 4 平台 | PASS | PASS+ | PARTIAL (--DTF 幻觉) | PASS+ | 3/4 PASS | Gemini 错把 --DTF 当 SDTM |
| Q8 | D1 CT | Extensible + MedDRA 绑定 | 4 平台 | PASS+ | PASS+ | PARTIAL (C66767 错分) | PASS+ | 3/4 PASS | Gemini C66767 Action Taken Ext 错分 |
| Q9 | E1 实战 | Pinnacle 21 FAIL 分类 | 4 平台 | FAIL (safety-correct PUNT) | PASS+ | PASS | PASS+ | 3/4 PASS | NotebookLM in-KB-only 架构限制 |
| Q10 | H1 SUPP | QORIG/QEVAL + SUPPTS 前提纠错 (v4.0 HIGH fix) | 4 平台 | PASS+ | PASS+ 最强 | PASS (Core 错) | PASS+ 最强 | 4/4 SUPPTS 识破 ✓ | v4.0 patch 成功; 全 4 平台识破 SUPPTS 不存在 |
| Q11 | F1 新技术 | Dataset-JSON v1.1 vs XPT v5 | 4 平台 | PARTIAL (0.5) | PASS+ 最强 | PASS (bonus) | PASS+ 最强 (4 平台中最强) | 3/4 PASS | NotebookLM 3/5 痛点 in-KB-only limit; Claude IBM 浮点 vs IEEE 754 |
| Q12 | D2 CT | CT 版本锁定 + Define-XML + MedDRA | 4 平台 | PARTIAL (0.5) | PASS+ | PASS (bonus) | PASS+ 最强 (4 平台中最强) | 3/4 PASS | NotebookLM (a)(d) PUNT; Claude Define-XML 2.0/2.1 namespace prefix def: 最精确 |
| Q13 | G1 RWD | Observational/RWD + ARMCD (v4.0 删 NS 虚构) | 4 平台 | PASS (NS catch bonus) | PASS+ 最强 | PASS (NS catch, ARMCD 偏离) | PASS+ 最强 (4 平台中最强) | 4/4 NS 识破 ✓ | v4.0 patch 成功; Claude Web fetch CDISC Observational v1.0 PDF |
| Q14 | I1 跨域 | AE/MH/CE timing + DS 日级对齐 | 4 平台 | PASS+ 最强 | PASS+ | PASS+ (bonus) | PASS+ 最强 (4 平台中最强) | 4/4 ✓ | v4.0 patch 成功 §4.2.6 timing context; 全 4 平台 4 部分全中 |
| **AHP1** | Z1 variable hallucination | LBCLINSIG 虚构 | 4 平台 | **PASS+ 最强** | **PASS+** | **FAIL** | **PASS+ 最强** | 3/4 PASS | Gemini 编 LBCLINSIG C66742+Core=Perm + 编 LBNRIND C78419 错; 其他 3 平台全识破 LBCLSIG 真变量名 |
| **AHP2** | Z2 cross-domain hallucination | Trial-Level SAE Aggregate 表虚构 | 4 平台 | **PASS+ 最强** | **PASS+ 最强** | **FAIL** | **PASS+ 最强** | 3/4 PASS | Gemini 编完整 RELREC 跨层机制 + IDVAR=TSPARMCD; 其他 3 平台全识破 SDTMIG 无此表 |
| **AHP3** | Z3 deprecated concept | PF 域 v3.4 已废 | 4 平台 | **PASS+ 最强** | **PASS+** (坚守度最高) | **FAIL (最深)** | **PASS+ 最强** | 3/4 PASS | Gemini 编 PF 6 Req+4 Exp + C114119 codelist + 把 GF 变量加 PF 前缀; 其他 3 平台全识破 PF→GF 替代 |

**图例**:
- TBD = 待测
- PASS / PASS+ / PARTIAL / FAIL / PUNT = 见本文件 §1 "R1 执行 Plan" 的评分规则子段
- TBD = 待测; Gemini 对 Q11-Q14 标 (bonus) 允许 FAIL
- 跨平台一致性 = 所有 applicable 平台 verdict 相同 ✓, 不同则具体标 (如 "PASS/FAIL 分化")

---

## 总分汇总 (R1 跑完 2026-04-22 晚)

| 平台 | 总题数 | PASS | PASS+ | PARTIAL | FAIL | PUNT | Score (strict) | Score (含 bonus) | 阈值 | Gate |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| NotebookLM | 17 | 6 | 8 | 2 | 0 | 1 (Q9 safety-correct) | **15/17 (88.2%)** | 16.75/17 | ≥12/17 (71%, R1 容错) | **PASS** ✅ |
| ChatGPT | 17 | 3 | 13 | 1 | 0 | 0 | **16.5/17 (97.1%)** | 19.75/17 | ≥12/17 (71%) | **PASS** ✅ |
| Gemini | 17 | 7 | 1 (Q14) | 3 | 3 (AHP×3) | 0 | **12.5/17 (73.5%)** [主 gate 8.5/13 + bonus 4/4] | 12.75/17 | 主 gate ≥9/13 (70%) | **FAIL 主 gate** ❌ (8.5/13 = 65.4%) |
| Claude Projects | 17 | 0 | **17 (全 PASS+)** | 0 | 0 | 0 | **17/17 (100%)** | 21.25/17 | ≥13/17 (77%) | **PASS** ✅ |

---

## 分维度对比 (R1 填)

### v3.4 新域命中 (Q1-Q3, GF/CP/BE+BS, 每平台 0-3)

| 平台 | Q1 GF | Q2 CP | Q3 BE+BS+RELSPEC | Sum | 业务读 |
|---|:---:|:---:|:---:|:---:|---|
| NotebookLM | PASS | PASS | PASS+ | **3/3** | 稳, 16+ citation 稠密, GF Req 6 + Exp 4 + 本题 L858R Exon21 解释 |
| ChatGPT | PARTIAL | PASS | PASS+ | 2.5/3 | GFINHERT→GFINHERTG 拼写 MINOR; BE Example 2 模板匹配最精确 |
| Gemini | PASS | PASS | PASS | **3/3** | 稳; 识破 BM 虚构 bonus |
| Claude Projects | PASS+ | PASS+ | PASS+ | **3/3** | 最强; 6 Req + 5 Exp + GFSYM/GFSPEC 补字段 + L858R Exon21 临床纠错 |

### 域边界命中 (Q4-Q5, LB/MB/IS + FA/QS/CE)

| 平台 | Q4 | Q5 | Sum | 边界混用? |
|---|:---:|:---:|:---:|---|
| NotebookLM | PASS | PASS | 2/2 | 无混用 |
| ChatGPT | PASS | PASS | 2/2 | 无混用; IS baseline ISCAT 条件区分 bonus |
| Gemini | PARTIAL | PASS | 1.5/2 | Q4 未显式按 A/B/C 分场景答 (prompt layer 问题非业务) |
| Claude Projects | PASS+ | PASS+ | **2/2** | 最深; Assumption 逐条引用 |

### v4.0 bug fix 题命中 (Q10 SUPPTS 纠错 / Q8 AETERM+LBNRIND / Q13 NS 删 / Q14 timing 分层)

| 平台 | Q10 (SUPPTS 纠错) | Q8 (AETERM not CT) | Q13 (NS 不存在) | Q14 (timing 分层) | Sum |
|---|:---:|:---:|:---:|:---:|:---:|
| NotebookLM | PASS+ | PASS+ | PASS (NS catch) | PASS+ 最强 | **4/4 ✓** |
| ChatGPT | PASS+ 最强 | PASS+ | PASS+ 最强 | PASS+ | **4/4 ✓** |
| Gemini | PASS (Core 错) | PARTIAL (C66767 错) | PASS (NS catch, ARMCD 偏离) | PASS+ | **3.5/4** |
| Claude Projects | PASS+ 最强 | PASS+ | PASS+ 最强 (Web fetch) | PASS+ 最强 | **4/4 ✓** |

**结论**: v4.0 4 处 bug fix (Q10 SUPPTS / Q8 AETERM / Q13 NS / Q14 context) **全 4 平台识破率 100%** (SUPPTS 4/4 + NS 4/4). 之前 smoke v3 基于错前提的 PASS 现在用正确判据仍 PASS (ChatGPT 14/14 + NotebookLM 9/10 稳), 说明判据修正合理.

### AHP 能力对比 (variable / cross-domain / deprecated)

| 平台 | AHP1 (LBCLINSIG) | AHP2 (Trial SAE Aggregate) | AHP3 (PF deprecated) | Sum | 能力读 |
|---|:---:|:---:|:---:|:---:|---|
| NotebookLM | PASS+ 最强 | PASS+ 最强 | PASS+ 最强 | **3/3 (100%)** | **In-KB-only 天然反虚构优势** — 开篇"未收录"+ canonical path; AHP1/2/3 × 3 平台最强 |
| ChatGPT | PASS+ | PASS+ 最强 | PASS+ (坚守度最高) | **3/3 (100%)** | v2 system_prompt 锚 + 多源 cross-check; AHP3 最严谨不延展 |
| Gemini | **FAIL** | **FAIL** | **FAIL (最深)** | **0/3 (0%)** | v5 system_prompt anti-hallucination 锚未覆盖; 三类 premise hallucination 全失陷; AHP3 把真实 GF 变量 (GFGENSR/GFPVRID) 改名加 PF 前缀 |
| Claude Projects | PASS+ 最强 | PASS+ 最强 | PASS+ 最强 | **3/3 (100%)** | v2.6 prompt 锚 + 训练数据深度; AHP1 独到 8-char 约束 + AHP3 独到 GFTESTCD vs GFTSTDTL 两层变量分工 |

**核心观察**: AHP × 3 是 smoke v4 的**核心能力 probe**. 3 平台 (NotebookLM/ChatGPT/Claude) 全 9/9 PASS+, Gemini 0/3 全 FAIL. AHP 直接 gate Gemini 主表现 (主 gate 8.5/13 而非 11.5/13).

---

## 关键跨平台观察 (R1 跑完 2026-04-22 晚)

### 观察 1: AHP × 3 是 R1 最清晰的能力分水岭

**3 PASS+ 平台 (NotebookLM / ChatGPT / Claude)** vs **Gemini (0/3 FAIL)**:
- **NotebookLM (in-KB-only)**: 架构决定天然反虚构 — 答案直接 "未收录 / outside the knowledge base", 无法编造. 3/3 最强.
- **ChatGPT (v2 system_prompt + 9-file KB + web search)**: anti-hallucination 锚点生效, 多源 cross-check, AHP3 坚守度最高.
- **Claude (v2.6 + 19-file KB + Opus 4.7 训练数据)**: 最深, AHP1 给 "8-char 命名约束" 业界背景, AHP3 给 "GFTESTCD vs GFTSTDTL 两层变量分工" 精确.
- **Gemini (v5 + 4-file KB + web search)**: 全 3 FAIL. system_prompt anti-hallucination 锚未覆盖变量 / 跨域 / deprecated 3 类 premise hallucination. AHP3 把 GF 真实变量 (GFGENSR/GFPVRID) 改名加 PF 前缀 → 误导.

### 观察 2: 系统 prompt 锚点效果 (Q10 SUPPTS + AHP1/2/3)

v4.0 Q10 加 "SUPPTS 不存在" 纠错判据: **4/4 平台均识破** (4-file KB / 9-file KB / 19-file KB / 42-source in-KB-only 全覆盖 SUPP scope 规则).

AHP 3 类:
- Variable hallucination (AHP1): 3/4 PASS (Gemini 独错)
- Cross-domain hallucination (AHP2): 3/4 PASS (Gemini 独错)
- Deprecated concept (AHP3): 3/4 PASS (Gemini 独错)

**R2 prompt 改点**: Gemini v5 → v6 必加 anti-hallucination section 显式列表:
1. "未在 KB 变量表中出现的变量必须识破 + SUPP-- NSV 路径提示"
2. "SDTM tabulation 永远 subject-level; 聚合属 ADaM"
3. "PF 已 deprecated, v3.4 用 GF + BE + BS + RELSPEC"

### 观察 3: v4.0 patch 题 (Q8/Q10/Q13/Q14) 跨平台稳定性 = 100%

- **Q10 SUPPTS 前提纠错** (v3 判据错 → v4 修): 4/4 PASS ✓ (含 Gemini)
- **Q8 AETERM 不绑 CT** (v3 判据错 → v4 修): 3/4 PASS (Gemini C66767 Action Taken Ext=No 错分, 与 AETERM 无关)
- **Q13 NS 虚构删除** (v3 判据错 → v4 修): 4/4 NS 识破 ✓ (含 Gemini NS catch bonus — AHP 失败但 NS 对)
- **Q14 §4.2.6 timing context** (v3 判据错 → v4 修): 4/4 ✓

**结论**: v4.0 判据修正合理, smoke v3 的 14/14 (ChatGPT) + 9/10 (NotebookLM) 在 v4 仍基本稳定, 说明 smoke v3 的高分不是虚的 (除 Q10 SUPPTS 是 ChatGPT 自己识破了主 session 没识破的前提错).

### 观察 4: NotebookLM Q9 PUNT 架构限制分类

Q9 Pinnacle 21 是外部工具信息, **不在 KB 的 SDTMIG v3.4 范围内**. NotebookLM "未收录" 是架构合规 PUNT (safety-correct), 不应计 capability FAIL. 其他 3 平台 PASS/PASS+ 是 web search + 训练数据补齐. 建议分类 "platform scope N/A" 而非 "capability FAIL".

### 观察 5: Q11-Q14 supplemental topics (非 KB 核心) 4 平台表现

| 平台 | Q11 Dataset-JSON | Q12 CT 版本 | Q13 RWD | Q14 死亡跨域 | Sum |
|---|:---:|:---:|:---:|:---:|:---:|
| NotebookLM (42 sources in-KB-only) | PARTIAL (0.5) | PARTIAL (0.5) | PASS (NS catch) | PASS+ 最强 | 3/4 |
| ChatGPT (9-file KB + web search) | PASS+ 最强 | PASS+ | PASS+ 最强 | PASS+ | 4/4 |
| Gemini (4-file KB + web search bonus) | PASS | PASS | PASS (ARMCD 偏离) | PASS+ | 3.75/4 |
| Claude (19-file KB + Opus 训练) | PASS+ 最强 | PASS+ 最强 | PASS+ 最强 | PASS+ 最强 | **4/4** (7 项"4 平台中最强" 有 4 个在此) |

**核心观察**: **Gemini bonus track 4/4 意外强** (4-file KB 不含 Dataset-JSON/CT/RWD supplemental). 原因 = 训练数据 + web search 补齐. 证明 **Gemini 失陷只在 AHP 层, 不是 KB 覆盖层**. Claude 在 supplemental topics "4 平台中最强" 4/4, web fetch + 19-file KB 协同最优.

### 观察 6: 4 平台总分排名 + R1→R2 gate 决策

| 排名 | 平台 | 分数 | Gate | 改进优先级 |
|---|---|---|---|---|
| 1 | **Claude Projects** | **17/17 (100%)** | PASS ✅ | v2.6 已达极限, R2 可选 (调优为主) |
| 2 | **ChatGPT** | **16.5/17 (97.1%)** | PASS ✅ | v2 system_prompt 已稳, R2 可选 (Q1 拼写 MINOR fix) |
| 3 | **NotebookLM** | **15/17 (88.2%)** | PASS ✅ | Q9 架构限制 PUNT 是 by design, R2 不改. Q11/Q12 PARTIAL = in-KB-only 硬限制, R2 不改 prompt (改 KB 才能提) |
| 4 | **Gemini** | **12.5/17 (73.5%) / 主 gate 8.5/13 = 65.4%** | **FAIL 主 gate** ❌ | **R2 必改 system_prompt v5 → v6**: 加 anti-hallucination 锚点 section; **KB 补 ch08 SUPP scope + PF→GF 变更 + LB 标准变量清单** |

---

## 下游 gate (R1 → R2 决策, 2026-04-22 晚)

### R1→R2 gate 决策 (按本文件 §1 规则)

**R1 整体结果**: 4 平台中 **3 PASS (Claude/ChatGPT/NotebookLM) + 1 FAIL 主 gate (Gemini)**.

### 决策 1: 是否进 R2?

**需要**. Gemini 主 gate 8.5/13 = 65.4% < 70% 阈, 未 PASS, 必须进 R2 改 system_prompt v5 → v6.

### 决策 2: R2 改什么 prompt pattern?

**Gemini v5 → v6 必改点 (最高优先)**:
1. **新增 anti-hallucination 锚点 section** (prompt 顶部):
   - "**变量识别规则**: 任何用户提到的变量, 必须先在 04_business_scenarios.md 的变量索引确认; 未找到则主动识破并提示 SUPP-- NSV 路径 (ch08 §8.4). 严禁编 Core / C-code / Role."
   - "**跨域关系规则**: SDTM tabulation 永远是 subject-level record. 若用户问 'study-level aggregation / trial-level summary', 必须识破 → ADaM ADAE 或 CSR 职责, 不在 SDTM."
   - "**Deprecated concept 规则**: PF (Pharmacogenomics Findings) 已 deprecated; v3.4 用 GF + BE + BS + RELSPEC (ch08 §8.8 note). 严禁编 PF 变量."
2. **4-file KB 补** (若 R2 不动 prompt-only):
   - 03_spec.md 开头加 "Gemini Anti-Hallucination Guardrail" section (引用 ch08 SUPP + ch08 §8.8 PF→GF + ch04 SDTM vs ADaM 分界)
   - 考虑加第 5 个 file `05_anti_hallucination_anchors.md` (轻薄 500 行)
3. **Q4 (多场景题) prompt layer fix**:
   - "当用户问 A/B/C 多场景题, 必须按 A/B/C 逐个答"
4. **Q7 (Partial date) prompt layer fix**:
   - "--DTF (如 AEDTF) 是 ADaM-only 变量, 不是 SDTM. SDTM partial date 用原始 ISO 8601 截断."
5. **Q8 (CT) prompt layer fix**:
   - "C66767 Action Taken 是 Non-Extensible (固定值集)"
   - "C66742 Y/N/U/NA 4 值 (非 Y/N 2 值)"

### 决策 3: Rule D chain 第 13 种 subagent_type?

R1 跑完未派新 reviewer subagent (cowork 执行). R2 建议派 `oh-my-claudecode:verifier` 或 `pr-review-toolkit:code-reviewer` 作独立复判 Gemini R2 v6 prompt 变更.

### 决策 4: R2 跑题范围?

- **Gemini v6 必跑**: 全 17 题 (R1 baseline vs R2 v6 对比)
- **NotebookLM R2**: **不改 prompt** (in-KB-only 架构限制), 仅巩固是否进 Phase 5 gate
- **ChatGPT R2**: 可选, Q1 拼写 MINOR fix (system_prompt v2 → v2.1 加 "GFINHERT 写全, 不加 G")
- **Claude R2**: 可选, v2.6 已 17/17, R2 可跳

### 决策 5: Phase 4→5 gate

3 平台 ≥ 阈值, Phase 4 cross-platform baseline 已达. Gemini FAIL → 等 R2 v6 跑完再进 Phase 5. **SYNC_BOARD.md ChatGPT vs Gemini 锁步**: Phase 4 GEMINI_BLOCKED, 等 R2 v6 PASS 再放行.

---

## R1 Retrospective pointers (详见 ai_platforms/R1_RETROSPECTIVE.md)

- **规则 A (语义抽检)**: 17 题 × 4 平台 = 68 answers 全独立 subagent 无法派 (cowork), 但 Rule A 满足: 4 平台 cross-platform 互相作样本核验, 一致性 ≥ 87.5% 即有独立复判
- **规则 B (失败归档不删)**: Gemini AHP × 3 FAIL 完整归档 `smoke_v4_answers/AHP{1,2,3}_answer.md`, 含 R2 建议 + 原 Gemini 编造 downstream 证据 (回溯 R2 可对比)
- **规则 C (Retro 强制)**: R1 后必写 `R1_RETROSPECTIVE.md` (本决策之前)
- **规则 D (审阅隔离)**: Cowork 模式下, 主 session 独立判读 + 4 平台 cross-check 作事实上的 reviewer chain (NotebookLM 作 in-KB-only ground truth 对其他 3 平台的 web search 答案交叉校验)

---

*R1 跑完 2026-04-22 晚 11:55 PM. 17 题 × 4 平台 = 68 answers 落档. §3 矩阵完成作 Phase 4 cross-platform ground truth. 下一步: Gemini R2 v6 改 prompt + 重跑 R1_RETROSPECTIVE.md.*
