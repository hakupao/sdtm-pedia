# docs/jp/ 改訂履歴 (CHANGELOG)

> 本ファイルは `docs/jp/` 配下の全納品物 (.xlsx) + 内部文書 (PLAN / EXECUTION_PLAN) の改訂履歴を一元管理する.
> 各 .xlsx の「改訂履歴」シートにも同内容を転記する (両方更新が原則).

## 形式

```
## ITMS-SDTM-NN vX.Y (YYYY-MM-DD)
- 改訂区分: 新規作成 / 内容修正 / 形式修正 / 用語変更 / 構造変更
- 改訂内容: (箇条書き)
- 作成: (担当)
- 確認: (担当)
- 承認: (担当)
```

文書番号一覧:
- `ITMS-SDTM-PLAN` — 計画書 (内部用, PLAN.md)
- `ITMS-SDTM-EXEC` — 実行計画書 (内部用, EXECUTION_PLAN.md)
- `ITMS-SDTM-00` — 納品範囲案内 (中間版以降 同梱)
- `ITMS-SDTM-01` — 基本設計書
- `ITMS-SDTM-02` — 運用・保守マニュアル
- `ITMS-SDTM-03` — テスト結果報告書
- `ITMS-SDTM-04` — 要件定義書
- `ITMS-SDTM-05` — 詳細設計書
- `ITMS-SDTM-06` — トレーサビリティ管理表
- `ITMS-SDTM-07` — 進捗報告書
- `ITMS-SDTM-08` — 反復実績記録 (中間版 補助)
- `ITMS-SDTM-99` — 用語集

---

## ITMS-SDTM-PLAN v0.1 (2026-04-29)
- 改訂区分: 新規作成
- 改訂内容: 初版起草. 受信者 / 範囲 / 文書一覧 / 形式約定 / Phase 計画 / PASS 条件.
- 作成: 主 session (Bojiang 指示)
- 確認: pending
- 承認: pending

## ITMS-SDTM-PLAN v0.2 (2026-04-29)
- 改訂区分: 構造変更
- 改訂内容: 受信者 iTMS 確定 / 納品形式 Excel 主体 / §10 制約条件 + §11 用語規律 (黑名单 + 写像辞書 + 双重規格参照) 追加 / Phase 0.5 用語調研 + Phase 0.7 Excel 基盤 を Phase 計画に追加.
- 作成: 主 session
- 確認: pending
- 承認: pending

## ITMS-SDTM-EXEC v0.1 (2026-04-29)
- 改訂区分: 新規作成
- 改訂内容: 落地方案 + agent 调度設計 (HOW). Agent 配役表 / 並列度 / Phase ごとの派発計画 (🔀 / 📡 / ➡️ / ⚠️ マーカー) / プロンプトテンプレ / エスカレーション / コンテキスト予算 / 検証スクリプト / 並列効果サマリ.
- 作成: 主 session (Bojiang 指示)
- 確認: pending
- 承認: pending

## ITMS-SDTM-PLAN v0.3 (2026-04-29)
- 改訂区分: 構造変更 (優先度再設計)
- 改訂内容: §1 で 04 要件定義書 を P1 → **P0** に格上げ. 着手順を 04 → 01 → 02 → 03 → 05 → 06 → 07 と確定. §5 Phase 1 を「P0 三点セット」→「P0 四点セット (2.5-3.5 日)」に, Phase 2 を「P1 補完」→「05 詳細設計書のみ (1 日)」に再分割. 工程順序 (要件 → 基本設計 → 運用 → 試験 → 詳細設計 → 進捗 → 横断) と一致させ, 後段 3 文書 (01/02/03) が 04 の節を引用できるよう設計.
- 作成: 主 session (Bojiang 指示)
- 確認: pending
- 承認: pending

## term_mapping.yml v0.4 (2026-04-29)
- 改訂区分: 用語変更
- 改訂内容: ack エントリの candidates から「確認」除外. reason 欄に汎用語衝突理由を追記.
- 作成: Phase 1 04 要件定義書 着手時の検証で発覚した審査担当による mapping consistency 誤検出への対応.

## term_mapping.yml v0.5 (2026-04-29)
- 改訂区分: 用語変更
- 改訂内容: writer エントリの candidates から「作成者」, drift エントリから「差異」, chain エントリから「相互参照」を除外. adopted 値および notes は不変. 汎用日本語衝突による誤検出 3 件への対応.
- 作成: Phase 1 04 要件定義書 用語監査担当 round 1 指摘 (A-F-1 / A-F-3 / A-F-4) を統合した対応.

## ITMS-SDTM-EXEC v0.2 (2026-04-29)
- 改訂区分: 内容修正 (PLAN v0.3 同期)
- 改訂内容: §3 Phase 1 のスケジュールを「Day 1 = 04 直列 → Day 1 後半/Day 2 = 01 直列 → Day 3 = 02 + 03 並列 → Day 4 = 用語監査 並列」に更新. §3 Phase 2 を 05 単独 1 日構成に縮小. §8 並列効果サマリの所要工数を P0 四点換算 (5/3.5/2.5 日) + Phase 2 圧縮 (1.5/1/0.7 日) で再算出.
- 作成: 主 session
- 確認: pending
- 承認: pending

