# P2 B-02 batch 09 — Multi-Session Kickoff (大文件 + 1 mermaid FIGURE + 1 blockquote NOTE)

> 创建: 2026-05-05 (post `P2_B-02_batch_08` 全闭环 commit ce18b04, ch10 100% milestone + D6 codify)
> 父 kickoff: `multi_session/P2_B-02_kickoff.md` (umbrella §3 第 9 行 — **B-02 cycle 最后 batch**)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` + 本 kickoff §3 inline 头部
> 路由词: 用户说 **"P2 bulk B-02 batch 09 开始任务"** 即触发 dispatch
> **本 batch = 新 file (ch08_relationships.md), 单 dispatch full-file 模式同 batch 05/06/07/08**
> **L117/5表/62→61 教训**: 本 kickoff 写前已 Read source 全 (439 行 / 100+130+90+多分段) + 实数 9 H2 + 19 H3 (11 numbered + 8 numberless) + 8 HR skips + 15 表 (15 TABLE_HEADER + 84 TABLE_ROW) + 1 mermaid FIGURE + 1 blockquote-NOTE + 29 unordered LIST_ITEM + 19 ordered LIST_ITEM + 17 bold-caption SENTENCE 全 grep 校验 byte-exact

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_kickoff.md` (umbrella §5 + §6 — **B-02 cycle 最后 batch**)
2. `subagent_prompts/P0_writer_md_v1.9.md` + `P0_reviewer_v1.9.md`
3. `schema/atom_schema.json` v1.2.1
4. `evidence/checkpoints/P2_B-02_batch_08_report.md` (前 batch + ch10 milestone + D6 letter-prefix codify 参考)
5. 本 kickoff

---

## 2. Batch 09 任务

### 2.1 Target

