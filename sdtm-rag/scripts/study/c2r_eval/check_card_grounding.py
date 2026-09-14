#!/usr/bin/env python3
"""N5: study 出典の接地闸 (零 LLM) —— `[Source: st01__…]` を付けた記述の OID は、本当に
その文書に書いてあるか。

N4 の judge (§7) が拾った形: あるカードの真の出典を付けて、そのカードに**無い**活動 OID を
非表示アクティビティとして挙げる —— その OID は同じ run で検索された**兄弟カード**の非表示
リストに在った (= 移植; N4 審計の「16 源 0 次」は preview 300 字で grep した誤り、Erratum 済)、
真値と方向が逆。
画面層は N1/N2/N3 で『画面目視判読』『頁索引』に闸が付いたが、study 出典 (EDC 項目
カード / 手順書章節) には機械の闸が 1 つも無かった。ここはその層だけを撃つ。
**「非表示アクティビティ」だけの闸ではない**: study 出典を持つ記述の OID 全部が対象。

判定 (PLAN_c2r_pdf_bypass.md §10):
  SOURCE_GROUNDED   単元の OID が全部、引いた文書のどれかに在る
  SIBLING_NAMED     引いた文書には無いが、その OID 自身のカードがこの run の文脈に在る項目 OID
                    (文書の名前の言及; 緑と同じ扱いだが**別に数える** —— 真の命中と混ぜない)
  CONTEXT_MISCITED  引いた文書には無いが、その run で検索された別の study 源に在る = 出典違い
  UNGROUNDED        検索された study 源のどこにも無い = 捏造候補
  BAD_SOURCE        引いた path が磁盘に無い = 出典そのものが捏造 (実体照合は走らない)
  NEGATED           引いた文書に無い OID を、文が「無い / 含まれない」と言っている = 閘の事実と
                    文の主張が一致 (文の残りは検証できないので緑とは別に数える)
  NO_ENTITY         OID を 1 つも含まない単元 (標的外; 数だけ報告)

閘であって判分ではない: 赤 = 「その文書では言えない OID」であって「捏造が確定」ではない。
緑 = 「OID がその文書に在る」までで、**関係の向き** (表示 / 非表示、所属) は見ない。

実体にしないもの (設計; 各々の理由は当該箇所の注):
- フォーム OID (`NAC` 等): 21 種の**文書の名前**であって文書の中身ではない。path / 対応表 /
  画面 label の全部に出るうえ、活動 OID の族名 (`A_NAC_*` の「NAC 系」) としても書かれる。
- その run で**検索されたカードの項目 OID そのもの** (`st01__F__X.md` が文脈に在る X):
  文脈にある文書の名前を挙げただけで、あるカードの中身の主張ではない。1 文で兄弟項目を
  並べて出典を 1 つ付ける書き方が実データに多い (消融実測: この規則を切ると 36 文件で
  標紅 9 → 25、増分 16 件が全部この形)。緑ではなく SIBLING_NAMED として別に数える。
  ⚠ 穴 (既知): 兄弟カードを**比較する中身の主張** (「X と Y の非表示リストはほぼ同じ」
  「枠 G には X と Y が入る」) はこの規則で素通りする —— 閘は名前しか見ていない。
  **活動 OID は違う**: それは常にカードの中身 (非表示リスト) の主張なので、出典のカードに
  無ければ赤 (N4 の真陽性はまさにこの形: 別カードの非表示リストから移植された活動)。
- 対応表の書式 `OID(イベント › 活動)` の括弧の中身: 名前であって OID ではない (中に
  OID 形の語が偶然入る: 「ZNAC1コース」の ZNAC1)。
- 2 字以下の OID。

文脈 (CONTEXT) に数えるもの: 検索された study 源の全文 + **問題文** + **添付頁の
テキスト層** (B 臂; 画面から読んだ OID をカード出典で書くのは N2 型の出典違いで、
UNGROUNDED ではない)。出典マーカーは `[Source: …]` / 画面出典 / 『頁索引』の三種で切る。

既知の盲点:
- 極性を見ない。「A は非表示リストに**無い**」という正しい否定も肯定と同じに見える。
- 実体は catalog の OID (activity / form / event / item / item-group) だけ。**日本語名は
  見ない** —— 名前の合法な出所は対応表 (`_STUDY_OID_RULES`) であってカードではないので、
  名前を実体にすると規則どおりの答案が全部赤になる。**2 字以下の OID も見ない** (英字
  2 字の語に当たり放題)。catalog に無い OID 形の文字列 (存在しない OID の発明) も見ない。
- 兄弟カード間の**比較主張**・**関係の向き** (表示 / 非表示、所属) は見ない (上の穴)。
- attempt 2 の画面文除外の穴 (複審): **捏造に「画面では、」を前置すると両閘に見えない**
  (N2 は画面出典マーカーの無い文を単元にしない; N5 はここで捨てる)。文頭の画面指称だけを
  見るのは召回のため (文中の「画面」で捨てると既知真陽性が消える —— 消融実測)。
- 倒置の否定 (「指定されていないのは X です」) は、否定が OID より前に来るので NEGATED に
  ならず赤になる (假陽性方向; 本集 0 例)。judge が見たらこの類に帰属させること。
- 手順書章節は**節ファイル全体**で照合する (検索チャンクはその一部) = 超集で甘い方向。
- 単元は出典より**前**にしか伸びない (N2 と同じ設計)。

実行 (sdtm-rag/ から):
  .venv/bin/python scripts/study/c2r_eval/check_card_grounding.py c2r_v3 c2r_n1 c2r_n3 c2r_n3_a2 c2r_n4
  .venv/bin/python scripts/study/c2r_eval/check_card_grounding.py c2r_n4 --unmask
"""
from __future__ import annotations

