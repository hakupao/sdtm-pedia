# B-01 Retrospective — P2 Bulk model/* 4-batch cycle

> Date: 2026-04-29
> Scope: P2 Bulk B-01 cycle (batch 01..04) + cumulative cross-batch audit
> Atoms produced this cycle: 705 (109+244+160+192)
> Cumulative audit: 28/30 = 93.3% PASS, 1 HIGH hotfixed, 2 NEW v1.9.1 candidates
> Status: **B-02 GREEN-LIGHT WITH CONDITIONS**

---

## §1 保留下来的做法 (validated, keep doing)

### 1.1 单 dispatch full-file 模式 (production-stable)

4 个 batch (174 / 298 / 190 / 296 行) 全部单 executor dispatch 完成,无 fallback 切片需要。Token 输出 8K-17K,远低于 32K cap。Pilot Attempt 2 第 5 个 file 撞 32K 是 sub-line SENTENCE + 大表 + 多 file 累积所致,**单 file 单 dispatch 模式没问题**。下次 B-02 chapters 文件 (>1000 行) 才需要回到 hard-line-range 切片 (Pilot Attempt 2 验过的模式)。

### 1.2 Rule D 隔离 (writer ≠ reviewer)

4 batch + 1 cumulative audit = 5 lane,3 distinct subagent_type:
- writer × 5: `oh-my-claudecode:executor` (slot 70 reused, fresh dispatch each time)
- per-batch reviewer × 4: `oh-my-claudecode:scientist` (slot 72 reused)
- cumulative reviewer × 1: `oh-my-claudecode:code-reviewer` (slot 73, last burned at Pilot Attempt 1)

同 subagent_type 跨 batch 复用 OK (Rule D 只禁 writer=reviewer 同 atom),只要每次 fresh dispatch。**"独立"靠的是 dispatch 边界,不是 type 唯一性**。

### 1.3 Schema 优先 over dispatch prompt

Batch 02 executor 主动拒绝了我 dispatch prompt 里 3 处偏离 schema 的字段名 (`extracted_by` 形状 / `batch_id` 字段 / atom_type enum),全部 deferred 到 schema v1.2 frozen。**这是正确 behavior** — schema 是 frozen authority,dispatch prompt 是临时 instruction,冲突时 schema 赢。后续 batch 03 + 04 也都按 schema 走。

### 1.4 atom_id prefix 按 file_stem 约定

`md_model0X_aNNN` / `md_ch04_aNNN` / `md_dmCM_assn_aNNN` / `md_dmCM_ex_aNNN` — 都按 schema pattern `^md_[A-Za-z0-9_]+_a\d{3}$` + file_stem 派生。0 dup,0 pattern violation。可外推到 B-02 chapters / B-03+ domains。

### 1.5 atom_type 7-9/9 自然覆盖

batch 02 = 7/9 / batch 03 = 5/9 (源缺 4 类) / batch 04 = 7/9 (含 FIGURE 首次)。**LIST_ITEM/FIGURE/CODE_LITERAL/CROSS_REF 缺失要看源真实情况**,不是 prompt 缺陷。Reviewer 须接受 type-coverage 是 source-driven 自然分布,不是硬目标。

### 1.6 Cumulative cross-batch audit 制度

per-batch scientist 10-atom × 4 batch = 40/705 = 5.7% 抽审,**发现不了 batch 边界外的问题**。cumulative audit 派 code-reviewer 30-atom 跨 9 file 分层(覆盖 4 个 pilot 文件 + 4 个 B-01 文件 + 1 个 CM 桥接) 抓到了 1 HIGH (model/01 figure_ref null) + 2 v1.9.1 candidates,这是 per-batch scientist 看不到的盲区。**应固化为 inter-cycle gate**: 每 sub-cycle (B-01, B-02, ...) 闭环时跑一次 cumulative audit before 进下一个 sub-cycle。

---

## §2 必须补上的缺口 (gaps to fix before B-02)

### 2.1 [HIGH, hotfixed] md_model01_a013 figure_ref null

