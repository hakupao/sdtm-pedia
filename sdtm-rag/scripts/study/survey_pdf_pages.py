"""S0-1 勘察脚本 (一次性): catalog 名称 → PDF 页 的可定位性普查。

刻意与生产脚本隔离 (survey_ 前缀), 只产出 data/study/st01/pdf_page_index_survey_draft.json
和统计 JSON。不进任何生产路径。

复跑:
    uv run python scripts/study/survey_pdf_pages.py --out-dir <scratch>
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import subprocess
import sys
import time
from datetime import UTC, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1].parent))
from scripts.study.pdf_text import count_pages, extract_pages  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
SRC = REPO.parent / "source" / "study" / "ensemble"
PDFS = {
    "annotated": SRC / "ENSEMBLE_59.0_Annotated.pdf",
    "workflow": SRC / "ENSEMBLE 59.0 workflow.pdf",
}
CATALOG = REPO / "data" / "study" / "st01" / "catalog.json"

_WS = re.compile(r"\s+")
GENERIC_THRESHOLD = 20  # 命中 > 20 页 = 过泛, 不可用作定位键


def norm_ws(s: str) -> str:
    return _WS.sub(" ", s).strip()


def norm_nows(s: str) -> str:
    return _WS.sub("", s)


def build_page_texts(pdf: Path, cache: Path) -> list[dict]:
    """逐页抽取 (pdftotext -layout -f N -l N), 结果缓存到 cache (JSON)。"""
    if cache.exists():
        return json.loads(cache.read_text())
    t0 = time.time()
    pages = extract_pages(pdf)
    out = [{"page": i + 1, "ws": norm_ws(p), "nows": norm_nows(p)} for i, p in enumerate(pages)]
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(out, ensure_ascii=False))
    print(f"  extracted {len(out)} pages in {time.time() - t0:.1f}s -> {cache}", file=sys.stderr)
    return out


_ASCII = re.compile(r"^[A-Za-z0-9_.\\-]+$")


def locate(needle: str, pages: list[dict], boundary: bool = False) -> dict:
    """返回 {ws:[pages], nows:[pages], union:[pages]}。

    boundary=True (OID 类纯 ASCII 串) 用 token 边界正则。无边界的子串匹配下, 一个 2
    字符的 form OID 会命中以它开头的每个长 item OID, 单字符 OID 则命中一切 —— 定位率
    会被虚高到接近 100%。
    """
    nw, nn = norm_ws(needle), norm_nows(needle)
    if len(nn) < 1:
        return {"ws": [], "nows": [], "union": [], "skipped": "empty"}
    if boundary and _ASCII.match(nn):
        rx = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(nn) + r"(?![A-Za-z0-9_])")
        hw = [p["page"] for p in pages if rx.search(p["ws"])]
        return {"ws": hw, "nows": hw, "union": hw}
    if len(nn) < 2:
        return {"ws": [], "nows": [], "union": [], "skipped": "too_short"}
    hw = [p["page"] for p in pages if nw and nw in p["ws"]]
    hn = [p["page"] for p in pages if nn in p["nows"]]
    return {"ws": hw, "nows": hn, "union": sorted(set(hw) | set(hn))}



PAGE_PREFIX = "ENSEMBLE | ENSEMBLE [59.0] "


def workflow_blocks(cat: dict, pages: list[dict]) -> list[list]:
    """workflow PDF 按标题行切块。标题形如 `<event名> / <activity名> <form名>`。

    ⚠ 比"名称子串搜索"准得多: 子串搜索会把交叉引用页也算进去 (再評価 17 页),
    切块则把每页唯一归属到一个 (event, activity, form)。
    """
    pairs = sorted({(a["event_name"], a["activity_name"]) for a in cat["assignments"]},
                   key=lambda x: -(len(x[0]) + len(x[1])))
    fnames = sorted({f["name"] for f in cat["forms"]}, key=len, reverse=True)
    titled: dict[int, tuple] = {}
    for p in pages:
        t = p["ws"][len(PAGE_PREFIX):]
        for ev, ac in pairs:
            pre = f"{ev} / {ac} "
            if t.startswith(pre):
                rest = t[len(pre):]
                f = next((x for x in fnames if rest.startswith(x)), None)
                titled[p["page"]] = (ev, ac, f)
                break
    o = sorted(titled)
    return [[st, (o[i + 1] - 1) if i + 1 < len(o) else len(pages), *titled[st]]
            for i, st in enumerate(o)]


def annotated_blocks(cat: dict, pages: list[dict]) -> list[list]:
    """Annotated PDF 按标题行切块。表单页 `<form名> <form_oid>`; 代码表页 `<form名> - Code Lists`。"""
    forms = sorted(cat["forms"], key=lambda f: -len(f["name"]))
    titled: dict[int, tuple] = {}
    for p in pages:
        t = p["ws"][len(PAGE_PREFIX):]
        for f in forms:
            if t.startswith(f"{f['name']} {f['oid']} ") or t == f"{f['name']} {f['oid']}":
                titled[p["page"]] = ("form", f["oid"], f["name"])
                break
            if t.startswith(f"{f['name']} - Code Lists"):
                titled[p["page"]] = ("codelist", f["oid"], f["name"])
                break
    o = sorted(titled)
    return [[st, (o[i + 1] - 1) if i + 1 < len(o) else len(pages), *titled[st]]
            for i, st in enumerate(o)]


def entity_needles(cat: dict) -> dict[str, list[tuple[str, str]]]:
    """(key, needle) 列表。key 为 OID (items 用 item_oid)。"""
    seen_i = set()
    items = []
    for it in cat["items"]:
        k = it["item_oid"]
        if k in seen_i:
            continue
        seen_i.add(k)
        items.append((k, it.get("label") or ""))
    groups: dict[str, str] = {}
    for it in cat["items"]:
        g = it.get("group_oid")
        if g:
            groups.setdefault(g, it.get("group_name") or "")
    return {
        "activities": [(a["oid"], a["name"]) for a in cat["activities"]],
        "events": [(e["oid"], e["name"]) for e in cat["events"]],
        "forms": [(f["oid"], f["name"]) for f in cat["forms"]],
        "items": items,
        # 原始 OID 串 (S0-0 已知几乎搜不到, 这里量化)
        "activity_oids": [(a["oid"], a["oid"]) for a in cat["activities"]],
        "form_oids": [(f["oid"], f["oid"]) for f in cat["forms"]],
        "item_oids": [(k, k) for k in sorted(seen_i)],
        "groups": [(k, v) for k, v in groups.items() if v.strip()],
        "group_oids": [(k, k) for k in groups],
    }


# ── S0-3: Bedrock 多模态实测 ────────────────────────────────────────────
# 复跑: uv run python scripts/study/survey_pdf_pages.py probe --pdf workflow --page 315
PROBE_PROMPT = "この画面に表示されている項目名を列挙してください。OID ではなく画面上の日本語ラベルで。"


def probe_models(pdf_key: str, page: int, dpi: int, out_dir: Path) -> None:
    import asyncio
    import base64

    from server.config import Settings
    from server.llm_config import create_router

    out_dir.mkdir(parents=True, exist_ok=True)
    sizes = {}
    for r in (80, 110, 150):
        stem = out_dir / f"probe_{pdf_key}_{page}_r{r}"
        subprocess.run(["pdftoppm", "-r", str(r), "-png", "-f", str(page), "-l", str(page),
                        str(PDFS[pdf_key]), str(stem)], check=True)
        f = next(iter(sorted(stem.parent.glob(stem.name + "*.png"))))
        sizes[r] = {"path": str(f), "bytes": f.stat().st_size}
    png = Path(sizes[dpi]["path"])
    b64 = base64.b64encode(png.read_bytes()).decode()
    print(json.dumps({"png_bytes": sizes}, ensure_ascii=False, indent=1))

    s = Settings()
    router = create_router(s)
    msgs = [{"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{b64}"}},
        {"type": "text", "text": PROBE_PROMPT},
    ]}]

    async def one(mid: str) -> dict:
        t0 = time.time()
        try:
            r = await router.acompletion(model=mid, messages=msgs)
            u = getattr(r, "usage", None)
            return {"model_id": mid, "ok": True,
                    "reported_model": getattr(r, "model", None),
                    "text": (r.choices[0].message.content or "")[:300],
                    "prompt_tokens": getattr(u, "prompt_tokens", None),
                    "completion_tokens": getattr(u, "completion_tokens", None),
                    "wall_s": round(time.time() - t0, 2)}
        except Exception as e:  # noqa: BLE001 — 勘察要的正是失败文本本身
            return {"model_id": mid, "ok": False, "error": f"{type(e).__name__}: {e}"[:600],
                    "wall_s": round(time.time() - t0, 2)}

    ids = [m.id for m in s.selectable_models]
    async def all_of(xs):
        return await asyncio.gather(*(one(i) for i in xs))

    res = asyncio.run(all_of(ids))
    out = {"page": page, "pdf": pdf_key, "dpi": dpi, "png_bytes": sizes,
           "prompt": PROBE_PROMPT, "results": res}
    (out_dir / "model_probe.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
    print(json.dumps(out, ensure_ascii=False, indent=1))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", nargs="?", default="index", choices=["index", "probe"])
    ap.add_argument("--pdf", default="workflow", choices=list(PDFS))
    ap.add_argument("--page", type=int, default=315)
    ap.add_argument("--dpi", type=int, default=110)
    ap.add_argument("--out-dir", default="/tmp/c2r_s0")
    # ⚠ 既定の出力名は `pdf_page_index.json` **ではない**: そこは I2-1 の生産索引
    # (`build_pdf_page_index.py` の出力) の置き場で、本勘察スクリプトを再実行すると
    # 草案で上書きしてしまう (2026-09-09 に実際に起きた)。草案は別名で出す。
    ap.add_argument("--index-out",
                    default=str(CATALOG.parent / "pdf_page_index_survey_draft.json"))
    args = ap.parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.mode == "probe":
        probe_models(args.pdf, args.page, args.dpi, out_dir)
        return

    cat = json.loads(CATALOG.read_text())
    needles = entity_needles(cat)

    index: dict = {"meta": {}}
    stats: dict = {}
    for pdf_key, pdf in PDFS.items():
        print(f"[{pdf_key}] {pdf}", file=sys.stderr)
        npages = count_pages(pdf)
        pages = build_page_texts(pdf, out_dir / f"pages_{pdf_key}.json")
        assert len(pages) == npages, f"{len(pages)} != {npages}"
        index[pdf_key] = {"blocks": (workflow_blocks if pdf_key == "workflow" else annotated_blocks)(cat, pages)}
        stats[pdf_key] = {"pages": npages, "blocks": len(index[pdf_key]["blocks"])}
        for etype, pairs in needles.items():
            res = {}
            for key, needle in pairs:
                r = locate(needle, pages, boundary=etype.endswith("_oids"))
                res[key] = {"needle": needle, "pages": r["union"],
                            "n": len(r["union"]),
                            "ws_only": sorted(set(r["ws"]) - set(r["nows"])),
                            "nows_only": sorted(set(r["nows"]) - set(r["ws"])),
                            "generic": len(r["union"]) > GENERIC_THRESHOLD}
            index[pdf_key][etype] = res
            total = len(res)
            located = [k for k, v in res.items() if v["n"] >= 1]
            usable = [k for k, v in res.items() if 1 <= v["n"] <= GENERIC_THRESHOLD]
            med = statistics.median([res[k]["n"] for k in located]) if located else 0
            stats[pdf_key][etype] = {
                "total": total,
                "located": len(located),
                "located_pct": round(100 * len(located) / total, 2) if total else 0,
                "usable_1_20": len(usable),
                "usable_pct": round(100 * len(usable) / total, 2) if total else 0,
                "generic": total - len(usable) - (total - len(located)),
                "median_pages_per_located": med,
            }
            print(f"  {etype}: {len(located)}/{total} located, {len(usable)} usable(1-{GENERIC_THRESHOLD}), median={med}",
                  file=sys.stderr)

    index["meta"] = {
        "generated": datetime.now(UTC).isoformat(),
        "draft": True,
        "note": "S0-1 勘察草案; 非生产件。名称→页, 键 = catalog OID。",
        "generic_threshold": GENERIC_THRESHOLD,
        "extraction_command": "pdftotext -layout -f N -l N <pdf> -  (逐页, scripts/study/pdf_text.py::extract_pages)",
        "pdftotext_version": subprocess.run(["pdftotext", "-v"], capture_output=True, text=True).stderr.strip().splitlines()[0],
        "pdfs": {k: {"path": str(v), "pages": stats[k]["pages"]} for k, v in PDFS.items()},
        "match_variants": "union of whitespace-collapsed and whitespace-stripped containment",
    }
    Path(args.index_out).write_text(json.dumps(index, ensure_ascii=False, indent=1))
    (out_dir / "coverage_stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1))
    print(json.dumps(stats, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
