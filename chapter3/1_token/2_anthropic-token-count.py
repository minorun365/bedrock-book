# Pyhton外部モジュールのインポート
from anthropic import Anthropic

# クライアントの生成
client = Anthropic()

# トークン数を取得（日本語文字列）
tokens = client.count_tokens("Amazon BedrockはAWSの生成AIサービスです。")
print(tokens)

# トークン数を取得（英語文字列）
tokens = client.count_tokens("Amazon Bedrock is an AWS generative AI service")
print(tokens)
