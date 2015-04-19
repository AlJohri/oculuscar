import os
from flask import Flask
from flask import request
app = Flask(__name__)

last_data = {}

@app.route('/', methods = ['POST'])
def test():
	global last_data
	last_data = dict(request.form)
	return str(last_data)

@app.route('/', methods = ['GET'])
def other_function():
	return str(last_data)


if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv('PORT', '5000')), host='0.0.0.0')
