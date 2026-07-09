# RETROSPECTIVE — SP5 图增强校验器 (KG 重启 5/5, 收官)

> 2026-07-09 · 规则 C 强制复盘。SP5 = 给现有 Validator (Phase 1C, 7 规则) 接进 DESIGN §5.6
> 三类图增强跨域校验 (impact advisory / RELREC 跨域完整性 / CT 级联一致性), 对多域 study
> 上传做确定性跨域校验, 拿内存 GraphEngine (over meta.yaml) 当权威参照。全 advisory, 不碰 Neo4j。

## 1. 保留下来的做法 (下个项目继续用)

- **写码前先把 plan 的数据假设逐条实测对齐真值 (verification-first)**。SP5 plan 把测试/fixture 的
  具体实体 (AE→CM RELREC / AESER+MHSER 同绑 C66742 / USUBJID 高 impact) 写死在代码里。开工第一步
  用 `MetaStore`/`GraphEngine` 逐条打表, 抓出 **MHSER 实际不绑任何 codelist** (plan 假设错) +
  **AE 的 RELREC target 是 {CM, PR} 两个不是一个** + **pass study {AE,CM,MH} 非 RELREC-闭合** 三处
  硬伤。若照抄 plan 直接跑, Task 2/3/4 会红或 golden 误报。**教训固化: plan 里凡"探索实测"标注的
  数字, 实现者开工必须重测一遍, 不许信任 plan 的抄写。**
- **TDD 红-绿逐 task, 每 task 一 commit**。9 单测 + 2 e2e + 3 report + 2 endpoint 全部先写失败测试
  再实现, 每步 `pytest` 钉死, 全程 493 passed 零回归。
- **规则 A/D 双独立 lane 收口**: Rule D (code-reviewer subagent) + Rule A (general-purpose scientist,
  raw-yaml 独立重算不 import 被审模块) 异 subagent_type 并行, 与 writer (主 context) 隔离。
- **规则 B 失败/偏差归档不删**: `evidence/failures/sp5_attempt_1.md` 完整记录 plan 数据假设 vs 真值
  的 5 处对齐 (A-E) + Task 3 fixture 列长笔误, 附实测证据。**"实现逻辑一字未改去凑测试, 只改测试/
  fixture 数据对齐真值"** 的纪律写进归档, 供 Rule D 复核。

- **真实数据验证抓出合成 fixture + 单测都漏的假阳 (缺口修正 follow-up)**: 用户要求把披露的缺口全修。
  拉 **CDISCPILOT01** 真实 9 域全量 (LB 59580 行) 跑三类检查, 立刻抓出 cascade 对 **C71620 (Unit, extensible
  830 词)** 的真实假阳 (CM/EX/LB 单位词表合法不相交) — 这是合成 fixture 和非嵌套单测都想不到的形状。修为
  **跳过 extensible codelist** (开放式 codelist 跨域发散是设计使然)。**教训: 合成 fixture 证逻辑, 真实数据证
  校准; 校验器类工具必须过一遍真实脏数据才敢说"误报率低"。** cascade 还暴露"多变量共享 codelist"的固有弱点
  (C66742 被 AESER/DTHFL/LB flags 等语义无关变量共用, 值集本无理由跨域一致) → cascade 是三类里最弱, 诚实披露留 dogfood。
- **缺口修正的反过拟合守则**: completeness 拓宽时发现 KB 只有 2 条 RELREC 边、无更多可提取, **拒绝臆造一份
  "常见 RELREC 域对"清单** (用户对 example/编造敏感), 改用 KB-grounded 的两条: RELREC 对称 (WARN) + 45 条已策划
  关系降为 INFO (severity 匹配低保真)。宁可覆盖面诚实地窄, 不编数据凑广度。
- **lifespan/boot 路径必须有冒烟测试 (Rule D gap-fix 复审 B1 教训)**: GraphEngine 缓存加在 `main.py` lifespan,
  一处 `store.n_domains()` 把 `@property` 当方法调 → 生产 `uvicorn` 启动即 TypeError 崩。**503 全绿却漏网**, 因所有
  端点测试都 bare-app + 手工 `app.state`、**零测试进 create_app 全 lifespan**。补 `test_create_app_boots_through_lifespan`
  实跑 boot。**教训: 只测 handler 不测 boot = 生产起不来也全绿; 服务类项目必须有一条走真 lifespan 的冒烟。**

## 2. 必须补上的缺口 (诚实披露 + backlog)

- **CT cascade 是"跨域值集合不一致"的启发式, 有合法误报面**: 两个域对同一 codelist 合法地使用不同
  子集 (如一个域只出现 Y, 另一个出现 Y/N/U) 会触发 WARN。这是设计选择 (advisory, 非 ERROR, 不 hard-fail),
  但用户需理解"WARN≠错误"。已在 docstring + summary 文档化。
