import serial
import time
import msvcrt
import requests



from flask import request, Flask
from setuptools import setup

YO_API_TOKEN = '5da21321-c977-4643-ae5a-321bda4e3214'

prevSendPost = -1


print "opening serial port lol"
galileo = serial.Serial(4, 9600, timeout = 1)
time.sleep(.5)
while True:
	if (int) (galileo.readline()) == 1:
		if prevSendPost == -1:
			prevSendPost = 1
			requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN , 'username': 'NOTYHACK', 'link': 'http://google.com'})
			
	else:
		prevSendPost = -1
# app = Flask(__name__)

# @app.route("/")

# def yo():
# 	# username = request.args.get('username', '')
# 	# print "We got a Yo from " + username
	
# 	requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN , 'username': 'NOTYHACK', 'link': 'http://google.com'})
				
# 		# else:
# 		# 	sendPost = -1
# 		# 	prevSendPost = -1
		
# 	return 'OK'

# if __name__ == "__main__":
# 	app.run(host="127.0.0.1", port=3000);
	


# while True:
	# if int(galileo.readline()) == 1:
	# 	#if touch deteced
	# 	if prevSendPost == -1:
	# 		prevSendPost = 1
	# 		sendPost = 1
	# 	else:
	# 		sendPost = -1
	# else:
	# 	sendPost = -1
	# 	prevSendPost = -1