# KG 重启 — 子项目路线图 + 设计状态 (handoff)

> 2026-06-17 · **SP1 (meta.yaml 元数据层) DONE ✅** (brainstorm→spec→plan→9 Task TDD→Rule A/D 全过)。
> 2026-06-20 · **SP2 DONE ✅** — Phase 1 (答题通道, 默认 ON) + **Phase 2 (退役正则影子 KG) DONE** (structured_lookup 索引改读 meta.yaml; 严格行为等价 9891+4177 查询 0 divergence; Rule D APPROVE)。详见下方「SP2 Phase 1/2 DONE」段。
> 2026-06-20 · **SP3 (关系/影响查询) DONE ✅ 默认 ON** — 内存图引擎 (`GraphEngine` + 可换 `GraphBackend`) + NL 图答题 (`GraphAnswerer` 经 `CompositeAnswerer` 并入 SP2 通道)。能力: 影响/级联 · 跨域聚合 (variables_in_min_domains + most_shared) · 结构 (same_class via relationship) · 域间关系发现 (advisory)。**140q 零污染 0/140 (composite ON==OFF byte-identical)**, Rule D 三轮 APPROVE, Rule A N=8 PASS。详见下方「SP3 DONE」段。
> 2026-06-21 · **KG 价值 eval DONE ✅ — verdict: SP2 是 KG 价值, SP3 图层端到端≈0** (3-臂 × 3 模型, ΔSP2 +14~16pp 三模型一致 / ΔSP3≈0; SP3 唯一正向=aggregate 聚合但 NL 仅 45% 触发 + impact 与 SP2 byte-identical 冗余; Rule A ACCEPT-WITH-RESERVATIONS)。**结论: SP4/SP5 不靠答案质量证明** — 仅当要交互式图浏览 UX 才值。证据 `evidence/checkpoints/kg_value_eval.md` + `evidence/RETROSPECTIVE_kgval.md`。详见下方「KG 价值 eval DONE」段。
> 2026-07-07 · **AGG (aggregate 独立通道) DONE ✅ 默认 ON** — 价值 eval 两条榨值建议落地: aggregate 拆出 `AggregateAnswerer` + pattern-level 触发重写。ds 端到端 **Δ+41.7pp** (OFF 58%→ON 100%, 零退化); fire-rate 诚实口径 = 阈值族 novel 盲题 100% / 最高级族 25% (长尾入 backlog, 等 dogfood 信号); 140q 零污染 0/140; Rule D 整改完成 + Rule A 6/6。详见下方「AGG DONE」段。
> 用户决策: **SP1-5 全做**, 按依赖顺序逐个 (每个子项目走 设计→spec→plan→实现 循环)。**SP1-3 + AGG 全 DONE; SP4/SP5 均可选 (价值 eval 后: 仅产品 UX 理由, 非精度)。**
> 恢复方式: 新 session 说 **「KG 重启 开始任务」** → 读本文件 + memory `project_kg_decision` → 接 **SP4 (可选 Neo4j+Cypher+可视化) 或 SP5 (可选 图增强校验器)** = 新设计单元, 必须先 re-invoke `superpowers:brainstorming` (均可选; 若不要可视化/校验器则 KG 主线已收口)。
> ⚠️ **HARD-GATE (每个新设计单元)**: 先把设计问完 + 出 spec + 用户批准, 再 `writing-plans`/写码。**别跳过设计直接实现**。(SP4/SP5 是新单元, 必须走 brainstorm。)

## 已 settled (别再 re-litigate)

- KG **≠ 提检索精度** (检索已 99%)。真价值 = **新能力**: 计数/穷举 (q103「43 域」/q104「36 变量」今天答错)、影响/级联分析、替换 `server/structured_lookup.py` 里脆弱的正则「影子 KG」。
- 路径: deploy (DONE) → **meta.yaml (63 域)** → 可选 Neo4j。meta.yaml 便宜 + 立刻修计数/穷举 + 是 Neo4j 硬前置。
- **重定位 (本次 brainstorm 用户 ack)**: 能力 (计数/穷举/影响/关系) 在 SP1-SP3 用 **meta.yaml + 内存图遍历** 就能交付; **Neo4j 降级为「要不要可视化 / 临时 Cypher 探索界面」的产品选择, 不是能力前置**。省 16GB 机器多跑一个图库。
- 原始完整图 schema (节点/关系/示例 Cypher) 详 `docs/DESIGN_RAG_KG.md` §5 — 可复用做 meta.yaml/内存图的形状参考。

