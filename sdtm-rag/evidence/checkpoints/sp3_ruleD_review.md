# SP3 — Rule D 独立审 (写审隔离, 异 subagent_type)

> 2026-06-20 · SP3 (关系/影响图查询) 三轮独立审 (per-phase + 最终全量), 全部 `oh-my-claudecode:code-reviewer` (opus), writer = `executor` (异 type, fresh context)。

## 总览
| 轮 | 范围 | 初判 | 修后 |
|----|------|------|------|
| Phase 1 | 图引擎数据层 (graph_engine + MetaStore 访问器) | APPROVE (2 LOW + 2 NIT) | LOW/NIT 修复 (domains_in_class 大小写 + 类计数 7→8 + backend-edge 守卫) |
| Phase 2 | NL 图答题 (graph_answer + grounding + structured_answer) | **REQUEST_CHANGES** (1 HIGH + 2 MED + 1 LOW + 2 NIT) | 全修 → **APPROVE** (复审) |
| 最终全量 | 整个 SP3 surface + Phase 3 接线 (ship-default-on gate) | **APPROVE** (0 BLOCKER/HIGH; 2 MED + 2 LOW + 1 NIT) | 2 MED 修复, LOW/NIT 处置见下 |

## Phase 1 (图引擎) — APPROVE
reviewer 自建 from-scratch `RawBackend` (只实现 3 原语, 不用 MetaStore 索引), 证 GraphEngine 输出对每个公共方法 **byte-identical** → seam 真承载全部拓扑。findings 全修:
- LOW: `domains_in_class` 大小写敏感 (违 §4 契约) → casefold canonicalize。
- LOW: spec/plan 写 "7 classes" 实为 8 (含 "Findings About") → 改 spec+plan (代码本就对)。
- NIT: 3 个 backend edge (HAS_VARIABLE/BELONGS_TO/DEFHOME) 未被 engine 用 → 加 backend 原语守卫测试。

## Phase 2 (NL 答题) — REQUEST_CHANGES → APPROVE
**HIGH (真缺陷, 我 4 样本 smoke 漏掉、reviewer 全量 140q 扫到)**: 140q 零污染门失败 5/140 (q10/q33/q39/q60/q118)。根因 = class-aggregate 意图的 `" class "` 裸子串 + relationship 的 `linked`/`relationship` 在散文里误触发。
**MED-1**: `class_domains` 接地闸 reintroduce SP2 36→0 假阳类 (class 名是常用词, subject-collision; reviewer 复现 wrong "correct to N")。
- 修法 (用户决策, 非 whack-a-mole): **从 NL 面去掉 class-roster 意图** (class 名常用词→NL 检测固有脆弱); `domains_in_class`/`class_sizes` 保留在 GraphEngine (engine-only, SP4/API)。revert grounding 的 class_domains 加项 (只留 rare-subject `impacted_*`)。
- **复审 APPROVE**: 140q 零污染 = 0/140 (reviewer 独立重跑); class_domains 假阳结构性消除; SP2 base kinds byte-identical; 称「drop-class-roster 比我要求的 tighten 更 structurally clean」。
- 复审残留 LOW (variables_in_min_domains 在 "more than N + 非域名词" 误触发) → 加 domain-context 守卫 (后续在最终轮 MED 一并处理)。

## 最终全量 (ship-default-on gate) — APPROVE (0 BLOCKER/HIGH)
reviewer **独立重跑强证据**:
- **composite-path 140q 零污染** (经真 `maybe_build_answerer(Settings(graph_answer_enabled=True))`, 非裸 GraphAnswerer): ON facts 对全 140 题与 OFF **byte-identical**, 0 graph 注入 → 翻 flag 对现评测集 behavior-preserving, SP2 q103/q104 等 provably 不受扰。
- **端到端 merged-facts 接地闸**: 错 impact 基数→更正; 对的→不动; SP2+SP3 co-fire 产 4 个不重复 CheckableCount; 跨通道无矛盾; merge 去重不丢真事实。
- router/ask_stream/run_eval 三调用点 SP3-agnostic (经 shared helper); 反过拟合扫描零硬编实体。

findings 处置:
- **MED-1 (degenerate "affects 0 domains" for 858 unreferenced codelists)**: reviewer 明确 = **SP2 已上线通道的同样 pre-existing 行为**, SP3 mirror 非新缺陷, 非阻塞。仍**修了 SP3 侧** (GraphAnswerer impact 分支: n==0 跳过, 不注入/不计数)。SP2 同源行为记为独立 SP2 后续项 (本次不动 SP2 resolve, 避免范围蔓延)。
- **MED-2 ("more than N" 映射 >=N off-by-one, display-only 非 checkable)**: 修 ("more than"→n+1 strict; "at least"→n inclusive)。
- **LOW-1 ("无 SP3 spec/plan")**: **误报** — reviewer 找的是 `sdtm-rag/docs/`; spec/plan 在**项目根** `docs/superpowers/{specs,plans}/2026-06-20-sp3-graph-queries*.md` (与 SP1/SP2 同位)。无需动作。
- **LOW-2 (mechanism:null 未 back-fill, 50 边)**: 故意 defer (advisory 非权威, NL 优雅省略 "via" 子句)。记为 SP3+ 可选项 (见 roadmap)。
- **NIT (most_shared 固定 top-5 / merge_facts 块间空行)**: 合理默认 / 纯 cosmetic 不显现, 不动 (YAGNI)。

## 最终状态
2 MED 修复 (commit `72bdec6`); flag 默认 ON (commit `212b249`)。完整套 **414 passed**, mypy + ruff (SP3 文件) clean, 140q 零污染 0/140 (composite path)。**三门之 Rule D 门: PASS**。
