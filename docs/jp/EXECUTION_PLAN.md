<!-- chain: J' (落地方案 + 调度链 v0.1; PLAN.md 链 J 的下游)
  修改本文件后, 必须检查:
  → docs/jp/PLAN.md                  (上流 WHAT/WHY 文書, 整合性確認)
  → docs/jp/_progress.json           (Phase 開始前 / 完了後 双方更新)
  → docs/jp/prompts/                 (各 subagent 用提示テンプレ実体)
  → docs/jp/failures/                (失敗時の retro アーカイブ先)
  → ../../.work/MANIFEST.md          (新規ファイル登録)
-->

# docs/jp/ — 落地方案 + Agent 调度設計

> 创建: 2026-04-29
> 状态: **DRAFT v0.1** — Phase -1 産物, Phase 0 Setup 起動前に確定要
> 上流: `docs/jp/PLAN.md` v0.2 (WHAT/WHY)
> 本書職責: **HOW** — 各 Phase の agent 配役 / 派発順序 / 並列機会 / 隔離設計 / 失敗回路
> Tier: **2** (PLAN.md と同 Tier)

---

## 凡例 (本書共通)

| 記号 | 意味 |
|------|------|
| 🔀 | **同一 session 内並列** — 主 session が複数 subagent を Task 並列呼び出し |
| 📡 | **多 session 並列** — Claude Code 複数インスタンス起動 (`.work/06_deep_verification/multi_session/` パターン踏襲) |
| ➡️ | **直列必須** — 前段成果物が後段入力 |
| ⚠️ | **規則 D 注意** — 前段と異なる subagent_type 必須 |
| 💾 | **進捗書込み点** — `_progress.json` 更新タイミング |

---

## 1. Agent 配役表 (Default Lineup)

| 役割 | subagent_type | model | context 予算 | 用途 |
|------|--------------|-------|------------|------|
| **W: writer** | `executor` | sonnet (routine) / opus (複雑) | 中 (引用源 + 用語辞書 + テンプレ) | .xlsx 内容生成 (各文書) |
| **R: reviewer** | `code-reviewer` | opus | 中 (writer 産物 + PLAN §3 + §10 制約) | §6 PASS 1-3 審査 |
| **A: 用語監査** | `document-specialist` | sonnet | 小 (writer 産物 + blacklist + mapping) | §6 PASS 4 審査 (用語規律) |
| **V: 最終検証** | `verifier` | opus | 大 (全納品物 + cross-link) | Phase 4 最終 PASS |
| **S: 調研** | `document-specialist` | sonnet | 小〜中 (web + 規格 PDF) | Phase 0.5 用語規格調研 |
| **D: 設計助言** | `architect` | opus | 小 | 中途で設計判断要時のみオンデマンド |

**Rule D 隔離マトリックス** (writer ↔ 同 PASS 内の他 role が同 type 禁止):

| 工程 | writer | reviewer | 用語監査 | 隔離 OK? |
|------|--------|---------|---------|---------|
| 各文書生成 | `executor` | `code-reviewer` | `document-specialist` | ✅ 3 type 全異 |
| 用語調研 (Phase 0.5) | `document-specialist` (research) | `code-reviewer` (mapping 審査) | — | ✅ 異 |
| 最終 Phase 4 | (各文書既存成果) | `verifier` | — | ✅ verifier は別 type |

---

## 2. 並列度デフォルト (Open Issue I-3 で覆書可)

| 並列モード | 上限 | 理由 |
|----------|------|------|
| 🔀 単 session 内 subagent fan-out | **2** | 主 session の context 干渉回避 |
| 📡 多 session 並列 | **3** | ユーザの認知負荷上限 (06 deep verification 知見) |
| 読取専用 research subagent | 制限なし | write 競合なし |

「効率優先」要求のため, 各 Phase で**最大限の並列機会**を §3 に明示. 採用は用户判断.

---

## 3. Phase ごとの派発計画

### Phase 0 — Setup (0.5 日)
**性質**: 純粋ファイル作成, 軽量.

