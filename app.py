from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
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
    msg = event.message.text
    r = '我看不懂你說啥'

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    if msg in ['hi', 'Hi']:
        r = '嗨嗨'
    elif msg == '你吃飯了嗎':
        r = '還沒,很忙'
    elif msg == '你是誰':
        r = '我是機器人'
    elif '訂位' in msg:
        r = '你想訂孤支嗎?'
    elif msg == '誰是女神':
        r = '高文均'
    elif msg == '誰是帥哥':
        r = '吳忠頴'
    elif msg in ['哈哈', '哈哈哈', '哈']:
        r = '笑屁'
    elif msg in ['白癡', '白吃', '白痴']:
        r = '妳啊'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()