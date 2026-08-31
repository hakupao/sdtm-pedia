"""Rule 9 (联网参考的反捏造边界) 进 system prompt 的条件与回滚闸 (spec §5 §9.3)。

`scripts/tests/` 无 make_engine helper (已确认), 故本地直接构造 —— 只测 prompt 组装,
用 __new__ 绕开 chroma/embedding 初始化。
"""
from server.rag import RAGEngine


def _engine(*, web_search_enabled: bool):
    eng = RAGEngine.__new__(RAGEngine)
    eng.prompt_guardrail_enabled = True
    eng.web_search_enabled = web_search_enabled
    eng._routing_md = "(routing)"
    eng._index_md = "(index)"
    return eng


def test_rule9_absent_by_default():
    """回滚闸: 不开启时 system prompt 里没有任何 Rule 9 痕迹。"""
    sp = _engine(web_search_enabled=False)._build_system_prompt()
    assert "[Web:" not in sp
    assert "UNVERIFIED" not in sp


def test_rule9_present_when_enabled():
    sp = _engine(web_search_enabled=True)._build_system_prompt()
    assert "[Web:" in sp
    assert "Cxxxxx" in sp                      # 9(b) 禁码
    assert "class/category" in sp              # 9(b) 禁 class 归属
    assert "inference" in sp.lower()           # 9(c) 标推测


def test_rule9_is_the_only_difference():
    """开关只增加 Rule 9 那一段, 不动其它任何一个字节 (逐字节回滚闸)。"""
    off = _engine(web_search_enabled=False)._build_system_prompt()
    on = _engine(web_search_enabled=True)._build_system_prompt()
    assert on != off
    idx = on.find("9. **Web results are UNVERIFIED")
    assert idx > 0, "Rule 9 段落起始锚点变了, 同步更新本测试"
    tail = on.find("---\n\n## Routing Guide")
    assert tail > idx
    assert on[:idx] + on[tail:] == off         # 挖掉 Rule 9 段后必须逐字节还原
