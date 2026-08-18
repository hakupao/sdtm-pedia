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

⚠ 词表与正则已由 Task 9 在可见集 (legacy 181 + dev 12) 上标定并**冻结**, 此后不许再动
(held-out / amb / final 组全程封存, U3 §6.2 三道防线); 证据与轮次表见
`evidence/u6_task9_calibration.md`。词表纪律 (红线, 同 U3 §6.1): 只许标准结构词汇,
**零临床概念** —— 临床词一进来, 本层就从"结构信号"退化成"题面关键词命中", 那正是 U3
判死过的路子。

⚠ **未解阻断** (Task 9 §5, 交 controller): 上面 study 侧那条"`resolve` 有任何命中即算信号"
在可见集上误触 6 道纯标准题 (150 道 cdisc 判定题的 4.0%), 每触 −1 exact ⇒ 模拟 legacy
exact 173 < 冻结阈值 178。误触 6/6 全部来自 `resolve` 的通道②b (单个大写 token 撞上某个
item OID 段) —— 本研究 EDC 的 OID 段沿用 SDTM 风味命名, 于是一道纯标准题里的变量名会精确
撞段。收紧到强通道 (① label / ②a 多 token 交集 / ③ 别名) 的反事实已实测: 可见集 widen 0 次、
两信号仍活。该改动**不是**词表改动, 不在 Task 9 旋钮内, 故未做。
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

# 方向表: 每个单库判定只有**一个**合法拓宽理由 —— 拓宽的依据永远是**对侧**信号
# (cdisc 判定要 study 侧证据才值得多查 study 库, 反之亦然)。同侧理由 (cdisc 判定 +
# cdisc 信号) 不是"更强的确认", 而是无依据的拓宽: 它对每道 router 判对的单库题都成立,
# 等于把 auto 档整体推成 both。白名单只管"取值合法", 方向表管"这个取值配不配这道判定";
# 两者由测试钉成同一份 (值集 == WIDEN_REASONS)。
WIDEN_REASON_BY_CORPUS = {"cdisc": "study_sig", "study": "cdisc_sig"}

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
# SDTM 变量形态 (如 AESEV): 锚定到**公开标准的词表**, 不是"任意 4-8 位大写"。
# 起点版 (Task 8) 写的是 [A-Z]{4,8}, 它在 study 侧题面上大量误触 —— 试验缩写 (方案名 /
# 評価尺度名 / システム名) 与 NFKC 把罗马数字归一出来的大写串都是 4-8 位大写, 而它们与
# 标准结构毫无关系。Task 9 可见集标定实测: 起点版在 legacy 的 study 侧题上误触 6 题
# (证据 evidence/u6_task9_calibration.md §3), 每一触都是 −1 exact。
#
# 词源全部是**公开**件 (knowledge_base/, 进 git), 零 study 内容、零临床概念词; 三份表
# 均由下面这条命令从 VARIABLE_INDEX.md 机械派生, 可逐字复算 (复算命令见 evidence §2):
#   域码 = 域目录名 ∪ §2 域小节头; 词根 = §2 中以本域域码开头的变量去掉域码后的余段;
#   单独变量 = §1/§2 全部变量里不被"域码+词根"覆盖且 ≥4 位的那些 (CT 码另由 _CT_CODE_RE 管)。
# **冻结**: Task 9 标定结束后不许再改 (Task 10 全闸以此版为准)。
# 两字母域码 (knowledge_base/domains/ 的目录名 ∪ VARIABLE_INDEX.md §2 的域小节头)。
_SDTM_DOMAIN_CODES = (
    "AE", "AG", "BE", "BS", "CE", "CM", "CO", "CP", "CV", "DA", "DD", "DI", "DM", "DS", "DV",
    "EC", "EG", "EX", "FA", "FT", "GF", "HO", "IE", "IS", "LB", "MB", "MH", "MI", "MK", "ML",
    "MS", "NV", "OE", "OI", "PC", "PE", "PP", "PR", "QS", "RE", "RP", "RS", "SC", "SE", "SM",
    "SR", "SS", "SU", "SV", "TA", "TD", "TE", "TI", "TM", "TR", "TS", "TU", "TV", "UR", "VS",
)

