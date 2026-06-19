# SP2 — 确定性结构化答题通道 · 设计 (spec)

> 状态: **设计定稿待用户审** (2026-06-19)
> 来源: brainstorming 产物 (路由词「KG 重启 开始任务」)。上游 `branches/07_rag_kg/sdtm-rag/KG_ROADMAP.md` (SP2 段) + `SP2_structured_answer_design.md` (brainstorm 中途 handoff) + memory `project_kg_decision`。
> 下游: 用户审通过 → `superpowers:writing-plans` → 实现 (TDD + Rule A/B/C/D)。
> 接地证据: 架构引用的集成点均已在 2026-06-19 session 核对 (标 `[evi]`, file:line)。

---

## 0. 范围与非目标

**SP2 = 在 SP1 产出的 `data/meta/meta.yaml` 之上, 加一条与现有检索层并行的确定性答题通道**, 让计数/穷举/属性/CT 查找类问题走确定数据而非靠 LLM 记忆。**一个 SP2, 分两阶段顺序** (Q1):

- **Phase 1 — 答题通道** (主体): meta.yaml 载内存 → `/api/ask` & `/api/ask_stream` 注入权威事实块 + 计数接地闸。q103/q104 facts 翻绿。**完全不碰检索层**。
- **Phase 2 — 退役正则影子 KG**: 把 `server/structured_lookup.py` 的检索映射从「正则解析 KB markdown」改为「从 meta.yaml/MetaStore 取数」。

**两阶段各自独立回归门**, 共用一个 spec/plan (Q1)。

**非目标 (明确踢出 SP2)**:
- 关系/影响/级联查询 (内存图遍历 networkx) = **SP3**。MetaStore 持有 `same_class`/`relations_curated` 数据但 Phase 1 通道**不用** (Q4)。
- Neo4j / Cypher = **SP4 (可选)**; 图增强校验 = **SP5 (可选)**。
- `relations_curated.mechanism: null` 的确定性 back-fill (target ∈ {RELREC,RELSPEC,RELSUB}) = **SP3 可选增强** (SP1 reviewer 注记), SP2 不做。
- **q126 永久 known limitation** (SE 域语义/推理题, 非计数题): meta.yaml 把 SE 域变量事实注进 context 算 **best-effort, 不写硬验收** (双重独立阻断已记录在 SP1 spec §0)。
- **不提检索精度** — 检索已 99%, KG 的价值是评测从没测的**新能力** (计数/穷举), 不是把 99% 推更高。

---

## 1. 背景 (settled — 别 re-litigate)

- **KG ≠ 提检索精度**。真价值 = **新能力**: 计数/穷举 (q103「TAETORD 出现在 43 域」/ q104「VISITDY 出现在 36 域」今天 LLM 答错) + 退役 `structured_lookup.py` 里脆弱的正则「影子 KG」。
- SP1 已交付 `data/meta/meta.yaml` (64 域 = 63 真域 + DI 桩; 变量 name/label/role/type/core/`ct_codes`/`ct_dict` + `same_class` + `relations_curated` + `model_defhome` + `codelists`), 经独立锚对账 (reconcile gate 抓修 spec_loader 247 幻变量 bug) + Rule A N=8 + Rule D 三门。`TAETORD→43`/`VISITDY→36` 已由 reconcile 前瞻验证。
- **重定位 (用户 ack)**: 计数/穷举/属性/CT 能力用 **meta.yaml + 纯 dict 内存索引** 即可交付; **不用 networkx** (那是 SP3 关系遍历才需要)。Neo4j 是「要不要可视化界面」的产品选择, 非能力前置。

---

## 2. 已锁决策 (Q1–Q5 + 两参数, 用户 2026-06-19 brainstorming)

