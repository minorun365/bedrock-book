# Pyhton外部モジュールのインポート
import boto3

# Bedrockクライアントの作成
bedrock = boto3.client("bedrock")

# モデル一覧取得APIの呼び出し
result = bedrock.list_foundation_models()

# Amazon Novaモデルのみのフィルタリング
result = list(filter(lambda x: "Nova" in x["modelName"], result["modelSummaries"]))

# 結果をコンソールに表示
print(result)
