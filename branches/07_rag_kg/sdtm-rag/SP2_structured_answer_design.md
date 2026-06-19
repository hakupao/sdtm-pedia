# SP2 — 确定性结构化答题通道 · 设计草案 (DRAFT — 已被定稿取代, 仅作 brainstorm 历史)

> ⚠️ **SUPERSEDED 2026-06-20**: 本文件是 brainstorming 中途 handoff 草稿。**最终定稿 spec 在 `docs/superpowers/specs/2026-06-19-sp2-structured-answer-design.md`**, 实现计划在 `docs/superpowers/plans/2026-06-19-sp2-structured-answer.md`, Phase 1 已 DONE (见 `RETROSPECTIVE_sp2_phase1.md` + `KG_ROADMAP.md`)。本文件不再维护, 仅保留 brainstorm 决策轨迹。
>
> 创建 2026-06-19 · 原状态: brainstorming 进行中, 5 决策已锁, 架构第一块已呈现等用户确认。

## Resume 指南 (新 session 怎么接上)

1. 说「KG 重启 开始任务」→ 读 `KG_ROADMAP.md` + memory `project_kg_decision` + **本文件**。
2. 重新 invoke `superpowers:brainstorming` skill (HARD-GATE: 设计批准前不写码)。
3. 当前断点 = **架构第一块(下方 §架构 1-3)已呈现给用户, 等"看着对吗"确认**。
   - 用户若确认 → 走第二块(下方 §待走查: Phase 2 顺序 / 验证纪律 / 配置灰度 / 验收三门), 逐节征得批准。
   - 全设计批准 → 写最终 spec → spec 自审 → 用户审 spec → invoke `superpowers:writing-plans`。
4. **不要 re-litigate 已锁决策 (Q1-Q5)**, 除非用户主动改。

---

## 已锁决策 (Q1–Q5, 用户 2026-06-19 brainstorming)

