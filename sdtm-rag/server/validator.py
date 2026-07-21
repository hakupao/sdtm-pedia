"""SDTM dataset validator — 7-type rule engine (Phase 1C.2).

Rules (PLAN §5 1C.2 / EXECUTION_PLAN §4 1C.2):
  a. REQ  — Required variable completeness (Core=Req must be present)
  b. EXP  — Expected variable completeness (Core=Exp → WARN if missing)
  c. CT   — Controlled Terminology compliance (C-code codelist value check)
  d. TYPE — Data type validation (Char/Num)
  e. PK   — Primary key uniqueness (STUDYID + USUBJID + --SEQ)
  f. SUBJ — Cross-domain USUBJID check (all subjects in DM)
  g. VAR  — Unknown variable name warning
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from scripts.spec_loader import DomainSpec, SpecLoader


@dataclass
class Finding:
    severity: str  # ERROR, WARN, INFO
    rule: str  # REQ, EXP, CT, TYPE, PK, SUBJ, VAR
    variable: str | None
    message: str
    row_indices: list[int] | None = None
    value_sample: list[str] | None = None

    def to_dict(self) -> dict:
        d: dict = {
            "severity": self.severity,
            "rule": self.rule,
            "variable": self.variable,
            "message": self.message,
        }
        if self.row_indices:
            d["row_indices"] = self.row_indices[:20]
            d["affected_rows"] = len(self.row_indices)
        if self.value_sample:
            d["value_sample"] = self.value_sample[:10]
        return d


@dataclass
class ValidationResult:
    domain: str
    row_count: int
    col_count: int
    findings: list[Finding] = field(default_factory=list)

    @property
    def error_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "ERROR")

    @property
    def warn_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "WARN")

    @property
    def info_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "INFO")

    @property
    def completeness_pct(self) -> float:
        if not self._domain_spec:
            return 0.0
        req = set(self._domain_spec.req_vars())
        if not req:
            return 100.0
        present = req & set(self._present_vars)
        return round(len(present) / len(req) * 100, 1)

    _domain_spec: DomainSpec | None = field(default=None, repr=False)
    _present_vars: list[str] = field(default_factory=list, repr=False)

    def to_dict(self) -> dict:
        return {
            "domain": self.domain,
            "row_count": self.row_count,
            "col_count": self.col_count,
            "completeness_pct": self.completeness_pct,
            "error_count": self.error_count,
            "warn_count": self.warn_count,
            "info_count": self.info_count,
            "findings": [f.to_dict() for f in self.findings],
        }


_NUMERIC_RE = re.compile(r"^-?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$")

MAX_SAMPLE = 10


def validate(
    df: pd.DataFrame,
    domain: str,
    loader: SpecLoader,
    *,
    dm_df: pd.DataFrame | None = None,
) -> ValidationResult:
    """Run all 7 validation rules against a dataset.

    Args:
        df: Dataset DataFrame (columns already uppercased).
        domain: SDTM domain code (e.g. "AE").
        loader: SpecLoader with KB reference data.
        dm_df: Optional DM DataFrame for cross-domain USUBJID check (rule f).

    Returns:
        ValidationResult with all findings.
    """
    domain = domain.upper()
    spec = loader.get_domain(domain)
    result = ValidationResult(
        domain=domain,
        row_count=len(df),
        col_count=len(df.columns),
        _present_vars=list(df.columns),
    )

    if spec is None:
        result.findings.append(
            Finding("WARN", "VAR", None, f"Domain '{domain}' not found in KB. Skipping spec-based checks.")
        )
        return result

    result._domain_spec = spec
    present = set(df.columns)

    _check_req(df, spec, present, result)
    _check_exp(spec, present, result)
    _check_ct(df, spec, loader, present, result)
    _check_type(df, spec, present, result)
    _check_pk(df, spec, domain, present, result)
    _check_usubjid(df, present, dm_df, result)
    _check_varname(df, spec, present, result)

    return result


# ── Rule a: REQ completeness ────────────────────────────────────────────


def _check_req(
    df: pd.DataFrame,
    spec: DomainSpec,
    present: set[str],
    result: ValidationResult,
) -> None:
    if len(df) == 0:
        return
    for var_name in spec.req_vars():
        if var_name not in present:
            result.findings.append(
                Finding("ERROR", "REQ", var_name, f"Required variable '{var_name}' (Core=Req) is missing.")
            )
        else:
            null_count = df[var_name].isna().sum() + (df[var_name].astype(str).str.strip() == "").sum()
            if null_count > 0:
                pct = round(null_count / max(len(df), 1) * 100, 1)
                rows = df.index[df[var_name].isna() | (df[var_name].astype(str).str.strip() == "")].tolist()
                result.findings.append(
                    Finding(
                        "ERROR",
                        "REQ",
                        var_name,
                        f"Required variable '{var_name}' has {null_count} null/empty values ({pct}%).",
                        row_indices=rows,
                    )
                )


# ── Rule b: EXP completeness ────────────────────────────────────────────


def _check_exp(
    spec: DomainSpec,
    present: set[str],
    result: ValidationResult,
) -> None:
    for var_name in spec.exp_vars():
        if var_name not in present:
            result.findings.append(
                Finding("WARN", "EXP", var_name, f"Expected variable '{var_name}' (Core=Exp) is missing.")
            )


# ── Rule c: CT compliance ───────────────────────────────────────────────


def _check_ct(
    df: pd.DataFrame,
    spec: DomainSpec,
    loader: SpecLoader,
    present: set[str],
    result: ValidationResult,
) -> None:
    for v in spec.variables:
        ct_ref = v.controlled_terms.strip()
        if not ct_ref or v.name not in present:
            continue

        if not loader.is_ct_code(ct_ref):
            if ct_ref.upper() == "MEDDRA":
                result.findings.append(
                    Finding("INFO", "CT", v.name, f"'{v.name}' uses MedDRA coding (external dictionary, not validated).")
                )
            continue

        codelist = loader.get_codelist(ct_ref)
        if codelist is None:
            result.findings.append(
                Finding("INFO", "CT", v.name, f"Codelist {ct_ref} for '{v.name}' not found in KB terminology.")
            )
            continue

        allowed = set(codelist.submission_values)
        col_vals = df[v.name].dropna().astype(str).str.strip()
        col_vals = col_vals[col_vals != ""]
        if col_vals.empty:
            continue

        invalid = col_vals[~col_vals.isin(allowed)]
        if invalid.empty:
            continue

        invalid_unique = sorted(invalid.unique().tolist())
        bad_rows = invalid.index.tolist()

        if codelist.extensible:
            result.findings.append(
                Finding(
                    "INFO",
                    "CT",
                    v.name,
                    f"'{v.name}' has {len(invalid_unique)} value(s) not in extensible "
                    f"codelist {ct_ref} ({codelist.name}). May be sponsor-defined.",
                    row_indices=bad_rows,
                    value_sample=invalid_unique[:MAX_SAMPLE],
                )
            )
        else:
            result.findings.append(
                Finding(
                    "ERROR",
                    "CT",
                    v.name,
                    f"'{v.name}' has {len(invalid_unique)} value(s) not in non-extensible "
                    f"codelist {ct_ref} ({codelist.name}): {invalid_unique[:5]}",
                    row_indices=bad_rows,
                    value_sample=invalid_unique[:MAX_SAMPLE],
                )
            )


# ── Rule d: TYPE check ──────────────────────────────────────────────────


def _check_type(
    df: pd.DataFrame,
    spec: DomainSpec,
    present: set[str],
    result: ValidationResult,
) -> None:
    for v in spec.variables:
        if v.name not in present or v.var_type not in ("Char", "Num"):
            continue

        col = df[v.name].dropna()
        if col.empty:
            continue

        if v.var_type == "Num":
            str_vals = col.astype(str).str.strip()
            non_empty = str_vals[str_vals != ""]
            if non_empty.empty:
                continue
            non_numeric = non_empty[~non_empty.apply(lambda x: bool(_NUMERIC_RE.match(x)))]
            if not non_numeric.empty:
                bad_vals = sorted(non_numeric.unique().tolist())
                result.findings.append(
                    Finding(
                        "ERROR",
                        "TYPE",
                        v.name,
                        f"'{v.name}' is typed Num but has {len(non_numeric)} non-numeric value(s).",
                        row_indices=non_numeric.index.tolist(),
                        value_sample=bad_vals[:MAX_SAMPLE],
                    )
                )


# ── Rule e: PK uniqueness ───────────────────────────────────────────────


def _check_pk(
    df: pd.DataFrame,
    spec: DomainSpec,
    domain: str,
    present: set[str],
    result: ValidationResult,
) -> None:
    pk_cols: list[str] = []
    for base in ("STUDYID", "USUBJID"):
        if base in present:
            pk_cols.append(base)

    seq_var = spec.seq_variable()
    if seq_var and seq_var in present:
        pk_cols.append(seq_var)

    if len(pk_cols) < 2:
        result.findings.append(
            Finding(
                "INFO",
                "PK",
                None,
                f"Cannot check primary key: need at least STUDYID+USUBJID, found {pk_cols}.",
            )
        )
        return

    dupes = df[df.duplicated(subset=pk_cols, keep=False)]
    if not dupes.empty:
        n_dupe_groups = df[pk_cols].duplicated(keep="first").sum()
        result.findings.append(
            Finding(
                "ERROR",
                "PK",
                "+".join(pk_cols),
                f"Primary key ({'+'.join(pk_cols)}) has {n_dupe_groups} duplicate key(s) "
                f"({len(dupes)} total rows).",
                row_indices=dupes.index.tolist(),
            )
        )
    else:
        result.findings.append(
            Finding("INFO", "PK", "+".join(pk_cols), f"Primary key ({'+'.join(pk_cols)}) is unique. OK.")
        )


# ── Rule f: USUBJID cross-domain ────────────────────────────────────────


def _check_usubjid(
    df: pd.DataFrame,
    present: set[str],
    dm_df: pd.DataFrame | None,
    result: ValidationResult,
) -> None:
    if "USUBJID" not in present:
        return

    if dm_df is None:
        result.findings.append(
            Finding("INFO", "SUBJ", "USUBJID", "No DM dataset provided; cross-domain USUBJID check skipped.")
        )
        return

    dm_cols_upper = [c.upper() for c in dm_df.columns]
    if "USUBJID" not in dm_cols_upper:
        result.findings.append(
            Finding("WARN", "SUBJ", "USUBJID", "DM dataset does not contain USUBJID column.")
        )
        return

    usubjid_col = dm_df.columns[dm_cols_upper.index("USUBJID")]
    dm_subjects = set(dm_df[usubjid_col].dropna().astype(str).str.strip())

    ds_subjects = set(df["USUBJID"].dropna().astype(str).str.strip())
    missing = ds_subjects - dm_subjects

    if missing:
        result.findings.append(
            Finding(
                "ERROR",
                "SUBJ",
                "USUBJID",
                f"{len(missing)} subject(s) in dataset not found in DM.",
                value_sample=sorted(missing)[:MAX_SAMPLE],
            )
        )
    else:
        result.findings.append(
            Finding(
                "INFO",
                "SUBJ",
                "USUBJID",
                f"All {len(ds_subjects)} subject(s) found in DM. OK.",
            )
        )


# ── Rule g: unknown variable names ──────────────────────────────────────


def _check_varname(
    df: pd.DataFrame,
    spec: DomainSpec,
    present: set[str],
    result: ValidationResult,
) -> None:
    known = spec.var_names()
    unknown = present - known

    supp_re = re.compile(r"^SUPP[A-Z]{2}")
    for var in sorted(unknown):
        if var in ("DOMAIN",):
            continue
        if supp_re.match(var):
            result.findings.append(
                Finding("INFO", "VAR", var, f"'{var}' looks like a SUPP-- variable (supplemental qualifier).")
            )
        else:
            result.findings.append(
                Finding("WARN", "VAR", var, f"'{var}' is not defined in the {spec.domain} spec.")
            )
