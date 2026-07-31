"""catalog → field card markdown (spec §3.1 模板). 模板拼装, 零 LLM."""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from scripts.study.parse_demo import sample_demo_values
from scripts.study.paths import resolve_study


def render_field_card(item: dict, form: dict, codelist: dict | None,
                      samples: list[str], diff: list[str], *,
                      study: str, version: str) -> str:
    fm = "\n".join([
        "---",
        f"study: {study}",
        f"version: {version}",
        "doc_type: field_card",
        f"form_oid: {item['form_oid']}",
        f"field_oid: {item['item_oid']}",
        "source_sheet: Items and Groups",
        f"source_row: {item['row']}",
        "generated_by: build_field_cards.py",
        "---",
    ])
    length = "/".join(x for x in (item["min_length"], item["max_length"]) if x)
    type_bits = item["data_type"] or "?"
    if length:
        type_bits += f" (len {length})"
    type_bits += " / 必須" if item["required"] else " / 任意"
    if codelist:
        cl_lines = "\n".join(f"  - {code} = {text}" for code, text in codelist["entries"])
        cl_block = f"{item['choices']}\n{cl_lines}"
    else:
        cl_block = item["choices"] or "なし (自由記述)"
    checks = " / ".join(x for x in (item["data_checks"], item["system_checks"]) if x) or "—"
    # 可見性: visible_condition 只覆盖 Show on simple (66/959); 另有 36% 的条件散在
    # raw 的 advanced/hide 列 — 有条件但结构化字段空时降级为标记行 (公式不展开, pilot 再定)
    vis = item["visible_condition"]
    if not vis:
        vis_cols = [k.split("::")[1] for k in (
            "Visibility::Show on advanced condition",
            "Visibility::Hide on simple condition",
            "Visibility::Hide on advanced condition",
            "Visibility::Hidden in activity",
        ) if item["raw"].get(k)]
        vis = f"条件付き表示 ({', '.join(vis_cols)})" if vis_cols else "常時表示"
    lines = [
        # 30/959 item 无 label → 标题降级用 item_oid; 254/959 无组名 → '—'
        f"# [{item['form_name']} {item['form_oid']}] "
        f"{item['label'] or item['item_oid']} ({item['item_oid']})",
        f"- Form: {item['form_name']} ({item['form_oid']})",
        f"- Item group: {item['group_name'] or '—'} ({item['group_oid']})",
        f"- 型: {type_bits}",
        f"- Control: {item['control_type'] or '—'}"
        + (f" / 単位: {item['unit']}" if item["unit"] else ""),
        f"- Codelist: {cl_block}",
        f"- Edit checks: {checks}",
        f"- 表示条件: {vis}",
        # DEMO 每 sheet 仅 1 行数据 → 至多 1 个示例值; 288/959 永无示例值
        f"- DEMO 例値: {' / '.join(samples) if samples else '—'}",
        f"- 旧→新版差分: {'; '.join(diff) if diff else 'なし'}",
    ]
    if item["output_field_id"]:
        lines.append(f"- Output: {item['output_field_id']} ({item['output_field_label']})")
    for label, key in (("説明", "description"), ("入力指示", "instructions")):
        if item[key]:
            lines.append(f"- {label}: {item[key]}")
    return fm + "\n\n" + "\n".join(lines) + "\n"


def _write_index(catalog: dict, cards_dir: Path, per_form: dict[str, int]) -> None:
    rows = ["# st01 Field Card Index", "",
            f"Study: {catalog['study']} / version {catalog['version_new']}", "",
            "| Form | 名称 | 項目数 |", "|---|---|---|"]
    for f in catalog["forms"]:
        rows.append(f"| {f['oid']} | {f['name']} | {per_form.get(f['oid'], 0)} |")
    (cards_dir / "INDEX.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    routing = (
        "# Routing\n\n"
        f"本 KB は研究 {catalog['study']} の EDC 画面項目カード集 (1 項目 = 1 card)。\n"
        "画面名/フォーム名/項目ラベル/Item OID で検索する。SDTM 標準の規則は別 KB (cdisc)。\n"
    )
    (cards_dir / "ROUTING.md").write_text(routing, encoding="utf-8")


def build_cards(catalog: dict, samples: dict[str, list], cards_dir: Path, *,
                forms_filter: set[str] | None = None) -> list[Path]:
    if cards_dir.exists():
        shutil.rmtree(cards_dir)          # 幂等: 全量重生成, 勿手改产物
    cards_dir.mkdir(parents=True)
    forms_by_oid = {f["oid"]: f for f in catalog["forms"]}
    out: list[Path] = []
    per_form: dict[str, int] = {}
    for item in catalog["items"]:
        if forms_filter and item["form_oid"] not in forms_filter:
            continue
        card = render_field_card(
            item, forms_by_oid.get(item["form_oid"], {}),
            catalog["codelists"].get(item["choices"]),
            samples.get(item["item_oid"], []),
            catalog["diffs"].get(item["item_oid"], []),
            study=catalog["study"], version=catalog["version_new"],
        )
        p = cards_dir / f"{catalog['study']}__{item['form_oid']}__{item['item_oid']}.md"
        p.write_text(card, encoding="utf-8")
        out.append(p)
        per_form[item["form_oid"]] = per_form.get(item["form_oid"], 0) + 1
    _write_index(catalog, cards_dir, per_form)
    return out


def main(argv=None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--study", required=True)
    ap.add_argument("--forms", help="逗号分隔 form OID, 缺省全量")
    args = ap.parse_args(argv)
    sp = resolve_study(args.study)
    catalog = json.loads((sp.out_dir / "catalog.json").read_text(encoding="utf-8"))
    samples: dict[str, list] = {}
    if sp.demo_export is not None:
        samples, _stats = sample_demo_values(sp.demo_export, catalog["items"])
    flt = set(args.forms.split(",")) if args.forms else None
    paths = build_cards(catalog, samples, sp.cards_dir, forms_filter=flt)
    print(f"cards={len(paths)} dir={sp.cards_dir}")


if __name__ == "__main__":
    main()
