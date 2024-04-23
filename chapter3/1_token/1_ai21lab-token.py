# Pyhton外部モジュールのインポート
from ai21_tokenizer import Tokenizer

# トークナイザーの生成
tokenizer = Tokenizer.get_tokenizer()

text = "Amazon BedrockはAWSの生成AIサービスです。"

# トークナイザーでテキストをエンコード
encoded_text = tokenizer.encode(text)
# トークンごとに分割
tokens = tokenizer.convert_ids_to_tokens(encoded_text)

print(tokens)
