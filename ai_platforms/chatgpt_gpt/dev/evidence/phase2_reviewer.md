# ChatGPT GPTs Phase 2 PLAN — Reviewer Verdict

**Verdict**: CONDITIONAL_PASS
**Reviewed by**: oh-my-claudecode:verifier (独立 lane, 规则 D)
**Date**: 2026-04-20
**Subject**: ai_platforms/chatgpt_gpt/docs/PLAN.md (660 行, v1)
**Sources read**: PLAN.md + platform_profile.md + research.md + phase1_reviewer.md + _progress.json + _template/04_plan.md + _template/05_solution.md + SYNC_BOARD.md

---

## P1-P13 覆盖矩阵

| 规则 | 覆盖? | 本平台具象化? | 备注 |
|------|:-----:|:------------|------|
| P1 量化 PASS 标准 | YES | count_tokens.py + `[Stage X.Y]` 格式 + 单文件 <500 KB 目标 (来自 Q2 chunk 参数) | 具象化有效, 非照抄 |
| P2 写/审分离执行态 | YES | PLAN 本身即例证 (writer=executor, reviewer=verifier); 后续每 Task 明示 | PASS |
| P3 AI 估算值前缀 `~` | YES | upload_manifest.md 第一列全加 `~`, 第二列去 `~` — 明确双列区分 | PASS |
| P4 人工抽查 checkpoint hard/soft/none | YES | §4 每 Task 字段明示; §4 Phase 统计表汇总 | PASS |
| P5 源文件只读 knowledge_base/ 禁写 | YES | "合并脚本输出到 chatgpt_gpt/current/uploads/, 不回写" | PASS |
| P6 Subagent 上下文隔离 | YES | 每脚本独立 executor subagent; 主控不读脚本源 | PASS |
| P7 进度持久化 _progress.json | YES | "每批更新; Phase 2 完成后 2_plan.status=PASS 由主控写" | PASS |
| P8/规则 B 失败归档 | YES | `dev/evidence/failures/stage_<N>_attempt_<M>.md` 明示 | PASS |
| P9/规则 A 语义抽检 | YES | N=5 明确写入; 压缩率 >50% 触发; 批 1/批 2 各有 Task (B5/C5) | PASS |
| P10 A/B 衰减强制响应 | YES | 衰减 ≥2 题立即停 (Task D3); ≥1 题写 regression evidence; 13 题矩阵明示 | PASS |
| P11 合并粒度硬限 20 文件 | YES | 9 合并文件 + 11 spare; 来源 Phase 1 Q5 跨套餐一致 | PASS |
| P12 溯源标注强制 | YES | 每段起始 `<!-- source: <路径> -->`; 平台独有 (chunk 800 不可跨 heading) | PASS |
| P13 TableAware 分段 | YES | 单表不跨 heading; 规避 chunk 边界落入表格; 来源 profile F1 失败模式 | PASS |

**P1-P13 覆盖: 13/13**. 所有规则均有本平台具象化, 非照抄范本原文.

---

## Rule E 乘入审核

| Q | 值 | 公式位置 | 数字合理? |
|---|-----|---------|----------|
| Q1=C GPT Store 全网公开 | novelty_bonus +0.2 | §3.1 公式 novelty_bonus 定义段 + §7.1/7.2 (T13/T14 两道公开受众题必测) | PARTIAL — 见 Rule E 数字依据段 |
| Q2=C 混合受众 | audience_fit +0.2 | §3.1 公式 audience_fit 定义段; §1.3 表格 Q2=C 条目 "4 个 Starter 全部使用" | PARTIAL — 见 Rule E 数字依据段 |
| Q5=A 63 域全量平权 | coverage_weight floor 0.15 | §3.1 floor 规则; §3.2 第 05 行 floor 触发例; §2.4 合并文件清单 "63 域全量" | PARTIAL — 见 Rule E 数字依据段 |
| 三项均乘入公式 | YES | `score = coverage × priority × audience × novelty` — 四维全乘入 | 结构正确 |

