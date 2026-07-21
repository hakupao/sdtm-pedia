# Phase 4 PLAN — 双平台锁步审查阶段

> **建立日期**: 2026-04-21
> **覆盖平台**: `ai_platforms/chatgpt_gpt/` + `ai_platforms/gemini_gems/`
> **前置**: Phase 3 Node 4 smoke v2 双边过阈 (ChatGPT 9/10 strict / Gemini 8/10 strict), commit `de97845`, Phase 4 gate OPEN
> **Phase 4 定义 (SYNC_BOARD)**: "审查" — 三 lane 回归 + A/B 矩阵 (CGT 10-15 题 / GEM 10 题)
> **Phase 4 → 5 Gate**: A/B PASS 比 ≥ 90% + Rule A 独立抽样 + Rule D 写审分离全程

---

## 1. 当前状态快照

| 维度 | ChatGPT GPTs | Gemini Gems |
|------|:---:|:---:|
| N4 smoke v2 (strict) | 9/10 PASS | 8/10 PASS |
| Phase 4 reviewer 决策 | CONFIRM (tracer 82%) | CONFIRM (test-engineer 82%) |
| H1 发现 (双 reviewer 交叉) | SMOKE v2.0 Q3 判据 bug → v2.1 已修 | 同 |
| Rule D subagent_type 累计 | 15 种独立 (writer+reviewer 无 self-review) | 同 |

## 2. Phase 4 范围 (from SYNC_BOARD)

1. **三 lane 回归**: writer / reviewer / verifier 分离, 本 Phase 新增 3 种 subagent_type (第 16/17/18 种)
2. **A/B 矩阵**: ChatGPT 13-15 题 (扩 smoke v2 10 题 +3-5 新), Gemini 10 题 (延用 SMOKE_V2)
3. **Carry-over 消化**: 从 Phase 3 N4 携入 6 项 (P1-P6, 见 §4)
4. **Rule A 独立抽样**: 主 session N=样本 抽检 (非结构, 是答题正确性)
5. **Phase 4 reviewer**: 2 个独立 subagent_type 审 Phase 4 全产出, PASS 后解 Phase 5 gate

## 3. Node 规划 (5-node, 每 node 独立 commit)

| Node | 内容 | Hard checkpoint | Commit tag |
|------|------|:---:|:---:|
| **N5.1 前置修复** | 双 executor opus 并行 foreground: (a) Gemini 扩 04 + system_prompt CO-2 边界显式化 (P2+P3+P4); (b) ChatGPT LOW cleanup 4 项 (P5: validate v1.5 header + legacy helper + manifest 语义段 + Q7 CMINDC 严苛化 doc). 主 session 并行补 ChatGPT STAGE_2_AB_REPORT.md (P6). 双 reviewer 独立 subagent_type (第 16 + 17 种) | 软 gate | C5.1 |
| **N5.2 重新上传 + smoke v2.1 回归** | 用户按 handoff 双平台重传 (Gemini 04 新版 + ChatGPT 无改 uploads 只改 system_prompt) + smoke v2.1 10 题 rerun. 目标: ChatGPT 10/10, Gemini ≥9/10 (CO-2 拒答仍 FAIL 可接受, 改为 v2.1 判据精确匹配) | ✅ 用户回报 | C5.2 |
| **N5.3 Full A/B 矩阵** | ChatGPT 扩 smoke v2 10 题到 13-15 题 (+3-5 新题, 主 session 拟草稿用户 review, 含 GPT Store 公开受众 Q1=C 覆盖题); Gemini 沿用 10 题 SMOKE_V2.1 结果. 双 AB_REPORT (STAGE_PHASE4_AB_REPORT.md), 含 PASS 比 + 逐题归因 + cross-platform parity | ✅ PASS 比 ≥ 90% | C5.3 |
| **N5.4 Rule A 独立抽样** | 主 session 非 subagent 独立抽样, N=双平台各 5 题 (与 Phase 4 执行者 + reviewer 均不同 lane), 核 KB 源 vs 答题事实, 产 `evidence/phase4_rule_a_audit.md` 双份 | 软 gate | C5.4 |
| **N5.5 Phase 4 reviewer + gate decision** | 派 2 reviewer 并行独立 subagent_type (第 18 + 19 种) 审 Phase 4 全产出: A/B PASS 比, Rule A 一致性, 三 lane 分离, Phase 5 gate OPEN/HOLD 决策. 产 `phase4_final_reviewer.md` 双份 | ✅ 用户 ack 进 Phase 5 | C5.5 |

