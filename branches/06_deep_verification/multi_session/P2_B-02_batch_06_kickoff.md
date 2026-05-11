# P2 B-02 batch 06 — Multi-Session Kickoff (新 file)

> 创建: 2026-05-04 (post `P2_B-02_batch_05` 全闭环 commit d0a411c, ch01 100% milestone)
> 父 kickoff: `multi_session/P2_B-02_kickoff.md` (umbrella §3 第 6 行)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` + 本 kickoff §3 inline 头部
> 路由词: 用户说 **"P2 bulk B-02 batch 06 开始任务"** 即触发 dispatch
> **本 batch = 新 file (ch03_submitting_data.md), 单 dispatch full-file 模式同 batch 05**

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_kickoff.md` (umbrella §5 + §6)
2. `subagent_prompts/P0_writer_md_v1.9.md` + `P0_reviewer_v1.9.md`
3. `schema/atom_schema.json` v1.2.1
4. `evidence/checkpoints/P2_B-02_batch_05_report.md` (前 batch + ch01 milestone + 4 关键决策参考)
5. 本 kickoff

---

## 2. Batch 06 任务

### 2.1 Target

- **文件**: `knowledge_base/chapters/ch03_submitting_data.md`
- **切片**: **全文 130 行** (单 dispatch, B-01 model batch 模式同 batch 05)
- **估 atoms**: ~95-110 (基于 ch04 平均 density 0.746; 130 × 0.78 ≈ 100; **but L29-93 巨表 占 ~64 atoms**, 其余 narrative + list + small structure ~35 atoms, 总 ~95-105)
- **atom_id 起始**: `md_ch03_a001` (新 file)

### 2.2 ch03 结构 prefix

```
L1:   "# SDTMIG v3.4 — Chapter 3: Submitting Data in Standard Format"  ← H1 sib=1
L3:   SENTENCE source ref (parent §3)
L5:   "## 3.1 Standard Metadata for Dataset Contents and Attributes"  ← H2 sib=1 under §3
L7:   SENTENCE narrative (parent §3.1)
L9:   "- **CDISC Notes column** — ..."  ← LIST_ITEM
L10:  "- **Core column** — ... (see Section 4.1.5, ...)"  ← LIST_ITEM w/ inline cross-ref
L12:  SENTENCE narrative (multi-clause split candidate)
L14:  "## 3.2 Using the CDISC Domain Models in Regulatory Submissions — Dataset Metadata"  ← H2 sib=2
L16:  SENTENCE long narrative
L18:  SENTENCE "Dataset definition metadata should include:"
L19:  "- Dataset filenames, descriptions, locations, structures, class, purpose, and keys"  ← LIST_ITEM
L21:  "**Note:** \"In the event...\""  ← **NOTE** (bold-Note prefix)
L23:  "### 3.2.1 Dataset-level Metadata"  ← H3 sib=1 under §3.2
L25:  "**Note:** ..."  ← NOTE parent §3.2.1
L27:  SENTENCE
L29-30: TABLE_HEADER (Dataset/Description/Class/Structure/Purpose/Keys/Location 7 cols)
L31-93: **TABLE_ROW × 63** (Dataset list — CO/DM/SE/SM/SV/AG/CM/EC/EX/ML/PR/SU/AE/BE/CE/DS/DV/HO/MH/BS/CP/CV/DA/DD/EG/FT/GF/IE/IS/LB/MB/MI/MK/MS/NV/OE/PC/PE/PP/QS/RE/RP/RS/SC/SS/TR/TU/UR/VS/FA/SR/TA/TD/TE/TI/TM/TS/TV/RELREC/RELSPEC/RELSUB/SUPP--/OI = 63 rows; SUPP-- 行含 `--` literal 在 dataset name)
L95:  SENTENCE w/ inline ref "See Section 8.4, Relating Non-standard Variable Values to a Parent Domain"
L97:  "### 3.2.1.1 Primary Keys"  ← **H3 markdown level (### NOT ####)**, semantic sub-section under §3.2.1
L99:  SENTENCE w/ inline ref "Section 3.2.1, ..."
L101: SENTENCE w/ inline ref "Section 4.1.9, Assigning Natural Keys..."
L103: "**Definitions:**"  ← SENTENCE caption (bold-only, NOT NOTE — 普通 caption 不是 carve-out)
L104: "- A **natural key** is ... (multi-sentence)"  ← LIST_ITEM (multi-sentence retained whole)
L105: "- A **surrogate key** is ... (multi-sentence)"  ← LIST_ITEM
L107: "### 3.2.1.2 CDISC Submission Value-level Metadata"  ← **H3 markdown level**
L109: SENTENCE narrative
L111: "**Example:** The Vital Signs (VS) data domain..."  ← SENTENCE bold-Example caption (NOT NOTE — 普通 example caption 同 batch 04 a902 区分: a902 `**Exception**` 是 carve-out NOTE; **Example** 是 caption SENTENCE)
L113: SENTENCE w/ URL
L115: `---`  ← **horizontal rule SKIP** (per batch 02-04 directive)
L117: "### 3.2.2 Conformance"  ← H3 markdown level
L119: SENTENCE
L121-130: 10 numbered LIST_ITEM (`1. Following ...` to `10. Conforming ...`)
```

