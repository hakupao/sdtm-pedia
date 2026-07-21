# Rule D Review — SP4 Neo4j Exploration Layer

> 规则 D 独立审 (异 subagent_type = `feature-dev:code-reviewer`, 与全部 implementer 不同 lane)。
> 审查范围: 全量 diff `b2e2f92..6dc123c` (11 commits, SP4 从 plan commit 到 Gate 3 收尾)。
> 日期: 2026-07-09。

**Verdict:** APPROVE_WITH_NITS (无 BLOCKER / 无 HIGH; 1 MED + 2 LOW)

## Strengths

- `import_graph` (`scripts/build_neo4j.py`) 闭合了 spec 点名的 silent-MATCH-skip 风险: 用 `result.consume().counters.nodes_created` / `relationships_created` (非 `len(rows)`) 对**每个**节点标签和**每个**边类型比对, mismatch 即 `ValueError` — 完整自校验, 非部分。
- 对账独立性真实非表面: `expected_from_yaml` 用结构不同的遍历 (set/dict 推导 vs 导入器的 accumulate-in-dict), banned-import 测试强制, 且 D2 难例 (FOCID/C119013 必须 1 域非 3) 被三条独立代码路 (extract_graph / reconcile yaml 再导 / 生产 GraphEngine) 三角验证一致 (`sp4_reconcile_gate.txt` 与 `sp4_cookbook_golden.txt` 均 1/1)。
- 幂等证明可靠: 全清 (`MATCH (n) DETACH DELETE n`) + 确定性排序抽取 + `snapshot()` 排序输出行 → byte-diff 是真正顺序无关的证明。
- D4 `model_only` 拆分**不污染**计数类 cookbook 查询: `HAS_VARIABLE` 边仅从域迭代循环发出, 18 个 model-only Variable 节点结构上不可能收到 `HAS_VARIABLE`/`USES_CT` 边 — 查询 ②③④⑤⑦ 由构造免疫 (非靠可被遗忘的 `WHERE` 过滤器); 仅 ⑥ defhome 有意包含且正确标注。
- 生产隔离双层校验: 静态 (`neo4j` 仅在 dev extra, 不在 `[project.dependencies]`) + 运行时 (`sys.modules` + 停机 grep), 停机 `477 passed` 佐证。
- fix-round commits (a7f7000 自校验 / 91327ac None 守卫+顺序无关比较 / 2ba8947 锚点) 显示实现者主动硬化了对抗式审查会盯的脆弱点。

## Findings

### BLOCKER
None.

### HIGH
None.

### MED
- **localhost-only 绑定硬约束无持久化证据** [→ 已补, 见 `sp4_localhost_binding.txt`]: Spec §1/§4 列 `localhost-only (127.0.0.1:7474/7687)` 为硬约束, plan Task 1 Step 4 / Task 2 Step 2 都跑 `lsof` 验证 — 但不同于 Gate 1-3 各有持久化 `.txt`, Task 1-2 (infra) 无 evidence artifact 捕获该 `lsof` 输出。security 是 5 审查轴之一, 且 Neo4j 绑定配置不在 repo 内 (仅 plist, 不 override 默认 listen address), 此前该主张靠未记录的手动验证。**处置: Task 8 fix 补 `evidence/checkpoints/sp4_localhost_binding.txt` (lsof + SHOW SETTINGS listen address), 与其他三门同证据粒度。**

### LOW
- `eval/prod_wirein/sp4_cookbook_golden.py:90` — `os.environ["NEO4J_PASSWORD"]` bare 下标, 未设时抛不友好 `KeyError`, 不一致于 `build_neo4j.py`/`reconcile_neo4j.py` 的 `SystemExit("NEO4J_PASSWORD missing…")`。**处置: Task 8 fix 统一为友好 SystemExit。**
- `scripts/reconcile_neo4j.py` — `snapshot()` node-key lambda `p.get("code") or p.get("name") or p.get("path")` label-agnostic; 当前数据集安全 (各标签键不撞), 但若未来加入与 Domain code 同名的 Variable 会脆弱。仅用于幂等证明 (非 counts 对账), 影响限于 diff 可读性非正确性。**处置: Task 8 fix 加一行注释说明假设。**

## Axis coverage
- **import-correctness:** PASS — driver 写计数器自校验完整 (节点+边), 悬空 target loud-fail 有测试, 全部计数 + N=9+2锚点邻域与活库逐一吻合 (41/41)。
- **idempotency:** PASS — 确定性排序抽取 + 全清重建 + 顺序无关 snapshot byte-diff 是真证明。
- **reconcile-independence:** PASS — 不同代码形态 + banned-import 测试 + 第三独立 lane (生产 GraphEngine) 在最难例 (D2/FOCID) 交叉验证; 共享假设 (变量-域唯一) 诚实披露且已由 SP1 reconcile_meta.py 把关。
- **security:** PASS with one gap — 密码不入 git (`.env` gitignored / `.env.example` 空 / evidence 无泄漏), 但 localhost 绑定主张缺持久化证据 (见 MED, 已补)。
- **deviations-D1-D4:** PASS — 四项均数据接地, 跨 extract_graph/tests/reconcile/cookbook/golden-harness 一致实现, D4 model_only 拆分经证由构造不污染计数查询。
