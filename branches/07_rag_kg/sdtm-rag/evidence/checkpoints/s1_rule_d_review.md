# S1 Structured-Lookup — Rule D 独立 Reviewer 审查

> 判定: **PASS** (2026-06-09) — 独立 reviewer (非 executor 自审, Rule D 满足)
> Reviewer: code-reviewer agent. 全程跑真代码, 集合 `sdtm_kb_v1` (4146 chunks, 未重建)。

## 总判定: PASS

**反过拟合判定: 是真 pattern, 不是为 5 题量身定制。** 三重证据:
1. 代码无任何题号特例 / 写死 var→file 映射 (AESEV/VSTESTCD 仅出现在注释)。
2. 8 个测试集外变量的泛化探针全部返回与真实 KB 一致的术语文件。
3. v2 101 题 (含 48 道 v1 外新题) 零回归, 且救回 6 道全新题 (q67-q71/q90/q93)。

---

## 项 1 — 独立复现数字: PASS (属实)

| 类别 | baseline | +lookup | delta | 自报 |
|------|----------|---------|-------|------|
| single_domain | 96.4% | 100.0% | +3.6 | ✓ |
| cross_domain | 61.5% | 76.9% | +15.4 | ✓ |
| concept | 84.6% | 84.6% | +0.0 | ✓ |
| mixed | 92.3% | 100.0% | +7.7 | ✓ |
| **OVERALL** | **84.0%** | **90.6%** | **+6.6** | ✓ |

- Kill-switch: single_domain 96.4→100.0% (≥96.4 要求), **不降反升 PASS**。
- 零回归: +lookup 的 miss 集合 (6 题) 是 baseline miss 集合 (11 题) 的真子集。
- 5 道目标题 q07/q34/q16/s04/s05 全救回。
- 注: 用户标题 "+15.4pt" = cross_domain 类别 delta; overall 实际 +6.6。两口径数字均属实。
- 复现命令同自报 evidence; /tmp/rev_baseline.json + /tmp/rev_lookup.json。

## 项 2 — 反过拟合 (代码扫描): PASS

- grep `q07|q34|q16|s04|s05|hardcod|AESEV|AEACN|VSTESTCD` over structured_lookup.py + rag.py:
  仅命中文档注释和正则示例注释 (line 6/7/33/40), **无任何代码分支引用题号或目标变量**。
- 唯一 `.md` 字面量 = 注释里的 xref 格式示例 (line 33), 不是代码映射。
- resolve() 全部从全 KB 通用解析: 1523 known_variables / 524 var→termfile / 1005 ct→termfile / 135 ct→vars。
- **判定: 无硬编码, 无特例分支, 真通用解析。**

## 项 3 — 泛化探针 (测试集外变量): PASS

直接 import StructuredLookup, 对 8 个**不在 5 道目标题**的变量构造 NL query, resolve 输出核对真实 KB:

| 变量 | resolve 返回 | KB 真实核对 |
|------|------|------|
| RACE | terminology/core/dm.md | ✓ `## Race (C74457)` |
| SEX | terminology/core/dm.md | ✓ `## Sex (C66731)` |
| CMROUTE | terminology/core/interventions.md | ✓ `## Route of Administration (C66729)` |
| DSDECOD | terminology/core/disposition.md | ✓ Disposition codelists |
| LBTESTCD | terminology/core/lb_part2.md | ✓ `## Laboratory Test Code (C65047)` |
| QSCAT | terminology/core/qs_part1.md | ✓ `## Category of Questionnaire (C100129)` |
| VISITNUM | VARIABLE_INDEX.md | ✓ general var, 36 域共用 |
| MHTERM | `[]` (no-op) | ✓ 正确: Controlled Terms 为空 (自由文本), 该保守返回空 |

**判定: 对测试集外变量正确工作 = 真 pattern。** MHTERM 正确识别"无 codelist"尤其有说服力。

## 项 4 — 关键词过拟合 (pattern vs example): PASS (附 1 LOW)

清洁子进程逐词移除, 权威值取 JSON:

| 移除关键词 | overall | cross | single | 影响 |
|------|------|------|------|------|
| (full) | 90.6% | 76.9% | 100% | — |
| `extensible` | 90.6% | 76.9% | 100% | **零影响** |
| `values for` | 90.6% | 76.9% | 100% | **零影响** |
| `share` | 88.7% | 69.2% | 100% | q34 失败 |

- 最可疑的"具体词" `extensible` / `values for` 移除后 53q **逐题 recall 零变化** (s05 已被通用词 codelist/controlled term 触发)。它们是冗余安全网, 非 load-bearing。
- `share` 是 q34 唯一触发词, 但 "domains share codelist X" 是分布查询的**自然通用英语信号**, 非题面专属。合理 pattern。
- **LOW**: `extensible` / `values for` 是死代码式冗余关键词 (移除无任何损失), 可删以减少 example-shaped 表面积。不影响机制正确性, 不 block。

## 项 5 — 规模化 over-firing / collateral (v2 101 题): PASS

| | baseline | +lookup | delta |
|------|------|------|------|
| overall | 83.7% | 92.1% | +8.4 |
| single_domain | 98.1% | 100.0% | +1.9 |

- **逐题回归分析: 0 题下降** (无 VARIABLE_INDEX 误注入挤掉 gold)。
- 救回 11 题, 其中 **6 道是 v1 外全新题**: q67/q68/q69/q71 (cross), q90/q93 (mixed)。
- 新题变量/codelist (EXROUTE/EXDOSFRM/EXDOSU/CMDOSU, C66789/C71620/C78735) 全不在 v1 5 题里。
- **这是反过拟合最强证据: 同一机制泛化到从未见过的题, 零 collateral。**

## 项 6 — union-add 正确性: PASS

rag.py `_apply_structured_lookup` (L166-200):
1. resolve()=[] → `return cosine[:k]` (no-op, 向后兼容) ✓
2. `_lookup_chunk_for_file` 用 `where={"source": abs_source}` 过滤, 注入该 gold 文件对 query 最相关 chunk ✓
3. 合并 `lookup_chunks + cosine`, 按 `chunk_id` 去重, lookup 在前不被挤出 ✓
4. `merged[:k]` 截断 — v1+v2 共 154 题实证: single_domain 已命中 gold 无一被注入挤出 top-k ✓

## 项 7 — pytest: PASS

214 passed (72+72+70), exit 0。S1 未破坏任何现有测试。

## 非 S1 范围观察 (不 block)
- ruff: rag.py `_query_with_retry` (L337-343) 缺 explicit return (RET503)。属既有 query-expansion 代码, 非 S1 改动。LOW。
- lsp_diagnostics 无法运行 (ty / ast-grep 未安装); 用 py_compile + ruff + pytest 替代覆盖。

## 仍未覆盖 (符合设计, 非缺陷)
- concept (84.6%) 不动: miss 是 chapters/model 文件, 非变量/CT 查表场景。
- cross 余 miss q09/q33/q10/q32: 按域名/关系名定位 spec, S1 不覆盖。
