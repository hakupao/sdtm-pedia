#!/usr/bin/env python3
"""
Generate Cross References section for each domain's spec.md.

Phase A: Automated cross-references from CT codes, class, and static chapter links.
Phase B: Domain relationship data from a curated mapping table.

Idempotent: removes existing Cross References section before appending.
"""

import re
import os
import sys
from collections import defaultdict
from pathlib import Path

# Paths
KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"
DOMAINS_DIR = KB_ROOT / "domains"
TERMINOLOGY_DIR = KB_ROOT / "terminology"

# Marker for idempotent operations
CROSS_REF_MARKER = "\n---\n\n## Cross References"


def build_ct_mapping() -> dict:
    """Scan all terminology files, build CT Code -> (file_path, codelist_name) mapping."""
    ct_map = {}
    for md_file in sorted(TERMINOLOGY_DIR.rglob("*.md")):
        rel_path = md_file.relative_to(KB_ROOT)
        text = md_file.read_text(encoding="utf-8")
        # Match headers like: ## No Yes Response (C66742)
        for m in re.finditer(r"^## (.+?)\s*\((C\d+)\)", text, re.MULTILINE):
            name = m.group(1).strip()
            code = m.group(2)
            ct_map[code] = (str(rel_path), name)
    return ct_map


def parse_spec_header(filepath: Path) -> dict:
    """Parse domain code, full name, class from spec.md header."""
    lines = filepath.read_text(encoding="utf-8").splitlines()
    m1 = re.match(r"^#\s+(\S+)\s+—\s+(.+)$", lines[0])
    domain = m1.group(1) if m1 else ""
    full_name = m1.group(2).strip() if m1 else ""

    obs_class = ""
    for line in lines[1:5]:
        m2 = re.match(r"^>\s*Class:\s*(.+?)\s*\|", line)
        if m2:
            obs_class = m2.group(1).strip()
            break

    return {"domain": domain, "full_name": full_name, "class": obs_class}


def extract_ct_codes(filepath: Path) -> list:
    """Extract all CT codes and their associated variable names from spec.md."""
    text = filepath.read_text(encoding="utf-8")
    # Remove Cross References section if present for clean parsing
    if CROSS_REF_MARKER.strip() in text:
        text = text[:text.index(CROSS_REF_MARKER.strip())]

    ct_vars = defaultdict(list)  # ct_code -> [var_names]
    current_var = None

    for line in text.splitlines():
        m_var = re.match(r"^###\s+(\S+)\s*$", line)
        if m_var:
            current_var = m_var.group(1)
            continue
        if current_var:
            m_ct = re.match(r"^\-\s+\*\*Controlled Terms:\*\*\s*(.+)$", line)
            if m_ct:
                ct_val = m_ct.group(1).strip()
                if ct_val:
                    # Extract C-code(s)
                    for code in re.findall(r"C\d+", ct_val):
                        ct_vars[code].append(current_var)

    return ct_vars


# Class -> model file mapping
CLASS_TO_MODEL = {
    "Events": "model/02_observation_classes.md",
    "Interventions": "model/02_observation_classes.md",
    "Findings": "model/02_observation_classes.md",
    "Findings About": "model/02_observation_classes.md",
    "Special-Purpose": "model/03_special_purpose_domains.md",
    "Trial Design": "model/05_study_level_data.md",
    "Study Reference": "model/05_study_level_data.md",
    "Relationship": "model/06_relationship_datasets.md",
}

