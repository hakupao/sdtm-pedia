# P2 B-03 — Multi-Session Cycle Kickoff (umbrella)

> 创建: 2026-05-05 (post B-02 cycle CLOSED + cumulative audit GREEN-LIGHT 30/30=100% + v1.9.1 cut COMPLETED)
> 父 sub-plan: `plans/P2_md_atomization.md` v1.0 §B.1 (chunk 表) — 待按 B-03 scope 增补 §B.5
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` (8 NEW D-rules D-1..D-8; backward compat with v1.8/v1.9 atoms via §M-D6/§R-D6)
> Parent retro 入口: `multi_session/P2_B-02_RETROSPECTIVE.md` §5 post-cycle trigger #4
> 路由词: 用户在新 session 说 **"P2 bulk B-03 开始任务"** → 读本 kickoff + 看 §4 决定第一 batch
> 路由词: 用户说 **"P2 bulk B-03 batch 01 开始任务"** → 进 `P2_B-03_batch_01_kickoff.md` 派 dispatch (TBD, 写于第一 batch 启动前)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL)

本 kickoff 内 **每条 numeric claim 已 grep-verified against source byte-exact**. 逐项 verify 命令 + 实测值如下表 (执行日 2026-05-05). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | B-03 scope = 130 files | `find kb/model -name "*.md" \| grep -vE "(01\|04\|06)\.md" \| wc -l` (=3) + `find kb/domains -name "(assumptions\|examples).md" \| grep -v "/CM/" \| wc -l` (=124) + `find kb -maxdepth 1 -name "*.md" \| wc -l` (=3) | ✓ 3+124+3=130 |
| 2 | 总 in-scope 141 (PLAN §0.2 自检) | `find kb/domains -name "assumptions.md" \| wc -l` (63) + `examples.md` (63) + `kb/model` (6) + `kb/chapters` (6) + `kb -maxdepth 1` (3) | ✓ 63+63+6+6+3=141 |
| 3 | 已 atomized 11 files (B-02 close 后) | `grep -o '"file":"[^"]*"' md_atoms.jsonl \| sort -u \| wc -l` | ✓ 11 (6 chapters + 2 CM domains + 3 model 01/04/06) |
| 4 | model 余 = 02 + 03 + 05 (NOT "02/03/05/06" 如 B-01 retro 笔误) | `grep -o '"atom_id":"md_model[0-9]*"' md_atoms.jsonl \| sort -u` → md_model01, md_model04, md_model06 已存; 余 02/03/05 | ✓ 3 (02/03/05) |
| 5 | model 余 lines: 02=298 + 03=190 + 05=296 = 784 | `wc -l kb/model/{02,03,05}*.md` | ✓ 298+190+296=784 |
| 6 | domains 余 124 (CM 已做) | `grep -o '"file":"kb/domains/[^"]*"' md_atoms.jsonl \| sort -u` → CM/assumptions + CM/examples 已存; 余 62 domains × 2 = 124 | ✓ 124 |
| 7 | domains 余 lines (8674) | `find kb/domains -name "(a\|e).md" \| grep -v /CM/ \| xargs wc -l \| tail -1` | ✓ 8674 |
| 8 | domains 余 size buckets | `awk` 分桶: <50:78 / 50-99:26 / 100-199:13 / 200-499:5 / ≥500:2 | ✓ 78+26+13+5+2=124 |
| 9 | domains 余 ≥200L 文件 = 7 | TA(710) PC(572) EX(434) DM(429) DS(413) IS(273) FA(244) | ✓ 7 |
| 10 | top-level 3 文件 lines: INDEX=195 + ROUTING=211 + VARIABLE_INDEX=2005 = 2411 | `wc -l kb/{INDEX,ROUTING,VARIABLE_INDEX}.md` | ✓ 195+211+2005=2411 |
| 11 | B-03 总 source lines = 11,869 | model 784 + domains 8674 + top 2411 | ✓ 11,869 |
| 12 | B-02 close md_atoms.jsonl root atoms = 2867 | `wc -l md_atoms.jsonl` | ✓ 2867 |

**Drift 校正记录 (B-02 retro / progress recovery_hint vs 实测)**:
- retro/progress 表述 "余下 model + 126 domains" → **实测 3 model + 124 domains** (CM + model 01/04/06 已做; B-02 retro G-B02-4 默认 126 是误)
- B-01 retro 表 "model 02/03/05/06 atomized" → **实测 model 01/04/06 atomized** (B-01 batches 01-04 atomized 01/04/06 + CM × 2; B-01 retro 笔误)
- 此 §0.5 行 4 + 6 即为 drift 校正 byte-exact 来源

---

## 1. Session 启动前必读 (按序)

1. `multi_session/P2_B-02_RETROSPECTIVE.md` — 6 节 retro, 重点 §1 (7 保留做法 R-B02-1..7) + §2 (5 缺口 G-B02-1..5) + §5 (B-03 entry conditions)
2. `evidence/checkpoints/cumulative_audit_post_B02.md` — 30/30=100% strict PASS (与 B-01 28/30=93.3% 比较)
3. `subagent_prompts/P0_writer_md_v1.9.1.md` §D-1..§D-8 (8 NEW D-rules) — 重点 §D-1 (Hook 22b 本 §0.5 来源) + §D-8 (FALLBACK pool peer-alternative)
4. `subagent_prompts/P0_matcher_v1.9.1.md` + `P0_reviewer_v1.9.1.md` — backward compat §M-D6/§R-D6 verify 接受 v1.8 ch04 pilot atoms
5. 本 kickoff (umbrella)
6. 第一 batch kickoff: `P2_B-03_batch_01_kickoff.md` (TBD, 写于 batch 01 派发前)

---

## 2. B-03 Scope

`model/` 余 3 + `domains/` 余 124 + top-level 3 = **130 files** / **11,869 source lines**. 自检: B-02 close 11 files atomized + B-03 scope 130 = 141 = PLAN §0.2 in-scope total.

| 类别 | Files 余 | Lines 余 | 估 atoms (range) |
|---|---|---|---|
| `model/` (02/03/05) | 3 | 784 | ~470-550 (B-01 model02/05 1.0-1.3 atoms/line baseline) |
| `domains/` × 124 (62 ass + 62 ex) | 124 | 8674 | ~5800-7800 (混合 narrative/list/table; 0.7-0.9 atoms/line 估; CM pilot 18.7 lines/file → 83 atoms/file 偏 example-heavy) |
| top-level 3 (INDEX + ROUTING + VARIABLE_INDEX) | 3 | 2411 | ~1200-2000 (VARIABLE_INDEX 2005L spec table-heavy = TABLE_ROW 主导 ~1500+) |
| **合计** | **130** | **11,869** | **~7,500-10,500 atoms 估** (B-02 retro 早估 12K-20K 偏 high; 本 §0.5 verify 后 estimate refined) |

post B-03: md_atoms.jsonl 累计 ~10,400-13,400 atoms / 141 files (out of 141 in-scope = **100% 文件覆盖 milestone**). P2 phase exit gate.

---

## 3. Sub-cycle 结构 (B-03 三段)

B-03 比 B-02 大 ~3x atoms / ~5x files / ~30-60 batches estimate. 拆 3 sub-cycle 明确 boundary + retro 节奏 + cumulative audit 触发点:

### B-03a: model/ 余 3 文件 (warm-start 续 B-01 model 节奏)

- 3 batches single-dispatch full-file (model 02/05 ~298L 同 B-01 model02 298L=244 atoms 模式; model 03 190L 类比 ch01 102L=88 atoms)
- 估 atoms ~470-550 / 估 batches **3** / 估 duration **1-2 days**
- B-03a 闭环触发 mini-audit (10-atom stratified Rule A 单 batch reviewer FALLBACK pr-review-toolkit; **不**触发 cumulative inter-cycle audit, 留给 B-03 整 cycle 末)

### B-03b: top-level 3 文件 (含切片 VARIABLE_INDEX)

- INDEX (195L) + ROUTING (211L): 单 dispatch 各 1 batch (类比 ch04 lines 1-300 单 dispatch 模式)
- **VARIABLE_INDEX (2005L)**: 切 ~7 段 (类似 ch04 1395L 切 5 段 模式; 每段 ~280L hard line range)
- 估 atoms ~1200-2000 / 估 batches **9** (1+1+7) / 估 duration **3-5 days**

### B-03c: domains/ × 124 (62 domains × 2 files)

- 78 文件 <50L: 每 1 file = 1 batch (单 dispatch full-file; 不 pack 多 file 减 atom_id 前缀逻辑复杂度, B-02 R-B02-1 验证)
- 26 文件 50-99L: 每 1 file = 1 batch
- 13 文件 100-199L: 每 1 file = 1 batch
- 5 文件 200-499L: 单 dispatch full-file (类比 ch10 310L=258 atoms 验证 < 32K cap; 估 token < 28K = OK)
- 2 文件 ≥500L (PC 572L + TA 710L): 切 2-3 段 (类似 ch04 切片 模式)
- domain 顺序: **alphabetical by domain code** (AE → AG → ... → VS); 62 domains × 2 files (assumptions 先 / examples 后) = 1 domain = 2 batch consecutive
- 估 atoms ~5800-7800 / 估 batches **~127** (78+26+13+5+5 切片) / 估 duration **2-4 weeks**

**总估**: 3 sub-cycle = **~139 batches / 7,500-10,500 atoms / 3-5 weeks**.

---

## 4. Batch 序列 preview (B-03a 全 + B-03b head + B-03c head)

B-03a/b head batches 详见下表; B-03c 整体按 §3 alphabetical pattern 派发, 详细 batch_NN_kickoff.md 写于各 batch 派发前 (B-02 模式).

| Batch | Target | Lines | 估 atoms | 切片? | atom_id 起始 | 预派发 sub-cycle |
|---|---|---|---|---|---|---|
| **batch_01** | `model/03_special_purpose_domains.md` | 全 190 | ~150-180 | 单 dispatch | `md_model03_a001` | B-03a #1 (最短 model 先打) |
| **batch_02** | `model/05_study_level_data.md` | 全 296 | ~190-240 | 单 dispatch | `md_model05_a001` | B-03a #2 |
| **batch_03** | `model/02_observation_classes.md` | 全 298 | ~190-240 | 单 dispatch | `md_model02_a001` | B-03a #3 (闭 model/) |
| **batch_04** | `INDEX.md` | 全 195 | ~150-200 | 单 dispatch | `md_index_a001` | B-03b #1 |
| **batch_05** | `ROUTING.md` | 全 211 | ~150-220 | 单 dispatch | `md_routing_a001` | B-03b #2 |
| **batch_06** | `VARIABLE_INDEX.md` lines 1-300 | 300 | ~250-350 | 切片 (7 段中 #1) | `md_varindex_a001` | B-03b #3 |
| **batch_07** | `VARIABLE_INDEX.md` lines 301-600 | 300 | ~250-350 | 切片 #2 | (续) | B-03b #4 |
| **batch_08..12** | `VARIABLE_INDEX.md` 切片 #3-#7 (lines 601-2005) | 各 ~280L | 各 ~250-350 | 切片 | (续) | B-03b #5-#9 |
| **batch_13** | `domains/AE/assumptions.md` | 全 58 | ~45-55 | 单 dispatch | `md_AE_assumptions_a001` (TBD: 命名 TBD per first batch dispatch) | B-03c #1 |
| **batch_14** | `domains/AE/examples.md` | 全 97 | ~70-90 | 单 dispatch | `md_AE_examples_a001` | B-03c #2 |
| ... | (62 domains × 2 = 124 files alphabetical AE→...→VS) | | | | | B-03c #3-#127 |

注 1: B-02 R-B02-1 验证不打包合 batch — 1 file = 1 batch (or 切片 batch). atom_id 前缀 = `md_<file_stem>_aNNN` (3+ digits per schema v1.2.1 inline patch).

注 2: B-03c domains/ atom_id prefix 命名约定 TBD per first dispatch (建议 `md_<DOMAIN>_<assumptions|examples>_aNNN`, 如 `md_AE_assumptions_a001`). 第一 batch_13 kickoff 写前 lock convention.

注 3: VARIABLE_INDEX 2005L 切 7 段是 estimate; 实际 batch 06 派发前先看 line range 划分 (table-heavy 切片应按 logical group 不机械等距).

---

## 5. v1.9.1 prompt 入口条件 + B-02 retro inputs 落地

### v1.9.1 prompt 就绪 (post v1.9.1 cut 2026-05-05)

- ✅ `P0_writer_md_v1.9.1.md` (217L, 8 NEW D-rules D-1..D-8; FALLBACK pool peer-alternative status §D-8; backward compat §C 节)
- ✅ `P0_matcher_v1.9.1.md` (94L, 6 NEW anti-flag rules §M-D1..§M-D6; backward compat ch04 pilot v1.8 + B-01/B-02 v1.9)
- ✅ `P0_reviewer_v1.9.1.md` (126L, 7 NEW rules §R-D1..§R-D7; AUDIT pivot 51 cumulative)
- ✅ Rule D AUDIT slot #70 feature-dev:code-architect verdict PASS_with_observation 19/19 → PASS post 2 in-session remediations
- ✅ v1.9 archived `subagent_prompts/archive/v1.9_final_2026-05-05/`

### B-02 retro 入口 conditions 落地

回应 P2_B-02_RETROSPECTIVE.md §5 + §2 缺口:

- [x] **§5 trigger #1 cumulative audit GREEN-LIGHT** 30/30=100% (`evidence/checkpoints/cumulative_audit_post_B02.md`)
- [x] **§5 trigger #2 RETROSPECTIVE.md** 写完 (`multi_session/P2_B-02_RETROSPECTIVE.md`)
- [x] **§5 trigger #3 v1.9.1 cut** 完成 (4 prompt files cut, v1.9 archived, slot #70 PASS, commit 5373733)
- [x] **§5 trigger #4 B-03 entry kickoff prep** (本文件)
- [x] **G-B02-1 修复 (3 连续 kickoff drift)**: §0.5 grep checksum block 强制 (本 kickoff 已含; v1.9.1 §D-1 codified)
- [x] **G-B02-2 修复 (atom count 估算)**: §3 sub-cycle 估 use 0.7-0.9 atoms/line range (B-02 batch 09 实证 167 SENTENCE atoms / narrative-heavy)
- [x] **G-B02-3 修复 (FALLBACK 长期化)**: v1.9.1 §D-8 promote FALLBACK 到 peer-alternative (本 kickoff §6 explicit)
- [x] **G-B02-4 修复 (B-03 派发 strategy)**: 本 kickoff §3 三段 sub-cycle + §4 batch 序列 preview
- [x] **G-B02-5 carry-forward**: ch04 pilot a001-a218 v1.8 style backward compat 自动 accepted via §M-D6/§R-D6 (B-03 cycle 不 re-emit)
- [ ] **本 kickoff 用户 ack** (pending)

---

## 6. Dispatch template (每 batch 共用顶部)

每 batch dispatch 复用 schema-first 头部 + v1.9.1 hooks:

```
[Schema 字段表 — 12 keys 必填 (除 nullable 标的); v1.2.1 inline atom_id pattern \d{3,}]
- atom_id (string, pattern ^md_[A-Za-z0-9_]+_a\d{3,}$, unique within file)
- atom_type (string enum: HEADING / SENTENCE / LIST_ITEM / TABLE_HEADER / TABLE_ROW / CODE_LITERAL / NOTE / FIGURE / CROSS_REF)
- file (string, full repo-relative, must start with "knowledge_base/")
- line_start, line_end (int, 1-based)
- verbatim (string, byte-exact substring of source line(s))
- parent_section (string, canonical format §7 below)
- heading_level (int 1-6, REQUIRED for HEADING, null otherwise)
- sibling_index (int 0-based, REQUIRED for HEADING within parent_section, null otherwise)
- figure_ref (string, REQUIRED for FIGURE — pattern md_<file_stem>_<descriptor>_concept_map; null otherwise)
- cross_refs (array of atom_id strings, default [])
- extracted_by (object: { subagent_type: <see pool below>, prompt_version: "P0_writer_md_v1.9.1", ts: ISO8601 })

