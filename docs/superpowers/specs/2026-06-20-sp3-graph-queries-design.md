# SP3 — 关系/影响图查询 设计 (spec)

> 2026-06-20 · KG 重启子项目 3/5。在 SP1 `data/meta/meta.yaml` + SP2 `MetaStore` 之上加一个**纯 Python 内存图引擎**, 交付**影响/级联分析 · 跨域聚合 · 结构邻接 · 域间关系发现**, 并接入 SP2 答题通道 (NL)。与检索层正交、纯加法。
> 前置: SP1 (meta.yaml 元数据层) DONE · SP2 (确定性结构化答题通道 + MetaStore + grounding 接地闸) DONE。
> brainstorm 决策已锁 (见 §1), 用户批准设计 2026-06-20。

---

## 1. 已锁决策 (brainstorm Q1-Q5)

| # | 决策 | 选定 |
|---|------|------|
| Q1 | 首要交付面 | **图引擎模块 + NL 答题接入都做**;独立 `/api/graph/*` 端点 + §5.6 校验器 **defer 到 SP3 之后** |
| Q2 | 能力范围 | **全 4 族**: 影响/级联 · 跨域聚合 · 结构邻接/共用 · 域间关系发现 |
| Q3 | 低保真 `relations_curated` | **标 advisory/非穷尽**: 高保真事实当权威 + 接地闸硬校验;低保真域关系单独成块, 明标「curated, non-exhaustive」, 闸不硬校验, LLM 不得声称完整 |
| Q4 | 验证策略 | **确定性为主 + 少量盲写 NL 抽证**: 引擎 vs meta.yaml 独立重导 + 意图电池 + 140q 零污染 + 闸单测 + 盲写图 eval 题 (gold 从 meta.yaml 导) |
| Q5 | 图引擎底座 | **纯 Python + 预留可换接口**: `DictBackend` (MetaStore 反向索引) 实现原语, 高层 API 之下留 `GraphBackend` seam, 将来可换 networkx/Neo4j |

**反过拟合硬纪律 (贯穿, 沿用 SP1/SP2)**: 代码零硬编 q-id / 特定变量名 (只有通用语言形状);实体词表 = 全量 meta.yaml;must-fire / must-not-fire 电池 + held-out 探针证泛化;Rule A 独立样本核验。

---

## 2. 架构与模块边界

3 个新增 + 2 个扩展, 全加法, 不碰检索层 (cosine/hybrid/structured_lookup):

```
meta.yaml ──(SP1)──> MetaStore ──(SP2 反向索引)
                         │
              ┌──────────┴───────────┐
              ▼                      ▼
     GraphBackend(Protocol)    [SP2] StructuredAnswerer (计数/穷举/属性/CT)
        └ DictBackend(store)
              ▼
     GraphEngine (影响/聚合/邻接/关系 查询 API, 纯数据)
              ▼
     [SP3] GraphAnswerer (图意图检测 + 事实装配 -> StructuredFacts | None)
              │
   router/eval: merge_facts(SP2 facts, SP3 facts) -> augment_context -> LLM
                                                  -> apply_counting_gate (基数硬校验)
```

- **`server/graph_engine.py`** (新): `GraphBackend` Protocol + `DictBackend` (MetaStore 实现原语) + `GraphEngine` (高层查询 API, 纯数据, 无 NL/无 LLM)。
- **`server/graph_answer.py`** (新): `GraphAnswerer(engine)` — 图意图检测 + 事实装配 → `StructuredFacts | None` (复用 SP2 的 `StructuredFacts`/`CheckableCount` dataclass, 从 `structured_answer` import)。
- **`server/structured_answer.py`** (扩展, 小): 加 `merge_facts(*facts: StructuredFacts | None) -> StructuredFacts | None` (拼 text_block + 合并 checkable_counts), 供 router/eval 把 SP2+SP3 事实合并后 `augment_context`。SP2 既有 `resolve()` 逻辑**不动**。
- **`server/grounding.py`** (扩展, 极小或零): impact/aggregate 的**基数**走既有 `CheckableCount` 机制, `apply_counting_gate` 逻辑基本不变 (可能加 `CheckableCount.kind` 取值如 `"impacted_domains"`/`"impacted_variables"`)。advisory 关系不进 `checkable_counts`。
- **`server/main.py` / `server/router.py` / `eval/run_eval.py`** (扩展, 接线): gated 实例化 `GraphEngine`+`GraphAnswerer`;调用点把 `answerer.resolve` 改为 `merge_facts(answerer.resolve(q), graph_answerer.resolve(q))`。复用 SP2 已有的 `augment_context` + `apply_counting_gate` 接线 (eval/prod 同口径)。
- **config flag**: `graph_answer_enabled: bool = False` (初值 OFF, 验证后翻 ON, env 可覆盖)。

