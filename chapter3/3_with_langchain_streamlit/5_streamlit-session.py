import streamlit as st
from langchain_community.chat_models import BedrockChat
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

st.title("Bedrock チャット")

chat = BedrockChat(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000},
    streaming=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
    ]

for message in st.session_state.messages:
    if message.type != "system":
        with st.chat_message(message.type):
            st.markdown(message.content)

if prompt := st.chat_input("何でも聞いてください。"):
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(chat.stream(st.session_state.messages))
    st.session_state.messages.append(AIMessage(content=response))
