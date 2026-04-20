# 04 PLAN 模板

Phase 2 的核心产物. 每个平台部署必有一份 `docs/PLAN.md`, 用本文件做骨架.

---

## PLAN 必备章节

```
§0 修订记录
§1 执行规则 P1-P10 + 规则 E
§2 文件结构 map (Create / Modify / Read-only)
§3 Phase A: Setup
§4 Phase B-F: 批次执行 (按策略分批)
§5 Phase G: 终态 A/B 整合回归
§6 Phase H: 收束
§7 (可选) Subagent 模板预写
§8 (可选) 失败/退化应急预案
```

---

## §0 修订记录 (必填)

每次修改 PLAN 追加一行, 不覆盖.

| 版本 | 日期 | 修改人 | 变更 | 触发 |
|------|------|-------|------|------|
| v1 | 2026-04-<DD> | 主控 | 初版 | 启动 |
| v1.1 | ... | ... | 调研发现容量假设错, 改策略 | Phase 1 Q2 调研 |

---

## §1 执行规则

继承全局 `~/.claude/CLAUDE.md` 四条规则 A/B/C/D, 本范本新增规则 E, 本项目可补 P1-P10:

| # | 规则 | 适用 |
|---|------|------|
| A (全局) | 语义抽检: 压缩/改写 >50% 强制 N 样本独立抽检, N 写进本 PLAN | 每批 writer 完成后 |
| B (全局) | 失败归档: 任何 attempt 不删, `failures/step_NN_attempt_X.md` | 任何失败 |
| C (全局) | Retro 强制: Tier 2/3 收尾必写 RETROSPECTIVE.md | Phase 收束 |
| D (全局) | 写审分离: Writer ≠ Reviewer (不同 subagent_type) | 每次派发 |
| **E (本范本)** | **用户业务优先级必须在 §打分阶段即确认**, 不能等事后重平衡 | Phase 2 策略设计前 |
| P1 | 量化 PASS 标准: 每 Step 打印 `[Stage X.Y] <file>: <N> tokens (target ≤<X>K)` | 每 Step |
| P2 | 写/审分离执行态: executor 与 reviewer 必不同 subagent_type, 都可用 opus | 每 subagent 派发 |
| P3 | AI 估算值前缀 `~`, 实测值不加 | manifest / 报告 |
| P4 | 人工抽查 checkpoint: 每个阶段完成都是 hard/soft/none, 不擅自连推 | 每批 |
| P5 | 源文件只读: `knowledge_base/` 不允许 Edit/Write | 全程 |
| P6 | Subagent 上下文隔离: 每个脚本独立 executor, 主控不读脚本源 | 每次派发 |
| P7 | 进度持久化: 每 Step 完成立即更新 `evidence/_progress.json` | 每 Step |
| P8 | (同规则 B) | — |
| P9 | (同规则 A) | — |
| P10 | A/B 衰减强制响应: 衰减 ≥2 题立即停, ≥1 题写 regression evidence + reviewer 归因 | 每批 A/B 后 |

**自定义 P11-Pn**: 如果本平台有独特约束 (e.g. ChatGPT 20 文件硬限 → P11 "合并粒度不得超 20 文件"), 在本 §1 列出.

---

## §2 文件结构 map

列全部本次执行期间会动到的文件. **三分类**:

### 2.1 Create (本次新建)

```
ai_platforms/<platform>/dev/scripts/           (目录)
ai_platforms/<platform>/dev/scripts/*.py       (N 个脚本)
ai_platforms/<platform>/current/uploads/       (目录)
ai_platforms/<platform>/current/system_prompt.md
ai_platforms/<platform>/current/upload_manifest.md
ai_platforms/<platform>/current/UPLOAD_TUTORIAL.md
ai_platforms/<platform>/dev/evidence/_progress.json
ai_platforms/<platform>/dev/evidence/trace.jsonl
ai_platforms/<platform>/dev/test_results.md
ai_platforms/<platform>/docs/RETROSPECTIVE.md
ai_platforms/<platform>/docs/PLAN.md           (本文件)
...
```

### 2.2 Modify (执行中滚动更新)

```
ai_platforms/<platform>/dev/evidence/_progress.json      (每 Step)
ai_platforms/<platform>/dev/evidence/trace.jsonl         (append-only)
ai_platforms/<platform>/current/system_prompt.md         (每批增量)
ai_platforms/<platform>/current/upload_manifest.md       (每批累计)
ai_platforms/<platform>/dev/test_results.md              (每批 A/B)
.work/MANIFEST.md                                        (收尾时)
.work/meta/worklog.md                                    (收尾时)
docs/PROGRESS.md                                         (收尾时)
CLAUDE.md                                                (收尾时, Key Paths)
```

### 2.3 Read-only (强制禁写)

```
knowledge_base/**                                        (P5)
ai_platforms/_template/**                                (范本不可污染)
ai_platforms/<platform>/archive/**                       (冻结)
```

### 2.4 脚本职责边界 (每脚本单一职责)

| 脚本 | 单一职责 | 输入 | 输出 |
|------|---------|------|------|
| count_tokens.py | 测 token (可复用 claude_projects v1) | .md 文件/目录 | stdout: `<file>: <N> tokens` |
| score_<X>.py | 圈定批次优先级 | 源 + 用户优先级 | stdout: ranked list |
| build_<platform>_stage.py | 分阶段构建 + 累计 token + manifest | --stage v.X | 每批 manifest |
| merge_<type>.py | 合并文件 (如平台需要) | 源 | output/ |
| validate_<X>.py | 产物完整性校验 | output/ | rc=0/非0 |

