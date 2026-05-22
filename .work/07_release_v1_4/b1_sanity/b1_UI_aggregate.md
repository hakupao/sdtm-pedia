# v1.4 B1 Light Sanity — UI-level Aggregate (16 cells via Chrome MCP)

> Date: 2026-05-20 19:00+09:00
> Method: Chrome MCP fire to user-deployed 4 平台 UI, new conversation per cell, fire-and-forget then collect
> 跨 paper-level: paper 13/16 strict PASS + 3 PARTIAL + 0 FAIL → UI 15/16 PASS + 0 PARTIAL + 1 FAIL

---

## 16 cells UI Verdict 网格

| 题 \ 平台 | Gemini v9 | ChatGPT v3 | Claude v3 | NotebookLM v3 |
|---|:-:|:-:|:-:|:-:|
| Q-S1 BECAT EXTRACTION | **PASS+** | **PASS** | **PASS+** ★ | **PASS** |
| Q-S2 PP RELREC Method A/B/C/D | **FAIL** ❌ | **PASS+** ★ | **PASS+** ★★ | **PASS+** ★ |
| Q-S3 TR TRSTRESN/TRSTRESU | **PASS** | **PASS+** ★ | **PASS+** ★ | **PASS+** ★ |
| Q-S4 DI domain | **PASS+** | **PASS+** ★ | **PASS+** ★ | **PASS+** ★ |

**Aggregate**: 11 PASS+ + 4 PASS + 0 PARTIAL + 1 FAIL = **15/16 = 93.75%** ≥ B1 decision tree threshold (14/16 = 87.5%) → **APPROVE**

---

## Cells 与 paper-level 比较 (UI - paper delta)

| Cell | Paper-level (Layer 1+2 grep) | UI-level (real platform) | Delta |
|---|---|---|---|
| Q-S1 Gemini | PASS | PASS+ | ✓ same/better |
| Q-S1 ChatGPT | PASS | PASS | ✓ same |
| Q-S1 Claude | **PARTIAL** | **PASS+** ★ | **+2** (paper PARTIAL → UI PASS+ via R5 premise correction + Example 2 reasoning bridge) |
| Q-S1 NotebookLM | PASS | PASS | ✓ same |
| Q-S2 Gemini | PASS | **FAIL** ❌ | **-2** (paper Layer 1 PASS missed Method label anchor missing; UI exposes internal prior 覆盖 KB) |
| Q-S2 ChatGPT | PASS | PASS+ | ✓ same/better (v3 prompt L78 Method label anchor 生效) |
| Q-S2 Claude | **PARTIAL** | **PASS+** ★★ | **+2** (paper KB grep miss Method D + Quick Ref; UI A3.1 §N.N.N pipeline 实战命中) |
| Q-S2 NotebookLM | PASS | PASS+ | ✓ better (bucket 16 RAG-native) |
| Q-S3 Gemini | PASS | PASS | ✓ same |
| Q-S3 ChatGPT | PASS | PASS+ | ✓ better |
| Q-S3 Claude | PASS | PASS+ | ✓ better |
| Q-S3 NotebookLM | PASS | PASS+ | ✓ better |
| Q-S4 Gemini | PASS | PASS+ | ✓ better |
| Q-S4 ChatGPT | PASS | PASS+ | ✓ better |
| Q-S4 Claude | **PARTIAL** | **PASS+** ★ | **+2** (paper KB 06_assumptions:331 truncated; UI §9.1+§2.4 dual cite reasoning bridge) |
| Q-S4 NotebookLM | PASS | PASS+ | ✓ better |

**Delta summary**:
- **3 paper PARTIAL → UI PASS+** (all 3 Claude bundle KB gap cells, paper严格 grep miss, UI reasoning bridge upgrade)
- **1 paper PASS → UI FAIL** (Gemini Q-S2 Method label drift, paper Layer 1 grep 没 catch missing anchor)
- **11 cells UI strictly better than paper** (extra depth)
- **4 cells UI same as paper**
- **1 cell UI worse than paper** (Gemini Q-S2)

---

## 关键发现

### ★★ Finding 1: paper-level PARTIAL → UI-level PASS+ reasoning bridge 验证

3 Claude PARTIAL cells (Q-S1 BECAT, Q-S2 PP RELREC Method D, Q-S4 DI) 在 UI-level 全升级为 PASS+:
- **Q-S1 Claude**: R5 premise correction "三 canonical 非 CT 列表" + Example 2 cell-free RNA from plasma 完整 9 行表 → 答出 sponsor-extensible
- **Q-S2 Claude**: **v1.4 A3.1 §N.N.N capture pipeline 实战验证成功** ★★ — Claude extended thinking 中找到 09_examples_data_high 含 PP §6.3.5.9.3 Quick Reference 段 (A3.1 fix 在 v1.4 中加入的 SECTION_HDR_RE capture rule)
- **Q-S4 Claude**: §9.1 + §2.4 dual cite, Study Reference 独立第 5 类 binding, 跨 03_model.md + 06_assumptions.md reasoning

**结论**: paper-level Layer 2 byte grep PARTIAL 是过分严格的 verdict; UI-level 实际用户体验中, 平台 reasoning bridge + extended thinking 可弥补 KB bundle 字面缺失. **UI-level sanity 是 paper-level 的必要补充**.

