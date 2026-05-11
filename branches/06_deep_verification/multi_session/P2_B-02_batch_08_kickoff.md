# P2 B-02 batch 08 — Multi-Session Kickoff (新 file, 大表批)

> 创建: 2026-05-05 (post `P2_B-02_batch_07` 全闭环 commit 51d4ece, ch02 100% milestone)
> 父 kickoff: `multi_session/P2_B-02_kickoff.md` (umbrella §3 第 8 行)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` + 本 kickoff §3 inline 头部
> 路由词: 用户说 **"P2 bulk B-02 batch 08 开始任务"** 即触发 dispatch
> **本 batch = 新 file (ch10_appendices.md), 单 dispatch full-file 模式同 batch 05/06/07**
> **L117/5表 教训**: 本 kickoff 写前已 Read source 全 (310 行) + 实数 5 表 + 12 numberless H3 + 6 HR skips, 与 source 实测对齐

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_kickoff.md` (umbrella §5 + §6)
2. `subagent_prompts/P0_writer_md_v1.9.md` + `P0_reviewer_v1.9.md`
3. `schema/atom_schema.json` v1.2.1
4. `evidence/checkpoints/P2_B-02_batch_07_report.md` (前 batch + ch02 milestone + 2 conventions validation 参考)
5. 本 kickoff

---

## 2. Batch 08 任务

### 2.1 Target

- **文件**: `knowledge_base/chapters/ch10_appendices.md`
- **切片**: **全文 310 行** (单 dispatch, 模式同 batch 05/06/07)
- **估 atoms**: **~250-275** (修正 vs 原 ~210; 因 2 个超大表: Fragment Ref 62 行 + Section-by-Section 74 行 + Glossary 40 行 = 大表 3 个共 ~176 TABLE_ROW; 加 19 HEADING + ~22 LIST_ITEM + ~30 SENTENCE + 5 TABLE_HEADER ≈ 252 atoms; density ~0.81)
- **atom_id 起始**: `md_ch10_a001` (新 file)
- **特殊**: ch10 是 appendix-style (Appendix A-F), 大量结构化 reference data

### 2.2 ch10 结构 prefix (writer 必读 — 已与 source 310 行实测对齐)

