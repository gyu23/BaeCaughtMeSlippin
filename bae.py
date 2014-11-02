# Keenan Albee, George Yu
# Yhack 11/1/2014
# Python code for No Sleep November
# Note: Port in line 21 may require modification

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
DELAY = 200
BAUD = 9600
#open serial port to communicate with galileo
print "opening serial port lol"
galileo = serial.Serial(5, BAUD, timeout = 1)
time.sleep(.5) # brief pause to ensure port opened

#galileo sends back a serial stream of digital contact sensor information
#	if sensed: trigger a yo message: delay of 10 seconds before sending another yo
#	otherwise: do nothing
t0 = time.clock() - 11
prevIn = 0
counter = 0
galileo.write('G') # light is on (indicates armed for sending)

while True:
	nextIn = int(float(galileo.readline()))
	
	if int(time.clock() - t0) > WAITTIME:
		galileo.write('G')

	if (nextIn == 1): # touch has been sensed
		if int(time.clock() - t0) > WAITTIME: # send a yo if WAITTIME seconds have passed since the serial read last sensed touching
			requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN , 'username': ENDUSER, 'link': "http://6257f35e.ngrok.com"})
			print "bae alert sent"	
			galileo.write('K') # light is off (indicates disarmed for sending)
		t0 = time.clock()
	if counter == DELAY:	
		counter = 0
		r = requests.get("http://6257f35e.ngrok.com/sendnum")
	# if requests.head("http://72968c4.ngrok.com/sendnum", allow_redirects=False):
		if int(r.text) == 0:
			print "bae alarm armed"
		elif int(r.text) == 1:
			galileo.write('H')
			print"on"
			time.sleep(2)
			galileo.write('L')
			print"off"
	counter += 1	
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