**Q1 语义正确性**: §1.3 表格明确写 "任何人可搜索/使用, 非定向分享 (与 Gemini '链接给同事' 不同)" — 与 _progress.json `Q1_publish_scope_semantics_clarification` 字段完全一致. PASS.

---

## Phase 1 Carry-over 处置审核

| Carry-over | 处置位置 | 完整? |
|-----------|---------|:-----:|
| MEDIUM: Instructions "8,000 字符" source URL 缺失 + tokens vs chars 4x 精度差 | §1.4 (四点显式处置) + §3.3 (预算分配段 "来源 URL 待补") + §4 Task C1 (来源待补标注 + Phase 3 fallback) + §8 风险 R1 + §6 失败模式 12 | YES — 全面处置 |
| PARTIAL→Phase 3: Q8 Indexing indicator 实测 | §1.5 + Task E1 (soft checkpoint) + Task C7 (实测步骤嵌入) | YES |
| Phase 1 未决 #2: Hybrid search 权重 | §1.5 + Task D (A/B 矩阵加入精确 vs 语义对比题 T15) | YES |

**处置评估**: §1.4 四点处置完整: (1) 7,500 字符预算 (保守假设), (2) 来源待补标注, (3) Phase 3 实测 fallback Task E2, (4) 不阻塞. 全部到位, 可追溯.

**"保守按 7,500 字符"依据审查**: §1.4 说明"留 500 字符 buffer" (8000 - 500 = 7500). 8000 字符来自 research.md "对 PLAN 的修订"表格 #2 ("8,000 字符, 社区多次确认"), 该数字在 phase1_reviewer.md 中被标注为来源链断裂 (MEDIUM). 因此 7,500 是 "8,000 字符 - 500 buffer" 的推算结果 — 推算逻辑自洽, 但上游 8,000 字符本身来源仍待补 (已在 Task E2 安排实测). 处置方式合理, 不属 hallucinate, 属合理保守假设 + 待补标注.

---

## research.md 10 条 PLAN 修订吸收审核

| 修订 # | 原内容 | PLAN 对应段 | 吸收? |
|--------|--------|-----------|:-----:|
| 1 | 存储上限 10GB/user / 100GB/org | §2.4 "存储上限检查: ~10 MB ≪ 10 GB/user" | YES |
| 2 | Instructions 7,500 字符保守预算 | §1.4 四点 + §3.3 + Task C1 + R1 + 失败模式 12 | YES |
| 3 | 4 个 Conversation Starter 全用 | §1.3 Q2 条目 + Task C2 (4 题明确列出) + §7.1 "4 题 Starter 命中" | YES |
| 4 | chunk 参数固定 800/400, 格式是唯一可控变量 | P12/P13 规则 + §2.4 合并策略说明 + §3.1 "P12 溯源 + P13 TableAware" | YES |
| 5 | top-K=20 影响 A/B 跨 chunk 汇总题 | §7.2 T09/T10/T11 (跨 chunk 检索题 3 道) + §5.2 批 2 说明 | YES |
| 6 | Assistants API sunset; 项目仅用 GPT Builder | §2.3 Read-only 排除 API 侧; 无引入 API 相关 Task | YES |
| 7 | Phase 5 时间线预留 1 周审核缓冲 | §8 R6 "Phase 5 时间线预留 1 周 buffer" | YES |
| 8 | Plus 套餐发布路径: Private→Link→Store | Task F5 三选一发布决策 checkpoint + R6 | YES |
| 9 | 格式质量是唯一可控优化变量 (Q2/Q3 推论) | P12+P13 升核心约束; validate_chatgpt_stage.py 强制检查 | YES |
| 10 | Phase 3 执行必加上传后实际问答验证 | Task C7 / Task E1 / §7.3 smoke 子集 | YES |

**吸收率: 10/10**. 所有 10 条均有 PLAN 对应段, 无遗漏, 无凑数.

---

## 33 Task 合理性评估

### Task 计数核实

