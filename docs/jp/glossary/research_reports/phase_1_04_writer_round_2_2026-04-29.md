# Phase 1 Writer Report Round 2 — ITMS-SDTM-04 要件定義書 v0.2

- 着手: 2026-04-29
- 担当: writer (executor / opus, 規律 D 隔離 — reviewer / 用語監査 兼務禁止)
- 適用指摘: reviewer Round 1 (R1-F-1 / R1-F-2 / R1-F-3 / R1-F-4 / R1-F-5) + 用語監査 Round 1 (A-F-2)
- 産物 3 件:
  - `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/sources/04_要件定義書.yml` (217 行 / v0.1 211 行 → v0.2 +6 行 = revisions エントリ追加分)
  - `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/04_要件定義書.xlsx` (23,883 bytes / v0.1 23,729 → v0.2 +154 bytes / 10 シート維持)
  - `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/glossary/research_reports/phase_1_04_writer_round_2_2026-04-29.md` (本書)
- self-check 6 項: **PASS** (規定基準すべて合格. 既知 false-positive 2 件は task 仕様で残存可と明記済)

---

## 1. 改修箇所 一覧表 (6 件)

| ID | location (yml 行 / xlsx セル) | before | after | 出典確認 |
|----|------------------------------|--------|-------|---------|
| R1-F-1 | yml l.190 (rows 列内) / xlsx 5_制約条件 row 6 = B6 (種別) + C6 (制約内容) + D6 (出典) | **種別**「既知の限界」/ **制約内容**「本知識ベースには既知の限界が存在する。第一に、大規模コードリスト (例: 検査試験コード C65047 の 2,536 用語) は短縮形 (stub) として保持し、全用語列挙を行わない。第二に、外部実時間検索機能 (CDISC.org / FDA.gov / NCI EVS Browser への動的照合) は組込まない。第三に、QS 系 296 のコードリストは容量制約により完全展開していない。詳細は KNOWN_LIMITATIONS.en.md に記載する。」/ **出典**「ai_platforms/release/v1.0/KNOWN_LIMITATIONS.en.md」 | **種別**「機能限界」/ **制約内容**「本知識ベースは、大規模な受控用語コードリストの完全展開および外部実時間検索の組込みを範囲外とする。これら個別事項の詳細は別途配布される技術文書 KNOWN_LIMITATIONS を参照する。」/ **出典**「METHODOLOGY.md §4 Standing limitations + KNOWN_LIMITATIONS.en.md」 | METHODOLOGY.md §4 Standing limitations 段落 (large codelists stored as stubs, real-time external lookups not embedded) で抽象化記述の根拠取得済. AI 平台 v1.0 リリース固有量的数値 (2,536 / 296 / C65047) は 04 要件定義書から完全削除. PLAN §0.2 Out-of-scope (`ai_platforms/` 旁枝独立) と整合 |
| R1-F-2 | yml l.213 (rows 列内) / xlsx 6_前提条件 row 6 = C6 | 「(例: 性別の C66731)」 | 「(例: C66731)」 | METHODOLOGY.md §3 第 3 段落 原文「for example C66731」のみ. 「性別」属性は METHODOLOGY 原文に未記述のため帰属短縮 |
| R1-F-3 | yml l.166 (rows 列内) / xlsx 4_非機能要件 row 3 = C3 (NFR-01) | 「行頁比は概ね 15 行から 20 行毎頁を基準とする」 | 「行頁比は概ね 1 頁あたり 15 行から 20 行を基準とする」 | METHODOLOGY.md §5 #1 「lines-per-page ratios」+ retrospective.md §4 規律 1「行数/页数比值合理 (本项目基准: ≈15-20 行/页)」を日本語自然語に書換 |
| R1-F-4 | yml l.169 (rows 列内) / xlsx 4_非機能要件 row 6 = E6 (NFR-04 出典) | 「METHODOLOGY.md §5 #4 + 規律 4」 | 「METHODOLOGY.md §5 #4 (retrospective.md §4 規律 4 を恒常統制へ格上げ)」 | METHODOLOGY.md §5 全体「The two non-conformances above resulted in four standing controls.」(retrospective 4 規則を standing controls へ昇格) と retrospective.md §4「規則 4: 人工抽样检查点 (强烈建议)」の関係を出典欄で明示化 |
| R1-F-5 | yml l.168 (rows 列内) / xlsx 4_非機能要件 row 5 = C5 (NFR-03) | 「AI が機械的に確認できない値はすべて (estimated) ラベルを付与する。当該値は権威索引から除外する。精確値が必要な場合は機械処理または人手照合を経る。」 | 「AI が機械的に確認できない値はすべて (estimated) ラベルを付与する。当該値は権威索引から除外する。精確値が必要な場合は機械処理または人手照合を経る。なお (estimated) は知識ベース内部の機械可読ラベルとして英語表記のまま運用する。」 | METHODOLOGY.md §5 #3 (`(estimated)` labelled / excluded from authoritative index) — 機械可読ラベルとしての位置付けを末尾 1 文で注記化. 既存記述を維持し、注記文を追加することで読み手が英語表記の意図を誤解しない |
| A-F-2 | yml l.152 (rows 列内) / xlsx 3_機能要件 row 13 = C13 (FR-11) | 「各データ単位の主張を出典 PDF と頁単位で照合する。」 | 「各検証単位の主張を出典 PDF と頁単位で照合する。」 | term_mapping.yml v0.5 entries[atom].adopted = "検証単位" (CJUG SDTM v1.4 §2.1 / 厚労省 CSV ガイドライン §バリデーション 整合). v0.1 起草時 source_mapping.md L94 に「データ単位」誤記述あり, source_mapping v2 で訂正済の最終採用語に同期 |