[Writer/Reviewer pool — v1.9.1 §D-8 peer-alternative status]
Writer pool (any of):
- oh-my-claudecode:executor (OMC primary, opus model when available)
- general-purpose (FALLBACK peer-alternative; B-02 sustained 7 batches 1,331 atoms 0 writer defect; NOT in N21 ban list)
Reviewer pool (any of):
- pr-review-toolkit:code-reviewer (FALLBACK peer-alternative; B-02 sustained 7 batches 100% PASS)
- oh-my-claudecode:scientist / oh-my-claudecode:critic (OMC primary)
- feature-dev:code-reviewer (cumulative inter-cycle audit; Rule D distinct from per-batch reviewers)
N21 ban list (sustained, unchanged): oh-my-claudecode:writer, Explore, oh-my-claudecode:explore, feature-dev:code-explorer, oh-my-claudecode:document-specialist
Rule D 硬约束: writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance)

[v1.9.1 NEW hooks 22b + D-NOTE-BQ + D-D8 (writer_md hooks 22 → 25)]
- Hook 22b: kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims; absent/partial §0.5 = independently grep-verify
- Hook D-NOTE-BQ: blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE (verbatim 含 12-byte prefix `3e 20 2a 2a 4e 6f 74 65 3a 2a 2a 20`)
- Hook D-D8: numberless `## Overview` H2 不创 sub-namespace, children inherit chapter root parent_section
- Hook A4 (sustained): FIGURE atom 必带 figure_ref non-null + canonical pattern; null/empty → DO NOT emit
- Hook C-8 (sustained): file 字段必含 "knowledge_base/" 前缀

