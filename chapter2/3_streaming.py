# Python外部ライブラリのインポート
import json
import boto3

# Bedrockクライアントの作成
bedrock_runtime = boto3.client("bedrock-runtime")

# リクエストボディを定義
body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {"role": "user", "content": [{"type": "text", "text": "いろは歌を教えて"}]}
        ],
    }
)

# モデルを定義（Claude 3 Sonnet）
modelId = "anthropic.claude-3-sonnet-20240229-v1:0"

# レスポンスを定義
response = bedrock_runtime.invoke_model_with_response_stream(body=body, modelId=modelId)

# ストリーミング出力
for event in response.get("body"):
    chunk = json.loads(event["chunk"]["bytes"])
    if (
        chunk["type"] == "content_block_delta"
        and chunk["delta"]["type"] == "text_delta"
    ):
        print(chunk["delta"]["text"], end="")

# ストリーミング終了後に改行
print()