import argparse
import functools
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from scripts.study.c2r_eval.check_visual_grounding import (  # noqa: E402
    _CITE_SEP_RE,
    _SOURCE_REF_RE,
    _bounded_re,
    _citation_spans,
    line_of,
    line_starts,
    nfkc,
    scope_start,
)
from scripts.study.paths import resolve_study  # noqa: E402

SOURCE_GROUNDED = "SOURCE_GROUNDED"
CONTEXT_MISCITED = "CONTEXT_MISCITED"
UNGROUNDED = "UNGROUNDED"
BAD_SOURCE = "BAD_SOURCE"
SIBLING_NAMED = "SIBLING_NAMED"
NEGATED = "NEGATED"
NO_ENTITY = "NO_ENTITY"
CLASSES = (SOURCE_GROUNDED, SIBLING_NAMED, CONTEXT_MISCITED, UNGROUNDED, BAD_SOURCE, NEGATED, NO_ENTITY)
FLAGGED = (CONTEXT_MISCITED, UNGROUNDED, BAD_SOURCE)
# 単元の等級は最悪の実体で決める。
# NEGATED は緑より上: 「無い」は閘が確かめたが、文の残りは確かめていない。
_SEVERITY = {BAD_SOURCE: 3, UNGROUNDED: 2, CONTEXT_MISCITED: 1, NEGATED: 0.5, SIBLING_NAMED: 0.25,
             SOURCE_GROUNDED: 0}
# 「その OID はこのカードの一覧に**無い**」型の文。閘が見つけた事実 (OID が引いた文書に無い)
# と文の主張が一致している —— 一致を疑いとして立てるのは間違い。文の残りは検証できない
# (極性の盲点はそのまま) ので、緑ではなく別の級にして数える。判定は**その OID を含む文**
# (「。」区切り) の中に否定の語があるかだけ。
_NEGATION_RE = re.compile(
    r"含まれ(?:ません|ない|ていない|ていません|ておらず|ていない)|指定(?:されて|して|が|は)?(?:いません|いない|ありません|ない|無い)|"
    r"列挙されて(?:いません|いない)|挙げられて(?:いません|いない)|入って(?:いません|いない)|"
    r"記載(?:が|は)?(?:ありません|ない|無い)|該当しません|"
    r"未列|未包含|不包含|没有(?:列|包含|指定)|不属于|not (?:listed|included|in the|among)")