---

## §3 Phase A: Setup (一次性, 2-4 Tasks)

### Task A1: 归档基线 (如果有 v1)

- Files: Create `archive/v<N-1>_baseline/`
- [ ] Step 1: 复制前版本产物到 archive
- [ ] Step 2: 写 archive README 冻结声明

### Task A2: 初始化 evidence 目录

- Files: Create `dev/evidence/`, `dev/evidence/subagent_prompts/`, `dev/evidence/failures/`, `dev/evidence/checkpoints/`
- [ ] Step 1: 创建四目录
- [ ] Step 2: 初始化 `_progress.json` schema
- [ ] Step 3: 初始化 `trace.jsonl` (空)

### Task A3: 建 scripts/ + 复用 v1 count_tokens

- Files: Create `dev/scripts/`, symlink or copy `count_tokens.py`
- [ ] Step 1: 建目录
- [ ] Step 2: 复用 count_tokens

**Checkpoint 级别**: none (Setup 低风险)

---

## §4 Phase B-F: 批次执行 (按策略定 N)

**每批公共模板** (复制 N 份, 替换 `vB.X`):

### Task B.1: <功能>

- Files:
  - Create: `dev/scripts/<script>.py`, `stage_vB.1_<output>.md`
  - Modify: `_progress.json`, `trace.jsonl`, `upload_manifest.md`
- [ ] Step 1: executor subagent 写脚本 + 跑脚本
- [ ] Step 2: reviewer subagent 独立复核
- [ ] Step 3: 主控 N 样本抽检 (规则 A)
- [ ] Step 4: 用户 A/B 回归 (触发 hard checkpoint)
- [ ] Step 5: 更新 _progress + trace + manifest

**Checkpoint 级别**: **hard** (用户 A/B ack)

**规则 A 触发**: 压缩率 > 50%? Y → reviewer 抽 N=10 disjoint + 主控抽 N=5 独立

**失败处理**: 如 A/B 衰减 ≥2 题, 走 P10 → archive failures → reviewer 归因 → 用户决策 continue/rollback

---

## §5 Phase G: 终态 A/B 整合回归

一次性跑完整 A/B 矩阵, 验证所有批次累积后无跨批 regression.

- [ ] Step G1: 跑 T1-T<N> 全矩阵
- [ ] Step G2: 对比 v<prev> 每题答案 (质量 ↑ / 持平 / ↓)
- [ ] Step G3: 写 `ab_reports/STAGE_FINAL_AB_REPORT.md`
- [ ] Step G4: **独立 reviewer 复核** (规则 D)

**Checkpoint 级别**: **hard**

---

## §6 Phase H: 收束

按 `09_closure.md` 执行收束三件套 + reorg + 上游更新.

- [ ] Task H1: RETROSPECTIVE.md (规则 C, 三段式)
- [ ] Task H2: handoff.md (如有下游)
- [ ] Task H3: UPLOAD_TUTORIAL.md (10 章节)
- [ ] Task H4: Reorg 目录到四层
- [ ] Task H5: 更新上游索引 + CLAUDE.md + MANIFEST + PROGRESS
- [ ] Task H6: Commit + push

**Checkpoint 级别**: **hard** (H1 和 H6 各一次)

---

## §7 (可选) Subagent 模板预写

Tier 3 项目建议. 每类 subagent 调用的 prompt template 预写到 `dev/evidence/subagent_prompts/templates/`:

- `executor_writer_template.md` — 写脚本 / 产物 类型
- `reviewer_template.md` — 独立复核 类型
- `main_audit_template.md` — 主控 N 样本抽检

Tier 1/2 可跳过, 边用边写即可.

---

## §8 (可选) 失败/退化应急预案

列出**本平台已知** + **本次预判**的失败模式, 对应应急响应:

| 失败模式 | 触发信号 | 响应 |
|---------|---------|------|
| A/B 衰减 ≥2 题 | P10 触发 | 立即停, reviewer 归因, 用户决策 |
| capacity 超预算 | 某批 token 超 PLAN 目标 | 看是否内部冗余, 优先降冗余 |
| reviewer PASS 但主控抽样 FAIL | 规则 A 结果冲突 | 尊重主控 (v1 G1 教训), 重试 |
| Hard checkpoint 等用户 > 24h | 用户未 ack | `_progress.json.status = paused`, 不推进 |
| 源文件污染检测 | `git status knowledge_base/` 非 clean | **立即回滚**, 走 P5 调查 |

---

## 填写示例: Claude Projects v2 (已做, 供对照)

见 `claude_projects/docs/PLAN_V2.md` 实际执行的 PLAN. 典型结构:
- §0 修订记录: v1 初版 + 2 次调研后修订
- §1: P1-P10 + 规则 A/B/C/D
- §2: 完整文件 map + 8 个脚本职责
- §3-§6: Phase A setup + Phase B-F 五批 (v2.1-v2.5) + Phase G 终态 + Phase H 收束
- 总行数 ~1852 行 (Tier 3 规模)

---

*来源: claude_projects/docs/PLAN_V2.md §0-§H 结构抽象 + v1 G4 "checkpoint 级别隐式" 教训.*
