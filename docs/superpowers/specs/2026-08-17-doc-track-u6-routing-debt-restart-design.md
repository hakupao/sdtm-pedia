# doc 轨 U6 设计 — 判库欠账重启修法 (仪器先行 + 确定性信号层)

> 建立: 2026-08-17 · 用户点单 kickoff §0′ #1 · 四项裁定 (机制/条款4/E1/结构) 已于设计对话中做出
> 前置依据: U3 收口 §9 (6 条硬约束) + U5 收口 §9 (7 条硬约束) — 本 spec 逐条落实
> 数据红线: 零真名零正文, 研究代号 `st01`; 路由 gold 题面 gitignored 双红线不变

## 0. 一句话

先把 U3/U5 点名的判据仪器缺陷修掉并重冻基线 (Phase 0), 再用**确定性检索信号层**
(不动 `_ROUTER_SYSTEM` 一字) 修判库欠账 (Phase 1), 全程七条款闸住。

## 1. 现状与动机 (全部为已收口数字)

- **判库欠账 10pt 仍在** (U2 量出, U3 修法退回原样): `docs_v1_q15/q17/q53` 在 auto 下
  gold 零命中; U5 又观测到 `st01_v2_q07` 同形态 (合计 4 题路由打空, fallback 结构上
  捕获不到 —— `route_corpus` 只在异常时 fallback)。
- **U3 基线 fatal 10 分解**: both→study 6 / cdisc→study 3 / study→cdisc 1
  ⇒ **9/10 缺的是 cdisc 侧, 1/10 缺 study 侧** —— 修法必须双向。
- **措辞杠杆已到底** (U3 §9-3): 最强兜底指令三遍零方差不执行, 五轮净动 3 题。
  本单元不走措辞层 (用户裁定 2026-08-17: 确定性检索信号层)。
- **U5 前置已补掉**: auto 实判 both 的 5 题免费 (可比池内); 「放宽 router」未获干净支持;
  修法线必要性未被解除。E2=cheap 引用必须连可比池 (41/48·29/30) 与最坏界 (2.08pt) 并列。

## 2. 单元边界

**改**: `server/federation.py` (信号层, 只加宽) · `eval/u3_task8_verdict.py` (仪器修缮+条款修订)
· `eval/u5_verdict.py` (判定设计修, 按裁定) · `eval/run_routing_eval.py` (run 级元数据, A-3)
· 路由 gold 两处 (`st01_v2_q07` 入 final 组 + `u3_amb_01/04/06` 复核结果, 均在基线冻结**前**)。

**不改**: `_ROUTER_SYSTEM` 一字不动 · `score_run` fatal 定义 · `LEGACY_EXACT_FLOOR=178`
· 条款 1/2/3/5/6 阈值 · 语料与索引 (三库 4329/959/114) · U1/U2 产物。

**不做**: 放宽 router (仍是新单元) · C2 / L1 卷首 · 席位配置调整 (k=15 / doc_seats=8 不动)
· 答题侧全矩阵重跑 (只做 spot-check, 见 §5)。

## 3. 顺序 (硬的): Phase 0 全部收口并过闸, 才许开 Phase 1

理由与 U3 §3 相同: 判据先于数据写死; 且判据变更 (条款 4/7 + E1) 属换尺子,
不重冻基线的一切对比都不可比。

## 4. Phase 0 — 仪器修缮 + gold 复核 + 新基线冻结

### 4.1 U3 判定仪器修缮 (落实 U3 §9-1 的 4I + 2HIGH)

| 来源 | 缺陷 | 修法 |
|---|---|---|
| 审查 I-1 | `--runs 0/1` 也打「三遍一致」且 rc=0 | runs<3 时拒绝打印一致性结论, 非 3 遍显式 FAIL |
| 审查 I-2 | 判定脚本无输入校验 | baseline/after 文件身份校验 (路径不同 + run 元数据不同 + 内容 hash 不同) |
| 审查 I-4 | `by_group.passed` 用无条款使用的 0.95 | 删除该字段或改为逐条款判定引用, 不留误导读数 |
| 抽检 A-2 | 条款 2/3 单独零判别力 | 多数类基线并排打印已有 — 补整句带数值断言 (硬规矩 18) |
| 抽检 A-3 | run json 无 run 级元数据 | run 产物写入 timestamp/git rev/配置摘要, 判定脚本校验 |
| 抽检 A-1 | 条款 4 exact 口径双向失灵 | → §4.2 条款修订 |

### 4.2 条款修订 (用户裁定 2026-08-17, 先于一切跑批写死)

沿用 U3 §7 全表, 修订/新增如下, **其余条款与阈值一字不动**:

- **条款 4 (修订)**: 新写 cdisc 干扰题组 (12 题) **fatal+exact 双列双闸** ——
  fatal 数较基线**不得增加** AND exact 较基线**下降 ≤ 1 题**。触发时两列数字并列归档
  交用户裁定 (若 exact 闸响而 fatal 列实为改善, 用户拿全信息裁, 不盲拒)。
- **条款 7 (新增, 补审查 I-3 检出真空)**: u1_doc 组 (27 题) 同款**双列闸** ——
  fatal 不得增加 AND exact 下降 ≤ 1 题。修法受力方向 (study→both 漂移) 从此有闸。
- ⚠ **诚实声明 (预登记)**: 本单元机制为只加宽 (widen-only), 加宽**构造上不产生新 fatal**
  ⇒ 条款 4/7 的 fatal 半在本机制下由构造保证, **判别力在 exact 半**; 引用时必须写明
  (同 U2 「由构造保证判别力低」的纪律)。fatal 半留在闸里是为未来非 widen-only 机制服务。
- 条款 1 仍是主闸: 三遍每遍 fatal=0 (口径=全集减 final 组) 且 legacy exact ≥ 178。
  基线 fatal 10 ⇒ 信号层必须**修掉全部 10 个**, 不是不添新。

### 4.3 U5 判定设计修缮 (落实 U5 §9-2, 用户裁定 2026-08-17)

- **E1 (裁定: 稳健支配题移入确认代价)**: 满足 `max(both₃) < min(study₃)` (或反向) 的题,
  即使档内不稳定也计入已确证代价/收益 —— 支配关系本身就是噪声稳健的方向证据。
  最坏界尺子并入 E1 本体, 单一清单单一判词, 消除 C1 型双口径反向的结构来源。
- **E4 并集入闸**: 跨配置不可判并集 ≤ **20%** (per-config ≤15% 不动; 实测并集 14.6%,
  放大界 29.2% —— 20% 在实测之上留 5.4pt 余量且拦住放大)。
- **I-1 结论词抑制**: 任何 I 闸失守路径下, 产物不得写 `cheap_on_this_ruler` 等结论词。
- **divergent_readings**: verdict 同时落盘聚合均值差与配对净额, 符号不一致时脚本自动置
  `divergent_readings: true`。
- 修订后判定脚本**不许沿用旧脚本原样重测** (U5 §9-2 原文); 合成 fixture 测试先行。

### 4.4 gold 复核与变更 (出题侧, 基线冻结前, 此后一字不动)

- `u3_amb_01/04/06` 由**隔离出题侧 subagent** 复核 (审查方点名: 两种独立决策形式都判
  不需要 cdisc 侧)。controller 本 session **不读题面** (对 amb/heldout 保持干净);
  复核结论与理由落盘, gold 改动须用户确认后才生效。
- `st01_v2_q07` 加入路由 gold final 组 (只报告不作判据, 与 q15/q17/q53 同纪律)。

### 4.5 新基线冻结

判据变更 + gold 变更全部落定后, 253(+1) 题三遍重冻 (预期 rc=1, fatal≈10, 视 gold
复核结果浮动; 数字如实归档)。**冻结后阈值/gold/判据一字不许改** (U3 §7 纪律原样)。

## 5. Phase 1 — 确定性检索信号层修法

### 5.1 机制

`FederatedEngine.retrieve` 在 `route_corpus` 返回单库判定后, 加确定性纠偏层:

- **study 侧信号** (升 cdisc→both): `StudyLookup.resolve` 结构命中 (label/段/别名三通道,
  已存在的确定性件) + docs 通道命中强度探针。
- **cdisc 侧信号** (升 study→both): cdisc 侧确定性词面信号 (域码/变量名/CT 码形态) 或
  cdisc 检索命中强度探针, 具体取哪个信号由 dev 可见集标定决定 (plan 里定, 冻结前不上全闸)。
- **只加宽从不收窄**: 信号层只做 单库→both 升级, 永不做 both→单库 或 换库。
  ⇒ 构造上不产生新 fatal (加库永不丢 gold 侧); 代价只在挤占面, 由条款 4/7 exact 半
  + 答题侧 spot-check (§5.3) 看住。
- fallback 语义不变 (异常→both); 新增信号层触发的逐题观测字段 (沿 U5 观测属性写法,
  硬规矩 18: 当场补断言)。

### 5.2 标定纪律 (三道防线沿 U3 §6.2)

- 阈值/词表**只看可见集** (legacy 181 + dev 12) 标定; held-out 12 + amb 6 + final 组全程封存。
- 实现方**全新 session** (U3 §9-4), 只拿到可见集数字。
- 阈值冻结落盘后才跑全闸; 全闸 = 253(+1) 题修订后七条款 × 三遍。

### 5.3 答题侧 spot-check (用 Phase 0 修缮后仪器)

