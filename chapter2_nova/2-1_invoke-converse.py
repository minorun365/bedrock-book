# 新しい「Converse API」を使う場合、「2_invoke-model.py」を以下のように書き換えます。
# モデルが変わっても同じフォーマットで推論が可能です。

# Python外部ライブラリのインポート
import boto3

# Bedrockクライアントの作成
bedrock_runtime = boto3.client("bedrock-runtime")

# リクエストボディを定義
inference_config = {"maxTokens": 1000}
messages = [{
    "role": "user",
    "content": [{"text": "Bedrockってどういう意味？"}]
}]

# モデルを定義（Amazon Nova Pro）
model_id = "amazon.nova-pro-v1:0"

# レスポンスを定義
response = bedrock_runtime.converse(
    modelId=model_id,
    inferenceConfig=inference_config,
    messages=messages,
)
answer = response["output"]["message"]["content"][0]["text"]

# 生成されたテキストをコンソールに表示
print(answer)