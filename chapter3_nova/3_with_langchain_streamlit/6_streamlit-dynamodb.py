# Pyhton外部モジュールのインポート
import streamlit as st
from langchain_aws import ChatBedrock
from langchain_community.chat_message_histories import DynamoDBChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# タイトル
st.title("Bedrock チャット")

# セッションIDを定義
if "session_id" not in st.session_state:
    st.session_state.session_id = "session_id"

# セッションに履歴を定義
if "history" not in st.session_state:
    st.session_state.history = DynamoDBChatMessageHistory(
        table_name="BedrockChatSessionTable", session_id=st.session_state.session_id
    )

# セッションにChainを定義
if "chain" not in st.session_state:
    # プロンプトを生成
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "あなたのタスクはユーザーの質問に明確に答えることです。"),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="human_message"),
        ]
    )

    # ChatBedrockを生成
    chat = ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        model_kwargs={"max_tokens": 1000},
        streaming=True,
    )

    # Chainを生成
    chain = prompt | chat
    # Nova特別対応：出力が生成したテキストになるようにStrOutputParserを追加
    chain = chain | StrOutputParser()
    st.session_state.chain = chain

# 履歴クリアボタンを画面表示
if st.button("履歴クリア"):
    st.session_state.history.clear()

# メッセージを画面表示
for message in st.session_state.history.messages:
    with st.chat_message(message.type):
        st.markdown(message.content)

# チャット入力欄を定義
if prompt := st.chat_input("何でも聞いてください。"):
    # ユーザーの入力をメッセージに追加
    with st.chat_message("user"):
        st.markdown(prompt)

    # モデルの呼び出しと結果の画面表示
    with st.chat_message("assistant"):
        response = st.write_stream(
            st.session_state.chain.stream(
                {
                    "messages": st.session_state.history.messages,
                    "human_message": [HumanMessage(content=prompt)],
                },
                config={"configurable": {"session_id": st.session_state.session_id}},
            )
        )

    # 履歴に追加
    st.session_state.history.add_user_message(prompt)
    st.session_state.history.add_ai_message(response)
