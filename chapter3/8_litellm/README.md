# 3.7.3 LiteLLM (p.183)

本書の第２章や巻末の付録を参考にして、以下の開発環境を準備します。

- AWSアカウント、IAMユーザー、Cloud9の作成（付録１～４：p.498参照）
- Anthropic社の「Claude 3 Sonnet」モデル、「Claude Instant」の有効化（第2章：p.80参照）
- Amazon社の「Titan Text G1 - Lite」モデルの有効化（第2章：p.80参照）

以下のコマンドを実行して、必要なライブラリをインストールします。

```shell
pip install -r requirements.txt
```

以下のコマンドを実行してPythonファイルを実行します。

```shell
python3 1_litellm.py
```

## Claude 3.5 Sonnetへの対応

第2章のp.80を参考にAnthropic社の「Claude 3.5 Sonnet」モデルを有効化してください。

ソースコード中の`model`に`anthropic.claude-3-5-sonnet-20240620-v1:0`を追加してください。ライブラリーのバージョンアップは必要ありません。

```python
# 呼び出し対象の生成AIモデルを定義
models = [
    "bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
    "bedrock/anthropic.claude-instant-v1",
    "bedrock/amazon.titan-text-lite-v1",
    "bedrock/anthropic.claude-3-5-sonnet-20240620-v1:0",
]
```
