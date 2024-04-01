# Python外部ライブラリをインポート
import boto3
import streamlit as st

# フロントエンドを記述
st.title("おしえて！Bedrock")
question = st.text_input("質問を入力")
button = st.button("質問する")

# Bedrockクライアントを作成
kb = boto3.client("bedrock-agent-runtime")

# ボタンが押されたらナレッジベースを呼び出し
if button:
    
    # ナレッジベースを定義
    response = kb.retrieve_and_generate(
        input={"text": question},
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": "XXXXXXXXXX",  # ナレッジベースID
                "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0",
            },
        },
    )

    # RAG結果を画面に表示
    st.write(response["output"]["text"])
