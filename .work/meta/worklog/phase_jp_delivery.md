# Phase JP Delivery (iTMS 様 納品) — 工作日志

> docs/jp/ Chain J 下的提出实绩 entries. PLAN 在 `docs/jp/PLAN.md` + EXECUTION_PLAN 在 `docs/jp/EXECUTION_PLAN.md`.

> **新 entry** append 到本文件 (按日期倒序或顺序皆可, 保持 H2 标题 `## YYYY-MM-DD <topic> <verb>` 格式).

---

## 2026-04-29 docs/jp/ Phase 1 P0 着手順 1「04 要件定義書 v1.0」PASS (post P2 B-02 batch 01 同日)

- **触発**: 用户「04 要件定義書から始めて」 — Phase 0/0.5/0.7/0.5.8 完了状態から Phase 1 起動
- **完了の作業**:
  - **STEP A 派発前テンプレ整備**: `prompts/{writer_xlsx,reviewer_xlsx,term_audit}.md` 起草 + `sources/04_要件定義書.yml` 骨格 + `glossary/research_reports/04_source_mapping_2026-04-29.md` (引用源 8 件マッピング)
  - **STEP B Round 1 並列派発**: 起草担当 (executor opus) + 用語監査機械検査機能 implementor (executor sonnet) — 起草 self-check 5/5 PASS / 機械検査機能 (audit_terms 538 行 + extract_xlsx_text 164 行) 検証 5/5 PASS
  - **STEP C 確認担当 Round 1 (code-reviewer opus, 規律 D 隔離宣言済)**: sha256 一致 + 数値突合 18/18 + Phase 番号 7/7 + ALCOA+ 4/4 + 禁止語 31/31 ゼロ + である調 100% — CONDITIONAL_PASS (HIGH 0 / MEDIUM 1 R1-F-1 C-04 範囲整合 / LOW 4 / 情報 4)
  - **STEP D Q1+Q2 修正 + 機械検査機能拡張**: audit_terms.py に exempt_files 自動除外 (`*用語集*.xlsx` 追加) + 用語写像辞書 v0.4 (ack candidates「確認」除外) — 検証 4/4 PASS
  - **STEP E 用語監査 Round 1 (document-specialist sonnet, 規律 D 隔離宣言済)**: PASS 4 verdict CONDITIONAL_PASS — A-F-1〜4 実問題 + A-F-5/6/8 false-positive + A-F-7 IT 業界標準語 (パイプライン) 判断
  - **STEP F 用語写像辞書 v0.5**: writer / drift / chain candidates から汎用日本語語 (作成者 / 差異 / 相互参照) 除外 → audit inconsistency 6 → 3 (うち 1 件 writer 改修対象 atom; 残 2 件 既知 false-positive)
  - **STEP G 起草担当 Round 2 (executor opus)**: R1-F-1 C-04 抽象化 (案 A; AI 平台固有数値完全削除) + R1-F-2 P-04 帰属短縮 + R1-F-3 NFR-01 行頁比書換 + R1-F-4 NFR-04 出典補足 + R1-F-5 NFR-03 機械可読ラベル注記 + A-F-2 atom 採用語訂正 → self-check 6/6 PASS
  - **STEP H 確認担当 Round 2 (code-reviewer opus, 規律 D 隔離宣言済)**: 全 R1 finding 5 件 + A-F-2 妥当反映確認 + regression 検査 (R2 初実施) PASS → **PASS 無条件**
  - **STEP I closure 反映**: yml v0.2 → v1.0 + revisions v1.0 + xlsx 再生成 (sha256 f8a5b049…) + `_progress.json` 04 status PASS / current_phase phase_1_in_progress (1/4 完了) + CHANGELOG ITMS-SDTM-04 v1.0 追記
