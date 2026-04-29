<!-- chain: J (日本同事交付链 v0.2)
  修改本文件后, 必须检查:
  → docs/jp/_progress.json              (本目录进度真源, 待 P0 创建)
  → docs/jp/CHANGELOG.md                (本目录改訂履歴, 待 P0 创建)
  → docs/jp/glossary/term_blacklist.yml (内部 jargon 黑名单, 待 P0 创建)
  → docs/jp/templates/style_guide.xlsx  (浅色 IT+医療 配色テンプレ, 待 P0 创建)
  → ../../.work/MANIFEST.md             (顶层快速参考表新增 docs/jp/ 入口)
  → ../../.work/meta/worklog.md         (执行记录追加)
  → ../../CLAUDE.md Key Paths           (新增 1 行: docs/jp/ → iTMS 向け納品目录)
-->

# docs/jp/ — iTMS 様 納品ドキュメント整備計画

> 创建: 2026-04-29
> 改訂: 2026-04-29 v0.1 → v0.2 → **v0.3** (要件定義書 を P0 に格上げ / 工程順序 04 → 01 → 02 → 03 順で着手, ユーザー判断 2026-04-29)
> 状态: **DRAFT v0.3** — Phase 0 + 0.5 + 0.7 + 0.5.8 完了, Phase 1 (P0 四点セット) 起動準備可
> Tier: **2** (5-15 step; ただし Excel パイプライン構築で borderline 3 に近い, 用語調研時間は別枠)
> 受信者: **iTMS 株式会社 (日本)** — IT + 医療データ両分野の知見ある想定読者
> 旁枝定位: 既存 `.work/` / `docs/` / `ai_platforms/` の純粋下流. 源産物は一切変更せず, **翻訳 + 形式整備 + 再パッケージ** のみ.

---

## 0. Charter

### 0.1 目的 (Why)

本プロジェクト (SDTM 知識ベース + 検証エビデンス) を **iTMS 様** が違和感なく受け取り, 自社業務に組み込めるよう, **日本職場の標準ドキュメント形式 (Excel 主体)** で再構成する.

### 0.2 範囲 (Scope)

**In-scope**:
- 7 種の正式ドキュメント (§1 一覧)
- **Excel (.xlsx) 主体** の納品 (md は内部下書き / バージョン管理用途のみ)
- 浅色 IT + 医療系の視覚デザイン
- IT + 医療 双方の規格を参照した日本語用語選定
- 表紙 / 改訂履歴 / 承認欄 / 用語集 / 図表編号 等 形式要素

**Out-of-scope**:
- 検証の再実施 / 知識ベースの再生成 (既存エビデンスを引用のみ)
- 源 PDF / xlsx の翻訳 (CDISC 標準は英語原文を保持)
- `ai_platforms/` 双プラットフォーム展開ドキュメントの日本語化 (**Decision §8.5: 本旁枝に含めない**)
- 法務契約書類 (NDA / SOW)
- リアルタイム同期 (源材料更新時は手動同期, §7)

### 0.3 不做 (Non-Goals)

- ❌ 全文逐語翻訳ではない. **形式再構築 + 結論翻訳 + 字面依据は英語原典へリンク**.
- ❌ 開発過程の内部用語 (atom / ledger / round / batch / Rule D / subagent / Tier / PASS 四条 …) を納品物に残さない. **§11 用語規律で完全に除去**.
- ❌ 自動同期パイプライン構築 (頻度低 + 翻訳品質要求高 → 手動が合理的).

---

## 1. 文書一覧 (Priority + 来源マッピング + Excel シート構成)

**優先度方針 (v0.3 改訂)**: 工程順序 (要件 → 基本 → 運用 → 試験 → 詳細 → 進捗 → 横断) に整合させるため, 04 要件定義書 を P0 に格上げした. 着手順は 04 → 01 → 02 → 03 → 05 → 06 → 07 とする. ファイル番号 (NN_) は固定 (連番).

