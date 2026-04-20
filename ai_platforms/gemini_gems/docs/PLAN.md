# Gemini Gems — Phase 2 PLAN (v1)

> Phase: 2 · Tier 1-2 (本系列最轻量平台)
> Writer: oh-my-claudecode:executor (opus) subagent
> 最后更新: 2026-04-20
> 范本: [`../../_template/04_plan.md`](../../_template/04_plan.md) + [`../../_template/05_solution.md`](../../_template/05_solution.md)
> 锁步看板: [`../../SYNC_BOARD.md`](../../SYNC_BOARD.md) (与 ChatGPT GPTs 并行)

---

## §0 修订记录

| 版本 | 日期 | 修改人 | 变更 | 触发 |
|------|------|-------|------|------|
| v1 | 2026-04-20 | oh-my-claudecode:executor (opus) | 初版 (基于 Phase 1 PASS + Rule E ack + Q3 分享澄清) | Phase 2 启动, 用户 ack 进 Phase 2 |

**Phase 1 Carry-over 吸收状态**:
- LOW (F-1): 末尾召回量化 transfer_to_phase3 → 已内嵌 §1 P12 + §4 Phase D checkpoint
- C1 MEDIUM (profile E/I/F section 过时): 已在 Phase 1 收束时主 session 修复, 本 PLAN 基于新版 profile
- Phase 1 Q3 澄清: Gemini "公开" = 分享链接给同事 (定向/内部), 非 GPT Store 全网广播 → §4 Phase F 发布决策 + §7 A/B 矩阵不含陌生公开受众语气题

---

## §1 执行规则

### 1.1 全局规则 (继承 `~/.claude/CLAUDE.md`)

| # | 规则 | 适用 |
|---|------|------|
| A | 语义抽检: 压缩/改写 >50% 强制 N 样本独立抽检 | 每批 writer 完成后 (本平台单批, Phase B 合并后 N=5) |
| B | 失败归档: 任何 attempt 不删, `failures/stage_<N>_attempt_<M>.md` | 任何失败 |
| C | Retro 强制: Tier 2 收尾必写 RETROSPECTIVE.md | Phase G 收束 |
| D | 写审分离: Writer ≠ Reviewer (不同 subagent_type) | 每次派发 |

### 1.2 范本规则 P1-P10

| # | 规则 | 本平台具象化 |
|---|------|-------------|
| P1 | 量化 PASS 标准: `[Stage X.Y] <file>: <N> tokens (target ≤<X>K)` | 每合并文件产出时打印 token 数 (targets: 01~120K / 02~168K / 03~225K / 04~200K); 总计 target ≤800K (1M 窗口留 200K 响应余量) |
| P2 | 写/审分离执行态: 不同 subagent_type, 都可 opus | Writer = executor, Reviewer = code-reviewer/verifier; Phase B 合并脚本 / Phase D A/B 必须双 lane |
| P3 | 估算值前缀 `~`, 实测值不加 | manifest 中 "~713K" = 估算, 实测落盘后去掉 ~ |
| P4 | Checkpoint 级别: hard/soft/none, 不擅自连推 | 每 Task 明示 (见 §4) |
| P5 | 源文件只读: `knowledge_base/` 不 Edit/Write | 全程; 合并脚本只读源 |
| P6 | Subagent 上下文隔离: 每脚本独立 executor | merge_for_gemini.py 派独立 executor, 主控不读脚本源 |
| P7 | 进度持久化: 每 Step 完成立即更新 `_progress.json` | 每 Task 完成 writer/reviewer/checkpoint 状态入 L1 |
| P8 | (同 B) | — |
| P9 | (同 A) | — |
| P10 | A/B 衰减强制响应: ≥2 题停, ≥1 题写 regression evidence | 本平台单批, P10 适用于 Phase D 终态 A/B; 末尾召回 2 题独立 gate (见 P12) |

### 1.3 本平台独有 P11-P12

**P11 — 单批到位 (Single Batch Upload)**

- 1 批上传全部 3-5 合并文件, **不做渐进拐点测试**
- 依据: 1M 窗口官方 needle-in-haystack 100% recall @ 530K, >99.7% @ 1M (arxiv 2403.05530, Phase 1 Q1 确认)
- 估算 ~713K tokens (core 513K + terminology 高频 200K, Rule E Q4=A), 落在 100% recall 区
- 反模式: **不做** Claude v2 那种 5 批拐点建模; 源体量已知落在安全区, 一次到位
- **硬约束**: 若 Phase B 实测总 token > 900K, 触发降级决策 (回到 §8 R2), 考虑拆 terminology

**P12 — 末尾召回强验 (Tail Recall Hard Validation, Phase 1 F-1 carry-over 兑现)**