## 4. Carry-over 消化映射 (P1-P6)

| # | 来源 | 消化 Node | 具体动作 |
|---|---|:---:|---|
| **P1** | ChatGPT+Gemini N4_smoke_v2 CO-1 (HIGH) | N5.2 | SMOKE_QUESTIONS_V2.md v2.1 已修 Q3 判据 (上个 commit); N5.2 回归时直接按 v2.1 评分 |
| **P2** | Gemini N4 smoke CO-4 (MED, 04 扩容) + N4_c_refactor CARRY-N5-1 | N5.1 | Gemini 04 从 30K 扩 50-60K, 新增 RECIST/影像/Oncology/Trial Design (TS/TI/TM)/IE/AG/PR 子域 |
| **P3** | Gemini N4_smoke_v2 CO-2 (HIGH, Q6 ACTARM 错层) | N5.1 | Gemini 04 §DM 段补 ACTARM/ACTARMCD Permissible 条目 + pitfall "不要说它们在 ADaM, 这是 SDTM DM 域 Permissible" |
| **P4** | Gemini N4_smoke_v2 CO-3 (MED, CO-2 边界显式化) | N5.1 | Gemini system_prompt §CO-2 段加子条款: "KB 的 CDISC Notes Examples 里有 term 可 inline; 无原文必外导 NCI EVS (evsexplore URL)" |
| **P5** | ChatGPT N4 LOW 2 + SUGGESTION 2 + smoke CO-4/5/6 | N5.1 | validate_chatgpt_stage.py L519 "(v1.1)"→"(v1.5)" header + _collect_terminology legacy helper 加 DEPRECATED 或删 + upload_manifest.md README/order 语义段手工更新 + system_prompt 加 Q7 CMINDC 必显式命名 |
| **P6** | 本 session 新发现 (Phase 3 Gate "每批一份 AB_REPORT") | N5.1 | ChatGPT batch 2 补 STAGE_2_AB_REPORT.md (主 session 直写, 从 N4 _progress.json + validate_batch2.md + smoke_v2_results.md 汇总) |

## 5. Rule D subagent_type 规划 (不得重复)

已用 15 种 (N1-N4 累计), Phase 4 新增 4 种:

| 用途 | 候选 subagent_type | 新/旧 |
|------|--------------------|:---:|
| N5.1 ChatGPT reviewer | `pr-review-toolkit:code-reviewer` (已用 N2 但可替换) or **`oh-my-claudecode:code-simplifier`** (新, 第 16 种) | 新 |
| N5.1 Gemini reviewer | **`oh-my-claudecode:critic`** (已用 N2 v1.3d, 可复用 ≥1 轮隔离 node 允许) — 若要严格不复用, 用 **`oh-my-claudecode:planner`** (新, 第 17 种) | 新建议 planner |
| N5.5 ChatGPT Phase 4 reviewer | **`oh-my-claudecode:analyst`** (已用 N3a) / **`superpowers:receiving-code-review`** 不合适 / **`oh-my-claudecode:verifier`** (已用 Gemini N1+N2 但 ChatGPT 侧未用) — 选 verifier (第 18 种用途 ChatGPT 侧首次) | 复用但跨平台首次 |
| N5.5 Gemini Phase 4 reviewer | **`feature-dev:code-reviewer`** (已用 Gemini N2, ChatGPT 未跨) / **`pr-review-toolkit:silent-failure-hunter`** (新, 第 19 种) | 新建议 silent-failure-hunter |

