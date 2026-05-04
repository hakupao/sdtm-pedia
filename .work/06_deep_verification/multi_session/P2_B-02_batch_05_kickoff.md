# P2 B-02 batch 05 — Multi-Session Kickoff (新 file)

> 创建: 2026-05-04 (post `P2_B-02_batch_04` 全闭环 commit 29bed43, ch04 100% milestone, schema v1.2.1 patched)
> 父 kickoff: `multi_session/P2_B-02_kickoff.md` (umbrella §3 第 5 行)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` + 本 kickoff §3 inline 头部
> 路由词: 用户说 **"P2 bulk B-02 batch 05 开始任务"** 即触发 dispatch
> **本 batch = 新 file (ch01_introduction.md), 不跨 batch continuity, atom_id 重起 a001**; 模式参考 B-01 model batch single-dispatch full-file (非 mirror batch 04 切片)

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_kickoff.md` (umbrella §5 schema-first 模板 + §6 parent_section canonical format)
2. `subagent_prompts/P0_writer_md_v1.9.md` (主体 prompt) + `P0_reviewer_v1.9.md` (Rule A 用)
3. `schema/atom_schema.json` **v1.2.1** (post batch 04 patch — atom_id `\d{3,}` 已松弛, 但 ch01 100 atoms 估不会撞 999, 仍按 3-digit 起)
4. `evidence/checkpoints/P2_B-02_batch_04_report.md` + `rule_a_P2_B-02_batch_04_summary.md` (前 batch 末态 + ch04 milestone 参考)
5. 本 kickoff (本身)

---

## 2. Batch 05 任务

### 2.1 Target

- **文件**: `knowledge_base/chapters/ch01_introduction.md`
- **切片**: **全文 102 行** (单 dispatch, 不切片; 模式同 B-01 model batch)
- **估 atoms**: ~70-80 (基于 ch04 平均 density 0.746; 102 × 0.7 ≈ 71; 但 ch01 含 3 数据表 + 24 LIST_ITEM + 多 CROSS_REF 可能略高, ~80)
- **atom_id 起始**: `md_ch01_a001` (新 file 重起, 不跨 batch continuity)

### 2.2 ch01 结构 prefix (writer 必读以定 boundary)

```
L1:   "# SDTMIG v3.4 — Chapter 1: Introduction"  ← H1 sib=1
L3:   "Source: SDTMIG v3.4, Section 1 (Pages 7-12)"  ← SENTENCE metadata (parent §1)
L5:   "## 1.1 Purpose"  ← H2 sib=1 under §1
L7-11: 3 narrative SENTENCE (parent §1.1)
L13:  "## 1.2 Organization of this Document"  ← H2 sib=2 under §1
L15-26: Section table (TABLE_HEADER L15-16 + TABLE_ROW × 10 L17-26) parent §1.2
L28:  "## 1.3 Relationship to Prior CDISC Documents"  ← H2 sib=3 under §1
L30:  SENTENCE
L32:  SENTENCE 内含 "See Section 4.3, Coding and Controlled Terminology Assumptions, ..." — **CROSS_REF or SENTENCE w/ inline ref?** 见 §4
L34:  SENTENCE "The most significant changes since SDTMIG v3.3 include:"
L36-49: 14 LIST_ITEM (changes since v3.3 bullets) parent §1.3
L51:  "### Related Implementation Guides"  ← H3 sib=1 under §1.3 (无数字编号 H3, 纯 title)
L53-57: Related IG table (TABLE_HEADER + TABLE_ROW × 3) parent `§1.3 [.../Related Implementation Guides]` (sub-section)
L59:  "## 1.4 How to Read this Implementation Guide"  ← H2 sib=4 under §1
L61:  SENTENCE
L63:  SENTENCE "Recommended reading order:"
L65-72: 8 LIST_ITEM numbered list (1. ... 8. ...) parent §1.4 — 多 inline ref ("Sections 1-3", "Appendix B", "Section 4", "Section 5", ...)
L74:  SENTENCE 内含 inline ref "SDTMIG-AP / SDTMIG-MD / SDTMIG-PGx"
L76:  "### 1.4.1 How to Read a Domain Specification"  ← H3 sib=1 under §1.4
L78:  SENTENCE
L80-88: Column descriptions table (TABLE_HEADER + TABLE_ROW × 6) parent §1.4.1; 注: 表内多 cell 含 bold `**Variable Name**` 等 — TABLE_ROW verbatim 含完整 cell 内容
L90:  "## 1.5 Known Issues"  ← H2 sib=5 under §1
L92:  "### Derived Records and the use of --DRVFL"  ← H3 sib=1 under §1.5 (无数字编号)
L94:  SENTENCE
L96:  "### Use of --LNKID and --LNKGRP"  ← H3 sib=2 under §1.5 (无数字编号)
L98:  SENTENCE 末 "This implies:"
L99-100: 2 LIST_ITEM bullet (RELTYPE rules) parent §1.5/Use of --LNKID...
L102: SENTENCE "The examples in SDTMIG v3.4 have not been systematically reviewed..." (文件末)
```

