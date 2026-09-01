"""U2: run_eval 的 doc 通道与强制判库 flag (spec §4.6)。

只测 argparse 与装配, 不跑真检索 (RAGEngine/create_router 全 stub)。

⚠ 前四条是 plan 逐字给的; 实现方按 Global Constraint 7 做方向②变异 (「这行改坏了谁会红」)
时实测: **把 main() 里整个 doc 通道装配块删掉, 这四条全绿** (1142 passed, 0 failed) ——
因为 `--study-docs` / `--corpus` 不存在时 argparse 自己就以 "unrecognized arguments" 退出
SystemExit, 与闸拒绝的 SystemExit 无法区分。故下半部分补装配锁与 stderr 判别断言, 使
`main()` 里每一行新代码都有能杀死它的断言 (逐行对应见 evidence/step_u2_mutation_task3.md)。
"""
from types import SimpleNamespace

import pytest

from eval import run_eval as m
from server.study_corpus import StudyCorpusEngine


def test_study_docs_requires_federated():
    with pytest.raises(SystemExit):
        m.main(["x.yml", "--study-docs"])


def test_corpus_default_is_auto_and_adapter_passes_it_through():
    fed = SimpleNamespace(retrieve=lambda q, corpus, top_k: ([], corpus))
    ad = m._FederatedAdapter(fed)
    ad.retrieve("q")
    assert ad.routed == ["auto"]


def test_corpus_forced_study_is_passed_to_federation():
    """强制判库是把「判库损耗」与「接线损耗」拆开的唯一手段 —— 传丢了两个数就合并了。"""
    seen = {}

    def _retrieve(q, corpus, top_k):
        seen["corpus"] = corpus
        return [], corpus

    ad = m._FederatedAdapter(SimpleNamespace(retrieve=_retrieve), corpus="study")
    ad.retrieve("q")
    assert seen["corpus"] == "study"


def test_invalid_corpus_rejected():
    with pytest.raises(SystemExit):
        m.main(["x.yml", "--federated", "--corpus", "nope"])


# ---------------------------------------------------------------- 判别力补强 ↓

def test_study_docs_error_is_the_gate_not_an_unknown_flag(capsys):
    """闸的报错要能与「flag 根本不存在」区分开。

    否则 `--study-docs` 的 add_argument 被删掉时, argparse 的 "unrecognized arguments"
    同样是 SystemExit, 上面那条 raises(SystemExit) 照样绿 —— 实测过。
    """
    with pytest.raises(SystemExit):
        m.main(["x.yml", "--study-docs"])
    err = capsys.readouterr().err
    assert "unrecognized" not in err
    assert "--study-docs 需要 --federated" in err


def test_corpus_non_auto_requires_federated(capsys):
    """强制判库只有联邦有意义; 非联邦下静默忽略 = 量出来的数字口径不是命令行写的那个。"""
    with pytest.raises(SystemExit):
        m.main(["x.yml", "--corpus", "study"])
    err = capsys.readouterr().err
    assert "unrecognized" not in err
    assert "--corpus 只在 --federated 下有意义" in err


def test_corpus_choices_are_exactly_the_four(capsys):
    """`nope` 被拒必须是 choices 拒的, 不是「没有 --corpus 这个 flag」拒的。"""
    with pytest.raises(SystemExit):
        m.main(["x.yml", "--federated", "--corpus", "nope"])
    err = capsys.readouterr().err
    assert "invalid choice" in err
    # 引号形态随 argparse 版本变 (本机 "choose from auto, cdisc, …"), 只认名字不认引号
    tail = err.split("choose from", 1)[1]
    for c in ("auto", "cdisc", "study", "both"):
        assert c in tail


class _Stop(Exception):
    """哨兵: 装配一完成就停, 不进 run_evaluation (不发 embedding / 不发 LLM)。"""


# 屏幕回执里的 chunk 数。两台 study 引擎取**不同**值, 否则 `docs_rag.collection.count()`
# 被改读兄弟引擎 `study_rag` 时逐位不可分 (main.py 的 ready 日志是同一种共错, 已实测全绿)。
FAKE_DOC_CHUNKS = 137
FAKE_CARD_CHUNKS = 959


class _FakeRAG:
    def __init__(self, **kw):
        self.kwargs = kw
        n = (FAKE_DOC_CHUNKS if str(kw.get("collection_name", "")).endswith("_docs")
             else FAKE_CARD_CHUNKS)
        self.collection = SimpleNamespace(count=lambda: n)
        self.query_expansion = "none"
        self.hybrid_fusion = "rrf"
        self.hybrid_alpha = 0.5
        # 屏幕回执现在读引擎实收值 (B3' 修复轮 M-1 / R3), 假引擎必须带上这两个属性
        self.web_search_enabled = kw["web_search_enabled"]
        self.prompt_guardrail_enabled = kw["prompt_guardrail_enabled"]


