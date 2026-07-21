# Cypher Cookbook — SP4 Neo4j 探索层

7 条精选查询, 每条经 `eval/prod_wirein/sp4_cookbook_golden.py` (Gate 2) 逐字锚定到生产
`server.graph_engine.GraphEngine` / `server.meta_store.MetaStore`（生产等价 lane, 与 Gate 1
`scripts/reconcile_neo4j.py` 的 raw-yaml lane 分工不同, 详见 spec
`docs/superpowers/specs/2026-07-08-sp4-neo4j-exploration-design.md`）。

## 数据来源 & 重建

唯一源: `data/meta/meta.yaml`（SP1 reconcile-verified）。导入脚本
`scripts/build_neo4j.py` 是全量幂等 wipe+rebuild（先 `MATCH (n) DETACH DELETE n` 清库, 再
重建全部节点/边）, 不支持增量。meta.yaml 变了就重跑:

```bash
cd branches/07_rag_kg/sdtm-rag
.venv/bin/python scripts/build_neo4j.py       # 全量重建
.venv/bin/python scripts/reconcile_neo4j.py   # Gate 1 对账（应 41/41 PASS）
```

## Neo4j Browser 入口

`http://127.0.0.1:7474`（localhost-only, 不对外; 账密见本仓 gitignored `.env` 的
`NEO4J_USER`/`NEO4J_PASSWORD`）。bolt 端口 `bolt://127.0.0.1:7687`。

## `:param` 用法

Browser 里先单独执行一行 `:param` 设置参数, 再跑下面的查询主体（查询里的 `// :param ...`
是给人看的示例, 本身是 Cypher 注释, 不是可执行的 Browser 指令）:

```
:param code => 'C66742'
```

然后把对应查询的 Cypher 主体粘进同一个 Browser 标签页执行, `$code` 会取刚设置的值。用
`cypher-shell` 跑的话把 `$code` 换成字面量, 或用 `cypher-shell --param "code => 'C66742'"`。

## APOC 说明（重要）

本机 `brew install neo4j` 是裸装, **没有 APOC 插件**（`plugins/` 目录只有一个
`README.txt`）。实测:

```
cypher-shell> RETURN apoc.version();
42N48: ... The function apoc.version() was not found.
```

所以下面 7 条查询**全部是纯 Cypher**, 不依赖 `apoc.*`（①⑦ 在别处的草案里曾有
APOC 变体用于排序/合并集合, 这里统一改用 `collect(DISTINCT ...)` / `UNWIND` 达到同样效果,
结果集合完全等价, 只是不做服务端排序 — 排序在 Python 侧或 `ORDER BY` 里做）。

## advisory 边警示

`RELATED_TO`（Domain→Domain, 域间关系）是**curated / 低保真**, 来自散文来源的人工整理, 边上
带 `advisory: true` + `fidelity` 属性 — **仅供参考, 不进任何 golden 门, 不要当权威结论引用**。
`HAS_VARIABLE` / `USES_CT` / `IN_CLASS` / `DEFHOME` 四类是**结构边**, 直接从 meta.yaml
派生, 权威。

## model_only 变量说明

`Variable` 节点共 1541 个 = 1523 个出现在至少一个 IG 域的变量 + 18 个 `model_only: true`
的模型级变量（如 `APID`/`SETCD`/`SPECIES`/`STRAIN` 等, 只在 SDTM Model 章节定义, 不出现在
任何 IG 域, 也没有 `role`/`type`/`core` 属性）。做计数类查询时如果想只统计 IG 域里的变量,
自己加 `WHERE NOT v.model_only`；下面查询 ⑥ 的返回里用 `(model-only)` 后缀标出这类变量,
不做默认过滤。

---

## 1. 影响分析（impact）

改一个 codelist 波及哪些域/变量。`USES_CT.domains` 是该 (变量, codelist) 对实际生效的域列表
（逐域精确, 与生产 `GraphEngine.impact_of_codelist` 一致 — 不是"变量出现的所有域"的粗粒度
并集, 这是 C119013/FOCID 教训: FOCID 只在 OE 域用 C119013, 若按变量闭包算会错算成 3 域）。

```cypher
// 1 影响分析: 改一个 codelist 波及哪些域/变量 (参数化 C 码)
// USES_CT.domains = 该变量实际用此 CT 的域 (逐域精确, 与生产 GraphEngine 一致)
// 本机未装 APOC 插件, 用 collect(DISTINCT dom) 替代 apoc.coll.sort(...) (排序可省, 集合不变)
// :param code => 'C66742'
MATCH (c:Codelist {code: $code})<-[u:USES_CT]-(v:Variable)
UNWIND u.domains AS dom
RETURN c.code AS code, c.name AS codelist,
       count(DISTINCT v) AS n_variables, count(DISTINCT dom) AS n_domains,
       collect(DISTINCT dom) AS domains
```

期望结果形状: 单行。`code`/`codelist` 回显参数; `n_variables`/`n_domains` 是整数;
`domains` 是域码集合（无序）。

- `C66742`（"No Yes Response"）: **123 变量 / 41 域**（注意: spec §5 早期草案写的 44 是笔误,
  见 plan 偏差 D1, 以此处 123/41 为准）。
- `C119013`（FOCID 专用）: **1 变量 / 1 域**（`domains = ['OE']`）— 逐域精确回归护栏
  （D2）: 若错误地按变量出现的域闭包统计会得到 3 域, 这里必须是 1。

## 2. 变量跨域分布（min_domains）

哪些变量出现在 ≥ N 个域（跨域共性变量, 典型答案是 STUDYID/USUBJID 这类 identifier）。

