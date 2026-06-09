# S3 域长名→码映射 (longname-map) — Result Record

> 状态: **PASS / 零回归净增益** (2026-06-09) — retrieval-only, 102q (test_set_v2),
> collection `sdtm_kb_v1` (4146 chunks, 未重建)

## 背景 (Rule D 脆弱边界)
S1 确定性查表只在 query 字面命名 2 字母域码 (如 "DM") 时注入 `domains/<CODE>/spec.md`。
Rule D 复核发现唯一脆弱边界: 仅用**长名**的 single 查询 (如 "required variables in the
Demographics dataset", 不含 "DM") → `resolve()` 返回 `[]`, 确定性网失效, 这类 spec gold
在原始 cosine 下本就 miss。

## 堵法
从 `VARIABLE_INDEX.md §二` 域标题 `### CODE — Long Name (Class)` 解析
`domain_longname → code` 映射 (通用, 从 KB 来, 无硬编码)。`resolve()` 扩展: query 含某域
**完整长名** (word-boundary, 大小写不敏感, 最长匹配优先) → 该 `domains/CODE/spec.md`
union-add 进 targets, 受现有 `_MAX_DOMAIN_SPECS=3` cap 约束。

## 保守防撞 (collision guard)
- 跳过 SUPPQUAL 这类含 `[domain name]` 占位的标题 → 62 长名入 map。
- 长名为**单个短词** (1 词且 <10 字符) 时不建 matcher → 排除 `Exposure`(EX)/`Comments`(CO)
  这类高歧义通用词; 保留 `Demographics`/`Disposition`/`Procedures`/`Questionnaires`
  (单词但 ≥10 字符, 足够特异) 及全部多词长名 (`Adverse Events`/`Vital Signs`...)。
  → 60 个 matcher 生效。
- 效果: q96 "Cumulative Exposure" (FA 题的测试名示例) 不再误注入 EX/spec.md。

## 复现命令 (.venv/bin/python, retrieval-only)
```
# before (longname-map 之前) 与 after 用同一最优配置
.venv/bin/python eval/run_eval.py eval/test_set_v2.yml --retrieval-only \
  --structured-lookup --hybrid --output evidence/checkpoints/s3_before.json   # 改前 git stash 时
.venv/bin/python eval/run_eval.py eval/test_set_v2.yml --retrieval-only \
  --structured-lookup --hybrid --output evidence/checkpoints/s3_after.json
.venv/bin/python -m pytest        # 214 passed
```

## 逐类别 src recall: BEFORE → AFTER (最优配置 --structured-lookup --hybrid)
| 类别 | before | after | delta |
|------|--------|-------|-------|
| single_domain | 100.0% | 100.0% | +0.0 |
| cross_domain  | 96.0%  | 96.0%  | +0.0 |
| concept       | 100.0% | 100.0% | +0.0 |
| mixed         | 100.0% | 100.0% | +0.0 |
| **OVERALL**   | **99.0%** | **99.0%** | **+0.0** |

四类别全部仍 ≥95%。唯一 miss 仍为 q73 (gold `model/06_relationship_datasets.md`, 与本改动无关)。

## 零回归 GATE (逐题 diff before vs after)
- 102 题: **0 题 recall 下降, 0 题 recall 上升**。
- 仅 3 题 top5 顺序变化 (注入位于 rank 1-2, 把已命中 gold 之后的 tail 下移 1 格, gold 全部仍在 k=15 内):
  - q09 (cross): 注入 AE/spec ("adverse events"), gold RELREC/spec 仍 rank1。
  - q18 (mixed): 注入 AE/spec ("adverse events"), gold AE/spec+assumptions 仍命中。
  - q19 (mixed): 注入 DS/spec ("disposition"), gold DS/assumptions+disposition 仍命中。
- GATE: zero regression = **True**。

## 长名探针 (resolve 返回 + 真实 KB 核对; 这些 query 不含 2 字母码)
| probe query | resolve() | KB spec 首行标题 |
|-------------|-----------|------------------|
| required variables in the **Demographics** dataset | `domains/DM/spec.md` | `# DM — Demographics` |
| structure of the **Vital Signs** dataset | `domains/VS/spec.md` | `# VS — Vital Signs` |
| variables in the **Adverse Events** dataset | `domains/AE/spec.md` | `# AE — Adverse Events` |
| **Medical History** dataset structure | `domains/MH/spec.md` | `# MH — Medical History` |
| purpose of the **Trial Summary** dataset | `domains/TS/spec.md` | `# TS — Trial Summary` |
| **Questionnaires** structured in SDTM | `domains/QS/spec.md` | `# QS — Questionnaires` |

全部命中正确 spec.md, 长名与 spec 自身 `# CODE — Long Name` 标题一致。

## 结论
净增益 / no-op, 绝无净负。长名 single 查询现可被确定性网兜住 (Rule D 脆弱边界已堵);
v2 既有 4 类全 ≥95% 无一题回退。pytest 214 passed。

## 改动文件
- `server/structured_lookup.py`: 新增 `_DOMAIN_HEADER_RE`、`domain_longname_to_code` +
  `_longname_matchers`、`_build_domain_longname_index()`、`_query_longname_domains()`;
  `_query_domains()` union-add 长名匹配 (code-token 优先)。
- 测试集 / KB / bm25 / embedding 均未动; 默认仍 off (`--structured-lookup` flag 才生效)。
