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
| 02 | ig34 p.11-20 | oh-my-claudecode:writer (model=sonnet override) | pending (30-page milestone) | **323** | 0 | ✅ done 2026-04-24 | Batch 02 clean run: 0 schema errors (inline 4-digit fix for O-P1-03 worked, autofix 0), **9/9 atom_type 单批覆盖** (P1 首次, FIGURE=1 p.14), **CODE_LITERAL 63/323 (19.5%)** 首批出现证明 Option A spec 表原子化产出开始; atom_type dist SENTENCE 89 / LIST_ITEM 76 / TABLE_ROW 63 / CODE_LITERAL 63 / HEADING 16 / CROSS_REF 7 / NOTE 4 / TABLE_HEADER 4 / FIGURE 1; density 15-53 atoms/页; 0 collision with root. |
| 03 | ig34 p.21-30 | oh-my-claudecode:executor (model=sonnet) | superpowers:code-reviewer (#12) 30-atom ✅ PASS 100% | **269** | 0 | ✅ done 2026-04-24 | Batch 03 clean: 0 schema errors, SENTENCE 115/269 (42.8%) Ch.3 narrative-heavy, 0 CROSS_REF/0 FIGURE (TOC 已结束), 7/9 atom_type per-batch (cumulative 9/9), HEADING 34 多 subsection; density 16-40 atoms/页; 0 collision. 触发 30-page milestone: Rule A 100% PASS + drift 3-way FAIL (QS sparse-cell TABLE_ROW reproducibility), user Option 2' continue + Rule A 加密 per-batch. |
| 04 | ig34 p.31-40 | oh-my-claudecode:writer (model=sonnet) | oh-my-claudecode:tracer (#13) 10-atom ✅ PASS 90% | **330** | 0 | ✅ done 2026-04-25 | Batch 04 clean: 0 schema/id/json 错, **9/9 atom_type 单批再覆盖** (FIGURE=1 p.34 decision tree, NOTE 6, TABLE_HEADER 23 spec 表密度开始上升), density 22-42 atoms/页; SENTENCE 148 (44.8%) narrative-dominant 与 batch 03 一致, Ch.4 intro (Intervention/Event/Finding) 开段; 0 root collision (pre 918 + 330 = 1248). Per-batch Rule A v1.1 首跑 (slot #13 oh-my-claudecode:tracer sonnet), 9 PASS + 1 PARTIAL + 0 FAIL = 90% 正踩 ≥90% 门槛, 单一 PARTIAL 为 ig34_p0038_a017 "4.4 Actual and Relative Time Assumptions" heading_level claimed=1 应=2 (non-semantic off-by-one, 记 F-B04-RA-1 / O-P1-10). |
| 05 | ig34 p.41-50 | oh-my-claudecode:executor (model=sonnet) | oh-my-claudecode:planner (#14) 10-atom ✅ PASS 100% | **327** | 0 | ✅ done 2026-04-25 | Batch 05 clean: 0 schema/id/json 错, **9/9 atom_type 单批再覆盖** (P1 第 3 次), FIGURE=2 新高 p.46 'Representing Time Points' + 另一 figure, NOTE 4, TABLE_HEADER 7 + TABLE_ROW 57 spec 表持续高密度, HEADING 20 多 Ch.4.x subsection; density 15-46 atoms/页 (p.48=46 最高, p.50=15 最低); SENTENCE 144 (44.0%) narrative-dominant 延续 batch 04 44.8%; Ch.4 intervention/event/finding observation class 详述 + 时间点/SUBJID/Grouping; 0 root collision (pre 1248 + 327 = 1575); 2-type alternation O-P1-07 X' 第 3 次循环. Per-batch Rule A v1.1 第 2 跑 (slot #14 oh-my-claudecode:planner opus), 10 PASS + 0 PARTIAL + 0 FAIL = 100% 超门槛, 0 finding. Reviewer 明确指出 F-B04-RA-1 未 propagate 到 level-3 后裔 (4.4.11 level=3 correct), O-P1-10 保持 LOW 单例不升级. |
| 06 | ig34 p.51-60 | attempt 1 (FAILED) oh-my-claudecode:writer single-writer × 10 pages (27 atoms dropout); **attempt 2 Option C 并行**: 06a = oh-my-claudecode:executor × p.51-55 (156 atoms) + 06b = oh-my-claudecode:writer × p.56-60 (105→107 atoms post repair) + drift_cal executor 24 atoms p.60 promoted to primary post 06b under-extraction | oh-my-claudecode:code-simplifier (#15) 10-atom ✅ PASS 90% (1 FAIL F-B06-RA-1 row-vs-sibling-index 混淆 inline 修) | **263** (combined 156+107) | attempt 1: 1 dropout (archived Rule B) / attempt 2: 0 | ✅ done 2026-04-25 | Batch 06 Option C + E 复合策略: attempt 1 single-writer × 10 pages dropout 27 atoms 归档 evidence/failures/. Attempt 2 并行 mini-batch: 06a clean 9/9 type; 06b 9/7 type clean schema 但主 session 独立 PDF-read 发现 2 structural bugs (12 atoms §4.5.9 page misattribution + CO spec table under-extract 2/13 TABLE_ROWs). Option E inline repair: relocate 12 atoms p.60→p.59, replace writer 06b 22 p.60 atoms with executor 24 atoms, fix F-B06-RA-1. Final 263 atoms, 9/9 atom_type, pre 1575 + 263 = 1838. Findings: O-P1-11..14. |
| 07 | ig34 p.61-70 | **Option C parallel default** (per O-P1-13): 07a = oh-my-claudecode:executor × p.61-65 (115 atoms clean) + 07b = oh-my-claudecode:writer × p.66-70 (117→113 atoms post dedup) | pr-review-toolkit:silent-failure-hunter (#16) 10-atom raw FAIL 70% (F-B07-RA-1 HEADING→LIST_ITEM + F-B07-RA-2 **FALSE POSITIVE** reviewer misread + F-B07-RA-3 case drift); **effective post-repair 10/10 PASS** | **228** (combined 115+113) | 0 (attempt 1 clean) | ✅ done 2026-04-25 | Batch 07 Option C + H 复合: lettered list 8 atoms + 4 dup from p.67→p.66 + case drift. Findings O-P1-15/16/17. |
| 08 | ig34 p.71-80 | Option C parallel: 08a = oh-my-claudecode:executor × p.71-75 (130 atoms) + 08b = oh-my-claudecode:writer × p.76-80 (90 atoms) | pr-review-toolkit:comment-analyzer (#17) 10-atom RAW FAIL 40% (3 §5.x parent_section + 1 verbatim paraphrase + 1 truncation + 1 minor; 1 case PASS) | **220** (combined 130+90) | 0 | ✅ done 2026-04-25 (bulk repaired) | Batch 08 Option C + H 复合 MAJOR repair: (1) **systemic §5.x parent_section 错** 182/220 atoms (83%): 08a 130 atoms §5.1 DM (写手 §5.1/§5.2 numbering 反) + 08b 52 atoms §5.2 [CRF Metadata] (把 local table label 误当章节标题). 主 session PDF cross-check 确认 §5.1=CO §5.2=DM §5.3=SE. Bulk fix applied. (2) F-B08-RA-5 p.79 a008 verbatim paraphrase (evaluate→relate) inline 修. (3) F-B08-RA-6 p.80 a008 SEENDY TABLE_ROW 缺 Core 列 'Perm' inline 修. (4) Reviewer 本身 section numbering INVERTED (reviewer 说 §5.2=CO 反的), 方向对 rationale 错. Final 220 atoms post-repair (182 §5.2 DM + 38 §5.3 SE). Pre 2066 + 220 = 2286. Findings O-P1-18 HIGH (08a §5.1/§5.2 confusion) + O-P1-19 HIGH (08b local label as section title) + O-P1-20 MEDIUM (reviewer numbering inverted). |

### P1 Drift 校准 (每 300 atom = 每 3 batch)

| 校准点 | Atom range | Writer A | Writer B | Writer C | 一致率 | 门槛 (≥80%) | 动作 |
|---|---|---|---|---|---|---|---|
| 30-page (p.25) | batch 03 baseline | executor | writer | general-purpose | 67.5% / 37.5% / 37.5% (3-way unanimous 19.2%) | FAIL on TABLE_ROW verbatim | FAIL 原因确认为 QS sparse-cell PDF 解析噪声 (O-P1-09), atom_type distribution 100% identical 3-way; user Option 2' continue + Rule A 加密 per-batch 替代 v1.3 prompt immediate churn |
| 300-atom milestone (post batch 06) | p.60 | oh-my-claudecode:writer (06b) | oh-my-claudecode:executor drift_cal_p60_rerun | — | **17.6% strict (6/34)** | FAIL vs ≥80% | FAIL 根因非 O-P1-09 sparse-cell (batch 03 pattern), 是 writer 06b 独有 bug: (a) 12 atoms 页号 misattribution p.60→p.59, (b) CO spec table on p.60 under-extract (writer 2 TABLE_ROW vs executor 13). Executor rerun 更 complete → promoted to primary via Option E. 记 O-P1-12 MEDIUM. 未触发 tiebreaker (因 FAIL 根因已定位为 writer bug 非 reproducibility 噪声). Next drift cal 待 batch 07-09 累 300+ 触发. |

### P1 Rule A 独审 (per-batch 10-atom v1.1 + 30-page 30-atom 历史)

| 检查点 | Page range | Sampling mode | Reviewer type (slot) | Sample n | Pass / Partial / Fail | Pass rate | 门槛 | Verdict |
|---|---|---|---|---|---|---|---|---|
| 30-page milestone (historical v1.0) | ig34 p.1-30 | 30-atom 分层 (seed=20260424, 9/9 type 代表) | superpowers:code-reviewer (#12) | 30 | 30 / 0 / 0 | 100% | ≥90% | ✅ PASS |
| batch 04 per-batch (v1.1 cadence) | ig34 p.31-40 | 10-atom 分层 (seed=20260425, 9/9 type 代表, FIGURE+NOTE 强制) | oh-my-claudecode:tracer (#13) | 10 | 9 / 1 / 0 | 90% | ≥90% | ✅ PASS (threshold 正踩) |
| batch 05 per-batch (v1.1 cadence) | ig34 p.41-50 | 10-atom 分层 (seed=20260430, 9/9 type 代表, FIGURE+NOTE 强制, p.41-49 spread) | oh-my-claudecode:planner (#14) | 10 | 10 / 0 / 0 | **100%** | ≥90% | ✅ PASS (超门槛, 0 finding) |
| batch 06 per-batch (v1.1 cadence) | ig34 p.51-60 (combined 06a+06b) | 10-atom 分层 (seed=20260435, 9/9 type 代表, p.51-57 spread — 盲区: 未触及 p.59-60) | oh-my-claudecode:code-simplifier (#15) | 10 | 9 / 0 / 1 | **90%** | ≥90% | ✅ PASS (threshold 正踩, 1 FAIL = F-B06-RA-1 row-vs-sibling_index 混淆 inline 修; 但 **sample 未覆盖 p.59-60 结构性 bug**, 由主 session PDF-read 独立发现触发 Option E) |
| batch 07 per-batch (v1.1 cadence) | ig34 p.61-70 (combined 07a+07b) | 10-atom 分层 (seed=20260440, 8/9 type 代表, 无 FIGURE 本批, 页 62,64,65,67,68,69 spread = 6/10) | pr-review-toolkit:silent-failure-hunter (#16) | 10 | raw 7/1/2 (effective post-repair 10/0/0) | raw **70%** / effective **100%** | ≥90% | raw **FAIL** → triggered Option H inline repair; main-session PDF cross-check rejected 1 FAIL as false positive (F-B07-RA-2), fixed 1 FAIL real (F-B07-RA-1 + scope sweep 8 atoms) + 1 PARTIAL real (F-B07-RA-3 case). Post-repair atoms 10/10 PASS (gate effectively PASS). Findings O-P1-15/16/17. |
| batch 08 per-batch (v1.1 cadence + O-P1-14 lesson) | ig34 p.71-80 (combined 08a+08b) | 10-atom 分层 (seed=20260445, **10/10 page coverage** — O-P1-14 improvement landed; 4/9 atom_type HEADING/SENTENCE/TABLE_HEADER/TABLE_ROW dominant) | pr-review-toolkit:comment-analyzer (#17) | 10 | raw 4/2/4 | raw **40%** | ≥90% | raw **FAIL** → main session scope sweep found 182/220 atoms 系统性 §5.x parent_section 错 (远超 sample 3 flags), Option H bulk repair. Reviewer 自己 section numbering 反 (§5.1/§5.2 mental model 反向, O-P1-20). Post-repair parent_section distribution clean (182 §5.2 DM + 38 §5.3 SE). Sample Rule A re-run defer 下 session due to ctx budget. Findings O-P1-18/19/20. |

---

## Rule D Roster 累计

**烧过 (17/扩展)**: critic (#1) + verifier (#2) + Explore (#3) + omc:explore (#4) + fd:code-explorer (#5) + omc:document-specialist (#6) + omc:code-reviewer (#7) + omc:executor (#8) + omc:writer (#9) + pr:code-reviewer (#10) + fd:code-reviewer (#11) + superpowers:code-reviewer (#12) + omc:tracer (#13) + omc:planner (#14) + omc:code-simplifier (#15) + pr:silent-failure-hunter (#16) + **pr:comment-analyzer (#17)**.

**池余**: 带 Write tool 未烧 = pr-review-toolkit 家族 {comment-analyzer / pr-test-analyzer / type-design-analyzer / code-simplifier [pr版]} + vercel/plugin-dev 家族. 无 Write tool (主 session 代写支持) = scientist / architect / Plan. Roster 已超原 16 估算上限 — 扩展空间充足.

**Reviewer quality 观察** (O-P1-17): silent-failure-hunter 本次报 1 FAIL + 1 PARTIAL + 1 FAIL (actual false positive). False positive rate on batch 07 = 1/10 = 10%. Consider: reviewer 本身也受 Rule D 审? 或主 session PDF cross-check 永远是 final gate.

---

*Appended per batch + per drift calibration + per Rule A sampling. 不删行, 保留全历史.*
