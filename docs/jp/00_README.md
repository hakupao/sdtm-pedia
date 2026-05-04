# docs/jp/ — iTMS 様 納品ドキュメント (Internal Index)

> **Notice**: 本 README は **内部利用用** (リポジトリ内ナビゲーション目的). 納品物には含めない (中間版以降は `00_納品範囲.xlsx` が受信者向け案内として別途同梱).

## 概要

iTMS 株式会社 様 向けに, SDTM 知識ベースプロジェクトを **日本職場の標準ドキュメント形式 (Excel 主体)** で再構成した一式.

源プロジェクト (`knowledge_base/` / `.work/` / `docs/`) は read-only. 本目录は純粋下流の **翻訳 + 形式整備 + 再パッケージ** branch.

## 主要文書

### 内部管理ファイル

| ファイル | 種別 | 状態 |
|---------|------|------|
| `PLAN.md` | 計画書 (WHAT/WHY) | DRAFT v0.3 |
| `EXECUTION_PLAN.md` | 実行計画書 (HOW + agent 调度) | DRAFT v0.2 |
| `_progress.json` | 進捗真源 (Tier 2 schema) | active |
| `CHANGELOG.md` | 改訂履歴一元管理 | active |
| `WORKLOG.md` | 日次作業ログ (日本語, iTMS 様可視) | active |
| `glossary/term_blacklist.yml` | 使用禁止語リスト | active |
| `glossary/term_mapping.yml` | 用語写像辞書 | v0.5 active |
| `glossary/reference_standards.md` | 参照規格一覧 | active |
| `templates/style_guide.xlsx` | 配色 / フォント テンプレ | Phase 0.7 PASS |
| `templates/cover_template.xlsx` | 表紙統一様式 | Phase 0.7 PASS |
| `scripts/build_xlsx.py` | yml → xlsx 生成 (schema 検証付き) | active |
| `scripts/audit_terms.py` | 用語規律監査 | active |

### 納品物 (.xlsx)

| ファイル | 優先度 | 着手順 | 状態 |
|---------|-------|--------|------|
| `04_要件定義書.xlsx` | **P0** | 1 | ✅ v1.0 PASS 2026-04-29 |
| `01_基本設計書.xlsx` | **P0** | 2 | ✅ v1.0 PASS 2026-04-29 |
| `02_運用保守マニュアル.xlsx` | **P0** | 3 | 未着手 |
| `03_テスト結果報告書.xlsx` | **P0** | 4 | 未着手 |
| `05_詳細設計書.xlsx` | P1 | 5 | 未着手 |
| `07_進捗報告書.xlsx` | P2 | 6 | v0.5 中間版 PASS 2026-04-30 (Phase 3 で v1.0 化予定) |
| `06_トレーサビリティ管理表.xlsx` | P2 | 7 | 未着手 |
| `99_用語集.xlsx` | 附属 | — | v0.1 骨格 (33 entries; 中文列 Phase 3 充填) |

### 中間版 v0.5 補助物 (受信者要望対応)

| ファイル | 用途 | 状態 |
|---------|------|------|
| `00_納品範囲.xlsx` | 中間版 zip 同梱物の案内 | v0.5 PASS 2026-04-30 |
| `08_反復実績記録.xlsx` | 全工程の検査・反復実績集約 | v0.5 PASS 2026-04-30 |

### 子目录

| ディレクトリ | 用途 |
|-------------|------|
| `sources/` | yml 形式の文書源 (build_xlsx.py 入力) |
| `templates/` | xlsx テンプレ + style_guide |
| `glossary/` | 用語辞書 + 参照規格 + research_reports/ |
| `scripts/` | xlsx 生成 + 用語監査スクリプト |
| `prompts/` | subagent 用提示テンプレ (writer / reviewer / term audit / research) |
| `failures/` | 失敗 attempt のアーカイブ (規則 B) |
| `assets/` | 図表素材 |
| `deliverable/` | 受信者向け zip パッケージ |

## ドキュメント関係図

```
[ PLAN.md (v0.3) ] ─── (WHAT/WHY) ───┐
                                      │
[ EXECUTION_PLAN.md (v0.2) ] ─ (HOW) ─┐
                                       │
                                ┌──────┴──────┐
                                ↓             ↓
                  [ 納品 7 文書 + 99 用語集 ]   [ glossary/ + templates/ ]
                                │             │
                                └──────┬──────┘
                                       ↓
                              [ deliverable/*.zip ] → iTMS 様
```

## 起動順 (Phase 計画詳細は PLAN.md / EXECUTION_PLAN.md)

1. **Phase 0** Setup ✅ closed 2026-04-29
2. **Phase 0.5** 用語調研 ✅ closed 2026-04-29 (term_mapping.yml v0.3 PASS, 後 v0.5 改訂)
3. **Phase 0.7** Excel 基盤 ✅ closed 2026-04-29 (style_guide + cover_template + build_xlsx.py)
4. **Phase 0.5.8** 用語集骨格 ✅ closed 2026-04-29 (99_用語集.xlsx v0.1)
5. **Phase 1** P0 四点セット (04 → 01 → 02 → 03) ⏳ in_progress 2/4 (04 + 01 PASS; 中間版 v0.5 提出済 2026-04-30)
6. **Phase 2** P1 補完 (05 詳細設計書) — pending
7. **Phase 3** P2 仕上げ (06 / 07 v1.0 化 / 99 中文列充填) — pending
8. **Phase 4** Pack & Handoff (最終 zip + RETROSPECTIVE) — pending

## 関連リンク (源)

- 上流プロジェクト全体: `../../CLAUDE.md`
- 索引: `../../.work/MANIFEST.md` (Chain J 登録あり)
- 設計参照: `../DESIGN_RAG_KG.md`, `../TRACEABILITY.md`, `../PROGRESS.md`
- 検証エビデンス: `../../.work/06_deep_verification/`
