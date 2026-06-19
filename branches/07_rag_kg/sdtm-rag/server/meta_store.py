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
        self.meta_version: int = data["meta_version"]
        self._domains: list[dict] = data["domains"]
        self._codelists: list[dict] = data["codelists"]
        self._model_defhome: dict[str, str] = data["model_defhome"]
        # only domains that count toward the canonical 63 (DI stub excluded)
        self._real_domains: list[dict] = [d for d in self._domains if d["counts_toward_63"]]
        self._build_indices()

    def _build_indices(self) -> None:  # filled in Task 2
        pass

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
