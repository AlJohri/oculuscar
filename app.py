import os
from flask import Flask
from flask import request
app = Flask(__name__)

last_data = dict([['servo', 0], ['left', 0], ['right', 0]])

@app.route('/', methods = ['POST'])
def test():
	global last_data
	temp = dict(request.form)
	if 'left' in temp:
		last_data['left'] = temp['left']
	if 'right' in temp:
		last_data['right'] = temp['right']
	if 'servo' in temp:
		last_data['servo'] = temp['servo']
	return str(last_data)

@app.route('/', methods = ['GET'])
def other_function():
	global last_data
	return str("*"+last_data['servo']+'F'+last_data['left'] + 'F' +last_data['right'])


if __name__ == "__main__":
    app.run(debug=True, port=int(os.getenv('PORT', '5000')), host='0.0.0.0')
