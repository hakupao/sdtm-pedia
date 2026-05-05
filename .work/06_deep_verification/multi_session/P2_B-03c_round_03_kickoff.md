# P2 B-03c Round 03 — Multi-Domain Autonomous Cycle Kickoff (DM..EG scope)

> 创建: 2026-05-06 (post B-03c round 02 CLOSED 同日, commit be3c7f4)
> 父 umbrella: `multi_session/P2_B-03_kickoff.md`
> 父 prompt: `subagent_prompts/P0_writer_md_v1.9.1.md` (8 D-rules) + `P0_matcher_v1.9.1.md` + `P0_reviewer_v1.9.1.md`
> Parent round close ref: `multi_session/P2_B-03c_round_02_kickoff.md` + commit be3c7f4 (10 batches 278 atoms 5 domains CO/AG/CV/DA/DD per-batch Rule A 100% × 10 + mini-audit 10/10 + 5/5 invariants PASS 100% reviewer feature-dev:code-architect; H3a sub-namespace first-time lock fully validated batch_26 2 H3 atoms parent §CP.1.a + §CP.1.b)
> 路由词: 用户在 session 说 **"P2 bulk B-03c round 03 自治连跑"** → 进本 kickoff dispatch (post §0.5 + §1 scope + §2.4 first-time slice convention 用户 ack)
> Convention 继承: round 01 §2 + round 02 §2 carry-forward (atom_id + parent_section + H3a sub-namespace lock); **round 03 §2.4 first-time extension**: multi-batch single-file slicing for DM/ex (429L) + DS/ex (413L) — both > 300L slice threshold per umbrella §3 (round 01 BE/ex 161L + CE/ex 165L 与 round 02 CP/ex 181L 都 single-batch < 300L; round 03 首次触发)

---

## §0.5 Kickoff numeric claim grep checksum (MANDATORY per v1.9.1 §D-1 CRITICAL)

逐项 grep-verified against source byte-exact (执行日 2026-05-06). 任何修改本 kickoff 的 numeric claim 必须重跑对应 verify 命令. 缺 §0.5 = orchestrator preflight FAIL.