- **无真实 study 数据, 用合成 fixture**: repo 无真实多域 SDTM 数据集, pass/fail 版是手造的 {AE,CM,PR}/
  {AE,MH}。真实数据上的误报率未测 — 等 dogfood 信号 (与 AGG 长尾同款处理)。
- **spec §3.2 的 back-fill 经数据核验后撤销 (M1, Rule A+D 双抓)**: 原设计 `mechanism:null +
  target∈{RELREC,RELSPEC,RELSUB}→mech=target`。实测 meta.yaml: 这类 null-mech 边的 target 是**关系数据集本身**
  (LB/BS/IS/MB/MS → RELSPEC "specimen hierarchy"), target==机制名而非伙伴域, back-fill 在 `mech=='RELREC'`
  守卫下是死码, 且若放宽守卫会产 "X RELSPEC-linked to RELSPEC, absent" 的无意义 WARN。收窄 completeness 为
  **仅显式 mechanism=='RELREC'** (真实数据行为逐字不变: 全域仅 AE→CM/PR 两条 RELREC 边)。**教训: 连"确定性 back-fill
  非臆造"这种看似安全的推断, 也必须用真实数据打表验证其语义, 否则会引入死码或误报。**
- **校验未暴露进 go-live webchat**: 仅 Streamlit + API 端点, 对外分享面 (webchat) 不含 study 校验
  (spec §5 范围外; 与 SP4 Graph tab 同属二期 UX)。
- **report.py / router.py 存量 lint/type 债 (非 SP5 引入)**: 两文件在 SP5 前 (HEAD 2d5b5b9) 已有
  committed ruff/mypy 违规 (report.py 4 ruff + 5 mypy 于 generate_markdown; router.py 11 ruff = 2 B008
  + 7 B904 + 2 I001)。SP5 新增码本身干净, 唯一新增是 1 条 B008 (`files: list[UploadFile]=File(...)`
  FastAPI 惯用法, 文件里已有 2 处同款)。**未顺手修存量债 (超 SP5 scope, 且改 import 有 re-export 风险);
  诚实披露交 Rule D 判定, 不谎称 "ruff clean"。**

## 3. 关键决策复盘

- **advisory-only 基调 (WARN/INFO, 绝不 ERROR)**: 三类检查都基于 curated-prose 低保真关系或"跨域一致性"
  启发式, 任何一条升级为 ERROR 都会在真实数据上误伤合法情形。选择全 advisory = 零误报代价 (静默或提示,
  从不 pass/fail 一个 study 因为图层)。这也呼应 KG 价值 eval 的元教训: **图不是精度来源, determinism 才是** —
  图层在这里的价值是"提示高 impact / 缺关联域 / 跨域值漂移"这类新视角, 不是判对错。
- **确定性内存引擎, 不碰 Neo4j**: SP4 的 Neo4j 是探索层 (人工 Cypher/Browser), 与自动校验无关。SP5 复用
  SP2/SP3 的 `MetaStore`/`GraphEngine` (over meta.yaml 单一真值源), 零新依赖、零 I/O、可确定性单测。
  Neo4j 停机不影响 SP5。
- **study-level 聚合 vs 单域 report**: 新增 `generate_study_json` + `POST /api/validate-study` 多文件入口,
  单域 `/validate` 逐字节不动 (零回归硬约束)。study verdict = 各域 worst-of + 图层 severity 合并; 图层只加
  WARN/INFO, 永不把 study 顶成 FAIL (advisory 一致性)。
- **plan 数据假设错位时的处置**: 不"按 example 对症下药"改实现, 而是 (1) 实测真值 (2) 改测试/fixture 数据
  对齐真值 (3) 归档偏差 + 证据 (4) 留 Rule A 用独立码路复核。区分 "pattern 级正确" vs "凑测试" 是本项目
  一贯的反过拟合红线。

## 4. 验收门结果

> 见 `evidence/checkpoints/sp5_summary.md` (三类检查验收表) + `sp5_ruleD_review.md` (Rule D) +
> `sp5_ruleA_audit.md` (Rule A)。
> - **程序门**: **493 passed 零回归** (单域 validate 函数体逐字节不变) + golden pass/fail 精确命中 + 新码 ruff/mypy 干净。
> - **Rule D** (异 type code-reviewer, opus): **APPROVE_WITH_NITS, 0 BLOCKER / 0 HIGH** (advisory-only 构造级成立 + 诚实性偏保守核实); 1 MED (M1 back-fill 死码) 已修。
> - **Rule A** (异 type scientist, opus): **PASS, 8/8 样本零 mismatch** (raw-yaml 独立重算 vs run_graph_checks 逐字全串匹配)。
>
> **订正 (Rule D LOW)**: plan 反复引用的零回归依据 `test_validator.py`(37 测试) 实际不存在; 真实依据 = 493 全绿 + 端点纯追加字节未变。
