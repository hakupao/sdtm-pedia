"""KG-lite data layer: load data/meta/meta.yaml (SP1 output) once, build in-memory
reverse indices, expose deterministic query API. No networkx (that is SP3); pure dict
indices. Forward data is read-only after init; reverse indices are derived, never
materialised back to meta.yaml (avoids double-write drift, SP1 spec §3 detail e)."""
from __future__ import annotations

from pathlib import Path

import yaml


class MetaStore:
    def __init__(self, meta_path: Path):
        data = yaml.safe_load(Path(meta_path).read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(
                f"meta.yaml must be a YAML mapping; got {type(data).__name__}"
            )
        _required = {"meta_version", "domains", "codelists", "model_defhome"}
        _missing = _required - data.keys()
        if _missing:
            raise ValueError(
                f"meta.yaml is missing required top-level keys: {sorted(_missing)}"
            )
        self.meta_version: int = data["meta_version"]
        self._domains: list[dict] = data["domains"]
        self._codelists: list[dict] = data["codelists"]
        self._model_defhome: dict[str, str] = data["model_defhome"]
        # only domains that count toward the canonical 63 (DI stub excluded)
        self._real_domains: list[dict] = [d for d in self._domains if d["counts_toward_63"]]
        self._build_indices()

    def _build_indices(self) -> None:
        # var name -> sorted list of domain codes (counts_toward_63 domains only,
        # matching VARIABLE_INDEX coverage that reconcile verified TAETORD->43)
        self._var_to_domains: dict[str, list[str]] = {}
        # var name -> attribute dict (first occurrence only).
        # NOTE: role and core can legitimately differ across domains (~9 and ~13
        # variables respectively; e.g. USUBJID is Req in some domains and Exp in
        # others; TAETORD is Perm in most but Req in a few).  label diverges for ~2.
        # This dict stores the FIRST-SEEN value; domain-specific attributes are out
        # of scope for Phase 1 and deferred to SP3.
        self._var_attrs: dict[str, dict] = {}
        # domain code -> ordered list of variable names
        self._domain_to_vars: dict[str, list[str]] = {}
        # ct_code -> list of (domain, var) where it is referenced
        self._ctcode_to_locations: dict[str, list[tuple[str, str]]] = {}
        tmp_var_domains: dict[str, set[str]] = {}
        for d in self._real_domains:
            dom = d["domain"]
            self._domain_to_vars[dom] = [v["name"] for v in d["variables"]]
            for v in d["variables"]:
                name = v["name"]
                tmp_var_domains.setdefault(name, set()).add(dom)
                self._var_attrs.setdefault(name, {
                    "label": v["label"], "role": v["role"], "type": v["type"],
                    "core": v["core"], "ct_codes": list(v["ct_codes"]),
                })
                for code in v["ct_codes"]:
                    self._ctcode_to_locations.setdefault(code, []).append((dom, name))
        self._var_to_domains = {k: sorted(v) for k, v in tmp_var_domains.items()}
        # domain code -> domain dict (real domains only)
        self._domain_by_code: dict[str, dict] = {d["domain"]: d for d in self._real_domains}
        # codelist code -> codelist dict
        self._codelist_by_code: dict[str, dict] = {c["ct_code"]: c for c in self._codelists}
        self.known_variables: frozenset[str] = frozenset(self._var_to_domains)
        self.known_domains: frozenset[str] = frozenset(self._domain_to_vars)
        self.known_ctcodes: frozenset[str] = frozenset(self._codelist_by_code)

    # ── deterministic query API (Phase 1) ──
    def domains_for_variable(self, var: str) -> list[str]:
        return list(self._var_to_domains.get(var.upper(), []))

    def variable_attributes(self, var: str) -> dict | None:
        a = self._var_attrs.get(var.upper())
        if a is None:
            return None
        # Return a shallow copy with ct_codes re-listed so callers cannot mutate
        # the internal index by appending to the returned list.
        return {**a, "ct_codes": list(a["ct_codes"])}

    def variables_in_domain(self, dom: str) -> list[str]:
        return list(self._domain_to_vars.get(dom.upper(), []))

    def codelist(self, ct_code: str) -> dict | None:
        c = self._codelist_by_code.get(ct_code.upper())
        return dict(c) if c is not None else None

    def locations_for_codelist(self, ct_code: str) -> list[tuple[str, str]]:
        return list(self._ctcode_to_locations.get(ct_code.upper(), []))

    def domains_for_codelist(self, ct_code: str) -> list[str]:
        return sorted({dom for dom, _ in self.locations_for_codelist(ct_code)})

    def variables_for_codelist(self, ct_code: str) -> list[str]:
        return sorted({var for _, var in self.locations_for_codelist(ct_code)})

    def domain_info(self, dom: str) -> dict | None:
        d = self._domain_by_code.get(dom.upper())
        if d is None:
            return None
        return {
            "domain": d["domain"],
            "class": d["class"],
            "label": d["label"],
            "structure": d["structure"],
            "n_variables": len(d["variables"]),
        }

    def model_defhome(self, var: str) -> str | None:
        return self._model_defhome.get(var.upper())

    @property
    def n_domains(self) -> int:
        return len(self._real_domains)

    @property
    def n_variable_entries(self) -> int:
        return sum(len(d["variables"]) for d in self._real_domains)

    @property
    def n_unique_variables(self) -> int:
        names: set[str] = set()
        for d in self._real_domains:
            names.update(v["name"] for v in d["variables"])
        return len(names)
