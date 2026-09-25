"""DM2 研读包答案 生成后确定性闸 —— 纯函数, 零 LLM, 可枚举。

spec: docs/superpowers/specs/2026-09-25-dossier-output-gate-design.md (§2 闸定义, §3 编排, §4 回放)。
只在研读包挂上时跑: B 部是穷尽一览, 「不在一览 = 不存在」只在那时成立。

G-OID —— 只在「OID 断言」的位置取 token (`[A-Z][A-Z0-9_]{1,}`), 其余散文里的大写词一概不看:
  严格位 (不在一览、不在白名单 ⇒ 计):
    · `[… FORM]` 方括号的末 token (表单 OID 槽);
    · `[…] label (OID)` 引用形态里 label 后的**最后一个**纯 token 括号 (项目 OID 槽 —— label 自己
      可能带 `(缩写)`, 所以取最后一个; 代价: label 后接散文时可能取到散文里的括号, 见已知限制)。
  宽松位 (反引号 / 其它括号里的纯 token 列表): 只有「像一览里的 OID」才计 ——
    · 与一览里的真实 OID 并列在同一个列表里 (同一列表 = 同一类断言);
    · 词干 (前导字母段) 与一览里某个 OID 的词干相同, 且带数字或下划线 (自造编号/后缀的「补全」)。
    ⚠ 词干规则对本研究命名习惯敏感: 与一览同词干、差一个字母的 SDTM 侧取值 (如 --TESTCD 示例)
    靠「词干不同」才没被误标 —— 换一个命名习惯的研究可能翻转。
  全文 (唯一例外, 偏离 §2「窄提取」, 由 §4 预期迫使): `<前缀>_<真实表单 OID>` 形态的未知 token ——
    规则句 ③ 明令禁止给 OID 加前缀, 而这类捏造在回放里出现在表格裸文本中, 窄提取看不到。
  白名单 (不计): SDTM 变量名 / 域码 (KB `domains/*/spec.md` 的 `### VAR` + 目录名)、SUPP+域码、
  NCI C 码、常见缩写、占位写法 (含小写 n/x 或 `*` 的 token 本来就不被切出)、族前缀 (一览中有以其
  为前缀的成员)、列表/区间简写端点 (与同列表真实 OID 的前缀拼起来在一览中存在)。

G-LANG —— 去掉反引号 / `[…] label (OID)` 引用 / 其余方括号 / 「」『』引文 / 固定标记后计数:
  平仮名 ≥ HIRAGANA_JA_MIN ⇒ ja; 否则 漢字数 > 拉丁词数 ⇒ zh; 否则 en。
  阈值由 §4 回放校准 (42 份: 去引用后非 ja 答案平仮名最多 39, 真 ja 答案最少 294), 写死 100。
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from server.dossier_trigger import ANSWER_LANGUAGE_LINE, answer_language

HIRAGANA_JA_MIN = 100
REGEN_BUDGET = 1  # 重答上限 (spec §3): 再一次 ~150K prompt 全价调用, 不做第二次

# spec 点名的缩写 + 同类的标准/文档缩写。⚠ 只放「不可能是 EDC OID 的通用缩写」, 不放任何回放里
# 出现过的具体词来凑数 —— 凑数白名单会把同形的真捏造一起放过。
_ABBREVIATIONS = frozenset({
    "CT", "OID", "EDC", "PRT", "CRF", "SDTM", "SDTMIG", "CDISC", "CDASH", "NCI", "ISO", "ID",
    "QNAM", "SUPPQUAL", "RELREC",
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
_LATIN_WORD_RE = re.compile(r"[A-Za-z]+")
_QUOTE_RE = re.compile(r"「[^」\n]*」|『[^』\n]*』")
_FIXED_MARKERS = ("候補なし / no candidate item in the EDC", "候補なし", "推測")


@dataclass(frozen=True)
class OidIndex:
    forms: frozenset[str]
    items: frozenset[str]
    sdtm_names: frozenset[str] = frozenset()
    domains: frozenset[str] = frozenset()
    all_oids: frozenset[str] = field(init=False, repr=False)
    stems: frozenset[str] = field(init=False, repr=False)

    def __post_init__(self):
        allo = frozenset(self.forms) | frozenset(self.items)
        object.__setattr__(self, "all_oids", allo)
        object.__setattr__(self, "stems", frozenset(
            s for s in (_STEM_RE.match(o).group(0) for o in allo) if s))

    @classmethod
    def from_catalog(cls, catalog_path: Path, kb_root: Path) -> "OidIndex":
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
    lang_observed: str
    reasons: tuple[str, ...]

    def to_dict(self) -> dict:
        return {"ok": self.ok, "unknown_oids": list(self.unknown_oids),
                "lang_expected": self.lang_expected, "lang_observed": self.lang_observed,
                "reasons": list(self.reasons)}


# ── G-OID ──────────────────────────────────────────────────────────

def _whitelisted(t: str, idx: OidIndex) -> bool:
    return (t in idx.all_oids or t in idx.sdtm_names or t in _ABBREVIATIONS
            or _CCODE_RE.fullmatch(t) is not None
            or (t.startswith("SUPP") and t[4:] in idx.domains)
            or any(o.startswith(t) for o in idx.all_oids))           # 族前缀


def _expands_from_sibling(t: str, siblings: list[str], idx: OidIndex) -> bool:
    """`A_F2/F3` 的 F3: 同列表真实 OID 的某个前缀 + t 在一览中存在 ⇒ 简写端点, 不计。"""
    return any(s[:i] + t in idx.all_oids
               for s in siblings if s in idx.all_oids for i in range(1, len(s)))


def _prefixed_form(t: str, idx: OidIndex) -> bool:
    return any(t[i + 1:] in idx.forms for i, ch in enumerate(t) if ch == "_" and i > 0)


def _unknown_oids(answer: str, idx: OidIndex) -> tuple[str, ...]:
    text = _CITATION_RE.sub(" ", answer)
    bad: set[str] = set()

    def strict(tokens):
        for t in tokens:
            if not _whitelisted(t, idx) and not _expands_from_sibling(t, tokens, idx):
                bad.add(t)

    for m in _BRACKET_RE.finditer(text):                        # 表单 OID 槽
        toks = _TOKEN_RE.findall(m.group(1))
        if toks and m.group(1).rstrip().endswith(toks[-1]):
            strict(toks[-1:])
    item_slots = set()
    for m in _REFERENCE_RE.finditer(text):                      # 项目 OID 槽
        item_slots.add(m.span(3))
        strict(_TOKEN_RE.findall(m.group(3)))
    for rx in (_BACKTICK_RE, _PAREN_RE):                        # 宽松位
        for m in rx.finditer(text):
            if m.span(1) in item_slots or not _PURE_RE.fullmatch(m.group(1)):
                continue
            toks = _TOKEN_RE.findall(m.group(1))
            has_real = any(s in idx.all_oids for s in toks)
            for t in toks:
                if _whitelisted(t, idx) or _expands_from_sibling(t, toks, idx):
                    continue
                if has_real or (re.search(r"[0-9_]", t) and _STEM_RE.match(t).group(0) in idx.stems):
                    bad.add(t)
    for t in _TOKEN_RE.findall(text):                           # 全文: 自造前缀的表单 OID
        if not _whitelisted(t, idx) and _prefixed_form(t, idx):
            bad.add(t)
    return tuple(sorted(bad))


# ── G-LANG ─────────────────────────────────────────────────────────

def observed_language(answer: str) -> str:
    body = _BACKTICK_RE.sub(" ", answer)
    body = _REFERENCE_RE.sub(" ", body)
    body = re.sub(r"\[[^\[\]\n]*\]", " ", body)
    body = _QUOTE_RE.sub(" ", body)
    for mk in _FIXED_MARKERS:
        body = body.replace(mk, " ")
    if len(_HIRAGANA_RE.findall(body)) >= HIRAGANA_JA_MIN:
        return "ja"
    if len(_HAN_RE.findall(body)) > len(_LATIN_WORD_RE.findall(body)):
        return "zh"
    return "en"


def check_answer(answer: str, question: str, index: OidIndex) -> GateResult:
    unknown = _unknown_oids(answer or "", index)
    expected = answer_language(question)
    observed = observed_language(answer or "")
    reasons = []
    if unknown:
        reasons.append(f"一览中不存在的 OID {len(unknown)} 个: {', '.join(unknown)}")
    if observed != expected:
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
    if result.lang_observed != result.lang_expected:
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
