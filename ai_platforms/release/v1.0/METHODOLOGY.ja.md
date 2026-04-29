---
lang: ja
slug: methodology
order: 15
title: "構築方法と信頼性"
---

# 構築方法と信頼性 — このナレッジベースはどう作られ, なぜ信頼できるのか

> 最終更新: 2026-04-29 · ビルドと並行して維持されており, マーケティング資料ではありません.

「AI で抽出した SDTM ナレッジベース」と聞いて最初に湧く疑問は *「ハルシネーションは? ページ抜けは? 誰かちゃんと検証したのか?」* です. このページがその答えです. 何をやったか, 何が追跡可能か, 途中でどんな誤りが見つかったか, そして個別の回答を読者自身がどう監査できるかを記載しています.

1 節だけ読むなら [§4 — 検証と既知の問題](#4-検証と既知の問題) を読んでください.

---

## 1. 出典

`knowledge_base/` 内のあらゆる成果物は, 4 つの CDISC 公式刊行物のいずれかにたどれます. 第三者の要約や言い換えで生成されたものはありません.

| 出典 | バージョン | 範囲 |
|---|---|---|
| SDTM Implementation Guide PDF | v3.4 (2021-11-29) | 461 ページ — ドメイン spec / assumptions / examples |
| SDTM Model PDF | v2.0 Final (2021-11-29) | 74 ページ — 概念モデル |
| SDTMIG xlsx | v3.4 | 63 ドメイン / 1,917 変数 |
| CDISC Controlled Terminology xlsx | 2024 リリース | 1,005 codelist / 37,939 term |

原ファイルは著作権の都合で本リポジトリには含めていません. 詳細は [DISCLAIMER](https://github.com/hakupao/sdtm-pedia/blob/main/DISCLAIMER.md) を参照.

## 2. 構築プロセス

7 フェーズのパイプラインです. 各フェーズに独立した plan / 実行ログ / 検証記録があり, リポジトリの [`.work/`](https://github.com/hakupao/sdtm-pedia/tree/main/.work) 配下に置かれています — 別建てのドキュメントサイトではなく, ソースの一部です.

| フェーズ | 内容 | 主な成果物 |
|---|---|---|
| 1 | xlsx → Markdown 変換 (Python) | 63 個の `spec.md` + terminology |
| 2 | PDF ページインデックス (プログラム生成, 視覚読み取りではない) | `page_index.json` |
| 3 | AI 補助による PDF 抽出, 11 バッチ | 各ドメインの `assumptions.md` + `examples.md` |
| 4 | 補足コンテンツ抽出 | 6 つの model + 6 つの chapter |
| 5 | 全体検証パス + マスター索引 | `INDEX.md` + 検証レポート |
| 6 | 検索最適化 (ルーティング + 逆引き索引) | `ROUTING.md` + `VARIABLE_INDEX.md` (1,523 変数) |
| 6.5 | AI プラットフォーム展開 | 4 プラットフォーム配布バンドル |

別途, **リテラルレベル深度検証監査** が継続トラックとして進行中です. ナレッジベース内のすべての原子レベル記述を, ソース PDF とページ単位で照合します. 2026-04-29 時点で対象範囲の **97% ページが検証済み** で, 監査は継続中. バッチごとのレポートは [`.work/06_deep_verification/evidence/checkpoints/`](https://github.com/hakupao/sdtm-pedia/tree/main/.work/06_deep_verification/evidence/checkpoints) にあります.

## 3. トレーサビリティ — 個別の回答をどう監査するか

リポジトリは, 読み手がナレッジベースを PDF と数秒で照合できる構造に意図して作っています.「信じてください」のレイヤーはありません.

**ドメインレベルの回答を検証する場合:**

1. 回答内のドメインコード (`AE` / `LB` / `DM` 等) を確認.
2. `knowledge_base/domains/<DOMAIN>/` を開く:
   - `spec.md` — 変数レベル仕様 (xlsx 由来, Core / type / codelist 紐付けを含む)
   - `assumptions.md` — ドメイン固有のビジネスルール (PDF 由来)
   - `examples.md` — 実装例 (PDF 由来)
3. 各ファイル冒頭に対応する PDF ページ範囲が記載されているので, SDTMIG v3.4 PDF と照合.
4. 変数の Core / codelist 紐付けは, 手元に SDTMIG xlsx があれば直接照合できる.

**章レベルの回答**: `knowledge_base/chapters/chXX_*.md` を開く. ページ範囲と節番号は PDF 目次と直接対応.

**用語レベルの回答**: `knowledge_base/terminology/` の各 codelist ファイルには CDISC C-code (例: `C66731`) が付与されているため, NCI EVS Browser で逆引き可能.

source-to-output 全体マップはリポジトリの [`docs/TRACEABILITY.md`](https://github.com/hakupao/sdtm-pedia/blob/main/docs/TRACEABILITY.md) にあります.

## 4. 検証と既知の問題

検証段階で 2 つのシステム的な問題が見つかり, 公開アーカイブ済みです. 隠していません — この 2 つの発見こそが「検証プロセスが実際に機能している」最も有力な証拠だからです.

### Issue 1 — ページインデックスのずれ (2026-04-15, 解決済み)

PDF の画像・図表索引の初版は, AI エージェントによる視覚的なページ番号読み取りに依存していました. ドメイン専門家による抜き取り検査で, TD example のページ参照が 4 ページずれていることが判明し, 同種の ±2–4 ページのずれが約 60 図に分散していました.

**根因**: AI は PDF を読む際, ページ境界を正確には観測できず, 推定しています. パイプラインが当時「正確値」と「推定値」を区別していませんでした.

**修正**: ページインデックスをプログラム生成に作り直し, `page_index.json` を唯一の権威ソースとし, 下流ファイルはこれを参照. AI が出すページ推定値は明示的に `(estimated)` とラベル付け, 権威索引には直書きしない運用に変更.

詳細調査: [`.work/03_verification/issue1_investigation.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/03_verification/issue1_investigation.md).

### Issue 2 — 骨組みだけのコンテンツが PASS 判定された (2026-04-15, 解決済み)

`ch04_general_assumptions.md` は初回検証で PASS と判定されたが, 約 30% のサブセクションが 1–2 文のプレースホルダーと `<!-- 待補全 -->` マークのみでした. PDF のこの章は 38 ページの詳細ルール; 当時のファイルは 1 ページあたり約 9 行, 修正後は約 17 行になります.

**根因**: PASS 基準が *「欠落コンテンツが明示的にマークされている」* を *「コンテンツが完全である」* と等価に扱っていた. 加えて, 同一エージェントが書き手と承認者を兼ねており, PDF を独立に読む reviewer が不在でした.

**修正**: マーク済み全サブセクションを PDF から再構築. PASS 基準を定量化: 行数/ページ比のベースライン, ゼロプレースホルダー, ポイントカバレッジ ≥95%. 以後, ファイルを書くエージェントと承認するコンテキストは必ず別.

詳細記録: [`.work/03_verification/issues_found.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/03_verification/issues_found.md).

### 既知の制約

AI プラットフォーム展開形態では完全に解決できない制約 (巨大 codelist のスタブ保存, 外部リアルタイム参照の非埋め込み等) があり, 別途追跡しています: [既知の制約](./known-limitations/).

## 5. 独立レビュー体制

上記 2 件の issue から 4 つの常駐ルールが生まれました. リポジトリ内の全フェーズ・全トラックで強制適用されます.

1. **定量的 PASS 基準.** カバレッジ比, 行数/ページ比, ゼロプレースホルダー — 主観的な「正しそう」は使わない.
2. **書き手と reviewer は別.** ファイルを書いたエージェント・プロセスは, それを承認するエージェントになれない. reviewer は独立に PDF を読み, 構造化されたカバレッジレポートを出力.
3. **AI 推定値はラベル必須.** AI がプログラム的に確認できないものは `(estimated)` とラベル付けし, 権威索引には直書きしない.
4. **人手による抜き取り検査がワークフローの一部.** 各フェーズ終了時に PDF と無作為標本を照合する — 後付けの保険ではない.

4 つのルールとそれらを生んだ失敗事例の完全な記録は [`.work/meta/retrospective.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/meta/retrospective.md) にあります.

加えて, 検証トラック自体が反復的です — §2 の深度検証監査は本稿執筆時点で 14 ラウンド目, 各ラウンドの記録が残り, 検出された差異がナレッジベースに反映されています.

## 6. これがあなたにとって何を意味するか

- **懐疑は歓迎.** 数秒でソースページに到達できます; 数字が怪しければ PDF と直接照合してください.
- **差異を発見したら報告を.** 深度検証が見落としていたら [GitHub issue](https://github.com/hakupao/sdtm-pedia/issues) にお寄せください. 監査トラックは終了期限のないオープンなものです.
- **規制提出の代替ではない.** このナレッジベースは, SDTM 業務に関わるエンジニア・プログラマー・レビュアーの日常作業を補助するためのものです. 規制提出には常に CDISC 公式刊行物を参照してください.

---

**リポジトリ:** [github.com/hakupao/sdtm-pedia](https://github.com/hakupao/sdtm-pedia) · **ライセンス:** CC BY 4.0
