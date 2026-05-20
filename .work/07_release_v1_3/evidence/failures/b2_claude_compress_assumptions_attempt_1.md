# Rule B Failure Archive — B2 Claude compress_assumptions Attempt 1

> Date: 2026-05-20
> Rule B: 失败数据归档，含输入/产物/技术判定/业务判定/下一 attempt 输入

---

## Input

- Script: `ai_platforms/claude_projects/archive/v1/scripts/compress_assumptions.py`
- REPO_ROOT patch: applied (parents[3] → Path("/Users/bojiangzhang/MyProject/sdtm-pedia"))
- DOMAINS list: hardcoded 63 entries (no DI)

## Artifact Produced

- Output: `ai_platforms/claude_projects/output/06_assumptions.md`
- Size: 100,105 bytes
- Domain headers (`## `): 64 lines (misleading — multiple `## ` headings per domain file, not 1 per domain)
- DI-specific header `## DI`: ABSENT
- DI source annotation `<!-- source: .../DI/assumptions.md -->`: ABSENT

## Technical Judgment

**BUG / PRE-EXISTING**: compress_assumptions.py DOMAINS list is hardcoded with 63 entries.
DI was added to `knowledge_base/domains/` in 06 Deep Verification (P6) but was never added
to the DOMAINS list. Same bug as v1.1 release (per `.work/07_release_v1_1/failures/claude_rebuild_failures.md` F1:
"DI INCLUDED — assumptions.md exists" — v1.1 executor patched this inline).

The script does NOT auto-scan the domains directory; it iterates `DOMAINS` list explicitly:
```python
for dom in DOMAINS:
    raw = (SRC_DIR / dom / "assumptions.md").read_text(encoding="utf-8")
```

## Business Judgment

**NOT ACCEPTABLE for v1.3** — DI was included in v1.1's 06_assumptions.md. Shipping v1.3
without DI would be a regression vs v1.1.

## Fix (Attempt 2)

Injected `"DI"` between `"DV"` and `"EC"` in DOMAINS list before exec:
```python
patched = patched.replace('"DI", "DV", "EC"', '"DI", "DV", "EC"')
# actual: replace '"DV", "EC"' with '"DI", "DV", "EC"'
```

Attempt 2 result: rc=0, 64 domain headers, DI present at line 327-328.

## Next Attempt Input

If this bug recurs in future releases: edit `archive/v1/scripts/compress_assumptions.py`
DOMAINS list directly to add DI (and any future new domains) before running. Long-term fix:
replace hardcoded list with `sorted(p.parent.name for p in SRC_DIR.glob("*/assumptions.md"))`.
