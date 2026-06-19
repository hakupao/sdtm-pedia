# KG 重启 — 子项目路线图 + 设计状态 (handoff)

> 2026-06-17 · **SP1 (meta.yaml 元数据层) DONE ✅** (brainstorm→spec→plan→9 Task TDD→Rule A/D 全过)。
> 2026-06-20 · **SP2 Phase 1 (答题通道) DONE ✅ 默认 ON** (brainstorm→spec→plan→subagent-driven 14 task; q103/q104 翻绿, 检索零回归, 0 闸 violation, Rule D APPROVE + Rule A PASS)。**SP2 Phase 2 (退役正则) 待做**。详见下方「SP2 Phase 1 DONE」段。
> 用户决策: **SP1-5 全做**, 按依赖顺序逐个 (每个子项目走 设计→spec→plan→实现 循环)。
> 恢复方式: 新 session 说 **「KG 重启 开始任务」** → 读本文件 + memory `project_kg_decision` → 接 **SP2 Phase 2** (plan §Phase 2, Tasks 15-18) 或 backlog。下一个新设计单元 (SP3 关系查询) 才需 re-invoke `superpowers:brainstorming`。
> ⚠️ **HARD-GATE (每个新设计单元)**: 先把设计问完 + 出 spec + 用户批准, 再 `writing-plans`/写码。**别跳过设计直接实现**。(SP2 Phase 2 已有 spec+plan, 直接接 plan 即可。)

## 已 settled (别再 re-litigate)

- KG **≠ 提检索精度** (检索已 99%)。真价值 = **新能力**: 计数/穷举 (q103「43 域」/q104「36 变量」今天答错)、影响/级联分析、替换 `server/structured_lookup.py` 里脆弱的正则「影子 KG」。
- 路径: deploy (DONE) → **meta.yaml (63 域)** → 可选 Neo4j。meta.yaml 便宜 + 立刻修计数/穷举 + 是 Neo4j 硬前置。
- **重定位 (本次 brainstorm 用户 ack)**: 能力 (计数/穷举/影响/关系) 在 SP1-SP3 用 **meta.yaml + 内存图遍历** 就能交付; **Neo4j 降级为「要不要可视化 / 临时 Cypher 探索界面」的产品选择, 不是能力前置**。省 16GB 机器多跑一个图库。
- 原始完整图 schema (节点/关系/示例 Cypher) 详 `docs/DESIGN_RAG_KG.md` §5 — 可复用做 meta.yaml/内存图的形状参考。

## 子项目 (依赖顺序; 用户要全做)

- **SP1 — `meta.yaml` 元数据层** ✅ **DONE 2026-06-17** (基础, 硬前置): `scripts/build_meta.py` 确定性生成 `data/meta/meta.yaml` (64 域=63 真域+DI 桩; 变量 name/role/type/core/`ct_codes`/`ct_dict` + `same_class` + `relations_curated`[机制仅字面] + `model_defhome` + `codelists`) + `scripts/reconcile_meta.py` 独立锚对账。reconcile gate 抓修 `spec_loader` 247 幻变量 bug; 桩域是 DI 非 SUPPQUAL。Gate1 8/8 + Rule D APPROVE + Rule A N=8 PASS。详见下方「SP1 DONE」段。
- **SP2 — 确定性结构化答题通道**: **Phase 1 (答题通道) DONE ✅ 默认 ON** (meta.yaml 载内存 → `/api/ask` 计数/穷举/属性/CT 走确定数据, q103/q104 翻绿); **Phase 2 (退役 structured_lookup 正则) 待做** (plan §Phase 2)。
- **SP3 — 关系/影响查询**: meta.yaml 之上**内存图遍历** (networkx / 纯 Python): "改 C66742 影响哪些域/变量"、"哪些变量跨 >N 域"、关系发现; 接入 chat/API。
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

## 下一步 — SP2 Phase 2 (退役 structured_lookup 正则影子 KG)

- **入口**: plan `docs/superpowers/plans/2026-06-19-sp2-structured-answer.md` §Phase 2 (Tasks 15-18)。已有 spec+plan, **直接接 plan, 无需再 brainstorm**。
- **做什么**: 把 `server/structured_lookup.py` 的索引从「正则解析 KB markdown」改为读 MetaStore/meta.yaml (含用 `model_defhome` 替换脆弱的 load-bearing `len==6` 解析); 意图/锚定/resolve 逻辑不变。
- **零回归门**: 既有 `scripts/tests/test_structured_lookup.py` 全套 (canary RDOMAIN→model/06, EPOCH→model/03) + retrieval-only paired eval ≥99% 零回归 + Rule D 一轮独立审。
- 注意 (来自 SP1 reviewer): `relations_curated.mechanism: null` 表示「散文未声明」非「无机制」; target 本身是 RELREC/RELSPEC/RELSUB 时机制结构上确定, 可在 **SP3** 做确定性 back-fill (非臆造)。
- 之后: SP3 (内存图遍历, 关系/影响查询) = 新设计单元, 需 re-invoke brainstorming; SP4/SP5 可选。