- **Phase D 终态 A/B 矩阵必含 2 道末尾召回精确 term 题** (hard checkpoint):
  - T-tail-1: 末尾 04_terminology_core.md 某非首段的 codelist 精确 Term (e.g. C66742 完整 Term 表, 或 AE 某 codelist Synonym)
  - T-tail-2: 同文件另一段非尾部非首部的 Term (验证"lost in the middle")
- **PASS 判据**: 2 题均 PASS (Rule E Q4=A terminology 注入可行的必要证据)
- **FAIL 响应**:
  - 1 题 FAIL: 记录 regression evidence, reviewer 归因, 用户决策 continue or 移动 terminology 块
  - 2 题均 FAIL: 立即停, 考虑把 terminology 关键块 (高频 codelist) 移到中段 or 拆分 04 为 04a/04b
- **来源**: Phase 1 Q1 数据区间 + Google 官方多针任务建议 + Chroma 2025 "context rot" 研究
- **transfer_to_phase3 闭环**: Phase 1 carry-over F-1 在本 PLAN §4 Phase D 显式 hard checkpoint 标注, 不再 partial 状态

### 1.4 Phase 1 Research "对 PLAN 的修订" 8 条吸收

| # | 原 profile 假设 | 调研后事实 | 本 PLAN 吸收 |
|---|----------------|-----------|-------------|
| 1 | E section "仅个人" | 2025-09 起支持链接/公开/Workspace | §4 Phase F 发布决策给出 "私有默认 + 可选分享" 分支; A/B 不含陌生受众语气 (Q3 澄清) |
| 2 | 公开发布=否 | 已支持 | 同上 |
| 3 | F-1 末尾 100-200K 衰减无来源 | 官方 99.7% @ 1M 单针 / 60% @ 100 针 / 社区 100-150K 代码任务降级 | P12 明示 hard checkpoint; §8 R1 持续监控 |
| 4 | 文件 3-5 合并, 硬限 10 | 10 文件硬限确认 | §2 设计 4 文件 + 1 spare 余量 |
| 5 | 单文件大小上限"数百 MB" | 100 MB per file 精确 | §2 单文件目标 <5MB, 不构成瓶颈 |
| 6 | pricing URL 待核 | AI Plans URL 给出 | §2 不涉及 PLAN, 仅记录 |
| 7 | 2M tokens API 层澄清 | Gems Web UI 以 1M 为标准 | §2 按 1M 规划, 不依赖 2M |
| 8 | Q4 API 复用 | Gems 与 Gemini API 不共享 Knowledge | §9 开放问题 Phase 7 独立路径 |

---

## §2 文件结构 Map

### 2.1 Create (本次新建)

```
ai_platforms/gemini_gems/dev/scripts/                       (目录)
├── merge_for_gemini.py                                     (单批合并脚本)
├── count_tokens.py                                         (复用 claude_projects v1)
└── validate_gemini.py                                      (产物校验)

ai_platforms/gemini_gems/current/                           (目录, 发布版)
├── uploads/                                                (4 合并文件)
│   ├── 01_core_reference.md        (~120K tokens, P0)      # chapters + model + 导航层
│   ├── 02_domain_specs.md          (~168K tokens, P0)      # 63 spec.md
│   ├── 03_domain_knowledge.md      (~225K tokens, P1)      # 63 assumptions + examples
│   └── 04_terminology_core.md      (~200K tokens, P2)      # 高频 codelist, Rule E Q4=A 注入, 末尾放置
├── system_prompt.md                                        (Gem Instructions)
├── upload_manifest.md                                      (文件清单 + token 实测)
├── UPLOAD_TUTORIAL.md                                      (10 章节用户教程)
└── README.md                                               (导航入口)

ai_platforms/gemini_gems/dev/evidence/                      (已建, Phase 0-1 沿用)
├── _progress.json                                          (已有, 滚动更新)
├── trace.jsonl                                             (append-only)
├── checkpoints/                                            (hard checkpoint 握手)
├── failures/                                               (规则 B 归档)
└── step_NN_audit.md                                        (规则 A 抽检产物, Phase B 后)

ai_platforms/gemini_gems/dev/ab_reports/                    (目录)
└── STAGE_FINAL_AB_REPORT.md                                (单批即终态)

ai_platforms/gemini_gems/dev/test_results.md                (A/B 实测结果)
ai_platforms/gemini_gems/docs/RETROSPECTIVE.md              (Phase G 产物, 规则 C)
ai_platforms/gemini_gems/docs/PLAN.md                       (本文件)
```

### 2.2 Modify (执行中滚动更新)