- **関鍵決定**:
  - **D-r29-10 規律 D 三 type 隔離 production 検証**: writer = executor / reviewer = code-reviewer / 用語監査 = document-specialist 三 type 完全隔離 + Round 1/2 各々独立規律 D 自己宣言. METHODOLOGY §5 #2 (Author–approver separation) を実装レベルで実証
  - **D-r29-11 用語写像辞書 汎用語衝突対応 pattern**: 確認 / 作成者 / 差異 / 相互参照 = 一般日本語語が candidates 化されると mapping consistency 誤検出多発. 「adopted 強制で規律目的達成可」と判断し candidates から除外する pattern を確立 (term_mapping v0.4 + v0.5). 後段 01/02/03 でも同型パターン適用候補
  - **D-r29-12 04 要件定義書 範囲 (PLAN §0.2 整合)**: AI 平台 v1.0 リリース固有数値 (LB Test Code C65047 / 2,536 用語 / QS 系 296) は本納品物全体の根拠章 (= 04) 範囲外. KNOWN_LIMITATIONS.en.md 参照リンクで処理し抽象記述化. 案 A 採用. PLAN §0.2 Out-of-scope と整合
  - **D-r29-13 パイプライン IT 業界標準語**: METHODOLOGY「Construction pipeline」直接訳「パイプライン」を IT 業界標準語として現状維持 (auditor 推奨「処理連鎖」非採用). Phase 3 で 99_用語集.xlsx に正式登録予定 (出典 IPA / JIS X 0160)
- **Carry-over for next session**:
  - **NEXT**: docs/jp/ Phase 1 P0 着手順 2「01 基本設計書」 — 04 §3 業務 + §3 機能要件 引用継承
  - **その後**: 02 運用保守 (04 §4 非機能 / §5 制約引用) + 03 試験結果報告書 (04 §6 前提引用, 並列可) → Phase 1 P0 closure
  - **Phase 3 deferred**: パイプライン用語の 99_用語集.xlsx 正式登録
  - **PASS 五条 Open**: I-1 日方ネイティブ確認担当指名 (PLAN §6 補完事項) — 各文書 v1.0 confirmer 欄に明記
- **下一步**: commit + push (本 session 04 closure milestone)

## 2026-04-29 docs/jp/ Phase 1 P0 着手順 2「01 基本設計書 v1.0」PASS (post 04 closure 同日)

- **触発**: 用户「01 基本設計書から始めて」 — 04 PASS 直後の連続着手
- **完了の作業**:
  - **STEP A 派発前準備**: `glossary/research_reports/01_source_mapping_2026-04-29.md` 起草 (引用源 14 件 S-1〜S-14 + 公式刊行物 4 + 規格 5 = 23 件マッピング, 6 シート × 引用源対応表) + `sources/01_基本設計書.yml` 骨格 (シート構成 + headers + column_widths + プレースホルダ) + build_xlsx.py 試走 (rc=0) で構造検証
  - **STEP B 起草担当 Round 1 (executor sonnet, 規律 D 隔離宣言)**: 6 シート content / rows 充填 — 1 概要 / 2 全体構成 (4 サブシステム + Phase 7 設計済・未実装 明示) / 3 データモデル (atom_schema 9 enum + ledger_schema forward 9 / reverse 5 + RAG chunk + KG 6 nodes 7 relationships) / 4 外部 IF (CDISC 4 種 + NCI EVS Browser + AI 平台 + LiteLLM + 生成基盤) / 5 制約事項 (D-01〜D-05) / 6 参考資料 — self-check 9/9 PASS
  - **STEP C 並列派発: 確認担当 R1 (code-reviewer opus) + 用語監査 R1 (document-specialist sonnet)** — 規律 D 三役完全隔離宣言: 確認 = CONDITIONAL_PASS (HIGH 0 / MEDIUM 4 / LOW 4 / 情報 2; sha256 再現性 / chapters 章番号体系不連続性 / Claude 平台「最大」根拠不在 / 知識グラフ ノード件数情報落ち); 用語監査 = CONDITIONAL_PASS (HIGH 0 / MEDIUM 1 トレーサビリティ vs 追跡可能性 / LOW 3 false-positive 系 / mapping_proposal 5)
  - **STEP D 起草担当 Round 2 (executor sonnet, R1 とは別 instance)**: 確認 9 件 + 用語監査 1 件 = 10 件反映 (chapters 全列挙 / Claude 数値根拠 / KG count 復元 / 293 件算術整合 / §1.5 出典 4 設計理念別分割 / P3 meta.yaml 設計済・出力未実施分離 / sdtm-rag 「独立プロジェクト」/ PMDA 正式名称 / 97% inline 出典 / トレーサビリティ管理表 文書名維持) → yml v0.1 → v0.2 → self-check 12/12 PASS
  - **STEP E 主 session 整合補正 1 件 (T-01)**: writer R2 が用語監査 F-2 で「追跡可能性管理表 (文書正式名称: トレーサビリティ管理表)」と primary/secondary を反転していたため, yml §1.4 06 行を「トレーサビリティ管理表 (ITMS-SDTM-06)」primary 維持に補正 (PLAN §1 + 04 §1.4 整合). 規律 D 主旨は writer↔reviewer 自审禁止であり, 主 session の指示逸脱補正は別範疇として運用
  - **STEP F 確認担当 Round 2 (code-reviewer opus, R1 とは別 instance, 規律 D 隔離宣言)**: 11 件 (10 + T-01) 全反映確認 + 4 軸回帰検査 (04 接続 / atom_schema / ledger_schema / CDISC 数値) 差分ゼロ → **PASS 無条件** (新規 finding HIGH 0 / MEDIUM 0 / LOW 0 / 情報 2)
  - **STEP G 用語監査 機械再検査**: blacklist 0 hits / mapping consistency 1 false-positive (口語判定エントリ adopted=「文脈依存」設計上偽陽性 17 occurrences 全件正当) — 04 既知 false-positive pattern 整合
  - **STEP H closure 反映**: yml v0.2 → v1.0 + revisions v1.0 + xlsx 再生成 (31,860 bytes / sha256 12721d04050f5…ad8310cb) + revisions 内部用語クリーニング (writer / reviewer / round / だいたい 全削除 → 04 同パターン踏襲, blacklist hit 0 維持) + `_progress.json` 01 status PASS + phase_1_p0_four_docs (2/4 完了) + CHANGELOG ITMS-SDTM-01 v1.0 追記 + WORKLOG Day 1 補遺 2 + 累積知見 4 項
