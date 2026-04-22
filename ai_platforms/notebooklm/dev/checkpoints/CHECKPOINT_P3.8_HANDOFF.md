# Phase 3 P3.8 — NotebookLM 用户操作 Handoff (10 SMOKE v3 Q1-Q10 A/B)

> **Phase**: Phase 3 P3.8 Web UI 执行 (smoke v3 Q1-Q10, v2.2 2026-04-22 升级对齐 ChatGPT+Gemini N5.3)
> **前置 PASS**: P3.4 indexing smoke 10/10 + P3.4.5 Q1 红线语义级自证 CONDITIONAL_PASS 8.5/10 (Rule A 正本闭合)
> **PLAN 锚**: `ai_platforms/notebooklm/docs/PLAN.md` v2.2 §6 P3.8 + §7 A/B 矩阵
> **执行者**: 用户 + (可选) claude cowork MCP 代理 `ClipboardEvent('paste')`
> **估时**: sanity 3 题 ~5 min + Q1-Q10 ~30-40 min (每题独立对话, 避 context 污染)
> **下游 gate**: 回报 smoke v3 score → 主 session 派 P3.8 答题 reviewer (第 11 种 subagent_type, 与 Rule D 9-chain + P3.4.5 第 10 种 scientist 错开) + Phase 3 收束决策 → Phase 4 跨 4 平台对比矩阵

---

## Step 0: 题库位置 + 阈值

- **题库**: `ai_platforms/smoke_v3_questions_draft.md` v3.1 (14 题共 14, 本平台**只跑 Q1-Q10**; Q11-Q14 ChatGPT 专属不适用)
- **合格阈**: **≥9/10 (90%)** → P3.8 PASS, Phase 3 收束 gate 开闸
- **阈值不对齐 ChatGPT/Gemini 解释**: ChatGPT 71% / Gemini 70% 因首过 generalization probe 预留 buffer; NotebookLM 保 90% 因 P3.4.5 已 CONDITIONAL_PASS 8.5/10 验底座稳
- **评分**: PASS=1 / PARTIAL=0.5 / FAIL=0 (按每题 PASS+FAIL + PARTIAL 判据, 判据按 `smoke_v3_questions_draft.md` v3.1 每题末尾)

---

## Step 1: Notebook 状态 + Chat 配置 (**不变**)

- notebook URL: 沿用 P3.2 建立的 "SDTM Knowledge Base" notebook
- **42/42 sources indexed** (P3.4 VERIFIED, 每 tile preview PASS)
- Chat Custom mode 激活 (P3.3 H3 VERIFIED 三档可切), Custom instructions `current/instructions.md` (9,011/10,000 chars, 11% headroom)
- **不要改 instructions.md**, 不要重传 sources, 不要换 bucket
- P3.8 只测"现有配置 + v3 generalization 题库"的组合能力, 不动底座

---

## Step 2: 验证底座仍然生效 (sanity, 3 题)

**新开 chat** (避免 P3.4.5 HC-3 / P3.4 session 残留 context):

### Q_sanity_1: "AESER 的 Core 属性是 Req 还是 Exp?"
- **期望**: Exp (SDTMIG v3.4 AE spec); 若答 Req 说明底座回归, 停 smoke
- 检查 citation: 应引 `01_ae_domain_core` 或 `02_terminology_core_*` bucket

### Q_sanity_2: "LBNRIND 的 submission values 有哪些?"
- **期望**: HIGH / LOW / NORMAL / ABNORMAL (C78736, 全写); 若返 "H/L/N" 单字符说明底座漂移, 停 smoke
- 对应 instructions.md L?? "LBNRIND 全写" 硬锚

### Q_sanity_3: "CMINDC 用于哪种场景?"
- **期望**: 显式命名 CMINDC = concomitant medication indication (合并用药指征); 引用 CM 域 bucket citation
- 对应 Phase 4 N5.1 ChatGPT/Gemini 同测 anchor

**3 sanity 全 PASS → 进 Step 3**. 任一 FAIL → 停 P3.8, 先 debug instructions.md / bucket / Chat mode.

