from langchain.globals import set_debug
from langchain_community.chat_models import BedrockChat
from langchain_core.messages import HumanMessage, SystemMessage

set_debug(True)

chat = BedrockChat(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000},
)

messages = [
    SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
    HumanMessage(content="空が青いのはなぜですか？"),
]

response = chat.invoke(messages)

print(response.content)
