# Checkpoint: Section 7 — ig34_§6.3.12.2

**section_id:** ig34_§6.3.12.2  
**section_title:** §6.3.12.2 Tumor/Lesion Results (TR)  
**target_file:** knowledge_base/domains/TR/assumptions.md (not examples.md)  
**pdf_page_range:** 350–352  
**verdict:** PASS

## Atoms Processed

| atom_id | verdict | fix_applied |
|---------|---------|-------------|
| ig34_p0352_a008 | PARTIAL | Fixed column header error in TR/assumptions.md assumption 4 table: last column was "TRSTRESN" (duplicate) but should be "TRSTRESU". PDF verbatim: "TRLNKID | TRTESTCD | TRTEST | TRORRES | TRORRESU | TRSTRESC | TRSTRESN | TRSTRESU" |

**Note:** The section_coverage md_target_files lists TR/examples.md, but the actual error was found in TR/assumptions.md where the spec example table has a column header typo. The examples.md table headers (TRSTRESN | TRSTRESU) are correct.

**Atoms processed:** 1 PARTIAL  
**KB lines delta:** TR/assumptions.md line 15: "TRSTRESN" → "TRSTRESU" (last column header)

## Rule A Spot-Check (N=1)

1. `grep "TRSTRESU"` in TR/assumptions.md → MATCH: "| TRLNKID | TRTESTCD | TRTEST | TRORRES | TRORRESU | TRSTRESC | TRSTRESN | TRSTRESU |"

**Rule A probe count:** 1/1 PASS  
**TODO markers left:** 0
