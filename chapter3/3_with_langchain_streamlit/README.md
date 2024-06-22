# 3.5 LangChainとStreamlitを使った生成AIアプリ開発 (p.154)

## Claude 3.5 Sonnetへの対応

第2章のp.80を参考にAnthropic社の「Claude 3.5 Sonnet」モデルを有効化してください。

ソースコード中の`model_id`を`anthropic.claude-3-5-sonnet-20240620-v1:0`に変更します。ライブラリーのバージョンアップは必要ありません。

* 変更前
    ```python
    # ChatBedrockを生成
    chat = ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        model_kwargs={"max_tokens": 1000},
    )
    ```

* 変更後
    ```python
    # ChatBedrockを生成
    chat = ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        model_kwargs={"max_tokens": 1000},
    )
    ```
