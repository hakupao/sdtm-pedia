# P2 B-02 batch 01 — Multi-Session Kickoff

> 创建: 2026-04-29 (post `P2_B-02_kickoff.md` umbrella)
> 父 kickoff: `multi_session/P2_B-02_kickoff.md` (umbrella)
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.md` + 本 kickoff §4 inline 头部
> 路由词: 用户说 **"P2 bulk B-02 batch 01 开始任务"** 即触发 dispatch

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_kickoff.md` (umbrella, 本 batch 的语境框架)
2. `subagent_prompts/P0_writer_md_v1.9.md` (主体 prompt) + `P0_reviewer_v1.9.md` (Rule A 用)
3. `schema/atom_schema.json` v1.2 frozen
4. 本 kickoff (本身)

---

## 2. Batch 01 任务

### 2.1 Target

- **文件**: `knowledge_base/chapters/ch04_general_assumptions.md`
- **切片**: lines **301-1395** 4 段中的第 1 段 = **lines 301-600** (300 行)
- **估 atoms**: ~190 (pilot lines 1-300 = 218 atoms, density 0.73 atoms/行)
- **atom_id 起始**: `md_ch04_a219` (续 pilot a218)

### 2.2 Continuity context (从 pilot a218 接续)

pilot 末原子状态 (从 `md_atoms.jsonl` 读出):

```
a218 L300 SENTENCE | parent='§4.2.6 [Grouping Variables and Categorization]'
a217 L298 HEADING (h_lvl=3, sib=6 under §4.2) — 即 §4.2.6 节自身
```

源 line 301-310 内容 prefix:
```
L301: ""
L302: "#### Hierarchy of Grouping Variables"  ← L4 heading under §4.2.6
L304-: code block (STUDYID/DOMAIN/--CAT/--SCAT/USUBJID structure)
```

**进 batch 01 时 active context**:
- L1 active: `§4 [General Assumptions]` (pilot a001 H1)
- L2 active: 取决于段内首个 H2 (须 writer 推断, 但 §4.2 在 line 302 之前已经过, line 302 是 §4.2.6 下 sub-heading)
- L3 active: `§4.2.6 [Grouping Variables and Categorization]` (pilot a217 H3, line 298)
- 第一批 atoms 在 line 302 起点必然是 L4 HEADING `Hierarchy of Grouping Variables`, parent_section = `§4.2.6 [Grouping Variables and Categorization]`, **sibling_index = 1** (§4.2.6 下首个 H4 child)
- **sibling_index 1-based** per schema (`atom_schema.json $defs.md_atom.properties.sibling_index minimum: 1`) + pilot 全 1-based (a217 §4.2 下第 6 H3 child sib=6, 不是 sib=5) + B-01 model02 同 1-based. **schema-wins**, B-01 retro §1.3 codified.
- §4.2 下若本 slice 还有 §4.2.7 / §4.2.8 H3 children, sib continue from pilot a217 sib=6 → 下一 H3 sib=7, sib=8...

### 2.3 Dispatch 模板

派 `oh-my-claudecode:executor` 单 dispatch (writer 复用 B-01 4-batch slot 70, fresh dispatch independence per Rule D §1.2). Dispatch prompt 顶部必须粘:

1. **Schema-first 头部** (P2_B-02_kickoff.md §5 完整 12-key 表 + atom_type 9-enum + Hook A4)
2. **parent_section canonical format** (P2_B-02_kickoff.md §6, chapters v1.8 bracketed)
3. **本 batch 特定**:
   - file: `knowledge_base/chapters/ch04_general_assumptions.md`
   - line range: 301-600 (writer 须只读这 300 行 + 上文 §2.2 continuity context)
   - atom_id prefix: `md_ch04_a` 从 `a219` 起
   - batch_id: `P2_B-02_batch_01` (写到 trace.jsonl, 不入 atom 字段, schema 无)
   - 输出: `evidence/checkpoints/P2_B-02_batch_01_md_atoms.jsonl`
   - prompt_version (extracted_by): `"P0_writer_md_v1.9"` (无 v1.9.1 cut)
