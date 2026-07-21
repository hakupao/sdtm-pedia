# 下一步计划 (2026-04-22 晚 → 2026-04-23 session 更新)

> **Purpose**: 本 session 跑完 smoke v4 R1 baseline 4 平台 (17 × 4 = 68 answers) + 写 R1 retrospective. 新 session 来时先读本文 + `R1_RETROSPECTIVE.md` 即可恢复上下文.
> **当前日期**: 2026-04-23 (last revised AM)
> **上一次产物**: `git log -1` → 0bc4b1e (smoke v4 R1 闭合 + retro); 2026-04-23 新 session 启动后 (a) 澄清 P3.8 reviewer 早已完成 (12th slot), (b) 起草 Gemini v6 anti-hallucination guardrail 草案 (`gemini_gems/dev/v6_draft/system_prompt_v6.md`, 17.9K chars), (c) 派 Rule D 13th slot reviewer (`pr-review-toolkit:code-reviewer`) background 独立复判 R1 评分 + v6 adequacy
> **v1.1 修订记 (2026-04-23)**: §1 NotebookLM row + §2.1 P3.8 reviewer 项 校对为 DONE 状态 (上版 2026-04-22 晚 11:55 写时 cross-check `_progress.json` 权威源漏, 误以为未派); §2.3-2.5 Gemini R2 v6 已起草 + 13th reviewer 派出, 待 reviewer 产物回交后决策 R2 重跑.

---

## 1. 当前 4 平台 Phase 状态 (核实后的精确快照)

