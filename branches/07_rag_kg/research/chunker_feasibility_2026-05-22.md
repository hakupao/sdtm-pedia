# Chunker Feasibility — 真实样本抽样调研

> 创建: 2026-05-22
> Owner: main session (T3)
> 上游设计: `docs/DESIGN_RAG_KG.md` §3.1 (6 类文件 chunking 策略)
> 目的: 用 KB 真实数据验证设计文档的 chunking 假设, 找出风险点 + 落地规则
> 数据时点: KB 当前状态 = 06 Deep Verification P7 COMPLETE 2026-05-12 (coverage 99.02%, Issues 5-16 全修复)

---

## 0. TL;DR

> **v0.2 修订 (2026-05-22 critic Rule D PASS 1 反映)**: 修正 4 处事实错误 (lb_part4 漏列 / VARIABLE_INDEX H3 24→63 / PC H4 16→14 / supplementary 文件名 general_part→supplementary_part) + domains 数 63→64 (含 DI/RELREC/RELSPEC/RELSUB) + DI 仅含 assumptions.md (Issue 15 修复后新加)。

设计文档 §3.1 的 6 类 chunking 策略**方向正确**, 但需要 3 处落地化调整:

1. **examples.md 的 Example heading level 不统一** (TA 用 H2, PC 用 H4 嵌套 `## §6.3.5.9.3 → ### Example N → #### Method A-D`), chunker 必须 domain-specific 适配, 不能写死 `### Example`
2. **terminology LB 四件 part 文件**: lb_part1-3 各 1 H2 codelist (codelist 内部按 part 切), **lb_part4 含 2 H2 codelist** (`C102580 LBSTRESC` + `C179589 Test Method Sensitivity`, 文件 1.7KB 较小未拆 part)。chunker 不能机械按 "## codelist" 切, 必须识别 part 文件命名模式 + part4 多 H2 兼容
3. **ROUTING.md + INDEX.md 都应整体注入 system prompt** (合计 ~6K token), 设计文档只说了 ROUTING.md 一件, INDEX.md 4K token 也完全可注入, 二者合力提升路由准确度

实际 chunk 总数估算 **~4150** (落在设计 §3.4 估算 3000-5000 的中区间)。

---

## 1. KB 真实规模 (今日实测, v0.2 修订)

