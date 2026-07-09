# SP5 图增强校验器 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 给现有 Validator 加 DESIGN §5.6 三类图增强校验 (impact advisory / cross-domain completeness / CT cascade), 对多域 study 上传做确定性跨域校验, 拿内存 GraphEngine 当权威参照。

**Architecture:** 新 `server/graph_validator.py` (3 纯函数 + `run_graph_checks`, 只读 GraphEngine) → 新 `POST /api/validate-study` (收多文件, 逐域 validate() + 跑跨域 check) → `report.generate_study_json` 聚合 → Streamlit 多文件 UI。单域 `/api/validate` 不动。不碰 Neo4j。

**Tech Stack:** Python 3.11 (`.venv`), pandas, 现有 `server.validator.Finding`/`ValidationResult`/`validate`, `server.graph_engine.GraphEngine` + `server.meta_store.MetaStore`, FastAPI, Streamlit, pytest。

## Global Constraints

- 相对路径基准 = `branches/07_rag_kg/sdtm-rag/`; Run 命令先 `cd branches/07_rag_kg/sdtm-rag`; Python 一律 `.venv/bin/python` / `.venv/bin/pytest`。
- 全 advisory 基调: graph findings **只用 WARN/INFO, 绝不 ERROR** (避免误报 + curated 关系 LOW fidelity)。
- 复用现有 `Finding` dataclass (不新建), graph 规则码: `GIMPACT` / `GXDOM` / `GCASCADE`。
- 单域 `validate()` 路径**零回归** (现有 `test_validator.py` 37 测试必须仍绿)。
- 确定性: graph_validator 只读 GraphEngine/MetaStore, 不改数据、不引 Neo4j、不调 LLM。
- 反过拟合: Rule A 独立核 (Task 8) 对照 raw meta.yaml 手算期望, 不复用 graph_validator 代码。
- 规则 B 失败归档 `evidence/failures/sp5_attempt_*.md`; 规则 C `RETROSPECTIVE_sp5.md`; 规则 D Task 8 异 subagent_type。
- 每 task 结尾 commit (git 在 repo root)。

## 关键接口 (探索实测, 逐字)

```python
# server/validator.py
@dataclass
class Finding:
    severity: str; rule: str; variable: str | None; message: str
    row_indices: list[int] | None = None; value_sample: list[str] | None = None
    def to_dict(self) -> dict: ...
def validate(df, domain: str, loader, *, dm_df=None) -> ValidationResult  # findings via mutation
# ValidationResult: domain,row_count,col_count,findings[],.error_count/.warn_count/.info_count/.completeness_pct/.to_dict()

# server/report.py
@dataclass
class FullReport:
    domain:str; file_path:str; row_count:int; col_count:int; completeness_pct:float
    validation: ValidationResult; review: ReviewResult | None; generated_at:str=<auto>
    # @property total_errors/total_warnings/total_info/verdict
def generate_json(report: FullReport) -> dict
# report.py 顶部已: from server.validator import Finding, ValidationResult

# server/meta_store.py  (engine.store)
store.relations_curated(dom) -> list[dict{target,mechanism,category,note,fidelity}]  # mechanism 可 None
store.ct_codes_for_variable(var) -> list[str]        # 跨域 union
store.codelist(ct_code) -> dict|None                 # 有 "name"
# server/graph_engine.py
engine.impact_of_variable(var) -> dict|None          # {"var","domains","n_domains"}
engine.impact_of_codelist(code) -> dict|None         # {"code","name","domains","variables","n_domains","n_variables"}
# 构造: store=MetaStore(settings.meta_path); engine=GraphEngine(store)

# scripts/parse_dataset.py
parse_bytes(data: bytes, filename: str) -> (pd.DataFrame, DatasetMeta)  # 列已 uppercase
# DatasetMeta: domain,file_format,file_path,row_count,col_count,variables,file_size_bytes
# ⚠️ 上传文件 domain 只能靠 DOMAIN 列自动检测 (tempfile 名使文件名检测失效) → study 每文件须有 DOMAIN 列

# server/router.py
api_router = APIRouter(prefix="/api")   # /validate 端点内 lazy import; spec_loader = request.app.state.spec_loader
```

测试约定: `scripts/tests/`, conftest 已设 sys.path, `from server.xxx import ...`; MetaStore fixture = `MetaStore(settings.meta_path)` (from server.config import settings); 跑 `.venv/bin/python -m pytest scripts/tests/test_xxx.py -v`。

## Task 总览

1. `check_completeness` — RELREC 跨域完整性 (TDD, 含 back-fill)
2. `check_ct_cascade` — 共享 codelist 跨域值一致 (TDD)
3. `check_impact` advisory + `run_graph_checks` 汇总 (TDD)
4. 合成 study fixture + 端到端 golden
5. `report.generate_study_json` + study verdict (TDD)
6. `POST /api/validate-study` 端点
7. Streamlit 多文件 study UI
8. Rule D + Rule A + 收口

