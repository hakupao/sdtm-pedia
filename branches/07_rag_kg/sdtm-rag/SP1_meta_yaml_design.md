# SP1 — `meta.yaml` 元数据层 · 设计 (spec)

> 状态: **设计定稿待用户审** (2026-06-16)
> 来源: brainstorming 产物 (路由词「KG 重启 开始任务」)。上游 `KG_ROADMAP.md` (SP1-5) + memory `project_kg_decision`。
> 下游: 用户审通过 → `writing-plans` → 实现 (TDD + Rule A/D)。
> 接地证据: 本设计的每条数据断言来自 5 路并行侦察 (workflow `kg-sp1-recon`), 关键证据在正文标 `[evi]`。

---

## 0. 范围与非目标

**SP1 = 纯数据层**。产出 + 验证一份机生成的 `meta.yaml`, 对账 KB + Rule A 抽检即收口。**不答题、不翻 eval**。

**非目标 (明确踢出 SP1)**:
- q103/q104 翻绿 = **SP2** (确定性答题通道)。SP1 只保证 meta.yaml *能支撑* 这些计数 (见 §5 Gate 1 前瞻验)。
- 关系/影响查询 (内存图遍历) = **SP3**。
- Neo4j / Cypher = **SP4 (可选)**;图增强校验 = **SP5 (可选)**。
- **q126 永久 known limitation** (双重独立阻断: 单实例锚=例级作弊 + 架构只映 spec.md 无 sub-file 判别器), **不在任何 SP 验收范围** `[evi: d_channel_concept_definition.md:6,88-97]`。

---

## 1. 背景 (settled — 别 re-litigate)

- **KG ≠ 提检索精度** (检索已 99%)。真价值 = 评测从没测的**新能力**: 计数/穷举 (q103「43 域」/q104「36 域」今天答错)、影响/级联、以及**退役 `server/structured_lookup.py` 里脆弱的正则「影子 KG」**。
- `meta.yaml` 便宜、立刻给 SP2/SP3 当硬前置、**独立可验** (每个计数/关系都能对着 KB 核)。
- **重定位 (用户 ack)**: 能力在 SP1-3 用 meta.yaml + 内存图就能交付;Neo4j 降级为「要不要可视化界面」的产品选择, 非能力前置。

---

## 2. 数据源与可抽取性 (recon 实证)

| 字段 | 来源 | 确定性 | 证据 |
|------|------|--------|------|
| domain / class / label / structure | `domains/<D>/spec.md` H1 行 + `> Class: X \| Structure: Y` | **100%** (63/63, 0 缺失) | `AE/spec.md:1,3` |
| 变量 name/label/type/role/core | spec.md 每个 `### VAR` 块下 7 个固定 bullet | **100%**, 闭集 (Type∈{Char,Num}/Core∈{Req,Exp,Perm}/Role 固定 8 值) | `AE/spec.md:5-12` |
| ct_code(s) | 变量块 `- **Controlled Terms:**` | **100%**, 单 C 码 / 分号多码 `C..; C..` / 外部字典 token / 空 | grep: 113×ISO8601 / 45×duration / 11×MedDRA / 2×LOINC / 1×NullFlavor + 多码列表 |
| codelist 元数据 (submission value / 可扩展性 / 定义) | `terminology/**/*.md` 表 `\| Code \| Submission Value \| Synonym \| Definition \|` + `Extensible: Yes/No` | **100%** | `terminology/core/ae.md:5-7` |
| **关系机制 (RELREC/SUPP)** | **无结构化源** | **0%** — 仅通用变量定义 (RELREC/SUPPQUAL spec.md) + 散文 (ch08, 各域 `### Related Domains`) + 示例对 (RELREC/examples.md) | `RELREC/spec.md:50-66`; "via RELREC" 字样**只在 AE 出现** |
| 关系 target + 类别 (策划) | 各域 `### Related Domains` 跨类 bullet `**<Type>:** [DOM](../DOM/) — prose` | regex 净 (target+类别), **覆盖仅 28/63 域**, 1/63 无该小节 | `AE/spec.md:558-562`; VS 仅 same-class 无机制 |

**关键复用 / 独立锚**:
- `scripts/spec_loader.py` (246 行) **已存在**, 已产 `DomainSpec/VariableSpec(name/role/type/core/ct_code)` + `Codelist` + `known_domains()`。生成器在它之上即可。
- 独立计数锚 (生成器**不**经手, 用于破套套逻辑): `VARIABLE_INDEX.md` (1917 条目 / 1523 唯一 / 63 域)、`INDEX.md` (63 域 / 1005 codelist / 37939 term)。
- 变量数裸锚: spec.md `- **Order:**` 行数 = 1917 (`### ` 计数会多算节标题, 不可用)。

---

## 3. Schema (`meta.yaml` 形状)

采用 `DESIGN_RAG_KG.md §5.1` 的标量+变量部分**逐字照搬**, 在它实际数据粒度上做三处诚实调整 (ct 列表化 / 关系分层 / 加 model_defhome)。