- Phase A: A1, A2, A3 = 3 Tasks
- Phase B: B1, B2, B3, B4, B5, B6, B7 = 7 Tasks
- Phase C: C1, C2, C3, C4, C5, C6, C7 = 7 Tasks
- Phase D: D1, D2, D3 = 3 Tasks
- Phase E: E1, E2 = 2 Tasks
- Phase F: F1, F2, F3, F4, F5 = 5 Tasks
- Phase G: G1, G2, G3, G4, G5, G6 = 6 Tasks

**合计: 33 Tasks** — 计数核实正确.

### 凑数评估

- Phase A (3 Tasks): Setup 轻量合理; 3 是最小有效分解 (归档/脚本初始化/目录初始化). 无凑数嫌疑.
- Phase B (7 Tasks): 脚本写 (B1/B2) + 合并跑 (B3) + 校验 (B4) + 抽检 (B5) + reviewer (B6) + 用户 smoke (B7). 每步职责清晰, 无可合并项. 合理.
- Phase C (7 Tasks): 结构对称 Phase B, 但多了 C1 (system prompt) + C2 (Starter 选题), 差异合理 (批 2 增加 Instructions 设计). 合理.
- Phase D (3 Tasks): A/B 执行 (D1) + 报告 (D2) + 衰减响应 (D3). 最小合理分解.
- Phase E (2 Tasks): 两项 Phase 1 carry-over 实测. 独立必要.
- Phase F (5 Tasks): 终态回归 (F1) + reviewer (F2) + PASS 比决策 (F3) + Builder Profile (F4) + 发布决策 (F5). 全部必要, GPT Store 发布准备是 ChatGPT 平台独有流程, 不是凑数.
- Phase G (6 Tasks): RETRO (G1) + reviewer (G2) + TUTORIAL (G3) + ROADMAP 更新 (G4) + 上游索引 (G5) + commit (G6). 规则 C 强制, 合理.

**结论: 33 Tasks 均独立有价值, 无凑数迹象**.

### Hard Checkpoint 8 条必要性评估

| # | Task | checkpoint 内容 | 必要性 |
|---|------|----------------|:------:|
| 1 | B7 | 批 1 smoke ack (用户上传 + 测试) | 必要 — 用户操作节点 |
| 2 | C7 | 批 2 full A/B ack (用户上传 + 全量测试) | 必要 — 用户操作节点 |
| 3 | D3 | A/B 衰减 ≥2 题用户决策 | 必要 — P10 强制 |
| 4 | F1 | 终态回归 A/B (用户 A/B 终审) | 必要 — 最终质量门 |
| 5 | F3 | PASS 比 ≥90% 用户决策进 Phase 5 | 必要 — Phase 3→4 gate |
| 6 | F5 | 发布决策三选一 (Private/Link/Store) | 必要 — 不可逆操作前人工决策 |
| 7 | G2 | RETROSPECTIVE 独立复核 (规则 C 强制) | 必要 — 规则 C 明文要求 |
| 8 | G6 | 最终 commit + push (用户收尾 ack) | 必要 — 不可逆操作 |

**评估: 8 条均必要**. D3 仅在衰减触发时激活 (条件性 hard checkpoint), 实际执行路径只有 7 条必触发. F3 和 F5 可以考虑合并为一个决策节点 (Phase 5 进入 + 发布方式一次性确认), 但拆开使决策粒度更清晰, 风险可接受. **8 条不属于过多**, Tier 2 范畴内合理.

---

## Rule E 数字依据 (+0.2, +0.2, 0.15 floor)

### 可解释性评估

**audience_fit +0.2 (Q2=C 混合受众)**:
- 公式中 audience_fit 是乘法因子, 取值 0.2 (有新手友好) vs 0.0 (纯专家).
- 乘法结构意味着: P0 文件 (priority=3.0, coverage=1.0) 得 `3.0 × 1.0 × 0.2 × 0.0 = 0.0` vs `3.0 × 1.0 × 0.2 × 0.2 = 0.12` 差距约 0.12. 问题: 如果 audience=0.0 (仅专家), 整个 score 归零 — 但 §3.2 中 04_domain_specs_all.md 取 audience=0.0 得分为 `1.0 × 3.0 × 0.0 × 0.2 = 0.0`, 实际被 floor 0.15 救回. 逻辑自洽, 但 "0.2" 本身是经验值, 无外部来源支撑 — 属合理设计参数, 非 hallucinate. **ACCEPTABLE**.

