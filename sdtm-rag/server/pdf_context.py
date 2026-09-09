"""I2-2: 画面 PDF の按需旁路 — OID 集合 → 頁集合 → 画像 → 多模態片段。

C2 の DROP 判定 (`evidence/checkpoints/c2_pre_survey.md` §8) は動かさない: この 2 つの
PDF はベクトル庫に**入らない**。ここは検索の外側で、**既に当たったカードの OID を鍵に**
確定的に頁を選び、その頁だけを画像として答題文脈に足す通道。鍵は catalog 由来であって、
モデルに「何を検索するか」を決めさせない (PLAN_c2r_pdf_bypass.md §2)。

選頁の規則 (S0 §1-2/§1-4 の実測に基づく):
1. annotated は **item OID 直查** (941/959, 中位 1 頁)。当たらなければ form ブロック先頭頁。
   item OID の徽章が写っている頁が画面↔DB の橋渡しなので、ここが最優先。
2. workflow は **(activity, form) ブロック**。同じ form の複数 activity が作る画面は
   実データでは大幅に重複する (LB: 18 activity → 画面 5 種) ので、`hidden_items` が同一の
   ブロックは**同じ画面**とみなして 1 枚しか付けない。
3. 順位は ①問題文が名指しした activity ②取得済み項目が**表示されている**画面
   ③それ以外。②が③より上なのは、全項目が隠れている画面はカードが既にそう言っており、
   画像を 1 枚使う価値が最も低いから。
4. annotated が予算を食い尽くさないよう半分は workflow に取り置く —— R1 (活動をまたぐ
   表示) の答えは workflow 側にしかなく、カードが 6 枚当たった瞬間に 0 枚では意味が無い。

⚠ P1/I2 仕様からの逸脱 1 件 (意図的): 仕様は workflow の候補を「カードの
非表示アクティビティ ∪ 問題文の activity」と書いていたが、ここは**そのフォームの
全ブロック**を候補にしている。非表示リストは「その項目が出ない活動」しか指せず、
一番知りたい「出ている活動の画面」(dogfood の LB p.315 がまさにそれ) を構造的に
指せないため。非表示リストは全ブロックの部分集合なので、候補は狭まっていない。
"""
from __future__ import annotations

import base64
import hashlib
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

import structlog

# 境界照合は study_lookup が**唯一の定義**を持つ (`_bounded_re`)。同じ正規表現を
# ここにもう一度書くと境界の意味が 2 つになり、片方だけ締めた時の症状が無症状になる。
# `_norm_ws` も一緒に借りる: 問題文の全角 `Ａ＿ＯＮＥ` は NFKC を通さないと当たらず、
# 「OID を書いたのに 1 頁も付かない」という静かな取りこぼしになる (空白は保つ ——
# 理由は `_norm_ws` の docstring)。private 名を跨いで使うのは行儀が悪いが、
# 「定義は 1 つ」の方が優先 (team lead 2026-09-09 の指示)。
from server.study_lookup import _bounded_re, _norm_ws

log = structlog.get_logger()

PDF_KEYS = ("annotated", "workflow")
_PDFTOPPM = "pdftoppm"
# 日本語の活動名でページを名指しできる最短長。日本語に語境界は無いので裸の部分文字列
# 照合になり、短い名前ほど地の文に偶然現れる。4 は study_lookup の `_MIN_LABEL_LEN` と
# 同値 —— あちらと同じ天秤 (S0 §2-2: 名前の部分文字列照合は交差参照ページまで拾う)。
# ⚠ 誤爆の代償はここでは軽い: 既に選ばれた form のブロック内で**順位**が上がるだけで、
# 検索結果も答えの出典も動かない。だから study_lookup が名前索引ごと捨てた判断
# (C3, 假陽性の 83%) をここにそのまま持ち込まず、長さの下限だけ借りる。
_MIN_ACTIVITY_NAME_LEN = 4
# 問いが study の**フォーム**を名指ししたかの判定 (予登記 r3b, R3 の関連性フロア (c))。
# 名前側の下限は活動名と同じ 4 —— 実データの form 名には 2-3 字のものがあり、それを
# 裸の部分文字列で見ると日本語の地の文に偶然当たる。form OID 側は境界照合なので
# 下限を掛けない (2 字の OID でも、それを接頭に持つ長い OID の中には当たらない)。
_MIN_FORM_NAME_LEN = 4


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


