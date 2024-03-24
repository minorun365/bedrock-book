# Pyhton外部モジュールのインポート
import boto3

# Bedrockクライアントの作成
bedrock = boto3.client(service_name="bedrock")

# モデル一覧取得APIの呼び出し
result = bedrock.list_foundation_models()

# 結果をコンソールに表示
print(result)
