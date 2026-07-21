# D2 Review — extract_examples_data.py + 09_examples_data_high.md

> 复核日期: 2026-04-19
> Reviewer: oh-my-claudecode:code-reviewer (model=opus, agent_id a8e30db898b29a64c)
> 对象:
> - 脚本: `scripts_v2/extract_examples_data.py` (545 lines)
> - 产物: `output_v2/09_examples_data_high.md` (3,112 lines, 112,697 tokens, md5 `4cf1c1c6ab167cc31a47cdda891ec50e` — 确认匹配主控声明)
> 抽样域: DM, DS, EX, PC, IS (与主控抽样 AE/PP/MB/GF/CP 不重叠)
> 已知 spec deviation (用户 ack): token 超硬 cap 50K → 112K (2.25×), 因总 RAG 容量 ~3-4M, 112K = 3.2%。**本次复核不评估 cap**。

## 结论
**PASS**

脚本代码质量高, 幂等性/源只读/确定性均可核实。产物内容审: 5 个抽样域的 Example 数量、粗体 XPT 标记、数据表列/行、`Rows N-M:` 解释行丢弃全部与源一致。一处 **观察** (见 §2 EX / §2 DM / §4), 不影响 D2 PASS。

---

## 1. 脚本代码审 (10 条)

| # | 检查项 | 结论 | 证据 (file:line) |
|---|---|---|---|
| 1 | 幂等性 (时间戳源) | **PASS** — `_iso_from_mtimes()` (403-415) 取 source `examples.md` 的 max mtime, 非 wall-clock; 两次运行对未变源产出 byte-identical | `extract_examples_data.py:67, 403-415` |
| 2 | 源只读 | **PASS** — 源路径仅 `src.read_text(encoding="utf-8")` (460) 和 `path.read_text(...)` (119); 写操作仅 `out_path.write_text()` (514), out_path 硬编码到 `OUTPUT_DIR`, 物理上无法落到 `knowledge_base/` | `extract_examples_data.py:69, 460, 496-499, 513-514` |
| 3 | 路径处理 | **PASS** — `REPO_ROOT = Path(__file__).resolve().parents[3]` (67) 正确 (scripts_v2/ → claude_projects/ → ai_platforms/ → repo root) | `extract_examples_data.py:67` |
| 4 | Tier=others 分支完整 | **PASS** — `_resolve_domains()` (486-493) 有完整 exclude-list 解析 + 反选; 输出路径分支 (497-499) 和 tier_label (428) 均覆盖; `--tier others` 纯文本/markdown 两格式均支持 | `extract_examples_data.py:486-493, 497-499, 111-162` |
| 5 | Domain-list 解析 | **PASS** — `_parse_domain_list_file()` (111-162) 支持两种格式: (a) D1 markdown 从 `## 最终清单` 或 `## Final ... List` 下首个代码块抓取 (125-149); (b) 纯文本逐行 + 逗号分隔 + `#` 注释丢弃 (152-162); 两路径都有 UPPER+digit 校验 | `extract_examples_data.py:125-162` |
| 6 | 确定性 (sorted / 保序) | **PASS** — `build_document()` 首行 `domains = sorted(set(domains))` (424); 表格行用 `_collect_table_block()` (174-189) 保序收集, 未排序 | `extract_examples_data.py:424, 174-189` |
| 7 | 数据表识别 | **PASS** — `_collect_table_block()` 要求至少 1 行 `TABLE_SEP_RE` 分隔 + run ≥ 2 行 (187), 能正确排除纯 `\|...\|` 偶发行; XPT 粗体 (`FILENAME_BOLD_RE`, 92) 匹配 `^\*\*[a-z][a-z0-9_]*\.(xpt\|csv\|sas7bdat)\*\*\s*$`, 精确 | `extract_examples_data.py:88-105, 174-189` |
| 8 | "see also"/"shared with" 识别 | **PASS** — `CROSSREF_NOTE_RE` (100-103) 明确锚定首尾 `*...*` + 关键词 "shared with"/"see also"/"combined examples", case-insensitive; 只在 preamble 循环 (258-262) 和主循环 (368-372) 命中 | `extract_examples_data.py:100-103, 258-262, 368-372` |
| 9 | 错误处理 | **PASS** — 无 examples.md 不 crash, 塞 `(no examples file)` 占位并计入 `missing[]` (455-459); hard cap 超限 `sys.exit(1)` + stderr "EXCEED_HARD_CAP" (529-534); domain-list 解析不出任何 domain → `SystemExit` with clear msg (484) | `extract_examples_data.py:455-459, 529-534, 484-485` |
| 10 | 依赖 + Docstring | **PASS** — imports: argparse/datetime/re/sys/pathlib (stdlib) + tiktoken (1 个第三方); 模块 docstring (1-54) 说明了算法/CLI/输入输出/幂等性/soft vs hard cap 三档, 含 Drops/Keeps 明细 | `extract_examples_data.py:1-63` |

