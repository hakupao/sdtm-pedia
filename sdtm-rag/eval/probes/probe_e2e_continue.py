"""探针: 真 provider + 真 `/api/ask_stream`, 把天花板压低逼出真实续写。

**证明什么**: 续写在真实 Bedrock 上是不是真的"接着写"(而不是从头重写 / 报错 / 编一个
续写点)。产出全文落盘, 可对接缝做机械核验 (重复行 / 重复标题 / 元话语 / 章节编号连续性),
而不是靠目测说一句"看着挺好"。

**不证明什么**: n=1, 单模型 (opus-5), 单语种 (英文)。别的模型 / 中文答案的接缝未测。

**花费**: 约 1 万到 1.2 万 output token (3 轮 × 4000), 单次运行两三毛钱。

跑法 (cwd = sdtm-rag/):
    .venv/bin/python eval/probes/probe_e2e_continue.py --yes-spend

fake RAG 只为跳过检索 —— 被测的是续写循环, 不是检索。fallbacks 关掉: 回退会换 provider,
那就不是在测 opus-5 了。
"""
from __future__ import annotations

import collections
import json
import re
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from fastapi import FastAPI                            # noqa: E402
from fastapi.testclient import TestClient              # noqa: E402

from eval.probes._spend_gate import require_spend_consent   # noqa: E402
from server.config import Settings, SelectableModel         # noqa: E402
from server.llm_config import create_router                 # noqa: E402
from server.router import api_router                        # noqa: E402


class _FakeRAG:
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        return []

    def format_context(self, chunks):
        return "(No relevant context found in the knowledge base.)"

    def build_messages(self, q, ctx, history=None):
        return [{"role": "user", "content": q}]


Q = ("Write a detailed technical explanation of the CDISC SDTM Vital Signs (VS) domain: "
     "purpose, key variables, and how findings are structured. Aim for 1500 words.")

OUT = Path("/tmp/probe_continue_text.md")


def seam_report(text: str) -> None:
    """接缝的**机械**核验 —— 目测"读起来挺连贯"不是证据。"""
    lines = [ln.strip() for ln in text.split("\n") if ln.strip()]
    dup = [ln for ln, n in collections.Counter(lines).items() if n > 1 and len(ln) > 25]
    heads = [ln for ln in lines if ln.startswith("#")]
    meta = [ln for ln in lines if re.match(
        r"(?i)^(continuing|continued|sorry|apolog|as i was saying|picking up|to continue|resuming)",
        ln)]
    print(f"  行数={len(lines)}  重复长行={len(dup)}  "
          f"标题={len(heads)} (重复 {len(heads) - len(set(heads))})  接缝元话语={len(meta)}")
    for h in heads[:2] + heads[-2:]:
        print(f"    {h[:90]}")


def run(cap: int, rounds: int) -> None:
    base = Settings()
    s = Settings(
        max_continue_rounds=rounds,
        selectable_models=[SelectableModel(**{**m.model_dump(), "max_output_tokens": cap})
                           for m in base.selectable_models],
    )
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = _FakeRAG()
    app.state.settings = s
    router = create_router(s)
    router.fallbacks = []
    router.num_retries = 0
    app.state.llm_router = router

    r = TestClient(app).post("/api/ask_stream", json={"question": Q, "model": "opus-5"})
    events = []
    for block in r.text.split("\n\n"):
        ev = dict(line.split(": ", 1) for line in block.splitlines() if ": " in line)
        if "event" in ev:
            events.append((ev["event"], json.loads(ev.get("data", "{}"))))

    text = "".join(d.get("text", "") for e, d in events if e == "token")
    print(f"\n=== cap={cap}, max_continue_rounds={rounds} ===")
    print(f"continue 事件轮次 : {[d['round'] for e, d in events if e == 'continue']}")
    print(f"error 事件        : {[d for e, d in events if e == 'error']}")
    print(f"正文长度 (chars)  : {len(text)}")
    done = next((d for e, d in events if e == "done"), None)
    print(f"done              : {json.dumps(done, ensure_ascii=False)[:400] if done else None}")
    seam_report(text)
    OUT.write_text(text, encoding="utf-8")
    print(f"全文已存: {OUT}")


if __name__ == "__main__":
    require_spend_consent(__doc__.split("\n\n")[0], "约两三毛钱 (3 轮 × 4000 output token)")
    run(cap=4000, rounds=3)