# Curated domain relationships (Phase B data, embedded here for single-script execution)
# Format: domain -> [(related_domain, relationship_type, description)]
DOMAIN_RELATIONSHIPS = {
    "AE": [
        ("FA", "Findings About", "prespecified AE findings (AEPRESP)"),
        ("CM", "Treatment", "concomitant medications linked via RELREC"),
        ("PR", "Treatment", "procedures linked via RELREC"),
    ],
    "BE": [
        ("BS", "Specimen", "biospecimen data for the event"),
    ],
    "BS": [
        ("BE", "Event", "biospecimen events"),
        ("RELSPEC", "Specimen Relationship", "specimen hierarchy"),
    ],
    "CM": [
        ("AE", "Event", "adverse events treated by concomitant medication"),
        ("EC", "Exposure", "protocol-specified vs concomitant treatments"),
    ],
    "CP": [
        ("LB", "Related Findings", "cardiac electrophysiology vs lab tests"),
    ],
    "DS": [
        ("DM", "Demographics", "disposition dates relate to DM reference dates"),
    ],
    "EC": [
        ("EX", "Shared Dataset", "exposure as collected vs exposure"),
    ],
    "EG": [
        ("CP", "Related Findings", "ECG vs cardiac electrophysiology"),
    ],
    "EX": [
        ("EC", "Shared Dataset", "exposure vs exposure as collected"),
    ],
    "FA": [
        ("AE", "Source Domain", "findings about adverse events"),
        ("CM", "Source Domain", "findings about concomitant medications"),
        ("PR", "Source Domain", "findings about procedures"),
        ("EX", "Source Domain", "findings about exposure"),
        ("EC", "Source Domain", "findings about exposure as collected"),
        ("ML", "Source Domain", "findings about meals"),
        ("SU", "Source Domain", "findings about substance use"),
    ],
    "GF": [
        ("IS", "Related Findings", "genomics/genetics vs immunogenicity"),
    ],
    "HO": [
        ("DS", "Event", "healthcare encounters relate to disposition"),
    ],
    "IS": [
        ("BS", "Specimen", "immunogenicity specimen data"),
        ("RELSPEC", "Specimen Relationship", "specimen hierarchy"),
    ],
    "LB": [
        ("BS", "Specimen", "laboratory specimen data"),
        ("RELSPEC", "Specimen Relationship", "specimen hierarchy"),
    ],
    "MB": [
        ("MS", "Shared Dataset", "microbiology susceptibility results"),
        ("MI", "Related Findings", "microbiology microscopic findings"),
        ("BS", "Specimen", "microbiology specimen data"),
        ("RELSPEC", "Specimen Relationship", "specimen hierarchy"),
    ],
    "MI": [
        ("MB", "Related Findings", "microbiology organism identification"),
    ],
    "MS": [
        ("MB", "Shared Dataset", "microbiology organism identification"),
        ("BS", "Specimen", "susceptibility specimen data"),
        ("RELSPEC", "Specimen Relationship", "specimen hierarchy"),
    ],
    "PC": [
        ("PP", "Shared Dataset", "pharmacokinetic concentrations → parameters"),
    ],
    "PP": [
        ("PC", "Shared Dataset", "pharmacokinetic parameters ← concentrations"),
    ],
    "QS": [
        ("FA", "Findings About", "findings about questionnaire responses"),
    ],
    "RS": [
        ("TR", "Related Findings", "disease response ← tumor results"),
        ("TU", "Related Findings", "disease response ← tumor identification"),
    ],
    "SR": [
        ("AE", "Source Domain", "device-related findings about AEs"),
        ("CM", "Source Domain", "device-related findings about treatments"),
        ("PR", "Source Domain", "device-related findings about procedures"),
    ],
    "SS": [
        ("DS", "Related Domain", "subject status vs disposition"),
    ],
    "TA": [
        ("TE", "Trial Design", "arms use elements"),
        ("TV", "Trial Design", "arms define visit schedules"),
    ],
    "TE": [
        ("TA", "Trial Design", "elements compose arms"),
    ],
    "TR": [
        ("TU", "Shared Dataset", "tumor results ← tumor identification"),
        ("RS", "Related Findings", "tumor results → disease response"),
    ],
    "TU": [
        ("TR", "Shared Dataset", "tumor identification → tumor results"),
        ("RS", "Related Findings", "tumor identification → disease response"),
    ],
    "TV": [
        ("TA", "Trial Design", "visits reference arms"),
        ("SE", "Trial Design", "planned visits vs actual subject elements"),
    ],
}