```yaml
# data/meta/meta.yaml — 机生成, 勿手编. 生成器 scripts/build_meta.py
meta_version: 1
generated_from: knowledge_base/   # 单一真源
domains:
  - domain: AE
    class: Events
    label: Adverse Events
    structure: "One record per adverse event per subject"
    is_special: false              # SUPPQUAL=true (见下"开放细节 a")
    counts_toward_63: true
    variables:
      - name: AETERM
        label: Reported Term for the Adverse Event
        role: Topic
        type: Char
        core: Req
        ct_codes: []               # C 码列表 (可空)
        ct_dict: []                # 外部字典 token, 如 ["MedDRA"] (见"开放细节 b")
      - name: AESER
        label: Serious Event
        role: Record Qualifier
        type: Char
        core: Exp
        ct_codes: [C66742]
        ct_dict: []
    same_class: [BE, CE, DS, DV, HO, MH]        # 从 Class 派生, 确定
    relations_curated:                           # 显式 low-fidelity, 非权威
      - target: CM
        category: Treatment
        mechanism: RELREC          # 仅当散文字面写了才填, 否则 null
        note: "concomitant medications linked via RELREC"
        fidelity: curated_prose    # 永远标记来源, 提醒消费方非结构化
model_defhome:                     # 变量→引入它的 model 章节 (实际路径 build 时解析, 下为示意)
  RDOMAIN: model/06_relationship_datasets.md
  EPOCH: model/03_timing_variables.md
codelists:                         # ct_code → 元数据 (供 SP2 计数/解析; 不含 37939 term 全表)
  - ct_code: C66742
    name: "No Yes Response"
    extensible: false
    term_count: 2                  # 数量, 非全表枚举
    termfile: terminology/core/general_part4.md
```

**逐字段 provenance** (实现时每字段必须能 trace 到 file:line, 否则不写):

