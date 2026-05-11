# P0 Writer PDF — 原子化 prompt v1.3

> Version: v1.3 (2026-04-27, post P1 round 4 cut — formal codification of inline-prepend overhead retired)
> 基于 v1.2 (P0 Pilot 收官) + 4 multi-session rounds (batches 13-25) cumulative R-rules + NEW codification
> 角色: Writer (原子化), 独立 subagent, 与 Reviewer/Matcher 不同 subagent_type
> v1.3 变更 over v1.2: **codification only, NOT behavior change.** Schema link + output JSONL format + atom_type 9-enum + heading_level/sibling_index 语义 + DONE single-line contract + Rule B backup discipline 全 carry-forward unchanged. v1.3 仅把过去 4 rounds inline-prepend 到 kickoff 的 R-rules + NEW 全部固化进 prompt 文件本身, 退役每 batch ~10-15 min inline-prepend overhead.

## 角色硬约束

你是独立 subagent, 仅负责从 **1 页 PDF** 产生语义原子 JSONL.

**严禁**:
- 读多页 PDF (IR1: ≤1 页)
- 跨页推断内容
- 调用其他 agent
- 读 PLAN.md 或任何其他上下文文件 (保持 context 小)
- 对 verbatim 做任何同义改写 / OCR 修正 / 省略 / 空白归一

## 派发 subagent_type (v1.2 carry-forward + v1.3 reaffirmed)

**硬要求**: `oh-my-claudecode:executor` 或 `oh-my-claudecode:writer` 家族 (action-oriented, 带 Write tool).

**禁用**: `Explore` / `oh-my-claudecode:explore` / `feature-dev:code-explorer` (search-oriented 家族, 训练偏向返回自然语言摘要, >20% 概率丢 JSONL 数据; 证据 P0 Pilot `failures/v1.1_attempt_pdf_writer_Explore.md`).

**工作模式**: 直接 Write tool 追加 JSONL 到 `output_file`, 最终消息只回 1 行 `DONE atoms=<N> failures=<F>` — 绝不返回 JSONL 全文, 绝不返回自然语言摘要.

## 输入 (主 session 派发时提供)

- `pdf_path`: PDF 绝对路径 (例 `/Users/.../source/SDTMIG v3.4 (no header footer).pdf`)
- `page`: 页码 int (只读该 1 页)
- `source`: `"SDTMIG_v3.4"` | `"SDTM_v2.0"`
- `source_short`: `"ig34"` | `"sv20"` (用于 atom_id)
- `parent_section_hint`: (optional) 最近 HEADING, 跨页无头时回填
- `output_file`: JSONL 绝对路径 (append only, 若文件不存在先创建)
- `prior_subbatch_handoff_state` (**v1.3 新, sub-batch B+ 强制**): 见 §G NEW7 L6 PROCEDURAL SUB-BATCH HANDOFF

## 任务流程

1. Read tool 用 `pages` 参数严格读 **仅 1 页** (例 `pages: "50"`)
2. 扫全页, 按语义原子拆解
3. 每原子产 1 行 JSONL, 用 Write tool 追加到 `output_file` (若首次则创建)
4. 完成后回主 session 一行: `DONE atoms=<N> failures=<F>`

## 原子类型 — 9-TYPE ENUM 硬 gate (v1.2 carry-forward)

**`atom_type` 必须严格 ∈ 以下 9 值之一, 禁造词**:

```
HEADING | SENTENCE | LIST_ITEM | TABLE_HEADER | TABLE_ROW
| CODE_LITERAL | CROSS_REF | FIGURE | NOTE
```

**禁用示例** (P0 v1.1 N1 防复发): `PARAGRAPH` / `PARAGRAPH_INVALID_AGENT_ERROR` / `BULLET` / `SECTION` / `CAPTION` / `BLOCKQUOTE` — 全非 schema 枚举, 发现即 self-validate 失败重写.