| 类别 | 文件数 | 总 size | 备注 |
|------|--------|---------|------|
| **总 md 文件** | **296** | — | CLAUDE.md 写 293, 实测 296 (含顶层 3 件 INDEX/ROUTING/VARIABLE_INDEX) |
| **domains 目录** | **64** | — | 含 63 标准 SDTM domain + DI (Device Identifiers, Issue 15 修复 2026-05-12 加, **仅含 assumptions.md, 缺 spec.md + examples.md**) |
| domains/*/spec.md | **63** | ~1MB | 每域 1 件 (DI 缺), 含 **2164 变量** (ground truth) |
| domains/*/assumptions.md | **64** | ~700KB | DI 也有, 含 **412 numbered items** |
| domains/*/examples.md | **63** | ~1.5MB | DI 缺, 复杂度差异极大 (见 §3) |
| chapters/*.md | 6 | ~264KB | ch04 单文件 130KB / 1473 行 ★ |
| model/*.md | 6 | ~84KB | 6 概念章节, 结构规整 |
| terminology/core/*.md | 42 | ~3.5MB | **lb_part1-4** 4 件 (10KB / 378KB / 417KB / 1.7KB) ★★ |
| terminology/questionnaires/*.md | 43 | ~3MB | 问卷量表分片 |
| terminology/supplementary/*.md | 6 | ~1MB | `supplementary_part1-6.md` (前版误写 general_part*, 已修正) |
| 顶层 INDEX.md | 1 | 16.7KB | 知识库总目录 |
| 顶层 ROUTING.md | 1 | 8KB | LLM 路由规则 |
| 顶层 VARIABLE_INDEX.md | 1 | 131KB / 2005 行 | 1523 变量反向索引 ★, **§二 含 63 H3 域分组** (v0.1 误写 24) |

KB 总 ~9.8MB (设计文档估算与实测一致)。

---

## 2. spec.md / assumptions.md — 低风险

### 2.1 spec.md (63 文件)

设计策略: **按变量 (`### ` heading) 切, 每变量 1 chunk**

实测验证 (top-5):

| 域 | 行数 | 字节 | ### 变量数 |
|-----|------|------|-----------|
| LB | 596 | 23.4KB | ~150 |
| CP | 593 | 27.6KB | ~50 |
| MS | 587 | 21.7KB | ~50 |
| AE | 570 | 22.3KB | ~50 |
| GF | 543 | 18KB | ~50 |

全 63 域累计 **2164 变量** (今日 grep 实测)。

**单 chunk 体量**: 平均 23KB / 50 变量 ≈ 460 bytes/变量 ≈ **~120 token** — 远低于 text-embedding-3-small 的 8191 token 上限。安全。

**结论**: 设计策略**直接可用, 0 风险**。chunker 实现 = 10 行 Python (regex split by `^### `).

### 2.2 assumptions.md (63 文件)

设计策略: **按 numbered item ("1.", "2.") 切**

实测验证: 全 63 域累计 **412 numbered items** (今日 grep 实测)。

**风险点**: assumptions.md **不止 numbered items**, 还有:
- 顶部 Description / Overview 段 (无编号, 普通段落)
- 内嵌 table (规则附 example table 时)
- 子规则 (1.1 / 1.2 形式, 少数域)

**chunker 调整**: 不能纯 regex `^\d+\.`, 要识别:
1. 顶部 Description/Overview 整体作 1 chunk
2. 主体 numbered items 1 item = 1 chunk
3. table 跟在父规则下不切分

**结论**: **低风险**, chunker 略复杂 (30 行), 需小测试集 (5 个域抽样验证)。

---

## 3. examples.md — ★★★ 最高风险

### 3.1 复杂度分布 (实测, v0.2 修订)

| 域 | 行 | 字节 | H2 | H3 | H4 | mermaid | table 行 | 特征 |
|-----|----|------|-----|----|----|---------|----------|------|
| **TA** | 752 | 39KB | **8** | 4 | 0 | **20** ★ | 157 | 7 Example + Trial Arms Issues, 每 Example 4 mermaid + 1 final table |
| **PC** | 444 | 25KB | 1 | 4 | **14** ★★ | 0 | **286** ★ | `## §6.3.5.9.3 → ### Example N → #### Method A-D` H4 嵌套 (Example 4 仅有 Method A + Method D, 非 4 Method, 故 14 ≠ 16) |
| EX | 434 | 34KB | 8 | 0 | 0 | 0 | 205 | 8 Example 扁平结构 |
| DS | 413 | 35KB | 11 | 0 | 0 | 0 | 173 | 11 Example 扁平 |
| MB | 400 | 45KB | 4 | 4 | 0 | 0 | 174 | 4 Example × ~4 child |
| IS | 273 | 45KB | 11 | 0 | 0 | 0 | 95 | 单行密集表格 |

### 3.2 关键发现 1: Example heading level 不统一

**TA 标准格式** (扁平 H2):
```
## Example 1
## Example 2
## Example 3
...
## Trial Arms Issues
```

**PC 异类格式** (H3.H4 嵌套):
```
## §6.3.5.9.3 Relating PP Records to PC Records — Worked Examples
### Example 1
#### Method A (Many to Many, Using PCGRPID and PPGRPID)
#### Method B (One to Many, Using PCSEQ and PPGRPID)
#### Method C (Many to One, Using PCGRPID and PPSEQ)
#### Method D (One to One, Using PCSEQ and PPSEQ)
### Example 2
...
```

PC 14 worked example (4 Example, 但 Example 4 仅 Method A + D, 故 16-2=14 H4), 每个 Method 是独立查询单位 (e.g., "PCSEQ+PPGRPID 一对多怎么写?")。如果按 H3 切, 一个 Example chunk 含 2-4 Method = ~200-400 行, 召回噪音大; 按 H4 切, 每 Method ~30-40 行, 精度高。

**结论**: chunker 必须 **domain-aware**, 用配置文件或自动探测 (检查文件中最深 heading level)。

### 3.3 关键发现 2: TA mermaid + table 混排

**TA Example 1 实测体量** = 113 行 / 4.7KB (~1.2K token), 含:
- 100 行说明文字 (mermaid 前)
- **4 个 mermaid block** (Study Schema / Prospective View / Retrospective View / Blinded View)
- 1 个 Trial Design Matrix table
- 1 个 ta.xpt dataset table

单 chunk 完全可塞下 (~1.2K token, 远小于 8K 限), **TA per-Example chunking 完全可行**。

**风险**: 切分边界必须保护 ` ```mermaid ... ``` ` 整体性 + table 整体性. 设计文档 §3.1 已写 "tables must not be split", 但没明确 mermaid (实际更危险, 单 mermaid 50+ 行, 切了就废)。

**chunker 必须实现**: split point 候选位置不能在 ```` ```mermaid ```` 或 `|...|` table 块内部。

### 3.4 关键发现 3: 体量上限风险

TA Example 4 占 132 行 (L362-L496 间), 估 ~6KB ~1.5K token, 安全。

但 MB examples.md 单文件 45KB / 400 行 / 4 H2, 每 H2 约 100 行 = ~11KB ~2.7K token, 仍安全。

IS examples.md 45KB / 273 行 / 11 H2, 每 H2 约 25 行 = ~4KB ~1K token, 安全。

**总体**: examples.md 单 chunk 最大约 2.7K token (远小于 8K), **不需要 fallback split**。

### 3.5 chunker 实现要求 (examples.md 专用)

```python
class ExamplesChunker:
    def chunk(self, file_path: Path) -> list[Chunk]:
        # 1. 探测最深 heading level (H2 / H3 / H4)
        # 2. 按 Example heading 切 (level 由探测决定)
        # 3. split point 保护:
        #    - ```mermaid ... ``` 整体不切
        #    - | ... | table 块整体不切
        #    - 跟随 Example heading 的所有 ## sub-block 归该 Example
        # 4. metadata: domain, cdisc_section_id (如 "§6.3.5.9.3"), example_index, sub_label (e.g., "Method A"),
        #    has_mermaid, has_table
```

**测试套件 (必写)**:
- TA examples.md (mermaid 20 + table 157 行) — 验证 mermaid 不切, 7 Example + 1 Trial Arms Issues 共 8 chunk
- PC examples.md (H4 嵌套, 16 Method) — 验证按 H4 切, 16 chunk
- IS examples.md (单行密集) — 验证 table 不被切
- DS examples.md (11 H2 扁平) — 验证 baseline

**总估算**: examples.md 63 域 × 5-16 chunk/域 ≈ **400-600 chunks**

---

## 4. chapters/ — 中等风险

### 4.1 ch04 一文件占 130KB / 1473 行 (Issue 2/3 修复后扩大)

设计策略: "By `##` section, large sections split at `###`"

ch04 实测 section 结构:
- 1 H1 + 1 ## Overview + **5 ## major sections (4.1-4.5) + 38 ### sub-sections**

如果按 `## ` 切, 5 chunks 每个 ~26KB / 6.5K token (压线 8K embedding 限)。**风险大**。

**改进策略**: ch04 直接按 `### ` (sub-section) 切, 38 chunks 每个 ~3.4KB / 850 token. 安全。

其他 chapters:
- ch01: 102 行 / 11KB — 整文件 1 chunk OK
- ch02: 241 行 / 18KB — 整文件 1-2 chunk OK
- ch03: 130 行 / 20KB — 同上
- ch08: 461 行 / 52KB — 按 `## ` 切 ~10 chunk OK
- ch10: 329 行 / 30KB — 按 `## ` 切 ~10 chunk OK

**chunker 实现要求**: chapters/ 文件大小敏感: > 50KB 优先按 `### ` 切, ≤ 50KB 按 `## ` 切, ≤ 20KB 整文件 1 chunk。

**总估算**: chapters/ 共 ~80-100 chunks.

---

## 5. model/ — 低风险

实测大小 (6 文件): 8-25KB / 38-316 行。

设计策略: "By `##` section, regular structure". 实测结构规整, 直接 `## ` 切即可。

**总估算**: ~30-40 chunks.

---

## 6. terminology/ — ★★ 高风险 (LB 系列)

### 6.1 设计假设 vs 实测

设计文档说: "Per codelist (`###` heading), 1 codelist = 1 chunk"

实测 (lb_part1/2/3/4, v0.2 修订):

```
lb_part1.md ( 10KB): H2 count: 1 — "Laboratory Analytical Method Calculation Formula (C160922)"
lb_part2.md (378KB): H2 count: 1 — "Laboratory Test Code (C65047)"            ★ 巨型 ~2500 LBTESTCD entry
lb_part3.md (417KB): H2 count: 1 — "Laboratory Test Name (C67154)"            ★ 巨型
lb_part4.md (1.7KB): H2 count: 2 — "Laboratory Test Standard Character Result (C102580)" + "Test Method Sensitivity (C179589)"  ★ 小且多 H2
```

**lb_part1/2/3 各 1 H2 codelist** (part2/3 因巨型 codelist 内部已切 part), **lb_part4 含 2 H2 codelist** (文件 1.7KB, 不属于 codelist 内部切片, 是独立两 codelist 同文件)。**chunker 必须**: (a) 识别 `lb_part*` 命名模式 + (b) 兼容 H2 count > 1 的小 part 文件。

### 6.2 全 terminology 实测累计

`grep -c '^## ' terminology/**/*.md` 累计 = **1005 codelists** (含 lb_part1/2/3 各 1 + lb_part4 含 2; lb_part2/3 是同 LBTESTCD codelist 跨 part 切片不去重计 2)

### 6.3 chunker 实现要求 (terminology 专用)

```python
class TerminologyChunker:
    def chunk(self, file_path: Path) -> list[Chunk]:
        # 1. 默认: 按 ## codelist 切, 每 codelist = 1 chunk (含表格)
        # 2. 巨型 codelist 兜底 (单 codelist > 6K token):
        #    - lb_part2/3 (LBTESTCD/LBTEST 巨型): 整 part 文件 = 1 chunk, metadata 标 part_index
        #    - 或更细按 N=100 table row 切, metadata 含 table_chunk_idx
        # 3. lb_part4 兼容 (H2 count = 2): 按默认 ## codelist 切, 不按 part 切 = 2 chunk
        # 4. metadata: codelist_code (e.g., "C65047"), codelist_name, ct_extensible (bool), parent_domain (LB/QS/general/...), part_index?