## 子项目 (依赖顺序; 用户要全做)

- **SP1 — `meta.yaml` 元数据层** ✅ **DONE 2026-06-17** (基础, 硬前置): `scripts/build_meta.py` 确定性生成 `data/meta/meta.yaml` (64 域=63 真域+DI 桩; 变量 name/role/type/core/`ct_codes`/`ct_dict` + `same_class` + `relations_curated`[机制仅字面] + `model_defhome` + `codelists`) + `scripts/reconcile_meta.py` 独立锚对账。reconcile gate 抓修 `spec_loader` 247 幻变量 bug; 桩域是 DI 非 SUPPQUAL。Gate1 8/8 + Rule D APPROVE + Rule A N=8 PASS。详见下方「SP1 DONE」段。
- **SP2 — 确定性结构化答题通道** ✅ **DONE**: **Phase 1 (答题通道) DONE 默认 ON** (meta.yaml 载内存 → `/api/ask` 计数/穷举/属性/CT 走确定数据, q103/q104 翻绿); **Phase 2 (退役 structured_lookup 正则) DONE** (索引全改读 meta.yaml/MetaStore, 退役 load-bearing `len==6` + spec.md xref + VARIABLE_INDEX 解析 + `_cross_check_vars`; 严格行为等价, 净删 ~185 行)。详见下方「SP2 Phase 2 DONE」段。
- **SP3 — 关系/影响查询** ✅ **DONE**: meta.yaml 之上**纯 Python 内存图引擎** (`GraphEngine` + 可换 `GraphBackend` seam) + NL 答题 (`GraphAnswerer`)。"改 C66742 影响哪些域/变量"、"哪些变量跨 >N 域"、域间关系发现 (advisory)。class-roster + codelist_co_users 保留 engine-only (NL 未接, 见下方「SP3 DONE」段)。详见下方「SP3 DONE」段。
- **SP4 (可选) — Neo4j + Cypher + 混合路由**: 仅当要可视化图浏览器 / 临时 Cypher 探索界面作产品界面才上 (DESIGN §5.4/§5.5)。
- **SP5 (可选) — 图增强校验**: 影响/级联检查接进 Validator (impact analysis / cross-domain completeness / CT cascade, DESIGN §5.6)。

## SP1 DONE (2026-06-17) — 交付与发现

- **产出**: `scripts/build_meta.py` (确定性生成器, 无 LLM, 幂等) → `data/meta/meta.yaml` (64 域=63 真域+DI 桩) + `scripts/reconcile_meta.py` (独立锚对账, 不复用 spec_loader) + `scripts/tests/test_build_meta.py` (13 单测)。设计 `SP1_meta_yaml_design.md` / 计划 `PLAN_sp1_meta_yaml.md` / 证据 `evidence/checkpoints/sp1_meta_audit.md`。
- **5 设计决策** (接地 recon workflow): 纯数据层 (q103/q104 翻绿留 SP2) / schema 见 SP1 bullet / relations 确定性 core + 策划边(机制仅字面,低保真) / 验收两门(独立锚对账 + N=8 Rule A) / 输出 `data/meta/`。
- **重大发现**: reconcile gate 抓出并修 `spec_loader._parse_spec` 系统性 bug (`###` 扫描不停在 Cross References → 全 63 域 247 幻变量; 独立锚揪出, 自我对账永远发现不了)。纠正 recon: 桩域是 **DI** 非 SUPPQUAL, `counts_toward_63 = spec.md 存在`。
- **三门**: Gate1 reconcile 8/8 (63/1917/1523/1005/37939/TAETORD→43/VISITDY→36/裸 Order 1917) + Rule D opus 异 type APPROVE (mypy0/ruff清/300测试) + Rule A 独立 N=8 分层语义抽检 PASS。

## SP2 Phase 1 DONE (2026-06-20) — 交付与发现

