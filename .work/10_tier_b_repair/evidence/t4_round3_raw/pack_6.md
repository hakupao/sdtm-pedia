# T4.1 第三轮补检 — 包 6 (R3_IG34_EQUIV, T126-T150) 独立审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T06:37:57Z (`date -u +%Y-%m-%dT%H:%M:%SZ`)
- 口径: `subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` + `subagent_prompts/t4/t4_supp_round3_v1.0.md` (R3_IG34_EQUIV 层)
- 看过的渲染页 (Read 带 pages): SDTMIG v3.4 p358, p424, p450
- 文本层: `ig34_p0277/0278/0279/0283/0319/0320/0330/0331/0357/0358/0396/0424/0449/0450.txt`
- 用过的命令 (均只读): `sed -n`, `grep -n` / `grep -rn` (KB 定位), `awk 'NR>=a&&NR<=b && /^\| N \|/'` (取 KB 行号), `python3 -c` 按页 / kb_file 过滤 `work/t2_pdf_typo_registry.jsonl`

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| T126 | `ig34_p0277_a027` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0277.txt:28` (Ex1 Method A r4); `knowledge_base/domains/PC/examples.md:80` | 8 格逐格一致 (4/ABC-123/PP/ABC-123-0001/PPGRPID/DY8DRGX/空/2), 实为逐字. 包内 KB 指针 (PP/examples.md) 偏, 实际在 PC/examples.md §6.3.5.9.3 Example 1 Method A. 同表 r3 的 PDF IDVAR 笔误已登记 B-PCPP T-1, 不涉本行 |
| T127 | `ig34_p0278_a004` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0278.txt:4` (Ex1 Method B r2); `PC/examples.md:92` | 逐格一致, 实为逐字 |
| T128 | `ig34_p0278_a005` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0278.txt:5` (Ex1 Method B r3); `PC/examples.md:93` | 逐格一致, 实为逐字 |
| T129 | `ig34_p0278_a046` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0278.txt:50` (Ex1 Method C r13); `PC/examples.md:139` | 13/PP/PPSEQ/11/空/2 一致, 实为逐字 |
| T130 | `ig34_p0278_a047` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0278.txt:51` (Ex1 Method C r14); `PC/examples.md:140` | 逐格一致, 实为逐字 |
| T131 | `ig34_p0279_a002` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0279.txt:3` (Ex1 Method D r8); `PC/examples.md:160` | 逐格一致, 实为逐字 |
| T132 | `ig34_p0279_a014` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0279.txt:15` (Ex1 Method D r20); `PC/examples.md:172` | 20/PC/PCSEQ/13/空/2 一致, 实为逐字 |
| T133 | `ig34_p0283_a028` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0283.txt:34` (Ex4 Method D r16); `PC/examples.md:462` | 16/PC/PCSEQ/4/空/2 一致, 实为逐字 (包内 KB 指针为 "无", 实际存在) |
| T134 | `ig34_p0319_a008` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0319.txt:10`; `knowledge_base/domains/FT/spec.md:5-12` | Name/Label/Type/CT 空/Role/Notes/Core 全一致; KB 为字段列表格式 (等价) |
| T135 | `ig34_p0319_a010` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0319.txt:13-14`; `FT/spec.md:23-30` | 标签 "Unique Subject Identifier" (PDF 折行合并), Notes 全句一致, Req |
| T136 | `ig34_p0320_a009` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0320.txt:22-23`; `FT/spec.md:221-228` | (NY) 一致 (KB 追加码值 C66742, 不改义); Role Record Qualifier; Notes 全句一致; Perm |
| T137 | `ig34_p0320_a012` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0320.txt:28`; `FT/spec.md:248-255` | 全格一致 |
| T138 | `ig34_p0330_a007` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0330.txt:25-26`; `knowledge_base/domains/RS/spec.md:131-138` | (UNIT) (KB 追加 C71620) / Variable Qualifier / "Unit for RSORRES." / Perm 一致. 包内指针 (assumptions.md:80) 偏 |
| T139 | `ig34_p0331_a016` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0331.txt:41-43`; `RS/spec.md:365-372` | CT "ISO 8601 duration or interval"、Timing、Notes 全句 (含 "-P2M") 一致, Perm |
| T140 | `ig34_p0357_a011` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0357.txt:24-27`; `knowledge_base/domains/TR/examples.md:81` | 23 格逐格一致 (TRMETHOD/TRDTC/TRDY 空, 折行合并), 实为逐字 |
| T141 | `ig34_p0358_a003` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p358 r29 / `ig34_p0358.txt:12-13`; `TR/examples.md:98` | 逐格一致 (NON-TARGET、2010-04-02、88; TRORRESU/TRSTRESN/TRSTRESU 空), 实为逐字 |
| T142 | `ig34_p0358_a006` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p358 r32 / `ig34_p0358.txt:18-19`; `TR/examples.md:101` | 逐格一致 (R1-NEW02 折行合并), 实为逐字 |
| T143 | `ig34_p0396_a020` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0396.txt:34-35`; `knowledge_base/domains/TA/examples.md:682` (§Example 4, 起于 :523) | 11 格一致, 实为逐字 |
| T144 | `ig34_p0396_a032` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0396.txt:51-52`; `TA/examples.md:694` | 11 格一致, 实为逐字 |
| T145 | `ig34_p0424_a028` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p424 / `ig34_p0424.txt:48-51`; `knowledge_base/domains/TS/assumptions.md:88` (### Use of Null Flavor 起于 :63) | 3/QS/Sufficient quantity/定义全句一致, 实为逐字 |
| T146 | `ig34_p0448_a016` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | `ig34_p0449.txt:16`; `knowledge_base/chapters/ch10_appendices.md:180` | ADJUSTMENT/ADJ, 实为逐字 (原子页号比文本层早 1 页, 内容无误) |
| T147 | `ig34_p0449_a001` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p450 / `ig34_p0450.txt:1`; `ch10_appendices.md:212` | EXTERNAL/X, 实为逐字 |
| T148 | `ig34_p0449_a007` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p450 / `ig34_p0450.txt:7`; `ch10_appendices.md:218` | GRADE/GR, 实为逐字 |
| T149 | `ig34_p0449_a013` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p450 / `ig34_p0450.txt:13`; `ch10_appendices.md:224` | INTERPRETATION/INTP, 实为逐字 |
| T150 | `ig34_p0449_a033` | R3_IG34_EQUIV | EQUIVALENT | HOLDS | 渲染页 p450 / `ig34_p0450.txt:33`; `ch10_appendices.md:244` | OUTCOME/OUT, 实为逐字 |

## 计数 (R3_IG34_EQUIV, 包 6)

| HOLDS | TYPO_AFFECTED | NOT_HOLD | UNVERIFIABLE |
|---|---|---|---|
| 25 | 0 | 0 | 0 |

其中实为逐字 19 条 (T126-T133, T140-T150); 格式等价 6 条 (T134-T139, spec 表改字段列表格式, KB 追加 C-code, 信息无丢失).

## 样本外发现的 KB 内容问题

- `knowledge_base/domains/TS/assumptions.md:84-85` (NullFlavor 表): KB 加了表头 `Rank | Code | Display Name | Definition`, PDF p424 渲染页该表无列标题行 (只有表名行 "NullFlavor Enumeration. OID: ..."). 属 KB 自拟列名, 内容不矛盾 (PDF 下文说明 column 1 为层级), 仅记录.
- 同页相邻处的 PDF 笔误均已登记, KB 按登记处理: `PC/examples.md:79` (B-PCPP T-1)、Method B r13/r26 RDOMAIN (B-PCPP T-2/T-3)、Method B 叙述与表 RELID 矛盾照录 (B-PCPP T-4)、`TR/examples.md:84` TRSTRESC -60→-50 (B-TR T-2). 无新增未登记差异.