| # | Claim | Source verify command | Match? |
|---|---|---|---|
| 1 | post B-03c round 02 CLOSE 时 md_atoms.jsonl 末原子 = `md_dmDD_ex_a038` (round 02 batch_32 final atom; parent_section `§DD.2 [Example 2]`; file `knowledge_base/domains/DD/examples.md`) | `tail -1 md_atoms.jsonl \| python3 -c "import sys,json; a=json.loads(sys.stdin.read()); print(a['atom_id'], a.get('parent_section'), a.get('file'))"` | ✓ md_dmDD_ex_a038, §DD.2 [Example 2], knowledge_base/domains/DD/examples.md |
| 2 | md_atoms.jsonl 当前总原子 = **5642** (post round 02 CLOSED) | `wc -l md_atoms.jsonl` | ✓ 5642 |
| 3 | round 02 实际产 atoms = **278** (5642 − 5364 round 02 起始基线) | progress.json status string `10_batches_278_atoms_5_domains` + commit be3c7f4 message | ✓ 278 |
| 4 | round 02 atoms/line ratio = 278/453 = **0.614** (实证 BELOW 0.7-0.9 范围 per umbrella §3 — drift detected, signal用 conservative 估算 round 03) | round 02 kickoff §0.5 row 8 source 453 + row 3 实证 278 | ✓ 0.614 |
| 5 | 累计 unique files atomized = **37** (post round 02; B-02 17 + round 01 10 + round 02 10) | post-B-03b 17 files + round 01 added 10 files (5 domains × 2) + round 02 added 10 files (5 domains × 2) = 37 | ✓ 37 |
| 6 | domains/ 余 = **52 domains** (63 total − 1 CM B-02 done − 5 round 01 done − 5 round 02 done) | `ls knowledge_base/domains/ \| grep -vE "^(CM\|AE\|AG\|BE\|BS\|CE\|CO\|CP\|CV\|DA\|DD)$" \| wc -l` | ✓ 52 |
| 7 | Round 03 scope = 5 domains alphabetical (DM / DS / DV / EC / EG) × 2 files = **10 source files** | 字母序 first 5 post round 02: `ls knowledge_base/domains \| grep -vE "^(CM\|AE\|AG\|BE\|BS\|CE\|CO\|CP\|CV\|DA\|DD)$" \| sort \| head -5` → DM DS DV EC EG | ✓ 10 source files |
| 8 | Round 03 source lines total = **1257** | `wc -l knowledge_base/domains/{DM,DS,DV,EC,EG}/{assumptions,examples}.md \| tail -1` (40+429+41+413+7+24+32+135+26+110) | ✓ 1257 |
| 9 | Round 03 size buckets: <50L=**4**, 50-99L=**0**, 100-199L=**2**, 200-499L=**2** | DM/ass(40) + DV/ass(7) + DV/ex(24) + EG/ass(26) = 4 ∈ <50; (none ∈ 50-99); EC/ex(135) + EG/ex(110) = 2 ∈ 100-199; DS/ass(41) + EC/ass(32) carry over to <50 = 6 actually; **重算 correction**: DM/ass(40)+DS/ass(41)+EC/ass(32)+DV/ex(24)+EG/ass(26)+DV/ass(7) = 6 ∈ <50; DS/ex(413) + DM/ex(429) = 2 ∈ 300+ (slice trigger); EC/ex(135) + EG/ex(110) = 2 ∈ 100-199 | ✓ <50=6 + 100-199=2 + 300+=2 总 10 |
| 10 | DM/examples.md = **429L** > 300L slice threshold (umbrella §3) → **多 batch 切片 first-time** | `wc -l knowledge_base/domains/DM/examples.md` | ✓ 429 |
| 11 | DS/examples.md = **413L** > 300L slice threshold (umbrella §3) → **多 batch 切片 first-time** | `wc -l knowledge_base/domains/DS/examples.md` | ✓ 413 |
| 12 | DM/examples.md H2 boundaries = **7 examples** at lines 3,16,66,103,216,264,356; 自然切片点在 line 215\|216 (between Ex4 ends + Ex5 begins) → batch_34 lines 1-215 (Ex1-Ex4 215L) + batch_35 lines 216-429 (Ex5-Ex7 214L) | `grep -nE "^## " knowledge_base/domains/DM/examples.md` | ✓ 7 H2 + clean split point |
| 13 | DS/examples.md H2 boundaries = **11 examples** at lines 3,47,63,85,116,136,154,171,190,210,334; 自然切片点在 line 209\|210 (between Ex9 ends + Ex10 begins) → batch_37 lines 1-209 (Ex1-Ex9 209L) + batch_38 lines 210-413 (Ex10-Ex11 204L) | `grep -nE "^## " knowledge_base/domains/DS/examples.md` | ✓ 11 H2 + clean split point |
| 14 | Round 03 估 atoms = **754-1069** (round 02 实证 ratio 0.614 × 1257 = 772; lower 0.6 × 1257 = 754; upper 0.85 × 1257 = 1069 — 范围放宽允许 round 03 ratio 回升至 round 01 0.782 水平) | 1257L × 0.6 = 754.2; × 0.85 = 1068.4 | ✓ 754-1069 |
| 15 | Batch 序号续 = **batch_33..44** (round 02 末 batch = 32 = DD/examples.md final; round 03 共 12 batch: 5 单 file + 4 单 file + 4 切片 batch — wait 重算: DM/ass + DS/ass + DV/ass + DV/ex + EC/ass + EC/ex + EG/ass + EG/ex = 8 single-batch + DM/ex×2 + DS/ex×2 = 4 sliced batch = 12 total batches batch_33..44) | round 02 §1 final row batch_32 = DD/examples.md | ✓ batch_33..44 |
| 16 | post Round 03 累计 md_atoms.jsonl ≈ **6,396-6,711 atoms** | 5642 + 754-1069 | ✓ ~6,396-6,711 |
| 17 | post Round 03 累计 file coverage = **47/141 = 33.3%** | 37 + 10 = 47; 47/141 = 0.3333 | ✓ 33.3% |
| 18 | Convention inherit (round 01 + 02 lock): atom_id `md_dm<D>_assn\|ex_aNNN` + parent_section root `§<D> [<D> — <File-type>]` + H2 self-namespace `§<D>.N [Example N]` + H3a sub-namespace `§<D>.N.<a\|b\|...> [Example N<a\|b\|...>]` (round 02 batch_26 lock) | round 02 final atom md_dmDD_ex_a038, parent_section `§DD.2 [Example 2]` per md_atoms.jsonl tail = format alive | ✓ inherit |
| 19 | Round 02 atoms/line ratio drift downward (0.782 round 01 → 0.614 round 02 = -21.5%) → Round 03 估算下界 0.6 conservative; halt #8 atom 估算 lowered floor | round 01 510/652=0.782 + round 02 278/453=0.614 | ✓ ratio drift documented |
| 20 | progress.json status string drift detected: text `47_domains_x_2_files_94_files_remaining` — 实测 52 domains × 2 files = 104 files (status string drift -5 domains; 在 round 03 close 时一并修正 47→52 + 94→104) | `ls knowledge_base/domains/ \| grep -vE "^(CM\|AE\|AG\|BE\|BS\|CE\|CO\|CP\|CV\|DA\|DD)$" \| wc -l` = 52 | ✓ 52/104 (status string `_progress.json` next write 修正 47→52 + 94→104) |

