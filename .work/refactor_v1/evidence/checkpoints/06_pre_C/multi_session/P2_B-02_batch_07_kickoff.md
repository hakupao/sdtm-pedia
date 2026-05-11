# P2 B-02 batch 07 — Multi-Session Kickoff (新 file)

> 创建: 2026-05-04 (post `P2_B-02_batch_06` 全闭环 commit 65322bc, ch03 100% milestone, L117 Rule B exemplary)
> 父 kickoff: `multi_session/P2_B-02_kickoff.md` (umbrella §3 第 7 行)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` + 本 kickoff §3 inline 头部
> 路由词: 用户说 **"P2 bulk B-02 batch 07 开始任务"** 即触发 dispatch
> **本 batch = 新 file (ch02_fundamentals.md), 单 dispatch full-file 模式同 batch 05/06**
> **L117 教训**: 本 kickoff 写前已 Read source 全 (174 行); 所有 heading level 已与 source 实测对齐 (无 anomaly).

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_kickoff.md` (umbrella §5 + §6)
2. `subagent_prompts/P0_writer_md_v1.9.md` + `P0_reviewer_v1.9.md`
3. `schema/atom_schema.json` v1.2.1
4. `evidence/checkpoints/P2_B-02_batch_06_report.md` (前 batch + ch03 milestone + L117 Rule B 决策参考)
5. 本 kickoff

---

## 2. Batch 07 任务

### 2.1 Target

- **文件**: `knowledge_base/chapters/ch02_fundamentals.md`
- **切片**: **全文 174 行** (单 dispatch, 模式同 batch 05/06)
- **估 atoms**: ~120-135 (基于 ch01 0.86 + ch03 0.923; 174 × 0.75 ≈ 130; 含 1 FIGURE + 5 表 + ~48 LIST_ITEM + 嵌套 sub-bullets/sub-letters)
- **atom_id 起始**: `md_ch02_a001` (新 file)

### 2.2 ch02 结构 prefix (writer 必读 — 已与 source 174 行实测对齐)

