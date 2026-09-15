"""DM2 T3: 触发器是纯函数, 判定表可枚举. 域码识别是注入的 (D1 口径), 这里只测组合逻辑
和范围词类; 不重测 _query_domains 本身 (它有自己的测试)."""
import pytest
from server.dossier_trigger import decide_dossier

def _qd_hit(q): return ["DS"]
def _qd_none(q): return []

@pytest.mark.parametrize("q", [
    "本研究中，哪些数据适合进入 sdtm 的 ds domain？",
    "この試験で収集しているデータのうち、SDTM の DS ドメインに入れるべきものはどれですか？",
    "Which data collected in our study should go into the Disposition dataset?",
    "In this study, which EDC items belong in DS?",
    "当試験の EDC 項目で DS に入るもの",
])
def test_auto_fires_on_domain_plus_scope(q):
    d = decide_dossier(q, "auto", True, _qd_hit)
    assert d.attach and d.reason == "auto:domain+scope" and d.domains == ("DS",)

@pytest.mark.parametrize("q", [
    "DS 域有哪些变量？",                       # 域码但无范围词 (纯 CDISC 题)
    "What are the DSCAT values?",
    "What is EDC in SDTM terms, relative to DS?",       # 裸 EDC 定义题, 不是范围问句
    "Which DS variables are required in our dataset?",  # 代词+介词, 非 study/trial 锚定
    "How do the four Trial Design domains TA, TE, TV and TI work together?",  # fix round 2: "f<our Trial>" 词边界误触发回归例
])
def test_auto_quiet_without_scope(q):
    d = decide_dossier(q, "auto", True, _qd_hit)
    assert not d.attach and d.reason == "auto:no_match"

def test_auto_quiet_without_domain():
    d = decide_dossier("本研究の登録手順を教えて", "auto", True, _qd_none)
    assert not d.attach and d.reason == "auto:no_match" and d.domains == ()

def test_forced_on_and_off_override_auto():
    assert decide_dossier("何でも", "on", True, _qd_none).reason == "forced_on"
    assert decide_dossier("本研究 DS", "off", True, _qd_hit).reason == "forced_off"

def test_master_switch_beats_forced_on():
    d = decide_dossier("本研究 DS", "on", False, _qd_hit)
    assert not d.attach and d.reason == "disabled"

def test_query_domains_exception_is_quiet_not_500():
    def boom(q): raise RuntimeError("x")
    d = decide_dossier("本研究 DS", "auto", True, boom)
    assert not d.attach and d.reason == "auto:no_match"
