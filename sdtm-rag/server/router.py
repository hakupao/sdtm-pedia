"""API routes for SDTM RAG Q&A + Dataset Validation (Phase 1B + 1C)."""
from __future__ import annotations

import asyncio
import datetime
import json
import math
import time
from typing import Literal

import structlog
from fastapi import APIRouter, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, ConfigDict, Field

from server.config import SelectableModel
from server.llm_config import fell_back, known_model_groups, merge_reported_model
from server.web_search import WEB_TOOL_SPEC, WebSearcher, render_tool_result

log = structlog.get_logger()
api_router = APIRouter(prefix="/api")

# 单库 RAGEngine.format_context 在零 chunk 时返回的哨兵句 (server/rag.py)。联邦层的
# format_context 两组都空时返回空串 —— 空 context 会让模型以为"上下文段落缺失"而自由
# 发挥, 所以联邦路径在这里补回同一句, 与单库路径逐字节一致 (漂移由测试钉住)。
_NO_CONTEXT = "(No relevant context found in the knowledge base.)"

# 联网失败的严重度序 (F-10): 一次都没成功时报"最严重"的那个, 而不是"最后一个"。
# disabled (没配 key, 永远不会成) > quota_exceeded (今天的预算用光) > failed (可能是瞬时的)。
# 只有真打了网的尝试才进这张表 —— 模型自己出错 (bad_query / unknown_tool) 不算联网失败。
_WEB_FAIL_RANK = {"disabled": 3, "quota_exceeded": 2, "failed": 1}

# 「这一轮是被输出上限切断的」的两种拼法。OpenAI / litellm 归一化成 "length";
# Anthropic 原生 (以及部分透传的 Bedrock 路径) 报 "max_tokens"。⛔ 只认一个的话,
# 另一条路上的截断依旧是静默的 —— 而静默截断正是本功能要消灭的东西。
_TRUNCATED_FINISH_REASONS = frozenset({"length", "max_tokens"})

# 非流式 `/api/ask` 再开一轮续写所需的**最小剩余预算** (秒)。低于它就收手并如实报
# truncated —— 明知剩下的时间接不完还硬开一轮, 只会让客户端先超时、服务端白烧钱。
# 15 秒是"一轮起码得跑得起来"的量级估计, 不是实测阈值; 调它不影响正确性, 只影响
# "临界情况下多试一轮还是少试一轮"。
_CONTINUE_MIN_REMAINING_S = 15.0

# 触顶后回灌给模型的续写指令。
#
# ⚠ 为什么是**追加一条 user 消息**而不是 assistant prefill: prefill (把上一轮原文塞成
# 最后一条 assistant 消息、让模型接着补全) 是 Anthropic 特有能力, 走 Bedrock Converse 的
# 两个 OpenAI 模型 (gpt-terra / gpt-sol) 不支持 —— 同一段代码要服务四个可选模型加
# DeepSeek 兜底, 只能用所有 provider 都认的形状。代价是接缝处依赖模型听话 (可能重复
# 半句), 换来的是"四个模型一视同仁", 见 evidence/checkpoints/autocontinue_2026-09.md。
#
# 用英文写: 系统提示里的接地规则 ([Source: path] / [Web: url]) 本身是英文, 续写指令跟着
# 用英文可以逐字引用它们, 不必翻译一遍再指望模型对上号。
CONTINUE_PROMPT = (
    "Your previous message was cut off by the output length limit. Continue EXACTLY "
    "from where it stopped: do not repeat any already-written text, do not add a "
    "preamble, heading, apology or summary, keep the same language, formatting and "
    "citation rules ([Source: path] / [Web: url] verbatim)."
)

# C2R 画面 PDF 旁路 (I2-3)。画像が付いたときだけ system prompt の末尾に足す 1 文。
# ⛔ 常時足してはいけない: 画像が無い回答で「画面目視判読」という出典名だけが存在すると、
# モデルがそれを**使ってよい出典**と読み、カードから読んだ事実に画面の看板を付けかねない。
# 文面が日本語なのは study 側 prompt の既存規則 (_DOC_CORPUS_RULES / L1) と揃えるため。
# 2 条目 (N1) は「添付頁 = ブロックの一部」の明示。label に範囲を書くだけでは、
# 「無い」と言い切る前に範囲を限定する義務が生じない —— V3 の opus-5 は T3/T6 で
# 添付された先頭頁の不在をブロック全体の不在に外推し、同型の contradiction を出した。
# ⛔ 限定が掛かるのは**画面由来の否定だけ**。カード事実 (非表示アクティビティ 等) は
# 画面を見なくても確定しており、そこまで一緒に濁らせると T1④/T5③ 型の正解
# (「この活動では出ない」と言い切る答え) が hedge に化けて落ちる。
_PDF_SOURCE_RULE = (
    "\n- 画面ページ画像が添付されている場合、そこから読み取った事実は必ず"
    "『画面目視判読 p.NN』として出典を分け、カード事実・標準引用と混ぜない。\n"
    "- label の頁索引メタに『p.a–b のうち本頁 p.x』と書かれた頁は、そのブロックの一部しか"
    "添付されていない。"
    "添付頁に無いことは、そのフォーム / 活動の画面に無いことを意味しない。画面由来の"
    "否定の断定 (「表示されない」「描画されていない」等) は必ず「添付頁 p.x の範囲では」と"
    "限定し、未添付頁の内容は断定しない。カード事実 (非表示アクティビティ 等) に基づく"
    "否定は画面由来ではないので、この限定の対象外。\n"
    # N3 (b): 索引由来のメタ (範囲 / 同一画面 / グループ順) が『画面目視判読 p.NN』の出典で
    # 引用された 3 件 (N2 の census)。底の事実は正しいのに、その頁にそんな注記は無い ——
    # 出典を分ける規則が「画像から読んだもの」しか定義していなかったのが穴。
    # ⚠ ここに画像由来の出典名を**そのまま書かない**: 文中に 2 度目が現れた時点で、
    # モデルは画像を見ずに出典名を選べるようになる (wiring テストが出現回数を 1 に釘付け)。
    "- label の『頁索引メタ:』以降 (ブロック範囲 / 同一画面 / 本頁の項目グループ順 / 本頁の枠 /"
    " 前頁からの続き / 次頁へ続く) は"
    "頁索引が持っている情報であって、画像から読み取った事実ではない。引用する場合は出典を"
    "『頁索引』とし、画像由来の出典名を付けない。項目グループ順は画面上の枠 (パネル) の"
    "境界と並び順に対応し、見出しの無い枠 (label では『(無題)』) も独立した 1 つの枠として"
    "数える。『前頁からの続き』と書かれた枠は見出しが前頁にあり、本頁には見出しが"
    "描画されていない。\n"
    # N4: 印が無いことと「なし」と書いてあることはモデルには別物。1 枠の頁で label が
    # 沈黙すると、視覚から「前頁からの続きの可能性あり」を作った (N3 a2 の残り 1 件、
    # 実物は上辺が閉じて次頁へ続く)。索引が状態を宣言する以上、画像から読み取った内容は
    # それを超えない。(⚠ 注釈にも「画面判読」という語を書かない —— 次の編集者が注釈から
    # 語を写すと MAJOR-2 が戻る。)
    # 複審 MAJOR-1: 「なし = 見出しは本頁にある」は無題枠 (実データ: 単枠無題 12 頁中 10 頁が
    # continued=false) には嘘。無題枠に見出しを探しに行かせると N3 (a) の「先頭項目の
    # ラベルを組名にする」を呼び戻す。MAJOR-2: 出典様式の名詞を新しく作らない
    # (「画面判読」は N2 閘の正規表現に掛からず、閘が失明する)。
    "- 頁索引メタの『前頁からの続き: あり/なし』『次頁へ続く: あり/なし』は頁索引が"
    "確定している連続状態である。『前頁からの続き: なし』は先頭の枠が本頁で始まることを、"
    "『前頁からの続き: あり』は先頭の枠の見出しが前頁にあることを意味する (見出しのある枠が"
    "本頁で始まるなら、その見出しは本頁に描画されている。『(無題)』の枠は見出しそのものが"
    "存在しないので、その枠の見出しを画像の中に探さない —— 先頭の項目ラベルを枠の名前として"
    "報告しない)。『次頁へ続く: なし』は末尾の枠が本頁で閉じることを、『次頁へ続く: あり』は"
    "閉じないことを意味する。画像から読み取った内容でこれと矛盾する、またはこれを超える"
    "前後頁への続きの推測 (「続きの可能性あり」等) をしない。\n"
)

