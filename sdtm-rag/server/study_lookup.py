"""S2: study 侧确定性结构化直查 (Plan B Phase 2, spec 2026-08-04 §Phase 2).

golden v1.1 实测四类 miss 的确定性修复层: 数据源只有 catalog.json (+ 本地手工别名表),
零 LLM、不写卡片。契约对齐 S1: resolve(query) -> 要 union-add 的目标, 由 RAGEngine
前置注入。三条通道全部保守 — 不 fire 就回落纯检索, 绝不猜。
三条通道现均已通电。编号是设计标识, 不是执行序: 只有 ①② 争 cards 队列 (② 先入队,
段级精确 > label 子串, 末尾统一按总 cap 截断); ③ 只填 form_scopes, 不占 cards 名额。

  ① label 全文子串: 卡 label (NFKC+去空白归一化, >=4 字) 逐字出现在问句里 →
     该卡 + 其 OID 首段家族 (同 form + item_oid 首段相同; group 不是家族单元,
     真实数据里一个 group 可混装几十个家族)。歧义 label (卡+家族 > cap) 整体跳过。
  ② 拉丁 token → OID 段: 问句中的大写 token (>=3 位) 精确匹配 item_oid 的下划线段
     → 该段的卡集合 (1 <= n <= cap 才 fire)。近义双卡 (X vs 前缀加长的 X') 的判别
     天然成立: token 是段级精确匹配, 不是子串。
  ③ 别名表 → form scope: 手工别名 (自然语言词 -> form_oid, 本地 yml, 有据可查,
     不写入卡片) 命中 → 交给注入层做域内 cosine top-N (词面排序对该类实测失效)。
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

# 边界不能用 \b: 日文题面里 token 紧贴假名 (QSTは), 而 \w 含 CJK, \b 在此不成立。
# 只把 ASCII 字母/数字/下划线当作阻断邻居, 段级精确性照旧 (XABC 里取不出 ABC)。
_LATIN_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_])[A-Z][A-Z0-9]{2,}(?![A-Za-z0-9_])")
_MIN_LABEL_LEN = 4
_MIN_SEG_LEN = 3
_MAX_CARDS_PER_MATCH = 8   # 单个 label/token 命中集合上限, 超过 = 不具判别力, 跳过
_MAX_CARDS_TOTAL = 10      # resolve 输出的精确卡总上限 (k=15 里给 cosine 留位)


def _norm(s: str) -> str:
    """匹配用归一化: NFKC + 去全部空白 (label 与问句同变换)。"""
    return "".join(unicodedata.normalize("NFKC", s).split())


@dataclass
class StudyLookupResult:
    cards: list[str] = field(default_factory=list)
    form_scopes: list[str] = field(default_factory=list)


class StudyLookup:
    def __init__(self, catalog: dict, aliases: list[dict] | None = None):
        self.study_id = catalog["study"]
        items = catalog["items"]
        known_forms = {it["form_oid"] for it in items}
        self.aliases: list[dict] = []
        for a in aliases or []:
            if a["form"] not in known_forms:
                raise ValueError(
                    f"alias form {a['form']!r} not in catalog forms — 别名表指向不存在的 form")
            self.aliases.append({"term": _norm(a["term"]), "form": a["form"]})
        # label(归一化) -> [card_src]; (form, OID首段) -> [card_src]; 段 -> [card_src]
        self._label_index: dict[str, list[str]] = defaultdict(list)
        self._family: dict[tuple[str, str], list[str]] = defaultdict(list)
        self._segment_index: dict[str, list[str]] = defaultdict(list)
        self._card_family: dict[str, tuple[str, str]] = {}
        for it in items:
            src = f"{self.study_id}__{it['form_oid']}__{it['item_oid']}.md"
            ln = _norm(it["label"])
            if len(ln) >= _MIN_LABEL_LEN:
                self._label_index[ln].append(src)
            segs = it["item_oid"].split("_")
            fam = (it["form_oid"], segs[0])
            self._family[fam].append(src)
            self._card_family[src] = fam
            for seg in set(segs):
                if len(seg) >= _MIN_SEG_LEN:
                    self._segment_index[seg].append(src)

    def resolve(self, query: str) -> StudyLookupResult:
        qn = _norm(query)
        cards: list[str] = []

        def add(src: str) -> None:
            if src not in cards:
                cards.append(src)

        # ② 先入队: 段级精确命中的信号强度高于 label 子串, 末尾按总 cap 截断时不该被子串挤掉
        for tok in dict.fromkeys(_LATIN_TOKEN_RE.findall(query)):
            hits = self._segment_index.get(tok, [])
            if 1 <= len(hits) <= _MAX_CARDS_PER_MATCH:
                for s in hits:
                    add(s)

        # ① label 全文子串 → 卡 + OID 首段家族 (歧义超 cap 整体跳过)
        for ln, srcs in self._label_index.items():
            if ln not in qn:
                continue
            expanded: list[str] = []
            for s in srcs:
                for member in self._family[self._card_family[s]]:
                    if member not in expanded:
                        expanded.append(member)
            if len(expanded) <= _MAX_CARDS_PER_MATCH:
                for s in expanded:
                    add(s)

        # ③ 别名 → form scope (注入层做域内 cosine top-N; 词面排序对该类实测失效)
        scopes: list[str] = []
        for a in self.aliases:
            if a["term"] in qn and a["form"] not in scopes:
                scopes.append(a["form"])

        return StudyLookupResult(cards=cards[:_MAX_CARDS_TOTAL], form_scopes=scopes)

    @classmethod
    def from_paths(cls, catalog_path: Path, aliases_path: Path | None) -> "StudyLookup":
        """catalog 缺失 = 配置错误, 响亮失败; 别名表是可选增强, 缺失降级为空。"""
        catalog = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
        aliases: list[dict] = []
        if aliases_path is not None and Path(aliases_path).exists():
            data = yaml.safe_load(Path(aliases_path).read_text(encoding="utf-8")) or {}
            aliases = data.get("aliases", []) or []
        return cls(catalog, aliases=aliases)
