# insert.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123456@127.0.0.1:5432/testdb'
db = SQLAlchemy(app)

class students(db.Model):
	__tablename__ = 'students'
	sid = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), nullable = False)
	tel = db.Column(db.String(50))
	address = db.Column(db.String(200))
	email = db.Column(db.String(100))

	def __init__(self, name, tel, addr, email):
			self.name = name
			self.tel = tel
			self.addr = addr
			self.emaiil = email

@app.route('/')
def index():
	db.create_all()
	return "資料庫連線成功！"

@app.route('/insert')
def insert():
	student = students('綠谷出久', '0987654321', '台北市信義路101號', 'midoriya@test.com')
	db.session.add(student)
	db.session.commit()
	return "資料庫新增成功！"

@app.route('/insertall')
def insertall():
	datas = [
			students('爆豪', '0987654321', '台北市信義路101號', 'midoliya@test.com'),
			students('轟焦凍', '1234567890', '台北市信義路1號', 'todoroki@test.com')
	]
	db.session.add_all(datas)
	db.session.commit()
	return "資料庫批次新增成功！"


if __name__ == '__main__':
	app.run(debug = True)

