# 管理者向けデプロイガイド索引

本ディレクトリは、SDTM Pedia の各プラットフォームインスタンスを設定または保守する管理者向けです。通常のユーザーは、チームが設定済みの Claude Project、ChatGPT GPT、Gemini Gem、NotebookLM notebook にアクセスするだけで十分です。

## このディレクトリを読む場面

- チームにまだ入口がなく、管理者が新しく作成する必要がある場合。
- 組織内でアクセス権限、instructions、知識ファイルを一貫して保守する場合。
- 既存インスタンスを更新または置き換える場合。
- インスタンスが基本的な SDTM 照会に回答できることを確認する場合。

## プラットフォームガイド

| プラットフォーム | ガイド | 向いている場面 |
| --- | --- | --- |
| Claude Projects | [claude/tutorial.ja.md](./claude/tutorial.ja.md) | 複雑な標準説明とクロスドメイン推論。 |
| ChatGPT GPTs | [chatgpt/tutorial.ja.md](./chatgpt/tutorial.ja.md) | チームの日常検索と使い慣れた ChatGPT 入口。 |
| Gemini Gems | [gemini/tutorial.ja.md](./gemini/tutorial.ja.md) | 長い文脈の総合と探索的比較。 |
| NotebookLM | [notebooklm/tutorial.ja.md](./notebooklm/tutorial.ja.md) | 厳格な出典境界と引用確認。 |

## 共通原則

- 本リリースパッケージ内の対応プラットフォームディレクトリにある instruction ファイルと `uploads/` 内容を使用します。
- 新バージョンを意図的に保守する場合を除き、instruction 文を改写したり知識ファイル名を変更したりしないでください。
- 共有前に、組織のデータセキュリティ、患者プライバシー、アクセス権限要件を確認します。
- 編集権限は少数の保守担当者に限定し、通常ユーザーは利用権限のみとします。
- 更新後は、変数定義、ドメイン境界、統制用語の照会ができることを少数の標準質問で確認します。

## 利用範囲

デプロイ済みインスタンスは SDTM 照会支援ツールです。CDISC 公式刊行物、医学的判断、プロジェクトレベルのマッピングレビュー、内部品質プロセスを置き換えるものではありません。
