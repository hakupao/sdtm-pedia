"""DM2: 研读包要不要挂 —— 纯函数, 零 LLM (与 pdf_trigger 同一纪律: 可枚举可复现).

spec §4. 范围词是**词类** (研究指代 + study/試験/研究 / EDC), 不是某题的字面; 不加表单名/项目名.
域码识别注入 (D1 `_query_domains`), 这里不重写正则.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, Literal

DossierMode = Literal["auto", "on", "off"]

_SCOPE_RE = re.compile(
    r"本研究|本試験|当試験|当研究|この試験|この研究|本 ?study|our study|this study|in our\b|EDC",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class DossierDecision:
    attach: bool
    reason: str
    domains: tuple[str, ...] = ()


def decide_dossier(question: str, mode: DossierMode, enabled: bool,
                   query_domains: Callable[[str], list[str]]) -> DossierDecision:
    if not enabled:
        return DossierDecision(False, "disabled")
    if mode == "off":
        return DossierDecision(False, "forced_off")
    if mode == "on":
        return DossierDecision(True, "forced_on")
    try:
        domains = tuple(query_domains(question))
    except Exception:  # noqa: BLE001 — 识别炸了 = 不触发, 不是 500
        domains = ()
    if domains and _SCOPE_RE.search(question):
        return DossierDecision(True, "auto:domain+scope", domains)
    return DossierDecision(False, "auto:no_match", domains)
