# KG 重启 — 子项目路线图 + 设计状态 (handoff)

> 2026-06-16 · **brainstorming 进行中** (SP1-5 decomposition 已经用户 ack; SP1 详细设计**未完成**)。
> 用户决策: **SP1-5 全做**, 按依赖顺序逐个 (每个子项目走 设计→spec→plan→实现 循环)。
> 恢复方式: 新 session 说 **「KG 重启 开始任务」** → 读本文件 + memory `project_kg_decision` → **继续 brainstorming SP1 (meta.yaml)**。
> ⚠️ **HARD-GATE (brainstorming 规则)**: 先把 SP1 设计问完 + 出 spec + 用户批准, 再 `writing-plans`/写码。**别跳过设计直接实现**。

## 已 settled (别再 re-litigate)

- KG **≠ 提检索精度** (检索已 99%)。真价值 = **新能力**: 计数/穷举 (q103「43 域」/q104「36 变量」今天答错)、影响/级联分析、替换 `server/structured_lookup.py` 里脆弱的正则「影子 KG」。
- 路径: deploy (DONE) → **meta.yaml (63 域)** → 可选 Neo4j。meta.yaml 便宜 + 立刻修计数/穷举 + 是 Neo4j 硬前置。
- **重定位 (本次 brainstorm 用户 ack)**: 能力 (计数/穷举/影响/关系) 在 SP1-SP3 用 **meta.yaml + 内存图遍历** 就能交付; **Neo4j 降级为「要不要可视化 / 临时 Cypher 探索界面」的产品选择, 不是能力前置**。省 16GB 机器多跑一个图库。
- 原始完整图 schema (节点/关系/示例 Cypher) 详 `docs/DESIGN_RAG_KG.md` §5 — 可复用做 meta.yaml/内存图的形状参考。

## 子项目 (依赖顺序; 用户要全做)

- **SP1 — `meta.yaml` 元数据层** (基础, **先做**): 脚本从现有 KB (spec.md + Cross References + terminology) 自动生成 63 域结构化 YAML (域 / 变量[name·role·type·core·ct_code] / codelist / 跨域关系)。**独立可验** —— 里面每个计数/关系都能对着 KB 核对 (Rule A)。是后面一切的硬前置。
- **SP2 — 确定性结构化答题通道**: meta.yaml 载内存 → `/api/ask` 对计数/穷举/精确查找走确定数据 (q103/q104/q126 答对) + 退役正则影子 KG。
- **SP3 — 关系/影响查询**: meta.yaml 之上**内存图遍历** (networkx / 纯 Python): "改 C66742 影响哪些域/变量"、"哪些变量跨 >N 域"、关系发现; 接入 chat/API。
- **SP4 (可选) — Neo4j + Cypher + 混合路由**: 仅当要可视化图浏览器 / 临时 Cypher 探索界面作产品界面才上 (DESIGN §5.4/§5.5)。
- **SP5 (可选) — 图增强校验**: 影响/级联检查接进 Validator (impact analysis / cross-domain completeness / CT cascade, DESIGN §5.6)。

## 下一步 (新 session 恢复 brainstorming SP1) — 待问的 SP1 设计问题

1. **SP1 粒度**: 只生成+验证 meta.yaml, 还是连一条最小确定性答题一起 (SP1+SP2 合并出一个可见的 win)?
2. **数据源覆盖**: spec.md + Cross References + VARIABLE_INDEX.md 是否覆盖全部需要的关系? 有没有 KB 没显式记、需要补的关系 (如 SUPP--/RELREC mechanism)?
3. **schema**: 沿用 DESIGN_RAG_KG §5.1 的 meta.yaml 形状, 还是调整 (class/structure/关系 mechanism 粒度)?
4. **正确性验收**: 63 域怎么自动核对 —— 计数对账 (变量数/域数/codelist 数 对 KB) + N 样本 Rule A 抽检 (N 写进 PLAN)?
5. **落点**: 生成脚本 (`scripts/build_meta.py`?) + 输出位置 (knowledge_base/ 只读 → 落 `sdtm-rag/data/meta/` 或 `branches/07_rag_kg/.../meta/`?)。

SP1 设计定稿后: 写 spec → 用户审 → `writing-plans` → 实现 (TDD + Rule A/D)。然后 SP2、SP3… 逐个同样流程。
