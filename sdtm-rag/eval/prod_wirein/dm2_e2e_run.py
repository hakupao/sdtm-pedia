"""DM2 T9: L3 e2e 跑批 —— 3 题 × 2 模型 = 6 次生产调用, 全文/usage/研读包徽章落盘.

判据在 evidence/checkpoints/dm2_dossier_e2e.md §0 (本脚本提交**之前**已登记).
本脚本只**跑**不**判**: 判分由异 subagent 读 judge_pack.json 做 (规则 D).

跑 (从 sdtm-rag/, 生产服务需已起在 --base):
  .venv/bin/python eval/prod_wirein/dm2_e2e_run.py

产物 (全部在 gitignored data/study/<sid>/eval/runs/dm2_e2e/):
  <qid>_<model>.json  单次跑的 question/model/sources_event/answer/done_event/wall_seconds
  judge_pack.json     判分 agent 的唯一输入 (答案 + gold 卡 basename + 域定义段 + 一览文本)

⚠ 本文件不写任何 study OID / 表单名 / 日文 label —— 题面与 gold 卡都在运行时从
  gitignored 的 test set 读, 只有 question id 进版本库.
"""
from __future__ import annotations

import argparse
import codecs
import json
import sys
import time
from pathlib import Path

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from server.config import settings  # noqa: E402
from server.study_dossier import build_dossier  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]
QIDS = ("dm01", "dm02", "dm05")
MODELS = ("opus-5", "sonnet-5")
# 答案很长且可能自动续写多轮; 读超时按最坏情况给 15 分钟, 不是按平均给.
READ_TIMEOUT_S = 900
CONNECT_TIMEOUT_S = 10
RETRY_SLEEP_S = 60


# ── SSE ───────────────────────────────────────────────────────────────

def _sse_events(resp: requests.Response):
    """逐帧 yield (event, data_dict). 自己做增量 UTF-8 解码 —— iter_lines 的
    decode_unicode 会在多字节字符跨 chunk 边界时把日文/中文劈坏, 而本题集两题是
    非 ASCII 的, 劈坏了就是"答案看起来乱码", 排查成本远高于这几行."""
    dec = codecs.getincrementaldecoder("utf-8")()
    buf = ""
    event = None
    data_lines: list[str] = []
    for raw in resp.iter_content(chunk_size=None):
        buf += dec.decode(raw)
        while "\n" in buf:
            line, buf = buf.split("\n", 1)
            line = line.rstrip("\r")
            if line == "":
                if event is not None or data_lines:
                    payload = "\n".join(data_lines)
                    try:
                        data = json.loads(payload) if payload else {}
                    except json.JSONDecodeError:
                        data = {"_unparsed": payload}
                    yield event or "message", data
                event, data_lines = None, []
            elif line.startswith("event:"):
                event = line[len("event:"):].strip()
            elif line.startswith("data:"):
                data_lines.append(line[len("data:"):].lstrip(" "))
            # 其余 SSE 字段 (id:/retry:/注释行) 本服务不发, 有意忽略


def _one_call(base: str, question: str, model: str) -> dict:
    """一次 /api/ask_stream. 返回本次尝试的完整记录; 网络/HTTP 失败也返回记录
    (ok=False) 而不抛 —— 上层要把两次尝试都存进证据里 (规则 B)."""
    body = {"question": question, "history": [], "model": model, "dossier": "auto"}
    rec: dict = {"ok": False, "error": None, "http_status": None,
                 "sources_event": None, "answer": "", "done_event": None,
                 "error_event": None, "continue_events": [], "n_token_events": 0,
                 "wall_seconds": None}
    t0 = time.monotonic()
    try:
        with requests.post(f"{base}/api/ask_stream", json=body, stream=True,
                           timeout=(CONNECT_TIMEOUT_S, READ_TIMEOUT_S)) as resp:
            rec["http_status"] = resp.status_code
            if resp.status_code != 200:
                rec["error"] = f"HTTP {resp.status_code}: {resp.text[:500]}"
                return rec
            parts: list[str] = []
            for ev, data in _sse_events(resp):
                if ev == "sources":
                    rec["sources_event"] = data
                elif ev == "token":
                    parts.append(data.get("text", ""))
                    rec["n_token_events"] += 1
                elif ev == "continue":
                    rec["continue_events"].append(data)
                elif ev == "done":
                    rec["done_event"] = data
                elif ev == "error":
                    rec["error_event"] = data
                    rec["error"] = f"sse error event: {data}"
            rec["answer"] = "".join(parts)
    except Exception as e:  # noqa: BLE001 — 失败也要留档, 不能让异常把本次尝试抹掉
        rec["error"] = f"{type(e).__name__}: {e}"
    finally:
        rec["wall_seconds"] = round(time.monotonic() - t0, 1)
    if rec["error"] is None and rec["done_event"] is None:
        rec["error"] = "stream ended without a done event"
    rec["ok"] = rec["error"] is None
    return rec


