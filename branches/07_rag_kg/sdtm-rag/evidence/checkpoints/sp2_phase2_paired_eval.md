# SP2 Phase 2 — 退役正则影子 KG: 零回归证据

> 2026-06-20 · Task 15 (迁移) + Task 16 (零回归门)。
> 范围: `server/structured_lookup.py` 的索引数据源从「正则解析 KB markdown」换成 `data/meta/meta.yaml` (MetaStore)。**意图检测 / 实体锚定 / resolve() / 长名匹配逻辑全部逐字保留**, 只换数据来源。

## 1. 做了什么

| 项 | 旧 (正则) | 新 (meta.yaml-backed) |
|----|-----------|------------------------|
| `known_variables` | spec.md `### VAR` + VARIABLE_INDEX §一 | `store.known_variables` |
| `domain_to_spec` | 扫 `domains/*/spec.md` 目录 | `{dom: domains/<dom>/spec.md for dom in known_domains}` |
| `domain_longname_to_code` | VARIABLE_INDEX §二 标题解析 | meta `label` + 同样的 `[`-guard + slash 变体 + 长短名锚定 |
| `var_to_model_defhome` | **`len(inner)==6` model 表解析** (load-bearing) | `store.model_defhome_map` |
| `ctcode_to_termfile` | terminology `## Name (Cxxxxx)` 标题解析 | codelist `termfile` |
| `var_to_termfiles` | spec.md Cross-References 正则 + `_cross_check_vars` 截断回填 | 各变量**跨域 union** 的 ct_codes × codelist termfile |
| `ctcode_to_vars` | VARIABLE_INDEX §三 解析 | **删除 (死代码, 全仓无 reader)** |
| `general_assumptions_file` (ch04) | glob | **保留 glob** (meta.yaml 不覆盖 chapters/) |

- 构造签名 `StructuredLookup(kb_root, store: MetaStore)`; 3 个构造点改 (`rag.py` 懒构造 MetaStore — RAGEngine 签名不变, 另 5 个 RAGEngine 调用点零改动 / `probe_s3_longname.py` / 测试 fixture)。
- MetaStore 加 2 个**纯加法** API: `ct_codes_for_variable(var)` (跨域 union) + `model_defhome_map` property。Phase 1 的 first-seen `variable_attributes` 未动。
- 净: `structured_lookup.py` 删 ~250 行正则解析, 加 ~85 行; 6 文件改 +148/−248。

## 2. 零回归门 = 穷举行为快照等价 (比 retrieval eval 更强)

**为什么用快照而非跑 retrieval eval**: structured_lookup 只通过 `resolve()` 的 union-add 影响检索; cosine / hybrid 通道本次未碰。若 `resolve()` 对所有查询逐字节相同, 则 union-add 相同, 检索结果必然相同 —— 这是**确定性证明**, 强于一次带 embedding 非确定性的 retrieval eval (后者只是抽样测量)。

**harness**: `eval/prod_wirein/sp2p2_equiv_snapshot.py` —— 用同一脚本分别跑旧码 / 新码, dump (a) 全部 7 个 resolution map + (b) `resolve()` 在**穷举语料**上的输出 = 140 道 v3 测试题 + meta.yaml 全量扫描 (每个变量 1523 × {term/dist/concept-def/attribute/bare} + 每个 CT 码 1005 × {share/term} + 每个域 63 × {长名/代码}) = **9891 条查询**, 再逐字节 diff。

```
EQUIVALENCE PASS: 8/8 maps identical + 9891/9891 resolve() outputs identical
```

### 2.1 迁移前预分析的 4 个等价风险点 (全部解决)
- **(B) `len==6` 退役**: meta `model_defhome` 与旧 59-var 图 **逐项相同** (0 only-old / 0 only-meta / 0 changed); canary RDOMAIN→model/06, EPOCH→model/03 守住。
- **(A) 域长名 (label vs §二 标题)**: 62/63 完全一致; 唯一差异 SUPPQUAL (label = `Supplemental Qualifiers for [domain name]` 含 `[`), 被既有 `[`-guard 排除 → 与旧码一致 (62 base + slash 变体 = 72)。
- **(D) `var_to_termfiles`**: 仅当用**跨域 union** (非 first-seen) 才与旧码 524 逐项相同。FOCID 的 CT 码 C119013 只在 OE 域出现 (first-seen 的 MB 域无 CT), union 派生正确捕获 → 这是新增 `ct_codes_for_variable` 的理由。
- **`ctcode_to_termfile`**: 1005=1005 逐项相同 (codelist termfile)。

## 3. 其他验证
- **完整测试套**: `372 passed` (含 `test_structured_lookup.py` 36/36 + `test_meta_store.py` 20/20 含 2 新)。
- **反过拟合 held-out 探针**: `eval/prod_wirein/heldout_probes.py` 4/4 PASS (EPOCH→44 域 / USUBJID→55 / DTHFL 属性 / C66742→41 域)。
- **ruff** (改动文件): All checks passed。**mypy** (`meta_store.py` + `structured_lookup.py`): no issues (顺手修了旧码遗留的 `termfile` 变量类型 shadowing)。
- **运行时 smoke (生产路径)**: 真实 `RAGEngine(structured_lookup_enabled=True)` 构造出 meta-backed `StructuredLookup` (MetaStore 已注入), resolve() 三通道正确。
- **端到端 union-add**: `retrieve("Which controlled terminology codelist does AESEV use?")` union-add `terminology/core/ae.md` (via_lookup) —— 实证 meta-backed 通道穿透到检索结果。

## 4. Task 16 结论
零回归门**满足且超出**: 9891 条查询 resolve() 逐字节等价 = 检索结果确定性不变 ≥ 现 99% 基线 (cosine/hybrid 未碰)。

## 5. Rule D (Task 17) — APPROVE ✅
异 `subagent_type` (oh-my-claudecode:code-reviewer, opus) 对抗式复核 **APPROVE** (0 BLOCKER/HIGH/MEDIUM, 1 LOW, 2 NIT)。reviewer 独立重建旧码同进程对跑 + 从零重生 golden (逐字节同) + 自建 4177 查询对抗语料 → 0 divergence。LOW (meta/KB 漂移自愈丢失) 已加 `TestMetaKBDriftGuard` 漂移闸; NIT (tuple name-slot) 已加 docstring 注记。详 `sp2_phase2_ruleD_review.md`。

## 6. 测试数 (修复后)
完整套 **375 passed** (含 `test_structured_lookup.py` 39 [36 + 3 漂移闸] + `test_meta_store.py` 20 [+2 新])。