- **関鍵決定**:
  - **D-r29-14 三役完全隔離 round 別 instance まで徹底 = 集束パターン確立**: writer R1 / R2 別 instance + reviewer R1 / R2 別 instance + 用語監査 R1 = 5 別 subagent. 1 サイクル目 CONDITIONAL_PASS → 2 サイクル目 PASS 無条件 への集束パターン (04 + 01 で 2 連続再現). 規律 D + 規則 D の完全準拠
  - **D-r29-15 主 session 整合補正の運用範疇定義**: writer↔reviewer 自审禁止が規律 D 主旨であり, 主 session が writer の指示逸脱を補正する 1 line edit は別範疇として OK (今後同類補正を推奨手順化). T-01 が初の precedent. ただし大規模補正は writer round 3 派発に切替
  - **D-r29-16 revisions 改訂履歴も用語規律対象**: 04 で 1 件 round 既知 false-positive として PASS だったが, 01 では writer round 2 産物の v0.2 revisions 文案に writer / reviewer / round / だいたい が 6 件混入. 主 session で v0.2 + v1.0 revisions を 04 同パターンに書換え blacklist 0 hits まで圧縮. 後段 02 / 03 の writer 派発時にも revisions 文案の用語規律遵守を kickoff prompt で明示要
  - **D-r29-17 mapping consistency 偽陽性は 04 同パターンで documented PASS**: 口語判定エントリ adopted=「文脈依存」設計 (notes に「数値→約 / 範囲→概ね / 内容要約→概略として」明記) では candidates 出現が必然的に inconsistency と検出される. 04 「A-F-5/6/8 既知 false-positive」と同 pattern で documented PASS. term_mapping.yml v0.6 改訂 (口語判定エントリ candidates から「約」削除等) は Phase 3 案件
- **Carry-over for next session**:
  - **NEXT**: docs/jp/ Phase 1 P0 着手順 3-4「02 運用保守マニュアル + 03 試験結果報告書」並列起動可 — 04 §4 非機能 / §5 制約 / §6 前提 + 01 §2-§4 設計 を引用継承
  - **その後**: P1 補完 = 05 詳細設計書 単独 → P2 仕上げ = 06 / 07 / 99 + 00_README → Phase 4 Pack & Handoff
  - **Phase 3 deferred** (新規 4 件): build_xlsx.py 改修 (sha256 再現性 = openpyxl 作成日時固定化) / term_mapping.yml v0.6 改訂 (口語判定エントリ「約」削除案 + pipeline 登録 + 新規訳語 5 件 — チャンク / ノード / リレーション / ローカル先行 / 順方向・逆方向) / 99_用語集.xlsx 仕上げ時の新規訳語登録
  - **PASS 五条 Open** (継承): I-1 日方ネイティブ確認担当指名 — 各文書 v1.0 confirmer 欄に明記