# ── judge pack 原料 ───────────────────────────────────────────────────

def _first_paragraph(md: Path) -> str:
    """域 assumptions.md 的第一段 (跳过 H1 标题, 取首个非空块到空行为止)."""
    lines = md.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    for line in lines:
        if not out:
            if not line.strip() or line.startswith("#"):
                continue
            out.append(line)
        elif line.strip():
            out.append(line)
        else:
            break
    return "\n".join(out).strip()


def _item_list_text() -> str:
    """活的研读包 B 部 (EDC 项目一览) 全文 —— 判据 ② 的"一览中真实存在"要拿它 grep."""
    d = build_dossier(settings.dossier_docs_dir, settings.dossier_cards_dir,
                      sections=settings.dossier_prt_sections,
                      max_chars=settings.dossier_max_chars)
    for i, line in enumerate(d.text.splitlines()):
        if line.startswith("## B."):
            return "\n".join(d.text.splitlines()[i:])
    raise RuntimeError("dossier text has no '## B.' section")


def _load_questions(yml: Path) -> dict[str, dict]:
    items = yaml.safe_load(yml.read_text(encoding="utf-8"))
    return {q["id"]: q for q in items}


# ── main ──────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="http://127.0.0.1:8000")
    # 断点续跑: 已落盘的 <qid>_<model>.json 原样复用, 不重打生产. 六次调用一共近 20 分钟,
    # 中途被杀 (OOM / 断网) 时重跑全部既烧钱又会把已拿到的答案换成另一次采样 —— 那会让
    # "跑批"与"判分"看的不是同一批答案. 要重采某一次, 删掉那个 json 再跑.
    ap.add_argument("--no-resume", action="store_true",
                    help="忽略已落盘的结果, 六次全部重打生产")
    # attempt 3 (Claude 重跑 + 留出题) 用: 换题集/换产物目录, 不覆盖 attempt 2 的答案 (规则 B).
    ap.add_argument("--qids", default=",".join(QIDS), help="逗号分隔题号")
    ap.add_argument("--out-subdir", default="dm2_e2e", help="runs/ 下的产物目录名")
    ap.add_argument("--require-no-fallback", action="store_true",
                    help="任一 run fell_back 即 GATE FAIL (模型维度对比时必开)")
    args = ap.parse_args()
    qids = tuple(q.strip() for q in args.qids.split(",") if q.strip())

    study_dir = Path(settings.study_kb_root).parent
    yml = study_dir / "eval" / "test_set_domain_mapping_v1.yml"
    out_dir = study_dir / "eval" / "runs" / args.out_subdir
    out_dir.mkdir(parents=True, exist_ok=True)
    questions = _load_questions(yml)

    runs: list[tuple[str, str, dict]] = []
    print(f"# dm2 e2e: {len(qids)}q x {len(MODELS)}model = {len(qids) * len(MODELS)} runs "
          f"(sequential; base={args.base})")
    for qid in qids:
        q = questions[qid]
        for model in MODELS:
            dest = out_dir / f"{qid}_{model}.json"
            if not args.no_resume and dest.exists():
                rec = json.loads(dest.read_text(encoding="utf-8"))
                runs.append((qid, model, rec))
                print(_summary_line(qid, model, rec) + "  [resumed]", flush=True)
                continue
            # 顺跑, 不并行: 生产有 per-IP 限流, 并行会把这批跑成"限流实验".
            attempts = [_one_call(args.base, q["question"], model)]
            if not attempts[0]["ok"]:
                print(f"  !! {qid} {model} attempt 1 failed: {attempts[0]['error']}; "
                      f"retry once after {RETRY_SLEEP_S}s", flush=True)
                time.sleep(RETRY_SLEEP_S)
                attempts.append(_one_call(args.base, q["question"], model))
            last = attempts[-1]
            rec = {
                "question": q["question"],
                "model": model,
                "sources_event": last["sources_event"],
                "answer": last["answer"],
                "done_event": last["done_event"],
                "wall_seconds": last["wall_seconds"],
                # 额外留档 (规则 B): 失败的那次尝试原样保留, 不被成功的一次覆盖掉.
                "question_id": qid,
                "domain": q["domain"],
                "attempts": attempts,
                "n_attempts": len(attempts),
            }
            dest.write_text(json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
            runs.append((qid, model, rec))
            print(_summary_line(qid, model, rec), flush=True)

    _write_judge_pack(out_dir, runs, questions)
    return _gate(runs, out_dir, require_no_fallback=args.require_no_fallback)


def _summary_line(qid: str, model: str, rec: dict) -> str:
    dos = ((rec.get("done_event") or {}).get("dossier")
           or (rec.get("sources_event") or {}).get("dossier") or {})
    done = rec.get("done_event") or {}
    usage = done.get("usage") or {}
    return (f"{qid} {model:9s} attached={dos.get('attached')} reason={dos.get('reason')} "
            f"model_used={done.get('model_used')} fell_back={done.get('fell_back')} "
            f"prompt_tokens={usage.get('prompt_tokens')} "
            f"completion_tokens={usage.get('completion_tokens')} "
            f"continue_rounds={done.get('continue_rounds')} "
            f"truncated={done.get('truncated')} "
            f"wall_seconds={rec.get('wall_seconds')} "
            f"answer_chars={len(rec.get('answer') or '')}")


def _write_judge_pack(out_dir: Path, runs, questions: dict[str, dict]) -> None:
    item_list = _item_list_text()
    pack_runs = []
    for qid, model, rec in runs:
        q = questions[qid]
        gold = [s for s in q["expected_sources"] if not s.startswith("domains/")]
        defn = REPO_ROOT / "knowledge_base" / "domains" / q["domain"] / "assumptions.md"
        pack_runs.append({
            "qid": qid,
            "model": model,
            "question": q["question"],
            "answer": rec["answer"],
            "gold_cards": gold,
            "domain_definition_text": _first_paragraph(defn),
        })
    pack = {"runs": pack_runs, "item_list_text": item_list}
    p = out_dir / "judge_pack.json"
    p.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"# judge_pack: {p} ({len(pack_runs)} runs, item_list {len(item_list)} chars)")