- **文件**: `knowledge_base/chapters/ch08_relationships.md`
- **切片**: **全文 439 行** (单 dispatch, 模式同 batch 05/06/07/08; 估 token < 32K cap)
- **估 atoms**: **~245-275** (29 HEADING + 48 LIST_ITEM + 15 TABLE_HEADER + 84 TABLE_ROW + 1 FIGURE + 1 NOTE + ~65-75 SENTENCE; density ~0.6 atoms/line, 大表 + spec-table 结构密集; recovery_hint ~310 偏高估, 实际值待 dispatch 确认)
- **atom_id 起始**: `md_ch08_a001` (新 file)
- **特殊**: ch08 是 5 spec-table + 9 example-table + 1 question-table + 1 mermaid FIGURE + 1 blockquote-NOTE 混合形态; 是 P2 cycle 中**首次出现 mermaid FIGURE atom in chapters/** + **首次出现 blockquote-prefix `> **Note:**` NOTE 形态**

### 2.2 ch08 结构 prefix (writer 必读 — 已与 source 439 行实测对齐)

```
L1:   "# SDTMIG v3.4 — Chapter 8: Representing Relationships and Data"  ← H1 sib=1
L3:   "Source: SDTMIG v3.4, Section 8 (Pages 427-446)"  ← SENTENCE
L5:   "## Overview"  ← H2 sib=1 (numberless; D8 candidate — children inherit chapter root parent per batch 01-04 ch04 v2 precedent)
L7:   SENTENCE long narrative
L9-16: 8 LIST_ITEM `- **Section 8.X**, ...` (bold-prefix Overview list)
L18:  SENTENCE long narrative
L20-22: 3 LIST_ITEM `- ` (bold-prefix variable narratives)
L24:  "---"  ← HR SKIP
L26:  "## 8.1 Relating Groups of Records Within a Domain Using --GRPID"  ← H2 sib=2
L28:  SENTENCE long
L30:  SENTENCE
L32:  "### 8.1.1 --GRPID Example"  ← H3 numbered sib=1 under §8.1
L34:  SENTENCE long
L36/38/40/42: 4 SENTENCE bold-caption "**Rows N-M:**" (per bold-caption SENTENCE rule)
L44:  SENTENCE caption "cm.xpt:"
L46-47: TABLE_HEADER (CM 12-col)
L48-59: TABLE_ROW × 12 (cm.xpt example)
L61:  "---"  ← HR SKIP
L63:  "## 8.2 Relating Peer Records"  ← H2 sib=3
L65:  SENTENCE long
L67:  SENTENCE long
L69:  SENTENCE long
L71:  SENTENCE caption "The RELREC dataset should be used to represent either:"
L73-74: 2 LIST_ITEM `- ` (含 Section 8.3 cross_ref)
L76:  "### 8.2.1 Related Records (RELREC)"  ← H3 numbered sib=1 under §8.2
L78:  SENTENCE bold-caption "**RELREC — Description/Overview**" (single-line bold caption SENTENCE)
L80:  SENTENCE narrative
L82:  SENTENCE bold-caption "**RELREC — Specification**"
L84:  SENTENCE caption "relrec.xpt, Related Records — ..."
L86-87: TABLE_HEADER (RELREC Spec 7-col w/ Variable Name | Variable Label | Type | CT | Role | CDISC Notes | Core)
L88-94: TABLE_ROW × 7 (STUDYID/RDOMAIN/USUBJID/IDVAR/IDVARVAL/RELTYPE/RELID)
L96:  SENTENCE footnote `^1^ In this column, an asterisk...`
L98:  "### 8.2.2 RELREC Dataset Examples"  ← H3 numbered sib=2 under §8.2
L100: SENTENCE bold-caption "**Example 1:** ..."
L102/104: 2 SENTENCE bold-caption "**Rows N-M:**"
L106: SENTENCE caption "relrec.xpt:"
L108-109: TABLE_HEADER (RELREC Ex1 8-col)
L110-115: TABLE_ROW × 6 (Ex1)
L117: SENTENCE bold-caption "**Example 2:** ..."
L119: SENTENCE caption "relrec.xpt:"
L121-122: TABLE_HEADER (RELREC Ex2 8-col)
L123-127: TABLE_ROW × 5 (Ex2)
L129: SENTENCE bold-caption "**Example 3:** ..."
L131: SENTENCE caption "relrec.xpt:"
L133-134: TABLE_HEADER (RELREC Ex3 8-col)
L135-138: TABLE_ROW × 4 (Ex3)
L140: SENTENCE long w/ Section 6.2.4/6.3.5.9.3 cross_refs
L142: "---"  ← HR SKIP
L144: "## 8.3 Relating Datasets Using RELREC"  ← H2 sib=4
L146: SENTENCE long
L148: SENTENCE long w/ Section 8.3 cross_ref
L150: "### 8.3.1 RELREC Dataset Relationship Example"  ← H3 numbered sib=1 under §8.3
L152: SENTENCE bold-caption "**Example 1:** ..."
L154: SENTENCE caption "relrec.xpt:"
L156-157: TABLE_HEADER (RELREC §8.3 8-col)
L158-159: TABLE_ROW × 2
L161: SENTENCE long
L163: SENTENCE long
L165: LIST_ITEM ordered "1. **ONE and ONE.** ..." (ordered list bold-prefix)
L167: LIST_ITEM ordered "2. **ONE and MANY.** ..."
L169: LIST_ITEM ordered "3. **MANY and MANY.** ..."
L171: SENTENCE long
L173: "---"  ← HR SKIP
L175: "## 8.4 Relating Non-standard Variable Values to a Parent Domain"  ← H2 sib=5
L177: SENTENCE long w/ Section 8.4.2 cross_ref
L179: SENTENCE long w/ Section 4.1.8/Appendix C1 cross_refs
L181: SENTENCE long (含 inline bold "**attributions**")
L183: SENTENCE long
L185: SENTENCE long
L187: "### 8.4.1 Supplemental Qualifiers (SUPP--)"  ← H3 numbered sib=1 under §8.4
L189: SENTENCE caption "supp--.xpt, Supplemental Qualifiers..."
L191-192: TABLE_HEADER (SUPP-- Spec 7-col)
L193-202: TABLE_ROW × 10 (STUDYID/RDOMAIN/USUBJID/IDVAR/IDVARVAL/QNAM/QLABEL/QVAL/QORIG/QEVAL)
L204: SENTENCE footnote `^1^ In this column...`
L206: "### Key Rules"  ← H3 numberless sib=2 under §8.4 (S-02; located between §8.4.1 spec table and §8.4.2)
L208-211: 4 LIST_ITEM `- ` (Key Rules, w/ Section 4.5.3/Appendix C1 cross_refs)
L213: "### 8.4.2 Submitting Supplemental Qualifiers in Separate Datasets"  ← H3 numbered sib=3 under §8.4
L215: SENTENCE long (含 inline bold "**deprecated**" + Section 4.1.7 cross_ref)
L217: SENTENCE long w/ Section 4.5.3 cross_ref
L219: "### 8.4.3 Examples"  ← H3 numbered sib=4 under §8.4
L221: SENTENCE narrative
L223: SENTENCE bold-caption "**Example 1:** ..."
L225: SENTENCE caption "suppae.xpt:"
L227-228: TABLE_HEADER (suppae 11-col)
L229-230: TABLE_ROW × 2
L232: SENTENCE bold-caption "**Example 2:** ..." long
L234: SENTENCE caption "suppqs.xpt:"
L236-237: TABLE_HEADER (suppqs 11-col)
L238-241: TABLE_ROW × 4
L243: SENTENCE long w/ Section 5.2/6.3.3/6.3.5.6 cross_refs
L245: "### 8.4.4 When Not to Use Supplemental Qualifiers"  ← H3 numbered sib=5 under §8.4
L247: SENTENCE long (含 inline bold "**not**")
L249-252: 4 LIST_ITEM `- ` (含 Section 4.5.5 cross_ref)
L254: "---"  ← HR SKIP
L256: "## 8.5 Relating Comments to a Parent Domain"  ← H2 sib=6
L258: SENTENCE long w/ Section 5.1 cross_ref
L260: SENTENCE long
L262-264: 3 LIST_ITEM ordered "1./2./3."
L266: SENTENCE narrative
L268-269: 2 LIST_ITEM ordered "1./2." (含 Section 5.1 cross_ref)
L271: SENTENCE long
L273: "---"  ← HR SKIP
L275: "## 8.6 Where Data Belong"  ← H2 sib=7
L277: "### 8.6.1 Guidelines for Determining the General Observation Class"  ← H3 numbered sib=1 under §8.6
L279: SENTENCE long w/ Section 2.6/2.3 cross_refs
L281: SENTENCE long
L283: SENTENCE long w/ Section 8.6.3 cross_ref
L285: SENTENCE long w/ Section 8.6.3 cross_ref
L287: "### 8.6.2 Guidelines for Forming New Domains"  ← H3 numbered sib=2 under §8.6
L289: SENTENCE narrative w/ Section 2.6 cross_ref
L291: "### 8.6.3 Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions"  ← H3 numbered sib=3 under §8.6 (long heading)
L293: SENTENCE narrative
L295: SENTENCE long
L297: SENTENCE long
L299-304: 6 LIST_ITEM `- ` (含 Section 6.2.1 cross_ref @ L304)
L306: SENTENCE long
L308-309: TABLE_HEADER (Question/Interpretation 2-col)
L310-315: TABLE_ROW × 6 (questions table; 含 inline URL https://www.cdisc.org/foundational/qrs @ row 6)
L317: SENTENCE long w/ Section 6.2.1 cross_ref
L319: SENTENCE narrative
L321: SENTENCE long
L323-324: 2 LIST_ITEM `- ` (data choice; 含 Section 6.4.1 cross_ref @ L324)
L326: "---"  ← HR SKIP
L328: "## 8.7 Related Subjects (RELSUB)"  ← H2 sib=8
L330: "### Specification"  ← H3 numberless sib=1 under §8.7 (S-02)
L332-333: TABLE_HEADER (RELSUB Spec 4-col Variable/Label/Type/Core)
L334-338: TABLE_ROW × 5 (STUDYID/USUBJID/POOLID/RSUBJID/SREL)
L340: "### Assumptions"  ← H3 numberless sib=2 under §8.7 (S-02)
L342-349: 8 LIST_ITEM ordered "1.-8." (RELSUB Assumptions; 含 Section refs implicit)
L351: "### Example"  ← H3 numberless sib=3 under §8.7 (S-02)
L353: SENTENCE narrative
L355: SENTENCE narrative
L357-358: 2 SENTENCE bold-caption "**Row 1:**" / "**Rows 2-3:**"
L360: SENTENCE caption "dm.xpt:"
L362-363: TABLE_HEADER (DM example 7-col)
L364-366: TABLE_ROW × 3
L368: SENTENCE narrative
L370-372: 3 SENTENCE bold-caption "**Rows N-M:**"
L374: SENTENCE caption "relsub.xpt:"
L376-377: TABLE_HEADER (RELSUB example 5-col)
L378-383: TABLE_ROW × 6
L385: "---"  ← HR SKIP
L387: "## 8.8 Related Specimens (RELSPEC)"  ← H2 sib=9
L389: "> **Note:** BE, BS, and RELSPEC domain specifications, assumptions, and examples were copied and minimally updated from the provisional SDTMIG-PGx, published 2015-05-26. ..."  ← **NOTE atom_type** (D7 NEW: blockquote-prefix `> **Note:**` NOTE 形态; 详见 §4 决策)
L391: "### RELSPEC — Description/Overview"  ← H3 numberless sib=1 under §8.8 (S-02; em-dash divider in heading text, byte-exact preserved)
L393: SENTENCE narrative
L395: "### Specification"  ← H3 numberless sib=2 under §8.8 (S-02)
L397: SENTENCE caption "relspec.xpt, Related Specimens — ..."
L399-400: TABLE_HEADER (RELSPEC Spec 7-col)
L401-406: TABLE_ROW × 6 (STUDYID/USUBJID/REFID/SPEC/PARENT/LEVEL)
L408: "### Assumptions"  ← H3 numberless sib=3 under §8.8 (S-02)
L410-412: 3 LIST_ITEM ordered "1.-3."
L414: "### Example"  ← H3 numberless sib=4 under §8.8 (S-02)
L416: SENTENCE narrative
L418: SENTENCE bold-caption "**Figure. Sample Specimen Relationship**"
L420-426: ```mermaid graph TD ...```  ← **FIGURE atom_type** (1 FIGURE; figure_ref 必填; 详见 §3 Hook A4)
L428: SENTENCE long
L430: SENTENCE caption "relspec.xpt:"
L432-433: TABLE_HEADER (relspec.xpt 7-col Row/STUDYID/USUBJID/REFID/SPEC/PARENT/LEVEL)
L434-439: TABLE_ROW × 6 (relspec.xpt rows 1-6; row 1 = SPC-001 Tissue Level 1 / row 2 = SPC-001-A child Level 2 / row 3 = SPC-001-B child Level 2 / row 4 = SPC-001-B-1 DNA child Level 3 / row 5 = SPC-003 Brain Level 1 / row 6 = SPC-003-A RNA child Level 2)
**End of file at L439** (TABLE_ROW final = ch08 末原子)
```

**Source 实测校验 (kickoff 写前 grep checksum)**:
- 总行数: 439 ✓
- H1: 1 ✓ (L1)
- H2: 9 ✓ (L5/26/63/144/175/256/275/328/387 — 1 numberless + 8 numbered)
- H3: 19 ✓ (11 numbered: L32/76/98/150/187/213/219/245/277/287/291; 8 numberless: L206/330/340/351/391/395/408/414)
- HR `---`: 8 ✓ (L24/61/142/173/254/273/326/385)
- 表 (lines starting with `|`): 114 行 = 15 TABLE_HEADER 30 行 (header + alignment) + 84 TABLE_ROW
- 15 表 distribution:
  - cm.xpt L46-59 (12 ROW)
  - RELREC Spec L86-94 (7 ROW)
  - RELREC Ex1 L106-115 (6 ROW)
  - RELREC Ex2 L119-127 (5 ROW)
  - RELREC Ex3 L131-138 (4 ROW)
  - RELREC §8.3.1 L154-159 (2 ROW)
  - SUPP-- Spec L191-202 (10 ROW)
  - suppae L225-230 (2 ROW)
  - suppqs L234-241 (4 ROW)
  - §8.6.3 questions L308-315 (6 ROW)
  - RELSUB Spec L332-338 (5 ROW)
  - dm.xpt L360-366 (3 ROW)
  - relsub.xpt L374-383 (6 ROW)
  - RELSPEC Spec L399-406 (6 ROW)
  - relspec.xpt L430-439 (6 ROW)
  - **TABLE_ROW total = 12+7+6+5+4+2+10+2+4+6+5+3+6+6+6 = 84 ✓**
- LIST_ITEM unordered (`^- `): 29 ✓
- LIST_ITEM ordered (`^[0-9]+\.`): 19 ✓ (L165/167/169 + L262/263/264 + L268/269 + L342-349 + L410-412 = 3+3+2+8+3 = 19)
- LIST_ITEM total: 29 + 19 = 48
- bold-caption SENTENCE patterns (`^**(Row|Example) `): 17 ✓ (4 cm + 2 ex1 + 2 ex2 + 2 ex3 + 1 §8.3 + 2 §8.4 + 2 §8.7 dm + 3 §8.7 relsub + 1 §8.8 figure 缺 = 17 实测确认)
- blockquote-NOTE (`^> `): 1 ✓ (L389)
- mermaid block (` ```mermaid `): 1 ✓ (L420-426)
- inline `**Note:**` (non-blockquote): 0 ✓ (与 batch 02-04 carve-out 区分)

### 2.2.5 Boundary critical (Rule A 必入 sample, **8 atoms** — 因本 batch 多新形态: FIGURE + blockquote-NOTE + S-02 双 chain + bold-caption 大量 + ordered LIST_ITEM 多)

- **a001** L1 HEADING h_lvl=1 sib=1 (新 file H1; parent_section `§8 [Representing Relationships and Data]` simplified per batch 05/06/07/08)
- **L5 H2 ## Overview** sib=1 numberless (验 numberless H2 sib chain 第 1 位; parent_section 自身 `§8 [Representing Relationships and Data]`; **关键 D8**: 子 atom (L7/L9-16/L18/L20-22) parent_section **inherit chapter root** = `§8 [Representing Relationships and Data]` 而非 sub-namespace, per batch 01-04 ch04 v2 precedent + 修正 pilot F-P2P-002)
- **L165/167/169 LIST_ITEM ordered "1./2./3."** + **bold-prefix** `**ONE and ONE.**` (验 ordered LIST_ITEM atom_type per Axis 5 codification batch 47b precedent; bold-prefix preserved verbatim byte-exact)
- **L206 H3 numberless `### Key Rules`** sib=2 under §8.4 (S-02 验; positioned between §8.4.1 spec table and §8.4.2 numbered H3 — verify sib chain 数: §8.4.1=sib=1 numbered + Key Rules=sib=2 numberless + §8.4.2=sib=3 numbered + §8.4.3=sib=4 + §8.4.4=sib=5; mixed sib chain numbered+numberless under §8.4)
- **L389 NOTE blockquote `> **Note:**`** atom_type **NOTE** (验 D7 NEW blockquote-prefix bold-Note carve-out; parent_section `§8.8 [Related Specimens (RELSPEC)]`; verbatim 含 `> **Note:** ` prefix byte-exact)
- **L391 H3 numberless `### RELSPEC — Description/Overview`** sib=1 under §8.8 (验 em-dash `—` 在 heading text byte-exact; sib chain S-02 验 §8.8 下 4 numberless H3 chain L391/L395/L408/L414 sib=1/2/3/4)
- **L418 SENTENCE bold-caption `**Figure. Sample Specimen Relationship**`** + **L420-426 FIGURE atom** (验 caption-then-figure pattern; figure_ref pattern `md_ch08_specimen_relationship` 或 `md_ch08_relspec_lineage` 类似 descriptor)
- **末原子 L439 TABLE_ROW** relspec.xpt row 6 (ch08 文件末; pipe-delimited byte-exact)

---

## 3. Hook A4 inline (FIGURE figure_ref 校验)

每 atom_type=FIGURE 必满足: figure_ref 非 null + pattern `md_ch08_<descriptor>`.

**预期: ch08 全文 1 FIGURE** (L420-426 mermaid block)
- atom_id 形如 `md_ch08_aXXX` (single-digit-padded sequence)
- figure_ref 推荐: `md_ch08_relspec_specimen_relationship` 或 `md_ch08_specimen_lineage` (descriptor 描 mermaid 内容: 5 specimen nodes hierarchical lineage)
- caption_text 推荐: `"Figure. Sample Specimen Relationship"` (来自 L418 bold-caption SENTENCE 上一行; 与 figure_ref 双轨)
- verbatim 含整 mermaid block (L420 ` ```mermaid` 起 至 L426 ` ``` ` 止) byte-exact
- line_start=420 / line_end=426

---

## 4. atom_type 决策 (本 batch 关键)

| Source 形态 | atom_type | 注 |
|---|---|---|
| `# SDTMIG v3.4 — Chapter 8: Representing Relationships and Data` (L1) | HEADING h_lvl=1 sib=1 | parent_section `§8 [Representing Relationships and Data]` simplified per batch 05-08 |
| `## Overview` (L5) | HEADING h_lvl=2 sib=1 | **D8 NEW**: numberless `## Overview` H2; parent_section 自身 = `§8 [Representing Relationships and Data]` (chapter root); 子 atom parent_section **inherit chapter root** (NOT sub-namespace `§8.0 [Overview]`); per batch 01-04 ch04 v2 precedent + 修正 pilot F-P2P-002 non-canonical N27 |
| `## 8.X ...` (L26/63/144/175/256/275/328/387) | HEADING h_lvl=2 sib=2/3/4/5/6/7/8/9 | **关键**: 与 L5 ## Overview 共 sib chain (sib=1..9 in order of appearance); parent_section bracketed form `§8.1 [Relating Groups of Records Within a Domain Using --GRPID]` 等; 子 atom parent_section = `§8.1 [...]` etc. |
| `### 8.X.Y ...` (L32/76/98/150/187/213/219/245/277/287/291) | HEADING h_lvl=3 numbered | parent `§8.X [...]`; sib 由各 §8.X parent 内顺序 (e.g., §8.4 下 sib=1 §8.4.1, sib=2 ### Key Rules numberless, sib=3 §8.4.2, sib=4 §8.4.3, sib=5 §8.4.4) — **混合 sib chain** numbered + numberless 位置敏感 |
| `### Key Rules` (L206) | HEADING h_lvl=3 numberless | parent `§8.4 [...]`; sib=2 (between §8.4.1 sib=1 + §8.4.2 sib=3); 混合 sib 关键 (S-02 extension) |
| `### Specification` `### Assumptions` `### Example` (L330/340/351 §8.7) | HEADING h_lvl=3 numberless | parent `§8.7 [Related Subjects (RELSUB)]`; sib=1/2/3 (S-02 全 numberless 3-chain) |
| `### RELSPEC — Description/Overview` `### Specification` `### Assumptions` `### Example` (L391/395/408/414 §8.8) | HEADING h_lvl=3 numberless | parent `§8.8 [Related Specimens (RELSPEC)]`; sib=1/2/3/4 (S-02 全 numberless 4-chain); L391 含 em-dash `—` byte-exact |
| `---` (L24/61/142/173/254/273/326/385) | **不 emit** | 8 个 horizontal rule skip per batch 02-08 directive |
| `> **Note:** ...` (L389) | **NOTE atom_type** (**D7 NEW**) | **D7 NEW v1.9.1 codify candidate**: blockquote-prefix bold-Note `> **Note:**` 形态 — extends 既有 inline `**Note:**` carve-out NOTE 到 blockquote container variant; verbatim 含 `> ` blockquote prefix + `**Note:** ` bold markers byte-exact preserved; parent `§8.8 [Related Specimens (RELSPEC)]`; 与 batch 02-04 inline `^**Note:**` 严格区分 (本 batch 0 inline `**Note:**`) |
| 5 spec tables (RELREC L86-94 / SUPP-- L191-202 / RELSUB L332-338 / RELSPEC L399-406) + 9 example tables + 1 question table (L308-315) | TABLE_HEADER + TABLE_ROW | 标准 multi-col spec/example tables; C-5/A1 hook span ≤1 byte-exact |
| Spec tables 含 `^1^` footnote SENTENCE (L96/204) | SENTENCE | 含 `^1^` superscript byte-exact preserved (asterisk legend 注脚); 不 emit 为 TABLE_ROW; parent_section = 当前 §8.X.Y |
| Caption-then-table SENTENCE: "cm.xpt:" / "relrec.xpt:" / "suppae.xpt:" / etc. (L44/106/119/131/154/225/234/360/374/430) | SENTENCE | plain-text caption (非 bold) 引导后续 table; SENTENCE atom_type; parent_section per 当前 §8.X / §8.X.Y |
| Bold-caption SENTENCE `**Rows N-M:**` / `**Row N:**` / `**Example N:**` / `**Figure. ...**` (L36/38/40/42 + L100/102/104/117/129 + L152 + L223/232 + L357/358 + L370/371/372 + L418 = 17 instances) | SENTENCE | **bold-caption SENTENCE rule** per batch 06/07 codification: bold markers `**` preserved verbatim byte-exact; SENTENCE atom_type (NOT HEADING, NOT NOTE); parent_section per 当前 §8.X / §8.X.Y |
| Bold-prefix list items `- **Section 8.X**, ...` (L9-16 Overview) + `- **xxx (--SEQ)** ...` (L20-22) | LIST_ITEM | bullet `- ` + bold-prefix preserved; LIST_ITEM atom_type; parent_section `§8 [Representing Relationships and Data]` (chapter root per D8) |
| Ordered list bold-prefix `1. **ONE and ONE.** ...` `2. **ONE and MANY.** ...` `3. **MANY and MANY.** ...` (L165/167/169) | LIST_ITEM | **ordered LIST_ITEM** per Axis 5 codification batch 47b precedent (round 14 v1.9 N6-extension); ordering "1." prefix preserved verbatim; bold-prefix term preserved; parent `§8.3 [Relating Datasets Using RELREC]` |
| Ordered list plain `1. ... 2. ... 3. ...` (L262-264 §8.5 + L268-269 §8.5 + L342-349 §8.7 + L410-412 §8.8) | LIST_ITEM | **ordered LIST_ITEM** consistent w/ Axis 5; "N." prefix preserved byte-exact; parent_section per 当前 §8.X / §8.X.Y |
| Inline bold within SENTENCE `**deprecated**` (L215) `**not**` (L247) `**attributions**` (L181) | SENTENCE (no special handling) | inline bold 在 narrative SENTENCE 中 (非 caption); 不 emit 单独 atom; bold markers preserved verbatim |
| Mermaid block L420-426 | **FIGURE** (1 atom) | atom_type FIGURE; figure_ref `md_ch08_<descriptor>` 必填 (Hook A4); verbatim 含整 ```mermaid block``` byte-exact 包 fence |
| Bold caption "**Figure. Sample Specimen Relationship**" L418 | SENTENCE | 是 bold-caption SENTENCE (与 mermaid FIGURE 分离 atom; FIGURE-caption pair); parent_section `§8.8 [Related Specimens (RELSPEC)]` |

### 关键决策 D8 NEW: numberless `## Overview` H2 parent_section format (v1.9.1 codify candidate)

L5 `## Overview` 是 ch08 (也 ch04) 唯一 numberless H2 in chapters/. 处置:
- L5 H2 atom 自身 parent_section = `§8 [Representing Relationships and Data]` (chapter root)
- L5 H2 atom sib_index = 1 (与 L26/63/144/175/256/275/328/387 共 sib chain, 顺序 1-9)
- L5 H2 children atoms (L7 narrative + L9-16 8 LIST_ITEM + L18 narrative + L20-22 3 LIST_ITEM) parent_section **inherit chapter root** = `§8 [Representing Relationships and Data]` (NOT sub-namespace `§8.0 [Overview]` 或 `§8.Overview [Overview]`)
- 理由: pilot F-P2P-002 PARTIAL `§4.1 [OVERVIEW]` / `§4.0 [Overview]` 被 reviewer 标记 "convention is non-canonical per N27"; 后续 v2 batch 01-04 ch04 已修正为 chapter root inherit; 本 batch 沿用同一 convention 保 cross-batch consistency
- v1.9.1 候选 +1 codify D8: "numberless `## Overview` H2 numberless H2 sib chain + chapter root inherit for children"

### 关键决策 D7 NEW: blockquote-prefix bold-Note `> **Note:**` atom_type=NOTE (v1.9.1 codify candidate)

L389 `> **Note:** BE, BS, and RELSPEC domain specifications, ...`:
- atom_type = **NOTE** (extends 既有 inline `^**Note:**` carve-out NOTE 到 blockquote container variant)
- verbatim 含 `> ` blockquote prefix + `**Note:** ` bold markers byte-exact preserved (整行从 `>` 起到 SDTMIG. 句末)
- parent_section = `§8.8 [Related Specimens (RELSPEC)]` (定位在 H2 §8.8 之下, ### RELSPEC — Description/Overview 之前)
- 与 inline `^**Note:**` 形态 (batch 02-04 carve-out, 0 行无 `>` prefix) 严格区分 — 本 batch ch08 0 个 inline `**Note:**`, 仅 1 个 blockquote variant
- v1.9.1 候选 +1 codify D7: "blockquote-prefix bold-Note `> **Note:**` extends inline carve-out to blockquote container variant; verbatim 含 `> ` prefix"

### 关键决策: §8.4 混合 sib chain (numbered + numberless)

§8.4 [Relating Non-standard Variable Values to a Parent Domain] 下 H3 chain:
- L187 ### 8.4.1 Supplemental Qualifiers (SUPP--) — numbered sib=1
- L206 ### Key Rules — numberless sib=2 (S-02 extension; positioned between §8.4.1 spec content + §8.4.2)
- L213 ### 8.4.2 Submitting Supplemental Qualifiers in Separate Datasets — numbered sib=3
- L219 ### 8.4.3 Examples — numbered sib=4
- L245 ### 8.4.4 When Not to Use Supplemental Qualifiers — numbered sib=5

混合 sib 数 5 (1 numberless + 4 numbered, 顺序 1-5). 子 atom parent_section 应根据当前 H3 anchor:
- L208-211 4 LIST_ITEM Key Rules → parent `§8.4 [Relating Non-standard Variable Values to a Parent Domain]` (Key Rules 是 numberless H3, 子 atom inherit §8.4 chapter sub-section root, 同 D8 模式)
- 或: L208-211 4 LIST_ITEM parent `§8.4 / Key Rules` slash-separated form (alternative; non-canonical per N27)
- **推荐**: §8.4 / Key Rules 子 atom parent `§8.4 [Relating Non-standard Variable Values to a Parent Domain]` (chapter sub-section root inherit; consistent w/ D8)

§8.7 / §8.8 全 numberless H3 chain 不混合, 子 atom parent_section 同样 inherit §8.7 / §8.8 chapter sub-section root.

---

## 5. Dispatch 模板 — **FALLBACK PATH** sustained 6-batch (会变 7-batch post 本 batch — B-02 cycle 全闭)

派 `general-purpose` 单 dispatch.

1. Schema-first 头部
2. parent_section canonical bracketed format
3. 本 batch 特定:
   - file: `knowledge_base/chapters/ch08_relationships.md`
   - line range: **1-439 (全文)**
   - atom_id prefix: `md_ch08_a` 从 `a001`
   - batch_id: `P2_B-02_batch_09`
   - 输出: `evidence/checkpoints/P2_B-02_batch_09_md_atoms.jsonl`
   - extracted_by.subagent_type: `"general-purpose"`
   - extracted_by.prompt_version: `"P0_writer_md_v1.9"` (canonical literal per Hook 22 N round 14 codification)
   - extracted_by.ts: RFC3339 timestamp 必填
4. 22 hooks self-validate
5. **§4 atom_type 决策 + D7 NEW blockquote-NOTE + D8 NEW numberless-Overview-chapter-root + bold-caption SENTENCE rule + ordered LIST_ITEM Axis 5 + §8.4 混合 sib chain + FIGURE figure_ref + S-02 §8.7/§8.8 numberless H3 chains 全粘**
6. **关键警告**: 本 batch 是 P2 chapters/ 首次 mermaid FIGURE + 首次 blockquote-NOTE; writer 务必双倍校验 verbatim byte-exact (mermaid block 含 escape characters \\n, blockquote 含 `> ` prefix), figure_ref 非 null 必校 Hook A4

---

## 6. Rule A 跟进 — **FALLBACK PATH**

派 `pr-review-toolkit:code-reviewer`. 11-atom 分层独审 (8 boundary per §2.2.5 + 3 stratified)

Stratified 分层 sample 提议 (随机 seed=20260505_batch09):
- 1 atom from §8.1/8.2/8.3 group (前 §)
- 1 atom from §8.4/8.5/8.6 group (中 §)
- 1 atom from §8.7/8.8 group (末 §)

**总 sample = 8 boundary + 3 stratified = 11 atoms** (单批阈 N=10 略高; 加 1 因 batch 09 是 B-02 末 batch 多新 conventions 验)

---

## 7. PASS 后 append + checkpoint + B-02 cycle CLOSE

### 7.1 root pdf_atoms.jsonl 数据 append
- root append (~2520-2530 → ~2750-2800)
- atom_id 全 `md_ch08_a*` 0 collision 0 dup verify

### 7.2 audit_matrix.md update + ch08 milestone
- ch08 100% milestone (439/439 行 single dispatch)
- B-02 累计 6 文件全完: ch04 + ch01 + ch03 + ch02 + ch10 + ch08 = chapters/ 全 6 in-scope 100% atomized
- B-02 cycle CLOSED — 9 batch 全闭

### 7.3 trace.jsonl
- batch_complete event for batch 09
- phase_report event for B-02 cycle closure (重大 milestone)

### 7.4 _progress.json update
- batches_done = 9
- files_complete += ch08
- B-02 cycle status: CLOSED
- next_batch = N/A (B-02 全闭, 待 cumulative audit + retro + v1.9.1 cut)

### 7.5 写 batch_09_report.md
含:
- 8 节 standard report
- D7 + D8 NEW 决策详细 + verbatim evidence
- B-02 cycle 全闭描述 (~2,830-2,870 atoms 估累计 across 9 batches; 9/9 PASS chain)
- v1.9.1 候选 backlog 升至 **19** (post batch 09 +D7 +D8 = 17→19)
- B-02 cumulative audit + retrospective + v1.9.1 cut 触发条件 verify

### 7.6 (post batch 09) B-02 cycle CLOSE 后续动作
1. **B-02 cumulative audit** (30-atom stratified cross-batch per Rule A, B-01 retro 模式)
2. **B-02 RETROSPECTIVE.md** (Rule C 4 sections: 保留做法 / 缺口 / 决策 / 量化; 含 D5/D6/D7/D8/S-02 codify history + 3 kickoff drift catch + Rule B exemplary handling x3)
3. **v1.9.1 cut session** (19 候选: 1 CRITICAL kickoff self-consistency + D5/D6/D7/D8 codify + bold-caption rule + KB cleanup ch03 L117 + ordered LIST_ITEM Axis 5 + ...)

---

*Kickoff written 2026-05-05. Source 已实测 read 439 行 + 实数 9 H2 (1 numberless + 8 numbered) + 19 H3 (11 numbered + 8 numberless) + 8 HR + 15 表 (15 TABLE_HEADER + 84 TABLE_ROW) + 1 mermaid FIGURE (L420-426) + 1 blockquote-NOTE (L389) + 17 bold-caption SENTENCE + 29 unordered + 19 ordered LIST_ITEM 全 grep 校验 byte-exact. FALLBACK 路径 sustained 6-batch (会变 7-batch post 本 batch). B-02 cycle 最后 batch — 闭后触发 cumulative audit + retro + v1.9.1 cut.*
