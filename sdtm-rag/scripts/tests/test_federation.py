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


_EXPECTED_RULE1_SEGMENT = (
    '"cdisc" — the question is about the standard itself: which domain/dataset a kind of data '
    'belongs in, what a variable means or which role it has (topic, '
    'Required/Expected/Permissible), controlled terminology, model or implementation-guide rules,'
    ' and the conventions data must follow to be submitted (date/time representation, units, '
    'coding). A standard question stays "cdisc" even when it is told as a trial scenario — first-'
    'person framing ("in our study", "our protocol", "we collect ...", "a subject in our trial") '
    'is narrative background and does not by itself require the study corpus. What makes a '
    "question rule 1 is that it asks about the standard's structure; merely naming a clinical "
    'concept the standard happens to cover (adverse events, severity grading, lab results, '
    'dosing) does not. That allowance is about the setting of a question, never about its object:'
    " what separates rule 1 from rule 2 is the object of the question — the standard's way of "
    'representing data, or what this one study runs. Decide it by asking where the answer is '
    "written down. If it could only be written down in this study's own documents and forms — how"
    ' many levels or which categories a scheme it applies distinguishes, which criterion or cut-'
    'off it set, which of several possible methods it adopted, how it defines a term for its own '
    'use, what an instrument it administers actually contains, what deadline, duty or handling '
    'its own 手順・計画文書 lay down — then no public standard holds that answer, whatever clinical '
    'concept the question names, the ones listed just above included: that is rule 2, answer '
    '"study". Adopting something defined outside this study does not hand it to the standard: a '
    'standard describes how collected data is submitted (which dataset it belongs in, which '
    'variable carries it, which controlled term is allowed), never what any one study runs or how'
    ' any clinical instrument reads. The reverse is just as strict: when the answer is written '
    'down in the standard, the question is rule 1 and stays "cdisc" even though its setting is '
    'this study, and even though the data being discussed was collected here.'
)

_EXPECTED_RULE3_SEGMENT = (
    '"both" — everything else: questions that tie a concrete study EDC item to the SDTM standard '
    '(mapping), that need facts from both sides, or that you cannot confidently place under rule '
    '1 or rule 2. Rule 3 does not require the question to name the standard, but it is a test of '
    'necessity, not of topic overlap. Settle it with two separate look-ups. First: to answer, '
    "would you have to open this study's own artifacts and look up something particular of its "
    'own — an item, a value, an option, a definition? Second: would you have to consult the '
    'public CDISC standard — which dataset or variable such data belongs to, which controlled '
    'term or submission format applies? Answer "both" only when both look-ups are needed. The '
    'standard look-up can be needed without being named: asking what becomes of something this '
    "study holds once it leaves this study's own records — how it has to be represented in order "
    'to be submitted — needs it even when the question never says 標準 / SDTM / コントロールターミノロジー. '
    'Nothing else adds a look-up. A question you can answer from the standard alone is rule 1 '
    'however much study scenery it carries: first-person framing, naming this study, saying whose'
    ' data it is, or noting that the data was collected here adds no study look-up. A question '
    "you can answer from this study's artifacts alone is rule 2, and that includes asking where "
    'in this study something is entered, recorded or kept. Outside laws, guidelines or '
    "regulations this study complies with are documented on this study's side, not in the CDISC "
    'standard.'
)

_EXPECTED_TAIL_SEGMENT = (
    'When one of the three rules plainly covers the question, apply it and let it settle the '
    'answer: a clinical topic that sounds like the other corpus is not a reason to hesitate, and '
    '"both" is not a way of avoiding the decision. Real uncertainty is the other case, and there '
    '"both" is right: when the question genuinely needs facts from both sides, or when you cannot'
    ' place it under any one rule, answer "both" — a wrong single corpus makes the answer '
    'unrecoverable, while "both" is merely broader. Never guess a single corpus to look decisive.'
)