**Drift 校正记录**:
- progress.json status string contains "47_domains" + "94_files_remaining" — drift detected at round 03 kickoff write time. 实测 52 domains × 2 files = 104 files. Round 03 close 时 _progress.json status update 一并修正 47→52 + 94→104.
- progress.json `current_phase` = `P2_B-03c_round_01_CLOSED_pending_round_02_ack` — 也是 stale (round 02 已 CLOSED). Round 03 启动时 reconciler/orchestrator 一并修正 → `P2_B-03c_round_02_CLOSED_pending_round_03_ack` 或 `P2_B-03c_round_03_in_flight`.
- round 02 atoms/line ratio 0.614 vs round 01 0.782 = -21.5% drift downward. 原因假说: round 02 多 file <50L 小文件 (CV/ass 5L → 3 atoms 0.6 ratio; DD/ass 11L → 6 atoms 0.55) 拉低均值 + round 01 large-file CE/ex 165L 165 atoms 1.0 ratio 拉高均值. Round 03 同样有 4 个 <50L 小文件 + 2 个超大切片 file (DM/ex + DS/ex) — ratio 可能 reach round 02 水平; halt #8 估算下界相应放宽至 0.5×0.6×low.

---

## 1. Round 03 Scope (5 domains × 2 files = 10 source files = 12 batches)

| # | Batch | Target | Lines | 估 atoms | Bucket | atom_id prefix | parent_section root |
|---|---|---|---|---|---|---|---|
| 1 | **batch_33** | `domains/DM/assumptions.md` | 40 | ~24-34 | <50 | `md_dmDM_assn_a` | `§DM [DM — Assumptions]` |
| 2 | **batch_34** | `domains/DM/examples.md` (lines 1-215, Ex1-Ex4) | 215 | ~129-183 | **300+ slice part 1** | `md_dmDM_ex_a` | `§DM [DM — Examples]` |
| 3 | **batch_35** | `domains/DM/examples.md` (lines 216-429, Ex5-Ex7) | 214 | ~128-182 | **300+ slice part 2** | `md_dmDM_ex_a` (atom_id 续号 from batch_34 末) | `§DM [DM — Examples]` |
| 4 | **batch_36** | `domains/DS/assumptions.md` | 41 | ~25-35 | <50 | `md_dmDS_assn_a` | `§DS [DS — Assumptions]` |
| 5 | **batch_37** | `domains/DS/examples.md` (lines 1-209, Ex1-Ex9) | 209 | ~125-178 | **300+ slice part 1** | `md_dmDS_ex_a` | `§DS [DS — Examples]` |
| 6 | **batch_38** | `domains/DS/examples.md` (lines 210-413, Ex10-Ex11) | 204 | ~122-173 | **300+ slice part 2** | `md_dmDS_ex_a` (atom_id 续号 from batch_37 末) | `§DS [DS — Examples]` |
| 7 | **batch_39** | `domains/DV/assumptions.md` | 7 | ~4-6 | <50 | `md_dmDV_assn_a` | `§DV [DV — Assumptions]` |
| 8 | **batch_40** | `domains/DV/examples.md` | 24 | ~14-20 | <50 | `md_dmDV_ex_a` | `§DV [DV — Examples]` |
| 9 | **batch_41** | `domains/EC/assumptions.md` | 32 | ~19-27 | <50 | `md_dmEC_assn_a` | `§EC [EC — Assumptions]` |
| 10 | **batch_42** | `domains/EC/examples.md` | 135 | ~81-115 | 100-199 | `md_dmEC_ex_a` | `§EC [EC — Examples]` |
| 11 | **batch_43** | `domains/EG/assumptions.md` | 26 | ~16-22 | <50 | `md_dmEG_assn_a` | `§EG [EG — Assumptions]` |
| 12 | **batch_44** | `domains/EG/examples.md` | 110 | ~66-94 | 100-199 | `md_dmEG_ex_a` | `§EG [EG — Examples]` |
| **总** | 12 batches | 10 files (2 sliced) | **1257** | **~754-1069** | — | — | — |

