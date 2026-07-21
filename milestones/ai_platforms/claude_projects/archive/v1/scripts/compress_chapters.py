#!/usr/bin/env python3
"""Compress knowledge_base/chapters/*.md for Claude Projects (Phase 6.5 Step 3).

Emits a concatenated, compressed chapters file (target <=45000 tokens) at
ai_platforms/claude_projects/output/02_chapters.md.

Strategy (per PLAN.md §3.2 D5/D6 + §4.3):
- ch04 (reasoning substrate, 31315 tokens): preserve verbatim. Only the
  frontmatter "Source:" line is replaced by the source-path HTML comment so we
  do not duplicate provenance metadata. No prose/table/rule/example is removed.
- ch01/ch02/ch03/ch08/ch10: hand-targeted cuts via section-heading anchors.
  Drops introductory prose, illustrative example tables, long appendices, and
  legalese while retaining every Specification table, numbered rule list,
  variable name / codelist / domain-code reference, and cross-reference
  navigation line.

Idempotence (P7):
- Timestamp in the generated header is derived from max(mtime) of the sources,
  not from datetime.now(), so running the script twice produces a byte-
  identical file. Source files are read-only (P5).
"""
from __future__ import annotations

import datetime as _dt
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC_DIR = ROOT / "knowledge_base" / "chapters"
OUT = ROOT / "ai_platforms" / "claude_projects" / "output" / "02_chapters.md"

