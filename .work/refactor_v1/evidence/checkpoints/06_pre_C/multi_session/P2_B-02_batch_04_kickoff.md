# P2 B-02 batch 04 — Multi-Session Kickoff

> 创建: 2026-05-04 (post `P2_B-02_batch_03` 全闭环 commit 3b4c546, batch 03 227 atoms Rule A 10/10 100% via FALLBACK general-purpose + pr-review-toolkit:code-reviewer)
> 父 kickoff: `multi_session/P2_B-02_kickoff.md` (umbrella §3 第 4 行)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` + 本 kickoff §3 inline 头部
> 路由词: 用户说 **"P2 bulk B-02 batch 04 开始任务"** 即触发 dispatch
> **本 batch = ch04 末段** (195 行, 完成 ch04 全文 1395/1395 = 100%)

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_kickoff.md` (umbrella, 本 batch 的语境框架, §3 表 + §5 schema-first 模板 + §6 parent_section canonical format)
2. `subagent_prompts/P0_writer_md_v1.9.md` (主体 prompt) + `P0_reviewer_v1.9.md` (Rule A 用)
3. `schema/atom_schema.json` v1.2 frozen
4. `evidence/checkpoints/P2_B-02_batch_03_report.md` + `rule_a_P2_B-02_batch_03_summary.md` (前 batch 末态 + Rule A 通过项参考 + FALLBACK 决策记录)
5. 本 kickoff (本身)

---

## 2. Batch 04 任务

### 2.1 Target

- **文件**: `knowledge_base/chapters/ch04_general_assumptions.md`
- **切片**: lines **1201-1395** (195 行) = ch04 4 段中的第 4 段 (末段)
- **估 atoms**: ~140-180 (基于 batch 02 0.79 / batch 03 0.757 density; 本 batch 含 8 数据表 + 9 H3/H4 transitions + 多 narrative 段; table-heavy 段 density 持平 batch 03)
- **atom_id 起始**: `md_ch04_a880` (续 batch 03 a879)
- **特殊**: ch04 全文末 batch — 完成后 ch04 1395/1395 = 100% 全文原子化

### 2.2 Continuity context (从 batch 03 a879 接续)

batch 03 末原子状态 (从 `evidence/checkpoints/P2_B-02_batch_03_md_atoms.jsonl` tail 读出):

```
a879 L1200 LIST_ITEM | parent='§4.5.1.3 [Examples of Original and Standard Units and Test Not Done]' | h_lvl=null sib=null
      verbatim: "- **Row 3:** A result for VSTESTCD = \"HR\" is missing, as indicated by VSSTAT = \"NOT DONE\"; neither VSORRES nor VSSTRESC is populated."
```

源 line 1201-1220 内容 prefix (写手必读以定 boundary):

```
L1201: "- **Rows 4-5:** Two measurements for VSTESTCD = \"SYSBP\" were done at visit 1."
        ↑ 续 batch 03 a879 同 indent `- ` (顶级 list under §4.5.1.3 Example 3 narrative); a880 = LIST_ITEM parent §4.5.1.3
L1202: "- **Row 6:** A third measurement for VSTESTCD = \"SYSBP\" at visit 1 was a derived record, as indicated by VSDRVFL = \"Y\"."  ← LIST_ITEM
L1203: "- **Row 7:** At visit 2, there were no Vital Signs results, as indicated by VSTESTCD = \"VSALL\" and VSSTAT = \"NOT DONE\"."  ← LIST_ITEM
L1204: ""
L1205-1206: VS table header + separator (TABLE_HEADER) parent §4.5.1.3
L1207-1213: VS table 7 data rows (TABLE_ROW × 7) parent §4.5.1.3
L1214: ""
L1215: ""
L1216: "### 4.5.2 Linking Multiple Observations"  ← **H3 transition** sib=2 under §4.5
L1217: ""
L1218: "See Section 8, Representing Relationships and Data, for guidance on expressing relationships among multiple observations."
        ↑ **可能首 CROSS_REF atom in batch** (cross-ref to Section 8); 但若 writer 判 SENTENCE 含 inline ref 也合规 — 见 §4 决策
L1219: ""
L1220: "### 4.5.3 Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables"  ← H3 sib=3
```