| Step | 内容 | agent | 並列 | 備考 |
|------|------|-------|------|------|
| 0.1 | ディレクトリ骨格 (`sources/` `glossary/` `templates/` `scripts/` `assets/` `failures/` `deliverable/` `prompts/`) | 主 session 直接 Bash | — | 単発, 1 命令 |
| 0.2 | `_progress.json` 初期化 | 主 session 直接 Write | 🔀 0.3-0.6 と並列可 | Tier 2 schema 適用 |
| 0.3 | `CHANGELOG.md` 空骨格 | 主 session 直接 Write | 🔀 | |
| 0.4 | `00_README.md` placeholder | 主 session 直接 Write | 🔀 | |
| 0.5 | `glossary/term_blacklist.yml` 初期版 (PLAN §11.1 を yml 化) | 主 session 直接 Write | 🔀 | |
| 0.6 | `glossary/reference_standards.md` 初期骨格 (PLAN §11.3 一覧) | 主 session 直接 Write | 🔀 | |
| 0.7 | `.work/MANIFEST.md` 入口追加 + `CLAUDE.md` Key Paths 1 行追加 | 主 session 直接 Edit | ➡️ 0.1-0.6 完了後 | 整合性のため最後 |
| 💾 | `_progress.json` Phase 0 PASS 記録 | 主 session | — | |

**並列機会**: Step 0.2-0.6 は 5 並列 Write 可. **subagent 派遣不要** (主 session 単独で十分軽量).
**所要時間**: 並列実施で 30-45 分.

---

### Phase 0.5 — 用語調研フェーズ (1-2 日 ★ 短縮厳禁) 🔥 並列効果最大

**性質**: 7 規格を独立調査 + 25+ blacklist 用語の言換え調査. **本工程の並列化が全工程の所要時間を最も削減する**.

#### Option A: 単 session + 🔀 subagent fan-out (推奨, 管理楽)

| Step | 内容 | agent | 並列 | 備考 |
|------|------|-------|------|------|
| 0.5.1 | IT 規格 4 件調研 (IPA / JIS X 0160 / JIS X 25010 / 共通フレーム 2013) | S × 1 | — | 1 subagent が 4 規格まとめ |
| 0.5.2 | 医療規格 4 件調研 (PMDA ER/ES / 厚労省 ガイドライン / GAMP 5 / ICH E6(R3)) | S × 1 | 🔀 0.5.1 と並列 ⚠️ 同 type だが文脈完全独立 OK | Rule D は同 PASS 内の writer/reviewer 関係のみ適用; 並列 research は OK |
| 0.5.3 | CDISC 公式日本語訳調査 (CJUG) + JIS T 14971 + JIS Z 8301 | S × 1 | 🔀 0.5.1-0.5.2 と並列 | 補助規格 |
| 0.5.4 | blacklist 用語 25+ を 3 batch 分割 (約 8 用語/batch), 各 batch で言換え 3 候補 + 出典付与 | S × 3 | 🔀 3 並列 | 0.5.1-0.5.3 完了後 |
| 0.5.5 | 全候補を統合, `term_mapping.yml` 初版作成 | 主 session | ➡️ | reconciler 役 |
| 0.5.6 | mapping 独立審査 | R × 1 | ➡️ ⚠️ | code-reviewer 別 type で隔離 |
| 0.5.7 | reviewer NG → 0.5.5 ループ (上限 2 回) | — | — | エスカレーション §5 参照 |
| 0.5.8 | `99_用語集.xlsx` 骨格生成 (Phase 0.7 完了後にスタイル付与) | W × 1 | ➡️ | データ部分のみ |
| 💾 | `_progress.json` Phase 0.5 PASS 記録 | 主 session | — | |

**並列効果**: 0.5.1-0.5.3 で 3 並列 + 0.5.4 で 3 並列. 直列実施だと約 6 fan-out 分の時間が圧縮可.

#### Option B: 📡 多 session 並列 (大幅短縮狙い)

`.work/06_deep_verification/multi_session/` 既存パターン踏襲:

- **Session A** (主): 全体統括 + reconciler 役
- **Session B**: IT 規格 4 件調研 (kickoff: `kickoff_session_B_IT_standards.md`)
- **Session C**: 医療規格 4 件調研 (kickoff: `kickoff_session_C_medical_standards.md`)
- **Session D**: blacklist 用語言換え 25+ 件 (kickoff: `kickoff_session_D_term_mapping.md`)
- 完了後 Session A が統合 + reviewer 派発

**メリット**: context 完全分離, 各 session が深掘り可
**デメリット**: 用户が 4 session 管理する手間
**判断**: 用户の時間予算次第. 直列の 1.5-2 日 → 多 session で 0.5-1 日に短縮可能.

---

### Phase 0.7 — Excel スタイル基盤 (0.5 日)