**代码质量侧评**:
- `_emit_example_header_if_needed()` 内闭包 (279-286) 对 `nonlocal example_header_emitted` 处理干净, 避免空 header 的 degenerate case
- `pending_sub_header` lazy-emit 机制 (270, 322-326, 376-381) 处理 "### heading 后面跟空行再跟 table" 的合法情况, 同时在非 table 场景丢弃, 设计稳
- L388-390 degenerate case `(no data tables in source)` 是安全兜底, 没触发时不会污染输出

**代码质量微观察** (LOW, 不影响 PASS):
- `_collect_table_block()` 在 "run 但无 separator" 时返回 `([], start)` (189), 调用方 (345-360) 必须推进 `i += 1` 以免死循环 — 当前设计依赖最外层 `i += 1` fallthrough (L381), 正确但微妙。建议将 fallback 路径加 docstring 注释。

---

## 2. 产物内容审 (5 域抽样)

### DM

- 源 `knowledge_base/domains/DM/examples.md` 有 `## Example 1` 到 `## Example 7` = **7 个 Example**
- 产出 `09_examples_data_high.md:531-707` 有 `#### Example 1` 到 `#### Example 7` = **7 个** ✓ (顺序一致)
- XPT 粗体标记:
  - Example 1: `**dm.xpt**` ✓
  - Example 2: `**dm.xpt**` + `**se.xpt**` ✓
  - Example 3: `**dm.xpt**` + `**se.xpt**` ✓
  - Example 4: `**dm.xpt**` + `**suppdm.xpt**` ✓ (CRF Metadata 表也保留)
  - Example 5: `**dm.xpt**` + `**suppdm.xpt**` ✓
  - Example 6: `**dm.xpt**` + `**suppdm.xpt**` ✓
  - Example 7: `**dm.xpt**` + `**suppdm.xpt**` ✓
- 数据表列/行:
  - Ex1 dm.xpt: 源 6 行 (Row 1-6, 25 cols), 产出 6 行 25 cols ✓
  - Ex2 dm.xpt: 5 行 × 10 cols ✓; se.xpt: 11 行 × 9 cols ✓
  - Ex4 CRF Metadata: 11 行 × 14 cols ✓; dm.xpt: 3 × 6 ✓; suppdm.xpt: 5 × 11 ✓
- 首段 description ≤ 2 行: Ex2 首段源是 1 大段 (4 行), 产出保留了完整 4 行 (L550) — **观察**: 脚本的 "首段到空行为止, 截 2 行" 逻辑在源首段没有换行仅靠空行分段时, 可能超 2 行。实际上源 Ex2 首段是**单行**未换行 (DM examples.md L18 一整行), 产出 L550 也是单行, 长度一致, 未违规。同理 Ex4 首段 3 段落各 1 行 (L603), 产出 L603 只保留首段 1 行 ✓
- `**Rows N-M:**` 解释行已丢弃: Ex2 源有 `**Row 1:**` 到 `**Rows 10-11:**` 共 10 条, 产出全部丢弃 ✓; Ex4 源有 `**Rows 1, 2:**` 等 8 条, 产出丢弃 ✓
- Mermaid / CRF mock 图: Ex4, 5, 6, 7 源都有 `mermaid` fenced code block, 产出全部丢弃 ✓
- **Verdict**: **PASS**

