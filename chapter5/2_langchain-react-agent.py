import nest_asyncio
import streamlit as st
from bs4 import BeautifulSoup
from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_react_agent
from langchain_aws import ChatBedrock
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, SystemMessage

nest_asyncio.apply()

search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="duckduckgo-search",
        func=search.run,
        description="このツールはユーザーから検索キーワードを受け取り、Web上の最新情報を検索します。",
    )
]

# チャットモデルの設定
chat = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1500},
)

# エージェントの設定
agent = create_react_agent(chat, tools, prompt=hub.pull("hwchase17/react"))
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

# Streamlit アプリケーションの設定
st.title("Bedrock ReAct Agent チャット")
messages = [SystemMessage(content="あなたは質問に対して必ず日本語で回答します。")]

# ユーザー入力の処理
prompt = st.chat_input("何でも聞いてください。")
if prompt:
    messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        # エージェントを呼び出す
        result = agent_executor.invoke({"input": prompt})
        st.write(result["output"])
