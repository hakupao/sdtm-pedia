from pathlib import Path
from scripts import mine_implicit_relations as M

FIX = Path(__file__).parent / "fixtures" / "sp6_prose"

def test_load_prose_reads_examples():
    prose = M.load_prose(FIX, ["PR", "TU"])
    assert "recorded in the TR dataset" in prose["PR"]["examples"]
    assert prose["TU"]["assumptions"] == ""  # 缺文件 -> 空串

def test_resolve_cluster_adds_named_neighbors():
    # PR 散文点名 TR/TU;TU 点名 TR/RS -> 邻居并入
    cluster = M.resolve_cluster(FIX, ["PR", "TU"])
    assert {"PR", "TU", "TR", "RS"} <= set(cluster)
    assert "DM" not in cluster  # known non-seed dir, unnamed in any seed prose -> must be excluded
    assert cluster == sorted(cluster)


def test_explicit_links_finds_relrec():
    prose = M.load_prose(FIX, ["PR","TU"])
    edges = M.extract_explicit_links(prose, ["PR","TU","TR","RS"])
    relrec = [e for e in edges if e["relation"] == "RELREC"]
    assert any({e["source"], e["target"]} == {"PR","TU"} for e in relrec)
    e = relrec[0]
    assert e["kind"] == "explicit_link" and e["extractor"] == "regex"
    assert e["verified"] is True and e["directed"] is False
    assert "RELREC" in e["evidence"]["quote"]


def test_cooccurrence_counts_and_dedups():
    prose = {
        "PR": {"assumptions": "PR relates to TR. See TR again. TR TR.", "examples": ""},
        "TR": {"assumptions": "TR mentions PR here.", "examples": ""},
    }
    edges = M.extract_cooccurrence(prose, ["PR", "TR"], min_count=2)
    co = [e for e in edges if e["kind"] == "co_occurrence"]
    assert len(co) == 1                       # 无向, 只一条
    assert co[0]["source"] == "PR" and co[0]["target"] == "TR"  # source<target
    assert co[0]["directed"] is False and co[0]["extractor"] == "count"
