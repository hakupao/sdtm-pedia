# 04 要件定義書 引用源マッピング

> 作成日: 2026-04-29
> 用途: writer subagent への入力資料. 各シート content をどの源節 / 行 / 頁から起こすかの一次設計.
> 参照先: `docs/jp/sources/04_要件定義書.yml` (本マッピングを充填する yml 骨格)

---

## 0. 引用源 一覧 (実在性検証済)

| ID | パス | 用途 |
|----|------|------|
| S-1 | `METHODOLOGY.md` | 全シート 主源 |
| S-2 | `.work/00_planning/restructure_plan.md` | シート 1 / 6 |
| S-3 | `.work/00_planning/source_relationship.md` | シート 1 / 6 |
| S-4 | `.work/meta/retrospective.md` | シート 4 (NFR) |
| S-5 | `docs/jp/PLAN.md` | シート 1 / 5 (本納品物自身の制約) |
| S-6 | `DISCLAIMER.md` | シート 5 (著作権) |
| S-7 | `ai_platforms/release/v1.0/KNOWN_LIMITATIONS.en.md` | シート 5 |
| S-8 | `.work/03_verification/issues_found.md` | シート 4 補強 (Issue 2 NCR-002 直接出典) |

writer は派発時に各 S-X を `test -f` で実在確認すること.

---

## 1. シート別 引用源対応

### シート 1 (1_背景目的)

| 小節 | 源 | 抜粋ヒント | 文体目標 |
|------|-----|-----------|---------|
| 1.1 知識ベースの存在意義 | S-1 Purpose + Compliance framing | 「The knowledge base derives from CDISC SDTM publications mandated by the U.S. Food and Drug Administration, recognized by the Japanese Pharmaceuticals and Medical Devices Agency, and accepted by the European Medicines Agency …」 | 結論先行 + 規制機関名は日本語表記で省略せず |
| 1.2 本納品物の目的 | S-5 §0.1 | 「本プロジェクト (SDTM 知識ベース + 検証エビデンス) を **iTMS 様** が違和感なく受け取り…」 (内部用語「エビデンス」は使用禁止 → 「証跡」で言換) | 受信者明示 + 形式選択の理由 (Excel 主体) を 1 文 |
| 1.3 想定読者 | S-5 §0 受信者欄 | 「IT + 医療データ両分野の知見ある想定読者」 | 1-2 文で十分 |
| 1.4 関連文書一覧 | S-5 §1 | 7 文書 + 99_用語集 = 8 件. 各 1 行で役割記述 | 表形式ではなく箇条書き (本シートは text 型) |
| 1.5 本書の位置付け | S-5 §1 v0.3 改訂注記 | 「04 要件定義書 を P0 に格上げ」「後段 3 文書 (01 / 02 / 03) すべての根拠章になる」 | 1-2 文 |

### シート 2 (2_業務要件)

| 小節 | 源 | 抜粋ヒント | 文体目標 |
|------|-----|-----------|---------|
| 2.1 業務シナリオ | S-1 §6 first bullet | 「working reference for SDTM data programming, mapping review, and SDTM training」→ 「SDTM データプログラミング, マッピング品質確認, SDTM 教育」 | 3 用途を明確化 |
| 2.2 一次資料対応 | S-1 §1 Table | 4 行表 (種別 / 版数 / 範囲). 本シートは text 型なので文章化 | 数値はそのまま (461 頁 / 74 頁 / 1,917 変数 / 1,005 codelist / 37,939 用語) |
| 2.3 業務的限界 | S-1 §6 last 2 bullets | 「21 CFR Part 11 / PMDA-grade 電子記録の代替ではない」「規制提出時は CDISC 公式刊行物が権威源」 | 二重否定回避 |

### シート 3 (3_機能要件)

