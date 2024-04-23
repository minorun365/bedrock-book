# Pyhton外部モジュールのインポート
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# ChatOpenAIを生成
chat = ChatOpenAI(
    openai_api_key="sk-**********",
    model_name="gpt-3.5-turbo-0125",
)

# メッセージを定義
messages = [
    SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
    HumanMessage(content="空が青いのはなぜですか？"),
]

# モデル呼び出し
response = chat.invoke(messages)

print(response.content)