# 文の切れ目: 句点・改行、それに ASCII の `.` は**後ろが空白か行末のときだけ** (複審 NIT-4:
# `8.1` / `p.174` を切ると OID と否定の語が離れて偽の赤になる)。
_SENT_SPLIT_RE = re.compile(r"(?<=[。．!?！？\n])|(?<=\.)(?=\s|$)")
# 小句: 述語の後ろの読点でさらに割る (複審 MINOR-1: 「A は非表示であり、他は含まれません」の
# A を後ろの小句の否定で守らない)。読点全部で割ってはいけない —— 日本語の列挙は読点で
# つなぐ (「A、B、および C では…ありません」) ので、述語 (であり / ており / し / が …) の
# 直後の読点だけを切れ目にする。否定の語は OID より**後ろ**に無ければならない。
# attempt 2: 画面を主語にした文 (出典を持たない) は画面の主張 = N2 の担当。後ろのカード出典
# に帰属させると、画面から読んだ項目 OID がカードに無いのは当たり前なので赤になる (回扫の
# 純假陽性 4 件中 2 件がこの形)。文頭の画面指称だけを見る —— 文中に「画面」が出るだけでは
# 取らない (「カードでは X、画面では Y」の混在文まで捨てると穴になる)。
_SCREEN_LEAD_RE = re.compile(
    r"^\s*[-*・]?\s*(?:また、|なお、|一方、|ただし、)?\s*"
    r"(?:画面(?:上|では|には|で|に|の)|添付(?:頁|の画面|画像)|頁画像|p\.\s*\d+\s*の画面|"
    r"画面 p\.\s*\d+|画面 (?:workflow|annotated)|(?:workflow|annotated) p\.\s*\d+|"
    r"画面目視|附图|画面中|屏幕)")
# 洞 B (複審): 文頭が画面指称でも、文中でカード / 手順書に帰属している主張は捨てない。
_CARD_ATTRIB_RE = re.compile(r"カード|項目カード|手順書|章節|対応表|卡片|項目定義")
_CLAUSE_SPLIT_RE = re.compile(
    r"(?<=であり、)|(?<=であって、)|(?<=ており、)|(?<=ていて、)|(?<=なく、)|(?<=ず、)|(?<=し、)|"
    r"(?<=が、)|(?<=ため、)|(?<=ものの、)|(?<=けれど、)|(?<=けれども、)|(?<=[;；])")

_MIN_OID_LEN = 3
_ENTITY_KINDS = ("activity", "event", "item", "group")     # form は実体にしない (上の注)
# OID に直付けされた括弧 = 名前の注記 (対応表の書式 `OID(イベント名 › 活動名)`; モデルは
# `›` を省いて `A_X(A群 ZNAC1コース_day8)` とも書く)。全角/半角どちらも実データに出る。
# 括弧の中身は**捨てない** (複審 MAJOR-3: 捨てると `WEIGHT (A_ZOPE で非表示扱い)` が素通り)。
# 中では境界を厳しくするだけ: 名前の中の OID 形の語は日本語に**接着**している (「ZNAC1コース」)
# が、本物の OID の言及は独立した語 (空白・句読点・括弧に挟まれる)。
_GLOSSARY_PAREN_RE = re.compile(r"(?<=[A-Za-z0-9_`])\s?[（(][^()（）\n]{1,80}[)）]")
_CJK = "぀-ヿ一-鿿"


@functools.lru_cache(maxsize=4096)
def _strict_re(oid: str) -> re.Pattern[str]:
    return re.compile(rf"(?<![A-Za-z0-9_{_CJK}]){re.escape(oid)}(?![A-Za-z0-9_{_CJK}])")
# 『頁索引』出典 (N3 の規則が定める出典名)。単元の切れ目としてだけ使う。
_INDEX_CITE_RE = re.compile(r"[『【\[〔]\s*頁索引\s*[』】\]〕]")
# path は最初の空白 / 読点まで。実データは `[Source: st01__doc01__s8_1.md 8.1]` や
# `[…, §8.1]` のように節番号を後ろに付ける (規則「節番号を保持すること」の産物)。
# `st01__doc01__s3_8.md(3.8)` のように括弧を直付けする形も出る。
_SOURCE_PATH_RE = re.compile(r"\[Source:\s*([^\s,，(（\]\n]+)[^\]\n]*\]")
_SAFE_PATH_RE = re.compile(r"^[A-Za-z0-9_.\-]+$")


