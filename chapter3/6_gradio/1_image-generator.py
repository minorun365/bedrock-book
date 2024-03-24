import base64
import io
import json

import boto3
import gradio as gr
from PIL import Image

client = boto3.client("bedrock-runtime")


def predict(input: str):

    body = {
        "textToImageParams": {"text": input},
        "taskType": "TEXT_IMAGE",
        "imageGenerationConfig": {
            "cfgScale": 8,
            "seed": 0,
            "width": 512,
            "height": 512,
            "numberOfImages": 1,
        },
    }

    response = client.invoke_model(
        modelId="amazon.titan-image-generator-v1", body=json.dumps(body)
    )

    body = json.loads(response.get("body").read())
    image_encoded = body["images"][0]
    image_decoded = base64.decodebytes(bytes(image_encoded, "utf-8"))
    response_image = Image.open(io.BytesIO(image_decoded))

    return response_image


demo = gr.Interface(
    fn=predict, inputs=gr.Textbox(info="プロンプトを入力"), outputs=gr.Image()
)
demo.launch(server_port=8080)