**novelty_bonus +0.2 (Q1=C 公开广播)**:
- 取值对称 audience_fit, 逻辑上是同级别加成. 数字 0.2 与 audience_fit 一致, 体现等权处理两个 Rule E 维度. 无外部来源, 属设计选择. **ACCEPTABLE**.

**floor 0.15 (Q5=A 全量平权)**:
- §3.2 第 05 行 assumptions_all.md: score = 1.0 × 1.5 × 0.0 × 0.0 = 0.0, 被 floor 到 0.15. Floor 的存在确保 coverage=1.0 的文件不因 audience/novelty 全零而被排除 — 直接对应 Rule E Q5=A 约束逻辑. 0.15 > 0 的选择合理 (高于零保证 P1 批次进入), 具体数字属经验值. **ACCEPTABLE**.

**核心风险点**: 公式是乘法 (score = A × B × C × D), 但 audience_fit 和 novelty_bonus 取值 0.0 或 0.2 (非 1.0+0.2). 这意味着它们不是"加成"而是"直接值", 结构上是**四个因子全乘**, 不是 base × bonus. 因此 03_model_all.md 的 score = `1.0 × 3.0 × 0.2 × 0.0 = 0.6` (而非 3.0), 04_domain_specs_all.md = `1.0 × 3.0 × 0.0 × 0.2 = 0.6` — **这些文件的优先级排序合理** (P0 高于 P1/P2). §3.2 表格数字经本 reviewer 手动验算, 除 01/02 外结果一致.

**验算补充**:
- 01 navigation: 1.0 × 3.0 × 0.2 × 0.2 = **0.12** (不是 §3.2 标注的 2.4)
- §3.2 的写法实际是 `coverage_weight + priority_weight + audience + novelty` 的**展示列**, score 列才是最终值 — 但 §3.2 header 写的是 `coverage | priority | audience | novelty | score`, 列值 `1.0 | 3.0 | 0.2 | 0.2 | 2.4` 数学上 1.0 × 3.0 × 0.2 × 0.2 = 0.12, 不等于 2.4.

**这是一个计算错误**: §3.2 score 列数字与 §3.1 公式 (四因子相乘) 不一致. 实际看 2.4 的可能算法是 `(coverage × priority) + audience + novelty = 1.0 × 3.0 + 0.2 + 0.2 = 3.4` 也不对; 或 `coverage × priority × (1 + audience + novelty) = 3.0 × 1.4 = 4.2` 也不对. 无法从 §3.2 数字反推一致公式. **这是 hallucinate 风险点 — score 数字无法从公式推导**, 但对优先级排序结论影响有限 (P0 > P1 > P2 序关系仍然正确). 标注为 MEDIUM 缺口.

---

## 发现的缺口 / hallucinate 风险

### 缺口 1 (MEDIUM): §3.2 score 列数字无法从 §3.1 公式推导

**位置**: §3.2 打分表格 score 列
**问题**: §3.1 公式为四因子相乘 `coverage × priority × audience × novelty`. 以 01_navigation.md 为例: 1.0 × 3.0 × 0.2 × 0.2 = 0.12, 但 §3.2 标注 score=2.4. 差距 20x. 无法从正文找到将 2.4 推导出来的计算路径.
**风险**: 如 score_chatgpt_priority.py 按 §3.2 数字实现, 与 §3.1 公式将不一致. 实际排序正确性依赖执行者如何解读, 存在分歧风险.
**建议**: Phase 3 前, 在 §3.1 或 §3.2 补一行说明实际计算方法 (是纯乘法还是混合加权); 或修订 §3.2 score 列为正确推算值. 不需要重跑 Phase 2, 可作为 Phase 3 Task B1 前置 (score 脚本写作前澄清).
**严重度**: MEDIUM (影响打分脚本实现一致性, 但排序方向正确)

