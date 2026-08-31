"""eval/web_channel_spotcheck.py 的 I-6 机检 (关键词形状扫描) 回归钉子。

背景 (复审两轮): `_hard_fact_keyword_hits()` 是给 Rule 9(b) 剩下两样硬事实
(class/category 归属, Core/Role/Type) 做的最粗形状扫描——本意是"抓不全但至少
提示人多看一眼"。

第一轮复审发现: 大小写敏感只认大写字段名 (`Class`), 英文散文里写归属最自然
是小写 (`class`); 扫描范围又只看含 `[Web:` 的那句, 漏掉"先引后断"的推论句。
第一轮的修法 (大小写不敏感 + 往"含引用的句子"后面扩一句) 看似解决了这两点,
但**方向搞反了**——第二轮复审在真实语料 (`_answers.md` 三题原文) 上验证:
引用标记的标准落点是句末标点**之后**, 按 ASCII 句子标点切分, 断点恰好落在
句号后面, 于是"含 [Web: 的片段"其实是引用后面那句, 真正带硬事实词的断言句
被切到**前一个**片段, 反而不在扫描范围内; 而这套按句切分对中日文还整体失效
(全角句号 `。` 不触发 ASCII 标点切分), 导致两种语言的扫描粒度不一致。

第二轮改成不再按 ASCII 句子标点切、只按 markdown 段落/bullet 行 (`\n`) 切,
外加补上 `Type` 关键词 (文档写了但代码里一直没有) 和规则复数支持
(`Qualifier` → `Qualifiers`, 真实语料里 Q1 答案实测漏检)。

下面的用例覆盖复审给的场景 (本轮 A/B/C/D 已替换成复审第二轮的定义, 与首轮
report 里"A/B/C/D"的编号不是同一组用例) + 若干边界情形。
"""
from eval.web_channel_spotcheck import _hard_fact_keyword_hits

_RETR = "(retrieved 2026-08-31)"


def test_A_citation_trails_the_claim_after_a_period_hits():
    """复审第二轮定位的真正根因场景: 引用标记落在句末标点之后, 跟支撑它的
    断言同处一条 markdown 行——按 ASCII 句子标点切分时这个场景会漏检
    (断言句被切到前一个片段), 按段落/行切分后必须命中。"""
    ans = (f"The domain belongs to the Events Class. "
           f"[Web: https://x.example.com/y {_RETR}] Next sentence here.")
    hits = _hard_fact_keyword_hits(ans)
    assert [kw for kw, _ in hits] == ["Class"]


def test_B_lowercase_class_same_line_hits():
    """英文散文里写归属的常态是小写——大小写敏感会漏掉这个最常见的写法。"""
    ans = f"Some blog treats FA as a special class domain here [Web: https://e.com/1 {_RETR}]."
    hits = _hard_fact_keyword_hits(ans)
    assert [kw for kw, _ in hits] == ["class"]


def test_C_plural_qualifiers_hits():
    """规则复数: 真实语料 (Q1 答案) 里 "Supplemental **Qualifiers**" 就是这个
    形状, 修复前 `\\bQualifier\\b` 会因为词尾多了个 's' 匹配不上。"""
    ans = (f"Salyers used the term Supplemental Qualifiers in that paper "
           f"[Web: https://e.com/1 {_RETR}].")
    hits = _hard_fact_keyword_hits(ans)
    assert [kw for kw, _ in hits] == ["Qualifier"]


def test_D_no_hard_fact_words_near_citation_does_not_hit():
    """负例: 扩大扫描面 (大小写不敏感 + 段落级窗口 + 容复数) 之后不能变成无脑
    全命中——[Web:] 所在整行都没有硬事实词, 必须是空列表。"""
    ans = (f"Some blog explains general best practices for data mapping "
           f"[Web: https://e.com/1 {_RETR}]. Nothing technical here.")
    assert _hard_fact_keyword_hits(ans) == []


def test_uppercase_class_same_line_hits():
    """设计最初针对的形状 (第一轮遗留用例, 仍然有效): KB 字段名式的大写
    Class, 同行。"""
    ans = f"Some blog treats FA as a special Class domain here [Web: https://e.com/1 {_RETR}]."
    hits = _hard_fact_keyword_hits(ans)
    assert [kw for kw, _ in hits] == ["Class"]


def test_core_and_req_combo_hits_both():
    """对照用例 (第一轮遗留, 仍然有效): Core/Req 组合, 同行, 两个都要命中。"""
    ans = f"A blog claims this variable is Core and Req [Web: https://e.com/1 {_RETR}]."
    hits = _hard_fact_keyword_hits(ans)
    assert sorted(kw for kw, _ in hits) == ["Core", "Req"]


def test_type_keyword_hits():
    """`Type` 曾经完全不在关键词元组里 (文档写着扫 Core/Role/Class/Type, 代码
    只有 Core/Role/Class/Topic, 少了 Type)——单独钉一条防止再次漏掉。"""
    ans = f"A blog claims QNAM is Type Char [Web: https://e.com/1 {_RETR}]."
    hits = _hard_fact_keyword_hits(ans)
    assert "Type" in [kw for kw, _ in hits]


def test_scan_reaches_across_multiple_ascii_sentences_on_the_same_line():
    """有意的行为 (不是回归): 一条 markdown bullet 常横跨好几个 ASCII 句子,
    段落/行级窗口不再按句子数量设界——硬事实词出现在引用所在行的第三个 ASCII
    句子里, 依然要命中 (第一轮曾把"扩散"当成需要挡住的东西, 是基于错误的
    按句切分模型; 段落级窗口下这是预期行为, 不是需要挡住的东西)。"""
    ans = (f"Several teams do this [Web: https://e.com/1 {_RETR}]. "
           "It works well in practice. It is technically a Findings class domain.")
    hits = _hard_fact_keyword_hits(ans)
    assert [kw for kw, _ in hits] == ["class"]


def test_hard_fact_word_on_an_unrelated_line_is_not_pulled_in():
    """段落/行级窗口仍然提供隔离: 硬事实词出现在**不含引用**的相邻行里,
    不应该被拉进来——窗口是"含 [Web: 的那一行", 不是"整个答案"。"""
    ans = ("This line mentions Core and Role but has no citation.\n"
           f"This other line has the citation [Web: https://e.com/1 {_RETR}] and nothing else.")
    assert _hard_fact_keyword_hits(ans) == []


def test_no_citation_no_scan():
    """完全没有 [Web:] 引用的答案, 扫描面为空, 不应该报任何命中
    (即便正文里到处都是 Core/Role/Class/Type 这类词——那些是 KB 来源的正常
    内容, 不该被这项机检碰到)。"""
    ans = "QNAM is the Topic variable, Type Char, Core Req [Source: domains/SUPPQUAL/spec.md]."
    assert _hard_fact_keyword_hits(ans) == []
