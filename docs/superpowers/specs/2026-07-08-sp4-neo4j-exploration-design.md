# SP4 — Neo4j 探索层 设计 (spec)

> 2026-07-08 · KG 重启子项目 4/5 (用户指示: SP4/SP5 两个都做, SP4 先)。在 SP1 meta.yaml 之上建
> **Neo4j 图数据库探索层**: 交互式图浏览 (Neo4j Browser) + Cypher ad-hoc 查询 + 精选查询库。
> **定位 (价值 eval 2026-06-21 结论)**: 纯产品 UX 功能, 不提答题精度; 生产答题通道继续跑内存
> DictBackend, Neo4j 挂/停/没装对 8000 服务零影响。
> 前置: SP1-3 + AGG 全 DONE。brainstorm 3 决策已锁 (§1), 用户批准设计 2026-07-08。
> SP5 (图增强校验器) 为下一个独立设计单元, 本 spec 不涉及。

---

## 1. 已锁决策 (brainstorm Q1-Q3)

| # | 决策 | 选定 |
|---|------|------|
| Q1 | 底座 | **Neo4j** (完整愿景; 用户明确选择, 否决了纯前端方案)。生产答题不迁移: Neo4j 纯探索层 |
| Q2 | 安装形态 | **brew install neo4j + launchd** (机器无 Docker, 已核实; 与 com.sdtmrag.* 同一运维模式) |
| Q3 | 交付面 | **数据层 + Neo4j Browser + Cypher 查询库** — Browser 自带可视化/控制台, 免前端开发; webchat Graph tab 留二期 |

**硬约束 (贯穿)**:
- **生产隔离**: `server/` 运行时零 neo4j import / 零网络调用; neo4j Python driver 只进 `scripts/` (dev 依赖组)。
- **保真度纪律沿 SP3**: curated 域间关系边必须带 advisory 标注 (低保真, 散文来源); 结构边 (HAS_VARIABLE 等) 为权威。
- localhost-only (127.0.0.1:7474/7687); **go-live 范围不含 Neo4j**。
- 反过拟合惯例: 对账走独立码路, 不复用导入脚本的遍历逻辑。

---

## 2. 架构与组件

```
meta.yaml ──(SP1, 唯一源)──┬── MetaStore/GraphEngine (生产答题, 不动)
                           └── scripts/build_neo4j.py ──> Neo4j (bolt://127.0.0.1:7687)
                                                             │
                                    Neo4j Browser (127.0.0.1:7474) ← 探索/可视化/Cypher
                                    docs/cypher_cookbook.md ← 精选查询库
                                    scripts/reconcile_neo4j.py ← 独立对账门
```

- **`scripts/build_neo4j.py`** (新): meta.yaml → 全量幂等导入。流程: 连接 → 清库 (`MATCH (n) DETACH DELETE`)
  → 建约束/索引 → 批量 CREATE (UNWIND 批次)。幂等 = 重跑结果逐节点/逐边相同。
  依赖官方 `neo4j` driver, 加入 pyproject **dev 依赖组** (uv), 不进 server 运行时依赖。
- **`deploy/com.sdtmrag.neo4j.plist.template`** (新): launchd 托管 `neo4j console` (brew 安装的前台模式),
  绑 127.0.0.1, `NEO4J_server_memory_heap_max__size=1g` (16GB 机器友好), 日志进 neo4j 自身 logs 目录。
  装载步骤写进 runbook (deploy/README.md 追加 §Neo4j)。
- **`docs/cypher_cookbook.md`** (新, sdtm-rag/docs/): 每条查询 = 用途一句话 + Cypher + 期望结果形状。
  必含: ① 影响分析 (codelist→受影响域/变量, 参数化 C 码) ② 变量跨域分布 (含 ≥N 阈值版)
  ③ same-class 邻域 ④ codelist co-users ⑤ **类罗盘** (domains_in_class — SP3 因 class 名常用词
  未暴露 NL 的能力, Cypher 里安全) ⑥ model_defhome 邻接 ⑦ most-shared 排名。
- **`scripts/reconcile_neo4j.py`** (新): 独立对账 (raw yaml.safe_load 自行遍历, 禁止 import
  build_neo4j 的构图函数 / MetaStore / GraphEngine): 全量节点/边分类计数 + 抽样实体邻域逐边比对。

