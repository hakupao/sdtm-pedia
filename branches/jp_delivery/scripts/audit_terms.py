#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_terms.py — 納品物 (.xlsx) 用語規律監査スクリプト (PLAN §11.4)

使用方法:
  # blacklist 単独
  python3 docs/jp/scripts/audit_terms.py <xlsx> --blacklist docs/jp/glossary/term_blacklist.yml

  # mapping consistency 単独
  python3 docs/jp/scripts/audit_terms.py <xlsx> --mapping docs/jp/glossary/term_mapping.yml --check-consistency

  # 両方一括
  python3 docs/jp/scripts/audit_terms.py <xlsx> --blacklist <bl.yml> --mapping <m.yml> --check-consistency

追加フラグ:
  --human    人間可読サマリを stderr に追加出力
  --output   JSON 出力先ファイルパス (省略時: stdout)

依存: openpyxl, PyYAML, 標準 re / json / argparse / sys / os / datetime
"""

import argparse
import fnmatch
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path, PurePath
from typing import Optional

import yaml

# extract_xlsx_text の extract_cells を import (重複実装禁止)
sys.path.insert(0, os.path.dirname(__file__))
from extract_xlsx_text import extract_cells


# ─────────────────────────────────────────────────────────────────────────────
# exempt_files ヘルパ
# ─────────────────────────────────────────────────────────────────────────────

def _resolve_repo_root(blacklist_yml_path: str) -> Path:
    """
    blacklist yml パスから リポジトリルートを動的に判定する.

    戦略: blacklist yml は docs/jp/glossary/ に存在するため
    親 4 階層 (glossary → jp → docs → repo_root) を遡る.
    親が存在しない場合は yml の親ディレクトリを返す (フォールバック).
    """
    yml_abs = Path(blacklist_yml_path).resolve()
    # docs/jp/glossary/term_blacklist.yml → 親 4 = repo root
    try:
        repo_root = yml_abs.parents[3]
        if repo_root.is_dir():
            return repo_root
    except IndexError:
        pass
    return yml_abs.parent


def _to_relative_path(xlsx_path: str, repo_root: Path) -> str:
    """
    xlsx_path を repo_root 起点の相対パス文字列に正規化する.
    絶対パス / 相対パスいずれの入力にも対応する.
    """
    try:
        return str(Path(xlsx_path).resolve().relative_to(repo_root))
    except ValueError:
        # repo_root 外にある場合はそのまま返す
        return str(Path(xlsx_path).resolve())


def check_exempt(
    xlsx_path: str,
    exempt_patterns: list,
    repo_root: Path,
) -> dict:
    """
    xlsx_path が exempt_files glob リストにマッチするか判定する.

    glob 照合:
      1. fnmatch.fnmatch() でファイル名のみ照合 (PLAN.md / CHANGELOG.md 等)
      2. PurePath.match() でパスパターン照合 (glossary/** / failures/** 等)

    Parameters
    ----------
    xlsx_path : str
        監査対象 xlsx のパス.
    exempt_patterns : list of str
        blacklist yml の audit_rules.exempt_files リスト.
    repo_root : Path
        リポジトリルートの絶対パス.

    Returns
    -------
    dict
        {"matched": bool, "matched_pattern": str|None, "input_relative_path": str}
    """
    rel_path = _to_relative_path(xlsx_path, repo_root)
    filename = Path(xlsx_path).name

    for pattern in exempt_patterns:
        # 1) PurePath.match() — "glossary/**" や "docs/**" 等のパスパターン
        if PurePath(rel_path).match(pattern):
            return {
                "matched": True,
                "matched_pattern": pattern,
                "input_relative_path": rel_path,
            }
        # 2) fnmatch — ファイル名のみの単純パターン ("PLAN.md", "*.md" 等)
        if fnmatch.fnmatch(filename, pattern):
            return {
                "matched": True,
                "matched_pattern": pattern,
                "input_relative_path": rel_path,
            }

    return {
        "matched": False,
        "matched_pattern": None,
        "input_relative_path": rel_path,
    }


# ─────────────────────────────────────────────────────────────────────────────
# YML ローダ
# ─────────────────────────────────────────────────────────────────────────────

def load_blacklist(yml_path: str) -> dict:
    """
    term_blacklist.yml を読み込み、監査に必要な構造を返す.

    Parameters
    ----------
    yml_path : str
        term_blacklist.yml のパス.

    Returns
    -------
    dict
        {
          "audit_rules": { "case_sensitive": bool, "match_whole_word": bool },
          "categories": {
              "<category_name>": [{"term": str, ...}, ...]
          }
        }

    Raises
    ------
    SystemExit(2)
        ファイル不在 / YAML 構文エラー / 必須キー欠落の場合.
    """
    if not os.path.isfile(yml_path):
        print(f"[エラー] blacklist yml が見つからない: {yml_path}", file=sys.stderr)
        sys.exit(2)

    try:
        with open(yml_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"[エラー] blacklist yml YAML 構文エラー: {e}", file=sys.stderr)
        sys.exit(2)

    if not isinstance(data, dict):
        print("[エラー] blacklist yml のトップレベルは dict でなければならない.", file=sys.stderr)
        sys.exit(2)
    if "categories" not in data or not isinstance(data["categories"], dict):
        print("[エラー] blacklist yml に 'categories' (dict) が必須.", file=sys.stderr)
        sys.exit(2)
    if "audit_rules" not in data or not isinstance(data["audit_rules"], dict):
        print("[エラー] blacklist yml に 'audit_rules' (dict) が必須.", file=sys.stderr)
        sys.exit(2)

    return data


def load_mapping(yml_path: str) -> list:
    """
    term_mapping.yml を読み込み、entries リストを返す.

    Parameters
    ----------
    yml_path : str
        term_mapping.yml のパス.

    Returns
    -------
    list of dict
        各エントリは {"internal": str, "adopted": str, "candidates": list} を持つ.

    Raises
    ------
    SystemExit(2)
        ファイル不在 / YAML 構文エラー / 必須キー欠落の場合.
    """
    if not os.path.isfile(yml_path):
        print(f"[エラー] mapping yml が見つからない: {yml_path}", file=sys.stderr)
        sys.exit(2)

    try:
        with open(yml_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"[エラー] mapping yml YAML 構文エラー: {e}", file=sys.stderr)
        sys.exit(2)

    if not isinstance(data, dict):
        print("[エラー] mapping yml のトップレベルは dict でなければならない.", file=sys.stderr)
        sys.exit(2)
    if "entries" not in data or not isinstance(data["entries"], list):
        print("[エラー] mapping yml に 'entries' (list) が必須.", file=sys.stderr)
        sys.exit(2)

    return data["entries"]


# ─────────────────────────────────────────────────────────────────────────────
# 検査ロジック
# ─────────────────────────────────────────────────────────────────────────────

def _is_ascii_only(term: str) -> bool:
    """term が半角 ASCII 文字 (英数字 + 記号) のみで構成されているか判定する."""
    try:
        term.encode("ascii")
        return True
    except UnicodeEncodeError:
        return False


def _build_pattern(term: str, case_sensitive: bool, match_whole_word: bool):
    """
    term に対応する re パターンを構築する.

    match_whole_word の解釈:
      - ASCII のみの term: \\b (単語境界) で囲む
      - 日本語 / 非 ASCII 文字を 1 文字でも含む term: 部分一致 (re.escape のみ)

    1 文字の term は false positive リスクがあるため警告を stderr に出力する.
    """
    if len(term) == 1:
        print(
            f"[警告] term が 1 文字のため false positive の可能性あり: '{term}'",
            file=sys.stderr,
        )

    escaped = re.escape(term)
    flags = 0 if case_sensitive else re.IGNORECASE

    if match_whole_word and _is_ascii_only(term):
        pattern = re.compile(r"\b" + escaped + r"\b", flags)
    else:
        pattern = re.compile(escaped, flags)

    return pattern


def scan_blacklist(cells: list, blacklist_data: dict) -> list:
    """
    セルリストに対して blacklist 全カテゴリの全 term を検査し、ヒット一覧を返す.

    Parameters
    ----------
    cells : list of dict
        extract_cells() が返す辞書のリスト.
    blacklist_data : dict
        load_blacklist() が返す辞書.

    Returns
    -------
    list of dict
        各ヒットは以下のキーを持つ:
          term, category, sheet, row, col, coord, value_excerpt
    """
    audit_rules = blacklist_data["audit_rules"]
    case_sensitive = audit_rules.get("case_sensitive", False)
    match_whole_word = audit_rules.get("match_whole_word", True)

    # カテゴリ × term → パターン を事前コンパイル
    compiled = []
    for cat_name, terms in blacklist_data["categories"].items():
        if not isinstance(terms, list):
            continue
        for item in terms:
            term = item.get("term", "")
            if not term:
                continue
            pat = _build_pattern(term, case_sensitive, match_whole_word)
            compiled.append((cat_name, term, pat))

    hits = []
    for cell in cells:
        value = cell["value"]
        for cat_name, term, pat in compiled:
            if pat.search(value):
                # value_excerpt: 前後 30 文字以内に収める
                excerpt = value if len(value) <= 80 else value[:77] + "..."
                hits.append({
                    "term":          term,
                    "category":      cat_name,
                    "sheet":         cell["sheet"],
                    "row":           cell["row"],
                    "col":           cell["col"],
                    "coord":         cell["coord"],
                    "value_excerpt": excerpt,
                })

    return hits


def scan_mapping(cells: list, entries: list) -> list:
    """
    セルリストに対して mapping consistency を検査し、不整合一覧を返す.

    仕様:
      各 entry の candidates のうち adopted 以外の語 (未採用候補) が
      xlsx 内に出現した場合を inconsistency として記録する.
      adopted 語自体は一貫使用とみなしヒットしない.
      「文脈依存」「公開不要 (内部分類)」は adopted として扱い、
      candidates 中の全語が未採用候補扱いになる (文脈依存の場合は全候補が hit 対象).

    Parameters
    ----------
    cells : list of dict
        extract_cells() が返す辞書のリスト.
    entries : list of dict
        load_mapping() が返すエントリリスト.

    Returns
    -------
    list of dict
        各不整合は以下のキーを持つ:
          internal, adopted, found_alt, occurrences, first_location {sheet, coord}
    """
    inconsistencies = []

    for entry in entries:
        internal = entry.get("internal", "")
        adopted = entry.get("adopted", "")
        candidates = entry.get("candidates", [])

        # 未採用候補 = candidates から adopted を除いたもの
        # 「文脈依存」は特殊 adopted: candidates 全語が未採用候補
        if adopted in ("文脈依存", "公開不要 (内部分類)"):
            unadopted = list(candidates)
        else:
            unadopted = [c for c in candidates if c != adopted]

        for alt in unadopted:
            if not alt:
                continue
            # 非 ASCII を含む語は部分一致、ASCII のみは単語境界
            if _is_ascii_only(alt):
                pat = re.compile(r"\b" + re.escape(alt) + r"\b", re.IGNORECASE)
            else:
                pat = re.compile(re.escape(alt))

            count = 0
            first_loc = None
            for cell in cells:
                if pat.search(cell["value"]):
                    count += 1
                    if first_loc is None:
                        first_loc = {
                            "sheet": cell["sheet"],
                            "coord": cell["coord"],
                        }

            if count > 0:
                inconsistencies.append({
                    "internal":      internal,
                    "adopted":       adopted,
                    "found_alt":     alt,
                    "occurrences":   count,
                    "first_location": first_loc,
                })

    return inconsistencies


# ─────────────────────────────────────────────────────────────────────────────
# 出力フォーマッタ
# ─────────────────────────────────────────────────────────────────────────────

def format_output(
    xlsx_path: str,
    blacklist_result: Optional[dict],
    mapping_result: Optional[dict],
    exempt_info: Optional[dict] = None,
) -> dict:
    """
    監査結果を JSON 出力用辞書に整形する.

    Parameters
    ----------
    xlsx_path : str
        監査対象 xlsx のパス.
    blacklist_result : dict or None
        blacklist 検査結果. None の場合は checked=False.
    mapping_result : dict or None
        mapping 検査結果. None の場合は checked=False.
    exempt_info : dict or None
        check_exempt() が返す辞書. None の場合は {"matched": False, ...} 相当.

    Returns
    -------
    dict
        仕様に定める JSON 出力構造.
    """
    bl_hit_count = 0
    map_incon_count = 0

    # ── blacklist セクション ──────────────────────────────────────────────────
    if blacklist_result is None:
        bl_section = {"checked": False}
    else:
        hits = blacklist_result["hits"]
        bl_hit_count = len(hits)
        bl_section = {
            "checked":          True,
            "yml_path":         blacklist_result["yml_path"],
            "categories_loaded": blacklist_result["categories_loaded"],
            "terms_loaded":      blacklist_result["terms_loaded"],
            "hits":              hits,
            "hit_count":         bl_hit_count,
        }

    # ── mapping セクション ────────────────────────────────────────────────────
    if mapping_result is None:
        map_section = {"checked": False}
    else:
        inconsistencies = mapping_result["inconsistencies"]
        map_incon_count = len(inconsistencies)
        map_section = {
            "checked":              True,
            "yml_path":             mapping_result["yml_path"],
            "entries_loaded":        mapping_result["entries_loaded"],
            "inconsistencies":       inconsistencies,
            "inconsistency_count":   map_incon_count,
        }

    # ── exempt / verdict ──────────────────────────────────────────────────────
    if exempt_info is None:
        exempt_info = {"matched": False, "matched_pattern": None, "input_relative_path": str(xlsx_path)}

    if exempt_info["matched"]:
        verdict = "INFORMATIONAL"
    else:
        verdict = "PASS" if (bl_hit_count == 0 and map_incon_count == 0) else "FAIL"

    return {
        "xlsx":       os.path.abspath(xlsx_path),
        "scanned_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "exempt":     exempt_info,
        "blacklist":  bl_section,
        "mapping":    map_section,
        "summary": {
            "blacklist_hit_count":         bl_hit_count,
            "mapping_inconsistency_count": map_incon_count,
            "verdict":                     verdict,
        },
    }


def _print_human_summary(result: dict) -> None:
    """人間可読サマリを stderr に出力する."""
    summary = result["summary"]
    verdict = summary["verdict"]
    sep = "=" * 60

    print(sep, file=sys.stderr)
    print(f"用語監査サマリ — {result['xlsx']}", file=sys.stderr)
    print(f"検査日時: {result['scanned_at']}", file=sys.stderr)

    # exempt 表示
    ex = result.get("exempt", {})
    if ex.get("matched"):
        print(
            f"[exempt]     INFORMATIONAL (パターン: '{ex['matched_pattern']}',"
            f" 相対パス: '{ex['input_relative_path']}')",
            file=sys.stderr,
        )

    print(sep, file=sys.stderr)

    bl = result["blacklist"]
    if bl.get("checked"):
        print(
            f"[blacklist]  ヒット数: {bl['hit_count']}  "
            f"(カテゴリ: {bl['categories_loaded']}, 語数: {bl['terms_loaded']})",
            file=sys.stderr,
        )
        for h in bl["hits"][:5]:
            print(
                f"  HIT: '{h['term']}' @ {h['sheet']}!{h['coord']}"
                f"  [{h['value_excerpt'][:40]}...]",
                file=sys.stderr,
            )
        if bl["hit_count"] > 5:
            print(f"  ... 他 {bl['hit_count'] - 5} 件", file=sys.stderr)
    else:
        print("[blacklist]  未実行", file=sys.stderr)

    mp = result["mapping"]
    if mp.get("checked"):
        print(
            f"[mapping]    不整合数: {mp['inconsistency_count']}  "
            f"(エントリ: {mp['entries_loaded']})",
            file=sys.stderr,
        )
        for inc in mp["inconsistencies"][:5]:
            loc = inc["first_location"] or {}
            print(
                f"  INCONSISTENCY: '{inc['found_alt']}' (採用語: '{inc['adopted']}')"
                f"  @ {loc.get('sheet', '?')}!{loc.get('coord', '?')}"
                f"  ({inc['occurrences']} 箇所)",
                file=sys.stderr,
            )
        if mp["inconsistency_count"] > 5:
            print(f"  ... 他 {mp['inconsistency_count'] - 5} 件", file=sys.stderr)
    else:
        print("[mapping]    未実行", file=sys.stderr)

    print(sep, file=sys.stderr)
    print(f"verdict: {verdict}", file=sys.stderr)
    print(sep, file=sys.stderr)


# ─────────────────────────────────────────────────────────────────────────────
# CLI エントリポイント
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    """
    CLI エントリポイント.

    終了コード:
        0 : PASS (blacklist hit = 0 かつ mapping inconsistency = 0)
        1 : FAIL (blacklist hit > 0 または mapping inconsistency > 0)
        2 : 引数エラー / ファイル不在 / yml schema 不正
    """
    parser = argparse.ArgumentParser(
        description="納品物 .xlsx の用語規律を監査する (PLAN §11.4).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("xlsx", help="監査対象 .xlsx ファイルのパス")
    parser.add_argument(
        "--blacklist",
        metavar="PATH",
        default=None,
        help="term_blacklist.yml のパス",
    )
    parser.add_argument(
        "--mapping",
        metavar="PATH",
        default=None,
        help="term_mapping.yml のパス",
    )
    parser.add_argument(
        "--check-consistency",
        action="store_true",
        help="mapping consistency 検査を実行する (--mapping 必須)",
    )
    parser.add_argument(
        "--human",
        action="store_true",
        help="人間可読サマリを stderr に追加出力する",
    )
    parser.add_argument(
        "--output",
        metavar="PATH",
        default=None,
        help="JSON 出力先ファイルパス (省略時: stdout)",
    )
    args = parser.parse_args()

    # 引数検証
    if args.blacklist is None and not args.check_consistency:
        print(
            "[エラー] --blacklist または --mapping --check-consistency のいずれかが必要.",
            file=sys.stderr,
        )
        sys.exit(2)
    if args.check_consistency and args.mapping is None:
        print("[エラー] --check-consistency には --mapping が必要.", file=sys.stderr)
        sys.exit(2)

    # xlsx 存在チェック
    if not os.path.isfile(args.xlsx):
        print(f"[エラー] xlsx ファイルが見つからない: {args.xlsx}", file=sys.stderr)
        sys.exit(2)

    # セル抽出 (一度だけ読み込んでリスト化)
    cells = list(extract_cells(args.xlsx))

    # ── exempt 判定 ───────────────────────────────────────────────────────────
    exempt_info = None
    if args.blacklist:
        bl_data = load_blacklist(args.blacklist)
        exempt_patterns = bl_data.get("audit_rules", {}).get("exempt_files", [])
        if exempt_patterns:
            repo_root = _resolve_repo_root(args.blacklist)
            exempt_info = check_exempt(args.xlsx, exempt_patterns, repo_root)
        else:
            exempt_info = {
                "matched": False,
                "matched_pattern": None,
                "input_relative_path": _to_relative_path(
                    args.xlsx,
                    Path(args.blacklist).resolve().parent,
                ),
            }
    else:
        # blacklist なし: exempt 判定不可
        exempt_info = {
            "matched": False,
            "matched_pattern": None,
            "input_relative_path": str(args.xlsx),
        }

    # ── blacklist 検査 ────────────────────────────────────────────────────────
    blacklist_result = None
    if args.blacklist:
        # bl_data はすでに上でロード済み
        hits = scan_blacklist(cells, bl_data)

        # terms_loaded カウント
        terms_loaded = sum(
            len(items)
            for items in bl_data["categories"].values()
            if isinstance(items, list)
        )
        blacklist_result = {
            "yml_path":          os.path.abspath(args.blacklist),
            "categories_loaded": len(bl_data["categories"]),
            "terms_loaded":      terms_loaded,
            "hits":              hits,
        }

    # ── mapping 検査 ──────────────────────────────────────────────────────────
    mapping_result = None
    if args.check_consistency and args.mapping:
        entries = load_mapping(args.mapping)
        inconsistencies = scan_mapping(cells, entries)
        mapping_result = {
            "yml_path":      os.path.abspath(args.mapping),
            "entries_loaded": len(entries),
            "inconsistencies": inconsistencies,
        }

    # ── 出力整形 ──────────────────────────────────────────────────────────────
    result = format_output(args.xlsx, blacklist_result, mapping_result, exempt_info)

    if args.human:
        _print_human_summary(result)

    json_str = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(json_str + "\n")
    else:
        print(json_str)

    # 終了コード: INFORMATIONAL / PASS → 0, FAIL → 1
    verdict = result["summary"]["verdict"]
    sys.exit(0 if verdict in ("PASS", "INFORMATIONAL") else 1)


if __name__ == "__main__":
    main()
