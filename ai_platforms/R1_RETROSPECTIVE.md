# R1 Retrospective — smoke v4 baseline 4 平台跑题

> **Date**: 2026-04-22 晚 11:55 PM
> **Scope**: smoke v4 R1 baseline 17 题 (Q1-Q14 + AHP1-3) × 4 平台 (NotebookLM / ChatGPT / Gemini / Claude Projects) = 68 answers
> **Rule C (强制)**: Tier 2/3 项目收尾必写 RETROSPECTIVE. 本文作 R1 lifecycle 收尾, 为 R2 plan 输入.
> **前置文件**:
> - 题库 + R1 plan: `ai_platforms/SMOKE_V4.md`
> - 4 平台 results.md: `ai_platforms/{notebooklm,gemini_gems,chatgpt_gpt,claude_projects}/dev/evidence/smoke_v4_results.md`
> - 4 平台 answers: `ai_platforms/*/dev/evidence/smoke_v4_answers/Q{1-14}_answer.md` + `AHP{1,2,3}_answer.md`
> - 跨平台矩阵: `SMOKE_V4.md §3`

---

## 1. R1 整体结果 (摘自 SMOKE_V4.md §3)

| 排名 | 平台 | Score (strict) | Gate | 核心观察 |
|---|---|---|---|---|
| 1 | **Claude Projects** | **17/17 (100%)** | PASS ✅ | 全 17 题 PASS+; 7 题"4 平台中最强" (Q11-Q14 + AHP × 3) |
| 2 | **ChatGPT** | **16.5/17 (97.1%)** | PASS ✅ | 13 PASS+ / 3 PASS / 1 PARTIAL (Q1 GFINHERT 拼写); AHP × 3 全 PASS+ |
| 3 | **NotebookLM** | **15/17 (88.2%)** | PASS ✅ | 8 PASS+ / 6 PASS / 2 PARTIAL (Q11/Q12 supplemental PUNT) / 1 PUNT (Q9 架构限制); AHP × 3 全 PASS+ 最强 |
| 4 | **Gemini** | **12.5/17 (73.5%), 主 gate 8.5/13 = 65.4%** | **FAIL 主 gate** ❌ | 8.5/10 Q1-Q10 + 0/3 AHP + 3.75/4 bonus Q11-Q14 |

---

## 2. 保留下来的做法 (Rule C 第 1 段 — 确认有效应继续)

### R1-1. cowork + 4 平台并发 fire → 循环回收

**做法**: 每题 fire NotebookLM → Gemini → ChatGPT → Claude 4 个浏览器 tab, 然后循环回收. Gemini 最快 (~1 min), NotebookLM/ChatGPT/Claude 2-5 min extended reasoning.

**为什么保留**: 4 平台串行执行 = 68 × 3 min ≈ 3.4 小时; 并发 fire = 17 × 5 min ≈ 1.4 小时. 节省 60% 时间.

**条件**: 每题 prompt 完全一致 (Ctrl-C / Ctrl-V from SMOKE_V4.md §2), 保证 cross-platform 可比.

### R1-2. Anti-hallucination probe (AHP × 3) 作核心能力 gate

**做法**: v4.0 新增 3 题 AHP (variable / cross-domain / deprecated premise hallucination) 测"给错前提能否纠错".

**为什么保留**: AHP × 3 是 R1 最清晰的能力分水岭 — Gemini 在 Q1-Q10 主表现 8.5/10 还过得去, AHP × 3 全 FAIL 直接把主 gate 拉到 65.4% < 70% 阈. 没有 AHP, Gemini 会 "假 PASS" 通过.

**对比维度**: NotebookLM (in-KB-only 天然反虚构) / ChatGPT v2 system_prompt (锚生效) / Claude v2.6 (训练数据深度) / Gemini v5 (锚缺失) 4 种机制的 anti-hallucination 能力对比.

### R1-3. v4.0 bug fix 判据 (Q8/Q10/Q13/Q14)

**做法**: 基于 P3.8 主 session 独立复判的 5 findings, v4.0 修正了 4 处判据错 (Q10 SUPPTS 前提纠错 / Q8 AETERM 不绑 CT / Q13 NS 虚构删 / Q14 §4.2.6 timing context).