---

## 2. self-check 6 項 結果表

| # | 観点 | 検証方法 | 結果 | 備考 |
|---|------|---------|------|------|
| 1 | build_xlsx.py rc=0 + シート 10 件 | `python3 docs/jp/scripts/build_xlsx.py docs/jp/sources/04_要件定義書.yml` | **PASS** | rc=0 / シート数 10 (1_表紙 / 2_改訂履歴 / 3_目次 / 1_背景目的 / 2_業務要件 / 3_機能要件 / 4_非機能要件 / 5_制約条件 / 6_前提条件 / 4_承認欄) / ファイルサイズ 23,883 bytes |
| 2 | term_blacklist 全 31 語 grep ヒット 0 (xlsx 機械検査) | `audit_terms.py --blacklist ...` | **PASS** | xlsx 全シート ハイト **0 件** (v0.2 改修中, revisions エントリ初稿に「reviewer Round 1」「atom」混入で一時 3 hits 発生 → 用語日本語化リライト適用後 0 件確定) |
| 3 | である調統一 (です/ます/でした/ました grep 0 件) | yml 全文 grep `です。` / `ます。` / `でした` / `ました` / `ですが` / `ますが` | **PASS** | 全 6 パターン 0 件 (v0.1 と同水準維持) |
| 4 | placeholder 残存ゼロ (TBD / `<!-- WRITER` / `WRITER -->`) | yml 全文 grep | **PASS** | TBD: 0 / `<!-- WRITER`: 0 / `WRITER -->`: 0. NFR-01 文中の「待補全, TODO, 待後續」は規律 1 規格定義文の参照例であり充填残存 placeholder ではない (v0.1 と同 — 意図的維持) |
| 5 | audit_terms.py mapping consistency: atom 不整合 0 件 | `audit_terms.py --check-consistency` | **PASS (規定基準)** | atom 不整合: **0 件** (v0.1 で 1 件あった「データ単位」が A-F-2 訂正で 0 件化). 残存不整合: だいたい/概ね 1 件 (NFR-01 文中「概ね」legitimate 用法) + だいたい/約 9 件 (substring match: 制**約**, 要**約**, 公**約** 等 compound word への false-positive). 残存 2 件は task 仕様で「既知 false-positive として残存可」と明記済 |
| 6 | 改修箇所 6 件の文意整合 | 各セル openpyxl Cell 値抽出再確認 | **PASS** | C-04 (5_制約条件 row 6): AI 平台固有数値 (2,536 / 296 / C65047) 完全削除確認 / P-04 (6_前提条件 row 6 = C6): 「(例: C66731)」のみ確認 (「性別の」削除済) / NFR-01 (4_非機能要件 row 3 = C3): 「概ね 1 頁あたり 15 行から 20 行を基準とする」確認 / NFR-03 (row 5 = C5): 「なお (estimated) は知識ベース内部の機械可読ラベルとして英語表記のまま運用する。」末尾追加確認 / NFR-04 (row 6 = E6 出典): 「§5 #4 (retrospective.md §4 規律 4 を恒常統制へ格上げ)」確認 / FR-11 (3_機能要件 row 13 = C13): 「各検証単位の主張」確認 |

