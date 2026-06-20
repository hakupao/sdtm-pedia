# RETROSPECTIVE — SP2 Phase 2 (退役 structured_lookup 正则影子 KG)

> 2026-06-20 · Tasks 15-18。把 `server/structured_lookup.py` 的索引数据源从「init 时正则解析 KB markdown」换成 `data/meta/meta.yaml` (MetaStore), 退役 load-bearing `len==6` 等正则。**严格行为等价** (9891+4177 查询 0 divergence)。Rule D APPROVE。

## 1. 保留下来的做法

- **快照-再重构 (snapshot-then-refactor) 等价 harness = behavior-preserving refactor 的金标准。** 同一脚本跑旧码/新码, dump 全部索引 map + `resolve()` 在**穷举语料** (140 题 + 全量 1523 变量/1005 CT/63 域扫描 = 9891 查询) 上的输出, 逐字节 diff。比「跑一次 retrieval eval」强得多: 确定性穷举 vs 抽样+embedding 非确定。**未来任何等价迁移都应先 snapshot 旧行为再改。**
- **迁移前预分析每个 map 的等价性, 不盲改。** 改之前先 diff「meta 派生 vs 旧码 golden」各 map, 锁定唯一 divergence (FOCID) 并定位根因 (first-seen vs 跨域 union), 据此把代码**一次改对**, 而非改完再查。省一整轮试错。
- **Rule D 写审隔离真有价值 (再次印证)。** reviewer (异 subagent_type, opus) 没信我的产物: 从 git HEAD 重建旧码、同进程对跑、从零重生 golden (逐字节同证非伪造)、**自建 4177 查询对抗语料专门绕开我的语料** → 仍 0 divergence。独立样本核验 = 真闸。
- **最小爆炸半径。** rag.py 懒构造 MetaStore 不改 RAGEngine 签名 → 另 5 个 RAGEngine 调用点零改动; MetaStore 只加方法不动 Phase 1 的 first-seen 路径。改动越小回归面越小。

## 2. 必须补上的缺口

- **meta/KB 漂移自愈能力丢失 (Rule D LOW, 已部分缓解)。** 旧码 init 时实时重解析 KB, KB 改了自动跟上; 新码读 meta.yaml, 若 KB 重建未重生 meta.yaml 会**静默漂移**降级检索。已加 `TestMetaKBDriftGuard` (域级: spec 路径在盘 + 域数对账 + ch04 存在), 但**变量/CT 级漂移仍需手动跑 `scripts/reconcile_meta.py`**。**真缺口 = reconcile 未自动化**: 应在「KB 重建」流程里钉死一步「`build_meta.py` 重生 + `reconcile_meta.py` 对账」, 或把 reconcile 包成 (慢) pytest。本次按 LOW + 现有手动 reconcile 缓解收口, 列入 backlog。
- **死代码会积累。** `ctcode_to_vars` (旧 VARIABLE_INDEX §三 解析) 全仓无 reader 却一直在。本次顺带删。提示: 大改时顺手做死代码审计 (grep reader)。

## 3. 关键决策复盘

- **D1 — 用穷举快照等价证明替代 live retrieval-only paired eval。** structured_lookup 只经 union-add 影响检索, cosine/hybrid 本次未碰; ∴ `resolve()` 逐字节同 ⇒ union-add 同 ⇒ 检索确定性不变 ≥ 现 99% 基线。快照 (9891 查询确定性) 是 retrieval eval 的 superset 且无 embedding 非确定噪声。**接受不跑 live eval** (embedding=OpenAI API, 跑了只增噪不增信)。= "evidence over assumptions": 快照是更强的证据。
- **D2 — `var_to_termfiles` 用跨域 union 而非 first-seen。** FOCID 暴露: MetaStore.`variable_attributes` 是 first-seen (Phase 1 契约, 不能动), 但 FOCID 的 CT (C119013) 只在 OE 域; 旧码 var_to_termfiles 是全域 xref union。新增 `MetaStore.ct_codes_for_variable` (跨域 union, **纯加法**) 精确复现旧码 524=524。教训: 同一实体「first-seen 属性」≠「全域聚合」, 迁移时要对准旧码的聚合语义。
- **D3 — 保留 ch04 glob。** meta.yaml 不覆盖 `chapters/`, generic `--` 变量定义家 ch04 是唯一仍从 KB 文件读的索引, 明确注释为「meta 未涵盖的唯一保留 glob」。没有为了「全 meta 化」而硬塞。
- **D4 — rag.py 懒加载 settings/MetaStore, 不改 RAGEngine 签名。** 权衡: 略微 rag→config 耦合 (懒 import, 仅 lever-on 时) vs 给 RAGEngine 加 meta_store 参数 + 串 6 个调用点 + 可能动 Phase 1 answerer。选 low-churn。reviewer 确认无循环导入、生产路径实跑通过。

## 4. 验收 (三门, 沿用 SP1/Phase1)
- **程序门**: 等价快照 8/8 maps + 9891/9891 resolve() 逐字节同 + 完整套 375 passed (`test_structured_lookup.py` 39 含 3 漂移闸) + held-out 探针 4/4 + ruff/mypy clean + 运行时 smoke + 端到端 union-add 实证。
- **Rule D**: 异 type 独立审 **APPROVE** (0 BLOCKER/HIGH/MEDIUM; reviewer 自建 4177 对抗语料 0 divergence)。
- **Rule A**: Phase 2 无新答题语义 (纯检索侧等价迁移), 检索零回归即证 (沿用 plan §验收三门总览)。

## 5. 产出文件
- 代码: `server/structured_lookup.py` (重写, 净 −185 行) · `server/meta_store.py` (+`ct_codes_for_variable`/`model_defhome_map`) · `server/rag.py` (懒 MetaStore) · `eval/probe_s3_longname.py` · 测试 `scripts/tests/test_{structured_lookup,meta_store}.py`。
- 工具: `eval/prod_wirein/sp2p2_equiv_snapshot.py` (等价 harness, 可复用)。
- 证据: `evidence/checkpoints/sp2_phase2_{paired_eval,ruleD_review}.md`。
