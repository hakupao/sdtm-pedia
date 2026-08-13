"""U2: 生产 lifespan 上的 doc 通道接线锁 (spec §4.5)。

接线漏在这里是完全静默的 —— 服务照常起, study 侧只是回到纯卡片。所以三个方向都要锁:
开着一定包成 StudyCorpusEngine / 关着一定不包 / 开着但联邦关着要留声。
仿 test_main_study_lookup_wiring.py 的 stub 编制, 不碰 chroma。
"""
from __future__ import annotations

import asyncio
import os
from types import SimpleNamespace

import pytest
import structlog
from fastapi import FastAPI

from server import main as main_mod
from server import study_lookup as study_lookup_mod
from server.config import Settings
from server.study_corpus import StudyCorpusEngine

# 条数刻意取不寻常值 (仿 test_main_study_lookup_wiring.py 的 _FakeLookup=7): 返回 0 时
# "字段缺失" / "库是空的" / "写死成常量 0" 三种情况在断言上逐位不可分。
#
# ⚠ 两台 fake 的 count 必须**不同**: 两台同为 137 时把 ready 日志里的
# `chunks=rag_docs.collection.count()` 改读**兄弟引擎** `rag_study` 全量全绿 (抽检方 B 实测),
# 而那条日志正是"doc 库一条都没灌进去"的唯一现场线索 —— 共错下它会报 959。
FAKE_DOC_CHUNKS = 137
FAKE_CARD_CHUNKS = 959


@pytest.fixture
def boot(monkeypatch):
    engines: list[dict] = []

    class FakeCollection:
        def __init__(self, n):
            self._n = n

        def count(self):
            return self._n

    class FakeEngine:
        def __init__(self, **kwargs):
            engines.append(kwargs)
            # 实例上也留一份: 组合器收的是引擎**实例**(位置参数), 只看 engines 列表
            # 无法判断哪台引擎被放到了 cards 位、哪台被放到了 docs 位。
            self.kwargs = kwargs
            self.collection = FakeCollection(
                FAKE_DOC_CHUNKS if kwargs["collection_name"].endswith("_docs")
                else FAKE_CARD_CHUNKS
            )
            self.system_prompt = "SYS"

        def _vi_section_map(self):
            return {}

    monkeypatch.setattr(main_mod, "RAGEngine", FakeEngine)
    monkeypatch.setattr(main_mod, "create_router", lambda s: SimpleNamespace(model_list=[]))
    monkeypatch.setattr(main_mod, "SpecLoader",
                        lambda root: SimpleNamespace(domains=[], codelists=[]))
    # catalog.json 按数据红线不进 git ⇒ 不 stub 的话裸检出里这些测试全部 FileNotFoundError
    # (实测: catalog 路径指向不存在的文件时本文件 3 failed, 而参照文件 12 passed)。
    # 顺带免掉每次 boot 真读 959 items 的开销。
    monkeypatch.setattr(
        study_lookup_mod.StudyLookup, "from_paths",
        staticmethod(lambda catalog_path, aliases_path: SimpleNamespace(
            stats=lambda: "7 items/0 aliases")),
    )

    def _run(**overrides):
        s = Settings(**overrides)
        app = FastAPI()
        app.state.settings = s
        events: list[tuple] = []
        # ⚠ 计划原文写的是 `lambda _l, m, ed: events.append((m, ed))`, 但 structlog 的
        # processor 签名是 (logger, method_name, event_dict) —— `m` 绑的是 "info"/"warning"
        # 这个**方法名**, 事件名在 `ed["event"]` 里 (实测: log.warning("study_docs_ignored")
        # → ("warning", {"event": "study_docs_ignored", ...}))。照原文抄则下面两条日志断言
        # 在任何实现下都不可能通过。这里只把元组首位换成真正的事件名, 四条断言一字不动。
        # 用 capture_logs 而非裸 configure: 后者会把处理器永久留在全局配置里泄漏给后续测试。
        async def go():
            async with main_mod.lifespan(app):
                pass
        with structlog.testing.capture_logs() as logs:
            asyncio.run(go())
        events.extend((e["event"], e) for e in logs)
        return app, engines, events

    return _run