| # | 决策点 | 选定 |
|---|--------|------|
| Q1 | SP2 范围 | 一个 SP2, 分两阶段顺序; Phase 1 答题不碰检索, Phase 2 退役正则; 两阶段各自独立回归门, 一个 spec/plan。 |
| Q2 | 确定性置位 | **注入权威事实块 + 答题侧计数接地闸**。确定性解析器从 meta.yaml 算精确事实作权威 context 块注入, LLM 仍负责措辞/多部分; 确定性闸 (类比 `check_code_grounding.py`) 校验 LLM 数字与 meta.yaml 一致。 |
| Q3 | 路由机制 | **确定性代码路由** (无额外 LLM 调用)。entity-anchored + 增量注入 + 不确定退回纯 RAG。不依赖模型 tool-calling。 |
| Q4 | 能力范围 | **计数 + 穷举 + 变量属性 + CT/codelist 查找** 四类。`same_class`/`relations` 数据 MetaStore 持有但 Phase 1 通道不用 (留 SP3)。 |
| Q5 | 闸生产行为 | **追加权威更正块** (非破坏性): 数字不符时不改 LLM 原文, 答案后追加「据 SDTM 元数据, VISITDY 恰出现在 36 个域」之类更正; eval 统一记为 violation 指标。 |
| P1 | 规则 A 的 N | **N=8, 按 4 类能力分层抽** (计数/穷举/属性/CT 各 2)。验「用户最终看到的整段答案语义正确」, 不只数字。 |
| P2 | 接地闸覆盖 | **Phase 1 闸只硬校验计数类数字** (域数/变量数, q103/q104 正中靶心); 穷举类列表作 best-effort 注入但**不硬闸** (避免集合 diff + 措辞匹配误报 violation)。 |

### 验收靶子是能力类, 不是题 (反过拟合)
- q103 = TAETORD 出现在 **43** 个域 + label "Planned Order of Element within Arm"。
- q104 = VISITDY 出现在 **36** 个域 + label "Planned Study Day of Visit"。
- q126 = SE 域语义/推理题, **非计数题** → best-effort, 不写硬验收。
- eval 题只是验收证人; 设计按能力类 + held-out 探针 (非测试集变量/域/CT) 证 pattern 级泛化, 零硬编 q-id / 特定变量名。

---

## 3. 架构

### 3.1 模块边界 (新增, 与现有检索层并行、互不干扰)

| 模块 | 职责 | 依赖 |
|------|------|------|
| `server/meta_store.py` · `MetaStore` | **KG-lite 数据层**: init 载 `data/meta/meta.yaml`, 建内存反向索引, 暴露确定性查询 API | 仅 meta.yaml (纯 dict 索引, **不用 networkx** — 那是 SP3) |
| `server/structured_answer.py` · `StructuredAnswerer` | **答题通道**: `resolve(query)` → 实体抽取 (校验词表) + 意图线索 → `StructuredFacts` (权威文本块 + 机器可校验确定值) 或 `None` | MetaStore |
| `server/grounding.py` (新) | **计数接地闸 (运行时)**: 用 `StructuredFacts` 确定值校验 LLM 答案数字, 不符则在 live answer 路径追加权威更正块 (Q5)。eval 侧 (`eval/prod_wirein/`) **复用同一函数**只为记 violation 指标, 不另起一套逻辑 | StructuredFacts |

### 3.2 数据流 (`/api/ask` L95 与 `/api/ask_stream` L184 同构) `[evi: server/router.py:95,184]`

```
query
 ├─(1) StructuredAnswerer.resolve(query) ──► StructuredFacts | None
 │        实体锚定(命中 meta.yaml 词表才继续) + 意图线索 + 增量(只注真事实)
 ├─(2) rag.retrieve(query)            ──► chunks   [Phase 1 完全不动检索层]
 ├─(3) format_context: 若有 facts, 把权威事实块前置到 context
 │        "## Structured Facts (authoritative, exhaustive, from SDTM metadata)"
 ├─(4) build_messages → LLM completion
 └─(5) 计数接地闸(answer, facts): 数字不符 → 追加权威更正块; eval 记 violation
       └─► answer + sources
```

