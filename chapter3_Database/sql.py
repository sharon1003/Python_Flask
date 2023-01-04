# sql.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123456@127.0.0.1:5432/testdb'
db = SQLAlchemy(app)

# 上面跟之前的一樣
@app.route('/setup')
def setup():
	sql = """
		CREATE TABLE students2(
		sid serial NOT NULL,
		name character varying(50) NOT NULL,
		tel character varying(50),
		address character varying(200),
		email character varying(100),
		PRIMARY KEY(sid))
		"""
	db.engine.execute(sql)
	return "資料表建立成功"

@app.route('/insert')
def insert():
	sql = """
		INSERT INTO students2(name, tel, address, email) VALUES
		('綠谷出久', '0987654321', 'Japan', 'midoriya@test.com');
		INSERT INTO students2(name, tel, address, email) VALUES
		('爆豪勝己', '0987654321', 'Japan', 'bokuho@test.com');
		INSERT INTO students2(name, tel, address, email) VALUES
		('轟焦凍', '0987654321', 'Japan', 'todoroki@test.com');
		"""
	db.engine.execute(sql)
	return "資料新增成功！"

@app.route('/query')
def query():
	sql = "SELECT * FROM students2 ORDER BY sid DESC"
	students = db.engine.execute(sql)
	msg = ""
	for student in students:
		msg += f"{student['name']}, {student['tel']}, {student['address']}, {student['email']}<br>"
	return msg

@app.route('/updateusr/<int:uid>')
def updateusr(uid):
	sql = "UPDATE students2 SET tel = '098761234' WHERE sid = " + str(uid)
	db.engine.execute(sql)
	return "資料修改成功！"

@app.route('/deleusr/<int:uid>')
def deleusr(uid):
	sql = "DELETE FROM students2 WHERE sid = " + str(uid)
	db.engine.execute(sql)
	return "資料刪除成功"

if __name__ == '__main__':
	app.run(debug = True)