---

## Step 3: 跑 smoke v3 Q1-Q10

**规则** (与 ChatGPT/Gemini N5.3 一致以便对比):
- 按题号顺序 Q1 → Q10, **每题开新 chat** (NotebookLM 里点 "New chat"), 避 context cascade 污染
- 每题题干**从 `smoke_v3_questions_draft.md` 的 `> **题**:` 段整段复制** (不改写, 不加 hint, 不精简)
- 回答出来后**立即保存整段 markdown** 到 `dev/evidence/smoke_v3_answers/Q{N}_answer.md`, **含 inline citation marker `[1][2]...`** (NotebookLM 风格), 避免跨对话刷新丢
- 每题答完记一眼: (a) 是否命中核心事实 (b) citation 数量 (c) 是否引用了 v3.4 新域 bucket (Q1-Q3 应引 GF/CP/BE/BS 对应 bucket)
- **禁用 2 次 retry** (F-2: 同题 retry 幂等不强制, 按首答 PASS/FAIL)
- **小表单行漂移不扣语义分** (F-1-recurring: 表格渲染偶发漂移, 只要文字事实对就 PASS)

**10 题时间分配建议**:

| 题 | 主题 | 预期难度 | 建议时间 |
|---|---|---|---|
| Q1 | A1 GF 域 EGFR 基因变异 (v3.4 新域) | 中-难 | ~3 min |
| Q2 | A2 CP 域 CD4+ 流式细胞 (v3.4 新域) | 中-难 | ~3 min |
| Q3 | A3 BE + BS + RELSPEC 生物样本 (v3.4 新域) | 难 | ~4 min |
| Q4 | B1 LB vs MB vs IS 域边界 | 难 | ~4 min |
| Q5 | B2 FA vs QS vs CE 域边界 | 难 | ~4 min |
| Q6 | C1 Timing `--TPTREF/--TPT/--STTPT/--ENTPT/--DUR` | 中 | ~3 min |
| Q7 | C2 Partial date 精度 + imputation | 中-难 | ~3 min |
| Q8 | D1 Extensible vs Non-Extensible CT | 中 | ~2 min |
| Q9 | E1 Pinnacle 21 常见 FAIL 分类 | 难 | ~3 min |
| Q10 | H1 QORIG/QEVAL/QLABEL + SUPPTS vs SUPP-- | 难 | ~3 min |

**小计**: ~30-40 min (含切新 chat 间隙)

### NotebookLM 特有注意事项

- **Citation 格式**: NotebookLM 用 `[1][2][3]...` 数字 inline marker, 鼠标 hover 才显源 source 名. **保存 Q{N}_answer.md 时需把这些 marker 原样保留** (不改成 ChatGPT 的 markdown link 风格). 可 "Copy" 按钮 (回答右上) 一次性拿 markdown+marker.
- **Citation 精度**: NotebookLM citation 精度 = source (bucket) 级, 不是段级. P3.4 已验每 tile 点开可预览; 判据里若写"引 GF spec", 命中 `20_lab_findings_group_1` 等 bucket 即算 (对照 `current/uploads/MANIFEST.md` 42 bucket 映射).
- **F-3 known 弱点**: 业务场景/举例类题 (T2 题型) 偶发 inline cite dropout, 这类题 citation 缺失**不扣 A/B 题分**, 只记 Retro. 但内容事实仍按判据 PASS/FAIL.

---

## Step 4: 落档 smoke_v3_results.md

保存到: `ai_platforms/notebooklm/dev/evidence/smoke_v3_results.md`

