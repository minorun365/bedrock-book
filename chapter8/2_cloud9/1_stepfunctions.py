# Pyhton外部モジュールのインポート
import base64
import json
from io import BytesIO

import boto3
import streamlit as st
from PIL import Image

# タイトル
st.title("自己紹介アプリ")


# バケット情報を分割
def split_bucket_info(arn: str):
    from urllib.parse import urlparse

    result = urlparse(arn)
    bucket_name = result.netloc
    key = result.path[1:]
    return bucket_name, key


# 画像ファイルを取得
def get_object(arn: str):
    bucket_name, key = split_bucket_info(arn)

    s3 = boto3.client("s3")
    response = s3.get_object(Bucket=bucket_name, Key=key)

    return json.loads(response["Body"].read().decode("utf-8"))


# 入力フォームを生成
with st.form("form"):
    state_machine_arn = st.text_input("stateMachineArn")
    submit = st.form_submit_button("実行")

# 実行ボタンを押した際の処理
if submit:
    # Step Functionsクライアントを生成
    sfn_client = boto3.client("stepfunctions")

    # ステートマシンを実行
    response = sfn_client.start_sync_execution(stateMachineArn=state_machine_arn)

    # 実行結果を画面に表示
    st.json(response, expanded=False)

    output = json.loads(response["output"])

    for o in output:
        # 自己紹介を画面に表示
        if "Markdown" in o:
            completion = o["Markdown"]["Body"]["content"][0]["text"]
            st.markdown("# " + completion)

        # 画像を画面に表示
        if "Image" in o:
            s3_arn = o["Image"]["Body"]
            body = get_object(s3_arn)
            image_base64 = body["artifacts"][0]["base64"] ## 書籍に記載のSDXL 1.0を使用する場合
            # image_base64 = body["images"][0] ## Amazon Nova Canvasを使用する場合

            st.image(Image.open(BytesIO(base64.b64decode(image_base64))))
