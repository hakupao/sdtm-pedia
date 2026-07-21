# RETROSPECTIVE — SP3 (关系/影响图查询)

> 2026-06-20 · KG 重启子项目 3/5。在 SP1 meta.yaml + SP2 MetaStore 之上加纯 Python 内存图引擎 (`GraphEngine` + 可换 `GraphBackend`) + NL 图答题 (`GraphAnswerer`, 经 `CompositeAnswerer` 并入 SP2 答题通道)。能力: 影响/级联 · 跨域聚合 (variables_in_min_domains + most_shared) · 结构邻接/共用 · 域间关系发现 (advisory)。默认 ON。
> 全流程: brainstorm (Q1-Q5) → spec → plan (16 task) → subagent-driven (per-phase impl + per-phase 独立审 + 最终全量 Rule D) → Rule A N=8。

## 1. 保留下来的做法

- **subagent-driven + 控制器逐阶段亲自复核 = 抓真缺陷。** 每阶段独立 reviewer (异 type) **at-scale** 扫描抓到我自己 4 样本 smoke 漏掉的 HIGH (140q 零污染失败 5/140) 和 class_domains 接地闸假阳。控制器在 task 间亲自重跑 (suite/mypy/ruff/sweep) 又抓到 implementer 自检漏的: mypy 没跑、ruff 没覆盖测试文件、class_domains "已 revert" 其实只剩注释。**写审隔离 + 独立全量重跑, 不是走过场。**
- **穷举/快照对账 (engine vs raw meta.yaml)** 从 SP1/SP2 沿用: Task 5 不复用 GraphEngine 自身、直接从 `yaml.safe_load` 独立重导, 全 1005 codelist / 1523 var / 8 class 对账 → 反套套逻辑的确定性证明。最终 reviewer 又用 from-scratch `RawBackend` 证 seam byte-identical。
- **escalate-don't-whack-a-mole (兑现反过拟合红线)。** 意图收紧第一轮振荡 (修 5 题、又撞 5 题) 时, 我**停掉 subagent、自己诊断根因** (class 名是常用词)、把 scope 岔路 (A 去掉 / B 紧框架) **交给用户** 而非让 subagent 继续按题调参。这正是 memory 里「prompt 必区分 pattern vs example」的落地。
- **CompositeAnswerer 零改调用点。** 把 SP2+SP3 合并放进 `maybe_build_answerer` 返回的 composite, `resolve()` 内部 merge → router/ask_stream/run_eval **逐字不改**, 接地闸自然跑 merged counts。最小爆炸半径。
- **可换 backend seam (GraphBackend 3 原语)**: 高层 API / NL / 闸 与拓扑解耦, 将来 networkx/Neo4j 只换 backend。reviewer 实证可换。

## 2. 必须补上的缺口

- **零污染门 vs NL 能力覆盖的张力 (已知限制)。** 严格「graph 对全 140q 静默」意味着测试集里**本身是图形状**的题 (如 q10「TR 和 RS 怎么 linked」) NL 图通道也不答 (走普通 RAG)。能力在**其他措辞**上有效 (盲写集证), 但 relationship/aggregate 的 NL 覆盖是**保守的**。缺口: 若要更广覆盖, 需重新权衡零污染门 (允许图对图形状题注入正确事实) —— 留作未来迭代的产品决策。
- **class-roster NL 能力放弃 (engine-only)。** NL 检测「某 class 有哪些域」固有脆弱 (class 名=常用词, 撞 "disposition events"/"positive findings")。`domains_in_class`/`class_sizes` 保留在 GraphEngine, 但 NL 不接。缺口: 若要 class 聚合的 NL, 需结构化「[ClassName] class」解析或 UI 选择器, 或经 **SP4 API / 校验器** 暴露。
- **co_users / model_defhome-邻接 = engine-only (Q2→spec 收窄, Rule A 揪出)。** Q2 选的「结构邻接/共用」含 same_class + codelist_co_users + model_defhome 邻接; 写 spec §5.1 时只定义了 3 个 NL 意图 (impact/relationship/aggregate), same_class 并入 relationship, 但 **codelist_co_users 没分配 NL 意图** (引擎有 `codelist_co_users`, NL 不接)。Rule A slot 6 "与 AESER 共用 codelist 的变量" → None。spec 用户已批 (即 NL 3 意图), 故非违约, 但属 Q2 的 NL 覆盖收窄。co_users **可干净加** (锚定: 具名变量 + "same/share codelist" + 该变量有 CT, 非常用词脆弱) — 留作 fast-follow / SP4, 已向用户 flag。
- **mechanism:null 未 back-fill (50 curated 边)。** SP1 reviewer 提的确定性 RELREC/RELSPEC/RELSUB back-fill 仍 defer; advisory 非权威、NL 优雅省略, 不出错但不够具体。SP3+ 可选。
- **SP2 同源 degenerate 0-impact (858 codelist)。** SP3 impact 侧已修 (n==0 跳过), 但 **SP2 codelist 通道同样 pre-existing 行为未动** (不同措辞、已上线已默认开)。记为独立 SP2 后续小修 (两通道一起改更干净)。
- **implementer 自检纪律。** Phase 1 漏 mypy + 测试文件 ruff → 返工一轮。Phase 2/3 起在 implementer prompt **显式强制每 task 跑 mypy+ruff** 后不再发生。教训固化: 这类 prompt 默认必须写死三件套 (pytest+mypy+ruff)。

