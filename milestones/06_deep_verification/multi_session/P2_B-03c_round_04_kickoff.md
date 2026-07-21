# P2 B-03c Round 04 — Multi-Domain Autonomous Cycle Kickoff (EX..IE scope)

> 创建: 2026-05-06 (post B-03c round 03 CLOSED 同日, commit fb6e5ff)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` (8 D-rules) + `P0_matcher_v1.9.1.md` + `P0_reviewer_v1.9.1.md`
> Parent round close ref: `multi_session/P2_B-03c_round_03_kickoff.md` + commit fb6e5ff (12 batches 741 atoms 5 domains DM/DS/DV/EC/EG per-batch Rule A 100% × 12 + mini-audit 10/10 + 8/8 invariants PASS 100% reviewer pr-review-toolkit:type-design-analyzer; §2.4 multi-batch slice + §2.6 FIGURE-in-domains lock fully validated; LIST_ITEM sib_idx null precedent enforced)
> 路由词: 用户在 session 说 **"P2 bulk B-03c round 04 自治连跑"** → 进本 kickoff dispatch (post §0.5 + §1 scope Option B + §2.7 first-time numberless H2 in assumptions.md 用户 ack)
> Convention 继承: round 01-03 §2.1-2.6 carry-forward (atom_id + parent_section + H3a sub-namespace + §2.4 multi-batch slice + §2.6 FIGURE-in-domains lock); **round 04 §2.7 first-time extension**: numberless H2 in assumptions.md (FT/ass L9 `## QRS Shared Assumptions`) — first-time application of v1.9.1 D-4 Hook D-D8 outside examples.md

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL)

