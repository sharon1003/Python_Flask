# linebotFunc1.py

from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

line_bot_api = LineBotApi('+5hl+pZjbHxjlAd9CY9p+YsqRZK2Eg/AjGyFo3+91bxPr7cpV/hhCeAEcfdiljM2+A3i+BZsuPykZ0bbvjy0bz0JfB6aLgc77XzkZaEI7N29rckTCzLdcMcSiJIZEWyZBT3IgTUjxLpDj0X+OThz+gdB04t89/1O/w1cDnyilFU=') # Access token
handler = WebhookHandler('c8f2391102eeda18eefff15e33582ae1') # Channel secret


@app.route("/callback", methods=['POST']) # 建立callback路由，檢查Line Bot的資料是否正確
def callback():
	signature = request.headers['X-Line-Signature']
	body = request.get_data(as_text=True)
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	mtext = event.message.text # 獲取原本的資料
	if mtext == '@傳送文字':
		try:
			message = TextSendMessage(
				text = "Hi, I am Line Bot, How are you?"
			)
			line_bot_api.reply_message(event.reply_token, message)
		except:
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))
	
	elif mtext == '@傳送圖片':
		try:
			message = ImageSendMessage(
				original_content_url = "https://i.imgur.com/YZh2rN5.jpeg",
				preview_image_url = "https://i.imgur.com/YZh2rN5.jpeg"
			)
			line_bot_api.reply_message(event.reply_token, message)
		except:
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))
	
	elif mtext == '@傳送貼圖':
		try:
			message = StickerSendMessage(
				package_id = '11539',
				sticker_id = '52114118'
			)
			line_bot_api.reply_message(event.reply_token, message)
		except:
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

	elif mtext == '@多項傳送':
		try:
			message = [
				StickerSendMessage(
					package_id = '11539',
					sticker_id = '52114118'
				),
				TextSendMessage(
					text = '可愛吧'
				),
				ImageSendMessage(
					original_content_url = "https://i.imgur.com/YZh2rN5.jpeg",
					preview_image_url = "https://i.imgur.com/YZh2rN5.jpeg"
				),
			]
			line_bot_api.reply_message(event.reply_token, message)
		except:
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))
	elif mtext == '@傳送位置':
		try:
			message = LocationSendMessage(
				title = '101大樓',
				address = '台北市信義路五段7號',
				latitude = 25.034207,
				longitude = 121.564590 
			)
			line_bot_api.reply_message(event.reply_token, message)
		except:
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))
	elif mtext == '@快速選單':
		try:
			message = TextSendMessage(
				text = '請選擇最喜歡的程式語言',
				quick_reply = QuickReply(
					items = [
						QuickReplyButton(
							action = MessageAction(label='Python', text='Python')
						),
						QuickReplyButton(
							action = MessageAction(label='Java', text='Java')
						),
						QuickReplyButton(
							action = MessageAction(label='C#', text='C#')
						),
						QuickReplyButton(
							action = MessageAction(label='Basic', text='Basic')
						),
					]
				)
			)
			line_bot_api.reply_message(event.reply_token, message)
		except:
			line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤'))

if __name__ == '__main__':
	app.run(port=5050)