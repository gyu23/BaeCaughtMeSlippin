import requests
from flask import request, Flask
YO_API_TOKEN = ''

app = Flask(__name__)

@app.route("/")

def yo():
	username = request.args.get('username', '')
	print "We got a Yo from " + username
	requests.post("http://api.justyo.co/yo/", data={'api_token': YO_API_TOKEN , 'username': username, 'link': 'http://google.com'})
	return 'OK'

if __name__ == "__main__":
	app.debug = True
	app.run(host="127.0.0.1", port=3000);