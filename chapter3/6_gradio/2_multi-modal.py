# Pyhton外部モジュールのインポート
import base64
import json
import mimetypes

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
                        "type": "text",
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
                        "type": "text",
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
        mime_type = mimetypes.guess_type(path)[0]

        content.append(
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": mime_type,
                    "data": file_base64(path),
                },
            },
        )

    # テキストを追加
    content.append(
        {
            "type": "text",
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
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        body=json.dumps(
            {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 300,
                "messages": messages,
            }
        ),
    )

    # 呼び出し結果を画面に表示
    response_text = ""
    for event in response.get("body"):
        chunk = json.loads(event["chunk"]["bytes"])
        if "delta" in chunk and "text" in chunk["delta"]:
            response_text = response_text + chunk["delta"]["text"]
            yield response_text


# 画面項目を生成
demo = gr.ChatInterface(chatbot, multimodal=True)
demo.launch(server_port=8080)
