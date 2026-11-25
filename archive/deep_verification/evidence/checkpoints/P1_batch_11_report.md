# P1 Batch 11 Report — Option C parallel + Option E p.103 rerun + 4 Inline Repairs

> Date: 2026-04-25
> Strategy: Option C parallel mini-batch default (per O-P1-13) + TOC ground truth prepend (3rd consecutive run, methodology firmly locked from batch 09 #18 + batch 10 #19) + Option E p.103 rerun (writer 11a under-extracted §6.1.2 CM Example 5 + cm.xpt table) + Option H inline metadata + verbatim repairs (heading_level/sibling_index/atom_type drift + trailing empty cell scope sweep) + main-session salvage of §6.1.3 intro 2-sentence atomization
> Writers: 11a = `oh-my-claudecode:writer` × p.101-105 (138 atoms post-Option-E + Option-H); 11b = `oh-my-claudecode:executor` × p.106-110 (101 atoms clean)
> Scope: SDTMIG v3.4 p.101-110 (10 pages — §6.1.2 CM tail p.101-102 / §6.1.3 Exposure Domains intro p.103 / §6.1.3.1 Exposure (EX) p.104-106 / §6.1.3.2 Exposure as Collected (EC) p.107-110)
> Status: **✅ DONE + REPAIRED** (Rule A 95% PASS slot #20 + 0 frame tag + 0 collision + 4 Option H/E repair cycles)

---

## Metrics

| 指标 | 值 |
|---|---|
| Pages | 10 (p.101-110) |
| Atoms final | **239** (11a 138 + 11b 101) |
| Pre-root atoms | 2690 |
| Post-merge root | **2929** |
| Atom_type coverage | 8/9 single-batch (no FIGURE on dense-spec pages; CROSS_REF=0 narrative-driven) |
| Writer failures | 0 (parallel default + Option E rerun all clean) |
| DONE message vs actual (R7) | 11a writer reported 131 vs actual 122 ❌ (over-claim 9 atoms — same pattern as 09b 139→120, **O-P1-27**); 11b 101=101 ✓ |
| Frame tag contamination | 0 (R7 holding) |
| Schema errors | 0 post-repair (atom_id 4-digit/3-digit format ✓ ; atom_type 9-enum ✓) |
| Rule A verdict | **PASS @ 95%** (9 PASS + 1 PARTIAL + 0 FAIL = 9.5/10 weighted, slot #20 `pr-review-toolkit:code-simplifier`) |
| Drift cal | **NOT triggered this batch** (next at batch 12 per cadence; cumulative since last drift cal at p.89 = 416 atoms, trigger at ≥300 met → fire batch 12) |
| Option H/E repair cycles | **4** (Option E p.103 rerun 6→21+1 = 22-net atoms / Option H 11 metadata fixes / Option H 2-atom verbatim Rule A scope sweep / main-session salvage 1 missing §6.1.3 intro sentence) |
| Rule D slot 烧 | #20 `pr-review-toolkit:code-simplifier` (新烧, 20 total cumulative — Rule D §8 satisfied) |

## Execution summary

### Parallel mini-batch (Option C default) + TOC anchor prompt (3rd consecutive)

- Main session pre-dispatch: read PDF p.4 TOC for §6.1.3 ground truth (TOC p.4 covers §6.1.3 Exposure Domains p.103 / §6.1.3.1 EX p.104 / §6.1.3.2 EC p.107 / §6.1.3.3 Examples p.111+)
- Authoritative §6.1.2/§6.1.3/§6.1.3.1/§6.1.3.2/§6.1.3.3 section map prepended to BOTH 11a + 11b prompts AND Rule A reviewer prompt:
  - §6.1.2 [Concomitant/Prior Medications (CM)] (p.98-102)
  - §6.1.3 [Exposure Domains] (p.103)
  - §6.1.3.1 [Exposure (EX)] (p.104-106)
  - §6.1.3.2 [Exposure as Collected (EC)] (p.107-110)
  - §6.1.3.3 [Exposure/Exposure as Collected Examples] (p.111+, OUTSIDE batch 11b range)
- 10 cumulative R-rules force-applied (R10 NEW added 2026-04-25 batch 11 prompt, post O-P1-25 lesson)
- 11a writer × p.101-105: 2.4 min wall, 122 atoms physical (writer self-reported 131 — R7 over-claim, see O-P1-27)
  - p.101 §6.1.2 CM Assumptions tail + Example 1 narrative + cm.xpt rows 1-8: 31 atoms
  - p.102 cm.xpt rows 9-10 + Example 2/3/4 narratives + tables: 36 atoms
  - p.103 (under-extracted, 6 atoms only — Option E triggered)
  - p.104 §6.1.3.1 EX Description/Overview + Specification opening rows: 29 atoms
  - p.105 EX spec table continuation + EX – Assumptions list opening: 20 atoms
- 11b executor × p.106-110: 5.6 min wall, 101 atoms clean (R7 strict match holding)
  - p.106 EX Assumptions list 1.c.i-v + sub-items: 16 atoms
  - p.107 EX Assumptions tail (#5/#6.a-d) + §6.1.3.2 EC heading + EC Description/Overview + EC spec opening: 25 atoms
  - p.108 EC spec body (ECMOOD-ECPRESP, ECCAT-ECDOSU, ECLOT etc): 25 atoms
  - p.109 EC spec body (ECDOSFRQ-ECRFTDTC) + EC – Assumptions opening: 20 atoms
  - p.110 EC Assumptions 1-4 list: 15 atoms
- Parallel wall ~6 min vs sequential est ~10 min (40% speedup)

### Schema validation (immediate post-merge, post-repair)

- 0 atom_id 格式错 (all 4-digit 0-padded `ig34_pNNNN_aNNN`)
- 0 造词 atom_type (all ∈ 9-enum, R N1 holding)
- 0 missing heading_level/sibling_index on HEADING (post Option H fix, 11/11 HEADINGs in 11a have correct fields; 4/4 HEADINGs in 11b correct)
- 0 atom_id collision with root (2690 + 239 = 2929 total)
- 0 frame tag (`</content>` / `</response>` / `</answer>`) — R7 holding partial (verbatim discipline OK; **DONE atoms=N strict match BROKE on 11a** O-P1-27)
- HEADING tree post-Option-H repair:
  - §6.1.2 [CM] — sub-headings convention: `CM – Examples` L4 sib=4 (4th sub after Description/Overview/Specification/Assumptions); Examples 1-5 inside CM-Examples L5 sib=1-5
  - §6.1.3 [Exposure Domains] L3 sib=3 (3rd child of §6.1 after §6.1.1 sib=1, §6.1.2 sib=2)
  - §6.1.3.1 [EX] L4 sib=1 (1st child of §6.1.3); EX – Description/Overview L5 sib=1 / Specification L5 sib=2 / Assumptions L5 sib=3
  - §6.1.3.2 [EC] L4 sib=2 (2nd child of §6.1.3); EC – Description/Overview L5 sib=1 / Specification L5 sib=2 / Assumptions L5 sib=3
- parent_section dist 与 TOC ground truth 100% 一致:
  - 31× §6.1.2 [Concomitant/Prior Medications (CM)] (all p.101) ✓
  - 36× §6.1.2 [CM] (all p.102) ✓
  - 19× §6.1.2 [CM] (p.103 CM Example 5 finish + cm.xpt table)
  - 1× §6.1 [Models for Interventions Domains] (p.103 §6.1.3 heading itself, parent=§6.1)
  - 2× §6.1.3 [Exposure Domains] (p.103 intro 2 sentences post-§6.1.3 heading)
  - 29× §6.1.3.1 [Exposure (EX)] (p.104) ✓
  - 20× §6.1.3.1 [EX] (p.105) ✓
  - 16× §6.1.3.1 [EX] (p.106) ✓
  - 7× §6.1.3.1 [EX] (p.107 EX Assumptions tail) + 1× §6.1.3 [Exposure Domains] (p.107 §6.1.3.2 heading) + 17× §6.1.3.2 [EC] (p.107 EC Description/Spec opening) ✓
  - 25× §6.1.3.2 [EC] (p.108) ✓
  - 20× §6.1.3.2 [EC] (p.109) ✓
  - 15× §6.1.3.2 [EC] (p.110) ✓

### Pre-Rule-A main-session sweep (caught & repaired)

Before sample dispatch, main session PDF cross-checked 11a's HEADING/parent_section structure and uncovered:

1. **Under-extraction p.103**: 11a wrote 6 atoms for a page with cm.xpt 8-row Example 5 table + 5 Row narrative descriptions + cm.xpt 6-row data table + §6.1.3 heading + 2-sentence intro = ~21 expected. **Option E rerun** dispatched (`oh-my-claudecode:executor`) for p.103 only, returned 21 atoms; replaced 11a's 6 p.103 atoms wholesale.
2. **Heading_level convention drift (4 atoms)**: "CM – Examples" L2 sib=6 → fixed L4 sib=4; "Example 1/2/3/4" L3 → fixed L5; "EX – Description/Overview / Specification / Assumptions" L4 → fixed L5 (per batch 10 §6.1.x→L3 / sub→L4 → §6.1.3.x→L4 / sub→L5 convention delta+1).
3. **Missing sibling_index (3 atoms)**: §6.1.3 L3 sib=None → sib=3; §6.1.3.1 L4 sib=None → sib=1; §6.1.3.2 in 11b already sib=2 ✓.
4. **HEADING vs LIST_ITEM mis-classification (2 atoms)**: 11a a006 "Variables for timing relative to a time point" classified HEADING but PDF prints "4. Variables for timing..." (numbered list item under CM Assumptions list) → reclass LIST_ITEM sib=4. a013 "Although any identifier variables..." HEADING → LIST_ITEM sib=5 (item 5).
5. **Option E rerun a005 "Example 5" SENTENCE → HEADING L5 sib=5 fix**: rerun executor mis-classified Example 5 as SENTENCE; re-aligned to HEADING per Examples 1-4 convention.
6. **Salvage missing §6.1.3 intro 2nd sentence**: rerun a021 packed both sentences into 1 atom (length 636) violating IR2 / v1.1 M2 (1 sentence = 1 atom). Trimmed a021 to first sentence ("Clinical trial study designs can range...") + main-session-composed a022 from PDF ground truth ("To support standardization of various collection methods...") — both verified verbatim against PDF p.103.

Net impact of pre-Rule-A sweep: 122 → 138 atoms (+16 = +21 rerun -6 11a-replaced +1 salvage) and metadata clean across 11 atoms.

## Rule A gate (slot #20 `pr-review-toolkit:code-simplifier`)

**Sample**: 10 atoms with **10/10 page coverage** (1/page across p.101-110, O-P1-14 lesson holding). Seed=20260460. Atom_type coverage 5/9 exercised (LIST_ITEM×3 / TABLE_ROW×3 / HEADING×2 / CODE_LITERAL×1 / TABLE_HEADER×1) — under-cover SENTENCE/NOTE/CROSS_REF/FIGURE due to atom availability per page (p.109/p.110 had no SENTENCE atoms in stratum, fallback to LIST_ITEM).

**Raw verdict: 9 PASS + 1 PARTIAL + 0 FAIL = 95% weighted (9.5/10) PASS @ ≥90% threshold MET ✓**

### Findings

**F-B11-RA-1 PARTIAL (p.102 a022 ZOLOFT Example 3 cm.xpt Row 1 trailing empty cell missing)**: PDF Example 3 cm.xpt has 10 columns (Row | STUDYID | DOMAIN | USUBJID | CMSEQ | CMTRT | CMPRESP | CMOCCUR | CMSTAT | CMREASND). Row 1 ZOLOFT has 8 populated values + 2 trailing empty cells (CMSTAT=empty + CMREASND=empty). Atom verbatim rendered 8 values + 1 empty cell representation `| |` instead of 2 `| | |`. R8 break.
- **Inline fix applied** + **scope sweep main-session uncovered 1 additional atom same pattern**: a023 PROZAC Row 2 also has 2 trailing empty cells but atom rendered only 1.
- **Scope expansion: 1 Rule A flag → 2 atoms fixed inline** (a022 ZOLOFT + a023 PROZAC) → severity LOW (O-P1-31).
- Row 3 PAXIL (a024) excluded — has CMSTAT="NOT DONE" populated + CMREASND="Didn't ask due to interruption" populated (4 cells active).

### Codelist literal spot-check — **0 drift** ✓

Reviewer noted spot-check on p.104 EX spec CT codelist literals: EXDOSU=`(UNIT)`, EXDOSFRM=`(FRM)`, EXDOSFRQ=`(FREQ)`, EXROUTE=`(ROUTE)`, EXLOC=`(LOC)`, EXLAT=`(LAT)`, EXDIR=`(DIR)`, EXFAST=`(NY)`, EPOCH=`(EPOCH)` — all preserved verbatim including parentheses. R6 holding (no `(CNTMODE)`/`C\(NCI\)GCD` class hallucination, no CT-lookup paraphrase).

### Empty-cell / data-row check — **partial drift caught**

- Atom 8 (p.108 ECLOT row): empty CT cell `| |` correctly rendered ✓ R8 hold for 11b
- Atom 2 (p.102 ZOLOFT row): trailing CMREASND empty cell missed → R8 break for 11a (F-B11-RA-1, scope swept to 2 atoms inline 修)

### CODE_LITERAL R9 check — **0 mis-classification** ✓

Atom 3 (p.103 cm.xpt CODE_LITERAL): parent_section §6.1.2 [CM] correct (cm.xpt physically appears inside CM Example 5 narrative on p.103, parent attribution by physical-page-section rule). R9 holding (cross-domain reference physical-page rule continues to discipline correctly).

### Ground-truth anchor check — **0 inversion bug** ✓

All 10 sample atoms' parent_section matched TOC ground truth:
- p.101-103 atoms (CM tail) → `§6.1.2 [Concomitant/Prior Medications (CM)]` ✓
- p.103 cross-section atoms: cm.xpt (CODE_LITERAL) → `§6.1.2 [CM]` ✓ ; §6.1.3 heading (HEADING) → `§6.1 [Models for Interventions Domains]` ✓ (heading-self-reference rule); intro (SENTENCE) → `§6.1.3 [Exposure Domains]` ✓
- p.104-106 atoms → `§6.1.3.1 [Exposure (EX)]` ✓
- p.107 atoms: EX Assumptions tail → `§6.1.3.1 [EX]` ✓ ; §6.1.3.2 heading → `§6.1.3 [Exposure Domains]` ✓ (heading-self-reference); EC body → `§6.1.3.2 [EC]` ✓
- p.108-110 atoms → `§6.1.3.2 [EC]` ✓

Reviewer's own rationale 0 inverted (TOC anchor methodology held for **third consecutive batch** — slot #18 pr-test-analyzer + slot #19 type-design-analyzer + slot #20 code-simplifier all deliver 0 FP / 0 inversion across cumulative 30-atom independent sample). **Methodology firmly locked at 3 batch n=30.**

## Drift calibration — NOT triggered this batch

Per cadence (every 3 batches / ~300 atoms). Last drift cal at batch 09 (post 07-09 cumulative 675 atoms, Δ since=416 atoms 11+10+09 partial). **Next trigger BATCH 12** (post 10-12 cumulative ~600 atoms, mandatory). Candidate target page: p.115-118 EX/EC Examples spec table dense rows (drift cal value-add highest on TABLE_ROW where Rule A blind spot remains, per O-P1-23 lesson).

## Option H/E repairs applied (4 cycles)

| # | Type | Scope | Fix |
|---|---|---|---|
| 1 | Option E | Full p.103 rerun (6 → 21 atoms, +15 net) | `oh-my-claudecode:executor` rerun `pdf_atoms_batch_11_p103_rerun.jsonl`; replaced 11a a001-a006 with rerun a001-a021. Reason: 11a writer under-extracted Example 5 narrative + cm.xpt table (R7 over-claim 131→122 traces here). |
| 2 | Option H | 11 atoms metadata fix | heading_level/sibling_index/atom_type drift across p.101 (HEADING→LIST_ITEM 2 atoms; CM-Examples L2→L4; Example 1 L3→L5), p.102 (Examples 2-4 L3→L5), p.104 (§6.1.3.1 sib=None→1; EX-Desc/Spec L4→L5), p.105 (EX-Assumptions L4→L5). |
| 3 | Main-session salvage | 1 atom (p.103 a022 SENTENCE) | rerun a021 packed both §6.1.3 intro sentences into single SENTENCE (length 636) violating IR2 / v1.1 M2. Trimmed a021 verbatim to first sentence; main-session-composed a022 from PDF ground truth (verified character-for-character vs PDF p.103). Original 11a a006 had verbatim drift ("are available based on... and are available to" vs PDF "based on... are available to") — discarded, used PDF directly. |
| 4 | Option H (post Rule A) | 2 atoms (a022 + a023 PROZAC scope sweep) | F-B11-RA-1 LOW: appended trailing pipe ` |` to both atoms for missing CMREASND empty cell (PDF Example 3 cm.xpt Row 1 + Row 2 each have 2 trailing empty cells, atoms had 1). Row 3 PAXIL excluded (CMSTAT/CMREASND populated). |

## Findings added

| ID | Severity | Summary |
|---|---|---|
| O-P1-27 | LOW | 11a writer (`oh-my-claudecode:writer`) reported `DONE atoms=131` but actual file had 122 lines (R7 strict-match break, -9 atoms over-claim). Same writer-family pattern as 09b 139→120 (writer family), batch 10 10b 92=92 ✓ holding (executor pattern). Recommend v1.3 prompt: "writer must `wc -l` output file before reporting DONE; if mismatch with internal counter, recompute from file". Not blocking (file ground truth = 122; rerun + sweep brought final to 138). |
| O-P1-28 | MEDIUM | 11a writer p.103 under-extraction (6 atoms vs PDF expected ~21). Pattern: writer captured §6.1.3 heading + 2 SENTENCEs at top of page but DROPPED Example 5 narrative + 5 list items + cm.xpt CODE_LITERAL + TABLE_HEADER + 6 TABLE_ROWs. **Option E executor rerun** restored 15 missing atoms. Possible root cause: writer mis-prioritized "TOC transition page" (§6.1.2 → §6.1.3) and skipped CM tail content. Recommend v1.3 prompt: "transition pages (page contains 2+ section starts) must atomize ALL physical content on page including the *previous* section tail before processing the next section". |
| O-P1-29 | LOW | 11a writer heading_level convention drift across 4 sub-headings: "CM – Examples" L2 (should be L4); "Example 1-4" L3 (should be L5); "EX – Description/Overview / Specification / Assumptions" L4 (should be L5). Convention from batch 10: §6.1.x = L3 / sub-heading = L4. For deeper §6.1.3.1 = L4 / sub = L5 (delta +1). Inline fixed 11 atoms. Recommend v1.3 prompt: tabulate convention "section_level = depth_of_section_number_dots + 1; sub-heading_level = section_level + 1". |
| O-P1-30 | LOW | 11a writer mis-classified 2 numbered list items "4. Variables for timing relative to a time point" + "5. Although any identifier variables..." as HEADING (per their bold formatting / standalone-line layout), but PDF clearly numbers them as list items 4 and 5 of CM Assumptions list. Inline reclass LIST_ITEM. Recommend v1.3 prompt: "if PDF prints `<number>. <text>` with `<number>` matching the surrounding numbered list, classify as LIST_ITEM regardless of bold/italic styling". |
| O-P1-31 | LOW | 11a writer 2 atoms p.102 a022 ZOLOFT + a023 PROZAC missed trailing CMREASND empty cell (rendered 1 `\| \|` instead of 2 `\| \| \|`). Caught by Rule A reviewer slot #20 + main-session scope sweep. Inline fixed. Pattern: writer collapsed multi-empty trailing cells into single empty representation. Recommend v1.3 prompt: "TABLE_ROW verbatim must have exactly N-1 internal pipes for N PDF columns; trailing empty cells each get their own `\| \|` representation, no collapsing". |
| O-P1-26 (reaffirmed) | INFO | TABLE_ROW pipe-format inconsistency persists: rerun executor (p.103 TABLE_HEADER/TABLE_ROW) uses outer-pipe `\| Row \| ... \|`; original 11a writer (p.101/p.102 TABLE_ROWs) uses no-leading-pipe `Row \| STUDYID \| ...`; 11b executor (p.108/p.109) uses no-leading-pipe. Even within batch 11 mixed. Defer v1.3 prompt: "all TABLE_ROW + TABLE_HEADER verbatim use outer-pipe style `\| field1 \| field2 \| ... \|`". |

## Rule D roster (post batch 11)

- Cumulative: **20 distinct subagent types** burned
- New: pr-review-toolkit:code-simplifier (slot #20) — **0 false positive / 0 inverted rationale** on 10-atom sample (TOC-anchored methodology continued from slots #18 + #19; n=30 cumulative anchored audit 0 FP / 0 inverted, methodology firmly locked at 3 consecutive batches). Reviewer output quality: per-atom 4-dimension verdict (atom_type/verbatim/parent_section/heading_fields) + R6/R7/R8/R9/R10 rule discipline check + 7 spot-check observations outside sample useful for v1.3 candidate fixes (footnote ¹ as separate NOTE atom check / smart-quote risk in "Didn't" / Row 5 vs Row 6 CMENRTPT consistency / etc).
- Quality trend (TOC-anchored era): slot #18 pr-test-analyzer 90% pooled / slot #19 type-design-analyzer 95% / slot #20 code-simplifier 95%. **Methodology stable, reviewer family quality cluster around 90-95% post TOC anchor adoption**.
- Rule D pool remaining (with Write tool): vercel/plugin-dev/data/firecrawl/superpowers/oh-my-claudecode (subset) — pool sufficient for 30+ more batches at current rotation rate.

## Post-batch state

| 项 | Value |
|---|---|
| P1 pages_done | **110** / 535 (20.6%) |
| P1 atoms_done | **2929** root (pre 2690 + 239 = 2929 clean post-repair) |
| P1 batches_done | **11** |
| P1 failures_done | 1 (batch 06 attempt 1, Rule B archived) |
| Rule A cumulative | 8 batches × 10-atom + 1 × 30-atom = 110-atom independently PDF-verified sample; 1 batch 04 PARTIAL + 1 batch 06 FAIL + 1 batch 07 raw FAIL + 1 batch 08 raw FAIL + 1 batch 09 CONDITIONAL_PASS + 1 batch 10 PASS 95% + **1 batch 11 PASS 95%** |
| Drift cal cumulative | 3 runs (p.25 3-way FAIL O-P1-09 / p.60 2-way FAIL O-P1-12 writer bug / p.89 2-way FAIL O-P1-23 hallucination); next trigger **batch 12 mandatory** (cumulative since p.89 = 416 atoms ≥300 cadence) |
| Option H/E repair cycles | **9 cumulative** (batch 06 Option E + batch 07 + batch 08 bulk + batch 09 2× + batch 10 1× + **batch 11 4× = E + 2×H pre-RA + 1×H post-RA + 1×salvage**) |

## Session budget (batch 11 total)

- Session startup (5 prereq reads parallel): 4 min
- TOC read p.4 + extract §6.1.3 ground truth: 1 min
- 11a + 11b parallel dispatch + wait: 5.6 min wall (parallel, longer of two)
- Schema + collision check + parent_section vs TOC anchor verify: 2 min
- Pre-Rule-A main-session sweep (PDF p.101 + p.103 + p.107 read + 11a metadata diagnosis): 4 min
- Option E p.103 rerun dispatch (background) + wait: 1.3 min wall (run in parallel with metadata fix prep)
- Option H 11-atom metadata fix script: 1 min
- Main-session salvage 2 atoms (a021 trim + a022 insert + verbatim verify): 2 min
- Rule A sample build (seed 20260460, 1/page stratified) + dispatch (slot #20): 3.1 min wall
- Reviewer finding verify + Option H scope sweep 2 atoms inline: 2 min
- Paperwork (batch 11 report + audit_matrix + _progress.json + recovery_hint): 6 min
- **Total ~32 min** (heavier-than-usual batch — under-extraction + Option E rerun + 4 repair cycles + slot #20 dispatch + main-session salvage; vs batch 10's 21 min fast-path)

---

*Handoff: Next session reads `_progress.json.recovery_hint` + this report + `rule_a_batch_11_summary.md` + new findings O-P1-27/28/29/30/31/26-reaffirmed. Batch 12 dispatch SHOULD include: (a) **continue TOC anchor prompt** (validated 3rd consecutive 0-inversion); (b) force-apply O-P1-15/16/18/19/20/21/22/23/24/25/27/28/29/30/31 = **15 累 R-rules** (R10 already in batch 11; R11 NEW = "TABLE_ROW verbatim must preserve N PDF columns including each trailing empty cell as separate `\| \|` representation, no collapsing"; R12 NEW = "transition pages with 2+ section starts must atomize ALL physical content including previous section tail content"; R13 NEW = "atom_type LIST_ITEM if PDF prints `<num>. <text>` matching surrounding numbered list, regardless of bold/italic styling"); (c) Rule A reviewer slot #21 候选: pool with Write tool — `vercel:performance-optimizer` / `vercel:deployment-expert` / `vercel:ai-architect` / `oh-my-claudecode:designer` / `oh-my-claudecode:debugger` / `oh-my-claudecode:executor`-reuse (ban — already burned slot #8) / `pr-review-toolkit:code-reviewer` reuse (already burned slot #10) — recommend `oh-my-claudecode:debugger` (sonnet, action-oriented, Write tool, unburned); (d) batch 12 spans p.111-120 — covers §6.1.3.3 [Exposure/Exposure as Collected Examples] (p.111-120 likely full); TOC anchor extends to §6.1.3.3 / next sub-section §6.1.4 [Meal Data (ML)] starting p.121; (e) **drift cal MANDATORY trigger at batch 12** post-merge (cumulative 416+atoms since last cal at p.89; candidate target: p.115-118 EC/EX Examples spec table dense TABLE_ROWs for highest drift-cal value-add per O-P1-23 lesson).*
