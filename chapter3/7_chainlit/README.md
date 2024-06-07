# 3.7.3 Chainlit (p.181)

本書の第２章や巻末の付録を参考にして、以下の開発環境を準備します。

- AWSアカウント、IAMユーザー、Cloud9の作成（付録１～４：p.498参照）
- Anthropic社の「Claude 3 Haiku」モデルの有効化（第2章：p.80参照）

以下のコマンドを実行して、必要なライブラリをインストールします。

```shell
pip install -r requirements.txt
```

以下のコマンドを実行してPythonファイルを実行します。

```shell
chainlit run 1_chainlit.py --port 8080
```
