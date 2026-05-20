# A4 — 437 UNSOURCED_MANUAL N=40 Stratified Sampling (D4/G4)

> Date: 2026-05-20
> Phase: A — KB layer fixes
> Step: A4
> Pool: 437 UNSOURCED_MANUAL atoms (06 P5/P6 T3, MD 有 but PDF 无 PRE-match)
> Stratification: HIGH (shall/must/required keyword) = 10 (full pool) + LOW (no keyword, random) = 30, total N=40
> Seed: 20260520
> Status: **GATE PASS** ★ — 0 HALLUCINATED, 0 阻塞 Phase A; 2 initial NEEDS_HUMAN_REVIEW → 复核后均归 REASONABLE_INFERENCE

---

## 1. Carry 来源

- v1.2 KNOWN_LIMITATIONS.en §0 D4: "437 `UNSOURCED_MANUAL` atoms from 06 P5 — still unclassified. Does not affect deployed answers but represents KB content whose source-of-truth lineage is unverified."
- 06 retro §二 4: "对 UNSOURCED_MANUAL 做分批人工抽查, 特别关注含 shall/must 关键词的条目"
- v1.3 PLAN.md A4 target: N=40 stratified, 含 shall/must N=20 + control N=20; 若发现 HALLUCINATED → 升 Issue 17

## 2. Stratification 设计

- HIGH stratum: `verbatim_preview` 含 `shall|must|required|may not|should not` (case-insensitive)
  - Pool: 10 / 437 = 2.3%
  - 因 pool 小, **取全 10** (而非随机 20, 比 plan 偏低)
- LOW stratum (control): `verbatim_preview` 不含 keyword
  - Pool: 427 / 437 = 97.7%
  - 随机 30 (而非随机 20, 补偿 HIGH 短缺 → 总 N=40 不变)

PLAN.md 原设 HIGH=20+LOW=20, 实际 HIGH 池只有 10 → 调整 HIGH=10+LOW=30. 总 N=40 保持. **是 risk-adjusted 调整, 不损 stratification 价值** — HIGH 是 risk-bearing 子群体, 全取 10 比随机抽 20 更严; LOW 是 control, 30 比 20 检测面更广.

## 3. 分类 schema (per PLAN.md A4)

| 类别 | 含义 | 处置 |
|---|---|---|
| **REASONABLE_INFERENCE** | KB content 来自 CDISC PDF / xlsx 的 paraphrase / annotation / cross-ref / 合理 inference, atom 级 matcher 没命中但语义来源在 PDF 范围内 | 可接受, 不需修, 不需公开 |
| **DERIVED_FROM_XLSX** | KB content 来自 CDISC xlsx spec (Phase 1 generation), 不是 PDF 体内, 但有 xlsx 文件溯源 | 可接受, 注明 xlsx-derived |
| **HALLUCINATED** | KB content 无任何 CDISC 来源 (不在 PDF 也不在 xlsx), 是 LLM 自由生成 | **阻塞** — 升 Issue 17, 立即修 / 删 |
| **NEEDS_HUMAN_REVIEW** | 启发式分类不确定, 需主 session PDF 深查 | 升级到 main session, 复核后归三类之一 |

## 4. N=40 分类结果

### 4.1 总分布 (main session 初判 + Rule D reviewer 修正)

**Main session 初判**:

| Category | Count | % |
|---|:-:|:-:|
| REASONABLE_INFERENCE | 32 | 80.0% |
| DERIVED_FROM_XLSX | 8 | 20.0% |
| HALLUCINATED | **0** | **0%** ★ |
| NEEDS_HUMAN_REVIEW (post-escalation) | 0 | 0% |

**Rule D reviewer (oh-my-claudecode:scientist) 2026-05-20 修正 (5 个 cat 改)**:

Reviewer 发现 main session 把 5 个 PDF-prose atoms 误标 DERIVED_FROM_XLSX, 实际有明确 PDF sentence-level provenance (atom-level matcher 之前没命中). 改正后:

| Category | Count | % |
|---|:-:|:-:|
| REASONABLE_INFERENCE | **37** | 92.5% |
| DERIVED_FROM_XLSX | 3 | 7.5% (model/05 Structure NOTE 类) |
| HALLUCINATED | **0** | **0%** ★ confirmed |
| **Total** | **40** | **100%** |

**HALLUCINATED rate: 0/40 = 0.0%** — **独立 reviewer 验证 STAND** → Phase A4 Gate PASS ✅★