| # | 日本語文書名 | ファイル名 | 優先度 | 着手順 | Excel シート構成 | 主要参照源 | 想定工数 |
|---|------------|-----------|--------|--------|-----------------|-----------|---------|
| 4 | **要件定義書** | `04_要件定義書.xlsx` | **P0** | **1** | 表紙 / 改訂履歴 / 目次 / 1.背景目的 / 2.業務要件 / 3.機能要件 / 4.非機能要件 / 5.制約条件 / 6.前提条件 / 承認欄 | `METHODOLOGY.md` + `00_planning/` + `meta/retrospective.md` | 2-3h |
| 1 | **基本設計書** | `01_基本設計書.xlsx` | **P0** | **2** | 表紙 / 改訂履歴 / 目次 / 1.概要 / 2.全体構成 / 3.データモデル / 4.外部 IF / 5.制約事項 / 6.参考資料 / 承認欄 | `docs/DESIGN_RAG_KG.md` + schema | 3-4h |
| 2 | **運用・保守マニュアル** | `02_運用保守マニュアル.xlsx` | **P0** | **3** | 表紙 / 改訂履歴 / 目次 / 1.システム概要 / 2.ファイル構成 / 3.日常運用手順 / 4.保守作業手順 / 5.障害対応 / 6.連絡先 / 承認欄 | `README.md` + `MANIFEST.md` 抜粋 | 2-3h |
| 3 | **テスト結果報告書** | `03_テスト結果報告書.xlsx` | **P0** | **4** | 表紙 / 改訂履歴 / 目次 / 1.試験概要 / 2.試験範囲 / 3.実施結果サマリ / 4.検出事項一覧 / 5.合格判定 / 6.エビデンス一覧 / 承認欄 | `_progress.json` + `audit_matrix.md` + `evidence/` | 2-3h |
| 5 | **詳細設計書** | `05_詳細設計書.xlsx` | P1 | 5 | 表紙 / 改訂履歴 / 目次 / 1.全体方針 / 2.データ項目定義 / 3.ファイル定義 / 4.処理フロー / 5.バリデーション規則 / 承認欄 | `schema/*.json` + `MANIFEST.md` | 3-4h |
| 6 | **トレーサビリティ管理表** | `06_トレーサビリティ管理表.xlsx` | P2 | 7 | 表紙 / 改訂履歴 / 凡例 / 要件 ⇆ 設計 ⇆ 試験 ⇆ エビデンス 横断表 / 承認欄 | `docs/TRACEABILITY.md` 再構成 | 1.5h |
| 7 | **進捗報告書** | `07_進捗報告書.xlsx` | P2 | 6 | 表紙 / 改訂履歴 / 1.全体サマリ / 2.工程別進捗 / 3.課題管理 / 4.今後の予定 / 承認欄 | `docs/PROGRESS.md` + `_progress.json` | 1.5h |

附属物:
- `00_README.md` — 本目录入口 + ドキュメント関係図 (md, 内部用)
- `99_用語集.xlsx` — 英 ⇆ 日 ⇆ 中 + 出典規格 (4 列対照)
- `CHANGELOG.md` — 改訂履歴一元管理 (md, 内部用)
- `_progress.json` — 進捗真源 (Tier 2 schema)
- `glossary/term_blacklist.yml` — 内部 jargon 黑名单 (使用禁止語)
- `glossary/term_mapping.yml` — 内部用語 → 公開用語 写像辞書
- `templates/style_guide.xlsx` — 配色 / フォント / セル書式 共通テンプレ
- `scripts/build_xlsx.py` (or `.mjs`) — yaml/csv 源 → スタイル付き .xlsx 生成スクリプト

---

## 2. 目录构造提案