### DS

- 源 11 个 Example (DS/examples.md `## Example 1` 到 `## Example 11`) → 产出 L710-993 11 个 `#### Example` ✓
- 顺序一致: 1,2,3,4,5,6,7,8,9,10,11 ✓
- 数据表:
  - Ex1 ds.xpt: 21 行 × 12 cols ✓
  - Ex10 包含 5 张表 (te/ta/dm/ex/se/ds), 产出全保留; 注意 dm.xpt Row 编号源是 "1" 和 "3" (无 Row 2) — 产出保持 `| 3 | XYZ | DM | XYZ-767-002 ...` ✓ (verbatim)
  - Ex11 ds.xpt: 7 行 × 12 cols (含 TAETORD 列) ✓
- XPT 粗体全部保留 (ds/ae/relrec/te/ta/dm/ex/se) ✓
- **Rows N-M:** 解释行丢弃: Ex1 源有 9 条 (`**Rows 1, 2, 6, 8, 9, 12, 13, 17, 18:**` 等), 产出全丢弃 ✓; Ex10/Ex11 同
- 首段 description ≤ 2 行: Ex1 首段 2 段 (L5-7), 产出只保留首段 1 行 (L716) ✓; Ex11 首段长 (1 句但无换行), 产出 L941 保留 ✓
- "shared with"/"see also" 注释: DS 源无此类交叉引用 (N/A)
- **Verdict**: **PASS**

### EX

- 源 EX/examples.md 开头有 cross-ref note `Note: Examples for EX and EC are shared in Section 6.1.3.3... See also [EC Examples](...)` (L3)。产出 L1087-1089 **未保留该 note**。
  - **观察** (LOW): `CROSSREF_NOTE_RE` 要求 `^\*[^*].*(shared with|see also|combined examples)[^*]*\*\s*$` (必须整行以 `*...*` 包裹的 italic)。源 L3 是裸 `Note:` 前缀不是 italic, 因此 regex 不命中。这是**符合设计**的 — 脚本只保留 italic-wrapped cross-ref, 不保留普通 Markdown `Note:` 句子。不是 defect, 但如果目标是 "EX 和 EC 共享" 的提示, 该句被丢失了。**此观察适用主控决策**。
- 源 8 个 Example → 产出 L1091-1398 `#### Example 1` 到 `#### Example 8` ✓
- Ex1 CRF (Subject ABC1001 / ABC2001): 源有 `**Subject: ABC1001**` 和 `**Subject: ABC2001**` 两个小标题 + 两张小表; 产出 L1095-1103 保留了两张表, **Subject 标题被丢弃** — 这是**符合设计** (`FILENAME_BOLD_RE` 只匹配 `\.(xpt|csv|sas7bdat)`, `**Subject: ABC1001**` 不匹配, 作为普通粗体被丢弃, table 独立保留)。对数据正确性无影响, 但失去了 "这两张表分别属于哪个 subject" 的上下文。**观察 (LOW)**
- Ex1 ec.xpt 4 行 × 18 cols, ex.xpt 3 行 × 17 cols, relrec.xpt 2 行 × 8 cols ✓
- Ex6 (最复杂): 源 EC 24 行 × 21 cols + EX 8 行 × 18 cols → 产出 L1278-1316 完整保留, 无行丢失 ✓
- Ex7 (weekly infusions): 源 EC 6 行 × 23 cols + EX 2 行 × 21 cols + VS 2 行 × 19 cols + RELREC 6 行 → 产出 L1334-1368 完整 ✓
- `**Rows N-M:**` 解释行丢弃: Ex1 源 `**Rows 1-2, 4:**` + `**Row 3:**` → 产出丢 ✓; Ex5/Ex6/Ex7/Ex8 同
- **Verdict**: **PASS** (两处观察不是 defect, 是设计边界)

### PC

