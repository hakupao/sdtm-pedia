# Checkpoint: Section 1 — ig34_§2.7

**section_id:** ig34_§2.7  
**section_title:** §2.7 SDTM Variables Not Allowed in the SDTMIG  
**target_file:** knowledge_base/chapters/ch02_fundamentals.md  
**pdf_page_range:** 15–16  
**verdict:** PASS

## Atoms Processed

| atom_id | verdict | fix_applied |
|---------|---------|-------------|
| ig34_p0015_a004 | PARTIAL | Added full step k text including cross-reference to §8.4 and relationship mechanism |
| ig34_p0015_a021 | PARTIAL | Split merged row — RPPLDY now individual entry with (Timing Variables) |
| ig34_p0015_a022 | PARTIAL | Split merged row — RPPLSTDY now individual entry with (Timing Variables) |
| ig34_p0015_a023 | PARTIAL | Split merged row — RPPLENDY now individual entry with (Timing Variables) |
| ig34_p0016_a001 | PARTIAL | Split merged row — --NOMDY now individual entry with (Timing Variables) |
| ig34_p0016_a002 | PARTIAL | Split merged row — --NOMLBL now individual entry with (Timing Variables) |
| ig34_p0016_a003 | PARTIAL | Split merged row — --RPDY now individual entry with (Timing Variables) |
| ig34_p0016_a004 | PARTIAL | Split merged row — --RPSTDY now individual entry with (Timing Variables) |
| ig34_p0016_a005 | PARTIAL | Split merged row — --RPENDY now individual entry with (Timing Variables) |
| ig34_p0016_a010 | PARTIAL | Listed individually as "SPECIES (Demographics)" with category label |
| ig34_p0016_a011 | PARTIAL | Listed individually as "STRAIN (Demographics)" with category label |
| ig34_p0016_a012 | PARTIAL | Listed individually as "SBSTRAIN (Demographics)" with category label |
| ig34_p0016_a013 | PARTIAL | Listed individually as "RPATHCD (Demographics)" with category label |
| ig34_p0016_a018 | PARTIAL | SETCD (Demographics) entry already complete — verified acceptable as-is |
| ig34_p0016_a021 | PARTIAL | POOLID entry already complete — verified acceptable as-is |

**Atoms processed:** 15 PARTIAL  
**KB lines before:** 217 | **KB lines after:** 241 (+24)

## Rule A Spot-Check (N=3)

1. `grep "Section 8.4, Relating Non-standard Variable Values to a Parent Domain"` → MATCH in ch02 step k
2. `grep "RPPLDY"` → MATCH as individual row "| RPPLDY | Timing Variables |"
3. `grep "SPECIES (Demographics)"` → MATCH as individual bullet "- SPECIES (Demographics)"
4. `grep "SBSTRAIN (Demographics)"` → MATCH
5. `grep "--NOMDY"` → MATCH as individual row

**Rule A probe count:** 5/5 PASS  
**TODO markers left:** 0
