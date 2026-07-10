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


def test_data_flow_uses_injected_completer_and_marks_directed():
    prose = M.load_prose(M.Path(__file__).parent.joinpath("fixtures","sp6_prose"), ["PR","TR"])
    fake = lambda prompt, model: [{
        "source": "PR", "target": "TR", "relation": "measurements recorded in",
        "quote": "The tumor measurements obtained via the procedure are recorded in the TR dataset.",
        "confidence": 0.82,
    }]
    edges = M.extract_data_flow(prose, ["PR","TR"], model="x", complete=fake)
    assert edges and edges[0]["kind"] == "data_flow" and edges[0]["directed"] is True
    assert edges[0]["extractor"] == "llm"

def test_quote_in_source_gate():
    fix = M.Path(__file__).parent.joinpath("fixtures","sp6_prose")
    good = {"evidence": {"quote": "recorded in the TR dataset",
                         "source_file": "domains/PR/examples.md"}}
    bad  = {"evidence": {"quote": "THIS SENTENCE IS FABRICATED",
                         "source_file": "domains/PR/examples.md"}}
    assert M.quote_in_source(good, fix) is True
    assert M.quote_in_source(bad, fix) is False


def test_verify_rejects_when_judge_refutes():
    edge = {"source":"PR","target":"TR","relation":"x",
            "evidence":{"quote":"q","source_file":"f"}}
    refute = lambda prompt, model: [{"refuted": True, "reason": "quote does not support direction"}]
    v = M.verify_data_flow_edge(edge, "x", judge=refute)
    assert v["verified"] is False and "support" in v["note"]

def test_build_assembles_and_gates():
    fix = M.Path(__file__).parent.joinpath("fixtures","sp6_prose")
    flow = lambda prompt, model: [{"source":"PR","target":"TR","relation":"recorded in",
        "quote":"The tumor measurements obtained via the procedure are recorded in the TR dataset.",
        "confidence":0.82}]
    accept = lambda prompt, model: [{"refuted": False, "reason": "ok"}]
    res = M.build_implicit_relations(fix, ["PR","TU"], "x", complete=flow, judge=accept)
    kinds = {e["kind"] for e in res["edges"]}
    assert "data_flow" in kinds and "explicit_link" in kinds
    df = [e for e in res["edges"] if e["kind"]=="data_flow"]
    assert df and df[0]["verified"] is True     # 引文命中 + 裁判通过
    assert res["meta"]["confidence_threshold"] == M.CONF_THRESHOLD

def test_build_caps_data_flow_per_pair():
    q = "recorded in the TR dataset"  # verbatim substring of PR/examples.md -> passes gate1
    def flow(prompt, model):
        if "PR" in prompt and "TR" in prompt:
            return [{"source":"PR","target":"TR","relation":r,"quote":q,"confidence":0.8}
                    for r in ("a","b","c")]   # 3 candidates for the same pair
        return []
    accept = lambda prompt, model: [{"refuted": False, "reason": "ok"}]
    res = M.build_implicit_relations(FIX, ["PR","TU"], "x", complete=flow, judge=accept)
    df = [e for e in res["edges"] if e["kind"] == "data_flow"]
    assert len(df) == 2                                   # per_pair cap = MAX_FLOW_PER_PAIR
    capped = [e for e in res["_rejected"]
              if e["kind"] == "data_flow" and "cap" in e["verify_note"]]
    assert len(capped) == 1                               # 3rd rejected by the cap

def test_build_rejects_below_confidence():
    def flow(prompt, model):
        if "PR" in prompt and "TR" in prompt:
            return [{"source":"PR","target":"TR","relation":"x",
                     "quote":"recorded in the TR dataset","confidence":0.5}]  # < 0.6
        return []
    accept = lambda prompt, model: [{"refuted": False, "reason": "ok"}]
    res = M.build_implicit_relations(FIX, ["PR","TU"], "x", complete=flow, judge=accept)
    assert [e for e in res["edges"] if e["kind"] == "data_flow"] == []
    assert any(e["kind"] == "data_flow" and "confidence" in e["verify_note"]
               for e in res["_rejected"])
