# AI 平台双平台并行部署 — 锁步看板 (SYNC_BOARD)

> **目的**: ChatGPT GPTs + Gemini Gems 在 Phase 0-5 上严格锁步, 不靠人脑记, 由主 session 机械 gate.
> **覆盖平台**: `ai_platforms/chatgpt_gpt/` + `ai_platforms/gemini_gems/` (Claude Projects 已完成, 不参与本看板)
> **建立日期**: 2026-04-20
> **最后更新**: 2026-04-20 (Phase 1 双边 CONDITIONAL_PASS; Gemini profile C1 已修复; 等用户 ack 进 Phase 2)

---

## 锁步规则 (非协商)

1. **Phase N 两边都 PASS 之前, 任一方都不能进入 Phase N+1**. 主 session 在派发 Phase N+1 subagent 前, 必须读本看板 + 两份 `_progress.json`, 验证两边 Phase N = PASS. 未 PASS 则拒绝派发并汇报缺了什么.
2. **PASS 四条定义** (规则 D 强制, 缺一不可):
   - evidence 文件存在 (路径登记进本看板"Evidence 路径"段)
   - writer lane 产物合规 (格式 / 字段 / 链接完整)
   - **独立 reviewer lane PASS** (不同 subagent_type, 不得同 session 自审)
   - 主控用户**口头 ack** ("进 Phase N+1")
3. **偏离 >1 Phase 触发警示**: 若一边 doing Phase 3 而另一边仍在 Phase 1, 必须先同步慢的, 再推快的. 严禁跑完一边再补另一边.
4. **跨 session 持久**: 新 session 启动若涉及 chatgpt_gpt 或 gemini_gems, 第一件事读本文件 + 两份 `_progress.json`, 定位"当前锁步 Phase"再开工.

---

## 当前状态 (每步更新)

- **当前锁步 Phase**: Phase 2 完成 (双边 CONDITIONAL_PASS), Phase 3 待用户 ack 解锁
- **允许的下一动作**: 等用户 ack 后, 主 session 派发 Phase 3 落地 subagent (合并脚本 + 批次执行 + A/B)
- **偏离告警**: 无
- **上一次状态更新**: 2026-04-20 (PLAN writer 双边成功 ChatGPT 660 行/Gemini 578 行; verifier 双边 CONDITIONAL_PASS; ChatGPT 1 MEDIUM + 2 LOW / Gemini 2 LOW 全部 carry-over 到 Phase 3)

---

## Phase 矩阵 (状态总览)

| Phase | 内容 | ChatGPT GPTs | Gemini Gems | Phase 准入 Gate |
|-------|------|:---:|:---:|---|
| **0 启动** | `docs/platform_profile.md` 填完 + 用户优先级 ack (规则 E) | ✅ PASS | ✅ PASS | — (起点) |
| **1 调研** | 八问八答 → `docs/research.md` (Gemini 简化 3 问) | ✅ PASS (CGT C1→Phase2) | ✅ PASS (C1 修复 / C2→Phase2) | 两平台 Phase 0 = PASS ✅ |
| **2 策略+PLAN** | `docs/PLAN.md` 含 P1-P13 规则 + 批次设计 | ✅ PASS (1 MED + 2 LOW→P3) | ✅ PASS (2 LOW→P3) | 两平台 Phase 1 = PASS ✅ |
| **3 落地** | 批次执行 + evidence L1/L2 + 每批 A/B | ⏳ 待 ack | ⏳ 待 ack | 两平台 Phase 2 = PASS ✅ (等用户 ack) |
| **4 审查** | 三 lane 回归 + A/B 矩阵 (CGT 10-15 题 / GEM 10 题) | 🔒 locked | 🔒 locked | 两平台 Phase 3 终批 PASS |
| **5 收束** | RETROSPECTIVE + UPLOAD_TUTORIAL + ROADMAP 更新 | 🔒 locked | 🔒 locked | 两平台 Phase 4 = PASS |

**图例**: ⏳ todo · 🟡 doing · ✅ PASS · 🔒 locked (gate 未开) · ⚠️ 偏离

---

## 每 Phase Gate 细则

### Phase 0 → 1 Gate ✅ 已开

