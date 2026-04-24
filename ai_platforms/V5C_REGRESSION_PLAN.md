# V5C Full Regression Verification Plan (Q4-Q10 双平台 N5.4 等价假设实测)

> **Purpose**: 消化 Phase 5 retrospective §2 G5-4 "Q4-Q10 v5c 等价 10/10 假设未实测" 缺口. 双 Phase 4 reviewer #24 M-2 + #25 MED-1 独立交叉 flag 要求的 verification task.
> **Scope**: ChatGPT GPTs + Gemini Gems 两平台, smoke v4 Q4-Q10 共 7 题 × 2 平台 = 14 answer.md 新增
> **Status**: 🟡 **V5C 自评完成 pending Rule D reviewer** (2026-04-24 执行完毕 — ChatGPT v2.2 + Gemini v7 两平台各 Q4-Q10 = 14 答 strict **14/14 PASS** 主 gate 通过; self-score 详 `chatgpt_gpt/dev/evidence/smoke_v4_v2_2_regression_results.md` + `gemini_gems/dev/evidence/smoke_v4_v7_regression_results.md`); 待 15th R2-line reviewer 独立复核
> **前置**: `ai_platforms/PHASE5_RETROSPECTIVE.md §2 G5-4` / `SMOKE_V4.md §2 Q4-Q10` / `SMOKE_V4.md §3 跨平台矩阵` / `gemini_gems/dev/ab_reports/STAGE_N5.4_AB_REPORT.md` / `chatgpt_gpt/dev/ab_reports/STAGE_N5.4_AB_REPORT.md`
> **优先级**: Phase 5 post-sign-off optional, 不阻塞 Phase 5 FINAL

---

## §1 问题背景

### 1.1 假设内容

ChatGPT+Gemini N5.4 Phase 4 结论: "**Q4-Q10 v5c 等价 10/10**" (两平台分别).

**推理链**:
- v5c 改了 CO-4 (GF/CP/BE/BS v3.4 新域变量硬锚), 只影响 Q1/Q2/Q3 (v3.4 新域题)
- v5c 不动 CO-1 (AE Core) / CO-1b (DM ACTARM) / CO-2 (NCI EVS) / CO-2c (ARM/ACTARM CT) / CO-3 (源路径)
- KB uploads 不变 (9 文件 ChatGPT / 4 文件 Gemini)
- **∴** Q4-Q10 (不涉及 v3.4 新域) 无回归风险, 保持 N5.2 smoke v2.1 baseline 10/10

### 1.2 为什么这是"假设"

**实测仅 3 题** (Q1 GF / Q2 CP / Q3 BE+BS), Q4-Q10 没跑 apples-to-apples v5c baseline. 推理基于 "不改的部分不变", 但 prompt-level change 的 prime-position dilution / attention re-weighting 是已知 LLM 现象, 不能纯靠代码 diff 推论.

### 1.3 双 reviewer 独立交叉 flag

- **ChatGPT Phase 4 reviewer #24 (`oh-my-claudecode:code-reviewer`)**: M-2 "Q4-Q10 等价假设未引 diff hash provenance", Gate OPEN 不阻塞但 Phase 5 必须正式注册 verification task.
- **Gemini Phase 4 reviewer #25 (`feature-dev:code-explorer`)**: MED-1 "Q4-Q10 regression 需 Phase 5 正式注册", 独立 KB grep 确认 CO-4 修改边界 clean, 但仍要求回归实测.

**两 reviewer 独立 flag 同一 MEDIUM 点 = 真实弱点, 非 reviewer 过敏.**

---

## §2 执行手顺 (Chrome MCP cowork)

### 2.1 前置条件

- Gemini Gem 已 apply v5c (live 11,132 chars, current `gemini_gems/current/system_prompt.md`)
- ChatGPT GPT 已 apply v2.1 (live 5,681 chars, current `chatgpt_gpt/current/system_prompt.md`)
- **若先做 v7 (Gemini) / v2.2 (ChatGPT) apply, 本 regression 阈值要求相应调整** (v7/v2.2 在 Q4-Q10 无新改, 等价 v5c/v2.1)
- 新 chat (fresh context), 每题独立 chat, 不 cross-question 污染