| Step | 内容 | agent | 並列 | 備考 |
|------|------|-------|------|------|
| 0.7.1 | openpyxl vs exceljs 確定調査 | D × 1 | — | architect が短評 |
| 0.7.2 | `templates/style_guide.xlsx` 作成 (PLAN §3.1 配色 + フォント + セル書式 サンプル収録) | W × 1 | 🔀 0.7.3 と並列 | |
| 0.7.3 | `templates/cover_template.xlsx` 作成 (表紙 / 改訂履歴 / 承認欄 統一様式) | W × 1 | 🔀 | |
| 0.7.4 | `scripts/build_xlsx.{py|mjs}` PoC | W × 1 | ➡️ 0.7.1 完了後 | |
| 0.7.5 | サンプル文書で生成テスト + 視覚 QA | R × 1 | ➡️ ⚠️ | reviewer が別 type で確認 |
| 0.7.6 | 用户視覚 ack ("好看" 基準) | 用户 | ➡️ | 人手 gate |
| 💾 | `_progress.json` Phase 0.7 PASS 記録 | | | |

**並列機会**: 0.7.2 + 0.7.3 で 2 並列 (異ファイル, 独立).

---

### Phase 1 — P0 四点セット (2.5-3.5 日, v0.3 改訂で 04 を P0 格上げ) 🔥 並列効果大

**重要な依存関係 (改訂)**:
- `04_要件定義書.xlsx` の **目的 / 業務要件 / 制約 / 前提条件** が後段 3 文書 (01 / 02 / 03) すべての根拠章になる
- → **04 を先行 (0.5-1 日), 続いて 01 (1 日), 完成後 02 + 03 を並列 (1-1.5 日)** が最効率

#### 推奨スケジュール

```
Day 1 前半:  ➡️  04 writer → reviewer → 用語監査 → 用户 ack       (直列, 0.5-1 日)
Day 1 後半 / Day 2:  ➡️  01 writer (04 の節を引用) → reviewer → 用語監査 → 用户 ack    (直列, 1 日)
Day 3:  🔀  02 writer + 03 writer (並列, 各々 04 + 01 の節を引用)
        ➡️  02 reviewer + 03 reviewer (各々直列)
Day 4 前半:  🔀  02 用語監査 + 03 用語監査 (並列) + 用户 ack
```

#### 各文書内のステップ (パターン化)

| Step | 内容 | agent | 並列 |
|------|------|-------|------|
| N.1 | 源材料読取 + .xlsx 生成 (sources/NN.yml + script 経由) | W × 1 | — |
| N.2 | 形式 + 内容 審査 (PASS 1-3) | R × 1 ⚠️ | ➡️ |
| N.3 | 用語監査 (PASS 4, blacklist + mapping) | A × 1 ⚠️ | 🔀 N.2 と並列可 (両者 writer 産物のみ参照) |
| N.4 | 監査結果統合 → 修正必要なら N.1 へ (上限 2 回) | 主 session | ➡️ |
| N.5 | 用户口頭 ack (PASS 5) | 用户 | ➡️ |
| 💾 | `_progress.json` 文書 N PASS 記録 | | |

**追加並列機会** (各文書内):
- N.2 reviewer と N.3 用語監査は **同時起動可** (両者とも writer 産物のみ読む, 互いに独立)
- 1 文書の処理時間を約 30-40% 短縮

#### Option B: 📡 多 session で 02 + 03 を完全分離

- **Session A**: 01 専任 + 全体統括
- **Session B**: 02 専任 (Day 2 起動)
- **Session C**: 03 専任 (Day 2 起動)
- 各 session が writer/reviewer/用語監査 を内部で回す

**判断基準**: 用户が 3 session 同時管理可なら採用. context 競合ゼロ.

---

### Phase 2 — P1 補完 (1 日, v0.3 改訂で 04 を Phase 1 に移したため 05 のみ)

`05_詳細設計書.xlsx` 単独. Phase 1 終了後 01 基本設計を引用しつつ単線で進める.

| Step | 内容 | agent | 並列 |
|------|------|-------|------|
| 5.1 | sources/05_詳細設計書.yml 整備 + .xlsx 生成 | W × 1 | — |
| 5.2 | 形式 + 内容 審査 | R × 1 ⚠️ | ➡️ |
| 5.3 | 用語監査 | A × 1 ⚠️ | 🔀 5.2 と並列可 |
| 5.4 | 用户 ack | 用户 | ➡️ |

**所要時間**: 1 日.

---

### Phase 3 — P2 仕上げ (1 日) 🔥 4 並列可

