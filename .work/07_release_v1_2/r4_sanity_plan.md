# R4 Sanity Test Plan — Gemini v8.1 LIVE Regression Check

> **目的**: v8.1 prompt 已 promote LIVE (2026-05-19 16:55), 但 dry-run 只测了 4 个 R3 FAIL 题 (Q3/Q4/Q11/AHP1) 全 PASS+. **R3 PASS 的 13 题在 v8.1 下是否回归** 未验证 — Rule D #17 列为遗留 finding.
>
> **本计划**: 选 5 题 sanity (代表性强 + Pro quota 内可完成), 验证 v8.1 不引入 regression. 如 5 题全 PASS → v8.1 sanity 通过, 风险可控; 如 ≥1 FAIL → 触发 R4 全 17 题或 v8.1 rollback 决策.
>
> **执行前置**: Gemini 3.1 Pro quota 已恢复 (4 题/window, 5h rolling reset).
> **预计时长**: 5 题串行 ≈ 1-2 quota cycle = 5-10h (含等待).
> **执行位置**: Gemini Gem (instructions = v8.1 LIVE, current ≡ deployed).
> **创建日期**: 2026-05-19 evening (post v1.2 cut + tag verified)

---

## 5 题选择 + 理由

| # | 题简述 | SMOKE_V4 anchor | R3 v7.1 verdict | 选择理由 |
|:-:|---|---|:---:|---|
| Q1 | GF 域变量拼写 (GFINHERT) + Core | `ai_platforms/SMOKE_V4.md:440` | PASS | 基础: 单域 + 域变量 + Core, 验证基本 KB 召回不退化 |
| Q2 | CP 细胞表型 (CPCSMRKS 等) | `ai_platforms/SMOKE_V4.md:469` | PASS | 中复杂: 多变量, 验证 v8.1 没把"多候选"过度限制 (Reviewer M2 候选数限) |
| Q5 | FA vs QS vs CE 三场景判别 | `ai_platforms/SMOKE_V4.md:562` | PASS | 经典 use-case: 域边界判别, 验证 4-prong CO-2f 文件格式 gate 没把正常题误锁 |
| Q6 | PK 时间窗 PCTPT/PCTPTREF 四件套 | `ai_platforms/SMOKE_V4.md:591` | PASS | Define 级 timing 深化, 验证 v8.1 的 default reflection 不干扰 timing 类题 |
| Q14 | AE+CE+MH timing + DS 死亡跨域 | `ai_platforms/SMOKE_V4.md:841` | PASS | 跨域综合, 验证 v8.1 在多步推理时不被 CO-5 default reflection 卡死 |

**为什么这 5 题**:
- 全是 R3 v7.1 **PASS** 题 (非 FAIL) — sanity 目标是 "不退化", 不是 "修复" (修复已 dry-run 验过)
- 覆盖 spectrum: 单变量 (Q1) → 多变量 (Q2) → 域边界 (Q5) → timing 深化 (Q6) → 跨域综合 (Q14)
- 避开 AHP 探针题 (Q10/Q13/AHP1/AHP2/AHP3) — 那 5 题已在 v8.1 dry-run 4/5 验过 (含 AHP1 修复)
- 避开 R3 FAIL 4 题 (Q3/Q4/Q11/AHP1) — 那些已在 v8.1 dry-run **4/4 PASS+** 验过, 重复测无新信息
- 避开 bonus 容错题 (Q9 Pinnacle 21 / Q11 Dataset-JSON / Q12 CT 版本锁定) — 容错允许 PARTIAL

---

## 执行步骤 (机械流程)

每题:

1. **打开 Gemini Gem** (URL: Gemini Gem instance, instructions = v8.1 LIVE)
2. **复制 SMOKE_V4.md 对应 anchor 题目原文** (含场景 / 问题 / 期望答案要点) 到 Gem
3. **粘贴, 不加任何 reflection 提示** (v8.1 default reflection 应自动触发)
4. **等回答完成, paste 答案给主 session** (chat 里直接 paste)
5. **主 session 评判** (按 Strict 判据, 见下) → PASS / PASS+ / PARTIAL / FAIL
6. **写 evidence** `evidence/q{NN}_sanity.md` (主 session 写, 含题目 / 答案 / verdict / 关键命中点)

