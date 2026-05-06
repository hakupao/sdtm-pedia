# SDTM IG v3.4 Variables - OI Domain

**Domain Code:** `OI`

**Total Variables:** 7

| Variable | Label | Type | Core | Role | Notes |
|---|---|---|---|---|---|
| `STUDYID` | Study Identifier | Char | Req | Identifier | Unique identifier for a study. |
| `DOMAIN` | Domain Abbreviation | Char | Req | Identifier | Two-character abbreviation for the domain. |
| `NHOID` | Non-host Organism Identifier | Char | Req | Identifier | Sponsor-defined identifier for a non-host organism. NHOID should be populated with an intuitive name based on the identity of the organism as reported by the lab. It must be unique for each unique organism as defined by the specific values of the organism's entire known taxonomy described by pairs of OIPARMCD and OIVAL . |
| `OISEQ` | Sequence Number | Num | Req | Identifier | Sequence number to given to ensure uniqueness within a parameter within an organism (NHOID) within dataset. |
| `OIPARMCD` | Non-host Organism ID Element Short Name | Char | Req | Topic | Short name of the taxon being described. Examples: "GROUP", "GENTYP", "SUBTYP". |
| `OIPARM` | Non-host Organism ID Element Name | Char | Req | Synonym Qualifier | Name of the taxon being described. Examples: "Group", "Genotype", "Subtype". |
| `OIVAL` | Non-host Organism ID Element Value | Char | Req | Result Qualifier | Value for the taxon in OIPARMCD/OIPARM for the organism identified by NHOID. |