@pytest.fixture
def assemble(monkeypatch, tmp_path):
    """跑到 retriever 装配完为止, 交出 (engines, fed_args, adapter)。"""
    engines: list[_FakeRAG] = []
    fed_args: dict = {}
    adapters: list = []
    real_adapter = m._FederatedAdapter

    def _rag(**kw):
        engines.append(_FakeRAG(**kw))
        return engines[-1]

    def _fed(cdisc, study, router, *, top_k=None, signals=None):
        # 签名必须跟着真构造器走: 少一个 kwarg 就是 TypeError, 而那正是接线测试要看的东西
        fed_args.update(cdisc=cdisc, study=study, top_k=top_k, signals=signals)
        return SimpleNamespace(retrieve=lambda q, corpus, top_k: ([], corpus))

    def _adapter(*a, **kw):
        adapters.append(real_adapter(*a, **kw))
        return adapters[-1]

    monkeypatch.setattr(m, "RAGEngine", _rag)
    monkeypatch.setattr(m, "create_router", lambda s: SimpleNamespace(model_list=[]))
    monkeypatch.setattr(m, "FederatedEngine", _fed)
    monkeypatch.setattr(m, "_FederatedAdapter", _adapter)
    monkeypatch.setattr(m, "run_evaluation", lambda *a, **kw: (_ for _ in ()).throw(_Stop()))

    ts = tmp_path / "t.yml"
    ts.write_text("- id: q1\n  category: c\n  question: x\n  expected_sources: [a.md]\n")

    def _run(*extra):
        with pytest.raises(_Stop):
            m.main([str(ts), "--retrieval-only", "--federated", *extra])
        return engines, fed_args, adapters[-1]

    return _run


def test_docs_engine_is_built_and_wrapped_and_corpus_reaches_the_adapter(assemble):
    """整块装配锁: 三台引擎 / 包成 StudyCorpusEngine / 交给联邦 / corpus 传到 adapter。

    这四件事任缺其一都是静默的 —— 服务照跑, 只是 doc 一条都不出现 (或强制判库悄悄失效)。
    """
    engines, fed, adapter = assemble("--study-docs", "--doc-seats", "7", "--corpus", "study")

    assert len(engines) == 3                       # cdisc / cards / docs
    docs_kw = engines[2].kwargs
    assert docs_kw["collection_name"] == m.settings.study_docs_collection_name
    assert docs_kw["collection_name"] != m.settings.study_collection_name
    assert docs_kw["kb_root"] == m.settings.study_kb_root   # 与 U1 上界口径逐字相同
    assert docs_kw["top_k"] == 7                   # 席位下传, 不是 args.top_k
    assert docs_kw["structured_lookup_enabled"] is False
    assert "study_lookup" not in docs_kw           # S2 的数据源对 doc chunk 无定义

    study_engine = fed["study"]
    assert isinstance(study_engine, StudyCorpusEngine)
    assert study_engine.doc_seats == 7
    assert study_engine.cards is engines[1]        # 顺序装反 = cards/docs 角色互换
    assert study_engine.docs is engines[2]
    assert fed["cdisc"] is engines[0]
    assert adapter.corpus == "study"               # 端到端: CLI → adapter → 联邦


def test_doc_seats_defaults_to_settings_not_a_hardcoded_constant(assemble, monkeypatch):
    """默认值必须来自 settings。写死成 5 时与出厂值相同, 只有换掉 settings 才照得出来。"""
    monkeypatch.setattr(m.settings, "study_docs_seats", 9)
    engines, fed, _ = assemble("--study-docs")
    assert fed["study"].doc_seats == 9
    assert engines[2].kwargs["top_k"] == 9


def test_doc_seats_zero_is_honoured_not_silently_defaulted(assemble, monkeypatch):
    """`args.doc_seats if … is not None else …` 写成 `or` 时, `--doc-seats 0` 静默变成
    8 席 —— 而 0 正是**空臂那一臂**唯一的表达方式: 声称的"关掉 doc 通道"会被悄悄跑成满席,
    两臂差值于是塌成噪声, 且屏幕回执与 JSON 都不会有任何提示。

    settings 换成 9 (≠ 出厂 8) 才能把"回落"与"恰好等于默认"分开。
    """
    monkeypatch.setattr(m.settings, "study_docs_seats", 9)
    engines, fed, _ = assemble("--study-docs", "--doc-seats", "0")
    assert fed["study"].doc_seats == 0
    assert engines[2].kwargs["top_k"] == 0


def test_docs_channel_receipt_reports_the_docs_collection_not_its_sibling(assemble, capsys):
    """屏幕回执里的 chunk 数读成兄弟引擎 (`study_rag`) 时, doc 库一条都没灌进去也会报 959。

    这一行是"库真的灌进去了"在 eval 侧唯一的现场线索 (114 → 0 是静默失效, 不会崩)。
    """
    capsys.readouterr()
    assemble("--study-docs", "--doc-seats", "7")
    out = capsys.readouterr().out
    assert f"Study docs channel: {FAKE_DOC_CHUNKS} chunks" in out
    assert f"collection={m.settings.study_docs_collection_name}, seats=7" in out


def test_without_study_docs_the_federation_gets_the_bare_cards_engine(assemble):
    """OFF 时逐位回到 Task 3 之前: 两台引擎, 不包 wrapper, corpus=auto。"""
    engines, fed, adapter = assemble()
    assert len(engines) == 2
    assert fed["study"] is engines[1]
    assert not isinstance(fed["study"], StudyCorpusEngine)
    assert adapter.corpus == "auto"