@dataclass(frozen=True)
class Vocab:
    """catalog の OID 語彙。kind は報告用で、判定は kind を見ない。"""
    oids: dict[str, str]
    n_skipped_short: int

    @classmethod
    def from_catalog(cls, catalog: dict) -> Vocab:
        raw: dict[str, str] = {}
        for kind, key, rows in (("activity", "oid", catalog.get("activities", ())),
                                ("form", "oid", catalog.get("forms", ())),
                                ("event", "oid", catalog.get("events", ())),
                                ("item", "item_oid", catalog.get("items", ())),
                                ("group", "group_oid", catalog.get("items", ()))):
            for r in rows:
                oid = r.get(key)
                if oid:
                    raw.setdefault(oid, kind)
        kept = {o: k for o, k in raw.items() if len(o) >= _MIN_OID_LEN and k in _ENTITY_KINDS}
        return cls(kept, sum(1 for o in raw if len(o) < _MIN_OID_LEN))

    @property
    def patterns(self) -> list[tuple[str, str, re.Pattern[str]]]:
        # 長い OID から。`WEIGHTZST` と `WEIGHT` は有界照合で既に別語だが、報告の順が安定する。
        return [(o, k, _bounded_re(o)) for o, k in sorted(self.oids.items(), key=lambda t: -len(t[0]))]


class SourceStore:
    """study 文書 (cards/ + docs/) の本文。path 名 → テキスト。磁盘の読み出しはここだけ。"""

    def __init__(self, study_id: str, root: Path | None, texts: dict[str, str] | None = None):
        self.prefix = f"{study_id}__"
        self.root = root
        self._texts = texts
        self._cache: dict[str, str | None] = {}

    @classmethod
    def from_dict(cls, study_id: str, texts: dict[str, str]) -> SourceStore:
        return cls(study_id, None, texts)

    def is_study(self, path: str) -> bool:
        return path.startswith(self.prefix)

    def text(self, path: str) -> str | None:
        if path in self._cache:
            return self._cache[path]
        if self._texts is not None:
            t = self._texts.get(path)
        else:
            # 安全でない path (区切り / `..` 等) は読みに行かない = 磁盘に無い扱い。
            # 例外にすると、発明された出典 1 つで回扫全体が止まる。
            t = None
            if not _SAFE_PATH_RE.match(path):
                self._cache[path] = None
                return None
            for sub in ("cards", "docs"):
                f = self.root / sub / path  # type: ignore[operator]
                if f.is_file():
                    t = f.read_text(encoding="utf-8")
                    break
        self._cache[path] = None if t is None else nfkc(t)
        return self._cache[path]


@dataclass(frozen=True)
class Unit:
    text: str
    line: int
    sources: tuple[str, ...]


@dataclass(frozen=True)
class Verdict:
    unit: Unit
    klass: str
    entities: tuple[dict, ...]
    missing_sources: tuple[str, ...] = ()
    screen_sentences: int = 0          # attempt 2: 実体集から外した画面文の数 (観測用)

    @property
    def sources(self) -> tuple[str, ...]:
        return self.unit.sources


@dataclass
class AnswerReport:
    file: str
    arm: str
    model: str
    qid: str
    n_units: int
    counts: dict[str, int]
    verdicts: list[Verdict] = field(default_factory=list)


def _source_markers(text: str, store: SourceStore) -> list[tuple[int, int, str, str | None]]:
    """出典マーカー全部を位置つきで: (開始, 終了, 種類, path)。種類 = "study" / "other" /
    "screen"。study 以外も要る —— 単元は**直前の出典 (種類を問わず)** で切る。"""
    out: list[tuple[int, int, str, str | None]] = []
    for m in _SOURCE_PATH_RE.finditer(text):
        path = m.group(1)
        out.append((m.start(), m.end(), "study" if store.is_study(path) else "other", path))
    for s, e, _ in _citation_spans(text):
        out.append((s, e, "screen", None))
    for m in _INDEX_CITE_RE.finditer(text):
        out.append((m.start(), m.end(), "index", None))
    return sorted(out)


def split_units(answer: str, store: SourceStore) -> list[Unit]:
    """study 出典を持つ主張単元に切る。単元 = 直前の出典の直後 (または行頭; 中身が無ければ
    上の塊ごと) から、この study 出典 (連続するものは 1 つの帰属リスト) の末尾まで。"""
    text = nfkc(answer)
    lines, line_start = line_starts(text)
    marks = _source_markers(text, store)
    units: list[Unit] = []
    idx = 0
    while idx < len(marks):
        start, end, kind, path = marks[idx]
        if kind != "study":
            idx += 1
            continue
        paths = [path]
        last = idx
        while (last + 1 < len(marks) and marks[last + 1][2] == "study"
               and _CITE_SEP_RE.fullmatch(text[marks[last][1]:marks[last + 1][0]])):
            last += 1
            paths.append(marks[last][3])
        end = marks[last][1]
        prev_end = marks[idx - 1][1] if idx else 0
        i = line_of(line_start, start)
        scope = scope_start(text, lines, line_start, prev_end, start, i)
        units.append(Unit(text[scope:end], i + 1, tuple(p for p in paths if p)))
        idx = last + 1
    return units