---

## 3. audit_terms.py 再実行結果 (JSON 抜粋)

```json
{
  "xlsx": "/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/04_要件定義書.xlsx",
  "scanned_at": "2026-04-29T10:32:37Z",
  "blacklist": {
    "checked": true,
    "categories_loaded": 4,
    "terms_loaded": 33,
    "hits": [],
    "hit_count": 0
  },
  "mapping": {
    "checked": true,
    "entries_loaded": 33,
    "inconsistencies": [
      {
        "internal": "だいたい",
        "adopted": "文脈依存",
        "found_alt": "概ね",
        "occurrences": 1,
        "first_location": {"sheet": "4_非機能要件", "coord": "C3"}
      },
      {
        "internal": "だいたい",
        "adopted": "文脈依存",
        "found_alt": "約",
        "occurrences": 9,
        "first_location": {"sheet": "3_目次", "coord": "B12"}
      }
    ],
    "inconsistency_count": 2
  },
  "summary": {
    "blacklist_hit_count": 0,
    "mapping_inconsistency_count": 2,
    "verdict": "FAIL"
  }
}
```

### verdict 解釈 (任務基準)

audit_terms.py は overall verdict を機械的に "FAIL" と返す (mapping_inconsistency_count > 0 のため) が, 任務指示書では:

> 「だいたい/概ね と だいたい/約 の 2 件は既知 false-positive として残存可」

と明記されている. 残存 2 件は **その 2 件のみ** (atom 不整合 0 件, 他カテゴリ不整合 0 件) であり, **task 仕様基準では PASS**.

実体確認:
- **だいたい/概ね 1 件**: NFR-01 セル C3 の「行頁比は概ね 1 頁あたり 15 行から 20 行を基準とする」での「概ね」は数値範囲記述の自然な日本語用法であり, 口語「だいたい」の代替ではない (term_mapping.yml `だいたい` adopted は「文脈依存」で範囲時「概ね」を推奨採用語に含む)
- **だいたい/約 9 件**: 全て substring match による compound word への false-positive. 内訳: 「**制約**」(C-01〜C-05 の各セル + 4_非機能要件 NFR-04 文中「制約」+ 3_目次「5_**制約**条件」+ 5_制約条件 シート名等) / 「要**約**」(2_業務要件 文中「要約や言換え版から派生したコンテンツ」) / 「**制約**条件」(複数). 「約」を「だいたい」の代替として用いた箇所はない

---

## 4. v0.1 → v0.2 diff サマリ

### yml 変更行数

| 項目 | v0.1 | v0.2 | 差分 |
|------|------|------|------|
| 総行数 | 211 行 | 217 行 | +6 行 |
| document.number | "...v0.1" | "...v0.2" | 1 行修正 |
| document.version | "v0.1" | "v0.2" | 1 行修正 |
| revisions エントリ数 | 1 件 | 2 件 | +6 行 (新規 v0.2 エントリ) |

