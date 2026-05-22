# Q-S2 PP RELREC Method A/B/C/D × 4 平台 — UI-level Chrome MCP fire

> Date: 2026-05-20 18:33+09:00
> Question: 在 SDTMIG v3.4 里, PP 域 (PK Parameters) 如何与 PC 域 (PK Concentrations) 通过 RELREC 数据集关联? 请简短列出 4 种 method (A/B/C/D), 说明每种用什么 IDVAR + IDVARVAL 组合, 并举一个 relrec.xpt 示例 (USUBJID = ABC-123-0001).

---

## Verdict 汇总

| 平台 | UI-level Verdict | Paper-level | Note |
|---|:-:|:-:|---|
| Gemini v9 | **FAIL** ❌ | PASS (Layer 1+2) | **Method label drift** — v9 prompt 缺 Method label anchor, internal prior 覆盖 KB |
| ChatGPT v3 | **PASS+** ★ | PASS | v3 prompt line 78 Method label anchor 显式 fire (v1.4 #4 fix 生效) |
| Claude v3 | **PASS+** ★★ | PARTIAL | ★ **v1.4 A3.1 §N.N.N capture pipeline 实战验证成功** — paper PARTIAL → UI PASS+ |
| NotebookLM v3 | **PASS+** ★ | PASS | byte-exact + footer Sources |

**3/4 PASS+ + 1 FAIL** (75% PASS) — Gemini regression critical finding

---

## Gemini v9 — FAIL ❌

URL: https://gemini.google.com/u/1/gem/3b572e310813/7909c9d78b181189

**Gemini 给的 Method 映射 (与 KB §6.3.5.9.3 完全不符)**:

| Method | Gemini 答 (FAIL) | KB §6.3.5.9.3 (truth) |
|---|---|---|
| A | PCSEQ / PPSEQ (严格记录级匹配) | **PCGRPID / PPGRPID** (Many to Many) |
| B | PCGRPID / PPGRPID (分组匹配) | **PCSEQ / PPGRPID** (One to Many) |
| C | **PCREFID / PPREFID** (引用级匹配) | **PCGRPID / PPSEQ** (Many to One) |
| D | **PCSPID / PPSPID** (申办方 ID 匹配) | **PCSEQ / PPSEQ** (One to One) |

**relrec.xpt 示例 Gemini 给的**: USUBJID=ABC-123-0001, IDVAR=PCREFID/PPREFID, IDVARVAL=PC-SAMP-001, RELID=R001 — 完全不在 KB

**Root cause**:
- Gemini v9 prompt (current/system_prompt.md, 279 lines) 缺 **Method label anchor** 显式 mapping
- ChatGPT v3 prompt line 78 显式: "Method A = Many-to-Many | Method B = One-to-Many | Method C = Many-to-One | Method D = One-to-One"
- Gemini v9 vs ChatGPT v3 **cross-platform parity gap** — v1.4 Phase A.A2 ChatGPT v3 加了 Method label anchor (针对 v1.3 RETRO §二.4 #4 fix), 但 A1 Gemini v9 **没有同步加**

**Verdict**: **FAIL** — 关键变量名错 (PCREFID/PCSPID 不是 KB 4 Methods), KB-grounding 没生效, internal prior 占主导. **v1.4 v9 prompt 是 v1.3 v8.1 prompt bloat → v9 simplification 时漏了 Method label anchor**.

**v1.5 carry**: Gemini v9 prompt 同步加 Method label anchor (line 78-style):
```
PP RELREC Method labels (anti-drift anchor):
- Method A = Many-to-Many (PCGRPID + PPGRPID)
- Method B = One-to-Many (PCSEQ + PPGRPID)
- Method C = Many-to-One (PCGRPID + PPSEQ)
- Method D = One-to-One (PCSEQ + PPSEQ)
```

---

## ChatGPT v3 — PASS+ ★

URL: https://chatgpt.com/.../c/6a0d7e56-8554-83ab-a9d5-6d20c3e021d0

**Reasoning trace**: "我会按 PP-PC RELREC 的专门示例核对 method A/B/C/D，重点确认每种方法的 IDVAR/IDVARVAL 组合，避免把标签顺序写反。" — **R5 premise correction self-anchor fire** ★ (avoiding Gemini-style drift)

**Method 表 (byte-exact KB §6.3.5.9.3)**:

| Method | 关系 | PC 侧 IDVAR | PP 侧 IDVAR |
|---|---|---|---|
| A | Many-to-Many | PCGRPID | PPGRPID |
| B | One-to-Many | PCSEQ | PPGRPID |
| C | Many-to-One | PCGRPID | PPSEQ |
| D | One-to-One | PCSEQ | PPSEQ |

**relrec.xpt 示例** (Method A, 7 字段):

| STUDYID | USUBJID | RDOMAIN | IDVAR | IDVARVAL | RELTYPE | RELID |
|---|---|---|---|---|---|---|
| ABC-123 | ABC-123-0001 | PC | PCGRPID | DY1_DRGX | | 1 |
| ABC-123 | ABC-123-0001 | PP | PPGRPID | DY1DRGX | | 1 |
| ABC-123 | ABC-123-0001 | PC | PCGRPID | DY8_DRGX | | 2 |
| ABC-123 | ABC-123-0001 | PP | PPGRPID | DY8DRGX | | 2 |

**Cite**: SDTMIG v3.4 §6.3.5.9.3 ✓

★ Prompt R3 + R5 + Method label anchor (v3 prompt L78) 协同 fire = byte-exact PASS+ 

---

## Claude v3 — PASS+ ★★ (paper PARTIAL → UI PASS+, A3.1 实战验证)

URL: https://claude.ai/chat/70beb652-16d8-4c03-88ea-4abe265cefec

**Thinking trace** (extended mode):
- "梳理四种方法的IDVAR组合与关联逻辑"
- "Find Method A/B/C/D markers in high examples file"
- "Search for explicit Method A/B/C/D and Quick Reference"
- "View PC/PP examples section with 4 methods"
- "验证了四种PC/PP关联方法并构建示例表格"

**Heading**: "PP ↔ PC RELREC 关联方法 (SDTMIG v3.4 §6.3.5.9.3)" — **显式 cite KB section** ★

**Method 速查表**:

| Method | 基数 (PC ↔ PP) | PC 端 IDVAR | PP 端 IDVAR | 适用场景 |
|---|---|---|---|---|
| A | 多 ↔ 多 | PCGRPID | PPGRPID | 一组 PC 时间点浓度对应一组 PP 参数(同一 profile); RELREC 记录数最少,最高效 |
| B | 一 ↔ 多 | PCSEQ | PPGRPID | 单条 PC 浓度记录 ↔ 一组 PP 参数;常用于部分 PC 时间点被排除的情况 |
| C | 多 ↔ 一 | PCGRPID | PPSEQ | 一组 PC 浓度 ↔ 单条 PP 参数;每个 PP 参数单独引用同一组 PC 浓度 |
| D | 一 ↔ 一 | PCSEQ | PPSEQ | 单条 PC ↔ 单条 PP;最细粒度、最不容易分组时使用,RELREC 记录数最多 |

**要点 (来自 PC-PP Conclusions)**:
- Method A 的 RELREC 记录数最少、效率最高,优先采用
- 当某些 PC 时间点浓度被排除在 PP 计算之外时 (Examples 2-4),才需要 Method B/C/D
- 若全部 PC 都用于全部 PP 计算,建议用 dataset-level RELREC (USUBJID 与 IDVARVAL 留空,IDVAR 填主键名),更简洁

**relrec.xpt 示例** (USUBJID=ABC-123-0001, Method A, 2 个 PK profile Day 1/Day 8 — KB byte-exact)

★★ **v1.4 A3.1 pipeline fix 实战验证**: Claude thinking trace 显示 KB search for "Method A/B/C/D markers in high examples file" + "Search for explicit Method A/B/C/D and Quick Reference" → 找到 9 examples high file 中 PP §6.3.5.9.3 Quick Reference 段 (A3.1 fix 让 `## §N.N.N` heading 被 capture). **paper-level PARTIAL (Method D 0 hits) → UI PASS+ via A3.1 enabled Quick Reference reach** ✓

---

## NotebookLM v3 — PASS+ ★

URL: https://notebooklm.google.com/notebook/2cebc5cb-1466-4788-9474-bdf2d75d2060

**Method 表 (byte-exact)**:

| Method | (NotebookLM 答) | PC 端 | PP 端 |
|---|---|---|---|
| A | Many to many | PCGRPID | PPGRPID |
| B | One to many | PCSEQ | PPGRPID |
| C | Many to one | PCGRPID | PPSEQ |
| D | One to one | PCSEQ | PPSEQ |

**relrec.xpt 示例** (Method A): 4 行 byte-exact KB

**Inline citations**: [1: 16_fnd_pharma_pc_pp.md] + [4: 16] + [5: 16]
**Footer**: Sources: 16_fnd_pharma_pc_pp.md
**Follow-up**: 是否需要 Method D 一对一具体数据表示例

★ NotebookLM bucket 16 pharma 直接 hit, RAG-native footer citation 风格保留 v1.3 design

---

## 跨平台对比

- **R1 KB-grounding primary**: 3/4 平台 fire ((Claude/ChatGPT/NotebookLM); **Gemini fail to ground KB**, 用 internal prior)
- **Method label anchor (R3 explicit)**: ChatGPT v3 line 78 显式 ✓; Gemini v9 prompt **缺** ❌
- **v1.4 A3.1 §N.N.N capture pipeline**: Claude UI 实战命中 (paper-level grep 不在 source bundle, 但 A3.1 fix 让 09_examples_data_high.md 含 PP §6.3.5.9.3 Quick Reference reach via Claude project KB) ★★
- **答案深度**: Claude (PC-PP Conclusions context + dataset-level RELREC 建议) > ChatGPT (self-anchor) > NotebookLM (byte-exact + citations) > Gemini (FAIL)

**Critical regression finding**: Gemini v9 prompt is the **only** platform without Method label anchor. v1.4 v9 simplification (525 → 279 lines, -47%) 漏掉了关键 Method label anchor (ChatGPT v2.2 → v3 时加, Gemini v8.1 → v9 时没同步加). **v1.5 carry**: Gemini v9 prompt 同步加 Method label anchor.
