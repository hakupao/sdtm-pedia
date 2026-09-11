#!/usr/bin/env python3
"""N2: 画面出処の接地闸 (零 LLM) —— 『画面目視判読 p.NN』が本当にその頁の画像で言えるか。

V3 §4 第 3 条 / N1 §2.2 #4 / §2.6 #11 は同じ形をしている: **底層の事実は真** (折り畳んだ
ブロック集合や块表という、builder が label に書き込んだメタ情報) なのに、出処が
『画面目視判読 p.NN』になっている —— その頁の画像には、そんな注記は一行も無い。
頁番号の越界闸 (runner §8) は添付頁の中で起きるこの捏造を構造的に見られず、N1 の
「添付頁の範囲では」規則も否定断言しか縛らない。ここはその隙間だけを撃つ。

判定 (PLAN_c2r_pdf_bypass.md §7):
  PAGE_GROUNDED    主張単元の実体が全部その頁のテキスト層に在る (実体ゼロも含む)
  LABEL_ATTRIBUTED 頁に無いが **label のメタ情報** に在る = 画像由来ではない
  OFF_PAGE         頁にも label にも無い
  OUT_OF_RANGE     引いた頁が添付頁集合の外
  AMBIGUOUS        頁名が無く、同じ頁番号が両 PDF に添付されていて帰属できない

闸であって判分ではない: ここが赤くても「捏造が確定」ではなく「画像では言えない出処」。
逆に緑は「その頁に実体名が写っている」までしか言っていない (下の盲点を見よ)。

既知の盲点 (全量は evidence/checkpoints/c2r_n2_visual_grounding.md §6):
- 頁テキスト層だけを見る。図中の文字や、テキスト層に落ちないレイアウト情報 (枠線・
  パネルの境界) は見えない —— N1 §2.5 #8 型 (面板边界の合併) は原理的に検出できない。
- **文の極性を見ない**。「X はこの頁に無い」という正しい否定も、「同じ画面だとは確認
  できない」という hedge も、肯定の主張と同じに見える (実測の假陽性 2 件はこれ)。
- 実体は activity / form の OID と名前、それに annotated 頁の**項目グループ名**
  (`page_groups`, N3 が label に載せる情報) だけ。item OID は**入れない**: workflow の
  頁テキストに OID は 1 つも出ない (S0 実測) ので、入れた瞬間に全主張が OFF_PAGE になる。
- 単元は出典より**前**にしか伸びない (出典は後置の帰属なので)。出典を主張の前に置く
  書き方は取りこぼす —— 実測 39 の実体ゼロ単元のうち 19 件で、出典の直後に実体が在る。
- 折り畳み集合は索引から**復算**した超集。builder は問題が名指しした活動を畳まないので、
  そのランの label には出ていない名前も含む (LABEL 判定が甘い方向に外れる)。

実行 (sdtm-rag/ から):
  .venv/bin/python scripts/study/c2r_eval/check_visual_grounding.py c2r_v3 c2r_n1 --arm B
  .venv/bin/python scripts/study/c2r_eval/check_visual_grounding.py c2r_n1 --unmask
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from scripts.study.paths import resolve_study  # noqa: E402

PAGE_GROUNDED = "PAGE_GROUNDED"
LABEL_ATTRIBUTED = "LABEL_ATTRIBUTED"
OFF_PAGE = "OFF_PAGE"
OUT_OF_RANGE = "OUT_OF_RANGE"
AMBIGUOUS = "AMBIGUOUS"
CLASSES = (PAGE_GROUNDED, LABEL_ATTRIBUTED, OFF_PAGE, OUT_OF_RANGE, AMBIGUOUS)
# 人が見に行くべき単元。AMBIGUOUS も入れる: 帰属できていない主張を
# 「無罪」側に置くと、闸の緑が「確かめた」の意味を失う。
FLAGGED = (LABEL_ATTRIBUTED, OFF_PAGE, OUT_OF_RANGE, AMBIGUOUS)

REASON_ENTITY = "entity"
REASON_SAMENESS = "sameness-vocab"

PDF_KEYS = ("workflow", "annotated")

# 出典マーカー。简/繁(日) 両方が実データに出る —— 同じ答案の中で混在した例すらある。
_CITE_MARK = re.compile(r"画面目[視视]判[読读]")
# マーカーから頁番号までの許容距離。地の文の「画面目視判読という手段は…」が 2 段落先の
# `p.NN` を拾わないための窓。実データの出典は一様に「マーカー + 10 字以内」。
_CITE_WINDOW = 40
_PDF_NAME_RE = re.compile(r"(workflow|annotated)")
_PAGE_RE = re.compile(r"p\.\s*(\d{1,4})(?:\s*[–—〜~−-]\s*(\d{1,4}))?")
# カード / 標準の出典。答案の三分来源のうち画面以外の 2 つはこの形で出る。
_SOURCE_REF_RE = re.compile(r"\[Source:[^\]\n]*\]")
_CLOSE_RE = re.compile(r"[』】〕\]〉》)）]")
# 頁の列挙の区切り。読点・空白だけでなく「と」「および」「and」も実データに出る ——
# これを落とすと `p.29 と p.74` の 2 頁目が別の主張の頁に見え、引用頁が 1 枚に化ける。
_SEP_RE = re.compile(r"(?:[\s,，、;；・/&]|と|および|及び|または|or|and)*", re.IGNORECASE)
# 出典どうしの間が「区切りだけ」なら同じ帰属リスト
_CITE_SEP_RE = re.compile(r"[\s、,，・;；\[\]『』【】〔〕]*")
# 名前の出どころを言うだけの帰属句 (L1 が答題時に付ける「活動 OID 対応表」)。**句だけ**
# 落として長さを測る: 文ごと落とすと「X は対応表より Y であり、画面には Z が並ぶ」のような
# 混在文まで中身ゼロ扱いになり、単元が不必要に上へ伸びる。
_TABLE_ATTRIB_RE = re.compile(r"(?:名称|名前)?は?、?\s*(?:EDC\s*)?(?:OID\s*)?対応表(?:より|による|から)[。、]?")
_MIN_UNIT_CHARS = 12
_MAX_RANGE = 30           # `p.A–B` の展開上限 (誤読で 900 頁展開しないための安全弁)

# 実体名の下限。日本語に語境界は無いので裸の部分文字列照合になり、短い名前ほど地の文に
# 偶然現れる (`server/pdf_context.py::_MIN_ACTIVITY_NAME_LEN` と同じ天秤)。ここは闸なので
# 取りこぼし側に倒し、pdf_context の 4 ではなく PLAN §7 の 3 を採る。
_MIN_NAME_LEN = 3
# 項目グループ名の下限。活動名より緩い 2: 枠の名前は実データで 2 字のものが普通に在り、
# しかも照合先は**その頁の枠一覧**という狭い集合なので、偶然当たる面が小さい。
_MIN_GROUP_NAME_LEN = 2

# 主張単元の遡り上限。出典が単独行で後置される形 (実データに頻出) を拾うために前の行まで
# 見るが、節ひとつを丸ごと 1 単元にすると無関係な実体まで巻き込む。
_MAX_SCOPE_LINES = 15
_BOUNDARY_RE = re.compile(r"^\s*(?:#{1,6}\s|-{3,}\s*$|\*{3,}\s*$|={3,}\s*$)")
# 箇条書き / 番号付き / 表の行。出典が塊の後ろに後置された時、塊は途中で切らない。
_LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+・]\s|\d+[.)、]\s?|\|)")
# 出典の後ろを覗く量 (盲点の実測用; 判定には使わない)。
_TAIL_CHARS = 200

# ── 画面同一性の主張 (実体照合の第 2 の網) ────────────────────────────────
# **1 枚の頁画像は「別の画面も同じ」を証明できない**。その同一性は builder が label に
# 書いた「同一画面: …」にしか無い情報で、頁の上には一行も無い (V3 §4 第 3 条 /
# N1 §2.2 #4 / §2.6 #11 の 3 件はすべてこの形)。実体照合が解けない言い換え
# (活動名を中国語に意訳する等) でも、この**概念**は残る。
#
# 語彙は概念の語彙 (同一性 × 画面) であって、実データから拾った言い回しの一覧ではない:
# 日本語 / 简体 / 繁体の同一性語をまとめて置き、画面を指す名詞の近くに出たら取る。
_SAMENESS_LEX_RE = re.compile(
    r"完全に同じ|まったく同じ|全く同じ|完全相同|同样的|同樣的|"
    r"同じ|同一|同様|同樣|同等|共通|共有|共用|一致|相同|同样|同樣")
_SCREEN_NOUN_RE = re.compile(r"画面構成|显示画面|顯示画面|画面|表示|レイアウト|页面|頁面|ページ|頁")
# 同一性語から画面名詞までの許容距離。文 1 つ分 (実データの主張はこの範囲に収まる)。
_SAMENESS_WINDOW = 25
# ① 1 つの画面の**中**の話 (「同一画面内/上に…が並ぶ」「同じ画面に…表示される」) は
#    画面をまたぐ同一性の主張ではない。
_INTRA_SCREEN_RE = re.compile(
    r"^(?:の|な)?(?:画面構成|显示画面|画面|表示|レイアウト|页面|ページ|頁)"
    # 「で」は格助詞だけ。「です」の「で」まで取ると「…は同じ画面です」という
    # まさに拾いたい断定が画面**内**の話に化ける。
    r"(?:内|上|の中|には|では|に|で(?!す))")
# ② 同一性が掛かっている対象が画面ではなく中身 (項目・値・順序…) の時も対象外。
_SAMENESS_OBJECT_RE = re.compile(
    r"^(?:の|な)?(?:項目|項|欄|値|データ|内容|順序|並び|番号|グループ|セクション|"
    r"項目名|条件|定義|項目群)")


def nfkc(s: str) -> str:
    """NFKC 正規化 (空白は保つ) —— 有界 OID 照合はこちらの上で行う。

    空白を潰したテキストで境界を判定すると、隣接関係が人工的に作られて短い OID の
    判定が揺れる (`server/study_lookup.py::_norm_ws` の同じ理由)。
    """
    return unicodedata.normalize("NFKC", s)


def squash(s: str) -> str:
    """NFKC + 全空白除去 —— 日本語名の部分文字列照合用。

    `pdftotext -layout` の頁テキストは桁揃えの空白だらけで、名前の途中に空白が入ることも
    ある。名前側・頁側の両方をここに通してから比べる。
    """
    return re.sub(r"\s+", "", nfkc(s))


def _bounded_re(oid: str) -> re.Pattern[str]:
    """有界照合。`server/study_lookup.py::_bounded_re` と同じ境界語義 (両側が
    [A-Za-z0-9_] でない)。短い OID (2-3 字は実データに普通に在る) が無関係な語の
    部分文字列に当たるのを防ぐ。CJK は境界文字扱いなので日本語に挟まれても当たる。
    """
    return re.compile(rf"(?<![A-Za-z0-9_]){re.escape(oid)}(?![A-Za-z0-9_])")


@dataclass(frozen=True)
class Entity:
    kind: str        # "activity" | "form" | "group"
    oid: str
    name: str        # activity は短名 (イベント名を落としたもの), form は form 名, group は枠の名前
    # group だけ: その枠の見出しが**前の頁**から続いている (= この頁には見出しが無い)。
    continued: bool = False

    @property
    def key(self) -> tuple[str, str]:
        return (self.kind, self.oid)


@dataclass(frozen=True)
class Citation:
    pdf: str | None
    pages: tuple[int, ...]
    # 頁参照が読めなかった (範囲が `_MAX_RANGE` 超, 逆順など)。黙って先頭頁に丸めると
    # 「引用頁はこれ 1 枚」と誤って断定してしまうので、帰属不能として扱う。
    unparsable: bool = False


@dataclass(frozen=True)
class Unit:
    text: str
    line: int                     # 出典が載っている行 (1 始まり)
    citations: tuple[Citation, ...]
    tail: str = ""                # 出典の**後ろ**の本文 (次のマーカーまで); 観測専用


@dataclass(frozen=True)
class Verdict:
    unit: Unit
    klass: str
    reason: str
    pages: tuple[tuple[str, int], ...]
    entities: tuple[dict, ...]
    no_entity: bool
    # 実体ゼロの単元のうち、出典の**直後**に実体が出てくるもの。単元は前にしか伸びない
    # という設計上の盲点の実測量 (§6 盲点 8)。
    entity_after: bool = False


@dataclass
class AnswerReport:
    file: str
    arm: str
    model: str
    qid: str
    n_units: int
    counts: dict[str, int]
    no_entity: int
    verdicts: list[Verdict] = field(default_factory=list)


class PageIndex:
    """`data/study/<id>/pdf_page_index.json` の読み取り専用の薄い包み。

    形の自己検証は `server/pdf_context.py::PdfPageIndex` と同じ理由で入れる: S0 の勘察
    草案は同じ拡張子でブロックが list の list なので、素通しすると読めない例外になる。
    """

    def __init__(self, data: dict):
        if data.get("meta", {}).get("draft"):
            raise ValueError("S0 勘察の草案索引 (meta.draft=true)。生産索引を使うこと")
        blocks = data.get("workflow", {}).get("blocks")
        if not isinstance(blocks, list) or (blocks and not isinstance(blocks[0], dict)):
            raise ValueError("pdf_page_index: workflow.blocks が dict のリストではない")
        self._d = data
        names = data.get("names", {})
        self.forms: dict[str, str] = dict(names.get("forms", {}))
        self.activities: dict[str, str] = {
            oid: name.split("›")[-1].strip() for oid, name in names.get("activities", {}).items()
        }
        self._wf_blocks: list[dict] = list(data["workflow"]["blocks"])
        self._ann_blocks: list[dict] = list(data["annotated"]["blocks"])
        # N3 が足す頁内の項目グループ (label の「本頁の項目グループ順: …」の出どころ)。
        # 無い索引 (N3 以前) では黙って空 —— 闸は他の実体だけで動く。
        self._page_groups: dict = data["annotated"].get("page_groups") or {}
        self.entities: tuple[Entity, ...] = tuple(
            [Entity("activity", oid, self.activities[oid]) for oid in sorted(self.activities)]
            + [Entity("form", oid, self.forms[oid]) for oid in sorted(self.forms)]
        )

    @classmethod
    def load(cls, path: Path | str) -> PageIndex:
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    def sha(self, pdf_key: str) -> str:
        return self._d["meta"]["pdfs"][pdf_key]["sha256"]

    def block_for(self, pdf: str, page: int) -> dict | None:
        blocks = self._wf_blocks if pdf == "workflow" else self._ann_blocks
        for b in blocks:
            if b["start"] <= page <= b["end"]:
                return b
        return None

    def own_keys(self, pdf: str, page: int) -> set[tuple[str, str]]:
        """その頁**自身**の宛名 (属するブロックの activity / form)。

        これは通道が全ての添付頁について label の見出しで明示的に教えている情報
        (【画面 workflow p.74 — …アクティビティ名 / フォーム名 (OID) の実表示】)。
        「この頁は X フォームの画面だ」と書くのは捏造ではなく宛名の復唱なので、
        `folded_keys` (他ブロックの話) とは分けて扱う。
        """
        b = self.block_for(pdf, page)
        if b is None:
            return set()
        if pdf == "annotated":
            return {("form", b["form_oid"])}
        return {("activity", b["activity_oid"]), ("form", b["form_oid"])}

    def page_group_entities(self, pdf: str, page: int) -> list[Entity]:
        """その annotated 頁の**項目グループ名** (label が「本頁の項目グループ順」で載せる)。

        これも頁索引由来のメタ情報であって、画像から読んだ事実ではない。とくに
        `continued` な枠は見出しが**前の頁**に在るので、その頁の画像には名前が無い ——
        名前を挙げて『画面目視判読 p.NN』と書けば、それは label を読んだということ。

        名前の無い枠 ((無題)) は実体にしない: 照合できる文字列が無いし、label 側も
        「(無題)」としか言っていない。
        """
        if pdf != "annotated" or not self._page_groups:
            return []
        b = self.block_for(pdf, page)
        if b is None:
            return []
        rows = self._page_groups.get(b["form_oid"], {}).get(str(page), [])
        out: list[Entity] = []
        for r in rows:
            name = (r.get("name") or "").strip()
            if len(squash(name)) < _MIN_GROUP_NAME_LEN:
                continue
            # `continued` が無い索引 (生成途中の版) は「続きではない」と読む。判定自体は
            # 頁テキストに名前が在るかで決まるので、この既定値で結論は変わらない。
            out.append(Entity("group", r.get("group_oid") or "", name,
                              bool(r.get("continued", False))))
        return out

    def folded_keys(self, pdf: str, page: int) -> set[tuple[str, str]]:
        """label が「同一画面: …」として書き添える**他ブロック**の activity。

        同 form・同 hidden_items のブロック = builder の画面キー
        (`pdf_context._workflow_candidates`) をそのまま復算する。頁の画像からは
        絶対に読めない情報で、N2 が撃つのはここに帰属する主張。
        """
        b = self.block_for(pdf, page)
        if b is None or pdf == "annotated":
            return set()
        screen = tuple(sorted(b["hidden_items"]))
        return {("activity", o["activity_oid"]) for o in self._wf_blocks
                if o["form_oid"] == b["form_oid"]
                and tuple(sorted(o["hidden_items"])) == screen
                and o["activity_oid"] != b["activity_oid"]}


def _citation_spans(text: str) -> list[tuple[int, int, Citation]]:
    """NFKC 済みテキストの出典を (開始, 終了, Citation) で返す。マーカー 1 つ = 出典 1 つ。

    窓は「次のマーカーの手前」「閉じ括弧」「`_CITE_WINDOW` 字」の一番手前。頁は
    **連続している間だけ** 取る —— 区切り (読点・空白) 以外の地の文を挟んだ `p.N` は
    次の主張の頁であって、この出典の頁ではない。これを見ないと
    「〔画面目視判読 workflow p.34〕 ただし、これは p.34–43 ブロックのうち…」の
    ブロック範囲まで引用頁に化け、正しい注意書きが丸ごと OUT_OF_RANGE になる。
    """
    marks = list(_CITE_MARK.finditer(text))
    out: list[tuple[int, int, Citation]] = []
    for i, m in enumerate(marks):
        end = min(len(text), m.end() + _CITE_WINDOW)
        if i + 1 < len(marks):
            end = min(end, marks[i + 1].start())
        win = text[m.end():end]
        close = _CLOSE_RE.search(win)
        if close:
            win = win[:close.start()]
        pages: list[int] = []
        last_end: int | None = None
        first_start: int | None = None
        unparsable = False
        for pm in _PAGE_RE.finditer(win):
            if last_end is not None and not _SEP_RE.fullmatch(win[last_end:pm.start()]):
                break
            if first_start is None:
                first_start = pm.start()
            lo = int(pm.group(1))
            hi = int(pm.group(2)) if pm.group(2) else lo
            if hi < lo or hi - lo > _MAX_RANGE:
                # 読めない範囲。先頭頁に丸めると「引用頁はこの 1 枚」と誤って断定する
                # ことになるので、この出典は帰属不能として立てる。
                unparsable = True
                last_end = pm.end()
                continue
            pages.extend(p for p in range(lo, hi + 1) if p not in pages)
            last_end = pm.end()
        # PDF 名は**最初の頁参照より前**でだけ探す。後ろまで見ると、上の連続性で切った
        # 先にある別の主張の「annotated p.164」から名前だけ拾ってしまう。
        name = _PDF_NAME_RE.search(win[:first_start] if first_start is not None else win)
        out.append((m.start(), m.end() + (last_end or 0),
                    Citation(name.group(1) if name else None, tuple(pages), unparsable)))
    return out


def parse_citations(text: str) -> list[Citation]:
    return [c for _, _, c in _citation_spans(text)]


def _content_len(s: str) -> int:
    """出典・帰属句を除いた「主張の中身」の文字数 (記号と空白は数えない)。

    ⚠ この長さが `_MIN_UNIT_CHARS` 未満かどうかで単元が上へ伸びるかが決まり、既知
    捏造 3 件のうち 1 件 (出典が「名称は…対応表より。〔出典〕」の行に後置される形) の
    召回はここに依存している。だからこそ**句だけ**を落とす: 「対応表」を含む文を丸ごと
    落とすと「X は対応表より Y であり、画面には Z が並ぶ」のような混在文まで中身ゼロに
    なり、伸ばす必要の無い単元まで上へ伸びて假陽性を作る。
    """
    s = _SOURCE_REF_RE.sub("", s)
    s = _CITE_MARK.sub("", s)
    s = _TABLE_ATTRIB_RE.sub("", s)
    return len(re.findall(r"\w", s))


def is_screen_sameness_claim(text: str, n_pages: int = 1) -> bool:
    """「この画面は別の画面とも同じ」型の主張か (概念判定)。

    成立の理屈は 1 つ: **1 枚の頁画像は、別の活動の画面がこれと同じであることを証明
    できない**。その同一性は builder が label に書いた「同一画面: …」由来であって、
    頁の上には無い。だから実体照合が解けない言い換えでも、この概念さえ見えれば拾える。

    取らない場合:
    - 1 つの画面の**中**の話 (「同一画面上に…が並ぶ」)。画面をまたいでいない。
    - 同一性が掛かっている対象が画面でなく中身 (項目・値・順序…)。
    - **添付頁を 2 枚以上引いている**主張。見えている 2 枚を見比べて「同じ」と言うのは
      画像から言える —— label を持ち出す必要が無い。
    """
    if n_pages >= 2:
        return False
    # 出典そのものを先に消す: 「画面目視判読」というマーカー自体が「画面」を含むので、
    # 消さないと出典を書いただけで画面名詞が 1 つ立ってしまう。
    t = _CITE_MARK.sub(" ", _SOURCE_REF_RE.sub(" ", text))
    for m in _SAMENESS_LEX_RE.finditer(t):
        after = t[m.end():m.end() + 8]
        if _INTRA_SCREEN_RE.match(after) or _SAMENESS_OBJECT_RE.match(after):
            continue
        lo = max(0, m.start() - _SAMENESS_WINDOW)
        if _SCREEN_NOUN_RE.search(t[lo:m.end() + _SAMENESS_WINDOW]):
            return True
    return False


def _markers(text: str) -> list[tuple[int, int, str]]:
    """出典マーカーを位置つきで全部拾う: 画面出典と **カード出典 `[Source: …]`**。

    カード出典も数えるのが要: 実データの答案は「カード事実 [Source: …]。…画面の話
    〔画面目視判読 p.N〕」と 1 行に両方を書く。カード出典を無視すると、カードに帰属
    された非表示アクティビティの一覧が画面主張の単元に流れ込み、頁に無いのは当たり前
    なので全部 OFF_PAGE になる (実測: それだけで假陽性 5 件)。
    """
    out: list[tuple[int, int, str]] = [(s, e, "screen") for s, e, _ in _citation_spans(text)]
    for sm in _SOURCE_REF_RE.finditer(text):
        out.append((sm.start(), sm.end(), "source"))
    return sorted(out)


def split_units(answer: str) -> list[Unit]:
    """出典を持つ主張単元に切る。

    単元 = **直前の出典 (画面でもカードでも) の直後から、その画面出典の末尾まで**。
    見出し / 水平線 / `_MAX_SCOPE_LINES` 行でも止まる。

    行単位で切らないのは両側から要る:
    ① 箇条書きの後に出典が単独行で後置される形 (N1 §2.6 #11 がまさにそれ) —— 行だけ
       見ると単元に実体が 1 つも入らず素通りする。
    ② 逆に出典の**後ろ**に続くカード由来の文 (同じ行にある) は、その画面出典の担当では
       ない —— 巻き込むと頁に無い実体だらけになる。出典は後置の帰属なので、単元は
       出典で閉じる。
    """
    text = nfkc(answer)
    line_start = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            line_start.append(i + 1)
    lines = text.split("\n")

    def line_of(pos: int) -> int:
        lo, hi = 0, len(line_start) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if line_start[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo

    units: list[Unit] = []
    marks = _markers(text)
    idx = 0
    while idx < len(marks):
        start, end, kind = marks[idx]
        if kind != "screen":
            idx += 1
            continue
        def _cits(a: int, b: int) -> list[Citation]:
            return [c for c in parse_citations(text[a:b]) if c.pages or c.unparsable]

        citations = _cits(start, end)
        # 続けて並ぶ出典 (`[… p.29] [… p.74] [… p.87]`) は 1 つの帰属リスト。別々の
        # 主張に割ると、同じ本文が最初の頁だけで採点され、他の頁に写っているものまで
        # OFF_PAGE になる。
        last = idx
        while (last + 1 < len(marks) and marks[last + 1][2] == "screen"
               and _CITE_SEP_RE.fullmatch(text[marks[last][1]:marks[last + 1][0]])):
            last += 1
            citations += _cits(marks[last][0], marks[last][1])
        end = marks[last][1]
        if not citations:
            idx = last + 1
            continue
        prev_end = marks[idx - 1][1] if idx else 0
        i = line_of(start)
        scope = max(prev_end, line_start[i])
        # 前の行まで遡るのは、出典行それ自体が**中身を持たない**時だけ。出典は後置の
        # 帰属なので普通は自分の行を担っており、無条件に遡ると手前のカード/対応表由来の
        # 文まで巻き込む。逆に「名称は対応表より。〔出典〕」のような純粋な帰属行は、
        # 担っている本文が上にある (N1 §2.6 #11 がその形)。
        #
        # 遡る時は**箇条書き / 表の塊を丸ごと**取る。「中身が足りたら止める」にすると
        # 7 項目の箇条書きのうち最後の 1 行しか入らず、捏造が塊の先頭に在れば素通りする
        # —— 出典は塊全体を担っているので、途中で切る根拠が無い。
        if _content_len(text[scope:start]) < _MIN_UNIT_CHARS:
            j = i
            while j - 1 >= 0 and i - (j - 1) <= _MAX_SCOPE_LINES:
                prev = lines[j - 1]
                if line_start[j - 1] < prev_end or _BOUNDARY_RE.match(prev):
                    break
                if not prev.strip():
                    # 空行は塊の中の息継ぎ。**塊が続いているなら**跨ぐ (箇条書きと
                    # その導入文の間、箇条書きと後置出典の間はどちらも空行で空く)。
                    k = j - 1
                    while k - 1 >= 0 and not lines[k - 1].strip():
                        k -= 1
                    if k - 1 < 0 or line_start[k - 1] < prev_end or _BOUNDARY_RE.match(lines[k - 1]):
                        break
                    j = k
                    continue
                was_list = _LIST_ITEM_RE.match(prev) is not None
                j -= 1
                if not was_list and _content_len(text[line_start[j]:start]) >= _MIN_UNIT_CHARS:
                    break           # 塊の導入文まで取ったら止める
            scope = max(prev_end, line_start[j])
        tail_end = marks[last + 1][0] if last + 1 < len(marks) else len(text)
        units.append(Unit(text[scope:end], i + 1, tuple(citations),
                          text[end:min(tail_end, end + _TAIL_CHARS)]))
        idx = last + 1
    return units


class Grounding:
    def __init__(self, index: PageIndex, page_text: Callable[[str, int], str], *,
                 sameness_rule: bool = True):
        self.index = index
        self.page_text = page_text
        self.sameness_rule = sameness_rule
        self._page_cache: dict[tuple[str, int], tuple[str, str]] = {}

    # ── 照合 ──────────────────────────────────────────────────────────
    def _page_forms(self, pdf: str, page: int) -> tuple[str, str]:
        key = (pdf, page)
        if key not in self._page_cache:
            raw = self.page_text(pdf, page) or ""
            self._page_cache[key] = (nfkc(raw), squash(raw))
        return self._page_cache[key]

    @staticmethod
    def _mention(ent: Entity, text_ws: str, text_sq: str) -> str | None:
        # group は名前照合だけ。枠の OID は画面にも答案にも出てこない識別子で、
        # 短いものは無関係な語に当たる。
        if ent.kind != "group" and ent.oid and _bounded_re(ent.oid).search(text_ws):
            return "oid"
        name = squash(ent.name)
        floor = _MIN_GROUP_NAME_LEN if ent.kind == "group" else _MIN_NAME_LEN
        if len(name) >= floor and name in text_sq:
            return "name"
        return None

    def _entities_in(self, text: str, extra: Sequence[Entity] = ()) -> list[tuple[Entity, str]]:
        """主張単元が名指ししている実体。名前照合は**極大一致**だけ取る。

        実データの活動短名は互いの部分文字列になる (`偽活動一` ⊂
        `偽活動一_追加検査` のような入れ子が普通にある)。素の部分文字列照合だと、長い名前を
        1 つ書いただけで短い名前の活動が 3-4 個「名指しされた」ことになり、その頁に無いのは当然なので
        まとめて OFF_PAGE になる。`pdf_context.form_named_in` が「長い名前を先に見る」
        のと同じ天秤 —— あちらは 1 つ選ぶので順序、こちらは集合なので被覆判定。
        """
        ws, sq = nfkc(text), squash(text)
        hits: list[tuple[Entity, str]] = []
        by_name: list[tuple[Entity, str, list[tuple[int, int]]]] = []
        for e in (*self.index.entities, *extra):
            if e.kind != "group" and e.oid and _bounded_re(e.oid).search(ws):
                hits.append((e, "oid"))
                continue
            name = squash(e.name)
            if len(name) < (_MIN_GROUP_NAME_LEN if e.kind == "group" else _MIN_NAME_LEN):
                continue
            spans = [(m.start(), m.end()) for m in re.finditer(re.escape(name), sq)]
            if spans:
                by_name.append((e, name, spans))
        for e, name, spans in by_name:
            covered = all(
                any(o_s <= s and t <= o_t and len(o_name) > len(name)
                    for _, o_name, o_spans in by_name for o_s, o_t in o_spans)
                for s, t in spans)
            if not covered:
                hits.append((e, "name"))
        return sorted(hits, key=lambda h: (h[0].kind, h[0].oid))

    # ── 頁の帰属 ──────────────────────────────────────────────────────
    @staticmethod
    def _resolve_pages(citations: Iterable[Citation],
                       attached: Sequence[tuple[str, int]]) -> tuple[list[tuple[str, int]], str]:
        """引用頁 → (帰属できた頁, 状態)。状態は "" / OUT_OF_RANGE / AMBIGUOUS。"""
        by_page: dict[int, list[str]] = {}
        for pdf, page in attached:
            by_page.setdefault(page, []).append(pdf)
        resolved: list[tuple[str, int]] = []
        status = ""
        for c in citations:
            if c.unparsable:
                status = AMBIGUOUS      # 頁参照が読めない = 帰属できない
            for page in c.pages:
                if c.pdf is not None:
                    if (c.pdf, page) in set(attached):
                        resolved.append((c.pdf, page))
                    else:
                        return resolved, OUT_OF_RANGE
                    continue
                owners = by_page.get(page, [])
                if not owners:
                    return resolved, OUT_OF_RANGE
                if len(set(owners)) > 1:
                    status = AMBIGUOUS
                    continue
                resolved.append((owners[0], page))
        return resolved, status

    # ── 判定 ──────────────────────────────────────────────────────────
    def classify(self, unit: Unit, attached: Sequence[tuple[str, int]]) -> Verdict:
        pages, status = self._resolve_pages(unit.citations, attached)
        if status:
            return Verdict(unit, status, "page-attribution", tuple(pages), (), False)

        own_keys: set[tuple[str, str]] = set()
        folded_keys: set[tuple[str, str]] = set()
        groups: dict[tuple[str, str], Entity] = {}
        for pdf, page in pages:
            own_keys |= self.index.own_keys(pdf, page)
            folded_keys |= self.index.folded_keys(pdf, page)
            for gent in self.index.page_group_entities(pdf, page):
                groups.setdefault((gent.oid, gent.name), gent)
        mentioned = self._entities_in(unit.text, tuple(groups.values()))
        details: list[dict] = []
        for ent, how in mentioned:
            on_page = any(self._mention(ent, *self._page_forms(pdf, page)) is not None
                          for pdf, page in pages)
            if on_page:
                st = "page"
            elif ent.kind == "group":
                # 引いた頁の枠なのに、その頁のテキスト層に名前が無い = 見出しが前の頁に
                # 在る (continued) か、そもそも画像に無い。どちらでも「label 由来」。
                st = "label"
            elif ent.key in own_keys:
                st = "own"          # 頁の宛名 (label の見出し) —— 捏造ではない
            elif ent.key in folded_keys:
                st = "label"
            else:
                st = "off"
            d = {"kind": ent.kind, "oid": ent.oid, "name": ent.name,
                 "mentioned_as": how, "status": st}
            if ent.kind == "group":
                d["continued"] = ent.continued
            details.append(d)

        statuses = {d["status"] for d in details}
        if "off" in statuses:
            klass, reason = OFF_PAGE, REASON_ENTITY
        elif "label" in statuses:
            klass, reason = LABEL_ATTRIBUTED, REASON_ENTITY
        else:
            klass, reason = PAGE_GROUNDED, REASON_ENTITY
        if (klass == PAGE_GROUNDED and self.sameness_rule
                and is_screen_sameness_claim(unit.text, n_pages=len(set(pages)))):
            klass, reason = LABEL_ATTRIBUTED, REASON_SAMENESS
        after = bool(not details and unit.tail and self._entities_in(unit.tail))
        return Verdict(unit, klass, reason, tuple(pages), tuple(details), not details, after)

    def check_answer(self, answer: str,
                     attached: Sequence[tuple[str, int]]) -> list[Verdict]:
        return [self.classify(u, attached) for u in split_units(answer)]


# ── ラン ディレクトリの集計 ───────────────────────────────────────────────
def _attached(resp: dict) -> list[tuple[str, int]]:
    return [(p["pdf"], int(p["page"])) for p in (resp.get("pdf_pages") or [])]


def analyse_dir(runs_dir: Path, grounding: Grounding, arm: str | None = None) -> list[AnswerReport]:
    reports: list[AnswerReport] = []
    for f in sorted(Path(runs_dir).glob("*.json")):
        if f.name in {"questions.json", "visual_grounding.json"}:
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        meta, resp = d.get("_meta", {}), d.get("response", {})
        if arm and meta.get("arm") != arm:
            continue
        attached = _attached(resp)
        if not attached:          # 通道が発火しなかった答案 = 画面主張が在り得ない
            continue
        verdicts = grounding.check_answer(resp.get("answer") or "", attached)
        counts = {k: sum(1 for v in verdicts if v.klass == k) for k in CLASSES}
        reports.append(AnswerReport(
            file=f.name, arm=meta.get("arm", "?"), model=meta.get("model_id", "?"),
            qid=meta.get("qid", "?"), n_units=len(verdicts), counts=counts,
            no_entity=sum(1 for v in verdicts if v.no_entity), verdicts=verdicts))
    return reports


def _mask(v: Verdict) -> str:
    """実体の**数と状態**だけ。OID / 名前 / 問題文は 1 文字も出さない。"""
    if v.klass == AMBIGUOUS:
        # 帰属できていないので実体照合は走っていない。「no entity」と書くと
        # 「実体が無いから無罪」と読めてしまう。
        return "page not attributable; entities not checked"
    if not v.entities:
        return "no entity"
    by: dict[str, int] = {}
    for e in v.entities:
        by[e["status"]] = by.get(e["status"], 0) + 1
    return ", ".join(f"{n} {st}" for st, n in sorted(by.items()))


def render_table(reports: list[AnswerReport], unmask: bool = False) -> str:
    cols = ["file", "model", "qid", "units", "grounded", "label", "off", "range", "ambig",
            "no-ent", "ent-after"]
    out = ["| " + " | ".join(cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    tot = {k: 0 for k in CLASSES}
    tot_units = tot_noent = tot_after = 0
    for r in reports:
        c = r.counts
        after = sum(1 for v in r.verdicts if v.entity_after)
        out.append("| " + " | ".join([
            r.file, r.model, r.qid, str(r.n_units), str(c[PAGE_GROUNDED]),
            str(c[LABEL_ATTRIBUTED]), str(c[OFF_PAGE]), str(c[OUT_OF_RANGE]),
            str(c[AMBIGUOUS]), str(r.no_entity), str(after)]) + " |")
        for k in CLASSES:
            tot[k] += c[k]
        tot_units += r.n_units
        tot_noent += r.no_entity
        tot_after += after
    out.append("| " + " | ".join([
        f"**{len(reports)} files**", "", "", f"**{tot_units}**", f"**{tot[PAGE_GROUNDED]}**",
        f"**{tot[LABEL_ATTRIBUTED]}**", f"**{tot[OFF_PAGE]}**", f"**{tot[OUT_OF_RANGE]}**",
        f"**{tot[AMBIGUOUS]}**", f"**{tot_noent}**", f"**{tot_after}**"]) + " |")

    flagged = [(r, v) for r in reports for v in r.verdicts if v.klass in FLAGGED]
    if flagged:
        out.append("")
        out.append(f"### flagged units ({len(flagged)})")
        for r, v in flagged:
            pages = ", ".join(f"{p} p.{n}" for p, n in v.pages) or "-"
            out.append(f"- {r.file} L{v.unit.line} [{pages}] **{v.klass}** "
                       f"({v.reason}; {_mask(v)})")
            if unmask:
                ents = "; ".join(f"{e['kind']}:{e['oid']}/{e['name']}={e['status']}"
                                 for e in v.entities) or "-"
                out.append(f"    entities: {ents}")
                out.append(f"    text: {v.unit.text.replace(chr(10), ' ⏎ ')}")
    return "\n".join(out)


def _json_payload(reports: list[AnswerReport], sameness_rule: bool) -> dict:
    return {
        "sameness_rule": sameness_rule,
        "totals": {k: sum(r.counts[k] for r in reports) for k in CLASSES}
        | {"units": sum(r.n_units for r in reports),
           "no_entity": sum(r.no_entity for r in reports),
           "entity_after": sum(1 for r in reports for v in r.verdicts if v.entity_after),
           "files": len(reports)},
        "answers": [{
            "file": r.file, "arm": r.arm, "model": r.model, "qid": r.qid,
            "n_units": r.n_units, "counts": r.counts, "no_entity": r.no_entity,
            "units": [{
                "line": v.unit.line, "class": v.klass, "reason": v.reason,
                "pages": [f"{p} p.{n}" for p, n in v.pages],
                "entities": list(v.entities), "no_entity": v.no_entity,
                "entity_after": v.entity_after, "text": v.unit.text,
            } for v in r.verdicts],
        } for r in reports],
    }


# ── 実 PDF 側 (子プロセス境界はここ 1 箇所) ───────────────────────────────
class PageText:
    """`pdftotext -layout -f N -l N` の頁テキスト。gitignored なディスクキャッシュ付き。"""

    def __init__(self, pdf_paths: dict[str, Path], cache_dir: Path):
        self.pdf_paths = pdf_paths
        self.cache_dir = Path(cache_dir)

    def __call__(self, pdf: str, page: int) -> str:
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        f = self.cache_dir / f"{pdf}_p{page}.txt"
        if f.is_file():
            return f.read_text(encoding="utf-8")
        r = subprocess.run(
            ["pdftotext", "-layout", "-f", str(page), "-l", str(page),
             str(self.pdf_paths[pdf]), "-"],
            capture_output=True, text=True, check=False)
        if r.returncode != 0:
            raise RuntimeError(f"pdftotext failed: {pdf} p.{page}: {r.stderr[:200]}")
        f.write_text(r.stdout, encoding="utf-8")
        return r.stdout


def verify_pdf_sha(index: PageIndex, paths: dict[str, Path | None]) -> None:
    """PDF の実体が索引の `meta.sha256` と一致するか。違えば**出数しない**。

    頁番号は PDF の版に紐づく: 差し替わった PDF に古い索引を当てると、闸は別の画面を
    根拠に「接地している」と言う —— 索引欠落 (頁が付かないだけ) より悪い。
    """
    for key in PDF_KEYS:
        p = paths.get(key)
        if p is None or not Path(p).is_file():
            raise FileNotFoundError(f"{key} pdf not found: {p}")
        h = hashlib.sha256()
        with Path(p).open("rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
        if h.hexdigest() != index.sha(key):
            raise RuntimeError(
                f"{key} pdf sha256 mismatch (index={index.sha(key)[:12]}… "
                f"file={h.hexdigest()[:12]}…) — 索引を作り直す: "
                "scripts/study/build_pdf_page_index.py")


def build_grounding(study_id: str = "st01", *, sameness_rule: bool = True) -> tuple[Grounding, Path]:
    """生産の索引 + 実 PDF で闸を組む。"""
    sp = resolve_study(study_id)
    index = PageIndex.load(sp.out_dir / "pdf_page_index.json")
    paths: dict[str, Path | None] = {"workflow": sp.pdf_workflow, "annotated": sp.pdf_annotated}
    verify_pdf_sha(index, paths)
    return (Grounding(index, PageText({k: Path(paths[k]) for k in PDF_KEYS},  # type: ignore[arg-type]
                                      sp.out_dir / ".pdf_page_txt"),
                      sameness_rule=sameness_rule),
            sp.out_dir / "eval" / "runs")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="C2R N2: 『画面目視判読 p.NN』の接地闸 (零 LLM)")
    ap.add_argument("dirs", nargs="+", help="runs/ 配下のディレクトリ名 (例: c2r_v3 c2r_n1)")
    ap.add_argument("--arm", default=None, help="臂で絞る (例: B)")
    ap.add_argument("--unmask", action="store_true", help="OID / 名前 / 本文も出す (画面用, 貼らない)")
    ap.add_argument("--study", default="st01")
    ap.add_argument("--no-sameness-rule", action="store_true",
                    help="画面同一性の語彙規則を切る (実体照合だけの数を見るため)")
    a = ap.parse_args(argv)

    grounding, runs_root = build_grounding(a.study, sameness_rule=not a.no_sameness_rule)
    rc = 0
    for name in a.dirs:
        runs_dir = Path(name) if Path(name).is_dir() else runs_root / name
        reports = analyse_dir(runs_dir, grounding, arm=a.arm)
        print(f"\n## {runs_dir.name}  (arm={a.arm or 'all'}, "
              f"sameness_rule={'off' if a.no_sameness_rule else 'on'})")
        print(render_table(reports, unmask=a.unmask))
        out = runs_dir / "visual_grounding.json"
        out.write_text(json.dumps(_json_payload(reports, not a.no_sameness_rule),
                                  ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nsaved -> {out}")
        if any(v.klass in FLAGGED for r in reports for v in r.verdicts):
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