---

### Task 1: `check_completeness` — RELREC 跨域完整性 (TDD)

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/server/graph_validator.py`
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_validator.py`

**Interfaces:**
- Consumes: `GraphEngine` (engine.store.relations_curated)
- Produces: `check_completeness(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]` (datasets 键=大写域码); 模块常量 `IMPACT_DOMAIN_THRESHOLD = 10`

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_graph_validator.py`:

```python
"""SP5 graph validator — cross-domain checks over meta.yaml (deterministic, no Neo4j)."""
from __future__ import annotations

import pandas as pd
import pytest

from server.config import settings
from server.graph_engine import GraphEngine
from server.graph_validator import check_completeness
from server.meta_store import MetaStore


@pytest.fixture(scope="module")
def engine():
    return GraphEngine(MetaStore(settings.meta_path))


def _df(domain: str) -> pd.DataFrame:
    return pd.DataFrame({"STUDYID": ["S1"], "DOMAIN": [domain], "USUBJID": ["S1-1"]})


def test_completeness_flags_missing_relrec_target(engine):
    # AE is curated-related to CM via mechanism RELREC (meta.yaml). Submit AE without CM.
    findings = check_completeness({"AE": _df("AE")}, engine)
    assert any(f.rule == "GXDOM" and "CM" in f.message for f in findings)
    assert all(f.severity == "WARN" for f in findings)


def test_completeness_silent_when_target_present(engine):
    findings = check_completeness({"AE": _df("AE"), "CM": _df("CM")}, engine)
    assert not any("CM" in f.message for f in findings)


def test_completeness_unknown_domain_no_crash(engine):
    assert check_completeness({"ZZ": _df("ZZ")}, engine) == []
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd branches/07_rag_kg/sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_graph_validator.py -v`
Expected: FAIL, `ModuleNotFoundError: No module named 'server.graph_validator'`

- [ ] **Step 3: 写实现**

`server/graph_validator.py`:

```python
"""SP5 graph-augmented validation (DESIGN §5.6): cross-domain checks for an
uploaded SDTM study, using the in-memory GraphEngine (meta.yaml) as the reference.
Deterministic, read-only, no Neo4j, no LLM. All findings are advisory (WARN/INFO).
"""
from __future__ import annotations

import pandas as pd

from server.graph_engine import GraphEngine
from server.validator import Finding

IMPACT_DOMAIN_THRESHOLD = 10
_RELATIONSHIP_DATASETS = {"RELREC", "RELSPEC", "RELSUB"}