```
ai_platforms/gemini_gems/dev/evidence/_progress.json      (每 Task)
ai_platforms/gemini_gems/dev/evidence/trace.jsonl         (append-only)
ai_platforms/gemini_gems/current/system_prompt.md         (Phase C 单次)
ai_platforms/gemini_gems/current/upload_manifest.md       (Phase B 落盘)
ai_platforms/gemini_gems/dev/test_results.md              (Phase D A/B)
ai_platforms/gemini_gems/ROADMAP.md                       (Phase G 状态更新)
ai_platforms/gemini_gems/docs/platform_profile.md         (如有新发现补丁)
../SYNC_BOARD.md                                           (每 Phase 跨 gate)
../README.md                                               (Phase G 收束时)
/.work/MANIFEST.md                                         (Phase G)
/.work/meta/worklog.md                                     (Phase G)
/docs/PROGRESS.md                                          (Phase G)
/CLAUDE.md                                                 (Phase G Key Paths)
```

### 2.3 Read-only (强制禁写, P5)

```
knowledge_base/**                                          (源只读, P5 硬约束)
ai_platforms/_template/**                                  (范本不可污染)
ai_platforms/claude_projects/**                            (已完成, 冻结)
ai_platforms/chatgpt_gpt/**                                (锁步邻居, 本 PLAN 不写)
```

### 2.4 脚本职责边界 (P6 单一职责)

| 脚本 | 单一职责 | 输入 | 输出 |
|------|---------|------|------|
| count_tokens.py | 测 token (复用 claude_projects v1) | .md 文件/目录 | stdout: `<file>: <N> tokens` |
| merge_for_gemini.py | 按 4 桶合并源 → 4 合并文件 | `knowledge_base/**` | `current/uploads/0{1-4}_*.md` + 合并 manifest |
| validate_gemini.py | 产物校验 (段数 / md5 / 非空 / token 上限) | `current/uploads/` | rc=0/非0 + 报告 |

**位置策略嵌入 merge_for_gemini.py**:
- 01 (导航) 最早产出, 文件内顺序: chapters → model → ROUTING/INDEX
- 02 (spec) 按域字母序
- 03 (assumptions + examples) 按域字母序, assumptions 块在前
- 04 (terminology) **高频优先, 尾部留给最常查的 codelist** (recency bias 有利)
- 四文件上传顺序: 01 → 02 → 03 → 04 (Gem Knowledge 文件列表展示顺序影响上下文位置)

---

## §3 Rule E 打分公式

### 3.1 公式

```
score(item) = coverage_weight × priority_weight × position_fit
```

- `coverage_weight`: 域/章节覆盖率 (63 域 Q5=A 全量平权, 每域 weight=1.0; chapters/model 作为引导层 weight=1.2)
- `priority_weight`: 来自 Rule E ack (Q3=C 兼顾精确+全域, Q4=A terminology 高频注入, Q5=A 全域平权)
  - P0 (core + spec + 导航) = 3.0
  - P1 (domain_knowledge) = 2.0
  - P2 (terminology_core) = 1.5 (Q4=A 注入但体量上给予合理节制)
- `position_fit`: 文件在 Gem Knowledge 列表中的位置与内容性质的匹配度
  - 高频导航层前置 (01 position=0.9, 避 lost-in-the-middle)
  - 中段 spec/knowledge (02-03 position=0.7, 最危险区, 靠 query anchor 拉回)
  - 尾部 terminology (04 position=0.9, recency bias; 若 >250K 降至 0.6 触发 §8 R2)

### 3.2 与 Rule E ack 的对应

| Rule E ack | 公式中体现 | 本 PLAN 落地 |
|-----------|-----------|-------------|
| Q3=C (精确查询 + 全域对比兼顾) | coverage_weight 对导航层加成 1.2 (支撑全域对比) + spec/knowledge 全量 (支撑精确查询) | §4 Phase B 三文件全量产出 + §7 A/B 两类题型同等权重 (各 3-4 题) |
| Q4=A (terminology 高频段注入 ~713K) | priority_weight P2=1.5 + position_fit 0.9 (尾部) | §2 04_terminology_core.md ~200K 高频段, 尾部放置; P12 末尾召回 hard checkpoint 强验 |
| Q5=A (63 域全量平权) | coverage_weight 每域 1.0 | §4 Phase B 02/03 文件不减配低频域, 全量合并 |

### 3.3 Phase 1 carry-over 处置汇总

| carry-over | 级别 | 处置 | PLAN 位置 |
|-----------|------|------|----------|
| F-1: 末尾召回量化 transfer_to_phase3 | LOW | P12 hard checkpoint + §4 Phase D T-tail-1/2 + §8 R1 | §1.3 P12 + §4 Phase D + §8 |
| C1 MEDIUM: profile E/I/F 过时 | 已修复 (Phase 1 收束) | 本 PLAN 基于新版 profile, 无需再修 | §0 修订记录注明 |
| Q3 分享语义澄清: Gemini "公开" = 链接给同事 | (session 澄清) | §4 Phase F 发布决策 + §7 A/B 无陌生受众题 | §4 Phase F + §7 |

---

## §4 Phase A-G Task 分解 (Tier 1-2 轻量)

