# Pyhton外部モジュールのインポート
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# ChatBedrockを生成
chat = ChatBedrock(
    model_id="amazon.nova-pro-v1:0",
    model_kwargs={"max_tokens": 1000},
    streaming=True,
)
# Nova特別対応：出力が生成したテキストになるようにStrOutputParserを追加
chat = chat | StrOutputParser()

# メッセージを定義
messages = [
    SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
    HumanMessage(content="空が青いのはなぜですか？"),
]

# Stream形式でモデル呼び出し
for chunk in chat.stream(messages):
    print(chunk, end="", flush=True)

print("")