## 3. 图建模 (SP3 同构, Term 不物化)

**节点** (标签 + 属性):

| 标签 | 数 | 属性 |
|------|----|------|
| Domain | 63 真域 (DI 桩**不导**) | code, label, class, structure, n_variables |
| Variable | 1523 (唯一名) | name, label(first-seen), role, type, core |
| Codelist | 1005 | code, name, extensible, term_count, termfile |
| Class | 8 | name, n_domains |

注: Variable 的 role/type/core 可能跨域不同 — 节点存 first-seen 值, **逐域权威值存在 HAS_VARIABLE 边属性上**
(role/type/core per-domain), cookbook 查询默认读边属性。

**边**:

| 边 | 方向 | 保真 | 属性 |
|----|------|------|------|
| HAS_VARIABLE | Domain→Variable | 权威 | role, type, core (该域取值) |
| USES_CT | Variable→Codelist | 权威 | — |
| IN_CLASS | Domain→Class | 权威 | — |
| DEFHOME | Variable→Domain | 权威 | — (model_defhome) |
| RELATED_TO | Domain→Domain | **advisory** | mechanism (可 null), note, `advisory:true` |

**Term 节点不物化** (meta.yaml 只有 term_count/termfile 指针; 物化需新解析源 = 范围膨胀) — backlog。

## 4. 数据流与运维

- meta.yaml 唯一源; KB 冻结 → 重建低频; 一条命令全量重建 (`.venv/bin/python scripts/build_neo4j.py`)。
- **生产隔离验证义务**: Neo4j 停机时 8000 服务/pytest/composite 输出必须与运行时逐字节相同 (§5 门 3)。
- 安全姿态: localhost-only 双端口; Neo4j 原生 auth 初始密码必改 (写 runbook, 密码进 .env 不进 git);
  与现有登录门/共享部署解耦 (探索层自用)。

## 5. 验收门 (四道)

1. **导入对账门**: `reconcile_neo4j.py` — 节点分类计数 (63/1523/1005/8) + 边分类计数 (HAS_VARIABLE=1917
   条目级 / USES_CT / IN_CLASS=63 / DEFHOME / RELATED_TO) 全对 + **N≥8 抽样实体邻域逐边比对**
   (跨 4 节点类型分层抽样, Rule A lane 惯例); 期望值全部从 raw meta.yaml 独立程序导。
2. **cookbook golden**: 每条查询经 driver 执行, 结果锚定 meta.yaml 程序导期望 (如 C66742 影响分析
   必回 123 变量/44 域; most-shared top-5 与 GraphEngine 输出一致)。
3. **生产不受扰**: Neo4j **停机**状态下全套 pytest 全绿 + composite resolve 对代表性查询输出与
   Neo4j **运行**状态 byte-identical + `grep -r neo4j server/` 零命中。
4. **Rule D 异 subagent_type 审** (导入正确性/幂等/对账独立性/安全姿态) + Tier 2 惯例
   (失败归档 `evidence/failures/sp4_attempt_*.md`; 证据 `evidence/checkpoints/sp4_neo4j_summary.md`)。

Rule A 形态说明: 门 1 的独立码路对账即 Rule A 精神的样本核验 (N≥8 写进 PLAN), 不另设第三 lane。

## 6. 交付物与收尾

- 代码/脚本: `scripts/{build_neo4j,reconcile_neo4j}.py` + `deploy/com.sdtmrag.neo4j.plist.template`
  + pyproject dev 依赖 + `deploy/README.md` §Neo4j runbook。
- 文档: `docs/cypher_cookbook.md` (查询库) 。
- 文档链 (Chain 07_RAG): KG_ROADMAP.md SP4 段 + worklog + PROGRESS + `_progress.json` + RETROSPECTIVE_sp4.md (规则 C)。
- 体量: **Tier 2** (~7-10 task)。完成后 **SP5 = 独立设计单元**另起 brainstorm。

## 7. 范围外 (defer)

webchat Graph tab (二期, 用过 Browser 再决定) / `Neo4jBackend` 接 GraphBackend seam / Term 节点物化 /
共享部署 (go-live 线) / LLM→Cypher 自然语言查询 (原 §5.4 路由, SP1-3 已用确定性通道更好地覆盖)。