```
docs/jp/
├── PLAN.md                          (本文書, 内部用)
├── 00_README.md                     入口 / 関係図 (内部用)
├── 01_基本設計書.xlsx              ★ P0 納品物
├── 02_運用保守マニュアル.xlsx      ★ P0 納品物
├── 03_テスト結果報告書.xlsx        ★ P0 納品物
├── 04_要件定義書.xlsx              P1 納品物
├── 05_詳細設計書.xlsx              P1 納品物
├── 06_トレーサビリティ管理表.xlsx  P2 納品物
├── 07_進捗報告書.xlsx              P2 納品物
├── 99_用語集.xlsx                  納品物 (附属)
├── CHANGELOG.md                    改訂履歴一元管理
├── _progress.json                  進捗真源
├── sources/                        各 .xlsx の源データ (yaml/csv)
│   ├── 01_基本設計書.yml
│   ├── 02_運用保守マニュアル.yml
│   └── ...
├── glossary/
│   ├── term_blacklist.yml          使用禁止語リスト
│   ├── term_mapping.yml            内部用語 → 公開用語
│   └── reference_standards.md      参照規格一覧 (§11.3)
├── templates/
│   ├── style_guide.xlsx            配色 / フォント 共通テンプレ
│   └── cover_template.xlsx         表紙統一様式
├── scripts/
│   └── build_xlsx.{py|mjs}         .xlsx 生成器
├── deliverable/                    納品 zip パッケージ最終版
│   └── YYYYMMDD_iTMS_SDTM_納品物_v1.0.zip
└── assets/
    └── (図N-N_xxx.png)
```

---

## 3. 形式約定 (Excel + 文書共通)

### 3.1 Excel 視覚デザイン (浅色 IT + 医療系)

**配色パレット** (HEX):

| 用途 | カラー | 補足 |
|------|--------|------|
| メインアクセント (見出し帯) | **#1F4E79** (深ティール) | IT 系信頼感 |
| サブアクセント (副見出し) | **#2E86AB** (中明度ブルー) | |
| ヘッダー行背景 | **#D9E7F1** (淡ブルー) | 黒文字で視認性確保 |
| ゼブラ縞 (奇数行) | **#F4F8FB** (極淡ブルー) | |
| 罫線 | **#A6B5C2** (中明度グレー) | thin |
| 強調 (PASS/合格) | **#4D8B7C** (医療グリーン) | 多用禁止, アクセントのみ |
| 警告 (要対応) | **#C97B5C** (落ち着いたオレンジ) | 赤は使わない (医療系で警告色強すぎ) |
| 背景 | **#FFFFFF** (純白) | 余白多めに |
| 補助テキスト | **#5A6B7A** (グレー) | キャプション等 |

**禁止配色**: 鮮やかな赤 / 蛍光色 / グラデーション / 影 / 立体効果.

**フォント**:
- 日本語: **Yu Gothic UI** 第一候補, fallback **Meiryo UI** → **Noto Sans JP**
- 英数字: **Segoe UI** または **Arial**
- 等幅 (コード/パス): **Consolas** または **Yu Gothic UI Mono**
- サイズ: 表紙タイトル 20pt / 章見出し 14pt / 本文 11pt / 注記 9pt

**セル書式**:
- 行高: 本文 18pt / 見出し 24pt
- 列幅: 内容に合わせ調整, 横スクロール最小化
- 罫線: thin の medium gray, 過剰罫線禁止 (表外側 + ヘッダー下のみが原則)
- 折り返し: 文章セルは「折り返して全体表示」ON
- ウィンドウ枠固定: ヘッダー行 + 識別列を固定
- 印刷設定: A4 縦, 余白 normal, ヘッダー繰返し設定済

### 3.2 各シート冒頭の必須要素

```
─────────────────────────────────
【表紙シート】
  - 文書名 (大きく中央)
  - 文書番号 (例: ITMS-SDTM-01-BASIC-DESIGN-v1.0)
  - 受信者: iTMS 株式会社 御中
  - 作成: (作成者名)
  - 作成日 / 最終更新日
  - 版数 (v1.0)
─────────────────────────────────
【改訂履歴シート】
  | 版 | 改訂日 | 改訂内容 | 作成 | 確認 | 承認 |
─────────────────────────────────
【目次シート】
  各シートへのハイパーリンク
─────────────────────────────────
【本文シート群】
  1. はじめに (本書の目的 / 想定読者 / 関連文書)
  2. ...本論...
  N. 用語集 (`99_用語集.xlsx` へのリンク)
  N+1. 参考資料 (英語原典への絶対パス + 取得日)
─────────────────────────────────
【承認欄シート】
  | 役割     | 氏名 | 日付 | 押印/署名 |
  |----------|------|------|----------|
  | 作成     |      |      |          |
  | 確認     |      |      |          |
  | 承認     |      |      |          |
─────────────────────────────────
```

