# Phase 6.5 Claude Projects v2 — 复盘 (RETROSPECTIVE_V2)

> 范围: Stage v2.0 setup → v2.6 terminal (2026-04-18 → 2026-04-20, commits `c7e558c` → `V6.4-done`)
> 产出: 19 个真实上传文件 (1,286,161 tokens, 32 实体含 meta / 1,336,360 tokens), 6 批 A/B 回归, 24/24 PASS
> 状态: v2.6 终态 PASS, 已进入 Phase H 收尾 (取代原计划 v2.5 终态, 因 2026-04-20 用户优先级重平衡触发 v2.6 追加批)

---

## 1. 保留下来的做法 (推广到其他项目)

| # | 做法 | 理由 |
|---|------|------|
| R1 | 5 批 + 1 重平衡批渐进上传, 每批 hard checkpoint A/B 回归 | RAG 衰减拐点可量化观察 (本次观察到的 0 衰减纪录是 capacity vs 质量曲线的关键数据点) |
| R2 | 规则 A/B/C/D 全程固化 (语义抽检 / 失败归档 / 写审分离 / Retro 强制) | v1 留下的四条规则在 v2 对抗了 G1 subdir 优先级反转被动暴露 — 规则 A 的抽样揪出模型覆盖与用户期望不一致 |
| R3 | 第三 lane 独立 reviewer (Cowork writer / 主控 writer / code-reviewer subagent) | v2.4 独立复核 7 维度 / v2.6 (V6.2) code-reviewer 7 checks PASS, 同一 session 自审被根本堵死 |
| R4 | 每批 build_v2_stage.py 强制打印 stage tokens + C12 gate + md5 幂等 | 把 "上传前需要 byte-exact 产物" 变成可 rc=0/非0 判定的机器检查 |
| R5 | subagent-driven + 预授权 + hard checkpoint 分层 | 批内执行 auto, 批间等用户 A/B ack; 全程 14 个 executor/reviewer 调用只卡在上传+回归点 |
| R6 | RAG 衰减曲线作为一等产物 (rag_decay_curve.md) | 数据点在设计阶段就要求 "每批必填", 否则 Phase 7 没 actionable 输入 |
| R7 | 失败归档不删 (stage_v2.1_t3_regression.md 全程保留) | v2.1 T3 ↓ 是唯一 regression 数据点, v2.3 发现 T3 跨批正向激活时这条 archive 直接就是对照 |
| R8 | subagent_prompts/ 全留 (14 份) | 下次如果需要 replay 批 5 或者做 prompt 变体实验, 直接复用, 不再重写 |

## 2. 必须补上的 (本次暴露的 v2 专属缺口)

| # | 缺口 | 本次表现 | 补法 |
|---|------|---------|------|
| G1 | **子目录优先级默认按"引用次数"计算, 与用户业务优先级不对齐** | v2.5 收尾前 F1/G1 打分 = 域引用次数 → quest (用户最不重要) 覆盖 55.8%, supp (用户第二重要) 覆盖 25%, core (用户最重要) 覆盖 53.7%; 用户 2026-04-20 要求重平衡才触发 v2.6 追加批 | PLAN §F1 应在打分阶段先问"用户业务优先级", 将优先级作为打分的**乘数**而非事后重平衡; 避免多跑一批 188,981 tokens 的重算成本 |
| G2 | **capacity token 预测偏差没做公式校准** | v2.6 预测 63-68%, 实测 77% (+9-14pp); 原因是 Claude Projects UI 的 token 统计含 UI 元数据/内部索引开销, 与本地 tiktoken 不一致 | Phase 7 RAG 若沿用本系统, 需先跑 calibration 实验 (空 Project 上传一个已知 N tokens 的文件测 Δcapacity), 反推 "UI token 放大系数" |
| G3 | **Indexing indicator 全程不可靠** | 所有 6 批上传后 UI indicator 持续显示 "Indexing" 但提问立即命中; v2.1 首次被 MCP 上传阻塞, 后续全用手工拖拽 | 不是我们可控缺口, 但要写进 Phase 7 handoff: "不要等 UI indicator, 直接试问" |
| G4 | **tail giant 阈值 500 terms 是经验值, 未做灵敏度扫描** | 6 giants (C65047/C67154/C85491/C85494/C120527/C120528) 全部 >558 terms, 刚好跨过 500 阈值; 如果调成 400/600 会不会更优未测 | Phase 7 如果要做类似 stub/inline 切分, 先做阈值扫描 (e.g. 300/500/700/1000 各跑一次 A/B) |
| G5 | **文件数爬升 11 → 19, 未实测对 RAG 召回速度影响** | 手感 v2.6 召回延迟 ~20-30s 与 v2.1 相当, 但无客观 metric (UI 无 latency 暴露) | Phase 7 若要定量, 需在 client 侧计时 (chrome-devtools MCP network timing) |