4 ファイル全て独立:
- `06_トレーサビリティ管理表.xlsx`
- `07_進捗報告書.xlsx`
- `00_README.md` 完成版
- `99_用語集.xlsx` 完成版 (Phase 0.5 骨格にスタイル付与)

| Mode | 構成 |
|------|------|
| **🔀** | 主 session が 4 並列 writer 派発 (上限 2 制約のため 2+2 分割推奨) |
| **📡** | 4 session 並列 — 用户負担が大きいので非推奨 |

**所要時間**: 並列 (2 batch) で 0.5-1 日.

---

### Phase 4 — Pack & Handoff (0.5 日)

| Step | 内容 | agent | 並列 |
|------|------|-------|------|
| 4.1 | 全文書 cross-link 検証 (Bash + script) | 主 session | — |
| 4.2 | zip パッケージ作成 → `deliverable/` | 主 session | — |
| 4.3 | 最終検証 (PASS 五条 全文書 cross-check) | V × 1 ⚠️ | ➡️ |
| 4.4 | `RETROSPECTIVE.md` 起草 (規則 C 強制) | 主 session | 🔀 4.3 と並列可 |
| 4.5 | CLAUDE.md / MANIFEST.md 最終整合確認 | 主 session | ➡️ |
| 💾 | `_progress.json` 全工程 PASS 記録 + final ack | | |

---

## 4. プロンプトテンプレ (実体は `docs/jp/prompts/` 配下)

Phase 0 Setup で骨格作成, Phase 0.7 完了後に最終化.

| ファイル | 用途 |
|----------|------|
| `prompts/writer_xlsx.md` | 各文書 writer 共通テンプレ (源参照 / シート構成 / 用語制約 注入) |
| `prompts/reviewer_xlsx.md` | reviewer 共通 (PASS 1-3 チェックリスト) |
| `prompts/term_audit.md` | 用語監査 (PASS 4 チェックリスト + blacklist + mapping 注入) |
| `prompts/research_standards.md` | Phase 0.5 規格調研テンプレ (一次資料 URL 必須 + 取得日記録) |
| `prompts/term_mapping_proposal.md` | Phase 0.5.4 言換え候補生成 (3 候補 + 出典必須) |
| `prompts/final_verifier.md` | Phase 4 最終検証 (cross-doc + cross-link) |

**設計原則**:
- 各テンプレは「入力 / 産物 / 受入条件 / 失敗時の挙動」を明示
- 注入する制約は PLAN §10 + §11 をそのまま埋込み (writer が制約を見えなくする事故防止)
- テンプレは git 管理, 改訂は CHANGELOG に記録

---

## 5. エスカレーション (失敗時回路)

| 失敗ケース | 対応 |
|-----------|------|
| reviewer NG (1 回目) | writer に diff + 指摘事項を渡し再生成. ループ回数を `_progress.json` に記録 |
| reviewer NG (2 回目) | 主 session が介入. PLAN/制約を読み直し, writer プロンプトに不足追加. ループ回数 +1 |
| reviewer NG (3 回目) | **強制中断**. `failures/Phase_NN_attempt_X.md` 起草 (規則 B 強制). architect 派発で根本判断を求める |
| 用語監査 NG | blacklist hit を mapping で置換 → writer に再生成依頼 (上限 2 回) |
| 用户 ack NG | 用户フィードバックを `failures/` 経由でアーカイブ + writer に渡し再起動 |
| subagent エラー (timeout / context overflow) | context 予算を §1 から 1 段下げ + 不要源削減で再派発 |

**失敗アーカイブ書式** (`failures/Phase_NN_doc_NN_attempt_X.md`):

```markdown
# Failure Record — Phase X / Doc Y / Attempt Z
- 発生日時:
- 失敗段階: writer / reviewer / 用語監査 / 用户 ack
- 入力概要: (元プロンプト + 注入源)
- 産物概要: (writer/reviewer の出力サマリ)
- 技術的判定: (構造的に何が壊れたか)
- 業務的判定: (内容/用語的に何が NG か)
- 次 attempt 入力: (どう修正して再起動するか)
```

---

## 6. コンテキスト予算 (subagent ごとの読込み源 白リスト)

context 爆発を防ぐため **各 subagent には必要最小源のみ** 渡す:

| agent | 必須読込 | 任意読込 | 禁止読込 |
|-------|---------|---------|---------|
| W (writer) | 該当 `sources/NN.yml` + `templates/style_guide.xlsx` + `glossary/term_mapping.yml` + PLAN §3 §11 抜粋 | 該当源産物 (例: 01 なら DESIGN_RAG_KG.md) | `.work/06_deep_verification/` 内部資料 |
| R (reviewer) | writer 産物 + PLAN §3 §6 §10 抜粋 | — | 源産物 (writer 産物のみで判定) |
| A (用語監査) | writer 産物 + `glossary/term_blacklist.yml` + `glossary/term_mapping.yml` | — | PLAN 全文 (制約だけ抜粋注入) |
| S (調研) | 規格名 + 検索キーワード | web fetch 結果 | リポジトリ内産物 |
| V (最終検証) | 全納品 .xlsx + PLAN §6 + cross-link マップ | — | — |
| D (architect) | 該当 PLAN 章 + 失敗 record | — | — |

---

## 7. 検証スクリプト白リスト (`scripts/` 配下)

Phase 0.7 で作成 + Phase 0.5 後に追加:

| script | 用途 | 使用 Phase |
|--------|------|-----------|
| `scripts/build_xlsx.{py|mjs}` | yml → スタイル付き .xlsx | Phase 0.7 以降全 |
| `scripts/audit_terms.py` | blacklist 残存検査 + mapping 一貫性検査 | Phase 1 以降 |
| `scripts/check_links.py` | 文書間 cross-link 検証 | Phase 4 |
| `scripts/extract_xlsx_text.py` | .xlsx → 全文 txt 抽出 (audit_terms.py の前処理) | Phase 1 以降 |

---

## 8. 全工程 並列効果サマリ

| Phase | 直列想定 | 並列 (🔀) | 多 session (📡) | 短縮率 |
|-------|---------|-----------|----------------|-------|
| 0 Setup | 1h | 0.5h | — | 50% |
| 0.5 用語調研 | 2 日 | 1.5 日 | **0.5-1 日** | 50-75% |
| 0.7 Excel 基盤 | 0.5 日 | 0.5 日 | — | 0% (元々短い) |
| 1 P0 四点 (v0.3) | 5 日 | 3.5 日 | **2.5 日** | 30-50% |
| 2 P1 補完 (v0.3, 05 のみ) | 1.5 日 | 1 日 | **0.7 日** | 33-53% |
| 3 P2 仕上げ | 2 日 | 1 日 | 0.7 日 | 50-65% |
| 4 Pack | 0.5 日 | 0.5 日 | — | 0% |
| **合計 (v0.3)** | **約 11.5 日** | **約 8 日** | **約 5.5-6 日** | **~50%** |

**判断材料**:
- 🔀 単 session 並列のみ → **約 8 日** (用户負担最小)
- 📡 多 session 投入 (Phase 0.5 + Phase 1) → **約 5-6 日** (用户が 3-4 session 管理可なら)

---

## 9. Open Issues (Phase 0 起動前に決定要)

| # | 質問 | 既定値 (本 PLAN 採用) | 用户判断 |
|---|------|-------------------|---------|
| I-3 | agent 池範囲 | OMC 全カタログ可, ただし §1 デフォルト 6 役で運用開始 | 限定する? |
| I-4 | 並列度上限 (🔀) | 単 session 内 ≤2 | 上下調整? |
| I-5 | 多 session 採用 (📡) | Phase 0.5 + Phase 1 で**任意採用** | 全採用 / 不採用 / Phase 限定? |
| I-6 | Excel 生成基盤 | openpyxl (Python) 推奨 | exceljs 指定? Python 環境準備可? |
| I-7 | 日方ネイティブ reviewer | 未定 → 「pending JP review」状態許容で進行 | 指名できる? |
| I-8 | 用户 ack のタイミング | 各 Phase 完了時 + 各文書完了時 (5 文書 + 7 Phase = 12 ack 点) | 頻度調整? |

---

## 10. Next Action

本 EXECUTION_PLAN.md の用户確認 → I-3〜I-8 決定 → Phase 0 Setup 起動.

Phase 0 起動コマンド (用户合図後):
1. `_progress.json` + `CHANGELOG.md` + `00_README.md` + `term_blacklist.yml` + `reference_standards.md` を 5 並列 Write
2. ディレクトリ骨格 1 命令で作成
3. `MANIFEST.md` + `CLAUDE.md` Key Paths 更新
4. `_progress.json` に Phase 0 PASS 記録
5. 用户に Phase 0.5 起動可否を確認
