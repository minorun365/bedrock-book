import asyncio

import nest_asyncio
import streamlit as st
from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_react_agent
from langchain.prompts.prompt import PromptTemplate
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_community.chat_models import BedrockChat
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import AIMessage, HumanMessage

nest_asyncio.apply()

search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="duckduckgo-search",
        func=search.run,
        description="このツールはWeb上の最新情報を検索します。ユーザから検索キーワードを受け取ります。最新情報が必要ない場合はこのツールは使用しません。",
    )
]

# チャットモデルの設定
chat = BedrockChat(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000},
    streaming=True,
)

prompt = hub.pull("hwchase17/react")

# エージェントの設定
agent = create_react_agent(chat, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

# Streamlit アプリケーションの設定
st.title("Bedrock ReAct Agent チャット")

async def run_agent(prompt):
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        result = await agent_executor.ainvoke({"input": prompt})
        st.write(result["output"])

if prompt := st.chat_input("何でも聞いてください。"):
    with st.chat_message("user"):
        st.markdown(prompt)

    asyncio.run(run_agent(prompt))
