"""U2 Task 3b: docs 引擎「两条路径同源」闸。

docs 引擎被两条独立代码路径各造一次 —— `server/main.py` 的 lifespan (生产) 与
`eval/run_eval.py` 的 `--study-docs` 分支 (尺子)。两处各抄一份参数清单时, 漂移的表现是
**尺子全绿而生产是另一台引擎, 且不会有任何报错**, 这直接抽掉本单元 Task 4/6/8 全部数字的
效力 (Task 2 审查方与 Task 3 实现方独立提出的同一条风险)。

本文件锁三件事:
1. 两条路径都**经过同一个工厂** (只比 kwargs 抓不到"绕过工厂但抄对了参数");
2. 工厂写死的那组 kwargs 在两条路径上**逐键相同**, 且方向单独钉 (两边同时指错也相等);
3. eval 侧 docs 引擎与**同一次运行里的 cards 引擎** lever 一致 —— Task 3 的实际缺陷是
   docs 侧 `rerank_*` / `query_expansion` 三族根本没传, 吃 RAGEngine 默认值, 而默认值恰好
   等于 settings 出厂值 ⇒ 不跑 `--rerank` 就永远看不出来。

两侧都 stub 掉真引擎/路由/评测: 零 chroma、零 embedding、零 LLM。
"""
from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest
from fastapi import FastAPI

from eval import run_eval as ev
from server import main as main_mod
from server import study_corpus as sc
from server import study_lookup as study_lookup_mod
from server.config import Settings, settings

# 工厂自己写死/自己填的那组键。lever 不在此列 —— 生产取 settings、eval 取 args 覆盖是
# spec §4.6 明确保留的差异 (被钉住的是装配方式, 不是取值来源)。
STRUCTURAL = ("chroma_dir", "kb_root", "collection_name", "embedding_model",
              "top_k", "structured_lookup_enabled")

# 生产 lifespan 对 rerank/expansion 一个字都不传 (cards 引擎同样不传, main.py:122-135 ⇒
# 两台一起吃 RAGEngine 默认值), eval 侧则必须从 args 取。这是两条路径唯一允许的键集差。
EVAL_ONLY_LEVERS = {"rerank_enabled", "rerank_model", "rerank_candidates",
                    "query_expansion", "expansion_model", "expansion_n_queries"}


class _Stop(Exception):
    """哨兵: eval 侧装配一完成就停, 不进 run_evaluation。"""


def _fake_lookup(catalog_path, aliases_path):
    # catalog.json 按数据红线不进 git ⇒ 不 stub 则裸检出里这些测试全 FileNotFoundError
    return SimpleNamespace(stats=lambda: "7 items/0 aliases")


@pytest.fixture
def prod_boot(monkeypatch):
    """跑生产 lifespan, 交出按构造顺序排的 kwargs 列表 [cdisc, cards, docs]。"""
    engines: list[dict] = []

    class FakeEngine:
        def __init__(self, **kwargs):
            engines.append(kwargs)
            self.kwargs = kwargs
            self.collection = SimpleNamespace(count=lambda: 0)
            self.system_prompt = "SYS"

        def _vi_section_map(self):
            return {}

    monkeypatch.setattr(main_mod, "RAGEngine", FakeEngine)
    monkeypatch.setattr(main_mod, "create_router", lambda s: SimpleNamespace(model_list=[]))
    monkeypatch.setattr(main_mod, "SpecLoader",
                        lambda root: SimpleNamespace(domains=[], codelists=[]))
    monkeypatch.setattr(study_lookup_mod.StudyLookup, "from_paths",
                        staticmethod(_fake_lookup))

    def _run(**overrides):
        app = FastAPI()
        app.state.settings = Settings(
            federation_enabled=True, study_docs_enabled=True, **overrides)

        async def go():
            async with main_mod.lifespan(app):
                pass

        asyncio.run(go())
        # 本次 boot 实际用的 Settings。lever **取值**断言必须对着它, 不能对着模块级 settings
        # 单例的值再抄一份常量 —— 那样断的是"本机 .env 长什么样"而不是"生产把 settings 传
        # 下去了" (见 test_prod_docs_engine_carries_every_lever_its_cards_engine_carries)。
        _run.settings = app.state.settings
        return engines

    return _run