结构模板:
```markdown
# NotebookLM — smoke v3 Q1-Q10 (P3.8 A/B) 结果

> Date: <YYYY-MM-DD>
> 题库: smoke_v3_questions_draft.md v3.1 Q1-Q10 (generalization probe, 对齐 ChatGPT+Gemini N5.3)
> PLAN 版本: v2.2 (2026-04-22 升级 v2.1→v3 Q1-Q10)
> Notebook: "SDTM Knowledge Base" (42/42 sources indexed, Chat Custom mode, instructions.md 9011 chars)
> 执行者: user (手动 copy-paste) / (可选) claude cowork MCP Chrome JS paste
> 合格阈: ≥9/10 (90%)
> 底座 sanity 3 题: PASS / FAIL (一行说明)

## 逐题结果

### Q1 (A1 GF 域 EGFR 基因变异, v3.4 新域)
- 对话 URL (可选): https://notebooklm.google.com/notebook/...
- 完整回答: `dev/evidence/smoke_v3_answers/Q1_answer.md`
- Citation 数: N ; 命中 bucket: `<bucket_name>` (对照 `current/uploads/MANIFEST.md`)
- 判据对齐 (逐项勾): 域 GF ✓ / 5 Req ✓ / 3 Exp ✓ / GFGENSR ✓ / GFPVRID ✓ / GFGENREF ✓ / GFINHERT ✓
- **Verdict**: PASS / FAIL / PARTIAL
- 归因 (若非 PASS): ...

### Q2-Q10: 类似格式

## 总分
- Strict PASS 数: X/10
- 宽判 (含 PARTIAL): Y/10
- Citation 总数: Z (avg. Z/10 per question)
- Q1-Q3 v3.4 新域命中: x/3
- Q4-Q5 域边界: x/2
- Q6-Q7 Timing: x/2
- Q8 CT: x/1
- Q9-Q10 Pinnacle+SUPP: x/2
- 是否 ≥9/10: YES / NO

## Carry-over 观察
- F-1-recurring 小表单行漂移: 发生 N 次 (不扣分)
- F-3 citation dropout T2 偏向: 业务场景题 citation 率 vs 规则题 citation 率对比
- HC-3 bucket 38 尾段: 若跑 (作第 11 题单独计, 不入分母) → PASS/FAIL 单列

## 归因 (若 <9/10)
- FAIL 题是否集中 Q1-Q3 v3.4 新域? (→ 触发 P10 (d) knowledge_base v3.4 覆盖审)
- FAIL 题是否集中 Q4-Q5 域边界? (→ 触发 instructions.md 边界规则微调)
- FAIL 题是否 citation 全缺? (→ 触发 Chat mode 切回 Learning Guide 再测)
```

另存每题完整回答到 `dev/evidence/smoke_v3_answers/Q{N}_answer.md` (10 个文件, Q1-Q10).

---

## Step 5: 回报主 session

回报格式:
```
NotebookLM smoke v3 Q1-Q10 完成: X/10 strict PASS (Y/10 宽判含 PARTIAL)
底座 sanity 3 题: PASS
- Q1-Q3 (v3.4 新域 GF/CP/BE+BS): x/3
- Q4-Q5 (域边界 LB-MB-IS / FA-QS-CE): x/2
- Q6-Q7 (Timing C1/C2): x/2
- Q8 (CT D1 Extensible): x/1
- Q9-Q10 (Pinnacle + SUPP E1/H1): x/2
- Citation 平均数/题: Z
- F-3 citation dropout T2 题型: 命中率 x/5 业务场景题 vs y/5 规则题 (证系统性弱点)
- HC-3 补题 (可选第 11 题): PASS/FAIL/未跑
- 是否 ≥9/10 阈值: YES / NO
- 归因摘要 (若未达): ...
```

主 session 接手后:
1. 派 **P3.8 答题 reviewer** (第 11 种 subagent_type, 候选 `oh-my-claudecode:critic` / `pr-review-toolkit:type-design-analyzer` / `superpowers:requesting-code-review` — 避开已用的 9-chain + P3.4.5 scientist 第 10 种) 独立审 10 题 answer + 计 PASS 比 + 交叉验 citation 精度
2. 主 session 对照判据 + bucket 映射独立复判
3. Phase 3 收束决策:
   - ≥9/10 → P3.8 PASS → P3.9 (3 档切换演练, 30 min) → Phase 3 收束 commit → Phase 4 开闸
   - 8/10 → 边缘, 用户 ack 后可作 CONDITIONAL_PASS 带 carry-over 入 Phase 4
   - ≤7/10 → 触发 P10 归因 (v2.2 (a)(b)(c)(d) 四路径)

