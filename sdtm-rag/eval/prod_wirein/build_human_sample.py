"""对抗抽样与人判包。

⚠ **为什么 5 条抽自 `consistent`**: 人判存在的意义是兜**裁判漏网**, 而漏网按定义
只可能发生在裁判说"干净"的那堆里。只判裁判报警的那些, 结构上测不到漏网 ——
那正是 guardrail v2 那轮真实发生过的失败形状。

⚠ **包里不放 verdict**: 预登记判据写死"人判看答案原文 + 权威表, 不看裁判的 verdict"。
放进去就是把答案提前告诉判卷人, 人判退化成复核裁判。裁判的 `quote` 只用来定位, 故保留。
"""
from __future__ import annotations

import random

_FLAGGED = ("inconsistent", "unsure")


def pick_sample(rows: list[dict], n_consistent: int = 5, n_flagged: int = 3,
                seed: int = 0) -> tuple[list[dict], dict]:
    total = n_consistent + n_flagged
    if len(rows) < total:
        raise ValueError(f"可抽样本不足: 只有 {len(rows)} 条, 需要 {total} 条")
    rng = random.Random(seed)
    clean = [r for r in rows if r["verdict"] == "consistent"]
    flagged = [r for r in rows if r["verdict"] in _FLAGGED]
    take_flagged = min(n_flagged, len(flagged))
    backfilled = n_flagged - take_flagged
    take_clean = n_consistent + backfilled
    if len(clean) < take_clean:
        raise ValueError(f"consistent 一档不足以补满: 有 {len(clean)} 条, 需要 {take_clean} 条")
    sample = rng.sample(clean, take_clean) + rng.sample(flagged, take_flagged)
    comp = {"consistent": take_clean, "flagged": take_flagged, "backfilled": backfilled}
    return sample, comp


def render_human_packet(sample: list[dict], answers_by_id: dict[str, str],
                        authority_md: str) -> str:
    parts = ["# 人判包 — 分类归属 (b) 层", "",
             "> 判据: 无归属断言 ⇒ PASS(N/A) · 有断言且与下表一致 ⇒ PASS · "
             "不一致或权威出处是编的 ⇒ FAIL", "",
             "## 权威表", "", authority_md, "", "## 待判条目", ""]
    for i, r in enumerate(sample, 1):
        parts += [f"### {i}. `{r['id']}`", "",
                  "**裁判定位到的句子** (只用来定位, 不是判定):",
                  "", f"> {r['quote'] or '(裁判未定位到)'}", "",
                  "**答案原文**:", "", answers_by_id.get(r["id"], "(缺)"), "",
                  "**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)", "", "---", ""]
    return "\n".join(parts)