[Rule B 强制]
Source markdown anomaly (kickoff doc 与 source 不一致, OR 形式不规范) → emit source byte-exact + flag in batch report `kickoff_doc_drift_detected: <count>` 或 `source_anomaly_preserved: <count>`. Writer 永不 fabricate match.
```

---

## 7. parent_section canonical format (3 类 file)

### 7.1 model/ 02-05 (B-01 spaced format 沿用)

model/ 章节 markdown 多无正式 numbering, B-01 验证用 **v1.9 spaced format**:

```
canonical: § <Title>
examples:
  § Concepts and Terms
  § Special-Purpose Datasets
  § Domain Models
  § Trial Design Datasets
```

### 7.2 top-level 3 (INDEX / ROUTING / VARIABLE_INDEX)

参考 model/ spaced format. 第一 batch_04 kickoff 派发前 lock convention (按 actual heading structure 推断). 默认 `§ <H2 Title>` (无 chapter number).

### 7.3 domains/ × 124 (62 domains × 2 files)

domains/ 文件 heading 结构如 `## Assumptions` 或 `## Examples` (各文件首 H1 = domain 名, e.g. `# AE — Adverse Events`; H2 通常仅 1-2 个). parent_section convention TBD per first batch_13 kickoff (建议 spaced format `§ Assumptions [<DOMAIN>]` 或 chapter root inherit chain). Lock convention 后 alphabetical 全 cycle 沿用.

