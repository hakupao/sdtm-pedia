# Phase 1A.3 Batch C — Done

> 实施: 2026-05-22 — Batch C executor (med-risk chunkers)
> 上游: PLAN.md §6.3 / §6.4 / §6.5 + EXECUTION_PLAN.md §1A.3 Batch C + phase_1a_0_sanity.md §4 (L-3/L-4/L-5)

## Deliverables

| 文件 | bytes | 说明 |
|------|------:|------|
| `scripts/chunkers/chapters.py` | 3796 | size-aware split (>50KB→### / 20-50KB→## / ≤20KB→whole) |
| `scripts/chunkers/terminology.py` | 4516 | H2==1+_partN→part mode / 否则 codelist mode |
| `scripts/chunkers/variable_index.py` | 6523 | §一 1 + §二 63 (H3 domain) + §三 1 = 65 chunks |
| `scripts/chunkers/_smoke_batch_c.py` | 7647 | 26 个 assertion, 全 PASS |

无修改: `base.py`, `spec.py`, `assumptions.py`, `model.py`, `examples.py` (其他 batch 范围).

## Self-smoke 结果 (26/26 PASS)

### ChaptersChunker

| sample | size | expected chunks | actual | 备注 |
|--------|-----:|----------------:|-------:|------|
| ch01 (~11KB, ≤20KB) | 11070 B | 1 (whole_file) | 1 | section="whole_file" |
| ch04 (~130KB, >50KB) | 130532 B | 47 (### split) | 47 | grep `^### ` = 47 (含 §4.4/4.5 等 sub-section); chunk[0]="4.1.1 …", cdisc_section_id="4.1.1" |
| ch08 (~52KB, >50KB) | 51764 B | 19 (### split) | 19 | grep `^### ` = 19 |

**ch04 token range: 32–3852** (max < 8000, L-4 lock 满足, 完美避开 §4.4 = 9598 token over-limit).

### TerminologyChunker

| sample | H2 | mode | expected chunks | actual | 备注 |
|--------|---:|------|----------------:|-------:|------|
| ae.md | 4 | codelist | 4 | 4 | ct_code 解析: C66767/111110/66768/66769 |
| lb_part1.md | 1 | **part** (H2==1 + _part1) | 1 | 1 | part_index=1, section="lb_part1" |
| lb_part4.md | 2 | **codelist** (H2>1, 即使是 _part4) | 2 | 2 | ★ 1A.0.a 硬要求: H2=2 走 codelist; ct_code C102580/C179589 解析 OK |
| questionnaires_part1.md | 66 | codelist | 66 | 66 | — |

### VariableIndexChunker

| section | expected chunks | actual | 备注 |
|---------|----------------:|-------:|------|
| §一 通用变量 | 1 | 1 | section="§一 通用变量" |
| §二 领域专属变量 (63 H3) | 63 | 63 | chunk[1]: domain="AE", class="Events"; 全 63 chunk 都有 domain |
| §三 CT 交叉引用 | 1 | 1 | 单大表格无 sub-heading, task 说明 "if no clear sub-headings, just 1 chunk" |
| **TOTAL** | **65** | **65** | task 估算 ~69 (§三 ~5), 实测 §三 = 1 (无 ###/##), 65 = 1+63+1 |

## Edge cases / 关键决策

1. **L-4 (chapters >50KB → ###)**: ch04 grep `^### ` = 47 (不是 task 估算的 ~38; 估算可能漏数). ch04 实际 47 sub-sections (`### 4.1.1 ... 4.10.x`). 所有 chunk 最大 3852 token < 8K, **L-4 lock 验证成功** — §4.4 那种 9598 token over-limit case 被 ### 切分有效解决.

2. **L-5 (lb_part4 H2=2 → codelist 模式)**: 实现严格按 `len(h2s) == 1 AND filename matches _partN` 判 part 模式. lb_part4 文件名虽然带 `_part4`, 但 H2=2 → 走 H2>1 分支 = codelist 模式 (2 chunks). 同时 `part_index=4` 仍写入 chunk metadata (filename signal, 给下游 lb 系列跨 part 重组用).

3. **VARIABLE_INDEX §三 = 1 chunk (不是 ~5)**: §三 全 KB grep 后无任何 `^### ` 或 `^#### ` sub-heading, 是单一巨型 GFM table (135 CT codes). 按 task 指令 "if no clear sub-headings, just 1 chunk for §三" 处理.

4. **`cdisc_section_id` 解析**: chapters 用 `^(\d+(\.\d+){0,3})\s+` regex, 严格只接受数字+点格式. `### 4.1.1 Title` → "4.1.1"; `### 4.1.10 Title` → "4.1.10"; 不会误捕 "4." 后没数字的字符串.

5. **`cdisc_class` 在 §二 来自 H3 末尾括号**: regex `(.+?)\s+—\s+(.+?)(?:\s+\(([^)]+)\))?` — group 3 (parens content) 取作 class. 实测 "AE — Adverse Events (Events)" → domain="AE", class="Events".

6. **`ct_extensible` deferred (None)**: 当前 H2 heading + body 中无可靠 "Extensible" 标记 signal (codelist body 是表格, 表格列未显式含 extensible flag). PLAN §6.4 列了字段, 但未给信号来源. 留 None, 转 1A.4 test-engineer / 1A.6 review 二审决定信号源.

## TODOs for 1A.4 test-engineer

1. **chapters.py 边界**: ch10 (30KB) 应走 `^## ` 分支 (level 2). 当前 smoke 没覆盖 20-50KB 中段; 1A.4 应加 ch10/ch03 (~20KB) 覆盖.

2. **terminology.py 巨型 codelist (lb_part2/3 >6K token)**: 当前 H2=1 part 模式生成 1 chunk, 但 lb_part2 全 file 可能 > embedding 8K limit. 1A.0.a 表 §4.1 提到 "巨型 codelist 跨 part 切片" 但未在本批次 in-scope. 1A.4 应实测 `lb_part1/2/3` 的 chunk_size_tokens, 若 > 8K, 1A.5 需加 N=100 row 表内切片 (PLAN §6.4 提到的 `table_chunk_idx`).

3. **terminology.py ct_extensible 信号**: 1A.4 应扫一遍 ~10 个 codelist 看是否有 "Extensible: Yes/No" 模式, 决定 regex 信号源或保持 None.

4. **VARIABLE_INDEX §三 token check**: 实测 §三 单 chunk token 数; 若 > 8K (135 CT codes 大表格), 1A.5 ingest 时需要 row-based 切片回退方案 (类似 lb_part2/3 处理).

5. **小验证**: assumptions/spec 对 file_type 一致性, terminology / variable_index 对 to_metadata() rename 'class' 字段, 全部满足.

## 收尾

- Step 6 (DO NOT commit): 不做 git add/commit.
- 状态写回 / `_progress.json` 更新由主 session 在 cross-review 后处理.
- 本批次完成确认: 3 chunkers + smoke + done note 齐备, 26/26 assertion PASS.
