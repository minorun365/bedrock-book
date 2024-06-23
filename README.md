# 書籍「Amazon Bedrock 生成AIアプリ開発入門」 ハンズオン用サンプルコード

表題の書籍のハンズオンを実施しやすいよう、サンプルコード部分をファイルとして格納したリポジトリです。

- 紙の書籍を購入くださった方も、コピー＆ペーストが可能になります。
- 今後の環境変化でコードに不具合が生じた際、適宜改修していきます。

## このGitHubリポジトリの説明

### 書籍について

まだお持ちでない方は、ぜひお買い求めください！

[Amazon Bedrock 生成AIアプリ開発入門](https://www.sbcr.jp/product/4815626440/)

![](images/flyer.png)

### このリポジトリの構成

- `chapter⚫️` ディレクトリ ：各章のハンズオン用コードや、手打ちが大変な設定値などを格納しています。
  - 必要なPythonライブラリを記載した `requirements.txt` も、参考までに格納しています。
  - 書籍刊行後の機能アップデートへの対応方法などを `README.md` にて補足しています。

### エラー等を見つけた際は

本リポジトリの [Issues](https://github.com/minorun365/bedrock-book/issues) へ起票ください。ベストエフォートで対応します。

### 誤植などのお知らせ

[SBクリエイティブ公式サイト](https://www.sbcr.jp/product/4815626440/) にて、正誤情報を適宜掲載します。


## 書籍刊行後のアップデート補足

### 2024/6/20：新モデル「Claude 3.5 Sonnet」がリリース！（対象：第2章ほか）

Anthropic社の新モデルで、Claude 3 Sonnetの後継となります。性能・コストともにClaude 3 Opusをも上回るとされています。

https://qiita.com/minorun365/items/cd46235d5e446b1f41c5

本書のハンズオンへの取り込み方法

- 書籍P.80を参考に `Claude 3.5 Sonnet` をバージニア北部リージョンのBedrockで有効化する（需要過多により「利用不可」ステータスとなり、有効化できないタイミングがあります。）
- 各章のサンプルコードにおいて、Claude 3 SonnetのモデルIDを指定している箇所を、Claude 3.5 SonnetのモデルID（`anthropic.claude-3-5-sonnet-20240620-v1:0`）に置き換える

注意点

- Bedrockでは、GUIやAPI経由での単体モデル呼び出しに対応していますが、応用機能（ナレッジベースやエージェント）へは未対応です（2024/6/20時点）。
- Knowkedge bases for Amazon Bedrockにおいては、 `Retrieve` APIを利用すればClaude 3.5 Sonnetをすぐに活用できます（書籍P.216参照）。

### 2024年7月：Claude 3シリーズがAWS東京リージョンに対応予定（対象：第2章）

参考記事（クラウドWatch）

https://cloud.watch.impress.co.jp/docs/event/1601745.html

### 2024年内：Amazon Q Businessが日本語およびAWS東京リージョンに対応予定（対象：第9章）

参考記事（クラウドWatch）

https://cloud.watch.impress.co.jp/docs/event/1601745.html