post Round 03 累计 file coverage: 37 + 10 = 47/141 = **33.3%** (was 26.2% post round 02).
post Round 03 累计 md_atoms.jsonl: 5642 + ~754-1069 = ~6,396-6,711 atoms.

**Round 03 vs Round 02 对照**: round 02 = 453L 278 atoms 10 batches; round 03 = 1257L ~772 atoms (中点) 12 batches. **体量 ≈ round 02 2.78×** (atom 实测中点) — 单 session 完成可行性 **降低**, 主要由 DM/ex + DS/ex 两大切片 file 推高. 估算 ctx 用量增加 ~3×, halt #7 (ctx <30%) 触发概率上升; round 03 启动后须按 batch 紧密 monitor ctx, 若需要 mid-round handoff 主动写 resume prompt.

**Round 03 vs Round 01 对照**: round 01 = 652L 510 atoms 10 batches; round 03 = 1257L ~772 atoms 12 batches. 体量 ≈ round 01 1.51×.

---

## 2. Convention inherit + first-time extension §2.4 multi-batch slice lock

### 2.1-2.3 inherit from round 01 + round 02

| Heading level | Pattern | Example |
|---|---|---|
| H1 (file root) | `§<D> [<D> — <File-type>]` | `§DM [DM — Assumptions]` / `§DM [DM — Examples]` |
| H2 (only in examples) | `§<D>.<index> [<H2 title>]` | `§DM.1 [Example 1]` |
| H3 (round 02 lock) | sub-namespace `§<D>.<index>.<sub-index> [...]` from md suffix; H3 atom emits parent_section = its H2 parent; children inherit H3 sub-namespace | `### Example 1a` (h_lvl=3, sib=1, parent=§DM.1, sub-ns=§DM.1.a) |
| H4+ | TBD per future encounter | not in round 03 (none in 10 source files per grep) |

| File | Prefix | 4-digit 容许 (per v1.9.1 §D-7.13) |
|---|---|---|
| `domains/<D>/assumptions.md` | `md_dm<D>_assn_aNNN` | YES (round 03 max ~183 atoms in DM/ex part 1 < 999, no 4-digit needed) |
| `domains/<D>/examples.md` | `md_dm<D>_ex_aNNN` | YES |

aNNN 起始 `a001` per file (NOT per batch — see §2.4 below). 不跨 file 续号.

### 2.4 First-time multi-batch slice convention (LOCKED 2026-05-06 round 03 kickoff §2.4 pending Bojiang ack)

**Trigger**: 单 source file > 300L (umbrella §3 阈值). Round 03 首次触发 = DM/examples.md (429L) + DS/examples.md (413L).

**切片规则** (锁定):

1. **Split point at H2 boundary**: 切片点 = 自然 H2 line boundary (`## Example N` 之间), 永不切到 H2 内部 (atom continuity 保护). 若两 H2 之间长度极不均, 容许 ±5% 偏离均分.
2. **atom_id 续号 cross-batch within file**: 同一 source file 切片成 2 batch, **atom_id 续号 cross batch boundary** (不重置). 例: batch_34 末 atom = `md_dmDM_ex_a128`, batch_35 起始 atom = `md_dmDM_ex_a129`. 这与 round 01/02 跨 file 不续号约定区别.
3. **parent_section consistent within file**: H1 root (§DM [DM — Examples]) + H2 (§DM.N [Example N]) 在 cross-batch 边界保持一致; writer 必看到前一 batch 末 atom 的 parent_section context (kickoff 内 inline 注明).
4. **per-batch jsonl 输出 separate**: batch_34 写 `P2_B-03_batch_34_md_atoms.jsonl`; batch_35 写 `P2_B-03_batch_35_md_atoms.jsonl`. Reconciler-side merge 序按 batch 号 cat.
5. **每切片 batch 各自独立 Rule A**: batch_34 + batch_35 各派一次 reviewer agent, 不共享; per-batch ≥90% gate. Cross-batch atom_id collision check 在 mini-audit invariant #1 强化.
6. **Mini-audit cross-batch coverage**: round close mini-audit 10-atom 样本 中, 切片 file (DM/ex + DS/ex) 各贡献 ≥1 atom 跨 batch 边界 (e.g. batch_34 末 atom + batch_35 首 atom 相邻 atom_id 验证连续).