```
L1:   "# SDTMIG v3.4 — Chapter 10: Appendices"  ← H1 sib=1
L3:   "Source: ..."  ← SENTENCE
L5:   "---"  ← HR SKIP
L7:   "## Appendix A: CDISC SDS Team"  ← H2 sib=1 (无数字编号, 只 Appendix X 标识)
L9:   SENTENCE narrative
L11:  SENTENCE narrative (~70 contributors 描述)
L13:  "---"  ← HR SKIP
L15:  "## Appendix B: Glossary and Abbreviations"  ← H2 sib=2
L17:  SENTENCE w/ inline ref Section 7.1.2 + URL https://www.cdisc.org/standards/glossary
L19-20: TABLE_HEADER (Abbreviation/Full Term 2 cols)
L21-60: TABLE_ROW × 40 (ADaM/ADSL/ATC/CDASH/CDISC/CRF/CRO/CTCAE/Dataset/Define-XML/Domain/eDT/FDA/HL7/ICH/ICH E2A/ICH E2B/ICH E3/ICH E9/ISO/ISO 8601/ISO 3166/LOINC/MedDRA/NCI/NSV/PRO/SAP/SDS/SDTM/SDTMIG/SDTMIG-AP/SDTMIG-MD/SDTMIG-PGx/SEND/SNOMED/SOC/TDM/WHODRUG/XML)
L62:  "---"  ← HR SKIP
L64:  "## Appendix C: Controlled Terminology"  ← H2 sib=3
L66:  SENTENCE
L68:  "### Key Points"  ← numberless H3 sib=1 under Appendix C
L70-74: 5 LIST_ITEM (含 inline URLs)
L76:  "### Appendix C1: Supplemental Qualifiers Name Codes"  ← numberless H3 sib=2 under Appendix C
L78:  SENTENCE
L80-81: TABLE_HEADER (QNAM/QLABEL/Applicable Domains 3 cols)
L82-84: TABLE_ROW × 3 (AESOSP/AETRTEM/--REAS)
L86:  "---"  ← HR SKIP
L88:  "## Appendix D: CDISC Variable-naming Fragments"  ← H2 sib=4
L90:  SENTENCE
L92:  "### Rules for Using Fragments"  ← numberless H3 sib=1 under Appendix D
L94-96: 3 LIST_ITEM
L98:  "### Fragment Reference Table"  ← numberless H3 sib=2 under Appendix D
L100-101: TABLE_HEADER (5 cols! Keyword(s)/Fragment/<empty>/Keyword(s)/Fragment — side-by-side 2-list 表 with empty middle separator column)
L102-163: TABLE_ROW × 62 (Fragment Reference, 各 row 含 left+right 2 fragment pairs; 部分 row 末尾 empty 因 left/right 列数不等 e.g. L147 only 4 cols populated; L148-163 only right-column populated)
L164: "---"  ← HR SKIP
L166: "## Appendix E: Revision History"  ← H2 sib=5
L168: SENTENCE
L170-171: 2 LIST_ITEM (Diff file note / Public review note)
L173: "### General Changes Throughout"  ← numberless H3 sib=1 under Appendix E
L175-185: 11 LIST_ITEM (Text/examples clarified, Text updated, Values updated, ISO formats, New variables, Domain tables, Supplemental qualifier names, Assumptions providing, Numbered lists, Links, Typographical errors)
L187: "### New Domains for SDTMIG v3.4"  ← numberless H3 sib=2 under Appendix E
L189-190: TABLE_HEADER (Domain/Description 2 cols)
L191-195: TABLE_ROW × 5 (BE/BS/CP/GF/RELSPEC)
L197: "### Decommissioning of MO (Morphology)"  ← numberless H3 sib=3 under Appendix E
L199: SENTENCE
L201: LIST_ITEM "- Morphology (MO)"
L203: SENTENCE long narrative
L205: SENTENCE narrative
L207: "### Key Section-by-Section Changes"  ← numberless H3 sib=4 under Appendix E
L209: SENTENCE
L211-212: TABLE_HEADER (Section Number/Section Name/Change(s) 3 cols)
L213-286: TABLE_ROW × 74 (Section-by-Section Changes — **关键: 含 group separator rows with bold cell only** like L213 `| **Section 1. Introduction** | | |` (空 cell 2 个), L215 `| **Section 2. Fundamentals of the SDTM** | | |`, L220 `| **Section 3. Submitting Data in a Standard Format** | | |`, L224 `| **Section 4. Assumptions for Domain Models** | | |`, L229 `| **Section 5. Models for Special-purpose Domains** | | |`, L236 `| **Section 6. Domain Models Based on the General Observation Classes** | | |`, L265 `| **Section 7. Trial Design Model Datasets** | | |`, L273 `| **Section 8. Representing Relationships and Data** | | |`, L280 `| **Section 9. Study References** | | |`, L282 `| **Appendices** | | |` — 10 separator rows; 其余 64 数据 rows 含 section number / name / changes)
L288: "---"  ← HR SKIP
L290: "## Appendix F: Representations and Warranties, Limitations of Liability, and Disclaimers"  ← H2 sib=6
L292: "### CDISC Patent Disclaimers"  ← numberless H3 sib=1 under Appendix F
L294: SENTENCE long
L296: "### Representations and Warranties"  ← numberless H3 sib=2 under Appendix F
L298: SENTENCE quoted (CDISC grants...)
L300: SENTENCE long multi-clause legal (Each Participant...)
L302: "### No Other Warranties/Disclaimers"  ← numberless H3 sib=3 under Appendix F
L304: SENTENCE long ALL CAPS legal
L306: "### Limitation of Liability"  ← numberless H3 sib=4 under Appendix F
L308: SENTENCE long ALL CAPS legal
L310: SENTENCE "Note: The CDISC Intellectual Property Policy can be found at http://..." (file 末; **NOT bold `**Note:**` carve-out** — 是 plain narrative SENTENCE 起首 "Note:" 后无 bold; **NOT NOTE**)
```

### 2.2.5 Boundary critical (Rule A 必入 sample, 7 atoms — 因本 batch 大表 + 多 H3 chain + appendix 形态特殊)

- **a001** L1 HEADING h_lvl=1 sib=1 (新 file H1; parent_section `§10 [Appendices]` simplified)
- **L7 H2 §10.A** sib=1 (验 appendix-style H2 parent_section format `§10.A [CDISC SDS Team]` — 见 §4 D6)
- **L100-101 TABLE_HEADER 5 cols** Fragment Ref side-by-side (验 5 cols 含 empty middle separator column byte-exact)
- **L213 TABLE_ROW group separator** `| **Section 1. Introduction** | | |` (验 separator row 含 bold cell + 2 empty cells preserved byte-exact, 不误判为 SENTENCE 或 HEADING)
- **L201 LIST_ITEM** "- Morphology (MO)" parent §10.E/Decommissioning 子节 (验 LIST_ITEM under numberless H3 § sub-section)
- **L290 H2 §10.F** sib=6 + **L292/L296/L302/L306 H3 §10.F chain** sib=1/2/3/4 (验 §10.F 下 4 numberless H3 sib chain)
- **末原子 L310 SENTENCE** "Note: The CDISC..." (ch10 文件末; **NOT NOTE — 是 plain SENTENCE 起首 "Note:"**)