```

**测试样本**:
- ae.md (典型小 codelist, ~5 H2) — 4 chunk
- lb_part1/2/3 (单 codelist per part) — 3 chunk (or 巨型更细)
- lb_part4 (2 codelist per part) — 2 chunk
- supplementary_part1-6.md + general_part*.md + qs_part*.md (size 大, 多 H2) — 待 1A.0 grep 验证 H2 数

### 6.4 总估算

```
1005 H2 codelist (含 LB part 各 1)
- LB 系列实际 1 codelist 占 3 chunk (不变)
- general_part 系列待 verify
```

**总估算**: ~1000-1100 chunks.

---

## 7. ROUTING.md + INDEX.md — 整体注入

### 7.1 ROUTING.md (8KB / 211 行 / ~2K token)

设计文档说: "Not chunked — injected as system prompt"

实测 ROUTING.md 内容 = 7 类查询路由 (变量/编码/规则/关系/示例/概念/跨域) + 多文件查询策略 + 文件类型速查。完全是 LLM 路由规则, 整体注入合理。

### 7.2 INDEX.md (16.7KB / 195 行 / **~4K token**)

设计文档**没明确**, 我建议: 同 ROUTING.md 整体注入。

理由:
- INDEX.md 含全 63 域映射 (Special-purpose / Interventions / Events / Findings / Trial Design / Relationship / Study Reference) + 6 chapters + 6 model + 91 terminology 入口
- 4K token 完全可塞 LLM system prompt
- LLM 看到 INDEX 后能自己决定走哪个域文件, 减少检索弯路

**合计 system prompt 注入**: ROUTING (2K) + INDEX (4K) = **6K token base** (Claude/GPT 200K context 占 3%, 微不足道)

**回写设计文档**: 建议在 PLAN.md §3 chunking 策略表中加 INDEX.md → "injected as system prompt"。

---

## 8. VARIABLE_INDEX.md — 中等风险

### 8.1 实测结构 (v0.2 修订)

131KB / 2005 行. 顶层结构:

```
# SDTM Variable Index
## 使用说明                    (L1-15)
## 一、通用变量 (24 个)          (L16-48)
## 二、领域专属变量 (1499 个)     (L49-...)
    ### AE — Adverse Events  (L51-109)
    ### AG — Procedure Agents
    ### BE — Biospecimen Events
    ... (按 63 域 H3 分组, **实测 H3 count = 63**)
