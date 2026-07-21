# Phase 6.5 Claude Project — v2 扩容实施计划 (PLAN_V2)

> ⚠️ **Post-reorg note (2026-04-20 晚)**: 本计划在 reorg 前写就, 内部所有 `output_v2/...`, `scripts_v2/...`, `evidence_v2/...`, `RETROSPECTIVE_V2.md`, `capacity_research.md` 等路径引用为**历史执行语境**, 未随 reorg 更新. 当前实际路径映射:
>   - `output_v2/*.md` (上传文件) → `current/uploads/*.md`
>   - `output_v2/system_prompt_v2.md` → `current/system_prompt.md`
>   - `output_v2/upload_manifest_v2.md` → `current/upload_manifest.md`
>   - `output_v2/evidence_v2/*` → `dev/evidence/*`
>   - `output_v2/STAGE_V2.*_AB_REPORT.md` → `dev/ab_reports/`
>   - `output_v2/CHECKPOINT_V2.*_HANDOFF.md` → `dev/checkpoints/`
>   - `output_v2/rag_decay_curve.md` → `docs/rag_decay_curve.md`
>   - `output_v2/phase7_handoff.md` → `docs/phase7_handoff.md`
>   - `output_v2/test_results_v2.md` → `dev/test_results.md`
>   - `scripts_v2/*.py` → `dev/scripts/*.py`
>   - `RETROSPECTIVE_V2.md` → `docs/RETROSPECTIVE_V2.md`
>   - `capacity_research.md` → `docs/capacity_research.md`
> 详见 [README.md](../README.md) 和 [dev/README.md](../dev/README.md).

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 Claude Project 从 v1 (192K, 12% capacity) 扩容到 v2.5 (~1.3-1.5M, ~50% capacity), 通过 5 批渐进 + A/B 测试建立 RAG 质量 vs 规模曲线, 不衰减 v1 已 PASS 的 T1-T8。

**Architecture:** 5 批渐进上传 (chapters 全展开 → examples 高频 → examples 全 → terminology 高频 → terminology mid), 每批由 executor subagent 写脚本 + code-reviewer 独立复核 + 主控独立抽样 + 用户在第二个 Claude Project 做 A/B 回归。v1 11 文件 archive 到 output_v1_baseline/, v2 在 output_v2/ 滚动构建。

**Tech Stack:** Python 3 + tiktoken (cl100k_base) + git + Claude.ai Project Knowledge (RAG) + 主控 Opus + executor/reviewer subagent 模板 (沿用 v1 PLAN §7.2-7.3)

**上游设计**: `docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md`

**v1 参照**: `ai_platforms/claude_projects/PLAN.md` (尤其 §7 Claude Code 执行手册)

---

## 0. 修订记录

| 版本 | 日期 | 变更 |
|------|------|------|
| v1 | 2026-04-18 晚 | 中庸-事实修正版, 5 批 / 16-18 文件 / ~50% 容量 |

---

## 1. 强制遵守的执行规则

继承 v1 PLAN.md §7.1 全部规则 (P1-P7) + 全局 CLAUDE.md 四条 (规则 A/B/C/D), 本计划进一步强化:

| # | 规则 | 适用 |
|---|------|------|
| P1 | 量化 PASS 标准 | 每 Step 完成必打印 `[Stage X.Y] <file>: <tokens> tokens (target ≤<X>K)` |
| P2 | 写/审分离 (规则 D) | executor 与 code-reviewer 必不同 subagent_type, model 都用 opus |
| P3 | AI 估算值标记 | manifest 只写实测值, 估算用 `~` 前缀 |
| P4 | 人工抽查 checkpoint | 每个 v2.X 阶段完成都是 hard checkpoint, 不擅自连续推进 |
| P5 | 源文件只读 | knowledge_base/ 不允许 Edit/Write, 只能 Read |
| P6 | subagent 上下文隔离 | 每个脚本独立 executor, 主控不读脚本源 |
| P7 | 进度持久化 | 每 Step 完成立即更新 output_v2/evidence_v2/_progress.json |
| P8 (新) | 失败归档 (规则 B) | failures/stage_v2.X_attempt_M.md 含输入/产物/技术判定/业务判定/下一 attempt 输入 |
| P9 (新) | 语义抽检 (规则 A) | 压缩率 >50% 步骤强制 N=10 样本独立抽检 (reviewer 抽 5 + 主控抽 5, 不重叠), 结果留 evidence_v2/stage_v2.X_audit.md |
| P10 (新) | A/B 衰减强制响应 | T1-T8 衰减 ≥2 题立即停, ≥1 题写 regression evidence + reviewer 归因 |

---

## 2. 文件结构 (实施前先 map)

### 2.1 新建/修改文件总览

**Create:**
- `ai_platforms/claude_projects/output_v1_baseline/` (整个目录, v1 11 文件 archive)
- `ai_platforms/claude_projects/output_v2/` (整个目录, v2 滚动产物)
- `ai_platforms/claude_projects/output_v2/evidence_v2/` (三层 evidence 体系)
- `ai_platforms/claude_projects/scripts_v2/` (新脚本, ~7 个 Python 文件)
- `ai_platforms/claude_projects/RETROSPECTIVE_V2.md` (收尾时写)
- `ai_platforms/claude_projects/PLAN_V2.md` (本文件)

**Modify (during execution):**
- `ai_platforms/claude_projects/output_v2/_progress.json` (每 Step 更新)
- `ai_platforms/claude_projects/output_v2/evidence_v2/trace.jsonl` (append-only)
- `ai_platforms/claude_projects/output_v2/system_prompt_v2.md` (每批后增量修订)
- `ai_platforms/claude_projects/output_v2/upload_manifest_v2.md` (累计 token + 阶段历史)
- `ai_platforms/claude_projects/output_v2/test_results_v2.md` (T1-T20 A/B 矩阵)
- `ai_platforms/claude_projects/output_v2/rag_decay_curve.md` (RAG 质量曲线一等产物)
- `.work/MANIFEST.md` (收尾时注册 output_v2/, scripts_v2/)
- `.work/meta/worklog.md` (收尾时追加)
- `docs/PROGRESS.md` (收尾时更新 Phase 6.5 状态)
- `CLAUDE.md` (收尾时新增 Key Paths 行)

**不动 (强制只读):**
- `knowledge_base/**` (全部, P5)
- `ai_platforms/claude_projects/PLAN.md` (v1)
- `ai_platforms/claude_projects/RETROSPECTIVE.md` (v1)
- `ai_platforms/claude_projects/capacity_research.md`
- `ai_platforms/claude_projects/output/**` (v1, baseline 不动)
- `ai_platforms/claude_projects/scripts/**` (v1)

### 2.2 脚本职责边界

| 脚本 | 职责 (单一) | 输入 | 输出 |
|------|------------|------|------|
| `count_tokens.py` (v1 已有, 复用) | 测 token | 任意 .md 文件或目录 | stdout 行 `<file>: <N> tokens` |
| `score_domains.py` (新) | 圈定批 2 高频域 | knowledge_base/ + 用户 20 域清单 | stdout 行 `<domain>: <score>`, top 25-28 |
| `score_codelists.py` (新) | 圈定批 4/5 codelist | knowledge_base/terminology/ | stdout 行 `<codelist>: <score>`, top 200 / 200-500 |
| `rebuild_chapters_full.py` (新) | 批 1 chapters 全展开 | knowledge_base/chapters/*.md | output_v2/02_chapters.md |
| `extract_examples_data.py` (新, 参数化) | 批 2/3 examples 数据表 | knowledge_base/domains/*/examples.md + 域清单 | output_v2/09_examples_data_high.md or 10_examples_data_others.md |
| `extract_terminology_terms.py` (新, 参数化) | 批 4/5 terminology Term 值 | knowledge_base/terminology/**/*.md + codelist 清单 | output_v2/11_terminology_high.md or 12_terminology_mid.md |
| `build_v2_stage.py` (新) | 分阶段构建 + 累计 token + 写 manifest | --stage v2.1/.../v2.5 | output_v2/upload_manifest_v2.md |
| `compare_versions.py` (新, 可选) | A/B token 对比 | output/, output_v2/ | stdout 对比表 |

---

## 3. Phase A: Setup (一次性, 3 任务)

### Task A1: 归档 v1 baseline

**Files:**
- Create: `ai_platforms/claude_projects/output_v1_baseline/` (目录)
- Create: `ai_platforms/claude_projects/output_v1_baseline/README.md`

- [ ] **Step 1: 创建 baseline 目录**

```bash
mkdir -p /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v1_baseline
```

- [ ] **Step 2: 复制 v1 11 文件 (其余非 .md 不复制)**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
cp output/00_routing.md output/01_index.md output/02_chapters.md output/03_model.md output/04_variable_index.md output/05_mega_spec.md output/06_assumptions.md output/07_examples_catalog.md output/08_terminology_map.md output/system_prompt.md output/upload_manifest.md output_v1_baseline/
```

- [ ] **Step 3: 验证 md5 一致 (10 文件 ×2 行)**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
for f in 00_routing 01_index 02_chapters 03_model 04_variable_index 05_mega_spec 06_assumptions 07_examples_catalog 08_terminology_map system_prompt; do
  a=$(md5 -q output/${f}.md)
  b=$(md5 -q output_v1_baseline/${f}.md)
  [ "$a" = "$b" ] && echo "PASS $f" || echo "FAIL $f"
done
```

Expected: 10 行全部 `PASS`.

- [ ] **Step 4: 写 baseline README**

```bash
cat > output_v1_baseline/README.md <<'EOF'
# v1 Baseline (只读)

> 本目录是 Phase 6.5 v1 的 11 文件冷藏版, 对应**第一个**已上传的 Claude Project ("SDTM-Knowledge-v1" 或类似命名)。
>
> **不要修改本目录任何文件。**
>
> 用途:
> 1. v2 任何阶段失败时的回退源 (md5 与 output/ 一致)
> 2. A/B 测试时与 v2 对照 (用户在两个 Claude Project 间切换)
> 3. v1 设计的可追溯证据
>
> 对应文档:
> - `../PLAN.md` v1 实施计划
> - `../RETROSPECTIVE.md` v1 复盘
> - `../output/upload_manifest.md` v1 实测 token + 阶段记录
EOF
```

