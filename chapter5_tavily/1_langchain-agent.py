import os
import nest_asyncio
import streamlit as st
from bs4 import BeautifulSoup
from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_xml_agent
from langchain_aws import ChatBedrock
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, SystemMessage

nest_asyncio.apply()

# Web ページの内容を読み込む関数
def web_page_reader(url: str) -> str:
    loader = WebBaseLoader(url)
    content = loader.load()[0].page_content
    return content

# 検索ツールと Web ページ読み込みツールの設定
tavily_api_key = os.environ.get('TAVILY_API_KEY')
search = TavilySearchResults(max_results=3, tavily_api_key=tavily_api_key)
tools = [
    Tool(
        name="tavily-search",
        func=search.run,
        description="このツールはユーザーから検索キーワードを受け取り、Web上の最新情報を検索します。",
    ),
    Tool(
        name="WebBaseLoader",
        func=web_page_reader,
        description="このツールはユーザーからURLを渡された場合に内容をテキストを返却します。URLの文字列のみを受け付けます。",
    ),
]

# チャットモデルの設定
chat = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1500},
)

# エージェントの設定
agent = create_xml_agent(chat, tools, prompt=hub.pull("hwchase17/xml-agent-convo"))

agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

# Streamlit アプリケーションの設定
st.title("Bedrock Agent チャット")
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