**串行**, 不并行 — Pro quota 不允许. 4 题/window 用完后等 5h.

**Quota 规划**:
- Window 1 (4 题): Q1 → Q2 → Q5 → Q6
- 等 5h reset
- Window 2 (1 题): Q14
- 总耗时 ≈ 5-10h (含等待)

---

## Strict 判据 (per R3 SMOKE_V4 规则)

| Verdict | 标准 |
|---|---|
| **PASS+** | 答出全部期望要点 + 主动列出额外深度 (e.g. Define-XML CT URL / Assumption 行号引用 / cross-ref 跨域链路) |
| **PASS** | 答出全部期望要点, 无主动深度但无遗漏 |
| **PARTIAL** | 答出 ≥50% 要点, 有 1-2 处可补救的遗漏 (不算 regression 但需 follow-up) |
| **FAIL** | 跑题 / 关键变量名错 / 域错 / 幻觉变量 / 答非所问 / 拒答 — **触发 halt** |

**关键 finding watch** (v8.1 reviewer audit Rule D #17 已列 4 项 LOW/MED, sanity 期间观察):
1. M2 候选数限 隐式 — Q2 多变量题特别注意 v8.1 是否输出 <5 候选 (per reviewer 担忧)
2. PASS+ §1.2 strict 应 "AHP 专属" — sanity 5 题非 AHP, 期望 PASS 不期望 PASS+
3. CO-5 default reflection — Q6/Q14 timing/跨域复杂题, 看 v8.1 reflection 是否过度自我修正反而出错
4. CO-2f 文件格式 gate — Q5 边界判别, 看 v8.1 是否把正常域判别误判成文件格式题锁死

---

## 决策树 (跑完后)

```
5/5 PASS (含可接受 PARTIAL)
  → v8.1 sanity APPROVE
  → 不需要跑 R4 全 17 题 (除非用户额外要求)
  → 进入 v1.3 / Phase 7 选向

≥1 FAIL (任何一题 regression)
  → halt + 写 R4 fail report
  → 决策点: (a) v8.1 rollback v7.1 + v1.2 重新 cut [大动作]
            (b) v8.1 patch v8.2 prompt + dry-run + re-promote [中动作]
            (c) 接受 known limitation 文档化 + v1.2 不动 [小动作]
  → Bojiang 决策

PARTIAL > 2 题
  → 触发 R4 全 17 题 (扩大样本验证)
```

---

## Evidence 路径

每题:
- `.work/07_release_v1_2/r4_sanity/evidence/q{01,02,05,06,14}_sanity.md`

Combined report:
- `.work/07_release_v1_2/r4_sanity/R4_SANITY_RETROSPECTIVE.md` (跑完后写)

更新 _progress.json:
- `ai_platforms/gemini_gems/dev/evidence/_progress.json` — 加 `r4_sanity_2026-05-20` 节点
- `docs/PROGRESS.md` — 加 milestone 一行
- `ai_platforms/SYNC_BOARD.md` — "上一次状态更新" 段

---

## Pre-Flight Checklist (跑前确认)

- [ ] Gemini Pro quota 已恢复 (4 题/window 可用)
- [ ] Gemini Gem instructions field = v8.1 LIVE (verify: `ai_platforms/gemini_gems/current/system_prompt.md` 525 行 v8.1 header)
- [ ] SMOKE_V4.md 5 题 anchor 可访问 (line 440/469/562/591/841)
- [ ] `.work/07_release_v1_2/r4_sanity/evidence/` 目录已建 (跑前主 session 建)
- [ ] 主 session 知道 Strict 判据 + 决策树 (本文档)

---

## 启动指令 (明天发给主 session)

> "开始 R4 sanity. 读 `.work/07_release_v1_2/r4_sanity_plan.md`, 我开 Gemini Gem 跑 Q1, 跑完 paste 答案."

主 session 收到后:
1. Read 本 plan
2. Read SMOKE_V4.md:440-468 拿 Q1 题目
3. Paste 题目给用户 (或直接告诉用户 anchor, 让用户自己复制到 Gem)
4. 等用户 paste Gemini 答案
5. 评判 + 写 evidence
6. 进 Q2 (Window 1 内连跑 Q2/Q5/Q6, 然后 halt 等 quota reset 跑 Q14)