**进 batch 04 时 active context**:
- L1 active: `§4 [General Assumptions]` (pilot a001 H1 sib=1)
- L2 active 在 a879 末: `§4.5 [Other Assumptions]` (sib=5 from batch 03 a814 H2 §4.5)
- L3 active 在 a879 末: `§4.5.1 [Original and Standardized Results]`
- L4 active 在 a879 末: `§4.5.1.3 [Examples of Original and Standard Units and Test Not Done]`
- 续 emit a880=L1201 LIST_ITEM under §4.5.1.3
- a881=L1202 LIST_ITEM, a882=L1203 LIST_ITEM (续 Example 3 vs.xpt narrative bullets)
- a883=L1205-1206 TABLE_HEADER (VS table 11 cols), parent §4.5.1.3
- a884..a890=L1207-1213 TABLE_ROW × 7 (VS table data, 含 null cells L1209/L1212/L1213)
- a891=L1216 HEADING h_lvl=3 §4.5.2 (active L3 跳出 §4.5.1 → §4.5.2; **sib=2** 1-based, 续 §4.5 下 H3 chain §4.5.1=1, §4.5.2=2)
- a892=L1218 CROSS_REF (suggested) 或 SENTENCE 内含 ref ("See Section 8, ...") parent §4.5.2 — 见 §4 atom_type 决策
- a893=L1220 HEADING h_lvl=3 §4.5.3 sib=3

**主要结构 transitions (本 batch 内多个 H3/H4)**:

| Line | atom_type | content | parent_section / sib_index |
|---|---|---|---|
| L1216 | HEADING h_lvl=3 | `### 4.5.2 Linking Multiple Observations` | parent `§4.5 [Other Assumptions]` sib=2 (续 §4.5 H3 chain; §4.5.1=1, §4.5.2=2) |
| L1220 | HEADING h_lvl=3 | `### 4.5.3 Text Strings that Exceed the Maximum Length for General Observation-class Domain Variables` | parent `§4.5 [Other Assumptions]` sib=3 |
| L1222 | HEADING h_lvl=4 | `#### 4.5.3.1 Test Name (--TEST) Greater than 40 Characters` | parent `§4.5.3 [...]` sib=1 (RESTART under new H3 parent) |
| L1233 | HEADING h_lvl=4 | `#### 4.5.3.2 Text Strings Greater than 200 Characters in Other Variables` | parent `§4.5.3 [...]` sib=2 |
| L1302 | HEADING h_lvl=3 | `### 4.5.4 Evaluators in the Interventions and Events Observation Classes` | parent `§4.5 [...]` sib=4 |
| L1320 | HEADING h_lvl=3 | `### 4.5.5 Clinical Significance for Findings Observation Class Data` | parent `§4.5 [...]` sib=5 |
| L1329 | HEADING h_lvl=3 | `### 4.5.6 Supplemental Reason Variables` | parent `§4.5 [...]` sib=6 |
| L1345 | HEADING h_lvl=3 | `### 4.5.7 Presence or Absence of Prespecified Interventions and Events` | parent `§4.5 [...]` sib=7 |
| L1368 | HEADING h_lvl=3 | `### 4.5.8 Accounting for Long-term Follow-up` | parent `§4.5 [...]` sib=8 |
| L1383 | HEADING h_lvl=3 | `### 4.5.9 Baseline Values` | parent `§4.5 [...]` sib=9 |

### 2.2.5 Boundary 末段 (L1391-1395, ch04 全文末)

```
L1389-1390: Variable comparison table TABLE_HEADER (§4.5.9)
L1391-1393: TABLE_ROW × 3 (--LOBXFL / ABLFL / --BLFL rows)
L1394: ""
L1395: "As shown in the table, each variable serves a specific need. The SDTM variable --LOBXFL (and/or --BLFL, if used) can be copied to ADaM for traceability and transparency, but only the ADaM variable ABLFL would be used to signify baseline for analysis. The content of --LOBXFL and ABLFL will be exactly the same when the SAP specifies that the baseline used for analysis is the last non-missing value prior to RFXSTDTC."  ← **末 SENTENCE** (ch04 全文末 atom)
```

注: ch04 文件 1395 行结束 (无 trailing blank). 本 batch 末原子 = L1395 SENTENCE (可能 sub-line split per §C-1 multi-clause; 也可能整体 1 atom). batch 04 闭后 ch04 全文完, **B-02 batch 05 起跨入新 chapter** (ch01_introduction.md 全 102 行).