**Risk register** (round 03 sliced batch 特有):
- R-rd03-1: writer 若不知前一 batch 末 atom_id, 起始 a001 → atom_id collision. **缓解**: kickoff 内 inline 写明 batch_35 dispatch prompt 须 include "前 batch 末 atom_id = X, 续号 = X+1 起" instruction.
- R-rd03-2: 切片在 H2 boundary 不在 atom boundary. **缓解**: H2 自然 line gap (空行) 永远在 atom 之间, 不在 atom 内.
- R-rd03-3: batch_34 + batch_35 cross-batch parent_section H2 boundary 不一致. **缓解**: §2.1 inherit (H2 命名 deterministic from `## Example N` source line, writer 照搬不假设).

### 2.5 共通规则 (sustained)

- domains/ spaced format `§<D>` (无 numbered) — 区别于 chapters/ numbered
- examples 内 H2 `## Example N` → `§<D>.N [Example N]` 格式
- 跨 file (round 03 全 1-file-1-or-2-batch 模式) parent_section 不续接, atom_id 重置 a001

### 2.6 First-time FIGURE-in-domains lock (LOCKED 2026-05-06 round 03 batch_34 a072 in-place fix, Bojiang ack "Option 1 in-place fix")

**触发**: round 03 batch_34 a072 (DM/ex L115-149) writer 误标 CODE_LITERAL — round 01/02 整 0 例 FIGURE in domains/ (grep 实证 root md_atoms.jsonl). 此为 PLAN.md Appendix B 已 lock 约定首次在 domains/ 落地, NOT NEW convention.

**Rule (carry-forward from PLAN.md Appendix B + P0 Pilot v1.2 schema, 域内首次显式)**:

当 markdown 含 fenced Mermaid block (`^```mermaid$` ... `^```$`):
- atom_type = **FIGURE** (NOT CODE_LITERAL, NOT SENTENCE, NOT TABLE_*)
- verbatim = 完整 Mermaid 源码 byte-exact (含 fence 行 ` ```mermaid ` + ` ``` ` + 中间所有 graph 定义), preserved indentation
- figure_ref = non-null, 格式 `<file path> L<start>-<end> mermaid <graph type>: <one-line semantic description>` (Hook A4 sustained)
- line_start = fence-open line; line_end = fence-close line (含两端)
- parent_section = 该 figure 所在 H2 sub-namespace (e.g. `§DM.4 [Example 4]`)
- heading_level + sibling_index = null

**例 (a072 in-place fix)**:
```json
{
  "atom_id": "md_dmDM_ex_a072",
  "atom_type": "FIGURE",
  "file": "knowledge_base/domains/DM/examples.md",
  "line_start": 115, "line_end": 149,
  "verbatim": "```mermaid\\ngraph TD\\n    Q[...]\\n    ...\\n```",
  "parent_section": "§DM.4 [Example 4]",
  "heading_level": null, "sibling_index": null,
  "figure_ref": "knowledge_base/domains/DM/examples.md L115-149 mermaid graph TD: Race question CRF (RACE01-07) -> RACE + subcategory CRACE01-21 -> SUPPDM.QVAL data flow",
  "cross_refs": [],
  "extracted_by": {...}
}
```

**Round 03 affected**: batch_34 (1 FIGURE: a072 fixed) + batch_35 (3 FIGURE expected at L222-237 + L276-304 + L360-388 in DM/ex). batch_37/38 (DS/ex) grep 实证 0 mermaid block (DS/ex 仅 TABLE_ROW heavy). 其他 round 03 文件 (DV/EC/EG) 0 mermaid (待 grep 验证).

**Future rounds carry-forward**: RELSPEC/TD/TA/TV examples.md 含 mermaid (per round 03 grep), 后续 round 起 writer 默认按 §2.6 处理.

**CODE_LITERAL 正确用法保留**: CODE_LITERAL 仍专用于 **单字面 codelist 值** (e.g. `C66742`, `Y`, `N`) — 不用于 fenced code block.

---

## 3. v1.9.1 prompt 入口条件 (round 01 + 02 carry-forward)

### Writer pool (per v1.9.1 §D-8 peer-alternative)
- `oh-my-claudecode:executor` (OMC primary, opus when available)
- `general-purpose` (FALLBACK peer-alternative; B-02 + round 01 + round 02 sustained 27 batches 1898 atoms 0 writer defect cumulative)

