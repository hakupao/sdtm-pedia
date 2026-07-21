#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
yml_to_glossary.py — term_mapping.yml v0.3 → 99_用語集.yml 変換ヘルパ

使用方法:
  python3 docs/jp/scripts/yml_to_glossary.py

入力:  docs/jp/glossary/term_mapping.yml
出力:  docs/jp/sources/99_用語集.yml

変換ルール:
  - entries[] × {internal, adopted, candidates, reason, reference}
    → シート 1_用語対照表 (internal / adopted / placeholder 中文 / reference[0])
    → シート 2_採用根拠   (internal / adopted / reason 要約 ≤200 字)
    → シート 3_候補参考   (internal / candidates 結合 / 不採用理由要約)
  - 中文訳は Phase 3 充填前提で "(中文訳要追加)" を placeholder とする.
    ただし SDTM / CDISC のように英語が固有名詞として通用するものは英語そのままを入れる.
  - Tier 1/2/3 の adopted="公開不要 (内部分類)" エントリは用語対照表に掲載するが,
    日本語訳列・中文訳列はともに「(納品物不使用)」と明示する.
  - 各コンテンツシートの先頭 1 行目に使用禁止語に関する注意書きを挿入する.
  - 採用根拠・候補参考シートの説明文中に blacklist 語を引用する場合は
    鉤括弧「」で囲み (使用禁止語) と付記して blacklist 監査を通す.