- 源 PC/examples.md 开头有 italic cross-ref `*Note: PC and PP share a combined examples section...*` (L3)
  - 产出 L2286 **正确保留**: `*Note: PC and PP share a combined examples section (6.3.5.9.3 Relating PP Records to PC Records). The PC concentration data table is shown here; see also PP examples for the derived pharmacokinetic parameters and the 4 RELREC methods for relating PC to PP.*` ✓ (这句是 italic-wrapped, 命中 `CROSSREF_NOTE_RE`)
- 源只有 `## Example 1` 一个 (L7), 但有大量 `### ...` H3 子段 (`### PC-PP Relating Datasets`, `### PC-PP Relating Records`, `### Shared PC Dataset for All Examples`, `### Example 1 (All PC records used)` 到 `### Example 4`)
- 产出:
  - `#### Example 1` (L2289) 对应源 `## Example 1` ✓
  - `### Shared PC Dataset for All Examples` (L2337) 保留 ✓ (因为后面紧跟 pc.xpt data table)
  - `### PC-PP Relating Datasets` / `### PC-PP Relating Records` / `### Example 1 (All PC records used)` 等 H3 **在产出中被丢弃** — 这是**符合设计**: `pending_sub_header` lazy-emit 机制要求 H3 后面紧跟 data table 或 filename marker 才 emit (322-360)。实际上 `### PC-PP Relating Datasets` 后面先跟一大段文字再跟 relrec.xpt 表, 所以 H3 被丢弃, 但 relrec.xpt 表本身被保留 (L2330-2335)。数据完整性无损失, 但读者失去"这段 relrec 属于哪个 method" 的提示。
  - **观察 (MEDIUM)**: PC 是 28 域里唯一一个域, 其内容结构是 "1 个 ## Example + 10 个 ### sub-heading 组织的 4 大 Methods" 而不是标准的 "N 个 ## Example"。产出因此有 11 张 `**relrec.xpt**` 表 (L2330, 2368, 2377, 2408, 2429, 2472, 2479, 2495, 2508, 2530, 2540, 2569, 2584, 2618, 2640 — 共 **15 张** 实际 count) 彼此没有 `### Method A/B/C/D` 或 `### Example 1/2/3/4` 区分。阅读者只能通过表内 `| PCGRPID | DY1_DRGX |` 等 IDVAR 值推断属于哪个 Method, 语义 traceability 下降。
  - 但这**符合 D2 prompt spec**: "每个 `## Example N` 源 → `#### Example N` 产出 (数量一致, 顺序一致)" — 源只有 1 个 `## Example`, 产出有 1 个 `#### Example`, 合规。附加的 `### Shared PC Dataset` 也保留了。所以是**规则符合, 语义 traceability 损失**。
- 数据表列/行核查 (抽 Ex1 pc.xpt + Shared PC Dataset):
  - Ex1 pc.xpt: 源 32 行 × 28 cols (L23-56) → 产出 32 行 × 28 cols (L2295-2328) ✓ 逐行 md5-level 对比了 Row 1/15/32
  - Shared PC Dataset pc.xpt: 源 24 行 × 33 cols (L93-118) → 产出 24 行 × 33 cols (L2341-2366) ✓
  - Method A/B/C/D 下各 Example 的 relrec 表 row 数量对得上源 (e.g. Method D Ex1 relrec = 38 行, 产出 L2483-2520 = 38 行 ✓)
- `**pc.xpt**` / `**relrec.xpt**` 全部保留 ✓
- **Verdict**: **PASS** (with note: PC 结构是 outlier, traceability 下降是脚本通用 extract 逻辑的自然产物, 不是 bug)

### IS

- 源 11 个 Example (IS/examples.md `## Example 1` 到 `## Example 11`) → 产出 L1709-1885 `#### Example 1` 到 `#### Example 11` = 11 个 ✓
- 顺序一致 ✓
- 数据表全部保留:
  - Ex1 is.xpt: 3 行 × 23 cols ✓
  - Ex2 is.xpt: 8 行 × 23 cols ✓
  - Ex5 is.xpt: 7 行 × 22 cols (注意 cols 变化: 无 ISGRPID) ✓
  - Ex10 is.xpt: 11 行 × 22 cols ✓ (ISGRPID 混合 "1", "1a", "1b", "2", "3", "4" — 字母数字混合 verbatim 保留)
  - Ex11 is.xpt: 9 行 × 20 cols + **两张** suppis.xpt (4 行 + 1 行) ✓ 两张 suppis.xpt 都保留 (L1872-1878 和 L1881-1885)
