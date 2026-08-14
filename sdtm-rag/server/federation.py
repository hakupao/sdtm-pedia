"""Plan B 联邦路由: 双库组合 + LLM 判库 + 配额合并 (spec 2026-08-04 §1).

设计要点:
- 组合而非改造: 两个 RAGEngine 各自保留 BM25 索引 (study 侧天然 CJK bigram) 与直查通道。
- LLM 路由是全计划唯一非确定性组件: temperature 0 + 严格 JSON + 任何异常降级 "both"
  (兜底方向 = 宁可多查不可漏查; 路由准确率由 eval/run_routing_eval.py 三遍闸把守)。
- both 合并不做跨库分数排序 —— 两库相似度分布不可比, 按库配额 ceil(k/2) 分组拼接。
"""
from __future__ import annotations

import json
import math

import structlog

log = structlog.get_logger()

VALID_CORPORA = ("cdisc", "study", "both")

_ROUTER_SYSTEM = """You are a corpus router for a clinical-data Q&A service. Two corpora exist:
- "cdisc": the public CDISC SDTM standard — domains (DM, AE, VS, ...), variables, controlled \
terminology, implementation-guide chapters. English content.
- "study": ONE specific clinical study's own artifacts — its EDC field cards \
(forms/screens, field labels, item groups, display conditions, units) AND that study's own \
protocol / procedure document sections (手順・計画文書の節: eligibility, treatment schedule, \
assessments, statistical plan). Japanese content.
Decide which corpus the question needs, applying these rules in order:
1. "cdisc" — the question is about the standard itself: which domain/dataset a kind of data belongs \
in, what a variable means or which role it has (topic, Required/Expected/Permissible), controlled \
terminology, model or implementation-guide rules, and the conventions data must follow to be \
submitted (date/time representation, units, coding). A standard question stays "cdisc" even when it is \
told as a trial scenario — first-person framing ("in our study", "our protocol", "we collect ...", \
"a subject in our trial") is narrative background and does not by itself require the study corpus. \
What makes a question rule 1 is that it asks about the standard's structure; merely naming a \
clinical concept the standard happens to cover (adverse events, severity grading, lab results, \
dosing) does not. That allowance is about the setting of a question, never about its object: what \
separates rule 1 from rule 2 is the object of the question — the standard's way of representing \
data, or one study's own decision — and not the clinical topic either of them may touch. Test it \
on the answer. If the answer would have to be a fact that only this study's own documents could \
have fixed — how many levels or which categories its own scheme distinguishes, which criterion or \
cut-off it set, which of several possible methods it adopted, how it defines a term for its own \
use, what deadline, duty or handling its own 手順・計画文書 lay down — then no public standard \
contains that answer, whatever clinical concept the question names, the ones listed just above \
included. A standard prescribes how such data is submitted once a study has decided it (which \
dataset it belongs in, which variable carries it, which controlled term is allowed); it never \
prescribes what any single study decided. Route those to rule 2, however standard-flavoured the \
topic sounds. The reverse lock holds too: when the object is what the standard prescribes for such \
data, the question stays rule 1 even though its setting is this study.
2. "study" — the question is about this one study's own data-entry artifacts: whether an item \
exists, whether two related things are captured in one field or in separate fields, how a field is \
labelled, which form/screen/画面 it sits on, its 選択肢 / 単位 / 入力方法, what the site is actually \
asked to enter. Short Japanese questions about 項目 / フィールド / \
フォーム are study questions even when they give little context. Language is not evidence: \
Japanese is both this study's EDC vocabulary and the language its users ask standard questions in, \
so route on the subject alone — a Japanese question about the standard is rule 1, a Japanese \
question about this study's entry items is rule 2, and a Japanese question that could be read \
either way is rule 3. Rule 2 outranks rule 1 whenever the question asks about 項目 / フォーム / \
画面: every user of this service works on this one study, so "項目はありますか" means "does THIS \
study's EDC have such a field" — and no public standard document lists any study's entry items, so \
the standard alone can never answer it, however standard-flavoured the clinical concept sounds. \
Rule 3 in turn outranks rule 2: when the question asks how such an item relates to the standard \
(マッピング / 対応 / どの変数に…), neither corpus alone can answer it — answer "both".
3. "both" — everything else: questions that tie a concrete study EDC item to the SDTM standard \
(mapping), that need facts from both sides, or that you cannot confidently place under rule 1 or \
rule 2. Rule 3 does not require the question to name the standard, but it is a test of necessity, \
not of topic overlap. Ask whether a correct and complete answer would have to state two facts at \
once: one that can only be read off this study's own artifacts (a particular thing it holds, or a \
choice it made) and one that only the public CDISC standard fixes (which dataset or variable such \
data belongs to, which controlled term or submission format applies). Only when the answer is \
incomplete without either of them is it "both", and each half has to be independently necessary. \
The standard half may be implied rather than named: a question asking what becomes of something \
this study holds once it leaves this study's own records — how it has to be represented to be \
submitted — needs the standard side even when it never says 標準 / SDTM / コントロールターミノロジー. \
Nothing else implies either half. Asking where in this study something is entered, recorded or kept \
is rule 2 and carries no implied standard side; and telling a question in the first person, or \
naming this study as whose data is being discussed, never supplies the study half — when \
everything the answer must state comes from the standard, the question is rule 1 no matter whose \
data occasioned it. "The standard side" also means the public CDISC SDTM standard specifically: \
outside laws, guidelines or regulations this study complies with belong to this study's own \
documents, not to the cdisc corpus.
Never guess a single corpus. A wrong single corpus makes the answer unrecoverable, while "both" is \
merely broader — so commit to "cdisc" or "study" only when the question clearly matches that rule, \
and answer "both" in every remaining case.
Respond with ONLY this JSON, nothing else: {"corpus": "cdisc"} or {"corpus": "study"} or {"corpus": "both"}"""