def _gate(runs, out_dir: Path, require_no_fallback: bool = False) -> int:
    attached = [f"{q}/{m}" for q, m, r in runs
                if not (((r.get("done_event") or {}).get("dossier") or {}).get("attached"))]
    fell = [f"{q}/{m}" for q, m, r in runs if (r.get("done_event") or {}).get("fell_back")]
    trunc = [f"{q}/{m}" for q, m, r in runs if (r.get("done_event") or {}).get("truncated")]
    retried = [f"{q}/{m}" for q, m, r in runs if r["n_attempts"] > 1]
    print(f"# GATE attached: {len(runs) - len(attached)}/{len(runs)} "
          + ("PASS" if not attached else f"FAIL (missing: {', '.join(attached)})"))
    # fell_back / truncated 不静默重跑: 它们是要进报告的事实, 重跑会把它们洗掉.
    print(f"# fell_back: {fell or 'none'}   truncated: {trunc or 'none'}   retried: {retried or 'none'}")
    print(f"# runs dir: {out_dir}")
    if require_no_fallback:
        # fell_back 三态: None (未知) 也算不过 —— 对比要的是"确证没回退", 不是"没报回退".
        unproven = [f"{q}/{m}" for q, m, r in runs
                    if (r.get("done_event") or {}).get("fell_back") is not False]
        print("# GATE no-fallback: " + ("PASS" if not unproven
                                         else f"FAIL (fell_back not False: {', '.join(unproven)})"))
        if unproven:
            return 1
    return 0 if not attached else 1


if __name__ == "__main__":
    sys.exit(main())