### 2.2.5 Boundary critical (Rule A 必入 sample, 6 atoms 因新 file + CROSS_REF + 多 H2/H3 transitions)

- **a001** L1 HEADING h_lvl=1 sib=1 (file 起首 H1, 验证 H1 单原子 + parent_section 自指 / null 决策)
- **L5 HEADING h_lvl=2 sib=1** §1.1 (首 H2, 验证 sib RESTART under H1)
- **L32 CROSS_REF or SENTENCE w/ inline ref** (验 atom_type 决策, 同 batch 04 a892 "See Section..." 模式)
- **L51 HEADING h_lvl=3 sib=1** under §1.3 (验证 H3 无数字编号 case + sib RESTART under new H2 parent)
- **L92 / L96 HEADING h_lvl=3 sib=1/2** under §1.5 (验证 §1.5 下 2 个无编号 H3, sib chain 续)
- **末原子 L102 SENTENCE** (file 末, 验证 ch01 全文末 boundary)

---

## 3. Hook A4 inline (FIGURE figure_ref 校验)

每 atom_type=FIGURE 必满足:
- `figure_ref` 非 null
- pattern: `md_ch01_<topic_slug>_concept_map` (canonical) 或 `md_ch01_<descriptor>` (alt)

**预期: ch01 全文 0 FIGURE** (扫源 L1-102 未见 mermaid block; 全 narrative + table + list).

---

## 4. atom_type 决策 (本 batch 关键 cases)