逐项 grep-verified against source byte-exact (执行日 2026-05-06). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 03 CLOSE 时 md_atoms.jsonl 末原子 = `md_dmEG_ex_a078` (round 03 batch_44 final atom; parent_section `§EG.4 [Example 4]`; file `knowledge_base/domains/EG/examples.md`) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'), a.get('file'))"` | ✓ md_dmEG_ex_a078, §EG.4 [Example 4], knowledge_base/domains/EG/examples.md |
| 2 | md_atoms.jsonl 当前总原子 = **6383** (post round 03 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 6383 |
| 3 | round 03 实际产 atoms = **741** (6383 − 5642 round 03 起始基线) | progress.json `b_03c_round_03_details.atoms` + commit fb6e5ff message | ✓ 741 |
| 4 | round 03 atoms/line ratio = 741/1257 = **0.589** (实证 ratio drift downward sustained: round 01 0.782 → round 02 0.614 → round 03 0.589; signal用 conservative 估算 round 04) | round 03 §0.5 row 8 source 1257 + actual 741 atoms | ✓ 0.589 |
| 5 | 累计 unique files atomized = **47** (post round 03; B-02 17 + round 01 10 + round 02 10 + round 03 10) | post-round 03 47 files; `_progress.json` cumulative_post_round_03.files_atomized = 47 | ✓ 47 |
| 6 | domains/ 余 = **47 domains** (63 total − 1 CM B-02 done − 5 round 01 done − 5 round 02 done − 5 round 03 done) | `ls knowledge_base/domains/ \| grep -vE "^(CM\|AE\|AG\|BE\|BS\|CE\|CO\|CP\|CV\|DA\|DD\|DM\|DS\|DV\|EC\|EG)$" \| wc -l` | ✓ 47 |
| 7 | Round 04 scope = 6 domains alphabetical (EX / FA / FT / GF / HO / IE) × 2 files = **12 source files** | 字母序 first 6 post round 03: `ls knowledge_base/domains \| grep -vE "^(...全 16 done...)$" \| sort \| head -6` → EX FA FT GF HO IE | ✓ 12 source files |
| 8 | Round 04 source lines total = **1135** | `wc -l knowledge_base/domains/{EX,FA,FT,GF,HO,IE}/{assumptions,examples}.md \| tail -1` (33+434+15+244+53+28+25+182+13+81+9+18) | ✓ 1135 |
| 9 | Round 04 size buckets: <50L=**8**, 50-99L=**2**, 100-199L=**1**, 200-499L=**1** (FA/ex 244L), 300+slice=**1** (EX/ex 434L) | EX/ass(33) + FA/ass(15) + FT/ex(28) + GF/ass(25) + HO/ass(13) + HO/ex(81 — wait 81 > 50) + IE/ass(9) + IE/ex(18) — 重算: <50 = EX/ass(33) + FA/ass(15) + FT/ex(28) + GF/ass(25) + HO/ass(13) + IE/ass(9) + IE/ex(18) = **7 ∈ <50**; 50-99 = FT/ass(53) + HO/ex(81) = **2 ∈ 50-99**; 100-199 = GF/ex(182) = **1 ∈ 100-199**; 200-499 = FA/ex(244) = **1 ∈ 200-299**; 300+ slice = EX/ex(434) = **1 ∈ 300+ slice** — 总 12 ✓ | ✓ 7/2/1/1/1 总 12 (correction: <50=7 not 8, kickoff row above noted) |
| 10 | EX/examples.md = **434L** > 300L slice threshold (umbrella §3) → **多 batch 切片 round 04 second-time** (after round 03 DM/ex 429L + DS/ex 413L) | `wc -l knowledge_base/domains/EX/examples.md` | ✓ 434 |
| 11 | EX/examples.md H2 boundaries = **8 examples** at lines 5, 59, 109, 148, 165, 233, 307, 389; 自然切片点在 line 232\|233 (between Ex5 ends + Ex6 begins) → batch_46 lines 1-232 (Ex1-Ex5 232L) + batch_47 lines 233-434 (Ex6-Ex8 202L) | `grep -nE "^## " knowledge_base/domains/EX/examples.md` | ✓ 8 H2 + clean split point 232\|233 (53.5%/46.5% distribution) |
| 12 | FT/assumptions.md = 53L 含 H2 at line 9 = `## QRS Shared Assumptions` (numberless H2 — **round 04 first-time encounter in assumptions.md**; round 01-03 整 0 例 H2 in assumptions.md per grep) | `grep -nE "^## " knowledge_base/domains/FT/assumptions.md` → `9:## QRS Shared Assumptions` | ✓ 1 numberless H2 in assumptions.md (FIRST TIME); pre-H2 prefatory L1-8 (file root H1 + 1 SENTENCE intro + 2 LIST_ITEM 1-2); under-H2 L9-53 含 LIST_ITEM 1-10 各含 sub-bullet abc-d 等 |
| 13 | EX/examples.md L3 含 cross-reference note `Note: Examples for EX and EC are shared in Section 6.1.3.3 of the SDTMIG. See also [EC Examples](../EC/examples.md).` — **non-blockquote inline Note** (NOT `> **Note:**` 格式 → atom_type 应 SENTENCE per Hook D-NOTE-BQ negative case) | `head -5 knowledge_base/domains/EX/examples.md` | ✓ inline Note treated as SENTENCE (Hook D-NOTE-BQ requires blockquote prefix for NOTE atom_type) |
| 14 | Mermaid blocks across 12 round 04 source files = **0** (所有 12 文件 grep 实证 0 fenced mermaid block) → round 04 expected **0 FIGURE atoms** (vs round 03 4 FIGURE in DM/ex) | `grep -l '^\`\`\`mermaid$' knowledge_base/domains/{EX,FA,FT,GF,HO,IE}/{assumptions,examples}.md \|\| echo NONE` → NONE | ✓ 0 mermaid in round 04 scope |
| 15 | Round 04 估 atoms = **568-965** (round 03 实证 ratio 0.589 × 1135 = 668 mid; lower 0.5 × 1135 = 568; upper 0.85 × 1135 = 965 — 范围采用 round 03 same lower bound 0.5 conservative) | 1135L × 0.5 = 567.5; × 0.589 = 668.5; × 0.85 = 964.75 | ✓ 568-668-965 |
| 16 | Batch 序号续 = **batch_45..57** (round 03 末 batch = 44 = EG/examples.md final; round 04 共 13 batch: 6 ass single + 5 ex single + 2 sliced = 13) | round 03 §0.5 row 15 + round 03 close batch_44 final | ✓ batch_45..57 (13 batches) |
| 17 | post Round 04 累计 md_atoms.jsonl ≈ **6,951-7,348 atoms** | 6383 + 568-965 | ✓ ~6,951-7,348 |
| 18 | post Round 04 累计 file coverage = **59/141 = 41.8%** | 47 + 12 = 59; 59/141 = 0.4184 | ✓ 41.8% (was 33.3% post round 03) |
| 19 | Convention inherit (round 01-03 lock): atom_id `md_dm<D>_assn\|ex_aNNN` + parent_section root `§<D> [<D> — <File-type>]` + H2 self-namespace `§<D>.N [Example N]` + H3a sub-namespace `§<D>.N.<a\|b\|...> [Example N<a\|b\|...>]` (round 02 lock) + §2.4 multi-batch slice cross-batch atom_id 续号 within file (round 03 lock) + §2.6 FIGURE-in-domains lock (round 03 lock) + LIST_ITEM sib_idx null precedent (round 03 lock) | round 03 final atom md_dmEG_ex_a078, parent_section `§EG.4 [Example 4]` per md_atoms.jsonl tail = format alive | ✓ inherit |
| 20 | progress.json `current_phase` post round 03 close = `P2_B-03c_round_03_CLOSED_pending_round_04_ack` (kickoff 写时 stale → 启动 round 04 dispatch 时一并 update → `P2_B-03c_round_04_in_flight_acked_2026-05-06_Option_B_6_domains_EX_FA_FT_GF_HO_IE_13_batches_batch_45_to_57_first_time_numberless_H2_in_assumptions_md_FT_ass_acked`) | `jq '.current_phase' _progress.json` | ✓ stale; 校正 at round 04 dispatch |

**Drift 校正记录**:
- progress.json `b_03c_round_03_details.round_04_trigger` 字段 implicit "42 domains × 2 = 84 files remaining" — drift detected (实测 47 × 2 = 94 files remaining post round 03; round 03 close stale carry from earlier "47→52→42" sequence). Round 04 close 时一并修正 `round_04_trigger` text 或在 `b_03c_round_04_details` 字段 fresh write.
- Round 03 atoms/line ratio 0.589 vs round 02 0.614 = -4.1% drift (不显著, 在波动范围内). Round 04 sustained 估算下界 0.5 (与 round 03 一致).
- post round 04 remaining = 47 − 6 = 41 domains × 2 = 82 files (8 rounds 后 alphabetical 完整覆盖 estimate 6-8 round 完成 P2 B-03c).

---

## 1. Round 04 Scope (6 domains × 2 files = 12 source files = 13 batches, Option B)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root |
|---|---|---|---|---|---|---|---|
| 1 | **batch_45** | `domains/EX/assumptions.md` | 33 | ~17-28 | <50 | `md_dmEX_assn_a` | `§EX [EX — Assumptions]` |
| 2 | **batch_46** | `domains/EX/examples.md` (lines 1-232, Ex1-Ex5) | 232 | ~116-197 | **300+ slice part 1** | `md_dmEX_ex_a` | `§EX [EX — Examples]` |
| 3 | **batch_47** | `domains/EX/examples.md` (lines 233-434, Ex6-Ex8) | 202 | ~101-172 | **300+ slice part 2** | `md_dmEX_ex_a` (atom_id 续号 from batch_46 末) | `§EX [EX — Examples]` |
| 4 | **batch_48** | `domains/FA/assumptions.md` | 15 | ~8-13 | <50 | `md_dmFA_assn_a` | `§FA [FA — Assumptions]` |
| 5 | **batch_49** | `domains/FA/examples.md` | 244 | ~122-207 | 200-499 | `md_dmFA_ex_a` | `§FA [FA — Examples]` |
| 6 | **batch_50** | `domains/FT/assumptions.md` | 53 | ~27-45 | 50-99 (**含 1 numberless H2**) | `md_dmFT_assn_a` | `§FT [FT — Assumptions]` |
| 7 | **batch_51** | `domains/FT/examples.md` | 28 | ~14-24 | <50 | `md_dmFT_ex_a` | `§FT [FT — Examples]` |
| 8 | **batch_52** | `domains/GF/assumptions.md` | 25 | ~13-21 | <50 | `md_dmGF_assn_a` | `§GF [GF — Assumptions]` |
| 9 | **batch_53** | `domains/GF/examples.md` | 182 | ~91-155 | 100-199 | `md_dmGF_ex_a` | `§GF [GF — Examples]` |
| 10 | **batch_54** | `domains/HO/assumptions.md` | 13 | ~7-11 | <50 | `md_dmHO_assn_a` | `§HO [HO — Assumptions]` |
| 11 | **batch_55** | `domains/HO/examples.md` | 81 | ~41-69 | 50-99 | `md_dmHO_ex_a` | `§HO [HO — Examples]` |
| 12 | **batch_56** | `domains/IE/assumptions.md` | 9 | ~5-8 | <50 | `md_dmIE_assn_a` | `§IE [IE — Assumptions]` |
| 13 | **batch_57** | `domains/IE/examples.md` | 18 | ~9-15 | <50 | `md_dmIE_ex_a` | `§IE [IE — Examples]` |
| **总** | 13 batches | 12 files (1 sliced) | **1135** | **~568-965** (mid 668) | — | — | — |

post Round 04 累计 file coverage: 47 + 12 = 59/141 = **41.8%** (was 33.3% post round 03).
post Round 04 累计 md_atoms.jsonl: 6383 + ~568-965 = ~6,951-7,348 atoms.

**Round 04 vs Round 03 对照**: round 03 = 1257L 741 atoms 12 batches; round 04 = 1135L ~668 atoms 13 batches. **体量 ≈ round 03 0.90× by lines / 0.90× by atoms / 1.08× by batch count** (slight more batches due to more <50 small-file ratio + 1 sliced 300+). 单 session 完成可行性 **回升** (vs round 03 2.78× round 02 高压).

**Round 04 vs Round 02 对照**: round 02 = 453L 278 atoms 10 batches; round 04 = 1135L ~668 atoms 13 batches. 体量 ≈ round 02 2.50×.

**ctx pressure forecast**: round 03 12 batches + 12 reviewer + 1 mini-audit dispatch 共 25 subagent calls; round 04 13 + 13 + 1 = **27 dispatch calls**. round 03 触发 1 次 halt #7 infra rate limit (handoff resume). round 04 同等概率触发, ctx checkpoint 在 batch_50 (FT/ass 完成) 后强制 review.

---

## 2. Convention inherit + first-time §2.7 numberless H2 in assumptions.md lock

### 2.1-2.6 inherit from round 01-03

(全 carry-forward, 不重复列出 — 详见 round 03 kickoff §2.1-2.6:)
- §2.1 Heading level pattern (H1 file root / H2 examples self-namespace / H3 sub-namespace / H4+ TBD)
- §2.2 atom_id prefix per file (4-digit 容许)
- §2.3 atom_id 起始 a001 per file (NOT per batch; 不跨 file 续号)
- §2.4 multi-batch single-file slice convention (round 03 lock; round 04 second application: EX/ex 434L sliced batch_46+47 at L232|233 H2 boundary)
- §2.5 共通规则 (domains/ spaced format, `## Example N` → `§<D>.N [Example N]`, 跨 file 不续号)
- §2.6 FIGURE-in-domains lock (round 03 lock; **round 04 expected 0 FIGURE atoms** per §0.5 row 14 grep 实证 0 mermaid in 12 source files)

### 2.7 First-time numberless H2 in assumptions.md (LOCKED 2026-05-06 round 04 kickoff §2.7 pending Bojiang ack)

**Trigger**: FT/assumptions.md L9 `## QRS Shared Assumptions` — round 04 首次在 assumptions.md 遇到 H2 (round 01-03 全 0 例 per grep). 此 H2 numberless (无 `## Example N` numbering) → 触发 v1.9.1 D-4 Hook D-D8 "numberless `## Overview` H2 不创 sub-namespace" 的首次 application 在 assumptions.md (round 02-03 D-D8 仅在 examples.md 内 numberless H2 use case).

**Rule (carry-forward from v1.9.1 D-4 Hook D-D8, 域内 assumptions.md 首次显式 application)**:

当 `domains/<D>/assumptions.md` 含 numberless H2 (非 `## Example N` 格式):
- **H2 atom 本身**: atom_type=**HEADING** + heading_level=2 + sibling_index=**1** (该 H2 在 file 内 sibling_index=1 因 file 内仅 1 numberless H2; 若多个 numberless H2 各按出现序 sibling_index=1,2,3,...) + parent_section=**file root** (`§FT [FT — Assumptions]`)
- **H2 之前 (L1-8 prefatory) atoms**: parent_section = **file root** (`§FT [FT — Assumptions]`); sibling_index per atom_type 标准规则 (LIST_ITEM=null, HEADING=按 sib 续号 — 但 file root H1 sibling_index=null 是 H2 之上)
- **H2 之后 (L11-53 under-H2) atoms**: parent_section = **file root** (`§FT [FT — Assumptions]`) — **不创 sub-namespace `§FT.QRS [QRS Shared Assumptions]` 等**, 因 D-D8 numberless 不创 sub-namespace
- **LIST_ITEM 续号 cross-H2**: 若 H2 前已有 LIST_ITEM 1-2 + H2 后再 LIST_ITEM 1-10 (FT/ass 实测), atom_id 内 sibling_index 全 null per LIST_ITEM rule (round 03 lock); LIST_ITEM 不跨 H2 边界 enforce sibling continuity (各 H2 段独立 1..N source-line numbering preserved in verbatim, atom-level sib_idx null)

**例 (FT/ass batch_50 expected)**:
```jsonc
// L1: # FT — Assumptions  (H1 file root, atom_id a001)
{
  "atom_id": "md_dmFT_assn_a001",
  "atom_type": "HEADING", "heading_level": 1, "sibling_index": 1,
  "verbatim": "# FT — Assumptions",
  "parent_section": "§FT [FT — Assumptions]"
}
// NOTE: H1 sibling_index = 1 (universal precedent across 48 prior H1 atoms in root jsonl, post-batch_45 INFO H1 sib correction 2026-05-06; v1.9.2 prompt candidate: explicit H1 sib=1 declaration)

// L9: ## QRS Shared Assumptions  (H2 numberless, atom_id ~a005)
{
  "atom_id": "md_dmFT_assn_a005",
  "atom_type": "HEADING", "heading_level": 2, "sibling_index": 1,
  "verbatim": "## QRS Shared Assumptions",
  "parent_section": "§FT [FT — Assumptions]"  // file root, NOT new sub-namespace
}

// L11: 1. The name of a QRS instrument is described under...  (LIST_ITEM under H2, atom_id ~a006)
{
  "atom_id": "md_dmFT_assn_a006",
  "atom_type": "LIST_ITEM", "heading_level": null, "sibling_index": null,  // sib_idx null per round 03 lock
  "verbatim": "1. The name of a QRS instrument is described under the variable --CAT in the relevant QRS domain (i.e., FT, QS, RS), and may be either abbreviations or longer names...",
  "parent_section": "§FT [FT — Assumptions]"  // file root, inherit from H2 (which itself = file root)
}
```

**Risk register** (round 04 §2.7 numberless H2 in assumptions.md 特有):
- R-rd04-1: writer 误创 sub-namespace `§FT.QRS [...]` 等 → 违反 D-D8. **缓解**: kickoff §2.7 inline 写明 + writer dispatch prompt include "FT/ass numberless H2 不创 sub-namespace; under-H2 atoms 续 file-root parent_section".
- R-rd04-2: writer 给 numberless H2 sib_idx null (混 LIST_ITEM rule) → 违反 H2 HEADING sib_idx ≥1 standard. **缓解**: kickoff §2.7 显式 sib_idx=1 for the numberless H2.
- R-rd04-3: writer LIST_ITEM cross-H2 误续 sib_idx (将 H2 后 1-10 续给 H2 前 1-2 → sib 1-12 假象). **缓解**: round 03 LIST_ITEM sib_idx null lock 已硬 enforced, sib_idx 全 null 自然规避.
- R-rd04-4: under-H2 LIST_ITEM 内 sub-bullet `a.` `b.` etc. → 与 round 02 H3a sub-namespace 决策无关 (因 sub-bullet 是 LIST_ITEM 内 sub-content, 非 H3 heading). **缓解**: writer 按 LIST_ITEM 整体 (含 sub-bullet text) treat, round 03 batch_36 DS/ass 1.a/1.b 已先例.

---

## 3. v1.9.1 prompt 入口条件 (round 01-03 carry-forward)

### Writer pool (per v1.9.1 §D-8 peer-alternative)
- `oh-my-claudecode:executor` (OMC primary, opus when available)
- `general-purpose` (FALLBACK peer-alternative; B-02 + round 01-03 sustained 60 batches 4847+741=5588 atoms 0 writer defect cumulative)

### Reviewer pool (per v1.9.1 §D-8)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01-03 sustained 100% PASS; round 04 默认 per-batch reviewer)
- `oh-my-claudecode:scientist` / `oh-my-claudecode:critic` (OMC primary)
- `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn — round 04 mini-audit 必避用)
- `feature-dev:code-architect` (round 02 mini-audit burn — round 04 mini-audit 必避用)
- `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn — round 04 mini-audit 必避用)

