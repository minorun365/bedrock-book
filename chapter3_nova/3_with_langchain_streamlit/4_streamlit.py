# Pyhton外部モジュールのインポート
import streamlit as st
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# タイトル
st.title("Bedrock チャット")

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
]

# チャット入力欄を定義
if prompt := st.chat_input("何でも聞いてください。"):
    # ユーザーの入力をメッセージに追加
    messages.append(HumanMessage(content=prompt))

    # ユーザーの入力を画面表示
    with st.chat_message("user"):
        st.markdown(prompt)

    # モデルの呼び出しと結果の画面表示
    with st.chat_message("assistant"):
        st.write_stream(chat.stream(messages))