def test_docs_engine_is_built_and_wrapped_when_enabled(boot):
    app, engines, _ = boot(federation_enabled=True, study_docs_enabled=True, study_docs_seats=5)
    built = [e["collection_name"] for e in engines]
    assert "study_st01_docs" in built
    assert isinstance(app.state.federation.study, StudyCorpusEngine)
    assert app.state.federation.study.doc_seats == 5


def test_docs_engine_absent_when_disabled(boot):
    app, engines, _ = boot(federation_enabled=True, study_docs_enabled=False)
    assert "study_st01_docs" not in [e["collection_name"] for e in engines]
    assert not isinstance(app.state.federation.study, StudyCorpusEngine)


def test_engine_positions_are_not_swapped(boot):
    """两台引擎是**位置**参数 —— 写反了 isinstance 与 doc_seats 都照样绿。

    位置重排是最可能真实发生的编辑, 后果却是核心不变量整个反转: docs 引擎当上 "cards"
    拿走 15 席去查 114 条章节, 真 cards 降成 5 席查 959 张卡, 且 system_prompt 会来自
    docs 引擎 —— 正是 spec §4.1 花一整条测试去钉的那条约束的反面。只能断到构造实参上。
    """
    app, _, _ = boot(federation_enabled=True, study_docs_enabled=True, study_docs_seats=5)
    eng = app.state.federation.study
    assert eng.cards.kwargs["collection_name"] == "study_st01"
    assert eng.docs.kwargs["collection_name"] == "study_st01_docs"


def test_docs_engine_shares_every_lever_with_the_cards_engine(boot):
    """spec §4.1「与 U1 测上界时逐字同一条路径, 数字因此可比」的可执行形式。

    逐参数抄一遍清单是抄写练习 (且漏一个就是漏一个); 这里改成**同源比对**: 两台引擎的
    构造实参只允许差三处 —— 库名、席位数、以及卡片侧专属的 S2 直查。任何一条检索杠杆
    (hybrid 三件套 / embedding / chroma_dir / kb_root / S1 / 答题护栏) 在 docs 侧被改成
    另一个值, 这条就红 —— 因为那一刻两条路径不再可比, U1 的上界数字也就不再是参照物。
    """
    app, engines, _ = boot(federation_enabled=True, study_docs_enabled=True, study_docs_seats=7)
    cards, docs = engines[1], engines[2]
    assert cards["collection_name"] == "study_st01" and docs["collection_name"] == "study_st01_docs"
    # S2 是卡片侧专属通道 (docs 侧连键都不该出现, 传 None 也不行 —— 那会掩盖 RAGEngine
    # 的 S1/S2 互斥闸把 docs 引擎误配成直查通道的情形)
    assert set(cards) - set(docs) == {"study_lookup"}
    assert set(docs) - set(cards) == set()
    assert {k for k in docs if cards[k] != docs[k]} == {"collection_name", "top_k"}
    # 差集只说"两者不同", 不说谁大 —— 实测把两台引擎的 top_k **对调** (cards 拿 seats、
    # docs 拿全局 15) 差集一字不变, 全量 1144 全绿。而那正是"加席不抢席"在接线层的反面:
    # 真 cards 降成 5 席查 959 张卡, docs 拿 15 席查 114 条章节。所以方向必须单独钉。
    assert cards["top_k"] == Settings().top_k and docs["top_k"] == 7


def test_docs_enabled_without_federation_logs_ignored(boot):
    _, engines, events = boot(federation_enabled=False, study_docs_enabled=True)
    assert "study_st01_docs" not in [e["collection_name"] for e in engines]
    assert any(m == "study_docs_ignored" for m, _ in events)


def test_no_ignored_warning_when_federation_is_on(boot):
    """反方向: 去掉 `and not s.federation_enabled` 后每次正常启动都报警 = 告警失效,
    而正方向那条照样绿。参照文件两处反方向断言都写了 (`:186-188` / `:191-193`)。"""
    _, _, events = boot(federation_enabled=True, study_docs_enabled=True)
    assert not [e for m, e in events if m == "study_docs_ignored"]


