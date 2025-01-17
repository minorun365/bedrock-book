# Pyhton外部モジュールのインポート
import base64
import json
import os

import boto3
import gradio as gr

# Bedrockクライアントを生成
client = boto3.client("bedrock-runtime")


# 画像ファイルの読み込み関数
def file_base64(path: str):
    with open(path, mode="rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    return data


# メッセージを作成する関数
def create_message(message: dict, history: list):
    messages = []

    # 履歴をメッセージに追加
    for conversation in history:
        if type(conversation[0]) is tuple:
            # 添付ファイルの場合は追加しない
            continue

        user_message = conversation[0]
        assistant_message = conversation[1]

        # ユーザープロンプト
        messages.append(
            {
                "role": "user",
                "content": [
                    {
                        "text": user_message,
                    }
                ],
            }
        )

        # アシスタントプロンプト
        messages.append(
            {
                "role": "assistant",
                "content": [
                    {
                        "text": assistant_message,
                    }
                ],
            }
        )

    # 最新のメッセージ
    text = message["text"]
    files = message["files"]

    content = []

    # 添付ファイルを追加
    for file in files:
        path = file
        _, ext = os.path.splitext(path)
        format = ext[1:].lower()
        
        content.append(
            {
                "image": {
                    "format": format,
                    "source": {
                        "bytes": file_base64(path),
                    },
                }
            },
        )

    # テキストを追加
    content.append(
        {
            "text": text,
        }
    )

    # 最新のメッセージをユーザープロンプトとして追加
    messages.append(
        {
            "role": "user",
            "content": content,
        }
    )
    return messages


# チャットメッセージ送信時に呼ばれる関数
def chatbot(message: dict, history: list):
    # メッセージを生成
    messages = create_message(message, history)

    # モデル呼び出し
    response = client.invoke_model_with_response_stream(
        modelId="amazon.nova-pro-v1:0",
        body=json.dumps(
            {
                "messages": messages,
                "inferenceConfig": {"max_new_tokens": 300}
            }
        ),
    )

    # 呼び出し結果を画面に表示
    response_text = ""
    for event in response.get("body"):
        chunk = json.loads(event["chunk"]["bytes"])
        if "contentBlockDelta" in chunk:
            response_text = response_text + chunk["contentBlockDelta"]["delta"]["text"]
            yield response_text


# 画面項目を生成
demo = gr.ChatInterface(chatbot, multimodal=True)
demo.launch(server_name="0.0.0.0", server_port=8080)
