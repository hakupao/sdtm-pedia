"""部署索引陈旧检测 (运维闸).

背景 (2026-08-04 实测): 部署中的向量库把 VARIABLE_INDEX.md 欠切 70% (65 vs 222 chunk),
陈旧至少跨越 chunker 的一次演进, 期间生产 RAG 一直用残缺索引回答, CDISC recall 白丢
5.7pt —— **全程无任何告警**。

既有的 `kb_commit_sha` 用 `git rev-parse HEAD` (整仓 HEAD), 任何一次代码提交都会让它变,
误报太多故从未被接上检查。本模块改用**内容指纹**: 只随 KB 文件内容变化, 且能捕获未提交
的本地修改 (git tree SHA 做不到)。
"""
from __future__ import annotations

import pytest

from scripts.kb_freshness import check_freshness, kb_fingerprint


def _kb(tmp_path, files: dict[str, str]):
    root = tmp_path / "kb"
    for rel, body in files.items():
        p = root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
    return root


# ---- 指纹本身 ----

def test_fingerprint_is_deterministic(tmp_path):
    root = _kb(tmp_path, {"a.md": "x", "d/b.md": "y"})
    assert kb_fingerprint(root) == kb_fingerprint(root)


def test_fingerprint_changes_on_content_edit(tmp_path):
    root = _kb(tmp_path, {"a.md": "x"})
    before = kb_fingerprint(root)
    (root / "a.md").write_text("x2", encoding="utf-8")
    assert kb_fingerprint(root) != before


def test_fingerprint_changes_on_file_added_or_removed(tmp_path):
    root = _kb(tmp_path, {"a.md": "x"})
    before = kb_fingerprint(root)
    (root / "b.md").write_text("y", encoding="utf-8")
    added = kb_fingerprint(root)
    assert added != before
    (root / "b.md").unlink()
    assert kb_fingerprint(root) == before      # 删回去应还原


def test_fingerprint_ignores_non_markdown(tmp_path):
    root = _kb(tmp_path, {"a.md": "x"})
    before = kb_fingerprint(root)
    (root / "note.txt").write_text("irrelevant", encoding="utf-8")
    assert kb_fingerprint(root) == before


def test_fingerprint_path_sensitive_not_just_content(tmp_path):
    """同内容不同路径必须产生不同指纹 (改名/移动也是 KB 变更)."""
    r1 = _kb(tmp_path / "one", {"a.md": "same"})
    r2 = _kb(tmp_path / "two", {"renamed.md": "same"})
    assert kb_fingerprint(r1) != kb_fingerprint(r2)


# ---- 闸本身 ----

def test_fresh_when_stamp_matches(tmp_path):
    root = _kb(tmp_path, {"a.md": "x"})
    stamp = tmp_path / "stamp.txt"
    stamp.write_text(f"kb_fingerprint={kb_fingerprint(root)}\n", encoding="utf-8")
    res = check_freshness(stamp, root)
    assert res.fresh is True


def test_stale_when_kb_edited_after_ingest(tmp_path):
    root = _kb(tmp_path, {"a.md": "x"})
    stamp = tmp_path / "stamp.txt"
    stamp.write_text(f"kb_fingerprint={kb_fingerprint(root)}\n", encoding="utf-8")
    (root / "a.md").write_text("edited", encoding="utf-8")
    res = check_freshness(stamp, root)
    assert res.fresh is False
    assert "reingest" in res.reason.lower() or "stale" in res.reason.lower()


def test_missing_stamp_is_stale_not_crash(tmp_path):
    """戳不存在 = 从未灌过 or 戳被删 → 按陈旧处理 (fail loud), 不得静默通过."""
    root = _kb(tmp_path, {"a.md": "x"})
    res = check_freshness(tmp_path / "absent.txt", root)
    assert res.fresh is False
    assert "stamp" in res.reason.lower()


def test_stamp_without_fingerprint_key_is_stale(tmp_path):
    """旧格式戳 (只有 kb_commit_sha) → 无法判定即按陈旧, 提示重灌一次以写入指纹."""
    root = _kb(tmp_path, {"a.md": "x"})
    stamp = tmp_path / "stamp.txt"
    stamp.write_text("kb_commit_sha=abc123\ntotal_chunks=10\n", encoding="utf-8")
    res = check_freshness(stamp, root)
    assert res.fresh is False
    assert "kb_fingerprint" in res.reason


def test_result_carries_both_fingerprints_for_diagnosis(tmp_path):
    root = _kb(tmp_path, {"a.md": "x"})
    stamp = tmp_path / "stamp.txt"
    stamp.write_text("kb_fingerprint=deadbeef\n", encoding="utf-8")
    res = check_freshness(stamp, root)
    assert res.stamped == "deadbeef"
    assert res.current == kb_fingerprint(root)


# ---- ingest 侧: 戳必须写入指纹 ----

def test_ingest_stamp_records_fingerprint(tmp_path, monkeypatch):
    from scripts import ingest as ing
    root = _kb(tmp_path, {"a.md": "x"})
    monkeypatch.setattr(ing, "KB_ROOT", root)
    chroma = tmp_path / "chroma"
    chroma.mkdir()
    stamp = ing.write_ingest_stamp(chroma, total_chunks=3, kb_sha="abc")
    body = stamp.read_text(encoding="utf-8")
    assert f"kb_fingerprint={kb_fingerprint(root)}" in body
    assert check_freshness(stamp, root).fresh is True


# ---- CLI: 部署前置检查 (deploy.sh 可用, 陈旧则非零退出) ----

def test_cli_exits_nonzero_when_stale(tmp_path, capsys):
    from scripts.check_index_freshness import main
    root = _kb(tmp_path, {"a.md": "x"})
    stamp = tmp_path / "stamp.txt"
    stamp.write_text("kb_fingerprint=deadbeef\n", encoding="utf-8")
    rc = main(["--kb-root", str(root), "--stamp", str(stamp)])
    assert rc == 1
    assert "stale" in capsys.readouterr().out.lower()


def test_cli_exits_zero_when_fresh(tmp_path, capsys):
    from scripts.check_index_freshness import main
    root = _kb(tmp_path, {"a.md": "x"})
    stamp = tmp_path / "stamp.txt"
    stamp.write_text(f"kb_fingerprint={kb_fingerprint(root)}\n", encoding="utf-8")
    assert main(["--kb-root", str(root), "--stamp", str(stamp)]) == 0
    assert "in sync" in capsys.readouterr().out.lower()


# ---- 服务侧: /api/info 必须暴露新鲜度 (陈旧要看得见, 不能只躺在日志里) ----

def test_info_response_exposes_freshness():
    from server.router import InfoResponse
    r = InfoResponse(
        collection_name="c", chunk_count=1, default_model="m", fallback_model="f",
        top_k=5, structured_lookup=True, hybrid=True, prompt_guardrail=True,
        index_fresh=False, index_freshness_reason="stale: kb changed",
    )
    assert r.index_fresh is False and "stale" in r.index_freshness_reason


def test_info_freshness_defaults_are_conservative():
    """未显式设置时不得默认为 fresh —— 默认值说谎比没有字段更糟."""
    from server.router import InfoResponse
    r = InfoResponse(
        collection_name="c", chunk_count=1, default_model="m", fallback_model="f",
        top_k=5, structured_lookup=True, hybrid=True, prompt_guardrail=True,
    )
    assert r.index_fresh is not True