- **产出**: `server/meta_store.py` (MetaStore: 载 meta.yaml + 内存反向索引 + 确定性查询 API) + `server/structured_answer.py` (StructuredAnswerer 实体锚定+意图检测+事实装配, augment_context) + `server/grounding.py` (apply_counting_gate 高精度 v2) + router/main/config/eval 接线 + `eval/prod_wirein/heldout_probes.py`。spec `docs/superpowers/specs/2026-06-19-sp2-structured-answer-design.md` / plan `docs/superpowers/plans/2026-06-19-sp2-structured-answer.md` / 复盘 `RETROSPECTIVE_sp2_phase1.md` / 证据 `evidence/checkpoints/sp2_phase1_{paired_eval,ruleA_audit}.md`。`structured_answer_enabled` 默认 ON (env 可回滚)。
- **5 决策 (Q1-Q5) + 2 参数**: 见 spec §2。两阶段顺序 / 注入权威事实块+计数接地闸 / 确定性代码路由 / 能力=计数+穷举+属性+CT / 闸追加更正; Rule A N=8、闸只硬校验计数。
- **重大发现 (评测暴露)**: (1) 计数接地闸 v1 在真实 140q 评测上 36 个全假阳 (整句扫数字, 把术语数/字符限值误判为域计数) → 重建 v2「缺席前提 + 双语 kind 词邻近 + 合理性」, 36→0。(2) Rule A N=8 抽检揪出 q67 codelist 变量计数幻觉 (答 106/真值 123, 而 fact_recall 子串假阳给 1.0) → 补 codelist 变量计数闸。**两者都是程序门 (fact_recall) 漏掉、独立验收门抓到的——印证规则 A/D 价值。**
- **验收**: q103 TAETORD→43 / q104 VISITDY→36 翻绿 (fr 0.5→1.0); 检索零回归 (src 99.6%→99.6%); 0 计数闸 violation (闸 v2 oracle); Rule D (critic 异 type) APPROVE「safe default-ON」; Rule A N=8 PASS。
- **backlog (转复盘 §2)**: 词典词变量 (RACE/SEX) 锚定 relevance gate / s05 codelist 元数据注入 / enumerate corpus 列表 / FP2 是否改 eval-log-only / first-seen 属性跨域分歧 (→SP3)。

## SP2 Phase 2 DONE (2026-06-20) — 交付与发现

- **产出**: `server/structured_lookup.py` 重写 (净 −185 行) — 7 个索引全改读 MetaStore/meta.yaml, 退役 load-bearing `len(inner)==6` model 解析 + spec.md Cross-References 正则 + terminology 标题解析 + VARIABLE_INDEX 解析 + `_cross_check_vars` 截断回填 + 死代码 `ctcode_to_vars`; **意图/锚定/resolve()/长名匹配逻辑逐字保留**, 只换数据源。唯一仍读 KB 文件的是 ch04 glob (meta 不覆盖 chapters/)。`MetaStore` 加 2 纯加法 API (`ct_codes_for_variable` 跨域 union + `model_defhome_map`)。`rag.py` 懒构造 MetaStore (RAGEngine 签名不变, 另 5 调用点零改)。
- **零回归证明 (比 retrieval eval 更强)**: 穷举快照 harness `eval/prod_wirein/sp2p2_equiv_snapshot.py` — 同脚本跑旧/新码, 7 map + `resolve()` 在 9891 查询 (140 题 + 全量变量/CT/域扫描) 上**逐字节 diff** = `8/8 maps + 9891/9891 identical`。理由: structured_lookup 只经 union-add 影响检索, cosine/hybrid 未碰 → resolve 同 ⇒ 检索确定性同。
- **关键发现**: `var_to_termfiles` 必须用**跨域 union** 才与旧码 524 逐项相同 (FOCID 的 C119013 只在 OE 域, first-seen 会丢) → 加 `ct_codes_for_variable`。`model_defhome` meta 与旧 `len==6` 图逐项相同 (59=59) → 退役安全。
- **三门**: 程序门 (快照等价 + 375 passed + held-out 4/4 + ruff/mypy clean + 运行时 smoke) + Rule D 异type APPROVE (reviewer 重建旧码同进程对跑 + 自建 4177 对抗语料 0 divergence) + Rule A N/A (纯检索侧等价, 无新答题语义)。
- **缺口 (LOW, 已缓解)**: meta/KB 漂移自愈丢失 (旧码实时重解析自愈) → 加 `TestMetaKBDriftGuard` 域级闸; var/CT 级仍需手动 `reconcile_meta.py`。
- 复盘 `RETROSPECTIVE_sp2_phase2.md` / 证据 `evidence/checkpoints/sp2_phase2_{paired_eval,ruleD_review}.md`。