## 3. 关键决策复盘

- **D1 — brainstorm 5 决策 (Q1-Q5) 全部站住**: 图引擎+NL 都做 / 全 4 能力族 / 低保真 advisory / 确定性为主验证 / 纯 Python+可换接口。无返工。
- **D2 — 从 NL 去掉 class-roster (枢纽决策)。** 不是预先设计的, 是实现中振荡暴露了「class 名常用词」的固有脆弱后, 我把岔路交给用户决定的。选 robustness > 保功能但脆弱; 引擎保留能力。reviewer 评「比我要求的紧框架更 structurally clean」。**复盘: 当一个 NL 意图反复振荡, 那往往是信号——这个意图本身不可靠地可检测, 该重新审范围而非继续调参。**
- **D3 — 接地闸只硬校验 rare-subject 计数 (impact codelist/var), class 名不闸。** MED 教训: common-word subject (class 名) 做闸 subject 会 reintroduce SP2 36→0 的假阳类。原则固化: **闸的 subject 必须是稀有 token (var 名/C 码), 常用词不能当 grounding 锚。**
- **D4 — 零污染作硬门。** 严格但抓到了真 HIGH; 代价是 NL 覆盖保守 (见缺口 1)。复盘: 硬门值得 (防回归 > 边际覆盖), 但应在 spec 里把「图对图形状测试题静默」显式记为设计取舍, 避免被当 bug。
- **D5 — 控制器在 subagent 之间亲自重跑 + 不替 subagent 改代码 (除 flag/doc)。** 既 preserve context 又独立验证; 发现 3 处 implementer 自报与实际的偏差。值得保留。

## 4. 验收 (三门, PASS)
- **程序门**: 引擎 vs raw meta.yaml 穷举对账 + 意图 must-fire/not-fire 电池 + **140q 零污染 0/140 (composite path)** + 接地闸单测 + 盲写 10 题 NL 端到端 (基数对账 meta.yaml) + 全套 **414 passed** + mypy/ruff (SP3 文件) clean + 运行时 composite ON==OFF byte-identical。
- **规则 D**: 三轮异 type 独立审 (Phase1/Phase2/最终), 最终 APPROVE 0 BLOCKER/HIGH。详 `evidence/checkpoints/sp3_ruleD_review.md`。
- **规则 A**: N=8 分层语义抽检 (独立 scientist), 详 `evidence/checkpoints/sp3_ruleA_audit.md`。

## 5. 产出
- 代码: `server/graph_engine.py` (新) + `server/graph_answer.py` (新) + `structured_answer.py` (advisory_block/merge_facts/CompositeAnswerer) + `grounding.py` (impacted_* kinds) + `meta_store.py` (same_class/relations_curated/ct_codes_for_variable/model_defhome_map) + config/main/run_eval 接线。
- 测试/工具: `test_graph_engine.py` / `test_graph_answer.py` + `eval/prod_wirein/sp3_graph_probes.py` (held-out + 140q 零污染) + `eval/test_set_sp3_graph.yml` (盲写 10 题)。
- 文档: spec `docs/superpowers/specs/2026-06-20-sp3-graph-queries-design.md` + plan + 本 retro + 证据 2 份。
- 下一步: **SP4 (可选 Neo4j+Cypher+可视化)** / **SP5 (可选 图增强校验器)** — 均可选; class-roster + mechanism back-fill + 更广 NL 覆盖可在那里或独立小修处理。
