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

from scripts.study.collect_scope import collect_scope

# 边界不能用 \b: 日文题面里 token 紧贴假名 (QSTは), 而 \w 含 CJK, \b 在此不成立。
# 只把 ASCII 字母/数字/下划线当作阻断邻居, 段级精确性照旧 (XABC 里取不出 ABC)。
_LATIN_TOKEN_RE = re.compile(r"(?<![A-Za-z0-9_])[A-Z][A-Z0-9]{2,}(?![A-Za-z0-9_])")
_MIN_LABEL_LEN = 4
_MIN_SEG_LEN = 3
_MAX_CARDS_PER_MATCH = 8   # 单个 label/token 命中集合上限, 超过 = 不具判别力, 跳过
_MAX_CARDS_TOTAL = 10      # resolve 输出的精确卡总上限 (k=15 里给 cosine 留位)
# resolve_events 总输出上限。**不是**从 _MAX_CARDS_TOTAL 抄来的诊断性质的阈值 (团队 lead
# 2026-08-26 复审指出 8 是从卡片场景抄的, 未必适用于此处 —— 采纳)。语义不同:
# `resolve()` 的 cap 是"匹配集合太大 = 不具判别力"的质量闸(见 _MAX_CARDS_PER_MATCH,
# 超出直接整体跳过, 不进候选池); resolve_events 的这三类目标里"一个事件/表单合法地对应
# 几十条 assignment"是数据的正常形态, 不是匹配质量差的信号(实测: 单个 form 最多挂 40 条
# assignment, 单个 item 的 collect_scope 最多算出 40 条, 均为真实值非异常)。故这里定位
# 是"防真正失控的输出量级"的安全阀, 不是诊断质量闸, 阈值定得比 _MAX_CARDS_TOTAL 宽松
# 很多, 覆盖到实测最大单次命中(40)之上留出余量, 但仍然是个上限(未知查询理论上可能同时
# 撞上多个索引键叠加得更大, 需要有底)。
_MAX_EVENTS_TOTAL = 50
_MIN_EVENT_NAME_LEN = 3    # 事件/活动名称索引最短长度, 防短名命中一切
_MIN_ITEM_OID_LEN = 3      # item OID 索引最短长度 (与 _MIN_SEG_LEN 同阈值)
# form_oid 词汇表本身很短 (21 个真实值, 7 个只有 2 字符, 见 assignments 池): 沿用
# _MIN_ITEM_OID_LEN=3 会永久排除 1/3 的 form, 直接废掉这条索引对短 form 的价值 ——
# 但 2 字符阈值若用裸子串匹配, 误召回面太大, 靠下面的 _bounded_contains 有界匹配
# (两侧都不是 ASCII 字母/数字/下划线) 兜底, 而不是靠拉高最短长度。
_MIN_FORM_OID_LEN = 2


def _norm(s: str) -> str:
    """匹配用归一化: NFKC + 去全部空白 (label 与问句同变换)。"""
    return "".join(unicodedata.normalize("NFKC", s).split())


def _norm_ws(s: str) -> str:
    """NFKC 正规化但**保留空白**, 供 _bounded_contains 的有界 OID 匹配专用。

    与 `_norm` 的关键差异: `_norm` 去空白会把被空格隔开的两个 token 拼接成一个连续串,
    让"两侧是否有边界"这个判断失真——实测案例 (2026-08-26 复审发现): 某题题面里一个
    3 字符 item OID 后面紧跟半角空格再接数字 (OID 与数字之间原有空格), 去空白后 OID
    直接贴上该数字, 对短 OID 的有界判断而言, 这个人为拼接的邻接关系是假的, 必须在保留
    空白的文本上判边界, 结论才稳定。名称索引 (Tier 3) 不受这个问题影响, 继续用 `_norm`。
    """
    return unicodedata.normalize("NFKC", s)


