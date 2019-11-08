from serial import *
from time import sleep
from requests import *

connect_flag = False

def get_com():
	try:
		res = get('http://127.0.0.1:5000/connect')
		return res.text
	except:
		res = -1
		return res

while connect_flag == False:
	
	com = str(get_com())

	try:
		ARM = Serial(com,9600)
		sleep(2)
		print('Done')
		connect_flag = True
	except:
		print('Error')

	sleep(3)

