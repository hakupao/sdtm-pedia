# AGG — Aggregate 独立答题通道 (触发面拓宽 + 并入 SP2 通道语义) 设计 (spec)

> 2026-07-07 · KG 价值 eval (2026-06-21) 的直接后续: 榨取 SP3 唯一正向生态位。把 aggregate 聚合能力
> (variables_in_min_domains / most_shared_codelists) 从 SP3 GraphAnswerer 的极窄 NL 面拆出,
> 独立成 `AggregateAnswerer` 小通道并重写 pattern-level 触发检测 (fire-rate 2/10 → 目标 ≥80% held-out)。
> 前置: SP1/SP2/SP3 DONE 默认 ON · KG 价值 eval DONE (verdict: aggregate 触发时 set_recall +11~17pp, 但 NL 仅 2/10 触发)。
> brainstorm 决策已锁 (见 §1), 用户批准设计 2026-07-07。完成后接 SP4/SP5 独立设计单元 (KG 重启)。

---

## 1. 已锁决策 (brainstorm Q1-Q3)

| # | 决策 | 选定 |
|---|------|------|
| Q1 | 拓宽范围 | **只拓 aggregate** — eval 证明 impact 与 SP2 逐字冗余、relationship 真触发 ΔSP3=0; 两者保持现状不动。codelist_co_users NL 接入不做 (留 backlog) |
| Q2 | 验收门 | **程序门 + fire-rate 门 + ds 迷你端到端** — 新盲写 held-out 题测触发泛化; deepseek OFF vs ON 配对证 set_recall 真涨 |
| Q3 | 架构归宿 | **独立 `AggregateAnswerer`** — 新 ~60-80 行小答题器注册进 CompositeAnswerer; SP2 `StructuredAnswerer` 零改动; SP3 `graph_answer` 删 aggregate 分支回归纯图 |

**反过拟合硬纪律 (贯穿, 沿用 SP1-SP3 + kgval)**: 代码零硬编 q-id / 特定变量名; **kgval 40 题不作为 pattern 提取源, 只作事后回归对照**; pattern 来自英语数量/最高级表达的语言形状分类; held-out 盲写题 (写手不见触发词表/不见 kgval 题) 证泛化; Rule A 独立样本核验。

---

## 2. 架构与模块边界

```
CompositeAnswerer (main.py maybe_build_answerer, 注册顺序 = 权威事实块行文顺序)
 ├─ StructuredAnswerer (SP2)        ← 零改动
 ├─ AggregateAnswerer  (AGG, 新)    ← detect_aggregate_intents + 装配 (平移自 graph_answer)
 │     └─ 调 GraphEngine.variables_in_min_domains / most_shared_codelists (只读)
 └─ GraphAnswerer      (SP3)        ← 删 aggregate 分支 → 纯图 (impact / relationship)
```

- **`server/aggregate_answer.py`** (新, ~60-80 行): `detect_aggregate_intents(query) -> set[str]`
  (子意图 `threshold` / `superlative`) + `AggregateAnswerer(engine)`, `resolve(query) -> StructuredFacts | None`。
  装配逻辑**平移**自 `graph_answer.py` 现 aggregate 分支: strict→n+1 / inclusive→n 语义、`[:50]` 截断、
  most_shared top-5 输出格式全保留 (kgval 已证有效, 不重新发明); 装配行文格式逐字不变。
- **`server/graph_answer.py`** (改): 删 `detect_graph_intents` 的 aggregate 两条检测 + `resolve` 的
  aggregate 装配分支; docstring 三意图族改两意图族。`GraphEngine` 两个聚合方法**保留不动** (SP4/API 用)。
- **`server/config.py`** (改): `aggregate_answer_enabled: bool = False` 初值 OFF, 本单元全门过后翻默认 ON
  (同 SP3 惯例), env `SDTM_RAG_AGGREGATE_ANSWER_ENABLED` 可回滚。
- **`server/main.py`** (改, 接线): `maybe_build_answerer` 按 flag 注册 AggregateAnswerer (顺序 SP2 → AGG → SP3),
  boot log 一行。GraphEngine 实例在 AGG/SP3 任一开启时构造一次共享。
- **`eval/run_eval.py`** (改, 接线): 加 `--aggregate-answer` flag, 对齐既有 `--structured-answer`/`--graph-answer`,
  供拉臂。
- **测试**: `scripts/tests/test_aggregate_answer.py` (新) — 意图电池 + 装配对账;
  `scripts/tests/test_graph_answer.py` 同步删 aggregate 用例 (迁移至新文件)。

**范围外 (defer)**: codelist_co_users NL 接入; impact/relationship 触发面; upper-bound 聚合查询
("fewer than N" 需要引擎新方法, 见 §3); grounding gate 新 kind; SP4/SP5。

---

## 3. 触发检测设计 (pattern-level)

### 3a. `threshold` 子意图 (variables_in_min_domains)

触发条件 = **阈值表达命中** ∧ `"variable"` 在 query ∧ `"domain"` 在 query (双词共现门, 沿用现语义, 大小写不敏感)。

阈值表达 regex 家族 (语言形状, 只收**下界**表达; 数字是表达式一部分, 无数字不触发):

