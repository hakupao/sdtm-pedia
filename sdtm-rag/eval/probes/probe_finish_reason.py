"""探针: 真实 provider 被输出上限切断时, 流式 chunk 的 `finish_reason` 到底写什么?

**证明什么**: `server/router.py` 的 `_TRUNCATED_FINISH_REASONS = {"length", "max_tokens"}`
是从文档推的。推错的表现是**截断照旧静默** —— 与修复前一样, 不会更糟, 但也没修好。
这条探针把每个 provider 真正报出来的字符串抄下来, 并当场判它认不认。

**不证明什么**: 只覆盖这里列出的三个组。别的 provider 报第三种拼法, 这里看不到。

**花费**: 3 次调用 × 200 output token, 约几分钱。

跑法 (cwd = sdtm-rag/):
    .venv/bin/python eval/probes/probe_finish_reason.py --yes-spend

做法: per-call 传一个**很小**的 max_tokens (覆盖 deployment 级的天花板), 问一个必然写很长
的问题, 把每个 chunk 的 finish_reason 抄下来。
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from eval.probes._spend_gate import require_spend_consent      # noqa: E402
from server.config import Settings                              # noqa: E402
from server.llm_config import create_router                     # noqa: E402
from server.router import _TRUNCATED_FINISH_REASONS             # noqa: E402

GROUPS = ["opus-5", "gpt-terra", "default-fallback"]
Q = ("Write a detailed, multi-section technical essay of at least 3000 words about the "
     "CDISC SDTM Vital Signs (VS) domain. Do not stop early.")


async def main() -> None:
    router = create_router(Settings())
    router.fallbacks = []      # 回退会换成另一个 provider, 那就不是在测这一个了
    router.num_retries = 0

    for g in GROUPS:
        reasons: list[str] = []
        chars = 0
        try:
            resp = await router.acompletion(
                model=g, messages=[{"role": "user", "content": Q}],
                stream=True, max_tokens=200)   # per-call 压低, 逼出触顶
            async for ch in resp:
                choices = getattr(ch, "choices", None)
                if not choices:
                    continue
                fr = getattr(choices[0], "finish_reason", None)
                if fr:
                    reasons.append(fr)
                chars += len(getattr(choices[0].delta, "content", None) or "")
            last = reasons[-1] if reasons else None
            print(f"{g:<18} chars={chars:<6} finish_reasons={reasons} "
                  f"-> 被判为触顶: {last in _TRUNCATED_FINISH_REASONS}")
        except Exception as e:  # noqa: BLE001
            print(f"{g:<18} FAIL {type(e).__name__}: {str(e)[:200]}")


if __name__ == "__main__":
    require_spend_consent(__doc__.split("\n\n")[0], "约几分钱 (3 次调用 × 200 output token)")
    asyncio.run(main())
