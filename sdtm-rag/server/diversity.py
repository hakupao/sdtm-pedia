"""检索结果多样性: per-section 配额。

治的是模板化同质簇 —— 63 个域的同名变量行 (DOMAIN / STUDYID / USUBJID / VISIT /
EPOCH …) 正文逐字近似, 对含该字面的问句齐刷刷高分, 会占满 top-k。
q38 实测: top-15 里 14 席是 §DOMAIN, 只剩 1 席给别的内容。

是否启用由证据决定, 见 evidence/checkpoints/crowding_layer2.md。
"""
from __future__ import annotations

from collections import Counter


def apply_section_cap(chunks, cap, exempt_lookup=True):
    """同名 section 最多保留 cap 席, 其余丢弃; 相对顺序不变。cap=None 为恒等。

    section=None 的条目不参与聚簇 (缺元数据不等于同质)。
    via_lookup=True 的条目在 exempt_lookup 下豁免且**不计入**簇计数 ——
    它们是 S1/S2 的确定性 gold 注入, 不属被检验对象。
    """
    if cap is None:
        return list(chunks)
    seen: Counter = Counter()
    out = []
    for c in chunks:
        if exempt_lookup and getattr(c, "via_lookup", False):
            out.append(c)
            continue
        sec = getattr(c, "section", None)
        if sec is None:
            out.append(c)
            continue
        if seen[sec] >= cap:
            continue
        seen[sec] += 1
        out.append(c)
    return out