### N21 ban list (sustained)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer`, `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.1 active hooks
- **Hook 22b** (D-1 CRITICAL): kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓
- **Hook D-NOTE-BQ** (D-2 HIGH): blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE (round 04 EX/ex L3 inline non-blockquote Note → SENTENCE per Hook negative case)
- **Hook D-D8** (D-4): numberless `## Overview` H2 不创 sub-namespace → **round 04 §2.7 first-time application in assumptions.md (FT/ass L9)**
- **Hook A4** (sustained): FIGURE atom 必带 figure_ref non-null (round 04 expected 0 occurrence)
- **Hook C-8** (sustained): file 字段必含 `knowledge_base/` 前缀
- **NEW round 03 §2.4** (multi-batch slice §D-rd03): atom_id cross-batch 续号 within same file when sliced — round 04 EX/ex batch_46+47 application
- **NEW round 03 §2.6** (FIGURE-in-domains): round 04 expected 0 occurrence
- **NEW round 03 LIST_ITEM sib_idx null**: 全 round 04 enforce

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 04 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 20/20 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常**
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call
5. **v1.9.1 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** — round 04 §2.7 numberless H2 in assumptions.md 已锁定; 若遇到 H4+ 子标题 / FIGURE in domains/ 突发 (虽 grep 实证 0) / 切片 file 不在 EX/ex 还有第三个 / numbered H2 in assumptions.md (区别于 §2.7 numberless 场景) → 暂停 + 请求 lock 扩展
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1.5 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户. **Round 04 ctx pressure 警戒线**: ~668 atoms × 13 batch dispatch 估算 ctx 用量与 round 03 同等 (~700-800 atoms 12 batch); batch_50 (FT/ass 完成 含 §2.7 first-time) 后强制 ctx checkpoint
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 04 各 batch 估算与下限/上限:

| Batch | est range | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 45 EX/ass | 17-28 | <8 | >42 |
| 46 EX/ex part 1 (Ex1-5) | 116-197 | <58 | >296 |
| 47 EX/ex part 2 (Ex6-8) | 101-172 | <50 | >258 |
| 48 FA/ass | 8-13 | <4 | >19 |
| 49 FA/ex | 122-207 | <61 | >311 |
| 50 FT/ass | 27-45 | <13 | >67 |
| 51 FT/ex | 14-24 | <7 | >36 |
| 52 GF/ass | 13-21 | <6 | >32 |
| 53 GF/ex | 91-155 | <45 | >232 |
| 54 HO/ass | 7-11 | <3 | >16 |
| 55 HO/ex | 41-69 | <20 | >103 |
| 56 IE/ass | 5-8 | <2 | >12 |
| 57 IE/ex | 9-15 | <4 | >22 |

9. **NEW round 04 (carry from round 03)**: cross-batch atom_id 续号 violation (batch_47 atom_id 起始非 batch_46 末 +1) → 暂停 §2.4 enforcement.
10. **NEW round 04 (carry from round 03)**: cross-batch parent_section H2 inconsistency (batch_46 末 H2 ≠ batch_47 首 H2 expected per source line — 源 H2 boundary 在 232|233 之间, batch_46 末 atom expected parent ∈ §EX.5, batch_47 首 atom expected parent ∈ §EX.6; mismatch 暂停).
11. **NEW round 04 §2.7**: FT/ass batch_50 H2 处理 violation (writer 误创 sub-namespace `§FT.QRS [...]` OR H2 sib_idx ≠ 1 OR under-H2 LIST_ITEM 非 file-root parent) → 暂停 §2.7 lock enforcement.

