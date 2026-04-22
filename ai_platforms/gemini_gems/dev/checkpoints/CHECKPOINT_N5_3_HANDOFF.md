# Phase 4 Node 5.3 — Gemini 用户操作 Handoff (Full A/B 矩阵 + Generalization Probe)

> **Node**: Phase 4 N5.3 Step 4 Web UI 执行 (smoke v3 10 题, 双平台共用子集)
> **前置 commit**: `7edcb1c` (Phase 4 N5.3 C5.3a 题库设计 + 双 reviewer 审 + v3.1 修)
> **执行者**: 用户 + claude cowork MCP 代理 (Chrome JS `execCommand('insertText')` + `InputEvent` + wait 2s 绕 Quill ngModel race, 沿用 N4/N5.2 经验)
> **估时**: 验证 ~5 min + 10 题 ~30-45 min (Pro mode 每次 navigate 需手动重选; Q3/Q6 Quill race 历史易踩)
> **下游 gate**: 回报 smoke v3 score → 主 session 派 N5.3 答题 reviewer (第 23 种 subagent_type) + 进 Phase 4→5 Gate decision

---

## Step 0: 题库位置 + 阈值

- **题库**: `ai_platforms/smoke_v3_questions_draft.md` v3.1 (Q1-Q10 双平台共用; Q11-Q14 仅 ChatGPT, Gemini **不跑**)
- **合格阈**: **≥7/10 (70%)** → Phase 4→5 Gate 开闸候选
- **评分**: PASS=1 / PARTIAL=0.5 / FAIL=0

## Step 1: Custom Instructions / Knowledge (**不变**)

- system_prompt v5 (N5.2 lock, 7925 chars) + 4 文件 knowledge (01/02/03 原版 + 04 N5.1 扩 51K + N5.2 v5b 跨文件污染修) 全部保持 N5.2 状态
- **无需重传任何文件, 无需改 Custom Instructions**
- N5.3 只测"题库在现有 v5+v5b 配置下的 generalization 能力", 不动底座

## Step 2: 验证底座仍然生效 (sanity, 4 题)

新开对话问 (避 N5.2 session 残留):

### Q_sanity_1: "AESER 的 Core 属性是 Req 还是 Exp?"
- **期望**: Exp; 若答 Req 说明底座回归, 停 smoke

### Q_sanity_2: "LBNRIND 的 submission values 有哪些?"
- **期望**: HIGH / LOW / NORMAL / ABNORMAL (C78736); 若返 "H/N/L" 单字符说明 v5 CO-2 subclause 被改, 停 smoke

### Q_sanity_3: "ACTARMCD 在哪个域? Core 属性?"
- **期望**: DM 域 Order=26 Core=Exp; 若答 ADaM/EX 错层, 说明 §1.6 硬锚点失效

### Q_sanity_4: "Disease Milestones 实际发生记录在哪个域? TM 和 SM 什么关系?"
- **期望**: SM 域 (Subject Disease Milestones); TM 定义 + SM 记录实例 + 其他域用 `--MIDS` 引用 (MIDS 三角关系)

4 sanity 全 PASS → 进 Step 3

## Step 3: 跑 smoke v3 10 题 (Q1-Q10)

**规则**:
- 按题号顺序 Q1 → Q10, 每题**开新对话** (避 context cascade)
- 推荐方式: claude cowork MCP 代理 `execCommand('insertText')` + `InputEvent` dispatch + `wait 2s` + UI click (绕 Quill ngModel race, Node 4/N5.2 Q3/Q6 各踩过一次)
- 每题题干从 `smoke_v3_questions_draft.md` 的 `> **题**:` 段整段复制
- DOM 回读完整回答后立即保存 `dev/evidence/smoke_v3_answers/Q{N}_answer.md`

**10 题分布**:
- Q1-Q3 (GF/CP/BE+BS+RELSPEC, v3.4 新域, 中-难): 每题 ~3 min — Gemini 1M 窗口有完整 02 spec 原材料
- Q4 (LB/MB/IS 边界, 难 + 跨版本记忆风险 reviewer HIGH-2): ~5 min — 重点观察场景 A (抗麻疹 IgG) 是否触 v3.3 MB 旧规则
- Q5 (FA/QS/CE, reframe 后 04 重叠 <25%): ~4 min
- Q6-Q7 (Timing, 中-难): 每题 ~3 min
- Q8 (CT D1): ~2 min
- Q9 (Pinnacle 21, 难 — Gemini 预训练支撑但 KB 0 覆盖): ~3 min
- Q10 (QORIG/QEVAL + SUPPTS vs SUPP--, 难): ~3 min

