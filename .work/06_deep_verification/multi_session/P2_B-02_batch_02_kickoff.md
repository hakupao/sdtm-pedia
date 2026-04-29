# P2 B-02 batch 02 — Multi-Session Kickoff

> 创建: 2026-04-29 (post `P2_B-02_batch_01` 全闭环 same day, batch 01 196 atoms 14-sweep clean Rule A 100%)
> 父 kickoff: `multi_session/P2_B-02_kickoff.md` (umbrella §3 第 2 行)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` + 本 kickoff §3 inline 头部
> 路由词: 用户说 **"P2 bulk B-02 batch 02 开始任务"** 即触发 dispatch

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_kickoff.md` (umbrella, 本 batch 的语境框架, 特别是 §3 表 + §5 schema-first 模板 + §6 parent_section canonical format)
2. `subagent_prompts/P0_writer_md_v1.9.md` (主体 prompt) + `P0_reviewer_v1.9.md` (Rule A 用)
3. `schema/atom_schema.json` v1.2 frozen
4. `evidence/checkpoints/P2_B-02_batch_01_report.md` + `rule_a_P2_B-02_batch_01_summary.md` (前 batch 末态 + Rule A 通过项参考)
5. 本 kickoff (本身)

---

## 2. Batch 02 任务

### 2.1 Target

- **文件**: `knowledge_base/chapters/ch04_general_assumptions.md`
- **切片**: lines **601-900** (300 行) = ch04 4 段中的第 2 段
- **估 atoms**: ~190-200 (batch 01 实测 196 / 300 行 = density 0.65 atoms/行)
- **atom_id 起始**: `md_ch04_a415` (续 batch 01 a414)

### 2.2 Continuity context (从 batch 01 a414 接续)

batch 01 末原子状态 (从 `evidence/checkpoints/P2_B-02_batch_01_md_atoms.jsonl` tail 读出):

```
a414 L600 LIST_ITEM | parent='§4.2.9 [Variable Lengths]' | h_lvl=null sib=null
a413 L599 LIST_ITEM | parent='§4.2.9 [Variable Lengths]'
a412 L598 LIST_ITEM | parent='§4.2.9 [Variable Lengths]'
... (上溯到 H3 §4.2.9 自身在 L592, 是 §4.2 下第 9 个 H3 child sib=9)
```

源 line 601-630 内容 prefix (写手必读以定 boundary):

```
L601: "    - --TESTCD and IDVAR will never be more than 8, so the length can always be set to 8."
L602: "    - The length for variables that use controlled terminology can be set to the length of the longest term."
        ↑ 注: L600/L601/L602 三条 LIST_ITEM 同一缩进级 `  - ` (2-space indent), 实际是 L599 例子下的 sub-bullets;
          batch 01 a414 emit 了 L600 这一条; L601-L602 须 batch 02 续 emit, atom_id a415/a416, parent 仍 §4.2.9
L603: ""
L604: "---"   ← Markdown 水平分隔符 (horizontal rule)
L605: ""
L606: "## 4.3 Coding and Controlled Terminology Assumptions"  ← **H2 transition**
L607: ""
L608: "> **Note:** Examples provided in the CDISC Notes column and domain examples are only examples and not intended to imply controlled terminology. For current CDISC Controlled Terminology, visit https://datascience.cancer.gov/resources/cancer-vocabulary/cdisc-terminology."
L609: ""
L610: "### 4.3.1 Controlled Terms, Codelist or Format Column"  ← H3 first child of §4.3
L611-: ...
L621: "### 4.3.2 Controlled Terminology Text Case"
L623: "### 4.3.3 Controlled Terminology Values"
L625: (continues...)
```

