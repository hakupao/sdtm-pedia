# SP2 Phase 2 — Rule D 独立审 (Task 17)

> 2026-06-20 · 异 `subagent_type` (`oh-my-claudecode:code-reviewer`, opus) 对抗式复核, fresh context, writer ≠ reviewer。
> **VERDICT: APPROVE** — 0 BLOCKER / 0 HIGH / 0 MEDIUM / 1 LOW / 2 NIT。

## 审阅范围
7 文件: `structured_lookup.py` (重写) / `meta_store.py` / `rag.py` / 2 测试 / `probe_s3_longname.py` / `sp2p2_equiv_snapshot.py` (新)。

## reviewer 独立验证 (不信 writer 产物, 自己重做)
1. 从 `git HEAD` **重建旧码** (615 行, 含 `len(inner)==6` 解析 / `_cross_check_vars` / `ctcode_to_vars` / spec.md+VARIABLE_INDEX 正则), 用 `importlib` 在**同进程**跑旧 vs 新 —— 不依赖 writer 的换码重跑。
2. **从零重生 golden** (旧码): 与提交的 `/tmp/sp2p2_golden_old.json` **逐字节相同** (`writer-golden == my-OLD-golden: True`) → golden 非陈旧/伪造。
3. 重跑 writer harness diff: `8/8 maps identical + 9891/9891 resolve() identical`。
4. **独立 map 级 diff** (不用 writer 语料): 7 个 live map 全逐字节相同 (var_to_termfiles 524=524 零多加/零漏/零顺序变 · known_variables 1523 · domain_longname 72 · model_defhome 59 · ctcode_to_termfile 1005 · domain_to_spec 63 · ch04 同)。
5. **自建对抗语料 4177 查询** (无锚长名 / `codelist for X` / `allowed values for Cxxxx` 等专门绕开 writer 语料) + 19 道手工边界 (多变量 term 顺序 / `_MAX_DOMAIN_SPECS` 5-8 码 / slash 变体 / "Exposure dataset" vs "Cumulative Exposure" 碰撞 / mixed dist+concept / FOCID union-CT / 大写散文 def-verb 陷阱 / dist 抑制 generic) → **0 divergence**。

合计 ~14k 查询 + 全 map 等价, reviewer **构造不出任何 divergence**。

## findings + 处置
- **[NIT] rag.py lint/mypy 是 pre-existing** (HEAD 同样 2 ruff + 18 mypy, 全在未改方法; 我的 12 行 diff 零新增)。reviewer 确认 6 个真改文件 100% ruff-clean。→ **无需动** (rag.py 既有问题不在本次范围)。
- **[NIT] tuple name-slot 差异**: 旧 `_cross_check_vars` 回填 `(code, code, termfile)`, 新 `(cl["name"], code, termfile)`; 仅 `termfile` 被 resolve() 读, 不可观测。→ **已加 docstring 注记** (`_build_var_termfile_index` 说明只有 termfile 可观测, name/code 非 load-bearing)。
- **[LOW] 等价依赖 meta.yaml 与 KB 保持对账**: 旧码 init 时实时重解析 KB (KB 改了自愈), 新码读 meta.yaml; 若 KB 重建未重生 meta.yaml 会**静默漂移**。→ **已加漂移闸 pytest** `TestMetaKBDriftGuard` (3 用例: domain_to_spec 路径全在盘上 / on-disk `domains/*/spec.md` 数 == meta n_domains / ch04 文件存在) —— 域级漂移即测试失败而非静默降级; 完整 var/CT 对账仍是 `scripts/reconcile_meta.py` (KB 重建后跑)。

## 修复后复验
- `test_structured_lookup.py` 39/39 (36 + 3 漂移闸); 完整套 **375 passed**。
- 等价快照仍 **8/8 maps + 9891/9891 identical** (docstring/测试新增不改行为)。
- ruff + mypy (改动文件) clean。

## reviewer 正面结论 (节选)
- "Genuinely behavior-preserving. ~14k queries + full map equality, **zero divergence**."
- "var_to_termfiles 从 first-seen back-fill 换成跨域 union 恰好正确: union 是必须的 (FOCID→C119013 只在 OE) 且零多加 (524=524, 顺序保留)。"
- "`ct_codes_for_variable` union accessor is the right fix, correctly additive (first-seen 路径未动, Phase-1 不受影响)。"
- "No circular import. Real `RAGEngine(structured_lookup_enabled=True)` builds and resolves correctly."