**Task 标注格式**: 内容 / checkpoint (hard/soft/none) / 依赖 / 产物 / 估计.

### Phase A: Setup (一次性, 3 Tasks)

#### A1: 初始化 current/ 目录骨架
- 内容: 创建 `current/uploads/`; 预留 README.md 占位
- checkpoint: none
- 依赖: 无
- 产物: 空目录 + README.md 骨架
- 估计: 5 min

#### A2: scripts/ 搭建 + 复用 count_tokens.py
- 内容: 创建 `dev/scripts/`; 从 `claude_projects/dev/scripts/` 复用 count_tokens.py (或 symlink)
- checkpoint: none (低风险)
- 依赖: A1
- 产物: `dev/scripts/count_tokens.py`
- 估计: 5 min

#### A3: 初始化 ab_reports/ 目录 + 补充 evidence 子目录
- 内容: 创建 `dev/ab_reports/`, 确认 `dev/evidence/{checkpoints,failures,subagent_prompts}/` 已存在
- checkpoint: none
- 依赖: 无
- 产物: 目录骨架
- 估计: 3 min

**Phase A 总 checkpoint 级别**: **none** (Setup 低风险, 全通过即进 Phase B)

---

### Phase B: 合并产出 3-5 主题文件 (单批核心)

#### B1: 设计 + 实现 merge_for_gemini.py (复用/改造 ChatGPT 脚本架构)
- 内容: executor subagent 写脚本; 实现 4 桶路由 (core_reference / domain_specs / domain_knowledge / terminology_core) + 按 token 预算切分 + 位置控制 (导航层前置, terminology 后置高频)
- checkpoint: **soft** (脚本逻辑合理性复核, 不含最终产物)
- 依赖: A2
- 产物: `dev/scripts/merge_for_gemini.py`
- 估计: 30-45 min (executor 写脚本 20 min + reviewer soft 15 min)
- P6 约束: 主控不读脚本源, 派独立 executor

#### B2: 产出 01_core_reference.md + 02_domain_specs.md
- 内容: 跑 merge_for_gemini.py --stage core+spec; 打印 token 数 (P1)
- checkpoint: **hard** (token 实测偏差 >15% 触发审查)
- 依赖: B1
- 产物: `current/uploads/01_core_reference.md` (~120K) + `02_domain_specs.md` (~168K); manifest 累加
- 估计: 15 min (脚本跑 5 min + 验证 10 min)

#### B3: 产出 03_domain_knowledge.md
- 内容: 跑 merge_for_gemini.py --stage knowledge; 打印 token 数
- checkpoint: **hard** (总累计 tokens 阶段校验; 若累计 >600K 考虑降级 04)
- 依赖: B2
- 产物: `03_domain_knowledge.md` (~225K); 累计 ~513K
- 估计: 15 min

#### B4: 产出 04_terminology_core.md (Rule E Q4=A 兑现)
- 内容: 跑 merge_for_gemini.py --stage terminology; 选高频 codelist inline; 位置尾部; 打印 token 数
- checkpoint: **hard** (总累计 ≤800K 验证 P11 约束; >900K 触发 §8 R2)
- 依赖: B3
- 产物: `04_terminology_core.md` (~200K); 累计 ~713K
- 估计: 20 min

#### B5: 合并产物规则 A 语义抽检 (N=5 样本)
- 内容: 主控读 5 个随机段 (每文件 1-2 段) 对比源, 验证合并忠实度 (压缩率预计 <50%, 但 Q4=A 有选择性注入, 启动抽检)
- checkpoint: **hard** (规则 A 触发条件: Q4=A 对 terminology 做选择性注入即为"改写 >50%")
- 依赖: B4
- 产物: `dev/evidence/step_B5_audit.md`
- 估计: 30 min

#### B6: validate_gemini.py 产物完整性校验
- 内容: executor 写 validate 脚本; 检查段数 / md5 稳定 / 无空文件 / 单文件 <5MB / 总 token ≤800K
- checkpoint: **soft**
- 依赖: B4
- 产物: `dev/scripts/validate_gemini.py`; rc=0 报告
- 估计: 20 min

**Phase B 总 checkpoint 级别**: **hard** (B2/B3/B4/B5 四个 hard, token 累计 + 规则 A 抽检)

---

### Phase C: Gem 创建 + Instructions + 单批上传

#### C1: 起草 Gem Custom Instructions (system_prompt.md)
- 内容: 按 `05_solution.md` System Prompt 骨架 + Rule E Q3=C 兼顾题型 + 边界诚实; **不含陌生公开受众语气** (Phase 1 Q3 澄清: 本平台分享 = 给同事)
- checkpoint: **hard** (Instructions 直接决定回答质量, 需 reviewer lane 复核, 规则 D)
- 依赖: B6
- 产物: `current/system_prompt.md`
- 估计: 30 min (writer 15 min + reviewer 15 min)

