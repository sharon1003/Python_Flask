# show.py
from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime


app = Flask(__name__)

@app.route('/show')
def show():
	person1 = {"name":"Emliy", "phone":"0956158888", "age":"27"}
	person2 = {"name":"Kelly", "phone":"0975925137", "age":"23"}
	person3 = {"name":"James", "phone":"0987654321", "age":"20"}
	persons = [person1, person2, person3]
	return render_template('show.html', **locals())

if __name__ == '__main__':
	app.run()