```
L1:   "# SDTMIG v3.4 — Chapter 2: Fundamentals of the SDTM"  ← H1 sib=1
L3:   "Source: ..."  ← SENTENCE
L5:   "## 2.1 Observations and Variables"  ← H2 sib=1
L7:   SENTENCE (multi-clause, 含 bold inline `**observations**` + `**role**`)
L9:   "### Variable Roles (5 major roles)"  ← **numberless H3** sib=1 under §2.1
L11-15: 5 numbered LIST_ITEM (Identifier/Topic/Timing/Qualifier/Rule, 含 bold cell name)
L17:  "### Qualifier Variable Subclasses"  ← numberless H3 sib=2 under §2.1
L19-20: TABLE_HEADER (Subclass/Purpose/Examples 3 cols)
L21-25: TABLE_ROW × 5 (Grouping/Result/Synonym/Record/Variable Qualifiers, 含 bold cell)
L27:  SENTENCE caption "**Example:** ..."
L28-31: 4 LIST_ITEM (Topic variable / Identifier variable / Timing variable / Record Qualifier — 含 bold cell)
L33:  "## 2.2 Datasets and Domains"  ← H2 sib=2
L35:  SENTENCE 含 bold `**domain**`
L37:  SENTENCE
L38-41: 4 numbered LIST_ITEM (DOMAIN code uses)
L43:  SENTENCE
L45:  SENTENCE w/ inline cross-refs (Section 5, Section 6, Section 1.4.1)
L47:  SENTENCE "Data represented in SDTM datasets include:"
L48-51: 4 LIST_ITEM (Data as originally collected... / Data from protocol / Assigned / Derived)
L53:  "## 2.3 The General Observation Classes"  ← H2 sib=3
L55:  SENTENCE
L57-58: TABLE_HEADER (Class/What/Examples 3 cols)
L59-61: TABLE_ROW × 3 (Interventions/Events/Findings, 含 bold class name + EX/CM/PR/AE/DS/MH/LB/VS/EG inline)
L63:  SENTENCE
L65:  SENTENCE caption "**Additional guidance** on choosing the appropriate GOC is in Section 8.6.1, ..." (bold-prefix on phrase, NOT Note carve-out)
L67:  SENTENCE w/ inline ref Section 4
L69:  "## 2.4 Datasets Other than General Observation Class Domains"  ← H2 sib=4
L71:  SENTENCE
L73-74: TABLE_HEADER (Type/Description/Examples/Section 4 cols)
L75-78: TABLE_ROW × 4 (Special-purpose/Trial Design Model/Relationship/Study Reference)
L80:  "## 2.5 The SDTM Standard Domain Models"  ← H2 sib=5
L82:  SENTENCE narrative
L84:  SENTENCE w/ inline refs (Section 3.2.1, URL https://..., CDISC wiki)
L86:  "### General rules for determining which variables to include:"  ← numberless H3 sib=1 under §2.5
L88-94: 7 numbered LIST_ITEM (general rules; L93/94 long multi-clause)
L96:  "## 2.6 Creating a New Domain"  ← H2 sib=6
L98-108: ```mermaid graph TD ... ```  ← **FIGURE atom!** parent §2.6, figure_ref required (suggested `md_ch02_new_domain_creation_concept_map`)
L110: SENTENCE "Process for creating a custom domain..."
L112: 1 numbered LIST_ITEM "1. Confirm that none of the existing..."  含 sub-bullets L113-114
L113-114: 2 sub-LIST_ITEM (`  - ` indented under L112) parent §2.6
L115: 1 numbered LIST_ITEM "2. Check the SDTM Draft..."
L116: 1 numbered LIST_ITEM "3. Look for an existing..." 含 sub-letters L117-127
L117-127: 11 sub-LIST_ITEM `  - a. ...` `  - b. ...` ... `  - k. ...` parent §2.6
L129: SENTENCE caption "**Key rules for custom domains:**"
L130-133: 4 LIST_ITEM (rules for custom domains)
L135: "## 2.7 SDTM Variables Not Allowed in the SDTMIG"  ← H2 sib=7
L137: "### Must NEVER be used in human clinical trials (SEND-only):"  ← numberless H3 sib=1 under §2.7
L139-140: TABLE_HEADER (Variable/Class(es) 2 cols)
L141-155: TABLE_ROW × 15 (--USCHFL/--METHOD/--RSTIND/--RSTMOD/--IMPLBL/--RESLOC/--DTHREL/--EXCLFL/--REASEX/FETUSID/RPHASE/RPPLDY,RPPLSTDY,RPPLENDY/--NOMDY,--NOMLBL/--RPDY,--RPSTDY,--RPENDY/--DETECT)
L157: "### Must NEVER be used in DM domain (SEND nonclinical only):"  ← numberless H3 sib=2 under §2.7
L159: SENTENCE w/ inline ref Section 9.2
L161: 1 LIST_ITEM "- SPECIES, STRAIN, SBSTRAIN, RPATHCD"
L163: "### Use with extreme caution (not fully evaluated for human clinical trials):"  ← numberless H3 sib=3 under §2.7
L165-168: 4 LIST_ITEM (--ANTREG / --CHRON / --DISTR / SETCD w/ inline ref Trial Sets)
L170: "### May be used when appropriate:"  ← numberless H3 sib=4 under §2.7
L172: 1 LIST_ITEM "- POOLID — additionally requires the Pool Definition dataset"
L174: SENTENCE long narrative w/ inline ref Section 2.6 (file 末 atom)
```

### 2.2.5 Boundary critical (Rule A 必入 sample, 6 atoms)

- **a001** L1 HEADING h_lvl=1 sib=1 (新 file H1; parent_section `§2 [Fundamentals of the SDTM]` simplified)
- **L9 / L17 H3 §2.1 numberless chain** sib=1/2 (验 numberless H3 D5 + S-02)
- **L98-108 FIGURE mermaid `graph TD`** parent §2.6 figure_ref non-null (本 batch 唯一 FIGURE, Hook A4 关键)
- **L116 numbered LIST_ITEM `3.` w/ 11 sub-letter sub-bullets L117-127** (验 nested LIST_ITEM 多层 indent: 数字 prefix + sub-letter prefix `  - a.` `  - b.` 等; parent_section 同 outer)
- **L137 / L157 / L163 / L170 H3 §2.7 numberless chain** sib=1/2/3/4 (验 4 个 numberless H3 sib chain 续)
- **末原子 L174 SENTENCE** (ch02 文件末; 含 inline ref Section 2.6 走 cross_refs field)

---

## 3. Hook A4 inline (FIGURE figure_ref 校验)