```cypher
// 2 变量跨域分布: 哪些变量出现在 ≥ N 个域 (参数化阈值)
// :param min => 20
MATCH (d:Domain)-[:HAS_VARIABLE]->(v:Variable)
WITH v.name AS var, count(d) AS n_domains
WHERE n_domains >= $min
RETURN var, n_domains ORDER BY n_domains DESC, var
```

期望结果形状: 多行, 按 `n_domains` 降序、`var` 升序排列。

`min=20`: **8 行** — STUDYID 63, DOMAIN 59, USUBJID 55, EPOCH 44, TAETORD 43, VISIT 36,
VISITDY 36, VISITNUM 36。

## 3. same-class 邻域（same_class）

与某域同 observation class 的其他域（结构性同类, 不是策展关系）。

```cypher
// 3 same-class 邻域: 与某域同 observation class 的其他域
// :param dom => 'DM'
MATCH (d:Domain {code: $dom})-[:IN_CLASS]->(k:Class)<-[:IN_CLASS]-(o:Domain)
WHERE o.code <> d.code
RETURN k.name AS class, collect(o.code) AS siblings
```

期望结果形状: 单行, `siblings` 为域码集合（无序）。

`dom='DM'`: `class = 'Special-Purpose'`, `siblings = {CO, SE, SM, SV}`（集合相等, 顺序不定）。

## 4. codelist co-users（co_users）

与某变量共用同一 CT 的其他变量有哪些（"改这个 codelist 还会波及哪些兄弟变量"）。

```cypher
// 4 codelist co-users: 与某变量共用同一 CT 的其他变量
// :param var => 'AECONTRT'
MATCH (v:Variable {name: $var})-[:USES_CT]->(c:Codelist)<-[:USES_CT]-(o:Variable)
RETURN c.code AS code, c.name AS codelist, count(o) AS n_others
ORDER BY n_others DESC
```

期望结果形状: 每个变量用到的 codelist 各一行, 按 `n_others` 降序。

`var='AECONTRT'`: **1 行** — `C66742`（"No Yes Response"）, `n_others = 122`。

## 5. 类罗盘（class_compass）

某 observation class 下全部域一次看全（SP3 因 class 名撞常用词如 "Findings" 未把这条能力
暴露给自然语言问答, 在 Cypher 里直接查是安全的）。

```cypher
// 5 类罗盘: 某 observation class 下全部域 (SP3 因 class 名撞常用词未暴露 NL 的能力, Cypher 里安全)
// :param cls => 'Findings'
MATCH (d:Domain)-[:IN_CLASS]->(k:Class {name: $cls})
RETURN k.name AS class, k.n_domains AS n, collect(d.code) AS domains
```

期望结果形状: 单行, `n` 与 `size(domains)` 一致。

`cls='Findings'`: **n = 30**。

全类概览变体（非 golden, 探索用）:

```cypher
MATCH (k:Class) RETURN k.name, k.n_domains ORDER BY k.name
```

→ 8 行: Events 7 / Findings 30 / Findings About 2 / Interventions 7 / Relationship 4 /
Special-Purpose 5 / Study Reference 1 / Trial Design 7。

## 6. model_defhome 邻接（defhome）

某 model 章节定义的全部变量（`model_only=true` 的变量只在 SDTM model 出现, 不在任何 IG 域,
返回里用 `(model-only)` 后缀标出）。

```cypher
// 6 model_defhome 邻接: 某 model 章节定义的全部变量 (model_only=true 的变量只在 SDTM model 出现, 不在任何 IG 域)
// :param chapter => 'model/06_relationship_datasets.md'
MATCH (v:Variable)-[:DEFHOME]->(m:ModelChapter {path: $chapter})
RETURN m.path AS chapter, count(v) AS n, collect(v.name + CASE WHEN v.model_only THEN ' (model-only)' ELSE '' END) AS variables
```

期望结果形状: 单行, `variables` 集合应与 `MetaStore.model_defhome_map`（属性, 非方法）中
该章节对应的条目逐项相同（具体数值由 harness 用真实 store 现算比对, 不在此处写死）。

## 7. most-shared 排名（most_shared）

被最多变量共用的 codelist top-K（"最该优先做 CT 变更影响评估的 codelist 是哪些"）。

```cypher
// 7 most-shared 排名: 被最多变量共用的 codelist top-K (本机未装 APOC, 用 UNWIND 代替 apoc.coll.flatten/toSet)
// :param k => 5
MATCH (c:Codelist)<-[u:USES_CT]-(v:Variable)
UNWIND u.domains AS dom
WITH c, count(DISTINCT v) AS n_variables, count(DISTINCT dom) AS n_domains
RETURN c.code AS code, c.name AS name, n_variables, n_domains
ORDER BY n_variables DESC, code LIMIT $k
```

期望结果形状: `k` 行, 按 `n_variables` 降序、`code` 升序（并列时）。

`k=5`: C66742 123/41, C71620 58/32, C66789 36/36, C66728 26/9, C74456 19/19 — 与
`GraphEngine.most_shared_codelists(5)` 逐项一致。

## 8. 可视化起点（Browser 画布）— 探索用, 不进 golden 门

两条纯用来在 Browser 里看图的查询, **不锚定 golden、不进 Gate 2**:

```cypher
// advisory 邻域: AE 域的 curated 域间关系 (低保真, 仅供探索参考)
MATCH p=(d:Domain {code:'AE'})-[:RELATED_TO]->() RETURN p
```

```cypher
// Trial Design class 下的域, 看类罗盘的可视化形态
MATCH p=(d:Domain)-[:IN_CLASS]->(:Class {name:'Trial Design'}) RETURN p
```
