# Pyhton外部モジュールのインポート
import os

from litellm import completion

# AWSリージョンを指定
os.environ["AWS_REGION"] = "us-east-1"

# 呼び出し対象の生成AIモデルを定義
models = [
    "bedrock/amazon.nova-pro-v1:0",
    "bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
    "bedrock/anthropic.claude-instant-v1",
    "bedrock/amazon.titan-text-lite-v1",
]

for model in models:

    # モデルの呼び出し
    response = completion(
        model=model,
        messages=[{"content": "Hello, how are you?", "role": "user"}],
    )

    # 呼び出し結果の表示
    print(f"{model} :\n\n{response.choices[0].message.content}\n-----")
