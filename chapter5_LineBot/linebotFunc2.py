# linebotFunc2.py

from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, AudioSendMessage, VideoSendMessage

line_bot_api = LineBotApi('MhWxNZOKv1uIJ7b52XvIiVwN+EUatLpNDnrSp5u8h9HKSL1yx1S5MrheF8ogrIbB4ApjbHNboRdjOi4GZe2CVW8synrF6Ed5+Viw2Gjc4Iop1mMVff2llQYfT8bI6z4YAz5lkmRlAACp6h5MzEYfFgdB04t89/1O/w1cDnyilFU=') # Access token
handler = WebhookHandler('dcc1a1faa43cfc38f3a080b33d18641d') # Channel secret


@app.route("/callback", methods=['POST']) # 建立callback路由，檢查Line Bot的資料是否正確
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

baseurl = 'https://8e7e-140-122-21-160.jp.ngrok.io/static/'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	mtext = event.message.text # 獲取原本的資料
	if mtext == '@傳送聲音':
		try:
			message = AudioSendMessage(
				original_content_url = baseurl + 'mario.m4a',
				duration = 20000 # 豪秒，聲音長度20秒
			)
			line_bot_api.reply_message(event.reply_token, message)
		except:
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))
	
	elif mtext == '@傳送影片':
		try:
			message = VideoSendMessage(
				original_content_url = baseurl + 'robot.mp4',
				preview_image_url = baseurl + 'robot.jpg'
			)
			line_bot_api.reply_message(event.reply_token, message)
		except:
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

if __name__ == '__main__':
	app.run(port=5050)