**进 batch 02 时 active context**:
- L1 active: `§4 [General Assumptions]` (pilot a001 H1 sib=1)
- L2 active 在 a414 末: 需 writer 从 batch 01 头部 a001..a047 推断 §4.2 H2 sib (L1=§4.1 sib=1 → §4.2 sib=2)
- L3 active 在 a414 末: `§4.2.9 [Variable Lengths]` (sib=9 under §4.2)
- 续 emit a415=L601 LIST_ITEM, a416=L602 LIST_ITEM, parent_section 仍 `§4.2.9 [Variable Lengths]`
- L604 `---` 水平分隔: per B-01 model02 / pilot 经验 **不 emit** (非 content, schema atom_type 9 enum 无对应); writer 须明确跳过, **不**生成 atom 带 verbatim="---"
- a417 起 = L606 HEADING h_lvl=2 `## 4.3 Coding and Controlled Terminology Assumptions`, parent_section = `§4 [General Assumptions]`, **sibling_index = 3** (§4.1 sib=1, §4.2 sib=2, §4.3 sib=3 — 1-based per schema)
- 进 §4.3 后, active L2 = `§4.3 [Coding and Controlled Terminology Assumptions]`
- a418 = L608 NOTE (`> **Note:** ...`), parent_section = `§4.3 [Coding and Controlled Terminology Assumptions]`, Hook C-6: bold-only ≠ HEADING (NOTE 正确)
- a419 = L610 HEADING h_lvl=3 `### 4.3.1 Controlled Terms, Codelist or Format Column`, parent_section = `§4.3 [...]`, **sibling_index = 1** (§4.3 下首 H3 child)
- 后续 §4.3.2..§4.3.X H3 sib=2,3,4,... 持续累计

**boundary critical**:
- a415 (段首 LIST_ITEM 续 §4.2.9) 是跨段连续性 critical atom — Rule A 必入 sample
- a417 (段首 H2 §4.3 transition + sib=3 跨段) 是结构 critical atom — Rule A 必入 sample
- 段末 atom (~a610 取决于 L900 处) 是 boundary 末 — Rule A 必入 sample

### 2.3 Dispatch 模板

派 `oh-my-claudecode:executor` 单 dispatch (同 batch 01 writer 类型, fresh dispatch 独立性 per Rule D §1.2; 同 type 不同 dispatch 计入同 slot 家族, Rule D 不撞). Dispatch prompt 顶部必须粘:

1. **Schema-first 头部** (`P2_B-02_kickoff.md` §5 完整 12-key 表 + atom_type 9-enum + Hook A4 + Hook C-8)
2. **parent_section canonical format** (`P2_B-02_kickoff.md` §6, chapters v1.8 bracketed `§<num>.<num> [<title>]`, 严禁 v1.9 spaced format)
3. **本 batch 特定**:
   - file: `knowledge_base/chapters/ch04_general_assumptions.md`
   - line range: **601-900** (writer 须只读这 300 行 + 上文 §2.2 continuity context)
   - atom_id prefix: `md_ch04_a` 从 `a415` 起
   - batch_id: `P2_B-02_batch_02` (写到 trace.jsonl, 不入 atom 字段, schema 无)
   - 输出: `evidence/checkpoints/P2_B-02_batch_02_md_atoms.jsonl`
   - prompt_version (extracted_by): `"P0_writer_md_v1.9"`
4. **22 hooks self-validate** + **Hook A4 inline** (§3) + **L604 `---` skip directive** (§2.2)

### 2.4 Rule A 跟进

派 `oh-my-claudecode:scientist` (fresh dispatch, 同 batch 01 reviewer 类型, Rule D 同家族延续 OK) 跑 10-atom 分层独审:

- 加载 `subagent_prompts/P0_reviewer_v1.9.md` (含 §R-C1 sub-line tolerance + §R-C3..C-7 anti-defect)
- 输入: `evidence/checkpoints/P2_B-02_batch_02_md_atoms.jsonl`
- 输出: `evidence/checkpoints/rule_a_P2_B-02_batch_02_verdicts.jsonl` + `_summary.md`
- gate ≥90% PASS
- **额外 boundary 必入 sample (3 atoms)**:
  - **a415** (段首 LIST_ITEM 续 §4.2.9, 验证跨 batch parent_section 持续)
  - **a417** (段首 H2 §4.3 transition, 验证 sib=3 1-based + parent_section canonical bracketed format)
  - **段末 atom** (~a610 取决于 L900 实际命中, 验证下段连续性 hook)

