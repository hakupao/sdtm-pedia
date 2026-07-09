# SP4 Neo4j 探索层 — 四门验收 checkpoint (2026-07-09)

> Spec `docs/superpowers/specs/2026-07-08-sp4-neo4j-exploration-design.md` (批准 2026-07-08) / Plan `docs/superpowers/plans/2026-07-08-sp4-neo4j-exploration.md`。
> SP1 meta.yaml (唯一源) 之上建 brew+launchd 本机 Neo4j 图探索层 (数据层 + Neo4j Browser + Cypher 查询库)。**生产答题通道 (内存 DictBackend) 零改动、零依赖、零扰动** — `server/` 无任何 neo4j 引用。

## 四门验收表

| 门 | 命令 | 实测结果 | Artifact |
|----|------|----------|----------|
| **Gate 1** 独立对账 (Rule A lane) | `.venv/bin/python scripts/reconcile_neo4j.py` | **41/41 `[OK]`, exit 0**；幂等: 两次全清重建 → 确定性排序 snapshot **5254 行逐字节同 (empty diff)**；N=9 seeded 分层邻域抽检 + 2 个确定性锚点 (Domain AE:RELATED_TO / Codelist C66742:users) | `evidence/checkpoints/sp4_reconcile_gate.txt` |
| **Gate 2** cookbook golden | `.venv/bin/python eval/prod_wirein/sp4_cookbook_golden.py` | **15/15 PASS (7 drift + 8 golden), exit 0**；锚定生产 `GraphEngine`/`MetaStore` (等价 lane，非 tautology — reviewer 已读源码确认 GraphEngine=DictBackend over meta.yaml 零 neo4j 依赖)；APOC 在裸 brew 装机上缺失 → cookbook 用 plain-Cypher 变体 (`collect(DISTINCT ...)` 而非 APOC 函数) | `evidence/checkpoints/sp4_cookbook_golden.txt` |
| **Gate 3** 生产隔离 | Neo4j STOPPED → `.venv/bin/pytest scripts/tests/` + off/on composite diff + `server/` grep | 全套 **477 passed, exit 0** (Neo4j 停机)；composite answerer 输出 Neo4j-off vs Neo4j-on **byte-identical (6225 bytes, empty diff)**，9/12 battery 双态一致命中；`server/` 零 neo4j 引用 (import-grep + 小写字面量-grep + 运行时 `sys.modules` 三重校验均 clean) | `evidence/checkpoints/sp4_isolation_gate.txt` |
| **Gate 4** Rule D 异 type 审 | `feature-dev:code-reviewer` 全量审 `b2e2f92..6dc123c` (11 commits) | **APPROVE_WITH_NITS**，无 BLOCKER / 无 HIGH；1 MED (localhost 绑定证据缺口) + 2 LOW，**三条均已修补并有独立证据** | `evidence/checkpoints/sp4_ruleD_review.md` + `evidence/checkpoints/sp4_localhost_binding.txt` (两端口均验证 127.0.0.1-only：`lsof` + `SHOW SETTINGS listen_address`) |

## 图形状 (实测, meta.yaml 唯一源)

| 节点标签 | 数量 | | 边类型 | 数量 |
|---------|------|---|--------|------|
| Domain | 63 | | HAS_VARIABLE | 1917 |
| Variable | 1541 (= 1523 IG + 18 model-only) | | USES_CT | 542 |
| Codelist | 1005 | | IN_CLASS | 63 |
| Class | 8 | | DEFHOME | 59 |
| ModelChapter | 4 | | RELATED_TO | 52 |

节点合计 2621，边合计 2633。

## 4 数据接地偏差 (D1-D4, 计划期程序实测 `data/meta/meta.yaml` 抓出, Rule D 审查项)

| # | Spec 原文 | 实测 | 处理 |
|---|----------|------|------|
| D1 | C66742 影响分析 "必回 123 变量/**44 域**" | **123 变量 / 41 域** (变量数吻合, 域数是 spec 笔误) | golden 锚 123/41 |
| D2 | USES_CT 边属性 "—" | C119013 (FOCID) 是唯一 closure≠location 的 codelist (变量级闭包 3 域, 逐域精确 1 域); 无边属性则 impact 查询无法与生产 GraphEngine 逐数吻合 | USES_CT 边加 `domains: [list]` 属性 (该变量实际使用该 CT 的域), cookbook impact 查询 `UNWIND u.domains` |
| D3 | DEFHOME "Variable→**Domain**" | `model_defhome` 映射变量 → **model 章节文件** (如 `model/03_special_purpose_domains.md`), 非域 | 新增第 5 节点标签 **ModelChapter** (4 节点, `path` 属性); DEFHOME = Variable→ModelChapter |
| D4 | Variable 节点 1523 | model_defhome 59 变量中 **18 个不在任何 IG 域** (APID/SETCD/SPECIES/STRAIN 等模型级变量); 若只建 1523 节点, DEFHOME 只能建 41 条, 静默丢 18 条数据 | 18 个模型级变量也建 Variable 节点, 标 `model_only: true`; Variable 总数 **1541 = 1523 + 18**; DEFHOME 全量 59 条; 计数类 cookbook 查询默认 `WHERE NOT v.model_only` |

