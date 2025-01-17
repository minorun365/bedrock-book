# 3.7.1 LlamaIndex (p.179)

> [!NOTE]
> 💡 本ディレクトリーはAmazon Novaへ対応したソースを配置しています。

書籍に記載しているBoto3はAmazon Novaに未対応です。Amazon Novaを使用したい場合は以下のコマンドを実行して、Amazon Novaに対応したバージョンのライブラリをインストールします。

```shell
pip install -r requirements.txt
```

以下のコマンドを実行してPythonファイルを実行します。

```shell
python3 1_llamaindex.py
```

## 注意事項

LlamaIndexのサンプルは、「llama-index-llms-bedrock-converse」ライブラリーの依存関係の都合上、書籍にある他のサンプルコードより新しいバージョンのboto3を使用します。動作に問題が出た場合は、一度インストール済みのライブラリーを削除し、再度pipコマンドを試してください。

インストール済みのライブラリーを削除するコマンド

```shell
rm -rf  ~/.local/lib/python3.9/site-packages/
```
