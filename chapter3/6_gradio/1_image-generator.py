import base64
import io
import json

import boto3
import gradio as gr
from PIL import Image

client = boto3.client("bedrock-runtime")


def predict(input: str):

    body = {
        "text_prompts": [{"text": input, "weight": 1}],
        "cfg_scale": 10,
        "seed": 0,
        "steps": 50,
        "width": 1024,
        "height": 1024,
    }

    response = client.invoke_model(
        modelId="stability.stable-diffusion-xl-v1", body=json.dumps(body)
    )

    body = json.loads(response.get("body").read())
    image_encoded = body["artifacts"][0]["base64"]
    image_decoded = base64.decodebytes(bytes(image_encoded, "utf-8"))
    response_image = Image.open(io.BytesIO(image_decoded))

    return response_image


demo = gr.Interface(
    fn=predict, inputs=gr.Textbox(info="プロンプトを入力"), outputs=gr.Image()
)
demo.launch(server_port=8080)
