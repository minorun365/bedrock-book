# 新しい「Converse API」を使う場合、「3_streaming.py」を以下のように書き換えます。
# モデルが変わっても同じフォーマットでストリーミング推論が可能です。

# Python外部ライブラリのインポート
import boto3

# Bedrockクライアントの作成
bedrock_runtime = boto3.client("bedrock-runtime")

# リクエストボディを定義
inference_config = {"maxTokens": 1000}
messages = [{
    "role": "user",
    "content": [{"text": "いろは歌を教えて"}]
}]

# モデルを定義（Claude 3 Sonnet）
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

# レスポンスを定義
response = bedrock_runtime.converse_stream(
    modelId=model_id,
    inferenceConfig=inference_config,
    messages=messages,
)

# ストリーミング出力
for chunk in response["stream"]:
    if "contentBlockDelta" in chunk:
        text = chunk["contentBlockDelta"]["delta"]["text"]
        print(text, end="")

# ストリーミング終了後に改行
print()