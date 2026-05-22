# Q-S4 Claude — PARTIAL detail

## Question
DI 域 (Device Identifiers) 是哪个 SDTMIG version 引入? 属于哪个 SDTM dataset class (Special-Purpose / Events / Findings / Trial Design / Study Reference)? 列 DI 主要变量 (至少 3 个 Core=Req 变量) + 描述用途.

## Pre-existing KB-level limitation (4 平台共通)
`knowledge_base/domains/DI/` 只有 `assumptions.md` (463 bytes, 仅 §9.1 description), **无 spec.md/examples.md**. DI 是 SDTMIG-MD extension (Medical Devices supplementary IG, separate document), 非 SDTMIG v3.4 core domain. Core=Req 变量列在所有 4 平台都不完整 — KNOWN_LIMITATIONS pre-existing gap, 非 v1.4 引入.

## Layer 1 — Prompt fidelity (Claude v3): PASS

- L45 R1 KB-grounding primary
- L47-53 R2 AHP — DI 是 SDTM-shaped 2-char domain code, AHP-V1 fire 触发 KB lookup (然 KB 仅 assumptions.md 微薄)
- 06_assumptions.md routing

Layer 1 PASS — Claude v3 prompt 必把题路由 06_assumptions DI 段.

## Layer 2 — KB reach (Claude current/uploads/): PARTIAL

### Hits
- `06_assumptions.md:330-331`:
```
**DI - Description/Overview (§9.1)**
The DI dataset was introduced as part of the SDTMIG for Medical Devices (SDTMIG-MD).
```
- `03_model.md:85`: "...Device-subject Relationships dataset includes the variable DOMAIN, but other study reference datasets do not" — 提及 "study reference dataset" 概念 (但非 DI 直接绑定)
- 多处 SPDEVID (Sponsor Device Identifier) variable rows in `05_mega_spec.md`

### Miss (关键)
- **"study reference dataset since SDTM v1.7"** 句: 仅 03_model.md:85 提及 "study reference dataset" 概念, **未与 DI 直接 bind**
- DI assumptions paragraph TRUNCATED at L331 — 缺 source KB (`knowledge_base/domains/DI/assumptions.md`) 完整 "It was originally classified as a special-purpose domain, but since SDTM v1.7 it has been classified as a study reference dataset" 句
- Source KB confirm: `knowledge_base/domains/DI/assumptions.md` 全文有此完整句

### Root cause (architectural)
- Source: `knowledge_base/domains/DI/assumptions.md` 全文 463 bytes, 第 2 段完整 4 句
- Pipeline: `extract_examples_data.py` 当 build `06_assumptions.md` 时 DI 段 byte truncated 后接 DV 段 (verified at L333 "<!-- source: knowledge_base/domains/DV/assumptions.md -->")
- 不同于 Q-S1/Q-S2 是 `## §N.N.N` heading capture gap — 这是 paragraph-level truncation, 可能 `extract_examples_data.py` 在 DI assumptions 段处理时遇到 short paragraph 边界 bug

### v1.4 disposition
- v1.4 A3.1 script fix scope: `## §N.N.N` Quick Reference capture
- **此 PARTIAL 的 root cause 不同**: paragraph-level truncation (DI assumptions L2), 非 §N.N.N heading
- A3.1 fix 可能不 cover 此 truncation, 需 Phase C C4 rebuild 时 diff verify; 若 fix scope 不 cover → defer v1.5 explicit pipeline fix
- Bundle rebuild defer Phase C C4

## Verdict: PARTIAL

- Layer 1 PASS
- Layer 2 KB 命中 SDTMIG-MD (✓), 缺 study reference dataset 直接 binding (truncated); Core=Req 变量列 KB pre-existing gap (4 平台同)
- Claude 实际答 (UI-level) 可能 reason 出 "study reference dataset" (via 03_model.md cross-reference) — UI reasoning bridge
- 计 PARTIAL (≥50% 要点 reachable; class binding + Core=Req KB gap)

## v1.4 not-blocked

非 v9 prompt regression. v9 prompt 完整含 R1+R2 AHP. DI 域 Core=Req KB gap 是 pre-existing KNOWN_LIMITATIONS, 非 v1.4 引入.

B1 verdict: APPROVE WITH KNOWN_KB_GAP. KNOWN_LIMITATIONS 三语 §0 加 entry "DI 域 KB only assumptions.md, no spec.md/examples.md — Core=Req variables incomplete across 4 platforms (pre-existing, SDTMIG-MD extension non-core, defer v1.5 OR SDTMIG-MD source ingest)".