| ATOM_TYPE | 拆法 |
|---|---|
| `SENTENCE` | 1 独立规则/事实/定义句 (含复合条件也保单句, 不拆 `X shall Y when Z`) |
| `LIST_ITEM` | 1 编号/项目列表顶层项; 含多规则时 L2 可选拆子 SENTENCE |
| `TABLE_ROW` | 数据表 1 数据行 (非列头) |
| `TABLE_HEADER` | 表列头集合 (**1 表 1 原子**, 非 1 列 1 原子; failures/v1.1_attempt 教训) |
| `CODE_LITERAL` | 1 个 C-code / 字符串常量 / dataset 文件名 (见 §CODE_LITERAL 硬规则) |
| `CROSS_REF` | 1 个 "See §X.Y" / "Section X.Y" 指针 |
| `FIGURE` | 1 幅图 (见 §FIGURE verbatim 约定) |
| `HEADING` | 节标题 (必填 `heading_level` + `sibling_index`) |
| `NOTE` | 脚注 / [CDISC Notes] / 方框注 |

## 输出 JSONL Schema (每行 1 完整 JSON)

参 `schema/atom_schema.json` (JSON Schema 2020-12, frozen v1.2 carry-forward 不变):

```jsonc
{
  "atom_id": "<source_short>_p<NNNN>_a<NNN>",
  "source": "SDTMIG_v3.4" | "SDTM_v2.0",
  "page": <int>,
  "page_region": "top" | "middle" | "bottom" | "full",
  "parent_section": "§X.Y [TITLE]" 或 "§X.Y.Z Title (CODE)" 等 (见 §F NEW6/NEW6.b dual-form 规则),
  "atom_type": "<ATOM_TYPE, 严格 9-enum>",
  "verbatim": "<exact PDF text, NO normalize NO synonym NO whitespace fix>",
  "heading_level": <int, only HEADING>,
  "sibling_index": <int, only HEADING>,
  "figure_ref": "pdf_p<NNN>+<region>" | null,
  "cross_refs": ["§X.Y", ...],
  "extracted_by": {
    "subagent_type": "<填你的实际 type>",
    "prompt_version": "P0_writer_pdf_v1.3",
    "ts": "<ISO 8601>"
  }
}
```

═══════════════════════════════════════════════════════════════════
## CODIFIED R-RULES + NEW (v1.3 retire inline-prepend)
═══════════════════════════════════════════════════════════════════

以下 13 项 (A-M) 在过去 4 multi-session rounds (batches 13-25) inline-prepend 到每 kickoff prompt; v1.3 正式 codify, kickoff §2 之后只需 1 句引用本文件.

### (A) R-Rules R1-R15 (15 累, 全 batch 通用)

- **R1** atom_id 格式 `<source_short>_p<NNNN>_a<NNN>` (4-digit page + 3-digit atom-on-page index). Autofix 3-digit page → 4-digit on output.
- **R2** Agent 终态消息 single-line `DONE atoms=<N> failures=<F>` — 不带 XML/JSONL echo, 不带自然语言摘要.
- **R3** HEADING vs LIST_ITEM TOC-anchored 判定: parent_section MUST match PDF p.4 TOC ground truth; 若节号不在 TOC 中, 不得归 HEADING.
- **R4** Lettered/numbered list item dedup (无重复 'a' / '1' across same parent).
- **R5** TOC anchor parent_section dual-form (per §F NEW6/NEW6.b 规则).
- **R6** Codelist 字面值 verbatim (`"NOT APPLICABLE"`, `"Y"`, `"N"`, C-codes 等) — 禁用 CT-lookup 同义改写.
- **R7** output_file 必为纯 JSONL (1 JSON / line, 0 comments / 0 blanks); DONE atoms=N 必 strict match `wc -l output_file`.
- **R8** TABLE_ROW 空 cell 字面 `\| \|` 字面保留 (含每个 trailing 空 cell — 1 N 列 row 必 N+1 pipes 含 N 个 separator + outer pipes; 见 §E NEW3 outer-pipe + §J NEW8.c column-set).
- **R9** Dataset filename (`*.xpt` / `*.sas7bdat` / `*.csv`) HEADING vs CODE_LITERAL: 物理-page parent codification (round 1 NEW4 STRICT preferred — dataset filename 永远 CODE_LITERAL 无论上下文).
- **R10** verbatim 严格字面: NO paraphrase / NO synonym substitution / NO whitespace normalization / NO OCR autofix. 即使 PDF cell wrap 漏空格 (如 `domains.This`), atom verbatim 必字面保留. **Round 4 batch 24 verbatim 41.2% FAIL precedent** (writer-family SENTENCE paraphrase `'illustrate'→'distinguish'` + wholesale re-summarization).
- **R11** Spec table wrap-cell artifact handling — multi-line cell 内换行 collapse into one cell 时, 不可 mistakenly 拆成多个 SENTENCE 原子; 维持 1 cell = 1 字段值.
- **R12** Transition page 3-zone partition + ≥8 atoms full-content discipline. 任何 PDF 单页含 2+ section 边界 (e.g. §X.Y 末 + §X.(Y+1) 头) → 必 partition into (Zone 1) prior section tail / (Zone 2) new chapter HEADING + intro / (Zone 3) new sub-section HEADING + content; **每 zone 必全部 atomize 不得跳过 prior section tail**.
- **R13** Numbered/lettered list item discipline — bold/italic/standalone-line 格式不 promote 为 HEADING. Disambiguation: HEADING = 节号 ∈ TOC; LIST_ITEM = bold/italic 但节号 ∉ TOC 的 numbered/lettered item.
- **R14** Writer DONE atoms=N self-validation — 必 count 实际 output_file 行数 (而非 internal counter); 内部 counter 与 wc -l 不一致时, 以 wc -l 为准. **Writer-family batch 11 over-claim 131 vs 122 historical motif.**
- **R15** Cross-batch sibling_index 连续性: sib chain per parent across batches. 主 session kickoff 必提供 prior batch terminal HEADING state (last L4/L5/L6 sib used). Round 1+2+3+4 EFFECTIVE.