### 3.3 文体規律
- **である調** で統一 (「です・ます」混在禁止)
- 一文一義 / 主語明示 / 受動態多用回避
- 半角英数字 + 全角句読点「、」「。」
- 専門用語は初出時に括弧で英語併記 (例: 「臨床試験データ表形式モデル (SDTM: Study Data Tabulation Model)」)
- **§11 用語規律** に厳格準拠

### 3.4 図表
- 図番号: **図N-N** / 表番号: **表N-N**
- キャプション必須, 図表下に配置
- 出典明記 (例: 「出典: 米国 CDISC 規格 SDTMIG v3.4 第 119 頁」)
- スクリーンショットは `assets/` に配置, .xlsx 内挿入

---

## 4. ファイル命名 + 版数

### 4.1 ファイル名
- リポジトリ内: `NN_文書名.xlsx` (連番 + 日本語)
- 納品時 zip: `YYYYMMDD_iTMS_SDTM_納品物_vX.Y.zip`
- 個別ファイル納品時: `YYYYMMDD_ITMS-SDTM-NN_文書名_vX.Y.xlsx`
  - 例: `20260429_ITMS-SDTM-01_基本設計書_v1.0.xlsx`

### 4.2 版数
- **v0.x** = DRAFT (社内レビュー前)
- **v1.0** = 初版 iTMS 様提出可 (全 PASS 後)
- **v1.x** = 軽微修正 (誤記訂正, 補足追記)
- **v2.0+** = 構造変更を伴う改訂

### 4.3 改訂履歴
- 全文書の履歴を `CHANGELOG.md` に集約
- 各 .xlsx の「改訂履歴」シートにも同内容を転記 (両方更新)
- 形式: `## ITMS-SDTM-NN vX.Y (YYYY-MM-DD)` + 箇条書き

---

## 5. Phase 計画

### Phase 0 — Setup (0.5 日)
- [ ] `_progress.json` 作成 (Tier 2 schema)
- [ ] `CHANGELOG.md` 作成 (空テンプレ)
- [ ] `00_README.md` 作成 (関係図 placeholder)
- [ ] ディレクトリ骨格作成 (`sources/` `glossary/` `templates/` `scripts/` `assets/` `deliverable/`)
- [ ] `.work/MANIFEST.md` + `CLAUDE.md` Key Paths 更新

### Phase 0.5 — 用語調研フェーズ (1-2 日 ★ 短縮厳禁)
**制約 §10 硬約束 H-1/H-2 への必須対応工程**

- [ ] §11.3 参照規格を全て一次資料で確認 (URL + 取得日記録)
  - IPA 設計書テンプレート / JIS X 0160 / JIS X 25010
  - PMDA ER/ES 指針 / 厚労省コンピュータ化システム適正管理ガイドライン
  - GAMP 5 / GAMP Good Practice Guide
  - ICH GCP E6(R3) / CDISC 公式日本語訳 (CJUG)
  - JIS T 14971 (医療機器リスクマネジメント, 参考)
- [ ] 内部 jargon 全洗い出し → `glossary/term_blacklist.yml`
- [ ] 各内部用語の公開言換え案 → `glossary/term_mapping.yml` (1 用語 3 候補 + 採用根拠)
- [ ] reviewer subagent で言換え案を独立審査 (異 subagent_type)
- [ ] 用語集骨格 `99_用語集.xlsx` 初版

**PASS 条件 (Phase 0.5)**:
1. 参照規格全件に一次資料リンク
2. blacklist + mapping が独立 reviewer PASS
3. 用户 (Bojiang) ack

### Phase 0.7 — Excel スタイル基盤 (0.5 日)
- [ ] `templates/style_guide.xlsx` 作成 (§3.1 配色 + フォント + セル書式 サンプル収録)
- [ ] `templates/cover_template.xlsx` 作成 (表紙 + 改訂履歴 + 承認欄 統一様式)
- [ ] `scripts/build_xlsx.{py|mjs}` PoC (yaml → スタイル付き .xlsx)
  - openpyxl (Python) 採用候補 / exceljs (Node) 候補 — Phase 0.7 で確定
- [ ] サンプル文書で生成 → 視覚 QA

**PASS 条件 (Phase 0.7)**:
1. 生成 .xlsx が §3.1 デザイン基準に 100% 準拠
2. 用户 (Bojiang) 視覚 ack ("好看" 基準クリア)