- 范围: 信号层实际改判的题 + 检索侧脆弱 4 题 + `q23r` 在池检查 (U5 §9-6)。
- auto 前后对照 × 3 遍, 修订后 E 规则判读; 可比池限定纪律入收口自检 (U5 §9-1)。
- 不做全矩阵重跑 (U5 §8 边界原样; 全矩阵属「放宽 router」新单元)。

### 5.4 顶层成功指标 (聚合, 不对症)

**auto 相对强制 study 的 docs 侧 source_recall 差**: −10pt → 0 (U5 §9-5 建议的显式指标)。
动机题 `q15/q17/q53/q07` 只报告不作判据 (条款 5 纪律)。

## 6. 人员与规则 D (五方不同 session)

| 角色 | subagent_type | 约束 |
|---|---|---|
| 实现方 | executor (opus) | 每 task 独立 session; Phase 1 只见可见集 |
| 出题侧复核方 | 独立 session | 只做 §4.4, 结论落盘, 边做边落盘 (硬规矩 17) |
| 审查方 | code-reviewer (opus) | 审信号层是否泄漏 held-out 概念 + 判定链 vs 本 spec |
| 抽检方 A | debugger (opus) | 关键数字非自洽复算 (硬规矩 17b) |
| 抽检方 B | test-engineer (opus) | 变异含对调型 + **合取/并集每一半** + purge `__pycache__` + compile 前置 (U5 §9-3) |
| controller | 本 session | 派单 + 复算; 不读 amb/heldout 题面 |

## 7. 判据与自毁 (先于数据写死)

- 全闸任一条款触发 ⇒ 修法退回 (revert) + 失败归档 (规则 B) + 上报, **不许改阈值不许删题**。
- Phase 0 的仪器修缮以合成 fixture 测试 + 变异测试验收; 修缮本身不许顺手改判定语义
  (语义变更仅限 §4.2/§4.3 裁定项)。
- 引用纪律入收口自检闸: 可比池限定 (U5 §9-1) · fallback 全 False 必带「打空未触发」限定
  (U5 §9-5) · +2.78pt 禁作放宽论据 (U5 §9-4) · 条款 2/3 不得单独引用 (U3 §7.1)
  · 强制档数字必须并列 auto 实测触发面 (U5 §9-7)。

## 8. 本单元明确不能证明什么 (预登记)

- **不能**证明答案质量整体变好 —— spot-check 范围外的题未测
- **不能**证明信号层阈值对未来题泛化 —— 标定集 = 可见集, held-out 仍只有 12 题
- **不能**证明席位配置 / N=8 最优 —— 只加宽不调席
- **不能**证明「放宽 router」成立或不成立 —— 仍是新单元
- 条款 4/7 的 fatal 半在 widen-only 机制下不携带信息 (§4.2 诚实声明)

## 9. 开工自检 (在 `sdtm-rag/` 下)

前三条 2026-08-17 已实测全过; 第四条本设计日**未跑** (引 U3 收口 §8 的预期值),
Phase 0 开工时必须实跑并归档:

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2   # → 1353 passed (实测 2026-08-17)
./.venv/bin/python -c "import chromadb; cl=chromadb.PersistentClient(path='data/chroma'); print({c.name: c.count() for c in cl.list_collections()})"  # → 4329/959/114 (实测 2026-08-17)
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid --study-lookup --collection study_st01 --kb-root data/study/st01/cards --output /tmp/chk.json  # → 87.5% (实测 2026-08-17)
./.venv/bin/python -m eval.run_routing_eval --runs 3            # rc=1 预期, 基线 fatal=10 (U3 §8 数字, 本设计日未复跑)
```

---

## 勘误 (2026-08-18, 收口时补记)

- §4.2/§4.5 所写「基线 fatal 10 / 修掉全部 10 个 / 预期 fatal≈10」以设计日 U3 收口数字为据;
  §4.4 的 gold 复核落地后 (`u3_amb_06` both→study, 用户裁定 2026-08-18) 实际冻结基线为
  **254 题 / fatal 9**。差异归因见 `sdtm-rag/evidence/u6_task6_baseline_freeze.md` §3-2。
- §7 预登记的「任一条款触发 ⇒ 修法退回 (revert)」在 Task 10 实际触发时被**用户裁定覆盖**
  (保留信号层, FAIL 诚实收口), 记录见 `sdtm-rag/evidence/failures/u6_task10_attempt_1.md` 处置节。
- §5.1 study 侧信号原文含「docs 通道命中强度探针」— 该探针**本单元未实现** (study 半边仅按
  G1 强通道 `strong_hit` 落地, 见收口 checkpoint §1); 属设计候选未落地, 非静默偏离 (终审 O1 收录)。
