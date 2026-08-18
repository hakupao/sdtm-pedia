"""U6 确定性路由信号层 (spec §5.1)。widen-only, 零 LLM, `_ROUTER_SYSTEM` 一字不动。

判库欠账的形态是**漏查一库**: router 判了单库, 而 gold 在另一库 —— 这类失败结构上
捕获不到 (`route_corpus` 只在异常时兜底), 表现为该题 recall 直接归零。本层用两侧各自
已有的确定性件, 在 router 判定之后做一次纠偏, 且**只做 单库 → both**:

- **study 侧信号** (cdisc → both): `StudyLookup.resolve` 结构命中 (label 子串 / OID 段 /
  别名三通道, Plan B Phase 2 的确定性件, 零 LLM)。
- **cdisc 侧信号** (study → both): 标准结构词汇 + CT 码形态 + SDTM 变量形态的词面命中。

只加宽的理由与 `route_corpus` 的兜底同向 (宁可多查不可漏查): 信号判错的最坏代价是多查
一库 (挤占面, 由条款 4/7 exact 半 + 答题侧 spot-check 看住), 而收窄判错的代价是某题
recall 归零且不可恢复。

⚠ 本文件的词表与正则是**标定起点**, 不是终态: Task 9 只拿可见集 (legacy 181 + dev 12)
标定并冻结, 冻结 commit 之后不许再动 (held-out / amb / final 组全程封存, U3 §6.2 三道
防线)。词表纪律 (红线, 同 U3 §6.1): 只许标准结构词汇, **零临床概念** —— 临床词一进来,
本层就从"结构信号"退化成"题面关键词命中", 那正是 U3 判死过的路子。
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from server.study_lookup import StudyLookup

# 拓宽理由白名单 (冻结)。`decide_corpus` 在使用前对照本表校验 —— 信号层返回表外取值
# (典型: 直接返回库名) 时, 不设闸的实现会照样拓宽, 并把该取值写进逐题观测字段, 让下游
# 把它读成一次合法拓宽。新增理由必须同时改本表与 Task 9 的标定记录。
WIDEN_REASONS = ("study_sig", "cdisc_sig")

# 标准结构词汇 (NFKC + 小写归一后比对, 故词条自身必须已是该形态; 见测试的自洽闸)。
# 初版 = Task 9 标定起点。零临床概念 (红线)。
CDISC_STRUCT_TERMS = (
    "sdtm",
    "cdisc",
    "マッピング",
    "どの変数",
    "対応する変数",
    "どのドメイン",
    "controlled terminology",
    "提出データ",
)

# 边界不能用 \b: 日文题面里形态紧贴假名 (AESEVは / C12345に), 而 Python 的 \w 含 CJK,
# 那个位置上 \b 不成立 —— 整条正则会在真实题面上静默失灵 (study_lookup.py 同一坑)。
# 只把 ASCII 字母/数字/下划线当作阻断邻居。
_CT_CODE_RE = re.compile(r"(?<![A-Za-z0-9_])C\d{5,6}(?![A-Za-z0-9_])")      # NCI C-code
# SDTM 变量形态 (如 AESEV): 4-8 位大写拉丁。两字母裸域码 (DM/AE/VS) 刻意不收 —— 它们
# 在日文题面里与缩写噪声不可分, 收进来等于对一大批题无条件拓宽。
_DOMAIN_VAR_RE = re.compile(r"(?<![A-Za-z0-9_])[A-Z]{4,8}(?![A-Za-z0-9_])")


def _nfkc(s: str) -> str:
    """全角/半角归一。日文输入法产出的 ＡＥＳＥＶ 与 AESEV 必须同判。"""
    return unicodedata.normalize("NFKC", s)


def _norm(s: str) -> str:
    """词表比对用归一化: NFKC + 小写。"""
    return _nfkc(s).lower()


class RoutingSignals:
    """双向确定性信号。`widen_reason` 是唯一出口, 返回值恒在 `WIDEN_REASONS` 或 None。"""

    def __init__(self, study_lookup):
        # 生产侧必须传 lifespan 已构造的那一份 (不再造第二份): 两份可以来自不同文件,
        # 而信号层用的那份从不出现在任何日志里, 不一致会一路静默到评测数字上。
        self.study_lookup = study_lookup

    def _study_signal(self, question: str) -> bool:
        r = self.study_lookup.resolve(question)
        # form_scopes 也算命中: 通道③ (别名 → form scope) 不产 cards, 只看 cards
        # 会让别名命中这一整条通道对信号层静默失效。
        return bool(r.cards or r.form_scopes)

    def _cdisc_signal(self, question: str) -> bool:
        q = _nfkc(question)
        ql = q.lower()
        return (
            any(t in ql for t in CDISC_STRUCT_TERMS)
            or bool(_CT_CODE_RE.search(q))
            or bool(_DOMAIN_VAR_RE.search(q))
        )

    def widen_reason(self, routed: str, question: str) -> str | None:
        """判库结果 + 原问句 → 拓宽理由 (或 None = 不拓宽)。

        只问**对侧**信号: routed=cdisc 时 study 信号才有意义 (cdisc 信号只会把 cdisc
        拓宽成 cdisc), 反之亦然。`both` 与任何表外取值一律沉默 —— 本层永不收窄也不换库。
        """
        if routed == "cdisc" and self._study_signal(question):
            return "study_sig"
        if routed == "study" and self._cdisc_signal(question):
            return "cdisc_sig"
        return None


def build_signals(settings, study_lookup=None) -> RoutingSignals:
    """生产与 eval 同源工厂。**永不返回 None** —— 装不上就抛。

    None 在调用侧的语义是"信号层未装配": `eval/run_routing_eval.py --signal-layer on`
    拿到 None 会 SystemExit, 因为那批数字的 meta 仍写着 "on", 会被当成"信号层开着"的
    证据引用。所以这里用异常表达失败, 把原因 (哪个路径不在) 一并带出。

    `study_lookup` 传入时直接复用 (生产接线走这条: lifespan 已按 study_lookup_enabled
    构造过一份); 不传才按 settings 自行加载 (eval / 独立跑批)。
    """
    if study_lookup is None:
        catalog = Path(settings.study_catalog_path)
        if not catalog.exists():
            raise FileNotFoundError(
                f"study catalog not found: {catalog} (settings.study_catalog_path) — "
                "信号层的 study 半边没有数据源, 拒绝半装配"
            )
        # 别名表缺失是 S2 刻意的优雅降级 (通道③ 空转), 不升级成硬失败。
        study_lookup = StudyLookup.from_paths(catalog, settings.study_aliases_path)
    return RoutingSignals(study_lookup)