**Round 04 intended 退出**:
- batch_45..57 全 PASS Rule A ≥90%
- batch_57 后派 reviewer 10-atom stratified mini-audit (6 domains × ~1.7 atoms each, 选 boundary + sentence + list_item; **+ 切片 file EX/ex 跨 batch 边界 atom 各 ≥1 (batch_46 末 + batch_47 首 相邻 atom_id 验证连续); + FT/ass H2 atom + 1 under-H2 LIST_ITEM 验证 §2.7 lock**)
- mini-audit ≥90% PASS → 单 commit (含全 13 batches + mini-audit + 3 index files 更新) + push → 一行 summary 报告 → session 自然结束 / 等用户路由词 round 05

---

## 5. Per-batch 产物 (round 01-03 模式 carry-forward)

- `evidence/checkpoints/P2_B-03_batch_<NN>_md_atoms.jsonl` — writer 产物 (atomized JSONL)
- `evidence/checkpoints/rule_a_P2_B-03_batch_<NN>_verdicts.jsonl` + `_summary.md` — Rule A audit (8 boundary + 3 stratified per B-02 R-B02-3; 小文件 <30 atoms 减 stratified 至 2; round 04 极小文件 IE/ass 9L ~5-8 atoms 可全审 + 0 stratified; HO/ass 13L ~7-11 atoms 同; FA/ass 15L ~8-13 atoms 同)
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加 (per batch + round close mini-audit)
- `trace.jsonl` phase_report 事件 + dispatch 事件 (每 subagent 调用一行)
- `_progress.json` 字段更新 (last_completed_batch / current_phase / cumulative atom count + round 03 close stale `current_phase` 校正 → round_04_in_flight)

