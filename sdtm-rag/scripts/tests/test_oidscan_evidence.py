import json

import pytest

from scripts.oidscan_evidence import (
    ALLOWLIST,
    DEFAULT_MIN_LEN,
    KNOWN_PUBLIC_COLLISIONS,
    compile_needle_pattern,
    load_cdisc_domain_codes,
    load_cdisc_variable_names,
    load_label_needles,
    load_needles,
    main,
    mask_needle,
    scan_file,
)


def _write_catalog(tmp_path, forms=(), items=(), events=(), activities=()):
    cat = {
        "forms": [{"oid": o} for o in forms],
        "items": [{"item_oid": o} for o in items],
        "events": [{"oid": o} for o in events],
        "activities": [{"oid": o} for o in activities],
    }
    p = tmp_path / "catalog.json"
    p.write_text(json.dumps(cat), encoding="utf-8")
    return p


def _write_full_catalog(tmp_path, **pools):
    """写入含 label/name 字段的合成 catalog (供 load_label_needles / N3 测试用)。
    pools 直接是四池的记录列表 (每条已是完整 dict), 不套 _write_catalog 的简化形状。"""
    cat = {k: pools.get(k, []) for k in ("forms", "items", "events", "activities")}
    p = tmp_path / "catalog.json"
    p.write_text(json.dumps(cat, ensure_ascii=False), encoding="utf-8")
    return p


def test_load_needles_excludes_pure_numeric(tmp_path):
    """行号 / 长度这类纯数字字段不能混进 needle 集 (会到处假阳性)。"""
    cat = _write_catalog(tmp_path, forms=["偽FRM01", "12"], items=["偽ITM01", "34"])
    needles = load_needles(cat)
    assert needles == {"偽FRM01", "偽ITM01"}


def test_load_needles_excludes_given_set(tmp_path):
    # needle 必须 >= min_len, 否则本测试会因"被长度剔除"而通过, 证不到 exclude 生效
    cat = _write_catalog(tmp_path, forms=["偽FRM01", "TESTCD"])
    needles = load_needles(cat, exclude={"TESTCD"})
    assert needles == {"偽FRM01"}


def test_load_needles_drops_values_shorter_than_min_len(tmp_path):
    """短 OID (2-3 字符) 与大写缩写 / 模板占位符 / Python 变量名大量撞车。

    实测依据 (c1_redline_triage.md): 闸对 `scripts/ server/` 的 26 处命中**全部**
    来自 4 个 2-3 字符 OID needle, 无一是真泄漏 (假阳性率 87.5%)。与 label 池
    (`load_label_needles(min_len=4)`) 同一处置, 此前 OID 池漏掉这一手。
    """
    cat = _write_catalog(tmp_path, forms=["偽F1", "偽FORM1"], items=["偽I", "偽ITEM1"])
    needles = load_needles(cat, min_len=4)
    assert needles == {"偽FORM1", "偽ITEM1"}   # 6 字保留, 3 字/2 字被剔除


def test_load_needles_unions_four_pools(tmp_path):
    cat = _write_catalog(tmp_path, forms=["偽FRM01"], items=["偽ITM01"],
                         events=["偽EVT01"], activities=["偽ACT01"])
    assert load_needles(cat) == {"偽FRM01", "偽ITM01", "偽EVT01", "偽ACT01"}


# ---- N3: label/name 池 (spec §8 第 2 条 "OID / label" 并列, 只扫 OID 不算闭合) ----

def test_load_label_needles_collects_all_named_fields(tmp_path):
    cat = _write_full_catalog(
        tmp_path,
        forms=[{"oid": "偽FRM01", "name": "偽表单名称甲", "description": "偽表单说明甲"}],
        items=[{"item_oid": "偽ITM01", "label": "偽项目标签甲", "group_name": "偽分组甲",
                "form_name": "偽表单名甲"}],
        events=[{"oid": "偽EVT01", "name": "偽事件名称甲"}],
        activities=[{"oid": "偽ACT01", "name": "偽活动名称甲", "event_name": "偽关联事件甲"}],
    )
    needles = load_label_needles(cat)
    assert needles == {
        "偽表单名称甲", "偽表单说明甲", "偽项目标签甲", "偽分组甲", "偽表单名甲",
        "偽事件名称甲", "偽活动名称甲", "偽关联事件甲",
    }


