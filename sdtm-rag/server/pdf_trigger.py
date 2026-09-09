"""I2-3: 画面 PDF 旁路を付けるかどうかの**純粋関数** (P1 §3 の R1/R2/R3)。

設計の要 (PLAN_c2r_pdf_bypass.md §0-2): 判定材料は**命中したカードの形**であって、
問題文を路由モデルに読ませることではない。よってここは LLM を一切呼ばない ——
呼べば「なぜ付いた/付かなかった」が再現できなくなり、反例集も回帰にならない。

⚠ P1 §3 からの逸脱 1 件 (実装時に発見, 意図的):
R1 の語彙表 (visit / 時点 / いつ / 表示 / 出る / 每次 / 只录一次 / 显示) では P1 §1 の
**T4「…採取項目がどう違いますか」が発火しない** —— T4 は「2 つの活動で表示項目がどう
違うか」を訊いており R1 の狙いそのものなのに、語彙表に差異系の語が 1 つも無かった。
example ではなく**語のクラス**を 1 つ足して塞いだ (差異・比較: 違い/違う/比較)。
T4 の字面 (Day8 / 採取項目) は足していない —— それは example 対症になる。
"""
from __future__ import annotations

import re
from dataclasses import dataclass

# ── カード本文から読む形 ────────────────────────────────────────────────
_FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_HIDDEN_LINE_RE = re.compile(r"^- 非表示アクティビティ:\s*(.*)$", re.MULTILINE)
_COND_LINE_RE = re.compile(r"^- 表示条件:\s*(.*)$", re.MULTILINE)
# 「値なし」の書き方。カード生成側は em dash を使うが、`-` / 空 も同義として呑む。
_EMPTY_TOKENS = {"", "—", "-", "ー", "なし"}
# 「式がカードに載っていない」の 2 通りの綴り (P1 §3)。空白を除いてから照合するのは、
# 生成側が括弧前の半角空白を落としても判定が変わらないようにするため。
_ADVANCED_MARKERS = ("条件あり(式は別ソース)", "非表示条件あり")
_WS_RE = re.compile(r"\s+")


@dataclass(frozen=True)
class CardFacts:
    """1 枚の EDC 項目カードから、触発判定と選頁に要る 4 つだけを抜いたもの。"""

    form_oid: str
    item_oid: str
    hidden_activities: frozenset[str]
    has_advanced_condition: bool
    # このカードが study 直查 (S2) 経由で来たか。**カード本文からは読めない** chunk 側の
    # 事実なので既定は False = 「保証なし」。R3 の関連性フロア (M10) だけがこれを見る。
    via_lookup: bool = False

    @classmethod
    def from_text(cls, text: str, *, via_lookup: bool = False) -> CardFacts | None:
        """field card なら CardFacts, それ以外 (手順書章節 / CDISC chunk) なら None。

        ⛔ None を「空のカード」に丸めないこと: 手順書 chunk が「非表示アクティビティ
        0 件のカード」として静かに数に入ると、R3 (カード集合が非空なら発火) が
        study 側の実カードゼロでも発火する。
        """
        m = _FM_RE.search(text)
        if not m:
            return None
        fm = {}
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        if fm.get("doc_type") != "field_card":
            return None
        form_oid, item_oid = fm.get("form_oid", ""), fm.get("field_oid", "")
        if not form_oid or not item_oid:
            return None
        body = text[m.end():]
        hidden: set[str] = set()
        hm = _HIDDEN_LINE_RE.search(body)
        if hm:
            for part in hm.group(1).split(","):
                tok = part.strip()
                if tok not in _EMPTY_TOKENS:
                    hidden.add(tok)
        cm = _COND_LINE_RE.search(body)
        cond = _WS_RE.sub("", cm.group(1)) if cm else ""
        return cls(form_oid=form_oid, item_oid=item_oid,
                   hidden_activities=frozenset(hidden),
                   has_advanced_condition=any(m2 in cond for m2 in _ADVANCED_MARKERS),
                   via_lookup=via_lookup)


def parse_cards(texts: list[str]) -> list[CardFacts]:
    out = [CardFacts.from_text(t) for t in texts]
    return [c for c in out if c is not None]


def parse_chunks(chunks) -> list[CardFacts]:
    """検索結果の chunk から。本文に無い `via_lookup` (S2 直查で union-add されたか)
    を一緒に運ぶのが `parse_cards` との唯一の差 —— R3 のフロア (M10) がそれを要る。"""
    out = [CardFacts.from_text(c.text, via_lookup=bool(getattr(c, "via_lookup", False)))
           for c in chunks]
    return [c for c in out if c is not None]


