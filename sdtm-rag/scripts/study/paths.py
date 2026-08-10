"""st01 研究路径解析: 真名只存在于本地 studies.local.yaml, 代码只认代号."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import cast

import yaml

SDTM_RAG_ROOT = Path(__file__).resolve().parent.parent.parent
STUDY_DATA_ROOT = SDTM_RAG_ROOT / "data" / "study"
DEFAULT_REGISTRY = STUDY_DATA_ROOT / "studies.local.yaml"


@dataclass(frozen=True)
class StudyPaths:
    study_id: str
    version_label_new: str
    version_label_old: str | None
    config_report_new: Path
    config_report_old: Path | None
    demo_export: Path | None
    out_dir: Path
    cards_dir: Path
    # C1 文档轨: registry 里 doc_pdfs 缺省时为空 tuple, xlsx 轨照跑不误.
    doc_pdfs: tuple[Path, ...] = ()

    @property
    def docs_dir(self) -> Path:
        """章节 chunk 输出目录. 用 property 而非字段: 不可能与 out_dir 失同步, 且类型不必 Optional."""
        return self.out_dir / "docs"


def resolve_study(study_id: str, registry_path: Path | str | None = None) -> StudyPaths:
    reg_path = Path(registry_path) if registry_path is not None else DEFAULT_REGISTRY
    if not reg_path.is_file():
        raise FileNotFoundError(f"study registry not found: {reg_path}")
    registry = yaml.safe_load(reg_path.read_text(encoding="utf-8")) or {}
    if study_id not in registry:
        raise KeyError(f"unknown study_id: {study_id} (known: {sorted(registry)})")
    ent = registry[study_id]
    source_dir = Path(ent["source_dir"])
    if not source_dir.is_absolute():
        source_dir = (reg_path.parent / source_dir).resolve()

    def _file(key: str, required: bool) -> Path | None:
        name = ent.get(key)
        if not name:
            if required:
                raise KeyError(f"{study_id}: registry missing required key {key}")
            return None
        p = source_dir / name
        if not p.exists():
            raise FileNotFoundError(f"{study_id}: {key} not found: {p}")
        return p

    out_dir = ((reg_path.parent if registry_path is not None else STUDY_DATA_ROOT) / study_id).resolve()
    # Safety check: when using default registry (production), ensure out_dir is within STUDY_DATA_ROOT
    if registry_path is None and not out_dir.is_relative_to(STUDY_DATA_ROOT):
        raise RuntimeError(
            f"out_dir={out_dir} not within STUDY_DATA_ROOT={STUDY_DATA_ROOT}"
        )

    doc_pdfs: list[Path] = []
    for name in ent.get("doc_pdfs", []) or []:
        p = source_dir / name
        if not p.is_file():
            raise FileNotFoundError(f"{study_id}: doc pdf not found: {p}")
        doc_pdfs.append(p)

    return StudyPaths(
        study_id=study_id,
        version_label_new=ent["version_label_new"],
        version_label_old=ent.get("version_label_old"),
        config_report_new=cast(Path, _file("config_report_new", required=True)),
        config_report_old=_file("config_report_old", required=False),
        demo_export=_file("demo_export", required=False),
        out_dir=out_dir,
        cards_dir=out_dir / "cards",
        doc_pdfs=tuple(doc_pdfs),
    )
