import json

import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    url = "https://aws.amazon.com/jp/blogs/aws/"

    # リクエストを送信してHTMLを取得
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 最新の記事を1件取得
    articles = soup.select("article.blog-post")[:1]

    result = []
    for article in articles:
        title = article.select_one("h2.blog-post-title").text.strip()
        link = article.select_one("h2.blog-post-title a")["href"]
        date = article.select_one("footer.blog-post-meta").text.strip()


        result.append({"title": title, "link": link, "date": date})

    contents = json.dumps(result, ensure_ascii=False)

    response_body = {"application/json": {"body": contents}}
    action_response = {
        "actionGroup": event["actionGroup"],
        "apiPath": event["apiPath"],
        "httpMethod": event["httpMethod"],
        "httpStatusCode": 200,
        "responseBody": response_body,
    }
    api_response = {"messageVersion": "1.0", "response": action_response}

    return api_response