- **下一步**: commit + push (本 session 01 closure milestone)

## 2026-04-30 docs/jp/ 中間版 v0.5 集約 + 提出可能状態 (Phase 1 P0 中間 milestone)

- **触发**: 用户「明白了, 是 A 这种情况 (中間版/进度汇报), 你帮我制作一下」+ 後続要望「反復記録も Excel にしてほしい + 全提交ファイル Excel 化 (公司の習慣)」 — Phase 1 P0 4 件中 2 件確定段階での中間版集約 + クラウド提出.
- **完了の作業**:
  - **STEP A 中間版補助文書 起草 第 1 弾 (07 + 旧 README md)**: yml + build_xlsx.py 経由で 07 進捗報告書.xlsx (9 シート / 19,731 bytes) + README_今回納品範囲.md 起草. audit_terms.py blacklist 機械検査で 07 に内部ファイル名引用 (`_progress.json` + `WORKLOG`) 1 件ヒット → 出典行抽象化 → hits=0 確認.
  - **STEP B 04 改訂履歴 用語規律 軽微修正**: 04 機械再検査で改訂履歴 v1.0 行に round 表記 1 件残存検出 (本文監査 PASS 後の改訂履歴シート由来) → 「第 N 回」表記置換 + xlsx 再 build (24,131 bytes 不変, sha256 f8a5b049 → 4f5c4fd6).
  - **STEP C 第 1 弾 zip 集約**: 4 件 xlsx (04 / 01 / 07 / 99) + README md + 公開発布版 ai_platforms/release/v1.0/ 全部 (.omc 除外) を `20260430_iTMS_SDTM_進捗版_v0.5.zip` に集約. 解凍テスト OK + sha256 sidecar 作成.
  - **STEP D 中間版補助文書 起草 第 2 弾 (00 + 08, 全提交ファイル Excel 化要望)**: ① 旧 README md → 00_納品範囲.xlsx に変換 (10 シート / 19,399 bytes); ② 反復実績データ調査 (AI 平台 4 種 dev/checkpoints/ + retrospectives/ + SMOKE_V4 + .work/06_deep_verification/_progress.json + docs/jp/glossary/research_reports/ + 自身 _progress.json + WORKLOG + CHANGELOG) → 08_反復実績記録.xlsx 起草 (12 シート / 27,116 bytes / 5 系統 約 50 回次相当を集約). audit_terms.py で 08 に「round 表記」再帰引用 1 件ヒット → 表記除去 → hits=0 確認.
  - **STEP E 第 2 弾 zip 再集約**: 旧 README md と古い zip / sha256 を削除し, 6 件 xlsx (00 + 01 + 04 + 07 + 08 + 99) + 公開発布版資料同梱の新パッケージ作成. 4,680,626 bytes / 130 files / sha256 0871069…d881e. 全 6 xlsx 解凍テスト OK (openpyxl 開閉成功).
  - **STEP F 用语规律監査 6/6 PASS**: 全 6 xlsx で blacklist hits=0. 修正サイクル累計 3 件適用 (07 出典内部ファイル名抽象化 + 04 round 表記置換 + 08 D-15 行再帰引用除去).
  - **STEP G 収尾**: _progress.json 更新 (interim_v0_5_submission_2026_04_30 + 04 sha256 訂正 + 00/07/08 documents 追加) + CHANGELOG (5 件追記) + WORKLOG Day 2 + .work/MANIFEST.md Chain J + docs/PROGRESS.md docs/jp 段 + .work/meta/worklog.md (本エントリ).
