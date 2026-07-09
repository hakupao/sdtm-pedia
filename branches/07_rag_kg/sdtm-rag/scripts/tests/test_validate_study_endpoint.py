"""SP5 /api/validate-study endpoint — multi-file study validation."""
from __future__ import annotations

import io

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from scripts.spec_loader import SpecLoader
from server.config import settings
from server.router import api_router


@pytest.fixture(scope="module")
def client():
    # Convention (test_router_structured.py): bare app + manual app.state.* — no lifespan/
    # create_app (which would build the full RAG engine). validate() needs a real spec_loader;
    # the SP5 graph checks build their own MetaStore/GraphEngine from settings.meta_path.
    app = FastAPI()
    app.include_router(api_router)
    app.state.spec_loader = SpecLoader(settings.kb_root)
    return TestClient(app)


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


def test_validate_study_uses_cached_engine():
    # When app.state.graph_engine is present (prod lifespan path), the endpoint reuses it.
    from server.graph_engine import GraphEngine
    from server.meta_store import MetaStore
    app = FastAPI()
    app.include_router(api_router)
    app.state.spec_loader = SpecLoader(settings.kb_root)
    app.state.graph_engine = GraphEngine(MetaStore(settings.meta_path))
    c = TestClient(app)
    files = [("files", ("ae.csv", io.BytesIO(_csv("AE", "AESEQ")), "text/csv"))]
    r = c.post("/api/validate-study", files=files)
    assert r.status_code == 200
    assert r.json()["domains"] == ["AE"]


def test_validate_study_missing_domain_column_422(client):
    # No DOMAIN column -> domain cannot be detected -> 422.
    bad = b"STUDYID,USUBJID,AGE\nS1,S1-1,30\n"
    files = [("files", ("nodom.csv", io.BytesIO(bad), "text/csv"))]
    r = client.post("/api/validate-study", files=files)
    assert r.status_code == 422