## 3. 关键决策复盘

### 3.1 Stage v2.1 T3 单点衰减 — 选择 continue (D1) 而非 rollback

- **情景**: chapters 全展开后 T3 (PC↔PP RELREC 4 方法) 从 v1 PASS → v2.1 ↓ (硬拒答)
- **reviewer 诊断**: design-intent (规则 A 副作用) — chapters 只展开章节 TOC, §6.3.5.9.3 narrative 不在, 边界模板正确触发
- **决策**: 用户 ack continue, 等 batch 2 (examples) 补齐
- **结果验证**: v2.2 未修 (仍缺 narrative) → v2.3 突破 (从 09 PC relrec 数据推导 4 粒度, 保边界诚实) → v2.4 质变 (显式 Method A/B/C/D + A-D 汇总矩阵)
- **教训**: 单点衰减不一定是"退步"的信号, **可能是"边界变严谨"的信号**; 跨批累积后 RAG 会自发修复. 决策前需区分 "硬退步" vs "边界变严". 失败归档 (规则 B) 让这条 trace 可重现.

### 3.2 v2.4 terminology 拆分 A+B+D (11a/11b/11c 三文件 vs 单文件 11_terminology_high.md)

- **起点**: F2 executor 初版单文件 423K tokens (+72K Related Domain per-term 重复)
- **用户介入 2026-04-19**: "token 多一点没关系", 接受 A+B+D 组合 (按 subdir 拆 + Related Domain 提 header + F1 ranking 在每 subdir 内保序)
- **结果**: 总 tokens 351,752 (-17% vs 423K 初版), 11b 单文件 256K tokens 是 v2 最大记录, 但 T1/T15/T3 零衰减证明未造成 RAG 稀释
- **教训**: "单文件越小越好"是幻觉; RAG 更在意**内部冗余度**而非文件数. 本决策是"中庸 50%"设计哲学的具体兑现.

### 3.3 v2.5 终态 → v2.6 追加批 (用户优先级重平衡)

- **情景**: v2.5 执行完 C12 PASS (1.14M tokens, 81.6% of 1.4M), 原计划进 Phase H 收尾
- **用户 2026-04-20 ack**: "子目录优先级 core > supp > quest 是工作语境, 非 SDTM 标准", 要求重平衡
- **决策**: 不回滚 v2.5, 追加 v2.6 tail batch (V6.1 打分 + V6.2 产物 + V6.3 build + V6.4 checkpoint), 对 core/supp 未覆盖的 209 个 codelist 做 tail-tier 压缩 (3-列表 / giants 走 Deferred stub)
- **结果验证**: v2.6 A/B 24/24 PASS (T1-T20 零衰减 + T21/T22 tail-tier PASS + T-core-reb/T-supp-reb 优先级验证 PASS), capacity 77%, core 99.3% / supp 100% / quest 55.8% 覆盖达成; long tail 302 codelist (296 quest + 6 giants) 明确归 Phase 7 RAG
- **教训**: 用户业务优先级必须在 PLAN §F1 即问, 不能等打分完成后才发现反转 (G1 缺口). 但本次追加批零衰减 + 0 LOW blocking + 1 LOW cosmetic 的质量证明**增量扩容不破坏稳态** — 这是 RAG 衰减曲线的反向正证 (1.14M → 1.29M +13% tokens, 零衰减).

### 3.4 6 tail giants → Deferred stub 而非 inline (TAIL_GIANT_TERM_THRESHOLD=500)