| ID | 源節 | 主機能 | 主要産物 |
|----|------|--------|---------|
| FR-01 | S-1 §2 Phase 1 | xlsx → spec.md 自動変換 | 63 ドメイン spec.md + 用語索引 |
| FR-02 | S-1 §2 Phase 2 | PDF ページ索引化 (プログラム実行) | page_index.json |
| FR-03 | S-1 §2 Phase 3 | PDF からの AI 補助抽出 (11 ロット 各内検証付) | 各ドメイン assumptions.md / examples.md |
| FR-04 | S-1 §2 Phase 4 | 補完抽出 (モデル + 章レベル) | 6 モデル文書 + 6 章文書 |
| FR-05 | S-1 §2 Phase 5 | 全件確認 + 索引化 | INDEX.md + 確認報告 |
| FR-06 | S-1 §2 Phase 6 | 検索最適化 (経路層 + 逆引き) | ROUTING.md + VARIABLE_INDEX.md (1,523 変数) |
| FR-07 | S-1 §2 Phase 6.5 | AI 平台展開 | 4 平台向け配布物 |
| FR-08 | S-1 §3 第 1 段落 | ドメイン回答追跡 (4 step 手順) | spec.md / assumptions.md / examples.md |
| FR-09 | S-1 §3 第 2 段落 | 章節回答追跡 | knowledge_base/chapters/chXX_*.md |
| FR-10 | S-1 §3 第 3 段落 | 受控用語追跡 (C-code) | knowledge_base/terminology/ |
| FR-11 | S-1 §2 末尾段落 | 字面級確認の継続実施 | .work/06_deep_verification/evidence/checkpoints/ (97% 範囲, 進行中) |

writer 注: 各行の「要件項目」列は 4-12 字程度の名詞句. 「要件内容」列は 1-2 文で要件を述べる (である調).

### シート 4 (4_非機能要件)

| ID | 観点 | 源 | 抜粋ヒント |
|----|------|-----|-----------|
| NFR-01 | 定量合格判定基準 | S-1 §5 #1 + S-4 §4 規則 1 | 「覆盖率 ≥ 95% / 占位マーカー 0 / 行頁比 ≈15-20 行/頁」(S-4 §4 規則 1 の数値定義をそのまま採用) |
| NFR-02 | 作成者・確認者分離 | S-1 §5 #2 + S-4 §4 規則 2 | 「The agent or process that authored a file may not approve it」→ である調訳 |
| NFR-03 | AI 推測値の明示 | S-1 §5 #3 + S-4 §4 規則 3 | 「`(estimated)` ラベル / 権威索引から除外」 |
| NFR-04 | 各工程閉幕の無作為抽出確認 | S-1 §5 #4 + S-4 §4 規則 4 | 「事後是正ではなく工程閉幕時に組込む」 |
| NFR-05 | 追跡可能性 | S-1 §3 + §6 first bullet | 「任意の主張を一次資料に数秒で照合できる構造」 |
| NFR-06 | GAMP 5 / ALCOA+ 整合 | S-1 Compliance framing | 「risk-based verification approach informed by GAMP 5 (ISPE) — declared specification, executed verification, independent review, …」+ 「formal categorization or certification は取得しない旨」明示 |

writer 注: ALCOA+ 列は S-1 §5 表の対応次元をそのまま転記.

### シート 5 (5_制約条件)

| ID | 種別 | 源 | 抜粋ヒント |
|----|------|-----|-----------|
| C-01 | 規格優先性 | S-1 §6 last bullet | 「Where this knowledge base and the official publication appear to differ, the official publication governs」 |
| C-02 | 規制範囲外 | S-1 §6 second bullet | 「not itself a 21 CFR Part 11 / PMDA-grade electronic record」 |
| C-03 | 著作権 | S-1 §1 末尾 + S-6 | 「CDISC retains copyright. The original publications are not redistributed」 |
| C-04 | 既知の限界 | S-7 + S-1 §4 Standing limitations | 「large codelists stored as stubs / 外部実時間検索 embed なし」 |
| C-05 | 機密区分 | S-5 §10 H-4 | 「公開可レベル (CDISC 規格自体が public)」 |

### シート 6 (6_前提条件)

