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
