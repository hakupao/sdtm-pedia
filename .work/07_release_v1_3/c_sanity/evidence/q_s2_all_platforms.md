# Q-S2 — PP RELREC linking 4 Methods (Phase A1 v1.3 KB 改动验证)

> Date: 2026-05-20 PM
> Q-S2 source: c_sanity_plan.md
> Verdict: **2 PASS+ + 1 PARTIAL + 1 FAIL** ⚠️

---

## 题目

> 在 SDTMIG v3.4 里, PP 域 (PK Parameters) 如何与 PC 域 (PK Concentrations) 通过 RELREC 数据集关联? 请简短列出 4 种 method (A/B/C/D), 说明每种用什么 IDVAR + IDVARVAL 组合 (例如 PCSEQ / PCGRPID / PPSEQ / PPGRPID), 并举一个 relrec.xpt 示例 (USUBJID = ABC-123-0001).

## 期望命中 (per v1.3 KB §6.3.5.9.3 Phase A1 fix)

- Method A — Many-to-Many — PCGRPID + PPGRPID
- Method B — One-to-Many — PCSEQ + PPGRPID
- Method C — Many-to-One — PCGRPID + PPSEQ
- Method D — One-to-One — PCSEQ + PPSEQ
- relrec.xpt for ABC-123-0001

---

## 4 平台 verdict

### Gemini Gem — **FAIL** ⚠️

完全没用 v1.3 KB §6.3.5.9.3 Method 内容. 答出错误版本:
- ❌ 开头说 "PP 和 PC 不通过 RELREC 关联" (与 §6.3.5.9.3 本质相反)
- ❌ Method A/B/C/D: PCSEQ+PPLNKID / PCGRPID / PCREFID / 自定义 LNKID — **完全不对应 v1.3 KB 的 4 methods**
- ❌ 幻觉变量 PPLNKID (PP 域 spec 无此变量)
- ❌ 引用 `knowledge_base/domains/RELREC/` (KB 无此目录)

**核心问题**: Gemini 没有检索到 v1.3 新加入 PP/examples.md §6.3.5.9.3 RELREC Method Quick Reference 内容; 改为依赖 training prior 编造了一套与 SDTMIG 不符的 method 命名.

### ChatGPT — **PARTIAL** ⚠️

4 IDVAR 组合正确但 method labels 与 v1.3 KB 错位:
- ChatGPT Method A (PCGRPID+PPSEQ) = KB Method C
- ChatGPT Method B (PCSEQ+PPSEQ) = KB Method D
- ChatGPT Method C (PCGRPID+PPGRPID) = KB Method A
- ChatGPT Method D ("多 PCSEQ→PPSEQ") = **不在 KB 4 methods 内**, 漏 KB Method B (One-to-Many)

内容大致对, label 错. Cardinality 语言 (Many-to-Many 等) 也没用. 内部知识 vs KB 优先级偏内部.

### Claude — **PASS+** ★★

完美匹配 v1.3 KB §6.3.5.9.3:
- ✅ Method A — Many-to-Many — PCGRPID + PPGRPID
- ✅ Method B — One-to-Many — PCSEQ + PPGRPID
- ✅ Method C — Many-to-One — PCGRPID + PPSEQ
- ✅ Method D — Record-by-Record (≈ One-to-One) — PCSEQ + PPSEQ
- ✅ relrec.xpt for ABC-123-0001 + PCGRPID=DY1_DRGX (KB Method A 原文)
- ✅ Cross-ref: §8.2.2 RELREC examples + §8.3.1 RELTYPE rules
- ✅ Method C 标 "PP Example 3 实测样式"
- ⚠️ Self-flagged: "Method C/D 在 KB 描述被截断" — claude compressed bundle 可能丢了 PP/examples.md L155 之后的 Method D 内容, 但 claude reconstruct from §6.3.5.9.3 PC Examples 2-4 内容仍 correct

### NotebookLM — **PASS+** ★★

完美匹配 v1.3 KB §6.3.5.9.3:
- ✅ Method A (多对多/Many-to-Many) — PCGRPID + PPGRPID
- ✅ Method B (一对多/One-to-Many) — PCSEQ + PPGRPID
- ✅ Method C (多对一/Many-to-One) — PCGRPID + PPSEQ
- ✅ Method D (一对一/One-to-One) — PCSEQ + PPSEQ
- ✅ relrec.xpt 完整 Day 1 + Day 8 双 RELID example
  - Row 1: PC | ABC-123-0001 | PCGRPID | DY1_DRGX | RELID=1
  - Row 2: PP | ABC-123-0001 | PPGRPID | DY1DRGX | RELID=1
  - Row 3: PC | ABC-123-0001 | PCGRPID | DY8_DRGX | RELID=2
  - Row 4: PP | ABC-123-0001 | PPGRPID | DY8DRGX | RELID=2
