import streamlit as st
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

st.title("Bedrock チャット")

chat = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000},
    streaming=True,
)

messages = [
    SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
]

if prompt := st.chat_input("何でも聞いてください。"):
    messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        st.write_stream(chat.stream(messages))
