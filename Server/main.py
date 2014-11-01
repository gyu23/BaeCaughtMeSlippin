import time
import requests
from flask import request, Flask
app = Flask(__name__)
fixedUsername = ""
@app.route("/")
def yo():
	print fixedUsername
	if len(request.args) > 0:
		username = request.args.get('username')
		return 1
	return 'OK'
	# if(username == None):
	# 	print "lol"
	# 	return fixedUsername
	# else:
	# 	print "yo from " + username
	# 	requests.post("http://72968c4.ngrok.com", data=username)
	# 	# fixedUsername = username
	# 	print fixedUsername
	# 	return username

if __name__ == "__main__":
    app.run(port=3000)