| Gate 条件 | ChatGPT | Gemini |
|----------|:---:|:---:|
| `docs/platform_profile.md` 所有占位符填空 (5+ 字段) | ✅ 97% | ✅ 97% |
| 用户业务优先级 ack (Rule E) | ✅ Q1=C/Q2=C/Q5=A | ✅ Q3=C/Q4=A/Q5=A |
| evidence 路径登记本看板 | ✅ phase0_reviewer.md | ✅ phase0_reviewer.md |
| Reviewer lane PASS (Tier 2 强制) | ✅ CONDITIONAL_PASS | ✅ CONDITIONAL_PASS |

### Phase 1 → 2 Gate ✅ 已开 (等用户 ack)

| Gate 条件 | ChatGPT | Gemini |
|----------|:---:|:---:|
| `docs/research.md` 完成 (八问八答 / 简化 3 问) | ✅ 10/10 (9 ANS + 1 PARTIAL→P3) | ✅ 6/6 (3必答+Q4+carry-over 2) |
| 来源链接完整 (官方 + 社区 / 学术) | ✅ 每问 ≥2 来源 | ✅ Q1 六来源, 其他 ≥3 |
| "对 PLAN 的修订" 段落产出 | ✅ 10 条 | ✅ 8 条 |
| Phase 0 carry-over 关闭 | ✅ B/E CLOSED, C PARTIAL→P3 | ✅ A CLOSED, F-1 PARTIAL→P3 |
| Reviewer lane PASS | ✅ CONDITIONAL_PASS | ✅ CONDITIONAL_PASS |
| **用户 ack 进 Phase 2** | ⏳ 等 | ⏳ 等 |

**Phase 1 Carry-over 到 Phase 2**:
- ChatGPT MEDIUM: Instructions "8,000 字符" source URL 缺失 + tokens/chars 4x 精度差 → Phase 2 PLAN writer 补齐
- Gemini LOW: F-1 末尾召回量化 transfer_to_phase3 → Phase 2 PLAN P12 段标注 Phase 3 hard checkpoint (末尾 codelist 精确 term 2 道)
- Gemini MEDIUM (C1) **已修复**: profile.md E/I/F section 根据 Q3 调研同步更新 (2025-09 分享功能发布)

### Phase 2 → 3 Gate
- PLAN.md 含 P1-P10 范本规则 + 平台独有 P11+ (ChatGPT P11-P13, Gemini P11-P12)
- Rule E: 用户业务优先级已乘入打分公式, 非事后重平衡
- 每 Task 明示 checkpoint 级别 (hard / soft / none)
- 批次粒度 + A/B 矩阵大小确定
- Reviewer lane PASS (code-reviewer)

### Phase 3 → 4 Gate
- 所有批次 evidence 入 `_progress.json` (L1)
- 每批一份 `dev/ab_reports/STAGE_<N>_AB_REPORT.md`
- 失败归档规则 B: `evidence/failures/stage_<N>_attempt_<M>.md` 若有失败
- Hard checkpoint 用户均已 ack
- **ChatGPT**: Q8 Indexing indicator 实测 (Phase 1 PARTIAL transfer)
- **Gemini**: 末尾召回 2 题 PASS (Phase 1 PARTIAL transfer)

### Phase 4 → 5 Gate
- A/B 矩阵 PASS 比 ≥ 目标阈值 (CGT 建议 ≥ 90%, GEM 建议 ≥ 90%)
- 主控独立抽样 Rule A 完成 (样本数 N 写进 PLAN, 产物 `evidence/step_NN_audit.md`)
- 写审分离规则 D 全程满足

### Phase 5 完成 (归档前)
- `docs/RETROSPECTIVE.md` 过规则 D 独立复核 PASS
- `current/UPLOAD_TUTORIAL.md` 10 章节产出
- `ROADMAP.md` 状态 `**待开始**` → `**已完成**` + 实际 capacity / A/B 数据
- `ai_platforms/README.md` 总览表格更新
- `CLAUDE.md` Key Paths 回填新入口
- Commit + push

---

## Evidence 路径速查

