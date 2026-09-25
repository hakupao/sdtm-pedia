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

# 2026-09-25 用户裁定: attempt 3 (Claude) 未达标期间暂停 auto 挂载, 手动 on 照挂.
# 暂停时命中题报 auto:paused (前端据此提示「可手动开」), 未命中题仍是 auto:no_match.
def test_auto_paused_reports_would_attach_but_does_not():
    d = decide_dossier("本研究 DS", "auto", True, _qd_hit, auto_attach=False)
    assert not d.attach and d.reason == "auto:paused" and d.domains == ("DS",)

def test_auto_paused_leaves_no_match_as_no_match():
    d = decide_dossier("DS 域有哪些变量？", "auto", True, _qd_hit, auto_attach=False)
    assert not d.attach and d.reason == "auto:no_match"

def test_auto_paused_does_not_block_forced_on():
    assert decide_dossier("何でも", "on", True, _qd_none, auto_attach=False).attach

# attempt 4: 规则句里的语言要求两轮压不住 sonnet (en 问 → ja 答), 改为结构性手段:
# 按问句文字种类确定答题语言, 研读包挂上时在 user 消息末尾追加一行. 纯函数, 可枚举.
from server.dossier_trigger import answer_language

@pytest.mark.parametrize("q,lang", [
    ("この試験で収集しているデータのうち DS はどれ？", "ja"),
    ("本研究中，哪些数据适合进入 sdtm 的 ds domain？", "zh"),
    ("In our study, which collected data items belong in the ae domain?", "en"),
    ("本研究の DS", "ja"),          # 漢字 + 仮名 ⇒ 日本語 (仮名が決め手)
    ("DS", "en"),                   # 文字種なし ⇒ en に倒す
    # 审查负例: 问句里嵌入的 EDC 表单/项目名 (日文原文) 不得决定答题语言
    ("In our study, which items on the 有害事象 form map to AE?", "en"),
    ("In our study, which fields on the バイタルサイン page go to VS?", "en"),
    ("本研究中 バイタルサイン 页面的哪些字段进 VS？", "zh"),
    ("本研究里「有害事象・副作用」表单的字段应该进 AE 吗？", "zh"),
    ("Which items in 「治療経過」 belong to EX in this study?", "en"),
])
def test_answer_language_by_script(q, lang):
    assert answer_language(q) == lang
