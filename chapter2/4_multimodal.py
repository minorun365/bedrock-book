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
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image_data,
                    },
                },
                {"type": "text", "text": "この画像は何？日本語で説明して"},
            ],
        }
    ],
}

# Bedrock呼び出しパラメーターの定義
body = json.dumps(prompt_config)
modelId = "anthropic.claude-3-sonnet-20240229-v1:0"
accept = "application/json"
contentType = "application/json"

# レスポンスの取得
response = bedrock_runtime.invoke_model(
    body=body, modelId=modelId, accept=accept, contentType=contentType
)
response_body = json.loads(response.get("body").read())
results = response_body.get("content")[0].get("text")

# 生成テキストをコンソールに出力
print(results)
