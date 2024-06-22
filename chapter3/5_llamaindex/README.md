# 3.7.1 LlamaIndex (p.179)

本書の第２章や巻末の付録を参考にして、以下の開発環境を準備します。

- AWSアカウント、IAMユーザー、Cloud9の作成（付録１～４：p.498参照）
- Anthropic社の「Claude 3 Sonnet」モデルの有効化（第2章：p.80参照）

以下のコマンドを実行して、必要なライブラリをインストールします。

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

## Claude 3.5 Sonnetへの対応

Claude 3.5 Sonnetを使用する場合は、モデルを有効化した後、`model`の指定を変更してください。

* 変更前

    ```python
    # Bedrockを生成
    llm = BedrockConverse(
        model="anthropic.claude-3-sonnet-20240229-v1:0",
    )
    ```

* 変更後
    
    ```python
    # Bedrockを生成
    llm = BedrockConverse(
        model="anthropic.claude-3-5-sonnet-20240620-v1:0",
    )
    ```