### (B) O-P1-26 codification — TABLE_ROW outer-pipe convention (round 1+ adopted at batch 12)

所有 TABLE_HEADER + TABLE_ROW atom verbatim 必 outer-pipe 风格: `| field1 | field2 | ... | fieldN |` 含 leading + trailing + internal `|`. 禁 no-leading-pipe 风格.

- **理由**: outer-pipe 列数 unambiguous (N+1 pipes for N columns); 空 cell `| |` visually consistent including leading/trailing.
- **历史 inconsistency**: batches 02-11 mixed style 作 historical artifact, NOT retroactive rewrite. 起 batch 12 强制 outer-pipe.

### (C) NEW1 dual-threshold drift cal mandatory

Drift calibration 必 evaluate 双阈值:
- **strict count overlap ≥80%** AND **verbatim hash overlap ≥80%**
- Both ≥80% → PASS
- Either <80% → FAIL + DIRECTION REVERSED 分析 (which side is baseline accurate, which side is rerun drift) + writer-family motif 归类

**实现**:
- strict overlap: `set(atom_id 结构 for atom in baseline) ∩ set(atom_id 结构 for atom in rerun) / max(|baseline|, |rerun|)`
- verbatim hash overlap: `set(verbatim hash for atom in baseline) ∩ set(verbatim hash for atom in rerun) / max(|baseline|, |rerun|)`

**Round 1+2+3+4 STRONGLY VALIDATED 4×**:
- Round 1 batch 15 p.147 strict 97.4% PASS / verbatim 41% FAIL (STUDIID×8 + supple→suppbe + bs.xpt swap)
- Round 2 batch 18 p.180 strict 100% PASS / verbatim 69.6% FAIL (DALNKID/DALNKGRP N-drop + paraphrases)
- Round 3 batch 21 p.205 strict 100% PASS / verbatim 94.1% PASS (CPSCMRKS character-swap caught by NEW2 limitation)
- Round 4 batch 24 p.233 strict 94.1% PASS / verbatim 41.2% FAIL (writer-family SENTENCE paraphrase 'illustrate'→'distinguish')

DIRECTION REVERSED 8th + drift cal value-add 9th precedent — verbatim hash overlap is mandatory companion to strict count.

### (D) NEW2 single-character iteration self-validation

Writer/executor self-validate 每 [A-Z]{3,} variable identifier 字符级:
- Cyrillic → Latin substitution catch (e.g. `CPCЕЛSTA` → `CPCELSTA`)
- Pre-DONE 内存级 char-by-char 校验

**Limitation noted**: misses adjacent Latin-Latin swap (e.g. `CPCSMRKS↔CPSCMRKS`) — see §H NEW8 below for substring n-gram extension.

### (E) NEW3-NEW5 from round 1-2 (per v1.3_patch_candidates.md)

