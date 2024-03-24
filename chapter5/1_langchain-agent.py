import streamlit as st
from langchain.agents import AgentExecutor, Tool, create_xml_agent
from langchain.prompts.prompt import PromptTemplate
from langchain_community.callbacks import StreamlitCallbackHandler
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_community.chat_models import BedrockChat
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Web ページの内容を読み込む関数
def web_page_reader(url: str) -> str:
    loader = WebBaseLoader(url)
    content = loader.load()[0].page_content
    return content

# 検索ツールと Web ページ読み込みツールの設定
search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="duckduckgo-search",
        func=search.run,
        description="このツールはWeb上の最新情報を検索します。ユーザから検索キーワードを受け取ります。最新情報が必要ない場合はこのツールは使用しません。",
    ),
    Tool(
        name="WebBaseLoader",
        func=web_page_reader,
        description="このツールはユーザからURLを渡された場合に内容をテキストを返却します。URLの文字列のみを受け付けます。",
    ),
]

# チャットモデルの設定
chat = BedrockChat(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000},
    streaming=True,
)

# プロンプトテンプレートの設定
prompt = PromptTemplate(
    template="""
    以下の質問に対して回答してください。回答には上記のツールを適切に使用してください。

    ツール:
    {tools}

    現在のメモ:
    {agent_scratchpad}

    質問:
    {input}
    """,
    input_variables=["input", "agent_scratchpad", "tools"],
)

# チャット履歴の設定
chat_history = StreamlitChatMessageHistory(key="chat_messages")

# チャット履歴の表示
for chat in chat_history.messages:
    st.chat_message(chat.type).write(chat.content)

# エージェントの設定
agent = create_xml_agent(chat, tools, prompt=prompt)
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

# Streamlit アプリケーションの設定
st.title("Bedrock Agent チャット")
messages = [SystemMessage(content="あなたは質問に対して必ず日本語で回答します。")]

# ユーザー入力の処理
if prompt := st.chat_input("何でも聞いてください。"):
    messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())

        result = agent_executor.invoke(
            {"input": prompt, "chat_history": chat_history.messages},
            {"callbacks": [st_callback]},
        )
        st.write(result["output"])

    chat_history.add_messages(
        [
            HumanMessage(content=prompt),
            AIMessage(content=result["output"]),
        ]
    )
