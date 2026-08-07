"""扫描器只做一件事: 列出 top-N 里不被任何 gold 匹配的条目。判定留给人/独立 agent。"""
from eval.scan_gold_gaps import unmatched_in_top_n


class _C:
    def __init__(self, source, section, sim):
        self.source, self.section, self.similarity = source, section, sim


def test_lists_entries_no_gold_matches():
    chunks = [
        _C("kb/chapters/ch04.md", "4.2.2 Two-character Domain Identifier", 0.70),
        _C("kb/chapters/ch02_fundamentals.md", "whole_file", 0.56),
    ]
    out = unmatched_in_top_n(chunks, ["chapters/ch02"], n=3)
    assert [o["source"] for o in out] == ["kb/chapters/ch04.md"]
    assert out[0]["rank"] == 1


def test_respects_section_level_gold():
    chunks = [_C("kb/VARIABLE_INDEX.md", "§一 通用变量: ARMCD", 0.6)]
    # section 级 gold 未命中 -> 该条目算 unmatched
    assert unmatched_in_top_n(chunks, ["VARIABLE_INDEX.md#§一 通用变量: ARM$"], n=3)
    # 命中 -> 不算
    assert not unmatched_in_top_n(chunks, ["VARIABLE_INDEX.md#§一 通用变量: ARMCD$"], n=3)


def test_n_truncates():
    chunks = [_C(f"kb/f{i}.md", "s", 0.5) for i in range(10)]
    assert len(unmatched_in_top_n(chunks, ["nothing"], n=3)) == 3


def test_or_group_gold_counts_as_matched():
    chunks = [_C("kb/domains/DM/spec.md", "DOMAIN", 0.6)]
    assert not unmatched_in_top_n(chunks, [], n=3, any_of=["domains/DM/spec.md"])


def test_scanner_actually_delegates_to_source_matches(monkeypatch):
    """运行期锁: 扫描工具必须真的走 source_matches, 不是自带一份等价逻辑。

    Task 2 的结构锁 (inspect.getsource) 只锁文本、防漂移; 这条锁的是**运行时真的
    调用了那个函数** —— 把它 patch 成恒 True 后, 本该 unmatched 的条目必须消失。
    两端合起来才让"同语义"成为结构保证而非约定 (Task 2 评审的建议)。
    """
    import eval.scan_gold_gaps as m

    chunks = [_C("kb/whatever.md", "S", 0.5)]
    assert unmatched_in_top_n(chunks, ["nothing-matches-this"], n=3)

    monkeypatch.setattr(m, "source_matches", lambda *a, **k: True)
    assert not unmatched_in_top_n(chunks, ["nothing-matches-this"], n=3)
