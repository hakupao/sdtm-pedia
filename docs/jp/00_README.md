# docs/jp/ — iTMS 様 納品ドキュメント (Internal Index)

> **Notice**: 本 README は **内部利用用** (リポジトリ内ナビゲーション目的). 納品物には含めない.

## 概要

iTMS 株式会社 様 向けに, SDTM 知識ベースプロジェクトを **日本職場の標準ドキュメント形式 (Excel 主体)** で再構成した一式.

源プロジェクト (`knowledge_base/` / `.work/` / `docs/`) は read-only. 本目录は純粋下流の **翻訳 + 形式整備 + 再パッケージ** branch.

## 主要文書

| ファイル | 種別 | 状態 |
|---------|------|------|
| `PLAN.md` | 内部 — 計画書 (WHAT/WHY) | DRAFT v0.2 |
| `EXECUTION_PLAN.md` | 内部 — 実行計画書 (HOW + agent 调度) | DRAFT v0.1 |
| `_progress.json` | 内部 — 進捗真源 | active |
| `CHANGELOG.md` | 内部 — 改訂履歴一元管理 | active |
| `WORKLOG.md` | 内部 — 日次作業ログ (日本語, iTMS 様可視) | active |
| `glossary/term_blacklist.yml` | 内部 — 使用禁止語リスト | initial |
| `glossary/reference_standards.md` | 内部 — 参照規格一覧 | initial (URL 補完は Phase 0.5) |
| `glossary/term_mapping.yml` | 内部 — 用語写像辞書 | (Phase 0.5 産物, 未作成) |
| `templates/style_guide.xlsx` | 内部 — 配色 / フォント テンプレ | (Phase 0.7 産物, 未作成) |
| `templates/cover_template.xlsx` | 内部 — 表紙統一様式 | (Phase 0.7 産物, 未作成) |
| `01_基本設計書.xlsx` | 納品 — P0 | 未作成 |
| `02_運用保守マニュアル.xlsx` | 納品 — P0 | 未作成 |
| `03_テスト結果報告書.xlsx` | 納品 — P0 | 未作成 |
| `04_要件定義書.xlsx` | 納品 — P1 | 未作成 |
| `05_詳細設計書.xlsx` | 納品 — P1 | 未作成 |
| `06_トレーサビリティ管理表.xlsx` | 納品 — P2 | 未作成 |
| `07_進捗報告書.xlsx` | 納品 — P2 | 未作成 |
| `99_用語集.xlsx` | 納品 — 附属 | 未作成 |

## ドキュメント関係図 (Phase 完了時に最終化)

```
[ PLAN.md ] ─── (WHAT/WHY) ───┐
                              │
[ EXECUTION_PLAN.md ] ─── (HOW) ─┐
                                  │
                              ┌───┴────┐
                              ↓        ↓
                        [ 納品 8 文書 ]   [ glossary/ ]
                              │              │
                              └─────┬────────┘
                                    ↓
                          [ deliverable/*.zip ] → iTMS 様
```

## 起動順 (Phase 計画詳細は EXECUTION_PLAN.md)

1. **Phase 0** Setup (本骨格作成) ← *current*
2. **Phase 0.5** 用語調研 (1-2 日, 短縮厳禁)
3. **Phase 0.7** Excel 基盤 (style_guide + cover_template + build script PoC)
4. **Phase 1** P0 三点セット (01 / 02 / 03)
5. **Phase 2** P1 補完 (04 / 05)
6. **Phase 3** P2 仕上げ (06 / 07 + 00_README + 99_用語集)
7. **Phase 4** Pack & Handoff (zip 化 + RETROSPECTIVE)

## 関連リンク (源)

- 上流プロジェクト全体: `../../CLAUDE.md`
- 索引: `../../.work/MANIFEST.md` (Chain J 登録あり)
- 設計参照: `../DESIGN_RAG_KG.md`, `../TRACEABILITY.md`, `../PROGRESS.md`
- 検証エビデンス: `../../.work/06_deep_verification/`