### ⚠️ Finding 2: Gemini Q-S2 Method label drift FAIL (critical regression)

Gemini v9 prompt 在 PP RELREC Method A/B/C/D 题上**完全 hallucinate**:

| Method | Gemini 答 (FAIL) | KB §6.3.5.9.3 (truth) |
|---|---|---|
| A | PCSEQ / PPSEQ | **PCGRPID / PPGRPID** (Many to Many) |
| B | PCGRPID / PPGRPID | **PCSEQ / PPGRPID** (One to Many) |
| C | **PCREFID** / PPREFID (虚构) | **PCGRPID / PPSEQ** (Many to One) |
| D | **PCSPID** / PPSPID (虚构) | **PCSEQ / PPSEQ** (One to One) |

**Root cause**: Gemini v9 prompt 缺 **Method label anchor**:
- ChatGPT v3 prompt L78 显式: `Method A = Many-to-Many | Method B = One-to-Many | Method C = Many-to-One | Method D = One-to-One` (v1.4 #4 fix 针对 v1.3 RETRO §二.4 ChatGPT label drift)
- Gemini v9 prompt 在 v8.1 (525) → v9 (279) simplification 时**漏掉**了同步加 Method label anchor — A1 vs A2 cross-platform parity gap

**Critical v1.4 finding**: paper-level Layer 1 grep 验证 R1+R2+R3 essential rules 都在, 但**没 catch Method label anchor 这种 question-specific anchor 的 cross-platform 不一致**. UI-level fire 暴露真实 prompt design gap.

### v1.5 Carries (from this UI sanity)

1. **Gemini v9 prompt 同步加 Method label anchor** (line 78-style):
   ```
   PP RELREC Method labels (anti-drift anchor):
   - Method A = Many-to-Many (PCGRPID + PPGRPID)
   - Method B = One-to-Many (PCSEQ + PPGRPID)
   - Method C = Many-to-One (PCGRPID + PPSEQ)
   - Method D = One-to-One (PCSEQ + PPSEQ)
   ```
   (并同步 Claude v3 + NotebookLM v3 prompts; 不仅 ChatGPT 一家)

2. **paper-level sanity protocol 加强**: Layer 1 grep R1+R2+R3 essential rules 不够, 应加 **question-specific anchor cross-platform parity check** (对每个 sanity 题 grep 平台 prompt 中是否有 题目相关 anchor; mismatch warning).

3. **UI-level sanity 应作为 Phase B.B1 必跑** (不只 paper-level optional). 本次 UI-level 暴露 1 critical FAIL paper-level 没 catch.

---

## Decision tree apply (UI-level)

```
15/16 PASS (含 11 PASS+) + 0 PARTIAL + 1 FAIL
≥14/16 threshold: 15 ≥ 14 ✓
1 FAIL: 注 Gemini Q-S2 Method label drift, v1.4 v9 prompt cross-platform parity gap, v1.5 carry
```

**Verdict**: **B1 UI-level APPROVE** with documented Gemini Q-S2 FAIL → v1.5 carry "Gemini v9 prompt Method label anchor sync"

vs paper-level "APPROVE WITH KNOWN_KB_GAP" (3 Claude PARTIAL bundle gap) → 现在 paper PARTIAL 全 UI 升级 PASS+; 新发现 Gemini prompt parity gap.

---

## Rule A 16 UI probes

每 cell 1 UI probe = 16 probes 累计 (UI-level Rule A 抽检).
- PASS+: 11
- PASS: 4
- PARTIAL: 0
- FAIL: 1

---

## Disposition / Next

1. ✅ Q-S1/S2/S3/S4 UI evidence 写 (4 文件)
2. ✅ b1_UI_aggregate.md (本文件)
3. Update audit_matrix.md B1 row 加 UI 数据
4. Update _progress.json B1 verdict (paper 13/16 + UI 15/16, reconciled APPROVE)
5. Append trace.jsonl B1 UI events
6. Update B1_SANITY_RETROSPECTIVE.md 加 UI section + Gemini Q-S2 critical finding
7. **Critical: Gemini v9 prompt v1.5 carry 显式 doc 进 KNOWN_LIMITATIONS** (Method label anchor cross-platform parity)

---

## 与 v1.3 c_sanity 模式对比

v1.3 c_sanity (Phase C 14-15/16 PASS APPROVE): 用 Chrome MCP fire-and-forget 跑 16 cells UI-level. 也发现 Gemini PP RELREC fail (v1.3 RETRO §二.1 触发 v1.4 Gemini prompt v8.1 → v9 refactor MAIN).

v1.4 B1 UI sanity 用同样方法 (continuity), 验 v9 prompts 是否解决 v1.3 RETRO 触发的问题:
- v1.3 RETRO §二.1 Gemini PP RELREC fail → v1.4 Gemini v9 simpler (vs v8.1)
- **v1.4 B1 UI sanity 反而暴露**: Gemini v9 PP RELREC **仍 fail** (Method label drift), 因 v9 simplification 漏掉 Method label anchor
- **v1.5 必修**: Gemini v9 prompt 加 Method label anchor (同 ChatGPT v3 L78 pattern)

**B1 UI sanity 比 paper-level 更早暴露 prompt parity gap, 应固化进 Phase B 必跑流程**.