- [ ] **Step 5: Commit**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/claude_projects/output_v1_baseline/
git commit -m "Phase 6.5 v2 Setup A1: 归档 v1 baseline (11 文件 + README)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task A2: 创建 output_v2/ + scripts_v2/ + evidence_v2/ 骨架

**Files:**
- Create: `ai_platforms/claude_projects/output_v2/` 及子目录
- Create: `ai_platforms/claude_projects/scripts_v2/` 及子目录
- Create: 6 个空骨架文件

- [ ] **Step 1: 创建目录骨架**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
mkdir -p output_v2/evidence_v2/{checkpoints,subagent_prompts,failures,rag_decay_observations}
mkdir -p scripts_v2
```

- [ ] **Step 2: 复制 v1 不变文件到 output_v2/ (9 个 + system_prompt 模板)**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
cp output/00_routing.md output/01_index.md output/03_model.md output/04_variable_index.md output/05_mega_spec.md output/06_assumptions.md output/07_examples_catalog.md output/08_terminology_map.md output_v2/
cp output/system_prompt.md output_v2/system_prompt_v2.md
ls output_v2/*.md | wc -l
```

Expected: `9` (8 v1 不变 + 1 system_prompt_v2 起始版)
说明: 02_chapters.md 不复制, 由批 1 生成。

- [ ] **Step 3: 写 evidence_v2/README.md**

```bash
cat > output_v2/evidence_v2/README.md <<'EOF'
# v2 Evidence 三层体系

| 层 | 文件 | 写入频率 |
|----|------|---------|
| L1 状态 | `_progress.json` | 每 Step 完成 |
| L2 轨迹 | `trace.jsonl` (append-only) | 每事件实时 |
| L3 证据 | `stage_v2.X_*.md`, `batch_NN_*.md` | 每 Stage/Batch 完成 |

子目录:
- `checkpoints/` 用户互动归档
- `subagent_prompts/` 完整 prompt 归档 (executor + reviewer)
- `failures/` 失败 attempt 归档 (规则 B 强制)
- `rag_decay_observations/` 每阶段 RAG 衰减观察

参照: v1 `output/evidence/README.md` 同结构 + PLAN_V2.md §1 P1-P10
EOF
```

- [ ] **Step 4: 初始化 _progress.json**

```bash
cat > output_v2/evidence_v2/_progress.json <<'EOF'
{
  "phase": "6.5-claude-v2",
  "plan": "ai_platforms/claude_projects/PLAN_V2.md",
  "design": "docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md",
  "current_stage": "v2.0-setup",
  "current_batch": null,
  "completed_stages": [],
  "completed_batches": [],
  "checkpoints_acked": [],
  "v1_baseline": "ai_platforms/claude_projects/output_v1_baseline/",
  "started_at": "2026-04-18T00:00:00Z",
  "last_updated": "2026-04-18T00:00:00Z"
}
EOF
```

- [ ] **Step 5: 初始化 trace.jsonl (写一行 phase_init)**

```bash
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"phase_init\",\"phase\":\"6.5-claude-v2\",\"plan\":\"PLAN_V2.md\"}" > output_v2/evidence_v2/trace.jsonl
```

- [ ] **Step 6: 初始化 upload_manifest_v2.md (空表头)**

```bash
cat > output_v2/upload_manifest_v2.md <<'EOF'
# v2 上传清单 + 阶段历史

> 自动维护 by `scripts_v2/build_v2_stage.py`
> 每阶段完成后追加一行

## 当前状态
- 阶段: v2.0-setup
- 文件数: 9 (v1 不变 8 + system_prompt_v2)
- 总 tokens: TBD (Stage v2.1 起测)

## 阶段历史

| 阶段 | 完成日期 | 文件数 | 总 tokens | 与 v1 对比 | 备注 |
|------|---------|-------|----------|-----------|------|

## 当前 v2 文件清单 (随阶段更新)

| 文件 | 来源 | tokens | 阶段产出 |
|------|------|--------|---------|
EOF
```

- [ ] **Step 7: 初始化 test_results_v2.md (T1-T20 占位)**

```bash
cat > output_v2/test_results_v2.md <<'EOF'
# v2 A/B 测试结果矩阵

> 用户每阶段后回填; 主控写入并归档到 evidence_v2/stage_v2.X_audit.md

## T1-T8 回归 (源自 v1)

| # | 题目 | 期望 | v1 答案 | v2.X 答案 | 精度 | 阶段 |
|---|-----|------|--------|----------|------|------|
| T1 | AE.AEDECOD 的 Core 属性是什么? | Expected | TBD | TBD | TBD | TBD |
| T2 | AE 严重程度变化如何记录? | AEGRPID 方案 | TBD | TBD | TBD | TBD |
| T3 | PC↔PP 通过 RELREC 关联的 4 种方法? | Method A-D | TBD | TBD | TBD | TBD |
| T4 | 哪些域有 EPOCH 变量? | 完整列表 | TBD | TBD | TBD | TBD |
| T5 | 如何判断变量是否需要提交到 SUPP--? | ch08 §8.4 规则 | TBD | TBD | TBD | TBD |
| T6 | AE Example 2 的具体数据是什么? | 数据表 | TBD | TBD | TBD | TBD |
| T7 | CT Code C66742 有哪些具体值? | 完整 Term 表 | TBD | TBD | TBD | TBD |
| T8 | CV 域所有变量值范围? | "需查 examples/terminology" | TBD | TBD | TBD | TBD |

## T9-T20 新增 (覆盖 v2 五批)

| # | 批 | 题目 | 期望 | v1 答案 | v2.X 答案 | 精度 |
|---|----|-----|------|--------|----------|------|
| T9  | 1 | ch01 SDTM 整体架构 + Foundational concepts? | 完整段落 | (FAIL 期望) | TBD | TBD |
| T10 | 1 | ch02 §2.6 创建新 domain 的所有步骤? | 完整列表 | (FAIL 期望) | TBD | TBD |
| T11 | 1 | ch08 §8.3 RELREC 数据集关系示例完整流程? | 完整规则+示例 | TBD | TBD | TBD |
| T12 | 1 | ch10 附录所有 entity 列表? | 完整 | (FAIL 期望) | TBD | TBD |
| T13 | 2 | DM 的 Example 1 完整数据表? | 表格 | (兜底模板) | TBD | TBD |
| T14 | 2 | EX 剂量调整 Example 数据怎么写? | 表格 | (兜底) | TBD | TBD |
| T15 | 3 | RP 域 Example 数据? | 表格 | (兜底) | TBD | TBD |
| T16 | 3 | FT 域 Example 数据? | 表格 | (兜底) | TBD | TBD |
| T17 | 4 | C66742 codelist 所有 Term 值 + Definition? | 完整 Term 表 | (兜底) | TBD | TBD |
| T18 | 4 | AERELN codelist 全部 Synonyms? | Synonyms 字段 | TBD | TBD | TBD |
| T19 | 5 | FREQ codelist (中频) 全部 Term + Code? | 表格 | TBD | TBD | TBD |
| T20 | 5 | PROBLEM_TYPE codelist (中频) 全部值? | 表格 | TBD | TBD | TBD |

## 阶段汇总

(每阶段完成后追加一段)
EOF
```

- [ ] **Step 8: 初始化 rag_decay_curve.md**

```bash
cat > output_v2/rag_decay_curve.md <<'EOF'
# RAG 质量 vs 规模曲线 (Phase 6.5 v2 一等产物)

> 目标: 建立 Claude Project RAG 质量随集合规模变化的曲线
> 用途: Phase 7 RAG 拓扑设计参考 + 决定是否在 Phase 6.5+ 推到 70%
> 触发: capacity_research §6.3 第 2 条疑点 ("RAG 检索质量随集合增大如何衰减?" 未实测)

## 数据点

| 阶段 | tokens | 文件数 | Capacity % (UI 实测) | T1-T8 PASS | T9-T20 PASS | 平均答题精度 (主控判) |
|------|-------|-------|---------------------|-----------|-----------|----------------------|
| v1   | 192,036 | 11 | 12% | 8/8 | N/A | baseline |
| v2.1 | TBD | 11 | TBD | TBD | T9-T12 TBD | TBD |
| v2.2 | TBD | 12 | TBD | TBD | T13-T14 TBD | TBD |
| v2.3 | TBD | 13-14 | TBD | TBD | T15-T16 TBD | TBD |
| v2.4 | TBD | 14-17 | TBD | TBD | T17-T18 TBD | TBD |
| v2.5 | TBD | 16-19 | TBD | TBD | T19-T20 TBD | TBD |

## 观察

(每阶段后追加 1-3 句关键观察)

## 结论 (终态后填)

- v2 终态推到 X% 的 RAG 质量是否仍 PASS?
- 衰减拐点 (如有) 在 ~Y% capacity?
- 对 Phase 7 的 actionable insight?
EOF
```

- [ ] **Step 9: Commit setup A2**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/claude_projects/output_v2/ ai_platforms/claude_projects/scripts_v2/
git commit -m "Phase 6.5 v2 Setup A2: 创建 output_v2/scripts_v2/evidence_v2 骨架

- output_v2/ 含 9 个 v1 不变文件 + 5 份元文档骨架
- evidence_v2/ 三层体系初始化 (_progress.json + trace.jsonl + 4 子目录)
- rag_decay_curve.md 作为一等产物启动

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task A3: 验证 v1 不变文件 md5 一致

**Files:**
- Test only

- [ ] **Step 1: 8 个 v1 复制文件 md5 比对**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
for f in 00_routing 01_index 03_model 04_variable_index 05_mega_spec 06_assumptions 07_examples_catalog 08_terminology_map; do
  a=$(md5 -q output/${f}.md)
  b=$(md5 -q output_v2/${f}.md)
  [ "$a" = "$b" ] && echo "PASS $f" || { echo "FAIL $f"; exit 1; }
