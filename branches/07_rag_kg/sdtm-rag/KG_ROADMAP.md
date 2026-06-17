# KG 重启 — 子项目路线图 + 设计状态 (handoff)

> 2026-06-17 · **SP1 (meta.yaml 元数据层) DONE ✅** (brainstorm→spec→plan→9 Task TDD→Rule A/D 全过)。**下一个 = SP2**。
> 用户决策: **SP1-5 全做**, 按依赖顺序逐个 (每个子项目走 设计→spec→plan→实现 循环)。
> 恢复方式: 新 session 说 **「KG 重启 开始任务」** → 读本文件 + memory `project_kg_decision` → **进 SP2 (确定性答题通道) brainstorming**。
> ⚠️ **HARD-GATE (每个子项目)**: 先把设计问完 + 出 spec + 用户批准, 再 `writing-plans`/写码。**别跳过设计直接实现**。

## 已 settled (别再 re-litigate)

- KG **≠ 提检索精度** (检索已 99%)。真价值 = **新能力**: 计数/穷举 (q103「43 域」/q104「36 变量」今天答错)、影响/级联分析、替换 `server/structured_lookup.py` 里脆弱的正则「影子 KG」。
- 路径: deploy (DONE) → **meta.yaml (63 域)** → 可选 Neo4j。meta.yaml 便宜 + 立刻修计数/穷举 + 是 Neo4j 硬前置。
- **重定位 (本次 brainstorm 用户 ack)**: 能力 (计数/穷举/影响/关系) 在 SP1-SP3 用 **meta.yaml + 内存图遍历** 就能交付; **Neo4j 降级为「要不要可视化 / 临时 Cypher 探索界面」的产品选择, 不是能力前置**。省 16GB 机器多跑一个图库。
- 原始完整图 schema (节点/关系/示例 Cypher) 详 `docs/DESIGN_RAG_KG.md` §5 — 可复用做 meta.yaml/内存图的形状参考。

## 子项目 (依赖顺序; 用户要全做)

- **SP1 — `meta.yaml` 元数据层** ✅ **DONE 2026-06-17** (基础, 硬前置): `scripts/build_meta.py` 确定性生成 `data/meta/meta.yaml` (64 域=63 真域+DI 桩; 变量 name/role/type/core/`ct_codes`/`ct_dict` + `same_class` + `relations_curated`[机制仅字面] + `model_defhome` + `codelists`) + `scripts/reconcile_meta.py` 独立锚对账。reconcile gate 抓修 `spec_loader` 247 幻变量 bug; 桩域是 DI 非 SUPPQUAL。Gate1 8/8 + Rule D APPROVE + Rule A N=8 PASS。详见下方「SP1 DONE」段。
- **SP2 — 确定性结构化答题通道**: meta.yaml 载内存 → `/api/ask` 对计数/穷举/精确查找走确定数据 (q103/q104/q126 答对) + 退役正则影子 KG。
- **SP3 — 关系/影响查询**: meta.yaml 之上**内存图遍历** (networkx / 纯 Python): "改 C66742 影响哪些域/变量"、"哪些变量跨 >N 域"、关系发现; 接入 chat/API。
- **SP4 (可选) — Neo4j + Cypher + 混合路由**: 仅当要可视化图浏览器 / 临时 Cypher 探索界面作产品界面才上 (DESIGN §5.4/§5.5)。
- **SP5 (可选) — 图增强校验**: 影响/级联检查接进 Validator (impact analysis / cross-domain completeness / CT cascade, DESIGN §5.6)。

## SP1 DONE (2026-06-17) — 交付与发现

- **产出**: `scripts/build_meta.py` (确定性生成器, 无 LLM, 幂等) → `data/meta/meta.yaml` (64 域=63 真域+DI 桩) + `scripts/reconcile_meta.py` (独立锚对账, 不复用 spec_loader) + `scripts/tests/test_build_meta.py` (13 单测)。设计 `SP1_meta_yaml_design.md` / 计划 `PLAN_sp1_meta_yaml.md` / 证据 `evidence/checkpoints/sp1_meta_audit.md`。
- **5 设计决策** (接地 recon workflow): 纯数据层 (q103/q104 翻绿留 SP2) / schema 见 SP1 bullet / relations 确定性 core + 策划边(机制仅字面,低保真) / 验收两门(独立锚对账 + N=8 Rule A) / 输出 `data/meta/`。
- **重大发现**: reconcile gate 抓出并修 `spec_loader._parse_spec` 系统性 bug (`###` 扫描不停在 Cross References → 全 63 域 247 幻变量; 独立锚揪出, 自我对账永远发现不了)。纠正 recon: 桩域是 **DI** 非 SUPPQUAL, `counts_toward_63 = spec.md 存在`。
- **三门**: Gate1 reconcile 8/8 (63/1917/1523/1005/37939/TAETORD→43/VISITDY→36/裸 Order 1917) + Rule D opus 异 type APPROVE (mypy0/ruff清/300测试) + Rule A 独立 N=8 分层语义抽检 PASS。

## 下一步 — SP2 (确定性结构化答题通道)

新 session 说「KG 重启 开始任务」→ 读本文件 + memory → **进 SP2 brainstorming**。
- SP2 = meta.yaml **载内存** → `/api/ask` 对计数/穷举/精确查找走确定数据 (**q103/q104 翻绿**) + **退役 `structured_lookup.py` 正则影子 KG** (含用 SP1 已产的 `model_defhome` 数据替换那段脆弱 `len==6` 解析)。
- 注意 (来自 SP1 reviewer): `relations_curated.mechanism: null` 表示「散文未声明」非「无机制」; target 本身是 RELREC/RELSPEC/RELSUB 时机制结构上确定, 可在 **SP3** 做确定性 back-fill (非臆造)。
- ⚠️ HARD-GATE: SP2 也先设计问完 + spec + 用户批准, 再 `writing-plans`/写码。之后 SP3 (内存图遍历)、SP4/SP5 (可选) 逐个同样流程。
