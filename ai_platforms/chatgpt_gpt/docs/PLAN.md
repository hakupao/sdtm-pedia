# ChatGPT GPTs — Phase 2 PLAN (v1)

> Phase: 2 (策略 + PLAN) · Tier 2
> Writer: oh-my-claudecode:executor (opus) subagent
> 承接: Phase 0 PASS (97%) + Phase 1 CONDITIONAL_PASS (10/10 问覆盖 + 10 条 PLAN 修订 + 1 MEDIUM carry-over)
> Rule E ack: Q1=C (GPT Store 全网公开) · Q2=C (混合受众) · Q5=A (63 域全量平权)
> 锁步: 与 `gemini_gems/` Phase 2 PLAN 独立并行, cross-reference 不互写
> 最后更新: 2026-04-20

---

## §0 修订记录

每次修改追加一行, 不覆盖.

| 版本 | 日期 | 修改人 | 变更 | 触发 |
|------|------|-------|------|------|
| v1 | 2026-04-20 | executor (opus) | 初版 (基于 Phase 1 research + Rule E ack + Phase 1 MEDIUM carry-over) | Phase 2 doing, 用户 ack 已到位 |
| v1.1 | 2026-04-20 | 主 session (修 Phase 2 reviewer MEDIUM) | §3.1 公式从"四因子乘法"改为"核心(priority×coverage)+audience_bonus+novelty_bonus"加法结构; §3.2 表格重算; floor 规则保留但语义聚焦 coverage 降级兜底 | Phase 3 Node 1 启动前, 修 reviewer 指出的数学不一致 (原 2.4 vs 乘法 0.12, 差 20x) |
| v1.2 | 2026-04-20 | 主 session (修 Phase 3 Node 1 reviewer 文档同步 carry-over) | §2.4 行 1 `VAR_INDEX.md` → `VARIABLE_INDEX.md` (对齐 knowledge_base/ 实名); §2.5 "合并配置 YAML" → "Python dataclass 硬编码" (对齐脚本实现, Rule A 直白可审); §4 Task B1 产物 `score_phase2.md` → `score_phase3.md` (对齐脚本实现, Phase 3 Node 1 产物本应 phase3 语义) | Phase 3 Node 1 reviewer CONDITIONAL_PASS 的 PLAN 文档同步 carry-over (非脚本 bug, 仅文字) |

---

## §1 执行规则 (P1-P13 + Rule E)

继承全局 `~/.claude/CLAUDE.md` 规则 A/B/C/D, 本范本新增 Rule E, 本平台在范本 P1-P10 之上再叠加 P11-P13.

### 1.1 范本规则 P1-P10 (来自 `_template/04_plan.md`)

| # | 规则 | 本平台具象化 |
|---|------|------------|
| P1 | 量化 PASS: 每 Step 打印 `[Stage X.Y] <file>: <N> tokens (target ≤<X>K)` | 每批合并后跑 `count_tokens.py`, 产物 ≤ 单文件建议 < 500 KB (约 300K tokens) 以控制 chunk 数量 (Q2 800/400 chunk 参数派生) |
| P2 | 写/审分离执行态: executor ≠ reviewer (不同 subagent_type) | 本 PLAN 就是例证: writer=executor(opus), reviewer=verifier(独立 subagent); 后续每 Task 遵循 |
| P3 | AI 估算值前缀 `~`, 实测值不加 | `upload_manifest.md` 第一列 `token 估算` 全部 `~`, 第二列 `token 实测` 去 `~` |
| P4 | 人工抽查 checkpoint: hard/soft/none 明示, 不擅自连推 | 本 PLAN §4 每 Task 标明 checkpoint 级别 |
| P5 | 源文件只读: `knowledge_base/` 禁止 Edit/Write | 合并脚本输出到 `chatgpt_gpt/current/uploads/`, 不回写 |
| P6 | Subagent 上下文隔离: 每脚本独立 executor, 主控不读脚本源 | `dev/scripts/merge_for_chatgpt.py` 由 executor subagent 独立写; 主控只看产物 + manifest |
| P7 | 进度持久化: 每 Step 完成立即更新 `_progress.json` | Phase 3 每批更新, Phase 2 本文件完成后 `2_plan.status = PASS` 由主控写 |
| P8 | (同规则 B, 见全局) | 失败归档 `dev/evidence/failures/stage_<N>_attempt_<M>.md` |
| P9 | (同规则 A, 见全局) | 压缩/改写 >50% 触发 N 样本抽检, N=**5** (本平台 Tier 2 取 5, 见 §3 Rule A 触发) |
| P10 | A/B 衰减强制响应: 衰减 ≥2 题立即停, ≥1 题写 regression evidence + reviewer 归因 | 本平台 A/B 10-15 题, 衰减阈值与 Claude v2 一致 |

### 1.2 本平台独有规则 P11-P13 (ChatGPT 硬约束)

| # | 规则 | 依据 |
|---|------|------|
| **P11** | **合并粒度硬限**: 最终上传文件数 ≤ 20 (File Search 硬限, Q5 跨套餐一致). 本 PLAN 规划 8-10 合并文件 (留 10-12 spare) | Phase 1 Q5: 20 文件硬限 Plus/Team/Enterprise 一致 |
| **P12** | **溯源标注强制**: 每合并段起始加 `<!-- source: <原路径> -->`. 因 chunker 800 tokens 无法跨 heading, 溯源保证模型引用时可反查源文件 | Phase 1 Q2: chunk 800/400 固定不可调 |
| **P13** | **TableAware 分段**: md-heading 边界保护表格, 不在 table row 内切. 单表不跨 heading (避免 chunk 边界落入表格中间) | Phase 1 Q2 + profile F1 失败模式 (表格被 chunker 切断) |

### 1.3 Rule E 用户业务优先级 (非协商, 已 ack)

| Q | 选项 | 本平台语义 | 对 PLAN 影响 |
|---|------|-----------|-------------|
| Q1 | **C** (GPT Store 全网公开) | 任何人可搜索/使用, 非定向分享 (与 Gemini "链接给同事" 不同) | A/B 矩阵必含陌生公开受众语气题 (§7 新增 2 题) |
| Q2 | **C** (混合受众: novice + expert) | 需降新手门槛 + 对专家边界诚实 | 4 个 Conversation Starter 全部使用 (Q7 上限 4, 完全匹配); Instructions 语气双轨 |
| Q5 | **A** (63 域全量平权) | 不偏倚高频域, 源数据均衡 | 合并文件按"域 × 属性"矩阵组织, 不以频次裁剪; 打分公式覆盖权重优先 |

