import serial
import time
import msvcrt
import requests
from flask import request, Flask
from setuptools import setup

YO_API_TOKEN = 'ia='
prevSendPost = -1
ENDUSER = 'NOTYHACK'
WAITTIME = 5 # number of seconds of time off pillow before another yo can be sent
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
		if int(time.clock() - t0) > WAITTIME: # send a yo if WAITTIME seconds have passed since the serial read last sensed touching
			requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN , 'username': ENDUSER, 'link': 'http://time.is'})		
		t0 = time.clock()

	if requests.get("http://72968c4.ngrok.com/sendnum") == 1:
		#alarm goes off here

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


