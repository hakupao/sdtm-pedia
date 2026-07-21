# 范本应用 Checklist — 新平台部署启动清单

把 `_template/` 应用到某个具体平台 (e.g. `chatgpt_gpt/`, `gemini_gems/`, 未来的 `xxx/`) 的操作清单. 按顺序执行.

---

## Phase 0: 启动 (30 分钟)

- [ ] **确认 Tier 等级**: 参照 `~/.claude/CLAUDE.md <workflow_tiers>`, 小平台 <5 步可 Tier 1 裸跑; 5-15 步 Tier 2; >15 步或多天 Tier 3. 本范本**默认 Tier 2**, Tier 1 可跳过 evidence 层, Tier 3 需补 trace.jsonl + 全 subagent_prompts.
- [ ] **复制本范本**: `cp -r ai_platforms/_template/* ai_platforms/<platform>/_spec/`
- [ ] **读完 `00_platform_profile.md`** 并填空 (RAG/容量/分享/失败模式 5+ 字段). 不填就不能进 Phase 1.
- [ ] **问清楚用户业务优先级 (规则 E)**: 平台的覆盖优先级是什么? 哪些内容必须 100% 命中? 哪些可以只覆盖高频? 记录进 `docs/PLAN.md §打分阶段`.

---

## Phase 1: 调研 (Tier 2/3 强制, Tier 1 可简化)

- [ ] **按 `03_research.md` 八问八答格式做前置调研**, 输出到 `docs/research.md` (或 `docs/capacity_research.md` 如果平台是容量不透明型)
- [ ] 调研必答的 8 个问题:
  1. 平台 "capacity" / "limit" 的官方定义?
  2. 当前容量上限是多少? 不同套餐差异?
  3. 历史上限调整过吗?
  4. 文件是全量注入还是 RAG 检索?
  5. 索引指示器 / Indexing status 可靠吗?
  6. 本平台 Knowledge 和其他 (Files API / Memory) 是同一概念吗?
  7. 分享机制: 个人/团队/公开哪些支持?
  8. 本地 token 统计和平台 UI token 统计一致吗? (calibration 偏差)
- [ ] 每个答案**附官方文档或社区实测链接** (避免 hallucinate)
- [ ] 给出"对 PLAN 的修订"段: 调研后需要改哪些原假设

---

## Phase 2: 策略设计 + PLAN

- [ ] **按 `05_solution.md` 定内容策略**: 文件合并粒度 / 批次数量 / System Prompt 累积段设计 / 是否需要 Deferred stub
- [ ] **按 `04_plan.md` 模板写 PLAN.md**: §0 修订记录 + §1 P1-Pn 执行规则 + §2 文件结构 map + §3-§N Phase A-H Task 分解
- [ ] PLAN 必包含的规则:
  - P1-P7 (v1 传承): 量化 PASS / 写审分离 / 估算值 `~` 前缀 / 人工抽查 checkpoint / 源文件只读 / subagent 上下文隔离 / 进度持久化
  - P8 失败归档 (规则 B) / P9 语义抽检 (规则 A) / P10 A/B 衰减强制响应
  - **规则 E (新)**: 用户优先级乘入打分公式, 非事后重平衡
- [ ] PLAN 每个 Task 明示 **checkpoint 级别** (hard / soft / none), 避免 v1 G4 缺口

---

## Phase 3: 落地 (批次执行)

- [ ] **按 `07_agent_dispatch.md` 调度 subagent**:
  - writer = executor subagent (model=opus for complex work)
  - reviewer = code-reviewer subagent (**不同 subagent_type**, 规则 D)
  - 主控独立抽样 N (见规则 A)
- [ ] **按 `08_evidence.md` 建立三层 evidence**:
  - L1 `evidence/_progress.json` — state of truth
  - L2 `evidence/trace.jsonl` — append-only 事件流
  - L3 `evidence/subagent_prompts/` + `evidence/failures/` — 证据链
- [ ] **每批做一次 A/B 回归** (`06_review.md` 矩阵), 结果写到 `dev/ab_reports/STAGE_<N>_AB_REPORT.md`
- [ ] **Hard checkpoint 必停**, 等用户 A/B ack, 不擅自连续推进
- [ ] **失败不删** (规则 B), 归档到 `evidence/failures/stage_<N>_attempt_<M>.md`

---

## Phase 4: 收束

- [ ] **按 `09_closure.md` 写三件套**:
  - `docs/RETROSPECTIVE.md` (三段式: 保留/补上/决策复盘 + 规则 C 产出)
  - `docs/handoff.md` (如有下游, e.g. Phase 7 RAG)
  - `current/UPLOAD_TUTORIAL.md` (10 章节用户视角教程)
- [ ] **RETROSPECTIVE 必须由独立 lane 审阅** (规则 D), 不能主控自写自审
- [ ] **ROADMAP.md 状态更新**: `**待开始**` → `**已完成**` + 实际产出 / capacity / A/B PASS 数据
- [ ] **目录 reorg 到 current/docs/dev/archive** (参照 `01_directory_structure.md`)
- [ ] 更新上游 `ai_platforms/README.md` 总览表格 + 项目 `CLAUDE.md` Key Paths 新增入口
- [ ] Commit + push, 单 commit 不拆分无关 PR

---

## 填空点位速览

本范本中需要替换的占位符:

| 占位符 | 含义 | 示例 |
|--------|------|------|
| `<platform>` | 平台目录名 | `chatgpt_gpt`, `gemini_gems` |
| `<PLATFORM_NAME>` | 平台显示名 | `ChatGPT GPTs`, `Gemini Gems` |
| `<CAPACITY_LIMIT>` | 平台容量限制 | `20 文件` / `1M tokens` / `77%` |
| `<RAG_MODE>` | RAG 机制 | `自动分片` / `全量注入` / `内置 RAG` |
| `<SHARE_MODEL>` | 分享模型 | `私有` / `团队` / `公开` |
| `<TIER>` | 项目 Tier | `2` / `3` |
| `<N_BATCHES>` | 渐进批次数 | `1` / `2` / `5+1` |
| `<AB_MATRIX_SIZE>` | A/B 矩阵题数 | `10` / `24` |

---

## 规则 A-E 快查

| 规则 | 内容 | 触发 |
|------|------|------|
| A (全局) | 压缩/改写 >50% 强制 N 样本独立抽检 | 每批 writer 完成后 |
| B (全局) | 失败归档不删, 留 `failures/step_NN_attempt_X.md` | 任何失败 attempt |
| C (全局) | Tier 2/3 收尾强制 RETROSPECTIVE.md | Phase 4 收束 |
| D (全局) | Writer ≠ Reviewer (不同 subagent_type) | 每次 subagent 派发 |
| **E (本范本)** | 用户业务优先级 PLAN §打分阶段即确认 | Phase 2 策略设计前 |

---

## 什么时候可以跳过部分规范?

| 情况 | 可跳过 |
|------|-------|
| Tier 1 小平台 (1-2 文件, <1 小时) | L2 trace + L3 prompts + A/B 矩阵 (抽 3 题即可) + RETROSPECTIVE (一段话) |
| 平台官方有精确容量文档 | 八问八答简化为 3 问 (容量/分享/索引指示器) |
| 所有批次 1 批完成 (e.g. Gemini 1M 窗口全上) | 批次 checkpoint 合并为 1 个终态 checkpoint |
| 无下游交接 | 跳过 handoff.md |

---

*来源: claude_projects/ v2 完整执行经验抽象.*
