from ai21_tokenizer import Tokenizer

tokenizer = Tokenizer.get_tokenizer()

encoded_text = tokenizer.encode("Amazon BedrockはAWSの生成AIサービスです。")
print(len(encoded_text))

encoded_text = tokenizer.encode("Amazon Bedrock is an AWS generative AI service")
print(len(encoded_text))