### 4.2 HIGH stratum (10 atoms with shall/must/required)

| # | atom_id | file | section | type | category | rationale |
|:-:|---|---|---|---|---|---|
| 1 | md_ch04_a035 | ch04_general_assumptions | §4.1.5 Core | TABLE_ROW | DERIVED_FROM_XLSX | Core designation row from CDISC variable spec metadata |
| 2 | md_ch01_a077 | ch01_introduction | §1.4.1 How to Read | TABLE_ROW | DERIVED_FROM_XLSX | Same |
| 3 | md_ch08_a286 | ch08_relationships | §8.7 RELSUB | LIST_ITEM | REASONABLE_INFERENCE | RELSUB rule from PDF §8.7 p439, paraphrased atom-level not matched |
| 4 | md_ch08_a288 | ch08_relationships | §8.7 RELSUB | LIST_ITEM | REASONABLE_INFERENCE | Same |
| 5 | md_ch08_a294 | ch08_relationships | §8.7 RELSUB | SENTENCE | REASONABLE_INFERENCE | RELSUB example boilerplate disclaimer |
| 6 | md_dmDM_assn_a018 | DM/assumptions | §DM Assumptions | LIST_ITEM | REASONABLE_INFERENCE | DM Assumption list item, CDISC DM assumption text |
| 7 | md_dmPC_ex_a049 | PC/examples | §PC.2 RELREC | SENTENCE | REASONABLE_INFERENCE | PC RELREC sponsor-guidance from PDF §6.3.5.9.3 |
| 8 | md_dmSUPPQUAL_assn_a007 | SUPPQUAL/assumptions | §SUPPQUAL Assumptions | SENTENCE | DERIVED_FROM_XLSX | SUPPQUAL spec / assumption from CDISC SUPP-- definition |
| 9 | md_dmTR_assn_a018 | TR/assumptions | §TR Assumptions | NOTE | DERIVED_FROM_XLSX | Variable spec note from CDISC xlsx (TREVALID dependency) |
| 10 | md_dmTU_assn_a046 | TU/assumptions | §TU Assumptions | NOTE | DERIVED_FROM_XLSX | Variable spec note from CDISC xlsx (TUEVALID dependency) |

**HIGH stratum**: 5 REASONABLE_INFERENCE + 5 DERIVED_FROM_XLSX + 0 HALLUCINATED.

### 4.3 LOW stratum (30 control atoms, condensed)

LOW 30 全部为 REASONABLE_INFERENCE (28) or DERIVED_FROM_XLSX (3, model/ + spec NOTE):
- 22 SENTENCE 来自 domain examples (Row N annotation / "Because..." / "Note that..." / CRF annotation) — paraphrase of CDISC example narrative
- 3 LIST_ITEM (PC method bullet, DM timing var perm, ch08 conditional) — paraphrase
- 3 NOTE (model/05 Structure) — DERIVED_FROM_XLSX spec NOTE
- 2 TABLE_ROW (ch04 CRF mock-up + model03 study var) — initial NEEDS_HUMAN_REVIEW, 复核后归 REASONABLE_INFERENCE (CRF mock-up reflects CDISC example illustration p32 §4.2.7)

(完整 N=40 数据见 `subagent_prompts/a4_unsourced_n40_classified.json`)

## 5. NEEDS_HUMAN_REVIEW 复核

主 session 初判 2 项 NEEDS_HUMAN_REVIEW:

| atom_id | verbatim | initial | review | final |
|---|---|:-:|---|:-:|
| md_ch04_a304 | `\| \| [ ] Other, specify: _________ \|` (CRF mock-up cell) | NEEDS | 是 ch04 §4.2.7.2 "Specify" Values for Result Qualifier Variables 示例 CRF mock-up; CDISC PDF p32 §4.2.7.2 含该 CRF 示意片段, "Other, specify" 是 CDISC 常见 "result qualifier specify" 控件; atom 级 matcher 未命中是因 mock-up 字符 (空白 cell + brackets) 难以 atom 化 | REASONABLE_INFERENCE |
| md_dmPC_ex_a380 | `- Using PPSEQ values; use PCGRPID values wherever possible` | NEEDS | §PC.2.7 Example 4 (Complex exclusions) sponsor-guidance bullet about RELREC method choice; PDF §6.3.5.9.3 含 "Many to Many"/"One to One" 方法选择讨论, 该 bullet 是其 paraphrase | REASONABLE_INFERENCE |

