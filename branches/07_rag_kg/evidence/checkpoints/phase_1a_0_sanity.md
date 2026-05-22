# Phase 1A.0 Sanity Re-grep Verify — Checkpoint

> 实施: 2026-05-22 main session 启动 1A.0
> 上游: PLAN.md v0.2 §5 Phase 1A.0 + EXECUTION_PLAN.md v0.2 §1A.0 + chunker_feasibility v0.2 §13 (R-13)
> 目的: chunker writer 1A.3 启动前, 不信任 chunker_feasibility 估算, re-grep verify 6 项 [UNVERIFIED]
> 工期: 0.3 d (实际单 session 完成)
> Owner: main session 直接 Bash + Read + Python (tiktoken)
> 状态: ✅ **完成** — 6 项全 verify, chunker config defaults 锁定, 总 chunk 估算微调

---

## 0. TL;DR (3 行)

1. **HIGH 发现 (C3)**: ch04 §4.4 单 `##` section = **9598 cl100k tokens > 8191 embedding limit** → 强制确认 chunker_feasibility §4 "ch04 必须按 `### ` 切" 的判定, chunker `chapters.py` size-aware 必须 default ≥ 50KB → `### ` (不允许跌回 `## `)
2. **MED 发现 (char/4 → tiktoken)**: char/4 估算最大偏差 **+23.6%** (MB dense table) → chunker 实现必须用 **tiktoken 实测**, 不允许 char/4 (chunker_feasibility 内估算仅作 magnitude 判断)
3. **LOW 复核**: terminology H2 累计实测 **1004** (chunker_feasibility v0.2 估 1005, near-exact), 0 HTML rowspan/`<table>`, mermaid fence 全 balanced (29 块 / 58 fence)

总 chunk 数估算从 ~4368 微调至 **~4304** (-1.5%, 误差在 chunker_feasibility v0.2 容许 ±5% 内, 不需要 chunker_feasibility 文档增订).

---

## 1. 1A.0.a — terminology 三系 H2 全量 grep (R-13 第 1-3 项)

### 1.1 supplementary_part 系列 (6 files, 全 codelist 模式)

| file | size | H2 (codelist) |
|------|------|---------------|
| supplementary_part1.md | 72 KB | 27 |
| supplementary_part2.md | 85 KB | 30 |
| supplementary_part3.md | 90 KB | 46 |
| supplementary_part4.md | 89 KB | 38 |
| supplementary_part5.md | 87 KB | 42 |
| supplementary_part6.md | 25 KB | 5 |
| **合计** | **448 KB** | **188 H2** |

**结论**: supplementary_part1-6 全是 codelist 模式 (多 H2/文件), 不存在"part 占整文件"模式. chunker `terminology.py` default `^## codelist` 切即可, **不需要 part 兜底**.

### 1.2 questionnaires 系列 (43 files, 全 codelist 模式)

H2 分布 (questionnaires_part1-43.md):
- min 1 (part18/19/43, 单 instrument 占整 part), max 66 (part1), median ~17
- **合计 670 H2 codelist** (= 每 questionnaire instrument 一个 codelist)

**结论**: questionnaires 走 default codelist 切法. 单 H2 文件 (part18/19/43) 与 lb_part1/2/3 同模式 (整 file = 1 chunk), terminology chunker 已有兜底.

### 1.3 core/ part files 系列 (31 files, 混合模式)

| 系 | 文件数 | H2 合计 | part 模式 (H2=1 占整 file) | codelist 模式 (H2>1) |
|----|--------|---------|---------------------------|----------------------|
| cp | 2 | 4 | 0 | 2 |
| eg | 3 | 9 | 0 | 3 |
| general | 5 | 24 | 3 (part1/3/5) | 2 (part2 H2=8, part4 H2=13) |
| is_domain | 2 | 4 | 1 (part2) | 1 (part1 H2=3) |
| lb | 4 | 5 | 3 (part1/2/3, 巨型 codelist 跨 part) | 1 (part4 H2=2) |
| microbiology | 3 | 6 | 2 (part2/3) | 1 (part1 H2=4) |
| oncology | 2 | 11 | 0 | 2 |
| other | 5 | 34 | 1 (part3) | 4 |
| pk | 4 | 7 | 2 (part2/4) | 2 (part1 H2=2, part3 H2=3) |
| qs | 1 | 1 | 1 (part1) | 0 |
| **合计** | **31** | **104** | **13** | **18** |

**确认**: 13 个 part 文件是 "part 占整文件"模式 (H2=1), terminology chunker 必须有 part 模式分支 (chunker_feasibility §6.3 已写). lb_part4 H2=2 兼容已确认.

