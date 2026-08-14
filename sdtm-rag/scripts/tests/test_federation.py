"""Plan B Phase 1: route_corpus + FederatedEngine (spec §1.1-1.3).

路由是全计划唯一非确定性组件 — 测试全部用 fake llm_router 钉死行为边界:
合法 JSON 三值 / 包噪声 JSON / 非法值 / 异常 → 兜底 both (宁可多查)。
引擎侧用 stub (duck-typed), 不碰 chroma。
"""
from types import SimpleNamespace

import pytest

from server.federation import _ROUTER_SYSTEM, VALID_CORPORA, FederatedEngine, route_corpus
from server.rag import RetrievedChunk


def _resp(text):
    return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=text))])


class _FakeLLM:
    def __init__(self, text=None, exc=None):
        self.text, self.exc, self.calls = text, exc, []

    def completion(self, model, messages, **kw):
        self.calls.append({"model": model, "messages": messages, **kw})
        if self.exc:
            raise self.exc
        return _resp(self.text)


class _StubEngine:
    def __init__(self, name, n=20):
        self.name = name
        self.system_prompt = f"SYS-{name}"
        self._chunks = [
            RetrievedChunk(chunk_id=f"{name}-{i}", source=f"{name}/f{i}.md",
                           domain=None, file_type=None, section=None,
                           similarity=0.9 - i * 0.01, text=f"t{i}")
            for i in range(n)
        ]
        self.retrieve_kwargs = None

    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        self.retrieve_kwargs = {"domain": domain, "file_type": file_type, "top_k": top_k}
        return self._chunks[: (top_k or 15)]

    def format_context(self, chunks):
        return f"CTX-{self.name}({len(chunks)})"

    def build_messages(self, q, ctx, history=None):
        return [{"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"{ctx}\n{q}"}]


# ── _ROUTER_SYSTEM 事实描述 ──

def test_router_prompt_describes_the_study_document_corpus():
    """C1 之后 study 库里除了 EDC 卡片还有本研究自己的手順/計画文書章节 chunk。

    判库 prompt 里 study 的语料描述若仍只写 field cards, 偏"标准味"的手順問題会被判给
    cdisc, 而 CDISC 库结构上答不出本研究的手順 (该题 recall 归零)。

    ⚠ 断言范围只取 study 那一条 bullet, 不是整段 prompt: 规则 1 的正文里早就有
    "our protocol" 这个词 (第一人称叙事的例子), 所以 `"protocol" in _ROUTER_SYSTEM.lower()`
    这种整段断言在改动**之前**就是绿的 = 装饰品, 不能用。
    """
    study_bullet = _ROUTER_SYSTEM.split("Decide which corpus")[0].split('- "study":')[1]
    assert "field cards" in study_bullet, "study 语料描述必须仍包含 EDC 卡片"
    low = study_bullet.lower()
    assert "protocol" in low and "section" in low, (
        "study 语料描述必须写明本研究自己的手順/計画文書章节 (protocol/procedure document sections)"
    )


# 三条规则之后的收尾段 (讲兜底取舍) 的起始锚点。三条规则各自的正文都切到它为止。
_TAIL_MARKER = "\nWhen one of the three rules"


def test_router_prompt_tail_anchor_is_intact():
    """锚点自检: 下面几条切片测试全靠 _TAIL_MARKER 定位收尾段。

    锚点一旦被改没 (第 5 轮就把收尾段首句从 "Never guess…" 换成了别的), 切片会**静默**地
    连收尾段一起吞进规则 3, 断言可能因此恒绿。这条让锚点失效直接变红, 而不是悄悄退化。
    """
    assert _ROUTER_SYSTEM.count(_TAIL_MARKER) == 1


def _rule_segment(n: int) -> str:
    """取 _ROUTER_SYSTEM 里第 n 条规则的正文段 (不含其他规则与收尾段)。

    与上一条测试同理由: 整段 prompt 断言在改动**之前**多半已经是绿的 (例如 "even when"
    在规则 1/2 里早就有), 那种断言是装饰品。规则级切片才能让变异 (删掉新增规则文本) 变红。
    """
    seg = _ROUTER_SYSTEM.split(f"\n{n}. ")[1]
    for tail in (f"\n{n + 1}. ", _TAIL_MARKER):
        seg = seg.split(tail)[0]
    return seg


def test_router_prompt_tail_keeps_both_as_the_safe_fallback():
    """收尾段被重写 (U3 Task 7 第 5 轮) 后, 安全意图必须仍在。

    第 5 轮删掉的是"默认值 = both"那半句 (它把有规则明确覆盖的题也拽去 both);
    **不得**顺手删掉真不确定时退到 both 的指示 —— 那会把判库从"宁可多查"翻成"敢猜单库",
    漏查不可恢复。这条钉住三件事: 无法归类 → both / 单库判错不可恢复 / 不许猜单库。
    """
    tail = _ROUTER_SYSTEM.split(_TAIL_MARKER)[1].split("\nRespond with ONLY")[0].lower()
    assert "cannot place it" in tail, "必须保留「无法归入任一规则 ⇒ both」"
    assert '"both"' in tail
    assert "unrecoverable" in tail, "必须保留「单库判错不可恢复」这条取舍理由"
    assert "never guess a single corpus" in tail, "必须保留「不许猜单库」"


def test_router_prompt_covers_study_own_definitions():
    """规则 1 侧: 必须显式覆盖「本研究自己规定的分類/判定/定義」这一类。"""
    rule1 = _rule_segment(1)
    assert "手順" in rule1 or "計画文書" in rule1, (
        "规则 1 必须写明这类问题指向本研究自己的手順/計画文書 (→ 规则 2)"
    )
    # 判别器是「问题的对象」而非临床主题
    assert "object of the question" in rule1


def test_router_prompt_covers_unmarked_both():
    """规则 3 侧: 必须覆盖「无标准侧显式标记的真两可」形态。"""
    low = _rule_segment(3).lower()
    assert "without" in low or "even when" in low


def test_router_prompt_carries_no_heldout_clinical_terms():
    """反对症下药闸: 规则文本不得出现 held-out 题的临床概念。

    词表**不写在这里** —— 写进 tracked 的测试文件等于把「held-out 是关于什么的」
    交给任何读它的人。词表由 controller 预置在 gitignored 文件里,
    实现方不需要、也不许打开它。

    ⚠ 本闸**失败时也不能泄漏**: pytest 的断言改写会把被断言表达式里的值打进输出, 所以
    断言只落在 int 上 —— 词表本身和命中的词都不进任何 assert 表达式, 也不进失败消息。
    末尾的 del 是同一考虑的第二道: 万一有人带 --showlocals 跑, 局部变量里也没有词表。
    """
    from pathlib import Path
    p = Path("data/study/st01/eval/heldout_banned_terms.txt")
    assert p.exists(), f"{p} 缺失 —— 本闸无词表则恒绿, 拒绝静默通过"
    banned = [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines()
              if ln.strip() and not ln.startswith("#")]
    n_terms = len(banned)
    assert n_terms > 0, f"{p} 为空 —— 空词表恒绿, 拒绝静默通过"
    n_hits = sum(w in _ROUTER_SYSTEM for w in banned)
    del banned
    assert n_hits == 0, f"规则文本泄漏 held-out 概念 ({n_hits} 个, 内容不打印以免二次泄漏)"


# ── route_corpus ──

@pytest.mark.parametrize("corpus", VALID_CORPORA)
def test_route_valid_json(corpus):
    got, fallback = route_corpus(_FakeLLM(f'{{"corpus": "{corpus}"}}'), "q")
    assert got == corpus and fallback is False


def test_route_json_embedded_in_prose():
    got, fallback = route_corpus(_FakeLLM('Sure! {"corpus": "study"} hope that helps'), "q")
    assert got == "study" and fallback is False


@pytest.mark.parametrize("bad", ['{"corpus": "everything"}', "not json", ""])
def test_route_bad_output_falls_back_both(bad):
    got, fallback = route_corpus(_FakeLLM(bad), "q")
    assert got == "both" and fallback is True


def test_route_exception_falls_back_both():
    got, fallback = route_corpus(_FakeLLM(exc=RuntimeError("timeout")), "q")
    assert got == "both" and fallback is True


def test_route_actually_sends_the_router_prompt_and_the_question():
    """上一条只钉 prompt 常量的**内容**; 这条钉它确实被**送出去**。

    变异实证 (2026-08-12, U2 Task 5): 把 route_corpus 送出的 system 换成空串、或把用户问题
    换成空串, 全量 1155 条测试**一条都不红** —— 判库整个 prompt 通道此前零覆盖, 只有跑 181
    题的 run_routing_eval (LLM, 不在 pytest 里) 才看得见。
    """
    llm = _FakeLLM('{"corpus": "cdisc"}')
    route_corpus(llm, "どの項目ですか")
    msgs = llm.calls[0]["messages"]
    assert msgs[0] == {"role": "system", "content": _ROUTER_SYSTEM}
    assert msgs[1] == {"role": "user", "content": "どの項目ですか"}


def test_route_uses_light_model_temperature_zero():
    llm = _FakeLLM('{"corpus": "cdisc"}')
    route_corpus(llm, "q")
    assert llm.calls[0]["model"] == "light" and llm.calls[0]["temperature"] == 0


# ── FederatedEngine ──

def _fed(llm_text='{"corpus": "cdisc"}'):
    cd, st = _StubEngine("cdisc"), _StubEngine("study")
    return FederatedEngine(cd, st, _FakeLLM(llm_text), top_k=15), cd, st


def test_explicit_corpus_skips_llm():
    fed, cd, st = _fed()
    fed.llm_router = _FakeLLM(exc=RuntimeError("must not be called"))
    chunks, routed = fed.retrieve("q", corpus="study")
    assert routed == "study" and all(c.corpus == "study" for c in chunks)
    assert len(chunks) == 15 and cd.retrieve_kwargs is None


def test_auto_routes_via_llm():
    fed, cd, st = _fed('{"corpus": "cdisc"}')
    chunks, routed = fed.retrieve("q", corpus="auto")
    assert routed == "cdisc" and all(c.corpus == "cdisc" for c in chunks)
    assert st.retrieve_kwargs is None


def test_both_quota_ceil_half_each_no_score_sort():
    fed, cd, st = _fed()
    chunks, routed = fed.retrieve("q", corpus="both", top_k=15)
    assert routed == "both"
    assert [c.corpus for c in chunks] == ["cdisc"] * 8 + ["study"] * 8  # ceil(15/2)=8, 分组不混排
    assert cd.retrieve_kwargs["top_k"] == 8 and st.retrieve_kwargs["top_k"] == 8


def test_domain_filter_forwarded_to_cdisc_only():
    fed, cd, st = _fed()
    fed.retrieve("q", corpus="both", domain="AE")
    assert cd.retrieve_kwargs["domain"] == "AE"
    assert st.retrieve_kwargs["domain"] is None


def test_invalid_corpus_rejected():
    fed, _, _ = _fed()
    with pytest.raises(ValueError):
        fed.retrieve("q", corpus="everything")


def test_format_context_groups_by_corpus():
    fed, _, _ = _fed()
    chunks, _ = fed.retrieve("q", corpus="both", top_k=4)
    ctx = fed.format_context(chunks)
    assert "【標準 CDISC】" in ctx and "【本研究 (study)】" in ctx
    assert "CTX-cdisc(2)" in ctx and "CTX-study(2)" in ctx
    assert ctx.index("CDISC") < ctx.index("本研究")


def test_build_messages_system_per_corpus():
    fed, _, _ = _fed()
    single = fed.build_messages("q", "CTX", corpus="study")
    assert single[0]["role"] == "system"
    assert "SYS-study" in single[0]["content"] and "SYS-cdisc" not in single[0]["content"]
    both = fed.build_messages("q", "CTX", corpus="both")
    assert "SYS-cdisc" in both[0]["content"] and "SYS-study" in both[0]["content"]
    # 联邦规则恒在 (标源库 + 跨库推理性标注)
    for msgs in (single, both):
        assert "Federation rules" in msgs[0]["content"]