### 2.5 PASS 后 append + checkpoint

PASS 后:
- cat `P2_B-02_batch_02_md_atoms.jsonl` → `md_atoms.jsonl` 追加 (`>> md_atoms.jsonl`)
- `wc -l md_atoms.jsonl` 验证累计 (post batch 01 close = 1298; post batch 02 应 ~1488-1498)
- `audit_matrix.md` P2 Bulk 表加 batch 02 行 (file / lines / atoms / Rule A 结果 / status)
- `trace.jsonl` 写 batch 02 phase_report 事件
- `_progress.json` 更新 last_completed_batch = "P2_B-02_batch_02"
- 写 `evidence/checkpoints/P2_B-02_batch_02_report.md` (atoms 总数 / atom_type 分布 / boundary 验证 / 与 batch 01 density 对比)

---

## 3. Hook A4 inline (FIGURE figure_ref 校验)

每 atom_type=FIGURE 必满足:
- `figure_ref` 非 null
- pattern: `md_ch04_<topic_slug>_concept_map` (canonical) 或 `md_ch04_<descriptor>` (alt)

**预期: ch04 lines 601-900 内 FIGURE = 0** (扫源 L600-900 未见 mermaid block 或 ASCII 图; 此切片主要为 §4.3 controlled terminology narrative + sub-headings + 可能少量 list/note; 若 writer 误判, Hook A4 拦截).

---

## 4. atom_type 边界 cases (本 batch 预期)

| Source 形态 | atom_type | 注 |
|---|---|---|
| `    - --TESTCD and IDVAR will never...` (L601-602) | LIST_ITEM | 续 batch 01 a414 sub-bullets, parent §4.2.9 持续 |
| `---` 水平分隔 (L604) | **不 emit** | 非 content, schema 无 enum; writer 跳过 (§2.2 directive) |
| `## 4.3 Coding and Controlled Terminology Assumptions` (L606) | HEADING h_lvl=2 | 在 §4 下 sib=3 (1-based, §4.1=1 §4.2=2 §4.3=3) |
| `> **Note:** Examples provided...visit https://...` (L608) | NOTE | C-6 hook: bold-only ≠ HEADING; URL 在内 — chapters/md 不 bind N21 (PDF-only) |
| `### 4.3.1 Controlled Terms...` (L610) | HEADING h_lvl=3 | 在 §4.3 下 sib=1 (首 H3 child) |
| `### 4.3.2 ...` `### 4.3.3 ...` ... | HEADING h_lvl=3 | 在 §4.3 下 sib=2, 3, 4, ... 累计 |
| narrative paragraph | SENTENCE (multi-atom 同 line_start 合法 per §R-C1 + R22) | sub-line SENTENCE byte-exact substring |
| 段内若有 list (`- `) | LIST_ITEM | 顶级缩进 vs 嵌套缩进区分 |
| 段内若有 table (pipe-formatted) | TABLE_HEADER + TABLE_ROW | C-5 hook: TABLE_HEADER line_end-line_start ≤ 1 |
| 段内若有 code block (fenced ```) | CODE_LITERAL | 整 block 1 atom 或多 atom 视 prompt 决定 |

---

## 5. 失败处理 (Rule B)

若 dispatch 或 Rule A FAIL:
- 写 `evidence/failures/P2_B-02_batch_02_attempt_<M>.md` 含输入/产物/技术判定/业务判定/下次输入
- attempt 2 调整后再派
- 连续 2 attempt FAIL → halt B-02, 评估 v1.9 prompt 是否需 cut v1.9.1

---

## 6. Recovery hint

若本 batch session 中断:
- writer 已派但未完: 看 trace.jsonl 末事件; checkpoint 文件存在则 partial recover, 不存在则重派
- writer 完但 reviewer 未派: 直接派 scientist, 无需重写
- reviewer FAIL: 走 Rule B 归档

---

*Kickoff written 2026-04-29 (post B-02 batch 01 闭环 same day). 用户 ack 后即可派 executor.*
