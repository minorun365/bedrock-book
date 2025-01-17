# Pyhton外部モジュールのインポート
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

# ChatBedrockを生成
chat = ChatBedrock(
    model_id="amazon.nova-pro-v1:0",
    model_kwargs={"max_tokens": 1000},
)

# メッセージを定義
messages = [
    SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
    HumanMessage(content="空が青いのはなぜですか？"),
]

# モデル呼び出し
response = chat.invoke(messages)

print(response.content)
