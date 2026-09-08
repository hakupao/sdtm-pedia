"""探针: 配置里的 `max_tokens` 天花板, provider 收不收?

**证明什么**: 八个 Router 组各发一次最短请求, 带着自己 deployment 级的 `max_tokens`。
provider 接受 ⇒ 那个天花板可用; 拒绝 ⇒ 错误原文里通常写着允许的上限, 照着下调即可。
`gpt-terra` / `gpt-sol` 的 128000 **没有一手文档背书** (只有 litellm 静态表), 这条探针
就是它们唯一的实证。

**不证明什么**: provider 接受一个参数值 ≠ 模型真的能吐满那么多 token。

**花费**: 8 次调用 × 每次几个 token, 约几分钱。

跑法 (cwd = sdtm-rag/):
    .venv/bin/python eval/probes/probe_max_tokens.py --yes-spend

刻意用 `create_router(Settings())` 而不是裸 litellm: 测的必须是**生产真正会用的那条路**
(含 .env 覆盖后的模型串 + deployment 级 max_tokens), 不是一个长得像的近似物。
fallbacks 关掉 —— 否则某个 deployment 被拒会静默落到 DeepSeek 上答成功, 探针就报了个
假绿 (正是它要证伪的那件事)。
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from eval.probes._spend_gate import require_spend_consent  # noqa: E402
from server.config import Settings                          # noqa: E402
from server.llm_config import create_router                 # noqa: E402

GROUPS = ["opus-5", "sonnet-5", "gpt-terra", "gpt-sol", "default", "default-fallback",
          "hard", "light"]


async def main() -> None:
    s = Settings()
    router = create_router(s)
    router.fallbacks = []      # 见 docstring: 回退会把"被拒"伪装成"成功"
    router.num_retries = 0

    caps = {d["model_name"]: (d["litellm_params"]["model"],
                              d["litellm_params"].get("max_tokens"))
            for d in router.model_list}

    print(f"{'group':<18} {'max_tokens':>10}  result")
    print("-" * 100)
    for g in GROUPS:
        model, cap = caps[g]
        try:
            r = await router.acompletion(
                model=g, messages=[{"role": "user", "content": "Reply with the single word OK."}])
            text = (r.choices[0].message.content or "").strip().replace("\n", " ")[:40]
            print(f"{g:<18} {cap:>10}  OK  [{model}] -> {text!r}")
        except Exception as e:  # noqa: BLE001 — 探针要的就是把错误原文抄下来
            print(f"{g:<18} {cap:>10}  FAIL [{model}] {type(e).__name__}: {str(e)[:220]}")


if __name__ == "__main__":
    require_spend_consent(__doc__.split("\n\n")[0], "约几分钱 (8 次极短调用)")
    asyncio.run(main())