| 平台 | Phase 状态 | 本次 R1 表现 | 下一步 |
|---|---|---|---|
| **Claude Projects** | ✅ 完全结束 (不参与 SYNC_BOARD) | 17/17 (100%) | — (R2 可选, 不必要) |
| **ChatGPT GPTs** | ✅ Phase 4 COMPLETE (N5.4 + Rule D #24) | 16.5/17 (97.1%) | 🔒 Phase 5 pending, 冻结等 NotebookLM |
| **Gemini Gems** | ✅ Phase 4 闭合 + **R2 PASS ✓✓ (2026-04-23 PM)** | R1 12.0/17 → **R2 16.0/17 (94.1%)**, 主 gate **12.5/13 (96.2%)**, AHP 0/3 → **3/3 PASS+** | ✅ Phase 5 ready (14th reviewer APPROVE, 0 blockers) |
| **NotebookLM** | 🔄 Phase 4 部分完成 | 15/17 (88.2%) | P3.9 三档分享切换未做 (P3.8 reviewer ✅ 已完成 12th slot, 见下方修正) |

**SYNC_BOARD 锁步状态**: ChatGPT + Gemini 已 Phase 5 pending 冻结, 等 NotebookLM P3.9 拉齐后跨 4 平台合流启 Phase 5 RETROSPECTIVE (P3.8 reviewer 已闭合, 不再是阻塞项).

**smoke v4 R1 对 NotebookLM Phase 4 的影响**: 消掉了 "Phase 4 #3 跨 4 平台对比矩阵" 子项 (✅ SMOKE_V4.md §3 矩阵 17 × 4 已全填). NotebookLM Phase 4 仍欠 #2 (P3.9 三档分享切换演练), #1 P3.8 reviewer 实际早已于 2026-04-22 PM 完成 (12th slot `feature-dev:code-reviewer`, evidence `ai_platforms/notebooklm/dev/evidence/p3_8_reviewer_notes.md`, `_progress.json` L509-547 `p3_8_reviewer_verdict_12th_slot` 块记录 PASS 9/10 + 5 action items).

---

## 2. 下一步推荐优先级

### 🔥 最高优先 (阻塞项): NotebookLM P3.9 + Gemini R2 v6 reviewer 回收

**为什么最高**: ChatGPT + Gemini 已冻结 Phase 5 pending, 卡在等 NotebookLM P3.9 拉齐. NotebookLM Phase 4 完成后 → 跨 4 平台统一启 Phase 5 (享受 cross-pollination + `_template/` 补丁合并红利). Gemini R2 平行推进, 不阻塞 NotebookLM.

#### ~~2.1 NotebookLM P3.8 reviewer~~ ✅ DONE (2026-04-22 PM, 2026-04-23 session 澄清)

**实际状态 (校对权威源后)**:
- Evidence: `ai_platforms/notebooklm/dev/evidence/p3_8_reviewer_notes.md` (119 行)
- 12th slot Rule D subagent_type: `feature-dev:code-reviewer` (非 11th — 11th 是 `oh-my-claudecode:document-specialist` 做 smoke v3→v4 audit)
- Verdict: **PASS** (9/10 strict 维持, 无降级依据)
- 5 action items: #1 HIGH (Q10 SUPPTS) 已 bundled 进 v4.0; #2 MEDIUM (Q3 BETERM 降 MINOR); #3 MEDIUM (Finding 6/7 登记); #4 MEDIUM (Rule A caveat: N ≥ 5 抽检补 Phase 5 retro); #5 MEDIUM (Rule E caveat: `p3_8_user_ack` structured field 补登)
- `_progress.json` L509-547 `p3_8_reviewer_verdict_12th_slot` 块完整记录

**上版 NEXT_STEPS v1.0 (2026-04-22 晚 11:55) 误判为未派的原因**: 写作时未 cross-check `_progress.json` authoritative source, 凭 R1 lifecycle "Rule D chain 第 13 种未派" 句子反推, 但那句指的是"下一 slot 13th"而非"P3.8 reviewer 未派". 澄清归档.

**5 action items 剩余**: #3/#4/#5 挪 Phase 5 RETROSPECTIVE 合流处理 (非阻塞). #1/#2 已 bundled.

#### 2.2 NotebookLM P3.9 (3 档分享切换演练) ← 当前 NotebookLM 唯一阻塞项

**任务**: 演练 Custom Mode / Learning Guide / Custom 回切 3 档分享模式切换, 验证 H3 hypothesis VERIFIED PASS (已在 P3.3 做初步验证, P3.9 正式归档).

**注**: 可能已在 P3.3 chat_mode_toggle_test.md 涵盖 (210 行). P3.9 是否单独跑还是引用 P3.3 evidence? **新 session 读 PLAN v2.2 §P3.9 确认**.

**预估时间**: 30-90 分钟 (若单独跑 Chrome MCP 演练)

### 🔶 次优先 (能力提升, 并行推进): Gemini R2 v5c → v6

**为什么次优先**: Gemini Phase 4 已 PASS (N5.4 Rule D #25), R1 FAIL 的是 smoke v4 新 AHP 维度. 不阻塞 SYNC_BOARD 合流, 但影响跨平台最终产物质量.

#### 2.3 Gemini system_prompt v6 draft ✅ DONE (2026-04-23)

**产物**: `ai_platforms/gemini_gems/dev/v6_draft/system_prompt_v6.md` (338 行 / **17,883 chars**; v5c 11,132 → v6 17,883, +6,751 chars, +60%)

**v6 新增内容**:
- **CO-5 ANTI-HALLUCINATION GUARDRAIL** 整节 (新): AHP-V1 变量级幻觉 + AHP-V2 跨域层级幻觉 + AHP-V3 Deprecated concept 幻觉 + 6 条 CO-5 共同执行规则
- **CO-2e** 子条款: C66742 NY codelist 4 值 (Y/N/U/NA) + C66767 Non-Ext (Q8 R1 PARTIAL 修)
- **回答规范** 补 "多场景题逐场景显式答" (Q4 R1 修) + "SDTM vs ADaM 边界 --DTF ADaM-only" (Q7 R1 修)
- **路由规则** 1/3/4/7 插 CO-5 check hook, 新增 Route 7 Deprecated
- **边界处理模板** ⑥⑦⑧ 对应 AHP-V1/V2/V3 标准话术
- **工作流程** Step 0 前提核 + Step 9 多场景显式 + Step 10 sanity 自检

**字符预算澄清**: v5c header 标 "8K/10K cap" 是旧草约束, Gem UI 实际接受 v5c 11,132 chars 不拒. v6 17,883 chars 若 UI 拒再压缩, 作 Rule D 13th reviewer 审时的边界问题.

#### 2.4 Rule D 13th slot reviewer (`pr-review-toolkit:code-reviewer`) 🔄 RUNNING (2026-04-23)

**已派出 (background)**: `pr-review-toolkit:code-reviewer` 独立复判 (1) R1 主 session 判分准确性 (包括 Gemini 8.5/13 FAIL gate + AHP × 3 FAIL + 4 平台跨平台矩阵), (2) Gemini v6 prompt draft 修 AHP × 3 FAIL 的能力.

**Reviewer 输出回交**: 主 session 落档 `ai_platforms/gemini_gems/dev/evidence/r2_13th_reviewer.md` + 回交决策 (v6 draft 是否需修正后才跑 R2 / 字符预算是否减).

#### 2.5 跑 Gemini v6 × 17 题 ✅ COMPLETE (2026-04-23 PM)

**执行**: 主 session 经 Chrome MCP cowork 单 session 连续跑 17 题, v6-post-A1 (18,716 chars) 已 pre-apply to Gem UI.

**结果** (主 session self-score + 14th reviewer 独审 APPROVE):
- Q1-Q10 主 gate: **9.5/10 (95%)** — Q1 PARTIAL (GFGENE regression) + Q2-Q10 全 PASS/PASS+
- AHP × 3 hard gate: **3/3 PASS+ (100%)** — R1 0/3 FAIL → R2 3/3 PASS+ 完全修复
- 主 gate 合计: **12.5/13 (96.2%)** (R1 8.5/13 = 65.4%, +30.8%)
- Bonus Q11-Q14: 3.5/4 strict (Q13 PARTIAL 同 R1 ARMCD 规则 gap)
- **Strict 总分: 16.0/17 (94.1%)** (R1 12.0/17 = 70.6%, +23.5%)
- **双硬 gate: PASS ✓✓** — Q1-Q10 9.5 ≥ 7 + AHP 3 ≥ 2

**关键发现 (v6 effectiveness)**:
- ✅ CO-5 AHP-V1/V2/V3 章 + A1 dual-grep 对 AHP × 3 完全生效 (14th reviewer 判 AHP-V2/V3 "真修 structural invariant", AHP-V1 "近真修" 置信 78)
- ✅ Q4/Q7/Q8 micro-fix (多场景 / --DTF ADaM-only / C66742 4 值 + C66767 Non-Ext) 全线修复 R1 PARTIAL
- ⚠️ **v7 carry-over HIGH × 2**: Q1 GF Exp 正向清单 (GFGENE 违反 CO-4 negative list) + Q13 ARMCD-null + ARMNRS 全称 + C142179 锚 (v6 未覆盖)

**独立复核**: 14th slot Rule D reviewer (`oh-my-claudecode:verifier`) APPROVE / high confidence / 0 blockers. 所有 5 key verdict 与主 session 一致. 报告 `ai_platforms/gemini_gems/dev/evidence/r2_14th_reviewer.md`.

**Gate 判定**: **Gemini Phase 4 完全闭合 + Phase 5 ready**. SYNC_BOARD Gemini row 可转 Phase 5 ready (carry-over Q1/Q13 v7 迭代 non-blocking).

### 🔹 低优先 (可延后)

#### 2.6 ChatGPT R2 Q1 拼写 MINOR fix
- Q1 GFINHERT 被 ChatGPT 写成 GFINHERTG (1 字符多). system_prompt v2 → v2.1 加 "GFINHERT 写全, 不加 G" 锚. 可选, 不阻塞 Phase 5.

#### 2.7 Claude R2 完全 skip
- 17/17 已达 v2.6 极限, R2 可跳.

---

## 3. 推荐执行顺序 (v1.1 2026-04-23 修订)

```
2026-04-23 session 已完成
  ├─ 澄清 P3.8 reviewer = DONE (12th slot, 见 2.1)
  ├─ 2.3 Gemini v6 draft 写就
  └─ 2.4 派 pr-review-toolkit:code-reviewer (13th slot, background)

下一 session 启动
  ↓
读 NEXT_STEPS.md v1.1 (本文) + R1_RETROSPECTIVE.md + r2_13th_reviewer.md (reviewer 产物)
  ↓
[分支 A: NotebookLM P3.9 (SYNC_BOARD 唯一剩余阻塞)]
  ├─ 2.2 P3.9 三档切换演练 (引用 P3.3 evidence 或 Chrome MCP 再跑)
  └─ 更新 SYNC_BOARD + NotebookLM _progress.json P3.9 完成字段
  ↓
[分支 B: Gemini R2 v6 → Re-run (可与 A 并行)]
  ├─ 读 r2_13th_reviewer.md (13th slot verdict)
  ├─ 若 reviewer 有修订建议: apply 修订 → v6.1 draft
  ├─ 2.5 Gemini v6(.1) × 17 题重跑 (Chrome MCP), 对比 R1 baseline
  ├─ 新阈值: AHP × 3 hard gate (≥2/3) + Q1-Q10 ≥7/10
  └─ 若 PASS → apply v6 to Gem UI; 若 FAIL → v7 迭代
  ↓
[汇合: Phase 5 统一 RETROSPECTIVE]
  4 平台全齐后跨 lane 合流 (ChatGPT/Gemini SYNC_BOARD 3 finding + NotebookLM 独立 lane 教训 + 5 action items 消化 + Rule A/E caveat retro 补)
```

**推荐走法 (v1.1)**:
- 下一个 session (第三 session): **跑 2.2 (30-90 min) + 2.5 (1-2 h)**, A 分支 + B 分支可并行, 共计 2-3 小时
- 第四 session: Phase 5 统一 RETROSPECTIVE (4 平台全齐后)

---

## 4. 预留决策点 (给你思考)

### 决策 1: AHP × 3 是否设 R2 的 hard gate?

**R1 发现**: Gemini Q1-Q10 主表现 8.5/10 还过得去, AHP × 3 全 FAIL 拖分. 若不设 hard gate, 未来版本升级可能"假 PASS".

**建议**: R2 改 "主 gate 阈 ≥ 9/13" 为 "Q1-Q10 ≥ 7/10 + AHP ≥ 2/3" 双约束.

### 决策 2: Gemini v6 走 prompt-only 还是 KB 补 file?

- **Prompt-only**: 简单, 但 v5 7925/8000 超限风险, 需压缩 v5
- **KB 补 file** (第 5 个 KB file): 清晰分层, 但 Gemini 1M token 窗口下加 1 file 不太构成负担

**推荐**: 先 prompt-only 试一版, 若字符预算挤不下再加 KB file.

### 决策 3: 是否加 Rule E (跨平台 cross-check) 到全局 CLAUDE.md?

**R1 证明价值**: 4 平台并发 ≥ 3 = 事实上的 multi-reviewer baseline, Gemini 单平台 AHP FAIL 有 3 平台对比作 ground truth 才能无歧义判断.

**建议**: 写入 `~/.claude/CLAUDE.md` 的 personal_operating_principles section (Rule E 候选已在 `R1_RETROSPECTIVE.md §4.D5` 登记).

### 决策 4: NotebookLM Q11/Q12 PARTIAL 是否视为架构限制?

**R1 发现**: NotebookLM Q11 Dataset-JSON + Q12 CT 版本 PARTIAL 是 42-source KB 不深入 supplemental topics, 非能力 FAIL.

**建议**: 与 Q9 Pinnacle 21 FAIL-PUNT 同归类 "architecture-scope N/A", 不与 capability FAIL/PARTIAL 混计. 后续改 KB (加 supplemental chapter source) 才能提分.

---

## 5. 相关文件速查

```
# R1 核心产物 (本 commit 落档)
ai_platforms/SMOKE_V4.md                          # 题库 + R1 plan + §3 跨平台矩阵 (17×4)
ai_platforms/R1_RETROSPECTIVE.md                  # Rule C 产物 (保留/缺口/决策 + R2 plan)
ai_platforms/R1_SESSION_HANDOFF.md                # 2 版 R1 进度 handoff
ai_platforms/NEXT_STEPS.md                        # 本文
ai_platforms/SYNC_BOARD.md                        # 锁步看板 (未更新, 下次 session 读)

# 4 平台 evidence (每平台 17 answer.md + 1 results.md)
ai_platforms/{notebooklm,gemini_gems,chatgpt_gpt,claude_projects}/dev/evidence/
  smoke_v4_answers/{Q1-Q14}_answer.md + {AHP1-3}_answer.md
  smoke_v4_results.md (总分填完)
  _progress.json (总分待更新进 checkpoints_acked)

# R2 起点候选
ai_platforms/gemini_gems/docs/PLAN_V2_C.md        # Gemini C 方案 Node 4 架构
ai_platforms/gemini_gems/dev/evidence/smoke_v4_answers/AHP{1,2,3}_answer.md  # 含 "R2 建议"
ai_platforms/gemini_gems/dev/v6_draft/system_prompt_v6.md  # **v6 draft 2026-04-23**, 17.9K chars, 待 13th reviewer 审
ai_platforms/gemini_gems/dev/evidence/r2_13th_reviewer.md  # **待主 session 落档**, 13th slot pr-review-toolkit:code-reviewer 产物
ai_platforms/notebooklm/dev/evidence/p3_8_reviewer_notes.md  # **已完成 2026-04-22 PM**, 12th slot feature-dev:code-reviewer 独立审 P3.8 9/10 PASS 维持
```

---

## 6. 本 session 核心洞察 (给未来你一个 hook)

1. **AHP × 3 是 v4 的灵魂**: 不加 AHP, Gemini 会用 12.5/17 骗过 71% 阈 PASS; 加了 AHP, 能力差异无歧义暴露
2. **4 平台 cross-check 等价于 multi-reviewer**: NotebookLM in-KB-only 作 "找不到就说不存在" ground truth, 其他 3 平台 (web search/训练数据) 的编造自然暴露
3. **Claude 一致性最深**: 17/17 全 PASS+, 训练数据 + 19-file KB + web fetch 三重 cross-check 给最深答案
4. **Gemini 失陷只在 AHP, 不在 KB 覆盖**: bonus Q11-Q14 意外 4/4 (4-file KB 不含 supplemental 但训练数据补齐), 说明 anti-hallucination 锚缺失 是唯一问题
5. **v4 判据修正合理**: v3 的 "ChatGPT 14/14 + NotebookLM 9/10" 在 v4 仍基本稳定, 说明 smoke v3 高分不是虚的, Q10 SUPPTS 只是唯一一个真正的 "答对错前提的巧合"

---

*v1.0 2026-04-22 晚 11:55 PM. 下次 session 读本文 + R1_RETROSPECTIVE.md 即可恢复. 推荐先做 2.1 NotebookLM P3.8 reviewer 解 SYNC_BOARD 阻塞.*