class Grounding:
    def __init__(self, vocab: Vocab, store: SourceStore):
        self.vocab = vocab
        self.store = store

    @staticmethod
    def _drop_screen_sentences(text: str) -> tuple[str, int]:
        """画面指称で始まり、出典を持たない文を外す (attempt 2)。文単位 = 改行 / 句点。"""
        kept: list[str] = []
        dropped = 0
        for sent in _SENT_SPLIT_RE.split(text):
            if _SCREEN_LEAD_RE.match(sent) and not _SOURCE_REF_RE.search(sent) \
                    and not _INDEX_CITE_RE.search(sent) and not _CARD_ATTRIB_RE.search(sent):
                dropped += 1
                continue
            kept.append(sent)
        return "".join(kept), dropped

    def _entities_in(self, text: str) -> list[tuple[str, str]]:
        # 出典マーカーの中の OID (path に form / item が入る) は主張ではないので消す。
        # 名前の注記 (OID 直付けの括弧) は本文から外して、中は厳しい境界で別に見る。
        text, _ = self._drop_screen_sentences(text)
        no_ref = _SOURCE_REF_RE.sub(" ", text)
        body = _GLOSSARY_PAREN_RE.sub(" ", no_ref)
        parens = " ".join(m.group(0) for m in _GLOSSARY_PAREN_RE.finditer(no_ref))
        found: list[tuple[str, str]] = []
        for oid, kind, pat in self.vocab.patterns:
            if pat.search(body) or (parens and _strict_re(oid).search(parens)):
                found.append((oid, kind))
        return found

    def check_answer(self, answer: str, retrieved: list[str], *,
                     extra_context: str = "") -> list[Verdict]:
        """`retrieved` = その run で検索された study 源の path。`extra_context` = 問題文と
        添付頁のテキスト層 (OID の出所として合法だが、カードの中身ではない)。"""
        ctx_paths = [p for p in retrieved if self.store.is_study(p)]
        ctx_texts = [t for p in ctx_paths if (t := self.store.text(p)) is not None]
        if extra_context:
            ctx_texts.append(nfkc(extra_context))
        # 文脈に在るカードの項目 OID = 文書の名前 (上の設計注)。
        sibling_items = {p.split("__")[-1].removesuffix(".md") for p in ctx_paths
                         if p.count("__") >= 2 and "__doc" not in p}
        verdicts: list[Verdict] = []
        for u in split_units(answer, self.store):
            cited = {p: self.store.text(p) for p in u.sources}
            missing = tuple(p for p, t in cited.items() if t is None)
            if missing:
                verdicts.append(Verdict(u, BAD_SOURCE, (), missing))
                continue
            ents = []
            kept, n_screen = self._drop_screen_sentences(u.text)
            body = _GLOSSARY_PAREN_RE.sub(" ", _SOURCE_REF_RE.sub(" ", kept))
            clauses = [c for sent in _SENT_SPLIT_RE.split(body) for c in _CLAUSE_SPLIT_RE.split(sent)]
            for oid, kind in self._entities_in(u.text):
                pat = _bounded_re(oid)
                if any(pat.search(t) for t in cited.values() if t):
                    st = SOURCE_GROUNDED
                elif kind == "item" and oid in sibling_items:
                    st = SIBLING_NAMED         # 文脈にある文書の名前 (設計注); 真の命中と混ぜない
                elif any((m := pat.search(x)) and _NEGATION_RE.search(x, m.end()) for x in clauses):
                    st = NEGATED
                elif any(pat.search(t) for t in ctx_texts):
                    st = CONTEXT_MISCITED
                else:
                    st = UNGROUNDED
                ents.append({"oid": oid, "kind": kind, "status": st})
            if not ents:
                klass = NO_ENTITY
            else:
                klass = max((e["status"] for e in ents), key=lambda k: _SEVERITY[k])
            verdicts.append(Verdict(u, klass, tuple(ents), screen_sentences=n_screen))
        return verdicts


# ── ラン ディレクトリの集計 ───────────────────────────────────────────────
def _retrieved(resp: dict) -> list[str]:
    return [s.get("source", "") for s in (resp.get("sources") or [])
            if s.get("corpus") == "study" or not s.get("corpus")]