def test_load_label_needles_drops_values_shorter_than_min_len(tmp_path):
    """group_name/form_name 常见 1-3 字通用词, 太短会重蹈"纯数字"式假阳性覆辙。"""
    cat = _write_full_catalog(
        tmp_path,
        items=[{"item_oid": "偽ITM01", "label": "偽", "group_name": "偽甲乙丙丁"}],
    )
    needles = load_label_needles(cat, min_len=4)
    assert needles == {"偽甲乙丙丁"}   # 4 字保留, 1 字 "偽" 被剔除


def test_load_label_needles_ignores_missing_and_empty_fields(tmp_path):
    cat = _write_full_catalog(
        tmp_path,
        forms=[{"oid": "偽FRM01"}],                 # 无 name/description 键
        items=[{"item_oid": "偽ITM01", "label": ""}],  # 空字符串
    )
    assert load_label_needles(cat) == set()


def test_load_label_needles_excludes_given_set(tmp_path):
    cat = _write_full_catalog(
        tmp_path,
        forms=[{"oid": "偽FRM01", "name": "公開語彙甲甲"}],
    )
    needles = load_label_needles(cat, exclude={"公開語彙甲甲"})
    assert needles == set()


def test_compile_needle_pattern_matches_underscore_delimited_filename():
    """核心行为: 不是 \\b —— 下划线两侧也要能命中 (study__form__item.md 约定)。"""
    pattern = compile_needle_pattern({"偽TESTFORM1", "偽TESTITEM1"})
    assert pattern.search("st01__偽TESTFORM1__偽TESTITEM1.md")


def test_compile_needle_pattern_rejects_substring_of_longer_word():
    """整词边界: needle 是更长词的一部分时不该命中 (字母数字边界外)。"""
    pattern = compile_needle_pattern({"偽AE"})
    assert not pattern.search("偽AEXTRA the operation")
    assert not pattern.search("some偽AE")


def test_compile_needle_pattern_matches_standalone_token():
    pattern = compile_needle_pattern({"偽AE"})
    assert pattern.search("这是 偽AE 命中")


def test_compile_needle_pattern_matches_multiword_label_needle():
    """label 池的 needle 可能带空格/标点, 边界只检查整个子串两端, 不逐词切。"""
    pattern = compile_needle_pattern({"偽多字标签 甲乙"})
    assert pattern.search("前缀 偽多字标签 甲乙 后缀")
    assert not pattern.search("偽多字标签甲乙丙")   # 不同子串, 不该命中


def test_scan_file_reports_line_numbers(tmp_path):
    p = tmp_path / "evidence.md"
    p.write_text("line one\n偽ITEM1 appears here\nline three\n偽ITEM1 twice\n",
                 encoding="utf-8")
    pattern = compile_needle_pattern({"偽ITEM1"})
    hits = scan_file(p, pattern)
    assert hits == [(2, "偽ITEM1"), (4, "偽ITEM1")]


def test_scan_file_skips_undecodable_file(tmp_path):
    p = tmp_path / "binary.bin"
    p.write_bytes(b"\xff\xfe\x00\x01" + "偽ITEM1".encode("utf-16-le"))
    pattern = compile_needle_pattern({"偽ITEM1"})
    # 不崩溃, 二进制解码失败按"不在扫描面"处理 (不是 LEAK, 也不是假 CLEAN 断言)
    assert scan_file(p, pattern) == []


def test_load_cdisc_domain_codes_empty_when_dir_missing(tmp_path):
    assert load_cdisc_domain_codes(tmp_path / "nope") == set()


def test_load_cdisc_domain_codes_reads_directory_names(tmp_path):
    d = tmp_path / "domains"
    d.mkdir()
    (d / "AE").mkdir()
    (d / "DM").mkdir()
    (d / "not_a_dir.txt").write_text("x", encoding="utf-8")
    assert load_cdisc_domain_codes(d) == {"AE", "DM"}


def test_load_cdisc_variable_names_empty_when_file_missing(tmp_path):
    assert load_cdisc_variable_names(tmp_path / "nope.md") == set()


def test_load_cdisc_variable_names_parses_first_column(tmp_path):
    p = tmp_path / "VARIABLE_INDEX.md"
    p.write_text(
        "| Variable | Domains |\n|--------|------|\n| AGE | 1 |\n| VISIT | 2 |\n",
        encoding="utf-8",
    )
    assert load_cdisc_variable_names(p) == {"AGE", "VISIT"}


# ---- N1: target 路径缺失必须 fail-closed, 不许悄悄放行成 CLEAN ----