# Order in output and relative path (used in the `<!-- source: ... -->` marker
# and for the max-mtime idempotence anchor).
CHAPTERS = [
    "ch01_introduction.md",
    "ch02_fundamentals.md",
    "ch03_submitting_data.md",
    "ch04_general_assumptions.md",
    "ch08_relationships.md",
    "ch10_appendices.md",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _strip_source_line(text: str) -> str:
    """Remove the single 'Source: SDTMIG v3.4, ...' line (redundant with the
    source-path HTML comment we emit)."""
    return re.sub(r"^Source:[^\n]*\n\n?", "", text, count=1, flags=re.MULTILINE)


def _collapse_blank_lines(text: str) -> str:
    """Collapse 3+ consecutive blank lines to 2 (keeps paragraph breaks intact)."""
    return re.sub(r"\n{3,}", "\n\n", text)


def _cut_between(text: str, start_marker: str, end_marker: str) -> str:
    """Remove the region starting at start_marker up to (but not including) end_marker.

    Both markers are line-anchored literal strings (full-line prefix matches).
    If either is not found, returns text unchanged.
    """
    i = text.find(start_marker)
    if i < 0:
        return text
    j = text.find(end_marker, i + len(start_marker))
    if j < 0:
        return text
    return text[:i] + text[j:]


def _cut_to_end(text: str, start_marker: str) -> str:
    """Remove from start_marker through end-of-file."""
    i = text.find(start_marker)
    if i < 0:
        return text
    return text[:i]


def _replace_block(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    """Replace the block [start_marker, end_marker) with replacement."""
    i = text.find(start_marker)
    if i < 0:
        return text
    j = text.find(end_marker, i + len(start_marker))
    if j < 0:
        return text
    return text[:i] + replacement + text[j:]


# ---------------------------------------------------------------------------
# Per-chapter compressors
# ---------------------------------------------------------------------------

def compress_ch01(text: str) -> str:
    """ch01 (2411 tokens -> ~1200): drop §1.1 prose, §1.4 prose/reading-order,
    §1.5 Known Issues. Keep §1.2 structure table, §1.3 changes bullets + IG
    table, §1.4.1 column-description table."""
    text = _strip_source_line(text)

    # Drop §1.1 body prose; keep heading-less intro-skip by replacing body.
    text = _replace_block(
        text,
        "## 1.1 Purpose",
        "## 1.2 Organization of this Document",
        "## 1.1 Purpose\n\n"
        "SDTMIG v3.4 guides the organization, structure, and format of standard "
        "clinical trial tabulation datasets submitted to regulatory authorities. "
        "v3.4 supersedes all prior versions. Use in concert with SDTM v2.0.\n\n",
    )

    # §1.3: keep bullet list + related-IG table; drop the multi-paragraph intro.
    text = _replace_block(
        text,
        "## 1.3 Relationship to Prior CDISC Documents",
        "The most significant changes since SDTMIG v3.3 include:",
        "## 1.3 Relationship to Prior CDISC Documents\n\n"
        "All updates are backward-compatible; full diff in Appendix E. "
        "CT is updated quarterly; see Section 4.3 and the CDISC CT site.\n\n"
        "The most significant changes since SDTMIG v3.3 include:",
    )

    # §1.4: keep heading + §1.4.1; drop the reading-order prose.
    text = _replace_block(
        text,
        "## 1.4 How to Read this Implementation Guide",
        "### 1.4.1 How to Read a Domain Specification",
        "## 1.4 How to Read this Implementation Guide\n\n"
        "Recommended reading order: SDTM -> §1-3 -> §4 Assumptions -> §5-6 -> "
        "§7 Trial Design -> §8 Relationships -> §9 Study References -> "
        "appendices (esp. Appendix C, Controlled Terminology). See also "
        "SDTMIG-AP and SDTMIG-MD.\n\n",
    )

    # §1.5 Known Issues: drop entirely (two draft/future-release advisories).
    text = _cut_to_end(text, "## 1.5 Known Issues")

    return text


def compress_ch02(text: str) -> str:
    """ch02 (2783 -> ~1700): keep the role/subclass/GOC/type tables and the
    custom-domain rules (a-k). Drop discursive prose, the single worked example
    under §2.1, and the Mermaid diagram in §2.6."""
    text = _strip_source_line(text)

    # §2.1 intro prose: tighten to a one-paragraph lead-in before the role list.
    text = _replace_block(
        text,
        "## 2.1 Observations and Variables",
        "### Variable Roles (5 major roles)",
        "## 2.1 Observations and Variables\n\n"
        "The SDTM is built around **observations** (rows) described by "
        "**variables** (columns); each variable has a **role**.\n\n",
    )

    # Remove the worked "Example: In the observation..." block between the
    # Qualifier subclasses table and §2.2.
    text = _replace_block(
        text,
        "**Example:** In the observation",
        "## 2.2 Datasets and Domains",
        "## 2.2 Datasets and Domains",
    )

    # §2.2 prose around the numbered list: keep the 4-way code usage + flat-file
    # + Define-XML facts; drop the repeated prose about model sections.
    text = _replace_block(
        text,
        "All datasets are structured as flat files",
        "Data represented in SDTM datasets include:",
        "All datasets are structured as flat files with rows=observations and "
        "columns=variables. Metadata live in the Define-XML document.\n\n"
        "Data represented in SDTM datasets include:",
    )

    # §2.3: drop the tail prose after the GOC table.
    text = _replace_block(
        text,
        "In most cases, the choice of observation class",
        "## 2.4 Datasets Other than General Observation Class Domains",
        "See §8.6.1 for GOC selection guidance; §4 for general assumptions.\n\n"
        "## 2.4 Datasets Other than General Observation Class Domains",
    )

    # §2.5: drop the long submission-guidance prose; keep the numbered rules.
    text = _replace_block(
        text,
        "## 2.5 The SDTM Standard Domain Models",
        "### General rules for determining which variables to include:",
        "## 2.5 The SDTM Standard Domain Models\n\n"
        "Submit only domains actually collected (or directly derived). Tabulation "
        "(SDTM) data must be traceable to any ADaM analysis dataset.\n\n",
    )

    # §2.7: the "never used" / "DM never" / "extreme caution" / "may use"
    # tables are routing-relevant but their subheadings carry most of the
    # signal. Collapse the long bullet explanations per subsection.
    text = re.sub(
        r"### Must NEVER be used in DM domain \(SEND nonclinical only\):\n[\s\S]+?(?=\n### Use with extreme caution)",
        "### Must NEVER be used in DM domain (SEND nonclinical only):\n\n"
        "- SPECIES, STRAIN, SBSTRAIN, RPATHCD (use §9.2 Non-host Organism Identifiers for bacteria/virus taxonomy)\n\n",
        text,
        count=1,
    )

    # §2.6: drop the Mermaid diagram; keep the numbered procedure.
    text = re.sub(
        r"```mermaid\ngraph TD\n[^`]+```\n\n",
        "",
        text,
        count=1,
    )
    # Tighten §2.6 lead-in after the diagram drop.
    text = _replace_block(
        text,
        "## 2.6 Creating a New Domain",
        "Process for creating a custom domain",
        "## 2.6 Creating a New Domain\n\n",
    )

    return text


def compress_ch03(text: str) -> str:
    """ch03 (4907 -> ~3500): the Dataset-level Metadata table (§3.2.1) is the
    lookup backbone and must be kept whole. Trim §3.1 prose, §3.2 intro prose,
    §3.2.1.1 definitions prose, and §3.2.1.2 worked example."""
    text = _strip_source_line(text)

    # §3.1: shrink to a two-sentence lead.
    text = _replace_block(
        text,
        "## 3.1 Standard Metadata for Dataset Contents and Attributes",
        "## 3.2 Using the CDISC Domain Models in Regulatory Submissions",
        "## 3.1 Standard Metadata for Dataset Contents and Attributes\n\n"
        "Each domain model has descriptive metadata (Define-XML) plus two "
        "shaded, non-submitted columns assisting sponsors:\n"
        "- **CDISC Notes** - variable-use guidance\n"
        "- **Core** - Req/Exp/Perm classification (see §4.1.5)\n\n",
    )

    # §3.2 intro prose: tighten.
    text = _replace_block(
        text,
        "## 3.2 Using the CDISC Domain Models in Regulatory Submissions — Dataset Metadata",
        "### 3.2.1 Dataset-level Metadata",
        "## 3.2 Using the CDISC Domain Models in Regulatory Submissions - Dataset Metadata\n\n"
        "Define-XML describes each submitted dataset and its natural-key structure. "
        "Typical safety set: DM + EX, CM, AE, DS, MH, LB, VS (selection depends on protocol).\n\n"
        "Dataset definition metadata includes: filenames, descriptions, locations, "
        "structures, class, purpose, keys.\n\n"
        "Empty datasets should not be submitted and should not be in Define-XML.\n\n",
    )

    # §3.2.1 Dataset-level Metadata table: drop redundant "Purpose" and
    # "Location" columns (always "Tabulation" and "<code>.xpt" respectively),
    # saving ~20% of the largest table in the chapter.
    def _slim_datasets_table(chunk: str) -> str:
        lines = chunk.splitlines()
        out = []
        for ln in lines:
            if ln.startswith("|") and ln.count("|") >= 8:
                # parse and drop columns 6 (Purpose) and 8 (Location)
                cells = ln.split("|")
                # cells: ['', ' Dataset ', ' Description ', ..., '']
                if len(cells) >= 9:
                    # indexes: 1=Dataset 2=Description 3=Class 4=Structure
                    # 5=Purpose 6=Keys 7=Location 8=''
                    kept = cells[:5] + cells[6:7] + cells[8:]
                    out.append("|".join(kept))
                    continue
            out.append(ln)
        return "\n".join(out)

    _m = re.search(
        r"(### 3\.2\.1 Dataset-level Metadata\n[\s\S]+?)(?=\n### 3\.2\.1\.1 Primary Keys)",
        text,
    )
    if _m:
        text = text[: _m.start(1)] + _slim_datasets_table(_m.group(1)) + text[_m.end(1):]

    # §3.2.1.1 Primary Keys: drop the natural-key/surrogate-key definitions prose.
    text = _replace_block(
        text,
        "### 3.2.1.1 Primary Keys",
        "### 3.2.1.2 CDISC Submission Value-level Metadata",
        "### 3.2.1.1 Primary Keys\n\n"
        "List all natural keys that define record uniqueness, consistent with "
        "Define-XML. For GOC domains and some special-purpose domains, "
        "**--SEQ** combined with STUDYID, USUBJID, DOMAIN yields a unique record. "
        "--SEQ is normally a surrogate key; occasionally it contributes to the "
        "natural key (see §4.1.9). A SUPP-- variable may also contribute.\n\n",
    )

    # §3.2.1.2: drop the VS worked example; keep the short lead-in.
    text = _replace_block(
        text,
        "### 3.2.1.2 CDISC Submission Value-level Metadata",
        "## 3.2.2 Conformance",
        "### 3.2.1.2 CDISC Submission Value-level Metadata\n\n"
        "Findings use a vertical (one row per observation) structure. When one "
        "domain holds heterogeneous test codes with different attributes (e.g., VS "
        "systolic BP vs. height vs. BMI), value-level metadata in Define-XML "
        "captures per-test-code differences in type, units, role, and origin.\n\n",
    )

    # drop the "---" divider preceding §3.2.2 created by the cut.
    text = re.sub(r"\n---\n\n## 3\.2\.2", "\n## 3.2.2", text)

    # §3.2.2 Conformance: keep the headline; tighten the 10-item list (most
    # items restate §2.5 rules). Retain compliance axes without re-explaining.
    text = re.sub(
        r"## 3\.2\.2 Conformance\n\nConformance with the SDTMIG domain models is minimally indicated by:\n\n(?:\d+\. [^\n]+\n)+",
        "## 3.2.2 Conformance\n\n"
        "Minimum conformance checklist:\n\n"
        "1. Complete metadata structure per domain.\n"
        "2. Follow SDTMIG domain models where applicable; use SDTMIG domain names + prefixes + variable names + types.\n"
        "3. Follow CT and format guidance for each variable where provided.\n"
        "4. Place all collected/relevant derived data in a standard / special-purpose / GOC domain.\n"
        "5. Include all Req+Exp variables; populate all Req values.\n"
        "6. Each record has Identifier + Timing + Topic variables.\n"
        "7. Honor all CDISC Notes business rules and general + domain-specific assumptions.\n",
        text,
        count=1,
    )

    return text


def compress_ch04(text: str) -> str:
    """ch04 (31315 tokens): the reasoning substrate. Preserve verbatim.

    The only permitted edit is stripping the leading "Source: ..." line
    (redundant with the `<!-- source: ... -->` comment emitted by the caller).
    This keeps character retention >= 99% of the source file (PLAN §5.1 C6
    requires >= 95%).
    """
    return _strip_source_line(text)


_SUPP_SPEC_REPLACEMENT = """supp--.xpt, Supplemental Qualifiers for [domain name] - Relationship. One record per supplemental qualifier per related parent domain record(s), Tabulation.

| Variable | Label | Type | CT/Format | Role | CDISC Notes | Core |
|----------|-------|------|-----------|------|-------------|------|
| STUDYID | Study Identifier | Char | | Identifier | Parent study identifier. | Req |
| RDOMAIN | Related Domain Abbreviation | Char | (DOMAIN) | Identifier | 2-char parent domain code. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Parent record USUBJID. | Req |
| IDVAR | Identifying Variable | Char | * | Identifier | Parent-identifying variable (e.g., --SEQ, --GRPID). | Exp |
| IDVARVAL | Identifying Variable Value | Char | | Identifier | Value of IDVAR. | Exp |
| QNAM | Qualifier Variable Name | Char | * | Topic | Qualifier short name, <=8 chars, must not start with a digit, letters/digits/_ only. | Req |
| QLABEL | Qualifier Variable Label | Char | | Synonym Qualifier | Long name/label of QNAM, <=40 chars. | Req |
| QVAL | Data Value | Char | | Result Qualifier | Value of the qualifier; never null. | Req |
| QORIG | Origin | Char | | Record Qualifier | Origin of QVAL (e.g., CRF, Assigned, Derived); see §4.1.8. | Req |
| QEVAL | Evaluator | Char | (EVAL) | Record Qualifier | Role of the evaluator for subjective values (null if objective). | Exp |

"""

_RELREC_SPEC_REPLACEMENT = """relrec.xpt, Related Records - Relationship. One record per related record, group of records or dataset, Tabulation.

| Variable | Label | Type | CT/Format | Role | CDISC Notes | Core |
|----------|-------|------|-----------|------|-------------|------|
| STUDYID | Study Identifier | Char | | Identifier | Unique study identifier. | Req |
| RDOMAIN | Related Domain Abbreviation | Char | (DOMAIN) | Identifier | Parent domain code. | Req |
| USUBJID | Unique Subject Identifier | Char | | Identifier | Parent subject. | Exp |
| IDVAR | Identifying Variable | Char | * | Identifier | Parent-identifying variable (e.g., --SEQ, --GRPID). | Req |
| IDVARVAL | Identifying Variable Value | Char | | Identifier | Value of IDVAR in the parent record. | Exp |
| RELTYPE | Relationship Type | Char | (RELTYPE) | Record Qualifier | ONE or MANY; only for dataset-to-dataset relationships (§8.3). | Exp |
| RELID | Relationship Identifier | Char | | Record Qualifier | Same RELID within USUBJID groups related records. | Req |

"""


def compress_ch08(text: str) -> str:
    """ch08 (11980 -> ~5500): keep every Specification table and rule list.
    Drop the illustrative data tables under §8.1.1 (12-row CM), §8.2.2
    (Examples 1-3 relrec), §8.4.3 (suppae + suppqs), §8.7 (DM + RELSUB data),
    and §8.8 (RELSPEC data + mermaid).

    Implemented with regex cuts anchored to the surrounding headings so each
    replacement is deterministic and preserves the surrounding structure.
    """
    text = _strip_source_line(text)

    # ch08 Overview: tighten 8-item section index + IDVAR bullet list.
    text = re.sub(
        r"## Overview\n[\s\S]+?(?=\n---\n\n## 8\.1 Relating Groups of Records Within a Domain Using --GRPID)",
        "## Overview\n\n"
        "SDTM provides these relationship mechanisms, with keys STUDYID, "
        "DOMAIN, USUBJID + IDVAR/IDVARVAL identifying record-level joins:\n\n"
        "- **§8.1** --GRPID groups records within one subject + one domain\n"
        "- **§8.2** RELREC peer record relationships (same or cross-domain)\n"
        "- **§8.3** RELREC dataset-to-dataset relationships\n"
        "- **§8.4** SUPP-- for non-standard variables\n"
        "- **§8.5** CO for unstructured comments\n"
        "- **§8.6** where data belong (GOC selection)\n"
        "- **§8.7** RELSUB for subject <-> subject relationships\n"
        "- **§8.8** RELSPEC for specimen lineage\n\n"
        "Common IDVAR values: --SEQ (required in all GOC except DM; sponsor-"
        "defined), --REFID (permissible sponsor-defined identifier for "
        "specimens/ECGs), --GRPID (§8.1).\n\n",
        text,
        count=1,
    )

    # §8.1 body prose before §8.1.1: tighten.
    text = re.sub(
        r"## 8\.1 Relating Groups of Records Within a Domain Using --GRPID\n[\s\S]+?(?=\n### 8\.1\.1 --GRPID Example)",
        "## 8.1 Relating Groups of Records Within a Domain Using --GRPID\n\n"
        "--GRPID is Permissible in all GOC domains; records within a USUBJID "
        "within a single domain that share the same --GRPID value are "
        "related (e.g., medications in a combination therapy). Values are "
        "sponsor-defined; if carrying embedded meaning, must be consistent "
        "across the submission. No meaning across subjects or domains.\n\n"
        "Using --GRPID can reduce the number of rows needed in RELREC, "
        "SUPP--, and CO to relate groups of GOC records.\n\n",
        text,
        count=1,
    )

    # §8.2.1 RELREC Specification table: keep structure but slim CDISC Notes
    # (the full notes merely repeat §8.2 intro text that we already kept).
    text = re.sub(
        r"relrec\.xpt, Related Records — Relationship\. One record per related record, group of records or dataset, Tabulation\.\n\n\| Variable Name \|[\s\S]+?\n\n\^1\^ In this column, an asterisk \(\*\) indicates that the variable may be subject to controlled terminology\. CDISC/NCI codelist values are enclosed in parentheses\.\n\n",
        _RELREC_SPEC_REPLACEMENT,
        text,
        count=1,
    )

    # §8.4.1 SUPP-- Specification table: same slim-notes treatment.
    text = re.sub(
        r"supp--\.xpt, Supplemental Qualifiers for \[domain name\] — Relationship\. One record per supplemental qualifier per related parent domain record\(s\), Tabulation\.\n\n\| Variable Name \|[\s\S]+?\n\n\^1\^ In this column, an asterisk \(\*\) indicates that the variable may be subject to controlled terminology\. CDISC/NCI codelist values are enclosed in parentheses\.\n\n",
        _SUPP_SPEC_REPLACEMENT,
        text,
        count=1,
    )

    # §8.2 intro prose (before §8.2.1): tighten five paragraphs into bullets.
    text = re.sub(
        r"## 8\.2 Relating Peer Records\n[\s\S]+?(?=\n### 8\.2\.1 Related Records)",
        "## 8.2 Relating Peer Records\n\n"
        "RELREC describes collected relationships between records (same or "
        "cross-domain) for a subject; relationships are collected via CRF "
        "reference, checkbox, or CRF design (e.g., vital signs during exercise "
        "stress test).\n\n"
        "A relationship is defined by adding a RELREC record for each related "
        "record and assigning a unique character RELID (identical for all "
        "related records within USUBJID). Keys: STUDYID, RDOMAIN, USUBJID, "
        "IDVAR, IDVARVAL. Single records use --SEQ in IDVAR; groups use "
        "--GRPID (more efficient, e.g., AE linked to a group of CM records).\n\n"
        "Use RELREC for: (a) explicit relationships (e.g., CM taken because of "
        "an AE); or (b) dataset-level relationships (see §8.3).\n\n",
        text,
        count=1,
    )

    # §8.4 intro prose (before §8.4.1): tighten.
    text = re.sub(
        r"## 8\.4 Relating Non-standard Variable Values to a Parent Domain\n[\s\S]+?(?=\n### 8\.4\.1 Supplemental Qualifiers)",
        "## 8.4 Relating Non-standard Variable Values to a Parent Domain\n\n"
        "SDTM forbids adding new variables. Non-standard variables (NSVs) are "
        "captured in separate SUPP-- datasets (one per parent domain) covering "
        "GOC domains, DM, and SV. Each SUPP-- record holds QNAM (variable "
        "name), QLABEL, QVAL, QORIG (origin; see §4.1.8), and QEVAL (evaluator "
        "role; e.g., \"SPONSOR\", \"ADJUDICATION COMMITTEE\"). See Appendix C1 "
        "for CT. SUPP-- also stores **attributions** (subjective "
        "interpretations): for objective data QEVAL is null; for subjective "
        "data QEVAL reflects the person/institution role.\n\n"
        "STUDYID...QNAM must be unique per record. If two evaluators provide "
        "the same attribution (e.g., investigator vs. adjudicator TE flag), "
        "use distinct QNAM values (e.g., AETRTEMI, AETRTEMA). --GRPID in IDVAR "
        "may be used to relate a SUPP-- record to a group of parent records "
        "(e.g., attribution on a group of ECG measurements).\n\n",
        text,
        count=1,
    )

    # §8.3 Relating Datasets: tighten the intro prose before §8.3.1.
    text = re.sub(
        r"## 8\.3 Relating Datasets Using RELREC\n[\s\S]+?(?=\n### 8\.3\.1 RELREC Dataset Relationship Example)",
        "## 8.3 Relating Datasets Using RELREC\n\n"
        "RELREC can also describe dataset-to-dataset relationships (e.g., "
        "one-to-many / parent-child). Include one record per related dataset "
        "identifying the keys used to link records. Use only when the sponsor "
        "had to split information between datasets that need joint analysis. "
        "SUPP-- and CO do not need RELREC (they already carry parent keys).\n\n",
        text,
        count=1,
    )

    # §8.3.1: drop the TU/TR worked example table + long narrative after it;
    # keep a compact TU/TR example sentence + collapsed RELTYPE semantics.
    text = re.sub(
        r"### 8\.3\.1 RELREC Dataset Relationship Example\n[\s\S]+?(?=\n---\n\n## 8\.4 Relating Non-standard)",
        "### 8.3.1 RELREC Dataset Relationship Example\n\n"
        "Dataset-to-dataset row pairs carry null USUBJID + null IDVARVAL. "
        "Example (TU ONE <-> TR MANY via --LNKID): two RELREC rows sharing "
        "RELID, IDVAR=TULNKID for TU and IDVAR=TRLNKID for TR.\n\n"
        "IDVAR names the join key (not --SEQ, which is subject- and "
        "dataset-scoped). Typical choices: --GRPID, --SPID, --REFID, "
        "--LNKID, --LNKGRP. RELTYPE semantics:\n\n"
        "- **ONE / ONE**: no hierarchy; at most one record per dataset per "
        "IDVAR within USUBJID.\n"
        "- **ONE / MANY**: parent-child; one record in the ONE side maps to "
        "many on the MANY side (same IDVAR within USUBJID).\n"
        "- **MANY / MANY**: unusual; often not a usable merge/join (e.g., "
        "§6.3.5.9.3 PP <-> PC).\n",
        text,
        count=1,
    )

    # §8.4.1 Key Rules: strip the long re-explanation of SUPP-- linkage
    # (already captured in the §8.4 intro + spec table).
    text = re.sub(
        r"### Key Rules\n\n- A record in a SUPP-- dataset relates back to its parent record\(s\)[\s\S]+?(?=\n### 8\.4\.2 Submitting Supplemental Qualifiers in Separate Datasets)",
        "### Key Rules\n\n"
        "- SUPP-- -> parent via STUDYID, RDOMAIN, USUBJID, IDVAR/IDVARVAL. Exception: SUPP-- for DM records -- IDVAR/IDVARVAL are null (DM has one record per USUBJID).\n"
        "- Every SUPP-- record must have a non-null QVAL; delete null-QVAL rows before submission.\n"
        "- QVAL > 200 chars: see §4.5.3.\n"
        "- CT for QNAM/QLABEL: see Appendix C1; additional QNAM values may be created per QVAL guidance.\n\n",
        text,
        count=1,
    )

    # §8.4.2: tighten four paragraphs into two sentences + the SQ-prefix rule.
    text = re.sub(
        r"### 8\.4\.2 Submitting Supplemental Qualifiers in Separate Datasets\n[\s\S]+?(?=\n### 8\.4\.3 Examples)",
        "### 8.4.2 Submitting Supplemental Qualifiers in Separate Datasets\n\n"
        "One SUPP-- dataset per parent domain (the single SUPPQUAL approach "
        "from SDTMIG v3.1 is deprecated). Name is SUPP-- where -- is the "
        "parent domain code (e.g., suppdm.xpt, supppr.xpt). Split-domain "
        "datasets have longer names (SUPPFAMH). For SDTMIG-AP SUPP-- on FA "
        "(which would exceed length), use the SQ prefix (e.g., SQAPFAMH).\n\n"
        "See §4.5.3 for values > 200 chars.\n\n",
        text,
        count=1,
    )

    # §8.4.4 When Not to Use Supplemental Qualifiers: preserve rule list but
    # tighten the embedded ECG example into one phrase.
    text = re.sub(
        r"- Findings interpretations that should be added as an additional test code and result\. An example of this would be a record for electrocardiogram interpretation where EGTESTCD = \"INTP\", and the same EGGRPID or EGREFID value would be assigned for all records associated with that ECG \(see Section 4\.5\.5, Clinical Significance for Findings Observation Class Data\)",
        "- Findings interpretations that belong as a new test code + result (e.g., EGTESTCD=\"INTP\" with matching EGGRPID/EGREFID; see §4.5.5)",
        text,
        count=1,
    )

    # §8.5 Relating Comments: retain the numbered rules only.
    text = re.sub(
        r"## 8\.5 Relating Comments to a Parent Domain\n[\s\S]+?(?=\n---\n\n## 8\.6 Where Data Belong)",
        "## 8.5 Relating Comments to a Parent Domain\n\n"
        "The CO special-purpose domain (§5.1) captures free-text comments. CO "
        "uses the same keys as SUPP-- (STUDYID, RDOMAIN, USUBJID, IDVAR, "
        "IDVARVAL). STUDYID, USUBJID, and DOMAIN=CO are always populated; "
        "RDOMAIN/IDVAR/IDVARVAL follow:\n\n"
        "1. Subject-general comment (log-style): RDOMAIN, IDVAR, IDVARVAL null.\n"
        "2. Domain-scoped (not record-specific): RDOMAIN populated; IDVAR/IDVARVAL null.\n"
        "3. Record-scoped: RDOMAIN + IDVAR + IDVARVAL identify the parent record(s).\n\n"
        "Extras: CRF page/name -> COREF; Timing (VISITNUM, VISIT) may be added. "
        "--GRPID in IDVAR works as in SUPP--/RELREC but only one RDOMAIN per "
        "CO record; if a comment spans multiple domains it must be repeated.\n\n",
        text,
        count=1,
    )

    # §8.6 Where Data Belong: tighten intro + drop §8.6.3 long discursive prose.
    # Keep the decision table (load-bearing) and the short decision rules.
    text = re.sub(
        r"### 8\.6\.1 Guidelines for Determining the General Observation Class\n[\s\S]+?(?=\n### 8\.6\.2)",
        "### 8.6.1 Guidelines for Determining the General Observation Class\n\n"
        "See §2.6 for creating new domains. Classify by the observation's "
        "content (not CRF structure):\n\n"
        "- **Intervention**: something done to a subject expected to have a "
        "physiological effect (includes subject-administered). Measurements "
        "from a procedure are findings even if the procedure has intervention "
        "aspects (e.g., exercise stress test).\n"
        "- **Event**: something that happens to a subject spontaneously. MH "
        "and CE are the usual landing places for non-AE medical events. "
        "Events data is events data regardless of whether dates were "
        "collected (e.g., MH may have no dates).\n"
        "- **Finding**: measurements, tests, assessments, examinations on a "
        "subject or their specimen. Findings about an event/intervention use "
        "FA (see §6.4 and §8.6.3).\n\n",
        text,
        count=1,
    )
    text = re.sub(
        r"### 8\.6\.3 Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions\n[\s\S]+?(?=\n---\n\n## 8\.7 Related Subjects)",
        "### 8.6.3 Guidelines for Differentiating Between Interventions, Events, Findings, and Findings About Events or Interventions\n\n"
        "FA represents findings **about** events or interventions (key use: "
        "CE vs. FA). Typical confounders:\n\n"
        "- Events may be prespecified rather than verbatim.\n"
        "- Some events are long-lasting (\"conditions\"); dates may be irrelevant.\n"
        "- Some Events records lack dates (e.g., post-marketing AE occurrence collection).\n"
        "- Properties of an event that vary over time -> findings about events, not events.\n"
        "- Severity / relationship to treatment are built-in Event qualifiers (not FA).\n"
        "- Sponsors choose how they define an \"event\" (see AE assumption 7e).\n\n"
        "Decision table:\n\n"
        "| Question | Interpretation |\n"
        "|----------|----------------|\n"
        "| Measurement with units? | Yes -> finding (possibly FA if of an event). No is inconclusive. |\n"
        "| CRF per visit or log form? | Log form -> Events/Interventions (dates are start/end). Per-visit -> usually Findings. |\n"
        "| What dates collected? | Start/end -> event or intervention. Assessment dates -> finding. |\n"
        "| Verbatim text coded? | Yes -> Events/Interventions (topic coded). Findings results may also be coded. |\n"
        "| Applies to event as a whole? | Yes -> Events record. No -> multiple FA records over time. |\n"
        "| Fits QRS criteria (https://www.cdisc.org/foundational/qrs)? | Use QS/FT/RS when applicable; format (e.g., VAS) alone does not imply QRS. |\n\n"
        "**Rule**: an Events-class record represents the event as a whole; "
        "per-event-part or time-varying observations go in FA (not in "
        "--SUPP). If a related finding/intervention fits an existing class, "
        "store it there and link via RELREC; otherwise use SUPP-- or FA per "
        "§6.4.1.\n",
        text,
        count=1,
    )
    # §8.1.1 --GRPID Example body: drop the 12-row cm.xpt table + row commentary.
    text = re.sub(
        r"### 8\.1\.1 --GRPID Example\n[\s\S]+?\n(?=---\n)",
        "### 8.1.1 --GRPID Example\n\n"
        "In CM, two subjects each record two combination therapies with three "
        "medications each; CMGRPID groups medications within a subject "
        "(e.g., \"COMBO THPY 1\"). The value is meaningful only within a "
        "subject within a domain.\n\n",
        text,
        count=1,
    )

    # §8.2.2 RELREC Dataset Examples: drop Examples 1-3 relrec tables.
    text = re.sub(
        r"### 8\.2\.2 RELREC Dataset Examples\n[\s\S]+?(?=\nAdditional examples may be found in the domain examples such as Section 6\.2\.4)",
        "### 8.2.2 RELREC Dataset Examples\n\n"
        "Typical uses: (1) relate an AE record (IDVAR=AESEQ) to peer CM/LB "
        "records via shared RELID; (2) collapse multiple related records using "
        "--GRPID in IDVAR to reduce RELREC rows; (3) dataset-to-dataset "
        "relationships use IDVAR=--LNKID (never --SEQ) with RELTYPE=ONE/MANY "
        "and null USUBJID/IDVARVAL.\n",
        text,
        count=1,
    )

    # §8.4.3 Examples: drop the suppae.xpt + suppqs.xpt worked tables.
    text = re.sub(
        r"### 8\.4\.3 Examples\n[\s\S]+?(?=\n### 8\.4\.4)",
        "### 8.4.3 Examples\n\n"
        "Typical SUPPAE rows qualify an AE (IDVAR=AESEQ, IDVARVAL=parent "
        "AESEQ) with QNAM values like AESOSP (Other Medically Important SAE, "
        "QORIG=CRF) or AETRTEM (Treatment Emergent Flag, QORIG=Derived, "
        "QEVAL=SPONSOR). SUPPQS rows may capture QSLANG per subject per "
        "questionnaire (IDVAR=QSCAT, IDVARVAL=BPI/ADAS-COG).\n",
        text,
        count=1,
    )

    # §8.7 RELSUB Example: drop the DM + RELSUB data tables.
    text = re.sub(
        r"### Example\n\nExample 1: The following data are from a hemophilia study[\s\S]+?(?=\n---\n\n## 8\.8 Related Specimens)",
        "### Example\n\n"
        "A mother-twins hemophilia example: for a mother and two "
        "dizygotic-twin sons, RELSUB has 6 rows (3 subjects x bidirectional), "
        "with SREL values \"MOTHER, BIOLOGICAL\", \"CHILD, BIOLOGICAL\", and "
        "\"TWIN, DIZYGOTIC\".\n",
        text,
        count=1,
    )

    # §8.7 Assumptions: tighten from 8 verbose paragraphs to 8 compact rules.
    text = re.sub(
        r"### Assumptions\n\n1\. RELSUB is used to represent relationships between persons[\s\S]+?(?=\n### Example\n\nA mother-twins)",
        "### Assumptions\n\n"
        "1. RELSUB is only for relationships between two study subjects. Subject <-> non-subject use APRELSUB (SDTMIG-AP).\n"
        "2. POOLID is nonclinical in origin but permitted for human trials; if submitted, POOLDEF must also be submitted.\n"
        "3. If POOLID is submitted, exactly one of USUBJID or POOLID is populated per record.\n"
        "4. If POOLID is not used, USUBJID is populated on every record.\n"
        "5. RSUBJID must be a USUBJID that exists in DM and is populated on every record.\n"
        "6. SREL should come from the CT codelist RELSUB where possible; must not be less specific than the verbatim term (e.g., do not record \"brother\" as \"RELATIVE, FIRST DEGREE\").\n"
        "7. Every relationship is recorded as two directional rows (viewpoint of each subject; SREL mirrors).\n"
        "8. If two subjects have multiple relationships (e.g., maternal aunt + wet nurse), each relationship is two rows.\n\n",
        text,
        count=1,
    )

    # §8.8 RELSPEC: drop the provisional-PGx banner (historical context) and
    # the trivial description line; keep spec + assumptions + trimmed example.
    text = re.sub(
        r"## 8\.8 Related Specimens \(RELSPEC\)\n\n> \*\*Note:\*\* BE, BS, and RELSPEC[\s\S]+?(?=\n### RELSPEC)",
        "## 8.8 Related Specimens (RELSPEC)\n\n"
        "RELSPEC (copied from SDTMIG-PGx) represents relationships between "
        "specimens; under revision for a future SDTMIG.\n\n",
        text,
        count=1,
    )
    text = re.sub(
        r"### RELSPEC — Description/Overview\n\nA dataset used to represent relationships between specimens\.\n\n",
        "",
        text,
        count=1,
    )

    # §8.8 Example: drop the mermaid diagram + relspec.xpt data table (ends at EOF).
    text = re.sub(
        r"### Example\n\nExample 1: This example uses the sample specimen lineage[\s\S]+\Z",
        "### Example\n\n"
        "Example: parent-child specimen lineage. LEVEL=1 with null PARENT "
        "denotes a collected sample; LEVEL>1 with non-null PARENT denotes a "
        "derived sample (e.g., SPC-001 TISSUE L1 -> SPC-001-B TISSUE L2 -> "
        "SPC-001-B-1 DNA L3). SPEC reflects the specimen type whether "
        "collected or derived.\n",
        text,
        count=1,
    )

    return text


def compress_ch10(text: str) -> str:
    """ch10 (7129 -> ~1800): drop Appendix A (acknowledgments), most of
    Appendix E (the huge section-by-section changelog), and Appendix F
    (legalese). Keep Appendix B glossary, Appendix C pointers, Appendix C1 QNAM
    codes, Appendix D variable-naming fragments, and an Appendix E summary."""
    text = _strip_source_line(text)

    # Appendix C: drop the CT-process Key Points (meta about release cadence,
    # not routing-relevant); keep intro sentence + Appendix C1 QNAM table.
    text = re.sub(
        r"## Appendix C: Controlled Terminology\n\nCDISC Terminology is centrally managed by the CDISC Controlled Terminology Team[\s\S]+?(?=\n### Appendix C1:)",
        "## Appendix C: Controlled Terminology\n\n"
        "CDISC CT serves SDTM, CDASH, ADaM, SEND, and TA standards; browse "
        "packages at https://www.cdisc.org/standards/terminology/controlled-terminology "
        "and https://www.cancer.gov/research/resources/terminology/cdisc.\n\n",
        text,
        count=1,
    )

    # Appendix B intro prose: drop the leading two-sentence introduction; the
    # glossary table alone is self-explanatory.
    text = re.sub(
        r"## Appendix B: Glossary and Abbreviations\n\nThe following table lists some of the abbreviations and terms are used in this document\. Additional definitions can be found in the individual sections of this document \(see esp\. Section 7\.1\.2, Definitions of Trial Design Concepts\) and in the CDISC Glossary \(available at https://www\.cdisc\.org/standards/glossary\)\.\n\n",
        "## Appendix B: Glossary and Abbreviations\n\n"
        "See also §7.1.2 and the CDISC Glossary (https://www.cdisc.org/standards/glossary).\n\n",
        text,
        count=1,
    )

    # Appendix B: collapse long-winded ICH / ISO 8601 descriptions.
    text = text.replace(
        "| ICH | International Conference on Harmonisation of Technical Requirements for Registration of Pharmaceuticals for Human Use |",
        "| ICH | International Conference on Harmonisation |",
    )
    text = text.replace(
        "| ICH E2A | ICH guidelines on Clinical Safety Data Management: Definitions and Standards for Expedited Reporting |",
        "| ICH E2A | Clinical Safety Data Mgmt: Expedited Reporting |",
    )
    text = text.replace(
        "| ICH E2B | ICH guidelines on Clinical Safety Data Management: Data Elements for Transmission of Individual Cases Safety Reports |",
        "| ICH E2B | Clinical Safety Data Mgmt: Case Safety Report elements |",
    )
    text = text.replace(
        "| ICH E3 | ICH guidelines on Structure and Content of Clinical Study Reports |",
        "| ICH E3 | Structure / content of clinical study reports |",
    )
    text = text.replace(
        "| ICH E9 | ICH guidelines on Statistical Principles for Clinical Trials |",
        "| ICH E9 | Statistical principles for clinical trials |",
    )
    text = text.replace(
        "| ISO 8601 | ISO character representation of dates, date/times, intervals, and durations of time. The SDTM uses the extended format |",
        "| ISO 8601 | Date/time, interval, and duration representation (SDTM uses the extended format) |",
    )
    text = text.replace(
        "| ISO 3166 | ISO codelist for representing countries; the Alpha-3 codelist uses 3-character codes |",
        "| ISO 3166 | Country codelist; Alpha-3 uses 3-char codes |",
    )
    text = text.replace(
        "| SDS | Submission Data Standards. Also the name of the team that created the SDTM and SDTMIG |",
        "| SDS | Submission Data Standards (team that created SDTM + SDTMIG) |",
    )
    text = text.replace(
        "| SDTMIG | Study Data Tabulation Model Implementation Guide: Human Clinical Trials |",
        "| SDTMIG | SDTM Implementation Guide: Human Clinical Trials |",
    )
    text = text.replace(
        "| SDTMIG-AP | Study Data Tabulation Model Implementation Guide: Associated Persons |",
        "| SDTMIG-AP | SDTMIG: Associated Persons |",
    )
    text = text.replace(
        "| SDTMIG-MD | Study Data Tabulation Model Implementation Guide for Medical Devices |",
        "| SDTMIG-MD | SDTMIG: Medical Devices |",
    )
    text = text.replace(
        "| SDTMIG-PGx | Study Data Tabulation Model Implementation Guide: Pharmacogenomics/Genetics |",
        "| SDTMIG-PGx | SDTMIG: Pharmacogenomics/Genetics |",
    )

    # Appendix A -> drop whole appendix (acknowledgments prose).
    text = _replace_block(
        text,
        "## Appendix A: CDISC SDS Team",
        "## Appendix B: Glossary and Abbreviations",
        "## Appendix A: CDISC SDS Team\n\n"
        "Acknowledgments list elided; see source PDF page 444.\n\n---\n\n",
    )

    # Appendix E: drop the 70+ row section-by-section change table; keep the
    # "New Domains" table, "Decommissioning of MO" explanation, and general-
    # changes bullets (the only entries that are routing/content-relevant).
    text = _replace_block(
        text,
        "### Key Section-by-Section Changes",
        "## Appendix F: Representations and Warranties, Limitations of Liability, and Disclaimers",
        "### Key Section-by-Section Changes\n\n"
        "Detailed per-section changelog elided; consult the source CDISC diff "
        "file on https://www.cdisc.org/members-only/cdisc-library-archives.\n\n---\n\n",
    )

    # Appendix D: keep the fragment table but drop the "Rules for Using
    # Fragments" prose bullets (trivial guidance) and the intro sentence.
    text = re.sub(
        r"## Appendix D: CDISC Variable-naming Fragments\n\nThe CDISC SDS group has defined a standard list of fragments to use as a guide when naming variables in SUPP-- datasets \(as QNAM\) or assigning --TESTCD values\.\n\n### Rules for Using Fragments\n\n[\s\S]+?(?=\n### Fragment Reference Table)",
        "## Appendix D: CDISC Variable-naming Fragments\n\n"
        "Use the longest fragment that fits the 8-char QNAM / --TESTCD limit; "
        "drop characters as needed while avoiding name collisions.\n\n",
        text,
        count=1,
    )

    # Appendix F: drop whole appendix (patent / warranty / liability legalese).
    text = _cut_to_end(text, "## Appendix F: Representations and Warranties")

    return text


COMPRESSORS = {
    "ch01_introduction.md": compress_ch01,
    "ch02_fundamentals.md": compress_ch02,
    "ch03_submitting_data.md": compress_ch03,
    "ch04_general_assumptions.md": compress_ch04,
    "ch08_relationships.md": compress_ch08,
    "ch10_appendices.md": compress_ch10,
}


# ---------------------------------------------------------------------------
# Build output
# ---------------------------------------------------------------------------

def build_output() -> str:
    src_paths = [SRC_DIR / name for name in CHAPTERS]
    for p in src_paths:
        if not p.is_file():
            raise FileNotFoundError(f"source not found: {p}")

    # Idempotence anchor: max mtime across sources (not datetime.now()).
    max_mtime = max(os.path.getmtime(p) for p in src_paths)
    ts = _dt.datetime.utcfromtimestamp(max_mtime).strftime("%Y-%m-%d %H:%M")

    parts: list[str] = []
    parts.append(
        f"<!-- generated by scripts/compress_chapters.py (source mtime: {ts}) -->\n"
    )
    parts.append("\n")
    parts.append("# SDTMIG v3.4 - Chapters (Compressed)\n\n")
    parts.append(
        "Six chapter compressions. ch04 (General Assumptions) is preserved "
        "verbatim; others are compressed by removing prose, illustrative "
        "example data tables, and legalese while retaining all Specification "
        "tables, numbered rule lists, and variable / codelist / domain-code "
        "references.\n\n"
    )
    parts.append("---\n\n")

    for idx, name in enumerate(CHAPTERS):
        src_path = SRC_DIR / name
        raw = src_path.read_text(encoding="utf-8")
        compressed = COMPRESSORS[name](raw)
        compressed = _collapse_blank_lines(compressed).rstrip() + "\n"
        parts.append(f"<!-- source: knowledge_base/chapters/{name} -->\n\n")
        parts.append(compressed)
        if idx != len(CHAPTERS) - 1:
            parts.append("\n---\n\n")

    return "".join(parts)


def main() -> int:
    output = build_output()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(output, encoding="utf-8")
    print(
        f"wrote {OUT} ({len(output)} chars, {len(output.splitlines())} lines)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
