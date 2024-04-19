from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage


def invoke_bedrock(prompt: str):
    chat = ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        model_kwargs={"max_tokens": 1000},
    )

    messages = [
        SystemMessage(content="あなたのタスクはユーザーの質問に明確に答えることです。"),
        HumanMessage(content=prompt),
    ]

    response = chat.invoke(messages)
    return response.content


def lambda_handler(event, context):
    result = invoke_bedrock("空が青いのはなぜですか？")
    return {"statusCode": 200, "body": result}