**Defer (SP3 之后)**: 独立 `/api/graph/*` 端点;§5.6 图增强校验器 (impact/跨域完整性/CT 级联一致性 接进 validator);Term 节点;多跳路径/中心度算法。

---

## 3. 图数据模型 (节点 / 边 / 保真度)

**节点** (类型 + 来源, 不物化 Term):

| 类型 | 数 | 来源 |
|------|----|------|
| Domain | 63 | MetaStore.known_domains |
| Variable | 1523 | MetaStore.known_variables |
| Codelist | 1005 | MetaStore.known_ctcodes |
| Class | 7 | meta domains 的 `class` 去重 |

**边** (类型 / 方向 / 保真 / 来源):

| 边 | 方向 | 保真 | 来源 |
|----|------|------|------|
| HAS_VARIABLE | Domain→Var | HIGH | `_domain_to_vars` |
| IN_DOMAIN | Var→Domain | HIGH | `_var_to_domains` (反向) |
| USES_CT | Var→Codelist | HIGH | var.ct_codes (跨域 union, 沿用 SP2 P2 `ct_codes_for_variable`) |
| CT_USED_BY | Codelist→(Domain,Var) | HIGH | `_ctcode_to_locations` |
| BELONGS_TO / CLASS_HAS | Domain↔Class | HIGH | domain.class |
| SAME_CLASS | Domain→Domain | HIGH | domain.same_class |
| DEFHOME | Var→model file | HIGH | model_defhome |
| RELATED_TO | Domain→Domain | **LOW (advisory)** | domain.relations_curated (52 边; edge_data 带 mechanism/category/note/fidelity) |

---

## 4. 能力集 (GraphEngine 查询 API)

所有方法纯数据 (返回 dict/list), 大小写不敏感入口, 未知实体 → 空/None 不抛。

**高保真** (权威注入 + 接地闸硬校验**基数**):

```python
# 影响/级联
impact_of_codelist(code) -> {"code","name","domains":[...],"variables":[...],
                             "n_domains","n_variables"} | None
impact_of_variable(var)  -> {"var","domains":[...],"n_domains"} | None

# 跨域聚合
variables_in_min_domains(n) -> [(var, count), ...]   # count>=n, 降序
domains_in_class(cls)        -> [dom, ...]
class_sizes()               -> {cls: count}
most_shared_codelists(k=10) -> [{"code","name","n_variables","n_domains"}, ...]

# 结构邻接 / 共用
same_class_domains(dom)  -> [dom, ...]
codelist_co_users(var)   -> {code: {"name","others":[var,...]}, ...}  # 用同一 CT 的其他变量
```

**低保真** (advisory, 不进 checkable_counts, 不声称穷尽):

```python
domain_relations(dom) -> {"structural": {"same_class": [...]},
                          "curated": [{"target","mechanism","category","note",
                                       "fidelity":"curated_prose"}, ...]} | None
```

> 注 (SP1 reviewer): `relations_curated.mechanism: null` = 「散文未声明」非「无机制」。SP3 **不做** 臆造 back-fill (Q3 选 advisory 而非 back-fill);如将来要, 仅当 target 结构上确定 (RELREC/RELSPEC/RELSUB) 时做, 另立单元。

---