### 1.4 core/ 单文件 codelist 系列 (11 files)

| file | size | H2 |
|------|------|-----|
| ae.md | 4.0 KB | 4 |
| dm.md | 4.9 KB | 5 |
| disposition.md | 9.8 KB | 5 |
| findings_about.md | 67 KB | 4 |
| gf.md | 16 KB | 6 |
| interventions.md | 89 KB | 6 |
| mi.md | 67 KB | 3 |
| oi.md | 5.0 KB | 2 |
| special_purpose.md | 1.0 KB | 1 |
| trial_design.md | 48 KB | 3 |
| vs.md | 27 KB | 3 |
| **合计** | **339 KB** | **42 H2** |

### 1.5 terminology 总 H2 累计

```
core/ 单文件 codelist (11 files):                42
core/ part files (31 files):                    104
supplementary/ supplementary_part (6 files):    188
questionnaires/ questionnaires_part (43 files): 670
-------------------------------------------------------
TOTAL terminology H2 codelist:                 1004
```

**vs chunker_feasibility v0.2 §6.2 估算 1005**: near-exact match, off-by-one (可能 lb_part2/3 同 LBTESTCD codelist 跨 part 切片是否独立计 1 vs 计 2 的边界判断差异). **接受**, 不需修 chunker_feasibility.

---

## 2. 1A.0.b — mermaid 嵌套 + 表格变体验证 (R-13 第 4-5 项)

### 2.1 mermaid block 嵌套扫描

全 KB examples.md 含 mermaid 的 5 文件:

| file | ```mermaid 开 | total ``` fence | balanced? |
|------|--------------|------------------|-----------|
| domains/TA/examples.md | 20 | 40 | ✅ |
| domains/DM/examples.md | 4 | 8 | ✅ |
| domains/TD/examples.md | 3 | 6 | ✅ |
| domains/TV/examples.md | 1 | 2 | ✅ |
| domains/RELSPEC/examples.md | 1 | 2 | ✅ |
| **合计** | **29** | **58** | **全 even, 0 嵌套** |

**结论**: 0 个嵌套 fence (无 ` ``` ` inside ` ```mermaid `), 0 个 unbalanced. **chunker examples.py split-point 保护实现简单**:
```python
# 状态机: 遇 ```mermaid 进入 mermaid 块, 遇下一个 ``` 退出. 不需要 stack.
```

### 2.2 表格变体扫描

```bash
grep -rEln 'rowspan=|colspan=' knowledge_base/  # 0 命中
grep -rln  '<table'           knowledge_base/  # 0 命中
```

**结论**: 全 KB **0 个 HTML `<table>`, 0 个 rowspan/colspan**. 所有表格都是 GFM (GitHub Flavored Markdown) pipe-table 格式. **markdown 解析库选择**:
- ✅ 简单 regex GFM pipe-table 识别即可 (检测 `^|` 行 + 下一行是 `---` 分隔)
- ❌ 不需要 mistletoe / markdown-it-py / commonmark 等重型 parser

**附加观察 (非 R-13 但发现)**: multi-line cell 检查需要在 examples.md TA/DM/IS table 中验, 暂未发现 (GFM pipe-table 不支持多行 cell, 全 KB 应该都是单行). 1A.3 chunker 测试套件中应专项断言 "table block = 连续 pipe 行 + 单独分隔行 + 后续连续 pipe 行".

---

## 3. 1A.0.c — tiktoken 实测 5 候选 chunk (R-13 第 6 项)

### 3.1 实测结果 (`branches/07_rag_kg/scripts/sanity_tiktoken.py`, tiktoken 0.12.0)

| chunk | lines | bytes | chars | **cl100k** | o200k | char/4 估 | δ (cl100k - char/4) | safe (< 8191)? |
|-------|------:|------:|------:|-----------:|------:|----------:|--------------------:|---------------|
| C1 TA examples Example 1 (4 mermaid + 1 table, 113 行) | 113 | 6,514 | 6,504 | **1,488** | 1,490 | 1,626 | -138 | ✅ |
| C2 MB examples Example 3 (dense table, 91 行) | 91 | 12,866 | 12,866 | **3,974** | 3,969 | 3,216 | +758 | ✅ |
| C3 ch04 §4.4 Actual/Relative Time (`## ` section, 463 行) | 463 | 38,097 | 38,081 | **9,598** | 9,569 | 9,520 | +78 | **❌ OVER 8K** |
| C4 lb_part4 整文件 (H2=2, 27 行) | 27 | 1,700 | 1,700 | **401** | 398 | 425 | -24 | ✅ |
| C5 VARIABLE_INDEX §二.AE (L51-L109) | 59 | 4,465 | 4,417 | **1,243** | 1,245 | 1,104 | +139 | ✅ |

