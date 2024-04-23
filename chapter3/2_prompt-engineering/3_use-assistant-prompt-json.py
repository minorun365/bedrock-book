# Pyhton外部モジュールのインポート
import json

import boto3

# Bedrockクライアントを生成
client = boto3.client("bedrock-runtime")

# ユーザープロンプト
user_prompt = """あなたのタスクは文書から必要な情報をピックアップすることです。
<document></document>タグの内容はAWSのニュース記事からの引用です。

<document>
Meta Llama 2, Cohere Command Light, and Amazon Titan FMs can now be fine-tuned in Amazon Bedrock
Posted On: Nov 28, 2023

Amazon Bedrock is an easy way to build and scale generative AI applications with leading foundation models (FMs). Amazon Bedrock now supports fine-tuning for Meta Llama 2 and Cohere Command Light, along with Amazon Titan Text Lite and Amazon Titan Text Express FMs, so you can use labeled datasets to increase model accuracy for particular tasks.

Organizations with small, labeled datasets that want to specialize a model for a specific task use a process called fine-tuning, which adapts the model’s parameters to produce outputs that are more specific to their business. Parameters represent what the model has learned during training, and adjusting them can refine the model’s knowledge and capabilities to make decisions within an organization’s context. Using a small number of labeled examples in Amazon S3, you can fine-tune a model without having to annotate large volumes of data. Bedrock makes a separate copy of the base foundation model that is accessible only by you and trains this private copy of the model. None of your content is used to train the original base models. You can configure your Amazon VPC settings to access Amazon Bedrock APIs and provide model fine-tuning data in a secure manner.
Meta Llama 2, Cohere Command Light, and Amazon Titan Text FMs can now be fine-tuned in Amazon Bedrock in the US East (N. Virginia) and US West (Oregon) AWS Regions. To learn more, read the AWS News launch blog, Amazon Bedrock product page, and documentation. To get started with fine-tuning in Amazon Bedrock, visit the Amazon Bedrock console.
</document>

タイトル、発表日、概要をJSON形式で出力してください。
"""
# アシスタントプロンプト
assistant_prompt = "{"

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
