# P2 B-02 batch 03 — Multi-Session Kickoff

> 创建: 2026-05-04 (post `P2_B-02_batch_02` 全闭环 commit 79a4a75, batch 02 238 atoms Rule A 10/10 100%)
> 父 kickoff: `multi_session/P2_B-02_kickoff.md` (umbrella §3 第 3 行)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` + 本 kickoff §3 inline 头部
> 路由词: 用户说 **"P2 bulk B-02 batch 03 开始任务"** 即触发 dispatch

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_kickoff.md` (umbrella, 本 batch 的语境框架, 特别是 §3 表 + §5 schema-first 模板 + §6 parent_section canonical format)
2. `subagent_prompts/P0_writer_md_v1.9.md` (主体 prompt) + `P0_reviewer_v1.9.md` (Rule A 用)
3. `schema/atom_schema.json` v1.2 frozen
4. `evidence/checkpoints/P2_B-02_batch_02_report.md` + `rule_a_P2_B-02_batch_02_summary.md` (前 batch 末态 + Rule A 通过项参考)
5. 本 kickoff (本身)

---

## 2. Batch 03 任务

### 2.1 Target

- **文件**: `knowledge_base/chapters/ch04_general_assumptions.md`
- **切片**: lines **901-1200** (300 行) = ch04 4 段中的第 3 段
- **估 atoms**: ~230-260 (batch 02 实测 238 / 300 行 = density 0.79; 本 batch 含 3 mermaid + 多 H3/H4 transitions + 4 数据表 + 1 大 crossover trial 表 ~40 行 → density 持平或略高)
- **atom_id 起始**: `md_ch04_a653` (续 batch 02 a652)

### 2.2 Continuity context (从 batch 02 a652 接续)

batch 02 末原子状态 (从 `evidence/checkpoints/P2_B-02_batch_02_md_atoms.jsonl` tail 读出):

```
a652 L900 LIST_ITEM | parent='§4.4.7 [Use of Relative Timing Variables]' | h_lvl=null sib=null
      verbatim: "- **Concomitant Medications (--STRF/--ENRF):** --STRF = \"BEFORE\", --ENRF = \"DURING\""
a651 L899 LIST_ITEM | parent='§4.4.7 [Use of Relative Timing Variables]'
a650 L898 SENTENCE | parent='§4.4.7 [Use of Relative Timing Variables]' (verbatim "**Example applications:**")
```

源 line 901-920 内容 prefix (写手必读以定 boundary):

```
L901: "- **Adverse Events (--ENRTPT):** --ENRTPT = \"ONGOING\", --ENTPT = \"DATE OF LAST DOSE\""
        ↑ 注: L900/L901 同一缩进级 `- ` (顶级), sub-bullets of L898 "**Example applications:**" 列举;
          batch 02 a652 emit 了 L900 这一条; L901 须 batch 03 续 emit, atom_id a653, parent 仍 §4.4.7
L902: ""
L903: "**Example 1: Medical History**"  ← SENTENCE bold caption (Hook C-6: ≠ HEADING) parent §4.4.7
L904: ""
L905: "CRF contains \"Year Started\"..."  ← SENTENCE narrative
L906-909: "- MHDTC = ..." 4 LIST_ITEM
L910: ""
L911-920: ```mermaid graph LR ... ```  ← **FIGURE atom!** parent §4.4.7
L921: italic caption "*Medical event began...*"  ← SENTENCE (NOTE? italic alone is SENTENCE per v1.9)
```

**进 batch 03 时 active context**:
- L1 active: `§4 [General Assumptions]` (pilot a001 H1 sib=1)
- L2 active 在 a652 末: `§4.4 [Use of Timing Variables]` (sib=4 from batch 02 a474 H2 §4.4)
- L3 active 在 a652 末: `§4.4.7 [Use of Relative Timing Variables]`
- 续 emit a653=L901 LIST_ITEM under §4.4.7
- a654 起 = L903 SENTENCE `**Example 1: Medical History**` (bold-only ≠ HEADING per Hook C-6, parent §4.4.7)
- L911-920 mermaid block = **1 FIGURE atom**, parent §4.4.7, **figure_ref 必填** (see §3 Hook A4 + §4)

**主要结构 transitions (本 batch 内多个 H2/H3/H4)**:

| Line | atom_type | content | parent_section / sib_index |
|---|---|---|---|
| L941 | HEADING h_lvl=3 | `### 4.4.8 Date and Time Reported in a Domain Based on Findings` | parent `§4.4 [Use of Timing Variables]` sib=8 (1-based) |
| L960 | HEADING h_lvl=3 | `### 4.4.9 Use of Dates as Result Variables` | parent `§4.4 [...]` sib=9 |
| L972 | HEADING h_lvl=3 | `### 4.4.10 Representing Time Points` | parent `§4.4 [...]` sib=10 |
| L986-991 | FIGURE | mermaid graph LR REF → CTP | parent `§4.4.10 [Representing Time Points]`, figure_ref required |
| L1070 | HEADING h_lvl=3 | `### 4.4.11 Disease Milestones and Disease Milestone Timing Variables` | parent `§4.4 [...]` sib=11 |
| L1076 | HEADING h_lvl=4 | `#### Disease Milestone Naming (MIDS)` | parent `§4.4.11 [...]` sib=1 (1-based RESTART under new H3 parent) |
| L1080 | HEADING h_lvl=4 | `#### Timing Relative to a Disease Milestone (MIDS, RELMIDS, MIDSDTC)` | parent `§4.4.11 [...]` sib=2 |
| L1098 | HEADING h_lvl=4 | `#### Use of Disease Milestone Timing Variables with Other Timing Variables` | parent `§4.4.11 [...]` sib=3 |
| L1108 | HEADING h_lvl=4 | `#### Linking and Disease Milestones` | parent `§4.4.11 [...]` sib=4 |
| L1115 | **不 emit** | `---` horizontal rule (markdown HR) | skip per batch 02 §2.2 directive |
| L1117 | HEADING h_lvl=2 | `## 4.5 Other Assumptions` | parent `§4 [General Assumptions]` sib=5 (1-based, §4.1=1 §4.2=2 §4.3=3 §4.4=4 §4.5=5) |
| L1119 | HEADING h_lvl=3 | `### 4.5.1 Original and Standardized Results` | parent `§4.5 [Other Assumptions]` sib=1 (RESTART) |
| L1123-1128 | FIGURE | mermaid graph LR ORRES → STRESC | parent `§4.5.1 [Original and Standardized Results]`, figure_ref required |
| L1145 | HEADING h_lvl=4 | `#### 4.5.1.3 Examples of Original and Standard Units and Test Not Done` | parent `§4.5.1 [...]` sib=1 (1-based RESTART; **MD 仅有 .3 子节, 无 .1/.2; sib 仍 1, 不为 3**) |

### 2.2.5 Boundary 末段 (L1196-1200, batch 03 closes mid-narrative-list)

```
L1196: ""
L1197: "**Example 3 (vs.xpt)**"  ← SENTENCE bold caption parent §4.5.1.3
L1198: ""
L1199: "- **Rows 1-2:** Numeric values were converted to standard units."  ← LIST_ITEM
L1200: "- **Row 3:** A result for VSTESTCD = \"HR\" is missing..."  ← LIST_ITEM **batch 末原子**
```

注: VS table 起 L1205 落入 batch 04, 不属本 batch. 末原子是 L1200 LIST_ITEM "Row 3" (mid-list 切, 4-7 进 batch 04). batch 04 将续 a???+1 = L1201 起.

**boundary critical (Rule A 必入 sample)**:
- **a653** L901 LIST_ITEM (跨 batch parent_section §4.4.7 续接) — **boundary 段首**
- **L911-920 FIGURE** (本 batch 第 1 mermaid, figure_ref 必填) — **schema-criticism boundary**
- **L941 HEADING h_lvl=3 §4.4.8** sib=8 (跨 batch H3 chain 持续 §4.4 parent) — **boundary structural cross-batch**
- **L1117 HEADING h_lvl=2 §4.5** sib=5 (mid-batch H2 大 transition) — **boundary structural mid-batch**
- **L1145 HEADING h_lvl=4 §4.5.1.3** sib=1 (1-based RESTART under new H3 parent; 注 MD 跳过 .1 .2 直接 .3, 但 sib 仍 1) — **anti-pattern guard**
- **末原子 ~a8?? L1200 LIST_ITEM** "Row 3" (boundary 段末 mid-list 切) — **batch 04 续接锚**

### 2.3 Dispatch 模板

派 `oh-my-claudecode:executor` 单 dispatch (同 batch 01/02 writer 类型, fresh dispatch 独立性 per Rule D §1.2; 同 type 不同 dispatch 计入同 slot 家族, Rule D 不撞). Dispatch prompt 顶部必须粘:

1. **Schema-first 头部** (`P2_B-02_kickoff.md` §5 完整 12-key 表 + atom_type 9-enum + Hook A4 + Hook C-8)
2. **parent_section canonical format** (`P2_B-02_kickoff.md` §6, chapters v1.8 bracketed `§<num>.<num> [<title>]`, 严禁 v1.9 spaced format)
3. **本 batch 特定**:
   - file: `knowledge_base/chapters/ch04_general_assumptions.md`
   - line range: **901-1200** (writer 须只读这 300 行 + 上文 §2.2 continuity context)
   - atom_id prefix: `md_ch04_a` 从 `a653` 起
   - batch_id: `P2_B-02_batch_03` (写到 trace.jsonl, 不入 atom 字段, schema 无)
   - 输出: `evidence/checkpoints/P2_B-02_batch_03_md_atoms.jsonl`
   - prompt_version (extracted_by): `"P0_writer_md_v1.9"`
4. **22 hooks self-validate** + **Hook A4 inline** (§3) + **L1115 `---` skip directive** (§2.2)
5. **3 个 mermaid block 必都 emit FIGURE atom 带 figure_ref** (本 batch 与 batch 02 最大差异, 切勿漏, 见 §4)

### 2.4 Rule A 跟进

派 `oh-my-claudecode:scientist` (fresh dispatch, 同 batch 01/02 reviewer 类型, Rule D 同家族延续 OK) 跑 10-atom 分层独审:

- 加载 `subagent_prompts/P0_reviewer_v1.9.md` (含 §R-C1 sub-line tolerance + §R-C3..C-7 anti-defect)
- 输入: `evidence/checkpoints/P2_B-02_batch_03_md_atoms.jsonl`
- 输出: `evidence/checkpoints/rule_a_P2_B-02_batch_03_verdicts.jsonl` + `_summary.md`
- gate ≥90% PASS
- **额外 boundary 必入 sample (5 atoms, 比 batch 02 多 2 因结构密度高)**:
  - **a653** (段首 LIST_ITEM 续 §4.4.7, 跨 batch parent 持续)
  - **L911-920 FIGURE** (figure_ref 校验, 本 batch 首引入 FIGURE 类型)
  - **L941 H3 §4.4.8** sib=8 (跨 batch H3 chain)
  - **L1117 H2 §4.5** sib=5 (mid-batch H2 大 transition + canonical bracketed)
  - **末原子 L1200 LIST_ITEM** (boundary 段末)
- **stratified 5 atoms 余样**: SENTENCE / TABLE_HEADER / TABLE_ROW / NOTE / 其余 H4 (e.g. §4.4.11 下 sub-headings)

### 2.5 PASS 后 append + checkpoint

PASS 后:
- cat `P2_B-02_batch_03_md_atoms.jsonl` → `md_atoms.jsonl` 追加 (`>> md_atoms.jsonl`)
- `wc -l md_atoms.jsonl` 验证累计 (post batch 02 close = 1536; post batch 03 应 ~1770-1796)
- `audit_matrix.md` P2 Bulk 表加 batch 03 行 (file / lines / atoms / Rule A 结果 / status)
- `trace.jsonl` 写 batch 03 phase_report 事件
- `_progress.json` 更新 last_completed_batch = "P2_B-02_batch_03"
- 写 `evidence/checkpoints/P2_B-02_batch_03_report.md` (atoms 总数 / atom_type 分布 / boundary 验证 / 与 batch 01/02 density 对比 / FIGURE atom 首引入说明)

---

## 3. Hook A4 inline (FIGURE figure_ref 校验) — **本 batch 高风险**

每 atom_type=FIGURE 必满足:
- `figure_ref` 非 null
- pattern: `md_ch04_<topic_slug>_concept_map` (canonical) 或 `md_ch04_<descriptor>` (alt)

**预期: ch04 lines 901-1200 内 FIGURE = 3** (3 个 mermaid block at L911-920 + L986-991 + L1123-1128).