| 字段 | 来源 | 方法 |
|------|------|------|
| domain/class/label/structure | spec.md header | line parse |
| variables.* (5 标) | spec.md `### VAR` 块 | line parse (spec_loader) |
| ct_codes | `Controlled Terms` 分号切 + `^C\d+$` 过滤 | regex |
| ct_dict | `Controlled Terms` 里非 C 码 token | 闭集白名单 |
| same_class | Class 头 → 同类域聚合 | 派生 |
| relations_curated | `### Related Domains` 跨类 bullet | regex, mechanism 仅字面 |
| model_defhome | `model/*.md` 定义动词锚 | line parse |
| codelists | terminology/*.md `## Name (Cxxxxx)` + Extensible + 行计数 | parse |

**开放细节 (我替你拍板, 标清好让你审时可否决)**:

- **(a) 64-vs-63 (实现期查实修正 2026-06-16)**: 磁盘 64 个 domain 目录;缺 spec.md 的是 **DI**(仅 `assumptions.md`, 无变量), **不是 SUPPQUAL** —— SUPPQUAL 有完整 spec/assumptions/examples 且在 VARIABLE_INDEX/INDEX 的 63 域内 (INDEX.md L134 明列 SUPPQUAL; DI 仅在 model study-references 被提及)。原 recon 把 SUPPQUAL 当被排除的第 64 个是**错的**, 已纠。**决定**: meta.yaml 收录全 64 个 (SP3 关系可能指向 DI/OI, 留桩防悬挂); `counts_toward_63 = spec.md 存在` (DI=false, SUPPQUAL=true, 其余 true → 恰 63, 与 VARIABLE_INDEX「覆盖域 63」一致); `is_special = 无 spec.md 的桩目录` (当前仅 DI=true)。
- **(b) 外部字典 token**: `MedDRA/LOINC/ISO 8601.../ISO 21090 NullFlavor` **不是 C 码**、无 terminology 文件。**决定**: 不塞进 `ct_codes`, 单列 `ct_dict` 字段保留, `ct_codes` 永远只装可解析的 C 码。
- **(c) 文件布局**: **单文件 `data/meta/meta.yaml`** (SP2 一次 `safe_load`, 单一真源, YAML 行级可 diff)。若审下来嫌大可再切 per-domain;默认单文件。
- **(d) `model_defhome` 是否纳入 SP1**: 纳入**数据生成** (SP1 只产出这份映射数据)。它确定性可解析, 且正是 `structured_lookup.py` 里那个自述脆弱的 `len(inner)==6` LOAD-BEARING 表解析将来的退役依据 `[evi: structured_lookup.py:408-413]`。**注意**: SP1 不碰 structured_lookup 代码;实际把那段解析换成读 meta.yaml 是 **SP2** 的事。
- **(e) 反向索引不落盘**: 变量→域、CT码→变量(域.变量)、域长名→码 都是 meta.yaml 纯函数 → **SP2 载入内存时建** (dict/networkx), meta.yaml 不材化, 避免双写漂移。

---

## 4. 生成器设计

- `scripts/build_meta.py`: `spec_loader` 解析 63+1 域 → 组装 per-domain dict → emit `data/meta/meta.yaml`。**全程无 LLM** (relations_curated 也是 regex 抓散文, mechanism 只照字面填)。
- 幂等: 同 KB 输入 → 同字节输出 (YAML key 排序固定、无时间戳进正文)。
- `_cross_check_vars` 那类「补正则截断尾」的修补相 `[evi: structured_lookup.py:464-474]` 在完整 meta.yaml 下应可删除 (codelist 成员用完整源, 不再依赖 `13 total` 截断尾)。

---

## 5. 验收 (Rule A + Rule D + Rule B)

**Gate 1 — 自动·阻塞·独立锚计数对账** (`scripts/reconcile_meta.py`)
对账器**从 `VARIABLE_INDEX.md`/`INDEX.md` 文本独立复现计数, 绝不复用生成器的 `spec_loader`** (否则同义反复, 啥也没证)。断言清单:
- `counts_toward_63==true` 的域数 == **63**
- 变量条目总数 == **1917**;唯一变量名 == **1523**
- codelist 数 == **1005**;term 数 == **37939**
- **每域变量数** 对齐 (聚合对、单域错 = 补偿误差, 必须逐域)
- 裸 `- **Order:**` 计数 == 1917 (对 meta 条目数的**第二个独立锚**: 裸 grep vs VARIABLE_INDEX header —— 同一个量、两条独立提取路径; 两者都独立于生成器, 故对破「生成器套套逻辑」有效, 但非第三个独立量)
- **SP2 readiness 前瞻验**: 从 meta.yaml 推 `TAETORD → 43 域`、`VISITDY → 36 域` `[evi: judge_result_v3.json q103/q104]`
- 每个 `ct_codes` 元素都能在 `codelists`/terminology 找到对应 codelist

**Gate 2 — 手工·阻塞·N=8 分层 Rule A 抽检** (证据 `evidence/step_NN_audit.md`)
8 个分层槽 (打开 meta.yaml 条目 ↔ 打开 source spec.md/terminology, 逐字段 + 关系手核):
1. tiny 域 (如 TE/TD) 2. medium (如 VS) 3. large (如 AE 或 LB)
4. 特殊目的域 DM 5. 关系域 RELREC 6. SUPPQUAL (验 is_special/变量收录)
7. ct_code 多码解析 (分号列表 → 多 codelist) 8. relations_curated 一条 (验 target+mechanism 不臆造)

**Rule D — 审阅隔离**: 生成器代码 + reconciler 由**异 `subagent_type`** 独立审 (writer ≠ reviewer 同 context 自审无效)。
**Rule B — 失败归档**: 任何失败 attempt 归 `failures/`, 不删。

---

## 6. 风险 / 已知边界

- `relations_curated` **低保真**: 28/63 覆盖, 1/63 无 Related Domains, mechanism 多为 null。消费方 (SP3) 必须当「线索」非「权威关系矩阵」。**绝不发明边**。
- **`mechanism: null` 的语义 (code-review LOW #3 注记)**: null = 「散文未字面声明机制」, **不等于「无关系机制」**。SP2/SP3 消费方不可把 null 当「无机制」。实测全 52 条策划边仅 2 条 (→CM/→PR「via RELREC」) 有非 null 机制; 另有 5 条 (LB/BS/MB/IS/MS→RELSPEC) target 本身即 RELSPEC 数据集、机制结构上确定但散文没写。**确定性 back-fill** (当 target ∈ {RELREC,RELSPEC,RELSUB} 时机制即该 target) 是 **SP3 可选增强**, 属结构推断非臆造; SP1 守「仅字面」决策不做。
- `VARIABLE_INDEX.md` 生成于 2026-04-16, 可能与 spec.md 漂移 → 对账若不一致, **暴露漂移本身即价值** (而非判 meta.yaml 错前先查哪边对)。
- 套套逻辑陷阱: 已用「独立锚 + 第三方裸计数」破 (§5 Gate 1)。
- `ct_dict` 外部字典 token 无 codelist, 计数/解析对它无效 (设计如此)。

---

## 7. 交付物清单

- `data/meta/meta.yaml` (单文件)
- `scripts/build_meta.py` (生成器)
- `scripts/reconcile_meta.py` (独立锚对账)
- `scripts/tests/test_build_meta.py` (TDD: 字段解析 / ct 分号切 / SUPPQUAL flag / relations mechanism-仅字面 / 幂等;项目 `testpaths=["scripts/tests"]`)
- `evidence/step_NN_audit.md` (N=8 手检)
- `failures/` (如有失败 attempt)
- 不改 `server/structured_lookup.py` (退役是 **SP2** 的事;SP1 只产出 meta.yaml)

---

## 8. 不做 (YAGNI)

- 不材化反向索引 (SP2 内存建)
- 不材化 37939 个 term 全表 (terminology/ 已有;codelists 只存数量+termfile 指针)
- 不用 LLM 合成关系 (踩反作弊敏感点)
- 不碰 `knowledge_base/` (只读 authored)
- 不在 SP1 动答题层 / 不退役 structured_lookup (SP2)