done
```

Expected: 8 行全部 `PASS`. 任一 FAIL 立即停, 检查 cp 操作。

- [ ] **Step 2: 写 evidence stage_v2.0_setup.md**

```bash
cat > output_v2/evidence_v2/stage_v2.0_setup.md <<'EOF'
# Stage v2.0 — Setup

> 完成日期: 2026-04-18
> Tasks: A1-A3

## 输入
- v1 baseline (output/ 11 文件, md5 全部记录在 _progress.json)
- knowledge_base/ (只读)

## 产出
- output_v1_baseline/ 11 文件 (md5 与 output/ 一致, A1 Step 3 验证)
- output_v2/ 9 文件 (8 v1 不变 + 1 system_prompt_v2 起始版)
- output_v2/evidence_v2/ 三层体系骨架
- 5 份元文档骨架 (upload_manifest_v2 / test_results_v2 / rag_decay_curve / evidence/README / _progress.json)

## 复核
- A3 Step 1 md5 PASS (8/8)

## 偏差
无

## Checkpoint
无 (Setup 阶段)

## 下一步
进入 Phase B (Tooling) Task B1: 验证 count_tokens.py 复用
EOF
```

- [ ] **Step 3: 更新 _progress.json**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
python3 -c "
import json, datetime
p = json.load(open('output_v2/evidence_v2/_progress.json'))
p['current_stage'] = 'v2.0-setup-done'
p['completed_stages'].append('v2.0-setup')
p['last_updated'] = datetime.datetime.utcnow().isoformat() + 'Z'
json.dump(p, open('output_v2/evidence_v2/_progress.json', 'w'), indent=2)
print('progress updated')
"
```

- [ ] **Step 4: trace.jsonl 写 stage_done**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"stage_done\",\"stage\":\"v2.0-setup\",\"status\":\"PASS\"}" >> output_v2/evidence_v2/trace.jsonl
```

- [ ] **Step 5: Commit + checkpoint**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/claude_projects/output_v2/evidence_v2/
git commit -m "Phase 6.5 v2 Setup A3: 验证 + stage v2.0 done

- 8 个 v1 复制文件 md5 验证 PASS
- evidence stage_v2.0_setup.md 归档

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

**主控 Checkpoint (soft)**: 向用户汇报 "Setup 完成, 进入 Tooling 阶段?" — 等用户 ack 后进 Phase B (本计划允许预授权连续推进 Setup→Tooling, 见 §8 预授权约定)

---

## 4. Phase B: Tooling (5 任务, 复用 v1 count_tokens + 4 个新脚本骨架)

### Task B1: 验证 count_tokens.py 复用

**Files:**
- Test only (v1 脚本不修改)

- [ ] **Step 1: 跑 v1 count_tokens 测 v1 文件**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
python3 scripts/count_tokens.py output_v2/00_routing.md
```

Expected: 输出 `output_v2/00_routing.md: 2657 tokens` (与 v1 manifest 一致)

- [ ] **Step 2: 测一个 v1 不变文件累计**

```bash
python3 scripts/count_tokens.py output_v2/
```

Expected: 9 行各文件 token + 1 行 TOTAL ≈ 192K - (02_chapters 31K) - (system_prompt 重命名 ~5K) = ~156K (因为缺 02_chapters)

- [ ] **Step 3: trace + commit**

```bash
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"step_done\",\"task\":\"B1\",\"status\":\"PASS\"}" >> output_v2/evidence_v2/trace.jsonl

cd /Users/bojiangzhang/MyProject/SDTM-compare
# 无文件变更, 仅 trace 更新
git add ai_platforms/claude_projects/output_v2/evidence_v2/trace.jsonl
git commit -m "Phase 6.5 v2 B1: count_tokens 复用 PASS

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task B2: 写 score_domains.py (批 2 圈定打分工具)

**Files:**
- Create: `scripts_v2/score_domains.py`
- Test: 主控直接 Bash 跑 + 验证输出

**Agent 调度**: subagent_type=`oh-my-claudecode:executor` model=opus

**Subagent prompt 模板** (落盘到 `evidence_v2/subagent_prompts/B2_executor.md` 再调):

```
## 上下文
你正在执行 SDTM Phase 6.5 v2 扩容的 Task B2 (PLAN_V2.md §4 Task B2)。
完整设计见 docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md §2.3。

## 你的任务
写 ai_platforms/claude_projects/scripts_v2/score_domains.py, 圈定批 2 高频域。

## 算法
score = 0.4 * normalize(cross_ref_count)   # VARIABLE_INDEX.md 中该域被引用次数
      + 0.4 * normalize(examples_tokens)    # domains/<X>/examples.md 文件 token 数
      + 0.2 * (20 if domain in T_test_hits else 0)

T_test_hits = ["AE", "PC", "PP", "EX", "MH", "LB"]