4. **22 hooks self-validate** + **Hook A4 inline** (§4)

### 2.4 Rule A 跟进

派 `oh-my-claudecode:scientist` (slot 72 复用 OK, fresh dispatch) 跑 10-atom 分层独审:

- 加载 `subagent_prompts/P0_reviewer_v1.9.md` (含 §R-C1 sub-line tolerance + §R-C3..C-7 anti-defect)
- 输入: `evidence/checkpoints/P2_B-02_batch_01_md_atoms.jsonl`
- 输出: `evidence/checkpoints/rule_a_P2_B-02_batch_01_verdicts.jsonl` + `_summary.md`
- gate ≥90% PASS
- **额外 verbatim 抽审**: 跨段 boundary atom (a219 / 段首 first L4 HEADING / 段末 last atom) 必入 sample, 验证 lines 301-600 边界处 atom 不漏行

### 2.5 PASS 后 append + checkpoint

PASS 后:
- cat `P2_B-02_batch_01_md_atoms.jsonl` → `md_atoms.jsonl` 追加 (`>> md_atoms.jsonl`)
- `wc -l md_atoms.jsonl` 验证累计 (post B-01 close = 1102; post batch 01 应 ~1292)
- `audit_matrix.md` P2 Bulk 表加 batch 01 行 (file / lines / atoms / Rule A 结果 / status)
- `trace.jsonl` 写 batch 01 phase_report 事件
- `_progress.json` 更新 last_completed_batch = "P2_B-02_batch_01"
- 写 `evidence/checkpoints/P2_B-02_batch_01_report.md` (atoms 总数 / atom_type 分布 / boundary 验证)

---

## 3. Hook A4 inline (FIGURE figure_ref 校验)

每 atom_type=FIGURE 必满足:
- `figure_ref` 非 null
- pattern: `md_ch04_<topic_slug>_concept_map` (canonical) 或 `md_ch04_<descriptor>` (alt)

**预期: ch04 lines 301-600 内 FIGURE 数量 ≤ 1** (扫源未见 mermaid block, 但 line 304 起 code block 是树形结构 ASCII, 应判 CODE_LITERAL 不是 FIGURE). 若 writer 误判为 FIGURE, Hook A4 会拦截.

---

## 4. atom_type 边界 cases (本 batch 预期)

| Source 形态 | atom_type | 注 |
|---|---|---|
| `#### Hierarchy of Grouping Variables` (L302) | HEADING h_lvl=4 | 在 §4.2.6 下 sibling_index=0 |
| code block 树形 ASCII (L304-309 STUDYID/...) | CODE_LITERAL | 整 block 1 atom 或多 atom 视 prompt 决定; B-01 model02 a059 模式参考 |
| 段内表格 (若有) | TABLE_HEADER + TABLE_ROW | C-5 hook: TABLE_HEADER line_end-line_start ≤ 1 |
| `**Note:**` 加粗 caption | NOTE | C-6 hook: bold ≠ HEADING |
| narrative paragraph | SENTENCE (multi-atom 同 line_start 合法 per §R-C1 + R22) | sub-line SENTENCE byte-exact substring |

---

## 5. 失败处理 (Rule B)

若 dispatch 或 Rule A FAIL:
- 写 `evidence/failures/P2_B-02_batch_01_attempt_<M>.md` 含输入/产物/技术判定/业务判定/下次输入
- attempt 2 调整后再派
- 连续 2 attempt FAIL → halt B-02, 评估 v1.9 prompt 是否需 cut v1.9.1

---

## 6. Recovery hint

若本 batch session 中断:
- writer 已派但未完: 看 trace.jsonl 末事件; checkpoint 文件存在则 partial recover, 不存在则重派
- writer 完但 reviewer 未派: 直接派 scientist, 无需重写
- reviewer FAIL: 走 Rule B 归档

---

*Kickoff written 2026-04-29 (B-02 cycle 起). 用户 ack 后即可派 executor.*
