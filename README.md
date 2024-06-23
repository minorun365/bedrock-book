# 書籍「Amazon Bedrock 生成AIアプリ開発入門」 ハンズオン用サンプルコード

表題の書籍のハンズオンを実施しやすいよう、サンプルコード部分をファイルとして格納したリポジトリです。

- 紙の書籍を購入くださった方も、コピー＆ペーストが可能になります。
- 今後の環境変化でコードに不具合が生じた際、適宜改修していきます。

## このGitHubリポジトリの説明

### 書籍について

まだお持ちでない方は、ぜひお買い求めください！

[Amazon Bedrock 生成AIアプリ開発入門](https://www.sbcr.jp/product/4815626440/)

<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/74597894/333667801-6f862dd4-7eff-4eea-abba-9e0b411bdd8d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240611%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240611T005852Z&X-Amz-Expires=300&X-Amz-Signature=41a6fa7a34799c2dcaab23bf85c90455b4c03cada5dd3af78436a1b6e500f642&X-Amz-SignedHeaders=host&actor_id=74597894&key_id=0&repo_id=775996749" width="70%" />

### このリポジトリの構成

- `chapter⚫️` ディレクトリ ：各章のハンズオン用コードや、手打ちが大変な設定値などを格納しています。
  - 必要なPythonライブラリを記載した `requirements.txt` も、参考までに格納しています。

### エラー等を見つけた際は

本リポジトリの [Issues](https://github.com/minorun365/bedrock-book/issues) へ起票ください。ベストエフォートで対応します。

### 誤植などのお知らせ

[SBクリエイティブ公式サイト](https://www.sbcr.jp/product/4815626440/) にて、正誤情報を適宜掲載します。


## 書籍刊行後のアップデート補足

### 2024/6/20 新モデル「Claude 3.5 Sonnet」がリリース！

Anthropic社の新モデルで、Claude 3 Sonnetの後継となります。性能・コストともにClaude 3 Opusをも上回るとされています。

https://qiita.com/minorun365/items/cd46235d5e446b1f41c5

本書のハンズオンへの取り込み方法

- 書籍P.80を参考に `Claude 3.5 Sonnet` をバージニア北部リージョンのBedrockで有効化する
- 各章のサンプルコードにおいて、Claude 3 SonnetのモデルIDを指定している箇所を、Claude 3.5 SonnetのモデルID（`anthropic.claude-3-5-sonnet-20240620-v1:0`）に置き換える

注意点

- Bedrockでは、GUIやAPI経由での単体モデル呼び出しに対応していますが、応用機能（ナレッジベースやエージェント）へは未対応です（2024/6/20時点）。
- Knowkedge bases for Amazon Bedrockにおいては、 `Retrieve` APIを利用すればClaude 3.5 Sonnetをすぐに活用できます（書籍P.216参照）。

### 2024年7月 Claude 3シリーズがAWS東京リージョンに対応予定

参考記事（クラウドWatch）

https://cloud.watch.impress.co.jp/docs/event/1601745.html

### 2024年内 Amazon Q Businessが日本語およびAWS東京リージョンに対応予定

参考記事（クラウドWatch）

https://cloud.watch.impress.co.jp/docs/event/1601745.html
