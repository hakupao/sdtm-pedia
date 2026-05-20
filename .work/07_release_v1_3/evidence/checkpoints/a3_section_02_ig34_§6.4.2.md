# Checkpoint: Section 2 — ig34_§6.4.2

**section_id:** ig34_§6.4.2  
**section_title:** §6.4.2 Naming Findings About Domains  
**target_file:** knowledge_base/chapters/ch02_fundamentals.md  
**pdf_page_range:** 363–364  
**verdict:** PASS

## Atoms Processed

| atom_id | verdict | fix_applied |
|---------|---------|-------------|
| ig34_p0363_a006 | PARTIAL | Added disease milestone/RELMIDS guidance: "If the event or intervention is a disease milestone, then RELMIDS is not included in this event or intervention record. Is the relationship of a data item to the disease milestone (RELMIDS) needed? If so, it can be represented in FA, but not as a supplemental qualifier to the parent record." |
| ig34_p0363_a014 | PARTIAL | Added full split FA guidance items: DOMAIN="FA", prefix="FA", dataset naming (FACE/FAMH), FASEQ uniqueness, SUPP naming, RELREC 4-char rule |
| ig34_p0364_a003 | PARTIAL | Added "The DOMAIN value is sponsor-defined and does not begin with FA, following examples in Section 6.4.5, Skin Response, which has a domain code of SR." |
| ig34_p0364_a011 | PARTIAL (also §6.4.3) | Fixed in 02_observation_classes.md (see Section 8) |

**Atoms processed:** 4 PARTIAL  
**KB lines before:** 217 | **KB lines after:** 241 (+24, shared with §2.7 edits)

## Rule A Spot-Check (N=3)

1. `grep "RELMIDS"` in ch02 → MATCH: "RELMIDS is not included in this event or intervention record"
2. `grep "FASEQ must be unique within USUBJID"` in ch02 → MATCH
3. `grep "does not begin with FA"` in ch02 → MATCH: "The DOMAIN value is sponsor-defined and does not begin with FA"

**Rule A probe count:** 3/3 PASS  
**TODO markers left:** 0