## ITMS-SDTM-04 v1.0 (2026-04-29)
- 改訂区分: 新規作成
- 改訂内容: 要件定義書 初版受信者納品候補確定. Phase 1 P0 着手順 1 として起草. 起草 (writer round 1) → 確認担当指摘反映 (writer round 2) → 独立確認担当 round 2 PASS 無条件 → 用語監査 round 1 指摘 4 件実体修正 (mapping v0.5 + writer v0.2 反映) + 1 件 IT 業界標準語として現状維持 (Phase 3 用語集登録予定) → 用户口頭承認の経路で 2026-04-29 に v1.0 確定.
- 産物: docs/jp/sources/04_要件定義書.yml (217 行) + docs/jp/04_要件定義書.xlsx (10 シート).
- 作成: Phase 1 P0 着手順 1 (主 session 統括 + executor / code-reviewer / document-specialist subagent 3 種並列).
- 確認: 日方ネイティブ確認担当指名待ち (PLAN §6 PASS 五条 補完事項).
- 承認: Bojiang Zhang (用户).

## ITMS-SDTM-04 v1.0 用語規律 軽微修正 (2026-04-30)
- 改訂区分: 用語変更 (本文影響なし — 改訂履歴シートの内部用語表記のみ)
- 改訂内容: 改訂履歴 v1.0 行の内部用語 (round 表記) を「第 N 回」表記に置換. 中間版 v0.5 提出時の用語規律監査でヒット 1 件残存検出 → 修正後 hits=0 確認. 受信者向け本文 (背景目的 / 業務要件 / 機能要件 / 非機能要件 / 制約条件 / 前提条件) には影響なし. xlsx 再 build (新 sha256: 4f5c4fd6d0cf0e41f572e3bfc5ca6dc3afd91786503f5af17930818d601f45a2 / 24,131 bytes 不変).
- 作成: 主 session (中間版 v0.5 提出時の用語規律監査結果を反映).
- 確認: 機械再検査 (audit_terms.py blacklist hits=0).
- 承認: Bojiang Zhang (用户).

## ITMS-SDTM-00 v0.5 (2026-04-30)
- 改訂区分: 新規作成 (中間版 補助文書)
- 改訂内容: 中間版 zip 同梱物の案内. 元 `deliverable/README_今回納品範囲.md` を Excel 化 (受信者要望「全提交ファイル Excel 化 — 公司習慣準拠」対応 2026-04-30). 6 シート構成 (1 本納品の位置づけ / 2 同梱物一覧 / 3 進捗概況 / 4 残工程予定 / 5 ご確認いただきたい事項 / 6 連絡先).
- 産物: docs/jp/sources/00_納品範囲.yml + docs/jp/00_納品範囲.xlsx (19,399 bytes / 10 シート / sha256 a8552b2f1fba6afd062abe6506779e145dd64da059aaf4b5c6f0558ebc2b0063).
- 作成: 主 session (executor + build_xlsx.py).
- 確認: 機械再検査 (audit_terms.py blacklist hits=0 一発).
- 承認: Bojiang Zhang (用户).

## ITMS-SDTM-07 v0.5 (2026-04-30)
- 改訂区分: 新規作成 (中間版)
- 改訂内容: 受信者向け中間版進捗報告書. 5 シート構成 (1 全体サマリ / 2 工程別進捗 / 3 課題管理 / 4 今後の予定 / 5 参考資料). 受信者向け納品候補 7 件中 2 件 (要件定義書 / 基本設計書) を確定状態 (v1.0) でお送りし, 残 5 件の予定および 4 件の追跡課題を整理.
- 産物: docs/jp/sources/07_進捗報告書.yml + docs/jp/07_進捗報告書.xlsx (19,731 bytes / 9 シート / sha256 a96b8642af4c04eb0af3d9c5005d9c4821745b037ea243b5643bd5e4d8524be4).
- 作成: 主 session (executor + build_xlsx.py).
- 確認: 機械再検査 (audit_terms.py blacklist hits=0 — 1 cycle 修正後: 出典行の `_progress.json` + `WORKLOG.md` 内部ファイル名引用を抽象化).
- 承認: Bojiang Zhang (用户).