- **候选**: C65047 (2,536 terms LB Test Code) / C67154 (2,536 terms MS Test Name) / C85491 (1,639 terms) / C85494 (592) / C120527/C120528 (558 each)
- **决策**: 6 者均 ≥500 terms, 如果 inline 会立即挤占 >100K tokens, 且 99% 下游需求只查 1-2 个 term, 故走 1-行 stub (codelist 元信息 + "Deferred to Phase 7 RAG" 声明)
- **结果验证 (T22 PASS)**: Claude 精准识别 stub, 声明 "Project 内未完整列出所有 Term 值", 引用源文件 `knowledge_base/terminology/core/lb_part*.md` + NCI EVS Browser, **零臆造 term**
- **教训**: 知识库不必"越全越好", 对于 MedDRA-level 大表, stub + RAG 路径比 inline 更准确 (避免 RAG 被 tail 稀释); Phase 7 RAG 设计需把这 6 giants 作为 "必须索引" 的第一批.

### 3.5 Indexing indicator 不可靠 — 全程忽略, 靠"直接试问"判可用

- **情景**: 6 批上传后 UI 均显示 "Indexing" 持续数十分钟, 但每次上传后立即提问都能命中新内容
- **决策**: 从 v2.2 起不再等 indicator, Cowork handoff 明确写 "Indexing indicator 不 gating, 用提问命中判可用"
- **教训**: 不可控依赖要主动测 + 写进 handoff, 否则后续 session 会再被同样问题阻塞.

## 4. 可迁移规则 (评估是否新增到全局 CLAUDE.md)

本次**未新增**全局规则. 全局 CLAUDE.md 四条规则 (A 语义抽检 / B 失败归档 / C Retro 强制 / D 写审分离) 全部命中并生效:

- 规则 A: 每批 reviewer N=10 disjoint 样本 + 主控 N=5 样本, 共 20 codelist 交叉审计 — G2 发现 12b questionnaires +12.3% 超 soft target 但 in-spec
- 规则 B: `failures/stage_v2.1_t3_regression.md` 是唯一失败 archive, v2.3 修复时直接作为对照
- 规则 C: 本文件即 Rule C 产物
- 规则 D: Cowork (writer) + 主控 (writer) + code-reviewer subagent (reviewer) 三 lane 隔离, 本次 14 个 subagent 调用全部遵守

**候选新增规则** (建议写进本项目 CLAUDE.md 而非全局, 因场景专属):

- **规则 E (建议, 本项目范围)**: 用户业务优先级必须在 PLAN §打分阶段即确认, 不能等打分完成后重平衡. 触发: 本次 G1 缺口. 成本: 多跑一批 188K tokens ≈ 30 分钟 subagent + 60 分钟用户 A/B, 远大于提前问一句.

## 5. 工作量数据

| 指标 | 值 |
|------|---|
| 源 tokens (knowledge_base/ 全量) | ~2,527,153 (v1 baseline) |
| v1 baseline tokens (参照) | 192,036 (11 文件, capacity 12%) |
| v2 终态 tokens (real upload) | 1,286,161 (19 文件) — **+571%** vs v1 |
| v2 终态 tokens (incl meta) | 1,336,360 (32 实体) |
| Capacity 实测 | 77% (v2.6 终态) |
| v2 文件类型分布 | v2.1 全展开重建 v1 的 9 文件 (00-08, ch02 byte-exact expand) + 2 examples (09/10) + 3 terminology high (11a/b/c) + 3 terminology mid (12a/b/c) + 2 terminology tail (13a/13c, 13b by design 不存在) |
| 覆盖率 (用户优先级) | core 99.3% (146/147) / supp 100% (188/188) / quest 55.8% (374/670) |
| Long tail → Phase 7 RAG | 302 codelist (296 quest + 6 tail giants) |
| 脚本行数 | ~1,200 行 Python (scripts_v2/ 6 个脚本) |
| Subagent 调用 | 14 次 (executor 7 + reviewer 7) 记录在 subagent_prompts/ |
| 重试 (failures) | 1 个归档 (stage_v2.1_t3_regression.md) |
| Hard checkpoints (acked) | 4 已 ack (v2.1/v2.2/v2.3/v2.4, 见 _progress.json.checkpoints_acked); v2.6 终态 ack 在 Phase H4 追加 (v2.5 被 v2.6 接续, skipped) |
| A/B 测试题数 | 24 (T1-T22 + T-core-reb + T-supp-reb) |
| A/B 测试 PASS | 24/24 (100%) |
| 回归衰减 ↓ | 0 / 所有批 |
| 跨批正向激活数据点 | 1 (T3 RELREC 4 方法, v2.2 拒答 → v2.3 推导 → v2.4 显式) |
| Commits (Phase 6.5 v2) | 33 (`c7e558c` setup → `adaf3a8` V6.3; H1-H5 本 session 内 pending, 将在 H5 landing 后累计 ≥37) |
| 源文件污染 (knowledge_base/) | 0 (P5 强制只读, git status 全程 clean) |
| 壁钟时间 | ~3 天 (2026-04-18 → 2026-04-20), 跨多 session |