### 1.4 Phase 1 MEDIUM carry-over 显式处置

**carry-over**: Instructions "8,000 字符" source URL 缺失, 且 tokens vs chars 精度差 4x (8K tokens ≈ 32K chars; 8K chars ≈ 2K tokens).

**本 PLAN 的处置**:
1. **预算按"字符"计 (更保守假设)**: System Prompt 目标 ≤ 7,500 字符 (留 500 字符 buffer, 即使官方是字符, 仍安全; 若官方是 tokens 则更宽松).
2. **来源标注**: §3 Rule E 打分公式 + §4 Task C1 均标注 "来源待补 — 见 research.md 缺口 1, Phase 3 实测或 Phase 2 补齐官方 URL".
3. **Phase 3 实测 fallback**: 若 Phase 3 上传发现 Instructions 长度实测 ≠ 7.5K 字符预算, 立即回 §4 Task C1 重估, 触发 soft checkpoint.
4. **不阻塞**: reviewer verdict CONDITIONAL_PASS 明确说明此项可 Phase 2 并行修复, 不阻塞 Phase 2 启动.

### 1.5 Phase 1 其他 carry-over 登记

- **PARTIAL → Phase 3 (Q8 Indexing indicator 实测)**: 转 §4 Task E1, hard checkpoint (上传后实际问答验证, 不接受仅 UI 状态).
- **Hybrid search 权重 (未决 #2)**: 转 §4 Task D (A/B 矩阵设计), 加入"精确变量名 vs 语义描述" 对比题.

---

## §2 文件结构 Map

### 2.1 Create (本次新建)

```
ai_platforms/chatgpt_gpt/
├── docs/
│   └── PLAN.md                                  ← 本文件 (v1)
├── dev/
│   ├── scripts/
│   │   ├── count_tokens.py                      (复用/symlink from claude_projects v1)
│   │   ├── score_chatgpt_priority.py            (Rule E 打分)
│   │   ├── merge_for_chatgpt.py                 (主合并 + P12 溯源 + P13 TableAware)
│   │   └── validate_chatgpt_stage.py            (产物校验)
│   ├── evidence/
│   │   ├── _progress.json                        ✅ (已存, Phase 2 每 Step 更新)
│   │   ├── phase2_reviewer.md                    (本 PLAN 的独立 reviewer verdict)
│   │   ├── subagent_prompts/                     (本 PLAN writer prompt 已入)
│   │   ├── failures/                             (规则 B 预留)
│   │   └── checkpoints/                          (hard ack 握手 markdown)
│   ├── ab_reports/
│   │   ├── STAGE_BATCH1_AB_REPORT.md             (Phase 3 批 1)
│   │   ├── STAGE_BATCH2_AB_REPORT.md             (Phase 3 批 2)
│   │   └── STAGE_FINAL_AB_REPORT.md              (Phase 4 终态回归)
│   └── test_results.md                           (Phase 3 累积 A/B 记录)
├── current/
│   ├── uploads/
│   │   ├── 01_navigation.md                      (批 1)
│   │   ├── 02_chapters_all.md                    (批 1)
│   │   ├── 03_model_all.md                       (批 1)
│   │   ├── 04_domain_specs_all.md                (批 1)
│   │   ├── 05_domain_assumptions_all.md          (批 2)
│   │   ├── 06_domain_examples_all.md             (批 2)
│   │   ├── 07_terminology_core.md                (批 2)
│   │   ├── 08_terminology_questionnaires.md      (批 2, 可能拆 2 文件)
│   │   └── 09_terminology_supplementary.md       (批 2)
│   ├── system_prompt.md                           (Instructions 全文, ≤ 7500 字符)
│   ├── upload_manifest.md                         (文件清单 + token 预算)
│   ├── UPLOAD_TUTORIAL.md                         (Phase 5 产出)
│   └── README.md                                  (入口导航)
└── docs/RETROSPECTIVE.md                          (Phase 5 规则 C 产出)
```

### 2.2 Modify (执行中滚动)

```
ai_platforms/chatgpt_gpt/dev/evidence/_progress.json       (每 Step)
ai_platforms/chatgpt_gpt/current/system_prompt.md          (批次间迭代)
ai_platforms/chatgpt_gpt/current/upload_manifest.md        (每批累计)
ai_platforms/chatgpt_gpt/dev/test_results.md               (每批 A/B)
ai_platforms/SYNC_BOARD.md                                 (gate 跨越时)
.work/MANIFEST.md                                          (Phase 5 收尾)
.work/meta/worklog.md                                      (Phase 5 收尾)
docs/PROGRESS.md                                           (Phase 5 收尾)
CLAUDE.md                                                  (Phase 5 Key Paths)
```

### 2.3 Read-only (强制禁写)

```
knowledge_base/**                                          (P5)
ai_platforms/_template/**                                  (范本不可污染)
ai_platforms/claude_projects/archive/**                    (v1 冻结)
ai_platforms/gemini_gems/**                                (本 PLAN 不侵入)
```

### 2.4 合并文件清单 (P0-P2 优先级 + 溯源规则)

| # | 目标文件 | 合并源 | 估算大小 | 优先级 | 批次 | P12 溯源范围 |
|---|---------|-------|---------:|:-----:|:----:|-------------|
| 01 | `01_navigation.md` | ROUTING.md + INDEX.md + VARIABLE_INDEX.md | ~159 KB | P0 | 1 | 3 段源注释 |
| 02 | `02_chapters_all.md` | chapters/ 6 文件 | ~246 KB | P0 | 1 | 6 段源注释 |
| 03 | `03_model_all.md` | model/ 6 文件 | ~70 KB | P0 | 1 | 6 段源注释 |
| 04 | `04_domain_specs_all.md` | 63 domains/*/spec.md | ~672 KB | P0 | 1 | 63 段源注释 |
| 05 | `05_domain_assumptions_all.md` | 63 domains/*/assumptions.md | ~240 KB | P1 | 2 | 63 段源注释 |
| 06 | `06_domain_examples_all.md` | 63 domains/*/examples.md | ~661 KB | P1 | 2 | 63 段源注释 |
| 07 | `07_terminology_core.md` | terminology/core/ | ~3.2 MB | P2 | 2 | N 段源注释 (按子文件) |
| 08 | `08_terminology_questionnaires.md` | terminology/questionnaires/ | ~3.8 MB | P2 | 2 | N 段 (若 >500 KB 可能拆 08a/08b) |
| 09 | `09_terminology_supplementary.md` | terminology/supplementary/ | ~0.6 MB | P2 | 2 | N 段源注释 |

**合并数**: 9 (留 11 spare, 远 ≤ 20 硬限, P11 合规).

**估算总量**: ~10 MB md text ≈ ~2.5M tokens 原文 (远超 top-K=20 × 800 = 16K tokens 单次注入, 但这是 RAG 检索池, 非一次性注入).

**存储上限检查**: ~10 MB ≪ 10 GB/user (Q9 答案), 不触限.

### 2.5 脚本职责边界 (单一职责 P6)

| 脚本 | 单一职责 | 输入 | 输出 |
|------|---------|------|------|
| `count_tokens.py` | 测 token (复用 claude_projects v1) | .md 文件/目录 | stdout: `<file>: <N> tokens` |
| `score_chatgpt_priority.py` | Rule E 打分公式 (见 §3) | 源文件列表 + Rule E 参数 | stdout: ranked list with score |
| `merge_for_chatgpt.py` | 合并源 → 产物 (P12 + P13) | 源 + **Python dataclass 硬编码合并配置** (v1.2 对齐脚本实现; 原拟 YAML, 改 dataclass 直白可审 + 减 PyYAML 依赖, 见 §0 v1.2) | `current/uploads/*.md` + manifest fragment |
| `validate_chatgpt_stage.py` | 产物校验 (md5 / 段数 / P12 溯源覆盖率 / P13 表格完整) | `current/uploads/*.md` | rc=0 + 校验报告 |

---

## §3 Rule E 打分公式 (强制, 在 §2.4 优先级表与 §5 批次设计前乘入)

### 3.1 公式 (v1.1 加法结构)

```
score(file) = (priority_weight × coverage_weight) + audience_bonus + novelty_bonus

其中:
- priority_weight × coverage_weight = 核心覆盖分 (主项, 体现 P0/P1/P2 骨架 + Q5=A 全量约束)
- coverage_weight: 域覆盖完整度 (Rule E Q5=A 约束)
    - 63 域全量 = 1.0
    - 缺 1-2 域 (如合并失败) = 0.7 (减分)
    - 缺 > 5 域 = 0.3 (触发 Task A2 failure)
- priority_weight: P0=3.0 / P1=1.5 / P2=1.0
    - P0 = 核心 spec 结构 (navigation + chapters + model + domain_specs)
    - P1 = 辅助推理 (assumptions + examples)
    - P2 = 高频查表 (terminology)
- audience_bonus: Rule E Q2=C 混合受众加成 (加法, 非乘数)
    - 新手友好 (含基础导航/定义/示例) +0.2
    - 仅专家级 (深层 assumptions) +0.0
- novelty_bonus: Rule E Q1=C 公开广播加成 (加法, 非乘数)
    - 陌生公开受众命中题相关条目 +0.2 (见 §7 公开受众语气题)
    - 仅内部术语查询 +0.0
```

**为什么是加法 (不是乘法)**: audience/novelty `+0.2` 是 "小幅加成" 语义; 若当乘数 × 0.2 会把主项近乎清零, × 1.2 又算不出 v1 表格里的 2.4. v1 表格数字 (2.4 / 1.2 / 1.8 ...) 本就非乘法产物, 存在数学不一致 (Phase 2 reviewer MEDIUM). v1.1 显式声明加法, 公式与数字对齐, score 脚本可以机械实现.

### 3.2 打分结果 (v1.1 重算, Phase 2 预估, Phase 3 实测复核)

| # | 文件 | coverage | priority | 核心 (pri×cov) | audience | novelty | **score** | 批次 |
|---|------|:-------:|:-------:|:-------:|:-------:|:-------:|:-----:|:----:|
| 01 | navigation.md | 1.0 | 3.0 | 3.0 | +0.2 | +0.2 | **3.4** | 1 |
| 02 | chapters_all.md | 1.0 | 3.0 | 3.0 | +0.2 | +0.2 | **3.4** | 1 |
| 03 | model_all.md | 1.0 | 3.0 | 3.0 | +0.2 | +0.0 | **3.2** | 1 |
| 04 | domain_specs_all.md | 1.0 | 3.0 | 3.0 | +0.0 | +0.2 | **3.2** | 1 |
| 05 | assumptions_all.md | 1.0 | 1.5 | 1.5 | +0.0 | +0.0 | **1.5** | 2 |
| 06 | examples_all.md | 1.0 | 1.5 | 1.5 | +0.2 | +0.2 | **1.9** | 2 |
| 07-09 | terminology/* | 1.0 | 1.0 | 1.0 | +0.2 | +0.0 | **1.2** | 2 |

**排序语义** (v1.1): `P0 核心 (01/02=3.4 > 03=04=3.2) > P1 辅助 (06=1.9 > 05=1.5) > P2 查表 (07-09=1.2)`. 符合"批 1 优先 P0 结构层 / 批 2 补 P1-P2 推理+查表"设计 (§5). P1 的 06 examples 高于 P2 terminology, 自然表达 "混合受众下 examples 比裸 codelist 更有新手价值".

**floor 规则 (v1.1 简化)**: coverage_weight 从 1.0 降到 0.3 时, 核心覆盖分即为 0.3 × priority (最低 0.3). 任何文件 score 不低于 **0.15** (Rule E Q5=A 全量平权下限; 即便极端 coverage + 零 bonus 也保留最小存在感). v1.1 下 audience/novelty 是加法, 不再出现 "乘到 0" 的病理场景, floor 主要兜底 coverage 严重降级.

### 3.3 Phase 1 carry-over (Instructions 8K 字符) 对打分的影响

- System Prompt 设计 §4 Task C1 中, 需把 **高分文件 (01/02/04)** 的路由规则 优先压入 Instructions; 低分文件 (07-09) 按 "查表时" 规则描述即可, 不占 Instructions 字符配额.
- **字符预算分配**: 7,500 字符总预算分为 4 块: 角色定义 ~500 / 路由规则 ~4000 / 回答规范 ~2000 / 边界处理 ~1000.
- **若 Phase 3 实测 Instructions 上限为 tokens 而非 chars**: 预算放宽 4x, 但不扩写 (保持简洁, 避免注入退化).
- **来源 URL 待补**: 当前官方 OpenAI docs 未公开字段精度; 来源待 Phase 2 补齐 (可查 community.openai.com + help.openai.com "customize_gpt" 文章) 或 Phase 3 UI 实测.

---

## §4 Phase A-G Task 分解

每 Task 字段: ID / 内容 / checkpoint 级别 / 依赖 / 产物 / 估计.

### Phase A: Setup (一次性)

#### Task A1: 归档 Phase 2 前产物

- 内容: 确认 `docs/platform_profile.md`, `docs/research.md`, `dev/evidence/phase0_reviewer.md`, `dev/evidence/phase1_reviewer.md` 已入 git; 无需 archive 目录 (非 v1→v2 迁移场景)
- checkpoint: **none**
- 依赖: 无
- 产物: (检查项, 无新文件)
- 估计: 5 分钟

#### Task A2: 初始化 scripts/ 目录

- 内容: 建 `dev/scripts/`, symlink 或复制 `claude_projects/v1/scripts/count_tokens.py`; 初始化空脚本文件 `score_chatgpt_priority.py`, `merge_for_chatgpt.py`, `validate_chatgpt_stage.py`
- checkpoint: **none**
- 依赖: A1
- 产物: `dev/scripts/*.py` (骨架)
- 估计: 15 分钟

#### Task A3: 初始化 ab_reports/ 和 checkpoints/ 目录

- 内容: 建空目录 + .gitkeep
- checkpoint: **none**
- 依赖: A1
- 产物: `dev/ab_reports/.gitkeep`, `dev/checkpoints/.gitkeep`
- 估计: 2 分钟

---

### Phase B: 批次 1 合并 (P0 文件 01-04)

#### Task B1: executor 写 `score_chatgpt_priority.py`

- 内容: 按 §3 公式打分, 输出 ranked list 到 stdout + `dev/evidence/score_phase3.md` (v1.2 对齐脚本实现; Phase 3 Node 1 产物本应 phase3 语义, 见 §0 v1.2)
- checkpoint: **soft** (主控 + verifier 复审打分公式对齐 Rule E)
- 依赖: A2
- 产物: `dev/scripts/score_chatgpt_priority.py`, `dev/evidence/score_phase3.md`
- 估计: 30 分钟

#### Task B2: executor 写 `merge_for_chatgpt.py` (含 P12 + P13)

- 内容: 读合并配置 YAML, 按 md-heading 分段, 单表不跨 heading (P13), 每段起始加 `<!-- source: ... -->` (P12); 输出到 `current/uploads/<NN>_*.md`; 同时 emit manifest fragment 到 stdout
- checkpoint: **soft** (verifier 复核 P12 覆盖率 + P13 表格完整率)
- 依赖: A2
- 产物: `dev/scripts/merge_for_chatgpt.py`
- 估计: 60 分钟

#### Task B3: executor 跑合并, 产出 P0 文件 01-04

- 内容: 跑 `merge_for_chatgpt.py --stage batch1 --targets 01,02,03,04`; 产物落到 `current/uploads/`
- checkpoint: **none** (脚本自动, 结果走 B4)
- 依赖: B2
- 产物: `current/uploads/01_navigation.md`, `02_chapters_all.md`, `03_model_all.md`, `04_domain_specs_all.md`
- 估计: 10 分钟

#### Task B4: executor 跑 `validate_chatgpt_stage.py`

- 内容: 验证 批 1 产物 md5 稳定 / 段数 == 源文件数 / 无空文件 / P12 覆盖率 100% / P13 表格 0 条跨 heading
- checkpoint: **none** (rc=0 自动过, 非0 回 B3 debug)
- 依赖: B3
- 产物: `dev/evidence/validate_batch1.md`
- 估计: 10 分钟

#### Task B5: 主控 Rule A 抽检 (压缩率门槛)

- 内容: 如批 1 合并压缩率 > 50% (产物/源 tokens 比), 抽 **N=5** 段独立验证 (保留源结构 + P12 溯源可反查 + P13 表格完整)
- checkpoint: **soft** (主控判, 未过则回 B3 重做)
- 依赖: B4
- 产物: `dev/evidence/batch1_audit.md` (如触发)
- 估计: 20 分钟 (若触发)

#### Task B6: verifier 独立复审批 1 合并质量 (规则 D)

- 内容: 独立 subagent_type (如 code-reviewer) 验证 B3 产物 + B4 校验报告 + B5 抽检
- checkpoint: **soft**
- 依赖: B4, B5
- 产物: `dev/evidence/batch1_reviewer.md`
- 估计: 20 分钟

#### Task B7: 用户 GPT Builder 上传批 1 (4 文件) + smoke test

- 内容: 用户 (非 AI) 在 chat.openai.com Web UI 新建 GPT 或进现有 GPT Configure 页, 上传批 1 4 文件; 等 indexing; 跑 **3-5 题 smoke test** (见 §7 smoke 子集)
- checkpoint: **HARD** (用户 ack, 触发批 2 依赖)
- 依赖: B6
- 产物: `dev/checkpoints/batch1_smoke_ack.md` (用户填)
- 估计: 30 分钟 (用户侧, 不含等待 indexing)

---

### Phase C: 批次 2 合并 (P1-P2 文件 05-09)

#### Task C1 (首轮): executor 起草 `current/system_prompt.md` (Instructions)

- 内容: 按 §3.3 字符预算 4 块结构起草 ≤ 7,500 字符; Rule E Q1=C 公开广播语气 + Q2=C 混合受众语气; 边界诚实强调; 4 个 Conversation Starter 选题 (Q7 上限 4, 全部使用)
- **来源待补**: Instructions "8,000 字符" 官方 URL; 本 Task 输出产物 standoff note "若 Phase 3 实测上限是 tokens 而非 chars, 本预算有 4x 松弛"
- checkpoint: **soft** (verifier 复核对齐 Rule E 三项 + 字符数 ≤ 7500)
- 依赖: B7
- 产物: `current/system_prompt.md` v1 初稿
- 估计: 45 分钟

#### Task C2: executor 选 4 个 Conversation Starter

- 内容: 基于 Rule E Q2=C 混合受众, 4 个 starter 覆盖: (1) 变量快查 (专家高频) / (2) 域概念解释 (新手友好) / (3) 跨域关联 (中级) / (4) 术语查表 (专家高频)
- 初选 (承接 ROADMAP §4, Phase 3 可微调):
  - "AE 域的 AESER 变量定义是什么? 有哪些允许值?"
  - "RELREC 是什么? 什么场景下需要用它?"
  - "PC 和 PP 域之间是什么关系? 如何关联?"
  - "ISO 8601 日期格式在 SDTM 中有什么特殊规则?"
- checkpoint: **soft** (verifier 复核 4 题语气是否混合受众)
- 依赖: C1
- 产物: `current/system_prompt.md` 追加段 (并在 §7 A/B 矩阵对应 Conversation Starter 命中题)
- 估计: 15 分钟

#### Task C3: executor 跑 `merge_for_chatgpt.py` 批 2 (文件 05-09)

- 内容: 跑合并产出 05-09; 若 07/08 单文件 > 500 KB (chunk 数量考虑), 拆为 a/b 两文件 (总数不超 11, 仍 ≤ 20)
- checkpoint: **none**
- 依赖: B7 (批 1 用户 ack 保证路径有效)
- 产物: `current/uploads/05_*` .. `09_*`
- 估计: 20 分钟

#### Task C4: executor 跑 `validate_chatgpt_stage.py` 批 2

- 内容: 同 B4, 范围扩至批 2 5 文件
- checkpoint: **none**
- 依赖: C3
- 产物: `dev/evidence/validate_batch2.md`
- 估计: 10 分钟

#### Task C5: 主控 Rule A 抽检批 2 (N=5)

- 内容: 同 B5 但范围批 2. terminology 特别关注 codelist 完整性 (Rule E Q5=A 63 域不缺 codelist)
- checkpoint: **soft**
- 依赖: C4
- 产物: `dev/evidence/batch2_audit.md` (如触发)
- 估计: 20 分钟

#### Task C6: verifier 独立复审批 2 (规则 D)

- 内容: 同 B6 但对批 2
- checkpoint: **soft**
- 依赖: C4, C5
- 产物: `dev/evidence/batch2_reviewer.md`
- 估计: 20 分钟

#### Task C7: 用户 GPT Builder 上传批 2 (5 文件) + 完整 A/B 矩阵

- 内容: 用户上传批 2; 等 indexing; **执行 Q8 Indexing indicator 实测 (Phase 1 PARTIAL carry-over)** — 上传后立即问批 2 某文件特定唯一术语, 验证实际可检索 (不接受仅 UI 状态); 然后跑 §7 完整 A/B (10-15 题)
- checkpoint: **HARD** (用户 ack, 触发 Phase D 依赖)
- 依赖: C6
- 产物: `dev/checkpoints/batch2_full_ab_ack.md`
- 估计: 60-90 分钟 (用户侧)

---

### Phase D: A/B 矩阵执行与归档 (10-15 题)

#### Task D1: 跑完整 A/B 矩阵 (§7 定义的 13 题)

- 内容: 用户在 GPT 对话框逐题提问; AI 主控记录答案到 `dev/test_results.md`
- checkpoint: **none** (每题记录自动, 汇总走 D2)
- 依赖: C7
- 产物: `dev/test_results.md` 追加批 2 全题答案
- 估计: 60 分钟

#### Task D2: executor 写 `dev/ab_reports/STAGE_BATCH2_AB_REPORT.md`

- 内容: 13 题 PASS/FAIL 统计 + 归因 (若 FAIL); Rule E Q1=C 公开受众语气题 2 道 + Q2=C Conversation Starter 4 题 + 跨 chunk 检索题 + 边界诚实 + hybrid search 对比题 (Phase 1 未决 #2)
- checkpoint: **soft** (verifier 复核)
- 依赖: D1
- 产物: `dev/ab_reports/STAGE_BATCH2_AB_REPORT.md`
- 估计: 45 分钟

#### Task D3: A/B 衰减响应 (P10)

- 内容: 如 D2 结果 FAIL 题 ≥ 2, **立即停** Phase D, 走 Rule B 归档 → verifier 归因 → 用户决策 continue / rollback / 重合并
- checkpoint: **HARD** (用户决策)
- 依赖: D2 (仅触发时)
- 产物: `dev/evidence/failures/stage_4_attempt_<M>.md` (如触发, 规则 B 数字惯例与其他 Phase 对齐)
- 估计: 可变 (阻塞 Phase E 直到决策)

---

### Phase E: Phase 3→Phase 4 carry-over 回归 + 实测 carry-over 收集

#### Task E1: Q8 Indexing indicator 实测 (Phase 1 PARTIAL transfer)

- 内容: 复核 C7 的 Indexing 实测记录是否完整; 补 "UI 显示已上传 vs 实际可检索" 对比表; 作为 Phase 3 → Phase 4 输入
- checkpoint: **soft**
- 依赖: C7
- 产物: `dev/evidence/phase3_q8_indexing_reality.md`
- 估计: 20 分钟

#### Task E2: Instructions 字符 vs tokens 精度实测 (Phase 1 MEDIUM carry-over)

- 内容: 在 GPT Builder Configure 页实测当前 Instructions 的长度限制 (UI 提示 / 粘贴超长测试); 记录官方实际约束 (chars 还是 tokens); 若 ≠ 字符, Phase 4 前回 Task C1 调整预算; 补来源 URL
- checkpoint: **soft** (若实测结果触发 C1 调整, 升级 hard)
- 依赖: C7
- 产物: `dev/evidence/phase3_instructions_budget_reality.md`
- 估计: 20 分钟

---

### Phase F: Phase 4 审查 + 发布准备

#### Task F1: 终态回归 A/B (Phase G 级别)

- 内容: 批 1 + 批 2 合并上传后, 再跑一次 13 题全矩阵, 对比 Task D1 结果, 确认无跨批 regression
- checkpoint: **HARD** (用户 A/B 终审)
- 依赖: E1, E2
- 产物: `dev/ab_reports/STAGE_FINAL_AB_REPORT.md`
- 估计: 60 分钟

#### Task F2: verifier 独立复核 STAGE_FINAL (规则 D)

- 内容: code-reviewer (独立 subagent) 复核 F1 报告 + Rule A 抽检结果 + P10 合规
- checkpoint: **soft**
- 依赖: F1
- 产物: `dev/evidence/stage_final_reviewer.md`
- 估计: 30 分钟

#### Task F3: A/B PASS 比检查 (≥ 90% 目标)

- 内容: 计算 13 题 PASS 比; 若 ≥ 90% (11/13+) 开 Phase 5 gate; 若 < 90%, 回 Phase D3 归因循环
- checkpoint: **HARD** (用户决策是否进 Phase 5)
- 依赖: F1, F2
- 产物: `dev/evidence/phase4_pass_rate_decision.md`
- 估计: 15 分钟

#### Task F4: Builder Profile + Privacy Policy 起草 (Q6 要求)

- 内容: 根据 Phase 1 Q6, 为 Rule E Q1=C Store 发布准备: Builder Profile (姓名/组织/域名); 由于无 GPT Actions, Privacy Policy 可用通用 placeholder (或指引用户自填)
- checkpoint: **soft** (用户完成实际提交)
- 依赖: F3 (F3 PASS 才意义)
- 产物: `current/builder_profile_draft.md` + `current/privacy_policy_draft.md`
- 估计: 45 分钟

#### Task F5: 发布决策 checkpoint

- 内容: 用户决策三选一: (a) 仅 Private 自用 / (b) 链接共享 (默认下一步) / (c) GPT Store 公开 (Rule E Q1=C 预设, 但用户可否决)
- checkpoint: **HARD** (决策 → 触发 Phase G 收束方向)
- 依赖: F4
- 产物: `dev/checkpoints/phase5_publish_decision.md`
- 估计: 用户侧 (可离线考虑)

---

### Phase G: 收束 (Phase 5)

#### Task G1: executor 写 `docs/RETROSPECTIVE.md` (规则 C 三段式)

- 内容: 保留下来的做法 / 必须补上的缺口 / 关键决策复盘; 必含 Phase 1 10 条修订落地情况 + Rule E 三项实际命中率 + Phase 1 MEDIUM carry-over 处置结果
- checkpoint: **soft**
- 依赖: F5
- 产物: `docs/RETROSPECTIVE.md`
- 估计: 60 分钟

#### Task G2: verifier 独立复核 RETROSPECTIVE (规则 D)

- 内容: code-reviewer 独立 subagent 复核三段是否完整 + 是否有 "self-congrat" (v1 G1 教训: writer 说 PASS ≠ 业务 PASS, 必须有独立视角)
- checkpoint: **HARD** (规则 C 强制独立 PASS)
- 依赖: G1
- 产物: `dev/evidence/retrospective_reviewer.md`
- 估计: 30 分钟

#### Task G3: executor 写 `current/UPLOAD_TUTORIAL.md` (10 章节)

- 内容: 参照 Claude `claude_projects/current/UPLOAD_TUTORIAL.md` 结构, 10 章节: 前置 / 建 GPT / Instructions / 上传 / Smoke Test / 回归 / 排错 / 升降级 / 分享 / 后续
- checkpoint: **soft**
- 依赖: G1
- 产物: `current/UPLOAD_TUTORIAL.md`
- 估计: 90 分钟

#### Task G4: 更新 ROADMAP.md 为 "已完成"

- 内容: `ai_platforms/chatgpt_gpt/ROADMAP.md` 顶部状态改 "**已完成** (2026-MM-DD)"; 补实际数据 (capacity % / A/B PASS 比 / 实际合并文件数)
- checkpoint: **none**
- 依赖: G2, G3
- 产物: ROADMAP.md 修订
- 估计: 15 分钟

#### Task G5: 更新上游索引 (收尾三件套 + Key Paths)

- 内容: 按 CLAUDE.md "Session Wrap-up" 协议, 更新 `.work/MANIFEST.md`, `.work/meta/worklog.md`, `docs/PROGRESS.md`, `CLAUDE.md` Key Paths table, `ai_platforms/README.md`, `ai_platforms/SYNC_BOARD.md`
- checkpoint: **none**
- 依赖: G4
- 产物: 6 个索引文件修订
- 估计: 30 分钟

#### Task G6: Commit + push

- 内容: 单一 descriptive commit (中文, 遵循项目 commit 风格), push main
- checkpoint: **HARD** (用户 ack 最终收尾)
- 依赖: G5
- 产物: git commit
- 估计: 10 分钟

---

### Phase 统计

| Phase | Task 数 | Hard checkpoint | Soft checkpoint | None |
|-------|:-------:|:--------------:|:---------------:|:----:|
| A | 3 | 0 | 0 | 3 |
| B | 7 | 1 | 4 | 2 |
| C | 7 | 1 | 5 | 1 |
| D | 3 | 1 | 1 | 1 |
| E | 2 | 0 | 2 | 0 |
| F | 5 | 3 | 2 | 0 |
| G | 6 | 2 | 3 | 1 |
| **合计** | **33** | **8** | **17** | **8** |

---

## §5 批次设计

### 5.1 批次表

| 批次 | 范围 | 文件数 | 累计文件 | 预计 MB | A/B 题数 | Hard checkpoint |
|------|------|:-----:|:--------:|--------:|:-------:|:---------------:|
| 1 | P0 (01-04) | 4 | 4/20 | ~1.15 MB | 3-5 smoke | B7 (用户 smoke ack) |
| 2 | P1-P2 (05-09) | 5 (可能 6 若拆 07/08) | 9-10/20 | ~8.5 MB | 10-15 full | C7 (用户 full A/B ack) |

### 5.2 每批回答 3 问 (来自 `_template/05_solution.md`)

**批 1**:
1. 目标 token 数? 估算 ~280K tokens (navigation + chapters + model + specs 合计 1.15 MB text)
2. 覆盖 slice? **结构层** — 导航路由 + 章节概念 + 模型约束 + 63 域变量 spec (不含 assumptions/examples/terminology, 专家路径够用)
3. A/B 新增题? smoke 3-5 题 (§7 定义): 1 路由 + 1 定义查询 + 1 边界诚实 (未上传 assumptions 应承认未收录) + (可选 2 公开受众语气)

**批 2**:
1. 目标 token 数? 估算 ~2.15M tokens (assumptions + examples + terminology 3 类合计 ~8.5 MB; RAG 池不是一次性注入, 不触 context 上限)
2. 覆盖 slice? **推理层 + 查表层** — 补全 Rule E Q5=A 63 域平权 + Q2=C 混合受众场景 (新手找示例 + 专家查 codelist)
3. A/B 新增题? 完整 13 题 (§7), 含: 2 路由 + 3 跨 chunk 检索 + 2 边界诚实 + 4 Conversation Starter 命中 + **2 公开受众语气 (Rule E Q1=C 必考)**

### 5.3 为何 2 批到位 (非 Claude 的 5+1 批拐点)

- Phase 1 Q2/Q4: chunk 800/400 + top-K=20 硬参数清晰, 无 "capacity 不透明" 问题
- Phase 1 Q5: 20 文件硬限跨套餐一致, 不需 calibration
- Phase 1 Q9: 10 GB/user 存储远超 SDTM ~10 MB, 不触限
- 结论: 2 批 = P0 + P1-P2 一次到位, 不做增量拐点测试

---

## §6 失败模式 → 归档路径 (规则 B)

| # | 失败模式 | 触发信号 | 响应 | 归档路径 |
|---|---------|---------|------|---------|
| 1 | 合并后表格被 chunker 切断 (profile F1) | A/B 表格题 FAIL | Instructions 强调 "数据查 04/06" 路由优先; P13 TableAware 审查 | `dev/evidence/failures/stage_<N>_attempt_<M>.md` |
| 2 | 跨 chunk 检索表格断裂 hallucinate (profile F2) | A/B codelist 题答错 | 提高 P12 溯源密度 + Instructions 强调 "只答源中明写" | 同上 |
| 3 | 20 文件硬限下批 2 超量 (profile F3) | 批 2 文件数 > (20 - 批1) | 合并粒度二次压缩 (e.g. terminology 三文件合一) | 同上 |
| 4 | 公开 GPT 被 Store 搜索暴露未定稿 (profile F4) | Phase 4 未 PASS 就公开 | Phase F5 hard checkpoint 必须在 F3 PASS 后 | 同上 (发布撤回) |
| 5 | Custom Actions NCI EVS rate limit (profile F5) | 暂不实现 Actions, 规避 | — (不实现) | N/A |
| 6 | **A/B 衰减 ≥2 题 (P10)** | D2 FAIL 题 ≥ 2 | **立即停**, reviewer 归因, 用户决策 continue/rollback/重合并 | 同上 |
| 7 | capacity 超预算 | 某批产物 > 预估 15% | 看是否内部冗余, 优先降冗余; 不直接加批 | 同上 |
| 8 | reviewer PASS 但主控抽样 FAIL (规则 A vs 结构检查冲突) | Rule A 抽检与 verifier 结果矛盾 | **尊重主控** (Claude v1 G1 教训), 重做 | 同上 |
| 9 | Hard checkpoint 等用户 > 24h | 用户未 ack | `_progress.json.status = paused`, 不推进 | N/A (暂停不归档) |
| 10 | 源文件污染检测 (P5 违规) | `git status knowledge_base/` 非 clean | **立即回滚**, P5 调查 | `dev/evidence/failures/p5_violation.md` |
| 11 | Q8 Indexing UI 状态 ≠ 可检索 (Phase 1 carry-over) | C7/E1 实测 "已上传但不可检索" | 重新上传 (Q8 社区建议); 若仍不过, 归档 + 拆文件重传 | 同上 |
| 12 | Instructions 超字符限制 (Phase 1 MEDIUM carry-over) | C1 产物 > 7500 字符 或 GPT Builder UI 拒绝 | 压缩 + 实测上限; 若上限是 tokens (松 4x) 恢复; 若是 chars (紧), 砍路由规则详细度 | 同上 |

---

## §7 A/B 矩阵 (13 题初稿, Phase 3 细化)

### 7.1 矩阵结构

- 路由题: 2 (批 1 smoke 含 1)
- Conversation Starter 命中: 4 (批 2 全量, Q7 上限 4 完全使用)
- 跨 chunk 检索: 3 (批 2, 验证 top-K=20 覆盖性)
- 边界诚实: 2 (批 1 smoke 1, 批 2 1)
- **公开受众语气 (Rule E Q1=C 必考)**: 2 (批 2 全量)
- hybrid search 精确 vs 语义对比 (Phase 1 未决 #2): 1 (批 2 可选)

**总计**: 13 题 (2+4+3+2+2=13; 可选 hybrid 题 +1 = 14).

### 7.2 题目清单

| ID | 维度 | 题目 | 预期命中方式 | PASS 判据 | 批次 |
|:---|------|------|-------------|-----------|:----:|
| T01 | 路由 (smoke) | "AE 域的 AESER 变量定义?" | 04_domain_specs_all.md → AE 段 → AESER 行 | 引用变量名 + Role (Record Qualifier) + Core (Perm) + CT (NY) | 1 |
| T02 | 定义查询 (smoke) | "RELREC 是什么?" | 02_chapters_all.md + 04 相关域 | 识别为关联关系数据集, 给出使用场景; 不臆造具体字段 | 1 |
| T03 | 边界诚实 (smoke) | "AERELN codelist 所有 Synonyms 是什么?" | 批 1 不含 terminology → 应答 "批 1 未收录, 见批 2 07_terminology_core" 或 "未收录, 见 NCI EVS" | **零臆造 synonyms**; 明确声明未收录 | 1 |
| T04 | 路由 (full) | "PC 和 PP 域怎么关联?" | 04 (PC/PP spec) + 02 (chapters RELREC 章) | 引用两域; 给出 RELREC 或直接 key; 避免混淆 | 2 |
| T05 | Starter 命中 | "AE 域的 AESER 变量定义是什么? 有哪些允许值?" (Starter 1) | 04 → AE → AESER | 首答 PASS; 包含 allowed values Y/N | 2 |
| T06 | Starter 命中 | "RELREC 是什么? 什么场景下需要用它?" (Starter 2) | 02 + 04 | 首答 PASS; 场景描述清晰 | 2 |
| T07 | Starter 命中 | "PC 和 PP 域之间是什么关系? 如何关联?" (Starter 3) | 04 (PC/PP) + 02 | 首答 PASS; 关联字段正确 | 2 |
| T08 | Starter 命中 | "ISO 8601 日期格式在 SDTM 中有什么特殊规则?" (Starter 4) | 02 (chapters 数据类型章) | 首答 PASS; 引用 --DTC 字段规范 | 2 |
| T09 | 跨 chunk 检索 | "列出 AE 域所有 Core=Req 的变量" | 04 AE 段跨多 chunk 汇总 (top-K=20 覆盖) | 完整列表 (参照 SDTMIG AE spec); 缺失 ≤ 1 PASS | 2 |
| T10 | 跨 chunk 检索 | "LB 域有哪些 timing 变量?" | 04 LB + 02 timing 章 | 完整列表; 包含 LBDTC, --STDTC, --ENDTC etc. | 2 |
| T11 | 跨 chunk 检索 | "EX 和 CM 两域在药品记录上的差异?" | 04 (EX spec + CM spec) + 05 assumptions | 差异点 ≥ 3 条; Role / timing / controlled terms 对比 | 2 |
| T12 | 边界诚实 (full) | "AESOC codelist 从 MedDRA 哪个版本开始支持?" | 07 terminology 不含版本元数据 | **零臆造版本号**; 指向 NCI EVS Browser + MedDRA 官方 | 2 |
| T13 | **公开受众语气 (Q1=C)** | "我是病人家属, 能简单解释 SDTM 是什么吗?" | 01 navigation + 02 chapters 概念段 | **新手友好**; 无生僻术语堆砌; 类比恰当; 不假设行业背景 | 2 |
| T14 | **公开受众语气 (Q1=C)** | "我刚入行监管数据, AE 和 DV 一般哪个先学?" | 04 + 02 chapter priorities | **非专业用户友好**; 两者定位解释; 给学习路径; 不过度 jargon | 2 |
| T15 (可选) | hybrid search 对比 | 精确: "LBTEST 变量含义?" vs 语义: "lab test 的标签字段是哪个?" | 04 LB + 07 terminology | 两种提问风格命中率对比; 实际差距 ≤ 20% PASS | 2 |

### 7.3 Smoke 子集 (批 1 用, 3-5 题)

- T01 (路由)
- T02 (定义)
- T03 (边界诚实, 关键 — 验证没 terminology 时不会臆造)
- T13 (Q1=C 公开语气, **必测** — Rule E Q1=C 公开受众预检, smoke 提前暴露语气偏差, Phase 3 Node 3a reviewer LOW-L1 升级 2026-04-20)
- **T-Q8** (Indexing indicator 实测, Phase 1 PARTIAL carry-over 兑现, smoke_questions_draft.md S5)

**v1.3 修订** (2026-04-20, Phase 3 Node 3a reviewer carry-over L1): T13 从"可选"升"必测", 同时明示 Q8 indexing 实测题纳入 smoke 5 题. 对应 `dev/evidence/smoke_questions_draft.md` S1-S5 映射为 T01/T02/T03/T13/T-Q8.

### 7.4 衰减阈值 (P10)

- 13 题中 FAIL 1 题 = regression evidence + reviewer 归因 (不停, 继续)
- FAIL 2 题 = 立即停, 走 Task D3
- FAIL 3+ = 强制回滚批 2 重做

---

## §8 风险缓解

| # | 风险 | 可能时点 | 缓解策略 | 监测信号 |
|---|------|---------|---------|---------|
| R1 | Instructions 上限精度未明 (Phase 1 MEDIUM) | Task C1 (Phase C) | 按字符保守预算 7500; Task E2 实测后调整 | C1 产物 UI 接受 yes/no; E2 实测数字 |
| R2 | Q8 Indexing 不可靠 (Phase 1 PARTIAL) | Task C7 (批 2 上传后) | 上传后立即实测唯一术语查询 (非 UI 状态); 失败重上传 | C7 smoke 是否首答 PASS |
| R3 | Rule E Q1=C 公开语气偏离 | Task C1 + D2 | T13/T14 双题测试; D2 verifier 独立复审语气 | T13/T14 PASS? |
| R4 | Q5=A 63 域平权被"常用域偏倚"侵蚀 | Task B2 (merge 脚本) | validate_chatgpt_stage.py 强制段数 == 源文件数 (63); 少即 FAIL | B4/C4 rc 状态 |
| R5 | 批 1 → 批 2 跨批 regression | Task F1 终态回归 | F1 跑完整 13 题, 对比 D1 结果 | F1 报告 FAIL 题数 |
| R6 | GPT Store 审核延迟 (Q6: 2-5 工作日) | Task F5 决策后 | Phase 5 时间线预留 1 周 buffer; F5 不强求公开, 可先链接共享 | Store Dashboard 状态 |
| R7 | hybrid search 语义 vs 关键词命中不均 | Task T15 | A/B 发现后, 在 Instructions 加路由 hint "如精确变量名查询失败, 请换语义描述" | T15 两题命中率差 |
| R8 | 批 2 terminology 三文件仍超单文件 chunk 数量 | Task C3 | 拆 07/08 为 a/b 两文件 (总数 ≤ 10, P11 合规) | C3 validate 报告单文件 chunks 数 |

---

## §9 开放问题 (Phase 3 前需决策)

| # | 问题 | 当前建议 | 决策节点 |
|---|------|---------|---------|
| O1 | 07/08 terminology 三大文件是否预拆 a/b? | 先合并 (保持文件数低), 若 Phase 3 A/B 跨 chunk 题 FAIL 再拆 | Task C3 |
| O2 | Task F4 Builder Profile 域名验证是否必需? | 先用普通 Builder Profile (无域名); 若 Store 审核要求域名, Phase 5 补 | Task F4 |
| O3 | Privacy Policy 是否需要独立 URL 还是文本即可? | 无 GPT Actions 情况下文本 placeholder 应足够; Phase F5 前最终确认 Q6 官方要求 | Task F4/F5 |
| O4 | Task G6 commit 是单次大提交还是分 Phase 多提交? | 分 Phase 多次 commit (A/B/C/D/F/G 边界各一次, 便于 rollback) | 各 Phase 收尾 |
| O5 | Hybrid search T15 是否 Phase 3 必做? | Phase 3 可选 (12 题必做 + 1 可选). 若 Phase 3 时间允许即做 | Task D1 |
| O6 | Phase 1 MEDIUM carry-over 如 Phase 3 实测仍无官方 URL 怎么办? | 保留 "来源待补" note, 以实测数字为 de-facto 标准入 RETROSPECTIVE G1 | Task G1 |

---

*来源: `_template/04_plan.md` 骨架 + `_template/05_solution.md` 策略 + `docs/platform_profile.md` Phase 0 + `docs/research.md` Phase 1 + `dev/evidence/phase1_reviewer.md` carry-over + `dev/evidence/_progress.json` rule_e_ack. 结构借鉴 `claude_projects/docs/PLAN_V2.md` (不照抄).*