def check_completeness(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """WARN when a submitted domain is RELREC-linked to a target domain absent from
    the submission. mechanism==None is back-filled to the target when the target is
    itself a relationship dataset (deterministic structural inference, SP5-local)."""
    submitted = {d.upper() for d in datasets}
    findings: list[Finding] = []
    for dom in sorted(submitted):
        for rel in engine.store.relations_curated(dom):
            target = str(rel["target"]).upper()
            mech = rel.get("mechanism")
            if mech is None and target in _RELATIONSHIP_DATASETS:
                mech = target
            if mech == "RELREC" and target not in submitted:
                findings.append(Finding(
                    "WARN", "GXDOM", None,
                    f"Domain {dom} is RELREC-linked to {target}, but {target} "
                    f"is not present in this study submission.",
                ))
    return findings
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_validator.py -v`
Expected: 3 passed。补 `.venv/bin/ruff check server/graph_validator.py scripts/tests/test_graph_validator.py` + `.venv/bin/mypy server/graph_validator.py` 干净。

> 若 `test_completeness_flags_missing_relrec_target` FAIL (AE 无 RELREC→CM 边): 说明 meta.yaml 该边 mechanism 非 "RELREC" 或 target 非 CM。先 `.venv/bin/python -c "from server.meta_store import MetaStore; from server.config import settings; import json; print(json.dumps(MetaStore(settings.meta_path).relations_curated('AE'), ensure_ascii=False))"` 看真实边, 按实测的 (dom, mechanism=='RELREC', target) 改测试期望的域/target (不许改实现去凑), 归档 `evidence/failures/sp5_attempt_1.md`。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/graph_validator.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_validator.py
git commit -m "feat(sp5): check_completeness — RELREC cross-domain completeness (WARN advisory, back-fill)"
```

---

### Task 2: `check_ct_cascade` — 共享 codelist 跨域值一致 (TDD)

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/server/graph_validator.py`
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_validator.py` (追加)

**Interfaces:**
- Consumes: `engine.store.ct_codes_for_variable(var)`, `engine.store.codelist(ct)`
- Produces: `check_ct_cascade(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]`

- [ ] **Step 1: 写失败测试** (追加)

```python
from server.graph_validator import check_ct_cascade


def test_ct_cascade_flags_inconsistent_values(engine):
    # AESER + MHSER both bind codelist C66742 (No Yes Response). Give them different value sets.
    ae = pd.DataFrame({"DOMAIN": ["AE", "AE"], "AESER": ["Y", "N"]})
    mh = pd.DataFrame({"DOMAIN": ["MH"], "MHSER": ["U"]})
    findings = check_ct_cascade({"AE": ae, "MH": mh}, engine)
    assert any(f.rule == "GCASCADE" and "C66742" in f.message for f in findings)
    assert all(f.severity == "WARN" for f in findings)


def test_ct_cascade_silent_when_consistent(engine):
    ae = pd.DataFrame({"DOMAIN": ["AE"], "AESER": ["Y"]})
    mh = pd.DataFrame({"DOMAIN": ["MH"], "MHSER": ["Y"]})
    assert check_ct_cascade({"AE": ae, "MH": mh}, engine) == []


def test_ct_cascade_silent_single_domain(engine):
    ae = pd.DataFrame({"DOMAIN": ["AE"], "AESER": ["Y", "N"]})
    assert check_ct_cascade({"AE": ae}, engine) == []
```

> 注: `AESER`/`MHSER` 均绑 C66742 是探索实测 (most_shared top-1, 123 变量含 AE/MH 的 SER 变量)。Step 3 后若测试因具体变量不绑 C66742 而 FAIL, 用 `.venv/bin/python -c "from server.meta_store import MetaStore; from server.config import settings; s=MetaStore(settings.meta_path); print(s.ct_codes_for_variable('AESER'), s.ct_codes_for_variable('MHSER'))"` 核实, 换一对同绑同一 codelist 的真实变量 (归档 sp5_attempt_N)。

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_validator.py -k ct_cascade -v`
Expected: FAIL, `ImportError: cannot import name 'check_ct_cascade'`

- [ ] **Step 3: 写实现** (追加到 graph_validator.py)

```python
def check_ct_cascade(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """WARN when the distinct actual values used for a shared codelist differ across
    domains (a codelist used by >=2 submitted domains should have a consistent value
    domain). Advisory only — different coverage is legitimate, hence WARN not ERROR."""
    cascade: dict[str, dict[str, set[str]]] = {}
    for dom, df in datasets.items():
        dom = dom.upper()
        for col in df.columns:
            for ct in engine.store.ct_codes_for_variable(str(col).upper()):
                vals = {str(v).strip() for v in df[col].dropna().unique() if str(v).strip()}
                if vals:
                    cascade.setdefault(ct, {}).setdefault(dom, set()).update(vals)
    findings: list[Finding] = []
    for ct in sorted(cascade):
        dom_vals = cascade[ct]
        if len(dom_vals) < 2:
            continue
        union = set().union(*dom_vals.values())
        if any(vals != union for vals in dom_vals.values()):
            cl = engine.store.codelist(ct)
            name = cl["name"] if cl else ct
            detail = "; ".join(f"{d}={sorted(v)}" for d, v in sorted(dom_vals.items()))
            findings.append(Finding(
                "WARN", "GCASCADE", None,
                f"Codelist {ct} ({name}) has inconsistent values across domains: {detail}",
            ))
    return findings
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_validator.py -v`
Expected: 6 passed。ruff + mypy 干净。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/graph_validator.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_validator.py
git commit -m "feat(sp5): check_ct_cascade — shared-codelist cross-domain value consistency (WARN)"
```

---

### Task 3: `check_impact` advisory + `run_graph_checks` 汇总 (TDD)

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/server/graph_validator.py`
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_validator.py` (追加)

**Interfaces:**
- Consumes: `engine.impact_of_variable(var)`, `engine.impact_of_codelist(ct)`
- Produces: `check_impact(datasets, engine) -> list[Finding]` (INFO); `run_graph_checks(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]` (三者汇总)

- [ ] **Step 1: 写失败测试** (追加)

```python
from server.graph_validator import check_impact, run_graph_checks


def test_impact_flags_high_impact_variable(engine):
    # USUBJID appears in 55 domains (>= threshold 10) — high impact INFO.
    df = pd.DataFrame({"DOMAIN": ["AE"], "USUBJID": ["S1-1"], "AESER": ["Y"]})
    findings = check_impact({"AE": df}, engine)
    assert any(f.rule == "GIMPACT" and f.variable == "USUBJID" for f in findings)
    assert all(f.severity == "INFO" for f in findings)


def test_impact_silent_low_impact_variable(engine):
    # AETERM is AE-specific (1 domain) — below threshold, no impact finding for it.
    df = pd.DataFrame({"DOMAIN": ["AE"], "AETERM": ["headache"]})
    findings = check_impact({"AE": df}, engine)
    assert not any(f.variable == "AETERM" for f in findings)


def test_run_graph_checks_merges_all_three(engine):
    ae = pd.DataFrame({"DOMAIN": ["AE"], "USUBJID": ["S1-1"], "AESER": ["Y", "N"]})
    mh = pd.DataFrame({"DOMAIN": ["MH"], "MHSER": ["U"]})
    findings = run_graph_checks({"AE": ae, "MH": mh}, engine)
    rules = {f.rule for f in findings}
    assert {"GIMPACT", "GXDOM", "GCASCADE"} <= rules
    assert not any(f.severity == "ERROR" for f in findings)  # advisory only
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_validator.py -k "impact or run_graph" -v`
Expected: FAIL, `ImportError: cannot import name 'check_impact'`

- [ ] **Step 3: 写实现** (追加)

```python
def check_impact(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """INFO advisory: flag high-impact variables/codelists present in the data
    (a variable or its codelist spanning >= IMPACT_DOMAIN_THRESHOLD domains) so the
    user knows changes there have wide cross-domain effect. Never pass/fail."""
    findings: list[Finding] = []
    for dom in sorted(datasets):
        df = datasets[dom]
        seen_vars: set[str] = set()
        seen_cts: set[str] = set()
        for col in df.columns:
            var = str(col).upper()
            if var not in seen_vars:
                seen_vars.add(var)
                iv = engine.impact_of_variable(var)
                if iv and iv["n_domains"] >= IMPACT_DOMAIN_THRESHOLD:
                    findings.append(Finding(
                        "INFO", "GIMPACT", var,
                        f"{var} is high-impact: appears in {iv['n_domains']} domains; "
                        f"changes have wide cross-domain effect.",
                    ))
            for ct in engine.store.ct_codes_for_variable(var):
                if ct in seen_cts:
                    continue
                seen_cts.add(ct)
                ic = engine.impact_of_codelist(ct)
                if ic and ic["n_domains"] >= IMPACT_DOMAIN_THRESHOLD:
                    findings.append(Finding(
                        "INFO", "GIMPACT", var,
                        f"Codelist {ct} ({ic['name']}) used by {var} is high-impact: "
                        f"{ic['n_domains']} domains / {ic['n_variables']} variables.",
                    ))
    return findings


def run_graph_checks(datasets: dict[str, pd.DataFrame], engine: GraphEngine) -> list[Finding]:
    """Run all three SP5 graph checks over a submitted study. Returns merged findings
    (all WARN/INFO). datasets maps uppercase domain code -> its DataFrame."""
    return (
        check_impact(datasets, engine)
        + check_completeness(datasets, engine)
        + check_ct_cascade(datasets, engine)
    )
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_validator.py -v`
Expected: 9 passed。ruff + mypy 干净。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/graph_validator.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_validator.py
git commit -m "feat(sp5): check_impact advisory + run_graph_checks (merge all 3, advisory-only)"
```

---

### Task 4: 合成 study fixture + 端到端 golden

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/scripts/tests/fixtures/sp5_study/{ae,cm,mh}_pass.csv` + `{ae,mh}_fail.csv`
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_validator_e2e.py`

**Interfaces:**
- Consumes: `run_graph_checks`, fixture CSV
- Produces: 端到端 golden 断言 (pass 版 0 GXDOM/GCASCADE; fail 版精确命中 GXDOM + GCASCADE)

- [ ] **Step 1: 写 fixture CSV**

`scripts/tests/fixtures/sp5_study/ae_pass.csv`:
```csv
STUDYID,DOMAIN,USUBJID,AESEQ,AESER
S1,AE,S1-001,1,Y
S1,AE,S1-002,1,Y
```
`cm_pass.csv`:
```csv
STUDYID,DOMAIN,USUBJID,CMSEQ,CMTRT
S1,CM,S1-001,1,ASPIRIN
```
`mh_pass.csv`:
```csv
STUDYID,DOMAIN,USUBJID,MHSEQ,MHSER
S1,MH,S1-001,1,Y
```
`ae_fail.csv` (study 不含 CM → completeness WARN; AESER 值域 {Y,N} 与 mh_fail 冲突):
```csv
STUDYID,DOMAIN,USUBJID,AESEQ,AESER
S1,AE,S1-001,1,Y
S1,AE,S1-002,1,N
```
`mh_fail.csv` (MHSER 用额外值 U, 制造跨域不一致):
```csv
STUDYID,DOMAIN,USUBJID,MHSEQ,MHSER
S1,MH,S1-001,1,U
```

> pass 版共享 codelist C66742 的值须一致: ae_pass 全 Y, mh_pass 全 Y → 无 GCASCADE。若实测 AESER/MHSER 不绑 C66742 (Task 2 已核实), 用 Task 2 换定的那对变量重造 fixture 列名。

- [ ] **Step 2: 写 golden 测试**

`scripts/tests/test_graph_validator_e2e.py`:

```python
"""SP5 end-to-end golden: run_graph_checks over a synthetic study fixture."""
from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from server.config import settings
from server.graph_engine import GraphEngine
from server.graph_validator import run_graph_checks
from server.meta_store import MetaStore

FIX = Path(__file__).resolve().parent / "fixtures" / "sp5_study"


@pytest.fixture(scope="module")
def engine():
    return GraphEngine(MetaStore(settings.meta_path))


def _load(name: str) -> pd.DataFrame:
    df = pd.read_csv(FIX / name, dtype=str, keep_default_na=False)
    df.columns = [c.upper() for c in df.columns]
    return df


def test_pass_study_no_completeness_or_cascade_warns(engine):
    study = {"AE": _load("ae_pass.csv"), "CM": _load("cm_pass.csv"), "MH": _load("mh_pass.csv")}
    findings = run_graph_checks(study, engine)
    assert not any(f.rule == "GXDOM" for f in findings)     # CM present -> no missing RELREC target
    assert not any(f.rule == "GCASCADE" for f in findings)  # AESER/MHSER consistent
    assert all(f.severity in ("INFO", "WARN") for f in findings)


def test_fail_study_hits_completeness_and_cascade(engine):
    study = {"AE": _load("ae_fail.csv"), "MH": _load("mh_fail.csv")}  # no CM; AESER {Y,N} vs MHSER {U}
    findings = run_graph_checks(study, engine)
    assert any(f.rule == "GXDOM" and "CM" in f.message for f in findings)
    assert any(f.rule == "GCASCADE" and "C66742" in f.message for f in findings)
    assert not any(f.severity == "ERROR" for f in findings)
```

- [ ] **Step 3: 跑测试**

Run: `.venv/bin/python -m pytest scripts/tests/test_graph_validator_e2e.py -v`
Expected: 2 passed。

> 若 pass 版误报 GCASCADE: 调 fixture 让共享 codelist 值域一致 (改 fixture 数据不改实现)。归档 sp5_attempt_N 若反复。

- [ ] **Step 4: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/scripts/tests/fixtures/sp5_study branches/07_rag_kg/sdtm-rag/scripts/tests/test_graph_validator_e2e.py
git commit -m "test(sp5): synthetic study fixture + end-to-end golden (pass clean, fail hits GXDOM+GCASCADE)"
```

---

### Task 5: `report.generate_study_json` + study verdict (TDD)

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/server/report.py`
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_report_study.py`

**Interfaces:**
- Consumes: `FullReport`, `generate_json`, `Finding`
- Produces: `generate_study_json(datasets: list[FullReport], graph_findings: list[Finding]) -> dict` (键: `study_verdict`, `n_datasets`, `domains`, `total_errors`, `total_warnings`, `total_info`, `datasets`, `graph_findings`)

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_report_study.py`:

```python
"""SP5 study-level report aggregation."""
from __future__ import annotations

from server.report import FullReport, generate_study_json
from server.validator import Finding, ValidationResult


def _full(domain: str, findings: list[Finding]) -> FullReport:
    vr = ValidationResult(domain=domain, row_count=1, col_count=3, findings=findings)
    return FullReport(domain=domain, file_path=f"{domain}.csv", row_count=1, col_count=3,
                      completeness_pct=100.0, validation=vr, review=None)


def test_study_verdict_warns_on_graph_findings():
    ds = [_full("AE", []), _full("MH", [])]
    graph = [Finding("WARN", "GXDOM", None, "AE RELREC-linked to CM, absent")]
    out = generate_study_json(ds, graph)
    assert out["study_verdict"] == "PASS_WITH_WARNINGS"
    assert out["n_datasets"] == 2
    assert sorted(out["domains"]) == ["AE", "MH"]
    assert out["total_warnings"] == 1
    assert out["graph_findings"][0]["rule"] == "GXDOM"
    assert len(out["datasets"]) == 2


def test_study_verdict_fail_on_dataset_error():
    ds = [_full("AE", [Finding("ERROR", "REQ", "USUBJID", "missing")])]
    out = generate_study_json(ds, [])
    assert out["study_verdict"] == "FAIL"
    assert out["total_errors"] == 1


def test_study_verdict_pass_clean():
    out = generate_study_json([_full("AE", [])], [])
    assert out["study_verdict"] == "PASS"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_report_study.py -v`
Expected: FAIL, `ImportError: cannot import name 'generate_study_json'`

- [ ] **Step 3: 写实现** (追加到 report.py; 顶部已 `from server.validator import Finding, ValidationResult`)

```python
def generate_study_json(datasets: list[FullReport], graph_findings: list[Finding]) -> dict:
    """Aggregate per-domain FullReports + cross-domain graph findings into one
    study-level JSON. graph_findings are advisory (WARN/INFO); study_verdict is the
    worst-of per-dataset verdict combined with graph severities."""
    g_err = sum(1 for f in graph_findings if f.severity == "ERROR")
    g_warn = sum(1 for f in graph_findings if f.severity == "WARN")
    g_info = sum(1 for f in graph_findings if f.severity == "INFO")
    total_errors = sum(d.total_errors for d in datasets) + g_err
    total_warnings = sum(d.total_warnings for d in datasets) + g_warn
    total_info = sum(d.total_info for d in datasets) + g_info
    if total_errors:
        verdict = "FAIL"
    elif total_warnings:
        verdict = "PASS_WITH_WARNINGS"
    else:
        verdict = "PASS"
    return {
        "study_verdict": verdict,
        "n_datasets": len(datasets),
        "domains": [d.domain for d in datasets],
        "total_errors": total_errors,
        "total_warnings": total_warnings,
        "total_info": total_info,
        "datasets": [generate_json(d) for d in datasets],
        "graph_findings": [f.to_dict() for f in graph_findings],
    }
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest scripts/tests/test_report_study.py -v`
Expected: 3 passed。ruff + mypy 干净。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/report.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_report_study.py
git commit -m "feat(sp5): report.generate_study_json — study-level roll-up (verdict + graph findings)"
```

---

### Task 6: `POST /api/validate-study` 端点

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/server/router.py` (追加端点, 镜像 `/validate`)
- Test: `branches/07_rag_kg/sdtm-rag/scripts/tests/test_validate_study_endpoint.py`

**Interfaces:**
- Consumes: `parse_bytes`, `validate`, `FullReport`, `generate_study_json`, `run_graph_checks`, `MetaStore`/`GraphEngine`, `request.app.state.spec_loader`
- Produces: `POST /api/validate-study` (多 `files: list[UploadFile]`) → `generate_study_json` dict

- [ ] **Step 1: 写失败测试** (FastAPI TestClient + 内存 CSV)

`scripts/tests/test_validate_study_endpoint.py`:

```python
"""SP5 /api/validate-study endpoint — multi-file study validation."""
from __future__ import annotations

import io

import pytest
from fastapi.testclient import TestClient

from server.main import create_app


@pytest.fixture(scope="module")
def client():
    return TestClient(create_app())


def _csv(domain: str, extra: str) -> bytes:
    return f"STUDYID,DOMAIN,USUBJID,{extra}\nS1,{domain},S1-1,X\n".encode()


def test_validate_study_returns_rollup(client):
    files = [
        ("files", ("ae.csv", io.BytesIO(_csv("AE", "AESEQ")), "text/csv")),
        ("files", ("mh.csv", io.BytesIO(_csv("MH", "MHSEQ")), "text/csv")),
    ]
    r = client.post("/api/validate-study", files=files)
    assert r.status_code == 200
    body = r.json()
    assert body["study_verdict"] in ("PASS", "PASS_WITH_WARNINGS", "FAIL")
    assert set(body["domains"]) == {"AE", "MH"}
    assert "graph_findings" in body and "datasets" in body
```

> `create_app` 是否存在: 若 `server.main` 无 `create_app` (探索: main.py:151 `application.include_router`, main.py:103 建 app.state.spec_loader — app 工厂名待实现者核实), 用实测的工厂名; 若只有模块级 `app`, 改 `from server.main import app; TestClient(app)`。端点 semantic_review 默认关。

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest scripts/tests/test_validate_study_endpoint.py -v`
Expected: FAIL, 404 (端点不存在)

- [ ] **Step 3: 写端点** (追加到 router.py, 紧随 `/validate` 之后, 镜像其结构)

```python
@api_router.post("/validate-study")
async def validate_study(
    request: Request,
    files: list[UploadFile] = File(...),
    semantic_review: str = Form("false"),
):
    """Validate a multi-domain SDTM study: per-domain rule validation + SP5 graph
    checks (impact/completeness/CT-cascade) over the whole submission."""
    from scripts.parse_dataset import parse_bytes, ParseError
    from server.validator import validate
    from server.report import FullReport, generate_study_json
    from server.graph_validator import run_graph_checks
    from server.meta_store import MetaStore
    from server.graph_engine import GraphEngine
    from server.config import settings

    spec_loader = request.app.state.spec_loader
    t0 = time.perf_counter()

    per_dataset: list[FullReport] = []
    frames: dict[str, pd.DataFrame] = {}  # domain -> DataFrame (for graph checks)
    for uf in files:
        data = await uf.read()
        fname = uf.filename or "upload.csv"
        try:
            df, meta = parse_bytes(data, fname)
        except ParseError as e:
            raise HTTPException(status_code=422, detail=f"{fname}: {e}")
        dom = (meta.domain or "").upper()
        if not dom:
            raise HTTPException(
                status_code=422,
                detail=f"{fname}: cannot detect domain (need a DOMAIN column).",
            )
        val = validate(df, dom, spec_loader)
        per_dataset.append(FullReport(
            domain=dom, file_path=fname, row_count=meta.row_count,
            col_count=meta.col_count, completeness_pct=val.completeness_pct,
            validation=val, review=None,
        ))
        frames[dom] = df

    engine = GraphEngine(MetaStore(settings.meta_path))
    graph_findings = run_graph_checks(frames, engine)
    out = generate_study_json(per_dataset, graph_findings)

    log.info("validate_study_done", n=len(files), verdict=out["study_verdict"],
             elapsed_s=round(time.perf_counter() - t0, 2))
    return out
```

> 需要 `import pandas as pd` 在 router.py 顶部 (若无则加, 或改 frames 注解为 `dict[str, "object"]` 避免顶部新 import — 实现者按 router.py 现有 import 风格择一, ruff 干净即可)。

- [ ] **Step 4: 跑测试确认通过 + 全套零回归**

Run: `.venv/bin/python -m pytest scripts/tests/test_validate_study_endpoint.py -v && .venv/bin/python -m pytest scripts/tests/ -q`
Expected: 端点测试 passed; 全套绿 (含 test_validator.py 37 未回归)。ruff + mypy 干净。

- [ ] **Step 5: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/server/router.py branches/07_rag_kg/sdtm-rag/scripts/tests/test_validate_study_endpoint.py
git commit -m "feat(sp5): POST /api/validate-study — multi-domain study validation endpoint"
```

---

### Task 7: Streamlit 多文件 study UI

**Files:**
- Modify: `branches/07_rag_kg/sdtm-rag/ui/streamlit_app.py` (在 `with tab_validate:` 末尾追加 study 段)

**Interfaces:**
- Consumes: `POST /api/validate-study`; 现有 `API_URL`, `requests`, `st`, `json`
- Produces: 多文件 uploader + study 报告渲染 (study_verdict + 逐 dataset + graph_findings)

- [ ] **Step 1: 加 study 上传+渲染块** (在 `with tab_validate:` 块末尾追加)

```python
    st.divider()
    with st.expander("Study-level validation (multi-domain, SP5)", expanded=False):
        st.caption("Upload multiple domain files (each needs a DOMAIN column) for "
                   "cross-domain graph checks: impact, RELREC completeness, CT cascade.")
        study_files = st.file_uploader(
            "Study domain files",
            type=["csv", "xpt", "sas7bdat"],
            accept_multiple_files=True,
            key="study_files",
        )
        if study_files and st.button("Validate study", type="primary", key="validate_study_btn"):
            with st.status("Validating study...", expanded=True) as status:
                files = [("files", (f.name, f.getvalue(), "application/octet-stream"))
                         for f in study_files]
                try:
                    r = requests.post(f"{API_URL}/api/validate-study", files=files, timeout=180)
                    r.raise_for_status()
                    study = r.json()
                    status.update(label="Study validation complete", state="complete", expanded=False)
                except requests.exceptions.ConnectionError:
                    status.update(label="Error", state="error")
                    st.error("Cannot connect to API. Start server first.")
                    st.stop()
                except requests.exceptions.HTTPError as e:
                    status.update(label="Error", state="error")
                    st.error(f"Study validation error: {e.response.text[:500]}")
                    st.stop()

            sv = study.get("study_verdict", "?")
            vc = {"PASS": "green", "PASS_WITH_WARNINGS": "orange", "FAIL": "red"}.get(sv, "gray")
            st.markdown(f"### Study verdict: :{vc}[{sv}]")
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Datasets", study.get("n_datasets", 0))
            m2.metric("Errors", study.get("total_errors", 0))
            m3.metric("Warnings", study.get("total_warnings", 0))
            m4.metric("Info", study.get("total_info", 0))

            gf = study.get("graph_findings", [])
            if gf:
                st.subheader("Cross-Domain Graph Findings")
                for f in gf:
                    st.markdown(f"**[{f.get('rule', '')}]** {f.get('message', '')}")
            for ds in study.get("datasets", []):
                with st.expander(f"{ds.get('domain', '?')} — {ds.get('verdict', '?')} "
                                 f"({ds.get('total_errors', 0)}E/{ds.get('total_warnings', 0)}W)"):
                    for f in ds.get("validation", {}).get("findings", []):
                        st.markdown(f"**[{f.get('rule', '')}]** `{f.get('variable', '')}`: "
                                    f"{f.get('message', '')}")

            st.download_button(
                "Download study JSON",
                data=json.dumps(study, indent=2, ensure_ascii=False),
                file_name="sdtm_study_validation.json",
                mime="application/json",
                key="study_dl",
            )
```

- [ ] **Step 2: 冒烟验证** (Streamlit 无单测)

Run: `cd branches/07_rag_kg/sdtm-rag && .venv/bin/python -c "import ast; ast.parse(open('ui/streamlit_app.py').read()); print('syntax ok')"`
Expected: `syntax ok`。

- [ ] **Step 3: Commit**

```bash
git add branches/07_rag_kg/sdtm-rag/ui/streamlit_app.py
git commit -m "feat(sp5): streamlit multi-file study validation UI (verdict + graph findings)"
```

---

### Task 8: Rule D + Rule A + 收口

**Files:**
- Create: `branches/07_rag_kg/sdtm-rag/evidence/checkpoints/sp5_{ruleD_review,ruleA_audit,summary}.md`
- Create: `branches/07_rag_kg/sdtm-rag/RETROSPECTIVE_sp5.md`
- Modify: `branches/07_rag_kg/sdtm-rag/KG_ROADMAP.md`, `.work/meta/worklog/phase_07_rag_kg.md`, `docs/PROGRESS.md`, `branches/07_rag_kg/_progress.json`

- [ ] **Step 1: Rule D — 异 type reviewer 全量审**

派 1 个 `feature-dev:code-reviewer` (异 lane), 给: spec 路径 + 全 diff (`git diff <Task1 前 commit>..HEAD -- branches/07_rag_kg/sdtm-rag/`) + 审查重点: (1) advisory-only 是否真 (grep graph findings 无 ERROR); (2) check_ct_cascade 误报面 (合法覆盖不同触发 WARN — 可接受/文档化); (3) completeness back-fill 逻辑正确性; (4) 单域 validate 零回归; (5) 端点错误处理 (缺 DOMAIN 列 422)。产出写 `evidence/checkpoints/sp5_ruleD_review.md`。BLOCKER/HIGH 必修 (改后重跑受影响 pytest), MED/LOW 逐条决策。

- [ ] **Step 2: Rule A — 独立 scientist 抽检 N=6**

派 1 个 fresh `general-purpose` (异 lane), 指令: **不 import graph_validator**, 直接 raw 解析 `data/meta/meta.yaml`, 手算 6 样本期望: 2 completeness (挑 2 个有 RELREC 边的域, 手查 target 是否在给定提交集) + 2 cascade (挑 2 个共享 codelist, 手比对给定域数据值集合) + 2 impact (手数 2 个变量/codelist 的 n_domains 是否 ≥10)。对照 `run_graph_checks` 实际输出。产出 `evidence/checkpoints/sp5_ruleA_audit.md`。任何 mismatch = 业务门 FAIL → 修复重跑。

- [ ] **Step 3: findings 修复后重绿**

BLOCKER/HIGH 修完, 重跑 `.venv/bin/python -m pytest scripts/tests/ -q` 全绿 + ruff + mypy。

- [ ] **Step 4: 写 summary + RETROSPECTIVE**

`evidence/checkpoints/sp5_summary.md`: 三类检查验收表 (check / 门 / 结果 / 测试) + 交付物 + 诚实缺口 (CT cascade advisory 误报面 / 无真实数据用合成 / go-live webchat 未暴露 / back-fill 仅 SP5-local 未写回 meta.yaml)。
`RETROSPECTIVE_sp5.md` (规则 C, ≥3 段): 保留做法 / 补上缺口 / 关键决策复盘 (advisory-only 设计 / 确定性内存引擎不碰 Neo4j / study-level 聚合 vs 单域 report)。

- [ ] **Step 5: 文档链 + 收口 commit + push**

- `KG_ROADMAP.md`: 头部时间线加 SP5 DONE 行; 「恢复方式」改为「**KG 重启全线收官** (SP1-5 + AGG 全 DONE)」; SP5 子项目标 DONE; 加「SP5 DONE (日期)」段。
- worklog append SP5 记录; `docs/PROGRESS.md` 最后更新行改 SP5; `_progress.json` 追加 `phase_sp5` 条目。
- 更新 memory `project_kg_decision` (SP5 DONE, KG 全线收官)。

```bash
git add -A
git commit -m "SP5 DONE: 图增强校验器收口 (3 类图增强校验接进 validator, advisory-only, study-level 入口; Rule D+A PASS) — KG 重启全线收官"
git push origin main
```

- [ ] **Step 6: 汇报** — 一段: 三类检查 + 验收门 + KG 重启 SP1-5+AGG 全收官。

---

## Self-Review 记录

- **Spec coverage**: §1 决策全落 (完整3类=T1-3 / advisory=Finding WARN-INFO / study-level=T6 端点 / 内存引擎=graph_validator import GraphEngine / 合成 fixture=T4 / back-fill=T1 `_RELATIONSHIP_DATASETS`); §2 架构=graph_validator(T1-3)+router(T6)+report(T5)+streamlit(T7); §3 三类算法逐一=T1/T2/T3; §4 验收门=T4 golden + T8 Rule D/A + 零回归 (T6 Step4); §5 范围外未越界 (无 Neo4j/无 webchat 暴露/无 per-domain attr/back-fill 不写回); §6 交付物+文档链=T8。无缺口。
- **Placeholder scan**: 无 TBD/TODO; 每 code step 给完整可粘贴代码; fixture CSV 内容完整。
- **Type consistency**: `Finding(severity,rule,variable,message)` 位置参数跨 T1/T2/T3/T5 一致; rule 码 `GIMPACT`/`GXDOM`/`GCASCADE` 全文一致; `run_graph_checks(datasets: dict[str,DataFrame], engine)` 签名 T3 定义、T4/T6 消费一致; `generate_study_json(datasets: list[FullReport], graph_findings: list[Finding])` T5 定义、T6 消费一致; `IMPACT_DOMAIN_THRESHOLD=10` T1 定义、T3 用。
