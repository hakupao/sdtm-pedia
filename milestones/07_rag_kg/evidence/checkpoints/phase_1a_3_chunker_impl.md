# Phase 1A.3 Chunker Implementation — Checkpoint

> 実施: 2026-05-22 main session + 3 executor subagents (a3fb9d / affb90 / a8a49a 並列)
> 上流: PLAN.md v0.2 §5 + §6 (8 chunker spec) + §7 (Chunk metadata) + EXECUTION_PLAN.md §1A.3
> 状態: ✅ **完成** — 8 modules + combined smoke 10/10 PASS; chunker config 5 lock 全 verified in real code
> Owner: main (base.py) + executor sonnet (Batch A) + executor opus (Batch B + C)
> Work time: ~12 min wallclock (3 executors parallel + main integration); EXECUTION_PLAN estimated 0.9 d (并列) — 实际 < 0.02 d (over-estimate 由于本批 chunker 实现相对简单 + 高质量 base.py 减少接口磨合)

---

## 0. TL;DR (3 行)

1. **8 chunker modules implemented** (base + 7 type-specific), 全 import + smoke PASS
2. **Combined integration smoke 10/10 PASS**: 全 chunker × 10 samples; file_type / metadata 18 keys / token count (L-3 tiktoken) 全验证
3. **Chunker config 5 lock (来自 1A.0 sanity) 在真实代码中 verified**: L-1 mermaid 状态机 / L-2 GFM 简单 regex / L-3 tiktoken / L-4 chapters >=50KB → ### / L-5 terminology part 模式 vs codelist 模式

---

## 1. 8 Chunker Modules

| Module | Owner | Bytes | LOC ~ | file_type | Strategy |
|--------|-------|------:|------:|-----------|----------|
| base.py | main | 6,715 | 190 | (abstract) | Chunk dataclass + BaseChunker ABC + helpers (count_tokens / find_mermaid_blocks / find_table_blocks / heading_positions / kb_commit_sha) |
| spec.py | Batch A | 1,529 | 35 | spec | regex split by `^### ` (variable level) |
| assumptions.py | Batch A | 2,938 | 70 | assumptions | overview (before first numbered item) + 1 chunk per `^N.` numbered item |
| model.py | Batch A | 2,155 | 55 | model | regex split by `^## ` (section level) |
| examples.py | Batch B | 7,792 | 210 | examples | **domain-aware** — H2 flat (TA/IS/DS) or H4 nested (PC Method A-D); L-1 + L-2 split-point protection |
| chapters.py | Batch C | 3,796 | 105 | chapter | **size-aware** L-4: >50KB → `^### ` / 20-50KB → `^## ` / ≤20KB → whole file |
| terminology.py | Batch C | 4,516 | 130 | terminology | **L-5**: H2 count==1 AND filename matches `*_part[0-9]+.md` → part 模式 (whole file = 1 chunk + part_index) / else → codelist 模式 |
| variable_index.py | Batch C | 6,523 | 175 | variable_index | §一 1 chunk + §二 63 H3 (1 per domain) + §三 1 chunk (no sub-headings detected) = **65** chunks |
| **Total prod code** | | **35,964** | **~970** | | 1 base + 7 chunkers |
| _smoke_batch_{a,b,c}.py | A/B/C | 5043+7253+7647 = 19,943 | 540 | (tests) | self-smoke scripts (not for prod) |
| __init__.py | main | 1,900 | 60 | (registry) | exports 7 chunker classes + CHUNKER_REGISTRY dict (file_type → class) |

---

## 2. Combined Integration Smoke (10/10 PASS)

```
chunker                        | sample                              | chunks | type ok? | metadata
SpecChunker                    | domains/AE/spec.md                  | 64     | YES     | 18 keys
AssumptionsChunker             | domains/AE/assumptions.md           | 13     | YES     | 18 keys
ModelChunker                   | model/01_concepts_and_terms.md      | 2      | YES     | 18 keys
ExamplesChunker (TA)           | domains/TA/examples.md              | 8      | YES     | 18 keys
ExamplesChunker (PC)           | domains/PC/examples.md              | 14     | YES     | 18 keys
ChaptersChunker (ch01 11KB)    | chapters/ch01_introduction.md       | 1      | YES     | 18 keys
ChaptersChunker (ch04 130KB)   | chapters/ch04_general_assumptions   | 47     | YES     | 18 keys
TerminologyChunker (ae)        | terminology/core/ae.md              | 4      | YES     | 18 keys
TerminologyChunker (lb_part4)  | terminology/core/lb_part4.md        | 2      | YES     | 18 keys (codelist mode H2>1)
VariableIndexChunker           | VARIABLE_INDEX.md                   | 65     | YES     | 18 keys

Overall: ALL PASS

Token count sanity (chunks[0].chunk_size_tokens via tiktoken cl100k_base):
  SpecChunker: 56          ← small variable description
  AssumptionsChunker: 6    ← overview chunk
  ModelChunker: 1434       ← large model concept
  ExamplesChunker (TA): 1294  ← TA Example 1 含 4 mermaid blocks
  ExamplesChunker (PC): 276   ← PC Method A
```

