from typing import List

import chainlit as cl
from langchain.document_loaders.text import TextLoader
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document, StrOutputParser
from langchain_community.chat_models import BedrockChat


@cl.on_chat_start
async def on_chat_start():
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "あなたはドキュメントを参照し、ユーザーのタスクを達成することです。 <document>{document}</document>",
            ),
            ("human", "{question}"),
        ]
    )

    model = BedrockChat(
        model_id="anthropic.claude-3-haiku-20240307-v1:0",
        model_kwargs={"max_tokens": 300},
        streaming=True,
    )

    chain = prompt | model | StrOutputParser()

    cl.user_session.set("chain", chain)


@cl.step
async def load_text(path: str) -> List[Document]:
    loader = TextLoader(path, encoding="UTF-8")
    return loader.load()


@cl.on_message
async def on_message(message: cl.Message):
    msg = cl.Message(content="")

    doc = []
    for e in message.elements:
        doc.append(await load_text(e.path))

    chain = cl.user_session.get("chain")

    async for chunk in chain.astream(
        input={"question": message.content, "document": doc}
    ):
        await msg.stream_token(chunk)

    await msg.send()
