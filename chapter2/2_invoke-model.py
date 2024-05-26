# Python外部ライブラリをインポート
import json
import boto3

# Bedrockクライアントを作成
bedrock = boto3.client("bedrock-runtime")

# リクエストボディを定義
body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": "Bedrockってどういう意味？",
            }
        ],
    }
)

# モデルを定義（Claude 3 Sonnet）
modelId = "anthropic.claude-3-sonnet-20240229-v1:0"

# HTTPヘッダーを定義
accept = "application/json"
contentType = "application/json"

# レスポンスを定義
response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
response_body = json.loads(response.get("body").read())
answer = response_body["content"][0]["text"]

# 生成されたテキストをコンソールに表示
print(answer)
