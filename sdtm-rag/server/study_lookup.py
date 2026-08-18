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
     天然成立: token 是段级精确匹配, 不是子串。题面含 >=2 个 token 时另取各段集合的
     交集 (合取) 作独立候选先入队 —— 单段命中面过宽被 cap 挡掉时, 交集常仍够窄。
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


@dataclass
class _ChannelHits:
    """四条通道各自的命中 (cap 过滤后, 未合并未去重未截断)。内部件, 别当公开契约用。"""

    intersection: list[str] = field(default_factory=list)   # ②a 多 token 段交集 (强)
    single_token: list[str] = field(default_factory=list)   # ②b 单 token 段命中 (弱)
    label: list[str] = field(default_factory=list)          # ① label 子串 + 家族 (强)
    form_scopes: list[str] = field(default_factory=list)    # ③ 别名 → form scope (强)


class StudyLookup:
    def __init__(self, catalog: dict, aliases: list[dict] | None = None):
        self.study_id = catalog["study"]
        items = catalog["items"]
        self.n_items = len(items)
        known_forms = {it["form_oid"] for it in items}
        self.aliases: list[dict] = []
        for a in aliases or []:
            term = _norm(a["term"])
            if not term:
                raise ValueError(
                    f"alias term for form {a['form']!r} is empty after normalization — 空别名会命中所有问句")
            if a["form"] not in known_forms:
                raise ValueError(
                    f"alias form {a['form']!r} has no item in catalog — 别名表指向不存在的 form")
            # raw = 作者在 yml 写的字面, 供命中日志排查 (term 是归一化形态, 对不上账)
            self.aliases.append({"term": term, "raw": a["term"], "form": a["form"]})
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

    def _channel_hits(self, query: str) -> _ChannelHits:
        """四条通道各自的命中 (均已按 cap 过滤), 未合并未截断。

        拆出来只为让"哪条通道命中了"有**一处**定义: `resolve` 要四条按序去重的并集,
        U6 信号层只要强通道 (见 `strong_hit`)。两处各写一份筛选就会各自漂移, 而漂移的
        症状是静默的 (信号层照常 fire, 只是 fire 的依据与 resolve 注入的卡不是一回事)。
        """
        qn = _norm(query)

        # ② 段级精确命中的信号强度高于 label 子串, 末尾按总 cap 截断时不该被子串挤掉
        tokens = list(dict.fromkeys(_LATIN_TOKEN_RE.findall(query)))

        # ②a 多 token 交集 (合取: 同时提到多个段 → 同属这些段的卡最相关)。交集恒 ⊆ 各单
        #     token 集合, 只会更窄, 与 cap"集合太大=不具判别力"同向, 故沿用同一 cap 且
        #     比单 token 更精确 → 排在 ②b 之前。任一 token 段命中为空则交集为空 = 不 fire。
        intersection: list[str] = []
        if len(tokens) >= 2:
            hit_sets = [self._segment_index.get(t, []) for t in tokens]
            others = [set(h) for h in hit_sets[1:]]
            inter = [s for s in hit_sets[0] if all(s in o for o in others)]
            if 1 <= len(inter) <= _MAX_CARDS_PER_MATCH:
                intersection = inter

        # ②b 单 token → 该段卡集合 (集合超 cap = 不具判别力, 跳过)
        single_token: list[str] = []
        for tok in tokens:
            hits = self._segment_index.get(tok, [])
            if 1 <= len(hits) <= _MAX_CARDS_PER_MATCH:
                single_token.extend(hits)

        # ① label 全文子串 → 卡 + OID 首段家族 (歧义超 cap 整体跳过)
        label: list[str] = []
        for ln, srcs in self._label_index.items():
            if ln not in qn:
                continue
            expanded: list[str] = []
            for s in srcs:
                for member in self._family[self._card_family[s]]:
                    if member not in expanded:
                        expanded.append(member)
            if len(expanded) <= _MAX_CARDS_PER_MATCH:
                label.extend(expanded)

        # ③ 别名 → form scope (注入层做域内 cosine top-N; 词面排序对该类实测失效)
        scopes: list[str] = []
        for a in self.aliases:
            if a["term"] in qn and a["form"] not in scopes:
                scopes.append(a["form"])

        return _ChannelHits(intersection=intersection, single_token=single_token,
                            label=label, form_scopes=scopes)

    def resolve(self, query: str) -> StudyLookupResult:
        h = self._channel_hits(query)
        cards: list[str] = []
        # 入队顺序 = ②a → ②b → ①, 首次出现为准; 总 cap 在最后截断 (顺序即优先级)
        for src in (*h.intersection, *h.single_token, *h.label):
            if src not in cards:
                cards.append(src)
        return StudyLookupResult(cards=cards[:_MAX_CARDS_TOTAL], form_scopes=h.form_scopes)

    def strong_hit(self, query: str) -> bool:
        """强通道 (①/②a/③) 是否命中 —— U6 判库信号层专用, 不影响 `resolve` 的注入。

        弱通道 ②b (单个大写 token 撞上某个 item OID 段) 刻意排除: 本研究 EDC 的 OID 段
        沿用 SDTM 风味命名, 于是一道**纯标准题**里的变量名 (AESEV 之类) 会精确撞段。
        对注入层那是廉价的多召回几张卡, 对判库层却是把 cdisc 判定错误地拓宽成 both ——
        Task 9 可见集标定实测 6 道纯标准题误触, 全部出自这条通道 (每触 −1 exact,
        模拟 legacy 173 < 阈值 178, 见 evidence/u6_task9_calibration.md §5)。

        用的是**cap 过滤后**的命中: 命中集超 cap 在 resolve 里就是"不具判别力, 整体跳过",
        没有理由在信号层反倒算作依据。
        """
        h = self._channel_hits(query)
        return bool(h.intersection or h.label or h.form_scopes)

    def stats(self) -> str:
        """加载规模一行摘要, 供启动日志与评测回执共用。

        别名表缺失是 from_paths 刻意的优雅降级 (见下), 代价是"别名 0 条 = 通道③ 完全没通电"
        与"别名表加载成功"在外部表现一致。把条数打出来是唯一能在跑的时候看出区别的地方 ——
        别名文件放错目录/文件名写错/顶层键不叫 aliases, 三种错误都只表现为这里的 0。
        """
        return f"{self.n_items} items/{len(self.aliases)} aliases"

    @classmethod
    def from_paths(cls, catalog_path: Path, aliases_path: Path | None) -> StudyLookup:
        """catalog 缺失 = 配置错误, 响亮失败; 别名表是可选增强, 缺失降级为空。"""
        catalog = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
        aliases: list[dict] = []
        if aliases_path is not None and Path(aliases_path).exists():
            data = yaml.safe_load(Path(aliases_path).read_text(encoding="utf-8")) or {}
            aliases = data.get("aliases", []) or []
        return cls(catalog, aliases=aliases)