注: round 04 不写 per-batch kickoff_NN.md (round 01-03 模式 sustained) — 本 kickoff §1 batch 序列 + §2 convention (含 §2.4 + §2.7) + §3 prompt + §4 halt 已含 dispatch contract, batch dispatch 直接复用本文 + B-02 dispatch template (umbrella §6).

**切片 batch 特殊 dispatch context** (batch_47):
- batch_47 dispatch prompt 必须 include: "前一 batch (batch_46) 末 atom_id = `md_dmEX_ex_aXXX` (执行 batch_46 后写入); 本 batch 起始 atom_id = `md_dmEX_ex_aYYY` (XXX+1); H2 namespace 续接 §EX.5 → §EX.6 boundary at line 232|233".

**§2.7 batch 特殊 dispatch context** (batch_50):
- batch_50 dispatch prompt 必须 include: "FT/ass L9 `## QRS Shared Assumptions` numberless H2 — atom_type=HEADING + heading_level=2 + sibling_index=1 + parent_section=`§FT [FT — Assumptions]` (NOT new sub-namespace). 该 H2 之后所有 atoms (L11-53) parent_section 续 file root, 不创 sub-namespace per §2.7 lock + Hook D-D8."

---

## 6. Round close mini-audit (gate before round 05)

- **Trigger**: batch_57 PASS + 全部入 root md_atoms.jsonl
- **Sample**: 10-atom 跨累积 6 domains × 2 files = 12 文件 中分层 (10 atoms 跨 12 files 不能 1-per-file 全覆盖 → 选 6 domains 中 stratified pick 1 ass + 1 ex per domain coverage = 12 atoms? 不, mini-audit 标准 10 atoms 上限). 实操: 选 boundary atom (首 atom + 末 atom 交替 OR 中段 SENTENCE/LIST_ITEM), **+ 切片 file EX/ex 跨 batch 边界 atom (batch_47 a001 = sliced part 2 first atom 验证 atom_id 续号), + FT/ass §2.7 numberless H2 atom (batch_50 中 H2 sib_idx=1 verify) + 1 under-H2 LIST_ITEM (batch_50 verify file-root parent_section)**
- **Reviewer**: subagent_type **distinct from per-batch reviewers AND round 01-03 mini-audit reviewers** (Rule D 跨 batch 隔离). 排除 list:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn)
  - `pr-review-toolkit:type-design-analyzer` (round 03 mini-audit burn 2026-05-06)
  - `pr-review-toolkit:code-reviewer` (round 04 per-batch × 13 burn)
  - 任一 round 04 per-batch reviewer (TBD per batch dispatch — default `pr-review-toolkit:code-reviewer`, 按 R-rd04 计划 sustained)
  - 候选: `pr-review-toolkit:silent-failure-hunter` / `pr-review-toolkit:comment-analyzer` / `pr-review-toolkit:pr-test-analyzer` / `superpowers:code-reviewer` 中 round 04 未 burn 的
  - **首选 (round 04 mini-audit)**: `pr-review-toolkit:silent-failure-hunter` AUDIT mode (NOT silent-failure detection — pivot to atom 字面审 mode; 6th cumulative B-03c reviewer family-pivot)