def test_no_ignored_warning_when_docs_disabled(boot):
    _, _, events = boot(federation_enabled=False, study_docs_enabled=False)
    assert not [e for m, e in events if m == "study_docs_ignored"]


def test_settings_study_docs_defaults(monkeypatch):
    """本文件唯一读**代码默认值**的测试。四条接线测试全部显式传值 ⇒ 默认被偷偷改掉时
    全量仍全绿。体例仿 test_run_eval_flags.py::test_settings_study_lookup_defaults。

    ⚠ `Settings` 走 pydantic-settings 的 `env_prefix="SDTM_RAG_"`, 且 config.py import 期
    就 `load_dotenv` 把 .env 灌进 os.environ ⇒ 不隔离环境时本条量的是**本机配置**而不是
    代码默认。实测 `SDTM_RAG_STUDY_DOCS_SEATS=5 SDTM_RAG_STUDY_DOCS_ENABLED=true pytest …`
    → 1 failed。后果两面: 这条断言挡不住通过 .env 打开通道 (而那正是生产启用的正规方式),
    且团队一旦在 .env 里改, 全量套件会伪红。故先清掉全部 SDTM_RAG_* 再构造。

    生产默认 `study_docs_enabled=True` (2026-08-13 翻转): 收益侧 doc 答题 0.0333→0.9517,
    代价侧卡片侧回归**未被建立** (ON-ON 对照里驱动条款的 q23r 不复现, ON 臂自身噪声
    +2.78pt 已达声称效应量)。即 **spec §6 自毁条款 3 是触发状态, 由用户 2026-08-13 裁定
    豁免**后翻转 —— 不是"未触发", 也不是"验收通过"。
    """
    for k in list(os.environ):
        if k.startswith("SDTM_RAG_"):
            monkeypatch.delenv(k, raising=False)
    s = Settings()
    assert s.study_docs_enabled is True
    assert s.study_docs_collection_name == "study_st01_docs"
    # 席位数 8 是 Task 4 sweep 实测裁定的 (evidence/step_u2_sweep.md §4): 它是召回天花板上
    # 的**最小** N —— N=8 满分 30/30 而 N=5 只有 25/30 (丢 11.67pt), N=10/15 零召回增益却
    # 把 context 从 3.17x 推到 3.68x/5.19x。改这个值 = 换掉一个有实测依据的裁定, 要连
    # evidence 一起改。
    assert s.study_docs_seats == 8
    # 库名与卡片库必须是两个不同的 collection (指成同一个 = doc 通道其实没接上)
    assert s.study_docs_collection_name != s.study_collection_name


def test_seats_and_collection_are_reported_in_the_ready_log(boot):
    """条数/库名进日志: 席位写死成常量或库名指错时, 唯一的现场线索就是这一行。"""
    app, _, events = boot(federation_enabled=True, study_docs_enabled=True, study_docs_seats=7)
    hit = [ed for m, ed in events if m == "study_docs"]
    assert hit and hit[0]["seats"] == 7 and hit[0]["collection"] == "study_st01_docs"
    # ↓ 补做的断言 (实现方自查, 计划没有)。计划的三条变异里 `doc_seats=s.study_docs_seats`
    # 改成常量 `5` 实测**全绿 1131 passed** —— 因为上面唯一检查引擎席位的那条测试恰好也用
    # seats=5, 而这条只看日志。日志报 7 而引擎实际只拿 5 席正是"日志在撒谎"的那类故障,
    # 用非默认值把两者钉成同源。
    assert app.state.federation.study.doc_seats == 7
    # chunks 是"库真的灌进去了"的唯一现场线索 (114 → 0 是静默失效, 不会崩)。用不寻常的
    # FAKE_DOC_CHUNKS 断, 才能把"字段缺失/库是空的/写死成常量"三种情况分开; 与卡片库的
    # FAKE_CARD_CHUNKS 不同值, 才能把"读了兄弟引擎的 count"也分开 (共错型)。
    assert hit[0]["chunks"] == FAKE_DOC_CHUNKS != FAKE_CARD_CHUNKS