- **関鍵決定**:
  - **D-r30-1 中間版 v0.5 構成パターン確立**: 「確定 2 件 + 中間/補助 3 件 + 骨格 1 件 + 公開発布版資料」構成. 残工程提出までの間, 受信者からのフィードバックを残工程に反映可能とする時間バッファとして機能.
  - **D-r30-2 全提交ファイル Excel 化要望対応**: 受信者公司の習慣として md 直接投入禁止 → build_xlsx.py の text/table/links 三型シート構成で md → yml → xlsx 機械変換ライン確立. 案内 README は 00_納品範囲.xlsx として 6 シート構成に再構成. 公開発布版資料 (md) は zip 内同梱されるが既に公開済 + 受信者社内共有可能レベル + 補助案内として明示する形で容認.
  - **D-r30-3 反復実績の可視化価値**: 内部記録 (50 回次相当) を受信者向け説明資料に転換することで, 単なる「結果」ではなく「結果に至る検査・修正の規模」を訴求可能に. 08_反復実績記録.xlsx は今後類似プロジェクトでも再利用可能なテンプレート (5 系統 集約 + 7 シート + データソース注記).
  - **D-r30-4 中間版 audit の improvement 効果**: 04 改訂履歴 v1.0 行 round 表記残存は本文監査では検出不能だった (本文 audit PASS 後の改訂履歴シート由来). 中間版集約時の機械再監査が catch-net として機能する確証. 今後の中間版/正式版集約時にも全件 audit 必須 = 規律 §11.4 の運用拡大.
- **Carry-over for next session**:
  - **NEXT**: クラウド提出 ack 受領後 → Phase 1 P0 着手順 3-4「02 運用保守マニュアル + 03 試験結果報告書」並列起動 (04 §4 非機能 + §5 制約 + §6 前提 + 01 §2-§4 設計 を引用継承). 中間版に対する受信者フィードバックがあれば残工程に反映.
  - **その後**: Phase 2 (05 詳細設計書) → Phase 3 仕上げ (06 トレーサビリティ + 07 v1.0 化 + 99 中文列充填) → Phase 4 Pack & Handoff (正式版 v1.0 zip + RETROSPECTIVE.md). 予定 = 2026-05-中旬末 正式版 v1.0 提出.
  - **PASS 五条 Open** (継承): I-1 日方ネイティブ確認担当指名 — 中間版 00_納品範囲 §5.1 で受信者側に明示要望済.
- **下一步**: commit + push (本 session 中間版集約 milestone).

## 2026-05-04 docs/jp/ 内部 navigation 一致性修正

- **触发**: 用户フィードバック「汇报放眼整个项目, 不要把成果物制作过程当项目进度」→ scope を docs/jp 内部に絞り直し → 内部 navigation/version 参照ドリフト 5 件特定 + 修正.
- **修正対象**: docs/jp 内部の navigation/version 参照 (実状態に対するドリフト) — Phase / 進捗 / 産物状態は不変.
  - `00_README.md` (65→95 行) 全面刷新: 内部 / 納品 / 中間版補助 / 子目录 4 表構成. PLAN v0.3 / EXEC v0.2 / 04+01 v1.0 PASS / 中間版 v0.5 補助 (00/08/07) / 99 v0.1 骨格 / scripts (build_xlsx + audit_terms) / 子目录入口 (sources/templates/glossary/scripts/prompts/failures/assets/deliverable) を全反映. Phase 起動順 PLAN v0.3 整合.
  - `CHANGELOG.md` 時序修正: ITMS-SDTM-01 v1.0 (2026-04-29) を末尾から 04 v1.0 (4-29) と 04 用語規律修正 (4-30) の間 (L86) に移動 + 残骸 `---` separator 除去. 4-29 → 4-30 時系列に整合.
  - `PLAN.md` L16 状態行: 「Phase 0+0.5+0.7+0.5.8 完了, Phase 1 起動準備可」→「Phase 1 in_progress, 04+01 v1.0 PASS, 残 02+03; 中間版 v0.5 提出済」.
  - `EXECUTION_PLAN.md` L13-14: DRAFT v0.1 → v0.2; 上流 PLAN v0.2 → v0.3.
  - `_progress.json` references: plan v0.2 → v0.3; exec v0.1 → v0.2 (JSON parser PASS).
- **検証**: 5 ファイル個別 verify (sed/grep) + JSON load PASS + CHANGELOG ordering grep (78=04 v1.0 / 86=01 v1.0 / 95=04 用語修正 / 127=中間版 v0.5).
- **scope 限定**: project-level (`.work/MANIFEST.md` L4 / `docs/PROGRESS.md` L3) の 4.8 万 / 6.9 万字符巨行は別案 — 用户が docs/jp scope を指定したため本 session は触らず. 巨行修正は別 session で計画案を出してから実施.
- **関鍵決定**:
  - **D-r504-1 navigation 索引 ≠ progress 看板**: 00_README は内部 navigation 専用 (誰がどのファイルを見るか) → 状態列は最小限 (✅ PASS / 未着手 / v0.5 中間版); 反復・round / writer 派発回数等は worklog / _progress.json 側. 本修正で navigation と progress 看板の役割境界が明確化.
  - **D-r504-2 CHANGELOG 時序整合は単一情報源責務**: CHANGELOG は改訂履歴の single source of truth. 投入順ではなく文書発行日順 (4-29 → 4-30) に整列することで, 後続の正式版 v1.0 集約や RETROSPECTIVE 起草時に時系列引用可能.