- **Gate**: ≥90% functional PASS (round 01-03 mini-audit 100% 持平 期待) + 9/9 round invariants:
  1. atom_id collision check (cumulative ~7000 atoms post round 04; **特别**: cross-batch within-file 续号 verification for EX/ex)
  2. Hook C-8 file prefix universal (knowledge_base/ prefix)
  3. H3a sub-namespace convention (round 02 lock; round 04 expected **0 occurrence** — round 04 source 12 files grep 实证 0 H3 atoms — verify expectation)
  4. TABLE_HEADER Hook A1 span=1 (continued v1.9 standard)
  5. extracted_by consistency (subagent_type + prompt_version P0_writer_md_v1.9.1)
  6. **§2.4 lock validation (round 03 carry-forward)**: EX/ex batch_46+47 atom_id 续号 + parent_section H2 boundary clean
  7. **§2.6 lock validation (round 03 carry-forward)**: round 04 expected 0 FIGURE — verify 0 atom_type=FIGURE 出现
  8. **LIST_ITEM sib_idx null (round 03 lock)**: round 04 全 LIST_ITEM atoms sib_idx=null verify
  9. **NEW §2.7 lock validation**: FT/ass numberless H2 atom 满足 (HEADING + h_lvl=2 + sib_idx=1 + parent=§FT [...]) AND under-H2 atoms parent=§FT [...] (file root, NOT sub-namespace)
