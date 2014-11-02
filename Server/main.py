import time
import requests
from flask import request, Flask
YO_API_TOKEN = '5da21321-c977-4643-ae5a-321bda4e3214'

app = Flask(__name__)
@app.route("/")

def yo():
	username = request.args.get('username')
	print "We got a Yo from " + username
	requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN , 'username': 'NOTYHACK', 'link': 'http://6257f35e.ngrok.com'})
	return 'OK'

if __name__ == "__main__":
	app.run(port=5000)