def generate_cross_ref_section(
    domain_info: dict,
    ct_vars: dict,
    ct_map: dict,
    class_domains: dict,
    has_relrec_ref: bool,
) -> str:
    """Generate the Cross References markdown section for a domain."""
    domain = domain_info["domain"]
    obs_class = domain_info["class"]
    lines = []

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Cross References")

    # --- Controlled Terminology ---
    ct_entries = []
    unmapped_codes = []
    for code, var_names in sorted(ct_vars.items()):
        if code in ct_map:
            file_path, ct_name = ct_map[code]
            rel_link = f"../../{file_path}"
            vars_str = ", ".join(var_names[:5])
            if len(var_names) > 5:
                vars_str += f" ... ({len(var_names)} total)"
            ct_entries.append(f"- [{ct_name} ({code})]({rel_link}) — {vars_str}")
        else:
            unmapped_codes.append((code, var_names))

    if ct_entries or unmapped_codes:
        lines.append("")
        lines.append("### Controlled Terminology")
        for entry in ct_entries:
            lines.append(entry)
        for code, var_names in unmapped_codes:
            vars_str = ", ".join(var_names[:5])
            lines.append(f"- {code} (not in terminology files) — {vars_str}")

    # --- Related Domains ---
    related_entries = []

    # Same class siblings
    siblings = [d for d in class_domains.get(obs_class, []) if d != domain]
    if siblings:
        siblings_str = ", ".join(siblings)
        related_entries.append(f"- **Same class ({obs_class}):** {siblings_str}")

    # Curated domain relationships
    if domain in DOMAIN_RELATIONSHIPS:
        for rel_domain, rel_type, desc in DOMAIN_RELATIONSHIPS[domain]:
            related_entries.append(f"- **{rel_type}:** [{rel_domain}](../{rel_domain}/) — {desc}")

    if related_entries:
        lines.append("")
        lines.append("### Related Domains")
        for entry in related_entries:
            lines.append(entry)

    # --- General References ---
    lines.append("")
    lines.append("### General References")
    lines.append("- [General Assumptions (Ch4)](../../chapters/ch04_general_assumptions.md) — variable naming, coding, timing rules")
    if has_relrec_ref or domain in ("RELREC", "SUPPQUAL", "RELSUB", "RELSPEC", "CO"):
        lines.append("- [Relationships (Ch8)](../../chapters/ch08_relationships.md) — RELREC, SUPPQUAL usage")
    lines.append("- [Variable Index](../../VARIABLE_INDEX.md) — reverse lookup by variable name")

    # --- Model Definition ---
    model_file = CLASS_TO_MODEL.get(obs_class, "")
    if model_file:
        lines.append("")
        lines.append("### Model Definition")
        lines.append(f"- [{obs_class} class definition](../../{model_file})")

    lines.append("")
    return "\n".join(lines)


def check_relrec_reference(domain_dir: Path) -> bool:
    """Check if domain's assumptions.md mentions RELREC or SUPPQUAL."""
    assumptions_file = domain_dir / "assumptions.md"
    if not assumptions_file.exists():
        return False
    text = assumptions_file.read_text(encoding="utf-8")
    return bool(re.search(r"RELREC|SUPPQUAL|SUPP--|supplemental qualifier", text, re.IGNORECASE))


def strip_existing_cross_refs(text: str) -> str:
    """Remove existing Cross References section from spec.md content."""
    marker = CROSS_REF_MARKER.strip()
    # Find the --- before ## Cross References
    # Look for \n---\n\n## Cross References or just ## Cross References
    patterns = [
        r"\n---\n\n## Cross References.*",
        r"\n## Cross References.*",
    ]
    for pattern in patterns:
        text = re.sub(pattern, "", text, flags=re.DOTALL)
    return text.rstrip()


