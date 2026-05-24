"""Dataset parser for SDTM validation (Phase 1C.1).

Supports CSV, XPT (SAS Transport), SAS7BDAT formats.
Auto-detects domain from DOMAIN column or filename.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB (PLAN R-21 / 1C.1)
MAX_ROWS = 500_000


class ParseError(Exception):
    pass


@dataclass
class DatasetMeta:
    domain: str | None
    file_format: str
    file_path: str
    row_count: int
    col_count: int
    variables: list[str]
    file_size_bytes: int


def parse_file(path: Path | str) -> tuple[pd.DataFrame, DatasetMeta]:
    """Parse a dataset file, return (DataFrame, metadata).

    All column names are uppercased.  CSV is read as str dtype to preserve
    original values; XPT/SAS7BDAT use pyreadstat native types.
    """
    path = Path(path)
    if not path.exists():
        raise ParseError(f"File not found: {path}")

    size = path.stat().st_size
    if size > MAX_FILE_SIZE:
        raise ParseError(
            f"File too large: {size:,} bytes exceeds 100 MB limit. "
            "Consider subsetting your data."
        )
    if size == 0:
        raise ParseError("File is empty (0 bytes).")

    suffix = path.suffix.lower()
    if suffix == ".csv":
        df = _read_csv(path)
        fmt = "csv"
    elif suffix == ".xpt":
        df = _read_xpt(path)
        fmt = "xpt"
    elif suffix == ".sas7bdat":
        df = _read_sas7bdat(path)
        fmt = "sas7bdat"
    else:
        raise ParseError(
            f"Unsupported format: '{suffix}'. Supported: .csv, .xpt, .sas7bdat"
        )

    df.columns = [c.strip().upper() for c in df.columns]
    if len(df) > MAX_ROWS:
        raise ParseError(
            f"Dataset has {len(df):,} rows, exceeds {MAX_ROWS:,} limit."
        )
    domain = _detect_domain(df, path)

    return df, DatasetMeta(
        domain=domain,
        file_format=fmt,
        file_path=str(path),
        row_count=len(df),
        col_count=len(df.columns),
        variables=list(df.columns),
        file_size_bytes=size,
    )


def parse_bytes(data: bytes, filename: str) -> tuple[pd.DataFrame, DatasetMeta]:
    """Parse in-memory bytes (from Streamlit upload). Writes to a temp file."""
    import os
    import stat
    import tempfile

    suffix = Path(filename).suffix.lower()
    if suffix not in (".csv", ".xpt", ".sas7bdat"):
        raise ParseError(
            f"Unsupported format: '{suffix}'. Supported: .csv, .xpt, .sas7bdat"
        )
    if len(data) > MAX_FILE_SIZE:
        raise ParseError(
            f"Upload too large: {len(data):,} bytes exceeds 100 MB limit."
        )

    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        os.chmod(tmp.name, stat.S_IRUSR | stat.S_IWUSR)
        tmp.write(data)
        tmp_path = Path(tmp.name)

    try:
        df, meta = parse_file(tmp_path)
        meta.file_path = filename
        return df, meta
    finally:
        tmp_path.unlink(missing_ok=True)


# ── Format readers ───────────────────────────────────────────────────────


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def _read_xpt(path: Path) -> pd.DataFrame:
    import pyreadstat

    df, _ = pyreadstat.read_xport(str(path))
    return df


def _read_sas7bdat(path: Path) -> pd.DataFrame:
    try:
        import pyreadstat

        df, _ = pyreadstat.read_sas7bdat(str(path))
        return df
    except ImportError:
        pass
    except Exception as e:
        raise ParseError(f"Failed to read SAS7BDAT with pyreadstat: {e}")

    try:
        from sas7bdat import SAS7BDAT

        with SAS7BDAT(str(path)) as f:
            return f.to_data_frame()
    except ImportError:
        raise ParseError(
            "Cannot read SAS7BDAT: neither pyreadstat nor sas7bdat "
            "is installed. Install: pip install pyreadstat"
        )


# ── Domain detection ─────────────────────────────────────────────────────


def _detect_domain(df: pd.DataFrame, path: Path) -> str | None:
    if "DOMAIN" in df.columns:
        vals = df["DOMAIN"].dropna().unique()
        non_empty = [str(v).strip().upper() for v in vals if str(v).strip()]
        if len(non_empty) == 1:
            return non_empty[0]

    stem = path.stem.upper()
    if 2 <= len(stem) <= 4 and stem.isalpha():
        return stem

    return None