def test_iter_target_files_reports_missing_targets(tmp_path):
    from scripts.oidscan_evidence import iter_target_files

    real = tmp_path / "a.md"
    real.write_text("x", encoding="utf-8")
    missing = tmp_path / "does_not_exist"

    files, missing_out = iter_target_files([real, missing])
    assert [f.name for f in files] == ["a.md"]
    assert missing_out == [missing]


def test_iter_target_files_expands_directory_and_skips_binary(tmp_path):
    from scripts.oidscan_evidence import iter_target_files

    (tmp_path / "a.md").write_text("x", encoding="utf-8")
    (tmp_path / "b.png").write_bytes(b"\x89PNG")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "c.txt").write_text("y", encoding="utf-8")

    files, missing = iter_target_files([tmp_path])
    names = {p.name for p in files}
    assert names == {"a.md", "c.txt"}
    assert missing == []


def test_main_fails_closed_on_missing_target(tmp_path, capsys):
    """N1 回归钉: 拼错路径 / cwd 不对必须非零退出并明说缺了哪个, 不能打印 CLEAN。"""
    cat = _write_catalog(tmp_path, forms=["偽FRM01"])
    missing_target = tmp_path / "typo_path_does_not_exist"
    rc = main([str(missing_target), "--catalog", str(cat)])
    out = capsys.readouterr().out
    assert rc == 2
    assert "ABORT" in out
    assert "typo_path_does_not_exist" in out
    assert "CLEAN:" not in out           # "CLEAN:" 是真正的过闸小节标题 (非子串误伤)


# ---- N2: 默认扫描面锚定仓库根, 不依赖调用时 cwd ----

def test_default_targets_are_absolute_and_git_root_anchored():
    from scripts.oidscan_evidence import DEFAULT_TARGETS, GIT_ROOT, REPO_ROOT

    assert all(t.is_absolute() for t in DEFAULT_TARGETS)
    # evidence/ 只在 sdtm-rag/ 下, docs/ 两处都要覆盖 (repo 根 + sdtm-rag/), 闸自身也在内
    assert REPO_ROOT / "evidence" in DEFAULT_TARGETS
    assert GIT_ROOT / "docs" in DEFAULT_TARGETS
    assert REPO_ROOT / "docs" in DEFAULT_TARGETS
    assert any(t.name == "oidscan_evidence.py" for t in DEFAULT_TARGETS)


def test_default_targets_include_source_trees():
    """默认扫描面必须覆盖源码 —— C1 那次真实泄漏就发生在 `scripts/tests/` 里, 而当时
    默认面只有 evidence/ + docs/, 于是"手跑一次闸"这个动作天然看不见它 (判定书 §4
    记的"红线扫描有结构性盲区: 对照产物而非源")。

    pre-commit 只管**新进 git 的**文件; 存量面只能靠不带参数的手动全仓审计, 所以
    默认面必须包含源码树, 否则那次审计仍是"扫了个寂寞却给绿灯"。
    """
    from scripts.oidscan_evidence import DEFAULT_TARGETS, REPO_ROOT

    assert REPO_ROOT / "scripts" in DEFAULT_TARGETS
    assert REPO_ROOT / "server" in DEFAULT_TARGETS


def test_find_git_root_walks_up_to_dot_git(tmp_path):
    from scripts.oidscan_evidence import _find_git_root

    (tmp_path / ".git").mkdir()
    nested = tmp_path / "a" / "b" / "c.py"
    nested.parent.mkdir(parents=True)
    nested.write_text("x", encoding="utf-8")
    assert _find_git_root(nested) == tmp_path


def test_find_git_root_raises_when_no_dot_git_found(tmp_path):
    from scripts.oidscan_evidence import _find_git_root

    orphan = tmp_path / "no_git_here.py"
    orphan.write_text("x", encoding="utf-8")
    with pytest.raises(RuntimeError):
        _find_git_root(orphan)


# ---- main() 端到端 (CLI 行为), 全部用 偽 前缀合成数据 ----

def test_main_clean_when_no_hits(tmp_path, capsys):
    cat = _write_catalog(tmp_path, forms=["偽FRM01"])
    target = tmp_path / "clean.md"
    target.write_text("nothing sensitive here", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat)])
    assert rc == 0
    assert "CLEAN" in capsys.readouterr().out