集成点 `[evi]`: `RAGEngine.retrieve`(server/rag.py:215) → `format_context`(rag.py:670) → `build_messages`(rag.py:683)。Phase 1 在 `format_context` 前置事实块、在 completion 后挂接地闸, **不动 `retrieve` / `_apply_structured_lookup`(rag.py:281)**。

### 3.3 答题通道的保守性 (反过拟合核心)

- **实体锚定**: 必须先在 query 命中 meta.yaml 全量词表 (1917 变量条目 / 1523 唯一变量名 / 63 域 / 全部 CT 码) 的已知实体, 否则 `resolve→None` 退回纯 RAG。
- **增量注入**: 意图线索 ("how many"/"which domains"/"label"/"codelist"…) 只决定**注入哪些真事实并如何强调**; 线索误判最坏后果是多注几条**真**事实 (recall-additive, 不会答错), 不是给错答案。
- **意图是通用语言形状**, 零硬编 q-id / 特定变量名; 配 must-fire / must-not-fire 电池 + 非测试集 held-out 探针证泛化。
- 计数正确性由**接地闸独立兜底**, 与意图检测解耦。
- **must-not-fire 的语义** (澄清): 注入是 recall-additive, 不让答案「事实错」; 但 must-not-fire 电池仍重要 — 它防的不是答错, 而是**答非所问 / 污染 context** (如问 VISITDY 的*用法*却硬塞计数事实, 致非 sequitur)。must-not-fire 守**相关性/质量**, correctness 由接地闸独立兜底, 两层解耦。

---

## 4. 组件设计细节

### 4.1 `MetaStore` (`server/meta_store.py`)

- **init**: 一次 `yaml.safe_load(data/meta/meta.yaml)` (21138 行 / 496KB `[evi: data/meta/meta.yaml]`), 在内存建反向索引 (SP1 §3 开放细节 e: 反向索引不落盘, 内存建, 避免双写漂移)。
- **正向数据**: `domains`(L5027) / `codelists`(L1) / `model_defhome`(L21079) `[evi: data/meta/meta.yaml]`。
- **内存反向索引** (init 时建):
  - 变量名 → [域列表] (穷举/计数; 大小写折叠匹配)
  - CT 码 → [(域, 变量)] (CT 查找)
  - codelist 名/码 → 元数据
  - 域 → [变量列表]
- **Phase 1 查询 API** (确定性, 纯函数):
  - `domains_for_variable(var) -> list[str]` (+ `len()` 即计数; q103/q104 靠这个)
  - `variable_attributes(var) -> {label, role, type, core, ct_codes}`
  - `variables_in_domain(dom) -> list[str]`
  - `codelist(ct) -> {name, extensible, term_count, termfile}`
  - `domains_for_codelist(ct)` / `variables_for_codelist(ct)`
  - `n_domains` / `n_variables` (总数; counts_toward_63 口径)
- **不暴露** (Phase 1): `same_class` / `relations_curated` 遍历 API (留 SP3)。

### 4.2 `StructuredAnswerer` (`server/structured_answer.py`)

- `resolve(query) -> StructuredFacts | None`:
  1. **实体锚定**: 扫 query, 匹配 MetaStore 全量词表里的已知实体 (变量名/域/CT 码)。零命中 → `None`。
  2. **意图线索**: 通用语言形状检测 (count / enumerate / attribute / codelist), 零硬编 q-id 或特定变量名。
  3. **增量装配 `StructuredFacts`**: 对命中实体 + 意图, 从 MetaStore 取真事实, 组装 (a) 人读权威文本块 (注入 context) + (b) 机器可校验确定值 (供接地闸)。
- `StructuredFacts` 数据结构: `{ text_block: str, checkable_counts: dict[str,int] }` (Phase 1 闸只读 `checkable_counts`, 见 P2)。
- **保守默认**: 任何不确定 → 倾向多注真事实或 `None` 退回 RAG, 绝不构造未在 meta.yaml 出现的断言。

