import json

import boto3

client = boto3.client("bedrock-runtime")

user_prompt = """あなたのタスクは料理のレシピを考えることです。

1. 料理を考え、<タイトル></タイトル>タグで出力します。
2. 料理の材料を考え、<材料></材料>タグで出力します。
3. 料理の手順を考え、<手順></手順>タグで出力します。

パスタのレシピを考えて
"""
stop_sequences = "</材料>"

body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "messages": [{"role": "user", "content": [{"type": "text", "text": user_prompt}]}],
    "stop_sequences": [stop_sequences],
}

response = client.invoke_model(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0", body=json.dumps(body)
)

response_body = json.loads(response["body"].read())
assistant_text = response_body["content"][0]["text"]

print(assistant_text)
