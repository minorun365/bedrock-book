# Pyhton外部モジュールのインポート
from ai21_tokenizer import Tokenizer

# トークナイザーの生成
tokenizer = Tokenizer.get_tokenizer()

# トークナイザーでテキストをエンコードし、長さを出力（日本語文字列）
encoded_text = tokenizer.encode("Amazon BedrockはAWSの生成AIサービスです。")
print(len(encoded_text))

# トークナイザーでテキストをエンコードし、長さを出力（英語文字列）
encoded_text = tokenizer.encode("Amazon Bedrock is an AWS generative AI service")
print(len(encoded_text))
