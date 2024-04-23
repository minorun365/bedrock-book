# Pyhton外部モジュールのインポート
import json

import boto3

# Bedrockクライアントを生成
client = boto3.client("bedrock-runtime")

# ユーザープロンプト
user_prompt = "HTMLの雛形を書いて"
# アシスタントプロンプト
assistant_prompt = "<!DOCTYPE html>"

# リクエストボディを定義
body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "messages": [
        {"role": "user", "content": [{"type": "text", "text": user_prompt}]},
        {"role": "assistant", "content": [{"type": "text", "text": assistant_prompt}]},
    ],
}

# モデル呼び出し
response = client.invoke_model(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0", body=json.dumps(body)
)

# レスポンスから必要な情報を取得
response_body = json.loads(response["body"].read())
assistant_text = response_body["content"][0]["text"]

print(assistant_text)