### 2.2 跑题顺序

**每平台单 session 连续跑, 不并发** (保 prompt 一致):

```
Gemini: Q4 → Q5 → Q6 → Q7 → Q8 → Q9 → Q10  (~15-25 min)
ChatGPT: Q4 → Q5 → Q6 → Q7 → Q8 → Q9 → Q10  (~25-35 min)
```

**Note**: Q11-Q14 是 ChatGPT 专属 bonus 题, 本 regression 不重跑; Q1-Q3 已有 R1+R2 实测, 不重跑; AHP × 3 对 Gemini R2 已做 (post-v6), 对 ChatGPT R1 已做 (post-v2.1), 不重跑.

### 2.3 题目源

题库固定 `ai_platforms/SMOKE_V4.md §2 Q4-Q10`, 不修改. 直接 Ctrl-C / Ctrl-V 到 Gem / GPT 对话框.

### 2.4 答案落档

- Gemini: `ai_platforms/gemini_gems/dev/evidence/smoke_v4_v5c_regression_answers/Q{4-10}_answer.md`
- ChatGPT: `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v4_v2_1_regression_answers/Q{4-10}_answer.md`
- 每文件 DOM 回读原文 + 主 session inline self-score (PASS/PARTIAL/FAIL + 判据对照)

### 2.5 总分文件

- Gemini: `ai_platforms/gemini_gems/dev/evidence/smoke_v4_v5c_regression_results.md`
- ChatGPT: `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v4_v2_1_regression_results.md`
- 含: (1) Q4-Q10 verdict 表 / (2) 对比 N5.2 baseline 差异 / (3) 总分 / (4) 判定 PASS / PARTIAL / FAIL

---

## §3 PASS 阈值

### 3.1 主阈值 (strict)

- **双平台各 Q4-Q10 = 7/7 PASS** → 等价假设成立, G5-4 闭合
- **任一平台 ≥ 1 FAIL** → 假设破, 需深查 FAIL 根因 (prompt 改动污染 / KB 漂移 / LLM 输出随机性)

### 3.2 宽松阈值 (lax, 若 strict fail 时的 fallback)

- 双平台各 **≥ 5/7 PASS** + FAIL 题可归因为 "LLM 输出随机性" (再跑 2 次, 2/3 PASS 视同 PASS) → 假设 BORDERLINE_PASS
- FAIL 题归因为 "v5c/v2.1 prompt 副作用" → FAIL, 返工 prompt

### 3.3 PARTIAL 处理

smoke v4 §2 原判据定义的 PARTIAL 保留原等级 (不降为 FAIL 也不升为 PASS). N5.2 baseline 有 PARTIAL 的题 (若有), R1/R2 baseline 已 locked, 本 regression 对比是"新 PARTIAL 数是否多于 baseline".

---

## §4 Rule D 独立 reviewer 规划

### 4.1 第 15 R2-line Rule D slot 候选

post-R2 R2-line 已用 13th (`pr-review-toolkit:code-reviewer`) + 14th (`oh-my-claudecode:verifier`). 本 regression reviewer 候选 (独立 subagent_type, 无 self-review):

- **优选**: `superpowers:code-reviewer` (Phase 5 reviewer 也候选此)
- **次选**: `oh-my-claudecode:critic` (跨 Phase 能 meta-audit)
- **再次**: `oh-my-claudecode:scientist` (统计样本 + 假设检验视角)

### 4.2 Reviewer 职责

独立核:
1. 14 answer.md 主 session self-score 准确性 (每题逐条对照 SMOKE_V4.md §2 判据)
2. 双平台 PASS/FAIL 分布是否合理 (跨平台同题差异可归因)
3. G5-4 假设是否闭合 (等价 / BORDERLINE / 破)
4. 若破, 根因归因是否正确 (prompt 污染 vs KB 漂移 vs 随机性)

### 4.3 产物