## ITMS-SDTM-08 v0.5 (2026-04-30)
- 改訂区分: 新規作成 (中間版 補助文書)
- 改訂内容: 受信者向け反復実績記録. 全工程 5 系統 (AI 平台 4 種プロンプト整備 / smoke 動作試験 / 知識ベース字面級確認 / 受信者向け文書整備 / 用語整備) の検査・修正・反復実績 (約 50 回次相当) を集約. 8 シート構成 (1 全体サマリ / 2 工程別反復集計 / 3 AI 平台反復履歴 / 4 smoke 試験反復履歴 / 5 深層検証反復履歴 / 6 文書整備反復履歴 / 7 主要マイルストーン / 8 参考資料). 受信者要望「過程の試行錯誤の規模を可視化」対応.
- 産物: docs/jp/sources/08_反復実績記録.yml + docs/jp/08_反復実績記録.xlsx (27,116 bytes / 12 シート / sha256 8b9cc08cbb81fa6d3112f480305d9d683d2c392fe09419e036c4366b03fe0b00).
- データソース: ai_platforms/release/v1.0/CHANGELOG.md + ai_platforms/retrospectives/ + ai_platforms/SMOKE_V4.md + 4 平台 dev/checkpoints/ + .work/06_deep_verification/_progress.json + docs/jp/glossary/research_reports/ + docs/jp/CHANGELOG.md + docs/jp/WORKLOG.md.
- 作成: 主 session (executor + build_xlsx.py).
- 確認: 機械再検査 (audit_terms.py blacklist hits=0 — 1 cycle 修正後: D-15 行の round 表記再帰引用 1 件除去).
- 承認: Bojiang Zhang (用户).

## docs/jp/ 中間版 v0.5 提出 (2026-04-30)
- 種別: 受信者向け納品 (中間版 集約)
- 提出産物: docs/jp/deliverable/20260430_iTMS_SDTM_進捗版_v0.5.zip (4,680,626 bytes / 130 files / sha256 087106953c202d5983f5b99c63c3cab95ce3730707a3c9a3d557eb124eed881e) + .sha256 sidecar.
- 同梱物: 6 件 xlsx (00 案内 / 01 基本設計 / 04 要件定義 / 07 進捗報告 / 08 反復実績 / 99 用語集骨格) + ai_platforms/release/v1.0/ 公開発布版資料.
- 経緯: ユーザー判断「P0 4 件中 2 件確定 + 公開発布版で中間版提出」→ 中間版補助文書 3 件 (00 / 07 / 08) 起草 + 全提交ファイル Excel 化 (公司習慣準拠) → audit_terms.py 監査 6/6 PASS → zip 集約 + 解凍テスト + sha256 算出.
- 用语规律監査: 全 6 xlsx hits=0 (修正サイクル 2 件適用後; 04 改訂履歴 round 表記置換 + 07 出典内部ファイル名抽象化 + 08 D-15 行再帰引用除去).

---

## ITMS-SDTM-01 v1.0 (2026-04-29)
- 改訂区分: 新規作成
- 改訂内容: 基本設計書 初版受信者納品候補確定. Phase 1 P0 着手順 2 として起草. 04 要件定義書 §3 機能要件 (FR-01〜FR-11) + §4 非機能要件 (NFR-01〜NFR-06) + §5 制約条件 (C-01〜C-05) を実現する設計レベル文書. 6 シート構成 (1 概要 / 2 全体構成 / 3 データモデル / 4 外部 IF / 5 制約事項 / 6 参考資料) で 4 サブシステム (知識ベース本体 / 検証パイプライン / AI 平台展開 / Phase 7 RAG+KG 設計済・未実装) を扱う. 起草 (writer round 1, self-check 9/9 PASS) → 確認担当 round 1 (CONDITIONAL_PASS, MEDIUM 4 / LOW 4 / info 2) + 用語監査 round 1 (CONDITIONAL_PASS, MEDIUM 1) 並列 → writer round 2 で 10 件反映 + 主 session で T-01 (トレーサビリティ管理表 文書正式名称復元) 補正 → 確認担当 round 2 PASS 無条件 (回帰差分ゼロ + 新規 finding HIGH 0 / MEDIUM 0) → 用语監査 機械再検査 PASS (blacklist 0 hits / mapping 1 false-positive 既知) → 用户口頭承認の経路で 2026-04-29 に v1.0 確定.
- 産物: docs/jp/sources/01_基本設計書.yml + docs/jp/01_基本設計書.xlsx (31,860 bytes / 10 シート / sha256 12721d04050f525014549eada7aef662edcbfd550acbfde7e4c4bc65ad8310cb).
- 作成: Phase 1 P0 着手順 2 (主 session 統括 + executor / code-reviewer / document-specialist subagent 3 種; round 1 + round 2 別 instance; 規律 D 三役完全隔離).
- 確認: 日方ネイティブ確認担当指名待ち (PLAN §6 PASS 五条 補完事項).
- 承認: Bojiang Zhang (用户).
- 申送り (Phase 3): build_xlsx.py 改修 (sha256 再現性 = openpyxl 作成日時固定化) / term_mapping.yml v0.6 改訂 (口語判定エントリ「約」削除案 + pipeline 登録 + 新規訳語 5 件) / 99_用語集.xlsx 仕上げ時の新規訳語登録.
