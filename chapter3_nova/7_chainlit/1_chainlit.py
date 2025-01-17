# Pyhton外部モジュールのインポート
from typing import List

import chainlit as cl
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document, StrOutputParser
from langchain_aws import ChatBedrock
from langchain_community.document_loaders import TextLoader


# チャットセッション開始時の処理
@cl.on_chat_start
async def on_chat_start():
    # プロンプトを生成
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "あなたはドキュメントを参照し、ユーザーのタスクを達成することです。 <document>{document}</document>",
            ),
            ("human", "{question}"),
        ]
    )

    # ChatBedrockを生成
    model = ChatBedrock(
        model_id="amazon.nova-pro-v1:0",
        model_kwargs={"max_new_tokens": 300},
        streaming=True,
    )

    # Chainを生成
    chain = prompt | model | StrOutputParser()

    cl.user_session.set("chain", chain)


# テキストファイル読み込み処理
@cl.step
async def load_text(path: str) -> List[Document]:
    loader = TextLoader(path, encoding="UTF-8")
    return loader.load()


# メッセージ受信時の処理
@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="")

    # 添付ファイルの取得
    doc = []
    for e in message.elements:
        doc.append(await load_text(e.path))

    # Chainの取得
    chain = cl.user_session.get("chain")

    # モデルの呼び出しと結果の画面表示
    async for chunk in chain.astream(
        input={"question": message.content, "document": doc}
    ):
        await msg.stream_token(chunk)

    await msg.send()