### 2.2.5 Boundary critical (Rule A 必入 sample, 6 atoms)

- **a001** L1 HEADING h_lvl=1 sib=1 (新 file H1; parent_section `§3 [Submitting Data in Standard Format]` simplified per batch 05 D1 模式)
- **L23 H3 §3.2.1** sib=1 (首 H3 RESTART under §3.2)
- **L29-30 TABLE_HEADER** + **L31 TABLE_ROW** (首 row CO; 验证 7 cols / Hook A1 span ≤1 / byte-exact pipe-delimited)
- **L92 TABLE_ROW** "SUPP-- | Supplemental Qualifiers for [domain name] | ..." (验证 `--` literal 在 cell 内 byte-exact + `[domain name]` brackets 保留)
- **L97 H3 §3.2.1.1** + **L107 H3 §3.2.1.2** (验证 markdown-level vs semantic-numbering 决策, 见 §4 D5; sib_index 决策也是关键)
- **末原子 L130 LIST_ITEM** (numbered `10. Conforming...`, ch03 文件末)

---

## 3. Hook A4 inline (FIGURE figure_ref 校验)

每 atom_type=FIGURE 必满足: figure_ref 非 null + pattern `md_ch03_<descriptor>`.

**预期: ch03 全文 0 FIGURE** (扫源未见 mermaid block).

---

## 4. atom_type 决策 (本 batch 关键)

| Source 形态 | atom_type | 注 |
|---|---|---|
| `# SDTMIG v3.4 — Chapter 3: Submitting Data in Standard Format` (L1) | HEADING h_lvl=1 sib=1 | parent_section: 简化 `§3 [Submitting Data in Standard Format]` per batch 05 D1 模式 |
| `Source: ...` (L3) | SENTENCE | metadata 行, parent §3 |
| `## 3.1 ...` (L5) `## 3.2 ...` (L14) | HEADING h_lvl=2 sib=1/2 | parent `§3 [Submitting Data in Standard Format]` |
| `### 3.2.1 Dataset-level Metadata` (L23) | HEADING h_lvl=3 sib=1 | parent `§3.2 [Using the CDISC Domain Models...]`; sib=1 RESTART under §3.2 |
| `### 3.2.1.1 Primary Keys` (L97) `### 3.2.1.2 CDISC Submission Value-level Metadata` (L107) | HEADING h_lvl=3 sib=1/2 | **关键 D5 决策** (见下) |
| `### 3.2.2 Conformance` (L117) | HEADING h_lvl=3 sib=? | **关键 D5 决策** |
| `**Note:** ...` L21 / L25 | NOTE (bold-Note 形态, carve-out 说明) | 与 batch 02-04 一致 |
| `**Example:** The Vital Signs ...` L111 | **SENTENCE** (NOT NOTE) | 与 batch 04 a902 `**Exception**` NOTE 区分: `**Exception**` 是 carve-out NOTE, `**Example**` 是 普通 caption SENTENCE; 同 batch 03 / 04 多次 `**Example N (xx.xpt)**` 已用 SENTENCE 模式 |
| `**Definitions:**` L103 | SENTENCE caption | 同 `**Example:**` 处理 |
| `- **CDISC Notes column** — ...` `- **Core column** — ...` (L9-10) | LIST_ITEM | bullet `- ` retained + bold cell name + content |
| `- A **natural key** is ... (multi-sentence)` `- A **surrogate key** ...` (L104-105) | LIST_ITEM (multi-sentence retained whole per Hook C-7) | C-7 严守: 不截断多句 list item |
| `1. Following ... 2. Following ... ... 10. Conforming ...` (L121-130) | LIST_ITEM × 10 | 数字 prefix retained `1. ` ... `10. `; 含 inline ref ("Section 4.1.5" 等) 走 cross_refs field |
| `---` (L115) | **不 emit** | horizontal rule skip per batch 02-04 directive |
| Dataset table (L29-93, **63 rows**) | TABLE_HEADER (L29-30) + TABLE_ROW × 63 (L31-93) | C-5 hook span ≤1; pipe-delimited byte-exact 含 `--` literal (L92 SUPP--) + `[domain name]` brackets / 多 cell 含 commas in keys cell (e.g. L31 keys `STUDYID, USUBJID, IDVAR, COREF, COOTC`) |
| 长 narrative paragraph (L7/12/16/27/95/99/101/109/113/119) | SENTENCE (multi-atom 同 line_start 合法 per §C-1) | sub-line split for multi-clause |