"""

import os
import re
import yaml

# パス解決
_HERE = os.path.dirname(os.path.abspath(__file__))
_JP_ROOT = os.path.normpath(os.path.join(_HERE, ".."))
_TERM_MAPPING = os.path.join(_JP_ROOT, "glossary", "term_mapping.yml")
_OUTPUT_YML   = os.path.join(_JP_ROOT, "sources", "99_用語集.yml")

# 注意書き (各シート先頭行に挿入)
_NOTICE_TABLE = (
    "※ 本表内に列挙される英語の内部用語は受信者への納品物では使用しない. "
    "日本語訳側 (「採用訳」列) を納品物で採用する."
)
_NOTICE_RATIONALE = (
    "※ 本表の「採用根拠」列は内部用語の選定理由を説明する目的で作成した. "
    "鉤括弧「」内に引用されている語は使用禁止語 (内部専用) であり, "
    "納品物本文では一切使用しない."
)
_NOTICE_CANDIDATES = (
    "※ 本表の「採用候補」「不採用理由」列は内部用語の候補選定根拠を説明する目的で作成した. "
    "鉤括弧「」内に引用されている語は使用禁止語 (内部専用) であり, "
    "納品物本文では一切使用しない."
)

# 中文訳が自明な固有名詞 (英語表記そのまま維持)
_OBVIOUS_ZH = {
    "SDTM", "CDISC", "GAMP", "GCP", "ICH", "IPA", "JIS", "PMDA",
}


def _load_blacklist_terms(blacklist_path: str) -> list:
    """term_blacklist.yml から全禁止語を読み込む."""
    with open(blacklist_path, encoding="utf-8") as f:
        bl_data = yaml.safe_load(f)
    terms = []
    for cat in bl_data["categories"].values():
        for item in cat:
            terms.append(item["term"])
    return terms


def _wrap_blacklist_terms(text: str, blacklist_terms: list) -> str:
    """
    テキスト内の blacklist 語を 「語」(使用禁止語) 形式に置換する.
    英語列 (英語内部用語そのものを掲載する列) ではなく,
    説明文テキスト中に混入する blacklist 語を鉤括弧引用に変換する.

    処理手順:
      1. 既に 「term」(使用禁止語) 形式でラップ済みの箇所は再処理しない.
      2. 未ラップの term を 「term」(使用禁止語) に置換する.
         ハイフン結合語 (例: Cross-batch) も対象とするため, 境界は
         \w (ASCII 英数字 + _) のみでなく CJK / ひらがな / カタカナも除外する.
    """
    # 長い語から順に処理して部分一致衝突を防ぐ
    sorted_terms = sorted(blacklist_terms, key=len, reverse=True)
    for term in sorted_terms:
        full_wrapped = f"「{term}」(使用禁止語)"
        # 既に完全ラップ済みの箇所をプレースホルダに退避して二重処理防止
        placeholder = f"\x00BL{hash(term) & 0xFFFF:04X}\x00"
        text_held = text.replace(full_wrapped, placeholder)
        # 残存する未ラップの term を置換 (case-insensitive; 元の表記を wrapper 内に保持)
        pattern = r'(?<![ぁ-ん一-龥ァ-ン\w])(' + re.escape(term) + r')(?![ぁ-ん一-龥ァ-ン\w])'
        text_held = re.sub(
            pattern,
            lambda m: f"「{m.group(1)}」(使用禁止語)",
            text_held,
            flags=re.IGNORECASE,
        )
        # プレースホルダを元に戻す
        text = text_held.replace(placeholder, full_wrapped)
    return text


def _truncate(text: str, max_len: int = 200) -> str:
    """テキストを max_len 文字以内に収める. 改行は空白に変換."""
    text = text.replace("\n", " ").replace("  ", " ").strip()
    if len(text) <= max_len:
        return text
    return text[:max_len - 1] + "…"


def _zh_placeholder(internal: str, adopted: str) -> str:
    """中文訳 placeholder を決定する."""
    # 納品物不使用の内部分類はそのまま明示
    if adopted == "公開不要 (内部分類)":
        return "(納品物不使用)"
    # 固有名詞や英略語はそのまま
    if internal.upper() in _OBVIOUS_ZH:
        return internal
    return "(中文訳要追加)"


def _candidates_str(candidates: list) -> str:
    """候補リストを「/ 」区切りの文字列に変換する."""
    return " / ".join(str(c) for c in candidates)


def _rejection_reason(entry: dict, blacklist_terms: list) -> str:
    """
    不採用理由の要約を生成する.
    reason フィールドから採用根拠を抽出し, 候補側の不採用理由を補足する.
    blacklist 語引用時は鉤括弧で囲み (使用禁止語) と付記する.
    """
    reason_raw = entry.get("reason", "").replace("\n", " ").strip()
    adopted = entry.get("adopted", "")
    candidates = entry.get("candidates", [])
    # 不採用候補 (adopted 以外)
    rejected = [c for c in candidates if c != adopted and c != "文脈依存"]
    if not rejected:
        return _truncate(f"採用語: 「{adopted}」. 詳細は採用根拠シート参照.", 200)
    rej_str = "・".join(f"「{r}」" for r in rejected)
    reason_short = _truncate(reason_raw, 120)
    combined = f"不採用候補: {rej_str}. 根拠: {reason_short}"
    combined = _wrap_blacklist_terms(combined, blacklist_terms)
    return _truncate(combined, 200)


def build_glossary_yml(mapping_path: str, output_path: str) -> None:
    _BLACKLIST_PATH = os.path.join(_JP_ROOT, "glossary", "term_blacklist.yml")
    blacklist_terms = _load_blacklist_terms(_BLACKLIST_PATH)

    with open(mapping_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    entries = data.get("entries", [])
    assert len(entries) == 33, f"entries 数が 33 でない: {len(entries)}"

    # ── シート 1: 用語対照表 ──────────────────────────────────────────────────
    rows_table = [
        [
            "【注意書き】",
            _NOTICE_TABLE,
            "",
            "",
        ]
    ]
    for e in entries:
        internal = e["internal"]
        adopted  = e["adopted"]
        # 「公開不要 (内部分類)」は日本語訳列に明示
        adopted_display = adopted if adopted != "公開不要 (内部分類)" else "(納品物不使用)"
        zh = _zh_placeholder(internal, adopted)
        ref = e.get("reference", [""])[0] if e.get("reference") else ""
        rows_table.append([internal, adopted_display, zh, ref])

    # ── シート 2: 採用根拠 ──────────────────────────────────────────────────
    rows_rationale = [
        [
            "【注意書き】",
            _NOTICE_RATIONALE,
            "",
        ]
    ]
    for e in entries:
        internal = e["internal"]
        adopted  = e["adopted"]
        # reason 中の blacklist 語を鉤括弧引用に変換 (説明目的での引用)
        reason_raw = _truncate(e.get("reason", ""), 200)
        reason_wrapped = _wrap_blacklist_terms(reason_raw, blacklist_terms)
        rows_rationale.append([internal, adopted, reason_wrapped])

    # ── シート 3: 候補参考 ──────────────────────────────────────────────────
    rows_candidates = [
        [
            "【注意書き】",
            _NOTICE_CANDIDATES,
            "",
        ]
    ]
    for e in entries:
        internal   = e["internal"]
        cands_str  = _candidates_str(e.get("candidates", []))
        rej_reason = _rejection_reason(e, blacklist_terms)
        rows_candidates.append([internal, cands_str, rej_reason])

    # ── yml 組み立て ──────────────────────────────────────────────────────────
    doc = {
        "document": {
            "name":      "用語集",
            "number":    "ITMS-SDTM-99-GLOSSARY-v0.1",
            "recipient": "iTMS 株式会社 御中",
            "author":    "担当部門",
            "created":   "2026-04-29",
            "updated":   "2026-04-29",
            "version":   "v0.1",
            "output":    "docs/jp/99_用語集.xlsx",
        },
        "revisions": [
            {
                "version":   "v0.1",
                "date":      "2026-04-29",
                "content":   "初版骨格作成 (33 entries)",
                "author":    "担当部門",
                "confirmer": "",
                "approver":  "",
            }
        ],
        "sheets": [
            {
                "name":            "1_用語対照表",
                "type":            "table",
                "content_summary": "英語内部用語 ⇆ 日本語採用訳 ⇆ 中文訳 ⇆ 出典規格 (33 entries)",
                "headers":         ["英 (内部用語)", "日 (採用訳)", "中 (中文訳)", "出典規格"],
                "rows":            rows_table,
            },
            {
                "name":            "2_採用根拠",
                "type":            "table",
                "content_summary": "各用語の採用根拠 (reason 要約 ≤200 字)",
                "headers":         ["英", "日", "採用根拠"],
                "rows":            rows_rationale,
            },
            {
                "name":            "3_候補参考",
                "type":            "table",
                "content_summary": "採用候補一覧と不採用理由",
                "headers":         ["英", "採用候補 (3 種)", "不採用理由"],
                "rows":            rows_candidates,
            },
        ],
        "approval": {
            "enabled": True,
        },
    }

    # YAML 出力 (allow_unicode=True で日本語そのまま, default_flow_style=False で読みやすく)
    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(
            doc,
            f,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
            width=120,
        )

    print(f"生成完了: {output_path}")
    print(f"  シート数 (本文): 3")
    print(f"  用語対照表 行数: {len(rows_table)} (注意書き 1 行 + entries 33 行)")
    print(f"  採用根拠  行数: {len(rows_rationale)}")
    print(f"  候補参考  行数: {len(rows_candidates)}")


if __name__ == "__main__":
    build_glossary_yml(_TERM_MAPPING, _OUTPUT_YML)
