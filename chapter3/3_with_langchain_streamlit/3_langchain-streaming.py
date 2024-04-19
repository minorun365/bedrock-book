from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000},
    streaming=True,
)

messages = [
    SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
    HumanMessage(content="空が青いのはなぜですか？"),
]

for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)

print("")
