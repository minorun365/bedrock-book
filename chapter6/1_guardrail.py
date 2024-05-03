# Python外部ライブラリをインポート
import json
import boto3

# Bedrockクライアントを作成
bedrock = boto3.client("bedrock-runtime")

# リクエストボディを定義
body = json.dumps(
   {
       "anthropic_version": "bedrock-2023-05-31",
       "max_tokens": 1024,
       "messages": [
           {"role": "user",
            "content": [{"type": "text", "text": "生成AIって何？"}]}
       ],
   }
)

# レスポンスを定義
response = bedrock.invoke_model(
   body=body,
   modelId="anthropic.claude-3-sonnet-20240229-v1:0",
   guardrailIdentifier="XXXXXXXXXX", #ここにガードレールのIDを記載する
   guardrailVersion="1", #ここにガードレールのバージョンを記載する
)

# 生成されたテキストをコンソールに表示
output = json.loads(response.get("body").read())["content"][0]["text"]
print(output)