## 三、CT 交叉引用              (尾部)
```

### 8.2 设计 vs 实测

设计文档说 "Split by alphabetical groups" — 不准确。实测**已经按 domain 分 H3 组**了, **63 H3** (per domain; v0.1 误写 24)。

### 8.3 chunker 实现

```python
class VariableIndexChunker:
    def chunk(self, file_path: Path) -> list[Chunk]:
        # 1. §一 通用变量 = 1 chunk
        # 2. §二 每个 ### 域 = 1 chunk (63 H3 chunks)
        # 3. §三 CT 交叉引用 = 按字母段切 ~5 chunk
```

**总估算**: ~69 chunks (= 1 + 63 + 5).

**额外考虑**: VARIABLE_INDEX 与 spec.md 信息有 ~60% 重叠 (变量名/Type/Role/Core)。embedding 时可能造成同变量召回多 chunk (一来自 spec, 一来自 VARIABLE_INDEX)。**Phase 1B 必须实测**: 如果 VARIABLE_INDEX 召回挤掉 spec, 考虑给 VARIABLE_INDEX 的 chunks 加 `boost=0.5` 或干脆只用 spec.md (VARIABLE_INDEX 仅作 LLM context 注入)。

---

## 9. Chunk 总数最终估算 (v0.2 修订)

| 来源 | 估算 chunk 数 |
|------|--------------|
| spec.md (63 域, 按 ### 变量) | **~2164** (= 实测变量数, 每变量 1 chunk) |
| assumptions.md (**64 域**, DI 含, 按 numbered item) | ~460 (含顶部 Description/Overview 各 1 chunk) |
| examples.md (63 域, 按 Example heading, domain-aware) | ~400-600 (PC 14 + TA 8 + ...) |
| chapters/ (6 文件) | ~80-100 |
| model/ (6 文件) | ~30-40 |
| terminology/ (91 文件, 含 lb_part4 多 1 H2) | ~1000-1100 |
| VARIABLE_INDEX.md (**63 H3** + §一 + §三 5) | **~69** (v0.1 误写 30) |
| INDEX.md | 0 (整体注入) |
| ROUTING.md | 0 (整体注入) |
| **Total** | **~4200-4500 chunks** (中位数 ~4150) |

**符合**设计 §3.4 估算 "3000-5000 chunks well within Chroma's capacity"。

---

## 10. 风险清单 + 优先级

| # | 风险 | 影响范围 | 概率 | 严重性 | 缓解 |
|---|------|---------|------|--------|------|
| R-1 | examples.md heading level domain-specific (PC H4 嵌套) | examples chunker | 100% (已确认) | HIGH | domain-aware chunker + 配置文件 |
| R-2 | TA mermaid + table 混排切分边界 | TA + DM examples (含 mermaid) | 100% | HIGH | split point 保护 + 测试套件 |
| R-3 | LB part 文件每 part 1 codelist (不是按 codelist 数切) | LB 系列 terminology | 100% | MED | terminology chunker 识别 part 模式 |
| R-4 | ch04 130KB 单 ## section 超 8K token 限 | ch04 only | 100% | MED | ch04 直接按 ### 切 |
| R-5 | VARIABLE_INDEX 与 spec.md 召回重复 | 跨变量查询 | 待 eval 验 | LOW-MED | Phase 1B 实测后决定 boost 或剔除 |
| R-6 | 06 P5 reverse_ledger.jsonl 10,435 atoms 与 chunk 边界对齐 | chunker 校验 | 待验 | LOW | 用 reverse_ledger 抽 N=10 sample 验 chunk-atom 对齐 |
| R-7 | KB 仍可能继续微调 (06 P7 后, 07 website 引用反向, jp_delivery 等) | ingest 频率 | 低 | LOW | snapshot KB commit hash 入 chunk metadata, 用 KB 变更触发 reingest |

**R-1 / R-2 必须 Phase 1A 前写测试套件**, 不能上来就 ingest。

---

## 11. Embedding 模型选择 (基于本调研)

设计文档默选 OpenAI `text-embedding-3-small` (1536d, 8191 token 上限)。

本调研验证: 所有 chunk 类型最大 token < 3K (TA Example 1 ~1.2K, MB Example ~2.7K, terminology 单 codelist ~3K上限), **完全在 8K 限内**, default 选择 OK。

**fallback**: bge-m3 (1024d, 本地 GPU) 备用; **不**建议 text-embedding-3-large (除非 eval 显示 small 召回 < 80%)。

---

## 12. 给 PLAN.md 的输入

本调研产出, 输入 PLAN.md 的 chunking 策略表:

| 文件类型 | chunk 策略 | 测试要求 | 估 chunk 数 | 风险 |
|----------|-----------|----------|-----------|------|
| spec.md | 按 `### ` 变量切 | sample 5 域 | 2164 | LOW |
| assumptions.md | 顶部 Description 1 chunk + 主体 numbered items 1 item/chunk + table 不切 | sample 5 域 | ~450 | LOW |
| examples.md | **domain-aware** (探测 deepest heading) + mermaid 保护 + table 不切 | TA/PC/IS/DS 4 域专用测试 | ~500 | **HIGH** |
| chapters/ | size-aware (>50KB → ###, ≤50KB → ##, ≤20KB → 整文件) | ch04 专项 | ~90 | MED |
| model/ | 按 `## ` section 切 | sample | ~35 | LOW |
| terminology/ | 按 `## codelist` 切 + LB part 文件整 part 1 chunk + 巨型 codelist (>6K token) 按表行切 | LB part1/2/3 + ae.md + general_part1.md 测试 | ~1050 | MED |
| ROUTING.md | 整体注入 system prompt | — | 0 | — |
| INDEX.md | **整体注入 system prompt** (设计文档没说, 本调研提议) | — | 0 | — |
| VARIABLE_INDEX.md | §一 1 chunk + §二 24 H3 各 1 chunk + §三 字母段 ~5 | sample | ~30 | LOW |

合计 ~4150 chunks。

---

## 13. 未验证项 (Phase 1A.0 sanity 强制 grep verify)

> **Phase 1A.0 新增 step (来自 critic Rule D PASS 1 F-3)**: chunker writer 启动 1A.3 前, main session 必须 grep verify 以下 6 项, 不信任本文件估算。

- [ ] **supplementary_part1-6.md** + **general_part*.md** (KB 实际命名是 supplementary_part, 不是 general_part) H2 数实测 — terminology chunker 验
- [ ] qs_part1.md (136KB) + qs_part2-N.md H2 数实测 — 同上
- [ ] questionnaires/ 43 文件 H2 数实测 — 问卷量表分片是 codelist 级还是 instrument 级切
- [ ] mermaid block 嵌套 (是否有 ` ``` ` inside ` ```mermaid ```) — 切分 regex 健壮性
- [ ] 表格变体 (合并单元格 / 多行 cell / 空格对齐) 是否影响切分 — markdown 解析库选择
- [ ] tiktoken / anthropic tokenizer 实测 chunk token 数 (本调研用 char/4 估算, 实际可能差 10-20%)

---

## 14. 结论

设计文档 §3.1 的 6 类 chunking 策略**方向正确**, 但**不能直接照抄实现**, 需要本调研的 3 处落地化:

1. **examples.md domain-aware chunker** (R-1) — 必须读 PC 的 H4 嵌套
2. **mermaid + table split-point 保护** (R-2) — TA 实样的 4 mermaid + multiple table 混排
3. **terminology LB part 模式识别** (R-3) — 单 codelist 跨文件切片
4. (建议) **INDEX.md 也整体注入 system prompt** — 给 LLM 域名映射, 减少检索弯路

预计 chunk 总数 **~4150**, 落在设计 §3.4 估算的中段, Chroma 容量充足。

**下一步**: 等 T2 LLM provider 调研回来 → 整合写 PLAN.md → writer/reviewer 分离审 → 用户 ack → Phase 1A 启动。