def _bounded_contains(oid_key: str, text_ws: str) -> bool:
    """oid_key 是否以完整边界 token 形式出现在 text_ws 里 (两侧都不是 ASCII 字母/数字/
    下划线) —— 比裸子串更严格, 专防短 OID (2-3 字符, form_oid/item_oid 词汇表里均有
    这个长度的真实值) 撞上无关内容的子串 (2026-08-26 复审实测案例: 一个 3 字符 item OID
    撞进题面里一段无关文字, 贡献 7 条与本题无关的噪声目标)。CJK 字符不在 [A-Za-z0-9_]
    里, 紧贴假名/汉字两侧天然满足边界, 不受影响 (同 `_LATIN_TOKEN_RE` 的边界哲学, 见
    文件顶部说明)。

    `text_ws` 必须是 `_norm_ws` 的输出 (保留空白), 不能传 `_norm` 的去空白版本 ——
    原因见 `_norm_ws` 文档字符串。
    """
    pattern = re.compile(rf"(?<![A-Za-z0-9_]){re.escape(oid_key)}(?![A-Za-z0-9_])")
    return bool(pattern.search(text_ws))


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

        # 事件层索引 (三池是 2026-08-25 新增, 老 catalog 无此 key → 空索引, 静默降级)。
        # 拆两个索引对应 resolve_events 的两个精度层级 (2026-08-26 复审后拆分):
        # Tier 1 `_exact_oid_index` = OID/form 精确命中 (event OID / activity OID /
        #   form OID, 有界匹配), 命中即直接给目标, 不含推断成分;
        # Tier 3 `_name_index` = 事件/活动**名称**子串命中 (自然语言短语, 沿用既有裸
        #   子串, 不加边界——通用词碰撞风险已知, 见 checkpoint 已知限制)。
        # 两者分开是为了 resolve_events 能按"精确 > 推导 > 名称"优先级分层拼接输出,
        # 名称这类较弱信号不会在总 cap 截断时把精确/推导目标挤出去。
        self._exact_oid_index: dict[str, list[str]] = defaultdict(list)
        self._name_index: dict[str, list[str]] = defaultdict(list)
        for e in catalog.get("events", []):
            target = f"event:{e['oid']}"
            self._exact_oid_index[_norm(e["oid"])].append(target)
            n = _norm(e.get("name", ""))
            if len(n) >= _MIN_EVENT_NAME_LEN:
                self._name_index[n].append(target)
        for a in catalog.get("activities", []):
            target = f"activity:{a['event_oid']}/{a['oid']}"
            self._exact_oid_index[_norm(a["oid"])].append(target)
            n = _norm(a.get("name", ""))
            if len(n) >= _MIN_EVENT_NAME_LEN:
                self._name_index[n].append(target)
        # Ruling P2 (团队 lead 复审, 2026-08-26 修复轮1): form_oid -> 该 form 的**全部**
        # assignment (未做 item 级减法的原始清单)。与下面 item 采集范围索引 (Tier 2)
        # 是两回事——这里回答"这个表单被分配到哪些活动/事件"(event_form_assignment/
        # repeating_rule 两类问法的判据落点), 不做"某个具体 item 实际在哪采集"的减法;
        # 该减法是 item 级概念, 对表单本身不适用。真实数据 21 个 form_oid 里 7 个只有
        # 2 字符 (_MIN_FORM_OID_LEN=2 覆盖全部), 裸子串在这个长度下误召回风险高, 故这类
        # 键统一走 `_bounded_contains` 有界匹配, 不直接并进 `_exact_oid_index` (下同)。
        #
        # 单独存一个索引 (不并进 `_exact_oid_index`) 是因为 resolve_events 需要在填充
        # 这层之前先知道 Tier 2 覆盖了哪些 form ——若某 form 在本次查询里**同时**被
        # Tier 2 的减法结果覆盖 (题面同时点名了这个 form 下某个具体 item OID, 类型6的
        # 5 题常见), 该 form 的未减法原始清单要让位, 否则精确的减法答案会被同一 form
        # 的几十条未减法原始清单埋掉——precision 会暴跌 (2026-08-26 复审后追加发现,
        # 实测 `ev_q27`/`ev_q28` 从"tp=gold,fp=0"退化到两位数 fp; 详见 checkpoint)。
        # ⚠ 2026-08-26 修复轮2 复审指出: "整 form 让位"不是无损操作——Tier 2 的结果按
        # 定义是该 form 全量的**子集** (= 分配 − 该 item 的隐藏清单), 若隐藏清单非空,
        # 这就是真子集, 被让掉的差集**没有任何其他层会补回来**。这个claim只在"gold 恰好
        # 落在 Tier 2 那个子集里"(即题面问的是 item 采集范围) 时才成立"命中不丢";
        # 对 form 级问法 (event_form_assignment/repeating_rule, 正是 Ruling P2 要服务
        # 的那两类) 不成立——若 gold 是该 form 里**被这个 item 隐藏、但仍是真实分配**的
        # 另一条 assignment, 会被静默让掉。真实数据: 231/959 个 item 的减法结果是所属
        # form 全量的真子集 (涉 7/21 个 form), 单次最多让掉 39 条; 当前 33 题因这条让位
        # 丢失 gold 的题数 = 0 (未触发, 不代表设计上不存在), 已记入 checkpoint 已知限制,
        # 未在本轮修复 (更稳妥的解是"逐条相减"而非"整 form 让位", 留作后续工作)。
        # `_form_assignment_form_oid` 记录归一化键对应的原始 form_oid 字面 (同一 key 下
        # 全部 assignment 的 form_oid 相同, 取一份即可)。
        self._form_assignment_index: dict[str, list[str]] = defaultdict(list)
        self._form_assignment_form_oid: dict[str, str] = {}
        for a in catalog.get("assignments", []):
            key = _norm(a["form_oid"])
            if len(key) >= _MIN_FORM_OID_LEN:
                t = f"assignment:{a['event_oid']}/{a['activity_oid']}/{a['form_oid']}"
                self._form_assignment_index[key].append(t)
                self._form_assignment_form_oid[key] = a["form_oid"]

        # item 采集范围索引 (Tier 2, spec §2.3 的 collect_scope 减法, 经本类接通"类型6/
        # item_collection_scope"问法; Task 4 review M4/M5 —— 该函数原来只活在渲染器
        # 里, 生产渲染路径从不调用它, 是纯粹的死代码风险; 这里是它的第一个真实消费方)。
        # 索引对象是 item_oid (有界匹配, 与 Tier 1 同精神), 真正命中时才现算
        # collect_scope, 不预算 (959 item 逐一预算无意义, 命中面通常个位数)。
        # 键过 _norm (与 _exact_oid_index/_form_assignment_index 同规范, 2026-08-26
        # 复审 Minor-2 修复——之前裸 oid 当键, 与查找端 _bounded_contains(oid, q_ws) 的
        # q_ws 只做 NFKC (未去空白) 尚可对齐, 但和其他三类索引的键规范不对称, 是没写下来
        # 也没测到的隐含不变量; item OID 现实中不含内部空白, 本次是无行为变化的加固)。
        self._item_oid_index: dict[str, list[dict]] = defaultdict(list)
        for it in items:
            oid = it.get("item_oid")
            if oid and len(oid) >= _MIN_ITEM_OID_LEN:
                self._item_oid_index[_norm(oid)].append(it)
        # (form_oid, activity_oid) -> 该组合下的 assignment 行 (供 collect_scope 算出
        # activity_oid 后反查 event_oid, 组出 assignment:{event}/{activity}/{form} 目标)
        self._assignments_by_form_activity: dict[tuple[str, str], list[dict]] = defaultdict(list)
        for a in catalog.get("assignments", []):
            self._assignments_by_form_activity[(a["form_oid"], a["activity_oid"])].append(a)
        self._assignments: list[dict] = catalog.get("assignments", [])

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

    def resolve_events(self, query: str) -> list[str]:
        """事件层命中: OID/form 精确匹配 + item 采集范围推导 + 名称子串, 三层按精度
        优先级拼接后统一按 _MAX_EVENTS_TOTAL 截断。

        与 resolve() 分开是刻意的 —— 事件目标名不是卡名, 混进 cards 会让调用方
        把它当 chunk 去取, 那是静默的类型错误。

        **三层优先级是 2026-08-26 复审后的核心修复** (团队 lead Ruling, 抽检方实测
        验证): 若不分层、按索引遍历顺序 (事件/活动先于 item) 简单拼接再截断, 较弱的
        名称子串命中会排在结构化目标**前面**抢占 cap 名额——噪声先于信号, 已实测复现
        (`ev_q30` 一题在旧实现下未截断即达到 4 条, 其中 3 条是名称索引段的巧合命中)。
        现按下列优先级拼接, **同层内部去重, 跨层也去重**, 最后统一截断:

        - **Tier 1a (event/activity OID 精确命中, 有界匹配)**: 直接给 `event:`/
          `activity:` 目标, 无推断成分。
        - **Tier 2 (结构化推导)**: item OID (有界匹配) 命中后现算 `collect_scope()`
          减法 (表单分配 − 隐藏清单, spec §2.3), 换算成实际收集到它的 assignment
          目标——这是类型6/item_collection_scope 问法的判据, 唯一同时消费 items 与
          assignments 两池的通道。不做 precision 判断: 减法算出的 activity 集合只要
          非空就全部纳入, 一个"该 item 恰好命中多个候选"的 query 会把它们的收集点
          都并入同一层, 调用方无法从返回值本身分辨"这条是唯一候选"还是"多个候选之
          一"——已知限制, 见 checkpoint。
        - **Tier 1b (form OID → 该 form 的全部 assignment 原始清单, 有界匹配)**:
          Ruling P2 (团队 lead 复审, 2026-08-26 修复轮1) ——未做 item 级减法, 回答的是
          "这个表单被分配到哪些活动/事件"(event_form_assignment/repeating_rule 两类
          问法的判据落点), 与 Tier 2 的"某个具体 item 实际在哪采集"是不同问题。**排在
          Tier 2 之后而不是之前**是刻意的: 若某 form 在本次查询里同时被 Tier 2 的减法
          结果覆盖 (题面同时点名了这个 form 下某个具体 item OID, 类型6的 5 题常见),
          该 form 的未减法原始清单让位 (`covered_forms` 收集 Tier 2 已算过的 form,
          Tier 1b 跳过这些 form 的原始清单)——否则精确的减法答案会被同一 form 几十条
          未减法条目埋掉, precision 暴跌 (2026-08-26 复审后实测复现: 不做这个避让时,
          `ev_q27`/`ev_q28` 从"tp=gold,fp=0"退化到两位数 fp, 详见 checkpoint)。
          ⚠ 这个"整 form 让位"不是无损操作, "命中不丢"**不是**一般性结论——只在
          gold 恰好落在 Tier 2 那个 (真) 子集里时成立; 若 gold 是该 form 里被这个
          item 隐藏、但仍是别的问题真实需要的另一条 assignment, 会被静默让掉 (真实
          数据 231/959 个 item 触发此情形, 当前 33 题未因此丢过 gold, 但设计上存在,
          详见 `__init__` 里 `_form_assignment_index` 那段注释与 checkpoint 已知限制)。
          form OID 词汇表 7/21 只有 2 字符, 裸子串在这个长度下误召回风险不可接受,
          故用 `_bounded_contains`。
        - **Tier 3 (名称子串, 裸匹配, 无边界)**: event/activity 名称是自然语言短语,
          边界概念不适用 (与 label 子串同精神)。已知会撞上研究内高频通用词造成假阳性
          (如某治疗方案缩写同时是一个 event 的可读名) ——正因为这层信号最弱、误召回
          风险最高, 才必须排在最后, 只填充前几层用剩的名额。
        """
        qn = _norm(query)
        q_ws = _norm_ws(query)

        tier1a: list[str] = []
        for key, targets in self._exact_oid_index.items():
            if key and _bounded_contains(key, q_ws):
                for t in targets:
                    if t not in tier1a:
                        tier1a.append(t)

        tier2: list[str] = []
        covered_forms: set[str] = set()
        for oid, cand_items in self._item_oid_index.items():
            if not _bounded_contains(oid, q_ws):
                continue
            for it in cand_items:
                scope = collect_scope(it, self._assignments)
                if scope:
                    covered_forms.add(it["form_oid"])
                for act_oid in scope:
                    for a in self._assignments_by_form_activity.get((it["form_oid"], act_oid), []):
                        t = f"assignment:{a['event_oid']}/{act_oid}/{it['form_oid']}"
                        if t not in tier2:
                            tier2.append(t)

        tier1b: list[str] = []
        for key, targets in self._form_assignment_index.items():
            if not key or not _bounded_contains(key, q_ws):
                continue
            if self._form_assignment_form_oid[key] in covered_forms:
                continue
            for t in targets:
                if t not in tier1b:
                    tier1b.append(t)

        tier3: list[str] = []
        for key, targets in self._name_index.items():
            if key and key in qn:
                for t in targets:
                    if t not in tier3:
                        tier3.append(t)

        out: list[str] = []
        for t in (*tier1a, *tier2, *tier1b, *tier3):
            if t not in out:
                out.append(t)
        return out[:_MAX_EVENTS_TOTAL]

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