- 粗体 XPT 标记: `**is.xpt**` (所有 11 个 Example) + `**suppis.xpt**` (Ex11 两张) 全部保留 ✓
- 首段 description ≤ 2 行: 抽查 Ex1 (源 L5 单行) → 产出 L1711 单行 ✓; Ex5 源 4 段 → 产出 L1771 仅首段 1 行 ✓; Ex8 源 4 段 → 产出 L1812 首段 2 行 (恰好截断正确) ✓
- `**Rows N-M:**` 解释行丢弃: Ex1 源 3 条, Ex2 源 4 条, Ex10 源 2 条, 全部丢弃 ✓
- 源 L123 的段落 "Thus far, all the IS tests..." 是 Example 5 和 6 之间的桥接 narrative, 产出丢弃 ✓ (符合 "drops: business-context prose" 设计)
- **Verdict**: **PASS**

---

## 3. 结构审 (09 整体)

- **首行 generated comment**: `<!-- generated by scripts_v2/extract_examples_data.py --tier high at 2026-04-15T06:20:26Z -->` ✓ 时间戳源 deterministic (source mtime max)。主控声明的 md5 `4cf1c1c6ab167cc31a47cdda891ec50e` 与本次复核测量的 md5 **完全一致**, 确认幂等性可 reproduce。
- **每域 source comment**: 28 个域全部有 `<!-- source: knowledge_base/domains/<X>/examples.md -->` ✓ (grep 计数 = 28)
- **域间 `---` 分隔**: 抽查 L708 (DM→DS 之间), L994 (DS→EG), L1085 (EG→EX), L1399 (EX→FA), L1703 (GF→IS), L2281 (MS→PC), L2696 (PC→PP) 全部正确 ✓
- **28 域全覆盖**:
  - Source list 28 个: AE, BE, BS, CE, CM, CP, DD, DM, DS, EG, EX, FA, GF, IS, LB, MB, MH, MI, MS, PC, PP, PR, RS, SE, SS, SU, TR, TU
  - 产出 28 个 source comment 全覆盖 ✓
  - 注意: `grep -c "^### " = 31` 含 3 个域内 H3 (`### Example 1a`, `### Example 1b`, `### Shared PC Dataset for All Examples`), 其余 28 个是 "### X — Examples" ✓
  - RS 和 SS 两个域源 `## Example` 数为 0 (无标准 `## Example N` 块, 只有 narrative + 表), 因此在 `grep -c "^#### Example"` 按域统计里为 0 — 这**符合脚本 degenerate 兜底**: 如果无可提取内容, 产出 "(no data tables in source)" 占位。实际 RS/SS 有内嵌表格, 所以 `extract_domain()` 仍会保留, 只是没有 `#### Example` 标题。此行为**可接受**但建议日后增强。

### Top-level H3 (域 header) 匹配

```
### AE — Examples, ### BE — Examples, ### BS — Examples, ### CE — Examples,
### CM — Examples, ### CP — Examples, ### DD — Examples, ### DM — Examples,
### DS — Examples, ### EG — Examples, ### EX — Examples, ### FA — Examples,
### GF — Examples, ### IS — Examples, ### LB — Examples, ### MB — Examples,
### MH — Examples, ### MI — Examples, ### MS — Examples, ### PC — Examples,
### PP — Examples, ### PR — Examples, ### RS — Examples, ### SE — Examples,
### SS — Examples, ### SU — Examples, ### TR — Examples, ### TU — Examples
```
28 / 28 ✓

---

## 4. 关键发现