每 atom_type=FIGURE 必满足: figure_ref 非 null + pattern `md_ch02_<descriptor>`.

**预期: ch02 全文 1 FIGURE** (L98-108 mermaid `graph TD` New Domain Creation flow). 建议 figure_ref: `md_ch02_new_domain_creation_concept_map` (内容: Identifier/Timing nodes AND Topic-Qualifier nodes OR-branch to Interventions/Events/Findings GOC-specific OR-branch to New Domain).

---

## 4. atom_type 决策 (本 batch 关键)

| Source 形态 | atom_type | 注 |
|---|---|---|
| `# SDTMIG v3.4 — Chapter 2: Fundamentals of the SDTM` (L1) | HEADING h_lvl=1 sib=1 | parent_section `§2 [Fundamentals of the SDTM]` simplified per batch 05 D1 / batch 06 |
| `## 2.1` (L5) `## 2.2` (L33) `## 2.3` (L53) `## 2.4` (L69) `## 2.5` (L80) `## 2.6` (L96) `## 2.7` (L135) | HEADING h_lvl=2 sib=1/2/3/4/5/6/7 | parent `§2 [Fundamentals of the SDTM]`; 7 H2 chain 全打 |
| `### Variable Roles ...` (L9) `### Qualifier Variable Subclasses` (L17) | HEADING h_lvl=3 numberless | parent `§2.1 [Observations and Variables]`; sib=1/2 (per S-02 rule from batch 05) |
| `### General rules for determining which variables to include:` (L86) | HEADING h_lvl=3 numberless | parent `§2.5 [The SDTM Standard Domain Models]`; sib=1 RESTART under §2.5 |
| `### Must NEVER be used in human clinical trials (SEND-only):` (L137) `### Must NEVER be used in DM domain (SEND nonclinical only):` (L157) `### Use with extreme caution (not fully evaluated for human clinical trials):` (L163) `### May be used when appropriate:` (L170) | HEADING h_lvl=3 numberless | parent `§2.7 [SDTM Variables Not Allowed in the SDTMIG]`; sib=1/2/3/4 chain (per S-02) |
| `**Example:** In the observation ...` (L27) | SENTENCE caption | per kickoff §4 ch03 batch 06 D `**Example:**` = SENTENCE caption (NOT NOTE), 全句 retained whole |
| `**Additional guidance** on choosing the appropriate GOC is in Section 8.6.1, ...` (L65) | SENTENCE | bold prefix on PHRASE not full caption; treat as normal SENTENCE w/ bold inline preserved + cross_refs `["§8.6.1 Guidelines for Determining the General Observation Class"]` |
| `**Key rules for custom domains:**` (L129) | SENTENCE caption | 普通 label, 同 `**Definitions:**` (L103 ch03) 处理 |
| **5 表** | TABLE_HEADER + TABLE_ROW | C-5/A1 hook span ≤1; bold cell content (e.g., `\| **Grouping Qualifiers** \| ...`) preserved byte-exact in TABLE_ROW verbatim, NOT split as HEADING |
| L98-108 mermaid block | FIGURE | figure_ref 必填 `md_ch02_new_domain_creation_concept_map`; verbatim 全 mermaid 含围栏; parent §2.6 |
| L11-15 5 numbered LIST_ITEM (Variable Roles) | LIST_ITEM | 数字 prefix `1. ` `2. ` ... + bold cell `**Identifier variables**` etc. retained byte-exact in verbatim |
| L28-31 4 LIST_ITEM (Example obs subitems) | LIST_ITEM | bullet `- ` + bold cell `**Topic variable value**` retained |
| L38-41 4 numbered LIST_ITEM (DOMAIN uses) | LIST_ITEM | 数字 prefix |
| L48-51 4 LIST_ITEM (Data types) | LIST_ITEM | bullet `- ` |
| L88-94 7 numbered LIST_ITEM (general rules) | LIST_ITEM | 数字 prefix; L93/94 long multi-clause kept whole per Hook C-7 |
| L112 + L113-114 nested | L112 LIST_ITEM (1.) parent §2.6 + L113-114 sub-LIST_ITEM (`  - `) parent §2.6 (per kickoff §4 batch 04: sub-bullets 同 LIST_ITEM 不 nest type, parent same as outer) |
| L115 L116 numbered LIST_ITEM (2./3.) + L117-127 sub-letters | L115 LIST_ITEM (2.) + L116 LIST_ITEM (3.) + L117-127 11 sub-LIST_ITEM (`  - a.` `  - b.` ... `  - k.`) parent §2.6 | sub-letter prefix `  - a. ` retained byte-exact; parent §2.6 |
| L130-133 4 LIST_ITEM (key rules) | LIST_ITEM | bullet `- ` parent §2.6 |
| L141-155 SEND vars TABLE_ROW × 15 | TABLE_ROW | parent `§2.7 [...] / Must NEVER human` (numberless H3 sub-section — but per S-02/ch01 D, parent 走父 H2 `§2.7 [...]` 即可, 不造合成); 每行含 `--XXXX` literal prefix |
| L161 LIST_ITEM "SPECIES, STRAIN, SBSTRAIN, RPATHCD" | LIST_ITEM | parent `§2.7 [...]` (under numberless H3 §2.7/Must NEVER DM) |
| L165-168 LIST_ITEM × 4 | LIST_ITEM | parent `§2.7 [...]` (under numberless H3 §2.7/Use extreme caution) |
| L172 LIST_ITEM "POOLID — additionally requires the Pool Definition dataset" | LIST_ITEM | parent `§2.7 [...]` (under numberless H3 §2.7/May be used) |
| L174 SENTENCE 长 narrative w/ inline ref Section 2.6 | SENTENCE w/ cross_refs `["§2.6 Creating a New Domain"]` (or sub-line split per §C-1 if multi-clause) | ch02 文件末 |
| L7/35/37/43/45/47/55/63/67/71/82/84/110 long narrative | SENTENCE (multi-atom 同 line_start per §C-1) | sub-line split for multi-clause |