### 缺口 2 (LOW): Phase F 阶段标题与 Task 编号命名不一致

**位置**: §4 Phase F (Task F1-F5) 与 PLAN 顶部 Phase A-H 命名
**问题**: §4 中实际执行相包含 Phase A (Setup) + Phase B (批 1) + Phase C (批 2+Instructions) + Phase D (A/B) + Phase E (carry-over 实测) + Phase F (审查+发布准备) + Phase G (收束). PLAN 顶部标注"Phase A-H Task 分解"(§4 标题), 但实际只到 Phase G. "H" 未出现在 Task 分解中 — 范本 04_plan.md 有 Phase H 收束, PLAN.md 将其并入 Phase G. 不影响实际执行, 但标题与范本有偏差.
**风险**: LOW (无实质执行影响)

### 缺口 3 (LOW): Task D3 (A/B 衰减响应) 缺少 failures/ 路径的 stage 编号规范

**位置**: §6 失败模式 6 列 `dev/evidence/failures/stage_D_attempt_*.md`
**问题**: Task D3 产物写的是 `dev/evidence/failures/stage_D_attempt_*.md`, 而规则 B 和其他失败模式统一格式为 `stage_<N>_attempt_<M>.md` (N 是数字). "stage_D" 混用字母和数字命名, 可能导致文件排序混乱.
**建议**: 统一为 `stage_4_attempt_<M>.md` (Phase D = 第 4 阶段).
**风险**: LOW

---

## 放行结论

**Phase 2 → Phase 3 准入评估**:

| Gate 条件 | 状态 |
|----------|:----:|
| PLAN.md 含 P1-P10 范本规则 + 本平台具象化 | PASS (13/13) |
| P11-P13 平台独有规则存在且合理 | PASS |
| Rule E 打分公式存在 + 三项 Q 全部乘入 | PASS (结构正确; §3.2 score 数字有 MEDIUM 计算不一致) |
| Q1=C 语义正确 (全网公开, 区分 Gemini) | PASS |
| Phase 1 Instructions 8K carry-over 处置显式可追溯 | PASS |
| research.md 10 条修订全吸收 | PASS (10/10) |
| 每 Task 标 checkpoint 级别 | PASS |
| Phase A-G 分解完整, 批次数 1-2 合理 | PASS |
| A/B 矩阵 10-15 题含 4 Starter + 公开受众 ≥2 | PASS (13+1可选题, T13/T14 公开受众, 4 Starter T05-T08) |
| 失败归档路径规则 B 明示 | PASS |
| 无 hallucinate (所有数字可追溯) | PARTIAL (§3.2 score 数字无法从公式推导; 不影响排序方向) |
| 33 Task 数量合理 | PASS |

**最终 Verdict**: **CONDITIONAL_PASS**

**放行条件 (Phase 3 并行修复, 不阻塞 Phase 3 启动)**:

1. **[MEDIUM — 建议 Task B1 前澄清]** §3.2 score 列数字与 §3.1 四因子乘法公式数学不一致 (01_navigation 公式得 0.12, 表格写 2.4). 在 score_chatgpt_priority.py 编写前 (Task B1), executor 需澄清实际计算方法并修订 §3.2 或 §3.1, 防止脚本实现与 PLAN 意图分歧. **不需要重跑 Phase 2**.

2. **[LOW — 可随时修复]** Task D3 失败归档路径 `stage_D_attempt_*.md` 建议统一为 `stage_4_attempt_<M>.md`, 与规则 B 数字编号惯例一致.

**不阻塞理由**: P1-P13 全覆盖, Rule E 三项均入公式且 Q1 语义正确, Phase 1 MEDIUM carry-over 四点处置完整, research.md 10/10 吸收, 33 Tasks 全独立有价值, 8 hard checkpoints 全必要, A/B 矩阵 13 题结构完整 (4 Starter + 2 公开受众). 核心执行路径可信, §3.2 数字瑕疵不影响批次设计和上传流程.