# DM2 研读包 (study dossier)。挂上研读包时才加的一段 system 规则。
# ⛔ 常時足してはいけない (_PDF_SOURCE_RULE と同じ教訓): 研読パッケージが付いていない
# 回答で「part B は網羅的」と書いてあると、モデルは検索で来なかっただけの不在を
# 「存在しない」と言い切れてしまう —— 付いた時だけが真。
_DOSSIER_RULES = (
    "\n\n## Study dossier rules\n"
    "- The context ends with 【本研究 研読パッケージ】: this study's protocol (PRT) chapters "
    "verbatim (part A) and the COMPLETE list of EDC items (part B). Study-side retrieval was "
    "skipped on purpose: part B is exhaustive, so if an item is not there, it does not exist.\n"
    # (1) 曾无条件写"从【標準 CDISC】数"—— 但 federation 关 / CDISC 侧零命中时那个块根本
    # 不存在, 规则却仍在命令模型去那里数 ⇒ 模型只能编一个块出来。块在不在是可观测的,
    # 让它自己说"块不在"比让它假装块在要诚实得多。
    # T9 attempt 1 (4/6, evidence/failures/dm2_task9_attempt_1.md) 的失败是**类别轴混淆**:
    # (1) 只说"枚举标准定义的记录类别", 没说沿哪条轴 ⇒ 模型拿 `--SCAT` 子类别 / 阶段轴切一刀
    # 凑够条数, 真正漏掉的那个 `--CAT` 值既没列也没申报无候选。旧 (5)「说清哪类没候选」挂在
    # (1) 的产物上 —— (1) 漏了 (5) 就一起哑, 所以把它并进 (2): 每个类别值各起一个小标题,
    # "漏"于是变成看得见的空标题。修法停在**模式级** (说"沿 --CAT 轴", 不说某域有几类):
    # 凡分类轴不止一条 (--CAT / --SCAT / epoch) 的域都会复发, 写死题面只会修绿一道题。
    # (4) 同样收紧: attempt 1 有一跑只在开头做一次全局声明, 段内不复标 —— 下游一摘表就丢。
    # T9 attempt 3 (Claude 两模型, evidence/failures/dm2_task9_attempt_3.md) 的四个失败模式,
    # 修法仍停在模式级 (不写域名 / CT 取值 / 表单 / OID):
    # ① 无 CT 的类别轴被静默跳过 —— 旧 (1) 只讲了「--CAT 有 CT」一种形态, 模型遇到无 CT /
    #    无 --CAT 的域就直接按表单分组, 不声明也不点名替代轴 ⇒ 改为开篇一句「属于哪种形态」必答;
    # ② CT 值被意译或以 codelist 名顶替 ⇒ 写死「逐字大写 CT 串」;
    # ③ 排除清单 / 表格列里出现一览中没有的 OID (含自造的表单 OID 前缀) ⇒ 作用域扩到全文;
    # ④ 研读包以日文为主, 答题语言被带偏 (zh/en 问 → ja 答), rag.py 的通用语言规则压不住 ⇒ 这里再说一次.
    "- Domain-level mapping questions: answer in the language of the question — the dossier "
    "being mostly Japanese does not change that. Steps, in order: (1) category axis — before "
    "looking at any EDC item, open with ONE sentence stating which case holds for the target "
    "domain, then follow it: (a) its `--CAT` variable has controlled terminology (take it from "
    "【標準 CDISC】 when that block is present; if it is absent, say so and use the standard as "
    "you know it, marked (推測)): list EVERY CT value as its own heading, in the standard's "
    "order, writing each value as the exact uppercase CT string — do not translate, abbreviate "
    "or replace it with the codelist name; (b) `--CAT` exists without controlled terminology, "
    "or (c) the domain has no `--CAT` variable: say which, name the grouping axis you use "
    "instead (derived from the domain definition), then one heading per group. Never substitute "
    "sub-category (`--SCAT`), epoch or timing axes for the category axis; "
    "(2) under each heading either list the candidate items found by scanning part B form by "
    "form, quoting each as `[form OID] item (OID)` exactly as written, or write explicitly "
    "「候補なし / no candidate item in the EDC」 — no heading may be silently skipped; "
    "(3) EVERY EDC OID anywhere in the answer — candidate, excluded or reference lists, "
    "table columns — must be copied character for character from part B, with the form OID of "
    "the form it is listed under there; never construct, prefix or complete an OID — if unsure, "
    "describe the item in words without an OID. Give each item one assignment only: never list "
    "the same item both as a candidate and as excluded; (4) name as target-domain variables only "
    "variables the standard defines for that domain; anything else is a SUPPQUAL QNAM proposal "
    "and must be labelled so; (5) when part A defines or governs what the domain records, cite "
    "the section number; (6) every EDC→SDTM assignment is inference — mark it with (推測) in the "
    "heading or first line of each group that lists candidates AND inline on every individual "
    "assignment, not only in a global disclaimer.\n"
)


def _attach_dossier_rules(messages: list[dict], question: str) -> None:
    """研读包挂上时: system 追加规则句, 最后一条 user 消息追加确定的答题语言行。
    /api/ask 与 /api/ask_stream 共用 (两处各写一份 = 只修好一边)。"""
    from server.dossier_trigger import ANSWER_LANGUAGE_LINE, answer_language
    messages[0]["content"] += _DOSSIER_RULES
    line = "\n\n" + ANSWER_LANGUAGE_LINE[answer_language(question)]
    last = messages[-1]
    if isinstance(last["content"], list):  # PDF 通道的多模态 parts: 接到首个 text part 上
        text_part = next(p for p in last["content"] if p.get("type") == "text")
        text_part["text"] += line
    else:
        last["content"] += line


# ── Request / Response models ────────────────────────────────────────────