---

## 3. Hook A4 inline (FIGURE figure_ref 校验)

每 atom_type=FIGURE 必满足: figure_ref 非 null + pattern `md_ch10_<descriptor>`.

**预期: ch10 全文 0 FIGURE** (扫源全无 mermaid block; appendix 是 reference data 形式).

---

## 4. atom_type 决策 (本 batch 关键)

| Source 形态 | atom_type | 注 |
|---|---|---|
| `# SDTMIG v3.4 — Chapter 10: Appendices` (L1) | HEADING h_lvl=1 sib=1 | parent_section `§10 [Appendices]` simplified per batch 05/06/07 |
| `## Appendix A: CDISC SDS Team` etc. (L7/15/64/88/166/290) | HEADING h_lvl=2 sib=1/2/3/4/5/6 | **关键 D6**: appendix-style H2 没数字编号只 letter (Appendix A-F); parent_section bracketed form 推荐 `§10.A [CDISC SDS Team]` / `§10.B [Glossary and Abbreviations]` etc. (per number-prefix convention 用 letter A-F 替数字; 同 ch04 §4.5.X subsection 模式但 letter); 该 H2 atom 自身 parent_section = `§10 [Appendices]` (父); 子 atom parent_section = `§10.A [...]` etc. |
| `### Key Points` `### Appendix C1: Supplemental Qualifiers Name Codes` (L68/L76) | HEADING h_lvl=3 numberless | parent `§10.C [Controlled Terminology]`; sib=1/2 (S-02 rule) |
| `### Rules for Using Fragments` `### Fragment Reference Table` (L92/L98) | HEADING h_lvl=3 numberless | parent `§10.D [CDISC Variable-naming Fragments]`; sib=1/2 |
| `### General Changes Throughout` `### New Domains for SDTMIG v3.4` `### Decommissioning of MO (Morphology)` `### Key Section-by-Section Changes` (L173/L187/L197/L207) | HEADING h_lvl=3 numberless | parent `§10.E [Revision History]`; sib=1/2/3/4 |
| `### CDISC Patent Disclaimers` `### Representations and Warranties` `### No Other Warranties/Disclaimers` `### Limitation of Liability` (L292/L296/L302/L306) | HEADING h_lvl=3 numberless | parent `§10.F [Representations and Warranties, Limitations of Liability, and Disclaimers]`; sib=1/2/3/4 |
| `---` (L5, L13, L62, L86, L164, L288) | **不 emit** | 6 个 horizontal rule skip per batch 02-04 directive |
| L310 SENTENCE 起首 "Note: The CDISC..." | **SENTENCE** (NOT NOTE) | 起首 "Note:" 但**无 bold** `**Note:**` 标记; 是 plain narrative SENTENCE; 与 batch 02-04 `**Note:**` carve-out NOTE 区分 (Hook C-6 PASS) |
| Glossary L19-60 (40 rows) Supp Qual L80-84 (3 rows) New Domains L189-195 (5 rows) | TABLE_HEADER + TABLE_ROW | 标准 2-3 col 表; C-5/A1 hook span ≤1 |
| Fragment Ref L100-163 (62 rows) | TABLE_HEADER (5 cols!) + TABLE_ROW × 62 | **5 col 含 empty middle separator column** `\| Keyword(s) \| Fragment \| \| Keyword(s) \| Fragment \|`; 各 row 含 left+right 2 keyword/fragment pairs; 部分 row 末尾 empty cells (L147 only 4 cols populated, L148-163 only right column populated因左列已穷尽); 全 byte-exact pipe-delimited 含 empty cells |
| Section-by-Section L211-286 (74 rows) | TABLE_HEADER + TABLE_ROW × 74 | **含 10 group separator rows w/ bold cell** like `\| **Section 1. Introduction** \| \| \|` (L213/L215/L220/L224/L229/L236/L265/L273/L280/L282); separator row = 1 TABLE_ROW with bold cell + 2 empty cells (NOT split as HEADING per Hook C-6); 其余 64 数据 row 含 section / name / changes |
| L70-74 5 LIST_ITEM (Key Points) | LIST_ITEM | bullet `- ` + 含 inline URLs (cross_refs field) |
| L94-96 3 LIST_ITEM (Rules for Using Fragments) | LIST_ITEM | bullet `- ` |
| L170-171 2 LIST_ITEM (Diff file note / Public review note) | LIST_ITEM | bullet `- ` 含 inline URL |
| L175-185 11 LIST_ITEM (General Changes Throughout) | LIST_ITEM | bullet `- ` |
| L201 1 LIST_ITEM (Morphology MO) | LIST_ITEM | bullet `- ` parent `§10.E [Revision History]` (under numberless H3 §10.E/Decommissioning) |
| L9/11/17/66/78/90/168/199/203/205/209/294/298/300/304/308 SENTENCE narrative | SENTENCE (multi-atom 同 line_start per §C-1) | sub-line split for multi-clause; 多 inline cross_refs (Section 7.1.2 / URLs) 走 cross_refs field |
| L298 SENTENCE quoted | SENTENCE | quote inline (`"CDISC grants..."`) byte-exact preserved |
| L300/L304/L308 SENTENCE long ALL CAPS legal | SENTENCE (multi-clause split per §C-1 if needed) | 长 legal text retained whole 或 sub-line split |

