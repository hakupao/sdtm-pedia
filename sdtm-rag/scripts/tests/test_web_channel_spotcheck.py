"""eval/web_channel_spotcheck.py 的 I-6 机检 (关键词形状扫描) 回归钉子。

背景 (复审 v4→v5): `_hard_fact_keyword_hits()` 是给 Rule 9(b) 剩下两样硬事实
(class/category 归属, Core/Role/Type) 做的最粗形状扫描——本意是"抓不全但至少
提示人多看一眼"。复审发现它比自己的描述还弱得多: 大小写敏感只认大写字段名
(`Class`), 而英文散文里写归属最自然是小写 (`class`); 扫描面又只看含 `[Web:`
的那句, 漏掉"引用单独一句、断言紧跟下一句"这种最常见的"先引后断"写法。合起来
的后果是: 这一列能抓到的恰好是最不像问题的形状, 最可能真出问题的形状全漏——
比"没有这一列"更危险, 因为它会让人误以为这部分已经被机检覆盖。

下面四个用例 (A/B/C/D) 是复审给的原始用例, 加一条负例防止"改成无脑全命中"
这种反向回归。
"""
from eval.web_channel_spotcheck import _hard_fact_keyword_hits

_RETR = "(retrieved 2026-08-31)"


def test_A_uppercase_class_same_sentence_hits():
    """设计最初针对的形状: KB 字段名式的大写 Class, 同句。"""
    ans = f"Some blog treats FA as a special Class domain here [Web: https://e.com/1 {_RETR}]."
    hits = _hard_fact_keyword_hits(ans)
    assert [kw for kw, _ in hits] == ["Class"]


def test_B_lowercase_class_same_sentence_hits():
    """英文散文里写归属的常态是小写——大小写敏感会漏掉这个最常见的写法。"""
    ans = f"Some blog treats FA as a special class domain here [Web: https://e.com/1 {_RETR}]."
    hits = _hard_fact_keyword_hits(ans)
    assert [kw for kw, _ in hits] == ["class"]


def test_C_inference_in_the_sentence_after_the_citation_hits():
    """最危险的漏检形状: 引用单独一句, 支撑的断言紧跟下一句 ("先引后断")。
    断言句本身不含 `[Web:`, 只扫"含引用的句子"会把它整句漏掉。"""
    ans = (f"Several teams do this [Web: https://e.com/1 {_RETR}]. "
           "It is a Findings class domain.")
    hits = _hard_fact_keyword_hits(ans)
    assert [kw for kw, _ in hits] == ["class"]
    assert hits[0][1] == "It is a Findings class domain."


def test_D_core_and_req_control_hits():
    """对照用例: Core/Req 组合, 同句, 两个都要命中。"""
    ans = f"A blog claims this variable is Core and Req [Web: https://e.com/1 {_RETR}]."
    hits = _hard_fact_keyword_hits(ans)
    assert sorted(kw for kw, _ in hits) == ["Core", "Req"]


def test_no_hard_fact_words_near_citation_does_not_hit():
    """负例: 扩大扫描面 (+ 大小写不敏感) 之后不能变成无脑全命中——
    [Web:] 句和它后一句里都没有硬事实词, 必须是空列表。"""
    ans = (f"Some blog explains general best practices for data mapping "
           f"[Web: https://e.com/1 {_RETR}]. Nothing technical here.")
    assert _hard_fact_keyword_hits(ans) == []


def test_scan_does_not_reach_two_sentences_after_the_citation():
    """只扩后一句, 不无限扩散: 硬事实词出现在引用后第二句时不应命中。"""
    ans = (f"Several teams do this [Web: https://e.com/1 {_RETR}]. "
           "It works well in practice. It is technically a Findings class domain.")
    assert _hard_fact_keyword_hits(ans) == []