## 输入
- knowledge_base/VARIABLE_INDEX.md (cross_ref 来源)
- knowledge_base/domains/*/examples.md (token 数来源, 用 tiktoken cl100k_base)
- 用户必选 20 域: DM, SE, DS, BS, BE, MI, GF, PR, CM, EX, TU, TR, RS, SS, DD, LB, FA, CE, MH, SU

## 产出
- scripts_v2/score_domains.py (CLI: python score_domains.py)
- stdout 格式 (按 score 降序):
  ```
  # 必选域 (用户清单 + T_test_hits)
  DM: must (user)
  SE: must (user)
  ...
  AE: must (T_test_hits)
  PC: must (T_test_hits)
  ...
  # 打分排序 (除必选外, top 20)
  VS: 0.78
  EG: 0.75
  ...
  # 推荐合并清单 (必选 + top N 直至总数 25-28):
  [DM, SE, DS, BS, BE, MI, GF, PR, CM, EX, TU, TR, RS, SS, DD, LB, FA, CE, MH, SU, AE, PC, PP, VS, EG, IE, QS, EX]
  ```

## 强制要求
- 只读 knowledge_base/
- 脚本可重复执行 (idempotent), 同输入同输出
- 必须解释 normalize 算法 (min-max 还是 z-score?)
- 用 tiktoken cl100k_base (与 v1 一致)

## 完成标准
脚本跑通, stdout 含三段 (必选/打分/推荐合并), 推荐合并总数 25-28。

## 不要做
- 不要修改 knowledge_base/
- 不要写 .md 文档
- 不要解释做了什么, 只报告结果
```

- [ ] **Step 1: 落盘 subagent prompt**

```bash
mkdir -p /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/output_v2/evidence_v2/subagent_prompts
# (主控用 Write 工具落盘上述 prompt 到 B2_executor.md)
```

- [ ] **Step 2: trace step_start**

```bash
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"step_start\",\"task\":\"B2\",\"agent\":\"executor\",\"model\":\"opus\"}" >> output_v2/evidence_v2/trace.jsonl
```

- [ ] **Step 3: 调 executor subagent (主控)**

主控用 Agent 工具调 oh-my-claudecode:executor (model=opus), prompt 取自 B2_executor.md。

- [ ] **Step 4: 跑 score_domains.py 验证**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
python3 scripts_v2/score_domains.py 2>&1 | tee evidence_v2/B2_score_output.log
```

Expected: stdout 三段, 推荐合并清单总数 25-28。

- [ ] **Step 5: 调 code-reviewer 复核 (独立 subagent)**

主控用 Agent 工具调 oh-my-claudecode:code-reviewer (model=opus), prompt:

```
复核 ai_platforms/claude_projects/scripts_v2/score_domains.py:
1. 读源文件 + 跑一次脚本
2. 验证 (a) 用户 20 域全在必选 (b) T_test_hits 6 域全在必选 (c) 推荐合并总数 25-28
3. 验证 normalize 算法是否合理 (min-max vs z-score, 若用 min-max 是否对极端值敏感?)
4. 验证脚本是否 idempotent (跑两次输出一致)

报告: PASS / FAIL + 关键发现 ≤ 200 字
```

- [ ] **Step 6: 落盘 reviewer prompt + 结果**

```bash
# Write tool 落盘 evidence_v2/subagent_prompts/B2_reviewer.md
# Write tool 落盘 evidence_v2/B2_review.md (reviewer 关键结论)
```

- [ ] **Step 7: trace step_done + commit**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"step_done\",\"task\":\"B2\",\"output\":\"scripts_v2/score_domains.py\",\"status\":\"PASS\"}" >> output_v2/evidence_v2/trace.jsonl

cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/claude_projects/scripts_v2/score_domains.py ai_platforms/claude_projects/output_v2/evidence_v2/
git commit -m "Phase 6.5 v2 B2: score_domains.py + reviewer PASS

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task B3: 写 score_codelists.py (批 4/5 圈定打分工具)

**Files:**
- Create: `scripts_v2/score_codelists.py`

**算法** (同 design §2.5):
```
score = 0.5 * normalize(domain_ref_count)  # 被多少 domain spec.md 引用
      + 0.3 * normalize(term_count)        # codelist 内 Term 数 (中等优先, 太大太小都减分: 用 sigmoid)
      + 0.2 * (50 if codelist in T_codelist_hits else 0)

T_codelist_hits = ["NY" (C66742), "AERELN", "FREQ", "PROBLEM_TYPE"]
```

- [ ] **Step 1-7: 同 B2 模板 (落 prompt → executor → 跑 → reviewer → 落 review → trace + commit)**

复用 B2 流程, 唯独输出 stdout 三段:
- top 200 codelist (批 4 用)
- 200-500 名 codelist (批 5 用)
- 总计 codelist 总数 (验证 ≈ 1005)

主控验证: `python3 scripts_v2/score_codelists.py 2>&1 | tee evidence_v2/B3_score_output.log`, expected: 三段 + 总数 ≈ 1005。

Commit 信息:
```
Phase 6.5 v2 B3: score_codelists.py + reviewer PASS

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

---

### Task B4: 写 build_v2_stage.py (分阶段构建工具)

**Files:**
- Create: `scripts_v2/build_v2_stage.py`

**职责**:
- CLI: `python build_v2_stage.py --stage v2.1` (或 v2.2/.../v2.5)
- 负责: (1) 跑当批脚本 (2) 累计 token (3) 修订 system_prompt_v2.md 对应阶段段落 (4) 追加 upload_manifest_v2.md (5) 写 stage_v2.X_*.md evidence (6) 更新 _progress.json (7) trace.jsonl 写事件
- **不**直接调 subagent (主控调), 但提供"模板填充" function 供主控填 reviewer 关键结论

- [ ] **Step 1-7: 同 B2 模板**

主控验证: `python3 scripts_v2/build_v2_stage.py --stage v2.1 --dry-run`, expected: 打印将执行的 8 步, 不实际改文件。

Commit:
```
Phase 6.5 v2 B4: build_v2_stage.py + reviewer PASS

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

---

### Task B5: 写 compare_versions.py (A/B token 对比工具, 可选)

**Files:**
- Create: `scripts_v2/compare_versions.py`

**职责**: CLI `python compare_versions.py output/ output_v2/` 输出对比表 (每文件 token v1 vs v2 + 总量)

- [ ] **Step 1-5: 简化流程 (无 reviewer, 因纯工具)**

主控直接 Bash 跑验证, 跳过 reviewer 调用 (B5 是辅助工具)。

Commit:
```
Phase 6.5 v2 B5: compare_versions.py PASS (辅助工具)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
```

---

## 5. Phase C: Batch 1 — chapters 全展开 (Stage v2.1, 8 任务)

### Task C1: 写 rebuild_chapters_full.py

**Files:**
- Create: `scripts_v2/rebuild_chapters_full.py`
- Output: `output_v2/02_chapters.md`

**算法**:
- 读 6 个章节: ch01/ch02/ch03/ch04/ch08/ch10
- ch04 完整保留 (从 v1 02_chapters 复用 ch04 段, 或从源完整读取)
- ch01/02/03/08/10 完整读取源文件 (撤销 v1 精简)
- 每章节起始加 `<!-- source: knowledge_base/chapters/chXX_*.md -->`
- 输出第一行加 `<!-- generated by scripts_v2/rebuild_chapters_full.py at <ISO timestamp> -->`

**Subagent prompt 模板** (落盘到 `evidence_v2/subagent_prompts/C1_executor.md`):

```
## 上下文
SDTM Phase 6.5 v2 扩容 Task C1 (PLAN_V2.md §5)。
完整设计见 design doc §2.2。

## 任务
写 ai_platforms/claude_projects/scripts_v2/rebuild_chapters_full.py。

## 输入
- knowledge_base/chapters/ch01_introduction.md (102 行)
- knowledge_base/chapters/ch02_fundamentals.md (174 行)
- knowledge_base/chapters/ch03_submitting_data.md (130 行)
- knowledge_base/chapters/ch04_general_assumptions.md (1395 行) - 完整保留
- knowledge_base/chapters/ch08_relationships.md (439 行)
- knowledge_base/chapters/ch10_appendices.md (310 行)

## 产出
- output_v2/02_chapters.md (替换 v1 版)
- 软目标 ≤ 90K tokens
- 硬上限 110K tokens

## 算法
1. 文件第一行: `<!-- generated by scripts_v2/rebuild_chapters_full.py at <ISO ts> -->`
2. 第二行: `# SDTMIG v3.4 - Chapters (v2 Full)`
3. 按 ch01 → ch02 → ch03 → ch04 → ch08 → ch10 顺序
4. 每章节前加 `<!-- source: knowledge_base/chapters/chXX_*.md -->`
5. 章节内容: 完整源文件内容 (不删任何段落)
6. 章节间用 `\n---\n` 分隔
7. 末尾用 count_tokens.py 测产出, 打印 `[C1 DONE] 02_chapters.md: <N> tokens (target ≤90K)`

## 强制要求
- 源只读
- 幂等 (跑两次输出 byte 一致)
- 用 tiktoken 测 token

## 完成标准
- 文件生成
- 6 chapters 全部出现 (grep `<!-- source:` 必有 6 行)
- token ≤ 110K (硬上限)

## 不要做
- 不要写文档
- 不要解释做了什么
```

- [ ] **Step 1: 落盘 prompt + trace step_start**

```bash
# Write tool 落盘 evidence_v2/subagent_prompts/C1_executor.md
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"step_start\",\"task\":\"C1\",\"batch\":1,\"stage\":\"v2.1\",\"agent\":\"executor\",\"model\":\"opus\"}" >> output_v2/evidence_v2/trace.jsonl
```

- [ ] **Step 2: 调 executor subagent**

主控 Agent 工具调 oh-my-claudecode:executor model=opus

- [ ] **Step 3: 跑脚本验证 token + 6 chapter 覆盖**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
python3 scripts_v2/rebuild_chapters_full.py
TOKENS=$(python3 scripts/count_tokens.py output_v2/02_chapters.md | awk '{print $NF}' | head -1)
SOURCES=$(grep -c "^<!-- source:" output_v2/02_chapters.md)
echo "tokens=$TOKENS, sources=$SOURCES"
[ "$SOURCES" = "6" ] && echo "C3 PASS (6 sources)" || echo "C3 FAIL"
[ "$TOKENS" -le 110000 ] && echo "C11 PASS (≤110K)" || echo "C11 FAIL"
```

Expected: `C3 PASS` + `C11 PASS`

- [ ] **Step 4: C4 检查 - ch04 字符数 ≥ 源 95%**

```bash
SRC=$(wc -c < /Users/bojiangzhang/MyProject/SDTM-compare/knowledge_base/chapters/ch04_general_assumptions.md)
DST=$(awk '/<!-- source:.*ch04/,/<!-- source:.*ch08/' output_v2/02_chapters.md | wc -c)
RATIO=$(python3 -c "print(round($DST / $SRC * 100, 1))")
echo "ch04 ratio=$RATIO%"
python3 -c "exit(0 if $DST / $SRC >= 0.95 else 1)" && echo "C4 PASS" || echo "C4 FAIL"
```

Expected: `C4 PASS` (ratio ≥ 95%)

- [ ] **Step 5: C3 (chapters 撤销精简) 检查 - 5 个非-ch04 chapter 字符数 ≥ 源 90%**

```bash
for ch in ch01_introduction ch02_fundamentals ch03_submitting_data ch08_relationships ch10_appendices; do
  SRC=$(wc -c < /Users/bojiangzhang/MyProject/SDTM-compare/knowledge_base/chapters/${ch}.md)
  # 提取该 chapter 段
  DST=$(awk -v ch="${ch}" '$0 ~ "<!-- source:.*"ch {found=1; next} /^<!-- source:/ && found {exit} found' output_v2/02_chapters.md | wc -c)
  python3 -c "import sys; sys.exit(0 if $DST / $SRC >= 0.9 else 1)" && echo "PASS ${ch}" || echo "FAIL ${ch} (ratio=$(python3 -c 'print(round('$DST'/'$SRC'*100,1))')%)"
done
```

Expected: 5 行全 `PASS`. 任一 FAIL 写 failures/stage_v2.1_attempt_M.md, 回 executor 调整。

- [ ] **Step 6: C5 (ch08 §8.3/§8.4) 检查**

```bash
GREP_83=$(grep -c "^## 8.3" output_v2/02_chapters.md)
GREP_84=$(grep -c "^## 8.4" output_v2/02_chapters.md)
SUB_83=$(grep -c "^### 8.3" output_v2/02_chapters.md)
SUB_84=$(grep -c "^### 8.4" output_v2/02_chapters.md)
echo "8.3=$GREP_83, 8.4=$GREP_84, sub8.3=$SUB_83, sub8.4=$SUB_84"
[ "$GREP_83" -ge 1 ] && [ "$GREP_84" -ge 1 ] && echo "C5 PASS" || echo "C5 FAIL"
```

Expected: 1+ 个 §8.3 + 1+ 个 §8.4 + sub-section ≥1.

- [ ] **Step 7: 调 code-reviewer 独立复核**

主控 Agent 工具调 oh-my-claudecode:code-reviewer (model=opus), prompt:

```
复核 ai_platforms/claude_projects/output_v2/02_chapters.md (Phase 6.5 v2 批 1 产出):
1. 抽 5 个章节段落, 与 knowledge_base/chapters/ 对应文件随机比对 5 段, 验证内容一致 (无遗漏/截断)
2. 验证 ch04 与 v1 02_chapters 中 ch04 段一致 (md5 段比较, 或文本 diff 接受换行差异)
3. 验证 token 总数 ≤ 110K
4. 验证 6 个 source 注释块齐全

报告: PASS / FAIL + 抽样发现 ≤ 200 字 + 任何遗漏点 (含具体行号引用)
```

落盘 prompt + reviewer 结论到 evidence_v2/。

- [ ] **Step 8: 主控独立抽样 (规则 A: N=10 样本, reviewer 抽 5 + 主控抽 5 不重叠)**

主控随机选 5 个章节段落 (与 reviewer 抽样不同), Read 源 + Read 产出, 比对内容。落盘到 evidence_v2/stage_v2.1_audit.md, 8 节模板:

```markdown
# Stage v2.1 Audit (规则 A 强制)

## 1. 输入
- 6 章节源 (md5 各 1 行)

## 2. Agent 调度
- executor: subagent_prompts/C1_executor.md
- reviewer: subagent_prompts/C1_reviewer.md

## 3. 产出
- output_v2/02_chapters.md = <N> tokens (target ≤90K, 偏差 <X>%)
- 6 source 注释块: 全有

## 4. Reviewer 抽样 (5 段)
- ch01 §1.2 - 与源一致 ✓
- ch02 §2.5 - 与源一致 ✓
- (3 段省略)

## 5. 主控独立抽样 (5 段, 与 reviewer 不重叠)
- ch01 §1.4 - 与源一致 ✓
- ch08 §8.3.1 - 与源一致 ✓
- (3 段省略)

## 6. 偏差与处理
无 / <若有, 列出>

## 7. 累计指标
- 累计 token: <X>
- 累计文件数: <N>

## 8. 下一步
进 Task C2 (build_v2_stage.py 跑 v2.1 阶段聚合)
```

- [ ] **Step 9: trace + commit**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"step_done\",\"task\":\"C1\",\"output\":\"output_v2/02_chapters.md\",\"tokens\":<N>,\"target\":110000,\"status\":\"PASS\"}" >> output_v2/evidence_v2/trace.jsonl

cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/claude_projects/scripts_v2/rebuild_chapters_full.py ai_platforms/claude_projects/output_v2/02_chapters.md ai_platforms/claude_projects/output_v2/evidence_v2/
git commit -m "Phase 6.5 v2 C1: 02_chapters.md 全展开 (<N> tokens, 6 chapters PASS)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task C2: build_v2_stage.py 跑 stage v2.1

**Files:**
- Modify: `output_v2/system_prompt_v2.md` (v2.1 段落)
- Modify: `output_v2/upload_manifest_v2.md` (追加 v2.1 行)
- Modify: `output_v2/evidence_v2/_progress.json`
- Create: `output_v2/evidence_v2/stage_v2.1_chapters.md`

- [ ] **Step 1: 跑 build_v2_stage.py --stage v2.1**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
python3 scripts_v2/build_v2_stage.py --stage v2.1 2>&1 | tee evidence_v2/C2_build_output.log
```

Expected: stdout 含
- "[Stage v2.1] 02_chapters.md: <N> tokens"
- "[Stage v2.1] Total v2.1: <M> tokens (target ~270K)"
- "[Stage v2.1] system_prompt_v2.md updated"
- "[Stage v2.1] upload_manifest_v2.md row added"
- "[Stage v2.1] _progress.json updated"

- [ ] **Step 2: 验证 system_prompt_v2.md v2.1 修订**

```bash
grep -A 2 "v2.1" output_v2/system_prompt_v2.md | head -10
```

Expected: 含 "02_chapters 已是完整版" + "ch08 §8.3/§8.4 等含 RELREC + SUPP-- 完整规则" 句

- [ ] **Step 3: 验证 upload_manifest_v2.md 追加 v2.1 行**

```bash
grep "v2.1" output_v2/upload_manifest_v2.md
```

Expected: 1 行含 v2.1 阶段实测 token + 文件数 11 + 与 v1 对比 (差量约 +75K)

- [ ] **Step 4: trace stage_done + commit**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"stage_done\",\"stage\":\"v2.1\",\"total_tokens\":<M>,\"files\":11,\"status\":\"PASS\"}" >> output_v2/evidence_v2/trace.jsonl

cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/claude_projects/output_v2/
git commit -m "Phase 6.5 v2 C2: stage v2.1 build done (<M> tokens, 11 files)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task C3: ⚠️ HARD CHECKPOINT - v2.1 用户上传 + A/B 测试

**主控行为**: 停下, 向用户汇报 + 等待操作回报。

- [ ] **Step 1: 主控汇报 (使用模板)**

```
=== Hard Checkpoint @ Stage v2.1 ===
本阶段产出: output_v2/02_chapters.md = <N> tokens (target ≤90K) [PASS]
累计文件数: 11 (与 v1 一致, 因替换非新增)
累计 token: <M> tokens (target ~270K, 实测偏差 <±10%)

Layer 1 自动检查: C2/C3/C4/C5/C11 全 PASS

变更对比 v1:
- 02_chapters.md: 31K (v1) → <N>K (v2.1, +X%, 撤销精简 + ch08 §8.3/§8.4 完整)

请你完成以下操作:
1. 在 Claude.ai 新建第二个 Project (建议名: "SDTM-Knowledge-v2")
2. 把 output_v2/system_prompt_v2.md 全文粘贴到 Project Instructions
3. 上传 output_v2/ 下 11 个 .md 文件 (00_routing 到 08_terminology_map + 02_chapters)
4. 等待 indexing 完成 (UI 显示 capacity %)
5. 跑 A/B 测试 12 题 (T1-T12), 把答案粘贴到 v2 Project 的对话, 记录 v1 对应答案
6. 把测试结果按格式回报给我

回报模板:
"v2.1 上传完成, capacity 显示 X%, T1-T12 测试结果如下: ..."

是否准备好执行? 或需要调整?
```

- [ ] **Step 2: 用户回报后, 主控写 checkpoints/ckpt_v2.1.md**

```markdown
# Checkpoint @ Stage v2.1
> 时间: YYYY-MM-DD HH:MM

## 主控汇报 (上面 Step 1 原文)
...

## 用户回应
- 上传 X 文件成功
- Capacity %: <实测>
- T1 答案: ...
- T2 答案: ...
- (T3-T12)

## 决议
- 继续 / 调整 / 暂停: <选>
- 调整内容: <如有>
- 是否产生 regression: <是/否, 若是 regression 题目数 N>
```

- [ ] **Step 3: 主控更新 test_results_v2.md (T1-T12 v2.1 列)**

填入用户回报数据。判定每题精度 (持平/↑/↓)。

- [ ] **Step 4: 主控更新 rag_decay_curve.md (v2.1 行)**

填入 capacity % + T1-T8 PASS 数 + T9-T12 PASS 数。

- [ ] **Step 5: 写 evidence_v2/rag_decay_observations/obs_v2.1.md (1-3 句关键观察)**

```markdown
# Stage v2.1 RAG 观察

- v2.1 实测 capacity: X%
- T1-T8 衰减题数: 0 / 1 / ≥2
- T9-T12 PASS 数: N/4
- 关键观察: <用户/主控 1-3 句, 例如 "T11 ch08 §8.3 引用从 v1 间接重建升级为原文精确, T12 仍弱因 ch10 附录格式 RAG 未抓到">
```

- [ ] **Step 6: 决策分支**

| 用户回应 + 测试结果 | 主控决策 |
|-------------------|---------|
| 全 PASS, 0 衰减, 用户 ack 继续 | 进 Task D1 (批 2) |
| 0 衰减, 但 T9-T12 PASS=0 | 写 failures/stage_v2.1_attempt_2.md, 回 C1 调整算法 (executor 重做) |
| 1 衰减 (T1-T8) | 写 regression evidence, 调 reviewer 归因, **询问用户是否仍进** |
| ≥2 衰减 (T1-T8) | **立即停, 视 v2.1 为 v2 终态, 跳到 Phase H 收尾** |
| 用户疲劳/暂停 | trace.jsonl 写 phase_pause, 等用户重启 |

- [ ] **Step 7: trace checkpoint_ack + commit**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"checkpoint_ack\",\"stage\":\"v2.1\",\"response\":\"<yes/adjust/pause>\",\"regression_count\":<N>}" >> output_v2/evidence_v2/trace.jsonl

cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/claude_projects/output_v2/
git commit -m "Phase 6.5 v2 C3: stage v2.1 checkpoint <ack/decision>

- 用户 capacity 实测: X%
- T1-T8 衰减: N
- T9-T12 PASS: M/4
- 决议: <继续/回退/终止>

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

## 6. Phase D: Batch 2 — examples 高频域数据表 (Stage v2.2, 8 任务)

> 触发条件: Stage v2.1 用户 ack 继续

### Task D1: 跑 score_domains.py + 主控人工 review 名单

- [ ] **Step 1: 跑打分**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
python3 scripts_v2/score_domains.py 2>&1 | tee evidence_v2/D1_domain_score.log
```

- [ ] **Step 2: 主控 review 推荐合并清单**

主控 Read D1_domain_score.log, 验证:
- 用户 20 域全在
- T_test_hits 6 域全在 (AE, PC, PP, EX, MH, LB; 注意 EX/MH/LB 已在用户清单, 实际新增 AE/PC/PP)
- 总数 25-28

如发现关键域漏 (例如 VS/EG 高 score 但未入选), 主控可手动补 1-2 域到清单。

- [ ] **Step 3: 落盘最终域清单到 evidence_v2/D1_domain_list.md**

```markdown
# Stage v2.2 域清单 (批 2 输入)

## 用户 20 必选
DM, SE, DS, BS, BE, MI, GF, PR, CM, EX, TU, TR, RS, SS, DD, LB, FA, CE, MH, SU

## 打分新增 (top N)
AE (must, T_test_hits)
PC (must, T_test_hits)
PP (must, T_test_hits)
VS (score 0.78)
EG (score 0.75)
...

## 主控人工补充
(如有)

## 最终清单 (N 个域)
[完整列表]
```

---

### Task D2: 写 extract_examples_data.py (--tier high 模式)

**Files:**
- Create: `scripts_v2/extract_examples_data.py`
- Output: `output_v2/09_examples_data_high.md`

**Subagent prompt** (落盘 evidence_v2/subagent_prompts/D2_executor.md):

```
## 任务
写 scripts_v2/extract_examples_data.py, 抽取高频域 examples 数据表。

## CLI
python extract_examples_data.py --tier high --domain-list <path>
python extract_examples_data.py --tier others --exclude-list <path>

## 输入 (tier=high)
- evidence_v2/D1_domain_list.md (最终域清单)
- knowledge_base/domains/<X>/examples.md

## 算法
对每个高频域:
1. 读 domains/<X>/examples.md
2. 解析 markdown table 段 (markdown 表格语法识别 | --- |)
3. 保留 Example 标题 (## 或 ### 级别)
4. 保留 Variable Name | Value 双列数据表 (完整)
5. 保留关键 Description (≤2 行, 取第一段)
6. 保留共享 examples 链接 (EX/EC, MB/MS 等, 用 grep 识别"see also"或"shared with")
7. 不保留: 冗长 Description 段, 业务背景叙述

## 产出 (tier=high)
- output_v2/09_examples_data_high.md
- 软目标 ≤30K, 硬上限 50K
- 第一行: `<!-- generated by scripts_v2/extract_examples_data.py --tier high at <ISO ts> -->`
- 每域起始: `<!-- source: knowledge_base/domains/<X>/examples.md -->`
- 域间 `\n---\n` 分隔
- 末尾打印 `[Tier high] 09_examples_data_high.md: <N> tokens (target ≤30K)`

## 强制要求
- 源只读, 幂等
- token 用 tiktoken cl100k_base
- 若 token 超 50K, 主动告警 (退出 1, 让主控决策拆分)

## 不要做
- 不要写文档
- 不要解释
```

- [ ] **Step 1-9: 沿用 C1 模板** (落 prompt → trace → executor → 跑 → reviewer → 主控独立抽样 → trace + commit)

主控验证额外:
```bash
DOMAIN_COUNT=$(grep -c "^### " output_v2/09_examples_data_high.md)
echo "domains in 09: $DOMAIN_COUNT"
[ "$DOMAIN_COUNT" -ge 25 ] && [ "$DOMAIN_COUNT" -le 30 ] && echo "C6 PASS" || echo "C6 FAIL"
```

Expected: 25-28 域 (允许小溢出到 30 因为打分边界)

主控独立抽样 (规则 A): 抽 5 个域不与 reviewer 重叠, Read examples.md 源 + Read 09 产出, 验证 Example 完整性 (Variable + Value 双列对得上)。

Commit:
```
Phase 6.5 v2 D2: 09_examples_data_high.md (<N> tokens, <D> 域)
```

---

### Task D3: build_v2_stage.py 跑 stage v2.2

- [ ] **Step 1-4: 沿用 C2 模板**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
python3 scripts_v2/build_v2_stage.py --stage v2.2 2>&1 | tee evidence_v2/D3_build_output.log
```

system_prompt_v2.md 应新增 v2.2 段: "09_examples_data_high 提供 25-28 高频域数据表; 该域查 example 数据时优先 09"

Commit: `Phase 6.5 v2 D3: stage v2.2 build done (<M> tokens, 12 files)`

---

### Task D4: ⚠️ HARD CHECKPOINT - v2.2 用户上传 + A/B 测试

- [ ] **Step 1-7: 沿用 C3 模板**

主控汇报:
```
=== Hard Checkpoint @ Stage v2.2 ===
本阶段产出: output_v2/09_examples_data_high.md = <N> tokens (target ≤30K) [PASS]
累计文件数: 12 (新增 1)
累计 token: <M> tokens (target ~360K)

请操作:
1. 在 v2 Project 上传 1 个新文件 output_v2/09_examples_data_high.md
2. 系统提示更新 Project Instructions, 复制最新 output_v2/system_prompt_v2.md 全文
3. 等 indexing
4. 跑测试 4 题: T13, T14 (新), + 抽 T1, T11 (回归)
5. 回报
```

A/B 测试 4 题, 决策分支同 C3 Step 6。

Commit: `Phase 6.5 v2 D4: stage v2.2 checkpoint <decision>`

---

## 7. Phase E: Batch 3 — examples 剩余域数据表 (Stage v2.3, 8 任务)

> 触发条件: Stage v2.2 用户 ack 继续

### Task E1: 跑 extract_examples_data.py --tier others

- [ ] **Step 1: 准备 exclude-list (D1 的高频域清单)**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
# 从 D1_domain_list.md 提取最终清单
grep "^[A-Z]\{2,4\}" evidence_v2/D1_domain_list.md | head -30 > evidence_v2/E1_exclude_list.txt
wc -l evidence_v2/E1_exclude_list.txt
```

- [ ] **Step 2: 跑 --tier others (新 executor subagent)**

落盘 prompt evidence_v2/subagent_prompts/E1_executor.md (内容沿用 D2, 但 tier=others, 输出 10_examples_data_others.md)

执行:
```bash
python3 scripts_v2/extract_examples_data.py --tier others --exclude-list evidence_v2/E1_exclude_list.txt
```

- [ ] **Step 3: 验证 token + 域数 + 拆分判定**

```bash
TOKENS=$(python3 scripts/count_tokens.py output_v2/10_examples_data_others.md | awk '{print $NF}')
DOMAINS=$(grep -c "^### " output_v2/10_examples_data_others.md)
echo "tokens=$TOKENS, domains=$DOMAINS"

if [ "$TOKENS" -gt 50000 ]; then
  echo "C7/C11 FAIL - 需拆分 10a/10b"
  # 跑拆分模式
  python3 scripts_v2/extract_examples_data.py --tier others --exclude-list evidence_v2/E1_exclude_list.txt --split-by-class
fi
```

如拆分: 产生 10a_examples_findings.md + 10b_examples_events_interventions.md (按 SDTM Class)

- [ ] **Step 4: C8 (全 63 域) 验证**

```bash
HIGH_DOMAINS=$(grep -c "^### " output_v2/09_examples_data_high.md)
OTHERS_DOMAINS=$(grep -c "^### " output_v2/10_examples_data_others.md output_v2/10a_*.md output_v2/10b_*.md 2>/dev/null | awk -F: '{sum+=$2}END{print sum}')
TOTAL=$((HIGH_DOMAINS + OTHERS_DOMAINS))
echo "high=$HIGH_DOMAINS, others=$OTHERS_DOMAINS, total=$TOTAL"
[ "$TOTAL" = "63" ] && echo "C8 PASS" || echo "C8 FAIL"
```

Expected: total = 63

- [ ] **Step 5-9: reviewer + 主控抽样 + commit (沿用 D2)**

Commit: `Phase 6.5 v2 E1: 10_examples_data_others.md (<N> tokens, <D> 域, 全 63 域 PASS)`

---

### Task E2: build_v2_stage.py --stage v2.3

- [ ] **Step 1-4: 沿用 C2/D3 模板**

system_prompt_v2.md 新增 v2.3 段: "10 (或 10a+10b) 提供其余 ~35 域 examples 数据表; 全 63 域 examples 数据现可命中"

Commit: `Phase 6.5 v2 E2: stage v2.3 build done`

---

### Task E3: ⚠️ HARD CHECKPOINT - v2.3 上传 + 测试

- [ ] **Step 1-7: 沿用 C3/D4 模板**

测试 4 题: T15, T16 (新) + 抽 T6, T13 (回归)

Commit: `Phase 6.5 v2 E3: stage v2.3 checkpoint <decision>`

---

## 8. Phase F: Batch 4 — terminology 高频 codelist Term 值 (Stage v2.4, 9 任务)

### Task F1: 跑 score_codelists.py + 主控 review

- [ ] **Step 1-3: 沿用 D1 模板**

```bash
python3 scripts_v2/score_codelists.py 2>&1 | tee evidence_v2/F1_codelist_score.log
```

主控 review top 200 名单, 必含 T_codelist_hits (NY, AERELN, FREQ, PROBLEM_TYPE 中至少前两个属于 high tier)。

落盘 evidence_v2/F1_codelist_high.md (top 200 名单)

---

### Task F2: 写 extract_terminology_terms.py (--tier high)

**Files:**
- Create: `scripts_v2/extract_terminology_terms.py`
- Output: `output_v2/11_terminology_high.md` (或拆 11a/b/c)

**Subagent prompt** (落盘):

```
## 任务
写 scripts_v2/extract_terminology_terms.py, 抽取 terminology 高频 codelist 完整 Term 值。

## CLI
python extract_terminology_terms.py --tier high --list <path>
python extract_terminology_terms.py --tier mid --list <path>

## 输入 (tier=high)
- evidence_v2/F1_codelist_high.md (top 200 codelist 名单)
- knowledge_base/terminology/{core,questionnaires,supplementary}/*.md

## 算法 (tier=high)
对每个 high tier codelist:
1. 解析 codelist 文件 (find by codelist name match)
2. 完整保留 codelist 标题 + 描述
3. 完整保留 Term 表, 5 列: Code | Term | Synonyms | Definition (截断 ≤200 字符) | Related Domain
4. 不展开 NCI Concept Description 长文本 (用链接 placeholder)

## 产出 (tier=high)
- output_v2/11_terminology_high.md
- 软目标 ≤200K, 硬上限 250K
- 若超 250K, 拆 11a_terminology_high_core.md + 11b_terminology_high_questionnaires.md + 11c_terminology_high_supp.md (按 terminology 子目录)
- 第一行 generated 注释 + 每 codelist 起始 source 注释

## 完成
打印 `[Tier high] 11*.md: total <N> tokens (target ≤200K)`
```

- [ ] **Step 1-9: 沿用 D2 模板, 但 reviewer 抽样数加大到 10 (规则 A 强制, 因 99% 区间压缩率最容易丢)**

主控独立抽样 10 个 codelist (与 reviewer 不重叠), Read 源 + Read 11 产出, 验证 Term 表完整。

Commit: `Phase 6.5 v2 F2: 11_terminology_high*.md (<N> tokens, top 200 codelist)`

---

### Task F3: build_v2_stage.py --stage v2.4

- [ ] **Step 1-4: 沿用模板**

system_prompt_v2.md 新增 v2.4 段: "11 (或 11a+b+c) 提供 top 200 codelist 完整 Term 值; CT Code 查询优先 11, 命中失败 fall back 到 08"

Commit: `Phase 6.5 v2 F3: stage v2.4 build done`

---

### Task F4: ⚠️ HARD CHECKPOINT - v2.4 上传 + 测试

- [ ] **Step 1-7: 沿用模板**

测试 4 题: T17, T18 (新) + 抽 T7, T15 (回归)

⚠️ **额外注意**: v2.4 是 token 跃升最大的阶段 (+350-400K), RAG 衰减风险最高。主控提醒用户:
- "本阶段后 capacity 可能从 ~18% 跳到 ~40%, 留意 indexing 时间是否变长 (可能 >30 分钟)"
- "T1-T8 抽 4 题做更全面回归 (T1, T3, T6, T8), 不只抽 2"

如本阶段 ≥1 衰减, 主控立即调 reviewer 归因 (是 RAG 重排序拐点? 还是 11 内部冲突 codelist?)。

Commit: `Phase 6.5 v2 F4: stage v2.4 checkpoint <decision>`

---

## 9. Phase G: Batch 5 — terminology 中频 codelist Term 值 (Stage v2.5, 9 任务)

### Task G1: 跑 score_codelists.py 取 200-500 名

- [ ] **Step 1-3: 沿用 F1 模板**

落盘 evidence_v2/G1_codelist_mid.md (200-500 名 codelist 名单, ~300 个)

---

### Task G2: 跑 extract_terminology_terms.py --tier mid

**算法差异 (vs tier=high)**:
- 完整保留 Code + Term + Definition (截断 ≤100 字符)
- 不保留 Synonyms 大段
- 不保留 NCI Description 链接
- 必拆 12a_terminology_mid_core.md + 12b_terminology_mid_questionnaires.md (各 ~250K)

- [ ] **Step 1-9: 沿用 F2 模板, reviewer 抽样 N=10**

Commit: `Phase 6.5 v2 G2: 12a/12b_terminology_mid.md (<N> tokens, ~300 codelist)`

---

### Task G3: build_v2_stage.py --stage v2.5

- [ ] **Step 1-4: 沿用模板**

system_prompt_v2.md 新增 v2.5 段: "12a/12b 提供 mid 频 codelist; CT Code 查询优先级 11 > 12 > 08"

⚠️ 检查 C12: 累计 token ≤ 1.5M。如超, 不进 G4, 写 failures/stage_v2.5_overflow.md, 主控决策回退或压缩 12 子集。

Commit: `Phase 6.5 v2 G3: stage v2.5 build done (<M> tokens, target ~1.3-1.5M)`

---

### Task G4: ⚠️ HARD CHECKPOINT - v2.5 上传 + 终测

- [ ] **Step 1-7: 沿用模板, 但终测 = T1-T20 全跑**

主控汇报:
```
=== Hard Checkpoint @ Stage v2.5 (终态) ===
本阶段产出: output_v2/12a + 12b = <N> tokens
累计文件数: 16-19
累计 token: <M> tokens (target ~1.3-1.5M, RAG 容量 ~50%)

⚠️ **本阶段是 v2 终态**, 终测要求:
1. 在 v2 Project 上传 12a + 12b (2 文件)
2. 等 indexing (可能 >40 分钟, 因 RAG 容量大)
3. 跑 T1-T20 全 20 题, 答案粘贴回报

回报后, 主控写终态 RAG 衰减观察 + 进入 Phase H 收尾。
```

- [ ] **Step 8: 终测后写 evidence_v2/stage_v2.5_terminal.md**

汇总: T1-T20 全数据 + 与 v1 baseline 对比 + 关键观察 (3-5 条)

Commit: `Phase 6.5 v2 G4: stage v2.5 终态 checkpoint`

---

## 10. Phase H: Wrap-up (5 任务)

### Task H1: 写 RETROSPECTIVE_V2.md (规则 C 强制)

**Files:**
- Create: `ai_platforms/claude_projects/RETROSPECTIVE_V2.md`

- [ ] **Step 1: 主控起草 RETROSPECTIVE_V2.md**

按 v1 RETROSPECTIVE.md 同结构 (5 段):
1. 保留下来的做法 (R1-RN)
2. 必须补上的 (G1-GN)
3. 关键决策复盘 (3-5 条, 含"为何不 90%"决策 + "事实修正合并 6→5 批"决策)
4. 可迁移规则 (评估是否新增到全局 CLAUDE.md)
5. 工作量数据 (subagent 调用数 / commits 数 / 用户 A/B 题数)

- [ ] **Step 2: 调 code-reviewer 复核 RETROSPECTIVE 完整性**

reviewer 检查: 三段齐全 + 关键决策有"why"段 + 工作量数据有事实支持 (从 trace.jsonl + git log 抽)

- [ ] **Step 3: trace + commit**

```bash
git add ai_platforms/claude_projects/RETROSPECTIVE_V2.md
git commit -m "Phase 6.5 v2 H1: RETROSPECTIVE_V2.md 复盘归档

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task H2: 收尾 RAG 衰减曲线 + Phase 7 输入文档

**Files:**
- Modify: `output_v2/rag_decay_curve.md` (终态 + 结论段)
- Create: `output_v2/phase7_handoff.md` (RAG 衰减曲线对 Phase 7 的可执行 insight)

- [ ] **Step 1: 主控完成 rag_decay_curve.md 结论段**

填写 6 个数据点终态 + 衰减拐点 (如有) + actionable insight。

- [ ] **Step 2: 写 phase7_handoff.md**

```markdown
# Phase 6.5 → Phase 7 交接 (RAG 衰减观察)

## 6 数据点
(从 rag_decay_curve.md 复制)

## 关键发现
1. RAG 容量在 X% 仍 PASS, 衰减拐点在 ~Y%
2. 文件数 Z 是否影响检索 (与 v2.4 拆 vs 不拆比对)
3. 不同内容类型衰减不一 (chapters vs examples vs terminology)

## 对 Phase 7 RAG 设计的 actionable insight
1. 索引粒度 (按 chunk 还是按文件): <建议>
2. 是否值得推到 70%: <建议>
3. terminology 是否需自建索引而非塞进 Project: <建议>
```

- [ ] **Step 3: commit**

```bash
git add ai_platforms/claude_projects/output_v2/rag_decay_curve.md ai_platforms/claude_projects/output_v2/phase7_handoff.md
git commit -m "Phase 6.5 v2 H2: RAG 衰减曲线收尾 + Phase 7 交接文档

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task H3: Chain B + Chain C + Chain E 索引更新

**Files:**
- Modify: `.work/MANIFEST.md` (注册 output_v2/, scripts_v2/, RETROSPECTIVE_V2.md)
- Modify: `.work/meta/worklog.md` (追加 Phase 6.5 v2 工作记录)
- Modify: `docs/PROGRESS.md` (Phase 6.5 Claude v2 状态)
- Modify: `CLAUDE.md` (Key Paths 表新增 v2 entry)

- [ ] **Step 1: 主控更新 MANIFEST.md**

在 §计划导航 → ai_platforms 段加入 v2 entry, 在 §快速参考表加入 v2 行。

- [ ] **Step 2: 主控追加 worklog.md**

```markdown
## 2026-04-XX Phase 6.5 v2 完成

- 5 批渐进扩容: chapters 全展开 → examples 高频 → examples 全 → terminology 高 → terminology mid
- v2.5 终态 token: <M>, 文件数: <N>, capacity: <X>%
- A/B 测试 T1-T20: PASS <P>/20, 衰减 <D>
- subagent 调用: <S>, 重试: <R>
- 关键产物: output_v2/, scripts_v2/, RETROSPECTIVE_V2.md, rag_decay_curve.md
```

- [ ] **Step 3: 主控更新 PROGRESS.md**

Phase 6.5 Claude 状态从"v1 完成"改为"v2 完成 (中庸 50% 容量)"

- [ ] **Step 4: 主控更新 CLAUDE.md Key Paths 表**

加入:
```
| Phase 6.5 Claude v2 计划 | `ai_platforms/claude_projects/PLAN_V2.md` |
| Phase 6.5 Claude v2 产物 | `ai_platforms/claude_projects/output_v2/` |
| Phase 6.5 Claude v2 复盘 | `ai_platforms/claude_projects/RETROSPECTIVE_V2.md` |
| Phase 6.5 Claude v2 RAG 衰减 | `ai_platforms/claude_projects/output_v2/rag_decay_curve.md` |
```

- [ ] **Step 5: commit (单 commit 多文件)**

```bash
git add .work/MANIFEST.md .work/meta/worklog.md docs/PROGRESS.md CLAUDE.md
git commit -m "Phase 6.5 v2 H3: Chain B/C/E 索引文档更新

- MANIFEST.md 注册 v2 文件
- worklog.md 追加 v2 完成记录
- PROGRESS.md 更新 Phase 6.5 v2 状态
- CLAUDE.md Key Paths 加 4 行 v2 entry

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task H4: 最终 evidence + _progress.json 收尾

- [ ] **Step 1: 写 evidence_v2/_phase_summary.md**

```markdown
# Phase 6.5 v2 全程总结

## 时间线
- 启动: 2026-04-18
- 完成: <终态日期>

## 总数据
- Stages 完成: 5 (v2.1-v2.5) (或如提前终止注明实际)
- Subagent 调用: <S> (executor X + reviewer Y + verifier Z)
- 重试 (failures): <R>
- Checkpoints: 5 hard
- Commits: <C>
- 用户 A/B 题数: <N>

## 关键决策回顾
1. 中庸策略 (~50% 而非 90%): 见 design §1.4
2. 5 批合并 (从 6 批): 见 design v3 修订
3. 文件数策略 (软 15 / 硬 20): 见 design §3.3

## 完结信号
- ✅ output_v2/ 16-19 文件齐
- ✅ Layer 1 自动检查全 PASS
- ✅ Layer 2 A/B 测试达成 PASS 标准 (或文档记录提前终止原因)
- ✅ Chain B/C/E 走完
- ✅ RETROSPECTIVE_V2.md 归档
- ✅ rag_decay_curve.md 6 数据点完整
- ✅ phase7_handoff.md 输出
```

- [ ] **Step 2: 更新 _progress.json 终态**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects
python3 -c "
import json, datetime
p = json.load(open('output_v2/evidence_v2/_progress.json'))
p['status'] = 'completed'
p['phase_done_at'] = datetime.datetime.utcnow().isoformat() + 'Z'
p['ready_for_next_phase'] = 'phase-7-rag-kg'
json.dump(p, open('output_v2/evidence_v2/_progress.json', 'w'), indent=2)
"
```

- [ ] **Step 3: trace phase_done + commit**

```bash
TIMESTAMP=$(date -u +%Y-%m-%dT%H:%M:%SZ)
echo "{\"ts\":\"${TIMESTAMP}\",\"event\":\"phase_done\",\"phase\":\"6.5-claude-v2\",\"total_tokens\":<M>,\"total_files\":<N>,\"total_subagents\":<S>}" >> output_v2/evidence_v2/trace.jsonl

cd /Users/bojiangzhang/MyProject/SDTM-compare
git add ai_platforms/claude_projects/output_v2/evidence_v2/
git commit -m "Phase 6.5 v2 H4: phase_done + _phase_summary.md

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

---

### Task H5: Push + 主控总结报告

- [ ] **Step 1: git push 主分支**

```bash
cd /Users/bojiangzhang/MyProject/SDTM-compare
git status
git log --oneline -20
git push origin main
```

- [ ] **Step 2: 主控向用户最终汇报**

```
=== Phase 6.5 Claude v2 完成 ===

最终态: <终态 stage>
- 文件数: <N>
- 总 tokens: <M>
- Capacity 实测: <X>%

A/B 测试 T1-T20:
- PASS: <P>/20
- 衰减: <D>
- T3/T6/T7 升级状况: <↑/持平/↓>

关键产物 (已 commit + push):
- output_v2/ (扩容产物)
- output_v1_baseline/ (v1 永久 archive)
- scripts_v2/ (7 个新脚本)
- RETROSPECTIVE_V2.md (复盘)
- rag_decay_curve.md (RAG 质量曲线 6 数据点)
- phase7_handoff.md (Phase 7 交接)

下一阶段建议:
- Phase 6.5 ChatGPT GPT 路线 (尚未启动)
- 或 Phase 7 RAG + 知识图谱 (设计完成, 可直接用 v2 衰减曲线指导)

是否进入下一阶段?
```

---

## 11. 并行调度策略 (可选优化)

> 默认串行 (因每批后必有 hard checkpoint), 但每批内的 executor + reviewer 可后台运行。

**严禁跨批并行** (因每批要等用户 A/B 测试)。

**批内并行**:
- B2 + B3 + B4 + B5 (5 个 Tooling 任务) 可同时调 4 个 executor + 4 个 reviewer
  - 节省 ~20-30 分钟壁钟时间
- E1 (others 拆分) 如启用, 可并行跑两个 sub-batch (10a + 10b 各一个 executor)

**主控调度示例 (Phase B 并行)**:

主控在一个消息内同时调:
```
Agent(B2 score_domains executor)
Agent(B3 score_codelists executor)
Agent(B4 build_v2_stage executor)
Agent(B5 compare_versions executor)
```

四者全返回后, 再同时调 4 个 reviewer。

---

## 12. 失败处理流程

### 12.1 失败分类

| 类型 | 触发 | 处理 |
|------|------|------|
| Subagent 输出 token 超目标 ≤10% | reviewer 报告 | 接受, manifest 记 actual, 不重做 |
| 超目标 >10% 但 ≤30% | reviewer 报告 | 主控决策: 回 executor 调整, prompt 加 "上次 X tokens 超 Y%, 请压缩 Z 段" |
| 超目标 >30% | reviewer 报告 | 写 failures/, 设计层修订 (e.g. 拆文件) |
| reviewer 提 ≥1 高优问题 | reviewer 报告 | 不让 executor 自改, 开新 executor + 新 reviewer 循环 |
| 主控独立抽样发现 reviewer 漏掉的问题 | 主控判定 | 同上 (这是规则 A 的核心保险) |
| 总 token 超 1.5M | build_v2_stage 报告 | 优先回退顺序: terminology mid > terminology high > examples others > examples high > chapters |
| 脚本 bug 导致产出错误 | 主控发现 | 不直接 Edit, 开新 debugger subagent 修, 修完走 reviewer |
| Claude Project 上传后行为异常 | 用户回报 | 不重做压缩, 先调 system_prompt_v2 (主控 Edit) |
| A/B 衰减 ≥2 题 | 用户回报 | 立即停, 失败归档, 进 Phase H 收尾 (视 v2.(X-1) 为终态) |

### 12.2 failures 文件模板

```markdown
# Stage v2.X attempt M FAIL

> 时间: YYYY-MM-DD HH:MM
> 触发: <错误类型>

## 输入
- 源文件: <list>
- subagent: <name>
- prompt: <link to subagent_prompts/>

## 产物
- 文件: <path>
- token: <N> (target ≤<X>K)
- 实际 vs 期望: <diff 描述>

## 技术判定
- 是否结构性问题 (脚本 bug)?
- 是否 prompt 描述歧义?
- 是否 RAG 限制?

## 业务判定
- 是否丢内容? 哪些?
- 是否影响下游 stage?

## 下一 attempt 输入
- 调整 prompt: <具体改动>
- 或: 调整算法: <具体改动>
- 或: 接受 + 进下批 (附条件)
```

---

## 13. Checkpoint 与用户互动

### 13.1 Hard Checkpoints (5 个, 每 Stage 一个)

每个 hard checkpoint:
1. 主控用 §13.2 模板汇报
2. 等用户回应 (yes/adjust/pause)
3. 写 checkpoints/ckpt_v2.X.md (附用户原文)
4. trace.jsonl 写 checkpoint_open + checkpoint_ack

### 13.2 主控汇报模板

```
=== Hard Checkpoint @ Stage v2.X ===
本阶段产出: <file> = <N> tokens (target ≤<X>K) [PASS/FAIL]
累计文件数: <F>
累计 token: <M>K / 1500K (<Y>%)

Layer 1 检查 (本阶段相关 C*): 全 PASS / FAIL <list>

变更对比 v(X-1):
- <文件>: 前 →>K, 现 →>K (差量 <±N>K)

请你完成以下操作:
1. <上传/删除/Project 操作具体步骤>
2. <测试题集 N 题>
3. 回报格式: ...

回报后, 主控判定:
- 全 PASS → 进 Stage v2.(X+1)
- 衰减 1 题 → reviewer 归因, 主控+你商讨是否进
- 衰减 ≥2 题 → 立即停, 视 v2.X 为 v2 终态

是否准备好执行? (yes / 调整 / 暂停)
```

### 13.3 预授权约定 (用户可一次性给)

用户可在 v2.1 之前一次性预授权:
- "Phase A + Phase B 预授权连续推进 (Setup + Tooling 是基础, 不需逐个 ack)"
- "如 Stage v2.X 全 PASS 0 衰减, 自动进 v2.(X+1)"
- "如衰减 ≥1 题, 必须停下问我"

预授权写入 _progress.json:
```json
{
  "preauth": {
    "phase_AB_continuous": true,
    "auto_advance_on_full_pass": true,
    "halt_on_any_regression": true
  }
}
```

主控启动时读 preauth 调整 checkpoint 行为。

---

## 14. Self-Review (本计划完成后由主控做)

执行此计划前, 主控按以下清单自审:

### 14.1 Spec coverage
- [ ] design §2.1 5 批 → PLAN §5-9 五个 Phase ✓
- [ ] design §3.1 文件结构 → PLAN §2.1 file map ✓
- [ ] design §3.4 system_prompt 5 阶段修订 → 各 Task <X>3 (build_v2_stage 跑) ✓
- [ ] design §4.2 5 阶段上传 → 5 个 Task <X>4 (hard checkpoint) ✓
- [ ] design §5.1 C1-C15 → 各 Task 验证 step 内引用 ✓
- [ ] design §5.2 T1-T20 → test_results_v2.md 骨架 (Task A2 Step 7) ✓
- [ ] design §5.3 RAG 衰减曲线 → rag_decay_curve.md 骨架 + 终态 H2 ✓
- [ ] design §6 R1-R13 → §12 失败处理对应 ✓
- [ ] 规则 A 语义抽检 N=10 → Task C1 Step 8 + 各 batch 同模式 ✓
- [ ] 规则 B 失败归档 → §12.2 模板 ✓
- [ ] 规则 C RETROSPECTIVE → Task H1 ✓
- [ ] 规则 D 写/审分离 → §1 P2 + 各 Task subagent_type 不同 ✓

### 14.2 Placeholder 扫描
- 所有 `<N>` `<M>` `<X>` `<P>` `<file>` 是运行时填充, 不是设计 placeholder ✓
- 没有 "TBD/TODO/implement later" ✓
- 没有 "similar to Task N" 而无具体内容 ✓

### 14.3 Type/命名一致性
- score_domains.py 在 D1/D2 一致 ✓
- score_codelists.py 在 F1/G1 一致 ✓
- 文件名 09/10/11/12 命名贯穿 design + PLAN ✓
- subagent_type 全用 oh-my-claudecode:executor / code-reviewer / verifier ✓

---

## 15. 执行交接

完成本计划后, 你 (主控) 有两个执行选项:

### 选项 1: Subagent-Driven (推荐)
**REQUIRED SUB-SKILL**: superpowers:subagent-driven-development
- 每个 Task 派一个新 executor subagent (隔离 context)
- 复核 Task 间状态后再派下一个
- 适合本计划: Tasks 独立性高, subagent 隔离最有效

### 选项 2: Inline Execution
**REQUIRED SUB-SKILL**: superpowers:executing-plans
- 在主 session 内串行执行
- 适合: 想快速看到全程

**推荐**: 选项 1 (subagent-driven), 因本计划 ~30 个 Task + 7 个脚本 + 6 阶段, 主控 context 极易膨胀。

---

## 16. 完结信号

满足以下全部条件, Phase 6.5 v2 视为完结:

1. ✅ output_v2/ 16-19 文件齐, 总 token ≤1.5M
2. ✅ Layer 1 C1-C15 全 PASS (或 FAIL 项有 failures 归档 + 用户决策接受)
3. ✅ Layer 2 A/B 测试达成 PASS 标准 (T1-T8 不衰减, T9-T20 至少 80% PASS, 或文档记录提前终止)
4. ✅ Chain B/C/E 走完
5. ✅ RETROSPECTIVE_V2.md + rag_decay_curve.md + phase7_handoff.md 归档
6. ✅ git push 完成
7. ✅ 用户确认 v2 Project 日常可用

满足后, 主控向用户报告 Phase 6.5 Claude v2 完结 + 建议下一阶段 (ChatGPT GPT 或 Phase 7 RAG)。