**已知风险**:
- Q3 Gemini CO-2 拒答设计可能过度保守 (KB BE/spec.md BECAT Examples 含 "COLLECTION" 字面, 应 inline 引用, 不拒答) — 若 Gemini 答 "无 KB 原文不能给" → PARTIAL 而非 FAIL (参考 smoke v2.1 Q3 CO-2 拒答等价处理)
- Q4 场景 A (IgG baseline) 答 "MB" → PARTIAL (v3.3 旧规则记忆但理由含"免疫应答/antibody" 可接受; 答 MB 无理由 → FAIL)

## Step 4: 落档 smoke_v3_results.md

保存到: `ai_platforms/gemini_gems/dev/evidence/smoke_v3_results.md`

结构:
```markdown
# Gemini Gems — smoke v3 (N5.3 Full A/B) 10 题结果

> Date: <date>
> 题库: smoke_v3_questions_draft.md v3.1 (generalization probe)
> 前置 commit: 7edcb1c
> 执行者: user + claude cowork MCP Chrome JS Quill helper
> 合格阈: ≥7/10 (70%)
> 预期 strict score: 7-9/10 (1M 窗口 + 04 非预压缩场景下 generalization)

## 逐题结果

### Q1 (A1 GF 域 EGFR 基因变异)
- 对话 URL: https://gemini.google.com/...
- 完整回答: dev/evidence/smoke_v3_answers/Q1_answer.md
- 判据对齐: ...
- Verdict: PASS / FAIL / PARTIAL
- 归因: ...

### Q2-Q10: 类似
```

另存每题完整回答到 `dev/evidence/smoke_v3_answers/Q{N}_answer.md` (10 个文件)

## Step 5: 回报主 session

回报格式:
```
Gemini smoke v3 完成: X/10 strict PASS (Y/10 宽判包含 PARTIAL)
- Q1-Q3 (v3.4 新域 A1/A2/A3): x/3
- Q4-Q5 (域边界 B1/B2): x/2 (Q4 IS scope 跨版本记忆是否触 v3.3 MB 旧规则: YES/NO)
- Q6-Q7 (Timing C1/C2): x/2
- Q8 (CT D1): x/1
- Q9-Q10 (Pinnacle + SUPP E1/H1): x/2
- 04 引用率: x/10 (<3/10 才证 generalization 真)
- CO-2 拒答触发题数: x (>2 说明 guard 过严, Phase 5 retrospective 记)
- 是否达 ≥7/10 阈值: YES / NO
```

主 session 接手后: 派 N5.3 答题 reviewer (第 23 种 subagent_type, 候选 `pr-review-toolkit:type-design-analyzer` 或 `vercel:ai-architect`) 独立审答题 + Phase 4→5 Gate decision.

---

## 若 smoke v3 未达 7/10 阈值

- **6/10 (边缘)**: 可接受为 PASS, carry-over Phase 5 RETROSPECTIVE 记"04 pre-cook 对 Gemini 真实 generalization 的副作用"
- **≤5/10**: 分析 FAIL 集中点:
  - 若集中 Q4 (IS scope) → Gemini 预训练 v3.3 记忆盖过 v3.4 新 spec → system_prompt 需加 IS scope 硬锚点 (Phase 5 前补)
  - 若集中 Q9/Q11 (Pinnacle 21 / Dataset-JSON) → KB 本身未覆盖, 接受边界
  - 若集中 Q3 CO-2 拒答 → 把 CO-2 subclause 软化 (允许 KB Examples 字面 term inline)
- **04 引用率 >4/10**: pre-cook 侵蚀严重, Phase 5 必改弹药包策略

## 相关路径

- 题库: `ai_platforms/smoke_v3_questions_draft.md` (v3.1, 487 行)
- 题库设计: `ai_platforms/N5_3_QUESTIONS_DESIGN.md` (212 行)
- Step 3 Q 正确性 reviewer: `ai_platforms/gemini_gems/dev/evidence/phase4_n5_3_questions_reviewer.md` (第 21 种 feature-dev:code-explorer)
- ChatGPT 侧 handoff: `ai_platforms/chatgpt_gpt/dev/checkpoints/CHECKPOINT_N5_3_HANDOFF.md`
- 前轮 smoke v2.1 reviewer: `ai_platforms/gemini_gems/dev/evidence/phase4_n5_2_smoke_reviewer.md` (verifier 第 18 种)
- Phase 4 总 plan: `ai_platforms/PHASE4_PLAN.md` (§3 N5.3 行)
- SYNC_BOARD: `ai_platforms/SYNC_BOARD.md`
