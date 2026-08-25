import json

import pytest

from scripts.oidscan_evidence import (
    ALLOWLIST,
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
    cat = _write_catalog(tmp_path, forms=["偽F1", "12"], items=["偽I1", "34"])
    needles = load_needles(cat)
    assert needles == {"偽F1", "偽I1"}


def test_load_needles_excludes_given_set(tmp_path):
    cat = _write_catalog(tmp_path, forms=["偽F1", "AE"])
    needles = load_needles(cat, exclude={"AE"})
    assert needles == {"偽F1"}


def test_load_needles_unions_four_pools(tmp_path):
    cat = _write_catalog(tmp_path, forms=["偽F1"], items=["偽I1"],
                         events=["偽E1"], activities=["偽A1"])
    assert load_needles(cat) == {"偽F1", "偽I1", "偽E1", "偽A1"}


# ---- N3: label/name 池 (spec §8 第 2 条 "OID / label" 并列, 只扫 OID 不算闭合) ----

def test_load_label_needles_collects_all_named_fields(tmp_path):
    cat = _write_full_catalog(
        tmp_path,
        forms=[{"oid": "偽F1", "name": "偽表单名称甲", "description": "偽表单说明甲"}],
        items=[{"item_oid": "偽I1", "label": "偽项目标签甲", "group_name": "偽分组甲",
                "form_name": "偽表单名甲"}],
        events=[{"oid": "偽E1", "name": "偽事件名称甲"}],
        activities=[{"oid": "偽A1", "name": "偽活动名称甲", "event_name": "偽关联事件甲"}],
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
        items=[{"item_oid": "偽I1", "label": "偽", "group_name": "偽甲乙丙丁"}],
    )
    needles = load_label_needles(cat, min_len=4)
    assert needles == {"偽甲乙丙丁"}   # 4 字保留, 1 字 "偽" 被剔除


def test_load_label_needles_ignores_missing_and_empty_fields(tmp_path):
    cat = _write_full_catalog(
        tmp_path,
        forms=[{"oid": "偽F1"}],                 # 无 name/description 键
        items=[{"item_oid": "偽I1", "label": ""}],  # 空字符串
    )
    assert load_label_needles(cat) == set()


def test_load_label_needles_excludes_given_set(tmp_path):
    cat = _write_full_catalog(
        tmp_path,
        forms=[{"oid": "偽F1", "name": "公開語彙甲甲"}],
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
    cat = _write_catalog(tmp_path, forms=["偽F1"])
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
    cat = _write_catalog(tmp_path, forms=["偽F1"])
    target = tmp_path / "clean.md"
    target.write_text("nothing sensitive here", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat)])
    assert rc == 0
    assert "CLEAN" in capsys.readouterr().out


def test_main_leak_when_hit_not_allowlisted(tmp_path, capsys):
    cat = _write_catalog(tmp_path, forms=["偽F1"])
    target = tmp_path / "leaky.md"
    target.write_text("包含 偽F1 在正文里", encoding="utf-8")
    # --show-values: 本测试要断言具体命中了哪个 needle, 数据是合成 偽 前缀值, 打真值无害。
    rc = main([str(target), "--catalog", str(cat), "--show-values"])
    out = capsys.readouterr().out
    assert rc == 1
    assert "LEAK" in out
    assert "偽F1" in out


def test_main_catches_label_leak_not_just_oid(tmp_path, capsys):
    """N3 回归钉: 只含真实 label (不含任何真实 OID) 的文件也必须被抓到。"""
    cat = _write_full_catalog(
        tmp_path,
        items=[{"item_oid": "偽I1", "label": "偽長い項目ラベル甲乙丙"}],
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
    monkeypatch.setitem(ALLOWLIST, (fake_rel, "偽F1"), "测试用假条目")
    cat = _write_catalog(tmp_path, forms=["偽F1"])
    target_dir = tmp_path / "scripts" / "tests"
    target_dir.mkdir(parents=True)
    target = target_dir / "_fake_allowlisted.md"
    target.write_text("偽F1 出现在这里", encoding="utf-8")

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
    collision_needle = next(iter(KNOWN_PUBLIC_COLLISIONS))
    cat = _write_catalog(tmp_path, forms=[collision_needle, "偽F1"])
    target = tmp_path / "doc.md"
    target.write_text(f"讨论 {collision_needle} 与 偽F1 都出现", encoding="utf-8")
    rc = main([str(target), "--catalog", str(cat), "--show-values"])
    out = capsys.readouterr().out
    assert rc == 1                       # 偽F1 仍应被抓到
    leak_section = out.split("LEAK:", 1)[1]
    assert "偽F1" in leak_section
    assert f"'{collision_needle}'" not in leak_section   # 公开词汇不算泄漏, 不进 LEAK 明细


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
        items=[{"item_oid": "偽I1", "label": "偽長い項目ラベル甲乙丙"}],
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
    cat = _write_catalog(tmp_path, forms=["偽F1"])
    empty_dir = tmp_path / "empty_target_dir"
    empty_dir.mkdir()
    rc = main([str(empty_dir), "--catalog", str(cat)])
    out = capsys.readouterr().out
    assert rc == 2
    assert "ABORT" in out
    assert "0 个文件" in out
    assert "CLEAN:" not in out


def test_main_fails_closed_on_directory_with_only_binary_files(tmp_path, capsys):
    cat = _write_catalog(tmp_path, forms=["偽F1"])
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
