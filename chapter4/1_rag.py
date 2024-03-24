# 外部ライブラリをインポート
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import BedrockChat
from langchain_community.retrievers.bedrock import AmazonKnowledgeBasesRetriever

# 検索手段を指定
retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="XXXXXXXXXX",  # ここにナレッジベースIDを記載する
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 10}},
)

# プロンプトのテンプレートを定義
prompt = ChatPromptTemplate.from_template(
    "以下のcontextに基づいて回答してください: {context} / 質問: {question}"
)

# LLMを指定
model = BedrockChat(
    model_id="anthropic.claude-3-haiku-20240307-v1:0", model_kwargs={"max_tokens": 1000}
)

# チェーンを定義（検索 → プロンプト作成 → LLM呼び出し → 結果を取得）
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# フロントエンドを記述
st.title("おしえて！Bedrock")
question = st.text_input("質問を入力")
button = st.button("質問する")

# ボタンが押されたらチェーン実行結果を表示
if button:
    st.write(chain.invoke(question))
