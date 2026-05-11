# P4a Forward Matcher Prompt v1.0

> Created: 2026-05-11 (P4a S1 kickoff)
> Purpose: Assign PDF→MD coverage verdicts for one batch of 100 pre-joined atoms
> Agent role: Matcher (writer slot, Rule D P4a)
> Output: evidence/p4a_batches/batch_NNN_ledger.jsonl + trace.jsonl batch_quality_sample

---

## Your Task

You are processing **one batch of 100 PDF atoms** to determine whether each atom's content
appears in the knowledge base (KB) Markdown files.

**Input**: `evidence/p4a_batches/batch_NNN_input.jsonl` — 100 lines, each line has:
- `pdf_atom_id`, `pdf_atom_type`, `pdf_source`, `pdf_page`
- `pdf_parent_section` — which PDF section this atom is from
- `pdf_verbatim` — the exact text from the PDF
- `candidates[]` — up to 5 pre-ranked MD candidates, each with:
  - `md_atom_id`, `md_file`, `md_atom_type`, `md_parent_section`
  - `md_verbatim` — text from the MD file
  - `score` (Jaccard similarity, 0–1)

**Output**: Write `evidence/p4a_batches/batch_NNN_ledger.jsonl` — 100 lines of coverage verdicts.
Then append one `batch_quality_sample` event to `trace.jsonl`.

---

## Verdict Assignment Rules

For each atom, assign exactly one verdict from this enum:

| Verdict | When to use |
|---------|-------------|
| `EXACT` | pdf_verbatim and md_verbatim are character-identical (or differ only in trivial normalization: whitespace, "Required"↔"Req", punctuation) |
| `EQUIVALENT` | Same information, different words. A reader would understand the same thing from both. KB has paraphrased, reformatted, or abbreviated the content correctly. |
| `PARTIAL` | MD covers only part of the PDF content. Example: PDF says "X shall Y when Z, otherwise W" but MD only has "X shall Y" — conditions omitted. |
| `MISPLACED` | Text matches (would be EXACT/EQUIVALENT) BUT `pdf_parent_section` and `md_parent_section` are clearly in different domains/sections. The content is in the KB but under the wrong heading. |
| `MISSING` | None of the 5 candidates contain the PDF atom content. The knowledge base does not have this information. |
| `ERROR` | KB contains an actively wrong value that contradicts the PDF. Not just missing — a factual error (wrong number, wrong domain code, hallucinated rule). |
| `INTENTIONAL_EXCLUDE` | Pre-approved exclusion — see §4 below. |

**Decision flowchart:**
1. Is `pdf_parent_section` a pre-approved exclusion category? → `INTENTIONAL_EXCLUDE` (§4)
2. Check candidates in score order. Does the top-1 (or any candidate) contain the PDF content?
   - Yes, verbatim/trivially → `EXACT`
   - Yes, paraphrased → `EQUIVALENT` (check parent section alignment → else `MISPLACED`)
   - Yes, partially → `PARTIAL`
   - Candidate contradicts PDF → `ERROR`
   - No candidate matches → `MISSING`

---

## §1 Matching Criteria Detail

### EXACT threshold
`score >= 0.85` AND verbatim text is essentially the same (minor whitespace/punctuation).
Use judgment — score is a heuristic, not the rule.

### EQUIVALENT threshold
Content is the same. Check: "Would a domain expert reading the MD entry understand the
same fact/rule as the PDF original?" If yes → EQUIVALENT.
Don't penalize for:
- Abbreviating "not applicable" → "N/A"
- Removing parenthetical context that's covered elsewhere in the file
- Standard domain terminology reformatting

Do NOT call EQUIVALENT if the MD is missing material conditions (→ PARTIAL).

### PARTIAL indicators
- PDF atom has 3 sub-conditions; MD covers 1-2
- PDF sentence has a "shall not ... unless ..." clause; MD drops the exception
- PDF lists 5 items; MD has 3

### MISPLACED detection (mandatory)
When a candidate looks EXACT/EQUIVALENT, check:
- `pdf_parent_section` domain code (e.g., "§5.2 DM" → domain "DM")
- `md_parent_section` domain code (e.g., "§AE.1" → domain "AE")
- If domain codes clearly differ → `MISPLACED`
- If sections are in different chapters (e.g., §4 vs §8) but same topic → use judgment

### MISSING: default for low-score cases
If `score < 0.35` for ALL candidates AND the verbatim content is substantive (not
EDITORIAL_META), default verdict is `MISSING` unless a candidate clearly contains
a paraphrase that escaped the token-based scoring.

### ERROR: use sparingly
Only when MD makes a factually wrong statement. Not for omissions. When in doubt
between PARTIAL and ERROR, use PARTIAL.

---

## §2 Atom-type Specific Notes

**HEADING**: Usually `EXACT` or `EQUIVALENT` if the KB has the corresponding section
heading. `MISSING` if the section is absent from the KB entirely.

**TABLE_ROW / TABLE_HEADER**: Compare cell-by-cell. EXACT if table content matches
verbatim. EQUIVALENT if same data with different formatting. PARTIAL if some columns
are present but others absent.

**CODE_LITERAL**: Must be character-exact. Any difference → `PARTIAL` or `ERROR`.
Controlled terminology codes (e.g., `C66742`) must match exactly.

**CROSS_REF**: A cross-reference like "See §4.2.1" is in the KB only if the KB has
a corresponding pointer. If the KB integrates the referenced content inline instead
of linking, verdict = `EQUIVALENT`. If missing entirely → `MISSING`.

