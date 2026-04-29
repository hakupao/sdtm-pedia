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
- `ITMS-SDTM-01` — 基本設計書
- `ITMS-SDTM-02` — 運用・保守マニュアル
- `ITMS-SDTM-03` — テスト結果報告書
- `ITMS-SDTM-04` — 要件定義書
- `ITMS-SDTM-05` — 詳細設計書
- `ITMS-SDTM-06` — トレーサビリティ管理表
- `ITMS-SDTM-07` — 進捗報告書
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

## ITMS-SDTM-EXEC v0.2 (2026-04-29)
- 改訂区分: 内容修正 (PLAN v0.3 同期)
- 改訂内容: §3 Phase 1 のスケジュールを「Day 1 = 04 直列 → Day 1 後半/Day 2 = 01 直列 → Day 3 = 02 + 03 並列 → Day 4 = 用語監査 並列」に更新. §3 Phase 2 を 05 単独 1 日構成に縮小. §8 並列効果サマリの所要工数を P0 四点換算 (5/3.5/2.5 日) + Phase 2 圧縮 (1.5/1/0.7 日) で再算出.
- 作成: 主 session
- 確認: pending
- 承認: pending