### 关键决策 reminders

1. **L1 H1 parent**: simplified `§2 [Fundamentals of the SDTM]` per batch 05 D1 / batch 06 模式
2. **7 H3 全 numberless** (per ch01 batch 05 S-02 rule): parent_section 走父 H2 bracketed form
3. **L98-108 FIGURE mermaid**: figure_ref 必填 `md_ch02_new_domain_creation_concept_map`
4. **Nested LIST_ITEM** (L112/113-114 + L116/117-127): sub-bullets 同 LIST_ITEM 不另立 nested type, parent_section 同 outer
5. **`**Example:**` (L27)** = SENTENCE caption kept whole (per batch 06 D)
6. **`**Additional guidance**` (L65)** = SENTENCE w/ bold inline + cross_refs (NOT carve-out NOTE)
7. **0 NOTE** (本 batch 无 `**Note:**` carve-out 形态)
8. **多 inline section refs** 走 cross_refs field on parent SENTENCE/LIST_ITEM (Section 4 / 5 / 6 / 1.4.1 / 3.2.1 / 8.6.1 / 9.2 / 2.6 等); 不 promote 独立 CROSS_REF (vs batch 04 a892 short standalone 区分)

---

## 5. Dispatch 模板 — **FALLBACK PATH** sustained

派 `general-purpose` 单 dispatch.

1. Schema-first 头部
2. parent_section canonical bracketed format
3. 本 batch 特定:
   - file: `knowledge_base/chapters/ch02_fundamentals.md`
   - line range: **1-174 (全文)**
   - atom_id prefix: `md_ch02_a` 从 `a001`
   - batch_id: `P2_B-02_batch_07`
   - 输出: `evidence/checkpoints/P2_B-02_batch_07_md_atoms.jsonl`
   - extracted_by.subagent_type: `"general-purpose"`
4. 22 hooks self-validate
5. **§4 atom_type 决策 + 7 reminders 全粘**

---

## 6. Rule A 跟进 — **FALLBACK PATH**

派 `pr-review-toolkit:code-reviewer`. 10-atom 分层独审 (6 boundary + 4 stratified per §2.2.5).

---

## 7. PASS 后 append + checkpoint

- root append (2132 → ~2255-2275)
- audit_matrix.md + ch02 milestone
- trace.jsonl batch_complete + phase_report
- _progress.json batches_done=7 / files_complete += ch02 / next_batch=batch 08 (ch10)
- 写 batch_07_report.md

---

*Kickoff written 2026-05-04 (post batch 06 + ch03 milestone + L117 教训). Source 已实测 read 174 行, 无 markdown anomaly; FALLBACK 路径 sustained.*