### Reviewer pool (per v1.9.1 §D-8)
- `pr-review-toolkit:code-reviewer` (FALLBACK peer-alternative; B-02 + round 01 + round 02 sustained 100% PASS)
- `oh-my-claudecode:scientist` / `oh-my-claudecode:critic` (OMC primary)
- `feature-dev:code-reviewer` (cumulative inter-cycle audit; round 01 mini-audit + round 02 batch_23 已 burn — round 03 mini-audit 必避用)
- `feature-dev:code-architect` (round 02 mini-audit burn 2026-05-06 — round 03 mini-audit 必避用)

### N21 ban list (sustained)
`oh-my-claudecode:writer`, `Explore`, `oh-my-claudecode:explore`, `feature-dev:code-explorer`, `oh-my-claudecode:document-specialist`

### Rule D 硬约束
writer ≠ reviewer (不同 subagent_type, NOT 仅不同 instance).

### v1.9.1 active hooks
- **Hook 22b** (D-1 CRITICAL): kickoff §0.5 verified 100% byte-exact = trust kickoff numeric claims ✓
- **Hook D-NOTE-BQ** (D-2 HIGH): blockquote-prefix `> **Note:**` / `> **Exception:**` = atom_type NOTE
- **Hook D-D8** (D-4): numberless `## Overview` H2 不创 sub-namespace
- **Hook A4** (sustained): FIGURE atom 必带 figure_ref non-null
- **Hook C-8** (sustained): file 字段必含 `knowledge_base/` 前缀
- **NEW round 03 §2.4** (multi-batch slice §D-rd03): atom_id cross-batch 续号 within same file when sliced

---

## 4. 自治连跑 halt 条件 (per umbrella §10.2 + round 03 specific)

任一触发 → 暂停 + ping 用户, 不强行进下一步:

1. **任一 batch §0.5 grep checksum 任一项 FAIL** (numeric drift detected at kickoff write time — 本 kickoff 已 20/20 PASS)
2. **任一 batch Rule A audit < 90% PASS rate** 或现 HIGH severity finding
3. **Schema violation / atom_id collision / 9 atom_type 任一异常**
4. **Source markdown anomaly** 需 Rule B preserve + 业务 judgment call
5. **v1.9.1 prompt 路径 drift** — writer pool 任一不可用 OR reviewer pool 任一不可用 + FALLBACK 也不可
6. **Convention lock 首次扩展** — round 03 §2.4 multi-batch slice 已锁定; 若遇到 H4+ 子标题 / FIGURE in domains/ / 切片 file 不在 DM/ex + DS/ex 还有第三个 → 暂停 + 请求 lock 扩展
7. **ctx 紧张 (剩 < 30%)** 或 session 累计已 > 1.5 hr 仍未到 round 闭环 — 主动写 handoff.md + resume prompt 给用户. **Round 03 ctx pressure 警戒线提前**: ~772 atoms × 12 batch dispatch 估算 ctx 用量 round 02 (~278 atoms 10 batch) 的 2.5-3×; batch_38 (DS/ex part 2 完成) 后强制 ctx checkpoint
8. **Round-specific**: 任一 batch atom 数实际 outside 估算 [0.5×low, 1.5×high] → 暂停核 source / prompt drift. Round 03 各 batch 估算与下限/上限 (使用 round 02 实证 ratio 0.614 调低下界):

| Batch | est range | halt low (0.5×low) | halt high (1.5×high) |
|---|---|---|---|
| 33 DM/ass | 24-34 | <12 | >51 |
| 34 DM/ex part 1 (Ex1-4) | 129-183 | <64 | >275 |
| 35 DM/ex part 2 (Ex5-7) | 128-182 | <64 | >273 |
| 36 DS/ass | 25-35 | <12 | >53 |
| 37 DS/ex part 1 (Ex1-9) | 125-178 | <62 | >267 |
| 38 DS/ex part 2 (Ex10-11) | 122-173 | <61 | >260 |
| 39 DV/ass | 4-6 | <2 | >9 |
| 40 DV/ex | 14-20 | <7 | >30 |
| 41 EC/ass | 19-27 | <9 | >41 |
| 42 EC/ex | 81-115 | <40 | >173 |
| 43 EG/ass | 16-22 | <8 | >33 |
| 44 EG/ex | 66-94 | <33 | >141 |