| 家族 | 形状 | strict/inclusive |
|------|------|------|
| 比较词前置-严格 | `(more than|greater than|over|exceed(s|ing)?) N` | strict → 阈值 n+1 |
| 比较词前置-含界 | `(at least|a minimum of|no fewer than) N` | inclusive → 阈值 n |
| 数字后置-含界 | `N (or more|or greater|and above|and up)` · `N+` | inclusive → 阈值 n |

**明确不触发 (must-not-fire)**: 上界表达 (`fewer than` / `less than` / `at most` / `no more than` / `N or fewer`) —
引擎只有 ≥ 语义 (`variables_in_min_domains`), 触发会注入**方向错误**的事实; 上界家族进 must-not-fire 电池。

### 3b. `superlative` 子意图 (most_shared_codelists)

触发条件 = **最高级表达命中** ∧ **codelist 上下文词共现** (复用 SP2 `_CODELIST_CUES`:
codelist / controlled term / ct code / terminology / code list)。

最高级表达 regex 家族:

| 家族 | 形状 |
|------|------|
| most + (副词) + 分词/形容词 | `most (\w+ly )?(shared|used|reused|common|frequent\w*|prevalent|popular)` |
| 最大数量式 | `(largest|highest|greatest|biggest) number of` |

共现门挡散文误触发 ("most common adverse events" 无 codelist 词 → 不触发)。
must-not-fire 三层兜底: 共现门 (设计) → 单测电池 (程序) → 140q 零污染门 (最终裁判)。

---

## 4. 数据流与保守性

- `resolve` 无命中 / 装配空 → `None` (与 SP2/SP3 语义一致); 只读 GraphEngine; 无状态。
- **不新增 grounding gate 的 CheckableCount kind** (现 aggregate 装配本无 checkable_counts, 加新闸 kind 属范围外)。
- 误触发最坏情形 = 注入多余**真**事实 (recall-additive), 与现有两通道同一安全模型。
- 行为等价保证: 对**新旧都触发**的 query, 新通道装配输出与旧 graph_answer aggregate 分支**逐字相同**
  (golden 单测钉住)。**一处刻意收窄** (行为变化, 非等价): 旧 superlative 检测无 codelist 词门
  ("most common" 单独即触发), 新检测加共现门 → "most common + 无 codelist 词" 的 query 从
  「注入离题 most-shared 事实」变为「不触发」— 定向改进, 进 must-not-fire 电池锁定。

---

## 5. 验收门 (五道, 全过才翻默认 ON)

1. **单测电池**: must-fire (每个语言形状家族 ≥3 例) / must-not-fire (上界表达 · SP2 计数题 · 无 codelist 词的
   最高级散文题 · 无数字阈值句) + 装配 vs meta.yaml 对账 + 旧新装配 golden 等价 + strict/inclusive 阈值映射单测。
2. **140q 零污染门**: 生产 composite (SP2+AGG+SP3 ON) vs 全 OFF 在 140q 检索评测集上 **byte-identical 0/140**
   (复用 `eval/prod_wirein/sp3_graph_probes.py` 模式, 扩展进 AGG flag)。
3. **fire-rate 门**: 新盲写 held-out aggregate 题 **15-20 道** (写手 agent 不见触发词表/pattern/kgval 题;
   threshold/superlative 两子族约各半), fire-rate **≥80%**; kgval aggregate 旧 10 题回归报告 (参考, 非唯一证据)。
4. **ds 迷你端到端**: (kgval aggregate 10 回归 + held-out 新题) × 2 臂 (生产 ON vs `aggregate_answer_enabled=false`)
   × deepseek temp=0 配对; gold 程序导 (`gen_kgval_goldset.py` 模式) + raw-yaml 独立 reconcile;
   **set_recall 为主** (词边界), cardinality 辅, judge 佐证。要求: held-out aggregate set_recall
   **Δ(ON−OFF) ≥ +10pp** (方向与 kgval +11~17pp 一致); 出现退化题时**逐题因果人审**再判
   (temp=0 仍有解码变异 — kgval rl05 教训, 不把单题摆动误判为通道伤害), 真·通道致害 = 门 FAIL。
5. **质量门**: 全套 pytest 0 fail + ruff/mypy (新/改文件) clean + **Rule D** 异 subagent_type 审 diff +
   **Rule A** 独立抽检 N=6 (触发样本装配事实 vs meta.yaml 双源核验 + 端到端评分抽核), N 写进 PLAN。

失败归档 Rule B: `branches/07_rag_kg/sdtm-rag/evidence/failures/agg_attempt_*.md`。

---

## 6. 交付物与收尾

- 代码: `server/aggregate_answer.py` (新) + `graph_answer.py`/`config.py`/`main.py`/`run_eval.py` (改)。
- 测试/评测资产: `test_aggregate_answer.py` + held-out 题集 `eval/test_set_agg_heldout.yml` (盲写+gold+reconcile)
  + fire-rate 探针 (复用 `kgval_fire_probe.py` 模式)。
- 证据: `evidence/checkpoints/agg_channel_summary.md` (五门结果) + failures/ (如有)。
- 文档链 (Chain 07_RAG): KG_ROADMAP.md 加 AGG 段并更新「下一步」→ SP4/SP5; worklog phase_07_rag_kg.md;
  docs/PROGRESS.md; `_progress` (Tier 2)。
- 体量: **Tier 2** (~8-12 step, 半天)。完成后 **SP4/SP5 = 独立设计单元**, 另起 brainstorm (KG 重启路由词)。