def test_main_leak_when_hit_not_allowlisted(tmp_path, capsys):
    cat = _write_catalog(tmp_path, forms=["偽FRM01"])
    target = tmp_path / "leaky.md"
    target.write_text("包含 偽FRM01 在正文里", encoding="utf-8")
    # --show-values: 本测试要断言具体命中了哪个 needle, 数据是合成 偽 前缀值, 打真值无害。
    rc = main([str(target), "--catalog", str(cat), "--show-values"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "LEAK" in out
    assert "偽FRM01" in out


def test_main_catches_label_leak_not_just_oid(tmp_path, capsys):
    """N3 回归钉: 只含真实 label (不含任何真实 OID) 的文件也必须被抓到。"""
    cat = _write_full_catalog(
        tmp_path,
        items=[{"item_oid": "偽ITM01", "label": "偽長い項目ラベル甲乙丙"}],
    )
    target = tmp_path / "label_only_leak.md"
    target.write_text("正文里混进了 偽長い項目ラベル甲乙丙 这段标签文本", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat), "--show-values"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "偽長い項目ラベル甲乙丙" in out


def test_main_aborts_on_missing_catalog(tmp_path, capsys):
    rc = main([str(tmp_path), "--catalog", str(tmp_path / "nope.json")])
    assert rc == 2
    assert "ABORT" in capsys.readouterr().out


def test_main_aborts_on_empty_catalog(tmp_path, capsys):
    cat = _write_catalog(tmp_path)   # 四池全空
    rc = main([str(tmp_path), "--catalog", str(cat)])
    assert rc == 2
    assert "ABORT" in capsys.readouterr().out


def test_allowlist_entries_are_excluded_from_leak(tmp_path, monkeypatch, capsys):
    """守门人: allowlist 命中的 (文件, needle) 不计入 LEAK, 但仍打印在报告里。"""
    fake_rel = "scripts/tests/_fake_allowlisted.md"
    monkeypatch.setitem(ALLOWLIST, (fake_rel, "偽FRM01"), "测试用假条目")
    cat = _write_catalog(tmp_path, forms=["偽FRM01"])
    target_dir = tmp_path / "scripts" / "tests"
    target_dir.mkdir(parents=True)
    target = target_dir / "_fake_allowlisted.md"
    target.write_text("偽FRM01 出现在这里", encoding="utf-8")

    import scripts.oidscan_evidence as mod
    monkeypatch.setattr(mod, "GIT_ROOT", tmp_path)   # rel 现在相对 GIT_ROOT (N2 修复)
    rc = main([str(target), "--catalog", str(cat)])
    out = capsys.readouterr().out
    assert rc == 0
    assert "allowlist 命中" in out
    assert "CLEAN" in out
    assert "LEAK:" not in out            # "LEAK:" 是真正的泄漏小节标题 (非子串误伤)


def test_known_public_collisions_are_excluded_globally(tmp_path, capsys):
    """KNOWN_PUBLIC_COLLISIONS 里的 needle 即便是 catalog 真实 OID, 也不该被当泄漏 ——
    这批是公开/通用词汇 (CT/K/MAX/... ) 与私密 OID 偶然撞车, 见模块 docstring 教训。"""
    # 必须挑 >= min_len 的条目: 短条目会被长度剔除, 本测试就证不到 exclude 这条路径
    collision_needle = next(n for n in KNOWN_PUBLIC_COLLISIONS if len(n) >= 4)
    cat = _write_catalog(tmp_path, forms=[collision_needle, "偽FRM01"])
    target = tmp_path / "doc.md"
    target.write_text(f"讨论 {collision_needle} 与 偽FRM01 都出现", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat), "--show-values"])
    out = capsys.readouterr().out
    assert rc == 1                       # 偽FRM01 仍应被抓到
    leak_section = out.split("LEAK:", 1)[1]
    assert "偽FRM01" in leak_section
    assert f"'{collision_needle}'" not in leak_section   # 公开词汇不算泄漏, 不进 LEAK 明细


def test_short_oid_paired_with_its_label_still_leaks_via_label_pool(tmp_path, capsys):
    """min_len 造出的盲区是**有界的**: 短 OID 与自身 label 成对出现时, label 侧仍抓得到。

    这条钉住 `load_needles` docstring 里"盲区小于被剔除的 OID 数"这个论断 —— 本仓
    实测 70 条用短 OID 的记录里 63 条的名称仍在 label 池, 全盲只剩 7 条。C1 那次
    真实泄漏正是"OID 与其 label 同行成对"的形态 (识别性最强的一种), 该形态必须
    保持可检出, 否则 min_len 就不是降噪而是拆闸。
    """
    cat = _write_full_catalog(
        tmp_path,
        items=[{"item_oid": "偽I", "label": "偽項目標籤甲"}],   # OID 2 字 (低于 min_len)
    )
    target = tmp_path / "paired.md"
    target.write_text("# 偽項目標籤甲 (偽I)", encoding="utf-8")   # C1 那次的成对形态
    rc = main([str(target), "--catalog", str(cat)])
    out = capsys.readouterr().out
    assert rc == 1, "短 OID 与自身 label 成对出现时必须仍判 LEAK"
    assert "<LABEL len=6>" in out          # 由 label 侧抓到 (掩码输出)
    assert "<OID" not in out.split("LEAK:", 1)[1]   # OID 侧确实已被 min_len 剔除


