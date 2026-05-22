---
lang: ja
slug: glossary
order: 40
title: "用語集"
---

# 用語集

本ページでは、SDTM Pedia を使う際によく出てくる臨床データ標準用語だけを説明します。プラットフォーム設定、ファイルアップロード、内部検証に関する用語は、公開用語集からは除外しています。

| 用語 | 意味 | 使用上の注意 |
| --- | --- | --- |
| CDISC | SDTM、ADaM、CDASH などを発行する臨床データ標準団体。 | 正式な解釈は CDISC 公式刊行物を確認してください。 |
| SDTM | Study Data Tabulation Model。 | 臨床研究の提出用データの構造を定めます。 |
| SDTMIG | SDTM Implementation Guide。 | ドメイン、変数、実装ルールを説明します。 |
| Domain | AE、DM、LB、CM など、テーマ別の SDTM データ構造。 | 標準化されたデータセットとして理解できます。 |
| Variable | AESER、LBTESTCD、CMTRT など、ドメイン内の標準フィールド。 | 質問時は英語コードのまま残すと照合しやすくなります。 |
| Core | Required、Expected、Permissible などの変数使用区分。 | データセット上での変数の扱いを判断する手がかりです。 |
| Controlled Terminology | CDISC/NCI により管理される標準値セット。 | submission value を制限する場面で使われます。 |
| Codelist | NY、AESEV、LBNRIND など、名前付きの用語リスト。 | 必要に応じて C-code と submission values をあわせて確認します。 |
| C-code | NCI EVS 上の用語または codelist コード。 | 公式用語ソースとの照合に役立ちます。 |
| Submission Value | 提出データで実際に使う値。 | 例: NY codelist の Y、N、U、NA。 |
| MedDRA | Medical Dictionary for Regulatory Activities。不良事象コーディングでよく使われます。 | AEDECOD、AELLT、AEHLT など AE 関連変数と関係します。 |
| SUPPQUAL / SUPP-- | 標準変数で表現しきれない補足情報を扱う仕組み。 | すべてのドメインや場面に適用されるわけではありません。 |
| RELREC | レコード間の関係を表す Related Records テーブル。 | クロスドメイン関係の質問でよく出てきます。 |
| Trial Design | TA、TE、TV、TI、TS など試験設計関連ドメイン。 | subject-level のイベントや所見データとは性質が異なります。 |
| ISO 8601 | 日付と時刻の表現標準。 | SDTM の --DTC 変数でよく使われます。 |
| Define-XML | 臨床試験提出におけるメタデータ交換形式。 | データセット、変数、用語、由来などを説明します。 |

## 読み方

回答に知らない変数、ドメイン、C-code が出てきた場合は、まずその用語の説明を SDTM Pedia に尋ねてから元の質問に戻ると理解しやすくなります。正式成果物では、説明を CDISC 公式資料と照合してください。