@pytest.fixture
def eval_boot(monkeypatch, tmp_path):
    """跑 run_eval.main() 到 retriever 装配完为止, 交出 [cdisc, cards, docs]。"""
    engines: list[dict] = []

    class FakeEngine:
        def __init__(self, **kwargs):
            engines.append(kwargs)
            self.__dict__.update(kwargs)   # 屏幕回执要读 rerank_model / query_expansion 等
            self.collection = SimpleNamespace(count=lambda: 0)

    monkeypatch.setattr(ev, "RAGEngine", FakeEngine)
    monkeypatch.setattr(ev, "create_router", lambda s: SimpleNamespace(model_list=[]))
    monkeypatch.setattr(ev, "FederatedEngine",
                        lambda *a, **kw: SimpleNamespace(
                            retrieve=lambda q, corpus, top_k: ([], corpus)))
    monkeypatch.setattr(ev, "run_evaluation",
                        lambda *a, **kw: (_ for _ in ()).throw(_Stop()))
    monkeypatch.setattr(study_lookup_mod.StudyLookup, "from_paths",
                        staticmethod(_fake_lookup))

    ts = tmp_path / "t.yml"
    ts.write_text("- id: q1\n  category: c\n  question: x\n  expected_sources: [a.md]\n")

    def _run(*extra):
        with pytest.raises(_Stop):
            ev.main([str(ts), "--retrieval-only", "--federated", "--study-docs", *extra])
        return engines

    return _run


def test_both_paths_build_the_docs_engine_through_the_one_factory(
    prod_boot, eval_boot, monkeypatch
):
    """绕过工厂直接 `RAGEngine(...)` 抄一份参数, kwargs 可以逐键相同 ⇒ 只比 kwargs 抓不到。

    所以调用本身要钉: 哪条路径不走工厂, 它那次计数就不涨, 而"参数清单又被抄成两份"正是
    本 task 要消灭的东西。
    """
    calls: list[dict] = []
    real = sc.make_docs_engine

    def _spy(*a, **kw):
        calls.append(kw)
        return real(*a, **kw)

    monkeypatch.setattr(sc, "make_docs_engine", _spy)

    prod_boot()
    assert len(calls) == 1, "server/main.py 的 lifespan 没走工厂"
    eval_boot("--doc-seats", "7")
    assert len(calls) == 2, "eval/run_eval.py 的 --study-docs 分支没走工厂"


def test_the_two_paths_hand_the_docs_engine_identical_structural_kwargs(
    prod_boot, eval_boot
):
    """本 task 的核心断言 —— 两个 dict 相等。

    ⚠ 相等是**对调/共错盲区**最重的那种形状: 两条路径同时指到卡片库、同时把 S1 打开、
    同时把席位读成 args.top_k, 三种情形下这条断言全都照绿。故相等之后逐条钉方向。
    """
    prod = prod_boot(study_docs_seats=7)[2]
    evl = eval_boot("--doc-seats", "7")[2]

    assert {k: prod[k] for k in STRUCTURAL} == {k: evl[k] for k in STRUCTURAL}

    # ── 方向 (相等不说"等在哪个值上") ──
    assert prod["collection_name"] == settings.study_docs_collection_name
    assert prod["collection_name"] != settings.study_collection_name
    assert prod["kb_root"] == settings.study_kb_root      # 与 U1 上界口径逐字相同
    assert prod["top_k"] == 7                             # 席位数, 不是全局 top_k
    # ⚠ 此处原有一条 `prod["top_k"] != settings.top_k`, 已删: `Settings` 走 env_prefix
    #   SDTM_RAG_ 且 config.py import 期就 load_dotenv ⇒ 有人把 SDTM_RAG_TOP_K 设成 7,
    #   这条就伪红 (量的是本机环境而不是代码)。"cards 拿全局 top_k、docs 拿席位"这个方向
    #   由下面两条同源测试里的 `cards["top_k"] == …top_k and docs["top_k"] == 7` 承担。
    assert prod["structured_lookup_enabled"] is False     # S1 是 CDISC 专属

    # S2 的数据源是 catalog.json, 对 doc chunk 无定义 ⇒ 两条路径都不许把它传进来
    # (传 None 也不行: 那会掩盖 docs 引擎被误配成直查通道的情形)
    assert "study_lookup" not in prod and "study_lookup" not in evl

    # 键集差也要钉死: 少一个键 = 悄悄吃 RAGEngine 默认值, 上面的值比对看不见。
    assert set(prod) - set(evl) == set()
    assert set(evl) - set(prod) == EVAL_ONLY_LEVERS