#### C2: 单批上传 4 文件到 Gem
- 内容: 用户手动拖拽 01-04 文件到 Gem Knowledge; 等待 Gem 状态就绪 (无 indexing 概念, 秒级)
- checkpoint: **hard** (用户操作确认 + 上传成功截图)
- 依赖: C1
- 产物: `dev/checkpoints/C2_upload_handshake.md` + 截图
- 估计: 5 min (上传) + 用户握手

#### C3: 响应时间 / truncate 烟雾测试
- 内容: 跑 2-3 个简单查询, 观察响应时间 + 首答完整性 (是否触 truncate)
- checkpoint: **soft**
- 依赖: C2
- 产物: `dev/test_results.md` 烟雾段
- 估计: 15 min

**Phase C 总 checkpoint 级别**: **hard** (C1/C2 两处 hard)

---

### Phase D: A/B 10 题矩阵 (终态单次, 含 P12 末尾召回 hard checkpoint)

#### D1: 跑 A/B 10 题 (精确 3-4 + 全域对比 3-4 + 末尾召回 2 + 边界 1-2)
- 内容: 按 §7 矩阵跑 10 题; 每题记录答案 + 命中域/文件引用 + PASS/FAIL 判定
- checkpoint: **hard** (终态回归, 规则 D 独立 reviewer lane)
- 依赖: C3
- 产物: `dev/ab_reports/STAGE_FINAL_AB_REPORT.md` + `dev/test_results.md` 10 题详表
- 估计: 60-90 min (跑题 45 min + 记录判定 30 min)

#### D2: P12 末尾召回 hard checkpoint 独立 gate
- 内容: D1 中 T-tail-1 + T-tail-2 独立 gate 判定 (2 题均 PASS 才放行)
- checkpoint: **hard** (P12 兑现 Phase 1 F-1 carry-over)
- 依赖: D1
- 产物: `dev/checkpoints/D2_tail_recall_gate.md`
- 估计: 10 min (判定归档)

#### D3: 独立 reviewer 复核 (规则 D)
- 内容: 派 code-reviewer / verifier subagent 复核 STAGE_FINAL_AB_REPORT.md; 判 PASS 比 ≥ 90% + 末尾召回 gate
- checkpoint: **hard**
- 依赖: D2
- 产物: `dev/evidence/phase_d_reviewer.md`
- 估计: 20 min

**Phase D 总 checkpoint 级别**: **hard** (D1/D2/D3 三处)

**规则 P10 触发**:
- 衰减 ≥2 题: 立即停, reviewer 归因, 用户决策 continue/rollback
- 衰减 ≥1 题: 写 regression evidence, reviewer 归因
- 末尾召回 2 题中任 1 FAIL: 见 §1.3 P12 FAIL 响应

---

### Phase E: Phase 3 carry-over 实测落地 (并入 Phase D, 不单独 Phase)

(本平台 Tier 轻, Phase 1 F-1 carry-over 的 Phase 3 hard checkpoint 已在 Phase D 兑现, 无独立 Phase E 执行. 预留 section 用于记录实测衰减 %.)

**实测数字预留栏** (Phase D 完成后回填):
- T-tail-1 位置 (文件 offset): `TBD`
- T-tail-2 位置 (文件 offset): `TBD`
- 实际命中 %: `TBD`
- 与 Phase 1 Q1 数据区间对比: `TBD`

---

### Phase F: 发布决策 (保守默认)

#### F1: 发布范围决策 (hard checkpoint, 用户拍板)
- 内容: 给用户两个选项:
  - 选项 A (保守默认, 推荐): 保持 Private, 仅个人使用
  - 选项 B (可选扩展): 分享链接给同事 (定向内部传播, Viewer 权限; **不追求** Store 式广播发现, 与 ChatGPT 公开路径语义不同)
- checkpoint: **hard** (用户拍板, 不代判)
- 依赖: D3 PASS
- 产物: `dev/checkpoints/F1_publish_decision.md`
- 估计: 用户决策时间 (非工时)

#### F2: (条件) 若选 B, 验证 Viewer vs Editor 权限设置
- 内容: 按 profile Q3 Q4 结论, 确认分享链接 Viewer 权限不泄露 Instructions 编辑; 确认 device 上传的 .md 满足分享条件
- checkpoint: **soft** (仅在选 B 时执行)
- 依赖: F1 (选项 B)
- 产物: 分享链接 + 权限验证记录
- 估计: 10 min

**Phase F 总 checkpoint 级别**: **hard** (F1)

---

### Phase G: 收束 (规则 C + reorg + 上游索引)

#### G1: RETROSPECTIVE.md (规则 C, 三段式)
- 内容: 保留做法 / 必须补上的缺口 / 关键决策复盘; 至少三段
- checkpoint: **hard** (规则 D 独立复核 PASS)
- 依赖: F1 PASS
- 产物: `docs/RETROSPECTIVE.md`
- 估计: 45 min

