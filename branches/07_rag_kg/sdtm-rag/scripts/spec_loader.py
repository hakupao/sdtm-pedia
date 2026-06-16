"""KB spec + terminology loader for SDTM validation (Phase 1C.2 prerequisite).

Parses knowledge_base/domains/*/spec.md  -> per-domain variable registry.
Parses knowledge_base/terminology/**/*.md -> codelist submission values.

Usage:
    loader = SpecLoader(kb_root)
    dm = loader.get_domain("DM")       # DomainSpec with variables
    cl = loader.get_codelist("C66769")  # Codelist with submission values
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class VariableSpec:
    name: str
    order: int
    label: str
    var_type: str  # "Char" or "Num"
    controlled_terms: str  # C-code, "MedDRA", "ISO 8601 ...", or ""
    role: str
    core: str  # "Req", "Exp", "Perm"
    cdisc_notes: str = ""


@dataclass
class DomainSpec:
    domain: str
    domain_class: str
    structure: str
    variables: list[VariableSpec] = field(default_factory=list)

    def var_names(self) -> set[str]:
        return {v.name for v in self.variables}

    def req_vars(self) -> list[str]:
        return [v.name for v in self.variables if v.core == "Req"]

    def exp_vars(self) -> list[str]:
        return [v.name for v in self.variables if v.core == "Exp"]

    def get_variable(self, name: str) -> VariableSpec | None:
        for v in self.variables:
            if v.name == name:
                return v
        return None

    def seq_variable(self) -> str | None:
        """Return the --SEQ variable name for this domain (e.g., AESEQ)."""
        prefix = self.domain
        seq_name = f"{prefix}SEQ"
        if self.get_variable(seq_name):
            return seq_name
        return None


@dataclass
class Codelist:
    code: str
    name: str
    extensible: bool
    submission_values: list[str]


_CT_CODE_RE = re.compile(r"^C\d+$")


class SpecLoader:
    """Loads and caches KB spec and terminology reference data."""

    def __init__(self, kb_root: Path):
        self.kb_root = kb_root
        self._domains: dict[str, DomainSpec] | None = None
        self._codelists: dict[str, Codelist] | None = None

    @property
    def domains(self) -> dict[str, DomainSpec]:
        if self._domains is None:
            self._domains = self._load_all_specs()
        return self._domains

    @property
    def codelists(self) -> dict[str, Codelist]:
        if self._codelists is None:
            self._codelists = self._load_all_codelists()
        return self._codelists

    def get_domain(self, domain: str) -> DomainSpec | None:
        return self.domains.get(domain.upper())

    def get_codelist(self, code: str) -> Codelist | None:
        return self.codelists.get(code.upper())

    def known_domains(self) -> list[str]:
        return sorted(self.domains.keys())

    def is_ct_code(self, ct_ref: str) -> bool:
        return bool(_CT_CODE_RE.match(ct_ref.strip()))

    # ── Spec parsing ─────────────────────────────────────────────────────

    def _load_all_specs(self) -> dict[str, DomainSpec]:
        specs: dict[str, DomainSpec] = {}
        domains_dir = self.kb_root / "domains"
        if not domains_dir.exists():
            return specs
        for domain_dir in sorted(domains_dir.iterdir()):
            if not domain_dir.is_dir():
                continue
            spec_file = domain_dir / "spec.md"
            if not spec_file.exists():
                continue
            domain_name = domain_dir.name.upper()
            spec = self._parse_spec(spec_file, domain_name)
            if spec:
                specs[domain_name] = spec
        return specs

    def _parse_spec(self, path: Path, domain: str) -> DomainSpec | None:
        text = path.read_text(encoding="utf-8")
        lines = text.split("\n")

        domain_class = ""
        structure = ""
        for line in lines[:5]:
            m = re.match(r">\s*Class:\s*(.+?)\s*\|\s*Structure:\s*(.+)", line)
            if m:
                domain_class = m.group(1).strip()
                structure = m.group(2).strip()
                break

        variables: list[VariableSpec] = []
        i = 0
        while i < len(lines):
            # Stop at the "---" separator that precedes the Cross References block.
            # This prevents section headings like "### Controlled Terminology",
            # "### Related Domains", "### General References", "### Model Definition"
            # from being misidentified as variable names.
            if lines[i].startswith("---") or lines[i].startswith("## "):
                break
            m = re.match(r"^### (\w+)", lines[i])
            if m:
                var_name = m.group(1)
                var_fields: dict[str, str] = {}
                i += 1
                while i < len(lines) and not lines[i].startswith("### ") and not lines[i].startswith("---") and not lines[i].startswith("## "):
                    fm = re.match(r"^- \*\*(.+?):\*\*\s*(.*)", lines[i])
                    if fm:
                        var_fields[fm.group(1).strip()] = fm.group(2).strip()
                    i += 1

                order_str = var_fields.get("Order", "0")
                try:
                    order = int(order_str)
                except ValueError:
                    order = 0

                variables.append(
                    VariableSpec(
                        name=var_name,
                        order=order,
                        label=var_fields.get("Label", ""),
                        var_type=var_fields.get("Type", ""),
                        controlled_terms=var_fields.get("Controlled Terms", ""),
                        role=var_fields.get("Role", ""),
                        core=var_fields.get("Core", ""),
                        cdisc_notes=var_fields.get("CDISC Notes", ""),
                    )
                )
            else:
                i += 1

        return DomainSpec(
            domain=domain,
            domain_class=domain_class,
            structure=structure,
            variables=variables,
        )

    # ── Terminology parsing ──────────────────────────────────────────────

    def _load_all_codelists(self) -> dict[str, Codelist]:
        result: dict[str, Codelist] = {}
        term_dir = self.kb_root / "terminology"
        if not term_dir.exists():
            return result

        for md_file in sorted(term_dir.rglob("*.md")):
            for cl in self._parse_terminology(md_file):
                result[cl.code] = cl
        return result

    def _parse_terminology(self, path: Path) -> list[Codelist]:
        text = path.read_text(encoding="utf-8")
        codelists: list[Codelist] = []

        sections = re.split(r"^## ", text, flags=re.MULTILINE)
        for section in sections[1:]:
            lines = section.split("\n")
            heading = lines[0].strip()

            m = re.match(r"(.+?)\s*\(([Cc]\d+)\)", heading)
            if not m:
                continue

            cl_name = m.group(1).strip()
            cl_code = m.group(2).upper()

            extensible = False
            for line in lines[1:6]:
                ext_m = re.match(r"Extensible:\s*(Yes|No)", line, re.IGNORECASE)
                if ext_m:
                    extensible = ext_m.group(1).lower() == "yes"
                    break

            values: list[str] = []
            in_table = False
            value_col_idx = -1
            for line in lines:
                if line.startswith("|") and "CDISC Submission Value" in line:
                    cols = [c.strip() for c in line.split("|")]
                    for idx, col in enumerate(cols):
                        if "CDISC Submission Value" in col:
                            value_col_idx = idx
                            break
                    in_table = True
                    continue
                if in_table and line.startswith("|---"):
                    continue
                if in_table and line.startswith("|"):
                    cols = [c.strip() for c in line.split("|")]
                    if value_col_idx < len(cols):
                        val = cols[value_col_idx].strip()
                        if val:
                            values.append(val)
                elif in_table and not line.strip().startswith("|"):
                    in_table = False

            codelists.append(
                Codelist(
                    code=cl_code,
                    name=cl_name,
                    extensible=extensible,
                    submission_values=values,
                )
            )

        return codelists