- **Carry-over for next session**:
  - **NEXT**: 中間版 v0.5 受信者フィードバック待ち → ack 後に Phase 1 P0 着手順 3-4「02 運用保守 + 03 試験結果報告書」並列起動.
  - **別案**: project-level 巨行修正 (`docs/PROGRESS.md` L3 = 48,234 字 / `.work/MANIFEST.md` L4 = 69,438 字) — CLAUDE.md 写作規則 + 新規則「成果物制作過程 ≠ 項目進度」両方違反. 巨行内容を `.work/meta/worklog.md` に既に mirror 済か確認 → 不足なら退避先用意 → 看板側を「最後更新: 2026-05-04. Phase 状態は下方表参照.」短文に置換 + 残長行 (PROGRESS L11/102-107/171/330-337 + MANIFEST L317-328) を ≤ 200 字短指針化.
- **下一步**: commit + push (本 session docs/jp 内部一致性修正 milestone).

---

## 2026-05-08 scope 錯誤根原修正 + 読者視点クリーンアップ

- **発端**: 01_要件定義書 の scope 錯誤を Bojiang が指摘 — 「本納品物」が SDTM KB ではなく docs/jp Excel セット自体を指し、docs/jp session の作業動機が要件定義書本文に混入していた.
- **Root cause trace**: PLAN.md §0.2 in-scope の歧义 + writer が PLAN.md §0.1 (docs/jp 旁枝の存在理由) を要件定義書 §1.2 に直接適用 → 「本納品物 = Excel 7件套」という誤フレーミングが §1.2/1.4/1.5 全体に伝染.
- **修正内容 (ymls + xlsx 再生成)**:
  - `01_要件定義書.yml`: §1.2 全面改稿 (題名「本書の目的」に変更、Excel 来由説明を削除)、§1.3「本納品物→本書」、§1.4 誤フレーム削除+関連文書再構成、§1.5 誤定位修正、C-05「本納品物→本知識ベースおよび関連納品文書」.
  - `build_xlsx.py`: text-type シートで「出典:」行をすべて除去するフィルター追加 (全ファイル系統対応).
  - `01_要件定義書.yml`: §1.4 内部パス (.work/06_deep_verification/schema/) 削除、NFR-01 行頁比削除、NFR-02「処理プロセス」→「担当者」、FR-02 page_index.json 削除.
  - `02_基本設計書.yml`: IF-05 (build_xlsx.py 内部ツール) 削除、2_全体構成 §2.3 atom_id/verdict 列挙等の内部スキーマ詳細を読者向け簡略記述に置換、参考資料 .work/ パスを「内部管理リポジトリ」に変更、D-03「P0 Pilot / frozen_at / frozen_evidence」削除、§1.5(4)「本納品物→関連文書」.
  - `07_進捗報告書.xlsx` / `08_反復実績記録.xlsx`: 再生成 (build_xlsx.py フィルター適用).
- **未解決 (次 session へ)**:
  - `99_用語集.yml`: 現状は blacklist 用語マッピング (round/batch/subagent/Rule D 等) のみ収録 — 読者向け SDTM 技術用語集への完全書き直しが必要.
  - `02 §3.4/§3.5` データモデル粒度: atom_id フォーマット・verdict 列挙が基本設計書として適切か要議論.
- **検証**: 4 xlsx 全件 CLEAN (出典行・内部パス・禁止語 0 件).
- **関鍵決定**: 読者視点原則を確立 — 「制作者しか分からない内容 (出典行、内部パス、内部用語、ツール名) は xlsx に一切出力しない」. build_xlsx.py で系統的に担保.
- **下一步 route word**: `docs/jp 用語集修正` → 次 session で 99_用語集 完全書き直し + §3.4/§3.5 粒度議論.

