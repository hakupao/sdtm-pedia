# 06 Deep Verification — Audit Matrix

> 创建: 2026-04-24
> 用途: 每 phase Rule A 抽检 + per-batch writer/reviewer roster + drift 校准结果落档
> 同步: PLAN v0.5 §7 Rule E + §9 Gate + Tier 3 workflow

---

## P0 Pilot (已完成)

| Target | PDF 页 | MD 文件 | PDF atoms | MD atoms | Writer type | Matcher type | Reviewer type (slot) | Accuracy |
|---|---|---|---|---|---|---|---|---|
| T1 v1 | sv20 p.50 | model/04 | 17 | 25 | Explore (#3) | feature-dev:code-explorer (#5) | oh-my-claudecode:code-reviewer (#7) | 70% FAIL |
| T1 v1.1 | sv20 p.50 | model/04 | 21 | 21 | oh-my-claudecode:executor (#8) | oh-my-claudecode:executor (#8 reuse) | pr-review-toolkit:code-reviewer (#10) | **85% PASS** |
| T2 | ig34 p.428 | chapters/ch08 | 30 | 42 | oh-my-claudecode:executor (#8) | oh-my-claudecode:executor (#8) | feature-dev:code-reviewer (#11) | **81.25% PASS** |
| T3 | ig34 p.137 | domains/AE/assumptions | 32 | 55 | oh-my-claudecode:executor (#8) | oh-my-claudecode:executor (#8) | feature-dev:code-reviewer (#11) | **81.25% PASS** |
| T2b FIGURE | ig34 p.440 | chapters/ch08 §8.8 | 16 | 15 | main-session-sanity-check | main-session-sanity-check | (deferred optional) | self-validated 6/6 v1.2 fix PASS |

**P0 final: ✅ PASS, 9/9 atom_type, Rule D 11 slot 烧**.

---

## P1 PDF Atomization (in progress)

### P1 Batch Roster (writer/reviewer 轮换)

| Batch | Page range | Writer type | Reviewer type (Rule A 抽检) | Atoms | Failures | Status | Notes |
|---|---|---|---|---|---|---|---|
| 01 | ig34 p.1-10 | oh-my-claudecode:executor | pending (30-page milestone) | **326** | 0 | ✅ done 2026-04-24 | TOC heavy (p.2-5 = 210 CROSS_REF, 65%), p.6 稀疏 2 atom, 正文 p.7-10 合理; atom_id 3→4 digit autofix 全 326; atom_type dist CROSS_REF 212 / LIST_ITEM 62 / SENTENCE 30 / HEADING 13 / TABLE_ROW 8 / TABLE_HEADER 1; 0 schema error post-fix |

### P1 Drift 校准 (每 300 atom = 每 3 batch)

| 校准点 | Atom range | Writer A | Writer B | Writer C | 一致率 | 门槛 (≥80%) | 动作 |
|---|---|---|---|---|---|---|---|
| (pending after batch 3) | | | | | | | |

### P1 Rule A 30-page 独审

| 检查点 | Page range | Reviewer type (slot) | Sampled atoms | 一致率 | 门槛 (≥90%) | Verdict |
|---|---|---|---|---|---|---|
| (pending after batch 3, ~p.1-30) | | | | | | |

---

## Rule D Roster 累计

**烧过 (11/16)**: critic (#1) + verifier (#2) + Explore (#3) + omc:explore (#4) + fd:code-explorer (#5) + omc:document-specialist (#6) + omc:code-reviewer (#7) + omc:executor (#8) + omc:writer (#9) + pr:code-reviewer (#10) + fd:code-reviewer (#11).

**池余 (5 + 2)**: superpowers:code-reviewer / omc:scientist / omc:tracer / omc:architect / omc:ai-slop-cleaner / omc:planner / Plan.

---

*Appended per batch + per drift calibration + per Rule A sampling. 不删行, 保留全历史.*