**boundary critical (Rule A 必入 sample, 6 atoms 比 batch 03 的 5 多 1 因末 batch 验整 ch04 全闭)**:
- **a880** L1201 LIST_ITEM (跨 batch parent_section §4.5.1.3 续接) — **boundary 段首**
- **L1216 HEADING h_lvl=3 §4.5.2** sib=2 (1st H3 transition out of §4.5.1, 验证 sib chain 续 §4.5 下) — **boundary structural**
- **L1218 CROSS_REF (or SENTENCE w/ ref)** "See Section 8..." — **可能首 CROSS_REF in batch** (验 atom_type 决策 + cross_refs 字段)
- **L1222 HEADING h_lvl=4 §4.5.3.1** sib=1 (RESTART under new H3 parent §4.5.3) — **anti-pattern guard**
- **L1302 HEADING h_lvl=3 §4.5.4** sib=4 (H3 chain mid-batch jump 跨多节, 验证 sib 续) — **boundary structural mid-batch**
- **末原子 L1395 SENTENCE** (ch04 全文末 atom, 验证 ch04 100% 完结) — **boundary 段末 + 文末**

### 2.3 Dispatch 模板 — **FALLBACK PATH** (除非 OMC env 恢复)

派 `general-purpose` 单 dispatch (FALLBACK for `oh-my-claudecode:executor`, 同 batch 03 路径; 用户 ack Option B 2026-05-04). Dispatch prompt 顶部必须粘:

1. **Schema-first 头部** (`P2_B-02_kickoff.md` §5 完整 12-key 表 + atom_type 9-enum + Hook A4 + Hook C-8)
2. **parent_section canonical format** (`P2_B-02_kickoff.md` §6, chapters v1.8 bracketed `§<num>.<num> [<title>]`, 严禁 v1.9 spaced format)
3. **本 batch 特定**:
   - file: `knowledge_base/chapters/ch04_general_assumptions.md`
   - line range: **1201-1395** (writer 须只读这 195 行 + 上文 §2.2 continuity context)
   - atom_id prefix: `md_ch04_a` 从 `a880` 起
   - batch_id: `P2_B-02_batch_04` (写到 trace.jsonl, 不入 atom 字段, schema 无)
   - 输出: `evidence/checkpoints/P2_B-02_batch_04_md_atoms.jsonl`
   - prompt_version (extracted_by): `"P0_writer_md_v1.9"`
   - extracted_by.subagent_type: `"general-purpose"` (FALLBACK 同 batch 03)
4. **22 hooks self-validate** + **Hook A4 inline** (本 batch 0 FIGURE 预期; 但若 writer 误判表/list 为 FIGURE, Hook A4 拦截)
5. **FALLBACK 路径若仍生效** (OMC 未恢复): 同走 general-purpose; 否则改回 oh-my-claudecode:executor

### 2.4 Rule A 跟进 — **FALLBACK PATH**

派 `pr-review-toolkit:code-reviewer` (FALLBACK for `oh-my-claudecode:scientist`, 同 batch 03 路径) 跑 10-atom 分层独审:

- 加载 `subagent_prompts/P0_reviewer_v1.9.md` (含 §R-C1 sub-line tolerance + §R-C3..C-7 anti-defect)
- 输入: `evidence/checkpoints/P2_B-02_batch_04_md_atoms.jsonl`
- 输出: `evidence/checkpoints/rule_a_P2_B-02_batch_04_verdicts.jsonl` + `_summary.md`
- gate ≥90% PASS
- **额外 boundary 必入 sample (6 atoms, 比 batch 03 的 5 多 1 因末 batch + CROSS_REF 引入)**:
  - **a880** L1201 LIST_ITEM (跨 batch parent §4.5.1.3 续 + bullet prefix)
  - **L1216 H3 §4.5.2** sib=2 (验证 sib chain 续 §4.5 下)
  - **L1218 CROSS_REF / SENTENCE w/ ref** (验 atom_type 决策, 若 CROSS_REF 验 cross_refs 字段)
  - **L1222 H4 §4.5.3.1** sib=1 (RESTART anti-pattern guard)
  - **L1302 H3 §4.5.4** sib=4 (mid-batch H3 chain 续验)
  - **末原子 L1395 SENTENCE** (ch04 全文末 atom; 若 sub-line split 验 §R-C1 byte-exact substring)
- **stratified 4 atoms 余样**: TABLE_HEADER (从 8 表中选 1) / TABLE_ROW (含 null cells, 选 mh.xpt L1254 或 supppr.xpt L1290) / NOTE (`**Exception — IETEST...**` L1231 bold-Exception, 是 NOTE 还是 SENTENCE — 见 §4) / 1 多句 LIST_ITEM (L1245-1247 sub-bullets 嵌套)

### 2.5 PASS 后 append + checkpoint

