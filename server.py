from flask import Flask,request,make_response

app = Flask(__name__)

status = False

#Запрос на подключение
@app.route('/connect', methods=['POST'])
def get_com():
	com = request.get_data()
	print(com)
	return ("")

#Статус ардуинки
@app.route('/status', methods=['POST','GET'])
def set_status():
	if request.method == 'POST':
		if status != request.get_data():
			status = request.get_data()
	if request.method == 'GET':
		return status
	return("")

app.run(debug=True)