### 关键决策 D6: appendix-style H2 parent_section format

ch10 6 H2 `## Appendix A` 到 `## Appendix F` 没数字编号, 只 letter (A-F):
- 推荐 parent_section bracketed format 用 letter: `§10.A [CDISC SDS Team]` / `§10.B [Glossary and Abbreviations]` / `§10.C [Controlled Terminology]` / `§10.D [CDISC Variable-naming Fragments]` / `§10.E [Revision History]` / `§10.F [Representations and Warranties, Limitations of Liability, and Disclaimers]`
- 该 H2 atoms 本身 parent_section = `§10 [Appendices]` (父)
- 子 atom parent_section = `§10.A [...]` etc. (per number-prefix semantic convention 同 §4.5.1.3 / §3.2.1 等模式)
- alternative: 全 atoms parent_section = `§10 [Appendices]` (markdown-strict, 不区分 appendix sub-grouping); **不推荐** (失结构)

writer 选 D6 推荐 (semantic letter-prefix), 在 dispatch report flag + 例 atom_id 让 reviewer 验. v1.9.1 候选 +1 codify D6 同 D5 类 sub-pattern: "letter-prefix appendix-style H2 sib chain".

### Hook C-6 关键: TABLE_ROW group separator 含 bold cell 不误判为 HEADING

L213/L215/L220/L224/L229/L236/L265/L273/L280/L282 (Section-by-Section table 内 10 group separator rows) 形如 `| **Section 1. Introduction** | | |`:
- atom_type = TABLE_ROW (因 pipe-delimited 在 markdown table 内, 不是 standalone heading line)
- verbatim 含 `\| **Section 1. Introduction** \| \| \|` 全 pipe 分隔含 bold + empty cells, byte-exact
- Hook C-6 PASS: bold inside table cell ≠ HEADING (ascii `^#{1,6}\s+` regex 不匹配 pipe-delimited line)

### L310 关键: "Note: ..." 起首 SENTENCE NOT NOTE

L310 source: `Note: The CDISC Intellectual Property Policy can be found at http://...`:
- 起首 "Note:" 但**无** `**` bold markers
- 是 plain narrative SENTENCE 起首 "Note:" 短语 (interleaved 模式)
- 与 batch 02-04 `**Note:** ...` (bold-Note carve-out NOTE) 严格区分
- atom_type = SENTENCE, parent `§10.F [...]` (under numberless H3 §10.F/Limitation of Liability — 末 sub-section trailing); 末 atom

---

## 5. Dispatch 模板 — **FALLBACK PATH** sustained 5-batch (会变 6-batch post 本 batch)

派 `general-purpose` 单 dispatch.

1. Schema-first 头部
2. parent_section canonical bracketed format
3. 本 batch 特定:
   - file: `knowledge_base/chapters/ch10_appendices.md`
   - line range: **1-310 (全文)**
   - atom_id prefix: `md_ch10_a` 从 `a001`
   - batch_id: `P2_B-02_batch_08`
   - 输出: `evidence/checkpoints/P2_B-02_batch_08_md_atoms.jsonl`
   - extracted_by.subagent_type: `"general-purpose"`
4. 22 hooks self-validate
5. **§4 atom_type 决策 + D6 letter-prefix appendix H2 + Hook C-6 separator row + L310 SENTENCE-not-NOTE 全粘**

---

## 6. Rule A 跟进 — **FALLBACK PATH**

派 `pr-review-toolkit:code-reviewer`. 10-atom 分层独审 (7 boundary + 3 stratified per §2.2.5).

---

## 7. PASS 后 append + checkpoint

- root append (2264 → ~2520-2530)
- audit_matrix.md + ch10 milestone (B-02 5 文件全完, 余 1 batch ch08)
- trace.jsonl batch_complete + phase_report
- _progress.json batches_done=8 / files_complete += ch10 / next_batch=batch 09 (ch08, **最后 1 batch in B-02 cycle**)
- 写 batch_08_report.md (含 D6 决策详细)

---

*Kickoff written 2026-05-05. Source 已实测 read 310 行 + 实数 5 表 + 12 numberless H3 + 6 HR + 19 HEADING; 无 markdown anomaly. FALLBACK 路径 sustained.*