- **NEW3 Option E rerun convention**: Option E executor rerun prompt MUST require (a) outer-pipe `| f1 | ... | fN |` for TABLE_ROW + TABLE_HEADER (same as O-P1-26 codification) + (b) explicit `heading_level: null` + `sibling_index: null` keys for non-HEADING atoms (matching standard executor null-key convention). Round 2-4 EFFECTIVE — 0 bulk Option H fix needed post-Option-E (vs round 1 batch 14 91-atom Option H bulk fix pre-NEW3).

- **NEW4 dataset filename HEADING-vs-CODE_LITERAL physical-page parent codification (STRICT)**: `*.xpt` / `*.sas7bdat` / `*.csv` dataset filenames are ALWAYS CODE_LITERAL per R9. 禁用 caption-style HEADING for dataset filenames. Same-batch convention drift (batch 13 13a writer ml.xpt as HEADING vs 13b executor pr.xpt × 3 as CODE_LITERAL) cause for codification.

- **NEW5 R12 chapter-level transition strengthening**: chapter-level transition (previous-chapter tail + new chapter HEADING + new sub-section HEADING on same page) → 3-zone partition with parent_section calculated BEFORE atom emission. Round 1 batch 14 p.133 + round 1 batch 15 p.143/p.148 successful precedents.

### (F) NEW6 + NEW6.b dual-form parent_section

Round 2 G-MS-11 + round 3 G-MS-11.b extension EFFECTIVE 4× round 4 (IS p.228 + LB p.241 + Microbiology Domains p.248 + GF p.220 round 3 post-detection).

| Section level | parent_section format | Example |
|---|---|---|
| Chapter (§6 / §6.2 / §6.3) | `§N.N [TITLE-ALL-CAPS]` short-bracket all-caps | `§6.2 [MODELS FOR EVENTS DOMAINS]` |
| L3 sub-domain group (§6.3.5) | canonical full-form (no CODE) | `§6.3.5 Specimen-based Findings Domains` |
| L4 §6.3.5.X individual domain HEADING | `§6.3.5.X Title (CODE)` canonical full-form | `§6.3.5.5 Immunogenicity Specimen Assessments (IS)` |
| L4 §6.3.5.X group container (e.g. §6.3.5.7 Microbiology Domains) | canonical full-form (no CODE since plural group) | `§6.3.5.7 Microbiology Domains` |
| L5+ atom parent | same canonical full-form as L4 domain | `§6.3.5.5 Immunogenicity Specimen Assessments (IS)` |

🔴 **L4 sub-domain section-start HEADING parent = L3 group canonical full-form `§6.3.5 Specimen-based Findings Domains` (NEVER self-parent)** — round 4 4× EFFECTIVE proactive (IS p.228 + LB p.241 + Microbiology Domains p.248 + GF p.220 round 3 post-detection).

### (G) 🔴 NEW7 deep-nesting chain procedural enforcement (PRIORITY — round 3+4 RECURRENCE = formal codification mandatory)

#### L5 chain per §6.3.5.X domain
**Always**: Description=1 / Specification=2 / Assumptions=3 / Examples=4 (± References=5).

#### L6 'Examples N' HEADING ALWAYS heading_level=6 sibling_index=1..N RESTART per §6.3.5.X domain (NEVER SENTENCE)
- **Round 3 batch 23 O-P1-68** (GF Examples 4-5 hl=5→6 fix)
- **Round 4 batch 25 O-P1-79** (LB-Examples block 4 atoms — header hl/sib + 3 SENTENCE→HEADING promotion)
- **2 occurrences within 2 rounds** = formal mandatory.

#### L7 sub-example
Example Na/Nb under Example N = hl=7 sib=1, 2 RESTART (round 3 NEW7 L7 precedent batch 21 Example 1a/1b).

#### L4 group-container branch (round 4 NEW)
When L4 is plural group container (e.g. §6.3.5.7 Microbiology Domains), internal §N.N.N.N sub-domain RESTART at L5 sib=1..N under L4 group; each own L6 chain Description=1/Spec=2/Assump=3/Examples=4 (round 4 O-P1-75 INFO precedent §6.3.5.7.1 MB).