@dataclass(frozen=True)
class PdfContextStatus:
    available: bool
    reason: str = ""

    @classmethod
    def ok(cls) -> PdfContextStatus:
        return cls(True, "")

    @classmethod
    def unavailable(cls, reason: str) -> PdfContextStatus:
        return cls(False, reason)


@dataclass(frozen=True)
class PageRef:
    pdf: str          # "annotated" | "workflow"
    page: int
    label: str        # 文脈に出す見出し (人が読む名前入り)
    reason: str       # なぜ選ばれたか (観測用; done 事件には載せない)
    activity_oid: str = ""            # workflow 頁のみ


@dataclass(frozen=True)
class PageSelection:
    pages: tuple[PageRef, ...]
    omitted: tuple[PageRef, ...]       # 頁予算で落ちた候補 (上限を上げれば出てくる)
    truncated: bool
    # 同一画面として畳んだブロック。**omitted とは別枠**: 上限を上げても出てこないので、
    # 混ぜると「予算さえ増やせば見られる」と読めてしまう。折り畳んだ事実自体は
    # 生き残った頁の label に書く (「同一画面: …」)。
    folded: tuple[PageRef, ...] = ()
    max_pages: int = 0                 # そのとき効いていた設定値 (降級案内が使う)


@dataclass(frozen=True)
class ImagePart:
    pdf: str
    page: int
    label: str
    b64: str


class PdfPageIndex:
    """`scripts/study/build_pdf_page_index.py` の出力を読むだけの薄い包み。"""

    def __init__(self, data: dict):
        # 形の自己検証。S0 の勘察草案 (`survey_pdf_pages.py` の出力) は同じ拡張子で
        # ブロックが**リストのリスト**なので、素通しすると最初の添字アクセスで
        # `TypeError: list indices must be integers` という原因の読めない例外になる。
        # 実際に一度、勘察スクリプトの再実行が生産索引を上書きしてこれを踏んだ。
        if data.get("meta", {}).get("draft"):
            raise ValueError(
                "これは S0 勘察の**草案**索引です (meta.draft=true)。生産索引は "
                "`uv run python scripts/study/build_pdf_page_index.py` で作り直すこと")
        blocks = data.get("workflow", {}).get("blocks")
        if not isinstance(blocks, list) or (blocks and not isinstance(blocks[0], dict)):
            raise ValueError("pdf_page_index: workflow.blocks が dict のリストではない")
        self._d = data
        self._wf_by_form: dict[str, list[dict]] = {}
        for b in data["workflow"]["blocks"]:
            self._wf_by_form.setdefault(b["form_oid"], []).append(b)
        for blocks in self._wf_by_form.values():
            blocks.sort(key=lambda b: b["start"])
        self._form_block: dict[str, dict] = {}
        for b in data["annotated"]["blocks"]:
            if b["kind"] == "form":
                self._form_block.setdefault(b["form_oid"], b)
        self._names = data.get("names", {})
        # 表示名は `イベント名 › アクティビティ名`。問題文が含むのは普通アクティビティ名
        # だけなので、照合用に後半を切り出しておく (イベント名側は広すぎて、それで
        # 名指しと見なすとイベント配下の全活動が上位に来てしまう)。
        self._activity_short = {oid: name.split("›")[-1].strip()
                                for oid, name in self._names.get("activities", {}).items()}
        self.activity_oids = frozenset(b["activity_oid"] for b in data["workflow"]["blocks"])

    @classmethod
    def load(cls, path: Path | str) -> PdfPageIndex:
        import json
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    def sha(self, pdf_key: str) -> str:
        return self._d["meta"]["pdfs"][pdf_key]["sha256"]

    def item_pages(self, form_oid: str, item_oid: str) -> list[int]:
        return list(self._d["annotated"]["item_pages"].get(form_oid, {}).get(item_oid, []))

    def form_block(self, form_oid: str) -> dict | None:
        return self._form_block.get(form_oid)

    def workflow_blocks(self, form_oid: str) -> list[dict]:
        return self._wf_by_form.get(form_oid, [])

    def form_name(self, oid: str) -> str:
        return self._names.get("forms", {}).get(oid, oid)

    def activity_name(self, oid: str) -> str:
        return self._names.get("activities", {}).get(oid, oid)

    def activity_short_name(self, oid: str) -> str:
        """イベント名を落としたアクティビティ名 (照合用 / 折り畳み表示用)。"""
        return self._activity_short.get(oid, oid)

    def form_named_in(self, question: str) -> str | None:
        """問いが名指しした form の OID (無ければ None) —— R3 のフロア (c) の判定 (r3b)。

        なぜ `StudyLookup.resolve().form_scopes` では埋まらないのか: あちらを埋めるのは
        **手書き別名表だけ** (通道 ③) で、catalog の form 名や form OID を問いから拾う
        経路が無い。実データの別名表は 1 件しか無く、V3 attempt 1 の T6 (フォームを
        日本語名と OID の両方で名指しした純粋な画面レイアウト問い) がそこで落ちた
        (`evidence/failures/c2r_v3_attempt_1_T6.md`)。

        判定材料は**頁索引の名前表**。ここで完結させる利点は 2 つ: ① 別名表を触らない
        ので検索が 1 件も動かない (`form_scopes` は `_apply_study_lookup` の注入に効く)
        ② 凍結中の study_lookup.py に手を入れない。
        """
        q = _norm_ws(question)
        forms = self._names.get("forms", {})
        for oid in sorted(forms):
            if _bounded_re(oid).search(q):
                return oid
        # 長い名前を先に見る: 短い名前が長い名前の一部という catalog は普通に在り、
        # 先に短い方を返すと「どのフォームを訊かれたか」が名前の長さで揺れる。
        for oid, name in sorted(forms.items(), key=lambda kv: -len(kv[1])):
            if len(name) >= _MIN_FORM_NAME_LEN and _norm_ws(name) in q:
                return oid
        return None


