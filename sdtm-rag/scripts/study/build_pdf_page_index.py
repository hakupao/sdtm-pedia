"""I2-1: 画面 PDF の確定的ページ索引 (PLAN_c2r_pdf_bypass.md §4, 零 LLM)。

S0 勘察 (`survey_pdf_pages.py`) の切块ロジックを生産形に収束させたもの。勘察との差:

- 出力が**ブロック表 2 枚 + item→頁 1 枚**だけ (草案は全実体の逐頁命中表で 1.16 MB)。
- 名称ではなく **OID** を書く (catalog の assignments 経由)。名前は表示用であって鍵ではない。
- 「黙って間違ったページを返す」を全部**響く失敗**に変えた: 題名が catalog に無い form を
  指す / assignments に無い組合せを指す / 同名 activity が 2 つの OID を指す → ValueError。
  ブロック数・被覆頁数・form ブロック数の 3 本は `check_index` が非零終了で落とす。

子プロセスを起こすのは `scripts/study/pdf_text.py` ただ一箇所 (split_sections.py と同じ
纪律)。本モジュールの切块関数は `list[str]` (頁本文) しか見ないので、合成 fixture で
完全にテストできる。

復跑:
    uv run python scripts/study/build_pdf_page_index.py            # st01, 既定の出力先
    uv run python scripts/study/build_pdf_page_index.py --no-cache # 頁本文キャッシュを使わない
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scripts.study.paths import resolve_study  # noqa: E402
from scripts.study.pdf_text import extract_pages  # noqa: E402

# 境界照合は server/study_lookup.py が唯一の定義を持つ。2 文字 OID を裸の部分文字列で
# 探すと、それで始まる長い OID の中にまで当たって定位率が偽って 100% 近くになる
# (S0 §2-1 の自己修正)。同じ正規表現をここに書き直さない —— 片方だけ締めた時の症状は
# 「索引が静かに違うページを指す」で、赤くならない。
# ⚠ 頁本文には NFKC を掛けない: 抽出口径 (meta.extraction_command) を変えると索引の
# 数字が S0 実測と比較できなくなる。画面の OID 徽章は元々半角 ASCII。
from server.study_lookup import _bounded_re  # noqa: E402

# 両 PDF の全頁 (1,145/1,145) が持つ頁眉。版番号は緩く取る —— 59.0 を焼き込むと、
# 版が上がった瞬間に「一つもブロックが取れない索引」が**静かに**出来上がる。
_HEADER_RE = re.compile(r"^ENSEMBLE \| ENSEMBLE \[[0-9.]+\]\s*")
_WS_RE = re.compile(r"\s+")
_CODELIST_SUFFIX = " - Code Lists"

# 画面の OID 徽章は半角 ASCII の**独立した列**に描かれ、日本語に食い込まない。
# `_bounded_re` の境界は ASCII 英数のみを見るので、日本語 (と全角) の直前直後は
# 境界として通ってしまう —— 2 字 OID が隣の頁の日本語見出しの頭と一致して、その頁に
# 居ることにされる (複審の実例: 1 頁分の過剰計上 + 別 1 件は定位そのものが誤り)。
# 実測での天秤 (annotated 942 対): この規則で落ちるのは 2 対だけで、残り 940 対は
# すべて非 ASCII に隣接しない出現を持つ。列位置まで要求する案 (行端 or 2 空白以上) は
# 54 対落とし、うち 52 対は 1 空白字下げの**真の徽章** —— だから採らない。
_NON_ASCII_RE = re.compile(r"[^\x00-\x7f]")

# workflow の被覆断言の許容外れ頁数。S0 実測では表紙 + 目次の 3 頁 (933 → 930) だけが
# どのブロックにも属さない。定数で持つのは「930」という study 固有の数を焼かないため。
MAX_UNCOVERED_PAGES = 3


def norm_page(text: str) -> str:
    """頁本文を 1 行に潰す。`-layout` は日本語の連なりを空白で割るので、題名照合の前に
    空白を単一化しておく (勘察の norm_ws と同じ口径)。"""
    return _WS_RE.sub(" ", text).strip()


def strip_header(page: str) -> str:
    return _HEADER_RE.sub("", page, count=1)


def _blocks_from_titles(titled: dict[int, dict], n_pages: int) -> list[dict]:
    """題名頁 → ブロック。終端は**次の題名頁の 1 つ前** (前方埋め)。

    題名を持つ頁は全体の 12-20% しかなく、残りは継続頁 —— 「頁ごとに身元を判定」は
    成立せず「ブロックごとに判定」だけが成立する (S0 §2-1)。
    """
    starts = sorted(titled)
    out = []
    for i, st in enumerate(starts):
        end = starts[i + 1] - 1 if i + 1 < len(starts) else n_pages
        out.append({"start": st, "end": end, **titled[st]})
    return out


def cut_workflow_blocks(catalog: dict, pages: list[str]) -> list[dict]:
    """workflow PDF を `(event, activity, form)` ブロックに切る。

    題名行は `<event名> / <activity名> <form名>`。名前から OID への変換は
    `assignments` が唯一の出所 —— 表示名で索引を作ると、消費側 (server/pdf_context.py)
    が OID しか持っていないので毎回名前に訳し直す必要があり、その訳が 2 箇所に散る。
    """
    pair_to_activity: dict[tuple[str, str], set[tuple[str, str]]] = {}
    for a in catalog["assignments"]:
        key = (a["event_name"], a["activity_name"])
        pair_to_activity.setdefault(key, set()).add((a["event_oid"], a["activity_oid"]))
    form_oid_by_name = {f["name"]: f["oid"] for f in catalog["forms"]}
    # 三つ組 → その assignment の hidden_items。ブロックに焼き込むのは「このページ範囲は
    # どの画面か」を消費側が判別できるようにするため —— LB 実測では 18 個の activity が
    # 作る画面は 5 種類しかなく (残り 13 個は既出画面の複製), 区別する材料は catalog の
    # この欄にしか無い。server 側に catalog を持ち込む代わりにここで一度だけ写す。
    hidden_by_triple = {
        (a["event_oid"], a["activity_oid"], a["form_oid"]):
            [x.strip() for x in (a.get("hidden_items") or "").split(",") if x.strip()]
        for a in catalog["assignments"]
    }
    # 長い順: `活動一` と `活動一 甲` の両方が前置一致し得るとき、短い方に食わせない。
    pairs = sorted(pair_to_activity, key=lambda x: -(len(x[0]) + len(x[1])))
    form_names = sorted(form_oid_by_name, key=len, reverse=True)

    titled: dict[int, dict] = {}
    for i, raw in enumerate(pages, 1):
        t = strip_header(norm_page(raw))
        hit = next((p for p in pairs if t.startswith(f"{p[0]} / {p[1]} ")), None)
        if hit is None:
            continue  # 継続頁 (または表紙/目次) —— 題名が無いのは正常
        acts = pair_to_activity[hit]
        if len(acts) > 1:
            raise ValueError(
                f"page {i}: ambiguous title {hit!r} maps to {len(acts)} activities "
                f"{sorted(acts)} — catalog に同名 activity が複数ある"
            )
        (event_oid, activity_oid), = acts
        rest = t[len(f"{hit[0]} / {hit[1]} "):]
        fname = next((f for f in form_names if rest.startswith(f)), None)
        if fname is None:
            raise ValueError(
                f"page {i}: title {hit!r} followed by unknown form name: {rest[:60]!r}"
            )
        form_oid = form_oid_by_name[fname]
        if (event_oid, activity_oid, form_oid) not in hidden_by_triple:
            raise ValueError(
                f"page {i}: ({event_oid}, {activity_oid}, {form_oid}) is not a catalog "
                f"assignment — PDF と ConfigReport の版が食い違っている疑い"
            )
        titled[i] = {"event_oid": event_oid, "activity_oid": activity_oid,
                     "form_oid": form_oid,
                     "hidden_items": hidden_by_triple[(event_oid, activity_oid, form_oid)]}
    return _blocks_from_titles(titled, len(pages))


def cut_annotated_blocks(catalog: dict, pages: list[str]) -> list[dict]:
    """Annotated PDF を form ブロックと code-list ブロックに切る。

    題名行は `<form名> <form_oid>` か `<form名> - Code Lists`。form ブロックが「画面」で、
    code-list ブロックは符号表 —— 画面判読の出典として使えるのは前者だけ。
    """
    forms = sorted(catalog["forms"], key=lambda f: -len(f["name"]))
    titled: dict[int, dict] = {}
    for i, raw in enumerate(pages, 1):
        t = strip_header(norm_page(raw))
        for f in forms:
            if t.startswith(f"{f['name']} {f['oid']} ") or t == f"{f['name']} {f['oid']}":
                titled[i] = {"kind": "form", "form_oid": f["oid"]}
                break
            if t.startswith(f["name"] + _CODELIST_SUFFIX):
                titled[i] = {"kind": "codelist", "form_oid": f["oid"]}
                break
    return _blocks_from_titles(titled, len(pages))


def _is_badge_hit(text: str, m: re.Match) -> bool:
    """その一致が**徽章**か (日本語見出しに食い込んだ頭ではないか)。

    両隣を見るだけ: 非 ASCII が直に接していたら、それは日本語の語の一部であって
    徽章ではない。改行は `norm_page` で空白になっているので、行末の徽章は落ちない。
    """
    return not (_NON_ASCII_RE.match(text[m.end():m.end() + 1] or " ")
                or _NON_ASCII_RE.match(text[max(0, m.start() - 1):m.start()] or " "))


def item_pages_by_form(catalog: dict, annotated_blocks: list[dict],
                       pages: list[str]) -> dict[str, dict[str, list[int]]]:
    """`{form_oid: {item_oid: [頁...]}}` —— Annotated の item OID 直查 (941/959, 中位 1 頁)。

    一致は**徽章の形**でなければ数えない (`_is_badge_hit`) —— 範囲を切っても、同じ
    ブロックの隣の頁の日本語見出しの頭と 2 字 OID が一致する経路が残る。

    探索範囲を**その form の form ブロック内**に限るのが短 OID 串味防止の本体 (S0 §1-3):
    `PS` は 6 頁に出るが、そのうち `LB` の画面は 1 頁だけ。範囲を切らずに拾うと、LB の
    `PS` が別フォームの頁を指し、「画面 p.NN」という出典ごと嘘になる。code-list ブロックを
    外すのも同じ理由 —— あれは画面ではない。
    """
    form_pages: dict[str, list[int]] = {}
    for b in annotated_blocks:
        if b["kind"] == "form":
            form_pages.setdefault(b["form_oid"], []).extend(range(b["start"], b["end"] + 1))
    items_by_form: dict[str, list[str]] = {}
    for it in catalog["items"]:
        oids = items_by_form.setdefault(it["form_oid"], [])
        if it["item_oid"] not in oids:
            oids.append(it["item_oid"])
    out: dict[str, dict[str, list[int]]] = {}
    for form_oid, pgs in form_pages.items():
        texts = {p: norm_page(pages[p - 1]) for p in pgs}
        hits: dict[str, list[int]] = {}
        for oid in items_by_form.get(form_oid, []):
            rx = _bounded_re(oid)
            found = [p for p in pgs
                     if any(_is_badge_hit(texts[p], m) for m in rx.finditer(texts[p]))]
            if found:  # 空リストは載せない: 「探してゼロ」と「探していない」が混ざる
                hits[oid] = found
        out[form_oid] = hits
    return out


def page_groups_by_form(
    catalog: dict, item_pages: dict[str, dict[str, list[int]]],
) -> dict[str, dict[str, list[dict]]]:
    """`{form_oid: {"頁": [{group_oid, name, n_items, continued, continues}, ...]}}` —— 本頁に項目が
    在る catalog グループの並び (N3)。

    なぜ索引に要るのか: 画面の枠 (パネル) の境界は catalog の項目グループ境界と逐字
    一致するのに、**見出しの無い枠**は画像から見ると前の枠の続きに見える。V3/N1 では
    2 モデルとも無題パネルを前のパネルに併合した (PLAN §8 (a))。並びを確定的に持って
    おけば、消費側が label に書いて観測可能にできる。

    並び順は catalog の `row` —— 配列順ではない。実データの 21 フォームでグループは
    row について連続 (実測 0 件の非連続) なので、頁内の視覚的な上下と一致する。

    `n_items` は**その頁で定位できた**項目数であって、グループ全体の項目数ではない。
    グループ総数を書くと「添付頁に無い項目まで本頁に在る」と読め、N1 で塞いだ外推を
    索引側で作り直すことになる。

    `continued` は「このグループの項目が**前の頁**にも定位している」= 本頁は枠の途中。
    `continues` (N4) はその対: 「**後の頁**にも定位している」= 枠は本頁で閉じない。
    1 枠だけの頁は N3 では並びを書かないので label が沈黙し、モデルは閉じているか
    どうかを視覚で推測した (実データ p.161: 上辺は閉じ、次頁へ続く)。両方向を持てば、
    消費側は沈黙の代わりに状態を宣言できる。
    label の語は「**次頁**へ続く」だが、欄の意味は「後のいずれかの頁にも在る」。両者が
    一致するのはグループの頁区間が連続しているときだけ (実測 28 件全部が隣接頁、
    非連続 0 件) なので、非連続が現れたら黙って嘘を書く前に落とす。
    ⚠ これは**意図した選択** (複審 MINOR-F): 非連続の最も有り得る原因は定位漏れで、その
    とき枠は物理的には連続しており「次頁へ続く: あり」は本当は正しい。それでも索引全体を
    建てない方を選んだ —— 嘘を 1 件書くより通路が止まる方が見つかりやすい。代替案は
    そのグループだけ `continues` を落として消費側の次元降級に乗せること。
    実測: 発火対象 40 頁のうち 10 頁は先頭の枠が前頁からの続きで、続き頁に見出しが
    描画されている例は名前付き 25 件中 **0 件**。並びだけ渡して続きだと言わないと、
    モデルは前頁にしか無い見出しを「本頁に在る」と報告する —— N2 が拾った
    LABEL 型捏造の新しい面 (複審 MAJOR-1)。

    頁を**文字列**キーで持つのは JSON の往復で形が変わらないようにするため。int で
    組むと、生成直後のテストは通るのに読み直した索引では 1 件も当たらない。
    """
    meta: dict[tuple[str, str], tuple[str, str, int]] = {}
    for it in catalog["items"]:
        meta.setdefault((it["form_oid"], it["item_oid"]),
                        (it["group_oid"], it.get("group_name") or "", it["row"]))
    out: dict[str, dict[str, list[dict]]] = {}
    for form_oid, items in item_pages.items():
        per_page: dict[int, dict[str, dict]] = {}
        first_page: dict[str, int] = {}      # グループが最初に現れた頁 (continued の基準)
        last_page: dict[str, int] = {}       # 最後に現れた頁 (continues の基準)
        for item_oid, pgs in items.items():
            key = meta.get((form_oid, item_oid))
            if key is None:
                # item_pages は catalog から作るので、ここに来るのは入力が食い違って
                # いる時だけ。黙って飛ばすとその頁の注記だけが消える無症状の壊れ方。
                raise ValueError(
                    f"{form_oid}.{item_oid} is not a catalog item —— item_pages と "
                    f"catalog が食い違っている")
            group_oid, name, row = key
            for p in pgs:
                g = per_page.setdefault(p, {}).setdefault(
                    group_oid, {"group_oid": group_oid, "name": name, "row": row, "n": 0})
                g["n"] += 1
                g["row"] = min(g["row"], row)
                first_page[group_oid] = min(first_page.get(group_oid, p), p)
                last_page[group_oid] = max(last_page.get(group_oid, p), p)
        pages_of: dict[str, list[int]] = {}
        for p, groups in per_page.items():
            for oid in groups:
                pages_of.setdefault(oid, []).append(p)
        for oid, pgs in pages_of.items():
            pgs.sort()
            if pgs != list(range(pgs[0], pgs[-1] + 1)):
                raise ValueError(
                    f"{form_oid}.{oid} は頁 {pgs} に飛び飛びに在る —— 『次頁へ続く』が"
                    f"嘘になる (N4 の前提: グループの頁区間は連続)")
        out[form_oid] = {
            str(p): [{"group_oid": g["group_oid"], "name": g["name"], "n_items": g["n"],
                      "continued": first_page[g["group_oid"]] < p,
                      "continues": last_page[g["group_oid"]] > p}
                     for g in sorted(groups.values(), key=lambda g: g["row"])]
            for p, groups in sorted(per_page.items())
        }
    return out


def display_names(catalog: dict) -> dict[str, dict[str, str]]:
    """表示専用の名前表 (OID → 人が読む名前)。索引の鍵は OID だけ、名前はページ見出し
    (`【画面 workflow p.NN — イベント名 › アクティビティ名 / フォーム名】`) を組むためだけに使う。

    ここに持つのは、答題時に catalog.json (3.7 MB) を開かずに済ませるため —— 索引は
    catalog と同時に再生成されるので、名前が catalog と食い違う窓は構造的に無い。
    activity は L1 のグロッサリと同じ `イベント名 › アクティビティ名` 形式に揃える。
    """
    acts = {}
    for a in catalog.get("activities", []):
        ev = a.get("event_name")
        acts[a["oid"]] = f"{ev} › {a['name']}" if ev else a["name"]
    return {
        "forms": {f["oid"]: f["name"] for f in catalog.get("forms", [])},
        "activities": acts,
        "events": {e["oid"]: e["name"] for e in catalog.get("events", [])},
    }


def build_index(catalog: dict, workflow_pages: list[str], annotated_pages: list[str],
                meta: dict) -> dict:
    ann_blocks = cut_annotated_blocks(catalog, annotated_pages)
    item_pages = item_pages_by_form(catalog, ann_blocks, annotated_pages)
    # n_pages は meta とは別に索引本体に持つ: 被覆断言の分母がブロック表由来だと、
    # ブロックが丸ごと落ちた索引ほど分母も一緒に縮んで断言が通ってしまう (自己参照)。
    return {
        "meta": meta,
        "names": display_names(catalog),
        "workflow": {"n_pages": len(workflow_pages),
                     "blocks": cut_workflow_blocks(catalog, workflow_pages)},
        "annotated": {
            "n_pages": len(annotated_pages),
            "blocks": ann_blocks,
            "item_pages": item_pages,
            "page_groups": page_groups_by_form(catalog, item_pages),
        },
    }


@dataclass(frozen=True)
class AssertionResult:
    name: str
    ok: bool
    detail: str


def check_index(index: dict, catalog: dict) -> list[AssertionResult]:
    """3 本の断言を**全部**計算して返す (最初の 1 本で raise しない)。

    S0 §4-1 の要求そのもの: この 2 本 (ブロック数 == assignments 数 / 被覆 ≥930) が将来の
    PDF 版で破れたときに、黙って違うページを返すのではなく響いて落ちること。1 本目で
    止めると「直った?」を確かめるのに 3 往復かかる。
    """
    blocks = index["workflow"]["blocks"]
    n_assign = len(catalog["assignments"])
    covered = sum(b["end"] - b["start"] + 1 for b in blocks)
    triples = {(b["event_oid"], b["activity_oid"], b["form_oid"]) for b in blocks}
    want = {(a["event_oid"], a["activity_oid"], a["form_oid"]) for a in catalog["assignments"]}
    total_pages = index["workflow"]["n_pages"]
    n_form_blocks = sum(1 for b in index["annotated"]["blocks"] if b["kind"] == "form")
    n_forms = len(catalog["forms"])
    missing = sorted(want - triples)
    return [
        # 件数だけだと「1 つ落ちて 1 つ重複」が通ってしまうので、三つ組の集合一致まで見る。
        AssertionResult(
            "workflow_blocks_eq_assignments",
            len(blocks) == n_assign and triples == want,
            f"blocks={len(blocks)} assignments={n_assign} "
            f"unique_triples={len(triples)} missing={missing[:3]}",
        ),
        AssertionResult(
            "workflow_page_coverage",
            covered >= total_pages - MAX_UNCOVERED_PAGES,
            f"covered {covered}/{total_pages} (許容外れ ≤{MAX_UNCOVERED_PAGES} 頁)",
        ),
        AssertionResult(
            "annotated_form_blocks_eq_forms",
            n_form_blocks == n_forms,
            f"form blocks={n_form_blocks} forms={n_forms}",
        ),
    ]


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _pdftotext_version() -> str:
    r = subprocess.run(["pdftotext", "-v"], capture_output=True, text=True)
    return (r.stderr or r.stdout).strip().splitlines()[0]


def load_pages(pdf: Path, cache_dir: Path | None, sha: str) -> list[str]:
    """頁本文 (キャッシュ鍵 = PDF の sha256)。1,145 頁で子プロセス 1,145 回 ≈20s、
    再実行が毎回それを払うと索引を触るのが億劫になる。鍵が中身そのものなので、
    PDF が変われば必ず取り直す。"""
    cache = cache_dir / f"{sha}.json" if cache_dir else None
    if cache and cache.is_file():
        return json.loads(cache.read_text(encoding="utf-8"))
    pages = extract_pages(pdf)
    if cache:
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(json.dumps(pages, ensure_ascii=False), encoding="utf-8")
    return pages


def build_from_pdfs(workflow_pdf: Path, annotated_pdf: Path, catalog: dict,
                    cache_dir: Path | None = None) -> dict:
    shas = {"workflow": _sha256(workflow_pdf), "annotated": _sha256(annotated_pdf)}
    wf = load_pages(workflow_pdf, cache_dir, shas["workflow"])
    ann = load_pages(annotated_pdf, cache_dir, shas["annotated"])
    meta = {
        "generated": datetime.now(UTC).isoformat(),
        "study": catalog.get("study"),
        "catalog_version": catalog.get("version_new"),
        "extraction_command": "pdftotext -layout -f N -l N <pdf> -",
        "pdftotext_version": _pdftotext_version(),
        "pdfs": {
            "workflow": {"name": workflow_pdf.name, "pages": len(wf), "sha256": shas["workflow"]},
            "annotated": {"name": annotated_pdf.name, "pages": len(ann), "sha256": shas["annotated"]},
        },
    }
    return build_index(catalog, wf, ann, meta)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--study", default="st01")
    ap.add_argument("--registry", default=None)
    ap.add_argument("--out", default=None, help="既定: <out_dir>/pdf_page_index.json")
    ap.add_argument("--no-cache", action="store_true")
    args = ap.parse_args()

    sp = resolve_study(args.study, args.registry)
    if not (sp.pdf_workflow and sp.pdf_annotated):
        raise SystemExit(
            f"{args.study}: registry に pdf_workflow / pdf_annotated が無い —— "
            "画面判読通道はこの 2 つのファイル無しには成立しない"
        )
    catalog = json.loads((sp.out_dir / "catalog.json").read_text(encoding="utf-8"))
    cache_dir = None if args.no_cache else sp.out_dir / ".pdf_page_text_cache"
    index = build_from_pdfs(sp.pdf_workflow, sp.pdf_annotated, catalog, cache_dir)

    results = check_index(index, catalog)
    for r in results:
        print(f"[{'PASS' if r.ok else 'FAIL'}] {r.name}: {r.detail}")
    if not all(r.ok for r in results):
        return 1  # 断言が落ちた索引は書かない —— 書けば次の実行が"古くて正しい"を上書きする

    out = Path(args.out) if args.out else sp.out_dir / "pdf_page_index.json"
    out.write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
    n_items = sum(len(v) for v in index["annotated"]["item_pages"].values())
    print(f"wrote {out} ({out.stat().st_size / 1024:.0f} KB; "
          f"workflow blocks={len(index['workflow']['blocks'])}, "
          f"annotated blocks={len(index['annotated']['blocks'])}, "
          f"item→page entries={n_items})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