def _questions(runs_root: Path) -> dict[str, str]:
    """題面 (gitignored `c2r_v3/questions.json`; T/N 組)。無ければ空。"""
    f = runs_root / "c2r_v3" / "questions.json"
    if not f.is_file():
        return {}
    q = json.loads(f.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for grp in ("T", "N"):
        for qid, text in (q.get(grp) or {}).items():
            out[qid] = text if isinstance(text, str) else json.dumps(text, ensure_ascii=False)
    return out


def analyse_dir(runs_dir: Path, grounding: Grounding, arm: str | None = None, *,
                questions: dict[str, str] | None = None,
                page_text=None) -> list[AnswerReport]:
    """`page_text(pdf, page) -> str` は添付頁のテキスト層 (N2 の `PageText`)。無ければ頁は文脈に入らない。"""
    reports: list[AnswerReport] = []
    for f in sorted(Path(runs_dir).glob("*.json")):
        if f.name in {"questions.json", "visual_grounding.json", "card_grounding.json"}:
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        meta, resp = d.get("_meta", {}), d.get("response", {})
        if arm and meta.get("arm") != arm:
            continue
        extra = [(questions or {}).get(meta.get("qid", ""), "")]
        if page_text is not None:
            extra += [page_text(p["pdf"], int(p["page"])) for p in (resp.get("pdf_pages") or [])]
        verdicts = grounding.check_answer(resp.get("answer") or "", _retrieved(resp),
                                          extra_context="\n".join(x for x in extra if x))
        counts = {k: sum(1 for v in verdicts if v.klass == k) for k in CLASSES}
        reports.append(AnswerReport(
            file=f.name, arm=meta.get("arm", "?"), model=meta.get("model_id", "?"),
            qid=meta.get("qid", "?"), n_units=len(verdicts), counts=counts, verdicts=verdicts))
    return reports


def _mask(v: Verdict) -> str:
    if v.klass == BAD_SOURCE:
        return f"{len(v.missing_sources)} cited path(s) not on disk; entities not checked"
    if not v.entities:
        return "no entity"
    by: dict[str, int] = {}
    for e in v.entities:
        by[e["status"]] = by.get(e["status"], 0) + 1
    return ", ".join(f"{n} {st}" for st, n in sorted(by.items()))


def render_table(reports: list[AnswerReport], unmask: bool = False) -> str:
    cols = ["file", "model", "qid", "units", "grounded", "sibling", "miscited", "ungrounded", "bad-src",
            "negated", "no-ent"]
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    tot = {k: 0 for k in CLASSES}
    tot_units = 0
    for r in reports:
        c = r.counts
        out.append("| " + " | ".join([
            r.file, r.model, r.qid, str(r.n_units), str(c[SOURCE_GROUNDED]), str(c[SIBLING_NAMED]),
            str(c[CONTEXT_MISCITED]), str(c[UNGROUNDED]), str(c[BAD_SOURCE]), str(c[NEGATED]),
            str(c[NO_ENTITY])]) + " |")
        for k in CLASSES:
            tot[k] += c[k]
        tot_units += r.n_units
    out.append("| " + " | ".join([
        f"**{len(reports)} files**", "", "", f"**{tot_units}**", f"**{tot[SOURCE_GROUNDED]}**",
        f"**{tot[SIBLING_NAMED]}**", f"**{tot[CONTEXT_MISCITED]}**", f"**{tot[UNGROUNDED]}**", f"**{tot[BAD_SOURCE]}**",
        f"**{tot[NEGATED]}**", f"**{tot[NO_ENTITY]}**"]) + " |")
    negated = [(r, v) for r in reports for v in r.verdicts if v.klass == NEGATED]
    if negated:
        # 複審 MINOR-4: NEGATED は閘自身の極性判断。judge が抽検できるよう場所だけ出す。
        out.append("")
        out.append(f"### negated units ({len(negated)}; not flagged, for spot-check)")
        for r, v in negated:
            out.append(f"- {r.file} L{v.unit.line} [{len(v.sources)} src] NEGATED ({_mask(v)})")
    flagged = [(r, v) for r in reports for v in r.verdicts if v.klass in FLAGGED]
    if flagged:
        out.append("")
        out.append(f"### flagged units ({len(flagged)})")
        for r, v in flagged:
            out.append(f"- {r.file} L{v.unit.line} [{len(v.sources)} src] **{v.klass}** ({_mask(v)})")
            if unmask:
                ents = "; ".join(f"{e['kind']}:{e['oid']}={e['status']}" for e in v.entities) or "-"
                out.append(f"    sources: {', '.join(v.sources)}")
                out.append(f"    entities: {ents}")
                out.append(f"    text: {v.unit.text.replace(chr(10), ' ⏎ ')}")
    return "\n".join(out)


def _json_payload(reports: list[AnswerReport], vocab: Vocab, *,
                  n_questions: int = 0, page_text_available: bool = False) -> dict:
    # 複審 MINOR-2: 問題文と頁テキストは gitignored / PDF 依存。無いと 3 単元が MISCITED から
    # UNGROUNDED に落ちる (消融実測) のに黙っていた。証拠件に「その回の文脈が揃っていたか」を残す。
    return {
        "vocab": {"n_oids": len(vocab.oids), "n_skipped_short": vocab.n_skipped_short},
        "context": {"n_questions": n_questions, "page_text_available": page_text_available},
        "totals": {k: sum(r.counts[k] for r in reports) for k in CLASSES}
        | {"units": sum(r.n_units for r in reports), "files": len(reports),
           "screen_sentences": sum(v.screen_sentences for r in reports for v in r.verdicts)},
        "answers": [{
            "file": r.file, "arm": r.arm, "model": r.model, "qid": r.qid,
            "n_units": r.n_units, "counts": r.counts,
            "units": [{
                "line": v.unit.line, "class": v.klass, "sources": list(v.sources),
                "missing_sources": list(v.missing_sources), "screen_sentences": v.screen_sentences,
                "entities": list(v.entities), "text": v.unit.text,
            } for v in r.verdicts],
        } for r in reports],
    }


def build_grounding(study_id: str = "st01") -> tuple[Grounding, Path, Vocab]:
    sp = resolve_study(study_id)
    catalog = json.loads((sp.out_dir / "catalog.json").read_text(encoding="utf-8"))
    vocab = Vocab.from_catalog(catalog)
    return Grounding(vocab, SourceStore(study_id, sp.out_dir)), sp.out_dir / "eval" / "runs", vocab


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="C2R N5: study 出典 ([Source: st01__…]) の接地闸 (零 LLM)")
    ap.add_argument("dirs", nargs="+", help="runs/ 配下のディレクトリ名 (例: c2r_v3 c2r_n4)")
    ap.add_argument("--arm", default=None, help="臂で絞る (例: B)")
    ap.add_argument("--unmask", action="store_true", help="OID / 本文も出す (画面用, 貼らない)")
    ap.add_argument("--study", default="st01")
    a = ap.parse_args(argv)

    grounding, runs_root, vocab = build_grounding(a.study)
    questions = _questions(runs_root)
    if not questions:
        print("WARNING: questions.json not found —— 問題文は文脈に入らない (MISCITED が UNGROUNDED に落ちる)")
    # 複審 MINOR-3: 添付頁のテキスト層は N2 の道具 (PDF + sha 検証) を借りる。カード層の判定自体は
    # PDF を要らないので、無ければ降級して続ける (その旨は payload に残る)。
    try:
        from scripts.study.c2r_eval.check_visual_grounding import build_grounding as _n2
        page_text = _n2(a.study)[0].page_text
    except (FileNotFoundError, RuntimeError) as e:
        print(f"WARNING: page text unavailable ({e}) —— 添付頁は文脈に入らない")
        page_text = None
    print(f"vocab: {len(vocab.oids)} OIDs (skipped short: {vocab.n_skipped_short}); "
          f"questions: {len(questions)}; page_text: {'yes' if page_text else 'no'}")
    rc = 0
    for name in a.dirs:
        runs_dir = Path(name) if Path(name).is_dir() else runs_root / name
        reports = analyse_dir(runs_dir, grounding, arm=a.arm, questions=questions, page_text=page_text)
        print(f"\n## {runs_dir.name}  (arm={a.arm or 'all'})")
        print(render_table(reports, unmask=a.unmask))
        out = runs_dir / "card_grounding.json"
        out.write_text(json.dumps(_json_payload(reports, vocab, n_questions=len(questions),
                                                page_text_available=page_text is not None),
                                  ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nsaved -> {out}")
        if any(v.klass in FLAGGED for r in reports for v in r.verdicts):
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