# ── 語彙表 (P1 §3) ─────────────────────────────────────────────────────
# 部分文字列照合。日本語に語境界は無く、ここで拾いたいのは「時点/表示について訊いて
# いる」という粗い信号なので、形態素解析を持ち込む価値は無い (誤触のコストは
# 「無関係な画像が 6 枚付く」であって、誤答ではない)。
_R1_WORDS = (
    # P1 §3 の原文
    "visit", "時点", "いつ", "表示", "出る", "每次", "只录一次", "显示",
    # 実装時の追加 (module docstring の逸脱 1 件): 差異・比較・時点のクラス
    # + 「出る」の活用形。P1 §3 に登記した一覧と**逐字一致**させること —— doc と code の
    # 食い違いは「登記した判据と実際の判定が違う」という最も気付きにくい形の嘘になる。
    "違い", "違う", "比較", "タイミング", "毎回", "出ます",
)
_R2_WORDS = ("条件", "いつ", "どんな時", "显示", "表示")
_R3_WORDS = ("画面", "レイアウト", "並び", "並ん", "布局", "排列")


@dataclass(frozen=True)
class TriggerDecision:
    fire: bool
    rule: str | None
    reason: str


_NO = TriggerDecision(False, None, "no rule matched")


def _hit(question: str, words: tuple[str, ...]) -> str | None:
    lowered = question.lower()   # "visit" は英字なので大小文字を吸収 (和語には無害)
    return next((w for w in words if w in lowered), None)


def should_attach_pdf(question: str, cards: list[CardFacts], *,
                      study_strong_hit: bool = False,
                      study_form_named: bool = False) -> TriggerDecision:
    """P1 §3 の 3 規則。順に見て**最初に**当たったものを返す (規則名は観測用に出す)。

    カード集合が空なら常に不発 —— 付けるページを決める鍵 (form/item OID) が
    どこにも無い状態で、語だけを根拠に画像を付けるのは当て推量になる。

    R3 の関連性フロア (M10 + 予登記 r3) は 3 つの or —— corpus=both では study 側が
    **類似度の閾値なしに**配額で埋まるため、CDISC 寄りの問いに 画面/並び が入っている
    だけで、たまたま混じった 1 枚のカードで R3 が発火してしまう:
      (a) 直查 (S2) 経由で来たカードが 1 枚でも在る (`CardFacts.via_lookup`)
      (b) `study_strong_hit` = 問い自体が直查の強通道に当たった (`StudyLookup.strong_hit`)
      (c) `study_form_named` = 問いが study のフォームを名指しした
    (c) は V3 attempt 1 で T6 (純粋な画面レイアウト問い) が (a)(b) のどちらも満たさず
    不発だったのを受けた改訂 (`evidence/failures/c2r_v3_attempt_1_T6.md`)。

    (c) の値は接線 (`server/router.py::maybe_attach_pdf_pages`) が 2 経路の or で作る:
      主 = **頁索引の名前表** `PdfPageIndex.form_named_in` (r3b) —— form OID は境界照合、
           form 名は 4 字以上の部分文字列。ここが T6 型を通す実質の経路。
      副 = `StudyLookup.resolve(question).form_scopes` 非空。⚠ これを埋めるのは
           **手書き別名表** (`lookup_aliases.yml`, 通道 ③) だけで、catalog のフォーム名や
           form OID を問いから拾う経路は `resolve` に無い。実データの別名表は 1 件しか
           なく、attempt 1 の T6 はまさにここで落ちた —— 副経路だけに頼らないこと。
    本関数は bool を受け取るだけで、どちらの経路で立ったかは知らない (判定材料が
    索引と別名表に散っているので、純粋関数の外で合流させる)。

    R1/R2 にフロアが要らないのは、あちらの証拠がカードの**中身** (非表示名簿 /
    式が別ソース) であって、カードが在ることそのものではないから。
    """
    if not cards:
        return TriggerDecision(False, None, "no study cards retrieved")
    hidden = set().union(*(c.hidden_activities for c in cards))
    if len(hidden) >= 2:
        w = _hit(question, _R1_WORDS)
        if w:
            shown = ", ".join(sorted(hidden)[:4])
            return TriggerDecision(
                True, "R1",
                f"R1: 非表示アクティビティ {len(hidden)} 件 ({shown}...) × 時点/表示語 {w!r}")
    advanced = [c for c in cards if c.has_advanced_condition]
    if advanced:
        w = _hit(question, _R2_WORDS)
        if w:
            return TriggerDecision(
                True, "R2",
                f"R2: 式が別ソースのカード {len(advanced)} 枚 "
                f"({advanced[0].form_oid}.{advanced[0].item_oid}...) × 条件語 {w!r}")
    w = _hit(question, _R3_WORDS)
    if w:
        vouched = [c for c in cards if c.via_lookup]
        if not (vouched or study_strong_hit or study_form_named):
            return TriggerDecision(
                False, None,
                f"R3 の語 {w!r} は当たったが、関連性フロア未達 (直查経由のカード 0 枚 / "
                f"問いが強通道に当たらない / 問いが study のフォームを名指ししていない)")
        if vouched:
            why = f"直查カード {len(vouched)} 枚"
        elif study_strong_hit:
            why = "問いが直查の強通道に命中"
        else:
            why = "問いが study のフォームを名指し"
        return TriggerDecision(
            True, "R3", f"R3: 画面/レイアウト語 {w!r} × カード {len(cards)} 枚 ({why})")
    return _NO