# ---- 豁免条目可达性 (C2 前置): 永不触发的豁免 = 死代码 ----

def test_allowlist_entries_are_reachable_under_default_min_len():
    """allowlist 条目若短于 `DEFAULT_MIN_LEN`, 其 needle 根本进不了任何 needle 池 ——
    该条目永远不会被查询, 是恒假的死代码。

    本仓刚吃过这个亏 (Ruling C1: events/activities guard "原写法恒假是死代码")。
    给 OID 池加 min_len 会一次性造出 11 条这样的死条目, 故把"不许留死豁免"钉成测试:
    一个要接进 CI 的闸, 不能悄悄积累永不触发的豁免。
    """
    # 掩码: allowlist 的 needle 不保证是公开词汇, 断言失败信息会进 CI 日志 ——
    # 一条防红线的测试自己打真值, 就是模块 docstring 点名的"绕道进日志"那个模式。
    dead = sorted(
        f"{path}:<len={len(needle)}>"
        for (path, needle) in ALLOWLIST if len(needle) < DEFAULT_MIN_LEN
    )
    assert dead == [], (
        f"{len(dead)} 条 allowlist 条目的 needle 短于 DEFAULT_MIN_LEN="
        f"{DEFAULT_MIN_LEN}, 永不触发 (死代码): {dead}"
    )


def test_known_public_collisions_are_reachable_under_default_min_len():
    """同上: `exclude` 在两个池里都作用于已过 min_len 的取值, 故短于 min_len 的
    公开词汇条目同样恒不触发。"""
    # 这批按定义是公开 CDISC 词汇, 打真值无害; 仍与上一条保持同一掩码形状便于比对
    dead = sorted(f"<len={len(n)}>" for n in KNOWN_PUBLIC_COLLISIONS
                  if len(n) < DEFAULT_MIN_LEN)
    assert dead == [], (
        f"{len(dead)} 条 KNOWN_PUBLIC_COLLISIONS 条目短于 DEFAULT_MIN_LEN="
        f"{DEFAULT_MIN_LEN}, 永不触发 (死代码)"
    )


# ---- 输出脱敏 (复审第 3 轮): 默认掩码, --show-values 才打真值 ----

def test_mask_needle_reports_kind_and_length_not_value():
    assert mask_needle("偽ITEM12345", "OID") == "<OID len=10>"
    assert mask_needle("偽長い標籤", "LABEL") == "<LABEL len=5>"


def test_main_masks_leak_values_by_default(tmp_path, capsys):
    """N-系列复审第 3 轮红线: 闸自己的默认输出不能把真名 (哪怕是合成的 偽 值) 打进
    stdout —— CI 日志/issue/贴给 LLM 都是红线绕道进 git 的路径。"""
    cat = _write_catalog(tmp_path, forms=["偽SENSITIVE1"])
    target = tmp_path / "leaky.md"
    target.write_text("包含 偽SENSITIVE1 在正文里", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat)])   # 不带 --show-values
    out = capsys.readouterr().out
    assert rc == 1
    assert "偽SENSITIVE1" not in out
    assert "<OID len=11>" in out


