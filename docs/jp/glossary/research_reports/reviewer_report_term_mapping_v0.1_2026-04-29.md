# Independent Review Report — term_mapping.yml v0.1

> Phase 0.5.6 産物 (規則 D 独立審査)
> 起草: `oh-my-claudecode:document-specialist` × 3 並列 (Batch 1/2/3) + 主 session 統合
> 審査: `oh-my-claudecode:code-reviewer` (異 subagent_type → 規則 D 隔離 ✅)
> 審査日: 2026-04-29
> 審査範囲: 全 33 エントリ + audit_targets ブロック + cross-batch reconciliation
> 一次資料照合: SDTMIG v3.2 日本語版 PDF 実機読込

---

## 総合判定

**CONDITIONAL_PASS** (PASS 不可)

理由: HIGH 1 件以上のため EXECUTION_PLAN §5 エスカレーション規定により再生成サイクル必須.

## 必須チェック結果 (10/10)

| # | 項目 | 結果 |
|---|------|------|
| 1 | candidates >= 3 | ✅ |
| 2 | reference >= 2 | ✅ (但 F-2 で内容空疎) |
| 3 | reference_standards.md 未掲載規格混入なし | ⚠️ F-1 (dropout 引用 §SE ドメイン p.130-145 が事実誤認) |
| 4 | adopted 語が口語表現でない | ✅ |
| 5 | カタカナ直訳なし (例外 2 種) | ✅ |
| 6 | CJUG D-2 明示 | ⚠️ F-3 (claim 7 / 実 6) |
| 7 | cross-batch 不整合整合済 | ✅ |
| 8 | 臨床用語衝突注記 | ✅ |
| 9 | Tier 1/2/3 全件「公開不要」 | ✅ |
| 10 | 口語語 4 件 文化庁公用文引用 | ✅ |

集計: ✅ 7 / ⚠️ 部分違反 3.

## audit_targets メタ整合性

| 主張 | 実測 | 差分 |
|------|------|------|
| `total_entries: 33` | 33 件 | ✅ |
| `cjug_d2_application_count: 7` | 6 件 (dropout 欠落) | ❌ F-3 |
| `paid_standards_referenced_via_alternatives: 4` | 2 件 (X 25010 / T 14971 引用ゼロ) | ❌ F-5 |

---

## Findings (11 件)

### F-1 [HIGH] dropout 引用 §SE ドメイン p.130-145 が事実誤認

- 該当: `dropout` (line 234-247)
- 問題: reference 第 3 件 `CJUG SDTMIG v3.2 §SE ドメイン p.130-145` は誤り
- 一次資料確認: PDF p.130-145 は DM (被験者背景) + SE (被験者エレメント) ドメイン用例で dropout 用語定義頁ではない
- **正解**: SDTMIG v3.2 における dropout の主要記載ドメインは **DS (Disposition Event)** で被験者中止理由 (DSDECOD = "DROPPED OUT" 等) として制御用語登録
- 修正案:
  ```yaml
  - "CJUG SDTMIG v3.2 §DS ドメイン (Disposition; 被験者中止理由) — 臨床 dropout との概念区別根拠 (公式訳なし; D-2 適用)"
  ```
- 影響度: HIGH (Bojiang のような SDTM 専門家が読めば即気づくレベル)

### F-2 [HIGH] 有償 JIS 規格の §節タイトル検証可能性体系的弱

- 該当: 多数 (handoff / cut / multi-session / reconciler / writer / reviewer / subagent / Rule D / gate / chain / drift / evidence / atom / progress.json / worklog 等)
- 問題: JIS X 0160:2021 / JIS Z 8301:2019 / 共通フレーム 2013 はすべて有償 (D-6 で「購入なし」決定済)
- §節名 (例: `JIS X 0160:2021 §プロセスインタフェース・入出力` `JIS X 0160:2021 §並行プロセスとプロセスインタフェース`) は kikakurui.com / パブコメ草案 / 概要 PDF では検証不能
- 起草担当による創作 § 名の可能性が高い (session_A レポート抜粋用語リストに該当語が現れない)
- 修正案 (短期):
  ```yaml
  # Before
  - "JIS X 0160:2021 §プロセスインタフェース・入出力"
  # After
  - "JIS X 0160:2021 ソフトウェアライフサイクルプロセス (kikakurui.com 抜粋で確認可能な範囲; 詳細§番号は有償全文未確認 — D-6 制約)"
  ```
- 修正案 (長期, Phase 2 以降): kikakurui.com で公開済の節を white list 化, 不在の場合は「業界慣用 + IPA で代替根拠」に置換
- 影響度: HIGH (Phase 0.6 audit script 実装時に外部レビュアが検証不能 → 起草担当の信頼性失墜)

### F-3 [MEDIUM] D-2 適用エントリ数カウント不一致 (7 vs 6)

- 該当: `audit_targets.cjug_d2_application_count: 7` (line 504)
- 問題: 実際は 6 件 (dropout に「D-2 適用」明示欠落)
- 修正案: F-1 修正と統合 (dropout reference に D-2 注記追加) or count を 6 に訂正

### F-4 [MEDIUM] governance_jargon ヘッダー件数不正確 (8 vs 9)