- ✅ Method D use-case 描述深入 ("某特定时间点浓度仅未参与半衰期计算, 但参与 AUC")
- ✅ Footer citation `Sources: 16_fnd_pharma_pc_pp.md` (v1.3 citation style)
- ✅ 主动 follow-up: "您是否需要查看更复杂的 Method C 或 Method D 的展开数据示例?"

---

## v1.3 KB Phase A1 fix 验证

| 平台 | bundle 含 v1.3 PP/examples.md §6.3.5.9.3? | 答出 KB 4 methods? |
|---|:-:|:-:|
| Gemini | ✓ (`03_domains_examples.md` +5,432 bytes) | ❌ (内部知识 override) |
| ChatGPT | ✓ (`06_domain_examples_all.md` +5,432 bytes) | ⚠️ partial (labels 错位) |
| Claude | ✓ (`09_examples_data_high.md` +592 bytes) | ✅ (matched + Self-aware truncation) |
| NotebookLM | ✓ (`16_fnd_pharma_pc_pp.md` +2,620 bytes) | ✅ (matched + bonus Day 8 example) |

**Phase A1 fix 在 4 平台 bundles 内容验证 (B3 oracle): byte-exact 一致**. 但 LLM-level retrieval performance:
- Claude + NotebookLM: 强 KB-grounded retrieval, 答出与 KB 一致
- ChatGPT: 中等, 部分 KB-grounded
- Gemini Gem v8.1: 弱, KB content 在 file 内但 LLM 没引用, 反而 hallucinate

## 分析: Gemini FAIL 是 v1.3 regression?

**No** — 这是 **pre-existing Gemini 弱点, 不是 v1.3 引入的 regression**:
- v1.3 KB rebuild B3 oracle 已 confirm 4 平台 byte-exact 一致 — KB content 正确
- Claude + NotebookLM 用同一 KB content 答出正确 4 methods → 证明 KB content 在 bundle 内
- Gemini 的失败是 retrieval/prior-knowledge override 问题, 非 KB 内容缺失

**对照 R3 (2026-05-19) SMOKE_V4 baseline**:
- R3 Gemini v7.1 had 4 FAIL: Q3 BE/BS/RELSPEC, Q4 IS routing, Q11 Dataset-JSON, AHP1 LBCLINSIG
- v1.2 v8.1 patched these 4
- Q-S2 PP RELREC was **not in R3 17 题, 没 baseline 比对**
- 但同类型问题 (PC RELREC, ch08 RELREC) 在 R3 Gemini 没 fail

**结论**: Gemini Q-S2 FAIL 是新发现的 weakness, 不是 v1.3 regression. KNOWN_LIMITATIONS §0 添 entry.

## 决策树命中

per c_sanity_plan.md:
- ≥1 FAIL on previously-PASS platform: Q-S2 没 R3 baseline, 不算 regression
- PARTIAL > 4: 当前 1 PARTIAL (ChatGPT Q-S2)

→ **不 halt, 继续 Q-S3 / Q-S4**

## v1.4 carries (从本 Q-S2 derived)

| Finding | v1.4 action |
|---|---|
| Gemini PP RELREC retrieval 弱 | v1.4 Gemini prompt 加 PP RELREC 锚点; 或 03_domains_examples.md split 让 §6.3.5.9.3 内容更显眼 |
| ChatGPT method label 混淆 | v1.4 06_domain_examples_all.md PP §6.3.5.9.3 段标更明显; 加 "Method A=Many-Many, Method B=One-Many, ..." 锚点 |
| Claude self-truncation flag | v1.4 claude compress_assumptions/examples 脚本检查 PP/examples.md §6.3.5.9.3 块是否完整传输 |

## 最终 verdict

- 2 PASS+ (Claude, NotebookLM) — v1.3 KB Phase A1 fix 在这两平台**充分生效**
- 1 PARTIAL (ChatGPT) — KB 内容部分进入答案, label shuffled
- 1 FAIL (Gemini) — KB 内容在 bundle 内但 LLM 没正确 surface; 留 v1.4 prompt patch

**Q-S2 总分**: 2 PASS+ + 1 PARTIAL + 1 FAIL = 6/16 (按 PASS+ = 2pt, PASS = 1pt, PARTIAL = 0.5pt, FAIL = 0pt) — 但单 Q 的 verdict 是 "PARTIAL across platforms".
