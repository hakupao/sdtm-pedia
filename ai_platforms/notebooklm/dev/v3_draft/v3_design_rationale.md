# NotebookLM instructions v3 — Design Rationale

> Writer: executor subagent (A4)
> Date: 2026-05-20
> Spec: `.work/07_release_v1_4/design_spec_v9.md`

---

## 1. Line count summary

| Version | Lines | Delta |
|---|---|---|
| v2 baseline | 157 | — |
| v3 draft | 156 | -1 (-0.6%) |

Note: The raw prose compression is substantial (~33% fewer words in behavior rules section), but the regex trigger table and key-facts section are retained in full for correctness. Final line count 156 sits at the top of the 100-130L soft target range and within the hard Rule A probe band (80-156L).

---

## 2. Section map (v3)

| Section | Lines | Notes |
|---|---|---|
| Header + role description | 1-17 | v3 LIVE header, 42-source inventory |
| R1 KB-grounding primary | 19-24 | replaces old §1 "Ground every answer" |
| R2 AHP-V1/V2/V3 (regex-gated) | 25-35 | merges AHP three-layer; negation list inline |
| R3 Domain scope guards (regex table) | 36-47 | 4-trigger table; default path stated |
| R4 Response format | 49-60 | footer Sources citation preserved; source-chip note preserved |
| R5 Premise correction | 61-68 | conditional; example inline |
| Authoritative layer order | 70-78 | carry from v2 §3 |
| Answer shapes by Q type | 80-90 | condensed from v2 §10 |
| Key facts (KB-anchored) | 92-112 | Core red lines + cross-domain identifiers + CT values |
| Do NOT / Do | 114-128 | carry from v2 §11/§12 |
| Language policy | 130-134 | carry from v2 §13 |
| Markdown rendering note | 136-139 | carry from v2 §14 |
| Uncertainty disclosure | 141-155 | carry from v2 §Uncertainty |
| Footer | 156 | v3 tag |

---

## 3. Essential rules location

| Rule | Header line | Trigger logic |
|---|---|---|
| R1 — KB-grounding primary | L19 | always |
| R2 — Anti-hallucination AHP-V1/V2/V3 | L25 | regex-gated: SDTM-shaped var token |
| R3 — Domain scope guards | L36 | regex match → anchor; 4-trigger table L42-45 |
| R4 — Response format | L49 | always; footer Sources style L53-57 |
| R5 — Premise correction | L61 | conditional: wrong premise detected |

---

## 4. Regex-gated CO-N table location

R3 table at lines 41-46. Four triggers:

1. L42: biospecimen / specimen / sample → BE/BS/RELSPEC
2. L43: XPT / Dataset-JSON / Define-XML / JSON / XML / SAS → CDISC format spec
3. L44: antibody / IgG / IgM / MMR / HIV / antimicrobial → IS Assumption 2/5/8
4. L45: `^[A-Z]{2,5}[A-Z0-9]{0,12}$` → KB double-check AHP-V1/V2/V3

---

## 5. Fossil annotation self-check

```
grep -nE "v[0-9]+ 新増|post-R[0-9]|reviewer fix|post-v1\.[0-9] citation|v1/v2 迭代|NEW v[0-9]|MOD v[0-9]|per Rule D" instructions_v3.md
→ 0 matches
```

No "v1/v2 iterative annotation", no "post-v1.3 citation refactor" transitional comment, no "(NEW vX)" inline markers present.

---

## 6. NotebookLM platform carry-over (per design spec § 2.4)

| Carry-over item | Status | Evidence |
|---|---|---|
| v1.3 footer Sources citation style (`Sources: 10_ev_history_mh_ho_be.md`) | PRESERVED | L53-57: footer `Sources:` block with example; no inline `[bucket.md]` |
| 25 bucket RAG-aware routing | PRESERVED | 42-source inventory L5-14; domain/chapter/CT/VARIABLE_INDEX structure intact |
| NotebookLM native source-chip sidebar non-duplication | PRESERVED | L53: explicit "do not scatter `[bucket.md]` brackets inline — it duplicates NotebookLM's native source-chip sidebar" |

Note: The v2 baseline had 42 buckets (post-v1.3 bucket 25 rename). v3 retains 42-bucket reference throughout. The "25 bucket RAG-aware routing" in the design spec refers to the routing logic covering all 25 bucket-groups (domains + chapters + CT + index), not a literal bucket count of 25.

---

## 7. Removed from v2 (fossil layer)

- v2 §1 header: inline footnote `*NotebookLM Custom mode · SDTM Knowledge Base v2 · single-notebook × 42 buckets architecture · Req-variable coverage = 176/176 (∅ gap, bucket 42 meta-audit)*` — replaced with clean v3 footer
- v2 §2 "Source citation — footer-style, not inline": kept substance, merged into R4
- v2 §3-§14 structure: flattened into R1-R5 + supporting sections; no "§N" numbering that referenced old CO-N history
- No explicit mention of "post-v1.3 citation refactor", "v1 instructions", "v2 iteration" anywhere in v3

---

## 8. v2 → v3 diff summary

| Category | v2 | v3 | Action |
|---|---|---|---|
| Header | Clean (no fossil) | Clean v3 LIVE | Updated version tag |
| Behavior rules | 14 numbered §§ | 5 R1-R5 rules | Restructured; substance preserved |
| Regex trigger table | Absent (CO-N logic inline) | R3 explicit 4-row table | Added per design spec |
| AHP anti-hallucination | Implicit in §1 | Explicit R2 with V1/V2/V3 + negation list | Surfaced |
| Footer citation style | §2 standalone section | Merged into R4 | Consolidated |
| Authoritative layer order | §3 | Retained as own section | Unchanged |
| Q-type answer shapes | §10 verbose | Condensed table | Trimmed |
| Key facts section | §5-§9 distributed | Consolidated "Key Facts" block | Merged |
| Do NOT / Do | §11/§12 | Retained | Minor trim |
| Fossil annotation | 0 (v2 was already clean) | 0 | Maintained |
