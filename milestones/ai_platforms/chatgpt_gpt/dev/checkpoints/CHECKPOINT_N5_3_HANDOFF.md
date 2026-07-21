# Phase 4 Node 5.3 — ChatGPT 用户操作 Handoff (Full A/B 矩阵 + Generalization Probe)

> **Node**: Phase 4 N5.3 Step 4 Web UI 执行 (smoke v3 14 题)
> **前置 commit**: `7edcb1c` (Phase 4 N5.3 C5.3a 题库设计 + 双 reviewer 审 + v3.1 修)
> **执行者**: 用户 + claude cowork MCP 代理 (Chrome JS `ClipboardEvent('paste')`, 沿用 N4/N5.2 经验)
> **估时**: 验证 ~3 min + 14 题 ~35-50 min (每题独立对话, 避 context 污染)
> **下游 gate**: 回报 smoke v3 score → 主 session 派 N5.3 答题 reviewer (第 22 种 subagent_type) + 进 Phase 4→5 Gate decision

---

## Step 0: 题库位置 + 阈值

- **题库**: `ai_platforms/smoke_v3_questions_draft.md` v3.1 (14 题 Q1-Q14; Q1-Q10 双平台共用, Q11-Q14 ChatGPT 专属)
- **合格阈**: **≥10/14 (71%)** → Phase 4→5 Gate 开闸候选
- **评分**: PASS=1 / PARTIAL=0.5 / FAIL=0 (按每题 PASS+FAIL 判据)

## Step 1: Custom Instructions / Knowledge (**不变**)

- system_prompt v2 (N5.1 lock, 7568 bytes) + 9 文件 knowledge (N4 batch 2) 全部保持 N5.2 状态
- **无需重传任何文件, 无需改 Instructions**
- N5.3 只测"题库在现有配置下的 generalization 能力", 不动底座

## Step 2: 验证底座仍然生效 (sanity, 3 题)

新开对话问 (避 N5.2 session 残留 context):

### Q_sanity_1: "AESER 的 Core 属性是 Req 还是 Exp?"
- **期望**: Exp (若答 Req 说明底座回归, 停 smoke)

### Q_sanity_2: "LBNRIND 的 submission values 有哪些?"
- **期望**: HIGH / LOW / NORMAL / ABNORMAL (C78736); 若返 "H/L/N" 单字符说明 system_prompt 被改或 knowledge 被替换, 停 smoke

### Q_sanity_3: "CMINDC 用于哪种场景?"
- **期望**: 显式命名 CMINDC (concomitant medication indication); 对应 N5.1 bullet

3 sanity 全 PASS → 进 Step 3

## Step 3: 跑 smoke v3 14 题 (Q1-Q14)

**规则**:
- 按题号顺序 Q1 → Q14, 每题**开新对话** (避 context cascade)
- 推荐方式: claude cowork MCP 代理 Chrome JS `ClipboardEvent('paste')` 绕 type 丢字 (Node 3b/4/N5.2 已验证)
- 每题题干从 `smoke_v3_questions_draft.md` 的 `> **题**:` 段整段复制 (不改写, 不加 hint)
- DOM 回读完整回答后**立即保存** `dev/evidence/smoke_v3_answers/Q{N}_answer.md`, 避免跨对话丢

**14 题分布** (粗略时间分配建议):
- Q1-Q3 (GF/CP/BE+BS+RELSPEC, v3.4 新域, 中-难): 每题 ~3 min
- Q4-Q5 (LB/MB/IS + FA/QS/CE 边界, 难): 每题 ~4 min
- Q6-Q7 (Timing 四件套 + Partial date, 中-难): 每题 ~3 min
- Q8 (Extensible CT, 中): ~2 min
- Q9 (Pinnacle 21, 难): ~3 min
- Q10 (QORIG/QEVAL + SUPPTS vs SUPP--, 难): ~3 min
- Q11-Q14 (ChatGPT 专属 F1/G1/D2/I1): 每题 ~3 min

## Step 4: 落档 smoke_v3_results.md

保存到: `ai_platforms/chatgpt_gpt/dev/evidence/smoke_v3_results.md`

结构模板:
```markdown
# ChatGPT GPTs — smoke v3 (N5.3 Full A/B) 14 题结果

> Date: <date>
> 题库: smoke_v3_questions_draft.md v3.1 (generalization probe)
> 前置 commit: 7edcb1c
> 执行者: user + claude cowork MCP Chrome JS paste
> 合格阈: ≥10/14 (71%)
> 预期 strict score: 10-13/14 (ChatGPT RAG + batch 2 terminology 优势)

## 逐题结果

### Q1 (A1 GF 域 EGFR 基因变异)
- 对话 URL: https://chatgpt.com/...
- 完整回答: dev/evidence/smoke_v3_answers/Q1_answer.md
- 判据对齐: 域 GF ✓ / 5 Req ✓ / 3 Exp ✓ / GFGENSR ... / GFPVRID ... / GFGENREF ... / GFINHERT ...
- Verdict: PASS / FAIL / PARTIAL
- 归因: ...

### Q2-Q14: 类似格式
```

另存每题完整回答到 `dev/evidence/smoke_v3_answers/Q{N}_answer.md` (14 个文件)

## Step 5: 回报主 session

回报格式:
```
ChatGPT smoke v3 完成: X/14 strict PASS (Y/14 宽判包含 PARTIAL)
- Q1-Q3 (v3.4 新域 A1/A2/A3): x/3
- Q4-Q5 (域边界 B1/B2): x/2
- Q6-Q7 (Timing C1/C2): x/2
- Q8 (CT D1): x/1
- Q9-Q10 (Pinnacle + SUPP E1/H1): x/2
- Q11-Q14 (ChatGPT 专属 F1/G1/D2/I1): x/4
- 04 引用率: x/14 (<4/14 才证 generalization 真)
- 是否达 ≥10/14 阈值: YES / NO
```

主 session 接手后: 派 N5.3 答题 reviewer (第 22 种 subagent_type, 候选 `oh-my-claudecode:critic` 或 `pr-review-toolkit:type-design-analyzer`) 独立审答题 + 计算 PASS 比 + Phase 4→5 Gate decision.

---

## 若 smoke v3 未达 10/14 阈值

- **9/14 (边缘)**: 可接受为 PASS, 记 carry-over 到 Phase 5 RETROSPECTIVE
- **≤8/14**: 分析 FAIL 题是否集中某一类 (e.g., Q11-Q14 新技术都 FAIL → RAG 未覆盖 2025 新议题, 接受 generalization 有边界)
- **04 引用率 >5/14**: 说明 04 被过度依赖, Phase 5 retrospective 必记"pre-cook 对 ChatGPT RAG 的侵蚀"

## 相关路径

- 题库: `ai_platforms/smoke_v3_questions_draft.md` (v3.1, 487 行)
- 题库设计: `ai_platforms/N5_3_QUESTIONS_DESIGN.md` (212 行)
- Step 3 Q 正确性 reviewer: `ai_platforms/chatgpt_gpt/dev/evidence/phase4_n5_3_questions_reviewer.md` (第 20 种 scientist)
- Gemini 侧 handoff: `ai_platforms/gemini_gems/dev/checkpoints/CHECKPOINT_N5_3_HANDOFF.md`
- 前轮 smoke v2.1 reviewer: `ai_platforms/chatgpt_gpt/dev/evidence/phase4_n5_2_smoke_reviewer.md` (planner 第 19 种)
- Phase 4 总 plan: `ai_platforms/PHASE4_PLAN.md` (§3 N5.3 行)
- SYNC_BOARD: `ai_platforms/SYNC_BOARD.md`