## 5. NL 接入 + 接地 (GraphAnswerer + fidelity 政策)

### 5.1 意图检测 (通用语言形状, 零硬编实体)
- **impact** 意图: `affect/affects/impact/impacted/change/changing/depend/depends/cascade/downstream` + 锚定实体 (codelist Cxxxx 或 known variable)。
- **relationship** 意图: `related to / relationship / linked / connected / association` + 锚定 domain。
- **aggregate** 意图: 复用/扩展 SP2 的 count/enumerate 形状 (e.g. `which variables ... more than N domains`, `most shared codelist`, `how many domains in the Events class`)。
- **must-not-fire 守卫**: 无能力意图, 或有意图但无锚定 meta.yaml 实体 → `resolve()` 返回 None (回退普通 RAG, 绝不臆造)。
- 实体锚定: 复用 SP2 的 token 锚定 (uppercase var token ∈ known_variables;Cxxxx ∈ known_ctcodes;domain code ∈ known_domains, 带 SP2 的 domain/sdtm 上下文守卫防 PR/DM 误锚)。

### 5.2 注入格式
- **HIGH 块**: 沿用 SP2 header「## Structured Facts (authoritative, exhaustive, from SDTM metadata)」, 列影响集合 + 基数 (e.g. 「Codelist C66742 (No Yes Response) is used by **N** variables across **M** domains: …」), 并产出 `CheckableCount(subject=code, kind="impacted_domains"/"impacted_variables", value=M/N)`。影响**集合全列** (确定性穷尽);遗漏=recall 非 fabrication (集合已在块内)。
- **LOW/advisory 块**: 单独 header「## Related domains (curated, non-exhaustive — derived from prose, may be incomplete)」, 列 curated 关系 + mechanism/note;**不进 checkable_counts**, 提示「do not claim this list is complete」。

### 5.3 接地闸 (grounding.py)
- 复用 SP2 `apply_counting_gate`: 对 HIGH 基数 (impact/aggregate 的 N/M) 做「主语邻近数字矛盾 → 追加权威更正」, 沿用 SP2 v2 高精度闸 (缺席前提 + kind 词邻近 + 合理性)。
- **集合成员不硬校验** (Q 设计确认): 集合作权威事实注入即可, 遗漏非 fabrication;硬校验留给最脆弱的**基数**。
- advisory 关系**不校验**。

### 5.4 SP2 / SP3 重叠与去重 (避免双重注入)
SP2 已对 codelist 查询 (term/dist 意图) 注入 codelist→域/变量事实 + `CheckableCount(code,"domains"/"codelist_variables")`。SP3 的 `impact_of_codelist` 覆盖**相同数据**, 仅「影响/级联」语义框架不同。两条规避:
1. **意图词表设计上不相交**: SP3 impact 意图只在显式 `affect/impact/change/depend/cascade/downstream` 触发, 与 SP2 dist 的 `use/include/which domains` 不重叠 → 普通「which domains use C66742」只走 SP2, 「what is affected if C66742 changes」只走 SP3。
2. **`merge_facts` 去重兜底**: 合并 SP2+SP3 事实时, `CheckableCount` 按 `(subject, kind, value)` 去重, text_block 按整行去重;若同一 code 两边都产出, SP2 先序保留。
- 单测须覆盖: 一个会同时擦到两边意图的边界 query 不产生重复事实块 / 重复 count。

---

## 6. 验证 (确定性为主 + 少量盲写 NL;沿用 SP1/SP2 三门)