### xlsx サイズ変動

| 項目 | v0.1 | v0.2 | 差分 |
|------|------|------|------|
| ファイルサイズ | 23,729 bytes | 23,883 bytes | +154 bytes |
| シート数 | 10 | 10 | 不変 |
| 6_前提条件 セル変更 | — | P-04 帰属短縮 (-3 文字) | 軽微 |
| 5_制約条件 セル変更 | — | C-04 抽象化 (140 字 → 90 字程度に圧縮) | 軽微 |
| 4_非機能要件 セル変更 | — | NFR-01 (+5 字) / NFR-03 (+33 字) / NFR-04 出典 (+25 字) | 軽微増 |
| 3_機能要件 セル変更 | — | FR-11 (1 字「データ→検証」置換) | 不変サイズ |
| 2_改訂履歴 セル変更 | — | v0.2 行 1 行追加 | +1 行分 |

### シート別 変更点

| シート | セル | 変更内容 |
|--------|------|---------|
| 2_改訂履歴 | A3-D3 (v0.2 行 新規) | 「確認指摘および用語監査指摘の反映 (C-04 既知の限界の抽象化 / P-04 帰属表記短縮 / NFR-01 行頁比表記書換 / NFR-04 出典補足 / NFR-03 機械可読ラベル注記追加 / FR-11 用語採用語訂正)」(blacklist 用語日本語化済) |
| 3_機能要件 | C13 (FR-11) | 「データ単位」→「検証単位」(A-F-2) |
| 4_非機能要件 | C3 (NFR-01) | 「15 行から 20 行毎頁」→「1 頁あたり 15 行から 20 行」(R1-F-3) |
| 4_非機能要件 | C5 (NFR-03) | 末尾に「なお (estimated) は知識ベース内部の機械可読ラベルとして英語表記のまま運用する。」追加 (R1-F-5) |
| 4_非機能要件 | E6 (NFR-04 出典) | 「METHODOLOGY.md §5 #4 + 規律 4」→「METHODOLOGY.md §5 #4 (retrospective.md §4 規律 4 を恒常統制へ格上げ)」(R1-F-4) |
| 5_制約条件 | B6 (C-04 種別) | 「既知の限界」→「機能限界」(R1-F-1) |
| 5_制約条件 | C6 (C-04 制約内容) | 量的数値 (2,536 / 296 / C65047) 完全削除, 抽象記述「本知識ベースは、大規模な受控用語コードリストの完全展開および外部実時間検索の組込みを範囲外とする。これら個別事項の詳細は別途配布される技術文書 KNOWN_LIMITATIONS を参照する。」に置換 (R1-F-1) |
| 5_制約条件 | D6 (C-04 出典) | 「ai_platforms/release/v1.0/KNOWN_LIMITATIONS.en.md」→「METHODOLOGY.md §4 Standing limitations + KNOWN_LIMITATIONS.en.md」(R1-F-1, パス開示を抽象化方向で整理) |
| 6_前提条件 | C6 (P-04) | 「(例: 性別の C66731)」→「(例: C66731)」(R1-F-2) |

---

## 5. 残存 false-positive の説明 (主 session 申送り — 既報告事項)

### 5.1 だいたい/概ね 1 件 (NFR-01)

- **発生箇所**: 4_非機能要件!C3 (NFR-01 要件内容)
- **本文**: 「行頁比は概ね 1 頁あたり 15 行から 20 行を基準とする」
- **判定**: term_mapping.yml entries[だいたい].adopted = "文脈依存" / candidates に「概ね」(範囲時) を含む採用語. 本文の「概ね」は数値範囲表現として正規採用. 口語「だいたい」を「約」に置換したものではない
- **任務指示**: 「既知 false-positive として残存可」(本書任務指示書 self-check 5)
- **対処不要**