**FIGURE**: Only first 200 chars of verbatim are provided (see `[TRUNCATED:FIGURE]`
marker). Match on the available text + figure_ref anchor. If the KB has a Mermaid
diagram covering the same concept → `EQUIVALENT`. If no diagram → `MISSING`.

**NOTE**: Notes/warnings often paraphrased in KB. EQUIVALENT is common.
MISSING if the note content is not reflected anywhere in the MD.

**LIST_ITEM**: Each list item is one atom. Match individually against candidates.

---

## §3 MISPLACED Output Format

When verdict = `MISPLACED`, set `discrepancy` field:
```
"MISPLACED: pdf §<pdf_parent_section> vs md §<md_parent_section>"
```
Example: `"MISPLACED: pdf §5.2 DM vs md §AE.1 [Adverse Events]"`

---

## §4 INTENTIONAL_EXCLUDE (Pre-approved Categories)

You MAY auto-classify as `INTENTIONAL_EXCLUDE` WITHOUT user confirmation for:

| Category | Pattern | Example |
|----------|---------|---------|
| `EDITORIAL_META` | `pdf_parent_section` starts with `§0` (Cover page, Table of Contents, copyright notices, revision history) | `§0 [Cover]`, `§0 [Table of Contents]` |
| `EDITORIAL_META` | Version statement atoms: "Version X.Y (Final)", "Effective Date:", "Copyright" | Any page |
| `VERSION_MISMATCH` | Atoms from `pdf_source=SDTM_v2.0` covering content that SDTMIG v3.4 explicitly supersedes | sv20 atoms when ig34 has the same rule |

For `INTENTIONAL_EXCLUDE`, fill:
```json
"exclusion_reason": "<why this content is excluded from KB>",
"category": "EDITORIAL_META|VERSION_MISMATCH",
"approved_by": "pre-approved-category"
```

Do NOT auto-classify as `INTENTIONAL_EXCLUDE` for:
- `REDUNDANT_WITH_SPEC` (requires user ack)
- `FIGURE_ALREADY_CONVERTED` (requires user ack)
- Any substantive content you're unsure about (→ use `MISSING` or `PARTIAL` instead)

---

## §5 Output Format

Each line of `evidence/p4a_batches/batch_NNN_ledger.jsonl`:

```jsonc
{
  "pdf_atom_id": "ig34_p0001_a001",
  "md_atom_ids": ["md_ch01_a003"],      // empty array [] if MISSING/INTENTIONAL_EXCLUDE
  "verdict": "EQUIVALENT",
  "similarity_score": 0.82,             // top-1 candidate score; null if MISSING/INTENTIONAL_EXCLUDE
  "discrepancy": null,                  // string for PARTIAL/MISPLACED/ERROR; null otherwise
  "exclusion_reason": null,             // string for INTENTIONAL_EXCLUDE only
  "category": null,                     // "EDITORIAL_META"|"VERSION_MISMATCH"|null
  "approved_by": null,                  // "pre-approved-category" for INTENTIONAL_EXCLUDE
  "matched_by": {
    "subagent_type": "oh-my-claudecode:executor",
    "batch_id": "batch_NNN",
    "prompt_version": "P4a_forward_matcher_v1.0",
    "ts": "<ISO8601 timestamp>"
  }
}
```

**Rules:**
- One line per atom, in the SAME ORDER as the input file
- ALL 100 atoms must have an entry (no skips)
- `md_atom_ids`: use the BEST matching candidate's `md_atom_id`; `[]` if no match
- `similarity_score`: use top-1 candidate score from input; `null` if MISSING/INTENTIONAL_EXCLUDE
- Use proper JSON (double quotes, no trailing commas)

---

## §6 Batch Quality Sample (trace.jsonl)

After writing all 100 ledger entries, append ONE line to `trace.jsonl`:

```jsonc
{
  "ts": "<ISO8601>",
  "phase": "P4a",
  "slot": "batch_quality_sample",
  "batch_id": "batch_NNN",
  "subagent_type": "oh-my-claudecode:executor",
  "prompt_version": "P4a_forward_matcher_v1.0",
  "stats": {
    "total": 100,
    "EXACT": <count>,
    "EQUIVALENT": <count>,
    "PARTIAL": <count>,
    "MISPLACED": <count>,
    "MISSING": <count>,
    "ERROR": <count>,
    "INTENTIONAL_EXCLUDE": <count>
  },
  "samples": [
    // 5 representative atoms (pick: 1 EXACT, 1 EQUIVALENT or PARTIAL, 1 MISSING, 2 others)
    {"pdf_atom_id": "...", "verdict": "...", "top1_score": 0.0}
  ]
}
```

---

## §7 Execution Steps

1. Read `evidence/p4a_batches/batch_NNN_input.jsonl` (all 100 lines)
2. For each atom, apply verdict rules (§1-§4)
3. Write all 100 ledger entries to `evidence/p4a_batches/batch_NNN_ledger.jsonl`
   (create new file, do NOT append to an existing ledger — this is a fresh batch)
4. Append batch_quality_sample to `trace.jsonl`
5. Print a 3-line summary: batch_id / total atoms / verdict distribution

---

## §8 Hard Stops

Stop and report (do NOT write partial output) if:
- The input file has fewer than expected atoms (file corruption)
- More than 20% of atoms would be `ERROR` (systematic prompt issue, not organic)
- You are unsure about a verdict AND it involves `shall`/`must`/`required` language
  → prefer `PARTIAL` over `EQUIVALENT`, and note the uncertainty in `discrepancy`