### Phase 1 — P0 四点セット (2.5-3.5 日, v0.3 改訂)
直列推奨 (`04` → `01` 完成後 `02` `03` を並列).

- [ ] `04_要件定義書.xlsx` (着手順 1) ← writer (sonnet) → reviewer (opus, 異 subagent_type) → 用語監査 (§11) → 用户 ack
  - **本旁枝で先頭に書く意図**: 01-03 全文書の根拠章となる「目的 / 業務要件 / 制約条件」を確定し, 後段文書が 04 の節を引用できるようにする.
- [ ] `01_基本設計書.xlsx` (着手順 2) ← 04 の業務 / 機能要件を引用 → 同じ 4 工程
- [ ] `02_運用保守マニュアル.xlsx` (着手順 3) ← 04 の非機能 / 制約条件を引用 → 同上
- [ ] `03_テスト結果報告書.xlsx` (着手順 4) ← 04 の前提条件で試験範囲を画定 → 同上 (エビデンス引用必須)

**PASS 五条** (各文書):
1. エビデンス引用が全て実在ファイルにリンク (Bash で grep 検証)
2. §3 形式約定 100% 準拠
3. 独立 reviewer subagent (異 subagent_type) PASS
4. **§11 用語規律 監査 PASS** (blacklist 残存ゼロ + mapping 適用済)
5. 用户 (Bojiang) 口頭 ack

### Phase 2 — P1 補完 (1 日, v0.3 改訂で 04 を Phase 1 に移したため 05 のみ)
- [ ] `05_詳細設計書.xlsx` ← 01 基本設計の章別詳細展開

### Phase 3 — P2 仕上げ (1 日)
- [ ] `06_トレーサビリティ管理表.xlsx`
- [ ] `07_進捗報告書.xlsx`
- [ ] `00_README.md` 完成版
- [ ] `99_用語集.xlsx` 完成版

### Phase 4 — Pack & Handoff (0.5 日)
- [ ] 全文書 cross-link 検証 (リンク切れなし)
- [ ] zip パッケージ作成 → `deliverable/YYYYMMDD_iTMS_SDTM_納品物_v1.0.zip`
- [ ] `RETROSPECTIVE.md` 記録 (規則 C 強制)
- [ ] CLAUDE.md からの参照経路最終確認

**全体 PASS**: Phase 0-4 全 PASS + 用户 final ack

---

## 6. PASS 五条 (本旁枝 適用)

CLAUDE.md 規則 D + 本旁枝固有の用語規律により五条:

1. **エビデンス存在** — 引用元の英語原典 / work artifact が実在
2. **writer 産物合規** — §3 形式約定 100% 準拠
3. **独立 reviewer subagent PASS** — writer と異なる `subagent_type` (同 context 自審禁止)
4. **§11 用語規律 監査 PASS** — blacklist 残存ゼロ + mapping 完全適用
5. **用户口頭 ack** — Bojiang の最終承認

**追加考慮**:
- 日本語の自然さは AI subagent では完全保証できない
- → 「日方ネイティブ review」を **Out-of-band な人手 gate** として明示, PLAN 上は「pending JP review」状態を許容
- 該当 issue は `docs/jp/issues_pending_jp_review.md` に蓄積 (発生時作成)

---

## 7. 維持戦略 (源材料との同期)

| 源材料 | 影響を受ける JP 文書 | 同期方針 |
|--------|---------------------|---------|
| `knowledge_base/` 内容変更 | 03 テスト結果, 06 トレーサビリティ | round 単位で手動更新 |
| `docs/DESIGN_RAG_KG.md` | 01 基本設計, 05 詳細設計 | major change 時のみ |
| `.work/06_deep_verification/_progress.json` | 03 テスト結果, 07 進捗 | 節目で更新 |
| schema 変更 | 01 基本設計, 05 詳細設計 | フリーズ単位 |
| README / CLAUDE.md | 02 運用保守 | 半年に 1 回 review |

自動化は不要. 手動 + CHANGELOG 記録で十分.

---

## 8. Decisions (受信者確認済)

