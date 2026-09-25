"""DM2: 研读包要不要挂 —— 纯函数, 零 LLM (与 pdf_trigger 同一纪律: 可枚举可复现).

spec §4. 范围词是**词类** (研究指代 + study/試験/研究), 不是某题的字面; 不加表单名/项目名.
裸 "EDC"/"in our\b" 已收紧 (fix round 1): EDC 需搭配 study/trial/研究 锚定才算范围词, 否则纯 CDISC 定义题
(如 "What is EDC in SDTM terms?") 会误触发.
英文分支加 `\b` 词边界 (fix round 2, DM2 T8 attempt 1): 无边界时 "f<our Trial>" 之类跨词边匹配会误触发
(见 evidence/failures/dm2_task8_attempt_1.md, q29 "the four Trial Design domains..."); CJK 分支与
`本 ?study` 保持不加 `\b` (`\b` 在 CJK 字符边界上行为不可靠).
域码识别注入 (D1 `_query_domains`), 这里不重写正则.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, Literal

DossierMode = Literal["auto", "on", "off"]

_SCOPE_RE = re.compile(
    r"本研究|本試験|当試験|当研究|この試験|この研究|本 ?study"
    r"|\bour study\b|\bthis study\b|\bour trial\b|\bthis trial\b"
    r"|\bin (?:our|this) (?:study|trial|research)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class DossierDecision:
    attach: bool
    reason: str
    domains: tuple[str, ...] = ()


def decide_dossier(question: str, mode: DossierMode, enabled: bool,
                   query_domains: Callable[[str], list[str]],
                   auto_attach: bool = True) -> DossierDecision:
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
        if not auto_attach:  # 命中但暂停: 报出来, 让用户知道可以手动 on
            return DossierDecision(False, "auto:paused", domains)
        return DossierDecision(True, "auto:domain+scope", domains)
    return DossierDecision(False, "auto:no_match", domains)


# ── 答题语言 (attempt 4 → 5) ─────────────────────────────────────────
# 研读包 13 万字以日文为主, system 里的「跟问句语言」两轮压不住 (evidence/failures/
# dm2_task9_attempt_4.md: sonnet en 问 → ja 答)。改为按问句**文字种类**确定语言, 由 router 在
# 最后一条 user 消息末尾追加一行 —— 离生成最近, 且是确定值不是让模型自己判断。
# 仮名があれば ja (漢字だけでは zh/ja を区別できない); 漢字のみ ⇒ zh; どちらもなし ⇒ en.
_KANA_RE = re.compile(r"[぀-ヿ]")
_HAN_RE = re.compile(r"[一-鿿]")

ANSWER_LANGUAGE_LINE = {
    "ja": "【回答言語】日本語で回答すること (OID・SDTM 変数名・CT 値・固定標記はそのまま)。",
    "zh": "【回答语言】请用中文回答 (OID、SDTM 变量名、CT 取值、固定标记保持原样)。",
    "en": "[Answer language] Answer in English (keep OIDs, SDTM variable names, CT values and "
          "fixed markers as written).",
}


def answer_language(question: str) -> str:
    if _KANA_RE.search(question):
        return "ja"
    if _HAN_RE.search(question):
        return "zh"
    return "en"
