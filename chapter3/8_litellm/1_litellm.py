import os

from litellm import completion

os.environ["AWS_REGION"] = "us-east-1"


models = [
    "bedrock/anthropic.claude-3-sonnet-20240229-v1:0",
    "bedrock/anthropic.claude-instant-v1",
    "bedrock/amazon.titan-text-lite-v1",
]

for model in models:

    response = completion(
        model=model,
        messages=[{"content": "Hello, how are you?", "role": "user"}],
    )

    print(f"{model} :\n\n{response.choices[0].message.content}\n-----")