**问题**: pilot 期 (v1.8 prompt) 写 model/01 时 a013 FIGURE atom 的 figure_ref 写成 null,违反 v1.9 batch 04 验证过的 convention `md_<stem>_<topic>_concept_map`。

**Root cause**: v1.8 writer prompt 没显式要求 FIGURE 必填 figure_ref;schema 允许 figure_ref nullable for any atom_type (无 allOf 条件 enforce)。convention 是 writer prompt 隐式约定,v1.9 batch 04 落实了,v1.8 没落实。

**Fix applied (本 session)**: surgical Edit md_atoms.jsonl line 13, figure_ref null → `"md_model01_sdtm_domains_concept_map"` (镜像 batch 04 `md_model05_DI_concept_map` 命名)。extracted_by 加 `hotfix_2026-04-29T14:00:00Z` audit trail key (schema 无 additionalProperties:false 限制,合规)。验证: 0 FIGURE-null post-hotfix / 1102 atoms 不变 / 0 dup / 0 schema 缺字段。

### 2.2 [HIGH, v1.9.1 candidate V1] FIGURE figure_ref pre-DONE 校验 Hook A4

**问题**: writer prompt v1.9 没有 self-validate FIGURE 必填 figure_ref 的 hook。下次 B-02 / B-03+ 若再有 FIGURE atom (chapters / domain examples 概念图概率不低),可能再漏。

**Fix planned (B-02 入口前)**: writer prompt cut v1.9.1, 加 Hook A4:
```
[Hook A4 NEW pre-DONE FIGURE check]
For every emitted atom_type=FIGURE, verify figure_ref non-null AND matches pattern
md_<file_stem>_<topic_slug>_concept_map (canonical) OR
md_<file_stem>_<atom_id_hint>_<descriptor> (alt).
If figure_ref null/empty: DO NOT emit, fix and re-emit.
```

**Alt (lighter weight)**: 不 cut v1.9.1,直接在 B-02 dispatch template 加这个 self-check。这样 v1.9 baseline 不动。**推荐 alt**,因为 (a) v1.9 baseline 4-batch 100% PASS,不该轻易碰 (b) FIGURE atoms 在 B-02 chapters 中数量预期 < 5,dispatch-level 校验足够。

### 2.3 [MEDIUM, v1.9.1 candidate V2] parent_section 格式漂移

**问题**: 397 pilot atoms 用 v1.8 `§<num> [<title>]` 格式;705 B-01 atoms 用 v1.9 `§ <title>` (无中括号) 或带括号但风格不一。Cumulative audit reviewer 发现 4 sub-variants 跨 batch。**不是 schema violation** (schema 只要 parent_section non-empty string),但 corpus consistency 受影响。下游 P3 ledger / P4a matcher 若按 parent_section 分组,会因格式 drift 而误分。