#### G2: UPLOAD_TUTORIAL.md (10 章节, 用户视角)
- 内容: 前置 / 建 Gem / Instructions / 上传 / Smoke Test / 回归 / 排错 / 升降级 / (可选) 分享 / 后续
- checkpoint: **soft**
- 依赖: G1
- 产物: `current/UPLOAD_TUTORIAL.md`
- 估计: 45 min

#### G3: ROADMAP 状态更新 + ai_platforms/README.md 总览
- 内容: ROADMAP "待开始" → "已完成" + 回填实际 capacity / A/B 数据 + 分享决策; `../README.md` 总览表格更新
- checkpoint: **soft**
- 依赖: G1
- 产物: `ROADMAP.md` + `../README.md`
- 估计: 20 min

#### G4: 上游索引 + CLAUDE.md Key Paths + MANIFEST + PROGRESS + SYNC_BOARD
- 内容: 按 SDTM-compare/CLAUDE.md Session Wrap-up 清单执行
- checkpoint: **soft**
- 依赖: G3
- 产物: `/CLAUDE.md` + `/.work/MANIFEST.md` + `/.work/meta/worklog.md` + `/docs/PROGRESS.md` + `../SYNC_BOARD.md`
- 估计: 15 min

#### G5: Commit + push
- 内容: 单 commit 描述性消息, push main
- checkpoint: **hard** (用户 ack)
- 依赖: G4
- 产物: git commit SHA
- 估计: 5 min

**Phase G 总 checkpoint 级别**: **hard** (G1/G5)

---

## §5 批次设计 (单批)

| 批次 | 范围 | 文件数 | 预计 tokens | A/B 题数 | Hard checkpoint |
|------|-----|-------|-----------|---------|----------------|
| 1 (单批即终态) | 全 (core + spec + knowledge + terminology 高频) | 4 | ~713K (≤800K target, 1M 窗口留 ~287K 响应余量) | 10 (终态一次跑) | Yes (含 P12 末尾召回 2 题 gate) |

**与 Claude Projects v2 对比**:
- Claude: 5+1 批, 12%→77% capacity, 渐进拐点建模
- Gemini: 1 批, ~71% 窗口 (713K/1M), 单次到位
- 差异来源: 官方 100% recall 至 530K + >99.7% @ 1M, 无需 calibration

**与 ChatGPT GPTs 对比**:
- ChatGPT: 2 批到位, 8-10 文件 (20 文件硬限下)
- Gemini: 1 批, 4 文件 (10 文件硬限下, 留 6 文件 spare)
- 差异来源: Gemini 无 RAG chunk, 文件数更少, 单文件更大

---

## §6 失败模式 → 归档 (规则 B)

### 6.1 profile F section 5 条 (含 Phase 1 修复的分享约束)

| # | 现象 | 缓解 |
|---|------|------|
| F-1 | 长上下文末尾召回衰减 | 关键内容前置; P12 末尾召回 hard checkpoint 强验 (2 题 gate) |
| F-2 | 上下文稀释, 具体问题命中率下降 | Instructions 强调"精确匹配源文件, 不做全扫" |
| F-3 | Gemini hallucinate 倾向 (相对 Claude) | A/B 含边界诚实至少 1-2 道; Instructions 强制引用源文件路径 |
| F-4 | 1M 窗口接近上限响应变慢 / truncate | Phase C3 烟雾测试; 实际使用 ~713K 留 287K 余量 |
| F-5 | 分享时 device/Drive 文件约束 (Phase 1 Q3 新增) | 本项目已用 device 上传 .md, 满足分享条件; Phase F2 若扩展分享时再验 |

### 6.2 Phase 1 & Phase 2 新增失败模式

| # | 现象 | 触发信号 | 缓解 |
|---|------|---------|------|
| F-6 | 多针任务降级 (Q1 官方承认 ~60% @ 100 针) | A/B 全域对比题 FAIL 比异常高 | 拆分 query, 单题不要求"所有 63 域完整列表" 类极端多针 |
| F-7 | Phase B 合并产物 token 超 900K | B4 打印超上限 | §8 R2: 拆 04_terminology_core.md, 保留顶部高频 100K |
| F-8 | Phase D 末尾召回 2 题均 FAIL | P12 gate | 移 terminology 高频块到 01 尾部 or 02 中段; 拆 04 为 04a/04b |

**归档约定**: 任何 attempt 失败 → `dev/evidence/failures/stage_<Phase>_<Task>_attempt_<N>.md`, 含输入 / 产物 / 技术判定 / 业务判定 / 下一 attempt 输入 (规则 B).

---

## §7 A/B 10 题清单 (初稿)

