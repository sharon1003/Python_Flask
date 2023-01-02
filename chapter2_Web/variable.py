# variable.py

from flask import Flask
from flask import request
from flask import render_template
from datetime import datetime


app = Flask(__name__)

@app.route('/variable')
def variable():
	student = {'Stu_id':'8765432', 'name':'張三', 'Gender':'Male'}
	fruit = ['apple', 'banana', 'Gwava', 'Watermelon']
	return render_template('variable.html', **locals())

if __name__ == '__main__':
	app.run()
