# 下一步计划 (2026-04-22 晚收尾 → 下次 session)

> **Purpose**: 本 session 跑完 smoke v4 R1 baseline 4 平台 (17 × 4 = 68 answers) + 写 R1 retrospective. 新 session 来时先读本文 + `R1_RETROSPECTIVE.md` 即可恢复上下文.
> **当前日期**: 2026-04-22 晚 11:55 PM
> **上一次产物**: `git log -1` → 本次 commit (smoke v4 R1 闭合 + retro)

---

## 1. 当前 4 平台 Phase 状态 (核实后的精确快照)

| 平台 | Phase 状态 | 本次 R1 表现 | 下一步 |
|---|---|---|---|
| **Claude Projects** | ✅ 完全结束 (不参与 SYNC_BOARD) | 17/17 (100%) | — (R2 可选, 不必要) |
| **ChatGPT GPTs** | ✅ Phase 4 COMPLETE (N5.4 + Rule D #24) | 16.5/17 (97.1%) | 🔒 Phase 5 pending, 冻结等 NotebookLM |
| **Gemini Gems** | ✅ Phase 4 COMPLETE (N5.4 + Rule D #25) | 12.5/17, 主 gate 65.4% **FAIL** | 🔥 **R2 必须**: v5→v6 加 anti-hallucination 锚点 |
| **NotebookLM** | 🔄 Phase 4 部分完成 | 15/17 (88.2%) | P3.8 reviewer + P3.9 未做 |

**SYNC_BOARD 锁步状态**: ChatGPT + Gemini 已 Phase 5 pending 冻结, 等 NotebookLM 拉齐 Phase 4 (P3.8 reviewer + P3.9) 才合流统一启 Phase 5 RETROSPECTIVE.

**smoke v4 R1 对 NotebookLM Phase 4 的影响**: 消掉了 "Phase 4 #3 跨 4 平台对比矩阵" 子项 (✅ SMOKE_V4.md §3 矩阵 17 × 4 已全填). NotebookLM Phase 4 仍欠 #1 (P3.8 reviewer) + #2 (P3.9 三档分享切换).

---

## 2. 下一步推荐优先级

### 🔥 最高优先 (阻塞项): NotebookLM P3.8 reviewer + P3.9

**为什么最高**: ChatGPT + Gemini 已冻结 Phase 5 pending, 卡在等 NotebookLM 拉齐. NotebookLM Phase 4 完成后 → 跨 4 平台统一启 Phase 5 (享受 cross-pollination + `_template/` 补丁合并红利).

#### 2.1 NotebookLM P3.8 reviewer (第 11 种 NotebookLM chain subagent_type 未派)

**任务**: 派独立 reviewer subagent 审 P3.8 执行产物 (smoke v3 Q1-Q10 9/10 strict PASS + 主 session 独立复判 5 findings 含 Q10 (b) 前提错).

**候选 subagent**:
- `oh-my-claudecode:document-specialist` (11th slot 候选, 已在 SMOKE_V4_DESIGN_HANDOFF.md §7 登记)
- `pr-review-toolkit:code-reviewer`
- `oh-my-claudecode:verifier`

**执行 prompt pointer**:
- 读 `ai_platforms/notebooklm/dev/evidence/phase3_task_P3.8_xxx.md` + `smoke_v3_results.md`
- 独立判 P3.8 执行是否 strict PASS, 主 session 5 findings 是否合理, Q10 前提错修订方向是否正确
- 产物 `ai_platforms/notebooklm/dev/evidence/p3_8_reviewer.md`

**预估时间**: 30-60 分钟 (subagent 运行时间)

#### 2.2 NotebookLM P3.9 (3 档分享切换演练)

**任务**: 演练 Custom Mode / Learning Guide / Custom 回切 3 档分享模式切换, 验证 H3 hypothesis VERIFIED PASS (已在 P3.3 做初步验证, P3.9 正式归档).

**注**: 可能已在 P3.3 chat_mode_toggle_test.md 涵盖 (210 行). P3.9 是否单独跑还是引用 P3.3 evidence? **新 session 读 PLAN v2.2 §P3.9 确认**.

**预估时间**: 30-90 分钟 (若单独跑 Chrome MCP 演练)

### 🔶 次优先 (能力提升): Gemini R2 v5 → v6

**为什么次优先**: Gemini Phase 4 已 PASS, R1 FAIL 的是 smoke v4 新 AHP 维度. 不阻塞 SYNC_BOARD 合流, 但影响跨平台最终产物质量.

#### 2.3 Gemini system_prompt v6 draft

**必改点** (来自 R1_RETROSPECTIVE.md §5):
```
### ANTI-HALLUCINATION GUARDRAIL (v6 新增, ~500 chars)
规则 1 变量识别: 任何用户提到的变量, 必须先在 04_business_scenarios.md 变量索引确认;
  未找到则主动识破 + 提示 SUPP-- NSV 路径 (ch08 §8.4). 严禁编 Core/C-code/Role.
规则 2 跨域关系: SDTM tabulation 永远是 subject-level record. 若问 'study-level aggregation',
  必须识破 → ADaM ADAE 或 CSR 职责, 不在 SDTM.
规则 3 Deprecated concept: PF (Pharmacogenomics Findings) 已 deprecated; v3.4 用 GF + BE + BS + RELSPEC.
  严禁编 PF 变量.
```

**字符预算**: 现 v5 = 7925/8000. 加 500 超限, 需先压缩 v5 既有 CO-4 部分. 或考虑加第 5 个 KB file `05_anti_hallucination_anchors.md`.

**预估时间**: 1-2 小时 (draft + 字符预算优化 + 独立 reviewer 复判)

#### 2.4 派 Rule D 13th slot: pr-review-toolkit:code-reviewer

**任务**: 独立复判 (1) R1 主 session 判分准确性 (2) Gemini v6 prompt draft 合理性.

**预估时间**: 30-45 分钟 subagent 运行

#### 2.5 跑 Gemini v6 × 17 题, 对比 R1 baseline

**阈值建议 (R2 调整)**: AHP × 3 设 **hard gate** (必 ≥ 2/3), 而非仅主 gate summing ≥ 9/13. 若 Gemini v6 AHP ≥ 2/3 → Phase 4 gate 开闸.

**预估时间**: 1-1.5 小时 (17 题 × ~4 min)

### 🔹 低优先 (可延后)

#### 2.6 ChatGPT R2 Q1 拼写 MINOR fix
- Q1 GFINHERT 被 ChatGPT 写成 GFINHERTG (1 字符多). system_prompt v2 → v2.1 加 "GFINHERT 写全, 不加 G" 锚. 可选, 不阻塞 Phase 5.

#### 2.7 Claude R2 完全 skip
- 17/17 已达 v2.6 极限, R2 可跳.

---

## 3. 推荐执行顺序 (建议新 session 按此顺序)

```
新 session 启动
  ↓
读 NEXT_STEPS.md (本文) + R1_RETROSPECTIVE.md
  ↓
[分支 A: 优先解 SYNC_BOARD 阻塞]
  ├─ 2.1 派 NotebookLM P3.8 reviewer subagent (#11 NBL chain slot)
  ├─ 2.2 P3.9 演练 (若需要, 否则引用 P3.3)
  └─ 更新 SYNC_BOARD + _progress.json
  ↓
[分支 B: Gemini R2 能力修复, 可并行或顺序]
  ├─ 2.3 Gemini v6 prompt draft
  ├─ 2.4 派 pr-review-toolkit:code-reviewer (Rule D 13th)
  └─ 2.5 Gemini v6 × 17 题重跑, 对比 R1 baseline
  ↓
[汇合: Phase 5 统一 RETROSPECTIVE]
  跨 4 平台合流 (3 lane SYNC_BOARD finding + NotebookLM 独立 lane 教训)
```

**推荐走法**:
- 下一个 session: **先跑 2.1 + 2.2** (新 subagent 动作快, 30-90 分钟), 解 SYNC_BOARD 阻塞
- 第三 session: **跑 2.3-2.5** (Gemini R2), 3-4 小时投入
- 第四 session: Phase 5 统一 RETROSPECTIVE

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