_FEDERATION_RULES = (
    "\n\n## Federation rules\n"
    "- Retrieved context may come from two corpora: 【標準 CDISC】 (public SDTM standard) and "
    "【本研究 (study)】 (this study's EDC field cards). Always state which corpus each claim "
    "comes from.\n"
    "- EDC↔SDTM mapping questions: NO mapping document exists in either corpus — any mapping "
    "you state is inference. Label it explicitly (推測/inference), never present it as documented "
    "fact.\n"
)


def route_corpus(llm_router, question: str) -> tuple[str, bool]:
    """判库. 返回 (corpus, fallback_used). 任何异常 → ("both", True)."""
    try:
        resp = llm_router.completion(
            model="light",
            messages=[
                {"role": "system", "content": _ROUTER_SYSTEM},
                {"role": "user", "content": question},
            ],
            temperature=0,
        )
        raw = (resp.choices[0].message.content or "").strip()
        start, end = raw.find("{"), raw.rfind("}")
        if start < 0 or end <= start:
            raise ValueError(f"no JSON object in router output: {raw!r}")
        corpus = json.loads(raw[start : end + 1])["corpus"]
        if corpus not in VALID_CORPORA:
            raise ValueError(f"invalid corpus {corpus!r}")
        return corpus, False
    except Exception:
        log.warning("route_corpus_fallback_both", exc_info=True)
        return "both", True


class FederatedEngine:
    def __init__(self, cdisc, study, llm_router, top_k: int = 15):
        self.cdisc = cdisc
        self.study = study
        self.llm_router = llm_router
        self.top_k = top_k

    def retrieve(
        self,
        question: str,
        *,
        corpus: str = "auto",
        top_k: int | None = None,
        domain: str | None = None,
        file_type: str | None = None,
    ):
        """返回 (chunks, routed_corpus). domain/file_type 是 CDISC 侧概念, 只透传 cdisc 引擎."""
        if corpus not in ("auto", *VALID_CORPORA):
            raise ValueError(f"corpus must be auto|cdisc|study|both, got {corpus!r}")
        k = top_k or self.top_k
        routed = corpus
        if corpus == "auto":
            routed, fallback = route_corpus(self.llm_router, question)
            log.info("federation_routed", corpus=routed, fallback=fallback)
        if routed == "cdisc":
            chunks = self.cdisc.retrieve(question, domain=domain, file_type=file_type, top_k=k)
            for c in chunks:
                c.corpus = "cdisc"
            return chunks, routed
        if routed == "study":
            chunks = self.study.retrieve(question, top_k=k)
            for c in chunks:
                c.corpus = "study"
            return chunks, routed
        # both: 按库配额, 分组拼接 (cdisc 先), 不做跨库分数排序
        k_each = math.ceil(k / 2)
        cd = self.cdisc.retrieve(question, domain=domain, file_type=file_type, top_k=k_each)
        st = self.study.retrieve(question, top_k=k_each)
        for c in cd:
            c.corpus = "cdisc"
        for c in st:
            c.corpus = "study"
        return cd + st, "both"

    def format_context(self, chunks) -> str:
        cd = [c for c in chunks if c.corpus == "cdisc"]
        st = [c for c in chunks if c.corpus == "study"]
        parts = []
        if cd:
            parts.append("# 【標準 CDISC】\n" + self.cdisc.format_context(cd))
        if st:
            parts.append("# 【本研究 (study)】\n" + self.study.format_context(st))
        return "\n\n".join(parts)

    def build_messages(self, question, context, history=None, *, corpus: str):
        # 委托 cdisc 引擎产出消息结构 (user 消息格式与单库路径逐字节一致), 只替换 system
        msgs = self.cdisc.build_messages(question, context, history)
        msgs[0] = {"role": "system", "content": self._system_for(corpus)}
        return msgs

    def _system_for(self, corpus: str) -> str:
        if corpus == "cdisc":
            base = self.cdisc.system_prompt
        elif corpus == "study":
            base = self.study.system_prompt
        else:
            base = self.cdisc.system_prompt + "\n\n" + self.study.system_prompt
        return base + _FEDERATION_RULES