1. **脚本整体质量高**。幂等性 (source mtime) 、源只读 (物理路径隔离) 、确定性 (sorted domains) 三项 non-functional 需求全部达标。10 项 code 审 cleared, 0 CRITICAL / 0 HIGH / 0 MEDIUM defects; 仅 1 LOW 微观察 (`_collect_table_block` fallback 路径靠外层 `i+=1` 推进, 建议加 docstring)。

2. **内容保真度高**。5 抽样域 (DM/DS/EX/PC/IS) Example 数、顺序、XPT 粗体、数据表 (含 cols × rows verbatim 复制) 全部一致; `**Rows N-M:**` 解释行丢弃行为符合设计; Mermaid / CRF mock narrative 正确被 fenced-code 规则清除。

3. **三处观察, 皆非 defect**:
   - **(EX 观察, LOW)**: 源 EX/examples.md L3 的 "Note: Examples for EX and EC are shared..." 不是 italic-wrapped, 因此不命中 `CROSSREF_NOTE_RE`, 未在产出中保留。此交叉引用上下文丢失, 但脚本行为符合设计 (只保留 italic notes)。建议: 主控是否需要把这种跨域共享提示单独抓一遍 (E1 可参考)。
   - **(EX 观察, LOW)**: Ex1 CRF 里的 `**Subject: ABC1001**` / `**Subject: ABC2001**` 小标题被丢弃 (因为 `FILENAME_BOLD_RE` 只匹配 `.xpt`/`.csv`/`.sas7bdat`), 导致两张小表失去 "属于哪个 subject" 上下文。数据本身 (start/end date) 无损失。此为脚本通用 bold-filter 的可接受副作用。
   - **(PC 观察, MEDIUM 但可接受)**: PC 源结构是 "1 个 `## Example 1` + 4 Methods × 4 Examples 的 `###` 子层级", 脚本将 `### Method A/B/C/D` 和 `### Example 1/2/3/4` 子标题 (因后跟 narrative+table, H3 → table 之间的 narrative 触发 pending_sub_header 清空) 丢弃, 产出得到 15 张连续 `**relrec.xpt**` 表但无 Method/Example 分层。语义 traceability 下降但数据完整。阅读者需从表 IDVAR 值 (PCGRPID/PPSEQ/等) 推断归属。**不影响 D2 PASS**, 但 RAG 检索时 PC 可能因此降权; 建议 PP 检查时注意类似情况。

4. **结构 100% 合规**。28 域全覆盖, 每域 source comment + H3 domain header + `---` 分隔 齐全; 首行 generated comment 时间戳可 reproduce (md5 复测 `4cf1c1c6ab167cc31a47cdda891ec50e` = 主控声明)。

---

## 5. 下一步建议

- **PASS → 主控可继续 D3** (`build_v2_stage.py --stage v2.2`, 把 09_examples_data_high.md 并入 stage v2.2 aggregation)
- 上述 3 处 "观察" 建议记入 `V2_SESSION_STARTER.md` 或 `followup_plan.md` 的 tech debt / future enhancement 清单, 但**不 block D3**:
  1. (E1 增强) `CROSSREF_NOTE_RE` 增加裸 `Note: ... shared with ...` 前缀模式, 覆盖非 italic 跨域引用 (EX 场景)
  2. (E1 增强) `FILENAME_BOLD_RE` 可选扩展到 `**Subject: ...**` 这类 "cell context label", 以保留小表的归属上下文
  3. (PC/PP 特殊) PC 作为 outlier (单 `## Example` + 多层 `###` Method), 如果 RAG 检索表现下降, 考虑为 PC/PP 写一个 dedicated extractor 分支, 把 `### Method A` 标签提为可检索 anchor
- **无需重跑脚本**。幂等已验证 (md5 对账), 产物 byte-identical reproducible。
- **无需修改脚本**。10 项代码审全部 PASS, 唯一 LOW 观察 (docstring 微完善) 可与 E1 一同处理。

---

**最终结论: D2 PASS**

Reviewer 已独立 session 完成 (规则 D 满足), 未与 executor / 主控上下文重叠。评审基于 cat 出的脚本代码全量 + 5 域源 examples.md 全量 + 产物对应 5 域段落全量, 无幻觉。
