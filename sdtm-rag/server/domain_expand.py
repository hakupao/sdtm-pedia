"""DM1 D3 — deterministic domain-code query expansion (retrieval side only).

A question like「sdtm 的 ds domain」carries one informative token, a 2-letter
code that is nearly invisible to both the embedding and BM25. Appending the
domain's official label from meta.yaml gives dense and lexical search a real word
to match ("Disposition") without an LLM and without rewriting what the user asked.
The expanded text is used for retrieval only; the LLM still sees the original question.

⚠ **label only, no structure** —— meta.yaml 的 `structure` 字段 ("One record per ... per
subject") 是**跨域通用**的记录粒度模板。attempt 1 把它一起追加, 实测 140q 的 q47 从
recall 1.0 掉到 0.5: 那段散文让"讲记录粒度的块" (AE/PC 的 assumptions、ch03) 在稠密与
BM25 两侧一起上浮, 把问句真正问的 QS 自己的 assumptions 挤出 15 席
(evidence/failures/dm1_task5_attempt_1.md)。label 是域**专属**的词, structure 不是 ——
扩写只该加前者。

⚠ 追加的是**散文** (域的正式名), 不是变量名或码。S1/S2 的 resolve 是 token 级的,
让它们看见追加段会凭空多出域/长名命中 —— 故 `retrieve` 只把扩写文本喂稠密/BM25
(见 rag.py `q_ret`), 直查通道恒收原句。
"""
from __future__ import annotations

from server.meta_store import MetaStore
from server.structured_lookup import StructuredLookup

_MAX_DOMAINS = 3


class DomainExpander:
    def __init__(self, store: MetaStore, lookup: StructuredLookup):
        self._store = store
        self._lookup = lookup

    def expand(self, query: str) -> str:
        parts: list[str] = []
        for code in self._lookup._query_domains(query)[:_MAX_DOMAINS]:
            # 两份数据源: 识别走 domain_to_spec (KB 目录树), 取值走 meta.yaml。一边有而
            # 另一边没有时 domain_info 返回 None —— 跳过, 不炸请求。
            info = self._store.domain_info(code) or {}
            label = (info.get("label") or "").strip()
            if not label:
                continue
            parts.append(label)
        return f"{query} {' '.join(parts)}" if parts else query


def build_expander(s) -> DomainExpander:
    """按 `s` (Settings) 的路径装配一台扩写器。开关 `domain_expand_enabled` 由各装配点
    自己判 —— 本函数只管"怎么造", 不管"造不造"。

    ⚠ 恒用 `s.kb_root` / `s.meta_path`, **不跟随** run_eval 的 `--kb-root` 覆盖: 域码表
    是 CDISC 的词汇表, 不是被检索语料的属性。跟着 `--kb-root` 走时, 48 题 study 尺子
    (`--kb-root data/study/st01/cards`, 树里没有 domains/) 会建出一张空域表 ⇒ 扩写恒不
    触发, 而生产的 study 引擎 (kb_root 取 settings) 是触发的 —— 尺子全绿而量的是另一台
    引擎, 正是本仓 Task 3b 花力气消灭的那种漂移。

    三条路径共用本装配点: server/main.py (生产)、eval/run_eval.py (尺子)、
    eval/prod_wirein/check_code_grounding.py (按落盘 lever 重建)。
    """
    store = MetaStore(s.meta_path)
    return DomainExpander(store, StructuredLookup(s.kb_root, store))