**为什么保留**: R1 跑完证明判据修正合理 — 4/4 平台 SUPPTS 识破 + NS 识破 + §4.2.6 timing 识破, 之前 smoke v3 的高分 (ChatGPT 14/14 + NotebookLM 9/10) 在 v4 基本稳定, 说明 smoke v3 的高分不是虚的, 是判据错 + 答对"错前提"的巧合.

### R1-4. 双阈值机制 (Gemini 主 gate + bonus track)

**做法**: Gemini 4-file KB 不含 supplemental (Dataset-JSON / CT 版本 / RWD / 死亡跨域), 设主 gate Q1-Q10+AHP ≥9/13 + bonus Q11-Q14 容错 FAIL.

**为什么保留**: 实际结果 Gemini bonus track 4/4 意外强 (训练数据 + web search 补齐 KB gap), 证明 bonus 设计合理 — 不把 KB 覆盖缺陷误判为能力 FAIL.

### R1-5. 4 平台 cross-check 作独立 reviewer chain (Rule D 变体)

**做法**: cowork 模式下主 session 逐题判读 4 平台答案, 跨平台互相作"样本复核" (e.g. NotebookLM 说"PF 已被 GF 取代" → 证实 Gemini AHP3 编造的 PF 6 Req 是 FAIL).

**为什么保留**: 每题 4 份独立答案 + 判据对照, 构成事实上的多 reviewer chain. Rule D "审阅隔离" 满足 (4 平台不是同一 agent 同一 session 自审).

---

## 3. 必须补上的缺口 (Rule C 第 2 段 — 下次 R2 或后续项目必改)

### G1. Rule A 语义抽检强度不够

**问题**: R1 每平台答案主 session 自己判读, 未派独立 subagent 做"N 样本独立核验". Rule A 要求"压缩率 >50% 或改写率 >50% 必做 N 样本独立抽检".

**影响**: 17 题 × 4 平台 = 68 answers 只有 cowork + 跨平台 cross-check, 缺对 **主 session 判读本身** 的独立复核. 如主 session 把 "ChatGPT AHP1 隐式识破" 判 PASS+, 但可能 Rule D reviewer 会更严格判 PASS (无 "最强").

**R2 必补**:
1. 派 `pr-review-toolkit:code-reviewer` 或 `oh-my-claudecode:verifier` 作**独立复判 subagent**, 读 4 平台 answer.md 独立打分 (不见主 session self-score), 然后 cross-check 差异.
2. 保留 Rule A "每 3 个 platform 一次 N=3 独立抽检" 到 subagent_prompts/.

### G2. Gemini FAIL pattern 未在 R1 内立即修

**问题**: R1 发现 Gemini AHP × 3 全 FAIL, 主 session 记录 "R2 建议" 但 R1 内未派 agent 立即改 system_prompt v5 → v6. 导致 R2 session 从零开始读 FAIL 证据.

**R2 必补**:
1. R2 session 启动第一件事: 读 `ai_platforms/gemini_gems/dev/evidence/smoke_v4_answers/AHP{1,2,3}_answer.md` 的 "R2 建议" 部分, 合并成 v6 prompt draft.
2. v6 draft 必含 3 段 anti-hallucination section (变量 / 跨域 / deprecated).

### G3. Rule D chain 第 13 种 subagent_type 未派

**问题**: R1 cowork 自跑, 未激活 Rule D chain. 之前 12 种 subagent_type 已烧到 P3.8 reviewer (`oh-my-claudecode:document-specialist` 第 11th slot).

**R2 必补**:
1. 派 `pr-review-toolkit:code-reviewer` (Rule D 13th slot) 独立复判 R1 全 68 answers + 判 Gemini v5 → v6 prompt draft 合理性.
2. 或派 `oh-my-claudecode:verifier` 作 R2 gate check.

### G4. SYNC_BOARD.md 未更新

**问题**: R1 跑完后 SYNC_BOARD.md Phase 4 状态应转为 "3 平台 PASS, Gemini BLOCKED". 未同步.

