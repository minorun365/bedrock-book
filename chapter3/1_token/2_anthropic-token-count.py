from anthropic import Anthropic

client = Anthropic()

tokens = client.count_tokens("Amazon BedrockはAWSの生成AIサービスです。")
print(tokens)

tokens = client.count_tokens("Amazon Bedrock is an AWS generative AI service")
print(tokens)