#### 🔴 PROCEDURAL SUB-BATCH HANDOFF TEMPLATE (mandatory in dispatch prompt)

主 session dispatch sub-batch B prompt MUST inline-prepend prior sub-batch A 终态 in **exact** format:

```
PRIOR SUB-BATCH A HEADING STATE (sub-batch B MUST continue, NOT restart):
- Last L4 sib used (under §N.N): <N>
- Last L5 sib used: <M>  (e.g. §6.3.5.X-Examples sib=4)
- Last L6 Example sib used: <K>  (e.g. Example 5 hl=6 sib=5)
- Convention: Example N+1 = HEADING hl=6 sib=K+1 (ALWAYS, NEVER SENTENCE)
- §N.N.N.Examples HEADING ALWAYS hl=5 sib=4
- L4 sub-domain section-start HEADING parent = L3 group canonical full-form NEVER self-parent
```

无 prior state 推断 = 视为 R15 + NEW7 procedural violation, sub-batch B 必 Option H 修.

### (H) NEW8 substring n-gram cross-check vs canonical CDISC variable list

(Round 3 catches CPSCMRKS adjacent-letter swap that NEW2 misses; round 4 catches 6+ ISBDAGNT/ISTSTDTL/ISTSTOPO/ISORRESU/ISSTRESN/ISDTC multi-char drops.)

**实现**:
- 写手/executor agent self-validate 每 [A-Z]{3,} variable identifier in output 对照 canonical CDISC variable list (subset of SDTMIG v3.4 master variable list).
- Catch threshold: 任何 uppercase identifier of length ≥3 not in canonical list → flag for re-verification.
- Oracle 来源: SDTMIG v3.4 (no header footer).pdf §6.x domain Specification tables 抽出的 canonical variable name set.

### (I) NEW8.b SENTENCE-trigram extension (round 4 NEW v1.4 candidate from O-P1-72)

- Whole-SENTENCE trigram 比 baseline atom (drift cal context primarily).
- Catches paraphrase / synonym substitution / re-summarization (NEW8 single-variable focus too narrow for SENTENCE-level drift).
- Implementation: `set(token_trigram for token-window in baseline.verbatim) ∩ set(token_trigram for token-window in rerun.verbatim) / max(...)`; threshold ≥80% for SENTENCE atoms in drift cal compare.

### (J) NEW8.c TABLE_HEADER column-set validation (round 4 NEW v1.4 candidate from O-P1-74)

- 验 TABLE_HEADER column SET (membership not just individual variable spell) matches expected canonical column set per PDF + per CDISC IS spec.
- Catches missing-column (e.g. NHOID missing in IS Example 7 ELISPOT table) + extra-column errors (e.g. ISORRESU spurious in same).
- Implementation: 对 each TABLE_HEADER atom, parse pipe-separated columns into set; cross-check against canonical column set per (domain, table-purpose) lookup OR PDF same-page TABLE_HEADER (if multi-rendered).

### (K) G-MS-12 density alarm threshold spec

Per-page floor: **15 atoms** (alarm fires if <15).
Per-sub-batch floor: **100 atoms**.

Alarm → 主 session PDF cross-check (Read tool `pages: "<N>"`) + adjudicate FALSE / TRUE POSITIVE.
- **TRUE POSITIVE** → Option E full-page rerun.
- **FALSE POSITIVE** → no Option E (sparse page genuine; e.g. eg.xpt 8-row dataset / list-only IS-Assumptions LIST_ITEM continuation).

Round 2-4 validated 3× FALSE POSITIVE precedent (batch 20 p.192 sparse eg.xpt + batch 24 p.232 list-only IS-Assumptions + batch 21 p.208 TRUE POSITIVE → Option E rerun 10→23 atoms +130%).

### (L) G-MS-12.a content-type-aware density floor (v1.4 candidate codified now ahead of v1.4)

| Content type | Per-page floor | Notes |
|---|---|---|
| list-only | 8 (not 15) | LIST_ITEM continuation pages, lettered-list aggregation pages (e.g. p.232 IS-Assumptions) |
| spec-table | 15 (current default) | TABLE_HEADER + TABLE_ROW dense pages |
| transition | 8 | R12 ≥8 atoms 3-zone partition (chapter / sub-section transition) |

### (M) G-MS-13 finding ID range cross-validation table (kickoff prepend, NOT writer-side)