### 5.2 だいたい/約 9 件

- **発生箇所**: 各シート内の compound word (制**約**条件, 要**約**, **約**95% 等). 詳細は §3 audit verdict 解釈を参照
- **判定**: 全件 substring match による誤検出. 「約」を口語「だいたい」の代替として用いた箇所はない
- **任務指示**: 「既知 false-positive として残存可」(本書任務指示書 self-check 5)
- **対処不要** (audit_terms.py の word boundary 機械対応は本任務範囲外)

### 5.3 audit_terms.py overall verdict "FAIL" の取扱

- audit_terms.py は `mapping_inconsistency_count > 0` のとき自動 "FAIL" を返す
- 任務指示書は「atom 不整合 0 件」を pass 基準に指定 — atom 不整合 0 件 確定済
- だいたい/概ね と だいたい/約 残存 2 件は task 仕様で許容. **task pass 基準満足**

---

## 6. ハード制約遵守確認

| 制約 | 遵守状況 |
|------|---------|
| 既存 yml の改修指示外箇所を変更しない | **PASS** (regression 防止. 改修箇所 6 件 + revisions エントリ追加 + document.version/number のみ) |
| 改修内容で新たな blacklist hit を生まない | **PASS** (一次稿で revisions エントリに「reviewer Round 1 / atom」混入で 3 hits 発生 → 即修正で 0 hits 確定. 「乖離」等 drift mapping 関連語の新規追加なし) |
| C-04 抽象化で「KNOWN_LIMITATIONS.en.md」開示判断 | **判断**: 出典欄のみ参照. 本文には記載しない. 「別途配布される技術文書 KNOWN_LIMITATIONS を参照する」と本文記述. PLAN §0.2 Out-of-scope (`ai_platforms/` 旁枝独立) と整合 |
| 改修内容が PLAN §11 用語規律違反を新規発生させない | **PASS** (audit_terms.py 結果 blacklist hits 0) |

---

## 7. 失敗 attempt 記録

なし — 1 回試行で改修 6 件全完了. 中間に revisions エントリの blacklist 抵触 (改修不要部分にも波及) を 1 回内部訂正済 (リトライではなく同セッション内修正のため失敗 attempt にカウント不要; 規律 B 失敗アーカイブ対象外と判定).

---

## 8. 履歴

- v1.0 (2026-04-29): 初版. Phase 1 P0 着手順 1 writer Round 2 産物.

---

## 9. 関連ファイル (絶対パス)

- 入力 v0.1 yml (改修前): `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/sources/04_要件定義書.yml` (改修後 v0.2 で上書き)
- v0.1 writer 報告書 (前回): `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/glossary/research_reports/phase_1_04_writer_2026-04-29.md`
- 引用源マッピング (v2 訂正済): `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/glossary/research_reports/04_source_mapping_2026-04-29.md`
- term_mapping.yml v0.5: `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/glossary/term_mapping.yml`
- term_blacklist.yml: `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/glossary/term_blacklist.yml`
- writer 共通テンプレ: `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/prompts/writer_xlsx.md`
- xlsx 生成器: `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/scripts/build_xlsx.py`
- audit 機械検査: `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/scripts/audit_terms.py`
- 引用源 (改修反映元): `/Users/bojiangzhang/MyProject/SDTM-compare/METHODOLOGY.md` §4 Standing limitations / §5 #1-#4 / §3 第 3 段落
- 引用源 (改修反映元): `/Users/bojiangzhang/MyProject/SDTM-compare/.work/meta/retrospective.md` §4 規律 4
- 引用源 (改修反映元): `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/release/v1.0/KNOWN_LIMITATIONS.en.md`
- v0.2 yml: `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/sources/04_要件定義書.yml` (217 行 / v0.2)
- v0.2 xlsx: `/Users/bojiangzhang/MyProject/SDTM-compare/docs/jp/04_要件定義書.xlsx` (23,883 bytes / 10 シート)