| ID | 種別 | 源 | 抜粋ヒント |
|----|------|-----|-----------|
| P-01 | 一次資料 | S-1 §1 Table | 4 種公式刊行物 (SDTMIG v3.4 PDF / SDTM Model v2.0 PDF / SDTMIG xlsx / Controlled Terminology xlsx) を読者が必要に応じ参照可能 |
| P-02 | 読者背景 | S-5 §0 受信者欄 | IT + 医療データ両分野の知見 |
| P-03 | 概念整理 | S-2 §二 | SDTMIG v3.4 = implementation; SDTM v2.0 = model. 前者は後者を読了している前提で書かれる |
| P-04 | 受控用語 | S-1 §3 第 3 段落 | C-code 体系 (例: C66731) と NCI EVS Browser 照合可能性 |
| P-05 | 検証証跡保管 | S-1 §2 末尾 | 「.work/06_deep_verification/evidence/checkpoints/」 (内部パス開示は範囲外, 「監査可能形式で保管されている」と抽象化) |

---

## 2. 用語規律ヒント (writer 派発前 注入)

writer は本マッピング + `term_mapping.yml` を併読し以下を厳守:

| 源原文 (英語) | 採用語 (term_mapping.yml) | 出典規格 |
|---------------|--------------------------|----------|
| evidence | 証跡 | 業界慣行 (規律 H-1) |
| atom (内部用語) | 検証単位 | CJUG 公式訳なし; CDISC SDTM「オブザベーション」と別概念 (term_mapping.yml notes) |
| ledger (内部用語) | 管理表 | (mapping 参照) |
| round (内部用語) | フェーズ | (mapping 参照) |
| author / approver | 作成者 / 承認者 | METHODOLOGY.md 自身 |
| traceability | 追跡可能性 | JIS X 0160 |
| placeholder | 占位マーカー | (規律 H-1) |
| coverage ratio | 覆盖率 (本書では「網羅率」も検討余地; 用語監査担当に確認要請) | (mapping 参照) |

**注意**: writer が新規導入する訳語があれば term_audit subagent への提案として記録 (本書 §3 mapping 提案候補).

---

## 3. mapping 提案候補 (writer → audit に申送り想定)

| 用語 (英語 / 内部) | 本書での仮採用 | 候補別案 | 監査依頼内容 |
|--------------------|---------------|---------|-------------|
| coverage ratio | 覆盖率 | 網羅率 / カバー率 | JIS X 25010 / GAMP 5 で出典が確認できる方の採用 |
| risk-based verification | リスク主導検証 | リスクベース検証 | GAMP 5 公式日本語の確認要 |
| audit trail | 監査追跡 | 監査証跡 | PMDA ER/ES 指針の用語確認 |

writer はこの候補について audit subagent から指示が来る前提で yml 内に該当語を使う場合は 1 候補に統一して記録.

---

## 4. 抜粋禁止事項

writer は以下を yml に転記しないこと:

- METHODOLOGY.md 内の固有名詞 (例: 「FDA」「PMDA」「EMA」) は規制機関名としてはそのまま使えるが, 内部 commit hash / GitHub URL / 著者名は除外
- `.work/06_deep_verification/_progress.json` の round 番号 / batch 番号 (内部用語規律違反)
- `.work/03_verification/issues_found.md` の Issue 番号や fix commit リンク (規律 H-1: 開発内部識別子)
- 開発担当者の個人名 (規律 H-4: 作成者個人情報含めない)

ただし以下は OK:
- 公式刊行物の版番号 / 頁番号
- 規格名 (GAMP 5 / ICH E6(R3) / ALCOA+ 等)
- 標準訳の用語

---

## 5. writer self-check 補強

writer は産物提出前に本マッピング §1 の各シート ID 行を逐行に対応させた充足表を実行記録に必須含める. 対応欠落あれば自己 FAIL.

---

## 履歴

- v0.1 (2026-04-29): 初版. 04 要件定義書 writer 派発前.