## SP3 DONE (2026-06-20) — 交付与发现

- **产出**: `server/graph_engine.py` (`GraphBackend` Protocol + `DictBackend` + `GraphEngine`: impact_of_codelist/variable, variables_in_min_domains, most_shared_codelists, same_class_domains, codelist_co_users, domain_relations, domains_in_class/class_sizes) + `server/graph_answer.py` (`detect_graph_intents` + `GraphAnswerer`) + `structured_answer.py` (`advisory_block`/`merge_facts`/`CompositeAnswerer`) + `grounding.py` (impacted_* kinds) + config/main/run_eval 接线 + `eval/prod_wirein/sp3_graph_probes.py` + `eval/test_set_sp3_graph.yml` (盲写 10 题)。spec/plan `docs/superpowers/{specs,plans}/2026-06-20-sp3-graph-queries*.md`; 复盘 `RETROSPECTIVE_sp3.md`; 证据 `evidence/checkpoints/sp3_rule{D,A}_*.md`。
- **NL 暴露 4 意图**: impact (codelist/variable→域/变量 + 接地闸校验基数) · relationship-discovery (单域→same_class 权威 + curated advisory) · aggregate (variables_in_min_domains + most_shared)。**engine-only (NL 未接)**: domains_in_class/class_sizes (class 名常用词→NL 脆弱) + codelist_co_users + model_defhome 邻接 (留 SP4/API)。
- **重大发现 (review 揪出)**: ① 140q 零污染门: class-roster 意图 (class 名常用词撞散文) 破门 → **从 NL 去掉 class-roster** (用户决策, 引擎保留); ② class_domains 接地闸 reintroduce SP2 假阳 (common-word subject) → ungate, 闸只锚 rare-subject (var/C 码); ③ degenerate 0-impact codelist (858 个) 注入误导 → 跳过。
- **三门**: 程序门 (引擎 vs raw meta.yaml 穷举对账 + 140q 零污染 0/140 composite path + 盲写 10 题基数对账 + 414 passed + mypy/ruff) + Rule D 三轮异 type APPROVE + Rule A N=8 PASS (独立 scientist vs meta.yaml+KB)。
- 注意 (来自 SP1 reviewer, 仍 defer): `relations_curated.mechanism: null` = 「散文未声明」非「无机制」; target 本身是 RELREC/RELSPEC/RELSUB 时机制结构上确定, 可做确定性 back-fill (非臆造)。

## KG 价值 eval DONE (2026-06-21) — verdict 与证据