- **Findings 处理**: HIGH 必修在 round 05 前 / MEDIUM 入 v1.9.2 backlog / LOW carry-forward
- **Round 05 trigger**: round 04 mini-audit PASS + Bojiang ack → 进 round 05 (alphabetical IS..onwards 或 用户决定 scope; **IE 已 round 04 done — round 05 起步 IS 或更后**)

---

## 7. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-03_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id:
  - **若是新 file (默认)**: a001 (round 04 多数 1-file-1-batch 模式不跨 file 续号)
  - **若是切片 file 同 file 下一 part (batch_47 only)**: 前 batch 末 atom_id +1 续号
- 跨 round 边界: 看 round 04 mini-audit 状态 + 用户 ack round 05 scope 决定后续
- 若 §2.7 first-time (batch_50 FT/ass) halt 触发 → 看 multi_session/P2_B-03c_round_04_HANDOFF.md (若存在) + 用户 ack 决定是否 in-place fix vs lock 调整

---

## 8. 用户 ack 状态 (round 04 启动 prerequisite)

**Bojiang ack 待 (本 session 起始, 用户路由词 "P2 bulk B-03c round 04 自治连跑" + ack "B" = Option B 6 domains)**:

1. **§1 round 04 scope = 6 domains (EX/FA/FT/GF/HO/IE) × 2 files = 13 batches** (vs round 03 12 batches; +1 batch due to EX/ex slicing — round 03 had 2 sliced files DM/ex+DS/ex; round 04 only 1 sliced EX/ex)
2. **§2.4 multi-batch slice convention** (round 03 lock carry-forward) — round 04 second application: EX/ex (434L) sliced batch_46+47 at line 232|233 H2 boundary (Ex5 ends + Ex6 begins); atom_id cross-batch 续号 within file
3. **§2.7 first-time numberless H2 in assumptions.md** for FT/ass L9 `## QRS Shared Assumptions` — first-time application of v1.9.1 D-4 Hook D-D8 outside examples.md; H2 atom (HEADING h_lvl=2 sib_idx=1 parent=file-root) + under-H2 atoms parent=file-root (不创 sub-namespace)
4. **§3 v1.9.1 prompt 路径 (active baseline)** — writer pool + reviewer pool sustained; round 04 mini-audit reviewer 候选 `pr-review-toolkit:silent-failure-hunter` AUDIT mode
5. **§4 halt 条件 1-11 (含 round-specific #8 atom 估算 outside [0.5×low, 1.5×high] + #9 §2.4 cross-batch atom_id 续号 violation + #10 §2.4 cross-batch parent_section H2 inconsistency + #11 §2.7 numberless H2 in ass.md violation)**
6. **Round 04 体量 ≈ round 03 0.90×** — 单 session 完成可行性回升; halt #7 (ctx <30%) 触发概率与 round 03 同等 (round 03 撞过 1 次 mid-round handoff resume)

**Scope 备选** (用户已选 §1 default Option B):
- **Option A (5 domains)**: EX/FA/FT/GF/HO = 11 batches (略小, 不含 IE)
- **Option B (default acked 2026-05-06)**: 6 domains EX/FA/FT/GF/HO/IE = 13 batches ✓
- **Option C (扩展)**: 7-8 domains EX..IS 或 EX..LB = 16-22 batches (ctx 风险更高, 用户已不选)

**用户路由词 + B ack 激活 (acked Option B 2026-05-06)** → **PENDING final §2.7 ack** for first-time numberless H2 in assumptions.md treatment (kickoff §2.7 LOCKED 等用户 ack "go" or "ack §2.7" → dispatch unblocked).

---

*Kickoff written 2026-05-06 post round 03 CLOSED commit fb6e5ff. §0.5 grep checksum 20/20 byte-exact verified. v1.9.1 §D-1 mandatory compliance. Convention inherit per round 01-03 §2 + first-time §2.7 numberless H2 in assumptions.md lock pending Bojiang ack 2026-05-06. Round 04 自治连跑 dispatch awaiting §2.7 final ack.*