| # | 决策点 | 选定 |
|---|--------|------|
| Q1 | SP2 范围 | **一个 SP2, 分两阶段顺序**: Phase 1 = 答题通道(q103/q104/q126 翻绿, **不碰检索**); Phase 2 = 退役 structured_lookup 正则(改从 meta.yaml 取数)。**两阶段各自独立回归门**, 一个 spec/plan。 |
| Q2 | 确定性置位 | **注入权威事实块 + 答题侧计数接地闸**。确定性解析器从 meta.yaml 算精确事实作权威 context 块注入, LLM 仍负责措辞/多部分; 确定性闸(类比 `check_code_grounding.py`)校验 LLM 数字与 meta.yaml 一致。 |
| Q3 | 路由机制 | **确定性代码路由**(无额外 LLM 调用)。entity-anchored + 增量注入 + 不确定退回纯 RAG。与现有 completion 管线契合, 不依赖模型 tool-calling。 |
| Q4 | 能力范围 | **计数 + 穷举 + 变量属性 + CT/codelist 查找** 四类。①计数(变量→#域, 域→#变量, 总域/变量数) ②穷举(变量→域列表, codelist→变量/域列表) ③属性(label/role/type/core) ④CT/codelist(变量→CT码, codelist→termfile/extensible/term_count)。same_class/relations 数据 MetaStore 持有但 Phase 1 通道不用(留 SP3)。 |
| Q5 | 闸生产行为 | **追加权威更正块**(非破坏性): 数字不符时不改 LLM 原文, 答案后追加「据 SDTM 元数据, VISITDY 恰出现在 36 个域」之类更正; eval 统一记为 violation 指标。 |

### 验收靶子是能力类, 不是题 (反过拟合)
- q103 = TAETORD 出现在 **43** 个域 + label "Planned Order of Element within Arm"。
- q104 = VISITDY 出现在 **36** 个域 + label "Planned Study Day of Visit"。
- q126 = SE 域语义题(UNPLAN / SEUPDES / "actually passed through" / "One record per planned Element") — **检索+推理题非计数题**, meta.yaml 把 SE 域变量事实注进 context 算 **best-effort, 不写硬验收**。
- eval 题只是验收证人; 设计按能力类 + held-out 探针证 pattern 级泛化。

---

## 架构 (第一块 — 已呈现, 等用户确认)

### 1. 模块边界 (新增, 与现有检索层并行、互不干扰)

| 模块 | 职责 | 依赖 |
|------|------|------|
| `server/meta_store.py` · `MetaStore` | **KG-lite 数据层**: init 载 `data/meta/meta.yaml`, 建内存反向索引, 暴露确定性查询 API | 仅 meta.yaml (纯 dict 索引, **不用 networkx** — 那是 SP3) |
| `server/structured_answer.py` · `StructuredAnswerer` | **答题通道**: `resolve(query)` → 实体抽取(校验词表) + 意图线索 → `StructuredFacts`(权威文本块 + 机器可校验确定值) 或 `None` | MetaStore |
| `server/grounding.py`(新) / 扩展 `eval/prod_wirein/check_code_grounding.py` | **计数接地闸**: 用 `StructuredFacts` 确定值校验 LLM 答案数字 | StructuredFacts |

`MetaStore` 查询 API (Phase 1 用): `domains_for_variable(var)`→列表+count、`variable_attributes(var)`→{label,role,type,core,ct_codes}、`variables_in_domain(dom)`、`codelist(ct)`→{name,extensible,term_count,termfile}、`domains_for_codelist`/`variables_for_codelist`、总数 `n_domains`/`n_variables`。

### 2. 数据流 (`/api/ask` 与 `/ask_stream` 同构)

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

**要点: Phase 1 不碰 `structured_lookup`(检索层)** — 新通道是加法、并行的, 风险完全隔离(落实 Q1)。

### 3. 答题通道的保守性 (反过拟合)

- **实体锚定**: 必须先在 query 命中 meta.yaml 全量词表(1917 变量 / 63 域 / 全部 CT 码)的已知实体, 否则 `resolve→None` 退回纯 RAG。
- **增量注入**: 意图线索("how many"/"which domains"/"label"/"codelist"…)只决定**注入哪些真事实并如何强调**; 线索误判最坏后果是多注几条**真**事实(recall-additive, 不会答错), 不是给错答案。
- **意图是通用语言形状**, 零硬编 q-id / 特定变量名; 配 must-fire / must-not-fire 电池 + 非测试集 held-out 探针证泛化。
- 计数正确性由**接地闸独立兜底**, 与意图检测解耦。

---

## 待走查 (第二块 — 已起草, 尚未与用户逐节确认)

> 以下为草拟, 新 session 需逐节呈现征得用户批准 (brainstorming "present design sections" 步骤)。

### A. Phase 2 (退役正则) 顺序
- Phase 1 翻绿且独立验收**之后**才动。
- 把 `structured_lookup.py` 检索映射从「正则解析 KB markdown」改为「从 MetaStore/meta.yaml 取数」(含用 SP1 产的 `model_defhome` 替换脆弱 `len==6` 解析)。
- **独立回归门**: retrieval-only paired eval v3 140q ≥ 现 99% **零回归** + 反过拟合探针电池不变。

### B. 验证 / 反过拟合纪律
- **Phase 1**: OFF vs ON paired eval (DeepSeek temp=0, v3 140q) — q103/q104 facts 翻绿(43/36+labels), 全类零回归, 计数接地闸 0 violation。Held-out 探针电池(非测试集变量/域/CT 的 count/enumerate/attr/CT 查询 → 对账 reconcile-verified meta.yaml)。单测: MetaStore 索引 + StructuredAnswerer must-fire/must-not-fire + 闸。
- **Phase 2**: retrieval-only paired = 现状零回归 + 探针不变。
- **规则 A**: N 独立语义抽检 deterministic answer vs KB (N 写进 plan)。**规则 B**: 失败归档 `evidence/failures/`。**规则 C**: 收尾 RETROSPECTIVE。**规则 D**: 异 `subagent_type` 独立审 (writer≠reviewer), Phase 1/Phase 2 各一轮。
- **反过拟合硬纪律**: 零 q-id/特定变量硬编; 实体词表=全量 meta.yaml; must-not-fire 电池(属性/用法题命名同实体不应触发错事实); held-out 探针。

### C. 配置 / 灰度
- `config.py` 加 `structured_answer_enabled` (env `SDTM_RAG_STRUCTURED_ANSWER`), build 期默认 **OFF** → paired eval → 验证后默认 **ON** (沿用 structured_lookup / guardrail 灰度范式)。
- `/ask` + `/ask_stream` 都接。

### D. 验收三门 (沿用 SP1)
1. **程序门**: paired eval 指标达标 + held-out 探针对账 + 单测全绿 + 接地闸 0 violation。
2. **规则 D**: 异 type 独立代码审 APPROVE (Phase 1 一轮, Phase 2 一轮)。
3. **规则 A**: N 独立语义抽检 PASS。

### E. Tier
- **Tier 2** (5-15 step)。产出 `PLAN_sp2_structured_answer.md` / `_progress*.json` / `evidence/checkpoints/` / `evidence/failures/` / RETROSPECTIVE。

---

## 关键参考 (代码现状, 已读)
- `server/rag.py`: `RAGEngine.retrieve()`(L215) → cosine + `_apply_structured_lookup`(L281, 检索杠杆 union-add gold 文件) ; `format_context`(L670) / `build_messages`(L683)。
- `server/router.py`: `/api/ask`(L94) 同步; `/api/ask_stream`(L183) SSE。
- `server/structured_lookup.py`: 要 Phase 2 退役的正则检索层(resolve→gold file paths)。当前 99%、反过拟合测试守护。
- `data/meta/meta.yaml`: 21138 行 / 496KB; 顶层 `codelists:` / `domains:`(L5027) / `model_defhome:`(L21079)。SP1 reconcile 已验 TAETORD→43 / VISITDY→36。
- 现有确定性闸范式: `eval/prod_wirein/check_code_grounding.py`。
