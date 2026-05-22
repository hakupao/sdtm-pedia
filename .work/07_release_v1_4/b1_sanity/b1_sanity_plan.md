# v1.4 Phase B.B1 — Light Sanity Plan (paper-level, deterministic)

> Date: 2026-05-20 PM (post Phase A close, 4 平台 promote 完)
> Scope: 4 平台 × 4 题 = 16 cells, paper-level (prompt fidelity + KB reach), 不依赖 UI deploy
> Goal: 验证 v9/v3 prompts 替换 v8.1/v2.x 后, KB-grounding default 命中能力不 regression (i.e. 4 v1.3-targeted sanity 题在新 prompts 下仍应 PASS)

---

## 复用 v1.3 c_sanity 4 题 (各题 target v1.3 KB 改动)

- **Q-S1**: BECAT EXTRACTION sponsor-extensible (v1.3 A2 KB 改动 in BE/spec.md)
- **Q-S2**: PP RELREC Method A/B/C/D label (v1.3 A1 KB 改动 in PP/examples.md §6.3.5.9.3)
- **Q-S3**: TR TRSTRESN/TRSTRESU 区别 (v1.3 Batch M Tier B fix in TR examples §6.3.12.2)
- **Q-S4**: DI domain (NotebookLM bucket 25 重点 + Device Identifiers, MD)

(题目原文 see `.work/07_release_v1_3/c_sanity/c_sanity_plan.md` §Q-S1..Q-S4)

---

## Paper-level Verification 双层判据

为何 paper-level: UI deploy 由用户在外部完成 (Gemini Gem / ChatGPT GPT / Claude Project / NotebookLM custom instructions), 主 session 无法直接验证. paper-level sanity 验 **v9/v3 prompts 的设计 fidelity** (KB-grounding default + KB 实际可达), 这是 UI-level 答案的必要前提. UI-level (Chrome MCP fire-and-forget) 作为可选增强, 如用户已 UI deploy 可补跑.

### Layer 1 — Prompt fidelity (平台 current/ prompt 设计验证)

对每个 (题, 平台) cell, grep 平台 current/ prompt 验证 4 个 essential rules 中相关 rules 完整:

| Rule | 触发条件 | 各题相关性 |
|---|---|---|
| **R1 KB-grounding primary** | 任何答案先 KB lookup | **all 4 题 必触** |
| **R2 Anti-hallucination triple-anchor (AHP-V1/V2/V3)** | SDTM-shaped var → KB double-check | Q-S2 PCSEQ/PPGRPID, Q-S3 TRSTRESN, Q-S4 DI vars 必触 |
| **R3 Domain scope guard (regex-gated CO-N)** | biospecimen / IS scope shift / file format | Q-S1 biospecimen 必触 |
| **R4 Response format** | cite source 标准 | all 4 题 必触 |
| **R5 Premise correction** | 用户 wrong premise 时识破 | conditional, sanity 题无 wrong premise, 不强求 |

**Pass condition (Layer 1)**: 平台 current/ prompt 含 R1 + R4, 题相关的 R2/R3 显式触发.

### Layer 2 — KB reach (KB upload 中答案可 grep)

对每个 (题, 平台) cell, grep 平台 KB upload bundle 验证答案核心事实可达:

| 题 | grep target | 验证 |
|---|---|---|
| Q-S1 | "BECAT" + "EXTRACTION" + "sponsor" + "extensible" | KB 中 4 关键词同时可达 |
| Q-S2 | "Many to Many" + "PCGRPID" + "PPSEQ" + "RELREC" | KB 中 4 关键事实可达 |
| Q-S3 | "TRSTRESN" + "TRSTRESU" + "standardized" | KB 中 3 关键变量可达 |
| Q-S4 | "Device Identifiers" + "DI" + "STUDYID" + ("Special Purpose" OR "Trial Design" OR "Study Reference") | KB 中 DI domain class 可达 |

**Pass condition (Layer 2)**: KB upload 中 ≥80% grep target 关键词命中 (各题 grep target N ≥ 3, 命中 ≥ N-1).

### Combined Verdict (per cell)

| Layer 1 (prompt) | Layer 2 (KB) | Verdict |
|:---:|:---:|:---:|
| PASS | PASS | **PASS** |
| PASS | PARTIAL | PARTIAL (KB gap, log v1.5 carry) |
| PARTIAL | PASS | PARTIAL (prompt gap, 不立即回 Phase A 若 KB-grounding 仍命中) |
| FAIL | * | FAIL |
| * | FAIL | FAIL |

---

## 决策树 (16 cells aggregate)

```
16/16 PASS → IDEAL → B1 APPROVE → 进 B2 决策点
≥14/16 PASS (含 ≤2 PARTIAL) → ACCEPTABLE → B1 APPROVE → 进 B2 决策点
<14/16 PASS OR ≥1 FAIL → NEEDS_REVISION → 归档 attempt 1 per Rule B + 回 Phase A 修对应平台
```

---

## Evidence 路径

- `.work/07_release_v1_4/b1_sanity/evidence/q_s{1,2,3,4}_<platform>.md` (16 文件)
- `.work/07_release_v1_4/b1_sanity/b1_aggregate.md` (16 cells 总览表)
- `.work/07_release_v1_4/b1_sanity/B1_SANITY_RETROSPECTIVE.md` (跑完后写)

---

## Rule A 计数

16 cells 每 cell 1 grep probe = 16 probes 累计.

---

## 启动顺序

1. Layer 2 (KB reach) 先跑 — 4 题 × 4 平台 KB grep, fast (脚本 OR 手动 grep), 不依赖平台 prompt
2. Layer 1 (Prompt fidelity) 跑 — 4 平台 current/ × 5 essential rules grep
3. 16 cells combined verdict + aggregate
4. Retrospective
