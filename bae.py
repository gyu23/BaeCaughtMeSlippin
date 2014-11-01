import serial
import time
import msvcrt
import requests
from flask import request, Flask
from setuptools import setup

YO_API_TOKEN = '5da21321-c977-4643-ae5a-321bda4e3214'
prevSendPost = -1
ENDUSER = 'NOTYHACK'
WAITTIME = 10 # number of seconds before another yo can be sent
#open serial port to communicate with galileo
print "opening serial port lol"
galileo = serial.Serial(4, 9600, timeout = 1)
time.sleep(.5) # brief pause to ensure port opened

#galileo sends back a serial stream of digital contact sensor information
#	if sensed: trigger a yo message: delay of 10 seconds before sending another yo
#	otherwise: do nothing
t0 = time.clock() - 11
prevIn = 0

while True:
	nextIn = int(float(galileo.readline()))
	if (nextIn == 1): # touch has been sensed
		if int(time.clock() - t0) > WAITTIME and prevIn == 0: # send a yo if WAITTIME seconds have passed and the last serial read sensed nothing
			t0 = time.clock()
			requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN , 'username': ENDUSER, 'link': 'http://time.is'})		
		prevIn = 1
	else:
		prevIn = 0

# jorge's crap below
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