**共通规则**:
- `§<num>.<num>...` numbered format **仅** chapters/ (B-02 已用); model/ + top-level + domains/ 都 spaced format
- 跨 batch (切片 file) parent_section 必持续: 进 batch N+1 时 active L1 = batch N 末 active L1 (B-02 ch04 切片 模式)

---

## 8. Per-batch 产物 (每 batch 共用)

- `evidence/checkpoints/P2_B-03_batch_<NN>_md_atoms.jsonl` — writer 产物 (atomized JSONL)
- `evidence/checkpoints/rule_a_P2_B-03_batch_<NN>_verdicts.jsonl` + `_summary.md` — 11+ atom Rule A audit (8 boundary + 3 stratified per B-02 R-B02-3; ≥200 atoms batch 加 5-7 stratified)
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加
- `trace.jsonl` phase_report 事件 + dispatch 事件
- `_progress.json` 字段更新 (last_completed_batch / current_phase / cumulative atom count)

---

## 9. B-03 闭环 cumulative audit (gate before P2 phase exit)

固化 inter-cycle gate 制度 (B-01 retro §6 + B-02 retro R-B02-4):

- **Trigger**: B-03 final batch (~batch 139 estimate) PASS + 全部入 root md_atoms.jsonl
- **Sample**: **30-atom 跨累积 141 files 分层** (chapters 6 + model 6 + domains 63+63 + top 3); 比 B-02 30/14 比例更稀疏 (30/141 ≈ 21% file coverage) — 可考虑放大 sample 到 **50-atom** 以维持 cross-file representative power (Daisy ack 决定)
- **Reviewer**: subagent_type **distinct from per-batch reviewers + B-01/B-02 cumulative reviewers** (Rule D 跨 cycle 隔离更严; 候选: oh-my-claudecode:critic OR superpowers:code-reviewer OR pr-review-toolkit:code-reviewer 中未 burned 的)
- **Gate**: ≥90% functional PASS (与 B-01 28/30=93.3% / B-02 30/30=100% 一致)
- **Findings 处理**: HIGH 必修在 P2 → P3 phase 前 / MEDIUM 入 v1.9.2 backlog / LOW carry-forward
- **P2 phase exit 触发**: B-03 cumulative audit PASS + RETROSPECTIVE_P2.md 写完 (Rule C; 跨 B-01+B-02+B-03 整 P2 phase 复盘) + Daisy/Bojiang 用户 ack → 进 P3 (索引构建)