- `ai_platforms/gemini_gems/dev/evidence/v5c_regression_reviewer.md`
- `ai_platforms/chatgpt_gpt/dev/evidence/v2_1_regression_reviewer.md`
- (或合并成 1 份 `ai_platforms/v5c_v2_1_regression_reviewer.md`, 单 reviewer 跨双平台)

---

## §5 Rule A/B/C/D/E 合规

- **Rule A (语义抽检)**: 14 题 (N=14) 已超 N≥5 门槛, 不需额外抽检.
- **Rule B (失败归档)**: 若任一题 FAIL, 归档 `failures/v5c_regression_attempt_X.md` 含 prompt / 回答 / 判据对照 / 下一 attempt 输入.
- **Rule C (Retro 强制)**: 本 regression 完成后**不强制** 独立 retro (Tier 不足), 但结果回灌 `PHASE5_RETROSPECTIVE.md §2 G5-4` 闭合记录.
- **Rule D (审阅隔离)**: 主 session self-score + 独立 reviewer 15th R2-line slot. ✓
- **Rule E (跨平台 cross-check)**: 双平台同题直接对比 = Rule E 兑现. 若跨平台同题同 FAIL 模式 → 两平台共性问题 (KB source 或 smoke 判据本身); 单平台 FAIL → 该平台 prompt/KB 问题.

---

## §6 预估工作量

- 跑题: ~40-60 min (两平台串行 Chrome MCP, 14 答)
- 落档 + self-score: ~20-30 min
- reviewer 独审: ~20-40 min (background agent)
- 决策 + 回灌 retro: ~10 min
- **合计**: ~1.5-2.5 h

---

## §7 决策: 跑还是不跑?

### 7.1 跑的理由

- 闭合 G5-4 缺口, Phase 5 FINAL retro 无悬置假设
- 若假设破, 触发 v5c / v2.1 prompt 返工, 避免未来 v6/v7 迭代时问题扩散
- Rule E 实战一次补 cross-check 数据

### 7.2 不跑的理由

- 7/7 × 2 = 14/14 全过的概率经验上 ≥ 70% (N5.2 baseline 10/10 strict, Q4-Q10 7/10 恒过; v5c 改动边界 clean)
- Phase 5 已 FINAL 后再跑效果同; 不阻塞
- Gemini v7 / ChatGPT v2.2 apply 后需要**新 baseline 跑**, 现跑 v5c/v2.1 baseline 相当于为旧版背书, ROI 低

### 7.3 推荐

**跑 v7/v2.2 apply 后的新 baseline 作 combined regression**: 把 G5-4 闭合 + v7/v2.2 等价性验证合并成一次 Chrome MCP cowork, 节省一半时间. 即:
- v7 (Gemini) + v2.2 (ChatGPT) apply 后跑 Q4-Q10 × 2 = 14 题
- 同时 verify (a) v7/v2.2 新 prompt 在 Q4-Q10 不 regression / (b) G5-4 假设 (相对 v5c/v2.1) 等价

**触发条件**: v7 / v2.2 reviewer APPROVE + 用户 apply live 后.

---

## §8 本 plan 版本管理

| 版本 | 日期 | 状态 | 触发 |
|---|---|---|---|
| v0.1 | 2026-04-23 | 📋 DRAFT plan only | Phase 5 RETROSPECTIVE 骨架后起草, G5-4 登记 |
| v1.0 | 2026-04-24 | 🟡 **自评完成** | Chrome MCP cowork 全自动 14 题串行, ChatGPT 7/7 + Gemini 7/7 strict PASS; **G5-4 等价假设成立** |
| v2.0 | [TBD] | ⏳ pending reviewer | 15th R2-line reviewer (背景派 `superpowers:code-reviewer`) 独立复核 pending |
| v3.0 | [TBD] | ✅ DONE | reviewer APPROVE + 回灌 PHASE5_RETROSPECTIVE §2 G5-4 closure note |

---

*v0.1 2026-04-23 起草. 本 plan 是 Phase 5 sign-off 时可声明 "G5-4 有执行 plan 待触发" 的凭证, 不必在 sign-off 前执行. 与 `PHASE5_RETROSPECTIVE.md §2 G5-4` 交叉引用.*