# ── 切片锚点与逐字期望值 ──────────────────────────────────────────
#
# 审阅 Important-1 (task-7-review.md §2): 第 5 轮交付的 5 条 prompt 测试对**语义反转**零抵抗 ——
# 审查方 6 个变异全部存活, 其中 M6 只改 1 个字符 (兜底段 answer "both" → answer "study") 却全绿,
# 因为断言是「四个子串各自存在」而不是它们的**合取**, 而那几个子串在段内别处独立满足。
# 修法 (修复轮 1): 每段做**两级**断言 —— 语义级 (句内合取 / 整句在) + 逐字级 (整段精确相等)。
# 逐字级是必须的: 子串断言挡不住**追加**一句反向指示 (M3), 只有整段相等挡得住。
# _ROUTER_SYSTEM 是无开关的生产常量, 改它就是改生产, 因此"改 prompt 必须同时改测试"是刻意的设计。

# 三条规则之后的收尾段 (讲兜底取舍) 的起始锚点。三条规则各自的正文都切到它为止。
_TAIL_MARKER = "\nWhen one of the three rules"

_PIN_HINT = (
    "本段与逐字期望值不符。这不是测试坏了 —— _ROUTER_SYSTEM 是无开关的生产判库 prompt, "
    "任何改动都必须连同本期望值一起改, 并在 code review 里被看见。"
    "若确属有意改动: 更新对应的 _EXPECTED_* 常量, 并复跑可见集回归 (报告 §10.8 的命令)。"
)

# 规则 1 的反向锁整句: 干扰组 (对象在标准侧 + 场景在本研究) 的唯一保护句。
# 审查方 M2 把这句整条删掉, 5 条测试全绿 —— 故单独钉一次, 让失败消息指得准。
_RULE1_REVERSE_LOCK = (
    "The reverse is just as strict: when the answer is written down in the standard, the question "
    'is rule 1 and stays "cdisc" even though its setting is this study, and even though the data '
    "being discussed was collected here."
)

# 规则 3 的必要性判据整句 (AND, 不是 OR)。审查方 M1 把它改成 either 即 AND→OR, 全绿。
_RULE3_NECESSITY = 'Answer "both" only when both look-ups are needed.'

# 兜底段的安全句**整句**。审阅 Minor-2(b): 第 5 轮给它加了目的状语 "to look decisive",
# 而原断言只取前缀子串 `never guess a single corpus`, 限定加不加都绿 —— 故改钉整句。
_TAIL_NEVER_GUESS = "Never guess a single corpus to look decisive."


def test_router_prompt_slice_anchors_are_unique():
    """锚点自检 (审阅 I-1 附带项): 四个切片锚点各自必须唯一。

    锚点失效时切片会**静默**地把别的段一起吞进来, 断言可能因此恒绿。
    第 5 轮就发生过一次: 收尾段首句从 "Never guess…" 换掉, 旧尾锚点当场失效。
    原先只有 _TAIL_MARKER 有唯一性自检, 现在三个规则锚点同等对待。
    """
    for anchor in ("\n1. ", "\n2. ", "\n3. ", _TAIL_MARKER):
        assert _ROUTER_SYSTEM.count(anchor) == 1, f"切片锚点 {anchor!r} 不唯一 (切片会静默错位)"


def test_router_prompt_tail_anchor_is_intact():
    """收尾段锚点存在性 (保留独立一条, 失败消息比上一条更直接)。"""
    assert _ROUTER_SYSTEM.count(_TAIL_MARKER) == 1


def _rule_segment(n: int) -> str:
    """取 _ROUTER_SYSTEM 里第 n 条规则的正文段 (不含其他规则与收尾段)。

    整段 prompt 的子串断言多半在改动**之前**就是绿的 (例如 "even when" 在规则 1/2 里早就有),
    那种断言是装饰品。规则级切片才能让变异变红。
    """
    seg = _ROUTER_SYSTEM.split(f"\n{n}. ")[1]
    for tail in (f"\n{n + 1}. ", _TAIL_MARKER):
        seg = seg.split(tail)[0]
    return seg


def _tail_segment() -> str:
    """取三条规则之后的收尾段 (不含结尾的 JSON 输出说明)。"""
    return _TAIL_MARKER.lstrip("\n") + _ROUTER_SYSTEM.split(_TAIL_MARKER)[1].split(
        "\nRespond with ONLY")[0]