PASS 后:
- cat `P2_B-02_batch_04_md_atoms.jsonl` → `md_atoms.jsonl` 追加 (`>> md_atoms.jsonl`)
- `wc -l md_atoms.jsonl` 验证累计 (post batch 03 close = 1763; post batch 04 应 ~1903-1943)
- `audit_matrix.md` P2 Bulk 表加 batch 04 行 (file / lines / atoms / Rule A 结果 / status; 含 ch04 全闭 milestone)
- `trace.jsonl` 写 batch 04 phase_report 事件 + ch04 全闭 milestone 事件
- `_progress.json` 更新 last_completed_batch = "P2_B-02_batch_04" + ch04_atomization_complete: true + next_batch = batch 05 (ch01 全)
- 写 `evidence/checkpoints/P2_B-02_batch_04_report.md` (atoms 总数 / atom_type 分布 / boundary 验证 / 与 batch 01/02/03 density 对比 / **ch04 全闭 cumulative 报告 4 segment 总 atoms = pilot 218 + B-02 batch 01 196 + batch 02 238 + batch 03 227 + batch 04 ?? = ?? atoms / 1395 行**)

---

## 3. Hook A4 inline (FIGURE figure_ref 校验)

每 atom_type=FIGURE 必满足:
- `figure_ref` 非 null
- pattern: `md_ch04_<topic_slug>_concept_map` (canonical) 或 `md_ch04_<descriptor>` (alt)

**预期: ch04 lines 1201-1395 内 FIGURE = 0** (扫源 L1201-1395 未见 mermaid block; 本 batch 全 narrative + table + list 形态. 若 writer 误判, Hook A4 拦截).

---

## 4. atom_type 边界 cases (本 batch 预期)

| Source 形态 | atom_type | 注 |
|---|---|---|
| `- **Rows 4-5:** ...` (L1201-1203) | LIST_ITEM | 续 batch 03 a879 sub-bullets, parent §4.5.1.3 持续 |
| VS / mh.xpt / suppmh.xpt / ae.xpt / suppae.xpt / pr.xpt / supppr.xpt / Convention / suppho.xpt / Situation / Variable comparison 表 (8+ 表) | TABLE_HEADER + TABLE_ROW | C-5 hook: TABLE_HEADER line_end-line_start ≤ 1; 跨多行表 1 TABLE_HEADER + N TABLE_ROW; 含多 null cells row (eg L1209/L1212/L1213/L1316-1318) |
| `### 4.5.2 ...` `### 4.5.3 ...` `### 4.5.4 ...` `### 4.5.5 ...` `### 4.5.6 ...` `### 4.5.7 ...` `### 4.5.8 ...` `### 4.5.9 ...` (L1216, 1220, 1302, 1320, 1329, 1345, 1368, 1383) | HEADING h_lvl=3 | parent `§4.5 [Other Assumptions]` sib 续 §4.5 H3 chain (sib=2/3/4/5/6/7/8/9 1-based) |
| `#### 4.5.3.1 ...` `#### 4.5.3.2 ...` (L1222, 1233) | HEADING h_lvl=4 | parent `§4.5.3 [...]` sib=1/2 (RESTART under new H3 parent) |
| `**Example 1 (mh.xpt / suppmh.xpt):** ...` (L1248) | SENTENCE | bold-Example caption ≠ HEADING (Hook C-6 PASS) |
| `**Example 2 (ae.xpt / suppae.xpt):** ...` (L1263) | SENTENCE | 同上 |
| `**Example 3 (pr.xpt / supppr.xpt):** ...` (L1277) | SENTENCE | 同上 |
| `**Example:** An adjudication committee evaluated...` (L1310) | SENTENCE | 同上 |
| `**Exception — IETEST in IE and TI domains:** ...` (L1231) | **NOTE** (bold-Exception 同 NOTE 形态) **或 SENTENCE** (bold caption + 内容句); writer 自定 — **建议 NOTE** (类似 `**Note:**` 形态, 是 carve-out 特例说明) | C-6 hook: bold-only ≠ HEADING; 但 NOTE vs SENTENCE 决策由 v1.9 prompt §R-C 解释 |
| `**Domain-specific conventions for text > 200 characters:**` (L1292) | SENTENCE | bold caption (无明显 carve-out 含义) |
| `mh.xpt:` `suppmh.xpt:` `ae.xpt:` `suppae.xpt:` `pr.xpt:` `supppr.xpt:` `suppae.xpt:` `suppho.xpt:` (L1250, 1256, 1265, 1271, 1279, 1285, 1312, 1339) | SENTENCE | dataset filename label SENTENCE; 注: 与 batch 03 同 (lb.xpt/eg.xpt/vs.xpt) 处理一致, 单独 SENTENCE atom; 不分 CODE_LITERAL (因 trailing colon `:` 标 label) |
| `lb.xpt` / `eg.xpt` / `vs.xpt` / `mh.xpt` / `ae.xpt` / `pr.xpt` / `suppmh.xpt` / `suppae.xpt` / `supppr.xpt` / `suppho.xpt` 内嵌 inline (e.g. L1248 caption 内 `mh.xpt`) | CODE_LITERAL | dataset filename inline 引用; 与 parent SENTENCE 共存 (同 batch 03 模式) |
| `See Section 8, Representing Relationships and Data, for guidance...` (L1218) | **CROSS_REF** (推荐) **或 SENTENCE w/ inline ref**; writer 自定 — **建议 CROSS_REF** 因句首 "See Section X" 是典型 cross-ref form, 且 cross_refs 字段可填 ref target | 若 writer 选 CROSS_REF: cross_refs 字段填 `["ig34_section_8"]` 或类似; 若选 SENTENCE: 在 cross_refs 字段填 inline ref string |
| narrative paragraph (e.g. L1224, L1235-1247, L1304-1308, L1322, L1331-1335, L1347-1356, L1370-1374, L1385-1395) | SENTENCE (multi-atom 同 line_start 合法 per §R-C1 + R22) | sub-line SENTENCE byte-exact substring; 多句 split |
| 段内 list (L1226-1227, L1239-1247, L1326-1327, L1376-1381) | LIST_ITEM | 顶级缩进 vs 嵌套缩进区分; L1239-1247 含 sub-bullet (L1244-1246 缩进 `  - `) — sub-bullet 是 sub-LIST_ITEM 同 parent_section, 还是嵌套 — 见 v1.9 §C-7 (建议 sub-bullets 同 LIST_ITEM, 不 nest, parent_section 同 outer) |
| 段内 numbered list (L1376-1381 "1. ...", "2. ...", ...) | LIST_ITEM | 数字 prefix `1. ` / `2. ` ...; 顶级 |

