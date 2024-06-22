# 3.7.2 Gradio (p.180)

本書の第２章や巻末の付録を参考にして、以下の開発環境を準備します。

- AWSアカウント、IAMユーザー、Cloud9の作成（付録１～４：p.498参照）
- Anthropic社の「Claude 3 Haiku」モデルの有効化（第2章：p.80参照）
- Stability AI社の「SDXL 1.0」モデルの有効化（第2章：p.80参照）

Cloud9のPython3.9の環境ではライブラリーの依存関係の解決ができないため、Python3.10の環境を使用します。

以下のコマンドを実行して、Python3.10のDockerコンテナを起動します。

```shell
docker run -it -v $PWD:/work -v ~/.aws:/root/.aws -p 8080:8080 -w /work python:3.10 bash
```

以下のコマンドを実行して、必要なライブラリをインストールします。

```shell
pip install -r requirements.txt
```

## 1_image-generator.py

以下のコマンドを実行してPythonファイルを実行します。

```shell
python3 1_image-generator.py
```

画面上部にあるPreviewをクリックし、Preview Running Applicationをクリックします。

input入力欄に`An astronaut riding a green horse`などを入力し、`Submit`ボタンをクリックします。

終わったら`Ctrl` + `c`でGradioアプリを終了します。

## 2_multi-modal.py

以下のコマンドを実行してPythonファイルを実行します。

```shell
python3 python3 2_multi-modal.py
```

画面上部にあるPreviewをクリックし、Preview Running Applicationをクリックします。

クリップのアイコンから画像ファイルをアップロードし、プロンプトを入力します。

終わったら`Ctrl` + `c`でGradioアプリを終了します。

### Claude 3.5 Sonnetへの対応

サンプルコードではClaude 3 Haikuを使用していますが、Claude 3.5 Sonnetを使用する場合は、モデルを有効化した上で、`modelId`の指定を変更してください。

* 変更前
    ```python
    # モデル呼び出し
    response = client.invoke_model_with_response_stream(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        body=json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 300,
                "messages": messages,
            }
        ),
    )
    ```

* 変更後
    ```python
    # モデル呼び出し
    response = client.invoke_model_with_response_stream(
        modelId="anthropic.claude-3-5-sonnet-20240620-v1:0",
        body=json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 300,
                "messages": messages,
            }
        ),
    )
    ```


## 後処理

Dockerコンテナを抜けます

```shell
exit
```