### 4.3 计数接地闸 (`server/grounding.py`, 运行时; eval 复用)

- 范式沿用 `eval/prod_wirein/check_code_grounding.py` (4996B, 确定性码 grounding 闸) `[evi: eval/prod_wirein/check_code_grounding.py]`。
- **位置决定** (消歧): 闸逻辑放运行时 `server/grounding.py` (Q5 要求在 live `/api/ask` 路径追加更正块); eval 侧 import 同一函数记 violation 指标, **不复制逻辑** (避免运行时与 eval 口径漂移)。
- 输入: LLM `answer` + `StructuredFacts.checkable_counts`。
- 行为 (Q5 + P2): 抽 answer 里与 checkable_counts 同语境的数字, 与确定值比对; **只硬校验计数类** (域数/变量数)。不符 → **追加权威更正块** (非破坏性, 不改原文): 「据 SDTM 元数据, <VAR> 恰出现在 <N> 个域」。eval 统一记 violation 指标。
- 穷举类列表: best-effort 注入, **不硬闸** (P2)。

---

## 5. 验收 (三门 + 验证纪律 + 反过拟合)

### 5.1 验收三门 (沿用 SP1 已跑通的)

1. **程序门**: paired eval 指标达标 + held-out 探针对账 + 单测全绿 + 接地闸 0 violation。
2. **规则 D — 审阅隔离**: 异 `subagent_type` 独立代码审 APPROVE (writer ≠ reviewer 同 context 自审无效)。**Phase 1 一轮, Phase 2 一轮**。
3. **规则 A — N=8 分层语义抽检** (证据 `evidence/checkpoints/` 或 `evidence/step_NN_audit.md`): 4 类能力各 2 (计数/穷举/属性/CT), 核「用户最终看到的整段答案」语义对 meta.yaml + KB source。

### 5.2 验证 / 反过拟合纪律

- **Phase 1**: OFF vs ON paired eval (DeepSeek temp=0, v3 140q) — q103/q104 facts 翻绿 (43/36 + labels), **全类零回归**, 计数接地闸 0 violation。
- **Held-out 探针电池**: 用**非测试集**的变量/域/CT 跑 count/enumerate/attr/CT 四类查询, 答案对账 reconcile-verified 的 meta.yaml。证「pattern 级泛化、非背题」。
- **单测**: MetaStore 索引正确性 + StructuredAnswerer must-fire/must-not-fire 电池 + 接地闸。
- **反过拟合硬纪律**: 零 q-id / 特定变量硬编; 实体词表 = 全量 meta.yaml; must-not-fire 电池 (属性/用法题命名同实体不应触发错事实/非 sequitur); held-out 探针。
- **规则 B — 失败归档**: 任何失败 attempt 归 `evidence/failures/step_NN_attempt_X.md`, 不删。
- **规则 C — Retro**: 收尾前写 RETROSPECTIVE (保留做法 / 缺口 / 决策复盘)。

### 5.3 配置 / 灰度 (沿用 structured_lookup / guardrail 已验证范式)

- `server/config.py` 加 `structured_answer_enabled: bool` (env `SDTM_RAG_STRUCTURED_ANSWER_ENABLED`)。范式对齐现有 `structured_lookup_enabled`(L63)/`hybrid_enabled`(L70)/`prompt_guardrail_enabled`(L87) `[evi: server/config.py:63,70,87]`。
- build 期默认 **OFF** → paired eval → 验证后默认 **ON**。env-overridable 供 A/B 即时回滚。
- `/api/ask` + `/api/ask_stream` 都接。

---

## 6. Phase 2 — 退役正则影子 KG (Phase 1 独立验收之后才动)