| Source 形态 | atom_type | 注 |
|---|---|---|
| `# SDTMIG v3.4 — Chapter 1: Introduction` (L1) | HEADING h_lvl=1 sib=1 | parent_section: 文件起首 H1, 推荐 parent_section = 自身或 null; 参考 ch04 pilot a001 H1 模式 (a001 parent='§4 [General Assumptions]' 自指 — 但 ch04 H1 文本不完全等于 parent name, 见 batch 03 report §5 表). 建议: parent_section = `§1 [Introduction]` (简化, 与 H2 chain `§1.X` 对齐) |
| `Source: SDTMIG v3.4, Section 1 (Pages 7-12)` (L3) | SENTENCE 或 NOTE | metadata 行; 推荐 SENTENCE (无 bold/italic prefix); parent_section = `§1 [Introduction]` |
| `## 1.1 Purpose` `## 1.2 Organization of this Document` `## 1.3 Relationship to Prior CDISC Documents` `## 1.4 How to Read this Implementation Guide` `## 1.5 Known Issues` (L5/13/28/59/90) | HEADING h_lvl=2 sib=1/2/3/4/5 | parent `§1 [Introduction]`; sib 1-based 续 §1 H2 chain |
| `### Related Implementation Guides` (L51, 无编号) | HEADING h_lvl=3 sib=1 | parent `§1.3 [Relationship to Prior CDISC Documents]`; sib=1 RESTART under new H2; parent_section bracketed format `§1.3 [...]` (注: 无编号 H3 不需 §1.3.X 子号, 仍归在 §1.3 下作 sib=1) |
| `### 1.4.1 How to Read a Domain Specification` (L76) | HEADING h_lvl=3 sib=1 | parent `§1.4 [How to Read this Implementation Guide]`; sib=1 RESTART under new H2 |
| `### Derived Records and the use of --DRVFL` (L92, 无编号) | HEADING h_lvl=3 sib=1 | parent `§1.5 [Known Issues]`; sib=1 RESTART |
| `### Use of --LNKID and --LNKGRP` (L96, 无编号) | HEADING h_lvl=3 sib=2 | parent `§1.5 [Known Issues]`; sib=2 续 §1.5 H3 chain |
| L32 SENTENCE 内含 `See Section 4.3, Coding and Controlled Terminology Assumptions, ...` | **SENTENCE** (推荐) **w/ cross_refs field populated** OR **CROSS_REF** | L32 是长 paragraph, 含 inline cross-ref 但非完全 cross-ref directive; **建议 SENTENCE** + cross_refs 字段填 inline ref string; 与 batch 04 a892 (L1218 short 句首 "See Section 8...") 区分: a892 是纯 cross-ref directive (CROSS_REF), L32 是 narrative + inline ref (SENTENCE w/ ref) |
| L65-72 numbered list 8 items (`1. Read the SDTM...` etc.) | LIST_ITEM | 含多 inline section refs ("Sections 1-3", "Appendix B, Glossary and Abbreviations", "Section 4, Assumptions...", etc.); cross_refs field 可填 inline ref strings (writer 自定 — fluent option: 不填 cross_refs 内嵌 verbatim) |
| L36-49 bullet list 14 items (`- Expanded the scope...` etc.) | LIST_ITEM | 全 prefix `- ` retained (Hook C-7 PASS); narrative changes-since-v3.3 list, 单句 / 多句 mix |
| L99-100 `- RELTYPE = ONE → ...` `- RELTYPE = MANY → ...` | LIST_ITEM | 顶级 `- ` bullet, parent §1.5/Use of --LNKID 子节 |
| Section table L15-26 (3 cols, 10 rows) | TABLE_HEADER + TABLE_ROW × 10 | C-5 hook span ≤1; pipe-delimited; 含 "10 \| Appendices \| ..." style |
| Related IG table L53-57 (2 cols, 3 rows) | TABLE_HEADER + TABLE_ROW × 3 | parent `§1.3 [...]` 或 `§1.3 [.../Related Implementation Guides]` (table 在 H3 §1.3.Related... 之后, 应归 H3 sub-section parent) |
| Column descriptions table L80-88 (2 cols, 6 rows) | TABLE_HEADER + TABLE_ROW × 6 | parent `§1.4.1 [How to Read a Domain Specification]`; cells 含 bold formatting (`**Variable Name**` etc.) — TABLE_ROW verbatim 含 cell 内 bold (no special handling, byte-exact pipe-delimited) |
| L74 SENTENCE 含 inline `SDTMIG-AP / SDTMIG-MD / SDTMIG-PGx` refs | SENTENCE w/ cross_refs (optional) | 同 L32 处理, inline ref 不单独 CROSS_REF |
| narrative paragraph (L7/9/11, L30, L61, L78, L94) | SENTENCE (multi-atom 同 line_start 合法 per §R-C1) | sub-line SENTENCE byte-exact substring; multi-clause 段 split |

### 关键决策 reminders for writer

1. **L1 H1 parent_section**: 推荐 `§1 [Introduction]` (简化 + 与 §1.X H2 chain 一致); 不用文件 H1 全文 "SDTMIG v3.4 — Chapter 1: Introduction" 作 parent (太长, 与 H2 不对齐)
2. **L51 / L92 / L96 无编号 H3**: parent_section bracketed format 走父 H2 (§1.3 / §1.5 / §1.5), sib 在父 H2 下顺序 (§1.3 下 sib=1, §1.5 下 sib=1/2)
3. **L32 vs L1218 (batch 04 a892) CROSS_REF 分界**: 
   - L1218 = 句首 "See Section X..." 短句 = CROSS_REF (atom 主体即 cross-ref)
   - L32 = 长 narrative + inline "See Section X" = SENTENCE w/ optional cross_refs field
   - 写 writer 注意: L66-72 numbered list items 也是 LIST_ITEM 内含 inline ref, 不单独 CROSS_REF

---

