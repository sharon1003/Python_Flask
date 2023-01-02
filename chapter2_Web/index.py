from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return '歡迎來到首頁！'

@app.route('/hello')
def hello():
	return '歡迎來到頁面'

if __name__ == '__main__':
	app.run()