D2 的 FOCID/C119013 难例由 **3 条独立代码路** (extract_graph / reconcile 独立重导 yaml / 生产 GraphEngine) 三角验证一致 (`sp4_reconcile_gate.txt` 与 `sp4_cookbook_golden.txt` 均 1/1)，是本单元反过拟合证据最强的一点。D4 的 `model_only` 拆分经证**不污染**计数类 cookbook 查询 — 18 个 model-only 节点结构上不可能收到 `HAS_VARIABLE`/`USES_CT` 边 (由构造免疫，非靠可被遗忘的 `WHERE` 过滤器)。

## 产物清单

- **代码**: `scripts/build_neo4j.py` (纯函数 `extract_graph`: meta.yaml → 5 标签/5 边行, golden-anchored TDD; 导入层 `import_graph`: driver 批量写 + 写计数器自校验 `created==input` fail-loud + 5 唯一性约束) + `scripts/reconcile_neo4j.py` (独立码路对账, **禁止 import** `build_neo4j`/`MetaStore`/`GraphEngine`) + `scripts/tests/test_build_neo4j.py`。
- **运维**: `deploy/com.sdtmrag.neo4j.plist.template` (launchd, localhost-only 7474/7687) + `deploy/README.md` §Neo4j (brew 安装/heap 配置/验证 runbook)。
- **查询库**: `docs/cypher_cookbook.md` (7 条锚定 Cypher 查询 + Neo4j Browser 可视化起手式)。
- **评测工具**: `eval/prod_wirein/sp4_cookbook_golden.py` (Gate 2 harness) + `eval/prod_wirein/sp4_isolation_probe.py` (Gate 3 12-query battery)。
- **依赖**: `pyproject.toml` `[project.optional-dependencies].dev` 追加 `neo4j>=6.2.0` (非 `[project.dependencies]`)。
- **配置**: `.env.example` 追加 `NEO4J_URI` / `NEO4J_USER` / `NEO4J_PASSWORD` (空值行, 实值只进 gitignored `.env`)。
- **证据**: 本文件 + `sp4_{reconcile_gate,cookbook_golden,isolation_gate,ruleD_review,localhost_binding}.{txt,md}`。

## 限制 / 诚实缺口

- **Term 节点未物化** — spec §3 明确列为 backlog；本单元只建 5 节点标签 (Domain/Variable/Codelist/Class/ModelChapter)，术语值 (controlled terminology 的具体 term) 不进图，仍停留在 meta.yaml 的 `codelists[].term_count`。
- **webchat Graph tab 是二期** — SP4 brainstorm 决策 ③ 明确交付面止于「数据层 + Neo4j Browser + Cypher 查询库」，聊天前端内嵌图可视化 (webchat Graph tab) 未做，属未来产品决策。
- **对账两侧同源 meta.yaml** — Gate 1 (`reconcile_neo4j.py` 独立重导 yaml) 与 Gate 2 (cookbook golden 锚定生产 `GraphEngine`) 虽是两条独立代码路径 (互不 import)，但两者的**数据源头都是同一份 `data/meta/meta.yaml`**。这两门能抓的是「代码路径 bug」(extract_graph 抽取错、导入层丢行、Cypher 查询写错)，**抓不出** meta.yaml 本身相对 PDF/xlsx 源文件的错误 — 那是 SP1 `scripts/reconcile_meta.py` (对 raw CDISC 源文件的独立锚对账) 已经把关的职责，本单元不重复也不覆盖。
- **heap 配置实际落点是 `neo4j.conf`，不是环境变量** — Task 1 (2026-07-08) 实测: docker-entrypoint.sh 风格的 `NEO4J_server_memory_heap_max__size` 环境变量对 brew 原生安装的 Neo4j **无效**；heap 上限改为在 `deploy/README.md` runbook 里直接 `echo 'server.memory.heap.max_size=1g' >> neo4j.conf`，用 `SHOW SETTINGS` 验证生效 (`sp4_localhost_binding.txt` 复核: `server.memory.heap.max_size = "1.00GiB"`)。plist 模板本身不设置 heap，靠 conf 文件持久化。
- **Neo4j 是机器本地服务，不在 go-live 范围内** — 与 `deploy/.env.service.template` (RAG API 共享部署) 完全隔离，本单元明确"不碰" `.env.service.template`；Neo4j 探索层只服务本机开发/探索用途，没有对外共享计划。

## Browser 入口

`http://127.0.0.1:7474` (登录 `neo4j` / `$NEO4J_PASSWORD`)。查询库见 `docs/cypher_cookbook.md`。