- **路由词「KG 价值 eval 开始任务」已执行完毕** (`KG_VALUE_EVAL_KICKOFF.md` 立项 → `KG_VALUE_EVAL_PLAN.md` 执行)。
- **设计**: 3-臂 (arm0 检索 / arm1 +SP2 / arm2 +SP2+SP3=生产) × 3 模型 (ds deepseek-chat / gpt4o / gpt54 真前沿); 40 盲写题 4 family; gold meta.yaml 程序导 + 独立 reconcile (raw-yaml 40/40) + 独立 reviewer (Rule D); 指标 = 确定性 set_recall (主) + cardinality + judge (佐证); **fire-rate 仪表**。
- **verdict**: **KG 通道整体大赢 (judge +14~16pp) 但价值几乎全来自 SP2** (计数/穷举/CT, 三模型一致); **SP3 图层端到端 ΔSP3≈0** (set_recall +2~4pp)。SP3 唯一正向=**aggregate 聚合** (+11~17pp, SP2 不做) + 6 题 SP3-unique; 被稀释到 0 因: NL **仅 45% 触发** + impact 上与 SP2 **byte-identical 冗余** + relationship ΔSP3=0。
- **Rule A 对抗审计**: ACCEPT-WITH-RESERVATIONS; **推翻初版「relationship 注入反伤」误判** (实为 rl05 SP3 未触发的解码变异) + 抓 judge iv01 对纯基数答案判松 (set_recall 免疫)。
- **对 SP4/SP5 的含义**: **不靠答案质量证明继续投资**。SP4 (Neo4j/可视化) / SP5 (图校验器) **仅当要交互式图浏览 UX 作产品功能才值** — 非精度决策。榨取 SP3 已有价值性价比最高的是: ① 拓宽 SP3 NL 触发面 (45%→更高, 当前最大瓶颈) ② 把 aggregate 聚合并入 SP2。
- 证据: `evidence/checkpoints/kg_value_eval.md` + `evidence/RETROSPECTIVE_kgval.md` + `evidence/failures/kgval_gpt54_arm2_quota.md`; 资产 `eval/{gen_kgval_goldset,reconcile_kgval_gold,assemble_kgval_testset}.py` + `eval/test_set_kg_value.yml` + `eval/prod_wirein/{kgval_fire_probe,analyze_kgval}.py`。

## AGG DONE (2026-07-07) — 交付与发现

- **产出**: `server/aggregate_answer.py` (新: `detect_aggregate_intents` 9 形状类 + word-boundary anchor 同义词 datasets/vars + `AggregateAnswerer`, 装配逐字平移 SP3 golden 钉死) 注册 CompositeAnswerer (SP2→AGG→SP3); `graph_answer.py` 删 aggregate 回归纯图; flag `aggregate_answer_enabled` 默认 ON。评测资产: 3 轮盲写 held-out + novelty-check 工具 (`eval/novelty_check.py`) + e2e 26 题 + `agg_fire_probe/analyze_agg_e2e`。
- **五门**: 单测 48 + 140q 零污染 0/140 (artifact 落盘) + fire-rate (r3 门 15/16; **诚实口径** novelty 补充集: 阈值族 4/4=100% / 最高级族 2/8=25%) + **ds e2e Δ+41.7pp** (held-out OFF 58%→ON 100%, 26 题零退化, 审查者独立复算) + Rule D 整改完成/Rule A 6/6。证据 `evidence/checkpoints/agg_channel_summary.md` + `agg_rule{D,A}_*.md`。
- **重大发现**: ① 盲写收敛 — 同一 need card 跨轮盲写措辞收敛, "fresh held-out" 必须过 novelty check (Rule D 抓出, 流程工具已沉淀); ② 词法 pattern 对最高级家族有措辞长尾天花板 (每轮盲写挖出新同义表达), **用户决策: 诚实披露收口**, 长尾造册等 dogfood ⚑ 信号; ③ 触发时价值极大且零风险 (静默=与无通道等价)。
- 2 次门失败归档 `evidence/failures/agg_attempt_{1,2}.md` (规则 B); 5 轮 shape-level 修复全程无按题硬编 (Rule D 逐条判定)。

## 下一步 — SP4/SP5 仅产品 UX 理由 (非精度)

- **价值 eval 两条榨值建议已由 AGG 落地** (触发面 + aggregate 独立通道化)。
- **SP4 (可选)** Neo4j + Cypher + 可视化图浏览器 / 临时探索界面 (DESIGN §5.4/§5.5)。
- **SP5 (可选)** 图增强校验器: impact / 跨域完整性 / CT 级联一致性 接进 Validator (DESIGN §5.6)。
- **可选小补 (SP4 或独立)**: codelist_co_users NL 接入 (Q2 选过, 干净可加) / mechanism:null back-fill / SP2 同源 degenerate 0-impact codelist 修 / AGG backlog (最高级长尾 KL-4 + MED-1/2/3 注入侧收紧, 见 `agg_channel_summary.md`)。
- 均为**新设计单元**: 必须先 `superpowers:brainstorming` → spec → 用户批准 → plan。若用户不要可视化/校验器, KG 主线 (能力交付) 已于 SP3+AGG 收口。