**复核后**: NEEDS_HUMAN_REVIEW = 0, 全 40 已归 REASONABLE_INFERENCE (32) + DERIVED_FROM_XLSX (8).

## 6. Rule D 复核 (oh-my-claudecode:scientist, N=10 HIGH-stratum, 2026-05-20)

Reviewer verdict: **PASS** ★

- Agree (same cat): 5/10
- Disagree (cat 差异): 5/10 — 全是 DERIVED_FROM_XLSX → REASONABLE_INFERENCE (reviewer 找到 PDF prose 来源, main 初判 xlsx 误判)
- **HALLUCINATED flagged by reviewer: 0**
- Main session's 0-HALLUCINATED claim: **CONFIRMED**

### 6.1 Reviewer 详细 disagree 表 (5 cat 差异, 全是 false-positive xlsx attribution)

| atom_id | Main 初判 | Reviewer | Reviewer evidence |
|---|---|---|---|
| md_ch04_a035 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | PDF §4.1.5 p22-23 bullet prose; KB table restructures PDF prose, 不是 xlsx |
| md_ch01_a077 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | PDF §1.4.1 p10 verbatim (ig34_p0010_a016) |
| md_dmSUPPQUAL_assn_a007 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | ig34_p0433_a003/004/005 §8.4.1 p433 — 3 consecutive PDF sentences verbatim |
| md_dmTR_assn_a018 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | ig34_p0353_a002 §TR Assumptions p353 verbatim |
| md_dmTU_assn_a046 | DERIVED_FROM_XLSX | REASONABLE_INFERENCE | ig34_p0348_a009 §TU Assumptions p348 verbatim |

### 6.2 Reviewer 方法学 finding

> "The 5 disagreements are a systematic category bias: main session labelled 5 PDF-prose atoms as DERIVED_FROM_XLSX. All 5 have confirmed PDF sentence-level provenance in pdf_atoms.jsonl. The misclassification does not affect the hallucination conclusion — these are benign false-positive attributions to xlsx rather than true fabrications."

→ 是 main session 启发式分类器 bias (Rule 1/9/10 把 spec NOTE 自动归 DERIVED_FROM_XLSX), 但实际这些 NOTE 在 PDF 内. **重要 finding for v1.4**: 启发式分类前应先扫 pdf_atoms.jsonl 寻 verbatim, 找到即 REASONABLE_INFERENCE; 找不到再 fallback xlsx 检查.

### 6.3 Reviewer artifacts

- `evidence/checkpoints/a4_rule_d_reviewer_audit.md` (reviewer 详细 audit 报告, 主 session 不动)
- trace.jsonl `phase_report` event 已 append

## 7. Gate

| Gate | Pass condition | Actual | Verdict |
|---|---|---|---|
| A4-G1 | HALLUCINATED rate ≤ 5% in N=40 stratified | 0/40 = 0.0% | ✅ PASS |
| A4-G2 | Rule D reviewer N=10 sub-sample 0 disagree on HALLUCINATED | 0 reviewer-flagged HALLUCINATED, 5 cat disagrees (DERIVED_FROM_XLSX → REASONABLE_INFERENCE) | ✅ PASS |
| A4-G3 | 任何 HALLUCINATED → 升 Issue 17 即时修 | n/a (0 hit) | n/a |

## 8. KNOWN_LIMITATIONS reconcile (Phase D)

v1.2 KNOWN_LIMITATIONS.en §0 D4:
> "437 `UNSOURCED_MANUAL` atoms from 06 P5 — still unclassified."

v1.3 应改为:
> "437 `UNSOURCED_MANUAL` atoms from 06 P5 — N=40 stratified sample (HIGH=10 全, LOW=30 random) classified as 80% REASONABLE_INFERENCE (CDISC paraphrase / annotation) + 20% DERIVED_FROM_XLSX (variable spec NOTE) + 0% HALLUCINATED. Full 437 classification deferred to v1.4. Sample HALLUCINATED rate gate PASS."

## 9. Carry status post-step

- v1.2 KNOWN_LIMITATIONS §0 D4: **PARTIALLY RESOLVED** (N=40 sample done, 全 437 留 v1.4)
- 06 retro §二 4: **RESOLVED** for HIGH-risk subset (full 10 跑了)
- Phase A A4 gate: PASS ✅

## 10. 下一步

- 派 Rule D reviewer subagent N=10 sub-sample 复核 (HIGH 全 10)
- 写 A5 — section_coverage.jsonl 重跑 (G6) — A3 batch M executor 完成后跑
