#!/usr/bin/env python3
"""C2R V3 runner — 真实 /api/ask 打点, 零判分.

题面真值只从 gitignored data/study/st01/eval/runs/c2r_v3/questions.json 读,
本脚本自身不含任何真实 OID/label。
"""
import argparse, json, sys, time, urllib.request, urllib.error
from pathlib import Path

EVAL = Path(__file__).resolve().parents[3] / "data/study/st01/eval/runs"
QS = json.loads((EVAL / "c2r_v3" / "questions.json").read_text())
RUNS = EVAL / "c2r_v3"   # --out で差し替え (N1 以降は別ディレクトリに書く)
ARM_PORT = {"A": 8010, "B": 8011}


def post_ask(port, payload, timeout):
    req = urllib.request.Request(
        f"http://localhost:{port}/api/ask",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read().decode()
            return r.status, json.loads(body), time.time() - t0, None
    except urllib.error.HTTPError as e:
        return e.code, {"_raw": e.read().decode()[:4000]}, time.time() - t0, f"HTTP {e.code}"
    except Exception as e:  # timeout / conn reset
        return None, {}, time.time() - t0, f"{type(e).__name__}: {e}"


def one(arm, model, qid, question, timeout, pause):
    port = ARM_PORT[arm]
    payload = {"question": question, "model": model, "corpus": "auto"}
    attempts = []
    for attempt in (1, 2):
        status, resp, wall, err = post_ask(port, payload, timeout)
        attempts.append({"attempt": attempt, "status": status, "wall_s": round(wall, 2), "error": err})
        print(f"  [{arm}/{model}/{qid}] attempt{attempt} status={status} wall={wall:.1f}s err={err}", flush=True)
        if err is None and status == 200:
            break
        if attempt == 1:
            time.sleep(pause * 2)
    rec = {
        "_meta": {
            "arm": arm, "flag_pdf_context": arm == "B", "port": port, "model_id": model,
            "qid": qid, "endpoint": "POST /api/ask", "corpus": "auto",
            "attempts": attempts, "wall_s": attempts[-1]["wall_s"],
            "status": attempts[-1]["status"],
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        },
        "request": payload,
        "response": resp,
    }
    ok = attempts[-1]["error"] is None and attempts[-1]["status"] == 200
    out = (RUNS if ok else RUNS / "failures") / f"{arm}_{model}_{qid}.json"
    out.write_text(json.dumps(rec, ensure_ascii=False, indent=2))
    return ok


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--group", choices=["T", "N"], required=True)
    p.add_argument("--arms", default="A,B")
    p.add_argument("--models", default="opus-5,gpt-terra")
    p.add_argument("--qids", default="")
    p.add_argument("--timeout", type=float, default=900)
    p.add_argument("--pause", type=float, default=5)
    p.add_argument("--out", default="c2r_v3", help="runs/ 配下の出力ディレクトリ名")
    a = p.parse_args()
    global RUNS
    RUNS = EVAL / a.out
    (RUNS / "failures").mkdir(parents=True, exist_ok=True)

    qs = QS[a.group]
    qids = [q.strip() for q in a.qids.split(",") if q.strip()] or list(qs)
    arms = a.arms.split(",")
    models = a.models.split(",")
    n_ok = n_fail = 0
    for arm in arms:
        for model in models:
            for qid in qids:
                if one(arm, model, qid, qs[qid], a.timeout, a.pause):
                    n_ok += 1
                else:
                    n_fail += 1
                time.sleep(a.pause)
    print(f"DONE group={a.group} ok={n_ok} fail={n_fail}", flush=True)
    sys.exit(1 if n_fail else 0)


if __name__ == "__main__":
    main()