---

## 10. 路由词 quick reference

| 用户说 | session 动作 |
|---|---|
| `P2 bulk B-03 开始任务` | 读本 kickoff (umbrella), 报告下一 batch (默认 batch 01 model/03), 等 ack |
| `P2 bulk B-03 batch 01 开始任务` | 进 `P2_B-03_batch_01_kickoff.md` (TBD) dispatch executor for `model/03_special_purpose_domains.md` |
| `P2 bulk B-03 batch NN 开始任务` (NN=02..~139) | 进对应 batch_NN_kickoff.md (按 §4 表逐个写, 派发前一刻完成 §0.5 grep checksum) |
| `B-03a 闭环 mini-audit 开始任务` | post batch 03 PASS, 派 reviewer 10-atom stratified Rule A (model/ 3 batch 跨 batch consistency check) |
| `B-03b 闭环 mini-audit 开始任务` | post batch 12 PASS (top-level + VARIABLE_INDEX 切片闭环), 派 reviewer 10-atom stratified |
| `B-03 cumulative audit 开始任务` | post final batch (~139) PASS, 派 reviewer 30-50 atom 跨 141 files 分层 audit |

---

## 11. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-03_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id = ++NNN (同一 file 切片) 或 a001 (新 file)
- 跨 sub-cycle 边界 (B-03a→b→c): 看 §3 sub-cycle 表 boundary batches; 续点不模糊

---

*Kickoff written 2026-05-05 (B-02 cycle CLOSED + cumulative audit GREEN-LIGHT + v1.9.1 cut COMPLETED 同日, commit 5373733). 等用户 ack 后写 batch_01_kickoff.md (model/03) 或直接进 dispatch. §0.5 grep checksum 12/12 byte-exact verified. v1.9.1 §D-1 mandatory compliance.*