def test_main_masks_label_leak_values_by_default(tmp_path, capsys):
    cat = _write_full_catalog(
        tmp_path,
        items=[{"item_oid": "偽ITM01", "label": "偽長い項目ラベル甲乙丙"}],
    )
    target = tmp_path / "label_leak.md"
    target.write_text("正文混进 偽長い項目ラベル甲乙丙 标签文本", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "偽長い項目ラベル甲乙丙" not in out
    assert "<LABEL len=11>" in out


def test_main_shows_real_values_with_show_values_flag(tmp_path, capsys):
    cat = _write_catalog(tmp_path, forms=["偽SENSITIVE1"])
    target = tmp_path / "leaky.md"
    target.write_text("包含 偽SENSITIVE1 在正文里", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat), "--show-values"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "偽SENSITIVE1" in out
    assert "<OID len=" not in out


def test_main_masks_allowlist_hit_values_by_default(tmp_path, monkeypatch, capsys):
    fake_rel = "scripts/tests/_fake_allowlisted.md"
    monkeypatch.setitem(ALLOWLIST, (fake_rel, "偽SENSITIVE1"), "测试用假条目")
    cat = _write_catalog(tmp_path, forms=["偽SENSITIVE1"])
    target_dir = tmp_path / "scripts" / "tests"
    target_dir.mkdir(parents=True)
    target = target_dir / "_fake_allowlisted.md"
    target.write_text("偽SENSITIVE1 出现在这里", encoding="utf-8")

    import scripts.oidscan_evidence as mod
    monkeypatch.setattr(mod, "GIT_ROOT", tmp_path)
    rc = main([str(target), "--catalog", str(cat)])   # 不带 --show-values
    out = capsys.readouterr().out
    assert rc == 0
    assert "allowlist 命中" in out
    assert "偽SENSITIVE1" not in out
    assert "<OID len=11>" in out


# ---- 复审第 4 轮 Item 3: target 存在但展开后 0 个文件也要 fail-closed ----

def test_main_fails_closed_on_empty_directory(tmp_path, capsys):
    cat = _write_catalog(tmp_path, forms=["偽FRM01"])
    empty_dir = tmp_path / "empty_target_dir"
    empty_dir.mkdir()
    rc = main([str(empty_dir), "--catalog", str(cat)])
    out = capsys.readouterr().out
    assert rc == 2
    assert "ABORT" in out
    assert "0 个文件" in out
    assert "CLEAN:" not in out


def test_main_fails_closed_on_directory_with_only_binary_files(tmp_path, capsys):
    cat = _write_catalog(tmp_path, forms=["偽FRM01"])
    d = tmp_path / "only_binary"
    d.mkdir()
    (d / "a.png").write_bytes(b"\x89PNG")
    rc = main([str(d), "--catalog", str(cat)])
    out = capsys.readouterr().out
    assert rc == 2
    assert "ABORT" in out


# ---- 复审第 4 轮 Item 2: 路径/文件名本身也要掩码 (不只是打印出的 needle) ----

def test_main_masks_needle_inside_filename_by_default(tmp_path, capsys):
    """study__form__item.md 文件名约定本身就是真名的载体 —— R3 只掩了打印出的
    needle 本身 (LEAK 行冒号后的那段), 没掩冒号前的 `{rel}:{lineno}:` 路径前缀;
    真实卡片正文的 frontmatter/H1 本就把 form_oid/item_oid 明文写进内容 (见
    render_field_card), 所以真实卡片会同时命中"内容里的 needle"与"文件名里的
    needle" —— 内容那份 R3 已经掩了, 文件名那份 (即路径前缀) 之前没掩, 复审第 4
    轮实测: 138/138 处泄漏行全部靠路径前缀漏出真名。这里合成同样的形状: 正文与
    文件名都含同一个 needle。"""
    cat = _write_catalog(tmp_path, forms=["偽SENSITIVE1"])
    target = tmp_path / "st01__偽SENSITIVE1__偽ITEM1.md"
    target.write_text("正文里也提到 偽SENSITIVE1", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat)])
    out = capsys.readouterr().out
    assert rc == 1
    assert "偽SENSITIVE1" not in out
    assert "<OID len=11>" in out


def test_main_masks_needle_in_missing_target_path(tmp_path, capsys):
    """ABORT 的缺失路径清单同样要掩码 (用户手滑打错真实卡片路径时不能把真名回显)。"""
    cat = _write_catalog(tmp_path, forms=["偽SENSITIVE1"])
    missing = tmp_path / "st01__偽SENSITIVE1__typo.md"
    rc = main([str(missing), "--catalog", str(cat)])
    out = capsys.readouterr().out
    assert rc == 2
    assert "偽SENSITIVE1" not in out
    assert "<OID len=11>" in out


def test_main_shows_real_path_with_show_values_flag(tmp_path, capsys):
    cat = _write_catalog(tmp_path, forms=["偽SENSITIVE1"])
    target = tmp_path / "st01__偽SENSITIVE1__偽ITEM1.md"
    target.write_text("正文里也提到 偽SENSITIVE1", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat), "--show-values"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "偽SENSITIVE1" in out