9. **NEW round 03**: cross-batch atom_id 续号 violation (batch_35 atom_id 起始非 batch_34 末 +1; batch_38 atom_id 起始非 batch_37 末 +1) → 暂停 §2.4 enforcement.
10. **NEW round 03**: cross-batch parent_section H2 inconsistency (batch_34 末 H2 ≠ batch_35 首 H2 expected per source line — 源 H2 boundary 在 215|216 之间, batch_34 末 atom expected parent ∈ §DM.4, batch_35 首 atom expected parent ∈ §DM.5; mismatch 暂停).

**Round 03 intended 退出**:
- batch_33..44 全 PASS Rule A ≥90%
- batch_44 后派 reviewer 10-atom stratified mini-audit (5 domains × 2 atoms each, 选 boundary + sentence + list_item; **+ 切片 file 跨 batch 边界 atom 各 ≥1 (DM/ex batch_34末 a + batch_35首 b 相邻; DS/ex batch_37末 + batch_38首 相邻)**)
- mini-audit ≥90% PASS → 单 commit (含全 12 batches + mini-audit + 3 index files 更新) + push → 一行 summary 报告 → session 自然结束 / 等用户路由词 round 04

---

## 5. Per-batch 产物 (round 01 + 02 模式 carry-forward)

- `evidence/checkpoints/P2_B-03_batch_<NN>_md_atoms.jsonl` — writer 产物 (atomized JSONL)
- `evidence/checkpoints/rule_a_P2_B-03_batch_<NN>_verdicts.jsonl` + `_summary.md` — Rule A audit (8 boundary + 3 stratified per B-02 R-B02-3; 小文件 <30 atoms 减 stratified 至 2; round 03 极小文件 DV/ass 7L ~4 atoms 可全审 + 0 stratified)
- 追加 root `md_atoms.jsonl` (`>> md_atoms.jsonl`)
- `audit_matrix.md` 行追加 (per batch + round close mini-audit)
- `trace.jsonl` phase_report 事件 + dispatch 事件 (每 subagent 调用一行)
- `_progress.json` 字段更新 (last_completed_batch / current_phase / cumulative atom count + round 02 stale `current_phase` 校正 + status string drift 47→52 + 94→104 校正)

注: round 03 不写 per-batch kickoff_NN.md (round 01 + 02 模式 sustained) — 本 kickoff §1 batch 序列 + §2 convention (含 §2.4) + §3 prompt + §4 halt 已含 dispatch contract, batch dispatch 直接复用本文 + B-02 dispatch template (umbrella §6).

**切片 batch 特殊 dispatch context** (batch_35 + batch_38):
- batch_35 dispatch prompt 必须 include: "前一 batch (batch_34) 末 atom_id = `md_dmDM_ex_aXXX` (执行 batch_34 后写入); 本 batch 起始 atom_id = `md_dmDM_ex_aYYY` (XXX+1); H2 namespace 续接 §DM.4 → §DM.5 boundary at line 215|216".
- batch_38 dispatch prompt 同样 include cross-batch context for DS/ex.

---

## 6. Round close mini-audit (gate before round 04)

- **Trigger**: batch_44 PASS + 全部入 root md_atoms.jsonl
- **Sample**: 10-atom 跨累积 5 domains × 2 files = 10 文件 分层 (1 atom/file; 选 boundary atom: 首 atom + 末 atom 交替 OR 中段 SENTENCE/LIST_ITEM; **+ 切片 file DM/ex + DS/ex 各保证 ≥1 sample 跨 batch 边界**, 实操: 10 atom 样本中 DM/ex 选 1 atom 来自 batch_34/35 边界 (e.g. batch_35 a001 = sliced part 2 first atom); DS/ex 选 1 atom 来自 batch_37/38 边界 (e.g. batch_38 a001))
- **Reviewer**: subagent_type **distinct from per-batch reviewers AND round 01 + 02 mini-audit reviewers** (Rule D 跨 batch 隔离). 排除 list:
  - `feature-dev:code-reviewer` (round 01 mini-audit + round 02 batch_23 burn)
  - `feature-dev:code-architect` (round 02 mini-audit burn 2026-05-06)
  - `pr-review-toolkit:code-reviewer` (round 02 batch_24-32 + round 01 全 burn)
  - 任一 round 03 per-batch reviewer (TBD per batch dispatch)
  - 候选: `oh-my-claudecode:scientist` / `oh-my-claudecode:critic` / `superpowers:requesting-code-review` / `oh-my-claudecode:verifier` 中 round 03 未 burn 的
