from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('') # Access token
handler = WebhookHandler('') # Channel secret

@app.route("/callback", methods=['POST']) # 建立callback路由，檢查Line Bot的資料是否正確
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

@handler.add(MessageEvent, message=TextMessage) # 如果接受到使用者的訊息，就將街道的文字訊息傳回。
def handle_message(event):
	line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))


if __name__ == '__main__':
	app.run(port=5050)