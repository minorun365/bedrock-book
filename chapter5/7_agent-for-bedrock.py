import uuid

import boto3
import streamlit as st

# Agentの定義
agent_id: str = "XXXXXXX"  # エージェントのIDを入力
agent_alias_id: str = "XXXXXXX"  # エイリアスのIDを入力
session_id: str = str(uuid.uuid1())
client = boto3.client("bedrock-agent-runtime")

st.title("Agents for Amazon Bedrok チャット")

if prompt := st.chat_input("何でも聞いてください。"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Agentの実行
        response = client.invoke_agent(
            inputText=prompt,
            agentId=agent_id,
            agentAliasId=agent_alias_id,
            sessionId=session_id,
            enableTrace=False,
        )

        # Agent実行結果の取得
        event_stream = response["completion"]
        text = ""  # textを初期化
        for event in event_stream:
            if "chunk" in event:
                text += event["chunk"]["bytes"].decode("utf-8")
        st.write(text)