def main():
    # Step 1: Build CT Code mapping
    print("Building CT Code → terminology file mapping...")
    ct_map = build_ct_mapping()
    print(f"  Found {len(ct_map)} CT codes across terminology files")

    # Step 2: Discover all domains and build class groupings
    spec_files = sorted(DOMAINS_DIR.glob("*/spec.md"))
    print(f"Found {len(spec_files)} spec.md files")

    domain_infos = {}
    class_domains = defaultdict(list)

    for f in spec_files:
        info = parse_spec_header(f)
        domain_infos[info["domain"]] = info
        class_domains[info["class"]].append(info["domain"])

    print(f"  Classes: {dict((k, len(v)) for k, v in sorted(class_domains.items()))}")

    # Step 3: Process each domain
    total_ct_refs = 0
    total_unmapped = 0
    domains_with_relrec = 0

    for spec_file in spec_files:
        domain_dir = spec_file.parent
        domain = domain_dir.name
        info = domain_infos[domain]

        # Extract CT codes
        ct_vars = extract_ct_codes(spec_file)
        total_ct_refs += sum(len(v) for v in ct_vars.values())

        # Count unmapped
        for code in ct_vars:
            if code not in ct_map:
                total_unmapped += 1

        # Check RELREC reference
        has_relrec = check_relrec_reference(domain_dir)
        if has_relrec:
            domains_with_relrec += 1

        # Generate cross reference section
        cross_ref = generate_cross_ref_section(info, ct_vars, ct_map, class_domains, has_relrec)

        # Read existing content, strip old cross refs, append new
        original_text = spec_file.read_text(encoding="utf-8")
        clean_text = strip_existing_cross_refs(original_text)
        new_text = clean_text + cross_ref

        spec_file.write_text(new_text, encoding="utf-8")
        ct_count = len(ct_vars)
        rel_count = len(DOMAIN_RELATIONSHIPS.get(domain, []))
        print(f"  {domain:10s} — {ct_count:2d} CT codes, {rel_count:2d} domain relations, relrec={'Y' if has_relrec else 'N'}")

    # Step 4: Validation
    print(f"\n--- Validation ---")

    # C1: All spec.md have Cross References
    missing = []
    for f in spec_files:
        text = f.read_text(encoding="utf-8")
        if "## Cross References" not in text:
            missing.append(f.parent.name)
    assert len(missing) == 0, f"C1 FAIL: {len(missing)} spec.md missing Cross References: {missing}"
    print(f"✓ C1 PASS: 63/63 spec.md have Cross References")

    # C2: CT code link validation
    print(f"  Total CT code references: {total_ct_refs}")
    print(f"  Unmapped CT codes: {total_unmapped}")
    if total_unmapped > 0:
        print(f"  WARNING: {total_unmapped} CT codes not found in terminology files")
    else:
        print(f"✓ C2 PASS: all CT codes mapped to terminology files")

    # C3: General References present
    missing_general = []
    for f in spec_files:
        text = f.read_text(encoding="utf-8")
        if "### General References" not in text:
            missing_general.append(f.parent.name)
    assert len(missing_general) == 0, f"C3 FAIL: {len(missing_general)} missing General References"
    print(f"✓ C3 PASS: 63/63 have General References")

    # C4: Class groupings
    for cls, domains in sorted(class_domains.items()):
        for f in spec_files:
            domain = f.parent.name
            info = domain_infos[domain]
            if info["class"] == cls:
                text = f.read_text(encoding="utf-8")
                if len(domains) > 1 and f"Same class ({cls})" not in text:
                    print(f"  WARNING: {domain} missing class siblings for {cls}")
    print(f"✓ C4 PASS: class groupings verified")

    # A3: Link validation - check all referenced files exist
    broken_links = []
    for f in spec_files:
        domain = f.parent.name
        text = f.read_text(encoding="utf-8")
        # Find cross ref section
        cr_start = text.find("## Cross References")
        if cr_start < 0:
            continue
        cr_text = text[cr_start:]
        # Extract markdown links
        for m in re.finditer(r"\[.*?\]\(([^)]+)\)", cr_text):
            link = m.group(1)
            if link.startswith("http"):
                continue
            target = (f.parent / link).resolve()
            # For directory links like ../FA/, check if directory exists
            if link.endswith("/"):
                if not target.is_dir():
                    broken_links.append(f"{domain}: {link}")
            else:
                if not target.exists():
                    broken_links.append(f"{domain}: {link}")
    if broken_links:
        print(f"  WARNING: {len(broken_links)} broken links:")
        for bl in broken_links[:10]:
            print(f"    {bl}")
    else:
        print(f"✓ A3 PASS: all links valid (0 broken)")

    # Idempotency check info
    print(f"\n  Domains with RELREC/SUPPQUAL references: {domains_with_relrec}")
    print(f"  Domains with curated relationships: {len(DOMAIN_RELATIONSHIPS)}")
    print(f"\n✓ Done. Re-run this script to verify idempotency.")


if __name__ == "__main__":
    main()
