# RELSPEC — Examples

## Example 1

This example uses the sample specimen lineage illustrated below.

**Specimen Relationship Diagram:**

```mermaid
graph TD
    subgraph L1["Level 1 — Originally Collected Specimen"]
        SPC001["SPC-001<br/>(Tissue)"]
        SPC003["SPC-003<br/>(Brain)"]
    end
    subgraph L2["Level 2 — Child Specimen"]
        SPC001A["SPC-001-A<br/>(Tissue)"]
        SPC001B["SPC-001-B<br/>(Tissue)"]
        SPC003A["SPC-003-A<br/>(RNA)"]
    end
    subgraph L3["Level 3 — Child Specimen"]
        SPC001B1["SPC-001-B-1<br/>(DNA)"]
    end
    SPC001 --> SPC001A
    SPC001 --> SPC001B
    SPC001B --> SPC001B1
    SPC003 --> SPC003A

    style SPC001 fill:#b3d4fc,stroke:#333
    style SPC003 fill:#b3d4fc,stroke:#333
    style SPC001A fill:#b3d4fc,stroke:#333
    style SPC001B fill:#b3d4fc,stroke:#333
    style SPC003A fill:#b3d4fc,stroke:#333
    style SPC001B1 fill:#b3d4fc,stroke:#333
```

A specimen with a LEVEL value of "1" and a blank value for PARENT indicates a collected sample. All other values represent a derived sample. SPEC reflects the specimen type for the sample regardless of whether it is collected or derived.

**relspec.xpt**

| Row | STUDYID | USUBJID | REFID | SPEC | PARENT | LEVEL |
|-----|---------|---------|-------|------|--------|-------|
| 1 | ABC-123 | 001-01 | SPC-001 | TISSUE | | 1 |
| 2 | ABC-123 | 001-01 | SPC-001-A | TISSUE | SPC-001 | 2 |
| 3 | ABC-123 | 001-01 | SPC-001-B | TISSUE | SPC-001 | 2 |
| 4 | ABC-123 | 001-01 | SPC-001-B-1 | DNA | SPC-001-B | 3 |
| 5 | ABC-123 | 001-01 | SPC-003 | TISSUE | | 1 |
| 6 | ABC-123 | 001-01 | SPC-003-A | RNA | SPC-003 | 2 |
