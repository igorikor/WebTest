from flask import Flask,request,make_response

app = Flask(__name__)
com = ''

status = 0

#Запрос на подключение
@app.route('/connect', methods=['POST','GET'])
def get_com():
	if request.method == 'POST':
		global com
		com = request.form['com']
	if request.method == 'GET':
		return com
		com = ''
	return ("")

#Статус ардуинки
@app.route('/status', methods=['POST','GET'])
def set_status():
	if request.method == 'POST':
		global status
		status = request.form['status']
	if request.method == 'GET':
		return status
	return("")

app.run(debug=True)