def test_eval_docs_engine_carries_every_lever_its_cards_engine_carries(eval_boot):
    """Task 3 的实际缺陷: eval 侧 docs 引擎少了 rerank/expansion 三族, 吃默认值。

    默认值恰好等于 settings 出厂值 ⇒ 不跑 `--rerank` 永远看不出来; 一旦跑, 三台引擎
    (cdisc / cards / docs) 口径不一致而数字不会有任何提示。这里把每个 lever 都给一个
    **非默认**值, 使"没传"与"传了默认值"可分。
    """
    engines = eval_boot("--doc-seats", "7", "--rerank", "--rerank-candidates", "33",
                        "--query-expansion", "multiquery", "--hybrid",
                        "--hybrid-fusion", "weighted", "--hybrid-alpha", "0.7",
                        "--hybrid-pool", "41", "--guardrail")
    cards, docs = engines[1], engines[2]

    assert set(cards) - set(docs) == {"study_lookup"}
    assert set(docs) - set(cards) == set()
    assert {k for k in docs if cards[k] != docs[k]} == {"collection_name", "top_k"}

    # 差集不说谁是谁 —— 实测把两台的 top_k 对调后差集一字不变、全量全绿, 而那正是
    # "加席不抢席"的反面 (真 cards 降成 7 席查 959 张卡, docs 拿 15 席查 114 条章节)。
    assert cards["top_k"] == ev.TOP_K and docs["top_k"] == 7
    assert cards["collection_name"] == settings.study_collection_name
    assert docs["collection_name"] == settings.study_docs_collection_name

    # 值必须真的跟着 CLI 走 (全部取非默认值, 与"两台一起吃出厂值"可分)
    assert docs["rerank_enabled"] is True and docs["rerank_candidates"] == 33
    assert docs["query_expansion"] == "multiquery"
    assert docs["hybrid_enabled"] is True and docs["hybrid_fusion"] == "weighted"
    assert docs["hybrid_alpha"] == 0.7 and docs["hybrid_pool"] == 41
    assert docs["prompt_guardrail_enabled"] is True

    # 无 CLI 覆盖的两个键: 只比"两台相同"时**两台一起指错**照样绿 (抽检方 B 的 S2: 四台
    # study 引擎的 embedding_model 一起换成 bogus 值 ⇒ 全量全绿)。用与索引期同一个
    # settings 取值钉方向 —— 生产用与索引不同的 embedding = 检索静默崩塌 (不报错, 只是
    # 全查不中); chroma_dir 指错则是查了另一份库。
    assert docs["embedding_model"] == settings.embedding_model
    assert docs["chroma_dir"] == settings.chroma_dir


def test_prod_docs_engine_carries_every_lever_its_cards_engine_carries(prod_boot):
    """生产侧同一条不变量的镜像 —— eval 侧那条改红了而这条没有, 就是单边漂移。"""
    engines = prod_boot(study_docs_seats=7)
    cards, docs = engines[1], engines[2]
    assert set(cards) - set(docs) == {"study_lookup"}
    assert set(docs) - set(cards) == set()
    assert {k for k in docs if cards[k] != docs[k]} == {"collection_name", "top_k"}
    assert cards["top_k"] == settings.top_k and docs["top_k"] == 7
    assert cards["collection_name"] == settings.study_collection_name
    assert docs["collection_name"] == settings.study_docs_collection_name

    # ── lever **取值** (生产侧此前一条都没有) ──
    # 上面全是 cards↔docs 自比, 跨路径又只比 6 个 STRUCTURAL 键 ⇒ 把两台 study 引擎的
    # lever **一起**改掉在生产侧完全没人管 (抽检方 B 的 Q: 两台 hybrid_alpha 一起改成
    # 0.99 ⇒ 全量全绿), 而 eval 侧的同类变异 S3 是被杀的 —— 两侧强度不对称。
    # 断的是"生产把 settings 那一份传下去了", 不是"取值等于某个常量": 对着本次 boot 真正
    # 用的 Settings, 故 .env 覆盖任一 lever 时这条跟着走而不会伪红。
    s = prod_boot.settings
    assert docs["hybrid_enabled"] == s.hybrid_enabled
    assert docs["hybrid_fusion"] == s.hybrid_fusion
    assert docs["hybrid_alpha"] == s.hybrid_alpha
    assert docs["hybrid_pool"] == s.hybrid_pool
    assert docs["prompt_guardrail_enabled"] == s.prompt_guardrail_enabled
    # 方向钉 (STRUCTURAL 里比了但没钉方向, 两条路径一起指错就照绿): 生产用与索引不同的
    # embedding = 检索静默崩塌; chroma_dir 指错 = 查的是另一份库。
    assert docs["embedding_model"] == s.embedding_model
    assert docs["chroma_dir"] == s.chroma_dir
