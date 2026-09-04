"""(b) 层驱动: 权威表 → 逐答案裁判扫描 → 对抗抽样 → 人判包。

⚠ **本脚本产出的不是判定, 是给人判的材料。** 预登记判据写死 (b) 层是**人判 8 条**,
裁判的 verdict 只用来决定抽样池 (5 条抽自它说"干净"的 + 3 条抽自它报警的), 且**不进
人判包** —— 放进去人判就退化成复核裁判, 兜不住漏网。

⚠ **成本**: 逐答案一次裁判调用 ⇒ 102 题 = 102 次。`--dry-run` 走桩裁判, 零调用,
用来验证管线接得通。

跑法 (从 sdtm-rag/):
  .venv/bin/python eval/prod_wirein/run_class_assertion_scan.py \\
      evidence/checkpoints/verified_runs/run_opus-5.json --dry-run
  .venv/bin/python eval/prod_wirein/run_class_assertion_scan.py \\
      evidence/checkpoints/verified_runs/run_opus-5.json --judge-model deepseek/deepseek-chat
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).parent))

from class_assertion_scan import scan_answers  # noqa: E402
from class_authority import (  # noqa: E402
    authority_table_markdown,
    load_class_authority,
)

from build_human_sample import pick_sample, render_human_packet  # noqa: E402  isort:skip

DEFAULT_JUDGE_MODEL = "deepseek/deepseek-chat"


def entries_from_report(report: dict) -> list[dict]:
    """[{id, answer}] —— 只收**完整答案**。

    ⛔ 不回退到 `answer_preview`: 它只有 600 字符, 而答案中位数 3187。拿它去问裁判,
    大部分归属断言不在截断范围内 ⇒ 裁判大面积判"无断言" ⇒ (b) 层恒 PASS,
    且这种失败看起来和真通过一模一样。
    """
    entries = []
    for r in report["results"]:
        answer = r.get("answer")
        if not answer:
            raise ValueError(
                f"{r['id']}: 报告里没有完整 `answer` (只有 answer_preview 或为空)。"
                f"⛔ 拒绝退回 600 字预览 —— (b) 层会因此恒 PASS。"
                f"重跑生成时请带 --full-answers。"
            )
        entries.append({"id": r["id"], "answer": answer})
    return entries


def blind_order(sample: list[dict], seed: int) -> list[dict]:
    """打乱条目顺序后再渲染人判包。

    ⛔ `pick_sample` 返回的是 `clean 段 + flagged 段`, **后 3 条恒是裁判报警的** ——
    顺序本身就是 verdict, 而预登记写死"人判看答案原文 + 权威表, ⛔ 不看裁判的 verdict"。
    不打乱, 判卷人一眼就知道该盯哪三条, 人判退化成复核裁判。
    """
    import random
    out = list(sample)
    random.Random(seed).shuffle(out)
    return out


def make_judge(model: str, dry_run: bool):
    """裁判可调用对象。dry-run 走桩, 零调用, 只验管线。"""
    if dry_run:
        def _stub(prompt: str) -> str:
            return ('{"has_assertion": false, "verdict": "consistent", '
                    '"quote": "", "authority": ""}')
        return _stub

    import litellm

    def _judge(prompt: str) -> str:
        resp = litellm.completion(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        return resp.choices[0].message.content or ""

    return _judge


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("report", help="run_eval 报告 (需 --full-answers 跑出来的)")
    ap.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL)
    ap.add_argument("--dry-run", action="store_true", help="桩裁判, 零 LLM 调用")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out-dir", default="evidence/checkpoints")
    ap.add_argument("--reuse-scan", default=None,
                    help="复用已落盘的扫描结果重渲人判包 (零 LLM 调用)")
    args = ap.parse_args(argv)

    report_path = Path(args.report)
    if not report_path.is_absolute():
        report_path = ROOT / report_path
    report = json.loads(report_path.read_text())

    mapping = load_class_authority()
    authority_md = authority_table_markdown(mapping)
    entries = entries_from_report(report)
    tag = report_path.stem.replace("run_", "")

    print(f"权威表: {len(mapping)} 行 / {len(set(mapping.values()))} 个 Class")
    print(f"待扫答案: {len(entries)} 条 | judge="
          f"{'STUB (dry-run, 零调用)' if args.dry_run else args.judge_model}")

    if args.reuse_scan:
        prior = json.loads((ROOT / args.reuse_scan).read_text())
        rows = prior["rows"]
        print(f"复用已落盘扫描 (零 LLM 调用): {args.reuse_scan} "
              f"(judge={prior.get('judge_model')})")
    else:
        rows = scan_answers(entries, make_judge(args.judge_model, args.dry_run),
                            authority_md)

    tally: dict[str, int] = {}
    for r in rows:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    n_parse_err = sum(1 for r in rows if r.get("parse_error"))
    n_err = sum(1 for r in rows if r.get("error"))
    print(f"裁判分布: {tally} | parse_error={n_parse_err} | 调用失败={n_err}")

    sample, comp = pick_sample(rows, seed=args.seed)
    print(f"抽样构成 (预登记要求记录): {comp}")

    out_dir = ROOT / args.out_dir
    scan_path = out_dir / f"class_scan_{tag}.json"
    scan_path.write_text(json.dumps(
        {"report": str(report_path), "judge_model":
         "STUB" if args.dry_run else args.judge_model,
         "seed": args.seed, "tally": tally, "composition": comp,
         "sample_ids": [r["id"] for r in sample], "rows": rows},
        indent=2, ensure_ascii=False), encoding="utf-8")

    answers_by_id = {e["id"]: e["answer"] for e in entries}
    packet_path = out_dir / f"human_packet_{tag}.md"
    packet_path.write_text(
        render_human_packet(blind_order(sample, args.seed), answers_by_id, authority_md),
        encoding="utf-8")

    print(f"扫描落盘 -> {scan_path}")
    print(f"人判包   -> {packet_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