**设计原则** (Rule E 乘入 + Phase 1 Q3 澄清):
- Q3=C 兼顾精确查询 (类 Claude) + 全域对比 (Gemini 独家) → 两类题型各 3-4 题
- Q4=A terminology 末尾注入 → 必含 2 道末尾 codelist term 题 (P12 gate)
- **不含陌生公开受众语气题** (本平台分享语义 = 给同事, 非广播)
- 边界诚实 1-2 道 (继承 Claude/ChatGPT 共通)

### 7.1 精确查询类 (3-4 题, 类 Claude RAG 验证)

| ID | 维度 | 题目 | 预期命中 | PASS 判据 |
|----|------|------|---------|-----------|
| T1 | 变量定义精确 | "AE 域 AESER 变量的允许值是什么?" | 02_domain_specs.md (AE 段) | 答 Y/N 二值 + 引用 AE spec 路径 + 无臆造 |
| T2 | codelist 头部 Term | "C66742 (No Yes Response) 完整 Term 表" | 04_terminology_core.md 头部 | 全 Term 准确, 引用源路径 |
| T3 | 变量路由规则 | "如果某变量是 SUPP-- 补充数据, 应引用哪份 assumptions?" | 01 导航层 + 03 assumptions | 引用域特定 assumptions.md + SUPP 规则链 |
| T4 | chapter 查询 | "Section 4.1.5 关于 Timing Variables 的主要规则?" | 01_core_reference.md chapters 段 | 规则 3-5 条准确 + 引用 chapter 路径 |

### 7.2 全域对比类 (3-4 题, Gemini 独家能力)

| ID | 维度 | 题目 | 预期命中 | PASS 判据 |
|----|------|------|---------|-----------|
| T5 | 全域变量分布 | "所有域中哪些使用了 EPOCH 变量? 列出 Core 属性差异" | 全量 02 扫描 + 01 VAR_INDEX 辅助 | ≥80% 命中 EPOCH 使用域 (≥50 域/63); Core 属性差异分类合理 |
| T6 | 跨域 assumptions 搜索 | "哪些域的 assumptions 提到了 RELREC?" | 全量 03 assumptions 扫描 | 列出域名 + 引用 assumptions 具体段 |
| T7 | 模式识别 | "EX/EC, MB/MS, TU/TR, PC/PP 四对域的 examples section 有什么相似结构?" | 03 对应 4 对 examples | 至少识别 2 对共享结构 + 引用 examples 路径 |
| T8 | 大规模对比 | "比较 Events 类 7 个域 (AE/CE/DS/DV/HO/MH/SA) 的 assumptions 结构差异" | 全量 03 Events 域 | 识别 3+ 共性 + 2+ 差异点, 引用源路径 |

### 7.3 末尾召回 P12 gate 题 (2 题, hard checkpoint)

| ID | 维度 | 题目 | 预期命中 | PASS 判据 |
|----|------|------|---------|-----------|
| T-tail-1 | 末尾 codelist 精确 Term (尾段) | "04_terminology_core.md 最末一个 codelist 的所有 Term 和 Synonyms" | 04 文件尾部 ≤10% 位置 | 全 Term 准确, 无臆造, 无 "未收录" fallback |
| T-tail-2 | 非首非尾中段 codelist Term (Lost-in-Middle 验证) | "04_terminology_core.md 中段某 codelist (e.g. NY/NYC 问候类) 完整 Synonyms" | 04 文件 40-60% 位置 | 同上; 与 T-tail-1 对比判断 recency vs middle 差异 |

### 7.4 边界诚实类 (1-2 题, 继承)

| ID | 维度 | 题目 | 预期命中 | PASS 判据 |
|----|------|------|---------|-----------|
| T9 | 边界诚实 (未收录) | "AERELN codelist 所有 Synonyms?" (本 Gem 未 inline 此 codelist) | 无命中 → 应答 "未收录" + 引 NCI EVS Browser | 声明未收录, 给外部入口, **零臆造** Synonym |
| T10 (可选) | 边界诚实 (超范围) | "SDTM Protocol 设计建议?" (超出 SDTMIG 范围) | 无命中 | 声明超 SDTMIG 范围 + 建议查 Protocol 模板 |

### 7.5 A/B 矩阵 PASS 门槛

- 总 PASS 比 ≥ 90% (10 题中 ≥9 PASS)
- T-tail-1 + T-tail-2 独立 gate: 2 题均 PASS (P12, hard)
- 任 ≥2 题 FAIL → P10 触发停机
- 边界题 (T9/T10) 零臆造为硬门槛 (1 道臆造即 FAIL)

---

## §8 风险缓解

### R1: 末尾召回衰减 (Phase 1 F-1 carry-over)

- **触发信号**: T-tail-1 或 T-tail-2 FAIL
- **响应**:
  - 1 题 FAIL: regression evidence + reviewer 归因 + 用户决策 continue/调整
  - 2 题均 FAIL: 立即停, 移 terminology 高频块到 02 中段 or 拆 04