| 资产 | ChatGPT GPTs | Gemini Gems |
|------|-------------|-------------|
| L1 progress | `ai_platforms/chatgpt_gpt/dev/evidence/_progress.json` | `ai_platforms/gemini_gems/dev/evidence/_progress.json` |
| Phase 0 profile | `ai_platforms/chatgpt_gpt/docs/platform_profile.md` ✅ | `ai_platforms/gemini_gems/docs/platform_profile.md` ✅ (Phase 1 Q3 更新) |
| Phase 0 reviewer | `ai_platforms/chatgpt_gpt/dev/evidence/phase0_reviewer.md` ✅ | `ai_platforms/gemini_gems/dev/evidence/phase0_reviewer.md` ✅ |
| Phase 1 research | `ai_platforms/chatgpt_gpt/docs/research.md` ✅ (261 行) | `ai_platforms/gemini_gems/docs/research.md` ✅ (215 行, Attempt 2) |
| Phase 1 reviewer | `ai_platforms/chatgpt_gpt/dev/evidence/phase1_reviewer.md` ✅ | `ai_platforms/gemini_gems/dev/evidence/phase1_reviewer.md` ✅ |
| L3 失败归档 (规则 B) | (暂无) | `ai_platforms/gemini_gems/dev/evidence/failures/stage_phase1_attempt_1.md` ✅ |
| L2 trace (Tier 3 才必要) | `ai_platforms/chatgpt_gpt/dev/evidence/trace.jsonl` | `ai_platforms/gemini_gems/dev/evidence/trace.jsonl` |
| L3 subagent prompts | `ai_platforms/chatgpt_gpt/dev/evidence/subagent_prompts/` | `ai_platforms/gemini_gems/dev/evidence/subagent_prompts/` |
| A/B 报告 (每批一份) | `ai_platforms/chatgpt_gpt/dev/ab_reports/` | `ai_platforms/gemini_gems/dev/ab_reports/` |
| Hard checkpoint 握手 | `ai_platforms/chatgpt_gpt/dev/checkpoints/` | `ai_platforms/gemini_gems/dev/checkpoints/` |

---

## 偏离记录 (若发生)

格式: `YYYY-MM-DD | 偏离描述 | 修正动作 | 是否已恢复锁步`

- 2026-04-20 | Gemini Phase 1 Attempt 1 过早终止 (40 秒, research.md 未落盘, 中途思考被当最终 reply) | Rule B 归档到 `failures/stage_phase1_attempt_1.md`, Attempt 2 加强 prompt (PHASE1_RESEARCH_COMPLETE: 前缀 + Read 自验证) 成功 | ✅ 恢复锁步

---

## 操作流程 (给主 session 的机械指令)

**新 session 启动**:
1. 读本文件定位"当前锁步 Phase"
2. 并行读两平台 `_progress.json` 核对
3. 若不一致, 以 `_progress.json` 为真, 修正本看板
4. 报告当前状态 + 下一步建议给用户

**每步操作完**:
1. 更新对应平台 `_progress.json` (状态 / evidence_paths / 时间戳)
2. 同步更新本看板 Phase 矩阵该格
3. 若刚跨过 gate, 更新"当前状态"段

**gate 判定伪码**:
```
if chatgpt.phase_N.status == "PASS" and gemini.phase_N.status == "PASS":
    允许两边并行进 Phase N+1 (主 session 派发 2 个 subagent)
elif one_side == "PASS" and other == "doing":
    等慢的一边完成, 不推快的
elif one_side == "PASS" and other == "todo":
    ⚠️ 偏离告警; 慢的立刻启动 Phase N
```

**并行派发模式** (每 Phase 内):
- 主 session 用 2 个 subagent 并行 (一个做 ChatGPT, 一个做 Gemini)
- 主 session 在两者都完成后做 cross-review: 若一边发现 `_template/` 缺陷, 另一边立即吸收
- 两边独立 reviewer lane PASS 后, 主 session 合并 evidence, 开 gate

---

## Phase 3 Node 规划 (2026-04-20 共识, 每 node 独立 commit)

Phase 3 分 6 个 session node, 每 node 结束即 commit + 可切换 session resume:

| Node | 内容 | Hard checkpoint | Commit tag |
|------|------|:---:|:---:|
| **N1** | 主 session 先修 ChatGPT §3.2 MEDIUM (score 公式) → 双平台 `merge_for_*.py` 开发 (2 executor opus) → 双平台 reviewer 审脚本 | ✅ 用户看脚本 | C1 |
| **N2** | 跑脚本产物: ChatGPT batch 1 (4 文件 P0) + Gemini 全批 (3-4 文件); 溯源/TableAware/token 校验 | 软 gate | C2 |
| **N3** | 平台配置 + 上传 + Smoke: GPT Builder Instructions + 4 Conversation Starters + 上传; Gem Instructions + 单批上传; 两平台各 3-5 题 smoke | ✅ 看 smoke 答题 | C3 |
| **N4** | ChatGPT batch 2 合并 + 上传 (文件 5-9); Gemini 并行 A/B 预热 (利用锁步间隙) | ✅ CGT batch 2 smoke | C4 |
| **N5** | 完整 A/B: CGT 13 题 + Q8 Indexing indicator 实测 (Phase 1 carry-over); GEM 10 题 + 末尾召回 T-tail-1/2 (Phase 2 hard checkpoint D2) + 全域对比; 双 ab_reports | ✅ PASS 比 ≥ 90% | C5 |
| **N6** | Phase 3 reviewer (规则 D) + 汇总 carry-over 关闭 + 等用户 ack 进 Phase 4 | ✅ 进 Phase 4 | C6 |

**机械指令**: 每 node 结束时主 session 执行: (1) `_progress.json` 更新 (2) SYNC_BOARD 同步 (3) git commit (4) 汇报用户. 新 session 启动只需说 "开 Phase 3 Node X", 主 session 从 SYNC_BOARD + _progress.json resume.

**Node 间 context 隔离**: 每 node 的 subagent 上下文在本 session 内 ephemeral, node 产物全部落盘. 跨 session 不依赖 subagent 记忆.

---

## 变更日志

| 日期 | 动作 |
|------|------|
| 2026-04-20 | 看板建立 (空白 Phase 0 起点, 两平台 todo) |
| 2026-04-20 | Phase 0 两边 verifier CONDITIONAL_PASS (~97%), Rule E ack (CGT: Q1=C/Q2=C/Q5=A / GEM: Q3=C/Q4=A/Q5=A), Phase 0 → PASS, Phase 1 解锁 doing, 2 个 executor subagent 并行派发 |
| 2026-04-20 | Phase 1 ChatGPT writer Attempt 1 成功 (10 问 9 ANS + 1 PARTIAL, 10 PLAN 修订); Gemini writer Attempt 1 失败 (过早终止, 归档规则 B); Gemini writer Attempt 2 加强 prompt 成功 (3+Q4 全 ANS, 8 PLAN 修订); 2 个 verifier reviewer 双边 CONDITIONAL_PASS; Gemini C1 MEDIUM (profile 分享机制过时) 主 session 当场修复 (E/I/F section + 顶部状态 + J checkbox); Phase 1 → PASS, Phase 2 待用户 ack |
| 2026-04-20 | 用户 ack 进 Phase 2 + 关键澄清: Gemini "公开" = 分享链接给同事 (定向/内部传播), ChatGPT Q1=C "公开" = GPT Store 全网广播; 两份 progress.json 记录语义澄清 (publish_scope_semantics_clarification_2026-04-20 字段); 2 个 executor (model=opus) 并行派发写 PLAN.md |
| 2026-04-20 | Phase 2 PLAN writer 双边成功: ChatGPT 660 行/13 规则/33 Task/8 hard cp, Gemini 578 行/12 规则/18 Task/12 hard cp; verifier 双边 CONDITIONAL_PASS; ChatGPT 1 MEDIUM (§3.2 score 公式不一致 Task B1 前修) + 2 LOW (路径/标题); Gemini 2 LOW (B2/B3 口头澄清 + §7 10 题组成); Phase 2 → PASS, Phase 3 待用户 ack |
| 2026-04-20 | 用户 ack Phase 3 混合锁步方案 + 6-node 分块规划 (每 node 独立 commit + session 可切换); ChatGPT 2 LOW 主 session 修复 (PLAN §4 标题 A-H→A-G + Task D3 路径 stage_D→stage_4); 准备 C0 打包 commit (Phase 0-2 全部产出) 结束当前 session, 下 session 开 N1 脚本 |

---

*来源: Phase 6.5 Claude v2 单平台经验 (claude_projects/) + 2026-04-20 session 共识 (双平台并行锁步方案). 本看板是机械 gate, 不是计划书; 计划在各平台 `docs/PLAN.md`.*