### 附: trace.jsonl 事件分布 (实测口径, 2026-04-20)

```
65 events total (trace.jsonl wc -l)
├── stage_done: 8 (v2.0 setup + v2.1 chapters + v2.2 examples_high + v2.3 examples_others
│                  + v2.4 terminology_high + v2.5 terminology_mid + v2.6 terminology_tail
│                  + 1 early pre-checkpoint stage_done for chapters)
├── step_done: 10 / step_start: 6 / task_start: 4 (细粒度 Step 编排事件)
├── checkpoint acked (合口径): 4 (stage_checkpoint_acked=1 + checkpoint_acked=1 + checkpoint_ack=2,
│                                与 _progress.json.checkpoints_acked 的 4 entries 一致)
├── executor/reviewer 派发事件 (合口径): 10
│      executor_dispatched=1 / executor_done=1 / executor_done_v1=1 / executor_done_v2=1
│      executor_resumed=1 / reviewer_dispatched=1 / reviewer_done=3 / main_audit_done=2
│      (实际 subagent 调用落盘在 subagent_prompts/ 14 份为准, trace 事件是派发/完成快照)
├── build/script events: build_script_patched=2 / main_ran_script=1 / f3_build_run=1
│                        / script_bug_fixed=1 / script_tail_tier_added=1
├── output artifact events: g1_done=1 / g2_output_written_progress_updated=1
│                           / g3_output_written_progress_updated=1
│                           / v6.3_output_written_progress_updated=1 / tail_list_generated=1
├── A/B & checkpoint events: ab_report_received=1 / cowork_ab_test_done=1
│                            / cross_audit_summary=1 / layer1_pass=1
├── user/consult events: user_consult=1 / spec_deviation_ack=1
└── phase_init=1 + main_review_done=1 + unknown=3
```

**口径说明**: 初版 retrospective 附表报 "subagent_spawned: 14 / reviewer_verdict: 7 / stage_done: 6"
与实际 trace.jsonl 事件名对不上 (evidence-freshness cosmetic 问题, Rule D reviewer 已揪出).
以上为对照 `evidence_v2/trace.jsonl` 实测重新统计的口径, **数字 source of truth 顺序**:
`evidence_v2/_progress.json` → `evidence_v2/trace.jsonl` → `evidence_v2/subagent_prompts/`.

---

## 6. 这次留下但不一定每次都做

- `rag_decay_curve.md` 7 数据点 (v1 baseline + v2.1/v2.2/v2.3/v2.4/v2.5/v2.6) + 3 段跨批观察 — 需要 "建立 RAG 质量 vs 规模曲线" 为目标的项目必留, 其他场景过度
- `evidence_v2/checkpoints/ckpt_v2.X.md` 逐批 — 本次只写了 ckpt_v2.1 (设计复盘), 后续批通过 _progress.json 的 checkpoints_acked 字段归档; 证明 hybrid (JSON + 文件) 够用
- `output_v1_baseline/` 永久 archive — v2 vs v1 的 A/B 能回头对比, 不然 "v1 192K 9 文件" 这个 anchor 点会随时间消失

---

## 7. 对后续项目的 actionable advice

1. **先问用户业务优先级**, 再打分 (G1 教训), 节省一批重算 ~1-2 天
2. **capacity 预测用 calibration 不用公式** (G2 教训), Phase 7 RAG 首次上传前做一次 known-N-tokens 实验
3. **RAG 衰减曲线必须在设计阶段就作为一等产物要求**, 否则会变"事后补数据"
4. **第三 lane 独立 reviewer 不可省** (规则 D), v2.4 / V6.2 两次都是独立 reviewer 7 checks 把 blocking 拦在 PR 之前
5. **Deferred stub 是 RAG 扩展的合法产物**, 不必强行 inline; T22 证明模型能正确使用 stub

---

*复盘人: 主控 (Claude Opus 4.7), 2026-04-20*
*下游文档: `output_v2/phase7_handoff.md` (本次复盘的 actionable insight 会落到该文件, Phase 7 可直接读)*