1. **`scripts/tests/test_graph_engine.py`** — 引擎输出 vs **meta.yaml 独立重导** (穷举, 像 SP2 快照): 全 1005 codelist 的 impact 集合 / 全 1523 var 的域分布 / 全 7 class 计数 / same_class 对称性 / co-users 自洽 == 从 meta.yaml 原始数据独立计算。**独立重导不复用 GraphEngine 自身代码** (反套套逻辑, 沿用 SP1 reconcile 思路)。
2. **`scripts/tests/test_graph_answer.py`** — 意图 must-fire / must-not-fire 电池 (通用形状, 反过拟合): impact/relationship/aggregate 各正反例 + 无意图/无锚定 → None;held-out 探针 (非示例实体)。
3. **140q 零污染** 确定性核验 — `GraphAnswerer.resolve()` 对现 test_set_v3 全部 **非图意图** 题返回 None (图注入不污染 SP1/SP2/检索题);写进 held-out 探针脚本, **不跑 live LLM eval 即证不污染**。
4. **接地闸单测** — impact/aggregate 基数被答错 → 追加更正块;基数对 → 不动;advisory 关系不触发闸。
5. **少量盲写图能力 NL eval 题** (≈8-12 题, gold 从 meta.yaml 程序导, 盲写 = 不看引擎实现) — 端到端 NL 抽证 + 运行时 smoke (真 `RAGEngine` + graph 接线穿透到答案)。
6. **Rule D** 异 `subagent_type` 独立审 (engine 正确性 + 意图 over/under-fire + advisory 是否会被 LLM 当权威 + 零污染);**Rule A** N=8 分层语义抽检 (4 能力族各 2: 影响/聚合/结构/关系, 打开答案 ↔ meta.yaml+KB 逐字段手核)。
- 失败 attempt 归档 `evidence/failures/` (规则 B);收尾 `RETROSPECTIVE_sp3.md` (规则 C)。

---

## 7. 可换后端 seam (YAGNI: 只留必要原语)

```python
class GraphBackend(Protocol):
    def nodes_of_type(self, ntype: str) -> list[str]: ...
    def out_neighbors(self, node: str, edge_type: str) -> list[str]: ...
    def edge_data(self, src: str, dst: str, edge_type: str) -> dict | None: ...  # curated attrs
```
- `DictBackend(store: MetaStore)` 用 MetaStore 反向索引实现以上 3 原语 (双向边预建)。
- `GraphEngine` 高层方法**只用这 3 原语** → 换 networkx/Neo4j 只需新写一个 Backend, GraphEngine + GraphAnswerer + 闸 + NL 全不动。
- **不做** 图查询 DSL / 通用路径语言 (那是 SP4 Neo4j+Cypher 的事)。

---

## 8. 文件结构

**新增**:
- `server/graph_engine.py` — GraphBackend + DictBackend + GraphEngine
- `server/graph_answer.py` — GraphAnswerer + 图意图检测
- `scripts/tests/test_graph_engine.py` — 引擎 vs meta.yaml 独立重导
- `scripts/tests/test_graph_answer.py` — 意图电池 + 零污染
- `eval/prod_wirein/sp3_graph_probes.py` — held-out 探针 (引擎 vs meta.yaml + 140q 零污染)
- `eval/test_set_sp3_graph.yml` — 盲写图能力 NL 题集 (gold 从 meta.yaml 导)

**修改**:
- `server/structured_answer.py` — 加 `merge_facts()` (SP2 resolve 不动)
- `server/grounding.py` — `CheckableCount.kind` 扩 impact 取值 (若需)
- `server/config.py` — `graph_answer_enabled: bool = False`
- `server/main.py` / `server/router.py` — gated 实例化 + 调用点 merge
- `eval/run_eval.py` — `--graph-answer` flag + 答案路径 merge (eval/prod 同口径)

---

## 9. 不在范围 (defer)
- 独立 `/api/graph/*` 端点;§5.6 图增强校验器;Term 节点;多跳路径/连通/中心度;networkx/Neo4j 后端 (seam 已留);relations_curated 的确定性 back-fill 升保真。

## 10. 验收三门 (沿用)
| 门 | SP3 |
|----|-----|
| 程序门 | 引擎 vs meta.yaml 独立重导 (穷举) + 意图电池 + 140q 零污染 + 闸单测 + 盲写 NL eval 抽证 + 全套绿 + ruff/mypy + 运行时 smoke |
| 规则 D | 异 type 独立审 APPROVE (0 BLOCKER/HIGH) |
| 规则 A | N=8 分层语义抽检 (4 能力族各 2) PASS |