### 3.2 关键发现 ★ HIGH (C3)

**ch04 §4.4 单 `## ` section = 9,598 cl100k tokens, 超 OpenAI text-embedding-3-small 的 8191 token 上限** ★.

这正是 chunker_feasibility §4 估计的 "5 chunks 每个 ~26KB / 6.5K token (压线 8K embedding 限). 风险大" 的实测确认. **chunker `chapters.py` size-aware 决策强制锁定**:

```python
# (锁定 by 1A.0.c) chapters chunker 三档:
def chunk_chapter(path, size_kb):
    if size_kb > 50:    # ch04 130KB, ch08 52KB
        split_by = "^### "   # ★ ch04 §4.4 = 9598 token > 8K, 必须按 ### 切, 不允许 ## 兜底
    elif size_kb > 20:  # ch08 52KB borderline, ch10 30KB, ch03 20KB
        split_by = "^## "
    else:               # ch01 11KB, ch02 18KB
        split_by = None  # 整文件 1 chunk
```

ch04 按 `^### ` 切: 38 sub-sections (`grep -c '^### ' ch04` = 38), 平均 38097 / 38 = 1003 bytes ≈ 250 cl100k token per chunk, 安全.

### 3.3 关键发现 ★ MED (char/4 估算偏差)

| chunk | cl100k / (char/4) | 偏差% | 原因 |
|-------|------------------:|------:|------|
| C1 TA Example 1 | 0.915 | -8.5% | mermaid block ASCII 字符多 token 少 (graph 节点名复合) |
| C2 MB Example 3 | 1.236 | **+23.6%** ★ | dense GFM table 短字符多 token (每 `|` `\n` 都是独立 token) |
| C3 ch04 §4.4 | 1.008 | +0.8% | 纯散文, char/4 估算最准 |
| C4 lb_part4 | 0.944 | -5.6% | codelist table |
| C5 VARIABLE_INDEX AE | 1.126 | +12.6% | 短列条目密集 |
| **平均** | — | **+4.6%** | — |
| **最大|偏差|** | — | **23.6%** | C2 (dense table) |

**chunker 实现强制锁定**: char/4 估算偏差 +23.6% > ±20% 容许带, **chunker 实现必须用 tiktoken cl100k_base 实测 token 数**, 不允许用 char/4 估算决策切分边界. char/4 仅作 magnitude 判断 (e.g., "这个 chunk 大约是 1K token 量级 vs 10K token 量级", 不用于 hard limit 判定).

### 3.4 cl100k vs o200k 对比

| chunk | cl100k | o200k | diff |
|-------|-------:|------:|-----:|
| C1 | 1,488 | 1,490 | +2 |
| C2 | 3,974 | 3,969 | -5 |
| C3 | 9,598 | 9,569 | -29 |
| C4 | 401 | 398 | -3 |
| C5 | 1,243 | 1,245 | +2 |

**结论**: cl100k 与 o200k 差 ≤ 0.3%, 完全可互换. **chunker 用 cl100k_base 即可** (是 text-embedding-3-small 的 native encoder). Claude tokenizer 内部 BPE 实测偏离 cl100k 约 ±5-10% (llm_providers §6 已记录), 同源 magnitude.

---

## 4. chunker config defaults 锁定 (1A.0.d)

下表是 1A.3 chunker writer kickoff prompt 必须遵循的 config defaults. 写代码前不允许偏离, 偏离需 critic Rule D 重审 + 用户 ack:

### 4.1 chunker config 表 (含 1A.0 sanity 锁定项)