### 关键决策 D5: §3.2.1.1 / §3.2.1.2 / §3.2.2 sib_index + parent_section

**问题**: source 用 `### 3.2.1.1` `### 3.2.1.2` `### 3.2.2` (markdown level=3), 与 §3.2.1 同 markdown level. 按 markdown 严格解释 4 个 H3 都是 §3.2 直 child (sib chain 1/2/3/4). 但语义上 §3.2.1.1/.1.2 是 §3.2.1 的 child.

**前例 (ch04)**: §4.5.1.3 用 `#### 4.5.1.3` (markdown level=4), 自然落入 §4.5.1 H3 父. ch03 不同 — 用 markdown level=3 表 .X.Y.Z.

**推荐 D5 (semantic-numbering aware, 同 §6 canonical bracketed format intent)**:
- §3.2.1.1 parent_section = `§3.2.1 [Dataset-level Metadata]` (per number prefix), sib=1 (1st child under §3.2.1)
- §3.2.1.2 parent_section = `§3.2.1 [Dataset-level Metadata]`, sib=2
- §3.2.2 parent_section = `§3.2 [Using the CDISC Domain Models...]`, sib=2 (§3.2.1=1, §3.2.2=2 under §3.2)

heading_level 字段仍按 markdown level (Hook A2) = 3 (因 source markdown 是 `###`); sibling_index 按 semantic parent.

**alternative (markdown-strict)**:
- 4 个 H3 都是 §3.2 child, sib chain: §3.2.1=1, §3.2.1.1=2, §3.2.1.2=3, §3.2.2=4. **不推荐** (失语义结构, P4b tree-build 难)

writer 选 D5 推荐 (semantic), 在 dispatch report flag 决策 + 例 atom_id (a??? L97 / a??? L107 / a??? L117) 让 reviewer 验. v1.9.1 候选 +1 codify D5 同 S-02 (numberless H3) 类 sub-pattern: "markdown-level-uniform numbered H3 semantic-parent attachment".

---

## 5. Dispatch 模板 — **FALLBACK PATH** sustained

派 `general-purpose` 单 dispatch.

1. Schema-first 头部 (12-key + 9-enum + Hook A4 + Hook C-8)
2. parent_section canonical bracketed format
3. 本 batch 特定:
   - file: `knowledge_base/chapters/ch03_submitting_data.md`
   - line range: **1-130 (全文)** 单 dispatch
   - atom_id prefix: `md_ch03_a` 从 `a001`
   - batch_id: `P2_B-02_batch_06`
   - 输出: `evidence/checkpoints/P2_B-02_batch_06_md_atoms.jsonl`
   - extracted_by.subagent_type: `"general-purpose"` (FALLBACK)
4. 22 hooks self-validate
5. **§4 atom_type 决策 + D5 §3.2.1.1/.1.2/§3.2.2 sib semantic 推荐 全粘**

---

## 6. Rule A 跟进 — **FALLBACK PATH**

派 `pr-review-toolkit:code-reviewer`. 10-atom 分层独审 (6 boundary + 4 stratified per §2.2.5).

---

## 7. PASS 后 append + checkpoint

PASS 后:
- root append (1924 → ~2110)
- audit_matrix.md + ch03 milestone block
- trace.jsonl batch_complete + phase_report
- _progress.json batches_done=6 / files_complete += ch03 / next_batch=batch 07 (ch02)
- 写 batch_06_report.md (含 D5 决策详细)

---

*Kickoff written 2026-05-04 (post batch 05 + ch01 milestone). 关键挑战: 63-row 巨表 + D5 markdown-level-uniform numbered H3 决策.*
