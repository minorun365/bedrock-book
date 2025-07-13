## 8.2 BedrockとStep Functionsを使った生成AIアプリ開発

2025/7/12追加：AWS Step Functionsのアップデートにより、ハンズオン実施手順が一部変更になります。

### 変更点１：Step FunctionsがJSONataに対応したことによる対応

Step Functionsで使用できるクエリ言語にJSONataが追加されました。書籍で使用しているクエリ言語がJSONPathのため、明示的に指定します。

P.386の「タスクを作成する」の手順

1. 最初にStep Functionsでタスクを作成します。マネジメントコンソールで「Step Functions」の画面を表示して、「今すぐ始める」ボタンをクリックします。
    ![](image.png)

1. 「自分で作成する」ボタンをクリックします。
    ![](image-1.png)

1. ステートマシン名に「Bedrock-StateMachine」と入力し、ステートマシンのタイプを「 Express 」に変更します。「続行」をクリックします。
    ![](image-2.png)

1. 右側のワークフローのステートマシンクエリ言語を「JSONPath」に変更します。
    ![](image-3.png)


P.387の「Workflow Studioの編集画面が表示されるので、」以降を実施してください。

### 変更点２：Stability AI社のSDXL 1.0モデルがEOLのため、Amazon Nova Canvasを使用するよう対応

SDXL 1.0が2025/5/20にEOLになったため、画像生成モデルをAmazon Nova Canvasに変更します。

1. 第2章のP.80を参考にAmazon Nova Canvasを有効化します。

1. P.414の手順が変更
    1. Bedrock model identifierを「arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-canvas-v1:0」に変更します。

    1. 「モデル推論パラメータの入力」に以下の内容を入力します。（[こちら](1_model-parameters/5_アイキャッチ画像を生成_NovaCanvas.json)）

        ```json
        {
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {
                "text.$": "$.Body.content[0].text"
            },
            "imageGenerationConfig": {
                "seed": 0,
                "quality": "standard",
                "height": 1024,
                "width": 1024,
                "numberOfImages": 1
            }
        }
        ```

1. P.421の`1_stepfunctions.py`のコードが一部変更（[こちら](2_cloud9/1_stepfunctions.py)）

    - 変更前：`image_base64 = body["artifacts"][0]["base64"]`
    - 変更後：`image_base64 = body["images"][0]`

### 変更点３：細かな画面項目の変更に対応

- P.387：「Call third-party API」の名称が「Call HTTPS APIs」に変更
- P.389：EventBridgeの設定画面が変更。「認証を設定」セクションをカスタム設定を選択した状態で「APIキー」を選択
- P.398、P.410、P.416：入力タブと出力タブが統合され、「入力/出力」タブに変更