- **前置门**: Phase 1 翻绿且独立验收 (5.1 三门) 通过**之后**才开 Phase 2。
- **改动**: 把 `server/structured_lookup.py` 的检索映射 (`resolve()` L561 → gold file paths) `[evi: server/structured_lookup.py:561]` 从「正则解析 KB markdown」改为「从 meta.yaml/MetaStore 取数」, 含用 SP1 产的 `model_defhome` 替换脆弱的 `len(inner) == 6` 解析。
- **⚠️ LOAD-BEARING 警告**: `structured_lookup.py:403-413,447` 显式标注 `len(inner) == 6` 是 **LOAD-BEARING discriminator** + "Do NOT relax" `[evi: server/structured_lookup.py:403,447]`。Phase 2 **不能只删它** — 必须用 meta.yaml/`model_defhome` 数据**保住它实现的判别行为** (隔离正确的表/变量), 并用回归门证明行为等价。
- **独立回归门**: retrieval-only paired eval v3 140q **≥ 现 99% 零回归** + 反过拟合探针电池不变。
- **规则 D**: Phase 2 单独一轮异 type 独立审。

---

## 7. 风险 / 已知边界

- **意图误判**: 由「增量注入 = recall-additive」+ must-not-fire 电池 + 接地闸三层兜底; 最坏多注真事实, 不答错。
- **Phase 2 LOAD-BEARING 退役**: `len==6` 判别器是已知脆弱点也是已知正确点; 退役风险由「行为等价回归门 (零回归)」+ 独立审控制。**不在未证等价前 ship**。
- **接地闸数字抽取**: 自然语言里数字抽取可能漏 (LLM 用文字「forty-three」而非「43」)。P2 决定只硬校验计数, 且更正块是追加非破坏 → 漏报最坏是少一条更正, 不会误伤正确答案。
- **meta.yaml 漂移**: meta.yaml 由 SP1 build_meta 生成, 若 KB 更新未重跑生成器会漂移; 这是 SP1 的再生职责, SP2 消费方假定 meta.yaml 已 reconcile-verified。
- **q126 / SE 语义题**: best-effort, 不硬验收 (§0)。

---

## 8. 交付物清单

- `server/meta_store.py` (`MetaStore` + 内存反向索引)
- `server/structured_answer.py` (`StructuredAnswerer` + `StructuredFacts`)
- `server/grounding.py` (计数接地闸, 运行时; eval/prod_wirein/ 复用同一函数记指标)
- `server/config.py` += `structured_answer_enabled` (默认 OFF→ON)
- `server/router.py` / `server/rag.py` 接线 (`/api/ask` + `/api/ask_stream` 注入事实块 + 挂接地闸)
- **Phase 2**: `server/structured_lookup.py` 改 meta.yaml 取数 (退役 `len==6` 正则)
- 单测: MetaStore 索引 / StructuredAnswerer must-fire-must-not-fire / 接地闸
- eval: Phase 1 OFF-vs-ON paired (v3 140q) + held-out 探针电池; Phase 2 retrieval-only paired
- `PLAN_sp2_structured_answer.md` / `_progress*.json` / `evidence/checkpoints/` / `evidence/failures/` / `RETROSPECTIVE_sp2.md` (Tier 2)

---

## 9. 不做 (YAGNI)

- 不用 networkx / 内存图遍历 (SP3)
- 不暴露 `same_class` / `relations_curated` 遍历 API (SP3)
- 不做 mechanism null 的 back-fill (SP3 可选)
- 不上 Neo4j / Cypher (SP4 可选)
- 不做图增强校验 (SP5 可选)
- 不额外 LLM 调用做路由 (Q3: 确定性代码路由)
- 不硬闸穷举列表 (P2: best-effort)
- 不为 q126/SE 语义题写硬验收 (best-effort)
- 不在 Phase 1 碰检索层 (Q1: 风险隔离)
- 不改 `knowledge_base/` / 不重生成 meta.yaml (SP1 职责)
</content>
</invoke>