class MessageItem(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(max_length=50000)


class AskRequest(BaseModel):
    # extra="forbid": 未知字段必须 422, 不能静默丢弃。抽检脚本 v1 就是往 /api/ask 传了
    # `web: true` —— pydantic 默默扔掉, 端点照常返回 200, 于是产出一整张"全 ✅ 却什么
    # 都没测到"的抽检表 (evidence/failures/web_channel_spotcheck_attempt_1_*)。
    model_config = ConfigDict(extra="forbid")

    question: str = Field(max_length=10000)
    domain: str | None = None
    file_type: str | None = None
    model: str = "default"
    history: list[MessageItem] = Field(default_factory=list)
    top_k: int | None = Field(None, ge=1, le=100)
    # Plan B 联邦: auto = LLM 判库; 显式值绕过路由 (federation 关时该字段无作用)
    corpus: Literal["auto", "cdisc", "study", "both"] = "auto"
    # DM2 研读包: auto = 域码+范围词自动判; on/off = 手动强开/强关 (总闸 OFF 时 on 也不挂).
    dossier: Literal["auto", "on", "off"] = "auto"


class SourceItem(BaseModel):
    chunk_id: str
    source: str
    domain: str | None
    file_type: str | None
    section: str | None
    similarity: float
    text_preview: str
    corpus: str | None = None  # 联邦路径下 "cdisc"|"study"; 单库路径 None


class AskResponse(BaseModel):
    answer: str
    sources: list[SourceItem]
    model_used: str
    usage: dict | None = None
    routed_corpus: str | None = None  # 实际检索的库; federation 关时 None
    # 输出触顶自动续写 (2026-09-08)。与 ask_stream 的 done 事件同名同义。默认值是
    # "没发生过", 所以老调用方 (eval 脚本按字段名取值) 一行不改也照常工作; 但
    # truncated=True 时它们至少**能**发现答案不完整, 而不是把半句话当完整答案打分。
    continue_rounds: int = 0
    truncated: bool = False
    # 续写轮抛异常时的异常类名 (None = 没发生)。⛔ 不并进 `truncated`: "写到上限了"与
    # "续写的时候炸了"是两件事, 调用方对后者该有别的反应 (重试往往能成)。
    continue_error: str | None = None
    # C2R 画面 PDF 旁路 (I2-3)。ask_stream の done 事件と同名同義。None = 通道が動いて
    # いない (OFF か不発火); リストなら実際に添付した頁。既定 None なので既存の呼び出し
    # 側は一行も変わらない。
    pdf_trigger: str | None = None
    pdf_pages: list[dict] | None = None
    # DM2 研读包. None = 通道没跑 (总闸 OFF); dict = 跑了 (attached 说挂没挂, reason 说为何).
    dossier: dict | None = None


class InfoResponse(BaseModel):
    collection_name: str
    chunk_count: int
    default_model: str
    fallback_model: str
    top_k: int
    structured_lookup: bool
    hybrid: bool
    hybrid_fusion: str | None = None
    prompt_guardrail: bool
    web_search: bool = False  # Rule 9 是否在线 (回滚开关的唯一可观测出口)
    # Phase 2 compare/judge defaults (UI prefills its model slots from these).
    compare_models: list[str] = Field(default_factory=list)
    judge_model: str | None = None
    # 用户可选答题模型 (spec §7)。前端下拉直接渲染这张表 —— 与 Router 组同源, 见 §3.1。
    selectable_models: list[SelectableModel] = Field(default_factory=list)
    # 索引新鲜度 (运维闸): 默认 None 而非 True —— 判不出来时说"新鲜"比没有该字段更糟
    index_fresh: bool | None = None
    index_freshness_reason: str | None = None
    federation: bool = False  # Plan B: 双库联邦是否已构建


# ── Endpoints ────────────────────────────────────────────────────────────

@api_router.get("/health")
def health():
    return {"status": "ok"}


@api_router.get("/info", response_model=InfoResponse)
def info(request: Request):
    rag = request.app.state.rag
    s = request.app.state.settings
    return InfoResponse(
        collection_name=s.collection_name,
        chunk_count=rag.collection.count(),
        default_model=s.default_model,
        fallback_model=s.fallback_model,
        top_k=s.top_k,
        structured_lookup=rag.structured_lookup_enabled,
        hybrid=rag.hybrid_enabled,
        hybrid_fusion=rag.hybrid_fusion if rag.hybrid_enabled else None,
        prompt_guardrail=rag.prompt_guardrail_enabled,
        web_search=rag.web_search_enabled,
        compare_models=s.compare_models,
        judge_model=s.judge_model,
        selectable_models=s.selectable_models,
        # 启动时算好存在 app.state, 避免每次 /info 都重扫 KB 目录
        index_fresh=getattr(request.app.state, "index_fresh", None),
        index_freshness_reason=getattr(request.app.state, "index_freshness_reason", None),
        federation=getattr(request.app.state, "federation", None) is not None,
    )


def maybe_attach_pdf_pages(request: Request, question: str, chunks, messages):
    """命中カードの形が P1 §3 の規則に当たれば、画面ページ画像を user メッセージに足す。

    戻り値 `(pdf_pages, rule)` は観測用 (done 事件 / AskResponse)。付けなかったときは
    `(None, None)` —— 空リストではなく None なのは「通道が動いて 0 枚」と「そもそも
    動いていない」を客側で区別できるようにするため。

    ⚠ 開関 OFF (既定) では `app.state.pdf_context` が None ⇒ `messages` に一切触れない。
    「OFF なら本機能導入前と逐位同一」はこの 1 行の早期 return が担保している。
    /api/ask と /api/ask_stream の**両方**から呼ぶ (2 箇所に書くと片方だけ直る)。
    """
    builder = getattr(request.app.state, "pdf_context", None)
    if builder is None:
        return None, None
    from server.pdf_trigger import parse_chunks, should_attach_pdf

    # CDISC chunk / 手順書章節は CardFacts.from_text が None を返して落ちる (front matter の
    # doc_type で判別) ので、ここで corpus を見て絞る必要は無い。
    cards = parse_chunks(chunks)
    # R3 の関連性フロア (M10)。壊れても本リクエストは通す —— フロアの供給元が落ちる代償は
    # 「R3 が発火しない」であるべきで、/api/ask が 500 になることではない。
    lookup = getattr(request.app.state, "study_lookup", None)
    strong = form_named = False
    if lookup is not None:
        try:
            strong = bool(lookup.strong_hit(question))
            # (c-1) 別名表経由 (通道 ③)。⚠ 検索側 (`_apply_study_lookup`) も同じ
            # `resolve` を呼ぶが、結果はどこにも残らず rag.py は凍結中なのでここで
            # 2 度目を呼ぶ。実測 0.01-0.03 ms/回 (in-memory の文字列照合のみ、LLM も
            # 埋め込みも無い) —— 1 リクエストの数十秒に対して無視できる。
            form_named = bool(lookup.resolve(question).form_scopes)
        except Exception:  # noqa: BLE001
            log.warning("pdf_trigger_study_floor_failed", exc_info=True)
    # (c-2) 頁索引の名前表経由 (r3b)。別名表は実データで 1 件しか無く、それだけを
    # フロアにすると「フォームを名指しした純粋な画面レイアウト問い」が落ちる (V3
    # attempt 1 の T6)。別名表を増やす手もあるが、あちらは検索の注入に効くので
    # golden の再走が要る —— こちらは触発判定だけを見て検索を 1 件も動かさない。
    form_named = form_named or builder.index.form_named_in(question) is not None
    decision = should_attach_pdf(question, cards, study_strong_hit=strong,
                                 study_form_named=form_named)
    if not decision.fire:
        return None, None
    selection = builder.select_pages(cards, question)
    images = builder.render(selection)
    parts = builder.to_message_parts(selection, images)
    if not parts:
        # 描画が全部失敗した (pdftoppm 不在など)。builder 側が warning を 1 度出している。
        # ⛔ None に丸めない: 「規則に当たらなかった」と区別が付かなくなり、
        # 「なぜ画面が付かないのか」を後から切り分けられない (M4)。
        log.warning("pdf_context_no_pages_rendered", rule=decision.rule,
                    selected=len(selection.pages))
        return [], decision.rule
    last = messages[-1]
    last["content"] = [{"type": "text", "text": last["content"]}, *parts]
    messages[0]["content"] += _PDF_SOURCE_RULE
    log.info("pdf_context_attached", rule=decision.rule, pages=len(images),
             selected=len(selection.pages), folded=len(selection.folded),
             truncated=selection.truncated, reason=decision.reason)
    # 報告するのは**実際に付いた**頁 (M3): 答えの中の 画面目視判読 p.NN がどの頁から
    # 来たのかを後から辿れる唯一の記録がこれ。
    return [{"pdf": i.pdf, "page": i.page} for i in images], decision.rule


def maybe_attach_dossier(request: Request, question: str, chunks, routed: str | None, mode: str,
                         *, domain: str | None = None, file_type: str | None = None,
                         top_k: int | None = None):
    """DM2: 域级映射题触发时, 丢 study 侧 chunks, 返回研读包文本块供拼进 context.

    → (chunks, routed, dossier_block | None, dossier_info | None).
    通道 OFF (`app.state.dossier is None`) → 原样返回, info=None: 由这一行早期 return 担保
    messages 数组与 sources 列表与引入前逐字节同; 响应信封多一个 `dossier: null` 键 (有意三态:
    null=通道 OFF / attached=false 带 reason=跑了没挂 / attached=true=挂了, 与 pdf 通道
    None/[] 的区分同一教训). /api/ask 与 /api/ask_stream 都调这一个函数.

    `domain` / `file_type` / `top_k` 是**请求原样**的检索参数: 挂上研读包时本函数可能替
    federation 重跑一次 CDISC 侧检索, 那一次必须和 federation 自己走 `both` 时收到的参数
    完全一样 —— 否则"挂了研读包"会静默吃掉用户给的过滤条件。
    """
    dossier = getattr(request.app.state, "dossier", None)
    if dossier is None:
        return chunks, routed, None, None
    from server.dossier_trigger import decide_dossier

    lookup = getattr(getattr(request.app.state, "rag", None), "_structured_lookup", None)
    query_domains = lookup._query_domains if lookup is not None else (lambda q: [])
    s = request.app.state.settings
    decision = decide_dossier(question, mode, s.dossier_enabled, query_domains,
                              auto_attach=s.dossier_auto_attach)
    info = {"attached": decision.attach, "reason": decision.reason,
            "domains": list(decision.domains), "sha": dossier.sha,
            "sections": list(dossier.sections), "chars": dossier.chars}
    if not decision.attach:
        return chunks, routed, None, info
    fed = getattr(request.app.state, "federation", None)
    if fed is not None and routed == "study":
        # study 单库路由下没有 CDISC 定义段 (D2), 补取 CDISC 侧。席位口径与 federation 走
        # `both` 时**同一条式子** (`FederatedEngine.retrieve`: k = top_k or self.top_k,
        # 每边 ceil(k/2)), 过滤条件也原样透传 —— 这里少传一个参数, 用户就会拿到一份
        # 悄悄忽略了 domain/file_type/top_k 的结果, 而 API 上完全看不出来。
        k = top_k or fed.top_k
        k_each = math.ceil(k / 2)
        try:
            cd = fed.cdisc.retrieve(question, domain=domain, file_type=file_type, top_k=k_each)
        except Exception as e:
            # 检索炸了要报 502 (与两个端点开头那次检索同口径), 不能穿透成 500 ——
            # "上游检索暂时不可用"是调用方能重试的, 500 只会被当成本服务的 bug。
            log.error("dossier_cdisc_refetch_failed", error=str(e), exc_info=True)
            raise HTTPException(status_code=502,
                                detail="Retrieval service temporarily unavailable.") from e
        for c in cd:
            c.corpus = "cdisc"
        chunks = list(cd)
    else:
        chunks = [c for c in chunks if getattr(c, "corpus", None) != "study"]
    if fed is not None:
        routed = "both"
    log.info("dossier_attached", reason=decision.reason, domains=list(decision.domains),
             sha=dossier.sha, chars=dossier.chars, kept_chunks=len(chunks))
    return chunks, routed, dossier.text, info


@api_router.post("/ask", response_model=AskResponse)
def ask(body: AskRequest, request: Request):
    rag = request.app.state.rag
    llm_router = request.app.state.llm_router
    s = request.app.state.settings
    t0 = time.perf_counter()

    if not body.question.strip():
        raise HTTPException(status_code=422, detail="question must not be empty")

    # 与 /api/ask_stream 共用 known_model_groups —— 曾经这里是一份写死的
    # {"default","hard","light"}, 于是 /api/info 广播出去的 id 打到本端点就 422,
    # 同一个仓库两个端点对同一个模型名给出相反答案 (它连 default-fallback 都漏了)。
    # 白名单只能有一份, 且必须是 Router 事实的那份。
    known = known_model_groups(s)
    if body.model not in known:
        raise HTTPException(status_code=422,
                            detail=f"unknown model {body.model!r}; known: {sorted(known)}")

    log.info("ask", question=body.question[:100], model=body.model, domain=body.domain)

    fed = getattr(request.app.state, "federation", None)
    routed: str | None = None
    try:
        if fed is not None:
            chunks, routed = fed.retrieve(
                body.question, corpus=body.corpus, top_k=body.top_k,
                domain=body.domain, file_type=body.file_type,
            )
        else:
            chunks = rag.retrieve(
                body.question,
                domain=body.domain,
                file_type=body.file_type,
                top_k=body.top_k,
            )
    except Exception as e:
        log.error("retrieve_failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.") from e

    # 画面 PDF 通道看的是**过滤前**的 chunks (spec §5: 两条通道并存且互不知情)。研读包丢掉
    # study 侧 card 是为了不让它们再进 context, 不是说这些 card 对"该不该附画面"的判断也不
    # 存在了 —— 把过滤后的传进去, PDF 通道会因为"一张卡都没有"而静默不发火 (should_attach_pdf
    # 的第一条就是 `if not cards: 不发`), 于是两条通道变成事实上的互斥。
    chunks_for_pdf = chunks
    # ⚠ 研读包判定必须排在 answerer 之前: 它可能把 routed 从 "study" 抬成 "both", 而下面那句
    # `if routed == "study": answerer = None` 要看的是**抬过之后**的值。_DOSSIER_RULES 第 ①
    # 步要模型先从标准枚举记录类别, 那条确定性事实通道不能被一个已经不成立的判断掐掉。
    chunks, routed, dossier_block, dossier_info = maybe_attach_dossier(
        request, body.question, chunks, routed, body.dossier,
        domain=body.domain, file_type=body.file_type, top_k=body.top_k)

    answerer = getattr(request.app.state, "answerer", None)
    if routed == "study":
        answerer = None  # CDISC 专用事实通道, study 单库路由下必须静默跳过
    try:
        facts = answerer.resolve(body.question) if answerer else None
    except Exception:
        log.warning("structured_answer_resolve_failed", exc_info=True)
        facts = None

    engine = fed if fed is not None else rag
    context = engine.format_context(chunks)
    if fed is not None and not context:
        context = _NO_CONTEXT
    if dossier_block:
        context = (dossier_block if (not context or context == _NO_CONTEXT)
                   else context + "\n\n" + dossier_block)
    if facts is not None:
        from server.structured_answer import augment_context
        context = augment_context(facts, context)

    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    if fed is not None:
        messages = fed.build_messages(body.question, context, history_dicts or None,
                                      corpus=routed or body.corpus)
    else:
        messages = rag.build_messages(body.question, context, history_dicts or None)
    if dossier_block:
        _attach_dossier_rules(messages, body.question)
    pdf_pages, pdf_trigger = maybe_attach_pdf_pages(request, body.question, chunks_for_pdf, messages)

    # 输出触顶自动续写 (2026-09-08)。⚠ 这里是**第二份**实现: /api/ask 走同步
    # `llm_router.completion`, 与 ask_stream 的 `acompletion` 不共用任何辅助函数。
    # ⛔ 两处的常量必须是同一个 (`CONTINUE_PROMPT` / `_TRUNCATED_FINISH_REASONS`),
    # 不许各抄一份。
    #
    # ⚠ 受益方是 **Chat UI 之外的 HTTP 调用方** —— 今天就是 `ui/streamlit_app.py`。
    # ⛔ **不是 eval**: `eval/run_eval.py` 自己 `rag.build_messages()` 后直接调
    # `router.completion(model="default", max_tokens=8192)`, **从不碰本端点**, 也因此
    # 既不吃 deployment 天花板也不吃自动续写 —— 那个 8192 是 V-2 跨模型可比性要求的
    # **有意**取值, 它自己那条 `find_truncated` 会把撞顶的题报出来。别去"修"它。
    msgs = list(messages)
    answer_parts: list[str] = []
    continue_rounds = 0
    truncated = False
    continue_error: str | None = None
    usage_total = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    usage_seen = False
    usage_missing = False
    try:
        while True:
            try:
                response = llm_router.completion(model=body.model, messages=msgs)
            except Exception as e:  # noqa: BLE001 — 只吞**续写轮**的失败, 见下
                if continue_rounds == 0:
                    raise      # 第 1 轮就失败 ⇒ 什么内容都没有, 维持老行为 502
                # 续写轮失败: 已经拿到的正文**不能丢**。引入续写之前, 一次成功但被截断的
                # 调用返回的是 200 + 半截答案; 若这里让异常穿透, 同一种情况会退化成 502
                # 什么都没有 ——「本来能拿到半篇」变成「什么都拿不到」。
                # 代价必须是**明的**: truncated + continue_error 让调用方看得见这不是
                # 一篇正常写完的答案。
                log.warning("continue_round_failed", round=continue_rounds,
                            model=body.model, error=str(e), exc_info=True)
                truncated = True
                continue_error = type(e).__name__
                break
            round_text = response.choices[0].message.content or ""
            answer_parts.append(round_text)
            if response.usage:
                # 每轮独立计费 —— 只报最后一轮会系统性低报成本 (同 ask_stream)
                usage_seen = True
                usage_total["prompt_tokens"] += response.usage.prompt_tokens or 0
                usage_total["completion_tokens"] += response.usage.completion_tokens or 0
                usage_total["total_tokens"] += response.usage.total_tokens or 0
            else:
                usage_missing = True   # 与流式同口径: 缺了一轮就不许呈现成完整总量
            if getattr(response.choices[0], "finish_reason", None) not in _TRUNCATED_FINISH_REASONS:
                break
            if continue_rounds >= s.max_continue_rounds:
                truncated = True
                break
            # 墙钟预算: `Router(timeout=...)` 是**每次调用**的上限, 管不住整次请求。
            # 最坏 (1 + max_continue_rounds) 轮 ⇒ 单个 HTTP 请求可占用十几分钟, 而
            # `ui/streamlit_app.py` 只等 120 秒 —— 用户早已拿到 ReadTimeout, 服务端还在
            # 为一条没人接的请求烧钱。剩余不足下一轮的最小值就收手, 如实报 truncated。
            # ⚠ 流式路**不需要**这个: token 一直在流, 客户端不会判超时, 加了反而会截断
            # 一个正在健康推进的长答案。
            if s.request_timeout_s - (time.perf_counter() - t0) < _CONTINUE_MIN_REMAINING_S:
                log.warning("continue_budget_exhausted", round=continue_rounds,
                            elapsed_s=round(time.perf_counter() - t0, 1))
                truncated = True
                break
            continue_rounds += 1
            # 空轮不加锚, 原样重开一轮 —— 理由与实测见 ask_stream 里同一处的注释。
            if round_text:
                msgs.append({"role": "assistant", "content": round_text})
                msgs.append({"role": "user", "content": CONTINUE_PROMPT})
    except Exception as e:
        log.error("llm_failed", error=str(e), model=body.model, exc_info=True)
        raise HTTPException(status_code=502, detail="LLM service temporarily unavailable.") from e

    # 计数闸看的是**拼接后的全文** —— 分轮跑会把跨接缝的那句话判漏。
    answer = "".join(answer_parts)
    if facts is not None:
        from server.grounding import apply_counting_gate
        answer, violations = apply_counting_gate(answer, facts)
        if violations:
            log.warning("structured_count_violation", violations=violations)
    model_used = getattr(response, "model", None) or body.model
    usage = None
    if usage_seen:
        usage = dict(usage_total)
        if usage_missing:
            usage["partial"] = True

    sources = [
        SourceItem(
            chunk_id=c.chunk_id,
            source=c.source,
            domain=c.domain,
            file_type=c.file_type,
            section=c.section,
            similarity=c.similarity,
            text_preview=c.text[:300],
            corpus=getattr(c, "corpus", None) or None,
        )
        for c in chunks
    ]

    elapsed = time.perf_counter() - t0
    log.info(
        "ask_done",
        chunks=len(chunks),
        model_used=model_used,
        tokens=usage.get("total_tokens") if usage else None,
        elapsed_s=round(elapsed, 2),
    )

    return AskResponse(
        answer=answer,
        sources=sources,
        model_used=model_used,
        usage=usage,
        routed_corpus=routed,
        continue_rounds=continue_rounds,
        truncated=truncated,
        continue_error=continue_error,
        pdf_trigger=pdf_trigger,
        pdf_pages=pdf_pages,
        dossier=dossier_info,
    )


# ── Streaming single-model Q&A (chat UI; DESIGN_chat_ui.md §3) ─────────


class AskStreamRequest(BaseModel):
    question: str = Field(max_length=10000)
    history: list[MessageItem] = Field(default_factory=list)
    top_k: int | None = Field(None, ge=1, le=100)
    domain: str | None = None
    file_type: str | None = None
    corpus: Literal["auto", "cdisc", "study", "both"] = "auto"
    web: bool = False  # 联网参考通道; 与 corpus 判库正交 (spec §4)
    # 答题模型组名。与 AskRequest.model 同名同默认值。校验在 ask_stream 里做 ——
    # 合法值集合来自 Router (与 /api/info 同源), pydantic 层拿不到它。
    model: str = "default"
    # DM2 研读包: auto = 域码+范围词自动判; on/off = 手动强开/强关 (总闸 OFF 时 on 也不挂).
    dossier: Literal["auto", "on", "off"] = "auto"


@api_router.post("/ask_stream")
async def ask_stream(body: AskStreamRequest, request: Request):
    """SSE 流式单模型问答 (DeepSeek V4 Pro via Router 'default'). 检索一次 (FR1),
    然后流式生成。检索失败在开流前返 502; 流中途失败发 error 事件。"""
    rag = request.app.state.rag
    llm_router = request.app.state.llm_router
    s = request.app.state.settings

    if not body.question.strip():
        raise HTTPException(status_code=422, detail="question must not be empty")

    known = known_model_groups(s)
    if body.model not in known:
        # ⛔ 不静默退回 default: 静默退回会让"选了模型 X 却拿到 Y 的答案"完全不可见。
        raise HTTPException(status_code=422,
                            detail=f"unknown model {body.model!r}; known: {sorted(known)}")

    verified_by_id = {m.id: m.verified for m in s.selectable_models}
    # default/hard/light 不在表里 ⇒ None = "未知", 不是 False。发 False 会把"没这个概念"
    # 误报成"验过且不通过" (spec §6)。
    model_verified = verified_by_id.get(body.model)

    fed = getattr(request.app.state, "federation", None)
    routed: str | None = None
    try:
        if fed is not None:
            chunks, routed = fed.retrieve(
                body.question, corpus=body.corpus, top_k=body.top_k,
                domain=body.domain, file_type=body.file_type,
            )
        else:
            chunks = rag.retrieve(
                body.question, domain=body.domain, file_type=body.file_type, top_k=body.top_k
            )
    except Exception as e:
        log.error("stream_retrieve_failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.") from e

    # 画面 PDF 通道看的是**过滤前**的 chunks (spec §5: 两条通道并存且互不知情)。研读包丢掉
    # study 侧 card 是为了不让它们再进 context, 不是说这些 card 对"该不该附画面"的判断也不
    # 存在了 —— 把过滤后的传进去, PDF 通道会因为"一张卡都没有"而静默不发火 (should_attach_pdf
    # 的第一条就是 `if not cards: 不发`), 于是两条通道变成事实上的互斥。
    chunks_for_pdf = chunks
    # ⚠ 研读包判定必须排在 answerer 之前: 它可能把 routed 从 "study" 抬成 "both", 而下面那句
    # `if routed == "study": answerer = None` 要看的是**抬过之后**的值。_DOSSIER_RULES 第 ①
    # 步要模型先从标准枚举记录类别, 那条确定性事实通道不能被一个已经不成立的判断掐掉。
    chunks, routed, dossier_block, dossier_info = maybe_attach_dossier(
        request, body.question, chunks, routed, body.dossier,
        domain=body.domain, file_type=body.file_type, top_k=body.top_k)

    answerer = getattr(request.app.state, "answerer", None)
    if routed == "study":
        answerer = None  # CDISC 专用事实通道, study 单库路由下必须静默跳过
    try:
        facts = answerer.resolve(body.question) if answerer else None
    except Exception:
        log.warning("structured_answer_resolve_failed", exc_info=True)
        facts = None

    engine = fed if fed is not None else rag
    context = engine.format_context(chunks)
    if fed is not None and not context:
        context = _NO_CONTEXT
    if dossier_block:
        context = (dossier_block if (not context or context == _NO_CONTEXT)
                   else context + "\n\n" + dossier_block)
    if facts is not None:
        from server.structured_answer import augment_context
        context = augment_context(facts, context)

    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    if fed is not None:
        messages = fed.build_messages(body.question, context, history_dicts or None,
                                      corpus=routed or body.corpus)
    else:
        messages = rag.build_messages(body.question, context, history_dicts or None)
    if dossier_block:
        _attach_dossier_rules(messages, body.question)
    pdf_pages, pdf_trigger = maybe_attach_pdf_pages(request, body.question, chunks_for_pdf, messages)
    sources = [
        {"chunk_id": c.chunk_id, "source": c.source, "domain": c.domain,
         "file_type": c.file_type, "section": c.section,
         "similarity": c.similarity, "text_preview": c.text[:300],
         "corpus": getattr(c, "corpus", None) or None}
        for c in chunks
    ]

    # DM1 D6: 问句落盘 (前 100 字 + 判库 + chunk id), 不记答案. 没有这一行, dogfood ⚑ 的
    # 第一轮原句就永久丢失, 只能用重构句复现 (evidence/checkpoints/dogfood_ds_domain_2026-09-15.md).
    log.info(
        "ask_stream", question=body.question[:100], corpus=routed,
        n_chunks=len(chunks), chunk_ids=[c.chunk_id for c in chunks],
        dossier=(dossier_info or {}).get("reason"),
    )

    def sse(event: str, data: dict) -> str:
        return f"event: {event}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"

    use_web = bool(body.web) and s.web_search_enabled
    tools = [WEB_TOOL_SPEC] if use_web else None
    searcher = WebSearcher(s) if use_web else None

    async def _open_stream(msgs, with_tools: bool):
        """include_usage 让 done 能报 token; 个别 provider 不收该 kwarg, 失败则退化重开一次
        (保住答案, usage 报 null 而非编造)。开流失败才重试 —— 迭代中途失败不重试 (会重复生成),
        由下面的 except 兜。工具参数只在 with_tools 时传 —— web 关闭时请求体与本功能引入前
        逐位相同。"""
        kw = {"model": body.model, "messages": msgs, "stream": True}
        if with_tools and tools:
            kw["tools"] = tools
        try:
            return await llm_router.acompletion(**kw, stream_options={"include_usage": True})
        except Exception:  # noqa: BLE001 — 窄重试: 去掉 stream_options, 保住答案
            log.warning("stream_options_unsupported_retry_without", exc_info=True)
            return await llm_router.acompletion(**kw)

    async def gen():
        yield sse("sources", {"sources": sources, "routed_corpus": routed,
                              "dossier": dossier_info})
        model_used = None   # 流里一个 chunk 都没报模型时就一直是 None —— done 事件如实发 null,
                            # ⛔ 不许兜成 "default": 那是**编**一个模型名, 而这个值会进历史存档
        # 逐 chunk 收全**出现过的**模型, 有序去重 (spec R6)。与 model_used 各记一件事:
        # model_used = 最后一个 (最后那段文字是谁写的), models_used = 全部 (整次问答里
        # 有没有别人插过手)。⚠ 只看最后一个会漏掉"某一轮回退、末轮落回主模型"这种情况,
        # 那正是"回退了却不说"。
        models_used: list[str] = []
        parts: list[str] = []   # 跨轮全文, 只给 counting gate 用
        # 每轮都是一次独立计费的 API 调用 —— usage 必须跨轮累加, 只报最后一轮会系统性低报
        # 成本。某轮走了 stream_options 窄重试就拿不到 usage; 那种情况打 partial 标记:
        # 部分数据比没有有用, 但不能把"缺了一轮"呈现成一个看起来完整的总量。
        usage_total = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
        usage_seen = False
        usage_missing = False
        # 触顶自动续写 (2026-09-08): 本次回答一共为"接着写"多开了几次 API 调用, 以及
        # 收尾时是不是**仍然**卡在上限上。两个都进 done —— 一条被截断的答案与一条完整
        # 答案在存档里必须长得不一样 (与 web_status / fell_back 同一条教训)。
        continue_rounds = 0
        truncated = False
        web_ok = 0
        web_fail: str | None = None   # 最严重的一次联网失败 (见 _WEB_FAIL_RANK)
        if not body.web:
            web_status = "off"
        elif not s.web_search_enabled:
            # 用户勾了联网、服务端关着 —— 报 off 会让界面一声不吭, 那正是最骗人的失败模式。
            web_status = "disabled"
        else:
            web_status = "ok"
        msgs = list(messages)

        try:
            # web 开启时多跑一轮: 前 max_rounds 轮带工具, 最后一轮**不带**工具 ——
            # 触顶后模型必须用手上的东西作答, 不能再要搜索, 也不会被硬切断在半句话上。
            total_rounds = (s.web_max_rounds + 1) if use_web else 1
            for rnd in range(1, total_rounds + 1):
                with_tools = use_web and rnd <= s.web_max_rounds
                # 输出触顶自动续写的内层循环 (2026-09-08)。它**不消耗**外层的工具轮预算:
                # 续写不是一次新的工具决策, 只是把同一段回答接着写完。故它嵌在 rnd 里面,
                # 而不是把 total_rounds 加大 —— 后者会让"续写"偷偷买到额外的搜索机会。
                while True:
                    # 开流的外层上限 (REV MED-b): provider 连接挂死时以 error 事件收场, 不把
                    # SSE 连接晾着。流中途**不**包 wait_for —— 单一 deadline 会截断健康的长答案。
                    resp = await asyncio.wait_for(
                        _open_stream(msgs, with_tools), timeout=s.request_timeout_s)

                    acc: dict[int, dict] = {}   # 流式 tool_calls 是增量的, 按 index 拼
                    round_parts: list[str] = []  # 本轮文本, 回灌 assistant 消息用
                    cu_round = None
                    # 本次调用的收尾理由: 取**最后一个非 None** 的。分片流里绝大多数 chunk
                    # 的 finish_reason 是 None, 只有收尾那片带值; 裸赋值会被**收尾片之后
                    # 还带 choices 的尾片**抹回 None ⇒ 触顶永远测不出来。
                    # ⚠ 初版这里写的理由是"会被 usage 片抹回 None", **那是错的** ——
                    # 读取点在下面的 `if choices:` 里面, 而 usage 片的 choices 是空列表,
                    # 根本进不来 (2026-09-08 复审 M-1 指出)。守卫要防的是尾片, 不是 usage 片。
                    finish_reason = None
                    async for chunk in resp:
                        choices = getattr(chunk, "choices", None)
                        if choices:
                            ch = choices[0]
                            # **工具**循环是否继续只看 acc 是否攒到工具调用, 不看 finish_reason
                            # —— 各 provider 的收尾理由字段并不统一, acc 是唯一可靠的信号。
                            # (2026-09-08 起 finish_reason 也读了, 但只用来判"是不是被输出
                            # 上限截断", 与工具判定各管各的, 见内层 while 末尾。)
                            fr = getattr(ch, "finish_reason", None)
                            if fr:
                                finish_reason = fr
                            # 只取 content / tool_calls, 其余 delta 字段有意丢弃 ——
                            # 含 GPT-5.6 Sol 的 reasoning_content (模型内部思考, 不该进
                            # 知识库答案, 更不该被当成引用来源)。spec §4.3。
                            # 实测边界: 流式下两个 GPT 均未发该增量, 只有非流式 boto3 调用
                            # 时 Sol 发了 reasoningContent 块 ⇒ 这是预防, 不是现实问题。
                            text = getattr(ch.delta, "content", None)
                            if text:
                                parts.append(text)
                                round_parts.append(text)
                                yield sse("token", {"text": text})
                            for tc in (getattr(ch.delta, "tool_calls", None) or []):
                                # index / id 一律 getattr 兜底: 缺字段的 delta 若让
                                # AttributeError 穿透, 用户拿到的是 "LLM stream failed",
                                # 整个答案丢光 —— 这比少拼一个分片严重得多。
                                slot = acc.setdefault(getattr(tc, "index", 0),
                                                      {"id": None, "name": "", "args": ""})
                                tc_id = getattr(tc, "id", None)
                                if tc_id and not slot["id"]:
                                    slot["id"] = tc_id          # 取首个非空
                                fn = getattr(tc, "function", None)
                                if fn and getattr(fn, "name", None) and not slot["name"]:
                                    slot["name"] = fn.name      # 取首个非空: 有 provider 每片都重发
                                if fn and getattr(fn, "arguments", None):
                                    slot["args"] += fn.arguments  # 只有 arguments 是真分片
                        # 两半各防一件事, 缺任一半 model_used 都会丢成 None (⇒ 回退发生了也报不出来):
                        # · 搁在 `if choices:` **外面**: usage chunk 的 choices 是空列表, 而有
                        #   provider 只在那一片上报模型 —— 搁在里面就整条流都取不到。
                        # · `reported` 为假时**不赋值**: 报模型的往往只有首片, 后续片的 .model
                        #   是 None, 裸赋值会被最后一片抹掉 (等价于原来的 `or model_used`)。
                        reported = getattr(chunk, "model", None)
                        if reported:
                            model_used = reported
                            # 去重判据在 llm_config 里, 与 fell_back 共用同一个 `_same_model`
                            # (终审 I-2): litellm 对同一次回答会报两种拼法, 裸 `not in` 会把
                            # 一个模型收成两项 ⇒ 徽章把 2 个模型写成 4 个串, R4 想要的
                            # "一眼看出实际是谁答的"就没了。⛔ 不在这里另写一套判据。
                            merge_reported_model(models_used, reported)
                        cu = getattr(chunk, "usage", None)
                        if cu:
                            cu_round = cu

                    if cu_round is not None:
                        usage_seen = True
                        usage_total["prompt_tokens"] += getattr(cu_round, "prompt_tokens", None) or 0
                        usage_total["completion_tokens"] += (
                            getattr(cu_round, "completion_tokens", None) or 0)
                        usage_total["total_tokens"] += getattr(cu_round, "total_tokens", None) or 0
                    else:
                        usage_missing = True

                    # 触顶判定与「是否继续工具循环」是两件事, 别混: 后者仍然只看 acc
                    # (见上面 chunk 循环里的注释), 前者只看 finish_reason。
                    # 本轮**同时**有工具调用又报触顶 ⇒ 走工具路径, 工具优先: 那一轮的
                    # 文本本来就会被回灌进 assistant 消息, 模型下一轮自然能接着说。
                    if acc or finish_reason not in _TRUNCATED_FINISH_REASONS:
                        break
                    if continue_rounds >= s.max_continue_rounds:
                        # 兜底触发: 收尾, 并在 done 里如实说「可能不完整」。⛔ 不许静默
                        # 收场 —— 无声的半句话正是本功能要消灭的那个失败模式。
                        truncated = True
                        break
                    continue_rounds += 1
                    # 回灌上一轮原文 + 续写指令。⚠ 用 user 消息而非 assistant prefill,
                    # 理由见 CONTINUE_PROMPT 上方 (prefill 是 Anthropic 专有, GPT 系不支持)。
                    #
                    # ⚠ 本轮一个可见字都没吐时**什么都不加**, 原样重开一轮 —— 预算刷新,
                    # 让模型把想清楚的东西写出来。实测 (真 Bedrock + opus-5, 天花板压到
                    # 200/1200) 这一支是**会发生**的: 预算可能被模型的内部思考吃光, 于是
                    # content 一个字没有却报 length。此时照旧回灌 `assistant: ""` 的后果:
                    # litellm 警告 "Potential consecutive user/tool blocks. Trying to merge."
                    # 并把空消息丢掉、合并相邻 user 块 ⇒ 模型收到一句"从断处接着写"却没有
                    # 可接的东西, 只能凭空编一个续写点。实测产物是从一个中段小标题开始的、
                    # **没有开头**的文章。
                    if round_parts:
                        msgs.append({"role": "assistant", "content": "".join(round_parts)})
                        msgs.append({"role": "user", "content": CONTINUE_PROMPT})
                    # 纯信息事件: 前端只记日志, 不画东西 —— 用户要的是一段连续的答案,
                    # 不是「这里换了一次 API 调用」这个实现细节。轮数在 done 里汇总呈现。
                    yield sse("continue", {"round": continue_rounds})

                # 没有工具调用 = 本轮就是最终答案; 本轮压根没挂工具 (web 关闭, 或已是收尾轮)
                # 也一律当最终答案 —— 没挂工具就不该解释工具调用, 更不该为它烧一次配额。
                if not acc or not with_tools:
                    break

                # 回灌 assistant 本轮的文本 + tool_calls。content 不能硬写 None —— 模型调
                # 工具前说的话已经流给用户了, 不回灌它就"忘了"自己说过什么, 最终答案会重复一遍。
                round_text = "".join(round_parts)
                msgs.append({"role": "assistant", "content": round_text or None, "tool_calls": [
                    {"id": v["id"], "type": "function",
                     "function": {"name": v["name"], "arguments": v["args"]}}
                    for _, v in sorted(acc.items())]})

                for _, v in sorted(acc.items()):
                    try:
                        query = json.loads(v["args"] or "{}").get("query", "")
                    except json.JSONDecodeError:
                        query = ""   # 模型偶发畸形 JSON: 当空查询处理, 不炸循环
                    yield sse("tool_call", {"round": rnd, "query": query, "id": v["id"]})

                    if v["name"] != "web_search":
                        # 工具分发不能"名字不管一律当 web_search"。模型点名不存在的工具就
                        # 如实告诉它, 不执行、不烧配额 —— 这是安全边界, 不只是健壮性。
                        refs, st = [], "unknown_tool"
                        content = json.dumps(
                            {"status": st, "results": [],
                             "error": f"No tool named {v['name']!r}. Only 'web_search' exists."},
                            ensure_ascii=False)
                    elif not query:
                        # 模型给了畸形/空 query: 是**模型**出错不是**联网**出错, 不能让用户
                        # 看到"联网失败"。如实标在这一条上, 不动 web_status。
                        refs, st = [], "bad_query"
                        content = json.dumps(
                            {"status": st, "results": [],
                             "error": "tool call carried no usable 'query' argument."},
                            ensure_ascii=False)
                    elif searcher.searches_used >= s.web_max_searches:
                        refs, st = [], "quota_exceeded"
                        content = render_tool_result(refs, st)
                    else:
                        # searcher.search 是同步 requests.post, 单次最长 web_timeout_s,
                        # 单请求可跑 web_max_searches 次 —— 直接调会把整个 event loop
                        # (所有并发 SSE 流 + 健康检查) 占死几分钟。本服务是 LAN 共享的。
                        refs, st = await asyncio.to_thread(searcher.search, query)
                        content = render_tool_result(refs, st)

                    if st == "ok":
                        web_ok += 1
                    elif st in _WEB_FAIL_RANK and (
                            web_fail is None or _WEB_FAIL_RANK[st] > _WEB_FAIL_RANK[web_fail]):
                        web_fail = st

                    yield sse("tool_result", {"id": v["id"], "count": len(refs),
                                              "status": st, "urls": [r.url for r in refs]})
                    msgs.append({"role": "tool", "tool_call_id": v["id"],
                                 "name": v["name"], "content": content})

            # 全成 -> ok; 有成有败 -> partial; 一次没成 -> 最严重的那个失败状态。
            # 逐条的失败细节不丢, 它已经在每条 tool_result 事件里。
            if web_fail is not None:
                web_status = "partial" if web_ok else web_fail

            # counting gate: 拼出来的答案与可核验的计数矛盾时, 在 done 之前补发一段修正 token
            if facts is not None:
                from server.grounding import apply_counting_gate
                full = "".join(parts)
                corrected, violations = apply_counting_gate(full, facts)
                if violations:
                    log.warning("structured_count_violation_stream", violations=violations)
                    yield sse("token", {"text": corrected[len(full):]})

            usage = None
            if usage_seen:
                usage = dict(usage_total)
                if usage_missing:
                    usage["partial"] = True   # 有轮次没拿到 usage, 总量不完整, 必须标明
            # web_searches_ok: 本次真正拿到结果的搜索次数。web_status 的 6 个值分不出
            # "开了联网但一次都没搜成" (模型净吐畸形/不存在的工具时它仍是 ok) —— 与其再往
            # 枚举里塞值让前端分支爆炸, 不如给一个整数, 顺带能显示"本次联网检索了 N 次"。
            fell = fell_back(s, body.model, models_used)
            if fell:
                # 让运维日志也留痕, 不只在用户屏幕上 —— 回退同时意味着"钱走了别的账"(C3/D4)
                # 与"答案来自未验证模型"两件事, 值得能被 grep 到。
                log.warning("model_fell_back", model_id=body.model, models_used=models_used)
            yield sse("done", {"model_used": model_used,
                               "models_used": models_used,
                               "model_id": body.model,
                               "verified": model_verified,
                               "fell_back": fell,
                               "usage": usage, "web_status": web_status,
                               "web_searches_ok": web_ok,
                               "continue_rounds": continue_rounds,
                               "truncated": truncated,
                               # 画面 PDF 旁路 (I2-3)。通道 OFF / 不発火なら両方 null ——
                               # 「付いていない」と「0 枚付いた」を客側が区別できる形。
                               "pdf_trigger": pdf_trigger,
                               "pdf_pages": pdf_pages,
                               # DM2 研读包。None = 通道没跑 (总闸 OFF); dict 里
                               # attached 说挂没挂, reason 说为何 (徽章/存档读它)。
                               "dossier": dossier_info})
        except Exception as e:  # noqa: BLE001 — 流已开, 以事件形式暴露
            log.error("stream_failed", error=str(e), exc_info=True)
            yield sse("error", {"message": "LLM stream failed"})

    return StreamingResponse(
        gen(), media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


# ── Dogfood failure capture (⚑ in chat UI -> append to backlog file) ──


class FlagRequest(BaseModel):
    question: str = Field("", max_length=10000)
    answer: str = Field("", max_length=50000)
    note: str = Field("", max_length=2000)
    # 归因串在回退时是"实际模型(可能多个)（回退自 用户选的）", 比单个模型名长得多。
    # 装不下的后果不是截断而是 422 ⇒ 用户点 ⚑ 后**记录失败** (前端会在按钮旁显示
    # "记录失败", 所以是**响的**失败不是静默的 —— 但那条反馈仍然丢了), 而 dogfood backlog
    # 正是本项目最贵的那类数据 (规则 B)。上限由
    # test_flag_model_field_fits_the_worst_case_attribution 用真实配置串钉住, 不是拍脑袋。
    model: str | None = Field(None, max_length=300)


@api_router.post("/flag")
def flag(body: FlagRequest, request: Request):
    """Append a flagged Q/A + note to the dogfood backlog (settings.dogfood_log_path).
    Single-user localhost tool: turns weak answers into a durable, prioritisable list
    instead of forgotten frustration. The file is a personal local log (not rendered to
    other users), so raw markdown in the fields is acceptable; the answer is wrapped in a
    <details> block so it can't bleed into the heading structure."""
    s = request.app.state.settings
    path = s.dogfood_log_path
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    note = body.note.strip() or "(no note)"
    entry = (
        f"\n## {ts}" + (f" · {body.model}" if body.model else "") + "\n\n"
        f"**Q:** {body.question.strip()}\n\n"
        f"**Note:** {note}\n\n"
        f"<details><summary>answer</summary>\n\n{body.answer.strip()}\n\n</details>\n\n---\n"
    )
    try:
        new = not path.exists()
        with path.open("a", encoding="utf-8") as f:
            if new:
                f.write(
                    "# Dogfood failure log\n\n"
                    "> chat UI 里 ⚑ 标记的答错/答弱例 + 期望, 作优先级 backlog "
                    "(append-only, 规则 B 失败不删)。\n"
                )
            f.write(entry)
    except OSError as e:
        log.error("flag_write_failed", error=str(e), path=str(path))
        raise HTTPException(status_code=500, detail="Could not write the flag log.") from e
    log.info("flag", question=body.question[:100], note=note[:120], path=str(path))
    return {"ok": True}


# ── Multi-model compare + judge (Phase 2; DEPLOY_PLAN §2.5) ───────────


class JudgeConfig(BaseModel):
    enabled: bool = False
    model: str | None = None  # None -> settings.judge_model


class AskCompareRequest(BaseModel):
    question: str = Field(max_length=10000)
    models: list[str] | None = None  # None -> settings.compare_models
    domain: str | None = None
    file_type: str | None = None
    history: list[MessageItem] = Field(default_factory=list)
    top_k: int | None = Field(None, ge=1, le=100)
    judge: JudgeConfig = Field(default_factory=JudgeConfig)


class ModelAnswerItem(BaseModel):
    model: str
    answer: str
    usage: dict | None = None
    latency_ms: int
    cost_usd: float | None = None
    error: str | None = None


class JudgeRankItem(BaseModel):
    model: str
    rank: int
    comment: str


class JudgeResult(BaseModel):
    ranking: list[JudgeRankItem]
    best_model: str | None = None
    rationale: str


class AskCompareResponse(BaseModel):
    sources: list[SourceItem]
    answers: list[ModelAnswerItem]
    judge: JudgeResult | None = None


# Safety cap: at most this many generation models per compare request. The UI offers
# 3 slots; the cap guards an arbitrary API caller from fanning out an unbounded burst.
_MAX_COMPARE_MODELS = 6


@api_router.post("/ask_compare", response_model=AskCompareResponse)
async def ask_compare(body: AskCompareRequest, request: Request):
    """One question -> N models answer over the SAME retrieved context, side by side,
    with an optional anonymized judge. Reuses retrieve/format/build (FR1: retrieval runs
    ONCE), then fans generation out in parallel (FR2) with per-model failure isolation
    (NFR2). See server/compare.py."""
    from server.auth import sanitize_compare_errors
    from server.compare import run_compare, run_judge

    rag = request.app.state.rag
    s = request.app.state.settings
    t0 = time.perf_counter()

    if not body.question.strip():
        raise HTTPException(status_code=422, detail="question must not be empty")

    models = [m.strip() for m in (body.models or s.compare_models) if m and m.strip()]
    # De-dup, preserving order: identical slots would render indistinguishable columns
    # and map two judge labels back to the same model name (ambiguous "best"). Running
    # the same model twice for variance is not a goal here (compare is temperature-0-ish
    # and aims to expose CROSS-model disagreement).
    models = list(dict.fromkeys(models))
    if not models:
        raise HTTPException(status_code=422, detail="no models specified")
    if len(models) > _MAX_COMPARE_MODELS:
        raise HTTPException(
            status_code=422,
            detail=f"too many models ({len(models)} > {_MAX_COMPARE_MODELS})",
        )

    log.info("ask_compare", question=body.question[:100], models=models,
             judge=body.judge.enabled, domain=body.domain)

    # retrieve/format/build are SYNC and run inline on the event loop. Intentional for
    # the §1 single-user localhost deployment (retrieval is fast vs the LLM calls that
    # dominate). If this ever moves multi-user (§6 搬云), wrap retrieve in
    # asyncio.to_thread so one request's retrieval can't serialize others.
    #
    # DM2: 本端点有意不挂研读包 (离线四模型对比评的是检索路径答案; 若要对比研读包答案需显式接
    # maybe_attach_dossier).
    try:
        chunks = rag.retrieve(
            body.question,
            domain=body.domain,
            file_type=body.file_type,
            top_k=body.top_k,
        )
    except Exception as e:
        log.error("retrieve_failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.") from e

    context = rag.format_context(chunks)
    history_dicts = [{"role": m.role, "content": m.content} for m in body.history]
    messages = rag.build_messages(body.question, context, history_dicts or None)

    # Outer ceiling over the whole parallel fan-out (REV MED-b): per-model timeout is
    # compare_timeout_s; this guards the request from exceeding request_timeout_s even if a
    # provider ignores its own timeout. wait_for cancels the pending gather on expiry.
    try:
        answers = await asyncio.wait_for(
            run_compare(
                models, messages,
                timeout_s=s.compare_timeout_s, num_retries=s.compare_num_retries,
            ),
            timeout=s.request_timeout_s,
        )
    except TimeoutError:
        log.error("ask_compare_timeout", request_timeout_s=s.request_timeout_s, models=models)
        raise HTTPException(status_code=504, detail="Compare request timed out.") from None

    judge_result = None
    if body.judge.enabled:
        judge_model = body.judge.model or s.judge_model
        try:
            judge_raw = await asyncio.wait_for(
                run_judge(
                    body.question, context, answers, judge_model,
                    timeout_s=s.compare_timeout_s, num_retries=s.compare_num_retries,
                ),
                timeout=s.request_timeout_s,
            )
        except TimeoutError:
            log.warning("judge_timeout", request_timeout_s=s.request_timeout_s)
            judge_raw = None
        if judge_raw:
            judge_result = JudgeResult(
                ranking=[JudgeRankItem(**r) for r in judge_raw["ranking"]],
                best_model=judge_raw["best_model"],
                rationale=judge_raw["rationale"],
            )

    sources = [
        SourceItem(
            chunk_id=c.chunk_id,
            source=c.source,
            domain=c.domain,
            file_type=c.file_type,
            section=c.section,
            similarity=c.similarity,
            text_preview=c.text[:300],
        )
        for c in chunks
    ]

    elapsed = time.perf_counter() - t0
    log.info(
        "ask_compare_done",
        chunks=len(chunks),
        n_models=len(answers),
        n_errors=sum(1 for a in answers if a.error),
        judged=judge_result is not None,
        elapsed_s=round(elapsed, 2),
    )

    # Sanitize client-facing per-model error strings when sharing (SEC MED). Done AFTER the
    # judge + the n_errors log so neither loses the real upstream detail (still in the log).
    answers = sanitize_compare_errors(answers, s.sanitize_errors)

    return AskCompareResponse(
        sources=sources,
        answers=[ModelAnswerItem(**vars(a)) for a in answers],
        judge=judge_result,
    )


# ── Dataset Validation (Phase 1C) ─────────────────────────────────────


@api_router.post("/validate")
async def validate_dataset(
    request: Request,
    file: UploadFile = File(...),
    domain: str | None = Form(None),
    dm_file: UploadFile | None = File(None),
    semantic_review: str = Form("true"),
):
    """Validate an SDTM dataset against KB specs + optional RAG semantic review."""
    from scripts.parse_dataset import ParseError, parse_bytes
    from server.report import FullReport, generate_json
    from server.reviewer import review
    from server.validator import validate

    spec_loader = request.app.state.spec_loader
    t0 = time.perf_counter()

    data = await file.read()
    filename = file.filename or "upload.csv"
    log.info("validate_start", filename=filename, size=len(data), domain=domain)

    try:
        df, meta = parse_bytes(data, filename)
    except ParseError as e:
        raise HTTPException(status_code=422, detail=str(e)) from e

    effective_domain = domain or meta.domain
    if not effective_domain:
        raise HTTPException(
            status_code=422,
            detail="Cannot detect domain. Provide 'domain' parameter or include DOMAIN column.",
        )

    dm_df = None
    if dm_file:
        dm_data = await dm_file.read()
        dm_filename = dm_file.filename or "dm.csv"
        try:
            dm_df, _ = parse_bytes(dm_data, dm_filename)
        except ParseError as e:
            raise HTTPException(status_code=422, detail=f"DM file error: {e}") from e

    val_result = validate(df, effective_domain, spec_loader, dm_df=dm_df)

    run_semantic = semantic_review.lower() in ("true", "1", "yes")
    review_result = None
    if run_semantic:
        try:
            rag = request.app.state.rag
            llm_router = request.app.state.llm_router
            review_result = review(
                df, effective_domain, meta.variables, rag,
                model="hard", llm_router=llm_router,
            )
        except Exception as e:
            log.error("semantic_review_failed", error=str(e))
            from server.reviewer import ReviewResult, SemanticFinding
            review_result = ReviewResult(
                domain=effective_domain,
                findings=[SemanticFinding(
                    "WARN", "business_rule",
                    "Semantic review failed",
                    "The LLM-based review could not be completed. Rule-based results are still valid.",
                )],
            )

    full = FullReport(
        domain=effective_domain,
        file_path=filename,
        row_count=meta.row_count,
        col_count=meta.col_count,
        completeness_pct=val_result.completeness_pct,
        validation=val_result,
        review=review_result,
    )

    elapsed = time.perf_counter() - t0
    log.info("validate_done", domain=effective_domain, errors=full.total_errors,
             warnings=full.total_warnings, elapsed_s=round(elapsed, 2))

    return generate_json(full)


@api_router.post("/validate-study")
async def validate_study(
    request: Request,
    files: list[UploadFile] = File(...),
):
    """Validate a multi-domain SDTM study: per-domain rule validation + SP5 graph
    checks (impact/completeness/CT-cascade) over the whole submission. Study-level is
    deterministic rule + graph checks only (no per-domain semantic LLM review)."""
    import pandas as pd

    from scripts.parse_dataset import ParseError, parse_bytes
    from server.config import settings
    from server.graph_engine import GraphEngine
    from server.graph_validator import run_graph_checks
    from server.meta_store import MetaStore
    from server.report import FullReport, generate_study_json
    from server.validator import validate

    spec_loader = request.app.state.spec_loader
    t0 = time.perf_counter()

    per_dataset: list[FullReport] = []
    frames: dict[str, pd.DataFrame] = {}  # domain -> DataFrame (for graph checks)
    for uf in files:
        data = await uf.read()
        fname = uf.filename or "upload.csv"
        try:
            df, meta = parse_bytes(data, fname)
        except ParseError as e:
            raise HTTPException(status_code=422, detail=f"{fname}: {e}") from e
        dom = (meta.domain or "").upper()
        if not dom:
            raise HTTPException(
                status_code=422,
                detail=f"{fname}: cannot detect domain (need a DOMAIN column).",
            )
        val = validate(df, dom, spec_loader)
        per_dataset.append(FullReport(
            domain=dom, file_path=fname, row_count=meta.row_count,
            col_count=meta.col_count, completeness_pct=val.completeness_pct,
            validation=val, review=None,
        ))
        frames[dom] = df

    engine = getattr(request.app.state, "graph_engine", None)
    if engine is None:  # bare-app / test path without lifespan
        engine = GraphEngine(MetaStore(settings.meta_path))
    graph_findings = run_graph_checks(frames, engine)
    out = generate_study_json(per_dataset, graph_findings)

    log.info("validate_study_done", n=len(files), verdict=out["study_verdict"],
             elapsed_s=round(time.perf_counter() - t0, 2))
    return out