# `--` 词根: VARIABLE_INDEX.md §2 里**以本域域码开头**的变量去掉域码后的余段 (≥3 位)。
# 归属自己域是关键: 按「任意两字母前缀」切会切出 SUBJID→BJID 这类假词根。
_SDTM_VAR_ROOTS = (
    "ABCLID", "ACN", "ACNDEV", "ACNOTH", "ACPTFL", "ADJ", "AGENT", "ANCVAR", "ANMETH", "ANTREG",
    "BDAGNT", "BDSYCD", "BEATNO", "BLFL", "BODSYS", "BRANCH", "CAT", "CELSTA", "CHROM", "CLAS",
    "CLASCD", "CLSIG", "CNDAGT", "CNTMOD", "COLSRT", "CONC", "CONCU", "CONTRT", "COPYID",
    "CSMRKS", "DECOD", "DEF", "DIR", "DOSE", "DOSFRM", "DOSFRQ", "DOSRGM", "DOSTOT", "DOSTXT",
    "DOSU", "DRVFL", "DTC", "DUR", "ELTM", "ENDTC", "ENDY", "ENINT", "ENRF", "ENRL", "ENRTPT",
    "ENTPT", "EPCHGI", "EVAL", "EVALID", "EVDTYP", "EVINTX", "EVLINT", "FAST", "GATDEF", "GATE",
    "GENLOC", "GENREF", "GENSR", "GRPID", "HLGT", "HLGTCD", "HLT", "HLTCD", "INDC", "INHERT",
    "LAT", "LEAD", "LLOD", "LLOQ", "LLT", "LLTCD", "LNKGRP", "LNKID", "LOBXFL", "LOC", "LOINC",
    "LOT", "MAXPAI", "METHOD", "MINPAI", "MODIFY", "MOOD", "MRKSTR", "MSCBCE", "NAM", "NRIND",
    "NUMRPT", "OBJ", "OCCUR", "ORDER", "ORNRHI", "ORNRLO", "ORREF", "ORRES", "ORRESU", "OUT",
    "PARM", "PARMCD", "PARTY", "PATT", "PDUR", "PORTOT", "POS", "PRESP", "PRTYID", "PSTRG",
    "PSTRGU", "PTCD", "PTFL", "PVRID", "REASND", "REASOC", "REF", "REFID", "REL", "RELNST",
    "REPNUM", "RESCAT", "RESSCL", "RESTYP", "RFTDTC", "RLDEV", "RLPRC", "RLPRT", "ROUTE", "RPT",
    "RSDISC", "RUNID", "SBMRKS", "SCAN", "SCAT", "SCONG", "SDISAB", "SDTH", "SEQ", "SEQID",
    "SER", "SEV", "SHOSP", "SINTV", "SLIFE", "SMIE", "SOC", "SOCCD", "SOD", "SPCCND", "SPCUFL",
    "SPEC", "SPID", "SPTSTD", "STAT", "STDTC", "STDY", "STINT", "STNRC", "STNRHI", "STNRLO",
    "STOFF", "STREFC", "STREFN", "STRESC", "STRESN", "STRESU", "STRF", "STRL", "STRTPT",
    "STTPT", "SYM", "SYMTYP", "TERM", "TEST", "TESTCD", "TGTPAI", "TMTHSN", "TOX", "TOXGR",
    "TPT", "TPTNUM", "TPTREF", "TRANS", "TRT", "TSTCND", "TSTDTL", "TSTOPO", "TSTPNL", "ULOQ",
    "UNANT", "UPDES", "VAL", "VALCD", "VALNF", "VCDREF", "VCDVER", "VERS", "XFN",
)

# 不走 `--` 组合的标准变量 (§1 共通变量 + 各域里前缀非本域码的那些, ≥4 位, 去掉 CT 码)。
_SDTM_STANDALONE_VARS = (
    "ACTARM", "ACTARMCD", "ACTARMUD", "AGEU", "ARMCD", "ARMNRS", "BRTHDTC", "BSDY", "CEDY",
    "CODY", "COUNTRY", "CPDY", "CVDY", "DADY", "DDDY", "DMDY", "DOMAIN", "DSDY", "DTHDTC",
    "DTHFL", "EGDY", "ELEMENT", "EPOCH", "ETCD", "ETHNIC", "FADY", "FOCID", "FTDY", "GFDY",
    "HODY", "IDVAR", "IDVARVAL", "IEDY", "INVID", "INVNAM", "ISDY", "LBDY", "LEVEL", "MBDY",
    "MHDY", "MIDS", "MIDSDTC", "MIDSTYPE", "MIDY", "MKDY", "MLDY", "MSDY", "NHOID", "NVDY",
    "OEDY", "PARENT", "PCDY", "PEDY", "POOLID", "PPDY", "QEVAL", "QLABEL", "QNAM", "QORIG",
    "QSDY", "QVAL", "RACE", "RDOMAIN", "REDY", "REFID", "RELID", "RELMIDS", "RELTYPE",
    "RFCENDTC", "RFCSTDTC", "RFENDTC", "RFICDTC", "RFPENDTC", "RFSTDTC", "RFXENDTC", "RFXSTDTC",
    "RPDY", "RSDY", "RSUBJID", "SCDY", "SITEID", "SPDEVID", "SPEC", "SRDY", "SREL", "SSDY",
    "STUDYID", "SUBJID", "TAETORD", "TIRL", "TRDY", "TUDY", "URDY", "USUBJID", "VISIT",
    "VISITDY", "VISITNUM", "VSDY",
)


def _alt(words: tuple[str, ...]) -> str:
    """词表 → 正则交替式。长词优先: 短词条先匹上会让尾部的负向前瞻失败 (AESTDTC 先吃到
    短词根那种), re 照样回溯出同一结果, 排序只是省掉那一轮回溯。"""
    return "|".join(sorted(words, key=len, reverse=True))


_DOMAIN_VAR_RE = re.compile(
    rf"(?<![A-Za-z0-9_])(?:(?:{_alt(_SDTM_DOMAIN_CODES)})(?:{_alt(_SDTM_VAR_ROOTS)})"
    rf"|{_alt(_SDTM_STANDALONE_VARS)})(?![A-Za-z0-9_])"
)


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