| 文件类型 | 切分策略 | 关键 lock | 测试样本 |
|----------|---------|-----------|---------|
| `domains/*/spec.md` | regex `^### ` (变量级) | 平均 ~120 token / chunk, 安全 | top-5 域 |
| `domains/*/assumptions.md` | 顶部 Description = 1 chunk + numbered items = 1 chunk + table 不切 | DI 仅有此文件 | top-5 域 + DI |
| `domains/*/examples.md` | **domain-aware** 探测最深 heading level (H2/H3/H4) + mermaid/table split 保护 (1A.0.b 锁: 状态机, 0 嵌套) | PC H4 嵌套 (14 chunk 不是 16) | TA / PC / IS / DS / DM (含 mermaid) |
| `chapters/*.md` (size-aware ★) | **size_kb > 50 → `^### `** ★ (1A.0.c HIGH 锁) / 20-50 → `^## ` / ≤ 20 → 整文件 | C3 ch04 §4.4 = 9598 token > 8K | ch04 (38 ###) + ch01/ch08 |
| `model/*.md` | regex `^## ` | 6 文件结构规整 | sample 2 |
| `terminology/core/*_part*.md` (mixed) | 默认 `^## codelist` / 单 H2 part 文件 (13/31 实测) → 整 part 1 chunk + part_index metadata / 巨型 codelist (>6K token, lb_part2/3) → N=100 row 切片 + table_chunk_idx | lb_part1/2/3/4 全 4 case 覆盖 (1A.0.a 锁) | lb_part1/2/3/4 + general_part1/2 |
| `terminology/core/{ae,dm,...}.md` (11 单文件 codelist) | `^## codelist` | 总 42 H2 | ae/dm/disposition |
| `terminology/supplementary/*.md` | `^## codelist` (全 codelist 模式, 0 part 文件) | 188 H2 | supplementary_part1 + part6 |
| `terminology/questionnaires/*.md` | `^## codelist` (全 codelist 模式, 单 H2 文件 3 个) | 670 H2 | questionnaires_part1 + part18 + part43 |
| `VARIABLE_INDEX.md` | §一 1 chunk + §二 63 H3 各 1 chunk + §三 字母段 ~5 chunk | 1A.0.c C5 验 AE 1243 token | top-5 H3 |
| `ROUTING.md` + `INDEX.md` | **不切**, 整体注入 system prompt (~6K token base) | — | (注入测试) |

### 4.2 chunker 通用 lock (1A.0 sanity 衍生)

- **L-1** (来自 1A.0.b): split-point 保护用**状态机** (进入 ```mermaid 跳到下一个 ``` 退出), 不用 stack/嵌套. 因为 0 嵌套.
- **L-2** (来自 1A.0.b): markdown 解析用**简单 regex GFM pipe-table**, 不用 mistletoe/markdown-it-py. 因为 0 HTML rowspan/colspan/`<table>`.
- **L-3** (来自 1A.0.c): chunker 实现的 token 计数**必须用 tiktoken cl100k_base 实测**, 不允许 char/4. (char/4 偏差最大 23.6% > 20% 容许带.)
- **L-4** (来自 1A.0.c HIGH): chapters/ size-aware **>50KB 走 `### ` 切, 不允许 `## ` 兜底**. ch04 §4.4 实测 9598 cl100k > 8191 embedding limit.
- **L-5** (来自 1A.0.a): terminology chunker 对 core/part 文件用 `H2 count == 1` 判断 part 模式 vs codelist 模式. 13/31 part 文件 H2=1 (qs_part1, lb_part1/2/3, general_part1/3/5, is_domain_part2, microbiology_part2/3, other_part3, pk_part2/4).

---

## 5. 总 chunk 数估算 (1A.0 sanity 后修正)

| 来源 | 估算 chunk 数 | 实测/锁定依据 |
|------|--------------|--------------|
| spec.md (63 域) | 2,164 | 1A.0 不涉及, 沿用 chunker_feasibility v0.2 |
| assumptions.md (64 域, DI 含) | ~460 | 同上 |
| examples.md (63 域, domain-aware) | ~500 | 1A.0.b 锁 mermaid 状态机, ~不变 |
| chapters/ (6 文件, size-aware, ch04 强制 ### 切) | **~62** ★ | ch04 38 (### 切) + ch08 ~10 (## 切) + ch10 ~10 + ch01/02/03 各 1 = ~62 (chunker_feasibility v0.2 估 90, 实测下调 ~28) |
| model/ (6 文件) | ~35 | 1A.0 不涉及 |
| terminology/ (91 文件) | **~1,014** ★ | 实测 H2 合计 1004 codelist + LB part2/3 巨型内部切片 ~10 (按 N=100 row) = ~1014 (chunker_feasibility v0.2 估 1050-1100, 实测下调) |
| VARIABLE_INDEX.md | 69 | 实测 §一 1 + 63 H3 + §三 ~5 = 69 |
| INDEX.md, ROUTING.md | 0 (整体注入) | — |
| **TOTAL** | **~4,304 chunks** ★ | chunker_feasibility v0.2 估 ~4,368, 修正 -1.5% (在 ±5% 容许内) |

**结论**: 不需要修订 chunker_feasibility v0.2 §3 总数表 (-1.5% 在容许带内). Phase 1A.5 ingest 完成后实测 chunk 数应落在 [4,100, 4,500] 区间.

---

## 6. R-13 6 项 verify 结果总表

| # | R-13 项 | 状态 | 结果 |
|---|---------|------|------|
| 1 | supplementary_part1-6 H2 数 | ✅ | 188 codelist (全 codelist 模式, 0 part 兜底) |
| 2 | qs_part*.md / general_part*.md H2 数 | ✅ | qs_part1 H2=1 (整 part 模式) / general_part1-5 mixed (1/8/1/13/1) |
| 3 | questionnaires/ 43 文件 H2 数 | ✅ | 670 codelist H2 (codelist 级切分, 非 instrument 级) |
| 4 | mermaid block 嵌套 | ✅ | 29 mermaid / 58 fence, 全 balanced, 0 嵌套 → 状态机实现 |
| 5 | 表格变体 (合并/多行/对齐) | ✅ | 0 HTML rowspan/colspan/`<table>` → GFM pipe-table 简单 regex 即可 |
| 6 | tiktoken 实测 5 chunk | ✅ | **HIGH C3 ch04 §4.4 = 9598 > 8K**, char/4 max 偏差 +23.6% → tiktoken 强制 |

---

## 7. Phase 1A.0 PASS 五条 (规则 D + 本旁枝)

1. **evidence 存在** ✅ — 本文件 + `branches/07_rag_kg/scripts/sanity_tiktoken.py` (落代码 + 实测 stdout 包含在 §3.1 表)
2. **writer 产物合规** ✅ — main session 直接 grep/Python, 无 subagent 委派; chunker config 6 项 lock + 1 总数估算微调齐备
3. **独立 reviewer subagent PASS** — Phase 1A.0 PASS 规模小 (0.3 d sanity), 按 EXECUTION_PLAN §2.1 Rule D 矩阵不强制 reviewer (此项是 1A.3 chunker writer 启动前的 main self-check 性质 sanity, Rule D 真审在 1A.3 → code-reviewer 那一步). 若用户要求, 可加 critic 二审一遍此文档. ⚠️ **deferred / 用户决定**
4. **规则 A 抽检** N/A — 本 sanity step 压缩率 < 10% (主要是 grep + tiktoken 实测), 不触发规则 A
5. **用户 Bojiang 口头 ack** — pending

## 8. Next Action

1. ⏳ 用户 ack 本 sanity 结果 + 6 项 lock + chunk 总数微调 ~4304
2. ⏳ (可选) Rule D 第三方审本文件 (critic / verifier; 短文档 ~10 min 即可)
3. ⏳ 1A.0 closure: `_progress.json` 1A.0 PASS + commit `branches/07_rag_kg/{evidence,scripts}/...`
4. ⏳ Phase 1A.1 启动 (sdtm-rag/ 仓库脚手架, 含 .env/.env.example/.gitignore R-17 + pyreadstat sanity R-20)

---

## 附录 A — sanity_tiktoken.py 输出原文 (stdout)

```
# Phase 1A.0.c tiktoken 实测 — 5 候选 chunk
# Encoders: cl100k_base (embedding-3-small native), o200k_base (gpt-4o family)
# Embedding limit (text-embedding-3-small): 8191 tokens

id                           |  lines |  bytes |  chars |  cl100k |   o200k |   char/4 估 |  cl100k - char/4 | safe?
----------------------------------------------------------------------------------------------------------------------------------
C1_TA_examples_Example1      |    113 |   6514 |   6504 |    1488 |    1490 |       1626 |             -138 | ✓ <8K
C2_MB_examples_Example3      |     91 |  12866 |  12866 |    3974 |    3969 |       3216 |             +758 | ✓ <8K
C3_ch04_section_4.4          |    463 |  38097 |  38081 |    9598 |    9569 |       9520 |              +78 | ✗ OVER 8K
C4_lb_part4_full             |     27 |   1700 |   1700 |     401 |     398 |        425 |              -24 | ✓ <8K
C5_variable_index_AE         |     59 |   4465 |   4417 |    1243 |    1245 |       1104 |             +139 | ✓ <8K

## 偏差分析 (chunker_feasibility 用 char/4 估算 vs tiktoken cl100k 实测)
  C1_TA_examples_Example1      cl100k / (char/4) = 0.915  → 偏差 -8.5%
  C2_MB_examples_Example3      cl100k / (char/4) = 1.236  → 偏差 +23.6%
  C3_ch04_section_4.4          cl100k / (char/4) = 1.008  → 偏差 +0.8%
  C4_lb_part4_full             cl100k / (char/4) = 0.944  → 偏差 -5.6%
  C5_variable_index_AE         cl100k / (char/4) = 1.126  → 偏差 +12.6%

  平均偏差: +4.6%  最大|偏差|: 23.6%
  结论: char/4 估算 WARN (>20% 偏差, 后续 chunker 实现优先用 tiktoken)
```