- **兜底**: P12 hard checkpoint 保证该风险不漏网

### R2: Terminology 超大导致 lost-in-middle 或总 token 超限

- **触发信号**: Phase B4 打印总 token >900K, 或 04 单文件 >250K
- **响应**:
  - 降 priority_weight P2 到 1.0, 重跑 merge 筛更高频 codelist
  - 或拆 04_terminology_core.md 为 04a (高频顶部 100K) + 04b (中频 100K)
  - 或移部分 terminology 到 Deferred stub (参考 05_solution.md stub 模式, 指向 NCI EVS)

### R3: 用户决策分享范围 (Phase F gate)

- **风险**: 用户可能要求超出当前保守默认的 Store 式广播
- **响应**:
  - 澄清本平台"公开" ≠ GPT Store 广播 (Phase 1 Q3 session 澄清已落地 _progress.json)
  - 若用户坚持广播发现, 记录为 Phase 7 或下个 Gem 部署的需求 (本项目不追求)
- **默认**: 保守私有 + 可选分享链接给同事

### R4: Gemini multi-needle 降级 (Q1 官方承认 ~60% @ 100 针)

- **触发信号**: T5/T6/T8 全域对比题 PASS 率异常低 (<50%)
- **响应**:
  - 若为个别题受影响: 拆 query (用户端拆 "分两步问: 先列域, 再对比 Core 属性")
  - 若系统性 FAIL: Instructions 加显式拆分指引 ("当用户问'所有域...'时, 建议拆两步回答")
  - 不视为合并失败, 视为使用模式调优

### R5: Indexing indicator 不适用 (Gemini 无 indexing 概念)

- Gemini Gems 无 RAG 无 indexing, 上传即全量注入
- **不构成风险**, 但 UPLOAD_TUTORIAL.md 需明示 (避免用户按 Claude/ChatGPT 经验等待 indexing)

---

## §9 开放问题

1. **Phase 7 Gemini API 镜像部署可行性**: Q4 结论 Gems Knowledge 与 Gemini API 文件不共享. 若 Phase 7 RAG/KG pipeline 需 Gemini 模型, 是独立路径 (API 自带 File API + context injection), 不能复用本 Gem 产物. 待 Phase 7 启动时独立设计.

2. **Terminology 切分粒度优化**: 当前 04 ~200K 高频段, 若 Phase D 末尾召回数字好 (≥95% recall @ tail), 未来可扩 04 至 300K; 若数字差 (<80%), 拆分 terminology 降密度. 需 Phase D 实测后反馈.

3. **Google AI Plus vs Pro Gems Knowledge 边界**: Phase 1 Q2 未决, 对本项目 (Pro 订阅) 无影响. 若未来用户要降级 Plus, 需重新确认可用性.

4. **陌生公开受众语气是否需要 (未来)**: 若用户改主意要 Store 式广播, 需补 A/B 新题型 (陌生用户语气 2 题), 本 PLAN 不覆盖.

5. **多针任务降级的精确 SDTM 阈值**: Q1 官方数字 "~60% @ 100 针" 是通用基准, SDTM 域多针 (e.g. "63 域全扫") 实际阈值未知. Phase D T5 是初步校准, 未来可扩展专项测试.

---

## §10 Phase 准入 gate 回顾 (self-check)

按 `SYNC_BOARD.md` Phase 2 → 3 Gate 细则:

| Gate 条件 | 本 PLAN 对应段 | 满足? |
|----------|---------------|-------|
| PLAN.md 含 P1-P10 范本规则 + 平台独有 P11+ | §1.2 (P1-P10) + §1.3 (P11-P12) | ✅ |
| Rule E: 用户业务优先级已乘入打分公式, 非事后重平衡 | §3 Rule E 打分公式 + §3.2 Q3=C/Q4=A/Q5=A 对应 | ✅ |
| 每 Task 明示 checkpoint 级别 (hard/soft/none) | §4 Phase A-G 每 Task 标 | ✅ |
| 批次粒度 + A/B 矩阵大小确定 | §5 批次表 + §7 A/B 10 题 | ✅ |
| Reviewer lane PASS (code-reviewer) | Phase 2 writer 产物待 reviewer subagent 独立复核 | ⏳ 待 reviewer |
| Phase 1 LOW carry-over 补齐: F-1 末尾召回 hard checkpoint 标注 | §1.3 P12 + §4 Phase D T-tail-1/2 + §8 R1 | ✅ |

---

*来源: 范本 `../../_template/04_plan.md` + `../../_template/05_solution.md` + Phase 0 profile + Phase 1 research 3+Q4 + Rule E ack + Phase 1 Q3 session 澄清 + claude_projects/docs/PLAN_V2.md 结构参考.*