- **Gate**: ≥90% functional PASS (round 01 + 02 mini-audit 100% 持平 期待) + 5/5 round invariants:
  1. atom_id collision check (cumulative ~772 atoms; **特别**: cross-batch within-file 续号 verification for DM/ex + DS/ex)
  2. Hook C-8 file prefix universal (knowledge_base/ prefix)
  3. H3a sub-namespace convention (round 02 已 lock; round 03 应 0 occurrence per source grep — verify expectation)
  4. TABLE_HEADER Hook A1 span=1 (continued v1.9 standard)
  5. extracted_by consistency (subagent_type + prompt_version P0_writer_md_v1.9.1)
- **Findings 处理**: HIGH 必修在 round 04 前 / MEDIUM 入 v1.9.2 backlog / LOW carry-forward
- **Round 04 trigger**: round 03 mini-audit PASS + Bojiang ack → 进 round 04 (alphabetical EX..onwards 或 用户决定 scope; **EC 已 round 03 done — round 04 起步 EX 或更后**)

---

## 7. Recovery hint

若 session 中断:
- 看 `_progress.json` (主) 找 `current_phase` + `last_completed_batch`
- 看 `audit_matrix.md` P2 Bulk 表最后 PASS 行
- 看 `trace.jsonl` 尾 phase_report 事件
- 续 batch: 找 `evidence/checkpoints/P2_B-03_batch_<last_NN>_md_atoms.jsonl` 末原子的 atom_id, 下一 batch 起始 atom_id:
  - **若是新 file (默认)**: a001 (round 03 全 1-file-1-or-2-batch 模式不跨 file 续号)
  - **若是切片 file 同 file 下一 part (batch_35 / batch_38)**: 前 batch 末 atom_id +1 续号
- 跨 round 边界: 看 round 03 mini-audit 状态 + 用户 ack round 04 scope 决定后续

---

## 8. 用户 ack 状态 (round 03 启动 prerequisite)

**Bojiang ack 2026-05-06** (本 session 起始, 用户路由词 "P2 bulk B-03c round 03 自治连跑" + ack "Option A 全 ack 开始"):

1. **§1 round 03 scope = 5 domains (DM/DS/DV/EC/EG) × 2 files = 12 batches** (vs round 02 10 batches; +2 batches due to slicing)
2. **§2.4 first-time multi-batch slice convention** for DM/ex (429L) + DS/ex (413L); split at H2 boundary line 215|216 + 209|210; atom_id cross-batch 续号 within file; parent_section consistent
3. **§3 v1.9.1 prompt 路径 (active baseline)**
4. **§4 halt 条件 1-10 (含 round-specific #8 atom 估算 outside [0.5×low, 1.5×high] + #9 cross-batch atom_id 续号 violation + #10 cross-batch parent_section H2 inconsistency)**
5. **Round 03 体量 ≈ round 02 2.78×** — 单 session 完成可行性下降; halt #7 (ctx <30%) 触发概率上升; 若 mid-round 触发 ctx 警戒, 自动写 handoff.md + resume prompt 给用户

**Scope 备选** (用户可选取代 §1 default):
- **Option A (default 推荐)**: 5 domains DM/DS/DV/EC/EG = 12 batches (alphabetical 续 round 02; 完整 alphabetical follow-through)
- **Option B (保守)**: 2 domains DM/DS = 6 batches (batch_33..38, 2 单 file + 4 切片 batch); 优先验证 §2.4 first-time slice convention, mini-audit PASS 后再开 round 04 = DV/EC/EG
- **Option C (扩展)**: 7 domains DM/DS/DV/EC/EG/EX/FA = ~16-17 batches (alphabetical 多 2; ctx 风险更高, 不推荐除非用户确信)

**用户路由词激活 (acked Option A 2026-05-06)** → 默认 5 domains DM/DS/DV/EC/EG × 12 batches 全 dispatch (§2.4 first-time slice convention 对 DM/ex + DS/ex acked).

---

*Kickoff written 2026-05-06 post round 02 CLOSED commit be3c7f4. §0.5 grep checksum 20/20 byte-exact verified. v1.9.1 §D-1 mandatory compliance. Convention inherit per round 01 + 02 §2 + first-time §2.4 multi-batch slice lock acked Bojiang 2026-05-06. Round 03 自治连跑 dispatch unblocked.*
