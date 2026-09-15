"""DM2 T2: 研读包到底多少 token —— 每个可选模型各量一次, 数字进 evidence.

跑 (从 sdtm-rag/):
  .venv/bin/python eval/prod_wirein/dm2_dossier_tokens.py [--sections 4,5,6,7,8,9,10,11,12] [--no-choices]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from litellm import token_counter  # noqa: E402

from server.config import settings  # noqa: E402
from server.study_dossier import build_dossier  # noqa: E402


def _strip_choices(text: str) -> str:
    """去掉一览项行里的编码表选择肢字段, 只留前两个 ' | ' 字段 (title | 型)."""
    out = []
    for line in text.splitlines():
        if line.startswith("[") and " | " in line:
            parts = line.split(" | ")
            line = " | ".join(parts[:2])
        out.append(line)
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sections", default="4,5,6,7,8,9,10,11,12")
    ap.add_argument("--max-chars", type=int, default=400_000)
    ap.add_argument("--no-choices", action="store_true",
                     help="丢弃一览项行里的编码表选择肢字段 (只留 title | 型), 给出收窄后的备选数字")
    args = ap.parse_args()
    cards = Path(settings.study_kb_root)
    docs = cards.parent / "docs"
    d = build_dossier(docs, cards, sections=args.sections.split(","), max_chars=args.max_chars)
    text = _strip_choices(d.text) if args.no_choices else d.text
    a_end = text.index("## B. EDC")
    print(f"sections={args.sections}  no_choices={args.no_choices}  chars={len(text)}  "
          f"(A={a_end}, B={len(text) - a_end})  "
          f"n_sections={len(d.sections)} n_items={d.n_items} sha={d.sha}")
    print(f"{'model id':10s} {'litellm model':60s} tokens")
    for m in settings.selectable_models:
        try:
            n = token_counter(model=m.model, text=text)
        except Exception as e:  # noqa: BLE001 — 记下来, 不让一个模型的 tokenizer 缺失挡住其它
            n = f"ERR {type(e).__name__}"
        print(f"{m.id:10s} {m.model:60s} {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