def _sentence_containing(text: str, needle: str) -> str:
    """取 text 里包含 needle 的**那一句**。找不到就 raise (断言用, 不许静默放过)。"""
    for s in text.split(". "):
        if needle in s:
            return s
    raise AssertionError(f"收尾段里找不到含 {needle!r} 的句子")


def test_router_prompt_tail_keeps_both_as_the_safe_fallback():
    """收尾段 (第 5 轮重写) 的安全意图必须仍在。

    第 5 轮删掉的是"默认值 = both"那半句 (它把有规则明确覆盖的题也拽去 both);
    **不得**顺手删掉真不确定时退到 both 的指示 —— 那会把判库从"宁可多查"翻成"敢猜单库",
    而漏查不可恢复。

    ⚠ 本 docstring 的保证范围 (审阅 I-1 点名: 声称钉死而未钉死比没有测试更危险):
    - 钉得住: 「无法归类」与「答 both」在**同一句**内 (句级合取, 不是两个分离的存在性断言) /
      该句不得改判任何单库 / 「不可恢复」这条理由在同一句内 / 安全句**整句**在 /
      收尾段**逐字**不变 (因此**追加**一句"拿不准就挑最像的单库"也会红)。
    - 钉不住: prompt 之外的任何东西 —— 这里只证明**文本**没被改坏,
      判库实际行为仍要靠可见集回归与 held-out 全闸说话。
    """
    tail = _tail_segment()
    uncertainty = _sentence_containing(tail, "cannot place it")
    assert 'answer "both"' in uncertainty, (
        "「无法归入任一规则」必须与「answer \"both\"」在同一句内 —— "
        "分成两个独立的存在性断言时, 把该句改判单库仍会全绿 (审查方 M6)"
    )
    for single in ('answer "study"', 'answer "cdisc"'):
        assert single not in uncertainty, f"真不确定时不得指示单库 ({single})"
    assert "unrecoverable" in uncertainty, "「单库判错不可恢复」必须在同一句内作为取舍理由"
    assert _TAIL_NEVER_GUESS in tail, "必须保留「不许猜单库」整句 (前缀子串不算, 见 Minor-2b)"
    assert tail == _EXPECTED_TAIL_SEGMENT, _PIN_HINT


def test_router_prompt_covers_study_own_definitions():
    """规则 1 侧: 「本研究自己规定的分類/判定/定義 → study」这条, 以及它的反向锁。

    保证范围: 判别器是「问题的对象」/ 排除条款给出**明确单库结论** /
    反向锁**整句**在 (干扰组的唯一保护句, 审查方 M2 曾整句删除而全绿) / 整段逐字不变。
    """
    rule1 = _rule_segment(1)
    assert "手順" in rule1 or "計画文書" in rule1, (
        "规则 1 必须写明这类问题指向本研究自己的手順/計画文書 (→ 规则 2)"
    )
    # 判别器是「问题的对象」而非临床主题
    assert "object of the question" in rule1
    assert 'that is rule 2, answer "study"' in rule1, "排除条款必须给出明确的单库结论"
    assert _RULE1_REVERSE_LOCK in rule1, "反向锁整句必须在 —— 它是干扰组保护的承载句"
    assert rule1 == _EXPECTED_RULE1_SEGMENT, _PIN_HINT


def test_router_prompt_covers_unmarked_both():
    """规则 3 侧: 「无标准侧显式标记的真两可」入口, 以及双查阅判据的 AND 语义。

    保证范围: 必要性判据**整句**在且是 AND (审查方 M1 把它改成 either 即 AND→OR, 曾全绿) /
    无标记入口在 / 整段逐字不变。
    """
    rule3 = _rule_segment(3)
    assert _RULE3_NECESSITY in rule3, (
        "双查阅判据必须是 AND (两次查阅都需要才 both); 改成 either 就是第 4 轮 185/193 的病因"
    )
    assert "without being named" in rule3, "「标准侧可以不被点名」这个入口必须在"
    assert rule3 == _EXPECTED_RULE3_SEGMENT, _PIN_HINT


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
