# Pyhton外部モジュールのインポート
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage


# Bedrock呼び出し関数
def invoke_bedrock(prompt: str):
    # ChatBedrockを生成
    chat = ChatBedrock(
        model_id="amazon.nova-pro-v1:0",
        model_kwargs={"max_tokens": 1000},
    )

    # メッセージを定義
    messages = [
        SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
        HumanMessage(content=prompt),
    ]

    # モデル呼び出し
    response = chat.invoke(messages)
    return response.content


# Lambda実行時に呼ばれる関数
def lambda_handler(event, context):
    result = invoke_bedrock("空が青いのはなぜですか？")
    return {"statusCode": 200, "body": result}