**R2 必补**: 更新 SYNC_BOARD.md Phase 4 矩阵 + 各平台 _progress.json checkpoints_acked 数组.

### G5. Q11/Q12 NotebookLM PARTIAL 未系统化为 in-KB-only 硬限制

**问题**: NotebookLM Q11 Dataset-JSON / Q12 CT 版本 PARTIAL 是因为 42-source KB 不深入 supplemental topics, 非能力 FAIL. 这与 Q9 Pinnacle 21 FAIL-PUNT 性质一样, 但分类不同.

**R2 必补**: 统一分类 "in-KB-only architectural PUNT" 为 "architecture-scope N/A" 单独 bucket, 不与 capability FAIL/PARTIAL 混计总分.

---

## 4. 关键决策复盘 (Rule C 第 3 段)

### D1. v4.0 AHP × 3 新增决策

**决策**: 在 smoke v3 → v4 升级时, 加 AHP × 3 (variable/cross-domain/deprecated).

**回头看**: **正确且高价值**. AHP × 3 是 R1 最清晰的能力分水岭. 没有 AHP, 无法把 Gemini 从其他 3 平台分开.

**支持证据**: Gemini Q1-Q10 + Q11-Q14 = 12.25 分通过主能力基本判据, AHP × 3 = 0 分直接拉到 FAIL. 若没 AHP, Gemini 12.5/17 勉强过 71% 阈.

### D2. Gemini 双阈值机制决策

**决策**: 为 Gemini 设主 gate (Q1-Q10+AHP ≥9/13) + bonus (Q11-Q14 容错).

**回头看**: **正确**. Bonus Q11-Q14 4/4 PASS 避免 KB 覆盖 bias 拖低总分. 但应**更严**: AHP × 3 全 FAIL 时, 即使 Q1-Q10 全 PASS 也应该是 FAIL (核心能力缺失).

**R2 调整**: 考虑把 AHP × 3 设 **hard gate** — 主 gate 阈值改为 "Q1-Q10 ≥7/10 + AHP ≥2/3", 而非单一 ≥9/13 summing pass.

### D3. NotebookLM Q9 Pinnacle 21 分类决策

**决策**: FAIL 但 safety-correct PUNT, 不计主 gate 阈值失败.

**回头看**: **正确**. Pinnacle 21 是 KB 外部工具, 架构限制应算 scope N/A 不算 capability FAIL. NotebookLM 给出 "SDTMIG §3.2.2 10 条 conformance rule" upstream 补齐, 行为合规.

**R2 保持**: 不改.

### D4. cowork 执行模式决策 (vs subagent 派发)

**决策**: R1 用 cowork (主 session 自跑 Chrome MCP) 而非派 subagent.

**回头看**: **部分正确**. cowork 效率高 (1.4 小时跑完), 但 Rule A 样本抽检 + Rule D 审阅隔离 不满足. R2 应考虑混合模式 — cowork 跑题 + 派 subagent 作独立 reviewer.

**R2 调整**: R2 跑 Gemini v6 时, 派 `verifier` subagent 独立判 v6 17 题. Claude/ChatGPT/NotebookLM 若不重跑, subagent 只审 Gemini.

### D5. Rule E 候选 (新规则提议)

基于 R1 经验, 提议新增 **Rule E (跨平台 cross-check)**:

> **任何 AI 平台能力测试 (smoke test / benchmark), 必须至少 3 平台并发跑同题, 作事实上的 multi-reviewer baseline. 若 <3 平台, 不能单平台结果作 ground truth.**

**理由**: R1 证明 Gemini 单平台 AHP × 3 FAIL 若没有其他 3 平台作对比, 主 session 很难判断是"题目难" vs "平台能力"问题. 4 平台 3/4 PASS 给出了无歧义的"平台能力差异" ground truth.

---

## 5. R2 Plan pointers (基于 G1-G5 缺口)

### R2-0. 前置 (新 session 启动)

1. 读 `ai_platforms/R1_RETROSPECTIVE.md` (本文)
2. 读 `ai_platforms/SMOKE_V4.md §3` 跨平台矩阵
3. 读 Gemini AHP × 3 answer.md 的 "R2 建议" 部分 (3 个文件)

