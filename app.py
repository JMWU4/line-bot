from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('PygaOkiL9Bh2756JaBGu8u8yEyaO/d9tidRvWdMxitd9oCAD6V/CVXYM6SALvrKTthBq5f1aIq9HTsjDMq1f5MXsQDjqv95+azKThuaQRm6cK6hcmlmuFtDoZCwXCkzn8v4TcSXb+M4tcHXi5MXdEgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a5d60f6825cc46365f5dd3932b94f708')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()