- 該当: line 279 `# Category 3: governance_jargon (8 terms)`
- 実: 9 件 (Rule D + PASS 四条 + PASS 五条 + Tier 1/2/3 + chain + gate + ack)
- 修正案: 「9 terms」に訂正

### F-5 [MEDIUM] paid_standards_referenced 主張範囲乖離 (4 vs 2)

- 該当: line 506 `paid_standards_referenced_via_alternatives: 4`
- 実: 2 件 (X 0160 + Z 8301; X 25010 / T 14971 引用ゼロ)
- 修正案: count 2 に訂正 OR JIS X 25010 を品質特性関連エントリに追加引用

### F-6 [MEDIUM] subagent カテゴリ配置 + 規格引用説明不足

- 該当: `subagent` (line 159, Category 1: process_jargon)
- 問題: subagent は AI 開発内部概念で IPA / JIS に対応語なし. JIS X 0160 §実装プロセス・役割定義引用は「規格に直接定義」と読めるとミスリーディング
- 修正案: reason に「subagent 自体は AI 開発概念で JIS / IPA に該当語なし; 訳語選定根拠として `実行担当者` 概念を借用適用」明示

### F-7 [LOW] 不採用候補 reason 妥当性薄弱

- multi-session の「多班同時実施」, kickoff 全体, cut の「版締め」(blacklist 第 1 候補だったのに不採用理由欠落), chain
- 修正案: 各エントリ不採用未言及候補について 1 文 reason 補強

### F-8 [LOW] PASS 四条 vs 五条 reference 完全重複

- 設計判断としては OK (内部 4 vs 5 の数差を納品物に出さない) だが構造冗長
- 修正案: notes で「五条が現行最新; 四条は legacy」明示

### F-9 [LOW] adopted「文脈依存」の機械 audit 扱いが未定義

- 口語 4 件 + audit_targets.required_fields_per_entry の `adopted` 項
- 修正案: `adopted_consistency_check_skip: true` meta フィールド追加 or audit_targets.notes に明記
- 影響度: LOW (Phase 0.6 audit script 実装タスク)

### F-10 [LOW] kickoff 不採用理由「カタカナ含む」記述漏れ

- カタカナ「キックオフ」自体の不採用理由 (硬約束 H-1) を冒頭で触れる方が一貫性あり

---

## 追加観察 (informational)

- **O-1 [良]** cross-batch reconciliation の透明性高 (規則 A 準拠の良い実践)
- **O-2 [良]** 臨床用語衝突 3 大警告 (dropout / drift / evidence) ★マーク統一視認性高
- **O-3 [良]** sibling pattern 統一 (writer/reviewer/subagent → 文書作成担当者/文書確認担当者/実行担当者)
- **O-4 [良]** D-7 長音符運用堅守 (ledger 「漢語のため D-7 不適用」明示)
- **O-5 [情報]** 臨床読者誤読リスク総合評価: notes 警告運用で許容レベル. ただし Excel セル単独抜粋時用に 99_用語集.xlsx で「★ 注意」列必須
- **O-6 [情報]** ICH E6(R3) / M11 / GAMP 5 / CDASH 引用ゼロは妥当. ただし 99_用語集.xlsx (Phase 0.5.8) で CDASH 活用機会あり

---

## 起草担当への質問 (clarifications needed)

### Q-1 (HIGH F-1 関連): dropout §SE 引用根拠は何か
session_B レポートには SE/DS ドメイン言及なし. SDTMIG v3.2 PDF p.130-145 は DM/SE 用例で dropout 定義頁でない. 起草担当 (Batch 2) はどの一次資料を見たか? 物理頁 vs 論理頁混同?

### Q-2 (HIGH F-2 関連): 有償 JIS §節タイトルの根拠
D-6 で「購入なし」決定済. 起草された §節名は kikakurui.com のどの URL で確認できるか? 推測で書いた場合は全件 reference 再構築必要

### Q-3 (MEDIUM F-3/F-5 関連): audit_targets.* カウント算定根拠
cjug_d2_application_count: 7 と paid_standards_referenced: 4 はどう数えたか?

---

## 結論

- **判定**: CONDITIONAL_PASS (HIGH 2 件 → PASS 不可)
- **次ステップ提言**:
  1. **即時必須 (HIGH)**: F-1 修正 (dropout §DS 訂正), F-2 対応 (有償 JIS §節名検証 or 表記緩和)
  2. **本フェーズ完了前 (MEDIUM)**: F-3, F-4, F-5 修正 (audit メタ整合) + F-6 修正 (subagent カテゴリ説明補強)
  3. **次フェーズに送り (LOW)**: F-7〜F-10
  4. **再審査**: 修正後改めて code-reviewer (異 session) で final review → PASS 移行

- **規則 A 適用観察**: 起草担当 + 統合担当が Self-PASS した状態だったが, 一次資料 PDF 実機 fetch で F-1 致命誤発見. **規則 A の N 様本独立抽検が機能した実例**

- **本審査の限界**: 有償 JIS 規格本文の §節タイトル妥当性は本 reviewer も購入していないため最終確認不可. F-2 は「無検証 = 黑」の保守的判定