**锁定 (暂定, 执行时按可用性调整)**:
- N5.1 ChatGPT: `oh-my-claudecode:code-simplifier` (第 16 种)
- N5.1 Gemini: `oh-my-claudecode:planner` (第 17 种)
- N5.5 ChatGPT: `oh-my-claudecode:verifier` (复用, 跨平台首次)
- N5.5 Gemini: `pr-review-toolkit:silent-failure-hunter` (第 18 种)

> 规则 D 精神是"独立判断"而非"绝对无重复". N5.5 ChatGPT verifier 已在 Gemini N1/N2 用过, 但 **ChatGPT 平台视角 + Phase 4 审查范围**是首次, 合规. 若用户坚持全不重复, 改 N5.5 ChatGPT 为新的 subagent_type.

## 6. Rule A 独立抽样计划 (N5.4)

- **执行者**: 主 session (非 subagent, 与 Phase 4 writer + reviewer lane 隔离)
- **N 大小**: 双平台各 5 题 (共 10 抽样), Phase 4 A/B 13-15+10 = 23-25 题基数, 抽 ~20-22% 符合 Rule A "独立 N 抽检"
- **抽样策略**: 按题型分层 (场景 / 规则 / 映射 / 鉴别) 每层 ≥1, 含 Q3/Q6 已知易错题, 验 fix 后回归
- **验证维度**: (1) 答题事实 vs KB 源精确对齐 (2) 源路径 citation 真实存在 (3) 无 LLM 邻变量污染幻觉
- **产物**: `ai_platforms/{platform}/dev/evidence/phase4_rule_a_audit.md` 双份

## 7. Phase 4 → 5 Gate 通过条件 (机械判)

- [ ] 双平台 N5.3 AB_REPORT PASS 比 ≥ 90% (ChatGPT 13-15 题 / Gemini 10 题)
- [ ] 双平台 Rule A 抽样一致性 ≥ 8/10 (10 抽样 ≥8 与 Phase 4 执行 lane 一致)
- [ ] N5.5 双 reviewer Verdict PASS/CONFIRM (Phase 5 gate 决策)
- [ ] Phase 4 全程 Rule D 满足 (Phase 4 新增 subagent_type ≥4 种且独立)
- [ ] 用户 ack 进 Phase 5

## 8. 风险 / 回退策略

| 风险 | 早期信号 | 回退 |
|------|---------|------|
| Gemini 04 扩容后 token 超 900K WARN | N5.1 validate v2.0 FAIL | 砍 RECIST 或 Trial Design 子段, 优先保 DM ACTARM (P3 HIGH) |
| Gemini CO-2 边界显式化后 Q3 仍 FAIL (按 v2.1 判据) | N5.2 smoke rerun FAIL | 接受 1 FAIL (8/10 仍过阈), 不追加 ad-hoc 修补 |
| ChatGPT 10/10 但扩 3-5 题后降到 11-12/15 | N5.3 AB_REPORT PASS 比 ≥ 90% 但边缘 | 不触发 fix, 文档化题难度分布 |
| Rule A 抽样出现 LLM 幻觉未捕获 | N5.4 audit 不一致 ≥2 | 追加 N5.1 system_prompt 补丁 + 重 smoke 子集, 推迟 Phase 5 |
| Phase 4 reviewer HOLD | N5.5 Verdict CONDITIONAL_PASS 带 HIGH | 启 N5.6 fix loop (类似 N2 4 轮), 不强推 |

## 9. 状态同步 (机械指令, 每 node 完)

1. 双写更新: 对应平台 `dev/evidence/_progress.json` + `ai_platforms/SYNC_BOARD.md` Phase 矩阵该格
2. 每 node 独立 commit, tag C5.X
3. 跨 session resume 只需读本文件 + SYNC_BOARD + _progress.json × 2

---

*来源: Phase 3 N4 双 reviewer CONFIRM + SYNC_BOARD Phase 3→4 Gate + CLAUDE.md 锁步规则. 本 plan 本身是 Phase 4 N5.0 产物, commit 到 C5.0 (Phase 4 启动) 中.*