## 5. Dispatch 模板 — **FALLBACK PATH** sustained

派 `general-purpose` 单 dispatch (FALLBACK for `oh-my-claudecode:executor`, sustained from batch 03/04). Dispatch prompt 顶部必须粘:

1. **Schema-first 头部** (`P2_B-02_kickoff.md` §5 完整 12-key 表 + atom_type 9-enum + Hook A4 + Hook C-8)
2. **parent_section canonical format** (`P2_B-02_kickoff.md` §6, chapters v1.8 bracketed `§<num>.<num> [<title>]`)
3. **本 batch 特定**:
   - file: `knowledge_base/chapters/ch01_introduction.md`
   - line range: **1-102 (全文)**, 单 dispatch (B-01 model batch 模式)
   - atom_id prefix: `md_ch01_a` 从 `a001` 起 (新 file)
   - batch_id: `P2_B-02_batch_05`
   - 输出: `evidence/checkpoints/P2_B-02_batch_05_md_atoms.jsonl`
   - prompt_version: `"P0_writer_md_v1.9"`
   - extracted_by.subagent_type: `"general-purpose"` (FALLBACK)
4. **22 hooks self-validate** + **Hook A4 inline** (本 batch 0 FIGURE 预期)
5. **§4 atom_type 决策 reminders 全粘**

---

## 6. Rule A 跟进 — **FALLBACK PATH** sustained

派 `pr-review-toolkit:code-reviewer` 跑 10-atom 分层独审:

- 加载 `subagent_prompts/P0_reviewer_v1.9.md`
- 输入: `evidence/checkpoints/P2_B-02_batch_05_md_atoms.jsonl`
- 输出: `evidence/checkpoints/rule_a_P2_B-02_batch_05_verdicts.jsonl` + `_summary.md`
- gate ≥90% PASS
- **额外 boundary 必入 sample (6 atoms)**:
  - **a001** L1 HEADING h_lvl=1 sib=1 (新 file H1)
  - **L5 H2 §1.1** sib=1 (首 H2 RESTART under H1)
  - **L32 SENTENCE w/ inline ref** OR **CROSS_REF** (验 atom_type 决策, vs batch 04 a892 比较)
  - **L51 H3 §1.3/Related IG** sib=1 (无编号 H3 + parent_section format)
  - **L92 / L96 H3 §1.5 下 2 H3 chain** sib=1/2 (无编号 H3 sib chain)
  - **末原子 L102 SENTENCE** (ch01 文件末)
- **stratified 4 atoms 余样**: TABLE_HEADER (1 of 3 表) / TABLE_ROW (1 含 bold cells L80-88 column desc 表) / LIST_ITEM (1 numbered L65-72 含 inline ref) / NOTE 或 LIST_ITEM (1 of 14 L36-49 changes bullets)

---

## 7. PASS 后 append + checkpoint

PASS 后:
- cat `P2_B-02_batch_05_md_atoms.jsonl` → `md_atoms.jsonl` 追加
- `wc -l md_atoms.jsonl` 验证累计 (post batch 04 close = 1924; post batch 05 应 ~1994-2004)
- `audit_matrix.md` P2 Bulk 表加 batch 05 行 (含 ch01 全闭 milestone)
- `trace.jsonl` 写 batch 05 phase_report 事件
- `_progress.json` 更新 last_completed_batch + B-02.batches_done=5 + B-02.atoms_so_far + files_complete += "ch01" + next_batch=batch 06 (ch03)
- 写 `evidence/checkpoints/P2_B-02_batch_05_report.md`

---

## 8. 失败处理 + Recovery hint

若 dispatch 或 Rule A FAIL:
- 写 `evidence/failures/P2_B-02_batch_05_attempt_<M>.md`
- attempt 2 调整后再派
- 连续 2 attempt FAIL → halt, 评估 v1.9.1 cut

Recovery: writer 已派但未完看 trace.jsonl 末; writer 完 reviewer 未派直接派; reviewer FAIL 走 Rule B.

---

*Kickoff written 2026-05-04 (post batch 04 + ch04 milestone). 新 file 模式 (单 dispatch full-file), atom_id 重起 a001; FALLBACK 路径 sustained.*
