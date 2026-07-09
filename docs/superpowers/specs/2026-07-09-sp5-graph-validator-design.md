# SP5 — 图增强校验器 设计 (spec)

> 2026-07-09 · KG 重启子项目 5/5 (最后一个)。扩展现有 Validator (Phase 1C, `server/validator.py`
> 7 规则 94.7% 检出), 加 DESIGN §5.6 三类图增强校验。对象 = 用户上传的**多域 SDTM study 数据集**,
> 拿知识图谱 (内存 `GraphEngine` over `meta.yaml`) 当权威参照。**确定性, 不碰 Neo4j** (SP4 的 Neo4j
> 是探索层, 与此无关; 价值 eval 元教训: graph 非价值来源, determinism 才是)。brainstorm 决策已锁, 用户批准 2026-07-09。

## 1. 已锁决策 (brainstorm)

| # | 决策 | 选定 |
|---|------|------|
| Q1 | 范围 | **完整 3 类** (impact / cross-domain completeness / CT cascade) |
| Q2 | impact 语义 | **advisory 注解** (INFO/WARN, 标注高 impact 变量/codelist, 零误报, 不 pass/fail) |
| Q3 | 跨域输入 | **新增 study-level 入口** (一次传多域文件, 真跨域比对); 单域 `/api/validate` 不动 |
| Q4 | 引擎 | 复用内存 `GraphEngine`/`MetaStore`, **不引 Neo4j** |
| Q5 | 验收数据 | 造**合成 study fixture** (repo 无真实数据集) |
| Q6 | mechanism back-fill | SP5 内部**临时推断**, 不改 `meta.yaml`/SP1 |

**硬约束**: 全 advisory 基调 (WARN/INFO, 不 ERROR — 避免误报 + curated 关系 LOW fidelity 不可 hard-fail);
单域 validate 路径零回归; 复用 `meta.yaml` 单一真值源。

## 2. 架构

```
上传多域文件 → POST /api/validate-study → 逐域 validate() (现有7规则) +
  graph_validator.py 三类跨域 check (over GraphEngine) → report.py 聚合 study-level 报告
Streamlit: 多文件 uploader (现有单域上传不动)
```

- **`server/graph_validator.py`** (新): 3 个纯函数, 输入 = {domain: DataFrame} 域集合 + GraphEngine, 输出 = list[Finding]。
- **`server/router.py`**: 新增 `POST /api/validate-study` (多 UploadFile, 各自 parse_bytes+detect domain, 逐域跑 validate, 再跑 3 类跨域 check)。
- **`ui/streamlit_app.py`**: 多文件上传 + study 报告展示。
- **`server/report.py`**: 加 study-level 聚合 (复用 generate_markdown/json)。
- Finding 复用现有 `validator.Finding` dataclass (severity/message/...); 新 category 值 `graph_impact`/`graph_completeness`/`graph_cascade`。

## 3. 三类检查 (算法)

**输入**: 提交域集合 `S = {dom: df}`。全部只读 GraphEngine (确定性), 不改数据。

1. **impact (advisory, 逐域 INFO/WARN)**: 对每个域 d 的每个变量 v, 查 `impact_of_variable(v)` 与
   `impact_of_codelist(c)` (c ∈ v 的 ct_codes)。若 `n_domains ≥ IMPACT_DOMAIN_THRESHOLD (=10)` →
   Finding "v/c 高 impact: 改动波及 N 域 M 变量" (severity INFO; WARN 若同时 v 是 REQ/Topic)。纯提示。

2. **cross-domain completeness (WARN)**: 对每个 d∈S, 取其 RELREC-linked target 集 =
   `relations_curated(d)` 中 `mechanism=='RELREC'` 的 target ∪ **back-fill**: `target ∈ {RELREC,RELSPEC,RELSUB}`
   时机制即该 target (临时推断)。若某 target ∉ S.keys() → Finding "d 经 RELREC 关联 t, 但 t 未在本次提交" (WARN)。

3. **CT cascade (WARN)**: 找 S 中被 ≥2 域使用的共享 codelist Y (via `domains_for_codelist(Y) ∩ S`)。
   对每个这样的 Y, 收集各域数据里绑定 Y 的变量列的 **distinct 实际值集合**。若各域的值集合不一致
   (对称差非空) → Finding "codelist Y 跨域值不一致: 域A={..} 域B={..}" (WARN, 列各域 distinct 值)。
   注: 单域"值不在 codelist 允许集"已由现有 c.CT 规则 ERROR 覆盖; 本类是**跨域一致性**, 独立增量。

## 4. 验收门 (规则 A/B/C/D)

- **合成 fixture** (`scripts/tests/fixtures/sp5_study/`): study = 域 AE/FA/LB/DM。含已知 RELREC (AE→FA per
  meta.yaml curated) + 共享 codelist C66742 (NY)。**pass 版** (全齐、CT 一致) + **fail 版** (缺 FA → completeness
  WARN; LB 的 C66742 值域与 AE 冲突 → cascade WARN)。
- **门**: (1) golden 单测钉死 3 类 check 输出 (pass 版 0 graph-WARN, fail 版精确命中); (2) 现有 validator
  单域路径零回归 (全套 pytest 绿); (3) Rule D 异 subagent_type 审; (4) Rule A N=6 独立核 (对照 meta.yaml
  手算 impact/completeness/cascade 期望, 不复用 graph_validator 代码)。
- 失败归档 `evidence/failures/sp5_attempt_*.md` (规则 B); 收口 `RETROSPECTIVE_sp5.md` (规则 C) +
  `evidence/checkpoints/sp5_summary.md`。
- 体量 **Tier 2** (~8 task)。

## 5. 范围外 (defer)

真实 study 数据 (用合成); 把校验暴露进 go-live webchat (仍只 Streamlit/API); domain-specific 属性校验
(API 无 per-(domain,var) attr); mechanism back-fill 写回 meta.yaml (SP1); Neo4j。

## 6. 交付物

`server/graph_validator.py` + 测试 + fixtures; `router.py`/`report.py`/`streamlit_app.py` 改; 文档链
(KG_ROADMAP SP5 段 + worklog + PROGRESS + `_progress.json` + RETROSPECTIVE_sp5)。**SP5 完成 = KG 重启全线收官。**
