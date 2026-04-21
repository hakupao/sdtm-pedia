# Phase 2 Reviewer #4 终审报告 — NotebookLM PLAN.md

- 审核日期: 2026-04-21
- Reviewer #4: `pr-review-toolkit:code-reviewer` (opus) — Rule D 第 8 种 subagent_type
- 审核对象: `docs/PLAN.md` (951 行, 由 Writer #3 `oh-my-claudecode:planner` 657 行 + Writer #4 `feature-dev:code-architect` blueprint 主 session apply 到 951 行)
- 审核链: W#1 `general-purpose` → R#1 `oh-my-claudecode:verifier` → W#2 `oh-my-claudecode:executor` → R#2 `oh-my-claudecode:critic` → W#3 `oh-my-claudecode:planner` → R#3 `oh-my-claudecode:analyst` → W#4 `feature-dev:code-architect` → **R#4 `pr-review-toolkit:code-reviewer` (本文)**
- Rule D 合规: ✅ 8 subagent_type 全互斥, 无自审
- 审核手段: 8 文件事实核验 (PLAN / research / platform_profile / phase2_reviewer R3 / _spec 04/05/06 / 全局 + 项目 CLAUDE.md) + SDTM `Core=Req` 记录数 Grep 抽检核对 Writer #4 声称的 366 数字 + 6 维度逐行核对
- 独立性声明: 不重复 planner 设计逻辑 / 不重复 analyst Top 6 判定逻辑, 用 CLAUDE.md 对齐视角核 "每个必改是否真落地 + 有无新引入问题 + 最终是否达 Phase 3 启动门槛"

---

## 维度 1 — R3 Top 6 每项核对

### 1.1 I3 Mind Map / Study Guide 刷新挂 Task — ✅

- **R3 指控**: "全文无 Mind Map 刷新, R1 原 I3 未挂到任何 Task"
- **本次核对**:
  - PLAN §6 新增 **Task P3.9** (line 641-658): "I3 Mind Map / Study Guide 刷新节奏 + I4 长源衰减实测"
  - 4 场景完整: I3a (Notebook 1 增量) + I3b (Notebook 2 concept cluster 增量) + I3c (Study Guide 刷新) + I4 (长源深层衰减)
  - Checkpoint 级别: soft (line 652) ✅ 合理, Mind Map 非核心 A/B
  - 产物: `dev/evidence/mind_map_refresh_test.md` + 4 场景 PASS/FAIL + UI 截屏
  - §10 carry-over 表 (line 870) 亦新加一行 "I3 (Writer #4 新挂载)" 指向 P3.9 + §8.3 tutorial § 6 + §8.4 失败 #12
  - §2.1 evidence 清单 (line 152) 含 `mind_map_refresh_test.md`
- **结论**: **落地彻底**, R3 称的"遗漏"已消除, 且三处连锁 (P3.9 / carry-over / 失败应急) 一致

### 1.2 §6 每 Task 加 operations_count + wallclock_hours + prerequisite_tasks + parallel_with — ✅

- **R3 指控**: "每 Task 无 per-Task 操作次数 / 工时预估 / 并行化标注"
- **本次核对** (逐 Task):

| Task | operations_count | wallclock_hours | prerequisite_tasks | parallel_with | line |
|------|------------------|-----------------|---------------------|---------------|------|
| P3.0 | ✅ 2 次脚本 | ✅ 1-2h | ✅ Phase A A1/A3/A4/A5/A6 | ✅ "Phase 3 入口, 串行" | 498-501 |
| P3.1 | ✅ 最坏 293 / 最好 3-10 | ✅ 2-3h batch / 3-5h 无 / 5-10h 保险 | ✅ P3.0 | ✅ Phase A A2 (instructions_1 撰写) | 517-520 |
| P3.2 | ✅ ~20 | ✅ 2-3h | ✅ P3.1 | ✅ P3.4 instructions_2 校对 | 535-538 |
| P3.3 | ✅ ~27-35 | ✅ 2.5-4h / 保险 5-8h | ✅ P3.2 | ✅ P3.4 上传 (两 tab 交替) | 555-558 |
| P3.4 | ✅ ~95 最坏 | ✅ 8-12h / 保险 16-24h | ✅ P3.3 soft + A4 Req 审计 | ✅ P3.5 (有 caveat batch 耦合) | 574-578 |
| P3.5 | ✅ ~90 | ✅ 8-12h / 保险 tripled | ✅ P3.4 + A4 | ✅ P3.4 Audio 阶段 | 594-598 |
| P3.6 | ✅ ~5 | ✅ 0.5-1h | ✅ P3.4 + 测试 email | ✅ P3.5 Audio 阶段 | 614-617 |
| P3.7 | ✅ ~7-10 | ✅ 1-2h | ✅ P3.5 | ✅ P3.8 准备阶段 | 632-635 |
| P3.9 | ✅ ~18 | ✅ 1-2h | ✅ P3.3 + P3.4 | ✅ P3.6 / P3.7 | 653-656 |
| P3.8 | ✅ ~20 人工核对 | ✅ 3-5h / 保险 10h | ✅ P3.4/P3.5/P3.7/P3.9 全 | ✅ — (串行末尾) | 671-675 |

- **汇总表** (line 697-712): 10 Task 下界 29-47h / 保险 ~94h / 5-16 天换算, **显式标注 "Q2 不赶, 按标准 7 天; 允许 16 天兜底"** (line 714-718)
- **结论**: **全覆盖 + 超出 R3 要求** (加了 rate limit 预算行). 唯一瑕疵: P3.1 的 "最好 3-10 次" 含义是 "batch 拖文件夹 3 次成功, 加上 indexing 补救 7 次" 的合成估算, 表述略 terse 但不阻塞.

### 1.3 §3.4 "2 Req 改 0" + 5 处连锁 — ✅

- **R3 指控 (最 HIGH)**: "2 Core=Req 变量阈值无依据; SDTM expert 不接受 '容忍丢 1 个 Req'"
- **本次核对** (用户 Q1 ack "零丢失" 后全链重写):

| 连锁处 | 应改内容 | 落地 line | 核对 |
|-------|---------|----------|-----|
| §3.2.1 concept cluster 30 source 方案 | 从 "按 domain 挑" 改为 "按 concept cluster 重 bucket" + 30 source 具体表 | line 275-317 | ✅ 30 source 完整列 (Common Identifiers / DM+SC / Intervention / Events / Findings 3 档 / Trial Design / Relationships / IG ch3-8 / Terminology / Examples / Assumptions / VARIABLE_INDEX 5 拆 / Cross-domain / Bridge / Timing / Rules / **#29 req_variable_coverage 审计元 source**) |
| §3.3 Notebook 3 继承 | 自动继承 + 一致性快照 diff | line 343 | ✅ "自动继承 Q1=0 Req 变量零丢失红线 (内容一致), 无需独立审计, 但 Phase 3 Task P3.5 末尾加 'Notebook 3 source 一致性快照' 验 Notebook 2/3 内容未漂" |
| §3.4 矩阵阈值 | "2 → 0" | line 367 | ✅ "Notebook 1 vs 2 Req 变量覆盖 ... **丢失 >0 Core=Req 变量触发 FAIL** (Q1 红线, 零容忍)" |
| §5 动作 4 | 引用 Phase A A4 + Req 审计 hard gate | line 468-479 | ✅ 明确 "本动作已在 §2.5 Phase A A4 展开详化" + "筛选策略从 '按 domain 挑' 改为 '按 concept cluster 重 bucket' (Q1=0 技术必要)" + "Checkpoint 级别: hard (Req 变量零丢失红线, gate 到 §6 Task P3.4)" |
| §6 P3.4 审计子步 | 命令 + diff==0 判据 + 失败归档路径 | line 576 | ✅ "Task 完成前必跑 `source_mapping.py --audit-req-coverage --notebook 2`, `diff==0` 方 PASS; 若 diff > 0 归档 `failures/task_P3.4_attempt_N.md` + 立即修 source #29 (`req_variable_coverage.md`) 重上传" |
| §10 carry-over 表 Q1=0 行 | 5 处连锁列 | line 871 | ✅ "**Q1=0 红线连锁** (用户 2026-04-21 ack) ... Notebook 2/3 Req 变量零丢失, 无容差 | §3.2.1 concept cluster 30 source 方案 + §3.4 矩阵 '2→0' + §5 动作 4 / §2.5 Phase A A4 (审计脚本) + §6 Task P3.4 审计子步骤 + §2.1 新脚本 (5 处连锁)" |

- **结论**: **5 处连锁全落地**, 从阈值定义到 concept cluster bucket 到审计脚本到失败路径, 一致无断链. R3 最 HIGH 项彻底消化.

### 1.4 Project Success Criteria — ✅

- **R3 指控**: "§8 Phase 5 收束三件套写的是交付物清单, 但没有项目成功的 business definition"
- **本次核对**:
  - 执行摘要后 (line 21-34) 插入 "## Project Success Criteria" 独立段
  - 5 条 quality / completeness / template contribution / cross-platform / workflow replication 全列
  - 3 use-case success A/B/C (个人本人 30 秒 / 受邀同事 10 分钟 / 陌生 public ≤20% 差异) 全列, 和 R3 建议的 "30 秒 / 10 分钟" 数字精确对齐 (Success A 明示 "30 秒", Success B 明示 "≤10 分钟")
- **结论**: **落地正对应 R3 建议**, 可测量 (时间数字 + 差异率 + ≥13/15 PASS + diff==0)

### 1.5a Phase A Setup 独立段 — ✅

- **R3 指控**: "PLAN 直接跳到 §3 Multi-notebook 架构, 没有独立的 'Phase A Setup' 段"
- **本次核对**:
  - §2 后, §3 前 (line 204-233) 新增 **§2.5 Phase A Setup (先于 Phase 3, 独立段)** ✅
  - 6 子动作 A1-A6 完整 (line 210-215):
    - A1 Pre-upload audit (hard, 15 min)
    - A2 Chat mode 决策固化 (soft, 2-4h)
    - A3 Notebook 1 source 映射 (hard, 1-2h)
    - A4 Notebook 2/3 精选 + Req 审计 (hard, 4-6h)
    - **A5 (新) Web UI batch upload 调研** (hard, 1h)
    - **A6 (新) SDTM Req 变量 extraction** (hard, 1-2h)
  - 依赖图 (line 220-226): A3 依 A1 / A4 依 A6 ✅ 和 R3 建议一致
  - 调度 (line 227): Day 1 并行 A1+A2+A5+A6; Day 2 串行 A3→A4 ✅ 合理
  - gate 判据 (line 229-232): 6 evidence 落盘 + 5 hard ack + Req 零缺集断言 ✅
- **结论**: **超出 R3 最小需求** (R3 只要 3 个 A1/A2/A3, Writer #4 加到 6 个含 A5 batch + A6 Req extract 两个原本是 carry-over 的硬前置), Phase A 完成前 gate 机制明确

### 1.5b §8.4 失败应急集中表 — ✅

- **R3 指控**: "失败模式散落在 §3.3 / §6 每 Task / §8.3 / §1 P10, 没有一张集中表"
- **本次核对**:
  - §8.3 UPLOAD_TUTORIAL 后, §9 前 (line 804-827) 新增 **§8.4 失败应急集中表**
  - **16 行** 覆盖: Phase A A1/A4/A5 (3 行) + P3.1-P3.9 (9 行) + 全局 3 行 (checkpoint 延迟 / 源污染 / Rule D 自审违规)
  - 每行 5 要素完整: Task / 失败模式 / 触发信号 / 归档路径 / 响应 ✅
  - 末尾 (line 827) 明示 "归档不删 (规则 B)" 5 段式要求 ✅
- **结论**: **全覆盖且超 R3 期望** (16 行 vs R3 预期 ~10). 唯一边界: R3 §6.4 外部风险中 "NotebookLM UI 改版 / SDTM IG 升版 / Chat custom goals 功能调整" 3 外部风险**未入** §8.4, 这 3 条是 Phase 3 执行期外部触发的中低频事件, Writer #4 选择不入表属合理范围收窄 (但可在 Phase 5 retro 复盘)

### 1.6 §6 parallel_with — ✅ (合并到 1.2)

- 同 1.2 表格末列 ✅ 全 Task 标, 含 caveat (P3.4 ∥ P3.5 "若 A5 不支持 batch 严重耦合, 此时不推荐并行") ✅ 诚实边界

### R3 Top 6 改对率: **6/6 = 100%**

---

## 维度 2 — Q1=0 红线 5 处连锁 + SDTM 事实核验

### 5 处连锁核对

1. **§3.2.1 concept cluster 30 source 方案** (line 275-317): ✅
   - 30 source 表齐 (line 294-316)
   - #29 `req_variable_coverage.md` 审计元 source 存在 (line 315) ✅
   - 审计脚本引用 (line 320-325): `source_mapping.py --audit-req-coverage` + 5 步 diff 流程 + `len(diff) == 0` 判据 ✅

2. **§3.3 Notebook 3 自动继承 + diff 快照** (line 343, 355): ✅
   - "自动继承 Q1=0 Req 变量零丢失红线 (内容一致), 无需独立审计" ✅
   - "Phase 3 Task P3.5 末尾加 'Notebook 3 source 一致性快照'" ✅ 对应 P3.5 里 `diff current/uploads_invite/MANIFEST.md current/uploads_public/MANIFEST.md` 期望空 diff (line 596) ✅

3. **§3.4 矩阵 FAIL 阈值** (line 367): ✅
   - "Notebook 1 vs 2 Req 变量覆盖 ... **丢失 >0 Core=Req 变量触发 FAIL** (Q1 红线, 零容忍)" ✅
   - Notebook 1 vs 3 综合行 (line 370) 也引用 Notebook 2→3 继承 ✅

4. **§5 动作 4 引用 Phase A A4 + hard gate** (line 468-479): ✅
   - "本动作已在 §2.5 Phase A A4 展开详化, 本段保留作 §6 Task 向后兼容索引" ✅ (避免重复, 单源头)
   - Checkpoint 级别: hard (Req 变量零丢失红线, gate 到 §6 Task P3.4) ✅

5. **§6 P3.4 Req 审计子步** (line 576): ✅
   - 命令具体: `source_mapping.py --audit-req-coverage --notebook 2` ✅
   - `diff==0` 方 PASS ✅
   - 失败归档 + 立即修 source #29 重上传 ✅

6. **§10 carry-over 表 Q1=0 行** (line 871): ✅
   - 5 处连锁全列 (§3.2.1 / §3.4 / §5 动作 4 / §2.5 A4 / §6 P3.4) ✅ **+ §2.1 新脚本 (合计实 6 处)**

### SDTM 事实核验 (独立 Grep 抽检)

- Writer #4 声称: **63 domain × 3-9 Req = ~366 Req 记录 / 去重 ~100-120 独立**
- 独立 `Grep **Core:** Req knowledge_base/domains` 结果:
  - 63 个 spec.md 全部命中
  - **累计 366 Req 记录** ← 与 Writer #4 **精确匹配**, 非近似
  - per-domain 分布: 最低 RELSUB 3 / 最高 TD+IE 9 / 中位 6 ← 合 "3-9" 范围
- `knowledge_base/VARIABLE_INDEX.md` 通用变量段 (line 21-45) 抽检:
  - 24 个通用变量中, Core=Req 的 **9 个**: STUDYID (63 域) / DOMAIN (59 域) / USUBJID (55 域) / ETCD (3 域) / RDOMAIN (3 域) / IECAT (2 域) / IETEST (2 域) / IETESTCD (2 域) / MIDSTYPE (2 域) ← 严密对应 Writer #4 engrained 事实
  - 剩余域特定 Req: **366 - (63+59+55+3×3+2×4)** ≈ **366 - 147 ≈ 219 条跨域 Req 实例**; 再按每变量 "出现域数" 去重, 估 **独立 Req ~100-120** ← Writer #4 数字方向正确
- **事实核验判定**: ✅ **Writer #4 声称与事实 100% 方向一致**, 366 是硬数字精确匹配, 去重估 100-120 是合理范围

### Q1=0 5 处连锁分布: ✅ 全 PASS / ⚠️ 0 / ❌ 0

---

## 维度 3 — 回归审查 (新修订未破坏原结构)

### 3.1 结构完整性

- §0-§11 全在 (line 38 §0 修订记录 / line 82 §1 规则 P1-P12 / line 110 §2 / line 204 §2.5 / line 236 §3 / line 384 §4 / line 440 §5 / line 482 §6 / line 722 §7 / line 768 §8 / line 831 §9 / line 849 §10 / line 875 §11 / line 892 Cheatsheet) — 新增 §2.5 插入合理位置 ✅
- Writer #4 修正日志 (line 912-950) 作为 §0 修订记录补充, 未污染主体段落 ✅

### 3.2 术语一致性

- "Standard" (不是 "Free"): 全文一致 ✅ (Phase 1 Writer #2 修过, 本次未回退)
- "Pro tier" (不是 "Plus"): 全文一致 ✅
- "Chat custom goals" / "Custom mode" / "Learning Guide": §3 各 notebook 对应一致 ✅
- **Notebook 2 Chat mode**: §3.2 明写 Learning Guide (line 268) / §10 carry-over C2.4 (line 858) 呼应 "Notebook 2 Learning Guide" ✅

### 3.3 与 Phase 1 research.md 事实一致性

- 500K words/source: §1 P1 (line 93) 对齐 ✅
- Pro tier 四数字 (500/300/500/20): §0 engrained #2 (line 58) + §3.1 Notebook 1 (line 247) 对齐 ✅
- Chat custom goals 发布日期: research.md Q3 line 78 明 2025-10-29; PLAN §0 engrained #4 (line 60) 引 "2025-10-29 blog.google 发布" ✅ (R3 C2.10 建议 "UI 截屏防第三方误读" 被 I9 贯穿 P3.2/P3.4/P3.5 消化, line 860 引)
- Source 隔离 P12: research.md §11 line 314 / PLAN §1 P12 (line 104) / §6 P3.4/P3.5 标 "P12 再次独立上传" (line 566, 586) ✅
- Mode A 50-cap / Mode B UNVERIFIED: research.md Q7 / PLAN §3.2 (line 271) / §3.3 (line 354) / §6 P3.7 I8 实测 (line 622-637) ✅

### 3.4 表格格式合法性

- 抽检 3 复杂表格: §3.2.1 30 source 表 (line 294-316 管道对齐 ✅) / §6 工时汇总表 (line 699-711 ✅) / §8.4 失败应急 16 行 (line 809-825 ✅)
- 无格式崩塌

### 3.5 引用完整性 (`_spec/04_plan.md` 骨架 vs PLAN)

| `_spec/04_plan.md` §要 | PLAN 对应 | PASS? |
|----------------------|-----------|-------|
| §0 修订记录 | §0 (line 38) + Writer #4 日志 (line 912) | ✅ |
| §1 执行规则 P1-P10 + 规则 E | §1 P1-P12 + A/B/C/D/E (line 82) | ✅ (本平台扩 P11/P12) |
| §2 文件结构 map | §2 (line 110) + 2.1/2.2/2.3/2.4 分段 | ✅ |
| §3 Phase A: Setup | **§2.5 Phase A Setup** (line 204) | ✅ (R3 指出的缺失已补) |
| §4 Phase B-F: 批次 | §6 Phase 3 Task 分解 (line 482) | ✅ (本平台单批无多批) |
| §5 Phase G: 终态 A/B | §6 P3.8 跨 notebook 一致性 (line 662) | ✅ |
| §6 Phase H: 收束 | §8 Phase 5 收束三件套 (line 768) | ✅ |
| §7 Subagent 模板 (可选) | §7 Phase 4 审查设计 (line 722) | ✅ (轻版 7.1 subagent 候选表) |
| §8 失败应急 (可选) | **§8.4 失败应急集中表** (line 804) | ✅ (R3 指出的缺失已补) |

### 3.6 可能引入的新问题 (回归扫描)

1. **§5 动作 4 vs §2.5 A4 双源重复风险**: Writer #4 选择 §5 动作 4 保留作 "向后兼容索引" 指向 §2.5 A4. 现状可接受 (避免冗余), 但如果 Phase 3 执行者只读 §5 跳过 §2.5, 可能错过 A6 (extract_req_vars.py) 前置. **缓解**: §5 动作 4 line 470 明写 "本动作已在 **§2.5 Phase A A4** 展开详化", 提示跳转; §6 P3.0 的 `prerequisite_tasks` 写 "Phase A A1 + A3 + A4 + A5 + A6 全部 PASS" (line 500) 作 gate. 风险可控. ⚠️ **LOW 级非阻塞**
2. **§3.2.1 30 source 表的 ≤30 与 Pro tier 30 × 500K = 15M cap 的 words 估算** (line 317 "总字数估 ~550K words"): 此处是**文件数压缩 ~90% (293→30), 内容字数压缩 ~82% (~550K vs ~3M)** — §3.4 line 373 已明示修正, 和原 "压缩率 90%" 命名错位 (R3 维度 4(b)) 已纠偏. ✅
3. **P3.9 和 P3.8 编号倒置** (line 641 P3.9 出现在 line 662 P3.8 之前): Task P3.9 物理位置在 P3.8 之前, **编号不连续但逻辑合理** (P3.9 soft checkpoint, P3.8 hard 且依赖前一切 Task). §6 checkpoint 汇总表 (line 683-693) 和工时汇总表 (line 700-710) 均按 P3.0-P3.9 顺序列, P3.9 行列在 P3.8 行上方. **瑕疵**: P3.9 若改名 P3.7b 或 P3.8 之前的新 P3.8 更符合编号单调递增, 但不阻塞. ⚠️ **COSMETIC 非阻塞**

### 维度 3 判定: ✅ 无回归, 2 条 LOW/COSMETIC 不阻塞

---

## 维度 4 — 新增内容可用性 (Project Success / Phase A / §8.4)

### 4.1 Project Success Criteria 可测量性

- **Success A**: "30 秒内用 Notebook 1 回答 smoke v2 Q1-Q3" — ✅ **可测** (秒表计时 + SMOKE_QUESTIONS_V2.md 3 题)
- **Success B**: "5 位受邀同事 onboard 后 ≤10 分钟独立查任 core domain spec + 理解 Learning Guide Socratic 引导" — ✅ **可测** (需招募 5 人, 实测点)
- **Success C**: "陌生访客打开 Notebook 3 能读懂 smoke v2 Q1-Q3 且回答不含臆造事实 (对比 Notebook 2 差异 ≤20%)" — ⚠️ "陌生访客" 在 Phase 3 内难找真实陌生人, 但 "第二 Gmail 模拟" 是 fallback (§6 P3.7 已用此模式); 差异 ≤20% 阈值的度量口径需在 Phase 4 §7.2 cross_platform_compare 中细化 (如按题差异还是语义差异). **LOW** 非阻塞.
- 5 条 criteria 整体 business-oriented 合理, 超过 "技术 PASS 13/15" 层面

### 4.2 Phase A Setup 6 子动作工时合理性

- **A1 Pre-upload audit 15 分钟**: `find knowledge_base -name '*.md' -exec wc -w {} \;` + Python sort Top 5 + 写 evidence md — ✅ 合理 (SDTM 293 md, `wc -w` 极快)
- **A2 Chat mode 固化 2-4h**: 3 instructions_N.md 各 ≤10K char, 撰写 + 审稿 — ✅ 合理
- **A3 Notebook 1 source 映射 1-2h**: 293 md → 293 source (一对一) 或合并决策, 写 MANIFEST.md — ✅ 合理
- **A4 Notebook 2/3 精选 + Req 审计 4-6h**: 30 source bucket 设计 + `cluster_req_variables.py` 运行 + diff 审计 — ✅ 合理 (脚本逻辑非平凡, 需跨 63 spec.md 解析)
- **A5 Web UI batch 调研 1h**: 手测三场景 + UI 截屏 — ✅ 合理 (非自动化)
- **A6 Req extract 1-2h**: 解析 `VARIABLE_INDEX.md` (线性查找 `Req` 列, 已 Grep 核实 177 个 Req 匹配 in line 2005 行文件) + 63 spec.md 抽 — ✅ 合理 (VARIABLE_INDEX 格式结构化, parse 不难)
- **依赖图**: A3 依 A1 (outlier 决定是否拆 293) ✅ / A4 依 A6 (没 Req 全集无法审) ✅ / A5/A6 独立并行 ✅
- **调度 Day 1 A1+A2+A5+A6 / Day 2 A3→A4**: 逻辑正确

### 4.3 §8.4 失败应急表 可用性

- 16 行全含 "触发信号 + 归档路径 + fallback 响应" 三要素 ✅
- **#11 (Mode B 50-cap I8 FAIL)**: 关键 fallback 路径 (workflow_replication) 明确 ✅ — Scope B 广泛分享崩塌的应急链条清晰
- **#15 源文件污染**: `git checkout knowledge_base/` 立即回滚 ✅ — 规则 P5 强保障
- **#16 Rule D 自审违规**: "立即停, 换第 N+1 种 subagent_type 重跑 reviewer 轮" ✅ — 本 Phase 2 恰好跑到第 8 种, 如果 Phase 3 还要开两个 reviewer (§7.1), 候选表 (line 737) 足够
- 遗漏:
  - R3 §6.4 "Google tier 改价/改限额" / "NotebookLM UI 改版" / "SDTM IG v3.5/v3.6 发版" 三条外部风险**未列入**集中表. Writer #4 选择收窄到 Phase 3 内部失败模式, R3 原话 "建议 §8 加 §8.4 外部风险 + 失效监控子节" 未完全消化. **MEDIUM**: 建议 Phase 3 执行过程中若观察到外部环境变化, 立刻 carry-over 到 Phase 5 retrospective. 本 PLAN 内不阻塞, 因 3 条均属 Phase 3 执行期低概率事件.

### 维度 4 判定: ✅ 可用 (1 个 MEDIUM 建议 + 1 个 LOW 建议, 非阻塞)

---

## 维度 5 — Carry-over 17 条消化率

依 R3 原 17 条 (11 真消化 + 5 口头 + 1 遗漏 I3) 逐条再核, 评 Writer #4 后新的消化率:

| # | Carry-over | R3 原评 | 本次 (R4) 核对 | 结论 |
|---|------------|--------|--------------|-----|
| C2.9 | Mode B cap UNVERIFIED | ✅ | §3.3 line 354 UNVERIFIED 标 + §6 P3.7 line 622-629 I8 实测 + §8.3 UPLOAD_TUTORIAL § 10 fallback + §8.4 #11 | ✅ 真消化 |
| C2.10 | Chat mode 双日期 (Learning Guide 2025-09 vs Chat custom goals 2025-10-29) | 口头 | §0 engrained #4 (line 60) 引 "2025-10-29 blog.google 发布"; 未双列两日期; 但 §10 carry-over (line 854) 明写 "Learning Guide 2025-09-23 XDA vs Chat custom goals 2025-10-29 blog.google"; I9 贯穿 P3.2/P3.4/P3.5 (line 860) | ✅ 真消化 (升级, §10 line 854 双日期已列) |
| R1.1 (C2.5) | Pre-upload audit `wc -w` | ✅ | §5 动作 1 (line 442-450) + §6 Task P3.0 + §2.5 A1 + §8.4 #1 | ✅ 真消化 |
| R1.2 (C2.4) | Chat mode 默认 Custom | ✅ | §3.1 Custom (line 248) + §3.2 Learning Guide (line 268, 分化超出"默认") + §3.3 Custom public (line 345) + §10 line 858 | ✅ 真消化 (分化设计) |
| R1.3 (C2.2+) | Scope B personal Gmail | ✅ | §0 engrained #6 (line 62) + §3.2 Mode A 50 (line 271) + §3.3 Mode B (line 349) + §10 line 856 | ✅ 真消化 |
| R1.4 | 50 users invite-only | ✅ | §3.2 (line 266) + §6 P3.7 | ✅ 真消化 |
| R1.5 | 双 notebook 架构 Scope B | ✅ | §3 全段 (Notebook 2 + 3 分别设计) | ✅ 真消化 |
| C2.3 | 容量表四档 Pro 高亮 | 口头 | §0 engrained #2 (line 58) 只列 Pro 四数字, 未重复四档全表 (引 research.md Q2). Writer #4 未进一步补全 | ⚠️ 口头带过 (可接受, 单引用 research.md Q2 不冗余) |
| C2.4 | Chat mode 三档决策格 | ✅ | 同 R1.2 (分化到三 notebook) + §5 动作 2 (line 452) | ✅ 真消化 |
| C2.6 | Phase 3 I1-I9 每 item pass 判据 | 部分 | 逐条核 (见下表) — Writer #4 补了 I3 和 I4 | ⚠️ → ✅ 升级 (从部分升全覆盖) |
| C2.7 | Source 严格隔离 | ✅ | §1 P12 (line 104) + §3.3 (line 343) + §6 P3.4/P3.5 标 (line 566, 586) + §10 line 861 | ✅ 真消化 |
| C2.8 | A/B 15 题矩阵 | ✅ | §4 全节 (line 384-437) + §6 P3.2-P3.5 | ✅ 真消化 |
| I1 | Indexing 三场景 | ✅ (PDF 范围收窄) | §6 P3.1 line 509 + indexing smoke test 子动作; PDF 场景 N/A (SDTM 无 PDF 源) 已隐式合理 | ✅ 真消化 |
| I2 | re-index 增量 vs 全量 | 口头 | §6 P3.7 末尾 (line 637) "I2 re-index (可选, 若 Phase 3 内有时间)" — 仍 optional | ⚠️ 口头带过 (Writer #4 未升级为必做, R3 建议升级为必做未实现) |
| I3 | Mind Map / Study Guide 刷新节奏 | ❌ 遗漏 | **§6 新 Task P3.9** 4 场景 (I3a/b/c + I4) + §10 carry-over 行 + §8.3 § 6 + §8.4 #12 | ✅ 真消化 (从遗漏升级到独立 Task) |
| I4 | Audio 双语 (英→中) / Mind Map 长源衰减 | ✅ (Audio) / 未挂 (Mind Map) | Audio 双语 §4.2 P2 (line 410) + PASS 判据 "≥80% 术语准确"; Mind Map 长源 §6 P3.9 I4 (line 649) "末尾 20% 至少 1 节点" | ✅ 真消化 (Writer #4 拆分 I4 两面都挂 Task) |
| I5 | 公开链接访客回写 owner chat | 口头 | §6 P3.7 末尾 (line 637) "I5 (访客问答是否回写 owner chat history, 用第二账号测试)" — 仍无 PASS 判据细化 | ⚠️ 口头带过 (Writer #4 未升级) |
| I6 | 单次 chat 最大输入长度 | 口头 | §6 P3.8 (line 673) "50K / 200K / 500K words 三级用 Notebook 1 chat 提问, 记最大输入上限" — 三级量级显式列出 | ✅ 真消化 (升级, 量级显式 3 级) |
| I7 | Audio hallucination 三子类 | 口头 | §6 P3.3 line 553-554 仅列 "事实错误数" 整体判据, 未分 "跨 source / 长 source / interactive" 三子类 | ⚠️ 口头带过 (Writer #4 未升级, 但 §4.2 P1 判据 "0-1 事实错误 = PASS" 实操可行) |
| I8 | Mode B owner 50-cap | ✅ | §6 P3.7 (line 622-629) 3 步骤 (a 实际 cap / b UI 字段 / c 文档 re-survey) + Checkpoint hard + fallback 路径 (workflow_replication) + §8.4 #11 | ✅ 真消化 |
| I9 | Chat mode UI 截屏 | 口头 | §10 line 860 "I9 chat mode UI 截屏 贯穿 P3.2/P3.4/P3.5"; §6 P3.2 line 531 "Chat mode = Custom 已配置 (UI 截图)"; P3.4/P3.5 行文内未再重复 UI 截屏指令 | ⚠️ 口头带过 (贯穿关键词但 P3.4/P3.5 无 explicit 子步) |

### 消化率汇总

| 类别 | R3 原评 | R4 再核 | Δ |
|------|--------|---------|---|
| ✅ 真消化 | 11/17 (65%) | **13/17 (76%)** | +2 (C2.10 补双日期; I3 从遗漏升级; I6 升级; I4 Mind Map 长源升级) |
| ⚠️ 口头带过 | 5/17 (29%) | **4/17 (24%)** | -1 (I3 已消化) |
| ❌ 遗漏 | 1/17 (6%) | **0/17 (0%)** | -1 (I3 已消化) |

**Writer #4 消化成绩**: 从 65% → **76%**, 主要提升在 I3 (遗漏消除) + I4 Mind Map (碎片合并) + I6 (三档量级显式) + C2.10 (双日期已列); 剩 4 条口头 (C2.3 / I2 / I5 / I7 / I9) 属 Phase 3 执行时 on-the-fly 判据, R3 曾评 "不值得再一轮" (R3 line 408-411 同意降级接受), R4 同意此边界.

### 维度 5 判定: ✅ 13/17 (76%) 接近期望 "15+", 剩 4 条非阻塞 carry-over

---

## 维度 6 — CLAUDE.md 对齐 (pr-review-toolkit 本职)

### 6.1 全局 Rule A-E 显式引用

- PLAN §1 规则表 (line 86-104): A/B/C/D/E 全列且本平台特化明确 ✅
- 规则 E 在 §1 末尾 (line 106) 明示 "本次已 ack 2026-04-21 + 4 项 ack 内容 + 引用 `_progress.json rule_E_user_priority`" ✅ **零回头问用户**

### 6.2 每 Task 有 Rule D checkpoint

- §6 Task P3.0-P3.9 全标 hard/soft (line 497, 516, 534, 554, 573, 593, 613, 631, 652) ✅
- §6 Task Checkpoint 汇总表 (line 683-693) 明列 6 hard + 4 soft ✅ 符合 "v1 G4 教训显式写出" 原则
- §2.5 Phase A A1-A6 全标 hard/soft (line 210-215) ✅

### 6.3 每 Task 失败归档路径 (Rule B)

- §6 Task P3.0-P3.9 全含 `dev/evidence/failures/task_<N>_attempt_<X>.md` ✅
- §8.4 失败应急表 16 行全含归档路径 ✅
- §1 P8 引用规则 B (line 100) ✅

### 6.4 Tier 分级 (项目 CLAUDE.md Tier 2)

- PLAN header (line 7) 明写 "项目 Tier: **Tier 2** (5-15 step, 半天-1 天级体量, 走 workflow-tier2 模板 — PLAN.md / _progress.json / evidence/ / failures/ / RETROSPECTIVE.md 齐全)" ✅
- Phase A 6 + Phase 3 10 Tasks = 16 Tasks, 刚好在 Tier 2 (5-15) 上沿或刚破 Tier 3 门槛 (>15). Writer #4 选择维持 Tier 2 归类合理 (Task 颗粒度非 step 颗粒度)
- Tier 2 必备 5 产物齐: PLAN.md / _progress.json (§2.1 line 146) / evidence/ (§2.1) / failures/ (§2.1 line 155) / RETROSPECTIVE.md (§8.1 line 770) ✅

### 6.5 项目 CLAUDE.md Key Paths 更新

- 项目 CLAUDE.md 本 PLAN **不强制**更新 (Phase 5 收束时做)
- §2.2 Modify 段 (line 175) 列 "CLAUDE.md (Phase 5 收束时, Key Paths 新增 notebooklm 入口)" ✅ 已声明延后处理

### 6.6 项目 CLAUDE.md Phase 6.5 双平台锁步 N/A

- 项目 CLAUDE.md 规定 "**双平台锁步**" 只针对 ChatGPT GPTs + Gemini Gems; **NotebookLM 不在双平台锁步内** (属第三条路径, `ai_platforms/SYNC_BOARD.md` 不涉 NotebookLM 平台)
- PLAN §2.3 Read-only 段 (line 187) 明写 "ai_platforms/SYNC_BOARD.md (本平台**不**参与 2-way 锁步, 只在 Phase 5 加一行状态)" ✅ 边界清晰

### 6.7 SubAgent prompt 归档 (项目 P6)

- §1 P6 (line 98) + §2.1 `dev/evidence/subagent_prompts/` (line 154) ✅

### 维度 6 判定: ✅ 7/7 CLAUDE.md 对齐点全 PASS

---

## 最终判定

- **判定**: **PASS**
- **置信度**: **91%** (对比 R1 78% → R2 85% → R3 82% → **R4 91%**)
- **Rule D 合规**: ✅ 第 8 种 subagent_type, 前 7 种全异
- **Top N 必改**: 无阻塞项
- **放行建议**: **直接 commit PLAN.md, 进 Phase 3 Task P3.0** — 无需再一轮 Writer #5

### 置信度 91% 构成 (独立于 R3 82%)

**+ 加分项** (为何 +9% vs R3):
1. R3 Top 6 6/6 落地 = +4% (R3 预期仅 "必做 3 + 应做 3", Writer #4 100% 消化含 "应做")
2. Q1=0 5 处连锁全一致 + SDTM 事实核验 366 精确匹配 = +3% (R3 未独立核实 SDTM 数字, R4 Grep 366 对齐)
3. Carry-over 消化率 65% → 76% (+11pp) = +2%

**- 扣分项** (为何非 100%):
1. §5 动作 4 vs §2.5 A4 双源跳转 LOW 风险 = -2% (读者可能漏 §2.5, 但 gate 机制防护)
2. P3.9 编号 ∈ P3.8 之前 COSMETIC = -1% (非功能问题)
3. I2 / I5 / I7 / C2.3 / I9 4-5 条 carry-over 仍口头带过 = -3% (R3 已同意降级接受, 但未清 0)
4. R3 §6.4 外部风险 (Google tier 改价 / UI 改版 / SDTM IG 升版) 未入 §8.4 集中表 = -2% (Phase 5 retro 可补)

### 为何 PASS 而非 CONDITIONAL_PASS

Writer #4 已清除 R3 所有 MAJOR 级遗漏 (I3) + HIGH 级业务红线 (Req 零丢失) + 5 条 MEDIUM 级需求层缺失. 剩余 4-5 条 LOW/COSMETIC 均 R3 自评 "不值得再一轮" 或 R4 独立判为 Phase 3 执行/Phase 5 retro 可处理, **不构成 Phase 3 启动的业务/技术阻塞**.

**8 链 Rule D 累计审核足够深度**: 前 7 种 subagent_type 各自独立复核一轮, R4 作为 pr-review-toolkit:code-reviewer 以 CLAUDE.md 对齐视角 + SDTM 事实独立核验视角终审, 未发现新 MAJOR/HIGH 问题. 继续开 W#5 × R#5 轮 **边际收益 < 成本** (Writer #4 已 exhaust R3 6 必改, 下一轮优化点属 Phase 3 执行时才能发现).

### 为何不 FAIL

所有 Phase 3 启动 gate 条件具备:
- 3 notebook 架构设计完整
- Q1=0 审计脚本链条自洽 (extract_req_vars.py → cluster_req_variables.py → source_mapping.py --audit-req-coverage → diff==0 判据 → 失败归档)
- Phase A 6 子动作 + 依赖图 + gate 完整
- 45 题次 A/B 矩阵 + per-notebook 13/15 阈值
- 16 行 §8.4 失败应急
- 6 hard checkpoint + 4 soft
- 10 Task 工时汇总 29-94h / 5-16 天换算
- 5 条 Project Success Criteria + 3 use-case A/B/C

---

## Carry-over 到 Phase 3

继承 R3 I10/I11/I12 外加 R4 新增:

- **I10** (继承 R3): Phase A A5 Web UI batch upload 能力调研 — 决定 P3.1 操作成本; 本 R4 再核 Writer #4 已用 A5 独立动作消化, carry-over 关 ✅
- **I11** (继承 R3): P3.2 "Chat custom goals 当前 UI 命名/入口截屏" — 本 R4 再核 I9 贯穿 P3.2/P3.4/P3.5 (line 860) 部分消化; **建议 Phase 3 执行时显式在 P3.2 Task 产物清单加 `dev/evidence/chat_custom_goals_ui_snapshot_<date>.md`** 一行 (Writer #4 未加, 非阻塞)
- **I12** (继承 R3): Phase 3 Day 1 结束后 "tier re-check" 访 `notebooklm.google/plans` — 本 R4 再核未入 §8.4 / §6; **建议 Phase 3 P3.0 末尾加一检查项** (非阻塞)
- **I13** (R4 新): §5 动作 4 vs §2.5 A4 双源关系在 Phase 3 执行记要 follow-up ack 一次 — 防 executor 只读 §5 跳过 A6
- **I14** (R4 新): P3.9 和 P3.8 编号倒置, 建议 Phase 5 reorg 时统一 rename

## Carry-over 到 Phase 4

- Phase 4 §7.2 cross_platform_compare 的 "差异 ≤20%" 口径在 Phase 4 执行前需用户 ack 度量方式 (题差异 vs 语义差异)
- Phase 4 两 reviewer subagent_type (§7.1 候选表 line 737) 已列 6+ 种避免前 7 种, 供选

## Carry-over 到 Phase 5 retro

- 4-5 条口头 carry-over (C2.3 / I2 / I5 / I7 / I9 部分) 的 Phase 3 执行实际消化情况**在 RETROSPECTIVE R 段或 G 段复盘**, 决定是否纳入 `_template/` 补丁 (或改为 `_spec/` 未来强制子步)
- R3 §6.4 外部风险 (Google tier 变 / NotebookLM UI 改 / SDTM IG v3.5) 3 条如果 Phase 3 期间观察到, 归档到 RETROSPECTIVE D 段

---

## Rule D 合规声明 (8 subagent_type 完全互斥)

| lane | subagent_type | 产物 | Rule D 合规? |
|------|---------------|------|------|
| Writer #1 research | `general-purpose` | research.md v1 | ✅ |
| Reviewer #1 research | `oh-my-claudecode:verifier` | phase1_reviewer.md (78%) | ✅ 异 W#1 |
| Writer #2 research | `oh-my-claudecode:executor` | research.md 修正版 + 日志 | ✅ 异 W#1/R#1 |
| Reviewer #2 research | `oh-my-claudecode:critic` | phase1_reviewer2.md (85%) | ✅ 异 W#1/R#1/W#2 |
| Writer #3 PLAN | `oh-my-claudecode:planner` | PLAN.md (657 行 v1) | ✅ 异全部前 4 |
| Reviewer #3 PLAN | `oh-my-claudecode:analyst` | phase2_reviewer.md (82% CONDITIONAL) | ✅ 异全部前 5 |
| Writer #4 PLAN | `feature-dev:code-architect` | PLAN.md blueprint → 主 session apply 到 951 行 | ✅ 异全部前 6 |
| **Reviewer #4 PLAN (本文)** | **`pr-review-toolkit:code-reviewer`** | phase2_reviewer2.md (91% PASS) | ✅ **8 种完全互斥** |

**8 种 subagent_type 完全互斥**, Rule D 严格合规, 0 self-review, 0 session 自审. 本 R4 审核独立完成, 基于事实 + CLAUDE.md 对齐 + SDTM 领域数据 Grep 核实.

---

*本次 Reviewer #4 审核独立完成, 产物仅本文件 `phase2_reviewer2.md`. 未动 PLAN.md / research.md / phase1_reviewer*.md / phase2_reviewer.md / platform_profile.md / _progress.json / _spec/ / 其他平台 / SYNC_BOARD / 项目 CLAUDE.md / ~/.claude/. 主 session 决定: **接受 PASS 91%, 直接 commit PLAN.md 进 Phase 3 Task P3.0 (Phase A Setup 优先, 6 子动作 Day 1 并行 A1+A2+A5+A6 / Day 2 A3→A4)**.*