---

## 若 smoke v3 未达 9/10 阈值

- **8/10 (边缘)**: 接受 CONDITIONAL_PASS, 记 carry-over 到 Phase 5 RETROSPECTIVE 作关键决策 (与 P3.4.5 CONDITIONAL_PASS 8.5/10 同档)
- **7/10**: 用户决策; 默认触发 P10
- **≤6/10**: 必 P10 归因, 四路径按 FAIL 集中位置选:
  - (a) FAIL 集中单 bucket 题 → source 缺失, 重 bucket
  - (b) FAIL 集中某规则 (Timing / CT / SUPP 等) → instructions.md 对应规则段微调
  - (c) FAIL 集中 citation 全缺 → Chat mode 切回 Learning Guide 再测 1 轮对照
  - (d) **v2.2 新增**: FAIL 集中 Q1-Q3 v3.4 新域 (GF/CP/BE+BS) → knowledge_base/ v3.4 新域覆盖审 (部分 v3.4 新域 KB 本身可能不全, 需 regenerate bucket 02/42 的 `_auto_source` 派发)

---

## Rule B 失败归档

若任何 sanity 或 Q{N} FAIL 触发重跑, 归档到:
- `dev/evidence/failures/p3_8_attempt_<X>_<Q>.md` — 含 (1) 原题 (2) 原答 (3) FAIL 归因 (4) 修复动作 (5) 下一 attempt 输入
- Rule B 强制: **不删**原 attempt, 累加 attempt_1, attempt_2, ...

---

## 相关路径

- 题库: `ai_platforms/smoke_v3_questions_draft.md` v3.1 (487 行, Q1-Q10 双平台共用)
- 题库设计 rationale: `ai_platforms/N5_3_QUESTIONS_DESIGN.md` (212 行, 参考)
- PLAN 锚: `ai_platforms/notebooklm/docs/PLAN.md` v2.2 §6 P3.8 + §7 A/B 矩阵 + §0 v2.2 修订记录
- 上一步 evidence: `dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md` (P3.4.5 Q1 红线 CONDITIONAL_PASS 8.5/10)
- ChatGPT 同批次 handoff: `ai_platforms/chatgpt_gpt/dev/checkpoints/CHECKPOINT_N5_3_HANDOFF.md`
- Gemini 同批次 handoff: `ai_platforms/gemini_gems/dev/checkpoints/CHECKPOINT_N5_3_HANDOFF.md`
- 42 bucket 映射: `ai_platforms/notebooklm/current/uploads/MANIFEST.md` + `dev/scripts/bucket_config.json`
- Custom instructions: `ai_platforms/notebooklm/current/instructions.md` (9,011/10,000 chars)
- _progress.json P3.8 字段: `dev/evidence/_progress.json` → `ab_matrix_plan_v2` (v2.2 更新)
- SYNC_BOARD (NotebookLM lane 独立, 不锁步 ChatGPT/Gemini, 但 v3 题库共用): `ai_platforms/SYNC_BOARD.md`

---

## 执行前最终 checklist

- [ ] 42/42 sources 仍全绿 (点 Sources 面板扫一眼, 无 re-indexing 中)
- [ ] Chat Custom mode 仍激活 (开一个 chat 看右上 mode 标)
- [ ] `instructions.md` 未被动过 (对比 git status, 应 clean)
- [ ] 新开的 sanity 3 题 chat 是**全新 chat**, 不继承 P3.4.5 context
- [ ] `smoke_v3_answers/` 目录已建 (path: `dev/evidence/smoke_v3_answers/`)
- [ ] 备好空 `smoke_v3_results.md` 模板 (Step 4 提供)
- [ ] 题源 `smoke_v3_questions_draft.md` 在 tab 里备用 (直接 copy `> **题**:` 段)

全勾 → 开始执行 Step 2 (sanity 3 题).