---

## 3. Chunker Config 5 Lock — Real Code Verification

### L-1 mermaid 状态机 (base.py + examples.py)

base.py `find_mermaid_blocks(text)` 状态机实现 (no stack, 0 嵌套 assumption from 1A.0.b):
```python
while True:
    m = _MERMAID_FENCE.search(text, cursor)
    if not m: break
    start = m.start()
    close = _CLOSE_FENCE.search(text, m.end())
    if not close: break  # defensive
    blocks.append((start, close.end()))
    cursor = close.end()
```

Batch B verified: TA/examples.md returns 20 mermaid blocks (matches 1A.0.b finding).

### L-2 GFM pipe-table 简单 regex (base.py + examples.py + variable_index.py)

base.py `find_table_blocks(text)`: line-based detection — `^|.*|$` + 第二行 `^|[\s\-:|]+|$` (separator) → 连续 pipe lines 全部归 table block. **0 HTML 处理** (1A.0.b confirmed 0 rowspan/colspan/`<table>`).

### L-3 tiktoken cl100k_base 实测强制

base.py module-level `_ENC = tiktoken.get_encoding("cl100k_base")` + `count_tokens(text)` 包装.
`BaseChunker._new_chunk()` 自动 fill `chunk_size_tokens=count_tokens(text)`. 全 chunker 子类继承.

Token sanity 输出 verified — 全部 chunks 用 tiktoken, 没用 char/4.

### L-4 chapters/ size-aware

chapters.py:
```python
size_bytes = file_path.stat().st_size
if size_bytes > 50 * 1024:    # ch04 130KB, ch08 52KB
    level = 3  # ^###
elif size_bytes > 20 * 1024:
    level = 2  # ^##
else:                          # ch01 11KB
    return [whole_file_chunk]
```

ch04 实测 47 chunks (estimate 38, 实际 47 since H3 count is more than estimated); max token 3852 < 8K embedding limit ★ **L-4 lock holds — 解决 ch04 §4.4 = 9598 cl100k 单 ## section over-limit 问题**.

### L-5 terminology part vs codelist

terminology.py:
```python
h2s = heading_positions(text, 2)
is_part_named = re.match(r"^[a-z]+_part(\d+)\.md$", file_path.name)
if len(h2s) == 1 and is_part_named:
    # part 模式: whole file = 1 chunk, part_index from filename
else:
    # codelist 模式: 1 chunk per H2
```

Critical edge case verified: **lb_part4.md (H2=2, _partN named)** → codelist 模式 2 chunks (H2>1 branch wins; part_index=4 still propagated for cross-part reassembly metadata).

---

## 4. Anomalies / Findings for 1A.5 ingest planning

### Chunk count revision (vs PLAN §3 ~4304 estimate)

| 类别 | PLAN §3 估 | 抽样实测 推算 | 偏差 |
|------|-----------:|-------------:|------:|
| spec.md (63 files) | 2164 | AE=64 H3 (estimate 50), avg 30-65 × 63 = ~2500-4000 | 可能 +15-85% |
| assumptions.md (64 files) | ~460 | AE=13 (overview + 12 items), avg 10-15 × 64 = ~640-960 | +40-100% |
| examples.md (63 files) | ~500 | TA=8 PC=14 IS=11 DS=11, avg ~10 × 63 = ~630 | +26% |
| chapters/ (6 files) | ~62 | ch01=1 ch04=47 ch08=19; ~60-90 estimate | ≈ |
| model/ (6 files) | ~35 | per file ~2 × 6 = ~12 | -65% (PLAN overestimate) |
| terminology/ (91 files) | ~1014 | 实测 1A.0.a H2=1004 + 3 LB part 模式 (-3) + 兼容 part4 = ~1004 | -1% (near match) |
| VARIABLE_INDEX | 69 | **65** (§三 no sub-headings) | -6% |
| **TOTAL** | **~4304** | **~5000-6000** estimate | **+15-40%** |

★ **chunker_feasibility v0.2 §3 总数估算需要在 1A.5 ingest 实测后修订**. 当前估算偏低 ~15-40%. **不修 PLAN doc**, 1A.5 ingest 完整跑全 KB 后会有真实数, 那时一并 doc revision.