class PdfContextBuilder:
    def __init__(self, index: PdfPageIndex, pdf_paths: dict[str, Path], *,
                 max_pages: int = 6, dpi: int = 110, cache_dir: Path):
        self.index = index
        self.pdf_paths = {k: Path(v) for k, v in pdf_paths.items()}
        self.max_pages = max_pages
        self.dpi = dpi
        self.cache_dir = Path(cache_dir)
        self.status = self._probe()
        self._warned = False
        self._warned_budget = False

    def _probe(self) -> PdfContextStatus:
        if shutil.which(_PDFTOPPM) is None:
            return PdfContextStatus.unavailable(
                f"{_PDFTOPPM} not found — 画面を画像にできない (macOS: brew install poppler)")
        for key in PDF_KEYS:
            p = self.pdf_paths.get(key)
            if p is None or not p.is_file():
                return PdfContextStatus.unavailable(f"{key} pdf not found: {p}")
            # 索引は「どの PDF の何頁か」しか言えない。PDF が版更新で差し替わると同じ
            # 頁番号が別の画面を指し、答えは**出典付きで堂々と間違う** —— 索引欠落より
            # 悪い (あちらは頁が付かないだけ)。sha を meta に書いておいて照合しないのは、
            # 鍵を作って鍵穴を作らないのと同じ。13 MB の読み直しは起動 1 回だけ。
            got = _sha256(p)
            want = self.index.sha(key)
            if got != want:
                return PdfContextStatus.unavailable(
                    f"{key} pdf sha256 mismatch: index={want[:12]}… file={got[:12]}… "
                    f"({p}) — 索引を作り直す: scripts/study/build_pdf_page_index.py")
        return PdfContextStatus.ok()

    # ── 選頁 ───────────────────────────────────────────────────────────
    def select_pages(self, cards, question: str = "",
                     max_pages: int | None = None) -> PageSelection:
        cap = self.max_pages if max_pages is None else max_pages
        ann = self._annotated_candidates(cards)
        wf, folded = self._workflow_candidates(cards, question)
        if cap <= 0:
            # 上限 0 は「実質 OFF」。max(1, …) の丸めで 1 枚通すと、切ったつもりの通道が
            # 静かに動き続ける。
            if not self._warned_budget:
                self._warned_budget = True
                log.warning("pdf_context_zero_budget", max_pages=cap)
            return PageSelection(pages=(), omitted=tuple(ann + wf), truncated=bool(ann or wf),
                                 folded=folded, max_pages=cap)
        n_ann = min(len(ann), cap if not wf else max(1, (cap + 1) // 2))
        n_wf = min(len(wf), cap - n_ann)
        n_ann = min(len(ann), cap - n_wf)   # workflow が使い切らなかった枠は annotated に戻す
        pages = tuple(ann[:n_ann] + wf[:n_wf])
        omitted = tuple(ann[n_ann:] + wf[n_wf:])
        return PageSelection(pages=pages, omitted=omitted, truncated=bool(omitted),
                             folded=folded, max_pages=cap)

    def _annotated_candidates(self, cards) -> list[PageRef]:
        out: list[PageRef] = []
        seen: set[int] = set()
        for c in cards:
            pages = self.index.item_pages(c.form_oid, c.item_oid)
            reason = f"item {c.form_oid}.{c.item_oid}"
            if not pages:
                # OID が 1 頁も当たらないフォーム (S0 実測 18/959)。フォーム先頭頁なら
                # 少なくとも「そのフォームの画面」ではある —— 黙って 0 枚にはしない。
                blk = self.index.form_block(c.form_oid)
                if blk is None:
                    continue
                pages, reason = [blk["start"]], f"form block head {c.form_oid}"
            for p in pages:
                if p in seen:
                    continue
                seen.add(p)
                out.append(PageRef("annotated", p, self._ann_label(c.form_oid, p), reason))
        return out

    def _workflow_candidates(self, cards, question: str):
        """候補頁と、同一画面として畳んだブロックを返す。

        名指しの判定は **OID と日本語の活動名の両方**。実際の問いは活動を OID で呼ばない
        (T4/T5, dogfood はどれも日本語名) ので、OID だけ見ていると名指しされた画面が
        折り畳みで黙って落ちる —— それは「両日とも同じ画面か?」という問いの答えそのもの。
        """
        forms: list[str] = []
        items_by_form: dict[str, set[str]] = {}
        for c in cards:
            if c.form_oid not in items_by_form:
                forms.append(c.form_oid)
                items_by_form[c.form_oid] = set()
            items_by_form[c.form_oid].add(c.item_oid)
        asked = self._asked_activities(question)

        rows: list[tuple[int, int, PageRef]] = []
        folded: list[PageRef] = []
        # 画面 (= hidden_items) ごとの代表ブロック。畳んだ活動は代表の label に書き足す
        # ので、代表を確定してから label を作る (2 周目)。
        for form in forms:
            first_of_screen: dict[tuple[str, ...], dict] = {}
            folded_by_screen: dict[tuple[str, ...], list[str]] = {}
            for b in self.index.workflow_blocks(form):
                screen = tuple(sorted(b["hidden_items"]))
                if b["activity_oid"] in asked:
                    continue                      # 名指しは畳まない (下で tier 0)
                if screen in first_of_screen:
                    folded_by_screen.setdefault(screen, []).append(b["activity_oid"])
                    folded.append(PageRef("workflow", b["start"],
                                          self._wf_label(b), "folded into an identical screen",
                                          b["activity_oid"]))
                else:
                    first_of_screen[screen] = b
            for b in self.index.workflow_blocks(form):
                screen = tuple(sorted(b["hidden_items"]))
                shows = sorted(items_by_form[form] - set(b["hidden_items"]))
                if b["activity_oid"] in asked:
                    tier, why = 0, "activity named in question"
                elif first_of_screen.get(screen) is not b:
                    continue                      # 既出画面の複製 (LB 実測 18 中 13)
                elif shows:
                    tier, why = 1, f"shows {', '.join(shows[:3])}"
                else:
                    tier, why = 2, "hides every retrieved item"
                rows.append((tier, b["start"],
                             PageRef("workflow", b["start"],
                                     self._wf_label(b, folded_by_screen.get(screen, [])),
                                     f"{why} ({b['activity_oid']})", b["activity_oid"])))
        rows.sort(key=lambda r: (r[0], r[1]))
        out: list[PageRef] = []
        seen_pages: set[int] = set()
        for _, _, ref in rows:
            if ref.page not in seen_pages:
                seen_pages.add(ref.page)
                out.append(ref)
        return out, tuple(folded)

    def _asked_activities(self, question: str) -> set[str]:
        """問題文が名指しした activity OID の集合 (OID の有界一致 ∪ 日本語名の部分一致)。

        日本語側が境界なしの部分一致なのは、日本語に語境界が無いため —— `_bounded_re` を
        日本語名に使うと「名前の直後が漢字」で不一致になり、ほぼ全滅する。代わりに
        `_MIN_ACTIVITY_NAME_LEN` を下限に置く (定数の所に天秤を書いた)。
        """
        q = _norm_ws(question)
        asked = {a for a in self.index.activity_oids if _bounded_re(a).search(q)}
        for oid in self.index.activity_oids:
            name = _norm_ws(self.index.activity_short_name(oid))
            if len(name) >= _MIN_ACTIVITY_NAME_LEN and name in q:
                asked.add(oid)
        return asked

    def _ann_label(self, form_oid: str, page: int) -> str:
        return (f"【画面 annotated p.{page} — "
                f"{self.index.form_name(form_oid)} ({form_oid}) フォーム画面】")

    def _wf_label(self, b: dict, folded: list[str] | None = None) -> str:
        head = (f"【画面 workflow p.{b['start']} — {self.index.activity_name(b['activity_oid'])}"
                f" / {self.index.form_name(b['form_oid'])} ({b['form_oid']}) の実表示")
        if folded:
            # 「この画面は活動 X/Y でも共通」は答えそのもの (T4 の「両日の違い」)。
            # 予算節約のために消していい情報ではないので、生き残った頁に書き移す。
            # 短縮名ではなく**イベント込みの完全名**。実データでは A 群と B 群が同名の
            # 活動を持つので、短縮名だと「同一画面: 自分と同じ名前」に見えて何も伝わらない
            # —— どの群のどの活動と共通なのかが、まさに T4 型が訊いていること。
            names = ", ".join(self.index.activity_name(a) for a in folded)
            head += f" · 同一画面: {names}"
        return head + "】"

    # ── 描画 ───────────────────────────────────────────────────────────
    def render(self, selection: PageSelection) -> list[ImagePart]:
        """頁 → PNG (base64)。`(pdf sha, 頁, dpi)` でディスクキャッシュ。

        使えない構成では**空リスト**を返す (例外を投げない): 画像が付かないだけで
        答え自体は既存通路で出せるため。ただし黙って消えるのは許さない —— 起動時に
        `status` を、実行時に 1 度だけ warning を出す。
        """
        if not self.status.available:
            if not self._warned:
                self._warned = True
                log.warning("pdf_context_unavailable", reason=self.status.reason)
            return []
        parts: list[ImagePart] = []
        for ref in selection.pages:
            png = self._png(ref.pdf, ref.page)
            if png is None:
                continue
            parts.append(ImagePart(ref.pdf, ref.page, ref.label,
                                   base64.b64encode(png).decode()))
        return parts

    def _png(self, pdf_key: str, page: int) -> bytes | None:
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        stem = self.cache_dir / f"{pdf_key}_{self.index.sha(pdf_key)[:16]}_p{page}_r{self.dpi}"
        out = stem.with_suffix(".png")
        if out.is_file():
            return out.read_bytes()
        # -singlefile: 出力名を `<stem>.png` に確定させる。無いと pdftoppm が頁番号の
        # 桁数でファイル名を変え (`-315.png` / `-0315.png`), 拾う側が glob 頼みになる。
        r = subprocess.run(
            [_PDFTOPPM, "-r", str(self.dpi), "-png", "-singlefile",
             "-f", str(page), "-l", str(page), str(self.pdf_paths[pdf_key]), str(stem)],
            capture_output=True, text=True,
        )
        if r.returncode != 0 or not out.is_file():
            log.warning("pdftoppm_failed", pdf=pdf_key, page=page,
                        stderr=(r.stderr or "")[:200])
            return None
        return out.read_bytes()

    # ── 多模態片段 ─────────────────────────────────────────────────────
    def to_message_parts(self, selection: PageSelection,
                         images: list[ImagePart] | None = None) -> list[dict]:
        """litellm / OpenAI 形式の content parts。1 頁 = 見出しテキスト + 画像。

        形は S0-3 で 4 モデル全部が受け取れることを実測した並び
        (`scripts/study/survey_pdf_pages.py::probe_models`) をそのまま踏襲する。

        `images` を渡せるのは、呼び出し側が「実際に付いた頁」を報告する必要があるため
        (M3): 描画に失敗した頁を「付けた」と報告すると、答えの中の 画面目視判読 p.NN が
        どの頁から来たのか辿れなくなる。省略時はここで描画する。
        """
        imgs = self.render(selection) if images is None else images
        parts: list[dict] = []
        for img in imgs:
            parts.append({"type": "text", "text": img.label})
            parts.append({"type": "image_url",
                          "image_url": {"url": f"data:image/png;base64,{img.b64}"}})
        if not parts:
            return []
        # 見ていない頁は 2 種類ある: 予算で落ちた頁と、描画に失敗した頁。モデルから見れば
        # どちらも同じ「見ていない」で、黙っていると「これで全部」と思って断定する。
        attached = {(i.pdf, i.page) for i in imgs}
        unseen = [*selection.omitted,
                  *(p for p in selection.pages if (p.pdf, p.page) not in attached)]
        if unseen:
            listed = "、".join(f"{p.pdf} p.{p.page}" for p in unseen[:8])
            more = "…" if len(unseen) > 8 else ""
            parts.append({"type": "text",
                          "text": f"（他 {len(unseen)} ページ未添付: {listed}{more}"
                                  f" — ページ上限 {selection.max_pages}）"})
        return parts