建议 figure_ref 命名 (writer 自定, 与 model/* 同 stem 习惯一致):
- L911-920 → `md_ch04_medical_history_timing_concept_map` (内容: REF/YEAR/CTP nodes for Example 1 MH timing)
- L986-991 → `md_ch04_time_point_anchor_concept_map` (内容: REF → CTP elapsed time link, §4.4.10 总图)
- L1123-1128 → `md_ch04_findings_result_framework_concept_map` (内容: ORRES → STRESC → STRESN flow, §4.5.1 3-level framework)

writer 可调命名但必须 non-null + match pattern. Hook A4 拦截 null/empty.

---

## 4. atom_type 边界 cases (本 batch 预期)

| Source 形态 | atom_type | 注 |
|---|---|---|
| `- **Adverse Events ...**` (L901) | LIST_ITEM | 续 batch 02 a652 sub-bullets, parent §4.4.7 持续 |
| `**Example 1: Medical History**` (L903, L923, L933, L1149, L1178, L1197) | SENTENCE | bold-only caption ≠ HEADING (Hook C-6 PASS) |
| ```mermaid ... ``` 3 block (L911-920, L986-991, L1123-1128) | FIGURE | figure_ref 必填 (§3); 1 mermaid block = 1 FIGURE atom (verbatim 整 block) |
| 表 (3 rows L953-956, 5 rows L976-983, 4 rows L995-999, 4 rows L1005-1009, ~22 rows L1026-1046, ~22 rows L1049-1068, 4 rows L1084-1088, ~14 rows L1163-1176, ~9 rows L1187-1195) | TABLE_HEADER + TABLE_ROW | C-5 hook: TABLE_HEADER line_end-line_start ≤ 1; 跨多行表 1 TABLE_HEADER + N TABLE_ROW |
| `**Note:** ...` (L896, L958, L984, L1001, L1011) | NOTE | bold-Note prefix; C-6 PASS (≠ HEADING); 内含 cross-ref 不开 cross-refs 字段 (chapters 不强制) |
| `### 4.4.8 ...` `### 4.4.9 ...` `### 4.4.10 ...` `### 4.4.11 ...` (L941, L960, L972, L1070) | HEADING h_lvl=3 | parent `§4.4 [...]` sib 续 §4.4 H3 chain (L941=8 / L960=9 / L972=10 / L1070=11) |
| `## 4.5 Other Assumptions` (L1117) | HEADING h_lvl=2 | parent `§4 [General Assumptions]` sib=5 (5th H2 in §4 chain) |
| `### 4.5.1 ...` (L1119) | HEADING h_lvl=3 | parent `§4.5 [Other Assumptions]` sib=1 (RESTART under new H2 parent) |
| `#### 4.5.1.3 Examples of Original and Standard Units and Test Not Done` (L1145) | HEADING h_lvl=4 | parent `§4.5.1 [...]` sib=1 (1-based; **MD 跳 .1 .2 直接 .3, 但 sib_index 仍 1 因 MD tree 中是首 H4 child**) |
| `#### Disease Milestone Naming (MIDS)` 等 4 个 H4 (L1076-L1108) | HEADING h_lvl=4 | parent `§4.4.11 [...]` sib 1/2/3/4 (RESTART under new H3 parent) |
| `---` 水平分隔 (L1115) | **不 emit** | 非 content, schema 9-enum 无对应; writer 跳过 (§2.2 directive) |
| narrative paragraph (e.g. L905, L943, L949, L962-970, etc.) | SENTENCE (multi-atom 同 line_start 合法 per §R-C1 + R22) | sub-line SENTENCE byte-exact substring |
| `*Medical event began...*` italic caption (L921) | SENTENCE | italic-only ≠ NOTE/HEADING (per v1.9, italic 单独不打 NOTE 类型, 同 batch 02 经验) |
| `> Note that VSELTM is the planned elapsed time...` (L1001, L1011) | NOTE | block-quote prefix `> Note...` 是 NOTE form (Hook C-6 OK) |

---

## 5. 失败处理 (Rule B)

若 dispatch 或 Rule A FAIL:
- 写 `evidence/failures/P2_B-02_batch_03_attempt_<M>.md` 含输入/产物/技术判定/业务判定/下次输入
- attempt 2 调整后再派
- 连续 2 attempt FAIL → halt B-02, 评估 v1.9 prompt 是否需 cut v1.9.1 (重点: FIGURE figure_ref 命名规则若多次 ambiguous → cut 候选)

---

## 6. Recovery hint

若本 batch session 中断:
- writer 已派但未完: 看 trace.jsonl 末事件; checkpoint 文件存在则 partial recover, 不存在则重派
- writer 完但 reviewer 未派: 直接派 scientist, 无需重写
- reviewer FAIL: 走 Rule B 归档

---

*Kickoff written 2026-05-04 (post B-02 batch 02 闭环 commit 79a4a75). FIGURE atom 首引入 chapters/, Hook A4 高风险 batch — Rule A boundary sample 5 (vs batch 01/02 的 3) 应对.*
