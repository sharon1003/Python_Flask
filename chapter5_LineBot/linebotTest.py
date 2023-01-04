from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('Lao2pZRClh5mwt6s71PTvF7AD05pT0G0DwsyQd45uhTKdFInjSyOzvGsiOXtxPZPoChYjcIKf3VpR+HikbVbrap5eVBsLx814vsBhlyzPEPyOpFigpMaDzE2GT/yOJjHZSP8rK7L3p/A3UZARG2ckAdB04t89/1O/w1cDnyilFU=') # Access token
handler = WebhookHandler('a0e1aedb3fb0d74bb13f28237da3ed64') # Channel secret

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

# from flask import Flask
# app = Flask(__name__)

# from flask import request, abort
# from linebot import  LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import MessageEvent, TextMessage, TextSendMessage

# line_bot_api = LineBotApi('你的 CHANNEL_ACCESS_TOKEN')
# handler = WebhookHandler('你的 CHANNEL_SECRET')

# @app.route("/callback", methods=['POST'])
# def callback():
#     signature = request.headers['X-Line-Signature']
#     body = request.get_data(as_text=True)
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)
#     return 'OK'

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

# if __name__ == '__main__':
#     app.run(port=5050)
