# Python外部ライブラリのインポート
import base64
import json
import boto3

# Bedrock呼び出し用クライアントの作成
bedrock_runtime = boto3.client("bedrock-runtime")

# 画像ファイルの変換
with open("image.png", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

# プロンプトの定義
prompt_config = {
    "messages": [
        {
            "role": "user",
            "content": [
                {"image": {"format": "png", "source": {"bytes": image_data}}},
                {"text": "この画像は何？日本語で説明して"},
            ],
        }
    ],
    "inferenceConfig": {"max_new_tokens": 1000},
}

# Bedrock呼び出しパラメーターの定義
body = json.dumps(prompt_config)
modelId = "amazon.nova-pro-v1:0"
accept = "application/json"
contentType = "application/json"

# レスポンスの取得
response = bedrock_runtime.invoke_model(
    body=body, modelId=modelId, accept=accept, contentType=contentType
)
response_body = json.loads(response.get("body").read())
results = response_body["output"]["message"]["content"][0]["text"]

# 生成テキストをコンソールに出力
print(results)
