"""Per-call cost estimation for the multi-model compare badges (DEPLOY_PLAN §3 T3 / §9).

A small EXPLICIT price table (USD per 1M tokens, 2026-06) is the authoritative source
for the models DEPLOY_PLAN §9 lists; for anything else we ask litellm.completion_cost.
An unknown model returns None so the badge shows "—" rather than a wrong number or a
crash (§9: "表中没有的模型，badge 成本显示 '—' 而非报错").

cost is an ESTIMATE for a localhost dev badge, not billing: a wrong code in an answer
is a serious defect, a slightly-off cost badge is not. Honesty rule still applies — we
never fabricate a number for a model we cannot price; we return None and the UI shows "—".
"""
from __future__ import annotations

# USD per 1M tokens, (input, output). Source: DEPLOY_PLAN §9 (2026-06, authoritative
# rows from Anthropic / DeepSeek official). Keys are the normalized model id (provider
# prefix stripped, lowercased). Only rows §9 states are hardcoded; do NOT guess prices
# for models §9 does not list — those fall through to litellm, then to None.
_PRICES: dict[str, tuple[float, float]] = {
    "claude-sonnet-4-6": (3.00, 15.00),
    "claude-opus-4-7": (5.00, 25.00),
    "claude-haiku-4-5": (1.00, 5.00),
    "deepseek-v4-pro": (0.435, 0.87),
}


def _normalize(model: str) -> str:
    """Strip a litellm provider prefix and lowercase. 'anthropic/Claude-Sonnet-4-6'
    -> 'claude-sonnet-4-6'. A bare 'gpt-4o' is returned unchanged (lowercased)."""
    return model.split("/", 1)[-1].strip().lower()


def _table_price(model: str) -> tuple[float, float] | None:
    """Look the model up in the explicit §9 table. Tries an exact normalized match
    first, then a containment match so a dated/suffixed string
    ('claude-sonnet-4-6-20260514') still resolves to its base row. Returns None when
    the model is not in the table (caller then tries litellm, then gives up to None)."""
    norm = _normalize(model)
    if norm in _PRICES:
        return _PRICES[norm]
    # Prefix-anchored, most-specific (longest key) first: a dated suffix like
    # 'claude-sonnet-4-6-20260514' still resolves to its base row, but a future
    # 'claude-haiku-4-5-turbo' cannot silently borrow the 'claude-haiku-4-5' price
    # via a loose substring match.
    for key in sorted(_PRICES, key=len, reverse=True):
        if norm.startswith(key):
            return _PRICES[key]
    return None


def estimate_cost(model: str, usage: dict | None) -> float | None:
    """Estimate the USD cost of one completion.

    Returns a float, or None when it cannot be priced honestly:
      - no usage / no token counts          -> None  (nothing to price)
      - model in the §9 table               -> exact arithmetic from token counts
      - otherwise litellm.completion_cost   -> its number if > 0
      - all of the above fail               -> None  ("—" in the UI, never a guess)
    """
    if not usage:
        return None
    prompt_tokens = usage.get("prompt_tokens")
    completion_tokens = usage.get("completion_tokens")
    if prompt_tokens is None and completion_tokens is None:
        return None
    pt = int(prompt_tokens or 0)
    ct = int(completion_tokens or 0)

    table = _table_price(model)
    if table is not None:
        in_rate, out_rate = table
        return round(pt / 1_000_000 * in_rate + ct / 1_000_000 * out_rate, 6)

    # Not in §9's table — ask litellm's own (frequently-updated) price map via
    # cost_per_token (model, prompt_tokens, completion_tokens) -> (in_cost, out_cost).
    # It raises for models it doesn't know; we swallow that and return None rather than
    # fabricate a number for a model we cannot price honestly.
    try:
        import litellm

        in_cost, out_cost = litellm.cost_per_token(
            model=model, prompt_tokens=pt, completion_tokens=ct
        )
        total = (in_cost or 0.0) + (out_cost or 0.0)
        if total > 0:
            return round(float(total), 6)
    except Exception:  # noqa: BLE001 — unknown model / litellm internal: degrade to "—"
        pass
    return None