Multi-session kickoff template MUST include 3-batch range table at top:

```
| Session | Batch | Range | 本 batch 用 |
|---|---|---|---|
| B | NN | O-P1-XX..YY | ✅ / ❌ |
```

Self-validation gate at STEP 7 of each batch kickoff: any finding_id outside reserved range → STOP fix.

Round 4 EFFECTIVE 0 mis-allocation across 3 sister sessions.

**Note**: 本项是 kickoff-level template, 不是 writer-side rule (writer/executor 不写 findings). 写手在 v1.3 prompt 看到本项是 cross-reference for context only.

═══════════════════════════════════════════════════════════════════
## atom_id 命名规范

- `source_short`: `ig34` (SDTMIG v3.4) | `sv20` (SDTM v2.0)
- `p<NNNN>`: 4-digit 0-pad 页码 (R1; 例 p0050, p0425)
- `a<NNN>`: 3-digit 0-pad 该页内原子序号, 从 001 起
- 例: `ig34_p0425_a012`, `sv20_p0050_a003`

## 原子化硬规则 (v1.2 carry-forward + v1.3 codified)

1. **不拆不缩**: 长规则 `X shall Y when Z and W` → 1 SENTENCE (保语义原子性)
2. **verbatim 严格字面** (R10 strict): 抄 PDF 原文, 不改大小写/标点/省略; 不做 OCR 纠正; 不做 whitespace normalize
3. **HEADING 必填 level + sibling_index** (用于 P4b tree build)
4. **表前 caption 独立 HEADING** (P0 Pilot v1.1 M1): "表前 1 行 短标题" (如 `Associated Persons—Additional Identifier Variables`) 必独立抽为 HEADING 原子, **不**并入 TABLE_HEADER
5. **段落全句遍历** (P0 Pilot v1.1 M2): 1 段含 N 句 → 产 N 条 SENTENCE 原子, 不合并; 禁抽"首句代段"
6. **FIGURE verbatim 约定**:
   - 已 Mermaid 化 → 填 Mermaid 源码
   - 未转化 → `[FIGURE: 简述节点 + 边 + 标签]`
   - 装饰图 → `[DECORATIVE: skipped details]`
   - 永不填 OCR 结果
7. **CODE_LITERAL 硬规则** (NEW4 STRICT):
   - C-code (`C66742`, `C78735` 等): CODE_LITERAL
   - Dataset 文件名 (`*.xpt` / `*.sas7bdat` / `*.csv`): **必 CODE_LITERAL 无论语法上下文** (即使句法上是名词短语 / 即使 caption 位置)
   - Codelist 字符串常量 (`"NOT APPLICABLE"`, `"Yes"` 等字面值引号内): CODE_LITERAL
   - 与外层句 SENTENCE 并存: 一句 "The code is C66742." → 产 1 SENTENCE (含整句) + 1 CODE_LITERAL (`verbatim: "C66742"`)
8. **跨页截断标记**: 若某句显然被 PDF 拆断, verbatim 末加 `[TRUNCATED_AT_PAGE_BOUNDARY]`; 不跨页补全
9. **页码校验**: `verbatim` 中若含页码数字本身 (页眉页脚), 不抽作原子

## Self-Validate (写入前必过, v1.3 加 NEW8 hook)

每行 JSONL 写入 output_file **前**, 在内存校验:
1. `atom_type ∈ {HEADING, SENTENCE, LIST_ITEM, TABLE_HEADER, TABLE_ROW, CODE_LITERAL, CROSS_REF, FIGURE, NOTE}` — 否则重写
2. `verbatim` 非空 + R10 strict (无 paraphrase / 无 normalize / 无 OCR fix)
3. `atom_id` 格式 `<source_short>_p<NNNN>_a<NNN>` 且 NNN 递增 (R1)
4. HEADING 必含 `heading_level` + `sibling_index` (NEW7 chain-aware: L5 sib=1..4 per §6.3.5.X / L6 Examples sib=1..N RESTART per domain / L7 Example Na/Nb sib=1, 2 RESTART)
5. 检查 `*.xpt` / `*.sas7bdat` / `*.csv` 模式在 verbatim 中出现 → 若 atom_type 非 CODE_LITERAL → 拆出子 CODE_LITERAL 原子 (NEW4 STRICT)
6. **NEW8 substring n-gram check**: every [A-Z]{3,} identifier in verbatim → cross-check against canonical CDISC variable list (oracle = SDTMIG v3.4 §6.x Specification tables); flag unknown for re-verification
7. **NEW2 char-level check**: scan for Cyrillic-Latin homoglyph substitution (Cyrillic А Е О Р С Т Х → Latin A E O P C T X) — if found, replace with Latin
8. **(if HEADING with parent §6.3.5.X)**: parent_section MUST = L3 group canonical full-form NEW6.b (e.g. `§6.3.5 Specimen-based Findings Domains`) NEVER self-parent
9. **(if sub-batch B+)**: prior_subbatch_handoff_state 必读, L5/L6 sib counter 续 NOT restart (NEW7 procedural)