| # | 質問 | Decision (2026-04-29) |
|---|------|---------------------|
| 1 | 受信者 | **iTMS 株式会社 (日本)** |
| 2 | 納品形式 | **Excel (.xlsx) 主体, 視覚デザイン重視** |
| 3 | 公司既定テンプレ | **無し** → §3.1 を本プロジェクト基準として採用 |
| 4 | 機密区分 | **公開可 (普通文書扱い)** |
| 5 | `ai_platforms/` 日本語化 | **本旁枝に含めない** (将来別旁枝で検討) |

---

## 9. Open Issues (要追跡)

- I-1: 日方ネイティブ reviewer の特定 (現状 unspecified, §6 PASS の人手 gate 運用に直結)
- I-2: Excel 生成基盤の選定 (openpyxl vs exceljs) — Phase 0.7 で確定

---

## 10. 制約条件 (Constraints — 全工程 厳守)

### 10.1 硬約束 (Must / Must NOT)

**H-1: 用語規律**
- ❌ 開発過程の内部用語を一切納品物に残さない (atom / ledger / round / batch / Rule D / subagent / Tier / PASS 四条 / drift / dropout / writer / reviewer / chain / worklog / progress.json / handoff / multi-session / kickoff / reconciler 等)
- ❌ 口語表現禁止 (「だいたい」「ちゃんと」「ざっくり」「いい感じ」等)
- ❌ 英語ジャーゴン直訳禁止 (例: 「アトム」「レジャー」「サブエージェント」)
- ✅ **誰でも理解できる, 最も平易で正確な日本語** を使用
- ✅ 専門用語は **§11.3 参照規格のいずれか** に出典を持つ語のみ採用
- ✅ 出典規格を `99_用語集.xlsx` に明記

**H-2: 用語選定根拠**
- ❌ 安直な機械翻訳 / GPT 一発翻訳禁止
- ✅ **IT 規格 (IPA / JIS / GAMP) と医療規格 (PMDA / 厚労省 / ICH / CDISC 日本語訳) の双方** を必ず参照
- ✅ 1 用語につき最低 3 候補を出し採用根拠を `glossary/term_mapping.yml` に記録
- ✅ 調査時間を惜しまない. 短縮 = 規律違反

**H-3: 納品物形式**
- ✅ 主納品物は **必ず .xlsx** (md は内部下書きのみ)
- ✅ §3.1 配色 / フォント / セル書式 100% 準拠
- ❌ 派手な色 / 立体効果 / 影 / グラデーション禁止

**H-4: 機密区分**
- 公開可レベル (CDISC 規格自体が public). ただし作成者個人情報は含めない.

**H-5: 範囲制限**
- `ai_platforms/` 関連は本旁枝で扱わない
- 源産物 (`.work/` `knowledge_base/` `source/`) は read-only

### 10.2 軟偏好 (Prefer)

**S-1: 視覚デザイン**
- 浅色 IT + 医療系 (深ティール / 淡ブルー / 医療グリーン アクセント)
- 余白多め, 罫線控えめ, 折り返し丁寧
- 「内容正確 + 設計美しい」の両立 (片方だけでは S-1 不適合)

**S-2: 文書間の一貫性**
- 全 7 文書で表紙 / 改訂履歴 / 承認欄 / フォント / 配色を統一
- → `templates/style_guide.xlsx` + `cover_template.xlsx` で担保

**S-3: 印刷可読性**
- A4 縦 / 横 適切に選択, 1 シート 1 トピック
- ヘッダー行繰返し設定

---

## 11. 用語規律 (Terminology Discipline)

### 11.1 内部 jargon 黑名单 (Blacklist — 納品物使用禁止語)

`glossary/term_blacklist.yml` で管理. 以下は初期リスト:

```
# 開発工程内部用語 (絶対に納品物に残さない)
- atom               # → 「項目」「データ単位」
- ledger             # → 「管理表」「突合表」
- round              # → 「回次」「フェーズ」
- batch              # → 「ロット」「バッチ処理」(文脈次第で言換え)
- Rule D             # → 「審査独立性原則」
- subagent           # → 「担当者」「処理プロセス」
- Tier 1/2/3         # → 公開不要 (内部分類)
- PASS 四条          # → 「合格判定基準」
- drift              # → 「ずれ」「乖離」
- dropout            # → 「対象外」「除外項目」
- writer / reviewer  # → 「作成担当」「確認担当」
- chain              # → 「変更連鎖」「同期対象」
- worklog            # → 「作業記録」
- progress.json      # → 「進捗管理ファイル」
- handoff            # → 「引継ぎ」
- multi-session      # → 「並列作業」
- kickoff            # → 「開始指示」
- reconciler         # → 「整合確認担当」
- evidence           # → 「証跡」「裏付資料」
- ack                # → 「承認」「確認」
- gate               # → 「関門」「判定」
- cut                # → 「版締め」
```

### 11.2 用語写像辞書 (Term Mapping)

`glossary/term_mapping.yml` 形式:

```yaml
- internal: atom
  candidates:
    - "項目"
    - "データ単位"
    - "情報単位"
  adopted: "データ単位"
  reason: |
    GAMP 5 §「Data Integrity」では "data unit" の訳語として
    「データ単位」が定着. JIS X 0160 でも同様. 「項目」は
    DB カラムと混同される恐れがあるため不採用.
  reference:
    - "GAMP 5 (2nd Ed.) §M2"
    - "JIS X 0160:2021 §3.1.7"
```

全 blacklist 項目に対し同形式で記録. **空欄禁止 / reference 欄必須**.

### 11.3 参照規格一覧 (Dual Standard Reference Framework)

`glossary/reference_standards.md` で管理. **必ず一次資料 URL + 取得日を記録**.

**IT 系**:
- **IPA (情報処理推進機構)** — 「機能要件の合意形成ガイド」「非機能要求グレード」「システム要件定義ガイドライン」
- **JIS X 0160:2021** — ソフトウェアライフサイクルプロセス
- **JIS X 25010:2013** — システム及びソフトウェア品質モデル
- **JIS X 0129** — ソフトウェア製品の品質
- **共通フレーム 2013 (SLCP-JCF2013)** — 日本独自の SLCP 拡張

**医療 / 製薬系**:
- **PMDA「医薬品等の承認又は許可等に係る申請等における電磁的記録及び電子署名の利用について」(ER/ES 指針)**
- **厚生労働省「コンピュータ化システム適正管理ガイドライン」(2010)**
- **GAMP 5 (2nd Edition, 2022)** — ISPE 発行, 製薬 IT バリデーション国際標準
- **ICH E6(R3) GCP** — 臨床試験実施基準
- **ICH M11** — 臨床電子構造化プロトコル
- **CDISC 公式日本語訳 (CDISC Japan User Group / CJUG)** — SDTM IG 等の用語日本語版
- **JIS T 14971:2020** — 医療機器のリスクマネジメント (参考程度)

**文書形式系**:
- **JIS Z 8301:2019** — 規格票の様式及び作成方法
- **公用文作成の考え方 (文化庁, 2022)** — 文体一般

### 11.4 用語監査プロセス (PASS 五条 第 4 条)

各 .xlsx 完成後, **Bash + reviewer subagent** で以下を実行:

```bash
# 1. blacklist 残存検査 (xlsx → 文字列抽出 → grep)
python scripts/audit_terms.py 01_基本設計書.xlsx --blacklist glossary/term_blacklist.yml

# 2. mapping 適用検査 (採用語が一貫使用されているか)
python scripts/audit_terms.py 01_基本設計書.xlsx --mapping glossary/term_mapping.yml --check-consistency
```

両検査 PASS + 独立 reviewer subagent の人手判定 PASS で **第 4 条クリア**.

---

## 12. Next Action

**Phase 0 Setup** (5 ファイル + ディレクトリ骨格作成 + MANIFEST/CLAUDE.md 更新) を実行.
完了後 **Phase 0.5 用語調研フェーズ** を起動 (1-2 日, 短縮厳禁).
P0 三文書の writer 起動は Phase 0.7 完了後 (テンプレ + 用語辞書揃ってから).

---

> **Note**: 本 PLAN は Tier 2 規格. round / batch 等の Tier 3 仪式は不要.
> ただし用語調研 (Phase 0.5) と Excel 基盤構築 (Phase 0.7) は規律強化のため工数別枠.
> 進捗は `_progress.json` 単一ソースで管理.
