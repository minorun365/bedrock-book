import json

import boto3

client = boto3.client("bedrock-runtime")

user_prompt = "HTMLの雛形を書いて"

body = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "messages": [{"role": "user", "content": [{"type": "text", "text": user_prompt}]}],
}

response = client.invoke_model(
    modelId="anthropic.claude-3-sonnet-20240229-v1:0", body=json.dumps(body)
)

response_body = json.loads(response["body"].read())
assistant_text = response_body["content"][0]["text"]

print(assistant_text)