---

## 5. 失败处理 (Rule B)

若 dispatch 或 Rule A FAIL:
- 写 `evidence/failures/P2_B-02_batch_04_attempt_<M>.md` 含输入/产物/技术判定/业务判定/下次输入
- attempt 2 调整后再派
- 连续 2 attempt FAIL → halt B-02, 评估 v1.9 prompt 是否需 cut v1.9.1 (重点: CROSS_REF 决策若 reviewer 多次 ambiguous → cut 候选; 8+ tables 之内 TABLE_HEADER null-cell handling 若有缺陷 → cut 候选)

---

## 6. Recovery hint

若本 batch session 中断:
- writer 已派但未完: 看 trace.jsonl 末事件; checkpoint 文件存在则 partial recover, 不存在则重派
- writer 完但 reviewer 未派: 直接派 reviewer (pr-review-toolkit:code-reviewer FALLBACK), 无需重写
- reviewer FAIL: 走 Rule B 归档

---

## 7. ch04 全闭 milestone (post batch 04 PASS)

post batch 04: ch04 全文 1395/1395 = 100% 原子化, 累计 atoms = 218 (pilot) + 196 (batch 01) + 238 (batch 02) + 227 (batch 03) + ?? (batch 04) ≈ **~1020-1060 atoms**.

ch04 全闭后: B-02 cycle 第 4/9 batch 闭, **5 batch 余 (batch 05-09)** 要打:
- batch 05: ch01_introduction.md 全 102 行 ~70 atoms
- batch 06: ch03_submitting_data.md 全 130 行 ~90 atoms
- batch 07: ch02_fundamentals.md 全 174 行 ~120 atoms
- batch 08: ch10_appendices.md 全 310 行 ~210 atoms
- batch 09: ch08_relationships.md 全 439 行 ~310 atoms (B-01 model02 298 行 244 atoms 已验, 439 行 ~17K tokens 估算 < 32K cap; fallback 切 1-220 + 221-439)

post B-02 全闭 (9 batch): chapters/ 6 文件全完, 累计 atoms ~2700-2800 / 14 files (out of 141 in-scope).

---

*Kickoff written 2026-05-04 (post B-02 batch 03 闭环 commit 3b4c546). FALLBACK 路径同 batch 03; ch04 末 batch + 可能首 CROSS_REF in B-02 cycle.*
