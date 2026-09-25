"""DM2 研读包答案 生成后确定性闸 —— 纯函数, 零 LLM, 可枚举。

spec: docs/superpowers/specs/2026-09-25-dossier-output-gate-design.md (§2 闸定义, §3 编排, §4 回放)。
只在研读包挂上时跑: B 部是穷尽一览, 「不在一览 = 不存在」只在那时成立。

G-OID —— 只在「OID 断言」的位置取 token (`[A-Z][A-Z0-9_]{1,}`), 其余散文里的大写词一概不看:
  (引用 span 内槽以外的纯 token 括号: 半严格, 不在一览也不在宽白名单即计; 槽之后的还须像 OID。
   两段方括号 (非引用头) 的末段: 窄集 + SDTM 变量名放行。)
  严格位 —— 只认一览里的 OID 与列表简写端点, **不**套宽白名单 (SDTM 名 / 族前缀 / 缩写):
    · 表单槽: `[名称 FORM]` (方括号里 ≥2 段、末段是 token) 或 `[FORM] label (OID)` 引用的方括号;
    · 项目槽: `[…] label (OID)` 里第一个含真实 OID 的纯 token 括号; 没有则取最后一个纯 token 括号
      (label 自己可能带 `(缩写)`, 捏造的 OID 通常在最后)。
    槽里是列表且含真实 OID 时, 其余成员只有「像 OID」才计 (`(真实OID, HIV)` 里的缩写不计)。
  宽松位 (单 token 方括号 / 反引号 / 其它括号里的纯 token 列表): 先过宽白名单, 再只计「像 OID」的 ——
    · 与同列表里某个真实 OID 共享 ≥3 字符前缀 (同一列表 = 同一类断言, 编造的兄弟);
    · 词干 (前导字母段) 与一览里某个 OID 的词干相同, 且带数字或下划线 (自造编号/后缀的「补全」)。
  全文 (唯一例外, 偏离 §2「窄提取」, 由 §4 预期迫使): `<前缀>_<真实表单 OID>` 形态的未知 token ——
    规则句 ③ 明令禁止给 OID 加前缀, 而这类捏造在回放里出现在表格裸文本中, 窄提取看不到。
    表单 OID 恰是 SDTM 域码时不扫 (`RAW_AE` 之类说的是数据集, 不是表单)。
  宽白名单 (只给宽松位): SDTM 变量名 / 域码 (KB `domains/*/spec.md` 的 `### VAR` + 目录名)、SUPP+域码、
  NCI C 码、常见缩写、族前缀 (一览中有以其为前缀的成员)。占位写法 (含小写 n/x 或 `*`) 本来就不被切出。

G-LANG —— 去掉反引号 / `[…] label (OID)` 引用 / 其余方括号 / 「」『』引文 / markdown 表格行 / 固定
  标记后: 正文 (去空白) < MIN_BODY_CHARS ⇒ 不判 (lang_observed=None, 不计入 ok); 否则
  (仮名+漢字) ≤ 拉丁词数 ⇒ en; 否则 ja 信号比 ≥ JA_SIGNAL_RATIO ⇒ ja, 不然 zh。
  ja 信号 = 平仮名 + 片仮名 + 「日本字形漢字」(不在 GB2312 简体字符集里的漢字: 項/対/応/単/領…),
  分母 = 仮名 + 全部漢字。只数平仮名的旧口径把体言止め列表、见出し多的日文 (几乎无平仮名) 判成 zh。
  §4 回放校准 (42 份, 去除后): 正文最短 1364 字; en 的 (仮名+漢字)/拉丁词 ≤ 0.38, CJK 答案 ≥ 3.83;
  ja 信号比: zh ≤ 0.108, ja ≥ 0.627; 复审构造: 夹未加引号日文 label 的中文 0.167, 体言止め列表 0.47,
  见出し多 0.50 ⇒ 阈值 0.3, 安全带 [0.167, 0.47] (仅回放为 [0.108, 0.627])。

空答案一律不过。

已知限制 (漏报形态, 回放里都没出现, 修它们要付更多假阳性, 本单元不做):
  · M3 纯字母、与一览 OID 只差几个字母的单独反引号 token (无数字/下划线, 词干规则不看);
  · M5 markdown 表格单元格里的裸 OID; M6 粗体 (`**X**`) 里的裸 OID —— 都不是规则句规定的引用形态;
  · M10 给真实表单 OID 加**后缀**的裸 token (前缀形态才全文扫);
  · 词干规则对本研究命名习惯敏感: 与一览同词干、差一个字母的 SDTM 侧取值 (如 --TESTCD 示例) 靠
    「词干不同」才没被误标 —— 换一个命名习惯的研究可能翻转;
  · G-LANG 把「不在 GB2312 的漢字」当日文信号: 繁体中文答案会被判成 ja (本研究问答不用繁体);
  · 闸假设 item OID 在全研究内唯一 (一览按 OID 集合比对); 换研究时若有跨表单复用, 启动一致性检查
    (items 数 ≠ 研读包条数) 会关闭闸, /api/info dossier_gate=false 可见 —— runbook 须写明;
  · 引用 span 里**槽之后**的括号只计「像 OID」的 (与一览共享 ≥3 字符前缀 / 带数字下划线): 新词干的
    纯字母捏造 (与一览无共同前缀) 出现在槽后会漏报 —— 换来槽后散文里 (UNK)/(TBD)/(BID) 不误报;
  · 项目槽在「无真实 OID」时取引用后最后一个括号: 捏造 OID 后面再接带大写缩写括号的散文时,
    槽会落到散文的括号上 (捏造的那个转由宽松位判定, 只在像 OID 时才计)。
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from server.dossier_trigger import ANSWER_LANGUAGE_LINE, answer_language

MIN_BODY_CHARS = 200      # 去引文后正文少于这么多 (非空白) 字 ⇒ G-LANG 不判: 样本太小, 比例不稳
JA_SIGNAL_RATIO = 0.3     # (仮名+日本字形漢字)/(仮名+漢字) 的 ja 阈值; 安全带 [0.167, 0.47]
REGEN_BUDGET = 1  # 重答上限 (spec §3): 再一次 ~150K prompt 全价调用, 不做第二次

# spec 点名的缩写 + 同类的标准/文档缩写。⚠ 只放「不可能是 EDC OID 的通用缩写」, 不放任何回放里
# 出现过的具体词来凑数 —— 凑数白名单会把同形的真捏造一起放过。
_ABBREVIATIONS = frozenset({
    "CT", "OID", "EDC", "PRT", "CRF", "SDTM", "SDTMIG", "CDISC", "CDASH", "NCI", "ISO", "ID",
    "QNAM", "SUPPQUAL", "RELREC",
    # 通用医学 / 统计缩写 (EDC label 里常带, 如「…（HIV）感染」)。⛔ 不放本研究特有的词。
    "HIV", "HBV", "HCV", "BMI", "BSA", "ECG", "EKG", "ECOG", "CTCAE", "MEDDRA", "WHO", "MRI",
    "PET", "CI", "SD", "SAE", "TEAE", "ULN", "LLN", "ITT", "DNA", "RNA",
})

_T = r"[A-Z][A-Z0-9_]+"
_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_*])" + _T + r"(?![A-Za-z0-9_*])")
# 纯 token 列表: 逗号 / 斜线 / 顿号 / 区间号分隔 (全角半角都收)。
_LIST = r"\s*" + _T + r"(?:\s*(?:[,/、，〜~–…]|and|or)\s*" + _T + r")*\s*"
_PURE_RE = re.compile(_LIST)
_CITATION_RE = re.compile(r"\[(?:Source|Web):[^\]\n]*\]")
_BRACKET_RE = re.compile(r"\[([^\[\]\n]+)\](?!\()")  # 排除 markdown 链接 [text](url)
# `[…] label (OID)` —— G-OID 取项目 OID 槽与 G-LANG 去引文共用这一条, 两处不许各写一份。
_REFERENCE_RE = re.compile(
    r"\[([^\[\]\n]*)\]([^\n\[\]`|]*)[(（](" + _LIST + r")[)）]")
_PAREN_RE = re.compile(r"[(（]([^()（）\n]+)[)）]")
_BACKTICK_RE = re.compile(r"`([^`\n]+)`")
_CCODE_RE = re.compile(r"C\d+")
_STEM_RE = re.compile(r"[A-Z]*")

_HIRAGANA_RE = re.compile(r"[ぁ-ゖ]")
_HAN_RE = re.compile(r"[一-鿿]")
_KATAKANA_RE = re.compile(r"[ァ-ヺ]")
_LATIN_WORD_RE = re.compile(r"[A-Za-z]+")
_QUOTE_RE = re.compile(r"「[^」\n]*」|『[^』\n]*』")
_TABLE_ROW_RE = re.compile(r"^[ \t]*\|.*$", re.M)
_FIXED_MARKERS = ("候補なし / no candidate item in the EDC", "候補なし", "推測")


@dataclass(frozen=True)
class OidIndex:
    forms: frozenset[str]
    items: frozenset[str]
    sdtm_names: frozenset[str] = frozenset()
    domains: frozenset[str] = frozenset()
    all_oids: frozenset[str] = field(init=False, repr=False)
    stems: frozenset[str] = field(init=False, repr=False)
    prefixes3: frozenset[str] = field(init=False, repr=False)

    def __post_init__(self):
        allo = frozenset(self.forms) | frozenset(self.items)
        object.__setattr__(self, "all_oids", allo)
        object.__setattr__(self, "stems", frozenset(
            s for s in (_STEM_RE.match(o).group(0) for o in allo) if s))
        object.__setattr__(self, "prefixes3", frozenset(o[:3] for o in allo if len(o) >= 3))

    @classmethod
    def from_catalog(cls, catalog_path: Path, kb_root: Path) -> OidIndex:
        cat = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
        names, domains = load_sdtm_names(kb_root)
        return cls(forms=frozenset(f["oid"] for f in cat["forms"]),
                   items=frozenset(i["item_oid"] for i in cat["items"]),
                   sdtm_names=names, domains=domains)


def load_sdtm_names(kb_root: Path) -> tuple[frozenset[str], frozenset[str]]:
    """KB `domains/*/spec.md` 的 `### VAR` 标题 + 域目录名 → (SDTM 名集, 域码集)。"""
    root = Path(kb_root) / "domains"
    domains = frozenset(d.name for d in root.iterdir() if d.is_dir())
    names = set(domains)
    for spec in root.glob("*/spec.md"):
        names.update(re.findall(r"^###\s+(\S+)", spec.read_text(encoding="utf-8"), re.M))
    return frozenset(names), domains


@dataclass(frozen=True)
class GateResult:
    ok: bool
    unknown_oids: tuple[str, ...]
    lang_expected: str
    lang_observed: str | None   # None = 正文太短, 不判
    reasons: tuple[str, ...]

    def to_dict(self) -> dict:
        return {"ok": self.ok, "unknown_oids": list(self.unknown_oids),
                "lang_expected": self.lang_expected, "lang_observed": self.lang_observed,
                "reasons": list(self.reasons)}


# ── G-OID ──────────────────────────────────────────────────────────

def _whitelisted(t: str, idx: OidIndex) -> bool:
    """宽白名单 —— 只给宽松位用。严格位 (表单槽/项目槽) 不许靠它过: 槽里写的就是 OID 断言,
    一个 SDTM 变量名或被截断的族前缀出现在那里, 就是捏造。"""
    return (t in idx.all_oids or t in idx.sdtm_names or t in _ABBREVIATIONS
            or _CCODE_RE.fullmatch(t) is not None
            or (t.startswith("SUPP") and t[4:] in idx.domains)
            or any(o.startswith(t) for o in idx.all_oids))           # 族前缀


def _narrow_ok(t: str, idx: OidIndex) -> bool:
    """窄放行集 —— 给「不一定是 OID 断言」的严格位 (两段方括号的末段 / 无真实 OID 时兜底取到的括号):
    缩写、C 码、域码、SUPP<域码>。⚠ 不含 SDTM 变量名与族前缀: 项目槽里写变量名 / 半截 OID 仍是捏造。"""
    return (t in _ABBREVIATIONS or _CCODE_RE.fullmatch(t) is not None or t in idx.domains
            or (t.startswith("SUPP") and t[4:] in idx.domains))


def _expands_from_sibling(t: str, siblings: list[str], idx: OidIndex) -> bool:
    """`A_F2/F3` 的 F3: 同列表真实 OID 的某个前缀 + t 在一览中存在 ⇒ 简写端点, 不计。"""
    return any(s[:i] + t in idx.all_oids
               for s in siblings if s in idx.all_oids for i in range(1, len(s)))


def _oid_like(t: str, siblings: list[str], idx: OidIndex) -> bool:
    """「像一览里的 OID」: 与同列表真实 OID 共享 ≥3 字符前缀, 或同词干且带数字/下划线。"""
    if any(s in idx.all_oids and len(_common_prefix(s, t)) >= 3 for s in siblings):
        return True
    return re.search(r"[0-9_]", t) is not None and _STEM_RE.match(t).group(0) in idx.stems


def _common_prefix(a: str, b: str) -> str:
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]:
        n += 1
    return a[:n]


def _prefixed_form(t: str, idx: OidIndex) -> bool:
    return any(t[i + 1:] in idx.forms and t[i + 1:] not in idx.domains
               for i, ch in enumerate(t) if ch == "_" and i > 0)


def _unknown_oids(answer: str, idx: OidIndex) -> tuple[str, ...]:
    text = _CITATION_RE.sub(" ", answer)
    bad: set[str] = set()

    def strict(tokens, fallback=False, allow_sdtm=False):
        """全严格: 只认一览 + 简写端点。列表里有真实 OID 时, 其余成员只放过宽白名单 (`(真实, HIV)`);
        fallback (槽位本身不一定是 OID 断言) 时放过窄集。"""
        has_real = any(s in idx.all_oids for s in tokens)
        for t in tokens:
            if t in idx.all_oids or _expands_from_sibling(t, tokens, idx):
                continue
            if has_real and _whitelisted(t, idx):
                continue
            if fallback and not has_real and (
                    _narrow_ok(t, idx) or (allow_sdtm and t in idx.sdtm_names)):
                continue
            bad.add(t)

    def semi_strict(tokens, after_slot=False):
        """半严格: 引用 span 里槽以外的纯 token 括号 —— 不在一览、也不在宽白名单 ⇒ 计。
        槽**之后**的括号多半已是散文 (`— 未测时填 (UNK)`): 再加一条「像 OID」(与一览某 OID 共享
        ≥3 字符前缀, 或带数字/下划线) 才计。"""
        for t in tokens:
            if _whitelisted(t, idx) or _expands_from_sibling(t, tokens, idx):
                continue
            if after_slot and not (t[:3] in idx.prefixes3 or re.search(r"[0-9_]", t)):
                continue
            bad.add(t)

    def loose(tokens):
        for t in tokens:
            if _whitelisted(t, idx) or _expands_from_sibling(t, tokens, idx):
                continue
            if _oid_like(t, tokens, idx):
                bad.add(t)

    item_slots, ref_heads = set(), set()
    for m in _REFERENCE_RE.finditer(text):                      # 项目 OID 槽
        span, toks, fallback = m.span(3), _TOKEN_RE.findall(m.group(3)), True
        # 引用后接散文时, 最后一个括号可能已在散文里 (`(真实OID) — … (SUPPXX) …`): label 段里
        # 若已有含真实 OID 的纯 token 括号, 槽就是它; 没有才取最后一个 (兜底, 窄集放行)。
        for p in _PAREN_RE.finditer(text, m.start(2), m.end(2)):
            ptoks = _TOKEN_RE.findall(p.group(1))
            if _PURE_RE.fullmatch(p.group(1)) and any(t in idx.all_oids for t in ptoks):
                span, toks, fallback = p.span(1), ptoks, False
                break
        if any(t in idx.all_oids for t in toks):
            fallback = False
        item_slots.add(span)
        ref_heads.add(m.start())
        strict(toks, fallback=fallback)
        # 同一引用 span 里其余纯 token 括号 (同行第二项 / label 自带括号 / 槽后散文): 半严格。
        for p in _PAREN_RE.finditer(text, m.start(2), m.end(3) + 1):
            if p.span(1) != span and _PURE_RE.fullmatch(p.group(1)):
                item_slots.add(p.span(1))
                semi_strict(_TOKEN_RE.findall(p.group(1)), after_slot=p.start(1) > span[0])
    for m in _BRACKET_RE.finditer(text):                        # 表单 OID 槽
        toks = _TOKEN_RE.findall(m.group(1))
        if not toks or not m.group(1).rstrip().endswith(toks[-1]):
            continue
        if m.start() in ref_heads:
            strict(toks[-1:])
        elif len(m.group(1).split()) >= 2:
            # `[See SDTMIG]` / `[参考 VS]` / `[→ VSORRES]` 不是表单引用: 窄集 + SDTM 变量名放行
            strict(toks[-1:], fallback=True, allow_sdtm=True)
        else:
            loose(toks[-1:])   # `[TBD]` / `[!NOTE]` 之类单段方括号: 只有像 OID 才计
    for rx in (_BACKTICK_RE, _PAREN_RE):                        # 宽松位
        for m in rx.finditer(text):
            if m.span(1) in item_slots or not _PURE_RE.fullmatch(m.group(1)):
                continue
            loose(_TOKEN_RE.findall(m.group(1)))
    for t in _TOKEN_RE.findall(text):                           # 全文: 自造前缀的表单 OID
        if t not in idx.all_oids and _prefixed_form(t, idx):
            bad.add(t)
    return tuple(sorted(bad))


# ── G-LANG ─────────────────────────────────────────────────────────

def _language_body(answer: str) -> str:
    body = _BACKTICK_RE.sub(" ", answer)
    body = _REFERENCE_RE.sub(" ", body)
    body = re.sub(r"\[[^\[\]\n]*\]", " ", body)
    body = _QUOTE_RE.sub(" ", body)
    body = _TABLE_ROW_RE.sub(" ", body)   # 表格单元格多是 OID / 变量名 / 引用的 label, 不是地の文
    for mk in _FIXED_MARKERS:
        body = body.replace(mk, " ")
    return body


def observed_language(answer: str) -> str | None:
    body = _language_body(answer)
    if len(re.sub(r"\s", "", body)) < MIN_BODY_CHARS:
        return None
    kana = len(_HIRAGANA_RE.findall(body)) + len(_KATAKANA_RE.findall(body))
    han = _HAN_RE.findall(body)
    if kana + len(han) <= len(_LATIN_WORD_RE.findall(body)):
        return "en"
    ja_han = sum(1 for ch in han if not _in_gb2312(ch))
    return "ja" if (kana + ja_han) / (kana + len(han)) >= JA_SIGNAL_RATIO else "zh"


def _in_gb2312(ch: str) -> bool:
    """简体中文字符集里有没有这个漢字。没有 ⇒ 日本字形 (或繁体, 见已知限制)。"""
    try:
        ch.encode("gb2312")
    except UnicodeEncodeError:
        return False
    return True


def check_answer(answer: str, question: str, index: OidIndex) -> GateResult:
    unknown = _unknown_oids(answer or "", index)
    expected = answer_language(question)
    observed = observed_language(answer or "")
    reasons = []
    if not (answer or "").strip():
        reasons.append("答案为空")
    if unknown:
        reasons.append(f"一览中不存在的 OID {len(unknown)} 个: {', '.join(unknown)}")
    if observed is not None and observed != expected:
        reasons.append(f"答题语言 {observed} ≠ 问句语言 {expected}")
    return GateResult(ok=not reasons, unknown_oids=unknown, lang_expected=expected,
                      lang_observed=observed, reasons=tuple(reasons))


# ── 编排 (两端点共用; 端点只做 I/O) ──────────────────────────────────

def regenerate_feedback(result: GateResult) -> str:
    """第二轮的 user 反馈。只含**本次运行时**查到的事实, 不含任何预置 example。"""
    lines = ["Your previous answer failed a deterministic check against the study dossier."]
    if result.unknown_oids:
        lines.append("These OIDs do not exist in part B (the exhaustive EDC item list): "
                     + ", ".join(result.unknown_oids)
                     + ". Every OID must be copied character for character from part B; "
                       "if unsure, describe the item in words without an OID.")
    if result.lang_observed is not None and result.lang_observed != result.lang_expected:
        lines.append(f"The answer was written in '{result.lang_observed}' but must be written in "
                     f"'{result.lang_expected}'. " + ANSWER_LANGUAGE_LINE[result.lang_expected])
    lines.append("Rewrite the COMPLETE answer from the beginning with these problems fixed; "
                 "do not refer to the previous attempt.")
    return "\n".join(lines)


class GateRun:
    """一次问答的闸状态机。/api/ask 与 /api/ask_stream 都只调这里做决定:
    observe(整轮答案) → should_regenerate() → regenerate_messages() → observe(第二轮) → payload()。"""

    def __init__(self, index: OidIndex, question: str):
        self.index, self.question = index, question
        self.first: GateResult | None = None
        self.final: GateResult | None = None
        self._rounds = 0
        self._regen_error: str | None = None

    def observe(self, answer: str) -> GateResult:
        r = check_answer(answer, self.question, self.index)
        self._rounds += 1
        if self.first is None:
            self.first = r
        self.final = r
        return r

    def should_regenerate(self) -> bool:
        return (self.final is not None and not self.final.ok
                and self._rounds <= REGEN_BUDGET and self._regen_error is None)

    def regenerate_messages(self, messages: list[dict], answer: str) -> list[dict]:
        """原 messages (快照, 不含工具/续写轮) + 首轮答案 + 反馈。首轮为空时原样重问 ——
        空 assistant 消息会被 litellm 合并丢弃, 模型收到的反馈就没有可指代的东西 (同续写那处)。"""
        if not answer:
            return list(messages)
        return [*messages, {"role": "assistant", "content": answer},
                {"role": "user", "content": regenerate_feedback(self.final)}]

    def regeneration_failed(self, error: str) -> None:
        self._regen_error = error

    def payload(self) -> dict:
        regenerated = self._rounds > 1
        out = {"final": self.final.to_dict() if self.final else None,
               "first": self.first.to_dict() if regenerated else None,
               "regenerated": regenerated}
        if self._regen_error:
            out["regenerate_error"] = self._regen_error
        return out