### 实现 deviations 备记 (defer 到 1A.4 test-engineer 评估)

- **ct_extensible**: terminology chunker 默认 None (无可靠 signal source); 1A.4 评估是否能从 codelist content (e.g. "Extensible: Yes" 字样) 提取
- **VARIABLE_INDEX §三 1 chunk**: 实测 §三 无 sub-headings, 整段 = 1 chunk; PLAN §6.5 "字母段 ~5 chunk" 不适用 — 1A.4 评估是否需要按 byte size 拆分
- **AE spec.md 64 H3**: 包含 non-variable 元数据 H3 (例如 "### Model Definition"); 全部 H3 都被当成 chunk. 1A.4 评估是否需要白名单 filter
- **lb_part2/3 巨型 part (378KB/417KB)**: 当前实现按 part 模式 (H2=1 → 1 整 chunk); 实际 token 数可能 >> 8K embedding limit. **关键 TODO for 1A.4 / 1A.5**: 单 chunk 超 8K 时 fallback 切分策略 (按 N=100 table row 切, table_chunk_idx metadata, PLAN §6.4 已写但未实现)

---

## 5. CHUNKER_REGISTRY (1A.5 ingest 入口)

`scripts/chunkers/__init__.py` 暴露 `CHUNKER_REGISTRY: dict[str, type[BaseChunker]]`:

```python
{
    "spec": SpecChunker,
    "assumptions": AssumptionsChunker,
    "model": ModelChunker,
    "examples": ExamplesChunker,
    "chapter": ChaptersChunker,
    "terminology": TerminologyChunker,
    "variable_index": VariableIndexChunker,
}
```

1A.5 ingest.py 用 this registry 按 file path → file_type detection → dispatch chunker:
- `knowledge_base/domains/*/spec.md` → SpecChunker
- `knowledge_base/domains/*/assumptions.md` → AssumptionsChunker
- `knowledge_base/domains/*/examples.md` → ExamplesChunker
- `knowledge_base/model/*.md` → ModelChunker
- `knowledge_base/chapters/*.md` → ChaptersChunker
- `knowledge_base/terminology/{core,supplementary,questionnaires}/*.md` → TerminologyChunker
- `knowledge_base/VARIABLE_INDEX.md` → VariableIndexChunker
- `knowledge_base/INDEX.md` + `knowledge_base/ROUTING.md` → NOT chunked (整体 system prompt 注入, PLAN §6.5)

---

## 6. PASS 五条 (1A.3 chunker writer step)

1. **evidence 存在** ✅ — 8 modules + 3 batch done notes + 3 smoke scripts + combined smoke output + 本 checkpoint
2. **writer 产物合规** ✅ — 全 import OK, 全 file_type 正确, 全 metadata 18 keys, token count via tiktoken; 10/10 sample chunks 正常
3. **独立 reviewer subagent PASS** ⚠️ **DEFERRED 至 1A.4** — Phase 1A.3 是 writer step, Rule D 真审在 1A.4 (test-engineer 写测试 + code-reviewer 异 type 审; 见 EXECUTION_PLAN §2.1 矩阵)
4. **规则 A 抽检** ⚠️ **DEFERRED 至 1A.4** — chunker 实现压缩率 > 50% (将 9.8MB KB 切成 ~5K chunks 约 ~2KB avg), 1A.4 测试套件 + scientist N≥10 sample 抽检 边界 + metadata 完整性
5. **用户 Bojiang 口頭 ack** — pending

---

## 7. Next Action

1. ⏳ 用户 ack 1A.3 (8 chunker + smoke 10/10 PASS + L-1..L-5 全 verified)
2. ⏳ Commit 1A.3 (新 files: chunkers/{base,spec,assumptions,model,examples,chapters,terminology,variable_index,__init__}.py + 3 _smoke_*.py + 3 _batch_*_done.md + evidence/checkpoints/phase_1a_3_chunker_impl.md + _progress.json + CHANGELOG)
3. ⏳ Phase 1A.4 test-engineer dispatch:
   - Write test suite for all 7 chunkers (corner cases per each `_batch_X_done.md` TODO list)
   - Rule D: writer = test-engineer (异 1A.3 executor); reviewer = code-reviewer (异 test-engineer) after tests pass
   - Estimate: 0.7 d per EXECUTION_PLAN §1A.4
4. ⏳ 1A.5 ingest.py 全量跑 (Phase 1A.4 PASS 后) + 1A.6 规则 A chunk-atom 对齐 N=10