**Fix planned (B-02 入口前)**: B-02 kickoff 文件**显式声明 canonical format** = `§<num>.<num> [<title>]` (v1.8 风格,因为 B-02 是 chapters/, 章节都有正式编号)。v1.9 model/* batch 用的简化格式 (§ <title>) 仅适用于无正式编号的 model 章节。**两种格式按"源是否有编号"分流,不强求统一**。

**Pilot 397 atoms re-emit 决策**: V3 LOW 候选 reviewer 建议 re-emit pilot atoms under v1.9 to enforce 全 corpus 一致。**否决**,理由:
- pilot 397 atoms schema 有效,只是 stylistic 差异
- re-emit 风险 > 收益: 重新走 writer + reviewer + Rule A,可能引入新 defect
- 下游 matcher 可在 normalization 步骤 strip 格式后比较 (engineering choice, not corpus mutation)
- pilot atoms 的 prompt_version 标 v1.8 是诚实的历史记录;改成 v1.9 是 backdating

### 2.4 [LOW, my own dispatch prompt 写偏 3 次]

**问题**: 我在 batch 02/03/04 dispatch prompt 里都凭印象写字段名,3 次都偏离 schema:
- `extracted_by` 写成 `{subagent_type, model, session_date}` 应是 `{subagent_type, prompt_version, ts}`
- 加了 `batch_id` 字段不在 schema
- atom_type 写成 `CODE_BLOCK / FIGURE_CAPTION / CALLOUT` 应是 `CODE_LITERAL / FIGURE / NOTE`

Executor 都正确反弹回 schema,没造成实际 atom 污染。但如果 executor 信我的 dispatch 而非 schema,后果严重。

**Fix (本 session 后续 + 永久)**: 把 schema 字段表 + atom_type 9-enum 抽成 dispatch template 顶部 inline 引用 (不再凭印象)。下次 B-02 dispatch 第一行就是从 schema 复制的字段约束。

### 2.5 [LOW carry-forward] md_model06_a029 line off-by-one

**问题**: a029 HEADING atom 的 line_start=43,实际 heading 在 line 42。1/109 = 0.9% drift,孤立。

**Fix decision**: **defer**,不修。理由: (a) verbatim 字符串正确,只是 line metadata off-by-one (b) 下游 matcher 主要用 verbatim,line 是辅助 (c) 单点偏差,不是系统 pattern (cumulative audit 跨 9 file sweep 没有第二例) (d) 修这一个原子的 cost 不值得 surgical edit。**留 v1.9.1 backlog,B-02 batch 期间若再现同 pattern 才升级**。

---

## §3 关键决策复盘 (decisions reviewed)

### 3.1 H_C 假说 REJECTED → N21 全 ban writer-family 扩 MD-side

**Pilot Attempt 1 实证**: oh-my-claudecode:writer 在 MD-side narrative + table + list 上有 3 类系统缺陷 (TABLE_HEADER 100% overflow / bold-as-HEADING 14 atoms / LIST_ITEM 截断)。round 14 H_C "content-conditional writer-direction reliability" 假说 REJECTED。N21 PDF-side ban 外推到 MD-side。

**B-01 4-batch 验证**: 单 writer (executor) lock + drift cal WAIVED,4-batch 100% PASS。**实证 N21 MD-side 扩展正确,不需要回炉**。

### 3.2 sub-line SENTENCE 接受为合法 (§R-C1 codification)

Pilot Attempt 2 §3 主 session 直接验证 byte-exact substring → reviewer 严格判 67% FAIL_VERBATIM 是 over-strict 解读,reclassify 后 30/30 PASS。v1.9 cut 入 §R-C1 显式允许。

**B-01 4-batch 验证**: batch 01 4 sub-line / batch 02 不详 / batch 03 19 sub-line / batch 04 7 sub-line — 全部 byte-exact 验证 PASS。**§R-C1 codification 正确,scaled cleanly**。

### 3.3 Cumulative audit 必要性 — 决策正解

**用户 push "尽量严格一点"** 触发 Option B (cumulative audit before B-02)。**结果**: per-batch scientist 4 × 10-atom = 40/705 = 5.7% 抽审无法覆盖 pilot 期 4 文件 (model/01, ch04 lines 1-300, CM/assumptions, CM/examples, model/04),cumulative audit 30-atom 跨 9 file 抓到 model/01 a013 figure_ref null HIGH 缺陷。

**没做 Option A 的反事实**: 直接进 B-02 → model/01 figure_ref null 缺陷遗留 → B-02 做完发现某下游 matcher fail → 根因排查会回追到 P2 Pilot 期 v1.8 写入 → 修这个跨多个 step 的 backlog 比现在 in-place 修贵 5-10 倍。**Option B 是正解,规则 A 精神兑现**。

### 3.4 dispatch prompt 我自己 3 次写偏 — 写代码也要 schema-first

我在 dispatch prompt 里凭印象写字段,3 次写错。**Lesson**: 即使是临时 instruction,涉及 schema 字段时应直接复制 schema 内容,不要从记忆构造。下次 B-02 dispatch template 第一行就是 schema-quoted 字段表。

### 3.5 hotfix 加 audit trail (extracted_by 加 hotfix_<ts> key)

**决策**: 修 a013 figure_ref 时,在 extracted_by 里加 `hotfix_<ts>` key 记录修复来源 (cumulative_audit_post_B01 §7 V1)。**不删原 prompt_version=v1.8 / 不改 ts** — pilot 写入历史保真。schema extracted_by 无 additionalProperties:false 限制,加 audit key 合规。**这是规则 B 失败归档精神在 hotfix 上的延伸**: 修复轨迹也要可追溯,不能 silent rewrite。

---

## §4 量化指标

### 4.1 B-01 cycle 总账

| 指标 | 值 |
|---|---|
| Sub-cycle | B-01 (model/* 剩 4 文件) |
| Batches | 4 (model/06 / model/02 / model/03 / model/05) |
| Atoms produced | 705 (109 + 244 + 160 + 192) |
| Per-batch Rule A pass rate | 100% × 4 (40/40 atoms PASS) |
| Cumulative audit pass rate | 28/30 = 93.3% (≥90% gate PASS) |
| HIGH defects post-cycle | 0 (1 hotfixed in-cycle) |
| MEDIUM defects | 0 |
| LOW carry-forward | 1 (md_model06_a029 line off-by-one) |
| v1.9.1 candidates added | 3 (V1 HIGH figure_ref Hook / V2 MEDIUM parent_section format / V3 LOW pilot re-emit DEFERRED) |
| Writer dispatches | 4 (single executor, opus) |
| Reviewer dispatches | 5 (4 scientist + 1 code-reviewer) |
| Total executor + scientist + code-reviewer slots burned this cycle | 0 NEW slots (all reuse, fresh dispatch) |

### 4.2 全 P2 累积 (post B-01 close + hotfix)

| 指标 | 值 |
|---|---|
| md_atoms.jsonl total | **1102 atoms** (397 pilot + 705 B-01) / 0 dup / 100% schema 合规 |
| Files atomized | 9 / 141 in-scope = 6.4% |
| Atoms vs target | 1102 / ~10000 estimate ≈ 11% |
| FIGURE atoms total | 3 (md_model01_a013 + md_model05_a170 + md_model05_a184) all figure_ref non-null post-hotfix |
| atom_type 9-enum cumulative coverage | 8/9 (CROSS_REF 累计 1 atom from pilot Attempt 1; CODE_LITERAL/LIST_ITEM 等都 hit) |

---

## §5 B-02 入口 conditions checklist

进 B-02 前必满足:

- [x] **§2.1 hotfix 落地**: md_model01_a013 figure_ref 已修
- [ ] **§2.2 FIGURE 校验 hook**: B-02 dispatch template 加 FIGURE figure_ref 非 null self-check (light-weight, not v1.9.1 cut)
- [ ] **§2.3 parent_section format 声明**: B-02 kickoff 显式声明 canonical format (chapters 用 v1.8 编号风格 `§<num>.<num> [<title>]`)
- [ ] **§2.4 dispatch template 修正**: schema 字段表 + atom_type 9-enum 抽到 template 顶部, dispatch 不再凭印象写字段
- [x] **§2.5 LOW deferred**: md_model06_a029 不修, backlog 保留
- [ ] **B-02 multi-session kickoff**: 写 `multi_session/P2_B-02_batch_01_kickoff.md` (chapters 入口 / 估 5-10 batch)
- [ ] **本 retro 用户 ack**

---

## §6 下一 cumulative audit 触发条件

B-01 cumulative audit 沉淀的 inter-cycle gate 制度,B-02 入口前 / B-02 闭环后再触发一次。具体:

- **Trigger**: B-02 batch 全 PASS + 所有 batch atoms 入 root md_atoms.jsonl 后
- **Sample**: 30-atom 跨累积 N 文件分层 (B-01 close 9 file → B-02 close 14-19 file)
- **Reviewer**: code-reviewer (与 per-batch scientist 不同 type), opus
- **Gate**: ≥90% functional PASS
- **Findings 处理**: HIGH 必修在 B-03 入口前 / MEDIUM 入 v1.9.1 backlog 评估 / LOW carry-forward

---

*B-01 retrospective written 2026-04-29 same day as P1 CLOSURE + P2 Pilot + P2 Bulk B-01 4 batch + cumulative audit + hotfix. 收尾完整闭环点.*