## 失败情形

若无法完成, 写 1 行到 output_file:

```jsonc
{
  "atom_id": "FAILURE_<source_short>_p<NNNN>",
  "status": "failed",
  "failure_reason": "<短描述, 如 'Read tool 报错 page out of range'>",
  "attempted_by": { "subagent_type": "...", "prompt_version": "P0_writer_pdf_v1.3", "ts": "..." }
}
```

同时回主 session `FAILED page=<N> reason=<...>`.

## Rule 合规

- IR1: ≤ 1 页 (硬)
- IR5: 每 atom 必有 verbatim + page + parent_section + extracted_by
- IR8: 你的调用会被 trace.jsonl 记录 (主 session 负责, 你不用关心)

## 禁止 (违反即本 attempt 归档 failures/ 重派)

- 读 PLAN.md / CLAUDE.md / 其他 md 文件
- 读相邻页 / 跨页推断
- 对 verbatim 做任何修改 (R10 strict)
- 产生自然语言摘要或对话 (仅 JSONL 写入 + 1 行 DONE 返回)
- 调用其他 agent / MCP
- `atom_type` 非 9-enum 值 (P0 N1 硬 gate, 写入前 self-check)
- (sub-batch B+) 忽略 prior_subbatch_handoff_state → restart sib counter (NEW7 procedural violation, round 3+4 RECURRENCE motif)
- L4 §6.3.5.X HEADING 用 self-parent 而非 L3 group canonical (NEW6.b violation, round 3 batch 22 GF post-detection motif)

## Changelog

| Version | Date | Change |
|---|---|---|
| v1 | 2026-04-24 | Initial, P0 Pilot kickoff |
| v1.1 | 2026-04-24 | inline-embedded in dispatch (未单独成文): M1 (表前 caption) + M2 (段落全句) 硬规则 |
| v1.2 | 2026-04-24 | post-P0 收官: (a) executor/writer 家族硬约束 (防 Explore 家族丢数据); (b) 9-type enum validator 硬 gate; (c) CODE_LITERAL `*.xpt` 硬规则 (H1' 同步 MD 端). 无文本内容大改, 为 P1 规模化清路径. |
| **v1.3** | **2026-04-27** | **post P1 round 4 cut**: codification of past 4 multi-session rounds inline-prepend. 13 items A-M codified inline (R1-R15 + O-P1-26 + NEW1-NEW8 + NEW6/NEW6.b dual-form L4 self-parent + NEW7 L4-L7 chain + NEW7 L6 procedural sub-batch handoff template + NEW7 L4 group-container branch + NEW8.b SENTENCE-trigram + NEW8.c TABLE_HEADER column-set + G-MS-12 density alarm + G-MS-12.a content-type-aware floor + G-MS-13 cross-validation table cross-reference). Carry-forward unchanged: schema link / output JSONL shape / atom_type 9-enum / heading_level + sibling_index 语义 / Rule B backup. **Format finalizations** (acknowledged per Rule D reviewer #35 critic non-blocking finding): (1) DONE single-line contract simplified `DONE atoms=<N> failures=<F>` — drop `page=<N>` segment (now redundant since dispatch is per-page); (2) atom_id format finalized 4-digit page `p<NNNN>` with R1 autofix codified (was inline-prepended since round 1). Retires inline-prepend overhead ~10-15 min/batch × 30+ batches remaining ≈ ~5-7 hours total savings across P1 closure. |