### R2-1. Gemini v6 system_prompt (最高优先)

1. 在 v5 (7925/8000 chars) 基础上加 anti-hallucination section (~500 chars)
2. Draft 结构:
   ```
   ### ANTI-HALLUCINATION GUARDRAIL (v6 新增)
   规则 1: 变量识别 — [详细]
   规则 2: 跨域关系 — [详细]
   规则 3: Deprecated concept — [详细]
   ```
3. 字符预算: 7925 + 500 = 8425, 超 8000 lim. **需先压缩 v5 既有 CO-4 4-file KB 引用**.

### R2-2. 派 `pr-review-toolkit:code-reviewer` 独立复判 R1 + v6 draft

Prompt: "read R1_RETROSPECTIVE.md + SMOKE_V4.md §3 矩阵 + 4 平台 results.md, independent verdict on (1) main-session scoring accuracy, (2) Gemini v6 prompt draft adequacy for AHP × 3 fix"

### R2-3. 跑 Gemini v6 × 17 题, 对比 R1 baseline

阈值: AHP × 3 必 ≥2/3 (hard gate); Q1-Q10 ≥7/10. 若 Gemini v6 AHP ≥2/3 PASS, Phase 4 gate 开闸. 否则 v6 → v7 迭代.

### R2-4. 更新 SYNC_BOARD.md + _progress.json

Phase 4 矩阵: ChatGPT_PASSED / Gemini_R2_BLOCKED → Gemini_R2_PASSED (after R2 PASS).

### R2-5. Rule D chain 第 13 slot: 代码/方案独立复核

已用 12 种 subagent_type, R2 候选:
- `pr-review-toolkit:code-reviewer` (13th)
- `oh-my-claudecode:verifier` (13th alternate)

---

## 6. Rule A/B/C/D/E 合规自查

- **Rule A (语义抽检)**: **部分不满足** (cowork 主 session 判读, 未派 subagent 样本核验) → G1 补
- **Rule B (失败归档不删)**: **满足** — Gemini AHP × 3 FAIL 完整归档 `smoke_v4_answers/AHP{1,2,3}_answer.md`, 含编造 downstream 证据 + R2 建议. 回溯可查.
- **Rule C (Retro 强制)**: **满足** — 本文即 retro, 3 段 (保留 / 缺口 / 决策) 全写.
- **Rule D (审阅隔离)**: **部分满足** — 4 平台 cross-check 作事实上的 reviewer chain, 但未派 subagent 作 主 session 判读的复核 → G3 补.
- **Rule E (新提议)**: **满足** — 4 平台并发 ≥3, 有 multi-reviewer baseline.

---

## 7. 产物清单 (R1 lifecycle artifacts)

### 代码/脚本
- 无新脚本 (cowork via Chrome MCP).

### 文档
- `SMOKE_V4.md` — 题库 + R1 plan + §3 跨平台矩阵 (全量填 R1 数据)
- `R1_SESSION_HANDOFF.md` — R1 进度 2 版 handoff (Q14+AHP 前 / 全部 R1 完)
- `R1_RETROSPECTIVE.md` (本文) — Rule C 产物

### 4 平台 evidence (每平台 smoke_v4_answers/)
- 17 answer.md × 4 平台 = 68 文件 (每个 含题干 + raw 答 + self-score verdict + 判据对照)
- 4 × smoke_v4_results.md (每平台分项 + 总分 + 主结论)

### 跨平台矩阵
- SMOKE_V4.md §3 — 17 题 × 4 平台 verdict 矩阵 + 4 分维度 sub-matrix (v3.4 新域 / 域边界 / v4 bug fix / AHP) + 排名

### 待产 (R2)
- `R2_PLAN.md` (基于本 retro §5)
- Gemini `system_prompt_v6.md` draft (基于 §4.1)
- `pr-review-toolkit:code-reviewer` 独立复判 report

---

*v1.0 2026-04-22 晚 11:55 PM. R1 baseline 4 平台跑完, 3/4 PASS + Gemini FAIL 主 gate. 下一步: R2 Gemini v6 prompt fix + 派独立 reviewer subagent.*
