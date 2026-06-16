from __future__ import annotations
from pathlib import Path
import pytest
from scripts.build_meta import (
    build_meta, _split_ct, _parse_label, _same_class_map,
    _relations_curated, _model_defhome, _codelists,
)

KB_ROOT = Path(__file__).resolve().parents[5] / "knowledge_base"

@pytest.fixture(scope="module")
def kb_root() -> Path:
    return KB_ROOT

@pytest.fixture(scope="module")
def meta(kb_root):
    return build_meta(kb_root)


# ── Task 1: domain scalars + spec.md (DI stub) flag ───────────────────────

def test_domain_count_and_special_flag(meta):
    domains = {d["domain"]: d for d in meta["domains"]}
    # 64 个目录，但只 63 个有 spec.md（计入标准域）；DI 仅有 assumptions.md
    assert len(domains) == 64
    assert sum(1 for d in meta["domains"] if d["counts_toward_63"]) == 63
    assert domains["DI"]["is_special"] is True
    assert domains["DI"]["counts_toward_63"] is False
    assert domains["SUPPQUAL"]["is_special"] is False
    assert domains["SUPPQUAL"]["counts_toward_63"] is True
    assert domains["AE"]["counts_toward_63"] is True

def test_domain_scalars(meta):
    ae = next(d for d in meta["domains"] if d["domain"] == "AE")
    assert ae["class"] == "Events"
    assert ae["label"] == "Adverse Events"
    assert ae["structure"] == "One record per adverse event per subject"

def test_parse_label_unit():
    assert _parse_label("# AE — Adverse Events") == "Adverse Events"
    assert _parse_label("# LB — Laboratory Test Results") == "Laboratory Test Results"
    assert _parse_label("no title here") == ""


# ── Task 2: variables + ct_codes/ct_dict split ────────────────────────────

def test_split_ct_unit():
    assert _split_ct("C66742") == (["C66742"], [])
    assert _split_ct("C85494; C128684; C128683") == (["C85494", "C128684", "C128683"], [])
    assert _split_ct("MedDRA") == ([], ["MedDRA"])
    assert _split_ct("ISO 8601 datetime or interval") == ([], ["ISO 8601 datetime or interval"])
    assert _split_ct("") == ([], [])

def test_variables_present_and_ct(meta):
    ae = next(d for d in meta["domains"] if d["domain"] == "AE")
    by_name = {v["name"]: v for v in ae["variables"]}
    aeser = by_name["AESER"]
    assert aeser["role"] == "Record Qualifier"
    assert aeser["type"] == "Char"
    assert aeser["core"] == "Exp"
    assert aeser["label"] == "Serious Event"
    assert aeser["ct_codes"] == ["C66742"]
    assert aeser["ct_dict"] == []
    # STUDYID has no controlled terms
    assert by_name["STUDYID"]["ct_codes"] == []


# ── Task 3: same_class ───────────────────────────────────────────────────

def test_same_class(meta):
    by_name = {d["domain"]: d for d in meta["domains"]}
    ae_sib = set(by_name["AE"]["same_class"])
    # 策划 bullet 列的 Events 兄弟必须都在（group-by 是完整真源）
    assert {"BE", "CE", "DS", "DV", "HO", "MH"} <= ae_sib
    assert "AE" not in ae_sib                      # 不含自己
    assert all(by_name[s]["class"] == "Events" for s in ae_sib)  # 同类
    assert "AE" in by_name["BE"]["same_class"]     # 对称


# ── Task 4: relations_curated ─────────────────────────────────────────────

def test_relations_curated(meta):
    ae = next(d for d in meta["domains"] if d["domain"] == "AE")
    rels = {r["target"]: r for r in ae["relations_curated"]}
    # CM/PR 字面写了 "via RELREC"
    assert rels["CM"]["category"] == "Treatment"
    assert rels["CM"]["mechanism"] == "RELREC"
    assert rels["PR"]["mechanism"] == "RELREC"
    # FA 无机制词 -> null（None）
    assert rels["FA"]["category"] == "Findings About"
    assert rels["FA"]["mechanism"] is None
    # 全部标记来源
    assert all(r["fidelity"] == "curated_prose" for r in ae["relations_curated"])
    # "Same class" bullet（无链接）不应混进来
    assert "BE" not in rels


# ── Task 6: codelists ─────────────────────────────────────────────────────

def test_codelists(meta):
    cls = {c["ct_code"]: c for c in meta["codelists"]}
    assert len(meta["codelists"]) == 1005
    c = cls["C66742"]
    assert c["name"] == "No Yes Response"
    assert c["extensible"] is False
    # Plan says term_count==2 (N,Y) but real KB has 4 (N,NA,U,Y).
    # Asserting actual KB value per instructions (report discrepancy, don't fudge).
    assert c["term_count"] == 4                 # N, NA, U, Y
    assert c["termfile"] == "terminology/core/general_part4.md"


# ── Task 7: dump_meta + idempotent + keys ────────────────────────────────

def test_idempotent_and_keys(meta, kb_root):
    again = build_meta(kb_root)
    assert meta == again                         # 同输入同输出
    assert set(meta.keys()) == {
        "meta_version", "generated_from", "domains", "model_defhome", "codelists",
    }
    d0 = meta["domains"][0]
    assert set(d0.keys()) == {
        "domain", "class", "label", "structure", "is_special",
        "counts_toward_63", "variables", "same_class", "relations_curated",
    }

def test_yaml_roundtrip_stable(tmp_path, kb_root):
    import yaml
    from scripts.build_meta import dump_meta
    m = build_meta(kb_root)
    p = tmp_path / "meta.yaml"
    dump_meta(m, p)
    a = p.read_bytes()
    dump_meta(m, p)
    b = p.read_bytes()
    assert a == b                                # 落盘字节稳定
    assert yaml.safe_load(p.read_text()) == m    # 可往返


# ── Task 5: model_defhome ─────────────────────────────────────────────────

def test_model_defhome(meta):
    mdh = meta["model_defhome"]
    assert mdh["RDOMAIN"] == "model/06_relationship_datasets.md"
    assert "EPOCH" in mdh                       # 单 home 变量在
    assert "DOMAIN" not in mdh                  # 跨多文件 -> 丢弃
    assert "USUBJID" not in mdh
    assert not any(k.startswith("--") for k in mdh)  # 排除 -- 前缀
